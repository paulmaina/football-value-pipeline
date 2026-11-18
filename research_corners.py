"""Offline corner-total candidate K1 and its yardsticks (research only; nothing live reads this file).

K1: per league, home and away corner counts are Poisson with
    log E[home corners] = c_home + attack[home] + defence[away]
    log E[away corners] = c_away + attack[away] + defence[home]
fitted by time-weighted maximum likelihood (half-life in days) with a ridge penalty that shrinks every
attack and defence term toward 0, the league average (`prior_matches` sets its strength in matches of
evidence). The match total is negative binomial with mean E[home] + E[away] and a dispersion fitted on the
same weighted training matches. Refitted on every match day from earlier days only.

B0 (league average): the match total is negative binomial with the time-weighted league mean total and its
fitted dispersion (half-life 365 days), refitted on every match day from earlier days only.

NB2 is `count_markets.walk_forward` (count-markets-nb2-v1) unchanged.

Data: football-data.co.uk HC, AC (and HS, AS for NB2 only) from `.football_cache` and
`.football_cache/domestic_backfill`, read only up to CUTOFF (15 Jan 2026, the end of validation): rows after it
are dropped as each file is parsed. Goal columns are never loaded.
"""
from __future__ import annotations

import math
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.optimize import minimize, minimize_scalar
from scipy.stats import nbinom

VERSION = 'research-corners-k1-v1'
CUTOFF = pd.Timestamp('2026-01-15')
PERIODS = {'development': (pd.Timestamp('2022-08-01'), pd.Timestamp('2025-06-30')),
           'validation': (pd.Timestamp('2025-07-01'), CUTOFF)}
DIVISIONS = {'EPL': 'E0', 'LaLiga': 'SP1', 'Bundesliga': 'D1', 'SerieA': 'I1', 'Ligue1': 'F1',
             'Eredivisie': 'N1', 'PrimeiraLiga': 'P1', 'SuperLig': 'T1'}
MAIN_LINES = (8.5, 9.5, 10.5, 11.5)
COLUMNS = ('Date', 'HomeTeam', 'AwayTeam', 'HC', 'AC', 'HS', 'AS')
# Inputs tested on top of K1 (earlier matches only): goals for Dixon-Coles and Elo, shots on target, and
# Pinnacle's pre-match 1X2 and O/U 2.5 prices for the market-informed variant only.
INPUT_COLUMNS = COLUMNS + ('FTHG', 'FTAG', 'HST', 'AST', 'PSH', 'PSD', 'PSA', 'P>2.5', 'P<2.5')
WINDOW_DAYS = 4 * 365
BASELINE_HALF_LIFE_DAYS = 365.0
# Development grid for K1, chosen on development only (mean Over log loss over MAIN_LINES).
GRID_HALF_LIFE_DAYS = (120.0, 240.0, 480.0)
GRID_PRIOR_MATCHES = (2.0, 5.0, 12.0)
ALPHA_BOUNDS = (1e-4, 5.0)


# ---------------------------------------------------------------------------
# Data
# ---------------------------------------------------------------------------

def _read(path: Path, cutoff: pd.Timestamp, columns=COLUMNS) -> pd.DataFrame:
    try:
        frame = pd.read_csv(path, encoding='utf-8-sig', usecols=lambda c: c.lstrip('﻿') in columns)
    except UnicodeDecodeError:
        frame = pd.read_csv(path, encoding='latin-1', usecols=lambda c: c.lstrip('﻿') in columns)
    frame.columns = [c.lstrip('﻿') for c in frame.columns]
    frame = frame.dropna(subset=['Date', 'HomeTeam', 'AwayTeam'])
    # Two- and four-digit years differ between seasons; parse each file on its own, then write one format.
    when = pd.to_datetime(frame['Date'], dayfirst=True, format='mixed', errors='coerce')
    frame = frame.loc[when.notna() & (when <= cutoff)].copy()
    frame['Date'] = when.loc[frame.index].dt.strftime('%d/%m/%Y')
    return frame


