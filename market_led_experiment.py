"""Opt-in, forward-only market-led double-chance research. No production writes."""
from __future__ import annotations

from collections import Counter, defaultdict
from datetime import datetime, timedelta, timezone
import hashlib
import json
import math
import re
from pathlib import Path

VERSION = 'market-led-dc-v1'
FILE = 'market_led_experiment.json'
MARKETS = {'home_draw': 'Double Chance 1X', 'draw_away': 'Double Chance X2'}


def settings(max_age_minutes=10., max_skew_minutes=5., cost_bps=0.):
    values = (max_age_minutes, max_skew_minutes, cost_bps)
    if not all(math.isfinite(v) for v in values) or not (
        0 < max_age_minutes <= 60 and 0 <= max_skew_minutes <= max_age_minutes
        and 0 <= cost_bps < 10000
    ):
        raise ValueError('Invalid market-led freshness, skew or cost settings')
    return dict(reference='pinnacle', devig='power', max_age_minutes=max_age_minutes,
                max_skew_minutes=max_skew_minutes, cost_bps=cost_bps,
                min_probability=.80, min_ev=.03, settlement='regulation_time',
                promotion='disabled', selection='one market per fixture; at most ten fixtures')


def fresh(value, clock, cfg):
    from performance_tracking import utc
    stamp = utc(value)
    return stamp is not None and 0 <= (clock-stamp).total_seconds() <= cfg['max_age_minutes']*60


def fetch_event(api, league, event_id):
    from football_value_pipeline_v2_standalone import THE_ODDS_API_BASE
    if not re.fullmatch(r'[A-Za-z0-9_-]+', str(event_id)):
        raise ValueError('Invalid event ID')
    region = re.sub(r'[^a-z0-9]+', '_', api.regions.lower())
    return api._get_json(
        f'{THE_ODDS_API_BASE}/sports/{league.odds_api_sport_key}/events/{event_id}/odds',
        f'oddsapi_market_led_v1_{league.key}_{region}_{event_id}.json',
        ttl=timedelta(minutes=1), force_refresh=api.force_refresh, allow_stale=False,
        params={'apiKey': api.api_key, 'regions': api.regions,
                'markets': 'h2h,double_chance', 'oddsFormat': 'decimal', 'dateFormat': 'iso'})


