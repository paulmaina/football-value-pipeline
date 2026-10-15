from offline_test_case import OfflineQuotePolicyTestCase
import copy
from datetime import timedelta
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

import pandas as pd
import yaml
from performance_tracking import capture,review,verified_record,write_json
from test_performance_tracking import fixture,pick,final,T0,KICK,SHA
from workflow_checks import raw_check,archive_check,report_check,changed_forecasts,capture_event,coverage_check,smoke,COVERAGE_FLOORS

REPO=Path(__file__).resolve().parents[1]


class WorkflowChecksTests(OfflineQuotePolicyTestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup)
        self.root=Path(self.tmp.name)/'football_output_v2'
        raw=self.root/'raw';raw.mkdir(parents=True)
        pd.DataFrame([fixture()]).to_csv(raw/'all_leagues_predictions.csv',index=False)
        pd.DataFrame([pick()]).to_csv(raw/'conservative_bet_shortlist.csv',index=False)
        write_json(raw/'conservative_bet_summary.json',{'generated_at_utc':T0.isoformat(),'n_fixtures':1,
            'n_shortlisted':1,'n_strict_qualified':1,'n_provisional_watchlist':0})

    def reviewed(self, errors=None):
        capture(SHA,root=self.root,captured_at=T0)
        record=verified_record('PL',final())
        write_json(self.root/'performance/verified_results.json',{'PL:90002':record})
        with patch('performance_tracking.collect_results',return_value=([record],errors or {})):
            review(root=self.root,clock=KICK+timedelta(days=1))

    def test_valid_raw_and_report_reconcile_with_verified_cache_and_archives(self):
        self.assertEqual(raw_check(self.root)['forecasts'],1)
        self.reviewed();data=report_check(self.root)
        self.assertEqual(data['status'],'VERIFIED')
        self.assertEqual(data['shortlist']['wins'],1)
        self.assertEqual(data['snapshots'],1)
        self.assertIn('legacy/unspecified',data['policy_groups'])

    def test_pending_reports_do_not_claim_zero_success_or_profit(self):
        capture(SHA,root=self.root,captured_at=T0)
        with patch('performance_tracking.collect_results',return_value=([],{})):
            review(root=self.root,clock=T0)
        result=report_check(self.root)
        self.assertEqual(result['shortlist']['pending'],1)
        self.assertIsNone(result['shortlist']['win_rate'])
        self.assertIsNone(result['shortlist']['flat_stake_roi'])

    def test_failed_optional_capture_is_a_top_level_warning(self):
        self.reviewed()
        path = self.root/'performance/pipeline_health.json'
        health = json.loads(path.read_text())
        health['snapshot_capture_history'][-1]['experiments']['shortlist_policy_experiment'] = 'PRESENT_BUT_REJECTED'
        write_json(path, health)
        result = report_check(self.root)
        self.assertEqual(result['status'], 'VERIFIED_WITH_WARNINGS')
        self.assertTrue(any('shortlist_policy_experiment: latest snapshot PRESENT_BUT_REJECTED' in s for s in result['warnings']))

    def test_raw_check_validates_every_present_optional_sidecar(self):
        from workflow_checks import SIDECARS
        raw = self.root/'raw'
        for name in SIDECARS:
            write_json(raw/name, {})
        warnings = raw_check(self.root)['warnings']
        for name in SIDECARS:
            self.assertTrue(any(name in warning for warning in warnings), name)

    def test_provider_outage_is_visible_while_verified_cache_remains_usable(self):
        self.reviewed({'PL':'temporary provider failure'})
        data=report_check(self.root)
        self.assertEqual(data['status'],'VERIFIED_WITH_WARNINGS')
        self.assertEqual(data['shortlist']['graded'],1)
        self.assertIn('PL',data['provider_errors'])

    def test_raw_rejects_duplicate_unbound_or_invalid_forecasts(self):
        raw=self.root/'raw';path=raw/'all_leagues_predictions.csv'
        data=pd.read_csv(path)
        for frame in (pd.concat([data,data]),data.assign(p_home=float('nan')),data.assign(p_home=.95)):
            frame.to_csv(path,index=False)
            with self.assertRaises(ValueError):raw_check(self.root)
        data.to_csv(path,index=False)
        pd.DataFrame([dict(pick(),home_team='wrong fixture')]).to_csv(raw/'conservative_bet_shortlist.csv',index=False)
        with self.assertRaisesRegex(ValueError,'matching forecast'):raw_check(self.root)

    def test_raw_summary_mismatch_and_stale_sidecar(self):
        raw=self.root/'raw';summary=raw/'conservative_bet_summary.json'
        data=json.loads(summary.read_text());data['n_shortlisted']=9;write_json(summary,data)
        with self.assertRaisesRegex(ValueError,'summary'):raw_check(self.root)
        data['n_shortlisted']=1;write_json(summary,data)
        write_json(raw/'market_led_experiment.json',{})
        self.assertTrue(raw_check(self.root)['warnings'])

    def test_snapshot_tampering_or_path_traversal_blocks_publication(self):
        capture(SHA,root=self.root,captured_at=T0)
        directory=self.root/'performance/snapshots'/SHA[:16]
        meta=directory/'metadata.json';original=json.loads(meta.read_text())
        invalid=copy.deepcopy(original);invalid['sha256']['../outside']='a'*64;write_json(meta,invalid)
        with self.assertRaisesRegex(ValueError,'Unexpected snapshot path'):archive_check(self.root)
        write_json(meta,original)
        (directory/'predictions.csv').write_text('changed')
        with self.assertRaisesRegex(ValueError,'integrity failure'):archive_check(self.root)

    def test_optional_tampering_is_a_warning_and_baseline_survives(self):
        capture(SHA,root=self.root,captured_at=T0)
        directory=self.root/'performance/snapshots'/SHA[:16]
        meta=json.loads((directory/'metadata.json').read_text())
        meta['sha256']['goal_blend_experiment.json']='a'*64
        write_json(directory/'metadata.json',meta)
        self.assertTrue(archive_check(self.root)['warnings'])

    def test_invalid_manifest_timestamp_and_count_are_rejected(self):
        capture(SHA,root=self.root,captured_at=T0)
        path=self.root/'performance/snapshots'/SHA[:16]/'metadata.json'
        original=json.loads(path.read_text())
        for field,value in [('n_all_forecasts',99),('generated_at_utc',(T0+timedelta(days=1)).isoformat()),('git_commit_sha','not-a-sha')]:
            data={**original,field:value};write_json(path,data)
            with self.assertRaises(ValueError):archive_check(self.root)
        write_json(path,original)

    def test_wrong_report_totals_outcomes_prices_or_provenance_are_rejected(self):
        self.reviewed();performance=self.root/'performance'
        metrics=performance/'metrics.json';original=json.loads(metrics.read_text())
        wrong=copy.deepcopy(original);wrong['shortlist']['wins']=9;write_json(metrics,wrong)
        with self.assertRaisesRegex(ValueError,'Shortlist wins'):report_check(self.root)
        write_json(metrics,original)
        grades=performance/'shortlist_grades.csv';data=pd.read_csv(grades)
        for field,value in [('offered_decimal_odds',9),('final_score','0-5'),('selection_tier','PROVISIONAL'),('snapshot_commit','0'*40),('unit_profit',7)]:
            data.assign(**{field:value}).to_csv(grades,index=False)
            with self.assertRaises(ValueError):report_check(self.root)
        data.to_csv(grades,index=False)
        self.assertEqual(report_check(self.root)['status'],'VERIFIED')

    def test_missing_verified_source_and_broken_workbook_are_rejected(self):
        self.reviewed()
        cache=self.root/'performance/verified_results.json';data=cache.read_text();write_json(cache,{})
        with self.assertRaisesRegex(ValueError,'verified cache'):report_check(self.root)
        cache.write_text(data)
        (self.root/'readable/football_performance_report.xlsx').write_bytes(b'broken workbook')
        with self.assertRaises(Exception):report_check(self.root)

    def test_unfinished_cached_result_cannot_be_graded(self):
        self.reviewed()
        path=self.root/'performance/verified_results.json'
        data=json.loads(path.read_text());data['PL:90002']['source_status']='SCHEDULED';write_json(path,data)
        with self.assertRaisesRegex(ValueError,'not verified finished'):report_check(self.root)

    def test_workbook_cached_metrics_must_match_verified_report(self):
        from zipfile import ZipFile
        self.reviewed()
        path=self.root/'readable/football_performance_report.xlsx'
        with ZipFile(path) as z:parts={name:z.read(name) for name in z.namelist()}
        text=parts['xl/worksheets/sheet1.xml'].decode()
        import re
        text=re.sub(r'(<c[^>]*r="B9"[^>]*>.*?<v>)[^<]+',r'\g<1>99',text)
        parts['xl/worksheets/sheet1.xml']=text.encode()
        with ZipFile(path,'w') as z:
            for name,data in parts.items():z.writestr(name,data)
        with self.assertRaisesRegex(ValueError,'Workbook wins'):report_check(self.root)

    def test_code_only_push_skips_capture_and_initial_data_push_is_supported(self):
        repo=Path(self.tmp.name)/'repo';repo.mkdir()
        def git(*args):
            return subprocess.run(['git','-C',str(repo),*args],check=True,text=True,capture_output=True).stdout.strip()
        git('init');git('config','user.name','CI Test');git('config','user.email','ci@example.com')
        (repo/'code.py').write_text('pass\n');git('add','.');git('commit','-m','initial code')
        before=git('rev-parse','HEAD')
        (repo/'code.py').write_text('x=1\n');git('add','.');git('commit','-m','code only');sha=git('rev-parse','HEAD')
        self.assertFalse(changed_forecasts(repo,before,sha))
        self.assertFalse(capture_event(repo,self.root,'push',sha,before))
        raw=repo/'football_output_v2/raw';raw.mkdir(parents=True)
        (raw/'goal_blend_experiment.json').write_text('{}');git('add','.');git('commit','-m','sidecar')
        newest=git('rev-parse','HEAD')
        self.assertTrue(changed_forecasts(repo,sha,newest))
        self.assertTrue(changed_forecasts(repo,'0'*40,newest))
        with self.assertRaisesRegex(ValueError,'checkout differs'):changed_forecasts(repo,sha,sha)

    def test_unsupported_capture_event_is_rejected(self):
        with self.assertRaisesRegex(ValueError,'explicit manual'):capture_event(REPO,self.root,'schedule',SHA)

    def test_coverage_missing_module_or_regression_fails(self):
        data={'totals':{'percent_covered':80},'files':{k:{'summary':{'percent_covered':100}} for k in COVERAGE_FLOORS}}
        path=Path(self.tmp.name)/'coverage.json';write_json(path,data)
        self.assertEqual(coverage_check(path)['overall_percent'],80)
        del data['files']['match_scores.py'];write_json(path,data)
        with self.assertRaisesRegex(ValueError,'Missing coverage'):coverage_check(path)
        data['files']['match_scores.py']={'summary':{'percent_covered':10}};write_json(path,data)
        with self.assertRaisesRegex(ValueError,'coverage below'):coverage_check(path)

    def test_smoke_compiles_all_python_and_checks_all_cli_help(self):
        result=smoke(REPO)
        self.assertGreaterEqual(result['python_modules_compiled'],35)
        self.assertEqual(result['cli_help_checked'],len(__import__('workflow_checks').CLI_FILES))

    def test_workflow_matrix_permissions_triggers_and_failure_artifacts(self):
        workflows=REPO/'.github/workflows'
        ci=yaml.load((workflows/'pipeline-self-test.yml').read_text(),Loader=yaml.BaseLoader)
        review_workflow=yaml.load((workflows/'forward-performance.yml').read_text(),Loader=yaml.BaseLoader)
        matrix=ci['jobs']['self-test']['strategy']['matrix']
        self.assertEqual(set(matrix['os']),{'ubuntu-latest','windows-latest'})
        self.assertEqual(set(matrix['python']),{'3.12','3.14'})
        self.assertEqual(ci['permissions']['contents'],'read')
        self.assertEqual(review_workflow['permissions']['contents'],'write')
        self.assertIn('football_output_v2/raw/goal_blend_experiment.json',review_workflow['on']['push']['paths'])
        self.assertEqual(review_workflow['concurrency']['cancel-in-progress'],'false')
        for workflow in (ci,review_workflow):
            steps=next(iter(workflow['jobs'].values()))['steps']
            uploads=[s for s in steps if str(s.get('uses','')).startswith('actions/upload-artifact@')]
            self.assertEqual(uploads[0]['if'],'always()')
        text=(workflows/'forward-performance.yml').read_text()
        self.assertIn('--validate-reports',text)
        self.assertIn('--api-key-source environment',text)
