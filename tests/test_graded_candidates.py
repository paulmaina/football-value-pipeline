"""Strict-first ten-fixture shortlist and pathological bookmaker odds tests."""

import json
from pathlib import Path
import tempfile
import unittest

import pandas as pd

from conservative_bet_filter import build_conservative_shortlist
from football_value_pipeline_v2_standalone import TheOddsAPI, LEAGUES
from format_football_output import process_conservative_shortlist
from test_conservative_bet_filter import NOW, fixture


def sample_report():
    keys = ("home", "away", "over_1_5", "under_3_5", "btts_yes")
    groups = {
        "75plus": {
            "status": "PASSED",
            "development": {"n": 100}, "audit": {"n": 40},
            "development_only_penalty": 0.0,
        },
        "85plus": {
            "status": "INSUFFICIENT_HIGH_CONFIDENCE_HISTORY",
            "development": {"n": 29}, "audit": {
                "n": 11, "overconfidence": 0.04,
            },
            "development_only_penalty": 0.0,
        },
    }
    return {"markets": {key: {
        "status": "RELIABLE_FOR_RANKING",
        "confidence_penalty": 0.0,
        "development": {"n": 100}, "audit": {"n": 40, "brier": 0.17},
        "high_confidence": groups,
    } for key in keys}}


def only_over_goal(i):
    row = fixture(i)
    row["p_over_1_5"] = 0.83 if i < 4 else 0.91
    row["raw_p_over_1_5"] = 0.80 if i < 4 else 0.88
    for key in ("home", "away", "under_3_5", "btts_yes"):
        row[f"market_{key}_odds"] = None
    return row


