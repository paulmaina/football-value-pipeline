"""Goal-market/count-market validation runs only when the selection policy uses it."""
from datetime import datetime, timedelta
import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import pandas as pd

from offline_test_case import OfflineQuotePolicyTestCase
import asian_handicap
import football_value_pipeline_v2_standalone as pipeline
import prediction_runs as runs
from test_prediction_run_publication import publish
from test_performance_tracking import T0
from workflow_checks import raw_check


class PolicyMetadataTests(OfflineQuotePolicyTestCase):
    def test_policies_declare_whether_selection_reads_validation(self):
        self.assertFalse(asian_handicap.requires_goal_market_validation(asian_handicap.CAGEY_POLICY))
        self.assertFalse(asian_handicap.requires_goal_market_validation(asian_handicap.PRICE_EDGE_POLICY))
        for policy in (asian_handicap.NO_LOSS_CORNERS_POLICY, asian_handicap.POLICY, asian_handicap.LEGACY_POLICY,
                       asian_handicap.CORNERS_CARDS_POLICY, 'conservative-policy-before-asian-handicap'):
            self.assertTrue(asian_handicap.requires_goal_market_validation(policy), policy)

    def test_scheduled_v28_runs_skip_validation_unless_requested(self):
        parse = pipeline.build_parser().parse_args
        self.assertFalse(pipeline.goal_market_validation_enabled(parse(['--leagues', 'EPL'])))
        self.assertTrue(pipeline.goal_market_validation_enabled(parse(['--goal-market-validation'])))
        self.assertFalse(pipeline.goal_market_validation_enabled(parse(['--backtest', '--goal-market-validation'])))
        # Derived from the production policy's metadata, not hard-coded.
        with patch.object(asian_handicap, 'PRODUCTION_POLICY', asian_handicap.NO_LOSS_CORNERS_POLICY):
            self.assertTrue(pipeline.goal_market_validation_enabled(parse([])))


class PipelineTests(OfflineQuotePolicyTestCase):
    def test_validation_on_and_off_give_identical_predictions_and_picks(self):
        from test_conservative_bet_filter import fixture
        frame = pd.DataFrame([fixture()])
        outputs = {}
        import team_research
        from functools import partial
        fixed = partial(team_research.enrich, clock=lambda: T0)
        self.addCleanup(patch.stopall)
        patch.dict(os.environ).start()  # main() loads API keys into os.environ; restore it afterwards
        patch('team_research.enrich', side_effect=fixed).start()
        # Validation modes must use the same decision cutoff as their frozen research.
        clock = patch('football_value_pipeline_v2_standalone.datetime', wraps=datetime).start()
        clock.now.return_value = T0
        decision_clock = patch('conservative_bet_filter.datetime', wraps=datetime).start()
        decision_clock.now.return_value = T0
        for flag in ([], ['--goal-market-validation']):
            with tempfile.TemporaryDirectory() as path:
                raw = Path(path)/'raw'
                with patch('football_value_pipeline_v2_standalone.FootballValuePipelineV2.run_league',
                           return_value=(frame, {'training_end': '2026-09-20', 'training_matches': 1000,
                                                 'training_sha256': 'a'*64}, {})),                      patch('football_value_pipeline_v2_standalone.FootballValuePipelineV2.backtest_league',
                           return_value=(pd.DataFrame(), pd.DataFrame(), {}, pd.DataFrame())) as backtest,                      patch('count_markets.validate_league', return_value={}) as counts:
                    self.assertEqual(pipeline.main(['--no-research-free-sources', '--leagues', 'EPL', '--no-legacy-comparison', *flag,
                                                    '--out-dir', str(raw)]), 0)
                bundle = runs.resolve_raw(raw)
                validated = bool(flag)
                self.assertEqual((backtest.call_count, counts.call_count), (int(validated), int(validated)))
                self.assertEqual((bundle/'EPL_goal_market_validation.json').exists(), validated)
                diagnostics = json.loads((bundle/'EPL_diagnostics.json').read_text())
                self.assertEqual('goal_market_validation' in diagnostics, not validated)
                summary = json.loads((bundle/'conservative_bet_summary.json').read_text())
                self.assertFalse(summary['validation_required'])
                # Bound into the immutable summary, so replay knows this run carries monitoring records.
                self.assertEqual(summary['correction_monitoring_version'], 'cagey-correction-monitoring-v1')
                self.assertTrue((bundle/'cagey_correction_monitoring.csv').exists())
                outputs[validated] = {name: pd.read_csv(bundle/name) for name in
                                      ('all_leagues_predictions.csv', 'conservative_bet_shortlist.csv',
                                       'cagey_tier_shortlist.csv', 'conservative_bet_rejections.csv')}
        # Same inputs and cutoff; toggling validation must not change probabilities, picks or research.
        for name, frame_off in outputs[False].items():
            pd.testing.assert_frame_equal(frame_off.drop(columns=['evaluated_at_utc'], errors='ignore'),
                                          outputs[True][name].drop(columns=['evaluated_at_utc'], errors='ignore'),
                                          obj=name)


class BundleTests(OfflineQuotePolicyTestCase):
    def test_unused_validation_cache_is_not_copied_into_a_new_bundle(self):
        with tempfile.TemporaryDirectory() as temp:
            raw = Path(temp)/'raw'
            raw.mkdir()
            (raw/'EPL_goal_market_validation.json').write_text('{}')
            (raw/'EPL_predictions.csv').write_text('league\n')
            with runs.stage_run(raw, validation_cache=False) as staging:
                self.assertEqual(sorted(p.name for p in staging.iterdir()), [])
            with runs.stage_run(raw) as staging:
                self.assertEqual(sorted(p.name for p in staging.iterdir()), ['EPL_goal_market_validation.json'])
            with runs.stage_run(raw, seed=True, validation_cache=False) as staging:
                self.assertEqual(sorted(p.name for p in staging.iterdir()), ['EPL_predictions.csv'])

    def test_v28_refresh_leaves_validation_out_but_earlier_bundles_keep_it(self):
        from refresh_conservative_shortlist import refresh
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            first = publish(root)
            self.assertTrue((first/'EPL_goal_market_validation.json').exists())
            refresh(root, as_of=T0 + timedelta(minutes=1))
            current = runs.resolve_raw(root/'raw')
            self.assertNotEqual(current, first)
            self.assertFalse((current/'EPL_goal_market_validation.json').exists())
            self.assertTrue((first/'EPL_goal_market_validation.json').exists())
            self.assertEqual(runs.validate_bundle(first)['run_id'], first.name)
            self.assertEqual(raw_check(root)['forecasts'], 1)


class FailClosedTests(OfflineQuotePolicyTestCase):
    def summary_for(self, root, **changes):
        path = root/'raw'/'conservative_bet_summary.json'
        summary = {**json.loads(path.read_text()), **changes}
        path.write_text(json.dumps(summary))

    def test_policy_requiring_validation_fails_without_evidence(self):
        from test_prediction_run_tracking import save_run
        from test_performance_tracking import fixture, pick
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            save_run(root, T0, [fixture()], [pick()])
            policy = asian_handicap.NO_LOSS_CORNERS_POLICY
            self.summary_for(root, selection_policy_version=policy, validation_required=False)
            # Checked before any replay; absent files for a required policy also fail
            # ('Missing ... reliability evidence', test_probability_shortlist).
            with self.assertRaisesRegex(ValueError, 'requires goal-market validation evidence'):
                raw_check(root)


if __name__ == '__main__':
    unittest.main()
