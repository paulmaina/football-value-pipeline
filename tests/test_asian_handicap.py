"""Settlement, risk-first decisions, input binding and forward-report integration."""
from offline_test_case import OfflineQuotePolicyTestCase
from datetime import timedelta
import copy
import json
from pathlib import Path
import tempfile
from unittest.mock import patch

import numpy as np
import pandas as pd

import asian_handicap as ah
from conservative_bet_filter import build_conservative_shortlist
from test_conservative_bet_filter import NOW, fixture
from test_graded_candidates import sample_report


POLICY = {'allowed_bookmakers':['Pinnacle','bet365'],'per_stake_cost_bps':0}


def quote(side='home', point=0, price=1.8, book='Pinnacle'):
    return {'side':side,'line':point,'price':price,'opposite_price':2.05,
            'bookmaker':book,'last_update_utc':NOW.isoformat(),'market_key':'alternate_spreads'}


def row(i=0, offers=None):
    value = fixture(i)
    # No binary quotes: tests isolate Asian selection instead of choosing Over 1.5.
    for key in ('home','draw','away','over_1_5'):
        value['market_'+key+'_odds'] = None
    value.update(goal_margin_distribution=json.dumps({'-1':.15,'0':.30,'1':.35,'2':.20}),
                 raw_goal_margin_distribution=json.dumps({'-1':.15,'0':.30,'1':.35,'2':.20}),
                 asian_handicap_offers=json.dumps(offers if offers is not None else [quote()]))
    return value


def reliability():
    report = sample_report()
    report['league'] = 'Premier League'
    report['asian_handicap'] = {'version':ah.VERSION,'markets':{ah.label(s,p):{
        'status':'RELIABLE_FOR_RANKING','confidence_penalty':0.,
        'development_matches':100,'audit_matches':50,'audit_brier':.1}
        for s in ('home','away') for p in ah.LINES}}
    return {'Premier League':report}


def choose(values, reports=None, policy=POLICY):
    return build_conservative_shortlist(pd.DataFrame(values),as_of=NOW,
        market_reliability=reliability() if reports is None else reports,
        execution_policy=policy,selection_policy_version=ah.POLICY)


def event(book='Pinnacle', key='alternate_spreads', point=0, price=1.8):
    return {'id':'fixture-0','home_team':'Home_0','away_team':'Away_0',
        'commence_time':(NOW+timedelta(days=1)).isoformat(),
        'bookmakers':[{'title':book,'markets':[{'key':key,'last_update':NOW.isoformat(),
            'outcomes':[{'name':'Home_0','point':point,'price':price},
                        {'name':'Away_0','point':-point,'price':2.05}]}]}]}


