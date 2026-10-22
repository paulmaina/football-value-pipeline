"""Europa cache integrity, exact identity and production risk gates."""
import copy
from datetime import datetime, timedelta, timezone
import json
from pathlib import Path
import tempfile
from unittest import TestCase
from unittest.mock import patch

import pandas as pd

import europa_training as europa
from football_value_pipeline_v2_standalone import DixonColesModel, FootballValuePipelineV2, LEAGUES
from performance_tracking import fixture_match, collect_results
from pipeline_health import current_health

NOW = datetime(2026, 10, 22, tzinfo=timezone.utc)


def snapshot():
    rows = [{'date': (NOW-timedelta(days=40-i)).date().isoformat(),
             'home': 'roma', 'away': 'lyon', 'regulation': [i % 3, i % 2],
             'reported': [i % 3, i % 2], 'season': 2026} for i in range(30)]
    return {'schema_version': 1, 'score_basis': 'REGULATION_90_MINUTES',
            'verified_at_utc': NOW.isoformat(), 'matches': rows}


class EuropaProductionTests(TestCase):
    def test_verified_cache_is_the_only_training_source(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory)/'europa/training.json'
            path.parent.mkdir(); path.write_text(json.dumps(snapshot()))
            pipe = FootballValuePipelineV2(cache_dir=directory)
            with patch.object(pipe.source, 'history', side_effect=AssertionError('domestic leak')):
                history = pipe._history_for_league(LEAGUES['UEL'], NOW)
            self.assertEqual(len(history), 30)
            self.assertEqual(history.iloc[0].FTHG, 0)
            self.assertEqual(history.attrs['training_seasons_requested'], 1)

    def test_invalid_scores_duplicates_and_future_rows_fail_closed(self):
        for mutation in ('score', 'date', 'duplicate', 'basis'):
            payload = snapshot()
            if mutation == 'score': payload['matches'][0]['regulation'] = [True, 1]
            if mutation == 'date': payload['matches'][0]['date'] = '2027-01-01'
            if mutation == 'duplicate': payload['matches'].append(payload['matches'][0])
            if mutation == 'basis': payload['score_basis'] = 'EXTRA_TIME'
            with self.subTest(mutation=mutation), self.assertRaises(ValueError): europa.frame(payload, NOW)

    def test_stale_refresh_failure_preserves_previous_snapshot(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory)/'europa/training.json'; path.parent.mkdir()
            old = snapshot(); old['verified_at_utc'] = (NOW-timedelta(days=2)).isoformat()
            text = json.dumps(old); path.write_text(text)
            with patch('europa_training.refresh', side_effect=ValueError('sources disagree')):
                with self.assertRaisesRegex(ValueError, 'sources disagree'): europa.load(directory, NOW)
            self.assertEqual(path.read_text(), text)

    def test_refreshed_snapshot_used_and_future_refresh_stamp_not_trusted(self):
        with tempfile.TemporaryDirectory() as directory:
            with patch('europa_training.refresh', return_value=snapshot()) as refresh:
                self.assertEqual(len(europa.load(directory, NOW)), 30)
                refresh.assert_called_once()
        payload = snapshot(); payload['verified_at_utc'] = (NOW+timedelta(hours=1)).isoformat()
        self.assertFalse(europa.fresh(payload, NOW))

    def test_aliases_are_exact_and_unseen_clubs_do_not_get_fuzzy_identity(self):
        model = DixonColesModel(bbs_statistics=False).fit(europa.frame(snapshot(), NOW))
        model.league_key = 'UEL'
        self.assertEqual(model.resolve_team('Roma'), ('roma', 100.0))
        self.assertEqual(model.resolve_team('Romaa'), (None, 0.0))
        self.assertEqual(model.team_training_counts['roma'], 30)

    def test_six_appearance_gate_is_europa_only(self):
        row = {'league': 'UEFA Europa League', 'home_training_matches': 6, 'away_training_matches': 5}
        self.assertTrue(europa.eligibility(row))
        row['away_training_matches'] = 6
        self.assertEqual(europa.eligibility(row), [])
        row['home_training_matches'] = float('nan')
        self.assertTrue(europa.eligibility(row))
        row['league'] = 'Premier League'
        self.assertEqual(europa.eligibility(row), [])

    def test_utc_fixture_window_and_result_exclusion(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory)/'europa/sources/fixture-2026.csv'; path.parent.mkdir(parents=True)
            path.write_text('Match Number,Round Number,Date,Location,Home Team,Away Team,Result\n'
                            '1,3,22/10/2026 19:00,Rome,Roma,Lyon,\n'
                            '2,3,21/10/2026 19:00,Rome,Roma,Lyon,1 - 0\n')
            rows = europa.fixtures(directory, NOW, 2)
            self.assertEqual(len(rows), 1)
            self.assertEqual(rows.iloc[0].kickoff_utc, '2026-10-22T19:00:00+00:00')

    def test_grading_requires_exact_europa_identity(self):
        row = {'league': 'UEFA Europa League', 'home_team': 'Roma', 'away_team': 'Lyon', 'kickoff_utc': NOW.isoformat()}
        result = {'league_code': 'EL', 'home_team': 'roma', 'away_team': 'lyon', 'kickoff_utc': NOW.isoformat()}
        self.assertEqual(fixture_match(row, [result])[1], 'VERIFIED_FINISHED')
        result['home_team'] = 'romaa'
        self.assertEqual(fixture_match(row, [result])[1], 'UNVERIFIED_FIXTURE_OR_RESULT')

    def test_refresh_conflict_does_not_replace_snapshot(self):
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)/'europa'; sources = base/'sources'; sources.mkdir(parents=True)
            old = json.dumps(snapshot()); (base/'training.json').write_text(old)
            with patch('europa_training.reconcile', return_value=(snapshot()['matches'], {})), patch(
                'europa_training.audit_cornerflick', return_value=({'verified_for_research': False}, [])):
                with self.assertRaisesRegex(ValueError, 'prior snapshot retained'):
                    europa.refresh(directory, NOW, download=False)
            self.assertEqual((base/'training.json').read_text(), old)

    def test_europa_results_route_does_not_need_football_data_org_token(self):
        row = {'league': 'UEFA Europa League', 'kickoff_utc': (NOW-timedelta(days=1)).isoformat()}
        result = {'match_id': 'uel-1', 'league_code': 'EL', 'source': 'corroborated'}
        with tempfile.TemporaryDirectory() as directory, patch(
                'europa_training.results', return_value=[result]) as fetch, patch(
                'performance_tracking.fetch_verified', side_effect=AssertionError('wrong provider')):
            root = Path(directory)/'football_output_v2'
            verified, errors = collect_results([row], root=root, token='', clock=NOW)
            self.assertEqual(verified[0]['source'], 'corroborated')
            fetch.assert_called_once_with(root.parent/'.football_cache', NOW)

    def test_current_health_rechecks_europa_cache_freshness(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)/'football_output_v2'; raw = root/'raw'; raw.mkdir(parents=True)
            (raw/'UEL_diagnostics.json').write_text(json.dumps({'training_end': '2026-10-15',
                'training_matches': 696, 'training_data_health': {'status': 'VERIFIED_WITHIN_24_HOURS'}}))
            cache = root.parent/'.football_cache/europa/training.json'; cache.parent.mkdir(parents=True)
            cache.write_text(json.dumps(snapshot()))
            self.assertEqual(current_health(root, NOW)['training']['UEL']['current_source_health']['status'],
                             'VERIFIED_WITHIN_24_HOURS')
            self.assertEqual(current_health(root, NOW+timedelta(days=2))['training']['UEL']['current_source_health']['status'], 'STALE')
            cache.unlink()
            self.assertEqual(current_health(root, NOW)['training']['UEL']['current_source_health']['status'], 'DOWNLOAD_NOT_VERIFIED')
