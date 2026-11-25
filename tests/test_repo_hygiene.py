"""scripts/repo_hygiene.py: report-only listing of stale, unreferenced tracked files and ARCHIVED folders."""
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'scripts'))
import repo_hygiene  # noqa: E402


def git(repo, *args, date=None):
    env = {**os.environ, 'GIT_AUTHOR_NAME': 't', 'GIT_AUTHOR_EMAIL': 't@example.invalid',
           'GIT_COMMITTER_NAME': 't', 'GIT_COMMITTER_EMAIL': 't@example.invalid'}
    if date:
        env.update(GIT_AUTHOR_DATE=date, GIT_COMMITTER_DATE=date)
    subprocess.run(['git', '-C', str(repo), *args], check=True, capture_output=True, env=env,
                   stdin=subprocess.DEVNULL)


class RepoHygieneTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(); self.addCleanup(self.temp.cleanup)
        repo = self.repo = Path(self.temp.name)
        git(repo, 'init', '-q')
        (repo/'football_output_v2/performance/old_trial').mkdir(parents=True)
        (repo/'football_output_v2/performance/old_trial/big.csv').write_bytes(b'x' * 3_000_000)
        (repo/'football_output_v2/performance/live_report').mkdir(parents=True)
        (repo/'football_output_v2/performance/live_report/big.csv').write_bytes(b'y' * 3_000_000)
        (repo/'football_output_v2/performance/retired').mkdir(parents=True)
        (repo/'football_output_v2/performance/retired/report.md').write_text('> **ARCHIVED 2026-11-02.** Frozen.\n')
        (repo/'reader.py').write_text("OUTPUT = Path('football_output_v2') / 'performance' / 'live_report'\n")
        git(repo, 'add', '-A'); git(repo, 'commit', '-q', '-m', 'old', date='2026-01-01T00:00:00+00:00')
        (repo/'fresh.csv').write_bytes(b'z' * 3_000_000)
        git(repo, 'add', '-A'); git(repo, 'commit', '-q', '-m', 'new')

    def run_report(self, **kwargs):
        with patch.object(repo_hygiene, 'REPO', self.repo):
            return repo_hygiene.report(**kwargs)

    def test_lists_only_stale_unreferenced_large_paths_and_archived_folders(self):
        data = self.run_report(min_file_mb=1, min_folder_mb=2, stale_days=30)
        self.assertEqual([c['path'] for c in data['folders']], ['football_output_v2/performance/old_trial'])
        self.assertEqual(data['files'], [])  # the stale file is reported through its folder
        self.assertEqual(data['archived_folders'], ['football_output_v2/performance/retired'])
        text = repo_hygiene.markdown(data)
        self.assertIn('`football_output_v2/performance/old_trial`', text)
        self.assertNotIn('live_report', text)  # read by code
        self.assertNotIn('fresh.csv', text)  # changed recently

    def test_report_never_deletes_and_a_clean_tree_says_so(self):
        before = sorted(p.relative_to(self.repo).as_posix() for p in self.repo.rglob('*') if '.git' not in p.parts)
        self.run_report(min_file_mb=1, min_folder_mb=2, stale_days=30)
        after = sorted(p.relative_to(self.repo).as_posix() for p in self.repo.rglob('*') if '.git' not in p.parts)
        self.assertEqual(before, after)
        clean = self.run_report(min_file_mb=100, min_folder_mb=100, stale_days=30)
        clean['archived_folders'] = []
        self.assertIn('Nothing to review.', repo_hygiene.markdown(clean))

    def test_workflow_is_monthly_report_only_and_posts_an_issue(self):
        import yaml
        workflow = yaml.safe_load((Path(__file__).resolve().parents[1]/'.github/workflows/repo-hygiene.yml').read_text())
        self.assertEqual(workflow['permissions'], {'contents': 'read', 'issues': 'write'})
        triggers = workflow.get('on', workflow.get(True))
        self.assertEqual(triggers['schedule'], [{'cron': '17 6 1 * *'}])
        text = (Path(__file__).resolve().parents[1]/'.github/workflows/repo-hygiene.yml').read_text()
        self.assertIn('scripts/repo_hygiene.py', text)
        self.assertIn('gh issue create', text)
        for forbidden in ('git rm', 'git push', 'git commit', 'rm -'):
            self.assertNotIn(forbidden, text)


if __name__ == '__main__':
    unittest.main()
