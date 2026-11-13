"""Odds API credits: usage recording, no fixtures, all keys exhausted and the low-credit guard.

Every response is mocked; no request reaches the provider and no real key is used.
"""
from __future__ import annotations

from offline_test_case import OfflineQuotePolicyTestCase
from datetime import datetime, timedelta, timezone
import io
import json
import os
from contextlib import redirect_stdout
from pathlib import Path
import subprocess
import tempfile
from types import SimpleNamespace
from unittest.mock import patch

import pandas as pd
import requests

import closing_odds as c
import odds_api_usage as usage
import price_check
from football_value_pipeline_v2_standalone import TheOddsAPI
from performance_tracking import write_json
from publish_performance import git
import publish_scheduled_forecasts as publisher

URL = 'https://api.the-odds-api.com/v4/sports/soccer_epl/odds'
EVENTS = 'https://api.the-odds-api.com/v4/sports/soccer_epl/events'
EVENT_ODDS = 'https://api.the-odds-api.com/v4/sports/soccer_epl/events/abc123/odds'
KEYS = {'THE_ODDS_API_KEY': 'primary-secret-for-tests',
        'THE_ODDS_API_KEY_FALLBACK_1': 'secondary-secret-for-tests',
        'THE_ODDS_API_KEY_FALLBACK_2': 'tertiary-secret-for-tests'}
EXHAUSTED = {'error_code': 'OUT_OF_USAGE_CREDITS', 'message': 'Usage quota has been reached.'}


def response(status, payload, *, remaining=None, used=None, last=None, url=URL):
    r = requests.Response()
    r.status_code = status
    r._content = json.dumps(payload).encode('utf-8')
    r.headers['Content-Type'] = 'application/json'
    for name, value in (('x-requests-remaining', remaining), ('x-requests-used', used), ('x-requests-last', last)):
        if value is not None:
            r.headers[name] = str(value)
    r.url = url
    return r


class Replies:
    def __init__(self, *responses):
        self.responses = list(responses)

    def __call__(self, url, *, params, headers=None, timeout=None):
        return self.responses.pop(0)


def ledger(remaining, **kwargs):
    stamp = '2026-11-13T05:45:00+00:00'
    return usage.UsageLedger({'THE_ODDS_API_KEY': {'remaining': remaining, 'used': 500 - remaining,
                                                   'observed_at_utc': stamp}, **kwargs})


