"""Pinnacle O/U 2.5 anchor uses the per-event alternate line (audit M2).

Pinnacle's main totals line is 2.5 for only ~15% of events, but its
alternate_totals in the per-event response carry 2.5 for ~95%.
"""
from offline_test_case import OfflineQuotePolicyTestCase
from datetime import datetime, timedelta, timezone
import unittest
from types import SimpleNamespace
from unittest.mock import Mock, patch

import pandas as pd

from football_value_pipeline_v2_standalone import FootballValuePipelineV2, TheOddsAPI, pinnacle_ou25_reference
from tests.test_model_upgrades_v1 import NOW, live_row, pinnacle_totals, pipe, toy_model


def stamp(minutes_old):
    return (NOW - timedelta(minutes=minutes_old)).isoformat().replace("+00:00", "Z")


def event_payload(books, event="ev1"):
    return {"id": event, "home_team": "A", "away_team": "B",
            "commence_time": (NOW + timedelta(hours=5)).isoformat(), "bookmakers": books}


def book(key, outcomes, market="alternate_totals", minutes_old=3):
    return {"key": key, "title": key.title(), "last_update": stamp(minutes_old),
            "markets": [{"key": market, "last_update": stamp(minutes_old), "outcomes": outcomes}]}


def totals(*pairs):
    return [{"name": side, "point": point, "price": price}
            for point, over, under in pairs for side, price in (("Over", over), ("Under", under))]


class AlternateQuoteParsingTests(OfflineQuotePolicyTestCase):
    def test_exact_pinnacle_2_5_pair_is_extracted(self):
        payload = event_payload([
            book("onexbet", totals((2.5, 1.70, 2.20))),
            book("pinnacle", totals((2.25, 1.60, 2.40), (2.5, 1.85, 2.05), (2.75, 2.10, 1.80))),
        ])
        quote = TheOddsAPI._pinnacle_alternate_ou25(payload)
        self.assertEqual((quote["over"], quote["under"]), (1.85, 2.05))
        self.assertEqual((quote["bookmaker"], quote["event_id"]), ("pinnacle", "ev1"))
        self.assertEqual(quote["updated_at_utc"], stamp(3))

    def test_incomplete_duplicate_or_other_book_quotes_are_rejected(self):
        cases = {
            "other book only": [book("onexbet", totals((2.5, 1.85, 2.05)))],
            "no 2.5": [book("pinnacle", totals((2.25, 1.60, 2.40)))],
            "one side": [book("pinnacle", totals((2.5, 1.85, 2.05))[:1])],
            "duplicate": [book("pinnacle", totals((2.5, 1.85, 2.05), (2.5, 1.90, 2.00)))],
            "invalid price": [book("pinnacle", totals((2.5, 1.0, 2.05)))],
        }
        for name, books in cases.items():
            with self.subTest(name):
                self.assertIsNone(TheOddsAPI._pinnacle_alternate_ou25(event_payload(books)))

    def test_main_market_records_which_lines_pinnacle_quoted(self):
        event = event_payload([book("pinnacle", totals((3.0, 1.95, 1.90)), market="totals")])
        flat = TheOddsAPI.flatten_odds_event(event, as_of=NOW)
        self.assertIsNone(flat["shadow_pinnacle_totals"])
        self.assertEqual(flat["pinnacle_totals_lines"]["lines"], [3.0])
        stale = event_payload([book("pinnacle", totals((2.5, 1.95, 1.90)), market="totals", minutes_old=60 * 25)])
        flat = TheOddsAPI.flatten_odds_event(stale, as_of=NOW)
        self.assertIsNone(flat["shadow_pinnacle_totals"])
        self.assertEqual(flat["pinnacle_totals_lines"]["lines"], [2.5])


class AnchorStatusTests(OfflineQuotePolicyTestCase):
    def alternate(self, minutes_old=3, event="ev1", over=1.85, under=2.05):
        return dict(pinnacle_totals(minutes_old, event), over=over, under=under)

    def lines(self, minutes_old=3, lines=(3.0,)):
        return {"lines": list(lines), "updated_at_utc": stamp(minutes_old)}

    def test_statuses(self):
        cases = {
            "ANCHORED_MAIN": live_row(shadow_pinnacle_totals=pinnacle_totals(),
                                      pinnacle_alternate_ou25=self.alternate()),
            "ANCHORED_ALTERNATE": live_row(pinnacle_totals_lines=self.lines(),
                                           pinnacle_alternate_ou25=self.alternate()),
            "NOT_ANCHORED_STALE": live_row(pinnacle_totals_lines=self.lines(60 * 25)),
            "NOT_ANCHORED_PINNACLE_NO_2_5_LINE": live_row(pinnacle_totals_lines=self.lines()),
            "NOT_ANCHORED_NO_PINNACLE": live_row(),
            "NOT_ANCHORED_PINNACLE_EVENT_MISMATCH": live_row(
                pinnacle_totals_lines=self.lines(), pinnacle_alternate_ou25=self.alternate(event="other")),
        }
        for status, row in cases.items():
            with self.subTest(status):
                self.assertEqual(pinnacle_ou25_reference(row, NOW)[1], status)

    def test_stale_main_falls_back_to_fresh_alternate(self):
        row = live_row(shadow_pinnacle_totals=pinnacle_totals(minutes_old=60 * 25),
                       pinnacle_alternate_ou25=self.alternate())
        ref, status = pinnacle_ou25_reference(row, NOW)
        self.assertEqual(status, "ANCHORED_ALTERNATE")
        self.assertEqual((ref["over"], ref["under"], ref["source"]), (1.85, 2.05, "live_pinnacle_alternate"))
        both_stale = live_row(shadow_pinnacle_totals=pinnacle_totals(minutes_old=60 * 25),
                              pinnacle_alternate_ou25=self.alternate(minutes_old=60 * 25))
        self.assertEqual(pinnacle_ou25_reference(both_stale, NOW), (None, "NOT_ANCHORED_STALE"))

    def test_alternate_anchor_applies_the_same_method_as_main(self):
        main, _ = pipe()._predict_row(toy_model(), live_row(shadow_pinnacle_totals=pinnacle_totals()))
        alternate, _ = pipe()._predict_row(toy_model(), live_row(
            pinnacle_totals_lines=self.lines(), pinnacle_alternate_ou25=self.alternate(over=1.80, under=2.10)))
        self.assertEqual(main["totals_anchor_status"], "ANCHORED_MAIN")
        self.assertEqual(alternate["totals_anchor_status"], "ANCHORED_ALTERNATE")
        self.assertTrue(alternate["totals_anchor_applied"])
        for field in ("p_home", "p_draw", "p_away", "p_over_2_5", "p_under_3_5", "p_btts_yes",
                      "totals_anchor_scale", "totals_anchor_target_over_2_5"):
            self.assertEqual(main[field], alternate[field], field)


