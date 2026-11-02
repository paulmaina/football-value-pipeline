"""Versioned shortlist v28: v27 price edge with the cagey-match correction.

VALUE TIER (identical to v27 except):
  * a plus line (line >= +1.0) whose fair reference is the derived matrix
    (type c) is priced from the CORRECTED matrix (narrow_margin) instead:
    reference type "c-cagey", threshold still 3%;
  * where Pinnacle quotes the line (types a/b), Pinnacle stays the fair
    reference; the corrected-vs-Pinnacle gap is recorded;
  * minus lines never use the correction.
Each row records the uncorrected fair odds and whether it qualified only
because of the correction.

v27 stays registered and replayable. The switches in
cagey_correction_config.json turn the correction and the cagey tier on; with
both off, v28 returns exactly v27's picks and decisions.
"""
from __future__ import annotations

from typing import Dict, List, Mapping, Optional

import pandas as pd

import market_implied as mi
import narrow_margin as nm
import price_edge_shortlist as v27
from ah_close_backtest import devig_proportional

POLICY = '48h-ah-price-edge-cagey-v28'
OBJECTIVE = v27.OBJECTIVE
CORRECTED_MIN_LINE = 1.0
TOLERANCE = v27.EDGE_TOLERANCE
REFERENCES = {**v27.REFERENCES, 'c-cagey': 'market-implied, cagey-corrected (derived)'}
VALUE_COLUMNS = ['fair_odds_uncorrected', 'qualified_only_by_correction', 'corrected_fair_probability',
                 'corrected_fair_odds', 'corrected_no_loss_probability', 'corrected_expected_profit',
                 'corrected_vs_pinnacle_gap', 'corrected_cagey_score', 'corrected_fit']
OUTPUT_COLUMNS = [*v27.OUTPUT_COLUMNS[:-1], 'fair_odds_uncorrected', 'qualified_only_by_correction',
                  'corrected_cagey_score', v27.OUTPUT_COLUMNS[-1]]
# v27's guard order, so corrected rows list their reasons the same way.
REASON_ORDER = ('kickoff outside 20-minute to 48-hour window', v27.NO_OFFER, 'offered quote stale',
                v27.NO_REFERENCE, 'Pinnacle quote stale', 'Pinnacle overround outside [1.00, 1.10]',
                'offered and Pinnacle quotes more than 10 minutes apart', 'offered price above 1.15 x fair odds',
                'offered odds above 3.00', 'edge below 2%', 'edge below 3%')
PRICE_REASONS = ('offered price above 1.15 x fair odds', 'edge below 3%')
DEFAULT_SETTINGS = {'cagey_correction_enabled': True, 'cagey_tier_enabled': True}


def corrected_context(pin: Mapping, fit: mi.Fit, fit_info: Mapping, model: Mapping) -> Optional[Dict[str, object]]:
    """Corrected margin distribution for a fixture: fit B, else fit A; None when neither is usable."""
    source = fit if fit.usable else fit_info['fit_a'] if fit_info['fit_a'].usable else None
    if source is None or pin['h2h'] is None or pin['ou25'] is None:
        return None
    margins, probs = mi.margin_distribution(source.matrix)
    p_home, p_draw, p_away = mi.devig_three_way(*pin['h2h'][:3])
    inputs = {'p_over_2_5': devig_proportional(*pin['ou25'][:2])[0], 'p_home': p_home, 'p_away': p_away, 'p_draw': p_draw}
    p2, p3 = nm.corrected_tails(model, nm.margin_tail(margins, probs, 2), nm.margin_tail(margins, probs, 3), inputs)
    return {'fit': source.kind, 'fit_b': fit.usable, 'margins': margins,
            'probs': nm.correct_distribution(margins, probs, p2, p3), 'score': p2}


def corrected_price(context: Mapping, side: str, line: float, price=None) -> Dict[str, object]:
    priced = nm.price_distribution(context['margins'], context['probs'], side, line)
    expected = None
    if price is not None:
        expected = ((priced['p_win'] + priced['p_half_win'] / 2) * (price - 1)
                    - priced['p_loss'] - priced['p_half_loss'] / 2)
    return {'corrected_fair_probability': priced['win_share'], 'corrected_fair_odds': priced['fair_odds'],
            'corrected_no_loss_probability': priced['p_no_loss'], 'corrected_expected_profit': expected}


