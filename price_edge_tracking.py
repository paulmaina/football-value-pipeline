"""Forward tracking for production policy v27 (AH price edge vs Pinnacle).

1. Grades every frozen v27 pick by closing line value against Pinnacle's
   near-kickoff price on the same AH line (the closing-odds workflow already
   collects it): clv = entry odds x Pinnacle fair close win-share - 1, with
   the two-way margin removed proportionally, as in the selection rule.
   Splits: bookmaker, odds band, reference type, favourite/underdog side and
   each narrow-margin tag (balanced, low_total, high_draw, any tag, no tag).
2. Records every TAGGED candidate, picked or rejected, with the offered price
   vs fair at capture and the final result, so the narrow-margin hypothesis
   is measured forward even when no pick is made.

A STOP REVIEW flag is raised when at least 100 graded picks have mean CLV
below zero. v26 and older history is untouched. Evidence only: nothing here
changes forecasts, selection or stakes.
"""
from __future__ import annotations

import math
from datetime import timedelta
from pathlib import Path
from typing import Dict, List, Optional

import numpy as np
import pandas as pd

from price_edge_shortlist import POLICY, TAGS

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
SPLITS = ('bookmaker', 'odds_band', 'reference_type', 'side_role', 'balanced', 'low_total', 'high_draw', 'tagged',
          'cagey_quintile')
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


def split_table(frame: pd.DataFrame, value: str) -> Dict[str, Dict[str, dict]]:
    out = {}
    for column in SPLITS:
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
    picks = [r for r in frozen_rows(archive, 'shortlist', latest=True) if r.get('selection_policy_version') == POLICY]
    graded = grade(picks, observations, records, clock)
    tagged = grade(frozen_candidates(root, archive), observations, records, clock)
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
        'tagged_candidates': {
            'frozen': int(len(tagged)),
            'with_offered_price': int(tagged['offered_decimal_odds'].notna().sum()) if len(tagged) else 0,
            'edge_at_capture_1xbet': summarize(tagged.loc[tagged.bookmaker.eq('1xBet'), 'edge'] if len(tagged) else []),
            'return_at_capture_fair': summarize(tagged['return_at_capture_fair'] if len(tagged) else []),
            'return_at_capture_fair_plus_lines': summarize(
                tagged.loc[tagged.ah_line.astype(float) > 0, 'return_at_capture_fair'] if len(tagged) else []),
            'by_tag': {t: summarize(tagged.loc[tagged[t].eq('yes'), 'return_at_capture_fair'] if len(tagged) else [])
                       for t in TAGS}},
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
    (dest / 'report.md').write_text(report(summary), encoding='utf-8')
    return summary


def _fmt(m: dict) -> str:
    if not m.get('n'):
        return 'n/a (0)'
    se = f" ± {1.96 * m['standard_error']:.2%}" if m.get('standard_error') else ''
    return f"{m['mean']:+.2%}{se} (n={m['n']})"


def report(summary: dict) -> str:
    lines = ['# v27 price-edge tracking', '']
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
    t = summary['tagged_candidates']
    lines += ['## Tagged candidates (narrow-margin hypothesis)', '',
              f"Frozen tagged candidates: {t['frozen']} ({t['with_offered_price']} with an offered price).",
              f"1xBet edge vs fair at capture: {_fmt(t['edge_at_capture_1xbet'])}.",
              f"Return at the capture fair price, all tagged lines: {_fmt(t['return_at_capture_fair'])}; "
              f"plus lines only: {_fmt(t['return_at_capture_fair_plus_lines'])}.", '']
    lines += [f"- {k}: {_fmt(v)}" for k, v in t['by_tag'].items()]
    lines += ['', summary['note']]
    return '\n'.join(lines) + '\n'
