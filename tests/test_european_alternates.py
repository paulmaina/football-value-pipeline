"""UCL/UEL per-event markets 48 hours ahead, once a day, within 80 of pinnapi's 100 requests (plan item 15)."""
from __future__ import annotations

from offline_test_case import OfflineQuotePolicyTestCase
from datetime import timedelta
import json
from pathlib import Path
import tempfile
from types import SimpleNamespace
from unittest.mock import Mock, patch

import pandas as pd

import european_alternates as ea
from football_value_pipeline_v2_standalone import FootballValuePipelineV2
from goal_market_validation import prioritized_additional_events
from tests.test_model_upgrades_v1 import NOW


def record(day_offset=0, ran=True, requests=3, kit=4):
    when = (NOW + timedelta(days=day_offset)).isoformat()
    return {'recorded_at_utc': when, 'workflow': 'scheduled-forecasts', 'calls': 0,
            'odds_provider': {'providers': {'pinnapi': {'requests': kit, 'daily_allowance': 100}}},
            ea.KEY: {'ran': ran, 'requests': requests}}


class StepTests(OfflineQuotePolicyTestCase):
    def test_gates(self):
        self.assertFalse(ea.Step([], NOW, routed=False).allow('UCL', 5))         # switch off: Odds API credits
        self.assertFalse(ea.Step([record()], NOW, routed=True).allow('UCL', 5))  # already ran today
        self.assertTrue(ea.ran_today([record()], NOW))
        self.assertFalse(ea.ran_today([record(day_offset=-1), record(ran=False)], NOW))
        step = ea.Step([record(day_offset=-1)], NOW, routed=True)
        self.assertFalse(step.allow('EPL', 5))                                  # UCL and UEL only
        self.assertTrue(step.allow('UCL', 10))
        for _ in range(10):
            step.count('UCL')
        with patch('odds_provider.daily_projection', return_value={'busy_day': 60.0}):
            gated = ea.Step([], NOW, routed=True)
            self.assertTrue(gated.allow('UCL', 20))                             # 60 + 20 = 80: allowed
            for _ in range(20):
                gated.count('UCL')
            self.assertFalse(gated.allow('UEL', 1))                             # 60 + 20 + 1 > 80: skipped
        summary = gated.summary()
        self.assertEqual((summary['ran'], summary['requests'], summary['busy_day_projection_before']), (True, 20, 60.0))
        self.assertEqual(summary['leagues']['UEL']['reason'], 'skipped: projected 81 would exceed 80 a day')
        self.assertIsNone(ea.Step([], NOW, routed=True).summary())

    def test_window_widens_only_when_asked(self):
        rows = [({'kickoff_utc': (NOW + timedelta(hours=h)).isoformat(), 'odds_source': 'The Odds API',
                  'odds_event_id': f'e{h}'}, {}) for h in (5, 30, 47, 60)]
        self.assertEqual(prioritized_additional_events(rows, 9, as_of=NOW, coverage='all'), [0])
        self.assertEqual(prioritized_additional_events(rows, 9, as_of=NOW, coverage='all', hours=48), [0, 1, 2])


