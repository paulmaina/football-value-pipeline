"""Versioned shortlist v26: the v22 common no-loss rules plus Corners totals.

Reuse every v22 eligibility, floor and ranking rule unchanged and add corner
totals from the v25 count-market gates. A corner line must pass its own
league/line reliability audit and the same 75% adjusted no-loss and +1%
adjusted EV floors. Every league is approved per market, as in v25. Card
totals stay excluded. v22 and v25 stay importable so archived captures replay.
"""
import pandas as pd

import count_markets
import corners_cards_shortlist as v25

POLICY = '48h-zero-tolerance-ev1-no-loss75-corners-v26'
COUNT_GROUPS = (count_markets.GROUPS['corners'],)
COUNT_MARKETS = tuple(count_markets.market_label('corners', side, line)
                      for line in count_markets.LINES['corners'] for side in ('Over', 'Under'))
MAX_SELECTIONS = 12


def corner_decisions(predictions, as_of, market_reliability, policy, minimum_no_loss, minimum_ev):
    """v25 count-market gates, re-expressed on the v22 loss-risk scale.

    Corner lines are half-goal totals, so avoiding a loss means winning: there
    is no refund. The count model has no independent second forecast, so its
    unpenalized EV stands in for the unblended-EV check.
    """
    counts = v25.count_market_decisions(predictions, as_of, market_reliability, policy)
    if counts.empty:
        return counts
    counts = counts.loc[counts.market.isin(COUNT_MARKETS)].copy()
    counts['loss_probability_upper'] = 1-counts.rank_probability
    counts['p_no_loss'] = counts['raw_p_no_loss'] = counts.predicted_probability
    counts['p_any_loss'] = 1-counts.predicted_probability
    counts['p_refund'] = 0.
    counts['p_profit'] = counts['raw_p_profit'] = None
    counts['probability_basis'] = 'win'
    for idx, item in counts.iterrows():
        reasons = [r for r in str(item.rejection_reasons or '').split('; ') if r]
        if pd.isna(item.rank_probability) or item.rank_probability + 1e-12 < minimum_no_loss:
            reasons.append('adjusted probability of avoiding loss below '+format(minimum_no_loss, '.0%')+' or missing')
        if pd.isna(item.conservative_estimated_ev) or item.conservative_estimated_ev + 1e-12 < minimum_ev or item.raw_dc_ev < 0:
            reasons.append('adjusted EV below +1.0% or negative unblended EV')
        counts.at[idx, 'rejection_reasons'] = '; '.join(dict.fromkeys(reasons))
        counts.at[idx, 'decision'] = 'REJECTED' if reasons else 'ELIGIBLE'
    return counts


def build_shortlist(predictions, as_of, market_reliability, execution_policy=None):
    from asian_handicap import (POLICY as V22, MIN_ADJUSTED_EV, _rank_risk_band,
                                build_shortlist as build_v22)
    from performance_tracking import fixture_key
    _, decisions, summary = build_v22(predictions, as_of, market_reliability,
                                      execution_policy=execution_policy, policy_version=V22)
    policy = summary['quote_execution_policy']
    minimum_no_loss = summary['min_adjusted_no_loss_probability']
    tolerance = summary['loss_risk_tolerance']
    # Per-market approval for every league, stated explicitly as in v25.
    for idx in decisions.index[decisions.validation_status.ne('RELIABLE_FOR_RANKING')]:
        reasons = [r for r in str(decisions.at[idx, 'rejection_reasons'] or '').split('; ') if r]
        reasons.append(f"per-market approval: market audit {decisions.at[idx, 'validation_status']}")
        decisions.at[idx, 'rejection_reasons'] = '; '.join(dict.fromkeys(reasons))
        decisions.at[idx, 'decision'] = 'REJECTED'
    counts = corner_decisions(predictions, as_of, market_reliability, policy, minimum_no_loss, MIN_ADJUSTED_EV)
    if len(counts):
        decisions = pd.concat([decisions, counts.reindex(columns=list(dict.fromkeys([*decisions.columns, *counts.columns])))],
                              ignore_index=True)
    for field in ('count_kind', 'count_side', 'count_line', 'count_model_mean', 'count_model_version', 'unproven_edge'):
        if field not in decisions:
            decisions[field] = None
    eligible = decisions.decision.isin(['SHORTLISTED', 'NOT_SELECTED', 'ELIGIBLE'])
    decisions.loc[eligible, 'decision'] = 'NOT_SELECTED'
    decisions.loc[eligible, 'selection_tier'] = None
    # Re-run the v22 zero-tolerance ranking over the combined candidate pool.
    pool = decisions.loc[eligible].copy()
    pool['_fixture'] = pool.apply(fixture_key, axis=1) if len(pool) else pd.Series(dtype=str)
    decisions['loss_risk_tolerance'] = tolerance
    decisions['fixture_minimum_loss_probability'] = None
    decisions.loc[pool.index, 'fixture_minimum_loss_probability'] = pool.groupby('_fixture')['loss_probability_upper'].transform('min')
    pool = _rank_risk_band(pool, tolerance)
    chosen = pool.head(MAX_SELECTIONS).index
    decisions.loc[chosen, 'decision'] = 'SHORTLISTED'
    decisions.loc[chosen, 'selection_tier'] = 'STRICT'
    selected = decisions.loc[chosen].reset_index(drop=True)
    unproven = selected.market.isin(COUNT_MARKETS)
    summary.update(selection_policy_version=POLICY,
        n_markets_evaluated=len(decisions), n_shortlisted=len(selected), n_strict_qualified=len(selected),
        n_total_candidates=len(selected), target_distinct_matches=MAX_SELECTIONS,
        shortfall=MAX_SELECTIONS-len(selected), usable_distinct_fixtures=len(pool),
        selected_matches_within_48_hours=bool(len(selected)),
        status='TARGET_MET' if len(selected) == MAX_SELECTIONS else 'BELOW_TARGET' if len(selected) else 'NO BET',
        shortfall_reason=('No padding: missing evidence or failing the common safety/EV cutoffs can reduce the shortlist'
                          if len(selected) < MAX_SELECTIONS else None),
        eligible_markets=list(dict.fromkeys([*summary['eligible_markets'], *COUNT_MARKETS])),
        selection_method='Require common adjusted no-loss probability floor; zero risk tolerance; lowest conservative loss '
                         'estimate per fixture, then adjusted EV, unblended EV and refund probability; Corners totals compete '
                         'under the same floors; cap 12',
        shortlist_approval='per-market for every league',
        unproven_edge_market_groups=list(COUNT_GROUPS), unproven_edge_selections=int(unproven.sum()),
        unproven_edge_markets=[f'{r.home_team} vs {r.away_team}: {r.market}' for r in selected.loc[unproven].itertuples()],
        count_market_validation='Probability accuracy only: walk-forward on six football-data.co.uk seasons; '
                                'no historical corner odds exist, so profitability is unproven. Card totals are excluded.',
        negative_adjusted_ev_selections=int((selected.conservative_estimated_ev < 0).sum()),
        warning='Probabilities and EV are model estimates, not guarantees. Required adjusted no-loss probability: '
                + format(minimum_no_loss, '.0%') + '; required adjusted EV: ' + format(MIN_ADJUSTED_EV, '.1%')
                + '; unblended EV must be nonnegative. Refunds are not wins. Corners picks are UNPROVEN EDGE: validated on '
                'probability accuracy only, with no historical corner odds. Flat-stake research, not accumulator protection.')
    return selected, decisions.reset_index(drop=True), summary
