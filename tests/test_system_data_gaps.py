"""Regression cases from the October system audit; all requests are simulated."""
from datetime import datetime, timedelta, timezone
import json
import os
from pathlib import Path
import tempfile
from unittest.mock import patch

import pandas as pd
from offline_test_case import OfflineQuotePolicyTestCase
from tests import test_odds_api_key_failover as failover
from odds_provider_health import OddsProviderError
from pipeline_health import current_health, model_component_hashes, write_generation_metadata


class QuotaCircuitTests(OfflineQuotePolicyTestCase):
    setUp = failover.ApiKeyFailoverTests.setUp
    request = failover.ApiKeyFailoverTests.request

    def exhaust(self, code='OUT_OF_USAGE_CREDITS'):
        get = failover.RecordingGet(*(failover.fake_response(401 if code=='OUT_OF_USAGE_CREDITS' else 429,
                   {'error_code': code}) for _ in range(3)))
        with self.assertWarns(RuntimeWarning), self.assertRaises(OddsProviderError):
            self.request(get, 'exhausted.json')
        self.assertEqual(len(get.calls), 3)

    def test_exhaustion_stops_repeated_live_calls_but_preserves_fresh_cache(self):
        self.request(failover.RecordingGet(failover.fake_response(200, {'cached': True})), 'fresh.json')
        self.exhaust()
        get = failover.RecordingGet()
        with self.assertRaises(OddsProviderError) as caught:
            self.request(get, 'another-fixture.json')
        self.assertEqual(caught.exception.category, 'CREDITS_EXHAUSTED')
        self.assertEqual(get.calls, [])
        self.assertEqual(self.request(get, 'fresh.json'), {'cached': True})
        self.assertNotIn('secret', json.dumps(self.api.credit_exhaustion))

    def test_throttling_does_not_create_terminal_credit_lockout(self):
        self.exhaust('EXCEEDED_FREQ_LIMIT')
        get = failover.RecordingGet(failover.fake_response(200, {'recovered': True}))
        self.assertEqual(self.request(get, 'retry.json'), {'recovered': True})
        self.assertEqual(len(get.calls), 1)
        self.assertIsNone(self.api.credit_exhaustion)

    def test_changed_credentials_and_new_utc_day_can_recover(self):
        self.exhaust()
        get = failover.RecordingGet(failover.fake_response(200, {'changed': True}))
        self.api.http.session.get = get
        with patch.dict(os.environ, {'THE_ODDS_API_KEY': 'new-test-credential'}, clear=True):
            self.assertEqual(self.api._get_json(failover.URL, 'changed.json',
                ttl=timedelta(minutes=10), allow_stale=False), {'changed': True})
        self.assertIsNone(self.api.credit_exhaustion)
        self.exhaust()
        tomorrow = datetime.now(timezone.utc)+timedelta(days=1)
        with patch('football_value_pipeline_v2_standalone.datetime') as date:
            date.now.return_value = tomorrow
            result = self.request(failover.RecordingGet(failover.fake_response(200, {'reset': True})), 'reset.json')
        self.assertEqual(result, {'reset': True})
        self.assertIsNone(self.api.credit_exhaustion)


class HealthGapTests(OfflineQuotePolicyTestCase):
    def test_health_distinguishes_expired_selections_and_forecast_age(self):
        clock = datetime(2026,10,19,10,tzinfo=timezone.utc)
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp);raw=root/'raw';raw.mkdir()
            (raw/'conservative_bet_summary.json').write_text(json.dumps({
                'generated_at_utc':(clock-timedelta(hours=25)).isoformat()}))
            pd.DataFrame([{'kickoff_utc':(clock+timedelta(hours=hour)).isoformat(),
                'evaluated_at_utc':clock.isoformat(),'odds_age_hours':0} for hour in (-1,1)]
                +[{'kickoff_utc':'bad'}]).to_csv(raw/'conservative_bet_shortlist.csv',index=False)
            health=current_health(root,clock)
            self.assertEqual(health['forecast_freshness']['status'],'OLDER_THAN_24_HOURS')
            self.assertEqual(health['quote_audit']['past_kickoff_count'],1)
            self.assertEqual(health['quote_audit']['upcoming_kickoff_count'],1)
            self.assertEqual(health['quote_audit']['unknown_kickoff_count'],1)
            self.assertIn('rapidfuzz',health['dependencies'])

    def test_helper_provenance_is_line_ending_stable_and_hash_bound_to_new_runs(self):
        original=Path.read_bytes;baseline=model_component_hashes()
        def crlf(path):return original(path).replace(b'\r\n',b'\n').replace(b'\n',b'\r\n')
        with patch.object(Path,'read_bytes',crlf):self.assertEqual(model_component_hashes(),baseline)
        def changed(path):
            data=original(path)
            return data+b'\n# helper change\n' if path.name=='score_probability.py' else data
        with patch.object(Path,'read_bytes',changed):
            self.assertNotEqual(model_component_hashes()['score_probability.py'],baseline['score_probability.py'])
        with tempfile.TemporaryDirectory() as tmp:
            raw=Path(tmp)/'raw';raw.mkdir()
            (raw/'all_leagues_predictions.csv').write_text('league\n')
            write_generation_metadata(raw,{'generated_at_utc':'2026-10-19T10:00:00Z','selection_policy_version':'test'})
            result=json.loads((raw/'pipeline_run_metadata.json').read_text())
            self.assertEqual(result['model_component_sha256'],baseline)
