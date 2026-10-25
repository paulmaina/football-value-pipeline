"""Regression coverage for adding markets to cached historical validation."""
from offline_test_case import OfflineQuotePolicyTestCase
import copy
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import pandas as pd

from goal_market_validation import (
    MARKETS, SUPPORTED_COMPETITIONS, VALIDATOR_VERSION,
    enrich_historical_goal_markets, evaluate_market_history, validation_cache_matches,
)
from football_value_pipeline_v2_standalone import main
from test_conservative_bet_filter import fixture


class ValidationCacheTests(OfflineQuotePolicyTestCase):
    def test_12_gets_real_historical_validation_in_every_competition(self):
        prediction = fixture()
        prediction.update(p_home=.4, p_draw=.2, p_away=.4,
                          raw_p_home=.4, raw_p_draw=.2, raw_p_away=.4)
        rows = [dict(enrich_historical_goal_markets(
                    {"FTHG": 1, "FTAG": int(i % 5 == 0)}, prediction),
                    date=date)
                for i, date in enumerate(pd.date_range("2025-01-01", periods=160))]
        for league in SUPPORTED_COMPETITIONS:
            result = evaluate_market_history(pd.DataFrame(rows), league)["markets"]["home_away"]
            self.assertEqual(result["status"], "RELIABLE_FOR_RANKING", league)
            self.assertEqual(result["development"]["n"], 120)
            self.assertEqual(result["audit"]["n"], 40)
            self.assertAlmostEqual(result["audit"]["observed_rate"], .8)
            self.assertAlmostEqual(result["audit"]["brier"], .16)
            self.assertEqual(result["high_confidence"]["75plus"]["status"], "PASSED")
            self.assertEqual(result["historical_betting"]["n_quotes"], 0)
            self.assertIsNone(result["historical_betting"]["roi_per_unit"])

    def test_version_configuration_and_market_coverage_are_required(self):
        config = {"validator_version": VALIDATOR_VERSION, "training_end": "2026-09-20",
                  "training_sha256": 'a'*64, "validation_code_sha256": 'b'*64}
        report = evaluate_market_history(pd.DataFrame(), "Premier League")
        report["config"] = config.copy()
        self.assertTrue(validation_cache_matches(report, config))
        old = copy.deepcopy(report)
        old["config"]["validator_version"] = 4
        self.assertFalse(validation_cache_matches(old, config))
        for key in MARKETS:
            incomplete = copy.deepcopy(report)
            del incomplete["markets"][key]
            self.assertFalse(validation_cache_matches(incomplete, config), key)
        for invalid in (None, [], {}, {"config": config, "markets": []}):
            self.assertFalse(validation_cache_matches(invalid, config))

    def test_cli_rebuilds_legacy_and_incomplete_reports_then_reuses_complete_cache(self):
        with tempfile.TemporaryDirectory() as directory:
            raw = Path(directory) / "raw"
            args = ["--leagues", "EPL", "--no-legacy-comparison", "--out-dir", str(raw)]
            frame = pd.DataFrame([fixture()])
            with patch(
                "football_value_pipeline_v2_standalone.FootballValuePipelineV2.run_league",
                return_value=(frame, {"training_end": "2026-09-20",
                                     "training_matches": 1000, "training_sha256": 'a'*64}, {}),
            ), patch(
                "football_value_pipeline_v2_standalone.FootballValuePipelineV2.backtest_league",
                return_value=(pd.DataFrame(), pd.DataFrame(), {}, pd.DataFrame()),
            ) as backtest:
                self.assertEqual(main(args), 0)
                path = raw / "EPL_goal_market_validation.json"
                fresh = json.loads(path.read_text())
                self.assertIn("home_away", fresh["markets"])
                self.assertEqual(backtest.call_count, 1)

                # Reproduce the actual pre-DC12 cache: same model and training data.
                legacy = copy.deepcopy(fresh)
                legacy["config"]["validator_version"] = 4
                del legacy["markets"]["home_away"]
                path.write_text(json.dumps(legacy))
                self.assertEqual(main(args), 0)
                self.assertEqual(backtest.call_count, 2)
                rebuilt = json.loads(path.read_text())
                self.assertIn("home_away", rebuilt["markets"])
                self.assertEqual(rebuilt["config"]["validator_version"], VALIDATOR_VERSION)

                # A missing market must also invalidate a current-version report.
                del rebuilt["markets"]["home_away"]
                path.write_text(json.dumps(rebuilt))
                self.assertEqual(main(args), 0)
                self.assertEqual(backtest.call_count, 3)
                self.assertEqual(main(args), 0)
                self.assertEqual(backtest.call_count, 3)
