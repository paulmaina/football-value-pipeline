from offline_test_case import OfflineQuotePolicyTestCase
from datetime import datetime, timedelta, timezone
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import numpy as np
import pandas as pd

import football_value_pipeline_v2_standalone as fvp
from football_value_pipeline_v2_standalone import (DixonColesModel, FootballValuePipelineV2,
    LEGACY_MODEL_VERSION, MODEL_VERSION, SHOT_EXPERIMENT_MODEL_VERSION, build_parser, model_version_for)
import historical_benchmark as hb
from performance_tracking import verified_record

START = datetime(2026, 11, 2, 12, tzinfo=timezone.utc)


def toy_model(league_key=None):
    model = DixonColesModel(max_goals=10)
    model.teams = ['A', 'B']; model.team_to_idx = {'A': 0, 'B': 1}
    model.attack = np.array([.2, -.2]); model.weakness = np.zeros(2)
    model.base = np.log(1.2); model.home_adv = .1; model.rho = -.05
    model.league_key = league_key
    return model


def pipe():
    p = FootballValuePipelineV2.__new__(FootballValuePipelineV2)
    p.market_weight = .7; p.devig_method = 'power'; p.half_life_days = 480.
    p.totals_anchor = True; p.shot_features = True; p.half_life_tuning = False
    p.legacy_comparison = True; p._legacy_half_life = 365.
    return p


def live_row():
    now = datetime.now(timezone.utc)
    return pd.Series({'HomeTeam': 'A', 'AwayTeam': 'B', 'kickoff_utc': (now+timedelta(hours=5)).isoformat(),
        'odds_source': 'The Odds API', 'odds_event_id': 'ev1',
        'live_ref_home_odds': 2.0, 'live_ref_draw_odds': 3.6, 'live_ref_away_odds': 4.0,
        'shadow_pinnacle_totals': {'bookmaker': 'pinnacle', 'event_id': 'ev1', 'over': 1.8, 'under': 2.1,
                                   'updated_at_utc': (now-timedelta(minutes=2)).isoformat()}})


class ProductionProfileTests(OfflineQuotePolicyTestCase):
    def test_shots_are_gated_and_on_by_default(self):
        args = build_parser().parse_args([])
        self.assertFalse(args.no_shot_features)
        self.assertTrue(FootballValuePipelineV2.__init__.__kwdefaults__['shot_features'])
        self.assertTrue(fvp.MODEL_PROFILES[MODEL_VERSION]['shot_features'])
        self.assertIn('shots', MODEL_VERSION)
        prod = dict(market_weight=.7, half_life_days=480, half_life_tuning=False, totals_anchor=True)
        self.assertEqual(model_version_for(**prod, shot_features=False), fvp.NO_SHOTS_MODEL_VERSION)
        self.assertEqual(model_version_for(**prod, shot_features=True), MODEL_VERSION)
        self.assertIn(LEGACY_MODEL_VERSION, fvp.MODEL_PROFILES)

    def test_experimental_profile_keeps_its_identity_without_changing_predictions(self):
        self.assertEqual(SHOT_EXPERIMENT_MODEL_VERSION,
                         'dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-v2')
        self.assertNotEqual(MODEL_VERSION, SHOT_EXPERIMENT_MODEL_VERSION)
        self.assertEqual(fvp.MODEL_PROFILES[MODEL_VERSION],
                         fvp.MODEL_PROFILES[SHOT_EXPERIMENT_MODEL_VERSION])
        self.assertIsNot(fvp.MODEL_PROFILES[MODEL_VERSION],
                         fvp.MODEL_PROFILES[SHOT_EXPERIMENT_MODEL_VERSION])
        settings = fvp.MODEL_PROFILES[SHOT_EXPERIMENT_MODEL_VERSION]
        self.assertEqual(model_version_for(**settings), MODEL_VERSION)
        self.assertEqual(pipe()._model_version(), MODEL_VERSION)

    def test_each_custom_configuration_has_its_own_identity(self):
        base = dict(market_weight=.7, half_life_days=480, half_life_tuning=False, totals_anchor=True, shot_features=False)
        labels = {model_version_for(**{**base, **change}) for change in
                  ({'market_weight': .6}, {'market_weight': .65}, {'half_life_days': 365}, {'totals_anchor': False},
                   {'half_life_tuning': True})}
        self.assertEqual(len(labels), 5)
        self.assertTrue(all(label.startswith(MODEL_VERSION+'+custom-') for label in labels))
        self.assertEqual(model_version_for(**{**base, 'market_weight': .6}),
                         model_version_for(**{**base, 'market_weight': .6}))


