"""Win ranking, refund separation, evidence, executable quotes and frozen grades."""
import copy
import json
from pathlib import Path
import tempfile

import pandas as pd

import asian_handicap as ah
from conservative_bet_filter import build_conservative_shortlist
from format_football_output import process_conservative_shortlist
from goal_market_validation import evaluate_market_history, validation_cache_matches, VALIDATOR_VERSION
from offline_test_case import OfflineQuotePolicyTestCase
from performance_tracking import score_shortlist, calibration_buckets
from performance_excel import prepared_rows
from test_asian_handicap import NOW, POLICY, quote, reliability, row
from test_shortlist_market_alternatives import dc_fixture
from win_first_shortlist import POLICY as WIN_POLICY, VALIDATOR_VERSION as WIN_VALIDATOR


def reports():
    result = reliability()
    result['Premier League']['asian_handicap_win'] = {
        **copy.deepcopy(result['Premier League']['asian_handicap']),
        'version': WIN_VALIDATOR, 'probability_basis': 'net_profit'}
    return result


def select(values, evidence=None, policy=POLICY):
    return build_conservative_shortlist(pd.DataFrame(values), as_of=NOW,
        market_reliability=reports() if evidence is None else evidence,
        execution_policy=policy, selection_policy_version=WIN_POLICY)


