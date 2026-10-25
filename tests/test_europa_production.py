"""Europa cache integrity, exact identity and production risk gates."""
import copy
from datetime import datetime, timedelta, timezone
import json
from pathlib import Path
import tempfile
from unittest import TestCase
from unittest.mock import patch, Mock

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

    def test_refresh_uses_archived_period_facts_without_any_live_uefa_request(self):
        source = Path(__file__).resolve().parents[1]/'docs/audits/europa-uefa-attestations.json'
        facts = json.loads(source.read_text(encoding='utf-8'))['seasons']
        client = Mock()
        response = Mock(status_code=200, content=b'irrelevant input')
        client.get.return_value = response
        with tempfile.TemporaryDirectory() as directory, patch(
                'europa_training.reconcile', return_value=(snapshot()['matches'], {})) as reconcile, patch(
                'europa_training.audit_cornerflick', return_value=({'verified_for_research': True}, [])) as audit:
            payload = europa.refresh(directory, NOW, session=client)
            self.assertEqual(reconcile.call_args.kwargs['official_rows'], facts['2025']['matches'])
            self.assertEqual(audit.call_args.kwargs, {})
            self.assertFalse(any('uefa.com' in call.args[0] for call in client.get.call_args_list))
            self.assertEqual(payload['official_source_health']['2025']['status'], 'REVIEWED_HISTORICAL_FACTS')
            self.assertFalse((Path(directory)/'europa/sources/uefa-2026.html').exists())

    def test_committed_current_sources_refresh_without_any_uefa_html(self):
        import shutil
        with tempfile.TemporaryDirectory() as directory:
            sources = Path(directory)/'europa/sources'
            shutil.copytree(europa.ROOT/'.football_cache/europa/sources', sources)
            for html in sources.glob('uefa-*.html'):
                html.unlink()
            payload = europa.refresh(directory, datetime(2026, 10, 25, tzinfo=timezone.utc), download=False)
            audit = payload['current_audit']
            self.assertTrue(audit['verified_for_research'])
            self.assertGreater(audit['league_phase_rows'], 36)
            self.assertEqual(audit['league_phase_rows'], audit['fixture_download_completed_rows'])
            self.assertEqual(audit['verification_sources'], ['Cornerflick', 'Fixture Download'])
            self.assertFalse(any('uefa.com' in url for url in payload['sources'].values()))
            self.assertTrue(all(row['source'] == 'Cornerflick + Fixture Download'
                                for row in payload['matches'] if row['season'] == 2026))

    def test_current_results_need_no_uefa_file_or_attestation(self):
        from scripts.europa_research import audit_cornerflick
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            (base/'fixture-2026.csv').write_text('Date,Home Team,Away Team,Result,Round Number\n'
                '01/10/2026 19:00,Roma,Lyon,1 - 0,2\n')
            (base/'cornerflick.json').write_text(json.dumps({'competition': {'slug': 'europa-league'},
                'meta': {'match_count': 1}, 'matches': [{'round': 'League Stage - 2',
                'kickoff_at': '2026-10-01T19:00:00+00:00', 'status': 'finished',
                'home_score': 1, 'away_score': 0, 'home_team': 'Roma', 'away_team': 'Lyon'}]}))
            audit, rows = audit_cornerflick(base, europa.resolver(), NOW)
            self.assertTrue(audit['verified_for_research'])
            self.assertEqual(audit['verification_sources'], ['Cornerflick', 'Fixture Download'])
            self.assertEqual(audit['unverified_identities'], [])


class EuropaForecastAvailabilityTests(TestCase):
    def test_unverified_europa_excluded_without_using_old_snapshot(self):
        with patch('europa_training.load', side_effect=ValueError('coverage incomplete')) as load:
            leagues, status = europa.forecast_availability(['EPL', 'UEL', 'PrimeiraLiga'], 'cache', NOW)
        load.assert_called_once_with('cache', NOW)
        self.assertEqual(leagues, ['EPL', 'PrimeiraLiga'])
        self.assertEqual(status['excluded_leagues']['UEL']['status'], 'TRAINING_UNVERIFIED')
        self.assertEqual(status['requested_leagues'], ['EPL', 'UEL', 'PrimeiraLiga'])

    def test_verified_europa_automatically_rejoins(self):
        with patch('europa_training.load', return_value=pd.DataFrame()):
            leagues, status = europa.forecast_availability(['EPL', 'UEL'], 'cache', NOW)
        self.assertEqual(leagues, ['EPL', 'UEL'])
        self.assertEqual(status['excluded_leagues'], {})

    def test_europa_only_failure_still_fails_instead_of_publishing_empty_run(self):
        with patch('europa_training.load', side_effect=ValueError('unverified')):
            with self.assertRaisesRegex(ValueError, 'No requested leagues'):
                europa.forecast_availability(['UEL'], 'cache', NOW)

    def test_other_leagues_do_not_access_europa_and_programming_errors_propagate(self):
        with patch('europa_training.load', side_effect=AssertionError('bug')) as load:
            leagues, _ = europa.forecast_availability(['EPL'], 'cache', NOW)
            self.assertEqual(leagues, ['EPL'])
            load.assert_not_called()
            with self.assertRaises(AssertionError):
                europa.forecast_availability(['UEL', 'EPL'], 'cache', NOW)
