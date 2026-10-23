"""Closing-line value (CLV) for every evaluated candidate, by market and bookmaker.

The forward shortlist tracker (closing_odds.py) measures CLV for selected picks
only. This report measures it for *every* priced candidate the filter
evaluated, shortlisted or rejected, so you can see where positive CLV
appears, if anywhere, with a usable sample size.

Inputs (read-only, already produced by the pipeline):
  * entries: ``raw/shortlist_history/conservative_decisions_*.csv`` (every
    evaluation, with offered price, bookmaker and timestamp);
  * closes: ``closing_odds/observations/*.json`` (live feed quotes observed
    within six minutes of kickoff, de-vigged with the power method).

Per candidate, using the latest evaluation before kickoff and the latest
near-kickoff observation that prices it:

  clv_vs_pinnacle_fair = entry_odds / pinnacle_fair_close_odds - 1
      Main edge measure. Pinnacle's no-vig closing price is the best public
      estimate of the true probability. For win/lose bets this equals the
      EV at the closing fair probability. For lines that can refund it has
      the same sign, scaled by P(not refunded).
  same_book_price_clv = entry_odds / same_book_close_odds - 1
      Whether the entry beat that bookmaker's own closing price.
  market move towards model (binary markets with an entry reference)
      gap  = raw model probability - entry reference probability
      move = Pinnacle fair close probability - entry reference probability
      If the model knows something the market does not, ``move`` follows
      ``gap``: positive correlation and sign agreement above 50%.

Observed near-kickoff quotes are not guaranteed official closing prices and
local timestamps are not independently attested. Nothing here changes
forecasts, filters or stakes.
"""
from __future__ import annotations

import argparse
import json
import math
import re
from pathlib import Path
from typing import Dict, Optional, Tuple

import numpy as np
import pandas as pd

VERSION = 'candidate-clv-v1'
OUTPUT_DIR = Path('performance') / 'clv_report'
SELECTIONS = {'Home win': 'home', 'Draw': 'draw', 'Away win': 'away',
              'Double Chance 1X': 'home_draw', 'Double Chance X2': 'draw_away',
              'Double Chance 12': 'home_away', 'Both Teams to Score - Yes': 'btts_yes',
              'Both Teams to Score - No': 'btts_no'}
DOUBLE_CHANCE = {'home_draw': ('home', 'draw'), 'draw_away': ('draw', 'away'), 'home_away': ('home', 'away')}
HANDICAP = re.compile(r'Asian Handicap (Home|Away) ([+-]\d+\.\d{2})')
TOTAL = re.compile(r'(Over|Under) (\d+\.5)')
HOUR_BUCKETS = [0, 6, 24, 48, np.inf]
HOUR_LABELS = ['<6h', '6-24h', '24-48h', '48h+']
GROUPINGS = {'market_bookmaker': ['market_family', 'entry_bookmaker'],
             'market': ['market_family'], 'entry_bookmaker': ['entry_bookmaker'],
             'decision': ['decision_group'], 'hours_before_kickoff': ['hours_bucket'],
             'league': ['league'], 'market_detail': ['market_family', 'market']}


def selection_key(market: str) -> Optional[str]:
    """Closing-quote selection key for a decision market label."""
    if market in SELECTIONS:
        return SELECTIONS[market]
    if HANDICAP.fullmatch(str(market)):
        return str(market)
    total = TOTAL.fullmatch(str(market))
    if total:
        return f"{total[1].lower()}_{total[2].replace('.', '_')}"
    return None


def market_family(market: str) -> str:
    if market in ('Home win', 'Draw', 'Away win'):
        return '1X2'
    if str(market).startswith('Double Chance'):
        return 'Double chance'
    if str(market).startswith('Both Teams'):
        return 'BTTS'
    if HANDICAP.fullmatch(str(market)):
        return 'Asian handicap'
    if TOTAL.fullmatch(str(market)):
        return 'Goal totals'
    return 'Other'


