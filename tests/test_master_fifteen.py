"""Fifteen-fixture target, immutable legacy replay and honest frozen evidence."""
import json
import tempfile
from pathlib import Path
from unittest.mock import patch
from zipfile import ZipFile
import pandas as pd
from offline_test_case import OfflineQuotePolicyTestCase
import master_shortlist as master
import master_selection_fifteen as v8
import master_context_review as context
from test_master_market_selection import candidate, NOW
from test_value_per_market import fixture


def evidence():
    kick=NOW+pd.Timedelta(hours=24)
    hours=[dict(time=t.isoformat(),temperature_2m=20.,precipitation=1.,wind_speed_10m=12.)
        for t in pd.date_range(kick.floor('h'),(kick+pd.Timedelta(minutes=105)).floor('h'),freq='h')]
    return dict(observed_at_utc=NOW.isoformat(),
        form={'home':{'all':{'matches':10,'xg_matches':5}},'away':{'all':{'matches':8}}},
        coverage={'form':'recency weighted','xg':'supplied xG','weather':'match-hour forecast',
                  'motivation':'standings context, urgency unknown'},
        h2h=[dict(date=(NOW-pd.Timedelta(days=100)).isoformat(),home_goals=1,away_goals=0)],
        evidence={'weather':dict(hours=hours,complete_match_window=True,observed_at_utc=NOW.isoformat(),
            units={'temperature_2m':'°C','precipitation':'mm','wind_speed_10m':'km/h'},roof_status='unverified'),
            'sources':[dict(url='https://api.open-meteo.com/v1/forecast',status='available',observed_at_utc=NOW.isoformat())],
            'availability':[dict(team='Home FC',players=[{'player':'Player A','status':'doubtful'}])],
            'news':[dict(headline='Provider preview',published_at_utc=NOW.isoformat(),url='https://example.org/preview')],
            'rest_and_travel':{'home':{'days_between_kickoffs':3,'completed_matches_last_14_days':4}}},warnings=[])


def pool(count=18, with_context=True):
    rows=[]; forecasts=[]
    for i in range(count):
        home=f'Club {chr(65+i)} United'
        r=candidate(home=home,market='Home win',price=1.9)
        r['value_market_group']='match_winner'
        rows.extend([r,dict(r)])
        forecasts.append(dict(fixture(),home_team=home,fixture_id='f-'+home,
            model_version='production-model',training_data_status='VERIFIED',training_cutoff='2026-11-01',
            team_research_json=json.dumps(evidence()) if with_context else None))
    return pd.DataFrame(rows),pd.DataFrame(forecasts)