class GradedCandidatesTests(unittest.TestCase):
    def test_four_strict_plus_six_research_only_provisional(self):
        rows = pd.DataFrame([only_over_goal(i) for i in range(12)])
        picks, decisions, summary = build_conservative_shortlist(
            rows, as_of=NOW, market_reliability={"Premier League": sample_report()}
        )
        self.assertEqual(len(picks), 10)
        self.assertEqual(picks["fixture_id"].nunique(), 10)
        self.assertEqual(summary["n_strict_qualified"], 4)
        self.assertEqual(summary["n_provisional_watchlist"], 6)
        self.assertEqual(summary["status"], "TARGET_WITH_PROVISIONAL")
        self.assertEqual(sum(picks["selection_tier"]=="STRICT"), 4)
        self.assertEqual(sum(picks["selection_tier"]=="PROVISIONAL"), 6)
        watch = picks[picks["selection_tier"]=="PROVISIONAL"]
        self.assertTrue(watch["near_miss_reason"].str.contains(
            "INSUFFICIENT_HIGH_CONFIDENCE_HISTORY"
        ).all())
        self.assertTrue(watch["historical_gap_score"].notna().all())
        self.assertTrue((watch["decision"]=="SHORTLISTED_PROVISIONAL").all())

    def test_ucl_uses_own_validation_and_preserves_strict_gates(self):
        row = only_over_goal(0)
        row["league"] = "UEFA Champions League"
        picks, _, summary = build_conservative_shortlist(
            pd.DataFrame([row]), as_of=NOW,
            market_reliability={"UEFA Champions League": sample_report()},
        )
        self.assertEqual(len(picks), 1)
        self.assertEqual(picks.iloc[0]["selection_tier"], "STRICT")
        self.assertIn("UEFA Champions League", summary["eligible_leagues"])
        for reports in (None, {}, {"Premier League": sample_report()}):
            picks, _, _ = build_conservative_shortlist(
                pd.DataFrame([row]), as_of=NOW, market_reliability=reports,
            )
            self.assertTrue(picks.empty)

    def test_provisional_ucl_respects_horizon_and_invalid_odds(self):
        from datetime import timedelta
        rows = [only_over_goal(i) for i in (4, 5, 6)]
        for row in rows:
            row["league"] = "UEFA Champions League"
        rows[1]["kickoff_utc"] = (NOW + timedelta(hours=60, seconds=1)).isoformat()
        rows[2]["market_over_1_5_odds"] = None
        picks, _, summary = build_conservative_shortlist(
            pd.DataFrame(rows), as_of=NOW,
            market_reliability={"UEFA Champions League": sample_report()},
        )
        self.assertEqual(picks.fixture_id.tolist(), [rows[0]["fixture_id"]])
        self.assertEqual(summary["n_provisional_watchlist"], 1)
        self.assertEqual(picks.iloc[0]["selection_tier"], "PROVISIONAL")

    def test_missing_or_fabricated_reference_never_becomes_provisional(self):
        a=only_over_goal(4)
        a.update({
            "market_reference_home_odds": 1.1,
            "market_reference_draw_odds": 1.1,
            "market_reference_away_odds": 1.1,
        })
        # All goal-market quotes also rely on a valid coherent 1X2 blend;
        # make their own exact complementary reference implausible.
        a["market_reference_over_1_5_odds"] = 1.1
        a["market_reference_over_1_5_opposite_odds"] = 1.1
        picks, audit, summary = build_conservative_shortlist(
            pd.DataFrame([a]), as_of=NOW,
            market_reliability={"Premier League": sample_report()},
        )
        self.assertTrue(picks.empty)
        self.assertEqual(summary["n_provisional_watchlist"], 0)
        self.assertIn(
            "implausible same-book reference market overround",
            " ".join(audit["rejection_reasons"]),
        )

    def test_only_strict_without_validation_data(self):
        rows = pd.DataFrame([only_over_goal(i) for i in range(12)])
        picks, _, summary = build_conservative_shortlist(rows, as_of=NOW)
        self.assertEqual(len(picks), 10)
        self.assertEqual(summary["n_provisional_watchlist"], 0)
        self.assertTrue((picks["selection_tier"]=="STRICT").all())

    def test_formatter_marks_unvalidated_rows_without_relabeling(self):
        rows = pd.DataFrame([only_over_goal(i) for i in range(12)])
        picks, _, summary = build_conservative_shortlist(
            rows, as_of=NOW, market_reliability={"Premier League": sample_report()}
        )
        with tempfile.TemporaryDirectory() as tmp:
            raw = Path(tmp) / "raw"
            readable = Path(tmp) / "readable"
            raw.mkdir()
            readable.mkdir()
            picks.to_csv(raw / "conservative_bet_shortlist.csv", index=False)
            (raw / "conservative_bet_summary.json").write_text(json.dumps(summary))
            self.assertEqual(process_conservative_shortlist(raw, readable), 10)
            report = (readable / "conservative_bet_shortlist_report.md").read_text()
            self.assertIn("Strictly qualified:** 4", report)
            self.assertIn("Provisional watchlist:** 6", report)
            self.assertIn("NOT qualified bets", report)
            table = pd.read_csv(readable / "conservative_bet_shortlist_readable.csv")
            self.assertEqual((table["Qualification"]=="PROVISIONAL").sum(), 6)

    def test_real_odds_client_instance_calls_static_event_parser(self):
        """Regression: self.flatten_odds_event(event) must not inject self.

        Unlike direct class calls, this is the same code path exercised
        when production retrieves cached or fresh bookmaker odds.
        """
        from datetime import datetime, timezone

        event = {
            "id": "event-123",
            "home_team": "Home FC",
            "away_team": "Away FC",
            "commence_time": "2026-10-16T16:00:00Z",
            "bookmakers": [{
                "title": "Coherent Sportsbook",
                "markets": [{
                    "key": "h2h",
                    "last_update": "2026-10-09T14:00:00Z",
                    "outcomes": [
                        {"name": "Home FC", "price": 1.9},
                        {"name": "Draw", "price": 3.5},
                        {"name": "Away FC", "price": 4.2},
                    ],
                }],
            }],
        }

        class StubHttp:
            def get_json(self, *args, **kwargs):
                return [event]

        api = TheOddsAPI.__new__(TheOddsAPI)
        api.http = StubHttp()
        api.regions = "eu"
        api.api_key = "fake"
        api.force_refresh = False
        result = api.odds(
            LEAGUES["EPL"], lookahead_days=10,
            now=datetime(2026, 10, 9, 12, 0, tzinfo=timezone.utc),
        )

        self.assertEqual(len(result), 1)
        self.assertEqual(result.iloc[0]["odds_bookmakers_1x2"], 1)
        self.assertEqual(result.iloc[0]["live_ref_1x2_bookmaker"],
                         "Coherent Sportsbook")
        self.assertEqual(result.iloc[0]["live_best_home_odds"], 1.9)
        self.assertEqual(
            TheOddsAPI.flatten_odds_event(event)["live_best_home_odds"],
            result.iloc[0]["live_best_home_odds"],
        )

    def test_anomalous_newest_bookmaker_cannot_supply_reference_or_best(self):
        event = {
            "id": "event-ok",
            "home_team": "Good Home",
            "away_team": "Good Away",
            "commence_time": "2026-10-18T16:00:00Z",
            "bookmakers": [
                {"title": "Regular",
                 "markets": [{
                    "key": "h2h", "last_update": "2026-10-09T14:33:00Z",
                    "outcomes": [
                        {"name": "Good Home", "price": 1.9},
                        {"name": "Draw", "price": 3.5},
                        {"name": "Good Away", "price": 4.2},
                    ],
                 }]},
                {"title": "Broken",
                 "markets": [{
                    "key": "h2h", "last_update": "2026-10-09T14:39:00Z",
                    "outcomes": [
                        {"name": "Good Home", "price": 1.1},
                        {"name": "Draw", "price": 1.1},
                        {"name": "Good Away", "price": 100.0},
                    ],
                 }]},
            ],
        }
        flat=TheOddsAPI.flatten_odds_event(event)
        self.assertEqual(flat["live_ref_1x2_bookmaker"], "Regular")
        self.assertEqual(flat["odds_bookmakers_1x2"], 1)
        self.assertEqual(flat["live_best_away_odds"], 4.2)
        self.assertEqual(flat["live_best_away_bookmaker"], "Regular")
        self.assertEqual(flat["live_ref_home_odds"], 1.9)
        self.assertNotEqual(
            flat["live_best_away_last_update_utc"],
            "2026-10-09T14:39:00Z",
        )


if __name__=="__main__":
    unittest.main()

