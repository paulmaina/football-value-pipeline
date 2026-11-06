"""Totals source consistency and independent Pinnacle binary price checks."""
import copy
import json
import tempfile
from pathlib import Path
from unittest.mock import patch
import numpy as np
import pandas as pd
from offline_test_case import OfflineQuotePolicyTestCase
from test_cagey_no_loss_v4 import ctx, sample, NOW, POLICY, item, V4
from test_cagey_tier_v3 import FRESH
import cagey_tier_v3 as tier
import cagey_market_basis as basis
import price_edge_cagey_shortlist as v28

V5=dict(V4,cagey_tier_rule=tier.RULE_MARKET_BASIS)


def pin():
    return {'h2h':(1/(.4*1.03),1/(.3*1.03),1/(.3*1.03),FRESH),
            'ou15':(1/(.72*1.03),1/(.28*1.03),FRESH)}


def context():
    data=ctx();data['uncorrected_matrix']=np.array([[.1,.1,.05],[.1,.25,.1],[.05,.1,.15]])
    return data


def annotate(candidate, data=None, prices=None):
    data=context() if data is None else data
    tier.annotate(candidate,data,sample(),NOW,POLICY,0.,rule=tier.RULE_MARKET_BASIS,pin=pin() if prices is None else prices)
    return candidate


