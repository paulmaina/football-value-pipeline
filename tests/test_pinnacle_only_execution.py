"""Pinnacle-only execution quotes, exact lines and config-independent archived replay."""
import json
import tempfile
from pathlib import Path
from unittest.mock import patch
import pandas as pd
from offline_test_case import OfflineQuotePolicyTestCase
import quote_policy as qp
import price_edge_cagey_shortlist as v28
import master_shortlist as master
from test_cagey_tier_v3 import sample
from test_local_research_v2 import row_with_evidence
from test_price_edge_shortlist import NOW, ah_pair, offer

PIN={'allowed_bookmakers':['Pinnacle'],'per_stake_cost_bps':0}
OLD={'allowed_bookmakers':['Pinnacle','1xBet'],'per_stake_cost_bps':0}


class PinnacleOnlyTests(OfflineQuotePolicyTestCase):
    def test_all_three_lists_use_actual_pinnacle_prices_and_no_other_book_lines(self):
        row=sample()
        row['asian_handicap_offers']=json.dumps(json.loads(row['asian_handicap_offers'])+
            ah_pair(1.,1.25,4.8)+[offer('away',3.5,1.21)])
        original=row['team_research_json']
        predictions=pd.DataFrame([row])
        with qp.policy_scope(PIN):
            value,decisions,summary=v28.build_shortlist(predictions,NOW)
            cagey=v28.cagey_tier_list(decisions)
            top=master.build(decisions,predictions,master.VERSION_CONTEXT)
        for name,frame in [('value',value),('cagey',cagey),('master',top)]:
            with self.subTest(name=name):
                self.assertGreater(len(frame),0)
                self.assertTrue(frame.bookmaker.eq('Pinnacle').all())
                self.assertNotIn('Asian Handicap Away +3.50',frame.market.tolist())
                ah=frame.loc[frame.market.str.startswith('Asian Handicap ')]
                for r in ah.to_dict('records'):
                    observed=[o for o in json.loads(row['asian_handicap_offers'])
                        if o['bookmaker']=='Pinnacle' and o['side']==r['handicap_side']
                        and o['line']==r['handicap_line'] and o['price']==r['offered_decimal_odds']]
                    self.assertTrue(observed)
        self.assertEqual(summary['quote_execution_policy']['allowed_bookmakers'],['Pinnacle'])
        self.assertEqual(row['team_research_json'],original)

    def test_missing_pinnacle_offer_never_falls_back_to_1xbet(self):
        row=row_with_evidence();row['asian_handicap_offers']='[]'
        row['price_edge_quotes']=json.dumps([q for q in json.loads(row['price_edge_quotes']) if q['bookmaker']=='1xBet'])
        with qp.policy_scope(PIN):
            selected,decisions,_=v28.build_shortlist(pd.DataFrame([row]),NOW)
            self.assertTrue(selected.empty)
            self.assertTrue(v28.cagey_tier_list(decisions).empty)
            self.assertTrue(master.build(decisions,pd.DataFrame([row]),master.VERSION_CONTEXT).empty)

    def test_old_three_lists_replay_under_frozen_policy_after_switch_to_pinnacle_only(self):
        from workflow_checks import raw_check
        from pipeline_health import write_generation_metadata
        row=row_with_evidence();row['asian_handicap_offers']='[]'
        predictions=pd.DataFrame([row])
        value,decisions,info=v28.build_shortlist(predictions,NOW,execution_policy=OLD)
        self.assertTrue(value.bookmaker.eq('1xBet').any())
        with tempfile.TemporaryDirectory() as tmp,qp.policy_scope(PIN):
            root=Path(tmp);raw=root/'raw';raw.mkdir()
            predictions.to_csv(raw/'all_leagues_predictions.csv',index=False)
            value.to_csv(raw/'conservative_bet_shortlist.csv',index=False)
            decisions.to_csv(raw/'conservative_bet_rejections.csv',index=False)
            v28.cagey_tier_list(decisions).to_csv(raw/v28.TIER_FILE,index=False)
            top=master.write(decisions,raw,info,predictions)
            self.assertTrue(top.bookmaker.eq('1xBet').any())
            (raw/'conservative_bet_summary.json').write_text(json.dumps(info),encoding='utf-8')
            write_generation_metadata(raw,info)
            with patch('requests.sessions.Session.request',side_effect=AssertionError('Replay must be offline')):
                self.assertEqual(raw_check(root)['selections'],len(value))
            archived=master.build(decisions,predictions,master.VERSION_CONTEXT,execution_policy=OLD)
            self.assertTrue(master.matches(top,archived))
            # Live calls still enforce today's rule, even after a legacy replay.
            self.assertTrue(master.build(decisions,predictions,master.VERSION_CONTEXT).empty)
            self.assertEqual(qp.load_policy()['allowed_bookmakers'],['Pinnacle'])

    def test_api_requests_name_pinnacle_and_isolate_its_cache(self):
        from football_value_pipeline_v2_standalone import TheOddsAPI,LEAGUES
        api=TheOddsAPI.__new__(TheOddsAPI);api.regions='eu';api.api_key='fake';api.force_refresh=False
        for policy,scope in [(PIN,'pinnacle'),(OLD,'onexbet_pinnacle'),({'allowed_bookmakers':[]},'all')]:
            with self.subTest(scope=scope),qp.policy_scope(policy):
                with patch.object(api,'_get_json',return_value=[]) as request:
                    api.odds(LEAGUES['EPL'],3,NOW.to_pydatetime())
                main=request.call_args
                with patch.object(api,'_get_json',return_value={'id':'event0','bookmakers':[]}) as request:
                    api.extra_markets_for_event(LEAGUES['EPL'],'event0')
                extra=request.call_args
                for call in [main,extra]:
                    self.assertIn('_'+scope,call.args[1])
                    self.assertEqual(call.kwargs['params']['regions'],'eu')
                    expected='pinnacle' if scope=='pinnacle' else 'onexbet,pinnacle' if scope!='all' else None
                    self.assertEqual(call.kwargs['params'].get('bookmakers'),expected)

    def test_frozen_policy_scope_restores_after_nested_scope_and_exception(self):
        before=qp.load_policy()
        with qp.policy_scope(PIN):
            self.assertFalse(qp.usable_bookmaker('1xBet'))
            with self.assertRaises(RuntimeError):
                with qp.policy_scope(OLD):
                    self.assertTrue(qp.usable_bookmaker('1xBet'))
                    raise RuntimeError('test')
            self.assertFalse(qp.usable_bookmaker('1xBet'))
        self.assertEqual(qp.load_policy(),before)
