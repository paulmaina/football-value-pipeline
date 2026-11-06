"""Versioned shortlist v28: v27 price edge with the cagey-match correction.

Current cagey rule corrected-no-loss-per-market-v4 ranks corrected no-loss
across win/DC/AH/Over 1.5 at odds (1.15, 2.00], with no P(narrow) gate, one per
fixture/market group. See cagey_tier_v3.py and docs/cagey-tier-v3.md. The rules
below describe historical runs, which remain replayable; v3 retains its 67% gate.

VALUE TIER (identical to v27 except):
  * a plus line (line >= +1.0) whose fair reference is the derived matrix
    (type c) is priced from the CORRECTED matrix (narrow_margin) instead:
    reference type "c-cagey", threshold still 3%;
  * where Pinnacle quotes the line (types a/b), Pinnacle stays the fair
    reference; the corrected-vs-Pinnacle gap is recorded;
  * minus lines never use the correction.
Each row records the uncorrected fair odds and whether it qualified only
because of the correction.

CAGEY TIER (a separate list, never merged into the value tier):
  * eligible fixtures: the cagiest 20% by corrected_cagey_score among this
    run's fixtures in the 48h window (cutoff = that 20th percentile, never
    above the training-data 20th percentile; both recorded);
  * candidates: AH +1 .. +2.25, either side, at Pinnacle or 1xBet, with v27's
    freshness, sync, overround and odds guards, and the suspicious-price guard
    (offered <= 1.15 x fair) against both v27's fair odds and the corrected fair odds;
  * qualify if expected profit under the corrected matrix >= 0 (1e-9) AND
    corrected no-loss probability >= 0.85;
  * one row per fixture (highest corrected no-loss, then expected profit, then
    odds), no cap, safest first; a fixture may also be in the value tier.
  The rule above is "value-v1". cagey_correction_config.json may select
  "narrow-63-flagged-v2" instead (cagey_tier_rule):
  * eligible fixtures: P(narrow) = 1 - corrected_cagey_score >= 63%, in the
    48h window (a fixed cutoff, not a share of the run);
  * the same candidates and data guards, but expected profit >= 0 and
    no-loss >= 85% are NOT required: price_flag records "value" or
    "below fair" instead; same one-per-fixture safest-first ranking.
  A run records the rule in its summary (cagey_tier_rule); a run with none
  used value-v1, so earlier runs replay unchanged.

v27 stays registered and replayable. The switches in
cagey_correction_config.json turn the correction and the cagey tier on; with
both off, v28 returns exactly v27's picks and decisions.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, List, Mapping, Optional

import numpy as np
import pandas as pd

import market_implied as mi
import narrow_margin as nm
import price_edge_shortlist as v27
from ah_close_backtest import devig_proportional

POLICY = '48h-ah-price-edge-cagey-v28'
# Display only: how a bet settles under the corrected matrix (never used for selection).
SETTLEMENT_COLUMNS = ['corrected_p_win', 'corrected_p_half_win', 'corrected_p_push', 'corrected_p_half_loss',
                      'corrected_p_loss', 'corrected_p_profit']
OBJECTIVE = v27.OBJECTIVE
VALIDATION_REQUIRED = v27.VALIDATION_REQUIRED
CORRECTED_MIN_LINE = 1.0
TOLERANCE = v27.EDGE_TOLERANCE
REFERENCES = {**v27.REFERENCES, 'c-cagey': 'market-implied, cagey-corrected (derived)'}
VALUE_COLUMNS = ['fair_odds_uncorrected', 'qualified_only_by_correction', 'corrected_fair_probability',
                 'corrected_fair_odds', 'corrected_no_loss_probability', 'corrected_expected_profit',
                 'corrected_vs_pinnacle_gap', 'corrected_cagey_score', 'corrected_fit', *SETTLEMENT_COLUMNS,
                 'uncorrected_matrix_fair_odds']
OUTPUT_COLUMNS = [*v27.OUTPUT_COLUMNS[:-1], 'fair_odds_uncorrected', 'qualified_only_by_correction',
                  'corrected_cagey_score', v27.OUTPUT_COLUMNS[-1]]
# v27's guard order, so corrected rows list their reasons the same way.
REASON_ORDER = ('kickoff outside 20-minute to 48-hour window', v27.NO_OFFER, 'offered quote stale',
                v27.NO_REFERENCE, 'Pinnacle quote stale', 'Pinnacle overround outside [1.00, 1.10]',
                'offered and Pinnacle quotes more than 10 minutes apart', 'offered price above 1.15 x fair odds',
                'offered odds above 3.00', 'edge below 2%', 'edge below 3%')
PRICE_REASONS = ('offered price above 1.15 x fair odds', 'edge below 3%')
# Cagey-tier selection rules. A run records the rule it used; runs that record none used TIER_RULE_VALUE.
TIER_RULE_VALUE = 'value-v1'
TIER_RULE_NARROW = 'narrow-63-flagged-v2'
from cagey_tier_v3 import RULE as TIER_RULE_EXPANDED, RULE_NO_GATE as TIER_RULE_NO_GATE, EXPANDED_RULES
TIER_RULES = (TIER_RULE_VALUE, TIER_RULE_NARROW, *EXPANDED_RULES)
# Value-tier selection rules. A run records the rule it used; runs that record none used VALUE_RULE_ONE.
VALUE_RULE_ONE = 'one-per-fixture-v1'
VALUE_RULE_PER_MARKET = 'per-market-v2'
VALUE_RULE_PROFIT = 'team-research-profit-v1'
VALUE_RULE_LOCAL_RESEARCH = 'local-research-profit-115-200-dc12-v2'
PROFIT_RULES = (VALUE_RULE_PROFIT, VALUE_RULE_LOCAL_RESEARCH)
VALUE_RULES = (VALUE_RULE_ONE, VALUE_RULE_PER_MARKET, *PROFIT_RULES)
# Quote timing rules. skew-5min-v1 (runs that record none): a quote may be stamped up to 5 minutes after the
# evaluation clock (the shared freshness allowance for provider clock skew). observed-by-cutoff-v2: every quote a
# decision uses must be stamped at or before the evaluation clock, which live runs read after fetching the odds;
# the 5-minute allowance remains for capture and diagnostics only.
TIMING_RULE_SKEW = 'skew-5min-v1'
TIMING_RULE_CUTOFF = 'observed-by-cutoff-v2'
TIMING_RULES = (TIMING_RULE_SKEW, TIMING_RULE_CUTOFF)
FUTURE_REASON = 'quote timestamped after evaluation'
FUTURE_TIER_REASON = 'corrected distribution input timestamped after evaluation'
DEFAULT_SETTINGS = {'cagey_correction_enabled': True, 'cagey_tier_enabled': True, 'cagey_tier_rule': TIER_RULE_VALUE,
                    'value_rule': VALUE_RULE_ONE, 'quote_timing_rule': TIMING_RULE_SKEW}
CONFIG = Path(__file__).with_name('cagey_correction_config.json')
SWITCHES = ('cagey_correction_enabled', 'cagey_tier_enabled')
# Everything a replay needs from a run's summary to reproduce its selection.
REPLAY_SETTINGS = (*SWITCHES, 'cagey_tier_rule', 'value_rule', 'quote_timing_rule')


def tier_rule(settings: Mapping) -> str:
    rule = settings.get('cagey_tier_rule') or TIER_RULE_VALUE
    if rule not in TIER_RULES:
        raise ValueError(f'Unknown cagey_tier_rule {rule!r}; expected one of {", ".join(TIER_RULES)}')
    return rule


def timing_rule(settings: Mapping) -> str:
    rule = settings.get('quote_timing_rule') or TIMING_RULE_SKEW
    if rule not in TIMING_RULES:
        raise ValueError(f'Unknown quote_timing_rule {rule!r}; expected one of {", ".join(TIMING_RULES)}')
    return rule


def after(stamp, now) -> bool:
    """True when a quote's timestamp is later than the evaluation clock (not observable at the cutoff)."""
    from quote_freshness import quote_utc
    when = quote_utc(stamp)
    return when is not None and when > now


