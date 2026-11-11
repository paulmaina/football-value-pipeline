"""Candidate C6 (research_low_score_sharpen): C2's grid with C5's sharpening, its walk-forward fits
and its independence from odds."""
import json
from pathlib import Path
import unittest
from unittest.mock import patch

import numpy as np
import pandas as pd

import evaluation_harness as eh
import research_low_score as rls
import research_low_score_sharpen as c6
import research_sharpen as rs

REPO = Path(__file__).resolve().parents[1]
CFG = json.loads((REPO / 'evaluation_harness_config.json').read_text(encoding='utf-8'))
ODDS_PREFIXES = ('PS', 'P>', 'P<', 'PC', 'PAH', 'B365', 'Max', 'Avg', 'BW', 'IW', 'WH', 'VC', 'AH', '1X', 'BF', 'PSC')
LOW = {'rho': -.08, 'delta': .12}


def simulate(slope, n, seed=7):
    """Goal rates C would have used, and scores drawn from C6's grid with these parameters."""
    rng = np.random.default_rng(seed)
    rates = np.column_stack([rng.uniform(.6, 2.4, n), rng.uniform(.5, 2.0, n)])
    draws, out = np.random.default_rng(seed + 1), []
    for lam, mu in rates:
        grid = c6.grid((lam, mu), LOW, {'slope': slope})
        cell = draws.choice(grid.size, p=grid.ravel())
        out.append(((lam, mu), *np.unravel_index(cell, grid.shape)))
    return out


def research_row(league, date, goal_rates, hg, ag, scored=True, phase='development'):
    identity = {'league': league, 'date': str(date.date()),
                'week': f'{date.isocalendar().year}-W{date.isocalendar().week:02d}',
                'fixture_key': f'{league}|{date.isoformat()}', 'phase': phase, 'market_book': 'pinnacle'}
    return {'identity': identity, 'date': date, 'goal_rates': [float(v) for v in goal_rates],
            'home_goals': float(hg), 'away_goals': float(ag), 'scored': scored}


def by_fixture(records):
    return {(r['fixture_key'], r['market']): r['log_loss'] for r in records}


class GridTest(unittest.TestCase):
    def test_neutral_slope_gives_exactly_c2(self):
        for r in ((1.4, 1.1), (0.3, 2.9), (3.2, 0.4)):
            for low in (rls.NEUTRAL, LOW):
                np.testing.assert_array_equal(c6.grid(r, low, rs.NEUTRAL), rls.adjusted_grid(r, low))

    def test_sharpening_holds_c2s_draw_and_moves_the_favourite(self):
        base = rs.one_x_two(rls.adjusted_grid((1.7, 1.0), LOW))
        grid = c6.grid((1.7, 1.0), LOW, {'slope': 1.3})
        p = rs.one_x_two(grid)
        self.assertAlmostEqual(float(grid.sum()), 1., places=12)
        self.assertAlmostEqual(p[1], base[1], places=12)  # C2's draw, not C's
        self.assertNotAlmostEqual(p[1], rs.one_x_two(rs.sharpened_grid((1.7, 1.0), {'slope': 1.3}))[1], places=4)
        self.assertGreater(p[0], base[0])
        self.assertLess(p[2], base[2])

    def test_scorelines_keep_c2s_shape_inside_each_region(self):
        base, grid = rls.adjusted_grid((1.6, 1.1), LOW), c6.grid((1.6, 1.1), LOW, {'slope': 1.4})
        h, a = np.indices(base.shape)
        for mask in (h > a, h == a, h < a):
            np.testing.assert_allclose(grid[mask] / grid[mask].sum(), base[mask] / base[mask].sum(), rtol=1e-9)

    def test_c5_is_unchanged_by_the_shared_step(self):
        for r in ((1.4, 1.1), (2.2, 0.7)):
            from team_research import research_grid
            np.testing.assert_array_equal(rs.sharpened_grid(r, {'slope': 1.2}),
                                          rs.sharpen_matrix(research_grid(list(r)), 1.2))


