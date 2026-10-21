"""Full-time Asian goal handicaps: exact split settlement and loss-first selection.

Probabilities are model estimates, never guarantees. Use the entire score grid;
exported top-score lists are deliberately insufficient for this market.
"""
import json
import math
import re

import numpy as np
import pandas as pd

from quote_freshness import quote_is_fresh

LEGACY_POLICY = '48h-loss-first-asian-handicap-1x2-over15-v17'
FLOORLESS_POLICY = '48h-loss-first-asian-handicap-1x2-over15-v18'
ZERO_EV_POLICY = '48h-risk-band-ev-asian-handicap-1x2-over15-v19'
PREVIOUS_POLICY = '48h-risk-band-ev1-asian-handicap-1x2-over15-v20'
POLICY = '48h-risk-band-ev1-asian-handicap-dc-over15-v21'
ONE_PERCENT_POLICIES = (PREVIOUS_POLICY, POLICY)
RISK_BAND_POLICIES = (ZERO_EV_POLICY, *ONE_PERCENT_POLICIES)
POLICIES = (LEGACY_POLICY, FLOORLESS_POLICY, *RISK_BAND_POLICIES)
MIN_ADJUSTED_EV = .01
DEFAULT_RISK_TOLERANCE = .01
VERSION = 'asian-handicap-loss-first-v1'
LINES = tuple(i/4 for i in range(-12, 13))
OUTCOMES = ('full_win', 'half_win', 'refund', 'half_loss', 'full_loss')
SETTLED = ('WON', 'HALF_WON', 'REFUNDED', 'HALF_LOST', 'LOST')
FIELDS = ['handicap_side', 'handicap_line', 'p_full_win', 'p_half_win', 'p_refund',
          'p_half_loss', 'p_full_loss', 'p_no_loss', 'p_any_loss', 'raw_p_no_loss',
          'loss_probability_upper', 'probability_basis', 'asian_handicap_validation',
          'quote_source', 'quote_last_update_utc', 'opposite_decimal_odds']


def line(value):
    if isinstance(value, bool):
        raise ValueError('Invalid Asian handicap line')
    value = float(value)
    if not math.isfinite(value) or value not in LINES:
        raise ValueError('Asian goal handicap must be a quarter line between -3 and +3')
    return 0.0 if value == 0 else value


def label(side, point):
    if side not in ('home', 'away'):
        raise ValueError('Unknown handicap side')
    return f'Asian Handicap {side.title()} {line(point):+.2f}'


def parse_label(value):
    match = re.fullmatch(r'Asian Handicap (Home|Away) ([+-]\d+\.\d{2})', str(value))
    if not match:
        return None
    try:
        return match[1].lower(), line(match[2])
    except ValueError:
        return None


def components(point):
    point = line(point)
    return (point, point) if round(point*4) % 2 == 0 else (point-.25, point+.25)


def settlement(margin, point):
    """Return the fraction of stake won and lost; the remainder is refunded."""
    values = [margin+p for p in components(point)]
    return sum(v > 0 for v in values)/2, sum(v < 0 for v in values)/2


def profit(home, away, side, point, price, cost=0):
    if side not in ('home', 'away') or not math.isfinite(float(price)) or float(price) <= 1:
        raise ValueError('Invalid handicap settlement')
    w, lost = settlement((home-away)*(1 if side == 'home' else -1), point)
    status = {(1., 0.): 'WON', (.5, 0.): 'HALF_WON', (0., 0.): 'REFUNDED',
              (0., .5): 'HALF_LOST', (0., 1.): 'LOST'}[(w, lost)]
    return status, w*(float(price)-1)-lost-float(cost)


def margins(matrix):
    from score_probability import valid_matrix
    matrix = valid_matrix(matrix)
    if matrix.shape[0] != matrix.shape[1] or abs(matrix.sum()-1) > 1e-8:
        raise ValueError('Unnormalized full score grid')
    n = matrix.shape[0]-1
    return json.dumps({str(d): float(np.diagonal(matrix, offset=-d).sum())
                       for d in range(-n, n+1)}, sort_keys=True, allow_nan=False)