def value_rule(settings: Mapping) -> str:
    rule = settings.get('value_rule') or VALUE_RULE_ONE
    if rule not in VALUE_RULES:
        raise ValueError(f'Unknown value_rule {rule!r}; expected one of {", ".join(VALUE_RULES)}')
    return rule


# per-market-v2: one value pick per fixture AND market group (Asian handicap, home/away win = AH -0.5,
# double chance = AH +0.5, over 1.5). Every group qualifies at a 1% edge, whatever the fair reference;
# over 1.5 is priced only against Pinnacle's own over/under 1.5.
GROUP_AH = 'asian_handicap'
GROUP_WIN = 'match_winner'
GROUP_DC = 'double_chance'
GROUP_OVER_1_5 = 'over_1_5'
MARKET_GROUPS = (GROUP_AH, GROUP_WIN, GROUP_DC, GROUP_OVER_1_5)
GROUP_MIN_EDGE = 0.01
OVER_1_5 = 'Over 1.5'
VALUE_GROUP_COLUMNS = ['value_market_group']


def market_group(item: Mapping, rule=None) -> str:
    if rule == VALUE_RULE_LOCAL_RESEARCH:
        label = str(item.get('market') or '')
        if label.startswith('Asian Handicap '):
            return GROUP_AH
        if label.startswith('Double Chance '):
            return GROUP_DC
        if label in ('Home win', 'Away win'):
            return GROUP_WIN
    if item.get('market') == OVER_1_5:
        return GROUP_OVER_1_5
    if item.get('market') == 'Double Chance 12':
        return GROUP_DC
    try:
        line = float(item.get('handicap_line'))
    except (TypeError, ValueError):
        return GROUP_AH
    return GROUP_WIN if line == -0.5 else GROUP_DC if line == 0.5 else GROUP_AH


# Missing in old immutable summaries: replay the original v28 execution rules.
EXECUTION_VERSION = 2
EXECUTION_COLUMNS = ['price_edge_execution_version', 'corrected_input_timing_status',
                     'corrected_input_quote_skew_minutes', 'uncorrected_input_timing_status',
                     'uncorrected_input_quote_skew_minutes', 'uncorrected_fit', 'uncorrected_expected_profit',
                     'value_probability_basis', 'value_expected_profit',
                     *['uncorrected_p_' + kind for kind in ('win', 'half_win', 'push', 'half_loss', 'loss')]]


def settlement_basis(row: Mapping, tier='value') -> str:
    """Choose a single distribution; overlap between lists never changes a value pick's source."""
    if tier not in ('value', 'cagey'):
        raise ValueError('Unknown shortlist tier')
    return 'corrected_matrix' if tier == 'cagey' or row.get('reference_type') == 'c-cagey' else 'uncorrected_matrix'


def load_settings(path: Optional[Path] = None) -> Dict[str, object]:
    """Switches, tier and value rules, model version. A switch may be on only when the recorded holdout gate passed."""
    data = json.loads(Path(path or CONFIG).read_text(encoding='utf-8-sig'))
    if any(not isinstance(data.get(name), bool) for name in SWITCHES):
        raise ValueError('cagey_correction_enabled and cagey_tier_enabled must be true or false')
    if any(data[name] for name in SWITCHES) and nm.versions()['gate'].get('gate_result') != 'PASS':
        raise ValueError('The cagey correction may only be switched on after GATE: PASS')
    return {**{name: data[name] for name in (*SWITCHES, 'model_version')}, 'cagey_tier_rule': tier_rule(data),
            'value_rule': value_rule(data), 'quote_timing_rule': timing_rule(data)}
TIER_LINES = (1.0, 1.25, 1.5, 1.75, 2.0, 2.25)
TIER_MIN_NO_LOSS = 0.85
TIER_QUANTILE = 0.20
TIER_GUARDS = ('kickoff outside 20-minute to 48-hour window', 'offered quote stale', v27.NO_REFERENCE,
               'Pinnacle quote stale', 'Pinnacle overround outside [1.00, 1.10]',
               'offered and Pinnacle quotes more than 10 minutes apart', 'offered price above 1.15 x fair odds',
               'offered odds above 3.00')
TIER_FILE = 'cagey_tier_shortlist.csv'
TIER_COLUMNS = ['cagey_tier_decision', 'cagey_tier_reasons', 'pinnacle_fair_odds', 'in_value_tier']
TIER_OUTPUT_COLUMNS = [*OUTPUT_COLUMNS[:-1], 'corrected_no_loss_probability', *SETTLEMENT_COLUMNS,
                       'corrected_fair_odds', 'uncorrected_matrix_fair_odds', 'corrected_expected_profit',
                       'pinnacle_fair_odds', 'in_value_tier']
# narrow-63-flagged-v2: every fixture with P(narrow) >= 63% (corrected cagey score <= 0.37) is listed with its
# safest AH +1..+2.25 line; the price is flagged, not filtered. Data-quality guards still reject.
TIER_MIN_NARROW = 0.63
PRICE_VALUE = 'value'
PRICE_BELOW_FAIR = 'below fair'
NARROW_COLUMNS = ['price_flag']


def tier_columns(rule: str) -> List[str]:
    """Decision columns a tier rule adds; value-v1 adds none, so its runs replay unchanged."""
    if rule in EXPANDED_RULES:
        from cagey_tier_v3 import columns
        return [*TIER_COLUMNS, *NARROW_COLUMNS, *columns(rule)]
    return [*TIER_COLUMNS, *(NARROW_COLUMNS if rule == TIER_RULE_NARROW else [])]


def tier_output_columns(rule: str) -> List[str]:
    if rule in EXPANDED_RULES:
        return list(dict.fromkeys([*TIER_OUTPUT_COLUMNS, *tier_columns(rule)]))
    if rule != TIER_RULE_NARROW:
        return list(TIER_OUTPUT_COLUMNS)
    at = TIER_OUTPUT_COLUMNS.index('corrected_expected_profit') + 1
    return [*TIER_OUTPUT_COLUMNS[:at], 'price_flag', *TIER_OUTPUT_COLUMNS[at:]]


