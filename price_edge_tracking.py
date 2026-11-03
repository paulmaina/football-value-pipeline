"""Forward tracking for production policy v27 (AH price edge vs Pinnacle).

1. Grades every frozen v27 pick by closing line value against Pinnacle's
   near-kickoff price on the same AH line (the closing-odds workflow already
   collects it): clv = entry odds x Pinnacle fair close win-share - 1, with
   the two-way margin removed proportionally, as in the selection rule.
   Splits: bookmaker, odds band, reference type, favourite/underdog side and
   each narrow-margin tag (balanced, low_total, high_draw, even_odds, any tag, no tag).
2. Records every TAGGED candidate, picked or rejected, with the offered price
   vs fair at capture and the final result, so the narrow-margin hypothesis
   is measured forward even when no pick is made.

A STOP REVIEW flag is raised when at least 100 graded picks have mean CLV
below zero. v26 and older history is untouched. Evidence only: nothing here
changes forecasts, selection or stakes.

v28 adds the cagey tier (its own frozen list, cagey_tier_shortlist.csv) and
the cagey correction. Both tiers are graded by CLV and realised profit, split
by tier, policy, bookmaker, reference type (a, b, c, c-cagey), corrected
cagey-score quintile, each tag and "qualified only because of correction".
  * CAGEY REVIEW: >= 50 graded correction-only value picks with mean CLV < 0;
  * CAGEY TIER REVIEW: >= 50 graded cagey-tier picks whose realised ROI 95%
    interval is entirely below 0.
Each flag recommends switching its feature off; it never switches anything off.

Correction monitoring (v28) grades, per fixture, the first eligible pre-kickoff
record of the correction this run computed (cagey_correction_monitoring.csv):
2+/3+ margin rates by fixed quintile, corrected vs uncorrected log loss with a
paired gain, and returns at both fair prices (a calibration diagnostic, not
bookmaker ROI). CORRECTION REVIEW: >= 200 graded fixtures whose paired 2+
log-loss gain interval is entirely below 0; it recommends review only.
"""
from __future__ import annotations

import math
from datetime import timedelta
from pathlib import Path
from typing import Dict, List, Optional

import numpy as np
import pandas as pd

from price_edge_shortlist import POLICY, TAGS
from price_edge_cagey_shortlist import (POLICY as CAGEY_POLICY, MONITOR_FILE, MONITOR_LINES, MONITOR_VERSION,
                                        BOOK_COLUMNS, usable_quote)
import narrow_margin as nm
POLICIES = (POLICY, CAGEY_POLICY)  # v27 and v28 value-tier picks are graded together, split by policy.
from price_edge_cagey_shortlist import TIER_FILE
CAGEY_REVIEW_MIN_PICKS = 50
CAGEY_TIER_REVIEW_MIN_PICKS = 50

VERSION = 'price-edge-v27-tracking-v1'
FILE = 'price_edge_tagged_candidates.csv'
OUTPUT_DIR = Path('performance') / 'price_edge_v27'
STOP_REVIEW_MIN_PICKS = 100
MIN_LEAD_MINUTES = 20
COLUMNS = ['list_version', 'generated_at_utc', 'league', 'home_team', 'away_team', 'kickoff_utc', 'fixture_id',
           'market', 'market_to_bet', 'handicap_side', 'handicap_line', 'side_role', 'bookmaker',
           'offered_decimal_odds', 'fair_probability', 'fair_odds', 'reference_type', 'edge', 'decision',
           'rejection_reasons', 'tagged_probe', *TAGS, 'pinnacle_draw_probability', 'pinnacle_over_2_5_probability',
           'cagey_score', 'cagey_fit']
EQUIVALENT = {'Home win': ('home', -0.5), 'Away win': ('away', -0.5),
              'Double Chance 1X': ('home', 0.5), 'Double Chance X2': ('away', 0.5)}
SPLITS = ('bookmaker', 'odds_band', 'reference_type', 'side_role', 'balanced', 'low_total', 'high_draw', 'even_odds', 'tagged',
          'cagey_quintile')
TIER_SPLITS = ('tier', 'policy', 'bookmaker', 'reference_type', 'corrected_cagey_quintile', 'balanced', 'low_total',
               'high_draw', 'even_odds', 'qualified_only_by_correction')
QUINTILES = ('Q1 cagiest', 'Q2', 'Q3', 'Q4', 'Q5 most open')


def cagey_quintiles(scores) -> pd.Series:
    """Quintile of the cagey score within the graded set (Q1 = lowest P(2+ margin)); n/a when unavailable."""
    values = pd.to_numeric(pd.Series(scores), errors='coerce')
    out = pd.Series('n/a', index=values.index, dtype=object)
    known = values.dropna()
    if known.nunique() >= len(QUINTILES):
        out[known.index] = pd.qcut(known.rank(method='first'), len(QUINTILES), labels=QUINTILES).astype(str)
    return out


