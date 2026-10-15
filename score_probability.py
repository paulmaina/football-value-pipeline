"""Probability-safe score grids; frozen legacy reconstruction stays separate."""
import math
import numpy as np
from scipy.stats import poisson

SCORE_ENGINE_VERSION = 'dc-positive-tail-bounded-v1'
MAX_OMITTED_MASS = 1e-10
MAX_SCORE_GRID = 100


def valid_matrix(matrix):
    value = np.asarray(matrix, dtype=float)
    if (value.ndim != 2 or min(value.shape, default=0) < 1
            or not np.isfinite(value).all() or (value < 0).any()
            or not math.isfinite(float(value.sum())) or value.sum() <= 0):
        raise ValueError('Invalid score probability matrix')
    return value


def score_grid(lam, mu, rho, minimum=10):
    if not all(math.isfinite(x) for x in (lam, mu, rho)) or min(lam, mu) <= 0:
        raise ValueError('Invalid goal parameters')
    if isinstance(minimum, bool) or not isinstance(minimum, (int, np.integer)) or not 5 <= minimum <= MAX_SCORE_GRID:
        raise ValueError('Invalid minimum score grid')
    corrections = ((0, 0, 1-lam*mu*rho), (0, 1, 1+lam*rho),
                   (1, 0, 1+mu*rho), (1, 1, 1-rho))
    if any(tau <= 0 or not math.isfinite(tau) for _, _, tau in corrections):
        raise ValueError('Invalid Dixon-Coles low-score correction')
    quantile = max(poisson.isf(MAX_OMITTED_MASS/2, lam), poisson.isf(MAX_OMITTED_MASS/2, mu))
    if not math.isfinite(quantile) or quantile > MAX_SCORE_GRID:
        raise ValueError('Goal distribution exceeds the safe score-grid limit')
    size = max(minimum, int(math.ceil(quantile)))
    home_tail, away_tail = poisson.sf(size, lam), poisson.sf(size, mu)
    omitted = float(home_tail+away_tail-home_tail*away_tail)
    if not math.isfinite(omitted) or omitted > MAX_OMITTED_MASS:
        raise ValueError('Score-grid omitted probability exceeds tolerance')
    goals = np.arange(size+1)
    matrix = np.outer(poisson.pmf(goals, lam), poisson.pmf(goals, mu))
    for h, a, tau in corrections:
        matrix[h, a] *= tau
    matrix = valid_matrix(matrix)
    matrix = matrix/matrix.sum()
    return matrix, {'score_engine_version': SCORE_ENGINE_VERSION,
                    'score_grid_max_goals': size, 'score_grid_omitted_mass': omitted}
