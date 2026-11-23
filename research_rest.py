"""Candidate C6R: C6 plus rest and congestion (offline only; docs/plan.md, Phase 2h).

C6R adjusts the goal rates C6 starts from (C's rates) by each side's rest and congestion, then prices them
with C6's own walk-forward grid (C2's (rho, delta), then the slope, refitted on C6R's adjusted rates):

    log home' = log home + alpha . F_home + gamma . F_away
    log away' = log away + alpha . F_away + gamma . F_home

F = (S, C, E) per side, from the club's ESPN all-competition schedule (scripts/backfill_espn_schedules.py), counting
only completed competitive matches on calendar days strictly before the match day:
    S  short rest: the last competitive match 3 days or fewer before
    C  congestion: (min(n21, 6) - 3) / 3, n21 = competitive matches in the 21 days before
    E  European away: the last competitive match was a UEFA away fixture
A club without a schedule gets F = 0 (no adjustment). alpha (own fatigue on own scoring) and gamma (the opponent's
fatigue on own scoring) are fitted walk-forward by penalised Poisson maximum likelihood on the research rows forecast
and played before each fold origin, pooled across leagues, equal weights, each coefficient with a normal prior
(mean 0, sd PRIOR_SD). Neutral below MIN_MATCHES earlier rows: every coefficient 0 gives C's rates exactly, and so
C6 exactly.

Reads fixture dates, competitions and sides (the schedule cache holds no result), C's goal rates and final scores of
matches before the origin. Never odds, market fits or the published grid. Not used by the live pipeline and not a
registered harness candidate until it passes the release gate's declared test.
"""
from __future__ import annotations

from functools import lru_cache
import json
from pathlib import Path

import numpy as np
import pandas as pd

VERSION = 'research-rest-congestion-walk-forward-v1'
CANDIDATE = 'C6R'
ROOT = Path(__file__).resolve().parent
SCHEDULES = ROOT / 'data' / 'feature_cache' / 'espn_schedules'
TEAM_MAP = ROOT / 'evaluation' / 'c6_rest' / 'espn_team_map.csv'
FEATURES = ('short_rest', 'congestion', 'european_away')
PARAMETERS = tuple(f'alpha_{f}' for f in FEATURES) + tuple(f'gamma_{f}' for f in FEATURES)
MIN_MATCHES = 2000
PRIOR_SD = 0.10
SHORT_REST_DAYS = 3
CONGESTION_DAYS = 21
MAX_ITERATIONS = 100
TOLERANCE = 1e-10
NEUTRAL = {p: 0. for p in PARAMETERS}

# Competitive matches: the club's own country's competitions (league, cups, super cups, play-offs), UEFA competitions
# and qualifiers, and the Club World Cup. Fixed from the cached slugs on 23 Nov 2026 before any fit (Phase 2h).
COUNTRY = {'EPL': 'eng', 'LaLiga': 'esp', 'Bundesliga': 'ger', 'SerieA': 'ita', 'Ligue1': 'fra',
           'Eredivisie': 'ned', 'PrimeiraLiga': 'por', 'SuperLig': 'tur'}
# Slug review (every completed event in the cache, 23 Nov 2026): counted are each country's league, cups, super cups
# and play-offs, every uefa.* competition and qualifier, fifa.cwc and fifa.intercontinental_cup. Left out are
# club.friendly, friendly.emirates_cup, global.champs_cup, ger.audi_cup, esp.joan_gamper, eng.asia_trophy,
# jpn.world_challenge, global.club_challenge, euroamericana.supercopa and usa.1 (exhibitions). ESPN has no Turkish
# Cup or Super Cup and no Portuguese League Cup or Super Cup: those matches are missing for every club.
OTHER_COMPETITIVE_PREFIXES = ('uefa.', 'fifa.cwc', 'fifa.intercontinental_cup')
NON_COMPETITIVE = ('friendly', 'audi_cup', 'joan_gamper', 'champs_cup', 'asia_trophy')


def competitive(slug, league) -> bool:
    slug = str(slug or '')
    if not slug or any(k in slug for k in NON_COMPETITIVE):
        return False
    return slug.startswith(COUNTRY[league] + '.') or slug.startswith(OTHER_COMPETITIVE_PREFIXES)


def season_of(day) -> int:
    """ESPN season (start year) of a match day: July onwards belongs to the season starting that year."""
    day = pd.Timestamp(day)
    return day.year if day.month >= 7 else day.year - 1


# ---------------------------------------------------------------------------
# Schedules and features
# ---------------------------------------------------------------------------

def load_index(team_map=TEAM_MAP, folder=SCHEDULES):
    """(map {(league, season, football-data name): ESPN id}, {(ESPN id, league): (days, uefa_away)}): each club's
    completed competitive matches, deduplicated by event, as sorted UTC calendar days with a UEFA-away flag. All
    of a club's fetched seasons are pooled, so a season's first match sees the end of the previous one."""
    frame = pd.read_csv(team_map, dtype={'espn_id': str, 'season': int})
    ids = {(r.league, int(r.season), r.fd_team): r.espn_id for r in frame.itertuples(index=False)}
    events = {}
    for (espn_id, league), part in frame.groupby(['espn_id', 'league']):
        seen = {}
        for season in part.season.unique():
            file = Path(folder) / f'{espn_id}_{int(season)}.json'
            if not file.exists():
                continue
            data = json.loads(file.read_text(encoding='utf-8'))
            if data.get('schema') != 'espn-schedule-compact-v1':
                raise ValueError(f'{file.name}: not a compact schedule')
            for e in data['events']:
                if e.get('completed') and competitive(e.get('slug'), league) and e.get('date'):
                    seen[e['id']] = (pd.Timestamp(e['date']).tz_convert(None).normalize(),
                                     str(e['slug']).startswith('uefa.') and e.get('side') == 'away')
        if seen:
            rows = sorted(seen.values())
            events[(espn_id, league)] = (np.array([d for d, _ in rows], dtype='datetime64[D]'),
                                         np.array([a for _, a in rows], dtype=bool))
    return ids, events


