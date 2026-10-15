"""Passive forward-only EV policy comparison; never modifies production picks."""
from datetime import timedelta
import hashlib
import json
import math

VERSION = 'conservative-ev-sensitivity-v1'
FLOORS = (0.015, 0.03, 0.05)
SELECTED = {'SHORTLISTED', 'SHORTLISTED_PROVISIONAL'}


def clean(table):
    # pandas serializes missing/nonfinite values as JSON null.
    return json.loads(table.to_json(orient='records', double_precision=15))


def write_experiment(predictions, raw, summary, production_decisions, reliability):
    from conservative_bet_filter import build_conservative_shortlist
    from quote_policy import load_policy
    from performance_tracking import utc, write_json
    rows = []
    for floor in FLOORS:
        decisions = production_decisions
        if floor != FLOORS[0]:
            _, decisions, _ = build_conservative_shortlist(predictions,
                as_of=utc(summary['generated_at_utc']), market_reliability=reliability,
                adjusted_ev_floor=floor)
        rows.extend({**r, 'ev_floor': floor} for r in clean(decisions))
    data = {'version': VERSION, 'generated_at_utc': summary['generated_at_utc'],
        'selection_policy_version': summary['selection_policy_version'],
        'execution_policy': load_policy(), 'floors': list(FLOORS),
        'predictions_sha256': hashlib.sha256((raw/'all_leagues_predictions.csv').read_bytes()).hexdigest(),
        'rows': rows}
    write_json(raw/'filter_sensitivity_experiment.json', data)
    return data


def validate(data, generated, predictions):
    from performance_tracking import utc, fixture_key, number
    from conservative_bet_filter import MARKET_SPECS, _market_fields
    if not isinstance(data,dict):
        raise ValueError('Invalid filter experiment document')
    if data.get('version') != VERSION or data.get('floors') != list(FLOORS):
        raise ValueError('Invalid filter experiment version/grid')
    if utc(generated) is None or utc(data.get('generated_at_utc')) is None or abs((utc(generated)-utc(data['generated_at_utc'])).total_seconds()) >= 1:
        raise ValueError('Unbound filter experiment generation time')
    originals = {fixture_key(r):r for r in predictions}
    fixtures = set(originals)
    specs = {r[0]:r[1] for r in MARKET_SPECS}
    # Validate immutable captures using their original market set.
    if data.get("selection_policy_version") in {"72h-all-markets-net-ev15-execution-v7",
                                              "72h-five-markets-probability-odds-net-ev15-v8"}:
        specs.pop("Double Chance 12", None)
    if data.get("selection_policy_version") == "72h-all-markets-net-ev15-execution-v7":
        specs["Both Teams to Score - Yes"] = "btts_yes"
    markets = set(specs)
    expected = {(key, market, floor) for key in fixtures for market in markets for floor in FLOORS}
    seen = set()
    controls = {}
    for row in data.get('rows', []):
        if not isinstance(row,dict):raise ValueError('Invalid candidate row')
        key = (fixture_key(row), row.get('market'), row.get('ev_floor'))
        if key not in expected or key in seen or row.get('decision') not in {'REJECTED','NOT_SELECTED',*SELECTED}:
            raise ValueError('Invalid/duplicate candidate decision')
        seen.add(key)
        original = originals[key[0]]; market_key = specs[row['market']]
        for field,source in (('predicted_probability','p_'),('raw_dc_probability','raw_p_'),('market_probability','market_p_')):
            expected_p=number(original.get(source+market_key),min_value=0,max_value=1)
            actual_p=number(row.get(field),min_value=0,max_value=1)
            if (expected_p is None)!=(actual_p is None) or (expected_p is not None and abs(expected_p-actual_p)>1e-9):
                raise ValueError('Candidate probability differs from forecast')
        p=number(row.get('predicted_probability'),min_value=0,max_value=1)
        penalty=number(row.get('calibration_penalty'),min_value=0,max_value=1)
        rank=number(row.get('rank_probability'),min_value=0,max_value=1)
        if p is not None and (penalty is None or rank is None or abs(max(0,p-penalty)-rank)>1e-9):
            raise ValueError('Invalid reliability adjustment')
        # EV floor is the only experimental input. All other evidence must agree.
        changing={'ev_floor','decision','rejection_reasons','selection_tier','near_miss_reason','historical_gap_score'}
        common={k:v for k,v in row.items() if k not in changing}
        old=controls.setdefault(key[:2],common)
        if common!=old:raise ValueError('Policies use different candidate evidence')
        if row['decision'] in SELECTED:
            p = number(row.get('rank_probability'), min_value=0, max_value=1)
            odds = number(row.get('offered_decimal_odds'), min_value=1.000001)
            cost = number(row.get('per_stake_cost'), min_value=0, max_value=1)
            ev = number(row.get('conservative_estimated_ev'))
            if None in (p, odds, cost, ev) or abs(p*odds-1-cost-ev)>1e-9 or ev+1e-12<row['ev_floor']:
                raise ValueError('Invalid selected net EV')
            fields=_market_fields(original,market_key)
            original_price=number(fields['price'],min_value=1.000001)
            if original_price is None or abs(original_price-odds)>1e-9 or fields['bookmaker']!=row.get('bookmaker'):
                raise ValueError('Selected price/bookmaker differs from forecast')
            from quote_policy import usable_bookmaker
            policy=data.get('execution_policy',{})
            if not usable_bookmaker(row.get('bookmaker'),policy) or abs(cost-policy['per_stake_cost_bps']/10000)>1e-9:
                raise ValueError('Invalid selected execution policy')
            if row.get('selection_tier') != ('STRICT' if row['decision']=='SHORTLISTED' else 'PROVISIONAL'):
                raise ValueError('Invalid selection tier')
    if seen != expected:
        raise ValueError('Missing candidate decisions')
    for floor in FLOORS:
        selected = [r for r in data['rows'] if r['ev_floor']==floor and r['decision'] in SELECTED]
        if len(selected)>10 or len({fixture_key(r) for r in selected})!=len(selected):
            raise ValueError('Duplicate fixture or policy cap exceeded')


