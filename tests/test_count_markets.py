"""Corner/card count models: NB2 fit, leakage-free features, validation rules and quotes."""
import math
from pathlib import Path

import numpy as np
import pandas as pd

import count_markets as cm
from offline_test_case import OfflineQuotePolicyTestCase
from test_asian_handicap import NOW

REPO = Path(__file__).resolve().parents[1]


def history(n_days=400, seed=0):
    """Synthetic league: ten teams, team-specific corner and card rates."""
    rng = np.random.default_rng(seed)
    teams = [f'T{i}' for i in range(10)]
    strength = dict(zip(teams, np.linspace(3.5, 6.5, 10)))
    rows = []
    for day in range(n_days):
        order = rng.permutation(teams)
        date = (pd.Timestamp('2020-08-01') + pd.Timedelta(days=day)).strftime('%d/%m/%Y')
        for home, away in zip(order[::2], order[1::2]):
            hc, ac = rng.negative_binomial(20, 20/(20+strength[home])), rng.negative_binomial(20, 20/(20+strength[away]))
            rows.append({'Date': date, 'HomeTeam': home, 'AwayTeam': away, 'HC': hc, 'AC': ac,
                         'HS': 2*hc+rng.integers(0, 4), 'AS': 2*ac+rng.integers(0, 4),
                         'HY': rng.poisson(2), 'AY': rng.poisson(2), 'HR': 0, 'AR': 0,
                         'HF': rng.poisson(11), 'AF': rng.poisson(11)})
    return pd.DataFrame(rows)


class CountModelTests(OfflineQuotePolicyTestCase):
    def test_labels_lines_and_outcomes(self):
        self.assertEqual(cm.parse_label('Corners Over 9.5'), ('corners', 'Over', 9.5))
        self.assertEqual(cm.parse_label('Cards Under 4.5'), ('cards', 'Under', 4.5))
        for bad in ('Corners Over 9.0', 'Corners Over 20.5', 'Cards Exactly 4.5', 'Over 1.5', 'Home win'):
            self.assertIsNone(cm.parse_label(bad))
        self.assertTrue(cm.outcome('corners', 'Over', 9.5, 10))
        self.assertFalse(cm.outcome('corners', 'Under', 9.5, 10))
        probabilities = cm.probabilities(10., .05, 'corners')
        for line in cm.LINES['corners']:
            self.assertAlmostEqual(probabilities[cm.market_label('corners', 'Over', line)]
                                   + probabilities[cm.market_label('corners', 'Under', line)], 1.)
        # Overdispersion widens the distribution: tails gain probability.
        self.assertGreater(cm.probabilities(10., .2, 'corners')['Corners Over 12.5'], probabilities['Corners Over 12.5'])

    def test_cards_count_each_yellow_and_red_once(self):
        frame = pd.DataFrame([{'Date': '01/08/2025', 'HomeTeam': 'A', 'AwayTeam': 'B', 'HY': 2, 'AY': 3, 'HR': 1, 'AR': 0,
                               'HF': 10, 'AF': 12}])
        self.assertEqual(int(cm.prepare(frame, 'cards').total.iloc[0]), 6)
        self.assertTrue(cm.prepare(frame, 'corners').empty)

    def test_features_use_only_earlier_days(self):
        frame = cm.prepare(history(60), 'corners')
        rows, _, _ = cm.features(frame)
        changed = frame.copy()
        last_day = changed.date == changed.date.max()
        changed.loc[last_day, 'home_count'] = 40
        again, _, _ = cm.features(changed)
        self.assertEqual(rows, again)
        # Same-day matches never see each other's result.
        first_day = frame.date == frame.date.min()
        self.assertTrue(all(rows[i] is None for i in np.flatnonzero(first_day)))

    def test_nb2_fit_recovers_mean_and_overdispersion(self):
        rng = np.random.default_rng(1)
        y = rng.negative_binomial(10, 10/(10+9.0), size=4000)
        model = cm.fit(np.zeros((len(y), 8)), np.zeros(len(y)), y)
        self.assertAlmostEqual(math.exp(model['beta'][0]), 9.0, delta=.2)
        self.assertAlmostEqual(model['alpha'], .1, delta=.03)

    def test_walk_forward_trains_only_on_earlier_windows_and_learns_team_rates(self):
        frame = history(400)
        forecasts = cm.walk_forward(frame, 'corners')
        matches = cm.prepare(frame, 'corners')
        self.assertGreater(forecasts.date.min(), matches.date.iloc[cm.MIN_TRAIN-1])
        # Team rates are learned: high-corner teams forecast higher totals.
        strong = forecasts.loc[forecasts.home_team.isin(['T8', 'T9']) & forecasts.away_team.isin(['T8', 'T9'])].mu
        weak = forecasts.loc[forecasts.home_team.isin(['T0', 'T1']) & forecasts.away_team.isin(['T0', 'T1'])].mu
        self.assertGreater(strong.mean(), weak.mean() + 1)
        report = cm.evaluate(forecasts, 'corners')
        self.assertTrue(report['probability_only'])
        self.assertIn('UNPROVEN EDGE', report['warning'])
        self.assertEqual(set(report['markets']), {cm.market_label('corners', s, l) for l in cm.LINES['corners']
                                                  for s in ('Over', 'Under')})
        audit = report['count_accuracy']['audit']
        self.assertLess(audit['model_log_loss'], audit['constant_rate_log_loss'])

    def test_reliability_rules_match_the_goal_market_thresholds(self):
        n = 400
        dates = pd.date_range('2024-01-01', periods=n, freq='D')
        totals = np.where(np.arange(n) % 2, 12, 8)
        good = pd.DataFrame({'date': dates, 'total': totals, 'mu': 10., 'alpha': .01})
        for line in cm.LINES['corners']:
            good[cm.market_label('corners', 'Over', line)] = (totals > line).astype(float)*.9 + .05
            good[cm.market_label('corners', 'Under', line)] = 1 - good[cm.market_label('corners', 'Over', line)]
        report = cm.evaluate(good, 'corners')
        self.assertEqual(report['markets']['Corners Over 9.5']['status'], 'RELIABLE_FOR_RANKING')
        # Overconfident beyond the unchanged 0.12 limit fails the audit.
        bad = good.copy()
        bad['Corners Over 9.5'] = .99
        self.assertEqual(cm.evaluate(bad, 'corners')['markets']['Corners Over 9.5']['status'], 'UNRELIABLE_AUDIT')
        # Fewer than 80 development or 25 audit matches is insufficient.
        self.assertEqual(cm.evaluate(good.head(90), 'corners')['markets']['Corners Over 9.5']['status'],
                         'INSUFFICIENT_HISTORY')
        self.assertEqual(cm.evaluate(pd.DataFrame(), 'corners')['markets']['Corners Over 9.5']['status'],
                         'INSUFFICIENT_HISTORY')

    def test_only_quoted_leagues_are_validated_and_forecast(self):
        frame = history(400)
        self.assertEqual(set(cm.validate_league(frame, 'SerieA')), {'corners', 'cards'})
        self.assertEqual(set(cm.validate_league(frame, 'EPL')), {'corners'})
        self.assertEqual(cm.validate_league(frame, 'Eredivisie'), {})
        forecast = cm.forecast_fixtures(frame, 'EPL', [('T9', 'T8'), ('T0', 'T1')])
        self.assertEqual(set(forecast[0]), {'corners'})
        self.assertGreater(forecast[0]['corners']['mu'], forecast[1]['corners']['mu'])
        self.assertEqual(cm.forecast_fixtures(frame.head(100), 'EPL', [('T0', 'T1')]), [{}])

    def test_committed_history_loads_six_seasons(self):
        frame = cm.load_history(REPO/'.football_cache', 'I1')
        self.assertTrue({'HC', 'AC', 'HY', 'AY', 'HR', 'AR', 'HF', 'AF', 'HS', 'AS'} <= set(frame.columns))
        self.assertGreater(len(frame), 1500)


