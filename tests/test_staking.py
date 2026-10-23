import tempfile
import unittest
from pathlib import Path

import pandas as pd

import staking
from football_value_pipeline_v2_standalone import build_parser, simulate_staking


def ah_row(**overrides):
    """Shortlisted Augsburg/Union Berlin Away +2.00 row from a real run."""
    row = {'league': 'Bundesliga', 'home_team': 'Augsburg', 'away_team': 'Union Berlin',
           'kickoff_utc': '2026-10-24T13:30:00+00:00', 'fixture_id': 'f1',
           'market': 'Asian Handicap Away +2.00', 'selection_tier': 'STRICT', 'bookmaker': '1xBet',
           'offered_decimal_odds': 1.16, 'per_stake_cost': 0.0, 'predicted_probability': 0.92035,
           'rank_probability': 0.909959, 'conservative_estimated_ev': 0.032993,
           'handicap_side': 'away', 'handicap_line': 2.0, 'p_full_win': 0.77935, 'p_half_win': 0.0,
           'p_refund': 0.141, 'p_half_loss': 0.0, 'p_full_loss': 0.07965}
    row.update(overrides)
    return row


def binary_row(**overrides):
    row = {'league': 'Premier League', 'home_team': 'A', 'away_team': 'B', 'market': 'Over 1.5',
           'selection_tier': 'STRICT', 'offered_decimal_odds': 1.5, 'predicted_probability': 0.72,
           'rank_probability': 0.70, 'handicap_side': None}
    row.update(overrides)
    return row


class KellyMathTests(unittest.TestCase):
    def test_expected_value_and_binary_kelly(self):
        self.assertAlmostEqual(staking.expected_value(0.5, 2.1), 0.05)
        # f* = (p*b - q) / b with b = 1.1
        self.assertAlmostEqual(staking.kelly_fraction(0.5, 2.1), (0.55 - 0.5) / 1.1)
        self.assertLess(staking.kelly_fraction(0.4, 2.0), 0)
        for bad in ((1.2, 2.0), (-0.1, 2.0), (0.5, 1.0), (0.5, float('nan'))):
            with self.assertRaises(ValueError):
                staking.kelly_fraction(*bad)

    def test_settlement_kelly_matches_closed_forms(self):
        binary = {'full_win': 0.5, 'full_loss': 0.5}
        self.assertAlmostEqual(staking.settlement_kelly(binary, 2.1), staking.kelly_fraction(0.5, 2.1), places=7)
        # Refunds: f* = (p_w*b - p_l) / (b*(p_w + p_l)).
        push = {'full_win': 0.45, 'refund': 0.25, 'full_loss': 0.30}
        b = 1.9
        self.assertAlmostEqual(staking.settlement_kelly(push, 2.9), (0.45 * b - 0.30) / (b * 0.75), places=7)

    def test_half_outcomes_costs_and_edge_cases(self):
        quarter = {'full_win': 0.40, 'half_win': 0.15, 'half_loss': 0.15, 'full_loss': 0.30}
        self.assertAlmostEqual(staking.settlement_ev(quarter, 2.0), 0.475 - 0.375)
        f = staking.settlement_kelly(quarter, 2.0)
        self.assertGreater(f, 0)
        # Costs reduce every outcome's return, so they cannot increase the stake.
        self.assertLess(staking.settlement_kelly(quarter, 2.0, cost=0.02), f)
        self.assertEqual(staking.settlement_kelly({'full_win': 0.3, 'full_loss': 0.7}, 2.0), 0.0)
        self.assertEqual(staking.settlement_kelly({'full_win': 0.6, 'refund': 0.4}, 2.0), 1.0)
        with self.assertRaises(ValueError):
            staking.settlement_kelly({'full_win': 0.6}, 2.0)
        with self.assertRaises(ValueError):
            staking.settlement_returns(2.0, cost=1.0)