def distribution(value):
    data = json.loads(value) if isinstance(value, str) else value
    if not isinstance(data, dict) or not data:
        raise ValueError('Missing full goal-margin distribution')
    result = {}
    for key, prob in data.items():
        d, p = int(key), float(prob)
        if str(d) != str(key) or not math.isfinite(p) or not 0 <= p <= 1:
            raise ValueError('Invalid goal-margin distribution')
        result[d] = p
    if abs(sum(result.values())-1) > 1e-8:
        raise ValueError('Incomplete goal-margin distribution')
    return result


def probabilities(value, side, point, price, cost=0):
    if side not in ('home', 'away'):
        raise ValueError('Invalid handicap side')
    if not math.isfinite(float(price)) or price <= 1 or not math.isfinite(float(cost)) or not 0 <= cost <= 1:
        raise ValueError('Invalid handicap price or cost')
    result = dict.fromkeys(OUTCOMES, 0.)
    no_loss, ev = 0., 0.
    for margin, p in distribution(value).items():
        w, lost = settlement(margin*(1 if side == 'home' else -1), point)
        kind = {(1., 0.): 'full_win', (.5, 0.): 'half_win', (0., 0.): 'refund',
                (0., .5): 'half_loss', (0., 1.): 'full_loss'}[(w, lost)]
        result[kind] += p
        net = w*(price-1)-lost-cost
        ev += p*net
        no_loss += p*int(net >= -1e-12)
    return {**{'p_'+k: v for k, v in result.items()}, 'p_no_loss': no_loss,
            'p_any_loss': max(0., 1-no_loss), 'estimated_ev': ev}


def bookmaker(name):
    return {'pinnacle': 'Pinnacle', 'bet365': 'bet365', '1xbet': '1xBet'}.get(str(name).casefold().replace(' ', ''))


def parse_quotes(payload, as_of):
    """Only complete opposite-side, same-book/line pairs; no synthetic prices.

    Three-way European, half-time, corners, cards and in-play markets are excluded.
    """
    if not isinstance(payload,dict) or not isinstance(payload.get('bookmakers',[]),list):
        return []
    home, away = payload.get('home_team'), payload.get('away_team')
    if not isinstance(home, str) or not isinstance(away, str) or home == away:
        return []
    if payload.get('commence_time') is not None:
        kick = pd.to_datetime(payload['commence_time'], utc=True, errors='coerce')
        if pd.isna(kick) or as_of is None or kick <= pd.Timestamp(as_of):
            return []
    offers = {}
    for book in payload.get('bookmakers', []):
        if not isinstance(book,dict) or not isinstance(book.get('markets',[]),list):
            continue
        name = bookmaker(book.get('title') or book.get('key'))
        if name is None:
            continue
        for market in book.get('markets', []):
            if not isinstance(market,dict) or not isinstance(market.get('outcomes',[]),list):
                continue
            key = market.get('key')
            if key not in ('spreads', 'alternate_spreads', 'draw_no_bet'):
                continue
            stamp = market.get('last_update') or book.get('last_update')
            if not quote_is_fresh(stamp, as_of):
                continue
            pairs, invalid = {}, set()
            for outcome in market.get('outcomes', []):
                if not isinstance(outcome,dict) or (key=='draw_no_bet' and outcome.get('point') not in (None,0)):
                    invalid.add('all')
                    continue
                if outcome.get('name') not in (home, away):
                    invalid.add('all')
                    continue
                side = 'home' if outcome['name'] == home else 'away'
                try:
                    point = line(0 if key == 'draw_no_bet' else outcome.get('point'))
                    price = float(outcome['price'])
                    if isinstance(outcome['price'], bool) or not math.isfinite(price) or price <= 1:
                        raise ValueError('Invalid price')
                except (ValueError, TypeError, KeyError):
                    continue
                pair = point if side == 'home' else -point
                indexed = pairs.setdefault(pair, {})
                if side in indexed:
                    invalid.add(pair)
                indexed[side] = price
            for point, prices in pairs.items():
                if 'all' in invalid or point in invalid or set(prices) != {'home', 'away'}:
                    continue
                if not .98 <= sum(1/p for p in prices.values()) <= 1.20:
                    continue
                for side in ('home', 'away'):
                    item = {'side': side, 'line': point if side == 'home' else -point,
                            'price': prices[side], 'opposite_price': prices['away' if side == 'home' else 'home'],
                            'bookmaker': name, 'last_update_utc': stamp, 'market_key': key, 'quote_source':'The Odds API'}
                    identity = (side, item['line'], name)
                    previous = offers.get(identity)
                    if previous is None or (str(stamp), item['price']) > (str(previous['last_update_utc']), previous['price']):
                        offers[identity] = item
    return sorted(offers.values(), key=lambda r: (r['side'], r['line'], r['bookmaker']))


