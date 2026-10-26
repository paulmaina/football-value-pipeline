"""Interrupted generation, batch uploads and immutable current-run reads."""
from datetime import timedelta
import json
from pathlib import Path
import tempfile
from unittest.mock import patch

from offline_test_case import OfflineQuotePolicyTestCase
from test_performance_tracking import fixture, pick, T0, KICK, final, MockSession
from test_prediction_run_tracking import save_run
import prediction_runs as runs
from performance_tracking import snapshots, frozen_rows, review, write_json
from pipeline_health import write_generation_metadata
from workflow_checks import raw_check, archive_check, report_check


def populate(staging, clock, *, price=1.5, market='Home win'):
    selection = dict(pick(market=market), offered_decimal_odds=price)
    save_run(staging.parent, clock, [fixture()], [selection])
    summary = json.loads((staging/'conservative_bet_summary.json').read_text())
    summary['selection_policy_version'] = 'publication-regression'
    write_json(staging/'conservative_bet_summary.json', summary)
    from test_graded_candidates import sample_report
    write_json(staging/'EPL_goal_market_validation.json',
               {**sample_report(), 'league': fixture()['league']})
    write_generation_metadata(staging, summary)
    (staging/'EPL_predictions.csv').write_bytes((staging/'all_leagues_predictions.csv').read_bytes())


def publish(root, clock=T0, **kwargs):
    with runs.stage_run(root/'raw') as staging:
        populate(staging, clock, **kwargs)
        raw_check(staging.parent)
        return runs.publish_run(staging, root/'raw')


