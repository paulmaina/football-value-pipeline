"""Odds API caches are fresh only by their recorded fetch time (audit D4).

A git checkout sets every committed cache file's mtime to "now", so mtime
cannot show when the response was fetched. Already-played fixtures must
never reach prediction.
"""
from offline_test_case import OfflineQuotePolicyTestCase
from datetime import datetime, timedelta, timezone
import json
import os
from pathlib import Path
import tempfile
import unittest
from types import SimpleNamespace
from unittest.mock import Mock, patch

import pandas as pd
import requests

from football_value_pipeline_v2_standalone import LEAGUES, FootballValuePipelineV2, TheOddsAPI


KEYS = {"THE_ODDS_API_KEY": "primary-secret-for-tests"}
EVENT = {"id": "event1", "home_team": "Arsenal", "away_team": "Chelsea",
         "commence_time": "2026-10-28T19:00:00Z"}
OLD_EVENT = {"id": "old1", "home_team": "Everton", "away_team": "Fulham",
             "commence_time": "2026-10-24T14:00:00Z"}


def response(payload):
    result = requests.Response()
    result.status_code = 200
    result._content = json.dumps(payload).encode("utf-8")
    return result


class OddsCacheFreshnessTests(OfflineQuotePolicyTestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.cache = Path(self.tmp.name)
        self.api = TheOddsAPI(KEYS["THE_ODDS_API_KEY"], cache_dir=self.cache)
        self.api.http.session.get = self.get = Mock(return_value=response([EVENT]))
        env = patch.dict(os.environ, KEYS, clear=True)
        env.start()
        self.addCleanup(env.stop)

    def events(self, now):
        return self.api.events(LEAGUES["EPL"], 3, now)

    def test_checked_out_cache_without_fetch_time_is_refetched(self):
        # Pre-fix format: a bare provider payload whose mtime a checkout just reset.
        path = self.cache / "oddsapi_events_EPL.json"
        path.write_text(json.dumps([OLD_EVENT]), encoding="utf-8")
        os.utime(path, None)
        frame = self.events(datetime.now(timezone.utc))
        self.assertEqual(self.get.call_count, 1)
        self.assertEqual(frame["fixture_id"].tolist(), ["event1"])

    def test_cache_with_old_fetch_time_is_refetched_despite_new_mtime(self):
        now = datetime.now(timezone.utc)
        start, end = TheOddsAPI._window(now, 3)
        path = self.cache / "oddsapi_events_EPL.json"
        path.write_text(json.dumps({
            "fetched_at_utc": (now - timedelta(days=2)).isoformat(),
            "request": {"commenceTimeFrom": start, "commenceTimeTo": end},
            "payload": [OLD_EVENT]}), encoding="utf-8")
        os.utime(path, None)
        frame = self.events(now)
        self.assertEqual(self.get.call_count, 1)
        self.assertEqual(frame["fixture_id"].tolist(), ["event1"])

    def test_future_fetch_time_is_not_fresh(self):
        now = datetime.now(timezone.utc)
        start, end = TheOddsAPI._window(now, 3)
        (self.cache / "oddsapi_events_EPL.json").write_text(json.dumps({
            "fetched_at_utc": (now + timedelta(hours=1)).isoformat(),
            "request": {"commenceTimeFrom": start, "commenceTimeTo": end},
            "payload": [OLD_EVENT]}), encoding="utf-8")
        self.events(now)
        self.assertEqual(self.get.call_count, 1)

    def test_fresh_cache_is_reused_without_a_request(self):
        now = datetime.now(timezone.utc)
        first = self.events(now)
        second = self.events(now)
        self.assertEqual(self.get.call_count, 1)
        pd.testing.assert_frame_equal(first, second)
        stored = json.loads((self.cache / "oddsapi_events_EPL.json").read_text(encoding="utf-8"))
        self.assertEqual(stored["payload"], [EVENT])
        self.assertIsNotNone(pd.to_datetime(stored["fetched_at_utc"], utc=True))
        # The API key is never written into the cache.
        self.assertNotIn(KEYS["THE_ODDS_API_KEY"], json.dumps(stored))

    def test_events_cache_is_keyed_by_requested_window(self):
        now = datetime.now(timezone.utc)
        self.events(now)
        self.api.events(LEAGUES["EPL"], 7, now)
        self.events(now + timedelta(minutes=1))
        self.assertEqual(self.get.call_count, 3)
        windows = [(c.kwargs["params"]["commenceTimeFrom"], c.kwargs["params"]["commenceTimeTo"])
                   for c in self.get.call_args_list]
        self.assertEqual(len(set(windows)), 3)

    def test_odds_cache_uses_fetch_time_not_mtime(self):
        path = self.cache / "oddsapi_odds_ah_v1_EPL_eu.json"
        path.write_text(json.dumps([dict(OLD_EVENT, bookmakers=[])]), encoding="utf-8")
        os.utime(path, None)
        self.get.return_value = response([dict(EVENT, bookmakers=[])])
        now = datetime.now(timezone.utc)
        frame = self.api.odds(LEAGUES["EPL"], 3, now)
        self.assertEqual(frame["fixture_id"].tolist(), ["event1"])
        self.api.odds(LEAGUES["EPL"], 3, now)
        self.assertEqual(self.get.call_count, 1)


class StartedFixtureExclusionTests(OfflineQuotePolicyTestCase):
    NOW = datetime(2026, 10, 26, 11, 45, tzinfo=timezone.utc)

    def fixtures(self):
        rows = [
            # Played on 24/25 Oct: the stale-cache fixtures from the audit.
            ("Everton", "Fulham", "2026-10-24T14:00:00+00:00"),
            ("Leeds", "Wolves", "2026-10-25T16:30:00+00:00"),
            # Kickoff exactly now has started.
            ("Brentford", "Burnley", "2026-10-26T11:45:00+00:00"),
            ("Arsenal", "Chelsea", "2026-10-26T19:00:00+00:00"),
            ("Spurs", "Villa", "2026-10-27T19:45:00+00:00"),
        ]
        return pd.DataFrame([dict(Date=pd.Timestamp(k[:10]), kickoff_utc=k, HomeTeam=h, AwayTeam=a,
                                  fixture_source="The Odds API", odds_source="The Odds API",
                                  odds_event_id=f"e{i}") for i, (h, a, k) in enumerate(rows)])

    def test_unknown_kickoff_is_kept_only_for_a_later_date(self):
        frame = pd.DataFrame([
            dict(Date=pd.Timestamp("2026-10-25"), kickoff_utc=None, HomeTeam="A", AwayTeam="B"),
            dict(Date=pd.Timestamp("2026-10-26"), kickoff_utc=None, HomeTeam="C", AwayTeam="D"),
            dict(Date=pd.Timestamp("2026-10-27"), kickoff_utc=None, HomeTeam="E", AwayTeam="F"),
        ])
        with self.assertWarns(RuntimeWarning):
            kept, started = FootballValuePipelineV2._drop_started_fixtures(frame, LEAGUES["EPL"], self.NOW)
        self.assertEqual(kept["HomeTeam"].tolist(), ["E"])
        self.assertEqual([x["home_team"] for x in started], ["A", "C"])

    def test_past_kickoffs_never_reach_prediction_or_outputs(self):
        pipeline = object.__new__(FootballValuePipelineV2)
        for key, value in dict(half_life_days=480, l2=0.08, max_goals=10, devig_method="power",
                market_weight=0.7, fixture_provider="auto", odds_regions="eu",
                extra_event_odds_requests=0, max_extra_event_odds_requests=24,
                extra_event_odds_quota={"UCL": 4}, extra_event_odds_by_league={},
                additional_odds_coverage="all").items():
            setattr(pipeline, key, value)
        pipeline._training_health = Mock(return_value={"status": "OFFLINE_TEST"})
        pipeline._history_for_league = Mock(return_value=pd.DataFrame(
            columns=["Date", "HomeTeam", "AwayTeam", "FTHG", "FTAG"]))
        pipeline._current_fixtures = Mock(return_value=self.fixtures())
        pipeline._attach_live_odds = lambda fixtures, *args: fixtures
        predicted = []
        def predict(model, row):
            predicted.append(row["HomeTeam"])
            return dict(home_name_match_score=100, away_name_match_score=100), {}
        pipeline._predict_row = predict
        pipeline.odds_api = Mock()
        pipeline.odds_api.extra_markets_for_event.return_value = {}
        model = SimpleNamespace(training_matches=100, training_end=None, fit_result=None,
            resolve_team=lambda name: (name, 100.0),
                                base=0, home_adv=0, rho=0, half_life_days=480, max_goals=10)
        with patch("football_value_pipeline_v2_standalone.DixonColesModel") as model_class, \
                self.assertWarns(RuntimeWarning):
            model_class.return_value.fit.return_value = model
            frame, diagnostics, _ = pipeline.run_league("UCL", self.NOW)
        self.assertEqual(predicted, ["Arsenal", "Spurs"])
        self.assertEqual(frame["home_team"].tolist(), ["Arsenal", "Spurs"])
        self.assertEqual([x["home_team"] for x in diagnostics["excluded_started_fixtures"]],
                         ["Everton", "Leeds", "Brentford"])
        self.assertEqual(diagnostics["live_odds_matched"], 2)


if __name__ == "__main__":
    unittest.main()
