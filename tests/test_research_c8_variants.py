"""C8 variants (docs/plan.md, Phase 2g, "Penalty and season carry-over on top of C8"): the season carry-over of
the Dixon-Coles fit, the harness variants' goal rates and plumbing, and the report's choice rule. DixonColesModel's
defaults, every other candidate and a plain run are unchanged."""
import inspect
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest import mock
from unittest.mock import patch

import numpy as np
import pandas as pd

import evaluation_harness as eh
import football_value_pipeline_v2_standalone as fvp
from football_value_pipeline_v2_standalone import DixonColesModel, season_carry_over_multipliers
from tests import epl_research_rows as epl
import research_low_score as rls
import research_rate_calibration as rrc

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / 'scripts'))
import c8_variants_report as report  # noqa: E402

CFG = json.loads((REPO / 'evaluation_harness_config.json').read_text(encoding='utf-8'))
SINGLES = {'C8P1': {'l2': 1.}, 'C8P3': {'l2': 3.}, 'C8S70': {'season_carry_over': .7}, 'C8S50': {'season_carry_over': .5}}
RESULTS = ('FTHG', 'FTAG', 'FTR', 'HTHG', 'HTAG', 'HTR', 'HS', 'AS', 'HST', 'AST', 'HF', 'AF', 'HC', 'AC',
           'HY', 'AY', 'HR', 'AR')


def seasons(count=3, teams='ABCDEF', seed=5):
    """`count` double round-robin seasons (August to May, weekly rounds) with a summer gap between them."""
    rng = np.random.default_rng(seed)
    strength = dict(zip(teams, np.linspace(.5, -.5, len(teams))))
    rows = []
    for season in range(count):
        day = pd.Timestamp(2021 + season, 8, 7)
        for home in teams:
            for away in teams:
                if home != away:
                    rows.append({'Date': day, 'HomeTeam': home, 'AwayTeam': away,
                                 'FTHG': rng.poisson(np.exp(.3 + strength[home] - strength[away])),
                                 'FTAG': rng.poisson(np.exp(strength[away] - strength[home]))})
                    day += pd.Timedelta(days=9)
    return pd.DataFrame(rows)


