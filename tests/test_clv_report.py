import json
import math
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd

import clv_report

KICK = '2026-10-18T16:30:00+00:00'
FIXTURE = {'league': 'La Liga', 'home_team': 'Levante', 'away_team': 'Athletic Bilbao',
           'kickoff_utc': KICK, 'odds_event_id': 'e1'}


def quote(book, selection, odds, fair=None):
    return {'bookmaker': book, 'selection': selection, 'decimal_odds': odds, 'fair_probability': fair}


def observation(observed, quotes, fixture=FIXTURE):
    return {'fixture': fixture, 'observed_at_utc': observed, 'quotes': quotes, 'payload': {}}


def decision(market, odds, bookmaker, evaluated='2026-10-17T10:00:00+00:00', **extra):
    return {'league': 'La Liga', 'home_team': 'Levante', 'away_team': 'Athletic Bilbao',
            'kickoff_utc': KICK, 'evaluated_at_utc': evaluated, 'market': market,
            'bookmaker': bookmaker, 'offered_decimal_odds': odds, 'decision': 'REJECTED', **extra}


def write_root(root, observations, decisions_by_file):
    (root / 'closing_odds' / 'observations').mkdir(parents=True)
    for i, obs in enumerate(observations):
        (root / 'closing_odds' / 'observations' / f'{i}.json').write_text(json.dumps(obs))
    (root / 'raw' / 'shortlist_history').mkdir(parents=True)
    for i, rows in enumerate(decisions_by_file):
        pd.DataFrame(rows).to_csv(root / 'raw' / 'shortlist_history' / f'conservative_decisions_{i}.csv', index=False)


CLOSE = [quote('pinnacle', 'home', 2.5, 0.38), quote('pinnacle', 'draw', 3.4, 0.28),
         quote('pinnacle', 'away', 2.9, 0.34), quote('1xbet', 'home', 2.45, 0.37),
         quote('pinnacle', 'over_2_5', 1.9, 0.5), quote('pinnacle', 'Asian Handicap Home -0.50', 2.5),
         quote('pinnacle', 'Asian Handicap Away +0.50', 1.6)]


class LabelTests(unittest.TestCase):
    def test_market_labels_and_families(self):
        cases = {'Home win': ('home', '1X2'), 'Draw': ('draw', '1X2'), 'Double Chance X2': ('draw_away', 'Double chance'),
                 'Over 1.5': ('over_1_5', 'Goal totals'), 'Under 3.5': ('under_3_5', 'Goal totals'),
                 'Both Teams to Score - Yes': ('btts_yes', 'BTTS'),
                 'Asian Handicap Away +2.00': ('Asian Handicap Away +2.00', 'Asian handicap')}
        for market, (key, family) in cases.items():
            self.assertEqual((clv_report.selection_key(market), clv_report.market_family(market)), (key, family))
        self.assertIsNone(clv_report.selection_key('Correct Score 1-0'))
        self.assertEqual(clv_report.market_family('Correct Score 1-0'), 'Other')

    def test_fair_closing_prices(self):
        fair = clv_report.fair_closing_prices(CLOSE)
        self.assertAlmostEqual(fair['draw_away'], 0.62)
        self.assertAlmostEqual(fair['home_draw'], 0.66)
        self.assertNotIn('Asian Handicap Away +1.00', fair)
        self.assertAlmostEqual(fair['Asian Handicap Home -0.50'] + fair['Asian Handicap Away +0.50'], 1.0)
        self.assertLess(fair['Asian Handicap Home -0.50'], 1 / 2.5 / (1 / 2.5 + 1 / 1.6))  # power shades the longshot
        self.assertEqual(fair['home'], 0.38)  # 1xBet never sets the fair reference


class ReportTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.root = Path(self.directory.name)

    def tearDown(self):
        self.directory.cleanup()

    def test_clv_measures_latest_entry_and_close(self):
        early = observation('2026-10-18T16:20:00+00:00', [quote('pinnacle', 'home', 2.2, 0.45)])
        late = observation('2026-10-18T16:26:00+00:00', CLOSE)
        write_root(self.root, [late, early], [
            [decision('Home win', 2.6, '1xBet', evaluated='2026-10-16T10:00:00+00:00')],
            [decision('Home win', 2.7, '1xBet', market_probability=0.36, raw_dc_probability=0.42),
             decision('Asian Handicap Home -0.50', 2.6, 'Pinnacle'),
             decision('Over 2.5', 2.0, 'Pinnacle', decision='SHORTLISTED'),
             decision('Draw', None, 'Pinnacle'),
             decision('Away win', 3.0, 'Pinnacle', evaluated='2026-10-18T17:00:00+00:00'),  # after kickoff
             decision('Correct Score 1-0', 7.0, 'Pinnacle')]])
        frame = clv_report.candidate_clv(self.root).set_index('market')
        self.assertEqual(sorted(frame.index), ['Asian Handicap Home -0.50', 'Home win', 'Over 2.5'])
        home = frame.loc['Home win']
        self.assertEqual(home['offered_decimal_odds'], 2.7)  # latest pre-kickoff evaluation
        self.assertAlmostEqual(home['clv_vs_pinnacle_fair'], 2.7 * 0.38 - 1)  # latest observation wins
        self.assertAlmostEqual(home['same_book_price_clv'], 2.7 / 2.45 - 1)
        self.assertAlmostEqual(home['model_gap'], 0.06)
        self.assertAlmostEqual(home['market_move'], 0.02)
        self.assertEqual(home['hours_bucket'], '24-48h')  # 30.5 hours before kickoff
        handicap = frame.loc['Asian Handicap Home -0.50']
        self.assertTrue(math.isnan(handicap['model_gap']))
        self.assertAlmostEqual(handicap['same_book_price_clv'], 2.6 / 2.5 - 1)
        self.assertEqual(frame.loc['Over 2.5', 'decision_group'], 'shortlisted')

    def test_report_files_summary_and_movement(self):
        moves = [(0.05, 0.02), (-0.04, -0.01), (0.03, 0.01), (-0.02, 0.01)]
        rows, observations = [], []
        for i, (gap, move) in enumerate(moves):
            fixture = {**FIXTURE, 'home_team': f'Home{i}', 'kickoff_utc': f'2026-10-1{i}T16:30:00+00:00'}
            observations.append(observation(f'2026-10-1{i}T16:26:00+00:00', [quote('pinnacle', 'home', 2.0, 0.5 + move)], fixture))
            rows.append({**decision('Home win', 2.1, 'Coolbet', evaluated=f'2026-10-1{i}T10:00:00+00:00',
                                    market_probability=0.5, raw_dc_probability=0.5 + gap),
                         'home_team': f'Home{i}', 'kickoff_utc': fixture['kickoff_utc']})
        write_root(self.root, observations, [rows])
        clock = datetime(2026, 10, 23, tzinfo=timezone.utc)
        summary = clv_report.build_report(self.root, clock=clock)
        out = self.root / clv_report.OUTPUT_DIR
        self.assertEqual((summary['candidates'], summary['fixtures'], summary['generated_at_utc']),
                         (4, 4, clock.isoformat()))
        self.assertEqual(summary['market_move_towards_model']['sign_agreement'], 0.75)
        self.assertEqual(summary['positive_cells'][0]['entry_bookmaker'], 'Coolbet')
        self.assertFalse(summary['automatic_production_change'])
        for name in ('candidates.csv', 'by_market_bookmaker.csv', 'by_hours_before_kickoff.csv', 'summary.json', 'report.md'):
            self.assertTrue((out / name).is_file(), name)
        json.loads((out / 'summary.json').read_text())
        report = (out / 'report.md').read_text(encoding='utf-8')
        self.assertIn('1X2 @ Coolbet', report)
        self.assertIn('sign agreement 75%', report)

    def test_empty_inputs_and_statistics_helpers(self):
        summary = clv_report.build_report(self.root, self.root / 'out')
        self.assertEqual(summary['status'], 'NO_CANDIDATES_WITH_PINNACLE_CLOSE')
        self.assertIn('No priced candidate', (self.root / 'out' / 'report.md').read_text(encoding='utf-8'))
        self.assertEqual(clv_report.summarize(pd.Series([], dtype=float))['n'], 0)
        single = clv_report.summarize(pd.Series([0.02]))
        self.assertEqual((single['n'], single['t_stat']), (1, None))
        stats = clv_report.summarize(pd.Series([0.01, 0.03]))
        self.assertAlmostEqual(stats['t_stat'], 0.02 / (0.01414213562 / math.sqrt(2)), places=5)
        self.assertEqual(clv_report.movement(pd.DataFrame())['correlation'], None)
        self.assertIsNone(clv_report._finite(float('nan')))
        self.assertEqual((clv_report._pct(None), clv_report._num(float('nan'))), ('—', '—'))

    def test_cli(self):
        write_root(self.root, [observation('2026-10-18T16:26:00+00:00', CLOSE)],
                   [[decision('Home win', 2.7, '1xBet')]])
        self.assertEqual(clv_report.main(['--root-dir', str(self.root), '--output-dir', str(self.root / 'cli')]), 0)
        self.assertEqual(json.loads((self.root / 'cli' / 'summary.json').read_text())['candidates'], 1)


