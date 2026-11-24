"""C9 (C8 plus the development walk-forward slope) and the forward holdout (docs/plan.md, Phase 2g-4).

Nothing here reads a result of a match played after 10 Oct 2026: C9 is exercised on made-up research rows, the
forward period on made-up files and on a forward start moved into 2024 on real EPL history.
"""
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import numpy as np
import pandas as pd

import evaluation_harness as eh
import research_low_score as rls
import research_rate_calibration as rrc
import research_sharpen as rs
from scripts import c9_forward_outcome as outcome
from scripts import forward_holdout_count as fhc
from tests import epl_research_rows as epl

REPO = Path(__file__).resolve().parents[1]
CFG = json.loads((REPO / 'evaluation_harness_config.json').read_text(encoding='utf-8'))
V3 = 'slopes-0.90-1.10-or-closer-than-baseline-bands-30-5pp-bonferroni-v3'


def rows(n=2400, seed=3, start='2024-01-01', hours=12):
    """Research rows spanning the development end (1 Jul 2025), with an Elo effect C8 can learn."""
    rng = np.random.default_rng(seed)
    out = []
    for i in range(n):
        rates = [float(rng.uniform(.7, 2.4)), float(rng.uniform(.5, 2.))]
        z = float(rng.normal(.1, .3))
        date = pd.Timestamp(start) + pd.Timedelta(hours=hours * i)
        out.append(epl.research_row('EPL', date, rates, rng.poisson(rates[0] * np.exp(.4 * z)),
                                    rng.poisson(rates[1] * np.exp(-.4 * z)), base_rates=rates, elo_z=z,
                                    phase=eh.phase(date, 'EPL', CFG)))
    return out


def end_of(research):
    return research[-1]['date'] + pd.Timedelta(days=1)


