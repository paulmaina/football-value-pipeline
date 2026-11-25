"""Offline CI and forward-review integrity checks. Never generate probabilities."""
from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
import math
import os
from pathlib import Path
import re
import subprocess
import sys
import xml.etree.ElementTree as ET
from zipfile import ZipFile

import shortlist_window

FORECAST_PATHS = (
    'football_output_v2/raw/current_run.json',
    'football_output_v2/raw/prediction_runs',
    'football_output_v2/raw/all_leagues_predictions.csv',
    'football_output_v2/raw/conservative_bet_shortlist.csv',
    'football_output_v2/raw/conservative_bet_summary.json',
)
# Every sidecar an archived snapshot may hold, including retired experiments. The retired experiments' files were
# removed from the committed snapshots on 25 Nov 2026 (metadata.json still lists them): absent is expected and
# silent; a copy that is present is still checked against its digest.
RETIRED_SIDECARS = ('goal_blend_experiment.json', 'market_led_experiment.json', 'filter_sensitivity_experiment.json', 'benchmark_forward_experiment.json', 'totals_anchor_experiment.json', 'model_reliability_experiment.json', 'shortlist_policy_experiment.json', 'shortlist_weight_experiment.json')
SIDECARS = (*RETIRED_SIDECARS, 'price_edge_tagged_candidates.csv', 'cagey_tier_shortlist.csv', 'cagey_correction_monitoring.csv', 'corners_shadow.csv', 'master_shortlist.csv', 'master_shortlist_audit.csv', 'master_shortlist_new.csv', 'master_shortlist_old.csv', 'master_shortlist_strong.csv')
CLI_FILES = ('football_value_pipeline_v2_standalone.py', 'format_football_output.py',
             'collect_api_football_data.py', 'publish_api_football_data.py',
             'performance_tracking.py', 'performance_excel.py', 'publish_performance.py',
             'collect_bbs_data.py', 'publish_bbs_data.py', 'refresh_training_data.py', 'refresh_ucl_training.py', 'league_registry.py', 'historical_benchmark.py', 'publish_scheduled_forecasts.py', 'closing_odds.py', 'github_closing_odds.py', 'workflow_checks.py', 'clv_report.py', 'market_implied_calibration.py', 'narrow_margin.py', 'cagey_correction_report.py', 'model_activity.py')
COVERAGE_FLOORS = {'asian_handicap.py':85, 'api_football_data.py':85, 'api_football_integration.py':85,
    'win_first_shortlist.py':85, 'per_market_shortlist.py':85, 'corners_cards_shortlist.py':85, 'count_markets.py':85,
    'no_loss_corners_shortlist.py':85,
    'collect_api_football_data.py':75, 'publish_api_football_data.py':75,
    'prediction_runs.py':85, 'github_closing_odds.py':80, 'bbs_statistics_model.py':85, 'bbs_data.py':85, 'bbs_integration.py':85, 'collect_bbs_data.py':75,
    'publish_bbs_data.py':75, 'forecast_integrity.py':100, 'api_key_config.py':90, 'conservative_bet_filter.py':90,
    'shortlist_policy_experiment.py':85, 'shortlist_weight_experiment.py':85, 'quote_freshness.py':95, 'score_probability.py':95,
    'double_chance.py':90, 'goal_market_validation.py':85, 'goal_blend_experiment.py':90,
    'market_led_experiment.py':90, 'match_scores.py':90, 'performance_tracking.py':85, 'turkey_results.py':90,
    'performance_excel.py':85, 'publish_performance.py':75, 'workflow_checks.py':80,
    'dc_decay_validation.py':85, 'market_blend_validation.py':90, 'refresh_training_data.py':70, 'format_football_output.py':60, 'ucl_training.py':90, 'quote_policy.py':95, 'pipeline_health.py':90, 'refresh_ucl_training.py':75, 'league_registry.py':90, 'recency_experiment.py':85, 'filter_sensitivity_experiment.py':85, 'historical_benchmark.py':85, 'benchmark_forward_experiment.py':85, 'publish_scheduled_forecasts.py':80, 'odds_api_usage.py':90, 'totals_anchor_experiment.py':90, 'closing_odds.py':90, 'model_reliability_experiment.py':90, 'model_comparison.py':90,
    'excel_book.py':90, 'predictions_workbook.py':90, 'performance_report_layout.py':90, 'model_activity.py':85, 'odds_provider.py':85,
    'shortlist_replay.py':95, 'market_implied.py':95, 'market_implied_calibration.py':85, 'price_edge_shortlist.py':90, 'price_edge_tracking.py':90, 'narrow_margin.py':90, 'cagey_correction_report.py':90, 'price_edge_cagey_shortlist.py':95, 'staking.py':95, 'elo_ratings.py':95, 'clv_report.py':90}


def require(condition, message):
    if not condition: raise ValueError(message)


def read_json(path):
    # Reject non-standard NaN/Infinity rather than carrying invalid metrics.
    def invalid(value): raise ValueError(f'Nonfinite JSON number in {path.name}')
    with path.open(encoding='utf-8-sig') as handle:
        return json.load(handle, parse_constant=invalid)


def close(actual, expected, label):
    if expected is None:
        require(actual is None or actual == '', f'{label}: expected unavailable')
    else:
        require(actual is not None and actual != '' and math.isfinite(float(actual))
                and abs(float(actual)-expected) <= 1e-6, f'{label}: inconsistent value')


