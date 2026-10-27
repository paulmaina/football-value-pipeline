from offline_test_case import OfflineQuotePolicyTestCase
from datetime import datetime, timedelta, timezone
import json
import math
from pathlib import Path
import unittest

import numpy as np
import pandas as pd

import bet365_pinnacle
import football_value_pipeline_v2_standalone as fvp
from football_value_pipeline_v2_standalone import (DixonColesModel, FootballValuePipelineV2,
    LEGACY_MODEL_VERSION, MODEL_VERSION, CUSTOM_MODEL_VERSION, build_parser, devig,
    model_version_for, pinnacle_ou25_reference)
import shot_features


NOW = datetime.now(timezone.utc).replace(microsecond=0)


def toy_model():
    model = DixonColesModel(max_goals=10)
    model.teams = ['A', 'B']; model.team_to_idx = {'A': 0, 'B': 1}
    model.attack = np.array([.2, -.2]); model.weakness = np.zeros(2)
    model.base = math.log(1.2); model.home_adv = .1; model.rho = -.05
    return model


def pipe(anchor=True):
    p = FootballValuePipelineV2.__new__(FootballValuePipelineV2)
    p.market_weight = .7; p.devig_method = 'power'; p.half_life_days = 480.
    p.totals_anchor = anchor; p.shot_features = True; p.half_life_tuning = False
    return p


def live_row(**extra):
    stamp = (NOW - timedelta(minutes=3)).isoformat()
    return pd.Series({'HomeTeam': 'A', 'AwayTeam': 'B', 'kickoff_utc': (NOW+timedelta(hours=5)).isoformat(),
        'odds_source': 'The Odds API', 'odds_event_id': 'ev1', 'odds_h2h_last_update_utc': stamp,
        'live_ref_home_odds': 2.0, 'live_ref_draw_odds': 3.6, 'live_ref_away_odds': 4.0, **extra})


def pinnacle_totals(minutes_old=3, event='ev1'):
    return {'bookmaker': 'pinnacle', 'event_id': event, 'over': 1.80, 'under': 2.10,
            'updated_at_utc': (NOW - timedelta(minutes=minutes_old)).isoformat()}


class ProductionDefaultsTests(OfflineQuotePolicyTestCase):
    def test_cli_and_pipeline_defaults_are_the_v2_profile(self):
        args = build_parser().parse_args([])
        self.assertEqual(args.market_weight, .70)
        self.assertEqual(args.half_life_days, 480.)
        self.assertFalse(args.tune_half_life or args.no_totals_anchor or args.no_shot_features)
        self.assertEqual(FootballValuePipelineV2.__init__.__kwdefaults__['market_weight'], .70)
        self.assertTrue(FootballValuePipelineV2.__init__.__kwdefaults__['totals_anchor'])

    def test_scheduled_production_command_does_not_tune_half_life(self):
        text = Path('publish_scheduled_forecasts.py').read_text(encoding='utf-8')
        self.assertNotIn("'--tune-half-life'", text)
        self.assertIn("'--recency-experiment'", text)

    def test_model_version_tags_profiles_and_never_relabels_custom_runs(self):
        v2 = dict(market_weight=.7, half_life_days=480, half_life_tuning=False, totals_anchor=True, shot_features=True)
        self.assertEqual(model_version_for(**v2), MODEL_VERSION)
        self.assertEqual(model_version_for(market_weight=.5, half_life_days=240, half_life_tuning=True,
                                           totals_anchor=False, shot_features=False), LEGACY_MODEL_VERSION)
        for change in ({'market_weight': .5}, {'half_life_days': 240}, {'half_life_tuning': True},
                       {'totals_anchor': False}):
            self.assertTrue(model_version_for(**{**v2, **change}).startswith(CUSTOM_MODEL_VERSION+'-'))
        self.assertEqual(model_version_for(**{**v2, 'shot_features': False}), fvp.NO_SHOTS_MODEL_VERSION)
        # The legacy profile constants stay importable for archived replay.
        self.assertEqual(fvp.MODEL_PROFILES[LEGACY_MODEL_VERSION]['market_weight'], .5)


