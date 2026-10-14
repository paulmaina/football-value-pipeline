import copy
from datetime import timedelta
import hashlib
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import numpy as np
import pandas as pd
import totals_anchor_experiment as t
from benchmark_forward_experiment import simplex
from historical_benchmark import adjusted_matrix,goals
from football_value_pipeline_v2_standalone import reweight_matrix_to_1x2,TheOddsAPI
from performance_tracking import fixture_key,capture,snapshots,write_json,verified_record
from test_benchmark_forward_experiment import frame,NOW
from test_performance_tracking import final


def sample():
    row=frame().iloc[0].to_dict();row.update(lambda_home=1.7,lambda_away=.9,odds_event_id='abc')
    m=reweight_matrix_to_1x2(adjusted_matrix(1.7,.9,-.04,10),simplex(row,'p_'))
    for k,v in goals(m).items():row['p_'+k]=v
    ref={'bookmaker':'pinnacle','updated_at_utc':NOW.isoformat(),'over':1.95,'under':1.95,'event_id':'abc','kickoff_utc':row['kickoff_utc'],'home_team':row['home_team'],'away_team':row['away_team']}
    inputs={'lambda_home':1.7,'lambda_away':.9,'rho':-.04,'max_goals':10,'reference':ref}
    return row,m,inputs