def raw_check(root, *, raw_dir=None):
    from performance_tracking import read_csv, utc, fixture_key, SUPPORTED_MARKETS, number, pick_key
    from prediction_runs import resolve_raw
    raw=Path(raw_dir) if raw_dir is not None else resolve_raw(root/'raw')
    summary=read_json(raw/'conservative_bet_summary.json')
    require(utc(summary.get('generated_at_utc')) is not None, 'Invalid forecast generation timestamp')
    predictions=read_csv(raw/'all_leagues_predictions.csv')
    picks=read_csv(raw/'conservative_bet_shortlist.csv')
    require(bool(predictions), 'No forecast rows to capture')
    keys=set()
    for row in predictions:
        require(all(row.get(k) for k in ('league','home_team','away_team','kickoff_utc')), 'Incomplete forecast identity')
        require(utc(row['kickoff_utc']) is not None, 'Invalid forecast kickoff')
        key=fixture_key(row);require(key not in keys, 'Duplicate forecast fixture');keys.add(key)
        p=[number(row.get('p_'+side),min_value=0,max_value=1) for side in ('home','draw','away')]
        require(all(x is not None for x in p) and abs(sum(p)-1)<=1e-6, 'Invalid 1X2 probability simplex')
        for field,value in row.items():
            if (field.startswith('p_') or field.startswith('raw_p_')) and value not in ('',None):
                require(number(value,min_value=0,max_value=1) is not None, f'Invalid probability column {field}')
    selected=set()
    from conservative_bet_filter import (BALANCED_SELECTION_POLICIES,
        BALANCED_SELECTION_POLICY_VERSION, TWELVE_MATCH_BALANCED_SELECTION_POLICIES, CURRENT_MARKET_SPECS, NO_UNDER35_SELECTION_POLICIES, TARGET_DISTINCT_MATCHES)
    policy_version = summary.get('selection_policy_version')
    from asian_handicap import POLICIES as AH_POLICIES, RISK_BAND_POLICIES, ONE_PERCENT_POLICIES, SAFEST_POLICIES, parse_label as parse_handicap, ordinary_markets
    asian = policy_version in AH_POLICIES
    if asian or policy_version in TWELVE_MATCH_BALANCED_SELECTION_POLICIES:
        # The policy, not the summary alone, decides whether validation evidence is required.
        from asian_handicap import requires_goal_market_validation
        require(bool(summary.get('validation_required')) or not requires_goal_market_validation(policy_version),
                'Policy requires goal-market validation evidence but the run recorded none')
    from asian_handicap import WIN_FIRST_POLICIES
    from asian_handicap import PER_MARKET_POLICIES
    import corners_cards_shortlist, no_loss_corners_shortlist, per_market_shortlist, price_edge_shortlist, price_edge_cagey_shortlist
    from per_market_shortlist import PER_GROUP_CAP
    MAX_SELECTIONS = {per_market_shortlist.POLICY: per_market_shortlist.MAX_SELECTIONS,
                      corners_cards_shortlist.POLICY: corners_cards_shortlist.MAX_SELECTIONS,
                      price_edge_shortlist.POLICY: float('inf'),
                      price_edge_cagey_shortlist.POLICY: float('inf')}.get(policy_version, 12)  # v27/v28: one per fixture, no cap
    count_markets_allowed = {corners_cards_shortlist.POLICY: corners_cards_shortlist.COUNT_MARKETS,
                             no_loss_corners_shortlist.POLICY: no_loss_corners_shortlist.COUNT_MARKETS}.get(policy_version, ())
    win_first = policy_version in WIN_FIRST_POLICIES
    per_market = policy_version in PER_MARKET_POLICIES
    if asian:
        allowed_horizons = (shortlist_window.LEGACY_HOURS,)
        if policy_version == price_edge_cagey_shortlist.POLICY:
            allowed_horizons += (shortlist_window.DEFAULT_HOURS,)
        require(summary.get('shortlist_lookahead_hours') in allowed_horizons and len(picks) <= MAX_SELECTIONS,
                'Invalid Asian handicap horizon or cap')
    if per_market:
        from collections import Counter
        require(max(Counter(r.get('market_group') for r in picks).values(),default=0)<=PER_GROUP_CAP,
                'Per-market shortlist exceeds its group cap')
    balanced = policy_version in BALANCED_SELECTION_POLICIES
    excludes_under = policy_version in NO_UNDER35_SELECTION_POLICIES
    target = TARGET_DISTINCT_MATCHES if policy_version in TWELVE_MATCH_BALANCED_SELECTION_POLICIES else 10
    previous_score = float('inf')
    if balanced:
        require(summary.get('shortlist_lookahead_hours') == 48, 'Balanced shortlist must use 48 hours')
        require(summary.get('target_distinct_matches') == target, 'Balanced shortlist target differs from policy')
        require(len(picks) <= target, f'Balanced shortlist exceeds {target} fixtures')
    value_per_market = (policy_version == price_edge_cagey_shortlist.POLICY
                  and summary.get('value_rule') in (price_edge_cagey_shortlist.VALUE_RULE_PER_MARKET, *price_edge_cagey_shortlist.PROFIT_RULES))
    for row in picks:
        key=fixture_key(row);require(key in keys, 'Selection without matching forecast')
        # A per-market value run picks once per fixture AND market group; every other policy once per fixture.
        identity=pick_key({**row,'fixture_key':key}) if value_per_market else key
        require(identity not in selected, 'Multiple selected markets for one fixture');selected.add(identity)
        require(row.get('market') in summary.get('eligible_markets',SUPPORTED_MARKETS), 'Unsupported selected market')
        require(not excludes_under or row.get('market') != 'Under 3.5', 'Under 3.5 is excluded from this shortlist policy')
        if policy_version == BALANCED_SELECTION_POLICY_VERSION:
            require(row.get('market') in {spec[0] for spec in CURRENT_MARKET_SPECS}, 'Market is excluded from the current shortlist policy')
        if asian:
            counted = row.get('market') in count_markets_allowed
            require(row.get('market') in ordinary_markets(policy_version) or parse_handicap(row.get('market')) is not None
                    or counted or (value_per_market and row.get('market') == price_edge_cagey_shortlist.OVER_1_5)
                    or (summary.get('value_rule') in price_edge_cagey_shortlist.LOCAL_RESEARCH_RULES and row.get('market') == 'Double Chance 12'),
                    'Excluded Asian shortlist market')
            if value_per_market:
                require(row.get('value_market_group') == price_edge_cagey_shortlist.market_group(row, rule=summary.get('value_rule')),
                        'Per-market pick has the wrong market group')
            if counted:
                require('UNPROVEN EDGE' in str(row.get('selection_warnings') or ''),'Count-market pick missing its unproven-edge flag')
            require(row.get('selection_tier')=='STRICT','Asian shortlist must not bypass strict gates')
        require(row.get('selection_tier') in ('STRICT','PROVISIONAL'), 'Invalid selection tier')
        require(number(row.get('offered_decimal_odds'),min_value=1.000001) is not None, 'Missing real selection price')
        require(number(row.get('rank_probability') or row.get('predicted_probability'),min_value=0,max_value=1) is not None,
                'Missing selection probability')
        if summary.get('value_rule') in price_edge_cagey_shortlist.LOCAL_RESEARCH_RULES:
            from profit_shortlist import ODDS_FLOOR
            floor = ODDS_FLOOR[summary['value_rule']]
            require(floor < float(row['offered_decimal_odds']) <= 2.0, f'Researched shortlist price outside ({floor:.2f}, 2.00]')
        if balanced:
            from datetime import timedelta
            generated, kickoff = utc(summary['generated_at_utc']), utc(row['kickoff_utc'])
            require(generated+timedelta(minutes=20) <= kickoff <= generated+timedelta(hours=48),
                    'Balanced selection outside 48-hour window')
            a, b, score = [number(row.get(field),min_value=0,max_value=1)
                           for field in ('probability_percentile','ev_percentile','selection_score')]
            require(None not in (a,b,score) and abs(score-.5*(a+b))<1e-9, 'Invalid combined shortlist score')
            require(score <= previous_score+1e-9, 'Shortlist not ordered by combined score')
            previous_score = score
    for field,count in [('n_fixtures',len(predictions)),('n_shortlisted',len(picks)),
        ('n_strict_qualified',sum(r.get('selection_tier')=='STRICT' for r in picks)),
        ('n_provisional_watchlist',sum(r.get('selection_tier')=='PROVISIONAL' for r in picks))]:
        if field in summary: require(summary[field]==count, f'Forecast summary {field} does not match CSV')
    if policy_version in TWELVE_MATCH_BALANCED_SELECTION_POLICIES or asian:
        # The current production policy must be reproducible even if optional
        # experiment sidecars are absent. Checking score arithmetic alone does
        # not bind the selected market, price, EV or top-twelve membership.
        import pandas as pd
        from conservative_bet_filter import build_conservative_shortlist
        from shortlist_replay import READ_IDS_AS_TEXT, clean as clean_frame, difference, equivalent, monitoring_equivalent
        reliability = None
        if summary.get('validation_required'):
            reliability = {}
            for path in sorted(raw.glob('*_goal_market_validation.json')):
                report = read_json(path)
                require(isinstance(report, dict) and isinstance(report.get('league'), str),
                        'Invalid current shortlist reliability evidence')
                require(report['league'] not in reliability, 'Duplicate shortlist reliability evidence')
                reliability[report['league']] = report
            require(bool(reliability), 'Missing current shortlist reliability evidence')
        if policy_version == price_edge_cagey_shortlist.POLICY:
            # Replay with the switches and model recorded for this run, not today's config.
            import narrow_margin
            monitoring = []
            expected, decisions, replay = price_edge_cagey_shortlist.build_shortlist(
                pd.read_csv(raw/'all_leagues_predictions.csv', low_memory=False), utc(summary['generated_at_utc']),
                reliability, summary.get('quote_execution_policy'),
                # A run that records no tier rule used value-v1 (tier_rule() maps None to it); a run that
                # records no execution version used execution v1.
                settings={**{k: summary.get(k) for k in price_edge_cagey_shortlist.REPLAY_SETTINGS},
                          'price_edge_execution_version': summary.get('price_edge_execution_version', 1),
                          'shortlist_lookahead_hours': summary['shortlist_lookahead_hours']},
                model=narrow_margin.load(summary['cagey_model_version']) if summary.get('cagey_model_version') else None,
                monitor=monitoring)
        else:
            expected, _, replay = build_conservative_shortlist(
                pd.read_csv(raw/'all_leagues_predictions.csv', low_memory=False),
                as_of=utc(summary['generated_at_utc']), market_reliability=reliability,
                execution_policy=summary.get('quote_execution_policy'),
                selection_policy_version=policy_version)
        actual = pd.read_csv(raw/'conservative_bet_shortlist.csv', low_memory=False, dtype=READ_IDS_AS_TEXT)
        require(set(expected.columns).issubset(actual.columns), 'Missing current shortlist replay columns')
        # CSV blank strings deserialize as null, including empty strict-rule
        # warnings. Normalize only that representation difference for replay.
        written, replayed = clean_frame(actual[list(expected.columns)]), clean_frame(expected.replace('', None))
        if not equivalent(written, replayed):
            # Name the differing cells, so a failed run says why (the comparison itself is unchanged).
            require(False, 'Current shortlist differs from deterministic ranking replay: '
                    + difference(written, replayed))
        if policy_version == price_edge_cagey_shortlist.POLICY:
            # The cagey tier is a separate list: bind its rows to the same replay.
            # Labelled as the run recorded (runs before cagey-own-probabilities-v1 record nothing).
            tier_labels = summary.get('cagey_tier_labels_version')
            require(tier_labels in price_edge_cagey_shortlist.TIER_LABELS_VERSIONS, 'Unknown cagey-tier labels version')
            tier_expected = price_edge_cagey_shortlist.cagey_tier_list(decisions, tier_labels)
            tier_path = raw/price_edge_cagey_shortlist.TIER_FILE
            if replay['cagey_tier']['enabled']:
                require(tier_path.exists(), 'Missing current cagey-tier shortlist')
            if tier_path.exists():
                try:
                    tier_actual = pd.read_csv(tier_path, low_memory=False, dtype=READ_IDS_AS_TEXT)
                except pd.errors.EmptyDataError:
                    tier_actual = pd.DataFrame()
                if len(tier_expected) or len(tier_actual):
                    require(set(tier_expected.columns).issubset(tier_actual.columns),
                            'Missing current cagey-tier replay columns')
                    actual_rows = clean_frame(tier_actual[list(tier_expected.columns)])
                    replay_rows = clean_frame(tier_expected.replace('', None))
                    if not equivalent(actual_rows, replay_rows):
                        detail = f'row count {len(actual_rows)} saved, {len(replay_rows)} replayed'
                        if len(actual_rows) == len(replay_rows):
                            detail = next(
                                f'row {i}, {field}: saved={actual[field]!r}, replay={value!r}'
                                for i, (actual, expected) in enumerate(zip(actual_rows, replay_rows), 1)
                                for field, value in expected.items() if not equivalent(actual[field], value)
                            )
                        raise ValueError(f'Current cagey-tier shortlist differs from deterministic replay ({detail})')
            # Master shortlist: recorded runs must carry exactly the list the replayed decisions give.
            # Since the release (14 Nov 2026) master_shortlist.csv is the new master (VERSION_NEW_LIVE) and the old
            # master is checked the same way in its shadow files (master_shortlist_old.csv and its audit).
            import master_shortlist
            master_path = raw/master_shortlist.FILE

            def check_old_master(info, list_path, audit_name, label, audit_label):
                require(list_path.exists(), f'Missing current {label}')
                master_version = info.get('version')
                require(master_version in master_shortlist.VERSIONS, 'Unknown master shortlist version')
                if master_version in master_shortlist.MARKET_VERSIONS:
                    from master_selection import require_generation_clock
                    require_generation_clock(decisions, summary.get('generated_at_utc'))
                with shortlist_window.scope(summary['shortlist_lookahead_hours']):
                    master_expected = master_shortlist.build(
                        decisions, pd.read_csv(raw/'all_leagues_predictions.csv', low_memory=False), master_version,
                        execution_policy=summary.get('quote_execution_policy', {}))
                    master_summary_expected = master_shortlist.summary(master_expected, master_version)
                try:
                    master_actual = pd.read_csv(list_path, low_memory=False)
                except pd.errors.EmptyDataError:
                    master_actual = pd.DataFrame(columns=master_shortlist.columns(master_version))
                require(master_shortlist.matches(master_actual, master_expected, master_version),
                        f'Current {label} differs from deterministic replay')
                require(equivalent(info, master_summary_expected),
                        f'Current {label} summary differs from replay')
                if master_version in master_shortlist.MARKET_VERSIONS:
                    module = master_shortlist.selection_module(master_version)
                    audit_path = raw/(audit_name or module.AUDIT_FILE)
                    require(audit_path.exists(), f'Missing current {audit_label} selection audit')
                    from quote_policy import policy_scope
                    with shortlist_window.scope(summary['shortlist_lookahead_hours']), policy_scope(summary.get('quote_execution_policy')):
                        audit_expected = module.evaluate(decisions, pd.read_csv(raw/'all_leagues_predictions.csv', low_memory=False))
                    audit_actual = pd.read_csv(audit_path, low_memory=False)
                    require(master_shortlist.matches(audit_actual, audit_expected, master_version),
                            f'Current {audit_label} selection audit differs from deterministic replay')
                return master_expected

            live_info = summary.get('master_shortlist')
            # A release incident (master_shortlist.RELEASE_STATUS_KEY) must replay too: a run that says a master
            # failed is accepted only if that master fails again on the frozen inputs.
            release = summary.get(master_shortlist.RELEASE_STATUS_KEY)
            incident = (release or {}).get('status')
            require(release is None or incident in (master_shortlist.NEW_MASTER_FAILED,
                                                    master_shortlist.BASELINE_MISSING,
                                                    master_shortlist.STRONG_FAILED),
                    'Unknown master release status')

            def replays(build):
                try:
                    build()
                except Exception:
                    return False
                return True

            def replay_old(version):
                return master_shortlist._old_master(decisions, summary, pd.read_csv(
                    raw/'all_leagues_predictions.csv', low_memory=False), version)

            def replay_new(old_frame):
                return master_shortlist.new_live(decisions, old_frame, summary.get('generated_at_utc'), pd.read_csv(
                    raw/'all_leagues_predictions.csv', low_memory=False), summary.get('cagey_model_version'),
                    master_shortlist.cagey_settings(summary))

            def replay_baseline():
                import master_reconciliation as mr
                return mr.reconcile(decisions, None, mr.load_config(), pd.read_csv(
                    raw/'all_leagues_predictions.csv', low_memory=False), summary.get('generated_at_utc'))

            def replay_strong(baseline, rule=None):
                return master_shortlist.strong_live(decisions, baseline, summary.get('generated_at_utc'), pd.read_csv(
                    raw/'all_leagues_predictions.csv', low_memory=False), summary.get('cagey_model_version'),
                    master_shortlist.cagey_settings(summary), rule=rule)

            strong_rule = master_shortlist.strong_rule((live_info or {}).get('version'))
            if strong_rule is not None:
                # Live "strong" (23 Nov 2026): the strong-team master is master_shortlist.csv and today's master its
                # shadow baseline (master_shortlist_new.csv); no old master shadow.
                import master_reconciliation as mr
                require(release is None or incident == master_shortlist.BASELINE_MISSING,
                        'Unexpected release incident beside the live strong master')
                require(master_path.exists(), 'Missing current master shortlist')
                require(master_shortlist.OLD_SUMMARY_KEY not in summary and not (raw/master_shortlist.OLD_FILE).exists(),
                        'Unexpected old master shadow under the strong release')
                baseline_path = raw/mr.load_config()['file']
                baseline_expected = None
                if incident == master_shortlist.BASELINE_MISSING:
                    require(not baseline_path.exists(), "Today's master (shadow) file without its run")
                    require(not replays(replay_baseline),
                            "The run summary says today's master (shadow) failed, but it replays without error")
                else:
                    require(baseline_path.exists(), "Missing today's master (shadow), the strong master's baseline")
                    baseline_expected = replay_baseline()
                    try:
                        baseline_actual = pd.read_csv(baseline_path, low_memory=False)
                    except pd.errors.EmptyDataError:
                        baseline_actual = pd.DataFrame(columns=list(mr.COLUMNS))
                    require(len(baseline_actual) == len(baseline_expected) and list(baseline_actual.columns)
                            == list(mr.COLUMNS) and all(
                                master_shortlist._same(got, want)
                                for column in ('new_master_rank', 'new_master_decision', 'market', 'offered_decimal_odds')
                                for got, want in zip(master_shortlist._as_csv(baseline_actual)[column].astype(object),
                                                     master_shortlist._as_csv(baseline_expected)[column].astype(object))),
                            "Today's master (shadow) differs from deterministic replay")
                require((live_info or {}).get('rule') == strong_rule, 'Strong master live version and rule disagree')
                strong_expected, strong_summary_expected = replay_strong(baseline_expected, strong_rule)
                try:
                    strong_actual = pd.read_csv(master_path, low_memory=False)
                except pd.errors.EmptyDataError:
                    strong_actual = pd.DataFrame(columns=list(strong_expected.columns))
                require(master_shortlist.matches_strong(strong_actual, strong_expected, strong_rule),
                        'Current master shortlist (strong) differs from deterministic replay')
                require(equivalent(live_info, strong_summary_expected),
                        'Current master shortlist (strong) summary differs from replay')
            elif incident == master_shortlist.STRONG_FAILED:
                # The strong master failed: today's master was published as the live list for this run.
                require(live_info is not None and live_info.get('version') == master_shortlist.VERSION_NEW_LIVE,
                        "A run whose strong master failed must publish today's master")
                require(not replays(lambda: replay_strong(replay_baseline())),
                        'The run summary says the strong master failed, but it replays without error')
                new_expected, new_summary_expected = replay_new(None)
                new_actual = pd.read_csv(master_path, low_memory=False)
                require(master_shortlist.matches_new(new_actual, new_expected),
                        'Current master shortlist differs from deterministic replay')
                require(equivalent(live_info, new_summary_expected),
                        'Current master shortlist summary differs from replay')
            elif incident == master_shortlist.NEW_MASTER_FAILED:
                # The old master was published as the live list for this run, exactly as live "old" writes it.
                require(live_info is not None and live_info.get('version') in master_shortlist.VERSIONS,
                        'A run whose new master failed must publish the old master')
                require(master_shortlist.OLD_SUMMARY_KEY not in summary
                        and not any((raw/name).exists() for name in master_shortlist.RELEASE_FILES),
                        'Unexpected release files in a run whose new master failed')
                old_expected = check_old_master(live_info, master_path, None, 'master shortlist', 'master')
                require(not replays(lambda: replay_new(old_expected)),
                        'The run summary says the new master failed, but it replays without error')
            elif live_info is not None and live_info.get('version') == master_shortlist.VERSION_NEW_LIVE:
                require(master_path.exists(), 'Missing current master shortlist')
                old_info = summary.get(master_shortlist.OLD_SUMMARY_KEY)
                old_expected = None
                if old_info is not None:
                    require(release is None, 'A release incident is recorded beside a complete old master shadow')
                    old_expected = check_old_master(old_info, raw/master_shortlist.OLD_FILE,
                                                    master_shortlist.OLD_AUDIT_FILE, 'old master shortlist (shadow)',
                                                    'old master (shadow)')
                else:
                    # No old master (shadow): only when it failed in this run and fails again on replay.
                    require(incident == master_shortlist.BASELINE_MISSING,
                            'Missing current old master shortlist (shadow) summary')
                    require(not (raw/master_shortlist.OLD_FILE).exists()
                            and not (raw/master_shortlist.OLD_AUDIT_FILE).exists(),
                            'Old master (shadow) files without its summary')
                    version = release.get('old_master_version') or master_shortlist.configured_version()
                    require(not replays(lambda: replay_old(version)),
                            'The run summary says the old master (shadow) failed, but it replays without error')
                new_expected, new_summary_expected = replay_new(old_expected)
                try:
                    new_actual = pd.read_csv(master_path, low_memory=False)
                except pd.errors.EmptyDataError:
                    new_actual = pd.DataFrame(columns=list(new_expected.columns))
                require(master_shortlist.matches_new(new_actual, new_expected),
                        'Current master shortlist differs from deterministic replay')
                require(equivalent(live_info, new_summary_expected),
                        'Current master shortlist summary differs from replay')
            elif live_info is not None:
                require(release is None, 'A release incident is recorded for a run without the released master')
                check_old_master(live_info, master_path, None, 'master shortlist', 'master')
            # Correction monitoring is evidence only, but its rows must be this run's own. The run's
            # immutable summary says whether it was generated with monitoring; earlier v28 runs were not.
            monitor_path = raw/price_edge_cagey_shortlist.MONITOR_FILE
            monitored = summary.get('correction_monitoring_version')
            require(monitored in (None, price_edge_cagey_shortlist.MONITOR_VERSION),
                    'Unknown correction-monitoring version')
            if monitored:
                require(monitor_path.exists(), 'Missing current correction-monitoring records')
            if monitor_path.exists():
                monitor_expected = pd.DataFrame(monitoring, columns=price_edge_cagey_shortlist.MONITOR_COLUMNS)
                try:
                    monitor_actual = pd.read_csv(monitor_path, low_memory=False, dtype=READ_IDS_AS_TEXT)
                except pd.errors.EmptyDataError:
                    monitor_actual = pd.DataFrame(columns=price_edge_cagey_shortlist.MONITOR_COLUMNS)
                require(list(monitor_actual.columns) == price_edge_cagey_shortlist.MONITOR_COLUMNS,
                        'Correction-monitoring columns differ')
                require(monitoring_equivalent(clean_frame(monitor_actual.astype(object).replace('', None)),
                                   clean_frame(monitor_expected.astype(object).replace('', None))),
                        'Current correction-monitoring records differ from deterministic replay')
        for field in ('target_distinct_matches', 'shortfall', 'usable_distinct_fixtures',
                      *(['loss_risk_tolerance'] if policy_version in RISK_BAND_POLICIES else [] if asian else ['ranking_weights']),
                      *(['min_estimated_ev','min_raw_dc_ev','ev_required_for_selection'] if policy_version in ONE_PERCENT_POLICIES else []),
                      *(['min_adjusted_no_loss_probability','max_estimated_loss_probability'] if policy_version in SAFEST_POLICIES else []),
                      *(['selection_objective','ranking_metric','probability_basis','ev_required_for_selection',
                         'negative_adjusted_ev_selections'] if win_first else []),
                      *(['ranking_weights','market_groups','max_per_market_group','group_shortfall',
                         'negative_adjusted_ev_markets'] if per_market else []),
                      *(['unproven_edge_markets','negative_adjusted_ev_selections']
                        if policy_version == no_loss_corners_shortlist.POLICY else []),
                      *(['min_edge','min_edge_derived','rejection_counts','tagged_candidates','reference_type_counts']
                        if policy_version in (price_edge_shortlist.POLICY, price_edge_cagey_shortlist.POLICY) else []),
                      *(['cagey_correction_enabled','cagey_tier_enabled','cagey_model_version','correction_only_value_picks',
                         'cagey_tier','shortlist_lookahead_hours','shortlist_window_end_utc']
                        if policy_version == price_edge_cagey_shortlist.POLICY else []),
                      *(['price_edge_execution_version'] if 'price_edge_execution_version' in summary else []),
                      *(['cagey_tier_labels_version'] if 'cagey_tier_labels_version' in summary else []),
                      'eligible_markets', 'quote_execution_policy'):
            require(equivalent(summary.get(field), replay[field]),
                    f'Current shortlist summary {field} differs from ranking replay')
    return {'forecasts':len(predictions),'selections':len(picks),'warnings':[]}


