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
TIER_RULES = (TIER_RULE_VALUE, TIER_RULE_NARROW)
DEFAULT_SETTINGS = {'cagey_correction_enabled': True, 'cagey_tier_enabled': True, 'cagey_tier_rule': TIER_RULE_VALUE}
CONFIG = Path(__file__).with_name('cagey_correction_config.json')
SWITCHES = ('cagey_correction_enabled', 'cagey_tier_enabled')
# Everything a replay needs from a run's summary to reproduce its selection.
REPLAY_SETTINGS = (*SWITCHES, 'cagey_tier_rule')


def tier_rule(settings: Mapping) -> str:
    rule = settings.get('cagey_tier_rule') or TIER_RULE_VALUE
    if rule not in TIER_RULES:
        raise ValueError(f'Unknown cagey_tier_rule {rule!r}; expected one of {", ".join(TIER_RULES)}')
    return rule


def load_settings(path: Optional[Path] = None) -> Dict[str, object]:
    """Switches, tier rule and model version. A switch may be on only when the recorded holdout gate passed."""
    data = json.loads(Path(path or CONFIG).read_text(encoding='utf-8-sig'))
    if any(not isinstance(data.get(name), bool) for name in SWITCHES):
        raise ValueError('cagey_correction_enabled and cagey_tier_enabled must be true or false')
    if any(data[name] for name in SWITCHES) and nm.versions()['gate'].get('gate_result') != 'PASS':
        raise ValueError('The cagey correction may only be switched on after GATE: PASS')
    return {**{name: data[name] for name in (*SWITCHES, 'model_version')}, 'cagey_tier_rule': tier_rule(data)}
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
    return [*TIER_COLUMNS, *(NARROW_COLUMNS if rule == TIER_RULE_NARROW else [])]


def tier_output_columns(rule: str) -> List[str]:
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
            'probs': nm.correct_distribution(margins, probs, p2, p3), 'score': p2}


def corrected_price(context: Mapping, side: str, line: float, price=None) -> Dict[str, object]:
    priced = nm.price_distribution(context['margins'], context['probs'], side, line)
    expected = None
    if price is not None:
        expected = ((priced['p_win'] + priced['p_half_win'] / 2) * (price - 1)
                    - priced['p_loss'] - priced['p_half_loss'] / 2)
    uncorrected = (nm.price_distribution(context['margins'], context['uncorrected_probs'], side, line)['fair_odds']
                   if 'uncorrected_probs' in context else None)
    return {'corrected_fair_probability': priced['win_share'], 'corrected_fair_odds': priced['fair_odds'],
            'corrected_no_loss_probability': priced['p_no_loss'], 'corrected_expected_profit': expected,
            'corrected_p_win': priced['p_win'], 'corrected_p_half_win': priced['p_half_win'],
            'corrected_p_push': priced['p_push'], 'corrected_p_half_loss': priced['p_half_loss'],
            'corrected_p_loss': priced['p_loss'], 'corrected_p_profit': priced['p_win'] + priced['p_half_win'],
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
                                   item.get('offered_decimal_odds')))
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


def usable_quote(stamp, generated, kickoff) -> bool:
    """A bookmaker price counts as pre-match evidence only if its quote was fresh at generation
    (the selection freshness rule) and timestamped before kickoff."""
    from quote_freshness import quote_is_fresh, quote_utc
    when, kick = quote_utc(stamp), quote_utc(kickoff)
    return when is not None and kick is not None and when < kick and quote_is_fresh(stamp, generated)
MONITOR_COLUMNS = ['monitoring_version', 'generated_at_utc', 'league', 'home_team', 'away_team', 'fixture_id',
                   'kickoff_utc', 'model_version', 'quintile_model_sha256', 'status', 'exclusion_reason', 'fit',
                   'latest_input_quote_utc', 'corrected_p2', 'corrected_p3', 'uncorrected_p2', 'uncorrected_p3',
                   'corrected_cagey_quintile', *MONITOR_PRICE_COLUMNS]


def monitoring_record(row: Mapping, items: List[Mapping], fit: mi.Fit, fit_info: Mapping, now: pd.Timestamp,
                      context: Optional[Mapping], model: Mapping, quintiles: Mapping) -> Dict[str, object]:
    """One fixture's pre-match evidence, from the distribution and correction this run already computed."""
    from quote_freshness import quote_utc
    stamps = [t for t in (quote_utc(s) for s in fit_info['stamps']) if t is not None]
    record = {c: None for c in MONITOR_COLUMNS}
    record.update({k: row.get(k) for k in ('league', 'home_team', 'away_team', 'fixture_id', 'kickoff_utc')},
                  monitoring_version=MONITOR_VERSION, generated_at_utc=now.isoformat(), model_version=model['version'],
                  quintile_model_sha256=quintiles['model_sha256'],
                  latest_input_quote_utc=max(stamps).isoformat() if stamps else None)
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
                and usable_quote(stamp, now, row.get('kickoff_utc'))):
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


