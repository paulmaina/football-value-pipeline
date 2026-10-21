"""Pre-registered forward comparison of shortlist probability/EV weights."""
from datetime import timedelta
import hashlib
import math
import pandas as pd
from shortlist_policy_experiment import clean, equivalent, statistics, block_interval

NAME = 'shortlist_weight_experiment'
LEGACY_VERSION = 'shortlist-probability-ev-weights-v1'
VERSION = 'shortlist-probability-ev-weights-v2'
TEN_MATCH_BASELINE_POLICY = '48h-top-ten-probability-ev-no-under35-v14'
PREVIOUS_TWELVE_MATCH_POLICY = '48h-top-twelve-probability-ev-no-under35-v15'
BASELINE_POLICY = '48h-top-twelve-1x2-double-chance-over15-v16'
BALANCED_POLICIES = (TEN_MATCH_BASELINE_POLICY, PREVIOUS_TWELVE_MATCH_POLICY, BASELINE_POLICY)
LEGACY_VARIANTS = {
    'control': {},
    'probability_100_ev_0': {'probability_weight': 1.0},
    'probability_75_ev_25': {'probability_weight': .75},
    'probability_25_ev_75': {'probability_weight': .25},
}
ADAPTIVE_ID = 'adaptive_evidence'
ADAPTIVE_RULE = {
    'version': 'development-evidence-v1',
    'minimum_probability_weight': .5, 'maximum_probability_weight': .9,
    'development_target': 300, 'penalty_limit': .10,
    'disagreement_limit': .25, 'max_quote_age_hours': 24,
}
VARIANTS = {**LEGACY_VARIANTS, ADAPTIVE_ID: {'adaptive_rule': ADAPTIVE_RULE}}
SELECTED = {'SHORTLISTED', 'SHORTLISTED_PROVISIONAL'}
NOTE = ('Forward-only paper comparison: 100/0, 75/25, 50/50 (control), 25/75 probability/EV weights and adaptive evidence weights. '
        'All use the same frozen candidate market pool within each capture, 48-hour horizon, prices, costs and one-market-per-match policy cap (12 in v15/v16; 10 in archived v14). '
        'Primary results include ALL selections, with STRICT/PROVISIONAL shown separately. '
        'First eligible usable capture per fixture only; no historical backfill or repeated stakes. '
        'Win rates include Wilson intervals. Profit differences pair each verified usable fixture with control, '
        'using one unit for a selection and zero if skipped. Weekly block bootstrap intervals are exploratory, '
        'unadjusted for four comparisons in v2 (three in legacy v1), and unavailable before six weeks/100 paired fixtures. '
        'Selection-cohort Brier scores do not prove improved forecasts. Readiness requires 300 verified usable '
        'fixtures, six ISO weeks, 80% resolved coverage and 100 settled picks per weighting. '
        'Adaptive probability weight ranges from 50% to 90%, using only frozen development support, '
        'development calibration penalties, raw model/reference disagreement and quote age. '
        'These bounds are a pre-registered hypothesis, not fitted optimal weights or a safety guarantee. '
        'Legacy v1 results remain a separate cohort; v2 readiness and paired returns use only contemporaneous v2 captures. '
        'No automatic production change. Confirm any chosen weighting on a later untouched period.')


def variants_for(version):
    if version == LEGACY_VERSION:
        return LEGACY_VARIANTS
    if version == VERSION:
        return VARIANTS
    raise ValueError('Invalid shortlist policy version/grid')


def adaptive_weight(row):
    """Frozen, development-only evidence; no outcomes or audit metrics enter weights."""
    def bounded(value, scale, *, invert=False):
        if isinstance(value, bool):
            return 0.0
        try:
            value = float(value)
        except (ValueError, TypeError):
            return 0.0
        if not math.isfinite(value) or value < 0:
            return 0.0
        fraction = min(1.0, value/scale)
        return 1-fraction if invert else fraction
    rule = ADAPTIVE_RULE
    try:
        raw, reference = float(row['raw_dc_probability']), float(row['market_probability'])
        gap = abs(raw-reference) if all(math.isfinite(x) and 0 <= x <= 1 for x in (raw, reference)) else None
    except (ValueError, TypeError, KeyError):
        gap = None
    factors = {
        'adaptive_history_support': bounded(row.get('development_validation_matches'), rule['development_target']),
        'adaptive_calibration_quality': bounded(row.get('calibration_penalty'), rule['penalty_limit'], invert=True),
        'adaptive_market_agreement': bounded(gap, rule['disagreement_limit'], invert=True),
        'adaptive_quote_freshness': bounded(row.get('odds_age_hours'), rule['max_quote_age_hours'], invert=True),
    }
    quality = math.prod(factors.values())
    weight = rule['maximum_probability_weight']-(rule['maximum_probability_weight']-rule['minimum_probability_weight'])*quality
    return {**factors, 'adaptive_evidence_quality': quality,
            'probability_weight_used': weight, 'ev_weight_used': 1-weight}