def changed_forecasts(repo, before, sha):
    require(re.fullmatch(r'[0-9a-fA-F]{40}',sha or '') is not None, 'Capture requires a full source SHA')
    def git(*args):
        return subprocess.run(['git','-C',str(repo),*args],check=True,text=True,capture_output=True,
                              stdin=subprocess.DEVNULL).stdout
    require(git('rev-parse','HEAD').strip()==sha, 'Capture checkout differs from event SHA')
    if before == '0'*40:
        names=git('ls-tree','-r','--name-only',sha,'--',*FORECAST_PATHS)
    else:
        require(re.fullmatch(r'[0-9a-fA-F]{40}',before or '') is not None, 'Missing previous push SHA')
        names=git('diff','--name-only',before,sha,'--',*FORECAST_PATHS)
    return bool(names.strip())


def capture_event(repo,root,event,sha,before=''):
    from performance_tracking import capture
    if event=='push' and not changed_forecasts(repo,before,sha):
        print('No forecast inputs changed; capture skipped.')
        return False
    require(event in ('push','workflow_dispatch'), 'Capture is only permitted for data pushes or explicit manual requests')
    if event=='workflow_dispatch':
        require(re.fullmatch(r'[0-9a-fA-F]{40}',sha or '') is not None,'Capture requires a full source SHA')
        current=subprocess.run(['git','-C',str(repo),'rev-parse','HEAD'],check=True,text=True,capture_output=True,
                               stdin=subprocess.DEVNULL).stdout.strip()
        require(current==sha,'Capture checkout differs from event SHA')
    raw_check(root)
    from prediction_runs import capture_runs
    if (root/'raw/prediction_runs').exists():
        return bool(capture_runs(root,sha))
    return capture(sha,root=root)


