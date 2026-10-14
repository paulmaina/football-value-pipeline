"""Offline regression tests for ten-match, five-market candidate selection."""

from datetime import datetime, timedelta, timezone
from pathlib import Path
import json
import tempfile
import unittest
from unittest.mock import patch

import pandas as pd

from conservative_bet_filter import build_conservative_shortlist
from football_value_pipeline_v2_standalone import (
    LEAGUES, TheOddsAPI, main, prediction_from_matrix, DixonColesModel,
)
import numpy as np


NOW = datetime(2026, 10, 9, 9, 0, tzinfo=timezone.utc)


def fixture(i=0, kickoff=None):
    kickoff = kickoff or NOW + timedelta(days=1+i//6)
    updated = NOW - timedelta(hours=1)
    row = {
        "league": "Premier League",
        "date": kickoff.date().isoformat(),
        "kickoff_utc": kickoff.isoformat(),
        "fixture_id": f"fixture-{i}",
        "home_team": f"Home_{i}",
        "away_team": f"Away_{i}",
        "odds_source": "The Odds API",
        "market_blend_applied": True,
        "odds_bookmakers_1x2": 3,
        "model_home_team": f"Home_{i}",
        "model_away_team": f"Away_{i}",
        "home_name_match_score": 100.0,
        "away_name_match_score": 100.0,
        "p_home": 0.72,
        "p_draw": 0.17,
        "p_away": 0.11,
        "raw_p_home": 0.68,
        "raw_p_draw": 0.19,
        "raw_p_away": 0.13,
        "market_p_home": 0.70,
        "market_p_draw": 0.18,
        "market_p_away": 0.12,
        "market_reference_home_odds": 1.47,
        "market_reference_draw_odds": 4.3,
        "market_reference_away_odds": 7.3,
        "market_home_odds": 1.52,
        "market_away_odds": 7.4,
        "best_home_bookmaker": "Book A",
        "best_away_bookmaker": "Book B",
        "market_best_home_last_update_utc": updated.isoformat(),
        "market_best_away_last_update_utc": updated.isoformat(),
        "p_over_1_5": 0.86,
        "raw_p_over_1_5": 0.83,
        "market_p_over_1_5": 0.84,
        "market_over_1_5_odds": 1.27,
        "best_over_1_5_bookmaker": "Book A",
        "market_best_over_1_5_last_update_utc": updated.isoformat(),
        "market_reference_over_1_5_odds": 1.25,
        "market_reference_over_1_5_opposite_odds": 4.0,
        "market_over_1_5_bookmakers": 2,
        "p_under_3_5": 0.79,
        "raw_p_under_3_5": 0.77,
        "market_p_under_3_5": 0.77,
        "market_under_3_5_odds": 1.40,
        "best_under_3_5_bookmaker": "Book C",
        "market_best_under_3_5_last_update_utc": updated.isoformat(),
        "market_reference_under_3_5_odds": 1.38,
        "market_reference_under_3_5_opposite_odds": 3.1,
        "market_under_3_5_bookmakers": 2,
        "p_btts_yes": 0.73,
        "raw_p_btts_yes": 0.70,
        "market_p_btts_yes": 0.70,
        "market_btts_yes_odds": 1.49,
        "best_btts_yes_bookmaker": "Book D",
        "market_best_btts_yes_last_update_utc": updated.isoformat(),
        "market_reference_btts_yes_odds": 1.47,
        "market_reference_btts_yes_opposite_odds": 2.4,
        "market_btts_yes_bookmakers": 2,
    }
    return row


class TenMarketTests(unittest.TestCase):
    def evaluate(self, *rows):
        return build_conservative_shortlist(pd.DataFrame(list(rows)), as_of=NOW)

    def test_all_five_markets_are_evaluated_but_one_per_match(self):
        shortlist, decisions, summary = self.evaluate(fixture())
        self.assertEqual(len(decisions), 5)
        self.assertEqual(len(shortlist), 1)
        self.assertEqual(shortlist.iloc[0]["market"], "Over 1.5")
        self.assertEqual(summary["status"], "BELOW_TARGET")
        self.assertEqual(summary["shortfall"], 9)
        self.assertEqual(len(decisions[decisions.decision == "NOT_SELECTED"]), 1)

    def test_equal_probability_uses_highest_quoted_odds(self):
        row = fixture()
        row["p_home"] = row["p_over_1_5"]
        picks, _, _ = self.evaluate(row)
        self.assertEqual(picks.iloc[0]["market"], "Home win")
        self.assertEqual(picks.iloc[0]["offered_decimal_odds"], 1.52)

    def test_higher_probability_takes_priority_over_higher_odds(self):
        picks, _, _ = self.evaluate(fixture())
        self.assertEqual(picks.iloc[0]["market"], "Over 1.5")

    def test_btts_is_excluded_even_with_high_probability_and_value(self):
        row = fixture()
        row.update(p_btts_yes=0.99, raw_p_btts_yes=0.99, market_btts_yes_odds=2.0)
        picks, decisions, summary = self.evaluate(row)
        self.assertNotIn("Both Teams to Score - Yes", decisions["market"].tolist())
        self.assertNotIn("Both Teams to Score - Yes", summary["eligible_markets"])
        self.assertEqual(picks.iloc[0]["market"], "Over 1.5")

    def test_exactly_ten_distinct_fixtures_selected_across_multiple_days(self):
        rows = [fixture(i) for i in range(12)]
        shortlist, decisions, summary = self.evaluate(*rows)
        self.assertEqual(len(shortlist), 10)
        self.assertEqual(shortlist["fixture_id"].nunique(), 10)
        self.assertEqual(summary["status"], "TARGET_MET")
        self.assertEqual(summary["shortfall"], 0)
        self.assertEqual(len(decisions), 60)
        self.assertEqual(len(decisions[decisions.decision == "SHORTLISTED"]), 10)

    def test_winner_markets_without_extra_odds_remain_eligible(self):
        row = fixture()
        for key in ("over_1_5", "under_3_5", "btts_yes"):
            row.pop(f"market_{key}_odds")
        picks, decisions, _ = self.evaluate(row)
        self.assertEqual(len(picks), 1)
        self.assertEqual(picks.iloc[0]["market"], "Home win")
        self.assertEqual(len(decisions), 5)

    def test_away_win_can_be_selected(self):
        row = fixture()
        row.update({
            "p_home": 0.12, "p_draw": 0.16, "p_away": 0.72,
            "raw_p_home": 0.14, "raw_p_draw": 0.19, "raw_p_away": 0.67,
            "market_p_away": 0.69,
            "market_away_odds": 1.55,
        })
        for key in ("over_1_5", "under_3_5", "btts_yes"):
            row.pop(f"market_{key}_odds")
        picks, _, _ = self.evaluate(row)
        self.assertEqual(picks.iloc[0]["market"], "Away win")

    def test_no_prices_or_stale_prices_fail_closed(self):
        row = fixture()
        for key in ("over_1_5", "under_3_5", "btts_yes"):
            row.pop(f"market_{key}_odds")
        row["market_best_home_last_update_utc"] = (
            NOW - timedelta(days=3)
        ).isoformat()
        picks, decisions, summary = self.evaluate(row)
        self.assertEqual(len(picks), 0)
        self.assertEqual(summary["status"], "NO BET")
        self.assertTrue(any("stale" in x for x in decisions.rejection_reasons))

    def test_model_uncertainty_and_unsupported_league_are_rejected(self):
        row = fixture()
        row["league"] = "Unsupported Cup"
        row["model_home_team"] = "__LEAGUE_AVERAGE__"
        picks, decisions, _ = self.evaluate(row)
        self.assertTrue(picks.empty)
        self.assertTrue(
            all("competition excluded" in reason for reason in decisions.rejection_reasons)
        )

    def test_unblended_probabilities_must_not_have_negative_ev(self):
        row = fixture()
        # Strong blended score but raw O1.5 probability loses at this quote.
        row["raw_p_over_1_5"] = 0.73
        row["market_over_1_5_odds"] = 1.28  # raw EV < 0 at 73%
        picks, decisions, _ = self.evaluate(row)
        self.assertFalse(
            any((decisions.market == "Over 1.5") & (decisions.decision == "SHORTLISTED"))
        )
        self.assertTrue(len(picks) <= 1)

    def test_missing_price_but_high_probability_is_not_a_bet(self):
        row = fixture()
        for key in ("home", "away", "over_1_5", "under_3_5", "btts_yes"):
            row[f"market_{key}_odds"] = None
        picks, _, summary = self.evaluate(row)
        self.assertEqual(summary["status"], "NO BET")
        self.assertTrue(picks.empty)

    def test_empty_frames_and_clock(self):
        picks, decisions, summary = build_conservative_shortlist(
            pd.DataFrame(), as_of=NOW
        )
        self.assertEqual(summary["status"], "NO BET")
        self.assertTrue(picks.empty)
        self.assertEqual(len(decisions), 0)
        with self.assertRaisesRegex(ValueError, "timezone-aware"):
            build_conservative_shortlist(pd.DataFrame(), as_of=datetime(2026, 10, 9))

    def test_btts_probability_from_full_matrix(self):
        model = DixonColesModel(max_goals=10)
        matrix = np.full((3, 3), 1/9.0)
        scores = prediction_from_matrix(model, matrix, {})
        self.assertAlmostEqual(scores["p_btts_yes"], 4/9)
        self.assertAlmostEqual(scores["p_btts_no"], 5/9)

    def test_api_event_prices_are_verified_same_book_pairs(self):
        class StubHttp:
            def get_json(self, *args, **kwargs):
                return {
                    "id": "e42",
                    "bookmakers": [{
                        "title": "Book A",
                        "markets": [
                            {
                                "key": "alternate_totals",
                                "last_update": "2026-10-09T08:00:00Z",
                                "outcomes": [
                                    {"name": "Over", "point": 1.5, "price": 1.30},
                                    {"name": "Under", "point": 1.5, "price": 3.70},
                                    {"name": "Over", "point": 3.5, "price": 3.00},
                                    {"name": "Under", "point": 3.5, "price": 1.39},
                                ],
                            },
                            {
                                "key": "btts",
                                "last_update": "2026-10-09T08:15:00Z",
                                "outcomes": [
                                    {"name": "Yes", "price": 1.47},
                                    {"name": "No", "price": 2.43},
                                ],
                            },
                        ],
                    }],
                }

        api = TheOddsAPI.__new__(TheOddsAPI)
        api.http = StubHttp()
        api.regions = "eu"
        api.api_key = "fake"
        api.force_refresh = False
        extra = api.extra_markets_for_event(LEAGUES["EPL"], "e42")
        self.assertEqual(extra["market_over_1_5_odds"], 1.30)
        self.assertEqual(extra["market_under_3_5_odds"], 1.39)
        self.assertEqual(extra["market_btts_yes_odds"], 1.47)
        self.assertEqual(extra["market_btts_yes_bookmakers"], 1)
        self.assertEqual(
            extra["market_best_btts_yes_last_update_utc"],
            "2026-10-09T08:15:00Z",
        )

    def test_ucl_cli_generates_competition_specific_reliability_report(self):
        from test_graded_candidates import sample_report
        row = fixture()
        row["league"] = "UEFA Champions League"
        with tempfile.TemporaryDirectory() as tmp:
            raw = Path(tmp) / "raw"
            with patch(
                "football_value_pipeline_v2_standalone.FootballValuePipelineV2.run_league",
                return_value=(pd.DataFrame([row]), {
                    "training_end": "2026-09-20", "training_matches": 1000,
                }, {}),
            ), patch(
                "football_value_pipeline_v2_standalone.FootballValuePipelineV2.backtest_league",
                return_value=(pd.DataFrame(), pd.DataFrame(), {}, pd.DataFrame()),
            ) as backtest, patch(
                "goal_market_validation.evaluate_market_history",
                return_value=sample_report(),
            ):
                self.assertEqual(main(["--leagues", "UCL", "--out-dir", str(raw)]), 0)
            self.assertEqual(backtest.call_count, 1)
            self.assertEqual(backtest.call_args.args[0], "UCL")
            self.assertEqual(backtest.call_args.kwargs["min_train"], 250)
            report = json.loads((raw / "UCL_goal_market_validation.json").read_text())
            self.assertEqual(report["markets"]["home"]["status"], "RELIABLE_FOR_RANKING")
            summary = json.loads((raw / "conservative_bet_summary.json").read_text())
            self.assertIn("UEFA Champions League", summary["validation_market_statuses"])

    def test_normal_cli_still_writes_shortlist_and_snapshots(self):
        frame = pd.DataFrame([fixture()])
        with tempfile.TemporaryDirectory() as path:
            raw = Path(path) / "raw"
            with patch(
                "football_value_pipeline_v2_standalone.FootballValuePipelineV2.run_league",
                return_value=(frame, {
                    "sample": True, "training_end": "2026-09-20",
                    "training_matches": 1000,
                }, {}),
            ), patch(
                "football_value_pipeline_v2_standalone.FootballValuePipelineV2.backtest_league",
                return_value=(pd.DataFrame(), pd.DataFrame(), {}, pd.DataFrame()),
            ):
                result = main(["--leagues", "EPL", "--out-dir", str(raw)])
            self.assertEqual(result, 0)
            self.assertTrue((raw / "conservative_bet_shortlist.csv").exists())
            self.assertTrue((raw / "conservative_strict_qualifiers.csv").exists())
            self.assertTrue((raw / "conservative_bet_rejections.csv").exists())
            self.assertTrue((raw / "conservative_bet_summary.json").exists())
            self.assertEqual(len(list((raw / "shortlist_history").glob("*.csv"))), 1)
            self.assertEqual(
                json.loads((raw / "conservative_bet_summary.json").read_text())[
                    "target_distinct_matches"
                ], 10
            )


if __name__ == "__main__":
    unittest.main()


