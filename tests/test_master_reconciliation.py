"""Phase 4 master reconciliation, in shadow (master_reconciliation.py, rule master-reconciliation-shadow-v1).

Both views are scored on every offer either list shortlisted; groups follow the written definitions exactly;
missing evidence is never disagreement; European rows are marked and kept out of Both agree; the live master
files are byte-identical with the shadow on; and the offline backtest is walk-forward and locked.
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


def production_run(row=None):
    """The production rules on a real frozen forecast (Brighton v Brentford, 8 Nov 2026)."""
    predictions = pd.DataFrame([row or FROZEN['row']])
    _, decisions, summary = v28.build_shortlist(predictions, FROZEN['snapshot_generated_utc'], execution_policy=POLICY,
                                                settings=v28.load_settings(), model=nm.production_model())
    summary['quote_execution_policy'] = POLICY
    return predictions, decisions, summary


def binary(p):
    return np.array([p, 0., 0., 0., 1 - p])


def independent_group(research_ev, cagey_no_loss, price, cagey_fair):
    """The written definitions, re-derived without the module's code."""
    edge, loss = research_ev > 0, research_ev < 0
    safe = cagey_no_loss >= 0.75 - 1e-9
    risky = cagey_no_loss < 0.50
    fair = price * (1 + 0.026955172735899154) >= cagey_fair - 1e-9
    if edge and (safe or fair):
        return 'both_agree'
    if edge:
        return 'research_edge'
    if safe:
        return 'market_safe'
    if loss and risky:
        return 'conflict'
    return 'neither'


class DefinitionsTest(unittest.TestCase):
    def test_config_holds_the_written_definitions(self):
        self.assertEqual(CONFIG['version'], 'master-reconciliation-shadow-v1')
        self.assertEqual(CONFIG['target_fixtures'], 15)
        self.assertEqual(CONFIG['execution']['bookmaker'], 'Pinnacle')
        self.assertEqual(CONFIG['disagreement']['min_abs_gap'], 0.05)
        view = CONFIG['market_view']
        self.assertEqual((view['safe']['min_no_loss'], view['risky']['max_no_loss_exclusive']), (0.75, 0.5))
        self.assertIn('proposed', view['status'])
        import evaluation_harness as eh
        harness = json.loads((REPO / 'evaluation_harness_config.json').read_text(encoding='utf-8'))
        rule = next(r for r in eh.calibration_rules(harness).values() if r.get('kind') == 'cagey_events')
        self.assertEqual(view['fair']['pinnacle_average_margin'], rule['synthetic_ah_margin']['pinnacle']['margin'])

    def test_each_group_by_its_definition(self):
        cases = {  # research P(win), cagey P(win), price
            'both_agree': (0.80, 0.80, 1.30),     # research edge, market safe
            'research_edge': (0.70, 0.55, 1.70),  # research edge, market below fair and not safe
            'market_safe': (0.70, 0.80, 1.30),    # no research edge, market safe
            'conflict': (0.40, 0.45, 2.00),       # research expects a loss, market risky
            'neither': (0.55, 0.60, 1.60),        # no research edge, market middle
        }
        for group, (pr, pc, price) in cases.items():
            out = mr.classify(binary(pr), binary(pc), price, 0., None, european=False, config=CONFIG)
            self.assertEqual(out['reconciled_group'], group, group)
        fair = mr.classify(binary(0.62), binary(0.60), 1.65, 0., None, european=False, config=CONFIG)
        self.assertEqual((fair['market_price'], fair['market_safety'], fair['reconciled_group']),
                         ('fairly priced', 'middle', 'both_agree'))  # edge -0.9%: inside Pinnacle's margin

    def test_groups_match_the_definitions_on_a_grid(self):
        lines = [(0., 1.), (.5, .5), (.25, .75)]
        for pr, pc, price, cost, (w, push) in itertools.product(np.linspace(.3, .95, 14), np.linspace(.3, .95, 14),
                                                               (1.16, 1.3, 1.55, 1.8, 2.0), (0., .01), lines):
            research = np.array([pr * w, pr * (1 - w), 0., 0., 1 - pr]) if push == .5 else binary(pr)
            cagey = binary(pc)
            out = mr.classify(research, cagey, price, cost, None, european=False, config=CONFIG)
            ev = float(research @ (np.array([price - 1, (price - 1) / 2, 0, -.5, -1]) - cost))
            self.assertEqual(out['reconciled_group'], independent_group(ev, pc, price, 1 / pc))
            self.assertAlmostEqual(out['research_expected_return'], ev, places=12)

    def test_disagreement_is_a_flag_on_the_win_share(self):
        research = np.array([.40, .10, .20, 0., .30])  # win share (.45) / (.45 + .30) = 0.6
        out = mr.classify(research, binary(.6), 1.7, 0., 0.55, european=False, config=CONFIG)
        self.assertAlmostEqual(out['research_win_share'], 0.6)
        self.assertTrue(out['disagreement'])  # 0.05 apart
        close = mr.classify(research, binary(.6), 1.7, 0., 0.56, european=False, config=CONFIG)
        self.assertFalse(close['disagreement'])
        self.assertEqual(close['reconciled_group'], out['reconciled_group'])  # never a reason to bet
        self.assertIsNone(mr.classify(research, binary(.6), 1.7, 0., None, european=False,
                                      config=CONFIG)['disagreement'])

    def test_missing_evidence_is_never_disagreement(self):
        for research, cagey in ((None, binary(.6)), (binary(.9), None), (None, None)):
            out = mr.classify(research, cagey, 1.5, 0., 0.3, european=False, config=CONFIG)
            self.assertEqual(out['reconciled_group'], 'missing_evidence')
            self.assertIsNone(out['disagreement'])
            self.assertIsNone(out['disagreement_gap'])
            self.assertTrue(out['missing_evidence_reason'])


class LiveShadowTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.predictions, cls.decisions, cls.summary = production_run()
        cls.frame = mr.reconcile(cls.decisions)

    def pooled(self):
        d = self.decisions
        return d.loc[d.decision.eq('SHORTLISTED') | d.cagey_tier_decision.eq('SHORTLISTED')]

    def test_both_views_are_scored_on_every_offer_either_list_considers(self):
        pooled = self.pooled()
        self.assertEqual(len(self.frame), len(pooled))
        self.assertTrue((self.frame.in_value_shortlist & ~self.frame.in_cagey_tier).any())
        self.assertTrue((~self.frame.in_value_shortlist & self.frame.in_cagey_tier).any())
        scored = self.frame.loc[~self.frame.reconciled_group.eq('missing_evidence')]
        self.assertEqual(len(scored), len(self.frame))  # this forecast has both views everywhere
        for column in ('research_expected_return', 'research_win_share', 'cagey_no_loss_probability',
                       'cagey_fair_odds', 'market_safety', 'market_price'):
            self.assertTrue(scored[column].notna().all(), column)

    def test_the_views_are_the_lists_own_figures_on_that_exact_offer(self):
        pooled = self.pooled().reset_index(drop=True)
        key = ['market', 'handicap_side', 'handicap_line', 'offered_decimal_odds']
        merged = self.frame.merge(pooled, on=key, suffixes=('', '_decision'))
        self.assertEqual(len(merged), len(self.frame))
        np.testing.assert_allclose(merged.research_expected_return, merged.profit_expected_return, atol=1e-12)
        np.testing.assert_allclose(merged.research_profit_probability, merged.profit_probability, atol=1e-12)
        np.testing.assert_allclose(merged.cagey_no_loss_probability, merged.cagey_no_loss_probability_decision,
                                   atol=1e-12)
        np.testing.assert_allclose(merged.cagey_expected_return, merged.cagey_expected_return_decision, atol=1e-12)

    def test_groups_are_assigned_exactly_by_the_definitions(self):
        for row in self.frame.to_dict('records'):
            price = row['offered_decimal_odds']
            self.assertEqual(row['reconciled_group'], independent_group(
                row['research_expected_return'], row['cagey_no_loss_probability'], price, row['cagey_fair_odds']))

    def test_one_pick_per_match_target_and_sections(self):
        ranked = self.frame.loc[self.frame.reconciled_decision.eq('SHORTLISTED')]
        self.assertLessEqual(len(ranked), 15)
        self.assertEqual(ranked.home_team.nunique(), len(ranked))
        self.assertTrue(ranked.reconciled_section.isin(['both_agree', 'market_safe']).all())
        self.assertEqual(list(ranked.reconciled_rank), list(range(1, len(ranked) + 1)))
        self.assertTrue(ranked.bookmaker.eq('Pinnacle').all())
        chosen = self.frame.reconciled_decision.isin(['SHORTLISTED', 'BEYOND_TARGET', 'RESEARCH_EDGE_SECTION'])
        self.assertEqual(int(chosen.sum()), self.frame.loc[chosen, ['home_team']].drop_duplicates().shape[0])
        left = self.frame.loc[self.frame.reconciled_group.isin(['conflict', 'neither', 'missing_evidence'])]
        self.assertFalse(left.reconciled_decision.isin(['SHORTLISTED', 'RESEARCH_EDGE_SECTION']).any())

    def test_missing_evidence_is_recorded_and_never_disagreement(self):
        broken = self.decisions.copy()
        target = broken.decision.eq('SHORTLISTED') & broken.cagey_tier_decision.eq('SHORTLISTED')
        index = broken.index[target][0]
        for kind in mr.KINDS:
            broken.loc[index, 'research_p_' + kind] = np.nan  # a team the research model can't score
        frame = mr.reconcile(broken)
        row = frame.loc[(frame.market == broken.at[index, 'market'])
                        & (frame.offered_decimal_odds == broken.at[index, 'offered_decimal_odds'])].iloc[0]
        self.assertEqual(row.reconciled_group, 'missing_evidence')
        self.assertEqual(row.reconciled_decision, 'MISSING_EVIDENCE')
        self.assertTrue(pd.isna(row.disagreement))
        self.assertTrue(pd.notna(row.cagey_no_loss_probability))  # the other view is still shown
        summary = mr.summary(frame)
        self.assertEqual(summary['offers_by_group']['missing_evidence'], 1)
        self.assertEqual(summary['disagreement_flags'], int(frame.disagreement.eq(True).sum()))
        unsynced = self.decisions.copy()
        unsynced.loc[index, 'cagey_input_timing_status'] = 'UNAVAILABLE_OR_UNSYNCHRONIZED'
        frame = mr.reconcile(unsynced)
        self.assertEqual(int(frame.reconciled_group.eq('missing_evidence').sum()), 1)

    def test_a_missing_espn_match_is_not_missing_evidence(self):
        flagged = self.decisions.copy()
        flagged['research_warnings'] = 'free-source fixture identity missing or ambiguous'
        frame = mr.reconcile(flagged)
        self.assertFalse(frame.reconciled_group.eq('missing_evidence').any())

    def test_european_rows_are_marked_and_kept_out_of_both_agree(self):
        europe = self.decisions.assign(league='UEFA Champions League')
        frame = mr.reconcile(europe)
        self.assertTrue(frame.unvalidated_view.all())
        would = frame.reconciled_group.eq('both_agree')
        self.assertTrue(would.any())
        self.assertTrue(frame.loc[would, 'reconciled_section'].eq('european_unvalidated').all())
        self.assertTrue(frame.loc[would, 'reconciled_decision'].eq('EUROPEAN_UNVALIDATED').all())
        self.assertFalse(frame.reconciled_section.eq('both_agree').any())
        self.assertEqual(mr.summary(frame)['european_rows'], len(frame))
        self.assertFalse(self.frame.unvalidated_view.any())

    def test_the_reconciliation_is_a_pure_function_of_the_run(self):
        again = mr.reconcile(self.decisions.copy())
        self.assertEqual(again.to_csv(index=False), self.frame.to_csv(index=False))
        shuffled = mr.reconcile(self.decisions.sample(frac=1, random_state=3))
        ranked = lambda f: f.loc[f.reconciled_rank.notna()].to_csv(index=False)
        self.assertEqual(ranked(shuffled), ranked(self.frame))


