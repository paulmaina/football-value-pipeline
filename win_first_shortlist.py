"""Versioned top-twelve profitable-outcome ranking; refunds never count as wins.

Reuse v22 quote/identity/history checks, but do not reuse no-loss calibration
as win calibration. Historical policies and their frozen reports stay intact.
"""
import math

import numpy as np
import pandas as pd

POLICY = '48h-top-twelve-profitable-win-probability-v23'
VALIDATOR_VERSION = 'asian-handicap-profitable-win-v1'


def rank_candidates(pool):
    """One market per fixture, then the global top twelve; EV only breaks ties."""
    return pool.sort_values(
        ['rank_probability', 'conservative_estimated_ev', 'raw_dc_ev',
         'offered_decimal_odds', 'kickoff_utc', 'league', 'home_team',
         'away_team', 'market', 'bookmaker'],
        ascending=[False, False, False, False, True, True, True, True, True, True],
        kind='stable').drop_duplicates('_fixture')


def _finite(value):
    try:
        return math.isfinite(float(value))
    except (TypeError, ValueError):
        return False


def build_shortlist(predictions, as_of, market_reliability, execution_policy=None):
    from asian_handicap import build_shortlist as legacy_build, POLICY as V22, parse_label
    from performance_tracking import fixture_key
    from quote_policy import load_policy, validate_policy

    policy = load_policy() if execution_policy is None else validate_policy(dict(execution_policy))
    # v23 only supports the two bookmakers requested by the user, even if a
    # caller supplies an obsolete fallback configuration.
    allowed = [b for b in policy['allowed_bookmakers'] if b.casefold() in ('pinnacle', 'bet365')]
    if not policy['allowed_bookmakers']:
        allowed = ['Pinnacle', 'bet365']
    policy = validate_policy({**policy, 'allowed_bookmakers': allowed or ['__NO_SUPPORTED_BOOKMAKER__'],
                              'fallback_bookmakers': [], 'asian_handicap_risk_tolerance': 0,
                              'min_adjusted_no_loss_probability': 0})
    _, decisions, summary = legacy_build(predictions, as_of, market_reliability,
                                         execution_policy=policy, policy_version=V22)
    decisions = decisions.drop(columns=['loss_risk_tolerance', 'fixture_minimum_loss_probability'], errors='ignore')
    decisions['selection_warnings'] = ''
    decisions['p_profit'] = np.nan
    decisions['raw_p_profit'] = np.nan
    for idx, item in decisions.iterrows():
        reasons = [r for r in str(item.rejection_reasons or '').split('; ') if r]
        # Only the probability and value floors are removed. Missing numbers,
        # failed validation, stale prices and invalid identities remain blockers.
        soft = ('adjusted probability of avoiding loss below ',
                'reliability-adjusted EV below ',
                'independent Dixon-Coles EV is negative or missing',
                'adjusted EV below +1.0% or negative unblended EV',
                'reliability-adjusted probability below minimum')
        reasons = [r for r in reasons if not r.startswith(soft)]
        if parse_label(item.market):
            reasons = [r for r in reasons if r != 'Asian handicap historical reliability unavailable or failed']
            evidence = (market_reliability or {}).get(str(item.league), {}).get('asian_handicap_win', {})
            state = evidence.get('markets', {}).get(item.market, {})
            penalty = state.get('confidence_penalty')
            valid = (evidence.get('version') == VALIDATOR_VERSION
                     and evidence.get('probability_basis') == 'net_profit'
                     and state.get('status') == 'RELIABLE_FOR_RANKING'
                     and isinstance(state.get('development_matches'), int) and state['development_matches'] >= 80
                     and isinstance(state.get('audit_matches'), int) and state['audit_matches'] >= 40
                     and _finite(penalty) and 0 <= float(penalty) <= 1)
            if not valid:
                reasons.append('Asian handicap profitable-win validation unavailable or failed')
                penalty = 1.
            profit = float(item.p_full_win) + float(item.p_half_win)
            # Recompute the independent profitable probability from its full grid.
            from asian_handicap import probabilities
            sources = predictions.loc[predictions.apply(fixture_key, axis=1) == fixture_key(item)]
            try:
                raw = probabilities(sources.iloc[0]['raw_goal_margin_distribution'],
                                    item.handicap_side, item.handicap_line,
                                    float(item.offered_decimal_odds), float(item.per_stake_cost))
                raw_profit = raw['p_full_win'] + raw['p_half_win']
            except (IndexError, KeyError, ValueError, TypeError):
                reasons.append('missing independent profitable-win distribution')
                raw_profit = float('nan')
            adjusted = max(0., min(profit, raw_profit) - float(penalty))
            decisions.loc[idx, ['predicted_probability', 'raw_dc_probability', 'rank_probability',
                                'calibration_penalty', 'conservative_estimated_ev',
                                'validation_status', 'development_validation_matches',
                                'audit_validation_matches', 'audit_brier', 'asian_handicap_validation']] = [
                profit, raw_profit, adjusted, penalty,
                float(item.estimated_ev) - float(penalty)*float(item.offered_decimal_odds),
                state.get('status', 'INSUFFICIENT_HISTORY'), state.get('development_matches'),
                state.get('audit_matches'), state.get('audit_brier'), VALIDATOR_VERSION]
            # Keep actual no-loss/refund settlement fields, but do not mislabel
            # a win-calibration penalty as a calibrated loss-risk estimate.
            decisions.at[idx, 'loss_probability_upper'] = None
        else:
            profit, raw_profit = item.predicted_probability, item.raw_dc_probability
            if all(_finite(v) for v in (profit, raw_profit, item.calibration_penalty,
                                        item.offered_decimal_odds, item.per_stake_cost)):
                adjusted = max(0., min(float(profit), float(raw_profit)) - float(item.calibration_penalty))
                decisions.at[idx, 'rank_probability'] = adjusted
                decisions.at[idx, 'conservative_estimated_ev'] = adjusted*float(item.offered_decimal_odds)-1-float(item.per_stake_cost)
            if item.validation_status != 'RELIABLE_FOR_RANKING':
                reasons.append('profitable-win historical reliability unavailable or failed')
            decisions.at[idx, 'p_full_win'] = profit
            decisions.at[idx, 'p_half_win'] = 0.
        decisions.loc[idx, ['p_profit', 'raw_p_profit', 'probability_basis']] = [profit, raw_profit, 'net_profit']
        current = decisions.loc[idx]
        if not all(_finite(current[k]) for k in ('predicted_probability', 'raw_dc_probability',
                   'rank_probability', 'estimated_ev', 'conservative_estimated_ev', 'raw_dc_ev')):
            reasons.append('missing finite profitable probability or EV')
        elif not all(0 <= float(current[k]) <= 1 for k in ('predicted_probability', 'raw_dc_probability', 'rank_probability')):
            reasons.append('invalid profitable-win probability')
        warnings = []
        if _finite(current.conservative_estimated_ev) and float(current.conservative_estimated_ev) < 0:
            warnings.append('NEGATIVE ADJUSTED EV: high win chance does not imply a profitable price')
        if _finite(current.raw_dc_ev) and float(current.raw_dc_ev) < 0:
            warnings.append('Negative unblended model EV')
        decisions.at[idx, 'selection_warnings'] = '; '.join(warnings)
        decisions.at[idx, 'near_miss_reason'] = '; '.join(warnings) or None
        decisions.at[idx, 'rejection_reasons'] = '; '.join(dict.fromkeys(reasons))
        decisions.at[idx, 'decision'] = 'REJECTED' if reasons else 'ELIGIBLE'
        decisions.at[idx, 'selection_tier'] = None
    pool = decisions.loc[decisions.decision == 'ELIGIBLE'].copy()
    pool['_fixture'] = pool.apply(fixture_key, axis=1) if len(pool) else pd.Series(dtype=str)
    ranked = rank_candidates(pool)
    chosen = ranked.head(12).index
    decisions.loc[decisions.decision == 'ELIGIBLE', 'decision'] = 'NOT_SELECTED'
    decisions.loc[chosen, 'decision'] = 'SHORTLISTED'
    decisions.loc[chosen, 'selection_tier'] = 'STRICT'
    selected = decisions.loc[chosen].reset_index(drop=True)
    for key in ('loss_risk_tolerance', 'risk_tolerance_status', 'min_adjusted_no_loss_probability',
                'max_estimated_loss_probability', 'probability_cutoff_status'):
        summary.pop(key, None)
    summary.update(selection_policy_version=POLICY, selection_objective='MAXIMIZE_PROFITABLE_WIN_PROBABILITY',
        selection_method='Highest calibrated profitable-win probability per fixture, then global top twelve; adjusted EV breaks ties',
        ranking_metric='rank_probability descending; adjusted EV descending; unblended EV descending; odds descending',
        probability_basis='net_profit', min_estimated_ev=None, min_raw_dc_ev=None, ev_required_for_selection=False,
        probability_cutoff_status='NO_FIXED_PROBABILITY_CUTOFF', n_shortlisted=len(selected),
        n_strict_qualified=len(selected), n_provisional_watchlist=0, n_total_candidates=len(selected),
        usable_distinct_fixtures=len(ranked), shortfall=12-len(selected),
        selected_matches_within_48_hours=bool(len(selected)),
        status='TARGET_MET' if len(selected)==12 else 'BELOW_TARGET' if len(selected) else 'NO BET',
        shortfall_reason='Fewer than twelve distinct fixtures have usable quotes and validated evidence within 48 hours' if len(selected)<12 else None,
        negative_adjusted_ev_selections=int((selected.conservative_estimated_ev < 0).sum()),
        legacy_ranking_experiments='NOT_APPLICABLE_TO_WIN_FIRST_POLICY; archived experiments remain graded',
        warning='Full and half wins count as profitable outcomes; refunds do not. No fixed probability or EV floor. Negative EV is explicitly flagged. Estimates are not guarantees; twelve individual picks are not an accumulator recommendation.')
    return selected, decisions.reset_index(drop=True), summary
