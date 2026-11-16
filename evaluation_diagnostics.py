"""Standing diagnostics for the evaluation harness. Reporting only: never selects, stakes or changes a live number.

A locked harness run (`python evaluation_harness.py --output DIR`) writes `diagnostics.json` from its own
`fixture_scores.csv`, `forecasts_1x2.csv` and `diagnostic_fixtures.csv`. The same report is rebuilt from a
run's files, and saved with a readable copy, by

    python evaluation_diagnostics.py --run DIR --output evaluation/diagnostics

A holdout row anywhere aborts it: the diagnostics read development, validation and retrospective only.

Fixed on 15 Nov 2026 so that later candidates are judged against them (docs/plan.md, "How each change is
judged"). Everything is computed on the harness's common cohort (fixtures where C, C2, C3, C5, C6, M, D, A and
the two research baselines C0 and DC all exist), and every interval resamples whole calendar weeks.

  1. Research baselines: C0 (C without its form term) and DC (the fold model's own grid) beside C, C6 and M.
  2. Quote references, Pinnacle periods: the plain 1X2 quote de-vigged proportionally (QPROP) and by the
     power method (QPOW), beside M, on every match that has all three (no research view needed).
  3. Information test: p ~ M^a * R^b fitted by maximum likelihood on 1X2 for R = C, C6 and C0; a and b per
     period, and the gain over M on later periods with the development weights. Research passes only when b
     is positive with its interval clear of zero.
  4. Segment tables for the gap to M (1X2 and AH all lines): either team with fewer than 16 training matches
     against the rest; August-September against the rest; the favourite's market probability under 45%,
     45-60%, 60-75% and 75%+; and per league, with each league's sharpness (the t minimising the log loss of
     p^t, renormalised; above 1 means the forecasts are too flat).
  5. Flat-stake return at Pinnacle pre-match 1X2 prices by odds band (up to 1.3, 1.6, 2.0, 2.6, 3.5, 5.0,
     above): every quote backed, and for context each research view's positive-expected-return quotes.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd

VERSION = 'evaluation-diagnostics-v1'
DECLARED = '2026-11-15'
PHASES = ('development', 'validation', 'retrospective')
PERIODS = (('development', ('development',)), ('validation', ('validation',)), ('retrospective', ('retrospective',)),
           ('development+validation', ('development', 'validation')),
           ('validation+retrospective', ('validation', 'retrospective')))
PINNACLE_PERIODS = ('development', 'validation', 'development+validation')  # Pinnacle prices end 15 Jan 2026
COHORT = ('C', 'C2', 'C3', 'C5', 'C6', 'M', 'D', 'A', 'C0', 'DC')
GROUPS = ('1X2', 'Over 1.5', 'AH all', 'AH draw-sensitive')
BASELINE_TABLE = ('C', 'C6', 'C0', 'DC', 'M')
BASELINE_DIFFERENCES = (('C', 'C0'), ('C', 'DC'), ('C0', 'DC'), ('C6', 'C0'), ('C6', 'DC'),
                        ('C', 'M'), ('C6', 'M'), ('C0', 'M'), ('DC', 'M'))
RESEARCH_DIFFERENCES = tuple(pair for pair in BASELINE_DIFFERENCES if 'M' not in pair)
QUOTES = ('QPROP', 'QPOW')
QUOTE_DIFFERENCES = (('QPROP', 'M'), ('QPOW', 'M'), ('QPROP', 'QPOW'))
INFORMATION = ('C', 'C6', 'C0')  # the research views R of p ~ M^a * R^b
INFORMATION_FIT_PERIOD = 'development'
INFORMATION_LATER_PERIODS = ('validation', 'retrospective', 'validation+retrospective')
SEGMENT_CANDIDATES = ('C', 'C6', 'C0', 'DC')
SEGMENT_GROUPS = ('1X2', 'AH all')
MIN_TRAINING_MATCHES = 16
EARLY_SEASON_MONTHS = (8, 9)
FAVOURITE_BANDS = ((0., .45, 'under 45%'), (.45, .60, '45-60%'), (.60, .75, '60-75%'), (.75, 1.01, '75%+'))
ODDS_BANDS = (1.3, 1.6, 2.0, 2.6, 3.5, 5.0)
VALUE_PICK_CANDIDATES = ('C', 'C6', 'C0')
SAMPLES, SEED = 2000, 136  # week resampling, as evaluation_harness.paired
FIXTURE_COLUMNS = ['fixture_key', 'phase', 'league', 'date', 'week', 'home_training_matches',
                   'away_training_matches', 'pinnacle_home', 'pinnacle_draw', 'pinnacle_away']
PROBS = ['p_home', 'p_draw', 'p_away']


# ---------------------------------------------------------------------------
# Frames
# ---------------------------------------------------------------------------

def fixture_frame(calib) -> pd.DataFrame:
    """One row per scored fixture from the harness's calibration rows: C's row carries the fixture's date, week,
    each team's matches in the fold's training rows and, in Pinnacle periods, the Pinnacle 1X2 quote."""
    rows = []
    for r in calib:
        info = r.get('fixture')
        if info is None:
            continue
        home, draw, away = info.get('pinnacle_hda') or (np.nan, np.nan, np.nan)
        rows.append({'fixture_key': r['fixture_key'], 'phase': r['phase'], 'league': r['league'],
                     'date': info['date'], 'week': info['week'],
                     'home_training_matches': info['home_training_matches'],
                     'away_training_matches': info['away_training_matches'],
                     'pinnacle_home': home, 'pinnacle_draw': draw, 'pinnacle_away': away})
    return pd.DataFrame(rows, columns=FIXTURE_COLUMNS)


def cohort(scores, names=COHORT) -> pd.DataFrame:
    """The common cohort: fixtures where every named candidate has a 1X2 score. Indexed by fixture key, with
    the fixture's phase, league and week."""
    part = scores.loc[scores.group == '1X2']
    table = part.pivot(index='fixture_key', columns='candidate', values='log_loss')
    missing = [n for n in names if n not in table]
    if missing:
        raise ValueError('The run has no scores for ' + ', '.join(missing))
    keys = table[list(names)].dropna().index
    identity = part.drop_duplicates('fixture_key').set_index('fixture_key')[['phase', 'league', 'week']]
    return identity.loc[keys].sort_index()


