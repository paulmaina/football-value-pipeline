"""The new master shortlist, in shadow (Phase 4, fill rule, rule master-new-fill-rule-v4).

Scores both views on every offer either list nominates, at its exact Pinnacle line and price: the research
probability (p_r) and the cagey tier's corrected probability (p_c) that the bet does not lose; g = p_r - p_c in
percentage points. A bet is on the list only if the cagey tier rates it safe (no-loss >= 0.75; Pinnacle's
margin-free no-loss where the cagey score is missing), and the list is ranked by that chance alone. The research
view never removes or reorders a bet: it only labels rows ("both agree", "research too optimistic") and flags
the ones it strongly disputes ("research strongly disagrees", g <= -8 with cagey >= 0.85) for inspection.
Decided by Paul on 13 Nov 2026, replacing the 4-point rule (master-new-paul-rule-v1, frozen in master_rule_v1.py
for the offline comparison) on the backtest evidence of PR #171.

Fill rule (decided by Paul, 13 Nov 2026; pools decided by Paul, 14 Nov 2026; rule master-new-fill-rule-v4): those
safe picks are step 1. If fewer than 15 matches have one, step 2 fills the remaining slots, one per match, with each
match's best nominated executable Pinnacle offer that is not risky (market no-loss >= 0.50), ranked by the market
chance of profit (P(win) + P(half win)); only if still short, step 3 adds each remaining match's best nominated offer
by the same chance, labelled "risky fill". Every step draws only from the two lists' nominations, so when they cover
fewer than 15 matches the list is shorter (recorded in the summary). Every pick carries its tier (safe, fill, risky
fill). The cagey probabilities used are the current ones: the sharpening (cagey_sharpen.py) failed its pass rule and
stays off (config cagey_sharpening.use_sharpened).

Quote timing (config `timing`): before any tier is assigned, the offer and the reference that supplies its ranking
probabilities (the cagey tier's corrected distribution, or the Pinnacle stand-in) must pass exactly the live master's
timing checks (master_selection: the run's single generation clock, `_fresh` with MAX_AGE_MINUTES = 15, which also
rejects any stamp after evaluation, and the 10-minute input synchronisation). The reference's stamps come from the
run's own forecast, as the live master reads them. An offer or reference that fails is ineligible (NOT_EXECUTABLE),
with its reason in `timing_check`, counted in the summary.

Writes master_shortlist_new.csv beside the live master_shortlist.csv. Shadow only: the live master file, every
probability, every pick and every stake are untouched; this module only reads the run's decision rows and the
live master frame.

Definitions live in master_reconciliation_config.json (and docs/plan.md, Phase 4). The same `classify` and
`select` serve the live shadow and the offline backtest (evaluation_harness.py --mode master), so the two
can't drift apart.
"""
from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
from typing import Dict, List, Mapping, Optional, Sequence

import numpy as np
import pandas as pd

from master_selection import MAX_AGE_MINUTES

CONFIG = Path(__file__).with_name('master_reconciliation_config.json')
VERSION = 'master-new-fill-rule-v4'
KINDS = ('win', 'half_win', 'push', 'half_loss', 'loss')
GROUPS = ('included', 'left_out')
RANKED = ('included',)
GAP_CHECKS = ('agree', 'research_too_optimistic', 'research_more_pessimistic', 'no_research_check',
              'one_view_missing', 'no_view')
LEFT_OUT_REASONS = ('risky', 'in between (not safe)', 'one view missing: no Pinnacle reference', 'no view')
# Row labels, in the order they are written to `new_master_labels` (column name, label text).
LABELS = (('both_agree', 'both agree'), ('research_too_optimistic', 'research too optimistic'),
          ('inspection_flag', 'research strongly disagrees'), ('one_view_missing', 'one view missing'),
          ('no_research_check', 'no research check'), ('unvalidated_view', 'unvalidated view'),
          ('risky_fill', 'risky fill'))
TIERS = ('safe', 'fill', 'risky fill')  # the picks of step 1, step 2 and step 3
DECISIONS = ('SHORTLISTED', 'BEYOND_TARGET', 'NOT_SELECTED', 'LEFT_OUT', 'NOT_EXECUTABLE')
TOLERANCE = 1e-9
IDENTITY_COLUMNS = ['kickoff_utc', 'league', 'home_team', 'away_team', 'fixture_id', 'market', 'market_to_bet',
                    'handicap_side', 'handicap_line', 'bookmaker', 'offered_decimal_odds', 'offered_last_update_utc',
                    'source_market', 'per_stake_cost', 'fair_odds', 'reference_type', 'evaluated_at_utc',
                    'selection_policy_version', 'in_value_shortlist', 'in_cagey_tier']
