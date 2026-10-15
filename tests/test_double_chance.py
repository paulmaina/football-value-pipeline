from offline_test_case import OfflineQuotePolicyTestCase
import copy
import unittest
from unittest.mock import patch
import pandas as pd

from double_chance import probabilities,parse_quotes
from conservative_bet_filter import build_conservative_shortlist
from goal_market_validation import enrich_historical_goal_markets, evaluate_market_history, prioritized_additional_events
from performance_tracking import result_for_market
from test_conservative_bet_filter import fixture,NOW
from test_graded_candidates import sample_report


def event():
    return {'home_team':'Chelsea','away_team':'Fulham','bookmakers':[
        {'title':name,'markets':[{'key':'double_chance','last_update':NOW.isoformat(),
         'outcomes':[{'name':'Chelsea or Draw','price':1.35},
                     {'name':'Fulham or Draw','price':2.4},
                     {'name':'Chelsea or Fulham','price':1.12}]}]}
         for name in ('Book A','Book B')]}


class DoubleChanceTests(OfflineQuotePolicyTestCase):
    def test_probability_sum_not_synthetic_odds(self):
        r=probabilities({'p_home':.6,'p_draw':.25,'p_away':.15,
                         'raw_p_home':.5,'raw_p_draw':.3,'raw_p_away':.2})
        self.assertAlmostEqual(r['p_home_draw'],.85)
        self.assertAlmostEqual(r['raw_p_draw_away'],.5)
        self.assertAlmostEqual(r['p_home_away'],.75)
        self.assertAlmostEqual(r['raw_p_home_away'],.70)
        self.assertFalse(any('odds' in key for key in r))
        self.assertEqual(probabilities({'p_home':.8,'p_draw':.3,'p_away':.2}),{})

    def test_current_forecast_and_readable_output_include_12(self):
        from football_value_pipeline_v2_standalone import FootballValuePipelineV2, DixonColesModel
        from format_football_output import readable_predictions_frame, build_match_summary
        from test_recency_experiment import history
        model = DixonColesModel().fit(history())
        pipeline = FootballValuePipelineV2.__new__(FootballValuePipelineV2)
        pipeline.market_weight = 0.0; pipeline.devig_method = 'power'
        row = pd.Series({'HomeTeam': str(history().iloc[0]['HomeTeam']),
                         'AwayTeam': str(history().iloc[0]['AwayTeam'])})
        pred, _ = pipeline._predict_row(model, row)
        self.assertAlmostEqual(pred['p_home_away'], 1-pred['p_draw'])
        self.assertAlmostEqual(pred['raw_p_home_away'], 1-pred['raw_p_draw'])
        frame = readable_predictions_frame(pd.DataFrame([{**fixture(), **pred}]), {})
        self.assertNotEqual(frame.iloc[0]['Double Chance 12'], '—')
        self.assertIn('Double Chance 12 (either team wins)', build_match_summary(pred, []))

    def test_documented_labels_complete_books_and_overlap_reference(self):
        r=parse_quotes(event())
        self.assertEqual(r['market_home_draw_odds'],1.35)
        self.assertEqual(r['market_draw_away_bookmakers'],2)
        self.assertEqual(r['market_home_away_odds'],1.12)
        self.assertAlmostEqual(sum(r['market_p_'+k] for k in ('home_draw','draw_away','home_away')),2)
        self.assertGreater(r['market_p_home_draw'],.7)
        self.assertAlmostEqual(r['market_p_home_draw'],2*(1/1.35)/(1/1.35+1/2.4+1/1.12))
        broken=event()
        for book in broken['bookmakers']:book['markets'][0]['outcomes'].pop()
        self.assertEqual(parse_quotes(broken),{})
        duplicate=event()
        for book in duplicate['bookmakers']:book['markets'][0]['outcomes'].append({'name':'1X','price':1.3})
        self.assertEqual(parse_quotes(duplicate),{})

    def test_new_policy_removes_under_and_requires_validated_real_dc_quotes(self):
        r=fixture();r.update(probabilities({'p_home':.65,'p_draw':.25,'p_away':.1,
                            'raw_p_home':.6,'raw_p_draw':.25,'raw_p_away':.15}))
        r.update(parse_quotes(event()))
        report=sample_report()
        # Same predeclared gates, with a valid high-confidence report.
        report['markets']['home_draw']=copy.deepcopy(report['markets']['over_1_5'])
        report['markets']['draw_away']=copy.deepcopy(report['markets']['over_1_5'])
        report['markets']['home_draw']['high_confidence']['85plus']['status']='PASSED'
        picks,decisions,summary=build_conservative_shortlist(pd.DataFrame([r]),as_of=NOW,
            market_reliability={'Premier League':report})
        self.assertNotIn('Under 3.5',decisions.market.tolist())
        self.assertEqual(summary['selection_policy_version'],'72h-six-markets-dc12-probability-odds-net-ev15-v9')
        dc=decisions.loc[decisions.market.eq('Double Chance 1X')].iloc[0]
        self.assertNotEqual(dc.decision,'REJECTED',dc.rejection_reasons)
        r.pop('market_home_draw_odds')
        _,decisions,_=build_conservative_shortlist(pd.DataFrame([r]),as_of=NOW,
            market_reliability={'Premier League':report})
        self.assertEqual(decisions.loc[decisions.market.eq('Double Chance 1X'),'decision'].iloc[0],'REJECTED')
        r.update(parse_quotes(event()))
        _,decisions,_=build_conservative_shortlist(pd.DataFrame([r]),as_of=NOW)
        self.assertEqual(decisions.loc[decisions.market.eq('Double Chance 1X'),'decision'].iloc[0],'REJECTED')

    def test_historical_outcomes_and_no_fabricated_historical_prices(self):
        p=fixture();p.update(p_home=.6,p_draw=.25,p_away=.15,raw_p_home=.6,raw_p_draw=.2,raw_p_away=.2)
        r=enrich_historical_goal_markets({'FTHG':1,'FTAG':1},p)
        self.assertEqual(r['actual_home_draw'],1)
        self.assertEqual(r['actual_draw_away'],1)
        self.assertEqual(r['actual_home_away'],0)
        self.assertEqual(enrich_historical_goal_markets({'FTHG':2,'FTAG':1},p)['actual_home_away'],1)
        self.assertIsNone(r['historical_open_home_away_odds'])
        self.assertIsNone(r['historical_open_home_draw_odds'])
        self.assertAlmostEqual(r['p_home_draw'],.85)
        rows=[dict(r,date=f'2026-{1+i//28:02d}-{1+i%28:02d}') for i in range(112)]
        report=evaluate_market_history(pd.DataFrame(rows),'Premier League')
        self.assertGreater(report['markets']['home_draw']['audit']['n'],0)

    def test_grading_draw_home_away_and_legacy_under(self):
        for h,a,one_x,x_two in [(1,1,True,True),(2,0,True,False),(0,2,False,True)]:
            self.assertEqual(result_for_market('Double Chance 1X',h,a),one_x)
            self.assertEqual(result_for_market('Double Chance X2',h,a),x_two)
            self.assertEqual(result_for_market('Double Chance 12',h,a),h != a)
        self.assertFalse(result_for_market('Under 3.5',4,1))

    def test_event_request_includes_double_chance_and_uses_new_cache(self):
        from football_value_pipeline_v2_standalone import TheOddsAPI,LEAGUES
        payload=event();payload['id']='example'
        import tempfile
        with tempfile.TemporaryDirectory() as cache:
            api=TheOddsAPI('test-key',cache_dir=cache)
            with patch.object(api,'_get_json',return_value=payload) as fetch:
                r=api.extra_markets_for_event(LEAGUES['EPL'],'example')
                self.assertIn('double_chance',fetch.call_args.kwargs['params']['markets'])
                self.assertIn('dc_v1',fetch.call_args.args[1])
                self.assertEqual(r['market_home_draw_odds'],1.35)