def week_mean(values, weeks, samples=None, seed=SEED) -> dict:
    """Mean of `values` with a 95% interval that resamples whole calendar weeks (as evaluation_harness.paired)."""
    samples = samples or SAMPLES
    frame = pd.DataFrame({'value': np.asarray(values, float), 'week': np.asarray(weeks)}).dropna()
    if frame.empty:
        return {'n': 0, 'weeks': 0, 'mean': None, 'interval_95': None}
    by_week = frame.groupby('week').value.agg(['sum', 'count'])
    interval = None
    if len(by_week) >= 2:
        draws = np.random.default_rng(seed).integers(0, len(by_week), size=(samples, len(by_week)))
        means = by_week['sum'].to_numpy()[draws].sum(1) / by_week['count'].to_numpy()[draws].sum(1)
        interval = [float(v) for v in np.quantile(means, [.025, .975])]
    return {'n': int(len(frame)), 'weeks': int(len(by_week)), 'mean': float(frame.value.mean()),
            'interval_95': interval}


def period_keys(members):
    """(period, cohort fixture keys) for each period; a combined period only when each of its phases has fixtures."""
    for period, phases in PERIODS:
        if all((members.phase == phase).any() for phase in phases):
            yield period, members.index[members.phase.isin(phases)]


def _wide(scores, group) -> pd.DataFrame:
    return scores.loc[scores.group == group].pivot(index='fixture_key', columns='candidate', values='log_loss')


def _probabilities(forecasts, candidate) -> pd.DataFrame:
    part = forecasts.loc[forecasts.candidate == candidate]
    return part.set_index('fixture_key')[PROBS + ['outcome']]


# ---------------------------------------------------------------------------
# 1 and 2. Research baselines and quote references
# ---------------------------------------------------------------------------

def _differences(table, weeks, pairs) -> dict:
    """First minus second log loss for each pair (positive: the first-named is worse)."""
    return {f'{a}_minus_{b}': week_mean(table[a] - table[b], weeks) for a, b in pairs
            if a in table and b in table}


def baselines(scores, members) -> dict:
    """Mean log loss of C, C6, the research baselines C0 and DC, and M on the common cohort, per period and
    group, with paired differences. The research views need no market price, so their differences are also
    given on every fixture both views forecast (`research_differences_every_forecast`), a wider cohort."""
    wide = {group: _wide(scores, group) for group in GROUPS}
    everything = scores.drop_duplicates('fixture_key').set_index('fixture_key')[['phase', 'week']]
    every = dict(period_keys(everything))
    out = {}
    for period, keys in period_keys(members):
        entry = {'fixtures': int(len(keys))}
        for group in GROUPS:
            table = wide[group].reindex(keys)
            entry[group] = {'mean_log_loss': {c: float(table[c].mean()) for c in BASELINE_TABLE if c in table},
                            'differences': _differences(table, members.week.reindex(keys), BASELINE_DIFFERENCES),
                            'research_differences_every_forecast': _differences(
                                wide[group].reindex(every[period]), everything.week.reindex(every[period]),
                                RESEARCH_DIFFERENCES)}
        out[period] = entry
    return out


