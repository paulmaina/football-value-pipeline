"""Candidate C2 (research_low_score): the draw and low-score correction, its walk-forward fit
and its independence from odds (docs/plan.md, Phase 2a)."""
import json
from pathlib import Path
import unittest
from unittest.mock import patch

import numpy as np
import pandas as pd

import evaluation_harness as eh
from tests import epl_research_rows as epl
import research_low_score as rls
from team_research import research_grid

REPO = Path(__file__).resolve().parents[1]
CFG = json.loads((REPO / 'evaluation_harness_config.json').read_text(encoding='utf-8'))


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
    """low_score_candidate: each window is fitted only on C's forecasts of matches played before it.

    1,500 simulated forecasts (500 days) with the fit minimum lowered from 1,000 to 500 matches for this class
    only, so there are warm-up windows and fitted ones; the walk-forward is run once and shared."""
    N, MIN_MATCHES = 1500, 500

    @classmethod
    def setUpClass(cls):
        cls.enterClassContext(patch.object(rls, 'MIN_MATCHES', cls.MIN_MATCHES))
        rates, hg, ag, _ = simulate(1.4, 1.1, -.1, .2, cls.N, seed=3)
        start = pd.Timestamp(CFG['test_start'])
        cls.base = [research_row('EPL' if i % 2 else 'SerieA', start + pd.Timedelta(hours=8 * i), rates[i], hg[i], ag[i])
                    for i in range(len(rates))]
        cls.result = eh.low_score_candidate(cls.rows(), CFG, cls.end(cls.base))

    @classmethod
    def rows(cls):
        return [dict(r) for r in cls.base]

    @staticmethod
    def end(rows):
        return rows[-1]['date'] + pd.Timedelta(days=1)

    def test_fits_use_only_earlier_matches_and_warm_up_is_c(self):
        rows = self.rows()
        records, calib, coverage, fits = self.result
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
        opened = max(w[0] for w in eh.fold_windows(CFG, self.end(rows)) if w[0] <= cut)
        early = lambda records: {(r['fixture_key'], r['market']): r['log_loss'] for r in records
                                 if pd.Timestamp(r['fixture_key'].split('|')[1]) < opened}
        before, after = early(self.result[0]), early(eh.low_score_candidate(changed, CFG, self.end(rows))[0])
        self.assertGreater(len(before), 1000)
        self.assertEqual(before, after)

    def test_unscored_rows_feed_the_fit_but_are_not_scored(self):
        rows = self.rows()
        for r in rows[:750]:
            r['scored'] = False
        records, calib, _, fits = eh.low_score_candidate(rows, CFG, self.end(rows))
        self.assertEqual(len(calib), 750)
        self.assertEqual(fits[0]['status'], 'fitted')  # fitted on unscored forecasts alone
        self.assertEqual(fits[0]['matches'], sum(r['date'] < pd.Timestamp(fits[0]['origin']) for r in rows))

    def test_skipped_when_not_kept(self):
        rows = self.rows()
        self.assertEqual(eh.low_score_candidate(rows, CFG, self.end(rows), keep={'C', 'M'})[0], [])


class HarnessCandidateTest(unittest.TestCase):
    """C2 on real EPL folds: registered, and identical whatever any odds field says (tests/epl_research_rows.py)."""

    def test_c2_is_registered(self):
        self.assertIn('C2', eh.CANDIDATES)
        self.assertIn('research_low_score.py', eh.SETUP_FILES)

    def test_c2_ignores_every_odds_field_in_the_match_and_the_training_history(self):
        # Every price moves; handicap lines (AHh, AHCh) keep valid quarter values.
        self.assertGreater(len(epl.odds_columns()), 20)
        (rows, a), (rows2, b) = epl.research_rows(), epl.research_rows(moved=True)
        self.assertEqual(rows, rows2)  # C's goal rates and the scores: everything C2 reads
        for x, y in zip(a, b):
            np.testing.assert_array_equal(x['C'], y['C'])
            self.assertFalse(np.array_equal(x['M'], y['M']))  # the market reference did move
        # Force a real fit on the 40 earlier forecasts (below MIN_MATCHES the fit is neutral by design).
        end = epl.ORIGIN + pd.Timedelta(days=30)
        with patch.object(rls, 'MIN_MATCHES', 10):
            first, second = eh.low_score_candidate(rows, CFG, end), eh.low_score_candidate(rows2, CFG, end)
        self.assertEqual(first[3][-1]['status'], 'fitted')
        self.assertTrue(first[0])
        self.assertEqual(first[0], second[0])
        self.assertEqual(first[1], second[1])

    def test_c2_keeps_the_research_goal_rates(self):
        train, model = epl.scored_fold()
        row = epl.data()[epl.data().Date >= epl.ORIGIN].iloc[0]
        context, _, _ = eh.research_context(row, train, epl.ORIGIN, model)
        c, _, _ = eh.research_matrix(row, train, epl.ORIGIN, model)
        np.testing.assert_array_equal(eh.low_score_matrix(context['goal_rates'], rls.NEUTRAL), c)


if __name__ == '__main__':
    unittest.main()
