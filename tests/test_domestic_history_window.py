"""Keep the expanded domestic CSV window independent of UCL access."""
from datetime import datetime, timezone
from unittest.mock import Mock, patch
import unittest
import pandas as pd

from football_value_pipeline_v2_standalone import FootballValuePipelineV2, LEAGUES, build_parser, history_windows


class HistoryWindowTests(unittest.TestCase):
    def test_default_forecast_lookahead_is_three_days_and_explicit_overrides_survive(self):
        import inspect
        from football_value_pipeline_v2_standalone import FootballDataUK, FootballValuePipeline
        self.assertEqual(build_parser().parse_args([]).lookahead_days, 3)
        self.assertEqual(build_parser().parse_args(['--lookahead-days','10']).lookahead_days, 10)
        self.assertEqual(inspect.signature(FootballDataUK.fixtures).parameters['lookahead_days'].default, 3)
        self.assertEqual(inspect.signature(FootballValuePipeline).parameters['lookahead_days'].default, 3)
        with patch('football_value_pipeline_v2_standalone.FootballDataUK'):
            self.assertEqual(FootballValuePipelineV2(live_odds=False).lookahead_days, 3)
            self.assertEqual(FootballValuePipelineV2(lookahead_days=7,live_odds=False).lookahead_days, 7)

    def test_normal_cli_uses_six_domestic_seasons_and_four_ucl_seasons(self):
        args = build_parser().parse_args([])
        self.assertEqual(history_windows(args), {'domestic_seasons_back': 6, 'seasons_back': 4})
        shared = build_parser().parse_args(['--seasons-back', '3'])
        self.assertEqual(history_windows(shared), {'domestic_seasons_back': 3, 'seasons_back': 3})
        custom = build_parser().parse_args(['--domestic-seasons-back', '4', '--seasons-back', '2'])
        self.assertEqual(history_windows(custom), {'domestic_seasons_back': 4, 'seasons_back': 2})

    def test_source_and_reconciliation_receive_the_same_league_window(self):
        pipe = FootballValuePipelineV2(seasons_back=4, domestic_seasons_back=6, live_odds=False)
        now = datetime(2026, 10, 19, tzinfo=timezone.utc)
        pipe.source.history = Mock(return_value=pd.DataFrame())
        pipe.football_data_org = Mock()
        pipe.football_data_org.history.return_value = pd.DataFrame()
        def combine(history, cache, league, clock, seasons):
            self.assertEqual(seasons, 4 if league == 'UCL' else 6)
            return history.copy()
        with patch('bbs_integration.combined_training_history', side_effect=combine):
            for key in ('EPL', 'UCL'):
                frame = pipe._history_for_league(LEAGUES[key], now)
                self.assertEqual(frame.attrs['training_seasons_requested'], 4 if key == 'UCL' else 6)
        self.assertEqual(pipe.source.history.call_args.kwargs['seasons_back'], 6)
        self.assertEqual(pipe.football_data_org.history.call_args.kwargs['seasons_back'], 4)

    def test_programmatic_callers_keep_their_explicit_window_and_bad_overrides_fail(self):
        pipe = FootballValuePipelineV2(seasons_back=2, live_odds=False)
        self.assertIsNone(pipe.domestic_seasons_back)
        for value in (0, 11, True, 2.5):
            with self.assertRaises(ValueError):
                FootballValuePipelineV2(domestic_seasons_back=value, live_odds=False)
