"""Candidates C7 and C8 (research_rate_calibration): the fitted rate calibration on C0's goal rates, C8's Elo
term, their walk-forward fits and their independence from odds (docs/plan.md, Phase 2g)."""
import json
from pathlib import Path
import tempfile
import unittest
from unittest import mock
from unittest.mock import patch

import numpy as np
import pandas as pd

import evaluation_harness as eh
from tests import epl_research_rows as epl
import research_low_score as rls
import research_rate_calibration as rrc
from team_research import research_grid

REPO = Path(__file__).resolve().parents[1]
CFG = json.loads((REPO / 'evaluation_harness_config.json').read_text(encoding='utf-8'))
TRUE = {'a_home': .08, 'a_away': -.05, 'b': .8, 'c': .3}


def simulate(n, params=TRUE, seed=7, rho=0., delta=0.):
    """C0's goal rates, Elo differences / 400 and scores drawn from the calibrated grid, with ages in days."""
    rng = np.random.default_rng(seed)
    rates = np.column_stack([rng.uniform(.6, 2.6, n), rng.uniform(.5, 2.2, n)])
    z = rng.normal(.15, .35, n)
    goals = np.zeros((n, 2))
    for i in range(n):
        grid = rrc.grid(rates[i], params, {'rho': rho, 'delta': delta}, z[i])
        goals[i] = np.unravel_index(rng.choice(grid.size, p=grid.ravel()), grid.shape)
    return rates, goals[:, 0], goals[:, 1], (np.arange(n) % 700).astype(float), z


def by_fixture(records):
    return {(r['fixture_key'], r['market']): r['log_loss'] for r in records}


class RatesTest(unittest.TestCase):
    def test_neutral_parameters_give_exactly_c0(self):
        for rates in ((1.4, 1.1), (0.3, 2.9), (3.2, 0.4), (12.7, 0.2)):
            self.assertEqual(rrc.calibrated_rates(rates, rrc.NEUTRAL), list(rates))
            self.assertEqual(rrc.calibrated_rates(rates, rrc.NEUTRAL, z=.8), list(rates))  # c = 0: Elo unused
            np.testing.assert_array_equal(rrc.grid(rates, rrc.NEUTRAL, rls.NEUTRAL), research_grid(list(rates)))

    def test_the_calibration_is_the_stated_log_linear_rule(self):
        home, away = rrc.calibrated_rates((1.6, 0.9), TRUE, z=.5)
        self.assertAlmostEqual(np.log(home), .08 + .8 * np.log(1.6) + .3 * .5, places=12)
        self.assertAlmostEqual(np.log(away), -.05 + .8 * np.log(0.9) - .3 * .5, places=12)
        # b below 1 pulls an extreme rate toward the centre.
        self.assertLess(rrc.calibrated_rates((12.7, 1.), {**rrc.NEUTRAL, 'b': .8})[0], 12.7)

    def test_a_stronger_home_side_by_elo_raises_the_home_rate_and_lowers_the_away_rate(self):
        level = rrc.calibrated_rates((1.5, 1.2), TRUE, z=0.)
        ahead = rrc.calibrated_rates((1.5, 1.2), TRUE, z=.6)
        self.assertGreater(ahead[0], level[0])
        self.assertLess(ahead[1], level[1])
        self.assertAlmostEqual(ahead[0] / level[0], level[1] / ahead[1], places=12)  # +c z and -c z

    def test_an_elo_term_without_an_elo_difference_is_refused(self):
        for z in (None, float('nan')):
            with self.assertRaises(ValueError):
                rrc.calibrated_rates((1.5, 1.2), TRUE, z=z)
        with self.assertRaises(ValueError):
            rrc.calibrated_rates((0., 1.2), rrc.NEUTRAL)

    def test_the_grid_is_c2s_grid_on_the_calibrated_rates(self):
        low = {'rho': -.06, 'delta': .09}
        grid = rrc.grid((1.5, 1.2), TRUE, low, z=.4)
        np.testing.assert_array_equal(grid, rls.adjusted_grid(rrc.calibrated_rates((1.5, 1.2), TRUE, .4), low))
        self.assertAlmostEqual(float(grid.sum()), 1., places=12)

    def test_the_elo_difference_is_the_ratings_fixture_difference_over_400(self):
        from elo_ratings import EloRatings, fixture_features
        ratings = EloRatings()
        for day, (home, away, hg, ag) in enumerate((('A', 'B', 2, 0), ('B', 'C', 1, 1), ('C', 'A', 0, 3))):
            ratings.update(pd.Timestamp('2024-01-01') + pd.Timedelta(days=7 * day), home, away, hg, ag)
        self.assertEqual(rrc.elo_z(ratings, 'A', 'B'), fixture_features(ratings, 'A', 'B')['elo_rating_diff'] / 400)
        self.assertGreater(rrc.elo_z(ratings, 'A', 'B'), rrc.elo_z(ratings, 'B', 'A'))
        self.assertIsNone(rrc.elo_z(ratings, 'A', 'never seen'))


class FitTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = simulate(8000)

    def test_c8_fit_recovers_known_parameters(self):
        rates, hg, ag, age, z = self.data
        fitted = rrc.fit(rates, hg, ag, age, 1e6, z)
        self.assertEqual((fitted['status'], fitted['elo'], fitted['matches']), ('fitted', True, 8000))
        for key, tolerance in (('a_home', .05), ('a_away', .05), ('b', .08), ('c', .08)):
            self.assertAlmostEqual(fitted[key], TRUE[key], delta=tolerance)
        self.assertGreater(fitted['neutral_minus_fitted_loss'], 0)

    def test_c7_fit_has_no_elo_term(self):
        rates, hg, ag, age, _ = simulate(6000, {**TRUE, 'c': 0.}, seed=11)
        fitted = rrc.fit(rates, hg, ag, age, 1e6)
        self.assertEqual((fitted['status'], fitted['elo'], fitted['c']), ('fitted', False, 0.))
        for key, tolerance in (('a_home', .05), ('a_away', .05), ('b', .08)):
            self.assertAlmostEqual(fitted[key], TRUE[key], delta=tolerance)

    def test_goals_drawn_from_c0s_own_rates_fit_near_neutral(self):
        rates, hg, ag, age, z = simulate(8000, rrc.NEUTRAL, seed=5)
        fitted = rrc.fit(rates, hg, ag, age, 1e6, z)
        for key, tolerance in (('a_home', .05), ('a_away', .05), ('c', .06)):
            self.assertAlmostEqual(fitted[key], 0., delta=tolerance)
        self.assertAlmostEqual(fitted['b'], 1., delta=.08)

    def test_the_fit_is_the_maximum_of_the_poisson_likelihood(self):
        rates, hg, ag, age, z = (v[:3000] for v in self.data)
        fitted = rrc.fit(rates, hg, ag, age, 480., z)
        weights = np.exp(-np.log(2) * age / 480.)

        def likelihood(params):
            calibrated = np.array([rrc.calibrated_rates(r, params, v) for r, v in zip(rates, z)])
            return float(weights @ (hg * np.log(calibrated[:, 0]) - calibrated[:, 0]
                                    + ag * np.log(calibrated[:, 1]) - calibrated[:, 1]))

        best = likelihood(fitted)
        for key in rrc.PARAMETERS:
            for step in (-.01, .01):
                self.assertLess(likelihood({**fitted, key: fitted[key] + step}), best)

    def test_recent_matches_weigh_more(self):
        rates, hg, ag, _, z = (v[:4000] for v in self.data)
        old = simulate(4000, {**TRUE, 'c': -.3}, seed=3)
        stack = lambda a, b: np.concatenate([a, b])
        args = (stack(rates, old[0]), stack(hg, old[1]), stack(ag, old[2]),
                stack(np.full(4000, 10.), np.full(4000, 2000.)))
        both = stack(z, old[4])
        self.assertGreater(rrc.fit(*args, 200., both)['c'], rrc.fit(*args, 1e6, both)['c'])

    def test_warm_up_is_neutral(self):
        rates, hg, ag, age, z = (v[:rrc.MIN_MATCHES - 1] for v in self.data)
        for elo in (None, z):
            fitted = rrc.fit(rates, hg, ag, age, 480., elo)
            self.assertEqual({k: fitted[k] for k in rrc.PARAMETERS}, rrc.NEUTRAL)
            self.assertEqual(fitted['status'], 'warm_up')
        self.assertEqual(rrc.MIN_MATCHES, rls.MIN_MATCHES)  # C2's warm-up

    def test_bad_fit_rows_are_refused(self):
        rates, hg, ag, age, z = (v[:rrc.MIN_MATCHES].copy() for v in self.data)
        late = age.copy()
        late[0] = -1.
        with self.assertRaises(ValueError):
            rrc.fit(rates, hg, ag, late, 480.)
        missing = z.copy()
        missing[0] = np.nan
        with self.assertRaises(ValueError):
            rrc.fit(rates, hg, ag, age, 480., missing)
        zero = rates.copy()
        zero[0, 0] = 0.
        with self.assertRaises(ValueError):
            rrc.fit(zero, hg, ag, age, 480.)