if __name__ == '__main__':
    unittest.main()


class WorkbookSheetTests(unittest.TestCase):
    def parts(self):
        from zipfile import ZipFile
        from performance_excel import TEMPLATE
        with ZipFile(TEMPLATE) as z:
            return {n: z.read(n) for n in z.namelist()}

    def clv_sheet_text(self, parts):
        import xml.etree.ElementTree as ET
        from performance_report_layout import get_sheet
        sheet = get_sheet(parts, 'CLV')
        ns = '{http://schemas.openxmlformats.org/spreadsheetml/2006/main}'
        return ' | '.join(t.text for t in sheet.root.iter(ns + 't') if t.text)

    def test_sheet_from_report_and_placeholder(self):
        from performance_report_layout import add_clv, styles, clv_reading
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            parts = self.parts(); st = styles(parts)
            add_clv(parts, root, st)
            self.assertIn('No CLV report yet', self.clv_sheet_text(parts))
            rows = [{**decision('Home win', 2.1, 'Coolbet', evaluated=f'2026-10-1{i}T10:00:00+00:00',
                                market_probability=0.5, raw_dc_probability=0.55),
                     'home_team': f'Home{i}', 'kickoff_utc': f'2026-10-1{i}T16:30:00+00:00'} for i in range(3)]
            observations = [observation(f'2026-10-1{i}T16:26:00+00:00', [quote('pinnacle', 'home', 2.0, 0.5)],
                                        {**FIXTURE, 'home_team': f'Home{i}', 'kickoff_utc': f'2026-10-1{i}T16:30:00+00:00'})
                            for i in range(3)]
            write_root(root, observations, [rows])
            clv_report.build_report(root)
            add_clv(parts, root, st)  # replaces the placeholder sheet
            text = self.clv_sheet_text(parts)
            self.assertNotIn('No CLV report yet', text)
            for expected in ('Headline', 'Shortlisted picks', 'By market and entry bookmaker', 'Coolbet', 'Small sample'):
                self.assertIn(expected, text)
        self.assertEqual([clv_reading(n, t) for n, t in ((10, 5), (40, 2.5), (40, -3), (40, 0.5), (40, None))],
                         ['Small sample', 'Positive (t >= 2)', 'Negative (t <= -2)',
                          'Not distinguishable from zero', 'Not distinguishable from zero'])
