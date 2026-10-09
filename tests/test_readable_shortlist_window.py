"""Window-cohort and shortlist formatter regression tests (offline)."""

from datetime import timedelta
import json
from pathlib import Path
import tempfile
import unittest

import pandas as pd

from conservative_bet_filter import build_conservative_shortlist
from format_football_output import (
    main as formatter_main,
    process_conservative_shortlist,
    readable_shortlist_frame,
)
from test_conservative_bet_filter import NOW, fixture


class FourDaySelectionTests(unittest.TestCase):
    def setUp(self):
        self.clock = NOW

    def select(self, rows):
        return build_conservative_shortlist(pd.DataFrame(rows), as_of=self.clock)

    def test_prefer_eight_in_four_days_over_scattered_higher_probability(self):
        local = [fixture(i, kickoff=NOW + timedelta(days=1)) for i in range(8)]
        distant = [fixture(100 + i, kickoff=NOW + timedelta(days=7))
                   for i in range(2)]
        for item in distant:
            item["p_over_1_5"] = 0.93
            item["raw_p_over_1_5"] = 0.90
        shortlist, audit, info = self.select(distant + local)
        self.assertEqual(len(shortlist), 8)
        self.assertTrue(set(shortlist["fixture_id"]) == {
            item["fixture_id"] for item in local
        })
        self.assertTrue(info["selected_matches_within_four_days"])
        self.assertTrue(info["eight_match_four_day_window_available"])
        self.assertEqual(info["selected_kickoff_span_hours"], 0)
        self.assertEqual(info["shortfall"], 0)
        self.assertEqual(len(audit[audit["decision"] == "SHORTLISTED"]), 8)

    def test_choose_highest_chance_eligible_eight_match_window(self):
        low = [fixture(i, kickoff=NOW + timedelta(days=1)) for i in range(8)]
        high = [fixture(100 + i, kickoff=NOW + timedelta(days=8))
                for i in range(8)]
        for item in high:
            item["p_over_1_5"] = 0.91
            item["raw_p_over_1_5"] = 0.89
        shortlist, _, info = self.select(low + high)
        self.assertEqual(set(shortlist["fixture_id"]),
                         {item["fixture_id"] for item in high})
        self.assertTrue(info["selected_matches_within_four_days"])

    def test_96_hour_boundary_is_inclusive(self):
        games = [fixture(i, kickoff=NOW + timedelta(days=1, hours=(96 * i / 7)))
                 for i in range(8)]
        picks, _, info = self.select(games)
        self.assertEqual(len(picks), 8)
        self.assertTrue(info["selected_matches_within_four_days"])
        self.assertAlmostEqual(info["selected_kickoff_span_hours"], 96)
        self.assertEqual(info["status"], "TARGET_MET")

    def test_fallback_when_no_eight_game_window_exists(self):
        games = [fixture(i, kickoff=NOW + timedelta(days=1 + i*2))
                 for i in range(8)]
        picks, audit, info = self.select(games)
        self.assertEqual(len(picks), 8)
        self.assertFalse(info["eight_match_four_day_window_available"])
        self.assertFalse(info["selected_matches_within_four_days"])
        self.assertTrue(info["selected_kickoff_span_hours"] > 96)
        self.assertIn("full forecast horizon", info["selection_method"])
        self.assertEqual(len(audit[audit["decision"] == "SHORTLISTED"]), 8)

    def test_one_fixture_keeps_btts_or_goals_market_label(self):
        row = fixture()
        row["p_over_1_5"] = 0.78
        row["p_under_3_5"] = 0.77
        row["p_btts_yes"] = 0.83
        row["raw_p_btts_yes"] = 0.80
        row["market_btts_yes_odds"] = 1.40
        picks, _, info = self.select([row])
        self.assertEqual(picks.iloc[0]["market"],
                         "Both Teams to Score - Yes")
        readable = readable_shortlist_frame(picks)
        self.assertEqual(readable.iloc[0]["Shortlisted market"],
                         "Both Teams to Score - Yes")
        self.assertEqual(readable.iloc[0]["Match"], "Home_0 vs Away_0")
        self.assertEqual(info["shortfall"], 7)


class FormatterIntegrationTests(unittest.TestCase):
    def test_formatter_creates_both_readable_reports_and_does_not_edit_raw(self):
        picks, _, summary = build_conservative_shortlist(
            pd.DataFrame([fixture(0)]), as_of=NOW
        )
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "football_output_v2"
            raw = root / "raw"
            raw.mkdir(parents=True)
            # A minimal real pipeline-style per-league file triggers the
            # standard reporting flow alongside the shortlist formatter.
            pd.DataFrame([fixture(0)]).to_csv(
                raw / "EPL_predictions.csv", index=False
            )
            source = raw / "conservative_bet_shortlist.csv"
            picks.to_csv(source, index=False)
            (raw / "conservative_bet_summary.json").write_text(
                json.dumps(summary), encoding="utf-8"
            )
            before = source.read_bytes()
            self.assertEqual(formatter_main(["--root-dir", str(root)]), 0)
            readable = root / "readable"
            self.assertTrue((readable / "conservative_bet_shortlist_readable.csv").exists())
            md = (readable / "conservative_bet_shortlist_report.md").read_text(
                encoding="utf-8"
            )
            table = pd.read_csv(
                readable / "conservative_bet_shortlist_readable.csv"
            )
            self.assertIn("Shortlisted market", table.columns)
            self.assertEqual(table.iloc[0]["Shortlisted market"], "Over 1.5")
            self.assertIn("Home_0 vs Away_0", md)
            self.assertIn("Over 1.5", md)
            self.assertIn("Kickoffs within 4 days", md)
            self.assertEqual(source.read_bytes(), before)

    def test_empty_shortlist_formats_without_fabricated_match(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "raw").mkdir()
            (root / "readable").mkdir()
            shortlist = pd.DataFrame(columns=[
                "market", "home_team", "away_team", "kickoff_utc",
                "predicted_probability", "estimated_ev", "decision",
            ])
            shortlist.to_csv(root / "raw" / "conservative_bet_shortlist.csv", index=False)
            (root / "raw" / "conservative_bet_summary.json").write_text(
                json.dumps({"status": "NO BET", "target_distinct_matches": 8,
                            "shortfall": 8}), encoding="utf-8"
            )
            n = process_conservative_shortlist(
                root / "raw", root / "readable"
            )
            self.assertEqual(n, 0)
            result = pd.read_csv(
                root / "readable" / "conservative_bet_shortlist_readable.csv"
            )
            self.assertTrue(result.empty)
            self.assertIn("No qualifying matches", (
                root / "readable" / "conservative_bet_shortlist_report.md"
            ).read_text(encoding="utf-8"))

    def test_missing_raw_shortlist_removes_stale_readable_reports(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            raw, readable = root / "raw", root / "readable"
            raw.mkdir()
            readable.mkdir()
            for name in ("conservative_bet_shortlist_readable.csv",
                         "conservative_bet_shortlist_report.md"):
                (readable / name).write_text("stale")
            self.assertIsNone(process_conservative_shortlist(raw, readable))
            self.assertFalse(any(readable.iterdir()))


if __name__ == "__main__":
    unittest.main()
