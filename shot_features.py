"""Lagged Football-Data shot strengths blended into Dixon-Coles goal rates.

No API calls. Shots (HST/AST, optionally HS/AS) from a match only inform
matches on LATER dates; same-day results are excluded because the CSV dates
carry no kickoff time. Each fit re-runs a chronological audit with the gate
thresholds below and keeps pure Dixon-Coles unless every gate passes, so a
league's feature switches on or off per run with a logged reason.

The gate thresholds and the scoring helpers came from the BBS statistics
model, retired on 25 Nov 2026; they are unchanged.
"""
from __future__ import annotations

import math

import numpy as np
import pandas as pd


VERSION = 'football-data-lagged-shot-strength-v1'
SHRINKAGE = (5., 15., 40.)  # prior match-equivalents pulling teams to league average
COMPONENTS = ('shots_on_target', 'shots_on_target_and_total_shots')
TUNE_DAYS = 182
AUDIT_DAYS = 182
STEP_DAYS = 28
ITERATIONS = 8
COLUMNS = ('Date', 'HomeTeam', 'AwayTeam', 'FTHG', 'FTAG', 'HST', 'AST', 'HS', 'AS')
# Gates (unchanged from the retired BBS statistics model, whose thresholds this audit always used).
MIN_FORM = 3
MIN_TRAIN = 60
MIN_TUNE = 20
MIN_AUDIT = 40
MIN_AUDIT_DATES = 8
WEIGHTS = (.1, .2, .3)
MAX_RATE_RATIO = 1.25
MIN_AUDIT_GAIN = .01


def mix_rates(base, extra, weight):
    mixed = (1-weight)*np.asarray(base)+weight*np.asarray(extra)
    return np.clip(mixed, np.asarray(base)/MAX_RATE_RATIO, np.asarray(base)*MAX_RATE_RATIO)


def poisson_score(y, rates):
    return float(np.mean(rates-y*np.log(np.maximum(rates, 1e-12))))


def market_briers(y, rates, rho, minimum):
    from score_probability import score_grid
    scores = []
    for (h, a), (lam, mu), correction in zip(y, rates, rho):
        matrix, _ = score_grid(float(lam), float(mu), correction, minimum)
        hda = np.array([np.tril(matrix, -1).sum(), np.trace(matrix), np.triu(matrix, 1).sum()])
        target = int(0 if h > a else 1 if h == a else 2)
        home, away = np.indices(matrix.shape)
        scores.append([np.sum((hda-np.eye(3)[target])**2),
            (matrix[home+away >= 2].sum()-int(h+a >= 2))**2,
            (matrix[home+away <= 3].sum()-int(h+a <= 3))**2,
            (matrix[1:, 1:].sum()-int(h > 0 and a > 0))**2])
    return np.mean(scores, axis=0)


def day(value):
    stamp = pd.Timestamp(value)
    if pd.isna(stamp):
        raise ValueError('Invalid shot-feature date')
    if stamp.tzinfo is not None:
        stamp = stamp.tz_convert('UTC').tz_localize(None)
    return stamp.normalize()


def shot_table(history):
    """Completed rows with coherent non-negative integer shot counts only."""
    if 'HST' not in history or 'AST' not in history:
        return pd.DataFrame(columns=COLUMNS)
    frame = history.reindex(columns=COLUMNS).copy()
    for column in ('FTHG', 'FTAG', 'HST', 'AST', 'HS', 'AS'):
        frame[column] = pd.to_numeric(frame[column], errors='coerce')
    valid = frame[['FTHG', 'FTAG', 'HST', 'AST']].notna().all(axis=1)
    counts = frame[['HST', 'AST']]
    valid &= (counts >= 0).all(axis=1) & (counts % 1 == 0).all(axis=1)
    for part, total in (('HST', 'HS'), ('AST', 'AS')):
        valid &= frame[total].isna() | (frame[total] >= frame[part])
    frame = frame.loc[valid].copy()
    frame['Date'] = pd.to_datetime(frame['Date']).map(day)
    return frame.sort_values(['Date', 'HomeTeam', 'AwayTeam'], kind='stable').reset_index(drop=True)