def _power_devig(prices) -> list:
    from football_value_pipeline_v2_standalone import devig
    return devig(list(prices), method='power')


def fair_closing_prices(quotes) -> Dict[str, float]:
    """Pinnacle fair closing *probability* per selection key.

    1X2, totals and BTTS use the observation's de-vigged quotes. Double
    chance sums the de-vigged 1X2 pair. Asian handicaps de-vig each
    complete opposite-side Pinnacle pair (Home h vs Away -h); their value
    is the conditional win probability excluding refunds.
    """
    pinnacle = {q['selection']: q for q in quotes if q.get('bookmaker') == 'pinnacle'}
    fair = {k: float(q['fair_probability']) for k, q in pinnacle.items()
            if q.get('fair_probability') is not None}
    if all(k in fair for k in ('home', 'draw', 'away')):
        for key, (a, b) in DOUBLE_CHANCE.items():
            fair[key] = fair[a] + fair[b]
    for key, quote in pinnacle.items():
        match = HANDICAP.fullmatch(key)
        if not match:
            continue
        side, line = match[1], float(match[2])
        other = f"Asian Handicap {'Away' if side == 'Home' else 'Home'} {-line + 0.0:+.2f}"
        if other in pinnacle:
            probability = _power_devig([quote['decimal_odds'], pinnacle[other]['decimal_odds']])[0]
            if probability is not None:
                fair[key] = float(probability)
    return fair


def load_closes(root: Path) -> Dict[str, dict]:
    """Per fixture: Pinnacle fair probabilities and every book's closing odds.

    Later observations (closer to kickoff) overwrite earlier ones per
    selection, so each price is the last one seen before kickoff.
    """
    from performance_tracking import fixture_key
    closes: Dict[str, dict] = {}
    files = sorted((root / 'closing_odds' / 'observations').glob('*.json'))
    observations = [json.loads(f.read_text(encoding='utf-8')) for f in files]
    for obs in sorted(observations, key=lambda o: o.get('observed_at_utc', '')):
        record = closes.setdefault(fixture_key(obs['fixture']), {'fair': {}, 'odds': {}, 'observed': {}})
        for key, p in fair_closing_prices(obs.get('quotes', [])).items():
            record['fair'][key] = p
            record['observed'][key] = obs['observed_at_utc']
        for q in obs.get('quotes', []):
            record['odds'][(q['bookmaker'], q['selection'])] = float(q['decimal_odds'])
    return closes


def load_entries(root: Path) -> pd.DataFrame:
    """Latest priced pre-kickoff evaluation per fixture, market and bookmaker."""
    from performance_tracking import fixture_key
    files = sorted((root / 'raw' / 'shortlist_history').glob('conservative_decisions_*.csv'))
    frames = [pd.read_csv(f, low_memory=False) for f in files]
    columns = ['league', 'home_team', 'away_team', 'kickoff_utc', 'evaluated_at_utc', 'market',
               'bookmaker', 'offered_decimal_odds', 'decision', 'selection_tier',
               'predicted_probability', 'raw_dc_probability', 'market_probability', 'estimated_ev']
    if not frames:
        return pd.DataFrame(columns=columns)
    data = pd.concat(frames, ignore_index=True, sort=False).reindex(columns=columns)
    data['offered_decimal_odds'] = pd.to_numeric(data['offered_decimal_odds'], errors='coerce')
    data = data[(data['offered_decimal_odds'] > 1) & data['bookmaker'].notna()].copy()
    kickoff = pd.to_datetime(data['kickoff_utc'], utc=True, errors='coerce')
    evaluated = pd.to_datetime(data['evaluated_at_utc'], utc=True, errors='coerce')
    data['hours_before_kickoff'] = (kickoff - evaluated).dt.total_seconds() / 3600
    data = data[data['hours_before_kickoff'] > 0]
    data['fixture_key'] = [fixture_key(r) for r in data.to_dict('records')]
    data['entry_bookmaker'] = data['bookmaker'].astype(str)
    data = data.sort_values('evaluated_at_utc', kind='mergesort')
    return data.drop_duplicates(['fixture_key', 'market', 'entry_bookmaker'], keep='last').reset_index(drop=True)


