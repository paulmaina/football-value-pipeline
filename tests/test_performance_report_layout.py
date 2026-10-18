"""Monitoring layout must preserve calculations, uncertainty and source evidence."""
from offline_test_case import OfflineQuotePolicyTestCase
import copy
import json
from pathlib import Path
import tempfile
import unittest
import xml.etree.ElementTree as ET
from zipfile import ZipFile
from unittest.mock import patch

from performance_excel import write_workbook, add_health_sheet
from performance_report_layout import format_report, get_sheet, text, experiment_rows, NS, q


def parts(path):
    with ZipFile(path) as z:return {n:z.read(n) for n in z.namelist()}


def evidence(path, name):
    s=get_sheet(parts(path),name)
    return {c.get('r'):(text(c),c.find(q('f')).text if c.find(q('f')) is not None else None)
        for c in s.root.iter(q('c')) if int(''.join(filter(str.isdigit,c.get('r'))))>=6}


def row(key, status='WON', price=1.3, week='2026-W41'):
    return dict(fixture_key=key,kickoff_utc='2026-10-12T16:00:00Z',league='EPL',home_team='Home',away_team='Away',market='Over 1.5',selection_tier='STRICT',predicted_probability=.8,offered_decimal_odds=price,status=status,week=week,selection_policy_version='policy',per_stake_cost=.02)


