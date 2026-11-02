"""Read-only backtest of a pre-registered Asian handicap price-edge rule.

Rule (pre-registered, not tuned here): on the football-data.co.uk opening main
line (AHh), Pinnacle's opening pair PAHH/PAHA with the margin removed
(proportional; Shin as a check) is the fair probability of each side. Bet
1 unit on a side when offered_odds x fair_p - 1 >= 2%, at most one side per
match, settled at the offered odds on AHh.

Offered prices are reported per source: MaxAHH/A (best across books), B365AHH/A,
BFEAHH/A (net of exchange commission) and AvgAHH/A (control). The primary
metric is closing line value against Pinnacle's fair close, on matches whose
closing line equals the opening line.

Nothing here changes production models, policy, thresholds or workflows.
Output goes to football_output_v2/performance/price_edge_backtest/.
"""

from __future__ import annotations

import argparse
import json
import math
import warnings
from collections import Counter
from pathlib import Path
from typing import Dict, List, Optional, Sequence, Tuple

import numpy as np
import pandas as pd

from ah_close_backtest import (DIVISIONS, _json_default, _line, _price, _table, block_bootstrap,
                               devig_proportional, devig_shin, line_type, load_division, realised_return)

SOURCES = {
    'max': ('MaxAHH', 'MaxAHA', 'best price across bookmakers (which bookmaker is not recorded)'),
    'b365': ('B365AHH', 'B365AHA', 'Bet365'),
    'bfe': ('BFEAHH', 'BFEAHA', 'Betfair Exchange, odds net of commission'),
    'avg': ('AvgAHH', 'AvgAHA', 'market average (control: should not show an edge)'),
}
COMMISSION_SOURCES = ('bfe',)
BFE_COMMISSION = 0.05
EDGE_THRESHOLD = 0.02
SENSITIVITY_THRESHOLDS = (0.0, 0.01, 0.03)
EDGE_TOLERANCE = 1e-9  # floating-point slack only: an edge of exactly 2.0% bets.
MIN_OFFERED_OVERROUND = 0.98
MAX_PINNACLE_RATIO = 1.15
CLOSE_OVERROUND_RANGE = (1.00, 1.10)
DROP_REASONS = ('no_pinnacle_open', 'no_pinnacle_close', 'pinnacle_close_overround',
                'no_offered_price', 'offered_overround', 'offered_above_pinnacle_cap')
ODDS_BANDS = ((1.0, 1.70, '<1.70'), (1.70, 1.90, '1.70-1.90'), (1.90, 2.10, '1.90-2.10'),
              (2.10, 2.40, '2.10-2.40'), (2.40, math.inf, '>=2.40'))
BREAKDOWNS = ('season', 'league', 'line_type', 'odds_band', 'side_role')
RECENT_SEASON = '2526'
MIN_READABLE_BETS = 30  # same-line bets below which an interval is reported but not called.
WEEK_START = 1  # Tuesday, as the close backtest's gameweek blocks.
OUTPUT_DIR = Path('football_output_v2') / 'performance' / 'price_edge_backtest'


# ---------------------------------------------------------------------------
# Rule
# ---------------------------------------------------------------------------

def net_odds(odds: float, commission: float) -> float:
    """Decimal odds after commission on net winnings."""
    return 1 + (odds - 1) * (1 - commission)


def drop_reason(row, source: str) -> Optional[str]:
    """First data-quality filter a row fails for `source`, or None when usable."""
    home_col, away_col, _ = SOURCES[source]
    pin_home, pin_away = _price(row.get('PAHH')), _price(row.get('PAHA'))
    if _line(row.get('AHh')) is None or not (pin_home and pin_away):
        return 'no_pinnacle_open'
    close_home, close_away = _price(row.get('PCAHH')), _price(row.get('PCAHA'))
    if _line(row.get('AHCh')) is None or not (close_home and close_away):
        return 'no_pinnacle_close'
    low, high = CLOSE_OVERROUND_RANGE
    if not low <= 1 / close_home + 1 / close_away <= high:
        return 'pinnacle_close_overround'
    home, away = _price(row.get(home_col)), _price(row.get(away_col))
    if not (home and away):
        return 'no_offered_price'
    if 1 / home + 1 / away < MIN_OFFERED_OVERROUND:
        return 'offered_overround'
    # A pair with either side far above Pinnacle is treated as a bad quote, not a price.
    if home > MAX_PINNACLE_RATIO * pin_home or away > MAX_PINNACLE_RATIO * pin_away:
        return 'offered_above_pinnacle_cap'
    return None


