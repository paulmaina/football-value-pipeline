"""Observed-before-cutoff team form and a gated, regularized goal-rate model.

No API calls. Historical match statistics are inputs to LATER matches only.
The production model stays byte-for-byte numerically unchanged on fallback.
"""
from __future__ import annotations

from dataclasses import dataclass
import hashlib
import json
import math

import numpy as np
import pandas as pd
from scipy.optimize import minimize

from bbs_data import STAT_FIELDS, dumps, utc

VERSION = 'bbs-lagged-poisson-v2'
PUBLICATION_DELAY_HOURS = 24
MIN_FORM = 3
FORM_MATCHES = 8
MAX_AGE_DAYS = 180
FORM_HALF_LIFE = 30.
MIN_TRAIN = 60
MIN_TUNE = 20
MIN_AUDIT = 40
MIN_AUDIT_DATES = 8
RIDGES = (1., 10., 100.)
WEIGHTS = (.1, .2, .3)
MAX_RATE_RATIO = 1.25
MIN_AUDIT_GAIN = .01
CORE = ('total_shots', 'shots_on_target')
FEATURE_NAMES = tuple('own_'+f for f in STAT_FIELDS)+tuple('opponent_conceded_'+f for f in STAT_FIELDS)+('is_home',)


def stamp(value):
    """Naive model dates are UTC; source observations themselves require a zone."""
    date = pd.Timestamp(value)
    if pd.isna(date):
        raise ValueError('Invalid statistics cutoff')
    return date.tz_localize('UTC') if date.tzinfo is None else date.tz_convert('UTC')


def clean(values):
    if not isinstance(values, dict):
        raise ValueError('Invalid statistics side')
    out = {}
    for key in STAT_FIELDS:
        value = values.get(key)
        if value is not None:
            if (isinstance(value, bool) or not isinstance(value, (int, float))
                    or not math.isfinite(value) or value < 0
                    or (key in ('ball_possession', 'pass_percentage') and value > 100)
                    or (key not in ('ball_possession', 'pass_percentage') and value != int(value))):
                raise ValueError('Invalid feature statistic: '+key)
        out[key] = value
    for part, total in [('shots_on_target', 'total_shots'), ('accurate_passes', 'total_passes')]:
        if out[part] is not None and out[total] is not None and out[part] > out[total]:
            raise ValueError('Inconsistent feature statistics')
    return out