# ---------------------------------------------------------------------------
# Tagged-candidate sidecar
# ---------------------------------------------------------------------------

def write_list(decisions: pd.DataFrame, raw: Path, generated) -> List[dict]:
    """Every tagged candidate of this run (picked, rejected or probe), bound to its generation instant."""
    from performance_tracking import write_csv
    rows = []
    if len(decisions) and 'any_tag' in decisions:
        tagged = decisions.loc[decisions.any_tag.fillna(False).astype(bool)]
        rows = (tagged.reindex(columns=COLUMNS).assign(list_version=VERSION, generated_at_utc=generated)
                .astype(object).where(lambda f: f.notna(), None).to_dict('records'))
    write_csv(Path(raw) / FILE, rows, COLUMNS)
    return rows


def capture_file(raw: Path, generated) -> Optional[Path]:
    """Archive only a list bound to this exact generation instant."""
    from performance_tracking import read_csv, utc
    path = Path(raw) / FILE
    if not path.exists():
        return None
    rows = read_csv(path)
    if any(r.get('list_version') != VERSION or utc(r.get('generated_at_utc')) != utc(generated) for r in rows):
        return None
    return path


def capture_tier_file(raw: Path, generated) -> Optional[Path]:
    """Archive the cagey-tier list only when it belongs to this exact v28 generation."""
    from performance_tracking import read_csv, utc
    path = Path(raw) / TIER_FILE
    if not path.exists():
        return None
    rows = read_csv(path)
    if any(r.get('selection_policy_version') != CAGEY_POLICY or utc(r.get('evaluated_at_utc')) != utc(generated)
           for r in rows):
        return None
    return path


def archived_tier_rows(root: Path, archive) -> List[dict]:
    """Every pre-kickoff archived cagey-tier pick, oldest capture first."""
    from performance_tracking import read_csv, utc
    rows = []
    for meta, _, _ in sorted(archive, key=lambda item: item[0]['captured_at_utc']):
        path = Path(root) / 'performance' / 'snapshots' / meta['git_commit_sha'][:16] / TIER_FILE
        if TIER_FILE not in meta.get('sha256', {}) or not path.exists():
            continue
        captured, generated = utc(meta['captured_at_utc']), utc(meta['generated_at_utc'])
        for row in read_csv(path):
            kick = utc(row.get('kickoff_utc'))
            if kick is None or max(captured, generated) > kick - timedelta(minutes=MIN_LEAD_MINUTES):
                continue
            rows.append({**row, 'snapshot_commit': meta['git_commit_sha'],
                         'snapshot_captured_utc': meta['captured_at_utc']})
    return rows


def frozen_tier_picks(root: Path, archive) -> List[dict]:
    """Latest pre-kickoff archived cagey-tier pick per fixture."""
    from performance_tracking import fixture_key
    return list({fixture_key(row): row for row in archived_tier_rows(root, archive)}.values())


# ---------------------------------------------------------------------------
# Correction monitoring (v28): forward calibration evidence, never a decision
# ---------------------------------------------------------------------------

CORRECTION_REVIEW_MIN_FIXTURES = 200
BOOTSTRAP_SAMPLES = 2000


def capture_monitoring_file(raw: Path, generated) -> Optional[Path]:
    """Archive the correction-monitoring records only when bound to this exact generation instant."""
    from performance_tracking import read_csv, utc
    path = Path(raw) / MONITOR_FILE
    if not path.exists():
        return None
    rows = read_csv(path)
    if any(r.get('monitoring_version') != MONITOR_VERSION or utc(r.get('generated_at_utc')) != utc(generated)
           for r in rows):
        return None
    return path


def _exclusion(row: dict, meta: dict) -> Optional[str]:
    """Why an archived record cannot count as forward evidence, or None when it can."""
    from performance_tracking import utc
    captured, generated = utc(meta.get('captured_at_utc')), utc(meta.get('generated_at_utc'))
    kick, stamp = utc(row.get('kickoff_utc')), utc(row.get('generated_at_utc'))
    latest_input = utc(row.get('latest_input_quote_utc'))
    if kick is None or captured is None or generated is None or stamp != generated:
        return 'record not bound to its snapshot generation'
    if row.get('status') != 'USABLE':
        return row.get('exclusion_reason') or 'unusable market-implied fit'
    if max(captured, generated) > kick - timedelta(minutes=MIN_LEAD_MINUTES):
        return f'captured less than {MIN_LEAD_MINUTES} minutes before kickoff'
    if latest_input is None or latest_input > generated or latest_input >= kick:
        return 'input quote not observed before generation'
    return None