class LiveMasterUnchangedTest(unittest.TestCase):
    """master_shortlist.csv, its audit and the run summary are byte-identical with the shadow on."""

    def run_refresh(self, shadow=True):
        predictions, decisions, summary = production_run()
        before = decisions.to_csv(index=False)
        out = Path(tempfile.mkdtemp())
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
        self.assertTrue((with_shadow / CONFIG['file']).exists())
        self.assertTrue((with_shadow / CONFIG['summary_file']).exists())
        self.assertFalse((without / CONFIG['file']).exists())

    def test_overlap_reads_the_live_list_without_changing_the_reconciliation(self):
        out, _ = self.run_refresh(True)
        reconciled = pd.read_csv(out / CONFIG['file'])
        live = pd.read_csv(out / master_shortlist.FILE)
        _, decisions, _ = production_run()
        alone = mr.reconcile(decisions)
        drop = ['in_live_master', 'live_master_rank', 'live_master_same_offer']
        pd.testing.assert_frame_equal(reconciled.drop(columns=drop),
                                      pd.read_csv(io.StringIO(alone.to_csv(index=False))).drop(columns=drop))
        self.assertEqual(int(reconciled.in_live_master.sum()) > 0, len(live) > 0)

    def test_a_shadow_failure_never_touches_the_live_run(self):
        predictions, decisions, summary = production_run()
        out = Path(tempfile.mkdtemp())
        with mock.patch.object(mr, 'write_shadow', side_effect=RuntimeError('boom')):
            with self.assertWarns(UserWarning):
                frame = master_shortlist.refresh(decisions, out, summary, predictions)
        self.assertGreater(len(frame), 0)
        self.assertTrue((out / master_shortlist.FILE).exists())
        self.assertFalse((out / CONFIG['file']).exists())
        clean, _ = self.run_refresh(False)
        self.assertEqual((out / master_shortlist.FILE).read_bytes(), (clean / master_shortlist.FILE).read_bytes())

    def test_other_policies_remove_any_seeded_shadow(self):
        out = Path(tempfile.mkdtemp())
        for name in (CONFIG['file'], CONFIG['summary_file']):
            (out / name).write_text('stale', encoding='utf-8')
        master_shortlist.refresh(pd.DataFrame(), out, {'selection_policy_version': 'other'})
        self.assertFalse((out / CONFIG['file']).exists())
        self.assertFalse((out / CONFIG['summary_file']).exists())


