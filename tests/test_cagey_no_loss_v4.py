"""No universal narrow gate, market-specific support, no double counting, old replay."""
import json
from pathlib import Path
import tempfile
from unittest.mock import patch

import numpy as np
import pandas as pd
from offline_test_case import OfflineQuotePolicyTestCase
from test_cagey_tier_v3 import context as base_context, item, sample, SETTINGS, NOW, POLICY
from test_price_edge_cagey_shortlist import cagey_row
from test_value_per_market import over_1xbet
import cagey_tier_v3 as tier
import price_edge_cagey_shortlist as v28
import narrow_support as support

V4 = dict(SETTINGS, cagey_tier_rule=tier.RULE_NO_GATE)


def ctx(open_game=False):
    data = base_context()
    if open_game:
        data['matrix'] = np.array([[.05,.05,.35],[.05,.05,.05],[.30,.05,.05]])
    matrix = data['matrix']; delta=np.subtract.outer(np.arange(3),np.arange(3))
    data['probs'] = np.array([matrix[delta == m].sum() for m in data['margins']])
    data['score'] = float(matrix[abs(delta) >= 2].sum())
    return data


def annotate(candidate, context, rule=tier.RULE_NO_GATE, cost=0.):
    tier.annotate(candidate,context,sample(),NOW,POLICY,cost,rule=rule)
    return candidate


def run(data=None, settings=V4):
    return v28.build_shortlist(pd.DataFrame([data or sample()]),NOW,execution_policy=POLICY,settings=settings)


