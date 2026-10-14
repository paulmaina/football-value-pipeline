"""Visible evidence of data/quote/capture health; no automatic model promotion."""
from collections import Counter
from datetime import datetime, timezone
import hashlib
from importlib.metadata import version, PackageNotFoundError
import json
import math
from pathlib import Path
import platform


def read(path, default=None):
    return json.loads(path.read_text(encoding='utf-8-sig')) if path.exists() else default


def utc(value):
    try:
        date = datetime.fromisoformat(str(value).replace('Z', '+00:00'))
        return date.astimezone(timezone.utc) if date.tzinfo else None
    except (ValueError, TypeError):
        return None


def current_health(root, clock):
    from performance_tracking import read_csv
    from quote_policy import is_exchange, load_policy
    from ucl_training import health
    raw = root/'raw'; training = {}
    for path in sorted(raw.glob('*_diagnostics.json')):
        data = read(path, {})
        end = data.get('training_end')
        training[path.stem.replace('_diagnostics', '')] = {
            'training_end': end, 'training_matches': data.get('training_matches'),
            'days_since_latest_result': (clock.date()-datetime.fromisoformat(end).date()).days if end else None,
            'forecast_training_health': data.get('training_data_health', {'status': 'LEGACY_NOT_RECORDED'}),
            'diagnostics_sha256': hashlib.sha256(path.read_bytes()).hexdigest()}
    if 'UCL' in training:
        training['UCL']['current_source_health'] = health(root.parent, training['UCL']['training_end'], clock)
    picks = read_csv(raw/'conservative_bet_shortlist.csv')
    quote = {'selected_quotes': len(picks), 'exchange_quotes': 0, 'missing_quote_age': 0,
             'quote_age_over_24h': 0, 'costs_recorded': 0, 'bookmakers': dict(Counter(r.get('bookmaker', '') for r in picks)),
             'account_availability': 'NOT_VERIFIED_WITH_BOOKMAKER_ACCOUNTS'}
    for row in picks:
        quote['exchange_quotes'] += int(is_exchange(row.get('bookmaker')))
        try:
            age = float(row.get('odds_age_hours'))
            evaluated = utc(row.get('evaluated_at_utc'))
            if not math.isfinite(age) or evaluated is None:
                raise ValueError('Missing quote timing')
            age += (clock-evaluated).total_seconds()/3600
            quote['quote_age_over_24h'] += int(age > 24 or age < -5/60)
        except (ValueError, TypeError):
            quote['missing_quote_age'] += 1
        quote['costs_recorded'] += int(row.get('per_stake_cost') not in ('', None))
    dependencies = {'python': platform.python_version()}
    for package in ('numpy', 'pandas', 'scipy', 'requests', 'python-dotenv', 'coverage', 'PyYAML'):
        try:
            dependencies[package] = version(package)
        except PackageNotFoundError:
            dependencies[package] = 'NOT_INSTALLED'
    return {'training': training, 'quote_audit': quote, 'execution_policy': load_policy(),
            'dependencies': dependencies}


