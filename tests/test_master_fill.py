"""The new master's fill rule (master-new-fill-rule-v4) and the sharpened cagey probabilities (cagey_sharpen.py).

The fill order exactly as written (every step on the nominated pool only, rule v4: step 1 safe picks as #172; step 2
not-risky fill by chance of profit; step 3 risky fill only when still short; never two picks per match; stop at the
target, or shorter when the nominations cover fewer matches); the chance of
profit per line type (quarter lines, pushes) and its Pinnacle stand-in; the sharpening walk-forward (a later result
never changes an earlier forecast) and neutral before 1,000 fixtures; the pass rule and its fallback; the research
view never reaches the sharpening; the live master and the cagey tier's outputs untouched.
"""
from __future__ import annotations

import json
import math
from pathlib import Path
import unittest

import numpy as np
import pandas as pd

import cagey_sharpen as cs
import master_reconciliation as mr
import narrow_margin as nm

REPO = Path(__file__).resolve().parents[1]
CONFIG = mr.load_config()
TOL = 1e-9
HARNESS = json.loads((REPO / 'evaluation_harness_config.json').read_text(encoding='utf-8'))


def binary(p):
    return np.array([p, 0., 0., 0., 1 - p])


def row(match, no_loss, profit, odds, nominated=True, executable=True, market=None, **extra):
    """A classified offer as select() reads it: step-1 group from the 0.75 boundary (as classify)."""
    group = 'included' if no_loss is not None and no_loss + TOL >= 0.75 else 'left_out'
    return {'_match': match, 'new_master_group': group, 'ranking_no_loss_probability': no_loss,
            'ranking_profit_probability': profit, 'offered_decimal_odds': odds, 'market': market or f'{match}-{odds}',
            'kickoff_utc': '2026-11-08', 'league': 'L', 'home_team': match, 'away_team': 'x',
            'left_out_reason': None if group == 'included' else 'in between (not safe)', 'new_master_labels': None,
            'risky_fill': False, 'new_master_nominated': nominated, 'new_master_executable': executable, **extra}


def select_172(rows, target, match_key='_match', prefix='new_master'):
    """PR #172's select, verbatim (master_reconciliation.select before the fill rule)."""
    group, rank, decision, reason = (f'{prefix}_{k}' for k in ('group', 'rank', 'decision', 'reason'))
    best = {}
    for row in rows:
        row[rank] = None
        if row.get(f'{prefix}_executable', True) is False or row[group] not in mr.RANKED:
            continue
        current = best.get(row[match_key])
        if current is None or mr._tie_key(row) < mr._tie_key(current):
            best[row[match_key]] = row
    chosen = {id(r) for r in best.values()}
    for position, row in enumerate(sorted(best.values(), key=mr._tie_key), 1):
        if position <= target:
            row.update({rank: position, decision: 'SHORTLISTED', reason: ''})
        else:
            row.update({decision: 'BEYOND_TARGET', reason: f'beyond the {target}-match target'})
    for row in rows:
        if id(row) in chosen:
            continue
        if row.get(f'{prefix}_executable', True) is False:
            row.update({decision: 'NOT_EXECUTABLE', reason: row.get(reason) or 'not executable'})
        elif row[group] in mr.RANKED:
            row.update({decision: 'NOT_SELECTED', reason: 'another offer chosen for this match'})
        else:
            row.update({decision: 'LEFT_OUT', reason: row.get('left_out_reason') or 'left out by rule'})
    return rows


def independent_fill(rows, target):
    """The written fill rule re-derived without the module: [(match, market, tier)] in list order."""
    def best(candidates, key):
        out = {}
        for r in candidates:
            if r['_match'] not in out or key(r) < key(out[r['_match']]):
                out[r['_match']] = r
        return sorted(out.values(), key=key)
    ok = [r for r in rows if r['new_master_executable']]
    k1 = lambda r: (-round(r['ranking_no_loss_probability'], 9), -r['offered_decimal_odds'], r['market'])
    k2 = lambda r: (-round(r['ranking_profit_probability'], 9), -r['offered_decimal_odds'], r['market'])
    step1 = best([r for r in ok if r['new_master_nominated'] and r['ranking_no_loss_probability'] is not None
                  and r['ranking_no_loss_probability'] >= 0.75 - TOL], k1)
    picks = [(r['_match'], r['market'], 'safe') for r in step1][:target]
    if len(picks) < target:
        done = {r['_match'] for r in step1}
        viewed = [r for r in ok if r['_match'] not in done and r['new_master_nominated']
                  and r['ranking_no_loss_probability'] is not None
                  and r['ranking_profit_probability'] is not None]
        step2 = best([r for r in viewed if r['ranking_no_loss_probability'] >= 0.5 - TOL], k2)
        picks += [(r['_match'], r['market'], 'fill') for r in step2][:target - len(picks)]
        if len(picks) < target:
            done |= {r['_match'] for r in step2}
            step3 = best([r for r in viewed if r['_match'] not in done], k2)
            picks += [(r['_match'], r['market'], 'risky fill') for r in step3][:target - len(picks)]
    return picks


