"""D_pow2 (docs/plan.md, Phase 3b-2): the cagey grid with its 1X2 set separately. Offline candidate only.

D_pow2 is D_pow's grid and correction for the shape of margins, then

    logit(draw') = logit(draw_q) + a + b * (f - 0.5)      draw_q, f from the power quote

home and away sharing the rest in the power quote's ratio, and the corrected grid moved onto that 1X2. So:
  * the candidate model is the power candidate, coefficient for coefficient, plus a `one_x_two` block fitted on the
    same training rows, and it sits where nothing live reads;
  * no other model has the block, and a model without it is corrected exactly as before;
  * the grid's 1X2 is the rule's target exactly and, inside each result, its margins keep D_pow's shape;
  * the harness grid and the live cagey context are the same grid;
  * the candidate changes the cagey tier's own figures and nothing else, and stays a pure market view.
"""
from __future__ import annotations

import json
import math
import unittest

import numpy as np
import pandas as pd

import cagey_tier_v3
import evaluation_harness as eh
import market_implied as mi
import narrow_margin as nm
import price_edge_cagey_shortlist as v28
import price_edge_shortlist as v27
import research_backtest as rb
from football_value_pipeline_v2_standalone import reweight_matrix_to_1x2
from tests import test_cagey_market_independence as independence
from tests.test_cagey_devig_methods import H2H, PRICES, candidate_model, live_run

FROZEN = independence.FROZEN


def model():
    return nm.load(nm.ONE_X_TWO_VERSION, nm.CANDIDATE_DIR)


def one_x_two(grid):
    h, a = np.indices(grid.shape)
    return np.array([grid[h > a].sum(), grid[h == a].sum(), grid[h < a].sum()])


def logit(p):
    return math.log(p / (1 - p))


class ModelTest(unittest.TestCase):
    def test_it_is_the_power_candidate_plus_the_1x2_rule(self):
        power, candidate = candidate_model('power'), model()
        self.assertEqual(candidate['version'], nm.ONE_X_TWO_VERSION)
        self.assertEqual({k for k in candidate if candidate.get(k) != power.get(k)}, {'version', 'one_x_two'})
        self.assertEqual(candidate['targets'], power['targets'])
        spec = candidate['one_x_two']
        self.assertEqual(spec['rule'], nm.ONE_X_TWO_RULE)
        self.assertEqual(spec['base_version'], nm.CANDIDATE_VERSIONS['power'])
        self.assertIs(nm.one_x_two(candidate), spec)

    def test_the_rule_was_fitted_on_the_corrections_own_training_rows(self):
        production, spec = nm.production_model(), model()['one_x_two']
        self.assertEqual(spec['training_matches'], production['training_matches'])
        self.assertEqual(spec['training_matches'], 10956)
        self.assertEqual(spec['training_fingerprint'], production['training_fingerprint'])
        self.assertEqual(model()['training_until_exclusive'], '2025-07-01')
        self.assertLessEqual(spec['training_log_loss'], spec['quote_training_log_loss'])

    def test_no_other_model_has_a_1x2_rule(self):
        for other in (nm.production_model(), nm.load(nm.GATE_VERSION), candidate_model('power'), candidate_model('shin')):
            self.assertNotIn('one_x_two', other)
            self.assertIsNone(nm.one_x_two(other))

    def test_it_sits_where_nothing_live_reads(self):
        self.assertTrue((nm.CANDIDATE_DIR / f'{nm.ONE_X_TWO_VERSION}.json').exists())
        self.assertFalse((nm.MODEL_DIR / f'{nm.ONE_X_TWO_VERSION}.json').exists())
        self.assertNotIn(nm.ONE_X_TWO_VERSION, nm.CANDIDATE_VERSIONS.values())
        self.assertNotIn(nm.ONE_X_TWO_VERSION, json.dumps(nm.versions()))
        self.assertEqual(v28.load_settings()['model_version'], nm.PRODUCTION_VERSION)
        # Registered as harness candidate D_pow2 on 17 Nov 2026 (declared once against D): the holdout's setup
        # fingerprint now covers the model, as it covers everything that can change a score. Still nothing live.
        self.assertIn(f'narrow_margin_models/candidates/{nm.ONE_X_TWO_VERSION}.json', eh.SETUP_FILES)

    def test_the_rule_is_only_valid_on_the_power_grid(self):
        spec = model()['one_x_two']
        for wrong in ({**nm.production_model(), 'one_x_two': spec}, {**candidate_model('shin'), 'one_x_two': spec}):
            with self.assertRaisesRegex(ValueError, 'cannot correct a power grid'):
                nm.one_x_two(wrong)
        with self.assertRaisesRegex(ValueError, 'Unknown 1X2 rule'):
            nm.one_x_two({**candidate_model('power'), 'one_x_two': {**spec, 'rule': 'something-else'}})


