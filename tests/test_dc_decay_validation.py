"""Offline tests for Dixon-Coles time-decay selection."""

import unittest

import numpy as np
import pandas as pd
from scipy.optimize import check_grad

from football_value_pipeline_v2_standalone import (
    DixonColesModel,
    dixon_coles_loss_and_gradient,
)

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


class DixonColesGradientTests(unittest.TestCase):
    def test_analytic_gradient_matches_finite_differences(self):
        home_idx = np.array([0, 1, 2, 3, 0, 2, 1, 3, 0, 1])
        away_idx = np.array([1, 2, 3, 0, 3, 1, 0, 2, 2, 3])
        hg = np.array([0, 0, 1, 1, 2, 1, 0, 3, 2, 0], dtype=float)
        ag = np.array([0, 1, 0, 1, 0, 2, 1, 1, 3, 0], dtype=float)
        weights = np.linspace(0.3, 1.0, len(hg))
        params = np.array(
            [0.12, -0.10, 0.08, 0.09, -0.03, 0.05, 0.22, 0.16, -0.06],
            dtype=float,
        )
        common = (home_idx, away_idx, hg, ag, weights, 4, 0.08)
        error = check_grad(
            lambda p: dixon_coles_loss_and_gradient(p, *common)[0],
            lambda p: dixon_coles_loss_and_gradient(p, *common)[1],
            params,
        )
        self.assertLess(error, 1e-5)

    def test_many_team_fit_converges(self):
        # Many clubs historically required expensive numerical gradients.
        rng = np.random.default_rng(20261008)
        n_teams = 28
        n_matches = 420
        hi = rng.integers(0, n_teams, n_matches)
        ai = (hi + rng.integers(1, n_teams, n_matches)) % n_teams
        attack = rng.normal(0, 0.12, size=n_teams)
        defence = rng.normal(0, 0.10, size=n_teams)
        lam = np.exp(0.25 + attack[hi] + defence[ai])
        mu = np.exp(0.08 + attack[ai] + defence[hi])
        frame = pd.DataFrame({
            "Date": pd.date_range("2023-01-01", periods=n_matches, freq="D"),
            "HomeTeam": [f"Team_{i}" for i in hi],
            "AwayTeam": [f"Team_{i}" for i in ai],
            "FTHG": rng.poisson(lam),
            "FTAG": rng.poisson(mu),
        })
        model = DixonColesModel(half_life_days=240, l2=0.15)
        model.fit(frame)
        self.assertTrue(model.fit_result.success)
        self.assertLess(model.fit_result.nfev, 30000)


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