def corrected_context(pin: Mapping, fit: mi.Fit, fit_info: Mapping, model: Mapping) -> Optional[Dict[str, object]]:
    """Corrected margin distribution for a fixture: fit B, else fit A; None when neither is usable."""
    source = fit if fit.usable else fit_info['fit_a'] if fit_info['fit_a'].usable else None
    if source is None or pin['h2h'] is None or pin['ou25'] is None:
        return None
    margins, probs = mi.margin_distribution(source.matrix)
    p_home, p_draw, p_away = mi.devig_three_way(*pin['h2h'][:3])
    inputs = {'p_over_2_5': devig_proportional(*pin['ou25'][:2])[0], 'p_home': p_home, 'p_away': p_away, 'p_draw': p_draw}
    p2, p3 = nm.corrected_tails(model, nm.margin_tail(margins, probs, 2), nm.margin_tail(margins, probs, 3), inputs)
    return {'fit': source.kind, 'fit_b': fit.usable, 'margins': margins, 'uncorrected_probs': probs,
            'probs': nm.correct_distribution(margins, probs, p2, p3), 'score': p2,
            'input_stamps': [stamp for key, stamp in fit_info.get('input_stamps', {}).items()
                             if source.kind == 'B' or key != 'ah_main']}


def corrected_price(context: Mapping, side: str, line: float, price=None, cost=0.0) -> Dict[str, object]:
    priced = nm.price_distribution(context['margins'], context['probs'], side, line)
    expected = None
    no_loss = priced['p_no_loss']
    profit_probability = priced['p_win'] + priced['p_half_win']
    if price is not None:
        expected = ((priced['p_win'] + priced['p_half_win'] / 2) * (price - 1)
                    - priced['p_loss'] - priced['p_half_loss'] / 2 - cost)
        if cost:
            returns = {'p_win': price - 1 - cost, 'p_half_win': (price - 1) / 2 - cost,
                       'p_push': -cost, 'p_half_loss': -0.5 - cost, 'p_loss': -1 - cost}
            no_loss = sum(priced[key] for key, gain in returns.items() if gain >= -TOLERANCE)
            profit_probability = sum(priced[key] for key, gain in returns.items() if gain > TOLERANCE)
    uncorrected = (nm.price_distribution(context['margins'], context['uncorrected_probs'], side, line)['fair_odds']
                   if 'uncorrected_probs' in context else None)
    return {'corrected_fair_probability': priced['win_share'], 'corrected_fair_odds': priced['fair_odds'],
            'corrected_no_loss_probability': no_loss, 'corrected_expected_profit': expected,
            'corrected_p_win': priced['p_win'], 'corrected_p_half_win': priced['p_half_win'],
            'corrected_p_push': priced['p_push'], 'corrected_p_half_loss': priced['p_half_loss'],
            'corrected_p_loss': priced['p_loss'], 'corrected_p_profit': profit_probability,
            'uncorrected_matrix_fair_odds': uncorrected}


def _ordered(reasons) -> str:
    unique = list(dict.fromkeys(r for r in reasons if r))
    return '; '.join(sorted(unique, key=lambda r: REASON_ORDER.index(r) if r in REASON_ORDER else len(REASON_ORDER)))


def tier_candidate(item: Mapping, out: Dict[str, object], context: Optional[Mapping],
                   rule: str = TIER_RULE_VALUE) -> Dict[str, object]:
    """Per-candidate cagey-tier checks; the run-level fixture cutoff is applied afterwards.

    value-v1: expected profit >= 0 and no-loss >= 85% are requirements.
    narrow-63-flagged-v2: they are not; the price is recorded in price_flag instead.
    """
    line = float(item['handicap_line'])
    empty = {'cagey_tier_decision': None, 'cagey_tier_reasons': None,
             **({'price_flag': None} if rule == TIER_RULE_NARROW else {})}
    if line not in TIER_LINES or item.get('offered_decimal_odds') is None:
        return empty
    reasons = [r for r in str(item.get('rejection_reasons') or '').split('; ') if r in TIER_GUARDS]
    flag = None
    if context is None:
        reasons.append('no corrected price')
    else:
        # Data-quality guard: a price far above the corrected fair odds is more likely a bad quote than value.
        if (item['offered_decimal_odds'] > v27.MAX_FAIR_RATIO * out['corrected_fair_odds']
                and 'offered price above 1.15 x fair odds' not in reasons):
            reasons.append('offered price above 1.15 x fair odds')
        below_fair = out['corrected_expected_profit'] + TOLERANCE < 0
        if rule == TIER_RULE_NARROW:
            flag = PRICE_BELOW_FAIR if below_fair else PRICE_VALUE
        else:
            if below_fair:
                reasons.append('expected profit below 0 under the corrected matrix')
            if out['corrected_no_loss_probability'] + TOLERANCE < TIER_MIN_NO_LOSS:
                reasons.append('corrected no-loss probability below 85%')
    result = {'cagey_tier_decision': 'REJECTED' if reasons else 'ELIGIBLE', 'cagey_tier_reasons': '; '.join(reasons)}
    if rule == TIER_RULE_NARROW:
        result['price_flag'] = flag
    return result


def value_tier_item(item: Dict[str, object], context: Optional[Mapping], correction: bool,
                    tier=False) -> Dict[str, object]:
    """`tier`: False (no cagey tier), True (value-v1) or a tier rule name."""
    """Annotate one v27 row; re-price derived plus lines (>= +1.0) from the corrected matrix."""
    out = {**item, **{c: None for c in VALUE_COLUMNS}, 'qualified_only_by_correction': False,
           'fair_odds_uncorrected': item.get('fair_odds'), 'selection_policy_version': POLICY,
           'cagey_tier_decision': None, 'cagey_tier_reasons': None, 'in_value_tier': None,
           'pinnacle_fair_odds': item.get('fair_odds') if item.get('reference_type') == 'a' else None}
    if context is not None:
        out.update(corrected_cagey_score=context['score'], corrected_fit=context['fit'])
        out.update(corrected_price(context, item['handicap_side'], float(item['handicap_line']),
                                   item.get('offered_decimal_odds'), item.get('per_stake_cost', 0.0)))
    if tier:
        out.update(tier_candidate(item, out, context, TIER_RULE_VALUE if tier is True else tier))
    if context is None:
        return out
    line, price = float(item['handicap_line']), item.get('offered_decimal_odds')
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


# ---------------------------------------------------------------------------
# Correction monitoring (evidence only; never read by a decision)
# ---------------------------------------------------------------------------

MONITOR_FILE = 'cagey_correction_monitoring.csv'
MONITOR_VERSION = 'cagey-correction-monitoring-v1'
MONITOR_LINES = (1.0, 1.25, 1.5, 1.75, 2.0)
MONITOR_BOOKS = ('Pinnacle', '1xBet')


def _line_key(side: str, line: float) -> str:
    return f'{side}_plus_{line:g}'.replace('.', '_')


MONITOR_PRICE_COLUMNS = [f'{_line_key(side, line)}_{kind}' for side in ('home', 'away') for line in MONITOR_LINES
                         for kind in ('corrected_fair_odds', 'uncorrected_fair_odds', 'pinnacle_odds', 'pinnacle_odds_utc',
                                      'onexbet_odds', 'onexbet_odds_utc')]
BOOK_COLUMNS = {'Pinnacle': 'pinnacle_odds', '1xBet': 'onexbet_odds'}


def usable_quote(stamp, generated, kickoff, strict=False) -> bool:
    """A bookmaker price counts as pre-match evidence only if its quote was fresh at generation
    (the selection freshness rule) and timestamped before kickoff; `strict` (observed-by-cutoff-v2)
    also requires it to be stamped at or before generation."""
    from quote_freshness import quote_is_fresh, quote_utc
    when, kick = quote_utc(stamp), quote_utc(kickoff)
    return (when is not None and kick is not None and when < kick and quote_is_fresh(stamp, generated)
            and not (strict and when > quote_utc(generated)))