class ShotStrengths:
    """Team attack/defence multipliers estimated strictly before ``origin``."""

    def __init__(self, table, origin, half_life_days, shrinkage, component):
        if component not in COMPONENTS or not shrinkage > 0 or not half_life_days > 0:
            raise ValueError('Invalid shot-strength settings')
        self.origin = day(origin)
        past = table.loc[table['Date'] < self.origin]
        self.matches = len(past)
        self.counts = pd.concat([past['HomeTeam'], past['AwayTeam']]).value_counts().to_dict()
        self.ready = len(past) >= MIN_FORM
        if not self.ready:
            return
        age = (self.origin - past['Date']).dt.days.to_numpy(dtype=float)
        w = np.exp(-math.log(2.) * age / half_life_days)
        sot = self._strengths(past, w, 'HST', 'AST', shrinkage)
        if component == 'shots_on_target_and_total_shots' and past[['HS', 'AS']].notna().all(axis=1).sum() >= MIN_FORM:
            both = past[['HS', 'AS']].notna().all(axis=1).to_numpy()
            shots = self._strengths(past.loc[both], w[both], 'HS', 'AS', shrinkage)
            self.attack = {t: math.sqrt(sot[0][t] * shots[0].get(t, 1.)) for t in sot[0]}
            self.defence = {t: math.sqrt(sot[1][t] * shots[1].get(t, 1.)) for t in sot[1]}
        else:
            self.attack, self.defence = sot
        hst, ast = past['HST'].to_numpy(float), past['AST'].to_numpy(float)
        self.home_mean, self.away_mean = float(w @ hst / w.sum()), float(w @ ast / w.sum())
        # Goals per shot on target; league level so team finishing is not double counted.
        self.home_conversion = float(w @ past['FTHG'].to_numpy(float) / max(w @ hst, 1e-9))
        self.away_conversion = float(w @ past['FTAG'].to_numpy(float) / max(w @ ast, 1e-9))
        if min(self.home_mean, self.away_mean, self.home_conversion, self.away_conversion) <= 0:
            self.ready = False

    @staticmethod
    def _strengths(past, w, home_col, away_col, shrinkage):
        teams = sorted(set(past['HomeTeam']) | set(past['AwayTeam']))
        index = {t: i for i, t in enumerate(teams)}
        hi = past['HomeTeam'].map(index).to_numpy(int)
        ai = past['AwayTeam'].map(index).to_numpy(int)
        hs, as_ = past[home_col].to_numpy(float), past[away_col].to_numpy(float)
        mh, ma = float(w @ hs / w.sum()), float(w @ as_ / w.sum())
        prior = shrinkage * (mh + ma) / 2
        attack, defence = np.ones(len(teams)), np.ones(len(teams))
        for _ in range(ITERATIONS):
            # Opponent-adjusted ratios, shrunk toward 1 by `shrinkage` matches.
            scored = np.bincount(hi, w * hs, len(teams)) + np.bincount(ai, w * as_, len(teams))
            expected = (np.bincount(hi, w * mh * defence[ai], len(teams))
                        + np.bincount(ai, w * ma * defence[hi], len(teams)))
            attack = (scored + prior) / (expected + prior)
            conceded = np.bincount(hi, w * as_, len(teams)) + np.bincount(ai, w * hs, len(teams))
            expected = (np.bincount(hi, w * ma * attack[ai], len(teams))
                        + np.bincount(ai, w * mh * attack[hi], len(teams)))
            defence = (conceded + prior) / (expected + prior)
        return dict(zip(teams, attack.tolist())), dict(zip(teams, defence.tolist()))

    def rates(self, home, away):
        if not self.ready or min(self.counts.get(home, 0), self.counts.get(away, 0)) < MIN_FORM:
            return None
        lam = self.home_conversion * self.home_mean * self.attack[home] * self.defence[away]
        mu = self.away_conversion * self.away_mean * self.attack[away] * self.defence[home]
        return np.array([lam, mu])


