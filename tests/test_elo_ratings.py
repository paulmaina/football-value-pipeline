import unittest

import pandas as pd

import elo_ratings
from elo_ratings import EloRatings


def history(rows):
    return pd.DataFrame(rows, columns=['Date', 'HomeTeam', 'AwayTeam', 'FTHG', 'FTAG'])


class EloTests(unittest.TestCase):
    def test_expectancy_and_margin_multiplier(self):
        self.assertAlmostEqual(EloRatings.expected_score(0), 0.5)
        self.assertAlmostEqual(EloRatings.expected_score(400), 10 / 11)
        self.assertAlmostEqual(EloRatings.expected_score(-200) + EloRatings.expected_score(200), 1)
        self.assertEqual([EloRatings.margin_multiplier(g) for g in (0, -1, 2, 3, -5)],
                         [1.0, 1.0, 1.5, 14 / 8, 16 / 8])

    def test_update_is_zero_sum_and_venue_specific(self):
        r = EloRatings(home_advantage=0, venue_weight=0.5)
        delta = r.update('2025-01-01', 'A', 'B', 3, 0)
        self.assertAlmostEqual(delta, 20 * 1.75 * 0.5)
        self.assertAlmostEqual(r.overall['A'] + r.overall['B'], 3000)
        self.assertAlmostEqual(r.home['A'], 1500 + delta)
        self.assertEqual(r.away['A'], 1500)  # away form unaffected by a home result
        self.assertGreater(r.rating('A', 'home'), r.rating('A', 'away'))
        draw = EloRatings(home_advantage=60)
        self.assertLess(draw.update('2025-01-01', 'A', 'B', 1, 1), 0)  # home side was favoured

    def test_chronology_entry_rating_and_season_regression(self):
        r = EloRatings()
        r.update('2025-01-01', 'A', 'B', 2, 0)
        r.update('2025-01-08', 'C', 'D', 0, 0)
        with self.assertRaises(ValueError):
            r.update('2025-01-02', 'A', 'C', 1, 0)
        low = sorted(r.overall.values())
        r.update('2025-01-15', 'E', 'A', 0, 0)  # promoted-style newcomer
        self.assertLess(r.overall['E'], 1500 + 1e-9)
        self.assertGreaterEqual(r.overall['E'] + 1e-9, low[0] - 40)
        spread = max(r.overall.values()) - min(r.overall.values())
        r.update('2025-08-15', 'A', 'B', 0, 0)  # summer gap triggers regression first
        self.assertLess(max(r.overall.values()) - min(r.overall.values()), spread)
        with self.assertRaises(ValueError):
            EloRatings(k_factor=0)
        with self.assertRaises(ValueError):
            EloRatings(venue_weight=1.5)

    def test_fit_history_features_and_leakage_free_pre_match(self):
        frame = history([
            ['2025-01-08', 'B', 'A', 0, 1],
            ['2025-01-01', 'A', 'B', 2, 0],
            ['2025-01-15', 'A', 'C', None, None],  # upcoming fixture
        ])
        fitted = elo_ratings.fit_history(frame)
        self.assertEqual(fitted.matches, 2)
        self.assertEqual(fitted.table().index[0], 'A')
        features = elo_ratings.fixture_features(fitted, 'A', 'B')
        self.assertGreater(features['elo_home_expectancy'], 0.5)
        self.assertAlmostEqual(features['elo_rating_diff'],
                               features['elo_home_rating'] + 60 - features['elo_away_rating'])
        self.assertTrue(all(v is None for v in elo_ratings.fixture_features(fitted, 'A', '__LEAGUE_AVERAGE__').values()))
        pre = elo_ratings.pre_match_ratings(frame)
        self.assertAlmostEqual(pre.at[1, 'elo_home_expectancy'], EloRatings.expected_score(60))
        self.assertGreater(pre.at[0, 'elo_away_rating'], 1500)  # B v A uses A's earlier win only
        self.assertTrue(pre.loc[2].isna().all())
        info = elo_ratings.diagnostics(fitted)
        self.assertEqual((info['version'], info['teams'], info['last_match_date']),
                         (elo_ratings.VERSION, 2, '2025-01-08'))


if __name__ == '__main__':
    unittest.main()
