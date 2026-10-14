import copy
from datetime import timedelta
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import pandas as pd
import closing_odds as c
from performance_tracking import capture,snapshots,write_json,fixture_key
from test_totals_anchor_experiment import sample
from test_benchmark_forward_experiment import NOW


def payload(row,observed):
    books=[]
    for name in ('pinnacle','1xbet'):
        books.append({'key':name,'title':'1xBet' if name=='1xbet' else 'Pinnacle','markets':[
            {'key':'h2h','last_update':observed.isoformat(),'outcomes':[{'name':row['home_team'],'price':1.6},{'name':'Draw','price':4.0},{'name':row['away_team'],'price':6.0}]},
            {'key':'totals','last_update':observed.isoformat(),'outcomes':[{'name':'Over','point':2.5,'price':1.95},{'name':'Under','point':2.5,'price':1.95}]},
            {'key':'alternate_totals','last_update':observed.isoformat(),'outcomes':[{'name':'Over','point':1.5,'price':1.25},{'name':'Under','point':1.5,'price':4.5},{'name':'Under','point':3.5,'price':1.4},{'name':'Over','point':3.5,'price':3.2}]},
            {'key':'btts','last_update':observed.isoformat(),'outcomes':[{'name':'Yes','price':1.9},{'name':'No','price':2.0}]},
            {'key':'double_chance','last_update':observed.isoformat(),'outcomes':[{'name':'1X','price':1.15},{'name':'X2','price':2.5},{'name':'12','price':1.25}]}]})
    return {'id':row['odds_event_id'],'commence_time':row['kickoff_utc'],'home_team':row['home_team'],'away_team':row['away_team'],'bookmakers':books}


def setup(root,market='Home win'):
    row,_,_=sample();raw=root/'raw';raw.mkdir();pd.DataFrame([row]).to_csv(raw/'all_leagues_predictions.csv',index=False)
    pick={**row,'market':market,'bookmaker':'1xBet','offered_decimal_odds':1.7,'per_stake_cost':0,'decision':'SHORTLISTED'};pd.DataFrame([pick]).to_csv(raw/'conservative_bet_shortlist.csv',index=False);write_json(raw/'conservative_bet_summary.json',{'generated_at_utc':NOW.isoformat()});capture('f'*40,root=root,captured_at=NOW)
    observed=__import__('performance_tracking').utc(row['kickoff_utc'])-timedelta(seconds=60);return row,observed


