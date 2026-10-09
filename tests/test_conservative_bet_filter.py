"""Offline tests for the fail-closed, conservative bet-candidate filter."""

from datetime import datetime, timedelta, timezone
from pathlib import Path
import json
import tempfile
import unittest
from unittest.mock import patch

import pandas as pd

from conservative_bet_filter import build_conservative_shortlist
from football_value_pipeline_v2_standalone import main


NOW = datetime(2026, 10, 9, 9, 0, tzinfo=timezone.utc)


def fixture(
    home="Example Home",
    away="Example Away",
    league="Premier League",
    kickoff=None,
    updated=None,
    prob=0.72,
    raw_prob=0.68,
    price=1.50,
):
    kickoff = kickoff or NOW + timedelta(days=1)
    updated = updated or NOW - timedelta(hours=1)
    return {
        "league": league,
        "date": kickoff.date().isoformat(),
        "kickoff_utc": kickoff.isoformat(),
        "home_team": home,
        "away_team": away,
        "odds_source": "The Odds API",
        "market_blend_applied": True,
        "odds_bookmakers_1x2": 4,
        "model_home_team": home,
        "model_away_team": away,
        "home_name_match_score": 100.0,
        "away_name_match_score": 100.0,
        "p_home": prob,
        "p_draw": 0.18,
        "p_away": 1 - prob - 0.18,
        "raw_p_home": raw_prob,
        "raw_p_draw": 0.19,
        "raw_p_away": 1 - raw_prob - 0.19,
        "market_p_home": 0.70,
        "market_p_draw": 0.18,
        "market_p_away": 0.12,
        "market_reference_home_odds": 1.45,
        "market_reference_draw_odds": 4.8,
        "market_reference_away_odds": 7.5,
        "market_home_odds": price,
        "market_away_odds": 8.0,
        "best_home_bookmaker": "Book A",
        "best_away_bookmaker": "Book A",
        "market_best_home_last_update_utc": updated.isoformat(),
        "market_best_away_last_update_utc": updated.isoformat(),
        # Intentional: other-market metadata must NOT override stale quote.
        "odds_last_update_utc": NOW.isoformat(),
    }


