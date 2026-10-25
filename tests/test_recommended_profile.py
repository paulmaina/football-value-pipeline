"""Regression checks for the default single-model recommendation.

Offline checks: no network credentials required.
"""

from offline_test_case import OfflineQuotePolicyTestCase
import inspect
import unittest

import numpy as np

from football_value_pipeline_v2_standalone import (
    FootballValuePipelineV2,
    build_parser,
    reweight_matrix_to_1x2,
)


class RecommendedProfileTests(OfflineQuotePolicyTestCase):
    def test_one_command_uses_fixed_v2_profile(self):
        options = build_parser().parse_args([
            "--leagues", "EPL", "LaLiga", "Bundesliga", "SerieA", "Ligue1", "UCL",
        ])
        self.assertAlmostEqual(options.market_weight, 0.7)
        self.assertAlmostEqual(options.half_life_days, 480.0)
        self.assertFalse(options.tune_half_life)
        self.assertFalse(options.auto_market_weight)
        self.assertEqual(len(options.leagues), 6)

    def test_direct_python_pipeline_has_same_blend_default(self):
        default = inspect.signature(FootballValuePipelineV2.__init__).parameters[
            "market_weight"
        ].default
        self.assertAlmostEqual(default, 0.7)

    def test_blended_score_matrix_is_valid_distribution(self):
        scores = np.array([
            [0.16, 0.09, 0.04],
            [0.19, 0.18, 0.06],
            [0.15, 0.09, 0.04],
        ], dtype=float)
        scores /= scores.sum()
        h, a = np.indices(scores.shape)
        masks = [h > a, h == a, h < a]
        base = np.array([scores[mask].sum() for mask in masks])
        market = np.array([0.44, 0.27, 0.29])
        blended = reweight_matrix_to_1x2(scores, 0.5 * base + 0.5 * market)
        actual = np.array([blended[mask].sum() for mask in masks])
        np.testing.assert_allclose(actual, (base + market) / 2, atol=1e-12)
        self.assertAlmostEqual(blended.sum(), 1.0)
        self.assertTrue(np.all(blended >= 0))


if __name__ == "__main__":
    unittest.main()