def quote_references(scores) -> dict:
    """1X2 log loss of the de-vigged Pinnacle quote (proportional and power) beside M, on every fixture that has
    M and both quote references (Pinnacle periods). A market-only comparison needs no research view, so this
    cohort is every priced match: slightly wider than the common cohort, which also needs C ... A."""
    part = scores.loc[scores.group == '1X2']
    table = part.pivot(index='fixture_key', columns='candidate', values='log_loss')
    out = {}
    if any(c not in table for c in (*QUOTES, 'M')):
        return out
    table = table.dropna(subset=[*QUOTES, 'M'])
    priced = part.drop_duplicates('fixture_key').set_index('fixture_key')[['phase', 'week']].loc[table.index]
    for period, keys in period_keys(priced):
        if period in PINNACLE_PERIODS:
            out[period] = {'fixtures': int(len(keys)),
                           'mean_log_loss': {c: float(table.loc[keys, c].mean()) for c in (*QUOTES, 'M')},
                           'differences': _differences(table.loc[keys], priced.week.loc[keys], QUOTE_DIFFERENCES)}
    return out


# ---------------------------------------------------------------------------
# 3. Information test: p ~ M^a * R^b
# ---------------------------------------------------------------------------

def fit_powers(logs, outcome, weights=None, start=None):
    """Maximum-likelihood exponents t of p_j ~ prod_k P_kj^t_k over the three outcomes (renormalised).

    `logs` is (matches, 3, K): the log probabilities of K forecasts; `outcome` the observed index. The log
    likelihood is concave in t, so Newton's method from `start` (default: the first forecast alone) finds its
    maximum. Returns None when it does not converge (collinear forecasts, or too few matches)."""
    logs = np.asarray(logs, float)
    n, _, k = logs.shape
    weights = np.ones(n) if weights is None else np.asarray(weights, float)
    observed = logs[np.arange(n), np.asarray(outcome, int)]  # (n, K)
    theta = np.array([1.] + [0.] * (k - 1)) if start is None else np.array(start, float)
    for _ in range(100):
        z = logs @ theta
        p = np.exp(z - z.max(axis=1, keepdims=True))
        p /= p.sum(axis=1, keepdims=True)
        mean = np.einsum('nj,njk->nk', p, logs)
        gradient = weights @ (observed - mean)
        hessian = np.einsum('n,nj,njk,njl->kl', weights, p, logs, logs) - (mean * weights[:, None]).T @ mean
        try:
            step = np.linalg.solve(hessian, gradient)
        except np.linalg.LinAlgError:
            return None
        if not np.isfinite(step).all() or np.abs(theta + step).max() > 50:
            return None
        theta = theta + step
        if np.abs(step).max() < 1e-10:
            return theta
    return None


def power_log_loss(logs, outcome, theta) -> np.ndarray:
    """Each match's log loss under p ~ prod_k P_k^t_k."""
    z = np.asarray(logs, float) @ np.asarray(theta, float)
    z = z - z.max(axis=1, keepdims=True)
    log_p = z - np.log(np.exp(z).sum(axis=1, keepdims=True))
    return -log_p[np.arange(len(z)), np.asarray(outcome, int)]


def _logs(*frames) -> np.ndarray:
    return np.stack([np.log(np.clip(f[PROBS].to_numpy(float), 1e-12, 1.)) for f in frames], axis=2)


def week_bootstrap_fits(logs, outcome, weeks, start, samples=None, seed=SEED):
    """fit_powers on whole calendar weeks resampled with replacement: 95% interval per exponent."""
    samples = samples or SAMPLES
    codes, labels = pd.factorize(np.asarray(weeks), sort=True)
    if len(labels) < 2:
        return None
    draws = np.random.default_rng(seed).integers(0, len(labels), size=(samples, len(labels)))
    fits = []
    for draw in draws:
        theta = fit_powers(logs, outcome, np.bincount(draw, minlength=len(labels))[codes].astype(float), start)
        if theta is not None:
            fits.append(theta)
    if len(fits) < .95 * samples:
        return None
    return [[float(v) for v in np.quantile(np.array(fits)[:, k], [.025, .975])] for k in range(logs.shape[2])]