class WalkForwardTest(unittest.TestCase):
    """rate_calibration_candidate: each window is fitted only on matches forecast and played before it.

    1,500 simulated forecasts (500 days) with both fit minimums lowered from 1,000 to 500 matches for this
    class only, so there are warm-up windows and fitted ones; each walk-forward is run once and shared."""
    N, MIN_MATCHES = 1500, 500

    @classmethod
    def setUpClass(cls):
        cls.enterClassContext(patch.object(rls, 'MIN_MATCHES', cls.MIN_MATCHES))
        cls.enterClassContext(patch.object(rrc, 'MIN_MATCHES', cls.MIN_MATCHES))
        rates, hg, ag, _, z = simulate(cls.N, seed=3, rho=-.08, delta=.12)
        start = pd.Timestamp(CFG['test_start'])
        cls.base = [epl.research_row('EPL' if i % 2 else 'SerieA', start + pd.Timedelta(hours=8 * i),
                                     rates[i] * 1.3, hg[i], ag[i], base_rates=rates[i], elo_z=float(z[i]))
                    for i in range(cls.N)]
        cls.results = {name: eh.rate_calibration_candidate(cls.rows(), CFG, cls.end(), name)
                       for name in eh.RATE_CALIBRATION_CANDIDATES}

    @classmethod
    def rows(cls):
        return [dict(r) for r in cls.base]

    @classmethod
    def end(cls):
        return cls.base[-1]['date'] + pd.Timedelta(days=1)

    def opened(self, cut):
        return max(w[0] for w in eh.fold_windows(CFG, self.end()) if w[0] <= cut)

    def test_fits_use_only_earlier_matches(self):
        rows = self.rows()
        for name, (records, calib, coverage, fits) in self.results.items():
            self.assertEqual(fits[0]['status'], 'warm_up')
            self.assertEqual(fits[-1]['status'], 'fitted')
            self.assertEqual(fits[-1]['elo'], eh.RATE_CALIBRATION_CANDIDATES[name])
            for fit in fits:
                earlier = sum(r['date'] < pd.Timestamp(fit['origin']) for r in rows)
                self.assertEqual(fit['matches'], earlier)
                self.assertEqual(fit['low_score']['matches'], earlier)
            self.assertEqual(len(calib), len(rows))
            self.assertEqual({r['candidate'] for r in records}, {name})
            self.assertEqual(sum(v for k, v in coverage.items() if k.endswith(f':{name}:available')), len(rows))
        self.assertEqual(self.results['C7'][3][-1]['c'], 0.)
        self.assertGreater(self.results['C8'][3][-1]['c'], .1)  # the simulated Elo effect is found
        self.assertLess(self.results['C8'][3][-1]['b'], 1.)

    def test_warm_up_windows_are_c0_exactly(self):
        for name, (records, _, _, fits) in self.results.items():
            warm = [f for f in fits if f['status'] == 'warm_up']
            self.assertTrue(warm)
            self.assertTrue(all(f['low_score']['status'] == 'warm_up' for f in warm))
            stop = pd.Timestamp(warm[-1]['end_exclusive'])
            expected = []
            for r in sorted(self.rows(), key=lambda r: r['date']):
                if r['date'] < stop:
                    c0 = eh.rb.matrix_value(research_grid(r['base_rates']))
                    expected.extend(eh.rb.score_fixture(r['identity'], {name: c0}, r['home_goals'], r['away_goals']))
            self.assertGreater(len(expected), 1000)
            self.assertEqual(records[:len(expected)], expected)

    def test_the_form_blended_goal_rates_are_never_read(self):
        rows = self.rows()
        for r in rows:
            r['goal_rates'] = [9., 9.]
        for name, (records, _, _, fits) in self.results.items():
            again = eh.rate_calibration_candidate(rows, CFG, self.end(), name)
            self.assertEqual(again[0], records)
            self.assertEqual(again[3], fits)

    def test_low_score_fit_reads_the_candidates_own_earlier_rates(self):
        for name, elo in eh.RATE_CALIBRATION_CANDIDATES.items():
            research, rates, windows = eh.rate_calibration_walk_forward(self.rows(), CFG, self.end(), elo)
            dates = pd.DatetimeIndex([r['date'] for r in research])
            window = windows[-1]
            self.assertEqual(window['low_score']['status'], 'fitted')
            past = np.asarray(dates < window['origin'])
            goals = np.array([(r['home_goals'], r['away_goals']) for r in research])
            age = (window['origin'] - dates[past]).total_seconds().to_numpy() / 86400
            half_life = CFG['production_v2']['half_life_days']
            self.assertEqual(window['low_score'], rls.fit(rates[past], goals[past, 0], goals[past, 1], age, half_life))
            # Each earlier match keeps the rates it was forecast with (its own window's calibration).
            earlier = next(w for w in windows if w['calibration'] and w['calibration']['status'] == 'fitted')
            i = next(i for i in range(len(research)) if earlier['origin'] <= dates[i] < earlier['stop'])
            self.assertEqual(list(rates[i]), rrc.calibrated_rates(research[i]['base_rates'], earlier['calibration'],
                                                                  research[i]['elo_z'] if elo else None))
            self.assertNotEqual(earlier['calibration'], window['calibration'])

    def test_a_later_result_rate_or_elo_difference_never_changes_an_earlier_forecast(self):
        changed = self.rows()
        for r in changed[-300:]:
            r['home_goals'], r['away_goals'] = 0., 0.
            r['base_rates'] = [3.1, .4]
            r['elo_z'] = -2.
        opened = self.opened(changed[-300]['date'])
        early = lambda records: {k: v for k, v in by_fixture(records).items()
                                 if pd.Timestamp(k[0].split('|')[1]) < opened}
        for name, (records, _, _, _) in self.results.items():
            before = early(records)
            after = early(eh.rate_calibration_candidate(changed, CFG, self.end(), name)[0])
            self.assertGreater(len(before), 1000)
            self.assertEqual(before, after)

    def test_unscored_rows_feed_the_fits_but_are_not_scored(self):
        rows = self.rows()
        for r in rows[:750]:
            r['scored'] = False
        for name in eh.RATE_CALIBRATION_CANDIDATES:
            _, calib, _, fits = eh.rate_calibration_candidate(rows, CFG, self.end(), name)
            self.assertEqual(len(calib), 750)
            self.assertEqual(fits[0]['status'], 'fitted')  # fitted on unscored forecasts alone
            self.assertEqual(fits[0]['matches'], sum(r['date'] < pd.Timestamp(fits[0]['origin']) for r in rows))

    def test_c8_without_an_elo_difference_makes_no_forecast_and_stays_out_of_the_fits(self):
        rows = self.rows()
        missing = set(range(0, len(rows), 10))
        for i in missing:
            rows[i]['elo_z'] = None
        records, calib, coverage, fits = eh.rate_calibration_candidate(rows, CFG, self.end(), 'C8')
        fitted = [f for f in fits if f['status'] == 'fitted']
        for fit in fits:
            self.assertEqual(fit['matches'], sum(r['date'] < pd.Timestamp(fit['origin']) and r['elo_z'] is not None
                                                 for r in rows))
        first = pd.Timestamp(fitted[0]['origin'])
        unforecast = [r for r in rows if r['elo_z'] is None and r['date'] >= first]
        self.assertTrue(unforecast)
        self.assertEqual(sum(v for k, v in coverage.items() if k.endswith(':C8:no calibrated goal rates')),
                         len(unforecast))
        self.assertFalse({r['identity']['fixture_key'] for r in unforecast} & {r['fixture_key'] for r in records})
        # C7 never reads the Elo difference: it forecasts every match, identically.
        self.assertEqual(eh.rate_calibration_candidate(rows, CFG, self.end(), 'C7')[0], self.results['C7'][0])

    def test_skipped_when_not_kept(self):
        for name in eh.RATE_CALIBRATION_CANDIDATES:
            self.assertEqual(eh.rate_calibration_candidate(self.rows(), CFG, self.end(), name, keep={'C', 'M'})[0], [])


