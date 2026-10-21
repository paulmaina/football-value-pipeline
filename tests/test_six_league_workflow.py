"""One offline six-league run through both experiments, capture and verified review."""
from offline_test_case import OfflineQuotePolicyTestCase
import copy
from datetime import timedelta
from functools import partial
import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import pandas as pd
from football_value_pipeline_v2_standalone import LEAGUES,main
from conservative_bet_filter import build_conservative_shortlist
from format_football_output import main as format_main
from performance_tracking import capture,review,verified_record,write_json
from test_conservative_bet_filter import fixture,NOW
from test_graded_candidates import sample_report
from test_recency_experiment import history,tuning,ToyModel
from workflow_checks import raw_check,report_check


class SixLeagueWorkflowTests(OfflineQuotePolicyTestCase):
    def test_all_leagues_both_experiments_readable_outputs_and_forward_grading(self):
        keys=list(LEAGUES);frames={};records=[]
        for i,key in enumerate(keys):
            cfg=LEAGUES[key];row=fixture(i,kickoff=NOW+timedelta(days=1))
            row.update(p_under_3_5=.99, raw_p_under_3_5=.98, league=cfg.name,odds_event_id='event'+str(i),fixture_id='event'+str(i),
                       market_best_over_1_5_last_update_utc=NOW.isoformat())
            row.update(best_home_bookmaker='Pinnacle',best_away_bookmaker='Pinnacle',best_over_1_5_bookmaker='Pinnacle')
            frames[key]=pd.DataFrame([row])
            match={'id':i+1,'status':'FINISHED','utcDate':row['kickoff_utc'],
                'homeTeam':{'name':row['home_team']},'awayTeam':{'name':row['away_team']},
                'score':{'duration':'REGULAR','fullTime':{'home':2,'away':1}}}
            records.append(verified_record(cfg.football_data_org_code,match))
        def run_league(self,key,*args,**kwargs):
            self._recency_history=history()
            return frames[key],{'training_end':'2026-10-08','training_matches':1000},{}
        def payload(api,league,event_id):
            row=frames[league.key].iloc[0]
            return {'id':event_id,'home_team':row.home_team,'away_team':row.away_team,
                'commence_time':row.kickoff_utc,'bookmakers':[
                    {'key':'pinnacle','title':'Pinnacle','markets':[{'key':'h2h','last_update':NOW.isoformat(),
                        'outcomes':[{'name':row.home_team,'price':1.45},{'name':'Draw','price':5.0},{'name':row.away_team,'price':7.0}]}]},
                    *[{'key':'book_'+str(i),'title':'Book '+str(i),'markets':[{'key':'double_chance','last_update':NOW.isoformat(),
                        'outcomes':[{'name':'1X','price':1.25},{'name':'X2','price':2.6},{'name':'12','price':1.16}]}]} for i in (1,2)]]}
        reliability=sample_report()
        for market in reliability['markets'].values():
            for group in market['high_confidence'].values():group['status']='PASSED'
        def keys_from_test_file(*args,**kwargs):os.environ['THE_ODDS_API_KEY']='offline-fake-key'
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)/'football_output_v2';raw=root/'raw'
            with patch.dict(os.environ,{},clear=True),patch('requests.sessions.Session.request',side_effect=AssertionError('Live network disabled')),patch('api_key_config.load_api_keys',side_effect=keys_from_test_file),patch(
                'football_value_pipeline_v2_standalone.FootballValuePipelineV2.run_league',new=run_league),patch(
                'football_value_pipeline_v2_standalone.FootballValuePipelineV2.backtest_league',return_value=(pd.DataFrame(),pd.DataFrame(),{},pd.DataFrame())),patch(
                'goal_market_validation.evaluate_market_history',side_effect=lambda historical, league: {**copy.deepcopy(reliability), 'league': league}),patch(
                'conservative_bet_filter.build_conservative_shortlist',side_effect=partial(build_conservative_shortlist,as_of=NOW)),patch(
                'football_value_pipeline_v2_standalone.FootballValuePipelineV2._history_for_league',return_value=history()),patch(
                'dc_decay_validation.tune_half_life',side_effect=lambda *args,**kwargs:tuning()),patch(
                'football_value_pipeline_v2_standalone.DixonColesModel',ToyModel),patch(
                'market_led_experiment.fetch_event',side_effect=payload),patch('market_led_experiment.datetime') as dt:
                dt.now.return_value=NOW
                self.assertEqual(main(['--leagues',*keys,'--out-dir',str(raw),'--goal-blend-experiment','--market-led-experiment','--tune-half-life','--recency-experiment']),0)
                self.assertEqual(raw_check(root)['forecasts'],6)
                picks = pd.read_csv(raw/'conservative_bet_shortlist.csv')
                self.assertNotIn('Under 3.5', picks.market.tolist())
                self.assertNotIn('Both Teams to Score - Yes', picks.market.tolist())
                self.assertTrue(pd.read_csv(raw/'all_leagues_predictions.csv').p_under_3_5.eq(.99).all())
                summary = json.loads((raw/'conservative_bet_summary.json').read_text())
                self.assertEqual(summary['selection_policy_version'], '48h-risk-band-ev1-asian-handicap-1x2-over15-v20')
                self.assertTrue({'Home win','Draw','Away win','Over 1.5'}.issubset(summary['eligible_markets']))
                self.assertFalse(any('Double Chance' in m for m in summary['eligible_markets']))
                self.assertIn('Asian Handicap Home +0.00', summary['eligible_markets'])
                self.assertEqual(format_main(['--root-dir',str(root)]),0)
                readable = pd.read_csv(root/'readable/conservative_bet_shortlist_readable.csv')
                self.assertNotIn('Under 3.5', readable.to_string(index=False))
                self.assertTrue(capture('f'*40,root=root,captured_at=NOW+timedelta(minutes=1)))
                write_json(root/'performance/verified_results.json',{str(r['match_id']):r for r in records})
                with patch('performance_tracking.collect_results',return_value=(records,{})):
                    review(root=root,clock=NOW+timedelta(days=2))
                data=report_check(root)
            self.assertEqual(data['status'],'VERIFIED_WITH_WARNINGS')
            self.assertIn('UCL training/source health: DOWNLOAD_NOT_VERIFIED',data['warnings'])
            self.assertEqual(data['shortlist']['graded'],6)
            self.assertEqual(len(data['training_end_dates']),6)
            self.assertEqual(data['experiments']['goal_blend_experiment']['graded_fixture_markets'],18)
            self.assertEqual(data['experiments']['market_led_experiment']['graded_selections'],6)
            self.assertEqual(data['experiments']['recency_experiment']['graded_fixture_markets'],12)
            self.assertEqual(data['pipeline_health']['experiment_capture_counts']['recency_experiment:CAPTURED'],1)
            for name in ('filter_sensitivity_experiment','shortlist_weight_experiment','shortlist_policy_experiment'):
                self.assertEqual(data['experiments'][name]['total_fixtures'],0)
                self.assertEqual(data['pipeline_health']['experiment_capture_counts'][name+':NOT_GENERATED'],1)
            self.assertEqual(data['experiments']['benchmark_forward_experiment']['paired_fixtures'],0)
            self.assertEqual(len(data['pipeline_health']['review_queue']['experiments']),8)
            self.assertEqual(data['pipeline_health']['experiment_capture_counts']['benchmark_forward_experiment:CAPTURED'],1)
            self.assertTrue((root/'readable/football_performance_report.xlsx').exists())


