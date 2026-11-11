"""Candidate C5: walk-forward sharpening of the research model's home/away split (offline only).

C, C2 and C3 are all too flat on development: the logistic calibration slope of the
home and of the away probability is 1.11-1.19 (docs/plan.md, Phase 2d), so outcomes
are more extreme than C forecasts. C5 keeps C's goal rates, its score grid and its
draw probability, and sharpens only how C splits the rest between home and away:

    r  = p_home / (p_home + p_away)                 C's home share of a decided match
    r' = sigmoid(slope * logit(r))                  slope > 1 sharpens
    C5 1X2 = ((1 - p_draw) r', p_draw, (1 - p_draw)(1 - r'))

and the grid is moved onto that 1X2 by reweighting its home-win, draw and away-win
regions (football_value_pipeline_v2_standalone.reweight_matrix_to_1x2: scorelines
keep their relative shape inside each region), so every market, Asian handicaps
included, still comes from one score grid. The draw is held exactly: draws are C2's
correction, and the plan changes one thing at a time.

Fit: walk-forward weighted maximum likelihood of the slope, a logistic regression
without intercept of "home won" on logit(r) over C's own earlier decided matches
(draws carry no information about the split). For a fold starting at `origin` it uses
every match C already forecast that was played before the origin, pooled across
leagues, with recency weights (half-life in days). It reads only C's goal rates and
the final scores: never odds, market fits or the published grid. Until MIN_MATCHES
decided matches exist the slope is neutral (1.0) and C5 equals C exactly.

Not used by the live pipeline. It is a harness candidate until it passes the release
gate in docs/plan.md.
"""
from __future__ import annotations

import math

import numpy as np
from scipy.optimize import minimize_scalar

VERSION = 'research-home-away-sharpen-walk-forward-v1'
SLOPE_BOUNDS = (0.5, 2.5)
MIN_MATCHES = 1000  # pooled earlier decided (non-draw) forecasts before the slope moves any price
NEUTRAL = {'slope': 1.}
EPS = 1e-9


def one_x_two(matrix):
    h, a = np.indices(matrix.shape)
    return np.array([matrix[h > a].sum(), matrix[h == a].sum(), matrix[h < a].sum()], dtype=float)


def home_share_logit(probs):
    """logit(p_home / (p_home + p_away)) for an (n, 3) array of 1X2 probabilities."""
    probs = np.asarray(probs, dtype=float).reshape(-1, 3)
    share = np.clip(probs[:, 0] / (probs[:, 0] + probs[:, 2]), EPS, 1 - EPS)
    return np.log(share / (1 - share))


def fit(probs, outcomes, age_days, half_life_days, min_matches=MIN_MATCHES, bounds=SLOPE_BOUNDS):
    """The slope by weighted maximum likelihood on C's earlier forecasts of decided matches.

    `probs` is C's (n, 3) 1X2 for each earlier match, `outcomes` 0/1/2 (home/draw/away)
    and `age_days` how long before the fold origin it was played. Draws are dropped.
    Returns NEUTRAL (C5 == C) below MIN_MATCHES decided matches or when the optimiser
    fails, so a bad fit never moves a price. `min_matches` and `bounds` default to C5's;
    the European CE2 and CE4 pass their own (european_candidates).
    """
    probs = np.asarray(probs, dtype=float).reshape(-1, 3)
    outcomes, age = np.asarray(outcomes), np.asarray(age_days, dtype=float)
    if (age < 0).any() or not np.isfinite(probs).all():
        raise ValueError('Fit rows must precede the origin and carry finite probabilities')
    decided = outcomes != 1
    if decided.sum() < min_matches:
        return {**NEUTRAL, 'status': 'warm_up', 'matches': int(decided.sum())}
    x, y = home_share_logit(probs[decided]), (outcomes[decided] == 0).astype(float)
    w = np.exp(-math.log(2) * age[decided] / half_life_days)

    def loss(slope):
        z = slope * x
        return float((w * (np.logaddexp(0., z) - y * z)).sum() / w.sum())  # weighted logistic log loss

    result = minimize_scalar(loss, bounds=bounds, method='bounded', options={'xatol': 1e-6})
    if not result.success or not np.isfinite(result.fun):
        return {**NEUTRAL, 'status': 'optimiser_failed', 'matches': int(decided.sum())}
    return {'slope': float(result.x), 'status': 'fitted', 'matches': int(decided.sum()),
            'neutral_minus_fitted_loss': float(loss(1.) - result.fun)}


def sharpened(probs, slope):
    """C5's 1X2 from C's: the draw held, the home/away split sharpened by `slope`."""
    probs = np.asarray(probs, dtype=float)
    if slope == 1.:
        return probs.copy()
    z = slope * home_share_logit(probs)[0]
    share = 1 / (1 + math.exp(-z))
    rest = 1 - probs[1]
    return np.array([rest * share, probs[1], rest * (1 - share)])


def sharpen_matrix(matrix, slope):
    """A score grid moved onto its own sharpened 1X2 (draw held). Neutral returns it unchanged.

    Shared by C5 (on C's grid) and C6 (on C2's grid, research_low_score_sharpen)."""
    from football_value_pipeline_v2_standalone import reweight_matrix_to_1x2
    slope = float(slope)
    if slope == 1.:
        return matrix  # neutral: exactly the grid it was given
    matrix = reweight_matrix_to_1x2(matrix, sharpened(one_x_two(matrix), slope))
    return matrix / matrix.sum()


def sharpened_grid(goal_rates, params):
    """The research grid for these goal rates, moved onto the sharpened 1X2."""
    from team_research import research_grid
    return sharpen_matrix(research_grid(goal_rates), params['slope'])