class C9Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.enterClassContext(patch.object(rls, 'MIN_MATCHES', 400))
        cls.enterClassContext(patch.object(rrc, 'MIN_MATCHES', 400))
        cls.enterClassContext(patch.object(rs, 'MIN_MATCHES', 300))
        cls.rows = rows()
        cls.end = end_of(cls.rows)
        cls.cfg = {**CFG, 'end_exclusive': cls.end.date().isoformat()}
        cls.c8 = eh.rate_calibration_candidate(cls.rows, cls.cfg, cls.end, 'C8')
        cls.c9 = eh.rate_calibration_slope_candidate(cls.rows, cls.cfg, cls.end)

    def test_registered_walk_forward_and_reads_development_only(self):
        self.assertIn('C9', eh.CANDIDATES)
        self.assertIn('C9', eh.WALK_FORWARD_CANDIDATES)
        self.assertEqual(eh.SLOPE_FIT_END, 'development_end')
        self.assertEqual(CFG[eh.SLOPE_FIT_END], '2025-07-01')

    def test_a_neutral_slope_is_c8_exactly(self):
        with patch.object(rs, 'MIN_MATCHES', 10 ** 9):
            records, calib, _, fits = eh.rate_calibration_slope_candidate(self.rows, self.cfg, self.end)
        self.assertTrue(all(f['slope'] == 1. and f['status'] == 'warm_up' for f in fits))
        strip = lambda rs_: [{k: v for k, v in r.items() if k != 'candidate'} for r in rs_]
        self.assertEqual(strip(records), strip(self.c8[0]))
        self.assertEqual([r['probs'] for r in calib], [r['probs'] for r in self.c8[1]])

    def test_the_slope_moves_in_development_and_is_fixed_after_it(self):
        fits = self.c9[3]
        end = pd.Timestamp(CFG['development_end'])
        during = [f for f in fits if pd.Timestamp(f['origin']) < end and f['status'] == 'fitted']
        after = [f for f in fits if pd.Timestamp(f['origin']) >= end]
        self.assertGreater(len({round(f['slope'], 6) for f in during}), 1)
        self.assertTrue(after)
        self.assertTrue(all(f['slope_rows_last_date'] < CFG['development_end'] for f in fits if f['slope_rows_last_date']))
        self.assertLess(max(f['slope'] for f in after) - min(f['slope'] for f in after), 1e-5)
        self.assertNotEqual(after[0]['slope'], 1.)

    def test_no_result_after_the_development_end_reaches_the_slope(self):
        end = pd.Timestamp(CFG['development_end'])
        changed = [{**r, 'home_goals': r['away_goals'], 'away_goals': r['home_goals']} if r['date'] >= end else r
                   for r in self.rows]
        _, _, windows = eh.rate_calibration_slope_walk_forward(changed, self.cfg, self.end)
        _, _, original = eh.rate_calibration_slope_walk_forward(self.rows, self.cfg, self.end)
        self.assertEqual([w['slope'] for w in windows], [w['slope'] for w in original])

    def test_a_development_result_moves_later_slopes(self):
        end = pd.Timestamp(CFG['development_end'])
        changed = [{**r, 'home_goals': r['away_goals'], 'away_goals': r['home_goals']}
                   if end - pd.Timedelta(days=120) <= r['date'] < end else r for r in self.rows]
        _, _, windows = eh.rate_calibration_slope_walk_forward(changed, self.cfg, self.end)
        _, _, original = eh.rate_calibration_slope_walk_forward(self.rows, self.cfg, self.end)
        late = [(a['slope'], b['slope']) for a, b in zip(windows, original) if a['origin'] >= end and a['slope']]
        self.assertTrue(late and all(a['slope'] != b['slope'] for a, b in late))

    def test_a_result_on_or_after_the_origin_never_changes_a_forecast(self):
        origin = pd.Timestamp('2025-09-01')
        changed = [{**r, 'home_goals': 7., 'away_goals': 0.} if r['date'] >= origin else r for r in self.rows]
        early = lambda calib: {r['fixture_key']: r['probs'] for r in calib}
        before = early(self.c9[1])
        after = early(eh.rate_calibration_slope_candidate(changed, self.cfg, self.end)[1])
        keys = [r['identity']['fixture_key'] for r in self.rows if r['date'] < origin]
        self.assertTrue(keys)
        self.assertEqual({k: after[k] for k in keys if k in after}, {k: before[k] for k in keys if k in before})

    def test_c9_holds_c8s_draw_and_sharpens_the_split(self):
        c8 = {r['fixture_key']: r['probs'] for r in self.c8[1]}
        slope = self.c9[3][-1]['slope']
        for r in self.c9[1][-50:]:
            p8 = c8[r['fixture_key']]
            self.assertAlmostEqual(r['probs'][1], p8[1], places=9)
            share8, share9 = p8[0] / (p8[0] + p8[2]), r['probs'][0] / (r['probs'][0] + r['probs'][2])
            logit = lambda s: np.log(s / (1 - s))
            self.assertAlmostEqual(logit(share9), slope * logit(share8), places=6)

    def test_keep_without_c9_computes_nothing(self):
        self.assertEqual(eh.rate_calibration_slope_candidate(self.rows, self.cfg, self.end, keep={'C6', 'M'}),
                         ([], [], eh.Counter(), []))


