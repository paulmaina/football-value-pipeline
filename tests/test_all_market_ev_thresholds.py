import copy
import unittest
import pandas as pd
from conservative_bet_filter import _evaluate_market, MARKET_SPECS, build_conservative_shortlist
from test_conservative_bet_filter import fixture, NOW
from test_graded_candidates import sample_report
from test_double_chance import event
from double_chance import parse_quotes


class AllMarketEVTests(unittest.TestCase):
    def evaluate(self, spec, ev=.015, count=1, remove=None):
        label,key,min_p,min_raw=spec
        row=fixture();row.update(parse_quotes(event()))
        row['p_'+key]=.82
        row['raw_p_'+key]=.82
        row['market_'+key+'_odds']=(1+ev)/.82
        row['market_'+key+'_bookmakers']=count
        row['odds_bookmakers_1x2']=count
        if key in ('home','away'):
            for side in ('home','draw','away'):
                row['raw_p_'+side]=.82 if side==key else .09
        if remove: row.pop(remove,None)
        report=sample_report()
        report['markets'][key]=copy.deepcopy(report['markets']['over_1_5'])
        return _evaluate_market(pd.Series(row),spec,pd.Timestamp(NOW),report)

    def test_all_six_markets_pass_with_one_complete_book_at_one_point_five_percent(self):
        for spec in MARKET_SPECS:
            with self.subTest(market=spec[0]):
                row=self.evaluate(spec)
                self.assertNotEqual(row['decision'],'REJECTED',row['rejection_reasons'])
                self.assertAlmostEqual(row['conservative_estimated_ev'],.015)

    def test_all_six_reject_below_cutoff_or_zero_books(self):
        for spec in MARKET_SPECS:
            with self.subTest(market=spec[0]):
                row=self.evaluate(spec,ev=.0149)
                self.assertIn('reliability-adjusted EV below +1.5%',row['rejection_reasons'])
                row=self.evaluate(spec,count=0)
                self.assertIn('insufficient bookmaker coverage',row['rejection_reasons'])

    def test_one_book_still_requires_complete_reference_and_named_offer(self):
        for spec in MARKET_SPECS:
            key=spec[1]
            reference=('market_reference_dc_home_away_odds' if key in ('home_draw','draw_away')
                else 'market_reference_draw_odds' if key in ('home','away')
                else 'market_reference_'+key+'_opposite_odds')
            row=self.evaluate(spec,remove=reference)
            self.assertIn('incomplete same-book reference',row['rejection_reasons'])
            row=self.evaluate(spec,remove='best_'+key+'_bookmaker')
            self.assertIn('no validated bookmaker quote',row['rejection_reasons'])

    def test_summary_and_experiment_thresholds(self):
        _,_,summary=build_conservative_shortlist(pd.DataFrame([fixture()]),as_of=NOW)
        self.assertEqual(summary['min_estimated_ev'],.015)
        self.assertEqual(summary['min_bookmakers'],1)
        self.assertEqual(summary['selection_policy_version'],'72h-all-markets-ev15-one-book-v6')
        from market_led_experiment import settings
        self.assertEqual(settings()['min_ev'],.03)
        self.assertEqual(settings()['min_probability'],.8)