def week_block(date: pd.Timestamp) -> str:
    start = date.normalize() - pd.Timedelta(days=(date.weekday() - WEEK_START) % 7)
    return start.date().isoformat()


def candidate(row, source: str, commission: float = BFE_COMMISSION) -> Dict[str, object]:
    """Both sides of one screened match: offered odds, edge vs Pinnacle open, CLV, settled profit."""
    home_col, away_col, _ = SOURCES[source]
    rate = commission if source in COMMISSION_SOURCES else 0.0
    line, close_line = float(row['AHh']), float(row['AHCh'])
    margin = int(row['FTHG']) - int(row['FTAG'])
    same_line = line == close_line
    record = {'source': source, 'date': row['Date'].date().isoformat(), 'week': week_block(row['Date']),
              'league': row['Division'], 'season': row['Season'], 'home_team': row['HomeTeam'],
              'away_team': row['AwayTeam'], 'home_goals': int(row['FTHG']), 'away_goals': int(row['FTAG']),
              'line': line, 'close_line': close_line, 'same_line': same_line, 'line_type': line_type(line)}
    fair = {}
    for suffix, devig in (('', devig_proportional), ('_shin', devig_shin)):
        open_home = devig(float(row['PAHH']), float(row['PAHA']))[0]
        close_home = devig(float(row['PCAHH']), float(row['PCAHA']))[0]
        fair[suffix] = {'home': (open_home, close_home), 'away': (1 - open_home, 1 - close_home)}
    for side, sign, column in (('home', 1, home_col), ('away', -1, away_col)):
        quoted = float(row[column])
        odds = net_odds(quoted, rate)
        record[f'{side}_quoted'] = quoted
        record[f'{side}_odds'] = odds
        record[f'{side}_line'] = sign * line
        record[f'{side}_profit'] = realised_return(sign * margin, sign * line, odds)
        for suffix, sides in fair.items():
            open_p, close_p = sides[side]
            record[f'{side}_fair_open{suffix}'] = open_p
            record[f'{side}_edge{suffix}'] = odds * open_p - 1
            record[f'{side}_clv{suffix}'] = odds * close_p - 1 if same_line else float('nan')
    return record


def build_candidates(history: pd.DataFrame, source: str,
                     commission: float = BFE_COMMISSION) -> Tuple[pd.DataFrame, Counter]:
    records, drops = [], Counter()
    for _, row in history.iterrows():
        reason = drop_reason(row, source)
        if reason:
            drops[reason] += 1
        else:
            records.append(candidate(row, source, commission))
    return pd.DataFrame(records), drops


def odds_band(odds: float) -> str:
    return next(label for low, high, label in ODDS_BANDS if low <= odds < high)


def select_bets(candidates: pd.DataFrame, threshold: float = EDGE_THRESHOLD, devig: str = '') -> pd.DataFrame:
    """Bet the side whose edge clears `threshold`; when both do, the larger (home on a tie)."""
    if candidates.empty:
        return pd.DataFrame()
    edge_home, edge_away = candidates[f'home_edge{devig}'], candidates[f'away_edge{devig}']
    limit = threshold - EDGE_TOLERANCE
    home = (edge_home >= limit) & (edge_home >= edge_away)
    away = (edge_away >= limit) & ~home
    parts = []
    for side, mask in (('home', home), ('away', away)):
        part = candidates[mask]
        parts.append(pd.DataFrame({
            **{c: part[c] for c in ('date', 'week', 'league', 'season', 'home_team', 'away_team',
                                    'home_goals', 'away_goals', 'line', 'close_line', 'same_line', 'line_type')},
            'side': side, 'side_line': part[f'{side}_line'], 'quoted_odds': part[f'{side}_quoted'],
            'odds': part[f'{side}_odds'], 'fair_open_p': part[f'{side}_fair_open{devig}'],
            'edge': part[f'{side}_edge{devig}'], 'clv': part[f'{side}_clv{devig}'],
            'profit': part[f'{side}_profit']}))
    bets = pd.concat(parts).sort_index(kind='stable').reset_index(drop=True)
    bets['odds_band'] = bets['odds'].map(odds_band)
    bets['side_role'] = np.where(bets['side_line'] < 0, 'favourite',
                                 np.where(bets['side_line'] > 0, 'underdog', 'level'))
    return bets