class RuleTest(unittest.TestCase):
    def test_the_target_is_the_formula(self):
        spec = {'a': 0.07, 'b': -0.9}
        for odds in H2H:
            home, draw, away = mi.devig_three_way(*odds, method='power')
            h, d, a = nm.one_x_two_target(spec, home, draw, away)
            self.assertAlmostEqual(h + d + a, 1.0, places=12)
            self.assertAlmostEqual(logit(d) - logit(draw), 0.07 - 0.9 * (max(home, away) - 0.5), places=12)
            self.assertAlmostEqual(h / a, home / away, places=12)  # the quote's ratio

    def test_no_uplift_is_the_quote(self):
        for odds in H2H:
            quote = mi.devig_three_way(*odds, method='power')
            np.testing.assert_allclose(nm.one_x_two_target({'a': 0.0, 'b': 0.0}, *quote), quote, atol=1e-12)

    def test_a_negative_b_takes_draws_from_strong_favourites_only(self):
        spec = {'a': 0.05, 'b': -0.5}
        level = nm.one_x_two_target(spec, 0.36, 0.30, 0.34)
        strong = nm.one_x_two_target(spec, 0.80, 0.13, 0.07)
        self.assertGreater(level[1], 0.30)
        self.assertLess(strong[1], 0.13)
        self.assertGreater(strong[0], 0.80)

    def test_the_fit_recovers_known_parameters(self):
        rng = np.random.default_rng(7)
        home = rng.uniform(0.15, 0.8, 4000)
        draw = (1 - home) * rng.uniform(0.25, 0.6, 4000)
        away = 1 - home - draw
        truth = {'a': 0.06, 'b': -0.4}
        # Expected draw frequencies in place of results: maximum likelihood then returns the parameters exactly.
        expected = np.array([nm.one_x_two_target(truth, h, d, a)[1] for h, d, a in zip(home, draw, away)])
        fitted = nm.fit_one_x_two(home, draw, away, expected)
        self.assertAlmostEqual(fitted['a'], truth['a'], places=6)
        self.assertAlmostEqual(fitted['b'], truth['b'], places=6)
        self.assertEqual(fitted['rule'], nm.ONE_X_TWO_RULE)
        self.assertLess(fitted['training_log_loss'], fitted['quote_training_log_loss'])

    def test_training_refuses_other_rows_grids_and_models(self):
        power = candidate_model('power')
        frame = pd.DataFrame({'date': pd.to_datetime(['2024-01-01']), 'devig_method': ['power']})
        with self.assertRaisesRegex(ValueError, 'Training rows differ'):
            nm.train_one_x_two(frame, power, version='x')
        with self.assertRaisesRegex(ValueError, 'different margin-removal method'):
            nm.train_one_x_two(frame.assign(devig_method='shin'), power, version='x')
        with self.assertRaisesRegex(ValueError, 'different margin-removal method'):
            nm.train_one_x_two(frame.drop(columns='devig_method'), power, version='x')
        with self.assertRaisesRegex(ValueError, 'cannot correct a power grid'):
            nm.train_one_x_two(frame, nm.production_model(), version='x')
        with self.assertRaisesRegex(ValueError, 'already has a 1X2 rule'):
            nm.train_one_x_two(frame, model(), version='x')

    def test_the_cli_fits_the_rule_on_the_power_grid_only(self):
        for method in ('proportional', 'shin'):
            with self.assertRaises(SystemExit):
                nm.main(['--method', method, '--one-x-two-from', nm.CANDIDATE_VERSIONS['power'], '--divisions',
                         '--model-dir', str(nm.CANDIDATE_DIR)])