class AsianHandicapTests(OfflineQuotePolicyTestCase):
    def test_full_split_settlement_and_away_symmetry(self):
        self.assertEqual(ah.label('away',-0.0),'Asian Handicap Away +0.00')
        cases=[(0,0,'REFUNDED',0),(0,-.25,'HALF_LOST',-.5),
               (0,.25,'HALF_WON',.4),(1,-.75,'HALF_WON',.4),
               (1,-1,'REFUNDED',0),(1,-1.25,'HALF_LOST',-.5),
               (2,-1.25,'WON',.8),(-1,.75,'HALF_LOST',-.5),(-2,1,'LOST',-1)]
        for margin,point,status,gain in cases:
            with self.subTest(margin=margin,point=point):
                h,a=max(margin,0),max(-margin,0)
                actual,net=ah.profit(h,a,'home',point,1.8)
                self.assertEqual(actual,status);self.assertAlmostEqual(net,gain)
                self.assertEqual(ah.profit(a,h,'away',point,1.8),(actual,net))
        for point in ah.LINES:
            for margin in range(-5,6):
                won,lost=ah.settlement(margin,point)
                self.assertIn((won,lost),[(1,0),(.5,0),(0,0),(0,.5),(0,1)])

    def test_full_grid_mass_ev_and_refund_are_not_win_probability(self):
        matrix=np.zeros((3,3));matrix[0,1]=.15;matrix[1,1]=.30;matrix[2,1]=.55
        p=ah.probabilities(ah.margins(matrix),'home',0,1.8)
        self.assertAlmostEqual(p['p_no_loss'],.85)
        self.assertAlmostEqual(p['p_full_win'],.55)
        self.assertAlmostEqual(p['p_refund'],.30)
        self.assertAlmostEqual(p['estimated_ev'],.55*.8-.15)
        fee=ah.probabilities(ah.margins(matrix),'home',0,1.8,.01)
        self.assertAlmostEqual(fee['p_no_loss'],.55)
        for point in ah.LINES:
            q=ah.probabilities(ah.margins(matrix),'away',point,1.8)
            self.assertAlmostEqual(sum(q['p_'+k] for k in ah.OUTCOMES),1)
        for bad in (True,.1,4,float('nan')):
            with self.assertRaises((ValueError,TypeError)):ah.line(bad)
        for bad in ({'0':.5},{'0':float('nan')},{'x':1},[]):
            with self.assertRaises((ValueError,TypeError)):ah.distribution(bad)
        with self.assertRaises(ValueError):ah.margins(np.ones((2,2)))
        with self.assertRaises(ValueError):ah.profit(1,0,'other',0,2)
        with self.assertRaises(ValueError):ah.label('other',0)
        self.assertIsNone(ah.parse_label('Asian Handicap Home +9.00'))

    def test_quotes_require_complete_opposite_pairs_and_requested_books(self):
        for book in ('Pinnacle','bet365'):
            self.assertEqual(len(ah.parse_quotes(event(book),NOW)),2)
        d=event();d['bookmakers'][0]['markets'][0]['outcomes'].append({'name':'Home_0','point':.5,'price':1.5})
        self.assertEqual(len(ah.parse_quotes(d,NOW)),2)
        for mutate in (
            lambda d:d.update(home_team=d['away_team']),
            lambda d:d.update(commence_time=NOW.isoformat()),
            lambda d:d['bookmakers'][0].update(title='1xBet'),
            lambda d:d['bookmakers'][0]['markets'][0].update(key='spreads_h1'),
            lambda d:d['bookmakers'][0]['markets'][0].update(last_update=(NOW-timedelta(days=2)).isoformat()),
            lambda d:d['bookmakers'][0]['markets'][0]['outcomes'].pop(),
            lambda d:d['bookmakers'][0]['markets'][0]['outcomes'][1].update(point=.25),
            lambda d:d['bookmakers'][0]['markets'][0]['outcomes'].append({'name':'Draw','price':3}),
            lambda d:d['bookmakers'][0]['markets'][0]['outcomes'].append({'name':'Home_0','point':0,'price':1.8}),
            lambda d:d['bookmakers'][0]['markets'][0]['outcomes'][0].update(price=float('nan')),
        ):
            d=event();mutate(d);self.assertEqual(ah.parse_quotes(d,NOW),[])
        self.assertEqual(len(ah.parse_quotes(event(key='draw_no_bet'),NOW)),2)
        d=event();d['bookmakers']*=2
        self.assertEqual(len(ah.parse_quotes(d,NOW)),2)

    def test_risk_first_then_refund_tie_break_no_negative_ev_padding(self):
        picks,decisions,summary=choose([row(offers=[quote(point=-.5),quote(point=.5),quote(point=0)])])
        self.assertEqual(len(picks),1)
        self.assertEqual(picks.iloc[0].market,ah.label('home',0))
        self.assertAlmostEqual(picks.iloc[0].p_refund,.3)
        self.assertAlmostEqual(picks.iloc[0].loss_probability_upper,.15)
        self.assertEqual(summary['n_provisional_watchlist'],0)
        self.assertFalse(any('Double Chance' in x for x in summary['eligible_markets']))
        picks,failed,_=choose([row(offers=[{**quote(price=1.2),'opposite_price':4.0}])])
        self.assertTrue(picks.empty)
        self.assertTrue(failed.rejection_reasons.str.contains('positive conservative EV').any())
        values=[row(i) for i in range(20)]
        # All fixtures inside the same hard 48-hour window.
        for value in values:value['kickoff_utc']=(NOW+timedelta(days=1)).isoformat()
        picks,_,summary=choose(values)
        self.assertEqual(len(picks),12);self.assertEqual(picks.fixture_id.nunique(),12)
        self.assertEqual(summary['status'],'TARGET_MET')
        self.assertEqual(len(ah.best_per_match(choose(values)[1])),20)

    def test_missing_unreliable_stale_and_unknown_data_fail_closed(self):
        mutations=[lambda d:d.update(asian_handicap_offers='bad'),
                   lambda d:d.update(asian_handicap_offers=json.dumps({})),
                   lambda d:d.update(goal_margin_distribution='{}'),
                   lambda d:d.update(home_name_match_score=50),
                   lambda d:d.update(home_name_match_score=float('nan')),
                   lambda d:d.update(model_home_team='__LEAGUE_AVERAGE__'),
                   lambda d:d.update(league='Other'),
                   lambda d:d.update(odds_source='Other'),
                   lambda d:d.update(kickoff_utc=NOW.isoformat()),
                   lambda d:d.update(market_reference_1x2_last_update_utc=''),
                   lambda d:d.update(asian_handicap_offers=json.dumps([quote(book='1xBet')])),
                   lambda d:d.update(asian_handicap_offers=json.dumps([{**quote(),'last_update_utc':(NOW-timedelta(days=3)).isoformat()}])),
                   lambda d:d.update(asian_handicap_offers=json.dumps([{**quote(),'market_key':'corners'}]))]
        for mutate in mutations:
            d=row();mutate(d);self.assertTrue(choose([d])[0].empty)
        self.assertTrue(choose([row()],reports={})[0].empty)
        report=reliability();report['Premier League']['asian_handicap']['markets'][ah.label('home',0)]['status']='UNRELIABLE_AUDIT'
        self.assertTrue(choose([row()],reports=report)[0].empty)
        self.assertTrue(choose([row()],policy={**POLICY,'per_stake_cost_bps':10})[0].empty)
        with self.assertRaises(ValueError):choose([row()],policy={'allowed_bookmakers':[],'per_stake_cost_bps':-1})
        with self.assertRaises(ValueError):ah.build_shortlist(pd.DataFrame([row()]),NOW.replace(tzinfo=None),reliability())
        with self.assertRaises(ValueError):ah.build_shortlist(pd.DataFrame([row()]),NOW,reliability(),adjusted_ev_floor=.001)

    def test_chronological_calibration_and_insufficient_history(self):
        empty=ah.evaluate_history(pd.DataFrame())['markets']
        self.assertEqual(len(empty),len(ah.LINES)*2)
        self.assertTrue(all(r['status']=='INSUFFICIENT_HISTORY' for r in empty.values()))
        rows=[]
        for i in range(200):
            margin=-1 if i%20<3 else 0 if i%20<9 else 1
            rows.append({'date':(pd.Timestamp('2024-01-01')+pd.Timedelta(days=i)).date().isoformat(),
                'home_goals':max(margin,0),'away_goals':max(-margin,0),
                'goal_margin_distribution':row()['goal_margin_distribution']})
        reports=ah.evaluate_history(pd.DataFrame(rows))
        state=reports['markets'][ah.label('home',0)]
        self.assertEqual(state['development_matches'],130)
        self.assertEqual(state['audit_matches'],70)
        self.assertEqual(state['status'],'RELIABLE_FOR_RANKING')
        self.assertEqual(ah.evaluate_history(pd.DataFrame(rows[:20]))['markets'][ah.label('home',0)]['status'],'INSUFFICIENT_HISTORY')
        for x in rows:x['home_goals']=0;x['away_goals']=5
        self.assertEqual(ah.evaluate_history(pd.DataFrame(rows))['markets'][ah.label('home',0)]['status'],'UNRELIABLE_AUDIT')

    def test_quote_file_binds_event_order_kickoff_and_avoids_duplicates(self):
        with tempfile.TemporaryDirectory() as tmp:
            path=Path(tmp)/'quotes.json';path.write_text(json.dumps([event('bet365')]))
            frame=ah.apply_quote_file(pd.DataFrame([row(offers=[])]),path,NOW)
            self.assertEqual(len(json.loads(frame.iloc[0].asian_handicap_offers)),2)
            path.write_text(json.dumps([event(),event()]))
            with self.assertRaises(ValueError):ah.apply_quote_file(pd.DataFrame([row()]),path,NOW)
            path.write_text('{}')
            with self.assertRaises(ValueError):ah.apply_quote_file(pd.DataFrame([row()]),path,NOW)
            d=event();d['id']='another';path.write_text(json.dumps([d]))
            self.assertEqual(json.loads(ah.apply_quote_file(pd.DataFrame([row(offers=[])]),path,NOW).iloc[0].asian_handicap_offers),[])

    def test_capture_grade_report_and_tamper_end_to_end(self):
        from performance_tracking import capture,review,verified_record,write_json
        from workflow_checks import raw_check,report_check
        from format_football_output import process_conservative_shortlist
        values=pd.DataFrame([row(i,offers=[quote(point=p)]) for i,p in enumerate((0,.25,-.25))])
        picks,decisions,summary=choose(values.to_dict('records'))
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)/'football_output_v2';raw=root/'raw';raw.mkdir(parents=True)
            values.to_csv(raw/'all_leagues_predictions.csv',index=False)
            picks.to_csv(raw/'conservative_bet_shortlist.csv',index=False)
            write_json(raw/'conservative_bet_summary.json',summary)
            write_json(raw/'EPL_goal_market_validation.json',reliability()['Premier League'])
            self.assertEqual(raw_check(root)['selections'],3)
            readable=root/'readable';readable.mkdir()
            self.assertEqual(process_conservative_shortlist(raw,readable),3)
            self.assertIn('Full refund chance',(readable/'conservative_bet_shortlist_report.md').read_text())
            self.assertTrue(capture('a'*40,root=root,captured_at=NOW+timedelta(minutes=1)))
            records=[verified_record('PL',{'id':i+1,'status':'FINISHED','utcDate':value.kickoff_utc,
                'homeTeam':{'name':value.home_team},'awayTeam':{'name':value.away_team},
                'score':{'duration':'REGULAR','fullTime':{'home':1,'away':1}}}) for i,value in values.iterrows()]
            write_json(root/'performance/verified_results.json',{str(x['match_id']):x for x in records})
            with patch('performance_tracking.collect_results',return_value=(records,{})):
                review(root=root,clock=NOW+timedelta(days=2))
            check=report_check(root)
            metrics=json.loads((root/'performance/metrics.json').read_text())
            self.assertEqual(metrics['shortlist']['refunds'],1)
            self.assertEqual(metrics['shortlist']['wins'],1)
            self.assertEqual(metrics['shortlist']['half_wins'],1)
            self.assertEqual(metrics['shortlist']['half_losses'],1)
            self.assertEqual(metrics['shortlist']['graded'],3)
            self.assertAlmostEqual(metrics['shortlist']['flat_stake_roi'],-.1/3,places=6)
            picks.loc[0,'handicap_line']=-1
            picks.to_csv(raw/'conservative_bet_shortlist.csv',index=False)
            with self.assertRaises(ValueError):raw_check(root)

    def test_half_settlements_have_correct_metrics_and_excel_caches(self):
        from performance_tracking import score_shortlist,stats
        from performance_excel import prepared_rows,summarize
        picks,_,_=choose([row()]);base=picks.iloc[0].to_dict()
        base.update(fixture_key='x',snapshot_commit='a'*40,snapshot_captured_utc=NOW.isoformat(),snapshot_generated_utc=NOW.isoformat())
        final={'match_id':1,'home_goals':1,'away_goals':1}
        grades=[]
        for point in (0,.25,-.25):
            value={**base,'market':ah.label('home',point)}
            grades.append(score_shortlist(value,final,'VERIFIED_FINISHED'))
        self.assertEqual([x['status'] for x in grades],['REFUNDED','HALF_WON','HALF_LOST'])
        stats_=stats(grades)
        self.assertEqual(stats_['graded'],3);self.assertEqual(stats_['wins'],1);self.assertEqual(stats_['losses'],1)
        self.assertAlmostEqual(stats_['profit_per_unit_staked'],-.1)
        # prepared_rows requires distinct fixture keys; independent test legs.
        for i,g in enumerate(grades):g['fixture_key']=str(i)
        summary=summarize(prepared_rows(grades))
        self.assertAlmostEqual(summary[7],-.1)
        self.assertAlmostEqual(summary[8],-.1/3)

    def test_handicap_close_is_same_line_and_fair_probability_is_not_invented(self):
        import closing_odds as c
        from performance_tracking import capture, snapshots, write_json
        values=pd.DataFrame([row()]);values['odds_event_id']='fixture-0'
        picks,_,summary=choose(values.to_dict('records'))
        observed=NOW+timedelta(days=1,seconds=-60)
        response=event();response['bookmakers'][0]['key']='pinnacle'
        response['bookmakers'][0]['markets'][0]['last_update']=observed.isoformat()
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);raw=root/'raw';raw.mkdir()
            values.to_csv(raw/'all_leagues_predictions.csv',index=False)
            picks.to_csv(raw/'conservative_bet_shortlist.csv',index=False)
            write_json(raw/'conservative_bet_summary.json',summary)
            capture('f'*40,root=root,captured_at=NOW)
            calls=[]
            def fetcher(api,source,markets):
                calls.append(markets)
                return response
            status=c.collect_once(root,None,observed,fetcher=fetcher)
            self.assertEqual(status['written'],1)
            self.assertIn('alternate_spreads',calls[0])
            _,rows=c.evaluate(root,snapshots(root),observed+timedelta(minutes=2))
            mixed=copy.deepcopy(response)
            mixed['bookmakers'][0]['markets'].append({'key':'double_chance','last_update':observed.isoformat(),
                'outcomes':[{'name':'1X','price':1.35},{'name':'X2','price':2.4},{'name':'12','price':1.12}]})
            normalized=c.normalize(values.iloc[0].to_dict(),mixed,observed)
            self.assertTrue(any(q['selection']=='home_draw' for q in normalized['quotes']))
            self.assertTrue(any(q['selection']==ah.label('home',0) for q in normalized['quotes']))
            close=rows[0]['closing']['pinnacle']
            self.assertEqual(close['status'],'OBSERVED_NEAR_CLOSE')
            self.assertIsNone(close['fair_probability'])
            self.assertIsNone(close['fair_close_ev'])
            self.assertEqual(close['offered_price_clv'],0)
            self.assertEqual(rows[0]['closing']['bet365']['status'],'MISSING_VALID_PRE_KICKOFF_QUOTE')
