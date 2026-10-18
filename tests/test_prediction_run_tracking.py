"""Track later archived shortlists without duplicating uploads or model evidence."""
from offline_test_case import OfflineQuotePolicyTestCase
from datetime import timedelta
import copy
import json
from pathlib import Path
import tempfile
from unittest.mock import patch
from zipfile import ZipFile
import pandas as pd

from performance_tracking import capture, snapshots, frozen_rows, review, tracking_key, write_json
from performance_excel import REPORT_NAME, write_workbook
from performance_report_layout import get_sheet, q, text
from workflow_checks import report_check
from test_performance_tracking import fixture, pick, final, T0, KICK, MockSession


def save_run(root, generated, predictions, picks):
    raw=root/'raw';raw.mkdir(parents=True,exist_ok=True)
    pd.DataFrame(predictions).to_csv(raw/'all_leagues_predictions.csv',index=False)
    pd.DataFrame(picks).to_csv(raw/'conservative_bet_shortlist.csv',index=False)
    write_json(raw/'conservative_bet_summary.json', {'generated_at_utc':generated.isoformat(),
        'n_shortlisted':len(picks),'n_fixtures':len(predictions),
        'n_strict_qualified':sum(r['selection_tier']=='STRICT' for r in picks),
        'n_provisional_watchlist':sum(r['selection_tier']=='PROVISIONAL' for r in picks)})


