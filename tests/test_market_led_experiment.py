import copy
from datetime import timedelta
from functools import partial
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import Mock, patch

import pandas as pd
from market_led_experiment import evaluate, settings, write_experiment, capture_file, review_experiment, FILE
from performance_tracking import capture, snapshots, frozen_rows, verified_record
from test_performance_tracking import fixture, pick, final, T0, KICK, SHA


def source():
    return {**fixture(), 'odds_source':'The Odds API', 'odds_event_id':'event1',
            'p_home_draw':.60,'raw_p_home_draw':.55,'p_draw_away':.4,'raw_p_draw_away':.45}


def payload():
    row=source()
    ref={'key':'pinnacle','title':'Pinnacle','markets':[{'key':'h2h','last_update':T0.isoformat(),
        'outcomes':[{'name':row['home_team'],'price':1.45}, {'name':'Draw','price':5.0},
                    {'name':row['away_team'],'price':7.0}]}]}
    target={'key':'book_a','title':'Book A','markets':[{'key':'double_chance','last_update':T0.isoformat(),
        'outcomes':[{'name':'1X','price':1.25},{'name':'X2','price':2.6},{'name':'12','price':1.16}]}]}
    second=copy.deepcopy(target);second.update(key='book_b',title='Book B')
    return {'id':'event1','home_team':row['home_team'],'away_team':row['away_team'],
            'commence_time':KICK.isoformat(),'bookmakers':[ref,target,second]}