CLASSIFICATION_COLUMNS = [
    'research_no_loss_probability', 'cagey_no_loss_probability', 'gap_points', 'gap_check',
    'pinnacle_no_loss_probability', 'pinnacle_fair_odds',
    'research_expected_return', 'research_edge', 'cagey_expected_return', 'cagey_fair_odds',
    'line_type', 'cagey_profit_probability', 'cagey_sharpened_no_loss_probability',
    'cagey_sharpened_profit_probability', 'pinnacle_profit_probability', 'probability_source',
    'market_basis', 'market_safety', 'market_price', 'ranking_no_loss_probability', 'ranking_profit_probability',
    'new_master_labels',
    *[column for column, _ in LABELS], 'missing_view', 'missing_evidence_reason', 'new_master_group',
    'left_out_reason']
# Quote timing reasons (the live master's wording, master_selection.evaluate / _reference, where it has one).
TIMING_REASONS = ('missing, mixed or outdated evaluation generation',
                  'offered quote missing, future or older than fifteen minutes',
                  'unique same-generation fixture forecast unavailable',
                  'reference inputs missing, future or older than fifteen minutes',
                  'reference inputs and offer more than 10 minutes apart')
SYNC_SECONDS = 600  # master_selection._reference: Pinnacle inputs and the offer at most 10 minutes apart
COLUMNS = ['new_master_rank', 'new_master_tier', 'new_master_step', 'new_master_group', 'new_master_decision',
           'new_master_reason', 'timing_check', *IDENTITY_COLUMNS,
           *[c for c in CLASSIFICATION_COLUMNS if c != 'new_master_group'],
           'in_live_master', 'live_master_rank', 'live_master_same_offer', 'new_master_version']


def load_config(path: Optional[Path] = None) -> Dict[str, object]:
    config = json.loads(Path(path or CONFIG).read_text(encoding='utf-8'))
    if config.get('version') != VERSION:
        raise ValueError('Unknown master rule version')
    return config


def _number(value) -> Optional[float]:
    try:
        n = float(value)
    except (TypeError, ValueError):
        return None
    return n if math.isfinite(n) else None


def settlement_mass(values: Sequence) -> Optional[np.ndarray]:
    """A valid five-way settlement distribution (win, half win, push, half loss, loss), or None."""
    numbers = [_number(v) for v in values]
    if len(numbers) != 5 or any(n is None for n in numbers):
        return None
    mass = np.array(numbers, float)
    if (mass < -1e-12).any() or (mass > 1 + 1e-12).any() or abs(mass.sum() - 1) > 1e-6:
        return None
    win = mass[0] + mass[1] / 2
    return mass if win > 0 else None


def no_loss(mass: np.ndarray) -> float:
    """P(the bet does not lose): win, half win or push (for bets with no push, P(win))."""
    return float(mass[0] + mass[1] + mass[2])


def scored(mass: np.ndarray, price: float, cost: float) -> Dict[str, float]:
    """Expected return after cost, profit and no-loss probabilities and fair odds of one view."""
    returns = np.array([price - 1, (price - 1) / 2, 0., -.5, -1.]) - cost
    win, loss = mass[0] + mass[1] / 2, mass[4] + mass[3] / 2
    return {'expected_return': float(mass @ returns), 'profit': float(mass[returns > 1e-12].sum()),
            'no_loss': no_loss(mass), 'fair_odds': float(1 + loss / win)}


def _probability(value) -> Optional[float]:
    n = _number(value)
    return n if n is not None and 0 <= n <= 1 else None


def profit_chance(mass: np.ndarray) -> float:
    """Chance of profit: P(the bet returns more than the stake) = P(win) + P(half win) on this exact line. A push
    returns the stake, a half win stake + (odds - 1) / 2, a half loss half the stake (config chance_of_profit)."""
    return float(mass[0] + mass[1])