MONITOR_COLUMNS = ['monitoring_version', 'generated_at_utc', 'league', 'home_team', 'away_team', 'fixture_id',
                   'kickoff_utc', 'model_version', 'quintile_model_sha256', 'status', 'exclusion_reason', 'fit',
                   'latest_input_quote_utc', 'corrected_p2', 'corrected_p3', 'uncorrected_p2', 'uncorrected_p3',
                   'corrected_cagey_quintile', *MONITOR_PRICE_COLUMNS]


def monitoring_record(row: Mapping, items: List[Mapping], fit: mi.Fit, fit_info: Mapping, now: pd.Timestamp,
                      context: Optional[Mapping], model: Mapping, quintiles: Mapping,
                      *, used_inputs_only=False, strict=False) -> Dict[str, object]:
    """One fixture's pre-match evidence, from the distribution and correction this run already computed."""
    from quote_freshness import quote_utc
    inputs = context['input_stamps'] if used_inputs_only and context is not None else fit_info['stamps']
    stamps = [t for t in (quote_utc(s) for s in inputs) if t is not None]
    record = {c: None for c in MONITOR_COLUMNS}
    record.update({k: row.get(k) for k in ('league', 'home_team', 'away_team', 'fixture_id', 'kickoff_utc')},
                  monitoring_version=MONITOR_VERSION, generated_at_utc=now.isoformat(), model_version=model['version'],
                  quintile_model_sha256=quintiles['model_sha256'],
                  latest_input_quote_utc=max(stamps).isoformat() if stamps else None)
    if used_inputs_only and context is not None and (
            not stamps or (max(stamps) - min(stamps)).total_seconds() / 60 > v27.MAX_QUOTE_SKEW_MINUTES):
        record.update(status='UNUSABLE', exclusion_reason='corrected distribution inputs unavailable or more than 10 minutes apart')
        return record
    if strict and stamps and max(stamps) > now:
        record.update(status='UNUSABLE', exclusion_reason='distribution inputs timestamped after evaluation')
        return record
    if context is None:
        reasons = '; '.join(dict.fromkeys(fit.reasons + fit_info['fit_a'].reasons))
        record.update(status='UNUSABLE', exclusion_reason=f'no usable market-implied fit ({reasons or "missing quotes"})')
        return record
    margins, corrected, raw = context['margins'], context['probs'], context['uncorrected_probs']
    record.update(status='USABLE', exclusion_reason='', fit=context['fit'],
                  corrected_p2=context['score'], corrected_p3=nm.margin_tail(margins, corrected, 3),
                  uncorrected_p2=nm.margin_tail(margins, raw, 2), uncorrected_p3=nm.margin_tail(margins, raw, 3),
                  corrected_cagey_quintile=nm.quintile_label(context['score'], quintiles['boundaries']))
    # Only prices whose own quote passes the freshness and pre-kickoff checks; each keeps its timestamp.
    offered = {}
    for item in items:
        book, price, stamp = item.get('bookmaker'), item.get('offered_decimal_odds'), item.get('offered_last_update_utc')
        if (book in MONITOR_BOOKS and pd.notna(price) and item.get('handicap_side') in ('home', 'away')
                and usable_quote(stamp, now, row.get('kickoff_utc'), strict)):
            offered.setdefault((item['handicap_side'], float(item['handicap_line']), book), (price, stamp))
    for side in ('home', 'away'):
        for line in MONITOR_LINES:
            key = _line_key(side, line)
            record[f'{key}_corrected_fair_odds'] = nm.price_distribution(margins, corrected, side, line)['fair_odds']
            record[f'{key}_uncorrected_fair_odds'] = nm.price_distribution(margins, raw, side, line)['fair_odds']
            for book, column in BOOK_COLUMNS.items():
                price, stamp = offered.get((side, line, book), (None, None))
                record[f'{key}_{column}'], record[f'{key}_{column}_utc'] = price, stamp
    return record


def write_monitoring(records: List[Mapping], raw: Path) -> List[Mapping]:
    from performance_tracking import write_csv
    write_csv(Path(raw) / MONITOR_FILE, list(records), MONITOR_COLUMNS)
    return list(records)


def record_monitoring(summary: Dict[str, object], records: List[Mapping], raw: Path) -> None:
    """Write a v28 run's monitoring records and bind their version into its immutable summary.

    Runs generated before monitoring existed carry no version, so their replay never requires the file.
    """
    if summary.get('selection_policy_version') != POLICY:
        return
    write_monitoring(records, raw)
    summary['correction_monitoring_version'] = MONITOR_VERSION


def make_transform(model: Optional[Mapping], settings: Mapping, monitor: Optional[list] = None, cost=0.0,
                   policy: Optional[Mapping] = None):
    quintiles = nm.load_quintiles(model) if monitor is not None and model is not None else None
    per_market = value_rule(settings) in (VALUE_RULE_PER_MARKET, *PROFIT_RULES)
    strict = timing_rule(settings) == TIMING_RULE_CUTOFF

    def transform(row, items, pin, fit, fit_info, now) -> List[Dict[str, object]]:
        context = corrected_context(pin, fit, fit_info, model) if model is not None else None
        raw_context = None
        if fit.usable:
            margins, probs = mi.margin_distribution(fit.matrix)
            raw_context = {'margins': margins, 'probs': probs, 'input_stamps': list(fit_info['input_stamps'].values())}
        if monitor is not None and model is not None:
            monitor.append(monitoring_record(row, items, fit, fit_info, now, context, model, quintiles,
                           used_inputs_only=settings['price_edge_execution_version'] >= EXECUTION_VERSION,
                           strict=strict))
        expanded = settings['cagey_tier_enabled'] and tier_rule(settings) in EXPANDED_RULES
        if expanded and context is not None:
            from cagey_tier_v3 import corrected_grid
            source = fit if fit.usable else fit_info['fit_a']
            context = {**context, 'matrix': corrected_grid(context, source.matrix)}
        tier = tier_rule(settings) if settings['cagey_tier_enabled'] and not expanded else False
        out = []
        for item in items:
            if settings['price_edge_execution_version'] >= EXECUTION_VERSION:
                item = {**item, 'per_stake_cost': cost}
            decision = value_tier_item(item, context, settings['cagey_correction_enabled'], tier)
            if per_market:
                apply_group_threshold(decision)
            if settings['price_edge_execution_version'] >= EXECUTION_VERSION:
                if raw_context is not None:
                    priced = nm.price_distribution(raw_context['margins'], raw_context['probs'],
                                                   item['handicap_side'], float(item['handicap_line']))
                    decision.update({'uncorrected_' + key: priced[key]
                                     for key in ('p_win', 'p_half_win', 'p_push', 'p_half_loss', 'p_loss')})
                    price = item.get('offered_decimal_odds')
                    decision.update(uncorrected_fit='B', uncorrected_expected_profit=None if price is None else
                        (priced['p_win'] + priced['p_half_win'] / 2) * (price - 1)
                        - priced['p_loss'] - priced['p_half_loss'] / 2 - cost)
                apply_execution_checks(decision, context, raw_context)
            out.append(decision)
        if per_market:
            execution = settings['price_edge_execution_version'] >= EXECUTION_VERSION
            for decision in over_1_5_items(row, pin, fit, fit_info, now, policy, cost if execution else 0.0, execution):
                if execution:
                    apply_execution_checks(decision, context, raw_context)
                out.append(decision)
        if value_rule(settings) == VALUE_RULE_LOCAL_RESEARCH:
            from profit_shortlist import dc12_candidates
            out.extend(dc12_candidates(row, pin, fit, fit_info, now, policy))
        if strict:
            for decision in out:
                apply_cutoff_timing(decision, fit_info, context, now)
        if expanded:
            from cagey_tier_v3 import annotate
            for decision in out:
                annotate(decision, context, row, now, policy, cost, rule=tier_rule(settings))
        return out
    return transform


