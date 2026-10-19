from offline_test_case import OfflineQuotePolicyTestCase
import unittest
from datetime import datetime, timezone
from types import SimpleNamespace
from unittest.mock import Mock, patch
import pandas as pd
from goal_market_validation import prioritized_additional_events
from football_value_pipeline_v2_standalone import FootballValuePipelineV2


class CoverageTests(OfflineQuotePolicyTestCase):
    def fixtures(self):
        return pd.DataFrame([dict(Date=pd.Timestamp('2026-10-13'),
            kickoff_utc='2026-10-13T19:00:00Z', HomeTeam=f'Home{i}',
            AwayTeam=f'Away{i}', odds_source='The Odds API', odds_event_id=f'event{i}')
            for i in range(18)])

    def test_all_ignores_quota_and_model_thresholds_but_requires_link_and_window(self):
        rows = [(r.to_dict(), {}) for _, r in self.fixtures().iterrows()]
        rows += [(dict(rows[0][0], odds_event_id=None), {}),
                 (dict(rows[0][0], kickoff_utc='2026-11-01T19:00:00Z'), {})]
        now = datetime(2026, 10, 12, tzinfo=timezone.utc)
        self.assertEqual(prioritized_additional_events(rows, 4, now, 'all'), list(range(18)))
        self.assertEqual(prioritized_additional_events(rows, 4, now, 'ranked'), [])

    def test_additional_fetches_stop_at_current_48_hour_boundary(self):
        now=datetime(2026,10,12,tzinfo=timezone.utc)
        base={'odds_source':'The Odds API','odds_event_id':'event'}
        rows=[({**base,'kickoff_utc':(pd.Timestamp(now)+delta).isoformat()}, {})
              for delta in (pd.Timedelta(hours=48),pd.Timedelta(hours=48,seconds=1),pd.Timedelta(hours=72))]
        self.assertEqual(prioritized_additional_events(rows,100,now,'all'),[0])

    def run_pipeline(self, mode='all', mixed=False):
        pipeline = object.__new__(FootballValuePipelineV2)
        for key, value in dict(half_life_days=365, l2=0.1, max_goals=10,
                devig_method='power', market_weight=0.5, fixture_provider='auto',
                odds_regions='eu', extra_event_odds_requests=0,
                max_extra_event_odds_requests=24, extra_event_odds_quota={'UCL': 4},
                extra_event_odds_by_league={}, additional_odds_coverage=mode).items():
            setattr(pipeline, key, value)
        pipeline._training_health = Mock(return_value={'status':'OFFLINE_TEST'})
        pipeline._history_for_league = Mock(return_value=pd.DataFrame(
            columns=['Date', 'HomeTeam', 'AwayTeam', 'FTHG', 'FTAG']))
        pipeline._current_fixtures = Mock(return_value=self.fixtures())
        pipeline._attach_live_odds = lambda fixtures, *args: fixtures
        pipeline._predict_row = lambda *args: (dict(home_name_match_score=99,
            away_name_match_score=99, p_home_draw=.9, raw_p_home_draw=.9), {})
        quote = dict(market_home_draw_odds=1.2, market_draw_away_odds=1.3,
                     market_home_draw_bookmakers=2)
        pipeline.odds_api = Mock()
        pipeline.odds_api.extra_markets_for_event.return_value = quote
        if mixed:
            pipeline.odds_api.extra_markets_for_event.side_effect = [
                {}, RuntimeError('provider failed')] + [quote] * 16
        model = SimpleNamespace(training_matches=100, training_end=None, fit_result=None,
            base=0, home_adv=0, rho=0, half_life_days=365, max_goals=10)
        with patch('football_value_pipeline_v2_standalone.DixonColesModel') as model_class:
            model_class.return_value.fit.return_value = model
            result = pipeline.run_league('UCL', datetime(2026, 10, 12, tzinfo=timezone.utc))
        return pipeline, result

    def test_all_requests_18_even_with_four_slot_quota(self):
        pipeline, (frame, diagnostics, _) = self.run_pipeline()
        self.assertEqual(pipeline.odds_api.extra_markets_for_event.call_count, 18)
        self.assertEqual(len(frame), 18)
        self.assertEqual(diagnostics['additional_odds_unrequested_linked_fixtures'], 0)
        self.assertFalse(diagnostics['additional_event_odds_hard_cap_applies'])

    def test_ranked_preserves_four_slot_quota(self):
        pipeline, (_, diagnostics, _) = self.run_pipeline('ranked')
        self.assertEqual(pipeline.odds_api.extra_markets_for_event.call_count, 4)
        self.assertEqual(diagnostics['additional_odds_unrequested_linked_fixtures'], 14)

    def test_missing_quotes_and_failures_are_visible_and_do_not_stop_coverage(self):
        with self.assertWarns(RuntimeWarning):
            pipeline, (_, diagnostics, _) = self.run_pipeline(mixed=True)
        self.assertEqual(pipeline.odds_api.extra_markets_for_event.call_count, 18)
        rows = diagnostics['additional_odds_coverage']
        self.assertEqual(rows[0]['status'], 'RESPONSE_WITHOUT_VALID_DC_QUOTES')
        self.assertEqual(rows[1]['status'], 'REQUEST_FAILED')
        self.assertEqual(rows[2]['status'], 'RECEIVED_VALID_DC_QUOTES')
        self.assertEqual(rows[1]['error_type'], 'RuntimeError')