def classify(research: Optional[np.ndarray], cagey: Optional[np.ndarray], price: float, cost: float,
             pinnacle_no_loss: Optional[float] = None, pinnacle_fair_odds: Optional[float] = None, *,
             european: bool, config: Mapping, research_reason: Optional[str] = None,
             cagey_reason: Optional[str] = None, pinnacle_profit: Optional[float] = None,
             cagey_sharpened: Optional[Sequence[float]] = None, use_sharpened: Optional[bool] = None,
             line_kind: Optional[str] = None) -> Dict[str, object]:
    """Both views on one offer, its step-1 inclusion, its market view for the fill and its labels, exactly as
    master_reconciliation_config.json says.

    `research` / `cagey` are the views' settlement distributions on this exact line, or None when that view
    can't score the offer (`*_reason` says why). `pinnacle_no_loss` / `pinnacle_fair_odds` / `pinnacle_profit` are
    Pinnacle's margin-free no-loss probability, fair odds and chance of profit for the same bet (the market view
    when the cagey score is missing; never sharpened). `cagey_sharpened` is the sharpened cagey (no-loss, chance of
    profit), used for the thresholds, the ranking and the chance of profit only when `use_sharpened` (default: the
    config's cagey_sharpening.use_sharpened). Labels and flags always read the current cagey probabilities, as in
    #172. Inclusion and fill read the market view only; the research view only labels and flags.
    """
    gap, view, edge_rule = config['gap'], config['market_view'], config['research_edge']
    flag, include = config['inspection_flag'], config['inclusion']
    if use_sharpened is None:
        use_sharpened = bool(config['cagey_sharpening']['use_sharpened'])
    out: Dict[str, object] = dict.fromkeys(CLASSIFICATION_COLUMNS)
    out.update({column: False for column, _ in LABELS})
    out['unvalidated_view'] = bool(european)
    out['line_type'] = line_kind
    pin, pin_profit = _probability(pinnacle_no_loss), _probability(pinnacle_profit)
    pin_fair = _number(pinnacle_fair_odds)
    pin_fair = pin_fair if pin_fair is not None and pin_fair > 1 else None
    out.update(pinnacle_no_loss_probability=pin, pinnacle_fair_odds=pin_fair, pinnacle_profit_probability=pin_profit)
    r = scored(research, price, cost) if research is not None else None
    c = scored(cagey, price, cost) if cagey is not None else None
    sharp = None
    if c is not None and cagey_sharpened is not None:
        sharp = tuple(_probability(v) for v in cagey_sharpened)
        sharp = sharp if len(sharp) == 2 and None not in sharp else None
    if r is not None:
        out.update(research_no_loss_probability=r['no_loss'], research_expected_return=r['expected_return'],
                   research_edge=bool(r['expected_return'] > edge_rule['min_expected_return_exclusive']))
    if c is not None:
        out.update(cagey_no_loss_probability=c['no_loss'], cagey_expected_return=c['expected_return'],
                   cagey_fair_odds=c['fair_odds'], cagey_profit_probability=profit_chance(cagey))
    if sharp is not None:
        out.update(cagey_sharpened_no_loss_probability=sharp[0], cagey_sharpened_profit_probability=sharp[1])
    reasons = []
    if r is None:
        reasons.append('research: ' + (research_reason or 'settlement probabilities unavailable'))
    if c is None:
        reasons.append('cagey: ' + (cagey_reason or 'settlement probabilities unavailable'))
    if reasons:
        out['missing_evidence_reason'] = '; '.join(reasons)

    def finish(group, reason=None):
        out.update(new_master_group=group, left_out_reason=reason,
                   new_master_labels='; '.join(text for column, text in LABELS if out[column]) or None)
        return out

    if r is None and c is None:
        out.update(missing_view='both', gap_check='no_view')
        return finish('left_out', 'no view')
    # The market view: the cagey tier's figures (sharpened only if the pass rule passed), or Pinnacle's margin-free
    # ones when the cagey score is missing (never sharpened).
    if c is not None and use_sharpened and sharp is not None:
        basis, source, (chance, chance_profit) = 'cagey', 'cagey sharpened', sharp
    elif c is not None:
        basis, source, chance, chance_profit = 'cagey', 'cagey', c['no_loss'], profit_chance(cagey)
    else:
        basis, source, chance, chance_profit = 'pinnacle', 'pinnacle stand-in', pin, pin_profit
    fair_odds = c['fair_odds'] if c is not None else pin_fair
    safe = risky = fair = False
    if chance is not None:
        safe = chance + TOLERANCE >= include['min_cagey_no_loss']
        risky = chance < view['risky']['max_no_loss_exclusive']
        fair = fair_odds is not None and \
            price * (1 + view['fair']['pinnacle_average_margin']) + TOLERANCE >= fair_odds
        out.update(market_basis=basis, probability_source=source, ranking_no_loss_probability=chance,
                   ranking_profit_probability=chance_profit,
                   market_safety='safe' if safe else 'risky' if risky else 'middle',
                   market_price='fair' if fair else 'below fair')
    # Labels read the current cagey no-loss chance exactly as #172 (the same as `safe` unless sharpened is used).
    label_safe = c is not None and c['no_loss'] + TOLERANCE >= include['min_cagey_no_loss']
    if r is not None and c is not None:
        g = 100 * (r['no_loss'] - c['no_loss'])
        out['gap_points'] = g
        optimistic = g + TOLERANCE >= gap['research_too_optimistic_min_points']
        out['gap_check'] = ('research_too_optimistic' if optimistic else 'research_more_pessimistic'
                            if g - TOLERANCE <= gap['report_more_pessimistic_max_points'] else 'agree')
        out['research_too_optimistic'] = optimistic
        out['both_agree'] = bool(out['gap_check'] == 'agree' and out['research_edge'] and (label_safe or fair)
                                 and not european)
        out['inspection_flag'] = bool(g - TOLERANCE <= flag['max_gap_points']
                                      and c['no_loss'] + TOLERANCE >= flag['min_cagey_no_loss'])
    elif c is not None:
        out.update(missing_view='research', gap_check='no_research_check', no_research_check=True)
    else:
        out.update(missing_view='cagey', gap_check='one_view_missing', one_view_missing=True)
        if pin is None:
            return finish('left_out', 'one view missing: no Pinnacle reference')
    if safe:
        return finish('included')
    return finish('left_out', 'risky' if risky else 'in between (not safe)')


