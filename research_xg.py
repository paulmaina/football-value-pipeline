"""Candidate C6X: C6 plus rolling pre-kickoff xG for and against (offline only; docs/plan.md, Phase 2i).

C6X adjusts the goal rates C6 starts from (C's rates) by each side's recent expected goals, then prices them with
C6's own walk-forward grid (C2's (rho, delta), then the slope, refitted on C6X's adjusted rates):

    log home' = log home + alpha . F_home + gamma . F_away
    log away' = log away + alpha . F_away + gamma . F_home

F = (X_for, X_against) per side, from that club's last WINDOW league matches with cached API-Football xG
(scripts/extract_api_football_xg.py) played on calendar days strictly before the match day:

    X_for     = w * (mean xG for     - mean goals for)
    X_against = w * (mean xG against - mean goals against)      w = k / (k + SHRINK), k <= WINDOW matches

so the xG form is shrunk towards the goals-based form of the same matches when the history is short:
(k * xG + SHRINK * goals) / (k + SHRINK) minus goals. A club with no such match gets F = 0 (no adjustment).
alpha is the effect of a side's own xG-minus-goals on its scoring, gamma that of the opponent's. Four
coefficients, fitted walk-forward by penalised Poisson maximum likelihood on the research rows forecast and played
before each fold origin, the five leagues pooled, equal weights, each coefficient with a normal prior (mean 0,
sd PRIOR_SD). Neutral below MIN_MATCHES earlier rows where both sides have at least MIN_SIDE_MATCHES xG matches:
every coefficient 0 gives C's rates exactly, and so C6 exactly.

Reads cached xG of matches before the match day, final scores of matches before the match day (goals for the
shrinkage, and the fit's targets before the origin) and C's goal rates. Never odds, market fits or the published
grid. Not used by the live pipeline and not a registered harness candidate.
"""
from __future__ import annotations

from collections import defaultdict
from pathlib import Path

import numpy as np
import pandas as pd

VERSION = 'research-xg-form-walk-forward-v1'
CANDIDATE = 'C6X'
ROOT = Path(__file__).resolve().parent
XG_TABLE = ROOT / 'data' / 'feature_cache' / 'api_football_xg' / 'xg_matches.csv'
LEAGUES = ('EPL', 'LaLiga', 'Bundesliga', 'SerieA', 'Ligue1')
FEATURES = ('xg_for', 'xg_against')
PARAMETERS = tuple(f'alpha_{f}' for f in FEATURES) + tuple(f'gamma_{f}' for f in FEATURES)
WINDOW = 8
SHRINK = 4.
MIN_SIDE_MATCHES = 3
MIN_MATCHES = 600
PRIOR_SD = 0.20
MAX_ITERATIONS = 100
TOLERANCE = 1e-10
NEUTRAL = {p: 0. for p in PARAMETERS}


# ---------------------------------------------------------------------------
# Features
# ---------------------------------------------------------------------------

def load_xg(path=XG_TABLE):
    """{(league, date, home, away): (home xG, away xG)} for the five leagues; UCL rows are not read."""
    frame = pd.read_csv(path, dtype={'season': str})
    frame = frame.loc[frame.league.isin(LEAGUES)]
    if frame.duplicated(['league', 'date', 'home', 'away']).any():
        raise ValueError('Duplicate xG match')
    return {(r.league, r.date, r.home, r.away): (float(r.home_xg), float(r.away_xg)) for r in frame.itertuples(index=False)}


def team_index(matches, xg):
    """{(league, team): sorted [(day, xG for, xG against, goals for, goals against)]} over the matches that have xG.

    `matches`: (league, date, home, away, home goals, away goals) of completed league matches, the research rows'
    own fixtures. A match without cached xG is skipped, so it neither counts towards k nor moves the goals form."""
    index = defaultdict(list)
    for league, day, home, away, hg, ag in matches:
        value = xg.get((league, pd.Timestamp(day).date().isoformat(), home, away))
        if value is None:
            continue
        stamp = np.datetime64(pd.Timestamp(day).date(), 'D')
        index[(league, home)].append((stamp, value[0], value[1], float(hg), float(ag)))
        index[(league, away)].append((stamp, value[1], value[0], float(ag), float(hg)))
    return {k: sorted(v, key=lambda r: r[0]) for k, v in index.items()}


def side_features(rows, day):
    """((X_for, X_against), k) for one side on `day` from its sorted xG matches; strictly earlier days only."""
    d = np.datetime64(pd.Timestamp(day).date(), 'D')
    past = [r for r in rows if r[0] < d][-WINDOW:]
    k = len(past)
    if not k:
        return (0., 0.), 0
    a = np.array([r[1:] for r in past], float)
    w = k / (k + SHRINK)
    return (float(w * (a[:, 0].mean() - a[:, 2].mean())), float(w * (a[:, 1].mean() - a[:, 3].mean()))), k


def match_features(index, league, home, away, day):
    """((F_home, F_away), (k_home, k_away)) for one league match; zeros for a league or club without xG."""
    if league not in LEAGUES:
        return ((0., 0.), (0., 0.)), (0, 0)
    fh, kh = side_features(index.get((league, home), []), day)
    fa, ka = side_features(index.get((league, away), []), day)
    return (fh, fa), (kh, ka)


# ---------------------------------------------------------------------------
# Fit
# ---------------------------------------------------------------------------

def _design(f_home, f_away):
    """Stacked Poisson design, one row per side per match: home rows (F_home, F_away), away rows (F_away, F_home)."""
    return np.vstack([np.hstack([f_home, f_away]), np.hstack([f_away, f_home])])