def archive_check(root):
    from performance_tracking import utc,read_csv
    from datetime import timedelta
    manifests=[];warnings=[]
    base=root/'performance'/'snapshots'
    for directory in sorted(base.iterdir()) if base.exists() else []:
        if not directory.is_dir(): continue
        if directory.name.startswith('.capture-'): continue
        meta=read_json(directory/'metadata.json')
        sha=meta.get('git_commit_sha','')
        if 'archive_id' in meta:
            from prediction_runs import archive_identity
            sha=archive_identity(meta,directory.name)
        require(re.fullmatch(r'[0-9a-fA-F]{40}',sha) is not None and directory.name==sha[:16], 'Invalid snapshot SHA/directory')
        created,generated=utc(meta.get('captured_at_utc')),utc(meta.get('generated_at_utc'))
        require(created and generated and generated<=created+timedelta(minutes=5), 'Invalid snapshot timestamps')
        digests=meta.get('sha256',{})
        if 'archive_id' in meta:
            require('run_manifest.json' in digests, 'Missing prediction-run manifest binding')
        require(isinstance(digests,dict) and all(k in digests for k in ('predictions.csv','shortlist.csv','selection_summary.json')),
                'Snapshot missing required integrity manifest')
        for name,digest in digests.items():
            require(name in ('predictions.csv','shortlist.csv','selection_summary.json','pipeline_health.json','run_manifest.json','bet365_vs_pinnacle.csv',*SIDECARS), 'Unexpected snapshot path')
            path=directory/name
            if name in RETIRED_SIDECARS and not path.exists():
                continue
            valid=path.is_file() and hashlib.sha256(path.read_bytes()).hexdigest()==digest
            if name in (*SIDECARS, 'pipeline_health.json'):
                if not valid: warnings.append(f'{directory.name}/{name}: optional artifact missing/tampered; excluded from grading')
            else: require(valid, f'Snapshot integrity failure: {directory.name}/{name}')
        if 'archive_id' in meta:
            from prediction_runs import validate_archive_binding
            validate_archive_binding(directory,meta)
        summary=read_json(directory/'selection_summary.json')
        source_generated=utc(summary.get('generated_at_utc'))
        require(source_generated is not None and abs((source_generated-generated).total_seconds())<1,'Snapshot generation time differs from source summary')
        rows=read_csv(directory/'predictions.csv');picks=read_csv(directory/'shortlist.csv')
        eligible=sum(1 for r in rows if (kick:=utc(r.get('kickoff_utc'))) and
            max(created,generated)<=kick-timedelta(minutes=20))
        for key,count in [('n_all_forecasts',len(rows)),('n_shortlist',len(picks)),('n_pre_kickoff_forecasts',eligible)]:
            require(meta.get(key)==count, f'Snapshot {directory.name}: {key} mismatch')
        manifests.append({'sha':sha,'forecasts':len(rows),'selections':len(picks),'eligible':eligible,
                          'policy':meta.get('selection_policy_version','legacy/unspecified')})
    return {'snapshots':manifests,'warnings':warnings}