def _tie_key(row: Mapping) -> tuple:
    chance = _number(row.get('ranking_no_loss_probability'))
    odds = _number(row.get('offered_decimal_odds'))
    # Rounded so that equal chances computed by different paths (e.g. AH +0.25 and 1X) tie and go to the odds.
    return (-round(chance, 9) if chance is not None else math.inf, -odds if odds is not None else math.inf,
            str(row.get('kickoff_utc') or ''), str(row.get('league') or ''), str(row.get('home_team') or ''),
            str(row.get('away_team') or ''), str(row.get('market') or ''), str(row.get('handicap_side') or ''),
            _number(row.get('handicap_line')) or 0.)


def _fill_key(row: Mapping) -> tuple:
    """Steps 2-3: chance of profit (9 decimals), then higher odds, kickoff, league, teams, market, side, line."""
    chance = _number(row.get('ranking_profit_probability'))
    return (-round(chance, 9) if chance is not None else math.inf, *_tie_key(row)[1:])


def _best_per_match(rows, match_key, key, eligible) -> Dict[object, Dict[str, object]]:
    best: Dict[object, Dict[str, object]] = {}
    for row in rows:
        if not eligible(row):
            continue
        current = best.get(row[match_key])
        if current is None or key(row) < key(current):
            best[row[match_key]] = row
    return best


def select(rows: List[Dict[str, object]], target: int, match_key: str = '_match', prefix: str = 'new_master',
           fill: bool = True, fill_min_no_loss: float = 0.5) -> List[Dict[str, object]]:
    """The fill rule (config `fill`), one pick per match, at most `target` matches; labels and flags never read.

    Every step draws only from nominated rows (`<prefix>_nominated`, default True; rule v4). Step 1 (#172): among
    rows in group 'included' (safe), each match's offer with the highest no-loss chance; ranked by that chance alone.
    Only if fewer than `target` matches got one (and `fill`): step 2, among the executable rows of the matches without
    a step-1 pick, each match's not-risky
    offer (ranking no-loss >= `fill_min_no_loss`) with the highest chance of profit, ranked by that chance; then,
    only if still short, step 3, each remaining match's offer with the highest chance of profit (risky fill). Rows
    with `<prefix>_executable` False are never picked. With `fill` False this is exactly #172's selection.

    Mutates and returns `rows`, adding <prefix>_rank, _tier, _step (the step a row is its match's candidate in),
    _decision and _reason; step-3 picks get risky_fill True and the 'risky fill' label."""
    group, rank, decision, reason, tier, step = (f'{prefix}_{k}' for k in
                                                 ('group', 'rank', 'decision', 'reason', 'tier', 'step'))
    executable = lambda r: r.get(f'{prefix}_executable', True) is not False
    nominated = lambda r: r.get(f'{prefix}_nominated', True) is not False
    for row in rows:
        row.update({rank: None, tier: None, step: None})
    first = _best_per_match(rows, match_key, _tie_key, lambda r: executable(r) and nominated(r) and r[group] in RANKED)
    steps = [(1, sorted(first.values(), key=_tie_key))]
    if fill:
        taken = set(first)
        has_view = lambda r: (executable(r) and nominated(r) and r[match_key] not in taken
                              and _number(r.get('ranking_no_loss_probability')) is not None
                              and _number(r.get('ranking_profit_probability')) is not None)
        second = _best_per_match(rows, match_key, _fill_key, lambda r: has_view(r) and _number(
            r.get('ranking_no_loss_probability')) + TOLERANCE >= fill_min_no_loss)
        taken |= set(second)
        third = _best_per_match(rows, match_key, _fill_key, has_view)
        steps += [(2, sorted(second.values(), key=_fill_key)), (3, sorted(third.values(), key=_fill_key))]
    names = {1: 'safe', 2: 'fill', 3: 'risky fill'}
    chosen, position = set(), 0
    for number, candidates in steps:  # a later step runs only if the earlier ones left the list short
        for row in candidates:
            chosen.add(id(row))
            row[step] = number
            if position < target:
                position += 1
                row.update({rank: position, tier: names[number], decision: 'SHORTLISTED', reason: ''})
                if number == 3:
                    row['risky_fill'] = True
                    row['new_master_labels'] = '; '.join(t for t in (row.get('new_master_labels'), 'risky fill') if t)
            else:
                row.update({decision: 'BEYOND_TARGET', reason: f'beyond the {target}-match target' if number == 1
                            else f'step {number} candidate ({names[number]}) beyond the {target}-match target'})
    for row in rows:
        if id(row) in chosen:
            continue
        if not executable(row):
            row.update({decision: 'NOT_EXECUTABLE', reason: row.get(reason) or 'not executable'})
        elif not nominated(row):  # never picked (rule v4: every step uses the nominations only)
            row.update({decision: 'NOT_SELECTED', reason: 'not nominated by either list'})
        elif row[group] in RANKED:
            row.update({decision: 'NOT_SELECTED', reason: 'another offer chosen for this match'})
        else:
            row.update({decision: 'LEFT_OUT', reason: row.get('left_out_reason') or 'left out by rule'})
    return rows


