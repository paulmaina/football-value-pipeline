"""Offline tests for authorized The Odds API credential failover.

Never send real network calls or expose actual API keys. Exercise the
cached HTTP code path used for fixture/odds/event-specific live markets.
"""
from __future__ import annotations

from offline_test_case import OfflineQuotePolicyTestCase
from datetime import datetime, timedelta, timezone
import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import requests

from football_value_pipeline_v2_standalone import LEAGUES, TheOddsAPI


NOW = datetime(2026, 10, 10, 12, 0, tzinfo=timezone.utc)
URL = "https://api.the-odds-api.com/v4/sports/soccer_epl/odds"
TEST_KEYS = {
    "THE_ODDS_API_KEY": "primary-secret-for-tests",
    "THE_ODDS_API_KEY_FALLBACK_1": "secondary-secret-for-tests",
    "THE_ODDS_API_KEY_FALLBACK_2": "tertiary-secret-for-tests",
}


def fake_response(status: int, payload: object, url: str = URL) -> requests.Response:
    response = requests.Response()
    response.status_code = status
    response._content = json.dumps(payload).encode("utf-8")
    response.headers["Content-Type"] = "application/json"
    response.url = url
    return response


class RecordingGet:
    def __init__(self, *responses):
        self.responses = list(responses)
        self.calls = []

    def __call__(self, url, *, params, headers=None, timeout=None):
        self.calls.append((url, dict(params), timeout))
        if not self.responses:
            raise AssertionError("Unexpected additional HTTP request")
        return self.responses.pop(0)


