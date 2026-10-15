"""Reproductions for ingestion and quote-parser defects found in project audit."""
from offline_test_case import OfflineQuotePolicyTestCase
import copy
from datetime import datetime, timezone
import tempfile
import unittest
from unittest.mock import patch

import numpy as np
import pandas as pd

from football_value_pipeline_v2_standalone import (
    FootballDataUK, DixonColesModel, TheOddsAPI, LEAGUES,
    validated_completed_scores,
)


NOW = datetime(2026, 10, 15, tzinfo=timezone.utc)


def history():
    return pd.DataFrame({'Date': pd.date_range('2026-09-01', periods=30),
                         'HomeTeam': ['A']*30, 'AwayTeam': ['B']*30,
                         'FTHG': [2.0]*30, 'FTAG': [1.0]*30})


def event():
    return {'id': 'e', 'home_team': 'A', 'away_team': 'B',
        'commence_time': '2026-10-17T12:00:00Z', 'bookmakers': [
        {'title': 'Book A', 'key': 'book_a', 'markets': [
            {'key': 'h2h', 'last_update': NOW.isoformat(), 'outcomes': [
                {'name': 'A', 'price': 1.6}, {'name': 'Draw', 'price': 4.5}, {'name': 'B', 'price': 6.5}]},
            {'key': 'totals', 'last_update': NOW.isoformat(), 'outcomes': [
                {'name': 'Over', 'point': 2.5, 'price': 1.9}, {'name': 'Under', 'point': 2.5, 'price': 1.9}]}]}]}


class TrainingInputTests(OfflineQuotePolicyTestCase):
    def test_source_does_not_truncate_fractional_or_accept_negative_completed_scores(self):
        for value in (1.8, -1, 31, float('inf')):
            with self.subTest(value=value), tempfile.TemporaryDirectory() as tmp:
                provider = FootballDataUK(cache_dir=tmp)
                data = history(); data.loc[0, 'FTHG'] = value
                with patch.object(provider, 'season', return_value=data), self.assertRaisesRegex(ValueError, 'Invalid completed goals'):
                    provider.history(LEAGUES['EPL'], 1, NOW)

    def test_direct_model_rejects_malformed_scores_before_optimizer_runs(self):
        for value in (1.8, -1, 31, float('inf')):
            data = history(); data.loc[0, 'FTAG'] = value
            with self.subTest(value=value), patch('football_value_pipeline_v2_standalone.minimize') as optimizer:
                with self.assertRaisesRegex(ValueError, 'Invalid completed goals'):
                    DixonColesModel().fit(data)
                optimizer.assert_not_called()
        data = history().astype({'FTHG': object}); data.loc[0, 'FTHG'] = True
        with self.assertRaisesRegex(ValueError, 'Invalid completed goals'):
            validated_completed_scores(data)

    def test_integer_floats_remain_valid_and_inputs_are_not_mutated(self):
        data = history(); before = data.copy(deep=True)
        result = validated_completed_scores(data)
        self.assertTrue(pd.api.types.is_integer_dtype(result.FTHG))
        pd.testing.assert_frame_equal(data, before)

    def test_duplicate_completed_source_fixture_cannot_double_training_weight(self):
        with tempfile.TemporaryDirectory() as tmp:
            provider = FootballDataUK(cache_dir=tmp)
            data = pd.concat([history(), history().iloc[:1]], ignore_index=True)
            with patch.object(provider, 'season', return_value=data), self.assertRaisesRegex(ValueError, 'duplicate completed training fixture'):
                provider.history(LEAGUES['EPL'], 1, NOW)


class QuoteInputTests(OfflineQuotePolicyTestCase):
    def test_duplicate_winner_or_total_outcomes_are_rejected_independently(self):
        self.assertEqual(TheOddsAPI.flatten_odds_event(event())['live_best_home_odds'], 1.6)
        for index, field, unaffected in ((0, 'live_best_home_odds', 'live_best_over_2_5_odds'),
                                         (1, 'live_best_over_2_5_odds', 'live_best_home_odds')):
            response = event(); market = response['bookmakers'][0]['markets'][index]
            market['outcomes'].append(copy.deepcopy(market['outcomes'][0]))
            parsed = TheOddsAPI.flatten_odds_event(response)
            self.assertIsNone(parsed[field])
            self.assertIsNotNone(parsed[unaffected])

    def test_one_malformed_book_cannot_hide_another_valid_book(self):
        response = event(); valid = copy.deepcopy(response['bookmakers'][0]); valid['title'] = 'Book B'
        response['bookmakers'][0]['markets'][0]['outcomes'].append({'name': 'A', 'price': 1.7})
        response['bookmakers'].append(valid)
        parsed = TheOddsAPI.flatten_odds_event(response)
        self.assertEqual(parsed['live_best_home_odds'], 1.6)
        self.assertEqual(parsed['live_best_home_bookmaker'], 'Book B')

    def test_duplicate_alternate_totals_and_btts_are_rejected(self):
        for market_key, names, point, result_key in (
            ('alternate_totals', ('Over', 'Under'), 1.5, 'market_over_1_5_odds'),
            ('alternate_totals', ('Under', 'Over'), 3.5, 'market_under_3_5_odds'),
            ('btts', ('Yes', 'No'), None, 'market_btts_yes_odds'),
        ):
            response = event()
            outcomes = [{'name': name, 'price': price, **({'point': point} if point else {})}
                        for name, price in zip(names, (1.4, 3.1))]
            response['bookmakers'][0]['markets'] = [{'key': market_key, 'last_update': NOW.isoformat(), 'outcomes': outcomes}]
            with self.subTest(market=market_key, point=point), tempfile.TemporaryDirectory() as tmp:
                api = TheOddsAPI('offline', cache_dir=tmp)
                with patch.object(api, '_get_json', return_value=response):
                    self.assertEqual(api.extra_markets_for_event(LEAGUES['EPL'], 'e')[result_key], 1.4)
                    outcomes.append(copy.deepcopy(outcomes[0]))
                    self.assertNotIn(result_key, api.extra_markets_for_event(LEAGUES['EPL'], 'e'))
