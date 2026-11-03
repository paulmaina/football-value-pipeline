"""Narrow-margin report: probabilities, split of the narrow class, quote ages and output files."""

from offline_test_case import OfflineQuotePolicyTestCase
import tempfile
import unittest
from pathlib import Path

import pandas as pd

import narrow_margin_report as report

RUN = '2026-11-03T13:58:00+00:00'


def monitoring_rows():
    base = {'generated_at_utc': RUN, 'model_version': 'cagey-correction-through-2425-v1'}
    return pd.DataFrame([
        {**base, 'league': 'UEFA Champions League', 'home_team': 'A', 'away_team': 'B', 'status': 'USABLE',
         'exclusion_reason': None, 'kickoff_utc': '2026-11-03T20:00:00+00:00',
         'latest_input_quote_utc': '2026-11-03T13:58:00+00:00', 'corrected_p2': 0.36, 'corrected_p3': 0.14,
         'uncorrected_p2': 0.40, 'corrected_cagey_quintile': 'Q3'},
        {**base, 'league': 'Serie A', 'home_team': 'C', 'away_team': 'D', 'status': 'USABLE',
         'exclusion_reason': None, 'kickoff_utc': '2026-11-04T20:00:00+00:00',
         'latest_input_quote_utc': '2026-11-03T12:58:00+00:00', 'corrected_p2': 0.30, 'corrected_p3': 0.10,
         'uncorrected_p2': 0.32, 'corrected_cagey_quintile': 'Q2'},
        {**base, 'league': 'Premier League', 'home_team': 'E', 'away_team': 'F', 'status': 'UNUSABLE',
         'exclusion_reason': 'no usable market-implied fit (missing input: over_2_5)',
         'kickoff_utc': '2026-11-06T20:00:00+00:00', 'latest_input_quote_utc': None, 'corrected_p2': None,
         'corrected_p3': None, 'uncorrected_p2': None, 'corrected_cagey_quintile': None}])


def prediction_rows():
    return pd.DataFrame([
        {'league': 'UEFA Champions League', 'home_team': 'A', 'away_team': 'B', 'market_reference_home_odds': 2.0,
         'market_reference_draw_odds': 4.0, 'market_reference_away_odds': 4.0,
         'market_reference_over_2_5_odds': 1.9, 'market_reference_under_2_5_odds': 1.9},
        {'league': 'Serie A', 'home_team': 'C', 'away_team': 'D', 'market_reference_home_odds': 3.0,
         'market_reference_draw_odds': 3.0, 'market_reference_away_odds': 3.0,
         'market_reference_over_2_5_odds': 2.1, 'market_reference_under_2_5_odds': 1.75},
        {'league': 'Premier League', 'home_team': 'E', 'away_team': 'F'}])


class NarrowMarginReportTests(OfflineQuotePolicyTestCase):
    def run_report(self, monitoring=None):
        directory = Path(tempfile.mkdtemp())
        raw, readable = directory / 'raw', directory / 'readable'
        raw.mkdir()
        (monitoring if monitoring is not None else monitoring_rows()).to_csv(raw / report.MONITORING, index=False)
        prediction_rows().to_csv(raw / report.PREDICTIONS, index=False)
        return report.write(raw, readable), readable

    def test_narrow_is_one_minus_corrected_two_plus_and_splits_exactly(self):
        frame, _ = self.run_report()
        a = frame[frame.home_team == 'A'].iloc[0]
        self.assertAlmostEqual(a.p_narrow, 0.64)
        # No-vig draw 0.25 of a 0.60 uncorrected narrow class, rescaled to 0.64.
        self.assertAlmostEqual(a.p_draw, 0.25 * 0.64 / 0.60)
        self.assertAlmostEqual(a.p_draw + a.p_one_goal + a.p_two_plus, 1.0)
        self.assertLessEqual(a.p_three_plus, a.p_two_plus)

    def test_sorted_by_narrow_then_unscored_last(self):
        frame, _ = self.run_report()
        self.assertEqual(list(frame.home_team), ['C', 'A', 'E'])
        self.assertTrue(frame.iloc[-1:].p_narrow.isna().all())

    def test_quote_ages_use_run_and_kickoff_not_wall_clock(self):
        frame, _ = self.run_report()
        c = frame[frame.home_team == 'C'].iloc[0]
        self.assertEqual(c.quote_age_at_run_min, 60)
        self.assertEqual(c.quote_age_at_kickoff_min, 31 * 60 + 2)

    def test_out_of_domain_flags_competitions_outside_training(self):
        frame, _ = self.run_report()
        flags = dict(zip(frame.home_team, frame.out_of_domain))
        self.assertEqual(flags, {'A': True, 'C': False, 'E': False})

    def test_writes_csv_and_markdown_to_readable(self):
        frame, readable = self.run_report()
        self.assertEqual(len(pd.read_csv(readable / report.CSV_NAME)), 3)
        text = (readable / report.MD_NAME).read_text(encoding='utf-8')
        self.assertIn('| Serie A | C v D |', text)
        self.assertIn('## Not scored (1)', text)
        self.assertIn('missing input: over_2_5', text)

    def test_empty_monitoring_writes_empty_report(self):
        empty = monitoring_rows().iloc[0:0]
        frame, readable = self.run_report(empty)
        self.assertTrue(frame.empty)
        self.assertIn('No fixture had a usable Pinnacle fit', (readable / report.MD_NAME).read_text(encoding='utf-8'))


if __name__ == '__main__':
    unittest.main()
