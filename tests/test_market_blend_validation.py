"""Chronological market blend selection unit tests (offline)."""

from offline_test_case import OfflineQuotePolicyTestCase
import unittest

import numpy as np
import pandas as pd

from market_blend_validation import select_market_weight


def sample_predictions(n=160, pattern="market_good"):
    dates = pd.date_range("2024-01-01", periods=n, freq="D")
    y = np.arange(n) % 3
    raw = np.tile(np.array([0.34, 0.33, 0.33]), (n, 1))
    market = np.full((n, 3), 0.1)
    for i, klass in enumerate(y):
        if pattern == "market_good":
            market[i, klass] = 0.8
        elif pattern == "market_bad":
            market[i, (klass + 1) % 3] = 0.8
        elif pattern == "audit_only":
            if i < n * 0.75:
                market[i, (klass + 1) % 3] = 0.8
            else:
                market[i, klass] = 0.8
        else:
            raise ValueError(pattern)
    return pd.DataFrame({
        "date": dates,
        "actual_class": y,
        "raw_p_home": raw[:, 0],
        "raw_p_draw": raw[:, 1],
        "raw_p_away": raw[:, 2],
        "open_p_home": market[:, 0],
        "open_p_draw": market[:, 1],
        "open_p_away": market[:, 2],
    })


class MarketBlendTests(OfflineQuotePolicyTestCase):
    def test_market_can_improve_predictive_log_loss(self):
        result = select_market_weight(sample_predictions(pattern="market_good"))
        self.assertEqual(result["status"], "selected")
        self.assertGreater(result["selected_market_weight"], 0.0)
        self.assertGreater(result["development_log_loss_gain"], 0.0)
        self.assertGreater(result["audit_log_loss_gain"], 0.0)
        self.assertTrue(result["audit_improved"])

    def test_market_can_be_rejected(self):
        result = select_market_weight(sample_predictions(pattern="market_bad"))
        self.assertEqual(result["selected_market_weight"], 0.0)

    def test_later_audit_does_not_influence_selected_weight(self):
        result = select_market_weight(sample_predictions(pattern="audit_only"))
        self.assertEqual(result["selected_market_weight"], 0.0)
        # The audit period is reported; selection still uses earlier rows.
        self.assertFalse(result["audit_improved"])

    def test_missing_opening_odds_causes_fallback(self):
        frame = sample_predictions()
        frame[["open_p_home", "open_p_draw", "open_p_away"]] = np.nan
        result = select_market_weight(frame)
        self.assertIsNone(result["selected_market_weight"])
        self.assertEqual(result["status"], "insufficient_history")

    def test_invalid_weights(self):
        with self.assertRaisesRegex(ValueError, "Candidate weights"):
            select_market_weight(sample_predictions(), candidates=[0, -0.1])
        with self.assertRaisesRegex(ValueError, "Include weight 0"):
            select_market_weight(sample_predictions(), candidates=[0.5, 1.0])


if __name__ == "__main__":
    unittest.main()
