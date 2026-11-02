"""Offline tests for the read-only pre-registered AH price-edge backtest."""

from offline_test_case import OfflineQuotePolicyTestCase
import json
import math
import shutil
import tempfile
import unittest
from pathlib import Path

import pandas as pd

from price_edge_backtest import (
    BET_COLUMNS, EDGE_THRESHOLD, build_candidates, candidate, drop_reason, evaluate, export_bets,
    longest_losing_run, main, max_drawdown, net_odds, rule_metrics, select_bets, verdict, write_report)


def row(**overrides):
    """Pinnacle 2.00/2.00 open (fair 0.5 each side), 1.95/1.95 close, home -0.5 both."""
    base = {'Date': pd.Timestamp('2025-11-29'), 'Division': 'E0', 'Season': '2526',
            'HomeTeam': 'Home', 'AwayTeam': 'Away', 'FTHG': 1, 'FTAG': 0,
            'AHh': -0.5, 'AHCh': -0.5, 'PAHH': 2.0, 'PAHA': 2.0, 'PCAHH': 1.95, 'PCAHA': 1.95,
            'MaxAHH': 2.04, 'MaxAHA': 1.90, 'B365AHH': 1.95, 'B365AHA': 1.90,
            'BFEAHH': 2.10, 'BFEAHA': 1.95, 'AvgAHH': 1.92, 'AvgAHA': 1.88}
    base.update(overrides)
    return pd.Series(base)


def bets_for(source, *rows, threshold=EDGE_THRESHOLD, commission=0.05):
    frame, drops = build_candidates(pd.DataFrame(list(rows)), source, commission)
    return select_bets(frame, threshold), drops


class FilterTests(OfflineQuotePolicyTestCase):
    def test_clean_row_passes_every_source(self):
        for source in ('max', 'b365', 'bfe', 'avg'):
            self.assertIsNone(drop_reason(row(), source), source)

    def test_max_aha_22_row_from_2526_is_dropped(self):
        # Brentford v Burnley 29/11/2025: MaxAHA 22.0 against Pinnacle 1.85.
        bad = row(AHh=-1.25, AHCh=-1.0, PAHH=2.06, PAHA=1.85, PCAHH=1.83, PCAHA=2.11,
                  MaxAHH=2.03, MaxAHA=22.0, AvgAHH=1.97, AvgAHA=4.32)
        self.assertEqual(drop_reason(bad, 'max'), 'offered_overround')
        self.assertEqual(drop_reason(bad, 'avg'), 'offered_overround')
        bets, drops = bets_for('max', bad, threshold=0.0)
        self.assertTrue(bets.empty)
        self.assertEqual(drops, {'offered_overround': 1})

    def test_no_max_bet_when_pair_is_incoherent_even_with_a_huge_edge(self):
        # Overround fine (1.005) but home 2.40 > 1.15 x 2.00: the whole pair is distrusted,
        # including the away side, which on its own would not breach the cap.
        bad = row(MaxAHH=2.40, MaxAHA=1.70)
        self.assertEqual(drop_reason(bad, 'max'), 'offered_above_pinnacle_cap')
        self.assertTrue(bets_for('max', bad, threshold=0.0)[0].empty)
        self.assertIsNone(drop_reason(row(MaxAHH=2.30, MaxAHA=1.80), 'max'))  # exactly 1.15x is kept

    def test_offered_overround_floor(self):
        self.assertEqual(drop_reason(row(MaxAHH=2.10, MaxAHA=2.10), 'max'), 'offered_overround')  # 0.952
        self.assertIsNone(drop_reason(row(MaxAHH=2.04, MaxAHA=2.04), 'max'))                    # 0.980

    def test_pinnacle_close_overround_range(self):
        self.assertEqual(drop_reason(row(PCAHH=1.80, PCAHA=1.80), 'max'), 'pinnacle_close_overround')  # 1.111
        self.assertEqual(drop_reason(row(PCAHH=2.02, PCAHA=2.02), 'max'), 'pinnacle_close_overround')  # 0.990
        self.assertIsNone(drop_reason(row(PCAHH=2.0, PCAHA=2.0), 'max'))                              # 1.000

    def test_missing_prices(self):
        self.assertEqual(drop_reason(row(PAHH=float('nan')), 'max'), 'no_pinnacle_open')
        self.assertEqual(drop_reason(row(AHh=float('nan')), 'max'), 'no_pinnacle_open')
        self.assertEqual(drop_reason(row(PCAHA=None), 'max'), 'no_pinnacle_close')
        self.assertEqual(drop_reason(row(BFEAHH=float('nan')), 'bfe'), 'no_offered_price')
        no_bfe = row()
        del no_bfe['BFEAHH'], no_bfe['BFEAHA']  # pre-2425 CSVs have no BFE columns
        self.assertEqual(drop_reason(no_bfe, 'bfe'), 'no_offered_price')