class TotalsAnchorTests(OfflineQuotePolicyTestCase):
    def test_fresh_pinnacle_quote_anchors_totals_and_keeps_production_hda(self):
        row = live_row(shadow_pinnacle_totals=pinnacle_totals())
        anchored, _ = pipe()._predict_row(toy_model(), row)
        plain, _ = pipe(anchor=False)._predict_row(toy_model(), row)
        target = devig([1.80, 2.10], 'power')[0]
        self.assertTrue(anchored['totals_anchor_applied'])
        self.assertEqual(anchored['totals_anchor_status'], 'ANCHORED_MAIN')
        self.assertAlmostEqual(anchored['p_over_2_5'], target, places=7)
        for side in ('home', 'draw', 'away'):
            self.assertAlmostEqual(anchored['p_'+side], plain['p_'+side], places=9)
        self.assertAlmostEqual(anchored['unanchored_p_over_2_5'], plain['p_over_2_5'], places=12)
        self.assertEqual(anchored['model_version'], MODEL_VERSION)

    def test_missing_or_stale_pinnacle_quote_means_no_anchor(self):
        cases = {'NOT_ANCHORED_NO_PINNACLE': live_row(),
                 'NOT_ANCHORED_STALE': live_row(shadow_pinnacle_totals=pinnacle_totals(minutes_old=60*25)),
                 'NOT_ANCHORED_PINNACLE_EVENT_MISMATCH': live_row(shadow_pinnacle_totals=pinnacle_totals(event='other'))}
        plain, _ = pipe(anchor=False)._predict_row(toy_model(), live_row())
        for status, row in cases.items():
            with self.subTest(status=status):
                prediction, _ = pipe()._predict_row(toy_model(), row)
                self.assertFalse(prediction['totals_anchor_applied'])
                self.assertEqual(prediction['totals_anchor_status'], status)
                self.assertIsNone(prediction['totals_anchor_scale'])
                self.assertEqual(prediction['p_over_2_5'], plain['p_over_2_5'])
        # A non-Pinnacle totals reference is never used as a fallback.
        other = {**pinnacle_totals(), 'bookmaker': 'onexbet'}
        self.assertEqual(pinnacle_ou25_reference(live_row(shadow_pinnacle_totals=other), NOW)[1],
                         'NOT_ANCHORED_NO_PINNACLE')

    def test_historical_rows_use_only_pinnacle_opening_totals(self):
        row = pd.Series({'HomeTeam': 'A', 'AwayTeam': 'B', 'B365>2.5': 1.9, 'B365<2.5': 1.95})
        self.assertEqual(pinnacle_ou25_reference(row, NOW), (None, 'NOT_ANCHORED_NO_PINNACLE'))
        ref, status = pinnacle_ou25_reference(pd.Series({**row, 'P>2.5': 1.9, 'P<2.5': 2.0}), NOW)
        self.assertEqual(status, 'ANCHORED_MAIN'); self.assertEqual(ref['source'], 'historical_pinnacle_nominal_opening')