def features_at(days, uefa_away, day):
    """(S, C, E) for a match on `day` from one club's sorted competitive match days (strictly earlier days only)."""
    d = np.datetime64(pd.Timestamp(day).normalize().date(), 'D')
    before = days < d
    if not before.any():
        return (0., (0. - 3.) / 3., 0.)
    j = int(np.flatnonzero(before)[-1])
    rest = int((d - days[j]).astype(int))
    n21 = int(((days >= d - np.timedelta64(CONGESTION_DAYS, 'D')) & before).sum())
    return (float(rest <= SHORT_REST_DAYS), (min(n21, 6) - 3.) / 3., float(uefa_away[j]))


def match_features(index, league, team, day):
    """(S, C, E) for one side of a domestic league match, or None when the club has no ESPN schedule."""
    ids, events = index
    espn_id = ids.get((league, season_of(day), team))
    if espn_id is None or (espn_id, league) not in events:
        return None
    days, away = events[(espn_id, league)]
    return features_at(days, away, day)


# ---------------------------------------------------------------------------
# Fit
# ---------------------------------------------------------------------------

def _design(f_home, f_away):
    """Stacked Poisson design, one row per side per match: home rows (F_home, F_away), away rows (F_away, F_home)."""
    return np.vstack([np.hstack([f_home, f_away]), np.hstack([f_away, f_home])])


def _objective(beta, x, offset, y):
    eta = offset + x @ beta
    return float(y @ eta - np.exp(eta).sum() - (beta @ beta) / (2 * PRIOR_SD ** 2))


def fit(rates, home_goals, away_goals, f_home, f_away):
    """(alpha, gamma) by penalised Poisson maximum likelihood with C's log rates as offsets. The objective is
    concave, so Newton's method with step halving from the neutral point finds its maximum. NEUTRAL below
    MIN_MATCHES rows or when the optimiser fails, so a bad fit never moves a price."""
    rates = np.asarray(rates, float).reshape(-1, 2)
    f_home, f_away = np.asarray(f_home, float).reshape(-1, 3), np.asarray(f_away, float).reshape(-1, 3)
    out = {**NEUTRAL, 'matches': len(rates)}
    if len(rates) < MIN_MATCHES:
        return {**out, 'status': 'warm_up'}
    if not np.isfinite(rates).all() or (rates <= 0).any() or not (np.isfinite(f_home).all() and np.isfinite(f_away).all()):
        raise ValueError('Fit rows must carry positive goal rates and finite features')
    x = _design(f_home, f_away)
    offset = np.concatenate([np.log(rates[:, 0]), np.log(rates[:, 1])])
    y = np.concatenate([np.asarray(home_goals, float), np.asarray(away_goals, float)])
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
            return {**dict(zip(PARAMETERS, (float(v) for v in beta))), 'matches': len(rates), 'status': 'fitted',
                    'objective_gain_per_match': float((value - start) / len(rates))}
    return {**out, 'status': 'optimiser_failed'}


def adjusted_rates(rates, params, f_home, f_away):
    """C6R's goal rates for one match. Neutral parameters, or no features, return C's rates exactly."""
    home, away = float(rates[0]), float(rates[1])
    if not (np.isfinite(home) and np.isfinite(away) and home > 0 and away > 0):
        raise ValueError('positive goal rates required')
    alpha = np.array([params[f'alpha_{f}'] for f in FEATURES], float)
    gamma = np.array([params[f'gamma_{f}'] for f in FEATURES], float)
    if not alpha.any() and not gamma.any():
        return [home, away]
    fh, fa = np.asarray(f_home, float), np.asarray(f_away, float)
    return [float(np.exp(np.log(home) + alpha @ fh + gamma @ fa)), float(np.exp(np.log(away) + alpha @ fa + gamma @ fh))]


def walk_forward(research, features, windows):
    """C6R's adjusted rates for every research row, and one fit per window.

    `research`: rows sorted by date with 'date', 'goal_rates' (C's), 'home_goals', 'away_goals'; `features`: one
    (F_home, F_away) per row, zeros where a club has no schedule; `windows`: (origin, stop) pairs. For each window
    the fit reads only rows played before its origin, and every row inside the window gets its adjusted rates under
    that fit: C6R's forecast of it, scored or not."""
    dates = pd.DatetimeIndex([r['date'] for r in research])
    rates = np.array([r['goal_rates'] for r in research], float).reshape(-1, 2)
    goals = np.array([(r['home_goals'], r['away_goals']) for r in research], float).reshape(-1, 2)
    fh = np.array([f[0] for f in features], float).reshape(-1, 3)
    fa = np.array([f[1] for f in features], float).reshape(-1, 3)
    adjusted = rates.copy()
    fits = []
    for origin, stop in windows:
        inside = np.flatnonzero((dates >= origin) & (dates < stop))
        if not len(inside):
            continue
        past = np.asarray(dates < origin)
        params = fit(rates[past], goals[past, 0], goals[past, 1], fh[past], fa[past])
        fits.append({'origin': pd.Timestamp(origin).date().isoformat(), 'end_exclusive': pd.Timestamp(stop).date().isoformat(),
                     **params})
        for i in inside:
            adjusted[i] = adjusted_rates(rates[i], params, fh[i], fa[i])
    return adjusted, fits