# ---------------------------------------------------------------------------
# Metrics
# ---------------------------------------------------------------------------

def max_drawdown(profits) -> float:
    """Largest peak-to-trough fall in cumulative units, counting the start as a peak."""
    path = np.concatenate([[0.0], np.cumsum(np.asarray(profits, dtype=float))])
    return float((np.maximum.accumulate(path) - path).max())


def longest_losing_run(profits) -> int:
    """Most consecutive bets with a negative result; a push or win ends the run."""
    best = run = 0
    for profit in profits:
        run = run + 1 if profit < 0 else 0
        best = max(best, run)
    return best


def rule_metrics(bets: pd.DataFrame, n_boot: int) -> Dict[str, object]:
    out = {'bets': int(len(bets))}
    if bets.empty:
        return out
    ordered = bets.sort_values(['date', 'league', 'home_team'], kind='stable')
    same = bets[bets['same_line']]
    roi, roi_low, roi_high = block_bootstrap(bets['profit'], bets['week'], n_boot)
    out.update({'mean_edge': float(bets['edge'].mean()), 'mean_odds': float(bets['odds'].mean()),
                'roi': roi, 'roi_low95': roi_low, 'roi_high95': roi_high,
                'profit_units': float(bets['profit'].sum()),
                'max_drawdown_units': max_drawdown(ordered['profit']),
                'longest_losing_run': longest_losing_run(ordered['profit']),
                'same_line_bets': int(len(same))})
    if len(same):
        clv, clv_low, clv_high = block_bootstrap(same['clv'], same['week'], n_boot)
        out.update({'mean_clv': clv, 'clv_low95': clv_low, 'clv_high95': clv_high,
                    'share_clv_positive': float((same['clv'] > 0).mean())})
    return out


def evaluate(candidates: Dict[str, pd.DataFrame], n_boot: int = 2000) -> Dict[str, object]:
    summary = {'rule': {'edge_threshold': EDGE_THRESHOLD, 'line': 'opening AHh',
                        'fair_probability': 'Pinnacle opening PAHH/PAHA, proportional margin removal',
                        'clv': 'odds x Pinnacle fair close probability - 1, only where AHCh == AHh'},
               'sources': {}}
    for source, frame in candidates.items():
        bets = select_bets(frame)
        result = {'description': SOURCES[source][2], 'usable_matches': int(len(frame)),
                  'rule': rule_metrics(bets, n_boot),
                  'shin_check': rule_metrics(select_bets(frame, devig='_shin'), n_boot),
                  'sensitivity': {f'{t:.0%}': rule_metrics(select_bets(frame, t), n_boot)
                                  for t in SENSITIVITY_THRESHOLDS},
                  'recent_season': rule_metrics(bets[bets['season'] == RECENT_SEASON] if len(bets) else bets, n_boot),
                  'breakdowns': {}}
        if len(bets):
            result['breakdowns'] = {name: {str(k): rule_metrics(g, n_boot) for k, g in bets.groupby(name)}
                                    for name in BREAKDOWNS}
        summary['sources'][source] = result
    return summary


# ---------------------------------------------------------------------------
# Report
# ---------------------------------------------------------------------------

