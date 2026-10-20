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
