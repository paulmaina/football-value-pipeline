"""Candidate C5 (research_sharpen): the walk-forward home/away sharpening, its fit and its
independence from odds."""
import json
from pathlib import Path
import unittest
from unittest.mock import patch

import numpy as np
import pandas as pd

import evaluation_harness as eh
import research_sharpen as rs
from tests import epl_research_rows as epl
from team_research import research_grid

REPO = Path(__file__).resolve().parents[1]
CFG = json.loads((REPO / 'evaluation_harness_config.json').read_text(encoding='utf-8'))


def rates(n, seed):
    rng = np.random.default_rng(seed)
    return np.column_stack([rng.uniform(.6, 2.4, n), rng.uniform(.5, 2.0, n)])


def simulate(slope, n, seed=7):
    """Goal rates C would have used, and scores drawn from C's grid sharpened by `slope`."""
    rng, out = np.random.default_rng(seed + 1), []
    for lam, mu in rates(n, seed):
        grid = rs.sharpened_grid((lam, mu), {'slope': slope})
        cell = rng.choice(grid.size, p=grid.ravel())
        out.append(((lam, mu), *np.unravel_index(cell, grid.shape)))
    return out


def as_fit_inputs(sim):
    probs = np.array([rs.one_x_two(research_grid(list(r))) for r, _, _ in sim])
    outcomes = np.array([0 if h > a else 1 if h == a else 2 for _, h, a in sim])
    return probs, outcomes, (np.arange(len(sim)) % 700).astype(float)


def research_row(league, date, goal_rates, hg, ag, scored=True, phase='development'):
    identity = {'league': league, 'date': str(date.date()),
                'week': f'{date.isocalendar().year}-W{date.isocalendar().week:02d}',
                'fixture_key': f'{league}|{date.isoformat()}', 'phase': phase, 'market_book': 'pinnacle'}
    return {'identity': identity, 'date': date, 'goal_rates': [float(v) for v in goal_rates],
            'home_goals': float(hg), 'away_goals': float(ag), 'scored': scored}


class GridTest(unittest.TestCase):
    def test_neutral_slope_gives_exactly_the_research_grid(self):
        for r in ((1.4, 1.1), (0.3, 2.9), (3.2, 0.4)):
            np.testing.assert_array_equal(rs.sharpened_grid(r, rs.NEUTRAL), research_grid(list(r)))

    def test_sharpening_keeps_the_draw_and_moves_the_favourite(self):
        base = rs.one_x_two(research_grid([1.7, 1.0]))
        grid = rs.sharpened_grid((1.7, 1.0), {'slope': 1.3})
        p = rs.one_x_two(grid)
        self.assertAlmostEqual(float(grid.sum()), 1., places=12)
        self.assertAlmostEqual(p[1], base[1], places=12)
        self.assertGreater(p[0], base[0])
        self.assertLess(p[2], base[2])
        # Slope below 1 flattens; an even match stays even.
        self.assertLess(rs.one_x_two(rs.sharpened_grid((1.7, 1.0), {'slope': .8}))[0], base[0])
        even = rs.sharpened(np.array([.375, .25, .375]), 1.5)
        np.testing.assert_allclose(even, [.375, .25, .375])

    def test_scorelines_keep_their_shape_inside_each_region(self):
        base, grid = research_grid([1.6, 1.1]), rs.sharpened_grid((1.6, 1.1), {'slope': 1.4})
        h, a = np.indices(base.shape)
        for mask in (h > a, h == a, h < a):
            np.testing.assert_allclose(grid[mask] / grid[mask].sum(), base[mask] / base[mask].sum(), rtol=1e-9)


class FitTest(unittest.TestCase):
    def test_fit_recovers_a_known_slope(self):
        fitted = rs.fit(*as_fit_inputs(simulate(1.3, 6000)), 1e6)
        self.assertEqual(fitted['status'], 'fitted')
        self.assertAlmostEqual(fitted['slope'], 1.3, delta=.08)
        self.assertGreater(fitted['neutral_minus_fitted_loss'], 0)

    def test_calibrated_forecasts_fit_near_neutral(self):
        fitted = rs.fit(*as_fit_inputs(simulate(1., 6000, seed=11)), 1e6)
        self.assertAlmostEqual(fitted['slope'], 1., delta=.08)

    def test_draws_carry_no_weight_and_warm_up_is_neutral(self):
        probs, outcomes, age = as_fit_inputs(simulate(1.3, 3000))
        decided = int((outcomes != 1).sum())
        with patch.object(rs, 'MIN_MATCHES', decided + 1):
            self.assertEqual(rs.fit(probs, outcomes, age, 480.),
                             {'slope': 1., 'status': 'warm_up', 'matches': decided})
        draws = outcomes == 1
        moved = probs.copy()
        moved[draws] = [.1, .1, .8]  # a draw's forecast cannot change the fit
        self.assertEqual(rs.fit(probs, outcomes, age, 480.), rs.fit(moved, outcomes, age, 480.))

    def test_rows_after_the_origin_are_refused(self):
        probs, outcomes, age = as_fit_inputs(simulate(1., 50))
        age[0] = -1.
        with self.assertRaises(ValueError):
            rs.fit(probs, outcomes, age, 480.)


