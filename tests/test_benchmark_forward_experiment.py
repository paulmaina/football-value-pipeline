from offline_test_case import OfflineQuotePolicyTestCase
import base64
import copy
from datetime import datetime,timedelta,timezone
import hashlib
import json
import math
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import numpy as np
import pandas as pd

import benchmark_forward_experiment as bf
import experiment_review_queue as eq
from performance_tracking import capture,snapshots,write_json,verified_record
from test_conservative_bet_filter import fixture
from test_performance_tracking import final

NOW=datetime(2026,10,15,9,tzinfo=timezone.utc)


def frame():
    row=fixture(kickoff=NOW+timedelta(days=1));row.update(home_team='Manchester City FC',away_team='Everton FC',
        model_home_team='Manchester City FC',model_away_team='Everton FC',market_weight=.5,market_source_1x2='The Odds API / Pinnacle',
        odds_h2h_last_update_utc=(NOW-timedelta(minutes=5)).isoformat())
    for k,p in zip(('home','draw','away'),(.69,.185,.125)):row['p_'+k]=p
    return pd.DataFrame([row])


def setup(root):
    raw=root/'raw';raw.mkdir(parents=True);data=frame();data.to_csv(raw/'all_leagues_predictions.csv',index=False)
    data.iloc[:0].to_csv(raw/'conservative_bet_shortlist.csv',index=False)
    write_json(raw/'conservative_bet_summary.json',{'generated_at_utc':NOW.isoformat(),'selection_policy_version':'test'})
    result=bf.write_experiment(data,raw,NOW.isoformat());return raw,data,result


