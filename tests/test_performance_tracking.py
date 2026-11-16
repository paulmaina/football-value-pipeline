"""Offline regression tests for forward-only football outcome tracking."""

from offline_test_case import OfflineQuotePolicyTestCase
from datetime import datetime, timedelta, timezone
import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import pandas as pd
import requests

from performance_tracking import (
    calibration_buckets, capture, collect_results, fetch_verified,
    fixture_match, frozen_rows, review, score_prediction,
    score_shortlist, snapshots, stats, verified_record,
)


T0 = datetime(2026, 10, 10, 12, 0, tzinfo=timezone.utc)
KICK = datetime(2026, 10, 11, 17, 0, tzinfo=timezone.utc)
SHA = "abacabadabacabadabacabadabacabadabacabad"

def fixture(kickoff=KICK):
    return {
        "league": "Premier League", "home_team": "Manchester City FC",
        "away_team": "Everton FC", "kickoff_utc": kickoff.isoformat(),
        "fixture_id": "event1", "p_home": 0.70, "p_draw": 0.17,
        "p_away": 0.13, "predicted_1x2": "home",
        "p_over_1_5": 0.84, "p_under_3_5": 0.79,
        "p_btts_yes": 0.61, "p_btts_no": 0.39,
    }


def pick(kickoff=KICK, market="Under 3.5", tier="STRICT"):
    return {
        "league": "Premier League", "home_team": "Manchester City FC",
        "away_team": "Everton FC", "kickoff_utc": kickoff.isoformat(),
        "fixture_id": "event1", "market": market,
        "selection_tier": tier,
        "decision": "SHORTLISTED" if tier == "STRICT"
                    else "SHORTLISTED_PROVISIONAL",
        "rank_probability": 0.8, "offered_decimal_odds": 1.5,
    }


def final(status="FINISHED", duration="REGULAR", h=2, a=1):
    return {
        "id": 90002, "utcDate": KICK.isoformat(),
        "status": status, "homeTeam": {
            "name": "Manchester City FC", "shortName": "Man City",
        },
        "awayTeam": {
            "name": "Everton FC", "shortName": "Everton",
        },
        "score": {
            "duration": duration,
            "fullTime": {"home": h, "away": a},
            "regularTime": {"home": 1, "away": 1},
        },
    }


class MockResponse:
    status_code = 200
    def __init__(self, items):
        self.items = items
    def json(self):
        return {"matches": self.items}
    def raise_for_status(self):
        pass


class MockSession:
    def __init__(self, items):
        self.items = items
        self.calls = []
    def get(self, url, *, headers, params, timeout):
        self.calls.append((url, headers, params, timeout))
        return MockResponse(self.items)