def _ordered(reasons) -> str:
    unique = list(dict.fromkeys(r for r in reasons if r))
    return '; '.join(sorted(unique, key=lambda r: REASON_ORDER.index(r) if r in REASON_ORDER else len(REASON_ORDER)))


def value_tier_item(item: Dict[str, object], context: Optional[Mapping], correction: bool) -> Dict[str, object]:
    """Annotate one v27 row; re-price derived plus lines (>= +1.0) from the corrected matrix."""
    out = {**item, **{c: None for c in VALUE_COLUMNS}, 'qualified_only_by_correction': False,
           'fair_odds_uncorrected': item.get('fair_odds'), 'selection_policy_version': POLICY}
    if context is None:
        return out
    out.update(corrected_cagey_score=context['score'], corrected_fit=context['fit'])
    side, line, price = item['handicap_side'], float(item['handicap_line']), item.get('offered_decimal_odds')
    out.update(corrected_price(context, side, line, price))
    if item.get('reference_type') in ('a', 'b') and item.get('fair_probability') is not None:
        out['corrected_vs_pinnacle_gap'] = out['corrected_fair_probability'] - item['fair_probability']
    if not (correction and item.get('reference_type') == 'c' and line >= CORRECTED_MIN_LINE and context['fit_b']):
        return out
    q = out['corrected_fair_probability']
    fair = 1 / q
    reasons = [r for r in str(item.get('rejection_reasons') or '').split('; ') if r and r not in PRICE_REASONS]
    out.update(reference_type='c-cagey', reference_market='market-implied fit B, cagey-corrected',
               fair_probability=q, fair_probability_shin=None, fair_odds=fair,
               minimum_odds=fair * (1 + v27.MIN_EDGE_DERIVED), predicted_probability=q)
    if price is not None:
        out['edge'] = price * q - 1
        if price > v27.MAX_FAIR_RATIO * fair:
            reasons.append('offered price above 1.15 x fair odds')
        if out['edge'] + TOLERANCE < v27.MIN_EDGE_DERIVED:
            reasons.append('edge below 3%')
    out['rejection_reasons'] = _ordered(reasons)
    out['decision'] = 'REJECTED' if out['rejection_reasons'] else 'ELIGIBLE'
    out['qualified_only_by_correction'] = item.get('decision') == 'REJECTED' and out['decision'] == 'ELIGIBLE'
    return out


def make_transform(model: Mapping, settings: Mapping):
    def transform(row, items, pin, fit, fit_info, now) -> List[Dict[str, object]]:
        context = corrected_context(pin, fit, fit_info, model)
        return [value_tier_item(item, context, settings['cagey_correction_enabled']) for item in items]
    return transform


def build_shortlist(predictions: pd.DataFrame, as_of, market_reliability=None, execution_policy=None, *,
                    settings: Optional[Mapping] = None, model: Optional[Mapping] = None):
    """Value tier (and, in later changes, the cagey tier). Returns (shortlist, decisions, summary)."""
    settings = {**DEFAULT_SETTINGS, **(settings or {})}
    switched_on = settings['cagey_correction_enabled'] or settings['cagey_tier_enabled']
    if not switched_on:
        selected, decisions, summary = v27.build_shortlist(predictions, as_of, market_reliability, execution_policy)
    else:
        model = model or nm.production_model()
        selected, decisions, summary = v27.build_shortlist(
            predictions, as_of, market_reliability, execution_policy,
            transform=make_transform(model, settings), extra_columns=VALUE_COLUMNS)
    for frame in (selected, decisions):
        if 'selection_policy_version' in frame:
            frame['selection_policy_version'] = POLICY
    only = selected.get('qualified_only_by_correction', pd.Series(dtype=bool)).fillna(False).astype(bool)
    summary.update(selection_policy_version=POLICY, cagey_correction_enabled=bool(settings['cagey_correction_enabled']),
                   cagey_tier_enabled=bool(settings['cagey_tier_enabled']),
                   cagey_model_version=model['version'] if switched_on else None, reference_order=REFERENCES,
                   correction_only_value_picks=int(only.sum()),
                   reference_type_counts={k: int(v) for k, v in selected.reference_type.value_counts().items()}
                   if len(selected) else {},
                   correction_rule='Derived plus lines (>= +1.0) are priced from the cagey-corrected matrix (c-cagey, '
                                   '3% threshold); Pinnacle-quoted lines keep Pinnacle as the fair price; minus lines '
                                   'are never corrected.')
    return selected, decisions, summary