class ForwardPeriodTest(unittest.TestCase):
    def forward_cfg(self, end='2026-12-01'):
        return {**CFG, eh.FORWARD_RUN: CFG['forward_holdout'], 'end_exclusive': end}

    def test_the_config_names_the_settled_terms(self):
        forward = CFG['forward_holdout']
        self.assertEqual(forward['start'], '2026-10-11')
        self.assertEqual(forward['start'], CFG['holdout_end_exclusive'])
        self.assertEqual(sorted(forward['leagues']), sorted(CFG['leagues']))
        self.assertEqual(len(forward['leagues']), 8)
        self.assertEqual(forward['book'], 'bet365')
        self.assertEqual(forward['ledger'], 'evaluation/forward_holdout_ledger.json')
        self.assertNotEqual(eh.forward_ledger(CFG), eh.LEDGER)
        self.assertEqual(eh.promotion_minimums(), {'fixtures': 300, 'weeks': 6})

    def test_a_plain_run_labels_exactly_as_before(self):
        self.assertNotIn(eh.FORWARD_RUN, CFG)
        cases = {('2026-10-20', 'EPL'): 'retrospective', ('2026-10-20', 'Eredivisie'): 'retrospective',
                 ('2026-05-01', 'Eredivisie'): 'holdout', ('2026-05-01', 'EPL'): 'retrospective',
                 ('2025-09-01', 'EPL'): 'validation', ('2024-09-01', 'EPL'): 'development'}
        for (date, league), expected in cases.items():
            self.assertEqual(eh.phase(date, league, CFG), expected, (date, league))

    def test_a_forward_run_scores_the_eight_leagues_from_11_october_only(self):
        cfg = self.forward_cfg()
        for league in CFG['leagues']:
            self.assertEqual(eh.phase('2026-10-11', league, cfg), 'holdout')
            self.assertEqual(eh.phase('2026-10-10', league, cfg), 'retrospective')
        self.assertEqual(eh.phase('2026-05-01', 'Eredivisie', cfg), 'retrospective')  # the spent holdout
        self.assertEqual(eh.phase('2025-09-01', 'EPL', cfg), 'validation')
        self.assertEqual(eh.phase('2024-09-01', 'EPL', cfg), 'development')
        self.assertEqual(eh.period_book('2026-10-20', cfg), 'bet365')

    def test_fold_windows_are_unchanged_up_to_the_forward_start(self):
        plain = eh.fold_windows(CFG, pd.Timestamp('2026-12-01'))
        forward = eh.fold_windows(self.forward_cfg(), pd.Timestamp('2026-12-01'))
        self.assertEqual(plain, forward)
        self.assertIn(pd.Timestamp('2026-10-11'), {a for a, _ in forward})

    def test_forward_end_reads_dates_only(self):
        with tempfile.TemporaryDirectory() as tmp:
            cfg = {**CFG, 'seasons': ['2627']}
            for league in CFG['leagues']:
                day = '22/11/2026' if league == 'SerieA' else '2026-11-09'
                (Path(tmp) / f"2627_{eh.hb.CODES[league]}.csv").write_text(
                    f'Date,HomeTeam,AwayTeam\n01/10/2026,A,B\n{day},C,D\n', encoding='utf-8')
            self.assertEqual(eh.forward_end(cfg, tmp), pd.Timestamp('2026-11-23'))
            run = eh.forward_run_config(cfg, tmp)
        self.assertEqual(run['end_exclusive'], '2026-11-23')
        self.assertEqual(run[eh.FORWARD_RUN], CFG['forward_holdout'])
        self.assertEqual(run['holdout_end_exclusive'], CFG['holdout_end_exclusive'])

    def test_count_reads_no_result_column(self):
        header = 'Div,Date,HomeTeam,AwayTeam,B365H,B365D,B365A,B365>2.5,B365<2.5,AHh,B365AHH,B365AHA\n'
        good = ',2.0,3.4,3.9,1.9,1.95,-0.25,1.95,1.95\n'
        with tempfile.TemporaryDirectory() as tmp:
            cfg = {**CFG, 'seasons': ['2627']}
            for league in CFG['leagues']:
                lines = [header, f'X,05/10/2026,A,B{good}', f'X,18/10/2026,C,D{good}', f'X,26/10/2026,E,F{good}',
                         'X,26/10/2026,G,H,,,,,,,,\n']
                (Path(tmp) / f"2627_{eh.hb.CODES[league]}.csv").write_text(''.join(lines), encoding='utf-8')
            out = fhc.count(cfg, tmp)
        self.assertEqual(out['priced_fixtures'], 16)  # two per league from 11 Oct; the 5 Oct match is before it
        self.assertEqual(out['unpriced_fixtures'], 8)
        self.assertEqual(out['weeks'], 2)
        self.assertFalse(out['sample_minimum_met'])
        self.assertFalse(set(fhc.price_columns()) & set(fhc.RESULT_COLUMNS))

    def test_a_forward_declaration_goes_to_its_own_ledger_only(self):
        declaration = {'candidate': 'C9', 'baseline': 'C6', 'primary_metric': 'AH all',
                       'draw_sensitive_lines': [-.5, 0., .5], 'calibration_tolerance': V3,
                       'declared_by': 'test', 'declared_at': '2026-11-24T00:00:00Z',
                       'holdout_period': CFG['forward_holdout']['name']}
        with tempfile.TemporaryDirectory() as tmp:
            path, ledger = Path(tmp) / 'd.json', Path(tmp) / 'forward.json'
            path.write_text(json.dumps(declaration), encoding='utf-8')
            self.assertEqual(eh.declared_period(path), CFG['forward_holdout']['name'])
            declared = eh.validate_declaration(path, CFG, {'sha256': 'a' * 64}, ledger)
            eh.record_holdout(declared, {'sha256': 'a' * 64}, 'abc', 400, {'passes_holdout_gate': False}, ledger)
            entry = json.loads(ledger.read_text(encoding='utf-8'))[0]
            self.assertEqual((entry['candidate'], entry['holdout_period']), ('C9', CFG['forward_holdout']['name']))
            with self.assertRaisesRegex(ValueError, "already scored for candidate 'C9'"):
                eh.validate_declaration(path, CFG, {'sha256': 'b' * 64}, ledger)
            path.write_text(json.dumps({**declaration, 'holdout_period': 'something-else'}), encoding='utf-8')
            with self.assertRaisesRegex(ValueError, 'not the configured forward holdout'):
                eh.validate_declaration(path, CFG, {'sha256': 'a' * 64}, Path(tmp) / 'other.json')
        self.assertFalse(any(e['candidate'] == 'C9' for e in json.loads(eh.LEDGER.read_text(encoding='utf-8'))))


