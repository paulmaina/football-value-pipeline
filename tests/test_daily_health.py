import copy
from datetime import datetime, timedelta, timezone
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import Mock, patch
from zipfile import ZipFile
import xml.etree.ElementTree as ET

import pandas as pd
from ucl_training import inspect_payload, apply_payload, health, fetch_payload
from quote_policy import is_exchange, load_policy, usable_bookmaker, stake_cost
from conservative_bet_filter import build_conservative_shortlist
from performance_tracking import score_shortlist, capture, review, write_json
from performance_excel import write_workbook, NS
from pipeline_health import write_report
from test_conservative_bet_filter import fixture, NOW
from test_performance_tracking import fixture as forecast_fixture, pick, SHA as COMMIT


def payload():
    clock = NOW
    def match(i, status, delta):
        return {'id': i, 'status': status, 'utcDate': (clock+delta).isoformat(),
            'season': {'startDate': '2026-09-01'}, 'homeTeam': {'name': 'Home'},
            'awayTeam': {'name': 'Away'}, 'score': {'duration': 'REGULAR', 'fullTime': {'home': 2, 'away': 1}}}
    return {'competition': {'code': 'CL'}, 'resultSet': {'count': 2},
            'matches': [match(1, 'FINISHED', timedelta(days=-1)), match(2, 'TIMED', timedelta(days=1))]}