class GridTest(unittest.TestCase):
    """The harness grid (evaluation_harness.cagey_matrix)."""

    @classmethod
    def setUpClass(cls):
        cls.grids = []
        for hda in H2H[:3]:
            prices = {**PRICES, 'hda': hda}
            try:
                m_pow = eh.market_matrix(prices, 'power')
            except ValueError:
                continue  # these three prices need not be mutually consistent for every 1X2
            cls.grids.append((prices, m_pow, eh.cagey_matrix(m_pow, prices, candidate_model('power'), 'power'),
                              eh.cagey_matrix(m_pow, prices, model(), 'power')))
        prices = PRICES
        m_pow = eh.market_matrix(prices, 'power')
        cls.grids.append((prices, m_pow, eh.cagey_matrix(m_pow, prices, candidate_model('power'), 'power'),
                          eh.cagey_matrix(m_pow, prices, model(), 'power')))

    def test_its_1x2_is_the_rules_target_exactly(self):
        spec = model()['one_x_two']
        for prices, _, _, d_pow2 in self.grids:
            target = nm.one_x_two_target(spec, *mi.devig_three_way(*prices['hda'], method='power'))
            np.testing.assert_allclose(one_x_two(d_pow2), target, atol=1e-12)
            self.assertAlmostEqual(float(d_pow2.sum()), 1.0, places=12)

    def test_it_is_d_pow_moved_onto_that_1x2(self):
        spec = model()['one_x_two']
        for prices, _, d_pow, d_pow2 in self.grids:
            target = nm.one_x_two_target(spec, *mi.devig_three_way(*prices['hda'], method='power'))
            np.testing.assert_array_equal(d_pow2, rb.matrix_value(reweight_matrix_to_1x2(d_pow, target)))
            self.assertGreater(float(np.abs(d_pow2 - d_pow).max()), 1e-6)

    def test_inside_each_result_the_margins_keep_d_pows_shape(self):
        for _, _, d_pow, d_pow2 in self.grids:
            margins, before = mi.margin_distribution(d_pow)
            _, after = mi.margin_distribution(d_pow2)
            for mask in (margins > 0, margins < 0):
                np.testing.assert_allclose(after[mask] / after[mask].sum(), before[mask] / before[mask].sum(), atol=1e-12)
            h, a = np.indices(d_pow.shape)
            draws = h == a  # and the drawn scorelines keep their shape
            np.testing.assert_allclose(d_pow2[draws] / d_pow2[draws].sum(), d_pow[draws] / d_pow[draws].sum(), atol=1e-12)

    def test_it_needs_the_power_grid(self):
        with self.assertRaisesRegex(ValueError, 'fitted on the power grid'):
            eh.cagey_matrix(eh.market_matrix(PRICES), PRICES, model())
        with self.assertRaisesRegex(ValueError, 'fitted on the power grid'):
            eh.cagey_matrix(eh.market_matrix(PRICES, 'shin'), PRICES, model(), 'shin')

    def test_models_without_the_rule_are_corrected_as_before(self):
        # The correction's original arithmetic: margin classes rescaled to the corrected tails, nothing else.
        for method, correction in (('proportional', nm.production_model()), ('power', candidate_model('power')),
                                   ('shin', candidate_model('shin'))):
            grid = eh.market_matrix(PRICES, method)
            margins, probs = mi.margin_distribution(grid)
            home, draw, away = mi.devig_three_way(*PRICES['hda'], method=method)
            inputs = {'p_over_2_5': mi.devig_two_way(*PRICES['ou'], method=method)[0], 'p_home': home, 'p_away': away,
                      'p_draw': draw}
            p2, p3 = nm.corrected_tails(correction, nm.margin_tail(margins, probs, 2), nm.margin_tail(margins, probs, 3),
                                        inputs)
            np.testing.assert_array_equal(eh.cagey_matrix(grid, PRICES, correction, method),
                                          rb.matrix_value(nm.correct_matrix(grid, p2, p3)))


