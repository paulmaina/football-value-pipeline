"""Candidate C2 (research_low_score): the draw and low-score correction, its walk-forward fit
and its independence from odds (docs/plan.md, Phase 2a)."""
import json
from pathlib import Path
import unittest
from unittest.mock import patch

import numpy as np
import pandas as pd

import evaluation_harness as eh
import research_low_score as rls
from team_research import research_grid

REPO = Path(__file__).resolve().parents[1]
CFG = json.loads((REPO / 'evaluation_harness_config.json').read_text(encoding='utf-8'))
ODDS_PREFIXES = ('PS', 'P>', 'P<', 'PC', 'PAH', 'B365', 'Max', 'Avg', 'BW', 'IW', 'WH', 'VC', 'AH', '1X', 'BF', 'PSC')


def simulate(lam, mu, rho, delta, n, seed=7):
    """n scores drawn from the corrected grid, with the goal rates C would have used, and their ages."""
    grid = rls.adjusted_grid((lam, mu), {'rho': rho, 'delta': delta})
    cells = np.random.default_rng(seed).choice(grid.size, size=n, p=grid.ravel())
    hg, ag = np.unravel_index(cells, grid.shape)
    return np.tile([lam, mu], (n, 1)), hg.astype(float), ag.astype(float), (np.arange(n) % 700).astype(float)


def research_row(league, date, rates, hg, ag, scored=True, phase='development'):
    """One entry of the harness's research list (evaluate_league)."""
    identity = {'league': league, 'date': str(date.date()),
                'week': f'{date.isocalendar().year}-W{date.isocalendar().week:02d}',
                'fixture_key': f'{league}|{date.isoformat()}', 'phase': phase, 'market_book': 'pinnacle'}
    return {'identity': identity, 'date': date, 'goal_rates': [float(v) for v in rates],
            'home_goals': float(hg), 'away_goals': float(ag), 'scored': scored}


class GridTest(unittest.TestCase):
    def test_neutral_parameters_give_exactly_the_research_grid(self):
        for rates in ((1.4, 1.1), (0.3, 2.9), (3.2, 0.4)):
            np.testing.assert_array_equal(rls.adjusted_grid(rates, rls.NEUTRAL), research_grid(list(rates)))

    def test_grid_is_normalised_and_moves_draws_and_low_scores(self):
        base = research_grid([1.3, 1.1])
        grid = rls.adjusted_grid((1.3, 1.1), {'rho': -.1, 'delta': .1})
        self.assertAlmostEqual(float(grid.sum()), 1., places=12)
        self.assertGreater(np.trace(grid), np.trace(base))
        self.assertGreater(grid[0, 0], base[0, 0])
        self.assertGreater(grid[1, 1], base[1, 1])
        self.assertLess(grid[1, 0], base[1, 0])

    def test_invalid_low_score_cell_is_rejected(self):
        with self.assertRaises(ValueError):
            rls.adjusted_grid((4., 4.), {'rho': .1, 'delta': 0.})  # 1 - lam*mu*rho < 0


class FitTest(unittest.TestCase):
    def test_fit_recovers_known_parameters(self):
        fitted = rls.fit(*simulate(1.45, 1.15, -.12, .15, 6000), 1e6)
        self.assertEqual(fitted['status'], 'fitted')
        self.assertAlmostEqual(fitted['rho'], -.12, delta=.06)
        self.assertAlmostEqual(fitted['delta'], .15, delta=.08)
        self.assertGreater(fitted['neutral_minus_fitted_loss'], 0)

    def test_independent_poisson_scores_fit_near_neutral(self):
        fitted = rls.fit(*simulate(1.45, 1.15, 0., 0., 6000, seed=11), 1e6)
        self.assertLess(abs(fitted['rho']), .06)
        self.assertLess(abs(fitted['delta']), .08)

    def test_warm_up_is_neutral(self):
        fitted = rls.fit(*simulate(1.4, 1.1, -.1, .2, rls.MIN_MATCHES - 1), 480.)
        self.assertEqual((fitted['rho'], fitted['delta'], fitted['status']), (0., 0., 'warm_up'))

    def test_rows_after_the_origin_are_refused(self):
        rates, hg, ag, age = simulate(1.4, 1.1, 0., 0., rls.MIN_MATCHES)
        age[0] = -1.
        with self.assertRaises(ValueError):
            rls.fit(rates, hg, ag, age, 480.)


