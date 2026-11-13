"""The new master, in shadow (master_reconciliation.py, Paul's master rule, rule master-new-paul-rule-v1).

Every rule exactly as written (the 4.0-point boundaries in both directions, safe-but-below-fair kept, risky left
out, the missing-evidence fallback to Pinnacle's margin-free probability), both views on every offer either list
nominates, European rows flagged, the live master byte-identical, live grading beside the live master with the
comparison rule, and the offline backtest walk-forward and locked.
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
import master_shortlist
import narrow_margin as nm
import price_edge_cagey_shortlist as v28

REPO = Path(__file__).resolve().parents[1]
FROZEN = json.loads((Path(__file__).with_name('fixtures') / 'frozen_forecast_row.json').read_text(encoding='utf-8'))
POLICY = json.loads((REPO / 'shortlist_quote_policy.json').read_text(encoding='utf-8'))
CONFIG = mr.load_config()
MARGIN = 0.026955172735899154


def production_run(row=None):
    """The production rules on a real frozen forecast (Brighton v Brentford, 8 Nov 2026)."""
    predictions = pd.DataFrame([row or FROZEN['row']])
    _, decisions, summary = v28.build_shortlist(predictions, FROZEN['snapshot_generated_utc'], execution_policy=POLICY,
                                                settings=v28.load_settings(), model=nm.production_model())
    summary['quote_execution_policy'] = POLICY
    return predictions, decisions, summary


def binary(p):
    return np.array([p, 0., 0., 0., 1 - p])


def classify(pr, pc, price, pin=None, pin_fair=None, european=False, **kw):
    """Shorthand: binary research/cagey views (None = that view missing)."""
    return mr.classify(None if pr is None else binary(pr), None if pc is None else binary(pc), price, 0., pin, pin_fair,
                       european=european, config=CONFIG, **kw)


def independent(pr, pc, research_ev, price, cagey_fair, pin, pin_fair, european):
    """The written rule, re-derived without the module's code: (group, gap check)."""
    tol = 1e-9
    if pr is None and pc is None:
        return 'left_out', 'no_view'
    if pr is not None and pc is not None:
        g = 100 * (pr - pc)
        if g >= 4.0 - tol:
            return 'left_out', 'ignored'
        if g <= -4.0 + tol:
            return 'left_out', 'vetoed'
        check, chance, fair_odds, can_agree = 'kept', pc, cagey_fair, not european
    else:
        if pin is None:
            return 'left_out', 'one_view_missing_no_pinnacle'
        if abs(100 * ((pr if pr is not None else pc) - pin)) >= 4.0 - tol:
            return 'left_out', 'one_view_missing_apart'
        check = 'one_view_missing_kept'
        chance, fair_odds = (pc, cagey_fair) if pc is not None else (pin, pin_fair)
        can_agree = pc is not None and pr is not None and not european  # never: one view is missing
    safe, risky = chance >= 0.75 - tol, chance < 0.50
    fair = fair_odds is not None and price * (1 + MARGIN) >= fair_odds - tol
    edge = pr is not None and research_ev > 0
    if risky:
        return 'left_out', check
    if edge and (safe or fair) and can_agree:
        return 'both_agree', check
    if safe:
        return 'market_safe', check
    return 'left_out', check


