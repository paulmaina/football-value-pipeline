"""Fixed forward-only probability/calibration policies; no automatic promotion.

Each candidate changes one input only. Frozen forecasts, validation evidence
and execution settings permit deterministic replay before capture and review.
"""
from datetime import timedelta
import hashlib
import json
import math

import numpy as np
import pandas as pd

VERSION = 'shortlist-probability-calibration-v1'
BASELINE_POLICY = '72h-six-markets-dc12-probability-odds-net-ev15-v9'
NAME = 'shortlist_policy_experiment'
VARIANTS = {
    'control': {},
    'blended_lower': {'blended_shift': -.03},
    'blended_higher': {'blended_shift': .03},
    'raw_lower': {'raw_shift': -.03},
    'raw_higher': {'raw_shift': .03},
    'adjusted_lower': {'adjusted_shift': -.03},
    'adjusted_higher': {'adjusted_shift': .03},
    'penalty_half': {'penalty_multiplier': .5},
    'penalty_stronger': {'penalty_multiplier': 1.5},
}
SELECTED = {'SHORTLISTED', 'SHORTLISTED_PROVISIONAL'}
NOTE = ('Fixed one-factor comparisons, not an optimisation search. All variants use the same '
        'first eligible pre-kickoff fixtures, quotes, development-only calibration evidence '
        'and fixed audit/quote/matching gates. Primary returns use STRICT picks only; '
        'PROVISIONAL rows are watchlist simulations. Returns are simulated at frozen quotes '
        'after configured costs, not actual execution. Selected cohorts can differ: their '
        'Brier/ROI differences are not paired forecast improvements. Paired returns below '
        'use one unit per strict selection and zero for no selection on every verified fixture. '
        'Weekly block bootstrap intervals are exploratory, unadjusted for eight comparisons '
        'and unavailable before six weeks/100 verified fixtures. No automatic promotion; '
        'choose a policy only after review, then confirm it on a later untouched period.')


def clean(value):
    return json.loads(json.dumps(value, allow_nan=False, sort_keys=True))


def equivalent(actual, expected):
    """Allow only CSV/JSON floating-point roundoff, never semantic changes."""
    if isinstance(expected, dict):
        return isinstance(actual, dict) and actual.keys() == expected.keys() and all(equivalent(actual[k], v) for k, v in expected.items())
    if isinstance(expected, list):
        return isinstance(actual, list) and len(actual) == len(expected) and all(equivalent(a, b) for a, b in zip(actual, expected))
    if isinstance(expected, (int, float)) and not isinstance(expected, bool):
        return isinstance(actual, (int, float)) and not isinstance(actual, bool) and math.isfinite(actual) and abs(actual-expected) <= 1e-9
    return type(actual) is type(expected) and actual == expected


def decision_rows(predictions, generated, reliability, execution):
    from conservative_bet_filter import build_conservative_shortlist
    from filter_sensitivity_experiment import clean as clean_frame
    from performance_tracking import utc
    predictions = predictions.copy()
    # pandas uses NaN for an absent quote name; the archive CSV reader uses
    # empty strings. Both mean missing, and must replay as JSON null.
    for column in predictions.columns:
        if column == 'fixture_id' or (column.startswith('best_') and column.endswith('_bookmaker')):
            predictions[column] = predictions[column].map(
                lambda value: None if pd.isna(value) or value == '' else value)
    if 'market_blend_applied' in predictions:
        # The archive reader returns CSV strings; preserve the original boolean
        # semantics when replaying, rather than accepting truthy text generally.
        predictions['market_blend_applied'] = predictions['market_blend_applied'].map(
            lambda value: value if not isinstance(value, str) else value in ('True', '1', '1.0'))
    rows = []
    for variant, policy in VARIANTS.items():
        _, decisions, summary = build_conservative_shortlist(
            predictions, as_of=utc(generated), market_reliability=reliability,
            research_policy=policy, execution_policy=execution)
        if summary['selection_policy_version'] != BASELINE_POLICY:
            raise ValueError('Unsupported baseline shortlist policy; preserve replay compatibility')
        rows.extend({**row, 'variant_id': variant} for row in clean_frame(decisions))
    return rows


