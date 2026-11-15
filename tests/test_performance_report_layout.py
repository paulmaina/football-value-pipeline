"""football_performance_report.xlsx: sheets, the fresh start of master tracking, headline figures, CE3n monitoring
and the reports check, on a synthetic post-release run (tests/excel_fixtures.py)."""
from pathlib import Path
import json
import tempfile
import unittest
import warnings
from zipfile import ZipFile

from offline_test_case import OfflineQuotePolicyTestCase
import excel_book as xb
import performance_report_layout as layout
from excel_fixtures import START, post_release_root

try:
    import openpyxl
except ImportError:  # pragma: no cover - CI installs the dev requirements
    openpyxl = None

SHEETS = ['Dashboard', 'Picks & Results', 'Weekly Trends', 'Breakdowns', 'Calibration', 'CLV', 'Model Monitoring',
          'Guide']
PICKS = ['Kickoff (EAT)', 'Match', 'List', 'League', 'Bet', 'Price', 'Tier', 'Predicted no-loss', 'Chance of profit',
         'Labels and flags', 'Score', 'Result', 'Return (units)', 'CLV', 'Also on the other list']
CE3N = {'matches': 40, 'weeks': 2, 'ce3n_minus_ce_log_loss': 0.0012, 'interval_95': [-0.001, 0.003],
        'eligible': False, 'triggered': False, 'rule': 'After at least 150 UCL/UEL matches, roll back CE3n if ...'}


def table(book, sheet, header_row=4):
    cells = book['cells'][sheet]
    headers, c = [], 1
    while xb.address(header_row, c) in cells:
        headers.append(cells[xb.address(header_row, c)])
        c += 1
    rows, r = [], header_row + 1
    while cells.get(xb.address(r, 1)) not in (None, ''):
        rows.append({h: cells.get(xb.address(r, i)) for i, h in enumerate(headers, start=1)})
        r += 1
    return headers, rows


def sections(book, sheet):
    """{section title: {first column: second column}} for the Item/Value and Check/Status tables of a sheet."""
    cells, out, current = book['cells'][sheet], {}, None
    last = max(int(''.join(ch for ch in a if ch.isdigit())) for a in cells)
    for r in range(1, last + 1):
        a, b = cells.get(f'A{r}'), cells.get(f'B{r}')
        if a is not None and b is None and not cells.get(f'C{r}'):
            current = a
            out.setdefault(current, {})
        elif current is not None and a is not None:
            out[current][a] = b
    return out


class ReportCase(OfflineQuotePolicyTestCase):
    ce3n = None
    released = True
    ce3n_file = None

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = post_release_root(Path(self.tmp.name), ce3n=self.ce3n, released=self.released)
        if self.ce3n_file is not None:
            (self.root / 'performance' / layout.CE3N_FILE).write_text(json.dumps(self.ce3n_file), encoding='utf-8')
        metrics = json.loads((self.root / 'performance' / 'metrics.json').read_text(encoding='utf-8'))
        self.path = layout.write(self.root, self.root / 'readable' / layout.REPORT_NAME, metrics)
        self.book = xb.read_workbook(self.path)

    def named(self, name):
        return xb.named_value(self.book, name)