class FormIndex:
    """Immutable revisions are resolved as-of each individual prediction origin."""
    def __init__(self, observations, cutoff):
        from football_value_pipeline_v2_standalone import canonical_team_key
        self.cutoff = stamp(cutoff)
        self.records = []
        seen = {}
        for original in observations:
            observed = pd.Timestamp(utc(original['observed_at_utc']))
            if observed >= self.cutoff:
                continue
            kick = pd.Timestamp(utc(original['kickoff_utc']))
            if observed <= kick or not original.get('match_id'):
                raise ValueError('Statistics must be observed after their match kickoff')
            home = canonical_team_key(original['home_team'])
            away = canonical_team_key(original['away_team'])
            if not home or not away or home == away:
                raise ValueError('Invalid feature identities')
            available = original.get('available', True)
            item = {**original, 'home_key': home, 'away_key': away,
                    'observed_at_utc': observed.isoformat(), 'kickoff_utc': kick.isoformat(),
                    'available': available,
                    'home': clean(original['home']) if available else None,
                    'away': clean(original['away']) if available else None}
            key = (item['match_id'], observed.isoformat())
            if key in seen and dumps(seen[key]) != dumps(item):
                raise ValueError('Contradictory statistics at one observation instant')
            if key not in seen:
                seen[key] = item
                self.records.append(item)
        self.records.sort(key=lambda r: (r['observed_at_utc'], r['match_id']))
        self.sha256 = hashlib.sha256(dumps(self.records).encode()).hexdigest()
        self._cache = {}
        self._latest_cache = {}
        self.availability_field = 'observed_at_utc'

    def retrospective(self):
        """Latest revisions actually known at the OUTER cutoff, with an explicit
        post-match availability assumption for retrospective development only.
        Actual observation timestamps are never rewritten or backdated.
        """
        latest = {r['match_id']: r for r in self.records}
        result = FormIndex(list(latest.values()), self.cutoff)
        result.availability_field = 'assumed_available_at_utc'
        for item in result.records:
            item['assumed_available_at_utc'] = (stamp(item['kickoff_utc']) +
                pd.Timedelta(hours=PUBLICATION_DELAY_HOURS)).isoformat()
        result.sha256 = hashlib.sha256(dumps(result.records).encode()).hexdigest()
        return result

    def form(self, team, cutoff):
        from football_value_pipeline_v2_standalone import canonical_team_key
        cutoff = stamp(cutoff)
        team = canonical_team_key(team)
        key = (team, cutoff.isoformat())
        if key in self._cache:
            return self._cache[key]
        if cutoff.isoformat() not in self._latest_cache:
            latest = {}
            for item in self.records:
                if pd.Timestamp(item[self.availability_field]) < cutoff:
                    latest[item['match_id']] = item
            self._latest_cache[cutoff.isoformat()] = latest
        latest = self._latest_cache[cutoff.isoformat()]
        matches = []
        for item in latest.values():
            if not item['available']:
                continue
            age = (cutoff - pd.Timestamp(item['kickoff_utc'])).total_seconds()/86400
            if not 0 < age <= MAX_AGE_DAYS or team not in (item['home_key'], item['away_key']):
                continue
            side = 'home' if team == item['home_key'] else 'away'
            other = 'away' if side == 'home' else 'home'
            matches.append((pd.Timestamp(item['kickoff_utc']), item[side], item[other], item['observed_at_utc'], age))
        matches.sort(key=lambda r: r[0], reverse=True)
        matches = matches[:FORM_MATCHES]
        means = []
        coverage = {}
        for source in (1, 2):
            for field in STAT_FIELDS:
                values = [(r[source][field], math.exp(-math.log(2)*r[4]/FORM_HALF_LIFE))
                          for r in matches if r[source][field] is not None]
                coverage[(source, field)] = len(values)
                means.append(sum(v*w for v, w in values)/sum(w for _, w in values)
                             if len(values) >= MIN_FORM else float('nan'))
        result = (np.array(means), len(matches), max((r[3] for r in matches), default=None),
                  all(coverage[(s, f)] >= MIN_FORM for s in (1, 2) for f in CORE))
        self._cache[key] = result
        return result

    def pair(self, home, away, cutoff):
        h, hc, ho, hv = self.form(home, cutoff)
        a, ac, ao, av = self.form(away, cutoff)
        if not hv or not av:
            return None, {'home_matches': hc, 'away_matches': ac, 'status': 'INSUFFICIENT_TEAM_FORM'}
        n = len(STAT_FIELDS)
        matrix = np.array([np.r_[h[:n], a[n:], 1.], np.r_[a[:n], h[n:], 0.]])
        return matrix, {'home_matches': hc, 'away_matches': ac, 'status': 'AVAILABLE',
                        'latest_observed_at_utc': max(ho, ao)}


