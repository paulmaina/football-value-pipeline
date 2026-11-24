"""Candidates C7 and C8: fitted rate calibration on the Dixon-Coles goal rates, without the form term (offline only).

The research model (team_research.prepare) blends each Dixon-Coles goal rate with the raw last-ten goals
using hand-set weights that were never fitted. The standing diagnostics (docs/plan.md, "How each change is
judged") show that the grid without that form term, C0, is level with C on development and no worse
afterwards. C7 and C8 start from C0's goal rates (prepare's base_rates: the fold's Dixon-Coles rates) and
replace the hand-set blend with a calibration fitted on the model's own earlier forecasts:

  C7  log(home') = a_home + b * log(home)
      log(away') = a_away + b * log(away)
  C8  C7 plus Elo: + c * z on the home rate and - c * z on the away rate, where
      z = pre-match Elo difference / 400 (elo_ratings, the fixture's elo_rating_diff: home rating plus the
      home advantage minus the away rating, from the training rows before the fold origin only).

(a_home, a_away, b[, c]) are fitted by weighted Poisson maximum likelihood on the goals of the matches
already forecast and played before the fold origin, pooled across leagues, with C2's recency half-life.
The score grid is then C2's (research_low_score.adjusted_grid): (rho, delta) refitted by C2's own fit on
the candidate's earlier calibrated rates, so one grid prices every market.

Until MIN_MATCHES earlier forecasts exist the calibration is neutral (a = 0, b = 1, c = 0: the candidate's
rates are C0's exactly, and with C2's neutral (rho, delta) its grid is C0's grid).

Reads only the Dixon-Coles goal rates, the Elo difference and final scores: never odds, market fits, the
published grid, or the last-ten form. Not used by the live pipeline; harness candidates until one passes
the release gate in docs/plan.md.

C9 (docs/plan.md, Phase 2g-4; Paul, 17 Nov 2026) is C8 with a home/away calibration slope on top, the step
C6 adds to C2 (research_sharpen.sharpen_matrix: the draw held, the home/away split sharpened):

  C9 grid = research_sharpen.sharpen_matrix(C8 grid, slope)

The slope is research_sharpen.fit on C8's own earlier forecasts of decided matches, walk-forward, but only on
development matches (played before the harness's development end, 1 Jul 2025): never a validation, holdout or
later result. From the first fold after development it is the slope fitted on every development forecast.
A neutral slope (1.0, below research_sharpen.MIN_MATCHES decided matches) gives C8's grid exactly.
"""
from __future__ import annotations

import math

import numpy as np

import research_low_score as rls

VERSION = 'research-rate-calibration-walk-forward-v1'
MIN_MATCHES = rls.MIN_MATCHES  # the same pooled warm-up as C2
ELO_SCALE = 400.  # z = Elo difference / 400: one unit is a tenfold change in the Elo odds
NEUTRAL = {'a_home': 0., 'a_away': 0., 'b': 1., 'c': 0.}
PARAMETERS = ('a_home', 'a_away', 'b', 'c')
MAX_ITERATIONS = 100
TOLERANCE = 1e-10


def elo_z(ratings, home, away):
    """Pre-match Elo difference / 400 from fitted ratings (elo_ratings.fixture_features), or None when a team
    has no rating. The difference includes the ratings' home advantage, as the live forecast row's
    elo_rating_diff does; the constant is absorbed by a_home and a_away."""
    from elo_ratings import fixture_features
    diff = fixture_features(ratings, home, away)['elo_rating_diff']
    return None if diff is None else float(diff) / ELO_SCALE


def _design(rates, z):
    """Stacked Poisson design: one row per side per match, columns (a_home, a_away, b[, c])."""
    n = len(rates)
    ones, zeros = np.ones(n), np.zeros(n)
    home = [ones, zeros, np.log(rates[:, 0])]
    away = [zeros, ones, np.log(rates[:, 1])]
    if z is not None:
        home.append(z)
        away.append(-z)
    return np.vstack([np.column_stack(home), np.column_stack(away)])


def _log_likelihood(beta, x, y, w):
    eta = x @ beta
    return float(w @ (y * eta - np.exp(eta)))


