"""Cagey-match correction: matrix rescaling, logistic recalibration and the saved gate model."""

from offline_test_case import OfflineQuotePolicyTestCase
import json
import tempfile
import unittest
from pathlib import Path

import numpy as np
import pandas as pd

import market_implied as mi
import narrow_margin as nm


def matrix():
    return mi.dixon_coles_matrix(1.5, 1.1, -0.06)


def abs_margin(size):
    goals = np.arange(size)
    return np.abs(goals[:, None] - goals[None, :])


class CorrectionTests(OfflineQuotePolicyTestCase):
    def test_corrected_matrix_sums_to_one_and_hits_class_totals(self):
        corrected = nm.correct_matrix(matrix(), 0.30, 0.09)
        m = abs_margin(corrected.shape[0])
        self.assertAlmostEqual(corrected.sum(), 1.0, places=12)
        self.assertAlmostEqual(corrected[m >= 2].sum(), 0.30, places=12)
        self.assertAlmostEqual(corrected[m >= 3].sum(), 0.09, places=12)
        self.assertTrue((corrected >= 0).all())

    def test_each_class_keeps_its_shape_and_home_away_split(self):
        original = matrix()
        corrected = nm.correct_matrix(original, 0.30, 0.09)
        m = abs_margin(original.shape[0])
        goals = np.arange(original.shape[0])
        home = goals[:, None] > goals[None, :]
        for mask in nm.class_masks(m):
            ratio = corrected[mask] / original[mask]
            self.assertTrue(np.allclose(ratio, ratio[0]))
            for part in (mask & home, mask & ~home & (m > 0)):
                if original[mask].sum() and original[part].sum():
                    self.assertAlmostEqual(corrected[part].sum() / corrected[mask].sum(),
                                           original[part].sum() / original[mask].sum(), places=12)

    def test_p3_is_capped_at_p2(self):
        self.assertEqual(nm.class_targets(0.2, 0.35), (0.8, 0.0, 0.2))
        corrected = nm.correct_matrix(matrix(), 0.2, 0.35)
        m = abs_margin(corrected.shape[0])
        self.assertAlmostEqual(corrected[m >= 3].sum(), 0.2, places=12)
        self.assertAlmostEqual(corrected[m == 2].sum(), 0.0, places=12)

    def test_distribution_correction_matches_matrix_correction_for_pricing(self):
        corrected = nm.correct_matrix(matrix(), 0.31, 0.10)
        margins, from_matrix = mi.margin_distribution(corrected)
        _, probs = mi.margin_distribution(matrix())
        direct = nm.correct_distribution(margins, probs, 0.31, 0.10)
        self.assertTrue(np.allclose(direct, from_matrix, atol=1e-14))
        for side, line in (('home', 1.75), ('away', 1.0), ('home', -0.25)):
            fit = mi.Fit('B', True, [], matrix=corrected)
            self.assertAlmostEqual(nm.price_distribution(margins, direct, side, line)['win_share'],
                                   mi.price(fit, side, line)['win_share'], places=12)

    def test_moving_mass_into_an_empty_class_is_refused(self):
        margins = np.array([-1, 0, 1])
        with self.assertRaises(ValueError):
            nm.correct_distribution(margins, np.array([0.3, 0.4, 0.3]), 0.2, 0.0)


class LogisticTests(OfflineQuotePolicyTestCase):
    def test_fit_recovers_known_coefficients(self):
        rng = np.random.default_rng(0)
        x = rng.normal(size=(20000, 4))
        beta = np.array([-0.4, 0.8, -0.5, 0.0, 0.3])
        y = (rng.random(20000) < 1 / (1 + np.exp(-(beta[0] + x @ beta[1:])))).astype(float)
        params = nm.fit_logistic(x, y)
        recovered = np.array(params['coefficients']) / np.array(params['feature_std'])
        self.assertTrue(np.allclose(recovered, beta[1:], atol=0.06))
        p = nm.predict(params, x[:5])
        self.assertTrue(((p > 0) & (p < 1)).all())

    def frame(self, dates):
        rng = np.random.default_rng(1)
        n = len(dates)
        p2 = rng.uniform(0.25, 0.55, n)
        return pd.DataFrame({'date': pd.to_datetime(dates), 'matrix_p2': p2, 'matrix_p3': p2 * 0.35,
                             'p_over_2_5': rng.uniform(0.35, 0.65, n), 'p_home': rng.uniform(0.2, 0.6, n),
                             'p_away': rng.uniform(0.15, 0.5, n), 'p_draw': rng.uniform(0.2, 0.32, n),
                             'abs_margin': rng.integers(0, 5, n), 'fit': 'B', 'Division': 'E0',
                             'HomeTeam': [f'H{i}' for i in range(n)], 'AwayTeam': 'A'})

    def test_training_never_uses_data_on_or_after_the_cutoff(self):
        dates = pd.date_range('2023-06-01', '2024-06-01', periods=400)
        frame = self.frame(dates)
        model = nm.finalise(nm.train(frame, version='t', until=nm.GATE_CUTOFF), frame, nm.GATE_CUTOFF)
        self.assertLess(pd.Timestamp(model['training_last_date']), nm.GATE_CUTOFF)
        self.assertEqual(model['training_matches'], int((frame.date < nm.GATE_CUTOFF).sum()))
        self.assertEqual(model['training_fingerprint'], nm.fingerprint(frame[frame.date < nm.GATE_CUTOFF]))
        self.assertNotEqual(model['training_fingerprint'], nm.fingerprint(frame))
        self.assertTrue(0 < model['training_cagey_p20'] < 1)
        p2, p3 = nm.corrected_tails(model, 0.30, 0.25, {'p_over_2_5': 0.5, 'p_home': 0.4, 'p_away': 0.3, 'p_draw': 0.3})
        self.assertLessEqual(p3, p2)
        with self.assertRaises(ValueError):
            nm.train(frame, version='t', until=pd.Timestamp('2020-01-01'))
        with tempfile.TemporaryDirectory() as tmp:
            nm.save(model, Path(tmp))
            self.assertEqual(nm.load('t', Path(tmp)), json.loads(json.dumps(model)))

    def test_saved_gate_model_is_pre_2024_only(self):
        model = nm.load(nm.GATE_VERSION)
        self.assertEqual(model['version'], nm.GATE_VERSION)
        self.assertEqual(model['training_until_exclusive'], '2024-01-01')
        self.assertLess(pd.Timestamp(model['training_last_date']), nm.GATE_CUTOFF)
        self.assertEqual(model['features'], list(nm.FEATURES))
        self.assertEqual(set(model['targets']), {'2', '3'})
        self.assertEqual(len(model['training_fingerprint']), 64)


if __name__ == '__main__':
    unittest.main()