class SeasonCarryOverTest(unittest.TestCase):
    DATES = pd.to_datetime(['2022-05-20', '2022-08-06', '2022-11-12', '2023-01-21', '2023-05-27', '2023-08-12'])

    def test_defaults_are_unchanged(self):
        defaults = {k: p.default for k, p in inspect.signature(DixonColesModel.__init__).parameters.items() if k != 'self'}
        self.assertEqual(defaults, {'half_life_days': 240.0, 'l2': 0.08, 'max_goals': 10,
                                    'shot_features': False, 'season_carry_over': 1.0})
        self.assertEqual(CFG['baseline_l2'], .08)
        self.assertEqual(fvp.SEASON_GAP_DAYS, 45)

    def test_earlier_seasons_are_scaled_once_per_summer_gap(self):
        got = season_carry_over_multipliers(self.DATES, pd.Timestamp('2023-08-14'), .7)
        # Two summers back, one summer back (the 70-day winter break of 2022 is not a summer gap), this season.
        np.testing.assert_allclose(got, [.49, .7, .7, .7, .7, 1.])
        shuffled = self.DATES[[5, 0, 3, 1, 4, 2]]
        np.testing.assert_allclose(season_carry_over_multipliers(shuffled, pd.Timestamp('2023-08-14'), .5),
                                   [1., .25, .5, .5, .5, .5])

    def test_the_gap_before_the_fit_date_counts(self):
        earlier = self.DATES[:5]
        # A new season's first forecasts: 65 days after the last match, across 1 July.
        np.testing.assert_allclose(season_carry_over_multipliers(earlier, pd.Timestamp('2023-07-31'), .7),
                                   [.49, .7, .7, .7, .7])
        # 24 days after the last match, and 39 days across 1 July: no summer gap yet.
        for reference in ('2023-06-20', '2023-07-05'):
            np.testing.assert_allclose(season_carry_over_multipliers(earlier, pd.Timestamp(reference), .7),
                                       [.7, 1., 1., 1., 1.])

    def test_only_a_gap_of_45_days_across_1_july_is_a_summer_gap(self):
        scale = lambda first, second: season_carry_over_multipliers(
            pd.to_datetime([first, second]), pd.Timestamp(second), .5)[0]
        self.assertEqual(scale('2023-05-28', '2023-08-11'), .5)
        self.assertEqual(scale('2023-06-07', '2023-07-22'), .5)   # exactly 45 days
        self.assertEqual(scale('2023-06-07', '2023-07-21'), 1.)   # 44 days
        self.assertEqual(scale('2022-11-13', '2023-01-20'), 1.)   # the 2022 World Cup break, 68 days
        self.assertEqual(scale('2023-07-02', '2023-09-30'), 1.)   # 90 days, but no 1 July inside
        self.assertEqual(scale('2023-06-30', '2023-09-01'), .5)
        self.assertEqual(scale('2026-01-15', '2026-10-11'), .5)   # the holdout hole in a locked run's history

    def test_a_default_fit_never_computes_the_multipliers(self):
        history = seasons()
        with patch.object(fvp, 'season_carry_over_multipliers', side_effect=AssertionError('default fit scaled')):
            model = DixonColesModel().fit(history)
            self.assertEqual(model.season_carry_over, 1.)
            with self.assertRaises(AssertionError):
                DixonColesModel(season_carry_over=.7).fit(history)

    def test_the_carried_fit_is_the_default_fit_on_weights_one_half_life_older_per_summer(self):
        history = seasons()
        as_of = history.Date.max() + pd.Timedelta(days=3)
        carried = DixonColesModel(half_life_days=480., season_carry_over=.5).fit(history, as_of=as_of)
        # Halving a weight is ageing the match by one half-life: move each earlier season back 480 days per summer.
        summers = np.round(-np.log2(season_carry_over_multipliers(history.Date, as_of, .5))).astype(int)
        self.assertEqual(sorted(set(summers)), [0, 1, 2])
        aged = history.assign(Date=history.Date - pd.to_timedelta(480 * summers, unit='D'))
        plain = DixonColesModel(half_life_days=480.).fit(aged, as_of=as_of)
        for name in ('attack', 'weakness'):
            np.testing.assert_allclose(getattr(carried, name), getattr(plain, name), atol=2e-4)
        for name in ('base', 'home_adv', 'rho'):
            self.assertAlmostEqual(getattr(carried, name), getattr(plain, name), places=3)
        default = DixonColesModel(half_life_days=480.).fit(history, as_of=as_of)
        self.assertGreater(np.abs(carried.attack - default.attack).max(), 1e-3)

    def test_a_larger_penalty_pulls_team_strengths_together(self):
        history = seasons()
        spread = [float(np.square(DixonColesModel(l2=l2).fit(history).attack).sum())
                  for l2 in (.08, 1., 3.)]
        self.assertGreater(spread[0], spread[1])
        self.assertGreater(spread[1], spread[2])

    def test_invalid_carry_over_is_refused(self):
        for value in (0., -.5, 1.5, float('nan')):
            with self.assertRaises(ValueError):
                DixonColesModel(season_carry_over=value)

    def test_the_shot_gate_baselines_are_fitted_with_the_same_settings(self):
        train, _ = epl.scored_fold()
        fitted, fit = [], DixonColesModel.fit

        def recorded(model, *args, **kwargs):
            fitted.append((model.l2, model.season_carry_over))
            return fit(model, *args, **kwargs)

        with patch.object(DixonColesModel, 'fit', recorded):
            eh.fold_model(train, epl.ORIGIN, CFG, l2=1., season_carry_over=.7)
        self.assertGreater(len(fitted), 5)  # the fold model and the shot gate's walk-forward baselines
        self.assertEqual(set(fitted), {(1., .7)})