def evaluate_history(frame):
    """Chronological loss calibration, not historical AH profitability evidence."""
    report = {'version': VERSION, 'markets': {label(s,p):{'status':'INSUFFICIENT_HISTORY','development_matches':0,'audit_matches':0} for s in ('home','away') for p in LINES}}
    if frame.empty or 'goal_margin_distribution' not in frame:
        return report
    rows = frame.sort_values('date').to_dict('records')
    # Entire matchdays remain in one partition. No test outcomes tune the model.
    boundary = rows[int(len(rows)*.65)]['date']
    for side in ('home', 'away'):
        for point in LINES:
            dev, audit = [], []
            for row in rows:
                try:
                    p = probabilities(row['goal_margin_distribution'], side, point, 2.)['p_no_loss']
                    _, net = profit(int(row['home_goals']), int(row['away_goals']), side, point, 2.)
                    (dev if row['date'] < boundary else audit).append((p, int(net >= 0)))
                except (ValueError, TypeError, KeyError):
                    continue
            state = {'status': 'INSUFFICIENT_HISTORY', 'development_matches': len(dev), 'audit_matches': len(audit)}
            if len(dev) >= 80 and len(audit) >= 40:
                residuals = np.array([p-y for p, y in dev])
                penalty = min(1.,max(0.,float(residuals.mean()+1.96*residuals.std(ddof=1)/math.sqrt(len(dev)))))
                brier = float(np.mean([(p-y)**2 for p, y in audit]))
                reference = float(np.mean([y for _, y in dev]))
                reference_brier = float(np.mean([(reference-y)**2 for _, y in audit]))
                gap = float(np.mean([p-y for p, y in audit]))
                state.update(status='RELIABLE_FOR_RANKING' if brier <= reference_brier+.01 and gap <= .10 else 'UNRELIABLE_AUDIT',
                             confidence_penalty=penalty, audit_brier=brier, audit_overconfidence=gap,
                             note='Chronological no-loss calibration only; no historical handicap price/ROI claim')
            report['markets'][label(side, point)] = state
    return report


def _rank_risk_band(pool, tolerance):
    """Anchor each fixture's band to its minimum; never chain near ties."""
    pool = pool.copy()
    pool['fixture_minimum_loss_probability'] = pool.groupby('_fixture')['loss_probability_upper'].transform('min')
    pool['loss_risk_tolerance'] = tolerance
    pool = pool.loc[pool.loss_probability_upper <= pool.fixture_minimum_loss_probability + tolerance + 1e-12]
    # EV comes before refunds; stable identity fields resolve any remaining ties.
    pool = pool.sort_values(['conservative_estimated_ev','raw_dc_ev','p_refund',
        'loss_probability_upper','offered_decimal_odds','kickoff_utc','market','bookmaker'],
        ascending=[False,False,False,True,False,True,True,True],kind='stable').drop_duplicates('_fixture')
    # Rank the already chosen fixture representatives conservatively for the cap.
    return pool.sort_values(['loss_probability_upper','conservative_estimated_ev','raw_dc_ev',
        'p_refund','kickoff_utc','market','bookmaker'],ascending=[True,False,False,False,True,True,True],kind='stable')


