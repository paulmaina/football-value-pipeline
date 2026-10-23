import json
import math
import tempfile
import unittest
from pathlib import Path

import pandas as pd

import pipeline_service
import staking
from prediction_runs import publish_run
from test_staking import ah_row

GENERATED = '2026-10-22T15:07:55+00:00'


def publish(root: Path, with_stakes: bool) -> Path:
    raw = root / 'raw'
    raw.mkdir()
    staging = root / 'stage'
    staging.mkdir()
    pd.DataFrame([
        {'league': 'Bundesliga', 'home_team': 'Augsburg', 'away_team': 'Union Berlin', 'p_home': 0.4, 'elo_home_rating': float('nan')},
        {'league': 'Premier League', 'home_team': 'Aston Villa', 'away_team': 'Man City', 'p_home': 0.3, 'elo_home_rating': 1550.0},
    ]).to_csv(staging / 'all_leagues_predictions.csv', index=False)
    shortlist = pd.DataFrame([ah_row(), ah_row(fixture_id='f2', selection_tier='PROVISIONAL')])
    shortlist.to_csv(staging / 'conservative_bet_shortlist.csv', index=False)
    if with_stakes:
        staking.write_stake_recommendations(shortlist, staging)
    (staging / 'conservative_bet_summary.json').write_text(json.dumps(
        {'generated_at_utc': GENERATED, 'selection_policy_version': 'v-test', 'status': 'BELOW_TARGET'}))
    (staging / 'pipeline_run_metadata.json').write_text('{}')
    publish_run(staging, raw)
    return raw


class ServiceTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.root = Path(self.directory.name)

    def tearDown(self):
        self.directory.cleanup()

    def test_reads_only_the_validated_current_bundle(self):
        raw = publish(self.root, with_stakes=True)
        run = pipeline_service.current_run(raw)
        self.assertEqual((run['generated_at_utc'], run['selection_policy_version']), (GENERATED, 'v-test'))
        self.assertRegex(run['run_id'], '^[0-9a-f]{64}$')
        self.assertIn(staking.OUTPUT_FILE, run['files'])
        rows = pipeline_service.predictions(raw)
        self.assertIsNone(rows[0]['elo_home_rating'])  # NaN is JSON-safe None
        json.dumps(rows, allow_nan=False)
        self.assertEqual([r['home_team'] for r in pipeline_service.predictions(raw, league='EPL')], ['Aston Villa'])
        self.assertEqual(len(pipeline_service.predictions(raw, league='bundesliga')), 1)
        self.assertEqual(pipeline_service.predictions(raw, league='epl'), pipeline_service.predictions(raw, league='EPL'))
        self.assertEqual(len(pipeline_service.shortlist(raw, tier='strict')), 1)
        (raw / 'conservative_bet_shortlist.csv').write_text('tampered compatibility copy')
        self.assertEqual(len(pipeline_service.shortlist(raw)), 2)  # pointer-bound bundle wins

    def test_stake_plan_saved_or_recomputed(self):
        raw = publish(self.root, with_stakes=True)
        saved = pipeline_service.stake_plan(raw)
        self.assertEqual([r['staking_status'] for r in saved], ['STAKE_CAPPED', 'NO_STAKE_NOT_STRICT'])
        custom = pipeline_service.stake_plan(raw, bankroll=1000, max_fraction=0.01)
        self.assertAlmostEqual(custom[0]['stake_units'], 10.0)

    def test_older_runs_without_stake_file_and_missing_files(self):
        raw = publish(self.root, with_stakes=False)
        plan = pipeline_service.stake_plan(raw)
        self.assertAlmostEqual(plan[0]['stake_units'], 2.5)
        with self.assertRaises(FileNotFoundError):
            pipeline_service._read(raw, 'missing.csv')

    def test_price_fixture_exact_simulated_and_offered_odds(self):
        exact = pipeline_service.price_fixture(1.6, 1.1, -0.08, odds={'1x2:home': 2.1, 'asian_handicap:home:-0.5': 2.1})
        home = exact['markets']['1x2:home']
        self.assertAlmostEqual(home['expected_value'], home['win'] * 2.1 - 1)
        self.assertAlmostEqual(home['expected_value'], exact['markets']['asian_handicap:home:-0.5']['expected_value'])
        self.assertGreater(home['full_kelly_fraction'], 0)
        self.assertIn('total:over:2.5', exact['markets'])
        self.assertIsNone(exact['markets']['total:over:2.5']['expected_value'])
        json.dumps(exact, allow_nan=False)
        simulated = pipeline_service.price_fixture(1.6, 1.1, -0.08, n_simulations=2000, seed=3)
        self.assertEqual(simulated['model']['n_simulations'], 2000)
        self.assertIn('win_standard_error', simulated['markets']['btts:yes'])
        with self.assertRaises(KeyError):
            pipeline_service.price_fixture(1.6, 1.1, -0.08, odds={'1x2:winner': 2.0})

    def test_json_cleaning(self):
        import numpy as np
        cleaned = pipeline_service._clean({'a': np.float64('inf'), 'b': [np.int64(2), pd.NaT], 'c': (math.nan,)})
        self.assertEqual(cleaned, {'a': None, 'b': [2, None], 'c': [None]})


if __name__ == '__main__':
    unittest.main()
