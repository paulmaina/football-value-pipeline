"""Versioned eligibility, executable Double Chance competition and readable alternatives."""
import copy
import json
from datetime import timedelta
from pathlib import Path
import tempfile

import pandas as pd

import asian_handicap as ah
from conservative_bet_filter import build_conservative_shortlist
from double_chance import parse_quotes, probabilities
from format_football_output import process_conservative_shortlist
from offline_test_case import OfflineQuotePolicyTestCase
from test_asian_handicap import NOW, POLICY, choose, quote, reliability, row


def dc_fixture(key='home_draw', ev=.12, offers=None):
    value = row(offers=[] if offers is None else offers)
    outcomes = {'home_draw':(.65,.18,.17), 'draw_away':(.17,.18,.65), 'home_away':(.45,.17,.38)}[key]
    for prefix in ('p_', 'raw_p_'):
        value.update({prefix+k:p for k,p in zip(('home','draw','away'),outcomes)})
    value.update(probabilities(value))
    value.update(parse_quotes({'home_team':value['home_team'], 'away_team':value['away_team'],
        'bookmakers':[{'title':'Pinnacle', 'markets':[{'key':'double_chance', 'last_update':NOW.isoformat(),
        'outcomes':[{'name':'1X','price':1.35},{'name':'X2','price':2.4},{'name':'12','price':1.12}]}]}]},as_of=NOW))
    for other in ('home_draw','draw_away','home_away'):
        value['market_'+other+'_odds'] = (1+ev)/value['p_'+key] if other == key else None
    value['goal_margin_distribution'] = value['raw_goal_margin_distribution'] = json.dumps({'-1':.17,'0':.18,'1':.65})
    reports = reliability()
    for k in ('home_draw','draw_away','home_away'):
        state = copy.deepcopy(reports['Premier League']['markets']['home'])
        for group in state['high_confidence'].values():
            group['status'] = 'PASSED'
        reports['Premier League']['markets'][k] = state
    return value, reports