class BacktestTest(unittest.TestCase):
    """--mode master: picks never read results, every week stands alone, and the holdout is never read."""

    @staticmethod
    def fixture(margin=1, week='2023-W10', key='EPL|2023-03-11|A|B', research_shift=0.6, cagey_shift=0.35):
        def grid(shift):
            margins = list(range(-5, 6))
            probs = np.exp(-0.5 * ((np.array(margins) - shift) / 1.6) ** 2)
            return [margins, (probs / probs.sum()).tolist()]
        return {'phase': 'development', 'week': week, 'league': 'EPL', 'fixture_key': key, 'market_book': 'pinnacle',
                'date': '2023-03-11', 'home_team': key.split('|')[2], 'away_team': key.split('|')[3],
                'margin': margin, 'hda': [1.8, 3.8, 4.6], 'ah': [-0.5, 1.82, 2.08],
                'C': grid(research_shift), 'D': grid(cagey_shift), 'M': grid(0.3)}

    def test_picks_never_read_the_result(self):
        import evaluation_harness as eh
        drop = ['return']
        rows = [pd.DataFrame(eh.master_select_week(eh.master_fixture(self.fixture(margin=m), CONFIG), CONFIG))
                for m in (-3, 0, 1, 4)]
        for other in rows[1:]:
            pd.testing.assert_frame_equal(rows[0].drop(columns=drop), other.drop(columns=drop))
        self.assertNotEqual(list(rows[0]['return']), list(rows[-1]['return']))

    def test_both_views_on_every_pooled_offer_and_groups_by_definition(self):
        import evaluation_harness as eh
        rows = eh.master_fixture(self.fixture(), CONFIG)
        self.assertTrue(rows)
        for row in rows:
            self.assertTrue(row['in_value_shortlist'] or row['in_cagey_tier'])
            self.assertIsNotNone(row['research_expected_return'])
            self.assertIsNotNone(row['cagey_no_loss_probability'])
            self.assertEqual(row['reconciled_group'], independent_group(
                row['research_expected_return'], row['cagey_no_loss_probability'], row['offered_decimal_odds'],
                row['cagey_fair_odds']))

    def test_each_week_stands_alone(self):
        import evaluation_harness as eh
        week = [self.fixture(), self.fixture(margin=0, key='EPL|2023-03-12|C|D')]
        later = [self.fixture(margin=-2, week='2023-W11', key=f'EPL|2023-03-18|E{i}|F{i}', research_shift=2.0,
                              cagey_shift=1.2)
                 for i in range(20)]
        alone, _ = eh.master_frame(week)
        mixed, _ = eh.master_frame(week + later)
        first = mixed.loc[mixed.week.eq('2023-W10')].reset_index(drop=True)
        pd.testing.assert_frame_equal(alone.astype(object).where(alone.notna(), None),
                                      first[alone.columns].astype(object).where(first[alone.columns].notna(), None))
        second = mixed.loc[mixed.week.eq('2023-W11')]
        self.assertEqual(int(second.reconciled_decision.eq('SHORTLISTED').sum()), 15)  # target per week
        self.assertEqual(int(second.reconciled_decision.eq('BEYOND_TARGET').sum()), 5)
        self.assertEqual(int(second.live_master_rank.max()), 15)

    def test_the_backtest_is_locked(self):
        import evaluation_harness as eh
        with self.assertRaises(ValueError):
            eh.evaluate_league('EPL', '.football_cache', {}, True, master_rows=[])
        with mock.patch.object(eh, 'evaluate_league', lambda *a, **k: k['master_rows'].append({'phase': 'holdout'})):
            with self.assertRaises(ValueError):
                eh.master_league('Eredivisie', '.football_cache', {})
        with self.assertRaises(ValueError):
            eh.main(['--mode', 'master', '--output', tempfile.mkdtemp(), '--declaration', 'x.json'])

    def test_research_and_cagey_inputs_are_walk_forward(self):
        """Real cache, two 14-day folds (4 and 18 Mar 2024): results changed from a date on never move the C, D
        or M input of a match whose fold starts on or before that date; later folds may learn from them."""
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

        cache = str(REPO / '.football_cache')
        base = eh.master_league('EPL', cache, cfg)
        self.assertGreater(len(base), 15)
        self.assertEqual({r['phase'] for r in base}, {'development'})
        for start, frozen in (('2024-03-04', lambda r: pd.Timestamp(r['date']) < second_fold),
                              ('2024-03-18', lambda r: True)):
            with mock.patch.object(eh.hb, 'load_history', flipped_from(start)):
                changed = eh.master_league('EPL', cache, cfg)
            self.assertEqual([r['fixture_key'] for r in base], [r['fixture_key'] for r in changed])
            moved = [r for r in changed if pd.Timestamp(r['date']) >= pd.Timestamp(start)]
            self.assertTrue(moved)
            self.assertTrue(all(a['margin'] != b['margin'] for a, b in zip(base, changed)
                                if pd.Timestamp(a['date']) >= pd.Timestamp(start)))
            for a, b in zip(base, changed):
                self.assertEqual((a['hda'], a['ah']), (b['hda'], b['ah']))
                if frozen(a):
                    for cand in eh.MASTER_CANDIDATES:
                        self.assertEqual(a[cand], b[cand], (start, a['fixture_key'], cand))


if __name__ == '__main__':
    unittest.main()