class ForwardRunPlumbingTest(unittest.TestCase):
    """evaluate_league in a forward run, with the forward start moved to 1 Mar 2024 on real EPL history: only
    priced forward matches are scored; an unpriced one feeds the walk-forward fits and is not scored."""

    def test_only_priced_forward_matches_are_scored(self):
        data = epl.data()
        start, end = pd.Timestamp('2024-03-01'), pd.Timestamp('2024-03-29')
        blank = data.loc[data.Date >= start].index[0]
        frame = data.copy()
        frame.loc[blank, ['B365H', 'B365D', 'B365A']] = np.nan
        forward = {**CFG['forward_holdout'], 'start': start.date().isoformat()}
        cfg = {**CFG, 'seasons': ['2122', '2223', '2324'], 'test_start': '2024-02-02',
               'holdout_start': '2024-02-16', 'holdout_end_exclusive': start.date().isoformat(),
               'end_exclusive': end.date().isoformat(), eh.FORWARD_RUN: forward}
        with patch.object(eh.hb, 'load_history', return_value=(frame, [], {})):
            records, _, coverage, _, _, calib, research = eh.evaluate_league('EPL', 'unused', cfg, True,
                                                                             {'C9', 'C6', 'M'})
        scored = {r['fixture_key'] for r in records if r['phase'] == 'holdout'}
        expected = {eh.fixture_key('EPL', r) for _, r in data.loc[(data.Date >= start) & (data.Date < end)].iterrows()}
        unpriced = eh.fixture_key('EPL', frame.loc[blank])
        self.assertEqual(scored, expected - {unpriced})
        self.assertTrue(all(r['candidate'] in eh.GAP_CANDIDATES for r in records if r['phase'] != 'holdout'))
        # C9 and C6 are built from the research rows after the league pass; the pass itself scores M only.
        self.assertEqual({r['candidate'] for r in records if r['phase'] == 'holdout'}, {'M'})
        self.assertEqual(coverage['EPL:forward_unpriced'], 1)
        fed = [r for r in research if r['fixture_key'] == unpriced]
        self.assertEqual([(r['scored'], r['identity']['phase']) for r in fed], [(False, 'forward_unpriced')])
        self.assertTrue(all(r['scored'] for r in research if r['fixture_key'] in scored))


