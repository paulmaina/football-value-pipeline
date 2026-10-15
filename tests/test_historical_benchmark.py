from offline_test_case import OfflineQuotePolicyTestCase
import copy
from datetime import datetime
import hashlib
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import numpy as np
import pandas as pd

import historical_benchmark as hb
from football_value_pipeline_v2_standalone import DixonColesModel,reweight_matrix_to_1x2


def config():
    c=json.loads(Path('historical_benchmark_config.json').read_text())
    c.update(leagues=['EPL'],seasons=['2324'],test_start='2025-08-01',audit_start='2025-08-15',test_end_exclusive='2025-09-01',
        min_train=30,min_development_matches=1,min_audit_matches=1)
    c.pop('input_manifest',None);c.pop('dataset_source_commit',None)
    return c


def history():
    d=pd.DataFrame({'Date':pd.date_range('2025-06-01',periods=90),'HomeTeam':['A']*90,'AwayTeam':['B']*90,
        'FTHG':[2]*90,'FTAG':[1]*90})
    for col,value in {'PSH':1.9,'PSD':3.6,'PSA':4.4,'PSCH':1.8,'PSCD':3.8,'PSCA':4.8,
        'P>2.5':1.9,'P<2.5':2.0,'PC>2.5':1.8,'PC<2.5':2.1}.items():d[col]=value
    return d


class ToyModel:
    fits=[];last_rho=[]
    def __init__(self,half_life_days,l2,max_goals):self.half=half_life_days;self.l2=l2;self.max_goals=max_goals;self.rho=-.06
    def fit(self,data,as_of=None):
        assert data.Date.max()<as_of
        self.teams=['A','B'];self.fits.append((data.Date.max(),as_of,self.half,self.l2));return self
    def score_matrix(self,h,a):
        lam=1.2+.01*self.l2;mu=.8
        return hb.adjusted_matrix(lam,mu,self.rho,self.max_goals),{'lambda_home':lam,'lambda_away':mu}