def capture_health(root, clock, files):
    from performance_tracking import read_csv
    data = current_health(root, clock)
    data['experiments'] = {}
    raw = root/'raw'
    for name in ('goal_blend_experiment', 'market_led_experiment', 'filter_sensitivity_experiment', 'benchmark_forward_experiment', 'totals_anchor_experiment'):
        data['experiments'][name] = ('CAPTURED' if name+'.json' in files else
            'PRESENT_BUT_REJECTED' if (raw/(name+'.json')).exists() else 'NOT_GENERATED')
    parent=read(raw/'goal_blend_experiment.json',{})
    extension=parent.get('recency_experiment')
    from recency_experiment import valid_extension
    data['experiments']['recency_experiment'] = ('CAPTURED' if 'goal_blend_experiment.json' in files and valid_extension(extension,parent.get('generated_at_utc')) else
        'PRESENT_BUT_REJECTED' if extension is not None else 'NOT_GENERATED')
    data['captured_at_utc'] = clock.isoformat()
    data['forecast_generated_at_utc'] = read(raw/'conservative_bet_summary.json', {}).get('generated_at_utc')
    provenance = read(raw/'pipeline_run_metadata.json', {})
    from forecast_integrity import forecast_digest_variants
    source_time = utc(provenance.get('generated_at_utc'))
    expected_time = utc(data['forecast_generated_at_utc'])
    valid = (source_time is not None and source_time == expected_time
             and provenance.get('predictions_sha256') in forecast_digest_variants(raw/'all_leagues_predictions.csv'))
    data['forecast_runtime'] = provenance if valid else {'status': 'NOT_RECORDED_OR_UNBOUND'}
    data['pre_kickoff_forecasts'] = sum(1 for row in read_csv(raw/'all_leagues_predictions.csv')
        if (kick := utc(row.get('kickoff_utc'))) and (kick-clock).total_seconds() >= 1200)
    return data


def write_generation_metadata(raw, summary):
    clock = utc(summary['generated_at_utc'])
    data = {'generated_at_utc': summary['generated_at_utc'],
        'predictions_sha256': hashlib.sha256((raw/'all_leagues_predictions.csv').read_bytes()).hexdigest(),
        'dependencies': current_health(raw.parent, clock)['dependencies'],
        'selection_policy_version': summary['selection_policy_version'],
        'model_code_sha256': hashlib.sha256(Path(__file__).with_name('football_value_pipeline_v2_standalone.py').read_bytes()).hexdigest()}
    from performance_tracking import write_json
    write_json(raw/'pipeline_run_metadata.json', data)