@dataclass
class PoissonForm:
    median: np.ndarray
    scale: np.ndarray
    beta: np.ndarray
    supported: np.ndarray

    def design(self, x):
        missing = ~np.isfinite(x) | ~self.supported
        z = np.clip((np.where(missing, self.median, x)-self.median)/self.scale, -5, 5)
        return np.column_stack([np.ones(len(x)), z, missing.astype(float)])

    @classmethod
    def fit(cls, x, y, ridge, supported=None):
        # Imputation/scaling is learned from the fitting partition only.
        supported = np.isfinite(x).sum(axis=0) >= MIN_FORM if supported is None else supported.copy()
        x = np.where(supported, x, np.nan)
        median = np.array([float(np.median(c[np.isfinite(c)])) if np.isfinite(c).any() else 0. for c in x.T])
        filled = np.where(np.isfinite(x), x, median)
        scale = np.std(filled, axis=0)
        scale[scale < 1e-6] = 1.
        result = cls(median, scale, np.zeros(1+2*x.shape[1]), supported)
        design = result.design(x)
        initial = result.beta.copy(); initial[0] = math.log(max(float(np.mean(y)), .1))
        penalty = np.r_[0., np.full(len(initial)-1, ridge)]
        def loss(beta):
            eta = design @ beta
            rate = np.exp(eta)
            return (float(np.sum(rate-y*eta)+.5*np.sum(penalty*beta**2)),
                    design.T @ (rate-y)+penalty*beta)
        fit = minimize(loss, initial, jac=True, method='L-BFGS-B',
                       bounds=[(-3, 3)]*len(initial), options={'maxiter': 500, 'ftol': 1e-10})
        if not fit.success or not np.isfinite(fit.x).all() or not math.isfinite(fit.fun):
            raise ValueError('Statistical goal model failed convergence')
        result.beta = fit.x
        return result

    def predict(self, x):
        return np.exp(np.clip(self.design(x) @ self.beta, math.log(.05), math.log(10)))


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


class StatisticsModel:
    def __init__(self, index, cutoff):
        self.index = index
        self.cutoff = stamp(cutoff)
        self.model = None
        self.weight = 0.
        self.report = {'version': VERSION, 'status': 'INSUFFICIENT_PAST_OBSERVATIONS',
            'cutoff_utc': self.cutoff.isoformat(), 'observations': len(index.records),
            'observations_sha256': index.sha256, 'eligible_training_matches': 0,
            'required_training_matches': MIN_TRAIN+MIN_TUNE+MIN_AUDIT,
            'feature_fields': list(STAT_FIELDS), 'minimum_team_matches': MIN_FORM,
            'max_form_matches': FORM_MATCHES, 'max_form_age_days': MAX_AGE_DAYS,
            'max_goal_rate_ratio': MAX_RATE_RATIO, 'selected_weight': 0.}
        latest = {r['match_id']: r for r in index.records}
        self.report['usable_current_matches'] = sum(r['available'] for r in latest.values())

    def apply(self, home, away, base):
        info = {'bbs_statistics_applied': False, 'bbs_statistics_version': VERSION,
                'bbs_statistics_status': self.report['status'],
                'bbs_statistics_validation_mode': self.report.get('validation_mode', 'strict'),
                'bbs_statistics_cutoff_utc': self.cutoff.isoformat(),
                'bbs_statistics_weight': 0.}
        if self.model is None:
            return np.asarray(base), info
        x, coverage = self.index.pair(home, away, self.cutoff)
        info.update(bbs_statistics_home_matches=coverage['home_matches'],
                    bbs_statistics_away_matches=coverage['away_matches'])
        if x is None:
            info['bbs_statistics_status'] = coverage['status']
            return np.asarray(base), info
        rate = mix_rates(base, self.model.predict(x), self.weight)
        info.update(bbs_statistics_applied=True, bbs_statistics_status='APPLIED',
            bbs_statistics_weight=self.weight,
            bbs_statistics_latest_observed_utc=coverage['latest_observed_at_utc'])
        return rate, info

    def save(self, cache_dir, league):
        from pathlib import Path
        from bbs_data import atomic_json
        payload = {'report': self.report, 'weight': self.weight, 'version': VERSION,
            'parameters': None if self.model is None else {
                'median': self.model.median.tolist(), 'scale': self.model.scale.tolist(),
                'beta': self.model.beta.tolist(), 'supported': self.model.supported.tolist(),
                'columns': ['intercept', *FEATURE_NAMES, *('missing_'+f for f in FEATURE_NAMES)]}}
        digest = hashlib.sha256(dumps(payload).encode()).hexdigest()
        path = Path(cache_dir)/'bbs/feature_models'/league/(self.cutoff.strftime('%Y%m%dT%H%M%S%fZ')+'_'+digest+'.json')
        if path.exists():
            if json.loads(path.read_text(encoding='utf-8')) != payload:
                raise ValueError('Immutable feature-model artifact conflict')
            return path
        atomic_json(path, payload)
        return path