def evaluate(source, payload, clock, cfg, error=None):
    """Same-event, same-period comparison; target offers must exclude Pinnacle."""
    from football_value_pipeline_v2_standalone import canonical_team_key, devig
    from performance_tracking import utc, number
    from double_chance import parse_quotes
    kick = utc(source.get('kickoff_utc'))
    reasons = []
    if kick is None or not 20*60 <= (kick-clock).total_seconds() <= 72*3600:
        reasons.append('outside_selection_window')
    if source.get('odds_source') != 'The Odds API' or not source.get('odds_event_id'):
        reasons.append('unlinked_fixture')
    if error: reasons.append(error)
    payload = payload if isinstance(payload, dict) else {}
    event_kick = utc(payload.get('commence_time'))
    if (str(payload.get('id')) != str(source.get('odds_event_id')) or not kick or
            not event_kick or abs((event_kick-kick).total_seconds()) > 60 or
            any(canonical_team_key(str(payload.get(p,''))) != canonical_team_key(str(source.get(s,'')))
                for p,s in [('home_team','home_team'),('away_team','away_team')])):
        reasons.append('event_identity_or_kickoff_mismatch')
    books = payload.get('bookmakers', [])
    books = [b for b in books if isinstance(b, dict)] if isinstance(books,list) else []
    refs = []
    for book in books:
        if book.get('key') != 'pinnacle': continue
        markets = book.get('markets')
        if not isinstance(markets,list): continue
        for market in markets:
            if not isinstance(market, dict) or market.get('key') != 'h2h': continue
            outcomes = market.get('outcomes', [])
            if not isinstance(outcomes,list) or len(outcomes) != 3: continue
            prices = {}
            for o in outcomes:
                if not isinstance(o,dict) or o.get('point') is not None: continue
                name = str(o.get('name',''))
                key = 'draw' if name.lower() == 'draw' else (
                    'home' if name == payload.get('home_team') else
                    'away' if name == payload.get('away_team') else None)
                price = number(o.get('price'), min_value=1.000001)
                if key and price is not None and key not in prices: prices[key] = price
            stamp = market.get('last_update') or book.get('last_update')
            if set(prices) == {'home','draw','away'} and .98 <= sum(1/p for p in prices.values()) <= 1.20:
                if fresh(stamp,clock,cfg): refs.append((stamp, prices))
    ref = max(refs, key=lambda r:r[0]) if refs else None
    if not ref: reasons.append('missing_invalid_or_stale_pinnacle_1x2')
    probabilities = None
    if ref:
        h,d,a = devig([ref[1][k] for k in ('home','draw','away')], method='power')
        probabilities = dict(home_draw=h+d, draw_away=d+a)
    offers = defaultdict(list)
    for book in books:
        if not book.get('key') or book['key'] == 'pinnacle': continue
        if book['key'].startswith('betfair_ex') or book['key'] == 'matchbook': continue
        # Parse each bookmaker independently so reference and target never mix.
        parsed = parse_quotes({**payload, 'bookmakers':[book]})
        for key in MARKETS:
            price = parsed.get(f'market_{key}_odds')
            stamp = parsed.get(f'market_best_{key}_last_update_utc')
            if price and fresh(stamp,clock,cfg) and ref and abs((utc(stamp)-utc(ref[0])).total_seconds()) <= cfg['max_skew_minutes']*60:
                offers[key].append((price,book['key'],book.get('title',book['key']),stamp))
    rows = []
    for key in MARKETS:
        gaps = list(reasons)
        best = max(offers[key], default=None)
        if best is None: gaps.append('no_fresh_independent_complete_dc_offer')
        p = probabilities[key] if probabilities else None
        price = best[0] if best else None
        cost = cfg['cost_bps']/10000
        ev = p*price-1-cost if p is not None and price is not None else None
        base = number(source.get('p_'+key), min_value=0, max_value=1)
        raw = number(source.get('raw_p_'+key), min_value=0, max_value=1)
        selection_reasons = list(gaps)
        if len({x[1] for x in offers[key]}) < 2:
            selection_reasons.append('insufficient_independent_bookmaker_coverage')
        if p is not None and p < cfg['min_probability']: selection_reasons.append('below_probability_threshold')
        if ev is not None and ev < cfg['min_ev']: selection_reasons.append('below_ev_threshold')
        rows.append({**{k:source.get(k) for k in ('league','home_team','away_team','kickoff_utc','fixture_id','odds_event_id')},
            'policy_settings':dict(cfg),
            'market':key, 'generated_at_utc':clock.isoformat(), 'status':'unavailable' if gaps else 'available',
            'reasons':gaps, 'selection_reasons':selection_reasons, 'qualifies':not selection_reasons,
            'selected':False, 'reference_bookmaker':'pinnacle', 'reference_probability':p,
            'reference_odds':ref[1] if ref else None, 'reference_updated_at_utc':ref[0] if ref else None,
            'baseline_probability':base, 'raw_probability':raw,
            'model_minus_reference':base-p if base is not None and p is not None else None,
            'decimal_odds':price, 'bookmaker_key':best[1] if best else None,
            'bookmaker':best[2] if best else None, 'quote_updated_at_utc':best[3] if best else None,
            'independent_bookmaker_count':len({x[1] for x in offers[key]}),
            'estimated_ev_after_cost':ev, 'cost_per_unit':cost,
            'execution_status':'unverified_feed_quote'})
    return rows