def adaptive_rows(controls, baseline_policy):
    """Re-rank the control's identical usable pool; production code is untouched."""
    from performance_tracking import fixture_key
    rows = [{**r, 'variant_id': ADAPTIVE_ID, **adaptive_weight(r)} for r in controls]
    usable = [r for r in rows if r['decision'] != 'REJECTED']
    for row in usable:
        row['selection_score'] = (row['probability_weight_used']*row['probability_percentile']
                                  + row['ev_weight_used']*row['ev_percentile'])
        row.update(decision='NOT_SELECTED', selection_tier=None, near_miss_reason=None)
    ranked = sorted(usable, key=lambda r: (
        -r['selection_score'], -r['rank_probability'], -r['conservative_estimated_ev'],
        -r['offered_decimal_odds'], r['kickoff_utc'], r['league'], r['home_team'], r['away_team']))
    cap = 12 if baseline_policy in (BASELINE_POLICY, PREVIOUS_TWELVE_MATCH_POLICY) else 10
    chosen = set()
    for row in ranked:
        key = fixture_key(row)
        if key in chosen or len(chosen) >= cap:
            continue
        chosen.add(key)
        warning = row['rejection_reasons']
        row.update(decision='SHORTLISTED_PROVISIONAL' if warning else 'SHORTLISTED',
                   selection_tier='PROVISIONAL' if warning else 'STRICT', near_miss_reason=warning or None)
    return rows


def decision_rows(predictions, generated, reliability, execution, baseline_policy=None, *, version=VERSION):
    from shortlist_policy_experiment import decision_rows as shared_decisions
    grid = variants_for(version)
    baseline_policy = baseline_policy or BASELINE_POLICY
    rows = shared_decisions(predictions, generated, reliability, execution,
        baseline_policy=baseline_policy, variants={k:v for k,v in grid.items() if k != ADAPTIVE_ID})
    if ADAPTIVE_ID in grid:
        rows += adaptive_rows([r for r in rows if r['variant_id'] == 'control'], baseline_policy)
    return rows


def write_experiment(predictions, raw, summary, production_decisions, reliability):
    from filter_sensitivity_experiment import clean as clean_frame
    from performance_tracking import write_json
    from quote_policy import load_policy
    if summary['selection_policy_version'] != BASELINE_POLICY:
        raise ValueError('Weight experiment requires the current 48-hour production policy')
    execution = load_policy()
    rows = decision_rows(predictions, summary['generated_at_utc'], reliability, execution,
                         baseline_policy=summary['selection_policy_version'])
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
    if not isinstance(data, dict) or data.get('variants') != variants_for(data.get('version')):
        raise ValueError('Invalid shortlist policy version/grid')
    if data.get('selection_policy_version') not in BALANCED_POLICIES:
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
    expected = decision_rows(pd.DataFrame(predictions), generated, reliability, execution,
                             baseline_policy=data['selection_policy_version'], version=data['version'])
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
    controls = {(fixture_key(r), r['market']):r for r in data['rows']
                if r['variant_id'] == 'control' and r['decision'] in SELECTED}
    for pick in picks:
        row = controls[(fixture_key(pick), pick['market'])]
        if pick.get('bookmaker') != row['bookmaker']:
            raise ValueError('Control bookmaker differs from production shortlist')
        for field in ('rank_probability', 'offered_decimal_odds', 'conservative_estimated_ev',
                      'per_stake_cost', 'selection_score', 'probability_percentile', 'ev_percentile'):
            try:
                value = float(pick[field])
            except (KeyError, TypeError, ValueError):
                raise ValueError('Missing production control value') from None
            if not math.isfinite(value) or abs(value-row[field]) > 1e-9:
                raise ValueError('Control values differ from production shortlist')


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
        usable = {fixture_key(r) for r in data['rows'] if r['decision'] != 'REJECTED'}
        new = set()
        for row in data['rows']:
            key = fixture_key(row)
            kickoff = utc(row.get('kickoff_utc'))
            if (data['version'], key) in seen or key not in usable or kickoff is None:
                continue
            generated, captured = utc(meta['generated_at_utc']), utc(meta['captured_at_utc'])
            horizon = 48 if data['selection_policy_version'] in BALANCED_POLICIES else 72
            if max(generated, captured) > kickoff-timedelta(minutes=20) or kickoff > generated+timedelta(hours=horizon):
                continue
            new.add((data['version'], key))
            rows.append({**row, 'fixture_key': key, 'snapshot_commit': meta['git_commit_sha'],
                         'snapshot_captured_utc': meta['captured_at_utc'],
                         'selection_policy_version': data['selection_policy_version'],
                         'experiment_version': data['version']})
        seen.update(new)
    return rows, rejected