class MonitoringLayoutTests(OfflineQuotePolicyTestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.addCleanup(self.temp.cleanup);self.root=Path(self.temp.name)

    def test_source_ledgers_inputs_and_metric_caches_unchanged(self):
        rows=[row('a'),row('b','LOST',None),row('c','PENDING',week='2026-W42')]
        original=copy.deepcopy(rows)
        with patch('performance_report_layout.format_report'):
            path=write_workbook(self.root,rows,[],{})
        before={name:evidence(path,name) for name in ('Selections','Predictions','Calibration')}
        raw=parts(path);dashboard=get_sheet(raw,'Dashboard');values={f'B{i}':text(dashboard.cell(f'B{i}')) for i in range(7,20)}
        format_report(path,self.root)
        after=parts(path)
        for name,data in before.items():self.assertEqual(evidence(path,name),data)
        for address,value in values.items():self.assertEqual(text(get_sheet(after,'Dashboard').cell(address)),value)
        roi=get_sheet(after,'ROI Plan');self.assertEqual(text(roi.cell('B4')),100);self.assertEqual(text(roi.cell('B5')),1)
        self.assertFalse(any('B4' in m.get('ref') for m in roi.root.findall('.//'+q('mergeCell'))))
        self.assertEqual(rows,original)

    def test_repeated_formatting_is_deterministic_and_native_objects_survive(self):
        path=write_workbook(self.root,[row('a')],[],{});format_report(path,self.root);first=path.read_bytes();format_report(path,self.root)
        self.assertEqual(first,path.read_bytes())
        data=parts(path);self.assertEqual(len([p for p in data if '/charts/chart' in p and p.endswith('.xml')]),5)
        self.assertEqual(len([p for p in data if p.startswith('xl/tables/') and p.endswith('.xml')]),5)
        self.assertIsNotNone(get_sheet(data,'Selections').cell('N6').find(q('f')))
        self.assertTrue(data['[Content_Types].xml'].splitlines()[1].startswith(b'<Types xmlns='))

    def test_breakdown_table_header_matches_worksheet_after_formatting(self):
        path=write_workbook(self.root,[row('a')],[],{})
        for _ in range(2):
            data=parts(path)
            header=text(get_sheet(data,'Breakdowns').cell('O5'))
            tables=[ET.fromstring(value) for name,value in data.items()
                    if name.startswith('xl/tables/') and name.endswith('.xml')]
            table=next(t for t in tables if t.get('name')=='BreakdownsTable')
            self.assertEqual(header,'Calibration gap')
            self.assertEqual(table.find(q('tableColumns'))[14].get('name'),header)
            format_report(path,self.root)

    def test_no_prices_or_results_are_unavailable_in_profit_trend(self):
        for rows in ([],[row('a','PENDING')],[row('a','WON',None)]):
            path=write_workbook(self.root,rows,[],{});sheet=get_sheet(parts(path),'Weekly Trends')
            self.assertIn(text(sheet.cell('E6')),('n.a.',None))
        path=write_workbook(self.root,[row('a'),row('b','LOST',1.5,'2026-W42')],[],{})
        s=get_sheet(parts(path),'Weekly Trends');self.assertAlmostEqual(text(s.cell('E7')),-.74)
        self.assertIn('SUM($D$6:D7)',s.cell('E7').find(q('f')).text)

    def test_missing_reports_do_not_look_healthy(self):
        r=experiment_rows(self.root,None)
        self.assertEqual(len(r),10)
        self.assertTrue(all(x[1]=='Report unavailable or stale' and x[2]=='Unavailable' for x in r))
        self.assertTrue(all('Regenerate' in x[8] for x in r))

    def test_thresholds_coverage_blockers_and_readiness_come_from_registered_reports(self):
        directory=self.root/'performance/benchmark_forward_experiment';directory.mkdir(parents=True)
        summary={'review_gates':{'minimum_paired_fixtures':450,'minimum_gameweeks':8,'minimum_verified_coverage':.9},'verified_coverage':.85,'rejected_snapshot_commits':['x']}
        (directory/'summary.json').write_text(json.dumps(summary))
        health={'review_queue':{'experiments':[{'name':'benchmark_forward_experiment','status':'DATA_QUALITY_BLOCKED','settled_evidence':450,'gameweeks':8,'evidence':'NO_CLEAR_PROMOTION_EVIDENCE'}]}}
        values=experiment_rows(self.root,health)[4]
        self.assertEqual(values[4],'450 paired fixtures');self.assertEqual(values[5],'8 / 8 ISO weeks');self.assertEqual(values[6],.85)
        self.assertIn('Coverage below 90%',values[8]);self.assertIn('Rejected snapshots',values[8])
        health['review_queue']['experiments'][0]['status']='READY_FOR_REVIEW'
        self.assertIn('approval is separate',experiment_rows(self.root,health)[4][8])

    def test_health_sections_capture_states_formats_and_freeze_panes(self):
        path=write_workbook(self.root,[row('a')],[],{})
        health={'reviewed_at_utc':'2026-10-14T12:00:00Z','training':{'EPL':{'training_end':'2026-10-12','training_matches':20,'days_since_latest_result':2,'forecast_training_health':{'status':'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'}}},
            'snapshot_capture_history':[{'commit':'a'*40,'captured_at_utc':'2026-10-14T11:00:00Z','experiments':{'benchmark_forward_experiment':'CAPTURE_FAILED','totals_anchor_experiment':'CAPTURED'}}],
            'quote_audit':{'bookmakers':{'1xBet':1},'selected_quotes':1},'closing_odds':{'by_bookmaker':{'1xbet':{'covered_selections':1,'missing_selections':2,'pending_selections':3,'mean_fair_close_ev':.02,'mean_same_book_offered_price_clv':.01}}},'dependencies':{'python':'3.12'}}
        original=copy.deepcopy(health);add_health_sheet(self.root,health,{'days':{}})
        data=parts(path);s=get_sheet(data,'Pipeline Health')
        contents=[text(c) for c in s.root.iter(q('c'))]
        self.assertIn('Near-close quote coverage',contents);self.assertIn('Training data freshness',contents)
        self.assertIn('Source completeness unverified',contents);self.assertIn('Capture failed',contents)
        details=get_sheet(data,'Capture Details');self.assertEqual(text(details.cell('G6')),'CAPTURE_FAILED');self.assertEqual(text(details.cell('H6')),'CAPTURED')
        select=get_sheet(data,'Selections');pane=select.root.find('.//'+q('pane'));self.assertEqual(pane.get('topLeftCell'),'E6')
        self.assertEqual(health,original)
        self.assertIsNotNone(get_sheet(data,'Experiments').root.find(q('conditionalFormatting')))


if __name__=='__main__':unittest.main()
