"""Free-plan accounting, source reconciliation and observed-before-origin gates."""
import copy
from datetime import datetime, timedelta, timezone
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

import pandas as pd

import api_football_data as api
from api_football_integration import augment_history, records, supplement_fixtures, latest
from bbs_statistics_model import FormIndex
from bbs_data import Store, Deferred, FetchError, atomic_json

NOW = datetime(2026, 10, 20, 6, tzinfo=timezone.utc)


def match(entity=1, home=1, away=2, day='2026-10-10T15:00:00Z', status='FT', hg=2, ag=1, league='EPL'):
    names = {1: 'Arsenal', 2: 'Chelsea', 3: 'Liverpool'}
    return {'fixture': {'id': entity, 'date': day, 'status': {'short': status}},
        'league': {'id': api.LEAGUES[league], 'season': 2026,
                   'round': 'League Stage - 1' if league == 'UCL' else 'Regular Season - 1'},
        'teams': {'home': {'id': home, 'name': names[home]}, 'away': {'id': away, 'name': names[away]}},
        'goals': {'home': hg, 'away': ag}, 'score': {'fulltime': {'home': hg, 'away': ag},
        'extratime': {'home': None, 'away': None}, 'penalty': {'home': None, 'away': None}}}


def stats(home=1, away=2, shots=10):
    return [{'team': {'id': entity}, 'statistics': [
        {'type': 'Total Shots', 'value': shots}, {'type': 'Shots on Goal', 'value': 4},
        {'type': 'Ball Possession', 'value': '50%'}, {'type': 'Passes %', 'value': '80%'}]}
        for entity in (home, away)]


def envelope(rows, errors=None):
    return {'response': rows, 'results': len(rows), 'errors': errors or [],
            'paging': {'current': 1, 'total': 1}}


def baseline():
    return pd.DataFrame([
        {'Date': pd.Timestamp('2026-10-10'), 'HomeTeam': 'Arsenal', 'AwayTeam': 'Chelsea',
         'FTHG': 2, 'FTAG': 1, 'Season': '2627', 'B365H': 1.8},
        {'Date': pd.Timestamp('2026-10-05'), 'HomeTeam': 'Liverpool', 'AwayTeam': 'Arsenal',
         'FTHG': 1, 'FTAG': 1, 'Season': '2627', 'B365H': 2.1}])


class ApiFootballTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(); self.root = Path(self.temp.name)
        self.cache = self.root/'.football_cache'; self.store = Store(self.cache/'api_football/state')

    def tearDown(self):
        self.temp.cleanup()

    def client(self, replies=None, **kwargs):
        replies = iter(replies or [(200, {}, api.dumps(envelope([match()])).encode())])
        self.calls = []
        def sender(path, params, token):
            self.calls.append((path, params)); return next(replies)
        return api.Client(self.store, 'SECRET_TOKEN', sender=sender, clock=lambda: NOW,
                          sleeper=lambda _: None, **kwargs)

    def add(self, row=None, observed=NOW, statistics=True, league='EPL'):
        row = row or match()
        value = api.normal_match(row, league, 2026, observed.isoformat())
        self.store.put('match', league, row['fixture']['id'], observed.isoformat(), value)
        if statistics and value['status'] in api.FINISHED:
            self.store.put('statistics', league, row['fixture']['id'], observed.isoformat(),
                           api.normal_statistics(stats(row['teams']['home']['id'], row['teams']['away']['id']), value))

    def test_cached_response_reservations_survive_restart_and_observation_time_is_not_rewritten(self):
        client = self.client()
        data, observed = client.get('/fixtures', {'league': 39, 'season': 2026})
        self.assertEqual(len(data['response']), 1)
        self.assertEqual(client.get('/fixtures', {'season': 2026, 'league': 39})[1], observed)
        reopened = Store(self.store.path)
        self.assertEqual(reopened.state['quota'][NOW.date().isoformat()], 1)
        self.assertEqual(len(self.calls), 1)
        self.assertNotIn('SECRET_TOKEN', ''.join(p.read_text() for p in self.cache.rglob('*.json')))
        reopened.reserve(NOW, 2)
        with self.assertRaises(Deferred):reopened.reserve(NOW, 2)
        reopened.reserve(NOW+timedelta(days=1), 2)

    def test_account_limit_and_429_stop_further_calls(self):
        for reply in ((429, {}, b''), (200, {'x-ratelimit-requests-remaining': '20'}, api.dumps(envelope([])).encode())):
            self.store.state['settings'].clear(); self.store.set('blocked_day', '')
            client = self.client([reply])
            try:client.get('/fixtures', {'league': 39})
            except Deferred:pass
            with self.assertRaises(Deferred):client.get('/fixtures', {'league': 2})
            self.assertEqual(len(self.calls), 1)

    def test_budget_denied_plan_and_malformed_envelopes_never_silently_succeed(self):
        for budget in (0, 81):
            with self.assertRaises(ValueError):self.client(daily_budget=budget)
        with self.assertRaises(ValueError):api.Client(self.store, '')
        client = self.client(max_requests=1)
        client.get('/fixtures', {'league': 39})
        with self.assertRaises(Deferred):client.get('/fixtures', {'league': 2})
        failures = [b'not json', b'[]', api.dumps({'response': {}}).encode(),
            api.dumps({**envelope([]), 'paging': {'total': 2}}).encode(),
            api.dumps({**envelope([]), 'results': 1}).encode(),
            api.dumps(envelope([], {'plan': 'SECRET_TOKEN denied'})).encode()]
        for i, body in enumerate(failures):
            with self.subTest(i=i):
                client = self.client([(200, {}, body)])
                with self.assertRaises(FetchError):client.get('/fixtures', {'case': i})
        client = self.client()
        with self.assertRaisesRegex(FetchError, 'unavailable'):client.get('/fixtures', {'case': 5})
        self.assertFalse(self.calls)
        client = self.client([(500, {}, b'SECRET_TOKEN')])
        with self.assertRaisesRegex(FetchError, 'HTTP 500'):client.get('/fixtures', {'case': 'server'})
        client = self.client([(200, {'x-ratelimit-requests-remaining': 'invalid'}, b'{}')])
        with self.assertRaises(FetchError):client.get('/fixtures', {'case': 'header'})
        self.assertNotIn('SECRET_TOKEN', ''.join(p.read_text() for p in self.cache.rglob('*.json')))

    def test_normal_match_uses_regulation_scores_for_extra_time_and_penalties(self):
        for status in ('FT', 'AET', 'PEN', 'NS', 'TBD', 'PST', 'AWD', 'WO', 'ABD'):
            row = match(status=status)
            if status in ('AET', 'PEN'):row['goals'] = {'home': 4, 'away': 3}
            result = api.normal_match(row, 'EPL', 2026, NOW.isoformat())
            self.assertEqual(result['score'], {'home': 2, 'away': 1} if status in api.FINISHED else None)
        for mutate in (
            lambda r: r['fixture'].update(id=True), lambda r: r['league'].update(id=2),
            lambda r: r['league'].update(season=2025), lambda r: r['fixture'].update(date='2027-09-01T15:00:00Z'),
            lambda r: r['fixture'].update(date='2026-10-22T15:00:00Z'),
            lambda r: r['fixture']['status'].update(short='2026-10-20 15:45:00Z'),
            lambda r: r['teams']['home'].update(id=2), lambda r: r['teams']['home'].update(name=''),
            lambda r: r['score'].update(fulltime=None), lambda r: r['goals'].update(home=3)):
            row = match(); mutate(row)
            with self.assertRaises(ValueError):api.normal_match(row, 'EPL', 2026, NOW.isoformat())

    def test_statistics_validate_team_identity_missing_values_percentages_and_consistency(self):
        value = api.normal_match(match(), 'EPL', 2026, NOW.isoformat())
        result = api.normal_statistics(stats(), value)
        self.assertEqual(result['home']['ball_possession'], 50)
        with self.assertRaises(ValueError):api.normal_statistics(stats(), {**value, 'status': 'AET'})
        for rows in ([], stats(1, 1), stats(1, 3), stats(shots=2)):
            with self.assertRaises(ValueError):api.normal_statistics(rows, value)
        rows = stats(); rows[0]['statistics'] *= 2
        with self.assertRaises(ValueError):api.normal_statistics(rows, value)
        rows = stats(); rows[0]['statistics'][0]['value'] = -1
        with self.assertRaises(ValueError):api.normal_statistics(rows, value)
        rows = stats(); rows[0]['statistics'].append({'type': 'Unknown field', 'value': 'ignored'})
        self.assertTrue(api.normal_statistics(rows, value)['available'])
        rows = [{'team': {'id': i}, 'statistics': []} for i in (1, 2)]
        self.assertFalse(api.normal_statistics(rows, value)['available'])

    def test_collection_retains_all_fixtures_and_statistics_without_live_model_calls(self):
        future = match(2, 2, 3, day='2026-10-21T15:00:00Z', status='NS')
        client = self.client([(200, {}, api.dumps(envelope([match(), future])).encode()),
                              (200, {}, api.dumps(envelope(stats())).encode())])
        report = api.collect(client, ['EPL'], [2026], 10)
        self.assertEqual(report['status'], 'complete')
        self.assertEqual(report['statistics_saved'], 1)
        self.assertEqual(len(self.store.latest('match', NOW.isoformat())), 2)
        self.assertEqual(api.collect(client, ['EPL'], [2026], 10)['requests'], 2)
        self.assertEqual(len(self.calls), 2)

    def test_collection_quarantines_duplicate_or_invalid_fixtures_and_stats(self):
        bad = match(3); bad['fixture']['status']['short'] = 'timestamp'
        client = self.client([(200, {}, api.dumps(envelope([match(), match(), bad])).encode())])
        report = api.collect(client, ['EPL'], [2026], 10)
        self.assertEqual(report['quarantined_matches'], 2)
        self.assertEqual(records(self.cache, 'EPL', NOW.isoformat()), [])
        client = self.client([(200, {}, api.dumps(envelope([match(4)])).encode()),
                              (200, {}, api.dumps(envelope([{}])).encode())])
        # Remove the old response to exercise a newly received season revision.
        self.store.response_path('/fixtures?league=39&season=2026').unlink()
        report = api.collect(client, ['EPL'], [2026], 10)
        self.assertEqual(report['status'], 'partial')
        self.assertFalse(self.store.latest('statistics', NOW.isoformat())[0]['payload']['available'])

    def test_unchanged_matches_are_not_duplicated_and_schedule_freshness_is_bound_to_download(self):
        future = match(2, 2, 3, day='2026-10-21T15:00:00Z', status='NS')
        body = api.dumps(envelope([match(), future])).encode()
        client = self.client([(200, {}, body)])
        api.collect(client, ['EPL'], [2026], 0)
        later = NOW+timedelta(hours=25)
        client = api.Client(self.store, 'test', sender=lambda *args: (200, {}, body),
                            clock=lambda: later, sleeper=lambda _: None)
        api.collect(client, ['EPL'], [2026], 0)
        self.assertEqual(len(list((self.store.path/'observations/match').glob('*.json'))), 2)
        self.assertEqual(len(list((self.store.path/'observations/schedule').glob('*.json'))), 2)
        result = supplement_fixtures(pd.DataFrame(), baseline(), self.cache, 'EPL', later, 10)
        self.assertEqual(len(result), 1)
        self.assertEqual(result.iloc[0]['fixture_observed_at_utc'], later.isoformat())
        # Before the fresh response was observed, the old schedule is stale.
        self.assertTrue(supplement_fixtures(pd.DataFrame(), baseline(), self.cache, 'EPL',
                        later-timedelta(seconds=1), 10).empty)

    def test_no_access_empty_queries_and_failed_statistics_are_visible(self):
        client = self.client([(200, {}, api.dumps(envelope([], {'plan': 'not allowed'})).encode())])
        report = api.collect(client, ['EPL'], [2026], 0)
        self.assertEqual(report['status'], 'partial')
        client = self.client([(200, {}, api.dumps(envelope([])).encode())])
        self.assertEqual(api.collect(client, ['UCL'], [2026], 0)['status'], 'partial')
        client = self.client([(200, {}, api.dumps(envelope([match()])).encode()), (500, {}, b'')])
        self.store.response_path('/fixtures?league=39&season=2026').unlink()
        report = api.collect(client, ['EPL'], [2026], 1)
        self.assertEqual(report['status'], 'partial')
        self.assertEqual(self.store.latest('statistics', NOW.isoformat()), [])
        value = api.normal_match(match(), 'EPL', 2026, NOW.isoformat())
        self.store.put('statistics', 'EPL', '1', (NOW-timedelta(days=8)).isoformat(),
                       api.normal_statistics(stats(), value))
        client = self.client([(500, {}, b'')])
        self.assertEqual(api.collect(client, ['EPL'], [2026], 1)['status'], 'partial')
        self.assertTrue(self.store.latest('statistics', NOW.isoformat())[0]['payload']['available'])

    def test_reconciliation_preserves_prices_and_primary_scores_and_adds_missing_results_once(self):
        self.add(); self.add(match(2, 2, 3))
        data = augment_history(baseline(), self.cache, 'EPL', NOW, 6)
        self.assertEqual(len(data), 3)
        self.assertEqual(data.attrs['api_football']['added_results'], 1)
        self.assertEqual(data.loc[data.HomeTeam.eq('Arsenal'), 'B365H'].iloc[0], 1.8)
        self.assertTrue(pd.isna(data.loc[data.HomeTeam.eq('Chelsea'), 'B365H'].iloc[0]))
        self.assertEqual(len(augment_history(data, self.cache, 'EPL', NOW, 6)), 3)
        corrected = baseline(); corrected.loc[0, 'FTHG'] = 3
        result = augment_history(corrected, self.cache, 'EPL', NOW, 6)
        self.assertEqual(result.attrs['api_football']['conflicts'], 1)
        self.assertEqual(result.loc[result.HomeTeam.eq('Arsenal'), 'FTHG'].iloc[0], 3)
        self.assertEqual(len(result.attrs['bbs_statistics_observations']), 1)
        self.assertIs(augment_history(corrected, self.cache, 'EPL', NOW-timedelta(days=1), 6), corrected)

    def test_unmapped_teams_duplicates_date_conflicts_and_tamper_are_held(self):
        row = match(); row['teams']['home']['name'] = 'Unknown Club'
        self.add(row)
        result = augment_history(baseline(), self.cache, 'EPL', NOW, 6)
        self.assertEqual(result.attrs['api_football']['unmapped'], 1)
        atomic_json(self.cache/'api_football/team_map.json', {'EPL': {'1': 'Arsenal'}})
        self.assertEqual(augment_history(baseline(), self.cache, 'EPL', NOW, 6).attrs['api_football']['matched_results'], 1)
        self.add(match(2, day='2026-10-11T15:00:00Z'))
        self.assertEqual(augment_history(baseline(), self.cache, 'EPL', NOW, 6).attrs['api_football']['ambiguous'], 2)
        file = next((self.store.path/'observations/match').glob('*.json'))
        file.write_text('{}')
        result = augment_history(baseline(), self.cache, 'EPL', NOW, 6)
        self.assertEqual(result.attrs['api_football']['status'], 'BASELINE_RETAINED_SOURCE_ERROR')
        self.assertEqual(len(result), len(baseline()))

    def test_newer_quarantine_blocks_prior_match_and_stats_are_reconciled_against_primary(self):
        self.add()
        primary = baseline(); primary['HST'] = 5
        data = augment_history(primary, self.cache, 'EPL', NOW, 6)
        self.assertFalse(data.attrs['bbs_statistics_observations'][0]['available'])
        self.store.put('quarantine', 'EPL', '1', (NOW+timedelta(seconds=1)).isoformat(), {'reason': 'bad'})
        self.assertEqual(records(self.cache, 'EPL', (NOW+timedelta(seconds=2)).isoformat()), [])
        self.assertEqual(len(records(self.cache, 'EPL', NOW.isoformat())), 1)

    def test_form_inputs_count_one_physical_match_and_resolve_each_source_as_of_origin(self):
        self.add()
        frame = augment_history(baseline(), self.cache, 'EPL', NOW, 6)
        extra = frame.attrs['bbs_statistics_observations'][0]
        bbs = {**extra, 'match_id': 'EPL:bbs-one', 'source': 'bigballsdata'}
        index = FormIndex([extra, bbs], NOW+timedelta(hours=1))
        self.assertEqual(index.form('Arsenal', NOW+timedelta(minutes=1))[1], 1)
        self.assertEqual(index.form('Arsenal', NOW)[1], 0)
        tombstone = {**bbs, 'observed_at_utc': (NOW+timedelta(minutes=2)).isoformat(),
                     'available': False, 'home': None, 'away': None}
        index = FormIndex([bbs, extra, tombstone], NOW+timedelta(hours=1))
        self.assertEqual(index.form('Arsenal', NOW+timedelta(minutes=3))[1], 1)
        tombstone2 = {**tombstone, 'match_id': extra['match_id'], 'source': 'api-football'}
        index = FormIndex([bbs, extra, tombstone, tombstone2], NOW+timedelta(hours=1))
        self.assertEqual(index.form('Arsenal', NOW+timedelta(minutes=3))[1], 0)

    def test_cached_fixtures_fill_gaps_but_not_conflicting_dates_or_stale_schedules(self):
        self.add(match(2, 2, 3, day='2026-10-21T15:00:00Z', status='NS'), statistics=False)
        result = supplement_fixtures(pd.DataFrame(), baseline(), self.cache, 'EPL', NOW, 10)
        self.assertEqual(len(result), 1)
        self.assertEqual(result.iloc[0]['fixture_source'], 'API-Football cached')
        self.assertEqual(len(supplement_fixtures(result, baseline(), self.cache, 'EPL', NOW, 10)), 1)
        conflict = result.copy(); conflict['kickoff_utc'] = '2026-10-22T15:00:00Z'
        self.assertIs(supplement_fixtures(conflict, baseline(), self.cache, 'EPL', NOW, 10), conflict)
        self.assertTrue(supplement_fixtures(pd.DataFrame(), baseline(), self.cache, 'EPL', NOW+timedelta(hours=25), 10).empty)

    def test_pipeline_reads_both_sources_without_calling_api(self):
        from football_value_pipeline_v2_standalone import FootballValuePipelineV2, LEAGUES
        self.add()
        pipeline = FootballValuePipelineV2(cache_dir=self.cache)
        with patch.object(pipeline.source, 'history', return_value=baseline()), patch.object(api, 'transport', side_effect=AssertionError('no live calls')):
            result = pipeline._history_for_league(LEAGUES['EPL'], NOW)
        self.assertEqual(result.attrs['api_football']['matched_results'], 1)
        self.assertEqual(len(result.attrs['bbs_statistics_observations']), 1)
        from bbs_integration import training_provenance
        self.assertEqual(training_provenance(result)['api_football']['source'], 'api-football')

    def test_pipeline_uses_cached_schedule_as_union_or_last_resort_without_api_calls(self):
        from football_value_pipeline_v2_standalone import FootballValuePipelineV2, LEAGUES
        from types import SimpleNamespace
        self.add(match(2, 2, 3, day='2026-10-21T15:00:00Z', status='NS'), statistics=False)
        pipeline = FootballValuePipelineV2(cache_dir=self.cache)
        pipeline._validation_history = baseline()
        primary = pd.DataFrame([{'Date': pd.Timestamp('2026-10-21T18:00:00'),
            'HomeTeam': 'Arsenal', 'AwayTeam': 'Chelsea', 'fixture_source': 'The Odds API',
            'fixture_id': 'original', 'kickoff_utc': '2026-10-21T18:00:00Z'}])
        pipeline.odds_api = SimpleNamespace(events=lambda *args: primary)
        self.assertEqual(len(pipeline._current_fixtures(LEAGUES['EPL'], NOW)), 2)
        pipeline.odds_api = None; pipeline.football_data_org = None
        with patch.object(pipeline.source, 'fixtures', return_value=pd.DataFrame()):
            result = pipeline._current_fixtures(LEAGUES['EPL'], NOW)
        self.assertEqual(result.iloc[0]['fixture_source'], 'API-Football cached')

    def test_insufficient_api_statistics_leave_fitted_probabilities_identical(self):
        from football_value_pipeline_v2_standalone import DixonColesModel
        from tests.test_model_correctness import history
        self.add()
        extra = augment_history(baseline(), self.cache, 'EPL', NOW, 6).attrs['bbs_statistics_observations'][0]
        extra = {**extra, 'home_team': 'A', 'away_team': 'B'}
        frame = history(); frame.attrs['bbs_statistics_observations'] = [extra]
        reference = NOW+timedelta(hours=1)
        control = DixonColesModel(bbs_statistics=False).fit(frame, as_of=reference)
        augmented = DixonColesModel().fit(frame, as_of=reference)
        self.assertEqual(augmented.bbs_statistics_report['input_providers'], ['api-football'])
        for field in ('lambda_home', 'lambda_away'):
            self.assertEqual(augmented.expected_goals('A', 'B')[field], control.expected_goals('A', 'B')[field])

    def test_conflicting_observation_instants_fail_closed(self):
        row = {'league': 'EPL', 'entity': '1', 'observed': NOW.isoformat(), 'payload': {}}
        with self.assertRaises(ValueError):latest([row, {**row, 'payload': {'different': True}}])

    def test_consistent_statistics_fill_fields_only_after_observation_and_never_double_count(self):
        self.add()
        sample = augment_history(baseline(), self.cache, 'EPL', NOW, 6).attrs['bbs_statistics_observations'][0]
        values = []
        for i in range(3):
            extra = copy.deepcopy(sample)
            extra.update(match_id='api:'+str(i), kickoff_utc=f'2026-10-0{i+5}T15:00:00Z')
            primary = copy.deepcopy(extra)
            primary.update(match_id='bbs:'+str(i), source='bigballsdata',
                           observed_at_utc=(NOW-timedelta(minutes=1)).isoformat())
            for side in ('home', 'away'):primary[side]['total_shots'] = None
            values.extend([primary, extra])
        index = FormIndex(values, NOW+timedelta(hours=1))
        self.assertFalse(index.form('Arsenal', NOW)[3])
        after = index.form('Arsenal', NOW+timedelta(minutes=1))
        self.assertTrue(after[3]); self.assertEqual(after[1], 3)
        for row in values:
            if row.get('source') == 'api-football':row['home']['shots_on_target'] = 5
        self.assertFalse(FormIndex(values, NOW+timedelta(hours=1)).form('Arsenal', NOW+timedelta(minutes=1))[3])

    def test_ucl_scope_retains_regulation_scores_but_excludes_qualifiers_and_unknown_phases(self):
        history = baseline(); history['Season'] = '2026'
        self.add(match(1, league='UCL'), league='UCL')
        self.add(match(2, 2, 3, day='2026-10-11T15:00:00Z', league='UCL', status='AET'), league='UCL', statistics=False)
        result = augment_history(history, self.cache, 'UCL', NOW, 4)
        self.assertEqual(result.attrs['api_football']['added_results'], 1)
        self.assertEqual(result.loc[result.history_source.eq('api-football'), 'Date'].iloc[0].hour, 15)
        row = match(3, 2, 3, day='2026-06-25T15:00:00Z', league='UCL')
        row['league']['round'] = '1st Qualifying Round'
        self.add(row, league='UCL', statistics=False)
        self.assertEqual(augment_history(history, self.cache, 'UCL', NOW, 4).attrs['api_football']['excluded_phase'], 1)
        self.assertFalse(api.main_ucl_stage(None)); self.assertFalse(api.main_ucl_stage('Play-offs'))

    def test_transport_never_redirects_credentials_and_network_errors_are_sanitized(self):
        from types import SimpleNamespace
        import requests
        response = SimpleNamespace(status_code=200, headers={}, content=b'{}')
        with patch('requests.get', return_value=response) as get:
            self.assertEqual(api.transport('/fixtures', {'league': 39}, 'test')[0], 200)
            self.assertFalse(get.call_args.kwargs['allow_redirects'])
            self.assertEqual(get.call_args.kwargs['headers'], {'x-apisports-key': 'test'})
        with patch('requests.get', side_effect=requests.ConnectionError('SECRET_TOKEN')):
            with self.assertRaisesRegex(FetchError, 'network request failed'):api.transport('/fixtures', {}, 'test')
        response.content = b'x'*10_000_001
        with patch('requests.get', return_value=response):
            with self.assertRaisesRegex(FetchError, 'size limit'):api.transport('/fixtures', {}, 'test')

    def test_collector_cli_success_partial_missing_key_and_lock(self):
        from collect_api_football_data import main
        args = ['--cache', str(self.cache), '--leagues', 'EPL', '--stats-limit', '0']
        with patch('collect_api_football_data.load_api_keys'), patch.dict('os.environ', {'API_FOOTBALL_KEY': 'test'}):
            with patch('collect_api_football_data.collect', return_value={'status': 'complete'}):
                self.assertEqual(main(args), 0)
            with patch('collect_api_football_data.collect', return_value={'status': 'partial'}):
                self.assertEqual(main(args), 1)
            with patch.dict('os.environ', {'API_FOOTBALL_KEY': ''}):
                self.assertEqual(main(args), 2)
            (self.cache/'api_football/.collect.lock').mkdir()
            self.assertEqual(main(args), 2)
        (self.cache/'api_football/.collect.lock').rmdir()
        with self.assertRaises(SystemExit):main(args+['--stats-limit', '-1'])


if __name__ == '__main__':
    unittest.main()