def validate_control(data, picks):
    from performance_tracking import fixture_key
    actual={(fixture_key(r),r['market'],r.get('selection_tier')) for r in picks}
    control={(fixture_key(r),r['market'],r.get('selection_tier')) for r in data['rows']
             if r['ev_floor']==FLOORS[0] and r['decision'] in SELECTED}
    if actual != control:
        raise ValueError('1.5% control differs from production shortlist')


def capture_file(raw, generated):
    from performance_tracking import load_json, read_csv
    from forecast_integrity import forecast_digest_variants
    path = raw/'filter_sensitivity_experiment.json'
    if not path.exists():
        return None
    data = load_json(path, {})
    validate(data, generated, read_csv(raw/'all_leagues_predictions.csv'))
    validate_control(data,read_csv(raw/'conservative_bet_shortlist.csv'))
    if data.get('predictions_sha256') not in forecast_digest_variants(raw/'all_leagues_predictions.csv'):
        raise ValueError('Filter experiment forecast hash mismatch')
    return path


def frozen(root, archived):
    from performance_tracking import load_json, utc, fixture_key
    from forecast_integrity import forecast_digest_variants
    rows = []; seen = set(); rejected = []
    for meta, predictions, picks in archived:
        directory = root/'performance/snapshots'/meta['git_commit_sha'][:16]
        path = directory/'filter_sensitivity_experiment.json'
        digest = meta.get('sha256',{}).get(path.name)
        if not digest:
            continue
        try:
            if not path.exists() or hashlib.sha256(path.read_bytes()).hexdigest()!=digest:
                raise ValueError('Invalid archived experiment hash')
            data = load_json(path,{})
            validate(data,meta['generated_at_utc'],predictions)
            validate_control(data,picks)
            if data['selection_policy_version']!=meta['selection_policy_version']:
                raise ValueError('Unbound production policy version')
            if data.get('predictions_sha256') not in forecast_digest_variants(directory/'predictions.csv'):
                raise ValueError('Unbound archived forecast')
        except (ValueError, TypeError, KeyError):
            rejected.append(meta['git_commit_sha']); continue
        # Freeze the whole first eligible fixture decision set, including rejected markets.
        new = set()
        for row in data['rows']:
            key = fixture_key(row); kick = utc(row.get('kickoff_utc'))
            if key in seen or kick is None or max(utc(meta['captured_at_utc']),utc(meta['generated_at_utc'])) > kick-timedelta(minutes=20):
                continue
            if kick > utc(meta['generated_at_utc'])+timedelta(hours=72):
                continue
            new.add(key)
            rows.append({**row,'fixture_key':key,'snapshot_commit':meta['git_commit_sha'],
                'snapshot_captured_utc':meta['captured_at_utc'],
                'selection_policy_version':data['selection_policy_version']})
        seen.update(new)
    return rows, rejected