def information_test(forecasts, members) -> dict:
    """p ~ M^a * R^b by maximum likelihood on 1X2, for each research view R: a and b per period (each fitted
    on that period), and the gain over M on the later periods with the development weights.

    a alone sharpens or flattens M; b is what R adds to M. Research passes only when b is positive with its
    week-resampled 95% interval clear of zero. The later-period gain is split into what a alone gives (M^a
    fitted on development with b = 0) and what R adds beyond it."""
    market = _probabilities(forecasts, 'M')
    out = {}
    for name in INFORMATION:
        research = _probabilities(forecasts, name)
        if research.empty or market.empty:
            continue
        data = {}
        for period, keys in period_keys(members):
            keys = keys[keys.isin(market.index) & keys.isin(research.index)]
            if len(keys):
                m = market.loc[keys]
                data[period] = (_logs(m, research.loc[keys]), m.outcome.to_numpy(int), members.week.loc[keys].to_numpy())
        entry = {'by_period': {}, 'with_development_weights': {}}
        fitted = {}
        for period, (logs, outcome, weeks) in data.items():
            theta = fit_powers(logs, outcome)
            alone = fit_powers(logs[:, :, :1], outcome)
            row = {'fixtures': int(len(outcome)), 'weeks': int(len(set(weeks))), 'a': None, 'b': None,
                   'a_interval_95': None, 'b_interval_95': None, 'b_positive_and_clear_of_zero': False,
                   'market_only_a': None if alone is None else float(alone[0])}
            if theta is not None:
                intervals = week_bootstrap_fits(logs, outcome, weeks, theta)
                base = power_log_loss(logs, outcome, [1., 0.])
                row.update(a=float(theta[0]), b=float(theta[1]),
                           a_interval_95=intervals[0] if intervals else None,
                           b_interval_95=intervals[1] if intervals else None,
                           b_positive_and_clear_of_zero=bool(intervals and intervals[1][0] > 0),
                           in_sample_gain_over_M=float((base - power_log_loss(logs, outcome, theta)).mean()))
                fitted[period] = (theta, alone)
            entry['by_period'][period] = row
        if INFORMATION_FIT_PERIOD in fitted:
            theta, alone = fitted[INFORMATION_FIT_PERIOD]
            entry['development_weights'] = {'a': float(theta[0]), 'b': float(theta[1]),
                                            'market_only_a': None if alone is None else float(alone[0])}
            for period in INFORMATION_LATER_PERIODS:
                if period not in data:
                    continue
                logs, outcome, weeks = data[period]
                base = power_log_loss(logs, outcome, [1., 0.])
                blend = power_log_loss(logs, outcome, theta)
                gains = {'fixtures': int(len(outcome)), 'gain_over_M': week_mean(base - blend, weeks)}
                if alone is not None:
                    sharpened = power_log_loss(logs, outcome, [alone[0], 0.])
                    gains['market_only_gain_over_M'] = week_mean(base - sharpened, weeks)
                    gains['research_gain_beyond_market_only'] = week_mean(sharpened - blend, weeks)
                entry['with_development_weights'][period] = gains
        entry['passes'] = bool(entry['by_period'].get(INFORMATION_FIT_PERIOD, {}).get('b_positive_and_clear_of_zero'))
        out[name] = entry
    return out


# ---------------------------------------------------------------------------
# 4. Segment tables for the gap to M
# ---------------------------------------------------------------------------

def sharpness(probabilities) -> float | None:
    """The t minimising the 1X2 log loss of p^t (renormalised): above 1, the forecasts are too flat."""
    if len(probabilities) < 2:
        return None
    theta = fit_powers(_logs(probabilities), probabilities.outcome.to_numpy(int))
    return None if theta is None else float(theta[0])


def favourite_band(probability) -> str:
    return next(label for low, high, label in FAVOURITE_BANDS if low <= probability < high)


def segment_labels(members, fixtures, forecasts) -> pd.DataFrame:
    """Each cohort fixture's segment in every pre-declared dimension."""
    info = fixtures.set_index('fixture_key').reindex(members.index)
    market = _probabilities(forecasts, 'M').reindex(members.index)
    fewest = info[['home_training_matches', 'away_training_matches']].min(axis=1)
    month = pd.to_datetime(info.date).dt.month
    labels = pd.DataFrame(index=members.index)
    labels['training matches'] = np.where(fewest < MIN_TRAINING_MATCHES,
                                          f'either team under {MIN_TRAINING_MATCHES}',
                                          f'both teams {MIN_TRAINING_MATCHES} or more')
    labels['month'] = np.where(month.isin(EARLY_SEASON_MONTHS), 'August-September', 'rest of the season')
    if info.date.isna().any() or market.p_home.isna().any():
        raise ValueError('A cohort fixture has no diagnostic fixture row or no market forecast')
    labels['favourite market probability'] = market[['p_home', 'p_away']].max(axis=1).map(favourite_band)
    labels['league'] = members.league
    return labels