class CountQuoteTests(OfflineQuotePolicyTestCase):
    def payload(self, outcomes, key='alternate_totals_corners', book='pinnacle'):
        return {'commence_time': (NOW+pd.Timedelta(hours=10)).isoformat(), 'bookmakers': [
            {'key': book, 'title': book, 'last_update': NOW.isoformat(),
             'markets': [{'key': key, 'last_update': NOW.isoformat(), 'outcomes': outcomes}]}]}

    def test_only_complete_same_book_pairs_on_validated_half_lines(self):
        outcomes = [{'name': 'Over', 'point': 9.5, 'price': 1.9}, {'name': 'Under', 'point': 9.5, 'price': 1.95},
                    {'name': 'Over', 'point': 10.0, 'price': 2.1}, {'name': 'Under', 'point': 10.0, 'price': 1.75},
                    {'name': 'Over', 'point': 11.5, 'price': 3.0}]
        offers = cm.parse_quotes(self.payload(outcomes), NOW)
        self.assertEqual([(o['side'], o['line'], o['bookmaker']) for o in offers],
                         [('Over', 9.5, 'Pinnacle'), ('Under', 9.5, 'Pinnacle')])
        self.assertEqual(offers[0]['opposite_price'], 1.95)
        cards = cm.parse_quotes(self.payload([{'name': 'Over', 'point': 4.5, 'price': 1.9},
                                              {'name': 'Under', 'point': 4.5, 'price': 1.9}], 'alternate_totals_cards'), NOW)
        self.assertEqual({o['kind'] for o in cards}, {'cards'})

    def test_rejects_duplicates_implausible_pairs_unsupported_books_and_started_events(self):
        dup = [{'name': 'Over', 'point': 9.5, 'price': 1.9}, {'name': 'Over', 'point': 9.5, 'price': 2.0},
               {'name': 'Under', 'point': 9.5, 'price': 1.9}]
        self.assertEqual(cm.parse_quotes(self.payload(dup), NOW), [])
        wide = [{'name': 'Over', 'point': 9.5, 'price': 3.0}, {'name': 'Under', 'point': 9.5, 'price': 3.0}]
        self.assertEqual(cm.parse_quotes(self.payload(wide), NOW), [])
        good = [{'name': 'Over', 'point': 9.5, 'price': 1.9}, {'name': 'Under', 'point': 9.5, 'price': 1.95}]
        self.assertEqual(cm.parse_quotes(self.payload(good, book='leovegas'), NOW), [])
        started = self.payload(good)
        started['commence_time'] = (NOW-pd.Timedelta(minutes=1)).isoformat()
        self.assertEqual(cm.parse_quotes(started, NOW), [])
        self.assertEqual(cm.parse_quotes(self.payload(good), NOW+pd.Timedelta(days=2)), [])