def candidate_clv(root: Path) -> pd.DataFrame:
    """One row per candidate with a Pinnacle fair close (see module docstring)."""
    entries, closes = load_entries(Path(root)), load_closes(Path(root))
    rows = []
    for entry in entries.to_dict('records'):
        key = selection_key(entry['market'])
        close = closes.get(entry['fixture_key'])
        if key is None or close is None or key not in close['fair']:
            continue
        fair_p = close['fair'][key]
        if not 0 < fair_p < 1:
            continue
        odds = float(entry['offered_decimal_odds'])
        same_book = close['odds'].get((entry['entry_bookmaker'].lower().replace(' ', ''), key))
        reference = pd.to_numeric(entry.get('market_probability'), errors='coerce')
        model = pd.to_numeric(entry.get('raw_dc_probability'), errors='coerce')
        binary = not HANDICAP.fullmatch(entry['market'])
        rows.append({**entry, 'selection_key': key, 'market_family': market_family(entry['market']),
                     'decision_group': 'shortlisted' if str(entry['decision']).startswith('SHORTLISTED') else 'not selected',
                     'pinnacle_fair_close_probability': fair_p,
                     'pinnacle_fair_close_odds': 1 / fair_p,
                     'close_observed_at_utc': close['observed'][key],
                     'clv_vs_pinnacle_fair': odds * fair_p - 1,
                     'same_book_close_odds': same_book,
                     'same_book_price_clv': None if same_book is None else odds / same_book - 1,
                     'model_gap': (model - reference) if binary and pd.notna(model) and pd.notna(reference) else None,
                     'market_move': (fair_p - reference) if binary and pd.notna(reference) else None})
    frame = pd.DataFrame(rows)
    if not frame.empty:
        frame['hours_bucket'] = pd.cut(frame['hours_before_kickoff'], HOUR_BUCKETS, labels=HOUR_LABELS, right=False).astype(str)
    return frame


def summarize(values: pd.Series) -> dict:
    """Mean, spread and a t-statistic; |t| < 2 is indistinguishable from zero."""
    values = pd.to_numeric(values, errors='coerce').dropna()
    n = len(values)
    if not n:
        return {'n': 0, 'mean': None, 'median': None, 'positive_share': None, 'standard_error': None, 't_stat': None}
    se = float(values.std(ddof=1) / math.sqrt(n)) if n > 1 else None
    mean = float(values.mean())
    return {'n': n, 'mean': mean, 'median': float(values.median()),
            'positive_share': float((values > 0).mean()), 'standard_error': se,
            't_stat': mean / se if se else None}


def movement(frame: pd.DataFrame) -> dict:
    """Does the Pinnacle close move towards the model's raw disagreement?"""
    data = frame.dropna(subset=['model_gap', 'market_move']) if not frame.empty else frame
    data = data[data['model_gap'].abs() > 1e-9] if len(data) else data
    if len(data) < 3:
        return {'n': int(len(data)), 'correlation': None, 'sign_agreement': None}
    with np.errstate(invalid='ignore', divide='ignore'):
        correlation = np.corrcoef(data['model_gap'], data['market_move'])[0, 1]
    return {'n': int(len(data)),
            'correlation': _finite(correlation),  # undefined when either side is constant
            'sign_agreement': float((np.sign(data['model_gap']) == np.sign(data['market_move'])).mean()),
            'mean_abs_model_gap': float(data['model_gap'].abs().mean()),
            'mean_abs_market_move': float(data['market_move'].abs().mean())}