def listed(rows):
    picks = sorted((r for r in rows if r['new_master_decision'] == 'SHORTLISTED'), key=lambda r: r['new_master_rank'])
    return [(r['_match'], r['market'], r['new_master_tier']) for r in picks]


class ConfigTest(unittest.TestCase):
    def test_the_rule_is_written_before_it_ran(self):
        fill = CONFIG['fill']
        self.assertEqual(fill['decided'], 'decided by Paul, 13 Nov 2026; pools (every step uses only the '
                                          'nominations) decided by Paul, 14 Nov 2026')
        self.assertEqual(CONFIG['version'], mr.VERSION)
        self.assertEqual(mr.VERSION, 'master-new-fill-rule-v4')
        self.assertIn('decided by Paul, 14 Nov 2026, before any live grading', fill['pools']['decided'])
        self.assertIn('No step uses an offer that neither list nominated', fill['pools']['all_steps'])
        self.assertIn('stays out', fill['pools']['no_market_view'])
        self.assertIn('shorter than 15', fill['pools']['short_list'])
        self.assertEqual(fill['step_2_min_no_loss'], 0.5)
        self.assertEqual(set(fill['tiers']), set(mr.TIERS))
        self.assertIn('never two picks per match', fill['rule'])
        self.assertEqual(CONFIG['target_fixtures'], 15)
        profit = CONFIG['chance_of_profit']
        self.assertEqual(set(profit['by_line_type']), {'home_win_away_win', 'double_chance', 'asian_half_lines',
                                                       'asian_whole_lines', 'asian_quarter_lines'})
        self.assertIn('A push returns exactly the stake (not a profit)', profit['rule'])
        sharp = CONFIG['cagey_sharpening']
        self.assertEqual(sharp['version'], cs.VERSION)
        self.assertEqual((sharp['min_fixtures'], sharp['slope_bounds'], sharp['half_life_days']),
                         (1000, [0.5, 2.5], 480.0))
        self.assertEqual(set(sharp['pass_rule']), {'development', 'validation', 'passes', 'if_passes', 'if_fails'})
        self.assertIn('decided by Paul, 13-14 Nov 2026', sharp['decided'])
        self.assertFalse(sharp['use_sharpened'])  # failed its pre-set rule; stays off (Paul, 14 Nov 2026)
        self.assertTrue(sharp['status'].startswith('failed'))
        self.assertIn("won't be retried without a new decision", sharp['decision_after_result'])
        # use_sharpened can only be true once the pass rule has passed
        self.assertEqual(sharp['use_sharpened'], sharp['status'].startswith('passed'))
        self.assertIn('nothing restarts', CONFIG['live_comparison']['restart'])
        self.assertIn('by tier', CONFIG['live_comparison']['by_tier'])

    def test_c5_settings_are_reused(self):
        import research_sharpen as rs
        self.assertEqual(tuple(CONFIG['cagey_sharpening']['slope_bounds']), rs.SLOPE_BOUNDS)
        self.assertEqual(CONFIG['cagey_sharpening']['min_fixtures'], rs.MIN_MATCHES)
        self.assertEqual(CONFIG['cagey_sharpening']['half_life_days'], HARNESS['production_v2']['half_life_days'])