class ShotModel:
    def __init__(self, cutoff, half_life_days):
        self.cutoff = day(cutoff)
        self.half_life_days = float(half_life_days)
        self.strengths = None
        self.weight = 0.
        self.report = {'version': VERSION, 'status': 'NO_SHOT_DATA',
            'cutoff_date': self.cutoff.date().isoformat(), 'selected_weight': 0.,
            'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)',
            'lag_rule': 'matches dated strictly before the origin date',
            'gates': {'min_form': MIN_FORM, 'min_train': MIN_TRAIN, 'min_tune': MIN_TUNE,
                      'min_audit': MIN_AUDIT, 'min_audit_matchdays': MIN_AUDIT_DATES,
                      'min_audit_gain': MIN_AUDIT_GAIN, 'bootstrap_lower95': '>0',
                      'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'],
                      'max_goal_rate_ratio': MAX_RATE_RATIO}}

    def apply(self, home, away, base):
        info = {'shot_features_applied': False, 'shot_features_version': VERSION,
                'shot_features_status': self.report['status'], 'shot_features_weight': 0.}
        if self.strengths is None:
            return np.asarray(base), info
        extra = self.strengths.rates(home, away)
        if extra is None:
            info['shot_features_status'] = 'INSUFFICIENT_TEAM_SHOT_HISTORY'
            return np.asarray(base), info
        info.update(shot_features_applied=True, shot_features_status='APPLIED',
                    shot_features_weight=self.weight,
                    shot_lambda_home=float(extra[0]), shot_lambda_away=float(extra[1]))
        return mix_rates(base, extra, self.weight), info


def _walk(history, history_days, table, start, stop, baseline_factory, half_life):
    """Frozen-at-origin examples in [start, stop): DC base and every candidate."""
    examples = []
    for origin in pd.date_range(start, stop, freq=f'{STEP_DAYS}D'):
        end = min(origin + pd.Timedelta(days=STEP_DAYS), stop)
        test = table.loc[(table['Date'] >= origin) & (table['Date'] < end)]
        if test.empty:
            continue
        past = history.loc[history_days < origin]
        model = baseline_factory(past, origin)
        candidates = {(k, c): ShotStrengths(table, origin, half_life, k, c)
                      for k in SHRINKAGE for c in COMPONENTS}
        for row in test.itertuples(index=False):
            if row.HomeTeam not in model.team_to_idx or row.AwayTeam not in model.team_to_idx:
                continue
            extra = {key: s.rates(row.HomeTeam, row.AwayTeam) for key, s in candidates.items()}
            if any(v is None for v in extra.values()):
                continue
            meta = model.expected_goals(row.HomeTeam, row.AwayTeam)
            examples.append({'date': row.Date, 'y': (int(row.FTHG), int(row.FTAG)),
                'base': np.array([meta['lambda_home'], meta['lambda_away']]),
                'rho': float(model.rho), 'max_goals': model.max_goals, 'extra': extra})
    return examples


