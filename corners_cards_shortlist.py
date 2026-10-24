"""Versioned per-market shortlist v25: v24 plus Corners and Cards totals.

Reuse every v23 eligibility, quote, identity and 48-hour check and the v24
ranking and allocation unchanged. Every league is approved per market: a
league/market reaches the shortlist only on its own passing reliability audit.
Corner and card picks are validated on probability accuracy only (no
historical prices exist), so each carries an UNPROVEN EDGE warning.
v24 and older stay importable so archived captures replay.
"""
import json
import math

import pandas as pd

import count_markets
import per_market_shortlist as v24

POLICY = '48h-two-per-market-group-probability-ev-corners-cards-v25'
COUNT_GROUPS = tuple(count_markets.GROUPS[k] for k in ('corners', 'cards'))
MARKET_GROUPS = (*v24.MARKET_GROUPS, *COUNT_GROUPS)
PER_GROUP_CAP = v24.PER_GROUP_CAP
MAX_SELECTIONS = PER_GROUP_CAP*len(MARKET_GROUPS)
COUNT_MARKETS = tuple(count_markets.market_label(kind, side, line) for kind in ('corners', 'cards')
                      for line in count_markets.LINES[kind] for side in ('Over', 'Under'))


def market_group(market):
    parsed = count_markets.parse_label(market)
    return count_markets.GROUPS[parsed[0]] if parsed else v24.market_group(market)


def _finite(value):
    try:
        return math.isfinite(float(value))
    except (TypeError, ValueError):
        return False


def _count_evidence(market_reliability, league, kind, label):
    report = ((market_reliability or {}).get(league) or {}).get('count_markets', {}).get(kind, {})
    if report.get('version') != count_markets.VERSION:
        return {}
    return report.get('markets', {}).get(label, {})


