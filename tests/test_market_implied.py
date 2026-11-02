"""Market-implied fair distribution: fit accuracy, pricing, fail-closed rules and the calibration report."""

from offline_test_case import OfflineQuotePolicyTestCase
import json
import math
import shutil
import tempfile
import unittest
from pathlib import Path

import numpy as np
import pandas as pd

import market_implied as mi
import market_implied_calibration as cal
from ah_close_backtest import settle


def market_prices(lam_home, lam_away, rho, ah_line, margin=1.0):
    """Exact fair prices implied by a known matrix, optionally with a proportional margin."""
    matrix = mi.dixon_coles_matrix(lam_home, lam_away, rho)
    inputs = mi.model_inputs(matrix, ah_line)
    h2h = tuple(1 / (inputs[k] * margin) for k in ('home', 'draw', 'away'))
    ou = (1 / (inputs['over_2_5'] * margin), 1 / ((1 - inputs['over_2_5']) * margin))
    ah = (ah_line, 1 / (inputs['ah_main'] * margin), 1 / ((1 - inputs['ah_main']) * margin))
    return h2h, ou, ah


class FitTests(OfflineQuotePolicyTestCase):
    def test_fit_a_reproduces_1x2_and_over_under(self):
        for h2h, ou in (((2.10, 3.40, 3.60), (1.95, 1.95)), ((1.30, 5.50, 10.0), (1.60, 2.40)),
                        ((3.10, 3.00, 2.45), (2.30, 1.65))):
            targets = mi.targets_from_prices(h2h, ou)
            result = mi.fit(targets, include_ah=False)
            self.assertTrue(result.usable, result.reasons)
            self.assertLess(result.max_residual, 1e-6)
            inputs = mi.model_inputs(result.matrix, None)
            for key in mi.INPUTS_A:
                self.assertAlmostEqual(inputs[key], targets[key], places=6)

    def test_fit_b_reproduces_1x2_over_under_and_ah_from_a_consistent_market(self):
        for lam_home, lam_away, rho, line in ((1.6, 1.1, -0.08, -0.25), (1.2, 1.25, 0.05, 0.0),
                                              (2.4, 0.7, -0.12, -1.5), (1.0, 1.7, -0.02, 0.75)):
            h2h, ou, ah = market_prices(lam_home, lam_away, rho, line, margin=1.03)
            targets = mi.targets_from_prices(h2h, ou, ah)
            result = mi.fit(targets, include_ah=True)
            self.assertTrue(result.usable, result.reasons)
            self.assertLess(result.max_residual, 1e-4)
            self.assertEqual(set(result.residuals), set(mi.INPUTS_B))
            self.assertAlmostEqual(result.lam_home, lam_home, places=2)
            self.assertAlmostEqual(result.lam_away, lam_away, places=2)
            self.assertAlmostEqual(result.rho, rho, places=2)

    def test_inconsistent_ah_input_is_unusable_and_reports_residuals(self):
        targets = mi.targets_from_prices((2.60, 3.20, 2.80), (2.00, 1.90), (-0.25, 1.40, 3.00))
        result = mi.fit(targets, include_ah=True)
        self.assertFalse(result.usable)
        self.assertGreater(result.max_residual, mi.MAX_RESIDUAL)
        self.assertTrue(any(r.startswith('residual') for r in result.reasons))
        with self.assertRaises(ValueError):
            mi.price(result, 'home', 1.0)

    def test_stale_or_missing_inputs_fail_closed(self):
        targets = mi.targets_from_prices((2.10, 3.40, 3.60), (1.95, 1.95), (-0.25, 1.98, 1.92))
        stale = mi.fit(targets, include_ah=True, stale=['over_2_5'])
        self.assertFalse(stale.usable)
        self.assertIn('stale input: over_2_5', stale.reasons)
        missing = mi.fit(mi.targets_from_prices((2.10, 3.40, 3.60), (1.95, 1.95)), include_ah=True)
        self.assertFalse(missing.usable)
        self.assertIn('missing input: ah_main', missing.reasons)
        self.assertIsNone(missing.matrix)
        record = missing.record()
        self.assertFalse(record['fit_usable'])
        self.assertIsNone(record['fit_max_residual'])

    def test_invalid_low_score_correction_raises(self):
        with self.assertRaises(ValueError):
            mi.dixon_coles_matrix(3.0, 3.0, 0.3)