def _validated_prices(row: dict) -> dict:
    """Blank any recorded bookmaker price whose own quote was not fresh at generation or not before kickoff."""
    out, blanked = dict(row), 0
    for side in ('home', 'away'):
        for line in MONITOR_LINES:
            for column in BOOK_COLUMNS.values():
                key = f"{side}_plus_{line:g}".replace('.', '_') + '_' + column
                if out.get(key) not in (None, '') and not usable_quote(out.get(key + '_utc'), out.get('generated_at_utc'),
                                                                       out.get('kickoff_utc')):
                    out[key], blanked = None, blanked + 1
    out['prices_blanked'] = blanked
    return out


def first_monitoring_records(root: Path, archive) -> List[dict]:
    """One record per fixture: its first eligible pre-kickoff capture, else its first record with the reason."""
    from performance_tracking import fixture_key, read_csv
    first, fallback = {}, {}
    for meta, _, _ in sorted(archive, key=lambda item: item[0]['captured_at_utc']):
        path = Path(root) / 'performance' / 'snapshots' / meta['git_commit_sha'][:16] / MONITOR_FILE
        if MONITOR_FILE not in meta.get('sha256', {}) or not path.exists():
            continue
        for row in read_csv(path):
            key = fixture_key(row)
            reason = _exclusion(row, meta)
            item = {**_validated_prices(row), 'fixture_key': key, 'snapshot_commit': meta['git_commit_sha'],
                    'snapshot_captured_utc': meta['captured_at_utc'], 'exclusion_reason': reason or ''}
            if reason is None:
                first.setdefault(key, item)
            else:
                fallback.setdefault(key, item)
    return [first.get(key) or fallback[key] for key in sorted(set(first) | set(fallback))]


def _number(value) -> Optional[float]:
    value = pd.to_numeric(value, errors='coerce')
    return float(value) if pd.notna(value) else None


def _log_loss(p: float, outcome: bool) -> float:
    p = min(max(p, 1e-12), 1 - 1e-12)
    return -math.log(p if outcome else 1 - p)


def grade_monitoring(rows: List[dict], records: List[dict], clock) -> pd.DataFrame:
    """Per fixture: state (GRADED, PENDING, EXCLUDED), outcomes, log losses and fair-price returns."""
    from asian_handicap import profit
    from performance_tracking import fixture_match, utc
    graded = []
    for row in rows:
        item = {**row, 'state': 'EXCLUDED' if row['exclusion_reason'] else 'PENDING', 'final_score': None}
        kick = utc(row.get('kickoff_utc'))
        if item['state'] == 'PENDING' and kick is not None and kick <= clock - timedelta(hours=2):
            match, state = fixture_match(row, records)
            if state == 'VERIFIED_FINISHED':
                home, away = int(match['home_goals']), int(match['away_goals'])
                margin = abs(home - away)
                item.update(state='GRADED', final_score=f'{home}-{away}', abs_margin=margin,
                            gameweek=f'{kick.isocalendar().year}-W{kick.isocalendar().week:02d}')
                for goals in (2, 3):
                    for basis in ('corrected', 'uncorrected'):
                        item[f'log_loss_{goals}plus_{basis}'] = _log_loss(_number(row[f'{basis}_p{goals}']), margin >= goals)
                    item[f'log_loss_gain_{goals}plus'] = (item[f'log_loss_{goals}plus_uncorrected']
                                                          - item[f'log_loss_{goals}plus_corrected'])
                for side in ('home', 'away'):
                    for line in MONITOR_LINES:
                        key = f'{side}_plus_{line:g}'.replace('.', '_')
                        for basis in ('corrected', 'uncorrected'):
                            odds = _number(row.get(f'{key}_{basis}_fair_odds'))
                            item[f'{key}_return_{basis}'] = (profit(home, away, side, line, odds)[1]
                                                             if odds is not None and odds > 1 else None)
        graded.append(item)
    return pd.DataFrame(graded)


def _interval(values, blocks) -> Dict[str, object]:
    from ah_close_backtest import block_bootstrap
    values = pd.to_numeric(pd.Series(list(values)), errors='coerce')
    blocks = pd.Series(list(blocks))
    keep = values.notna().to_numpy()
    if not keep.any():
        return {'n': 0, 'mean': None, 'low95': None, 'high95': None}
    mean, low, high = block_bootstrap(values[keep].to_numpy(), blocks[keep].to_numpy(), n_boot=BOOTSTRAP_SAMPLES)
    return {'n': int(keep.sum()), 'mean': mean, 'low95': low, 'high95': high}