def fit(rates, home_goals, away_goals, age_days, half_life_days, z=None):
    """(a_home, a_away, b[, c]) by weighted Poisson maximum likelihood on earlier forecasts and their goals.

    `rates` is an (n, 2) array of C0's goal rates for each match (the fold's Dixon-Coles rates);
    `age_days` how long before the fold origin each match was played; `z`, for C8, each match's pre-match
    Elo difference / 400 as it stood when the match was forecast. The Poisson log likelihood with a log
    link is concave, so Newton's method with step halving from the neutral point finds its maximum.
    Returns NEUTRAL below MIN_MATCHES or when the fit fails, so a bad fit never moves a price.
    """
    rates = np.asarray(rates, dtype=float).reshape(-1, 2)
    hg, ag = np.asarray(home_goals, dtype=float), np.asarray(away_goals, dtype=float)
    age = np.asarray(age_days, dtype=float)
    z = None if z is None else np.asarray(z, dtype=float)
    out = {**NEUTRAL, 'elo': z is not None, 'matches': len(rates)}
    if len(rates) < MIN_MATCHES:
        return {**out, 'status': 'warm_up'}
    if (age < 0).any() or not np.isfinite(rates).all() or (rates <= 0).any():
        raise ValueError('Fit rows must precede the origin and carry positive goal rates')
    if z is not None and not np.isfinite(z).all():
        raise ValueError('Fit rows must carry a finite Elo difference')
    weights = np.exp(-math.log(2) * age / half_life_days)
    x, y, w = _design(rates, z), np.concatenate([hg, ag]), np.concatenate([weights, weights])
    beta = np.array([0., 0., 1.] + ([0.] if z is not None else []))
    start = value = _log_likelihood(beta, x, y, w)
    converged = False
    for _ in range(MAX_ITERATIONS):
        mean = np.exp(x @ beta)
        try:
            step = np.linalg.solve((x * (w * mean)[:, None]).T @ x, x.T @ (w * (y - mean)))
        except np.linalg.LinAlgError:
            break
        if not np.isfinite(step).all():
            break
        for _ in range(30):  # step halving: never accept a step that lowers the likelihood
            trial = _log_likelihood(beta + step, x, y, w)
            if np.isfinite(trial) and trial >= value - 1e-12 * abs(value):
                break
            step = step / 2
        else:
            break
        beta, value = beta + step, trial
        if np.abs(step).max() < TOLERANCE:
            converged = True
            break
    if not converged or not np.isfinite(beta).all():
        return {**out, 'status': 'optimiser_failed'}
    return {**dict(zip(PARAMETERS, (float(v) for v in beta))), 'c': float(beta[3]) if z is not None else 0.,
            'elo': z is not None, 'matches': len(rates), 'status': 'fitted',
            'neutral_minus_fitted_loss': float((value - start) / w.sum() * 2)}  # per match (two goal counts)


def calibrated_rates(rates, params, z=None):
    """The candidate's goal rates for one match: C0's rates through the fitted calibration. Neutral
    parameters return C0's rates exactly (no arithmetic), so a warm-up forecast is C0's."""
    home, away = float(rates[0]), float(rates[1])
    if not (math.isfinite(home) and math.isfinite(away) and home > 0 and away > 0):
        raise ValueError('positive goal rates required')
    a_home, a_away, b, c = (float(params[k]) for k in PARAMETERS)
    if (a_home, a_away, b, c) == tuple(NEUTRAL[k] for k in PARAMETERS):
        return [home, away]
    shift = 0.
    if c:
        if z is None or not math.isfinite(float(z)):
            raise ValueError('Elo difference required')
        shift = c * float(z)
    return [math.exp(a_home + b * math.log(home) + shift), math.exp(a_away + b * math.log(away) - shift)]


def grid(rates, params, low_score_params, z=None):
    """The candidate's score grid: its calibrated rates on C2's (rho, delta) grid. Everything neutral gives
    C0's grid (team_research.research_grid of the same rates) exactly."""
    return rls.adjusted_grid(calibrated_rates(rates, params, z), low_score_params)


SLOPE_VERSION = 'research-rate-calibration-elo-then-development-slope-v1'  # C9


def sharpened_grid(calibrated, low_score_params, slope):
    """C9's score grid: C8's grid (its calibrated rates on C2's (rho, delta) grid) moved onto its sharpened 1X2,
    the draw held (research_sharpen.sharpen_matrix, as C6 does to C2). A neutral slope gives C8's grid exactly."""
    import research_sharpen as rs
    return rs.sharpen_matrix(rls.adjusted_grid(calibrated, low_score_params), slope)
