"""Isolated same-history L2 and fixed-half-life forward trials; never production."""
from datetime import timedelta
import hashlib
import json
from pathlib import Path

import numpy as np
import pandas as pd

VERSION = 'model-reliability-forward-v1'
FILE = 'model_reliability_experiment.json'
MARKETS = ('1x2', 'over_1_5', 'under_3_5', 'btts_yes', 'over_2_5')
REGISTRY = {
    'version': VERSION, 'registered_on': '2026-10-14',
    'candidates': {'stronger_l2': {'l2': 3.0}, 'fixed_half_life': {'half_life_days': 480.0}},
    'leagues': ['Premier League', 'La Liga', 'Bundesliga', 'Serie A', 'Ligue 1'],
    'nomination': 'docs/benchmarks/2026-10-14/report.md; development-only ALL 1x2 choices: l2_3 and half_life_480; retrospective evidence is not untouched validation',
    'primary_metric': '1x2_log_loss', 'minimum_paired_fixtures': 300,
    'minimum_gameweeks': 6, 'minimum_verified_coverage': 0.8,
    'bootstrap_replicates': 2000, 'bootstrap_seed': 20261014,
    'confidence_level': 0.975,  # Bonferroni familywise 95% for two primary trials.
    'approval_required': True, 'automatic_production_change': False,
}


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':'), allow_nan=False).encode()).hexdigest()


def probabilities(matrix):
    from historical_benchmark import goals
    m = np.asarray(matrix, dtype=float)
    if (m.ndim != 2 or m.shape[0] != m.shape[1] or not m.size
            or not np.isfinite(m).all() or (m < 0).any() or abs(m.sum()-1) > 1e-8):
        raise ValueError('Invalid reliability score matrix')
    h, a = np.indices(m.shape)
    return dict(zip(('p_home', 'p_draw', 'p_away'),
                    (float(m[h > a].sum()), float(m[h == a].sum()), float(m[h < a].sum()))), **goals(m))


def baseline(row):
    from performance_tracking import number
    values = {k: number(row.get(k), min_value=0, max_value=1)
              for k in ('p_home', 'p_draw', 'p_away')}
    values.update({m: number(row.get('p_'+m), min_value=0, max_value=1) for m in MARKETS[1:]})
    if any(p is None for p in values.values()) or abs(sum(values[k] for k in ('p_home', 'p_draw', 'p_away'))-1) > 1e-8:
        return None
    return values


def candidate_probabilities(row, matrix):
    """Change the raw fit only, retaining production's 1X2 market blend."""
    from benchmark_forward_experiment import simplex
    from football_value_pipeline_v2_standalone import reweight_matrix_to_1x2
    raw = probabilities(matrix)
    weight = float(row['market_weight'])
    if not 0 <= weight <= 1:
        raise ValueError('Invalid production weight')
    if row.get('market_blend_applied') not in (True, 1, 'True'):
        # Do not compare an unknown production transformation with a raw candidate.
        control = simplex(row, 'raw_p_')
        prod = simplex(row, 'p_')
        if control is None or prod is None or not np.allclose(control, prod, atol=1e-9, rtol=0):
            raise ValueError('Unreproducible production basis')
        return raw
    market = simplex(row, 'market_p_')
    control = simplex(row, 'raw_p_')
    prod = simplex(row, 'p_')
    if market is None or control is None or prod is None or not np.allclose(
            prod, (1-weight)*np.array(control)+weight*np.array(market), atol=1e-9, rtol=0):
        raise ValueError('Unreproducible production blend')
    target = (1-weight)*np.array([raw[k] for k in ('p_home', 'p_draw', 'p_away')])+weight*np.array(market)
    return probabilities(reweight_matrix_to_1x2(np.asarray(matrix), target))