class UsageRecordingTests(OfflineQuotePolicyTestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.api = TheOddsAPI(KEYS['THE_ODDS_API_KEY'], cache_dir=self.tmp.name)

    def get(self, url, name):
        with patch.dict(os.environ, KEYS, clear=True):
            return self.api._get_json(url, name, ttl=timedelta(minutes=5), params={}, allow_stale=False)

    def test_headers_are_recorded_per_slot_and_endpoint_without_secrets(self):
        self.api.http.session.get = Replies(
            response(200, [], remaining=500, used=0, last=0, url=EVENTS),
            response(401, EXHAUSTED, remaining=0, used=500, last=0),
            response(200, [{'id': 'x'}], remaining=497, used=3, last=3),
            # Keys are tried in order on every call; an exhausted key costs nothing.
            response(401, EXHAUSTED, remaining=0, used=500, last=0, url=EVENT_ODDS),
            response(200, {'id': 'abc123'}, remaining=493, used=7, last=4, url=EVENT_ODDS))
        self.get(EVENTS, 'events.json')
        # The primary key runs out; the first fallback answers.
        with self.assertWarns(RuntimeWarning):
            self.get(URL, 'odds.json')
        with self.assertWarns(RuntimeWarning):
            self.get(EVENT_ODDS, 'event.json')
        calls = self.api.usage.calls
        self.assertEqual([(x['slot'], x['endpoint'], x['http_status']) for x in calls], [
            ('THE_ODDS_API_KEY', 'events', 200), ('THE_ODDS_API_KEY', 'odds', 401),
            ('THE_ODDS_API_KEY_FALLBACK_1', 'odds', 200), ('THE_ODDS_API_KEY', 'event_odds', 401),
            ('THE_ODDS_API_KEY_FALLBACK_1', 'event_odds', 200)])
        summary = self.api.usage.summary()
        self.assertEqual(summary['credits_spent'], 7)
        self.assertEqual(summary['by_endpoint'], {'event_odds': {'calls': 2, 'credits': 4},
                                                  'events': {'calls': 1, 'credits': 0},
                                                  'odds': {'calls': 2, 'credits': 3}})
        self.assertEqual(summary['slots']['THE_ODDS_API_KEY']['remaining'], 0)
        self.assertEqual(summary['slots']['THE_ODDS_API_KEY_FALLBACK_1']['remaining'], 493)
        self.assertEqual(summary['remaining_total'], 493)
        self.assertFalse(summary['all_keys_exhausted'])
        text = json.dumps(summary) + usage.summary_markdown(usage.run_record('test', self.api.usage))
        for secret in KEYS.values():
            self.assertNotIn(secret, text)
        self.assertNotIn('api.the-odds-api.com', text)

    def test_cache_hit_records_no_call(self):
        self.api.http.session.get = Replies(response(200, [], remaining=10, used=490, last=1))
        self.get(URL, 'cached.json')
        self.get(URL, 'cached.json')
        self.assertEqual(len(self.api.usage.calls), 1)

    def test_all_keys_exhausted_is_flagged(self):
        self.api.http.session.get = Replies(*[response(401, EXHAUSTED, remaining=0, used=500, last=0) for _ in KEYS])
        with self.assertWarns(RuntimeWarning), self.assertRaisesRegex(RuntimeError, 'all configured keys'):
            self.get(URL, 'odds.json')
        self.assertTrue(self.api.usage.exhausted)
        self.assertEqual(self.api.usage.remaining_total(), 0)
        self.assertEqual(len(self.api.usage.calls), 3)

    def test_log_round_trip_and_latest_balance_per_slot(self):
        with tempfile.TemporaryDirectory() as tmp:
            first = ledger(400)
            usage.append_log(usage.run_record('scheduled-forecasts', first), tmp)
            second = usage.UsageLedger()
            second.record('THE_ODDS_API_KEY', URL, 200, {'x-requests-remaining': '350', 'x-requests-used': '150',
                                                         'x-requests-last': '3'})
            usage.append_log(usage.run_record('closing-odds', second), tmp)
            (Path(tmp) / usage.LOG).open('a', encoding='utf-8').write('{torn line\n')
            records = usage.read_log(tmp)
            self.assertEqual([r['workflow'] for r in records], ['scheduled-forecasts', 'closing-odds'])
            self.assertEqual(usage.seeded_ledger(tmp).remaining_total(), 350)
            self.assertIsNone(usage.seeded_ledger(Path(tmp) / 'empty').remaining_total())

    def test_closing_session_record_merges_into_main_log(self):
        from github_closing_odds import merge_usage_log
        with tempfile.TemporaryDirectory() as tmp:
            source, work = Path(tmp) / 'source', Path(tmp) / 'work'
            usage.append_log({'workflow': 'old'}, work)
            usage.append_log({'workflow': 'old'}, source)
            usage.append_log({'workflow': 'closing-odds', 'credits_spent': 2}, source)
            self.assertEqual(merge_usage_log(source, work), [usage.LOG])
            self.assertEqual([r['workflow'] for r in usage.read_log(work)], ['old', 'closing-odds'])
            self.assertEqual(merge_usage_log(Path(tmp) / 'none', work), [])


class LowCreditGuardTests(OfflineQuotePolicyTestCase):
    def test_threshold_is_one_forecast_run_and_unknown_never_blocks(self):
        self.assertTrue(usage.UsageLedger().allows_optional(4))
        self.assertTrue(ledger(usage.FORECAST_RUN_CREDITS + 4).allows_optional(4))
        self.assertFalse(ledger(usage.FORECAST_RUN_CREDITS + 3).allows_optional(4))
        both = ledger(200, THE_ODDS_API_KEY_FALLBACK_1={'remaining': 200, 'used': 300})
        self.assertTrue(both.allows_optional(4))

    def coverage_with_balance(self, remaining):
        """The coverage suite's offline league run, with the mocked client holding a known balance."""
        from test_additional_odds_coverage import CoverageTests
        from unittest.mock import Mock
        case = CoverageTests('test_all_requests_18_even_with_four_slot_quota')

        def with_balance(*args, **kwargs):
            mock = Mock(*args, **kwargs)
            mock.usage = ledger(remaining)
            return mock
        with patch('test_additional_odds_coverage.Mock', side_effect=with_balance):
            return case.run_pipeline()

    def test_extra_coverage_is_skipped_but_main_odds_kept_when_credits_are_low(self):
        pipeline, (frame, diagnostics, _) = self.coverage_with_balance(usage.FORECAST_RUN_CREDITS - 1)
        self.assertEqual(pipeline.odds_api.extra_markets_for_event.call_count, 0)
        self.assertEqual(len(frame), 18)  # Every fixture is still forecast.
        self.assertEqual({r['status'] for r in diagnostics['additional_odds_coverage']}, {'NOT_REQUESTED_LOW_CREDITS'})
        self.assertEqual(diagnostics['additional_odds_unrequested_linked_fixtures'], 18)
        pipeline, _ = self.coverage_with_balance(usage.FORECAST_RUN_CREDITS + 100)
        self.assertEqual(pipeline.odds_api.extra_markets_for_event.call_count, 18)

    def test_price_check_is_skipped_without_any_request(self):
        from test_price_check import FakeApi, forecast
        from test_price_edge_shortlist import NOW
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / 'raw').mkdir()
            pd.DataFrame([forecast()]).to_csv(root / 'raw' / 'all_leagues_predictions.csv', index=False)
            api = FakeApi()
            api.usage = ledger(100)
            result = price_check.check(root, api, NOW.to_pydatetime())
            self.assertEqual(result['status'], 'SKIPPED_LOW_CREDITS')
            self.assertEqual(result['remaining_total'], 100)
            self.assertEqual(api.calls, [])

    def test_price_check_main_reports_skip_in_summary(self):
        with tempfile.TemporaryDirectory() as tmp:
            summary = Path(tmp) / 'summary.md'

            class Api:
                KEY_ENV_NAMES = ('THE_ODDS_API_KEY',)

                def __init__(self, key, cache_dir=None):
                    pass
            buffer = io.StringIO()
            with patch.dict(os.environ, {'THE_ODDS_API_KEY': 'offline-fake-key', 'GITHUB_STEP_SUMMARY': str(summary)}, clear=True), \
                    patch('football_value_pipeline_v2_standalone.TheOddsAPI', Api), \
                    patch.object(price_check, 'check', return_value={'status': 'SKIPPED_LOW_CREDITS'}), \
                    redirect_stdout(buffer):
                self.assertEqual(price_check.main(['--api-key-source', 'environment', '--root', str(Path(tmp) / 'out')]), 0)
            self.assertIn('price check skipped to keep the core forecast', summary.read_text(encoding='utf-8'))

    def test_closing_collects_picks_only_when_credits_are_low(self):
        from test_closing_odds import setup, payload
        from test_totals_anchor_experiment import sample
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            row, observed = setup(root)
            other = {**sample()[0], 'home_team': 'Other Home', 'away_team': 'Other Away', 'odds_event_id': 'nopick1'}
            pd.DataFrame([row, other]).to_csv(root / 'raw/all_leagues_predictions.csv', index=False)
            requested = []

            def fetch(api, source, markets):
                requested.append(source['odds_event_id'])
                return payload(source, observed)
            api = SimpleNamespace(usage=ledger(50))
            status = c.collect_once(root, api, observed, fetcher=fetch)
            self.assertEqual(requested, [row['odds_event_id']])
            self.assertEqual(status['skipped_low_credit_fixtures'], 1)
            # With credits, the fixture without a pick is collected too.
            requested.clear()
            api = SimpleNamespace(usage=ledger(1000))
            c.collect_once(root, api, observed, fetcher=fetch)
            self.assertEqual(requested, ['nopick1'])


