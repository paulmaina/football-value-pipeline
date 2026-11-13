"""The new master, in shadow (master_reconciliation.py, revised master rule, rule master-new-evidence-rule-v2).

Every rule exactly as written: inclusion only when the cagey tier rates the bet safe (the 0.75 boundary), no veto,
"research too optimistic" at g >= +4, ranking by the cagey no-loss chance only, "both agree" as a label, the
inspection flag at g <= -8 with cagey >= 0.85 (it never removes or reorders a bet), the missing-evidence labels,
European rows; both views on every offer either list nominates; the live master byte-identical; live grading beside
the live master with the comparison rule; and the offline backtest (with PR #171's rule frozen beside it)
walk-forward and locked.
"""
from __future__ import annotations

import io
import itertools
import json
from pathlib import Path
import tempfile
import unittest
from unittest import mock

import numpy as np
import pandas as pd

import master_reconciliation as mr
import master_rule_v1
import master_shortlist
import narrow_margin as nm
import price_edge_cagey_shortlist as v28

REPO = Path(__file__).resolve().parents[1]
FROZEN = json.loads((Path(__file__).with_name('fixtures') / 'frozen_forecast_row.json').read_text(encoding='utf-8'))
POLICY = json.loads((REPO / 'shortlist_quote_policy.json').read_text(encoding='utf-8'))
CONFIG = mr.load_config()
MARGIN = 0.026955172735899154
TOL = 1e-9


def production_run(row=None):
    """The production rules on a real frozen forecast (Brighton v Brentford, 8 Nov 2026)."""
    predictions = pd.DataFrame([row or FROZEN['row']])
    _, decisions, summary = v28.build_shortlist(predictions, FROZEN['snapshot_generated_utc'], execution_policy=POLICY,
                                                settings=v28.load_settings(), model=nm.production_model())
    summary['quote_execution_policy'] = POLICY
    return predictions, decisions, summary


def binary(p):
    return np.array([p, 0., 0., 0., 1 - p])


def classify(pr, pc, price, pin=None, pin_fair=None, european=False):
    """Shorthand: binary research/cagey views (None = that view missing)."""
    return mr.classify(None if pr is None else binary(pr), None if pc is None else binary(pc), price, 0., pin, pin_fair,
                       european=european, config=CONFIG)


def labels(out):
    return set(out['new_master_labels'].split('; ')) if out['new_master_labels'] else set()


def independent(pr, pc, research_ev, price, cagey_fair, pin, pin_fair, european):
    """The written rule, re-derived without the module's code: (group, gap check, labels)."""
    found = {'unvalidated view'} if european else set()
    if pr is None and pc is None:
        return 'left_out', 'no_view', found
    chance, fair_odds = (pc, cagey_fair) if pc is not None else (pin, pin_fair)
    safe = chance is not None and chance >= 0.75 - TOL
    fair = chance is not None and fair_odds is not None and price * (1 + MARGIN) >= fair_odds - TOL
    if pr is not None and pc is not None:
        g = 100 * (pr - pc)
        check = 'research_too_optimistic' if g >= 4 - TOL else 'research_more_pessimistic' if g <= -4 + TOL else 'agree'
        if check == 'research_too_optimistic':
            found.add('research too optimistic')
        if check == 'agree' and research_ev > 0 and (safe or fair) and not european:
            found.add('both agree')
        if g <= -8 + TOL and pc >= 0.85 - TOL:
            found.add('research strongly disagrees')
    elif pc is not None:
        check = 'no_research_check'
        found.add('no research check')
    else:
        check = 'one_view_missing'
        found.add('one view missing')
    return ('included' if safe else 'left_out'), check, found


def independent_v1(pr, pc, research_ev, price, cagey_fair, pin, pin_fair, european):
    """PR #171's rule as it was written (master-new-paul-rule-v1): (group, gap check)."""
    if pr is None and pc is None:
        return 'left_out', 'no_view'
    if pr is not None and pc is not None:
        g = 100 * (pr - pc)
        if g >= 4.0 - TOL:
            return 'left_out', 'ignored'
        if g <= -4.0 + TOL:
            return 'left_out', 'vetoed'
        check, chance, fair_odds, can_agree = 'kept', pc, cagey_fair, not european
    else:
        if pin is None:
            return 'left_out', 'one_view_missing_no_pinnacle'
        if abs(100 * ((pr if pr is not None else pc) - pin)) >= 4.0 - TOL:
            return 'left_out', 'one_view_missing_apart'
        check = 'one_view_missing_kept'
        chance, fair_odds = (pc, cagey_fair) if pc is not None else (pin, pin_fair)
        can_agree = False
    safe, risky = chance >= 0.75 - TOL, chance < 0.50
    fair = fair_odds is not None and price * (1 + MARGIN) >= fair_odds - TOL
    edge = pr is not None and research_ev > 0
    if risky:
        return 'left_out', check
    if edge and (safe or fair) and can_agree:
        return 'both_agree', check
    if safe:
        return 'market_safe', check
    return 'left_out', check


GRID = [None, *np.linspace(.42, .92, 11), .75, .85, .7499999, .8499999]