class WalkForwardTest(unittest.TestCase):
    """low_score_sharpen_candidate: C2 as it forecast each match, and a slope fitted on C2's earlier forecasts."""

    @classmethod
    def setUpClass(cls):
        start = pd.Timestamp(CFG['test_start'])
        cls.base = [research_row('EPL' if i % 2 else 'SerieA', start + pd.Timedelta(hours=8 * i), r, h, a)
                    for i, (r, h, a) in enumerate(simulate(1.25, 3000, seed=3))]
        cls.c6 = eh.low_score_sharpen_candidate(cls.rows(), CFG, cls.end(cls.base))
        cls.c2 = eh.low_score_candidate(cls.rows(), CFG, cls.end(cls.base))

    @classmethod
    def rows(cls):
        return [dict(r) for r in cls.base]

    @staticmethod
    def end(rows):
        return rows[-1]['date'] + pd.Timedelta(days=1)

    def window(self, date):
        return max(w[0] for w in eh.fold_windows(CFG, self.end(self.base)) if w[0] <= pd.Timestamp(date))

    def test_neutral_folds_are_c2_exactly(self):
        records, calib, coverage, fits = self.c6
        warm = {f['origin'] for f in fits if f['status'] == 'warm_up'}
        fitted = {f['origin'] for f in fits if f['status'] == 'fitted'}
        self.assertTrue(warm and fitted)
        self.assertTrue({f['low_score']['status'] for f in fits if f['origin'] in warm} >= {'fitted'},
                        'some warm-up folds must already carry a real C2 correction')
        self.assertEqual({r['candidate'] for r in records}, {'C6'})
        self.assertEqual(sum(v for k, v in coverage.items() if k.endswith(':C6:available')), len(self.base))
        c2, c6_ = by_fixture(self.c2[0]), by_fixture(records)
        neutral = {k for k in c6_ if self.window(k[0].split('|')[1]).date().isoformat() in warm}
        self.assertGreater(len(neutral), 1000)
        self.assertEqual({k: c6_[k] for k in neutral}, {k: c2[k] for k in neutral})
        moved = [k for k in c6_ if k not in neutral and c6_[k] != c2[k]]
        self.assertGreater(len(moved), 1000)
        c2_calib = {r['fixture_key']: r['probs'] for r in self.c2[1]}
        for r in calib:
            if self.window(r['fixture_key'].split('|')[1]).date().isoformat() in warm:
                self.assertEqual(r['probs'], c2_calib[r['fixture_key']])
            else:
                self.assertAlmostEqual(r['probs'][1], c2_calib[r['fixture_key']][1], places=12)  # C2's draw held

    def test_each_fit_uses_only_earlier_matches_and_c2s_own_forecasts(self):
        fits, c2_fits = self.c6[3], {f['origin']: f for f in self.c2[3]}
        rows = sorted(self.base, key=lambda r: r['date'])
        dates = pd.DatetimeIndex([r['date'] for r in rows])
        # C2's forecast of every match under the (rho, delta) of the window it was played in.
        c2_probs = np.array([c6.c2_one_x_two(r['goal_rates'], c2_fits[self.window(r['date']).date().isoformat()])
                             for r in rows])
        c_probs = np.array([rs.one_x_two(rls.adjusted_grid(r['goal_rates'], rls.NEUTRAL)) for r in rows])
        outcomes = np.array([0 if r['home_goals'] > r['away_goals'] else 1 if r['home_goals'] == r['away_goals'] else 2
                             for r in rows])
        for fit in fits:
            origin = pd.Timestamp(fit['origin'])
            past = np.asarray(dates < origin)
            self.assertEqual(fit['matches'], int((past & (outcomes != 1)).sum()))
            self.assertEqual({k: fit['low_score'][k] for k in ('rho', 'delta', 'status')},
                             {k: c2_fits[fit['origin']][k] for k in ('rho', 'delta', 'status')})
        last = fits[-1]
        origin = pd.Timestamp(last['origin'])
        past = np.asarray(dates < origin)
        age = (origin - dates[past]).total_seconds().to_numpy() / 86400
        half_life = CFG['production_v2']['half_life_days']
        expected = rs.fit(c2_probs[past], outcomes[past], age, half_life)
        self.assertEqual(last['slope'], expected['slope'])
        self.assertNotEqual(last['slope'], rs.fit(c_probs[past], outcomes[past], age, half_life)['slope'])
        self.assertAlmostEqual(last['slope'], 1.25, delta=.15)

    def test_a_later_result_never_changes_an_earlier_forecast(self):
        rows = self.rows()
        changed = [dict(r) for r in rows]
        for r in changed[-300:]:
            r['home_goals'], r['away_goals'] = 3., 0.
        opened = self.window(changed[-300]['date'])
        early = lambda recs: {k: v for k, v in by_fixture(recs).items()
                              if pd.Timestamp(k[0].split('|')[1]) < opened}
        before = early(self.c6[0])
        after = early(eh.low_score_sharpen_candidate(changed, CFG, self.end(rows))[0])
        self.assertGreater(len(before), 1000)
        self.assertEqual(before, after)

    def test_unscored_rows_feed_both_fits_but_are_not_scored(self):
        rows = self.rows()
        for r in rows[:1800]:
            r['scored'] = False
        _, calib, _, fits = eh.low_score_sharpen_candidate(rows, CFG, self.end(rows))
        self.assertEqual(len(calib), 1200)
        self.assertEqual(fits[0]['status'], 'fitted')
        self.assertEqual(fits[0]['low_score']['status'], 'fitted')

    def test_skipped_when_not_kept(self):
        rows = self.rows()
        self.assertEqual(eh.low_score_sharpen_candidate(rows, CFG, self.end(rows), keep={'C', 'C2', 'C5', 'M'})[0], [])