def write_experiment(predictions, raw: Path, baseline_generated, api, cfg):
    from football_value_pipeline_v2_standalone import LEAGUES
    from performance_tracking import utc, write_csv
    by_name = {v.name:v for v in LEAGUES.values()}
    from conservative_bet_filter import SUPPORTED_LEAGUES
    rows, evidence = [], []
    for source in predictions.astype(object).where(predictions.notna(),None).to_dict('records'):
        clock = datetime.now(timezone.utc)
        kick = utc(source.get('kickoff_utc'))
        payload, error = {}, None
        if source.get('league') not in SUPPORTED_LEAGUES:
            # Unvalidated competitions never qualify; spend no event-odds credits on them.
            error = 'competition_excluded_from_shortlist_validation'
        elif kick and 20*60 <= (kick-clock).total_seconds() <= 72*3600 and source.get('odds_event_id'):
            try:
                if api is None: error = 'api_unavailable'
                else: payload = fetch_event(api,by_name[source['league']],source['odds_event_id'])
            except Exception as exc:
                error = 'request_failed_'+type(exc).__name__  # Never persist credential-bearing exception text.
        clock = datetime.now(timezone.utc)
        payload = payload if isinstance(payload,dict) else {}
        rows.extend(evaluate(source,payload,clock,cfg,error))
        # Raw response evidence contains offered prices, no request URL or credentials.
        evidence.append({'event_id':source.get('odds_event_id'), 'retrieved_at_utc':clock.isoformat(), 'response':payload})
    seen = set()
    for row in sorted((r for r in rows if r['qualifies']), key=lambda r:(-r['reference_probability'],-r['estimated_ev_after_cost'],str(r['odds_event_id']),r['market'])):
        key = (row['league'],row['odds_event_id'])
        if key in seen or len(seen)>=10: continue
        seen.add(key); row['selected']=True
    data = {'version':VERSION, 'baseline_generated_at_utc':baseline_generated,
            'generated_at_utc':datetime.now(timezone.utc).isoformat(), 'settings':cfg,
            'predictions_sha256':hashlib.sha256((raw/'all_leagues_predictions.csv').read_bytes()).hexdigest(),
            'rows':rows, 'quote_evidence':evidence}
    (raw/FILE).write_text(json.dumps(data,indent=2,allow_nan=False)+'\n',encoding='utf-8')
    columns = list(rows[0]) if rows else ['league','market','selected','reasons']
    write_csv(raw/'market_led_candidates.csv',rows,columns)
    write_csv(raw/'market_led_shortlist.csv',[r for r in rows if r['selected']],columns)
    counts = Counter(reason for r in rows for reason in r['reasons'])
    (raw/'market_led_report.md').write_text(
        '# Market-led double-chance experiment\n\nResearch only; feed prices are not confirmed executable bets.\n\n'
        f'Candidate markets: {len(rows)}; available: {sum(r["status"]=="available" for r in rows)}; selected: {sum(r["selected"] for r in rows)}.\n\n'
        + '\n'.join(f'- {key}: {value}' for key,value in sorted(counts.items()))
        + '\n\nNo automatic promotion. Existing model and conservative shortlist are unchanged.\n',encoding='utf-8')
    return data


def capture_file(raw, baseline_generated):
    from performance_tracking import load_json
    path = raw/FILE
    if not path.exists(): return None
    data = load_json(path,{})
    from forecast_integrity import forecast_digest_variants
    digests = forecast_digest_variants(raw/'all_leagues_predictions.csv')
    if data.get('version') == VERSION and data.get('baseline_generated_at_utc') == baseline_generated and data.get('predictions_sha256') in digests:
        return path
    return None


