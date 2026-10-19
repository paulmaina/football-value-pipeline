"""Main-line O1.5 coverage and atomic merging without extra provider calls."""
import copy
from datetime import timedelta
from unittest.mock import Mock, patch

import pandas as pd

from offline_test_case import OfflineQuotePolicyTestCase
from football_value_pipeline_v2_standalone import (
    DixonColesModel, FootballValuePipelineV2, LEAGUES, TheOddsAPI,
)
from test_conservative_bet_filter import NOW
from test_recency_experiment import history


def event(price=1.63, opposite=2.49, name='1xBet', stamp=None, key='totals'):
    return {'id': 'event0', 'home_team': 'Home0', 'away_team': 'Away0',
            'commence_time': (NOW + timedelta(hours=12)).isoformat(),
            'bookmakers': [{'title': name, 'markets': [{
                'key': key, 'last_update': stamp or NOW.isoformat(), 'outcomes': [
                    {'name': 'Over', 'point': 1.5, 'price': price},
                    {'name': 'Under', 'point': 1.5, 'price': opposite},
                ]}]}]}


def primary(response):
    return TheOddsAPI.flatten_odds_event(response, as_of=NOW)['_main_over_1_5_offers']


class MainTotalsTests(OfflineQuotePolicyTestCase):
    def merged(self, response, offers):
        api = TheOddsAPI.__new__(TheOddsAPI)
        api.regions = 'eu'; api.api_key = 'fake'; api.force_refresh = False
        with patch.object(api, '_get_json', return_value=response) as request, patch(
                'football_value_pipeline_v2_standalone.datetime') as clock:
            clock.now.return_value = NOW
            result = api.extra_markets_for_event(
                LEAGUES['EPL'], 'event0', main_over_1_5_offers=offers)
        self.assertEqual(request.call_count, 1)
        self.assertEqual(request.call_args.kwargs['params']['markets'],
                         'alternate_totals,btts,double_chance')
        return result

    def test_exact_main_line_retains_pair_without_relabelling_as_25(self):
        flat = TheOddsAPI.flatten_odds_event(event(), as_of=NOW)
        self.assertEqual(flat['_main_over_1_5_offers'], [(NOW.isoformat(), '1xBet', 1.63, 2.49)])
        self.assertIsNone(flat['live_ref_over_2_5_odds'])
        result = self.merged({'id': 'event0', 'bookmakers': []}, primary(event()))
        self.assertEqual(result['market_over_1_5_odds'], 1.63)
        self.assertEqual(result['market_reference_over_1_5_opposite_odds'], 2.49)
        self.assertEqual(result['market_best_over_1_5_last_update_utc'], NOW.isoformat())

    def test_invalid_incomplete_ambiguous_or_stale_main_lines_are_rejected(self):
        valid = event()
        variants = []
        for outcomes in (None, 42, {}, [],
                         [{'name': 'Over', 'point': 1.5, 'price': 1.63}]):
            bad = copy.deepcopy(valid)
            bad['bookmakers'][0]['markets'][0]['outcomes'] = outcomes
            variants.append(bad)
        for change in ({'point': 2.5}, {'price': 1}, {'price': float('nan')}, {'price': 10}):
            bad = copy.deepcopy(valid)
            bad['bookmakers'][0]['markets'][0]['outcomes'][1].update(change)
            variants.append(bad)
        bad = copy.deepcopy(valid)
        bad['bookmakers'][0]['markets'][0]['outcomes'].append(
            {'name': 'Over', 'point': 1.5, 'price': 1.7})
        variants.append(bad)
        for stamp in ('bad-time', '', (NOW-timedelta(hours=25)).isoformat(),
                      (NOW+timedelta(hours=1)).isoformat()):
            bad = copy.deepcopy(valid)
            bad['bookmakers'][0]['markets'][0]['last_update'] = stamp
            variants.append(bad)
        for bad in variants:
            with self.subTest(bad=bad):
                self.assertEqual(primary(bad), [])

    def test_main_and_alternate_merge_best_allowed_book_and_reference_atomically(self):
        old = (NOW-timedelta(minutes=1)).isoformat()
        offers = primary(event(stamp=old))
        response = event(1.60, 2.44, 'Pinnacle', key='alternate_totals')
        # An inaccessible bookmaker cannot supply the executable best price.
        response['bookmakers'] += event(1.70, 2.30, 'Other', key='alternate_totals')['bookmakers']
        with patch('quote_policy.load_policy', return_value={
                'allowed_bookmakers': ['1xBet', 'Pinnacle', 'bet365']}):
            result = self.merged(response, offers)
        self.assertEqual(result['market_over_1_5_odds'], 1.63)
        self.assertEqual(result['best_over_1_5_bookmaker'], '1xBet')
        self.assertEqual(result['market_best_over_1_5_last_update_utc'], old)
        self.assertEqual(result['market_over_1_5_bookmakers'], 2)
        self.assertEqual(result['market_reference_over_1_5_last_update_utc'], NOW.isoformat())
        self.assertEqual(result['market_reference_over_1_5_odds'], 1.60)
        self.assertEqual(result['market_reference_over_1_5_opposite_odds'], 2.44)

    def test_newer_same_book_replaces_stale_favourable_price_and_counts_once(self):
        old = (NOW-timedelta(minutes=1)).isoformat()
        result = self.merged(event(1.60, 2.44, '1XBET', key='alternate_totals'),
                             primary(event(stamp=old)))
        self.assertEqual(result['market_over_1_5_odds'], 1.60)
        self.assertEqual(result['market_reference_over_1_5_opposite_odds'], 2.44)
        self.assertEqual(result['market_over_1_5_bookmakers'], 1)
        self.assertEqual(result['market_best_over_1_5_last_update_utc'], NOW.isoformat())
        result = self.merged(event(1.70, 2.30, stamp=(NOW-timedelta(hours=25)).isoformat(),
                                   key='alternate_totals'), primary(event()))
        self.assertEqual(result['market_over_1_5_odds'], 1.63)
        self.assertEqual(TheOddsAPI._goal_quote_fields('over_1_5', [('', 'Book', 1.63, 2.49)]), {})

    def test_primary_quotes_flow_through_live_join_and_prediction(self):
        data = history()
        model = DixonColesModel().fit(data)
        home, away = str(data.iloc[0]['HomeTeam']), str(data.iloc[0]['AwayTeam'])
        response = event()
        response.update(home_team=home, away_team=away)
        flat = TheOddsAPI.flatten_odds_event(response, as_of=NOW)
        pipeline = FootballValuePipelineV2.__new__(FootballValuePipelineV2)
        pipeline.market_weight = 0.5; pipeline.devig_method = 'power'
        pipeline.odds_regions = 'eu'; pipeline.lookahead_days = 7; pipeline.live_odds = True
        pipeline.odds_api = Mock()
        pipeline.odds_api.odds.return_value = pd.DataFrame([flat])
        fixtures = pd.DataFrame([{'HomeTeam': home, 'AwayTeam': away,
            'Date': pd.Timestamp(NOW).tz_localize(None).normalize(),
            'kickoff_utc': response['commence_time']}])
        joined = pipeline._attach_live_odds(fixtures, LEAGUES['EPL'], NOW)
        self.assertEqual(joined.iloc[0]['_main_over_1_5_offers'], primary(event()))
        with patch('football_value_pipeline_v2_standalone.datetime') as clock:
            clock.now.return_value = NOW
            baseline, _ = pipeline._predict_row(model, fixtures.iloc[0])
            pred, _ = pipeline._predict_row(model, joined.iloc[0])
        self.assertEqual(pred['market_over_1_5_odds'], 1.63)
        self.assertEqual(pred['p_over_1_5'], baseline['p_over_1_5'])
        self.assertNotIn('_main_over_1_5_offers', pred)

    def test_main_quotes_expire_before_prediction(self):
        data = history()
        model = DixonColesModel().fit(data)
        pipeline = FootballValuePipelineV2.__new__(FootballValuePipelineV2)
        pipeline.market_weight = 0; pipeline.devig_method = 'power'
        row = pd.Series({'HomeTeam': data.iloc[0]['HomeTeam'], 'AwayTeam': data.iloc[0]['AwayTeam'],
                         '_main_over_1_5_offers': primary(event())})
        with patch('football_value_pipeline_v2_standalone.datetime') as clock:
            clock.now.return_value = NOW+timedelta(hours=25)
            pred, _ = pipeline._predict_row(model, row)
        self.assertNotIn('market_over_1_5_odds', pred)