class VariantRegistryTest(unittest.TestCase):
    def test_variants_are_the_declared_settings(self):
        self.assertEqual({k: v for k, v in eh.RATE_VARIANTS.items() if len(v) == 1}, SINGLES)
        pairs = {k: v for k, v in eh.RATE_VARIANTS.items() if len(v) == 2}
        self.assertEqual(pairs, {'C8P1S70': {'l2': 1., 'season_carry_over': .7}, 'C8P1S50': {'l2': 1., 'season_carry_over': .5},
                                 'C8P3S70': {'l2': 3., 'season_carry_over': .7}, 'C8P3S50': {'l2': 3., 'season_carry_over': .5}})
        self.assertEqual(len(eh.RATE_VARIANTS), 8)
        self.assertTrue(set(eh.RATE_VARIANTS) <= eh.WALK_FORWARD_CANDIDATES)

    def test_no_variant_is_registered_so_none_can_be_declared(self):
        self.assertFalse(set(eh.RATE_VARIANTS) & set(eh.CANDIDATES))
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'declaration.json'
            for name in eh.RATE_VARIANTS:
                path.write_text(json.dumps({
                    'candidate': name, 'baseline': 'C8', 'primary_metric': 'AH all',
                    'draw_sensitive_lines': [-0.5, 0, 0.5], 'declared_by': 'test', 'declared_at': '2026-11-17',
                    'calibration_tolerance': CFG['calibration_tolerance']['name']}), encoding='utf-8')
                with self.assertRaises(ValueError):
                    eh.validate_declaration(path, CFG, {'sha256': 'a' * 64}, Path(tmp) / 'ledger.json')

    def test_rate_variants_are_refused_outside_a_locked_historical_run(self):
        with tempfile.TemporaryDirectory() as tmp:
            for extra in (['--mode', 'european'], ['--declaration', str(Path(tmp) / 'd.json')]):
                with self.assertRaises(ValueError):
                    eh.main(['--output', tmp, '--rate-variants', 'C8P1', *extra])

    def test_the_default_fold_model_is_the_fit_every_candidate_read_before(self):
        train, model = epl.scored_fold()
        again = eh.fold_model(train, epl.ORIGIN, CFG)
        for name in ('attack', 'weakness'):
            np.testing.assert_array_equal(getattr(again, name), getattr(model, name))
        self.assertEqual((again.base, again.home_adv, again.rho, again.l2, again.season_carry_over),
                         (model.base, model.home_adv, model.rho, .08, 1.))