class TotalsTests(unittest.TestCase):
    def test_anchor_matches_totals_preserves_hda_and_production(self):
        row,m,inputs=sample();before=m.copy();r,_=t.registry();d=t.decision(row,m,inputs,NOW,r)
        self.assertEqual(d['status'],'available');self.assertAlmostEqual(d['candidate_goals']['over_2_5'],.5,places=7);np.testing.assert_array_equal(before,m)
        from historical_benchmark import anchor_totals
        anchored,_=anchor_totals(1.7,.9,-.04,simplex(row,'p_'),.5,10);h,a=np.indices(m.shape)
        self.assertAlmostEqual(anchored[h>a].sum(),row['p_home'],places=8)
        self.assertNotEqual(d['baseline_goals']['under_3_5'],d['candidate_goals']['under_3_5'])

    def test_missing_stale_mismatched_and_invalid_inputs_fail_closed(self):
        row,m,inputs=sample();r,_=t.registry()
        for field,value in [('bookmaker','1xbet'),('updated_at_utc',(NOW-timedelta(minutes=11)).isoformat()),('updated_at_utc',(NOW+timedelta(seconds=1)).isoformat()),('event_id','wrong'),('home_team','wrong'),('over',1.0),('kickoff_utc',NOW.isoformat())]:
            altered=copy.deepcopy(inputs);altered['reference'][field]=value
            self.assertEqual(t.decision(row,m,altered,NOW,r)['status'],'unavailable',field)
        self.assertEqual(t.decision(row,m,{**inputs,'reference':float('nan')},NOW,r)['status'],'unavailable')
        for bad in (None,np.zeros((11,11)),np.full((11,11),np.nan)):
            self.assertEqual(t.decision(row,bad,inputs,NOW,r)['status'],'unavailable')
        altered=copy.deepcopy(inputs);altered['rho']=.5
        self.assertEqual(t.decision(row,m,altered,NOW,r)['status'],'unavailable')
        self.assertFalse(t.equivalent(float('nan'),float('nan')));self.assertTrue(t.equivalent([.5], [.5+1e-12]))

    def test_capture_grade_and_tamper_isolated_from_baseline(self):
        row,m,inputs=sample();key=fixture_key(row)
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);raw=root/'raw';raw.mkdir();data=pd.DataFrame([row]);data.to_csv(raw/'all_leagues_predictions.csv',index=False);pd.DataFrame(columns=['decision']).to_csv(raw/'conservative_bet_shortlist.csv',index=False);write_json(raw/'conservative_bet_summary.json',{'generated_at_utc':NOW.isoformat()})
            before=(raw/'all_leagues_predictions.csv').read_bytes();d=t.write_experiment(data,raw,NOW.isoformat(),{key:m},{key:inputs});self.assertIsNotNone(t.capture_file(raw,NOW.isoformat()))
            capture('c'*40,root=root,captured_at=NOW+timedelta(minutes=1));capture('d'*40,root=root,captured_at=NOW+timedelta(minutes=2));archive=snapshots(root)
            f=final(h=4,a=1);f['utcDate']=row['kickoff_utc'];rec=verified_record('PL',f);write_json(root/'performance/verified_results.json',{'x':rec})
            s=t.review_experiment(root,archive,[rec],NOW+timedelta(days=3));self.assertEqual(s['paired_fixtures'],1);self.assertTrue(t.validate_report(root));self.assertEqual(before,(raw/'all_leagues_predictions.csv').read_bytes())
            s['paired_fixtures']=999;write_json(root/'performance/totals_anchor_experiment/summary.json',s)
            with self.assertRaises(ValueError):t.validate_report(root)
            t.review_experiment(root,archive,[rec],NOW);self.assertTrue(t.validate_report(root));self.assertEqual(t.evaluate(root,archive,[rec],NOW)[0]['paired_fixtures'],0)
            path=root/'performance/snapshots'/('c'*16)/t.FILE;path.write_text('{}');self.assertEqual(len(snapshots(root)),2);self.assertIn('c'*40,t.evaluate(root,snapshots(root),[rec],NOW+timedelta(days=3))[0]['rejected_snapshot_commits'])
            d['rows'][0]['candidate_goals']['over_2_5']=.9
            with self.assertRaises(ValueError):t.validate(d,NOW.isoformat(),[row])
            with self.assertRaises(ValueError):t.validate({**d,'registry_sha256':'bad'},NOW.isoformat(),[row])

    def test_pinnacle_reference_is_separate_from_production_reference(self):
        row,_,inputs=sample();ref=inputs['reference'];payload={'id':'abc','home_team':row['home_team'],'away_team':row['away_team'],'commence_time':row['kickoff_utc'],'bookmakers':[{'key':'pinnacle','title':'Pinnacle','markets':[{'key':'totals','last_update':NOW.isoformat(),'outcomes':[{'name':'Over','point':2.5,'price':1.95},{'name':'Under','point':2.5,'price':1.95}]}]},{'key':'other','title':'Other','markets':[{'key':'totals','last_update':(NOW+timedelta(seconds=1)).isoformat(),'outcomes':[{'name':'Over','point':2.5,'price':2.0},{'name':'Under','point':2.5,'price':1.9}]}]}]}
        flat=TheOddsAPI.flatten_odds_event(payload);self.assertEqual(flat['live_ref_ou25_bookmaker'],'Other');self.assertEqual(flat['shadow_pinnacle_totals'],ref)

    def test_readiness_positive_and_negative_results(self):
        row,m,inputs=sample();r,sha=t.registry();observations=[];records=[]
        from benchmark_forward_experiment import registry_hash
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            for i in range(300):
                item={**row,'home_team':f'H{i}','away_team':f'A{i}','kickoff_utc':(NOW+timedelta(days=i%42+1)).isoformat()};key=fixture_key(item);year,week,_=__import__('performance_tracking').utc(item['kickoff_utc']).isocalendar()
                observations.append({**item,'status':'available','baseline_goals':{'under_3_5':.99,'over_1_5':.01,'btts_yes':.01,'over_2_5':.01},'candidate_goals':{'under_3_5':.1,'over_1_5':.9,'btts_yes':.9,'over_2_5':.9}})
                f=final(h=3,a=2);f['id']=i+1000;f['homeTeam']['name']=item['home_team'];f['awayTeam']['name']=item['away_team'];f['utcDate']=item['kickoff_utc'];records.append(verified_record('PL',f))
            # Exercise gates through a valid archived trial without solving 300 matrices.
            fake={'version':t.VERSION,'registry':r,'registry_sha256':sha,'generated_at_utc':NOW.isoformat(),'predictions_sha256':'x','rows':observations}
            directory=root/'performance/snapshots'/('e'*16);directory.mkdir(parents=True);write_json(directory/t.FILE,fake);(directory/'predictions.csv').write_text('x')
            meta={'git_commit_sha':'e'*40,'generated_at_utc':NOW.isoformat(),'captured_at_utc':NOW.isoformat(),'sha256':{t.FILE:hashlib.sha256((directory/t.FILE).read_bytes()).hexdigest()}}
            # Different dates need their own eligible generation window; move all into 72h and reduce gate for explicit unit gate branch.
            r['review_gates']['minimum_paired_fixtures']=2;r['review_gates']['minimum_gameweeks']=1
            for x in observations:x['kickoff_utc']=row['kickoff_utc']
            for rec in records:rec['kickoff_utc']=row['kickoff_utc']
            fake['rows']=observations;write_json(directory/t.FILE,fake);meta['sha256'][t.FILE]=hashlib.sha256((directory/t.FILE).read_bytes()).hexdigest()
            with patch.object(t,'registry',return_value=(r,sha)),patch.object(t,'validate'),patch('forecast_integrity.forecast_digest_variants',return_value={'x'}):
                s,g,c=t.evaluate(root,[(meta,[],[])],records,NOW+timedelta(days=4));self.assertEqual(s['paired_fixtures'],300);self.assertEqual(s['status'],'READY_FOR_REVIEW');self.assertFalse(s['automatic_production_change'])
