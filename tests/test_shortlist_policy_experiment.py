from offline_test_case import OfflineQuotePolicyTestCase
import copy
from datetime import timedelta
import hashlib
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import pandas as pd

from conservative_bet_filter import build_conservative_shortlist
import shortlist_policy_experiment as trial
from performance_tracking import capture, snapshots, write_json
from test_conservative_bet_filter import fixture, NOW
from test_filter_sensitivity_experiment import record
from test_graded_candidates import sample_report


def setup(root, row=None, clock=NOW, reliability=None):
    raw = root/'raw'; raw.mkdir(parents=True, exist_ok=True)
    row = row or fixture()
    row.update(home_team='Manchester City FC', away_team='Everton FC',
               model_home_team='Manchester City FC', model_away_team='Everton FC')
    predictions = pd.DataFrame([row])
    picks, decisions, summary = build_conservative_shortlist(predictions, as_of=clock,
        market_reliability=reliability)
    predictions.to_csv(raw/'all_leagues_predictions.csv', index=False)
    picks.to_csv(raw/'conservative_bet_shortlist.csv', index=False)
    write_json(raw/'conservative_bet_summary.json', summary)
    for i, (league, report) in enumerate((reliability or {}).items()):
        write_json(raw/f'{i}_goal_market_validation.json', {**report, 'league': league})
        report['league'] = league
    data = trial.write_experiment(predictions, raw, summary, decisions, reliability)
    return raw, data, predictions, picks, decisions, summary