def grouped(frame: pd.DataFrame, columns) -> pd.DataFrame:
    rows = []
    for name, part in frame.groupby(columns, dropna=False, sort=True):
        name = name if isinstance(name, tuple) else (name,)
        pinnacle, same = summarize(part['clv_vs_pinnacle_fair']), summarize(part['same_book_price_clv'])
        rows.append({**dict(zip(columns, name)), 'fixtures': part['fixture_key'].nunique(),
                     **{'pinnacle_fair_' + k: v for k, v in pinnacle.items()},
                     **{'same_book_' + k: v for k, v in same.items()},
                     'shortlisted': int((part['decision_group'] == 'shortlisted').sum())})
    return pd.DataFrame(rows).sort_values('pinnacle_fair_mean', ascending=False)


def _finite(value) -> Optional[float]:
    return None if value is None or not math.isfinite(float(value)) else float(value)


def _pct(value) -> str:
    return '—' if value is None or (isinstance(value, float) and math.isnan(value)) else f'{value:+.1%}'


def _num(value, fmt='{:.2f}') -> str:
    return '—' if value is None or (isinstance(value, float) and math.isnan(value)) else fmt.format(value)


def markdown(summary: dict, tables: Dict[str, pd.DataFrame]) -> str:
    overall = summary['overall_pinnacle_fair']
    lines = ['# Candidate closing-line value', '',
             f"Generated {summary['generated_at_utc']}; {summary['candidates']} priced candidates on "
             f"{summary['fixtures']} fixtures with a Pinnacle near-kickoff quote. "
             'CLV = entry odds × Pinnacle fair close probability − 1 (EV at the sharp close). '
             '|t| < 2 cannot be told apart from zero; positive CLV needs |t| ≥ 2 on a large sample.', '',
             f"**Overall:** mean {_pct(overall['mean'])}, {_num(overall['positive_share'], '{:.0%}')} positive, "
             f"t = {_num(overall['t_stat'])} (n = {overall['n']}).", '',
             f"**Shortlisted picks:** mean {_pct(summary['shortlisted_pinnacle_fair']['mean'])}, "
             f"n = {summary['shortlisted_pinnacle_fair']['n']}.", '']
    move = summary['market_move_towards_model']
    lines += ['**Does the market move towards the model?** '
              + (f"correlation {_num(move['correlation'])}, sign agreement "
                 f"{_num(move['sign_agreement'], '{:.0%}')} (n = {move['n']}; 50% = no information)."
                 if move['correlation'] is not None else f"insufficient data (n = {move['n']})."), '']
    positive = summary['positive_cells']
    lines += ['**Market × bookmaker cells with positive mean CLV:** '
              + ('; '.join(f"{c['market_family']} @ {c['entry_bookmaker']} {_pct(c['mean'])} "
                           f"(n = {c['n']}, t = {_num(c['t_stat'])})" for c in positive) or 'none') + '', '']
    for title, key, columns in (('By market and entry bookmaker', 'market_bookmaker', ['market_family', 'entry_bookmaker']),
                                ('By hours before kickoff at entry', 'hours_before_kickoff', ['hours_bucket']),
                                ('Shortlisted vs not selected', 'decision', ['decision_group']),
                                ('By league', 'league', ['league'])):
        lines += [f'## {title}', '',
                  '| ' + ' | '.join(columns) + ' | n | Fixtures | Mean CLV vs Pinnacle fair | Positive | t | Same-book CLV (n) |',
                  '|' + '---|' * len(columns) + '---:|---:|---:|---:|---:|---:|']
        for r in tables[key].to_dict('records'):
            lines.append('| ' + ' | '.join(str(r[c]) for c in columns) +
                         f" | {r['pinnacle_fair_n']} | {r['fixtures']} | {_pct(r['pinnacle_fair_mean'])} | "
                         f"{_num(r['pinnacle_fair_positive_share'], '{:.0%}')} | {_num(r['pinnacle_fair_t_stat'])} | "
                         f"{_pct(r['same_book_mean'])} ({r['same_book_n']}) |")
        lines.append('')
    lines += ['Near-kickoff feed quotes are not guaranteed official closing prices. '
              'Candidates repeat across markets of the same fixture, so fixtures are not independent '
              'samples and t-statistics are optimistic.', '']
    return '\n'.join(lines)