def count_market_decisions(predictions, as_of, market_reliability, policy):
    """One decision per quoted corner/card total, with every v23-style gate."""
    import league_registry
    from asian_handicap import bookmaker
    from europa_training import eligibility
    from quote_freshness import quote_is_fresh
    from quote_policy import usable_bookmaker
    now = pd.Timestamp(as_of).tz_convert('UTC')
    cost = policy['per_stake_cost_bps']/10000
    out = []
    for _, row in predictions.iterrows():
        try:
            offers = json.loads(row.get('count_market_offers') or '[]')
            model = json.loads(row.get('count_model') or '{}')
        except (TypeError, ValueError):
            continue
        if not isinstance(offers, list) or not isinstance(model, dict):
            continue
        league = str(row.get('league'))
        for offer in offers:
            try:
                kind, side, line = offer['kind'], offer['side'], float(offer['line'])
                price, opposite = float(offer['price']), float(offer['opposite_price'])
                label = count_markets.market_label(kind, side, line)
            except (KeyError, TypeError, ValueError):
                continue
            if count_markets.parse_label(label) is None:
                continue
            reasons = []
            book = bookmaker(offer.get('bookmaker'))
            if book is None or not usable_bookmaker(book, policy):
                reasons.append('bookmaker excluded by execution policy (exchange or user allowlist)')
            if not (all(math.isfinite(p) and p > 1 for p in (price, opposite)) and .98 <= 1/price+1/opposite <= 1.20):
                reasons.append('implausible same-book Over/Under pair')
            if not quote_is_fresh(offer.get('last_update_utc'), now):
                reasons.append('specific bookmaker quote is missing, stale or future-dated')
            kick = pd.to_datetime(row.get('kickoff_utc'), utc=True, errors='coerce')
            if pd.isna(kick) or not now+pd.Timedelta(minutes=20) <= kick <= now+pd.Timedelta(hours=48):
                reasons.append('kickoff outside 20-minute to 48-hour window')
            reasons.extend(eligibility(row))
            if league not in {league_registry.get(k).name for k in count_markets.LEAGUES[kind]}:
                reasons.append('competition has no validated count market')
            if row.get('odds_source') != 'The Odds API' or row.get('market_blend_applied') not in (True, 1, 'True'):
                reasons.append('missing verified live 1X2 blend')
            try:
                if not all(math.isfinite(float(row[s+'_name_match_score'])) and float(row[s+'_name_match_score']) >= 90
                           for s in ('home', 'away')) or any(
                        row.get('model_'+s+'_team') in (None, '__LEAGUE_AVERAGE__') for s in ('home', 'away')):
                    reasons.append('unreliable team identity')
            except (KeyError, TypeError, ValueError):
                reasons.append('unreliable team identity')
            fit = model.get(kind) if isinstance(model.get(kind), dict) else {}
            p = None
            if (fit.get('version') == count_markets.VERSION and _finite(fit.get('mu')) and _finite(fit.get('alpha'))
                    and float(fit['mu']) > 0 and float(fit['alpha']) > 0):
                p = count_markets.probabilities(float(fit['mu']), float(fit['alpha']), kind)[label]
            else:
                reasons.append('missing count-model forecast')
            # Per-market approval: this league's own audit for this exact line and side.
            evidence = _count_evidence(market_reliability, league, kind, label)
            status = evidence.get('status', 'NOT_ASSESSED')
            penalty = evidence.get('confidence_penalty')
            if status != 'RELIABLE_FOR_RANKING':
                reasons.append(f'per-market approval: market audit {status}')
            if not _finite(penalty) or not 0 <= float(penalty) <= 1:
                reasons.append('invalid or missing market calibration penalty')
                penalty = 1.
            penalty = float(penalty)
            if p is not None and p >= .75:
                tier = '85plus' if p >= .85 else '75plus'
                group = evidence.get('high_confidence', {}).get(tier, {})
                if group.get('status') != 'PASSED':
                    reasons.append(f"per-market approval: {tier} audit {group.get('status', 'INSUFFICIENT_HIGH_CONFIDENCE_HISTORY')}")
                if _finite(group.get('development_only_penalty')):
                    penalty = max(penalty, float(group['development_only_penalty']))
            rank = max(0., p - penalty) if p is not None else float('nan')
            ev = p*price - 1 - cost if p is not None else float('nan')
            adjusted_ev = rank*price - 1 - cost if p is not None else float('nan')
            warnings = [count_markets.UNPROVEN_EDGE]
            if _finite(adjusted_ev) and adjusted_ev < 0:
                warnings.append('NEGATIVE ADJUSTED EV: high win chance does not imply a profitable price')
            stamp = pd.to_datetime(offer.get('last_update_utc'), utc=True, errors='coerce')
            out.append({
                **{k: row.get(k) for k in ('date', 'league', 'home_team', 'away_team', 'fixture_id', 'kickoff_utc',
                                           'model_home_team', 'model_away_team')},
                'evaluated_at_utc': now.isoformat(), 'market': label, 'bookmaker': book or offer.get('bookmaker'),
                'offered_decimal_odds': price, 'opposite_decimal_odds': opposite, 'per_stake_cost': cost,
                'predicted_probability': p, 'raw_dc_probability': p, 'rank_probability': rank,
                'p_profit': p, 'raw_p_profit': p, 'p_full_win': p, 'p_half_win': 0., 'probability_basis': 'net_profit',
                'calibration_penalty': penalty, 'estimated_ev': ev, 'gross_estimated_ev': ev + cost if p is not None else ev,
                'conservative_estimated_ev': adjusted_ev, 'raw_dc_ev': ev, 'validation_status': status,
                'development_validation_matches': evidence.get('development', {}).get('n'),
                'audit_validation_matches': evidence.get('audit', {}).get('n'),
                'audit_brier': evidence.get('audit', {}).get('brier'),
                'quote_source': offer.get('quote_source', 'The Odds API'),
                'quote_last_update_utc': offer.get('last_update_utc'),
                'odds_age_hours': (now-stamp).total_seconds()/3600 if not pd.isna(stamp) else None,
                'count_kind': kind, 'count_side': side, 'count_line': line,
                'count_model_mean': fit.get('mu'), 'count_model_version': fit.get('version'),
                'unproven_edge': True, 'selection_warnings': '; '.join(warnings),
                'near_miss_reason': '; '.join(warnings),
                'rejection_reasons': '; '.join(dict.fromkeys(reasons)),
                'decision': 'REJECTED' if reasons else 'ELIGIBLE', 'selection_tier': None})
    return pd.DataFrame(out)