class ChanceOfProfitTest(unittest.TestCase):
    MARGINS = np.arange(-6, 7)
    PROBS = np.exp(-0.5 * ((MARGINS - 0.4) / 1.5) ** 2)
    PROBS = PROBS / PROBS.sum()

    def settled(self, side, line):
        out = nm.price_distribution(self.MARGINS.astype(float), self.PROBS, side, line)
        return np.array([out['p_' + k] for k in mr.KINDS])

    def independent(self, side, line, odds=1.5):
        """P(return > stake) by settling every score at `odds`: a quarter line is half the stake on each of its
        neighbouring lines; each half wins (odds x half), pushes (half back) or loses (nothing)."""
        total = 0.
        for margin, p in zip(self.MARGINS, self.PROBS):
            m = margin if side == 'home' else -margin
            halves = (line - .25, line + .25) if abs(line * 4) % 2 == 1 else (line, line)
            paid = sum(.5 * (odds if m + h > 0 else 1 if m + h == 0 else 0) for h in halves)
            total += p * (paid > 1 + 1e-12)
        return total

    def test_per_line_type(self):
        for side in ('home', 'away'):
            for line in (-2.0, -1.0, 0.0, 1.0, -1.5, -0.5, 0.5, 1.5, -0.75, -0.25, 0.25, 0.75, 1.25):
                mass = self.settled(side, line)
                self.assertAlmostEqual(mr.profit_chance(mass), self.independent(side, line), places=12)
                self.assertAlmostEqual(cs.profit(mass), mr.profit_chance(mass))
                kind = cs.line_type(line)
                if kind == 'whole':  # a push returns the stake: not a profit
                    self.assertAlmostEqual(mr.profit_chance(mass), mr.no_loss(mass) - mass[2], places=12)
                    self.assertGreater(mass[2], 0)
                else:  # no push on half or quarter lines: profit = no loss
                    self.assertAlmostEqual(mass[2], 0.)
                    self.assertAlmostEqual(mr.profit_chance(mass), mr.no_loss(mass), places=12)
                if kind == 'quarter':
                    self.assertGreater(mass[1] + mass[3], 0)  # half wins / half losses exist
        # a quarter line's half win is a profit, its half loss is not
        self.assertAlmostEqual(mr.profit_chance(np.array([.3, .2, 0., .1, .4])), .5)

    def test_wins_and_double_chance_are_half_lines(self):
        self.assertEqual([cs.offer_line_type(m, None) for m in ('Home win', 'Away win', 'Double Chance 1X',
                                                                'Double Chance X2')], ['half'] * 4)
        self.assertEqual([cs.offer_line_type('Asian Handicap Home', x) for x in (0.25, -0.75, 1.0, 0.0, -1.5, 'x')],
                         ['quarter', 'quarter', 'whole', 'whole', 'half', None])

    def test_classify_ranks_by_the_cagey_chance_of_profit(self):
        cagey = np.array([.40, .10, .25, .05, .20])
        out = mr.classify(None, cagey, 1.6, 0., european=False, config=CONFIG, use_sharpened=False)
        self.assertAlmostEqual(out['ranking_profit_probability'], .50)
        self.assertAlmostEqual(out['cagey_profit_probability'], .50)
        self.assertAlmostEqual(out['ranking_no_loss_probability'], .75)
        self.assertEqual(out['probability_source'], 'cagey')

    def test_pinnacle_stands_in_when_the_cagey_score_is_missing(self):
        base = {'pinnacle_no_loss_probability': 0.70, 'uncorrected_p_win': 0.45, 'uncorrected_p_half_win': 0.,
                'uncorrected_p_push': 0.25, 'uncorrected_p_half_loss': 0., 'uncorrected_p_loss': 0.30}
        self.assertAlmostEqual(mr.pinnacle_profit(base, 'whole'), 0.45)
        bare = {'pinnacle_no_loss_probability': 0.70}
        self.assertEqual((mr.pinnacle_profit(bare, 'quarter'), mr.pinnacle_profit(bare, 'half'),
                          mr.pinnacle_profit(bare, 'whole')), (0.70, 0.70, None))
        out = mr.classify(binary(.6), None, 1.5, 0., 0.70, 1.43, european=False, config=CONFIG, pinnacle_profit=0.45,
                          cagey_sharpened=(.9, .9), use_sharpened=True)
        self.assertEqual((out['probability_source'], out['ranking_no_loss_probability'],
                          out['ranking_profit_probability'], out['one_view_missing']),
                         ('pinnacle stand-in', 0.70, 0.45, True))  # never sharpened


