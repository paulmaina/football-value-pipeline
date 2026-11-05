"""Full-grid export and offline comparison integrity regressions."""
import copy
import json
from pathlib import Path
import tempfile
from unittest.mock import patch

import numpy as np
import pandas as pd

from offline_test_case import OfflineQuotePolicyTestCase
from test_model_upgrades_v2 import toy_model, pipe, live_row
from test_historical_benchmark import config, history, ToyModel
from test_team_research_profit import researched
from test_price_edge_shortlist import NOW
import historical_benchmark as hb
import research_backtest as rb


IDENTITY = {'fixture_key': 'one', 'league': 'UCL', 'date': '2026-11-01', 'phase': 'audit'}


class GridExportTests(OfflineQuotePolicyTestCase):
    def test_export_is_the_final_blended_anchored_grid_and_round_trips_csv(self):
        p = pipe()
        p._benchmark_trial_enabled = True
        p._benchmark_score_matrices = {}
        row = live_row()
        pred, _ = p._predict_row(toy_model(), row)
        self.assertTrue(pred['market_blend_applied'])
        self.assertTrue(pred['totals_anchor_applied'])
        matrix = rb.matrix_value(pred['score_matrix_json'])
        saved = next(iter(p._benchmark_score_matrices.values()))
        np.testing.assert_array_equal(matrix, saved)
        h, a = np.indices(matrix.shape)
        self.assertAlmostEqual(matrix[h == a].sum(), pred['p_draw'])
        self.assertAlmostEqual(matrix[h+a >= 2].sum(), pred['p_over_1_5'])
        from asian_handicap import margins
        self.assertEqual(margins(matrix), pred['goal_margin_distribution'])
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp)/'predictions.csv'
            pd.DataFrame([pred]).to_csv(path, index=False)
            np.testing.assert_array_equal(rb.matrix_value(pd.read_csv(path).iloc[0].score_matrix_json), matrix)

    def test_diagnostic_export_does_not_change_published_probabilities(self):
        p = pipe()
        p.totals_anchor = False
        model, row = toy_model(), live_row()
        pred, _ = p._predict_row(model, row)
        raw, _ = model.score_matrix('A', 'B')
        from football_value_pipeline_v2_standalone import market_snapshot, reweight_matrix_to_1x2
        snapshot = market_snapshot(row, devig_method=p.devig_method)
        original = model.one_x_two(raw)
        target = (1-p.market_weight)*np.array([original[k] for k in ('home', 'draw', 'away')]) + p.market_weight*np.array([snapshot['market_p_'+k] for k in ('home', 'draw', 'away')])
        np.testing.assert_array_equal(rb.matrix_value(pred['score_matrix_json']), reweight_matrix_to_1x2(raw, target))