def monitoring_summary(frame: pd.DataFrame) -> Dict[str, object]:
    states = frame['state'].value_counts().to_dict() if len(frame) else {}
    graded = frame[frame['state'] == 'GRADED'] if len(frame) else frame
    eligible = frame[frame['state'] != 'EXCLUDED'] if len(frame) else frame
    out = {'version': MONITOR_VERSION,
           'monitoring_start_utc': min(eligible['snapshot_captured_utc']) if len(eligible) else None,
           'model_versions': sorted(set(frame['model_version'].dropna())) if len(frame) else [],
           'fixtures': {'eligible': int(len(eligible)), 'pending': int(states.get('PENDING', 0)),
                        'graded': int(states.get('GRADED', 0)), 'excluded': int(states.get('EXCLUDED', 0))},
           'excluded_by_reason': (frame.loc[frame['state'] == 'EXCLUDED', 'exclusion_reason'].value_counts().to_dict()
                                  if len(frame) else {}),
           'by_quintile': {}, 'log_loss': {}, 'fair_price_returns': {}}
    if not len(graded):
        out['correction_review'] = False
        return out
    blocks = graded['gameweek']
    for label in nm.QUINTILE_LABELS:
        part = graded[graded['corrected_cagey_quintile'] == label]
        out['by_quintile'][label] = {
            'n': int(len(part)),
            **{f'{goals}plus_{kind}': (float((part['abs_margin'] >= goals).mean()) if kind == 'actual'
                                       else float(pd.to_numeric(part[f'{kind}_p{goals}']).mean())) if len(part) else None
               for goals in (2, 3) for kind in ('actual', 'corrected', 'uncorrected')},
            # Gameweek-block bootstrap interval for each actual rate.
            **{f'{goals}plus_actual_interval': _interval((part['abs_margin'] >= goals).astype(float), part['gameweek'])
               for goals in (2, 3)}}
    for goals in (2, 3):
        out['log_loss'][f'{goals}plus'] = {
            'corrected': float(graded[f'log_loss_{goals}plus_corrected'].mean()),
            'uncorrected': float(graded[f'log_loss_{goals}plus_uncorrected'].mean()),
            'paired_gain': _interval(graded[f'log_loss_gain_{goals}plus'], blocks)}
    # Every AH line of every fixture, kept in its fixture's gameweek block.
    for basis in ('corrected', 'uncorrected'):
        columns = [c for c in graded.columns if c.endswith(f'_return_{basis}')]
        stacked = graded[[*columns, 'gameweek']].melt(id_vars='gameweek', value_vars=columns)
        out['fair_price_returns'][basis] = _interval(stacked['value'], stacked['gameweek'])
    gain = out['log_loss']['2plus']['paired_gain']
    out['correction_review'] = bool(gain['n'] >= CORRECTION_REVIEW_MIN_FIXTURES and gain['high95'] is not None
                                    and gain['high95'] < 0)
    return out


def _interval_text(m: dict, scale: float = 1.0, unit: str = '') -> str:
    if not m.get('n'):
        return 'n/a (0)'
    return (f"{m['mean'] * scale:+.3f}{unit} [{m['low95'] * scale:+.3f}, {m['high95'] * scale:+.3f}] "
            f"(n={m['n']})")