SEGMENT_ORDER = {'training matches': (f'either team under {MIN_TRAINING_MATCHES}',
                                      f'both teams {MIN_TRAINING_MATCHES} or more'),
                 'month': ('August-September', 'rest of the season'),
                 'favourite market probability': tuple(label for _, _, label in FAVOURITE_BANDS)}


def segments(scores, forecasts, fixtures, members) -> dict:
    """Candidate minus M log loss (positive: behind the market) on 1X2 and AH all lines, per period and
    pre-declared segment; per league also each view's sharpness."""
    labels = segment_labels(members, fixtures, forecasts)
    wide = {group: _wide(scores, group) for group in SEGMENT_GROUPS}
    probabilities = {c: _probabilities(forecasts, c) for c in (*SEGMENT_CANDIDATES, 'M')}
    out = {}
    for phase in PHASES:
        inside = members.index[members.phase == phase]
        if not len(inside):
            continue

        def gap(keys):
            weeks = members.week.reindex(keys)
            return {cand: {group: week_mean(wide[group][cand].reindex(keys) - wide[group]['M'].reindex(keys), weeks)
                           for group in SEGMENT_GROUPS} for cand in SEGMENT_CANDIDATES}

        entry = {'all': {'fixtures': int(len(inside)), 'gap_to_M': gap(inside)}}
        for dimension in labels.columns:
            values = labels.loc[inside, dimension]
            order = SEGMENT_ORDER.get(dimension) or tuple(sorted(values.unique()))
            rows = []
            for label in order:
                keys = inside[(values == label).to_numpy()]
                row = {'segment': label, 'fixtures': int(len(keys)), 'gap_to_M': gap(keys) if len(keys) else None}
                if dimension == 'league':
                    row['sharpness'] = {c: sharpness(p.reindex(keys).dropna()) for c, p in probabilities.items()}
                rows.append(row)
            entry[dimension] = rows
        out[phase] = entry
    return out


# ---------------------------------------------------------------------------
# 5. Flat-stake return at Pinnacle 1X2 prices by odds band
# ---------------------------------------------------------------------------

def odds_band(odds) -> str:
    index = int(np.searchsorted(ODDS_BANDS, odds, side='left'))
    if index == 0:
        return f'up to {ODDS_BANDS[0]:.2f}'
    if index == len(ODDS_BANDS):
        return f'above {ODDS_BANDS[-1]:.2f}'
    return f'{ODDS_BANDS[index - 1]:.2f}-{ODDS_BANDS[index]:.2f}'


BAND_ORDER = tuple(dict.fromkeys(odds_band(v) for v in (*ODDS_BANDS, ODDS_BANDS[-1] + 1)))


def quote_bets(forecasts, fixtures, members) -> pd.DataFrame:
    """One flat-stake bet per Pinnacle 1X2 quote of every cohort fixture that has one: its price, band, result
    and return, with each research view's probability for the quoted outcome."""
    info = fixtures.set_index('fixture_key').reindex(members.index).dropna(subset=['pinnacle_home'])
    market = _probabilities(forecasts, 'M').reindex(info.index)
    views = {c: _probabilities(forecasts, c).reindex(info.index) for c in VALUE_PICK_CANDIDATES}
    parts = []
    for k, side in enumerate(('home', 'draw', 'away')):
        odds = info['pinnacle_' + side].to_numpy(float)
        won = market.outcome.to_numpy() == k
        part = pd.DataFrame({'fixture_key': info.index, 'phase': members.phase.reindex(info.index).to_numpy(),
                             'week': members.week.reindex(info.index).to_numpy(), 'selection': side,
                             'odds': odds, 'won': won, 'return': np.where(won, odds - 1, -1.)})
        for c, view in views.items():
            part['p_' + c] = view['p_' + side].to_numpy(float)
        parts.append(part)
    bets = pd.concat(parts, ignore_index=True) if parts else pd.DataFrame()
    if len(bets):
        bets['band'] = bets.odds.map(odds_band)
    return bets


def band_table(bets) -> list:
    rows = []
    for band in (*BAND_ORDER, 'all'):
        part = bets if band == 'all' else bets.loc[bets.band == band]
        result = week_mean(part['return'], part.week) if len(part) else week_mean([], [])
        rows.append({'band': band, 'bets': int(len(part)), 'fixtures': int(part.fixture_key.nunique()),
                     'weeks': result['weeks'], 'mean_odds': float(part.odds.mean()) if len(part) else None,
                     'mean_quoted_probability': float((1 / part.odds).mean()) if len(part) else None,
                     'win_rate': float(part.won.mean()) if len(part) else None,
                     'return_per_bet': result['mean'], 'interval_95': result['interval_95']})
    return rows


