"""league_predictions.xlsx: list tabs first (master, old master, value, cagey), then one tab per league; display only."""
from pathlib import Path
import json
import tempfile
import unittest
import warnings
import xml.etree.ElementTree as ET
from zipfile import ZipFile

import pandas as pd

from offline_test_case import OfflineQuotePolicyTestCase
import excel_book as xb
import format_football_output as formatter
from format_football_output import WORKBOOK_NAME, main, read_shortlist_tabs, write_predictions_workbook
import predictions_workbook as pw
from test_conservative_bet_filter import fixture
from test_readable_safest_ah import MARGINS, offer

try:
    import openpyxl
except ImportError:  # pragma: no cover - CI installs the dev requirements
    openpyxl = None

LIST_TABS = ['Master shortlist', 'Old master (shadow)', 'Value shortlist', 'Cagey tier']
MASTER = ['Rank', 'Kickoff (EAT)', 'League', 'Match', 'Bet', 'Price', 'Tier', 'Cagey no-loss chance',
          'Chance of profit', 'Research no-loss chance', 'Research gap (points)', 'Labels and flags', 'Inspection note',
          'On value shortlist', 'On cagey tier']
TAIL = ['Quote time (EAT)', 'Re-check price before betting']
LISTS = ['Kickoff (EAT)', 'League', 'Match', 'Bet', 'Price', 'Chance of no loss', 'Chance of profit',
         'Expected return', 'Probability basis', 'Price check status']
LEAGUE = ['Kickoff (EAT)', 'Match', 'Research lean', 'Research lean chance', 'Cagey lean', 'Cagey lean chance',
          'Views agree', 'Research home win', 'Research draw', 'Research away win', 'Cagey home win', 'Cagey draw',
          'Cagey away win', 'Research expected goals', 'Cagey expected goals', 'Research most likely score',
          'Cagey most likely score', 'Research Over 2.5', 'Cagey Over 2.5', 'Research BTTS Yes', 'Cagey BTTS Yes',
          'On value shortlist', 'On cagey tier', 'On master', 'Best offer', 'Research no-loss', 'Cagey no-loss',
          'Gap (points)', 'Gap label', 'Cagey tier', 'Master check', 'Safest AH line (cagey)',
          'Safest AH odds (Pinnacle)', 'Safest AH cagey no-loss', 'Safest AH research no-loss', 'Benchmark home win',
          'Benchmark draw', 'Benchmark away win']
KICKOFF = '2026-11-17T19:00:00+00:00'  # 22:00 in Nairobi


def league_rows(league, count, start=0):
    rows = []
    for i in range(start, start + count):
        row = fixture(i)
        row.update({
            "league": league, "fixture_source": "The Odds API",
            "p_over_2_5": 0.55, "p_under_2_5": 0.45, "p_btts_yes": 0.52, "p_btts_no": 0.48,
            "p_over_0_5": 0.93, "p_over_3_5": 0.31, "p_under_3_5": 0.69, "p_under_4_5": 0.84,
            "p_under_1_5": 0.22, "p_home_draw": 0.89, "p_draw_away": 0.28, "p_home_away": 0.83,
            "lambda_home": 1.9, "lambda_away": 0.8, "goal_margin_distribution": MARGINS,
            "asian_handicap_offers": json.dumps([offer("home", .5, 1.40, book="Pinnacle", opposite=2.9)]),
            "totals_anchor_status": "ANCHORED_MAIN",
            "top_scorelines": json.dumps([{"score": "2-0", "p": 0.137}, {"score": "1-0", "p": 0.12}]),
        })
        rows.append(row)
    return rows