def monitoring_report(m: dict) -> List[str]:
    f = m['fixtures']
    lines = ['## Correction monitoring', '']
    if m.get('correction_review'):
        gain = m['log_loss']['2plus']['paired_gain']
        lines += [f"> **CORRECTION REVIEW**: {gain['n']} graded forward fixtures with a paired 2+ margin log-loss gain "
                  f"of {_interval_text(gain, 1000)} x 1e-3, interval entirely below 0. Recommendation: review the "
                  'correction (this report does not change selection, the correction or stakes).', '']
    lines += [f"Forward monitoring of {MONITOR_VERSION} started {m['monitoring_start_utc'] or 'not yet'} "
              '(first eligible capture). Earlier forecasts are not backfilled. One record per fixture: its first '
              f'pre-kickoff capture at least {MIN_LEAD_MINUTES} minutes before kickoff. Quintiles use the fixed '
              'training-period boundaries stored with the model.', '',
              f"Fixtures: eligible {f['eligible']}, pending {f['pending']}, graded {f['graded']}, "
              f"excluded {f['excluded']}.", '']
    if m['excluded_by_reason']:
        lines += ['| excluded because | fixtures |', '|---|---:|']
        lines += [f'| {k} | {v} |' for k, v in m['excluded_by_reason'].items()]
        lines.append('')
    if not f['graded']:
        return lines + ['No graded fixtures yet.', '']
    lines += ['| quintile | n | 2+ actual | 2+ corrected | 2+ uncorrected | 3+ actual | 3+ corrected | 3+ uncorrected |',
              '|---|---:|---:|---:|---:|---:|---:|---:|']
    def rate(q, goals, kind):
        value = q.get(f'{goals}plus_{kind}')
        if value is None:
            return 'n/a'
        band = q.get(f'{goals}plus_actual_interval') if kind == 'actual' else None
        return f'{value:.1%} [{band["low95"]:.1%}, {band["high95"]:.1%}]' if band and band.get('n') else f'{value:.1%}'
    for label, q in m['by_quintile'].items():
        cells = [rate(q, g, k) for g in (2, 3) for k in ('actual', 'corrected', 'uncorrected')]
        lines.append(f"| {label} | {q['n']} | " + ' | '.join(cells) + ' |')
    lines += ['', '| log loss | corrected | uncorrected | paired gain x 1e-3 [95%] |', '|---|---:|---:|---|']
    for goals in (2, 3):
        ll = m['log_loss'][f'{goals}plus']
        lines.append(f"| {goals}+ margin | {ll['corrected']:.4f} | {ll['uncorrected']:.4f} | "
                     f"{_interval_text(ll['paired_gain'], 1000)} |")
    r = m['fair_price_returns']
    lines += ['', 'Calibration diagnostic, NOT achievable bookmaker ROI: return per bet when every AH +1 to +2 line '
              'on both sides is settled at its own fair price (no margin). A calibrated price returns about 0.',
              f"- at the corrected fair price: {_interval_text(r['corrected'], 100, '%')}",
              f"- at the uncorrected fair price: {_interval_text(r['uncorrected'], 100, '%')}", '',
              'Actual rates show their 95% interval in brackets. '
              f'Intervals: gameweek-block bootstrap ({BOOTSTRAP_SAMPLES} resamples); every line of a fixture stays in '
              f'its gameweek block. CORRECTION REVIEW: >= {CORRECTION_REVIEW_MIN_FIXTURES} graded fixtures with the '
              '2+ paired log-loss gain interval entirely below 0; it recommends review only.', '']
    return lines


def tier_frame(value: pd.DataFrame, tier: pd.DataFrame) -> pd.DataFrame:
    """Both tiers in one frame with the v28 tracking splits."""
    parts = [f.assign(tier=name) for name, f in (('value', value), ('cagey', tier)) if len(f)]
    if not parts:
        return pd.DataFrame(columns=[*TIER_SPLITS, 'clv', 'unit_profit'])
    frame = pd.concat(parts, ignore_index=True, sort=False)
    versions = frame.get('selection_policy_version', pd.Series(index=frame.index, dtype=object))
    frame['policy'] = versions.map({POLICY: 'v27', CAGEY_POLICY: 'v28'}).fillna('other')
    frame['corrected_cagey_quintile'] = cagey_quintiles(frame.get('corrected_cagey_score',
                                                                  pd.Series(index=frame.index, dtype=float)))
    flag = frame.get('qualified_only_by_correction', pd.Series(index=frame.index, dtype=object))
    frame['qualified_only_by_correction'] = flag.map(lambda v: 'yes' if _flag(v) else 'no')
    return frame


def cagey_flags(frame: pd.DataFrame) -> Dict[str, object]:
    """Review flags; each recommends switching its feature off and never does so itself."""
    if frame.empty:
        value_only, tier = pd.Series(dtype=float), pd.Series(dtype=float)
    else:
        value_only = frame.loc[(frame.tier == 'value') & (frame.qualified_only_by_correction == 'yes'), 'clv']
        tier = frame.loc[frame.tier == 'cagey', 'unit_profit']
    only, roi = summarize(value_only), summarize(tier)
    cagey_review = only['n'] >= CAGEY_REVIEW_MIN_PICKS and only['mean'] < 0
    tier_review = (roi['n'] >= CAGEY_TIER_REVIEW_MIN_PICKS and roi['standard_error'] is not None
                   and roi['mean'] + 1.96 * roi['standard_error'] < 0)
    return {'correction_only_clv': only, 'cagey_tier_roi': roi,
            'cagey_review': bool(cagey_review), 'cagey_tier_review': bool(tier_review),
            'cagey_review_rule': f'>= {CAGEY_REVIEW_MIN_PICKS} graded correction-only value picks with mean CLV < 0; '
                                 'recommends cagey_correction_enabled = false',
            'cagey_tier_review_rule': f'>= {CAGEY_TIER_REVIEW_MIN_PICKS} graded cagey-tier picks with realised ROI 95% '
                                      'interval entirely below 0; recommends cagey_tier_enabled = false'}


