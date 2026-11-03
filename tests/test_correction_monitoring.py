"""v28 correction monitoring: fixed quintiles, forward-only records, hand-worked grading and the review flag."""
from datetime import timedelta
import json
import math
from pathlib import Path
import tempfile
import unittest

import numpy as np
import pandas as pd

from offline_test_case import OfflineQuotePolicyTestCase
import narrow_margin as nm
import price_edge_cagey_shortlist as v28
import price_edge_tracking as tracking
from performance_tracking import capture, snapshots, verified_record, write_csv
from test_performance_tracking import KICK, T0, final, fixture
from test_prediction_run_tracking import save_run


def record(generated=T0, **changes):
    """A usable monitoring record for the shared test fixture (Man City v Everton)."""
    base = {c: None for c in v28.MONITOR_COLUMNS}
    base.update({k: fixture()[k] for k in ('league', 'home_team', 'away_team', 'fixture_id', 'kickoff_utc')},
                monitoring_version=v28.MONITOR_VERSION, generated_at_utc=generated.isoformat(),
                model_version=nm.PRODUCTION_VERSION, quintile_model_sha256='x', status='USABLE', exclusion_reason='',
                fit='B', latest_input_quote_utc=(generated - timedelta(minutes=5)).isoformat(),
                corrected_p2=0.3, corrected_p3=0.1, uncorrected_p2=0.4, uncorrected_p3=0.2,
                corrected_cagey_quintile='Q2')
    for column in v28.MONITOR_PRICE_COLUMNS:
        if column.endswith('_fair_odds'):
            base[column] = 2.0
    base.update(changes)
    return base


def result(h, a):
    item = final(h=h, a=a)
    item['utcDate'] = KICK.isoformat()
    return verified_record('PL', item)


class QuintileTests(OfflineQuotePolicyTestCase):
    def test_production_boundaries_are_bound_to_the_model(self):
        model = nm.production_model()
        data = nm.load_quintiles(model)
        self.assertEqual(data['model_version'], nm.PRODUCTION_VERSION)
        self.assertEqual(data['training_fingerprint'], model['training_fingerprint'])
        self.assertEqual(data['boundaries'][0], model['training_cagey_p20'])
        with self.assertRaisesRegex(ValueError, 'different model'):
            nm.load_quintiles({**model, 'training_cagey_p20': 0.5})

    def test_labels_at_the_boundaries(self):
        bounds = [0.2, 0.3, 0.4, 0.5]
        self.assertEqual([nm.quintile_label(s, bounds) for s in (0.1, 0.2, 0.2000001, 0.3, 0.45, 0.5, 0.9)],
                         ['Q1 cagiest', 'Q1 cagiest', 'Q2', 'Q2', 'Q4', 'Q4', 'Q5 most open'])

    def test_boundaries_require_the_training_rows_and_persist_once(self):
        rng = np.random.default_rng(0)
        frame = pd.DataFrame({'date': pd.date_range('2023-08-01', periods=40, freq='7D'),
                              'matrix_p2': rng.uniform(0.25, 0.5, 40), 'matrix_p3': rng.uniform(0.05, 0.2, 40),
                              'p_over_2_5': rng.uniform(0.4, 0.6, 40), 'p_home': 0.4, 'p_away': 0.3,
                              'p_draw': 0.3, 'abs_margin': rng.integers(0, 4, 40), 'fit': 'B',
                              'Division': 'E0', 'HomeTeam': [f'H{i}' for i in range(40)], 'AwayTeam': 'A',
                              'FTHG': 1, 'FTAG': 0})
        frame['Date'] = frame['date']
        model = nm.finalise(nm.train(frame, version='t', until=pd.Timestamp('2024-03-01')), frame,
                            pd.Timestamp('2024-03-01'))
        data = nm.quintile_boundaries(frame, model)
        self.assertEqual(data['boundaries'][0], model['training_cagey_p20'])
        self.assertEqual(data['boundaries'], sorted(data['boundaries']))
        with self.assertRaisesRegex(ValueError, 'recorded training data'):
            nm.quintile_boundaries(frame.iloc[1:], model)
        with tempfile.TemporaryDirectory() as tmp:
            nm.save_quintiles(data, Path(tmp))
            nm.save_quintiles(data, Path(tmp))  # identical content may be rewritten
            with self.assertRaisesRegex(ValueError, 'already exists'):
                nm.save_quintiles({**data, 'boundaries': [0.1, 0.2, 0.3, 0.4]}, Path(tmp))


