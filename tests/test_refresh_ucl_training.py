import json
from pathlib import Path
import subprocess
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch
import refresh_ucl_training as refresh
from refresh_training_data import git
from test_daily_health import payload, NOW


class UCLPublisherTests(unittest.TestCase):
    def test_publish_retries_main_race_and_keeps_unrelated_work(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);remote=root/'remote.git';repo=root/'repo';other=root/'other'
            subprocess.run(['git','init','--bare',str(remote)],check=True,capture_output=True)
            subprocess.run(['git','clone',str(remote),str(repo)],check=True,capture_output=True)
            git(repo,'config','user.name','Test');git(repo,'config','user.email','test@example.test')
            git(repo,'checkout','-b','main');(repo/'keep.txt').write_text('original')
            git(repo,'add','.');git(repo,'commit','-m','Initial');git(repo,'push','origin','main')
            subprocess.run(['git','clone','--branch','main',str(remote),str(other)],check=True,capture_output=True)
            git(other,'config','user.name','Test');git(other,'config','user.email','test@example.test')
            raced=False
            def race(path,*args,**kwargs):
                nonlocal raced
                if args[:3]==('push','origin','HEAD:refs/heads/main') and not raced:
                    raced=True;(other/'concurrent.txt').write_text('keep concurrent work')
                    git(other,'add','.');git(other,'commit','-m','Concurrent');git(other,'push','origin','main')
                return git(path,*args,**kwargs)
            with patch.object(refresh,'git',side_effect=race):
                status=refresh.publish(repo,payload(),2026,NOW)
            git(other,'pull','--ff-only')
            self.assertTrue(raced);self.assertEqual(status['completed_matches'],1)
            self.assertEqual((other/'keep.txt').read_text(),'original')
            self.assertEqual((other/'concurrent.txt').read_text(),'keep concurrent work')
            self.assertEqual(len(json.loads((other/'.football_cache/fdorg_history_UCL_2026.json').read_text())['matches']),2)
            self.assertNotIn('ucl-publish',git(repo,'worktree','list').stdout)
            # Publishing errors leave main unchanged and clean up temporary worktrees.
            old=git(repo,'ls-remote','origin','refs/heads/main').stdout
            def reject(path,*args,**kwargs):
                if args[:3]==('push','origin','HEAD:refs/heads/main'):
                    return SimpleNamespace(returncode=1)
                return git(path,*args,**kwargs)
            with patch.object(refresh,'git',side_effect=reject),self.assertRaisesRegex(RuntimeError,'publish failed'):
                refresh.publish(repo,payload(),2026,NOW.replace(minute=1))
            self.assertEqual(git(repo,'ls-remote','origin','refs/heads/main').stdout,old)
            with self.assertRaisesRegex(RuntimeError,'kept advancing'):
                refresh.publish(repo,payload(),2026,NOW,attempts=0)

    def test_cli_uses_explicit_key_source_and_local_or_published_update(self):
        with tempfile.TemporaryDirectory() as tmp:
            for publish in (False,True):
                args=['refresh_ucl_training.py','--repo',tmp,'--api-key-source','environment']+(['--publish'] if publish else [])
                with patch('sys.argv',args),patch.object(refresh,'load_api_keys') as load,patch.dict('os.environ',{'FOOTBALL_DATA_API_KEY':'secret'}),patch.object(refresh,'fetch_payload',return_value=payload()) as fetch,patch.object(refresh,'apply_payload',return_value={'completed_matches':1,'latest_completed_date':'2026-10-08','added_matches':1,'coverage_status':'CURRENT_WITHIN_PROVIDER_SCHEDULE'}) as apply,patch.object(refresh,'publish',return_value={'completed_matches':1,'latest_completed_date':'2026-10-08','added_matches':1,'coverage_status':'CURRENT_WITHIN_PROVIDER_SCHEDULE'}) as pub:
                    refresh.main()
                    load.assert_called_once_with('environment');self.assertEqual(fetch.call_args.args[0],'secret')
                    self.assertEqual(pub.called,publish);self.assertEqual(apply.called,not publish)


if __name__=='__main__':unittest.main()