class WinFirstTests(OfflineQuotePolicyTestCase):
    def test_refund_heavy_handicap_loses_to_higher_profitable_chance(self):
        value, evidence = dc_fixture(offers=[quote()])
        evidence['Premier League']['asian_handicap_win'] = reports()['Premier League']['asian_handicap_win']
        value['goal_margin_distribution'] = value['raw_goal_margin_distribution'] = json.dumps({'-1':.1,'0':.4,'1':.5})
        picks, decisions, summary = select([value], evidence)
        self.assertEqual(picks.iloc[0].market, 'Double Chance 1X')
        handicap = decisions.loc[decisions.market == ah.label('home',0)].iloc[0]
        self.assertAlmostEqual(handicap.predicted_probability,.5)
        self.assertAlmostEqual(handicap.p_no_loss,.9)
        self.assertAlmostEqual(handicap.p_refund,.4)
        self.assertEqual(summary['probability_basis'],'net_profit')
        self.assertFalse(summary['ev_required_for_selection'])

    def test_half_wins_count_but_refunds_do_not_and_ev_uses_half_payoff(self):
        picks, _, _ = select([row(offers=[quote(point=.25)])])
        pick = picks.iloc[0]
        self.assertAlmostEqual(pick.p_profit,.85)
        self.assertAlmostEqual(pick.p_half_win,.30)
        self.assertAlmostEqual(pick.p_full_win,.55)
        self.assertAlmostEqual(pick.estimated_ev,.55*.8+.30*.4-.15)

    def test_twelve_distinct_matches_no_75_floor_or_ev_floor(self):
        values = [row(i,offers=[{**quote(price=1.2),'opposite_price':5.0}]) for i in range(15)]
        picks, _, summary = select(values)
        self.assertEqual(len(picks),12)
        self.assertEqual(picks.home_team.nunique(),12)
        self.assertEqual(summary['status'],'TARGET_MET')
        self.assertEqual(summary['negative_adjusted_ev_selections'],12)
        self.assertTrue((picks.p_profit < .75).all())
        self.assertTrue(picks.selection_warnings.str.contains('NEGATIVE ADJUSTED EV').all())

    def test_order_is_probability_first_ev_breaks_ties(self):
        a,b,c = row(0),row(1),row(2)
        a['goal_margin_distribution']=a['raw_goal_margin_distribution']=json.dumps({'-1':.1,'0':.3,'1':.6})
        b['asian_handicap_offers']=json.dumps([{**quote(price=2.2),'opposite_price':1.9}])
        picks,_,_=select([b,c,a])
        self.assertEqual(list(picks.home_team),[a['home_team'],b['home_team'],c['home_team']])

    def test_only_exact_allowed_fresh_quotes_and_horizon(self):
        for book in ('Pinnacle','bet365'):
            self.assertEqual(len(select([row(offers=[quote(book=book)])])[0]),1)
        # v23 rejects 1xBet even under an obsolete broad execution allowlist.
        self.assertTrue(select([row(offers=[quote(book='1xBet')])],policy={**POLICY,'allowed_bookmakers':['Pinnacle','bet365','1xBet']})[0].empty)
        for mutate in (
            lambda r:r.update(kickoff_utc=(NOW+pd.Timedelta(hours=49)).isoformat()),
            lambda r:r.update(kickoff_utc=(NOW+pd.Timedelta(minutes=10)).isoformat()),
            lambda r:r.update(home_name_match_score=20),
            lambda r:r.update(asian_handicap_offers=json.dumps([{**quote(),'last_update_utc':(NOW-pd.Timedelta(days=2)).isoformat()}])),
        ):
            value=row();mutate(value)
            self.assertTrue(select([value])[0].empty)
        picks,_,summary=select([row(offers=[])])
        self.assertTrue(picks.empty);self.assertEqual(summary['shortfall'],12)

    def test_win_evidence_required_not_substituted_with_no_loss_validation(self):
        self.assertTrue(select([row()],reliability())[0].empty)
        for change in ({'status':'UNRELIABLE_AUDIT'},{'development_matches':79},
                       {'audit_matches':39},{'confidence_penalty':float('nan')}):
            evidence=reports()
            evidence['Premier League']['asian_handicap_win']['markets'][ah.label('home',0)].update(change)
            self.assertTrue(select([row()],evidence)[0].empty)
        evidence=reports()
        evidence['Premier League']['asian_handicap']['markets'][ah.label('home',0)]['status']='UNRELIABLE_AUDIT'
        self.assertEqual(len(select([row()],evidence)[0]),1)

    def test_win_penalty_and_unblended_probability_limit_ranking(self):
        evidence=reports()
        evidence['Premier League']['asian_handicap_win']['markets'][ah.label('home',0)]['confidence_penalty']=.1
        value=row();value['raw_goal_margin_distribution']=json.dumps({'-1':.3,'0':.3,'1':.4})
        picks,_,_=select([value],evidence)
        self.assertAlmostEqual(picks.iloc[0].rank_probability,.3)

    def test_history_separates_refund_from_win_and_invalidates_old_cache(self):
        data=pd.DataFrame([{'date':str(d),'home_goals':1,'away_goals':1,
             'goal_margin_distribution':json.dumps({'0':1.})}
             for d in pd.date_range('2025-01-01',periods=160)])
        old=ah.evaluate_history(data)['markets'][ah.label('home',0)]
        new=ah.evaluate_history(data,basis='net_profit')['markets'][ah.label('home',0)]
        self.assertEqual(old['audit_brier'],0)
        self.assertEqual(new['audit_brier'],0)
        # Calibration target differs: probability one for no loss, zero for profit.
        self.assertIn('refunds excluded',new['note'])
        report=evaluate_market_history(pd.DataFrame(),'Premier League')
        config={'validator_version':VALIDATOR_VERSION,'training_sha256':'a'*64,'validation_code_sha256':'b'*64}
        report['config']=config
        self.assertTrue(validation_cache_matches(report,config))
        del report['asian_handicap_win']
        self.assertFalse(validation_cache_matches(report,config))

    def test_refund_is_not_a_win_in_grades_excel_or_calibration(self):
        pick=select([row()])[0].iloc[0].to_dict()
        pick.update(fixture_key='fixture',snapshot_commit='a'*40,snapshot_captured_utc=NOW.isoformat())
        final={'home_goals':1,'away_goals':1,'match_id':1}
        grade=score_shortlist(pick,final,'VERIFIED_FINISHED')
        self.assertEqual(grade['status'],'REFUNDED')
        self.assertEqual(grade['probability_basis'],'net_profit')
        self.assertAlmostEqual(grade['brier'],.55**2)
        self.assertEqual(prepared_rows([grade])[0]['y'],0)
        self.assertEqual(calibration_buckets([grade])[0]['observed_win_rate'],0)
        old=score_shortlist({**pick,'probability_basis':'net_no_loss'},final,'VERIFIED_FINISHED')
        self.assertAlmostEqual(old['brier'],(.85-1)**2)

    def test_readable_report_and_best_per_match_follow_win_ranking(self):
        value=row(offers=[{**quote(price=1.2),'opposite_price':5.0}])
        picks,decisions,summary=select([value])
        self.assertEqual(ah.best_per_match(decisions).iloc[0].market,picks.iloc[0].market)
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory);raw=root/'raw';out=root/'readable';raw.mkdir();out.mkdir()
            picks.to_csv(raw/'conservative_bet_shortlist.csv',index=False)
            (raw/'conservative_bet_summary.json').write_text(json.dumps(summary))
            process_conservative_shortlist(raw,out)
            text=(out/'conservative_bet_shortlist_report.md').read_text()
            self.assertIn('NEGATIVE ADJUSTED EV',text)
            self.assertIn('refunds and losses do not',text)
            self.assertNotIn('Asian model chance includes refunds',text)

    def test_empty_and_current_dispatch(self):
        picks,_,summary=select([])
        self.assertTrue(picks.empty)
        self.assertEqual(summary['selection_policy_version'],WIN_POLICY)
        self.assertEqual(ah.CURRENT_POLICY,WIN_POLICY)
        with self.assertRaises(ValueError):
            ah.build_shortlist(pd.DataFrame([row()]),NOW,reports(),adjusted_ev_floor=.01,policy_version=WIN_POLICY)

    def test_frozen_replay_checks_top_twelve_and_value_warning(self):
        from workflow_checks import raw_check
        values=[row(i) for i in range(13)]
        picks,_,summary=select(values)
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory);raw=root/'raw';raw.mkdir()
            pd.DataFrame(values).to_csv(raw/'all_leagues_predictions.csv',index=False)
            picks.to_csv(raw/'conservative_bet_shortlist.csv',index=False)
            (raw/'conservative_bet_summary.json').write_text(json.dumps(summary))
            evidence=reports()['Premier League'];evidence['league']='Premier League'
            (raw/'EPL_goal_market_validation.json').write_text(json.dumps(evidence))
            self.assertEqual(raw_check(root)['selections'],12)
            picks.loc[0,'rank_probability']=.99
            picks.to_csv(raw/'conservative_bet_shortlist.csv',index=False)
            with self.assertRaisesRegex(ValueError,'deterministic ranking replay'):
                raw_check(root)

    def test_grade_uses_adjusted_win_probability_and_ordinary_quote_timestamp(self):
        evidence=reports();evidence['Premier League']['asian_handicap_win']['markets'][ah.label('home',0)]['confidence_penalty']=.1
        pick=select([row()],evidence)[0].iloc[0].to_dict()
        pick.update(fixture_key='fixture',snapshot_commit='a'*40,snapshot_captured_utc=NOW.isoformat())
        grade=score_shortlist(pick,{'home_goals':1,'away_goals':1,'match_id':1},'VERIFIED_FINISHED')
        self.assertAlmostEqual(grade['brier'],.45**2)
        value,evidence=dc_fixture(offers=[])
        ordinary=select([value],evidence)[0].iloc[0]
        self.assertEqual(pd.Timestamp(ordinary.quote_last_update_utc),pd.Timestamp(NOW))