class VariantRatesTest(unittest.TestCase):
    """variant_base_rates on real Eredivisie folds across the holdout start (16 Jan 2026), as the harness lock
    test: the same folds and matches as evaluate_league, results and dates only, no holdout result."""

    @classmethod
    def setUpClass(cls):
        cls.cfg = {**CFG, 'test_start': '2026-01-05', 'end_exclusive': '2026-01-19', 'seasons': ['2324', '2425', '2526']}
        cls.cache = str(REPO / '.football_cache')
        cls.load = eh.hb.load_history

        def without_holdout_results(cache_dir, league, load_cfg):
            data, sources, extra = cls.load(cache_dir, league, load_cfg)
            locked = data.Date.map(lambda d: eh.phase(d, league, cls.cfg) == 'holdout')
            data = data.copy()
            data.loc[locked, [c for c in RESULTS if c in data]] = np.nan
            return data, sources, extra

        cls.blanked = staticmethod(without_holdout_results)
        cls.enterClassContext(patch.dict(eh.RATE_VARIANTS, {'SAME': {}}))
        with mock.patch.object(eh.hb, 'load_history', without_holdout_results):
            cls.research = eh.evaluate_league('Eredivisie', cls.cache, cls.cfg, False, keep={'C', 'C0', 'C8'})[6]
            cls.rates = {name: eh.variant_base_rates('Eredivisie', cls.cache, cls.cfg, False, name)
                         for name in ('SAME', 'C8P3', 'C8S50')}

    def changed(self, change, name='C8S50'):
        def loader(cache_dir, league, load_cfg):
            data, sources, extra = self.blanked(cache_dir, league, load_cfg)
            return change(data.copy()), sources, extra
        with mock.patch.object(eh.hb, 'load_history', loader):
            return eh.variant_base_rates('Eredivisie', self.cache, self.cfg, False, name)

    def test_unchanged_settings_give_c0s_goal_rates_for_exactly_the_research_rows(self):
        self.assertTrue(self.research)
        self.assertEqual({r['fixture_key'] for r in self.research}, set(self.rates['SAME']))
        self.assertEqual({r['fixture_key']: r['base_rates'] for r in self.research}, self.rates['SAME'])
        self.assertTrue(all(r['fixture_key'] == r['identity']['fixture_key'] for r in self.research))

    def test_each_setting_moves_the_goal_rates(self):
        for name in ('C8P3', 'C8S50'):
            self.assertEqual(set(self.rates[name]), set(self.rates['SAME']))
            moved = [abs(a - b) for key, pair in self.rates[name].items() for a, b in zip(pair, self.rates['SAME'][key])]
            self.assertGreater(min(moved), 0.)
        # The larger penalty pulls the two sides' rates together on average.
        gap = lambda rates: np.mean([abs(np.log(h / a)) for h, a in rates.values()])
        self.assertLess(gap(self.rates['C8P3']), gap(self.rates['SAME']))

    def test_a_locked_run_forecasts_no_holdout_match_and_a_holdout_run_does(self):
        phases = lambda rates: {eh.phase(pd.Timestamp(key.split('|')[1]), 'Eredivisie', self.cfg) for key in rates}
        self.assertEqual(phases(self.rates['C8S50']), {'validation'})
        with mock.patch.object(eh.hb, 'load_history', self.blanked):
            unlocked = eh.variant_base_rates('Eredivisie', self.cache, self.cfg, True, 'C8S50')
        self.assertEqual(phases(unlocked), {'validation', 'holdout'})
        self.assertEqual({k: v for k, v in unlocked.items() if k in self.rates['C8S50']}, self.rates['C8S50'])

    def test_no_price_reaches_the_goal_rates(self):
        def shake(data):
            odds = [c for c in data.columns if c.startswith(epl.ODDS_PREFIXES) and c not in ('AHh', 'AHCh')]
            self.assertGreater(len(odds), 20)
            data[odds] = data[odds].apply(pd.to_numeric, errors='coerce') * 1.02 + .01
            return data
        self.assertEqual(self.changed(shake), self.rates['C8S50'])

    def test_a_later_result_never_changes_an_earlier_forecast_and_an_earlier_one_does(self):
        # The locked run's forecasts all belong to the fold of 5 Jan 2026 (the next window is the holdout's).
        origin = eh.fold_windows(self.cfg, pd.Timestamp(self.cfg['end_exclusive']))[0][0]
        self.assertTrue(all(pd.Timestamp(k.split('|')[1]) >= origin for k in self.rates['C8S50']))

        def flip_from(start):
            def change(data):
                played = (data.Date >= start) & data.FTHG.notna()
                self.assertTrue(played.any())
                data.loc[played, ['FTHG', 'FTAG']] = [0, 7]
                return data
            return change

        # The forecast matches' own results, and everything after the origin, never reach the fit.
        self.assertEqual(self.changed(flip_from(origin)), self.rates['C8S50'])
        self.assertNotEqual(self.changed(flip_from(origin - pd.Timedelta(days=60))), self.rates['C8S50'])


class InlinePool:
    """ProcessPoolExecutor's interface, run in the calling process."""
    def __init__(self, max_workers=None):
        pass

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        return False

    def submit(self, function, *args):
        future = mock.Mock()
        future.result.return_value = function(*args)
        return future