# ---------------------------------------------------------------------------
# Live shadow: a pure function of one run's decision rows (and, for overlap only, its live master list)
# ---------------------------------------------------------------------------

def _records(decisions: pd.DataFrame) -> List[Dict[str, object]]:
    if decisions is None or decisions.empty:
        return []
    return decisions.astype(object).where(decisions.notna(), None).to_dict('records')


def nominated(record: Mapping) -> bool:
    return record.get('decision') == 'SHORTLISTED' or record.get('cagey_tier_decision') == 'SHORTLISTED'


def pool(decisions: pd.DataFrame) -> List[Dict[str, object]]:
    """Every offer either list nominated (shortlisted): the live master's starting union and, under rule v4, the
    only pool of every step (safe, fill, risky fill), in decision order."""
    return [r for r in _records(decisions) if nominated(r)]


def forecasts(predictions: Optional[pd.DataFrame]) -> Dict[object, Optional[Mapping]]:
    """The run's forecasts by fixture identity, as the live master reads them (master_selection.evaluate): an
    ambiguous fixture maps to None (fails closed)."""
    from master_selection import identity
    out: Dict[object, Optional[Mapping]] = {}
    if predictions is not None and len(predictions):
        for r in predictions.astype(object).where(predictions.notna(), None).to_dict('records'):
            key = identity(r)
            out[key] = r if key not in out else None
    return out


def run_clock(records: Sequence[Mapping], generated_at_utc=None):
    """The run's generation clock, as the live master takes it: the given clock, else the decision rows' single
    evaluation clock; None when it is missing or mixed."""
    from quote_freshness import quote_utc
    if generated_at_utc is not None:
        return quote_utc(generated_at_utc)
    clocks = {quote_utc(r.get('evaluated_at_utc')) for r in records}
    return next(iter(clocks)) if len(clocks) == 1 else None


def reference_stamps(row: Mapping, forecast: Mapping, clock, source: str, fits: Dict) -> List[object]:
    """The quote stamps behind the probabilities a row is ranked by, from the run's forecast, read exactly as the
    live master and the cagey tier read them (price_edge_shortlist.pinnacle_quotes, market_fit with the
    observed-by-cutoff rule).

    Cagey: the corrected distribution's inputs (price_edge_cagey_shortlist.corrected_context: fit B's 1X2, O/U 2.5 and
    main AH line; fit A's 1X2 and O/U 2.5 when fit B is unusable). Pinnacle stand-in: the live master's reference
    (master_selection._reference: the Pinnacle 1X2 quote for wins and double chance, fit B's inputs for other AH
    lines), plus fit B's inputs where its chance of profit comes from the uncorrected fit."""
    from cagey_market_basis import binary_market
    from master_selection import identity
    from price_edge_shortlist import market_fit, pinnacle_quotes
    pin = pinnacle_quotes(forecast)
    key = identity(row)
    if key not in fits:
        fits[key] = market_fit(pin, clock, cutoff=True)
    fit, info = fits[key]
    inputs = info.get('input_stamps') or {}
    if source.startswith('cagey'):
        return [stamp for name, stamp in inputs.items() if fit.usable or name != 'ah_main']
    binary = binary_market(row)
    if binary is None:
        return list(inputs.values())
    record = pin.get('ou15' if binary == 'Over 1.5' else 'h2h')
    stamps = [record[-1] if record else None]
    if settlement_mass([row.get('uncorrected_p_' + k) for k in KINDS]) is not None:
        stamps += list(inputs.values())
    return stamps


def timing(row: Mapping, clock, forecast: Optional[Mapping], source: Optional[str], fits: Dict) -> Optional[str]:
    """None when the offer and the reference supplying its ranking probabilities pass the live master's timing
    checks, else the reason (TIMING_REASONS). `source` is the row's probability_source (None: no market view, so
    no reference to check)."""
    from master_selection import _fresh
    from quote_freshness import quote_utc
    if clock is None or quote_utc(row.get('evaluated_at_utc')) != clock:
        return TIMING_REASONS[0]
    if not _fresh(row.get('offered_last_update_utc'), clock):
        return TIMING_REASONS[1]
    if source is None:
        return None
    if forecast is None:
        return TIMING_REASONS[2]
    stamps = reference_stamps(row, forecast, clock, source, fits)
    if not stamps or not all(_fresh(stamp, clock) for stamp in stamps):
        return TIMING_REASONS[3]
    times = [quote_utc(stamp) for stamp in stamps] + [quote_utc(row.get('offered_last_update_utc'))]
    if (max(times) - min(times)).total_seconds() > SYNC_SECONDS:
        return TIMING_REASONS[4]
    return None


def executable(row: Mapping, config: Mapping) -> Optional[str]:
    """None when the offer meets the live master's execution rule, else the reason."""
    from master_selection_pinnacle_markets import allowed
    rule = config['execution']
    price = _number(row.get('offered_decimal_odds'))
    if row.get('bookmaker') != rule['bookmaker']:
        return 'bookmaker other than Pinnacle'
    if price is None or not rule['min_odds_exclusive'] < price <= rule['max_odds_inclusive']:
        return 'offered odds outside (1.15, 2.00]'
    if not allowed({**row, 'master_offer_source_market': row.get('source_market')}):
        return 'market outside the native Pinnacle master markets'
    return None