def load_league(cache: Path, division: str, cutoff: pd.Timestamp = CUTOFF, columns=COLUMNS) -> pd.DataFrame:
    """Backfill and cached seasons for one division, rows on or before `cutoff` only, oldest first."""
    cache = Path(cache)
    files = sorted((cache / 'domestic_backfill').glob(f'????_{division}.csv')) + sorted(cache.glob(f'????_{division}.csv'))
    frames = [_read(p, cutoff, columns) for p in files]
    frame = pd.concat([f for f in frames if len(f)], ignore_index=True)
    return frame.drop_duplicates(['Date', 'HomeTeam', 'AwayTeam'], keep='last').reset_index(drop=True)


def matches(history: pd.DataFrame) -> pd.DataFrame:
    """Completed matches with both corner counts, ordered by date."""
    frame = history.copy()
    frame['date'] = pd.to_datetime(frame['Date'], format='%d/%m/%Y')
    frame['home_count'] = pd.to_numeric(frame['HC'], errors='coerce')
    frame['away_count'] = pd.to_numeric(frame['AC'], errors='coerce')
    frame = frame.dropna(subset=['home_count', 'away_count'])
    frame = frame.sort_values(['date', 'HomeTeam', 'AwayTeam'], kind='stable').reset_index(drop=True)
    frame['total'] = (frame.home_count + frame.away_count).astype(int)
    return frame[['date', 'HomeTeam', 'AwayTeam', 'home_count', 'away_count', 'total']]


# ---------------------------------------------------------------------------
# Distributions
# ---------------------------------------------------------------------------

def nb_over(mu, alpha, lines=MAIN_LINES) -> dict:
    """P(total > line) for half lines under NB2 with mean mu and variance mu + alpha mu^2."""
    r = 1.0 / alpha
    dist = nbinom(r, r / (r + mu))
    return {line: float(1.0 - dist.cdf(math.floor(line))) for line in lines}


def nb_log_pmf(total, mu, alpha) -> float:
    r = 1.0 / alpha
    return float(nbinom.logpmf(total, r, r / (r + mu)))


def _fit_alpha(y, mu, w) -> float:
    """Weighted ML NB2 dispersion given fixed means."""
    y, mu, w = (np.asarray(a, float) for a in (y, mu, w))

    def nll(log_alpha):
        r = 1.0 / math.exp(log_alpha)
        return -float(np.sum(w * nbinom.logpmf(y, r, r / (r + mu))))
    out = minimize_scalar(nll, bounds=tuple(math.log(b) for b in ALPHA_BOUNDS), method='bounded',
                          options={'xatol': 1e-4})
    return float(math.exp(out.x))


def _weights(dates: np.ndarray, day: pd.Timestamp, half_life: float) -> np.ndarray:
    age = (np.datetime64(day, "ns") - dates.astype("datetime64[ns]")) / np.timedelta64(1, "D")
    return np.power(0.5, age / half_life)


# ---------------------------------------------------------------------------
# K1: team corner rates
# ---------------------------------------------------------------------------