class ThresholdTests(OfflineQuotePolicyTestCase):
    def test_exactly_two_percent_bets(self):
        bets, _ = bets_for('max', row(MaxAHH=2.04))
        self.assertEqual(list(bets['side']), ['home'])
        self.assertAlmostEqual(bets['edge'].iloc[0], 0.02, places=12)

    def test_exactly_two_percent_bets_despite_float_rounding(self):
        # Fair home is exactly 1.02 / 1.89 here, but the float edge is 0.0199999999999998.
        bets, _ = bets_for('max', row(PAHH=1.74, PAHA=2.04, MaxAHH=1.89, MaxAHA=2.00))
        self.assertLess(bets['edge'].iloc[0], 0.02)
        self.assertEqual(list(bets['side']), ['home'])

    def test_one_point_nine_nine_percent_does_not_bet(self):
        bets, _ = bets_for('max', row(MaxAHH=2.0398))
        self.assertTrue(bets.empty)

    def test_away_side_and_at_most_one_side(self):
        bets, _ = bets_for('max', row(MaxAHH=1.90, MaxAHA=2.06))
        self.assertEqual(list(bets['side']), ['away'])
        # Both sides at exactly 2% (overround 0.980): one bet, home on the tie.
        bets, _ = bets_for('max', row(MaxAHH=2.04, MaxAHA=2.04))
        self.assertEqual(list(bets['side']), ['home'])
        # Both clear 0%: the larger edge wins.
        bets, _ = bets_for('max', row(MaxAHH=2.01, MaxAHA=2.03), threshold=0.0)
        self.assertEqual(list(bets['side']), ['away'])


class CommissionTests(OfflineQuotePolicyTestCase):
    def test_net_odds(self):
        self.assertAlmostEqual(net_odds(2.0, 0.05), 1.95)
        self.assertAlmostEqual(net_odds(3.0, 0.02), 2.96)
        self.assertEqual(net_odds(2.0, 0.0), 2.0)

    def test_commission_applies_to_edge_and_winnings_only(self):
        # Raw 2.10 is a 5% edge; net 2.045 is 2.25%, still a bet.
        bets, _ = bets_for('bfe', row(BFEAHH=2.10))
        self.assertAlmostEqual(bets['odds'].iloc[0], 2.045)
        self.assertAlmostEqual(bets['quoted_odds'].iloc[0], 2.10)
        self.assertAlmostEqual(bets['edge'].iloc[0], 0.0225)
        self.assertAlmostEqual(bets['profit'].iloc[0], 1.045)          # 1.10 x 0.95
        lost, _ = bets_for('bfe', row(BFEAHH=2.10, FTHG=0, FTAG=0))
        self.assertAlmostEqual(lost['profit'].iloc[0], -1.0)           # no commission on a loss
        # Raw 2.08 is a 4% edge but only 1.3% after commission: no bet.
        self.assertTrue(bets_for('bfe', row(BFEAHH=2.08))[0].empty)
        # The rate is a parameter.
        self.assertFalse(bets_for('bfe', row(BFEAHH=2.08), commission=0.02)[0].empty)

    def test_commission_not_applied_to_bookmakers(self):
        bets, _ = bets_for('max', row(MaxAHH=2.10, MaxAHA=1.85), commission=0.05)
        self.assertAlmostEqual(bets['odds'].iloc[0], 2.10)

    def test_quarter_line_half_win_pays_net_half(self):
        # Away +0.25 on a draw: half won, half pushed.
        record = candidate(row(AHh=-0.25, AHCh=-0.25, FTHG=1, FTAG=1, BFEAHA=2.20), 'bfe', 0.05)
        self.assertAlmostEqual(record['away_profit'], 0.5 * 1.2 * 0.95)
        self.assertAlmostEqual(record['home_profit'], -0.5)


class ClvTests(OfflineQuotePolicyTestCase):
    def test_clv_against_fair_close_when_line_unchanged(self):
        bets, _ = bets_for('max', row(MaxAHH=2.04, PCAHH=1.90, PCAHA=2.00))
        q_close = (1 / 1.90) / (1 / 1.90 + 1 / 2.00)
        self.assertAlmostEqual(bets['clv'].iloc[0], 2.04 * q_close - 1)

    def test_clv_only_on_unchanged_lines(self):
        moved = row(MaxAHH=2.04, AHCh=-0.75)
        bets, _ = bets_for('max', moved, row(MaxAHH=2.06, HomeTeam='Other'))
        self.assertEqual(len(bets), 2)
        self.assertTrue(math.isnan(bets['clv'].iloc[0]))
        metrics = rule_metrics(bets, n_boot=50)
        self.assertEqual(metrics['same_line_bets'], 1)
        self.assertAlmostEqual(metrics['mean_clv'], bets['clv'].iloc[1])
        # The moved-line bet still settles and counts towards ROI.
        self.assertAlmostEqual(metrics['roi'], (1.04 + 1.06) / 2)

    def test_shin_check_uses_shin_on_open_and_close(self):
        record = candidate(row(PAHH=1.80, PAHA=2.10, PCAHH=1.75, PCAHA=2.20, MaxAHH=1.86), 'max')
        self.assertNotAlmostEqual(record['home_edge'], record['home_edge_shin'])
        self.assertNotAlmostEqual(record['home_clv'], record['home_clv_shin'])


