from offline_test_case import OfflineQuotePolicyTestCase
import json
import subprocess
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path
from unittest.mock import patch

import refresh_training_data as refresh

CLOCK = datetime(2026,10,12,tzinfo=timezone.utc)
HEADER = 'Div,Date,HomeTeam,AwayTeam,FTHG,FTAG\n'


def csv_data(rows='E0,11/10/2026,A,B,2,1\n'):
    return (HEADER+rows).encode()


def item(data):
    return {'league':'EPL','division':'E0','year':2026,
            'path':'.football_cache/2627_E0.csv','source_url':'test',
            'content':data,'matches':refresh.inspect_csv(data,'E0',2026,CLOCK)}


class RefreshTests(OfflineQuotePolicyTestCase):
    def test_validation_and_scheduled_rows(self):
        data=csv_data('E0,11/10/2026,A,B,0,0\nE0,18/10/2026,A,C,,\n')
        self.assertEqual(len(refresh.inspect_csv(data,'E0',2026,CLOCK)),1)
        for bad in [b'<html>failure</html>',csv_data(''),
                    csv_data('D1,11/10/2026,A,B,1,0\n'),
                    csv_data('E0,13/10/2026,A,B,1,0\n'),
                    csv_data('E0,11/10/2026,A,B,1,\n'),
                    csv_data('E0,11/10/2026,A,B,-1,0\n'),
                    csv_data('E0,11/10/2026,A,A,1,0\n'),
                    csv_data('E0,11/10/2026,A,B,1,0\n'*2)]:
            with self.subTest(bad=bad),self.assertRaises(ValueError):
                refresh.inspect_csv(bad,'E0',2026,CLOCK)

    def test_six_seasons_preserve_statistics_and_reject_season_or_result_mismatch(self):
        def fake(url):
            division=url.split('/')[-1][:-4]
            year=2000+int(url.split('/')[-2][:2])
            return f'Div,Date,HomeTeam,AwayTeam,FTHG,FTAG,FTR,HS,AS,HST,AST\n{division},01/09/{year},A,B,1,0,H,12,8,5,2\n'.encode()
        batch=refresh.fetch_batch(CLOCK,6,fake)
        self.assertEqual(len(batch),30)
        self.assertEqual({x['year'] for x in batch},set(range(2021,2027)))
        with tempfile.TemporaryDirectory() as tmp:
            entries=refresh.apply_batch(Path(tmp),batch,CLOCK)
            self.assertTrue(all(x['statistic_nonempty_rows']['HST']==1 for x in entries))
            self.assertEqual((Path(tmp)/batch[0]['path']).read_bytes(),batch[0]['content'])
        for data in [csv_data('E0,01/01/2026,A,B,1,0\n'),
                     b'Div,Date,HomeTeam,AwayTeam,FTHG,FTAG,FTR\nE0,11/10/2026,A,B,1,0,A\n']:
            with self.assertRaises(ValueError):refresh.inspect_csv(data,'E0',2026,CLOCK)

    def test_fetch_all_leagues_and_years_without_cache_fallback(self):
        def fake(url):
            division=url.split('/')[-1][:-4]
            year=2000+int(url.split('/')[-2][:2])
            return csv_data(f'{division},01/09/{year},A,B,1,0\n')
        batch=refresh.fetch_batch(CLOCK,4,fake)
        self.assertEqual(len(batch),20)
        self.assertEqual(len({x['path'] for x in batch}),20)
        with self.assertRaises(RuntimeError):
            refresh.fetch_batch(CLOCK,1,lambda url: (_ for _ in ()).throw(RuntimeError('offline')))

    def test_corrections_additions_and_status(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo=Path(tmp)
            first=item(csv_data())
            refresh.apply_batch(repo,[first],CLOCK)
            new=item(csv_data('E0,11/10/2026,A,B,3,1\nE0,12/10/2026,C,D,0,0\n'))
            result=refresh.apply_batch(repo,[new],CLOCK)[0]
            self.assertEqual(result['added_matches'],1)
            self.assertEqual(result['corrected_scores'],1)
            self.assertEqual((repo/new['path']).read_bytes(),new['content'])
            self.assertEqual(json.loads((repo/refresh.STATUS).read_text())['files'][0]['latest_completed_date'],'2026-10-12')
            self.assertEqual(refresh.apply_batch(repo,[new],CLOCK)[0]['download_status'],'unchanged')

    def test_batch_regression_leaves_every_file_untouched(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo=Path(tmp)
            old=item(csv_data('E0,10/10/2026,C,D,1,0\nE0,11/10/2026,A,B,2,1\n'))
            refresh.apply_batch(repo,[old],CLOCK)
            before={str(p.relative_to(repo)):p.read_bytes() for p in repo.rglob('*') if p.is_file()}
            valid=item(csv_data()); valid['path']='.football_cache/new.csv'
            with self.assertRaises(ValueError):
                refresh.apply_batch(repo,[valid,item(csv_data())],CLOCK)
            after={str(p.relative_to(repo)):p.read_bytes() for p in repo.rglob('*') if p.is_file()}
            self.assertEqual(before,after)

    def test_publish_retries_concurrent_commit_and_preserves_remote_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp); remote=root/'remote.git'; repo=root/'repo'; other=root/'other'
            def git(path,*args):
                return refresh.git(path,*args)
            subprocess.run(['git','init','--bare',str(remote)],check=True,capture_output=True)
            subprocess.run(['git','clone',str(remote),str(repo)],check=True,capture_output=True)
            for k,v in [('user.name','Test'),('user.email','test@example.test')]:git(repo,'config',k,v)
            git(repo,'checkout','-b','main')
            (repo/'README.md').write_text('preserve me')
            git(repo,'add','.');git(repo,'commit','-m','Initial');git(repo,'push','origin','main')
            subprocess.run(['git','clone','--branch','main',str(remote),str(other)],check=True,capture_output=True)
            git(other,'config','user.name','Test');git(other,'config','user.email','test@example.test')
            original=refresh.git; raced=False
            def race(path,*args,**kwargs):
                nonlocal raced
                if args[:3]==('push','origin','HEAD:refs/heads/main') and not raced:
                    raced=True
                    (other/'keep.txt').write_text('concurrent work')
                    original(other,'add','keep.txt');original(other,'commit','-m','Concurrent change')
                    original(other,'push','origin','main')
                return original(path,*args,**kwargs)
            with patch.object(refresh,'git',side_effect=race):
                refresh.publish(repo,[item(csv_data())],CLOCK)
            git(other,'pull','--ff-only')
            self.assertEqual((other/'keep.txt').read_text(),'concurrent work')
            self.assertEqual((other/'README.md').read_text(),'preserve me')
            # A Windows Git checkout can convert this mutable CSV to CRLF.
            # Assert preserved data independently of that representation.
            self.assertEqual((other/'.football_cache/2627_E0.csv').read_bytes().replace(b'\r\n',b'\n'),csv_data())
            self.assertTrue(raced)


if __name__=='__main__':
    unittest.main()