def fit_statistics(history, cutoff, baseline_factory, validation_mode='auto'):
    """Auto chooses strict evidence when sufficient, otherwise labelled backfill.
    Both modes admit only source revisions actually observed before outer cutoff.
    Audit cannot select ridge, blend weight, or the validation mode.
    """
    if validation_mode not in ('auto', 'strict'):
        raise ValueError('Unknown BBS statistics validation mode')
    index = FormIndex(history.attrs.get('bbs_statistics_observations', []), cutoff)
    result = StatisticsModel(index, cutoff)
    result.report.update(validation_policy=validation_mode, validation_mode='strict',
        strict_eligible_training_matches=0, retrospective_eligible_training_matches=0,
        retrospective_publication_delay_hours=PUBLICATION_DELAY_HOURS,
        forward_accuracy_improvement_established=False)
    if not index.records:
        return result
    first_observed = min(pd.Timestamp(r['observed_at_utc']) for r in index.records)
    result.report['first_observed_at_utc'] = first_observed.isoformat()
    rows = history.sort_values('Date', kind='stable').to_dict('records')
    def examples_from(inputs, earliest):
        examples = []
        for row in rows:
            origin = stamp(row['Date']).normalize()
            # Domestic labels are date-only: same-day results remain excluded.
            if origin >= stamp(cutoff).normalize() or origin <= earliest:
                continue
            x, _ = inputs.pair(row['HomeTeam'], row['AwayTeam'], origin)
            if x is not None:
                examples.append((origin, x, [int(row['FTHG']), int(row['FTAG'])], row['HomeTeam'], row['AwayTeam']))
        return examples

    examples = examples_from(index, first_observed)
    result.report['strict_eligible_training_matches'] = len(examples)
    required = MIN_TRAIN+MIN_TUNE+MIN_AUDIT
    if validation_mode == 'auto' and len(examples) < required:
        # Choose by coverage alone, before outcomes or audit scores are examined.
        development_index = index.retrospective()
        examples = examples_from(development_index,
            min(stamp(r['assumed_available_at_utc']) for r in development_index.records))
        result.report.update(validation_mode='retrospective_backfill',
            retrospective_eligible_training_matches=len(examples),
            retrospective_inputs_sha256=development_index.sha256,
            historical_corrections_may_be_present=True,
            evaluation_note='Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.')
    else:
        development_index = index
        result.report['historical_corrections_may_be_present'] = False
    result.report['eligible_training_matches'] = len(examples)
    if len(examples) < required:
        if result.report['validation_mode'] == 'retrospective_backfill':
            result.report['status'] = 'INSUFFICIENT_RETROSPECTIVE_EXAMPLES'
        return result
    # Date boundaries, never arbitrary row cuts within a matchday.
    tune_origin = examples[-(MIN_TUNE+MIN_AUDIT)][0]
    audit_origin = examples[-MIN_AUDIT][0]
    train = [e for e in examples if e[0] < tune_origin]
    tune = [e for e in examples if tune_origin <= e[0] < audit_origin]
    audit = [e for e in examples if e[0] >= audit_origin]
    result.report.update(training_matches=len(train), tuning_matches=len(tune), audit_matches=len(audit),
                         tuning_origin_utc=tune_origin.isoformat(), audit_origin_utc=audit_origin.isoformat())
    if len(train) < MIN_TRAIN or len(tune) < MIN_TUNE or len(audit) < MIN_AUDIT:
        result.report['status'] = 'INSUFFICIENT_CHRONOLOGICAL_PARTITIONS'
        return result

    def arrays(rows):
        return np.concatenate([e[1] for e in rows]), np.concatenate([e[2] for e in rows])

    def baseline(rows, origin):
        past = history.loc[pd.to_datetime(history['Date'], utc=True) < origin]
        model = baseline_factory(past, origin)
        rates, rhos = [], []
        for _, _, _, home, away in rows:
            meta = model.expected_goals(home, away)
            rates.append([meta['lambda_home'], meta['lambda_away']]); rhos.append(float(model.rho))
        return np.array(rates), rhos, model.max_goals

    x_train, y_train = arrays(train)
    supported = np.isfinite(x_train).sum(axis=0) >= MIN_TRAIN
    result.report['supported_feature_columns'] = [name for name, ok in zip(FEATURE_NAMES, supported) if ok]
    x_tune, y_tune = arrays(tune)
    tune_base, _, _ = baseline(tune, tune_origin)
    candidates = []
    for ridge in RIDGES:
        model = PoissonForm.fit(x_train, y_train, ridge, supported)
        extra = model.predict(x_tune).reshape(-1, 2)
        for weight in WEIGHTS:
            rates = mix_rates(tune_base, extra, weight)
            candidates.append((poisson_score(y_tune, rates.ravel()), ridge, weight))
    _, ridge, weight = min(candidates)
    x_dev, y_dev = arrays(train+tune)
    selected = PoissonForm.fit(x_dev, y_dev, ridge, supported)
    audit_base, rhos, minimum = baseline(audit, audit_origin)
    # The held-out feature matrix is frozen at the audit origin, matching the
    # frozen control fit; no within-audit result or statistic enters either arm.
    paired = []
    for example, base, rho in zip(audit, audit_base, rhos):
        x, _ = development_index.pair(example[3], example[4], audit_origin)
        if x is not None:
            paired.append((x, example[2], base, rho, example[0].date().isoformat()))
    result.report['paired_audit_matches'] = len(paired)
    if len(paired) < MIN_AUDIT:
        result.report['status'] = 'INSUFFICIENT_PAIRED_AUDIT'
        return result
    x_audit = np.concatenate([p[0] for p in paired])
    y_audit = np.array([p[1] for p in paired])
    base = np.array([p[2] for p in paired]); rhos = [p[3] for p in paired]
    enhanced = mix_rates(base, selected.predict(x_audit).reshape(-1, 2), weight)
    base_score = poisson_score(y_audit.ravel(), base.ravel())
    extra_score = poisson_score(y_audit.ravel(), enhanced.ravel())
    gain = base_score-extra_score
    try:
        base_brier = market_briers(y_audit, base, rhos, minimum)
        new_brier = market_briers(y_audit, enhanced, rhos, minimum)
        safe = bool(np.all(new_brier <= base_brier+1e-12))
    except ValueError:
        safe = False
        base_brier = new_brier = None
    # Resample whole matchdays: same-day fixtures are not independent draws.
    losses = np.mean(base-y_audit*np.log(base)-enhanced+y_audit*np.log(enhanced), axis=1)
    dates = sorted({p[4] for p in paired})
    result.report['audit_matchdays'] = len(dates)
    if len(dates) < MIN_AUDIT_DATES:
        result.report['status'] = 'INSUFFICIENT_AUDIT_MATCHDAYS'
        return result
    blocks = [losses[np.array([p[4] == day for p in paired])] for day in dates]
    totals = np.array([b.sum() for b in blocks]); counts = np.array([len(b) for b in blocks])
    draw = np.random.default_rng(0).integers(0, len(blocks), size=(1000, len(blocks)))
    lower = float(np.quantile(totals[draw].sum(axis=1)/counts[draw].sum(axis=1), .025))
    result.report.update(selected_ridge=ridge, proposed_weight=weight,
        audit_baseline_poisson_score=base_score, audit_candidate_poisson_score=extra_score,
        audit_gain=gain, audit_gain_lower95=lower,
        audit_baseline_briers=None if base_brier is None else base_brier.tolist(),
        audit_candidate_briers=None if new_brier is None else new_brier.tolist(),
        audit_brier_order=['1x2', 'over_1_5', 'under_3_5', 'btts_yes'])
    if gain < MIN_AUDIT_GAIN or lower <= 0 or not safe:
        result.report['status'] = 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED'
        return result
    x_all, y_all = arrays(examples)
    result.model = PoissonForm.fit(x_all, y_all, ridge, supported)
    result.weight = weight
    result.report.update(status='VALIDATED', selected_weight=weight)
    return result


