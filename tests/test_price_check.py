"""Lightweight price check: main odds refresh + v27 re-rank, off by default."""

from offline_test_case import OfflineQuotePolicyTestCase
import io
import json
import os
import tempfile
import unittest
from contextlib import redirect_stdout
from datetime import datetime, timezone
from pathlib import Path
from unittest.mock import patch

import pandas as pd

import price_check
from test_price_edge_shortlist import NOW, FRESH, ah_pair, offer, row

ROOT = Path(__file__).resolve().parents[1]


class FakeApi:
    def __init__(self, frames=None):
        self.frames, self.calls = frames or {}, []

    def odds(self, league, lookahead_days, now):
        self.calls.append(league.key)
        return self.frames.get(league.key, pd.DataFrame())


def forecast(**overrides):
    data = row(**overrides)
    data.update(odds_event_id=data['fixture_id'], p_home=0.45, p_draw=0.27, p_away=0.28)
    return data


class ScheduleTests(OfflineQuotePolicyTestCase):
    def test_due_only_on_interval_hours(self):
        at = lambda hour: datetime(2026, 11, 7, hour, 15, tzinfo=timezone.utc)
        self.assertTrue(price_check.due(at(3), 3))
        self.assertFalse(price_check.due(at(4), 3))
        self.assertTrue(price_check.due(at(12), 4))
        self.assertTrue(price_check.due(at(18), 6))
        with self.assertRaises(ValueError):
            price_check.due(at(0), 5)

    def test_leagues_in_window(self):
        frame = pd.DataFrame([forecast(), forecast(home='Later', kickoff=NOW + pd.Timedelta(hours=60)),
                              {**forecast(home='Past', kickoff=NOW - pd.Timedelta(hours=1)), 'league': 'LaLiga'}])
        self.assertEqual(price_check.leagues_in_window(frame, NOW.to_pydatetime()), ['EPL'])
        self.assertEqual(price_check.leagues_in_window(pd.DataFrame(), NOW.to_pydatetime()), [])

    def test_monthly_credits_scale_with_interval(self):
        daily = [pd.Timestamp('2026-01-01T15:00Z') + pd.Timedelta(days=d) for d in range(60)]
        three, six = price_check.monthly_credits(daily, 3), price_check.monthly_credits(daily, 6)
        self.assertAlmostEqual(three, 8 * 3 * 30, delta=30)
        self.assertAlmostEqual(six, three / 2, delta=20)
        self.assertEqual(price_check.monthly_credits([], 3), 0.0)
        weekly = [pd.Timestamp('2026-01-03T15:00Z') + pd.Timedelta(days=7 * w) for w in range(8)]
        self.assertLess(price_check.monthly_credits(weekly, 3), three / 2)

    def test_estimate_reports_three_intervals(self):
        estimate = price_check.estimate(ROOT / '.football_cache')
        self.assertEqual(set(estimate), {'3h', '4h', '6h'})
        self.assertGreater(estimate['3h'], estimate['4h'])
        self.assertGreater(estimate['4h'], estimate['6h'])


def event(data, **fields):
    """A flattened odds event for `data`'s fixture, as TheOddsAPI.odds returns it."""
    return {'fixture_id': data['fixture_id'], '_odds_home_team': data['home_team'],
            '_odds_away_team': data['away_team'], '_odds_commence_time': data['kickoff_utc'], **fields}


class MergeTests(OfflineQuotePolicyTestCase):
    def test_newest_quote_wins_and_unmatched_rows_are_untouched(self):
        old = forecast(offers=[offer('home', -0.75, 1.90, stamp='2026-11-07T08:00:00+00:00')])
        other = forecast(home='Other')
        fresh = pd.DataFrame([event(old, asian_handicap_offers=json.dumps([offer('home', -0.75, 2.10)]),
                                    price_edge_quotes=json.dumps([{'bookmaker': '1xBet', 'market': 'h2h', 'market_key': 'h2h',
                                                                   'point': None, 'prices': {'home': 2.2, 'draw': 3.3, 'away': 3.6},
                                                                   'last_update_utc': FRESH}]))])
        merged = price_check.merge_odds(pd.DataFrame([old, other]), fresh)
        offers = json.loads(merged.iloc[0].asian_handicap_offers)
        mine = [o for o in offers if o['bookmaker'] == '1xBet']
        self.assertEqual([o['price'] for o in mine], [2.10])
        self.assertTrue(any(q['bookmaker'] == '1xBet' for q in json.loads(merged.iloc[0].price_edge_quotes)))
        self.assertEqual(merged.iloc[1].asian_handicap_offers, other['asian_handicap_offers'])
        self.assertTrue(price_check.merge_odds(pd.DataFrame([old]), pd.DataFrame()).equals(pd.DataFrame([old])))

    def test_event_with_other_teams_or_moved_kickoff_is_not_merged(self):
        stored = forecast(offers=[offer('home', -0.75, 1.90, stamp='2026-11-07T08:00:00+00:00')])
        prices = json.dumps([offer('home', -0.75, 2.10)])
        later = (NOW + pd.Timedelta(days=8)).isoformat()
        for changed in ({'_odds_home_team': 'Different FC', '_odds_away_team': 'Other United'},
                        {'_odds_away_team': 'Other United'},
                        {'_odds_commence_time': later},
                        {'_odds_commence_time': (pd.Timestamp(stored['kickoff_utc']) + pd.Timedelta(minutes=6)).isoformat()},
                        {'_odds_commence_time': None}):
            merged = price_check.merge_odds(pd.DataFrame([stored]),
                                            pd.DataFrame([event(stored, asian_handicap_offers=prices, price_edge_quotes='[]', **changed)]))
            self.assertEqual(merged.iloc[0].asian_handicap_offers, stored['asian_handicap_offers'], changed)
            self.assertEqual(merged.iloc[0].home_team, stored['home_team'])
        within = (pd.Timestamp(stored['kickoff_utc']) + pd.Timedelta(minutes=4)).isoformat()
        merged = price_check.merge_odds(pd.DataFrame([stored]), pd.DataFrame(
            [event(stored, asian_handicap_offers=prices, price_edge_quotes='[]', _odds_commence_time=within)]))
        self.assertIn(2.10, [o['price'] for o in json.loads(merged.iloc[0].asian_handicap_offers)])