class DefinitionsTest(unittest.TestCase):
    def test_config_holds_the_written_rule(self):
        self.assertEqual(CONFIG['version'], 'master-new-paul-rule-v1')
        self.assertEqual(CONFIG['file'], 'master_shortlist_new.csv')
        self.assertEqual(CONFIG['target_fixtures'], 15)
        self.assertEqual(CONFIG['execution']['bookmaker'], 'Pinnacle')
        self.assertEqual((CONFIG['gap']['too_optimistic_min_points'], CONFIG['gap']['too_pessimistic_max_points']),
                         (4.0, -4.0))
        view = CONFIG['market_view']
        self.assertEqual((view['safe']['min_no_loss'], view['risky']['max_no_loss_exclusive']), (0.75, 0.5))
        self.assertIn('approved by Paul on 13 Nov 2026', view['status'])
        self.assertNotIn('disagreement', CONFIG)  # the 5-point flag is replaced for this list
        import evaluation_harness as eh
        harness = json.loads((REPO / 'evaluation_harness_config.json').read_text(encoding='utf-8'))
        rule = next(r for r in eh.calibration_rules(harness).values() if r.get('kind') == 'cagey_events')
        self.assertEqual(view['fair']['pinnacle_average_margin'], rule['synthetic_ah_margin']['pinnacle']['margin'])
        live = CONFIG['live_comparison']
        self.assertEqual((live['min_graded_matches'], live['min_weeks']), (150, 3))
        self.assertIn('entirely above zero', live['rule'])

    def test_no_loss_counts_wins_half_wins_and_pushes(self):
        mass = np.array([.40, .10, .20, .05, .25])
        self.assertAlmostEqual(mr.no_loss(mass), 0.70)
        out = mr.classify(mass, mass, 1.6, 0., european=False, config=CONFIG)
        self.assertAlmostEqual(out['research_no_loss_probability'], 0.70)
        self.assertAlmostEqual(out['cagey_no_loss_probability'], 0.70)
        self.assertAlmostEqual(out['gap_points'], 0.)

    def test_the_four_point_boundaries_in_both_directions(self):
        # cagey 0.75 (safe), research edge at 1.40 in every case below the ignore line.
        for pr, check in ((0.79, 'ignored'), (0.7901, 'ignored'), (0.789999, 'kept'), (0.75, 'kept'),
                          (0.710001, 'kept'), (0.71, 'vetoed'), (0.7099, 'vetoed')):
            out = classify(pr, 0.75, 1.40)
            self.assertEqual(out['gap_check'], check, pr)
            self.assertAlmostEqual(out['gap_points'], 100 * (pr - 0.75))
            if check != 'kept':
                self.assertEqual((out['new_master_group'], out['left_out_reason']), ('left_out', check))
        # exact representable gaps: 0.5625 - 0.5225 = 0.04 and the reverse
        self.assertEqual(classify(0.5625, 0.5225, 1.9)['gap_check'], 'ignored')
        self.assertEqual(classify(0.5225, 0.5625, 1.9)['gap_check'], 'vetoed')

    def test_vetoed_even_if_the_cagey_tier_rates_it_safe_and_fair(self):
        out = classify(0.70, 0.80, 1.30)  # cagey safe, fair; research 10 points lower
        self.assertEqual((out['gap_check'], out['new_master_group']), ('vetoed', 'left_out'))
        self.assertEqual((out['market_safety'], out['market_price']), ('safe', 'fair'))  # still shown

    def test_too_optimistic_research_is_ignored_and_the_bet_left_out(self):
        out = classify(0.70, 0.60, 1.70)  # research edge (+19%), cagey fair (1.70 x 1.027 >= 1.667)
        self.assertEqual((out['gap_check'], out['new_master_group'], out['left_out_reason']),
                         ('ignored', 'left_out', 'ignored'))

    def test_both_agree(self):
        safe = classify(0.80, 0.78, 1.30)  # edge 4%, safe
        self.assertEqual((safe['new_master_group'], safe['market_safety']), ('both_agree', 'safe'))
        fair = classify(0.62, 0.60, 1.65)  # edge 2.3%, middle, fair (1.65 x 1.027 = 1.694 >= 1.667)
        self.assertEqual((fair['new_master_group'], fair['market_safety'], fair['market_price']),
                         ('both_agree', 'middle', 'fair'))

    def test_safe_but_below_fair_is_kept_as_market_safe(self):
        out = classify(0.76, 0.78, 1.20)  # no research edge (EV -8.8%); cagey fair odds 1.282 > 1.20 x 1.027
        self.assertEqual((out['market_safety'], out['market_price'], out['research_edge']), ('safe', 'below fair', False))
        self.assertEqual(out['new_master_group'], 'market_safe')
        edge = classify(0.815, 0.78, 1.24)  # research edge +1.1%, 1.24 x 1.027 < 1.282: safe is enough for Both agree
        self.assertEqual((edge['market_price'], edge['new_master_group']), ('below fair', 'both_agree'))

    def test_risky_is_left_out_whatever_the_research_says(self):
        out = classify(0.52, 0.49, 2.00)  # research edge, cagey fair (2.054 >= 2.041), but risky
        self.assertEqual((out['research_edge'], out['market_price'], out['market_safety']), (True, 'fair', 'risky'))
        self.assertEqual((out['new_master_group'], out['left_out_reason']), ('left_out', 'risky'))

    def test_neither_safe_nor_fair_with_an_edge_is_left_out(self):
        out = classify(0.58, 0.56, 1.70)  # edge -1.4%: no edge; middle -> not safe
        self.assertEqual((out['research_edge'], out['market_safety'], out['new_master_group']),
                         (False, 'middle', 'left_out'))
        edge_below = classify(0.62, 0.60, 1.62)  # edge +0.4%, middle, 1.62 x 1.027 = 1.664 < 1.667: below fair
        self.assertEqual((edge_below['research_edge'], edge_below['market_price'], edge_below['new_master_group']),
                         (True, 'below fair', 'left_out'))
        self.assertEqual(edge_below['left_out_reason'], 'neither safe nor fair with a research edge')

    def test_missing_research_falls_back_to_pinnacle_in_both_directions(self):
        kept = classify(None, 0.80, 1.25, pin=0.78)  # cagey 2 points from Pinnacle, safe
        self.assertEqual((kept['gap_check'], kept['new_master_group'], kept['one_view_missing'], kept['missing_view']),
                         ('one_view_missing_kept', 'market_safe', True, 'research'))
        self.assertAlmostEqual(kept['pinnacle_gap_points'], 2.0)
        self.assertIsNone(kept['gap_points'])
        for pin in (0.76, 0.84, 0.7599, 0.8401):  # 4.0 points or more apart, either direction
            out = classify(None, 0.80, 1.25, pin=pin)
            self.assertEqual((out['gap_check'], out['new_master_group']), ('one_view_missing_apart', 'left_out'), pin)
        for pin in (0.7601, 0.8399):  # just inside
            self.assertEqual(classify(None, 0.80, 1.25, pin=pin)['gap_check'], 'one_view_missing_kept', pin)
        self.assertEqual(classify(None, 0.80, 1.25)['gap_check'], 'one_view_missing_no_pinnacle')
        middle = classify(None, 0.70, 1.50, pin=0.70)  # no research edge, not safe: left out
        self.assertEqual(middle['new_master_group'], 'left_out')

    def test_missing_cagey_uses_pinnacle_and_never_both_agree(self):
        safe = classify(0.80, None, 1.40, pin=0.78, pin_fair=1.30)  # research edge, Pinnacle safe
        self.assertEqual((safe['market_basis'], safe['new_master_group'], safe['missing_view']),
                         ('pinnacle', 'market_safe', 'cagey'))
        fair_only = classify(0.64, None, 1.70, pin=0.62, pin_fair=1.613)  # edge, Pinnacle fair, not safe
        self.assertEqual((fair_only['market_price'], fair_only['market_safety'], fair_only['new_master_group']),
                         ('fair', 'middle', 'left_out'))
        risky = classify(0.48, None, 2.0, pin=0.47, pin_fair=2.13)
        self.assertEqual((risky['new_master_group'], risky['left_out_reason']), ('left_out', 'risky'))
        for pin in (0.76, 0.84):  # research 4 points from Pinnacle, either direction
            self.assertEqual(classify(0.80, None, 1.40, pin=pin, pin_fair=1.3)['gap_check'], 'one_view_missing_apart')
        both = classify(None, None, 1.4, pin=0.8)
        self.assertEqual((both['gap_check'], both['new_master_group'], both['missing_view']),
                         ('no_view', 'left_out', 'both'))

    def test_european_rows_are_flagged_and_never_both_agree(self):
        safe = classify(0.80, 0.78, 1.30, european=True)
        self.assertEqual((safe['unvalidated_view'], safe['new_master_group']), (True, 'market_safe'))
        fair = classify(0.62, 0.60, 1.65, european=True)
        self.assertEqual(fair['new_master_group'], 'left_out')
        self.assertEqual(classify(0.70, 0.80, 1.30, european=True)['gap_check'], 'vetoed')  # the gap rule applies

    def test_the_rule_on_a_grid_against_an_independent_derivation(self):
        values = [None, *np.linspace(.42, .92, 11)]
        for pr, pc, price, european, pin in itertools.product(values, values, (1.16, 1.3, 1.55, 1.8, 2.0),
                                                              (False, True), (None, .6, .79)):
            pin_fair = None if pin is None else 1 / pin
            out = classify(pr, pc, price, pin, pin_fair, european)
            ev = None if pr is None else pr * price - 1
            expected = independent(pr, pc, ev, price, None if pc is None else 1 / pc, pin, pin_fair, european)
            self.assertEqual((out['new_master_group'], out['gap_check']), expected, (pr, pc, price, european, pin))

    def test_the_offline_switches_only_drop_their_half_of_the_check(self):
        self.assertEqual(classify(0.70, 0.80, 1.30, veto=False)['new_master_group'], 'market_safe')
        self.assertEqual(classify(0.70, 0.80, 1.30, ignore=False)['gap_check'], 'vetoed')
        self.assertEqual(classify(0.84, 0.80, 1.30, ignore=False)['new_master_group'], 'both_agree')
        self.assertEqual(classify(0.84, 0.80, 1.30, veto=False)['gap_check'], 'ignored')