def odds_bands(forecasts, fixtures, members) -> dict:
    """Flat-stake return per bet at the Pinnacle pre-match 1X2 price, by odds band, with week-resampled 95%
    intervals: every quote backed (the market's own favourite-longshot pattern, the bar any pick must beat),
    and, for context, the quotes each research view gives a positive expected return (p x odds > 1)."""
    bets = quote_bets(forecasts, fixtures, members)
    out = {}
    if bets.empty:
        return out
    for period, keys in period_keys(members):
        if period not in PINNACLE_PERIODS:
            continue
        part = bets.loc[bets.fixture_key.isin(keys)]
        if part.empty:
            continue
        out[period] = {'fixtures': int(part.fixture_key.nunique()), 'every_quote': band_table(part),
                       'positive_expected_return_quotes': {
                           c: band_table(part.loc[part['p_' + c] * part.odds > 1]) for c in VALUE_PICK_CANDIDATES}}
    return out


# ---------------------------------------------------------------------------
# Report
# ---------------------------------------------------------------------------

def report(scores, forecasts, fixtures) -> dict:
    """All five harness diagnostics from one locked run's frames."""
    for name, frame in (('scores', scores), ('forecasts', forecasts), ('fixtures', fixtures)):
        if (frame.phase == 'holdout').any():
            raise ValueError(f'Holdout rows found in the {name}; the diagnostics read locked runs only')
    members = cohort(scores)
    return {
        'version': VERSION, 'declared': DECLARED,
        'definitions': {
            'cohort': 'fixtures where ' + ', '.join(COHORT) + ' all have a score',
            'quote_reference_cohort': 'every fixture with M and both quote references (no research view needed)',
            'intervals': f'whole calendar weeks resampled, {SAMPLES} draws, seed {SEED}, 95%',
            'differences': 'X_minus_Y is X minus Y log loss: positive means X is worse',
            'information_test': 'p ~ M^a * R^b, maximum likelihood on 1X2; passes only when b on development is '
                                'positive with its interval clear of zero',
            'segments': {'training matches': f'either team with fewer than {MIN_TRAINING_MATCHES} matches in the '
                                             "fold's training rows, against the rest",
                         'month': 'kickoff in August or September, against the rest',
                         'favourite market probability': "the larger of M's home and away probability: "
                                                         + ', '.join(label for _, _, label in FAVOURITE_BANDS),
                         'league': 'each league; sharpness is the t minimising the 1X2 log loss of p^t'},
            'odds_bands': list(ODDS_BANDS)},
        'cohort': {phase: int((members.phase == phase).sum()) for phase in PHASES if (members.phase == phase).any()},
        'baselines': baselines(scores, members),
        'quote_references': quote_references(scores),
        'information_test': information_test(forecasts, members),
        'segments': segments(scores, forecasts, fixtures, members),
        'odds_bands': odds_bands(forecasts, fixtures, members),
        'notes': ['Reporting only: nothing here selects, stakes or changes a live probability.',
                  'No holdout row is read. Validation and retrospective were already inspected; they are '
                  'diagnostics, never release evidence.',
                  'The retrospective market reference is Bet365 with the margin removed, not Pinnacle.',
                  'Historical prices are pre-match snapshots without timestamps; returns are not claimed as '
                  'achievable.'],
    }


def from_run(run) -> dict:
    """The diagnostics of a locked harness run directory, from the files the run wrote."""
    run = Path(run)
    return report(pd.read_csv(run / 'fixture_scores.csv'), pd.read_csv(run / 'forecasts_1x2.csv'),
                  pd.read_csv(run / 'diagnostic_fixtures.csv'))


def write_json(path, data) -> None:
    Path(path).write_text(json.dumps(data, indent=2, sort_keys=True, allow_nan=False) + '\n', encoding='utf-8',
                          newline='\n')


# ---------------------------------------------------------------------------
# Readable copy
# ---------------------------------------------------------------------------

def _f(value, spec='.4f') -> str:
    return 'n/a' if value is None else format(value, spec)


def _ci(result, spec='+.4f') -> str:
    if not result or result.get('mean') is None:
        return 'n/a'
    interval = result.get('interval_95')
    return format(result['mean'], spec) + (f" ({format(interval[0], spec)} to {format(interval[1], spec)})"
                                           if interval else '')


def _table(header, rows) -> list:
    return ['| ' + ' | '.join(header) + ' |', '|' + '---|' * len(header),
            *('| ' + ' | '.join(str(c) for c in row) + ' |' for row in rows), '']


