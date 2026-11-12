"""C's forecasts on real EPL folds, with and without every price moved, shared by the C2, C5 and C6 odds tests.

test_research_low_score, test_research_sharpen and test_research_low_score_sharpen each check that their
candidate reads only C's goal rates and the scores. They need the same inputs: C's forecasts of 40 EPL matches
before 1 Dec 2023 (fit only) and 5 after 1 Mar 2024 (scored), from Dixon-Coles folds refitted on the real
history and on the same history with every price moved. Both are computed once per test process.
"""
from functools import lru_cache
import json
from pathlib import Path

import pandas as pd

import evaluation_harness as eh

REPO = Path(__file__).resolve().parents[1]
CFG = json.loads((REPO / 'evaluation_harness_config.json').read_text(encoding='utf-8'))
ODDS_PREFIXES = ('PS', 'P>', 'P<', 'PC', 'PAH', 'B365', 'Max', 'Avg', 'BW', 'IW', 'WH', 'VC', 'AH', '1X', 'BF', 'PSC')
ORIGIN = pd.Timestamp('2024-03-01')
FIT_ORIGIN = pd.Timestamp('2023-12-01')


def research_row(league, date, goal_rates, hg, ag, scored=True, phase='development'):
    """One entry of the harness's research list (evaluate_league)."""
    identity = {'league': league, 'date': str(date.date()),
                'week': f'{date.isocalendar().year}-W{date.isocalendar().week:02d}',
                'fixture_key': f'{league}|{date.isoformat()}', 'phase': phase, 'market_book': 'pinnacle'}
    return {'identity': identity, 'date': date, 'goal_rates': [float(v) for v in goal_rates],
            'home_goals': float(hg), 'away_goals': float(ag), 'scored': scored}


def fit(train, origin):
    from football_value_pipeline_v2_standalone import DixonColesModel
    return DixonColesModel(half_life_days=480., l2=.08, max_goals=10, shot_features=True,
                           bbs_statistics=False).fit(train.copy(), as_of=origin)


@lru_cache(maxsize=None)
def data():
    import historical_benchmark as hb
    frame, _, _ = hb.load_history(REPO / '.football_cache', 'EPL',
                                  {**CFG, 'seasons': ['2122', '2223', '2324'], 'test_end_exclusive': '2024-07-01'})
    return frame


def odds_columns():
    """Every price column; the handicap lines (AHh, AHCh) keep valid quarter values."""
    return [c for c in data().columns if c.startswith(ODDS_PREFIXES) and c not in ('AHh', 'AHCh')]


@lru_cache(maxsize=None)
def shaken():
    """The same history with every price moved by 2% plus 0.01."""
    frame = data().copy()
    odds = odds_columns()
    frame[odds] = frame[odds].apply(pd.to_numeric, errors='coerce') * 1.02 + .01
    return frame


@lru_cache(maxsize=None)
def scored_fold():
    """The Dixon-Coles fold at ORIGIN on the real history: (train, model)."""
    train = data()[data().Date < ORIGIN]
    return train, fit(train, ORIGIN)


def _research_rows(frame, folds):
    import narrow_margin as nm
    cagey, rows, matrices = nm.production_model(), [], []
    for (origin, scored), (train, model) in zip(((FIT_ORIGIN, False), (ORIGIN, True)), folds):
        test = frame[frame.Date >= origin].head(5 if scored else 40)
        for _, row in test.iterrows():
            m, _, extra = eh.candidates(row, train, origin, model, CFG, cagey)
            matrices.append(m)
            rows.append(research_row('EPL', row.Date, extra['research_goal_rates'], row.FTHG, row.FTAG, scored))
    return rows, matrices


def research_rows(moved=False):
    """C's forecasts (research rows) and every candidate's grid for the 45 matches, on the real history or,
    with `moved`, on the shaken one (refitted). Fresh copies of one computation per process."""
    rows, matrices = _cached_rows(moved)
    return [{**r, 'identity': dict(r['identity'])} for r in rows], [{k: v.copy() for k, v in m.items()} for m in matrices]


@lru_cache(maxsize=None)
def _cached_rows(moved):
    frame = shaken() if moved else data()
    folds = []
    for origin in (FIT_ORIGIN, ORIGIN):
        if origin == ORIGIN and not moved:
            folds.append(scored_fold())
            continue
        train = frame[frame.Date < origin]
        folds.append((train, fit(train, origin)))
    return _research_rows(frame, folds)
