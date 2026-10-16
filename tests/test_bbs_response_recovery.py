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

    def test_matching_id_cannot_override_contradictory_name(self):
        payload={'data':{'home':{'team_id':'h1','team_name':'Arsenal','total_shots':1}}}
        with self.assertRaisesRegex(ValueError,'name contradicts'):
            normal_stats(payload,match())
        payload['data']['home']['team_name']='Man United'
        self.assertTrue(normal_stats(payload,match())['available'])

    def test_empty_statistics_are_unavailable_but_zero_is_real_data(self):
        payload={'data':{'home':{'team_id':'h1'},'away':{'team_id':'a1'}}}
        out=normal_stats(payload,match())
        self.assertFalse(out['available'])
        self.assertIsNone(out['home'])
        payload['data']['home']['total_shots']=0
        out=normal_stats(payload,match())
        self.assertTrue(out['available'])
        self.assertEqual(out['home']['total_shots'],0)
        self.assertIsNone(out['away'])

    def test_collection_excludes_quarantine_and_unrequested_seasons(self):
        for mid,season,day in [('held',2026,'2026-10-10'),('old',2025,'2025-10-10'),('good',2026,'2026-10-11')]:
            value=normal_match(match(mid=mid,day=day),'EPL',NOW.isoformat(),{})
            value['requested_season']=season
            self.store.put('match','EPL',mid,NOW.isoformat(),value)
        self.store.put('quarantine','EPL','held',NOW.isoformat(),{'reason':'unavailable correction'})
        calls=[]
        def sender(path,params,key):
            calls.append(path)
            if path=='/v1/standings': data={'standings':[]}
            elif path.endswith('/statistics'): data={'home':{'team_id':'h1','total_shots':1}}
            else: data=[]
            return 200,{},json.dumps({'data':data}).encode()
        client=Client(self.store,'test',sender=sender,clock=lambda:NOW,sleeper=lambda _:None)
        report=collect(client,['EPL'],[2026])
        self.assertEqual([p for p in calls if p.endswith('/statistics')],['/v1/matches/good/statistics'])
        self.assertEqual(report['coverage']['EPL']['completed_matches'],1)
        self.assertEqual(report['coverage']['EPL']['statistics_available'],1)
        self.assertFalse(report['errors'])
        self.assertEqual(report['status'],'partial')

    def test_completed_duplicate_dates_are_both_held_before_training(self):
        baseline=base()+[{**base()[0],'AwayTeam':'Chelsea','Date':'2026-10-09'}]
        for mid,day in [('first','2026-10-11'),('second','2026-10-12')]:
            value=match(mid=mid,day=day)
            value['away']={'id':'c1','name':'Chelsea'}
            value=normal_match(value,'EPL',NOW.isoformat(),{})
            value['requested_season']=2026
            self.store.put('match','EPL',mid,NOW.isoformat(),value)
        # Remove the same-pair baseline while retaining both club identities.
        baseline[1]['HomeTeam']='Arsenal'
        out=build_dataset(self.store,baseline,NOW.isoformat())
        self.assertEqual(len(out['matches']),2)
        self.assertEqual([f['join_status'] for f in out['fixtures']],['ambiguous','ambiguous'])
        self.assertEqual(sum(i['type']=='duplicate_provider_fixture' for i in out['report']['issues']),2)

    def test_loader_rechecks_new_primary_statistics_without_overwriting_them(self):
        import pandas as pd
        from bbs_integration import write_dataset, combined_training_history
        value=normal_match(match(),'EPL',NOW.isoformat(),{});value['requested_season']=2026
        self.store.put('match','EPL','m1',NOW.isoformat(),value)
        self.store.put('statistics','EPL','m1',NOW.isoformat(),{'available':True,
            'team_ids':{'home':'h1','away':'a1'},'home':{'total_shots':8},'away':{'total_shots':3}})
        out=build_dataset(self.store,base(),NOW.isoformat())
        self.assertTrue(out['matches'][0]['bbs_statistics_feature_eligible'])
        cache=Path(self.temp.name)/'cache'
        write_dataset(out,cache/'bbs/combined')
        for source,expected_dispute in [('10',True),('-',True),(float('nan'),False)]:
            with self.subTest(source=source):
                fresh=pd.DataFrame(base());fresh.loc[0,'HS']=source
                row=combined_training_history(fresh,cache,'EPL',NOW,3).iloc[0]
                self.assertEqual(row['bbs_home_total_shots'],8)
                if expected_dispute:
                    self.assertEqual(row['HS'],source)
                    self.assertEqual(row['bbs_disputed_fields'],'HS')
                    self.assertIn('statistic_conflict',row['bbs_conflict_flags'])
                    self.assertFalse(row['bbs_statistics_feature_eligible'])
                else:
                    self.assertTrue(pd.isna(row['HS']))
                    self.assertTrue(row['bbs_statistics_feature_eligible'])



if __name__=='__main__': unittest.main()