def generate_league(predictions, history, model_class, *, half_life, l2, max_goals, as_of=None):
    """Two extra fits; identical private training copies; no odds/provider calls."""
    canonical = history[['Date', 'HomeTeam', 'AwayTeam', 'FTHG', 'FTAG']].to_csv(index=False, lineterminator='\n')
    provenance = {'training_sha256': hashlib.sha256(canonical.encode()).hexdigest(),
                  'training_end': pd.to_datetime(history.Date).max().isoformat(),
                  'training_matches': len(history), 'production_half_life_days': half_life,
                  'production_l2': l2, 'max_goals': max_goals,
                  'training_as_of_utc': None if as_of is None else pd.Timestamp(as_of).isoformat()}
    models, errors = {}, {}
    for name, change in REGISTRY['candidates'].items():
        params = {'half_life_days': half_life, 'l2': l2, 'max_goals': max_goals, **change}
        try:
            if name == 'stronger_l2' and l2 >= change['l2']:
                raise ValueError('Production regularisation already at least as strong')
            model = model_class(**params).fit(history.copy(deep=True),
                **({'as_of': pd.Timestamp(as_of)} if as_of is not None else {}))
            from football_value_pipeline_v2_standalone import LEAGUES
            leagues = set(predictions['league'].dropna())
            model.league_key = next((c.key for c in LEAGUES.values() if leagues == {c.name}), None)
            fit = getattr(model, 'fit_result', None)
            if fit is not None and not fit.success:
                raise ValueError('Optimizer did not converge')
            models[name] = model
        except Exception as exc:
            errors[name] = type(exc).__name__
    rows = []
    for source in predictions.astype(object).where(predictions.notna(), None).to_dict('records'):
        row = {k: source.get(k) for k in ('league', 'home_team', 'away_team', 'kickoff_utc')}
        row.update(provenance, baseline=baseline(source), candidates={})
        for name, change in REGISTRY['candidates'].items():
            item = {'settings': {'half_life_days': half_life, 'l2': l2, 'max_goals': max_goals, **change},
                    'status': 'unavailable', 'reason': errors.get(name), 'raw_matrix': None, 'probabilities': None}
            try:
                if row['league'] not in REGISTRY['leagues']:
                    raise ValueError('League outside frozen trial')
                if row['baseline'] is None or any(source.get(k) in (None, '__LEAGUE_AVERAGE__') for k in ('model_home_team', 'model_away_team')):
                    raise ValueError('Missing baseline or unknown team')
                if min(float(source.get(k) or 0) for k in ('home_name_match_score', 'away_name_match_score')) < 90:
                    raise ValueError('Unreliable production team identity')
                if name not in models:
                    raise ValueError('Candidate fit unavailable')
                matrix, meta = models[name].score_matrix(source['home_team'], source['away_team'])
                if min(float(meta.get(k, 0)) for k in ('home_name_match_score', 'away_name_match_score')) < 90:
                    raise ValueError('Unreliable candidate team identity')
                values = candidate_probabilities(source, matrix)
                item.update(status='available', reason=None, raw_matrix=np.asarray(matrix).tolist(), probabilities=values)
            except Exception as exc:
                item['reason'] = item['reason'] or type(exc).__name__
            row['candidates'][name] = item
        rows.append(row)
    return rows


def write_experiment(predictions, raw, generated, rows):
    from performance_tracking import write_json, fixture_key
    # Always include explicit unavailable rows if a league-level fit failed.
    known = {fixture_key(row): row for row in rows}
    for source in predictions.to_dict('records'):
        known.setdefault(fixture_key(source), {
            **{k: source.get(k) for k in ('league', 'home_team', 'away_team', 'kickoff_utc')},
            'baseline': baseline(source), 'generation_error': 'LEAGUE_GENERATION_FAILED', 'candidates': {}})
    data = {'version': VERSION, 'registry': REGISTRY, 'registry_sha256': digest(REGISTRY),
            'generated_at_utc': generated, 'rows': list(known.values()),
            'predictions_sha256': hashlib.sha256((raw/'all_leagues_predictions.csv').read_bytes()).hexdigest()}
    validate(data, generated, predictions.to_dict('records'))
    write_json(raw/FILE, data)
    return data


def validate(data, generated, predictions):
    from performance_tracking import utc, fixture_key
    from totals_anchor_experiment import equivalent
    if (data.get('version') != VERSION or data.get('registry') != REGISTRY
            or data.get('registry_sha256') != digest(REGISTRY)
            or utc(generated) is None or utc(data.get('generated_at_utc')) != utc(generated)):
        raise ValueError('Unbound reliability registry/time')
    originals = {fixture_key(r): r for r in predictions}
    seen = set()
    for row in data['rows']:
        key = fixture_key(row)
        if key in seen or key not in originals or not utc(row.get('kickoff_utc')):
            raise ValueError('Invalid reliability fixture')
        seen.add(key)
        source = originals[key]
        if not equivalent(row['baseline'], baseline(source)):
            raise ValueError('Reliability baseline differs from production')
        if row.get('generation_error'):
            if row.get('candidates'):
                raise ValueError('Failed generation has candidate probabilities')
            continue
        trained = pd.Timestamp(row['training_end'])
        trained = trained.tz_localize('UTC') if trained.tzinfo is None else trained.tz_convert('UTC')
        if trained > pd.Timestamp(utc(generated)) or row['training_matches'] <= 0:
            raise ValueError('Future or empty training history')
        if len(row['training_sha256']) != 64 or set(row['candidates']) != set(REGISTRY['candidates']):
            raise ValueError('Invalid training provenance/candidate coverage')
        for name, item in row['candidates'].items():
            expected = {'half_life_days': row['production_half_life_days'], 'l2': row['production_l2'],
                        'max_goals': row['max_goals'], **REGISTRY['candidates'][name]}
            if item['settings'] != expected or item['status'] not in ('available', 'unavailable'):
                raise ValueError('Candidate settings changed')
            if item['status'] == 'unavailable':
                if item['probabilities'] is not None or item['raw_matrix'] is not None:
                    raise ValueError('Unavailable candidate contains forecast')
                continue
            if row['league'] not in REGISTRY['leagues'] or row['baseline'] is None:
                raise ValueError('Candidate outside trial scope')
            if not equivalent(item['probabilities'], candidate_probabilities(source, item['raw_matrix'])):
                raise ValueError('Candidate probabilities differ from frozen matrix')
    if seen != set(originals):
        raise ValueError('Incomplete reliability coverage')