class SnapshotTests(OfflineQuotePolicyTestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "football_output_v2"
        raw = self.root / "raw"
        raw.mkdir(parents=True)
        pd.DataFrame([fixture()]).to_csv(raw / "all_leagues_predictions.csv", index=False)
        pd.DataFrame([pick()]).to_csv(raw / "conservative_bet_shortlist.csv", index=False)
        (raw / "conservative_bet_summary.json").write_text(json.dumps({
            "generated_at_utc": (T0-timedelta(minutes=4)).isoformat(),
            "n_shortlisted": 1,
        }), encoding="utf-8")

    def test_archive_immutable_then_grade_verified(self):
        self.assertTrue(capture(SHA, root=self.root, captured_at=T0))
        self.assertFalse(capture(SHA, root=self.root, captured_at=T0))
        archived = snapshots(self.root)
        self.assertEqual(len(archived), 1)
        self.assertEqual(len(frozen_rows(archived, "shortlist")), 1)
        self.assertEqual(len(frozen_rows(archived, "predictions")), 1)
        session = MockSession([final()])
        result = review(
            root=self.root, token="fake-token",
            clock=KICK + timedelta(days=1), session=session,
        )
        self.assertEqual(result["shortlist"]["wins"], 1)
        self.assertEqual(result["shortlist"]["graded"], 1)
        self.assertEqual(result["shortlist"]["flat_stake_roi"], 0.5)
        self.assertEqual(result["prediction_fixtures_graded"], 1)
        self.assertIsNotNone(result["prediction_1x2_multiclass_brier"])
        self.assertEqual(len(session.calls), 1)
        self.assertIn("competitions/PL/matches", session.calls[0][0])
        self.assertEqual(session.calls[0][1], {"X-Auth-Token": "fake-token"})
        self.assertTrue((self.root / "performance" / "weekly" / "2026-W41.md").exists())

    def two_picks_and_a_close(self):
        """Two picks on one match (one per market group) and a Pinnacle near-kickoff quote for it."""
        import closing_odds
        from test_clv_report import observation, quote
        picks = [{**pick(), "value_market_group": "totals"},
                 {**pick(market="Home win"), "offered_decimal_odds": 1.4, "value_market_group": "match_winner"}]
        pd.DataFrame(picks).to_csv(self.root / "raw" / "conservative_bet_shortlist.csv", index=False)
        observed = observation((KICK - timedelta(minutes=4)).isoformat(),
                               [quote("pinnacle", "home", 1.45), quote("pinnacle", "draw", 4.6),
                                quote("pinnacle", "away", 8.0)],
                               {**fixture(), "odds_event_id": "event1"})
        directory = self.root / "closing_odds" / "observations"
        directory.mkdir(parents=True)
        (directory / f"{closing_odds.digest(observed)}.json").write_text(json.dumps(observed), encoding="utf-8")
        self.assertTrue(capture(SHA, root=self.root, captured_at=T0))
        return observed

    def test_report_leads_with_clv_and_adds_one_row_per_fixture(self):
        import clv_report
        observed = self.two_picks_and_a_close()
        result = review(root=self.root, token="fake-token", clock=KICK + timedelta(days=1),
                        session=MockSession([final()]))
        self.assertEqual(result["shortlist"]["graded"], 2)  # the per-pick figures are unchanged
        self.assertAlmostEqual(result["shortlist"]["flat_stake_roi"], 0.45)
        headline = result["headline"]
        fair_home = clv_report.fair_closing_prices(observed["quotes"])["home"]
        self.assertTrue(headline["clv_available"])
        self.assertEqual((headline["picks"], headline["fixtures_with_picks"]), (2, 1))
        self.assertEqual((headline["per_pick"]["return"]["n"], headline["per_fixture"]["return"]["n"]), (2, 1))
        self.assertAlmostEqual(headline["per_fixture"]["return"]["mean"], 0.45)
        # Only the home win has a closing selection in the feed: one CLV, at the frozen 1.4.
        self.assertEqual((headline["per_pick"]["clv"]["n"], headline["per_fixture"]["clv"]["n"]), (1, 1))
        self.assertAlmostEqual(headline["per_pick"]["clv"]["mean"], 1.4 * fair_home - 1)
        self.assertEqual(set(headline["by_week"]), {"2026-W41"})
        self.assertNotIn("fixtures", headline)
        performance = self.root / "performance"
        self.assertEqual(json.loads((performance / "metrics.json").read_text(encoding="utf-8"))["headline"], headline)
        rows = pd.read_csv(performance / "fixture_grades.csv")
        self.assertEqual(list(rows.columns), clv_report.FIXTURE_VIEW_COLUMNS)
        self.assertEqual(rows[["picks", "picks_with_close", "settled_picks"]].iloc[0].tolist(), [2, 1, 2])
        self.assertAlmostEqual(rows.mean_unit_profit.iloc[0], 0.45)
        self.assertAlmostEqual(rows.mean_clv.iloc[0], 1.4 * fair_home - 1)
        readme = (performance / "README.md").read_text(encoding="utf-8")
        lead = readme.index("## Headline: closing-line value first, returns second")
        self.assertLess(lead, readme.index("## Cumulative shortlist"))
        self.assertIn("| per fixture (a match's picks averaged) | 1 |", readme)
        self.assertIn("2 picks on 1 matches", readme)
        self.assertIn("## Gameweeks: closing-line value first, per pick and per fixture", readme)
        self.assertIn("| All selections | 2 | 2-0 | 100.0% | +45.0% |", readme)
        weekly = (performance / "weekly" / "2026-W41.md").read_text(encoding="utf-8")
        self.assertLess(weekly.index("## Closing-line value first, returns second"), weekly.index("## Per-pick results"))
        from workflow_checks import report_check
        self.assertIn(report_check(self.root)["status"], ("VERIFIED", "VERIFIED_WITH_WARNINGS"))

    def test_unreadable_closing_quotes_leave_a_returns_only_headline(self):
        self.two_picks_and_a_close()
        with patch("clv_report.load_closes", side_effect=OSError("unreadable")), self.assertWarnsRegex(
                UserWarning, "closing-line value failed"):
            result = review(root=self.root, token="fake-token", clock=KICK + timedelta(days=1),
                            session=MockSession([final()]))
        self.assertFalse(result["headline"]["clv_available"])
        self.assertEqual(result["headline"]["per_pick"]["clv"]["n"], 0)
        self.assertAlmostEqual(result["headline"]["per_fixture"]["return"]["mean"], 0.45)
        readme = (self.root / "performance" / "README.md").read_text(encoding="utf-8")
        self.assertIn("Closing-line value is unavailable in this review", readme)

    def test_late_capture_never_counts_as_forward_prediction(self):
        time = KICK + timedelta(hours=3)
        self.assertFalse(capture(SHA, root=self.root, captured_at=time))
        self.assertFalse((self.root / "performance" / "snapshots").exists())

    def test_late_snapshot_row_excluded_even_if_another_fixture_qualifies(self):
        row2 = fixture(KICK + timedelta(days=4))
        frame = pd.DataFrame([fixture(), row2])
        frame.to_csv(self.root / "raw" / "all_leagues_predictions.csv", index=False)
        self.assertTrue(capture(
            SHA, root=self.root, captured_at=KICK + timedelta(hours=3)
        ))
        future = frozen_rows(snapshots(self.root), "predictions")
        self.assertEqual(len(future), 1)
        self.assertEqual(future[0]["kickoff_utc"], row2["kickoff_utc"])

    def test_archive_tampering_is_detected_and_excluded(self):
        self.assertTrue(capture(SHA, root=self.root, captured_at=T0))
        path = self.root / "performance" / "snapshots" / SHA[:16] / "shortlist.csv"
        path.write_text("fixture,market\nhacked,Under 3.5")
        with self.assertWarnsRegex(UserWarning, "Tampered"):
            self.assertEqual(len(snapshots(self.root)), 0)

    def test_no_token_produces_pending_not_fictitious_wins(self):
        capture(SHA, root=self.root, captured_at=T0)
        result = review(
            root=self.root, token="",
            clock=KICK + timedelta(days=1),
        )
        self.assertEqual(result["shortlist"]["graded"], 0)
        self.assertEqual(result["shortlist"]["pending"], 1)
        self.assertIsNone(result["shortlist"]["win_rate"])
        self.assertIn("configuration", result["provider_errors"])

    def test_repeated_snapshot_does_not_duplicate_fixture_across_commits(self):
        capture(SHA, root=self.root, captured_at=T0)
        capture("c"*40, root=self.root, captured_at=T0+timedelta(minutes=10))
        self.assertEqual(len(frozen_rows(snapshots(self.root), "shortlist")), 1)


class ResultsAndMarketsTests(OfflineQuotePolicyTestCase):
    def test_provider_finished_regulation_goals_only(self):
        standard = verified_record("PL", final())
        self.assertEqual((standard["home_goals"], standard["away_goals"]), (2, 1))
        self.assertIsNone(verified_record("PL", final(status="IN_PLAY")))
        knockout = verified_record("CL", final(duration="EXTRA_TIME", h=3, a=2))
        self.assertEqual((knockout["home_goals"], knockout["away_goals"]), (1, 1))
        knockout_missing = final(duration="PENALTY_SHOOTOUT")
        knockout_missing["score"]["regularTime"] = None
        self.assertIsNone(verified_record("CL", knockout_missing))
        missing_goals = final()
        missing_goals["score"]["fullTime"]["away"] = None
        self.assertIsNone(verified_record("PL", missing_goals))

    def test_match_verification_checks_teams_and_competition(self):
        row = fixture()
        self.assertEqual(fixture_match(row, [verified_record("PL", final())])[1],
                         "VERIFIED_FINISHED")
        self.assertEqual(fixture_match(row, [verified_record("PD", final())])[1],
                         "UNVERIFIED_FIXTURE_OR_RESULT")
        wrong_teams = final()
        wrong_teams["awayTeam"]["name"] = "Arsenal FC"
        wrong_teams["awayTeam"]["shortName"] = "Arsenal"
        self.assertEqual(fixture_match(row, [verified_record("PL", wrong_teams)])[1],
                         "UNVERIFIED_FIXTURE_OR_RESULT")

    def test_ambiguous_results_must_not_be_graded(self):
        a = verified_record("PL", final())
        b = dict(a)
        b["match_id"] = 90003
        self.assertEqual(fixture_match(fixture(), [a, b])[1], "AMBIGUOUS_FIXTURE")

    def test_market_results_and_roi(self):
        record = verified_record("PL", final())
        base = {
            **pick(), "fixture_key": "unique", "snapshot_commit": SHA,
            "snapshot_captured_utc": T0.isoformat(),
            "predicted_probability": 0.8,
        }
        for market, expected in [
            ("Home win", "WON"), ("Away win", "LOST"),
            ("Over 1.5", "WON"), ("Under 3.5", "WON"),
            ("Both Teams to Score - Yes", "WON"),
        ]:
            row = score_shortlist({**base, "market": market},
                                  record, "VERIFIED_FINISHED")
            self.assertEqual(row["status"], expected)
            self.assertEqual(row["unit_profit"], 0.5 if expected=="WON" else -1)
            self.assertIsInstance(row["brier"], float)
        scored = score_shortlist({**base, "market": "Unknown"},
                                 record, "VERIFIED_FINISHED")
        self.assertEqual(scored["status"], "UNSUPPORTED_MARKET")
        self.assertEqual(stats([scored])["graded"], 0)

    def test_calibration_bins_compare_frozen_chance_to_outcomes(self):
        inputs = [
            {"status": "WON", "predicted_probability": 0.82},
            {"status": "LOST", "predicted_probability": 0.88},
            {"status": "UNVERIFIED_FIXTURE_OR_RESULT",
             "predicted_probability": 0.99},
        ]
        bins = calibration_buckets(inputs)
        self.assertEqual(len(bins), 1)
        self.assertEqual(bins[0]["probability_band"], "80%–90%")
        self.assertEqual(bins[0]["n"], 2)
        self.assertEqual(bins[0]["observed_win_rate"], 0.5)
        self.assertAlmostEqual(bins[0]["mean_forecast"], 0.85)

    def test_missing_bookmaker_odds_does_not_invent_profit(self):
        record = verified_record("PL", final())
        base = {
            **pick(), "fixture_key": "unique", "snapshot_commit": SHA,
            "snapshot_captured_utc": T0.isoformat(),
            "offered_decimal_odds": "",
        }
        scored = score_shortlist(base, record, "VERIFIED_FINISHED")
        self.assertEqual(scored["status"], "WON")
        self.assertEqual(scored["unit_profit"], "")
        self.assertIsNone(stats([scored])["flat_stake_roi"])

    def test_prediction_1x2_and_market_outcome_metrics(self):
        record = verified_record("PL", final())
        base = {**fixture(), "fixture_key": "unique", "snapshot_commit": SHA}
        scored = score_prediction(base, record, "VERIFIED_FINISHED")
        self.assertEqual(scored["status"], "GRADED")
        self.assertEqual(scored["one_x_two_correct"], 1)
        self.assertEqual(scored["over_1_5_correct"], 1)
        self.assertEqual(scored["under_3_5_correct"], 1)
        self.assertEqual(scored["btts_yes_correct"], 1)

    def test_api_collects_only_verified_matches(self):
        session = MockSession([final(), final(status="SCHEDULED")])
        found = fetch_verified(
            "test-token", "PL", "2026-10-09", "2026-10-13", session=session,
        )
        self.assertEqual(len(found), 1)
        self.assertEqual(found[0]["match_id"], 90002)


if __name__ == "__main__":
    unittest.main()
