"""Adaptive rules are frozen pre-off, replayable and isolated from legacy results."""
import copy
from datetime import timedelta
from pathlib import Path
import tempfile
from zipfile import ZipFile

import shortlist_weight_experiment as trial
from offline_test_case import OfflineQuotePolicyTestCase
from performance_tracking import capture, snapshots, write_json
from test_shortlist_weight_experiment import setup
from test_conservative_bet_filter import NOW, fixture
from test_filter_sensitivity_experiment import record


class AdaptiveWeightTests(OfflineQuotePolicyTestCase):
    def evidence(self, **changes):
        return dict(development_validation_matches=300, calibration_penalty=0,
                    raw_dc_probability=.8, market_probability=.8, odds_age_hours=0, **changes)

    def test_evidence_bounds_and_each_uncertainty_factor_reduce_ev_influence(self):
        good = self.evidence()
        self.assertAlmostEqual(trial.adaptive_weight(good)['probability_weight_used'], .5)
        for field, value in [('development_validation_matches', 0), ('calibration_penalty', .1),
                             ('market_probability', .5), ('odds_age_hours', 24)]:
            bad = dict(good, **{field: value})
            self.assertAlmostEqual(trial.adaptive_weight(bad)['probability_weight_used'], .9)
        middle = dict(good, development_validation_matches=150, calibration_penalty=.02,
                      market_probability=.75, odds_age_hours=6)
        result = trial.adaptive_weight(middle)
        self.assertAlmostEqual(result['adaptive_evidence_quality'], .5*.8*.8*.75)
        self.assertAlmostEqual(result['probability_weight_used'], .804)
        for value in (None, '', 'bad', float('nan'), float('inf'), -1, True):
            for field in ('development_validation_matches', 'calibration_penalty', 'odds_age_hours'):
                self.assertAlmostEqual(trial.adaptive_weight(dict(good, **{field:value}))['probability_weight_used'], .9)
        for field, value in [('raw_dc_probability', None), ('market_probability', 2)]:
            self.assertAlmostEqual(trial.adaptive_weight(dict(good, **{field:value}))['probability_weight_used'], .9)
        changed = dict(good, audit_brier=0, audit_validation_matches=100000,
                       high_confidence_audit_observed_rate=1, outcome=1, unit_profit=100)
        self.assertEqual(trial.adaptive_weight(good), trial.adaptive_weight(changed))

    def test_frozen_rule_and_per_market_weights_are_bound_to_replay(self):
        with tempfile.TemporaryDirectory() as tmp:
            raw, data, frame, _, _, summary = setup(Path(tmp))
            adaptive = [r for r in data['rows'] if r['variant_id'] == trial.ADAPTIVE_ID]
            self.assertEqual(len(adaptive), 7)
            self.assertGreater(len({r['probability_weight_used'] for r in adaptive}), 1)
            for field in ('probability_weight_used', 'ev_weight_used', 'adaptive_history_support', 'adaptive_evidence_quality'):
                bad = copy.deepcopy(data)
                next(r for r in bad['rows'] if r['variant_id'] == trial.ADAPTIVE_ID)[field] = .12345
                with self.assertRaises(ValueError):
                    trial.validate(bad, summary['generated_at_utc'], frame.to_dict('records'))
            bad = copy.deepcopy(data)
            bad['variants'][trial.ADAPTIVE_ID]['adaptive_rule']['development_target'] = 1
            with self.assertRaises(ValueError): trial.validate(bad, summary['generated_at_utc'], frame.to_dict('records'))
            bad['version'] = trial.LEGACY_VERSION
            with self.assertRaises(ValueError): trial.validate(bad, summary['generated_at_utc'], frame.to_dict('records'))
            self.assertIsNotNone(trial.capture_file(raw, summary['generated_at_utc']))

    def legacy(self, raw, data, frame, summary):
        old = dict(data, version=trial.LEGACY_VERSION, variants=copy.deepcopy(trial.LEGACY_VARIANTS),
                   rows=trial.decision_rows(frame, summary['generated_at_utc'], data['validation_evidence'],
                       data['execution_policy'], version=trial.LEGACY_VERSION))
        write_json(raw/(trial.NAME+'.json'), old)
        self.assertIsNotNone(trial.capture_file(raw, summary['generated_at_utc']))
        return old

    def test_legacy_and_adaptive_captures_keep_separate_first_preoff_cohorts(self):
        from performance_excel import write_workbook
        from performance_report_layout import get_sheet, text, q
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            raw, data, frame, _, _, summary = setup(root)
            old = self.legacy(raw, data, frame, summary)
            self.assertEqual(len(old['rows']), 28)
            capture('a'*40, root=root, captured_at=NOW)
            legacy_only = trial.review_experiment(root, snapshots(root), [], NOW)
            self.assertEqual(legacy_only['total_fixtures'], 0)
            self.assertEqual(legacy_only['legacy_cohorts'][0]['total_fixtures'], 1)
            self.assertEqual(legacy_only['minimum_settled_per_weighting'], 0)
            self.assertTrue(trial.validate_report(root))
            write_json(raw/(trial.NAME+'.json'), data)
            capture('b'*40, root=root, captured_at=NOW+timedelta(minutes=1))
            capture('c'*40, root=root, captured_at=NOW+timedelta(minutes=2))
            frozen, rejected = trial.frozen(root, snapshots(root))
            self.assertEqual(rejected, [])
            self.assertEqual(len(frozen), 28+35)
            self.assertEqual({r['snapshot_commit'] for r in frozen}, {'a'*40, 'b'*40})
            rec = record(frame.iloc[0].to_dict())
            write_json(root/'performance/verified_results.json', {'PL:90002':rec})
            result = trial.review_experiment(root, snapshots(root), [rec], NOW+timedelta(days=3))
            self.assertEqual(result['verified_fixtures'], 1)
            self.assertEqual(result['legacy_cohorts'][0]['verified_fixtures'], 1)
            self.assertTrue(all(r['verified_fixtures'] == 1 for r in result['paired_all_returns']))
            self.assertEqual(len(result['comparisons']), 15)
            self.assertEqual(len(result['legacy_cohorts'][0]['comparisons']), 12)
            adaptive = next(r for r in result['comparisons'] if r['variant_id'] == trial.ADAPTIVE_ID and r['tier'] == 'ALL')
            self.assertEqual(adaptive['graded'], 1)
            self.assertIsNotNone(adaptive['mean_probability_weight'])
            self.assertTrue(trial.validate_report(root))
            report = (root/'performance'/trial.NAME/'report.md').read_text()
            self.assertIn('Legacy v1 fixed-weight cohort', report)
            self.assertIn('Calibration gap', report)
            self.assertIn('Adaptive evidence', report)
            workbook = write_workbook(root, [], [], {})
            with ZipFile(workbook) as z: parts = {n:z.read(n) for n in z.namelist()}
            displayed = ' '.join(str(text(c) or '') for c in get_sheet(parts, 'Experiments').root.iter(q('c')))
            self.assertIn('Legacy v1 fixed weights', displayed)
            self.assertIn('Adaptive evidence', displayed)
            self.assertIn('Brier', displayed)

    def test_hard_quote_identity_and_time_failures_are_never_rescued(self):
        for bad in (dict(fixture(), home_name_match_score=0), fixture(kickoff=NOW+timedelta(hours=49))):
            with tempfile.TemporaryDirectory() as tmp:
                _, data, *_ = setup(Path(tmp), [bad])
                self.assertFalse(any(r['decision'] in trial.SELECTED for r in data['rows'] if r['variant_id'] == trial.ADAPTIVE_ID))

    def test_weights_can_change_the_selected_market_without_changing_its_probability(self):
        from shortlist_policy_experiment import decision_rows as fixed
        with tempfile.TemporaryDirectory() as tmp:
            _, data, frame, _, _, summary = setup(Path(tmp))
            controls = [r for r in data['rows'] if r['variant_id'] == 'control']
            reference = fixed(frame, summary['generated_at_utc'], data['validation_evidence'],
                              data['execution_policy'], baseline_policy=trial.BASELINE_POLICY,
                              variants=trial.LEGACY_VARIANTS)
            self.assertEqual([r for r in data['rows'] if r['variant_id'] != trial.ADAPTIVE_ID], reference)
            # Fixed probabilities and EVs are never changed by adaptive ranking.
            for row, control in zip([r for r in data['rows'] if r['variant_id'] == trial.ADAPTIVE_ID], controls):
                for field in ('predicted_probability', 'raw_dc_probability', 'rank_probability',
                              'offered_decimal_odds', 'conservative_estimated_ev'):
                    self.assertEqual(row[field], control[field])
            candidates = [dict(controls[0], market='Home win', decision='NOT_SELECTED',
                probability_percentile=.6, ev_percentile=.95, **self.evidence()),
                dict(controls[0], market='Double Chance 1X', decision='NOT_SELECTED',
                probability_percentile=.95, ev_percentile=.4, **self.evidence())]
            candidates[0]['market_probability'] = .4
            ranked = trial.adaptive_rows(candidates, trial.BASELINE_POLICY)
            self.assertEqual([r['market'] for r in ranked if r['decision'] in trial.SELECTED], ['Double Chance 1X'])
