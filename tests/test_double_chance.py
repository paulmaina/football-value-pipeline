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


class DoubleChanceTests(unittest.TestCase):
    def test_probability_sum_not_synthetic_odds(self):
        r=probabilities({'p_home':.6,'p_draw':.25,'p_away':.15,
                         'raw_p_home':.5,'raw_p_draw':.3,'raw_p_away':.2})
        self.assertAlmostEqual(r['p_home_draw'],.85)
        self.assertAlmostEqual(r['raw_p_draw_away'],.5)
        self.assertFalse(any('odds' in key for key in r))
        self.assertEqual(probabilities({'p_home':.8,'p_draw':.3,'p_away':.2}),{})

    def test_documented_labels_complete_books_and_overlap_reference(self):
        r=parse_quotes(event())
        self.assertEqual(r['market_home_draw_odds'],1.35)
        self.assertEqual(r['market_draw_away_bookmakers'],2)
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
        self.assertEqual(summary['selection_policy_version'],'72h-double-chance-v4')
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
        self.assertIsNone(r['historical_open_home_draw_odds'])
        self.assertAlmostEqual(r['p_home_draw'],.85)
        rows=[dict(r,date=f'2026-{1+i//28:02d}-{1+i%28:02d}') for i in range(112)]
        report=evaluate_market_history(pd.DataFrame(rows),'Premier League')
        self.assertGreater(report['markets']['home_draw']['audit']['n'],0)

    def test_grading_draw_home_away_and_legacy_under(self):
        for h,a,one_x,x_two in [(1,1,True,True),(2,0,True,False),(0,2,False,True)]:
            self.assertEqual(result_for_market('Double Chance 1X',h,a),one_x)
            self.assertEqual(result_for_market('Double Chance X2',h,a),x_two)
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