def markdown(data) -> str:
    """The readable copy of the report."""
    lines = ['# Evaluation harness diagnostics', '',
             f"Run at commit `{data.get('source_commit', 'unknown')}`; definitions fixed on {data['declared']} "
             f"({data['version']}). Reporting only: nothing here changes a live probability, pick or stake. "
             'No holdout row is read.', '',
             'Common cohort (fixtures where ' + ', '.join(COHORT) + ' all exist): '
             + ', '.join(f'{phase} {n:,}' for phase, n in data['cohort'].items()) + '. '
             'Intervals are 95%, whole calendar weeks resampled. A difference "X minus Y" is in log loss: '
             'positive means X is worse.', '']

    lines += ['## 1. Research baselines', '',
              'C0 is C without its last-ten form term (independent Poisson on the Dixon-Coles goal rates); DC is '
              "the fold model's own Dixon-Coles grid.", '']
    for group in ('1X2', 'AH all'):
        lines += [f'### {group} log loss', '']
        lines += _table(['Period', 'Fixtures', *BASELINE_TABLE, 'C minus C0', 'C minus DC', 'C6 minus C0',
                         'C6 minus DC'],
                        [[period, f"{e['fixtures']:,}", *(_f(e[group]['mean_log_loss'].get(c)) for c in BASELINE_TABLE),
                          *(_ci(e[group]['differences'].get(k)) for k in
                            ('C_minus_C0', 'C_minus_DC', 'C6_minus_C0', 'C6_minus_DC'))]
                         for period, e in data['baselines'].items()])

    lines += ['### Research views on every match both forecast (1X2)', '',
              'The research views need no price, so the same differences are also taken on every match both '
              'views forecast (n in brackets), a wider cohort than the common one.', '']
    lines += _table(['Period', 'C minus C0', 'C minus DC', 'C6 minus C0', 'C6 minus DC'],
                    [[period, *(_ci(d) + f" [n={d['n']:,}]" for d in
                                (e['1X2']['research_differences_every_forecast'][k]
                                 for k in ('C_minus_C0', 'C_minus_DC', 'C6_minus_C0', 'C6_minus_DC')))]
                     for period, e in data['baselines'].items()])
    lines += ['## 2. Quote references (Pinnacle periods, 1X2)', '',
              'The plain Pinnacle 1X2 quote with the margin removed proportionally (QPROP) and by the power '
              'method (QPOW), beside M (the grid fitted to 1X2, totals and the main AH line). Cohort: every match '
              'with M and both quote references, which needs no research view and so is slightly wider than '
              'the common cohort.', '']
    lines += _table(['Period', 'Fixtures', 'QPROP', 'QPOW', 'M', 'QPROP minus M', 'QPOW minus M', 'QPROP minus QPOW'],
                    [[period, f"{e['fixtures']:,}", *(_f(e['mean_log_loss'][c]) for c in (*QUOTES, 'M')),
                      *(_ci(e['differences'][k], '+.5f') for k in ('QPROP_minus_M', 'QPOW_minus_M', 'QPROP_minus_QPOW'))]
                     for period, e in data['quote_references'].items()])

    lines += ['## 3. Information test: p ~ M^a x R^b', '',
              'Fitted by maximum likelihood on 1X2. a alone sharpens (above 1) or flattens M; b is what the '
              'research view R adds to M. **Research passes only when b is positive with its interval clear of '
              'zero** (development fit).', '']
    rows = []
    for name, e in data['information_test'].items():
        for period, r in e['by_period'].items():
            rows.append([name, period, f"{r['fixtures']:,}",
                         _ci({'mean': r['a'], 'interval_95': r['a_interval_95']}, '.3f'),
                         _ci({'mean': r['b'], 'interval_95': r['b_interval_95']}, '+.3f'),
                         _f(r['market_only_a'], '.3f'),
                         'yes' if r['b_positive_and_clear_of_zero'] else 'no'])
    lines += _table(['R', 'Period (fitted on it)', 'Fixtures', 'a', 'b', 'a with b = 0', 'b positive and clear'], rows)
    lines += ['Verdict (development): ' + '; '.join(
        f"{name} {'passes' if e['passes'] else 'does not pass'}" for name, e in data['information_test'].items())
              + '.', '',
              'Later periods with the development weights (gain = M minus the blend, positive: the blend is '
              'better). "a alone" is M^a with the development a fitted at b = 0; "R beyond a alone" is what '
              'the research view adds to it.', '']
    rows = []
    for name, e in data['information_test'].items():
        for period, g in e['with_development_weights'].items():
            rows.append([name, period, f"{g['fixtures']:,}", _ci(g['gain_over_M'], '+.5f'),
                         _ci(g.get('market_only_gain_over_M'), '+.5f'),
                         _ci(g.get('research_gain_beyond_market_only'), '+.5f')])
    lines += _table(['R', 'Period', 'Fixtures', 'Gain over M', 'a alone', 'R beyond a alone'], rows)

    lines += ['## 4. Segments: gap to M', '',
              'Candidate minus M log loss (positive: behind the market). Segments were fixed before this run.', '']
    for phase, e in data['segments'].items():
        for group in SEGMENT_GROUPS:
            rows = [['all', 'all', f"{e['all']['fixtures']:,}",
                     *(_ci(e['all']['gap_to_M'][c][group]) for c in SEGMENT_CANDIDATES)]]
            for dimension in ('training matches', 'month', 'favourite market probability', 'league'):
                for r in e[dimension]:
                    rows.append([dimension, r['segment'], f"{r['fixtures']:,}",
                                 *(_ci(r['gap_to_M'][c][group]) if r['gap_to_M'] else 'n/a'
                                   for c in SEGMENT_CANDIDATES)])
            lines += [f'### {phase.capitalize()}: {group}', '']
            lines += _table(['Dimension', 'Segment', 'Fixtures', *SEGMENT_CANDIDATES], rows)
        lines += [f'### {phase.capitalize()}: sharpness by league', '',
                  'The t minimising the 1X2 log loss of p^t: above 1 the forecasts are too flat, below 1 too sharp.', '']
        lines += _table(['League', 'Fixtures', *SEGMENT_CANDIDATES, 'M'],
                        [[r['segment'], f"{r['fixtures']:,}", *(_f(r['sharpness'][c], '.2f')
                                                                for c in (*SEGMENT_CANDIDATES, 'M'))]
                         for r in e['league']])

    lines += ['## 5. Flat-stake return at Pinnacle 1X2 prices by odds band', '',
              'One unit on every Pinnacle pre-match 1X2 quote (three per match). Prices are untimestamped '
              'pre-match snapshots: this is the market\'s own pattern by price, not an achievable return.', '']
    for period, e in data['odds_bands'].items():
        lines += [f"### {period.capitalize()} ({e['fixtures']:,} fixtures): every quote", '']
        lines += _table(['Odds band', 'Bets', 'Mean odds', 'Quoted probability', 'Win rate', 'Return per bet'],
                        [[r['band'], f"{r['bets']:,}", _f(r['mean_odds'], '.2f'), _f(r['mean_quoted_probability'], '.1%'),
                          _f(r['win_rate'], '.1%'), _ci({'mean': r['return_per_bet'], 'interval_95': r['interval_95']}, '+.1%')]
                         for r in e['every_quote']])
        lines += [f'### {period.capitalize()}: quotes a research view gives a positive expected return', '',
                  'Context for judging picks: p x odds above 1 under each view, bets and return per bet.', '']
        picks = e['positive_expected_return_quotes']
        lines += _table(['Odds band', *VALUE_PICK_CANDIDATES],
                        [[band, *(f"{r['bets']:,}: " + _ci({'mean': r['return_per_bet'], 'interval_95': r['interval_95']}, '+.1%')
                                  for r in (next(x for x in picks[c] if x['band'] == band) for c in VALUE_PICK_CANDIDATES))]
                         for band in (*BAND_ORDER, 'all')])
    lines += ['## Notes', '', *('- ' + note for note in data['notes']), '']
    return '\n'.join(lines)


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('--run', type=Path, required=True, help='A locked harness run directory')
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args(argv)
    results = json.loads((args.run / 'results.json').read_text(encoding='utf-8'))
    if results.get('mode') != 'historical':
        raise ValueError('Expected a locked historical run')
    data = {**from_run(args.run), 'source_commit': results.get('source_commit'),
            'harness_version': results.get('version'), 'config_sha256': results.get('config_sha256')}
    args.output.mkdir(parents=True, exist_ok=True)
    write_json(args.output / 'summary.json', data)
    (args.output / 'report.md').write_text(markdown(data), encoding='utf-8', newline='\n')
    for group in ('1X2', 'AH all'):
        for period, e in data['baselines'].items():
            print(period, group, e['fixtures'], {c: round(v, 4) for c, v in e[group]['mean_log_loss'].items()},
                  'C-C0', _ci(e[group]['differences'].get('C_minus_C0')))
    for period, e in data['quote_references'].items():
        print(period, 'quotes', e['fixtures'], {c: round(v, 4) for c, v in e['mean_log_loss'].items()})
    for name, e in data['information_test'].items():
        for period, r in e['by_period'].items():
            print(name, period, 'a', _f(r['a'], '.3f'), 'b', _f(r['b'], '+.3f'), r['b_interval_95'])
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