class _TeamRates:
    """Ridge-penalised weighted Poisson fit of home/away corner counts with team attack and defence terms."""

    def __init__(self, prior_matches: float, home_advantage: bool = True):
        self.prior_matches = prior_matches
        self.home_advantage = home_advantage
        self.params = {}

    def fit(self, train: pd.DataFrame, w: np.ndarray):
        teams = sorted(set(train.HomeTeam) | set(train.AwayTeam))
        index = {t: i for i, t in enumerate(teams)}
        n = len(teams)
        h = train.HomeTeam.map(index).to_numpy()
        a = train.AwayTeam.map(index).to_numpy()
        yh, ya = train.home_count.to_numpy(float), train.away_count.to_numpy(float)
        side_mean = float(np.average(np.r_[yh, ya], weights=np.r_[w, w]))
        # Poisson information per match is about the side mean, so prior_matches matches of evidence.
        penalty = 0.5 * self.prior_matches * side_mean
        start = np.zeros(2 + 2 * n)
        start[0], start[1] = math.log(np.average(yh, weights=w)), math.log(np.average(ya, weights=w))
        for team, value in self.params.items():  # warm start from the previous day's fit
            if team in index:
                start[2 + index[team]], start[2 + n + index[team]] = value

        def objective(theta):
            if not self.home_advantage:  # one intercept for both sides: no home advantage
                theta = theta.copy()
                theta[1] = theta[0]
            att, dfn = theta[2:2 + n], theta[2 + n:]
            eta_h = theta[0] + att[h] + dfn[a]
            eta_a = theta[1] + att[a] + dfn[h]
            lam_h, lam_a = np.exp(eta_h), np.exp(eta_a)
            value = float(np.sum(w * (lam_h - yh * eta_h)) + np.sum(w * (lam_a - ya * eta_a))
                          + penalty * (att @ att + dfn @ dfn))
            gh, ga = w * (lam_h - yh), w * (lam_a - ya)
            grad = np.empty_like(theta)
            grad[0], grad[1] = gh.sum(), ga.sum()
            if not self.home_advantage:
                grad[0], grad[1] = grad[0] + grad[1], 0.0
            grad[2:2 + n] = np.bincount(h, gh, n) + np.bincount(a, ga, n) + 2 * penalty * att
            grad[2 + n:] = np.bincount(a, gh, n) + np.bincount(h, ga, n) + 2 * penalty * dfn
            return value, grad
        result = minimize(objective, start, jac=True, method='L-BFGS-B')
        theta = result.x
        if not self.home_advantage:
            theta[1] = theta[0]
        self.c_home, self.c_away = float(theta[0]), float(theta[1])
        self.params = {t: (float(theta[2 + i]), float(theta[2 + n + i])) for t, i in index.items()}
        fitted = (np.exp(theta[0] + theta[2:2 + n][h] + theta[2 + n:][a])
                  + np.exp(theta[1] + theta[2:2 + n][a] + theta[2 + n:][h]))
        return fitted

    def mean(self, home: str, away: str) -> float:
        ah, dh = self.params.get(home, (0.0, 0.0))
        aa, da = self.params.get(away, (0.0, 0.0))
        return math.exp(self.c_home + ah + da) + math.exp(self.c_away + aa + dh)


def walk_forward_k1(frame: pd.DataFrame, start: pd.Timestamp, end: pd.Timestamp,
                    half_life: float, prior_matches: float, home_advantage: bool = True) -> pd.DataFrame:
    """K1 forecasts for every match dated in [start, end], each from matches on earlier days only."""
    model = _TeamRates(prior_matches, home_advantage)
    out = []
    for day in sorted(frame.date[(frame.date >= start) & (frame.date <= end)].unique()):
        day = pd.Timestamp(day)
        train = frame.loc[(frame.date < day) & (frame.date >= day - pd.Timedelta(days=WINDOW_DAYS))]
        w = _weights(train.date.to_numpy(), day, half_life)
        fitted = model.fit(train, w)
        alpha = _fit_alpha(train.total.to_numpy(), fitted, w)
        for m in frame.loc[frame.date == day].itertuples():
            mu = model.mean(m.HomeTeam, m.AwayTeam)
            out.append({'date': day, 'home_team': m.HomeTeam, 'away_team': m.AwayTeam, 'total': int(m.total),
                        'mu': mu, 'alpha': alpha})
    return pd.DataFrame(out)


def walk_forward_b0(frame: pd.DataFrame, start: pd.Timestamp, end: pd.Timestamp,
                    half_life: float = BASELINE_HALF_LIFE_DAYS) -> pd.DataFrame:
    """League-average forecasts for every match dated in [start, end], from earlier days only."""
    out = []
    for day in sorted(frame.date[(frame.date >= start) & (frame.date <= end)].unique()):
        day = pd.Timestamp(day)
        train = frame.loc[(frame.date < day) & (frame.date >= day - pd.Timedelta(days=WINDOW_DAYS))]
        w = _weights(train.date.to_numpy(), day, half_life)
        mu = float(np.average(train.total, weights=w))
        alpha = _fit_alpha(train.total.to_numpy(), np.full(len(train), mu), w)
        for m in frame.loc[frame.date == day].itertuples():
            out.append({'date': day, 'home_team': m.HomeTeam, 'away_team': m.AwayTeam, 'total': int(m.total),
                        'mu': mu, 'alpha': alpha})
    return pd.DataFrame(out)


# ---------------------------------------------------------------------------
# Scoring
# ---------------------------------------------------------------------------