def research_view(row: Mapping):
    mass = settlement_mass([row.get('research_p_' + k) for k in KINDS])
    if mass is None:
        return None, 'research settlement probabilities unavailable (team or goal rates unknown to the research model)'
    return mass, None


def cagey_view(row: Mapping):
    mass = settlement_mass([row.get('cagey_p_' + k) for k in KINDS])
    if mass is None:
        return None, 'cagey settlement probabilities unavailable'
    if row.get('cagey_input_timing_status') != 'SYNCHRONIZED':
        return None, 'cagey Pinnacle inputs unavailable, stale or unsynchronized with the offer'
    return mass, None


def pinnacle_reference(row: Mapping):
    """Pinnacle's margin-free no-loss probability on this bet (pinnacle_no_loss_probability: the uncorrected
    Pinnacle fit, on half lines the margin-free win share) and its margin-free fair odds where the fair reference
    is Pinnacle's own price (reference types a and b); None where unavailable."""
    chance = _number(row.get('pinnacle_no_loss_probability'))
    fair = _number(row.get('fair_odds'))
    return chance, (fair if row.get('reference_type') in ('a', 'b') and fair is not None and fair > 1 else None)


def pinnacle_profit(row: Mapping, line_kind: Optional[str]) -> Optional[float]:
    """Pinnacle's margin-free chance of profit on this bet (config chance_of_profit.pinnacle_stand_in): P(win) +
    P(half win) of the uncorrected Pinnacle fit (uncorrected_p_*, the fit behind pinnacle_no_loss_probability); where
    that settlement is unavailable, pinnacle_no_loss_probability on lines that can't push (half and quarter lines,
    wins, double chance); None on a whole line without it."""
    mass = settlement_mass([row.get('uncorrected_p_' + k) for k in KINDS])
    if mass is not None:
        return profit_chance(mass)
    if line_kind in ('half', 'quarter'):
        return _probability(row.get('pinnacle_no_loss_probability'))
    return None


def reconcile(decisions: pd.DataFrame, live_master: Optional[pd.DataFrame] = None,
              config: Optional[Mapping] = None, predictions: Optional[pd.DataFrame] = None,
              generated_at_utc=None) -> pd.DataFrame:
    """The new master of one run: every nominated offer with both views, its timing check, gap check, group, tier
    and decision.

    Reads the run's decision rows and, for the quote timing of each row's reference, the run's forecasts
    (`predictions`; without them no reference can be timed, so no row with a market view is eligible) at the run's
    generation clock (`generated_at_utc`, else the rows' single evaluation clock). `live_master` (the run's
    master_shortlist.csv frame) is used for the overlap columns only and never changes a group, a rank or a decision.
    """
    from master_selection import identity
    from cagey_sharpen import offer_line_type
    from performance_tracking import fixture_key
    config = config or load_config()
    european = set(config['european']['leagues'])
    records = pool(decisions)
    clock = run_clock(_records(decisions), generated_at_utc)
    by_fixture, fits = forecasts(predictions), {}
    rows = []
    for record in records:
        price = _number(record.get('offered_decimal_odds'))
        cost = _number(record.get('per_stake_cost')) or 0.
        research, research_reason = research_view(record)
        cagey, cagey_reason = cagey_view(record)
        blocked = executable(record, config)
        if price is None or price <= 1:
            research = cagey = None
            research_reason = cagey_reason = 'no valid offered price'
        kind = offer_line_type(record.get('market'), record.get('handicap_line'))
        row = {k: record.get(k) for k in IDENTITY_COLUMNS}
        row.update(in_value_shortlist=record.get('decision') == 'SHORTLISTED',
                   in_cagey_tier=record.get('cagey_tier_decision') == 'SHORTLISTED')
        row.update(classify(research, cagey, price or 0., cost, *pinnacle_reference(record),
                            european=record.get('league') in european, config=config,
                            research_reason=research_reason, cagey_reason=cagey_reason,
                            pinnacle_profit=pinnacle_profit(record, kind), line_kind=kind))
        late = timing(record, clock, by_fixture.get(identity(record)), row.get('probability_source'), fits)
        row['timing_check'] = late or 'ok'
        if blocked is None and late is not None:
            blocked = f'timing: {late}'
        row.update(new_master_executable=blocked is None, _match=fixture_key(record))
        if blocked is not None:
            row['new_master_reason'] = blocked
        rows.append(row)
    select(rows, int(config['target_fixtures']), fill_min_no_loss=float(config['fill']['step_2_min_no_loss']))
    frame = pd.DataFrame(rows, columns=[*COLUMNS, '_match'])
    frame['new_master_version'] = config['version']
    frame = overlap(frame, live_master)
    order = frame.assign(_rank=pd.to_numeric(frame.new_master_rank, errors='coerce'),
                         _dec=frame.new_master_decision.map({d: i for i, d in enumerate(DECISIONS)}),
                         _grp=frame.new_master_group.map({g: i for i, g in enumerate(GROUPS)}),
                         _nl=-pd.to_numeric(frame.ranking_no_loss_probability, errors='coerce'))
    order = order.sort_values(['_rank', '_dec', '_grp', '_nl', 'kickoff_utc', 'league', 'home_team', 'away_team',
                               'market'], na_position='last', kind='stable')
    return order.reindex(columns=COLUMNS).reset_index(drop=True)


