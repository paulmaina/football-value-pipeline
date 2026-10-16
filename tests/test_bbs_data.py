"""Offline contract and integration regressions; no credentials or network required."""
import copy
import json
from datetime import datetime, timedelta, timezone
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from bbs_data import Client, Deferred, FetchError, Store, collect, normal_match, normal_stats
from bbs_integration import build_dataset, read_existing, write_dataset
from collect_bbs_data import main

NOW = datetime(2026, 10, 15, 8, tzinfo=timezone.utc)


def match(mid='m1', day='2026-10-10', hg=2):
    return {'id': mid, 'sport': 'football', 'league': 'Premier League',
        'kickoff_utc': day+'T14:00:00Z', 'status': 'finished',
        'home': {'id': 'h1', 'name': 'Manchester United'},
        'away': {'id': 'a1', 'name': 'Arsenal'}, 'score': {'home': hg, 'away': 1}}


def base():
    return [{'league': 'EPL', 'Date': '2026-10-10', 'HomeTeam': 'Man United',
             'AwayTeam': 'Arsenal', 'FTHG': 2, 'FTAG': 1, 'Season': '2627', 'HS': '8'}]


class BbsTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.store = Store(self.root/'bbs')

    def tearDown(self):
        self.store.close()
        self.temp.cleanup()

    def client(self, sender, **kwargs):
        return Client(self.store, 'secret-do-not-log', sender=sender, clock=lambda: NOW,
                      sleeper=lambda _: None, **kwargs)

    def put_match(self, row=None, observed=NOW, league='EPL'):
        row = row or match()
        payload = normal_match(row, league, observed.isoformat(), {})
        payload['requested_season'] = 2026
        self.store.put('match', league, row['id'], observed.isoformat(), payload)
        return payload

    def test_cutoff_uses_instants_not_timestamp_string_order(self):
        self.store.put('team', 'EPL', 't', '2026-10-15T08:00:00Z', {'version': 1})
        self.store.put('team', 'EPL', 't', '2026-10-15T11:00:00.500000+03:00', {'version': 2})
        rows = self.store.latest('team', '2026-10-15T08:00:00.250000Z')
        self.assertEqual(rows[0]['payload']['version'], 1)
        self.assertEqual(self.store.latest('team', '2026-10-15T08:00:01Z')[0]['payload']['version'], 2)

    def test_coverage_outage_still_exports_checkpoint(self):
        def sender(path, params, key):
            if path == '/v1/coverage':
                return 503, {}, b'{}'
            if path == '/v1/standings':
                return 200, {}, b'{"data":{"standings":[]}}'
            return 200, {}, b'{"data":[]}'
        report = collect(self.client(sender), ['EPL'], [2026], 0)
        self.assertEqual(report['status'], 'partial')
        self.assertEqual(report['errors'][0]['scope'], 'coverage')
        self.assertIn('matches/EPL/2026/finished', report['completed_lists'])
        self.assertIn('player/EPL', report['completed_lists'])

    def test_freshness_reports_missing_and_observation_age(self):
        self.put_match()
        out = build_dataset(self.store, base(), (NOW + timedelta(hours=2)).isoformat())
        report = out['report']['observation_freshness']
        self.assertEqual(report['match']['EPL']['oldest_observation_age_hours'], 2)
        self.assertEqual(report['statistics']['EPL']['records'], 0)
        self.assertIsNone(report['statistics']['EPL']['oldest_observation_age_hours'])

    def test_cache_keeps_observation_time_and_budget(self):
        calls = []
        c = self.client(lambda *a: (calls.append(a) or (200, {}, b'{"data":[]}')))
        first = c.get('/v1/teams', {'league': 'epl'})
        second = c.get('/v1/teams', {'league': 'epl'})
        self.assertEqual(first, second)
        self.assertEqual(len(calls), 1)
        self.assertEqual(self.store.state['quota'][NOW.date().isoformat()], 1)
        self.assertNotIn('secret-do-not-log', self.store.latest_response(first[2])['payload'])

    def test_quota_survives_new_client_and_failed_request(self):
        c = self.client(lambda *a: (403, {}, b'secret-do-not-log'), budget=1, max_requests=1)
        with self.assertRaises(FetchError) as error:
            c.get('/v1/teams')
        self.assertNotIn('secret-do-not-log', str(error.exception))
        other = self.client(lambda *a: self.fail('must not request'), budget=1, max_requests=1)
        with self.assertRaises(Deferred):
            other.get('/v1/other-teams')

    def test_429_and_header_zero_defer_across_runs(self):
        c = self.client(lambda *a: (429, {'Retry-After': '600'}, b'{}'))
        with self.assertRaises(Deferred):
            c.get('/v1/teams')
        with self.assertRaises(Deferred):
            self.client(lambda *a: self.fail('cooldown')).get('/v1/teams')
        self.store.set('blocked_until', 0)
        c = self.client(lambda *a: (200, {'X-RateLimit-Remaining': '0',
                'X-RateLimit-Reset': str(NOW.timestamp()+60)}, b'{"data":[]}'))
        c.get('/v1/teams')
        with self.assertRaises(Deferred):
            c.get('/v1/players')

    def test_retry_and_no_retry_on_auth_or_redirect(self):
        calls = []
        def sender(*a):
            calls.append(a)
            return (503, {}, b'{}') if len(calls) < 3 else (200, {}, b'{"data":[]}')
        self.client(sender).get('/v1/teams')
        self.assertEqual(len(calls), 3)
        for status in (401, 403, 302):
            calls.clear()
            def fail(*a):
                calls.append(a)
                return status, {}, b'{}'
            with self.assertRaises(FetchError):
                self.client(fail).get('/v1/players', {'case': status}, ttl=0)
            self.assertEqual(len(calls), 1)

    def test_invalid_envelopes_and_ignored_filter(self):
        for body in (b'[]', b'{"data":NaN}', b'{"error":{}}',
                     b'{"data":[],"meta":{"ignored_params":["league"]}}'):
            with self.subTest(body=body), self.assertRaises(FetchError):
                self.client(lambda *a: (200, {}, body)).get('/v1/matches', {'league':'epl'})

    def test_pagination_top_level_and_repeated_page(self):
        def sender(path, params, key):
            offset = params['offset']
            return 200, {}, json.dumps({'data': [{'id': str(offset)}], 'pagination': {'total': 2}}).encode()
        pages = list(self.client(sender).pages('/v1/players', {}))
        self.assertEqual([p[0][0]['id'] for p in pages], ['0', '1'])
        def repeated(*a):
            return 200, {}, b'{"data":[{"id":"x"}],"meta":{"total":2}}'
        with self.assertRaises(FetchError):
            list(self.client(repeated).pages('/v1/teams', {}))

    def test_truncated_page_not_complete(self):
        with self.assertRaises(FetchError):
            list(self.client(lambda *a: (200, {}, b'{"data":[],"pagination":{"total":4}}')).pages('/v1/players', {}))

    def test_validation_and_unfamiliar_status(self):
        for change in ({'sport':'basketball'}, {'league':'La Liga'}, {'score':{'home':-1,'away':0}},
                       {'kickoff_utc':'2027-01-01T12:00:00Z'}):
            with self.subTest(change=change), self.assertRaises(ValueError):
                normal_match({**match(), **change}, 'EPL', NOW.isoformat(), {})
        row = {**match(), 'status':'new_unknown_state', 'score':None}
        self.assertEqual(normal_match(row, 'EPL', NOW.isoformat(), {})['status'], 'new_unknown_state')

    def test_statistics_null_zero_and_wrong_team(self):
        m = self.put_match()
        payload = {'data': {'home': {'team_id':'h1','total_shots':0}, 'away': None}, 'meta':{}}
        values = normal_stats(payload, m)
        self.assertEqual(values['home']['total_shots'], 0)
        self.assertIsNone(values['home']['shots_on_target'])
        self.assertIsNone(values['away'])
        for field,value in [('team_id','a1'),('total_shots',-1),('ball_possession',101),('total_shots',True)]:
            bad = copy.deepcopy(payload)
            bad['data']['home'][field] = value
            with self.assertRaises(ValueError): normal_stats(bad,m)
        payload['data']['home'].update(total_shots=2,shots_on_target=3)
        with self.assertRaises(ValueError): normal_stats(payload,m)

    def test_repeat_import_enrichment_and_correction_history(self):
        self.put_match()
        self.put_match()
        self.assertEqual(len(self.store.latest('match')),1)
        self.store.put('statistics','EPL','m1',NOW.isoformat(),
            {'available':True,'team_ids':{'home':'h1','away':'a1'},'home':{'total_shots':9},'away':None})
        out = build_dataset(self.store,base(),NOW.isoformat())
        self.assertEqual(len(out['matches']),1)
        row=out['matches'][0]
        self.assertEqual(row['integration_status'],'matched')
        self.assertEqual(row['HS'],'8')
        self.assertEqual(row['bbs_home_total_shots'],9)
        self.assertEqual(out['report']['issues'][0]['type'],'statistic_conflict')
        self.put_match(match(hg=3),NOW+timedelta(days=1))
        old=build_dataset(self.store,base(),NOW.isoformat())
        new=build_dataset(self.store,base(),(NOW+timedelta(days=1)).isoformat())
        self.assertEqual(old['matches'][0]['integration_status'],'matched')
        self.assertEqual(new['matches'][0]['integration_status'],'conflict')
        self.assertEqual(new['matches'][0]['FTHG'],2)
        self.assertFalse(new['matches'][0]['bbs_statistics_available'])

    def test_corrected_fixture_cannot_reuse_other_teams_statistics(self):
        self.put_match()
        self.store.put('statistics','EPL','m1',NOW.isoformat(),
            {'available':True,'team_ids':{'home':'wrong','away':'a1'},
             'home':{'total_shots':9},'away':None})
        out=build_dataset(self.store,base(),NOW.isoformat())
        self.assertFalse(out['matches'][0]['bbs_statistics_available'])
        self.assertEqual(out['report']['issues'][0]['type'],'statistics_identity_conflict')
        with self.assertRaises(ValueError):
            build_dataset(self.store,base(),NOW.isoformat(),{'EPL': []})

    def test_ambiguous_mapping_and_duplicate_provider_fixture(self):
        self.put_match()
        self.put_match(match(mid='m2'))
        out=build_dataset(self.store,base(),NOW.isoformat())
        self.assertEqual(len(out['matches']),1)
        self.assertEqual(out['report']['join_counts'],{'ambiguous':2})
        self.assertIsNone(out['matches'][0]['bbs_match_id'])

    def test_date_change_and_non_finished_never_add_training(self):
        self.put_match(match(day='2026-10-11'))
        out=build_dataset(self.store,base(),NOW.isoformat())
        self.assertEqual(len(out['matches']),1)
        self.assertEqual(out['report']['join_counts'],{'date_conflict':1})
        self.put_match({**match(), 'status':'postponed', 'score':None},NOW+timedelta(hours=1))
        out=build_dataset(self.store,base(),(NOW+timedelta(hours=1)).isoformat())
        self.assertEqual(out['matches'][0]['integration_status'],'conflict')

    def test_new_results_require_mapping_and_regulation(self):
        row=match(day='2026-10-11')
        row['away']={'id':'a2','name':'Chelsea'}
        self.put_match(row)
        out=build_dataset(self.store,base(),NOW.isoformat())
        self.assertEqual(len(out['matches']),1)
        out=build_dataset(self.store,base(),NOW.isoformat(),{'EPL':{'a2':'Chelsea'}})
        self.assertEqual(len(out['matches']),2)
        self.assertEqual(out['matches'][1]['integration_status'],'added')
        row['league']='UEFA Champions League'
        self.put_match(row,league='UCL')
        out=build_dataset(self.store,base(),NOW.isoformat(),{'UCL':{'h1':'Man United','a2':'Chelsea'}})
        self.assertIn('regulation_score_unknown',[x['type'] for x in out['report']['issues']])

    def test_future_observation_cannot_leak_into_export(self):
        self.put_match(observed=NOW+timedelta(days=1))
        out=build_dataset(self.store,base(),NOW.isoformat())
        self.assertEqual(out['report']['bbs_matches'],0)
        self.assertEqual(out['matches'][0]['integration_status'],'existing_only')

    def test_baseline_duplicate_rejected(self):
        with self.assertRaises(ValueError):
            build_dataset(self.store,base()*2,NOW.isoformat())

    def test_read_existing_csv_and_ucl_regulation(self):
        (self.root/'2627_E0.csv').write_text('Date,HomeTeam,AwayTeam,FTHG,FTAG,HS\n10/10/2026,Man United,Arsenal,2,1,8\n')
        payload={'matches':[{'status':'FINISHED','utcDate':'2026-10-10T19:00:00Z',
            'homeTeam':{'name':'A'},'awayTeam':{'name':'B'},
            'score':{'duration':'EXTRA_TIME','fullTime':{'home':3,'away':2},'regularTime':{'home':2,'away':2}}}]}
        (self.root/'fdorg_history_UCL_2026.json').write_text(json.dumps(payload))
        rows=read_existing(self.root)
        self.assertEqual(len(rows),2)
        self.assertEqual(rows[1]['FTHG'],2)
        (self.root/'2627_E0.csv').write_text('Date,HomeTeam,AwayTeam,FTHG,FTAG\n10/10/2026,A,B,-1,1\n')
        with self.assertRaises(ValueError): read_existing(self.root)

    def test_complete_collection_and_offline_cli(self):
        def sender(path,params,key):
            if path=='/v1/coverage': body={'data':{'football':{}}}
            elif path=='/v1/matches': body={'data':[match()] if params['status']=='finished' else []}
            elif path=='/v1/standings': body={'data':{'standings':[{'league_name':'Premier League',
                'sport':'football','season':'2026','rows':[]}]}}
            elif path.endswith('/statistics'): body={'data':{'home':{'team_id':'h1','total_shots':0},'away':None}}
            else: body={'data':[{'id':path,'name':'Example','sport':'football'}]}
            return 200,{},json.dumps(body).encode()
        report=collect(self.client(sender),['EPL'],[2026],1)
        self.assertEqual(report['status'],'complete')
        self.assertEqual(len(self.store.latest('player')),1)
        self.assertEqual(len(self.store.latest('standings')),1)
        # Cached observations require no quota; a later request limit still reports
        # the statistics already processed before the deferred endpoint.
        limited = self.client(sender, budget=10, max_requests=1)
        for path in (self.store.path/'responses').glob('*.json'):
            if json.loads(path.read_text())['query'].startswith(('/v1/teams?', '/v1/players?')):
                path.unlink()
        partial = collect(limited, ['EPL'], [2026], 1)
        self.assertEqual(partial['status'], 'partial')
        self.assertEqual(partial['statistics_fetched'], 0)
        (self.root/'2627_E0.csv').write_text('Date,HomeTeam,AwayTeam,FTHG,FTAG\n10/10/2026,Man United,Arsenal,2,1\n')
        with patch('bbs_data.transport',side_effect=AssertionError('offline network')):
            code=main(['--offline','--store',str(self.root/'bbs'),'--existing-cache',str(self.root),
                       '--output',str(self.root/'out'),'--as-of',NOW.isoformat()])
        self.assertEqual(code,0)
        manifest=json.loads((self.root/'out/latest.json').read_text())
        import csv
        rows=list(csv.DictReader((self.root/'out'/manifest['generation']/'EPL_enriched_history.csv').open()))
        self.assertEqual(rows[0]['bbs_home_total_shots'],'0')
        dataset=build_dataset(self.store,read_existing(self.root),NOW.isoformat())
        generation=write_dataset(dataset,self.root/'second')
        self.assertEqual(write_dataset(dataset,self.root/'second'),generation)

    def test_partial_collection_and_lock(self):
        report=collect(self.client(lambda *a:(200,{},b'{"data":[]}'),budget=1,max_requests=1),['EPL'],[2026])
        self.assertEqual(report['status'],'partial')
        self.assertIn('deferred',report)
        self.root.joinpath('bbs.lock').touch()
        self.assertEqual(main(['--offline','--store',str(self.root/'bbs')]),2)


if __name__=='__main__': unittest.main()
