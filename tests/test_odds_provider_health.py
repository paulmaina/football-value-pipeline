"""No live API calls: quota classification, idle persistence and failure delivery."""
from datetime import timedelta
import json
import os
from pathlib import Path
import subprocess
import tempfile
from unittest.mock import patch
import unittest

import closing_odds as c
import github_closing_odds as g
from odds_provider_health import OddsProviderError, alert_summary, checkpoint, http_details
from tests.test_closing_odds import setup, payload
from tests.test_github_closing_odds import seeded
from tests import test_odds_api_key_failover as failover
from tests.test_odds_api_key_failover import RecordingGet, fake_response
from offline_test_case import OfflineQuotePolicyTestCase
from publish_performance import git


class ProviderClassificationTests(OfflineQuotePolicyTestCase):
    setUp = failover.ApiKeyFailoverTests.setUp
    request = failover.ApiKeyFailoverTests.request
    def test_confirmed_credits_and_mixed_throttle_are_distinct(self):
        for codes, expected in [(['OUT_OF_USAGE_CREDITS']*3, 'CREDITS_EXHAUSTED'),
                                (['OUT_OF_USAGE_CREDITS', 'EXCEEDED_FREQ_LIMIT', 'OUT_OF_USAGE_CREDITS'], 'RATE_LIMITED')]:
            get = RecordingGet(*(fake_response(429 if code == 'EXCEEDED_FREQ_LIMIT' else 401,
                                               {'error_code': code}) for code in codes))
            with self.assertWarns(RuntimeWarning), self.assertRaises(OddsProviderError) as caught:
                self.request(get)
            self.assertEqual(caught.exception.category, expected)
            self.assertEqual(len(caught.exception.attempts), 3)
            self.assertNotIn('secret', json.dumps(caught.exception.attempts))

    def test_headers_and_codes_are_whitelisted(self):
        response = fake_response(401, {'error_code': 'secret', 'message': 'secret'})
        response.headers.update({'x-requests-remaining': '0', 'x-requests-used': '500',
                                 'x-requests-last': 'secret', 'Authorization': 'secret'})
        error = __import__('requests').HTTPError('secret', response=response)
        details = http_details(error, 'THE_ODDS_API_KEY')
        self.assertEqual(details['x-requests-remaining'], 0)
        self.assertEqual(details['x-requests-used'], 500)
        self.assertNotIn('secret', json.dumps(details))
        with self.assertRaises(OddsProviderError) as caught:
            self.request(RecordingGet(response))
        self.assertEqual(caught.exception.category, 'HTTP_ERROR')


class ProviderCheckpointTests(unittest.TestCase):
    def test_idle_cannot_erase_failure_and_success_records_recovery(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); row, clock = setup(root)
            error = OddsProviderError('safe', 'CREDITS_EXHAUSTED',
                [{'credential': 'THE_ODDS_API_KEY', 'http_status': 401, 'error_code': 'OUT_OF_USAGE_CREDITS'}])
            def fail(*args): raise error
            result = c.collect_once(root, None, clock, fetcher=fail)
            self.assertEqual(result['requests'], 1)
            self.assertEqual(result['errors'][0]['category'], 'CREDITS_EXHAUSTED')
            before = (root/'closing_odds/provider_status.json').read_text()
            c.collect_once(root, None, clock+timedelta(days=1), fetcher=fail)
            self.assertEqual((root/'closing_odds/provider_status.json').read_text(), before)
            self.assertIn('CREDITS_EXHAUSTED', alert_summary(root))
            c.collect_once(root, None, clock, fetcher=lambda *args: payload(row, clock))
            state = json.loads((root/'closing_odds/provider_status.json').read_text())
            self.assertEqual(state['state'], 'AVAILABLE')
            self.assertEqual(state['last_failure']['category'], 'CREDITS_EXHAUSTED')
            self.assertIn('recovered_at_utc', state)
            self.assertEqual(alert_summary(root), '')

    def test_session_exits_nonzero_and_releases_lock(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); _, clock = setup(root)
            checkpoint(root, clock, OddsProviderError('safe', 'RATE_LIMITED', []))
            with patch.dict(os.environ, {'THE_ODDS_API_KEY': 'test'}, clear=True), \
                 patch.object(c, 'collect_once', return_value={'requests': 1, 'errors': [{'category': 'RATE_LIMITED'}]}), \
                 patch('football_value_pipeline_v2_standalone.TheOddsAPI') as api, \
                 patch('api_key_config.load_api_keys'), patch.object(c.time, 'sleep') as sleep:
                api.KEY_ENV_NAMES = ('THE_ODDS_API_KEY',)
                self.assertEqual(c.main(['--root', str(root), '--watch']), 1)
                sleep.assert_not_called()
            self.assertFalse((root/'closing_odds/collector.lock').exists())

    def test_failed_collector_publishes_durable_evidence_and_recovery(self):
        with tempfile.TemporaryDirectory() as tmp:
            source, _, row, clock = seeded(tmp)
            def runner(cmd, cwd, check):
                def fail(*args):
                    raise OddsProviderError('safe', 'CREDITS_EXHAUSTED', [])
                c.collect_once(Path(cwd)/g.ROOT, None, clock, fetcher=fail, reservation_id='quota')
                raise subprocess.CalledProcessError(1, cmd)
            with self.assertRaises(subprocess.CalledProcessError):
                g.collect(source, 'quota', runner=runner, clock=lambda: clock)
            git(source, 'fetch', 'origin', 'main')
            health = json.loads(git(source, 'show', 'FETCH_HEAD:'+str(g.DATA/'provider_status.json')).stdout)
            self.assertEqual(health['state'], 'CREDITS_EXHAUSTED')
            budget = json.loads(git(source, 'show', 'FETCH_HEAD:'+str(g.BUDGET)).stdout)
            self.assertEqual(budget['reservations']['quota']['status'], 'complete')
            self.assertEqual(budget['requests'], 1)
            self.assertTrue((source/'workflow_artifacts/closing-odds-recovery/provider_status.json').exists())
