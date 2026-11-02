"""Offline tests for the read-only Asian handicap vs Pinnacle close backtest."""

from offline_test_case import OfflineQuotePolicyTestCase
import unittest

import numpy as np
import pandas as pd

import asian_handicap
from ah_close_backtest import (
    block_bootstrap, devig_proportional, devig_shin, effective_probability, eligible,
    expected_return, line_bucket, line_type, match_record, outcome_probabilities,
    realised_return, settle, sign_convention_check, simulated_clv, split_line, walk_forward)


def settled(margin, line):
    won, lost = settle(margin, line)
    return float(won), float(lost)


class SettlementTests(OfflineQuotePolicyTestCase):
    def test_half_lines_never_push(self):
        self.assertEqual(settled(0, -0.5), (0.0, 1.0))
        self.assertEqual(settled(1, -0.5), (1.0, 0.0))
        self.assertEqual(settled(-1, 1.5), (1.0, 0.0))
        self.assertEqual(settled(-2, 1.5), (0.0, 1.0))
        self.assertEqual(line_type(-1.5), 'half')
        self.assertEqual(line_type(0.5), 'half')

    def test_whole_lines_push_on_exact_margin(self):
        self.assertEqual(settled(0, 0), (0.0, 0.0))
        self.assertEqual(settled(1, -1), (0.0, 0.0))
        self.assertEqual(settled(2, -1), (1.0, 0.0))
        self.assertEqual(settled(-2, 2), (0.0, 0.0))
        self.assertEqual(settled(-3, 2), (0.0, 1.0))
        self.assertEqual(line_type(-2), 'whole')
        self.assertEqual(line_type(0), 'whole')

    def test_quarter_lines_split_stake_both_signs(self):
        self.assertEqual(split_line(-0.25), (-0.5, 0.0))
        self.assertEqual(split_line(0.75), (0.5, 1.0))
        self.assertEqual(settled(0, -0.25), (0.0, 0.5))   # half lost, half pushed
        self.assertEqual(settled(0, 0.25), (0.5, 0.0))    # half won, half pushed
        self.assertEqual(settled(1, -0.75), (0.5, 0.0))
        self.assertEqual(settled(2, -0.75), (1.0, 0.0))
        self.assertEqual(settled(1, -1.25), (0.0, 0.5))
        self.assertEqual(settled(2, -1.75), (0.5, 0.0))
        self.assertEqual(settled(-1, 0.75), (0.0, 0.5))
        self.assertEqual(settled(-1, 1.25), (0.5, 0.0))
        self.assertEqual(settled(4, -2.75), (1.0, 0.0))   # Man City 5-1 Luton
        self.assertEqual(settled(3, -3.25), (0.0, 0.5))   # beyond the production +/-3 range
        self.assertEqual(settled(4, -3.25), (1.0, 0.0))
        self.assertEqual(line_type(-2.75), 'quarter')

    def test_matches_production_settlement_on_every_production_line(self):
        for line in asian_handicap.LINES:
            for margin in range(-6, 7):
                self.assertEqual(settled(margin, line), asian_handicap.settlement(margin, line),
                                 (margin, line))

    def test_rejects_non_quarter_lines(self):
        for bad in (0.1, -1.3, float('nan'), float('inf')):
            with self.assertRaises(ValueError):
                split_line(bad)

    def test_realised_return_includes_half_outcomes(self):
        self.assertAlmostEqual(realised_return(0, 0.25, 2.0), 0.5)
        self.assertAlmostEqual(realised_return(0, -0.25, 2.0), -0.5)
        self.assertAlmostEqual(realised_return(1, -1, 1.9), 0.0)
        self.assertAlmostEqual(realised_return(2, -1.5, 1.9), 0.9)

    def test_outcome_probabilities_and_expected_return(self):
        margins = np.arange(-3, 4)
        probs = np.array([.05, .10, .20, .25, .20, .12, .08])
        for line in (-1.75, -1, -0.5, -0.25, 0, 0.25, 1.5, 2.75):
            out = outcome_probabilities(margins, probs, line)
            self.assertAlmostEqual(sum(out.values()), 1.0)
            expected = sum(p * realised_return(m, line, 1.95) for m, p in zip(margins, probs))
            self.assertAlmostEqual(expected_return(out, 1.95), expected)
            # Zero expected return at the effective fair price.
            self.assertAlmostEqual(expected_return(out, 1 / effective_probability(out)), 0.0)
        half = outcome_probabilities(margins, probs, -0.5)
        self.assertAlmostEqual(effective_probability(half), half['p_win'])
        self.assertAlmostEqual(half['p_win'], .20 + .12 + .08)

    def test_away_side_mirrors_home(self):
        margins = np.arange(-3, 4)
        probs = np.array([.05, .10, .20, .25, .20, .12, .08])
        home = outcome_probabilities(margins, probs, -0.75)
        away = outcome_probabilities(-margins, probs, 0.75)
        self.assertAlmostEqual(home['p_win'], away['p_loss'])
        self.assertAlmostEqual(home['p_half_win'], away['p_half_loss'])
        self.assertAlmostEqual(home['p_push'], away['p_push'])

    def test_line_buckets_cover_every_line(self):
        self.assertEqual(line_bucket(-1.5), '<= -1.25')
        self.assertEqual(line_bucket(-1.25), '<= -1.25')
        self.assertEqual(line_bucket(-1.0), '-1 to -0.25')
        self.assertEqual(line_bucket(-0.25), '-1 to -0.25')
        self.assertEqual(line_bucket(0.0), '0')
        self.assertEqual(line_bucket(1.0), '+0.25 to +1')
        self.assertEqual(line_bucket(1.25), '>= +1.25')