def statistics(rows):
    settled = sorted([r for r in rows if r['outcome'] is not None],
                     key=lambda r:(r['kickoff_utc'],r['fixture_key']))
    n = len(settled); profit = sum(r['unit_profit'] for r in settled)
    cumulative = peak = drawdown = 0.0
    # Settle simultaneous kickoffs together: avoid arbitrary ordering within a batch.
    for kick in sorted({r['kickoff_utc'] for r in settled}):
        cumulative += sum(r['unit_profit'] for r in settled if r['kickoff_utc']==kick)
        peak = max(peak,cumulative); drawdown=max(drawdown,peak-cumulative)
    bins=[]
    for low,high in ((0,.6),(.6,.7),(.7,.8),(.8,.9),(.9,1.000001)):
        group=[r for r in settled if low<=r['rank_probability']<high]
        if group:
            bins.append({'band':f'{low:.0%}-{min(high,1):.0%}','n':len(group),
                'mean_probability':sum(r['rank_probability'] for r in group)/len(group),
                'observed_rate':sum(r['outcome'] for r in group)/len(group)})
    return {'selected':len(rows),'graded':n,'pending':len(rows)-n,
        'wins':sum(r['outcome'] for r in settled),'profit_units':profit,
        'flat_stake_roi':profit/n if n else None,'max_drawdown_units':drawdown if n else None,
        'brier':sum(r['brier'] for r in settled)/n if n else None,
        'mean_probability':sum(r['rank_probability'] for r in settled)/n if n else None,
        'observed_rate':sum(r['outcome'] for r in settled)/n if n else None,
        'calibration':bins,'assessment':'COLLECT_MORE_DATA' if n<30 else 'REVIEW_ON_LATER_HOLDOUT'}


def evaluate(root, archived, records, clock):
    from performance_tracking import utc, fixture_match, result_for_market
    records=[r for r in records if r.get('source_status')=='FINISHED' and r.get('source')=='football-data.org/v4']
    candidates,rejected=frozen(root,archived); selections=[];coverage=[]
    for row in candidates:
        match,state=fixture_match(row,records)
        if utc(row['kickoff_utc'])>clock-timedelta(hours=2):
            match=None;state='PENDING_KICKOFF_OR_FINAL_SCORE'
        outcome=int(result_for_market(row['market'],match['home_goals'],match['away_goals'])) if match else None
        p=row.get('rank_probability')
        coverage.append({**row,'result_status':state,'outcome':outcome,
            'source_match_id':match['match_id'] if match else None,
            'brier':(p-outcome)**2 if p is not None and outcome is not None else None})
        if row['decision'] in SELECTED:
            selections.append({**coverage[-1], 'unit_profit':
                outcome*row['offered_decimal_odds']-1-row['per_stake_cost'] if outcome is not None else None})
    comparisons=[]
    for floor in FLOORS:
        cohort=[r for r in selections if r['ev_floor']==floor]
        for tier in ('ALL','STRICT','PROVISIONAL'):
            comparisons.append({'ev_floor':floor,'tier':tier,
                **statistics([r for r in cohort if tier=='ALL' or r['selection_tier']==tier])})
    breakdown=[]
    for field in ('league','market','week','selection_policy_version'):
        for row in selections:
            if field=='week':
                year,week,_=utc(row['kickoff_utc']).isocalendar(); row['week']=f'{year}-W{week:02d}'
        for value in sorted({r[field] for r in selections}):
            for floor in FLOORS:
                breakdown.append({'dimension':field,'value':value,'ev_floor':floor,
                    **statistics([r for r in selections if r[field]==value and r['ev_floor']==floor])})
    summary={'version':VERSION,'reviewed_at_utc':clock.isoformat(),
        'total_fixtures':len({r['fixture_key'] for r in candidates}),
        'candidate_decisions':len(candidates),'comparisons':comparisons,'breakdowns':breakdown,
        'rejected_snapshot_commits':rejected,
        'note':'One unit per simulated selection, net of frozen costs; simultaneous kickoff P&L grouped for drawdown. First eligible fixture snapshot freezes all policies and rejections. Different policies may select different markets/cohorts; results are not paired probability tests. Four weeks or 30 selections do not establish profitability. No automatic promotion; validate a chosen policy on later untouched data.'}
    return summary,selections,coverage