class CheckTests(OfflineQuotePolicyTestCase):
    def setUp(self):
        super().setUp()
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        (self.root / 'raw').mkdir()

    def tearDown(self):
        self.tmp.cleanup()
        super().tearDown()

    def write(self, rows):
        pd.DataFrame(rows).to_csv(self.root / 'raw' / 'all_leagues_predictions.csv', index=False)

    def test_no_fixture_in_window_makes_no_request(self):
        self.write([forecast(kickoff=NOW + pd.Timedelta(hours=72))])
        api = FakeApi()
        self.assertEqual(price_check.check(self.root, api, NOW.to_pydatetime())['status'], 'NO_FIXTURES_IN_WINDOW')
        self.assertEqual(api.calls, [])

    def test_check_refreshes_quotes_reranks_and_publishes_without_refit(self):
        import price_edge_cagey_shortlist as v28
        historical = {**v28.load_settings(), 'value_rule': v28.VALUE_RULE_PER_MARKET}
        self.addCleanup(patch.stopall)
        patch.object(v28, 'load_settings', return_value=historical).start()
        base = forecast(offers=[*ah_pair(-0.75, 1.95, 1.95)])
        self.write([base])
        fresh = pd.DataFrame([event(base, asian_handicap_offers=json.dumps([offer('home', -0.75, 2.10)]),
                                    price_edge_quotes='[]')])
        api = FakeApi({'EPL': fresh})
        result = price_check.check(self.root, api, NOW.to_pydatetime())
        self.assertEqual(result, {'status': 'CHECKED', 'leagues': ['EPL'], 'requests': 1, 'credits': 3, 'picks': 1})
        from prediction_runs import resolve_raw
        raw = resolve_raw(self.root / 'raw')
        picks = pd.read_csv(raw / 'conservative_bet_shortlist.csv')
        summary = json.loads((raw / 'conservative_bet_summary.json').read_text(encoding='utf-8'))
        predictions = pd.read_csv(raw / 'all_leagues_predictions.csv')
        self.assertEqual(picks.offered_decimal_odds.tolist(), [2.10])
        self.assertIn('no model refit', summary['refresh_source'])
        self.assertEqual(predictions.p_home.tolist(), [0.45])
        self.assertTrue((self.root / 'readable' / 'conservative_bet_shortlist_readable.csv').exists())


class MainTests(OfflineQuotePolicyTestCase):
    def test_estimate_flag_prints_json(self):
        buffer = io.StringIO()
        with patch.object(price_check, 'estimate', return_value={'3h': 1, '4h': 1, '6h': 1}), redirect_stdout(buffer):
            self.assertEqual(price_check.main(['--estimate']), 0)
        self.assertIn('monthly_credits_main_request_only', buffer.getvalue())

    def test_not_due_and_missing_key_exit_quietly(self):
        buffer = io.StringIO()
        with patch.object(price_check, 'due', return_value=False), redirect_stdout(buffer):
            self.assertEqual(price_check.main(['--interval-hours', '4']), 0)
        self.assertIn('Not due', buffer.getvalue())
        buffer = io.StringIO()
        with patch.dict(os.environ, {}, clear=True), redirect_stdout(buffer):
            self.assertEqual(price_check.main(['--api-key-source', 'environment']), 0)
        self.assertIn('No Odds API key', buffer.getvalue())

    def test_odds_cache_is_temporary_and_outside_the_repository(self):
        seen = {}

        class Recorder:
            KEY_ENV_NAMES = ('THE_ODDS_API_KEY',)

            def __init__(self, key, cache_dir=None):
                seen['cache'] = Path(cache_dir)
                seen['existed'] = Path(cache_dir).is_dir()

        buffer = io.StringIO()
        with patch.dict(os.environ, {'THE_ODDS_API_KEY': 'offline-fake-key'}, clear=True),                 patch('football_value_pipeline_v2_standalone.TheOddsAPI', Recorder),                 patch.object(price_check, 'check', return_value={'status': 'NO_FIXTURES_IN_WINDOW'}),                 redirect_stdout(buffer):
            self.assertEqual(price_check.main(['--api-key-source', 'environment']), 0)
        self.assertTrue(seen['existed'])
        self.assertFalse(seen['cache'].exists())
        self.assertNotIn(ROOT.resolve(), seen['cache'].resolve().parents)

    def test_workflow_is_off_by_default(self):
        text = (ROOT / '.github' / 'workflows' / 'price-checks.yml').read_text(encoding='utf-8')
        self.assertIn("if: vars.PRICE_CHECKS_ENABLED == 'true'", text)
        self.assertIn('price_check.py --api-key-source environment --interval-hours', text)
        self.assertLess(text.index('git diff --quiet'), text.index('git pull --rebase'))
        self.assertNotIn('per-event', price_check.MAIN_MARKETS)
        self.assertEqual(price_check.MAIN_MARKETS, ('h2h', 'totals', 'spreads'))


if __name__ == '__main__':
    unittest.main()
