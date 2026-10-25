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
import model_comparison as mc
import model_reliability_experiment as mre
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
        self.assertEqual(model_version_for(**prod, shot_features=True), SHOT_EXPERIMENT_MODEL_VERSION)
        self.assertIn(LEGACY_MODEL_VERSION, fvp.MODEL_PROFILES)

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

    def model(self, bbs, shots):
        m = toy_model()
        m.statistics_model = self.Stub(bbs, 'bbs_statistics')
        m.shot_features_enabled = True; m.shot_model = self.Stub(shots, 'shot_features')
        m.shot_features_report = {'status': 'VALIDATED'}
        return m

    def test_bbs_and_shots_never_stack_and_the_source_is_logged(self):
        self.assertFalse(fvp.SHOTS_WITH_BBS_VALIDATED)
        both = self.model(True, True).expected_goals('A', 'B')
        self.assertTrue(both['bbs_statistics_applied'])
        self.assertFalse(both.get('shot_features_applied'))
        self.assertEqual(both['shot_features_status'], 'SKIPPED_BBS_STATISTICS_APPLIED')
        self.assertEqual(both['goal_rate_features_used'], 'bbs_statistics')
        self.assertAlmostEqual(both['lambda_home'], both['dc_lambda_home']*1.1, places=12)
        shots = self.model(False, True).expected_goals('A', 'B')
        self.assertEqual(shots['goal_rate_features_used'], 'shot_features')
        self.assertEqual(self.model(False, False).expected_goals('A', 'B')['goal_rate_features_used'], 'none')


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


class ReliabilityLikeForLikeTests(OfflineQuotePolicyTestCase):
    def production_row(self, anchored=True, features='none'):
        p = pipe()
        pred, _ = p._predict_row(toy_model(), live_row())
        pred.update(league='Premier League', home_team='A', away_team='B', model_home_team='A', model_away_team='B',
                    kickoff_utc=live_row()['kickoff_utc'], goal_rate_features_used=features)
        if not anchored:
            pred.update(totals_anchor_applied=False, totals_anchor_target_over_2_5=None)
        return pred

    class Candidate:
        def __init__(self, **settings):
            self.settings = settings
        def fit(self, history, **kwargs):
            return self
        def score_matrix(self, home, away):
            m = toy_model(); m.attack = np.array([.3, -.25])
            matrix, meta = m.score_matrix('A', 'B')
            self.rho, self.max_goals = m.rho, m.max_goals
            return matrix, meta

    def generate(self, row, half_life=240.):
        history = pd.DataFrame({'Date': pd.to_datetime(['2026-10-01']), 'HomeTeam': ['A'], 'AwayTeam': ['B'],
                                'FTHG': [1], 'FTAG': [0]})
        return mre.generate_league(pd.DataFrame([row]), history, self.Candidate, half_life=half_life, l2=.08, max_goals=10)

    def test_candidate_gets_productions_anchor_so_only_the_factor_differs(self):
        row = self.production_row()
        item = self.generate(row)[0]['candidates']['stronger_l2']
        self.assertEqual(item['status'], 'available', item['reason'])
        self.assertIsNotNone(item['anchor'])
        self.assertAlmostEqual(item['probabilities']['over_2_5'], row['totals_anchor_target_over_2_5'], places=7)
        unanchored = self.generate(self.production_row(anchored=False))[0]['candidates']['stronger_l2']
        self.assertIsNone(unanchored['anchor'])
        self.assertNotAlmostEqual(unanchored['probabilities']['over_2_5'], row['totals_anchor_target_over_2_5'], places=4)
        # Archived reproduction uses the stored anchor inputs.
        self.assertEqual(mre.candidate_probabilities(row, item['raw_matrix'], item['anchor']), item['probabilities'])

    def test_non_comparable_forecasts_are_excluded_with_a_logged_reason(self):
        rows = self.generate(self.production_row(features='bbs_statistics'))
        self.assertEqual(rows[0]['candidates']['stronger_l2']['reason'], 'feature_application_differs')
        adopted = self.generate(self.production_row(), half_life=480.)
        self.assertEqual(adopted[0]['candidates']['fixed_half_life']['status'], 'unavailable')
        self.assertEqual(adopted[0]['candidates']['fixed_half_life']['reason'], 'candidate_equals_production_half_life')
        bad = self.production_row(); bad['totals_anchor_target_over_2_5'] = None
        self.assertEqual(self.generate(bad)[0]['candidates']['stronger_l2']['reason'], 'production_anchor_target_missing')


