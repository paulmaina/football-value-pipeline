"""Margin-removal methods for the cagey tier's market grid (docs/plan.md, Phase 3b): offline candidates only.

The power and Shin methods sit behind a `method` argument that defaults to today's proportional removal, so:
  * with the default, every function computes exactly what it did before the argument existed;
  * a correction model is only ever applied to the grid it was fitted on;
  * the candidate corrections are the production procedure on the same rows, saved where nothing live reads;
  * a candidate method changes the cagey tier's own figures and nothing else, and stays a pure market view.
"""
from __future__ import annotations

import inspect
import json
import unittest

import numpy as np
import pandas as pd

import cagey_market_basis
import cagey_tier_v3
import evaluation_harness as eh
import market_implied as mi
import narrow_margin as nm
import price_edge_cagey_shortlist as v28
import price_edge_shortlist as v27
from ah_close_backtest import devig_proportional, devig_shin
from tests import test_cagey_market_independence as independence

FROZEN, POLICY = independence.FROZEN, independence.POLICY
H2H = ((1.25, 6.5, 13.0), (2.10, 3.40, 3.60), (1.08, 12.0, 29.0), (3.10, 3.20, 2.45), (1.62, 4.10, 5.60))
PAIRS = ((1.95, 1.95), (1.50, 2.75), (1.25, 4.10), (2.02, 1.88))
PRICES = {'hda': (1.42, 4.9, 7.6), 'ou': (1.72, 2.2), 'ah': (-1.25, 1.93, 1.99)}


def candidate_model(method):
    return nm.load(nm.CANDIDATE_VERSIONS[method], nm.CANDIDATE_DIR)


class MethodsTest(unittest.TestCase):
    def test_power_is_the_pipelines_power_method_exactly(self):
        from football_value_pipeline_v2_standalone import devig
        for odds in (*H2H, *PAIRS):
            self.assertEqual(mi.devig_power(odds), tuple(devig(list(odds), 'power')))
        for odds in H2H:
            self.assertEqual(mi.devig_three_way(*odds, method='power'), tuple(eh.quote_references({'hda': odds})['QPOW']))

    def test_three_way_shin_is_the_two_way_shin_generalised(self):
        for odds in PAIRS:
            self.assertEqual(mi.devig_shin_n(odds), devig_shin(*odds))
            self.assertEqual(mi.devig_two_way(*odds, method='shin'), devig_shin(*odds))
        for odds in H2H:
            p = np.array(mi.devig_three_way(*odds, method='shin'))
            q = 1 / np.array(odds)
            book = q.sum()
            self.assertAlmostEqual(p.sum(), 1.0, places=12)
            # Shin's equations hold with one insider share z for every outcome:
            # p_i = (sqrt(z^2 + 4 (1 - z) q_i^2 / B) - z) / (2 (1 - z))  <=>  z = (q_i^2 / B - p_i^2) / (p_i (1 - p_i)).
            z = (q ** 2 / book - p ** 2) / (p * (1 - p))
            self.assertTrue((z > 0).all() and (z < 0.2).all(), z)
            np.testing.assert_allclose(z, z[0], atol=1e-9)

    def test_both_methods_give_favourites_more_than_proportional(self):
        for odds in H2H:
            base = mi.devig_three_way(*odds)
            favourite, longshot = int(np.argmax(base)), int(np.argmin(base))
            for method in ('power', 'shin'):
                fair = mi.devig_three_way(*odds, method=method)
                self.assertAlmostEqual(sum(fair), 1.0, places=12)
                self.assertGreater(fair[favourite], base[favourite])
                self.assertLess(fair[longshot], base[longshot])
        for odds in PAIRS[1:3]:
            for method in ('power', 'shin'):
                self.assertGreater(mi.devig_two_way(*odds, method=method)[0], devig_proportional(*odds)[0])
        for method in mi.DEVIG_METHODS:  # an even pair stays even
            self.assertAlmostEqual(mi.devig_two_way(1.95, 1.95, method=method)[0], 0.5, places=12)

    def test_without_a_margin_every_method_is_the_quote(self):
        fair = (0.5, 0.3, 0.2)
        odds = tuple(1 / p for p in fair)
        for method in mi.DEVIG_METHODS:
            np.testing.assert_allclose(mi.devig_three_way(*odds, method=method), fair, atol=1e-9)

    def test_unknown_method_is_refused_everywhere(self):
        with self.assertRaises(ValueError):
            mi.devig_three_way(2.1, 3.4, 3.6, method='additive')
        with self.assertRaises(ValueError):
            mi.devig_two_way(1.9, 1.9, method='additive')
        with self.assertRaises(ValueError):
            mi.targets_from_prices((2.1, 3.4, 3.6), (1.95, 1.95), method='additive')
        with self.assertRaises(ValueError):
            v28.devig_method({'devig_method': 'additive'})


