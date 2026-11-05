"""Research qualification, source provenance and positive-return settlement regressions."""
from datetime import datetime, timezone
import json
from pathlib import Path
import tempfile
from unittest.mock import Mock, patch

import numpy as np
import pandas as pd

from offline_test_case import OfflineQuotePolicyTestCase
from test_value_per_market import fixture, h2h_1xbet, price_at, V2, run
from test_price_edge_shortlist import NOW
import profit_shortlist as ps
import team_research as tr
import price_edge_cagey_shortlist as v28

SETTINGS = {**V2, 'value_rule': ps.RULE}


def researched(**extra):
    row = fixture(h2h_1xbet(home=price_at('home', -.1)))
    row.update(lambda_home=.8, lambda_away=2.2, p_home=.2, p_draw=.25, p_away=.55, **extra)
    row['team_research_json'] = json.dumps(tr.prepare(row, NOW))
    return row


class ResearchProfitTests(OfflineQuotePolicyTestCase):
    def test_negative_ev_is_eligible_with_missing_context_warnings(self):
        selected, decisions, summary = run(researched(), settings=SETTINGS)
        self.assertTrue(len(selected))
        loser = decisions[(decisions.market == 'Home win') & decisions.bookmaker.eq('1xBet')].iloc[0]
        self.assertIn(loser.decision, ('SHORTLISTED', 'NOT_SELECTED'))
        self.assertLess(loser.profit_expected_return, 0)
        self.assertIn('availability unavailable', loser.research_warnings)
        self.assertFalse(summary['ev_required_for_selection'])
        self.assertTrue(selected.profit_probability.is_monotonic_decreasing)

    def test_probability_is_positive_net_return_not_push_probability(self):
        row = researched()
        e = json.loads(row['team_research_json'])
        e['margin_distribution'] = {'-2': .15, '-1': .45, '0': .4}
        row['team_research_json'] = json.dumps(e)
        item = dict(market='Asian Handicap Home +1.00', handicap_side='home', handicap_line=1.,
                    offered_decimal_odds=1.2, offered_last_update_utc=NOW.isoformat(),
                    decision='REJECTED', rejection_reasons='edge below 1%')
        out = ps.annotate(row, item, NOW, 0.)
        self.assertAlmostEqual(out['profit_probability'], .4)
        self.assertAlmostEqual(out['p_no_loss'], .85)
        self.assertEqual(out['decision'], 'ELIGIBLE')
        out = ps.annotate(row, dict(item, handicap_line=1.25), NOW, .11)
        # Half-win gains are .10 before cost, so these outcomes are no longer profitable.
        self.assertAlmostEqual(out['profit_probability'], .4)

    def test_future_evidence_and_stale_offer_never_qualify(self):
        row = researched()
        e = json.loads(row['team_research_json'])
        e['observed_at_utc'] = (NOW+pd.Timedelta(seconds=1)).isoformat()
        row['team_research_json'] = json.dumps(e)
        selected, _, _ = run(row, settings=SETTINGS)
        self.assertTrue(selected.empty)
        item = dict(market='Home win', handicap_side='home', handicap_line=-.5,
                    offered_decimal_odds=1.2, offered_last_update_utc=(NOW-pd.Timedelta(hours=25)).isoformat())
        out = ps.annotate(researched(), item, NOW, 0.)
        self.assertEqual(out['decision'], 'REJECTED')

    def test_stakes_use_the_research_distribution_and_preserve_negative_ev_zero(self):
        from staking import stake_recommendations, conservative_settlement
        selected, _, _ = run(researched(), settings=SETTINGS)
        record = selected.iloc[0].to_dict()
        probs = conservative_settlement(record)
        self.assertAlmostEqual(probs['full_win'], record['research_p_win'])
        sized = stake_recommendations(selected)
        self.assertTrue(sized.probability_basis.eq(ps.BASIS).all())
        negative = sized.conservative_ev < 0
        self.assertTrue(sized.loc[negative, 'stake_fraction'].eq(0).all())

    def test_replay_is_offline_and_legacy_rule_stays_replayable(self):
        row = researched()
        with patch('requests.sessions.Session.request', side_effect=AssertionError('network during replay')):
            first, d, summary = run(row, settings=SETTINGS)
            replay, _, _ = run(row, settings={k: summary.get(k) for k in v28.REPLAY_SETTINGS})
        self.assertEqual(first.market_to_bet.tolist(), replay.market_to_bet.tolist())
        old, _, old_summary = run(row, settings=V2)
        self.assertEqual(old_summary['value_rule'], v28.VALUE_RULE_PER_MARKET)
        self.assertNotIn('research_warnings', old)

    def test_raw_validation_and_readable_output_from_recorded_research(self):
        from workflow_checks import raw_check
        from format_football_output import process_conservative_shortlist
        from pipeline_health import write_generation_metadata
        import master_shortlist as ms
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); raw = root/'raw'; raw.mkdir(); readable = root/'readable'; readable.mkdir()
            row = researched()
            selected, decisions, summary = run(row, settings=SETTINGS)
            pd.DataFrame([row]).to_csv(raw/'all_leagues_predictions.csv', index=False)
            selected.to_csv(raw/'conservative_bet_shortlist.csv', index=False)
            selected.to_csv(raw/'conservative_strict_qualifiers.csv', index=False)
            decisions.to_csv(raw/'conservative_bet_rejections.csv', index=False)
            v28.cagey_tier_list(decisions).to_csv(raw/v28.TIER_FILE, index=False)
            ms.refresh(decisions, raw, summary, pd.DataFrame([row]))
            (raw/'conservative_bet_summary.json').write_text(json.dumps(summary), encoding='utf-8')
            write_generation_metadata(raw, summary)
            self.assertEqual(raw_check(root)['selections'], len(selected))
            process_conservative_shortlist(raw, readable)
            out = pd.read_csv(readable/'conservative_bet_shortlist_readable.csv')
            self.assertIn('Chance of positive return', out)
            self.assertTrue(out['Coverage warnings'].str.contains('availability unavailable').all())


