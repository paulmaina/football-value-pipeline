"""Regressions for gaps exposed by the first real BBS collection."""
import copy
import json
import tempfile
import unittest
from datetime import timedelta
from pathlib import Path

from bbs_data import Client, FetchError, Store, collect, normal_match
from bbs_integration import build_dataset
from tests.test_bbs_data import NOW, base, match


class LiveCoverageTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.store = Store(Path(self.temp.name)/'state')

    def tearDown(self):
        self.temp.cleanup()

    def client(self, sender, **kwargs):
        return Client(self.store, 'offline-key', sender=sender, clock=lambda: NOW,
                      sleeper=lambda _: None, **kwargs)

    def test_upcoming_only_response_never_claims_training_complete(self):
        upcoming = {**match(day='2026-10-17'), 'status': 'scheduled', 'score': None}
        def sender(path, params, key):
            if path == '/v1/matches': payload = {'data': [upcoming]}
            elif path == '/v1/standings': payload = {'data': {'standings': []}}
            else: payload = {'data': []}
            return 200, {}, json.dumps(payload).encode()
        report = collect(self.client(sender), ['EPL'], [2026])
        self.assertEqual(report['status'], 'partial')
        self.assertEqual(report['coverage']['EPL']['completed_matches'], 0)
        self.assertEqual(report['statistics_fetched'], 0)
        self.assertTrue(any('status was not honored' in e['error'] for e in report['errors']))

    def test_two_hundred_record_pages_do_not_truncate_history(self):
        offsets = []
        def sender(path, params, key):
            self.assertEqual(params['limit'], 200)
            offsets.append(params['offset'])
            rows = [{'id': str(i)} for i in range(params['offset'], min(params['offset']+200, 201))]
            return 200, {}, json.dumps({'data': rows, 'pagination': {'total': 201}}).encode()
        pages = list(self.client(sender).pages('/v1/matches', {}))
        self.assertEqual(offsets, [0, 200])
        self.assertEqual(sum(len(p[0]) for p in pages), 201)

    def test_statistics_are_fetched_before_directories_and_backlog_is_visible(self):
        calls = []
        def sender(path, params, key):
            calls.append((path, params.copy()))
            if path == '/v1/matches':
                data = [match()] if params['status'] == 'finished' else []
            elif path == '/v1/standings': data = {'standings': []}
            elif path.endswith('/statistics'): data = {'home': {'team_id':'h1','total_shots':0}, 'away':None}
            else: data = []
            return 200, {}, json.dumps({'data':data}).encode()
        report = collect(self.client(sender, max_requests=7), ['EPL'], [2026])
        self.assertEqual(report['statistics_fetched'], 1)
        self.assertEqual(report['coverage']['EPL']['statistics_available'], 1)
        self.assertEqual(report['status'], 'partial')  # Directories deferred by budget.
        self.assertTrue(calls[-1][0].endswith('/statistics'))
        self.assertIn('finished', [p['status'] for path,p in calls if path=='/v1/matches'])
        report = collect(self.client(sender), ['EPL'], [2026], stats_limit=0)
        self.assertEqual(report['coverage']['EPL']['statistics_missing'], 0)

    def test_fresh_statistics_do_not_consume_backfill_slots(self):
        calls = []
        def sender(path, params, key):
            calls.append(path)
            if path == '/v1/matches':
                data = [match(), match(mid='m2', day='2026-10-09')] if params['status']=='finished' else []
            elif path == '/v1/standings': data = {'standings':[]}
            elif path.endswith('/statistics'): data = {'home':{'team_id':'h1','total_shots':1},'away':None}
            else: data = []
            return 200, {}, json.dumps({'data':data}).encode()
        self.store.put('statistics','EPL','m1',NOW.isoformat(), {
            'available':True,'team_ids':{'home':'h1','away':'a1'},'home':{'total_shots':0},'away':None})
        report = collect(self.client(sender), ['EPL'], [2026], stats_limit=1)
        self.assertIn('/v1/matches/m2/statistics', calls)
        self.assertNotIn('/v1/matches/m1/statistics', calls)
        self.assertEqual(report['coverage']['EPL']['statistics_missing'],0)

    def test_forbidden_history_is_not_requested_again_until_cache_expiry(self):
        calls = []
        def sender(*args):
            calls.append(args)
            return 403, {}, b'{}'
        for _ in range(2):
            with self.assertRaises(FetchError):
                self.client(sender).get('/v1/matches', {'season':2025, 'status':'finished'})
        self.assertEqual(len(calls), 1)
        later = Client(self.store, 'offline-key', sender=lambda *a:(200,{},b'{"data":[]}'),
                       clock=lambda:NOW+timedelta(days=2), sleeper=lambda _:None)
        later.get('/v1/matches', {'season':2025, 'status':'finished'})
        self.assertEqual(later.requests, 1)

    def test_wrong_season_results_are_quarantined(self):
        def sender(path, params, key):
            if path == '/v1/matches': data = [match(day='2025-10-10')] if params['status']=='finished' else []
            elif path == '/v1/standings': data = {'standings':[]}
            else: data = []
            return 200, {}, json.dumps({'data':data}).encode()
        report = collect(self.client(sender), ['EPL'], [2026])
        self.assertEqual(report['status'], 'partial')
        self.assertFalse(self.store.latest('match'))
        self.assertTrue(any('season was not honored' in e['error'] for e in report['errors']))

    def test_reviewed_aliases_bridge_fixture_and_standings_ids(self):
        baseline = [dict(base()[0], league='UCL', HomeTeam='FK Shakhtar Donetsk', AwayTeam='AS Roma')]
        row = dict(match(), league='UEFA Champions League')
        row['home'] = {'id':'fixture-id', 'name':'Shakhtar Donetsk'}
        row['away'] = {'id':'away', 'name':'AS Roma'}
        value = normal_match(row, 'UCL', NOW.isoformat(), {})
        value['requested_season'] = 2026
        self.store.put('match','UCL','m1',NOW.isoformat(),value)
        standings = {'data':{'standings':[{'rows':[
            {'team_id':'standings-id','team_name':'Shakhtar Donetsk','games_played':1,'wins':1,
             'ties':0,'losses':0,'points_for':2,'points_against':1}]}]}}
        self.store.put('standings','UCL','2026',NOW.isoformat(),standings)
        out = build_dataset(self.store, baseline, NOW.isoformat())
        self.assertEqual(out['report']['join_counts'], {'matched':1})
        self.assertEqual(out['report']['standings_checks'][0]['compared_teams'], 1)
        self.assertFalse(out['report']['standings_checks'][0]['unmapped_teams'])
        self.assertFalse(out['report']['standings_checks'][0]['differences'])
        self.assertEqual(len([m for m in out['team_mappings'] if m['name']=='FK Shakhtar Donetsk']), 2)
        changed = copy.deepcopy(standings)
        changed['data']['standings'][0]['rows'][0]['points_for']=3
        self.store.put('standings','UCL','2026',(NOW+timedelta(hours=1)).isoformat(),changed)
        out=build_dataset(self.store,baseline,(NOW+timedelta(hours=1)).isoformat())
        self.assertEqual(out['report']['data_quality_status'], 'partial')
        self.assertEqual(out['report']['standings_checks'][0]['differences'][0]['field'], 'points_for')

    def test_existing_results_without_bbs_confirmation_are_visible(self):
        row = {**match(day='2026-10-17'), 'status':'scheduled','score':None}
        value=normal_match(row,'EPL',NOW.isoformat(),{})
        value['requested_season']=2026
        self.store.put('match','EPL','m1',NOW.isoformat(),value)
        out=build_dataset(self.store,base(),NOW.isoformat())
        self.assertEqual(out['report']['training_coverage'][0]['existing_results_without_bbs_confirmation'],1)
        self.assertEqual(out['report']['data_quality_status'],'partial')


if __name__ == '__main__': unittest.main()