def frozen_candidates(root: Path, archive) -> List[dict]:
    """Latest pre-kickoff archived entry per fixture, side, line and bookmaker."""
    from performance_tracking import fixture_key, read_csv, utc
    frozen = {}
    for meta, _, _ in sorted(archive, key=lambda item: item[0]['captured_at_utc']):
        path = Path(root) / 'performance' / 'snapshots' / meta['git_commit_sha'][:16] / FILE
        if FILE not in meta.get('sha256', {}) or not path.exists():
            continue
        captured, generated = utc(meta['captured_at_utc']), utc(meta['generated_at_utc'])
        for row in read_csv(path):
            kick = utc(row.get('kickoff_utc'))
            if kick is None or max(captured, generated) > kick - timedelta(minutes=MIN_LEAD_MINUTES):
                continue
            key = (fixture_key(row), row.get('handicap_side'), row.get('handicap_line'), row.get('bookmaker') or '')
            frozen[key] = {**row, 'snapshot_commit': meta['git_commit_sha'], 'snapshot_captured_utc': meta['captured_at_utc']}
    return list(frozen.values())


# ---------------------------------------------------------------------------
# Closing line value
# ---------------------------------------------------------------------------

def ah_line(market: str, side=None, line=None):
    """(side, line) a v27 market settles as."""
    from asian_handicap import parse_label
    parsed = parse_label(market)
    if parsed:
        return parsed
    if market in EQUIVALENT:
        return EQUIVALENT[market]
    try:
        return (side, float(line)) if side in ('home', 'away') else None
    except (TypeError, ValueError):
        return None


def close_win_share(quotes: List[dict], side: str, line: float) -> Optional[float]:
    """Pinnacle fair close win-share on (side, line), proportional margin removal."""
    from asian_handicap import label
    from ah_close_backtest import devig_proportional
    pinnacle = {q['selection']: float(q['decimal_odds']) for q in quotes
                if q.get('bookmaker') == 'pinnacle' and q.get('decimal_odds')}
    mine, other = label(side, line), label('away' if side == 'home' else 'home', -line)
    if mine in pinnacle and other in pinnacle:
        return devig_proportional(pinnacle[mine], pinnacle[other])[0]
    if abs(line) == 0.5 and all(k in pinnacle for k in ('home', 'draw', 'away')):
        total = sum(1 / pinnacle[k] for k in ('home', 'draw', 'away'))
        p = {k: (1 / pinnacle[k]) / total for k in ('home', 'draw', 'away')}
        opponent = 'away' if side == 'home' else 'home'
        return p[side] if line < 0 else 1 - p[opponent]
    return None


def closing_for(row: dict, observations: List[dict], side: str, line: float):
    """Latest near-kickoff observation after capture that prices (side, line) for Pinnacle."""
    from performance_tracking import fixture_key, utc
    best = None
    for obs in observations:
        if fixture_key(obs['fixture']) != fixture_key(row) or utc(obs['fixture']['kickoff_utc']) != utc(row['kickoff_utc']):
            continue
        if utc(obs['observed_at_utc']) < utc(row['snapshot_captured_utc']):
            continue
        q = close_win_share(obs.get('quotes', []), side, line)
        if q is not None and (best is None or utc(obs['observed_at_utc']) > best[0]):
            best = (utc(obs['observed_at_utc']), q)
    return best


def odds_band(odds) -> Optional[str]:
    from price_edge_backtest import odds_band as band
    try:
        return band(float(odds))
    except (TypeError, ValueError, StopIteration):
        return None


def _flag(value) -> bool:
    return str(value).strip().lower() in ('true', '1')


def settle(row: dict, final: Optional[dict], side: str, line: float, price) -> Dict[str, object]:
    from asian_handicap import profit
    if not final:
        return {'result_status': None, 'unit_profit': None}
    try:
        status, gain = profit(int(final['home_goals']), int(final['away_goals']), side, line, float(price))
    except (TypeError, ValueError, KeyError):
        return {'result_status': None, 'unit_profit': None}
    return {'result_status': status, 'unit_profit': gain}