def review_experiment(root, archived, records, clock):
    from performance_tracking import write_json,write_csv
    summary,selections,coverage=evaluate(root,archived,records,clock)
    dest=root/'performance/filter_sensitivity_experiment'
    write_json(dest/'summary.json',summary)
    for name,rows in [('selections',selections),('candidate_decisions',coverage)]:
        write_csv(dest/(name+'.csv'),rows,list(rows[0]) if rows else ['fixture_key','ev_floor','decision','outcome'])
    lines=['# Conservative EV sensitivity experiment','',summary['note'],'',
        f"Frozen fixtures: {summary['total_fixtures']}; candidate decisions: {summary['candidate_decisions']}; rejected snapshots: {len(summary['rejected_snapshot_commits'])}.",'',
        '| EV floor | Tier | Selected | Settled | Pending | Net ROI | Drawdown (units) | Brier |',
        '|---|---|---:|---:|---:|---:|---:|---:|']
    for r in summary['comparisons']:
        roi=f"{r['flat_stake_roi']:+.1%}" if r['flat_stake_roi'] is not None else 'n.a.'
        dd=f"{r['max_drawdown_units']:.2f}" if r['max_drawdown_units'] is not None else 'n.a.'
        brier=f"{r['brier']:.4f}" if r['brier'] is not None else 'n.a.'
        lines.append(f"| {r['ev_floor']:.1%} | {r['tier']} | {r['selected']} | {r['graded']} | {r['pending']} | {roi} | {dd} | {brier} |")
    lines+=['','Calibration buckets, league/market/gameweek/policy breakdowns and all rejected candidates are in summary.json and candidate_decisions.csv. Older snapshots are not backfilled. Upload fresh outputs before kickoff; reporting runs in the existing forward-review workflow.','']
    (dest/'report.md').write_text('\n'.join(lines),encoding='utf-8')
    return summary


def validate_report(root):
    from performance_tracking import load_json,snapshots,utc,read_csv
    dest=root/'performance/filter_sensitivity_experiment'
    actual=load_json(dest/'summary.json',{})
    cache=load_json(root/'performance/verified_results.json',{})
    # Same cache representation used by the existing forward-review validators.
    records=list(cache.values())
    expected,selections,coverage=evaluate(root,snapshots(root),records,utc(actual['reviewed_at_utc']))
    if actual != expected:
        raise ValueError('Filter sensitivity summary differs from frozen evidence')
    for name,rows in [('selections',selections),('candidate_decisions',coverage)]:
        saved=read_csv(dest/(name+'.csv'))
        if len(saved)!=len(rows):raise ValueError('Incomplete filter sensitivity ledger')
        for a,b in zip(saved,rows):
            for key,value in b.items():
                if value is None:
                    if a.get(key) not in ('',None):raise ValueError('Unexpected ledger value')
                elif isinstance(value,(int,float)):
                    if not math.isfinite(float(a[key])) or abs(float(a[key])-value)>1e-9:raise ValueError('Inconsistent ledger number')
                elif str(value)!=a.get(key):raise ValueError('Inconsistent ledger decision')
    return True


