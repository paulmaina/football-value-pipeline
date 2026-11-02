"""Offline calibration check of the market-implied fair price (a check, not tuning).

Data: football-data.co.uk CSVs already in the cache, Pinnacle CLOSE prices:
1X2 (PSCH/PSCD/PSCA), O/U 2.5 (PC>2.5/PC<2.5) and the main AH (AHCh,
PCAHH/PCAHA). Per match two fits from market_implied: (A) 1X2 + O/U only and
(B) 1X2 + O/U + main AH. For each fit, bet 1 unit on every listed AH line,
both sides, at the matrix fair price and settle it. A correct fair price
returns zero on average; a positive mean return means the fit UNDERPRICES
that line: the side wins more often than its fair odds imply.

Nothing here is fitted to results or changes production. Many slices are
tested, so the report states how many intervals exclude zero against the
number expected by chance alone. Output:
football_output_v2/performance/market_implied_calibration/.
"""

from __future__ import annotations

import argparse
import json
import math
import warnings
from collections import Counter
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path
from typing import Dict, List, Optional, Sequence, Tuple

import numpy as np
import pandas as pd

import market_implied as mi
from ah_close_backtest import DIVISIONS, _json_default, _line, _price, _table, block_bootstrap, load_division, settle
from price_edge_backtest import CLOSE_OVERROUND_RANGE, available_seasons, week_block

PLUS_LINES = (0.5, 1.0, 1.25, 1.5, 1.75, 2.0, 2.25)
LINES = (*PLUS_LINES, *(-x for x in PLUS_LINES))
SPLIT_DATE = pd.Timestamp('2024-01-01')
PERIODS = ('all', 'to_2023', 'from_2024')
MIN_ROWS = 30  # Intervals on fewer bets are listed but not counted as tests.
OUTPUT_DIR = Path('football_output_v2') / 'performance' / 'market_implied_calibration'
COLUMNS_1X2 = ('PSCH', 'PSCD', 'PSCA')
COLUMNS_OU = ('PC>2.5', 'PC<2.5')
DROP_REASONS = ('missing_close_prices', 'close_overround')


# ---------------------------------------------------------------------------
# Per-match fits
# ---------------------------------------------------------------------------

def drop_reason(row) -> Optional[str]:
    prices = [_price(row.get(c)) for c in (*COLUMNS_1X2, *COLUMNS_OU, 'PCAHH', 'PCAHA')]
    if not all(prices) or _line(row.get('AHCh')) is None:
        return 'missing_close_prices'
    low, high = CLOSE_OVERROUND_RANGE
    groups = (prices[:3], prices[3:5], prices[5:])
    if not all(low <= sum(1 / p for p in g) <= high for g in groups):
        return 'close_overround'
    return None


def match_rows(row) -> List[Dict[str, object]]:
    """Fit A and B for one match; one row per fit, side and line priced at the matrix fair odds."""
    targets = mi.targets_from_prices(tuple(float(row[c]) for c in COLUMNS_1X2),
                                     tuple(float(row[c]) for c in COLUMNS_OU),
                                     (float(row['AHCh']), float(row['PCAHH']), float(row['PCAHA'])))
    fits = {kind: mi.fit(targets, include_ah=kind == 'B') for kind in ('A', 'B')}
    usable = all(f.usable for f in fits.values())
    margin = int(row['FTHG']) - int(row['FTAG'])
    base = {'match': f"{row['Division']}|{row['Date'].date()}|{row['HomeTeam']}", 'date': row['Date'], 'week': week_block(row['Date']), 'league': row['Division'],
            'season': row['Season'], 'period': 'to_2023' if row['Date'] < SPLIT_DATE else 'from_2024',
            'home_odds': float(row['PSCH']), 'away_odds': float(row['PSCA']),
            'p_home': targets['home'], 'p_draw': targets['draw'], 'p_away': targets['away'],
            'p_over_2_5': targets['over_2_5'], 'both_usable': usable,
            **{f'{k}_max_residual': f.max_residual for k, f in fits.items()},
            **{f'{k}_usable': f.usable for k, f in fits.items()},
            # Cagey-score calibration: market-implied P(2+ / 3+ goal margin) vs what happened.
            'abs_margin': abs(margin),
            **{f'{k}_cagey': mi.margin_at_least(f, 2) for k, f in fits.items() if f.usable},
            **{f'{k}_p3': mi.margin_at_least(f, 3) for k, f in fits.items() if f.usable}}
    rows = []
    if not usable:
        return [dict(base, fit=None)]
    for kind, result in fits.items():
        margins, probs = mi.margin_distribution(result.matrix)
        for side in ('home', 'away'):
            side_margin = margin if side == 'home' else -margin
            favourite = (targets['home'] > targets['away']) == (side == 'home')
            for line in LINES:
                q = mi.win_share(margins, probs, side, line)
                if not 0 < q < 1:
                    continue
                won, lost = settle(side_margin, line)
                rows.append(dict(base, fit=kind, side=side, line=line, win_share=q,
                                 side_role='favourite' if favourite else 'underdog',
                                 ret=float(won * (1 / q - 1) - lost)))
    return rows


