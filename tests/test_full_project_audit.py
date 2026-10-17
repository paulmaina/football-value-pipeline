"""Training, quote joins and archive failures reproduced by the project audit."""
from datetime import timedelta
import json
from pathlib import Path
import tempfile
from unittest.mock import Mock, patch

import numpy as np
import pandas as pd

from offline_test_case import OfflineQuotePolicyTestCase
from football_value_pipeline_v2_standalone import (
    DixonColesModel, FootballDataUK, FootballValuePipelineV2, LEAGUES,
    pick_best_price, read_csv_bytes,
)
from tests.test_model_correctness import history
from tests.test_performance_tracking import T0, SHA, fixture, pick
from performance_tracking import capture, snapshots, frozen_rows


class TrainingAuditTests(OfflineQuotePolicyTestCase):
    def test_bad_completed_rows_fail_before_the_optimizer(self):
        for field, value in [('HomeTeam', ''), ('HomeTeam', None), ('Date', 'bad'),
                             ('Date', None), ('FTAG', None), ('FTAG', 'bad')]:
            data = history().astype({field: object})
            data.loc[0, field] = value
            with self.subTest(field=field, value=value), patch(
                    'football_value_pipeline_v2_standalone.minimize') as optimizer:
                with self.assertRaises(ValueError):
                    DixonColesModel().fit(data)
                optimizer.assert_not_called()
        data = history(); data.loc[0, 'AwayTeam'] = data.loc[0, 'HomeTeam']
        with self.assertRaisesRegex(ValueError, 'Same team'):
            DixonColesModel().fit(data)
        data = pd.concat([history(), history().iloc[:1]], ignore_index=True)
        with self.assertRaisesRegex(ValueError, 'duplicate completed'):
            DixonColesModel().fit(data)

    def test_partial_or_nonnumeric_source_scores_do_not_silently_disappear(self):
        with tempfile.TemporaryDirectory() as tmp:
            provider = FootballDataUK(tmp)
            for score in (None, 'unavailable'):
                data = history().astype({'FTAG': object})
                data.loc[0, 'FTAG'] = score
                with self.subTest(score=score), patch.object(provider, 'season', return_value=data):
                    with self.assertRaisesRegex(ValueError, 'Invalid completed goals'):
                        provider.history(LEAGUES['EPL'], 1, T0)
            data = history().astype({'FTAG': object, 'FTHG': object})
            data.loc[0, ['FTHG', 'FTAG']] = None
            with patch.object(provider, 'season', return_value=data):
                self.assertEqual(len(provider.history(LEAGUES['EPL'], 1, T0)), len(data)-1)

    def test_overwide_csv_row_is_not_silently_skipped(self):
        with self.assertRaises(pd.errors.ParserError):
            read_csv_bytes(b'a,b\n1,2\n3,4,5\n')

    def test_invalid_model_parameters_are_rejected(self):
        for kwargs in ({'half_life_days': float('nan')}, {'half_life_days': float('inf')},
                       {'l2': float('nan')}, {'l2': -1}, {'max_goals': 5.5},
                       {'max_goals': True}, {'max_goals': 101}):
            with self.subTest(kwargs=kwargs), self.assertRaises(ValueError):
                DixonColesModel(**kwargs)

    def test_reviewed_model_aliases_resolve_without_changing_archive_keys(self):
        from football_value_pipeline_v2_standalone import canonical_team_key
        model = DixonColesModel()
        model.teams = ['PAE AEK', 'Racing Club de Lens']
        model.team_to_idx = {team: i for i, team in enumerate(model.teams)}
        model.attack = model.weakness = np.zeros(2)
        model.base = model.home_adv = model.rho = 0.
        original_key = canonical_team_key('AEK Athens')
        model.league_key = 'UCL'
        self.assertEqual(model.resolve_team('AEK Athens'), ('PAE AEK', 100.))
        self.assertEqual(model.resolve_team('RC Lens'), ('Racing Club de Lens', 100.))
        self.assertEqual(canonical_team_key('AEK Athens'), original_key)
        model.league_key = 'EPL'
        self.assertIsNone(model.resolve_team('AEK Athens')[0])

    def test_shadow_comparisons_share_production_clock_and_league(self):
        from tests.test_model_reliability_experiment import inputs, ToyModel
        from model_reliability_experiment import generate_league
        from recency_experiment import generate_league as recency_generate
        from tests.test_recency_experiment import predictions, history as recency_history, tuning, ToyModel as RecencyModel
        origins = []
        class ClockModel(ToyModel):
            def fit(self, data, as_of=None):
                origins.append(as_of)
                return super().fit(data)
        data, frame = inputs()
        report = generate_league(data, frame, ClockModel, half_life=240, l2=.08,
                                max_goals=10, as_of=T0.isoformat())
        self.assertEqual(origins, [pd.Timestamp(T0)]*2)
        self.assertEqual(report[0]['training_as_of_utc'], T0.isoformat())
        recency_origins = []
        class ClockRecencyModel(RecencyModel):
            def fit(self, data, as_of=None):
                recency_origins.append(as_of)
                return super().fit(data)
        recency_generate(predictions(), recency_history(), ClockRecencyModel, tuning(),
            league='Premier League', production_half_life=240, l2=.08, max_goals=10,
            as_of=T0.isoformat())
        self.assertEqual(recency_origins, [pd.Timestamp(T0)])

    def test_production_and_backtest_fits_use_prediction_origins(self):
        original = DixonColesModel.fit
        with tempfile.TemporaryDirectory() as tmp, patch.dict('os.environ', {}, clear=True):
            pipeline = FootballValuePipelineV2(cache_dir=tmp, live_odds=False)
            with patch.object(pipeline, '_history_for_league', return_value=history()), patch.object(
                    pipeline, '_current_fixtures', return_value=pd.DataFrame()), patch.object(
                    DixonColesModel, 'fit', autospec=True, side_effect=original) as fit:
                _, diagnostics, _ = pipeline.run_league('EPL', now=T0)
                self.assertEqual(fit.call_args.kwargs['as_of'], pd.Timestamp(T0))
                self.assertEqual(diagnostics['training_as_of_utc'], T0.isoformat())
                self.assertEqual(diagnostics['training_data_provenance']['bbs_added_results'], 0)
            with patch.object(DixonColesModel, 'fit', autospec=True, side_effect=original) as fit:
                pipeline.backtest_league('EPL', test_start='2024-03-01', step_days=7,
                    min_train=30, now=T0, history_override=history())
                self.assertGreater(fit.call_count, 1)
                for call in fit.call_args_list:
                    self.assertLess(call.args[1]['Date'].max(), call.kwargs['as_of'])

    def test_best_opening_price_is_highest_valid_available_price(self):
        from bbs_integration import training_provenance
        report = training_provenance(pd.DataFrame({'bbs_match_id': ['good', 'bad'],
            'integration_status': ['matched', 'conflict']}))
        self.assertEqual(report['bbs_confirmed_rows'], 1)
        self.assertEqual(report['bbs_result_conflicts'], 1)
        row = pd.Series({'PSH': 1.8, 'B365H': 2.1, 'AvgH': 1.9, 'MaxH': np.nan})
        self.assertEqual(pick_best_price(row, ['MaxH', 'PSH', 'B365H', 'AvgH']), 2.1)
        self.assertIsNone(pick_best_price(pd.Series({'PSH': 'bad'}), ['MaxH', 'PSH']))

    def test_current_csv_refreshes_once_and_rejects_poisoned_or_regressed_download(self):
        header = 'Div,Date,HomeTeam,AwayTeam,FTHG,FTAG\n'
        old = (header+'E0,01/09/2026,A,B,1,0\n').encode()
        new = old+b'E0,02/09/2026,C,D,0,0\n'
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp)/'2627_E0.csv'; path.write_bytes(old)
            provider = FootballDataUK(tmp)
            response = Mock(content=new)
            with patch.object(provider.http.session, 'get', return_value=response) as get:
                self.assertEqual(len(provider.season(LEAGUES['EPL'], 2026, 2026)), 2)
                provider.season(LEAGUES['EPL'], 2026, 2026)
                self.assertEqual(get.call_count, 1)
            for bad in (b'<html>not a CSV</html>', old):
                provider = FootballDataUK(tmp)
                with patch.object(provider.http.session, 'get', return_value=Mock(content=bad)), self.assertWarns(RuntimeWarning):
                    self.assertEqual(len(provider.season(LEAGUES['EPL'], 2026, 2026)), 2)
                self.assertEqual(path.read_bytes(), new)