def build_report(root: Path, out_dir: Optional[Path] = None, clock=None) -> dict:
    """Write candidate CSV, grouped CSVs, summary JSON and Markdown report."""
    from datetime import datetime, timezone
    root = Path(root)
    out_dir = Path(out_dir) if out_dir is not None else root / OUTPUT_DIR
    out_dir.mkdir(parents=True, exist_ok=True)
    frame = candidate_clv(root)
    generated = (clock or datetime.now(timezone.utc)).isoformat()
    if frame.empty:
        summary = {'version': VERSION, 'generated_at_utc': generated, 'candidates': 0, 'fixtures': 0,
                   'status': 'NO_CANDIDATES_WITH_PINNACLE_CLOSE'}
        (out_dir / 'summary.json').write_text(json.dumps(summary, indent=2), encoding='utf-8')
        (out_dir / 'report.md').write_text('# Candidate closing-line value\n\nNo priced candidate has a '
                                           'Pinnacle near-kickoff quote yet.\n', encoding='utf-8')
        return summary
    tables = {name: grouped(frame, columns) for name, columns in GROUPINGS.items()}
    cells = tables['market_bookmaker']
    positive = cells[cells['pinnacle_fair_mean'] > 0]
    summary = {'version': VERSION, 'generated_at_utc': generated, 'status': 'OK',
               'candidates': int(len(frame)), 'fixtures': int(frame['fixture_key'].nunique()),
               'entry_files': len(list((root / 'raw' / 'shortlist_history').glob('conservative_decisions_*.csv'))),
               'overall_pinnacle_fair': summarize(frame['clv_vs_pinnacle_fair']),
               'overall_same_book': summarize(frame['same_book_price_clv']),
               'shortlisted_pinnacle_fair': summarize(frame.loc[frame['decision_group'] == 'shortlisted', 'clv_vs_pinnacle_fair']),
               'market_move_towards_model': movement(frame),
               'positive_cells': [{'market_family': r['market_family'], 'entry_bookmaker': r['entry_bookmaker'],
                                   'mean': _finite(r['pinnacle_fair_mean']), 'n': int(r['pinnacle_fair_n']),
                                   't_stat': _finite(r['pinnacle_fair_t_stat'])} for r in positive.to_dict('records')],
               'automatic_production_change': False}
    frame.to_csv(out_dir / 'candidates.csv', index=False)
    for name, table in tables.items():
        table.to_csv(out_dir / f'by_{name}.csv', index=False)
    (out_dir / 'summary.json').write_text(json.dumps(summary, indent=2, allow_nan=False, default=str), encoding='utf-8')
    (out_dir / 'report.md').write_text(markdown(summary, tables), encoding='utf-8')
    return summary


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description='Closing-line value for every evaluated candidate, by market and bookmaker.')
    parser.add_argument('--root-dir', type=Path, default=Path(__file__).resolve().parent / 'football_output_v2')
    parser.add_argument('--output-dir', type=Path, default=None,
                        help='Default: <root-dir>/performance/clv_report')
    args = parser.parse_args(argv)
    summary = build_report(args.root_dir, args.output_dir)
    overall = summary.get('overall_pinnacle_fair', {})
    # ASCII only: Windows consoles may not encode the report's dash placeholder.
    print(f"CLV report: {summary['candidates']} candidates on {summary['fixtures']} fixtures; "
          f"mean CLV vs Pinnacle fair {_pct(overall.get('mean'))}, "
          f"t = {_num(overall.get('t_stat'))}".replace('—', 'n/a'))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