class FifteenMasterTests(OfflineQuotePolicyTestCase):
    def test_fifteen_distinct_matches_and_v7_keeps_ten(self):
        d,p=pool()
        top=master.build(d,p,master.VERSION_CONTEXT)
        self.assertEqual(len(top),15)
        self.assertEqual(top.home_team.nunique(),15)
        self.assertEqual(top.master_rank.tolist(),list(range(1,16)))
        self.assertTrue(top.master_suggested_stake.eq(0).all())
        info=master.summary(top)
        self.assertEqual(info['target_size'],15)
        self.assertEqual(info['shortfall'],0)
        self.assertEqual(info['context_status_counts'],{'PARTIAL':15})
        old=master.build(d,p,master.VERSION_NO_TOTALS)
        self.assertEqual(len(old),10)
        self.assertEqual(top.home_team[:10].tolist(),old.home_team.tolist())
        for col in ['master_profit_probability','master_expected_return','master_no_loss_probability']:
            self.assertEqual(top[col][:10].tolist(),old[col].tolist())
        # Weather/news coverage cannot manufacture a probability change or a missing-data advantage.
        p['team_research_json']=None
        changed=master.build(d,p,master.VERSION_CONTEXT)
        self.assertEqual(top.home_team.tolist(),changed.home_team.tolist())
        self.assertEqual(top.master_profit_probability.tolist(),changed.master_profit_probability.tolist())

    def test_shortfall_empty_and_source_exclusions_are_preserved(self):
        d,p=pool(3)
        top=master.build(d,p,master.VERSION_CONTEXT)
        self.assertEqual(master.summary(top)['shortfall'],12)
        for market in ['Over 1.5','Double Chance 12']:
            with self.subTest(market=market):
                d['market']=market;d['market_to_bet']=market
                d['value_market_group']='over_1_5' if market=='Over 1.5' else 'double_chance'
                empty=master.build(d,p,master.VERSION_CONTEXT)
                self.assertTrue(empty.empty)
                self.assertEqual(master.summary(empty)['version'],v8.VERSION)
                self.assertEqual(master.summary(empty)['shortfall'],15)
        empty=v8.select(v8.evaluate(None,None))
        self.assertTrue(empty.empty)
        self.assertEqual(list(empty.columns),master.COLUMNS_CONTEXT)

    def test_review_contains_training_weather_news_form_and_missing_factors(self):
        d,p=pool(1)
        a=v8.evaluate(d,p).iloc[0]
        saved=json.loads(a.master_context_json)
        self.assertEqual(saved['weather']['hours'][0]['temperature_2m'],20.)
        self.assertEqual(saved['form']['home']['all']['matches'],10)
        self.assertEqual(saved['training']['training_data_status'],'VERIFIED')
        self.assertEqual(saved['rest_and_travel']['home']['days_between_kickoffs'],3)
        self.assertEqual(saved['team_news']['availability'][0]['players'][0]['status'],'doubtful')
        self.assertEqual(len(saved['other_context']['h2h']),1)
        self.assertIn('lineups',saved['missing'])
        self.assertIn('no unvalidated numerical adjustment',saved['influence'])
        self.assertIn('context review: PARTIAL',a.master_coverage_warning)

    def test_future_research_or_source_is_not_used_and_stale_is_flagged(self):
        _,p=pool(1)
        row=p.iloc[0].to_dict()
        for mode in ['observation','source']:
            e=evidence();future=(NOW+pd.Timedelta(seconds=1)).isoformat()
            if mode=='observation':e['observed_at_utc']=future
            else:e['evidence']['sources'][0]['observed_at_utc']=future
            with self.subTest(mode=mode):
                result=context.review(dict(row,team_research_json=json.dumps(e)),NOW)
                self.assertEqual(result['master_context_status'],'INVALID_TIMING')
                self.assertEqual(json.loads(result['master_context_json'])['weather'],{})
                self.assertEqual(json.loads(result['master_context_json'])['form'],{})
        e=evidence();e['observed_at_utc']=(NOW-pd.Timedelta(hours=25)).isoformat()
        self.assertEqual(context.review(dict(row,team_research_json=json.dumps(e)),NOW)['master_context_status'],'STALE_RECHECK')
        for invalid in [None,'bad-json','[]']:
            with self.subTest(invalid=invalid):
                self.assertEqual(context.review(dict(row,team_research_json=invalid),NOW)['master_context_status'],'UNAVAILABLE')

    def test_future_weather_incomplete_hours_and_future_news_cannot_claim_coverage(self):
        _,p=pool(1);row=p.iloc[0].to_dict()
        for mode in ['future','hours','units']:
            e=evidence()
            if mode=='future':e['evidence']['weather']['observed_at_utc']=(NOW+pd.Timedelta(seconds=1)).isoformat()
            if mode=='hours':e['evidence']['weather']['hours'].pop()
            if mode=='units':e['evidence']['weather']['units']['wind_speed_10m']='mph'
            e['evidence']['news'].append(dict(headline='future result',published_at_utc=(NOW+pd.Timedelta(days=2)).isoformat()))
            e['h2h'].append(dict(date=(NOW+pd.Timedelta(days=2)).isoformat(),home_goals=5))
            with self.subTest(mode=mode):
                r=context.review(dict(row,team_research_json=json.dumps(e)),NOW)
                self.assertIn('weather',r['master_context_missing'])
                saved=json.loads(r['master_context_json'])
                self.assertEqual(len(saved['team_news']['news_leads']),1)
                self.assertEqual(len(saved['other_context']['h2h']),1)
        row['training_cutoff']=(NOW+pd.Timedelta(days=1)).isoformat()
        self.assertIn('training cutoff not before',context.review(row,NOW)['master_training_summary'])
        row['training_data_status']=None;row['training_cutoff']=None
        self.assertIn('status not recorded',context.review(row,NOW)['master_training_summary'])
        self.assertIsNone(context.clean(float('nan')))
        self.assertIsNone(context.clean(float('inf')))

    def test_write_replay_readable_and_excel_preserve_all_context_fields(self):
        from format_football_output import master_section,write_predictions_workbook
        d,p=pool(16);info={'generated_at_utc':NOW.isoformat()}
        with tempfile.TemporaryDirectory() as tmp,patch('team_research.FreeSources.get',side_effect=AssertionError('Replay must be offline')):
            root=Path(tmp);frame=master.write(d,root,info,p)
            expected=master.build(d,p,master.VERSION_CONTEXT)
            self.assertTrue(master.matches(frame,expected))
            self.assertTrue(master.matches(pd.read_csv(root/master.FILE),expected))
            for col in context.COLUMNS:
                altered=frame.copy();altered.loc[0,col]='tampered'
                self.assertFalse(master.matches(altered,expected))
            report=' '.join(master_section(info,root,root))
            self.assertIn('15 profit-first',report)
            readable=pd.read_csv(root/'master_shortlist_readable.csv',dtype=str,keep_default_na=False)
            self.assertEqual(len(readable),15)
            self.assertIn('Match-window weather',readable)
            self.assertIn('Training data review',readable)
            path=root/'league_predictions.xlsx'
            write_predictions_workbook([],path,[('Master shortlist',readable,'No picks')])
            with ZipFile(path) as archive:
                xml=archive.read('xl/worksheets/sheet1.xml').decode()
                self.assertIn('Match-window weather',xml)
                self.assertIn('Training data review',xml)
