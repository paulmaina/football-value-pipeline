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
        cases = [('2024-03-01', 'development', 'pinnacle'), ('2025-09-01', 'validation', 'pinnacle'),
                 ('2026-01-15', 'validation', 'pinnacle'), ('2026-01-16', 'holdout', 'bet365')]
        for date, name, book in cases:
            self.assertEqual((eh.phase(date, CFG), eh.period_book(date, CFG)), (name, book))

    def test_fold_windows_break_at_both_period_boundaries(self):
        bounds = {b for w in eh.fold_windows(CFG, pd.Timestamp(CFG['end_exclusive'])) for b in w}
        self.assertTrue({pd.Timestamp(CFG['development_end']), pd.Timestamp(CFG['holdout_start'])} <= bounds)
        locked = eh.fold_windows(CFG, pd.Timestamp(CFG['holdout_start']))
        self.assertEqual(locked[-1][1], pd.Timestamp(CFG['holdout_start']))


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

    def declaration(self, **extra):
        data = {'candidate': 'research-draw-fix-v1', 'baseline': 'C', 'primary_metric': 'AH all log loss',
                'draw_sensitive_lines': [-0.5, 0, 0.5], 'calibration_tolerance': 0.05,
                'declared_by': 'Paul', 'declared_at': '2026-11-10', **extra}
        path = self.dir / f"{data['candidate']}.json"
        path.write_text(json.dumps(data), encoding='utf-8')
        return path

    def test_a_complete_declaration_unlocks_once(self):
        declared = eh.validate_declaration(self.declaration(), self.ledger)
        self.assertEqual(len(declared['sha256']), 64)
        eh.record_holdout(declared, 'abc', 2100, self.ledger)
        with self.assertRaisesRegex(ValueError, 'already scored'):
            eh.validate_declaration(self.declaration(), self.ledger)

    def test_incomplete_or_reused_names_are_refused(self):
        with self.assertRaisesRegex(ValueError, 'missing calibration_tolerance'):
            eh.validate_declaration(self.declaration(calibration_tolerance=None), self.ledger)
        with self.assertRaisesRegex(ValueError, 'new named candidate'):
            eh.validate_declaration(self.declaration(candidate='C'), self.ledger)

    def test_an_unlocked_run_never_scores_the_holdout(self):
        cfg = {**CFG, 'test_start': '2026-01-01', 'end_exclusive': '2026-02-15'}
        locked = eh.evaluate_league('EPL', str(REPO / '.football_cache'), cfg, False)[0]
        self.assertTrue(locked)
        self.assertEqual({r['phase'] for r in locked}, {'validation'})
        unlocked = eh.evaluate_league('EPL', str(REPO / '.football_cache'), cfg, True)[0]
        holdout = {(r['market_book']) for r in unlocked if r['phase'] == 'holdout'}
        self.assertEqual(holdout, {'bet365'})


if __name__ == '__main__':
    unittest.main()
