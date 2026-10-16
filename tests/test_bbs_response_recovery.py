"""Missing IDs, record quarantine and unresolved statistical conflicts."""
import copy
import json
import tempfile
import unittest
from pathlib import Path
from datetime import timedelta
from bbs_data import Store, Client, collect, normal_match, normal_stats
from bbs_integration import build_dataset
from tests.test_bbs_data import NOW, base, match


class ResponseRecoveryTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory()
        self.store=Store(Path(self.temp.name)/'state')

    def tearDown(self):
        self.temp.cleanup()

    def test_missing_ids_require_verified_names_but_wrong_ids_still_fail(self):
        row=match()
        row['home']={'id':'h1','name':'Coventry City'}
        row['away']={'id':'a1','name':'Newcastle United'}
        payload={'data':{'home':{'team_id':None,'team_name':'Coventry','total_shots':0},
                         'away':{'team_id':None,'team_name':'Newcastle','total_shots':2}}}
        value=normal_stats(payload,row)
        self.assertEqual(value['identity_resolution']['home'],'verified_name')
        self.assertIsNone(value['provider_team_ids']['home'])
        self.assertEqual(value['home']['total_shots'],0)
        for change in ({'team_id':'wrong'}, {'team_name':'Arsenal'}, {'team_name':None}):
            bad=copy.deepcopy(payload);bad['data']['home'].update(change)
            with self.assertRaises(ValueError): normal_stats(bad,row)

    def test_invalid_record_does_not_discard_valid_neighbors(self):
        bad={**match(mid='bad'),'score':None,'score_status':'unavailable'}
        def sender(path,params,key):
            if path=='/v1/matches': data=[bad,match(mid='good')] if params['status']=='finished' else []
            elif path=='/v1/standings': data={'standings':[]}
            else: data=[]
            return 200,{},json.dumps({'data':data}).encode()
        client=Client(self.store,'test',sender=sender,clock=lambda:NOW,sleeper=lambda _:None)
        report=collect(client,['EPL'],[2026],stats_limit=0)
        self.assertEqual([x['entity'] for x in self.store.latest('match')],['good'])
        self.assertEqual(report['quarantined_records'][0]['bbs_match_id'],'bad')
        self.assertIn('matches/EPL/2026/finished',report['completed_lists'])
        self.assertEqual(report['status'],'partial')

    def test_quarantined_correction_holds_old_bbs_data_until_new_valid_record(self):
        value=normal_match(match(),'EPL',NOW.isoformat(),{});value['requested_season']=2026
        self.store.put('match','EPL','m1',NOW.isoformat(),value)
        later=NOW+timedelta(hours=1)
        self.store.put('quarantine','EPL','m1',later.isoformat(),{'reason':'score unavailable'})
        out=build_dataset(self.store,base(),later.isoformat())
        self.assertEqual(out['matches'][0]['integration_status'],'existing_only')
        self.assertEqual(len(out['report']['quarantined_records']),1)
        self.store.put('match','EPL','m1',(later+timedelta(seconds=1)).isoformat(),value)
        out=build_dataset(self.store,base(),(later+timedelta(seconds=2)).isoformat())
        self.assertEqual(out['matches'][0]['integration_status'],'matched')
        self.assertFalse(out['report']['quarantined_records'])

    def test_disputed_statistics_are_retained_but_not_feature_eligible(self):
        value=normal_match(match(),'EPL',NOW.isoformat(),{});value['requested_season']=2026
        self.store.put('match','EPL','m1',NOW.isoformat(),value)
        self.store.put('statistics','EPL','m1',NOW.isoformat(),{'available':True,
            'team_ids':{'home':'h1','away':'a1'},'home':{'total_shots':9},'away':{'total_shots':3}})
        out=build_dataset(self.store,base(),NOW.isoformat());row=out['matches'][0]
        self.assertEqual(row['HS'],'8')
        self.assertEqual(row['bbs_home_total_shots'],9)
        self.assertIn('HS',row['bbs_disputed_fields'])
        self.assertFalse(row['bbs_statistics_feature_eligible'])
        self.assertEqual(out['report']['statistic_reconciliation'][0]['policy'],'retain_primary_exclude_disputed_bbs')


if __name__=='__main__': unittest.main()
