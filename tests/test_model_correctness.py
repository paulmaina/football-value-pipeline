"""Numerical integrity, training cache identity and archived experiment bindings."""
import copy
import math
from pathlib import Path
import tempfile
from unittest.mock import patch

import numpy as np
import pandas as pd

from offline_test_case import OfflineQuotePolicyTestCase
from score_probability import score_grid, valid_matrix, MAX_OMITTED_MASS, SCORE_ENGINE_VERSION
from football_value_pipeline_v2_standalone import DixonColesModel, FootballValuePipelineV2, reweight_matrix_to_1x2
from goal_market_validation import (training_fingerprint, validation_code_fingerprint,
    validation_cache_matches, evaluate_market_history, VALIDATOR_VERSION)
from historical_benchmark import adjusted_matrix, goals
from test_conservative_bet_filter import NOW


def history():
    rng = np.random.default_rng(12)
    teams = ['A', 'B', 'C', 'D']
    rows = []
    for day in pd.date_range('2024-01-01', periods=80):
        home, away = rng.choice(teams, 2, replace=False)
        rows.append(dict(Date=day, HomeTeam=home, AwayTeam=away,
                         FTHG=int(rng.poisson(1.5)), FTAG=int(rng.poisson(1.1)), B365H=2.1))
    return pd.DataFrame(rows)