class ClosingRetryTests(OfflineQuotePolicyTestCase):
    def test_handicap_request_expects_only_requested_bookmakers(self):
        from test_totals_anchor_experiment import sample
        row = sample()[0]
        selected = {'Asian Handicap Home -0.50', 'Home win'}
        self.assertEqual(c.required_quotes(row, selected, []),
                         {('pinnacle', 'Asian Handicap Home -0.50'), ('pinnacle', 'home')})
        self.assertEqual(c.required_quotes(row, {'Home win'}, []), {('pinnacle', 'home'), ('1xbet', 'home')})

    def test_unavailable_quote_is_retried_once_then_left(self):
        from test_closing_odds import setup, payload
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            row, observed = setup(root, market='Over 1.5')
            calls = []

            def no_1_5_line(api, source, markets):
                calls.append(markets)
                response = payload(source, observed - timedelta(seconds=len(calls)))
                for book in response['bookmakers']:
                    for market in book['markets']:
                        if market['key'] == 'alternate_totals':
                            market['outcomes'] = [o for o in market['outcomes'] if o['point'] != 1.5]
                return response
            for step in range(4):
                c.collect_once(root, None, observed - timedelta(seconds=40 - 10 * step), fetcher=no_1_5_line)
            self.assertEqual(len(calls), c.MAX_REQUESTS_PER_FIXTURE)
            later = c.collect_once(root, None, observed, fetcher=no_1_5_line)
            self.assertEqual(later['requests'], 0)
            self.assertEqual(later['retry_cap_reached_fixtures'], 1)
            from performance_tracking import utc
            self.assertFalse(c.pending_window(root, utc(row['kickoff_utc']) + timedelta(minutes=1), observed))