class RunLeagueAlternateAnchorTests(OfflineQuotePolicyTestCase):
    def run_pipeline(self, extra):
        pipeline = object.__new__(FootballValuePipelineV2)
        for key, value in dict(half_life_days=480, l2=0.08, max_goals=10, devig_method="power",
                market_weight=0.7, totals_anchor=True, fixture_provider="auto", odds_regions="eu",
                extra_event_odds_requests=0, max_extra_event_odds_requests=24,
                extra_event_odds_quota={"UCL": 4}, extra_event_odds_by_league={},
                additional_odds_coverage="all").items():
            setattr(pipeline, key, value)
        pipeline._training_health = Mock(return_value={"status": "OFFLINE_TEST"})
        pipeline._history_for_league = Mock(return_value=pd.DataFrame(
            columns=["Date", "HomeTeam", "AwayTeam", "FTHG", "FTAG"]))
        kickoff = (NOW + timedelta(hours=5)).isoformat()
        pipeline._current_fixtures = Mock(return_value=pd.DataFrame([dict(
            Date=pd.Timestamp(kickoff[:10]), kickoff_utc=kickoff, HomeTeam="A", AwayTeam="B",
            odds_source="The Odds API", odds_event_id="ev1")]))
        pipeline._attach_live_odds = lambda fixtures, *args: fixtures
        seen = []
        def predict(model, row):
            alternate = row.get("pinnacle_alternate_ou25")
            seen.append(alternate)
            status = "ANCHORED_ALTERNATE" if alternate else "NOT_ANCHORED_PINNACLE_NO_2_5_LINE"
            return dict(home_name_match_score=100, away_name_match_score=100,
                        totals_anchor_status=status, legacy_p_home=None), {"1-0": 0.1}
        pipeline._predict_row = predict
        pipeline._legacy_columns = Mock(return_value={"legacy_p_home": 0.4})
        pipeline.legacy_comparison = True
        pipeline._fit_legacy_model = Mock(return_value=(None, "OFFLINE"))
        pipeline.odds_api = Mock()
        pipeline.odds_api.extra_markets_for_event.return_value = extra
        model = SimpleNamespace(training_matches=100, training_end=None, fit_result=None,
                                base=0, home_adv=0, rho=0, half_life_days=480, max_goals=10)
        with patch("football_value_pipeline_v2_standalone.DixonColesModel") as model_class:
            model_class.return_value.fit.return_value = model
            frame, diagnostics, _ = pipeline.run_league("UCL", NOW)
        return seen, frame, diagnostics

    def identity(self, home="A"):
        return {"home_team": home, "away_team": "B",
                "commence_time": (NOW + timedelta(hours=5)).isoformat()}

    def test_fixture_is_anchored_after_the_per_event_request(self):
        quote = dict(pinnacle_totals(), over=1.85, under=2.05)
        seen, frame, diagnostics = self.run_pipeline(
            {"pinnacle_alternate_ou25": quote, "_asian_handicap_identity": self.identity()})
        self.assertEqual(seen, [None, quote])
        self.assertEqual(frame["totals_anchor_status"].tolist(), ["ANCHORED_ALTERNATE"])
        self.assertEqual(diagnostics["totals_anchor_fixtures"], {"ANCHORED_ALTERNATE": 1})
        self.assertNotIn("pinnacle_alternate_ou25", frame.columns)
        self.assertEqual(frame["legacy_p_home"].tolist(), [0.4])

    def test_rejected_event_identity_never_anchors(self):
        quote = dict(pinnacle_totals(), over=1.85, under=2.05)
        seen, frame, _ = self.run_pipeline(
            {"pinnacle_alternate_ou25": quote, "_asian_handicap_identity": self.identity("Other")})
        self.assertEqual(seen, [None])
        self.assertEqual(frame["totals_anchor_status"].tolist(), ["NOT_ANCHORED_PINNACLE_NO_2_5_LINE"])


if __name__ == "__main__":
    unittest.main()
