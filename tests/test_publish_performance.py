from offline_test_case import OfflineQuotePolicyTestCase
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from publish_performance import SNAPSHOTS, git, merge_snapshots, publish


class PublisherTests(OfflineQuotePolicyTestCase):
    def test_conflicting_snapshot_fails_closed(self):
        with tempfile.TemporaryDirectory() as d:
            a, b = Path(d) / 'a', Path(d) / 'b'
            a.mkdir(); b.mkdir()
            (a / 'metadata.json').write_text('original')
            (b / 'metadata.json').write_text('changed')
            with self.assertRaisesRegex(ValueError, 'Immutable snapshot conflict'):
                merge_snapshots(a, b)
            self.assertEqual((b / 'metadata.json').read_text(), 'changed')

    def test_stale_checkout_and_push_race_preserve_remote_and_snapshots(self):
        with tempfile.TemporaryDirectory() as d:
            base = Path(d)
            remote, event, other = [base / x for x in ('remote.git', 'event', 'other')]
            subprocess.run(['git', 'init', '--bare', str(remote)], check=True, capture_output=True)
            subprocess.run(['git', 'clone', str(remote), str(event)], check=True, capture_output=True)
            git(event, 'checkout', '-b', 'main')
            for key, value in [('user.name', 'Test'), ('user.email', 'test@example.com')]:
                git(event, 'config', key, value)
            (event / 'baseline.txt').write_text('unchanged model')
            old = event / SNAPSHOTS / 'old'
            old.mkdir(parents=True); (old / 'metadata.json').write_text('original')
            git(event, 'add', '.'); git(event, 'commit', '-m', 'baseline')
            git(event, 'push', 'origin', 'main')
            subprocess.run(['git', 'clone', '-b', 'main', str(remote), str(other)], check=True, capture_output=True)
            for key, value in [('user.name', 'Test'), ('user.email', 'test@example.com')]:
                git(other, 'config', key, value)
            # Another process publishes newer reports and a new snapshot first.
            newest = other / SNAPSHOTS / 'remote'
            newest.mkdir(); (newest / 'metadata.json').write_text('remote original')
            (other / 'newer.txt').write_text('preserve me')
            git(other, 'add', '.'); git(other, 'commit', '-m', 'new remote work')
            git(other, 'push', 'origin', 'main')
            captured = event / SNAPSHOTS / 'captured'
            captured.mkdir(); (captured / 'metadata.json').write_text('capture timestamp')
            marker = base / 'race-done'
            reviewer = base / 'review.py'
            reviewer.write_text('''from pathlib import Path
import subprocess
import sys
other, marker = Path(sys.argv[1]), Path(sys.argv[2])
root = Path('football_output_v2/performance')
root.mkdir(parents=True, exist_ok=True)
(root / 'metrics.json').write_text('new reports; race=' + str(Path('race.txt').exists()))
if not marker.exists():
    (other / 'race.txt').write_text('concurrent user change')
    for args in [('add', '.'), ('commit', '-m', 'race'), ('push', 'origin', 'main')]:
        subprocess.run(['git', '-C', str(other), *args], check=True, capture_output=True)
    marker.write_text('done')
''')
            publish(event, review_command=[sys.executable, str(reviewer), str(other), str(marker)])
            git(other, 'pull', '--ff-only')
            self.assertEqual((other / 'baseline.txt').read_text(), 'unchanged model')
            self.assertEqual((other / 'newer.txt').read_text(), 'preserve me')
            self.assertEqual((other / 'race.txt').read_text(), 'concurrent user change')
            self.assertEqual((other / SNAPSHOTS / 'old/metadata.json').read_text(), 'original')
            self.assertEqual((other / SNAPSHOTS / 'captured/metadata.json').read_text(), 'capture timestamp')
            self.assertEqual((other / SNAPSHOTS / 'remote/metadata.json').read_text(), 'remote original')
            self.assertEqual((other / 'football_output_v2/performance/metrics.json').read_text(), 'new reports; race=True')
            # The original checkout, including pending captures, is untouched.
            self.assertFalse((event / 'newer.txt').exists())
            self.assertTrue(captured.exists())

class PublisherValidationTests(OfflineQuotePolicyTestCase):
    def test_failed_validation_blocks_push_and_retains_attempt_reports(self):
        with tempfile.TemporaryDirectory() as tmp:
            base=Path(tmp);remote=base/'remote.git';repo=base/'event'
            subprocess.run(['git','init','--bare',str(remote)],check=True,capture_output=True)
            subprocess.run(['git','clone',str(remote),str(repo)],check=True,capture_output=True)
            git(repo,'checkout','-b','main')
            git(repo,'config','user.name','CI Test');git(repo,'config','user.email','ci@example.com')
            (repo/'baseline.txt').write_text('keep')
            git(repo,'add','.');git(repo,'commit','-m','baseline');git(repo,'push','origin','main')
            initial=git(repo,'rev-parse','HEAD').stdout.strip()
            reviewer=base/'review.py'
            reviewer.write_text("from pathlib import Path\np=Path('football_output_v2/performance');p.mkdir(parents=True)\n(p/'metrics.json').write_text('{}')\n")
            diagnostics=repo/'workflow_artifacts';diagnostics.mkdir();(diagnostics/'preflight.json').write_text('keep preflight')
            with self.assertRaises(subprocess.CalledProcessError):
                publish(repo,review_command=[sys.executable,str(reviewer)],
                    validation_command=[sys.executable,'-c','raise SystemExit(3)'],artifact_dir=Path('workflow_artifacts'))
            self.assertEqual(git(repo,'ls-remote','origin','refs/heads/main').stdout.split()[0],initial)
            self.assertEqual((diagnostics/'performance/metrics.json').read_text(),'{}')
            self.assertEqual((diagnostics/'preflight.json').read_text(),'keep preflight')
            self.assertFalse((repo/'football_output_v2/performance/metrics.json').exists())

    def test_artifact_destination_cannot_overwrite_checkout_or_escape_it(self):
        with tempfile.TemporaryDirectory() as tmp:
            for destination in (Path('.'),Path('../workflow_artifacts'),Path('football_output_v2')):
                with self.assertRaisesRegex(ValueError,'Artifact destination'):
                    publish(Path(tmp),artifact_dir=destination)


if __name__ == '__main__':
    unittest.main()