class PublicationTests(OfflineQuotePolicyTestCase):
    def test_two_local_runs_one_upload_preserve_both_and_grade_latest(self):
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp)
            first=publish(root)
            second=publish(root,T0+timedelta(hours=1),price=3.,market='Away win')
            self.assertNotEqual(first,second)
            self.assertEqual(runs.resolve_raw(root/'raw'),second)
            self.assertEqual(len(list((root/'raw/prediction_runs').iterdir())),2)
            clock=T0+timedelta(hours=2)
            self.assertEqual(runs.capture_runs(root,'a'*40,captured_at=clock),2)
            # Another upload cannot duplicate a run or reset its capture clock.
            self.assertEqual(runs.capture_runs(root,'b'*40,captured_at=clock+timedelta(minutes=1)),0)
            archive=snapshots(root)
            self.assertEqual(len(archive),2)
            self.assertEqual(len(frozen_rows(archive,'shortlist',all_runs=True)),2)
            self.assertEqual(frozen_rows(archive,'shortlist')[0]['market'],'Home win')
            self.assertEqual(len({m['git_commit_sha'] for m,_,_ in archive}),2)
            for meta,_,_ in archive:
                self.assertEqual(meta['source_git_commit_sha'],'a'*40)
                self.assertEqual(__import__('performance_tracking').utc(meta['captured_at_utc']),clock)
            self.assertEqual(len(archive_check(root)['snapshots']),2)
            result=review(root=root,token='fake',clock=KICK+timedelta(days=1),session=MockSession([final()]))
            self.assertEqual(result['tracked_prediction_runs'],2)
            self.assertEqual(result['shortlist']['losses'],1)
            self.assertEqual(report_check(root)['shortlist']['graded'],1)

    def test_local_saved_time_cannot_backdate_late_cloud_capture(self):
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp);publish(root)
            self.assertEqual(runs.capture_runs(root,'a'*40,captured_at=KICK-timedelta(minutes=19)),0)
            self.assertEqual(snapshots(root),[])

    def test_same_generation_is_reused_and_archived_content_cannot_be_relabelled(self):
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp);first=publish(root)
            self.assertEqual(publish(root),first)
            self.assertEqual(len(list((root/'raw/prediction_runs').iterdir())),1)
            runs.capture_runs(root,'a'*40,captured_at=T0)
            meta=snapshots(root)[0][0]
            directory=root/'performance/snapshots'/meta['archive_id'][:16]
            file=directory/'shortlist.csv'
            file.write_bytes(file.read_bytes().replace(b'1.5',b'2.5'))
            metadata=json.loads((directory/'metadata.json').read_bytes())
            metadata['sha256']['shortlist.csv']=runs.digest(file.read_bytes())
            write_json(directory/'metadata.json',metadata)
            with self.assertWarnsRegex(UserWarning,'Unbound prediction-run archive'):
                self.assertEqual(snapshots(root),[])
            with self.assertRaisesRegex(ValueError,'content mismatch'):
                archive_check(root)

    def test_bundle_manifest_cannot_drop_required_files_or_escape_directory(self):
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp);bundle=publish(root)
            manifest=json.loads((bundle/runs.MANIFEST).read_bytes())
            def replace_manifest(changed):
                identity={k:changed[k] for k in ('version','generated_at_utc','sha256')}
                changed['run_id']=runs.digest(runs.encoded(identity))
                write_json(bundle/runs.MANIFEST,changed)
            missing=json.loads(json.dumps(manifest))
            del missing['sha256']['all_leagues_predictions.csv']
            replace_manifest(missing)
            with self.assertRaisesRegex(ValueError,'Incomplete'):
                runs.validate_bundle(bundle)
            unsafe=json.loads(json.dumps(manifest));unsafe['sha256']['../escape']='a'*64
            replace_manifest(unsafe)
            with self.assertRaisesRegex(ValueError,'Unsafe'):
                runs.validate_bundle(bundle)
            write_json(bundle/runs.MANIFEST,manifest)
            metadata={'git_commit_sha':'a'*40,'prediction_run_id':manifest['run_id'],
                      'archive_id':'b'*40}
            with self.assertRaisesRegex(ValueError,'archive identity'):
                runs.archive_identity(metadata,'b'*16)

    def test_windows_lock_denial_retries_and_releases_writer(self):
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp);lock=root/'raw/.prediction-run.lock'
            original=Path.rmdir;denials=[]
            def remove(path):
                if path==lock and len(denials)<2:
                    denials.append(path)
                    raise PermissionError(5,'Access is denied',str(path))
                return original(path)
            with patch.object(Path,'rmdir',remove), patch.object(runs.time,'sleep') as delay:
                first=publish(root)
            self.assertEqual(delay.call_count,2)
            self.assertFalse(lock.exists())
            self.assertEqual(runs.resolve_raw(root/'raw'),first)
            publish(root,T0+timedelta(hours=1))

    def test_persistent_lock_denial_preserves_success_and_original_failure(self):
        from football_value_pipeline_v2_standalone import main
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp);lock=root/'raw/.prediction-run.lock'
            original=Path.rmdir
            def remove(path):
                if path==lock:raise PermissionError(5,'Access is denied',str(path))
                return original(path)
            def generate(argv):
                populate(Path(argv[-1]),T0)
                return 0
            with patch.object(Path,'rmdir',remove), patch.object(runs.time,'sleep'):
                with patch('football_value_pipeline_v2_standalone._generate_main',side_effect=generate):
                    with self.assertLogs('prediction_runs',level='WARNING'):
                        self.assertEqual(main(['--out-dir',str(root/'raw')]),0)
                self.assertTrue(lock.exists())
                bundle=runs.resolve_raw(root/'raw')
                self.assertEqual(raw_check(root)['forecasts'],1)
                with self.assertRaisesRegex(RuntimeError,'Another prediction writer'):
                    with runs.stage_run(root/'raw'):pass
                original(lock)  # Explicit recovery after the previous writer stopped.
                with patch('football_value_pipeline_v2_standalone._generate_main',
                           side_effect=ValueError('original model failure')):
                    with self.assertLogs('prediction_runs',level='WARNING'):
                        with self.assertRaisesRegex(ValueError,'original model failure'):
                            main(['--out-dir',str(root/'raw')])
                self.assertEqual(runs.resolve_raw(root/'raw'),bundle)

    def test_failed_model_run_never_changes_current_or_legacy_outputs(self):
        from football_value_pipeline_v2_standalone import main
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp);first=publish(root)
            pointer=(root/'raw/current_run.json').read_bytes()
            original=(root/'raw/EPL_predictions.csv').read_bytes()
            def fail(argv):
                staging=Path(argv[-1]);(staging/'EPL_predictions.csv').write_text('new partial data')
                raise RuntimeError('Second league provider failed')
            with patch('football_value_pipeline_v2_standalone._generate_main',side_effect=fail):
                with self.assertRaisesRegex(RuntimeError,'Second league'):
                    main(['--out-dir',str(root/'raw'),'--leagues','EPL','LaLiga'])
            self.assertEqual((root/'raw/current_run.json').read_bytes(),pointer)
            self.assertEqual((root/'raw/EPL_predictions.csv').read_bytes(),original)
            self.assertEqual(runs.resolve_raw(root/'raw'),first)
            self.assertFalse((root/'raw/.prediction-run.lock').exists())

    def test_failure_during_projection_restores_previous_completed_run(self):
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp);first=publish(root)
            original=(root/'raw/EPL_predictions.csv').read_bytes()
            history=root/'raw/shortlist_history/same.csv'
            history.parent.mkdir();history.write_text('existing history')
            original_write=runs.atomic_write
            def fail(path,data):
                if path==root/'raw/current_run.json':raise OSError('locked pointer')
                return original_write(path,data)
            with runs.stage_run(root/'raw') as staging:
                populate(staging,T0+timedelta(hours=1),price=2.)
                (staging/'shortlist_history').mkdir()
                (staging/'shortlist_history/same.csv').write_text('replacement history')
                with patch.object(runs,'atomic_write',side_effect=fail):
                    with self.assertRaisesRegex(OSError,'locked pointer'):
                        runs.publish_run(staging,root/'raw')
            self.assertEqual(runs.resolve_raw(root/'raw'),first)
            self.assertEqual((root/'raw/EPL_predictions.csv').read_bytes(),original)
            self.assertEqual(history.read_text(),'existing history')
            # Completed second bundle survives for later publication/capture.
            self.assertEqual(len(list((root/'raw/prediction_runs').iterdir())),2)

    def test_readers_use_complete_bundle_even_if_compatibility_copy_is_interrupted(self):
        from format_football_output import main as formatter
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp);publish(root)
            (root/'raw/all_leagues_predictions.csv').write_text('partial projection')
            self.assertEqual(raw_check(root)['forecasts'],1)
            self.assertEqual(formatter(['--root-dir',str(root)]),0)
            self.assertTrue(runs.capture_runs(root,'a'*40,captured_at=T0))

    def test_tamper_unsafe_pointer_and_writer_overlap_fail_closed(self):
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp);bundle=publish(root)
            with runs.stage_run(root/'raw'):
                with self.assertRaisesRegex(RuntimeError,'Another prediction writer'):
                    with runs.stage_run(root/'raw'):pass
            pointer=root/'raw/current_run.json';original=pointer.read_bytes()
            for data in ({'version':1,'run_id':'../escape'},
                         {**json.loads(original),'manifest_sha256':'bad'}):
                pointer.write_text(json.dumps(data))
                with self.assertRaises(ValueError):runs.resolve_raw(root/'raw')
            pointer.write_bytes(original)
            file=bundle/'all_leagues_predictions.csv';file.write_text('changed')
            with self.assertRaisesRegex(ValueError,'checksum'):
                runs.capture_runs(root,'a'*40,captured_at=T0)

    def test_legacy_read_and_seeded_refresh_do_not_delete_unrelated_files(self):
        from refresh_conservative_shortlist import refresh
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp);raw=root/'raw';raw.mkdir()
            self.assertEqual(runs.resolve_raw(raw),raw)
            (raw/'notes.txt').write_text('keep')
            (raw/'EPL_backtest_predictions.csv').write_text('historical research')
            publish(root)
            self.assertEqual((raw/'notes.txt').read_text(),'keep')
            self.assertTrue((raw/'EPL_backtest_predictions.csv').exists())
            # Re-ranking is also a complete, separately preserved generation.
            refresh(root,as_of=T0+timedelta(minutes=1))
            self.assertEqual(len(list((raw/'prediction_runs').iterdir())),2)
            self.assertEqual(raw_check(root)['forecasts'],1)


