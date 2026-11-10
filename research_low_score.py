"""Candidate C2: draw and low-score correction for the research score grid (offline only).

The research model (team_research.research_grid) prices every score as two
independent Poisson counts. Independent Poisson under-prices draws and the
0-0 / 1-1 scores and over-prices 1-0 / 0-1 (docs/plan.md, Phase 2a). C2 keeps
the research goal rates exactly as they are and reshapes the grid with two
parameters fitted on the research model's own earlier forecasts and their scores:

  rho    Dixon-Coles low-score term on 0-0, 1-0, 0-1 and 1-1
  delta  draw inflation: every draw cell is multiplied by exp(delta)

    P(h, a) = tau_rho(h, a) * Pois(h; lam) * Pois(a; mu) * exp(delta * [h == a]) / Z

Fit: walk-forward weighted maximum likelihood on the research model's own
earlier forecasts. For a fold starting at `origin`, the fit uses every match
the research model (C) has already forecast and that was played before the
origin, pooled across the leagues, with C's goal rates for that match held
fixed and recency weights (half-life in days). It reads only C's goal rates
and the final scores: never odds, market fits or the published grid. Until
MIN_MATCHES such matches exist the correction is neutral (C2 == C).

Not used by the live pipeline. It is a harness candidate until it passes the
release gate in docs/plan.md.
"""
from __future__ import annotations

import math

import numpy as np
from scipy.optimize import minimize
from scipy.stats import poisson

VERSION = 'research-draw-low-score-walk-forward-v1'
GRID = 10  # goals per side in the fit; mass beyond it is negligible at league goal rates
RHO_BOUNDS = (-0.25, 0.10)
DELTA_BOUNDS = (-0.50, 0.50)
MIN_MATCHES = 1000  # pooled earlier forecasts needed before the correction moves any price
NEUTRAL = {'rho': 0., 'delta': 0.}


def tau_cells(lam, mu, rho):
    """Dixon-Coles multipliers for (0,0), (0,1), (1,0), (1,1)."""
    return 1 - lam * mu * rho, 1 + lam * rho, 1 + mu * rho, 1 - rho


def _log_likelihood(params, lam, mu, hg, ag, weights, pmf_h, pmf_a):
    rho, delta = params
    t00, t01, t10, t11 = np.broadcast_arrays(*tau_cells(lam, mu, rho))
    if min(t00.min(), t01.min(), t10.min(), t11.min()) <= 0:
        return -np.inf
    # Normaliser: the independent grid sums to ~1; the four tau cells and the diagonal change it.
    p00, p01, p10, p11 = pmf_h[:, 0] * pmf_a[:, 0], pmf_h[:, 0] * pmf_a[:, 1], pmf_h[:, 1] * pmf_a[:, 0], pmf_h[:, 1] * pmf_a[:, 1]
    diag = (pmf_h * pmf_a).sum(1)
    total = (pmf_h.sum(1) * pmf_a.sum(1)
             + (t00 - 1) * p00 + (t01 - 1) * p01 + (t10 - 1) * p10 + (t11 - 1) * p11
             + (math.exp(delta) - 1) * (diag - p00 - p11 + t00 * p00 + t11 * p11))
    tau = np.ones_like(lam)
    for (h, a), t in zip(((0, 0), (0, 1), (1, 0), (1, 1)), (t00, t01, t10, t11)):
        cell = (hg == h) & (ag == a)
        tau[cell] = t[cell]
    log_p = (poisson.logpmf(hg, lam) + poisson.logpmf(ag, mu) + np.log(tau)
             + delta * (hg == ag) - np.log(total))
    return float((weights * log_p).sum())


def fit(rates, home_goals, away_goals, age_days, half_life_days):
    """(rho, delta) by weighted maximum likelihood on earlier research forecasts and their scores.

    `rates` is an (n, 2) array of the research goal rates C used for each match;
    `age_days` is how long before the fold origin each match was played. Returns
    NEUTRAL (C2 == C) below MIN_MATCHES or when the optimiser fails, so a bad fit
    never moves a price.
    """
    rates = np.asarray(rates, dtype=float).reshape(-1, 2)
    hg, ag = np.asarray(home_goals, dtype=float), np.asarray(away_goals, dtype=float)
    age = np.asarray(age_days, dtype=float)
    if len(rates) < MIN_MATCHES:
        return {**NEUTRAL, 'status': 'warm_up', 'matches': len(rates)}
    if (age < 0).any() or not np.isfinite(rates).all() or (rates <= 0).any():
        raise ValueError('Fit rows must precede the origin and carry positive goal rates')
    lam, mu = rates[:, 0], rates[:, 1]
    weights = np.exp(-math.log(2) * age / half_life_days)
    goals = np.arange(GRID + 1)
    pmf_h, pmf_a = poisson.pmf(goals[None, :], lam[:, None]), poisson.pmf(goals[None, :], mu[:, None])

    def loss(p):
        value = -_log_likelihood(p, lam, mu, hg, ag, weights, pmf_h, pmf_a) / weights.sum()
        return value if np.isfinite(value) else 1e6  # an invalid low-score cell is never the optimum

    result = minimize(loss, x0=[0., 0.], method='L-BFGS-B', bounds=[RHO_BOUNDS, DELTA_BOUNDS])
    if not result.success or not np.isfinite(result.fun):
        return {**NEUTRAL, 'status': 'optimiser_failed', 'matches': len(rates)}
    rho, delta = (float(v) for v in result.x)
    return {'rho': rho, 'delta': delta, 'status': 'fitted', 'matches': len(rates),
            'neutral_minus_fitted_loss': float(loss([0., 0.]) - result.fun)}


def adjusted_grid(goal_rates, params):
    """The research grid for these goal rates, reshaped by (rho, delta) and renormalised."""
    from score_probability import score_grid, valid_matrix
    matrix, _ = score_grid(*goal_rates, float(params['rho']))
    if not params['delta']:
        return matrix  # rho = delta = 0 is exactly the research grid
    matrix = matrix.copy()
    matrix[np.diag_indices(min(matrix.shape))] *= math.exp(float(params['delta']))
    matrix = valid_matrix(matrix)
    return matrix / matrix.sum()