def master_files(raw: Path, kickoff: str = KICKOFF) -> None:
    """The released new master (every nominated offer) and the old master in shadow, as the pipeline writes them."""
    import master_reconciliation as mr
    import master_shortlist as ms
    base = {'kickoff_utc': kickoff, 'league': 'Premier League', 'bookmaker': 'Pinnacle',
            'offered_last_update_utc': '2026-11-16T08:55:00+00:00', 'evaluated_at_utc': '2026-11-16T09:00:00+00:00',
            'new_master_version': ms.VERSION_NEW_LIVE, 'pinnacle_no_loss_probability': 0.79}
    new = [
        dict(base, new_master_rank=1, new_master_tier='safe', new_master_decision='SHORTLISTED', home_team='Arsenal',
             away_team='Chelsea', market_to_bet='Asian Handicap Home +0.00', offered_decimal_odds=1.2,
             cagey_no_loss_probability=0.84, ranking_profit_probability=0.62, research_no_loss_probability=0.72,
             gap_points=-12.0, new_master_labels='research strongly disagrees', inspection_flag=True,
             inspection_summary='research expects a low-scoring draw', inspection_driver='form W-D-L 2-5-3',
             in_value_shortlist=False, in_cagey_tier=True, in_old_master=True, old_master_rank=1),
        dict(base, new_master_rank=2, new_master_tier='fill', new_master_decision='SHORTLISTED', home_team='Genoa',
             away_team='AC Milan', market_to_bet='Double Chance X2', offered_decimal_odds=1.3,
             cagey_no_loss_probability=None, ranking_profit_probability=0.66, research_no_loss_probability=None,
             gap_points=None, missing_evidence_reason='no research forecast', new_master_labels='unvalidated view',
             inspection_flag=False, in_value_shortlist=True, in_cagey_tier=False, in_old_master=False),
        dict(base, league='Serie A', new_master_rank=None, new_master_tier=None, new_master_decision='NOT_RANKED',
             home_team='Lazio',
             away_team='Roma', market_to_bet='Away win', offered_decimal_odds=1.95, cagey_no_loss_probability=0.51,
             ranking_profit_probability=0.51, research_no_loss_probability=0.55, gap_points=4.0,
             new_master_labels='both agree', inspection_flag=False, in_value_shortlist=True, in_cagey_tier=False),
    ]
    pd.DataFrame(new, columns=list(dict.fromkeys(mr.COLUMNS + ['old_master_rank', 'in_old_master', 'inspection_summary',
                                                               'inspection_driver']))).drop(
        columns=['in_live_master', 'live_master_rank', 'live_master_same_offer']).to_csv(raw / ms.FILE, index=False)
    old = [dict(master_rank=1, kickoff_utc=kickoff, league='Premier League', home_team='Arsenal', away_team='Chelsea',
                market_to_bet='Double Chance 1X', offered_decimal_odds=1.15, master_profit_probability=0.87,
                master_price_flag='negative market EV nomination', in_value_shortlist=True, in_cagey_tier=True,
                offered_last_update_utc='2026-11-16T08:58:00+00:00', master_offer_age_minutes=2.0),
           dict(master_rank=2, kickoff_utc=kickoff, league='Serie A', home_team='Lazio', away_team='Roma',
                market_to_bet='Away win', offered_decimal_odds=1.95, master_profit_probability=0.51,
                master_price_flag='value', in_value_shortlist=True, in_cagey_tier=False,
                offered_last_update_utc='', master_offer_age_minutes='')]
    pd.DataFrame(old).to_csv(raw / ms.OLD_FILE, index=False)
    (raw / 'conservative_bet_summary.json').write_text(json.dumps({'generated_at_utc': '2026-11-16T09:00:00+00:00'}))


def readable_lists(out: Path) -> None:
    value = pd.DataFrame({'Kickoff (UTC)': [KICKOFF], 'League': ['Premier League'], 'Home': ['Arsenal'],
                          'Away': ['Chelsea'], 'Market to bet': ['Asian Handicap Away +1.50'], 'Price': ['1.32'],
                          'Chance of no loss': ['88.6%'], 'Chance of positive return': ['88.6%'],
                          'Expected return after cost': ['+14.6%'], 'Probability basis': ['team_form_poisson_v1'],
                          'Price check status': ['PASSED'], 'Price check warning': [''],
                          'Corrected-grid no-loss lower bound': ['52.0%'], 'Corrected draw probability': ['19.8%']})
    cagey = value.assign(**{'Price check status': [''], 'Expected return after cost': ['-2.8%'],
                            'Also in value tier': ['yes']})
    value.to_csv(out / 'conservative_bet_shortlist_readable.csv', index=False, encoding='utf-8-sig')
    cagey.to_csv(out / 'cagey_tier_shortlist_readable.csv', index=False, encoding='utf-8-sig')