class ForwardBridgeTests(OfflineQuotePolicyTestCase):
    def test_missing_reference_round_trip_preserves_unavailable_evidence(self):
        from performance_tracking import read_csv
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);raw,data,_=setup(root)
            data['odds_h2h_last_update_utc']=None
            data['market_source_1x2']=None
            data.to_csv(raw/'all_leagues_predictions.csv',index=False)
            result=bf.write_experiment(data,raw,NOW.isoformat())
            bf.validate(result,NOW.isoformat(),read_csv(raw/'all_leagues_predictions.csv'))
            self.assertEqual(result['rows'][0]['status'],'unavailable')
            self.assertIsNotNone(bf.capture_file(raw,NOW.isoformat()))
            capture('f'*40,root=root,captured_at=NOW+timedelta(minutes=1))
            _,rejected=bf.frozen(root,snapshots(root));self.assertEqual(rejected,[])
            bad=copy.deepcopy(result)
            bad['rows'][0]['reference_updated_at_utc']=NOW.isoformat()
            with self.assertRaises(ValueError):
                bf.validate(bad,NOW.isoformat(),read_csv(raw/'all_leagues_predictions.csv'))

    def test_nomination_is_bound_and_changes_only_market_weight(self):
        r=bf.load_registry();self.assertEqual(r['market_weight'],.85)
        row=frame().iloc[0].to_dict();decision=bf.decision(row,r,NOW)
        self.assertEqual(decision['status'],'available');np.testing.assert_allclose(decision['candidate'],[.697,.1815,.1215])
        self.assertEqual(decision['baseline'],[.69,.185,.125])
        with patch.object(bf,'REGISTRY') as path:
            path.read_text.return_value=json.dumps({**r,'approval_required':False})
            with self.assertRaises(ValueError):bf.load_registry()
        with tempfile.TemporaryDirectory() as tmp:
            path=Path(tmp)/'registry.json';bad=copy.deepcopy(r);bad['selection']['source_sha256']='bad';bad['selection']['source']=str(Path(r['selection']['source']).resolve());path.write_text(json.dumps(bad))
            with patch.object(bf,'REGISTRY',path):
                with self.assertRaises(ValueError):bf.load_registry()

    def test_missing_stale_unknown_and_changed_baseline_fail_closed(self):
        row=frame().iloc[0].to_dict();r=bf.load_registry()
        for field,value in [('odds_h2h_last_update_utc',None),('market_weight',.7),('market_p_home',None),
            ('home_name_match_score',20),('model_home_team','__LEAGUE_AVERAGE__'),('league','UEFA Champions League'),
            ('market_reference_home_odds',1),('odds_source','cache'),('p_home',.7),('kickoff_utc',(NOW+timedelta(days=4)).isoformat())]:
            altered={**row,field:value};self.assertEqual(bf.decision(altered,r,NOW)['status'],'unavailable',field)
        altered={**row,'odds_h2h_last_update_utc':(NOW-timedelta(days=2)).isoformat()}
        self.assertIn('missing_stale_or_future_reference',bf.decision(altered,r,NOW)['reasons'])
        self.assertIsNone(bf.simplex({},'p_'))

    def test_capture_freeze_grading_and_tamper_preserves_baseline(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);raw,data,result=setup(root)
            before=(raw/'all_leagues_predictions.csv').read_bytes()
            self.assertIsNotNone(bf.capture_file(raw,NOW.isoformat()))
            self.assertTrue(capture('a'*40,root=root,captured_at=NOW+timedelta(minutes=1)))
            capture('b'*40,root=root,captured_at=NOW+timedelta(minutes=2))
            rows,rejected=bf.frozen(root,snapshots(root));self.assertEqual(len(rows),1);self.assertFalse(rejected)
            self.assertEqual(rows[0]['snapshot_commit'],'a'*40)
            f=final(h=2,a=1);f['utcDate']=data.iloc[0].kickoff_utc;rec=verified_record('PL',f)
            write_json(root/'performance/verified_results.json',{'PL:90002':rec})
            summary=bf.review_experiment(root,snapshots(root),[rec],NOW+timedelta(days=3))
            self.assertEqual(summary['paired_fixtures'],1);self.assertEqual(summary['status'],'COLLECT_MORE_DATA')
            self.assertTrue(bf.validate_report(root));self.assertEqual(before,(raw/'all_leagues_predictions.csv').read_bytes())
            bf.review_experiment(root,snapshots(root),[rec],NOW);self.assertTrue(bf.validate_report(root))
            self.assertEqual(json.loads((root/'performance/benchmark_forward_experiment/summary.json').read_text())['paired_fixtures'],0)
            summary['paired_fixtures']=999;write_json(root/'performance/benchmark_forward_experiment/summary.json',summary)
            with self.assertRaises(ValueError):bf.validate_report(root)
            path=root/'performance/snapshots'/('a'*16)/bf.FILE;path.write_text('{}')
            rows,rejected=bf.frozen(root,snapshots(root));self.assertIn('a'*40,rejected)
            self.assertEqual(len(snapshots(root)),2)

    def test_binding_rejects_retrofits_and_incomplete_coverage(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);raw,data,result=setup(root)
            for mutate in (lambda d:d['rows'][0]['candidate'].__setitem__(0,.9),lambda d:d['rows'].clear(),
                lambda d:d['rows'].append(copy.deepcopy(d['rows'][0])),lambda d:d.update(registry_sha256='bad'),
                lambda d:d['rows'][0].update(reference_source='invented')):
                altered=copy.deepcopy(result);mutate(altered)
                with self.assertRaises(ValueError):bf.validate(altered,NOW.isoformat(),data.to_dict('records'))
            with self.assertRaises(ValueError):bf.capture_file(raw,(NOW+timedelta(minutes=10)).isoformat())
            path=raw/'all_leagues_predictions.csv';path.write_bytes(path.read_bytes().replace(b'\n',b'\r\n'))
            self.assertIsNotNone(bf.capture_file(raw,NOW.isoformat()))
            path.write_bytes(path.read_bytes()+b'\n')
            with self.assertRaises(ValueError):bf.capture_file(raw,NOW.isoformat())
            (raw/bf.FILE).unlink();self.assertIsNone(bf.capture_file(raw,NOW.isoformat()))

    def test_readiness_is_sample_gated_and_not_automatic_approval(self):
        registry=bf.load_registry();rows=[]
        for i in range(300):
            week=i//50;kick=NOW+timedelta(days=1+7*week)
            rows.append({'fixture_key':str(i),'league':'Premier League','home_team':'A','away_team':'B',
                'kickoff_utc':kick.isoformat(),'status':'available','baseline':[.6,.2,.2],'candidate':[.74,.13,.13],
                'registry_sha256':bf.registry_hash(registry),'snapshot_commit':'a'*40,'secondary_status':'available',
                'baseline_goals':{'over_1_5':.6,'btts_yes':.6},'candidate_goals':{'over_1_5':.74,'btts_yes':.74}})
        rec={'home_goals':2,'away_goals':1,'match_id':1,'source_status':'FINISHED','source':'football-data.org/v4'}
        with patch.object(bf,'frozen',return_value=(rows,[])),patch('performance_tracking.fixture_match',return_value=(rec,'VERIFIED_FINISHED')):
            s,_,_=bf.evaluate(Path('.'),[],[rec],NOW+timedelta(days=60))
            self.assertEqual(s['status'],'READY_FOR_REVIEW');self.assertEqual(s['evidence'],'SUPPORTS_FORECASTING_REVIEW')
            self.assertFalse(s['automatic_production_change']);self.assertGreater(s['log_loss_gain_week_block95'][0],0)
            rec['home_goals']=0;rec['away_goals']=2
            s,_,_=bf.evaluate(Path('.'),[],[rec],NOW+timedelta(days=60))
            self.assertEqual(s['status'],'READY_FOR_REVIEW');self.assertEqual(s['evidence'],'NO_CLEAR_PROMOTION_EVIDENCE')
        with patch.object(bf,'frozen',return_value=(rows[:299],[])),patch('performance_tracking.fixture_match',return_value=(rec,'VERIFIED_FINISHED')):
            s,_,_=bf.evaluate(Path('.'),[],[rec],NOW+timedelta(days=60));self.assertEqual(s['status'],'COLLECT_MORE_DATA')
        with patch.object(bf,'frozen',return_value=(rows,['bad'])),patch('performance_tracking.fixture_match',return_value=(rec,'VERIFIED_FINISHED')):
            s,_,_=bf.evaluate(Path('.'),[],[rec],NOW+timedelta(days=60));self.assertEqual(s['status'],'DATA_QUALITY_BLOCKED')
        self.assertIsNone(bf.block_interval([],registry))
        self.assertIsNone(bf.block_interval([{'week':'same','log_loss_gain':1}]*3,registry))

    def test_matrix_capture_is_read_only_and_secondary_goals_are_bound(self):
        from football_value_pipeline_v2_standalone import DixonColesModel,FootballValuePipelineV2
        from performance_tracking import fixture_key
        model=DixonColesModel(max_goals=10);model.teams=['Manchester City FC','Everton FC'];model.team_to_idx={name:i for i,name in enumerate(model.teams)}
        model.attack=np.array([.15,-.15]);model.weakness=np.array([-.05,.05]);model.base=math.log(1.2);model.home_adv=math.log(1.18);model.rho=-.08
        pipe=object.__new__(FootballValuePipelineV2);pipe.market_weight=.5;pipe.devig_method='power'
        input_row=pd.Series({'HomeTeam':model.teams[0],'AwayTeam':model.teams[1],'kickoff_utc':(NOW+timedelta(days=1)).isoformat(),
            'live_ref_home_odds':1.47,'live_ref_draw_odds':4.3,'live_ref_away_odds':7.3,
            'live_best_home_odds':1.52,'live_best_draw_odds':4.3,'live_best_away_odds':7.4})
        plain=pipe._predict_row(model,input_row)
        pipe._benchmark_trial_enabled=True;pipe._benchmark_score_matrices={};pipe._totals_shadow_inputs={}
        shadow=pipe._predict_row(model,input_row);self.assertEqual(plain,shadow)
        matrix=pipe._benchmark_score_matrices[(model.teams[0],model.teams[1],input_row.kickoff_utc)];before=matrix.copy()
        row=frame().iloc[0].to_dict();row.update(shadow[0]);data=pd.DataFrame([row])
        with tempfile.TemporaryDirectory() as tmp:
            raw=Path(tmp);data.to_csv(raw/'all_leagues_predictions.csv',index=False)
            result=bf.write_experiment(data,raw,NOW.isoformat(),{fixture_key(row):matrix})
            self.assertEqual(result['rows'][0]['secondary_status'],'available');np.testing.assert_array_equal(matrix,before)
            bf.validate(result,NOW.isoformat(),data.to_dict('records'))
            altered=copy.deepcopy(result);altered['rows'][0]['candidate_goals']['over_1_5']+=.01
            with self.assertRaises(ValueError):bf.validate(altered,NOW.isoformat(),data.to_dict('records'))
            invalid=matrix.copy();invalid[0,0]=-1
            result=bf.write_experiment(data,raw,NOW.isoformat(),{fixture_key(row):invalid})
            self.assertEqual(result['rows'][0]['secondary_status'],'unavailable');self.assertEqual(result['rows'][0]['status'],'available')

    def test_queue_and_idempotent_notifications(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);setup(root)
            bf.review_experiment(root,[],[],NOW)
            q=eq.write_queue(root,NOW);self.assertEqual(len(q['experiments']),7)
            self.assertTrue(all(x['status']!='READY_FOR_REVIEW' for x in q['experiments']))
            q['experiments']=[{'name':'benchmark_forward_experiment','key':'trial-1','status':'READY_FOR_REVIEW','settled_evidence':300,'scope':'REVIEW_ONLY'}]
            payload=json.dumps({'content':base64.b64encode(json.dumps(q).encode()).decode()})
            def response(cmd,**kwargs):
                from subprocess import CompletedProcess
                if cmd[1]=='api':return CompletedProcess(cmd,0,payload,'')
                if cmd[2]=='list':return CompletedProcess(cmd,0,'[]','')
                if cmd[2]=='create':
                    body=Path(cmd[-1]).read_text();self.assertIn('does not approve',body)
                    return CompletedProcess(cmd,0,'https://github.com/owner/repo/issues/1\n','')
            self.assertEqual(eq.notify('owner/repo',NOW,runner=response),['https://github.com/owner/repo/issues/1'])
            def exists(cmd,**kwargs):
                from subprocess import CompletedProcess
                return CompletedProcess(cmd,0,payload if cmd[1]=='api' else '[{"number":1}]','')
            self.assertEqual(eq.notify('owner/repo',NOW,runner=exists),[])
            with self.assertRaises(ValueError):eq.notify('bad',NOW,runner=response)
            with self.assertRaises(ValueError):eq.notify('owner/repo',NOW+timedelta(days=3),runner=response)