class ForwardTrialExclusionTests(OfflineQuotePolicyTestCase):
    def test_frozen_basis_trials_name_the_new_model_when_excluding(self):
        import benchmark_forward_experiment as bfe
        reason = f'production_model_{MODEL_VERSION}_outside_frozen_trial_basis'
        self.assertEqual(bfe.production_version_reasons({'model_version': MODEL_VERSION}), [reason])
        for old in ({}, {'model_version': None}, {'model_version': ''}, {'model_version': LEGACY_MODEL_VERSION},
                    {'model_version': float('nan')}):
            self.assertEqual(bfe.production_version_reasons(old), [])
        rows = [{'status': 'unavailable', 'reasons': [reason, 'production_weight_outside_frozen_trial']},
                {'status': 'unavailable', 'reasons': [reason]}, {'status': 'available', 'reasons': []}]
        self.assertEqual(bfe.excluded_reasons(rows), {reason: 2, 'production_weight_outside_frozen_trial': 1})
        r = bfe.load_registry()
        row = {**self.prod(), 'league': r['leagues'][0]}
        decision = bfe.decision(row, r, datetime.now(timezone.utc))
        self.assertIn(reason, decision['reasons']); self.assertEqual(decision['status'], 'unavailable')

    def prod(self):
        pred, _ = pipe()._predict_row(toy_model(), live_row())
        return {**pred, 'kickoff_utc': live_row()['kickoff_utc'], 'home_team': 'A', 'away_team': 'B'}

    def test_totals_trial_records_that_production_adopted_its_candidate(self):
        import totals_anchor_experiment as tae
        r, _ = tae.registry()
        result = tae.decision({**self.prod(), 'league': r['leagues'][0]}, None, None, datetime.now(timezone.utc), r)
        self.assertIn('candidate_adopted_in_production', result['reasons'])
        self.assertIn(f'production_model_{MODEL_VERSION}_outside_frozen_trial_basis', result['reasons'])