class FillOrderTest(unittest.TestCase):
    def scenario(self):
        return [
            # step 1: safe nominated offers (ranked by no-loss; one per match)
            row('S1', .80, .80, 1.25), row('S1', .78, .78, 1.30), row('S2', .90, .62, 1.17), row('S3', .76, .76, 1.40),
            # step 2: not risky (>= 0.50), by chance of profit
            row('F2', .70, .70, 1.45), row('F2', .66, .40, 1.50),
            row('F3', .60, .35, 1.60), row('F3', .48, .48, 1.95),  # the not-risky whole line beats a risky one
            row('F4', .55, .55, 1.70), row('F5', .55, .55, 1.75),  # tie -> higher odds
            row('F5', .99, .99, 1.80, nominated=False),  # not nominated: never used, even for a match on the list
            # step 3: only risky offers
            row('R1', .45, .45, 1.90), row('R2', .40, .30, 1.99), row('R2', .38, .38, 1.98),
            # never picked: not nominated (in any step, however safe), no market view, not executable
            row('U1', .82, .82, 1.21, nominated=False), row('U2', .60, .60, 1.50, nominated=False),
            row('U3', .45, .45, 1.90, nominated=False),
            row('N1', None, None, 1.50), row('X1', .95, .95, 1.10, executable=False)]

    def test_the_fill_order_exactly_as_written(self):
        rows = self.scenario()
        mr.select(rows, 15)
        self.assertEqual(listed(rows), [
            ('S2', 'S2-1.17', 'safe'), ('S1', 'S1-1.25', 'safe'), ('S3', 'S3-1.4', 'safe'),
            ('F2', 'F2-1.45', 'fill'), ('F5', 'F5-1.75', 'fill'), ('F4', 'F4-1.7', 'fill'),
            ('F3', 'F3-1.6', 'fill'), ('R1', 'R1-1.9', 'risky fill'), ('R2', 'R2-1.98', 'risky fill')])
        self.assertEqual(listed(rows), independent_fill(self.scenario(), 15))
        by_market = {r['market']: r for r in rows}
        self.assertEqual([by_market[m]['new_master_labels'] for m in ('R1-1.9', 'R2-1.98')], ['risky fill'] * 2)
        self.assertTrue(by_market['R1-1.9']['risky_fill'])
        self.assertFalse(any(r['risky_fill'] for r in rows if r['new_master_tier'] in ('safe', 'fill')))
        self.assertEqual(by_market['X1-1.1']['new_master_decision'], 'NOT_EXECUTABLE')
        self.assertIsNone(by_market['N1-1.5']['new_master_rank'])
        for market in ('U1-1.21', 'U2-1.5', 'U3-1.9', 'F5-1.8'):  # rule v4: no step uses a non-nominated offer
            self.assertEqual((by_market[market]['new_master_decision'], by_market[market]['new_master_reason'],
                              by_market[market]['new_master_step'], by_market[market]['new_master_rank']),
                             ('NOT_SELECTED', 'not nominated by either list', None, None))
        ranked = [r for r in rows if r['new_master_decision'] == 'SHORTLISTED']
        self.assertEqual(len({r['_match'] for r in ranked}), len(ranked))  # never two picks per match

    def test_a_later_step_runs_only_if_the_list_is_still_short(self):
        rows = self.scenario()
        mr.select(rows, 5)
        self.assertEqual([t for _, _, t in listed(rows)], ['safe'] * 3 + ['fill'] * 2)
        self.assertFalse(any(r['risky_fill'] for r in rows))
        beyond = {r['_match']: r['new_master_step'] for r in rows if r['new_master_decision'] == 'BEYOND_TARGET'}
        self.assertEqual(beyond, {'F4': 2, 'F3': 2, 'R1': 3, 'R2': 3})
        rows = self.scenario()
        mr.select(rows, 2)
        self.assertEqual(listed(rows), [('S2', 'S2-1.17', 'safe'), ('S1', 'S1-1.25', 'safe')])
        self.assertEqual({r['_match'] for r in rows if r['new_master_decision'] == 'BEYOND_TARGET'},
                         {'S3', 'F2', 'F3', 'F4', 'F5', 'R1', 'R2'})

    def test_stop_when_no_match_remains(self):
        rows = self.scenario()
        mr.select(rows, 40)
        self.assertEqual(len(listed(rows)), 9)  # every nominated match with a market view, once

    def test_the_list_is_shorter_when_the_nominations_cover_fewer_matches(self):
        # 6 nominated matches and 30 matches nobody nominated (all safe): the list stops at 6
        rows = [row(f'N{i}', .6, .6, 1.5) for i in range(6)] + [row(f'U{i}', .9, .9, 1.2, nominated=False)
                                                                for i in range(30)]
        mr.select(rows, 15)
        self.assertEqual(sorted(m for m, _, _ in listed(rows)), [f'N{i}' for i in range(6)])
        self.assertEqual({t for _, _, t in listed(rows)}, {'fill'})

    def test_without_fill_it_is_172s_selection_verbatim(self):
        rng = np.random.default_rng(11)
        for _ in range(20):
            rows = [row(f'M{int(rng.integers(30)):02d}', float(rng.uniform(.4, .95)), float(rng.uniform(.3, .9)),
                        float(np.round(rng.uniform(1.16, 2.0), 2)), executable=bool(rng.random() > .1))
                    for _ in range(60)]
            ours = mr.select([dict(r) for r in rows], 15, fill=False)
            theirs = select_172([dict(r) for r in rows], 15)
            for a, b in zip(ours, theirs):
                self.assertEqual({k: a[k] for k in ('new_master_rank', 'new_master_decision', 'new_master_reason')},
                                 {k: b[k] for k in ('new_master_rank', 'new_master_decision', 'new_master_reason')})

    def test_against_an_independent_derivation(self):
        rng = np.random.default_rng(3)
        for trial in range(60):
            rows = []
            for _ in range(int(rng.integers(5, 80))):
                nl = float(rng.uniform(.3, .95))
                pr = nl if rng.random() < .6 else float(nl - rng.uniform(0, .3))
                rows.append(row(f'M{int(rng.integers(40)):02d}', nl, pr, float(np.round(rng.uniform(1.16, 2.0), 2)),
                                nominated=bool(rng.random() < .3), executable=bool(rng.random() > .05),
                                market=f'k{len(rows)}'))
            target = int(rng.integers(1, 20))
            expected = independent_fill([dict(r) for r in rows], target)
            self.assertEqual(listed(mr.select([dict(r) for r in rows], target)), expected, trial)

    def test_labels_flags_and_research_never_change_the_order(self):
        base = self.scenario()
        mr.select(base, 15)
        expected = listed(base)
        flip = np.random.default_rng(1)
        rows = [{**r, 'both_agree': bool(flip.integers(2)), 'inspection_flag': bool(flip.integers(2)),
                 'research_no_loss_probability': float(flip.random()), 'gap_points': float(flip.normal(0, 10))}
                for r in self.scenario()]
        mr.select(rows, 15)
        self.assertEqual(listed(rows), expected)


