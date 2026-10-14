"""Verify native Excel report calculations, integrity and integration offline."""
import copy
import tempfile
from pathlib import Path
import unittest
import xml.etree.ElementTree as ET
from zipfile import ZipFile

from performance_excel import NS, CHART, REPORT_NAME, write_workbook, export_existing
from performance_tracking import score_shortlist, report


def selection(key, status='WON', p=.8, odds=2.5, tier='STRICT'):
    return dict(fixture_key=key, kickoff_utc='2026-10-12T16:00:00Z',
                league='UEFA Champions League', home_team='Home', away_team='Away',
                market='Home win', selection_tier=tier, predicted_probability=p,
                offered_decimal_odds=odds, status=status, final_score='2-1',
                snapshot_commit='a'*40, snapshot_captured_utc='2026-10-11T07:00:00Z',
                match_source='football-data.org/v4', week='2026-W42',
                selection_policy_version='60h-ucl-v1', brier='', unit_profit='')


def cell(path, sheet, address):
    with ZipFile(path) as z:
        xml=ET.fromstring(z.read(f'xl/worksheets/sheet{sheet}.xml'))
        c=xml.find(f'.//{{{NS}}}c[@r="{address}"]')
        if c is None:return None
        v=c.find(f'{{{NS}}}v')
        if v is None:
            text=c.find(f'{{{NS}}}is/{{{NS}}}t')
            return text.text if text is not None else None
        return v.text if c.get('t')=='str' else float(v.text)


class ExcelReportTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.addCleanup(self.temp.cleanup)
        self.root=Path(self.temp.name)

    def test_win_rate_roi_and_brier_exclude_pending_and_missing_prices(self):
        rows=[selection('a'),selection('b','LOST',.7,1.5),
              selection('c','WON',.6,None,'PROVISIONAL'),selection('d','PENDING',.9,2)]
        before=copy.deepcopy(rows)
        path=write_workbook(self.root,rows,[],{})
        self.assertEqual(rows,before)
        self.assertEqual(cell(path,1,'B7'),4)
        self.assertEqual(cell(path,1,'B8'),3)
        self.assertEqual(cell(path,1,'B9'),2)
        self.assertEqual(cell(path,1,'B11'),1)
        self.assertAlmostEqual(cell(path,1,'B12'),2/3)
        self.assertAlmostEqual(cell(path,1,'B13'),.25)
        self.assertAlmostEqual(cell(path,1,'B14'),.5)
        self.assertAlmostEqual(cell(path,1,'B15'),.23)
        self.assertAlmostEqual(cell(path,2,'G13'),100.5)
        self.assertIsNone(cell(path,5,'M8'))
        self.assertIsNone(cell(path,5,'L9'))
        self.assertLess(cell(path,1,'B18'),2/3)
        self.assertGreater(cell(path,1,'B19'),2/3)

    def test_empty_and_pending_reports_do_not_claim_zero_win_rate(self):
        for rows in ([],[selection('a','UNVERIFIED_FIXTURE_OR_RESULT')]):
            path=write_workbook(self.root,rows,[],{})
            self.assertEqual(cell(path,1,'B12'),'n.a.')
            self.assertEqual(cell(path,1,'B13'),'n.a.')
            self.assertEqual(cell(path,1,'B15'),'n.a.')
            self.assertEqual(cell(path,1,'D11'),'Awaiting verified results')

    def test_report_is_deterministic_and_retains_native_charts_tables_and_formulas(self):
        rows=[selection(str(i)) for i in range(25)]
        rows[0]['home_team']='=SUM(A1:A2)'
        path=write_workbook(self.root,rows,[],{})
        first=path.read_bytes();write_workbook(self.root,rows,[],{})
        self.assertEqual(first,path.read_bytes())
        with ZipFile(path) as z:
            charts=[n for n in z.namelist() if '/charts/chart' in n and n.endswith('.xml')]
            self.assertEqual(len(charts),5)
            for n in charts:
                ET.fromstring(z.read(n))
            sheet=ET.fromstring(z.read('xl/worksheets/sheet5.xml'))
            self.assertIsNotNone(sheet.find(f'.//{{{NS}}}c[@r="N6"]/{{{NS}}}f'))
            self.assertIsNone(sheet.find(f'.//{{{NS}}}c[@r="D6"]/{{{NS}}}f'))
            tables=[ET.fromstring(z.read(n)) for n in z.namelist() if n.startswith('xl/tables/') and n.endswith('.xml')]
            table=next(t for t in tables if t.get('name')=='SelectionsTable')
            self.assertEqual(table.get('ref'),'A5:T30')
            roi_charts=[z.read(n).decode() for n in charts if 'ROI Plan' in z.read(n).decode()]
            self.assertIn('$34',roi_charts[0])
            self.assertIn('60h-ucl-v1',z.read('xl/worksheets/sheet3.xml').decode())

    def test_missing_probability_does_not_become_zero_in_calibration(self):
        path=write_workbook(self.root,[selection('a','LOST',None)],[],{})
        self.assertEqual(cell(path,1,'B15'),'n.a.')
        self.assertEqual(cell(path,3,'P6'),0)
        self.assertEqual(cell(path,4,'D6'),0)

    def test_duplicate_fixture_fails_instead_of_inflating_win_rate(self):
        with self.assertRaisesRegex(ValueError,'Duplicate frozen fixture'):
            write_workbook(self.root,[selection('a'),selection('a')],[],{})

    def test_review_generates_one_readable_workbook_and_export_can_refresh_it(self):
        rows=[selection('a')]
        report(self.root,rows,[],{},reviewed_at='2026-10-11T08:00:00Z')
        path=self.root/'readable'/REPORT_NAME
        self.assertTrue(path.exists())
        self.assertEqual(len(list((self.root/'readable').glob('*.xlsx'))),1)
        self.assertEqual(export_existing(self.root),path)

    def test_shortlist_brier_uses_reported_adjusted_probability(self):
        row=selection('a',p=.95);row['rank_probability']=.8
        final=dict(home_goals=2,away_goals=1,match_id=42)
        scored=score_shortlist(row,final,'VERIFIED_FINISHED')
        self.assertAlmostEqual(scored['predicted_probability'],.8)
        self.assertAlmostEqual(scored['brier'],.04)


if __name__=='__main__':unittest.main()