class DefinitionsTest(unittest.TestCase):
    def test_config_holds_the_written_rule(self):
        self.assertEqual(CONFIG['version'], 'master-new-evidence-rule-v2')
        self.assertIn('Decided by Paul, 13 Nov 2026, replacing the 4-point rule', CONFIG['decided'])
        self.assertIn('PR #171', CONFIG['decided'])
        self.assertEqual(CONFIG['file'], 'master_shortlist_new.csv')
        self.assertEqual(CONFIG['target_fixtures'], 15)
        self.assertTrue(CONFIG['one_pick_per_match'])
        self.assertEqual(CONFIG['execution']['bookmaker'], 'Pinnacle')
        self.assertEqual(CONFIG['inclusion']['min_cagey_no_loss'], 0.75)
        self.assertEqual(CONFIG['gap']['research_too_optimistic_min_points'], 4.0)
        self.assertNotIn('too_pessimistic_max_points', CONFIG['gap'])  # no veto
        self.assertEqual((CONFIG['inspection_flag']['max_gap_points'], CONFIG['inspection_flag']['min_cagey_no_loss']),
                         (-8.0, 0.85))
        self.assertEqual(CONFIG['inspection_flag']['label'], 'research strongly disagrees')
        view = CONFIG['market_view']
        self.assertEqual((view['safe']['min_no_loss'], view['risky']['max_no_loss_exclusive']), (0.75, 0.5))
        self.assertEqual(view['fair']['pinnacle_average_margin'], MARGIN)
        self.assertNotIn('groups', CONFIG)  # "both agree" is a label, not a ranking group
        live = CONFIG['live_comparison']
        self.assertEqual((live['min_graded_matches'], live['min_weeks'], live['bootstrap_samples'], live['seed']),
                         (150, 3, 2000, 136))
        self.assertIn('entirely above zero', live['rule'])
        self.assertIn('nothing restarts', live['restart'])
        self.assertEqual(CONFIG['previous_rule']['version'], master_rule_v1.VERSION)

    def test_no_loss_counts_wins_half_wins_and_pushes(self):
        mass = np.array([.40, .10, .20, .05, .25])
        self.assertAlmostEqual(mr.no_loss(mass), 0.70)
        out = mr.classify(mass, mass, 1.6, 0., european=False, config=CONFIG)
        self.assertAlmostEqual(out['research_no_loss_probability'], 0.70)
        self.assertAlmostEqual(out['cagey_no_loss_probability'], 0.70)
        self.assertAlmostEqual(out['gap_points'], 0.)

    def test_inclusion_is_cagey_safe_at_0_75_whatever_the_research_says(self):
        for pc, group, reason in ((0.75, 'included', None), (0.7500001, 'included', None),
                                  (0.7499999, 'left_out', 'in between (not safe)'),
                                  (0.50, 'left_out', 'in between (not safe)'), (0.4999999, 'left_out', 'risky')):
            for pr in (None, 0.30, pc - 0.0801, pc, pc + 0.02, min(pc + 0.10, 0.99)):
                out = classify(pr, pc, 1.30)
                self.assertEqual((out['new_master_group'], out['left_out_reason']), (group, reason), (pc, pr))

    def test_fair_is_a_label_only(self):
        fair_middle = classify(0.62, 0.60, 1.65)  # research edge, middle, fair (1.65 x 1.027 >= 1.667)
        self.assertEqual((fair_middle['market_price'], fair_middle['market_safety'], fair_middle['new_master_group']),
                         ('fair', 'middle', 'left_out'))
        below = classify(0.76, 0.78, 1.20)  # safe, below fair (1.20 x 1.027 < 1.282), no research edge
        self.assertEqual((below['market_price'], below['new_master_group']), ('below fair', 'included'))

    def test_no_veto(self):
        for pr in (0.7100001, 0.71, 0.70, 0.40, 0.01):  # research 4 to 79 points more pessimistic
            out = classify(pr, 0.80, 1.30)
            self.assertEqual((out['new_master_group'], out['left_out_reason']), ('included', None), pr)
        self.assertEqual(classify(0.70, 0.80, 1.30)['gap_check'], 'research_more_pessimistic')  # context only
        self.assertEqual(classify(0.7600001, 0.80, 1.30)['gap_check'], 'agree')
        self.assertEqual(classify(0.5225, 0.5625, 1.9)['gap_check'], 'research_more_pessimistic')  # exactly -4

    def test_research_too_optimistic_boundary_and_the_bet_kept_if_safe(self):
        for pr, optimistic in ((0.79, True), (0.7901, True), (0.95, True), (0.789999, False), (0.77, False)):
            out = classify(pr, 0.75, 1.40)
            self.assertEqual((out['research_too_optimistic'], 'research too optimistic' in labels(out)),
                             (optimistic, optimistic), pr)
            self.assertEqual(out['gap_check'], 'research_too_optimistic' if optimistic else 'agree')
            self.assertEqual(out['new_master_group'], 'included')  # safe: kept either way
            self.assertEqual('both agree' in labels(out), not optimistic)  # the research opinion is ignored
        self.assertTrue(classify(0.5625, 0.5225, 1.9)['research_too_optimistic'])  # exactly +4
        not_safe = classify(0.80, 0.70, 1.50)
        self.assertEqual((not_safe['research_too_optimistic'], not_safe['new_master_group']), (True, 'left_out'))

    def test_both_agree_is_a_label_not_a_group(self):
        safe = classify(0.80, 0.78, 1.30)  # research edge +4%, safe
        self.assertEqual((safe['new_master_group'], safe['both_agree'], safe['new_master_labels']),
                         ('included', True, 'both agree'))
        no_edge = classify(0.78, 0.78, 1.25)  # EV -2.5%
        self.assertEqual((no_edge['new_master_group'], no_edge['both_agree'], no_edge['new_master_labels']),
                         ('included', False, None))
        fair = classify(0.62, 0.60, 1.65)  # research edge, cagey fair but middle: label shown, bet left out
        self.assertEqual((fair['both_agree'], fair['new_master_group']), (True, 'left_out'))
        self.assertFalse(classify(0.62, 0.60, 1.62)['both_agree'])  # middle and below fair
        self.assertEqual(set(mr.GROUPS), {'included', 'left_out'})

    def test_inspection_flag_boundaries(self):
        cases = ((0.77, 0.85, True),          # g = -8.0 exactly, cagey 0.85 exactly
                 (0.7700001, 0.85, False),    # g just above -8
                 (0.76, 0.8499999, False),    # cagey just below 0.85
                 (0.60, 0.95, True), (0.84, 0.92, True), (0.8400001, 0.92, False), (0.50, 0.80, False))
        for pr, pc, flagged in cases:
            out = classify(pr, pc, 1.18)
            self.assertEqual(out['inspection_flag'], flagged, (pr, pc))
            self.assertEqual('research strongly disagrees' in labels(out), flagged, (pr, pc))
            self.assertEqual(out['new_master_group'], 'included')  # never removed
            self.assertAlmostEqual(out['gap_points'], 100 * (pr - pc))
            self.assertAlmostEqual(out['research_no_loss_probability'], pr)
            self.assertAlmostEqual(out['cagey_no_loss_probability'], pc)

    def test_missing_cagey_needs_pinnacle_safe_and_carries_no_research_labels(self):
        for pin, group in ((0.75, 'included'), (0.90, 'included'), (0.7499999, 'left_out'), (0.40, 'left_out')):
            out = classify(0.50, None, 1.30, pin=pin, pin_fair=1 / pin)  # research 25+ points below Pinnacle
            self.assertEqual((out['new_master_group'], out['market_basis'], out['missing_view']),
                             (group, 'pinnacle', 'cagey'), pin)
            self.assertEqual(labels(out), {'one view missing'})  # never flagged, never both agree
            self.assertEqual((out['one_view_missing'], out['inspection_flag'], out['both_agree']), (True, False, False))
            self.assertIsNone(out['gap_points'])
            self.assertAlmostEqual(out['ranking_no_loss_probability'], pin)
        rich = classify(0.99, None, 1.30, pin=0.80, pin_fair=1.25)  # research far above: no optimistic label either
        self.assertEqual((rich['new_master_group'], labels(rich)), ('included', {'one view missing'}))
        none = classify(0.80, None, 1.30)
        self.assertEqual((none['new_master_group'], none['left_out_reason']),
                         ('left_out', 'one view missing: no Pinnacle reference'))

    def test_missing_research_stays_in_if_safe_with_no_research_check(self):
        kept = classify(None, 0.80, 1.25, pin=0.60)  # Pinnacle far away: no check against it any more
        self.assertEqual((kept['new_master_group'], kept['missing_view'], labels(kept)),
                         ('included', 'research', {'no research check'}))
        self.assertEqual((kept['no_research_check'], kept['one_view_missing'], kept['gap_check']),
                         (True, False, 'no_research_check'))
        self.assertEqual(classify(None, 0.95, 1.18)['inspection_flag'], False)
        self.assertEqual(classify(None, 0.70, 1.40)['new_master_group'], 'left_out')
        both = classify(None, None, 1.4, pin=0.8)
        self.assertEqual((both['gap_check'], both['new_master_group'], both['missing_view']),
                         ('no_view', 'left_out', 'both'))

    def test_european_rows(self):
        safe = classify(0.80, 0.78, 1.30, european=True)  # would be both agree domestically
        self.assertEqual((safe['new_master_group'], labels(safe)), ('included', {'unvalidated view'}))
        self.assertEqual(classify(0.62, 0.70, 1.40, european=True)['new_master_group'], 'left_out')
        flagged = classify(0.70, 0.90, 1.18, european=True)  # otherwise the same rule: the flag applies
        self.assertEqual(labels(flagged), {'research strongly disagrees', 'unvalidated view'})
        optimistic = classify(0.90, 0.80, 1.30, european=True)
        self.assertEqual(labels(optimistic), {'research too optimistic', 'unvalidated view'})

    def test_the_rule_on_a_grid_against_an_independent_derivation(self):
        for pr, pc, price, european, pin in itertools.product(GRID, GRID, (1.16, 1.3, 1.55, 1.8, 2.0),
                                                              (False, True), (None, .6, .75, .79)):
            pin_fair = None if pin is None else 1 / pin
            out = classify(pr, pc, price, pin, pin_fair, european)
            ev = None if pr is None else pr * price - 1
            expected = independent(pr, pc, ev, price, None if pc is None else 1 / pc, pin, pin_fair, european)
            self.assertEqual((out['new_master_group'], out['gap_check'], labels(out)), expected,
                             (pr, pc, price, european, pin))
            for column, text in mr.LABELS:
                self.assertEqual(out[column], text in expected[2])

    def test_the_frozen_previous_rule_is_171s_rule_as_written(self):
        previous = master_rule_v1.config(CONFIG)
        self.assertEqual(previous['gap'], {'too_optimistic_min_points': 4.0, 'too_pessimistic_max_points': -4.0})
        for pr, pc, price, european, pin in itertools.product(GRID[:12], GRID[:12], (1.16, 1.55, 2.0), (False, True),
                                                              (None, .6, .79)):
            pin_fair = None if pin is None else 1 / pin
            out = master_rule_v1.classify(None if pr is None else binary(pr), None if pc is None else binary(pc),
                                          price, 0., pin, pin_fair, european=european, config=previous)
            ev = None if pr is None else pr * price - 1
            self.assertEqual((out['new_master_group'], out['gap_check']),
                             independent_v1(pr, pc, ev, price, None if pc is None else 1 / pc, pin, pin_fair, european))