def grade(rows: List[dict], observations: List[dict], records: List[dict], clock) -> pd.DataFrame:
    from performance_tracking import fixture_match, utc
    graded = []
    for row in rows:
        target = ah_line(row.get('market'), row.get('handicap_side'), row.get('handicap_line'))
        if target is None:
            continue
        side, line = target
        price = pd.to_numeric(row.get('offered_decimal_odds'), errors='coerce')
        fair = pd.to_numeric(row.get('fair_odds'), errors='coerce')
        close = closing_for(row, observations, side, line)
        final = None
        kick = utc(row.get('kickoff_utc'))
        if kick is not None and kick <= clock - timedelta(hours=2):
            match, state = fixture_match(row, records)
            final = match if state == 'VERIFIED_FINISHED' else None
        item = {**row, 'ah_side': side, 'ah_line': line, 'odds_band': odds_band(price),
                'tagged': 'any tag' if any(_flag(row.get(t)) for t in TAGS) else 'no tag',
                **{t: 'yes' if _flag(row.get(t)) else 'no' for t in TAGS},
                'close_observed_at_utc': close[0].isoformat() if close else None,
                'pinnacle_close_win_share': close[1] if close else None,
                'clv': float(price) * close[1] - 1 if close and pd.notna(price) else None,
                'final_score': f"{final['home_goals']}-{final['away_goals']}" if final else None,
                **settle(row, final, side, line, price if pd.notna(price) else None)}
        fair_result = settle(row, final, side, line, fair if pd.notna(fair) and fair > 1 else None)
        item['return_at_capture_fair'] = fair_result['unit_profit']
        graded.append(item)
    frame = pd.DataFrame(graded)
    if len(frame):
        frame['cagey_quintile'] = cagey_quintiles(frame.get('cagey_score', pd.Series(index=frame.index, dtype=float)))
    return frame


def summarize(values) -> Dict[str, object]:
    values = pd.to_numeric(pd.Series(values), errors='coerce').dropna()
    if values.empty:
        return {'n': 0, 'mean': None, 'positive_share': None, 'standard_error': None}
    se = float(values.std(ddof=1) / math.sqrt(len(values))) if len(values) > 1 else None
    return {'n': int(len(values)), 'mean': float(values.mean()), 'positive_share': float((values > 0).mean()),
            'standard_error': se}


def split_table(frame: pd.DataFrame, value: str, columns=SPLITS) -> Dict[str, Dict[str, dict]]:
    out = {}
    for column in columns:
        if frame.empty or column not in frame:
            out[column] = {}
            continue
        out[column] = {str(k): summarize(g[value]) for k, g in frame.groupby(frame[column].fillna('n/a'), sort=True)}
    return out


def review(root: Path, archive, records: List[dict], clock) -> dict:
    """Write performance/price_edge_v27/{summary.json, picks.csv, tagged_candidates.csv, report.md}."""
    from performance_tracking import frozen_rows, write_json
    from closing_odds import load_observations
    root = Path(root)
    observations, rejected = load_observations(root, clock)
    picks = [r for r in frozen_rows(archive, 'shortlist', latest=True) if r.get('selection_policy_version') in POLICIES]
    graded = grade(picks, observations, records, clock)
    tagged = grade(frozen_candidates(root, archive), observations, records, clock)
    tier = grade(frozen_tier_picks(root, archive), observations, records, clock)
    monitoring = grade_monitoring(first_monitoring_records(root, archive), records, clock)
    both = tier_frame(graded, tier)
    flags = cagey_flags(both)
    clv = graded['clv'] if len(graded) else pd.Series(dtype=float)
    overall = summarize(clv)
    stop = overall['n'] >= STOP_REVIEW_MIN_PICKS and overall['mean'] is not None and overall['mean'] < 0
    summary = {
        'version': VERSION, 'policy': POLICY, 'reviewed_at_utc': clock.isoformat(),
        'frozen_picks': int(len(graded)), 'clv': overall,
        'profit': summarize(graded['unit_profit'] if len(graded) else []),
        'stop_review': bool(stop),
        'stop_review_rule': f'>= {STOP_REVIEW_MIN_PICKS} graded picks with mean CLV < 0',
        'clv_by': split_table(graded, 'clv'),
        'cagey_tier_picks': int(len(tier)),
        'cagey_tier': {'clv': summarize(tier['clv'] if len(tier) else []),
                       'profit': summarize(tier['unit_profit'] if len(tier) else [])},
        'both_tiers_clv_by': split_table(both, 'clv', TIER_SPLITS),
        'both_tiers_profit_by': split_table(both, 'unit_profit', TIER_SPLITS),
        **flags,
        'tagged_candidates': {
            'frozen': int(len(tagged)),
            'with_offered_price': int(tagged['offered_decimal_odds'].notna().sum()) if len(tagged) else 0,
            'edge_at_capture_1xbet': summarize(tagged.loc[tagged.bookmaker.eq('1xBet'), 'edge'] if len(tagged) else []),
            'return_at_capture_fair': summarize(tagged['return_at_capture_fair'] if len(tagged) else []),
            'return_at_capture_fair_plus_lines': summarize(
                tagged.loc[tagged.ah_line.astype(float) > 0, 'return_at_capture_fair'] if len(tagged) else []),
            'by_tag': {t: summarize(tagged.loc[tagged[t].eq('yes'), 'return_at_capture_fair'] if len(tagged) else [])
                       for t in TAGS}},
        'correction_monitoring': monitoring_summary(monitoring),
        'rejected_observation_files': rejected,
        'note': 'CLV = entry odds x Pinnacle near-kickoff fair win-share on the same AH line - 1 (proportional). '
                'Near-kickoff feed quotes, not verified official closes or executed bets. Tagged candidates are '
                'tracked for the narrow-margin hypothesis only; they never change a decision.',
    }
    dest = root / OUTPUT_DIR
    dest.mkdir(parents=True, exist_ok=True)
    write_json(dest / 'summary.json', summary)
    graded.to_csv(dest / 'picks.csv', index=False)
    tagged.to_csv(dest / 'tagged_candidates.csv', index=False)
    tier.to_csv(dest / 'cagey_tier_picks.csv', index=False)
    monitoring.to_csv(dest / 'correction_monitoring.csv', index=False)
    (dest / 'report.md').write_text(report(summary), encoding='utf-8')
    return summary