class PredictionRunTrackingTests(OfflineQuotePolicyTestCase):
    def test_later_markets_prices_and_new_matches_are_graded_once_per_generation(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            first=dict(pick(market='Home win'),per_stake_cost=.02)
            save_run(root,T0,[fixture()],[first]);capture('a'*40,root=root,captured_at=T0)
            later=dict(pick(market='Away win',tier='PROVISIONAL'),offered_decimal_odds=3.,rank_probability=.3,per_stake_cost=.03)
            other=dict(fixture(),fixture_id='event2',home_team='Chelsea FC',away_team='Fulham FC')
            other_pick=dict(pick(market='Over 1.5'),fixture_id='event2',home_team='Chelsea FC',away_team='Fulham FC',offered_decimal_odds=1.8,per_stake_cost=.02)
            save_run(root,T0+timedelta(hours=1),[fixture(),other],[later,other_pick])
            capture('b'*40,root=root,captured_at=T0+timedelta(hours=1))
            # One generation pushed under a second commit is not a new forecast run.
            capture('c'*40,root=root,captured_at=T0+timedelta(hours=1,minutes=1))
            archive=snapshots(root)
            self.assertEqual(len(frozen_rows(archive,'shortlist')),2)
            rows=frozen_rows(archive,'shortlist',all_runs=True)
            self.assertEqual(len(rows),3)
            self.assertEqual(len({tracking_key(r) for r in rows}),3)
            second=final(h=1,a=0);second['id']=90003;second['homeTeam']={'name':'Chelsea FC'};second['awayTeam']={'name':'Fulham FC'}
            session=MockSession([final(),second])
            metrics=review(root=root,token='fake',clock=KICK+timedelta(days=1),session=session)
            self.assertEqual(len(session.calls),1)
            self.assertEqual(metrics['shortlist']['graded'],2)
            self.assertEqual(metrics['shortlist']['wins'],0)
            self.assertAlmostEqual(metrics['shortlist']['flat_stake_roi'],(-2.05/2),places=6)
            self.assertEqual(metrics['unique_shortlisted_fixtures'],2)
            self.assertEqual(metrics['tracked_prediction_runs'],2)
            self.assertEqual(metrics['first_prediction_reference']['wins'],1)
            self.assertAlmostEqual(metrics['first_prediction_reference']['flat_stake_roi'],-.27)
            self.assertEqual(metrics['prediction_fixtures_graded'],2)
            self.assertEqual(sorted(r['total'] for r in metrics['run_history_groups'].values()),[1,2])
            # Integrity verification joins each grade to its own run, not just the match.
            self.assertEqual(report_check(root)['shortlist']['graded'],2)
            grades=pd.read_csv(root/'performance/shortlist_grades.csv')
            self.assertEqual(grades.offered_decimal_odds.tolist(),[3.,1.8])
            self.assertEqual(grades.unit_profit.tolist(),[-1.03,-1.02])
            self.assertEqual(grades.snapshot_commit.tolist(),['b'*40,'b'*40])
            self.assertEqual(grades.snapshot_generated_utc.nunique(),1)
            history=pd.read_csv(root/'performance/shortlist_run_history.csv')
            self.assertEqual(len(history),3)
            self.assertEqual(history.offered_decimal_odds.tolist(),[1.5,3.,1.8])
            self.assertEqual(metrics['shortlist_run_history']['total'],3)
            with ZipFile(root/'readable'/REPORT_NAME) as z: parts={n:z.read(n) for n in z.namelist()}
            dashboard=get_sheet(parts,'Dashboard')
            self.assertEqual(text(dashboard.cell('B7')),2)
            self.assertAlmostEqual(text(dashboard.cell('B13')),-2.05/2)
            self.assertIn('Latest-match',text(dashboard.cell('A18')))
            runs=get_sheet(parts,'Run Tracking')
            self.assertEqual(text(runs.cell('A8')),2)
            self.assertEqual(text(runs.cell('I8')),2)
            sheet=get_sheet(parts,'Selections')
            self.assertEqual(text(sheet.cell('V5')),'Generated UTC')
            self.assertEqual(text(sheet.cell('W5')),'Captured UTC')
            for raw in parts.values():
                if raw.lstrip().startswith(b'<?xml') and b'<table ' in raw and b'name="SelectionsTable"' in raw:
                    self.assertIn(b':W7',raw)
                    self.assertIn(b'count="23"',raw)
            report=(root/'performance/README.md').read_text()
            self.assertIn('Latest selections by prediction run',report)
            self.assertIn('First-prediction reference',report)
            self.assertIn('Generated UTC',(root/'performance/weekly/2026-W41.md').read_text())
            # Every grade and unique-reference count is regenerated deterministically.
            again=review(root=root,clock=KICK+timedelta(days=1),session=session)
            self.assertEqual(again['shortlist'],metrics['shortlist'])
            self.assertEqual(again['first_prediction_reference'],metrics['first_prediction_reference'])

    def test_run_identity_retains_microseconds_and_normalizes_utc(self):
        base={'fixture_key':'match','snapshot_generated_utc':'2026-10-18T12:00:00.000001Z','snapshot_commit':'a'*40}
        same=dict(base,snapshot_generated_utc='2026-10-18T15:00:00.000001+03:00',snapshot_commit='b'*40)
        self.assertEqual(tracking_key(base),tracking_key(same))
        self.assertNotEqual(tracking_key(base),tracking_key(dict(base,snapshot_generated_utc='2026-10-18T12:00:00.000002Z')))

    def test_generation_and_capture_lead_safeguards_apply_to_every_run(self):
        def meta(sha, generated, captured):
            return {'git_commit_sha':sha,'generated_at_utc':generated.isoformat(),'captured_at_utc':captured.isoformat()}
        archives=[(meta('a'*40,T0,T0),[fixture()],[pick()]),
            (meta('b'*40,KICK-timedelta(minutes=20),KICK-timedelta(minutes=20)),[fixture()],[pick()]),
            (meta('c'*40,KICK-timedelta(minutes=19),KICK-timedelta(minutes=19)),[fixture()],[pick()]),
            (meta('d'*40,T0,KICK-timedelta(minutes=19)),[fixture()],[pick()]),
            (meta('e'*40,KICK+timedelta(hours=1),KICK+timedelta(hours=1)),[fixture()],[pick()])]
        rows=frozen_rows(archives,'shortlist',all_runs=True)
        self.assertEqual([r['snapshot_commit'] for r in rows],['a'*40,'b'*40])
        self.assertEqual(len(frozen_rows(archives,'shortlist')),1)

    def test_pending_runs_and_duplicate_records_do_not_fabricate_profit(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            for i,sha in enumerate(('a'*40,'b'*40)):
                clock=T0+timedelta(hours=i)
                save_run(root,clock,[fixture()],[pick()]);capture(sha,root=root,captured_at=clock)
            metrics=review(root=root,clock=T0+timedelta(hours=2))
            self.assertEqual(metrics['shortlist']['pending'],1)
            self.assertIsNone(metrics['shortlist']['win_rate'])
            self.assertIsNone(metrics['shortlist']['flat_stake_roi'])
            self.assertEqual(report_check(root)['shortlist']['pending'],1)
            rows=pd.read_csv(root/'performance/shortlist_grades.csv').to_dict('records')
            with self.assertRaisesRegex(ValueError,'Duplicate frozen fixture'):
                write_workbook(root,[rows[0],rows[0]],[],metrics)

    def test_cross_run_tampering_cannot_borrow_another_runs_price_or_identity(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            save_run(root,T0,[fixture()],[pick()]);capture('a'*40,root=root,captured_at=T0)
            later=dict(pick(),offered_decimal_odds=2.)
            clock=T0+timedelta(hours=1)
            save_run(root,clock,[fixture()],[later]);capture('b'*40,root=root,captured_at=clock)
            review(root=root,token='fake',clock=KICK+timedelta(days=1),session=MockSession([final()]))
            path=root/'performance/shortlist_grades.csv';original=pd.read_csv(path)
            for field,value in [('offered_decimal_odds',1.5),('snapshot_commit','a'*40),
                                ('snapshot_generated_utc',T0.isoformat()),
                                ('snapshot_captured_utc',T0.isoformat())]:
                changed=original.copy();changed.loc[0,field]=value;changed.to_csv(path,index=False)
                with self.assertRaises(ValueError): report_check(root)
            original.to_csv(path,index=False)
            path=root/'performance/metrics.json';metrics=json.loads(path.read_text())
            for field in ('tracked_prediction_runs','unique_shortlisted_fixtures'):
                changed=copy.deepcopy(metrics);changed[field]=99;write_json(path,changed)
                with self.assertRaises(ValueError): report_check(root)
            changed=copy.deepcopy(metrics);changed['groups']['run']={};write_json(path,changed)
            with self.assertRaises(ValueError): report_check(root)

    def test_latest_uses_generation_order_and_keeps_previously_shortlisted_matches(self):
        def meta(sha, generated, captured):
            return {'git_commit_sha':sha,'generated_at_utc':generated.isoformat(),'captured_at_utc':captured.isoformat()}
        newer=dict(pick(),market='Home win',offered_decimal_odds=1.4)
        old=dict(pick(),market='Away win',offered_decimal_odds=4.)
        second=dict(pick(),fixture_id='other',home_team='Chelsea FC',away_team='Fulham FC')
        archive=[(meta('a'*40,T0,T0),[fixture()],[pick()]),
            (meta('b'*40,T0+timedelta(hours=1),T0+timedelta(hours=1)),[fixture()],[newer]),
            # An older generation uploaded later cannot roll the tracked forecast back.
            (meta('c'*40,T0+timedelta(minutes=30),T0+timedelta(hours=2)),[fixture()],[old]),
            # Absence from the next shortlist does not erase the last shortlisted prediction.
            (meta('d'*40,T0+timedelta(hours=3),T0+timedelta(hours=3)),[fixture()],[second])]
        latest=frozen_rows(archive,'shortlist',latest=True)
        self.assertEqual(len(latest),2)
        self.assertEqual(latest[0]['snapshot_commit'],'b'*40)
        self.assertEqual(latest[0]['market'],'Home win')
        self.assertEqual(len(frozen_rows(archive,'shortlist',all_runs=True)),4)
        self.assertEqual(frozen_rows(archive,'shortlist')[0]['snapshot_commit'],'a'*40)
        with self.assertRaises(ValueError): frozen_rows(archive,'shortlist',latest=True,all_runs=True)
