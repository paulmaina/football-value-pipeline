"""Common risk eligibility, zero-tolerance ranking and frozen-policy replay."""
import json
from pathlib import Path
import tempfile

import pandas as pd

import asian_handicap as ah
from conservative_bet_filter import build_conservative_shortlist
from double_chance import probabilities
from format_football_output import process_conservative_shortlist
from offline_test_case import OfflineQuotePolicyTestCase
from quote_policy import validate_policy
from test_asian_handicap import NOW, POLICY, choose, quote, reliability, row
from test_shortlist_market_alternatives import dc_fixture


def select(values, reports=None, policy=POLICY):
    return build_conservative_shortlist(pd.DataFrame(values),as_of=NOW,
        market_reliability=reliability() if reports is None else reports,
        execution_policy=policy,selection_policy_version=ah.POLICY)


class CommonNoLossPolicyTests(OfflineQuotePolicyTestCase):
    def test_handicap_boundary_refunds_count_and_high_risk_is_not_padded(self):
        for loss, expected in ((.2499,1),(.25,1),(.2501,0),(.40,0)):
            value=row(offers=[{**quote(price=2.2),'opposite_price':1.9}])
            value['goal_margin_distribution']=value['raw_goal_margin_distribution']=json.dumps({'-1':loss,'0':.2,'1':.8-loss})
            picks, decisions, summary=select([value])
            self.assertEqual(len(picks),expected)
            self.assertEqual(summary['min_adjusted_no_loss_probability'],.75)
            self.assertEqual(summary['max_estimated_loss_probability'],.25)
            self.assertEqual(summary['loss_risk_tolerance'],0)
            item=decisions[decisions.market==ah.label('home',0)].iloc[0]
            self.assertGreater(item.conservative_estimated_ev,.01)
            if expected:
                self.assertAlmostEqual(item.p_refund,.2)
                self.assertLess(item.p_full_win,.75)
            else:
                self.assertIn('adjusted probability of avoiding loss below 75%',item.rejection_reasons)
                self.assertEqual(summary['status'],'NO BET')

    def test_zero_tolerance_prevents_higher_ev_handicap_displacing_safer_dc(self):
        value,reports=dc_fixture(offers=[quote()])
        value['goal_margin_distribution']=value['raw_goal_margin_distribution']=json.dumps({'-1':.178,'0':.18,'1':.642})
        old,_,old_summary=choose([value],reports)
        self.assertEqual(old.iloc[0].market,ah.label('home',0))
        self.assertEqual(old_summary['loss_risk_tolerance'],.01)
        picks,decisions,summary=select([value],reports)
        self.assertEqual(picks.iloc[0].market,'Double Chance 1X')
        self.assertAlmostEqual(picks.iloc[0].loss_probability_upper,.17)
        alternative=ah.qualifying_alternatives(picks,decisions,0)[0]
        self.assertGreater(alternative['conservative_estimated_ev'],picks.iloc[0].conservative_estimated_ev)
        self.assertFalse(alternative['within_selected_risk_band'])
        self.assertEqual(summary['selection_policy_version'],ah.POLICY)

    def test_equal_risk_candidates_still_compete_on_ev(self):
        value,reports=dc_fixture(offers=[{**quote(point=.5,price=1.5),'opposite_price':3.0}])
        picks,decisions,_=select([value],reports)
        self.assertEqual(picks.iloc[0].market,ah.label('home',.5))
        dc=decisions[decisions.market=='Double Chance 1X'].iloc[0]
        self.assertAlmostEqual(dc.loss_probability_upper,picks.iloc[0].loss_probability_upper)
        self.assertGreater(picks.iloc[0].conservative_estimated_ev,dc.conservative_estimated_ev)

    def test_ordinary_markets_use_common_floor_instead_of_unequal_old_floors(self):
        for probability,expected in ((.7499,0),(.75,1),(.76,1)):
            value=row(offers=[])
            value.update(p_over_1_5=probability,raw_p_over_1_5=probability,
                market_over_1_5_odds=1.5,best_over_1_5_bookmaker='Pinnacle')
            picks,_,_=select([value])
            self.assertEqual(len(picks),expected)
            self.assertTrue(choose([value])[0].empty)  # v21 retains the 78% floor.
        for probability,expected in ((.7499,0),(.75,1),(.76,1)):
            value,reports=dc_fixture()
            for prefix in ('p_','raw_p_'):
                value.update({prefix+'home':probability-.16,prefix+'draw':.16,prefix+'away':1-probability})
            value.update(probabilities(value));value['market_home_draw_odds']=1.6
            picks,_,_=select([value],reports)
            self.assertEqual(len(picks),expected)
            self.assertTrue(choose([value],reports)[0].empty)  # v21 retains the 80% blended floor.

    def test_home_and_away_wins_share_the_same_cutoff(self):
        for key in ('home','away'):
            for probability,expected in ((.70,0),(.7499,0),(.75,1)):
                value=row(offers=[])
                for prefix in ('p_','raw_p_'):
                    for side in ('home','draw','away'):
                        value[prefix+side]=probability if side==key else (1-probability)/2
                value.update({f'market_{key}_odds':1.6,f'best_{key}_bookmaker':'Pinnacle'})
                picks,_,_=select([value])
                self.assertEqual(len(picks),expected)
                if expected:self.assertEqual(picks.iloc[0].market,'Home win' if key=='home' else 'Away win')

    def test_raw_disagreement_and_calibration_are_included_in_every_risk_estimate(self):
        value,reports=dc_fixture();value['market_home_draw_odds']=1.6
        value['raw_p_home_draw']=.70
        picks,decisions,_=select([value],reports)
        self.assertTrue(picks.empty)
        dc=decisions[decisions.market=='Double Chance 1X'].iloc[0]
        self.assertAlmostEqual(dc.loss_probability_upper,.30)
        self.assertGreater(dc.raw_dc_ev,0)
        value['raw_p_home_draw']=value['p_home_draw']=.79
        reports['Premier League']['markets']['home_draw']['confidence_penalty']=.05
        picks,decisions,_=select([value],reports)
        self.assertTrue(picks.empty)
        dc=decisions[decisions.market=='Double Chance 1X'].iloc[0]
        self.assertAlmostEqual(dc.loss_probability_upper,.26)
        self.assertGreater(dc.conservative_estimated_ev,.01)
        self.assertIn('avoiding loss below 75%',dc.rejection_reasons)
        ah_value=row();ah_value['raw_goal_margin_distribution']=json.dumps({'-1':.3,'0':.2,'1':.5})
        self.assertTrue(select([ah_value])[0].empty)

    def test_ev_and_historical_integrity_gates_remain_required(self):
        for ev,expected in ((.0099,0),(.01,1)):
            value,reports=dc_fixture(ev=ev)
            self.assertEqual(len(select([value],reports)[0]),expected)
            price=(ev+.7)/.55
            value=row(offers=[{**quote(price=price),'opposite_price':3.0}])
            self.assertEqual(len(select([value])[0]),expected)
        value,reports=dc_fixture()
        reports['Premier League']['markets'].pop('home_draw')
        self.assertTrue(select([value],reports)[0].empty)
        value=row();value['raw_goal_margin_distribution']=json.dumps({'-1':.15,'0':.84,'1':.01})
        picks,decisions,_=select([value])
        self.assertTrue(picks.empty)
        candidate=decisions[decisions.market==ah.label('home',0)].iloc[0]
        self.assertGreater(candidate.rank_probability,.75)
        self.assertLess(candidate.raw_dc_ev,0)

    def test_common_floor_is_frozen_validated_and_risk_tolerance_must_be_zero(self):
        value=row();value['goal_margin_distribution']=value['raw_goal_margin_distribution']=json.dumps({'-1':.23,'0':.2,'1':.57})
        policy={**POLICY,'min_adjusted_no_loss_probability':.8,'asian_handicap_risk_tolerance':0}
        picks,_,summary=select([value],policy=policy)
        self.assertTrue(picks.empty)
        self.assertEqual(summary['quote_execution_policy']['min_adjusted_no_loss_probability'],.8)
        for bad in (True,'0.75',-.01,1.01,float('nan')):
            with self.assertRaises(ValueError):validate_policy({'min_adjusted_no_loss_probability':bad})
        with self.assertRaisesRegex(ValueError,'zero risk tolerance'):
            select([row()],policy={**POLICY,'asian_handicap_risk_tolerance':.01})
        # Archived v21 tolerances and probabilities are not relabelled as v22.
        old,_,summary=choose([value])
        self.assertEqual(len(old),1)
        self.assertNotIn('min_adjusted_no_loss_probability',summary)

    def test_reports_and_integrity_replay_freeze_common_safety_settings(self):
        value,reports=dc_fixture()
        picks,decisions,summary=select([value],reports)
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);raw=root/'raw';output=root/'readable';raw.mkdir();output.mkdir()
            pd.DataFrame([value]).to_csv(raw/'all_leagues_predictions.csv',index=False)
            picks.to_csv(raw/'conservative_bet_shortlist.csv',index=False)
            decisions.to_csv(raw/'conservative_bet_rejections.csv',index=False)
            (raw/'conservative_bet_summary.json').write_text(json.dumps(summary))
            (raw/'EPL_goal_market_validation.json').write_text(json.dumps(reports['Premier League']))
            from workflow_checks import raw_check
            self.assertEqual(raw_check(root)['selections'],1)
            process_conservative_shortlist(raw,output)
            text=(output/'conservative_bet_shortlist_report.md').read_text()
            self.assertIn('Common safety cutoff',text);self.assertIn('75.0%',text)
            self.assertIn('Zero risk tolerance',text)
            readable=pd.read_csv(output/'conservative_bet_shortlist_readable.csv')
            self.assertEqual(readable.iloc[0]['Minimum adjusted no-loss chance'],'75.0%')
            summary['min_adjusted_no_loss_probability']=.8
            (raw/'conservative_bet_summary.json').write_text(json.dumps(summary))
            with self.assertRaisesRegex(ValueError,'min_adjusted_no_loss_probability'):
                raw_check(root)
