"""Monte Carlo pricing from the production Dixon-Coles score grid.

Each simulation draws one scoreline from ``score_probability.score_grid``
(categorical sampling over every cell, so the Dixon-Coles low-score
correction is kept). Markets are settled per simulated scoreline with the
same rules as production: totals and BTTS directly, Asian handicaps through
``asian_handicap.settlement``.

For each selection the simulated win share ``p`` has standard error
``sqrt(p * (1 - p) / N)`` (about 0.5 points at N = 10,000, p = 0.5), and the
true decimal price is the zero-EV price

    1 + (loss + half_loss / 2) / (win + half_win / 2)

which is ``1 / p`` for a win/lose selection. Because the grid is known
exactly, simulated values converge to the ``exact_*`` columns, which remain
the pricing reference. Simulation is a consistency check and the hook for
score processes that are not a fixed matrix (for example game-state or
in-play models).
"""
from __future__ import annotations

from typing import Sequence, Union

import numpy as np
import pandas as pd

from asian_handicap import settlement
from score_probability import score_grid

VERSION = 'dc-grid-monte-carlo-v1'
DEFAULT_SIMULATIONS = 10_000
TOTAL_LINES = (1.5, 2.5, 3.5)
HANDICAP_LINES = (0.0, -0.5, 0.5)
COLUMNS = ['market', 'selection', 'line', 'win', 'half_win', 'refund', 'half_loss', 'loss']
Seed = Union[int, np.random.Generator, None]


def simulate_scores(matrix: np.ndarray, n_simulations: int = DEFAULT_SIMULATIONS,
                    seed: Seed = None) -> tuple[np.ndarray, np.ndarray]:
    """Draw ``n_simulations`` (home_goals, away_goals) pairs from a score grid."""
    if isinstance(n_simulations, bool) or not isinstance(n_simulations, (int, np.integer)) or n_simulations < 1:
        raise ValueError('n_simulations must be a positive integer')
    grid = np.asarray(matrix, dtype=float)
    if grid.ndim != 2 or (grid < 0).any() or not np.isfinite(grid).all() or grid.sum() <= 0:
        raise ValueError('Invalid score probability matrix')
    draws = np.random.default_rng(seed).choice(grid.size, size=int(n_simulations), p=(grid / grid.sum()).ravel())
    return np.divmod(draws, grid.shape[1])


def _row(market: str, selection: str, line, w: np.ndarray, lost: np.ndarray, weights: np.ndarray) -> dict:
    """Settlement shares for per-scoreline won/lost stake fractions."""
    share = lambda mask: float(weights[mask].sum())
    return {'market': market, 'selection': selection, 'line': line,
            'win': share((w == 1)), 'half_win': share((w == .5)),
            'refund': share((w == 0) & (lost == 0)),
            'half_loss': share((lost == .5)), 'loss': share((lost == 1))}


def price_scores(home: np.ndarray, away: np.ndarray, weights: np.ndarray,
                 total_lines: Sequence[float] = TOTAL_LINES,
                 handicap_lines: Sequence[float] = HANDICAP_LINES) -> pd.DataFrame:
    """Settle every selection over weighted scorelines.

    ``weights`` are probabilities: grid cell probabilities for exact pricing,
    or ``1/N`` per draw for simulated pricing.
    """
    home, away = np.asarray(home), np.asarray(away)
    weights = np.asarray(weights, dtype=float)
    one, zero = np.ones(home.shape), np.zeros(home.shape)
    rows = [_row('1x2', side, None, np.where(mask, one, zero), np.where(mask, zero, one), weights)
            for side, mask in (('home', home > away), ('draw', home == away), ('away', home < away))]
    total = home + away
    for line in total_lines:
        over_w, over_l = (total > line).astype(float), (total < line).astype(float)
        rows.append(_row('total', 'over', line, over_w, over_l, weights))
        rows.append(_row('total', 'under', line, over_l, over_w, weights))
    both = (home > 0) & (away > 0)
    rows.append(_row('btts', 'yes', None, both.astype(float), (~both).astype(float), weights))
    rows.append(_row('btts', 'no', None, (~both).astype(float), both.astype(float), weights))
    margin = home - away
    values = np.unique(margin)
    for point in handicap_lines:
        for side, sign, side_line in (('home', 1, point), ('away', -1, -point + 0.0)):
            table = {int(m): settlement(int(m) * sign, side_line) for m in values}
            w = np.array([table[int(m)][0] for m in margin])
            lost = np.array([table[int(m)][1] for m in margin])
            rows.append(_row('asian_handicap', side, side_line, w, lost, weights))
    frame = pd.DataFrame(rows, columns=COLUMNS)
    gain = frame['win'] + frame['half_win'] / 2
    lose = frame['loss'] + frame['half_loss'] / 2
    frame['fair_decimal_odds'] = np.where(gain > 0, 1 + lose / gain.where(gain > 0, 1), np.inf)
    return frame


def simulate_fixture(lambda_home: float, lambda_away: float, rho: float,
                     n_simulations: int = DEFAULT_SIMULATIONS, seed: Seed = None,
                     minimum_grid: int = 10,
                     total_lines: Sequence[float] = TOTAL_LINES,
                     handicap_lines: Sequence[float] = HANDICAP_LINES) -> pd.DataFrame:
    """Simulated and exact prices for one fixture.

    Columns: settlement shares from the simulation, ``win_standard_error``,
    ``true_decimal_price`` (simulated) and ``exact_win`` /
    ``exact_fair_decimal_odds`` from the full grid.
    """
    matrix, _ = score_grid(lambda_home, lambda_away, rho, minimum_grid)
    home, away = simulate_scores(matrix, n_simulations, seed)
    simulated = price_scores(home, away, np.full(home.shape, 1.0 / len(home)), total_lines, handicap_lines)
    grid_home, grid_away = np.indices(matrix.shape)
    exact = price_scores(grid_home.ravel(), grid_away.ravel(), matrix.ravel(), total_lines, handicap_lines)
    p = simulated['win'].to_numpy()
    result = simulated.rename(columns={'fair_decimal_odds': 'true_decimal_price'})
    result['win_standard_error'] = np.sqrt(p * (1 - p) / len(home))
    result['exact_win'] = exact['win']
    result['exact_fair_decimal_odds'] = exact['fair_decimal_odds']
    result.attrs.update(version=VERSION, n_simulations=len(home), lambda_home=lambda_home,
                        lambda_away=lambda_away, rho=rho, score_grid_max_goals=matrix.shape[0] - 1)
    return result


def exact_prices(lambda_home: float, lambda_away: float, rho: float, minimum_grid: int = 10,
                 total_lines: Sequence[float] = TOTAL_LINES,
                 handicap_lines: Sequence[float] = HANDICAP_LINES) -> pd.DataFrame:
    """Exact grid prices only (no sampling)."""
    matrix, _ = score_grid(lambda_home, lambda_away, rho, minimum_grid)
    home, away = np.indices(matrix.shape)
    return price_scores(home.ravel(), away.ravel(), matrix.ravel(), total_lines, handicap_lines)