class LayoutTests(ReportCase):
    def test_sheets_in_order_and_removed_tabs_gone(self):
        self.assertEqual(self.book['sheets'], SHEETS)
        for removed in ('Experiments', 'ROI Plan', 'Capture Details', 'Run Tracking', 'Predictions',
                        'Pipeline Health', 'Selections', 'Metric Guide'):
            self.assertNotIn(removed, self.book['sheets'])

    def test_fresh_start_hides_picks_from_before_the_first_post_release_run(self):
        self.assertEqual(layout.tracking_start(self.root), xb.parse_utc(START))
        start = self.named('master_tracking_start')
        self.assertIn('Master tracking started afresh on Mon 16 Nov 2026 12:00 EAT', start)
        _, rows = table(self.book, 'Picks & Results')
        self.assertNotIn('Old FC v Before United', [r['Match'] for r in rows])
        self.assertEqual(len(rows), 6 + 3)
        for sheet in SHEETS[:-1]:
            if sheet != 'Model Monitoring':
                self.assertIn('Master tracking from Mon 16 Nov 2026 12:00 EAT', self.book['cells'][sheet]['A2'], sheet)

    def test_headline_figures_side_by_side(self):
        _, rows = table(self.book, 'Dashboard', 7)
        figures = {r['Measure']: (r['New master (live)'], r['Old master (shadow)']) for r in rows}
        self.assertEqual(figures['Picks since the start'], (6, 3))
        self.assertEqual(figures['Graded'], (5, 3))
        self.assertEqual(figures['Not graded yet'], (1, 0))
        self.assertEqual(figures['Wins (full or half)'], (2, 2))
        self.assertAlmostEqual(figures['Win rate'][0], 2 / 5)
        self.assertAlmostEqual(figures['No-loss rate (win, half win or refund)'][0], 3 / 5)
        self.assertAlmostEqual(figures['Return (units)'][0], -1.17)
        self.assertAlmostEqual(figures['Return (units)'][1], -0.45)
        self.assertAlmostEqual(figures['Return per bet'][0], -1.17 / 5)
        self.assertAlmostEqual(figures['Average odds (graded picks)'][0], (1.20 + 1.24 + 1.30 + 1.45 + 1.26) / 5)
        self.assertEqual((self.named('new_master_picks'), self.named('new_master_graded')), (6, 5))
        self.assertAlmostEqual(self.named('old_master_return'), -0.45)

    def test_return_by_tier(self):
        cells = self.book['cells']['Dashboard']
        rows = {(cells.get(f'A{r}'), cells.get(f'B{r}')): [cells.get(f'{c}{r}') for c in 'CDEFGH'] for r in range(1, 80)}
        safe = rows[('New master (live)', 'safe')]
        self.assertEqual(safe[:2], [4, 3])
        self.assertAlmostEqual(safe[4], 0.20 - 0.5 + 0.13)
        self.assertEqual(rows[('New master (live)', 'risky fill')][:2], [1, 1])
        self.assertEqual(rows[('Old master (shadow)', 'all picks (old rule has no tiers)')][:2], [3, 3])

    def test_picks_and_results_columns_results_and_reasons(self):
        headers, rows = table(self.book, 'Picks & Results')
        self.assertEqual(headers, PICKS)
        by_match = {(r['Match'], r['List']): r for r in rows}
        arsenal = by_match[('Arsenal v Chelsea', 'New master (live)')]
        self.assertEqual((arsenal['Result'], arsenal['Score'], arsenal['Also on the other list']), ('Won', '2-1', 'yes'))
        self.assertAlmostEqual(arsenal['Return (units)'], 0.2)
        utrecht = by_match[('Utrecht v NEC', 'New master (live)')]
        self.assertEqual((utrecht['Result'], utrecht['Score'], utrecht['Return (units)']),
                         ('Not graded yet', 'not graded yet', 'not graded yet'))
        self.assertEqual(by_match[('Genoa v AC Milan', 'New master (live)')]['CLV'], 'no near-kickoff quote')
        self.assertEqual(by_match[('Rennes v Lille', 'New master (live)')]['Labels and flags'],
                         'on value shortlist; on cagey tier')
        self.assertEqual(by_match[('Freiburg v Union Berlin', 'New master (live)')]['Result'], 'Refund')
        self.assertIn('research strongly disagrees', by_match[('Villarreal v Getafe', 'New master (live)')]['Labels and flags'])

    def test_weekly_trends_and_charts(self):
        _, rows = table(self.book, 'Weekly Trends')
        self.assertEqual([r['Week'] for r in rows], ['2026-W47', '2026-W48'])
        self.assertAlmostEqual(rows[-1]['New master (live): cumulative (units)'], -1.17)
        self.assertAlmostEqual(rows[-1]['Old master (shadow): cumulative (units)'], -0.45)
        with ZipFile(self.path) as z:
            charts = [n for n in z.namelist() if n.startswith('xl/charts/chart')]
        self.assertEqual(len(charts), 2)

    def test_calibration_breakdowns_and_clv(self):
        _, rows = table(self.book, 'Calibration')
        self.assertEqual(len(rows), 2 * len(layout.BANDS))
        band = next(r for r in rows if r['List'] == 'New master (live)' and r['Predicted no-loss band'] == '80%–85%')
        self.assertEqual(band['Graded picks'], 2)
        self.assertAlmostEqual(band['Actual no-loss rate'], 0.5)
        self.assertEqual(band['Reading'], 'small sample (under 30)')
        _, rows = table(self.book, 'Breakdowns')
        dims = {(r['Breakdown'], r['Group'], r['List']) for r in rows}
        for key in (('League', 'Premier League', 'New master (live)'), ('Market', 'Double chance', 'New master (live)'),
                    ('Tier', 'risky fill', 'New master (live)'),
                    ('Labels and flags', 'research strongly disagrees', 'New master (live)'),
                    ('Labels and flags', 'negative market EV nomination', 'Old master (shadow)')):
            self.assertIn(key, dims)
        cells = self.book['cells']['CLV']
        self.assertIn('No candidate CLV report yet', ' '.join(str(v) for v in cells.values()))

    def test_no_silent_blank_in_any_table(self):
        with ZipFile(self.path) as z:
            tables = [z.read(n).decode() for n in z.namelist() if n.startswith('xl/tables/')]
        import re
        for xml in tables:
            ref = re.search(r'ref="([A-Z]+)(\d+):([A-Z]+)(\d+)"', xml)
            sheet = next(s for s in self.book['sheets'] if f'T_{re.sub("[^A-Za-z0-9_]", "_", s).strip("_")}'
                         in re.search(r'name="([^"]+)"', xml).group(1))
            cells = self.book['cells'][sheet]
            left, top, right, bottom = ref.group(1), int(ref.group(2)), ref.group(3), int(ref.group(4))
            columns = [xb.column_letter(i) for i in range(1, 30)]
            for r in range(top, bottom + 1):
                for c in columns[columns.index(left):columns.index(right) + 1]:
                    self.assertNotIn(cells.get(f'{c}{r}'), (None, ''), f'{sheet}!{c}{r}')

    def test_data_health_on_the_dashboard(self):
        health = sections(self.book, 'Dashboard')['Data health (folded in from Pipeline Health)']
        self.assertEqual(health['Odds API credits left'], '17712')
        self.assertEqual(health['Last run that produced forecasts'], 'Mon 16 Nov 2026 12:00 EAT')
        self.assertEqual(health['Last forecast generated'], 'Sat 21 Nov 2026 12:00 EAT')
        self.assertEqual(health['Last report validation'], 'VERIFIED_WITH_WARNINGS')
        warnings_ = sections(self.book, 'Dashboard')['Warnings']
        self.assertEqual(warnings_.get('Last report validation'), 'UEL: example warning')

    def test_model_monitoring_without_ce3n_says_not_released_yet(self):
        monitoring = sections(self.book, 'Model Monitoring')
        self.assertEqual(monitoring['CE3n vs CE (UCL/UEL): rollback trigger']['Status'], 'not released yet')
        self.assertEqual(self.named('ce3n_status'), 'not released yet')
        checks = sections(self.book, 'Dashboard')['Rollback status']
        self.assertEqual(checks['CE3n vs CE (UCL/UEL)'], 'not released yet')
        research = monitoring['Research v5 (C6) vs v4: rollback trigger']
        self.assertEqual(research['Status'], 'Not yet eligible (needs 150 matches and 3 weeks)')
        self.assertAlmostEqual(research['v5 − v4 research log loss (AH all lines)'], -0.0021)
        master = monitoring['New master vs old master: rollback rule']
        self.assertEqual(master['Status'], 'Waiting: 150 graded matches over 3 weeks on each list')
        self.assertEqual(master['Old master graded matches / weeks'], '64 / 3')