def apply_cutoff_timing(item: Dict[str, object], fit_info: Mapping, context: Optional[Mapping], now) -> None:
    """observed-by-cutoff-v2: reject a decision that uses any quote stamped after the evaluation clock.

    Value decision: the offer, its Pinnacle reference and, for fit-priced lines (c, c-cagey), the fit's
    inputs. Cagey tier: the offer, its Pinnacle reference and the corrected distribution's inputs.
    """
    own = [item.get('offered_last_update_utc'), item.get('pinnacle_last_update_utc')]
    fit_inputs = list((fit_info.get('input_stamps') or {}).values())
    used = own + (fit_inputs if item.get('reference_type') in ('c', 'c-cagey') else [])
    if any(after(s, now) for s in used):
        item['rejection_reasons'] = _ordered([*str(item.get('rejection_reasons') or '').split('; '), FUTURE_REASON])
        item['decision'] = 'REJECTED'
        item['qualified_only_by_correction'] = False
    if item.get('cagey_tier_decision'):
        tier_inputs = own + (list(context['input_stamps']) if context is not None else [])
        if any(after(s, now) for s in tier_inputs):
            reason = FUTURE_REASON if any(after(s, now) for s in own) else FUTURE_TIER_REASON
            item['cagey_tier_reasons'] = '; '.join(filter(None, [item.get('cagey_tier_reasons'), reason]))
            item['cagey_tier_decision'] = 'REJECTED'


def apply_group_threshold(item: Dict[str, object]) -> None:
    """per-market-v2: tag the market group; every priced candidate qualifies at a 1% edge.

    That covers every group and every fair reference: Pinnacle (a/b), the market-implied fit (c) and the
    cagey-corrected fit (c-cagey). The data guards and their reasons are untouched.
    """
    item['value_market_group'] = market_group(item)
    edge, fair = item.get('edge'), item.get('fair_odds')
    if item.get('reference_type') is None or edge is None:
        return
    reasons = [r for r in str(item.get('rejection_reasons') or '').split('; ') if r and not r.startswith('edge below ')]
    if edge + TOLERANCE < GROUP_MIN_EDGE:
        reasons.append(f'edge below {GROUP_MIN_EDGE:.0%}')
    item.update(min_edge=GROUP_MIN_EDGE, minimum_odds=fair * (1 + GROUP_MIN_EDGE) if fair else None,
                rejection_reasons=_ordered(reasons), decision='REJECTED' if reasons else 'ELIGIBLE')
    if item.get('reference_type') == 'c-cagey':
        # Qualified only because of the correction: the uncorrected fair price would not give 1%.
        price, uncorrected = item.get('offered_decimal_odds'), item.get('fair_odds_uncorrected')
        plain = price / uncorrected - 1 if price and uncorrected else None
        item['qualified_only_by_correction'] = bool(
            item['decision'] == 'ELIGIBLE' and (plain is None or plain + TOLERANCE < GROUP_MIN_EDGE))


def over_1_5_offers(row: Mapping, policy: Mapping) -> List[tuple]:
    """Allowed-book over 1.5 prices: (bookmaker, price, stamp), newest per book (main market on ties)."""
    from asian_handicap import bookmaker
    from quote_freshness import quote_utc
    from quote_policy import usable_bookmaker
    best = {}
    for quote in v27._json_list(row.get('price_edge_quotes')):
        if not isinstance(quote, dict) or quote.get('market') != 'totals' or quote.get('point') != 1.5:
            continue
        name = bookmaker(quote.get('bookmaker'))
        price = v27._price((quote.get('prices') or {}).get('over'))
        if name is None or price is None or not usable_bookmaker(name, policy):
            continue
        when = quote_utc(quote.get('last_update_utc'))
        rank = (when or pd.Timestamp.min.tz_localize('UTC'), quote.get('market_key') == 'totals')
        if name not in best or rank > best[name][0]:
            best[name] = (rank, (name, price, quote.get('last_update_utc')))
    return [offer for _, offer in sorted(best.values(), key=lambda v: v[1][0])]


def over_1_5_items(row: Mapping, pin: Mapping, fit: mi.Fit, fit_info: Mapping, now: pd.Timestamp, policy: Mapping,
                   cost: float, settlement: bool) -> List[Dict[str, object]]:
    """per-market-v2 over 1.5 candidates priced against Pinnacle's own over/under 1.5 (fail closed).

    Guards are v27's: kick-off window, fresh offer, fresh Pinnacle pair, Pinnacle overround [1.00, 1.10],
    quotes at most 10 minutes apart, offered <= 1.15 x fair, odds <= 3.00; then edge >= 1%.
    """
    from ah_close_backtest import devig_shin
    from quote_freshness import quote_is_fresh, quote_utc
    base = {**v27.fixture_base(row, pin, fit, fit_info, now), 'selection_policy_version': POLICY,
            **{c: None for c in VALUE_COLUMNS}, 'qualified_only_by_correction': False,
            'cagey_tier_decision': None, 'cagey_tier_reasons': None, 'in_value_tier': None, 'pinnacle_fair_odds': None}
    kickoff = quote_utc(row.get('kickoff_utc'))
    in_window = kickoff is not None and (now + pd.Timedelta(minutes=v27.MIN_MINUTES) <= kickoff
                                         <= now + pd.Timedelta(hours=v27.MAX_HOURS))
    ref = pin.get('ou15')
    p_over_fit = None
    if settlement and fit.usable:
        goals = np.arange(fit.matrix.shape[0])
        p_over_fit = float(fit.matrix[(goals[:, None] + goals[None, :]) >= 2].sum() / fit.matrix.sum())
    model_p = v27._price(row.get('p_over_1_5'))
    model_p = None if model_p is None else float(row.get('p_over_1_5'))
    items = []
    for name, price, stamp in over_1_5_offers(row, policy):
        reasons = [] if in_window else ['kickoff outside 20-minute to 48-hour window']
        item = {**base, 'market': OVER_1_5, 'market_to_bet': OVER_1_5, 'ah_equivalent': None, 'handicap_side': None,
                'handicap_line': None, 'side_role': None, 'source_market': 'totals', 'bookmaker': name,
                'offered_decimal_odds': price, 'offered_last_update_utc': stamp,
                'offered_quote_age_minutes': v27._age_minutes(stamp, now), 'tagged_probe': False,
                'value_market_group': GROUP_OVER_1_5, 'per_stake_cost': cost}
        if not quote_is_fresh(stamp, now):
            reasons.append('offered quote stale')
        if ref is None:
            reasons.append(v27.NO_REFERENCE)
            item.update(fair_probability=None, fair_odds=None, edge=None, reference_type=None)
        else:
            over, under, ref_stamp = ref
            q = devig_proportional(over, under)[0]
            fair = 1 / q
            overround = 1 / over + 1 / under
            item.update(reference_type='a', reference_market='Pinnacle O/U 1.5', fair_probability=q,
                        fair_probability_shin=devig_shin(over, under)[0], fair_odds=fair, min_edge=GROUP_MIN_EDGE,
                        minimum_odds=fair * (1 + GROUP_MIN_EDGE), pinnacle_overround=overround,
                        pinnacle_last_update_utc=ref_stamp, pinnacle_quote_age_minutes=v27._age_minutes(ref_stamp, now),
                        edge=price * q - 1, edge_shin=price * devig_shin(over, under)[0] - 1)
            if not quote_is_fresh(ref_stamp, now):
                reasons.append('Pinnacle quote stale')
            low, high = v27.PINNACLE_OVERROUND
            if not low <= overround <= high:
                reasons.append('Pinnacle overround outside [1.00, 1.10]')
            offered, pinned = quote_utc(stamp), quote_utc(ref_stamp)
            skew = abs((offered - pinned).total_seconds()) / 60 if offered is not None and pinned is not None else None
            item['quote_skew_minutes'] = skew
            if skew is None or skew > v27.MAX_QUOTE_SKEW_MINUTES:
                reasons.append('offered and Pinnacle quotes more than 10 minutes apart')
            if price > v27.MAX_FAIR_RATIO * fair:
                reasons.append('offered price above 1.15 x fair odds')
            if price > v27.MAX_ODDS:
                reasons.append('offered odds above 3.00')
            if item['edge'] + TOLERANCE < GROUP_MIN_EDGE:
                reasons.append(f'edge below {GROUP_MIN_EDGE:.0%}')
        q = item.get('fair_probability')
        item.update(pinnacle_no_loss_probability=q, p_no_loss=q, rank_probability=q, predicted_probability=q,
                    probability_basis='pinnacle_fair_win_share', model_win_share=model_p,
                    model_vs_pinnacle_gap=None if model_p is None or q is None else model_p - q,
                    rejection_reasons=_ordered(reasons), decision='REJECTED' if reasons else 'ELIGIBLE')
        if settlement:
            # Execution v2 settlement fields from fit B, as for every other uncorrected value pick (staking).
            if p_over_fit is not None:
                item.update(uncorrected_fit='B', uncorrected_p_win=p_over_fit, uncorrected_p_half_win=0.0,
                            uncorrected_p_push=0.0, uncorrected_p_half_loss=0.0, uncorrected_p_loss=1 - p_over_fit,
                            uncorrected_expected_profit=p_over_fit * (price - 1) - (1 - p_over_fit) - cost)
        items.append(item)
    return items