class PruneCapturedRunsTests(OfflineQuotePolicyTestCase):
    """Retention deletes only captured, non-current bundles and fails safe."""

    def runs_on_disk(self, root):
        return sorted(p.name for p in (root/'raw/prediction_runs').iterdir())

    def test_keeps_current_and_uncaptured_runs_and_capture_still_succeeds(self):
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp)
            first=publish(root);second=publish(root,T0+timedelta(hours=1),price=2.)
            self.assertEqual(runs.capture_runs(root,'a'*40,captured_at=T0+timedelta(hours=2)),2)
            third=publish(root,T0+timedelta(hours=3),price=2.5)
            current=publish(root,T0+timedelta(hours=4),price=3.)
            self.assertEqual(sorted(runs.prune_captured_runs(root)),sorted([first.name,second.name]))
            self.assertEqual(self.runs_on_disk(root),sorted([third.name,current.name]))
            self.assertEqual(runs.resolve_raw(root/'raw'),current)
            self.assertEqual(list(root.glob('.prediction-prune-*')),[])
            # The current run is kept even once captured; capture skips nothing it needs.
            self.assertEqual(runs.capture_runs(root,'b'*40,captured_at=T0+timedelta(hours=5)),2)
            self.assertEqual(runs.prune_captured_runs(root),[third.name])
            self.assertEqual(self.runs_on_disk(root),[current.name])
            self.assertEqual(runs.prune_captured_runs(root),[])
            self.assertEqual(runs.capture_runs(root,'c'*40,captured_at=T0+timedelta(hours=6)),0)
            self.assertEqual(len(snapshots(root)),4)
            self.assertEqual(len(archive_check(root)['snapshots']),4)

    def captured_old_run(self, root):
        """An older, captured run plus a current one; returns the older run's snapshot."""
        old=publish(root);publish(root,T0+timedelta(hours=1),price=2.)
        self.assertEqual(runs.prune_captured_runs(root),[])  # Nothing captured yet.
        runs.capture_runs(root,'a'*40,captured_at=T0+timedelta(hours=2))
        return root/'performance/snapshots'/runs.digest(('prediction-run:'+old.name).encode())[:16]

    def test_missing_or_unreadable_snapshots_delete_nothing(self):
        def missing(base): base.rename(base.with_name('moved'))
        def not_a_directory(base):
            missing(base);base.write_text('not a directory')
        damages={'missing folder':lambda s: missing(s.parent),
                 'folder is a file':lambda s: not_a_directory(s.parent),
                 'no metadata':lambda s: (s/'metadata.json').unlink(),
                 'corrupt metadata':lambda s: (s/'metadata.json').write_text('{corrupt'),
                 'metadata not an object':lambda s: (s/'metadata.json').write_text('[]'),
                 'tampered predictions':lambda s: (s/'predictions.csv').write_text('tampered'),
                 'no run manifest':lambda s: (s/'run_manifest.json').unlink()}
        for name,damage in damages.items():
            with self.subTest(name),tempfile.TemporaryDirectory() as temp:
                root=Path(temp);snapshot=self.captured_old_run(root)
                before=self.runs_on_disk(root)
                damage(snapshot)
                self.assertEqual(runs.prune_captured_runs(root),[])
                self.assertEqual(self.runs_on_disk(root),before)

    def test_missing_or_corrupt_pointer_deletes_nothing(self):
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp);self.captured_old_run(root)
            pointer=root/'raw/current_run.json';original=pointer.read_bytes()
            for data in (b'{corrupt',b'[]',json.dumps({'version':1}).encode(),
                         json.dumps({'version':1,'run_id':'../escape'}).encode(),
                         json.dumps({'version':1,'run_id':7}).encode()):
                pointer.write_bytes(data)
                self.assertEqual(runs.prune_captured_runs(root),[])
            pointer.unlink()
            self.assertEqual(runs.prune_captured_runs(root),[])
            self.assertEqual(len(self.runs_on_disk(root)),2)
            pointer.write_bytes(original)
            self.assertEqual(len(runs.prune_captured_runs(root)),1)