class MarginRemovalTests(OfflineQuotePolicyTestCase):
    def test_both_methods_sum_to_one(self):
        for home, away in ((1.95, 1.95), (1.87, 2.03), (1.40, 3.10), (1.06, 11.0), (2.0, 2.0)):
            for devig in (devig_proportional, devig_shin):
                q = devig(home, away)
                self.assertAlmostEqual(sum(q), 1.0, places=12)
                self.assertTrue(0 < q[0] < 1)

    def test_shin_equals_proportional_for_symmetric_or_marginless_books(self):
        self.assertAlmostEqual(devig_shin(1.95, 1.95)[0], 0.5)
        self.assertAlmostEqual(devig_shin(1.5, 3.0)[0], devig_proportional(1.5, 3.0)[0])

    def test_shin_moves_margin_toward_the_longshot(self):
        # Shin assigns the favourite more probability than proportional removal.
        self.assertGreater(devig_shin(1.25, 4.0)[0], devig_proportional(1.25, 4.0)[0])


def history(days=70, teams=('A', 'B', 'C', 'D')):
    rows = []
    start = pd.Timestamp('2023-01-01')
    for i in range(days):
        home, away = teams[i % len(teams)], teams[(i + 1) % len(teams)]
        rows.append({'Date': start + pd.Timedelta(days=i), 'HomeTeam': home, 'AwayTeam': away,
                     'FTHG': i % 3, 'FTAG': (i + 1) % 2})
    return pd.DataFrame(rows)


class NoLookaheadTests(OfflineQuotePolicyTestCase):
    def test_training_rows_strictly_precede_every_predicted_match(self):
        frame = history()
        score_from = pd.Timestamp('2023-01-20')
        fits = []

        def fit(train, as_of):
            fits.append((train['Date'].max(), as_of))
            return {'train': train.copy(), 'as_of': as_of}

        def predict(model, row):
            # The assertion the task requires: nothing on or after the match date.
            self.assertTrue((model['train']['Date'] < row['Date']).all())
            self.assertFalse(((model['train']['HomeTeam'] == row['HomeTeam'])
                              & (model['train']['Date'] == row['Date'])).any())
            return {'id': row['Date']}

        rows = walk_forward(frame, score_from, fit, predict, is_eligible=lambda row: True)
        self.assertEqual(len(rows), int((frame['Date'] >= score_from).sum()))
        self.assertTrue(all(r['train_max_date'] < r['match_date'] for r in rows))
        self.assertTrue(all(last < as_of for last, as_of in fits))
        self.assertTrue(all(as_of.weekday() == 1 for _, as_of in fits))  # weekly Tuesday refits
        self.assertTrue(all(pd.Timestamp(r['match_date']) >= score_from for r in rows))

    def test_warmup_rows_train_but_are_never_scored(self):
        frame = history()
        score_from = pd.Timestamp('2023-02-01')
        rows = walk_forward(frame, score_from, lambda train, as_of: train,
                            lambda model, row: {}, is_eligible=lambda row: True)
        self.assertTrue(min(r['match_date'] for r in rows) >= '2023-02-01')
        self.assertTrue(min(r['n_train'] for r in rows) >= 30)

    def test_ineligible_rows_are_skipped_but_still_train(self):
        frame = history()
        frame['ok'] = frame.index % 2 == 0
        rows = walk_forward(frame, pd.Timestamp('2023-02-01'), lambda train, as_of: len(train),
                            lambda model, row: {'n': model}, is_eligible=lambda row: bool(row['ok']))
        self.assertEqual(len(rows), int(((frame['Date'] >= '2023-02-01') & frame['ok']).sum()))