def apply_execution_checks(item: Dict[str, object], context: Optional[Mapping], raw_context: Optional[Mapping] = None) -> None:
    """v28 execution v2: synchronise every used correction input with the offer.

    Cost qualification/sizing use the distribution matching the fair reference;
    direct Pinnacle price edge remains separately reported as a gross statistic.
    """
    from quote_freshness import quote_utc
    offer = quote_utc(item.get('offered_last_update_utc'))
    for prefix, distribution in (('corrected', context), ('uncorrected', raw_context)):
        stamps = [quote_utc(s) for s in distribution['input_stamps']] if distribution else []
        times = [offer, *stamps]
        skew = (max(times) - min(times)).total_seconds() / 60 if times and all(t is not None for t in times) else None
        synchronized = bool(stamps) and skew is not None and skew <= v27.MAX_QUOTE_SKEW_MINUTES
        item[prefix + '_input_timing_status'] = 'SYNCHRONIZED' if synchronized else 'UNAVAILABLE_OR_UNSYNCHRONIZED'
        item[prefix + '_input_quote_skew_minutes'] = skew
    item['price_edge_execution_version'] = EXECUTION_VERSION
    basis = settlement_basis(item)
    prefix = basis.removesuffix('_matrix')
    item.update(value_probability_basis=basis, value_expected_profit=item.get(prefix + '_expected_profit'))
    if item.get('cagey_tier_decision') and item['corrected_input_timing_status'] != 'SYNCHRONIZED':
        item['cagey_tier_reasons'] = '; '.join(filter(None, [item['cagey_tier_reasons'],
                                            'corrected distribution inputs and offer more than 10 minutes apart or unavailable']))
        item['cagey_tier_decision'] = 'REJECTED'
    if item.get('per_stake_cost', 0) > 0:
        expected = item['value_expected_profit']
        reason = ('net profit unavailable without synchronized settlement inputs' if item[prefix + '_input_timing_status'] != 'SYNCHRONIZED'
                  else 'expected profit after stake cost below 0' if expected is None or expected + TOLERANCE < 0 else None)
        if reason:
            item['rejection_reasons'] = '; '.join(filter(None, [item.get('rejection_reasons'), reason]))
            item['decision'] = 'REJECTED'
            item['qualified_only_by_correction'] = False


def _tier_rank(frame: pd.DataFrame) -> pd.DataFrame:
    """Safest first: corrected no-loss probability, then expected profit, then odds."""
    return frame.sort_values(['corrected_no_loss_probability', 'corrected_expected_profit', 'offered_decimal_odds',
                              'kickoff_utc', 'market', 'bookmaker'],
                             ascending=[False, False, False, True, True, True], kind='stable')


def apply_cagey_tier(decisions: pd.DataFrame, selected: pd.DataFrame, now: pd.Timestamp,
                     model: Mapping, rule: str = TIER_RULE_VALUE) -> Dict[str, object]:
    """Run-level cutoff and one-per-fixture selection for the cagey tier (updates `decisions`)."""
    if rule in EXPANDED_RULES:
        from cagey_tier_v3 import select
        return select(decisions, selected, rule=rule)
    if rule == TIER_RULE_NARROW:
        return _apply_narrow_tier(decisions, selected, now)
    from performance_tracking import fixture_key
    for column in TIER_COLUMNS:
        decisions[column] = decisions[column].astype(object)
    keys = decisions.apply(fixture_key, axis=1) if len(decisions) else pd.Series(dtype=str)
    kick = pd.to_datetime(decisions.kickoff_utc, utc=True, errors='coerce')
    in_window = (kick >= now + pd.Timedelta(minutes=v27.MIN_MINUTES)) & (kick <= now + pd.Timedelta(hours=v27.MAX_HOURS))
    scored = in_window & decisions.corrected_cagey_score.notna()
    scores = (pd.DataFrame({'_fixture': keys[scored], 'score': decisions.corrected_cagey_score[scored]})
              .drop_duplicates('_fixture').score.astype(float))
    run_p20 = float(scores.quantile(TIER_QUANTILE)) if len(scores) else None
    training_p20 = float(model['training_cagey_p20'])
    cutoff = min(run_p20, training_p20) if run_p20 is not None else None
    candidates = decisions.cagey_tier_decision.notna()
    picked = set(selected.apply(fixture_key, axis=1)) if len(selected) else set()
    decisions.loc[candidates, 'in_value_tier'] = keys[candidates].isin(picked)
    score = pd.to_numeric(decisions.corrected_cagey_score, errors='coerce')
    cagey = score <= cutoff + TOLERANCE if cutoff is not None else pd.Series(False, index=decisions.index)
    for idx in decisions.index[candidates & ~cagey]:
        prior = decisions.at[idx, 'cagey_tier_reasons']
        decisions.at[idx, 'cagey_tier_reasons'] = '; '.join(filter(None, [prior, 'not among the cagiest 20% of fixtures']))
        decisions.at[idx, 'cagey_tier_decision'] = 'REJECTED'
    eligible = decisions.loc[decisions.cagey_tier_decision == 'ELIGIBLE'].copy()
    # Index-aligned: assign() of a Series onto an empty frame would adopt every row.
    eligible['_fixture'] = keys.reindex(eligible.index)
    chosen = _tier_rank(eligible).drop_duplicates('_fixture').index
    decisions.loc[eligible.index, 'cagey_tier_decision'] = 'NOT_SELECTED'
    decisions.loc[chosen, 'cagey_tier_decision'] = 'SHORTLISTED'
    return {'enabled': True, 'n_shortlisted': int(len(chosen)), 'fixtures_in_window': int(len(scores)),
            'cutoff_run_p20': run_p20, 'cutoff_training_p20': training_p20, 'cutoff_used': cutoff,
            'in_both_tiers': int(decisions.loc[chosen, 'in_value_tier'].fillna(False).astype(bool).sum()),
            'even_odds_picks': int(decisions.loc[chosen, 'even_odds'].fillna(False).astype(bool).sum()),
            'rule': 'cagiest 20% of this run (never above the training 20th percentile); AH +1..+2.25 at Pinnacle '
                    'or 1xBet; expected profit >= 0 and no-loss >= 85% under the corrected matrix; one per fixture'}