def _offer_key(row: Mapping) -> tuple:
    line = _number(row.get('handicap_line'))
    return (str(row.get('market') or ''), str(row.get('handicap_side') or ''),
            None if line is None else round(line, 4), round(_number(row.get('offered_decimal_odds')) or 0., 6))


def overlap(frame: pd.DataFrame, live_master: Optional[pd.DataFrame]) -> pd.DataFrame:
    from performance_tracking import fixture_key
    frame = frame.copy()
    frame['in_live_master'], frame['live_master_rank'], frame['live_master_same_offer'] = False, None, False
    if live_master is None or live_master.empty or frame.empty:
        return frame.drop(columns=['_match'], errors='ignore')
    live = {}
    for r in live_master.astype(object).where(live_master.notna(), None).to_dict('records'):
        live[fixture_key(r)] = (r.get('master_rank'), _offer_key(r))
    hits = [live.get(m) for m in frame['_match']]
    frame['in_live_master'] = [h is not None for h in hits]
    frame['live_master_rank'] = [h[0] if h else None for h in hits]
    frame['live_master_same_offer'] = [bool(h) and h[1] == _offer_key(r)
                                       for h, r in zip(hits, frame.to_dict('records'))]
    return frame.drop(columns=['_match'])


INSPECTION_FIELDS = ('new_master_rank', 'kickoff_utc', 'league', 'home_team', 'away_team', 'market_to_bet',
                     'offered_decimal_odds', 'research_no_loss_probability', 'cagey_no_loss_probability', 'gap_points',
                     'new_master_labels')