class HistoricalPlumbingTest(unittest.TestCase):
    """historical(): variants are fitted only when asked, each scored as C8 is on its own goal rates."""
    N, MIN_MATCHES = 1200, 400

    @classmethod
    def setUpClass(cls):
        cls.enterClassContext(patch.object(rls, 'MIN_MATCHES', cls.MIN_MATCHES))
        cls.enterClassContext(patch.object(rrc, 'MIN_MATCHES', cls.MIN_MATCHES))
        rng = np.random.default_rng(11)
        start = pd.Timestamp(CFG['test_start'])
        cls.rows = []
        for i in range(cls.N):
            rates = [float(rng.uniform(.7, 2.4)), float(rng.uniform(.5, 2.))]
            row = epl.research_row('EPL', start + pd.Timedelta(hours=8 * i), rates, rng.poisson(rates[0]),
                                   rng.poisson(rates[1]), base_rates=rates, elo_z=float(rng.normal(.1, .3)))
            cls.rows.append({**row, 'fixture_key': row['identity']['fixture_key']})
        cls.cfg = {**CFG, 'end_exclusive': str((cls.rows[-1]['date'] + pd.Timedelta(days=1)).date())}
        cls.shrunk = {r['fixture_key']: [float(np.sqrt(v)) for v in r['base_rates']] for r in cls.rows}

    def run_historical(self, **kwargs):
        calls = []

        def league(name, cache, cfg, include_holdout, keep):
            calls.append(('league', name))
            return [], [], {}, [], [], [], [dict(r) for r in self.rows]

        def variant(name, cache, cfg, include_holdout, variant_name):
            calls.append(('variant', name, variant_name))
            same = variant_name == 'SAME'
            return {r['fixture_key']: (r['base_rates'] if same else self.shrunk[r['fixture_key']]) for r in self.rows}

        with patch.object(eh, 'ProcessPoolExecutor', InlinePool), patch.object(eh, 'evaluate_league', league), \
                patch.object(eh, 'variant_base_rates', variant), patch.dict(eh.RATE_VARIANTS, {'SAME': {}}):
            return eh.historical('cache', self.cfg, leagues=['EPL'], **kwargs), calls

    def test_a_plain_run_fits_no_variant_and_is_unchanged_by_asking_for_them(self):
        (plain, calls) = self.run_historical()
        self.assertEqual(calls, [('league', 'EPL')])
        (asked, calls) = self.run_historical(variants=['C8P1', 'SAME'])
        self.assertEqual(calls, [('league', 'EPL'), ('variant', 'EPL', 'C8P1'), ('variant', 'EPL', 'SAME')])
        records, folds, coverage, _, _, calib = plain
        new = {'C8P1', 'SAME'}
        self.assertEqual([r for r in asked[0] if r['candidate'] not in new], records)
        self.assertEqual([r for r in asked[5] if r['candidate'] not in new], calib)
        self.assertEqual([f for f in asked[1] if f.get('candidate') not in new], folds)
        self.assertEqual({k: v for k, v in asked[2].items() if k.split(':')[1] not in new}, dict(coverage))
        self.assertFalse(new & {r['candidate'] for r in records})

    def test_a_variant_is_c8s_procedure_on_its_own_goal_rates(self):
        (records, folds, _, _, _, calib), _ = self.run_historical(variants=['C8P1', 'SAME'])
        of = lambda name: [{**r, 'candidate': 'x'} for r in records if r['candidate'] == name]
        self.assertTrue(of('C8'))
        self.assertEqual(of('SAME'), of('C8'))  # unchanged goal rates: C8 exactly, calibration with Elo included
        self.assertNotEqual(of('C8P1'), of('C8'))
        fits = {f['candidate']: f for f in folds if f.get('candidate')}
        self.assertEqual(fits['SAME']['walk_forward_fits'], fits['C8']['walk_forward_fits'])
        self.assertEqual(fits['C8P1']['settings'], {'l2': 1.})
        last = fits['C8P1']['walk_forward_fits'][-1]
        self.assertEqual((last['status'], last['elo'], last['low_score']['status']), ('fitted', True, 'fitted'))
        self.assertNotEqual(last['c'], 0.)
        # The refit sees the variant's rates: square-rooted rates are calibrated back with b near 2.
        self.assertGreater(last['b'], 1.5)
        direct = eh.rate_calibration_candidate(eh.with_variant_rates(self.rows, self.shrunk, 'C8P1'), self.cfg,
                                               pd.Timestamp(self.cfg['end_exclusive']), 'C8P1')
        self.assertEqual([r for r in records if r['candidate'] == 'C8P1'], direct[0])

    def test_a_declared_variant_is_fitted_without_being_asked_for(self):
        with patch.dict(eh.CANDIDATES, {'C8P1': 'registered for this test'}):
            _, calls = self.run_historical(keep={'C8P1', 'C8', 'M'})
        self.assertEqual(calls, [('league', 'EPL'), ('variant', 'EPL', 'C8P1')])

    def test_a_research_row_without_the_variants_rates_is_an_error(self):
        rates = dict(self.shrunk)
        rates.pop(self.rows[7]['fixture_key'])
        with self.assertRaisesRegex(ValueError, 'no goal rates for 1 research rows'):
            eh.with_variant_rates(self.rows, rates, 'C8P1')

    def test_goals_file_carries_the_grids_expected_goals_and_the_score(self):
        (_, _, _, _, _, calib), _ = self.run_historical(variants=['C8P1'])
        frame = eh.rate_goals_frame(calib)
        self.assertEqual(list(frame.columns), eh.RATE_GOALS_COLUMNS)
        self.assertEqual(set(frame.candidate), {'C7', 'C8', 'C8P1'})
        self.assertEqual(len(frame), 3 * self.N)
        first = frame[frame.candidate == 'C8'].iloc[0]  # a warm-up forecast: C0's grid on the row's own rates
        row = next(r for r in self.rows if r['fixture_key'] == first.fixture_key)
        self.assertAlmostEqual(first.expected_home_goals, row['base_rates'][0], places=3)
        self.assertAlmostEqual(first.expected_away_goals, row['base_rates'][1], places=3)
        self.assertEqual((first.home_goals, first.away_goals), (row['home_goals'], row['away_goals']))
        grid = np.zeros((4, 4))
        grid[3, 1] = 1.
        self.assertEqual(eh.expected_goals(grid), [3., 1.])


