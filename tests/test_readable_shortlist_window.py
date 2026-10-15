"""Window-cohort and shortlist formatter regression tests (offline)."""

from offline_test_case import OfflineQuotePolicyTestCase
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


class SeventyTwoHourSelectionTests(OfflineQuotePolicyTestCase):
    def setUp(self):
        self.clock = NOW

    def select(self, rows):
        return build_conservative_shortlist(pd.DataFrame(rows), as_of=self.clock)

    def test_stronger_distant_fixtures_cannot_override_hard_horizon(self):
        nearby = [fixture(i, kickoff=NOW + timedelta(hours=24)) for i in range(10)]
        far = fixture(100, kickoff=NOW + timedelta(hours=73))
        far.update(p_over_1_5=0.99, raw_p_over_1_5=0.96)
        picks, audit, info = self.select(nearby + [far])
        self.assertEqual(len(picks), 10)
        self.assertNotIn(far["fixture_id"], set(picks["fixture_id"]))
        self.assertTrue(info["selected_matches_within_72_hours"])
        rejected = audit[audit.fixture_id == far["fixture_id"]]
        self.assertTrue(rejected.rejection_reasons.str.contains("outside next 72 hours").all())

    def test_exact_72_hour_boundary_inclusive_and_one_second_over_rejected(self):
        rows = [fixture(0, NOW + timedelta(hours=72)),
                fixture(1, NOW + timedelta(hours=72, seconds=1))]
        picks, _, info = self.select(rows)
        self.assertEqual(picks.fixture_id.tolist(), ["fixture-0"])
        self.assertEqual(info["shortlist_lookahead_hours"], 72)
        self.assertEqual(info["shortlist_window_end_utc"], rows[0]["kickoff_utc"])

    def test_horizon_anchored_to_run_not_first_kickoff(self):
        rows = [fixture(0, NOW + timedelta(hours=71)),
                fixture(1, NOW + timedelta(hours=80))]
        picks, _, _ = self.select(rows)
        self.assertEqual(picks.fixture_id.tolist(), ["fixture-0"])

    def test_no_fallback_outside_horizon_when_fewer_than_ten(self):
        games = [fixture(i, kickoff=NOW + timedelta(days=1 + i*2)) for i in range(10)]
        picks, _, info = self.select(games)
        self.assertEqual(len(picks), 2)
        self.assertEqual(info["shortfall"], 8)
        self.assertEqual(info["status"], "BELOW_TARGET")

    def test_minimum_kickoff_lead_and_timezone_conversion(self):
        rows = [fixture(0, NOW + timedelta(minutes=19)),
                fixture(1, NOW + timedelta(minutes=20)),
                fixture(2, NOW - timedelta(hours=1))]
        rows[1]["kickoff_utc"] = pd.Timestamp(rows[1]["kickoff_utc"]).tz_convert("Africa/Nairobi").isoformat()
        picks, _, _ = self.select(rows)
        self.assertEqual(picks.fixture_id.tolist(), ["fixture-1"])

    def test_one_fixture_excludes_btts_and_keeps_qualifying_market_label(self):
        row = fixture()
        row["p_over_1_5"] = 0.78
        row["p_under_3_5"] = 0.77
        row["p_btts_yes"] = 0.83
        row["raw_p_btts_yes"] = 0.80
        row["market_btts_yes_odds"] = 1.40
        picks, _, info = self.select([row])
        self.assertEqual(picks.iloc[0]["market"],
                         "Home win")
        readable = readable_shortlist_frame(picks)
        self.assertEqual(readable.iloc[0]["Shortlisted market"],
                         "Home win")
        self.assertEqual(readable.iloc[0]["Match"], "Home_0 vs Away_0")
        self.assertEqual(info["shortfall"], 9)


class FormatterIntegrationTests(OfflineQuotePolicyTestCase):
    def test_refresh_replaces_stale_outputs_and_uses_all_stored_candidates(self):
        from refresh_conservative_shortlist import refresh
        from test_graded_candidates import sample_report, only_over_goal
        rows = [only_over_goal(i) for i in range(3)]
        rows[0]['kickoff_utc'] = (NOW + timedelta(days=8)).isoformat()
        rows[1]['kickoff_utc'] = (NOW + timedelta(hours=71)).isoformat()
        rows[2]['kickoff_utc'] = (NOW + timedelta(hours=72, seconds=1)).isoformat()
        rows[1]['league'] = 'UEFA Champions League'
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            raw = root / 'raw'
            raw.mkdir()
            pd.DataFrame(rows).to_csv(raw / 'all_leagues_predictions.csv', index=False)
            pd.DataFrame([rows[0]]).to_csv(raw / 'conservative_bet_shortlist.csv', index=False)
            for key, league in [('EPL', 'Premier League'), ('UCL', 'UEFA Champions League')]:
                report = dict(sample_report(), league=league)
                (raw / f'{key}_goal_market_validation.json').write_text(json.dumps(report))
            summary = refresh(root, as_of=NOW)
            picks = pd.read_csv(raw / 'conservative_bet_shortlist.csv')
            self.assertEqual(picks.fixture_id.tolist(), [rows[1]['fixture_id']])
            self.assertTrue(summary['selected_matches_within_72_hours'])
            self.assertTrue(summary['ucl_validation_available'])
            self.assertIn('72 hours', (root / 'readable' / 'conservative_bet_shortlist_report.md').read_text())

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
            self.assertIn("Kickoffs within next 72 hours of run", md)
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
                json.dumps({"status": "NO BET", "target_distinct_matches": 10,
                            "shortfall": 10}), encoding="utf-8"
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


