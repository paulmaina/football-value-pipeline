"""Synthetic exports exercise joins without redistributing provider data."""
import csv
from datetime import datetime, timezone
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from scripts.compare_europa_history import alias_map, compare


class EuropaHistoryComparisonTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.fd = self.root / 'fd.csv'
        self.fs = self.root / 'fs.csv'

    def write(self, path, rows):
        with path.open('w', newline='', encoding='utf-8') as stream:
            writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
            writer.writeheader()
            writer.writerows(rows)

    def fixture(self, **changes):
        return dict({'Date': '17/04/2025 19:00', 'Home Team': 'Club A',
                     'Away Team': 'Club B', 'Result': '5 - 4'}, **changes)

    def footy(self, **changes):
        stamp = int(datetime(2025, 4, 17, 19, tzinfo=timezone.utc).timestamp())
        return dict({'timestamp': str(stamp), 'status': 'complete',
                     'team_a_name': 'Club A', 'team_b_name': 'Club B',
                     'home_team_goal_count': '2', 'away_team_goal_count': '2'}, **changes)

    def run_comparison(self, left, right, aliases=None):
        self.write(self.fd, left)
        self.write(self.fs, right)
        return compare(self.fd, self.fs, 2024, aliases)

    def test_conflicting_reported_scores_never_become_training_approval(self):
        r = self.run_comparison([self.fixture()], [self.footy()])
        self.assertEqual(r['matched_unique_identities'], 1)
        self.assertEqual(r['score_conflicts'], [{'fixture_download_line': 2, 'footystats_line': 2}])
        self.assertFalse(r['regulation_time_verified'])
        self.assertEqual(r['training_rows_written'], 0)
        r = self.run_comparison([self.fixture()], [self.footy(home_team_goal_count='5', away_team_goal_count='4')])
        self.assertEqual(r['reported_scores_agree'], 1)
        self.assertFalse(r['regulation_time_verified'])

    def test_explicit_aliases_and_same_utc_date_join_without_fuzzy_guessing(self):
        left = [self.fixture(**{'Home Team': 'Short A'})]
        right = [self.footy()]
        self.assertEqual(self.run_comparison(left, right)['matched_unique_identities'], 0)
        r = self.run_comparison(left, right, {'Short A': 'Club A'})
        self.assertEqual(r['matched_unique_identities'], 1)
        self.assertEqual(r['footystats_only_candidates'], 0)

    def test_duplicate_on_either_side_quarantines_even_conflicting_scores(self):
        for left, right in [([self.fixture(), self.fixture(Result='1 - 0')], [self.footy()]),
                            ([self.fixture()], [self.footy(), self.footy()])]:
            r = self.run_comparison(left, right)
            self.assertEqual(r['matched_unique_identities'], 0)
            self.assertEqual(r['ambiguous_identities_quarantined'], 1)
            self.assertEqual(r['footystats_only_candidates'], 0)

    def test_skip_incomplete_and_reject_bad_scores_and_wrong_season(self):
        r = self.run_comparison([self.fixture()], [self.footy(status='incomplete'),
            self.footy(home_team_goal_count='-1'), self.footy(timestamp='0')])
        self.assertEqual(r['footystats']['skipped'], {'not_complete': 1})
        self.assertEqual(r['footystats']['rejected'], {'invalid_required_fields': 1, 'outside_season': 1})

    def test_different_dates_and_reversed_teams_remain_unmatched(self):
        r = self.run_comparison([self.fixture()], [self.footy(team_a_name='Club B', team_b_name='Club A')])
        self.assertEqual(r['matched_unique_identities'], 0)
        r = self.run_comparison([self.fixture(Date='18/04/2025 19:00')], [self.footy()])
        self.assertEqual(r['footystats_only_candidates'], 1)

    def test_kickoff_difference_does_not_hide_score_comparison(self):
        r = self.run_comparison([self.fixture(Date='17/04/2025 20:00')], [self.footy()])
        self.assertEqual(len(r['kickoff_differences']), 1)
        self.assertEqual(len(r['score_conflicts']), 1)

    def test_schema_and_alias_errors_fail_explicitly(self):
        self.write(self.fd, [self.fixture()])
        self.write(self.fs, [{'wrong': 'schema'}])
        with self.assertRaisesRegex(ValueError, 'schema'):
            compare(self.fd, self.fs, 2024)
        with self.assertRaises(ValueError):
            alias_map({'A': 'B', 'B': 'C'})
        with self.assertRaises(ValueError):
            alias_map({'A': 'B', 'a': 'C'})

    def test_cli_writes_only_aggregate_report_and_preserves_inputs(self):
        self.run_comparison([self.fixture()], [self.footy()])
        before = [p.read_bytes() for p in (self.fd, self.fs)]
        output = self.root / 'result.json'
        cmd = [sys.executable, 'scripts/compare_europa_history.py',
               '--fixture-download', str(self.fd), '--footystats', str(self.fs),
               '--season-start-year', '2024', '--output', str(output)]
        subprocess.run(cmd, check=True, capture_output=True)
        report = json.loads(output.read_text())
        self.assertEqual(report['training_rows_written'], 0)
        self.assertNotIn('Club A', output.read_text())
        self.assertEqual(before, [p.read_bytes() for p in (self.fd, self.fs)])
        cmd[-1] = str(self.fs)
        self.assertNotEqual(subprocess.run(cmd, capture_output=True).returncode, 0)
        self.assertEqual(before[1], self.fs.read_bytes())
