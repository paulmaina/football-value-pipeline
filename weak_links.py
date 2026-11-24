"""Weak-link flags on the live strong-team master's picks (Paul, 24 Nov 2026; docs/plan.md Phase 4d, Part 4).

Flag only: a flag never removes or reorders a pick. After the master list is built, a pick is a weak link if any of
these holds (thresholds in master_strong_config.json `weak_links`, since master-strong-team-v5):

  a) research no-loss is 8 or more points below the cagey no-loss;
  b) research no-loss below 0.75, or cagey no-loss below 0.75;
  c) the cagey view is missing, or fell back from D_pow2 to D (cagey_correction_fallback);
  d) the proven record rests on fewer than 8 of the last 10 matches, or the backed team's Elo expected score is
     within 0.03 of the strong-team line E;
  e) Pinnacle's fair probability for the bet has fallen 3 or more points since the earliest snapshot this run holds:
     the forecast runs archived in football_output_v2/performance/snapshots that were generated and captured before
     this run's clock and quote the same fixture and bet. Fair probability: the bet's Pinnacle quote with its opposite
     (1X2 for wins and double chance; the same Asian handicap line's other side), margin removed by the power method,
     as clv_report. No earlier snapshot holding the bet: the row notes "no movement data" (a note, not a flag);
  f) the pick sits in a "not proven" tier;
  g) any research warning on the offer (the value list's research_warnings, except the standing note that the research
     model has not passed a forward calibration gate), or a stale research fit for the fixture (the C6 or CE3n fit
     frozen in the forecast's research marked stale).

Each reason is written in plain words, prefixed with its letter ("(a) ..."), so the weekly review can grade each one.
"""
from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Dict, Iterable, List, Mapping, Optional, Tuple

import pandas as pd

SNAPSHOTS = Path(__file__).with_name('football_output_v2') / 'performance' / 'snapshots'
REASONS = ('a', 'b', 'c', 'd', 'e', 'f', 'g')
NOTE_NO_MOVEMENT = 'note: no movement data'
TOLERANCE = 1e-9


def _number(value) -> Optional[float]:
    try:
        n = float(value)
    except (TypeError, ValueError):
        return None
    return n if math.isfinite(n) else None


def _decode(value) -> object:
    if isinstance(value, (list, dict)):
        return value
    try:
        return json.loads(value) if value not in (None, '') and not (isinstance(value, float) and math.isnan(value)) \
            else None
    except (TypeError, ValueError):
        return None


def _power(prices: List[float]) -> Optional[List[float]]:
    if len(prices) < 2 or any(p is None or p <= 1 for p in prices):
        return None
    from football_value_pipeline_v2_standalone import devig
    try:
        return [float(x) for x in devig(list(prices), method='power')]
    except Exception:  # noqa: BLE001 - an unusable quote is simply no reference
        return None


# ---------------------------------------------------------------------------
# (e) Pinnacle's fair probability for one bet, from a forecast row's frozen quotes
# ---------------------------------------------------------------------------

def fair_probability(forecast: Optional[Mapping], market, side, line) -> Optional[float]:
    """Pinnacle's margin-free probability of the bet from the forecast row's frozen quotes (power method): the 1X2 quote
    for wins and double chance (price_edge_quotes, market h2h), the Asian handicap line's two prices
    (asian_handicap_offers: price and opposite_price of the backed side's line, or the other side's quote of the
    mirrored line). None when the run holds no such Pinnacle quote."""
    if forecast is None:
        return None
    market = str(market or '')
    if market in ('Home win', 'Away win', 'Double Chance 1X', 'Double Chance X2'):
        quotes = _decode(forecast.get('price_edge_quotes')) or []
        h2h = next((q for q in quotes if isinstance(q, Mapping) and q.get('bookmaker') == 'Pinnacle'
                    and q.get('market') == 'h2h'), None)
        prices = (h2h or {}).get('prices') or {}
        fair = _power([_number(prices.get(k)) for k in ('home', 'draw', 'away')]) if prices else None
        if fair is None:
            return None
        home, draw, away = fair
        return {'Home win': home, 'Away win': away, 'Double Chance 1X': home + draw, 'Double Chance X2': draw + away}[market]
    if not market.startswith('Asian Handicap') or side not in ('home', 'away') or _number(line) is None:
        return None
    line = round(float(line), 4)
    other = 'away' if side == 'home' else 'home'
    for quote in _decode(forecast.get('asian_handicap_offers')) or []:
        if not isinstance(quote, Mapping) or quote.get('bookmaker') != 'Pinnacle' or _number(quote.get('line')) is None:
            continue
        q_line = round(float(quote['line']), 4)
        pair = _power([_number(quote.get('price')), _number(quote.get('opposite_price'))])
        if pair is None:
            continue
        if quote.get('side') == side and q_line == line:
            return pair[0]
        if quote.get('side') == other and q_line == -line:
            return pair[1]
    return None