def expected_stats(rows):
    from asian_handicap import SETTLED
    rated=[r for r in rows if r['status'] in SETTLED]
    wins=sum(r['status'] in ('WON','HALF_WON') for r in rated)
    profit=[float(r['unit_profit']) for r in rated if r.get('unit_profit') not in ('',None)]
    brier=[float(r['brier']) for r in rated if r.get('brier') not in ('',None)]
    from asian_handicap import parse_label
    extras = dict(refunds=sum(r['status']=='REFUNDED' for r in rated),
        half_wins=sum(r['status']=='HALF_WON' for r in rated),
        half_losses=sum(r['status']=='HALF_LOST' for r in rated),
        no_loss_rate=sum(v >= -1e-12 for v in profit)/len(profit) if profit else None) if any(parse_label(r.get('market')) for r in rows) else {}
    return dict(**extras,total=len(rows),graded=len(rated),wins=wins,losses=sum(r['status'] in ('LOST','HALF_LOST') for r in rated),pending=len(rows)-len(rated),
        win_rate=wins/len(rated) if rated else None,brier=sum(brier)/len(brier) if brier else None,
        settled_with_odds=len(profit),profit_per_unit_staked=sum(profit) if profit else None,
        flat_stake_roi=sum(profit)/len(profit) if profit else None)


REPORT_SHEETS = ('Dashboard', 'Picks & Results', 'Weekly Trends', 'Breakdowns', 'Calibration', 'CLV',
                 'Model Monitoring', 'Model Activity', 'Guide')
GRADED_MASTER_FILES = (('new', 'master_shortlist_picks.csv'), ('old', 'master_shortlist_old_picks.csv'))


def report_workbook_check(root, workbook):
    """The performance workbook's sheets and its Dashboard headline, recounted here from the graded master files
    since the master tracking start: the first archived run whose summary records the released new master."""
    from excel_book import named_value, parse_utc, read_workbook
    from master_shortlist import VERSION_NEW_LIVE
    from performance_tracking import number, read_csv
    book = read_workbook(workbook)
    require(tuple(book['sheets']) == REPORT_SHEETS, 'Workbook sheets differ from the report layout')
    starts = [parse_utc(read_json(path).get('generated_at_utc'))
              for path in sorted((root/'performance'/'snapshots').glob('*/selection_summary.json'))
              if not path.parent.name.startswith('.capture-')
              and (read_json(path).get('master_shortlist') or {}).get('version') == VERSION_NEW_LIVE]
    start = min([s for s in starts if s is not None], default=None)
    shown = str(named_value(book, 'master_tracking_start') or '')
    require(('not started' in shown) if start is None else ('started afresh' in shown), 'Workbook tracking start differs')
    settled = ('WON', 'HALF_WON', 'REFUNDED', 'HALF_LOST', 'LOST')
    for which, name in GRADED_MASTER_FILES:
        path = root/'performance'/'price_edge_v27'/name
        rows = read_csv(path) if path.exists() and path.stat().st_size else []
        rows = [r for r in rows if start is not None and parse_utc(r.get('snapshot_generated_utc')) is not None
                and parse_utc(r.get('snapshot_generated_utc')) >= start]
        graded = [number(r.get('unit_profit')) for r in rows
                  if r.get('result_status') in settled and number(r.get('unit_profit')) is not None]
        close(named_value(book, f'{which}_master_picks'), len(rows), f'Workbook {which} master picks')
        close(named_value(book, f'{which}_master_graded'), len(graded), f'Workbook {which} master graded')
        shown_return = named_value(book, f'{which}_master_return')
        if graded:
            close(shown_return, sum(graded), f'Workbook {which} master return')
        else:
            require(isinstance(shown_return, str), f'Workbook {which} master return must be unavailable')


def headline_check(root, metrics, selections):
    """The report's headline (closing-line value first, returns second; per pick and one row per fixture),
    recomputed from the graded selections and the closing observations as of the review. Reports written
    before the headline existed carry none and are not checked."""
    headline = metrics.get('headline')
    if headline is None:
        return
    from clv_report import fixture_view, load_closes, pick_clv
    from performance_tracking import read_csv, utc
    clv = (pick_clv(selections, load_closes(root, utc(metrics['reviewed_at_utc'])))
           if headline.get('clv_available') else [None] * len(selections))
    view = fixture_view(selections, clv)
    require(headline.get('picks') == view['picks'] and headline.get('fixtures_with_picks') == view['fixtures_with_picks'],
            'Headline pick or fixture count mismatch')
    for scope in ('per_pick', 'per_fixture'):
        for measure in ('clv', 'return'):
            shown, want = headline.get(scope, {}).get(measure, {}), view[scope][measure]
            require(shown.get('n') == want['n'], f'Headline {scope} {measure} count mismatch')
            close(shown.get('mean'), want['mean'], f'Headline {scope} {measure}')
    rows = read_csv(root/'performance'/'fixture_grades.csv')
    require([r['fixture_key'] for r in rows] == [f['fixture_key'] for f in view['fixtures']],
            'Fixture view differs from the graded selections')
    for row, want in zip(rows, view['fixtures']):
        require(all(int(row[k]) == want[k] for k in ('picks', 'picks_with_close', 'settled_picks')),
                'Fixture view pick counts differ')
        close(row.get('mean_clv'), want['mean_clv'], 'Fixture view CLV')
        close(row.get('mean_unit_profit'), want['mean_unit_profit'], 'Fixture view return')