def run_division(division: str, cache_dir: str) -> Tuple[List[Dict[str, object]], Dict[str, int], int]:
    warnings.filterwarnings('ignore')
    history = load_division(Path(cache_dir), division, available_seasons(Path(cache_dir), division))
    rows, drops = [], Counter()
    for _, row in history.iterrows():
        reason = drop_reason(row)
        if reason:
            drops[reason] += 1
            continue
        rows.extend(match_rows(row))
    return rows, dict(drops), len(history)


# ---------------------------------------------------------------------------
# Slices
# ---------------------------------------------------------------------------

def _between(series, low, high):
    return (series >= low) & (series <= high)


def slices(frame: pd.DataFrame) -> Dict[str, pd.Series]:
    """Named boolean masks; tag-like slices use Pinnacle close prices."""
    balanced = _between(frame.home_odds, 2.0, 3.5) & _between(frame.away_odds, 2.0, 3.5)
    tight = _between(frame.home_odds, 2.0, 2.8) & _between(frame.away_odds, 2.0, 2.8)
    totals = {'total<45%': frame.p_over_2_5 < 0.45,
              'total 45-55%': (frame.p_over_2_5 >= 0.45) & (frame.p_over_2_5 <= 0.55),
              'total>55%': frame.p_over_2_5 > 0.55}
    draws = {'draw<24%': frame.p_draw < 0.24, 'draw 24-27%': (frame.p_draw >= 0.24) & (frame.p_draw < 0.27),
             'draw 27-30%': (frame.p_draw >= 0.27) & (frame.p_draw < 0.30), 'draw>=30%': frame.p_draw >= 0.30}
    out = {'all': pd.Series(True, index=frame.index), 'balanced [2.00,3.50]': balanced,
           'balanced [2.00,2.80]': tight, **totals, **draws}
    out.update({f'balanced x {k}': balanced & m for k, m in totals.items()})
    out.update({f'draw>=27% x {k}': (frame.p_draw >= 0.27) & m for k, m in totals.items()})
    out.update({'favourite side': frame.side_role == 'favourite', 'underdog side': frame.side_role == 'underdog',
                'home side': frame.side == 'home', 'away side': frame.side == 'away'})
    out.update({f'league {d}': frame.league == d for d in sorted(frame.league.unique())})
    return out


def evaluate(frame: pd.DataFrame, n_boot: int) -> pd.DataFrame:
    """Mean return with a gameweek-block 95% interval per fit x slice x period x line."""
    records = []
    masks = slices(frame)
    for name, mask in masks.items():
        for period in PERIODS:
            subset = frame[mask if period == 'all' else mask & (frame.period == period)]
            for (kind, line), group in subset.groupby(['fit', 'line']):
                mean, low, high = block_bootstrap(group.ret, group.week, n_boot)
                records.append({'fit': kind, 'slice': name, 'period': period, 'line': line,
                                'bets': len(group), 'matches': group.match.nunique(),
                                'mean_return': mean, 'low95': low, 'high95': high,
                                'tested': len(group) >= MIN_ROWS,
                                'excludes_zero': len(group) >= MIN_ROWS and (low > 0 or high < 0)})
    return pd.DataFrame(records)


CAGEY_QUINTILES = ('Q1 cagiest', 'Q2', 'Q3', 'Q4', 'Q5 most open')


