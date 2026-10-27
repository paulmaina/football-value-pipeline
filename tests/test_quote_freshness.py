"""Live ingestion, strict reference provenance and immutable legacy replay."""
import copy
from datetime import timedelta
import tempfile
from pathlib import Path
from unittest.mock import patch

import pandas as pd

from offline_test_case import OfflineQuotePolicyTestCase
from quote_freshness import quote_clock, quote_is_fresh, quote_utc
from football_value_pipeline_v2_standalone import TheOddsAPI, LEAGUES, market_snapshot
from conservative_bet_filter import MARKET_SPECS, _evaluate_market, build_conservative_shortlist
from test_conservative_bet_filter import fixture, NOW
from test_double_chance import event as dc_event
from test_graded_candidates import sample_report
from double_chance import parse_quotes


def book(name='Book A', stamp=None, home=1.52, away=7.3, over=1.30, btts=1.49):
    stamp = NOW.isoformat() if stamp is None else stamp
    return {'title': name, 'last_update': stamp, 'markets': [
        {'key': 'h2h', 'last_update': stamp, 'outcomes': [
            {'name': 'Home', 'price': home}, {'name': 'Draw', 'price': 4.3}, {'name': 'Away', 'price': away}]},
        {'key': 'totals', 'last_update': stamp, 'outcomes': [
            {'name': 'Over', 'point': 2.5, 'price': 1.90}, {'name': 'Under', 'point': 2.5, 'price': 1.95}]},
        {'key': 'alternate_totals', 'last_update': stamp, 'outcomes': [
            {'name': 'Over', 'point': 1.5, 'price': over}, {'name': 'Under', 'point': 1.5, 'price': 3.7},
            {'name': 'Under', 'point': 3.5, 'price': 1.40}, {'name': 'Over', 'point': 3.5, 'price': 2.8}]},
        {'key': 'btts', 'last_update': stamp, 'outcomes': [
            {'name': 'Yes', 'price': btts}, {'name': 'No', 'price': 2.4}]},
    ]}


def payload(books):
    return {'id': 'e', 'home_team': 'Home', 'away_team': 'Away', 'bookmakers': books}


def extra(response):
    api = TheOddsAPI.__new__(TheOddsAPI)
    api.regions = 'eu'; api.api_key = 'fake'; api.force_refresh = False
    with patch.object(api, '_get_json', return_value=response), patch(
            'football_value_pipeline_v2_standalone.datetime') as clock:
        clock.now.return_value = NOW
        return api.extra_markets_for_event(LEAGUES['EPL'], 'e')