class SelectTest(unittest.TestCase):
    @staticmethod
    def row(match, chance, odds, market='m', group='included', **extra):
        return {'_match': match, 'new_master_group': group, 'ranking_no_loss_probability': chance,
                'offered_decimal_odds': odds, 'market': market, 'kickoff_utc': '2026-11-08', 'league': 'L',
                'home_team': match, 'away_team': 'x', 'left_out_reason': None if group != 'left_out' else 'risky',
                'both_agree': False, 'inspection_flag': False, **extra}

    def test_ranked_by_no_loss_only_then_odds(self):
        rows = [self.row('A', .80, 1.30, 'a1', both_agree=True), self.row('A', .90, 1.20, 'a2'),
                self.row('B', .95, 1.17, 'b1', inspection_flag=True), self.row('B', .85, 1.25, 'b2', both_agree=True),
                self.row('C', .76, 1.40, 'c1'), self.row('C', .76 + 1e-13, 1.33, 'c2'),
                self.row('D', .99, 1.16, 'd1', group='left_out')]
        mr.select(rows, 15)
        picks = {r['market']: (r['new_master_rank'], r['new_master_decision']) for r in rows}
        self.assertEqual(picks['b1'], (1, 'SHORTLISTED'))  # highest no-loss, flagged or not
        self.assertEqual(picks['a2'], (2, 'SHORTLISTED'))  # beats its both-agree sibling on no-loss
        self.assertEqual(picks['c1'], (3, 'SHORTLISTED'))  # equal chance to 9 decimals -> higher odds
        self.assertEqual([picks[k][1] for k in ('a1', 'b2', 'c2', 'd1')],
                         ['NOT_SELECTED', 'NOT_SELECTED', 'NOT_SELECTED', 'LEFT_OUT'])

    def test_labels_and_the_flag_never_reorder(self):
        rng = np.random.default_rng(7)
        base = [self.row(f'M{i % 12:02d}', float(rng.uniform(.75, .97)), float(rng.uniform(1.16, 1.4)), f'k{i}')
                for i in range(40)]
        mr.select(base, 15)
        expected = [(r['new_master_rank'], r['new_master_decision']) for r in base]
        for seed in range(5):
            flip = np.random.default_rng(seed)
            rows = [{**r, 'both_agree': bool(flip.integers(2)), 'inspection_flag': bool(flip.integers(2)),
                     'research_too_optimistic': bool(flip.integers(2)), 'new_master_labels': str(flip.integers(9))}
                    for r in base]
            mr.select(rows, 15)
            self.assertEqual([(r['new_master_rank'], r['new_master_decision']) for r in rows], expected)

    def test_fifteen_match_target(self):
        rows = [self.row(f'M{i:02d}', .90 - i / 1000, 1.25) for i in range(18)]
        mr.select(rows, 15)
        self.assertEqual([r['new_master_rank'] for r in rows[:15]], list(range(1, 16)))
        self.assertEqual({r['new_master_decision'] for r in rows[15:]}, {'BEYOND_TARGET'})

    def test_non_executable_offers_are_never_picked(self):
        rows = [{**self.row('A', .9, 1.1), 'new_master_executable': False,
                 'new_master_reason': 'offered odds outside (1.15, 2.00]'}]
        mr.select(rows, 15)
        self.assertEqual((rows[0]['new_master_decision'], rows[0]['new_master_reason']),
                         ('NOT_EXECUTABLE', 'offered odds outside (1.15, 2.00]'))


class LiveShadowTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.predictions, cls.decisions, cls.summary = production_run()
        cls.frame = mr.reconcile(cls.decisions)

    def nominated(self):
        d = self.decisions
        return d.loc[d.decision.eq('SHORTLISTED') | d.cagey_tier_decision.eq('SHORTLISTED')]

    def row(self, frame, market='Asian Handicap Home +0.50'):
        return frame.loc[frame.market.eq(market)].iloc[0]

    def index(self, frame, market='Asian Handicap Home +0.50'):
        return frame.index[frame.cagey_tier_decision.eq('SHORTLISTED') & frame.market.eq(market)][0]

    def test_both_views_are_scored_on_every_offer_either_list_considers(self):
        self.assertEqual(len(self.frame), len(self.nominated()))
        self.assertTrue((self.frame.in_value_shortlist & ~self.frame.in_cagey_tier).any())
        self.assertTrue((~self.frame.in_value_shortlist & self.frame.in_cagey_tier).any())
        for column in ('research_no_loss_probability', 'cagey_no_loss_probability', 'gap_points',
                       'research_expected_return', 'pinnacle_no_loss_probability', 'gap_check', 'new_master_group'):
            self.assertTrue(self.frame[column].notna().all(), column)

    def test_the_views_are_the_lists_own_figures_on_that_exact_offer(self):
        nominated = self.nominated().reset_index(drop=True)
        key = ['market', 'handicap_side', 'handicap_line', 'offered_decimal_odds']
        merged = self.frame.merge(nominated, on=key, suffixes=('', '_decision'))
        self.assertEqual(len(merged), len(self.frame))
        research = merged[['research_p_' + k for k in ('win', 'half_win', 'push')]].sum(axis=1)
        np.testing.assert_allclose(merged.research_no_loss_probability, research, atol=1e-12)
        np.testing.assert_allclose(merged.cagey_no_loss_probability, merged.cagey_no_loss_probability_decision,
                                   atol=1e-12)  # Pinnacle's cost is 0, so P(no loss) is the tier's own figure
        np.testing.assert_allclose(merged.research_expected_return, merged.profit_expected_return, atol=1e-12)
        np.testing.assert_allclose(merged.pinnacle_no_loss_probability, merged.pinnacle_no_loss_probability_decision,
                                   atol=1e-12)
        np.testing.assert_allclose(merged.gap_points, 100 * (merged.research_no_loss_probability
                                                             - merged.cagey_no_loss_probability), atol=1e-9)

    def test_the_rule_on_real_rows(self):
        for row in self.frame.to_dict('records'):
            expected = independent(row['research_no_loss_probability'], row['cagey_no_loss_probability'],
                                   row['research_expected_return'], row['offered_decimal_odds'],
                                   row['cagey_fair_odds'], row['pinnacle_no_loss_probability'],
                                   row['pinnacle_fair_odds'], False)
            self.assertEqual((row['new_master_group'], row['gap_check'], labels(row)), expected)
        self.assertIn('research_too_optimistic', set(self.frame.gap_check))  # this forecast's Home win

    def test_one_pick_per_match_target_ranking_and_pinnacle_only(self):
        ranked = self.frame.loc[self.frame.new_master_decision.eq('SHORTLISTED')]
        self.assertEqual(len(ranked), 1)
        self.assertTrue(ranked.new_master_group.eq('included').all())
        self.assertTrue(ranked.bookmaker.eq('Pinnacle').all())
        self.assertEqual(ranked.iloc[0].market, 'Asian Handicap Home +0.25')  # equal no-loss chance, higher odds
        self.assertFalse(self.frame.loc[self.frame.new_master_group.eq('left_out'),
                                        'new_master_decision'].isin(['SHORTLISTED', 'BEYOND_TARGET']).any())

    def test_a_pessimistic_research_view_never_removes_a_cagey_pick(self):
        broken = self.decisions.copy()
        broken.loc[self.index(broken), [f'research_p_{k}' for k in mr.KINDS]] = [0.40, 0., 0., 0., 0.60]
        frame = mr.reconcile(broken)
        row = self.row(frame)
        self.assertEqual((row.gap_check, row.new_master_group, row.in_cagey_tier, row.inspection_flag),
                         ('research_more_pessimistic', 'included', True, False))  # cagey 0.764 < 0.85: no flag
        self.assertEqual(row.new_master_decision, self.row(self.frame).new_master_decision)

    def test_the_inspection_flag_on_a_real_row_keeps_its_place(self):
        """Cagey 0.90 and research 0.80 on the +0.50 offer: flagged, listed for inspection, same place."""
        def run(research):
            changed = self.decisions.copy()
            index = self.index(changed)
            changed.loc[index, [f'cagey_p_{k}' for k in mr.KINDS]] = [0.90, 0., 0., 0., 0.10]
            changed.loc[index, [f'research_p_{k}' for k in mr.KINDS]] = [research, 0., 0., 0., 1 - research]
            return mr.reconcile(changed)
        flagged, quiet = run(0.80), run(0.89)
        row = self.row(flagged)
        self.assertEqual((bool(row.inspection_flag), row.new_master_rank, row.new_master_decision),
                         (True, 1.0, 'SHORTLISTED'))
        self.assertIn('research strongly disagrees', row.new_master_labels)
        self.assertAlmostEqual(row.gap_points, -10.0)
        self.assertFalse(self.row(quiet).inspection_flag)
        ranks = lambda f: f[['market', 'new_master_rank', 'new_master_decision']].to_csv(index=False)
        self.assertEqual(ranks(flagged), ranks(quiet))
        section = mr.summary(flagged)['for_inspection']
        self.assertEqual(section['flagged_offers'], 1)
        self.assertEqual(len(section['picks']), 1)
        pick = section['picks'][0]
        self.assertEqual((pick['market_to_bet'], pick['new_master_rank']), (row.market_to_bet, 1.0))
        self.assertAlmostEqual(pick['research_no_loss_probability'], 0.80)
        self.assertAlmostEqual(pick['cagey_no_loss_probability'], 0.90)
        self.assertAlmostEqual(pick['gap_points'], -10.0)
        self.assertEqual(mr.summary(quiet)['for_inspection']['picks'], [])

    def test_missing_research_is_kept_with_no_research_check(self):
        broken = self.decisions.copy()
        broken.loc[self.index(broken), [f'research_p_{k}' for k in mr.KINDS]] = np.nan
        frame = mr.reconcile(broken)
        row = self.row(frame)
        self.assertEqual((row.gap_check, row.missing_view, row.new_master_group, row.new_master_labels),
                         ('no_research_check', 'research', 'included', 'no research check'))
        self.assertEqual(mr.summary(frame)['labels_offers']['no research check'], 1)

    def test_missing_cagey_falls_back_to_pinnacle(self):
        unsynced = self.decisions.copy()
        unsynced.loc[self.index(unsynced), 'cagey_input_timing_status'] = 'UNAVAILABLE_OR_UNSYNCHRONIZED'
        frame = mr.reconcile(unsynced)
        row = self.row(frame)
        self.assertEqual((row.missing_view, row.market_basis, row.new_master_labels, row.new_master_group),
                         ('cagey', 'pinnacle', 'one view missing', 'included'))  # Pinnacle 0.763 >= 0.75
        self.assertFalse(row.both_agree)
        self.assertEqual(mr.summary(frame)['labels_offers']['one view missing'], 1)

    def test_a_missing_espn_match_is_not_missing_evidence(self):
        flagged = self.decisions.copy()
        flagged['research_warnings'] = 'free-source fixture identity missing or ambiguous'
        frame = mr.reconcile(flagged)
        self.assertFalse(frame.one_view_missing.any() or frame.no_research_check.any())

    def test_european_rows_are_flagged_and_never_both_agree(self):
        europe = mr.reconcile(self.decisions.assign(league='UEFA Champions League'))
        self.assertTrue(europe.unvalidated_view.all())
        self.assertFalse(europe.both_agree.any())
        self.assertTrue(europe.new_master_labels.str.contains('unvalidated view').all())
        ranks = lambda f: f[['market', 'new_master_rank', 'new_master_decision']].to_csv(index=False)
        self.assertEqual(ranks(europe), ranks(self.frame))  # otherwise the same rule
        summary = mr.summary(europe)
        self.assertEqual((summary['european_offers'], summary['european_ranked']), (len(europe), 1))
        self.assertFalse(self.frame.unvalidated_view.any())

    def test_the_new_master_is_a_pure_function_of_the_run(self):
        again = mr.reconcile(self.decisions.copy())
        self.assertEqual(again.to_csv(index=False), self.frame.to_csv(index=False))
        shuffled = mr.reconcile(self.decisions.sample(frac=1, random_state=3))
        ranked = lambda f: f.loc[f.new_master_rank.notna()].to_csv(index=False)
        self.assertEqual(ranked(shuffled), ranked(self.frame))

    def test_rows_carry_what_grading_needs(self):
        self.assertTrue(self.frame.evaluated_at_utc.notna().all())
        self.assertTrue(self.frame.selection_policy_version.eq(v28.POLICY).all())
        self.assertTrue(self.frame.new_master_version.eq(mr.VERSION).all())
        self.assertNotIn('disagreement', self.frame.columns)
        for column in ('research_no_loss_probability', 'cagey_no_loss_probability', 'gap_points',
                       'new_master_labels', 'inspection_flag'):
            self.assertIn(column, self.frame.columns)