class ApiKeyFailoverTests(OfflineQuotePolicyTestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.api = TheOddsAPI(
            TEST_KEYS["THE_ODDS_API_KEY"],
            cache_dir=self.tmp.name,
            regions="eu",
        )

    def request(self, recording_get, suffix="data.json"):
        self.api.http.session.get = recording_get
        with patch.dict(os.environ, TEST_KEYS, clear=True):
            return self.api._get_json(
                URL,
                suffix,
                ttl=timedelta(minutes=10),
                params={
                    "apiKey": "ignored-argument-secret",
                    "regions": "eu",
                    "markets": "h2h,totals",
                },
                allow_stale=False,
            )

    def test_primary_success_uses_one_request_and_caches_result(self):
        get = RecordingGet(fake_response(200, [{"id": "fixture-a"}]))
        output = self.request(get)
        self.assertEqual(output, [{"id": "fixture-a"}])
        self.assertEqual(len(get.calls), 1)
        self.assertEqual(get.calls[0][1]["apiKey"], TEST_KEYS["THE_ODDS_API_KEY"])
        self.assertEqual(get.calls[0][1]["regions"], "eu")
        self.assertEqual(get.calls[0][1]["markets"], "h2h,totals")
        # Second call must read the key-independent cache without network.
        self.assertEqual(self.request(get), output)
        self.assertEqual(len(get.calls), 1)

    def test_primary_429_immediately_uses_secondary_exact_request(self):
        get = RecordingGet(
            fake_response(429, {"error_code": "EXCEEDED_FREQ_LIMIT"}),
            fake_response(200, {"ok": True}),
        )
        with self.assertWarnsRegex(RuntimeWarning, "THE_ODDS_API_KEY"):
            result = self.request(get)
        self.assertEqual(result, {"ok": True})
        self.assertEqual(len(get.calls), 2)
        first, second = [c[1] for c in get.calls]
        self.assertEqual(first["apiKey"], TEST_KEYS["THE_ODDS_API_KEY"])
        self.assertEqual(second["apiKey"], TEST_KEYS["THE_ODDS_API_KEY_FALLBACK_1"])
        self.assertEqual(
            {k: v for k, v in first.items() if k != "apiKey"},
            {k: v for k, v in second.items() if k != "apiKey"},
        )

    def test_quota_401_then_403_tries_tertiary(self):
        get = RecordingGet(
            fake_response(401, {"error_code": "OUT_OF_USAGE_CREDITS"}),
            fake_response(403, {"error_code": "OUT_OF_USAGE_CREDITS"}),
            fake_response(200, {"ok": "third"}),
        )
        with self.assertWarns(RuntimeWarning):
            result = self.request(get)
        self.assertEqual(result, {"ok": "third"})
        self.assertEqual([x[1]["apiKey"] for x in get.calls],
                         list(TEST_KEYS.values()))

    def test_all_quota_errors_give_clean_terminal_error(self):
        get = RecordingGet(*[
            fake_response(401, {"error_code": "OUT_OF_USAGE_CREDITS"})
            for _ in range(3)
        ])
        with self.assertWarns(RuntimeWarning):
            with self.assertRaisesRegex(RuntimeError, "all configured keys") as cm:
                self.request(get)
        self.assertEqual(len(get.calls), 3)
        for value in TEST_KEYS.values():
            self.assertNotIn(value, str(cm.exception))
        self.assertFalse((Path(self.tmp.name) / "data.json").exists())

    def test_invalid_401_must_not_rotate_or_expose_credentials(self):
        get = RecordingGet(fake_response(
            401, {"error_code": "INVALID_KEY"},
            url=URL+"?apiKey="+TEST_KEYS["THE_ODDS_API_KEY"],
        ))
        with self.assertRaisesRegex(RuntimeError, "not a confirmed quota") as cm:
            self.request(get)
        self.assertEqual(len(get.calls), 1)
        self.assertNotIn(TEST_KEYS["THE_ODDS_API_KEY"], str(cm.exception))

    def test_nonquota_403_does_not_rotate(self):
        get = RecordingGet(fake_response(403, {"error_code": "DEACTIVATED_KEY"}))
        with self.assertRaisesRegex(RuntimeError, "HTTP 403"):
            self.request(get)
        self.assertEqual(len(get.calls), 1)

    def test_network_failure_does_not_rotate(self):
        get = RecordingGet()
        def failure(*args, **kwargs):
            raise requests.ConnectionError(
                "Connection to URL?apiKey=" + TEST_KEYS["THE_ODDS_API_KEY"]
            )
        self.api.http.session.get = failure
        with patch.dict(os.environ, TEST_KEYS, clear=True):
            with self.assertRaisesRegex(RuntimeError, "network request failed") as cm:
                self.api._get_json(URL, "failure.json", ttl=timedelta(0),
                                   params={"regions": "eu"}, allow_stale=False)
        self.assertNotIn(TEST_KEYS["THE_ODDS_API_KEY"], str(cm.exception))

    def test_keys_are_read_dynamically_and_duplicates_are_deduplicated(self):
        with patch.dict(os.environ, TEST_KEYS, clear=True):
            self.assertEqual(len(self.api._configured_keys()), 3)
            os.environ["THE_ODDS_API_KEY_FALLBACK_1"] = "new-secondary"
            os.environ["THE_ODDS_API_KEY_FALLBACK_2"] = "new-secondary"
            self.assertEqual(
                [key for _, key in self.api._configured_keys()],
                [TEST_KEYS["THE_ODDS_API_KEY"], "new-secondary"],
            )

    def test_only_one_configured_key_does_not_fabricate_fallbacks(self):
        with patch.dict(os.environ, {"THE_ODDS_API_KEY": "only-key"}, clear=True):
            self.assertEqual(self.api._configured_keys(), [
                ("THE_ODDS_API_KEY", "only-key")
            ])

    def test_live_events_path_uses_same_quota_failover(self):
        events = [{
            "id": "evt001", "home_team": "AFC", "away_team": "BFC",
            "commence_time": "2026-10-14T17:30:00Z",
        }]
        get = RecordingGet(
            fake_response(429, {"error_code": "EXCEEDED_FREQ_LIMIT"}),
            fake_response(200, events),
        )
        self.api.http.session.get = get
        with patch.dict(os.environ, TEST_KEYS, clear=True):
            with self.assertWarns(RuntimeWarning):
                output = self.api.events(LEAGUES["EPL"], 7, NOW)
        self.assertEqual(len(output), 1)
        self.assertEqual(len(get.calls), 2)
        self.assertEqual(get.calls[1][1]["apiKey"], TEST_KEYS["THE_ODDS_API_KEY_FALLBACK_1"])

    def test_standard_odds_path_uses_same_quota_failover(self):
        get = RecordingGet(
            fake_response(401, {"error_code": "OUT_OF_USAGE_CREDITS"}),
            fake_response(200, [{
                "id": "event001", "home_team": "Home FC", "away_team": "Away FC",
                "commence_time": "2026-10-14T17:30:00Z", "bookmakers": [],
            }]),
        )
        self.api.http.session.get = get
        with patch.dict(os.environ, TEST_KEYS, clear=True):
            with self.assertWarns(RuntimeWarning):
                output = self.api.odds(LEAGUES["EPL"], 7, NOW)
        self.assertEqual(len(output), 1)
        self.assertEqual(len(get.calls), 2)

    def test_extra_markets_path_uses_same_quota_failover(self):
        event_id = "b5f0d5faabf345d9a531033dfa4cccfd"
        get = RecordingGet(
            fake_response(403, {"error_code": "OUT_OF_USAGE_CREDITS"}),
            fake_response(200, {"id": event_id, "bookmakers": []}),
        )
        self.api.http.session.get = get
        with patch.dict(os.environ, TEST_KEYS, clear=True):
            with self.assertWarns(RuntimeWarning):
                output = self.api.extra_markets_for_event(LEAGUES["EPL"], event_id)
        self.assertEqual(output, {})
        self.assertEqual(len(get.calls), 2)
        self.assertEqual(get.calls[0][1]["markets"], "alternate_totals,btts,alternate_spreads,draw_no_bet")
        self.assertEqual(get.calls[1][1]["markets"], "alternate_totals,btts,alternate_spreads,draw_no_bet")
        self.assertEqual(get.calls[1][1]["apiKey"], TEST_KEYS["THE_ODDS_API_KEY_FALLBACK_1"])

    def test_429_is_not_retried_by_adapter_before_fallback(self):
        adapter = self.api.http.session.get_adapter(URL)
        self.assertNotIn(429, adapter.max_retries.status_forcelist)


if __name__ == "__main__":
    unittest.main()