def forward_assessment(predictions, records, clock):
    """Paired raw-model Briers from frozen pre-kickoff forecasts only.
    No fitting, promotion, new forecasts or provider calls during grading.
    """
    from performance_tracking import fixture_match, number, MIN_LEAD_MINUTES
    paired, pending, invalid = [], 0, 0
    clock = stamp(clock)
    for row in predictions:
        if row.get('bbs_statistics_applied') not in (True, 'True'):
            continue
        try:
            kickoff = stamp(utc(row['kickoff_utc']))
            generated = stamp(utc(row['snapshot_generated_utc']))
            captured = stamp(utc(row['snapshot_captured_utc']))
            model_cutoff = stamp(utc(row['bbs_statistics_cutoff_utc']))
            observed = stamp(utc(row['bbs_statistics_latest_observed_utc']))
            mode = row['bbs_statistics_validation_mode']
            if (mode not in ('strict', 'retrospective_backfill') or observed >= model_cutoff
                    or model_cutoff > generated or max(generated, captured) > kickoff-pd.Timedelta(minutes=MIN_LEAD_MINUTES)):
                raise ValueError('Invalid forward provenance')
            arrays = []
            for prefix in ('raw_p_', 'bbs_control_p_'):
                p = [number(row.get(prefix+key), min_value=0, max_value=1)
                     for key in ('home','draw','away','over_1_5','under_3_5','btts_yes')]
                if any(v is None for v in p) or abs(sum(p[:3])-1) > 1e-6:
                    raise ValueError('Invalid paired probabilities')
                arrays.append(np.array(p))
        except (ValueError, KeyError, TypeError):
            invalid += 1
            continue
        final, state = fixture_match(row, records)
        if kickoff > clock-pd.Timedelta(hours=2) or final is None or state != 'VERIFIED_FINISHED':
            pending += 1
            continue
        h, a = final['home_goals'], final['away_goals']
        target = np.array([h>a,h==a,h<a,h+a>=2,h+a<=3,h>0 and a>0], dtype=float)
        briers = [np.r_[np.sum((p[:3]-target[:3])**2), (p[3:]-target[3:])**2] for p in arrays]
        paired.append({'fixture_key': row['fixture_key'], 'league': row['league'],
            'snapshot_commit': row['snapshot_commit'], 'kickoff_utc': kickoff.isoformat(),
            'source_match_id': final['match_id'], 'validation_mode': mode,
            'candidate_briers': briers[0].tolist(), 'control_briers': briers[1].tolist()})
    def summarize(rows):
        return {'paired_matches': len(rows),
            'candidate_mean_briers': np.mean([r['candidate_briers'] for r in rows],axis=0).tolist() if rows else None,
            'control_mean_briers': np.mean([r['control_briers'] for r in rows],axis=0).tolist() if rows else None}
    return {'version': VERSION, 'reviewed_at_utc': clock.isoformat(),
        'basis': 'Frozen pre-kickoff raw model versus same-fit Dixon-Coles control, before bookmaker blending',
        'status': 'DESCRIPTIVE_FORWARD_COMPARISON' if paired else 'AWAITING_ELIGIBLE_FORWARD_RESULTS',
        'brier_order': ['1x2','over_1_5','under_3_5','btts_yes'],
        'pending_matches': pending, 'invalid_forecasts': invalid, **summarize(paired),
        'by_validation_mode': {mode: summarize([r for r in paired if r['validation_mode']==mode])
                               for mode in ('strict','retrospective_backfill')},
        'automatic_promotion': False, 'paired_rows': paired}