def _apply_narrow_tier(decisions: pd.DataFrame, selected: pd.DataFrame, now: pd.Timestamp) -> Dict[str, object]:
    """narrow-63-flagged-v2: every in-window fixture with P(narrow) >= 63%, its safest guarded line, price flagged."""
    from performance_tracking import fixture_key
    for column in tier_columns(TIER_RULE_NARROW):
        decisions[column] = decisions[column].astype(object)
    keys = decisions.apply(fixture_key, axis=1) if len(decisions) else pd.Series(dtype=str)
    kick = pd.to_datetime(decisions.kickoff_utc, utc=True, errors='coerce')
    in_window = (kick >= now + pd.Timedelta(minutes=v27.MIN_MINUTES)) & (kick <= now + pd.Timedelta(hours=v27.MAX_HOURS))
    score = pd.to_numeric(decisions.corrected_cagey_score, errors='coerce')
    scored = in_window & score.notna()
    fixtures = pd.DataFrame({'_fixture': keys[scored], 'score': score[scored]}).drop_duplicates('_fixture')
    cutoff = 1 - TIER_MIN_NARROW
    candidates = decisions.cagey_tier_decision.notna()
    picked = set(selected.apply(fixture_key, axis=1)) if len(selected) else set()
    decisions.loc[candidates, 'in_value_tier'] = keys[candidates].isin(picked)
    narrow = score <= cutoff + TOLERANCE
    for idx in decisions.index[candidates & ~narrow]:
        prior = decisions.at[idx, 'cagey_tier_reasons']
        decisions.at[idx, 'cagey_tier_reasons'] = '; '.join(
            filter(None, [prior, f'P(narrow) below {TIER_MIN_NARROW:.0%}']))
        decisions.at[idx, 'cagey_tier_decision'] = 'REJECTED'
    eligible = decisions.loc[decisions.cagey_tier_decision == 'ELIGIBLE'].copy()
    eligible['_fixture'] = keys.reindex(eligible.index)
    chosen = _tier_rank(eligible).drop_duplicates('_fixture').index
    decisions.loc[eligible.index, 'cagey_tier_decision'] = 'NOT_SELECTED'
    decisions.loc[chosen, 'cagey_tier_decision'] = 'SHORTLISTED'
    flags = decisions.loc[chosen, 'price_flag']
    return {'enabled': True, 'n_shortlisted': int(len(chosen)), 'fixtures_in_window': int(len(fixtures)),
            'fixtures_at_or_above_cutoff': int((fixtures.score <= cutoff + TOLERANCE).sum()),
            'min_p_narrow': TIER_MIN_NARROW, 'cutoff_used': cutoff,
            'value_picks': int((flags == PRICE_VALUE).sum()), 'below_fair_picks': int((flags == PRICE_BELOW_FAIR).sum()),
            'in_both_tiers': int(decisions.loc[chosen, 'in_value_tier'].fillna(False).astype(bool).sum()),
            'even_odds_picks': int(decisions.loc[chosen, 'even_odds'].fillna(False).astype(bool).sum()),
            'rule': f'every fixture with P(narrow) >= {TIER_MIN_NARROW:.0%} (corrected cagey score <= {cutoff:.2f}) in '
                    'the 20-minute to 48-hour window; its safest AH +1..+2.25 line at Pinnacle or 1xBet after the data '
                    'guards; price_flag says whether expected profit after stake cost under the corrected matrix is >= 0 (value) or '
                    'not (below fair); one per fixture',
            'rule_version': TIER_RULE_NARROW}


def cagey_tier_list(decisions: pd.DataFrame) -> pd.DataFrame:
    """The cagey-tier shortlist (separate from the value tier), safest first."""
    expanded = 'cagey_tier_rule' in decisions and (decisions.empty or decisions.cagey_tier_rule.isin(EXPANDED_RULES).any())
    recorded = decisions.cagey_tier_rule.dropna() if expanded else pd.Series(dtype=str)
    rule = (recorded.iloc[0] if len(recorded) else TIER_RULE_NO_GATE if 'narrow_support_version' in decisions else TIER_RULE_EXPANDED) if expanded else TIER_RULE_NARROW if 'price_flag' in decisions else TIER_RULE_VALUE
    if 'cagey_tier_decision' not in decisions:
        return pd.DataFrame(columns=tier_output_columns(rule))
    picks = _tier_rank(decisions.loc[decisions.cagey_tier_decision == 'SHORTLISTED'])
    columns = tier_output_columns(rule)
    result = picks.reindex(columns=list(dict.fromkeys([*columns, *picks.columns]))).reset_index(drop=True)
    if expanded:
        from shortlist_schema import harmonize
        result = harmonize(result, 'cagey')
    return result