def paired(gain, low, high=None):
    return {'mean_gain': gain, 'interval_95': [low, gain + (gain - low) if high is None else high],
            'clear_of_zero': low > 0, 'fixtures': 100, 'weeks': 10}


def choice_report(development, validation, passes):
    """The part of the report choose() reads: C8 minus variant on AH all lines and development calibration."""
    return {'development': {'log_loss': {'AH all': {'c8_minus': development}},
                            'calibration': {n: {'v2': {'passes': passes.get(n, True), 'slopes': {'home': 1., 'away': 1.}}}
                                            for n in development}},
            'validation': {'log_loss': {'AH all': {'c8_minus': validation}}}}


class ChoiceRuleTest(unittest.TestCase):
    def choose(self, development, validation, passes=None):
        variants = {name: eh.RATE_VARIANTS[name] for name in development}
        return report.choose(choice_report(development, validation, passes or {}), variants)

    def test_kinds(self):
        self.assertEqual(report.kind({'l2': 1.}), 'penalty')
        self.assertEqual(report.kind({'season_carry_over': .7}), 'season carry-over')
        self.assertIsNone(report.kind({'l2': 1., 'season_carry_over': .7}))

    def test_c8_stands_when_no_variant_meets_all_three_conditions(self):
        development = {'C8P1': paired(.002, -.001), 'C8P3': paired(.003, .001), 'C8S70': paired(.004, .002),
                       'C8S50': paired(-.002, -.003, -.001)}
        validation = {'C8P1': paired(.001, -.002), 'C8P3': paired(-.0001, -.003), 'C8S70': paired(.001, -.002),
                      'C8S50': paired(.002, -.001)}
        out = self.choose(development, validation, {'C8S70': False})
        self.assertEqual(out['final_candidate'], 'C8')
        self.assertIsNone(out['combination'])
        conditions = {n: v['conditions'] for n, v in out['verdicts'].items()}
        self.assertFalse(conditions['C8P1']['development_ah_all_positive_and_clear'])   # interval spans zero
        self.assertFalse(conditions['C8P3']['validation_ah_all_not_negative'])
        self.assertFalse(conditions['C8S70']['development_calibration_v2_passes'])
        self.assertFalse(conditions['C8S50']['development_ah_all_positive_and_clear'])  # clear, but worse
        self.assertFalse(any(v['qualifies'] for v in out['verdicts'].values()))

    def test_a_validation_estimate_of_exactly_zero_is_not_negative(self):
        out = self.choose({'C8P1': paired(.002, .001)}, {'C8P1': paired(0., -.002)})
        self.assertTrue(out['verdicts']['C8P1']['qualifies'])
        self.assertEqual(out['final_candidate'], 'C8P1')

    def test_one_kind_qualifying_names_no_combination(self):
        development = {'C8P1': paired(.002, .001), 'C8P3': paired(.003, .001), 'C8S70': paired(.001, -.001),
                       'C8S50': paired(.001, -.001)}
        out = self.choose(development, {n: paired(.001, -.002) for n in development})
        self.assertIsNone(out['combination'])
        self.assertEqual(out['best_qualifying_setting'], {'penalty': 'C8P3', 'season carry-over': None})
        self.assertEqual(out['final_candidate'], 'C8P3')  # the larger development gain of the two

    def test_a_setting_of_each_kind_qualifying_names_their_pair_and_waits_for_it(self):
        development = {'C8P1': paired(.003, .001), 'C8P3': paired(.002, .001), 'C8S70': paired(.001, .0005),
                       'C8S50': paired(.004, .001)}
        validation = {n: paired(.001, -.002) for n in development}
        out = self.choose(development, validation)
        self.assertEqual((out['combination'], out['combination_in_run']), ('C8P1S50', False))
        self.assertIsNone(out['final_candidate'])
        # With the pair in the run: the qualifying variant with the largest development gain wins.
        for gain, low, final in ((.005, .002, 'C8P1S50'), (.0035, .001, 'C8S50'), (.009, -.001, 'C8S50')):
            both = self.choose({**development, 'C8P1S50': paired(gain, low)},
                               {**validation, 'C8P1S50': paired(.001, -.001)})
            self.assertEqual((both['combination'], both['combination_in_run']), ('C8P1S50', True))
            self.assertEqual(both['final_candidate'], final)

    def test_a_pair_the_rule_did_not_name_is_never_chosen(self):
        development = {'C8P1': paired(.003, .001), 'C8P3': paired(.002, -.001), 'C8S70': paired(.001, -.001),
                       'C8S50': paired(.001, -.001), 'C8P3S50': paired(.02, .01)}
        out = self.choose(development, {n: paired(.001, -.002) for n in development})
        self.assertIsNone(out['combination'])
        self.assertEqual(out['final_candidate'], 'C8P1')