class RecordTests(OfflineQuotePolicyTestCase):
    def test_every_fixture_gets_one_record_and_selection_is_unchanged(self):
        from test_price_edge_cagey_shortlist import cagey_row, run
        from test_price_edge_shortlist import offer, row
        rows = [cagey_row(offers=[offer('away', 1.5, 1.20)]), row(home='No Totals FC', quotes=[])]
        monitor = []
        with_monitor = run(*rows, monitor=monitor)
        without = run(*rows)
        self.assertTrue(with_monitor[0].equals(without[0]))
        self.assertTrue(with_monitor[1].equals(without[1]))
        self.assertEqual([r['home_team'] for r in monitor], ['Cagey FC', 'No Totals FC'])
        usable, unusable = monitor
        self.assertEqual((usable['status'], unusable['status']), ('USABLE', 'UNUSABLE'))
        self.assertIn('no usable market-implied fit', unusable['exclusion_reason'])
        self.assertIsNone(unusable['corrected_p2'])
        # The record holds this run's own correction and both fair prices.
        context = v28.corrected_context(*_fit(rows[0]))
        self.assertAlmostEqual(usable['corrected_p2'], context['score'])
        self.assertAlmostEqual(usable['uncorrected_p2'], nm.margin_tail(context['margins'], context['uncorrected_probs'], 2))
        self.assertLess(usable['corrected_p2'], usable['uncorrected_p2'])
        self.assertLess(usable['away_plus_1_5_corrected_fair_odds'], usable['away_plus_1_5_uncorrected_fair_odds'])
        self.assertEqual(usable['away_plus_1_5_onexbet_odds'], 1.20)
        self.assertIsNone(usable['home_plus_1_5_onexbet_odds'])  # not offered: blank, never invented
        self.assertEqual(usable['corrected_cagey_quintile'],
                         nm.quintile_label(usable['corrected_p2'], nm.load_quintiles(nm.production_model())['boundaries']))
        self.assertLessEqual(pd.Timestamp(usable['latest_input_quote_utc']), pd.Timestamp(usable['generated_at_utc']))


def _fit(data):
    import price_edge_shortlist as v27
    from test_price_edge_shortlist import NOW
    pin = v27.pinnacle_quotes(data)
    fit, info = v27.market_fit(pin, NOW)
    return pin, fit, info, nm.production_model()