def summary(frame: pd.DataFrame, live_master: Optional[pd.DataFrame] = None, config: Optional[Mapping] = None,
            generated_at_utc: Optional[str] = None, top: int = 15) -> Dict[str, object]:
    """Counts of included and left-out offers, labels and flags, the "For inspection" section (ranked picks the
    research view strongly disputes, with p_r, p_c and g) and overlap with the live master. Counts are over the
    executable (Pinnacle, native market, odds window) offers; others are counted apart."""
    from performance_tracking import fixture_key
    config = config or load_config()
    ranked = frame.loc[frame.new_master_decision.eq('SHORTLISTED')]
    listed = frame.loc[~frame.new_master_decision.eq('NOT_EXECUTABLE')]
    offers = listed  # nominated, executable (as #172; rule v4: the only offers any step draws from)
    keys = lambda f: {fixture_key(r) for r in f.astype(object).where(f.notna(), None).to_dict('records')}
    viewed = listed.loc[pd.to_numeric(listed.ranking_no_loss_probability, errors='coerce').notna()
                        & pd.to_numeric(listed.ranking_profit_probability, errors='coerce').notna()]
    nominated_keys = keys(frame) if len(frame) else set()
    executable_keys = keys(listed) if len(listed) else set()
    viewed_keys = keys(viewed) if len(viewed) else set()
    target = int(config['target_fixtures'])
    timed = frame['timing_check'].fillna('ok') if 'timing_check' in frame else pd.Series('ok', index=frame.index)
    blocked_by_timing = frame.loc[timed.ne('ok')]
    timed_out_keys = (keys(blocked_by_timing) if len(blocked_by_timing) else set()) - executable_keys
    live = live_master if live_master is not None else pd.DataFrame()
    live_keys, ranked_keys = (keys(live) if len(live) else set()), keys(ranked) if len(ranked) else set()
    count = lambda f, column, names: {n: int(f[column].eq(n).sum()) for n in names}
    labels = lambda f: {text: int(f[column].eq(True).sum()) for column, text in LABELS}
    clean = lambda r, fields: {k: (None if pd.isna(r[k]) else r[k]) for k in fields}
    picks = [clean(r, ('new_master_rank', 'new_master_tier', 'kickoff_utc', 'league', 'home_team', 'away_team',
                       'market_to_bet', 'offered_decimal_odds', 'cagey_no_loss_probability',
                       'ranking_no_loss_probability', 'ranking_profit_probability', 'probability_source',
                       'research_no_loss_probability', 'gap_points', 'research_expected_return', 'market_price',
                       'new_master_labels', 'in_live_master', 'live_master_same_offer'))
             for r in ranked.head(top).to_dict('records')]
    flag = config['inspection_flag']
    sharpening = config['cagey_sharpening']
    return {
        'version': config['version'], 'status': config['status'], 'generated_at_utc': generated_at_utc,
        'config_sha256': hashlib.sha256(json.dumps(config, sort_keys=True).encode()).hexdigest(),
        'target_fixtures': int(config['target_fixtures']), 'ranked_fixtures': int(len(ranked)),
        'shortfall': max(0, target - int(len(ranked))),
        'nominated_fixtures': len(nominated_keys),
        'nominated_executable_fixtures': len(executable_keys),
        'fixtures_with_market_view': len(viewed_keys),
        'fixtures_without_market_view': len(executable_keys - viewed_keys),
        'short_reason': (None if len(ranked) >= target else
                         f'nominations cover fewer than {target} matches' if len(nominated_keys) < target else
                         f'nominations cover {len(nominated_keys)} matches but only {len(viewed_keys)} with an '
                         f'eligible offer (execution and timing checks) that has a market view'),
        'timing_check': {
            'rule': f"the live master's: one generation clock; offer and ranking reference quoted 0-"
                    f"{MAX_AGE_MINUTES} minutes before evaluation (none after it); reference inputs and offer at most "
                    f"{SYNC_SECONDS // 60} minutes apart",
            'ineligible_offers': int(timed.ne('ok').sum()),
            'by_reason': {reason: int(timed.eq(reason).sum()) for reason in TIMING_REASONS},
            'fixtures_losing_every_eligible_offer': len(timed_out_keys)},
        'picks_by_tier': count(ranked, 'new_master_tier', TIERS),
        'fill_candidates': {f'step_{n}': int(listed.new_master_step.eq(n).sum()) for n in (1, 2, 3)},
        'probabilities': ('sharpened cagey probabilities' if sharpening['use_sharpened']
                          else 'current cagey probabilities') + f" ({sharpening['version']}: {sharpening['status']})",
        'nominated_offers': int(len(frame)),
        'not_executable_offers': int(len(frame) - len(listed)), 'offers': int(len(offers)),
        'matches_with_a_pick_or_candidate': int(listed.loc[listed.new_master_step.notna(),
                                                           ['league', 'home_team', 'away_team', 'kickoff_utc']]
                                                .drop_duplicates().shape[0]),
        'matches': int(offers[['league', 'home_team', 'away_team', 'kickoff_utc']].drop_duplicates().shape[0])
        if len(offers) else 0,
        'offers_by_group': count(offers, 'new_master_group', GROUPS),
        'gap_checks': count(offers, 'gap_check', GAP_CHECKS),
        'left_out_by_reason': count(offers, 'left_out_reason', LEFT_OUT_REASONS),
        'labels_offers': labels(offers),
        'labels_ranked': labels(ranked),
        'decisions': count(frame, 'new_master_decision', DECISIONS),
        'european_offers': int(offers.unvalidated_view.eq(True).sum()),
        'european_ranked': int(ranked.unvalidated_view.eq(True).sum()),
        'for_inspection': {
            'rule': f"research strongly disagrees: g <= {flag['max_gap_points']:+.1f} points and cagey no-loss "
                    f">= {flag['min_cagey_no_loss']:.2f}; the bet keeps its place (the flag never removes or "
                    f"reorders a bet)",
            'flagged_offers': int(offers.inspection_flag.eq(True).sum()),
            'picks': [clean(r, INSPECTION_FIELDS) for r in ranked.loc[ranked.inspection_flag.eq(True)]
                      .to_dict('records')]},
        'overlap_with_live_master': {
            'live_master_fixtures': len(live_keys), 'new_master_fixtures': len(ranked_keys),
            'same_fixture': len(live_keys & ranked_keys),
            'same_offer': int(ranked.live_master_same_offer.eq(True).sum()),
            'live_only': len(live_keys - ranked_keys), 'new_only': len(ranked_keys - live_keys)},
        'top_picks': picks,
        'note': 'Shadow only: master_shortlist.csv, every probability, pick and stake are unchanged.'}


def write_shadow(decisions: pd.DataFrame, out_dir, live_master: Optional[pd.DataFrame] = None,
                 generated_at_utc: Optional[str] = None, predictions: Optional[pd.DataFrame] = None) -> pd.DataFrame:
    """Write the new master CSV and its summary beside master_shortlist.csv. Never touches the live files."""
    config = load_config()
    frame = reconcile(decisions, live_master, config, predictions, generated_at_utc)
    for name in SUPERSEDED_FILES:
        (Path(out_dir) / name).unlink(missing_ok=True)
    frame.to_csv(Path(out_dir) / config['file'], index=False)
    (Path(out_dir) / config['summary_file']).write_text(
        json.dumps(summary(frame, live_master, config, generated_at_utc), indent=2, default=str) + '\n',
        encoding='utf-8')
    return frame


# #170's shadow files: removed wherever a run writes or clears the new master (one shadow list only).
SUPERSEDED_FILES = ('master_shortlist_reconciled.csv', 'master_shortlist_reconciled_summary.json')


def remove_shadow(out_dir) -> None:
    config = load_config()
    for name in (config['file'], config['summary_file'], *SUPERSEDED_FILES):
        (Path(out_dir) / name).unlink(missing_ok=True)
