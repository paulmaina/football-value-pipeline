"""Shared CSV loading, restart budgets and race-safe publication regressions."""
import json
import tempfile
import unittest
from datetime import timedelta
from pathlib import Path
from unittest.mock import patch

import pandas as pd

from bbs_data import Store, Deferred
from bbs_integration import build_dataset, write_dataset, combined_training_history, read_combined
from publish_bbs_data import publish, git
from tests.test_bbs_data import NOW, match, base
from bbs_data import normal_match


class SharedCacheTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.cache = self.root/'.football_cache'
        self.store = Store(self.cache/'bbs/state')

    def tearDown(self):
        self.temp.cleanup()

    def add(self, row, observed=NOW):
        value = normal_match(row, 'EPL', observed.isoformat(), {})
        value['requested_season'] = 2026
        self.store.put('match', 'EPL', row['id'], observed.isoformat(), value)

    def export(self, cutoff=NOW):
        data = build_dataset(self.store, base(), cutoff.isoformat(), {'EPL': {'a2': 'Chelsea'}})
        data['report']['collection'] = {'status': 'complete'}
        return write_dataset(data, self.cache/'bbs/combined')

    def test_restart_quota_replay_and_idempotency(self):
        self.add(match())
        self.add(match())
        for _ in range(500):
            self.store.reserve(NOW, 500)
        reopened = Store(self.store.path)
        self.assertEqual(len(reopened.latest('match', NOW.isoformat())), 1)
        with self.assertRaises(Deferred):
            reopened.reserve(NOW, 500)
        reopened.reserve(NOW+timedelta(days=1), 500)
        self.add(match(hg=3), NOW+timedelta(hours=1))
        self.assertEqual(Store(self.store.path).latest('match', NOW.isoformat())[0]['payload']['score']['home'], 2)
        self.assertFalse(list(self.cache.rglob('*.sqlite3')))

    def test_csv_loader_adds_once_preserves_prices_and_primary_corrections(self):
        self.add(match())
        extra = match('m2', '2026-10-11')
        extra['away'] = {'id': 'a2', 'name': 'Chelsea'}
        self.add(extra)
        self.export()
        baseline = pd.DataFrame(base())
        baseline['Date'] = pd.to_datetime(baseline['Date'])
        baseline['B365H'] = 2.5
        combined = combined_training_history(baseline, self.cache, 'EPL', NOW, 3)
        self.assertEqual(len(combined), 2)
        self.assertEqual(combined.iloc[0]['B365H'], 2.5)
        self.assertTrue(pd.isna(combined.iloc[1]['B365H']))
        self.assertEqual(combined.iloc[1]['Season'], '2627')
        self.assertEqual(combined.iloc[0]['bbs_home_team_id'], 'h1')
        twice = combined_training_history(combined, self.cache, 'EPL', NOW, 3)
        self.assertEqual(len(twice), 2)
        baseline.loc[0, 'FTHG'] = 4
        changed = combined_training_history(baseline, self.cache, 'EPL', NOW, 3)
        self.assertEqual(changed.iloc[0]['FTHG'], 4)
        self.assertEqual(changed.iloc[0]['integration_status'], 'conflict')
        self.assertIn('result_or_status_conflict', changed.iloc[0]['bbs_conflict_flags'])

    def test_one_generation_earlier_cutoffs_rebuild_and_tampering_fails(self):
        # A rebuild reads the primary cache beside the BBS state, like the pipeline.
        (self.cache/'2627_E0.csv').write_text('Date,HomeTeam,AwayTeam,FTHG,FTAG,HS\n10/10/2026,Man United,Arsenal,2,1,8\n')
        self.add(match())
        current = self.export()
        self.assertEqual(read_combined(self.cache, 'EPL', (NOW-timedelta(seconds=1)).isoformat()), [])
        self.add(match(hg=3), NOW+timedelta(hours=1))
        latest = self.export(NOW+timedelta(hours=1))
        # One generation is kept: no timestamped copies accumulate.
        combined = self.cache/'bbs/combined'
        self.assertEqual(sorted(p.name for p in combined.iterdir()), ['generations', 'latest.json'])
        self.assertEqual([p.name for p in (combined/'generations').iterdir()], [latest.name])
        self.assertFalse(current.exists())
        current = latest
        later = read_combined(self.cache, 'EPL', (NOW+timedelta(hours=2)).isoformat())
        earlier = read_combined(self.cache, 'EPL', NOW.isoformat())
        # The earlier cutoff is rebuilt from immutable observations, before the correction.
        self.assertEqual(len(earlier), 1)
        self.assertNotEqual(earlier, later)
        self.assertEqual(earlier, read_combined(self.cache, 'EPL', NOW.isoformat()))
        (current/'EPL_enriched_history.csv').write_text('broken')
        with self.assertRaisesRegex(ValueError, 'checksum'):
            read_combined(self.cache, 'EPL', (NOW+timedelta(hours=2)).isoformat())

    def test_interrupted_publish_keeps_the_previous_generation_readable(self):
        import bbs_data
        self.add(match())
        self.export()
        before = read_combined(self.cache, 'EPL', (NOW+timedelta(hours=2)).isoformat())
        self.add(match(hg=3), NOW+timedelta(hours=1))
        original = bbs_data.atomic_json
        def interrupted(path, value):
            if Path(path).name == 'latest.json':
                raise OSError('interrupted before the manifest switch')
            return original(path, value)
        with patch('bbs_data.atomic_json', side_effect=interrupted), self.assertRaises(OSError):
            self.export(NOW+timedelta(hours=1))
        # The staged generation exists, but readers still get the previous one intact.
        self.assertEqual(read_combined(self.cache, 'EPL', (NOW+timedelta(hours=2)).isoformat()), before)
        # The next complete publish prunes the unused staged generation.
        newest = self.export(NOW+timedelta(hours=1))
        self.assertEqual([p.name for p in newest.parent.iterdir()], [newest.name])
        self.assertNotEqual(read_combined(self.cache, 'EPL', (NOW+timedelta(hours=2)).isoformat()), before)

    def test_reader_retries_once_when_a_concurrent_publish_prunes_its_generation(self):
        import bbs_integration, shutil
        self.add(match())
        old = self.export()
        stale = json.loads((self.cache/'bbs/combined/latest.json').read_text())
        self.add(match(hg=3), NOW+timedelta(hours=1))
        self.export(NOW+timedelta(hours=1))
        self.assertFalse(old.exists())
        reads = []
        import bbs_data
        original = bbs_data.decode
        def first_stale(text):
            value = original(text)
            if isinstance(value, dict) and 'generation' in value and not reads:
                reads.append(1)
                return stale
            return value
        with patch('bbs_data.decode', side_effect=first_stale):
            rows = read_combined(self.cache, 'EPL', (NOW+timedelta(hours=2)).isoformat())
        self.assertEqual(reads, [1])
        self.assertEqual(rows, read_combined(self.cache, 'EPL', (NOW+timedelta(hours=2)).isoformat()))
        shutil.rmtree(self.cache/'bbs/combined/generations')
        with self.assertRaises(FileNotFoundError):
            read_combined(self.cache, 'EPL', (NOW+timedelta(hours=2)).isoformat())

    def test_legacy_snapshots_still_serve_cutoffs_before_the_last_of_them(self):
        import hashlib, shutil
        from bbs_data import atomic_json
        self.add(match())
        current = self.export()
        rows = read_combined(self.cache, 'EPL', NOW.isoformat())
        legacy = self.cache/'bbs/combined/snapshots/old'
        shutil.copytree(current, legacy)
        stamp = (NOW+timedelta(hours=1)).isoformat()
        data = (legacy/'EPL_enriched_history.csv').read_bytes()
        atomic_json(legacy/'manifest.json', {'version': 1, 'cutoff_utc': NOW.isoformat(), 'generation': 'snapshots/old',
                                             'sha256': {'EPL_enriched_history.csv': hashlib.sha256(data).hexdigest()}})
        atomic_json(self.cache/'bbs/combined/snapshots/later/manifest.json',
                    {'version': 1, 'cutoff_utc': stamp, 'generation': 'snapshots/later', 'sha256': {}})
        self.add(match(hg=3), NOW+timedelta(hours=2))
        self.export(NOW+timedelta(hours=2))
        # Before the last legacy snapshot: read exactly as before, never rebuilt.
        with patch('bbs_integration._rebuilt_files', side_effect=AssertionError('rebuilt')):
            self.assertEqual(read_combined(self.cache, 'EPL', NOW.isoformat()), rows)
            self.assertEqual(read_combined(self.cache, 'EPL', (NOW-timedelta(seconds=1)).isoformat()), [])

    def test_pipeline_history_uses_shared_loader_without_collecting(self):
        from football_value_pipeline_v2_standalone import FootballValuePipelineV2, LEAGUES
        self.add(match())
        self.export()
        pipeline = FootballValuePipelineV2(cache_dir=self.cache)
        with patch.object(pipeline.source, 'history', return_value=pd.DataFrame(base())):
            rows = pipeline._history_for_league(LEAGUES['EPL'], NOW)
        self.assertEqual(rows.iloc[0]['bbs_match_id'], 'm1')

    def test_publish_rebuilds_on_latest_primary_cache_and_retries_push_race(self):
        remote = self.root/'remote.git'
        repo = self.root/'repo'
        peer = self.root/'peer'
        git(self.root, 'init', '--bare', str(remote))
        git(self.root, 'init', '-b', 'main', str(repo))
        git(repo, 'config', 'user.name', 'test')
        git(repo, 'config', 'user.email', 'test@example.test')
        cache = repo/'.football_cache'
        cache.mkdir()
        def primary(score):
            (cache/'2627_E0.csv').write_text(f'Date,HomeTeam,AwayTeam,FTHG,FTAG\n10/10/2026,Man United,Arsenal,{score},1\n')
        primary(2)
        git(repo, 'add', '.')
        git(repo, 'commit', '-m', 'initial')
        git(repo, 'remote', 'add', 'origin', str(remote))
        git(repo, 'push', '-u', 'origin', 'main')
        git(self.root, 'clone', '--branch', 'main', str(remote), str(peer))
        git(peer, 'config', 'user.name', 'test')
        git(peer, 'config', 'user.email', 'test@example.test')
        self.add(match())
        self.store.reserve(NOW, 500)
        self.export()
        import shutil
        shutil.copytree(self.cache/'bbs', cache/'bbs')
        original_git = git
        raced = []
        def racing_git(where, *args, **kwargs):
            if args[0] == 'push' and not raced:
                raced.append(True)
                (peer/'.football_cache/2627_E0.csv').write_text('Date,HomeTeam,AwayTeam,FTHG,FTAG\n10/10/2026,Man United,Arsenal,4,1\n')
                (peer/'unrelated.txt').write_text('preserved')
                original_git(peer, 'add', '.')
                original_git(peer, 'commit', '-m', 'concurrent correction')
                original_git(peer, 'push', 'origin', 'main')
            return original_git(where, *args, **kwargs)
        with patch('publish_bbs_data.git', side_effect=racing_git):
            publish(repo)
        git(peer, 'pull', '--ff-only')
        rows = read_combined(peer/'.football_cache', 'EPL', NOW.isoformat())
        self.assertEqual(rows[0]['FTHG'], '4')
        self.assertEqual(rows[0]['integration_status'], 'conflict')
        self.assertEqual((peer/'unrelated.txt').read_text(), 'preserved')
        self.assertTrue((peer/'.football_cache/bbs/state/checkpoint.json').exists())
        # A stale clone must not overwrite the newer request checkpoint.
        with self.assertRaisesRegex(RuntimeError, 'checkpoint advanced'):
            publish(repo)


if __name__ == '__main__':
    unittest.main()
