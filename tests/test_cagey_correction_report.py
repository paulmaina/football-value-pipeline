"""Holdout gate for the cagey correction: gate logic, model integrity, tier simulation, tags."""

from offline_test_case import OfflineQuotePolicyTestCase
import unittest

import numpy as np
import pandas as pd

import cagey_correction_report as report
import market_implied as mi
import narrow_margin as nm


def interval(mean, low, high, n=100):
    return {'n': n, 'mean': mean, 'low95': low, 'high95': high}


class GateLogicTests(OfflineQuotePolicyTestCase):
    def passing(self):
        a = interval(0.002, 0.001, 0.004)
        b = {'corrected': interval(0.0, -0.01, 0.01), 'uncorrected': interval(0.01, 0.003, 0.02)}
        c = {'s1': interval(0.002, -0.001, 0.005), 's2': interval(0.001, 0.0001, 0.003)}
        return a, b, c

    def test_all_conditions_met_passes(self):
        self.assertTrue(report.gate(*self.passing())['pass'])

    def test_each_condition_can_fail_the_gate(self):
        a, b, c = self.passing()
        self.assertFalse(report.gate(interval(0.002, -0.0001, 0.004), b, c)['pass'])
        self.assertFalse(report.gate(a, {**b, 'corrected': interval(0.01, 0.002, 0.02)}, c)['pass'])
        self.assertFalse(report.gate(a, {**b, 'corrected': interval(-0.01, -0.02, -0.001)}, c)['pass'])
        self.assertFalse(report.gate(a, {**b, 'uncorrected': interval(-0.001, -0.01, 0.008)}, c)['pass'])
        result = report.gate(a, b, {**c, 's3': interval(-0.003, -0.006, -0.0001)})
        self.assertFalse(result['pass'])
        self.assertEqual([k for k, v in result['checks'].items() if not v], ['c_no_season_significantly_worse'])

    def test_report_states_fail_and_switch_off(self):
        a, b, c = self.passing()
        summary = {'gate': report.gate(interval(0.002, -0.0001, 0.004), b, c), 'a_log_loss_gain_2plus': a,
                   'b_returns_pooled': b, 'c_by_season': {k: {'log_loss_gain_2plus': v} for k, v in c.items()}}
        text = '\n'.join(report.gate_lines(summary))
        self.assertIn('GATE: FAIL', text)
        self.assertIn('switched OFF', text)


def dataset(n=60, start='2023-10-01'):
    rows = []
    dates = pd.date_range(start, periods=n, freq='3D')
    for i, date in enumerate(dates):
        lam_h, lam_a = 1.0 + 0.02 * (i % 20), 0.9 + 0.01 * (i % 15)
        matrix = mi.dixon_coles_matrix(lam_h, lam_a, -0.05)
        margins, probs = mi.margin_distribution(matrix)
        inputs = mi.model_inputs(matrix, None)
        margin = (i % 5) - 2
        rows.append({'match': f'E0|{date.date()}|H{i}', 'date': date, 'week': str(date.date()), 'league': 'E0',
                     'season': '2324' if date < pd.Timestamp('2024-07-01') else '2425', 'home_team': f'H{i}',
                     'away_team': 'A', 'home_odds': 1 / (inputs['home'] * 1.03), 'away_odds': 1 / (inputs['away'] * 1.03),
                     'fit': 'B', 'p_home': inputs['home'], 'p_draw': inputs['draw'], 'p_away': inputs['away'],
                     'p_over_2_5': inputs['over_2_5'], 'matrix_p2': nm.margin_tail(margins, probs, 2),
                     'matrix_p3': nm.margin_tail(margins, probs, 3), 'margin': margin, 'abs_margin': abs(margin),
                     'ah_line': 1.25 if i % 2 else -0.25, 'ah_home_close': 1.30, 'ah_away_close': 3.40, 'probs': probs,
                     'Division': 'E0', 'HomeTeam': f'H{i}', 'AwayTeam': 'A', 'FTHG': max(margin, 0), 'FTAG': max(-margin, 0)})
    frame = pd.DataFrame(rows)
    frame['Date'] = frame['date']
    return frame


class IntegrityTests(OfflineQuotePolicyTestCase):
    def setUp(self):
        super().setUp()
        self.frame = dataset()
        self.model = nm.finalise(nm.train(self.frame, version='t', until=nm.GATE_CUTOFF), self.frame, nm.GATE_CUTOFF)

    def test_model_with_post_2023_data_is_rejected(self):
        report.verify_gate_model(self.frame, self.model)
        with self.assertRaises(AssertionError):
            report.verify_gate_model(self.frame, {**self.model, 'training_last_date': '2024-01-05'})
        with self.assertRaises(AssertionError):
            report.verify_gate_model(self.frame, {**self.model, 'training_until_exclusive': '2024-06-01'})
        with self.assertRaises(AssertionError):
            report.verify_gate_model(self.frame.iloc[1:], self.model)

    def test_evaluate_runs_end_to_end_on_synthetic_data(self):
        summary = report.evaluate(self.frame, self.model, 20)
        self.assertEqual(set(summary['gate']['checks']), {'a_log_loss_gain_above_zero', 'b_corrected_interval_contains_zero',
                                                          'b_uncorrected_above_zero', 'c_no_season_significantly_worse'})
        self.assertGreater(summary['test_matches'], 0)
        self.assertTrue(pd.Timestamp(summary['test_dates'][0]) >= nm.GATE_CUTOFF)
        self.assertIn('LIMITED', summary['d_cagey_tier_simulation']['label'])
        self.assertIn('2024+ (test)', summary['e_identifier_comparison'])

    def test_tier_simulation_rules(self):
        data = report.apply_model(report.add_tags(self.frame), self.model)
        test = data[data.date >= nm.GATE_CUTOFF]
        result = report.tier_simulation(test, {**self.model, 'training_cagey_p20': 1.0}, 20)
        self.assertLessEqual(result['bets'], result['eligible_matches'])
        none = report.tier_simulation(test, {**self.model, 'training_cagey_p20': 0.0}, 20)
        self.assertEqual((none['eligible_matches'], none['bets']), (0, 0))


class TagTests(OfflineQuotePolicyTestCase):
    def test_even_odds_from_close_uses_raw_odds_boundaries(self):
        frame = pd.DataFrame({'home_odds': [2.50, 2.49, 3.00, 4.0], 'away_odds': [2.50, 3.00, 2.49, 2.6],
                              'p_over_2_5': 0.5, 'p_draw': 0.25})
        tagged = report.add_tags(frame)
        self.assertEqual(tagged.even_odds.tolist(), [True, False, False, True])
        self.assertEqual(tagged.balanced.tolist(), [True, True, True, False])

    def test_outcome_rates(self):
        frame = pd.DataFrame({'margin': [0, 1, -2, 3], 'abs_margin': [0, 1, 2, 3]})
        rates = report.outcome_rates(frame)
        self.assertEqual((rates['margin_2plus'], rates['margin_3plus']), (0.5, 0.25))
        self.assertEqual(rates['away_+2'], {'win': 0.75, 'push': 0.0, 'loss': 0.25})
        self.assertEqual(rates['home_+2'], {'win': 0.75, 'push': 0.25, 'loss': 0.0})
        self.assertEqual(rates['home_+1.5'], {'win': 0.75, 'push': 0.0, 'loss': 0.25})


if __name__ == '__main__':
    unittest.main()
