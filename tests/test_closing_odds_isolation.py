"""Closing odds never stand in for missing opening odds in a prediction path.

Closing columns (PSC*, PC>2.5 and the other C-suffixed books) are known only
at kickoff. They may feed evaluation and explicitly labelled oracle variants,
never the market blend, the totals anchor or the reported market prices.
"""
from offline_test_case import OfflineQuotePolicyTestCase
from datetime import datetime, timezone
import json
from pathlib import Path
import unittest

import numpy as np
import pandas as pd

import historical_benchmark as hb
from football_value_pipeline_v2_standalone import market_snapshot, pinnacle_ou25_reference
from tests.test_model_upgrades_v1 import pipe, toy_model


CLOSING = {
    "PSCH": 2.10, "PSCD": 3.40, "PSCA": 3.70, "B365CH": 2.05, "B365CD": 3.30, "B365CA": 3.60,
    "AvgCH": 2.02, "AvgCD": 3.30, "AvgCA": 3.55, "MaxCH": 2.20, "MaxCD": 3.60, "MaxCA": 3.90,
    "PC>2.5": 1.90, "PC<2.5": 2.00, "B365C>2.5": 1.85, "B365C<2.5": 1.95,
    "AvgC>2.5": 1.84, "AvgC<2.5": 1.96, "MaxC>2.5": 1.98, "MaxC<2.5": 2.05,
}
OPENING = {"PSH": 2.30, "PSD": 3.30, "PSA": 3.30, "P>2.5": 2.05, "P<2.5": 1.85}


def historical_row(**odds):
    return pd.Series({"HomeTeam": "A", "AwayTeam": "B", "Date": pd.Timestamp("2026-10-01"), **odds})


class PredictionPathTests(OfflineQuotePolicyTestCase):
    def test_market_snapshot_ignores_closing_only_rows(self):
        snapshot = market_snapshot(historical_row(**CLOSING))
        for field in ("market_p_home", "market_p_draw", "market_p_away", "market_p_over_2_5",
                      "market_p_under_2_5", "market_home_odds", "market_draw_odds", "market_away_odds",
                      "market_over_2_5_odds", "market_under_2_5_odds", "market_reference_home_odds",
                      "market_reference_over_2_5_odds"):
            self.assertIsNone(snapshot[field], field)
        self.assertIsNone(snapshot["market_source_1x2"])
        self.assertIsNone(snapshot["market_source_ou25"])

    def test_closing_columns_never_change_an_opening_snapshot(self):
        self.assertEqual(market_snapshot(historical_row(**OPENING, **CLOSING)),
                         market_snapshot(historical_row(**OPENING)))

    def test_live_rows_never_revive_closing_columns(self):
        snapshot = market_snapshot(historical_row(odds_source="The Odds API", **CLOSING))
        self.assertIsNone(snapshot["market_p_home"])
        self.assertIsNone(snapshot["market_p_over_2_5"])

    def test_totals_anchor_ignores_closing_totals(self):
        self.assertEqual(pinnacle_ou25_reference(historical_row(**CLOSING), datetime.now(timezone.utc)),
                         (None, "NOT_ANCHORED_NO_PINNACLE"))

    def test_predict_row_with_closing_only_equals_no_odds(self):
        with_closing, _ = pipe()._predict_row(toy_model(), historical_row(**CLOSING))
        without, _ = pipe()._predict_row(toy_model(), historical_row())
        self.assertFalse(with_closing["market_blend_applied"])
        self.assertFalse(with_closing["totals_anchor_applied"])
        for field in ("p_home", "p_draw", "p_away", "p_over_2_5", "p_under_3_5", "p_btts_yes"):
            self.assertEqual(with_closing[field], without[field], field)


class BenchmarkPathTests(OfflineQuotePolicyTestCase):
    ORACLE_VARIANTS = {"pinnacle_closing_only", "totals_closing_oracle"}

    def test_benchmark_uses_closing_only_in_labelled_oracle_variants(self):
        rng = np.random.default_rng(3)
        teams = [f"T{i}" for i in range(6)]
        rows = []
        for day, date in enumerate(pd.date_range("2024-01-01", "2025-09-20", freq="3D")):
            h, a = teams[day % 6], teams[(day + 1 + day // 6) % 6]
            if h == a:
                a = teams[(day + 2) % 6]
            # No opening prices at all; closing prices on every row.
            rows.append({"Date": date, "HomeTeam": h, "AwayTeam": a, "FTHG": int(rng.poisson(1.5)),
                         "FTAG": int(rng.poisson(1.1)), "HST": int(rng.integers(2, 8)),
                         "AST": int(rng.integers(1, 6)), "HS": 12, "AS": 9,
                         "PSCH": 2.1, "PSCD": 3.4, "PSCA": 3.6, "PC>2.5": 1.9, "PC<2.5": 1.95})
        cfg = json.loads(Path("historical_benchmark_config.json").read_text(encoding="utf-8-sig"))
        cfg.update(leagues=["EPL"], test_start="2025-08-01", audit_start="2025-08-29",
                   test_end_exclusive="2025-09-20", min_train=100, min_development_matches=1,
                   min_audit_matches=1)
        cfg["model_upgrade_comparison"]["production_v1"]["half_life_tuning"].update(
            candidates=[240., 480.], validation_days=120, step_days=60, min_train=60,
            min_validation_matches=5)
        records, _, _, errors = hb.evaluate_league(pd.DataFrame(rows), "EPL", cfg)
        self.assertEqual(errors, [])
        variants = {r["variant"] for r in records}
        self.assertIn("pinnacle_closing_only", variants)
        for record in records:
            if record["variant"] in self.ORACLE_VARIANTS:
                self.assertIn("evaluation_only", record["timing"])
                continue
            with self.subTest(variant=record["variant"]):
                self.assertEqual(record["timing"], "model_only")
                self.assertFalse(record.get("blend_applied", False))
                self.assertNotEqual(record.get("anchor_status"), "ANCHORED")


if __name__ == "__main__":
    unittest.main()