def fit_shot_model(history, cutoff, baseline_factory, half_life_days):
    """Select on tune, gate on a later audit; audit never chooses settings."""
    result = ShotModel(cutoff, half_life_days)
    table = shot_table(history)
    table = table.loc[table['Date'] < result.cutoff]
    result.report['shot_matches'] = len(table)
    if table.empty:
        return result
    audit_start = result.cutoff - pd.Timedelta(days=AUDIT_DAYS)
    tune_start = audit_start - pd.Timedelta(days=TUNE_DAYS)
    result.report.update(tune_start_date=tune_start.date().isoformat(),
                         audit_start_date=audit_start.date().isoformat(),
                         training_shot_matches=int((table['Date'] < tune_start).sum()))
    if result.report['training_shot_matches'] < MIN_TRAIN:
        result.report['status'] = 'INSUFFICIENT_SHOT_HISTORY'
        return result
    dates = pd.to_datetime(history['Date'])
    history_days = (dates.dt.tz_convert(None) if dates.dt.tz is not None else dates).dt.normalize()
    tune = _walk(history, history_days, table, tune_start, audit_start, baseline_factory, half_life_days)
    audit = _walk(history, history_days, table, audit_start, result.cutoff, baseline_factory, half_life_days)
    dates = sorted({e['date'] for e in audit})
    result.report.update(tuning_matches=len(tune), audit_matches=len(audit), audit_matchdays=len(dates))
    if len(tune) < MIN_TUNE or len(audit) < MIN_AUDIT:
        result.report['status'] = 'INSUFFICIENT_CHRONOLOGICAL_PARTITIONS'
        return result
    if len(dates) < MIN_AUDIT_DATES:
        result.report['status'] = 'INSUFFICIENT_AUDIT_MATCHDAYS'
        return result
    y_tune = np.array([e['y'] for e in tune], dtype=float)
    base_tune = np.array([e['base'] for e in tune])
    scores = []
    for key in sorted(tune[0]['extra']):
        extra = np.array([e['extra'][key] for e in tune])
        for weight in WEIGHTS:
            scores.append((poisson_score(y_tune.ravel(), mix_rates(base_tune, extra, weight).ravel()), key, weight))
    _, key, weight = min(scores)
    y = np.array([e['y'] for e in audit], dtype=float)
    base = np.array([e['base'] for e in audit])
    enhanced = mix_rates(base, np.array([e['extra'][key] for e in audit]), weight)
    base_score, extra_score = poisson_score(y.ravel(), base.ravel()), poisson_score(y.ravel(), enhanced.ravel())
    try:
        rhos = [e['rho'] for e in audit]
        base_brier = market_briers(y.astype(int), base, rhos, audit[0]['max_goals'])
        new_brier = market_briers(y.astype(int), enhanced, rhos, audit[0]['max_goals'])
        safe = bool(np.all(new_brier <= base_brier + 1e-12))
    except ValueError:
        safe, base_brier, new_brier = False, None, None
    # Resample whole matchdays, as the BBS gate does.
    losses = np.mean(base - y * np.log(base) - enhanced + y * np.log(enhanced), axis=1)
    day_of = np.array([e['date'] for e in audit])
    blocks = [losses[day_of == d] for d in dates]
    totals = np.array([b.sum() for b in blocks]); counts = np.array([len(b) for b in blocks])
    draw = np.random.default_rng(0).integers(0, len(blocks), size=(1000, len(blocks)))
    lower = float(np.quantile(totals[draw].sum(axis=1) / counts[draw].sum(axis=1), .025))
    gain = base_score - extra_score
    result.report.update(selected_shrinkage=key[0], selected_component=key[1], proposed_weight=weight,
        audit_baseline_poisson_score=base_score, audit_candidate_poisson_score=extra_score,
        audit_gain=gain, audit_gain_lower95=lower,
        audit_baseline_briers=None if base_brier is None else base_brier.tolist(),
        audit_candidate_briers=None if new_brier is None else new_brier.tolist(),
        audit_brier_order=['1x2', 'over_1_5', 'under_3_5', 'btts_yes'])
    failed = [name for name, bad in (('audit_gain_below_minimum', gain < MIN_AUDIT_GAIN),
              ('bootstrap_lower95_not_positive', lower <= 0), ('market_brier_worse', not safe)) if bad]
    if failed:
        result.report.update(status='BASELINE_RETAINED_AUDIT_NOT_IMPROVED', failed_gates=failed)
        return result
    result.strengths = ShotStrengths(table, result.cutoff, half_life_days, *key)
    result.weight = weight
    result.report.update(status='VALIDATED', selected_weight=weight, failed_gates=[])
    return result