class ArchiveTests(OfflineQuotePolicyTestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.archive = []

    def snapshot(self, sha, captured, rows, generated=None):
        generated = generated or captured
        directory = self.root / 'performance' / 'snapshots' / sha[:16]
        directory.mkdir(parents=True)
        write_csv(directory / v28.MONITOR_FILE, rows, v28.MONITOR_COLUMNS)
        self.archive.append(({'git_commit_sha': sha, 'captured_at_utc': captured.isoformat(),
                              'generated_at_utc': generated.isoformat(), 'sha256': {v28.MONITOR_FILE: '0' * 64}},
                             [], []))

    def test_first_eligible_capture_per_fixture_with_reasons_for_the_rest(self):
        other = {'home_team': 'Chelsea FC', 'away_team': 'Fulham FC', 'fixture_id': 'event2'}
        late = KICK - timedelta(minutes=10)
        self.snapshot('a' * 40, T0, [record(T0, status='UNUSABLE', exclusion_reason='no usable fit'),
                                     record(T0, **other, corrected_p2=0.25)])
        self.snapshot('b' * 40, T0 + timedelta(hours=1), [record(T0 + timedelta(hours=1), corrected_p2=0.33),
                                                          record(T0 + timedelta(hours=1), **other, corrected_p2=0.5)])
        self.snapshot('c' * 40, late, [record(late, corrected_p2=0.9)])
        rows = {r['home_team']: r for r in tracking.first_monitoring_records(self.root, self.archive)}
        self.assertEqual(len(rows), 2)  # one record per fixture
        # City: first capture unusable, second eligible, late third ignored.
        self.assertEqual((rows['Manchester City FC']['snapshot_commit'], float(rows['Manchester City FC']['corrected_p2'])),
                         ('b' * 40, 0.33))
        self.assertEqual(float(rows['Chelsea FC']['corrected_p2']), 0.25)  # first eligible, not the latest

    def test_records_never_acquire_forward_status_retroactively(self):
        after = KICK + timedelta(hours=3)
        cases = {
            'captured after kickoff': ('a' * 40, after, record(T0), T0),
            'regenerated label': ('b' * 40, T0, record(T0 - timedelta(days=1)), T0),
            'input after generation': ('c' * 40, T0, record(T0, latest_input_quote_utc=(T0 + timedelta(minutes=1)).isoformat()), T0),
            'late capture': ('d' * 40, KICK - timedelta(minutes=19), record(KICK - timedelta(minutes=19)), None),
        }
        expected = {'captured after kickoff': 'captured less than 20 minutes before kickoff',
                    'regenerated label': 'record not bound to its snapshot generation',
                    'input after generation': 'input quote not observed before generation',
                    'late capture': 'captured less than 20 minutes before kickoff'}
        for name, (sha, captured, row, generated) in cases.items():
            with self.subTest(name):
                self.setUp()
                self.snapshot(sha, captured, [row], generated)
                [result_row] = tracking.first_monitoring_records(self.root, self.archive)
                self.assertEqual(result_row['exclusion_reason'], expected[name])
                graded = tracking.grade_monitoring([result_row], [result(2, 0)], KICK + timedelta(days=1))
                self.assertEqual(graded.state.tolist(), ['EXCLUDED'])

    def test_unrecorded_or_missing_files_are_ignored(self):
        self.snapshot('a' * 40, T0, [record(T0)])
        self.archive[0][0]['sha256'] = {}
        self.assertEqual(tracking.first_monitoring_records(self.root, self.archive), [])


class GradingTests(OfflineQuotePolicyTestCase):
    def graded(self, h, a, **changes):
        row = {**record(**changes), 'fixture_key': 'k', 'snapshot_captured_utc': T0.isoformat(), 'exclusion_reason': ''}
        return tracking.grade_monitoring([row], [result(h, a)], KICK + timedelta(days=1)).iloc[0]

    def test_margin_outcomes_and_log_loss_by_hand(self):
        g = self.graded(2, 0)  # |margin| = 2: 2+ yes, 3+ no
        self.assertEqual((g.state, g.final_score, g.abs_margin), ('GRADED', '2-0', 2))
        self.assertAlmostEqual(g.log_loss_2plus_corrected, -math.log(0.3))
        self.assertAlmostEqual(g.log_loss_2plus_uncorrected, -math.log(0.4))
        self.assertAlmostEqual(g.log_loss_gain_2plus, math.log(0.3) - math.log(0.4))  # -0.2877: correction worse
        self.assertAlmostEqual(g.log_loss_gain_3plus, -math.log(0.8) + math.log(0.9))  # +0.1178: correction better

    def test_ah_settlement_at_fair_prices_by_hand(self):
        price = {f'{k}_corrected_fair_odds': 1.2 for k in ('home_plus_1', 'home_plus_1_25', 'home_plus_1_5',
                                                           'home_plus_1_75', 'home_plus_2', 'away_plus_1')}
        lose_by_one = self.graded(0, 1, **price)
        self.assertEqual(lose_by_one.home_plus_1_return_corrected, 0)                     # push
        self.assertAlmostEqual(lose_by_one.home_plus_1_25_return_corrected, 0.1)          # half push, half win
        self.assertAlmostEqual(lose_by_one.home_plus_1_5_return_corrected, 0.2)           # win
        self.assertAlmostEqual(lose_by_one.away_plus_1_return_corrected, 0.2)             # away won outright
        lose_by_two = self.graded(0, 2, **price)
        self.assertEqual(lose_by_two.home_plus_1_5_return_corrected, -1)                  # loss
        self.assertEqual(lose_by_two.home_plus_1_75_return_corrected, -0.5)               # half push, half loss
        self.assertEqual(lose_by_two.home_plus_2_return_corrected, 0)                     # push
        self.assertEqual(lose_by_two.home_plus_1_return_uncorrected, -1)                  # 2.0 fair, lost

    def test_pending_until_a_verified_result(self):
        row = {**record(), 'fixture_key': 'k', 'snapshot_captured_utc': T0.isoformat(), 'exclusion_reason': ''}
        before = tracking.grade_monitoring([row], [result(2, 0)], KICK + timedelta(hours=1))
        unverified = tracking.grade_monitoring([row], [], KICK + timedelta(days=1))
        self.assertEqual((before.state.tolist(), unverified.state.tolist()), (['PENDING'], ['PENDING']))


def summary_frame(n, gain):
    """n graded fixtures, one per gameweek block of 4, with a constant paired 2+ gain."""
    return pd.DataFrame({'state': 'GRADED', 'snapshot_captured_utc': T0.isoformat(), 'model_version': 'm',
                         'exclusion_reason': '', 'gameweek': [f'W{i // 4}' for i in range(n)],
                         'corrected_cagey_quintile': 'Q1 cagiest', 'abs_margin': 1,
                         'corrected_p2': 0.3, 'uncorrected_p2': 0.4, 'corrected_p3': 0.1, 'uncorrected_p3': 0.2,
                         'log_loss_2plus_corrected': 0.5, 'log_loss_2plus_uncorrected': 0.5 + gain,
                         'log_loss_gain_2plus': gain + np.linspace(-1e-4, 1e-4, n),
                         'log_loss_3plus_corrected': 0.2, 'log_loss_3plus_uncorrected': 0.2, 'log_loss_gain_3plus': 0.0,
                         'home_plus_1_return_corrected': 0.0, 'home_plus_1_return_uncorrected': 0.1})


class FlagTests(OfflineQuotePolicyTestCase):
    def test_correction_review_needs_200_fixtures_and_an_interval_below_zero(self):
        self.assertTrue(tracking.monitoring_summary(summary_frame(200, -0.01))['correction_review'])
        self.assertFalse(tracking.monitoring_summary(summary_frame(199, -0.01))['correction_review'])
        self.assertFalse(tracking.monitoring_summary(summary_frame(400, 0.01))['correction_review'])
        summary = tracking.monitoring_summary(summary_frame(200, -0.01))
        self.assertEqual(summary['fixtures'], {'eligible': 200, 'pending': 0, 'graded': 200, 'excluded': 0})
        expected = {'n': 200, '2plus_actual': 0.0, '2plus_corrected': 0.3, '2plus_uncorrected': 0.4,
                    '3plus_actual': 0.0, '3plus_corrected': 0.1, '3plus_uncorrected': 0.2}
        for key, value in expected.items():
            self.assertAlmostEqual(summary['by_quintile']['Q1 cagiest'][key], value)
        self.assertAlmostEqual(summary['fair_price_returns']['uncorrected']['mean'], 0.1)
        text = '\n'.join(tracking.monitoring_report(summary))
        self.assertIn('**CORRECTION REVIEW**', text)
        self.assertIn('NOT achievable bookmaker ROI', text)
        self.assertNotIn('CORRECTION REVIEW**', '\n'.join(tracking.monitoring_report(
            tracking.monitoring_summary(summary_frame(199, -0.01)))))

    def test_empty_monitoring_reports_its_start_and_counts(self):
        summary = tracking.monitoring_summary(pd.DataFrame(columns=['state']))
        self.assertEqual((summary['monitoring_start_utc'], summary['correction_review']), (None, False))
        self.assertIn('started not yet', '\n'.join(tracking.monitoring_report(summary)))


class EndToEndTests(OfflineQuotePolicyTestCase):
    def test_capture_and_review_write_the_section(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            save_run(root, T0, [fixture()], [])
            write_csv(root / 'raw' / v28.MONITOR_FILE, [record(T0)], v28.MONITOR_COLUMNS)
            capture('a' * 40, root=root, captured_at=T0)
            archive = snapshots(root)
            self.assertIn(v28.MONITOR_FILE, archive[0][0]['sha256'])
            summary = tracking.review(root, archive, [result(3, 0)], KICK + timedelta(days=1))
            monitoring = summary['correction_monitoring']
            self.assertEqual(monitoring['fixtures']['graded'], 1)
            self.assertEqual(pd.Timestamp(monitoring['monitoring_start_utc']), pd.Timestamp(T0))
            self.assertEqual(monitoring['by_quintile']['Q2']['3plus_actual'], 1.0)
            report = (root / tracking.OUTPUT_DIR / 'report.md').read_text(encoding='utf-8')
            self.assertIn('## Correction monitoring', report)
            graded = pd.read_csv(root / tracking.OUTPUT_DIR / 'correction_monitoring.csv')
            self.assertEqual(graded.state.tolist(), ['GRADED'])

    def test_records_from_another_generation_are_not_captured(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            save_run(root, T0, [fixture()], [])
            write_csv(root / 'raw' / v28.MONITOR_FILE, [record(T0 - timedelta(hours=1))], v28.MONITOR_COLUMNS)
            capture('a' * 40, root=root, captured_at=T0)
            self.assertNotIn(v28.MONITOR_FILE, snapshots(root)[0][0]['sha256'])


if __name__ == '__main__':
    unittest.main()