class OutcomeTest(unittest.TestCase):
    @staticmethod
    def verdict(all_gain=.003, draw_gain=.004, clear=False, calibrated=True, enough=True):
        paired = lambda gain, is_clear: None if gain is None else {
            'fixtures': 400, 'weeks': 7, 'mean_gain': gain, 'clear_of_zero': is_clear,
            'interval_95': [gain - .001, gain + .001] if is_clear else [gain - .004, gain + .004]}
        return {'candidate': 'C9', 'baseline': 'C6', 'primary_metric': 'AH all', 'primary': paired(all_gain, clear),
                'draw_sensitive': paired(draw_gain, False), 'sample_minimum_met': enough,
                'calibration': {'passes': calibrated}}

    def test_the_three_outcomes_in_c8s_order(self):
        read = lambda **k: outcome.declared_outcome(self.verdict(**k))['outcome']
        self.assertEqual(read(clear=True), 'proven')
        self.assertEqual(read(), 'release_with_guardrails')
        self.assertEqual(read(calibrated=False, clear=True), 'no_release')
        self.assertEqual(read(enough=False, clear=True), 'no_release')
        self.assertEqual(read(draw_gain=-.001, clear=True), 'no_release')  # a negative estimate beats "proven"
        self.assertEqual(read(all_gain=0.), 'no_release')  # exactly zero is not positive
        self.assertEqual(read(draw_gain=None), 'no_release')  # missing is not positive
        self.assertEqual(outcome.OUTCOMES, ('proven', 'release_with_guardrails', 'no_release'))

    def test_refuses_another_verdict(self):
        with self.assertRaises(ValueError):
            outcome.declared_outcome({**self.verdict(), 'candidate': 'C8'})


class CommittedDeclarationTest(unittest.TestCase):
    """The committed declaration: the settled terms, validated against an empty forward ledger; the real forward
    ledger now refuses it (C9 scored once on 24 Nov 2026); the 16 Jan - 10 Oct ledger never records C9."""
    PATH = REPO / 'evaluation' / 'declarations' / 'c9_forward_holdout.json'

    def test_the_settled_terms(self):
        data = json.loads(self.PATH.read_text(encoding='utf-8'))
        self.assertEqual((data['candidate'], data['baseline'], data['market_reference']), ('C9', 'C6', 'M'))
        self.assertEqual(data['holdout_period'], CFG['forward_holdout']['name'])
        self.assertEqual(data['primary_metric'], 'AH all')
        self.assertEqual(data['calibration_tolerance'], V3)
        self.assertEqual({k: data['sample_minimum'][k] for k in ('fixtures', 'weeks')}, eh.promotion_minimums())
        self.assertNotIn('deciding_criterion', data)
        self.assertEqual(tuple(data['outcomes']), outcome.OUTCOMES)

    def test_validates_once_and_only_in_its_own_ledger(self):
        with tempfile.TemporaryDirectory() as tmp:
            declared = eh.validate_declaration(self.PATH, CFG, {'sha256': 'a' * 64}, Path(tmp) / 'empty.json')
        self.assertEqual(declared['sha256'], '208bcdc27817dcca938f0aca3b9bdf4279134b882959a0f984c94ee222985ad1')
        with self.assertRaisesRegex(ValueError, "already scored for candidate 'C9'"):
            eh.validate_declaration(self.PATH, CFG, {'sha256': 'b' * 64}, eh.forward_ledger(CFG))
        entries = json.loads(eh.forward_ledger(CFG).read_text(encoding='utf-8'))
        self.assertEqual([(e['candidate'], e['holdout_period'], e['holdout_fixtures']) for e in entries],
                         [('C9', CFG['forward_holdout']['name'], 401)])
        self.assertNotIn('C9', {e['candidate'] for e in json.loads(eh.LEDGER.read_text(encoding='utf-8'))})


if __name__ == '__main__':
    unittest.main()