def capture_file(raw, generated):
    from performance_tracking import read_csv, load_json
    from forecast_integrity import forecast_digest_variants
    path = raw/FILE
    if not path.exists():
        return None
    data = load_json(path, {})
    validate(data, generated, read_csv(raw/'all_leagues_predictions.csv'))
    if data['predictions_sha256'] not in forecast_digest_variants(raw/'all_leagues_predictions.csv'):
        raise ValueError('Reliability forecast binding failed')
    return path


def frozen(root, archive):
    from performance_tracking import load_json, utc, fixture_key
    from forecast_integrity import forecast_digest_variants, snapshot_generated_at
    result, rejected = {}, []
    for meta, predictions, _ in archive:
        directory = root/'performance/snapshots'/meta['git_commit_sha'][:16]
        path = directory/FILE
        expected = meta.get('sha256', {}).get(FILE)
        if not expected:
            continue
        try:
            if not path.exists() or hashlib.sha256(path.read_bytes()).hexdigest() != expected:
                raise ValueError('Reliability snapshot integrity failure')
            data = load_json(path, {})
            validate(data, snapshot_generated_at(directory, meta), predictions)
            if data['predictions_sha256'] not in forecast_digest_variants(directory/'predictions.csv'):
                raise ValueError('Reliability snapshot binding failed')
        except (ValueError, KeyError, TypeError, OSError):
            rejected.append(meta['git_commit_sha'])
            continue
        generated, captured = utc(data['generated_at_utc']), utc(meta['captured_at_utc'])
        if generated.date().isoformat() < REGISTRY['registered_on']:
            continue
        for row in data['rows']:
            kickoff = utc(row['kickoff_utc'])
            if max(generated, captured) >= kickoff-timedelta(minutes=20) or kickoff > generated+timedelta(hours=72):
                continue
            if row['league'] in REGISTRY['leagues']:
                result.setdefault(fixture_key(row), {**row, 'snapshot_commit': meta['git_commit_sha']})
    return list(result.values()), rejected