class RunOutcomeTests(OfflineQuotePolicyTestCase):
    def generate(self, rows, exhausted):
        from football_value_pipeline_v2_standalone import _RUN_STATE

        def fake(argv):
            staging = Path(argv[-1])
            write_json(staging / 'conservative_bet_summary.json', {'generated_at_utc': '2026-11-13T05:45:00+00:00'})
            if rows:
                pd.DataFrame(rows).to_csv(staging / 'all_leagues_predictions.csv', index=False)
            client = SimpleNamespace(usage=ledger(0 if exhausted else 420))
            client.usage.exhausted = exhausted
            _RUN_STATE['odds_api'] = client
            return 0
        return fake

    def run_main(self, rows, exhausted):
        from football_value_pipeline_v2_standalone import main
        from prediction_runs import resolve_raw
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        raw, outcome_path = Path(tmp.name) / 'raw', Path(tmp.name) / 'outcome.json'
        stderr = io.StringIO()
        with patch('football_value_pipeline_v2_standalone._generate_main', side_effect=self.generate(rows, exhausted)), \
                patch('sys.stderr', stderr):
            code = main(['--out-dir', str(raw), '--run-outcome-out', str(outcome_path)])
        published = (raw / 'current_run.json').exists()
        return code, json.loads(outcome_path.read_text(encoding='utf-8')), published, stderr.getvalue()

    def test_no_fixtures_is_green_and_publishes_nothing(self):
        code, outcome, published, log = self.run_main([], exhausted=False)
        self.assertEqual(code, 0)
        self.assertFalse(published)
        self.assertEqual(outcome['status'], usage.NO_FIXTURES)
        self.assertEqual(outcome['message'], 'No fixtures in the next 3 days; nothing to forecast')
        self.assertIn('nothing to forecast', log)
        self.assertNotIn('Traceback', log)

    def test_no_fixtures_with_exhausted_keys_stays_green_with_a_note(self):
        code, outcome, published, _ = self.run_main([], exhausted=True)
        self.assertEqual((code, outcome['status'], published), (0, usage.NO_FIXTURES, False))
        self.assertIn('credits are also exhausted', outcome['notes'][0])

    def test_exhausted_keys_with_fixtures_fail_with_one_line(self):
        rows = [{'league': 'Premier League', 'home_team': 'A', 'away_team': 'B',
                 'kickoff_utc': '2026-11-21T15:00:00+00:00', 'odds_source': ''}]
        code, outcome, published, log = self.run_main(rows, exhausted=True)
        self.assertEqual(code, 3)
        self.assertFalse(published)
        self.assertEqual(outcome['status'], usage.CREDITS_EXHAUSTED)
        self.assertEqual(outcome['message'], 'Odds API credits exhausted on all keys; forecasts not produced')
        self.assertEqual(outcome['odds_api']['remaining_total'], 0)
        self.assertNotIn('Traceback', log)

    def test_priced_rows_are_still_published_after_mid_run_exhaustion(self):
        from football_value_pipeline_v2_standalone import run_outcome
        with tempfile.TemporaryDirectory() as tmp:
            pd.DataFrame([{'odds_source': 'The Odds API'}, {'odds_source': ''}]).to_csv(
                Path(tmp) / 'all_leagues_predictions.csv', index=False)
            client = SimpleNamespace(usage=ledger(0))
            client.usage.exhausted = True
            outcome = run_outcome(Path(tmp), 3, client)
        self.assertEqual(outcome['status'], usage.FORECASTS_PRODUCED)
        self.assertEqual(outcome['odds_api_priced_rows'], 1)
        self.assertIn('ran out', outcome['notes'][0])