class PricingTests(OfflineQuotePolicyTestCase):
    def setUp(self):
        super().setUp()
        self.result = mi.fit(mi.targets_from_prices((2.10, 3.40, 3.60), (1.95, 1.95)), include_ah=False)
        self.margins, self.probs = mi.margin_distribution(self.result.matrix)

    def test_opposite_sides_of_one_line_are_complementary(self):
        for line in (0.5, 1.0, 1.25, 1.5, 1.75, 2.0, 2.25, 0.0):
            home = mi.price(self.result, 'home', line)['win_share']
            away = mi.price(self.result, 'away', -line)['win_share']
            self.assertAlmostEqual(home + away, 1.0, places=12)

    def test_half_lines_equal_1x2_probabilities(self):
        inputs = mi.model_inputs(self.result.matrix, None)
        self.assertAlmostEqual(mi.price(self.result, 'home', -0.5)['win_share'], inputs['home'], places=12)
        self.assertAlmostEqual(mi.price(self.result, 'home', 0.5)['win_share'], 1 - inputs['away'], places=12)
        self.assertAlmostEqual(mi.price(self.result, 'away', -0.5)['win_share'], inputs['away'], places=12)

    def test_whole_line_excludes_refunds_and_quarter_line_is_exact(self):
        whole = mi.price(self.result, 'home', 0.0)
        inputs = mi.model_inputs(self.result.matrix, None)
        self.assertAlmostEqual(whole['win_share'], inputs['home'] / (inputs['home'] + inputs['away']), places=12)
        self.assertAlmostEqual(whole['p_push'], inputs['draw'], places=12)
        self.assertAlmostEqual(whole['p_no_loss'], inputs['home'] + inputs['draw'], places=12)
        quarter = mi.price(self.result, 'away', 1.75)
        won, lost = settle(-self.margins, 1.75)
        w, lo = (self.probs * won).sum(), (self.probs * lost).sum()
        self.assertAlmostEqual(quarter['win_share'], w / (w + lo), places=12)
        self.assertAlmostEqual(quarter['fair_odds'], (w + lo) / w, places=10)
        # Expected return at the fair price is zero on every line.
        self.assertAlmostEqual(w * (quarter['fair_odds'] - 1) - lo, 0.0, places=12)

    def test_unknown_side_rejected(self):
        with self.assertRaises(ValueError):
            mi.price(self.result, 'draw', 0.5)


def csv_row(**overrides):
    base = {'Date': pd.Timestamp('2023-11-04'), 'Division': 'E0', 'Season': '2324', 'HomeTeam': 'H',
            'AwayTeam': 'A', 'FTHG': 1, 'FTAG': 1, 'PSCH': 2.40, 'PSCD': 3.30, 'PSCA': 3.10,
            'PC>2.5': 2.05, 'PC<2.5': 1.85, 'AHCh': -0.25, 'PCAHH': 2.08, 'PCAHA': 1.84}
    base.update(overrides)
    return pd.Series(base)