def paired_returns(coverage, variant):
    from performance_tracking import utc
    fixtures = {r['fixture_key']: r for r in coverage if r['outcome'] is not None}
    returns = {key: {'control': 0.0, variant: 0.0} for key in fixtures}
    for row in coverage:
        if row['outcome'] is not None and row['decision'] in SELECTED and row['variant_id'] in returns[row['fixture_key']]:
            returns[row['fixture_key']][row['variant_id']] = row['unit_profit']
    blocks = {}
    for key, row in fixtures.items():
        year, week, _ = utc(row['kickoff_utc']).isocalendar()
        blocks.setdefault(f'{year}-W{week:02d}', []).append(returns[key][variant]-returns[key]['control'])
    values = [value for block in blocks.values() for value in block]
    return {'variant_id': variant, 'verified_fixtures': len(values), 'iso_weeks': len(blocks),
        'mean_profit_delta_per_fixture': sum(values)/len(values) if values else None,
        'weekly_block_bootstrap95': block_interval(blocks)}


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
        item = {**row, 'result_status': state, 'outcome': outcome, 'week': f'{year}-W{week:02d}',
            'source_match_id': match['match_id'] if match else None,
            'brier': (p-outcome)**2 if p is not None and outcome is not None else None,
            'log_loss': -(outcome*math.log(safe)+(1-outcome)*math.log(1-safe)) if safe is not None and outcome is not None else None,
            'unit_profit': outcome*price-1-cost if outcome is not None and price is not None else None}
        coverage.append(item)
        if row['decision'] in SELECTED:
            selections.append(item)
    current = [r for r in coverage if r.get('experiment_version', VERSION) == VERSION]
    summary = cohort_summary(current, VERSION, rejected, clock)
    summary['legacy_cohorts'] = [cohort_summary(
        [r for r in coverage if r.get('experiment_version') == LEGACY_VERSION],
        LEGACY_VERSION, rejected, clock)] if any(r.get('experiment_version') == LEGACY_VERSION for r in coverage) else []
    return summary, selections, coverage


def cohort_summary(coverage, version, rejected, clock):
    """Never borrow readiness or control returns from a different trial version."""
    from goal_market_validation import _wilson_interval
    selections = [r for r in coverage if r['decision'] in SELECTED]
    def stats(rows):
        result = statistics(rows)
        result['assessment'] = 'DESCRIPTIVE_ONLY_SEE_REVIEW_GATES'
        result['win_rate_wilson95'] = _wilson_interval(result['wins'], result['graded'])
        return result
    comparisons, breakdowns = [], []
    grid = variants_for(version)
    for variant, policy in grid.items():
        cohort = [r for r in selections if r['variant_id'] == variant]
        weight = None if variant == ADAPTIVE_ID else policy.get('probability_weight', .5)
        for tier in ('ALL', 'STRICT', 'PROVISIONAL'):
            selected = [r for r in cohort if tier == 'ALL' or r['selection_tier'] == tier]
            used = [r['probability_weight_used'] for r in selected] if variant == ADAPTIVE_ID else []
            comparisons.append({'variant_id': variant, 'probability_weight': weight,
                'ev_weight': None if weight is None else 1-weight,
                'mean_probability_weight': sum(used)/len(used) if used else weight,
                'minimum_probability_weight': min(used) if used else weight,
                'maximum_probability_weight': max(used) if used else weight,
                'tier': tier, **stats(selected)})
        for field in ('league', 'market', 'week'):
            for value in sorted({r[field] for r in cohort}):
                breakdowns.append({'variant_id': variant, 'dimension': field, 'value': value,
                    **stats([r for r in cohort if r[field] == value])})
    total = len({r['fixture_key'] for r in coverage})
    verified = len({r['fixture_key'] for r in coverage if r['outcome'] is not None})
    paired = [paired_returns(coverage, variant) for variant in grid if variant != 'control']
    weeks = max((r['iso_weeks'] for r in paired), default=0)
    fraction = verified/total if total else 0.0
    minimum_settled = min(r['graded'] for r in comparisons if r['tier'] == 'ALL')
    enough = verified >= 300 and weeks >= 6 and fraction >= .8 and minimum_settled >= 100
    summary = {'version': version, 'reviewed_at_utc': clock.isoformat(), 'variants': clean(grid),
        'total_fixtures': total, 'verified_fixtures': verified, 'verified_coverage': fraction,
        'gameweeks': weeks, 'minimum_settled_per_weighting': minimum_settled,
        'candidate_decisions': len(coverage), 'comparisons': comparisons, 'breakdowns': breakdowns,
        'primary_tier': 'ALL', 'paired_all_returns': paired, 'rejected_snapshot_commits': rejected,
        'status': 'DATA_QUALITY_BLOCKED' if rejected else 'READY_FOR_REVIEW' if enough else 'COLLECT_MORE_DATA',
        'review_gates': {'minimum_paired_fixtures': 300, 'minimum_gameweeks': 6,
            'minimum_verified_coverage': .8, 'minimum_settled_per_weighting': 100},
        'automatic_production_change': False, 'note': NOTE}
    return summary