class FreshnessTests(OfflineQuotePolicyTestCase):
    def test_shared_utc_clock_and_inclusive_boundaries(self):
        for delta in (timedelta(hours=-24), timedelta(minutes=5), timedelta()):
            self.assertTrue(quote_is_fresh(NOW+delta, NOW))
        for value in (None, '', 'bad-time', [], float('nan'), NOW-timedelta(hours=24, seconds=1),
                      NOW+timedelta(minutes=5, seconds=1)):
            self.assertFalse(quote_is_fresh(value, NOW))
        self.assertFalse(quote_is_fresh(NOW, 'bad-clock'))
        self.assertIsNone(quote_utc({}))
        self.assertEqual(quote_clock('2026-10-09T12:00:00+03:00'), pd.Timestamp(NOW))
        with self.assertRaisesRegex(ValueError, 'evaluation time'):
            quote_clock('bad-clock')

    def test_winner_and_ou25_prices_and_references_ignore_stale_and_future_books(self):
        for bad in (NOW-timedelta(hours=25), NOW+timedelta(hours=1)):
            response = payload([book('Book A', bad.isoformat(), home=1.60), book('Book B')])
            result = TheOddsAPI.flatten_odds_event(response, as_of=NOW)
            for side in ('home', 'draw', 'away', 'over_2_5', 'under_2_5'):
                self.assertEqual(result[f'live_best_{side}_bookmaker'], 'Book B')
                self.assertEqual(result[f'live_best_{side}_last_update_utc'], NOW.isoformat())
            self.assertEqual(result['live_ref_1x2_bookmaker'], 'Book B')
            self.assertEqual(result['live_ref_ou25_bookmaker'], 'Book B')
            self.assertEqual(result['odds_bookmakers_1x2'], 1)
            self.assertEqual(result['odds_bookmakers_ou25'], 1)
        for side in ('home', 'away'):
            stale = book('Book A', (NOW-timedelta(hours=25)).isoformat(),
                         home=1.6 if side == 'home' else 6, away=6 if side == 'home' else 1.6)
            fresh = book('Book B', home=1.52 if side == 'home' else 7.3,
                         away=7.3 if side == 'home' else 1.55)
            flat = TheOddsAPI.flatten_odds_event(payload([stale, fresh]), as_of=NOW)
            row = fixture(); row.update(market_snapshot(pd.Series(flat)))
            row.update(market_over_1_5_odds=None, market_btts_yes_odds=None)
            row['odds_bookmakers_1x2'] = flat['odds_bookmakers_1x2']
            for key in ('home', 'away'):
                row[f'best_{key}_bookmaker'] = flat[f'live_best_{key}_bookmaker']
                row[f'market_best_{key}_last_update_utc'] = flat[f'live_best_{key}_last_update_utc']
            if side == 'away':
                row.update(p_home=.12, p_draw=.16, p_away=.72, raw_p_home=.14, raw_p_draw=.18, raw_p_away=.68)
            picks, _, _ = build_conservative_shortlist(pd.DataFrame([row]), as_of=NOW)
            self.assertEqual(picks.market.tolist(), ['Home win' if side == 'home' else 'Away win'])

    def test_goal_offers_and_reference_timestamps_keep_only_fresh_complete_books(self):
        bad = book('Book A', (NOW-timedelta(hours=25)).isoformat(), over=1.40, btts=1.60)
        result = extra(payload([bad, book('Book B')]))
        for key, odds in (('over_1_5', 1.30), ('under_3_5', 1.40), ('btts_yes', 1.49)):
            self.assertEqual(result[f'best_{key}_bookmaker'], 'Book B')
            self.assertEqual(result[f'market_{key}_odds'], odds)
            self.assertEqual(result[f'market_{key}_bookmakers'], 1)
            self.assertEqual(result[f'market_reference_{key}_last_update_utc'], NOW.isoformat())
        self.assertEqual(extra(payload([bad])), {})
        for stamp in ('', 'bad-time', (NOW+timedelta(hours=1)).isoformat()):
            bad = book('Book A', stamp)
            bad.pop('last_update')
            self.assertEqual(extra(payload([bad])), {})
            flat = TheOddsAPI.flatten_odds_event(payload([bad]), as_of=NOW)
            self.assertIsNone(flat['live_ref_home_odds'])
            self.assertIsNone(flat['live_ref_over_2_5_odds'])

    def test_each_market_keeps_its_own_timestamp_and_fallback(self):
        response = payload([book()])
        response['bookmakers'][0]['markets'][0]['last_update'] = (NOW-timedelta(hours=25)).isoformat()
        flat = TheOddsAPI.flatten_odds_event(response, as_of=NOW)
        self.assertIsNone(flat['live_ref_home_odds'])
        self.assertIsNotNone(flat['live_ref_over_2_5_odds'])
        self.assertIn('market_btts_yes_odds', extra(response))
        response['bookmakers'][0]['markets'][2]['last_update'] = 'bad-time'
        result = extra(response)
        self.assertNotIn('market_over_1_5_odds', result)
        self.assertIn('market_btts_yes_odds', result)
        response = payload([book()])
        for market in response['bookmakers'][0]['markets']:
            market.pop('last_update')
        self.assertEqual(TheOddsAPI.flatten_odds_event(response, as_of=NOW)['odds_bookmakers_1x2'], 1)
        self.assertEqual(extra(response)['market_reference_btts_yes_last_update_utc'], NOW.isoformat())

    def test_reference_order_uses_utc_and_prices_keep_atomic_timestamps(self):
        old = book('Book A', '2026-10-09T10:00:00+02:00', home=1.60)
        new = book('Book B', NOW.isoformat())
        response = payload([old, new])
        flat = TheOddsAPI.flatten_odds_event(response, as_of=NOW)
        # The lower-margin 1X2 book is the reference however old (but fresh) it is;
        # equal-margin O/U books fall back to the newest UTC update.
        self.assertEqual(flat['live_ref_1x2_bookmaker'], 'Book A')
        self.assertEqual(flat['live_ref_ou25_bookmaker'], 'Book B')
        self.assertEqual(extra(response)['market_reference_btts_yes_last_update_utc'], NOW.isoformat())
        # Repeated display names must not relabel an older selected price as new.
        new['title'] = 'Book A'
        flat = TheOddsAPI.flatten_odds_event(response, as_of=NOW)
        self.assertEqual(flat['live_best_home_odds'], 1.60)
        self.assertEqual(flat['live_best_home_last_update_utc'], old['last_update'])
        self.assertEqual(flat['odds_bookmakers_1x2'], 1)

    def test_live_h2h_api_passes_clock_and_exports_prediction_provenance(self):
        api = TheOddsAPI.__new__(TheOddsAPI)
        api.regions = 'eu'; api.api_key = 'fake'; api.force_refresh = False
        response = payload([book('Bad', (NOW+timedelta(hours=1)).isoformat()), book('Book A')])
        with patch.object(api, '_get_json', return_value=[response]), patch(
                'football_value_pipeline_v2_standalone.datetime') as clock:
            clock.now.return_value = NOW
            result = api.odds(LEAGUES['EPL'], 10, NOW)
        snap = market_snapshot(result.iloc[0])
        for key in ('1x2', 'home', 'draw', 'away', 'over_2_5', 'under_2_5'):
            self.assertEqual(snap[f'market_reference_{key}_last_update_utc'], NOW.isoformat())
        with patch.object(api, '_get_json', return_value=[payload([book('Bad', (NOW+timedelta(hours=1)).isoformat())])]), patch(
                'football_value_pipeline_v2_standalone.datetime') as clock:
            clock.now.return_value = NOW
            snap = market_snapshot(api.odds(LEAGUES['EPL'], 10, NOW).iloc[0])
        self.assertIsNone(snap['market_p_home'])
        self.assertIsNone(snap['market_reference_1x2_last_update_utc'])

    def test_shortlist_rechecks_exact_and_blend_reference_for_every_market(self):
        for spec in MARKET_SPECS:
            key = spec[1]
            base = fixture(); base.update(parse_quotes(dc_event()))
            base['p_'+key] = .82; base['raw_p_'+key] = .82
            base['market_'+key+'_odds'] = 1.40
            if key in ('home', 'away'):
                for side in ('home', 'draw', 'away'):
                    base['raw_p_'+side] = .82 if side == key else .09
            evidence = sample_report()
            evidence['markets'][key] = copy.deepcopy(evidence['markets']['over_1_5'])
            for field in (f'market_reference_{key}_last_update_utc', 'market_reference_1x2_last_update_utc'):
                for invalid in (None, 'bad-time', (NOW-timedelta(hours=25)).isoformat(), (NOW+timedelta(hours=1)).isoformat()):
                    with self.subTest(key=key, field=field, invalid=invalid):
                        row = dict(base, **{field: invalid})
                        decision = _evaluate_market(pd.Series(row), spec, pd.Timestamp(NOW), evidence)
                        self.assertEqual(decision['decision'], 'REJECTED')
                        self.assertIn('reference is missing, stale or future-dated' if field.endswith('1x2_last_update_utc') or key in ('home_draw','draw_away','home_away') else 'reference market is missing, stale or future-dated', decision['rejection_reasons'])

    def test_missing_live_reference_cannot_reactivate_opening_prices_but_history_is_unchanged(self):
        historical = pd.Series({'B365H': 1.52, 'B365D': 4.3, 'B365A': 7.3,
                                'B365>2.5': 1.90, 'B365<2.5': 1.95})
        self.assertIsNotNone(market_snapshot(historical)['market_p_home'])
        live = historical.copy(); live['odds_source'] = 'The Odds API'
        current = market_snapshot(live)
        self.assertIsNone(current['market_p_home'])
        self.assertIsNone(current['market_p_over_2_5'])

    def test_v10_archive_replays_missing_reference_metadata_without_backfill(self):
        import shortlist_policy_experiment as trial
        import conservative_bet_filter as engine
        from test_shortlist_policy_experiment import setup
        from performance_tracking import capture, snapshots
        row = fixture()
        for field in list(row):
            if field.startswith('market_reference_') and field.endswith('_last_update_utc'):
                row.pop(field)
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            with patch.object(trial, 'BASELINE_POLICY', trial.PREVIOUS_BASELINE_POLICY), patch.object(
                    engine, 'SELECTION_POLICY_VERSION', trial.PREVIOUS_BASELINE_POLICY):
                raw, data, predictions, picks, _, summary = setup(root, row=row)
            self.assertFalse(picks.empty)
            trial.validate(data, summary['generated_at_utc'], predictions.to_dict('records'))
            self.assertIsNotNone(trial.capture_file(raw, summary['generated_at_utc']))
            self.assertTrue(capture('c'*40, root=root, captured_at=NOW))
            frozen, rejected = trial.frozen(root, snapshots(root))
            self.assertEqual(len(frozen), 63); self.assertFalse(rejected)
            current, _, _ = build_conservative_shortlist(predictions, as_of=NOW)
            self.assertTrue(current.empty)
            data['selection_policy_version'] = trial.BASELINE_POLICY
            with self.assertRaisesRegex(ValueError, 'frozen replay'):
                trial.validate(data, summary['generated_at_utc'], predictions.to_dict('records'))
