"""Actions timing, durable reservations and race-safe evidence publication."""
from offline_test_case import OfflineQuotePolicyTestCase
import copy
from datetime import timedelta
import json
import os
from pathlib import Path
import subprocess
import tempfile
from unittest.mock import patch

import yaml

import closing_odds as c
import github_closing_odds as g
from publish_performance import git
from tests.test_closing_odds import setup, payload
from tests.test_publish_scheduled_forecasts import repo


def seeded(directory):
    source, remote = repo(directory)
    root=source/g.ROOT;root.mkdir()
    row, observed=setup(root)
    git(source,'add','--',str(g.ROOT));git(source,'commit','-m','forecast');git(source,'push','origin','main')
    return source,remote,row,observed


class ActionsClosingTests(OfflineQuotePolicyTestCase):
    def test_plan_uses_current_and_archived_fixtures_with_utc_and_daily_bounds(self):
        with tempfile.TemporaryDirectory() as tmp:
            base=Path(tmp);root=base/g.ROOT;root.mkdir();row,clock=setup(root)
            self.assertTrue(g.plan(base,clock)['ready'])
            (root/'raw/all_leagues_predictions.csv').write_text('kickoff_utc,odds_event_id\ninvalid,broken\n')
            self.assertTrue(g.plan(base,clock)['ready'])  # Frozen fixture remains discoverable.
            self.assertFalse(g.plan(base,clock-timedelta(hours=1))['ready'])
            self.assertFalse(g.plan(base,clock+timedelta(minutes=1))['ready'])
            g.write(base/g.BUDGET,{'date':clock.date().isoformat(),'requests':100})
            self.assertEqual(g.plan(base,clock)['reason'],'DAILY_REQUEST_CAP_REACHED')
            with self.assertRaises(ValueError):g.plan(base,clock,21)
            g.write(base/g.BUDGET,{'date':clock.date().isoformat(),'requests':-1})
            with self.assertRaises(ValueError):g.plan(base,clock)
            self.assertFalse(g.plan(base,clock+timedelta(days=1))['ready'])
            with self.assertRaises(ValueError):g.utc('2026-10-10')

    def test_reservations_count_unknown_usage_and_settle_without_resetting_other_runs(self):
        from tests.test_benchmark_forward_experiment import NOW
        clock=NOW
        held,amount=g.reserve({},'run-1',clock,10)
        self.assertEqual(amount,10)
        self.assertEqual(held['requests'],10)
        another,_=g.reserve(held,'run-2',clock,10)
        local=copy.deepcopy(held);local['reservations']['run-1']['used']=2
        done=g.settle(another,local,'run-1')
        self.assertEqual(done['requests'],12)
        self.assertEqual(g.settle(done,local,'run-1'),done)
        self.assertEqual(done['reservations']['run-2']['status'],'reserved')
        tomorrow,_=g.reserve({},'tomorrow',clock+timedelta(days=1),7)
        self.assertEqual(g.settle(tomorrow,local,'run-1'),tomorrow)
        with self.assertRaises(ValueError):g.reserve(held,'run-1',clock,10)
        for bad in ('bad/id',''):
            with self.assertRaises(ValueError):g.reserve({},bad,clock,10)
        for amount in (0,101):
            with self.assertRaises(ValueError):g.reserve({},'id',clock,amount)
        with self.assertRaises(ValueError):g.reserve({'date':clock.date().isoformat(),'requests':-1},'id',clock,10)
        full,_=g.reserve({},'all',clock,100)
        self.assertEqual(g.reserve(full,'no-room',clock,1)[1],0)
        for altered in ({}, {'date':held['date'],'reservations':{'run-1':{'allowance':11,'used':0}}}):
            with self.assertRaises(ValueError):g.settle(held,altered,'run-1')
        local['reservations']['run-1']['used']=11
        with self.assertRaises(ValueError):g.settle(held,local,'run-1')
        local['reservations']['run-1']['used']=3
        with self.assertRaises(ValueError):g.settle(done,local,'run-1')

    def test_reserved_collector_charges_before_failure_and_refuses_expired_allowance(self):
        with tempfile.TemporaryDirectory() as tmp:
            base=Path(tmp);root=base/g.ROOT;root.mkdir();row,clock=setup(root)
            state,_=g.reserve({},'id',clock,2);g.write(base/g.BUDGET,state)
            def fail(*args):
                checkpoint=g.read(base/g.BUDGET)
                self.assertEqual(checkpoint['requests'],2)
                self.assertEqual(checkpoint['reservations']['id']['used'],1)
                raise RuntimeError('secret must not be printed')
            result=c.collect_once(root,None,clock,fetcher=fail,reservation_id='id')
            self.assertEqual(result['requests'],1)
            self.assertNotIn('secret',json.dumps(result))
            c.collect_once(root,None,clock,fetcher=lambda *args:payload(row,clock),reservation_id='id')
            self.assertEqual(g.read(base/g.BUDGET)['reservations']['id']['used'],2)
            self.assertEqual(c.collect_once(root,None,clock,reservation_id='id')['requests'],0)
            for key,when in [('missing',clock),('id',clock+timedelta(days=1))]:
                with self.assertRaises(ValueError):c.collect_once(root,None,when,reservation_id=key)
            state['reservations']['id']['status']='complete';g.write(base/g.BUDGET,state)
            with self.assertRaises(ValueError):c.collect_once(root,None,clock,reservation_id='id')

    def test_publication_retries_never_refetch_odds_or_overwrite_concurrent_data(self):
        with tempfile.TemporaryDirectory() as tmp:
            source,_,row,clock=seeded(tmp);calls=[];raced=[False]
            original=g.commit_push
            def runner(cmd,cwd,check):
                calls.append(cmd);work=Path(cwd)
                git(source,'fetch','origin','main')
                committed=json.loads(git(source,'show','FETCH_HEAD:'+g.BUDGET.as_posix()).stdout)
                self.assertEqual(committed['reservations']['id']['status'],'reserved')
                self.assertIn('--api-key-source',cmd);self.assertIn('environment',cmd)
                result=c.collect_once(work/g.ROOT,None,clock,fetcher=lambda *args:payload(row,clock),reservation_id='id')
                self.assertEqual(result['written'],1)
            def race(work,paths,message,remote,branch):
                if message.startswith('Publish') and not raced[0]:
                    raced[0]=True
                    git(source,'fetch','origin','main');git(source,'reset','--hard','FETCH_HEAD')
                    (source/'keep.txt').write_text('concurrent main data')
                    git(source,'add','keep.txt');git(source,'commit','-m','other data');git(source,'push','origin','main')
                return original(work,paths,message,remote,branch)
            with patch.object(g,'commit_push',side_effect=race):
                g.collect(source,'id',runner=runner,clock=lambda:clock)
            self.assertEqual(len(calls),1)
            git(source,'fetch','origin','main')
            budget=json.loads(git(source,'show','FETCH_HEAD:'+g.BUDGET.as_posix()).stdout)
            self.assertEqual(budget['requests'],1)
            self.assertEqual(budget['reservations']['id']['status'],'complete')
            self.assertEqual(git(source,'show','FETCH_HEAD:keep.txt').stdout,'concurrent main data')
            self.assertEqual(git(source,'show','FETCH_HEAD:'+(g.ROOT/'performance/closing_odds/summary.json').as_posix()).returncode,0)
            self.assertTrue(list((source/'workflow_artifacts/closing-odds-recovery/observations').glob('*.json')))
            with self.assertRaises(ValueError):g.collect(source,'id',runner=runner,clock=lambda:clock)

    def test_collection_failure_still_publishes_checkpoint_and_recovery(self):
        with tempfile.TemporaryDirectory() as tmp:
            source,_,row,clock=seeded(tmp)
            def failed(cmd,cwd,check):
                c.collect_once(Path(cwd)/g.ROOT,None,clock,fetcher=lambda *args:payload(row,clock),reservation_id='fail')
                raise RuntimeError('Interrupted collector')
            with self.assertRaisesRegex(RuntimeError,'Interrupted'):
                g.collect(source,'fail',runner=failed,clock=lambda:clock)
            git(source,'fetch','origin','main')
            budget=json.loads(git(source,'show','FETCH_HEAD:'+g.BUDGET.as_posix()).stdout)
            self.assertEqual(budget['requests'],1)
            self.assertEqual(budget['reservations']['fail']['status'],'complete')

    def test_failed_publication_keeps_reserved_allowance_and_artifact(self):
        with tempfile.TemporaryDirectory() as tmp:
            source,_,row,clock=seeded(tmp);original=g.commit_push;calls=[]
            def runner(cmd,cwd,check):
                calls.append(cmd)
                c.collect_once(Path(cwd)/g.ROOT,None,clock,fetcher=lambda *args:payload(row,clock),reservation_id='fail')
            def denied(work,paths,message,remote,branch):
                return False if message.startswith('Publish') else original(work,paths,message,remote,branch)
            with patch.object(g,'commit_push',side_effect=denied),self.assertRaisesRegex(RuntimeError,'recover'):
                g.collect(source,'fail',runner=runner,clock=lambda:clock,attempts=2)
            self.assertEqual(len(calls),1)
            git(source,'fetch','origin','main')
            budget=json.loads(git(source,'show','FETCH_HEAD:'+g.BUDGET.as_posix()).stdout)
            self.assertEqual(budget['requests'],10)
            self.assertEqual(budget['reservations']['fail']['status'],'reserved')
            self.assertTrue((source/'workflow_artifacts/closing-odds-recovery/request_budget.json').exists())

    def test_empty_run_and_failed_reservation_make_no_api_calls(self):
        with tempfile.TemporaryDirectory() as tmp:
            source,_,_,clock=seeded(tmp)
            with patch.object(g,'commit_push',return_value=False):
                with self.assertRaisesRegex(RuntimeError,'no API calls'):
                    g.collect(source,'id',runner=lambda *a,**kw:self.fail('No collector allowed'),clock=lambda:clock,attempts=1)
            with patch.object(g,'plan',return_value={'ready':False}):
                self.assertFalse(g.collect(source,'id',clock=lambda:clock)['ready'])

    def test_plan_cli_gates_missing_secrets_and_workflow_is_serial_main_only(self):
        with tempfile.TemporaryDirectory() as tmp:
            base=Path(tmp);root=base/g.ROOT;root.mkdir();setup(root)
            output=base/'output';summary=base/'summary'
            with patch.dict(os.environ,{'GITHUB_OUTPUT':str(output),'GITHUB_STEP_SUMMARY':str(summary),
                    'THE_ODDS_API_KEY':'','THE_ODDS_API_KEY_FALLBACK_1':'','THE_ODDS_API_KEY_FALLBACK_2':''}):
                self.assertEqual(g.main(['plan','--repo',str(base)]),0)
            self.assertIn('ready=false',output.read_text());self.assertIn('SETUP REQUIRED',summary.read_text())
            with self.assertRaises(SystemExit):g.main(['collect'])
            with patch.object(g,'collect') as collect:
                self.assertEqual(g.main(['collect','--repo',str(base),'--reservation-id','id']),0)
                collect.assert_called_once()
        path=Path(__file__).resolve().parents[1]/'.github/workflows/closing-odds.yml'
        workflow=yaml.safe_load(path.read_text())
        self.assertFalse(workflow['concurrency']['cancel-in-progress'])
        self.assertEqual(workflow['permissions'],{'contents':'write'})
        self.assertEqual(workflow['jobs']['collect']['if'],"github.ref == 'refs/heads/main'")

    def test_environment_watch_exits_idle_and_carries_reservation(self):
        class API:
            KEY_ENV_NAMES=('THE_ODDS_API_KEY',)
            def __init__(self,*args,**kwargs):pass
        with tempfile.TemporaryDirectory() as tmp, patch('api_key_config.load_api_keys') as load,\
                patch('football_value_pipeline_v2_standalone.TheOddsAPI',API),\
                patch.dict(os.environ,{'THE_ODDS_API_KEY':'dummy'}),\
                patch.object(c,'collect_once',return_value={'requests':0,'reason':'NO_FIXTURES_IN_PRE_KICKOFF_WINDOW'}) as once,\
                patch.object(c,'pending_window',return_value=False),patch.object(c.time,'sleep') as sleep:
            self.assertEqual(c.main(['--root',tmp,'--watch','--stop-when-idle','--api-key-source','environment',
                                     '--budget-reservation','id']),0)
            load.assert_called_once_with('environment');sleep.assert_not_called()
            self.assertEqual(once.call_args.kwargs['reservation_id'],'id')

    def test_watcher_waits_only_for_in_scope_incomplete_targets(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);row,clock=setup(root)
            kick=g.utc(row['kickoff_utc'])
            self.assertTrue(c.pending_window(root,kick,clock))
            self.assertFalse(c.pending_window(root,clock+timedelta(seconds=20),clock))
            c.collect_once(root,None,clock,fetcher=lambda *args:payload(row,clock))
            self.assertFalse(c.pending_window(root,kick,clock))
            self.assertFalse(c.pending_window(root,kick+timedelta(minutes=5),kick))