def report_check(root):
    from performance_tracking import read_csv,utc,frozen_rows,snapshots,result_for_market,number,graded_match,tracking_key,pick_key
    from performance_tracking import verified_result_source
    from asian_handicap import SETTLED, parse_label as parse_handicap
    from performance_excel import REPORT_NAME
    from datetime import timedelta
    audit=archive_check(root)
    archived=snapshots(root)
    performance=root/'performance'
    metrics=read_json(performance/'metrics.json')
    require(utc(metrics.get('reviewed_at_utc')) is not None, 'Missing report review timestamp')
    evidence_cache = {}
    def result_source_verified(record):
        if not verified_result_source(record):
            return False
        if record.get('league_code') == 'T1':
            from turkey_results import validate_evidence
            validate_evidence(root, record, utc(metrics['reviewed_at_utc']), evidence_cache=evidence_cache)
        return True
    selections=read_csv(performance/'shortlist_grades.csv');predictions=read_csv(performance/'prediction_grades.csv')
    latest = metrics.get('tracking_basis') == 'LATEST_PREMATCH_PER_FIXTURE'
    history = read_csv(performance/'shortlist_run_history.csv') if latest else []
    history_by_key = {tracking_key(r): r for r in history}
    frozen={tracking_key(r) if latest else pick_key(r):r for r in frozen_rows(archived,'shortlist',latest=latest)}
    require(len(selections)==len(frozen), 'Report omitted or added frozen selections')
    cache_path=performance/'verified_results.json'
    records=list(read_json(cache_path).values()) if cache_path.exists() else []
    seen=set()
    for row in selections:
        key=tracking_key(row) if latest else pick_key(row);require(key not in seen,'Duplicate graded fixture/run');seen.add(key)
        original=frozen.get(key);require(original is not None,'Graded selection without immutable snapshot')
        if latest:
            history_row=history_by_key.get(key)
            label='Latest grade differs from immutable run history'
            require(history_row is not None and row.keys()==history_row.keys(),label)
            # Result IDs are opaque: Europa uses a hash, and numeric provider
            # IDs must also retain exact identity rather than float tolerance.
            numeric={'predicted_probability','offered_decimal_odds','per_stake_cost','unit_profit','brier'}
            timestamps={'kickoff_utc','snapshot_generated_utc','snapshot_captured_utc'}
            for field,value in history_row.items():
                if field in numeric: close(row.get(field),number(value),label+' '+field)
                elif field in timestamps: require(utc(row.get(field))==utc(value),label+' '+field)
                else: require(row.get(field)==value,label+' '+field)
        require(row['snapshot_commit']==original['snapshot_commit'] and row['market']==original['market'], 'Report selection provenance changed')
        require(row['selection_policy_version']==original['selection_policy_version'], 'Report policy provenance changed')
        if latest:
            require(utc(row.get('snapshot_generated_utc'))==utc(original['snapshot_generated_utc']), 'Report generation provenance changed')
            require(utc(row.get('snapshot_captured_utc'))==utc(original['snapshot_captured_utc']), 'Report capture provenance changed')
        close(row.get('offered_decimal_odds'),number(original.get('offered_decimal_odds')),'Frozen selection price')
        # Win-first snapshots freeze the calibrated profitable-win ranking,
        # not the raw p_profit or the legacy refund-inclusive p_no_loss.
        probability_basis = original.get('probability_basis') or None
        require((row.get('probability_basis') or None) == probability_basis,
                'Report probability basis changed')
        expected_probability = (original.get('rank_probability') if probability_basis == 'net_profit'
            else original.get('p_no_loss') if parse_handicap(row.get('market'))
            else original.get('rank_probability') or original.get('predicted_probability'))
        close(row.get('predicted_probability'),number(expected_probability),'Frozen selection probability')
        from quote_policy import stake_cost
        close(row.get('per_stake_cost') or 0,stake_cost(original.get('per_stake_cost') or 0),'Frozen selection cost')
        require(row['selection_tier']==(original.get('selection_tier') or ('STRICT' if original.get('decision')=='SHORTLISTED' else 'PROVISIONAL')), 'Report selection tier changed')
        if row['status'] in SETTLED:
            verified,state=graded_match(original,records)
            require(verified is not None and str(verified['match_id'])==row.get('source_match_id'), 'Selection result absent from verified cache')
            require(result_source_verified(verified),'Selection cache source is not verified finished')
            require(row.get('final_score')==f"{verified['home_goals']}-{verified['away_goals']}", 'Selection score differs from verified cache')
            require(row.get('match_source')==verified['source'] and row.get('source_match_id'), 'Graded result lacks verified source')
            match=re.fullmatch(r'(\d+)-(\d+)',row.get('final_score',''));require(match is not None,'Invalid graded score')
            if parse_handicap(row['market']):
                from asian_handicap import profit
                status, gain = profit(int(match[1]),int(match[2]),*parse_handicap(row['market']),float(row['offered_decimal_odds']),stake_cost(original.get('per_stake_cost') or 0))
                require(row['status']==status,'Asian handicap settlement differs from regulation-time score')
                close(row.get('unit_profit'),gain,'Asian handicap P&L')
                p=number(row.get('predicted_probability'),min_value=0,max_value=1)
                if p is not None:
                    outcome = gain > 1e-12 if probability_basis == 'net_profit' else gain >= -1e-12
                    close(row.get('brier'),(p-int(outcome))**2,'Asian handicap Brier')
                continue
            import count_markets
            counted=count_markets.parse_label(row['market'])
            if counted:
                total=count_markets.verified_total(original,verified)
                require(total is not None,'Count result absent from committed match statistics')
                won=count_markets.outcome(*counted,total)
            else:
                won=result_for_market(row['market'],int(match[1]),int(match[2]))
            require(won is not None and won==(row['status']=='WON'), 'Outcome differs from regulation-time score')
            p=number(row.get('predicted_probability'),min_value=0,max_value=1)
            if p is not None: close(row.get('brier'),(p-int(won))**2,'Selection Brier')
            price=number(row.get('offered_decimal_odds'),min_value=1.000001)
            from quote_policy import stake_cost
            cost=stake_cost(original.get('per_stake_cost') or 0)
            close(row.get('per_stake_cost') or 0,cost,'Frozen selection cost')
            close(row.get('unit_profit'),((price-1 if won else -1)-cost) if price is not None else None,'Selection P&L')
        else:
            require(row.get('unit_profit') in ('',None) and row.get('brier') in ('',None),'Pending result included in scored metrics')
    for field,value in expected_stats(selections).items():close(metrics['shortlist'].get(field),value,'Shortlist '+field)
    headline_check(root, metrics, selections)
    if latest:
        from performance_tracking import score_shortlist
        originals = {tracking_key(r):r for r in frozen_rows(archived,'shortlist',all_runs=True)}
        require(len(history)==len(originals) and len({tracking_key(r) for r in history})==len(history),
                'Prediction history coverage mismatch')
        require(len({pick_key(r) for r in selections})==len(selections), 'Duplicate latest fixture')
        for row in history:
            original=originals.get(tracking_key(row))
            require(original is not None,'History without frozen prediction')
            match,state=graded_match(original,records)
            if utc(original['kickoff_utc']) > utc(metrics['reviewed_at_utc'])-timedelta(hours=2):
                match,state=None,'PENDING_KICKOFF_OR_FINAL_SCORE'
            if match is not None:
                require(result_source_verified(match),
                        'History cache source is not verified finished')
            expected=score_shortlist(original,match,state)
            for field,value in expected.items():
                if value is None:
                    require(row.get(field) in ('',None), 'History '+field+' differs from frozen replay')
                elif isinstance(value,(int,float)):
                    close(row.get(field),value,'History '+field)
                else:
                    require(row.get(field) == str(value), 'History '+field+' differs from frozen replay')
        # History and the latest ledger keep each market-group pick. The
        # first-prediction reference counts each fixture once, in archive order.
        first = {}
        for key, original in originals.items():
            first.setdefault(original['fixture_key'], key)
        first_rows = [history_by_key[key] for key in first.values()]
        require(metrics.get('unique_shortlisted_fixtures')==len(first), 'Unique fixture count mismatch')
        history_groups=metrics.get('run_history_groups',{})
        history_runs={tracking_key(r)[0] for r in history}
        require(metrics.get('tracked_prediction_runs')==len(history_runs), 'Prediction run count mismatch')
        for key,rows in [('first_prediction_reference',first_rows),('shortlist_run_history',history)]:
            for field,value in expected_stats(rows).items(): close(metrics.get(key,{}).get(field),value,key+' '+field)
        for groups,rows in [(metrics.get('groups',{}).get('run',{}),selections),(history_groups,history)]:
            require(set(groups)=={tracking_key(r)[0] for r in rows}, 'Prediction run groups mismatch')
            for run,values in groups.items():
                cohort=[r for r in rows if tracking_key(r)[0]==run]
                for field,value in expected_stats(cohort).items(): close(values.get(field),value,'Prediction run '+field)
        for run in history_runs:
            cohort=[r for r in history if tracking_key(r)[0]==run]
            provenance=metrics.get('run_provenance',{}).get(run,{})
            require(provenance.get('first_snapshot_commit')==cohort[0]['snapshot_commit'] and
                    utc(provenance.get('generated_at_utc'))==utc(cohort[0].get('snapshot_generated_utc')),
                    'Prediction run provenance mismatch')
    for dimension,column in [('tier','selection_tier'),('market','market'),('league','league'),('week','week'),('policy','selection_policy_version')]:
        groups=metrics.get('groups',{}).get(dimension,{})
        require(all(r.get(column) in groups for r in selections),f'Missing {dimension} group')
        for label,values in groups.items():
            for field,value in expected_stats([r for r in selections if r.get(column)==label]).items():
                close(values.get(field),value,f'{dimension} {label}: {field}')
    frozen_predictions={r['fixture_key']:r for r in frozen_rows(archived,'predictions')}
    require(len(predictions)==len(frozen_predictions) and len({r['fixture_key'] for r in predictions})==len(predictions), 'Prediction report coverage mismatch')
    require(all(r['fixture_key'] in frozen_predictions and r['snapshot_commit']==frozen_predictions[r['fixture_key']]['snapshot_commit'] for r in predictions), 'Prediction provenance changed')
    require(metrics['prediction_fixtures_graded']==sum(r['status']=='GRADED' for r in predictions), 'Prediction graded count mismatch')
    # Replay every forecast grade from the frozen rows and the verified cache:
    # status, bound result, duplicate groups and their keeper must all agree.
    from performance_tracking import (PREDICTION_SCORE_FIELDS, mark_duplicate_results,
                                      result_identity, score_prediction)
    reviewed=utc(metrics['reviewed_at_utc'])
    def usable_record(record):
        # The review drops Turkish records whose retained CSV evidence fails.
        if record.get('league_code')!='T1': return True
        from turkey_results import validate_evidence
        try: validate_evidence(root, record, reviewed, evidence_cache=evidence_cache)
        except (OSError, ValueError): return False
        return True
    replay_records=[r for r in records if usable_record(r)]
    originals=list(frozen_predictions.values())
    expected=[]
    for original in originals:
        match,state=graded_match(original,replay_records)
        if utc(original['kickoff_utc']) > reviewed-timedelta(hours=2):
            match,state=None,'PENDING_KICKOFF_OR_FINAL_SCORE'
        expected.append(score_prediction(original,match,state))
    mark_duplicate_results(originals,expected,replay_records)
    reported={r['fixture_key']:r for r in predictions}
    for want in expected:
        row=reported[want['fixture_key']]
        require(row['status']==want['status'], 'Prediction grade status differs from frozen replay')
        require(str(row.get('source_match_id') or '')==str(want['source_match_id'] or ''), 'Prediction result differs from frozen replay')
        for field in PREDICTION_SCORE_FIELDS:
            if want[field] in ('',None): require(row.get(field) in ('',None), 'Prediction '+field+' differs from frozen replay')
            else: close(row.get(field),want[field],'Prediction '+field)
    graded_ids=[result_identity(r) for r in predictions if r['status']=='GRADED']
    require(None not in graded_ids and len(set(graded_ids))==len(graded_ids), 'Verified result graded more than once')
    prediction_brier=[]
    for row in predictions:
        if row['status']!='GRADED': continue
        original=frozen_predictions[row['fixture_key']]
        verified,state=graded_match(original,records)
        require(verified is not None and str(verified['match_id'])==row.get('source_match_id'),'Prediction result absent from verified cache')
        require(result_source_verified(verified),'Prediction cache source is not verified finished')
        require(row.get('match_source')==verified['source'], 'Prediction result lacks verified source')
        require(row.get('final_score')==f"{verified['home_goals']}-{verified['away_goals']}", 'Prediction score differs from verified cache')
        probs=[number(original.get('p_'+side),min_value=0,max_value=1) for side in ('home','draw','away')]
        if all(p is not None for p in probs):
            h,a=verified['home_goals'],verified['away_goals']
            expected=sum((p-y)**2 for p,y in zip(probs,(h>a,h==a,h<a)))
            close(row.get('one_x_two_brier'),expected,'Prediction Brier')
            prediction_brier.append(expected)
    close(metrics.get('prediction_1x2_multiclass_brier'),sum(prediction_brier)/len(prediction_brier) if prediction_brier else None,'Prediction mean Brier')
    workbook=root/'readable'/REPORT_NAME
    with ZipFile(workbook) as z:
        require(z.testzip() is None,'Corrupt workbook ZIP')
        require('xl/workbook.xml' in z.namelist(),'Missing native workbook')
        for name in z.namelist():
            if name.endswith('.xml'):ET.fromstring(z.read(name))
        require(len([n for n in z.namelist() if '/charts/chart' in n and n.endswith('.xml')])>=2,'Missing native report charts')
    report_workbook_check(root, workbook)
    from model_activity import check as activity_check
    activity_check(root)  # the activity log only grows: every committed line kept byte for byte, ids unique
    require((performance/'README.md').is_file(),'Missing readable performance report')
    warnings=audit['warnings']
    if metrics.get('provider_errors'):warnings.append('Result provider has errors; cached verified results used where available')
    experiments={}
    # Retired experiments' committed reports are frozen (archive/), now including the
    # benchmark-forward and totals-anchor trials; no live trial must match this review.
    closing_path=performance/"closing_odds/summary.json"
    if closing_path.exists():
        from closing_odds import validate_report as validate_closing
        validate_closing(root)
    training={}
    from prediction_runs import resolve_raw
    for path in sorted(resolve_raw(root/'raw').glob('*_diagnostics.json')):
        data=read_json(path);training[path.stem.replace('_diagnostics','')]=data.get('training_end')
    health_path=performance/'pipeline_health.json'
    health_data=read_json(health_path) if health_path.exists() else {}
    if health_data:
        health_time=utc(health_data.get('reviewed_at_utc'))
        require(health_time and abs((health_time-utc(metrics['reviewed_at_utc'])).total_seconds())<1,'Health report timestamp differs from performance review')
        history=read_json(performance/'health_history.json')
        latest=history.get('days',{}).get(health_time.date().isoformat(),{})
        for field,value in metrics['shortlist'].items():close(latest.get('shortlist_performance',{}).get(field),value,'Daily health performance '+field)
        require(len(health_data.get('snapshot_capture_history',[]))==len(audit['snapshots']),'Health snapshot coverage mismatch')
        from excel_book import read_workbook
        dashboard=' '.join(str(v) for v in read_workbook(workbook)['cells']['Dashboard'].values())
        require('Data health' in dashboard and 'Last forecast generated' in dashboard,'Missing data health on the workbook Dashboard')
    for league, info in health_data.get('training',{}).items():
        state=info.get('current_source_health',{}).get('status')
        if state and state not in ('CURRENT_WITHIN_PROVIDER_SCHEDULE', 'VERIFIED_WITHIN_24_HOURS'): warnings.append(league+' training/source health: '+state)
        if info.get('current_source_health', {}).get('official_source_health'):
            warnings.append(league+': live UEFA denied access; using reviewed factual attestations for covered matches only')
    for league, info in health_data.get('training', {}).items():
        if info.get('odds_provider_health', {}).get('state') == 'CREDITS_EXHAUSTED':
            warnings.append(league+': all configured Odds API credentials confirmed exhausted during forecast generation')
    freshness = health_data.get('forecast_freshness', {})
    if freshness.get('status') == 'INVALID_FUTURE_TIME' or (freshness.get('upcoming_fixture_count', 0)
            and freshness.get('status') == 'OLDER_THAN_24_HOURS'):
        warnings.append('Stored forecast freshness: '+freshness['status'])
    quote_audit = health_data.get('quote_audit', {})
    if (quote_audit.get('selected_quotes', 0) and quote_audit.get('past_kickoff_count', 0)
            and not quote_audit.get('upcoming_kickoff_count', 0)
            and freshness.get('upcoming_fixture_count', 0)):
        warnings.append('Stored shortlist has no remaining future kickoffs; regenerate forecasts for current selections')
    if health_data.get('quote_audit',{}).get('exchange_quotes'): warnings.append('Latest stored shortlist includes gross exchange quotes from an older execution policy')
    capture_history = health_data.get('snapshot_capture_history', [])
    if capture_history:
        for name, state in capture_history[-1].get('experiments', {}).items():
            if state in ('PRESENT_BUT_REJECTED', 'MISSING_OR_TAMPERED'):
                warnings.append(f'{name}: latest snapshot {state}; experimental evidence was not accepted')
    # The master release's rollback rule (price_edge_tracking.master_rollback): reported first in the run summary.
    rollback_path=performance/'price_edge_v27'/'summary.json'
    tracking=read_json(rollback_path) if rollback_path.exists() else {}
    rollback=tracking.get('master_rollback') or {}
    incidents=tracking.get('master_release_incidents') or {}
    # Release incidents (new master failed -> old master published; old master shadow failed -> comparison baseline
    # missing), with their run counts, right after the rollback trigger; never an ordinary wait for data.
    for message in reversed(incidents.get('messages', [])): warnings.insert(0, message)
    if rollback.get('triggered'): warnings.insert(0, rollback['message'])
    return {'status':'VERIFIED_WITH_WARNINGS' if warnings else 'VERIFIED','pipeline_health':health_data,'reviewed_at_utc':metrics['reviewed_at_utc'],
        'snapshots':len(audit['snapshots']),'shortlist':metrics['shortlist'],'policy_groups':metrics['groups']['policy'],
        'provider_errors':metrics.get('provider_errors',{}),'training_end_dates':training,'experiments':experiments,'warnings':warnings,
        'master_rollback':rollback,'master_release_incidents':incidents}