class ModelCorrectnessTests(OfflineQuotePolicyTestCase):
    def test_unseen_low_score_correction_cannot_publish_negative_cells(self):
        model = DixonColesModel()
        model.teams = ['A', 'B']; model.team_to_idx = {'A': 0, 'B': 1}
        model.attack = np.array([1., -1.]); model.weakness = np.zeros(2)
        model.base = math.log(2); model.home_adv = 0.; model.rho = -.2
        with self.assertRaisesRegex(RuntimeError, 'low-score correction'):
            model.score_matrix('A', 'B')
        for bad in (np.array([[1.1, -.1]]), np.array([[float('nan')]]), np.zeros((2, 2)), [], [1.]):
            with self.subTest(matrix=str(bad)), self.assertRaises(ValueError):
                reweight_matrix_to_1x2(bad, [.5, .2, .3])
        for target in ([0, 0, 0], [float('nan'), .2, .3], [-.1, .5, .6]):
            with self.assertRaises(ValueError):
                reweight_matrix_to_1x2(np.ones((3, 3))/9, target)

    def test_adaptive_tail_matches_large_reference_for_actual_ucl_parameters(self):
        lam, mu, rho = 6.10255974479763, 1.3157396862942141, .05
        matrix, meta = score_grid(lam, mu, rho, 10)
        large = adjusted_matrix(lam, mu, rho, 100)
        old = adjusted_matrix(lam, mu, rho, 10)
        self.assertGreater(matrix.shape[0], 11)
        self.assertEqual(meta['score_engine_version'], SCORE_ENGINE_VERSION)
        self.assertLessEqual(meta['score_grid_omitted_mass'], MAX_OMITTED_MASS)
        self.assertGreater(abs(goals(old)['under_3_5']-goals(large)['under_3_5']), .003)
        for key, value in goals(large).items():
            self.assertAlmostEqual(goals(matrix)[key], value, places=9)
        np.testing.assert_allclose(list(DixonColesModel.one_x_two(matrix).values()),
                                   list(DixonColesModel.one_x_two(large).values()), atol=1e-10, rtol=0)
        self.assertGreaterEqual(matrix.min(), 0)
        self.assertAlmostEqual(matrix.sum(), 1.)
        stable, info = score_grid(.2, .3, -.05, 10)
        self.assertEqual(stable.shape, (11, 11))
        np.testing.assert_array_equal(stable, adjusted_matrix(.2, .3, -.05, 10))

    def test_unsafe_parameters_and_grid_capacity_fail_closed(self):
        for args in ((float('nan'), 1, 0), (0, 1, 0), (1, 1, float('inf')),
                     (6, 1, -.2), (5, 5, .05), (1000, 1, 0)):
            with self.subTest(parameters=args), self.assertRaises(ValueError):
                score_grid(*args)
        for minimum in (True, 3, 1.2, 101):
            with self.assertRaises(ValueError):
                score_grid(1, 1, 0, minimum)
        for bad in (np.array([[float('inf')]]), np.ones((1, 1, 1))):
            with self.assertRaises(ValueError):
                valid_matrix(bad)

    def test_prediction_and_experiment_inputs_record_the_actual_expanded_grid(self):
        model = DixonColesModel(max_goals=10)
        lam, mu = 6.10255974479763, 1.3157396862942141
        attack = .5*math.log(lam/mu)
        model.teams = ['A', 'B']; model.team_to_idx = {'A': 0, 'B': 1}
        model.attack = np.array([attack, -attack]); model.weakness = np.zeros(2)
        model.base = .5*math.log(lam*mu); model.home_adv = 0.; model.rho = .05
        pipe = FootballValuePipelineV2.__new__(FootballValuePipelineV2)
        pipe.market_weight = .5; pipe.devig_method = 'power'
        pipe._benchmark_trial_enabled = True; pipe._benchmark_score_matrices = {}; pipe._totals_shadow_inputs = {}
        row = pd.Series({'HomeTeam': 'A', 'AwayTeam': 'B', 'kickoff_utc': NOW.isoformat(),
                         'live_ref_home_odds': 1.2, 'live_ref_draw_odds': 5., 'live_ref_away_odds': 10.})
        prediction, _ = pipe._predict_row(model, row)
        key = ('A', 'B', NOW.isoformat())
        matrix = pipe._benchmark_score_matrices[key]; inputs = pipe._totals_shadow_inputs[key]
        self.assertGreater(inputs['max_goals'], 10)
        self.assertEqual(inputs['max_goals'], matrix.shape[0]-1)
        self.assertEqual(prediction['score_grid_max_goals'], inputs['max_goals'])
        self.assertEqual(inputs['score_engine_version'], SCORE_ENGINE_VERSION)
        expected = reweight_matrix_to_1x2(adjusted_matrix(lam, mu, .05, inputs['max_goals']),
                                         [prediction['p_'+k] for k in ('home', 'draw', 'away')])
        np.testing.assert_allclose(matrix, expected, atol=1e-12, rtol=0)

    def test_training_hash_tracks_scores_identities_and_opening_prices(self):
        frame = history(); original = frame.copy(deep=True)
        checksum = training_fingerprint(frame)
        self.assertEqual(checksum, training_fingerprint(frame.iloc[::-1, ::-1]))
        for field, value in (('FTHG', 9), ('HomeTeam', 'Changed'), ('B365H', 2.2)):
            changed = frame.copy(); changed.loc[0, field] = value
            self.assertNotEqual(checksum, training_fingerprint(changed), field)
        pd.testing.assert_frame_equal(frame, original)
        baseline = validation_code_fingerprint(); read = Path.read_bytes
        with patch.object(Path, 'read_bytes', lambda p: read(p)+(b'changed' if p.name == 'score_probability.py' else b'')):
            self.assertNotEqual(baseline, validation_code_fingerprint())

    def test_outcome_correction_invalidates_previously_reliable_cached_market(self):
        frame = history()
        forecast = pd.DataFrame({'date': pd.date_range('2024-01-01', periods=160),
                                'p_home': [.8]*160, 'actual_home': [int(i%5 != 0) for i in range(160)]})
        cached = evaluate_market_history(forecast, 'Premier League')
        config = {'validator_version': VALIDATOR_VERSION, 'training_matches': len(frame),
                  'training_end': str(frame.Date.max()), 'training_sha256': training_fingerprint(frame),
                  'validation_code_sha256': validation_code_fingerprint()}
        cached['config'] = config.copy()
        self.assertEqual(cached['markets']['home']['status'], 'RELIABLE_FOR_RANKING')
        self.assertTrue(validation_cache_matches(cached, config))
        corrected = forecast.copy()
        indices = corrected.index[(corrected.index >= 120) & corrected.actual_home.eq(1)][:10]
        corrected.loc[indices, 'actual_home'] = 0
        self.assertEqual(evaluate_market_history(corrected, 'Premier League')['markets']['home']['status'], 'UNRELIABLE_AUDIT')
        frame.loc[0, 'FTHG'] += 1
        changed = dict(config, training_sha256=training_fingerprint(frame))
        self.assertFalse(validation_cache_matches(cached, changed))
        for key in ('training_sha256', 'validation_code_sha256'):
            for value in (None, 'legacy', 'x'*64):
                self.assertFalse(validation_cache_matches(cached, dict(config, **{key: value})))
        self.assertFalse(validation_cache_matches(cached, None))

    def test_production_and_validation_use_the_same_private_history(self):
        frame = history()
        with tempfile.TemporaryDirectory() as tmp:
            pipe = FootballValuePipelineV2(cache_dir=tmp, live_odds=False)
            with patch.object(pipe, '_history_for_league', return_value=frame), patch.object(
                    pipe, '_current_fixtures', return_value=pd.DataFrame()):
                _, diagnostics, _ = pipe.run_league('EPL', now=NOW)
            original_hash = training_fingerprint(frame)
            self.assertEqual(diagnostics['training_sha256'], original_hash)
            frame.loc[0, 'FTHG'] += 1
            self.assertEqual(training_fingerprint(pipe._validation_history), original_hash)
            with patch.object(pipe, '_history_for_league', side_effect=AssertionError('Do not redownload validation history')):
                result, _, _, _ = pipe.backtest_league('EPL', min_train=30,
                    test_start='2024-02-15', history_override=pipe._validation_history, now=NOW)
            self.assertFalse(result.empty)

    def test_adaptive_totals_capture_reconstructs_actual_grid_and_preserves_legacy(self):
        import totals_anchor_experiment as trial
        from test_totals_anchor_experiment import sample, NOW
        from benchmark_forward_experiment import simplex
        from performance_tracking import capture, snapshots, fixture_key, write_json
        row, legacy, inputs = sample()
        registry, _ = trial.registry()
        before = trial.decision(row, legacy, inputs, NOW, registry)
        self.assertEqual(before['status'], 'available')
        original_inputs = copy.deepcopy(inputs)
        raw, meta = score_grid(inputs['lambda_home'], inputs['lambda_away'], inputs['rho'], 10)
        matrix = reweight_matrix_to_1x2(raw, simplex(row, 'p_'))
        for key, value in goals(matrix).items():
            row['p_'+key] = value
        inputs = dict(inputs, max_goals=matrix.shape[0]-1, score_engine_version=meta['score_engine_version'])
        self.assertEqual(trial.decision(row, matrix, inputs, NOW, registry)['status'], 'available')
        self.assertEqual(trial.decision(row, matrix, dict(inputs, score_engine_version='unknown'), NOW, registry)['status'], 'unavailable')
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); output = root/'raw'; output.mkdir()
            predictions = pd.DataFrame([row]); predictions.to_csv(output/'all_leagues_predictions.csv', index=False)
            pd.DataFrame(columns=['decision']).to_csv(output/'conservative_bet_shortlist.csv', index=False)
            write_json(output/'conservative_bet_summary.json', {'generated_at_utc': NOW.isoformat()})
            key = fixture_key(row)
            data = trial.write_experiment(predictions, output, NOW.isoformat(), {key: matrix}, {key: inputs})
            self.assertIsNotNone(trial.capture_file(output, NOW.isoformat()))
            self.assertTrue(capture('e'*40, root=root, captured_at=NOW))
            self.assertEqual(trial.evaluate(root, snapshots(root), [], NOW)[0]['rejected_snapshot_commits'], [])
            trial.validate(data, NOW.isoformat(), [row])
        # Legacy decisions still use the original fixed-grid solver.
        old_row, old_matrix, _ = sample()
        self.assertEqual(before, trial.decision(old_row, old_matrix, original_inputs, NOW, registry))