def evaluate(root, archive, records, clock):
    from performance_tracking import fixture_match, utc
    from historical_benchmark import metrics, score
    from benchmark_forward_experiment import block_interval
    rows, rejected = frozen(root, archive)
    records = [r for r in records if r.get('source_status') == 'FINISHED' and r.get('source') == 'football-data.org/v4']
    comparisons, ledger = [], []
    for name in REGISTRY['candidates']:
        graded, verified = [], 0
        for row in rows:
            match, _ = fixture_match(row, records)
            if not match or utc(row['kickoff_utc']) > clock-timedelta(hours=2):
                continue
            verified += 1
            item = row['candidates'].get(name, {})
            if item.get('status') != 'available':
                continue
            year, week, _ = utc(row['kickoff_utc']).isocalendar()
            actual = {'home_goals': match['home_goals'], 'away_goals': match['away_goals'],
                      'y': 0 if match['home_goals'] > match['away_goals'] else 1 if match['home_goals'] == match['away_goals'] else 2}
            base, candidate = {**row['baseline'], **actual}, {**item['probabilities'], **actual}
            graded.append({'week': f'{year}-W{week:02d}', 'baseline': base, 'candidate': candidate,
                           'log_loss_gain': score(base, '1x2')['log_loss']-score(candidate, '1x2')['log_loss']})
            ledger.append({'candidate_id': name, **{k: row[k] for k in ('league', 'home_team', 'away_team', 'kickoff_utc', 'snapshot_commit')},
                           'source_match_id': match['match_id'], **graded[-1]})
        interval = block_interval(graded, {'review_gates': REGISTRY})
        coverage = len(graded)/verified if verified else None
        weeks = len({r['week'] for r in graded})
        sufficient = len(graded) >= REGISTRY['minimum_paired_fixtures'] and weeks >= REGISTRY['minimum_gameweeks']
        quality = coverage is not None and coverage >= REGISTRY['minimum_verified_coverage'] and not rejected
        scores = {market: {variant: metrics([r[variant] for r in graded], market)
                           for variant in ('baseline', 'candidate')} for market in MARKETS}
        # Calibration is descriptive; expose it for every binary market and 1X2 top label.
        from benchmark_forward_experiment import metrics as hda_metrics
        hda = hda_metrics([{**r, 'baseline': [r['baseline'][k] for k in ('p_home', 'p_draw', 'p_away')],
                           'candidate': [r['candidate'][k] for k in ('p_home', 'p_draw', 'p_away')], 'y': r['baseline']['y']} for r in graded])
        guardrails = bool(graded) and all(s['candidate']['brier'] <= s['baseline']['brier'] and
                                        s['candidate']['log_loss'] <= s['baseline']['log_loss'] for s in scores.values())
        supports = (sufficient and quality and guardrails and interval is not None and interval[0] > 0
                    and hda['candidate']['ece'] <= hda['baseline']['ece'])
        by_league = {league: {market: {variant: metrics([r[variant] for r in ledger if r['candidate_id'] == name and r['league'] == league], market)
                                     for variant in ('baseline', 'candidate')} for market in MARKETS} for league in REGISTRY['leagues']}
        comparisons.append({'candidate_id': name, 'status': 'READY_FOR_REVIEW' if sufficient and quality else 'DATA_QUALITY_BLOCKED' if sufficient else 'COLLECT_MORE_DATA',
                            'evidence': 'SUPPORTS_FORECASTING_REVIEW' if supports else 'NO_CLEAR_PROMOTION_EVIDENCE',
                            'paired_fixtures': len(graded), 'verified_fixtures': verified, 'verified_coverage': coverage, 'gameweeks': weeks,
                            'primary_log_loss_gain_familywise95': interval, 'scores': scores, 'top_label_calibration': hda,
                            'guardrails_passed': guardrails, 'by_league': by_league})
    return {'version': VERSION, 'registry': REGISTRY, 'registry_sha256': digest(REGISTRY),
            'reviewed_at_utc': clock.isoformat(), 'observed_fixtures': len(rows), 'comparisons': comparisons,
            'rejected_snapshot_commits': rejected, 'automatic_production_change': False,
            'note': 'Two separate one-factor trials against actual production, not a combined configuration. First eligible snapshot freezes missing candidates too. Primary 1X2 week-block intervals use 97.5% per trial (familywise 95%); other markets/calibration are guardrails and descriptive. No automatic promotion or betting-edge claim.'}, ledger


def review_experiment(root, archive, records, clock):
    from performance_tracking import write_json
    if not any(FILE in meta.get('sha256', {}) for meta, _, _ in archive):
        return None
    summary, ledger = evaluate(root, archive, records, clock)
    dest = root/'performance/model_reliability_experiment'
    write_json(dest/'summary.json', summary)
    write_json(dest/'graded.json', ledger)
    lines = ['# Model reliability trials', '', summary['note'], '',
             '| Candidate | Status | Paired fixtures | Gameweeks | Verified coverage |', '|---|---|---:|---:|---:|']
    for r in summary['comparisons']:
        lines.append(f"| {r['candidate_id']} | {r['status']} | {r['paired_fixtures']}/300 | {r['gameweeks']}/6 | {r['verified_coverage']} |")
        lines += ['', f"## {r['candidate_id']}", '',
                  '| Market | Baseline log loss | Candidate log loss | Baseline Brier | Candidate Brier |', '|---|---:|---:|---:|---:|']
        for market, scores in r['scores'].items():
            b, c = scores['baseline'], scores['candidate']
            lines.append(f"| {market} | {b['log_loss']} | {c['log_loss']} | {b['brier']} | {c['brier']} |")
        lines += ['', f"Primary familywise 95% gain interval: {r['primary_log_loss_gain_familywise95']}",
                  f"Evidence: {r['evidence']}. Calibration and league breakdowns: summary.json.", '']
    (dest/'report.md').write_text('\n'.join(lines)+'\n', encoding='utf-8')
    return summary


def validate_report(root):
    from performance_tracking import load_json, snapshots, utc
    dest = root/'performance/model_reliability_experiment'
    actual = load_json(dest/'summary.json', {})
    expected, ledger = evaluate(root, snapshots(root), list(load_json(root/'performance/verified_results.json', {}).values()), utc(actual['reviewed_at_utc']))
    if actual != expected or load_json(dest/'graded.json', []) != ledger:
        raise ValueError('Reliability report differs from frozen forecasts/results')
    return True