def earlier_forecasts(fixtures: Iterable[str], clock, snapshots: Optional[Path] = None,
                      lookback_days: int = 30) -> Dict[str, List[Tuple[pd.Timestamp, Mapping]]]:
    """fixture key -> [(generated_at, forecast row)] from the archived forecast runs generated AND captured before
    `clock` (and within lookback_days of it), oldest first. Only immutable archived runs count, so a replay of this
    run sees the same snapshots."""
    from performance_tracking import fixture_key, utc
    wanted = set(fixtures)
    out: Dict[str, List[Tuple[pd.Timestamp, Mapping]]] = {}
    base = Path(snapshots or SNAPSHOTS)
    clock = pd.Timestamp(utc(clock)) if clock is not None and utc(clock) is not None else None
    if not wanted or clock is None or not base.exists():
        return out
    for meta_path in sorted(base.glob('*/metadata.json')):
        if meta_path.parent.name.startswith('.capture-'):
            continue
        try:
            meta = json.loads(meta_path.read_text(encoding='utf-8'))
        except (OSError, ValueError):
            continue
        generated, captured = utc(meta.get('generated_at_utc')), utc(meta.get('captured_at_utc'))
        if generated is None or captured is None:
            continue
        generated, captured = pd.Timestamp(generated), pd.Timestamp(captured)
        if not (generated < clock and captured < clock and clock - generated <= pd.Timedelta(days=lookback_days)):
            continue
        path = meta_path.parent / 'predictions.csv'
        if not path.exists():
            continue
        try:
            frame = pd.read_csv(path, dtype=str, keep_default_na=False)
        except (pd.errors.EmptyDataError, ValueError):
            continue
        for row in frame.to_dict('records'):
            key = fixture_key(row)
            if key in wanted:
                out.setdefault(key, []).append((generated, row))
    for rows in out.values():
        rows.sort(key=lambda item: item[0])
    return out


def movement(row: Mapping, forecast: Optional[Mapping], earlier: List[Tuple[pd.Timestamp, Mapping]]) -> Optional[dict]:
    """The bet's fair probability now and at the earliest earlier snapshot that holds it; None without both."""
    now = fair_probability(forecast, row.get('market'), row.get('handicap_side'), row.get('handicap_line'))
    if now is None:
        return None
    for generated, past in earlier:
        then = fair_probability(past, row.get('market'), row.get('handicap_side'), row.get('handicap_line'))
        if then is not None:
            return {'now': now, 'earliest': then, 'earliest_generated_utc': generated.isoformat(),
                    'drop_points': 100 * (then - now)}
    return None


# ---------------------------------------------------------------------------
# The flags
# ---------------------------------------------------------------------------

def research_warnings(text, standing: str) -> List[str]:
    """The offer's research warnings worth flagging: every one except the standing note on every row."""
    items = [w.strip() for w in str(text or '').split('; ') if w.strip() and w.strip().lower() != 'nan']
    return [w for w in items if w != standing]


def stale_fits(forecast: Optional[Mapping]) -> List[str]:
    research = _decode((forecast or {}).get('team_research_json')) or {}
    if not isinstance(research, Mapping):
        return []
    return [name for name, field in (('C6', 'c6_fit'), ('CE3n', 'ce3n_fit'))
            if isinstance(research.get(field), Mapping) and research[field].get('stale')]


