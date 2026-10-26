from offline_test_case import OfflineQuotePolicyTestCase
from pathlib import Path
import json
import subprocess
import tempfile
import unittest
from unittest.mock import patch
from publish_performance import git
from publish_scheduled_forecasts import publish,main


def repo(directory):
    source=Path(directory)/'source';remote=Path(directory)/'remote.git';source.mkdir()
    subprocess.run(['git','init','--bare',str(remote)],check=True,capture_output=True)
    git(source,'init','-b','main');git(source,'config','user.name','test');git(source,'config','user.email','test@example.invalid')
    (source/'keep.txt').write_text('preserve');git(source,'add','.');git(source,'commit','-m','seed');git(source,'remote','add','origin',str(remote));git(source,'push','-u','origin','main')
    return source,remote


class ScheduledPublisherTests(OfflineQuotePolicyTestCase):
    def test_capture_commit_and_safe_retry_preserve_concurrent_main(self):
        with tempfile.TemporaryDirectory() as tmp:
            source,remote=repo(tmp);calls=[];attempt=[0]
            def runner(cmd,cwd,check):
                work=Path(cwd);calls.append(cmd)
                if cmd[1]=='football_value_pipeline_v2_standalone.py':
                    for flag in ('--recency-experiment', '--reliability-experiment',
                                 '--goal-blend-experiment', '--market-led-experiment'):
                        self.assertIn(flag, cmd)
                    raw=work/'football_output_v2/raw';raw.mkdir(parents=True,exist_ok=True);(raw/'forecast.csv').write_text(str(len(calls)))
                    cache=work/'.football_cache';cache.mkdir(exist_ok=True)
                    (cache/'2627_E0.csv').write_text('validated training revision '+str(len(calls)))
                    (cache/'oddsapi_events_EPL.json').write_text('temporary odds response')
                if cmd[1]=='performance_tracking.py' and cmd[2]=='capture':
                    self.assertEqual(cmd[-1],git(work,'rev-parse','HEAD').stdout.strip())
                    p=work/'football_output_v2/performance';p.mkdir(parents=True,exist_ok=True);(p/'snapshot.json').write_text(cmd[-1])
                if cmd[1]=='performance_tracking.py' and cmd[2]=='review':
                    p=work/'football_output_v2/readable';p.mkdir(parents=True,exist_ok=True);(p/'football_performance_report.xlsx').write_bytes(b'workbook')
                    if attempt[0]==0:
                        attempt[0]+=1;(source/'keep.txt').write_text('concurrent update');git(source,'add','keep.txt');git(source,'commit','-m','concurrent');git(source,'push','origin','main')
                if cmd[1:3]==['workflow_checks.py','reports']:
                    self.assertEqual(cmd[3:],['--output','football_output_v2/performance/workflow_health.json'])
                    output=work/cmd[-1]
                    output.write_text(json.dumps({'status':'VERIFIED',
                        'forecast_commit':git(work,'rev-parse','HEAD').stdout.strip()}))
            publish(source,runner=runner)
            git(source,'fetch','origin','main');self.assertEqual(git(source,'show','FETCH_HEAD:keep.txt').stdout,'concurrent update')
            self.assertIn('validated training revision',git(source,'show','FETCH_HEAD:.football_cache/2627_E0.csv').stdout)
            self.assertNotEqual(git(source,'show','FETCH_HEAD:.football_cache/oddsapi_events_EPL.json',check=False).returncode,0)
            health=json.loads(git(source,'show','FETCH_HEAD:football_output_v2/performance/workflow_health.json').stdout)
            self.assertEqual(health['status'],'VERIFIED')
            self.assertEqual(health['forecast_commit'],git(source,'rev-parse','FETCH_HEAD^').stdout.strip())
            self.assertTrue(any(c[1]=='workflow_checks.py' and c[2]=='reports' for c in calls))
            self.assertEqual(sum(c[1]=='football_value_pipeline_v2_standalone.py' for c in calls),2)
            with patch('publish_scheduled_forecasts.publish') as p: self.assertEqual(main(['--repo',str(source)]),0);p.assert_called_once()

    def test_pruned_runs_leave_main_in_the_capture_commit(self):
        import shutil
        old='a'*64;kept='b'*64
        with tempfile.TemporaryDirectory() as tmp:
            source,_=repo(tmp)
            for run in (old,kept):
                bundle=source/'football_output_v2/raw/prediction_runs'/run;bundle.mkdir(parents=True)
                (bundle/'run_manifest.json').write_text(run)
            git(source,'add','.');git(source,'commit','-m','runs');git(source,'push','origin','main')
            order=[]
            def runner(cmd,cwd,check):
                work=Path(cwd);order.append(cmd[1:3])
                if cmd[1]=='football_value_pipeline_v2_standalone.py':
                    (work/'football_output_v2/raw/forecast.csv').write_text('new forecast')
                if cmd[1]=='performance_tracking.py' and cmd[2]=='capture':
                    p=work/'football_output_v2/performance';p.mkdir(parents=True,exist_ok=True);(p/'snapshot.json').write_text('captured')
                if cmd[1]=='performance_tracking.py' and cmd[2]=='review':
                    p=work/'football_output_v2/readable';p.mkdir(parents=True,exist_ok=True);(p/'report.xlsx').write_bytes(b'workbook')
            def prune(root):
                order.append('prune');self.assertTrue((root/'performance/snapshot.json').exists())
                shutil.rmtree(root/'raw/prediction_runs'/old);return [old]
            with patch('publish_scheduled_forecasts.prune_captured_runs',side_effect=prune):
                publish(source,runner=runner)
            self.assertEqual(order.index('prune'),order.index(['performance_tracking.py','capture'])+1)
            git(source,'fetch','origin','main')
            files=git(source,'ls-tree','-r','--name-only','FETCH_HEAD').stdout.split()
            self.assertNotIn(f'football_output_v2/raw/prediction_runs/{old}/run_manifest.json',files)
            self.assertIn(f'football_output_v2/raw/prediction_runs/{kept}/run_manifest.json',files)
            # The deletion and the snapshot it relies on land in one commit.
            changed=git(source,'show','--name-status','--format=','FETCH_HEAD').stdout
            self.assertIn(f'D\tfootball_output_v2/raw/prediction_runs/{old}/run_manifest.json',changed)
            self.assertIn('A\tfootball_output_v2/performance/snapshot.json',changed)

    def test_report_validation_failure_never_publishes_forecast_or_health(self):
        with tempfile.TemporaryDirectory() as tmp:
            source,_=repo(tmp);old=git(source,'rev-parse','HEAD').stdout.strip()
            def runner(cmd,cwd,check):
                work=Path(cwd)
                if cmd[1]=='football_value_pipeline_v2_standalone.py':
                    raw=work/'football_output_v2/raw';raw.mkdir(parents=True)
                    (raw/'forecast.csv').write_text('new forecast')
                if cmd[1]=='performance_tracking.py' and cmd[2]=='review':
                    (work/'football_output_v2/performance').mkdir(parents=True)
                if cmd[1:3]==['workflow_checks.py','reports']:
                    (work/cmd[-1]).write_text('{"status":"incomplete"}')
                    raise subprocess.CalledProcessError(1,cmd)
            with self.assertRaises(subprocess.CalledProcessError):
                publish(source,runner=runner)
            git(source,'fetch','origin','main')
            self.assertEqual(git(source,'rev-parse','FETCH_HEAD').stdout.strip(),old)
            self.assertNotEqual(git(source,'show','FETCH_HEAD:football_output_v2/performance/workflow_health.json',check=False).returncode,0)

    def test_failure_and_empty_run_never_publish_outputs(self):
        with tempfile.TemporaryDirectory() as tmp:
            source,_=repo(tmp);old=git(source,'rev-parse','HEAD').stdout
            with self.assertRaises(RuntimeError):publish(source,attempts=0)
            def fail(*args,**kwargs):raise subprocess.CalledProcessError(1,['pipeline'])
            with self.assertRaises(subprocess.CalledProcessError):publish(source,runner=fail)
            self.assertEqual(git(source,'rev-parse','HEAD').stdout,old)
            def empty(cmd,cwd,check):
                if cmd[1]=='football_value_pipeline_v2_standalone.py':(Path(cwd)/'football_output_v2/raw').mkdir(parents=True)
            publish(source,runner=empty)
            self.assertEqual(git(source,'rev-parse','HEAD').stdout,old)