class LegacyCompanionTests(OfflineQuotePolicyTestCase):
    def test_legacy_columns_replay_the_old_profile_on_the_same_row(self):
        row = live_row()
        production, _ = pipe()._predict_row(toy_model(), row)
        legacy = pipe()._legacy_columns(toy_model(), row, 'AVAILABLE')
        old = FootballValuePipelineV2.__new__(FootballValuePipelineV2)
        old.market_weight = .5; old.devig_method = 'power'; old.half_life_days = 365.
        expected, _ = old._predict_row(toy_model(), row)
        self.assertEqual(legacy['legacy_model_version'], LEGACY_MODEL_VERSION)
        self.assertEqual(legacy['legacy_half_life_days'], 365.)
        for key in ('p_home', 'p_draw', 'p_away', 'p_over_2_5', 'p_btts_yes'):
            self.assertAlmostEqual(legacy['legacy_'+key], expected[key], places=12)
        self.assertTrue(production['totals_anchor_applied'])
        self.assertNotAlmostEqual(legacy['legacy_p_over_2_5'], production['p_over_2_5'], places=4)
        self.assertNotAlmostEqual(legacy['legacy_p_home'], production['p_home'], places=4)

    def test_unavailable_legacy_model_is_recorded_not_invented(self):
        out = pipe()._legacy_columns(None, live_row(), 'UNAVAILABLE_HALF_LIFE_TUNING_RuntimeError')
        self.assertEqual(out['legacy_status'], 'UNAVAILABLE_HALF_LIFE_TUNING_RuntimeError')
        self.assertIsNone(out['legacy_p_home'])
        p = pipe(); p._legacy_half_life = None
        self.assertEqual(p._fit_legacy_model(pd.DataFrame(), START, None), (None, 'UNAVAILABLE_HALF_LIFE_TUNING'))

    def test_selection_code_never_reads_legacy_columns(self):
        for name in ('conservative_bet_filter.py', 'staking.py', 'asian_handicap.py', 'win_first_shortlist.py',
                     'per_market_shortlist.py', 'no_loss_corners_shortlist.py', 'corners_cards_shortlist.py',
                     'double_chance.py', 'bet365_pinnacle.py'):
            text = Path(name).read_text(encoding='utf-8')
            for column in ('legacy_'+k for k in (*FootballValuePipelineV2.LEGACY_COLUMNS, 'status', 'model_version', 'half_life_days')):
                self.assertNotIn(column, text, name)


class FeatureExclusionTests(OfflineQuotePolicyTestCase):
    class Stub:
        def __init__(self, applied, tag):
            self.applied, self.tag = applied, tag
            self.report = {'status': 'VALIDATED'}
        def apply(self, home, away, base):
            if not self.applied:
                return np.asarray(base), {self.tag+'_applied': False}
            return np.asarray(base)*1.1, {self.tag+'_applied': True}

    def model(self, shots):
        m = toy_model()
        m.shot_features_enabled = True; m.shot_model = self.Stub(shots, 'shot_features')
        m.shot_features_report = {'status': 'VALIDATED'}
        return m

    def test_shot_adjustment_and_its_source_are_logged(self):
        shots = self.model(True).expected_goals('A', 'B')
        self.assertEqual(shots['goal_rate_features_used'], 'shot_features')
        self.assertAlmostEqual(shots['lambda_home'], shots['dc_lambda_home']*1.1, places=12)
        self.assertFalse(any(k.startswith('bbs_') for k in shots))
        self.assertEqual(self.model(False).expected_goals('A', 'B')['goal_rate_features_used'], 'none')


class ValidationCacheTests(OfflineQuotePolicyTestCase):
    def test_component_fingerprints_cover_new_model_files(self):
        from goal_market_validation import validation_code_fingerprint
        from pipeline_health import model_component_hashes
        hashes = model_component_hashes()
        for name in ('shot_features.py', 'historical_benchmark.py', 'bet365_pinnacle.py'):
            self.assertIn(name, hashes)
            original = Path.read_bytes
            def changed(path, name=name):
                data = original(path)
                return data + b'\n# changed' if Path(path).name == name else data
            before = validation_code_fingerprint()
            with patch.object(Path, 'read_bytes', changed):
                self.assertNotEqual(validation_code_fingerprint(), before, name)
                self.assertNotEqual(model_component_hashes()[name], hashes[name])

    def test_anchor_shot_settings_and_code_invalidate_cached_approvals(self):
        from goal_market_validation import MARKETS, VALIDATOR_VERSION, validation_cache_matches, validation_code_fingerprint
        from asian_handicap import LINES, VERSION as AH_VERSION, label
        from win_first_shortlist import VALIDATOR_VERSION as WIN
        config = {'validator_version': VALIDATOR_VERSION, 'training_sha256': 'a'*64,
                  'validation_code_sha256': validation_code_fingerprint(),
                  'model_version': MODEL_VERSION, 'totals_anchor': True, 'shot_features': False}
        lines = {label(s, p): {'status': 'OK'} for s in ('home', 'away') for p in LINES}
        cached = {'config': dict(config), 'markets': {k: {'status': 'OK'} for k in MARKETS},
                  'asian_handicap': {'version': AH_VERSION, 'markets': lines},
                  'asian_handicap_win': {'version': WIN, 'probability_basis': 'net_profit', 'markets': lines}}
        # The cached approval is genuinely reusable before anything changes...
        self.assertTrue(validation_cache_matches(cached, dict(config)))
        # ...and every model setting or code change forces revalidation.
        for change in ({'totals_anchor': False}, {'shot_features': True},
                       {'model_version': fvp.NO_SHOTS_MODEL_VERSION}, {'model_version': MODEL_VERSION+'+custom-abc'}):
            self.assertFalse(validation_cache_matches(cached, {**config, **change}), change)
        original = Path.read_bytes
        for name in ('shot_features.py', 'historical_benchmark.py', 'bet365_pinnacle.py'):
            def changed(path, name=name):
                data = original(path)
                return data + b'\n# changed' if Path(path).name == name else data
            with patch.object(Path, 'read_bytes', changed):
                current = {**config, 'validation_code_sha256': validation_code_fingerprint()}
            self.assertFalse(validation_cache_matches(cached, current), name)

    def test_pipeline_writes_the_settings_into_the_cache_key(self):
        text = Path('football_value_pipeline_v2_standalone.py').read_text(encoding='utf-8')
        key = text[text.index('"validator_version": VALIDATOR_VERSION,'):text.index('"validation_code_sha256": validation_code_fingerprint(),')]
        for field in ('"model_version"', '"totals_anchor"', '"shot_features"', '"market_weight"', '"half_life_days"'):
            self.assertIn(field, key)