def table(book, sheet, header_row=4):
    """Rows of the sheet's first table as dicts (header row, then rows until column A is empty)."""
    cells = book['cells'][sheet]
    headers, c = [], 1
    while xb.address(header_row, c) in cells:
        headers.append(cells[xb.address(header_row, c)])
        c += 1
    rows, r = [], header_row + 1
    while xb.address(r, 1) in cells and cells[xb.address(r, 1)] not in (None, ''):
        rows.append({h: cells.get(xb.address(r, i)) for i, h in enumerate(headers, start=1)})
        r += 1
    return headers, rows


class WorkbookCase(OfflineQuotePolicyTestCase):
    """The formatter on EPL and LaLiga fixtures, an empty UCL file, a stale UEL CSV and both master files."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        root = Path(self.tmp.name)
        self.raw, self.readable = root / "raw", root / "readable"
        self.raw.mkdir()
        self.readable.mkdir()
        pd.DataFrame(league_rows("Premier League", 3)).to_csv(self.raw / "EPL_predictions.csv", index=False)
        pd.DataFrame(league_rows("La Liga", 2, start=10)).to_csv(self.raw / "LaLiga_predictions.csv", index=False)
        (self.raw / "UCL_predictions.csv").write_text("\n", encoding="utf-8")
        stale = pd.DataFrame(league_rows("Europa League", 1, start=20))
        formatter.readable_predictions_frame(stale, {}).to_csv(
            self.readable / "UEL_predictions_readable.csv", index=False, encoding="utf-8-sig")
        master_files(self.raw)
        self.assertEqual(main(["--root-dir", str(root)]), 0)
        self.path = self.readable / WORKBOOK_NAME
        self.book = xb.read_workbook(self.path)


class TabsAndColumnsTests(WorkbookCase):
    def test_tabs_in_order_lists_first_then_each_league_with_fixtures(self):
        self.assertEqual(self.book['sheets'], LIST_TABS + ['EPL', 'LaLiga'])
        self.assertEqual(formatter.workbook_league_tabs(self.path), ['EPL', 'LaLiga'])

    def test_master_and_old_master_columns(self):
        weak = ['Weak link', 'Weak-link reasons']  # since 24 Nov 2026 (master-strong-team-v5)
        self.assertEqual(table(self.book, 'Master shortlist')[0], MASTER + ['In old master (shadow)'] + TAIL + weak)
        self.assertEqual(table(self.book, 'Old master (shadow)')[0], MASTER + ['In new master (live)'] + TAIL + weak)

    def test_master_rows_show_tier_views_flags_inspection_overlap_and_times_in_eat(self):
        _, rows = table(self.book, 'Master shortlist')
        self.assertEqual([r['Rank'] for r in rows], [1.0, 2.0])  # ranked picks only, best first
        first, second = rows
        self.assertEqual(first['Match'], 'Arsenal v Chelsea')
        self.assertEqual(first['Tier'], 'safe')
        self.assertAlmostEqual(first['Cagey no-loss chance'], 0.84)
        self.assertAlmostEqual(first['Research gap (points)'], -12.0)
        self.assertEqual(first['Labels and flags'], 'research strongly disagrees')
        self.assertEqual(first['Inspection note'],
                         'research strongly disagrees: research expects a low-scoring draw; form W-D-L 2-5-3')
        self.assertEqual(first['In old master (shadow)'], 'yes (rank 1, other bet: Double Chance 1X)')
        self.assertEqual(first['Kickoff (EAT)'], xb.excel_time(KICKOFF))
        self.assertAlmostEqual(xb.excel_time(KICKOFF) % 1, 22 / 24, places=7)  # 19:00 UTC is 22:00 EAT
        self.assertTrue(first['Re-check price before betting'].startswith('yes: re-check at Pinnacle'))
        self.assertIn('5 min old', first['Re-check price before betting'])
        # Gaps carry a reason, never a silent blank.
        self.assertEqual(second['Cagey no-loss chance'], 'no cagey score (Pinnacle no-loss 79.0%)')
        self.assertEqual(second['Research no-loss chance'], 'no research forecast')
        self.assertEqual(second['Inspection note'], 'not flagged')
        self.assertEqual(second['In old master (shadow)'], 'no')

    def test_old_master_carries_the_new_rules_view_of_the_same_offer(self):
        _, rows = table(self.book, 'Old master (shadow)')
        arsenal, lazio = rows
        self.assertEqual(arsenal['Tier'], 'old rule: no tiers')
        self.assertEqual(arsenal['Cagey no-loss chance'], 'not nominated to the new master')
        self.assertEqual(arsenal['In new master (live)'], 'yes (rank 1, other bet: Asian Handicap Home +0.00)')
        self.assertAlmostEqual(lazio['Cagey no-loss chance'], 0.51)  # the same offer, nominated but not ranked
        self.assertAlmostEqual(lazio['Research gap (points)'], 4.0)
        self.assertEqual(lazio['Labels and flags'], 'value; both agree')
        self.assertEqual(lazio['In new master (live)'], 'no')
        self.assertEqual(lazio['Quote time (EAT)'], 'not recorded')
        self.assertEqual(lazio['Re-check price before betting'], 'yes: re-check at Pinnacle before betting')

    def test_league_tab_shows_both_views_and_the_benchmark_last(self):
        headers, rows = table(self.book, 'EPL')
        self.assertEqual(headers, LEAGUE)
        self.assertEqual(len(rows), 3)
        for dropped in ('Model lean', 'Benchmark BTTS Yes', 'Benchmark Over 0.5', 'Fixture source', 'Training status',
                        'Benchmark best EV (display only)', 'Best model-estimated value'):
            self.assertNotIn(dropped, headers)
        csv = pd.read_csv(self.readable / 'EPL_predictions_readable.csv', dtype=str, keep_default_na=False,
                          encoding='utf-8-sig')
        for kept in ('Research BTTS No', 'Cagey Under 3.5', 'Benchmark BTTS Yes'):
            self.assertIn(kept, csv.columns)  # full detail stays in the CSV
        row = rows[0]
        self.assertAlmostEqual(row['Benchmark home win'], xb.number(csv.loc[0, 'Benchmark home win']))
        self.assertEqual(row['Research home win'], xb.number(csv.loc[0, 'Research home win'])
                         if xb.number(csv.loc[0, 'Research home win']) is not None else 'no research view')
        self.assertIsInstance(row['Kickoff (EAT)'], float)

    def test_titles_name_the_run_time_in_eat_and_the_csv_with_full_columns(self):
        for sheet, csv in (('Master shortlist', 'master_shortlist_readable.csv'),
                           ('Old master (shadow)', 'master_shortlist_old.csv'),
                           ('Value shortlist', 'conservative_bet_shortlist_readable.csv'),
                           ('Cagey tier', 'cagey_tier_shortlist_readable.csv'),
                           ('EPL', 'EPL_predictions_readable.csv')):
            subtitle = self.book['cells'][sheet]['A2']
            self.assertIn('Run Mon 16 Nov 2026 12:00 EAT', subtitle, sheet)
            self.assertIn(csv, subtitle, sheet)
            self.assertTrue(self.book['cells'][sheet]['A1'], sheet)

    def test_no_silent_blank_in_any_table(self):
        with ZipFile(self.path) as archive:
            tables = [ET.fromstring(archive.read(n)) for n in archive.namelist() if n.startswith('xl/tables/')]
        self.assertEqual(len(tables), len(self.book['sheets']))  # one native table (with its filter) per tab
        for sheet in self.book['sheets']:
            headers, rows = table(self.book, sheet)
            for row in rows:
                for header in headers:
                    self.assertNotIn(row[header], (None, ''), f'{sheet}: {header}')

    def test_refresh_rewrites_list_tabs_and_keeps_league_tabs(self):
        readable_lists(self.readable)
        formatter.refresh_workbook_shortlists(self.readable, self.raw)
        book = xb.read_workbook(self.path)
        self.assertEqual(book['sheets'], LIST_TABS + ['EPL', 'LaLiga'])
        self.assertEqual(table(book, 'Value shortlist')[1][0]['Match'], 'Arsenal v Chelsea')
        self.assertEqual(table(book, 'Master shortlist')[1][0]['Match'], 'Arsenal v Chelsea')

    def test_same_inputs_give_the_same_bytes(self):
        first = self.path.read_bytes()
        formatter.refresh_workbook_shortlists(self.readable, self.raw)
        self.assertEqual(self.path.read_bytes(), first)


class ListTabTests(OfflineQuotePolicyTestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.out = Path(self.tmp.name)
        readable_lists(self.out)
        self.path = write_predictions_workbook([], self.out / WORKBOOK_NAME, read_shortlist_tabs(self.out))
        self.book = xb.read_workbook(self.path)

    def test_value_and_cagey_tabs_keep_only_the_columns_to_judge_a_bet(self):
        for sheet in ('Value shortlist', 'Cagey tier'):
            headers, rows = table(self.book, sheet)
            self.assertEqual(headers, LISTS)
            self.assertEqual(rows[0]['Match'], 'Arsenal v Chelsea')
            self.assertAlmostEqual(rows[0]['Price'], 1.32)
            self.assertAlmostEqual(rows[0]['Chance of no loss'], 0.886)
        self.assertEqual(table(self.book, 'Value shortlist')[1][0]['Price check status'], 'PASSED')
        self.assertEqual(table(self.book, 'Cagey tier')[1][0]['Price check status'], 'not checked in this run')
        self.assertAlmostEqual(table(self.book, 'Cagey tier')[1][0]['Expected return'], -0.028)

    def test_without_a_run_bundle_the_master_tabs_say_why(self):
        self.assertEqual(self.book['sheets'], LIST_TABS)
        for sheet in ('Master shortlist', 'Old master (shadow)'):
            self.assertEqual(table(self.book, sheet)[1][0]['Rank'], 'Run bundle not available to the workbook.')

    def test_a_pre_release_run_shows_its_live_old_master_and_why_the_new_tab_is_empty(self):
        import master_shortlist as ms
        raw = self.out / 'raw'
        raw.mkdir()
        pd.DataFrame([dict(master_rank=1, kickoff_utc=KICKOFF, league='Premier League', home_team='Arsenal',
                           away_team='Chelsea', market_to_bet='Home win', offered_decimal_odds=1.6,
                           master_profit_probability=0.6, in_value_shortlist=True, in_cagey_tier=False)]).to_csv(
            raw / ms.FILE, index=False)
        book = xb.read_workbook(write_predictions_workbook([], self.out / 'pre.xlsx', None, raw))
        self.assertEqual(table(book, 'Master shortlist')[1][0]['Rank'],
                         'No new-master file in this run (made before the release).')
        old = table(book, 'Old master (shadow)')[1][0]
        self.assertEqual(old['Match'], 'Arsenal v Chelsea')
        self.assertEqual(old['Cagey no-loss chance'], 'no new-master view in this run')
        self.assertIn('the old master was the live list', book['cells']['Old master (shadow)']['A2'])


@unittest.skipIf(openpyxl is None, "openpyxl is not installed")
class OpenpyxlTests(WorkbookCase):
    def test_reloads_cleanly_with_formats_tables_and_frozen_panes(self):
        with warnings.catch_warnings(record=True) as caught:
            warnings.simplefilter('always')
            book = openpyxl.load_workbook(self.path)
        self.assertEqual([str(w.message) for w in caught], [])
        master = book['Master shortlist']
        self.assertEqual(master.freeze_panes, 'E5')  # header row and rank, kickoff, league, match
        self.assertEqual(master['F5'].number_format, '0.00')
        self.assertEqual(master['H5'].number_format, '0.0%')
        self.assertEqual(master['B5'].number_format, 'ddd dd mmm hh:mm')
        self.assertEqual(master['B5'].value.hour, 22)
        self.assertEqual(len(master.tables), 1)
        self.assertTrue(master.conditional_formatting)
        epl = book['EPL']
        self.assertEqual(epl.freeze_panes, 'C5')
        self.assertEqual(epl['D5'].number_format, '0.0%')  # research lean chance


if __name__ == "__main__":
    unittest.main()
