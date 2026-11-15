"""Cached training, free research, new odds bounds and complete DC settlement."""
from datetime import timedelta
import json
from pathlib import Path
import tempfile
from unittest.mock import patch

import numpy as np
import pandas as pd

from offline_test_case import OfflineQuotePolicyTestCase
from test_team_research_profit import researched
from test_value_per_market import run, V2
from test_price_edge_shortlist import NOW, FRESH, quote, offer
from test_europa_production import snapshot, NOW as EURO_NOW
import europa_training as et
import profit_shortlist as ps
import price_edge_cagey_shortlist as v28
import team_research as tr
from master_switch import switched

SETTINGS = {**V2, 'value_rule': ps.RULE_V2}


def row_with_evidence(**kwargs):
    row = researched(**kwargs)
    evidence = json.loads(row['team_research_json'])
    evidence['margin_distribution'] = {'-1': .4, '0': .25, '1': .35}
    row['team_research_json'] = json.dumps(evidence)
    row['price_edge_quotes'] = json.dumps(json.loads(row['price_edge_quotes']) + [
        quote('h2h', {'home': 1.8, 'draw': 4., 'away': 1.9}, book='1xBet'),
        quote('double_chance', {'home_draw': 1.5, 'draw_away': 1.6, 'home_away': 1.7}, book='1xBet')])
    return row