def write_experiment(predictions, raw, summary, production_decisions, reliability):
    from filter_sensitivity_experiment import clean as clean_frame
    from performance_tracking import write_json
    from quote_policy import load_policy
    execution = load_policy()
    rows = decision_rows(predictions, summary['generated_at_utc'], reliability, execution)
    if [dict((k, v) for k, v in row.items() if k != 'variant_id')
            for row in rows if row['variant_id'] == 'control'] != clean_frame(production_decisions):
        raise ValueError('Research control differs from production decisions')
    data = {'version': VERSION, 'generated_at_utc': summary['generated_at_utc'],
            'selection_policy_version': summary['selection_policy_version'],
            'variants': clean(VARIANTS), 'execution_policy': execution,
            'validation_evidence': clean(reliability),
            'predictions_sha256': hashlib.sha256((raw/'all_leagues_predictions.csv').read_bytes()).hexdigest(),
            'rows': rows}
    write_json(raw/(NAME+'.json'), data)
    return data


def validate(data, generated, predictions):
    from performance_tracking import utc, fixture_key
    from quote_policy import validate_policy
    if not isinstance(data, dict) or data.get('version') != VERSION or data.get('variants') != VARIANTS:
        raise ValueError('Invalid shortlist policy version/grid')
    if data.get('selection_policy_version') != BASELINE_POLICY:
        raise ValueError('Unbound baseline policy')
    if utc(generated) is None or utc(data.get('generated_at_utc')) != utc(generated):
        raise ValueError('Unbound shortlist policy generation time')
    keys = [fixture_key(row) for row in predictions]
    if len(keys) != len(set(keys)):
        raise ValueError('Duplicate source fixture')
    reliability = data.get('validation_evidence')
    if reliability is not None and not isinstance(reliability, dict):
        raise ValueError('Invalid frozen validation evidence')
    execution = validate_policy(data.get('execution_policy'))
    if execution != data.get('execution_policy'):
        raise ValueError('Invalid frozen execution policy')
    expected = decision_rows(pd.DataFrame(predictions), generated, reliability, execution)
    # JSON is canonicalised so NaN, duplicates, missing rows, altered rankings,
    # rejection reasons, prices, costs, penalties and thresholds all fail closed.
    if not equivalent(clean(data.get('rows')), clean(expected)):
        raise ValueError('Candidate decisions differ from frozen replay')


def validate_control(data, picks):
    from performance_tracking import fixture_key
    actual = {(fixture_key(r), r['market'], r.get('selection_tier')) for r in picks}
    expected = {(fixture_key(r), r['market'], r.get('selection_tier')) for r in data['rows']
                if r['variant_id'] == 'control' and r['decision'] in SELECTED}
    if actual != expected or len(actual) != len(picks):
        raise ValueError('Control differs from production shortlist')


def capture_file(raw, generated):
    from performance_tracking import load_json, read_csv
    from forecast_integrity import forecast_digest_variants
    path = raw/(NAME+'.json')
    if not path.exists():
        return None
    data = load_json(path, {})
    if data.get('predictions_sha256') not in forecast_digest_variants(raw/'all_leagues_predictions.csv'):
        raise ValueError('Shortlist policy forecast hash mismatch')
    validate(data, generated, read_csv(raw/'all_leagues_predictions.csv'))
    validate_control(data, read_csv(raw/'conservative_bet_shortlist.csv'))
    # Bind the frozen validation inputs to the reports used for this run.
    evidence = data['validation_evidence']
    if evidence is not None:
        reports = [load_json(p, {}) for p in sorted(raw.glob('*_goal_market_validation.json'))]
        if any(not isinstance(r, dict) or not isinstance(r.get('league'), str) for r in reports):
            raise ValueError('Invalid current validation report')
        current = {r['league']: r for r in reports}
        if any(current.get(league) != report for league, report in evidence.items()):
            raise ValueError('Frozen validation evidence differs from current reports')
    return path


