import math
import unittest

import numpy as np
from scipy.stats import poisson

import match_simulation
from score_probability import score_grid


class SimulationTests(unittest.TestCase):
    def test_exact_prices_are_consistent_distributions(self):
        table = match_simulation.exact_prices(1.6, 1.1, -0.08)
        settled = table[['win', 'half_win', 'refund', 'half_loss', 'loss']].sum(axis=1)
        self.assertTrue(np.allclose(settled, 1.0))
        x12 = table[table['market'] == '1x2'].set_index('selection')['win']
        self.assertAlmostEqual(x12.sum(), 1.0)
        ah = table[table['market'] == 'asian_handicap'].set_index(['selection', 'line'])
        self.assertAlmostEqual(ah.loc[('home', 0.0), 'refund'], x12['draw'])
        self.assertAlmostEqual(ah.loc[('home', -0.5), 'win'], x12['home'])
        self.assertAlmostEqual(ah.loc[('away', 0.5), 'win'], x12['away'] + x12['draw'])
        self.assertAlmostEqual(ah.loc[('home', 0.0), 'fair_decimal_odds'], 1 + x12['away'] / x12['home'])
        binary = table[table['market'] != 'asian_handicap']
        self.assertTrue(np.allclose(binary['fair_decimal_odds'], 1 / binary['win']))

    def test_independent_poisson_btts_closed_form(self):
        table = match_simulation.exact_prices(1.3, 0.9, 0.0)
        btts = table[(table['market'] == 'btts') & (table['selection'] == 'yes')]['win'].item()
        self.assertAlmostEqual(btts, (1 - poisson.pmf(0, 1.3)) * (1 - poisson.pmf(0, 0.9)), places=9)

    def test_quarter_line_and_integer_total(self):
        table = match_simulation.exact_prices(1.4, 1.2, -0.05, total_lines=(2.0,), handicap_lines=(-0.25,))
        x12 = match_simulation.exact_prices(1.4, 1.2, -0.05)
        draw = x12[(x12['market'] == '1x2') & (x12['selection'] == 'draw')]['win'].item()
        home = table[(table['market'] == 'asian_handicap') & (table['selection'] == 'home')].iloc[0]
        self.assertAlmostEqual(home['half_loss'], draw)
        self.assertAlmostEqual(home['fair_decimal_odds'], 1 + (home['loss'] + draw / 2) / home['win'])
        over = table[(table['market'] == 'total') & (table['selection'] == 'over')].iloc[0]
        matrix, _ = score_grid(1.4, 1.2, -0.05)
        totals = np.add.outer(*map(np.arange, matrix.shape))
        self.assertAlmostEqual(over['refund'], matrix[totals == 2].sum())

    def test_monte_carlo_converges_to_exact_grid_and_is_reproducible(self):
        result = match_simulation.simulate_fixture(1.6, 1.1, -0.08, seed=7)
        self.assertEqual(result.attrs['n_simulations'], match_simulation.DEFAULT_SIMULATIONS)
        z = (result['win'] - result['exact_win']).abs() / result['win_standard_error']
        self.assertTrue((z < 5).all())
        again = match_simulation.simulate_fixture(1.6, 1.1, -0.08, seed=7)
        self.assertTrue(result['win'].equals(again['win']))
        self.assertTrue(np.isfinite(result['true_decimal_price']).all())

    def test_sampling_validation_and_degenerate_selection(self):
        home, away = match_simulation.simulate_scores(np.array([[0.0, 1.0], [0.0, 0.0]]), 5, seed=1)
        self.assertEqual((home.tolist(), away.tolist()), ([0] * 5, [1] * 5))
        priced = match_simulation.price_scores(home, away, np.full(5, 0.2))
        never = priced[(priced['market'] == '1x2') & (priced['selection'] == 'home')].iloc[0]
        self.assertTrue(math.isinf(never['fair_decimal_odds']))
        for args in ((np.ones((2, 2)), 0), (np.ones((2, 2)), True), (-np.ones((2, 2)), 5), (np.ones(3), 5)):
            with self.assertRaises(ValueError):
                match_simulation.simulate_scores(*args)


if __name__ == '__main__':
    unittest.main()