def ah_row(**overrides):
    row = {'Division': 'E0', 'Season': '2324', 'HomeTeam': 'A', 'AwayTeam': 'B', 'FTHG': 2, 'FTAG': 0,
           'AHh': -0.75, 'PAHH': 1.95, 'PAHA': 1.95, 'AHCh': -0.5, 'PCAHH': 1.90, 'PCAHA': 2.00,
           'PSH': 1.9, 'PSD': 3.5, 'PSA': 4.2}
    row.update(overrides)
    return pd.Series(row)


class RecordAndClvTests(OfflineQuotePolicyTestCase):
    distribution = {'-1': .2, '0': .3, '1': .3, '2': .2}

    def test_eligibility_requires_opening_closing_and_1x2(self):
        self.assertTrue(eligible(ah_row()))
        for column in ('AHh', 'PAHH', 'AHCh', 'PCAHA', 'PSD'):
            self.assertFalse(eligible(ah_row(**{column: float('nan')})), column)
        self.assertFalse(eligible(ah_row(AHCh=0.3)))

    def test_match_record_uses_closing_line_and_fair_close(self):
        record = match_record(ah_row(), {'dc': self.distribution})
        self.assertEqual(record['close_line_type'], 'half')
        self.assertEqual((record['home_close_won'], record['home_close_lost']), (1.0, 0.0))
        self.assertAlmostEqual(record['dc_q_home'], .5)
        q = record['pin_close_q_home']
        self.assertAlmostEqual(q, (1 / 1.9) / (1 / 1.9 + 1 / 2.0))
        self.assertAlmostEqual(record['home_return_fair_close'], 1 / q - 1)
        self.assertAlmostEqual(record['dc_er_home_fair_close'], .5 * (1 / q - 1) - .5)
        # Opening EV on the opening -0.75 line at 1.95 / away +0.75 at 1.95.
        self.assertAlmostEqual(record['dc_ev_open_home'], .2 * .95 + .3 * .95 / 2 - .3 - .2)
        self.assertAlmostEqual(record['dc_ev_open_away'], .5 * .95 - .3 / 2 - .2)

    def test_simulated_clv_only_scores_same_line_bets(self):
        frame = pd.DataFrame([
            {**match_record(ah_row(AHh=-0.5), {'dc': {'0': .1, '1': .9}}), 'refit_date': '2023-01-03'},
            {**match_record(ah_row(), {'dc': {'0': .1, '1': .9}}), 'refit_date': '2023-01-10'},
        ])
        clv = simulated_clv(frame, 'dc', n_boot=50)
        self.assertIn('SIMULATED', clv['label'])
        self.assertEqual(clv['bets'], 2)
        self.assertEqual(clv['same_line_bets'], 1)
        self.assertAlmostEqual(clv['mean_clv_vs_fair_close'], 1.95 * frame.loc[0, 'pin_close_q_home'] - 1)
        # Home bet at -0.75 that closed -0.5: the line moved away from the bet.
        self.assertEqual(clv['share_line_moved_favourable'], 0.0)


class BootstrapTests(OfflineQuotePolicyTestCase):
    def test_block_bootstrap_is_deterministic_and_brackets_mean(self):
        values = np.arange(20, dtype=float)
        blocks = np.repeat(np.arange(5), 4)
        first = block_bootstrap(values, blocks, n_boot=500)
        self.assertEqual(first, block_bootstrap(values, blocks, n_boot=500))
        self.assertAlmostEqual(first[0], values.mean())
        self.assertLess(first[1], first[0])
        self.assertGreater(first[2], first[0])

    def test_constant_blocks_give_degenerate_interval(self):
        mean, low, high = block_bootstrap(np.ones(8), np.repeat([1, 2], 4), n_boot=100)
        self.assertEqual((mean, low, high), (1.0, 1.0, 1.0))


class SignConventionTests(OfflineQuotePolicyTestCase):
    def test_home_favourite_must_have_negative_line(self):
        rows = pd.DataFrame([
            {'Season': '2324', 'Date': pd.Timestamp('2024-04-13'), 'HomeTeam': 'Man City', 'AwayTeam': 'Luton',
             'FTHG': 5, 'FTAG': 1, 'AHh': -2.5, 'AHCh': -2.75, 'PSCH': 1.08, 'PSCA': 26.0},
            {'Season': '2324', 'Date': pd.Timestamp('2023-08-27'), 'HomeTeam': 'Sheffield United',
             'AwayTeam': 'Man City', 'FTHG': 1, 'FTAG': 2, 'AHh': 2.0, 'AHCh': 1.75, 'PSCH': 16.0, 'PSCA': 1.2}])
        checks = sign_convention_check({'E0': rows})
        self.assertEqual([c['home_ah_result'] for c in checks], ['WON', 'WON'])
        flipped = rows.assign(AHCh=-rows['AHCh'])
        with self.assertRaises(ValueError):
            sign_convention_check({'E0': flipped})


if __name__ == '__main__':
    unittest.main()