class HarnessCandidateTest(unittest.TestCase):
    """C7 and C8 on real EPL folds: registered, and identical whatever any odds field says."""

    def test_candidates_are_registered_and_may_be_declared(self):
        for name in ('C7', 'C8'):
            self.assertIn(name, eh.CANDIDATES)
            self.assertIn(name, eh.WALK_FORWARD_CANDIDATES)
        for name in ('research_rate_calibration.py', 'elo_ratings.py', 'research_low_score.py'):
            self.assertIn(name, eh.SETUP_FILES)
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'declaration.json'
            for candidate, baseline in (('C7', 'C6'), ('C8', 'C6'), ('C8', 'C0')):
                path.write_text(json.dumps({
                    'candidate': candidate, 'baseline': baseline, 'primary_metric': 'AH all',
                    'draw_sensitive_lines': [-0.5, 0, 0.5], 'declared_by': 'test', 'declared_at': '2026-11-16',
                    'calibration_tolerance': CFG['calibration_tolerance']['name']}), encoding='utf-8')
                declared = eh.validate_declaration(path, CFG, {'sha256': 'a' * 64}, Path(tmp) / 'ledger.json')
                self.assertEqual((declared['candidate'], declared['baseline']), (candidate, baseline))

    def test_c7_and_c8_ignore_every_odds_field_in_the_match_and_the_training_history(self):
        # Every price moves; handicap lines (AHh, AHCh) keep valid quarter values.
        self.assertGreater(len(epl.odds_columns()), 20)
        (rows, a), (rows2, b) = epl.research_rows(), epl.research_rows(moved=True)
        # C0's goal rates, the Elo differences and the scores: everything C7 and C8 read.
        self.assertEqual(rows, rows2)
        self.assertTrue(all(np.isfinite(r['elo_z']) for r in rows))
        self.assertTrue(all(r['base_rates'] != r['goal_rates'] for r in rows))  # C0's rates, not C's
        for x, y in zip(a, b):
            np.testing.assert_array_equal(x['C0'], y['C0'])
            self.assertFalse(np.array_equal(x['M'], y['M']))  # the market reference did move
        # Force real fits on the 40 earlier forecasts (below MIN_MATCHES both fits are neutral by design).
        end = epl.ORIGIN + pd.Timedelta(days=30)
        with patch.object(rls, 'MIN_MATCHES', 10), patch.object(rrc, 'MIN_MATCHES', 10):
            for name, elo in eh.RATE_CALIBRATION_CANDIDATES.items():
                first = eh.rate_calibration_candidate(rows, CFG, end, name)
                second = eh.rate_calibration_candidate(rows2, CFG, end, name)
                fit = first[3][-1]
                self.assertEqual((fit['status'], fit['low_score']['status']), ('fitted', 'fitted'))
                self.assertNotEqual(fit['b'], 1.)
                self.assertEqual(fit['c'] != 0., elo)
                self.assertTrue(first[0])
                self.assertEqual(first[0], second[0])
                self.assertEqual(first[1], second[1])
                self.assertEqual(first[3], second[3])
                c0 = [p for x in a[-5:] for p in eh.rb.score_fixture({}, {name: x['C0']}, 1, 0)]
                self.assertNotEqual([r['log_loss'] for r in first[0]], [r['log_loss'] for r in c0][:len(first[0])])

    def test_the_elo_difference_reads_only_training_rows_before_the_fold_origin(self):
        from elo_ratings import fit_history
        train, model = epl.scored_fold()
        later = epl.data()[epl.data().Date >= epl.ORIGIN]
        row = later.iloc[0]
        context, _, _ = eh.research_context(row, train, epl.ORIGIN, model)
        z = eh.rate_calibration_inputs(row, context, fit_history(train))['elo_z']
        # Results on or after the origin, however different, are not in the fold's training rows.
        self.assertLess(train.Date.max(), epl.ORIGIN)
        flipped = epl.data().copy()
        flipped.loc[flipped.Date >= epl.ORIGIN, ['FTHG', 'FTAG']] = [0, 7]
        self.assertEqual(eh.rate_calibration_inputs(row, context, fit_history(flipped[flipped.Date < epl.ORIGIN]))['elo_z'], z)
        # An earlier result does move it (positive control), and no price column does.
        earlier = train.copy()
        last = earlier.index[(earlier.HomeTeam == row.HomeTeam) | (earlier.AwayTeam == row.HomeTeam)][-1]
        earlier.loc[last, ['FTHG', 'FTAG']] = [9, 0] if earlier.loc[last, 'HomeTeam'] == row.HomeTeam else [0, 9]
        self.assertNotEqual(eh.rate_calibration_inputs(row, context, fit_history(earlier))['elo_z'], z)
        shaken = epl.shaken()
        self.assertEqual(eh.rate_calibration_inputs(row, context, fit_history(shaken[shaken.Date < epl.ORIGIN]))['elo_z'], z)