class LiveMasterUnchangedTest(unittest.TestCase):
    """master_shortlist.csv, its audit and the run summary are byte-identical with the new master on."""

    def run_refresh(self, shadow=True, out=None):
        predictions, decisions, summary = production_run()
        before = decisions.to_csv(index=False)
        out = out or Path(tempfile.mkdtemp())
        if shadow:
            master_shortlist.refresh(decisions, out, summary, predictions)
        else:
            with mock.patch.object(master_shortlist, 'shadow', lambda *a, **k: None):
                master_shortlist.refresh(decisions, out, summary, predictions)
        self.assertEqual(decisions.to_csv(index=False), before)  # decision rows never touched
        return out, summary

    def test_live_master_files_are_byte_identical(self):
        with_shadow, summary_on = self.run_refresh(True)
        without, summary_off = self.run_refresh(False)
        for name in (master_shortlist.FILE, 'master_shortlist_audit.csv'):
            self.assertEqual((with_shadow / name).read_bytes(), (without / name).read_bytes(), name)
        self.assertEqual(json.dumps(summary_on, sort_keys=True, default=str),
                         json.dumps(summary_off, sort_keys=True, default=str))
        self.assertTrue((with_shadow / 'master_shortlist_new.csv').exists())
        self.assertTrue((with_shadow / 'master_shortlist_new_summary.json').exists())
        self.assertFalse((without / 'master_shortlist_new.csv').exists())

    def test_one_shadow_list_only(self):
        out = Path(tempfile.mkdtemp())
        for name in mr.SUPERSEDED_FILES:
            (out / name).write_text('stale', encoding='utf-8')
        self.run_refresh(True, out)
        self.assertFalse(any((out / name).exists() for name in mr.SUPERSEDED_FILES))
        masters = sorted(p.name for p in out.glob('master_shortlist*.csv'))
        self.assertEqual(masters, ['master_shortlist.csv', 'master_shortlist_audit.csv', 'master_shortlist_new.csv'])

    def test_overlap_reads_the_live_list_without_changing_the_new_master(self):
        out, _ = self.run_refresh(True)
        new = pd.read_csv(out / CONFIG['file'])
        _, decisions, _ = production_run()
        alone = mr.reconcile(decisions)
        drop = ['in_live_master', 'live_master_rank', 'live_master_same_offer']
        pd.testing.assert_frame_equal(new.drop(columns=drop),
                                      pd.read_csv(io.StringIO(alone.to_csv(index=False))).drop(columns=drop))

    def test_a_shadow_failure_never_touches_the_live_run(self):
        predictions, decisions, summary = production_run()
        out = Path(tempfile.mkdtemp())
        with mock.patch.object(mr, 'write_shadow', side_effect=RuntimeError('boom')):
            with self.assertWarns(UserWarning):
                frame = master_shortlist.refresh(decisions, out, summary, predictions)
        self.assertGreater(len(frame), 0)
        self.assertFalse((out / CONFIG['file']).exists())
        clean, _ = self.run_refresh(False)
        self.assertEqual((out / master_shortlist.FILE).read_bytes(), (clean / master_shortlist.FILE).read_bytes())

    def test_other_policies_remove_any_seeded_shadow(self):
        out = Path(tempfile.mkdtemp())
        for name in (CONFIG['file'], CONFIG['summary_file'], *mr.SUPERSEDED_FILES):
            (out / name).write_text('stale', encoding='utf-8')
        master_shortlist.refresh(pd.DataFrame(), out, {'selection_policy_version': 'other'})
        self.assertEqual(list(out.iterdir()), [])