def _ci(m: Dict[str, object], key: str, bounds: str) -> str:
    if key not in m:
        return 'n/a'
    return f"{m[key]:+.4f} [{m[bounds + '_low95']:+.4f}, {m[bounds + '_high95']:+.4f}]"


def _readable(m: Dict[str, object]) -> bool:
    return m.get('same_line_bets', 0) >= MIN_READABLE_BETS


def _call(m: Dict[str, object]) -> str:
    if 'mean_clv' not in m:
        return 'no same-line bets'
    if not _readable(m):
        return f'too few same-line bets to read (< {MIN_READABLE_BETS})'
    if m['clv_low95'] > 0:
        return 'positive CLV, interval above zero'
    return 'negative CLV, interval below zero' if m['clv_high95'] < 0 else 'interval includes zero'


def _metric_row(label, m: Dict[str, object]) -> List[object]:
    return [label, m['bets'], m.get('same_line_bets', 0), _ci(m, 'mean_clv', 'clv'),
            m.get('share_clv_positive', float('nan')), _ci(m, 'roi', 'roi'),
            m.get('max_drawdown_units', float('nan')), m.get('longest_losing_run', 0)]


METRIC_HEADERS = ['', 'bets', 'same-line bets', 'mean CLV [95%]', 'CLV > 0', 'ROI [95%]',
                  'max drawdown (u)', 'longest losing run']


def verdict(summary: Dict[str, object]) -> List[str]:
    sources = summary['sources']
    lines = []
    for s, r in sources.items():
        lines.append(f"- **{s}** ({r['description']}): {_ci(r['rule'], 'mean_clv', 'clv')} over "
                     f"{r['rule'].get('same_line_bets', 0)} same-line bets -> {_call(r['rule'])}.")
        if _readable(r['rule']):
            lines.append(f"  - Shin check {_ci(r['shin_check'], 'mean_clv', 'clv')} -> {_call(r['shin_check'])}; "
                         f"{RECENT_SEASON[:2]}/{RECENT_SEASON[2:]} only {_ci(r['recent_season'], 'mean_clv', 'clv')} "
                         f"over {r['recent_season'].get('same_line_bets', 0)} -> {_call(r['recent_season'])}.")
    positive = [s for s, r in sources.items()
                if s != 'avg' and _readable(r['rule']) and r['rule']['clv_low95'] > 0]
    lines += ['', 'Does the pre-registered rule show positive CLV with a 95% interval above zero? '
              + (f"Yes for: {', '.join(positive)}." if positive else 'No, for none of the offered-price sources.')]
    control = sources.get('avg', {}).get('rule', {})
    if not _readable(control):
        lines.append(f"The market-average control almost never clears the edge ({control.get('bets', 0)} bets), "
                     'as expected; there are too few bets to test its CLV.')
    elif control['clv_low95'] > 0:
        lines.append('WARNING: the market-average control also shows an interval above zero, which points '
                     'to a data or method problem rather than a usable edge.')
    elif control:
        lines.append(f"The market-average control does not show an edge ({_call(control)}), as expected.")
    lines += ['', 'History cannot show WHICH bookmaker offered the max price, or whether it would have '
              'accepted the stake, so the max-price result is an upper bound. Live tracking of quotes '
              'that can actually be taken is the real test. This backtest is not a recommendation to '
              'change production.']
    return lines


