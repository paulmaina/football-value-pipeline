"""Offline validation of market-specific risk gates and fair odds quotas."""

from offline_test_case import OfflineQuotePolicyTestCase
import unittest
from datetime import datetime, timedelta, timezone

import numpy as np
import pandas as pd

from goal_market_validation import (
    distribute_event_odds_budget, prioritized_additional_events,
    paired_opening_price, enrich_historical_goal_markets,
    evaluate_market_history,
)
from conservative_bet_filter import build_conservative_shortlist
from test_conservative_bet_filter import NOW, fixture


def historical(n=200, p=0.8, observed=0.8):
    dates = [f"2024-01-{1+i//6:02d}" for i in range(n)]
    rows = []
    for i in range(n):
        outcome = int((i % 10) < round(10 * observed))
        rows.append({
            "date": dates[i],
            "p_home": 0.5, "raw_p_home": 0.5,
            "actual_home": i % 2,
            "p_away": 0.25, "raw_p_away": 0.25,
            "actual_away": (i + 1) % 2,
            "p_over_1_5": p, "raw_p_over_1_5": p,
            "actual_over_1_5": outcome,
            "p_under_3_5": p, "raw_p_under_3_5": p,
            "actual_under_3_5": outcome,
            "p_btts_yes": p, "raw_p_btts_yes": p,
            "actual_btts_yes": outcome,
        })
    # Simple ascending chronological day labels in YYYY-MM-DD, including
    # more than 31 days for larger fixtures, via Timestamp arithmetic.
    for i, row in enumerate(rows):
        row["date"] = (
            pd.Timestamp("2024-01-01") + pd.Timedelta(days=i//6)
        ).date().isoformat()
    return pd.DataFrame(rows)


class MarketValidationTests(OfflineQuotePolicyTestCase):
    def test_fair_24_calls_split_across_all_six_competitions(self):
        allocation = distribute_event_odds_budget(
            ["EPL", "LaLiga", "Bundesliga", "SerieA", "Ligue1", "UCL"], 24
        )
        self.assertEqual(allocation, {
            "EPL": 4, "LaLiga": 4, "Bundesliga": 4,
            "SerieA": 4, "Ligue1": 4, "UCL": 4,
        })
        self.assertEqual(sum(allocation.values()), 24)
        self.assertEqual(distribute_event_odds_budget(["SerieA"], 24), {"SerieA": 24})
        self.assertEqual(distribute_event_odds_budget(["UCL"], 24), {"UCL": 24})

    def test_prioritize_best_eligible_fixture_not_first_upcoming(self):
        def item(i, p):
            fixture_row = {
                "odds_source": "The Odds API",
                "odds_event_id": f"event{i}",
            }
            model = {
                "home_name_match_score": 98,
                "away_name_match_score": 96,
                "p_over_1_5": p,
                "raw_p_over_1_5": p,
                "p_under_3_5": 0.2,
                "raw_p_under_3_5": 0.2,
                "p_btts_yes": 0.3,
                "raw_p_btts_yes": 0.3,
            }
            return (fixture_row, model)
        chosen = prioritized_additional_events(
            [item(0,0.79), item(1,0.94), item(2,0.85)], 2
        )
        self.assertEqual(chosen, [1, 2])

    def test_offline_real_historical_walk_forward_includes_goal_markets(self):
        """Exercise real fitting + outcome extraction from committed EPL CSV."""
        from pathlib import Path
        from unittest.mock import patch
        from football_value_pipeline_v2_standalone import FootballValuePipelineV2

        root = Path(__file__).resolve().parent.parent
        sources = [
            root / ".football_cache" / "2526_E0.csv",
            root / ".football_cache" / "2627_E0.csv",
        ]
        hist = pd.concat([pd.read_csv(path, low_memory=False)
                          for path in sources], ignore_index=True)
        hist["Date"] = pd.to_datetime(hist["Date"], dayfirst=True, errors="coerce")
        for key in ("FTHG", "FTAG"):
            hist[key] = pd.to_numeric(hist[key], errors="coerce")
        hist = hist.dropna(subset=["Date", "HomeTeam", "AwayTeam", "FTHG", "FTAG"])
        hist = hist.sort_values("Date").reset_index(drop=True)
        pipe = FootballValuePipelineV2(live_odds=False)
        with patch.object(pipe, "_history_for_league", return_value=hist):
            actual, _, _, _ = pipe.backtest_league(
                "EPL", min_train=200, step_days=150
            )
        self.assertGreater(len(actual), 40)
        for key in ("p_over_1_5", "p_under_3_5", "p_btts_yes",
                    "raw_p_over_1_5", "actual_under_3_5",
                    "historical_open_btts_yes_odds"):
            self.assertIn(key, actual.columns)
        evaluation = evaluate_market_history(
            actual, "Premier League", min_dev=40, min_audit=15
        )
        self.assertGreater(
            evaluation["markets"]["under_3_5"]["audit"]["n"], 15
        )
        self.assertEqual(
            evaluation["markets"]["btts_yes"]["historical_betting"]["status"],
            "UNAVAILABLE_NO_HISTORICAL_PRICES"
        )

    def test_high_probability_evidence_has_counts_rate_and_wilson_interval(self):
        report = evaluate_market_history(
            historical(n=240, p=0.91, observed=0.9), "Premier League"
        )
        group = report["markets"]["over_1_5"]["high_confidence"]["85plus"]
        self.assertEqual(group["status"], "PASSED")
        self.assertGreaterEqual(group["development"]["n"], 30)
        self.assertGreaterEqual(group["audit"]["n"], 12)
        lo, hi = group["audit"]["observed_wilson95"]
        self.assertLessEqual(lo, group["audit"]["observed_rate"])
        self.assertGreaterEqual(hi, group["audit"]["observed_rate"])
        self.assertIsNotNone(group["development_only_penalty"])

    def test_sparse_85percent_history_is_not_assumed_reliable(self):
        report = evaluate_market_history(historical(p=0.80), "Premier League")
        over = report["markets"]["over_1_5"]
        self.assertEqual(over["high_confidence"]["75plus"]["status"], "PASSED")
        self.assertEqual(over["high_confidence"]["85plus"]["status"],
                         "INSUFFICIENT_HIGH_CONFIDENCE_HISTORY")
        row = fixture()
        picks, audit, summary = build_conservative_shortlist(
            pd.DataFrame([row]), as_of=NOW,
            market_reliability={"Premier League": report},
        )
        chosen_market = audit.loc[audit["market"] == "Over 1.5"].iloc[0]
        self.assertEqual(chosen_market["high_confidence_tier"], "85plus")
        self.assertEqual(chosen_market["decision"], "REJECTED")
        self.assertIn("INSUFFICIENT_HIGH_CONFIDENCE_HISTORY",
                      chosen_market["rejection_reasons"])

    def test_overconfident_high_group_is_explicitly_rejected(self):
        report = evaluate_market_history(
            historical(n=240, p=0.91, observed=0.6), "Premier League"
        )
        group = report["markets"]["under_3_5"]["high_confidence"]["85plus"]
        self.assertEqual(group["status"], "HIGH_CONFIDENCE_OVERESTIMATION")
        self.assertGreater(group["audit"]["overconfidence"], 0.1)

    def test_audit_changes_do_not_train_high_confidence_penalty(self):
        hist = historical(n=240, p=0.88, observed=0.7)
        first = evaluate_market_history(hist, "Premier League")
        tampered = hist.copy()
        tampered.loc[tampered.index[-25:], "actual_under_3_5"] = 1
        second = evaluate_market_history(tampered, "Premier League")
        self.assertEqual(
            first["markets"]["under_3_5"]["high_confidence"]["85plus"][
                "development_only_penalty"
            ],
            second["markets"]["under_3_5"]["high_confidence"]["85plus"][
                "development_only_penalty"
            ],
        )

    def test_passing_85plus_subgroup_carries_audit_evidence_into_shortlist(self):
        report = evaluate_market_history(
            historical(n=240, p=0.9, observed=0.9), "Premier League"
        )
        row = fixture()
        picks, audit, summary = build_conservative_shortlist(
            pd.DataFrame([row]), as_of=NOW,
            market_reliability={"Premier League": report},
        )
        group = audit.loc[audit["market"] == "Over 1.5"].iloc[0]
        self.assertEqual(group["high_confidence_status"], "PASSED")
        self.assertGreaterEqual(group["high_confidence_audit_matches"], 12)
        self.assertTrue(0 <= group["high_confidence_wilson95_lower"] <= 1)
        self.assertEqual(summary["target_distinct_matches"], 10)

    def test_actual_outcomes_come_from_match_scores(self):
        prediction = {"p_over_1_5":0.75, "raw_p_over_1_5":0.73,
                      "p_under_3_5":0.8, "raw_p_under_3_5":0.78,
                      "p_btts_yes":0.71, "raw_p_btts_yes":0.70}
        result = enrich_historical_goal_markets(
            {"FTHG":2,"FTAG":1}, prediction
        )
        self.assertEqual(result["actual_over_1_5"], 1)
        self.assertEqual(result["actual_under_3_5"], 1)
        self.assertEqual(result["actual_btts_yes"], 1)
        self.assertIsNone(result["historical_open_under_3_5_odds"])

    def test_real_historical_price_must_have_same_book_opposite(self):
        self.assertIsNone(paired_opening_price({"B365<3.5":1.4}, "under_3_5"))
        self.assertEqual(paired_opening_price(
            {"B365<3.5":1.4,"B365>3.5":2.9},"under_3_5"
        ), 1.4)

    def test_market_validation_has_chronological_dev_and_audit(self):
        data = historical()
        r = evaluate_market_history(data, "Premier League")
        under = r["markets"]["under_3_5"]
        self.assertGreater(under["development"]["n"], 80)
        self.assertGreater(under["audit"]["n"], 25)
        self.assertEqual(under["status"], "RELIABLE_FOR_RANKING")
        self.assertIsInstance(under["audit"]["brier"], float)
        self.assertTrue(under["development_bins"])
        self.assertEqual(under["historical_betting"]["status"],
                         "UNAVAILABLE_NO_HISTORICAL_PRICES")
        self.assertIsNone(under["historical_betting"]["roi_per_unit"])

    def test_audit_label_changes_cannot_fit_development_penalty(self):
        hist = historical(observed=0.6)
        first = evaluate_market_history(hist, "Premier League")
        alt = hist.copy()
        alt.loc[alt.index[-30:], "actual_under_3_5"] = 1
        second = evaluate_market_history(alt, "Premier League")
        self.assertAlmostEqual(
            first["markets"]["under_3_5"]["confidence_penalty"],
            second["markets"]["under_3_5"]["confidence_penalty"],
        )

    def test_market_price_returns_only_when_recorded(self):
        data = historical()
        data["historical_open_under_3_5_odds"] = 1.5
        result = evaluate_market_history(data, "Premier League")
        bet = result["markets"]["under_3_5"]["historical_betting"]
        self.assertEqual(bet["status"], "SIMULATED_AT_RECORDED_OPENING_PRICES")
        self.assertEqual(bet["n_quotes"], 200)
        self.assertGreater(bet["n_simulated"], 0)
        self.assertIsInstance(bet["roi_per_unit"], float)

    def test_unreliable_audit_vetoes_candidate(self):
        candidate = fixture()
        report = evaluate_market_history(historical(), "Premier League")
        report["markets"]["over_1_5"]["status"] = "UNRELIABLE_AUDIT"
        for key in ("home", "away", "under_3_5", "btts_yes"):
            report["markets"][key]["status"] = "UNRELIABLE_AUDIT"
        picks, decisions, _ = build_conservative_shortlist(
            pd.DataFrame([candidate]), as_of=NOW,
            market_reliability={"Premier League": report},
        )
        self.assertTrue(picks.empty)
        self.assertIn("market historical reliability", " ".join(decisions.rejection_reasons))

    def test_development_penalty_reduces_rank_probability_and_ev(self):
        report = evaluate_market_history(historical(), "Premier League")
        for v in report["markets"].values():
            v["status"] = "RELIABLE_FOR_RANKING"
            v["confidence_penalty"] = 0.03
        picks, decisions, summary = build_conservative_shortlist(
            pd.DataFrame([fixture()]), as_of=NOW,
            market_reliability={"Premier League": report},
        )
        self.assertTrue(summary["validation_required"])
        selected = decisions.loc[decisions["market"] == "Over 1.5"].iloc[0]
        self.assertAlmostEqual(
            selected["rank_probability"],
            selected["predicted_probability"] - 0.03,
        )
        self.assertLess(selected["conservative_estimated_ev"],
                        selected["estimated_ev"])


if __name__ == "__main__":
    unittest.main()