def forecast(i, *, legacy=True, version=MODEL_VERSION):
    from asian_handicap import margins
    kick = START + timedelta(days=i//7, hours=i % 7)
    model = toy_model()
    matrix, _ = model.score_matrix('A', 'B')
    prob = DixonColesModel.one_x_two(matrix)
    row = {'league': 'Premier League', 'home_team': f'Team{i}A FC', 'away_team': f'Team{i}B FC',
           'kickoff_utc': kick.isoformat(), 'odds_event_id': f'e{i}', 'model_version': version,
           'p_home': prob['home'], 'p_draw': prob['draw'], 'p_away': prob['away'],
           **{('p_'+k): v for k, v in hb.goals(matrix).items()}, 'goal_margin_distribution': margins(matrix)}
    if legacy:
        row.update({'legacy_model_version': LEGACY_MODEL_VERSION, 'legacy_status': 'AVAILABLE',
                    'legacy_p_home': .4, 'legacy_p_draw': .3, 'legacy_p_away': .3,
                    **{'legacy_p_'+k: .5 for k in mc.BINARY}, 'legacy_goal_margin_distribution': margins(matrix)})
    return row


def record(i, h=2, a=1):
    kick = START + timedelta(days=i//7, hours=i % 7)
    return verified_record('PL', {'id': 1000+i, 'utcDate': kick.isoformat(), 'status': 'FINISHED',
        'homeTeam': {'name': f'Team{i}A FC'}, 'awayTeam': {'name': f'Team{i}B FC'},
        'score': {'duration': 'REGULAR', 'fullTime': {'home': h, 'away': a}, 'regularTime': {'home': h, 'away': a}}})


def archive(*snapshots):
    return [({'git_commit_sha': f'{n:040x}', 'captured_at_utc': (START-timedelta(hours=1-n/100)).isoformat(),
              'generated_at_utc': (START-timedelta(hours=1-n/100)).isoformat()}, rows, [])
            for n, rows in enumerate(snapshots)]


class ModelComparisonTests(OfflineQuotePolicyTestCase):
    def evaluate(self, snaps, n, clock=None):
        with tempfile.TemporaryDirectory() as tmp:
            return mc.evaluate(Path(tmp), archive(*snaps), [record(i) for i in range(n)],
                               clock or START+timedelta(days=60))

    def test_collect_more_data_until_300_matches_over_six_weeks(self):
        summary, paired = self.evaluate([[forecast(i) for i in range(299)]], 299)
        self.assertEqual(summary['status'], 'COLLECT_MORE_DATA'); self.assertEqual(summary['paired_matches'], 299)
        summary, _ = self.evaluate([[forecast(i) for i in range(300)]], 300)
        self.assertEqual(summary['status'], 'READY_FOR_REVIEW'); self.assertGreaterEqual(summary['weeks'], 6)
        self.assertFalse(summary['automatic_production_change'])
        short = [forecast(i) for i in range(300)]
        for i, row in enumerate(short):  # 300 matches squeezed into five weeks
            row['kickoff_utc'] = (START+timedelta(days=i % 35, minutes=i)).isoformat()
        records = [verified_record('PL', {**{'id': 2000+i, 'utcDate': r['kickoff_utc'], 'status': 'FINISHED'},
            'homeTeam': {'name': r['home_team']}, 'awayTeam': {'name': r['away_team']},
            'score': {'duration': 'REGULAR', 'fullTime': {'home': 1, 'away': 0}, 'regularTime': {'home': 1, 'away': 0}}})
            for i, r in enumerate(short)]
        with tempfile.TemporaryDirectory() as tmp:
            summary, _ = mc.evaluate(Path(tmp), archive(short), records, START+timedelta(days=60))
        self.assertEqual(summary['paired_matches'], 300); self.assertLess(summary['weeks'], 6)
        self.assertEqual(summary['status'], 'COLLECT_MORE_DATA')

    def test_only_the_first_eligible_forecast_counts_without_backfill(self):
        first = [forecast(0, legacy=False), forecast(1)]
        later = [forecast(0), forecast(1, version=MODEL_VERSION+'+custom-x')]
        summary, paired = self.evaluate([first, later], 2)
        self.assertEqual(summary['paired_matches'], 1)
        self.assertEqual(summary['excluded_fixtures'], {'first_forecast_without_legacy_model': 1})
        self.assertEqual(paired[0]['snapshot_commit'], f'{0:040x}')
        summary, _ = self.evaluate([[forecast(0, version='custom'), {**forecast(1), 'legacy_status': 'UNAVAILABLE_FIT_RuntimeError'}]], 2)
        self.assertEqual(summary['excluded_fixtures'], {'first_forecast_not_production_custom': 1,
                                                        'legacy_unavailable_fit_runtimeerror': 1})

    def test_scores_both_models_on_the_same_matches(self):
        summary, paired = self.evaluate([[forecast(i) for i in range(3)]], 3)
        table = {(t['league'], t['market']): t for t in summary['tables']}
        one = table[('ALL', '1x2')]
        self.assertEqual(one['matches'], 3)
        self.assertAlmostEqual(one['legacy']['log_loss'], -np.log(.4), places=12)
        self.assertAlmostEqual(one['production']['log_loss'], -np.log(paired[0]['production']['p_home']), places=12)
        self.assertEqual(set(summary['markets']), {'1x2', *mc.BINARY, *hb.AH})
        self.assertEqual(table[('Premier League', 'ah_home_-1.5')]['matches'], 3)
        self.assertEqual(table[('ALL', 'ah_home_-1.0')]['matches'], 0)  # 2-1 margin refunds at -1
        pending, _ = self.evaluate([[forecast(i) for i in range(3)]], 3, clock=START)
        self.assertEqual(pending['excluded_fixtures'], {'pending_or_unverified_result': 3})

    def test_distance_to_pinnacle_closing_probabilities(self):
        from asian_handicap import label
        row = forecast(0)
        obs = {'fixture': {k: row[k] for k in ('league', 'home_team', 'away_team', 'kickoff_utc', 'odds_event_id')},
               'observed_at_utc': row['kickoff_utc'],
               'quotes': [{'bookmaker': 'pinnacle', 'selection': k, 'fair_probability': v, 'decimal_odds': 2.}
                          for k, v in (('home', .5), ('draw', .3), ('away', .2), ('over_2_5', .55))]
                         + [{'bookmaker': 'pinnacle', 'selection': label('home', -1.5), 'fair_probability': None, 'decimal_odds': 3.},
                            {'bookmaker': 'pinnacle', 'selection': label('away', 1.5), 'fair_probability': None, 'decimal_odds': 1.4}]}
        close = mc.pinnacle_closing([obs], row)
        self.assertAlmostEqual(mc.distance({'p_home': .4, 'p_draw': .3, 'p_away': .3}, close, '1x2'), .1)
        self.assertAlmostEqual(mc.distance({'over_2_5': .5}, close, 'over_2_5'), .05)
        self.assertIsNone(mc.distance({'btts_yes': .5}, close, 'btts_yes'))
        self.assertAlmostEqual(close['ah_home_-1.5'], fvp.devig([3., 1.4], 'power')[0], places=12)
        self.assertIsNone(mc.pinnacle_closing([], row))

    def test_review_writes_report_and_reconciles(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            snaps = archive([forecast(i) for i in range(4)])
            records = [record(i) for i in range(4)]
            summary = mc.review(root, snaps, records, START+timedelta(days=60))
            report = (root/'performance/model_comparison/report.md').read_text(encoding='utf-8')
            self.assertIn('COLLECT_MORE_DATA', report)
            self.assertIn(MODEL_VERSION, report); self.assertIn(LEGACY_MODEL_VERSION, report)
            data = json.loads((root/'performance/model_comparison/summary.json').read_text(encoding='utf-8'))
            self.assertEqual(data['paired_matches'], 4)
            with patch('performance_tracking.snapshots', return_value=snaps), \
                    patch('performance_tracking.load_json', side_effect=lambda p, d: data if p.name == 'summary.json'
                          else {str(i): r for i, r in enumerate(records)} if p.name == 'verified_results.json'
                          else json.loads(p.read_text(encoding='utf-8'))):
                self.assertTrue(mc.validate_report(root))


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