def cagey_calibration(matches: pd.DataFrame, n_boot: int) -> List[Dict[str, object]]:
    """Actual vs predicted 2+ and 3+ goal-margin rates by cagey-score quintile, per fit and season half.

    Quintiles are cut on each fit's own score over all usable matches. Intervals
    resample whole gameweeks; `gap` is actual minus predicted per match.
    """
    records = []
    usable = matches[matches.both_usable.astype(bool)].copy()
    for kind in ('A', 'B'):
        if f'{kind}_cagey' not in usable or usable.empty:
            continue
        scores = usable[f'{kind}_cagey'].astype(float)
        quintile = pd.qcut(scores.rank(method='first'), len(CAGEY_QUINTILES), labels=CAGEY_QUINTILES)
        for label in CAGEY_QUINTILES:
            for period in PERIODS:
                part = usable[(quintile == label) & ((usable.period == period) if period != 'all' else True)]
                if part.empty:
                    continue
                record = {'fit': kind, 'quintile': label, 'period': period, 'matches': int(len(part)),
                          'score_low': float(part[f'{kind}_cagey'].min()), 'score_high': float(part[f'{kind}_cagey'].max())}
                for goals, predicted in ((2, f'{kind}_cagey'), (3, f'{kind}_p3')):
                    actual = (part.abs_margin >= goals).astype(float)
                    rate, low, high = block_bootstrap(actual, part.week, n_boot)
                    gap, gap_low, gap_high = block_bootstrap(actual - part[predicted].astype(float), part.week, n_boot)
                    record.update({f'actual_{goals}plus': rate, f'actual_{goals}plus_low95': low,
                                   f'actual_{goals}plus_high95': high,
                                   f'predicted_{goals}plus': float(part[predicted].mean()), f'gap_{goals}plus': gap,
                                   f'gap_{goals}plus_low95': gap_low, f'gap_{goals}plus_high95': gap_high})
                records.append(record)
    return records


def cagey_section(records: List[Dict[str, object]]) -> List[str]:
    lines = ['## Cagey score: actual vs predicted big margins', '',
             'cagey_score = market-implied P(2+ goal margin, either side); lower = cagier. Quintiles are cut on each '
             "fit's score over all usable matches."
             ' gap = actual - predicted rate, gameweek-block 95% interval; '
             '`*` = interval excludes zero. Tracking only: the score never changes a v27 decision.', '']
    rows = []
    for r in records:
        cells = [r['fit'], r['quintile'], r['period'], r['matches'], f"{r['score_low']:.3f}-{r['score_high']:.3f}"]
        for goals in (2, 3):
            star = ' *' if r[f'gap_{goals}plus_low95'] > 0 or r[f'gap_{goals}plus_high95'] < 0 else ''
            cells += [f"{r[f'actual_{goals}plus']:.3f} [{r[f'actual_{goals}plus_low95']:.3f}, {r[f'actual_{goals}plus_high95']:.3f}]",
                      f"{r[f'predicted_{goals}plus']:.3f}",
                      f"{r[f'gap_{goals}plus']:+.3f} [{r[f'gap_{goals}plus_low95']:+.3f}, {r[f'gap_{goals}plus_high95']:+.3f}]{star}"]
        rows.append(cells)
    lines.append(_table(['fit', 'quintile', 'period', 'matches', 'score range', 'actual 2+ [95%]', 'predicted 2+',
                         'gap 2+ [95%]', 'actual 3+ [95%]', 'predicted 3+', 'gap 3+ [95%]'], rows))
    return lines + ['']


# ---------------------------------------------------------------------------
# Report
# ---------------------------------------------------------------------------

def persistent(results: pd.DataFrame, kind: str) -> pd.DataFrame:
    """Plus-line underpricing (interval above zero) in BOTH season halves."""
    plus = results[(results.fit == kind) & (results.line > 0) & results.tested]
    halves = plus[plus.period != 'all'].pivot_table(index=['slice', 'line'], columns='period',
                                                     values='low95', aggfunc='first')
    if not {'to_2023', 'from_2024'} <= set(halves.columns):
        return pd.DataFrame(columns=['slice', 'line', 'to_2023_low95', 'from_2024_low95'])
    both = halves[(halves.to_2023 > 0) & (halves.from_2024 > 0)].reset_index()
    return both.rename(columns={'to_2023': 'to_2023_low95', 'from_2024': 'from_2024_low95'})