class SelectTest(unittest.TestCase):
    @staticmethod
    def row(match, group, chance, odds, market='m'):
        return {'_match': match, 'new_master_group': group, 'ranking_no_loss_probability': chance,
                'offered_decimal_odds': odds, 'market': market, 'kickoff_utc': '2026-11-08', 'league': 'L',
                'home_team': match, 'away_team': 'x', 'left_out_reason': None if group != 'left_out' else 'vetoed'}

    def test_one_pick_per_match_best_group_then_no_loss_then_odds(self):
        rows = [self.row('A', 'market_safe', .90, 1.20, 'a1'), self.row('A', 'both_agree', .70, 1.60, 'a2'),
                self.row('B', 'market_safe', .80, 1.30, 'b1'), self.row('B', 'market_safe', .85, 1.25, 'b2'),
                self.row('C', 'both_agree', .76, 1.40, 'c1'), self.row('C', 'both_agree', .76 + 1e-13, 1.33, 'c2'),
                self.row('D', 'left_out', .99, 1.16, 'd1')]
        mr.select(rows, 15)
        picks = {r['market']: (r['new_master_rank'], r['new_master_decision']) for r in rows}
        self.assertEqual(picks['c1'], (1, 'SHORTLISTED'))  # Both agree first; equal chance -> higher odds
        self.assertEqual(picks['a2'], (2, 'SHORTLISTED'))
        self.assertEqual(picks['b2'], (3, 'SHORTLISTED'))  # Market-safe after, by no-loss
        self.assertEqual([picks[k][1] for k in ('a1', 'b1', 'c2', 'd1')],
                         ['NOT_SELECTED', 'NOT_SELECTED', 'NOT_SELECTED', 'LEFT_OUT'])

    def test_fifteen_match_target(self):
        rows = [self.row(f'M{i:02d}', 'market_safe', .80 - i / 1000, 1.25) for i in range(18)]
        mr.select(rows, 15)
        self.assertEqual([r['new_master_rank'] for r in rows[:15]], list(range(1, 16)))
        self.assertEqual({r['new_master_decision'] for r in rows[15:]}, {'BEYOND_TARGET'})

    def test_non_executable_offers_are_never_picked(self):
        rows = [{**self.row('A', 'both_agree', .9, 1.1), 'new_master_executable': False,
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

    def test_groups_follow_the_rule_on_real_rows(self):
        for row in self.frame.to_dict('records'):
            expected = independent(row['research_no_loss_probability'], row['cagey_no_loss_probability'],
                                   row['research_expected_return'], row['offered_decimal_odds'],
                                   row['cagey_fair_odds'], row['pinnacle_no_loss_probability'],
                                   row['pinnacle_fair_odds'], False)
            self.assertEqual((row['new_master_group'], row['gap_check']), expected)
        self.assertIn('ignored', set(self.frame.gap_check))  # this forecast has an ignored offer

    def test_one_pick_per_match_target_and_pinnacle_only(self):
        ranked = self.frame.loc[self.frame.new_master_decision.eq('SHORTLISTED')]
        self.assertEqual(len(ranked), 1)
        self.assertTrue(ranked.new_master_group.isin(mr.RANKED).all())
        self.assertTrue(ranked.bookmaker.eq('Pinnacle').all())
        self.assertEqual(ranked.iloc[0].market, 'Asian Handicap Home +0.25')  # equal no-loss chance, higher odds
        self.assertFalse(self.frame.loc[self.frame.new_master_group.eq('left_out'),
                                        'new_master_decision'].isin(['SHORTLISTED', 'BEYOND_TARGET']).any())

    def test_a_vetoed_cagey_pick_is_left_out(self):
        broken = self.decisions.copy()
        target = broken.cagey_tier_decision.eq('SHORTLISTED') & broken.market.eq('Asian Handicap Home +0.50')
        index = broken.index[target][0]
        broken.loc[index, [f'research_p_{k}' for k in mr.KINDS]] = [0.70, 0., 0., 0., 0.30]  # 6.4 points below cagey
        frame = mr.reconcile(broken)
        row = frame.loc[frame.market.eq('Asian Handicap Home +0.50')].iloc[0]
        self.assertEqual((row.gap_check, row.new_master_decision, row.in_cagey_tier), ('vetoed', 'LEFT_OUT', True))
        summary = mr.summary(frame)
        self.assertEqual((summary['vetoed'], summary['vetoed_cagey_picks'], summary['ignored']), (1, 1, 1))

    def test_missing_research_falls_back_to_pinnacle_and_is_counted(self):
        broken = self.decisions.copy()
        index = broken.index[broken.cagey_tier_decision.eq('SHORTLISTED')
                             & broken.market.eq('Asian Handicap Home +0.50')][0]
        broken.loc[index, [f'research_p_{k}' for k in mr.KINDS]] = np.nan  # a team the research model can't score
        frame = mr.reconcile(broken)
        row = frame.loc[frame.market.eq('Asian Handicap Home +0.50')].iloc[0]
        self.assertEqual((row.gap_check, row.missing_view, row.new_master_group),
                         ('one_view_missing_kept', 'research', 'market_safe'))  # 0.764 vs Pinnacle 0.763, safe
        self.assertTrue(row.one_view_missing)
        self.assertAlmostEqual(row.pinnacle_gap_points, 100 * (row.cagey_no_loss_probability
                                                               - row.pinnacle_no_loss_probability))
        summary = mr.summary(frame)
        self.assertEqual(summary['one_view_missing']['offers'], 1)
        self.assertEqual(summary['one_view_missing']['kept_by_pinnacle_check'], 1)
        unsynced = self.decisions.copy()
        unsynced.loc[index, 'cagey_input_timing_status'] = 'UNAVAILABLE_OR_UNSYNCHRONIZED'
        frame = mr.reconcile(unsynced)
        row = frame.loc[frame.market.eq('Asian Handicap Home +0.50')].iloc[0]
        self.assertEqual((row.missing_view, row.market_basis), ('cagey', 'pinnacle'))
        self.assertNotEqual(row.new_master_group, 'both_agree')

    def test_a_missing_espn_match_is_not_missing_evidence(self):
        flagged = self.decisions.copy()
        flagged['research_warnings'] = 'free-source fixture identity missing or ambiguous'
        self.assertFalse(mr.reconcile(flagged).one_view_missing.any())

    def test_european_rows_are_flagged_and_never_both_agree(self):
        europe = mr.reconcile(self.decisions.assign(league='UEFA Champions League'))
        self.assertTrue(europe.unvalidated_view.all())
        self.assertFalse(europe.new_master_group.eq('both_agree').any())
        self.assertTrue(europe.new_master_group.eq('market_safe').any())  # safe offers may enter Market-safe
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
        return {'new_master_rank': 1 if decision == 'SHORTLISTED' else None, 'new_master_group': 'market_safe',
                'new_master_decision': decision, 'league': 'Premier League', 'home_team': home,
                'away_team': 'Away FC', 'kickoff_utc': self.KICK.isoformat(), 'market': 'Asian Handicap Away +1.00',
                'market_to_bet': 'Away +1.00', 'handicap_side': 'away', 'handicap_line': 1.0, 'bookmaker': 'Pinnacle',
                'offered_decimal_odds': price, 'per_stake_cost': 0., 'fair_odds': 1.33, 'reference_type': 'a',
                'evaluated_at_utc': generated, 'selection_policy_version': v28.POLICY,
                'new_master_version': mr.VERSION, 'gap_check': 'kept', 'one_view_missing': False, **extra}

    def test_capture_binds_to_its_generation_and_rule(self):
        import price_edge_tracking as tracking
        generated = (self.KICK - pd.Timedelta(hours=20)).isoformat()
        with tempfile.TemporaryDirectory() as tmp:
            raw = Path(tmp)
            self.assertIsNone(tracking.capture_new_master_file(raw, generated))
            pd.DataFrame([self.offer()]).to_csv(raw / CONFIG['file'], index=False)
            self.assertEqual(tracking.capture_new_master_file(raw, generated), raw / CONFIG['file'])
            self.assertIsNone(tracking.capture_new_master_file(raw, self.KICK.isoformat()))
            pd.DataFrame([self.offer(new_master_version='master-reconciliation-shadow-v1')]).to_csv(
                raw / CONFIG['file'], index=False)
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
                 [self.offer(price=1.31), self.offer(decision='LEFT_OUT', price=1.9, gap_check='vetoed')]),
                ('b' * 40, day - pd.Timedelta(hours=15), day - pd.Timedelta(hours=11), [self.offer(price=1.20)]),
                # captured 10 minutes before kickoff: never graded (lead check)
                ('c' * 40, self.KICK - pd.Timedelta(minutes=15), self.KICK - pd.Timedelta(minutes=10),
                 [self.offer(price=1.50)])])
            rows = tracking.frozen_new_master_picks(root, archive)
            counts = tracking.new_master_offer_counts(root, archive)
        self.assertEqual([float(r['offered_decimal_odds']) for r in rows], [1.31])
        self.assertEqual((counts['fixtures'], counts['offers'], counts['vetoed']), (1, 2, 1))

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
        out = tracking.compare_masters(better, live, rule, {'vetoed': 3})
        self.assertEqual(out['status'], 'COMPARED')
        self.assertGreater(out['interval_95'][0], 0)
        self.assertEqual(out['verdict'], 'new master better')
        self.assertEqual(out['new_master_offers'], {'vetoed': 3})
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
            archive = self.archive(root, [('d' * 40, generated, generated, [self.offer(price=1.40),
                                                                           self.offer(decision='LEFT_OUT')])])
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
        self.assertEqual(len(graded), 1)
        comparison = summary['master_comparison']
        self.assertEqual((comparison['status'], comparison['new_master']['graded_matches']), ('WAITING', 1))
        self.assertEqual(comparison['new_master_offers']['offers'], 2)
        self.assertIn('New master (shadow', report)
        self.assertIn('waiting for at least 150 graded matches', report)

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
    """--mode master: picks never read results, every week stands alone, the holdout is never read, and C and C6
    are both run as the research view."""

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
            rows = [pd.DataFrame(eh.master_select_week(eh.master_fixture(self.fixture(margin=m), CONFIG,
                                                                         research=research), CONFIG))
                    for m in (-3, 0, 1, 4)]
            for other in rows[1:]:
                pd.testing.assert_frame_equal(rows[0].drop(columns=drop), other.drop(columns=drop))
            self.assertNotEqual(list(rows[0]['return']), list(rows[-1]['return']))

    def test_both_views_on_every_pooled_offer_and_the_rule_as_written(self):
        import evaluation_harness as eh
        for research in eh.MASTER_RESEARCH:
            rows = eh.master_fixture(self.fixture(), CONFIG, research=research)
            self.assertTrue(rows)
            for row in rows:
                self.assertTrue(row['in_value_shortlist'] or row['in_cagey_tier'])
                self.assertIsNotNone(row['research_no_loss_probability'])
                self.assertIsNotNone(row['cagey_no_loss_probability'])
                expected = independent(row['research_no_loss_probability'], row['cagey_no_loss_probability'],
                                       row['research_expected_return'], row['offered_decimal_odds'],
                                       row['cagey_fair_odds'], row['market_no_loss_probability'],
                                       row['market_fair_odds'], False)
                self.assertEqual((row['new_master_group'], row['gap_check']), expected)

    def test_a_missing_c6_forecast_falls_back_to_pinnacle(self):
        import evaluation_harness as eh
        rows = eh.master_fixture(self.fixture(c6=None), CONFIG, research='C6')
        self.assertTrue(rows)
        self.assertFalse(any(r['in_value_shortlist'] for r in rows))  # no research view: no value nominations
        self.assertTrue(all(r['missing_view'] == 'research' for r in rows))
        self.assertTrue(all(r['gap_check'].startswith('one_view_missing') for r in rows))

    def test_each_week_stands_alone(self):
        import evaluation_harness as eh
        week = [self.fixture(), self.fixture(margin=0, key='EPL|2023-03-12|C|D')]
        later = [self.fixture(margin=-2, week='2023-W11', key=f'EPL|2023-03-18|E{i}|F{i}', research_shift=1.25,
                              cagey_shift=1.2, c6=1.22)
                 for i in range(20)]
        alone, _ = eh.master_frame(week)
        mixed, _ = eh.master_frame(week + later)
        first = mixed.loc[mixed.week.eq('2023-W10')].reset_index(drop=True)
        pd.testing.assert_frame_equal(alone.astype(object).where(alone.notna(), None),
                                      first[alone.columns].astype(object).where(first[alone.columns].notna(), None))
        second = mixed.loc[mixed.week.eq('2023-W11')]
        self.assertEqual(int(second.new_master_decision.eq('SHORTLISTED').sum()), 15)  # target per week
        self.assertEqual(int(second.new_master_decision.eq('BEYOND_TARGET').sum()), 5)
        self.assertEqual(int(second.live_master_rank.max()), 15)

    def test_the_summary_runs_both_research_views_and_the_veto_counterfactuals(self):
        import evaluation_harness as eh
        rng = np.random.default_rng(2)
        fixtures = [self.fixture(margin=int(rng.integers(-3, 4)), week=f'2023-W1{w}',
                                 key=f'EPL|2023-03-1{w}|A{i}|B{i}', research_shift=float(rng.normal(.4, .8)),
                                 cagey_shift=float(rng.normal(.3, .5)), c6=float(rng.normal(.35, .5)))
                    for w in range(3) for i in range(12)]
        frames = {name: eh.master_frame(fixtures, name)[0] for name in eh.MASTER_RESEARCH}
        summary = eh.master_summary(frames, None, len(fixtures), {})
        period = summary['periods']['development']
        self.assertEqual(set(period['research_views']), {'C', 'C6'})
        for view in period['research_views'].values():
            self.assertEqual(set(view['bets_by_gap_check']), set(eh.MASTER_GAP_CATEGORIES))
            self.assertIn(view['veto_verdict'], ('helps', 'hurts', 'no measurable difference', 'not measurable'))
            vetoed = view['bets_by_gap_check']['vetoed']
            if vetoed['offers']:
                self.assertIsNotNone(vetoed['observed_minus_cagey'])
        self.assertIn('veto_effect_C6_minus_C', period['C6_vs_C'])
        # the live master is C's in both views: the same picks whichever research view the new master uses
        live = lambda f: f.loc[f.live_master_rank.notna(), ['fixture_key', 'market']].to_csv(index=False)
        self.assertEqual(period['live_master']['picks'], int(frames['C'].live_master_rank.notna().sum()))
        self.assertTrue(live(frames['C']))

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