def _fmt(m: dict) -> str:
    if not m.get('n'):
        return 'n/a (0)'
    se = f" ± {1.96 * m['standard_error']:.2%}" if m.get('standard_error') else ''
    return f"{m['mean']:+.2%}{se} (n={m['n']})"


def report(summary: dict) -> str:
    lines = ['# v27/v28 price-edge tracking', '']
    if summary.get('cagey_review'):
        lines += [f"> **CAGEY REVIEW**: {summary['correction_only_clv']['n']} graded correction-only value picks with "
                  f"mean CLV {summary['correction_only_clv']['mean']:+.2%}. Recommendation: set "
                  'cagey_correction_enabled to false (this report does not change it).', '']
    if summary.get('cagey_tier_review'):
        roi = summary['cagey_tier_roi']
        lines += [f"> **CAGEY TIER REVIEW**: {roi['n']} graded cagey-tier picks with realised ROI {_fmt(roi)}, interval "
                  'entirely below 0. Recommendation: set cagey_tier_enabled to false (this report does not change it).', '']
    if summary['stop_review']:
        lines += [f"> **STOP REVIEW**: {summary['clv']['n']} graded picks with mean CLV {summary['clv']['mean']:+.2%} "
                  '(below zero). Review the policy before relying on further picks.', '']
    lines += [f"Reviewed {summary['reviewed_at_utc']}. Frozen v27 picks: {summary['frozen_picks']}.", '',
              f"**Mean CLV vs Pinnacle close:** {_fmt(summary['clv'])}. **Flat-stake profit per bet:** {_fmt(summary['profit'])}.",
              f"STOP REVIEW rule: {summary['stop_review_rule']}.", '']
    for column, groups in summary['clv_by'].items():
        lines += [f'## CLV by {column}', '', '| group | mean CLV (n) |', '|---|---|']
        lines += [f'| {k} | {_fmt(v)} |' for k, v in groups.items()] or ['| none | n/a |']
        lines.append('')
    if 'both_tiers_clv_by' in summary:
        lines += ['## Both tiers (value and cagey)', '',
                  f"Cagey-tier picks frozen: {summary['cagey_tier_picks']}; CLV {_fmt(summary['cagey_tier']['clv'])}; "
                  f"realised profit per bet {_fmt(summary['cagey_tier']['profit'])}. Correction-only value picks: "
                  f"CLV {_fmt(summary['correction_only_clv'])}.",
                  f"Flags: {summary['cagey_review_rule']}; {summary['cagey_tier_review_rule']}.", '']
        for column, groups in summary['both_tiers_clv_by'].items():
            profit = summary['both_tiers_profit_by'].get(column, {})
            lines += [f'### By {column}', '', '| group | mean CLV (n) | realised profit per bet (n) |', '|---|---|---|']
            lines += [f'| {k} | {_fmt(v)} | {_fmt(profit.get(k, {}))} |' for k, v in groups.items()] or ['| none | n/a | n/a |']
            lines.append('')
    t = summary['tagged_candidates']
    lines += ['## Tagged candidates (narrow-margin hypothesis)', '',
              f"Frozen tagged candidates: {t['frozen']} ({t['with_offered_price']} with an offered price).",
              f"1xBet edge vs fair at capture: {_fmt(t['edge_at_capture_1xbet'])}.",
              f"Return at the capture fair price, all tagged lines: {_fmt(t['return_at_capture_fair'])}; "
              f"plus lines only: {_fmt(t['return_at_capture_fair_plus_lines'])}.", '']
    lines += [f"- {k}: {_fmt(v)}" for k, v in t['by_tag'].items()]
    if 'correction_monitoring' in summary:
        lines += [''] + monitoring_report(summary['correction_monitoring'])
    lines += ['', summary['note']]
    return '\n'.join(lines) + '\n'