def review_experiment(root, archived, records, clock):
    from performance_tracking import load_json, utc, fixture_key, fixture_match, result_for_market, write_json, write_csv
    frozen, closing = {}, {}
    for meta,_,_ in sorted(archived,key=lambda x:x[0]['captured_at_utc']):
        path = root/'performance'/'snapshots'/meta['git_commit_sha'][:16]/FILE
        digest = meta.get('sha256',{}).get(FILE)
        if not digest or not path.exists() or hashlib.sha256(path.read_bytes()).hexdigest()!=digest: continue
        data = load_json(path,{})
        if data.get('version') != VERSION: continue
        for row in data.get('rows',[]):
            kick,generated,captured = utc(row.get('kickoff_utc')),utc(row.get('generated_at_utc')),utc(meta.get('captured_at_utc'))
            if not all((kick,generated,captured)) or generated>captured or max(generated,captured)>kick-timedelta(minutes=20): continue
            key = (fixture_key(row),row['market'])
            # Freeze first observation, including missing quotes; never select retrospectively.
            frozen.setdefault(key,{**row,'snapshot_commit':meta['git_commit_sha']})
            stamp = utc(row.get('reference_updated_at_utc'))
            if stamp and kick-timedelta(minutes=60)<=stamp<=generated and row.get('reference_probability') is not None:
                if key not in closing or stamp>utc(closing[key]['reference_updated_at_utc']): closing[key]=row
    if not frozen: return
    scored, groups, bets = [], defaultdict(list), []
    for key,row in frozen.items():
        match,state = fixture_match(row,records)
        if row['status']!='available' or match is None or utc(row['kickoff_utc'])>clock-timedelta(hours=2): continue
        outcome = int(result_for_market(MARKETS[row['market']],match['home_goals'],match['away_goals']))
        variants = {'market':row['reference_probability'],'baseline':row.get('baseline_probability'),'raw':row.get('raw_probability')}
        # Paired forecast comparison only when all three probabilities exist.
        if all(p is not None for p in variants.values()):
            for variant,p in variants.items():
                clipped = min(1-1e-12,max(1e-12,p))
                r = {k:row[k] for k in ('league','home_team','away_team','kickoff_utc','market','snapshot_commit')}
                r.update(variant=variant,probability=p,outcome=outcome,brier=(p-outcome)**2,
                         log_loss=-outcome*math.log(clipped)-(1-outcome)*math.log(1-clipped))
                scored.append(r); groups[(row['market'],variant)].append(r)
        if row['selected']:
            close = closing.get(key)
            proxy = None
            if close and utc(close['reference_updated_at_utc'])>utc(row['generated_at_utc']):
                proxy = row['decimal_odds']*close['reference_probability']-1-row['cost_per_unit']
            bets.append({**row,'outcome':outcome,'flat_unit_pnl':outcome*row['decimal_odds']-1-row['cost_per_unit'],
                         'late_reference_value_proxy':proxy,
                         'late_reference_updated_at_utc':close['reference_updated_at_utc'] if proxy is not None else None})
    comparisons=[]
    calibration=[]
    for (market,variant),items in sorted(groups.items()):
        n=len(items)
        comparisons.append(dict(market=market,variant=variant,n=n,
            brier=sum(r['brier'] for r in items)/n,log_loss=sum(r['log_loss'] for r in items)/n,
            mean_probability=sum(r['probability'] for r in items)/n,event_rate=sum(r['outcome'] for r in items)/n))
        for bucket in range(10):
            subset=[r for r in items if min(9,int(r['probability']*10))==bucket]
            if subset: calibration.append(dict(market=market,variant=variant,bin_lower=bucket/10,n=len(subset),
                mean_probability=sum(r['probability'] for r in subset)/len(subset),event_rate=sum(r['outcome'] for r in subset)/len(subset)))
    selected=sum(r['selected'] for r in frozen.values())
    summary={'version':VERSION,'reviewed_at_utc':clock.isoformat(),'decision':'INCONCLUSIVE_NO_AUTOMATIC_PROMOTION',
        'observed_fixture_markets':len(frozen),'available_fixture_markets':sum(r['status']=='available' for r in frozen.values()),
        'settings_observed':[json.loads(value) for value in sorted({json.dumps(r.get('policy_settings',{}),sort_keys=True) for r in frozen.values()})],
        'missing_reasons':dict(Counter(reason for r in frozen.values() for reason in r['reasons'])),
        'paired_graded_fixture_markets':len(scored)//3,'comparisons':comparisons,'calibration':calibration,
        'selected':selected,'graded_selections':len(bets),'pending_or_unverified_selections':selected-len(bets),
        'flat_unit_roi_after_configured_cost':sum(r['flat_unit_pnl'] for r in bets)/len(bets) if bets else None,
        'late_reference_proxy_count':sum(r['late_reference_value_proxy'] is not None for r in bets),
        'note':'Paper results at feed odds, not realized returns. Costs are user-configured per stake. Late reference proxy uses only archived quotes 20–60 minutes before kickoff; not actual closing odds. No automatic collection at close or promotion.'}
    dest=root/'performance'/'market_led_experiment'
    write_json(dest/'summary.json',summary)
    write_csv(dest/'graded_probabilities.csv',scored,list(scored[0]) if scored else ['market','variant','outcome'])
    write_csv(dest/'graded_selections.csv',bets,list(bets[0]) if bets else ['market','outcome','flat_unit_pnl'])
    lines=['# Market-led forward review','',summary['note'],'',
           f'Selected: {selected}; graded: {len(bets)}; paired forecast samples: {len(scored)//3}.',
           '',f'Paper ROI after configured costs: {summary["flat_unit_roi_after_configured_cost"]}',
           '', '| Market | Variant | N | Brier | Log loss | Mean probability | Event rate |',
           '|---|---|---:|---:|---:|---:|---:|']
    for r in comparisons:
        lines.append(f'| {r["market"]} | {r["variant"]} | {r["n"]} | {r["brier"]:.4f} | {r["log_loss"]:.4f} | {r["mean_probability"]:.1%} | {r["event_rate"]:.1%} |')
    lines += ['', 'Decision: inconclusive; no automatic promotion.']
    (dest/'report.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
