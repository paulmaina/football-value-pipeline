"""1X2 and O/U 2.5 de-vig reference: fresh Pinnacle, else lowest margin (audit D5).

The reference used to be whichever book updated last, so Pinnacle was the
reference in only 7.8% of rows and 11.8% used a book with >10% margin.
"""
from offline_test_case import OfflineQuotePolicyTestCase
from datetime import datetime, timedelta, timezone
import unittest

from football_value_pipeline_v2_standalone import TheOddsAPI, market_snapshot
import pandas as pd


NOW = datetime(2026, 10, 27, 12, 0, tzinfo=timezone.utc)


def book(key, minutes_old, home, draw, away, over, under):
    stamp = (NOW - timedelta(minutes=minutes_old)).isoformat()
    return {"key": key, "title": key.title(), "last_update": stamp, "markets": [
        {"key": "h2h", "last_update": stamp, "outcomes": [
            {"name": "Home", "price": home}, {"name": "Draw", "price": draw}, {"name": "Away", "price": away}]},
        {"key": "totals", "last_update": stamp, "outcomes": [
            {"name": "Over", "point": 2.5, "price": over}, {"name": "Under", "point": 2.5, "price": under}]}]}


def event(*books):
    return {"id": "e1", "home_team": "Home", "away_team": "Away",
            "commence_time": (NOW + timedelta(hours=6)).isoformat(), "bookmakers": list(books)}


# Overrounds: soft 1X2 1.087 / O/U 1.077; sharp 1.020 / 1.015; pinnacle 1.035 / 1.030.
SOFT_NEWEST = ("softbook", 1, 2.00, 3.30, 3.60, 1.80, 1.92)
SHARP = ("sharpbook", 30, 2.12, 3.55, 3.85, 1.95, 1.99)
PINNACLE = ("pinnacle", 60, 2.08, 3.50, 3.80, 1.92, 1.96)


class ReferenceBookTests(OfflineQuotePolicyTestCase):
    def test_fresh_pinnacle_is_preferred_over_newer_and_lower_margin_books(self):
        flat = TheOddsAPI.flatten_odds_event(event(book(*SOFT_NEWEST), book(*SHARP), book(*PINNACLE)), as_of=NOW)
        self.assertEqual(flat["live_ref_1x2_bookmaker"], "Pinnacle")
        self.assertEqual(flat["live_ref_ou25_bookmaker"], "Pinnacle")
        self.assertEqual((flat["live_ref_home_odds"], flat["live_ref_over_2_5_odds"]), (2.08, 1.92))
        snapshot = market_snapshot(pd.Series({**flat, "odds_source": "The Odds API"}))
        self.assertEqual(snapshot["market_source_1x2"], "The Odds API / Pinnacle")
        self.assertEqual(snapshot["market_source_ou25"], "The Odds API / Pinnacle")

    def test_without_pinnacle_the_lowest_margin_book_wins_not_the_newest(self):
        flat = TheOddsAPI.flatten_odds_event(event(book(*SOFT_NEWEST), book(*SHARP)), as_of=NOW)
        self.assertEqual(flat["live_ref_1x2_bookmaker"], "Sharpbook")
        self.assertEqual(flat["live_ref_ou25_bookmaker"], "Sharpbook")

    def test_stale_pinnacle_is_never_the_reference(self):
        stale = ("pinnacle", 60 * 25, *PINNACLE[2:])
        flat = TheOddsAPI.flatten_odds_event(event(book(*SOFT_NEWEST), book(*SHARP), book(*stale)), as_of=NOW)
        self.assertEqual(flat["live_ref_1x2_bookmaker"], "Sharpbook")
        self.assertEqual(flat["live_ref_ou25_bookmaker"], "Sharpbook")

    def test_equal_margins_fall_back_to_newest_then_name(self):
        older = ("bookb", 20, *SHARP[2:])
        newer = ("booka", 5, *SHARP[2:])
        flat = TheOddsAPI.flatten_odds_event(event(book(*older), book(*newer)), as_of=NOW)
        self.assertEqual(flat["live_ref_1x2_bookmaker"], "Booka")
        same_time = ("bookc", 5, *SHARP[2:])
        flat = TheOddsAPI.flatten_odds_event(event(book(*same_time), book(*newer)), as_of=NOW)
        self.assertEqual(flat["live_ref_1x2_bookmaker"], "Bookc")

    def test_structural_parsing_without_a_clock_uses_the_same_rule(self):
        flat = TheOddsAPI.flatten_odds_event(event(book(*SOFT_NEWEST), book(*SHARP), book(*PINNACLE)))
        self.assertEqual(flat["live_ref_1x2_bookmaker"], "Pinnacle")
        flat = TheOddsAPI.flatten_odds_event(event(book(*SOFT_NEWEST), book(*SHARP)))
        self.assertEqual(flat["live_ref_1x2_bookmaker"], "Sharpbook")


if __name__ == "__main__":
    unittest.main()
