"""CE2, CE3 and CE4 (european_candidates.py): independence from odds, walk-forward, pre-kickoff domestic data,
the European lock, and the fixed blend weight.

Real cached results are used only for locked runs (never a European holdout score); every run that
includes the holdout uses synthetic results.
"""
import hashlib
import json
from pathlib import Path
import unittest
from unittest import mock

import numpy as np
import pandas as pd

import european_candidates as ec
import european_results as er
import evaluation_harness as eh

REPO = Path(__file__).resolve().parents[1]
CACHE = REPO / '.football_cache'
CFG = json.loads((REPO / 'evaluation_harness_config.json').read_text(encoding='utf-8'))
END = CFG['european']['end_exclusive']
ODDS = ('PSH', 'PSD', 'PSA', 'B365H', 'B365D', 'B365A', 'P>2.5', 'P<2.5', 'AHh', 'PAHH', 'PAHA', 'AvgH', 'MaxH')
NAMES = ec.CANDIDATE_NAMES


def window(**european):
    return {**CFG, 'european': {**CFG['european'], **european}}


def synthetic(start, matches, teams=8, seed=7):
    rng = np.random.default_rng(seed)
    names = [f'Club {i}' for i in range(teams)]
    rows = []
    for k in range(0, matches, teams // 2):
        order = rng.permutation(teams)
        for home, away in zip(order[0::2], order[1::2]):
            rows.append({'Date': pd.Timestamp(start) + pd.Timedelta(days=3 * (k // (teams // 2))),
                         'HomeTeam': names[home], 'AwayTeam': names[away], 'FTHG': int(rng.poisson(1.5)),
                         'FTAG': int(rng.poisson(1.1)), 'Season': '2024', 'stage': 'LEAGUE_STAGE',
                         'stage_group': 'league phase'})
    return pd.DataFrame(rows[:matches])


def fake_strength(team, league_count=8):
    """A deterministic domestic strength per team name (tests only)."""
    h = int(hashlib.sha256(team.encode()).hexdigest()[:8], 16)
    att, dfn = ((h % 41) - 20) / 100, (((h // 41) % 41) - 20) / 100
    return {'goals': (att, dfn), 'xg': (att * .9, dfn * .9), 'league': CFG['leagues'][h % league_count],
            'domestic_matches': 30, 'used_xg': True}


def fake_strengths(data):
    out = {}
    for competition, frame in data.items():
        for r in frame.itertuples(index=False):
            key = '|'.join((competition, r.Date.date().isoformat(), r.HomeTeam, r.AwayTeam))
            out[key] = {'home': fake_strength(r.HomeTeam), 'away': fake_strength(r.AwayTeam)}
    return out


def small_minimums():
    return mock.patch.multiple(ec, MIN_DECIDED=40, FACTOR_MIN_MATCHES=30)


def by_candidate(calib):
    return {(r['candidate'], r['fixture_key']): r['probs'] for r in calib}


class SyntheticTest(unittest.TestCase):
    CFG = window(min_train=40, test_start='2023-09-04', end_exclusive='2024-07-01', step_days=14,
                 development_start={'UCL': '2023-09-04', 'UEL': '2023-09-04'})

    @classmethod
    def setUpClass(cls):
        cls.data = {'UCL': synthetic('2023-06-01', 520), 'UEL': synthetic('2023-06-01', 520, seed=8)}
        cls.strengths = fake_strengths(cls.data)
        with small_minimums():
            cls.base = eh.european(None, cls.CFG, data=cls.data, strengths=cls.strengths, extras=(extras := {}))
        cls.extras = extras

    def test_every_candidate_is_built_and_actually_moves(self):
        calib = self.base[3]
        found = {r['candidate'] for r in calib}
        self.assertEqual(found, {'CE', *NAMES})
        probs = by_candidate(calib)
        keys = {k for c, k in probs if c == 'CE'}
        for name in NAMES:
            self.assertTrue(any(probs[(name, k)] != probs[('CE', k)] for k in keys), name)
        fits = self.extras['fits']
        self.assertTrue(any(f['CE2']['pooled']['status'] == 'fitted' for f in fits))
        self.assertTrue(any(f['factors']['xg']['status'] == 'fitted' for f in fits))
        self.assertLess(ec.SLOPE_BOUNDS[0], 0.5)  # wider than C5's: CE is too sharp, so its slope may go well below 1

    def test_warm_up_folds_equal_ce_exactly(self):
        probs = by_candidate(self.base[3])
        first = {f['origin'] for f in self.extras['fits'] if f['CE2']['pooled']['status'] == 'warm_up'
                 and f['factors']['xg']['status'] == 'warm_up' and f['CE4']['pooled']['status'] == 'warm_up'}
        self.assertTrue(first)
        windows = [(o, s) for o, s in eh.fold_windows(self.CFG['european'], pd.Timestamp(self.CFG['european']['end_exclusive']))
                   if o.date().isoformat() in first]
        keys = [k for c, k in probs if c == 'CE' and any(o <= pd.Timestamp(k.split('|')[1]) < s for o, s in windows)]
        self.assertTrue(keys)
        for name in NAMES:
            for k in keys:
                self.assertEqual(probs[(name, k)], probs[('CE', k)], (name, k))

    def test_odds_never_reach_any_candidate(self):
        rng = np.random.default_rng(3)
        priced = {c: f.assign(**{o: rng.uniform(1.1, 15., len(f)) for o in ODDS}) for c, f in self.data.items()}
        with small_minimums():
            again = eh.european(None, self.CFG, data=priced, strengths=self.strengths)
        self.assertEqual(self.base[3], again[3])
        self.assertEqual(self.base[0], again[0])

    def test_a_later_european_result_never_changes_an_earlier_forecast(self):
        changed = {c: f.copy() for c, f in self.data.items()}
        cut = pd.Timestamp('2024-03-01')
        later = changed['UEL'].index[changed['UEL'].Date >= cut]
        changed['UEL'].loc[later, ['FTHG', 'FTAG']] = [[6, 0]] * len(later)
        with small_minimums():
            after = eh.european(None, self.CFG, data=changed, strengths=self.strengths)
        b, a = by_candidate(self.base[3]), by_candidate(after[3])
        origin = max(o for o, _ in eh.fold_windows(self.CFG['european'], pd.Timestamp(self.CFG['european']['end_exclusive']))
                     if o <= cut)
        earlier = [k for k in b if k[1].split('|')[1] < origin.date().isoformat()]
        moved = [k for k in b if k[1].split('|')[1] >= '2024-04-01' and k in a and k[0] != 'CE']
        self.assertTrue(earlier and moved)
        for k in earlier:
            self.assertEqual(b[k], a[k], k)
        self.assertTrue(any(b[k] != a[k] for k in moved))

    def test_holdout_runs_score_only_the_holdout_for_every_candidate(self):
        cfg = window(min_train=40, test_start='2024-09-01', end_exclusive='2026-11-01', step_days=28)
        data = {'UCL': synthetic('2024-09-01', 420), 'UEL': synthetic('2024-09-01', 420, seed=8)}
        strengths = fake_strengths(data)
        with small_minimums():
            locked, _, coverage, _ = eh.european(None, cfg, data=data, strengths=strengths)
            self.assertNotIn('holdout', {r['phase'] for r in locked})
            self.assertGreater(coverage['UCL:locked_holdout'], 0)
            for name in ('CE2', 'CE3', 'CE4'):
                run, folds, _, calib = eh.european(None, cfg, include_holdout=True, keep={name, 'CE'}, data=data,
                                                   strengths=strengths)
                self.assertTrue(run)
                self.assertEqual({(r['league'], r['phase']) for r in run}, {('UCL', 'holdout')})
                self.assertEqual({r['candidate'] for r in calib}, {name, 'CE'})
                # Its fits learned from the earlier UEL and UCL matches too (forecast, not scored).
                fits = next(f['walk_forward_fits'] for f in folds if f.get('candidate') == 'CE2-CE4')
                self.assertTrue(any(f['CE2']['decided']['UEL'] > 0 for f in fits))


class FitTest(unittest.TestCase):
    def rows(self, n=200, seed=1):
        rng = np.random.default_rng(seed)
        out = []
        for i in range(n):
            lh, la = CFG['leagues'][i % 8], CFG['leagues'][(i * 3 + 1) % 8]
            s = {'goals': (rng.normal(0, .2), rng.normal(0, .2)), 'xg': (0., 0.)}
            t = {'goals': (rng.normal(0, .2), rng.normal(0, .2)), 'xg': (0., 0.)}
            out.append({'date': pd.Timestamp('2019-01-01') + pd.Timedelta(days=i), 'competition': 'UCL' if i % 2 else 'UEL',
                        'home': (s, lh), 'away': (t, la), 'home_goals': int(rng.poisson(1.5)), 'away_goals': int(rng.poisson(1.1))})
        return out

    def test_factors_use_only_earlier_european_matches_and_shrink_when_thin(self):
        rows = self.rows()
        origin = pd.Timestamp('2019-05-01')
        fit = ec.fit_factors(rows, origin, CFG['leagues'], 'goals')
        self.assertEqual(fit['status'], 'fitted')
        changed = [{**r, 'home_goals': 9} if r['date'] >= origin else r for r in rows]
        self.assertEqual(fit, ec.fit_factors(changed, origin, CFG['leagues'], 'goals'))
        self.assertNotEqual(fit, ec.fit_factors(changed, pd.Timestamp('2019-07-01'), CFG['leagues'], 'goals'))
        self.assertEqual(ec.fit_factors(rows, pd.Timestamp('2019-02-01'), CFG['leagues'])['status'], 'warm_up')
        # The prior pulls every league toward equal strength: a league with no matches stays at 0.
        lonely = [r for r in rows if 'SuperLig' not in (r['home'][1], r['away'][1])]
        fit = ec.fit_factors(lonely, pd.Timestamp('2019-07-19'), CFG['leagues'], 'goals')
        self.assertEqual(fit['status'], 'fitted')
        self.assertAlmostEqual(fit['s']['SuperLig'], 0., places=5)

    def test_ce2_rule_pooled_unless_both_competitions_have_1000(self):
        rng = np.random.default_rng(2)
        n = 2400
        probs = rng.dirichlet([4, 2, 3], n)
        outcomes = rng.integers(0, 3, n)
        dates = pd.DatetimeIndex(pd.Timestamp('2015-01-01') + pd.to_timedelta(np.arange(n), 'D'))
        comps = np.array(['UCL'] * 1500 + ['UEL'] * 900)
        fits = ec.slope_fits(probs, outcomes, comps, dates, dates[-1] + pd.Timedelta(days=1))
        self.assertEqual(fits['rule'], 'pooled')  # UEL has fewer than 1,000 decided matches
        comps = np.array(['UCL', 'UEL'] * (n // 2))
        fits = ec.slope_fits(probs, outcomes, comps, dates, dates[-1] + pd.Timedelta(days=1))
        self.assertTrue(all(v >= 700 for v in fits['decided'].values()))
        self.assertEqual(fits['rule'], 'per_competition' if min(fits['decided'].values()) >= 1000 else 'pooled')
        self.assertEqual(ec.chosen_slope(fits, 'UCL', 'rule'), ec.chosen_slope(fits, 'UCL', fits['rule']))
        few = ec.slope_fits(probs[:100], outcomes[:100], comps[:100], dates[:100], dates[99] + pd.Timedelta(days=1))
        self.assertEqual(few['pooled']['slope'], 1.)  # neutral below MIN_DECIDED

    def test_c5_fit_defaults_are_unchanged(self):
        import research_sharpen as rs
        self.assertEqual((rs.MIN_MATCHES, rs.SLOPE_BOUNDS), (1000, (0.5, 2.5)))
        rng = np.random.default_rng(4)
        probs, outcomes = rng.dirichlet([4, 2, 3], 1500), rng.integers(0, 3, 1500)
        age = np.arange(1500.)
        self.assertEqual(rs.fit(probs, outcomes, age, 480.),
                         rs.fit(probs, outcomes, age, 480., min_matches=1000, bounds=(0.5, 2.5)))


class DomesticStrengthTest(unittest.TestCase):
    """Real domestic files: a strength reads only matches before the fold origin, and never a price."""
    @classmethod
    def setUpClass(cls):
        cls.frame = ec.league_frame(CACHE, 'EPL', CFG)
        cls.origin = pd.Timestamp('2023-10-02')

    def strengths(self, frame):
        return ec.league_strengths('EPL', frame, {self.origin.date().isoformat(): ['Arsenal', 'Man City', 'Newcastle']}, CFG)

    def test_no_price_column_and_no_domestic_holdout(self):
        self.assertFalse(set(self.frame.columns) & set(ODDS) - {'HS', 'AS'})
        self.assertEqual(set(self.frame.columns), {'Date', 'HomeTeam', 'AwayTeam', 'FTHG', 'FTAG', 'HS', 'AS', 'HST', 'AST',
                                                   'HxG', 'AxG'})
        for league in CFG['holdout_leagues']:
            f = ec.league_frame(CACHE, league, CFG)
            self.assertFalse(f.Date.map(lambda d, l=league: eh.phase(d, l, CFG) == 'holdout').any(), league)
        self.assertLess(self.frame.Date.min(), pd.Timestamp('2016-01-01'))  # the older domestic files are read

    def test_no_domestic_match_on_or_after_the_origin_reaches_a_strength(self):
        base = self.strengths(self.frame)
        self.assertEqual(len(base), 3)
        changed = self.frame.copy()
        later = changed.Date >= self.origin
        self.assertTrue(later.any())
        changed.loc[later, ['FTHG', 'FTAG', 'HxG', 'AxG']] = [9, 0, 5., 0.]
        self.assertEqual(base, self.strengths(changed))
        earlier = changed.copy()
        last = earlier.index[(earlier.Date < self.origin) & (earlier.HomeTeam == 'Arsenal')][-1]
        earlier.loc[last, ['FTHG', 'FTAG']] = [0, 7]
        self.assertNotEqual(base, self.strengths(earlier))
        # xG (Understat) is used for the five Understat leagues, and changes the strength.
        k = (self.origin.date().isoformat(), 'Arsenal')
        self.assertTrue(base[k]['used_xg'])
        self.assertNotEqual(base[k]['xg'], base[k]['goals'])

    def test_odds_never_reach_a_strength(self):
        rng = np.random.default_rng(9)
        priced = self.frame.assign(**{o: rng.uniform(1.1, 15., len(self.frame)) for o in ODDS if o not in self.frame})
        self.assertEqual(self.strengths(self.frame), self.strengths(priced))


class RealDataTest(unittest.TestCase):
    def test_blend_weight_is_what_its_rule_gives(self):
        e = CFG['european']
        frames = []
        for c in e['competitions']:
            d = er.load_with_backfill(CACHE, c, END)[['Date', 'HomeTeam', 'AwayTeam']]  # dates and names only
            frames.append(d.assign(competition=c, phase=d.Date.map(lambda x, c=c: eh.european_phase(x, c, CFG))))
        rule = ec.blend_weight_rule(pd.concat(frames, ignore_index=True), CACHE, CFG)
        self.assertEqual(rule['weight'], ec.DOMESTIC_WEIGHT)

    def test_the_european_lock_holds_for_every_candidate(self):
        cfg = window(test_start='2024-12-30', end_exclusive='2025-02-24')
        records, _, coverage, calib = eh.european(CACHE, cfg)
        self.assertTrue(records)
        self.assertNotIn('holdout', {r['phase'] for r in records} | {r['phase'] for r in calib})
        self.assertGreater(coverage['UCL:locked_holdout'], 0)
        self.assertTrue({'CE2', 'CE3', 'CE4'} <= {r['candidate'] for r in calib})
        # A window this short has too few earlier European matches for the factors: CE3 is CE exactly.
        ce = {r['fixture_key']: r['probs'] for r in calib if r['candidate'] == 'CE'}
        self.assertEqual({r['fixture_key']: r['probs'] for r in calib if r['candidate'] == 'CE3'}, ce)
        self.assertFalse(any(r.get('domestic_used') for r in calib))

    def test_registered_with_the_harness(self):
        for name in ('CE2', 'CE3', 'CE4'):
            self.assertIn(name, eh.EUROPEAN_CANDIDATES)
        for name in ('european_candidates.py', 'docs/audits/european-reviewed-aliases.json', 'understat_history.py'):
            self.assertIn(name, eh.EUROPEAN_SETUP_FILES)
        # The domestic ledger never holds a European candidate. The European ledger holds exactly one run:
        # CE3n against CE, declared in evaluation/declarations/ce3n_european_holdout.json and scored once on
        # 12 Nov 2026 (not proven). No other European candidate has been scored.
        domestic = json.loads(eh.LEDGER.read_text(encoding='utf-8')) if eh.LEDGER.exists() else []
        self.assertFalse([r for r in domestic if str(r.get('candidate', '')).startswith('CE')])
        european = json.loads(eh.european_ledger(CFG).read_text(encoding='utf-8'))
        self.assertEqual([(r['candidate'], r['baseline'], r['passes_holdout_gate']) for r in european],
                         [('CE3n', 'CE', False)])
        declaration = json.loads((eh.european_ledger(CFG).parent / 'declarations' / 'ce3n_european_holdout.json')
                                 .read_text(encoding='utf-8'))
        self.assertEqual(european[0]['declaration_sha256'],
                         hashlib.sha256(json.dumps(declaration, sort_keys=True).encode()).hexdigest())


if __name__ == '__main__':
    unittest.main()