class LocalResearchSelectionTests(OfflineQuotePolicyTestCase):
    def test_exact_price_bounds_and_legacy_replay_bounds(self):
        row = researched()
        for price, eligible in [(1., False), (1.15, False), (1.1501, True), (2., True), (2.0001, False), (3., False)]:
            item = {'market': 'Home win', 'handicap_side': 'home', 'handicap_line': -.5,
                    'offered_decimal_odds': price, 'offered_last_update_utc': NOW.isoformat()}
            with self.subTest(price=price):
                out = ps.annotate(row, dict(item), NOW, 0, rule=ps.RULE_V2)
                self.assertEqual(out['decision'] == 'ELIGIBLE', eligible)
        old = ps.annotate(row, dict(item, offered_decimal_odds=2.5), NOW, 0, rule=ps.RULE)
        self.assertEqual(old['decision'], 'ELIGIBLE')

    def test_dc12_is_quoted_and_ranked_from_non_draw_mass(self):
        row = row_with_evidence()
        selected, decisions, summary = run(row, settings=SETTINGS)
        pick = selected[selected.value_market_group.eq('double_chance')].iloc[0]
        self.assertEqual(pick.market, 'Double Chance 12')
        self.assertEqual(pick.bookmaker, '1xBet')
        self.assertAlmostEqual(pick.profit_probability, .75)
        self.assertTrue(pd.isna(pick.handicap_line))
        self.assertAlmostEqual(pick.research_p_loss, .25)
        self.assertEqual(summary['value_rule'], ps.RULE_V2)
        self.assertEqual(summary['min_offered_odds_exclusive'], 1.15)
        self.assertEqual(summary['max_offered_odds'], 2.)
        from staking import conservative_settlement
        self.assertAlmostEqual(conservative_settlement(pick)['full_win'], .75)
        from performance_tracking import result_for_market
        self.assertTrue(result_for_market('Double Chance 12', 1, 0))
        self.assertFalse(result_for_market('Double Chance 12', 1, 1))
        old, _, _ = run(row, settings={**SETTINGS, 'value_rule': ps.RULE})
        self.assertNotIn('Double Chance 12', old.market.tolist())

    def test_safest_actual_handicap_is_chosen_after_price_filter(self):
        row = row_with_evidence()
        offers = [offer('home', .25, 1.45), offer('home', 1., 1.30),
                  offer('home', 1.5, 1.16), offer('home', 2., 1.10)]
        row['asian_handicap_offers'] = json.dumps(offers)
        selected, decisions, _ = run(row, settings=SETTINGS)
        ah = selected[selected.value_market_group.eq('asian_handicap')]
        self.assertEqual(len(ah), 1)
        self.assertEqual(ah.iloc[0].handicap_line, 1.5)
        self.assertTrue(((selected.offered_decimal_odds > 1.15) & (selected.offered_decimal_odds <= 2)).all())

    def test_dc12_future_or_missing_quotes_are_not_synthesized(self):
        row = row_with_evidence()
        quotes = json.loads(row['price_edge_quotes'])
        for q in quotes:
            if q['market'] == 'double_chance':
                q['last_update_utc'] = (NOW+pd.Timedelta(seconds=1)).isoformat()
        row['price_edge_quotes'] = json.dumps(quotes)
        selected, decisions, _ = run(row, settings=SETTINGS)
        self.assertNotIn('Double Chance 12', selected.market.tolist())
        self.assertTrue(decisions.loc[decisions.market.eq('Double Chance 12'), 'decision'].eq('REJECTED').all())
        row['price_edge_quotes'] = json.dumps([q for q in quotes if q['market'] != 'double_chance'])
        _, decisions, _ = run(row, settings=SETTINGS)
        self.assertFalse(decisions.market.eq('Double Chance 12').any())

    def test_dc12_is_not_silently_skipped_by_forward_tracking(self):
        import price_edge_tracking as tracking
        from test_price_edge_tracking import pick, observation, KICK, CLOCK, CAPTURED
        row = pick(market='Double Chance 12', price=1.7, snapshot_captured_utc=CAPTURED, per_stake_cost=.02)
        obs = observation(quotes=[{'bookmaker': 'pinnacle', 'selection': key, 'fair_probability': p}
                                 for key, p in [('home', .4), ('draw', .3), ('away', .3)]])
        final = {'league_code': 'PL', 'kickoff_utc': KICK.isoformat(), 'home_team': row['home_team'],
                 'away_team': row['away_team'], 'home_goals': 1, 'away_goals': 0}
        grade = tracking.grade([row], [obs], [final], CLOCK)
        self.assertEqual(len(grade), 1)
        self.assertAlmostEqual(grade.iloc[0].clv, 1.7*.7-1)
        self.assertAlmostEqual(grade.iloc[0].unit_profit, .68)
        self.assertEqual(grade.iloc[0].result_status, 'WON')
        final['away_goals'] = 1
        self.assertAlmostEqual(tracking.grade([row], [], [final], CLOCK).iloc[0].unit_profit, -1.02)
        self.assertIsNone(tracking.close_dc12_share([{'bookmaker': 'pinnacle', 'selection': 'home', 'fair_probability': .4}]))

    @switched('old')  # pre-release behaviour: the rollback state (master_shortlist_config.json live "old")
    def test_replay_raw_readable_and_master_pool_remain_bound(self):
        from workflow_checks import raw_check
        from pipeline_health import write_generation_metadata
        from format_football_output import process_conservative_shortlist
        import master_shortlist as ms
        row = row_with_evidence()
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); raw = root/'raw'; raw.mkdir(); readable = root/'readable'; readable.mkdir()
            selected, decisions, summary = run(row, settings=SETTINGS)
            pd.DataFrame([row]).to_csv(raw/'all_leagues_predictions.csv', index=False)
            selected.to_csv(raw/'conservative_bet_shortlist.csv', index=False)
            selected.to_csv(raw/'conservative_strict_qualifiers.csv', index=False)
            decisions.to_csv(raw/'conservative_bet_rejections.csv', index=False)
            v28.cagey_tier_list(decisions).to_csv(raw/v28.TIER_FILE, index=False)
            master = ms.refresh(decisions, raw, summary, pd.DataFrame([row]))
            (raw/'conservative_bet_summary.json').write_text(json.dumps(summary), encoding='utf-8')
            write_generation_metadata(raw, summary)
            with patch('requests.sessions.Session.request', side_effect=AssertionError('replay must be offline')):
                self.assertEqual(raw_check(root)['selections'], len(selected))
                replay, _, _ = run(row, settings={k: summary.get(k) for k in v28.REPLAY_SETTINGS})
            self.assertEqual(replay.market.tolist(), selected.market.tolist())
            process_conservative_shortlist(raw, readable)
            output = pd.read_csv(readable/'conservative_bet_shortlist_readable.csv')
            self.assertIn('Double Chance 12', output['Market to bet'].tolist())
            self.assertIn('Chance of positive return', output)
            if (raw/'master_shortlist.csv').exists():
                self.assertNotIn('Double Chance 12', pd.read_csv(raw/'master_shortlist.csv').market.tolist())