def make_transform(model: Mapping, settings: Mapping, monitor: Optional[list] = None):
    quintiles = nm.load_quintiles(model) if monitor is not None else None

    def transform(row, items, pin, fit, fit_info, now) -> List[Dict[str, object]]:
        context = corrected_context(pin, fit, fit_info, model)
        if monitor is not None:
            monitor.append(monitoring_record(row, items, fit, fit_info, now, context, model, quintiles))
        tier = tier_rule(settings) if settings['cagey_tier_enabled'] else False
        return [value_tier_item(item, context, settings['cagey_correction_enabled'], tier) for item in items]
    return transform


def _tier_rank(frame: pd.DataFrame) -> pd.DataFrame:
    """Safest first: corrected no-loss probability, then expected profit, then odds."""
    return frame.sort_values(['corrected_no_loss_probability', 'corrected_expected_profit', 'offered_decimal_odds',
                              'kickoff_utc', 'market', 'bookmaker'],
                             ascending=[False, False, False, True, True, True], kind='stable')


def apply_cagey_tier(decisions: pd.DataFrame, selected: pd.DataFrame, now: pd.Timestamp,
                     model: Mapping, rule: str = TIER_RULE_VALUE) -> Dict[str, object]:
    """Run-level cutoff and one-per-fixture selection for the cagey tier (updates `decisions`)."""
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
                    'guards; price_flag says whether expected profit under the corrected matrix is >= 0 (value) or '
                    'not (below fair); one per fixture',
            'rule_version': TIER_RULE_NARROW}


def cagey_tier_list(decisions: pd.DataFrame) -> pd.DataFrame:
    """The cagey-tier shortlist (separate from the value tier), safest first."""
    rule = TIER_RULE_NARROW if 'price_flag' in decisions else TIER_RULE_VALUE
    if 'cagey_tier_decision' not in decisions:
        return pd.DataFrame(columns=tier_output_columns(rule))
    picks = _tier_rank(decisions.loc[decisions.cagey_tier_decision == 'SHORTLISTED'])
    columns = tier_output_columns(rule)
    return picks.reindex(columns=list(dict.fromkeys([*columns, *picks.columns]))).reset_index(drop=True)


def build_shortlist(predictions: pd.DataFrame, as_of, market_reliability=None, execution_policy=None, *,
                    settings: Optional[Mapping] = None, model: Optional[Mapping] = None,
                    monitor: Optional[list] = None):
    """Value tier and cagey tier. Returns (shortlist, decisions, summary); the tier is in `decisions`.

    `settings` defaults to cagey_correction_config.json; replays pass the run's recorded settings.
    `monitor`, when a list, receives one correction-monitoring record per fixture (evidence only).
    """
    settings = {**DEFAULT_SETTINGS, **(settings if settings is not None else load_settings())}
    switched_on = settings['cagey_correction_enabled'] or settings['cagey_tier_enabled']
    if not switched_on:
        selected, decisions, summary = v27.build_shortlist(predictions, as_of, market_reliability, execution_policy)
    else:
        model = model or (nm.load(settings['model_version']) if settings.get('model_version') else nm.production_model())
        selected, decisions, summary = v27.build_shortlist(
            predictions, as_of, market_reliability, execution_policy,
            transform=make_transform(model, settings, monitor),
            extra_columns=[*VALUE_COLUMNS, *tier_columns(tier_rule(settings))])
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
    summary.update(selection_policy_version=POLICY, cagey_correction_enabled=bool(settings['cagey_correction_enabled']),
                   cagey_tier_enabled=bool(settings['cagey_tier_enabled']),
                   cagey_model_version=model['version'] if switched_on else None, reference_order=REFERENCES,
                   correction_only_value_picks=int(only.sum()), cagey_tier=tier,
                   reference_type_counts={k: int(v) for k, v in selected.reference_type.value_counts().items()}
                   if len(selected) else {},
                   correction_rule='Derived plus lines (>= +1.0) are priced from the cagey-corrected matrix (c-cagey, '
                                   '3% threshold); Pinnacle-quoted lines keep Pinnacle as the fair price; minus lines '
                                   'are never corrected.')
    return selected, decisions, summary