def write_report(summary: Dict[str, object], path: Path) -> None:
    sources = summary['sources']
    parts = ['# Asian handicap price-edge backtest (pre-registered rule)', '',
             'Read-only. No production model, policy, threshold or workflow was changed.', '',
             f"Rule: on the opening line AHh, bet a side when offered odds x Pinnacle opening fair probability "
             f"(proportional margin removal) - 1 >= {EDGE_THRESHOLD:.0%}, at most one side per match, 1 unit "
             f"flat at the offered odds. Betfair Exchange odds are net of {summary['commission']:.0%} commission. "
             f"CLV = odds x Pinnacle fair closing probability - 1, only where the closing line equals the "
             f"opening line. 95% intervals resample whole gameweeks.", '', '## Verdict', '']
    parts += verdict(summary)
    parts += ['', f'## Pre-registered rule ({EDGE_THRESHOLD:.0%}), all seasons', '',
              _table(['source'] + METRIC_HEADERS[1:] + ['mean edge', 'mean odds'],
                     [_metric_row(s, r['rule']) + [r['rule'].get('mean_edge', float('nan')),
                                                   r['rule'].get('mean_odds', float('nan'))]
                      for s, r in sources.items()]),
              '', '### Check: Shin margin removal (selection and close)', '',
              _table(['source'] + METRIC_HEADERS[1:], [_metric_row(s, r['shin_check']) for s, r in sources.items()]),
              '', f'## Most recent period: {RECENT_SEASON[:2]}/{RECENT_SEASON[2:]} only', '',
              _table(['source'] + METRIC_HEADERS[1:], [_metric_row(s, r['recent_season']) for s, r in sources.items()]),
              '', '## Data quality: matches dropped per source', '',
              'Each match counts once, under the first filter it fails (in column order).', '',
              _table(['source', 'matches'] + list(DROP_REASONS) + ['usable'],
                     [[s, c['matches']] + [c['dropped'].get(k, 0) for k in DROP_REASONS] + [c['usable']]
                      for s, c in summary['coverage'].items()])]
    parts += ['', '## SENSITIVITY ONLY - not the rule', '',
              'Other thresholds, shown only to see whether the result depends on the 2% cut. '
              'They were not used to choose the rule.', '']
    parts.append(_table(['source / threshold'] + METRIC_HEADERS[1:],
                        [_metric_row(f'{s} {t}', m) for s, r in sources.items() for t, m in r['sensitivity'].items()]))
    for s, r in sources.items():
        parts += ['', f'## Breakdowns at {EDGE_THRESHOLD:.0%}: {s}', '']
        for name, table in r['breakdowns'].items():
            parts += [f'**{name}**', '', _table([name] + METRIC_HEADERS[1:],
                                                [_metric_row(k, m) for k, m in table.items()]), '']
    path.write_text('\n'.join(parts) + '\n', encoding='utf-8')


def available_seasons(cache_dir: Path, division: str) -> List[str]:
    return sorted(p.name.split('_')[0] for p in Path(cache_dir).glob(f'[0-9][0-9][0-9][0-9]_{division}.csv'))


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('--cache-dir', default='.football_cache')
    parser.add_argument('--output-dir', default=str(OUTPUT_DIR))
    parser.add_argument('--divisions', nargs='+', default=list(DIVISIONS))
    parser.add_argument('--commission', type=float, default=BFE_COMMISSION)
    parser.add_argument('--bootstrap', type=int, default=2000)
    args = parser.parse_args(argv)
    warnings.filterwarnings('ignore')
    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    history = pd.concat([load_division(Path(args.cache_dir), d, available_seasons(Path(args.cache_dir), d))
                         for d in args.divisions], ignore_index=True, sort=False)
    history = history.sort_values(['Date', 'Division', 'HomeTeam'], kind='stable').reset_index(drop=True)
    candidates, coverage = {}, {}
    for source in SOURCES:
        frame, drops = build_candidates(history, source, args.commission)
        candidates[source] = frame
        coverage[source] = {'matches': int(len(history)), 'dropped': dict(drops), 'usable': int(len(frame))}

    summary = evaluate(candidates, args.bootstrap)
    summary['commission'] = args.commission
    summary['coverage'] = coverage
    summary['seasons'] = sorted(history['Season'].unique())
    summary['usable_by_source_season'] = {s: f.groupby('season').size().to_dict() if len(f) else {}
                                          for s, f in candidates.items()}
    bets = pd.concat([select_bets(f).assign(source=s) for s, f in candidates.items() if len(f)], ignore_index=True)
    bets.to_csv(out_dir / 'bets.csv', index=False)
    (out_dir / 'summary.json').write_text(json.dumps(summary, indent=2, default=_json_default), encoding='utf-8')
    write_report(summary, out_dir / 'report.md')
    print('\n'.join(verdict(summary)))
    print(f'Wrote {out_dir}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