def reasons(row: Mapping, rule: Mapping, *, E: float, forecast: Optional[Mapping], warnings_text,
            fallback, move: Optional[dict]) -> Tuple[List[str], List[str]]:
    """(reasons that fired, notes) for one pick, each in plain words with its letter."""
    out, notes = [], []
    research = _number(row.get('research_no_loss_probability'))
    cagey = _number(row.get('cagey_no_loss_probability'))
    pct = lambda v: f'{v:.1%}'
    a = rule['a']
    if research is not None and cagey is not None and 100 * (cagey - research) + TOLERANCE >= a['min_gap_points']:
        out.append(f"(a) research no-loss {100 * (cagey - research):.1f} points below the cagey no-loss "
                   f"(research {pct(research)}, cagey {pct(cagey)})")
    b = rule['b']['min_no_loss']
    if research is not None and research + TOLERANCE < b:
        out.append(f"(b) research no-loss below {b:.0%} ({pct(research)})")
    if cagey is not None and cagey + TOLERANCE < b:
        out.append(f"(b) cagey no-loss below {b:.0%} ({pct(cagey)})")
    if cagey is None:
        out.append("(c) cagey view missing (ranked on Pinnacle's margin-free stand-in)")
    elif str(fallback or '').strip() not in ('', 'nan', 'None', 'False'):
        out.append(f"(c) cagey view fell back from D_pow2 to D ({str(fallback).strip()})")
    d = rule['d']
    matches = _number(row.get('strong_record_matches'))
    if matches is None or matches < d['min_record_matches']:
        out.append(f"(d) proven record on only {int(matches or 0)} of the last 10 matches "
                   f"(fewer than {d['min_record_matches']})")
    elo = _number(row.get('strong_elo_expectancy'))
    if elo is not None and abs(elo - float(E)) <= d['elo_margin'] + TOLERANCE:
        out.append(f"(d) backed team's Elo expected score {elo:.3f} within {d['elo_margin']:.2f} of the strong-team "
                   f"line {float(E):.2f}")
    e = rule['e']
    if move is None:
        notes.append(NOTE_NO_MOVEMENT)
    elif move['drop_points'] + TOLERANCE >= e['min_drop_points']:
        out.append(f"(e) Pinnacle fair probability fell {move['drop_points']:.1f} points since the earliest snapshot "
                   f"({pct(move['earliest'])} at {move['earliest_generated_utc'][:16]}Z, now {pct(move['now'])})")
    tier = str(row.get('strong_tier') or '')
    if tier.startswith('not proven'):
        out.append(f"(f) {tier} tier")
    for warning in research_warnings(warnings_text, rule['g']['standing_note']):
        out.append(f"(g) research warning: {warning}")
    for fit in stale_fits(forecast):
        out.append(f"(g) stale research fit ({fit})")
    return out, notes


def annotate(rows: List[Dict[str, object]], rule: Mapping, *, E: float, clock,
             snapshots: Optional[Path] = None) -> List[Dict[str, object]]:
    """Set weak_link ('yes' / 'no') and weak_link_reasons on every SHORTLISTED row (None on the others), in place.
    Each row carries its private inputs: _forecast (the run's forecast row), _research_warnings and _cagey_fallback."""
    from performance_tracking import fixture_key
    picks = [r for r in rows if r.get('strong_decision') == 'SHORTLISTED']
    earlier = earlier_forecasts({r['_match'] for r in picks}, clock, snapshots, int(rule['e']['lookback_days']))
    for row in rows:
        row['weak_link'], row['weak_link_reasons'] = None, None
    for row in picks:
        move = movement(row, row.get('_forecast'), earlier.get(row['_match'], []))
        fired, notes = reasons(row, rule, E=E, forecast=row.get('_forecast'), warnings_text=row.get('_research_warnings'),
                               fallback=row.get('_cagey_fallback'), move=move)
        row['weak_link'] = 'yes' if fired else 'no'
        row['weak_link_reasons'] = '; '.join(fired + notes)
    return rows


def reason_letters(text) -> List[str]:
    """The letters of the reasons in a weak_link_reasons text (notes excluded), in order, without repeats."""
    out = []
    for part in str(text or '').split('; '):
        part = part.strip()
        if len(part) > 3 and part[0] == '(' and part[2] == ')' and part[1] in REASONS and part[1] not in out:
            out.append(part[1])
    return out


def summary(frame: pd.DataFrame) -> Dict[str, object]:
    """The run's weak links: how many picks are flagged, by reason, and how many have no movement data."""
    if not len(frame) or 'weak_link' not in frame:
        return {'flagged_picks': 0, 'unflagged_picks': 0, 'by_reason': {letter: 0 for letter in REASONS},
                'picks_without_movement_data': 0}
    picks = frame.loc[frame.weak_link.isin(['yes', 'no'])]
    flagged = picks.loc[picks.weak_link.eq('yes')] if len(picks) else picks
    by_reason = {letter: 0 for letter in REASONS}
    for text in (flagged.weak_link_reasons if len(flagged) else []):
        for letter in reason_letters(text):
            by_reason[letter] += 1
    return {'flagged_picks': int(len(flagged)), 'unflagged_picks': int(len(picks) - len(flagged)),
            'by_reason': by_reason,
            'picks_without_movement_data': int(picks.weak_link_reasons.astype(str).str.contains(NOTE_NO_MOVEMENT).sum())
            if len(picks) else 0}
