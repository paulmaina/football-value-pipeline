from offline_test_case import OfflineQuotePolicyTestCase
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

from dc_decay_validation import tune_half_life
from recency_experiment import (VERSION,goal_probabilities,binary_metrics,historical_audit,
    generate_league,assemble,valid_extension,review_experiment,paired_comparison,validate_report)
from goal_blend_experiment import write_experiment,capture_file
from performance_tracking import capture,snapshots,verified_record,review,write_json
from test_goal_blend_experiment import frame
from test_performance_tracking import pick,final,T0,KICK,SHA


def history():
    return pd.DataFrame({'Date':pd.date_range('2023-01-01',periods=130,freq='7D'),
        'HomeTeam':['A']*130,'AwayTeam':['B']*130,'FTHG':[2]*130,'FTAG':[1]*130})


def predictions():
    data=frame()
    data['model_home_team']=data['home_team'];data['model_away_team']=data['away_team']
    data['home_name_match_score']=100;data['away_name_match_score']=100
    return data


class ToyModel:
    fits=[]; matrices=0
    def __init__(self,half_life_days,l2,max_goals):self.half=half_life_days
    def fit(self,data,as_of=None):
        if as_of is not None: assert data.Date.max()<as_of
        self.fits.append((self.half,len(data),as_of));return self
    def score_matrix(self,home,away):
        type(self).matrices+=1
        p=.4 if self.half==120 else .8
        matrix=np.zeros((3,3));matrix[0,0]=1-p;matrix[2,1]=p
        return matrix,{'home_name_match_score':100,'away_name_match_score':100}
    def one_x_two(self,matrix):
        return {'home':.8,'draw':.1,'away':.1} if self.half==120 else {'home':.4,'draw':.3,'away':.3}


def tuning():
    return tune_half_life(history(),ToyModel,candidates=[120,240],min_train=30,
        min_validation_matches=5,collect_recency_metrics=True)


def part(data=None):
    return generate_league(predictions() if data is None else data,history(),ToyModel,tuning(),
        league='Premier League',production_half_life=120,l2=.08,max_goals=10)


def setup(root,parts=None):
    raw=root/'raw';raw.mkdir(parents=True)
    data=predictions();data.to_csv(raw/'all_leagues_predictions.csv',index=False)
    pd.DataFrame([pick()]).to_csv(raw/'conservative_bet_shortlist.csv',index=False)
    write_json(raw/'conservative_bet_summary.json',{'generated_at_utc':T0.isoformat()})
    write_experiment(data,raw,T0.isoformat(),recency_parts=[part()] if parts is None else parts)
    return raw