class DefaultUnchangedTest(unittest.TestCase):
    """The default is today's behaviour, bit for bit."""

    def test_every_method_argument_defaults_to_proportional(self):
        for function in (mi.devig_three_way, mi.devig_two_way, mi.targets_from_prices, eh.market_matrix,
                         eh.cagey_matrix, v27.market_fit, v28.corrected_context, cagey_market_basis.reference,
                         cagey_market_basis.annotate, cagey_tier_v3.annotate, nm.match_record, nm.division_records,
                         nm.build_dataset, nm.train):
            self.assertEqual(inspect.signature(function).parameters['method'].default, 'proportional', function)
        self.assertEqual(v28.devig_method({}), 'proportional')
        self.assertEqual(v28.devig_method(v28.load_settings()), 'proportional')
        self.assertNotIn('devig_method', json.loads(v28.CONFIG.read_text(encoding='utf-8-sig')))

    def test_default_margin_removal_is_the_original_arithmetic(self):
        for home, draw, away in H2H:
            q = np.array([1 / home, 1 / draw, 1 / away])
            fair = q / q.sum()
            self.assertEqual(mi.devig_three_way(home, draw, away), (float(fair[0]), float(fair[1]), float(fair[2])))
        for pair in PAIRS:
            self.assertEqual(mi.devig_two_way(*pair), devig_proportional(*pair))

    def test_default_targets_and_grids_are_unchanged(self):
        h2h, ou, ah = PRICES['hda'], PRICES['ou'], PRICES['ah']
        original = {**dict(zip(('home', 'draw', 'away'), mi.devig_three_way(*h2h))),
                    'over_2_5': devig_proportional(*ou)[0], 'ah_line': float(ah[0]),
                    'ah_main': devig_proportional(*ah[1:])[0]}
        self.assertEqual(mi.targets_from_prices(h2h, ou, ah), original)
        self.assertEqual(mi.targets_from_prices(h2h, ou, ah, method='proportional'), original)
        m = eh.market_matrix(PRICES)
        np.testing.assert_array_equal(m, eh.market_matrix(PRICES, 'proportional'))
        model = nm.production_model()
        np.testing.assert_array_equal(eh.cagey_matrix(m, PRICES, model), eh.cagey_matrix(m, PRICES, model, 'proportional'))

    def test_the_other_methods_do_move_the_grid(self):
        m = eh.market_matrix(PRICES)
        for method in ('power', 'shin'):
            other = eh.market_matrix(PRICES, method)
            self.assertGreater(float(np.tril(other, -1).sum()), float(np.tril(m, -1).sum()))  # P(home favourite wins)


class CorrectionModelTest(unittest.TestCase):
    def test_a_correction_is_never_applied_to_another_methods_grid(self):
        production = nm.production_model()
        for method in ('power', 'shin'):
            grid = eh.market_matrix(PRICES, method)
            with self.assertRaisesRegex(ValueError, 'fitted on the proportional grid'):
                eh.cagey_matrix(grid, PRICES, production, method)
            with self.assertRaisesRegex(ValueError, f'fitted on the {method} grid'):
                eh.cagey_matrix(eh.market_matrix(PRICES), PRICES, candidate_model(method))
            corrected = eh.cagey_matrix(grid, PRICES, candidate_model(method), method)
            self.assertAlmostEqual(float(corrected.sum()), 1.0, places=9)

    def test_candidates_are_the_production_procedure_on_the_same_rows(self):
        production = nm.production_model()
        self.assertNotIn('devig_method', production)
        self.assertEqual(nm.model_method(production), 'proportional')
        for method, version in nm.CANDIDATE_VERSIONS.items():
            model = candidate_model(method)
            self.assertEqual((model['version'], model['devig_method']), (version, method))
            for key in ('features', 'matrix_source', 'training_until_exclusive', 'training_first_date',
                        'training_last_date', 'training_matches', 'training_fingerprint'):
                self.assertEqual(model[key], production[key], key)
            self.assertEqual(set(model['targets']), set(production['targets']))
            self.assertNotEqual(model['targets']['2']['coefficients'], production['targets']['2']['coefficients'])

    def test_candidates_live_where_nothing_live_reads(self):
        self.assertEqual(nm.CANDIDATE_DIR, nm.MODEL_DIR / 'candidates')
        self.assertEqual(sorted(p.name for p in nm.MODEL_DIR.glob('*.json')),
                         ['cagey-correction-pre2024-v1.json', 'cagey-correction-through-2425-v1.json',
                          'cagey-correction-through-2425-v1.quintiles.json', 'index.json'])
        self.assertEqual(nm.versions()['production']['version'], nm.PRODUCTION_VERSION)
        self.assertEqual(v28.load_settings()['model_version'], nm.PRODUCTION_VERSION)
        for version in nm.CANDIDATE_VERSIONS.values():
            self.assertFalse((nm.MODEL_DIR / f'{version}.json').exists())
            self.assertNotIn(f'narrow_margin_models/candidates/{version}.json', eh.SETUP_FILES)

    def test_training_refuses_a_dataset_from_another_method(self):
        frame = pd.DataFrame({'date': pd.to_datetime(['2024-01-01']), 'devig_method': ['power']})
        with self.assertRaisesRegex(ValueError, 'different margin-removal method'):
            nm.train(frame, version='x', until=pd.Timestamp('2025-01-01'))
        with self.assertRaisesRegex(ValueError, 'different margin-removal method'):
            nm.train(frame.drop(columns='devig_method'), version='x', until=pd.Timestamp('2025-01-01'), method='shin')

    def test_the_cli_never_saves_a_candidate_beside_the_production_models(self):
        with self.assertRaises(SystemExit):
            nm.main(['--method', 'power', '--model-dir', str(nm.MODEL_DIR), '--divisions'])