def ordinary_markets(policy_version):
    """Versioned eligibility keeps frozen forecasts replayable."""
    if policy_version == POLICY:
        return ['Home win', 'Away win', 'Over 1.5',
                'Double Chance 1X', 'Double Chance X2', 'Double Chance 12']
    return ['Home win', 'Draw', 'Away win', 'Over 1.5']


def market_family(market):
    if parse_label(market) is not None:
        return 'Asian Handicap'
    if str(market).startswith('Double Chance '):
        return 'Double Chance'
    return 'Match winner' if market in ('Home win', 'Away win', 'Draw') else market


def qualifying_alternatives(selected, decisions, tolerance):
    """Informational alternatives; never change selections or bypass eligibility.

    Prefer another market family. If none qualifies, compare other lines in the
    same family. Re-anchor the risk band to this alternative pool and disclose
    whether the result is outside the original selection's band.
    """
    from performance_tracking import fixture_key
    result = {}
    if decisions.empty:
        return result
    eligible = decisions.loc[decisions.decision.isin(['ELIGIBLE', 'NOT_SELECTED', 'SHORTLISTED']) &
                             decisions.rejection_reasons.fillna('').eq('')].copy()
    eligible['_fixture'] = eligible.apply(fixture_key, axis=1) if len(eligible) else pd.Series(dtype=str)
    for idx, pick in selected.iterrows():
        pool = eligible.loc[(eligible._fixture == fixture_key(pick)) &
                            (eligible.market != pick.market) &
                            (pd.to_datetime(eligible.evaluated_at_utc, utc=True) == pd.Timestamp(pick.evaluated_at_utc))].copy()
        different = pool.loc[pool.market.map(market_family) != market_family(pick.market)]
        other_family = bool(len(different))
        if other_family:
            pool = different
        if pool.empty:
            continue
        alternative = _rank_risk_band(pool, tolerance).iloc[0].to_dict()
        alternative['alternative_scope'] = ('Different market type' if other_family else
                                             'Same market type; no qualifying other type')
        alternative['within_selected_risk_band'] = (
            alternative['loss_probability_upper'] <= float(pick.fixture_minimum_loss_probability) + tolerance + 1e-12)
        result[idx] = alternative
    return result