class EvidenceTests(OfflineQuotePolicyTestCase):
    def test_recent_results_weight_more_and_future_day_is_excluded(self):
        history = pd.DataFrame([dict(Date='2026-11-01', HomeTeam='H', AwayTeam='A', FTHG=0, FTAG=2),
                                dict(Date='2026-11-06', HomeTeam='H', AwayTeam='A', FTHG=3, FTAG=0),
                                dict(Date='2026-11-07', HomeTeam='H', AwayTeam='A', FTHG=9, FTAG=0)])
        data = tr.form_history(history, 'H', 'A', NOW)
        self.assertEqual(len(data['home']), 2)
        stats = tr.weighted_form(data['home'], 'H', 'home')
        self.assertGreater(stats['goals_for'], 1.5)
        self.assertEqual(stats['results'], 'WL')
        self.assertNotIn('xg_for', stats)

    def test_cache_is_observation_bound_and_failures_are_visible(self):
        with tempfile.TemporaryDirectory() as tmp:
            response = Mock(content=b'{}', json=lambda: {'events': []})
            session = Mock(); session.get.return_value = response
            client = tr.FreeSources(tmp, session=session, clock=lambda: NOW.to_pydatetime())
            data = client.get('https://example.test/feed')
            self.assertEqual(data['status'], 'available')
            client.get('https://example.test/feed'); session.get.assert_called_once()
            offline = tr.FreeSources(tmp, session=session, clock=lambda: (NOW-pd.Timedelta(hours=1)).to_pydatetime(), online=False)
            self.assertEqual(offline.get('https://example.test/feed')['status'], 'unavailable')

    def test_completed_schedule_status_inside_competition_and_xg(self):
        competitors = [dict(homeAway='home', team={'displayName': 'H'}, score={'value': 2},
                            statistics=[dict(name='expectedGoals', value=1.4)]),
                       dict(homeAway='away', team={'displayName': 'A'}, score={'value': 0},
                            statistics=[dict(name='expectedGoals', value=.4)])]
        payload = {'events': [dict(date='2026-11-01T20:00Z', competitions=[dict(competitors=competitors,
                    status={'type': {'completed': True, 'name': 'STATUS_FULL_TIME'}})])]}
        data = tr.schedule_rows(payload, NOW, 'test')
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['home_xg'], 1.4)

    def test_future_news_is_not_evidence_and_missing_data_retains_baseline(self):
        xml = '<rss><channel><item><title>Test</title><link>https://example.test/a</link><pubDate>Sun, 08 Nov 2026 12:00:00 GMT</pubDate></item></channel></rss>'
        self.assertEqual(tr.news_items(xml, NOW), [])
        row = researched()
        result = tr.prepare(row, NOW, {'sources': [{'observed_at_utc': (NOW+pd.Timedelta(seconds=1)).isoformat()}],
                                      'coverage': {'availability': 'reported'}})
        self.assertNotIn('availability', result['coverage'])
        self.assertEqual(result['goal_rates'], [.8, 2.2])