class WalkForwardTest(unittest.TestCase):
    """low_score_candidate: each window is fitted only on C's forecasts of matches played before it."""

    def rows(self):
        rates, hg, ag, _ = simulate(1.4, 1.1, -.1, .2, 3000, seed=3)
        start = pd.Timestamp(CFG['test_start'])
        return [research_row('EPL' if i % 2 else 'SerieA', start + pd.Timedelta(hours=8 * i), rates[i], hg[i], ag[i])
                for i in range(len(rates))]

    def end(self, rows):
        return rows[-1]['date'] + pd.Timedelta(days=1)

    def test_fits_use_only_earlier_matches_and_warm_up_is_c(self):
        rows = self.rows()
        records, calib, coverage, fits = eh.low_score_candidate(rows, CFG, self.end(rows))
        self.assertEqual(fits[0]['status'], 'warm_up')
        self.assertEqual(fits[-1]['status'], 'fitted')
        for fit in fits:
            self.assertEqual(fit['matches'], sum(r['date'] < pd.Timestamp(fit['origin']) for r in rows))
        self.assertEqual(len(calib), len(rows))
        self.assertEqual({r['candidate'] for r in records}, {'C2'})
        self.assertEqual(sum(v for k, v in coverage.items() if k.endswith(':C2:available')), len(rows))

    def test_a_later_result_never_changes_an_earlier_forecast(self):
        rows = self.rows()
        changed = [dict(r) for r in rows]
        for r in changed[-300:]:
            r['home_goals'], r['away_goals'] = 0., 0.
        cut = changed[-300]['date']
        score = lambda rs: {(r['fixture_key'], r['market']): r['log_loss']
                            for r in eh.low_score_candidate(rs, CFG, self.end(rows))[0]
                            if pd.Timestamp(r['fixture_key'].split('|')[1]) < opened}
        opened = max(w[0] for w in eh.fold_windows(CFG, self.end(rows)) if w[0] <= cut)
        before, after = score(rows), score(changed)
        self.assertGreater(len(before), 1000)
        self.assertEqual(before, after)

    def test_unscored_rows_feed_the_fit_but_are_not_scored(self):
        rows = self.rows()
        for r in rows[:1500]:
            r['scored'] = False
        records, calib, _, fits = eh.low_score_candidate(rows, CFG, self.end(rows))
        self.assertEqual(len(calib), 1500)
        self.assertEqual(fits[0]['status'], 'fitted')  # fitted on unscored forecasts alone
        self.assertEqual(fits[0]['matches'], sum(r['date'] < pd.Timestamp(fits[0]['origin']) for r in rows))

    def test_skipped_when_not_kept(self):
        rows = self.rows()
        self.assertEqual(eh.low_score_candidate(rows, CFG, self.end(rows), keep={'C', 'M'})[0], [])


class HarnessCandidateTest(unittest.TestCase):
    """C2 on real EPL folds: registered, and identical whatever any odds field says."""

    @classmethod
    def setUpClass(cls):
        import historical_benchmark as hb
        data, _, _ = hb.load_history(REPO / '.football_cache', 'EPL',
                                     {**CFG, 'seasons': ['2122', '2223', '2324'], 'test_end_exclusive': '2024-07-01'})
        cls.origin = pd.Timestamp('2024-03-01')
        cls.data = data

    @staticmethod
    def fit(train, origin):
        from football_value_pipeline_v2_standalone import DixonColesModel
        return DixonColesModel(half_life_days=480., l2=.08, max_goals=10, shot_features=True,
                               bbs_statistics=False).fit(train.copy(), as_of=origin)

    def test_c2_is_registered(self):
        self.assertIn('C2', eh.CANDIDATES)
        self.assertIn('research_low_score.py', eh.SETUP_FILES)

    def research_rows(self, data):
        """C's forecasts of 40 matches before the origin (fit only) and 5 after (scored), as the harness collects them."""
        import narrow_margin as nm
        cagey, rows, matrices = nm.production_model(), [], []
        for origin, scored in ((pd.Timestamp('2023-12-01'), False), (self.origin, True)):
            train, test = data[data.Date < origin], data[data.Date >= origin].head(5 if scored else 40)
            model = self.fit(train, origin)
            for _, row in test.iterrows():
                m, _, extra = eh.candidates(row, train, origin, model, CFG, cagey)
                matrices.append(m)
                rows.append(research_row('EPL', row.Date, extra['research_goal_rates'], row.FTHG, row.FTAG, scored))
        return rows, matrices

    def test_c2_ignores_every_odds_field_in_the_match_and_the_training_history(self):
        # Every price moves; handicap lines (AHh, AHCh) keep valid quarter values.
        odds = [c for c in self.data.columns if c.startswith(ODDS_PREFIXES) and c not in ('AHh', 'AHCh')]
        self.assertGreater(len(odds), 20)
        shaken = self.data.copy()
        shaken[odds] = shaken[odds].apply(pd.to_numeric, errors='coerce') * 1.02 + .01
        (rows, a), (rows2, b) = self.research_rows(self.data), self.research_rows(shaken)
        self.assertEqual(rows, rows2)  # C's goal rates and the scores: everything C2 reads
        for x, y in zip(a, b):
            np.testing.assert_array_equal(x['C'], y['C'])
            self.assertFalse(np.array_equal(x['M'], y['M']))  # the market reference did move
        # Force a real fit on the 40 earlier forecasts (below MIN_MATCHES the fit is neutral by design).
        end = self.origin + pd.Timedelta(days=30)
        with patch.object(rls, 'MIN_MATCHES', 10):
            first, second = eh.low_score_candidate(rows, CFG, end), eh.low_score_candidate(rows2, CFG, end)
        self.assertEqual(first[3][-1]['status'], 'fitted')
        self.assertTrue(first[0])
        self.assertEqual(first[0], second[0])
        self.assertEqual(first[1], second[1])

    def test_c2_keeps_the_research_goal_rates(self):
        train = self.data[self.data.Date < self.origin]
        row = self.data[self.data.Date >= self.origin].iloc[0]
        model = self.fit(train, self.origin)
        context, _, _ = eh.research_context(row, train, self.origin, model)
        c, _, _ = eh.research_matrix(row, train, self.origin, model)
        np.testing.assert_array_equal(eh.low_score_matrix(context['goal_rates'], rls.NEUTRAL), c)


if __name__ == '__main__':
    unittest.main()