def build_shortlist(predictions, as_of, market_reliability, execution_policy=None, adjusted_ev_floor=None, policy_version=POLICY):
    """Risk first, strict gates, one market per fixture. No target-filling bypass."""
    from conservative_bet_filter import (build_conservative_shortlist, BALANCED_SELECTION_POLICY_VERSION,
                                        SHORTLIST_COLUMNS, SUPPORTED_LEAGUES, CURRENT_MARKET_SPECS, _evaluate_market)
    from quote_policy import load_policy, validate_policy, usable_bookmaker
    from performance_tracking import fixture_key
    now = pd.Timestamp(as_of)
    if now.tzinfo is None:
        raise ValueError('as_of must be timezone-aware')
    now = now.tz_convert('UTC')
    policy = load_policy() if execution_policy is None else validate_policy(dict(execution_policy))
    legacy = policy_version == LEGACY_POLICY
    current = policy_version in RISK_BAND_POLICIES
    one_percent = policy_version in ONE_PERCENT_POLICIES
    required_ev = MIN_ADJUSTED_EV if one_percent else 0.
    if current:
        policy = validate_policy({**policy, 'asian_handicap_risk_tolerance':policy.get('asian_handicap_risk_tolerance',DEFAULT_RISK_TOLERANCE)})
    tolerance = policy.get('asian_handicap_risk_tolerance',DEFAULT_RISK_TOLERANCE)
    supported = ['Pinnacle','bet365'] if legacy else ['Pinnacle','bet365','1xBet']
    allowed = [b for b in policy['allowed_bookmakers'] if bookmaker(b) in supported] if policy['allowed_bookmakers'] else supported
    policy = validate_policy({**policy, 'allowed_bookmakers': allowed or ['__NO_SUPPORTED_BOOKMAKER__']})
    cost = policy['per_stake_cost_bps']/10000
    floor = .015 if adjusted_ev_floor is None else adjusted_ev_floor
    if legacy:
        if not math.isfinite(floor) or floor < .015:
            raise ValueError('Invalid minimum expected value')
    elif adjusted_ev_floor is not None:
        raise ValueError('This Asian handicap policy does not accept a custom EV floor')
    if one_percent:
        # Reuse all binary-market integrity/calibration gates with the v20 floor.
        # Do not alter historical policy constants or replay their old gates at 1%.
        specs = [s for s in CURRENT_MARKET_SPECS if s[0] in ordinary_markets(policy_version)]
        records = [_evaluate_market(row,spec,now,(market_reliability or {}).get(str(row.get('league'))),
            policy,MIN_ADJUSTED_EV,require_fresh_references=True,lookahead_hours=48.)
            for _,row in predictions.iterrows() for spec in specs]
        ordinary = pd.DataFrame(records,columns=SHORTLIST_COLUMNS)
    else:
        _, ordinary, _ = build_conservative_shortlist(predictions, as_of=now, market_reliability=market_reliability,
            execution_policy=policy, selection_policy_version=BALANCED_SELECTION_POLICY_VERSION)
    ordinary = ordinary.loc[ordinary.market.isin(ordinary_markets(policy_version))].copy()
    # Restore the underlying gate; v16's watchlist ranking never relaxes v17 gates.
    ordinary['decision'] = ordinary.rejection_reasons.fillna('').map(lambda x: 'ELIGIBLE' if not x else 'REJECTED')
    ordinary['p_no_loss'] = ordinary.predicted_probability
    ordinary['p_any_loss'] = 1-ordinary.predicted_probability
    ordinary['p_refund'] = 0.
    ordinary['loss_probability_upper'] = 1-ordinary.rank_probability
    ordinary['probability_basis'] = 'win'
    for field in FIELDS:
        if field not in ordinary:
            ordinary[field] = None
    evaluated = ordinary.to_dict('records')
    for _, row in predictions.iterrows():
        try:
            offers = row.get('asian_handicap_offers', '[]')
            offers = json.loads(offers) if isinstance(offers, str) else offers
            if not isinstance(offers, list):
                continue
        except (ValueError, TypeError):
            continue
        for offer in offers:
            reasons = []
            try:
                side, point = offer['side'], line(offer['line'])
                name = label(side, point)
                price, opposite = float(offer['price']), float(offer['opposite_price'])
                book = bookmaker(offer['bookmaker'])
                if not all(math.isfinite(p) and p > 1 for p in (price, opposite)):
                    raise ValueError('Invalid pair')
                if not .98 <= 1/price+1/opposite <= 1.20:
                    raise ValueError('Invalid pair overround')
                if offer.get('market_key') not in ('spreads','alternate_spreads','draw_no_bet'):
                    raise ValueError('Unsupported period or market')
                if book is None or not usable_bookmaker(book, policy):
                    reasons.append('bookmaker unavailable: Pinnacle/bet365 or 1xBet fallback required')
                p = probabilities(row['goal_margin_distribution'], side, point, price, cost)
                raw = probabilities(row['raw_goal_margin_distribution'], side, point, price, cost)
            except (ValueError, TypeError, KeyError):
                continue
            kick = pd.to_datetime(row.get('kickoff_utc'), utc=True, errors='coerce')
            if pd.isna(kick) or not now+pd.Timedelta(minutes=20) <= kick <= now+pd.Timedelta(hours=48):
                reasons.append('kickoff outside 20-minute to 48-hour window')
            if row.get('league') not in SUPPORTED_LEAGUES:
                reasons.append('competition unsupported')
            if row.get('odds_source') != 'The Odds API' or row.get('market_blend_applied') not in (True, 1, 'True'):
                reasons.append('missing verified live 1X2 blend')
            for time in (offer.get('last_update_utc'), row.get('market_reference_1x2_last_update_utc')):
                if not quote_is_fresh(time, now):
                    reasons.append('missing stale or future quote/reference')
            try:
                if not all(math.isfinite(float(row[s+'_name_match_score'])) and float(row[s+'_name_match_score']) >= 90 for s in ('home','away')) or any(
                        row.get('model_'+s+'_team') in (None, '__LEAGUE_AVERAGE__') for s in ('home','away')):
                    reasons.append('unreliable team identity')
            except (KeyError, TypeError, ValueError):
                reasons.append('unreliable team identity')
            validation = (market_reliability or {}).get(str(row.get('league')), {}).get('asian_handicap', {}).get('markets', {}).get(name, {})
            penalty = validation.get('confidence_penalty')
            if (validation.get('status') != 'RELIABLE_FOR_RANKING' or
                    not isinstance(validation.get('development_matches'),int) or validation['development_matches'] < 80 or
                    not isinstance(validation.get('audit_matches'),int) or validation['audit_matches'] < 40 or
                    not isinstance(penalty, (int,float)) or not math.isfinite(penalty) or not 0 <= penalty <= 1):
                reasons.append('Asian handicap historical reliability unavailable or failed')
                penalty = 1.
            if cost != 0:
                reasons.append('nonzero-cost no-loss calibration not yet validated')
            # Conservatively move development overconfidence from the best payoff
            # to a full loss. A bound heuristic, not a statistical guarantee.
            adjusted_ev = p['estimated_ev']-penalty*price
            risk = min(1., max(p['p_any_loss'], raw['p_any_loss'])+penalty)
            if legacy and (adjusted_ev < floor or raw['estimated_ev'] < 0):
                reasons.append('positive conservative EV and nonnegative raw EV required')
            if current and (adjusted_ev < required_ev or raw['estimated_ev'] < 0):
                reasons.append('adjusted EV below +1.0% or negative unblended EV' if one_percent else 'negative adjusted or unblended EV')
            item = {field: None for field in SHORTLIST_COLUMNS+FIELDS}
            item.update({k: row.get(k) for k in ('date','league','home_team','away_team','fixture_id','kickoff_utc')})
            item.update(evaluated_at_utc=now.isoformat(), market=name,
                handicap_side=side, handicap_line=point, bookmaker=book, offered_decimal_odds=price,
                per_stake_cost=cost, predicted_probability=p['p_no_loss'], raw_dc_probability=raw['p_no_loss'],
                raw_p_no_loss=raw['p_no_loss'], rank_probability=1-risk, raw_dc_ev=raw['estimated_ev'],
                estimated_ev=p['estimated_ev'], gross_estimated_ev=p['estimated_ev']+cost,
                conservative_estimated_ev=adjusted_ev, calibration_penalty=penalty,
                loss_probability_upper=risk, probability_basis='net_no_loss',
                validation_status=validation.get('status','INSUFFICIENT_HISTORY'),
                asian_handicap_validation=VERSION, quote_source=offer.get('quote_source','The Odds API'),
                quote_last_update_utc=offer.get('last_update_utc'), opposite_decimal_odds=opposite, development_validation_matches=validation.get('development_matches'),
                audit_validation_matches=validation.get('audit_matches'), audit_brier=validation.get('audit_brier'),
                odds_age_hours=(now-pd.Timestamp(offer['last_update_utc'])).total_seconds()/3600 if quote_is_fresh(offer.get('last_update_utc'),now) else None,
                rejection_reasons='; '.join(dict.fromkeys(reasons)), decision='REJECTED' if reasons else 'ELIGIBLE',
                selection_tier=None, **{k:v for k,v in p.items() if k.startswith('p_')})
            evaluated.append(item)
    columns = list(dict.fromkeys(SHORTLIST_COLUMNS+FIELDS))
    decisions = pd.DataFrame(evaluated).reindex(columns=columns)
    if not legacy:
        # Fallback is per exact fixture/side/line; invalid or stale primary quotes
        # do not suppress a valid fallback. All other gates still apply.
        valid = decisions.loc[(decisions.decision == 'ELIGIBLE') & decisions.market.map(lambda x: parse_label(x) is not None)]
        primary = {(fixture_key(r), r['market']) for r in valid.to_dict('records') if r['bookmaker'] in ('Pinnacle','bet365')}
        for idx, r in valid.iterrows():
            if r.bookmaker == '1xBet' and (fixture_key(r), r.market) in primary:
                decisions.loc[idx, ['decision','rejection_reasons']] = ['REJECTED','primary bookmaker quote available for this handicap']
    pool = decisions.loc[decisions.decision == 'ELIGIBLE'].copy()
    pool['_fixture'] = pool.apply(fixture_key, axis=1) if len(pool) else pd.Series(dtype=str)
    ranking = ['loss_probability_upper','p_refund','conservative_estimated_ev'] + ([] if legacy else ['raw_dc_ev']) + ['offered_decimal_odds','kickoff_utc','market']
    if current:
        decisions['loss_risk_tolerance'] = tolerance
        decisions['fixture_minimum_loss_probability'] = None
        decisions.loc[pool.index,'fixture_minimum_loss_probability'] = pool.groupby('_fixture')['loss_probability_upper'].transform('min')
        pool = _rank_risk_band(pool,tolerance)
    else:
        pool = pool.sort_values(ranking, ascending=[True]+[False]*(len(ranking)-3)+[True,True], kind='stable').drop_duplicates('_fixture')
    chosen = pool.head(12).index
    decisions.loc[decisions.decision == 'ELIGIBLE','decision'] = 'NOT_SELECTED'
    decisions.loc[chosen,'decision'] = 'SHORTLISTED'
    decisions.loc[chosen,'selection_tier'] = 'STRICT'
    selected = decisions.loc[chosen].reset_index(drop=True)
    summary = {'generated_at_utc':now.isoformat(), 'selection_policy_version':policy_version,
        'status':'TARGET_MET' if len(selected)==12 else 'BELOW_TARGET' if len(selected) else 'NO BET',
        'n_fixtures':len(predictions), 'n_markets_evaluated':len(decisions), 'n_shortlisted':len(selected),
        'n_strict_qualified':len(selected), 'n_provisional_watchlist':0, 'n_total_candidates':len(selected),
        'target_distinct_matches':12, 'shortfall':12-len(selected), 'usable_distinct_fixtures':len(pool),
        'shortlist_lookahead_hours':48., 'selected_matches_within_48_hours':bool(len(selected)),
        'shortlist_window_start_utc':now.isoformat(), 'shortlist_window_end_utc':(now+pd.Timedelta(hours=48)).isoformat(),
        'eligible_markets':ordinary_markets(policy_version)+[label(s,p) for s in ('home','away') for p in LINES],
        'quote_execution_policy':policy, 'validation_required':True, 'selection_objective':'MINIMIZE_ESTIMATED_NET_LOSS',
        'selection_method':'Lowest conservative estimated loss risk, then refund probability, adjusted EV, unblended EV, price; one per fixture',
        'ranking_metric':'loss_probability_upper ascending; p_refund descending; adjusted EV descending' + ('' if legacy else '; unblended EV descending'),
        'min_estimated_ev':floor if legacy else required_ev if current else None,
        'min_raw_dc_ev':0. if legacy or current else None, 'ev_required_for_selection':legacy or current,
        'validation_market_statuses':{league:{key:state.get('status','INSUFFICIENT_HISTORY') for key,state in report.get('markets',{}).items()} for league,report in (market_reliability or {}).items()},
        'legacy_ranking_experiments':'NOT_APPLICABLE_TO_LOSS_FIRST_POLICY; archived experiments remain graded', 'ranking_is_empirically_optimized':False,
        'shortfall_reason':'No padding: missing quotes or historical reliability can reduce the shortlist' if len(selected)<12 else None,
        'bookmaker_coverage':{b:sum(str(x.get('bookmaker'))==b for x in evaluated if parse_label(x.get('market'))) for b in supported},
        'warning':'Probabilities are model estimates, not guarantees. Refunds are not wins; half-losses lose money. No selection when required evidence is missing. Negative estimated EV is possible under v18. Flat-stake research, not accumulator protection.'}
    if current:
        summary.update(selection_objective='MAXIMIZE_EV_WITHIN_NEAR_MINIMUM_ESTIMATED_LOSS_RISK',
            loss_risk_tolerance=tolerance, risk_tolerance_status='PROVISIONAL_POLICY_SETTING_NOT_EMPIRICALLY_TUNED',
            selection_method='Per fixture: within tolerance of minimum eligible loss risk, then adjusted EV, unblended EV, refund probability; fixture representatives ordered by loss risk; cap 12',
            ranking_metric='risk band per fixture; adjusted EV descending; unblended EV descending; refund probability descending',
            shortfall_reason='No padding: missing evidence or failing the EV floors can reduce the shortlist' if len(selected)<12 else None,
            warning='Probabilities and EV are model estimates, not guarantees. Required adjusted EV: '+format(required_ev,'.1%')+'; unblended EV must be nonnegative. Risk tolerance is provisional; refunds are not wins. Flat-stake research, not accumulator protection.')
    return selected, decisions.reset_index(drop=True), summary