class BenchmarkUpgradePathTests(OfflineQuotePolicyTestCase):
    def test_upgrade_variants_run_and_reconcile_on_real_dixon_coles(self):
        rng = np.random.default_rng(3)
        teams = [f'T{i}' for i in range(6)]
        rows = []
        for day, date in enumerate(pd.date_range('2024-01-01', '2025-09-20', freq='3D')):
            h, a = teams[day % 6], teams[(day + 1 + day // 6) % 6]
            if h == a:
                a = teams[(day + 2) % 6]
            rows.append({'Date': date, 'HomeTeam': h, 'AwayTeam': a, 'FTHG': int(rng.poisson(1.5)),
                         'FTAG': int(rng.poisson(1.1)), 'HST': int(rng.integers(2, 8)), 'AST': int(rng.integers(1, 6)),
                         'HS': 12, 'AS': 9, 'PSH': 2.1, 'PSD': 3.4, 'PSA': 3.6, 'P>2.5': 1.9 if day % 2 else None,
                         'P<2.5': 1.95 if day % 2 else None})
        data = pd.DataFrame(rows)
        cfg = json.loads(Path('historical_benchmark_config.json').read_text(encoding='utf-8-sig'))
        cfg.update(leagues=['EPL'], test_start='2025-08-01', audit_start='2025-08-29', test_end_exclusive='2025-09-20',
                   min_train=100, min_development_matches=1, min_audit_matches=1)
        cfg['model_upgrade_comparison']['production_v1']['half_life_tuning'].update(
            candidates=[240., 480.], validation_days=120, step_days=60, min_train=60, min_validation_matches=5)
        records, folds, coverage, errors = hb.evaluate_league(data, 'EPL', cfg)
        self.assertEqual(errors, [])
        variants = {r['variant'] for r in records}
        self.assertTrue(set(hb.UPGRADE_VARIANTS) <= variants)
        statuses = {r['anchor_status'] for r in records if r['variant'] == 'upgrade_pinnacle_ou25_anchor'}
        self.assertEqual(statuses, {'ANCHORED', 'NOT_ANCHORED_NO_PINNACLE_OU25_QUOTE'})
        self.assertTrue(all(f.get('production_v1_tuned_half_life_days') in (240., 480.) for f in folds))
        self.assertTrue(all('shot_gate_fixed_shots' in f for f in folds))
        hb.validate_records(records, folds, cfg)
        upgrade = hb.aggregate(records, cfg)['model_upgrade_comparison']
        one = next(r for r in upgrade['paired'] if r['league'] == 'ALL' and r['market'] == '1x2'
                   and r['variant'] == 'production_v1' and r['phase'] == 'development')
        self.assertGreater(one['n'], 0); self.assertEqual(one['log_loss_gain_vs_production_v1'], 0.)
        self.assertEqual(sum(upgrade['anchor_status_counts']['ALL'].values()),
                         sum(r['variant'] == 'upgrade_pinnacle_ou25_anchor' for r in records))
        with tempfile.TemporaryDirectory() as tmp:
            summary = {'model_upgrade_comparison': upgrade, 'limitations': '', 'evaluated_fixtures': 1,
                       'config': {**cfg, 'baseline_half_life': 240., 'baseline_l2': .08}, 'coverage': {'EPL': coverage},
                       'comparisons': [], 'development_choices': []}
            hb.write_report(Path(tmp), summary, records, folds)
            self.assertIn('Model upgrades versus the production v1 replay', (Path(tmp)/'report.md').read_text(encoding='utf-8'))


if __name__ == '__main__':
    unittest.main()