class RecencyTests(OfflineQuotePolicyTestCase):
    def test_optional_diagnostics_reuse_fits_and_leave_production_selection_unchanged(self):
        ToyModel.fits=[];ToyModel.matrices=0
        plain=tune_half_life(history(),ToyModel,candidates=[120,240],min_train=30,min_validation_matches=5)
        fits=ToyModel.fits.copy();matrices=ToyModel.matrices
        ToyModel.fits=[];ToyModel.matrices=0
        research=tuning()
        self.assertEqual(ToyModel.fits,fits);self.assertEqual(ToyModel.matrices,matrices)
        stripped=copy.deepcopy(research)
        for candidate in stripped['candidates']:
            candidate.pop('recency_folds');candidate.pop('recency_diagnostics_error')
        self.assertEqual(plain,stripped)
        self.assertEqual(plain['selected_half_life_days'],120)
        audit=historical_audit(research)
        self.assertEqual(audit['markets']['over_1_5']['selected_half_life_days'],240)
        self.assertEqual(audit['markets']['btts_yes']['selected_half_life_days'],240)

    def test_goal_metrics_do_not_invalidate_baseline_tuning_on_bad_matrix(self):
        with patch.object(ToyModel,'score_matrix',return_value=(np.array([[float('nan')]]),{})):
            data=tuning()
        self.assertEqual(data['selected_half_life_days'],120)
        self.assertTrue(all(c['valid'] and c['recency_diagnostics_error']=='ValueError' for c in data['candidates']))
        self.assertEqual(historical_audit(data)['status'],'INSUFFICIENT_HISTORY')
        with patch('recency_experiment.fold_diagnostic',side_effect=ValueError('auxiliary diagnostic failure')):
            broken=tuning()
        self.assertEqual(broken['selected_half_life_days'],120)
        self.assertTrue(all(c['valid'] and c['recency_diagnostics_error']=='ValueError' for c in broken['candidates']))

    def test_audit_outcomes_cannot_choose_the_half_life(self):
        data=tuning();n=len(data['candidates'][0]['recency_folds']);split=2*n//3
        for c in data['candidates']:
            for i,f in enumerate(c['recency_folds']):
                f['one_x_two_log_loss']=.5 if c['half_life_days']==240 else 1
                p=(.9 if c['half_life_days']==120 else .2) if i<split else (.1 if c['half_life_days']==120 else .9)
                for key in f['markets']:
                    f['markets'][key]=binary_metrics([p]*f['n'],[1]*f['n'])
        audit=historical_audit(data)
        self.assertEqual(audit['development_1x2_half_life'],240)
        for market in audit['markets'].values():
            self.assertEqual(market['selected_half_life_days'],120)
            self.assertLess(market['audit_log_loss_gain'],0)
            self.assertEqual(sum(market['development_fold_winners'].values()),audit['development_folds'])

    def test_historical_audit_requires_common_temporal_folds_and_phase_samples(self):
        data=tuning()
        self.assertEqual(historical_audit({})['status'],'INSUFFICIENT_HISTORY')
        short=copy.deepcopy(data)
        for c in short['candidates']:c['recency_folds']=c['recency_folds'][:2]
        self.assertEqual(historical_audit(short)['status'],'INSUFFICIENT_HISTORY')
        mismatch=copy.deepcopy(data);mismatch['candidates'][0]['recency_folds'].pop()
        self.assertEqual(historical_audit(mismatch)['status'],'INSUFFICIENT_HISTORY')
        too_few=copy.deepcopy(data);too_few['min_validation_matches']=10000
        self.assertEqual(historical_audit(too_few)['status'],'INSUFFICIENT_HISTORY')
        self.assertIsNone(historical_audit(too_few)['markets']['btts_yes']['selected_half_life_days'])
        leaked=copy.deepcopy(data);leaked['candidates'][0]['recency_folds'][0]['training_end']=leaked['candidates'][0]['recency_folds'][0]['origin']
        with self.assertRaisesRegex(ValueError,'chronological'):historical_audit(leaked)
        tied=copy.deepcopy(data)
        for c in tied['candidates']:
            for f in c['recency_folds']:
                f['one_x_two_log_loss']=.5
                f['one_x_two_brier']=.4 if c['half_life_days']==120 else .1
        self.assertEqual(historical_audit(tied)['development_1x2_half_life'],240)

    def test_generation_is_read_only_raw_control_and_exact_history_with_no_odds_needed(self):
        data=predictions();before=data.copy(deep=True);hist=history();hbefore=hist.copy(deep=True)
        data['market_over_1_5_odds']=None;data['market_btts_yes_odds']=None
        p=generate_league(data,hist,ToyModel,tuning(),league='Premier League',production_half_life=120,l2=.08,max_goals=10)
        pd.testing.assert_frame_equal(hist,hbefore)
        pd.testing.assert_frame_equal(data,before.assign(market_over_1_5_odds=None,market_btts_yes_odds=None))
        for r in p['rows']:
            self.assertEqual(r['variants']['production_raw'],.9)
            self.assertEqual(r['variants']['half_life_120'],.9)
            self.assertEqual(r['variants']['half_life_240'],.8)
            self.assertEqual(r['variants']['goal_selected'],.8)
            self.assertEqual(r['half_lives']['goal_selected'],240)
        self.assertEqual(p['training_matches'],len(history()))
        self.assertEqual(len(p['training_sha256']),64)

    def test_candidate_fit_or_mapping_failures_preserve_control_and_record_coverage(self):
        class Broken(ToyModel):
            def fit(self,*args,**kwargs):raise RuntimeError('No fit')
        p=generate_league(predictions(),history(),Broken,tuning(),league='Premier League',production_half_life=120,l2=.08,max_goals=10)
        self.assertEqual(p['candidate_fit_errors'],{'half_life_240':'RuntimeError'})
        self.assertNotIn('half_life_240',p['rows'][0]['variants'])
        self.assertEqual(p['rows'][0]['variants']['production_raw'],.9)
        class Unknown(ToyModel):
            def score_matrix(self,*args):return np.ones((1,1)),{'home_name_match_score':0,'away_name_match_score':0}
        p=generate_league(predictions(),history(),Unknown,tuning(),league='Premier League',production_half_life=120,l2=.08,max_goals=10)
        self.assertEqual(p['rows'][0]['candidate_errors']['half_life_240'],'ValueError')
        data=predictions();data['model_home_team']='__LEAGUE_AVERAGE__'
        self.assertFalse(part(data)['rows'][0]['variants'])
        invalid=tuning();invalid['candidates'][0]['half_life_days']=0
        with self.assertRaises(ValueError):generate_league(predictions(),history(),ToyModel,invalid,league='Premier League',production_half_life=120,l2=.08,max_goals=10)

    def test_assemble_requires_past_history_and_sufficient_fixture_lead(self):
        p=part();p['rows'][0]['kickoff_utc']=(T0+timedelta(minutes=10)).isoformat()
        data=assemble([p],T0.isoformat())
        self.assertFalse(data['rows'][0]['variants'])
        self.assertIn('insufficient_lead_time',data['rows'][0]['reasons'])
        p['training_end']=(T0+timedelta(days=1)).isoformat()
        with self.assertRaisesRegex(ValueError,'future'):assemble([p],T0.isoformat())
        with self.assertRaises(ValueError):assemble([],None)

    def test_extension_schema_rejects_nonfinite_duplicate_and_unbound_data(self):
        data=assemble([part()],T0.isoformat());self.assertTrue(valid_extension(data,T0.isoformat()))
        for mutation in [lambda d:d.update(version='wrong'),lambda d:d.update(rows=None),
            lambda d:d.update(leagues=None),lambda d:d['rows'].append(copy.deepcopy(d['rows'][0])),
            lambda d:d['rows'][0].update(market='home'),lambda d:d['rows'][0].update(kickoff_utc=None),
            lambda d:d['rows'][0]['variants'].update(production_raw=float('nan')),
            lambda d:d['rows'][0]['variants'].pop('production_raw'),lambda d:d['rows'][0].update(half_lives={}),
            lambda d:d['rows'][0].update(status='unknown'),lambda d:d['rows'].__setitem__(0,'bad')]:
            bad=copy.deepcopy(data);mutation(bad)
            self.assertFalse(valid_extension(bad,T0.isoformat()))
        self.assertFalse(valid_extension(data,(T0+timedelta(seconds=1)).isoformat()))

    def test_recency_failure_retains_existing_goal_blend_sidecar(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);raw=setup(root)
            with patch('recency_experiment.assemble',side_effect=ValueError('future history')),self.assertWarnsRegex(UserWarning,'blend sidecar retained'):
                write_experiment(predictions(),raw,T0.isoformat(),recency_parts=[])
            parent=json.loads((raw/'goal_blend_experiment.json').read_text())
            self.assertEqual(len(parent['rows']),3)
            self.assertEqual(parent['recency_experiment']['generation_error'],'ValueError')
            self.assertTrue(capture_file(raw,T0.isoformat()))

    def test_immutable_nested_capture_verified_paired_grading_and_pending_exclusion(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);raw=setup(root);before={p.name:p.read_bytes() for p in raw.iterdir() if p.name!='goal_blend_experiment.json'}
            self.assertTrue(capture(SHA,root=root,captured_at=T0+timedelta(minutes=1)))
            self.assertTrue(all((raw/name).read_bytes()==b for name,b in before.items()))
            parent=root/'performance/snapshots'/SHA[:16]/'goal_blend_experiment.json';frozen=parent.read_bytes()
            archived=snapshots(root)
            report=review_experiment(root,archived,[],T0)
            self.assertEqual(report['graded_fixture_markets'],0)
            self.assertEqual(report['comparisons'],[])
            record=verified_record('PL',final())
            write_json(root/'performance/verified_results.json',{'PL:'+str(record['match_id']):record})
            with patch('performance_tracking.collect_results',return_value=([record],{})):
                review(root=root,clock=KICK+timedelta(days=1))
            report=json.loads((root/'performance/recency_experiment/summary.json').read_text())
            self.assertEqual(report['graded_fixture_markets'],2)
            comparison=next(r for r in report['comparisons'] if r['league']=='ALL' and r['market']=='over_1_5' and r['variant']=='half_life_240')
            self.assertAlmostEqual(comparison['brier'],.04)
            self.assertAlmostEqual(comparison['paired_brier_gain'],.01-.04)
            self.assertEqual(comparison['n'],1)
            self.assertIsNone(comparison['paired_brier_gain_approx95'])
            self.assertEqual(parent.read_bytes(),frozen)
            health=json.loads((root/'performance/pipeline_health.json').read_text())
            self.assertEqual(health['experiment_capture_counts']['recency_experiment:CAPTURED'],1)
            self.assertIn('recency_experiment',health['experimental_reports'])
            self.assertIn('Goal recency', (root/'performance/recency_experiment/report.md').read_text())
            parent.write_text('{}')
            (root/'performance/recency_experiment/summary.json').unlink()
            self.assertIsNone(review_experiment(root,snapshots(root),[record],KICK+timedelta(days=1)))

    def test_first_unavailable_variants_cannot_be_replaced_by_later_predictions(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);p=part()
            for row in p['rows']:row['variants'].pop('half_life_240');row['variants'].pop('goal_selected')
            raw=setup(root,[p]);capture(SHA,root=root,captured_at=T0)
            write_experiment(predictions(),raw,T0.isoformat(),recency_parts=[part()])
            capture('c'*40,root=root,captured_at=T0+timedelta(minutes=1))
            report=review_experiment(root,snapshots(root),[verified_record('PL',final())],KICK+timedelta(days=1))
            self.assertFalse(any(r['variant']=='half_life_240' for r in report['comparisons']))

    def test_report_validation_reconciles_frozen_probabilities_counts_and_verified_scores(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);setup(root);capture(SHA,root=root,captured_at=T0)
            record=verified_record('PL',final())
            write_json(root/'performance/verified_results.json',{'id':record})
            review_experiment(root,snapshots(root),[record],KICK+timedelta(days=1))
            self.assertEqual(validate_report(root)['fixture_markets'],2)
            dest=root/'performance/recency_experiment'
            original=json.loads((dest/'summary.json').read_text())
            for mutation in [lambda d:d.update(graded_fixture_markets=999),
                lambda d:d['comparisons'][0].update(brier=.5),
                lambda d:d['weekly_comparisons'][0].update(n=999),
                lambda d:d.update(historical_audits=[]),lambda d:d['comparisons'].append(d['comparisons'][0])]:
                changed=copy.deepcopy(original);mutation(changed);write_json(dest/'summary.json',changed)
                with self.assertRaises(ValueError):validate_report(root)
            write_json(dest/'summary.json',original)
            grade=pd.read_csv(dest/'graded.csv');original_bytes=(dest/'graded.csv').read_bytes()
            for field,value in [('probability',.1),('source_match_id',-1),('half_life_days',999),('baseline_brier',.9),('week','wrong')]:
                changed=grade.copy();changed.loc[0,field]=value;changed.to_csv(dest/'graded.csv',index=False)
                with self.assertRaises(ValueError):validate_report(root)
            (dest/'graded.csv').write_bytes(original_bytes)
            grade.iloc[1:].to_csv(dest/'graded.csv',index=False)
            with self.assertRaises(ValueError):validate_report(root)
            (dest/'graded.csv').write_bytes(original_bytes)
            coverage=pd.read_csv(dest/'coverage.csv');coverage.iloc[1:].to_csv(dest/'coverage.csv',index=False)
            with self.assertRaises(ValueError):validate_report(root)

    def test_unbound_control_and_bad_extension_are_visible_rejections_without_baseline_loss(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);raw=setup(root)
            parent=json.loads((raw/'goal_blend_experiment.json').read_text())
            parent['recency_experiment']['rows'][0]['variants']['production_raw']=.1
            (raw/'goal_blend_experiment.json').write_text(json.dumps(parent),encoding='utf-8')
            capture(SHA,root=root,captured_at=T0)
            report=review_experiment(root,snapshots(root),[verified_record('PL',final())],KICK+timedelta(days=1))
            self.assertEqual(report['rejected_snapshot_commits'],[SHA])
            self.assertEqual(report['graded_fixture_markets'],1)
            parent['recency_experiment']['version']='invalid'
            (raw/'goal_blend_experiment.json').write_text(json.dumps(parent),encoding='utf-8')
            capture('c'*40,root=root,captured_at=T0+timedelta(minutes=1))
            report=review_experiment(root,snapshots(root),[],T0+timedelta(minutes=1))
            self.assertIn('c'*40,report['rejected_snapshot_commits'])
            self.assertEqual(len(snapshots(root)),2)

    def test_paired_gain_intervals_and_calibration_are_reported_on_matching_rows(self):
        rows=[{'probability':.8,'outcome':1,'brier':.04,'log_loss':-np.log(.8),
            'baseline_brier':.09,'baseline_log_loss':-np.log(.7)}]*35
        r=paired_comparison(rows)
        self.assertAlmostEqual(r['paired_brier_gain'],.05)
        self.assertEqual(r['assessment'],'REVIEW_ON_LATER_HOLDOUT')
        self.assertEqual(len(r['paired_log_loss_gain_approx95']),2)
        self.assertAlmostEqual(r['overconfidence'],-.2)
        self.assertIsNone(binary_metrics([],[])['brier'])
        for matrix in (np.array([1]),np.array([[.5]]),np.array([[float('nan')]]),np.array([[-1,2]])):
            with self.assertRaises(ValueError):goal_probabilities(matrix)

    def test_cli_requires_tuning_and_preserves_prediction_and_shortlist_bytes(self):
        from football_value_pipeline_v2_standalone import main
        from conservative_bet_filter import build_conservative_shortlist
        from functools import partial
        with self.assertRaises(SystemExit):main(['--recency-experiment'])
        def run(self,key,*args,**kwargs):
            self._recency_history=history()
            return predictions(),{'training_end':'2025-06-22','training_matches':130},{}
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            with patch('conservative_bet_filter.build_conservative_shortlist',side_effect=partial(build_conservative_shortlist,as_of=T0)),patch(
                'football_value_pipeline_v2_standalone.FootballValuePipelineV2.run_league',new=run),patch(
                'football_value_pipeline_v2_standalone.FootballValuePipelineV2._history_for_league',return_value=history()),patch(
                'football_value_pipeline_v2_standalone.FootballValuePipelineV2.backtest_league',return_value=(pd.DataFrame(),pd.DataFrame(),{},pd.DataFrame())),patch(
                'dc_decay_validation.tune_half_life',side_effect=lambda *args,**kwargs:tuning()),patch(
                'football_value_pipeline_v2_standalone.DixonColesModel',ToyModel):
                for enabled in (False,True):
                    args=['--leagues','EPL','--tune-half-life','--goal-blend-experiment','--out-dir',str(root/str(enabled))]
                    if enabled:args.append('--recency-experiment')
                    self.assertEqual(main(args),0)
            for name in ('all_leagues_predictions.csv','EPL_predictions.csv','conservative_bet_shortlist.csv','conservative_bet_rejections.csv'):
                self.assertEqual((root/'False'/name).read_bytes(),(root/'True'/name).read_bytes())
            old=json.loads((root/'False/goal_blend_experiment.json').read_text());new=json.loads((root/'True/goal_blend_experiment.json').read_text())
            self.assertEqual(old['rows'],new['rows'])
            self.assertNotIn('recency_experiment',old)
            self.assertEqual(new['recency_experiment']['version'],VERSION)
            self.assertTrue(new['recency_experiment']['rows'][0]['variants'])


if __name__=='__main__':unittest.main()
