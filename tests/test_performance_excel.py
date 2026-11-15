"""performance_excel: the shortlist ledger checks it keeps, and its integration with the review (offline)."""
from offline_test_case import OfflineQuotePolicyTestCase
import copy
import tempfile
from pathlib import Path
import unittest
from zipfile import ZipFile

import excel_book as xb
from performance_excel import REPORT_NAME, export_existing, prepared_rows, summarize, write_workbook
from performance_tracking import report, score_shortlist
from excel_fixtures import post_release_root


def selection(key, status='WON', p=.8, odds=2.5, tier='STRICT'):
    return dict(fixture_key=key, kickoff_utc='2026-10-12T16:00:00Z',
                league='UEFA Champions League', home_team='Home', away_team='Away',
                market='Home win', selection_tier=tier, predicted_probability=p,
                offered_decimal_odds=odds, status=status, final_score='2-1',
                snapshot_commit='a'*40, snapshot_captured_utc='2026-10-11T07:00:00Z',
                match_source='football-data.org/v4', week='2026-W42',
                selection_policy_version='60h-ucl-v1', brier='', unit_profit='')


class ExcelReportTests(OfflineQuotePolicyTestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def test_ledger_win_rate_roi_and_brier_exclude_pending_and_missing_prices(self):
        rows = [selection('a'), selection('b', 'LOST', .7, 1.5),
                selection('c', 'WON', .6, None, 'PROVISIONAL'), selection('d', 'PENDING', .9, 2)]
        before = copy.deepcopy(rows)
        stats = summarize(prepared_rows(rows))
        self.assertEqual(rows, before)
        self.assertEqual(stats[:5], [4, 3, 2, 1, 1])
        self.assertAlmostEqual(stats[5], 2/3)
        self.assertEqual(stats[6], 2)  # priced settled
        self.assertAlmostEqual(stats[7], .5)
        self.assertAlmostEqual(stats[8], .25)
        self.assertAlmostEqual(stats[9], .23)

    def test_empty_and_pending_ledgers_do_not_claim_zero_win_rate(self):
        for rows in ([], [selection('a', 'UNVERIFIED_FIXTURE_OR_RESULT')]):
            stats = summarize(prepared_rows(rows))
            self.assertEqual(stats[5], 'n.a.')
            self.assertEqual(stats[8], 'n.a.')
            self.assertEqual(stats[9], 'n.a.')

    def test_duplicate_fixture_fails_instead_of_inflating_win_rate(self):
        with self.assertRaisesRegex(ValueError, 'Duplicate frozen fixture'):
            write_workbook(self.root, [selection('a'), selection('a')], [], {})

    def test_workbook_is_deterministic_and_text_is_never_a_formula(self):
        root = post_release_root(self.root)
        tracking = root / 'performance' / 'price_edge_v27' / 'master_shortlist_picks.csv'
        tracking.write_text(tracking.read_text(encoding='utf-8').replace('Arsenal', '=SUM(A1:A2)'), encoding='utf-8')
        path = write_workbook(root, [selection('a')], [], {})
        first = path.read_bytes()
        write_workbook(root, [selection('a')], [], {})
        self.assertEqual(first, path.read_bytes())
        with ZipFile(path) as z:
            sheets = b''.join(z.read(n) for n in z.namelist() if n.startswith('xl/worksheets/sheet'))
        self.assertNotIn(b'<f>', sheets)
        self.assertIn('=SUM(A1:A2) v Chelsea', xb.read_workbook(path)['cells']['Picks & Results'].values())

    def test_review_generates_one_readable_workbook_and_export_can_refresh_it(self):
        report(self.root, [selection('a')], [], {}, reviewed_at='2026-10-11T08:00:00Z')
        path = self.root / 'readable' / REPORT_NAME
        self.assertTrue(path.exists())
        self.assertEqual(len(list((self.root / 'readable').glob('*.xlsx'))), 1)
        self.assertEqual(export_existing(self.root), path)
        self.assertEqual(xb.read_workbook(path)['sheets'][0], 'Dashboard')

    def test_cli_and_the_reviews_final_rewrite_with_health(self):
        import io
        import contextlib
        import json
        from performance_excel import add_health_sheet, main
        root = post_release_root(self.root)
        self.assertIsNone(add_health_sheet(root, {}))  # nothing to rewrite before the first write
        with self.assertRaises(SystemExit), contextlib.redirect_stderr(io.StringIO()):
            main(['--root', str(root)])  # no grades yet
        report(root, [selection('a')], [], {}, reviewed_at='2026-11-26T07:30:00Z')
        with contextlib.redirect_stdout(io.StringIO()) as printed:
            self.assertEqual(main(['--root', str(root)]), 0)
        self.assertIn(REPORT_NAME, printed.getvalue())
        health = json.loads((root / 'performance' / 'pipeline_health.json').read_text(encoding='utf-8'))
        health['forecast_freshness']['generated_at_utc'] = '2026-11-25T06:00:00+00:00'
        path = add_health_sheet(root, health)
        self.assertIn('Wed 25 Nov 2026 09:00 EAT', xb.read_workbook(path)['cells']['Dashboard'].values())

    def test_shortlist_brier_uses_reported_adjusted_probability(self):
        row = selection('a', p=.95)
        row['rank_probability'] = .8
        final = dict(home_goals=2, away_goals=1, match_id=42)
        scored = score_shortlist(row, final, 'VERIFIED_FINISHED')
        self.assertAlmostEqual(scored['predicted_probability'], .8)
        self.assertAlmostEqual(scored['brier'], .04)


if __name__ == '__main__':
    unittest.main()