class DailyHealthTests(unittest.TestCase):
    def test_ucl_cache_names_are_utf8_under_windows_default_encoding(self):
        p=payload();p['matches'][0]['homeTeam']['name']='Atlético Madrid'
        p['matches'][0]['awayTeam']['name']='Bodø/Glimt'
        read_text=Path.read_text
        def windows_default(path,encoding=None,errors=None):
            return read_text(path,encoding=encoding or 'cp1252',errors=errors)
        with tempfile.TemporaryDirectory() as tmp:
            repo=Path(tmp)
            apply_payload(repo,p,2026,NOW)
            with patch.object(Path,'read_text',windows_default):
                result=apply_payload(repo,p,2026,NOW)
                status=health(repo,'2026-10-08',NOW)
            self.assertEqual(result['added_matches'],0)
            self.assertEqual(result['corrected_scores'],0)
            self.assertTrue(status['cache_hash_verified'])

    def test_ucl_fallback_warning_explains_domain_validation_failure(self):
        from football_value_pipeline_v2_standalone import FootballDataOrg,LEAGUES
        p=payload();base=p['matches'][0]
        p['matches']=[copy.deepcopy(base) for _ in range(30)]
        for i,m in enumerate(p['matches']):
            m['id']=i+1;m['homeTeam']['name']=f'Home {i}'
            m['utcDate']=(NOW-timedelta(days=1,hours=i)).isoformat()
        p['resultSet']['count']=30
        with tempfile.TemporaryDirectory() as tmp:
            repo=Path(tmp);apply_payload(repo,p,2026,NOW)
            provider=FootballDataOrg('offline-test',cache_dir=repo/'.football_cache')
            reason='Refusing UCL refresh that removes completed matches'
            with patch('ucl_training.fetch_payload',side_effect=ValueError(reason)),self.assertWarnsRegex(RuntimeWarning,reason):
                history=provider.history(LEAGUES['UCL'],1,NOW)
            self.assertEqual(len(history),30)
            self.assertEqual(provider.ucl_refresh_error_reason,reason)

    def test_exchange_offer_exclusion_does_not_change_market_reference(self):
        from football_value_pipeline_v2_standalone import TheOddsAPI
        event = {'id':'e','home_team':'Home','away_team':'Away','commence_time':NOW.isoformat(),
            'bookmakers': []}
        for title, stamp, prices in [('Book A',NOW.isoformat(),[1.7,4,5]),
            ('Matchbook',(NOW+timedelta(minutes=1)).isoformat(),[1.8,3.8,4.8])]:
            event['bookmakers'].append({'title':title,'markets':[{'key':'h2h','last_update':stamp,
                'outcomes':[{'name':name,'price':price} for name,price in zip(('Home','Draw','Away'),prices)]}]})
        data=TheOddsAPI.flatten_odds_event(event)
        self.assertEqual(data['live_best_home_bookmaker'],'Book A')
        self.assertEqual(data['live_best_home_odds'],1.7)
        self.assertEqual(data['live_ref_1x2_bookmaker'],'Matchbook')

    def test_ucl_checks_schedule_and_preserves_previous_good_cache(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp); p = payload()
            first = apply_payload(repo, p, 2026, NOW)
            self.assertEqual(first['added_matches'], 1)
            self.assertEqual(health(repo, '2026-10-08', NOW)['status'], 'CURRENT_WITHIN_PROVIDER_SCHEDULE')
            self.assertEqual(health(repo, '2026-09-10', NOW)['status'], 'MODEL_BEHIND_VERIFIED_SOURCE')
            self.assertEqual(health(repo, '2026-10-08', NOW+timedelta(hours=9))['status'], 'REFRESH_OVERDUE')
            cached = (repo/'.football_cache/fdorg_history_UCL_2026.json').read_bytes()
            bad = copy.deepcopy(p); bad['matches'][0]['score']['fullTime']['home'] = None
            with self.assertRaises(ValueError): apply_payload(repo, bad, 2026, NOW)
            self.assertEqual((repo/'.football_cache/fdorg_history_UCL_2026.json').read_bytes(), cached)
            bad = copy.deepcopy(p); bad['matches'] = bad['matches'][1:]; bad['resultSet']['count'] = 1
            with self.assertRaisesRegex(ValueError, 'removes'): apply_payload(repo, bad, 2026, NOW)
            p['matches'][0]['score']['fullTime']['home'] = 3
            second = apply_payload(repo, p, 2026, NOW)
            self.assertEqual(second['corrected_scores'], 1)
            self.assertEqual(second['added_matches'], 0)
            (repo/'.football_cache/fdorg_history_UCL_2026.json').write_text('{}')
            self.assertEqual(health(repo, '2026-10-08', NOW)['status'], 'DOWNLOAD_NOT_VERIFIED')

    def test_ucl_rejects_malformed_duplicate_wrong_season_and_future_finished(self):
        mutations = [lambda p:p.update(competition={'code': 'PL'}),
            lambda p:p.update(matches=None), lambda p:p['matches'][1].update(id=1),
            lambda p:p['matches'][0]['season'].update(startDate='2025-09-01'),
            lambda p:p['matches'][0].update(utcDate=(NOW+timedelta(days=1)).isoformat()),
            lambda p:p['resultSet'].update(count=3), lambda p:p['matches'][0].update(status='UNKNOWN'),
            lambda p:p['matches'][0]['awayTeam'].update(name='Home')]
        for mutate in mutations:
            with self.subTest(mutation=mutate):
                p = payload(); mutate(p)
                with self.assertRaises(ValueError): inspect_payload(p, 2026, NOW)

    def test_ucl_incomplete_provider_schedule_is_visible(self):
        p = payload(); p['matches'][1]['utcDate'] = (NOW-timedelta(days=2)).isoformat()
        with tempfile.TemporaryDirectory() as tmp:
            report = apply_payload(Path(tmp), p, 2026, NOW)
            self.assertEqual(report['coverage_status'], 'PROVIDER_OVERDUE_RESULTS')
            self.assertEqual(report['overdue_unfinished_match_ids'], [2])

    def test_ucl_fetch_uses_full_season_and_no_secret_logging(self):
        session = Mock(); session.get.return_value.json.return_value = payload()
        self.assertEqual(fetch_payload('private-token', 2026, session), payload())
        kwargs = session.get.call_args.kwargs
        self.assertEqual(kwargs['params'], {'season': 2026})
        self.assertEqual(kwargs['headers'], {'X-Auth-Token': 'private-token'})
        with self.assertRaises(ValueError): fetch_payload('', 2026, session)
        session.get.return_value.raise_for_status.side_effect = RuntimeError('offline')
        with self.assertRaises(RuntimeError): fetch_payload('private-token', 2026, session)

    def test_execution_policy_excludes_exchange_and_enforces_user_allowlist(self):
        for name in ('Matchbook', 'Betfair Exchange', 'betfair_ex_eu', 'Smarkets', 'Betdaq'):
            self.assertTrue(is_exchange(name)); self.assertFalse(usable_bookmaker(name))
        self.assertFalse(is_exchange('Betfair Sportsbook'))
        policy = {'allowed_bookmakers': ['Book A'], 'per_stake_cost_bps': 0}
        self.assertTrue(usable_bookmaker('book a', policy)); self.assertFalse(usable_bookmaker('Book B', policy))
        self.assertFalse(usable_bookmaker(None, policy))
        with tempfile.TemporaryDirectory() as tmp:
            file = Path(tmp)/'policy.json'
            self.assertEqual(load_policy(file)['per_stake_cost_bps'], 0)
            for data in ({'allowed_bookmakers': 'Book A'}, {'allowed_bookmakers': ['']},
                         {'per_stake_cost_bps': -1}, {'per_stake_cost_bps': True}, {'per_stake_cost_bps': float('nan')}):
                file.write_text(json.dumps(data))
                with self.assertRaises(ValueError): load_policy(file)
        for value in ('bad', -1, 2, float('nan')):
            with self.assertRaises(ValueError): stake_cost(value)

    def test_exchange_hard_failure_cannot_enter_provisional_watchlist(self):
        row = fixture()
        for key in ('home', 'away', 'over_1_5', 'btts_yes'): row['best_'+key+'_bookmaker'] = 'Matchbook'
        picks, decisions, _ = build_conservative_shortlist(pd.DataFrame([row]), as_of=NOW)
        self.assertTrue(picks.empty)
        self.assertTrue(decisions[decisions.market.eq('Over 1.5')].rejection_reasons.iloc[0].startswith('bookmaker excluded'))

    def test_costs_apply_before_ev_filter_and_are_frozen(self):
        row = fixture(); row['p_over_1_5'] = .8; row['raw_p_over_1_5'] = .8
        row['market_over_1_5_odds'] = 1.275  # gross 2%, net 1% at 100 bps.
        policy = {'allowed_bookmakers': [], 'per_stake_cost_bps': 100, 'account_availability': 'NOT_VERIFIED'}
        with patch('conservative_bet_filter.load_policy', return_value=policy):
            _, decisions, _ = build_conservative_shortlist(pd.DataFrame([row]), as_of=NOW)
        r = decisions[decisions.market.eq('Over 1.5')].iloc[0]
        self.assertAlmostEqual(r['gross_estimated_ev'], .02)
        self.assertAlmostEqual(r['conservative_estimated_ev'], .01)
        self.assertIn('EV below +1.5%', r['rejection_reasons'])
        self.assertEqual(r['per_stake_cost'], .01)

    def test_net_settlement_costs_match_native_excel_formula_and_cache(self):
        row = fixture(); row.update(fixture_key='k', snapshot_commit=COMMIT,
            snapshot_captured_utc=NOW.isoformat(), market='Over 1.5', offered_decimal_odds=1.3,
            predicted_probability=.85, per_stake_cost=.02, decision='SHORTLISTED')
        final = {'match_id': 1, 'home_goals': 2, 'away_goals': 1}
        won = score_shortlist(row, final, 'VERIFIED_FINISHED')
        self.assertEqual(won['unit_profit'], .28)
        lost = score_shortlist(row, dict(final, home_goals=0, away_goals=0), 'VERIFIED_FINISHED')
        self.assertEqual(lost['unit_profit'], -1.02)
        with tempfile.TemporaryDirectory() as tmp:
            path = write_workbook(Path(tmp), [won, lost | {'fixture_key': 'second'}], [], {})
            with ZipFile(path) as z:
                sheet = ET.fromstring(z.read('xl/worksheets/sheet5.xml'))
                self.assertEqual(sheet.find(f'.//{{{NS}}}c[@r="N6"]/{{{NS}}}v').text, '0.28')
                self.assertIn('-U6', sheet.find(f'.//{{{NS}}}c[@r="N6"]/{{{NS}}}f').text)
                self.assertEqual(sheet.find(f'.//{{{NS}}}c[@r="U6"]/{{{NS}}}v').text, '0.02')
                ledger=ET.fromstring(z.read('xl/worksheets/sheet2.xml'))
                self.assertEqual(ledger.find(f'.//{{{NS}}}c[@r="E10"]/{{{NS}}}v').text, '0.28')

    def test_health_history_is_daily_and_frozen_health_is_hash_bound(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); raw = root/'raw'; raw.mkdir()
            pd.DataFrame([forecast_fixture()]).to_csv(raw/'all_leagues_predictions.csv',index=False)
            pd.DataFrame([pick()]).to_csv(raw/'conservative_bet_shortlist.csv',index=False)
            write_json(raw/'conservative_bet_summary.json',{'generated_at_utc':NOW.isoformat()})
            self.assertTrue(capture(COMMIT, root=root, captured_at=NOW))
            directory = root/'performance/snapshots'/COMMIT[:16]
            meta = json.loads((directory/'metadata.json').read_text())
            self.assertIn('pipeline_health.json', meta['sha256'])
            frozen = (directory/'pipeline_health.json').read_bytes()
            with patch('performance_tracking.collect_results', return_value=([], {})):
                metrics = review(root=root, clock=NOW)
                review(root=root, clock=NOW+timedelta(hours=1))
            history = json.loads((root/'performance/health_history.json').read_text())
            self.assertEqual(len(history['days']), 1)
            self.assertFalse(history['days'][NOW.date().isoformat()]['evidence']['model_improvement_established'])
            self.assertEqual((directory/'pipeline_health.json').read_bytes(), frozen)
            write_report(root, metrics, NOW+timedelta(days=1))
            self.assertEqual(len(json.loads((root/'performance/health_history.json').read_text())['days']), 2)


if __name__ == '__main__': unittest.main()