def frozen(root, archived):
    from performance_tracking import load_json, utc, fixture_key
    from forecast_integrity import forecast_digest_variants
    rows, rejected, seen = [], [], set()
    for meta, predictions, picks in archived:
        directory = root/'performance/snapshots'/meta['git_commit_sha'][:16]
        path = directory/(NAME+'.json')
        digest = meta.get('sha256', {}).get(path.name)
        if not digest:
            continue  # No backfill of snapshots created before this experiment.
        try:
            if not path.exists() or hashlib.sha256(path.read_bytes()).hexdigest() != digest:
                raise ValueError('Invalid archived policy hash')
            data = load_json(path, {})
            if data.get('predictions_sha256') not in forecast_digest_variants(directory/'predictions.csv'):
                raise ValueError('Unbound archived forecasts')
            if data['selection_policy_version'] != meta['selection_policy_version']:
                raise ValueError('Unbound archived policy')
            validate(data, meta['generated_at_utc'], predictions)
            validate_control(data, picks)
        except (ValueError, TypeError, KeyError):
            rejected.append(meta['git_commit_sha'])
            continue
        new = set()
        for row in data['rows']:
            key = fixture_key(row)
            kickoff = utc(row.get('kickoff_utc'))
            if key in seen or kickoff is None:
                continue
            generated, captured = utc(meta['generated_at_utc']), utc(meta['captured_at_utc'])
            if max(generated, captured) > kickoff-timedelta(minutes=20) or kickoff > generated+timedelta(hours=72):
                continue
            new.add(key)
            rows.append({**row, 'fixture_key': key, 'snapshot_commit': meta['git_commit_sha'],
                         'snapshot_captured_utc': meta['captured_at_utc'],
                         'selection_policy_version': data['selection_policy_version']})
        seen.update(new)
    return rows, rejected


def statistics(rows):
    from filter_sensitivity_experiment import statistics as selection_stats
    result = selection_stats(rows)
    settled = [r for r in rows if r['outcome'] is not None]
    result['log_loss'] = sum(r['log_loss'] for r in settled)/len(settled) if settled else None
    result['calibration_gap'] = (result['mean_probability']-result['observed_rate']) if settled else None
    return result


def block_interval(blocks):
    """Resample whole weeks, retaining all correlated fixtures within a week."""
    if len(blocks) < 6 or sum(len(block) for block in blocks.values()) < 100:
        return None
    totals = np.array([sum(block) for block in blocks.values()])
    sizes = np.array([len(block) for block in blocks.values()])
    draw = np.random.default_rng(20261015).integers(0, len(totals), size=(2000, len(totals)))
    means = totals[draw].sum(axis=1)/sizes[draw].sum(axis=1)
    return [float(x) for x in np.quantile(means, [.025, .975])]


def paired_probability_scores(coverage, variant):
    from performance_tracking import utc
    control = {(r['fixture_key'], r['market']): r for r in coverage
               if r['variant_id'] == 'control' and r['brier'] is not None}
    fixture_deltas = {}
    for row in coverage:
        key = (row['fixture_key'], row['market'])
        if row['variant_id'] != variant or row['brier'] is None or key not in control:
            continue
        year, week, _ = utc(row['kickoff_utc']).isocalendar()
        delta = fixture_deltas.setdefault(row['fixture_key'], {'week': f'{year}-W{week:02d}', 'brier': [], 'log_loss': []})
        for metric in ('brier', 'log_loss'):
            delta[metric].append(row[metric]-control[key][metric])
    result = {'variant_id': variant, 'paired_fixtures': len(fixture_deltas)}
    for metric in ('brier', 'log_loss'):
        blocks = {}
        for fixture in fixture_deltas.values():
            blocks.setdefault(fixture['week'], []).append(sum(fixture[metric])/len(fixture[metric]))
        values = [x for block in blocks.values() for x in block]
        result[metric+'_mean_delta'] = sum(values)/len(values) if values else None
        result[metric+'_weekly_bootstrap95'] = block_interval(blocks)
    return result