def live_run(row, method=None, model=None):
    settings = v28.load_settings() if method is None else {**v28.load_settings(), 'devig_method': method}
    selected, decisions, summary = v28.build_shortlist(
        pd.DataFrame([row]), FROZEN['snapshot_generated_utc'], execution_policy=POLICY, settings=settings,
        model=model or nm.production_model())
    return selected, decisions, v28.cagey_tier_list(decisions), summary


class LiveCandidateTest(unittest.TestCase):
    """A real frozen forecast (Brighton v Brentford, 8 Nov 2026) through the production v28 shortlist."""

    @classmethod
    def setUpClass(cls):
        cls.row = FROZEN['row']
        cls.base = live_run(cls.row)
        cls.candidates = {m: live_run(cls.row, m, candidate_model(m)) for m in ('power', 'shin')}

    def test_naming_the_default_method_changes_nothing(self):
        named = live_run(self.row, 'proportional')
        for before, after in zip(self.base[:3], named[:3]):
            self.assertEqual(before.to_csv(index=False), after.to_csv(index=False))
        self.assertEqual(json.dumps(self.base[3], sort_keys=True, default=str),
                         json.dumps(named[3], sort_keys=True, default=str))

    def test_a_candidate_method_needs_its_own_correction(self):
        with self.assertRaisesRegex(ValueError, 'fitted on the proportional grid'):
            live_run(self.row, 'power')
        with self.assertRaisesRegex(ValueError, 'fitted on the power grid'):
            live_run(self.row, None, candidate_model('power'))

    def test_a_candidate_moves_only_the_cagey_tiers_own_figures(self):
        _, base, _, _ = self.base
        # What the cagey tier computes from its own grid; p_narrow is the shared schema's copy of its P(narrow).
        own = (*independence.CAGEY_PREFIXES, 'price_flag', 'in_value_tier', 'p_narrow')

        def rest(frame):
            return frame[[c for c in frame.columns if not c.startswith(own)]].to_csv(index=False)

        for method, (selected, decisions, _, summary) in self.candidates.items():
            self.assertEqual(summary['cagey_model_version'], nm.CANDIDATE_VERSIONS[method])
            # The value shortlist: same picks, same order, every research and value figure unchanged.
            self.assertEqual(rest(selected), rest(self.base[0]))
            self.assertEqual(rest(decisions), rest(base))
            self.assertEqual(list(decisions.decision), list(base.decision))
            moved = (decisions.cagey_no_loss_probability.astype(float) - base.cagey_no_loss_probability.astype(float)).abs()
            self.assertGreater(moved.max(), 1e-6)
            self.assertLess(moved.max(), 0.05)
            # The binary price check de-vigs Pinnacle's 1X2 the same way as the grid it guards.
            binary = decisions.price_guard_basis.dropna().loc[lambda s: s.str.startswith('pinnacle_1x2_')]
            self.assertGreater(len(binary), 0)
            self.assertEqual(set(binary), {'pinnacle_1x2_' + method})
            self.assertEqual(set(base.price_guard_basis.dropna().loc[lambda s: s.str.startswith('pinnacle_1x2_')]),
                             {'pinnacle_1x2_proportional'})

    def test_a_candidate_stays_a_pure_market_view(self):
        # The research-perturbation test (tests/test_cagey_market_independence.py) on each candidate grid.
        for method, (_, decisions, picks, _) in self.candidates.items():
            for change in (independence.mirrored_research, independence.no_research,
                           independence.every_non_market_field):
                _, changed, changed_picks, _ = live_run(change(self.row), method, candidate_model(method))
                self.assertEqual(independence.cagey_view(changed), independence.cagey_view(decisions), (method, change))
                self.assertEqual(list(changed_picks.market), list(picks.market))


if __name__ == '__main__':
    unittest.main()
