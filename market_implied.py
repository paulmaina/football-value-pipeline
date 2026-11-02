"""Market-implied fair score distribution fitted to Pinnacle's margin-free prices.

Per fixture, fit home and away goal rates and a Dixon-Coles rho so the score
matrix jointly reproduces Pinnacle's margin-free 1X2, O/U 2.5 and (fit B) the
main Asian handicap line. Any AH line, whole, half or quarter, is then priced
exactly from the matrix. The production Dixon-Coles model is not involved.

The fit fails closed: it is unusable when any input is missing or stale, or
when any residual exceeds MAX_RESIDUAL. Unusable fits never price anything.
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from functools import lru_cache
from typing import Dict, Iterable, List, Optional, Tuple

import numpy as np
from scipy.optimize import least_squares
from scipy.stats import poisson

from ah_close_backtest import devig_proportional, effective_probability, outcome_probabilities, settle

VERSION = 'market-implied-dc-v1'
MAX_GOALS = 20
MAX_RESIDUAL = 0.03  # 3pp on any input.
LAMBDA_BOUNDS = (0.05, 6.0)
RHO_BOUNDS = (-0.3, 0.3)
INPUTS_A = ('home', 'draw', 'away', 'over_2_5')
INPUTS_B = (*INPUTS_A, 'ah_main')


def devig_three_way(home: float, draw: float, away: float) -> Tuple[float, float, float]:
    """Proportional margin removal for a 1X2 triple."""
    q = np.array([1 / home, 1 / draw, 1 / away])
    fair = q / q.sum()
    return float(fair[0]), float(fair[1]), float(fair[2])


def dixon_coles_matrix(lam_home: float, lam_away: float, rho: float, max_goals: int = MAX_GOALS) -> np.ndarray:
    """Normalised Dixon-Coles score grid; raises when a low-score factor is not positive."""
    goals = np.arange(max_goals + 1)
    matrix = np.outer(poisson.pmf(goals, lam_home), poisson.pmf(goals, lam_away))
    taus = ((0, 0, 1 - lam_home * lam_away * rho), (0, 1, 1 + lam_home * rho),
            (1, 0, 1 + lam_away * rho), (1, 1, 1 - rho))
    for h, a, tau in taus:
        if not tau > 0:
            raise ValueError('Invalid Dixon-Coles low-score correction')
        matrix[h, a] *= tau
    return matrix / matrix.sum()


@lru_cache(maxsize=None)
def _margin_index(size: int) -> np.ndarray:
    goals = np.arange(size)
    return (goals[:, None] - goals[None, :]).ravel() + (size - 1)


def margin_distribution(matrix: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    """Home goal margins and their probabilities."""
    size = matrix.shape[0]
    probs = np.bincount(_margin_index(size), weights=matrix.ravel(), minlength=2 * size - 1)
    return np.arange(-(size - 1), size), probs


def side_margins(margins: np.ndarray, side: str) -> np.ndarray:
    if side not in ('home', 'away'):
        raise ValueError('Unknown side')
    return margins if side == 'home' else -margins


def win_share(margins: np.ndarray, probs: np.ndarray, side: str, line: float) -> float:
    """Fair two-way probability of `side` at `line`: wins / (wins + losses), refunds excluded."""
    won, lost = settle(side_margins(margins, side), line)
    w, lo = float((probs * won).sum()), float((probs * lost).sum())
    return w / (w + lo) if w + lo > 0 else 0.5


def model_inputs(matrix: np.ndarray, ah_line: Optional[float]) -> Dict[str, float]:
    margins, probs = margin_distribution(matrix)
    goals = np.arange(matrix.shape[0])
    total = goals[:, None] + goals[None, :]
    out = {'home': float(probs[margins > 0].sum()), 'draw': float(probs[margins == 0].sum()),
           'away': float(probs[margins < 0].sum()), 'over_2_5': float(matrix[total > 2.5].sum())}
    if ah_line is not None:
        out['ah_main'] = win_share(margins, probs, 'home', ah_line)
    return out


def targets_from_prices(h2h: Optional[Tuple[float, float, float]] = None,
                        ou25: Optional[Tuple[float, float]] = None,
                        ah_main: Optional[Tuple[float, float, float]] = None) -> Dict[str, float]:
    """Margin-free targets: h2h (home, draw, away odds), ou25 (over, under), ah_main (home line, home, away odds)."""
    targets: Dict[str, float] = {}
    if h2h is not None:
        targets['home'], targets['draw'], targets['away'] = devig_three_way(*h2h)
    if ou25 is not None:
        targets['over_2_5'] = devig_proportional(*ou25)[0]
    if ah_main is not None:
        line, home, away = ah_main
        targets['ah_line'] = float(line)
        targets['ah_main'] = devig_proportional(home, away)[0]
    return targets


@dataclass
class Fit:
    kind: str
    usable: bool
    reasons: List[str]
    lam_home: Optional[float] = None
    lam_away: Optional[float] = None
    rho: Optional[float] = None
    residuals: Dict[str, float] = field(default_factory=dict)
    matrix: Optional[np.ndarray] = field(default=None, repr=False)

    @property
    def max_residual(self) -> Optional[float]:
        return max((abs(v) for v in self.residuals.values()), default=None)

    def record(self) -> Dict[str, object]:
        """Flat, JSON-safe summary for logs and CSVs."""
        return {'fit': self.kind, 'fit_usable': self.usable, 'fit_reasons': '; '.join(self.reasons),
                'fit_lambda_home': self.lam_home, 'fit_lambda_away': self.lam_away, 'fit_rho': self.rho,
                'fit_max_residual': self.max_residual,
                **{f'fit_residual_{k}': v for k, v in self.residuals.items()}}


def _start(targets: Dict[str, float]) -> np.ndarray:
    """Total goals from P(over 2.5) under Poisson, split by the 1X2 favourite."""
    over = min(max(targets['over_2_5'], 0.05), 0.95)
    total = 2.6
    for _ in range(50):
        p = 1 - poisson.cdf(2, total)
        total *= 1 + 0.5 * (over - p)
    share = 0.5 + 0.5 * (targets['home'] - targets['away'])
    share = min(max(share, 0.15), 0.85)
    return np.array([math.log(total * share), math.log(total * (1 - share)), -0.05])


def fit(targets: Dict[str, float], *, include_ah: bool, stale: Iterable[str] = ()) -> Fit:
    """Fit A (1X2 + O/U 2.5) or B (plus the main AH line). Fails closed."""
    kind = 'B' if include_ah else 'A'
    inputs = INPUTS_B if include_ah else INPUTS_A
    missing = [k for k in inputs if targets.get(k) is None or not math.isfinite(float(targets[k]))]
    if include_ah and targets.get('ah_line') is None:
        missing.append('ah_line')
    reasons = [f'missing input: {k}' for k in missing] + [f'stale input: {k}' for k in stale]
    if missing:
        return Fit(kind, False, reasons)
    line = float(targets['ah_line']) if include_ah else None

    def residuals(x):
        try:
            matrix = dixon_coles_matrix(math.exp(x[0]), math.exp(x[1]), x[2])
        except ValueError:
            return np.full(len(inputs), 1.0)
        model = model_inputs(matrix, line)
        return np.array([model[k] - targets[k] for k in inputs])

    low = [math.log(LAMBDA_BOUNDS[0])] * 2 + [RHO_BOUNDS[0]]
    high = [math.log(LAMBDA_BOUNDS[1])] * 2 + [RHO_BOUNDS[1]]
    start = np.clip(_start(targets), low, high)
    solution = least_squares(residuals, start, bounds=(low, high), xtol=1e-10, ftol=1e-12, gtol=1e-12)
    lam_home, lam_away, rho = math.exp(solution.x[0]), math.exp(solution.x[1]), float(solution.x[2])
    try:
        matrix = dixon_coles_matrix(lam_home, lam_away, rho)
    except ValueError:
        return Fit(kind, False, reasons + ['solver ended outside the valid Dixon-Coles region'])
    model = model_inputs(matrix, line)
    errors = {k: model[k] - targets[k] for k in inputs}
    worst = max(abs(v) for v in errors.values())
    if worst > MAX_RESIDUAL:
        reasons.append(f'residual {worst:.4f} above {MAX_RESIDUAL:.2f}')
    return Fit(kind, not reasons, reasons, lam_home, lam_away, rho, errors, matrix)


def price(result: Fit, side: str, line: float) -> Dict[str, float]:
    """Fair win-share, fair odds and settlement probabilities for `side` getting `line`."""
    if not result.usable or result.matrix is None:
        raise ValueError('Market-implied fit is unusable')
    margins, probs = margin_distribution(result.matrix)
    outcomes = outcome_probabilities(side_margins(margins, side), probs, line)
    q = effective_probability(outcomes)
    return {'win_share': q, 'fair_odds': 1 / q if q > 0 else math.inf,
            'p_no_loss': outcomes['p_win'] + outcomes['p_half_win'] + outcomes['p_push'], **outcomes}