def build_shortlist(predictions: pd.DataFrame, as_of, market_reliability=None, execution_policy=None, *,
                    settings: Optional[Mapping] = None, model: Optional[Mapping] = None,
                    monitor: Optional[list] = None):
    """Value tier and cagey tier. Returns (shortlist, decisions, summary); the tier is in `decisions`.

    `settings` defaults to cagey_correction_config.json; replays pass the run's recorded settings.
    `monitor`, when a list, receives one correction-monitoring record per fixture (evidence only).
    """
    settings = {**DEFAULT_SETTINGS, 'price_edge_execution_version': EXECUTION_VERSION,
                **(settings if settings is not None else load_settings())}
    execution_version = settings['price_edge_execution_version']
    if type(execution_version) is not int or execution_version not in (1, EXECUTION_VERSION):
        raise ValueError('Unknown v28 price-edge execution version')
    from quote_policy import load_policy, validate_policy
    policy = load_policy() if execution_policy is None else validate_policy(dict(execution_policy))
    cost = policy['per_stake_cost_bps'] / 10000 if execution_version == EXECUTION_VERSION else 0.0
    switched_on = settings['cagey_correction_enabled'] or settings['cagey_tier_enabled']
    per_market = value_rule(settings) in (VALUE_RULE_PER_MARKET, *PROFIT_RULES)
    group = dict(group_column='value_market_group') if per_market else {}
    groups = VALUE_GROUP_COLUMNS if per_market else []
    if not switched_on:
        uses_transform = execution_version == EXECUTION_VERSION or per_market or timing_rule(settings) != TIMING_RULE_SKEW
        selected, decisions, summary = v27.build_shortlist(
            predictions, as_of, market_reliability, policy,
            transform=make_transform(None, settings, cost=cost, policy=policy) if uses_transform else None,
            extra_columns=[*VALUE_COLUMNS, *TIER_COLUMNS, *groups,
                           *(EXECUTION_COLUMNS if execution_version == EXECUTION_VERSION else [])]
            if uses_transform else (), cutoff=timing_rule(settings) == TIMING_RULE_CUTOFF, **group)
    else:
        model = model or (nm.load(settings['model_version']) if settings.get('model_version') else nm.production_model())
        selected, decisions, summary = v27.build_shortlist(
            predictions, as_of, market_reliability, policy,
            transform=make_transform(model, settings, monitor, cost, policy=policy),
            extra_columns=[*VALUE_COLUMNS, *tier_columns(tier_rule(settings)), *groups,
                           *(EXECUTION_COLUMNS if execution_version == EXECUTION_VERSION else [])],
            cutoff=timing_rule(settings) == TIMING_RULE_CUTOFF, **group)
    if value_rule(settings) in PROFIT_RULES:
        from profit_shortlist import COLUMNS as PROFIT_COLUMNS, annotate, select
        from performance_tracking import fixture_key
        roster = {fixture_key(r): r for r in predictions.astype(object).where(predictions.notna(), None).to_dict('records')}
        records = [annotate(roster[fixture_key(item)], item, pd.Timestamp(summary['generated_at_utc']), cost, rule=value_rule(settings))
                   for item in decisions.to_dict('records')]
        decisions = pd.DataFrame(records, columns=list(dict.fromkeys([*decisions.columns, *PROFIT_COLUMNS])))
        selected, decisions = select(decisions)
    for frame in (selected, decisions):
        if 'selection_policy_version' in frame:
            frame['selection_policy_version'] = POLICY
    tier = {'enabled': False, 'n_shortlisted': 0}
    if settings['cagey_tier_enabled']:
        tier = apply_cagey_tier(decisions, selected, pd.Timestamp(summary['generated_at_utc']), model,
                                tier_rule(settings))
    only = selected.get('qualified_only_by_correction', pd.Series(dtype=bool)).fillna(False).astype(bool)
    if settings['cagey_tier_enabled'] and tier_rule(settings) != TIER_RULE_VALUE:
        # Recorded so replays reproduce it; value-v1 runs record nothing, exactly as before.
        summary['cagey_tier_rule'] = tier_rule(settings)
    if per_market:
        # Recorded so replays reproduce it; one-per-fixture-v1 runs record nothing, exactly as before.
        counts = selected['value_market_group'].value_counts() if len(selected) else pd.Series(dtype=int)
        summary.update(
            value_rule=VALUE_RULE_PER_MARKET,
            eligible_markets=[*summary['eligible_markets'], OVER_1_5],
            value_market_groups=list(MARKET_GROUPS),
            min_edge=GROUP_MIN_EDGE, min_edge_derived=GROUP_MIN_EDGE,
            min_edge_by_market_group={GROUP_AH: f'{GROUP_MIN_EDGE:.0%} vs Pinnacle (a/b) or the market-implied fit (c/c-cagey)',
                                      GROUP_WIN: f'{GROUP_MIN_EDGE:.0%} vs Pinnacle 1X2 or AH -0.5 (a/b)',
                                      GROUP_DC: f'{GROUP_MIN_EDGE:.0%} vs Pinnacle 1X2 or AH +0.5 (a/b)',
                                      GROUP_OVER_1_5: f'{GROUP_MIN_EDGE:.0%} vs Pinnacle O/U 1.5 (a); no Pinnacle quote, no pick'},
            value_market_group_counts={k: int(counts.get(k, 0)) for k in MARKET_GROUPS},
            selection_method='Per fixture and market group (asian_handicap, match_winner, double_chance, over_1_5): '
                             'qualifying candidate with the highest Pinnacle no-loss probability, then edge, then odds; '
                             'shortlist sorted safest first; no cap')
    summary.update(selection_policy_version=POLICY, cagey_correction_enabled=bool(settings['cagey_correction_enabled']),
                   cagey_tier_enabled=bool(settings['cagey_tier_enabled']),
                   cagey_model_version=model['version'] if switched_on else None, reference_order=REFERENCES,
                   correction_only_value_picks=int(only.sum()), cagey_tier=tier,
                   reference_type_counts={k: int(v) for k, v in selected.reference_type.value_counts().items()}
                   if len(selected) else {},
                   correction_rule='Derived plus lines (>= +1.0) are priced from the cagey-corrected matrix (c-cagey, '
                                   '3% threshold); Pinnacle-quoted lines keep Pinnacle as the fair price; minus lines '
                                   'are never corrected.')
    if execution_version == EXECUTION_VERSION:
        summary['price_edge_execution_version'] = EXECUTION_VERSION
    if timing_rule(settings) != TIMING_RULE_SKEW:
        # Recorded so replays reproduce it; skew-5min-v1 runs record nothing, exactly as before.
        summary['quote_timing_rule'] = timing_rule(settings)
    if value_rule(settings) in PROFIT_RULES:
        from profit_shortlist import BASIS
        rejected = decisions.loc[decisions.decision.eq('REJECTED'), 'rejection_reasons']
        reasons = pd.Series([r for text in rejected for r in str(text).split('; ') if r]).value_counts()
        summary.update(value_rule=value_rule(settings), selection_objective='TEAM_RESEARCH_PROFIT_PROBABILITY',
            probability_basis=BASIS, min_edge=None, min_edge_derived=None,
            min_edge_by_market_group={}, n_shortlisted=len(selected), n_strict_qualified=len(selected),
            n_total_candidates=len(selected), n_markets_evaluated=len(decisions),
            status='QUALIFIED' if len(selected) else 'NO BET',
            ev_required_for_selection=False, ranking_metric='probability of positive net return descending',
            selection_method='Highest positive-return probability per fixture and market group; expected return then odds break ties; no cap',
            value_market_group_counts={k: int(selected.value_market_group.eq(k).sum()) for k in MARKET_GROUPS},
            rejection_counts={str(k): int(v) for k, v in reasons.items()},
            research_missing_policy='eligible with visible coverage warnings',
            research_rule='ten recent games weighted newest first; venue splits; verified xG if supplied; Poisson goal rates; context evidence shown separately')
    if value_rule(settings) == VALUE_RULE_LOCAL_RESEARCH:
        summary.update(min_offered_odds_exclusive=1.15, max_offered_odds=2.0,
            eligible_markets=[*summary['eligible_markets'], 'Double Chance 12'],
            asian_handicap_selection='Highest positive-net-return probability among available quoted AH lines within (1.15, 2.00]; one per fixture/group',
            training_rule='Verified local competition history plus pre-cutoff free-source research; refresh failure retains valid cache with a warning',
            model_role='Researched settlement probabilities select and rank the main shortlist',
            warning='Research probabilities are model estimates and have not passed a forward calibration gate. Negative expected return remains eligible and flagged.')
    if settings['cagey_tier_enabled'] and tier_rule(settings) in EXPANDED_RULES:
        from shortlist_schema import harmonize
        selected = harmonize(selected, 'value')
        summary['shortlist_schema_version'] = 'comparable-shortlist-v1'
    return selected, decisions, summary