def score(forecasts: pd.DataFrame) -> pd.DataFrame:
    """Per-fixture P(Over) at each main line, binary log loss, and count log loss."""
    out = forecasts.reset_index(drop=True).copy()
    mu, alpha = out.mu.to_numpy(float), out.alpha.to_numpy(float)
    total = out.total.to_numpy(int)
    r = 1.0 / alpha
    q = r / (r + mu)
    out['count_log_loss'] = -nbinom.logpmf(total, r, q)
    for line in MAIN_LINES:
        p = np.clip(1.0 - nbinom.cdf(math.floor(line), r, q), 1e-12, 1 - 1e-12)
        out[f'p_over_{line}'] = p
        out[f'll_{line}'] = -np.log(np.where(total > line, p, 1 - p))
    return out


def logistic_calibration(p, y) -> dict:
    """logit P(y) = a + b logit(p): intercept and slope by maximum likelihood."""
    p = np.clip(np.asarray(p, float), 1e-9, 1 - 1e-9)
    y = np.asarray(y, float)
    x = np.log(p / (1 - p))

    def nll(theta):
        z = theta[0] + theta[1] * x
        return float(np.sum(np.logaddexp(0, z) - y * z))
    result = minimize(nll, np.array([0.0, 1.0]), method='BFGS')
    return {'intercept': float(result.x[0]), 'slope': float(result.x[1])}


def band_check(p, y, min_n: int = 30, gap: float = 0.05, alpha: float = 0.05) -> dict:
    """Probability bands in tenths: a band fails if |gap| > 5 points and clear after Bonferroni (as v2)."""
    from scipy.stats import norm
    p, y = np.asarray(p, float), np.asarray(y, float)
    band = np.minimum((p * 10).astype(int), 9)
    checked = []
    for b in range(10):
        mask = band == b
        if mask.sum() >= min_n:
            checked.append((b, int(mask.sum()), float(p[mask].mean()), float(y[mask].mean())))
    bar = float(norm.ppf(1 - alpha / 2 / max(len(checked), 1)))
    bands = []
    for b, n, mp, obs in checked:
        z = abs(obs - mp) / math.sqrt(mp * (1 - mp) / n)
        bands.append({'band': f'{b / 10:.1f}-{(b + 1) / 10:.1f}', 'n': n, 'mean_forecast': mp, 'observed': obs,
                      'z': z, 'fails': bool(abs(obs - mp) > gap and z > bar)})
    return {'bands_checked': len(checked), 'z_bar': bar, 'failing': sum(b['fails'] for b in bands), 'bands': bands}


# ---------------------------------------------------------------------------
# Inputs tested on top of K1 (each from earlier matches only)
# ---------------------------------------------------------------------------

FORM_HALF_LIFE_MATCHES = 10   # as count_markets
FORM_PRIOR_MATCHES = 3.0
DC_STEP_DAYS = 14             # the harness's fold length
STAGE2_STEP_DAYS = 28
STAGE2_START = pd.Timestamp('2020-08-01')  # K1 forecasts from here train the second stage
STAGE2_L2 = 1.0

# Odds-free groups (the corner research view) and the market-informed groups, as stage-two columns.
INPUT_GROUPS = {
    'shots': ['shots_for_home', 'shots_against_home', 'shots_for_away', 'shots_against_away'],
    'shots_on_target': ['sot_for_home', 'sot_against_home', 'sot_for_away', 'sot_against_away'],
    'dc_xg_total': ['log_xg_total'],
    'dc_xg_per_side': ['log_xg_home', 'log_xg_away'],
    'match_balance_xgd': ['xgd', 'abs_xgd'],
    'elo_difference': ['elo_diff', 'abs_elo_diff'],
    'league': ['league_' + k for k in DIVISIONS if k != 'EPL'],
}
MARKET_GROUPS = {
    'market_1x2_and_ou25': ['logit_p_over25', 'p_home_minus_away', 'abs_p_home_minus_away'],
    'market_ou25_only': ['logit_p_over25'],
    'market_1x2_only': ['p_home_minus_away', 'abs_p_home_minus_away'],
}