class MarketLedTests(unittest.TestCase):
    def test_reference_and_target_are_independent_and_model_does_not_veto(self):
        from football_value_pipeline_v2_standalone import devig
        s,p=source(),payload(); original=copy.deepcopy((s,p))
        rows=evaluate(s,p,T0,settings())
        q=devig([1.45,5.,7.],method='power')
        self.assertAlmostEqual(rows[0]['reference_probability'],q[0]+q[1])
        self.assertTrue(rows[0]['qualifies'])
        self.assertEqual(rows[0]['decimal_odds'],1.25)
        self.assertLess(rows[0]['model_minus_reference'],0)
        self.assertEqual((s,p),original)
        self.assertEqual(rows[0]['independent_bookmaker_count'],2)

    def test_same_book_cannot_supply_reference_and_target(self):
        p=payload(); p['bookmakers'][0]['markets'].append(copy.deepcopy(p['bookmakers'][1]['markets'][0]))
        p['bookmakers']=p['bookmakers'][:1]
        rows=evaluate(source(),p,T0,settings())
        self.assertIsNone(rows[0]['decimal_odds'])
        self.assertFalse(rows[0]['qualifies'])

    def test_missing_reference_is_not_replaced_with_model_or_other_book(self):
        p=payload();p['bookmakers'][0]['key']='ordinary_book'
        r=evaluate(source(),p,T0,settings())[0]
        self.assertIsNone(r['reference_probability'])
        self.assertIn('missing_invalid_or_stale_pinnacle_1x2',r['reasons'])

    def test_stale_future_skew_and_mismatched_identity_fail_closed(self):
        for mutate in (
            lambda p:p['bookmakers'][0]['markets'][0].update(last_update=(T0-timedelta(minutes=11)).isoformat()),
            lambda p:p['bookmakers'][0]['markets'][0].update(last_update=(T0+timedelta(seconds=1)).isoformat()),
            lambda p:p['bookmakers'][0]['markets'][0].update(last_update=(T0-timedelta(minutes=8)).isoformat()),
            lambda p:p.update(id='wrong'),lambda p:p.update(home_team='Wrong team'),
            lambda p:p.update(commence_time=(KICK+timedelta(hours=1)).isoformat()),
        ):
            p=payload();mutate(p)
            self.assertFalse(evaluate(source(),p,T0,settings())[0]['qualifies'])

    def test_incomplete_dc_and_insufficient_book_count_are_rejected(self):
        p=payload();p['bookmakers'][1]['markets'][0]['outcomes'].pop()
        r=evaluate(source(),p,T0,settings())[0]
        self.assertEqual(r['independent_bookmaker_count'],1)
        self.assertIn('insufficient_independent_bookmaker_coverage',r['selection_reasons'])

    def test_exchange_offers_not_used_without_liquidity_and_commission_support(self):
        p=payload();p['bookmakers'][1]['key']='betfair_ex_eu';p['bookmakers'][2]['key']='matchbook'
        self.assertFalse(evaluate(source(),p,T0,settings())[0]['qualifies'])

    def test_costs_reduce_ev_and_are_validated(self):
        a=evaluate(source(),payload(),T0,settings())[0]
        b=evaluate(source(),payload(),T0,settings(cost_bps=100))[0]
        self.assertAlmostEqual(a['estimated_ev_after_cost']-b['estimated_ev_after_cost'],.01)
        for args in ({'max_age_minutes':0},{'cost_bps':float('nan')},{'max_skew_minutes':11}):
            with self.assertRaises(ValueError): settings(**args)

    def setup(self, root):
        raw=root/'raw';raw.mkdir()
        frame=pd.DataFrame([source()]);frame.to_csv(raw/'all_leagues_predictions.csv',index=False)
        pd.DataFrame([pick()]).to_csv(raw/'conservative_bet_shortlist.csv',index=False)
        (raw/'conservative_bet_summary.json').write_text(json.dumps({'generated_at_utc':T0.isoformat()}))
        return raw,frame

    def write(self,raw,frame,response=None):
        api=Mock()
        with patch('market_led_experiment.fetch_event',return_value=response or payload()), patch('market_led_experiment.datetime') as dt:
            dt.now.return_value=T0
            return write_experiment(frame,raw,T0.isoformat(),api,settings())

    def test_write_capture_grading_and_tamper_do_not_modify_baseline(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);raw,frame=self.setup(root)
            before={p.name:p.read_bytes() for p in raw.iterdir()}; original=frame.copy(deep=True)
            data=self.write(raw,frame)
            self.assertEqual(sum(r['selected'] for r in data['rows']),1)
            for name,content in before.items():self.assertEqual((raw/name).read_bytes(),content)
            pd.testing.assert_frame_equal(frame,original)
            self.assertTrue(capture_file(raw,T0.isoformat()))
            self.assertIsNone(capture_file(raw,(T0+timedelta(seconds=1)).isoformat()))
            capture(SHA,root=root,captured_at=T0+timedelta(minutes=1))
            archive=snapshots(root)
            self.assertEqual(len(frozen_rows(archive,'predictions')),1)
            review_experiment(root,archive,[verified_record('PL',final())],KICK+timedelta(days=1))
            summary=json.loads((root/'performance/market_led_experiment/summary.json').read_text())
            self.assertEqual(summary['paired_graded_fixture_markets'],2)
            self.assertEqual(len(summary['comparisons']),6)
            self.assertEqual(summary['graded_selections'],1)
            self.assertAlmostEqual(summary['flat_unit_roi_after_configured_cost'],.25)
            self.assertEqual(summary['late_reference_proxy_count'],0)
            (root/'performance/snapshots'/SHA[:16]/FILE).write_text('{}')
            self.assertEqual(len(frozen_rows(snapshots(root),'predictions')),1)
            (raw/'all_leagues_predictions.csv').write_text('changed')
            self.assertIsNone(capture_file(raw,T0.isoformat()))

    def test_no_api_and_failures_are_reported_without_exposing_credentials(self):
        with tempfile.TemporaryDirectory() as tmp:
            raw,frame=self.setup(Path(tmp))
            with patch('market_led_experiment.datetime') as dt:
                dt.now.return_value=T0
                data=write_experiment(frame,raw,T0.isoformat(),None,settings())
            self.assertIn('api_unavailable',data['rows'][0]['reasons'])
            with patch('market_led_experiment.datetime') as dt, patch('market_led_experiment.fetch_event',side_effect=RuntimeError('apiKey=SECRET')):
                dt.now.return_value=T0
                data=write_experiment(frame,raw,T0.isoformat(),Mock(),settings())
            self.assertIn('request_failed_RuntimeError',data['rows'][0]['reasons'])
            self.assertNotIn('SECRET',(raw/FILE).read_text())

    def test_cli_opt_in_preserves_baseline_files_and_failure_is_isolated(self):
        from football_value_pipeline_v2_standalone import main
        from conservative_bet_filter import build_conservative_shortlist
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);frame=pd.DataFrame([source()])
            for mode in ('off','on','failure'):
                with patch('conservative_bet_filter.build_conservative_shortlist',side_effect=partial(build_conservative_shortlist,as_of=T0)), patch(
                    'football_value_pipeline_v2_standalone.FootballValuePipelineV2.run_league',return_value=(frame,{'training_end':'2026-09-20','training_matches':1000},{})), patch(
                    'football_value_pipeline_v2_standalone.FootballValuePipelineV2.backtest_league',return_value=(pd.DataFrame(),pd.DataFrame(),{},pd.DataFrame())), patch(
                    'market_led_experiment.datetime') as dt, patch('market_led_experiment.fetch_event',return_value=payload()), patch(
                    'market_led_experiment.write_experiment',wraps=write_experiment) as write:
                    dt.now.return_value=T0
                    if mode=='failure':write.side_effect=RuntimeError('research unavailable')
                    args=['--leagues','EPL','--out-dir',str(root/mode)]
                    if mode!='off':args+=['--market-led-experiment']
                    if mode=='failure':
                        with self.assertWarns(UserWarning):self.assertEqual(main(args),0)
                    else:self.assertEqual(main(args),0)
                    self.assertEqual(write.call_count,0 if mode=='off' else 1)
            for name in ('all_leagues_predictions.csv','EPL_predictions.csv','conservative_bet_shortlist.csv',
                         'conservative_strict_qualifiers.csv','conservative_bet_rejections.csv'):
                self.assertEqual((root/'off'/name).read_bytes(),(root/'on'/name).read_bytes())
                self.assertEqual((root/'off'/name).read_bytes(),(root/'failure'/name).read_bytes())
            self.assertFalse((root/'off'/FILE).exists())
            self.assertTrue((root/'on'/FILE).exists())

    def test_cli_rejects_leaking_historical_mode_before_requests(self):
        from football_value_pipeline_v2_standalone import main
        with self.assertRaises(SystemExit): main(['--market-led-experiment','--backtest'])

    def test_later_quotes_evaluate_value_without_replacing_first_selection(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);raw,frame=self.setup(root)
            first=self.write(raw,frame)
            capture(SHA,root=root,captured_at=T0+timedelta(minutes=1))
            late=KICK-timedelta(minutes=45)
            p=payload()
            for book in p['bookmakers']:
                for market in book['markets']: market['last_update']=late.isoformat()
            with patch('market_led_experiment.datetime') as dt, patch('market_led_experiment.fetch_event',return_value=p):
                dt.now.return_value=late
                write_experiment(frame,raw,T0.isoformat(),Mock(),settings())
            capture('c'*40,root=root,captured_at=late+timedelta(minutes=1))
            review_experiment(root,list(reversed(snapshots(root))),[verified_record('PL',final())],KICK+timedelta(days=1))
            summary=json.loads((root/'performance/market_led_experiment/summary.json').read_text())
            self.assertEqual(summary['selected'],1)
            self.assertEqual(summary['late_reference_proxy_count'],1)
            self.assertAlmostEqual(summary['flat_unit_roi_after_configured_cost'],.25)

    def test_late_or_tampered_sidecar_is_not_graded_and_baseline_survives(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);raw,frame=self.setup(root)
            self.write(raw,frame)
            data=json.loads((raw/FILE).read_text())
            for row in data['rows']: row['generated_at_utc']=KICK.isoformat()
            (raw/FILE).write_text(json.dumps(data))
            capture(SHA,root=root,captured_at=T0+timedelta(minutes=1))
            archive=snapshots(root)
            self.assertEqual(len(frozen_rows(archive,'predictions')),1)
            review_experiment(root,archive,[verified_record('PL',final())],KICK+timedelta(days=1))
            self.assertFalse((root/'performance/market_led_experiment/summary.json').exists())

    def test_no_flag_no_sidecar_preserves_capture(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);self.setup(root)
            capture(SHA,root=root,captured_at=T0)
            self.assertNotIn(FILE,snapshots(root)[0][0]['sha256'])