class SharpenTest(unittest.TestCase):
    SCFG = {**CONFIG['cagey_sharpening']}

    def events(self, n_fixtures, start='2023-01-01', slope=1.4, seed=0):
        """Too-flat synthetic forecasts: outcomes drawn from sigmoid(slope * logit(p))."""
        rng = np.random.default_rng(seed)
        rows = []
        for i in range(n_fixtures):
            date = pd.Timestamp(start) + pd.Timedelta(days=i // 10)
            for quantity in cs.QUANTITIES:
                for kind in cs.LINE_TYPES:
                    p = float(rng.uniform(.45, .9))
                    rows.append({'date': date, 'fixture_key': f'f{i}', 'quantity': quantity, 'line_type': kind,
                                 'p': p, 'y': int(rng.random() < cs.apply(p, slope))})
        return pd.DataFrame(rows)

    def test_neutral_before_1000_fixtures(self):
        for n, status in ((999, 'warm_up'), (1000, 'fitted')):
            ev = self.events(n)
            part = ev.loc[(ev.quantity == 'no_loss') & (ev.line_type == 'half')]
            fit = cs.fit(part.p, part.y, (pd.Timestamp('2030-01-01') - part.date).dt.days, part.fixture_key, 480.,
                         1000)
            self.assertEqual((fit['status'], fit['fixtures']), (status, n))
            if status == 'warm_up':
                self.assertEqual(fit['slope'], 1.)
            else:
                self.assertGreater(fit['slope'], 1.1)  # recovers the sharpening

    def test_neutral_is_the_identity_and_whole_line_profit_is_capped(self):
        self.assertEqual(cs.apply(0.6123, 1.), 0.6123)
        self.assertGreater(cs.apply(0.7, 1.3), 0.7)
        self.assertLess(cs.apply(0.3, 1.3), 0.3)
        neutral = {k: 1. for k in cs.KEYS}
        self.assertEqual(cs.sharpen(.7, .5, 'whole', neutral), (.7, .5))
        skew = {**neutral, 'no_loss:whole': 0.6, 'profit:whole': 2.5}
        nl, pr = cs.sharpen(.62, .60, 'whole', skew)
        self.assertLessEqual(pr, nl)

    def test_a_later_result_never_changes_an_earlier_forecast(self):
        ev = self.events(3000)
        origins = pd.date_range('2023-02-01', ev.date.max(), freq='14D')
        base = cs.walk_forward(ev, origins, self.SCFG)
        cut = origins[8]
        flipped = ev.copy()
        flipped.loc[flipped.date >= cut, 'y'] = 1 - flipped.loc[flipped.date >= cut, 'y']
        changed = cs.walk_forward(flipped, origins, self.SCFG)
        for origin in origins:
            key = origin.date().isoformat()
            if origin <= cut:
                self.assertEqual(base[key], changed[key], key)
        self.assertNotEqual(base[origins[-1].date().isoformat()], changed[origins[-1].date().isoformat()])
        neutral = [o for o in base if base[o]['no_loss:half']['status'] == 'warm_up']
        self.assertTrue(neutral and all(base[o]['no_loss:half']['slope'] == 1. for o in neutral))

    def test_a_fit_never_reads_a_match_on_or_after_its_origin(self):
        with self.assertRaises(ValueError):
            cs.fit([.6, .7], [1, 0], [3., 0.], ['a', 'b'], 480., 1)

    def test_fold_for(self):
        origins = ['2023-01-02', '2023-01-16', '2023-01-30']
        self.assertEqual([cs.fold_for(d, origins) for d in ('2023-01-01', '2023-01-02', '2023-01-29', '2024-01-01')],
                         [None, '2023-01-02', '2023-01-16', '2023-01-30'])


class HarnessSharpenTest(unittest.TestCase):
    """master_sharpen on synthetic fixtures: cagey-events-v1 bettable lines, folds from the harness windows."""

    @staticmethod
    def fixtures(n=600, seed=4):
        rng = np.random.default_rng(seed)
        out = []
        for i in range(n):
            date = pd.Timestamp('2022-08-01') + pd.Timedelta(days=int(i // 6))
            shift = float(rng.normal(0.3, 0.8))

            def grid(s):
                margins = list(range(-6, 7))
                probs = np.exp(-0.5 * ((np.array(margins) - s) / 1.7) ** 2)
                return [margins, (probs / probs.sum()).tolist()]
            line = float(np.round(-shift * 2) / 4)
            truth = grid(shift * 1.3)  # results a little more extreme than D forecasts (D too flat)
            margin = int(rng.choice(truth[0], p=truth[1]))
            out.append({'phase': 'development', 'week': f'{date.isocalendar().year}-W{date.isocalendar().week:02d}',
                        'league': 'EPL', 'fixture_key': f'EPL|{date.date()}|H{i}|A{i}', 'market_book': 'pinnacle',
                        'date': date.date().isoformat(), 'home_team': f'H{i}', 'away_team': f'A{i}',
                        'margin': margin, 'hda': [2.0, 3.5, 3.8], 'ah': [line, 1.93, 1.95],
                        'C': grid(shift + 1), 'D': grid(shift), 'M': grid(shift * 0.95), 'C6': None})
        return out

    def run_sharpen(self, fixtures, minimum=150):
        import evaluation_harness as eh
        rcfg = json.loads(json.dumps(CONFIG))
        rcfg['cagey_sharpening']['min_fixtures'] = minimum
        cfg = {**HARNESS, 'end_exclusive': '2023-02-01'}
        return eh.master_sharpen(fixtures, cfg, rcfg)

    def test_events_and_slopes_are_walk_forward_and_never_read_research(self):
        base = self.fixtures()
        events, fits = self.run_sharpen(base)
        self.assertTrue(set(events.line_type) <= set(cs.LINE_TYPES) and len(events))
        self.assertEqual(set(events.quantity), set(cs.QUANTITIES))
        fixed = [f['sharpen_slopes'] for f in base]
        self.assertTrue(any(s['no_loss:half'] != 1. for s in fixed if s))  # fits move once past the minimum
        self.assertTrue(all(s['no_loss:half'] == 1. for s, f in zip(fixed, base) if f['date'] < '2022-08-15'))
        # research changed or gone: identical events and slopes
        no_research = [{k: v for k, v in f.items() if k not in ('C', 'C6')} for f in self.fixtures()]
        events2, _ = self.run_sharpen(no_research)
        pd.testing.assert_frame_equal(events, events2)
        self.assertEqual(fixed, [f['sharpen_slopes'] for f in no_research])
        # results changed from a date on never move the slopes of a fixture in an earlier or the same fold
        cut = '2022-10-10'  # a fold origin: fixtures from then on get new results
        later = self.fixtures()
        for f in later:
            if f['date'] >= cut:
                f['margin'] = -f['margin'] + 2
        self.run_sharpen(later)
        for a, b in zip(base, later):
            if a['sharpen_fold'] is not None and a['sharpen_fold'] <= cut:
                self.assertEqual(a['sharpen_slopes'], b['sharpen_slopes'], a['fixture_key'])
        self.assertNotEqual(fixed[-1], later[-1]['sharpen_slopes'])

    def test_sharpened_probabilities_follow_their_fold(self):
        events, fits = self.run_sharpen(self.fixtures())
        sample = events.iloc[::97]
        for _, e in sample.iterrows():
            slope = fits[e.fold][f'{e.quantity}:{e.line_type}']['slope'] if e.fold else 1.
            expected = cs.apply(e.p, slope)
            if e.quantity == 'profit' and e.line_type == 'whole':
                self.assertLessEqual(e.p_sharpened, expected + 1e-12)
            else:
                self.assertAlmostEqual(e.p_sharpened, expected, places=12)


class PassRuleTest(unittest.TestCase):
    @staticmethod
    def entry(current, sharp, interval):
        return {'slope_current': current, 'slope_sharpened': sharp,
                'log_loss_current_minus_sharpened': {'interval_95': interval}}

    def check(self, **override):
        good = {q: self.entry(1.10, 1.02, [-0.0001, 0.0003]) for q in cs.QUANTITIES}
        check = {'development': dict(good), 'validation': dict(good), 'retrospective': {
            q: self.entry(1.0, 1.3, [-0.01, -0.005]) for q in cs.QUANTITIES}}
        for key, value in override.items():
            period, quantity = key.split('__')
            check[period] = {**check[period], quantity: value}
        return check

    def test_passes_only_when_development_and_validation_hold(self):
        self.assertTrue(cs.verdict(self.check())['passes'])  # the retrospective never decides
        self.assertEqual(cs.verdict(self.check())['uses'], 'sharpened cagey probabilities')
        fails = [
            {'development__no_loss': self.entry(1.10, 1.02, [-0.003, -0.0001])},  # log loss clearly worse
            {'development__profit': self.entry(1.10, 0.85, [0.0, 0.001])},       # slope further from 1
            {'validation__no_loss': self.entry(0.97, 0.90, [-0.001, 0.001])},     # validation, other direction
            {'validation__profit': self.entry(1.05, 1.05, [0.0, 0.001])},         # not strictly closer
            {'development__profit': self.entry(1.10, float('nan'), [0.0, 0.001])}]
        for override in fails:
            out = cs.verdict(self.check(**override))
            self.assertFalse(out['passes'], override)
            self.assertEqual(out['uses'], 'current cagey probabilities')
        self.assertFalse(cs.verdict({'development': self.check()['development']})['passes'])  # no validation

    def test_the_fallback_keeps_the_current_cagey_probabilities(self):
        cagey = np.array([.70, 0., 0., 0., .30])
        sharp = (.78, .78)
        current = mr.classify(binary(.69), cagey, 1.30, 0., european=False, config=CONFIG, cagey_sharpened=sharp,
                              use_sharpened=False)
        used = mr.classify(binary(.69), cagey, 1.30, 0., european=False, config=CONFIG, cagey_sharpened=sharp,
                           use_sharpened=True)
        missing = mr.classify(binary(.69), cagey, 1.30, 0., european=False, config=CONFIG, use_sharpened=True)
        self.assertEqual((current['ranking_no_loss_probability'], current['new_master_group'],
                          current['probability_source']), (.70, 'left_out', 'cagey'))
        self.assertEqual((used['ranking_no_loss_probability'], used['new_master_group'], used['probability_source']),
                         (.78, 'included', 'cagey sharpened'))
        self.assertEqual((missing['ranking_no_loss_probability'], missing['probability_source']), (.70, 'cagey'))
        for out in (current, used):  # labels and flags read the current cagey probabilities either way
            self.assertAlmostEqual(out['cagey_no_loss_probability'], .70)
            self.assertAlmostEqual(out['gap_points'], -1.0)
            self.assertEqual(out['cagey_sharpened_no_loss_probability'], .78)
        default = mr.classify(binary(.69), cagey, 1.30, 0., european=False, config=CONFIG, cagey_sharpened=sharp)
        self.assertEqual(default['probability_source'],
                         'cagey sharpened' if CONFIG['cagey_sharpening']['use_sharpened'] else 'cagey')

    def test_the_backtest_lists_the_chosen_variant(self):
        import evaluation_harness as eh
        fixtures = HarnessSharpenTest.fixtures(n=120)
        for f in fixtures:
            f['C6'] = f['C']
            f['sharpen_slopes'] = {k: 1.8 if k.endswith(':half') else 0.6 for k in cs.KEYS}
        for final in ('fill_current', 'fill_sharpened'):
            frame, _ = eh.master_frame(fixtures, 'C', final)
            for field in eh.MASTER_SELECTION_FIELDS:
                a, b = frame[f'new_master_{field}'], frame[f'{final}_{field}']
                self.assertTrue(((a == b) | (a.isna() & b.isna())).all(), (final, field))
        self.assertFalse(frame.fill_current_decision.equals(frame.fill_sharpened_decision))
        self.assertTrue((frame.loc[frame.safe_only_decision.eq('SHORTLISTED'), 'fill_current_decision']
                         .eq('SHORTLISTED')).all())  # step 1 is #172's list


class LiveFillTest(unittest.TestCase):
    """The live shadow on a real frozen forecast, copied into a run of several matches."""

    @classmethod
    def setUpClass(cls):
        from tests.test_master_reconciliation import production_run
        _, decisions, _ = production_run()
        copies = []
        for i in range(20):
            copy = decisions.copy()
            copy['home_team'] = copy['home_team'] + f' {i}'
            copy['away_team'] = copy['away_team'] + f' {i}'
            if i >= 4:  # matches whose only nomination is the value list's Home win (no-loss 0.52): fills
                home = copy.market_to_bet.eq('Home win')
                copy['decision'] = np.where(home, 'SHORTLISTED', 'REJECTED')
                copy['cagey_tier_decision'] = 'NOT_SELECTED'
            if i >= 18:  # matches neither list nominated: never listed (rule v4)
                copy['decision'] = 'REJECTED'
            copies.append(copy)
        cls.decisions = pd.concat(copies, ignore_index=True)
        cls.before = cls.decisions.to_csv(index=False)
        cls.frame = mr.reconcile(cls.decisions)

    def test_the_target_is_filled_one_pick_per_match(self):
        ranked = self.frame.loc[self.frame.new_master_decision.eq('SHORTLISTED')]
        self.assertEqual(len(ranked), 15)
        self.assertEqual(ranked[['home_team', 'away_team']].drop_duplicates().shape[0], 15)
        self.assertEqual(ranked.new_master_tier.value_counts().to_dict().get('safe'), 4)
        self.assertTrue(ranked.bookmaker.eq('Pinnacle').all())
        self.assertTrue(ranked.offered_decimal_odds.between(1.15 + 1e-9, 2.0).all())
        tiers = list(ranked.sort_values('new_master_rank').new_master_tier)
        self.assertEqual(tiers, sorted(tiers, key=mr.TIERS.index))  # safe, then fill, then risky fill
        fills = ranked.loc[ranked.new_master_tier.eq('fill')]
        self.assertTrue((fills.ranking_no_loss_probability >= 0.5 - 1e-9).all())
        self.assertTrue(fills.ranking_profit_probability.is_monotonic_decreasing)
        np.testing.assert_allclose(fills.ranking_profit_probability, fills.cagey_profit_probability, atol=1e-12)

    def test_the_file_lists_only_nominated_offers(self):
        self.assertEqual(len(self.frame), int((self.decisions.decision.eq('SHORTLISTED')
                                               | self.decisions.cagey_tier_decision.eq('SHORTLISTED')).sum()))
        self.assertTrue((self.frame.in_value_shortlist | self.frame.in_cagey_tier).all())
        self.assertFalse(self.frame.home_team.str.endswith((' 18', ' 19')).any())
        summary = mr.summary(self.frame)
        self.assertEqual((summary['ranked_fixtures'], summary['shortfall'], summary['short_reason']), (15, 0, None))
        self.assertEqual((summary['nominated_fixtures'], summary['fixtures_with_market_view'],
                          summary['fixtures_without_market_view']), (18, 18, 0))
        self.assertEqual(summary['picks_by_tier'], {'safe': 4, 'fill': 11, 'risky fill': 0})
        self.assertEqual(sum(summary['picks_by_tier'].values()), 15)
        self.assertIn('current cagey probabilities', summary['probabilities'])

    def test_a_short_list_is_recorded(self):
        keep = self.decisions.home_team.str.extract(r' (\d+)$')[0].astype(int) < 6
        frame = mr.reconcile(self.decisions.loc[keep])
        summary = mr.summary(frame)
        self.assertEqual((summary['ranked_fixtures'], summary['shortfall'], summary['nominated_fixtures']), (6, 9, 6))
        self.assertEqual(summary['short_reason'], 'nominations cover fewer than 15 matches')

    def test_a_match_without_a_market_view_stays_out(self):
        blind = self.decisions.copy()
        gone = blind.home_team.str.endswith(' 5')
        for column in [c for c in blind if c.startswith(('cagey_p_', 'uncorrected_p_'))] + [
                'pinnacle_no_loss_probability']:
            blind.loc[gone, column] = np.nan
        frame = mr.reconcile(blind)
        summary = mr.summary(frame)
        ranked = frame.loc[frame.new_master_decision.eq('SHORTLISTED')]
        self.assertFalse(ranked.home_team.str.endswith(' 5').any())
        self.assertEqual((summary['ranked_fixtures'], summary['fixtures_without_market_view']), (15, 1))

    def test_decision_rows_and_the_cagey_tier_are_untouched(self):
        self.assertEqual(self.decisions.to_csv(index=False), self.before)

    def test_research_never_changes_inclusion_or_order(self):
        changed = self.decisions.copy()
        changed[[f'research_p_{k}' for k in mr.KINDS]] = [0.2, 0., 0., 0., 0.8]
        ranks = lambda f: f[['home_team', 'market', 'new_master_rank', 'new_master_tier']].to_csv(index=False)
        self.assertEqual(ranks(mr.reconcile(changed)), ranks(self.frame))


if __name__ == '__main__':
    unittest.main()