def paired_returns(coverage, variant):
    from performance_tracking import utc
    fixtures = {r['fixture_key']: r for r in coverage if r['outcome'] is not None}
    returns = {key: {'control': 0.0, variant: 0.0} for key in fixtures}
    for row in coverage:
        if row['outcome'] is not None and row['variant_id'] in returns[row['fixture_key']] and row['decision'] == 'SHORTLISTED':
            returns[row['fixture_key']][row['variant_id']] = row['unit_profit']
    blocks = {}
    for key, row in fixtures.items():
        year, week, _ = utc(row['kickoff_utc']).isocalendar()
        blocks.setdefault(f'{year}-W{week:02d}', []).append(returns[key][variant]-returns[key]['control'])
    values = [x for block in blocks.values() for x in block]
    interval = block_interval(blocks)
    return {'variant_id': variant, 'verified_fixtures': len(values), 'iso_weeks': len(blocks),
            'mean_profit_delta_per_fixture': sum(values)/len(values) if values else None,
            'weekly_block_bootstrap95': interval}


def evaluate(root, archived, records, clock):
    from performance_tracking import utc, fixture_match, result_for_market
    records = [r for r in records if r.get('source_status') == 'FINISHED' and r.get('source') == 'football-data.org/v4']
    candidates, rejected = frozen(root, archived)
    coverage, selections, matches = [], [], {}
    for row in candidates:
        key = row['fixture_key']
        if key not in matches:
            matches[key] = fixture_match(row, records)
        match, state = matches[key]
        if utc(row['kickoff_utc']) > clock-timedelta(hours=2):
            match, state = None, 'PENDING_KICKOFF_OR_FINAL_SCORE'
        outcome = int(result_for_market(row['market'], match['home_goals'], match['away_goals'])) if match else None
        p = row['rank_probability']
        safe = min(1-1e-9, max(1e-9, p)) if p is not None else None
        price, cost = row['offered_decimal_odds'], row['per_stake_cost']
        year, week, _ = utc(row['kickoff_utc']).isocalendar()
        item = {**row, 'result_status': state, 'outcome': outcome,
                'week': f'{year}-W{week:02d}',
                'source_match_id': match['match_id'] if match else None,
                'brier': (p-outcome)**2 if p is not None and outcome is not None else None,
                'log_loss': -(outcome*math.log(safe)+(1-outcome)*math.log(1-safe)) if safe is not None and outcome is not None else None,
                'unit_profit': outcome*price-1-cost if outcome is not None and price is not None else None}
        coverage.append(item)
        if row['decision'] in SELECTED:
            selections.append(item)
    comparisons, breakdowns, probability_scores = [], [], []
    for variant in VARIANTS:
        cohort = [r for r in selections if r['variant_id'] == variant]
        for tier in ('STRICT', 'PROVISIONAL', 'ALL'):
            comparisons.append({'variant_id': variant, 'tier': tier,
                                 **statistics([r for r in cohort if tier == 'ALL' or r['selection_tier'] == tier])})
        for field in ('league', 'market', 'week'):
            for value in sorted({r[field] for r in cohort}):
                breakdowns.append({'variant_id': variant, 'dimension': field, 'value': value,
                                   **statistics([r for r in cohort if r[field] == value and r['selection_tier'] == 'STRICT'])})
        common = [r for r in coverage if r['variant_id'] == variant and r['brier'] is not None]
        probability_scores.append({'variant_id': variant, 'verified_fixture_markets': len(common),
            'brier': sum(r['brier'] for r in common)/len(common) if common else None,
            'log_loss': sum(r['log_loss'] for r in common)/len(common) if common else None,
            'calibration_gap': sum(r['rank_probability']-r['outcome'] for r in common)/len(common) if common else None})
    total = len({r['fixture_key'] for r in coverage})
    verified = len({r['fixture_key'] for r in coverage if r['outcome'] is not None})
    paired = [paired_returns(coverage, v) for v in VARIANTS if v != 'control']
    weeks = max((r['iso_weeks'] for r in paired), default=0)
    fraction = verified/total if total else 0.0
    enough = verified >= 300 and weeks >= 6 and fraction >= .8
    summary = {'version': VERSION, 'reviewed_at_utc': clock.isoformat(), 'variants': clean(VARIANTS),
        'total_fixtures': total, 'verified_fixtures': verified, 'verified_coverage': fraction,
        'gameweeks': weeks, 'candidate_decisions': len(coverage), 'comparisons': comparisons,
        'breakdowns': breakdowns, 'common_cohort_probability_scores': probability_scores,
        'paired_probability_deltas': [paired_probability_scores(coverage, v) for v in VARIANTS if v != 'control'],
        'paired_strict_returns': paired, 'rejected_snapshot_commits': rejected,
        'status': 'DATA_QUALITY_BLOCKED' if rejected else 'READY_FOR_REVIEW' if enough else 'COLLECT_MORE_DATA',
        'review_gates': {'minimum_paired_fixtures': 300, 'minimum_gameweeks': 6, 'minimum_verified_coverage': .8},
        'automatic_production_change': False, 'note': NOTE}
    return summary, selections, coverage