def registry_check(repo):
    """Every registry league has a scheduled refresh that runs its refresh script."""
    import league_registry
    league_registry.validate()
    workflows=repo/'.github/workflows'
    methods={}
    for league in league_registry.REGISTRY:
        method=league_registry.REFRESH_METHODS[league.refresh_method]
        require((repo/method['script']).is_file(),f"{league.key}: missing refresh script {method['script']}")
        workflow=workflows/method['workflow']
        require(workflow.is_file(),f"{league.key}: missing refresh workflow {method['workflow']}")
        text=workflow.read_text(encoding='utf-8')
        require('schedule:' in text and method['script'] in text,
                f"{league.key}: {method['workflow']} does not schedule {method['script']}")
        if method['needs_secret']:
            require(method['needs_secret'] in text,f"{league.key}: {method['workflow']} lacks {method['needs_secret']}")
        methods.setdefault(league.refresh_method,[]).append(league.key)
    return {'leagues':list(league_registry.LEAGUES),'refresh_methods':methods}


def run_help(repo, name):
    """Run a CLI's --help without inheriting this process's handles.

    Windows cannot always duplicate an inherited stdin/stderr (WinError 6), so
    stdin is closed and stderr captured, then echoed so output is unchanged.
    """
    try:
        result=subprocess.run([sys.executable,str(repo/name),'--help'],check=True,stdin=subprocess.DEVNULL,
                              stdout=subprocess.DEVNULL,stderr=subprocess.PIPE,cwd=repo,timeout=30)
    except (subprocess.CalledProcessError,subprocess.TimeoutExpired) as error:
        if error.stderr:sys.stderr.write(error.stderr.decode(errors='replace'))
        raise
    if result.stderr:sys.stderr.write(result.stderr.decode(errors='replace'))