class PolicyExperimentTests(OfflineQuotePolicyTestCase):
    def test_missing_bookmakers_replay_identically_from_csv_and_capture(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            row = fixture()
            for key in ('home', 'away', 'over_1_5', 'home_draw', 'draw_away', 'home_away'):
                row['best_'+key+'_bookmaker'] = float('nan')
            raw, data, predictions, _, _, summary = setup(root, row=row)
            self.assertTrue(all(r['bookmaker'] is None for r in data['rows']))
            self.assertTrue(all(r['decision'] == 'REJECTED' for r in data['rows']))
            self.assertIsNotNone(trial.capture_file(raw, summary['generated_at_utc']))
            self.assertTrue(capture('a'*40, root=root, captured_at=NOW))
            rows, rejected = trial.frozen(root, snapshots(root))
            self.assertEqual(len(rows), 54)
            self.assertFalse(rejected)

    def test_control_grid_isolation_and_production_unchanged(self):
        with tempfile.TemporaryDirectory() as tmp:
            raw, data, predictions, picks, decisions, summary = setup(Path(tmp))
            before = {p.name: p.read_bytes() for p in raw.glob('*.csv')}
            self.assertEqual(len(data['rows']), 54)
            self.assertEqual(len(trial.VARIANTS), 9)
            self.assertTrue(all(len(v) == 1 for k, v in trial.VARIANTS.items() if k != 'control'))
            trial.validate(data, summary['generated_at_utc'], predictions.to_dict('records'))
            with patch('quote_policy.load_policy', side_effect=AssertionError('Current policy must not replace frozen policy')):
                trial.validate(data, summary['generated_at_utc'], predictions.to_dict('records'))
            self.assertIsNotNone(trial.capture_file(raw, summary['generated_at_utc']))
            self.assertEqual(before, {p.name: p.read_bytes() for p in raw.glob('*.csv')})
            replay = build_conservative_shortlist(predictions, as_of=NOW)
            pd.testing.assert_frame_equal(picks, replay[0])
            pd.testing.assert_frame_equal(decisions, replay[1])
            self.assertEqual(summary, replay[2])
            self.assertFalse(any(r['market'] == 'Both Teams to Score - Yes' for r in data['rows']))
            self.assertTrue(any(r['market'] == 'Double Chance 12' for r in data['rows']))

    def test_probability_dimensions_and_penalty_strength_are_independent(self):
        row = fixture(); row['p_over_1_5'] = .76; row['raw_p_over_1_5'] = .70
        def decision(policy, report=None):
            _, table, _ = build_conservative_shortlist(pd.DataFrame([row]), as_of=NOW,
                market_reliability=report, research_policy=policy)
            return table.loc[table.market.eq('Over 1.5')].iloc[0]
        lower = decision({'blended_shift': -.03})
        self.assertNotIn('blended probability below', lower.rejection_reasons)
        self.assertIn('raw Dixon-Coles probability below', lower.rejection_reasons)
        self.assertIn('reliability-adjusted probability below', lower.rejection_reasons)
        lower = decision({'raw_shift': -.03})
        self.assertNotIn('raw Dixon-Coles probability below', lower.rejection_reasons)
        self.assertIn('blended probability below', lower.rejection_reasons)
        lower = decision({'adjusted_shift': -.03})
        self.assertNotIn('reliability-adjusted probability below', lower.rejection_reasons)
        self.assertIn('blended probability below', lower.rejection_reasons)
        row['p_over_1_5'] = .82; row['raw_p_over_1_5'] = .80
        report = sample_report()
        report['markets']['over_1_5']['confidence_penalty'] = .02
        report['markets']['over_1_5']['high_confidence']['75plus']['development_only_penalty'] = .04
        for multiplier in (.5, 1, 1.5):
            result = decision({'penalty_multiplier': multiplier}, {'Premier League': report})
            self.assertAlmostEqual(result.calibration_penalty, .04*multiplier)
            self.assertAlmostEqual(result.rank_probability, .82-.04*multiplier)
            self.assertEqual(result.high_confidence_status, 'PASSED')
        report['markets']['over_1_5']['confidence_penalty'] = 1
        self.assertEqual(decision({'penalty_multiplier': 1.5}, {'Premier League': report}).rank_probability, 0)
        report['markets']['over_1_5']['confidence_penalty'] = None
        self.assertIn('invalid or missing', decision({'penalty_multiplier': .5}, {'Premier League': report}).rejection_reasons)

    def test_invalid_research_and_execution_settings_are_rejected(self):
        for policy in ({'bogus': 1}, {'raw_shift': float('nan')}, {'raw_shift': -.031},
                       {'blended_shift': True}, {'penalty_multiplier': 0}, {'adjusted_shift': float('inf')}, []):
            with self.assertRaises(ValueError):
                build_conservative_shortlist(pd.DataFrame([fixture()]), as_of=NOW, research_policy=policy)
        from quote_policy import validate_policy
        for policy in (None, {'allowed_bookmakers': [3]}, {'per_stake_cost_bps': float('nan')}):
            with self.assertRaises(ValueError): validate_policy(policy)

    def test_frozen_validation_quotes_and_policy_are_bound(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            raw, data, predictions, picks, _, summary = setup(root, reliability={'Premier League': sample_report()})
            self.assertIsNotNone(trial.capture_file(raw, summary['generated_at_utc']))
            mutations = [lambda d: d.update(version='bad'), lambda d: d.update(variants={}),
                lambda d: d.update(selection_policy_version='other'), lambda d: d['rows'].pop(),
                lambda d: d['rows'].append(copy.deepcopy(d['rows'][0])),
                lambda d: d['rows'][0].update(rank_probability=.001),
                lambda d: d['rows'][0].update(bookmaker='Fabricated'),
                lambda d: d['rows'][0].update(rejection_reasons='altered'),
                lambda d: d.update(validation_evidence=[]), lambda d: d.update(execution_policy={})]
            for mutate in mutations:
                bad = copy.deepcopy(data); mutate(bad)
                with self.assertRaises(ValueError): trial.validate(bad, summary['generated_at_utc'], predictions.to_dict('records'))
            with self.assertRaises(ValueError): trial.validate(data, (NOW+timedelta(seconds=1)).isoformat(), predictions.to_dict('records'))
            with self.assertRaises(ValueError): trial.validate(data, summary['generated_at_utc'], predictions.to_dict('records')*2)
            with self.assertRaises(ValueError): trial.validate(None, summary['generated_at_utc'], [])
            bad = copy.deepcopy(data); bad['rows'][0]['rank_probability'] = float('nan')
            with self.assertRaises(ValueError): trial.validate(bad, summary['generated_at_utc'], predictions.to_dict('records'))
            with self.assertRaises(ValueError): trial.validate_control(data, [])
            report = next(raw.glob('*_goal_market_validation.json')); report.write_text('{}')
            with self.assertRaises(ValueError): trial.capture_file(raw, summary['generated_at_utc'])
            (raw/'all_leagues_predictions.csv').write_bytes(b'altered')
            with self.assertRaises(ValueError): trial.capture_file(raw, summary['generated_at_utc'])
            (raw/(trial.NAME+'.json')).unlink()
            self.assertIsNone(trial.capture_file(raw, summary['generated_at_utc']))

    def test_capture_freeze_grading_reconciliation_and_optional_tamper(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); raw, data, predictions, *_ = setup(root)
            capture('a'*40, root=root, captured_at=NOW)
            capture('b'*40, root=root, captured_at=NOW+timedelta(minutes=1))
            rows, rejected = trial.frozen(root, snapshots(root))
            self.assertEqual(len(rows), 54); self.assertFalse(rejected)
            rec = record(predictions.iloc[0].to_dict())
            write_json(root/'performance/verified_results.json', {'PL:90002': rec})
            clock = NOW+timedelta(days=3)
            summary = trial.review_experiment(root, snapshots(root), [rec], clock)
            self.assertEqual(summary['verified_fixtures'], 1)
            self.assertEqual(summary['verified_coverage'], 1)
            self.assertEqual(summary['status'], 'COLLECT_MORE_DATA')
            self.assertEqual(len(summary['comparisons']), 27)
            self.assertTrue(trial.validate_report(root))
            self.assertAlmostEqual(summary['paired_strict_returns'][0]['mean_profit_delta_per_fixture'], 0)
            pending = trial.review_experiment(root, snapshots(root), [rec], NOW)
            self.assertEqual(pending['verified_fixtures'], 0)
            self.assertTrue(trial.validate_report(root))
            dest = root/'performance'/trial.NAME
            altered = copy.deepcopy(pending); altered['candidate_decisions'] = 10000
            write_json(dest/'summary.json', altered)
            with self.assertRaises(ValueError): trial.validate_report(root)
            trial.review_experiment(root, snapshots(root), [rec], clock)
            ledger = dest/'selections.csv'; ledger.write_text(ledger.read_text().replace('SHORTLISTED', 'REJECTED'))
            with self.assertRaises(ValueError): trial.validate_report(root)
            trial.review_experiment(root, snapshots(root), [rec], clock)
            ledger.write_text('fixture_key\n')
            with self.assertRaises(ValueError): trial.validate_report(root)
            archive = root/'performance/snapshots'/('a'*16)/(trial.NAME+'.json')
            archive.write_text('{}')
            self.assertEqual(len(snapshots(root)), 2)
            rows, rejected = trial.frozen(root, snapshots(root))
            self.assertIn('a'*40, rejected); self.assertEqual(len(rows), 54)
            summary = trial.review_experiment(root, snapshots(root), [], clock)
            self.assertEqual(summary['status'], 'DATA_QUALITY_BLOCKED')

    def test_legacy_late_and_outside_horizon_do_not_supply_evidence(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); raw, *_ = setup(root, row=fixture(kickoff=NOW+timedelta(days=4)))
            capture('a'*40, root=root, captured_at=NOW)
            self.assertEqual(trial.frozen(root, snapshots(root))[0], [])
            (raw/(trial.NAME+'.json')).unlink()
            capture('b'*40, root=root, captured_at=NOW)
            self.assertEqual(trial.frozen(root, snapshots(root))[0], [])
            _, _, predictions, *_ = setup(root)
            captured = NOW+timedelta(days=1, minutes=-19)
            self.assertFalse(capture('c'*40, root=root, captured_at=captured))
            summary = trial.review_experiment(root, [], [], NOW)
            self.assertEqual(summary['total_fixtures'], 0)
            write_json(root/'performance/verified_results.json', {})
            # Validate an actually empty archive separately.
            with patch('performance_tracking.snapshots', return_value=[]):
                self.assertTrue(trial.validate_report(root))

    def test_bootstrap_and_readiness_count_unique_fixtures_not_markets(self):
        rows = []
        for i in range(300):
            for variant in trial.VARIANTS:
                rows.append({'fixture_key': str(i), 'kickoff_utc': (NOW+timedelta(days=i//5)).isoformat(),
                    'variant_id': variant, 'decision': 'SHORTLISTED', 'selection_tier': 'STRICT',
                    'market': 'Home win', 'league': 'Premier League', 'rank_probability': .8,
                    'offered_decimal_odds': 1.5, 'per_stake_cost': .02})
        match = {'home_goals': 2, 'away_goals': 0, 'match_id': 90002}
        with patch.object(trial, 'frozen', return_value=(rows, [])), patch('performance_tracking.fixture_match', return_value=(match, 'VERIFIED')):
            summary, _, coverage = trial.evaluate(Path('.'), [], [], NOW+timedelta(days=90))
        self.assertEqual(summary['verified_fixtures'], 300)
        self.assertEqual(summary['status'], 'READY_FOR_REVIEW')
        paired = summary['paired_strict_returns'][0]
        self.assertEqual(paired['weekly_block_bootstrap95'], [0, 0])
        self.assertFalse(summary['automatic_production_change'])
        self.assertEqual(summary['paired_probability_deltas'][0]['brier_weekly_bootstrap95'], [0, 0])
        self.assertEqual(summary['paired_probability_deltas'][0]['log_loss_mean_delta'], 0)
        self.assertEqual(trial.paired_returns([], 'raw_lower')['weekly_block_bootstrap95'], None)
        # A policy which skips loses no stake: explicit zero, not a missing pair.
        coverage[1]['decision'] = 'REJECTED'
        self.assertLess(trial.paired_returns(coverage, 'blended_lower')['mean_profit_delta_per_fixture'], 0)

    def test_broken_sidecar_never_blocks_baseline_capture_and_shows_health(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); raw, *_ = setup(root)
            (raw/(trial.NAME+'.json')).write_text('{}')
            with self.assertWarnsRegex(UserWarning, 'Shortlist policy capture skipped'):
                self.assertTrue(capture('a'*40, root=root, captured_at=NOW))
            health = json.loads((root/'performance/snapshots'/('a'*16)/'pipeline_health.json').read_text())
            self.assertEqual(health['experiments'][trial.NAME], 'PRESENT_BUT_REJECTED')

    def test_review_queue_and_excel_readiness_integration(self):
        from experiment_review_queue import build_queue
        from performance_report_layout import experiment_rows
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            summary = trial.review_experiment(root, [], [], NOW)
            queue = build_queue(root, NOW)
            item = next(r for r in queue['experiments'] if r['name'] == trial.NAME)
            self.assertEqual(item['status'], 'COLLECT_MORE_DATA')
            row = next(r for r in experiment_rows(root, {'review_queue': queue}) if r[0] == 'Probability / calibration policy')
            self.assertEqual(row[4], '300 paired fixtures')
            self.assertIn('300 more paired fixtures', row[8])

    def test_control_mismatch_unsupported_policy_and_missing_archive_are_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            raw, data, predictions, _, decisions, summary = setup(root)
            wrong = decisions.copy(); wrong.loc[0, 'decision'] = 'REJECTED'
            with self.assertRaises(ValueError):
                trial.write_experiment(predictions, raw, summary, wrong, None)
            with patch.object(trial, 'BASELINE_POLICY', 'unsupported'):
                with self.assertRaises(ValueError):
                    trial.decision_rows(predictions, summary['generated_at_utc'], None, data['execution_policy'])
            capture('a'*40, root=root, captured_at=NOW)
            archive = root/'performance/snapshots'/('a'*16)
            path = archive/(trial.NAME+'.json')
            # Changing a hash-bound field and updating only the sidecar hash
            # still fails replay/forecast binding; baseline snapshots survive.
            altered = copy.deepcopy(data); altered['predictions_sha256'] = '0'*64
            write_json(path, altered)
            meta_path = archive/'metadata.json'; meta = json.loads(meta_path.read_text())
            meta['sha256'][path.name] = hashlib.sha256(path.read_bytes()).hexdigest()
            write_json(meta_path, meta)
            self.assertEqual(trial.frozen(root, snapshots(root))[1], ['a'*40])
            altered = copy.deepcopy(data); altered['selection_policy_version'] = 'different'
            write_json(path, altered); meta['sha256'][path.name] = hashlib.sha256(path.read_bytes()).hexdigest(); write_json(meta_path, meta)
            self.assertEqual(trial.frozen(root, snapshots(root))[1], ['a'*40])