class CE3nTests(ReportCase):
    ce3n = CE3N

    def test_ce3n_section_fills_in_from_its_figures(self):
        ce3n = sections(self.book, 'Model Monitoring')['CE3n vs CE (UCL/UEL): rollback trigger']
        self.assertEqual(ce3n['Status'], 'Not yet eligible (needs its sample)')
        self.assertEqual(ce3n['Graded matches / weeks'], '40 / 2')
        self.assertAlmostEqual(ce3n['ce3n − ce log loss'], 0.0012)
        self.assertEqual(ce3n['95% interval (weeks resampled)'], '-0.00100 to +0.00300')
        self.assertEqual(ce3n['Rule'], CE3N['rule'])
        self.assertNotIn('not released yet', json.dumps(self.book['cells']['Model Monitoring']))


class CE3nFileTests(ReportCase):
    ce3n_file = {'version': 'ce3n-monitoring-v1', 'rollback': dict(CE3N, triggered=True, eligible=True,
                                                                   matches=160, weeks=4)}

    def test_ce3n_from_its_own_file_and_a_trigger_shows_on_the_dashboard(self):
        self.assertEqual(self.named('ce3n_status'), 'ROLLBACK TRIGGERED')
        self.assertEqual(sections(self.book, 'Dashboard')['Rollback status']['CE3n vs CE (UCL/UEL)'],
                         'ROLLBACK TRIGGERED')