class OddsJoinAuditTests(OfflineQuotePolicyTestCase):
    def setUp(self):
        super().setUp()
        self.temp = tempfile.TemporaryDirectory(); self.addCleanup(self.temp.cleanup)
        with patch.dict('os.environ', {}, clear=True):
            self.pipeline = FootballValuePipelineV2(cache_dir=self.temp.name)
        self.pipeline.odds_api = Mock()
        self.row = {'Date': pd.Timestamp('2026-10-11'), 'HomeTeam': 'Man City',
            'AwayTeam': 'Everton', 'fixture_id': 'event1', 'kickoff_utc': '2026-10-11T17:00:00Z'}
        self.quote = {'fixture_id': 'event1', '_odds_home_team': 'Manchester City FC',
            '_odds_away_team': 'Everton FC', '_odds_commence_time': '2026-10-11T17:00:00Z',
            'odds_source': 'The Odds API', 'live_best_home_odds': 1.8}

    def attach(self, quotes):
        self.pipeline.odds_api.odds.return_value = pd.DataFrame(quotes)
        return self.pipeline._attach_live_odds(pd.DataFrame([self.row]), LEAGUES['EPL'], T0).iloc[0]

    def test_matching_id_still_requires_correct_teams_kickoff_and_unique_response(self):
        self.assertEqual(self.attach([self.quote])['odds_event_id'], 'event1')
        for changes in ({'_odds_home_team': 'Arsenal'},
                        {'_odds_commence_time': '2026-10-11T19:00:00Z'},
                        {'_odds_commence_time': None}):
            with self.subTest(changes=changes):
                row = self.attach([{**self.quote, **changes}])
                self.assertTrue(pd.isna(row['odds_event_id']))
        self.assertTrue(pd.isna(self.attach([self.quote, self.quote])['odds_event_id']))

    def test_date_team_fallback_rejects_ambiguity_and_can_fill_verified_kickoff(self):
        self.row['fixture_id'] = 'fdco:fixture'
        self.row['kickoff_utc'] = None
        joined = self.attach([self.quote])
        self.assertEqual(joined['odds_match_method'], 'date+teams')
        self.assertEqual(pd.Timestamp(joined['kickoff_utc']), pd.Timestamp(self.quote['_odds_commence_time']))
        self.assertTrue(pd.isna(self.attach([self.quote, {**self.quote, 'fixture_id': 'event2'}])['odds_event_id']))