def _execution_policy(execution_policy):
    """The v23 execution policy: Pinnacle and bet365 only, no fallbacks."""
    from quote_policy import load_policy, validate_policy
    policy = load_policy() if execution_policy is None else validate_policy(dict(execution_policy))
    allowed = [b for b in policy['allowed_bookmakers'] if b.casefold() in ('pinnacle', 'bet365')]
    if not policy['allowed_bookmakers']:
        allowed = ['Pinnacle', 'bet365']
    return validate_policy({**policy, 'allowed_bookmakers': allowed or ['__NO_SUPPORTED_BOOKMAKER__'],
                            'fallback_bookmakers': []})


def build_shortlist(predictions, as_of, market_reliability, execution_policy=None):
    from win_first_shortlist import build_shortlist as build_v23
    _, decisions, summary = build_v23(predictions, as_of, market_reliability, execution_policy)
    # Per-market approval for every league, stated explicitly. v23 already
    # rejects these rows; this labels the rule without changing eligibility.
    for idx in decisions.index[decisions.validation_status.ne('RELIABLE_FOR_RANKING')]:
        reasons = [r for r in str(decisions.at[idx, 'rejection_reasons'] or '').split('; ') if r]
        reasons.append(f"per-market approval: market audit {decisions.at[idx, 'validation_status']}")
        decisions.at[idx, 'rejection_reasons'] = '; '.join(dict.fromkeys(reasons))
        decisions.at[idx, 'decision'] = 'REJECTED'
    counts = count_market_decisions(predictions, as_of, market_reliability, _execution_policy(execution_policy))
    if len(counts):
        decisions = pd.concat([decisions, counts.reindex(columns=list(dict.fromkeys([*decisions.columns, *counts.columns])))],
                              ignore_index=True)
    for field in ('count_kind', 'count_side', 'count_line', 'count_model_mean', 'count_model_version', 'unproven_edge'):
        if field not in decisions:
            decisions[field] = None
    eligible = decisions.decision.isin(['SHORTLISTED', 'NOT_SELECTED', 'ELIGIBLE'])
    decisions.loc[eligible, 'decision'] = 'NOT_SELECTED'
    decisions.loc[eligible, 'selection_tier'] = None
    ungrouped = eligible & decisions.market.map(market_group).isna()
    for idx in decisions.index[ungrouped]:
        decisions.at[idx, 'decision'] = 'REJECTED'
        decisions.at[idx, 'rejection_reasons'] = 'market outside v25 market groups'
    ranked = v24.rank_candidates(decisions.loc[eligible & ~ungrouped], market_group)
    fields = ['market_group', 'probability_percentile', 'ev_percentile', 'selection_score']
    for field in fields:
        decisions[field] = None if field == 'market_group' else float('nan')
    decisions.loc[ranked.index, fields] = ranked[fields]
    chosen = v24.select_candidates(ranked, MARKET_GROUPS)
    decisions.loc[chosen, 'decision'] = 'SHORTLISTED'
    decisions.loc[chosen, 'selection_tier'] = 'STRICT'
    selected = ranked.loc[chosen].assign(_group=lambda f: f.market_group.map(MARKET_GROUPS.index))
    selected = decisions.loc[selected.sort_values('_group', kind='stable').index].reset_index(drop=True)
    group_shortfall = {}
    for group in MARKET_GROUPS:
        n_selected = int((selected.market_group == group).sum())
        group_shortfall[group] = {
            'eligible_fixtures': int(ranked.loc[ranked.market_group == group, '_fixture'].nunique()),
            'selected': n_selected, 'shortfall': PER_GROUP_CAP-n_selected}
    negative = selected.conservative_estimated_ev < 0
    unproven = selected.market_group.isin(COUNT_GROUPS)
    summary.update(selection_policy_version=POLICY, selection_objective='PER_MARKET_PROBABILITY_WEIGHTED',
        selection_method=f'Within each market group, {v24.PROBABILITY_WEIGHT:g} x adjusted-probability percentile + '
                         f'{v24.EV_WEIGHT:g} x adjusted-EV percentile; at most {PER_GROUP_CAP} per group and '
                         f'{MAX_SELECTIONS} in total; one market per fixture; fill the most slots possible, then prefer higher scores in rank order',
        ranking_metric='selection_score descending; ties: adjusted probability descending, adjusted EV descending, unblended EV descending, odds descending',
        ranking_weights={'adjusted_probability_percentile': v24.PROBABILITY_WEIGHT,
                         'adjusted_ev_percentile': v24.EV_WEIGHT},
        score_formula=f'{v24.PROBABILITY_WEIGHT:g} * probability_percentile + {v24.EV_WEIGHT:g} * ev_percentile (within market group)',
        market_groups=list(MARKET_GROUPS), max_per_market_group=PER_GROUP_CAP,
        eligible_markets=list(dict.fromkeys([*summary.get('eligible_markets', []), *COUNT_MARKETS])),
        shortlist_approval='per-market for every league',
        unproven_edge_market_groups=list(COUNT_GROUPS), unproven_edge_selections=int(unproven.sum()),
        unproven_edge_markets=[f'{r.home_team} vs {r.away_team}: {r.market}' for r in selected.loc[unproven].itertuples()],
        count_market_validation='Probability accuracy only: walk-forward on six football-data.co.uk seasons; '
                                'no historical corner or card odds exist, so profitability is unproven.',
        target_distinct_matches=MAX_SELECTIONS, group_shortfall=group_shortfall,
        min_estimated_ev=None, min_raw_dc_ev=None, ev_required_for_selection=False,
        n_shortlisted=len(selected), n_strict_qualified=len(selected), n_provisional_watchlist=0,
        n_total_candidates=len(selected), usable_distinct_fixtures=int(ranked._fixture.nunique()),
        shortfall=MAX_SELECTIONS-len(selected), selected_matches_within_48_hours=bool(len(selected)),
        status='TARGET_MET' if len(selected) == MAX_SELECTIONS else 'BELOW_TARGET' if len(selected) else 'NO BET',
        shortfall_reason=(None if len(selected) == MAX_SELECTIONS else
            'Short groups: ' + ', '.join(f"{g} {s['selected']}/{PER_GROUP_CAP}"
                                         for g, s in group_shortfall.items() if s['shortfall']) +
            '. No allocation of eligible candidates fills these slots; they are not filled from other groups.'),
        negative_adjusted_ev_selections=int(negative.sum()),
        negative_adjusted_ev_markets=[f'{r.home_team} vs {r.away_team}: {r.market}'
                                      for r in selected.loc[negative].itertuples()],
        warning=f'Full and half wins count as profitable outcomes; refunds do not. No probability or EV floor. '
                f'Negative adjusted EV is explicitly flagged. Corners and Cards picks are UNPROVEN EDGE: validated on '
                f'probability accuracy only, with no historical corner or card odds. Percentile scores are relative ranks '
                f'within a market group, not probabilities. Estimates are not guarantees; {MAX_SELECTIONS} individual picks '
                f'are not an accumulator recommendation.')
    return selected, decisions.reset_index(drop=True), summary