def headline(results: pd.DataFrame) -> Dict[str, object]:
    tested = results[results.tested]
    counts = {kind: {'tested': int((tested.fit == kind).sum()),
                     'exclude_zero': int(tested[tested.fit == kind].excludes_zero.sum()),
                     'expected_by_chance': round(0.05 * int((tested.fit == kind).sum()), 1),
                     'plus_line_above_zero': int(((tested.fit == kind) & (tested.line > 0) & (tested.low95 > 0)).sum()),
                     'minus_line_below_zero': int(((tested.fit == kind) & (tested.line < 0) & (tested.high95 < 0)).sum())}
              for kind in ('A', 'B')}
    key = tested[(tested.period == 'all') & (tested.line > 0)]

    def plus_mean(kind, name):
        part = key[(key.fit == kind) & (key.slice == name)]
        return float(np.average(part.mean_return, weights=part.bets)) if len(part) else float('nan')
    focus = ('all', 'balanced [2.00,3.50]', 'total<45%', 'balanced x total<45%', 'draw>=27% x total<45%',
             'draw 27-30%', 'draw>=30%')
    return {'counts': counts,
            'plus_line_mean_return': {name: {'A': plus_mean('A', name), 'B': plus_mean('B', name)} for name in focus},
            'persistent_both_halves': {kind: persistent(results, kind).to_dict('records') for kind in ('A', 'B')}}


def verdict(head: Dict[str, object]) -> List[str]:
    lines = []
    for kind in ('A', 'B'):
        c = head['counts'][kind]
        lines.append(f"- Fit {kind}: {c['tested']} slice x period x line intervals tested; {c['exclude_zero']} exclude "
                     f"zero vs about {c['expected_by_chance']} expected by chance alone (5%). Plus lines with the "
                     f"interval above zero: {c['plus_line_above_zero']}; minus lines below zero: {c['minus_line_below_zero']}.")
    lines += ['', 'Slices overlap (all, halves, nested lines, both sides of a match), so these tests are strongly '
              'correlated; the 5% chance figure assumes independent tests and is only a rough yardstick.',
              'Both fits reproduce the 1X2 exactly, so returns on the +/-0.5 lines measure bias in Pinnacle\'s '
              'proportional margin-free close, not fit error; the wider lines add the matrix\'s own tail error.',
              'A positive plus-line return means the matrix fair odds are too long there, which UNDERSTATES a '
              'derived edge; a negative minus-line return means it OVERSTATES one. That is why the v27 derived '
              'reference is limited to plus lines.',
              '', 'Bet-weighted mean return on plus lines (+0.5 to +2.25), all seasons:', '',
              _table(['slice', 'fit A', 'fit B'], [[k, v['A'], v['B']] for k, v in head['plus_line_mean_return'].items()]), '']
    a, b = head['counts']['A'], head['counts']['B']
    removed = b['plus_line_above_zero'] < a['plus_line_above_zero']
    lines.append(f"Does fit B remove the plus-line underpricing seen in fit A? "
                 f"{'It reduces it' if removed else 'No'}: plus-line intervals above zero go from "
                 f"{a['plus_line_above_zero']} (A) to {b['plus_line_above_zero']} (B).")
    both = head['persistent_both_halves']['B']
    if both:
        lines.append('Fit B slices where plus-line underpricing remains in BOTH season halves (lower 95% bound > 0 '
                     'in each): ' + '; '.join(f"{r['slice']} {r['line']:+g}" for r in both) + '.')
    else:
        lines.append('Fit B: no slice shows plus-line underpricing in BOTH season halves.')
    if head['persistent_both_halves']['A']:
        lines.append(f"(Fit A: {len(head['persistent_both_halves']['A'])} slice/line pairs persist in both halves.)")
    lines += ['', 'These are hypotheses to track forward, not rules. No correction is fitted or applied here.']
    return lines