class LeagueRunTest(unittest.TestCase):
    """evaluate_league: the ratings behind C8's Elo difference are fitted on each fold's training rows, and
    a holdout run would still feed C7's and C8's fits with the earlier, unscored forecasts."""
    RESULTS = ('FTHG', 'FTAG', 'FTR', 'HTHG', 'HTAG', 'HTR', 'HS', 'AS', 'HST', 'AST', 'HF', 'AF', 'HC', 'AC',
               'HY', 'AY', 'HR', 'AR')

    def test_elo_ratings_stop_before_each_fold_origin_and_holdout_runs_feed_the_fits(self):
        import elo_ratings
        # Two fold windows across the holdout start (16 Jan 2026), as in the harness lock test.
        cfg = {**CFG, 'test_start': '2026-01-05', 'end_exclusive': '2026-01-19', 'seasons': ['2324', '2425', '2526']}
        cache = str(REPO / '.football_cache')
        load, fit_history = eh.hb.load_history, elo_ratings.fit_history
        fitted = []

        def without_holdout_results(cache_dir, league, load_cfg):
            """The cached history with every real holdout result blanked: no run below can read one."""
            data, sources, extra = load(cache_dir, league, load_cfg)
            locked = data.Date.map(lambda d: eh.phase(d, league, cfg) == 'holdout')
            data = data.copy()
            data.loc[locked, [c for c in self.RESULTS if c in data]] = np.nan
            return data, sources, extra

        def recorded(history, **settings):
            fitted.append(history.Date.max())
            return fit_history(history, **settings)

        identities_only = lambda identity, matrices, home_goals, away_goals: [
            {**identity, 'candidate': c} for c in matrices]
        origins = [w[0] for w in eh.fold_windows(cfg, pd.Timestamp(cfg['end_exclusive']))]
        with mock.patch.object(eh.hb, 'load_history', without_holdout_results), \
                mock.patch.object(elo_ratings, 'fit_history', recorded):
            research = eh.evaluate_league('Eredivisie', cache, cfg, False, keep={'C', 'C0', 'C8'})[6]
            self.assertEqual(len(fitted), len(origins))
            self.assertTrue(all(last < origin for last, origin in zip(fitted, origins)))
            self.assertTrue(research)
            self.assertEqual({r['identity']['phase'] for r in research}, {'validation'})  # no holdout row
            self.assertTrue(all(np.isfinite(r['elo_z']) and len(r['base_rates']) == 2 for r in research))
            fitted.clear()
            # Without C8 no ratings are fitted and no Elo difference is carried.
            plain = eh.evaluate_league('Eredivisie', cache, cfg, False, keep={'C', 'C7'})[6]
            self.assertEqual(fitted, [])
            self.assertTrue(all(r['elo_z'] is None for r in plain))
            self.assertEqual([r['base_rates'] for r in plain], [r['base_rates'] for r in research])
            # A holdout run (results blanked here, nothing scored) keeps the earlier forecasts for the fits.
            with mock.patch.object(eh.rb, 'score_fixture', identities_only):
                for name in eh.RATE_CALIBRATION_CANDIDATES:
                    rows = eh.evaluate_league('Eredivisie', cache, cfg, True, keep={name, 'C0', 'M'})[6]
                    unscored = [r for r in rows if not r['scored']]
                    self.assertEqual(len(unscored), len(research))
                    self.assertEqual({r['identity']['phase'] for r in unscored}, {'validation'})
                    self.assertEqual([r['base_rates'] for r in unscored], [r['base_rates'] for r in research])
                    held = [r for r in rows if r['scored']]
                    self.assertTrue(held and all(r['identity']['phase'] == 'holdout' for r in held))
                    self.assertTrue(all(np.isnan(r['home_goals']) for r in held))  # blank: never a real result


if __name__ == '__main__':
    unittest.main()
