"""Versioned qualification by positive-return probability, with frozen team research.

Full/half settlement is evaluated at the offered odds after the recorded stake
cost. A push is never a profitable outcome. Expected value is displayed but is
not a qualification gate. Missing context is a warning, not an invented fact.
"""
from __future__ import annotations

import json
import math
import numpy as np
import pandas as pd

RULE = 'team-research-profit-v1'
BASIS = 'team_form_poisson_v1'
COLUMNS = ['profit_model_fair_odds', 'profit_model_edge', 'profit_probability', 'profit_expected_return', 'profit_price_flag', 'research_probability_basis',
           'research_coverage', 'research_warnings', 'research_summary', 'research_details', 'research_sources',
           'research_p_win', 'research_p_half_win', 'research_p_push', 'research_p_half_loss', 'research_p_loss',
           'price_edge_decision', 'price_edge_rejection_reasons']


def context(row, now):
    from team_research import decode, utc, prepare
    evidence = decode(row.get('team_research_json'))
    stamp = utc(evidence.get('observed_at_utc'))
    if evidence and (pd.isna(stamp) or stamp > now):
        return {}, ['research evidence observed after evaluation or missing observation time']
    if not evidence:
        # Legacy cached forecasts stay eligible with an explicit coverage gap.
        evidence = prepare(row, now, {'errors': ['research not collected for this forecast']})
    warnings = list(evidence.get('warnings', []))
    if pd.notna(stamp) and now-stamp > pd.Timedelta(hours=24):
        warnings.append('research older than 24 hours; refresh team news')
    warnings.append('research probability model has not passed a forward calibration gate')
    return evidence, warnings


def probabilities(row, item, evidence):
    from narrow_margin import price_distribution
    from asian_handicap import distribution
    if item.get('market') == 'Over 1.5':
        p = evidence.get('p_over_1_5')
        if p is None:
            return None
        return {'p_win': float(p), 'p_half_win': 0., 'p_push': 0., 'p_half_loss': 0., 'p_loss': 1-float(p)}
    values = distribution(evidence.get('margin_distribution'))
    if not values:
        return None
    margins, mass = np.array(list(values), float), np.array(list(values.values()), float)
    if not np.isfinite(mass).all() or (mass < 0).any() or abs(mass.sum()-1) > 1e-6:
        return None
    if item.get('handicap_side') not in ('home', 'away'):
        return None
    return price_distribution(margins, mass, item['handicap_side'], float(item['handicap_line']))


def annotate(row, item, now, cost):
    """Leave the cagey decision and original Pinnacle fields available for their own lists."""
    from quote_freshness import quote_is_fresh, quote_utc
    from team_research import number
    from price_edge_shortlist import MAX_ODDS, MIN_MINUTES, MAX_HOURS
    item.update(price_edge_decision=item.get('decision'), price_edge_rejection_reasons=item.get('rejection_reasons'))
    evidence, warnings = context(row, now)
    item.update(value_market_group=__import__('price_edge_cagey_shortlist').market_group(item),
                research_probability_basis=BASIS, research_coverage=json.dumps(evidence.get('coverage', {}), sort_keys=True),
                research_warnings='; '.join(warnings), research_summary=json.dumps(evidence.get('form', {}), sort_keys=True),
                research_details=json.dumps({k: v for k, v in evidence.get('evidence', {}).items()
                                            if k not in ('sources', 'recent', 'standings')}, sort_keys=True),
                research_sources=json.dumps(evidence.get('evidence', {}).get('sources', []), sort_keys=True),
                probability_basis='net_profit', value_probability_basis=BASIS, per_stake_cost=cost)
    reasons = []
    price = number(item.get('offered_decimal_odds'))
    kickoff, offered = quote_utc(row.get('kickoff_utc')), quote_utc(item.get('offered_last_update_utc'))
    if kickoff is None or not now+pd.Timedelta(minutes=MIN_MINUTES) <= kickoff <= now+pd.Timedelta(hours=MAX_HOURS):
        reasons.append('kickoff outside 20-minute to 48-hour window')
    if price is None or price <= 1:
        reasons.append('no offered quote at an allowed bookmaker')
    elif price > MAX_ODDS:
        reasons.append('offered odds above 3.00')
    if offered is None or not quote_is_fresh(offered, now):
        reasons.append('offered quote stale or unavailable')
    elif offered > now or (kickoff is not None and offered >= kickoff):
        reasons.append('offered quote not observed before evaluation and kickoff')
    try:
        probs = probabilities(row, item, evidence)
    except (ValueError, TypeError):
        probs = None
    if probs is None:
        reasons.append('team goal-rate distribution unavailable at evaluation')
    else:
        kinds = ('win', 'half_win', 'push', 'half_loss', 'loss')
        mass = np.array([probs['p_' + k] for k in kinds])
        if price is not None:
            returns = np.array([price-1, (price-1)/2, 0, -.5, -1]) - cost
            p_profit = float(mass[returns > 1e-12].sum())
            ev = float(mass @ returns)
            win_stake = mass[0] + mass[1]/2
            model_fair = 1 + (mass[4] + mass[3]/2 + cost)/win_stake if win_stake > 0 else None
            item.update(profit_model_fair_odds=model_fair,
                        profit_model_edge=price/model_fair-1 if model_fair else None, profit_probability=p_profit, profit_expected_return=ev,
                        profit_price_flag='nonnegative expected value' if ev >= 0 else 'negative expected value',
                        predicted_probability=p_profit, rank_probability=p_profit,
                        p_no_loss=float(mass[returns >= -1e-12].sum()))
        item.update({'research_p_' + k: probs['p_' + k] for k in kinds})
    item.update(rejection_reasons='; '.join(reasons), decision='REJECTED' if reasons else 'ELIGIBLE',
                qualified_only_by_correction=False)
    return item


def rank(frame):
    return frame.sort_values(['profit_probability', 'profit_expected_return', 'offered_decimal_odds',
                              'kickoff_utc', 'market', 'bookmaker'],
                             ascending=[False, False, False, True, True, True], kind='stable')


def select(decisions):
    """One pick per match and existing market group. No forced quota or minimum edge."""
    from performance_tracking import fixture_key
    frame = decisions.copy()
    frame['selection_tier'] = frame['selection_tier'].astype(object)
    eligible = frame.loc[frame.decision.eq('ELIGIBLE')].copy()
    if eligible.empty:
        return frame.iloc[0:0].copy(), frame
    eligible['_identity'] = eligible.apply(fixture_key, axis=1) + '#' + eligible.value_market_group
    chosen = rank(eligible).drop_duplicates('_identity').index
    frame.loc[eligible.index, 'decision'] = 'NOT_SELECTED'
    frame.loc[eligible.index, 'rejection_reasons'] = 'higher profit-probability pick chosen in this market group'
    frame.loc[chosen, ['decision', 'rejection_reasons', 'selection_tier']] = ['SHORTLISTED', '', 'STRICT']
    return rank(frame.loc[chosen]).reset_index(drop=True), frame