def shot_history(days=420, start='2024-01-01'):
    teams = ['A', 'B', 'C', 'D']
    rows = []
    for i, date in enumerate(pd.date_range(start, periods=days, freq='D')):
        h, a = teams[i % 4], teams[(i+1+i//4) % 4]
        if h == a:
            a = teams[(i+2) % 4]
        rows.append({'Date': date, 'HomeTeam': h, 'AwayTeam': a, 'FTHG': (i*7) % 4, 'FTAG': (i*5) % 3,
                     'HST': 3+(i*5) % 6, 'AST': 2+(i*3) % 5, 'HS': 12+(i % 7), 'AS': 9+(i % 5)})
    return pd.DataFrame(rows)


class ShotFeatureLagTests(OfflineQuotePolicyTestCase):
    def test_strengths_use_only_matches_dated_before_the_origin(self):
        history = shot_history()
        origin = pd.Timestamp('2024-10-01')
        table = shot_features.shot_table(history)
        base = shot_features.ShotStrengths(table, origin, 480., 15., 'shots_on_target_and_total_shots')
        changed = history.copy()
        later = pd.to_datetime(changed['Date']) >= origin  # includes the same day
        changed.loc[later, ['HST', 'AST', 'HS', 'AS', 'FTHG', 'FTAG']] = [20, 0, 30, 1, 9, 0]
        again = shot_features.ShotStrengths(shot_features.shot_table(changed), origin, 480., 15.,
                                            'shots_on_target_and_total_shots')
        self.assertEqual(base.matches, int((history['Date'] < origin).sum()))
        self.assertEqual(base.attack, again.attack); self.assertEqual(base.defence, again.defence)
        np.testing.assert_array_equal(base.rates('A', 'B'), again.rates('A', 'B'))
        # An earlier match does move the estimate.
        earlier = history.copy(); earlier.loc[earlier['Date'] == origin - pd.Timedelta(days=1), 'HST'] = 20
        moved = shot_features.ShotStrengths(shot_features.shot_table(earlier), origin, 480., 15., 'shots_on_target')
        self.assertNotEqual(moved.attack, shot_features.ShotStrengths(table, origin, 480., 15., 'shots_on_target').attack)

    def test_gate_fit_ignores_future_rows_and_logs_its_decision(self):
        history = shot_history(days=800, start='2023-01-01')
        cutoff = pd.Timestamp('2025-02-01')
        factory = lambda past, origin: DixonColesModel(half_life_days=480, bbs_statistics=False).fit(past, as_of=origin)
        first = shot_features.fit_shot_model(history.loc[history['Date'] < cutoff], cutoff, factory, 480.)
        future = shot_history(days=30, start='2025-02-01'); future['HST'] = 25
        second = shot_features.fit_shot_model(pd.concat([history.loc[history['Date'] < cutoff], future]),
                                              cutoff, factory, 480.)
        self.assertEqual(first.report, second.report)
        # The full chronological tune/audit ran and logged every gate input.
        self.assertIn(first.report['status'], ('VALIDATED', 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED'))
        self.assertGreaterEqual(first.report['audit_matches'], shot_features.MIN_AUDIT)
        self.assertIn('audit_gain_lower95', first.report)
        self.assertLess(pd.Timestamp(first.report['tune_start_date']), pd.Timestamp(first.report['audit_start_date']))
        if first.report['status'] != 'VALIDATED':
            self.assertEqual(first.weight, 0.)

    def test_incoherent_or_missing_shots_are_dropped(self):
        frame = shot_history(days=6)
        frame.loc[0, 'HST'] = 99  # more on target than total shots
        frame.loc[1, 'AST'] = None
        frame.loc[2, 'HST'] = -1
        self.assertEqual(len(shot_features.shot_table(frame)), 3)
        self.assertTrue(shot_features.shot_table(frame.drop(columns=['HST'])).empty)

    def test_bbs_hook_is_off_until_bbs_validates(self):
        self.assertFalse(shot_features.BBS_SHOT_SOURCE_ENABLED)
        extra = shot_history(days=3); extra['HST'] = 1
        self.assertEqual(len(shot_features.shot_table(shot_history(days=5), extra)), 5)


def book(key, markets, minutes_old=2):
    stamp = (NOW - timedelta(minutes=minutes_old)).isoformat()
    return {'key': key, 'title': key, 'last_update': stamp,
            'markets': [{'key': k, 'last_update': stamp, 'outcomes': o} for k, o in markets.items()]}


def h2h(home, draw, away):
    return [{'name': 'A', 'price': home}, {'name': 'Draw', 'price': draw}, {'name': 'B', 'price': away}]


def payload(bet365_key='bet365', bet365_age=2, pinnacle_age=1):
    return {'id': 'ev1', 'home_team': 'A', 'away_team': 'B', 'commence_time': (NOW+timedelta(hours=5)).isoformat(),
            'bookmakers': [book('pinnacle', {'h2h': h2h(2.0, 3.6, 4.0),
                                             'totals': [{'name': 'Over', 'point': 2.5, 'price': 1.9},
                                                        {'name': 'Under', 'point': 2.5, 'price': 1.95}]}, pinnacle_age),
                           book(bet365_key, {'h2h': h2h(2.2, 3.3, 3.6),
                                             'double_chance': [{'name': 'A/Draw', 'price': 1.35},
                                                               {'name': 'Draw/B', 'price': 1.9},
                                                               {'name': 'A/B', 'price': 1.3}],
                                             'totals': [{'name': 'Over', 'point': 2.5, 'price': 1.8},
                                                        {'name': 'Under', 'point': 2.5, 'price': 2.0}]}, bet365_age)]}


class Bet365VersusPinnacleTests(OfflineQuotePolicyTestCase):
    def test_ev_uses_pinnacle_fair_probability_from_the_same_capture(self):
        rows = {r['selection']: r for r in bet365_pinnacle.compare_event(payload(), NOW)}
        fair = devig([2.0, 3.6, 4.0], 'power')
        self.assertAlmostEqual(rows['home']['pinnacle_fair_probability'], fair[0], places=12)
        self.assertAlmostEqual(rows['home']['ev_vs_pinnacle_fair'], fair[0]*2.2-1, places=12)
        self.assertAlmostEqual(rows['away']['ev_vs_pinnacle_fair'], fair[2]*3.6-1, places=12)
        over = devig([1.9, 1.95], 'power')[0]
        self.assertAlmostEqual(rows['over_2_5']['ev_vs_pinnacle_fair'], over*1.8-1, places=12)
        self.assertEqual(rows['home']['bet365_quote_age_seconds'], 120.)
        self.assertEqual(rows['home']['pinnacle_quote_age_seconds'], 60.)
        self.assertEqual(rows['home']['capture_utc'], NOW.isoformat())
        dc = rows['home_draw']
        self.assertIsNone(dc['pinnacle_decimal_odds'])  # no fabricated Pinnacle DC price
        self.assertAlmostEqual(dc['pinnacle_fair_probability'], fair[0]+fair[1], places=12)
        self.assertAlmostEqual(dc['ev_vs_pinnacle_fair'], (fair[0]+fair[1])*1.35-1, places=12)
        self.assertEqual(rows['home']['bet365_decimal_odds'], 2.2)

    def test_list_needs_two_percent_edge_fresh_quotes_and_window(self):
        quotes = bet365_pinnacle.compare_event(payload(), NOW)
        source = {'league': 'EPL', 'home_team': 'A', 'away_team': 'B', 'odds_event_id': 'ev1',
                  'kickoff_utc': (NOW+timedelta(hours=5)).isoformat(), 'bet365_pinnacle_quotes': json.dumps(quotes)}
        listed = bet365_pinnacle.build_list([source], NOW.isoformat())
        self.assertTrue(listed)
        self.assertTrue(all(r['ev_vs_pinnacle_fair'] >= .02 for r in listed))
        expected = {q['selection'] for q in quotes if q['ev_vs_pinnacle_fair'] >= .02}
        self.assertEqual({r['selection'] for r in listed}, expected)
        self.assertTrue(all(r['list'] == 'bet365 vs Pinnacle' for r in listed))
        later = (NOW+timedelta(hours=25)).isoformat()  # quotes now older than 24 hours
        self.assertEqual(bet365_pinnacle.build_list([{**source, 'kickoff_utc': (NOW+timedelta(hours=30)).isoformat()}], later), [])
        self.assertEqual(bet365_pinnacle.build_list([{**source, 'kickoff_utc': (NOW+timedelta(hours=60)).isoformat()}], NOW.isoformat()), [])
        self.assertEqual(bet365_pinnacle.build_list([{**source, 'odds_event_id': 'other'}], NOW.isoformat()), [])

    def test_stale_quotes_and_other_bet365_feeds_are_excluded(self):
        self.assertEqual(bet365_pinnacle.compare_event(payload(bet365_key='bet365_au'), NOW), [])
        stale = bet365_pinnacle.compare_event(payload(bet365_age=60*25), NOW)
        self.assertEqual(stale, [])
        self.assertEqual(bet365_pinnacle.compare_event(payload(pinnacle_age=60*25), NOW), [])

    def test_merge_keeps_newest_capture_per_selection(self):
        old = [{'selection': 'home', 'capture_utc': '2026-01-01T00:00:00+00:00', 'ev_vs_pinnacle_fair': .1}]
        new = [{'selection': 'home', 'capture_utc': '2026-01-01T00:05:00+00:00', 'ev_vs_pinnacle_fair': .03}]
        merged = json.loads(bet365_pinnacle.merge(json.dumps(old), new))
        self.assertEqual(merged, new)


if __name__ == '__main__':
    unittest.main()


class BenchmarkUpgradeTests(OfflineQuotePolicyTestCase):
    def test_asian_handicap_probabilities_and_refunds(self):
        import historical_benchmark as hb
        matrix = hb.adjusted_matrix(1.4, 1.1, -.05, 10)
        ah = hb.handicaps(matrix)
        h, a = np.indices(matrix.shape)
        self.assertAlmostEqual(ah['ah_home_-1.5'], float(matrix[h-a >= 2].sum()), places=12)
        win, loss = float(matrix[h > a].sum()), float(matrix[h < a].sum())
        self.assertAlmostEqual(ah['ah_home_+0.0'], win/(win+loss), places=12)
        row = {'home_goals': 1, 'away_goals': 1, 'ah_home_+0.0': .6, 'ah_home_-1.5': .2}
        self.assertIsNone(hb.score(row, 'ah_home_+0.0'))  # refunded: no binary outcome
        self.assertEqual(hb.score(row, 'ah_home_-1.5')['outcome'], 0)

    def test_upgrade_config_requires_v2_and_valid_settings(self):
        import historical_benchmark as hb
        cfg = json.loads(Path('historical_benchmark_config.json').read_text(encoding='utf-8-sig'))
        hb.validate_config(cfg)
        self.assertEqual(cfg['model_upgrade_comparison']['production_v2']['market_weight'], .7)
        self.assertEqual(cfg['model_upgrade_comparison']['production_v2']['half_life_days'], 480.)
        bad = json.loads(json.dumps(cfg)); bad['version'] = 'historical-dc-benchmark-v1'
        with self.assertRaises(ValueError):
            hb.validate_config(bad)
        bad = json.loads(json.dumps(cfg)); bad['model_upgrade_comparison']['production_v2']['market_weight'] = 1.0
        with self.assertRaises(ValueError):
            hb.validate_config(bad)
        old = json.loads(json.dumps(cfg)); old['version'] = 'historical-dc-benchmark-v1'; old.pop('model_upgrade_comparison')
        hb.validate_config(old)  # archived v1 benchmark artifacts still validate


class Bet365ClosingTests(OfflineQuotePolicyTestCase):
    def test_bet365_entries_require_bet365_and_pinnacle_closing_quotes(self):
        import closing_odds
        source = {'league': 'EPL', 'home_team': 'A', 'away_team': 'B', 'odds_event_id': 'ev1',
                  'kickoff_utc': NOW.isoformat()}
        missing = closing_odds.required_quotes(source, {closing_odds.BET365_TARGET+'Over 2.5'}, [])
        self.assertEqual(missing, {('bet365', 'over_2_5'), ('pinnacle', 'over_2_5')})
        both = closing_odds.required_quotes(source, {'Home win', closing_odds.BET365_TARGET+'Home win'}, [])
        self.assertEqual(both, {('1xbet', 'home'), ('pinnacle', 'home'), ('bet365', 'home')})