class ShortlistMarketAlternativesTests(OfflineQuotePolicyTestCase):
    def test_each_double_chance_market_competes_with_one_percent_ev_floor(self):
        for key, label in [('home_draw','Double Chance 1X'),('draw_away','Double Chance X2'),('home_away','Double Chance 12')]:
            for ev, expected in ((.0099,0),(.01,1),(.12,1)):
                value, reports = dc_fixture(key, ev)
                picks, decisions, summary = choose([value],reports)
                with self.subTest(key=key,ev=ev):
                    self.assertEqual(len(picks),expected)
                    if expected:
                        self.assertEqual(picks.iloc[0].market,label)
                        self.assertEqual(picks.iloc[0].p_refund,0)
                    self.assertNotIn('Draw',decisions.market.tolist())
                    self.assertNotIn('Draw',summary['eligible_markets'])

    def test_dc_quote_history_and_raw_ev_gates_are_not_bypassed(self):
        for change in ('missing','stale','history','raw'):
            value, reports = dc_fixture()
            if change == 'missing': value['market_home_draw_odds'] = None
            if change == 'stale': value['market_best_home_draw_last_update_utc'] = (NOW-timedelta(hours=25)).isoformat()
            if change == 'history': reports['Premier League']['markets'].pop('home_draw')
            if change == 'raw': value['raw_p_home_draw'] = .5
            self.assertTrue(choose([value],reports)[0].empty,change)

    def test_equivalent_dc_and_handicap_compete_by_ev_and_show_alternative(self):
        for price, winning in ((1.30,'Double Chance 1X'),(1.50,ah.label('home',.5))):
            value, reports = dc_fixture(offers=[{**quote(point=.5,price=price),'opposite_price':3.0}])
            picks, decisions, summary = choose([value],reports)
            self.assertEqual(picks.iloc[0].market,winning)
            self.assertEqual(len(picks),1)
            alternatives = ah.qualifying_alternatives(picks,decisions,.01)
            alternative = alternatives[0]
            self.assertNotEqual(ah.market_family(alternative['market']),ah.market_family(winning))
            self.assertTrue(alternative['within_selected_risk_band'])
            self.assertAlmostEqual(alternative['loss_probability_upper'],picks.iloc[0].loss_probability_upper)
            with tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp); raw = root/'raw'; output = root/'readable'
                raw.mkdir(); output.mkdir()
                picks.to_csv(raw/'conservative_bet_shortlist.csv',index=False)
                decisions.to_csv(raw/'conservative_bet_rejections.csv',index=False)
                (raw/'conservative_bet_summary.json').write_text(json.dumps(summary))
                pd.DataFrame([value]).to_csv(raw/'all_leagues_predictions.csv',index=False)
                (raw/'EPL_goal_market_validation.json').write_text(json.dumps(reports['Premier League']))
                from workflow_checks import raw_check
                self.assertEqual(raw_check(root)['selections'],1)
                before = {p:p.read_bytes() for p in raw.iterdir()}
                self.assertEqual(process_conservative_shortlist(raw,output),1)
                readable = pd.read_csv(output/'conservative_bet_shortlist_readable.csv')
                self.assertEqual(readable.iloc[0]['Shortlisted market'],winning)
                self.assertEqual(readable.iloc[0]['Alternative market'],alternative['market'])
                self.assertIn('within selected risk band',readable.iloc[0]['Alternative comparison'])
                text = (output/'conservative_bet_shortlist_report.md').read_text()
                self.assertIn('Qualifying alternatives for comparison',text)
                self.assertIn('Alternative adjusted EV',text)
                self.assertEqual(before,{p:p.read_bytes() for p in before})
                # A ledger from a different run must never supply alternatives.
                decisions['evaluated_at_utc'] = (NOW-timedelta(days=1)).isoformat()
                decisions.to_csv(raw/'conservative_bet_rejections.csv',index=False)
                process_conservative_shortlist(raw,output)
                readable = pd.read_csv(output/'conservative_bet_shortlist_readable.csv')
                self.assertEqual(readable.iloc[0]['Alternative comparison'],'Candidate ledger unavailable')

    def test_other_type_preferred_and_higher_risk_is_disclosed(self):
        value, reports = dc_fixture(ev=.08,offers=[quote(point=0,price=1.8),quote(point=.5,price=1.9)])
        reports['Premier League']['markets']['home_draw']['confidence_penalty'] = .03
        picks, decisions, _ = choose([value],reports)
        self.assertEqual(picks.iloc[0].market,ah.label('home',.5))
        alternative = ah.qualifying_alternatives(picks,decisions,.01)[0]
        self.assertEqual(alternative['market'],'Double Chance 1X')
        self.assertFalse(alternative['within_selected_risk_band'])
        self.assertIn('Different market type',alternative['alternative_scope'])
        # No cross-market candidate: keep another qualifying handicap line visible.
        decisions = decisions[~decisions.market.str.startswith('Double Chance')]
        alternative = ah.qualifying_alternatives(picks,decisions,.01)[0]
        self.assertEqual(alternative['market'],ah.label('home',0))
        self.assertIn('Same market type',alternative['alternative_scope'])
        self.assertEqual(ah.qualifying_alternatives(picks,decisions[decisions.market==picks.iloc[0].market],.01),{})

    def test_draw_is_excluded_but_v20_can_still_replay_it(self):
        value = row(offers=[])
        for key in ('home','draw','away'):
            value.update({f'p_{key}':.8 if key=='draw' else .1,
                          f'raw_p_{key}':.8 if key=='draw' else .1,
                          f'market_p_{key}':.8 if key=='draw' else .1,
                          f'market_reference_{key}_odds':1.25 if key=='draw' else 8.})
        value.update(market_draw_odds=1.3,best_draw_bookmaker='Pinnacle',
                     market_best_draw_last_update_utc=NOW.isoformat(),market_reference_draw_last_update_utc=NOW.isoformat())
        reports = reliability();reports['Premier League']['markets']['draw'] = copy.deepcopy(reports['Premier League']['markets']['home'])
        self.assertTrue(choose([value],reports)[0].empty)
        picks, _, summary = build_conservative_shortlist(pd.DataFrame([value]),as_of=NOW,
            market_reliability=reports,execution_policy=POLICY,selection_policy_version=ah.PREVIOUS_POLICY)
        self.assertEqual(picks.iloc[0].market,'Draw')
        self.assertNotIn('Double Chance 1X',summary['eligible_markets'])
        self.assertEqual(summary['min_estimated_ev'],.01)
