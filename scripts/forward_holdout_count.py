"""Count the forward holdout's priced fixtures and weeks (docs/plan.md, Phase 2g-4), before it is scored.

Reads only the date, the teams and the Bet365 price columns of the cached football-data.co.uk files: never a
score or any other result column. A fixture counts when it is in one of the eight leagues, played on or after the
forward start and before forward_end (the day after the last cached match), with valid Bet365 prices
(evaluation_harness.book_prices). Weeks are ISO calendar weeks, as the harness resamples them.

    python scripts/forward_holdout_count.py [--output evaluation/c9_forward_holdout/count.json]
"""
from __future__ import annotations

import argparse
import io
import json
from pathlib import Path
import sys

import pandas as pd

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO))

import evaluation_harness as eh  # noqa: E402
import historical_benchmark as hb  # noqa: E402

RESULT_COLUMNS = ('FTHG', 'FTAG', 'FTR', 'HTHG', 'HTAG', 'HTR')


def price_columns() -> list[str]:
    cols = eh.BOOKS['bet365']
    return [*cols['hda'], *cols['ou'], *cols['ah']]


def priced_rows(path, start, end) -> pd.DataFrame:
    """Date, teams and Bet365 prices of the file's matches in [start, end); the result columns are never read."""
    usecols = ['Date', 'HomeTeam', 'AwayTeam', *price_columns()]
    if set(usecols) & set(RESULT_COLUMNS):
        raise AssertionError('a result column would be read')
    raw = Path(path).read_bytes()
    try:
        content = raw.decode('utf-8-sig')
    except UnicodeDecodeError:
        content = raw.decode('latin1')
    header = pd.read_csv(io.StringIO(content), nrows=0).columns
    frame = pd.read_csv(io.StringIO(content), usecols=[c for c in usecols if c in header], low_memory=False)
    frame = frame.dropna(subset=['Date'])
    frame['Date'] = eh.file_dates(path).reindex(frame.index)
    return frame.loc[(frame.Date >= start) & (frame.Date < end)]


def count(cfg, cache) -> dict:
    forward = cfg['forward_holdout']
    start, end = pd.Timestamp(forward['start']), eh.forward_end(cfg, cache)
    leagues, weeks, total, unpriced = {}, set(), 0, 0
    for league in forward['leagues']:
        rows = pd.concat([priced_rows(Path(cache) / f"{season}_{hb.CODES[league]}.csv", start, end)
                          for season in cfg['seasons']], ignore_index=True)
        dates = [r.Date for r in rows.itertuples() if eh.book_prices(rows.loc[r.Index], forward['book']) is not None]
        n = len(dates)
        week = {f'{d.isocalendar().year}-W{d.isocalendar().week:02d}' for d in dates}
        weeks |= week
        leagues[league] = {'matches': len(rows), 'priced': n, 'weeks': sorted(week)}
        total += n
        unpriced += len(rows) - n
    minimum = eh.promotion_minimums()
    return {'start': start.date().isoformat(), 'end_exclusive': end.date().isoformat(),
            'last_match_date': (end - pd.Timedelta(days=1)).date().isoformat(), 'book': forward['book'],
            'priced_fixtures': total, 'unpriced_fixtures': unpriced, 'weeks': len(weeks), 'week_list': sorted(weeks),
            'by_league': leagues, 'sample_minimum': minimum,
            'sample_minimum_met': total >= minimum['fixtures'] and len(weeks) >= minimum['weeks'],
            'read': 'Date, HomeTeam, AwayTeam and Bet365 price columns only; no result column'}


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument('--cache', type=Path, default=REPO / '.football_cache')
    p.add_argument('--output', type=Path)
    args = p.parse_args(argv)
    cfg = json.loads(eh.CONFIG.read_text(encoding='utf-8'))
    out = count(cfg, args.cache)
    text = json.dumps(out, indent=1) + '\n'
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding='utf-8')
    print(text)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
