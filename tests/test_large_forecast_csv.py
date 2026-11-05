"""Oversized research must survive generation, capture and standalone consumers."""
import csv
import hashlib
import io
import json
from pathlib import Path
import subprocess
import sys
import tempfile
from unittest.mock import patch

from offline_test_case import OfflineQuotePolicyTestCase
from test_performance_tracking import fixture, T0, KICK
import csv_utils
import performance_tracking as pt


def research_payload():
    # Includes UTF-8, embedded quotes, commas and newlines inside a quoted cell.
    return json.dumps({'evidence': 'Atlético, "team news"\n' * 16000}, ensure_ascii=False)


class LargeForecastCSVTests(OfflineQuotePolicyTestCase):
    def setUp(self):
        self.addCleanup(csv.field_size_limit, csv.field_size_limit())

    def test_actual_default_limit_failure_then_lossless_read_after_import(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp)/'all_leagues_predictions.csv'
            value = research_payload()
            self.assertGreater(len(value), 131072)
            row = dict(fixture(), team_research_json=value)
            pt.write_csv(path, [row], list(row))
            before = path.read_bytes()
            csv.field_size_limit(131072)
            with path.open(encoding='utf-8', newline='') as handle, self.assertRaises(csv.Error):
                list(csv.DictReader(handle))
            # Reset after imports: every supported reader must configure itself.
            csv.field_size_limit(131072)
            actual = pt.read_csv(path)
            self.assertEqual(actual[0]['team_research_json'], value)
            self.assertEqual(json.loads(actual[0]['team_research_json']), json.loads(value))
            self.assertEqual(path.read_bytes(), before)
            self.assertEqual(pt.read_csv(Path(tmp)/'absent.csv'), [])

    def test_windows_narrow_c_integer_overflow_falls_back(self):
        original = csv.field_size_limit
        attempts = []
        def narrow(value):
            attempts.append(value)
            if value > 2**31-1:
                raise OverflowError('C long is 32 bit')
            return original(value)
        # Simulate a 64-bit Python with Windows' 32-bit C long on every host.
        with patch.object(csv_utils.sys, 'maxsize', 2**63-1), patch.object(csv_utils.csv, 'field_size_limit', narrow):
            result = list(csv_utils.dict_reader(io.StringIO('field\nvalue\n')))
        self.assertEqual(result, [{'field': 'value'}])
        self.assertGreater(len(attempts), 1)
        self.assertLessEqual(attempts[-1], 2**31-1)
        self.assertGreater(attempts[-1], 131072)

    def test_generation_health_capture_and_snapshot_keep_large_evidence(self):
        from pipeline_health import write_generation_metadata
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)/'football_output_v2'
            raw = root/'raw'
            raw.mkdir(parents=True)
            row = dict(fixture(), team_research_json=research_payload())
            pt.write_csv(raw/'all_leagues_predictions.csv', [row], list(row))
            pt.write_csv(raw/'conservative_bet_shortlist.csv', [], ['league', 'kickoff_utc'])
            summary = {'generated_at_utc': T0.isoformat(), 'selection_policy_version': 'large-csv-regression', 'n_shortlisted': 0}
            pt.write_json(raw/'conservative_bet_summary.json', summary)
            before = (raw/'all_leagues_predictions.csv').read_bytes()
            csv.field_size_limit(131072)
            write_generation_metadata(raw, summary)  # Exact failing workflow path.
            metadata = json.loads((raw/'pipeline_run_metadata.json').read_text())
            self.assertEqual(metadata['predictions_sha256'], hashlib.sha256(before).hexdigest())
            csv.field_size_limit(131072)
            self.assertTrue(pt.capture('a'*40, root=root, captured_at=T0))
            csv.field_size_limit(131072)
            archive = pt.snapshots(root)
            self.assertEqual(len(archive), 1)
            self.assertEqual(archive[0][1][0]['team_research_json'], row['team_research_json'])
            frozen = root/'performance'/'snapshots'/('a'*16)/'predictions.csv'
            self.assertEqual(frozen.read_bytes(), before)

    def test_closing_plan_starts_in_fresh_process_with_large_current_and_archived_csv(self):
        from datetime import timedelta
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            row = dict(fixture(), odds_event_id='event1', team_research_json=research_payload())
            current = repo/'football_output_v2'/'raw'/'all_leagues_predictions.csv'
            archived = repo/'football_output_v2'/'performance'/'snapshots'/'one'/'predictions.csv'
            pt.write_csv(current, [row], list(row))
            pt.write_csv(archived, [row], list(row))
            script = '''import csv,json,sys
from datetime import datetime
from pathlib import Path
import github_closing_odds as g
csv.field_size_limit(131072)
print(json.dumps(g.plan(Path(sys.argv[1]),datetime.fromisoformat(sys.argv[2]))))
'''
            output = subprocess.run([sys.executable, '-c', script, str(repo), (KICK-timedelta(minutes=10)).isoformat()],
                                    cwd=Path(__file__).resolve().parents[1], capture_output=True, text=True, check=True)
            result = json.loads(output.stdout)
            self.assertTrue(result['ready'])
            self.assertEqual(result['upcoming_fixtures'], 1)

    def test_standalone_workbook_export_preserves_large_grade_fields(self):
        import performance_excel as pe
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            perf = root/'performance'
            row = {'market': 'Home win', 'research_details': research_payload()}
            pt.write_csv(perf/'shortlist_grades.csv', [row], list(row))
            pt.write_csv(perf/'prediction_grades.csv', [row], list(row))
            pt.write_json(perf/'metrics.json', {})
            csv.field_size_limit(131072)
            with patch.object(pe, 'write_workbook', return_value='written') as write:
                self.assertEqual(pe.export_existing(root), 'written')
            self.assertEqual(write.call_args.args[1][0]['research_details'], row['research_details'])
            self.assertEqual(write.call_args.args[2][0]['research_details'], row['research_details'])