def smoke(repo):
    paths=sorted(repo.glob('*.py'))+sorted((repo/'tests').glob('*.py'))
    for path in paths:compile(path.read_text(encoding='utf-8-sig'),str(path),'exec')
    for name in CLI_FILES:run_help(repo,name)
    return {'python_modules_compiled':len(paths),'cli_help_checked':len(CLI_FILES),'league_registry':registry_check(repo)}


def coverage_check(path):
    data=read_json(path)
    require(data['totals']['percent_covered']>=75,'Overall application coverage below 75%')
    for name,floor in COVERAGE_FLOORS.items():
        found=[entry for file,entry in data['files'].items() if Path(file).name==name]
        require(len(found)==1,f'Missing coverage for {name}')
        require(found[0]['summary']['percent_covered']>=floor,f'{name}: coverage below {floor}%')
    return {'overall_percent':data['totals']['percent_covered'],'critical_module_floors':COVERAGE_FLOORS}


def emit(data,output=None,summary=False):
    content=json.dumps(data,indent=2,allow_nan=False)+'\n'
    if output:
        output.parent.mkdir(parents=True,exist_ok=True);output.write_text(content,encoding='utf-8')
    print(content)
    if summary and (destination:=os.getenv('GITHUB_STEP_SUMMARY')):
        with open(destination,'a',encoding='utf-8') as handle:
            rollback=data.get('master_rollback') or {}
            if rollback.get('triggered'):  # the release's rollback rule, first in the run summary; never acted on
                handle.write(f"> **{rollback['status']}** (master shortlist): {rollback['message']}\n\n")
            for message in (data.get('master_release_incidents') or {}).get('messages', []):
                head, _, rest = message.partition(' in ')
                handle.write(f"> **{head}** (master shortlist) in {rest}\n\n")
            handle.write('## Forward review integrity\n\n')
            handle.write(f'Status: **{data.get("status","VERIFIED")}**; snapshots: {data.get("snapshots",0)}.\n\n')
            if 'shortlist' in data:
                d=data['shortlist'];handle.write(f'Selections: {d["total"]}; graded: {d["graded"]}; pending: {d["pending"]}.\n\n')
            for warning in data.get('warnings',[]):handle.write(f'- {warning}\n')
            handle.write('\nTraining end dates: '+json.dumps(data.get('training_end_dates',{}))+'\n')
            handle.write('\n| Policy | Graded | Wins | Losses | Pending |\n|---|---:|---:|---:|---:|\n')
            for policy,counts in data.get('policy_groups',{}).items():
                handle.write(f"| {policy} | {counts['graded']} | {counts['wins']} | {counts['losses']} | {counts['pending']} |\n")
            for name,experiment in data.get('experiments',{}).items():
                handle.write('\n'+name+': '+json.dumps({k:v for k,v in experiment.items() if k in
                    ('total_fixture_markets','observed_fixture_markets','available_fixture_markets',
                     'graded_fixture_markets','paired_graded_fixture_markets','selected','graded_selections','decision')})+'\n')


def main(argv=None):
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action',choices=('smoke','capture','raw','archives','reports','coverage'))
    parser.add_argument('--repo',type=Path,default=Path('.'))
    parser.add_argument('--root',type=Path,default=Path('football_output_v2'))
    parser.add_argument('--event',default='workflow_dispatch')
    parser.add_argument('--sha',default=os.getenv('GITHUB_SHA',''))
    parser.add_argument('--before',default=os.getenv('BEFORE_SHA',''))
    parser.add_argument('--output',type=Path)
    parser.add_argument('--github-summary',action='store_true')
    parser.add_argument('--coverage-file',type=Path,default=Path('workflow_artifacts/coverage.json'))
    args=parser.parse_args(argv)
    if args.action=='smoke':data=smoke(args.repo)
    elif args.action=='capture':data={'captured':capture_event(args.repo,args.root,args.event,args.sha,args.before)}
    elif args.action=='raw':data=raw_check(args.root)
    elif args.action=='archives':data=archive_check(args.root)
    elif args.action=='reports':data=report_check(args.root)
    else:data=coverage_check(args.coverage_file)
    emit(data,args.output,args.github_summary)
    return 0


if __name__=='__main__':raise SystemExit(main())