class LiveCandidateTest(unittest.TestCase):
    """A real frozen forecast (Brighton v Brentford, 8 Nov 2026) through the production v28 shortlist."""

    @classmethod
    def setUpClass(cls):
        cls.row = FROZEN['row']
        cls.base = live_run(cls.row)
        cls.d_pow = live_run(cls.row, 'power', candidate_model('power'))
        cls.d_pow2 = live_run(cls.row, 'power', model())

    def test_it_needs_the_power_method(self):
        with self.assertRaisesRegex(ValueError, 'fitted on the power grid'):
            live_run(self.row, None, model())
        with self.assertRaisesRegex(ValueError, 'fitted on the power grid'):
            live_run(self.row, 'shin', model())

    def test_the_live_context_is_the_harness_grid(self):
        now = pd.Timestamp(FROZEN['snapshot_generated_utc'])
        pin = v27.pinnacle_quotes(self.row)
        fit, info = v27.market_fit(pin, now, True, method='power')
        self.assertTrue(fit.usable)
        prices = {'hda': pin['h2h'][:3], 'ou': pin['ou25'][:2]}
        for correction in (candidate_model('power'), model()):
            context = v28.corrected_context(pin, fit, info, correction, 'power')
            grid = cagey_tier_v3.corrected_grid(context, fit.matrix)
            expected = eh.cagey_matrix(rb.matrix_value(fit.matrix), prices, correction, 'power')
            np.testing.assert_allclose(grid, expected, atol=1e-12)
            margins, probs = mi.margin_distribution(expected)
            np.testing.assert_allclose(context['probs'], probs, atol=1e-12)
            self.assertAlmostEqual(context['score'], nm.margin_tail(margins, probs, 2), places=12)
        target = nm.one_x_two_target(model()['one_x_two'], *mi.devig_three_way(*pin['h2h'][:3], method='power'))
        np.testing.assert_allclose(one_x_two(grid), target, atol=1e-12)

    def test_it_moves_only_the_cagey_tiers_own_figures(self):
        own = (*independence.CAGEY_PREFIXES, 'price_flag', 'in_value_tier', 'p_narrow')

        def rest(frame):
            return frame[[c for c in frame.columns if not c.startswith(own)]].to_csv(index=False)

        selected, decisions, _, summary = self.d_pow2
        self.assertEqual(summary['cagey_model_version'], nm.ONE_X_TWO_VERSION)
        for other in (self.base, self.d_pow):
            self.assertEqual(rest(selected), rest(other[0]))
            self.assertEqual(rest(decisions), rest(other[1]))
            self.assertEqual(list(decisions.decision), list(other[1].decision))
            moved = (decisions.cagey_no_loss_probability.astype(float)
                     - other[1].cagey_no_loss_probability.astype(float)).abs()
            self.assertGreater(moved.max(), 1e-6)
            self.assertLess(moved.max(), 0.05)
        # The grid's draw is the rule's: the power quote's draw plus the uplift.
        spec = model()['one_x_two']
        pin = v27.pinnacle_quotes(self.row)
        quote = mi.devig_three_way(*pin['h2h'][:3], method='power')
        delta = decisions.corrected_draw_delta_vs_pinnacle.dropna().astype(float)
        self.assertGreater(len(delta), 0)
        np.testing.assert_allclose(delta, nm.one_x_two_target(spec, *quote)[1] - quote[1], atol=1e-9)

    def test_it_stays_a_pure_market_view(self):
        _, decisions, picks, _ = self.d_pow2
        for change in (independence.mirrored_research, independence.no_research, independence.every_non_market_field):
            _, changed, changed_picks, _ = live_run(change(self.row), 'power', model())
            self.assertEqual(independence.cagey_view(changed), independence.cagey_view(decisions), change)
            self.assertEqual(list(changed_picks.market), list(picks.market))


if __name__ == '__main__':
    unittest.main()