class RunLeagueTests(OfflineQuotePolicyTestCase):
    def run_pipeline(self, step, league='UCL'):
        pipeline = object.__new__(FootballValuePipelineV2)
        for key, value in dict(half_life_days=480, l2=0.08, max_goals=10, devig_method="power",
                market_weight=0.7, totals_anchor=True, fixture_provider="auto", odds_regions="eu",
                extra_event_odds_requests=0, max_extra_event_odds_requests=24,
                extra_event_odds_quota={}, extra_event_odds_by_league={},
                additional_odds_coverage="all", legacy_comparison=False, _european_step=step).items():
            setattr(pipeline, key, value)
        pipeline._training_health = Mock(return_value={"status": "OFFLINE_TEST"})
        pipeline._history_for_league = Mock(return_value=pd.DataFrame(
            columns=["Date", "HomeTeam", "AwayTeam", "FTHG", "FTAG"]))
        fixtures = []
        for hours, home in ((5, 'A'), (30, 'C'), (60, 'E')):
            kickoff = (NOW + timedelta(hours=hours)).isoformat()
            fixtures.append(dict(Date=pd.Timestamp(kickoff[:10]), kickoff_utc=kickoff, HomeTeam=home, AwayTeam='B',
                                 odds_source="The Odds API", odds_event_id=f"ev{hours}"))
        pipeline._current_fixtures = Mock(return_value=pd.DataFrame(fixtures))
        pipeline._attach_live_odds = lambda fixtures, *args: fixtures
        pipeline._predict_row = lambda model, row: (dict(home_name_match_score=100, away_name_match_score=100,
                                                         totals_anchor_status='NOT_ANCHORED'), {"1-0": 0.1})
        pipeline.odds_api = Mock()
        pipeline.odds_api.extra_markets_for_event.side_effect = lambda league, event_id, **kw: {}
        model = SimpleNamespace(training_matches=100, training_end=None, fit_result=None,
                                resolve_team=lambda name: (name, 100.0), base=0, home_adv=0, rho=0,
                                half_life_days=480, max_goals=10)
        pipeline.source = SimpleNamespace(http=SimpleNamespace(cache_dir='.'))
        with patch("football_value_pipeline_v2_standalone.DixonColesModel") as model_class,                 patch('count_markets.load_history', return_value=None),                 patch('count_markets.forecast_fixtures', side_effect=lambda h, k, pairs: [None] * len(pairs)):
            model_class.return_value.fit.return_value = model
            _, diagnostics, _ = pipeline.run_league(league, NOW)
        asked = [c.args[1] for c in pipeline.odds_api.extra_markets_for_event.call_args_list]
        return asked, {r['event_id']: r for r in diagnostics['additional_odds_coverage']}

    def test_allowed_step_requests_the_30_hour_fixture_and_counts_it(self):
        step = ea.Step([], NOW, routed=True)
        with patch('odds_provider.daily_projection', return_value={'busy_day': 10.0}):
            asked, coverage = self.run_pipeline(step)
        self.assertEqual(asked, ['ev5', 'ev30'])                     # 60 hours stays out
        self.assertEqual(coverage['ev30'].get('window_hours'), 48)
        self.assertNotIn('window_hours', coverage['ev5'])
        self.assertEqual(step.summary()['leagues']['UCL'], {'extra_fixtures': 1, 'allowed': True,
                                                           'reason': 'projected 11 of 80 a day', 'requests': 1})

    def test_blocked_step_keeps_the_24_hour_window(self):
        for step in (ea.Step([record()], NOW, routed=True), ea.Step([], NOW, routed=False)):
            asked, coverage = self.run_pipeline(step)
            self.assertEqual(asked, ['ev5'])
            self.assertEqual(coverage['ev30']['status'], 'NOT_REQUESTED_OUTSIDE_WINDOW_OR_UNLINKED')
            self.assertFalse(step.summary()['ran'])

    def test_domestic_leagues_never_use_it(self):
        step = ea.Step([], NOW, routed=True)
        asked, _ = self.run_pipeline(step, league='EPL')
        self.assertEqual(asked, ['ev5'])
        self.assertIsNone(step.summary())


class RecordTests(OfflineQuotePolicyTestCase):
    def test_outcome_usage_record_and_next_run(self):
        from football_value_pipeline_v2_standalone import run_outcome
        import odds_provider
        import publish_scheduled_forecasts as publisher
        block = {'ran': True, 'hours': 48, 'limit': 80, 'requests': 7, 'leagues': {}}
        with tempfile.TemporaryDirectory() as tmp:
            (Path(tmp) / 'conservative_bet_summary.json').write_text(json.dumps({ea.KEY: block}), encoding='utf-8')
            outcome = run_outcome(Path(tmp), 3)
        self.assertEqual(outcome[ea.KEY], block)
        rec = publisher.usage_record(outcome, 0)
        self.assertEqual(rec[ea.KEY], block)
        rec['recorded_at_utc'] = NOW.isoformat()
        self.assertTrue(ea.ran_today([rec], NOW))                     # the next run today skips the step
        projection = odds_provider.daily_projection([record(requests=7)], allowance=100)
        self.assertEqual(projection['workflows']['scheduled-forecasts']['european_alternates_48h_requests_per_run'],
                         {'normal': 7.0, 'busy': 7.0})
        self.assertIn('48-hour step made 7', odds_provider.projection_markdown(projection))
