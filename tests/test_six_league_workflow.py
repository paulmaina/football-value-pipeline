"""One offline six-league run through the live trials, capture and verified review."""
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
        import team_research
        fixed = partial(team_research.enrich, clock=lambda: NOW)
        self.addCleanup(patch.stopall)
        patch('team_research.enrich', side_effect=fixed).start()
        keys=list(LEAGUES);frames={};records=[]
        for i,key in enumerate(keys):
            cfg=LEAGUES[key];row=fixture(i,kickoff=NOW+timedelta(days=1))
            row.update(lambda_home=1.8, lambda_away=.5, p_under_3_5=.99, raw_p_under_3_5=.98, league=cfg.name,odds_event_id='event'+str(i),fixture_id='event'+str(i),
                       home_training_matches=12, away_training_matches=12, market_best_over_1_5_last_update_utc=NOW.isoformat())
            row.update(best_home_bookmaker='Pinnacle',best_away_bookmaker='Pinnacle',best_over_1_5_bookmaker='Pinnacle')
            # Current researched shortlist allows below-fair prices; actual offers stay within the new upper bound.
            stamp=(NOW-timedelta(minutes=1)).isoformat()
            row['price_edge_quotes']=json.dumps([
                {'bookmaker':'Pinnacle','market':'h2h','market_key':'h2h','point':None,'last_update_utc':stamp,
                 'prices':{'home':1.9,'draw':3.5,'away':4.4}},
                {'bookmaker':'1xBet','market':'h2h','market_key':'h2h','point':None,'last_update_utc':stamp,
                 'prices':{'home':1.95,'draw':3.4,'away':3.9}}])
            frames[key]=pd.DataFrame([row])
            match={'id':i+1,'status':'FINISHED','utcDate':row['kickoff_utc'],
                'homeTeam':{'name':row['home_team']},'awayTeam':{'name':row['away_team']},
                'score':{'duration':'REGULAR','fullTime':{'home':2,'away':1}}}
            record = verified_record(cfg.football_data_org_code,match)
            if key == 'UEL':
                # Europa's collector emits corroborated feed results and opaque
                # hashed IDs, rather than football-data.org integer IDs.
                record.update(source='Cornerflick + Fixture Download', match_id='e'+str(i).zfill(19))
            records.append(record)
        def run_league(self,key,*args,**kwargs):
            return frames[key],{'training_end':'2026-10-08','training_matches':1000},{}
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
                'europa_training.load',return_value=history(),
                side_effect=ValueError('coverage incomplete') if getattr(self, '_uel_unavailable', False) else None):
                requested_keys = list(keys)
                if getattr(self, '_uel_unavailable', False):
                    keys.remove('UEL')
                self.assertEqual(main(['--no-research-free-sources', '--leagues',*requested_keys,'--out-dir',str(raw),'--tune-half-life']),0)
                self.assertEqual(raw_check(root)['forecasts'],len(keys))
                picks = pd.read_csv(raw/'conservative_bet_shortlist.csv')
                self.assertNotIn('Under 3.5', picks.market.tolist())
                self.assertNotIn('Both Teams to Score - Yes', picks.market.tolist())
                self.assertTrue(pd.read_csv(raw/'all_leagues_predictions.csv').p_under_3_5.eq(.99).all())
                summary = json.loads((raw/'conservative_bet_summary.json').read_text())
                self.assertEqual(summary['selection_policy_version'], '48h-ah-price-edge-cagey-v28')
                self.assertTrue(summary['cagey_correction_enabled'] and summary['cagey_tier_enabled'])
                self.assertTrue({'Home win','Away win','Double Chance 1X','Double Chance X2'}.issubset(summary['eligible_markets']))
                # Draw remains excluded; the researched v2 rule includes all three double chances.
                self.assertIn('Double Chance 12', summary['eligible_markets'])
                for excluded in ('Draw',):
                    self.assertNotIn(excluded,summary['eligible_markets'])
                self.assertEqual(summary.get('value_rule'), 'local-research-profit-115-200-dc12-v2')
                # The pipeline writes the master shortlist beside the other lists and records it in the summary.
                master = pd.read_csv(raw/'master_shortlist.csv')
                self.assertEqual(summary['master_shortlist']['n_bets'], len(master))
                # A negative edge and missing optional research do not block nominations.
                self.assertEqual(len(master), min(10, len(keys)))
                self.assertEqual(summary['master_shortlist']['version'], 'master-profit-no-dc-v6')
                self.assertEqual(summary['master_shortlist']['shortfall'], max(0, 10-len(keys)))
                self.assertTrue(master.master_suggested_stake.eq(0).all())
                self.assertEqual(len(master[['league','home_team','away_team','kickoff_utc']].drop_duplicates()),len(master))
                audit = pd.read_csv(raw/'master_shortlist_audit.csv')
                self.assertEqual(set(audit.master_decision), {'ELIGIBLE'})
                self.assertTrue(audit.master_coverage_warning.str.contains('research').all())
                self.assertIn('Over 1.5', summary['eligible_markets'])
                self.assertEqual(set(picks.market),{'Home win'})
                self.assertEqual(set(picks.bookmaker),{'1xBet'})
                self.assertIn('Asian Handicap Home +0.00', summary['eligible_markets'])
                self.assertEqual(format_main(['--root-dir',str(root)]),0)
                readable = pd.read_csv(root/'readable/conservative_bet_shortlist_readable.csv')
                self.assertNotIn('Under 3.5', readable.to_string(index=False))
                self.assertTrue(capture('f'*40,root=root,captured_at=NOW+timedelta(minutes=1)))
                write_json(root/'performance/verified_results.json',{str(r['match_id']):r for r in records})
                with patch('performance_tracking.collect_results',return_value=(records,{})):
                    review(root=root,clock=NOW+timedelta(days=2))
                data=report_check(root)
                # v27 tracking: tagged candidates captured; picks graded (no closing quotes offline).
                tracking=json.loads((root/'performance/price_edge_v27/summary.json').read_text())
                snapshot=next((root/'performance/snapshots').glob('*/price_edge_tagged_candidates.csv'))
                tagged_rows=pd.read_csv(snapshot)
            self.assertEqual(data['status'],'VERIFIED_WITH_WARNINGS')
            self.assertIn('UCL training/source health: DOWNLOAD_NOT_VERIFIED',data['warnings'])
            # v27 has no cap: every toy fixture with a qualifying price gets one pick.
            self.assertEqual(len(picks),len(keys))
            self.assertEqual(picks.selection_tier.unique().tolist(),['STRICT'])
            self.assertEqual(tracking['frozen_picks'],len(keys))
            self.assertFalse(tracking['stop_review'])
            self.assertTrue(tagged_rows.high_draw.all())  # Pinnacle draw 27.6%
            self.assertGreater(tracking['tagged_candidates']['frozen'],0)
            # Leagues without a verified-results source (Super Lig) stay ungraded.
            settled = [k for k in keys if LEAGUES[k].football_data_org_code]
            self.assertEqual(data['shortlist']['graded'],len(settled))
            self.assertEqual(len(data['training_end_dates']),len(keys))
            # Retired experiments (archive/) are no longer generated, captured or reviewed.
            # The benchmark-forward and totals-anchor trials joined them in PR E.
            for name in ('goal_blend_experiment','market_led_experiment','recency_experiment','filter_sensitivity_experiment',
                         'shortlist_weight_experiment','shortlist_policy_experiment','model_reliability_experiment',
                         'benchmark_forward_experiment','totals_anchor_experiment'):
                self.assertNotIn(name,data['experiments'])
                self.assertEqual([p for p in root.rglob(name+'.json')],[])
                self.assertFalse((root/'performance'/name).exists())
            self.assertEqual(data['pipeline_health']['review_queue']['experiments'],[])
            self.assertEqual(data['pipeline_health']['experiment_capture_counts'],{})
            self.assertTrue((root/'readable/football_performance_report.xlsx').exists())




    def test_unverified_europa_does_not_block_other_leagues_or_experiments(self):
        self._uel_unavailable = True
        self.test_all_leagues_both_experiments_readable_outputs_and_forward_grading()