class ResearchComparisonTests(OfflineQuotePolicyTestCase):
    def test_missing_full_grid_never_uses_lambdas_or_top_scores(self):
        row = researched()
        with patch('requests.sessions.Session.request', side_effect=AssertionError('offline')):
            matrices, gaps = rb.archived_candidates(row, NOW)
        self.assertNotIn('A', matrices)
        self.assertIn('no reconstruction', gaps['A'])
        self.assertIn('C', matrices)
        for value in ('[[0.9]]', '[[1, -0.1], [0, 0.1]]', '[[0.5,0.5]]', None):
            with self.subTest(value=value), self.assertRaises((ValueError, TypeError)):
                rb.matrix_value(value)

    def test_future_research_and_pinnacle_quotes_fail_closed(self):
        row = researched()
        evidence = json.loads(row['team_research_json'])
        evidence['observed_at_utc'] = (NOW+pd.Timedelta(seconds=1)).isoformat()
        row['team_research_json'] = json.dumps(evidence)
        quotes = json.loads(row['price_edge_quotes'])
        for q in quotes:
            q['last_update_utc'] = (NOW+pd.Timedelta(seconds=1)).isoformat()
        row['price_edge_quotes'] = json.dumps(quotes)
        matrices, gaps = rb.archived_candidates(row, NOW)
        self.assertNotIn('C', matrices)
        self.assertIn('not observed', gaps['C'])
        self.assertNotIn('B', matrices)

    def test_quarter_line_log_loss_uses_half_win_as_its_own_category(self):
        matrix = np.zeros((3, 3))
        matrix[0, 1], matrix[1, 1], matrix[2, 0] = .2, .5, .3
        rows = rb.score_fixture(IDENTITY, {'A': matrix}, 1, 1)
        quarter = next(r for r in rows if r['market'] == 'AH +0.25')
        self.assertAlmostEqual(quarter['log_loss'], -np.log(.5))
        whole = next(r for r in rows if r['market'] == 'AH +0.00')
        self.assertAlmostEqual(whole['log_loss'], -np.log(.5))
        one_x_two = next(r for r in rows if r['market'] == '1X2')
        self.assertAlmostEqual(one_x_two['brier'], .2**2+.5**2+.3**2)

    def test_profit_bins_use_positive_net_return_not_push_or_half_win_below_cost(self):
        matrix = np.zeros((3, 3))
        matrix[0, 1], matrix[1, 1], matrix[2, 0] = .2, .5, .3
        offer = {'market': 'AH', 'side': 'home', 'line': .25, 'price': 1.2, 'stamp': NOW.isoformat()}
        out = rb.profit_observations(IDENTITY, {'A': matrix}, 1, 1, [offer], NOW, .11)
        self.assertAlmostEqual(out[0]['p_profit'], .3)
        self.assertEqual(out[0]['actual_profit'], 0)
        offer['stamp'] = (NOW+pd.Timedelta(seconds=1)).isoformat()
        self.assertFalse(rb.profit_observations(IDENTITY, {'A': matrix}, 1, 1, [offer], NOW, 0))

    def test_pairing_excludes_missing_baseline_and_preserves_weeks(self):
        rows = []
        for i in range(6):
            identity = dict(IDENTITY, fixture_key=str(i), date=f'2026-10-{1+7*i:02d}' if i < 4 else f'2026-11-{1+7*(i-4):02d}')
            rows += [dict(identity, candidate=c, market='AH', log_loss=value, brier=.2) for c, value in [('A', .6), ('C', .4)]]
        rows.append(dict(rows[-1], fixture_key='unpaired', log_loss=100))
        out = rb.paired_summary(rows, samples=100)['AH']['C']
        self.assertEqual(out['paired_fixtures'], 6)
        self.assertGreater(out['calendar_weeks'], 1)
        self.assertAlmostEqual(out['baseline_minus_candidate_log_loss'], .2)
        self.assertAlmostEqual(out['descriptive_95_interval'][0], .2)

    def test_future_rows_and_closing_odds_cannot_change_historical_candidates(self):
        cfg = config()
        cfg['model_upgrade_comparison'] = {'production_v2': {'market_weight': .7, 'totals_anchor': True}}
        data = history()
        origin = pd.Timestamp('2025-08-01')
        train = data.loc[data.Date < origin]
        model = ToyModel(480, .08, 10).fit(train, as_of=origin)
        model.one_x_two = __import__('football_value_pipeline_v2_standalone').DixonColesModel.one_x_two
        row = data.loc[data.Date >= origin].iloc[0].copy()
        first, gaps = rb.historical_candidates(row, train, origin, model, cfg)
        changed = data.copy()
        changed.loc[changed.Date >= origin, ['FTHG', 'FTAG', 'PSCH', 'PCAHH']] = 19
        changed_row = changed.loc[changed.Date >= origin].iloc[0]
        second, _ = rb.historical_candidates(changed_row, changed.loc[changed.Date < origin], origin, model, cfg)
        self.assertEqual(first.keys(), second.keys())
        for key in first:
            np.testing.assert_array_equal(first[key], second[key])
        self.assertTrue(all(stop <= pd.Timestamp(cfg['test_end_exclusive']) for _, stop in hb.fold_windows(cfg)))
        self.assertIn(pd.Timestamp(cfg['audit_start']), [origin for origin, _ in hb.fold_windows(cfg)])

    def test_empty_or_thin_evidence_never_promotes(self):
        result = rb.summarize([], [], {'UCL:missing_grid': 3}, {'mode': 'test'})
        self.assertIn('SHADOW_ONLY', result['promotion_status'])
        self.assertIsNone(result['roi'])
        self.assertEqual(result['coverage']['UCL:missing_grid'], 3)
        self.assertFalse(result['metrics'])

    def test_archive_cli_uses_latest_integrity_checked_snapshot_and_frozen_cost(self):
        from datetime import timedelta
        from test_performance_tracking import fixture, pick, final, T0
        from test_prediction_run_tracking import save_run
        from performance_tracking import capture, verified_record, write_json
        from team_research import prepare
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)/'football_output_v2'
            matrix = np.zeros((3, 3))
            matrix[1, 1], matrix[2, 0] = .6, .4
            for sha, cutoff in [('a'*40, T0), ('b'*40, T0+timedelta(hours=1))]:
                row = dict(fixture(), score_matrix_json=json.dumps(matrix.tolist()), lambda_home=1.2, lambda_away=.8)
                row['team_research_json'] = json.dumps(prepare(row, pd.Timestamp(cutoff)))
                row['price_edge_quotes'] = json.dumps([{'bookmaker': 'Pinnacle', 'market': 'h2h',
                    'prices': {'home': 1.2, 'draw': 4., 'away': 7.}, 'last_update_utc': cutoff.isoformat()}])
                save_run(root, cutoff, [row], [pick()])
                summary = root/'raw'/'conservative_bet_summary.json'
                data = json.loads(summary.read_text())
                data['quote_execution_policy'] = {'allowed_bookmakers': ['Pinnacle'], 'per_stake_cost_bps': 2100}
                write_json(summary, data)
                self.assertTrue(capture(sha, root=root, captured_at=cutoff))
            write_json(root/'performance'/'verified_results.json', {'PL:90002': verified_record('PL', final())})
            out = Path(tmp)/'comparison'
            with patch('requests.sessions.Session.request', side_effect=AssertionError('offline')):
                self.assertEqual(rb.main(['--mode', 'archives', '--root', str(root), '--output', str(out), '--source-commit', 'c'*40]), 0)
            report = json.loads((out/'results.json').read_text())
            self.assertEqual(report['coverage']['A:available'], 1)
            self.assertEqual(report['coverage']['C:available'], 1)
            self.assertIsNone(report['roi'])
            scores = pd.read_csv(out/'scores.csv')
            self.assertEqual(scores.fixture_key.nunique(), 1)
            reliability = pd.read_csv(out/'profit_observations.csv')
            home = reliability[(reliability.candidate == 'A') & (reliability.market == 'Home win')].iloc[0]
            self.assertEqual(home.p_profit, 0)  # 1.20 win cannot cover the frozen .21 cost.
            self.assertEqual(home.actual_profit, 0)

    def test_historical_runner_reuses_folds_without_live_research(self):
        class Model(ToyModel):
            def __init__(self, half_life_days, l2, max_goals, **kwargs):
                super().__init__(half_life_days, l2, max_goals)
            @staticmethod
            def one_x_two(matrix):
                h, a = np.indices(matrix.shape)
                return {'home': matrix[h > a].sum(), 'draw': matrix[h == a].sum(), 'away': matrix[h < a].sum()}
        cfg = config()
        cfg.update(test_start='2025-08-01', audit_start='2025-08-02', test_end_exclusive='2025-08-04')
        cfg['model_upgrade_comparison'] = json.loads(Path('historical_benchmark_config.json').read_text())['model_upgrade_comparison']
        with tempfile.TemporaryDirectory() as tmp:
            cache = Path(tmp)
            history().to_csv(cache/'2324_E0.csv', index=False)
            with patch('requests.sessions.Session.request', side_effect=AssertionError('offline')):
                rows, observations, coverage, metadata = rb.historical(cache, cfg, 'a'*40, Model)
            self.assertEqual(len(metadata['folds']), 2)
            self.assertEqual(len({r['fixture_key'] for r in rows}), 3)
            self.assertEqual(coverage['EPL:A:available'], 3)
            self.assertFalse(observations)
            self.assertEqual(metadata['mode'], 'historical_csv_proxy')