class FilterTests(unittest.TestCase):
    def evaluate(self, *rows):
        return build_conservative_shortlist(pd.DataFrame(list(rows)), as_of=NOW)

    def test_valid_home_single_and_rejection_audit(self):
        shortlist, decisions, summary = self.evaluate(fixture())
        self.assertEqual(len(shortlist), 1)
        self.assertEqual(len(decisions), 2)
        self.assertEqual(shortlist.iloc[0]["market"], "Home win")
        self.assertEqual(shortlist.iloc[0]["bookmaker"], "Book A")
        self.assertAlmostEqual(shortlist.iloc[0]["estimated_ev"], 0.08)
        self.assertEqual(summary["status"], "CANDIDATES_FOUND")

    def test_utc_matchday_cap_and_sorting(self):
        rows = [
            fixture(home="H1", prob=0.72),
            fixture(home="H2", prob=0.75),
            fixture(home="H3", prob=0.70),
            fixture(home="H4", prob=0.73, kickoff=NOW+timedelta(days=2)),
        ]
        picks, audit, summary = self.evaluate(*rows)
        self.assertEqual(len(picks), 3)
        same_day = picks[picks["date"] == (NOW + timedelta(days=1)).date().isoformat()]
        self.assertEqual(same_day["home_team"].tolist(), ["H2", "H1"])
        self.assertEqual(len(audit[audit["decision"] == "NOT_SELECTED"]), 1)
        self.assertEqual(summary["max_matches_per_utc_date"], 2)

    def test_reject_stale_quote_even_when_other_odds_fresh(self):
        row = fixture(updated=NOW-timedelta(hours=48))
        picks, audit, summary = self.evaluate(row)
        self.assertTrue(picks.empty)
        self.assertIn("over 24 hours", audit.iloc[0]["rejection_reasons"])
        self.assertEqual(summary["status"], "NO BET")

    def test_reject_unmatched_teams_and_unsupported_competition(self):
        row = fixture(league="UEFA Champions League")
        row["model_home_team"] = "__LEAGUE_AVERAGE__"
        picks, audit, _ = self.evaluate(row)
        self.assertTrue(picks.empty)
        self.assertIn("competition not in validated", audit.iloc[0]["rejection_reasons"])
        self.assertIn("team-model name mapping", audit.iloc[0]["rejection_reasons"])

    def test_reject_no_market_blend_and_outdated_fixture(self):
        row = fixture(kickoff=NOW+timedelta(minutes=10))
        row["market_blend_applied"] = False
        picks, audit, _ = self.evaluate(row)
        self.assertEqual(len(picks), 0)
        self.assertIn("20 minutes", audit.iloc[0]["rejection_reasons"])
        self.assertIn("no complete blended live", audit.iloc[0]["rejection_reasons"])

    def test_reject_when_raw_dc_favors_different_team(self):
        row = fixture()
        row["raw_p_home"] = 0.28
        row["raw_p_draw"] = 0.20
        row["raw_p_away"] = 0.52
        picks, audit, _ = self.evaluate(row)
        self.assertTrue(picks.empty)
        self.assertIn("raw Dixon-Coles", audit.iloc[0]["rejection_reasons"])

    def test_reject_when_expected_value_too_low(self):
        picks, audit, _ = self.evaluate(fixture(price=1.40))
        self.assertTrue(picks.empty)
        self.assertIn("below +3%", audit.iloc[0]["rejection_reasons"])

    def test_reject_missing_verified_best_quote_timestamp(self):
        row = fixture()
        row["market_best_home_last_update_utc"] = None
        picks, audit, _ = self.evaluate(row)
        self.assertTrue(picks.empty)
        self.assertIn("price is missing", audit.iloc[0]["rejection_reasons"])

    def test_reject_missing_market_price_and_bad_model_confidence(self):
        row = fixture()
        row["market_reference_draw_odds"] = None
        row["odds_bookmakers_1x2"] = 1
        row["away_name_match_score"] = 72
        picks, audit, _ = self.evaluate(row)
        self.assertTrue(picks.empty)
        self.assertIn("incomplete coherent reference", audit.iloc[0]["rejection_reasons"])
        self.assertIn("fewer than two", audit.iloc[0]["rejection_reasons"])
        self.assertIn("name mapping", audit.iloc[0]["rejection_reasons"])

    def test_empty_predictions_are_valid_no_bet(self):
        picks, audit, summary = build_conservative_shortlist(
            pd.DataFrame(), as_of=NOW
        )
        self.assertEqual(summary["status"], "NO BET")
        self.assertTrue(picks.empty)
        self.assertIn("market", picks.columns)
        self.assertIn("rejection_reasons", audit.columns)

    def test_aware_clock_is_required(self):
        with self.assertRaisesRegex(ValueError, "timezone-aware"):
            build_conservative_shortlist(pd.DataFrame(), as_of=datetime(2026, 10, 9))

    def test_main_writes_filter_outputs_without_new_cli_flags(self):
        frame = pd.DataFrame([fixture()])
        with tempfile.TemporaryDirectory() as temp:
            out = Path(temp) / "raw"
            with patch(
                "football_value_pipeline_v2_standalone.FootballValuePipelineV2.run_league",
                return_value=(frame, {"test": True}, {}),
            ):
                result = main(["--leagues", "EPL", "--out-dir", str(out)])
            self.assertEqual(result, 0)
            self.assertTrue((out / "EPL_predictions.csv").is_file())
            self.assertTrue((out / "conservative_bet_shortlist.csv").is_file())
            self.assertTrue((out / "conservative_bet_rejections.csv").is_file())
            self.assertTrue((out / "conservative_bet_summary.json").is_file())
            self.assertEqual(len(list((out / "shortlist_history").glob("*.csv"))), 1)
            summary = json.loads((out / "conservative_bet_summary.json").read_text())
            # Fake fixture is in 2026; testing on a real later CI day must
            # be fail-closed, but outputs must still be written.
            self.assertIn(summary["status"], ("NO BET", "CANDIDATES_FOUND"))


if __name__ == "__main__":
    unittest.main()
