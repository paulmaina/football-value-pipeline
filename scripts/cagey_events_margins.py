"""Average main-line AH margins frozen in calibration rule cagey-events-v1 (synthetic_ah_margin).

Each bookmaker's mean main-line AH overround (1/home + 1/away - 1) over the period it supplies the harness's
main line: Pinnacle on development and validation (1 Aug 2022 - 15 Jan 2026), Bet365 on the retrospective
(16 Jan 2026 onwards). Holdout matches are skipped before their prices are read. Also prints the means by
league and period (context only).

    python scripts/cagey_events_margins.py
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import evaluation_harness as eh  # noqa: E402
import historical_benchmark as hb  # noqa: E402


def margins(cache, cfg) -> pd.DataFrame:
    rows = []
    for league in cfg['leagues']:
        data, _, _ = hb.load_history(Path(cache), league, {**cfg, 'test_end_exclusive': cfg['end_exclusive']})
        data = data.loc[(data.Date >= cfg['test_start']) & (data.Date < cfg['end_exclusive'])]
        for _, row in data.iterrows():
            name = eh.phase(row.Date, league, cfg)
            if name == 'holdout':
                continue  # skipped before its prices are read
            for book in eh.BOOKS:
                prices = eh.book_prices(row, book)
                if prices:
                    rows.append({'league': league, 'phase': name, 'book': book,
                                 'margin': sum(1 / p for p in prices['ah'][1:]) - 1})
    return pd.DataFrame(rows)


def main() -> int:
    cfg = json.loads(eh.CONFIG.read_text(encoding='utf-8'))
    frame = margins(ROOT / '.football_cache', cfg)
    used = {'pinnacle': frame.loc[(frame.book == 'pinnacle') & frame.phase.isin(['development', 'validation'])],
            'bet365': frame.loc[(frame.book == 'bet365') & (frame.phase == 'retrospective')]}
    print(json.dumps({b: {'margin': float(part.margin.mean()), 'matches': int(len(part))} for b, part in used.items()},
                     indent=2))
    print(frame.pivot_table(index='league', columns=['book', 'phase'], values='margin', aggfunc='mean').round(4))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