class NoLossV4Tests(OfflineQuotePolicyTestCase):
    def test_open_matches_eligible_for_all_markets_without_67_gate(self):
        context=ctx(True)
        self.assertLess(1-context['score'],.67)
        for market,side,line in [('Home win','home',-.5),('Away win','away',-.5),
            ('Double Chance 1X','home',.5),('Double Chance X2','away',.5),
            ('Double Chance 12',None,None),('Over 1.5',None,None),
            ('Asian Handicap Home +1.00','home',1.),('Asian Handicap Away -1.50','away',-1.5)]:
            with self.subTest(market=market):
                current=annotate(item(market,side,line),context)
                self.assertEqual(current['cagey_tier_decision'],'ELIGIBLE')
                self.assertFalse(current['narrow_high_67'])
                old=annotate(item(market,side,line),context,rule=tier.RULE)
                self.assertEqual(old['cagey_tier_decision'],'REJECTED')
                self.assertIn('P(narrow) below 67%',old['cagey_tier_reasons'])
                self.assertNotIn('narrow_support_version',old)

    def test_plus_handicap_bounds_include_pushes_and_half_wins(self):
        for side in ('home','away'):
            for line in (1.,1.25,1.5,2.):
                with self.subTest(side=side,line=line):
                    result=annotate(item(f'Asian Handicap {side.title()} {line:+.2f}',side,line,1.16),ctx())
                    self.assertTrue(result['narrow_high_67'])
                    self.assertEqual(result['narrow_support_role'],'plus_handicap_protection')
                    self.assertAlmostEqual(result['corrected_narrow_no_loss_lower_bound'],.96)
                    self.assertGreaterEqual(result['corrected_no_loss_probability']+1e-12,.96)
                    if line==1.:
                        self.assertIsNone(result['corrected_narrow_profit_lower_bound'])
                    else:
                        self.assertAlmostEqual(result['corrected_narrow_profit_lower_bound'],.96)

    def test_minus_handicap_upper_bounds_and_cost_qualified_plus_support(self):
        for side in ('home','away'):
            result=annotate(item(f'Asian Handicap {side.title()} -1.50',side,-1.5),ctx())
            self.assertEqual(result['narrow_support_role'],'minus_handicap_caution')
            self.assertAlmostEqual(result['corrected_narrow_no_loss_upper_bound'],.04)
            self.assertAlmostEqual(result['corrected_narrow_profit_upper_bound'],.04)
            self.assertLessEqual(result['corrected_p_profit'],.04+1e-12)
        costed=annotate(item('Asian Handicap Home +1.00','home',1.,1.16),ctx(),cost=.01)
        self.assertIsNone(costed['corrected_narrow_no_loss_lower_bound'])
        self.assertIn('execution cost',costed['narrow_support_note'])
        expensive=annotate(item('Asian Handicap Home +1.25','home',1.25,1.16),ctx(),cost=.09)
        self.assertIsNone(expensive['corrected_narrow_no_loss_lower_bound'])
        self.assertIsNone(expensive['corrected_narrow_profit_lower_bound'])

    def test_draw_one_goal_and_joint_contributions_are_parts_not_boosts(self):
        for market in ('Over 1.5','Double Chance 12'):
            result=annotate(item(market,None,None),ctx())
            self.assertEqual(result['narrow_support_role'],'context_only')
            self.assertAlmostEqual(result['corrected_p_draw'],.47)
            self.assertAlmostEqual(result['corrected_p_home_by_one'],.22)
            self.assertAlmostEqual(result['corrected_p_away_by_one'],.27)
            self.assertAlmostEqual(sum(result[k] for k in ('corrected_p_draw','corrected_p_home_by_one','corrected_p_away_by_one')),.96)
            self.assertIsNone(result['corrected_narrow_no_loss_lower_bound'])
            expected=.45 if market=='Over 1.5' else .49
            self.assertAlmostEqual(result['corrected_narrow_profit_contribution'],expected)
            self.assertAlmostEqual(result['corrected_p_profit'],expected+.04)

    def test_support_is_not_a_probability_adjustment_or_ranking_bonus(self):
        for line in (1.,-1.5):
            candidate=item(f'Asian Handicap Home {line:+.2f}','home',line,1.16)
            old=annotate(dict(candidate),ctx(),rule=tier.RULE)
            new=annotate(dict(candidate),ctx())
            for key in ('corrected_no_loss_probability','corrected_p_profit','corrected_expected_profit',
                        'corrected_fair_odds',*v28.SETTLEMENT_COLUMNS[:5]):
                self.assertEqual(old[key],new[key])
        primary={'corrected_no_loss_probability','corrected_p_profit','corrected_expected_profit','corrected_fair_odds'}
        self.assertTrue(primary.isdisjoint(support.COLUMNS))
        first,decisions,_=run()
        with patch.object(support,'THRESHOLD',.99):
            second,changed,_=run()
        p1,p2=v28.cagey_tier_list(decisions),v28.cagey_tier_list(changed)
        self.assertEqual(p1.market.tolist(),p2.market.tolist())
        np.testing.assert_allclose(p1.corrected_no_loss_probability,p2.corrected_no_loss_probability)
        np.testing.assert_allclose(first.profit_probability,second.profit_probability)

    def test_missing_distribution_is_unavailable_not_low_narrow(self):
        result=annotate(item(),None)
        self.assertEqual(result['cagey_tier_decision'],'REJECTED')
        self.assertIsNone(result['narrow_high_67'])
        self.assertEqual(result['narrow_support_role'],'unavailable')
        no_price=support.supplement(item(price=None),ctx(),0.)
        self.assertTrue(no_price['narrow_high_67'])
        self.assertIsNone(no_price['corrected_narrow_no_loss_contribution'])
        unsupported=support.supplement(item('unsupported',None,None),ctx(),0.)
        self.assertIsNone(unsupported['corrected_narrow_profit_contribution'])

    def test_real_open_fixture_over15_qualifies_and_old_v3_replays(self):
        data=cagey_row(home='Open FC',lambdas=(2.8,1.5,-.02))
        data['price_edge_quotes']=json.dumps(json.loads(data['price_edge_quotes'])+[over_1xbet(1.2)])
        data.update(lambda_home=2.8,lambda_away=1.5,p_home=.6,p_draw=.2,p_away=.2,p_over_1_5=.9)
        selected,decisions,summary=run(data)
        picks=v28.cagey_tier_list(decisions)
        self.assertIn('Over 1.5',picks.market.tolist())
        self.assertTrue(picks.p_narrow.lt(.67).all())
        self.assertFalse(summary['cagey_tier']['narrow_general_gate'])
        self.assertIsNone(summary['cagey_tier']['min_p_narrow'])
        self.assertEqual(summary['cagey_tier']['narrow_supplement_threshold'],.67)
        old,old_decisions,old_summary=run(data,SETTINGS)
        self.assertTrue(v28.cagey_tier_list(old_decisions).empty)
        self.assertEqual(old_summary['cagey_tier']['min_p_narrow'],.67)
        self.assertEqual(old.market.tolist(),selected.market.tolist())
        np.testing.assert_allclose(old.profit_probability,selected.profit_probability)

    def test_v4_tracking_preserves_rule_and_all_groups(self):
        import price_edge_tracking as tracking
        _,decisions,_=run();picks=v28.cagey_tier_list(decisions)
        rows=picks.assign(snapshot_generated_utc=NOW.isoformat()).to_dict('records')
        with patch.object(tracking,'archived_tier_rows',return_value=rows):
            frozen=tracking.frozen_tier_picks(Path('.'),[])
        self.assertEqual(len(frozen),4)
        frame=tracking.tier_frame(pd.DataFrame(),pd.DataFrame(frozen))
        self.assertTrue(frame.cagey_tier_rule.eq(tier.RULE_NO_GATE).all())

    def test_v4_readable_support_and_offline_replay_in_both_lists(self):
        from workflow_checks import raw_check
        from pipeline_health import write_generation_metadata
        from format_football_output import process_conservative_shortlist
        import master_shortlist as master
        data=sample();monitor=[]
        selected,decisions,summary=v28.build_shortlist(pd.DataFrame([data]),NOW,execution_policy=POLICY,settings=V4,monitor=monitor)
        picks=v28.cagey_tier_list(decisions)
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);raw=root/'raw';raw.mkdir();out=root/'readable';out.mkdir()
            pd.DataFrame([data]).to_csv(raw/'all_leagues_predictions.csv',index=False)
            selected.to_csv(raw/'conservative_bet_shortlist.csv',index=False)
            selected.to_csv(raw/'conservative_strict_qualifiers.csv',index=False)
            decisions.to_csv(raw/'conservative_bet_rejections.csv',index=False)
            picks.to_csv(raw/v28.TIER_FILE,index=False)
            master.refresh(decisions,raw,summary,pd.DataFrame([data]))
            v28.record_monitoring(summary,monitor,raw)
            (raw/'conservative_bet_summary.json').write_text(json.dumps(summary),encoding='utf-8')
            write_generation_metadata(raw,summary)
            with patch('requests.sessions.Session.request',side_effect=AssertionError('offline replay')):
                raw_check(root)
            process_conservative_shortlist(raw,out)
            for name in ('conservative_bet_shortlist_readable.csv','cagey_tier_shortlist_readable.csv'):
                report=pd.read_csv(out/name)
                self.assertIn('Corrected narrow support',report)
                self.assertIn('Corrected-grid no-loss lower bound',report)
                self.assertIn('Corrected draw probability',report)
                self.assertIn('Chance of no loss',report)
            text=(out/'conservative_bet_shortlist_report.md').read_text(encoding='utf-8')
            self.assertIn('No general P(narrow) gate',text)