class CachedTrainingResearchTests(OfflineQuotePolicyTestCase):
    def test_failed_europa_refresh_remains_available_with_provenance(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp)/'europa'/'training.json'; path.parent.mkdir()
            old = snapshot(); old['verified_at_utc'] = (EURO_NOW-timedelta(days=3)).isoformat()
            encoded = json.dumps(old); path.write_text(encoded)
            histories = {}
            with patch.object(et, 'refresh', side_effect=ValueError('unverified new source row')) as refresh:
                with self.assertWarns(RuntimeWarning):
                    keys, status = et.forecast_availability(['EPL', 'UCL', 'UEL'], tmp, EURO_NOW, histories=histories)
            self.assertEqual(keys, ['EPL', 'UCL', 'UEL'])
            self.assertEqual(status['excluded_leagues'], {})
            self.assertIn('UEL', status['training_warnings'])
            self.assertEqual(histories['UEL'].attrs['training_verified_at_utc'], old['verified_at_utc'])
            self.assertEqual(path.read_text(), encoded)
            refresh.assert_called_once()
            from football_value_pipeline_v2_standalone import FootballValuePipelineV2, LEAGUES
            pipe = FootballValuePipelineV2(cache_dir=tmp)
            pipe._europa_preflight_history = histories['UEL']
            with patch.object(et, 'load', side_effect=AssertionError('preflight must be reused')):
                self.assertEqual(len(pipe._history_for_league(LEAGUES['UEL'], EURO_NOW)), 30)

    def test_europa_fallback_age_boundary_and_expired_snapshot_exclusion(self):
        for age in (et.MAX_FALLBACK_AGE, et.MAX_FALLBACK_AGE+timedelta(seconds=1)):
            with self.subTest(age=age), tempfile.TemporaryDirectory() as tmp:
                old = snapshot()
                old['verified_at_utc'] = (EURO_NOW-age).isoformat()
                path = Path(tmp)/'europa/training.json'; path.parent.mkdir()
                encoded = json.dumps(old); path.write_text(encoded)
                failure = ValueError('refresh sources disagree')
                with patch.object(et, 'refresh', side_effect=failure):
                    if age <= et.MAX_FALLBACK_AGE:
                        with self.assertWarns(RuntimeWarning):
                            keys, status = et.forecast_availability(['EPL', 'UEL'], tmp, EURO_NOW)
                        self.assertEqual(keys, ['EPL', 'UEL'])
                        self.assertEqual(status['training_warnings']['UEL']['verified_at_utc'], old['verified_at_utc'])
                    else:
                        keys, status = et.forecast_availability(['EPL', 'UEL'], tmp, EURO_NOW)
                        self.assertEqual(keys, ['EPL'])
                        self.assertEqual(status['excluded_leagues']['UEL']['status'], 'TRAINING_UNVERIFIED')
                        self.assertEqual(status['excluded_leagues']['UEL']['reason'], str(failure))
                        with self.assertRaises(ValueError) as raised:
                            et.load(tmp, EURO_NOW)
                        self.assertIs(raised.exception, failure)
                self.assertEqual(path.read_text(), encoded)

    def test_corrupt_or_future_verified_cache_does_not_bypass_exclusion(self):
        for issue in ('future', 'score', 'duplicate', 'self_match', 'missing_team'):
            with self.subTest(issue=issue), tempfile.TemporaryDirectory() as tmp:
                old = snapshot()
                old['verified_at_utc'] = (EURO_NOW-timedelta(days=3)).isoformat()
                if issue == 'future': old['verified_at_utc'] = (EURO_NOW+timedelta(hours=1)).isoformat()
                if issue == 'score': old['matches'][0]['regulation'] = [True, 0]
                if issue == 'duplicate': old['matches'].append(old['matches'][0])
                if issue == 'self_match': old['matches'][0]['away'] = old['matches'][0]['home']
                if issue == 'missing_team': old['matches'][0]['home'] = ''
                path = Path(tmp)/'europa'/'training.json'; path.parent.mkdir(); path.write_text(json.dumps(old))
                with patch.object(et, 'refresh', side_effect=ValueError('sources unavailable')):
                    keys, status = et.forecast_availability(['EPL', 'UEL'], tmp, EURO_NOW)
                self.assertEqual(keys, ['EPL'])
                self.assertEqual(status['excluded_leagues']['UEL']['status'], 'TRAINING_UNVERIFIED')

    def test_ucl_can_train_from_local_cache_without_api_key(self):
        from football_value_pipeline_v2_standalone import FootballValuePipelineV2, LEAGUES
        from test_daily_health import payload
        base = payload()['matches'][0]
        matches = []
        for i in range(30):
            match = json.loads(json.dumps(base))
            match['id'] = i+1
            match['utcDate'] = (NOW-timedelta(days=i+1)).isoformat()
            match['season'] = {'startDate': '2026-07-01'}
            matches.append(match)
        data = {'competition': {'code': 'CL'}, 'resultSet': {'count': 30}, 'matches': matches}
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp)/'fdorg_history_UCL_2026.json'; path.write_text(json.dumps(data))
            pipe = FootballValuePipelineV2(cache_dir=tmp)
            with patch('requests.sessions.Session.request', side_effect=AssertionError('cached UCL must not need internet')):
                frame = pipe._history_for_league(LEAGUES['UCL'], NOW.to_pydatetime())
            self.assertEqual(len(frame), 30)
            self.assertTrue(pipe.football_data_org.cache_only)
            self.assertEqual(frame.history_source.unique().tolist(), ['football-data.org'])

    def test_online_generation_default_and_explicit_cached_research_mode(self):
        from football_value_pipeline_v2_standalone import build_parser
        self.assertTrue(build_parser().parse_args([]).research_free_sources)
        self.assertFalse(build_parser().parse_args(['--no-research-free-sources']).research_free_sources)

    def test_all_leagues_use_local_form_and_verified_internet_form_before_cutoff(self):
        from league_registry import REGISTRY
        for league in REGISTRY:
            row = researched()
            row.update(league=league.name, training_data_status='LIVE_REFRESH_FAILED_USING_VERIFIED_CACHE',
                       training_cutoff='2026-10-01', training_refresh_warning='refresh unavailable')
            side = row['home_team']; other = row['away_team']
            past = [{'date': (NOW-pd.Timedelta(days=i+1)).isoformat(), 'home': side, 'away': other,
                     'home_goals': 3, 'away_goals': 0} for i in range(6)]
            evidence = {'sources': [{'observed_at_utc': NOW.isoformat()}], 'recent': {'home': past, 'away': past}}
            with self.subTest(league=league.key), tempfile.TemporaryDirectory() as tmp:
                with patch.object(tr, 'collect_fixture', return_value=evidence):
                    out = tr.enrich(pd.DataFrame([row]), tmp, fetch=True, clock=lambda: NOW.to_pydatetime())
                saved = json.loads(out.iloc[0].team_research_json)
                self.assertNotEqual(saved['base_rates'], saved['goal_rates'])
                self.assertIn('using verified local history', '; '.join(saved['warnings']))
                self.assertAlmostEqual(sum(out.iloc[0]['research_p_'+k] for k in ('home', 'draw', 'away')), 1.)