def write_report(summary: Dict[str, object], results: pd.DataFrame, path: Path) -> None:
    parts = ['# Market-implied fair price: calibration check', '',
             'Read-only check, not tuning. Pinnacle CLOSE prices; fit A = 1X2 + O/U 2.5, fit B = 1X2 + O/U 2.5 + '
             'main AH. Each line is bet at the matrix fair price on matches where both fits are usable; a correct '
             'price returns zero on average. 95% intervals resample whole gameweeks (Tuesday start), so every '
             f"row of a match shares a block. Intervals on fewer than {MIN_ROWS} bets are shown but not counted.", '',
             '## Headline', '']
    parts += verdict(summary['headline'])
    cov = summary['coverage']
    parts += ['', '## Data', '',
              _table(['matches', *DROP_REASONS, 'fit A unusable', 'fit B unusable', 'both usable'],
                     [[cov['matches'], *[cov['dropped'].get(k, 0) for k in DROP_REASONS], cov['fit_a_unusable'],
                       cov['fit_b_unusable'], cov['both_usable']]]),
              '', f"Seasons: {', '.join(summary['seasons'])}. Leagues: {', '.join(summary['divisions'])}. "
              f"Season split: before vs from {SPLIT_DATE.date()}.", '',
              f"Fit B residuals (pp, usable fits): median {summary['fit_b_residual_pp']['median']:.2f}, "
              f"95th percentile {summary['fit_b_residual_pp']['p95']:.2f}.", '']
    parts += cagey_section(summary.get('cagey_calibration', []))
    for name in results.slice.unique():
        part = results[results.slice == name]
        parts += [f'## {name}', '',
                  _table(['line', 'period', 'A bets', 'A mean [95%]', 'B bets', 'B mean [95%]'],
                         [[f'{line:+g}', period, *sum(([int(r.bets), f'{r.mean_return:+.4f} [{r.low95:+.4f}, {r.high95:+.4f}]'
                                                         + (' *' if r.excludes_zero else '')]
                                                        for r in [g[g.fit == k].iloc[0] for k in ('A', 'B') if (g.fit == k).any()]), [])]
                          for (line, period), g in part.groupby(['line', 'period'], sort=False)]), '']
    parts.append('`*` = 95% interval excludes zero (tested slices only).')
    path.write_text('\n'.join(parts) + '\n', encoding='utf-8')


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('--cache-dir', default='.football_cache')
    parser.add_argument('--output-dir', default=str(OUTPUT_DIR))
    parser.add_argument('--divisions', nargs='+', default=list(DIVISIONS))
    parser.add_argument('--workers', type=int, default=len(DIVISIONS))
    parser.add_argument('--bootstrap', type=int, default=2000)
    args = parser.parse_args(argv)
    warnings.filterwarnings('ignore')
    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    with ProcessPoolExecutor(max_workers=max(1, args.workers)) as pool:
        parts = list(pool.map(run_division, args.divisions, [args.cache_dir] * len(args.divisions)))
    rows = [r for p in parts for r in p[0]]
    drops = Counter()
    for p in parts:
        drops.update(p[1])
    matches = pd.DataFrame([r for r in rows if r['fit'] is None or (r['fit'] == 'A' and r['side'] == 'home'
                                                                      and r['line'] == LINES[0])])
    frame = pd.DataFrame([r for r in rows if r['fit'] is not None])
    results = evaluate(frame, args.bootstrap)
    usable_b = frame[frame.fit == 'B'].drop_duplicates('match')
    summary = {'version': mi.VERSION, 'max_residual': mi.MAX_RESIDUAL, 'lines': list(LINES),
               'divisions': list(args.divisions), 'seasons': sorted(frame.season.unique()),
               'coverage': {'matches': int(sum(p[2] for p in parts)), 'dropped': dict(drops),
                            'fit_a_unusable': int((~matches.A_usable).sum()),
                            'fit_b_unusable': int((~matches.B_usable).sum()),
                            'both_usable': int(matches.both_usable.sum())},
               'fit_b_residual_pp': {'median': float(usable_b.B_max_residual.median() * 100),
                                     'p95': float(usable_b.B_max_residual.quantile(0.95) * 100)},
               'headline': headline(results),
               'cagey_calibration': cagey_calibration(matches, args.bootstrap),
               'results': results.to_dict('records')}
    (out_dir / 'summary.json').write_text(json.dumps(summary, indent=2, default=_json_default), encoding='utf-8')
    write_report(summary, results, out_dir / 'report.md')
    print('\n'.join(verdict(summary['headline'])))
    print(f'Wrote {out_dir}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