class GoalsTableTest(unittest.TestCase):
    def test_predicted_and_actual_goals_follow_the_markets_favourite(self):
        import evaluation_diagnostics as ed
        keys = pd.Index(['a', 'b', 'c', 'd'], name='fixture_key')
        members = pd.DataFrame({'phase': 'development', 'league': 'EPL', 'week': ['w1', 'w1', 'w2', 'w2']}, index=keys)
        market = [(.80, .12, .08), (.20, .25, .55), (.50, .27, .23), (.30, .30, .40)]  # favourite: home, away, home, away
        forecasts = pd.DataFrame([{'phase': 'development', 'league': 'EPL', 'fixture_key': k, 'candidate': 'M',
                                   'outcome': 0, 'p_home': h, 'p_draw': d, 'p_away': a}
                                  for k, (h, d, a) in zip(keys, market)])
        labels = pd.DataFrame({'favourite market probability': [ed.favourite_band(max(h, a)) for h, _, a in market]},
                              index=keys)
        goals = pd.DataFrame([{'phase': 'development', 'league': 'EPL', 'fixture_key': k, 'candidate': 'C8',
                               'expected_home_goals': eh_, 'expected_away_goals': ea, 'home_goals': hg, 'away_goals': ag}
                              for k, (eh_, ea, hg, ag) in zip(keys, [(2.5, .5, 3, 0), (1., 2., 0, 1), (1.6, 1., 2, 2),
                                                                     (1.1, 1.3, 1, 1)])])
        rows = {r['band']: r for r in report.goals_by_favourite(goals, labels, forecasts, members, keys, ('C8',))}
        self.assertEqual([rows[b]['fixtures'] for b in ('all', 'under 45%', '45-60%', '60-75%', '75%+')], [4, 1, 2, 0, 1])
        top = rows['75%+']['views']['C8']
        self.assertEqual((top['predicted'], top['actual']), ({'favourite': 2.5, 'underdog': .5},
                                                              {'favourite': 3., 'underdog': 0.}))
        self.assertAlmostEqual(top['predicted_minus_actual']['supremacy']['mean'], -1.)
        middle = rows['45-60%']['views']['C8']  # b: the away side is the favourite; c: the home side
        self.assertAlmostEqual(middle['predicted']['favourite'], (2. + 1.6) / 2)
        self.assertAlmostEqual(middle['actual']['underdog'], (0 + 2) / 2)
        everything = rows['all']['views']['C8']['predicted_minus_actual']
        self.assertAlmostEqual(everything['total']['mean'], ((3. - 3) + (3. - 1) + (2.6 - 4) + (2.4 - 2)) / 4)
        self.assertIsNone(rows['60-75%']['views']['C8'])


if __name__ == '__main__':
    unittest.main()