class PublisherOutcomeTests(OfflineQuotePolicyTestCase):
    def outcome_runner(self, outcome, *, fail=False):
        calls = []

        def runner(cmd, cwd, check):
            calls.append(cmd[1])
            if cmd[1] == 'football_value_pipeline_v2_standalone.py':
                usage.write_json(cmd[cmd.index('--run-outcome-out') + 1], outcome)
                if fail:
                    raise subprocess.CalledProcessError(3, cmd)
        return runner, calls

    def outcome(self, status, message, remaining):
        record = ledger(remaining)
        record.record('THE_ODDS_API_KEY', EVENTS, 200, {'x-requests-remaining': str(remaining),
                                                        'x-requests-used': str(500 - remaining), 'x-requests-last': '0'})
        record.exhausted = status == usage.CREDITS_EXHAUSTED
        return {'status': status, 'message': message, 'notes': [], 'forecast_rows': 0, 'odds_api': record.summary()}

    def test_no_fixtures_finishes_green_and_commits_only_the_usage_log(self):
        from test_publish_scheduled_forecasts import repo
        with tempfile.TemporaryDirectory() as tmp:
            source, _ = repo(tmp)
            summary = Path(tmp) / 'summary.md'
            runner, calls = self.outcome_runner(self.outcome(usage.NO_FIXTURES, usage.no_fixtures_message(3), 480))
            with patch.dict(os.environ, {'GITHUB_STEP_SUMMARY': str(summary)}):
                result = publisher.publish(source, runner=runner)
            self.assertEqual(result['status'], usage.NO_FIXTURES)
            self.assertEqual(calls, ['football_value_pipeline_v2_standalone.py'])  # No raw check, no capture.
            text = summary.read_text(encoding='utf-8')
            self.assertTrue(text.startswith('No fixtures in the next 3 days; nothing to forecast'))
            self.assertIn('| THE_ODDS_API_KEY | 480 | 20 |', text)
            git(source, 'fetch', 'origin', 'main')
            changed = git(source, 'show', '--name-only', '--format=', 'FETCH_HEAD').stdout.split()
            self.assertEqual(changed, [usage.LOG.as_posix()])
            log = json.loads(git(source, 'show', f'FETCH_HEAD:{usage.LOG.as_posix()}').stdout)
            self.assertEqual((log['outcome'], log['remaining_total']), (usage.NO_FIXTURES, 480))
            self.assertNotIn('secret', json.dumps(log))

    def test_exhausted_keys_fail_with_one_line_and_keep_the_log(self):
        from test_publish_scheduled_forecasts import repo
        with tempfile.TemporaryDirectory() as tmp:
            source, _ = repo(tmp)
            summary = Path(tmp) / 'summary.md'
            runner, _ = self.outcome_runner(self.outcome(usage.CREDITS_EXHAUSTED, usage.EXHAUSTED_MESSAGE, 0), fail=True)
            buffer = io.StringIO()
            original = publisher.publish
            with patch.dict(os.environ, {'GITHUB_STEP_SUMMARY': str(summary)}), \
                    patch.object(publisher, 'publish', lambda repo: original(repo, runner=runner)), \
                    redirect_stdout(buffer):
                self.assertEqual(publisher.main(['--repo', str(source)]), 1)
            self.assertEqual(buffer.getvalue().strip().splitlines()[-1],
                             '::error::Odds API credits exhausted on all keys; forecasts not produced')
            self.assertTrue(summary.read_text(encoding='utf-8').startswith(usage.EXHAUSTED_MESSAGE))
            git(source, 'fetch', 'origin', 'main')
            log = json.loads(git(source, 'show', f'FETCH_HEAD:{usage.LOG.as_posix()}').stdout)
            self.assertTrue(log['all_keys_exhausted'])
            self.assertEqual(log['remaining_total'], 0)

    def test_other_pipeline_failures_still_raise(self):
        from test_publish_scheduled_forecasts import repo
        with tempfile.TemporaryDirectory() as tmp:
            source, _ = repo(tmp)
            runner, _ = self.outcome_runner({'status': 'FAILED', 'message': 'Forecast generation failed; see the log',
                                             'odds_api': None}, fail=True)
            with self.assertRaises(subprocess.CalledProcessError):
                publisher.publish(source, runner=runner)

    def test_scheduled_workflow_has_no_push_trigger(self):
        text = (Path(__file__).resolve().parents[1] / '.github/workflows/scheduled-forecasts.yml').read_text(encoding='utf-8')
        triggers = text.split('\npermissions:')[0]
        self.assertNotIn('push:', triggers)
        self.assertIn('schedule:', triggers)
        self.assertIn('workflow_dispatch:', triggers)