class CalibrationTests(OfflineQuotePolicyTestCase):
    def test_drop_reasons(self):
        self.assertIsNone(cal.drop_reason(csv_row()))
        self.assertEqual(cal.drop_reason(csv_row(PSCD=None)), 'missing_close_prices')
        self.assertEqual(cal.drop_reason(csv_row(AHCh=0.3)), 'missing_close_prices')
        self.assertEqual(cal.drop_reason(csv_row(PCAHH=1.5, PCAHA=1.5)), 'close_overround')

    def test_match_rows_cover_every_line_both_sides_and_both_fits(self):
        rows = cal.match_rows(csv_row())
        self.assertEqual(len(rows), 2 * 2 * len(cal.LINES))
        draw = [r for r in rows if r['fit'] == 'A' and r['side'] == 'home' and r['line'] == 0.5][0]
        self.assertGreater(draw['ret'], 0)  # 1-1 wins home +0.5
        self.assertEqual(draw['period'], 'to_2023')
        self.assertEqual({r['side_role'] for r in rows if r['side'] == 'home'}, {'favourite'})
        later = cal.match_rows(csv_row(Date=pd.Timestamp('2024-01-01')))
        self.assertEqual(later[0]['period'], 'from_2024')

    def test_unusable_fit_yields_one_marker_row(self):
        rows = cal.match_rows(csv_row(PCAHH=1.40, PCAHA=3.00))
        self.assertEqual(len(rows), 1)
        self.assertIsNone(rows[0]['fit'])
        self.assertFalse(rows[0]['B_usable'])

    def test_slice_boundaries(self):
        frame = pd.DataFrame({'home_odds': [2.00, 3.50, 1.99, 2.80], 'away_odds': [3.50, 2.00, 2.50, 2.81],
                              'p_over_2_5': [0.4499, 0.45, 0.55, 0.5501], 'p_draw': [0.27, 0.2699, 0.30, 0.24],
                              'side_role': ['favourite'] * 4, 'side': ['home'] * 4, 'league': ['E0'] * 4})
        masks = cal.slices(frame)
        self.assertEqual(list(masks['balanced [2.00,3.50]']), [True, True, False, True])
        self.assertEqual(list(masks['balanced [2.00,2.80]']), [False, False, False, False])
        self.assertEqual(list(masks['total<45%']), [True, False, False, False])
        self.assertEqual(list(masks['total 45-55%']), [False, True, True, False])
        self.assertEqual(list(masks['draw 27-30%']), [True, False, False, False])
        self.assertEqual(list(masks['draw>=30%']), [False, False, True, False])
        self.assertEqual(list(masks['draw 24-27%']), [False, True, False, True])

    def test_persistent_requires_both_halves(self):
        results = pd.DataFrame([
            {'fit': 'B', 'slice': 's', 'line': 1.0, 'period': 'to_2023', 'low95': 0.01, 'tested': True},
            {'fit': 'B', 'slice': 's', 'line': 1.0, 'period': 'from_2024', 'low95': 0.02, 'tested': True},
            {'fit': 'B', 'slice': 't', 'line': 1.0, 'period': 'to_2023', 'low95': 0.01, 'tested': True},
            {'fit': 'B', 'slice': 't', 'line': 1.0, 'period': 'from_2024', 'low95': -0.01, 'tested': True}])
        both = cal.persistent(results, 'B')
        self.assertEqual(both[['slice', 'line']].values.tolist(), [['s', 1.0]])
        self.assertTrue(cal.persistent(results, 'A').empty)

    def test_main_writes_report_and_summary(self):
        source = Path(__file__).resolve().parents[1] / '.football_cache' / '2324_E0.csv'
        with tempfile.TemporaryDirectory() as tmp:
            cache, out = Path(tmp) / 'cache', Path(tmp) / 'out'
            cache.mkdir()
            shutil.copy(source, cache / source.name)
            self.assertEqual(cal.main(['--cache-dir', str(cache), '--output-dir', str(out), '--divisions', 'E0',
                                       '--workers', '1', '--bootstrap', '20']), 0)
            summary = json.loads((out / 'summary.json').read_text(encoding='utf-8'))
            report = (out / 'report.md').read_text(encoding='utf-8')
        coverage = summary['coverage']
        self.assertEqual(coverage['matches'], 380)
        self.assertGreater(coverage['both_usable'], 300)
        counts = summary['headline']['counts']
        self.assertEqual(set(counts), {'A', 'B'})
        self.assertAlmostEqual(counts['A']['expected_by_chance'], 0.05 * counts['A']['tested'], places=1)
        self.assertIn('Does fit B remove the plus-line underpricing', report)
        self.assertIn('## balanced x total<45%', report)
        self.assertTrue(all(math.isfinite(r['mean_return']) for r in summary['results']))


if __name__ == '__main__':
    unittest.main()