class ArchiveAuditTests(OfflineQuotePolicyTestCase):
    def test_interrupted_staging_is_not_treated_as_a_published_archive(self):
        from workflow_checks import archive_check
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            stage = root/'performance/snapshots/.capture-interrupted/snapshot'
            stage.mkdir(parents=True)
            (stage/'predictions.csv').write_text('partial copy')
            self.assertEqual(archive_check(root)['snapshots'], [])
            self.assertEqual(snapshots(root), [])

    def test_failed_capture_leaves_no_partial_archive_and_same_commit_can_retry(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)/'football_output_v2'; raw = root/'raw'; raw.mkdir(parents=True)
            pd.DataFrame([fixture()]).to_csv(raw/'all_leagues_predictions.csv', index=False)
            pd.DataFrame([pick()]).to_csv(raw/'conservative_bet_shortlist.csv', index=False)
            (raw/'conservative_bet_summary.json').write_text(json.dumps({'generated_at_utc': T0.isoformat()}))
            with patch('pipeline_health.capture_health', side_effect=RuntimeError('disk/health failure')):
                with self.assertRaises(RuntimeError): capture(SHA, root=root, captured_at=T0)
            self.assertEqual(list((root/'performance/snapshots').iterdir()), [])
            with patch('pipeline_health.capture_health', return_value={}):
                self.assertTrue(capture(SHA, root=root, captured_at=T0))
            self.assertEqual(len(snapshots(root)), 1)

    def test_exact_minimum_lead_time_is_consistent_at_capture_and_grading(self):
        from tests.test_performance_tracking import KICK
        captured = KICK-timedelta(minutes=20)
        metadata = {'captured_at_utc': captured.isoformat(), 'generated_at_utc': captured.isoformat(),
                    'git_commit_sha': SHA}
        archive = [(metadata, [fixture()], [pick()])]
        self.assertEqual(len(frozen_rows(archive, 'predictions')), 1)
        self.assertEqual(len(frozen_rows(archive, 'shortlist')), 1)
        metadata['captured_at_utc'] = (captured+timedelta(microseconds=1)).isoformat()
        self.assertFalse(frozen_rows(archive, 'predictions'))