def write_report(root, metrics, clock):
    """Keep one reviewed observation per UTC day; never reinterpret old snapshots."""
    from performance_tracking import write_json, snapshots
    output = root/'performance'; data = current_health(root, clock)
    data.update(reviewed_at_utc=clock.isoformat(), selection_policy_groups=metrics.get('groups', {}).get('policy', {}),
        weekly_performance=metrics.get('groups', {}).get('week', {}),
        evidence={'graded_selections': metrics['shortlist']['graded'],
                  'prediction_fixtures_graded': metrics['prediction_fixtures_graded'],
                  'model_improvement_established': False,
                  'assessment': 'Forward evidence collection; improvements are not assumed from software or data changes.'})
    capture_rows = []; capture_counts = Counter()
    for meta, _, _ in snapshots(root):
        directory = output/'snapshots'/meta['git_commit_sha'][:16]
        path = directory/'pipeline_health.json'
        digest = meta.get('sha256', {}).get(path.name)
        valid = digest is not None and path.exists() and hashlib.sha256(path.read_bytes()).hexdigest() == digest
        frozen = read(path, {}) if valid else {}
        row = {'commit': meta['git_commit_sha'], 'captured_at_utc': meta['captured_at_utc'],
               'policy': meta.get('selection_policy_version'), 'health': frozen or None, 'experiments': {}}
        for name in ('goal_blend_experiment', 'market_led_experiment', 'filter_sensitivity_experiment', 'benchmark_forward_experiment', 'totals_anchor_experiment'):
            sidecar = directory/(name+'.json'); expected = meta.get('sha256', {}).get(sidecar.name)
            state = 'CAPTURED' if expected and sidecar.exists() and hashlib.sha256(sidecar.read_bytes()).hexdigest() == expected else (
                'MISSING_OR_TAMPERED' if expected else frozen.get('experiments', {}).get(name, 'LEGACY_NOT_RECORDED'))
            row['experiments'][name] = state; capture_counts[name+':'+state] += 1
        parent_path=directory/'goal_blend_experiment.json'
        parent=read(parent_path,{}) if row['experiments']['goal_blend_experiment']=='CAPTURED' else {}
        extension=parent.get('recency_experiment')
        from recency_experiment import valid_extension
        state=('CAPTURED' if valid_extension(extension,parent.get('generated_at_utc')) else
            'PRESENT_BUT_REJECTED' if extension is not None else
            frozen.get('experiments',{}).get('recency_experiment','LEGACY_NOT_RECORDED'))
        row['experiments']['recency_experiment']=state
        capture_counts['recency_experiment:'+state]+=1
        capture_rows.append(row)
    data['snapshot_capture_history'] = capture_rows
    data['experiment_capture_counts'] = dict(capture_counts)
    data['experimental_reports'] = {name:read(output/name/'summary.json', {}) for name in
        ('goal_blend_experiment', 'market_led_experiment', 'recency_experiment', 'filter_sensitivity_experiment', 'benchmark_forward_experiment', 'totals_anchor_experiment')}
    data['review_queue']=read(output/'experiment_review_queue.json',{})
    data['closing_odds']=read(output/'closing_odds/summary.json',{})
    history = read(output/'health_history.json', {'schema_version': 1, 'days': {}})
    observation = {k:v for k,v in data.items() if k != 'snapshot_capture_history'}
    observation['shortlist_performance'] = metrics['shortlist']
    history['days'][clock.date().isoformat()] = observation
    write_json(output/'health_history.json', history)
    write_json(output/'pipeline_health.json', data)
    lines = ['## Data, execution and experiment health', '',
             '| League | Model training end | Matches | Days since result | Source check |',
             '|---|---|---:|---:|---|']
    for league, info in data['training'].items():
        status = info.get('current_source_health', info['forecast_training_health']).get('status', 'NOT_RECORDED')
        lines.append(f"| {league} | {info['training_end']} | {info['training_matches']} | {info['days_since_latest_result']} | {status} |")
    quote = data['quote_audit']
    lines += ['', 'Latest shortlist audit: '+json.dumps(quote, ensure_ascii=False)+'.', '',
        'Source refresh does not retrain stored forecasts. Days since the last match do not by themselves establish missing data.', '',
        '| Snapshot | Goal blend | Market led | Recency | Filter sensitivity |', '|---|---|---|---|---|']
    for row in capture_rows[-20:]:
        lines.append(f"| {row['commit'][:12]} | {row['experiments']['goal_blend_experiment']} | {row['experiments']['market_led_experiment']} | {row['experiments']['recency_experiment']} | {row['experiments']['filter_sensitivity_experiment']} |")
    lines += ['', 'Dependency versions at review: '+json.dumps(data['dependencies'])+'. Forecast-generation versions are recorded in new frozen snapshot health; legacy generation environments are unknown.', '',
        'Closing odds: [report](closing_odds/report.md). Locally observed near-close quotes, coverage and offered-price comparisons; official close and accepted execution are unverified.', '',
        'Totals anchoring: [report](totals_anchor_experiment/report.md). Separate Pinnacle trial, no production probability changes.', '',
        'Experiment review queue: [report](experiment_review_queue.md). Benchmark candidate capture and readiness are evaluated automatically; no production promotion.', '',
        'Filter sensitivity: [report](filter_sensitivity_experiment/report.md). Frozen 1.5%, 3% and 5% adjusted EV policies; production unchanged.', '',
        'Recency comparisons: [report](recency_experiment/report.md). Raw goal probabilities, chronological selection/audit and paired forward scores; no automatic promotion.', '',
        'Daily observations: [health_history.json](health_history.json). Frozen forecast health: [pipeline_health.json](pipeline_health.json).', '',
        'Policy and gameweek results above show sample counts, ROI and calibration. Compare experiments on paired settled forecasts; small samples and changing cohorts cannot establish improvement. Historical missing experimental data is not backfilled.', '']
    path = output/'README.md'
    if path.exists():
        path.write_text(path.read_text(encoding='utf-8')+'\n'+'\n'.join(lines), encoding='utf-8')
    from performance_excel import add_health_sheet
    add_health_sheet(root, data, history)
    return data
