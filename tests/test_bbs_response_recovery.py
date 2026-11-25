"""Record quarantine, duplicate fixtures and primary-history reconciliation."""
import json
import tempfile
import unittest
from pathlib import Path
from datetime import timedelta
from bbs_data import Store, Client, collect, normal_match
from bbs_integration import build_dataset
from tests.test_bbs_data import NOW, base, match


class ResponseRecoveryTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory()
        self.store=Store(Path(self.temp.name)/'state')

    def tearDown(self):
        self.temp.cleanup()

    def test_invalid_record_does_not_discard_valid_neighbors(self):
        bad={**match(mid='bad'),'score':None,'score_status':'unavailable'}
        def sender(path,params,key):
            data=[bad,match(mid='good')] if path=='/v1/matches' and params['status']=='finished' else []
            return 200,{},json.dumps({'data':data}).encode()
        client=Client(self.store,'test',sender=sender,clock=lambda:NOW,sleeper=lambda _:None)
        report=collect(client,['EPL'],[2026])
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

    def test_collection_excludes_quarantine_and_unrequested_seasons(self):
        for mid,season,day in [('held',2026,'2026-10-10'),('old',2025,'2025-10-10'),('good',2026,'2026-10-11')]:
            value=normal_match(match(mid=mid,day=day),'EPL',NOW.isoformat(),{})
            value['requested_season']=season
            self.store.put('match','EPL',mid,NOW.isoformat(),value)
        self.store.put('quarantine','EPL','held',NOW.isoformat(),{'reason':'unavailable correction'})
        calls=[]
        def sender(path,params,key):
            calls.append(path)
            return 200,{},json.dumps({'data':[]}).encode()
        client=Client(self.store,'test',sender=sender,clock=lambda:NOW,sleeper=lambda _:None)
        report=collect(client,['EPL'],[2026])
        self.assertEqual(set(calls),{'/v1/matches','/v1/teams'})
        self.assertEqual(report['coverage']['EPL']['completed_matches'],1)
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

    def test_loader_keeps_primary_columns_and_adds_only_match_metadata(self):
        import pandas as pd
        from bbs_integration import write_dataset, combined_training_history
        value=normal_match(match(),'EPL',NOW.isoformat(),{});value['requested_season']=2026
        self.store.put('match','EPL','m1',NOW.isoformat(),value)
        out=build_dataset(self.store,base(),NOW.isoformat())
        cache=Path(self.temp.name)/'cache'
        write_dataset(out,cache/'bbs/combined')
        fresh=pd.DataFrame(base());fresh.loc[0,'HS']='10'
        row=combined_training_history(fresh,cache,'EPL',NOW,3).iloc[0]
        self.assertEqual(row['HS'],'10')
        self.assertEqual((row['FTHG'],row['FTAG']),(2,1))
        self.assertEqual(row['bbs_match_id'],'m1')
        self.assertEqual(row['integration_status'],'matched')
        self.assertFalse([c for c in row.index if 'statistic' in c])


if __name__=='__main__': unittest.main()