class ClosingTests(unittest.TestCase):
    def test_quotes_same_book_complete_and_pre_kickoff(self):
        row,_,_=sample();observed=__import__('performance_tracking').utc(row['kickoff_utc'])-timedelta(seconds=60);p=payload(row,observed);d=c.normalize(row,p,observed)
        self.assertEqual(len(d['quotes']),26);home=next(x for x in d['quotes'] if x['bookmaker']=='pinnacle' and x['selection']=='home');self.assertGreater(home['fair_probability'],.5)
        for field,value in [('id','bad'),('home_team','Wrong'),('commence_time',NOW.isoformat())]:
            with self.assertRaises(ValueError):c.normalize(row,{**p,field:value},observed)
        for badclock in (observed-timedelta(seconds=40),observed+timedelta(seconds=60)):
            with self.assertRaises(ValueError):c.normalize(row,p,badclock)
        stale=copy.deepcopy(p)
        for b in stale['bookmakers']:
            for m in b['markets']:m['last_update']=(observed-timedelta(seconds=121)).isoformat()
        self.assertEqual(c.normalize(row,stale,observed)['quotes'],[])
        bad=copy.deepcopy(p);bad['bookmakers'][0]['markets'][0]['outcomes'].pop();bad['bookmakers'][1]['key']='other'
        d=c.normalize(row,bad,observed);self.assertFalse(any(x['selection']=='home' for x in d['quotes']));self.assertTrue(all(x['bookmaker']=='pinnacle' for x in d['quotes']))
        bad=copy.deepcopy(p);bad['bookmakers'][0]['markets'][0]['outcomes'].append(bad['bookmakers'][0]['markets'][0]['outcomes'][0]);self.assertFalse(any(x['selection']=='home' and x['bookmaker']=='pinnacle' for x in c.normalize(row,bad,observed)['quotes']))

    def test_collect_once_cap_and_failure_safety(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);row,observed=setup(root);calls=[]
            def fetch(api,source,markets):calls.append(markets);return payload(row,observed)
            s=c.collect_once(root,None,observed,fetcher=fetch);self.assertEqual(s['written'],1);self.assertEqual(calls,[{'h2h','totals'}]);self.assertEqual(c.collect_once(root,None,observed,fetcher=fetch)['requests'],0)
            pending,_=c.evaluate(root,snapshots(root),observed);self.assertEqual(pending['by_bookmaker']['1xbet']['pending_selections'],1)
            s,rows=c.evaluate(root,snapshots(root),observed+timedelta(days=1));self.assertEqual(s['by_bookmaker']['1xbet']['covered_selections'],1);self.assertAlmostEqual(rows[0]['closing']['1xbet']['offered_price_clv'],1.7/1.6-1);self.assertIsNone(rows[0]['closing']['pinnacle']['offered_price_clv']);self.assertFalse(rows[0]['closing']['pinnacle']['official_close_verified'])
            write_json(root/'closing_odds/request_budget.json',{'date':observed.date().isoformat(),'requests':100});self.assertEqual(c.collect_once(root,None,observed,fetcher=fetch)['requests'],0)
            s=c.review(root,snapshots(root),observed+timedelta(days=1));self.assertTrue(c.validate_report(root));s['observations']=50;write_json(root/'performance/closing_odds/summary.json',s)
            with self.assertRaises(ValueError):c.validate_report(root)
            path=next((root/'closing_odds/observations').glob('*.json'));path.write_text('{}');self.assertEqual(len(c.load_observations(root)[1]),1)
            s,rows=c.evaluate(root,snapshots(root),observed+timedelta(days=1));self.assertEqual(s['by_bookmaker']['1xbet']['missing_selections'],1)
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);row,observed=setup(root,'Over 1.5')
            def failed(*a):raise RuntimeError('secret url must not be logged')
            s=c.collect_once(root,None,observed,fetcher=failed);self.assertEqual(s['written'],0);self.assertEqual(s['errors'][0]['error'],'RuntimeError');self.assertNotIn('secret',json.dumps(s));self.assertEqual(s['daily_requests'],1)

    def test_market_specific_requests_and_dc_fair_probability_fallback(self):
        for market,extra in [('Over 1.5','alternate_totals'),('Both Teams to Score - Yes','btts'),('Double Chance 1X','double_chance')]:
            with tempfile.TemporaryDirectory() as tmp:
                root=Path(tmp);row,observed=setup(root,market);requested=[]
                def fetch(api,source,markets):requested.append(markets);p=payload(row,observed);p['bookmakers'][0]['markets']=[m for m in p['bookmakers'][0]['markets'] if m['key']!='double_chance'];return p
                c.collect_once(root,None,observed,fetcher=fetch);self.assertIn(extra,requested[0]);s,rows=c.evaluate(root,snapshots(root),observed+timedelta(minutes=2))
                if extra=='double_chance':
                    q=rows[0]['closing']['pinnacle'];self.assertEqual(q['devig_method'],'power_1x2_sum_no_synthetic_price');self.assertIsNone(q['decimal_odds']);self.assertIsNotNone(q['fair_close_ev'])

    def test_fetch_is_fresh_and_uses_only_configured_bookmakers(self):
        row,_,_=sample()
        class API:
            def _get_json(self,*args,**kwargs):self.args=args;self.kw=kwargs;return {}
        api=API();c.fetch(api,row,{'h2h','totals'});self.assertFalse(api.kw['allow_stale']);self.assertTrue(api.kw['force_refresh']);self.assertEqual(api.kw['params']['bookmakers'],'pinnacle,1xbet');self.assertNotIn('apiKey',api.kw['params'])
        with self.assertRaises(ValueError):c.fetch(api,{**row,'odds_event_id':'bad/slash'},{'h2h'})

    def test_cli_default_dotenv_and_budget_exit(self):
        class API:
            KEY_ENV_NAMES=('THE_ODDS_API_KEY',)
            def __init__(self,*a,**kw):pass
        with patch('api_key_config.load_api_keys') as load,patch('football_value_pipeline_v2_standalone.TheOddsAPI',API),patch.dict('os.environ',{'THE_ODDS_API_KEY':'dummy'}),patch.object(c,'collect_once',return_value={'requests':1}) as collect:
            self.assertEqual(c.main(['--watch','--max-requests','1']),0);load.assert_called_once_with();collect.assert_called_once()
        with self.assertRaises(SystemExit):c.main(['--max-requests','0'])