class ConservativeBasisTests(unittest.TestCase):
    def test_asian_handicap_penalty_reproduces_shortlist_conservative_ev(self):
        row = ah_row()
        probs = staking.conservative_settlement(row)
        self.assertAlmostEqual(sum(probs.values()), 1.0)
        self.assertAlmostEqual(probs['full_loss'], 0.07965 + (0.92035 - 0.909959))
        self.assertAlmostEqual(staking.settlement_ev(probs, 1.16), row['conservative_estimated_ev'], places=5)

    def test_penalty_moves_half_wins_after_full_wins(self):
        probs = staking.conservative_settlement(ah_row(
            p_full_win=0.01, p_half_win=0.5, p_refund=0.0, p_half_loss=0.2, p_full_loss=0.29,
            predicted_probability=0.51, rank_probability=0.48))
        self.assertAlmostEqual(probs['full_win'], 0.0)
        self.assertAlmostEqual(probs['half_win'], 0.48)
        self.assertAlmostEqual(probs['full_loss'], 0.32)

    def test_binary_uses_rank_probability_then_predicted(self):
        self.assertEqual(staking.conservative_settlement(binary_row())['full_win'], 0.70)
        self.assertEqual(staking.conservative_settlement(binary_row(rank_probability=None))['full_win'], 0.72)
        with self.assertRaises(ValueError):
            staking.conservative_settlement(binary_row(rank_probability=None, predicted_probability=None))
        with self.assertRaises(ValueError):
            staking.conservative_settlement(ah_row(p_refund=None))


class RecommendationTests(unittest.TestCase):
    def test_quarter_kelly_cap_and_statuses(self):
        frame = pd.DataFrame([
            binary_row(rank_probability=0.69, offered_decimal_odds=1.5),   # f* = 0.07 -> 1.75%
            ah_row(),                                                     # capped at 2.5%
            binary_row(rank_probability=0.60, offered_decimal_odds=1.5),  # negative EV
            binary_row(selection_tier='PROVISIONAL'),
            binary_row(offered_decimal_odds=None),
        ])
        plan = staking.stake_recommendations(frame, bankroll=200, max_total_exposure=None)
        self.assertEqual(plan['staking_status'].tolist(), [
            'STAKE', 'STAKE_CAPPED', 'NO_STAKE_NON_POSITIVE_CONSERVATIVE_EV',
            'NO_STAKE_NOT_STRICT', 'NO_STAKE_INVALID_INPUT'])
        self.assertAlmostEqual(plan.at[0, 'stake_fraction'], 0.25 * (0.69 * 0.5 - 0.31) / 0.5)
        self.assertAlmostEqual(plan.at[1, 'stake_fraction'], 0.025)
        self.assertAlmostEqual(plan.at[1, 'stake_units'], 5.0)
        self.assertTrue((plan.loc[2:, 'stake_fraction'] == 0).all())
        self.assertIn('Missing odds', plan.at[4, 'staking_error'])

    def test_total_exposure_scales_every_stake_proportionally(self):
        frame = pd.DataFrame([ah_row(fixture_id=str(i)) for i in range(6)])
        plan = staking.stake_recommendations(frame, max_total_exposure=0.10)
        self.assertAlmostEqual(plan['stake_fraction'].sum(), 0.10)
        self.assertAlmostEqual(plan.at[0, 'exposure_scale'], 0.10 / 0.15)
        self.assertTrue((plan['stake_fraction'] == plan.at[0, 'stake_fraction']).all())

    def test_validation_and_empty_shortlist(self):
        empty = staking.stake_recommendations(pd.DataFrame())
        self.assertTrue(empty.empty)
        self.assertIn('stake_units', empty.columns)
        for kwargs in ({'bankroll': -1}, {'multiplier': 0}, {'max_fraction': 2},
                       {'max_total_exposure': 0}):
            with self.assertRaises(ValueError):
                staking.stake_recommendations(pd.DataFrame([ah_row()]), **kwargs)

    def test_writer_and_cli_defaults(self):
        with tempfile.TemporaryDirectory() as directory:
            path = staking.write_stake_recommendations(pd.DataFrame([ah_row()]), Path(directory), bankroll=50)
            self.assertEqual(path.name, staking.OUTPUT_FILE)
            self.assertAlmostEqual(pd.read_csv(path).at[0, 'stake_units'], 1.25)
        args = build_parser().parse_args([])
        self.assertEqual((args.stake_bankroll, args.stake_kelly_fraction, args.stake_cap,
                          args.stake_max_exposure), (100.0, 0.25, 0.025, 0.10))

    def test_backtest_staking_uses_shared_kelly(self):
        bets = pd.DataFrame({'date': ['2025-01-01'], 'model_prob': [0.5], 'odds_taken': [2.1], 'won': [True]})
        out = simulate_staking(bets, 1000.0, 'kelly', 0.25, 0.5, 0.01)
        self.assertAlmostEqual(out.at[0, 'stake'], 1000 * 0.25 * staking.kelly_fraction(0.5, 2.1))


if __name__ == '__main__':
    unittest.main()