def review_experiment(root, archived, records, clock):
    from performance_tracking import write_json, write_csv
    summary, selections, coverage = evaluate(root, archived, records, clock)
    dest = root/'performance'/NAME
    write_json(dest/'summary.json', summary)
    for name, rows in [('selections', selections), ('candidate_decisions', coverage)]:
        write_csv(dest/(name+'.csv'), rows, list(rows[0]) if rows else ['fixture_key', 'variant_id', 'decision', 'outcome'])
    lines = ['# Shortlist probability and calibration comparison', '', NOTE, '',
             'Status: '+summary['status'], '',
             '| Variant | Tier | Selected | Settled | Net ROI | Brier | Log loss |',
             '|---|---|---:|---:|---:|---:|---:|']
    def number(value):
        return f'{value:.4f}' if value is not None else 'n.a.'
    for row in summary['comparisons']:
        lines.append(f"| {row['variant_id']} | {row['tier']} | {row['selected']} | {row['graded']} | {number(row['flat_stake_roi'])} | {number(row['brier'])} | {number(row['log_loss'])} |")
    lines += ['', 'Frozen grid: blended/raw/adjusted cutoffs each ±3 percentage points independently; calibration penalty ×0.5 or ×1.5. All other settings stay fixed.',
              '', 'Detailed calibration bins, drawdowns, weekly/league/market results, common-cohort scores and paired return uncertainty are in summary.json. All rejected candidates are retained in candidate_decisions.csv. Old captures are never backfilled.', '']
    (dest/'report.md').write_text('\n'.join(lines), encoding='utf-8')
    return summary


def validate_report(root):
    from performance_tracking import load_json, snapshots, utc, read_csv
    dest = root/'performance'/NAME
    actual = load_json(dest/'summary.json', {})
    expected, selections, coverage = evaluate(root, snapshots(root),
        list(load_json(root/'performance/verified_results.json', {}).values()), utc(actual['reviewed_at_utc']))
    if actual != expected:
        raise ValueError('Shortlist policy summary differs from frozen evidence')
    for name, rows in [('selections', selections), ('candidate_decisions', coverage)]:
        saved = read_csv(dest/(name+'.csv'))
        if len(saved) != len(rows):
            raise ValueError('Incomplete shortlist policy ledger')
        for a, b in zip(saved, rows):
            for key, value in b.items():
                if value is None:
                    valid = a.get(key) in ('', None)
                elif isinstance(value, (int, float)):
                    valid = math.isfinite(float(a[key])) and abs(float(a[key])-value) <= 1e-9
                else:
                    valid = str(value) == a.get(key)
                if not valid:
                    raise ValueError('Inconsistent shortlist policy ledger value')
    return True