def shot_form(frame: pd.DataFrame) -> pd.DataFrame:
    """Exponentially weighted shots and shots on target for and against, as log ratios to the league mean.

    `frame` needs date, HomeTeam, AwayTeam, HS, AS, HST, AST. Each calendar day's matches see only earlier
    days' results (as count_markets._Form)."""
    stats = ('shots_for', 'shots_against', 'sot_for', 'sot_against')
    decay = 0.5 ** (1 / FORM_HALF_LIFE_MATCHES)
    teams, league, rows = {}, dict.fromkeys(stats), {}
    observed = 0
    data = frame.assign(hs=pd.to_numeric(frame.HS, errors='coerce'), as_=pd.to_numeric(frame.AS, errors='coerce'),
                        hst=pd.to_numeric(frame.HST, errors='coerce'), ast=pd.to_numeric(frame.AST, errors='coerce'))

    def value(team, s):
        sums, weight = teams.get(team, (dict.fromkeys(stats, 0.), 0.))
        return (sums[s] + FORM_PRIOR_MATCHES * league[s]) / (weight + FORM_PRIOR_MATCHES)
    for _, day in data.groupby('date', sort=True):
        if league['shots_for']:
            for m in day.itertuples():
                rows[m.Index] = {f'{s}_{side}': math.log(max(value(team, s), 1e-6) / league[s])
                                 for side, team in (('home', m.HomeTeam), ('away', m.AwayTeam)) for s in stats}
        for m in day.itertuples():
            if any(pd.isna(v) for v in (m.hs, m.as_, m.hst, m.ast)):
                continue
            for team, vals in ((m.HomeTeam, (m.hs, m.as_, m.hst, m.ast)), (m.AwayTeam, (m.as_, m.hs, m.ast, m.hst))):
                sums, weight = teams.get(team, (dict.fromkeys(stats, 0.), 0.))
                teams[team] = ({s: decay * sums[s] + v for s, v in zip(stats, vals)}, decay * weight + 1)
                observed += 1
                rate = max(0.005, 1 / observed)
                for s, v in zip(stats, vals):
                    league[s] = v if league[s] is None else (1 - rate) * league[s] + rate * v
    return pd.DataFrame.from_dict(rows, orient='index').reindex(frame.index)


def dc_expected_goals(history: pd.DataFrame, origins, cfg) -> pd.DataFrame:
    """Dixon-Coles expected goals per match from the harness's fold fit (evaluation_harness.fold_model),
    refitted at each origin on matches before it; a match uses the latest origin on or before its date."""
    import evaluation_harness as eh
    data = history.copy()
    data['Date'] = pd.to_datetime(data['Date'], format='%d/%m/%Y')
    for c in ('FTHG', 'FTAG', 'HS', 'AS', 'HST', 'AST'):
        data[c] = pd.to_numeric(data[c], errors='coerce')
    done = data.dropna(subset=['FTHG', 'FTAG'])
    rows = []
    origins = list(origins)
    for origin, end in zip(origins, origins[1:]):
        test = data.loc[(data.Date >= origin) & (data.Date < end)]
        if test.empty:
            continue
        train = done.loc[(done.Date < origin) & (done.Date >= origin - pd.Timedelta(days=WINDOW_DAYS))]
        model = eh.fold_model(train, origin, cfg)
        for m in test.itertuples():
            xg = model.expected_goals(m.HomeTeam, m.AwayTeam)
            rows.append({'date': m.Date, 'HomeTeam': m.HomeTeam, 'AwayTeam': m.AwayTeam,
                         'xg_home': float(xg['lambda_home']), 'xg_away': float(xg['lambda_away'])})
    return pd.DataFrame(rows)


def elo_differences(history: pd.DataFrame) -> pd.DataFrame:
    """Pre-match Elo difference (home rating + home advantage - away rating), from elo_ratings unchanged."""
    import elo_ratings
    data = history.copy()
    data['FTHG'] = pd.to_numeric(data['FTHG'], errors='coerce')
    data['FTAG'] = pd.to_numeric(data['FTAG'], errors='coerce')
    data['Date'] = pd.to_datetime(data['Date'], format='%d/%m/%Y')
    ratings = elo_ratings.pre_match_ratings(data)
    return pd.DataFrame({'date': data.Date, 'HomeTeam': data.HomeTeam, 'AwayTeam': data.AwayTeam,
                         'elo_diff': pd.to_numeric(ratings['elo_rating_diff'], errors='coerce')})