class StaleLockTests(OfflineQuotePolicyTestCase):
    """A writer killed before its finally block must not block later runs forever."""

    def lock_with(self, root, owner):
        lock = root/'raw'/runs.LOCK
        lock.mkdir(parents=True)
        if owner is not None:
            (lock/runs.LOCK_OWNER).write_text(json.dumps(owner))
        return lock

    def dead_pid(self):
        import subprocess, sys
        return int(subprocess.run([sys.executable, '-c', 'import os;print(os.getpid())'],
                                  capture_output=True, text=True, check=True).stdout)

    def test_process_start_token_tracks_live_and_exited_processes(self):
        import os
        token = runs.process_start_token(os.getpid())
        self.assertIsNotNone(token)
        self.assertEqual(runs.process_start_token(os.getpid()), token)
        self.assertIsNone(runs.process_start_token(self.dead_pid()))

    def test_lock_of_killed_writer_is_reclaimed_and_run_publishes(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            owner = {**runs.lock_owner(), 'pid': self.dead_pid()}
            lock = self.lock_with(root, owner)
            with self.assertLogs('prediction_runs', level='WARNING') as logs:
                bundle = publish(root)
            self.assertIn('no longer running', logs.output[0])
            self.assertEqual(runs.resolve_raw(root/'raw'), bundle)
            self.assertFalse(lock.exists())
            self.assertEqual([p.name for p in (root/'raw').iterdir() if p.name.startswith(runs.LOCK)], [])

    def test_recycled_pid_is_stale_but_live_owner_and_other_host_block(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            live = runs.lock_owner()
            lock = self.lock_with(root, live)
            with self.assertRaisesRegex(RuntimeError, r'Another prediction writer is active \(pid'):
                with runs.stage_run(root/'raw'): pass
            self.assertTrue((lock/runs.LOCK_OWNER).exists())  # A blocked writer never removes it.
            # PID namespaces / restricted process metadata may return 'running'.
            # Exercise recycled-PID logic with a known, readable start token.
            with patch.object(runs, 'process_start_token', return_value='newer-process'):
                self.assertIn('reused', runs.stale_lock_reason(lock, json.dumps(
                    {**live, 'process_started': 'an-earlier-process'}).encode()))
            with patch.object(runs, 'process_start_token', return_value='running'):
                self.assertIsNone(runs.stale_lock_reason(lock, json.dumps(live).encode()))
            elsewhere = json.dumps({**live, 'host': 'another-machine', 'pid': self.dead_pid()}).encode()
            self.assertIsNone(runs.stale_lock_reason(lock, elsewhere))

    def test_ownerless_lock_waits_for_grace_period_then_is_reclaimed(self):
        import os, time
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            lock = self.lock_with(root, None)
            with self.assertRaisesRegex(RuntimeError, r'Another prediction writer is active\.'):
                with runs.stage_run(root/'raw'): pass
            old = time.time() - runs.OWNERLESS_LOCK_GRACE_SECONDS - 60
            os.utime(lock, (old, old))
            with self.assertLogs('prediction_runs', level='WARNING'):
                with runs.stage_run(root/'raw'):
                    owner = json.loads((lock/runs.LOCK_OWNER).read_text())
                    self.assertEqual(owner['pid'], os.getpid())
            self.assertFalse(lock.exists())
            self.assertEqual(runs.stale_lock_reason(lock, None), 'lock already removed')

    def test_lock_replaced_after_staleness_check_is_untouched(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            lock = self.lock_with(root, runs.lock_owner())
            judged = json.dumps({**runs.lock_owner(), 'pid': self.dead_pid()}).encode()
            self.assertFalse(runs._discard_stale_lock(lock, judged))
            self.assertTrue((lock/runs.LOCK_OWNER).exists())
            self.assertTrue(runs._discard_stale_lock(root/'raw'/'missing.lock', judged))
            self.assertEqual(sorted(p.name for p in (root/'raw').iterdir()), [runs.LOCK])

    def test_owner_record_failure_releases_new_lock(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root/'raw').mkdir()
            with patch.object(runs, 'atomic_write', side_effect=OSError('disk full')):
                with self.assertRaisesRegex(OSError, 'disk full'):
                    runs.acquire_lock(root/'raw')
            self.assertFalse((root/'raw'/runs.LOCK).exists())


class LockGuardRegressionTests(OfflineQuotePolicyTestCase):
    def test_new_ownerless_directory_is_not_removed_by_old_stale_judgement(self):
        import os, time
        with tempfile.TemporaryDirectory() as tmp:
            raw = Path(tmp)
            lock = raw/runs.LOCK
            lock.mkdir()
            old = time.time() - runs.OWNERLESS_LOCK_GRACE_SECONDS - 10
            os.utime(lock, (old, old))
            judged = runs._read_owner(lock)
            self.assertIsNotNone(runs.stale_lock_reason(lock, judged))
            lock.rmdir()
            lock.mkdir()  # A different writer just created its ownerless lock.
            with runs.lock_guard(raw):
                self.assertFalse(runs._discard_stale_lock(lock, judged))
            self.assertTrue(lock.is_dir())

    def test_recovery_and_owner_initialization_exclude_other_processes(self):
        import os, subprocess, sys, time
        with tempfile.TemporaryDirectory() as tmp:
            raw = Path(tmp)
            lock = raw/runs.LOCK
            lock.mkdir()
            old = time.time() - runs.OWNERLESS_LOCK_GRACE_SECONDS - 10
            os.utime(lock, (old, old))
            script = """
import sys
from pathlib import Path
import prediction_runs as runs
print('ready', flush=True)
try:
    runs.acquire_lock(Path(sys.argv[1]))
except RuntimeError as exc:
    print(str(exc), flush=True)
else:
    raise AssertionError('second writer acquired a live lock')
"""
            with runs.lock_guard(raw):
                child = subprocess.Popen([sys.executable, '-c', script, str(raw)],
                                         stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                try:
                    self.assertEqual(child.stdout.readline().strip(), 'ready')
                    time.sleep(0.15)
                    self.assertIsNone(child.poll())
                    with self.assertLogs('prediction_runs', level='WARNING'):
                        acquired = runs._acquire_lock(raw)
                except BaseException:
                    child.kill(); child.communicate()
                    raise
            try:
                out, err = child.communicate(timeout=15)
                self.assertEqual(child.returncode, 0, err)
                self.assertIn('Another prediction writer is active', out)
                self.assertEqual(json.loads((lock/runs.LOCK_OWNER).read_bytes())['pid'], os.getpid())
            finally:
                if child.poll() is None:
                    child.kill(); child.communicate()
                runs.release_lock(acquired)
            self.assertTrue((raw/runs.LOCK_GUARD).exists())
            with runs.stage_run(raw, seed=True) as staging:
                self.assertFalse((staging/runs.LOCK_GUARD).exists())

    def test_guard_failure_and_release_do_not_mask_run_outcome(self):
        import errno, os
        with tempfile.TemporaryDirectory() as tmp:
            raw = Path(tmp)
            target = 'msvcrt.locking' if os.name == 'nt' else 'fcntl.flock'
            with patch(target, side_effect=BlockingIOError(errno.EAGAIN, 'busy')), patch.object(
                    runs.time, 'monotonic', side_effect=[0, 11]):
                with self.assertRaisesRegex(RuntimeError, 'metadata is busy'):
                    with runs.lock_guard(raw): pass
            with patch(target, side_effect=OSError(errno.EIO, 'disk error')):
                with self.assertRaises(OSError):
                    with runs.lock_guard(raw): pass
            with patch.object(runs, 'lock_guard', side_effect=OSError('unavailable')):
                with self.assertLogs('prediction_runs', level='WARNING'):
                    runs.release_lock(raw/runs.LOCK)