class WalkForwardTest(unittest.TestCase):
    """sharpen_candidate: each window is fitted only on C's forecasts of matches played before it.

    1,500 simulated forecasts (500 days) with the fit minimum lowered from 1,000 to 500 decided matches for
    this class only, so there are warm-up windows and fitted ones; the walk-forward is run once and shared."""
    N, MIN_MATCHES = 1500, 500

    @classmethod
    def setUpClass(cls):
        cls.enterClassContext(patch.object(rs, 'MIN_MATCHES', cls.MIN_MATCHES))
        start = pd.Timestamp(CFG['test_start'])
        cls.base = [research_row('EPL' if i % 2 else 'SerieA', start + pd.Timedelta(hours=8 * i), r, h, a)
                    for i, (r, h, a) in enumerate(simulate(1.25, cls.N, seed=3))]
        cls.result = eh.sharpen_candidate(cls.rows(), CFG, cls.end(cls.base))

    @classmethod
    def rows(cls):
        return [dict(r) for r in cls.base]

    @staticmethod
    def end(rows):
        return rows[-1]['date'] + pd.Timedelta(days=1)

    def test_fits_use_only_earlier_decided_matches_and_warm_up_is_c(self):
        rows = self.rows()
        records, calib, coverage, fits = self.result
        self.assertEqual(fits[0]['status'], 'warm_up')
        self.assertEqual(fits[-1]['status'], 'fitted')
        self.assertAlmostEqual(fits[-1]['slope'], 1.25, delta=.15)
        for fit in fits:
            self.assertEqual(fit['matches'], sum(r['date'] < pd.Timestamp(fit['origin'])
                                                 and r['home_goals'] != r['away_goals'] for r in rows))
        self.assertEqual(len(calib), len(rows))
        self.assertEqual({r['candidate'] for r in records}, {'C5'})
        self.assertEqual(sum(v for k, v in coverage.items() if k.endswith(':C5:available')), len(rows))
        # Warm-up windows are exactly C.
        warm = {f['origin'] for f in fits if f['status'] == 'warm_up'}
        self.assertTrue(warm and warm != {f['origin'] for f in fits})
        for row, cal in zip(sorted(rows, key=lambda r: r['date']), calib):
            window = max(w[0] for w in eh.fold_windows(CFG, self.end(rows)) if w[0] <= row['date'])
            if window.date().isoformat() in warm:
                np.testing.assert_array_equal(cal['probs'], rs.one_x_two(research_grid(row['goal_rates'])))

    def test_a_later_result_never_changes_an_earlier_forecast(self):
        rows = self.rows()
        changed = [dict(r) for r in rows]
        for r in changed[-300:]:
            r['home_goals'], r['away_goals'] = 3., 0.
        cut = changed[-300]['date']
        opened = max(w[0] for w in eh.fold_windows(CFG, self.end(rows)) if w[0] <= cut)
        early = lambda records: {(r['fixture_key'], r['market']): r['log_loss'] for r in records
                                 if pd.Timestamp(r['fixture_key'].split('|')[1]) < opened}
        before, after = early(self.result[0]), early(eh.sharpen_candidate(changed, CFG, self.end(rows))[0])
        self.assertGreater(len(before), 1000)
        self.assertEqual(before, after)

    def test_unscored_rows_feed_the_fit_but_are_not_scored(self):
        rows = self.rows()
        for r in rows[:900]:
            r['scored'] = False
        _, calib, _, fits = eh.sharpen_candidate(rows, CFG, self.end(rows))
        self.assertEqual(len(calib), 600)
        self.assertEqual(fits[0]['status'], 'fitted')  # fitted on unscored forecasts alone

    def test_skipped_when_not_kept(self):
        rows = self.rows()
        self.assertEqual(eh.sharpen_candidate(rows, CFG, self.end(rows), keep={'C', 'M'})[0], [])


class HarnessCandidateTest(unittest.TestCase):
    """C5 on real EPL folds: registered, and identical whatever any odds field says (tests/epl_research_rows.py)."""

    def test_c5_is_registered(self):
        self.assertIn('C5', eh.CANDIDATES)
        self.assertIn('research_sharpen.py', eh.SETUP_FILES)

    def test_c5_ignores_every_odds_field_in_the_match_and_the_training_history(self):
        self.assertGreater(len(epl.odds_columns()), 20)
        (rows, a), (rows2, b) = epl.research_rows(), epl.research_rows(moved=True)
        self.assertEqual(rows, rows2)  # C's goal rates and the scores: everything C5 reads
        for x, y in zip(a, b):
            np.testing.assert_array_equal(x['C'], y['C'])
            self.assertFalse(np.array_equal(x['M'], y['M']))  # the market reference did move
        end = epl.ORIGIN + pd.Timedelta(days=30)
        with patch.object(rs, 'MIN_MATCHES', 10):  # force a real fit on the 40 earlier forecasts
            first, second = eh.sharpen_candidate(rows, CFG, end), eh.sharpen_candidate(rows2, CFG, end)
        self.assertEqual(first[3][-1]['status'], 'fitted')
        self.assertNotEqual(first[3][-1]['slope'], 1.)
        self.assertTrue(first[0])
        self.assertEqual(first[0], second[0])
        self.assertEqual(first[1], second[1])


if __name__ == '__main__':
    unittest.main()