class HarnessCandidateTest(unittest.TestCase):
    """C6 on real EPL folds: registered, and identical whatever any odds field says."""

    @classmethod
    def setUpClass(cls):
        import historical_benchmark as hb
        data, _, _ = hb.load_history(REPO / '.football_cache', 'EPL',
                                     {**CFG, 'seasons': ['2122', '2223', '2324'], 'test_end_exclusive': '2024-07-01'})
        cls.origin, cls.data = pd.Timestamp('2024-03-01'), data

    @staticmethod
    def fit(train, origin):
        from football_value_pipeline_v2_standalone import DixonColesModel
        return DixonColesModel(half_life_days=480., l2=.08, max_goals=10, shot_features=True,
                               bbs_statistics=False).fit(train.copy(), as_of=origin)

    def test_c6_is_registered(self):
        self.assertIn('C6', eh.CANDIDATES)
        self.assertIn('research_low_score_sharpen.py', eh.SETUP_FILES)
        self.assertIn('C6', eh.common_cohort.__defaults__[0])

    def research_rows(self, data):
        """C's forecasts of 40 matches before the origin (fit only) and 5 after (scored)."""
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

    def test_c6_ignores_every_odds_field_in_the_match_and_the_training_history(self):
        odds = [c for c in self.data.columns if c.startswith(ODDS_PREFIXES) and c not in ('AHh', 'AHCh')]
        self.assertGreater(len(odds), 20)
        shaken = self.data.copy()
        shaken[odds] = shaken[odds].apply(pd.to_numeric, errors='coerce') * 1.02 + .01
        (rows, a), (rows2, b) = self.research_rows(self.data), self.research_rows(shaken)
        self.assertEqual(rows, rows2)  # C's goal rates and the scores: everything C6 reads
        for x, y in zip(a, b):
            np.testing.assert_array_equal(x['C'], y['C'])
            self.assertFalse(np.array_equal(x['M'], y['M']))  # the market reference did move
        end = self.origin + pd.Timedelta(days=30)
        # Force real fits on the 40 earlier forecasts: a real C2 correction and a real slope.
        with patch.object(rls, 'MIN_MATCHES', 10), patch.object(rs, 'MIN_MATCHES', 10):
            first = eh.low_score_sharpen_candidate(rows, CFG, end)
            second = eh.low_score_sharpen_candidate(rows2, CFG, end)
            c2 = eh.low_score_candidate(rows, CFG, end)
        last = first[3][-1]
        self.assertEqual((last['status'], last['low_score']['status']), ('fitted', 'fitted'))
        self.assertNotEqual(last['slope'], 1.)
        self.assertTrue(first[0])
        self.assertEqual(first[0], second[0])
        self.assertEqual(first[1], second[1])
        self.assertNotEqual(by_fixture(first[0]), by_fixture(c2[0]))  # the slope really moved C2


if __name__ == '__main__':
    unittest.main()