class NotStartedTests(ReportCase):
    released = False

    def test_before_the_first_post_release_run_nothing_is_shown_and_the_reason_is_given(self):
        self.assertIsNone(layout.tracking_start(self.root))
        self.assertIn('has not started yet', self.named('master_tracking_start'))
        self.assertEqual((self.named('new_master_picks'), self.named('old_master_picks')), (0, 0))
        self.assertEqual(self.named('new_master_return'), 'no graded picks yet')
        _, rows = table(self.book, 'Picks & Results')
        self.assertTrue(rows[0]['Kickoff (EAT)'].startswith('No picks yet: master tracking has not started'))


class ReportsCheckTests(ReportCase):
    def test_reports_check_recounts_the_dashboard_and_rejects_a_stale_workbook(self):
        import workflow_checks
        workflow_checks.report_workbook_check(self.root, self.path)
        picks = self.root / 'performance' / 'price_edge_v27' / 'master_shortlist_picks.csv'
        lines = picks.read_text(encoding='utf-8').splitlines()
        picks.write_text('\n'.join(lines + [lines[-1].replace('Utrecht', 'Ajax')]) + '\n', encoding='utf-8')
        with self.assertRaisesRegex(ValueError, 'new master picks'):
            workflow_checks.report_workbook_check(self.root, self.path)

    def test_reports_check_requires_the_layout(self):
        import workflow_checks
        book = xb.Book()
        book.sheet('Dashboard')
        book.save(self.path)
        with self.assertRaisesRegex(ValueError, 'sheets differ'):
            workflow_checks.report_workbook_check(self.root, self.path)


@unittest.skipIf(openpyxl is None, 'openpyxl is not installed')
class OpenpyxlTests(ReportCase):
    def test_reloads_cleanly_with_frozen_panes_formats_and_filters(self):
        with warnings.catch_warnings(record=True) as caught:
            warnings.simplefilter('always')
            book = openpyxl.load_workbook(self.path)
        self.assertEqual([str(w.message) for w in caught], [])
        picks = book['Picks & Results']
        self.assertEqual(picks.freeze_panes, 'C5')
        self.assertEqual(picks['F5'].number_format, '0.00')
        self.assertEqual(picks['H5'].number_format, '0.0%')
        self.assertEqual(picks['M5'].number_format, '+0.00;-0.00;0.00')
        self.assertTrue(all(len(book[s].tables) >= 1 for s in book.sheetnames))
        self.assertTrue(picks.conditional_formatting)


if __name__ == '__main__':
    unittest.main()