class MarketBasisTests(OfflineQuotePolicyTestCase):
    def test_totals_selection_ev_flag_schema_and_stakes_share_uncorrected_source(self):
        from shortlist_schema import harmonize
        from staking import conservative_settlement,stake_recommendations
        candidate=annotate(item('Over 1.5',None,None,1.5))
        self.assertEqual(candidate['cagey_tier_decision'],'ELIGIBLE')
        self.assertEqual(candidate['cagey_probability_basis'],basis.UNCORRECTED)
        self.assertEqual(v28.settlement_basis(candidate,'cagey'),'uncorrected_matrix')
        self.assertAlmostEqual(candidate['cagey_p_win'],.7)
        self.assertAlmostEqual(candidate['corrected_p_win'],.49)
        self.assertAlmostEqual(candidate['cagey_no_loss_probability'],.7)
        self.assertAlmostEqual(candidate['cagey_expected_return'],.05)
        self.assertEqual(candidate['price_flag'],'value')
        self.assertLess(candidate['corrected_expected_profit'],0)
        candidate.update(selection_policy_version=v28.POLICY,cagey_tier_decision='SHORTLISTED',per_stake_cost=0.,kickoff_utc=sample()['kickoff_utc'])
        out=harmonize(pd.DataFrame([candidate]),'cagey')
        self.assertAlmostEqual(out.chance_of_no_loss.iloc[0],.7)
        self.assertEqual(out.source_probability_basis.iloc[0],basis.UNCORRECTED)
        self.assertAlmostEqual(conservative_settlement(candidate,tier='cagey')['full_win'],.7)
        sized=stake_recommendations(pd.DataFrame([candidate]),tier='cagey')
        self.assertAlmostEqual(sized.conservative_ev.iloc[0],.05)
        self.assertEqual(sized.probability_basis.iloc[0],basis.UNCORRECTED)
        from staking import UnavailableDistribution
        with self.assertRaises(UnavailableDistribution):
            conservative_settlement({**candidate,'cagey_probability_basis':tier.BASIS},tier='cagey')
        self.assertAlmostEqual(candidate['totals_correction_delta'],-.21)

    def test_totals_missing_uncorrected_grid_never_falls_back(self):
        from staking import conservative_settlement,UnavailableDistribution
        data=context();data.pop('uncorrected_matrix')
        candidate=annotate(item('Over 1.5',None,None,1.5),data)
        self.assertEqual(candidate['cagey_tier_decision'],'REJECTED')
        self.assertIsNone(candidate['cagey_p_win'])
        with self.assertRaises(UnavailableDistribution): conservative_settlement(candidate,tier='cagey')

    def test_binary_guard_is_independent_of_wrong_corrected_fair(self):
        data=context();grid=np.array([[.05,.02,.01],[.60,.05,.01],[.20,.03,.03]])
        delta=np.subtract.outer(np.arange(3),np.arange(3));data['matrix']=grid
        data['probs']=np.array([grid[delta==m].sum() for m in data['margins']]);data['score']=float(grid[abs(delta)>=2].sum())
        for market,side,line,price in [('Home win','home',-.5,1.8),('Double Chance 1X','home',.5,1.6),('Double Chance 12',None,None,1.6),('Asian Handicap Home -0.50','home',-.5,1.8),
                ('Asian Handicap Home +0.50','home',.5,1.6)]:
            with self.subTest(market=market):
                candidate=annotate(item(market,side,line,price),data)
                self.assertGreater(price,1.15*candidate['corrected_fair_odds'])
                self.assertEqual(candidate['cagey_tier_decision'],'ELIGIBLE')
                self.assertEqual(candidate['price_guard_status'],'PASSED')
                self.assertEqual(candidate['price_guard_basis'],'pinnacle_1x2_proportional')

    def test_direct_dc_complements_and_totals_price_guard(self):
        for market,expected in [('Home win',.4),('Away win',.3),('Double Chance 1X',.7),('Double Chance X2',.6),('Double Chance 12',.7),('Over 1.5',.72)]:
            fair,warning=basis.reference(item(market),pin(),NOW)
            self.assertAlmostEqual(1/fair,expected)
            self.assertIsNone(warning)
        candidate=annotate(item('Over 1.5',None,None,1.8))
        self.assertEqual(candidate['price_guard_status'],'SUSPECTED_PRICE_ERROR')
        self.assertIn('independent Pinnacle',candidate['cagey_tier_reasons'])

    def test_unavailable_stale_future_and_bad_reference_are_visible_not_model_fallbacks(self):
        for kind in ('missing','stale','future','skew','overround'):
            prices=pin()
            if kind=='missing':prices['ou15']=None
            elif kind=='overround':prices['ou15']=(1.1,1.1,FRESH)
            else:
                stamp=NOW+pd.Timedelta(seconds=1) if kind=='future' else NOW-pd.Timedelta(hours=30) if kind=='stale' else NOW-pd.Timedelta(minutes=12)
                prices['ou15']=(*prices['ou15'][:2],stamp.isoformat())
            candidate=annotate(item('Over 1.5',None,None,1.5),prices=prices)
            self.assertEqual(candidate['cagey_tier_decision'],'ELIGIBLE')
            self.assertEqual(candidate['price_guard_status'],'UNAVAILABLE')
            self.assertIsNone(candidate['price_guard_fair_odds'])
            self.assertTrue(candidate['price_guard_warning'])
        self.assertIsNone(basis.over_probability(np.array([[float('nan')]])))

    def test_v4_remains_corrected_and_v5_uses_market_basis(self):
        old=item('Over 1.5',None,None,1.5)
        tier.annotate(old,context(),sample(),NOW,POLICY,0.,rule=tier.RULE_NO_GATE)
        new=annotate(item('Over 1.5',None,None,1.5))
        self.assertEqual(old['price_flag'],'below fair')
        self.assertEqual(new['price_flag'],'value')
        self.assertNotIn('cagey_p_win',old)
        self.assertAlmostEqual(old['corrected_p_win'],new['corrected_p_win'])

    def test_full_pipeline_ranks_generic_basis_and_keeps_value_picks(self):
        data=sample()
        old,_,_=v28.build_shortlist(pd.DataFrame([data]),NOW,execution_policy=POLICY,settings=V4)
        selected,decisions,summary=v28.build_shortlist(pd.DataFrame([data]),NOW,execution_policy=POLICY,settings=V5)
        picks=v28.cagey_tier_list(decisions)
        self.assertEqual(selected.market.tolist(),old.market.tolist())
        np.testing.assert_allclose(selected.profit_probability,old.profit_probability)
        self.assertTrue(picks.chance_of_no_loss.is_monotonic_decreasing)
        over=picks[picks.market.eq('Over 1.5')].iloc[0]
        self.assertEqual(over.source_probability_basis,basis.UNCORRECTED)
        self.assertAlmostEqual(over.chance_of_no_loss,over.uncorrected_over_1_5_probability)
        self.assertEqual(summary['cagey_tier']['rule_version'],tier.RULE_MARKET_BASIS)

    def test_v5_raw_replay_and_readable_price_check_labels(self):
        from workflow_checks import raw_check
        from pipeline_health import write_generation_metadata
        from format_football_output import process_conservative_shortlist
        import master_shortlist as master
        data=sample();monitor=[]
        selected,decisions,summary=v28.build_shortlist(pd.DataFrame([data]),NOW,execution_policy=POLICY,settings=V5,monitor=monitor)
        picks=v28.cagey_tier_list(decisions)
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);raw=root/'raw';raw.mkdir();out=root/'readable';out.mkdir()
            pd.DataFrame([data]).to_csv(raw/'all_leagues_predictions.csv',index=False)
            selected.to_csv(raw/'conservative_bet_shortlist.csv',index=False)
            selected.to_csv(raw/'conservative_strict_qualifiers.csv',index=False)
            decisions.to_csv(raw/'conservative_bet_rejections.csv',index=False)
            picks.to_csv(raw/v28.TIER_FILE,index=False)
            master.refresh(decisions,raw,summary,pd.DataFrame([data]));v28.record_monitoring(summary,monitor,raw)
            (raw/'conservative_bet_summary.json').write_text(json.dumps(summary),encoding='utf-8');write_generation_metadata(raw,summary)
            with patch('requests.sessions.Session.request',side_effect=AssertionError('offline replay')):raw_check(root)
            process_conservative_shortlist(raw,out)
            frame=pd.read_csv(out/'cagey_tier_shortlist_readable.csv')
            self.assertIn('Price check basis',frame)
            self.assertIn('Draw correction delta vs Pinnacle',frame)
            self.assertEqual(frame.loc[frame['Market to bet'].eq('Over 1.5'),'Probability basis'].iloc[0],basis.UNCORRECTED)