def _objective(beta, x, offset, y):
    eta = offset + x @ beta
    return float(y @ eta - np.exp(eta).sum() - (beta @ beta) / (2 * PRIOR_SD ** 2))


def fit(rates, home_goals, away_goals, f_home, f_away, eligible):
    """(alpha, gamma) by penalised Poisson maximum likelihood with C's log rates as offsets, on the `eligible` rows
    (both sides with at least MIN_SIDE_MATCHES xG matches). The objective is concave, so Newton's method with step
    halving from the neutral point finds its maximum. NEUTRAL below MIN_MATCHES eligible rows or when the optimiser
    fails, so a bad fit never moves a price."""
    eligible = np.asarray(eligible, bool)
    rates = np.asarray(rates, float).reshape(-1, 2)[eligible]
    f_home = np.asarray(f_home, float).reshape(-1, 2)[eligible]
    f_away = np.asarray(f_away, float).reshape(-1, 2)[eligible]
    home_goals, away_goals = np.asarray(home_goals, float)[eligible], np.asarray(away_goals, float)[eligible]
    out = {**NEUTRAL, 'matches': int(len(rates))}
    if len(rates) < MIN_MATCHES:
        return {**out, 'status': 'warm_up'}
    if not np.isfinite(rates).all() or (rates <= 0).any() or not (np.isfinite(f_home).all() and np.isfinite(f_away).all()):
        raise ValueError('Fit rows must carry positive goal rates and finite features')
    x = _design(f_home, f_away)
    offset = np.concatenate([np.log(rates[:, 0]), np.log(rates[:, 1])])
    y = np.concatenate([home_goals, away_goals])
    beta = np.zeros(len(PARAMETERS))
    value = start = _objective(beta, x, offset, y)
    penalty = np.eye(len(beta)) / PRIOR_SD ** 2
    for _ in range(MAX_ITERATIONS):
        mean = np.exp(offset + x @ beta)
        try:
            step = np.linalg.solve((x * mean[:, None]).T @ x + penalty, x.T @ (y - mean) - beta / PRIOR_SD ** 2)
        except np.linalg.LinAlgError:
            return {**out, 'status': 'optimiser_failed'}
        for _ in range(30):
            trial = _objective(beta + step, x, offset, y)
            if np.isfinite(trial) and trial >= value - 1e-12 * abs(value):
                break
            step = step / 2
        else:
            return {**out, 'status': 'optimiser_failed'}
        beta, value = beta + step, trial
        if np.abs(step).max() < TOLERANCE:
            mean = np.exp(offset + x @ beta)
            information = (x * mean[:, None]).T @ x + penalty
            se = np.sqrt(np.diag(np.linalg.inv(information)))
            return {**dict(zip(PARAMETERS, (float(v) for v in beta))),
                    **{f'se_{p}': float(s) for p, s in zip(PARAMETERS, se)},
                    'matches': int(len(rates)), 'status': 'fitted',
                    'objective_gain_per_match': float((value - start) / len(rates))}
    return {**out, 'status': 'optimiser_failed'}


def adjusted_rates(rates, params, f_home, f_away):
    """C6X's goal rates for one match. Neutral parameters, or zero features, return C's rates exactly."""
    home, away = float(rates[0]), float(rates[1])
    if not (np.isfinite(home) and np.isfinite(away) and home > 0 and away > 0):
        raise ValueError('positive goal rates required')
    alpha = np.array([params[f'alpha_{f}'] for f in FEATURES], float)
    gamma = np.array([params[f'gamma_{f}'] for f in FEATURES], float)
    fh, fa = np.asarray(f_home, float), np.asarray(f_away, float)
    if not (alpha.any() or gamma.any()) or not (fh.any() or fa.any()):
        return [home, away]
    return [float(np.exp(np.log(home) + alpha @ fh + gamma @ fa)), float(np.exp(np.log(away) + alpha @ fa + gamma @ fh))]


def walk_forward(research, features, counts, windows):
    """C6X's adjusted rates for every research row, and one fit per window.

    `research`: rows sorted by date with 'date', 'goal_rates' (C's), 'home_goals', 'away_goals'; `features`: one
    (F_home, F_away) per row; `counts`: one (k_home, k_away) per row; `windows`: (origin, stop) pairs. Each window's
    fit reads only rows played before its origin, and every row inside the window gets its adjusted rates under that
    fit: C6X's forecast of it, scored or not."""
    dates = pd.DatetimeIndex([r['date'] for r in research])
    rates = np.array([r['goal_rates'] for r in research], float).reshape(-1, 2)
    goals = np.array([(r['home_goals'], r['away_goals']) for r in research], float).reshape(-1, 2)
    fh = np.array([f[0] for f in features], float).reshape(-1, 2)
    fa = np.array([f[1] for f in features], float).reshape(-1, 2)
    eligible = np.array([min(k) >= MIN_SIDE_MATCHES for k in counts], bool)
    adjusted = rates.copy()
    fits = []
    for origin, stop in windows:
        inside = np.flatnonzero((dates >= origin) & (dates < stop))
        if not len(inside):
            continue
        past = np.asarray(dates < origin)
        if past.any() and dates[past].max() >= origin:
            raise ValueError('A fit row is not before its origin')
        params = fit(rates[past], goals[past, 0], goals[past, 1], fh[past], fa[past], eligible[past])
        fits.append({'origin': pd.Timestamp(origin).date().isoformat(), 'end_exclusive': pd.Timestamp(stop).date().isoformat(),
                     **params})
        for i in inside:
            adjusted[i] = adjusted_rates(rates[i], params, fh[i], fa[i])
    return adjusted, fits