class DoubleChanceAdjustedThresholdTests(OfflineQuotePolicyTestCase):
    def candidate(self, key, adjusted=.75, ev=.015):
        row=fixture()
        row.update(parse_quotes(event()))
        row['p_'+key]=.82
        row['raw_p_'+key]=.80
        row['market_'+key+'_odds']=(1+ev)/adjusted
        report=sample_report()
        report['markets'][key]=copy.deepcopy(report['markets']['over_1_5'])
        report['markets'][key]['confidence_penalty']=.82-adjusted
        return row,report

    def decision(self, key, **kwargs):
        row,report=self.candidate(key,**kwargs)
        _,decisions,summary=build_conservative_shortlist(pd.DataFrame([row]),as_of=NOW,
            market_reliability={'Premier League':report})
        label={'home_draw':'Double Chance 1X','draw_away':'Double Chance X2','home_away':'Double Chance 12'}[key]
        return decisions.loc[decisions.market.eq(label)].iloc[0],summary

    def test_both_double_chances_pass_at_new_thresholds(self):
        for key in ('home_draw','draw_away','home_away'):
            row,summary=self.decision(key,ev=.015)
            self.assertNotEqual(row.decision,'REJECTED',row.rejection_reasons)
            self.assertAlmostEqual(row.rank_probability,.75)
            self.assertEqual(summary['double_chance_min_adjusted_ev'],.015)
            self.assertEqual(summary['double_chance_min_adjusted_probability'],.75)

    def test_below_each_threshold_is_rejected_without_provisional_relaxation(self):
        row,_=self.decision('home_draw',ev=.0149)
        self.assertEqual(row.decision,'REJECTED')
        self.assertIn('below +1.5%',row.rejection_reasons)
        row,_=self.decision('draw_away',adjusted=.7499,ev=.02)
        self.assertEqual(row.decision,'REJECTED')
        self.assertIn('reliability-adjusted probability below minimum',row.rejection_reasons)

    def test_unadjusted_and_raw_gates_still_apply(self):
        for field,value in [('p_home_draw',.79),('raw_p_home_draw',.749)]:
            row,report=self.candidate('home_draw',adjusted=.78,ev=.025)
            row[field]=value
            _,decisions,_=build_conservative_shortlist(pd.DataFrame([row]),as_of=NOW,
                market_reliability={'Premier League':report})
            dc=decisions.loc[decisions.market.eq('Double Chance 1X')].iloc[0]
            self.assertEqual(dc.decision,'REJECTED')

    def test_12_can_win_ranking_and_requires_real_quote_and_history(self):
        row, report = self.candidate('home_away', adjusted=.81, ev=.04)
        picks, decisions, _ = build_conservative_shortlist(pd.DataFrame([row]), as_of=NOW,
            market_reliability={'Premier League':report})
        self.assertEqual(picks.iloc[0]['market'], 'Double Chance 12')
        for missing in ('market_home_away_odds', 'market_reference_dc_home_away_odds'):
            broken = dict(row); broken.pop(missing)
            _, audit, _ = build_conservative_shortlist(pd.DataFrame([broken]), as_of=NOW,
                market_reliability={'Premier League':report})
            self.assertEqual(audit.loc[audit.market.eq('Double Chance 12'), 'decision'].iloc[0], 'REJECTED')
        _, audit, _ = build_conservative_shortlist(pd.DataFrame([row]), as_of=NOW)
        self.assertEqual(audit.loc[audit.market.eq('Double Chance 12'), 'decision'].iloc[0], 'REJECTED')

    def test_market_led_experiment_remains_at_three_percent(self):
        from market_led_experiment import settings
        self.assertEqual(settings()['min_ev'],.03)
        self.assertEqual(settings()['min_probability'],.80)



