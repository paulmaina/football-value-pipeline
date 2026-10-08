"""Offline tests for Dixon-Coles time-decay selection."""

import unittest

import numpy as np
import pandas as pd

from dc_decay_validation import make_walkforward_folds, tune_half_life


def sample_results(n=130):
    return pd.DataFrame({
        "Date": pd.date_range("2023-01-01", periods=n, freq="7D"),
        "HomeTeam": ["A"] * n,
        "AwayTeam": ["B"] * n,
        "FTHG": [1] * n,
        "FTAG": [0] * n,
    })


class DeterministicModel:
    """Lightweight model stub isolating validation logic from fitting speed."""

    def __init__(self, half_life_days, l2, max_goals):
        self.half_life_days = half_life_days

    def fit(self, train, as_of=None):
        assert len(train) >= 30
        assert train["Date"].max() < as_of
        return self

    def score_matrix(self, home, away):
        return np.array([[1.0]]), {}

    def one_x_two(self, matrix):
        if self.half_life_days == 120:
            return {"home": 0.8, "draw": 0.1, "away": 0.1}
        return {"home": 0.4, "draw": 0.3, "away": 0.3}


class DecayValidationTests(unittest.TestCase):
    def test_no_future_data_leakage(self):
        folds = make_walkforward_folds(
            sample_results(), validation_days=365, step_days=56, min_train=30
        )
        self.assertGreater(len(folds), 1)
        for train, test, origin in folds:
            self.assertLess(train["Date"].max(), origin)
            self.assertGreaterEqual(test["Date"].min(), origin)
            self.assertLess(train["Date"].max(), test["Date"].min())

    def test_selects_lower_log_loss_candidate(self):
        score = tune_half_life(
            sample_results(),
            model_class=DeterministicModel,
            candidates=[240, 120],
            validation_days=365,
            step_days=56,
            min_train=30,
            min_validation_matches=5,
        )
        self.assertEqual(score["selected_half_life_days"], 120)
        self.assertGreater(score["n_folds"], 1)
        self.assertTrue(all(item["valid"] for item in score["candidates"]))

    def test_rejects_bad_candidates(self):
        with self.assertRaises(ValueError):
            tune_half_life(
                sample_results(),
                model_class=DeterministicModel,
                candidates=[0, 240],
                min_train=30,
            )


if __name__ == "__main__":
    unittest.main()