class HistoricalBenchmarkTests(OfflineQuotePolicyTestCase):
    def test_configuration_rejects_leaky_dates_and_invalid_grids(self):
        hb.validate_config(config())
        for key,value in [('audit_start','2025-07-01'),('test_end_exclusive','2025-08-02'),('min_train',10),
            ('max_goals',2),('market_weights',[1]),('baseline_l2',float('nan')),('l2_candidates',[3,3]),
            ('devig_method','invalid'),('leagues',['EPL','EPL']),('seasons',['../../']),('step_days',False),
            ('prospective_validation_start','2025-01-01')]:
            c=config();c[key]=value
            with self.assertRaises(ValueError):hb.validate_config(c)
        c=config();c['input_manifest']='../bad';c['dataset_source_commit']='a'*40
        with self.assertRaises(ValueError):hb.validate_config(c)

    def test_ingestion_pinned_hash_and_malformed_rows(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);path=root/'2324_E0.csv';d=history();d.to_csv(path,index=False)
            c=config();data,sources,excluded=hb.load_history(root,'EPL',c)
            self.assertEqual(len(data),90);self.assertEqual(sources[0]['sha256'],hb.digest(path))
            self.assertEqual(data.Date.min(),pd.Timestamp('2025-06-01'));self.assertEqual(data.Date.max(),pd.Timestamp('2025-08-29'))
            c['dataset_source_commit']='a'*40
            manifest={'dataset_source_commit':'a'*40,'sha256':{path.name:hb.digest(path)}}
            self.assertTrue(hb.verify_inputs(root,c,manifest))
            with patch('historical_benchmark.subprocess.run') as run:
                run.return_value.stdout=path.read_bytes()
                hb.materialize_inputs(root,root/'copy',c,manifest)
                self.assertEqual((root/'copy'/path.name).read_bytes(),path.read_bytes())
            path.write_bytes(path.read_bytes()+b'\n')
            with self.assertRaises(ValueError):hb.verify_inputs(root,c,manifest)
            bad=copy.deepcopy(manifest);bad['dataset_source_commit']='b'*40
            with self.assertRaises(ValueError):hb.verify_inputs(root,c,bad)
            for change in ('duplicate','score','date','team','same_team','missing_column'):
                bad=d.copy()
                if change=='duplicate':bad=pd.concat([bad,bad.iloc[:1]])
                if change=='score':bad.loc[0,'FTHG']=-1
                if change=='date':bad['Date']=bad.Date.astype(str);bad.loc[0,'Date']='invalid'
                if change=='team':bad.loc[0,'HomeTeam']=' '
                if change=='same_team':bad.loc[0,'AwayTeam']='A'
                if change=='missing_column':bad=bad.drop(columns='Date')
                bad.to_csv(path,index=False)
                with self.assertRaises(ValueError):hb.load_history(root,'EPL',config())
            bad=d.copy();bad.loc[0,['FTHG','FTAG']]=np.nan;bad.to_csv(path,index=False)
            _,_,excluded=hb.load_history(root,'EPL',config());self.assertEqual(excluded['unfinished_rows'],1)
            bad=d.copy();bad['HomeTeam']='Atlético';bad.to_csv(path,index=False,encoding='latin1')
            data,_,_=hb.load_history(root,'EPL',config());self.assertEqual(data.HomeTeam.iloc[0],'Atlético')
            path.unlink()
            with self.assertRaises(FileNotFoundError):hb.load_history(root,'EPL',config())

    def test_quote_checks_no_fallback_and_rps(self):
        self.assertIsNone(hb.market_probabilities({},('PSH','PSD','PSA'),'power'))
        for p in ([1,3,4],[float('inf'),3,4],[10,10,10]):
            self.assertIsNone(hb.market_probabilities(dict(zip(('a','b','c'),p)),('a','b','c'),'power'))
        p=hb.market_probabilities({'a':2,'b':3.5,'c':4},('a','b','c'),'power');self.assertAlmostEqual(sum(p),1)
        row={'p_home':.5,'p_draw':.3,'p_away':.2,'y':0,'over_1_5':.8,'home_goals':2,'away_goals':0}
        s=hb.score(row,'1x2');self.assertAlmostEqual(s['rps'],(.5**2+.2**2)/2)
        self.assertAlmostEqual(hb.score(row,'over_1_5')['brier'],.04)
        self.assertEqual(hb.metrics([], '1x2')['n'],0)

    def test_total_anchor_preserves_hda_and_fitted_rho(self):
        matrix=hb.adjusted_matrix(1.4,.8,-.06,10);p=DixonColesModel.one_x_two(matrix)
        target=[p[k] for k in ('home','draw','away')]
        anchor,scale=hb.anchor_totals(1.4,.8,-.06,target,.6,10)
        self.assertAlmostEqual(hb.goals(anchor)['over_2_5'],.6,places=7)
        np.testing.assert_allclose(list(DixonColesModel.one_x_two(anchor).values()),target,atol=1e-8)
        rebuilt=reweight_matrix_to_1x2(hb.adjusted_matrix(1.4*scale,.8*scale,-.06,10),target)
        np.testing.assert_allclose(anchor,rebuilt)
        for args in ((-1,.8,-.06), (1.4,.8,2)):
            with self.assertRaises(ValueError):hb.adjusted_matrix(*args,10)
        with self.assertRaises(ValueError):hb.anchor_totals(1.4,.8,-.06,target,1,10)
        with self.assertRaises(ValueError):hb.anchor_totals(.001,.001,0,target,.99999,10)

    def test_walkforward_independent_changes_unknown_teams_and_closing_are_labelled(self):
        ToyModel.fits=[];rows,folds,coverage,errors=hb.evaluate_league(history(),'EPL',config(),ToyModel)
        self.assertFalse(errors);self.assertTrue(all(end<origin for end,origin,_,_ in ToyModel.fits))
        hb.validate_records(rows,folds,config())
        self.assertTrue(any(r['variant']=='l2_3_raw' for r in rows))
        self.assertTrue(all(r['timing'].startswith('closing_') for r in rows if 'closing' in r['variant']))
        changed=history();changed.loc[changed.Date>='2025-08-01',['PSCH','PSCD','PSCA','PC>2.5','PC<2.5']]=[4,4,1.5,4,1.3]
        other,_,_,_=hb.evaluate_league(changed,'EPL',config(),ToyModel)
        original=[r for r in rows if 'closing' not in r['variant']]
        independent=[r for r in other if 'closing' not in r['variant']]
        self.assertEqual(original,independent)
        changed=history();changed.loc[changed.Date>='2025-08-01','HomeTeam']='Unknown'
        rows,_,counts,_=hb.evaluate_league(changed,'EPL',config(),ToyModel)
        self.assertEqual(rows,[]);self.assertGreater(counts['baseline_unknown_team_matches'],0)
        c=config();c['min_train']=1000
        rows,_,counts,_=hb.evaluate_league(history(),'EPL',c,ToyModel)
        self.assertEqual(rows,[]);self.assertGreater(counts['insufficient_training_matches'],0)
        with patch.object(ToyModel,'fit',side_effect=RuntimeError('fit failed')):
            rows,_,counts,errors=hb.evaluate_league(history(),'EPL',config(),ToyModel)
        self.assertEqual(rows,[]);self.assertTrue(errors)

    def test_audit_cannot_select_and_comparisons_use_paired_cohorts(self):
        rows,_,_,_=hb.evaluate_league(history(),'EPL',config(),ToyModel)
        first=hb.aggregate(rows,config())
        altered=copy.deepcopy(rows)
        for row in altered:
            if row['phase']=='audit':row.update(p_home=.01,p_draw=.01,p_away=.98,over_1_5=.01,under_3_5=.99,btts_yes=.01,over_2_5=.01)
        second=hb.aggregate(altered,config())
        self.assertEqual([r['selected_on_development'] for r in first['development_choices']],
            [r['selected_on_development'] for r in second['development_choices']])
        base=[r for r in rows if r['variant']==hb.BASE]
        selected=[r for r in rows if r['variant']=='l2_3'][:-2]
        paired=hb.paired(selected,base,'1x2')
        self.assertEqual(paired['n'],len(selected));self.assertEqual(paired['candidate']['n'],paired['baseline']['n'])
        altered=copy.deepcopy(rows);altered.append(rows[0])
        _,folds,_,_=hb.evaluate_league(history(),'EPL',config(),ToyModel)
        with self.assertRaises(ValueError):hb.validate_records(altered,folds,config())
        altered=copy.deepcopy(rows);altered[0]['training_end']=altered[0]['date']
        with self.assertRaises(ValueError):hb.validate_records(altered,folds,config())

    def test_full_report_reconciliation_tamper_and_cli_guards(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);cache=root/'cache';cache.mkdir();history().to_csv(cache/'2324_E0.csv',index=False)
            output=root/'output'
            before=(cache/'2324_E0.csv').read_bytes()
            with patch('requests.get',side_effect=AssertionError('No network allowed')):
                summary=hb.run(cache,output,config(),model_class=ToyModel)
            self.assertTrue(hb.validate_report(output));self.assertEqual(before,(cache/'2324_E0.csv').read_bytes())
            saved=(output/'manifest.json').read_text();hb.write_json(output/'manifest.json',{'version':hb.VERSION,'sha256':{}})
            with self.assertRaises(ValueError):hb.validate_report(output)
            (output/'manifest.json').write_text(saved)
            self.assertEqual(hb.main(['--out-dir',str(output),'--validate-only']),0)
            (output/'report.md').write_text('altered')
            with self.assertRaises(ValueError):hb.validate_report(output)
            hb.write_report(output,summary,pd.read_csv(output/'predictions.csv').replace({np.nan:None}).to_dict('records'),json.loads((output/'folds.json').read_text()))
            summary['comparisons'][0]['metrics']['n']=999
            hb.write_json(output/'summary.json',summary)
            manifest=json.loads((output/'manifest.json').read_text());manifest['sha256']['summary.json']=hb.digest(output/'summary.json');hb.write_json(output/'manifest.json',manifest)
            with self.assertRaises(ValueError):hb.validate_report(output)
            for args in (['--source-commit','bad'],['--out-dir',str(cache),'--cache-dir',str(cache)],['--out-dir',str(root/'raw')]):
                with self.assertRaises(SystemExit):hb.main(args)
            c=config();c['min_train']=9999
            with self.assertRaises(ValueError):hb.run(cache,output,c,model_class=ToyModel)