def market_probabilities(history: pd.DataFrame) -> pd.DataFrame:
    """Pinnacle pre-match 1X2 and O/U 2.5, margin removed proportionally (market-informed variant only)."""
    num = {c: pd.to_numeric(history[c], errors='coerce') if c in history else pd.Series(np.nan, index=history.index)
           for c in ('PSH', 'PSD', 'PSA', 'P>2.5', 'P<2.5')}
    inv = {c: 1 / v.where(v > 1) for c, v in num.items()}
    s3 = inv['PSH'] + inv['PSD'] + inv['PSA']
    s2 = inv['P>2.5'] + inv['P<2.5']
    return pd.DataFrame({'date': pd.to_datetime(history.Date, format='%d/%m/%Y'), 'HomeTeam': history.HomeTeam,
                         'AwayTeam': history.AwayTeam, 'p_home': inv['PSH'] / s3, 'p_away': inv['PSA'] / s3,
                         'p_over25': inv['P>2.5'] / s2})


def input_columns(rows: pd.DataFrame) -> pd.DataFrame:
    """Derived stage-two columns from the raw inputs."""
    out = rows.copy()
    out['log_xg_total'] = np.log(out.xg_home + out.xg_away)
    out['log_xg_home'], out['log_xg_away'] = np.log(out.xg_home), np.log(out.xg_away)
    out['xgd'] = out.xg_home - out.xg_away
    out['abs_xgd'] = out.xgd.abs()
    out['elo_diff'] = out.elo_diff / 100.0
    out['abs_elo_diff'] = out.elo_diff.abs()
    for k in DIVISIONS:
        if k != 'EPL':
            out['league_' + k] = (out.league == k).astype(float)
    p = out.p_over25.clip(1e-6, 1 - 1e-6)
    out['logit_p_over25'] = np.log(p / (1 - p))
    out['p_home_minus_away'] = out.p_home - out.p_away
    out['abs_p_home_minus_away'] = out.p_home_minus_away.abs()
    return out


# ---------------------------------------------------------------------------
# Stage two: NB2 on top of a base forecast, pooled over leagues, walk-forward
# ---------------------------------------------------------------------------

def _fit_stage2(x, offset, y):
    from scipy.special import gammaln
    x = np.column_stack([np.ones(len(y)), x])

    def nll(theta):
        beta, r = theta[:-1], 1.0 / math.exp(theta[-1])
        mu = np.exp(np.clip(offset + x @ beta, -10, 10))
        ll = gammaln(y + r) - gammaln(r) - gammaln(y + 1) + r * np.log(r / (r + mu)) + y * np.log(mu / (r + mu))
        return -ll.sum() + STAGE2_L2 * float(beta[1:] @ beta[1:])
    start = np.zeros(x.shape[1] + 1)
    start[-1] = math.log(0.02)
    res = minimize(nll, start, method='L-BFGS-B',
                   bounds=[(None, None)] * x.shape[1] + [tuple(math.log(b) for b in ALPHA_BOUNDS)])
    return res.x[:-1], float(math.exp(res.x[-1]))


def walk_forward_stage2(rows: pd.DataFrame, columns, start: pd.Timestamp, end: pd.Timestamp,
                        base: str = 'mu_k1', step_days: int = STAGE2_STEP_DAYS) -> pd.DataFrame:
    """log mu = log base + b0 + b.x (x standardised on the training rows), refitted every `step_days` on
    rows dated before each origin; forecasts for rows dated in [start, end]. Rows missing a column are dropped."""
    columns = list(columns)
    data = rows.dropna(subset=[base, 'total'] + columns).sort_values('date', kind='stable')
    out = []
    for origin in pd.date_range(start, end + pd.Timedelta(days=1), freq=f'{step_days}D'):
        test = data.loc[(data.date >= origin) & (data.date < origin + pd.Timedelta(days=step_days))
                        & (data.date <= end)]
        if test.empty:
            continue
        train = data.loc[data.date < origin]
        xt = train[columns].to_numpy(float).reshape(len(train), len(columns))
        centre = xt.mean(0)
        scale = xt.std(0)
        scale[scale == 0] = 1.0
        beta, alpha = _fit_stage2((xt - centre) / scale, np.log(train[base].to_numpy(float)),
                                  train.total.to_numpy(float))
        xs = (test[columns].to_numpy(float).reshape(len(test), len(columns)) - centre) / scale
        mu = np.exp(np.log(test[base].to_numpy(float)) + beta[0] + xs @ beta[1:])
        out.append(test[['league', 'date', 'home_team', 'away_team', 'total']].assign(mu=mu, alpha=alpha))
    return pd.concat(out, ignore_index=True) if out else pd.DataFrame()
