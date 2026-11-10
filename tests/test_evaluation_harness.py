"""Evaluation harness: periods, bookmaker inputs, independence, pairing and the holdout lock."""
import json
from pathlib import Path
import tempfile
import unittest

import numpy as np
import pandas as pd

import evaluation_harness as eh

REPO = Path(__file__).resolve().parents[1]
CFG = json.loads((REPO / 'evaluation_harness_config.json').read_text(encoding='utf-8'))


def priced(**extra):
    row = {'PSH': 2.1, 'PSD': 3.4, 'PSA': 3.6, 'P>2.5': 1.95, 'P<2.5': 1.95, 'AHh': -0.25, 'PAHH': 1.95, 'PAHA': 1.97,
           'B365H': 2.05, 'B365D': 3.3, 'B365A': 3.5, 'B365>2.5': 1.9, 'B365<2.5': 1.9, 'B365AHH': 1.9, 'B365AHA': 1.95}
    return {**row, **extra}


class PeriodTest(unittest.TestCase):
    def test_periods_and_their_bookmaker(self):
        cases = [('2024-03-01', 'EPL', 'development', 'pinnacle'), ('2025-09-01', 'Eredivisie', 'validation', 'pinnacle'),
                 ('2026-01-15', 'SuperLig', 'validation', 'pinnacle'), ('2026-01-16', 'Eredivisie', 'holdout', 'bet365'),
                 ('2026-10-10', 'PrimeiraLiga', 'holdout', 'bet365'), ('2026-10-11', 'SuperLig', 'retrospective', 'bet365'),
                 ('2026-03-01', 'EPL', 'retrospective', 'bet365'), ('2026-10-20', 'LaLiga', 'retrospective', 'bet365')]
        for date, league, name, book in cases:
            self.assertEqual((eh.phase(date, league, CFG), eh.period_book(date, CFG)), (name, book), (date, league))

    def test_fold_windows_break_at_every_period_boundary(self):
        bounds = {b for w in eh.fold_windows(CFG, pd.Timestamp(CFG['end_exclusive'])) for b in w}
        self.assertTrue({pd.Timestamp(CFG[k]) for k in ('development_end', 'holdout_start', 'holdout_end_exclusive')} <= bounds)


class PricesTest(unittest.TestCase):
    def test_complete_prices_per_book(self):
        self.assertEqual(eh.book_prices(priced(), 'pinnacle')['hda'], (2.1, 3.4, 3.6))
        self.assertEqual(eh.book_prices(priced(), 'bet365')['ah'], (-0.25, 1.9, 1.95))

    def test_missing_or_invalid_prices_are_rejected(self):
        for bad in ({'PSH': np.nan}, {'PSH': 1.0}, {'AHh': -0.3}, {'PSH': 1.2}):
            self.assertIsNone(eh.book_prices(priced(**bad), 'pinnacle'), bad)

    def test_market_and_cagey_grids_are_normalised(self):
        import narrow_margin as nm
        prices = eh.book_prices(priced(), 'pinnacle')
        market = eh.market_matrix(prices)
        cagey = eh.cagey_matrix(market, prices, nm.production_model())
        self.assertAlmostEqual(float(market.sum()), 1, places=8)
        self.assertAlmostEqual(float(cagey.sum()), 1, places=8)
        goals = np.arange(market.shape[0])
        wide = np.abs(goals[:, None] - goals[None, :]) >= 2
        self.assertLess(cagey[wide].sum(), market[wide].sum())

    def test_synthetic_prices_add_the_margin(self):
        prices = eh.synthetic_prices([.5, .3, .2], .034)
        self.assertAlmostEqual(float((1 / prices).sum()), 1.034, places=9)
        with self.assertRaises(ValueError):
            eh.synthetic_prices([.5, 0., .5], .034)


class IndependenceTest(unittest.TestCase):
    """The research model must give identical probabilities whatever the odds say."""

    def test_research_model_ignores_every_odds_field(self):
        import historical_benchmark as hb
        from football_value_pipeline_v2_standalone import DixonColesModel
        data, _, _ = hb.load_history(REPO / '.football_cache', 'EPL',
                                     {**CFG, 'seasons': ['2223', '2324'], 'test_end_exclusive': '2024-07-01'})
        origin = pd.Timestamp('2024-03-01')
        train, row = data[data.Date < origin], data[data.Date >= origin].iloc[0]
        model = DixonColesModel(half_life_days=480., l2=.08, max_goals=10, shot_features=True,
                                bbs_statistics=False).fit(train.copy(), as_of=origin)
        base, _, _ = eh.research_matrix(row, train, origin, model)
        odds = [c for c in row.index if any(c.startswith(p) for p in ('PS', 'P>', 'P<', 'PC', 'PAH', 'B365', 'Max', 'Avg', 'BW', 'IW', 'WH', 'VC', 'AH', '1X'))]
        self.assertTrue(odds)
        changed = row.copy()
        changed[odds] = 9.99
        again, _, _ = eh.research_matrix(changed, train, origin, model)
        np.testing.assert_array_equal(base, again)


class PairedTest(unittest.TestCase):
    def test_positive_gain_means_the_candidate_is_better(self):
        scores = pd.DataFrame([
            {'fixture_key': f'f{i}', 'week': f'w{i % 4}', 'candidate': c, 'log_loss': v}
            for i in range(40) for c, v in (('C', 1.0), ('M', 0.9 + (i % 3) * .01))])
        result = eh.paired(scores, 'C', 'M')
        self.assertGreater(result['mean_gain'], 0)
        self.assertEqual((result['fixtures'], result['weeks']), (40, 4))
        self.assertTrue(result['clear_of_zero'])

    def test_unpaired_candidates_give_nothing(self):
        scores = pd.DataFrame([{'fixture_key': 'a', 'week': 'w', 'candidate': 'C', 'log_loss': 1.}])
        self.assertIsNone(eh.paired(scores, 'C', 'M'))


class HoldoutLockTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.dir = Path(self.tmp.name)
        self.ledger = self.dir / 'ledger.json'
        self.setup = {'sha256': 'a' * 64}

    def declaration(self, **extra):
        data = {'candidate': 'D', 'baseline': 'M', 'primary_metric': 'AH all',
                'draw_sensitive_lines': [-0.5, 0, 0.5], 'calibration_tolerance': 0.05,
                'declared_by': 'Paul', 'declared_at': '2026-11-10', **extra}
        path = self.dir / 'declaration.json'
        path.write_text(json.dumps(data), encoding='utf-8')
        return path

    def test_a_declaration_is_scored_once_per_candidate_and_per_setup(self):
        declared = eh.validate_declaration(self.declaration(), CFG, self.setup, self.ledger)
        eh.record_holdout(declared, self.setup, 'abc', 646, {'passes_holdout_gate': False}, self.ledger)
        with self.assertRaisesRegex(ValueError, "already scored for candidate 'D'"):
            eh.validate_declaration(self.declaration(), CFG, {'sha256': 'b' * 64}, self.ledger)
        # Same frozen setup under another candidate: refused too.
        with self.assertRaisesRegex(ValueError, 'frozen setup'):
            eh.validate_declaration(self.declaration(candidate='A'), CFG, self.setup, self.ledger)

    def test_the_declaration_must_match_registered_candidates_and_scoring(self):
        bad = [({'calibration_tolerance': None}, 'missing calibration_tolerance'),
               ({'candidate': 'research-v9'}, 'registered'), ({'candidate': 'M'}, 'registered'),
               ({'primary_metric': 'profit'}, 'Primary metric'), ({'draw_sensitive_lines': [0]}, 'Draw-sensitive'),
               ({'calibration_tolerance': 0.5}, 'between 0 and 0.2')]
        for extra, message in bad:
            with self.assertRaisesRegex(ValueError, message):
                eh.validate_declaration(self.declaration(**extra), CFG, self.setup, self.ledger)

    def test_setup_fingerprint_changes_with_code_data_or_config(self):
        cfg = {**CFG, 'leagues': ['EPL'], 'seasons': ['2526']}
        first = eh.setup_fingerprint(cfg, REPO / '.football_cache')
        self.assertEqual(first, eh.setup_fingerprint(cfg, REPO / '.football_cache'))
        self.assertNotEqual(first['sha256'], eh.setup_fingerprint({**cfg, 'step_days': 7}, REPO / '.football_cache')['sha256'])
        self.assertIn('data/2526_E0.csv', first['parts'])
        self.assertIn('evaluation_harness.py', first['parts'])

    def test_locked_runs_skip_the_holdout_and_holdout_runs_score_only_it(self):
        cfg = {**CFG, 'test_start': '2026-01-01', 'end_exclusive': '2026-02-15'}
        cache = str(REPO / '.football_cache')
        locked, _, coverage, _, _, _ = eh.evaluate_league('Eredivisie', cache, cfg, False)
        self.assertTrue(locked)
        self.assertEqual({r['phase'] for r in locked}, {'validation'})
        self.assertGreater(coverage['Eredivisie:locked_holdout'], 0)
        unlocked = eh.evaluate_league('Eredivisie', cache, cfg, True, keep={'D', 'M'})[0]
        holdout = [r for r in unlocked if r['phase'] == 'holdout']
        self.assertEqual({r['candidate'] for r in holdout}, {'D', 'M'})
        self.assertEqual({r['market_book'] for r in holdout}, {'bet365'})
        self.assertTrue({r['candidate'] for r in unlocked if r['phase'] != 'holdout'} <= {'MP', 'MB'})
        # Big-league matches after 16 Jan were already scored elsewhere: retrospective, never holdout.
        retro = eh.evaluate_league('EPL', cache, cfg, False)[0]
        self.assertIn('retrospective', {r['phase'] for r in retro})


class SummaryTest(unittest.TestCase):
    def test_headline_uses_one_common_cohort(self):
        records = []
        for i in range(6):
            for cand in ('C', 'M', 'D', 'A') if i < 4 else ('C',):
                records.append({'fixture_key': f'f{i}', 'league': 'EPL', 'week': 'w', 'phase': 'validation',
                                'candidate': cand, 'market': '1X2', 'log_loss': 1. if cand == 'C' else .9})
        cohort = eh.common_cohort(eh.fixture_scores(records))
        row = next(r for r in cohort if r['group'] == '1X2')
        self.assertEqual(row['fixtures'], 4)
        self.assertAlmostEqual(row['C'], 1.)


class LiveReplayTest(unittest.TestCase):
    def test_each_verified_match_is_scored_once_with_all_views(self):
        records, _, coverage = eh.live_replay(REPO / 'football_output_v2')
        if not records:
            self.skipTest('no graded live forecasts in this checkout')
        keys = {r['fixture_key'] for r in records}
        self.assertEqual(len(keys), coverage['matches_scored'])
        self.assertLessEqual(coverage['matches_scored'], coverage['verified_matches_graded'])
        per_fixture = pd.DataFrame(records).query("market == '1X2'").groupby(['fixture_key', 'candidate']).size()
        self.assertEqual(int(per_fixture.max()), 1)
        self.assertIn('D', {r['candidate'] for r in records})


if __name__ == '__main__':
    unittest.main()