class LiveGradingTest(unittest.TestCase):
    """master_shortlist_new.csv is archived, graded and reported beside the live master, the same way."""

    KICK = pd.Timestamp('2026-11-07T15:00:00Z')

    def offer(self, home='Home FC', decision='SHORTLISTED', price=1.30, generated=None, **extra):
        generated = generated or (self.KICK - pd.Timedelta(hours=20)).isoformat()
        return {'new_master_rank': 1 if decision == 'SHORTLISTED' else None, 'new_master_group': 'included',
                'new_master_decision': decision, 'league': 'Premier League', 'home_team': home,
                'away_team': 'Away FC', 'kickoff_utc': self.KICK.isoformat(), 'market': 'Asian Handicap Away +1.00',
                'market_to_bet': 'Away +1.00', 'handicap_side': 'away', 'handicap_line': 1.0, 'bookmaker': 'Pinnacle',
                'offered_decimal_odds': price, 'per_stake_cost': 0., 'fair_odds': 1.33, 'reference_type': 'a',
                'evaluated_at_utc': generated, 'selection_policy_version': v28.POLICY,
                'new_master_version': mr.VERSION, 'gap_check': 'agree', 'new_master_labels': 'both agree',
                'both_agree': True, 'research_too_optimistic': False, 'inspection_flag': False,
                'one_view_missing': False, 'no_research_check': False, 'unvalidated_view': False, **extra}

    def test_capture_binds_to_its_generation_and_rule(self):
        import price_edge_tracking as tracking
        generated = (self.KICK - pd.Timedelta(hours=20)).isoformat()
        with tempfile.TemporaryDirectory() as tmp:
            raw = Path(tmp)
            self.assertIsNone(tracking.capture_new_master_file(raw, generated))
            pd.DataFrame([self.offer()]).to_csv(raw / CONFIG['file'], index=False)
            self.assertEqual(tracking.capture_new_master_file(raw, generated), raw / CONFIG['file'])
            self.assertIsNone(tracking.capture_new_master_file(raw, self.KICK.isoformat()))
            for old in ('master-reconciliation-shadow-v1', 'master-new-paul-rule-v1'):
                pd.DataFrame([self.offer(new_master_version=old)]).to_csv(raw / CONFIG['file'], index=False)
                self.assertIsNone(tracking.capture_new_master_file(raw, generated))

    def archive(self, root, versions):
        """versions: (sha, generated, captured, rows) per snapshot."""
        archive = []
        for sha, generated, captured, rows in versions:
            directory = root / 'performance' / 'snapshots' / sha[:16]
            directory.mkdir(parents=True)
            pd.DataFrame(rows).to_csv(directory / CONFIG['file'], index=False)
            archive.append(({'git_commit_sha': sha, 'captured_at_utc': captured.isoformat(),
                             'generated_at_utc': generated.isoformat(), 'selection_policy_version': v28.POLICY,
                             'sha256': {CONFIG['file']: '0' * 64}}, [], []))
        return archive

    def test_frozen_picks_are_the_newest_pre_kickoff_ranked_pick_per_fixture(self):
        import price_edge_tracking as tracking
        day = self.KICK.normalize()
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            archive = self.archive(root, [
                ('a' * 40, day - pd.Timedelta(hours=13), day - pd.Timedelta(hours=12),
                 [self.offer(price=1.31), self.offer(decision='LEFT_OUT', price=1.9, new_master_group='left_out',
                                                     inspection_flag=True, both_agree=False)]),
                ('b' * 40, day - pd.Timedelta(hours=15), day - pd.Timedelta(hours=11), [self.offer(price=1.20)]),
                # captured 10 minutes before kickoff: never graded (lead check)
                ('c' * 40, self.KICK - pd.Timedelta(minutes=15), self.KICK - pd.Timedelta(minutes=10),
                 [self.offer(price=1.50)])])
            rows = tracking.frozen_new_master_picks(root, archive)
            counts = tracking.new_master_offer_counts(root, archive)
        self.assertEqual([float(r['offered_decimal_odds']) for r in rows], [1.31])
        self.assertEqual((counts['fixtures'], counts['offers'], counts['included'], counts['both_agree'],
                          counts['inspection_flag']), (1, 2, 1, 1, 1))

    def test_picks_under_an_earlier_rule_never_count(self):
        """A rule change restarts the comparison: only picks made under the current version are graded."""
        import price_edge_tracking as tracking
        day = self.KICK.normalize()
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            archive = self.archive(root, [
                ('e' * 40, day - pd.Timedelta(hours=13), day - pd.Timedelta(hours=12),
                 [self.offer(price=1.31, new_master_version='master-new-paul-rule-v1')]),
                ('f' * 40, day - pd.Timedelta(hours=15), day - pd.Timedelta(hours=14),
                 [self.offer(home='Other FC', price=1.22)])])
            rows = tracking.frozen_new_master_picks(root, archive)
            counts = tracking.new_master_offer_counts(root, archive)
        self.assertEqual([(r['home_team'], float(r['offered_decimal_odds'])) for r in rows], [('Other FC', 1.22)])
        self.assertEqual((counts['fixtures'], counts['offers']), (1, 1))

    def frame(self, profits, start='2026-11-02', per_week=10):
        kicks = [pd.Timestamp(start, tz='UTC') + pd.Timedelta(days=7 * (i // per_week), hours=i % per_week)
                 for i in range(len(profits))]
        return pd.DataFrame({'kickoff_utc': [k.isoformat() for k in kicks], 'unit_profit': profits,
                             'offered_decimal_odds': 1.5})

    def test_the_comparison_rule_waits_for_150_matches_over_3_weeks(self):
        import price_edge_tracking as tracking
        rule = CONFIG['live_comparison']
        few = tracking.compare_masters(self.frame([0.5] * 149, per_week=50), self.frame([0.] * 200), rule)
        self.assertEqual((few['status'], few['verdict']), ('WAITING', 'not yet comparable'))
        short = tracking.compare_masters(self.frame([0.5] * 160, per_week=80), self.frame([0.] * 160, per_week=80),
                                         rule)
        self.assertEqual((short['new_master']['weeks'], short['status']), (2, 'WAITING'))
        ungraded = self.frame([0.5] * 150 + [np.nan] * 10, per_week=50)
        self.assertEqual(tracking.compare_masters(ungraded, self.frame([0.] * 150, per_week=50), rule)
                         ['new_master']['graded_matches'], 150)

    def test_better_only_if_the_interval_is_entirely_above_zero(self):
        import price_edge_tracking as tracking
        rule = CONFIG['live_comparison']
        rng = np.random.default_rng(5)
        live = self.frame(list(rng.choice([0.4, -1.], 200, p=[.7, .3])), per_week=40)
        better = self.frame(list(rng.choice([0.6, -1.], 200, p=[.8, .2])), per_week=40)
        out = tracking.compare_masters(better, live, rule, {'included': 3})
        self.assertEqual(out['status'], 'COMPARED')
        self.assertGreater(out['interval_95'][0], 0)
        self.assertEqual(out['verdict'], 'new master better')
        self.assertEqual(out['new_master_offers'], {'included': 3})
        same = tracking.compare_masters(live, live, rule)
        self.assertEqual((same['difference'], same['verdict']), (0.0, 'new master not shown better'))

    def test_review_grades_the_new_master_beside_the_live_master(self):
        import price_edge_tracking as tracking
        from master_shortlist import FILE as MASTER_FILE
        generated = self.KICK - pd.Timedelta(hours=20)
        live_pick = {**self.offer(market='Asian Handicap Home +0.50', handicap_side='home', handicap_line=0.5,
                                  price=1.6), 'master_rank': 1}
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            archive = self.archive(root, [('d' * 40, generated, generated,
                                           [self.offer(price=1.40),
                                            self.offer(decision='LEFT_OUT', new_master_group='left_out')])])
            directory = root / 'performance' / 'snapshots' / ('d' * 16)
            pd.DataFrame([live_pick]).to_csv(directory / MASTER_FILE, index=False)
            archive[0][0]['sha256'][MASTER_FILE] = '0' * 64
            final = {'home_goals': 0, 'away_goals': 1}
            with mock.patch('closing_odds.load_observations', return_value=([], [])), \
                    mock.patch('performance_tracking.fixture_match', return_value=(final, 'VERIFIED_FINISHED')):
                summary = tracking.review(root, archive, [], self.KICK + pd.Timedelta(hours=5))
            report = (root / tracking.OUTPUT_DIR / 'report.md').read_text(encoding='utf-8')
            graded = pd.read_csv(root / tracking.OUTPUT_DIR / 'master_shortlist_new_picks.csv')
        self.assertEqual((summary['new_master_picks'], summary['master_picks']), (1, 1))
        self.assertAlmostEqual(summary['new_master']['profit']['mean'], 0.40)  # away +1.00 wins 0-1 at 1.40
        self.assertAlmostEqual(summary['master']['profit']['mean'], -1.0)     # home +0.50 loses
        self.assertEqual(set(summary['new_master']['by_labels']), {'both agree'})
        self.assertEqual(len(graded), 1)
        comparison = summary['master_comparison']
        self.assertEqual((comparison['status'], comparison['new_master']['graded_matches']), ('WAITING', 1))
        self.assertEqual((comparison['new_master_offers']['offers'], comparison['new_master_offers']['included']),
                         (2, 1))
        self.assertIn('New master (shadow, revised master rule)', report)
        self.assertIn('waiting for at least 150 graded matches', report)
        self.assertIn('research strongly disagrees 0', report)

    def test_the_new_file_is_an_allowed_snapshot_sidecar(self):
        import performance_tracking  # noqa: F401  (load_snapshot's optional set is checked by source)
        import prediction_runs
        import workflow_checks
        self.assertIn(CONFIG['file'], prediction_runs.SIDECARS)
        self.assertIn(CONFIG['file'], workflow_checks.SIDECARS)
        source = (REPO / 'performance_tracking.py').read_text(encoding='utf-8')
        self.assertIn("'master_shortlist_new.csv'}", source)
        self.assertIn('capture_new_master_file', source)


class BacktestTest(unittest.TestCase):
    """--mode master: picks never read results, every week stands alone, the holdout is never read, C and C6 are
    both run as the research view, and PR #171's rule is scored beside the new one on the same offers."""

    @staticmethod
    def fixture(margin=1, week='2023-W10', key='EPL|2023-03-11|A|B', research_shift=0.6, cagey_shift=0.35,
                c6=0.5):
        def grid(shift):
            margins = list(range(-5, 6))
            probs = np.exp(-0.5 * ((np.array(margins) - shift) / 1.6) ** 2)
            return [margins, (probs / probs.sum()).tolist()]
        return {'phase': 'development', 'week': week, 'league': 'EPL', 'fixture_key': key, 'market_book': 'pinnacle',
                'date': '2023-03-11', 'home_team': key.split('|')[2], 'away_team': key.split('|')[3],
                'margin': margin, 'hda': [1.8, 3.8, 4.6], 'ah': [-0.5, 1.82, 2.08],
                'C': grid(research_shift), 'D': grid(cagey_shift), 'M': grid(0.3),
                'C6': None if c6 is None else grid(c6)}

    def test_picks_never_read_the_result(self):
        import evaluation_harness as eh
        drop = ['return', 'observed_no_loss']
        for research in eh.MASTER_RESEARCH:
            rows = [pd.DataFrame(eh.master_select_week(eh.master_fixture(self.fixture(margin=m, cagey_shift=2.0),
                                                                         CONFIG, research=research), CONFIG))
                    for m in (-3, 0, 1, 4)]
            for other in rows[1:]:
                pd.testing.assert_frame_equal(rows[0].drop(columns=drop), other.drop(columns=drop))
            self.assertNotEqual(list(rows[0]['return']), list(rows[-1]['return']))
            self.assertTrue(rows[0].new_master_decision.eq('SHORTLISTED').any())

    def test_both_views_on_every_pooled_offer_and_both_rules_as_written(self):
        import evaluation_harness as eh
        for research, cagey_shift in itertools.product(eh.MASTER_RESEARCH, (0.35, 2.0, 2.6)):
            rows = eh.master_fixture(self.fixture(cagey_shift=cagey_shift), CONFIG, research=research)
            self.assertTrue(rows)
            for row in rows:
                self.assertTrue(row['in_value_shortlist'] or row['in_cagey_tier'])
                args = (row['research_no_loss_probability'], row['cagey_no_loss_probability'],
                        row['research_expected_return'], row['offered_decimal_odds'], row['cagey_fair_odds'],
                        row['market_no_loss_probability'], row['market_fair_odds'], False)
                self.assertIsNotNone(args[0])
                self.assertIsNotNone(args[1])
                self.assertEqual((row['new_master_group'], row['gap_check'], labels(row)), independent(*args))
                self.assertEqual((row['v1_group'], row['v1_gap_check']), independent_v1(*args))

    def test_a_missing_c6_forecast_has_no_research_check(self):
        import evaluation_harness as eh
        rows = eh.master_fixture(self.fixture(c6=None), CONFIG, research='C6')
        self.assertTrue(rows)
        self.assertFalse(any(r['in_value_shortlist'] for r in rows))  # no research view: no value nominations
        self.assertTrue(all(r['missing_view'] == 'research' and r['no_research_check'] for r in rows))

    def test_each_week_stands_alone(self):
        import evaluation_harness as eh
        week = [self.fixture(cagey_shift=2.0), self.fixture(margin=0, key='EPL|2023-03-12|C|D')]
        later = [self.fixture(margin=-2, week='2023-W11', key=f'EPL|2023-03-18|E{i}|F{i}', research_shift=2.0,
                              cagey_shift=2.0 + i / 100, c6=1.22)
                 for i in range(20)]
        alone, _ = eh.master_frame(week)
        mixed, _ = eh.master_frame(week + later)
        first = mixed.loc[mixed.week.eq('2023-W10')].reset_index(drop=True)
        pd.testing.assert_frame_equal(alone.astype(object).where(alone.notna(), None),
                                      first[alone.columns].astype(object).where(first[alone.columns].notna(), None))
        second = mixed.loc[mixed.week.eq('2023-W11')]
        self.assertEqual(int(second.new_master_decision.eq('SHORTLISTED').sum()), 15)  # target per week
        self.assertEqual(int(second.new_master_decision.eq('BEYOND_TARGET').sum()), 5)
        self.assertEqual(int(second.v1_decision.eq('SHORTLISTED').sum()), 15)
        self.assertEqual(int(second.live_master_rank.max()), 15)
        ranked = second.loc[second.new_master_decision.eq('SHORTLISTED')].sort_values('new_master_rank')
        self.assertTrue(ranked.ranking_no_loss_probability.is_monotonic_decreasing)  # cagey no-loss only

    def test_the_summary_reports_both_views_the_previous_rule_and_the_flag(self):
        import evaluation_harness as eh
        rng = np.random.default_rng(2)
        fixtures = [self.fixture(margin=int(rng.integers(-3, 4)), week=f'2023-W1{w}',
                                 key=f'EPL|2023-03-1{w}|A{i}|B{i}', research_shift=float(rng.normal(1.2, 1.0)),
                                 cagey_shift=float(rng.normal(1.8, .8)), c6=float(rng.normal(1.2, 1.0)))
                    for w in range(3) for i in range(12)]
        frames = {name: eh.master_frame(fixtures, name)[0] for name in eh.MASTER_RESEARCH}
        summary = eh.master_summary(frames, None, len(fixtures), {})
        self.assertEqual((summary['rule'], summary['previous_rule']), (mr.VERSION, master_rule_v1.VERSION))
        period = summary['periods']['development']
        self.assertEqual(set(period['research_views']), {'C', 'C6'})
        for name, view in period['research_views'].items():
            self.assertEqual(set(view['bets_by_gap_check']), set(eh.MASTER_GAP_CATEGORIES))
            new = frames[name].loc[frames[name].new_master_decision.eq('SHORTLISTED')]
            self.assertEqual(view['new_master']['picks'], len(new))
            self.assertEqual(view['previous_rule']['picks'], int(frames[name].v1_decision.eq('SHORTLISTED').sum()))
            for key in ('new_minus_live_return', 'new_minus_previous_rule_return'):
                self.assertIn('interval_95', view[key])
            flag = view['inspection_flag']
            self.assertEqual(flag['offers']['offers'], int(frames[name].inspection_flag.eq(True).sum()))
            self.assertEqual(flag['on_list']['offers'], int(new.inspection_flag.eq(True).sum()))
            if flag['offers']['offers']:
                self.assertIsNotNone(flag['offers']['observed_minus_cagey'])
                self.assertEqual(flag['offers']['weeks_in_period'], 3)
        self.assertGreater(sum(v['inspection_flag']['offers']['offers'] for v in period['research_views'].values()), 0)
        self.assertIn('new_master_return_C6_minus_C', period['C6_vs_C'])
        self.assertEqual(period['live_master']['picks'], int(frames['C'].live_master_rank.notna().sum()))

    def test_the_backtest_is_locked(self):
        import evaluation_harness as eh
        with self.assertRaises(ValueError):
            eh.evaluate_league('EPL', '.football_cache', {}, True, master_rows=[])
        with mock.patch.object(eh, 'evaluate_league', lambda *a, **k: k['master_rows'].append({'phase': 'holdout'})):
            with self.assertRaises(ValueError):
                eh.master_league('Eredivisie', '.football_cache', {})
        leak = (None,) * 6 + ([{'identity': {'phase': 'holdout'}}],)
        with mock.patch.object(eh, 'evaluate_league', lambda *a, **k: leak):
            with self.assertRaises(ValueError):
                eh.master_league('Eredivisie', '.football_cache', {})
        with self.assertRaises(ValueError):
            eh.main(['--mode', 'master', '--output', tempfile.mkdtemp(), '--declaration', 'x.json'])

    def test_research_cagey_and_c6_inputs_are_walk_forward(self):
        """Real cache, two 14-day folds (4 and 18 Mar 2024): results changed from a date on never move the C, C6,
        D or M input of a match whose fold starts on or before that date; later folds may learn from them."""
        import evaluation_harness as eh
        cfg = {**json.loads((REPO / 'evaluation_harness_config.json').read_text(encoding='utf-8')),
               'test_start': '2024-03-04', 'end_exclusive': '2024-04-01', 'seasons': ['2122', '2223', '2324']}
        load = eh.hb.load_history
        second_fold = pd.Timestamp('2024-03-18')

        def flipped_from(start):
            def loader(cache_dir, league, load_cfg):
                data, sources, extra = load(cache_dir, league, load_cfg)
                data = data.copy()
                window = data.Date >= pd.Timestamp(start)
                data.loc[window, ['FTHG', 'FTAG']] = data.loc[window, ['FTAG', 'FTHG']].to_numpy() + [[3, 0]]
                return data, sources, extra
            return loader

        def run():
            rows, research = eh.master_league('EPL', cache, cfg)
            return eh.master_attach_c6(rows, research, cfg)

        cache = str(REPO / '.football_cache')
        base = run()
        self.assertGreater(len(base), 15)
        self.assertEqual({r['phase'] for r in base}, {'development'})
        self.assertTrue(all(r['C6'] is not None for r in base))
        for start, frozen in (('2024-03-04', lambda r: pd.Timestamp(r['date']) < second_fold),
                              ('2024-03-18', lambda r: True)):
            with mock.patch.object(eh.hb, 'load_history', flipped_from(start)):
                changed = run()
            self.assertEqual([r['fixture_key'] for r in base], [r['fixture_key'] for r in changed])
            self.assertTrue(all(a['margin'] != b['margin'] for a, b in zip(base, changed)
                                if pd.Timestamp(a['date']) >= pd.Timestamp(start)))
            for a, b in zip(base, changed):
                self.assertEqual((a['hda'], a['ah']), (b['hda'], b['ah']))
                if frozen(a):
                    for cand in (*eh.MASTER_CANDIDATES, 'C6'):
                        self.assertEqual(a[cand], b[cand], (start, a['fixture_key'], cand))


if __name__ == '__main__':
    unittest.main()