def weight_label(row):
    if row['variant_id'] == ADAPTIVE_ID:
        return 'Adaptive evidence'
    return f"{row['probability_weight']:.0%} / {row['ev_weight']:.0%}"


def review_experiment(root, archived, records, clock):
    from performance_tracking import write_json, write_csv
    summary, selections, coverage = evaluate(root, archived, records, clock)
    dest = root/'performance'/NAME
    write_json(dest/'summary.json', summary)
    for name, rows in [('selections', selections), ('candidate_decisions', coverage)]:
        write_csv(dest/(name+'.csv'), rows, list(dict.fromkeys(k for r in rows for k in r)) if rows else ['fixture_key', 'variant_id', 'decision', 'outcome'])
    def number(value):
        return f'{value:.4f}' if value is not None else 'n.a.'
    lines = ['# Shortlist probability / EV weighting comparison', '', NOTE, '', 'Status: '+summary['status'], '',
        '| Probability / EV | Tier | Selected | Settled | Win rate | Win rate 95% interval | Net ROI | Profit (units) | Drawdown (units) |',
        '|---|---|---:|---:|---:|---|---:|---:|---:|']
    for cohort in [summary, *summary['legacy_cohorts']]:
        if cohort is not summary:
            lines += ['', '## Legacy v1 fixed-weight cohort (separate results)', '',
                '| Probability / EV | Tier | Selected | Settled | Win rate | Win rate 95% interval | Net ROI | Profit (units) | Drawdown (units) |',
                '|---|---|---:|---:|---:|---|---:|---:|---:|']
        for row in cohort['comparisons']:
            interval = row['win_rate_wilson95']
            interval_text = f'{interval[0]:.1%} to {interval[1]:.1%}' if interval else 'Collect more data'
            lines.append(f"| {weight_label(row)} | {row['tier']} | {row['selected']} | {row['graded']} | {number(row['observed_rate'])} | {interval_text} | {number(row['flat_stake_roi'])} | {number(row['profit_units'])} | {number(row['max_drawdown_units'])} |")
        lines += ['', '| Weighting | Brier | Log loss | Calibration gap | Mean probability weight | Min / max probability weight |',
            '|---|---:|---:|---:|---:|---|']
        for row in cohort['comparisons']:
            if row['tier'] != 'ALL':
                continue
            bounds = f"{number(row['minimum_probability_weight'])} / {number(row['maximum_probability_weight'])}"
            lines.append(f"| {weight_label(row)} | {number(row['brier'])} | {number(row['log_loss'])} | {number(row['calibration_gap'])} | {number(row['mean_probability_weight'])} | {bounds} |")
        lines += ['', '| Alternative | Profit delta / usable fixture vs 50/50 | Weekly bootstrap 95% interval |',
            '|---|---:|---|']
        for row in cohort['paired_all_returns']:
            interval = row['weekly_block_bootstrap95']
            text = f'{interval[0]:+.4f} to {interval[1]:+.4f}' if interval else 'Collect more data'
            lines.append(f"| {row['variant_id']} | {number(row['mean_profit_delta_per_fixture'])} | {text} |")
    lines += ['', 'Full calibration, Brier/log-loss diagnostics, league/market/week breakdowns and review gates are in summary.json. Frozen selections and every candidate decision are retained in CSV. A ready report permits review only; it never changes production.', '']
    (dest/'report.md').write_text('\n'.join(lines), encoding='utf-8')
    return summary


def validate_report(root):
    from performance_tracking import load_json, snapshots, utc, read_csv
    dest = root/'performance'/NAME
    actual = load_json(dest/'summary.json', {})
    expected, selections, coverage = evaluate(root, snapshots(root),
        list(load_json(root/'performance/verified_results.json', {}).values()), utc(actual['reviewed_at_utc']))
    if actual != expected:
        raise ValueError('Shortlist weight summary differs from frozen evidence')
    for name, rows in [('selections', selections), ('candidate_decisions', coverage)]:
        saved = read_csv(dest/(name+'.csv'))
        if len(saved) != len(rows):
            raise ValueError('Incomplete shortlist policy ledger')
        columns = set(k for row in rows for k in row)
        for a, b in zip(saved, rows):
            if set(a) != columns or any(a[k] not in ('', None) for k in set(a)-set(b)):
                raise ValueError('Unexpected shortlist policy ledger columns or values')
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
