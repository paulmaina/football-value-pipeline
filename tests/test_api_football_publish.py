"""Publishing preserves concurrent source updates and durable free-plan accounting."""
from pathlib import Path
import shutil
import tempfile
import unittest
from unittest.mock import patch

from bbs_data import Store, atomic_json
from publish_api_football_data import publish, git
from tests.test_api_football import NOW, match
from api_football_data import normal_match


class PublishTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(); self.root = Path(self.temp.name)
        self.remote = self.root/'remote.git'; self.repo = self.root/'repo'; self.peer = self.root/'peer'
        git(self.root, 'init', '--bare', str(self.remote))
        git(self.root, 'init', '-b', 'main', str(self.repo))
        git(self.repo, 'config', 'user.name', 'test'); git(self.repo, 'config', 'user.email', 'test@example.test')
        (self.repo/'baseline.txt').write_text('primary data')
        git(self.repo, 'add', '.'); git(self.repo, 'commit', '-m', 'initial')
        git(self.repo, 'remote', 'add', 'origin', str(self.remote)); git(self.repo, 'push', '-u', 'origin', 'main')
        git(self.root, 'clone', '--branch', 'main', str(self.remote), str(self.peer))
        git(self.peer, 'config', 'user.name', 'test'); git(self.peer, 'config', 'user.email', 'test@example.test')
        self.cache = self.repo/'.football_cache/api_football'
        self.store = Store(self.cache/'state'); self.store.reserve(NOW, 80)
        self.store.put('match', 'EPL', '1', NOW.isoformat(), normal_match(match(), 'EPL', 2026, NOW.isoformat()))
        self.store.response('query', NOW.isoformat(), {'response': []})
        atomic_json(self.cache/'collection_status.json', {'collected_at_utc': NOW.isoformat(), 'status': 'complete'})

    def tearDown(self):
        self.temp.cleanup()

    def test_publish_retries_unrelated_push_race_and_stale_quota_cannot_overwrite(self):
        raced = []
        def racing(where, *args, **kwargs):
            if args[0] == 'push' and not raced:
                raced.append(True)
                (self.peer/'baseline.txt').write_text('corrected primary data')
                git(self.peer, 'add', '.'); git(self.peer, 'commit', '-m', 'concurrent primary correction')
                git(self.peer, 'push', 'origin', 'main')
            return git(where, *args, **kwargs)
        with patch('publish_api_football_data.git', side_effect=racing):publish(self.repo)
        git(self.peer, 'pull', '--ff-only')
        self.assertEqual((self.peer/'baseline.txt').read_text(), 'corrected primary data')
        saved = Store(self.peer/'.football_cache/api_football/state')
        self.assertEqual(saved.state['quota'][NOW.date().isoformat()], 1)
        self.assertEqual(len(saved.latest('match', NOW.isoformat())), 1)
        with self.assertRaisesRegex(RuntimeError, 'checkpoint advanced'):publish(self.repo)
        shutil.rmtree(self.cache)  # Remove generated untracked files in this temporary clone.
        git(self.repo, 'pull', '--ff-only')
        publish(self.repo)  # No-op publication is safe too.

    def test_failed_push_without_race_retains_recoverable_state(self):
        def denied(where, *args, **kwargs):
            if args[0] == 'push':
                from subprocess import CompletedProcess
                return CompletedProcess(args, 1, '', 'denied')
            return git(where, *args, **kwargs)
        with patch('publish_api_football_data.git', side_effect=denied):
            with self.assertRaisesRegex(RuntimeError, 'publication failed'):publish(self.repo)
        self.assertTrue((self.cache/'state/checkpoint.json').exists())

    def test_publication_stops_after_repeated_main_updates(self):
        attempt = []
        def racing(where, *args, **kwargs):
            if args[0] == 'push':
                attempt.append(True)
                (self.peer/'baseline.txt').write_text(str(len(attempt)))
                git(self.peer, 'add', '.'); git(self.peer, 'commit', '-m', 'concurrent change')
                git(self.peer, 'push', 'origin', 'main')
            return git(where, *args, **kwargs)
        with patch('publish_api_football_data.git', side_effect=racing):
            with self.assertRaisesRegex(RuntimeError, 'kept advancing'):publish(self.repo, attempts=2)
        self.assertEqual(len(attempt), 2)

    def test_symlink_response_is_rejected_and_cli_delegates(self):
        from publish_api_football_data import main
        with patch('publish_api_football_data.publish') as mocked:
            main(['--repo', str(self.repo)])
            mocked.assert_called_once_with(self.repo)
        file = self.cache/'state/responses/linked.json'
        try:file.symlink_to(self.repo/'baseline.txt')
        except OSError:self.skipTest('Symlinks unavailable for this Windows runner')
        with self.assertRaisesRegex(ValueError, 'Symlink'):publish(self.repo)