class RecordTests(OfflineQuotePolicyTestCase):
    def test_drawdown_and_losing_run(self):
        self.assertEqual(max_drawdown([1, -1, -1, 0.5, -2, 3]), 3.5)
        self.assertEqual(max_drawdown([-1, -1]), 2.0)  # the start counts as a peak
        self.assertEqual(max_drawdown([1, 1]), 0.0)
        self.assertEqual(longest_losing_run([-1, -0.5, -1, 0, -1, 1, -1, -1]), 3)  # push breaks a run
        self.assertEqual(longest_losing_run([1, 0]), 0)

    def test_evaluate_and_report_smoke(self):
        rows = [row(Date=pd.Timestamp('2025-08-16') + pd.Timedelta(days=7 * i), FTHG=i % 3, FTAG=1,
                    MaxAHH=2.04 + 0.01 * (i % 2), HomeTeam=f'H{i}') for i in range(12)]
        candidates = {s: build_candidates(pd.DataFrame(rows), s)[0] for s in ('max', 'b365', 'bfe', 'avg')}
        summary = evaluate(candidates, n_boot=50)
        self.assertEqual(summary['sources']['max']['rule']['bets'], 12)
        self.assertEqual(summary['sources']['avg']['rule']['bets'], 0)
        self.assertEqual(set(summary['sources']['max']['breakdowns']),
                         {'season', 'league', 'line_type', 'odds_band', 'side_role'})
        summary.update(commission=0.05, coverage={s: {'matches': 12, 'dropped': {}, 'usable': 12}
                                                  for s in candidates})
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'report.md'
            write_report(summary, path)
            text = path.read_text(encoding='utf-8')
        self.assertIn('SENSITIVITY ONLY', text)
        self.assertIn('Live tracking', text)

    def test_no_usable_prices_still_writes_every_output(self):
        # 2026/27 CSVs carry no Pinnacle AH columns, so no source has a single candidate.
        source = Path(__file__).resolve().parents[1] / '.football_cache' / '2627_E0.csv'
        with tempfile.TemporaryDirectory() as tmp:
            cache, out = Path(tmp) / 'cache', Path(tmp) / 'out'
            cache.mkdir()
            shutil.copy(source, cache / source.name)
            self.assertEqual(main(['--cache-dir', str(cache), '--output-dir', str(out),
                                   '--divisions', 'E0', '--bootstrap', '10']), 0)
            bets = pd.read_csv(out / 'bets.csv')
            summary = json.loads((out / 'summary.json').read_text(encoding='utf-8'))
            report = (out / 'report.md').read_text(encoding='utf-8')
        self.assertTrue(bets.empty)
        self.assertEqual(list(bets.columns), list(BET_COLUMNS))
        matches = summary['coverage']['max']['matches']
        self.assertGreater(matches, 0)
        for source_name, coverage in summary['coverage'].items():
            self.assertEqual(coverage, {'matches': matches, 'dropped': {'no_pinnacle_open': matches}, 'usable': 0})
        self.assertIn('No, for none of the offered-price sources.', report)

    def test_export_columns_match_bet_columns(self):
        candidates = {s: build_candidates(pd.DataFrame([row()]), s)[0] for s in ('max', 'b365', 'bfe', 'avg')}
        bets = export_bets(candidates)
        self.assertEqual(list(bets.columns), list(BET_COLUMNS))
        self.assertEqual(list(bets['source']), ['max', 'bfe'])  # bfe 2.10 is 2.25% net of commission

    def test_verdict_does_not_call_tiny_samples(self):
        tiny = {'bets': 2, 'same_line_bets': 2, 'mean_clv': 0.03, 'clv_low95': 0.02, 'clv_high95': 0.04}
        big = {'bets': 400, 'same_line_bets': 250, 'mean_clv': 0.02, 'clv_low95': 0.01, 'clv_high95': 0.03}
        summary = {'sources': {
            'max': {'description': 'max', 'rule': big, 'shin_check': big, 'recent_season': tiny},
            'b365': {'description': 'b365', 'rule': tiny}, 'avg': {'description': 'avg', 'rule': tiny}}}
        text = '\n'.join(verdict(summary))
        self.assertIn('Yes for: max.', text)
        self.assertNotIn('WARNING', text)
        self.assertIn('too few same-line bets', text)


if __name__ == '__main__':
    unittest.main()