def apply_quote_file(predictions, path, as_of):
    """Explicit user-supplied provider-shaped event array; no scraping or prices inferred."""
    from pathlib import Path
    from football_value_pipeline_v2_standalone import canonical_team_key
    data = json.loads(Path(path).read_text(encoding='utf-8-sig'))
    if not isinstance(data, list):
        raise ValueError('Asian quote file must contain a JSON array of events')
    result = predictions.copy()
    for idx, row in result.iterrows():
        matches = [e for e in data if isinstance(e, dict) and
            str(e.get('id')) == str(row.get('odds_event_id') or row.get('fixture_id')) and
            canonical_team_key(str(e.get('home_team',''))) == canonical_team_key(row['home_team']) and
            canonical_team_key(str(e.get('away_team',''))) == canonical_team_key(row['away_team']) and
            pd.to_datetime(e.get('commence_time'),utc=True,errors='coerce') == pd.to_datetime(row['kickoff_utc'],utc=True)]
        if len(matches) > 1:
            raise ValueError('Ambiguous duplicate quote-file event')
        if matches:
            offered = parse_quotes(matches[0], as_of)
            for item in offered:item['quote_source']='User-supplied bookmaker quote; account execution unverified'
            old = row.get('asian_handicap_offers','[]')
            old = json.loads(old) if isinstance(old,str) else []
            merged = {(x['side'],x['line'],x['bookmaker']):x for x in sorted(old+offered,key=lambda x:(x['last_update_utc'],x['price']))}
            result.at[idx,'asian_handicap_offers'] = json.dumps(list(merged.values()),sort_keys=True)
    return result


def best_per_match(decisions):
    """Best eligible Asian line for every fixture, even beyond the shortlist cap."""
    from performance_tracking import fixture_key
    subset = decisions.loc[decisions.market.map(lambda x: parse_label(x) is not None) &
                           decisions.rejection_reasons.fillna('').eq('')].copy()
    subset['_fixture'] = subset.apply(fixture_key,axis=1) if len(subset) else pd.Series(dtype=str)
    if 'loss_risk_tolerance' in decisions:
        values = decisions.loss_risk_tolerance.dropna().unique()
        if len(values) != 1 and len(subset):
            raise ValueError('Missing or inconsistent frozen risk tolerance')
        tolerance = float(values[0]) if len(values) else DEFAULT_RISK_TOLERANCE
        return _rank_risk_band(subset,tolerance).drop(columns='_fixture').reset_index(drop=True)
    return subset.sort_values(['loss_probability_upper','p_refund','conservative_estimated_ev','raw_dc_ev','offered_decimal_odds','market'],
        ascending=[True,False,False,False,False,True],kind='stable').drop_duplicates('_fixture').drop(columns='_fixture').reset_index(drop=True)
