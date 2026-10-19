"""Probability-first selection, quote safeguards and immutable policy replay."""
import copy
from datetime import timedelta
import json
from pathlib import Path
import tempfile

import pandas as pd

from offline_test_case import OfflineQuotePolicyTestCase
from conservative_bet_filter import build_conservative_shortlist, PROBABILITY_SELECTION_POLICY_VERSION, BALANCED_SELECTION_POLICY_VERSION
from test_conservative_bet_filter import fixture, NOW
from test_graded_candidates import only_over_goal, sample_report


def select(rows, reliability=None, selection_policy_version=None, **kwargs):
    return build_conservative_shortlist(pd.DataFrame(rows), as_of=NOW,
        market_reliability=reliability, selection_policy_version=selection_policy_version or PROBABILITY_SELECTION_POLICY_VERSION, **kwargs)


class ProbabilityShortlistTests(OfflineQuotePolicyTestCase):
    def test_ten_highest_probabilities_do_not_prioritize_strict_status(self):
        picks, decisions, summary = select([only_over_goal(i) for i in range(12)],
            {'Premier League': sample_report()})
        self.assertEqual(len(picks), 10)
        self.assertEqual(len(decisions), 96)
        self.assertEqual(picks.fixture_id.nunique(), 10)
        self.assertTrue(picks.rank_probability.is_monotonic_decreasing)
        self.assertEqual(picks.iloc[0].selection_tier, 'PROVISIONAL')
        self.assertEqual(summary['n_strict_qualified'], 2)
        self.assertEqual(summary['n_provisional_watchlist'], 8)
        self.assertEqual(summary['shortfall'], 0)

    def test_negative_ev_and_low_probability_are_visible_not_selection_gates(self):
        rows = [only_over_goal(i) for i in range(10)]
        for row in rows:
            row.update(p_over_1_5=.65, raw_p_over_1_5=.60, market_over_1_5_odds=1.05)
        picks, _, summary = select(rows, {'Premier League': sample_report()})
        self.assertEqual(len(picks), 10)
        self.assertTrue((picks.conservative_estimated_ev < 0).all())
        self.assertTrue(picks.near_miss_reason.str.contains('reliability-adjusted probability').all())
        self.assertTrue(picks.selection_tier.eq('PROVISIONAL').all())
        self.assertEqual(summary['selection_objective'], 'PROBABILITY_FIRST')
        limited, _, _ = select(rows, {'Premier League': sample_report()}, adjusted_ev_floor=.015)
        self.assertTrue(limited.empty)

    def test_under_three_point_five_can_win_and_price_breaks_probability_tie(self):
        row = fixture(); row.update(p_under_3_5=.96, raw_p_under_3_5=.94)
        picks, _, _ = select([row], {'Premier League': sample_report()})
        self.assertEqual(picks.iloc[0].market, 'Under 3.5')
        row['p_home'] = .96
        picks, _, _ = select([row], {'Premier League': sample_report()})
        self.assertEqual(picks.iloc[0].market, 'Home win')

    def test_probability_quality_and_bad_identity_or_quotes_still_fail_closed(self):
        variants = [
            {'market_over_1_5_odds': None}, {'best_over_1_5_bookmaker': 'Smarkets'},
            {'market_best_over_1_5_last_update_utc': (NOW-timedelta(hours=25)).isoformat()},
            {'market_best_over_1_5_last_update_utc': (NOW+timedelta(hours=1)).isoformat()},
            {'market_reference_over_1_5_last_update_utc': None},
            {'market_reference_over_1_5_odds': 1.01, 'market_reference_over_1_5_opposite_odds': 1.01},
            {'home_name_match_score': 10}, {'p_over_1_5': float('nan')},
            {'raw_p_over_1_5': float('nan')}, {'home_team': ''}, {'away_team':'Home_0'},
        ]
        for changes in variants:
            with self.subTest(changes=changes):
                row = only_over_goal(0); row.update(changes)
                picks, _, summary = select([row], {'Premier League': sample_report()})
                self.assertTrue(picks.empty)
                self.assertEqual(summary['shortfall'], 10)
        bad = sample_report(); bad['markets']['over_1_5']['confidence_penalty'] = None
        self.assertTrue(select([only_over_goal(0)], {'Premier League': bad})[0].empty)
        self.assertTrue(select([only_over_goal(0)], execution_policy={
            'allowed_bookmakers':['1xBet'], 'per_stake_cost_bps':0})[0].empty)

    def test_audit_failures_remain_visible_but_do_not_shorten_ranking(self):
        report = sample_report(); report['markets']['over_1_5']['status'] = 'UNRELIABLE_AUDIT'
        report['markets']['over_1_5']['high_confidence']['75plus'].pop('development_only_penalty')
        picks, _, _ = select([only_over_goal(0)], {'Premier League': report})
        self.assertEqual(len(picks), 1)
        self.assertIn('UNRELIABLE_AUDIT', picks.iloc[0].near_miss_reason)
        self.assertEqual(picks.iloc[0].selection_tier, 'PROVISIONAL')
        self.assertIn('NOT_ASSESSED', select([only_over_goal(0)])[0].iloc[0].near_miss_reason)

    def test_horizon_shortage_duplicate_identity_and_empty_inputs(self):
        rows = [only_over_goal(i) for i in range(5)]
        for row, delta in zip(rows, [timedelta(minutes=19), timedelta(minutes=20),
                                   timedelta(hours=72), timedelta(hours=72,seconds=1), timedelta(hours=-1)]):
            row['kickoff_utc'] = (NOW+delta).isoformat()
        duplicate = dict(rows[1], fixture_id='another-provider-id')
        picks, _, summary = select(rows+[duplicate], {'Premier League': sample_report()})
        self.assertEqual(set(picks.fixture_id), {'fixture-1','fixture-2'})
        self.assertEqual(summary['shortfall'], 8)
        self.assertTrue(summary['selected_matches_within_72_hours'])
        self.assertIn('Fewer than ten', summary['shortfall_reason'])
        self.assertTrue(select([])[0].empty)

    def test_new_experiments_capture_replay_and_reporting_include_control_without_ev_gate(self):
        import filter_sensitivity_experiment as ev
        import shortlist_policy_experiment as policy
        from performance_tracking import write_json, capture, snapshots
        from format_football_output import process_conservative_shortlist
        from workflow_checks import raw_check, archive_check
        row = only_over_goal(0); row['market_over_1_5_odds'] = 1.05
        predictions = pd.DataFrame([row]); reports = {'Premier League': sample_report()}
        picks, decisions, summary = select([row], reports)
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); raw = root/'raw'; raw.mkdir(); (root/'readable').mkdir()
            predictions.to_csv(raw/'all_leagues_predictions.csv', index=False)
            picks.to_csv(raw/'conservative_bet_shortlist.csv', index=False)
            write_json(raw/'conservative_bet_summary.json', summary)
            write_json(raw/'EPL_goal_market_validation.json', {'league':'Premier League', **reports['Premier League']})
            reports['Premier League']['league'] = 'Premier League'
            pdataset = policy.write_experiment(predictions, raw, summary, decisions, reports)
            edataset = ev.write_experiment(predictions, raw, summary, decisions, reports)
            self.assertEqual(edataset['floors'], [0., .015, .03, .05])
            self.assertEqual(len(edataset['rows']), 4*len(summary['eligible_markets']))
            self.assertIsNotNone(policy.capture_file(raw, summary['generated_at_utc']))
            self.assertIsNotNone(ev.capture_file(raw, summary['generated_at_utc']))
            self.assertEqual(raw_check(root)['warnings'], [])
            self.assertTrue(capture('abcdef01'*5, root=root, captured_at=NOW+timedelta(minutes=1)))
            self.assertEqual(archive_check(root)['warnings'], [])
            self.assertEqual(ev.frozen(root, snapshots(root))[1], [])
            self.assertEqual(policy.frozen(root, snapshots(root))[1], [])
            es, _, _ = ev.evaluate(root, snapshots(root), [], NOW)
            self.assertIn(0., [r['ev_floor'] for r in es['comparisons']])
            ev.review_experiment(root, snapshots(root), [], NOW)
            self.assertIn('No EV gate', (root/'performance/filter_sensitivity_experiment/report.md').read_text())
            process_conservative_shortlist(raw, root/'readable')
            text = (root/'readable/conservative_bet_shortlist_report.md').read_text()
            self.assertIn(f"Top {summary['target_distinct_matches']}", text)
            self.assertIn('Negative EV', text)
            forged = copy.deepcopy(pdataset); forged['rows'][0]['rank_probability'] = .99
            with self.assertRaises(ValueError): policy.validate(forged, summary['generated_at_utc'], predictions.to_dict('records'))


class BalancedShortlistTests(OfflineQuotePolicyTestCase):
    def select(self, rows, **kwargs):
        return select(rows, {'Premier League':sample_report()},
                      selection_policy_version=BALANCED_SELECTION_POLICY_VERSION, **kwargs)

    def test_twelve_cap_preserves_top_ten_and_frozen_v14_weighting_replay(self):
        from conservative_bet_filter import TEN_MATCH_BALANCED_SELECTION_POLICY_VERSION
        import shortlist_weight_experiment as trial
        rows = [dict(only_over_goal(i), kickoff_utc=(NOW+timedelta(hours=24)).isoformat()) for i in range(15)]
        reports = {'Premier League': sample_report()}
        current, _, summary = self.select(rows)
        legacy, decisions, old_summary = select(rows, reports,
            selection_policy_version=TEN_MATCH_BALANCED_SELECTION_POLICY_VERSION)
        self.assertEqual(current.fixture_id.nunique(), 12)
        self.assertEqual(legacy.fixture_id.nunique(), 10)
        self.assertEqual(summary['target_distinct_matches'], 12)
        self.assertEqual(old_summary['target_distinct_matches'], 10)
        self.assertEqual(legacy.fixture_id.tolist(), current.fixture_id.iloc[:10].tolist())
        pd.testing.assert_frame_equal(legacy, current.iloc[:10].reset_index(drop=True))
        execution = old_summary['quote_execution_policy']
        frozen = {'version': trial.VERSION, 'variants': trial.VARIANTS,
            'selection_policy_version': TEN_MATCH_BALANCED_SELECTION_POLICY_VERSION,
            'generated_at_utc': NOW.isoformat(), 'execution_policy': execution,
            'validation_evidence': reports,
            'rows': trial.decision_rows(pd.DataFrame(rows), NOW.isoformat(), reports, execution,
                baseline_policy=TEN_MATCH_BALANCED_SELECTION_POLICY_VERSION)}
        trial.validate(frozen, NOW.isoformat(), rows)
        trial.validate_control(frozen, legacy.to_dict('records'))

    def test_twelve_target_shortfall_and_raw_integrity_cap(self):
        from format_football_output import process_conservative_shortlist
        from performance_tracking import write_json
        from workflow_checks import raw_check
        rows = [dict(only_over_goal(i), kickoff_utc=(NOW+timedelta(hours=24)).isoformat()) for i in range(15)]
        picks, _, summary = self.select(rows)
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); raw = root/'raw'; raw.mkdir()
            readable = root/'readable'; readable.mkdir()
            pd.DataFrame(rows).to_csv(raw/'all_leagues_predictions.csv', index=False)
            picks.to_csv(raw/'conservative_bet_shortlist.csv', index=False)
            write_json(raw/'conservative_bet_summary.json', summary)
            write_json(raw/'EPL_goal_market_validation.json', dict(sample_report(), league='Premier League'))
            self.assertEqual(raw_check(root)['selections'], 12)
            process_conservative_shortlist(raw, readable)
            self.assertIn('Top 12', (readable/'conservative_bet_shortlist_report.md').read_text())
            # A forged target cannot bypass the policy's twelve-fixture cap.
            write_json(raw/'conservative_bet_summary.json', dict(summary, target_distinct_matches=13))
            with self.assertRaisesRegex(ValueError, 'target differs'):
                raw_check(root)
            write_json(raw/'conservative_bet_summary.json', summary)
            pd.concat([picks, picks.iloc[:1]]).to_csv(raw/'conservative_bet_shortlist.csv', index=False)
            with self.assertRaisesRegex(ValueError, 'exceeds 12'):
                raw_check(root)
        short, _, shortage = self.select(rows[:4])
        self.assertEqual(len(short), 4)
        self.assertEqual(shortage['shortfall'], 8)
        self.assertIn('Fewer than twelve', shortage['shortfall_reason'])

    def test_archive_gate_replays_membership_prices_ev_and_summary_without_sidecars(self):
        from performance_tracking import write_json
        from workflow_checks import raw_check
        rows = [dict(only_over_goal(i), kickoff_utc=(NOW+timedelta(hours=24)).isoformat()) for i in range(15)]
        picks, decisions, summary = self.select(rows)
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); raw = root/'raw'; raw.mkdir()
            pd.DataFrame(rows).to_csv(raw/'all_leagues_predictions.csv', index=False)
            write_json(raw/'conservative_bet_summary.json', summary)
            write_json(raw/'EPL_goal_market_validation.json', dict(sample_report(), league='Premier League'))
            source = raw/'conservative_bet_shortlist.csv'
            picks.to_csv(source, index=False)
            self.assertEqual(raw_check(root)['warnings'], [])
            for field, value in [('conservative_estimated_ev', 999),
                                 ('offered_decimal_odds', 99), ('calibration_penalty', .99)]:
                changed = picks.copy(); changed.loc[0, field] = value
                changed.to_csv(source, index=False)
                with self.subTest(field=field), self.assertRaisesRegex(ValueError, 'ranking replay'):
                    raw_check(root)
            # Replacing the twelfth selection by a lower-ranked valid candidate
            # preserves score ordering and counts, but must fail exact replay.
            alternative = decisions.loc[decisions.decision.eq('NOT_SELECTED') & decisions.selection_score.notna()]
            alternative = alternative.loc[~alternative.fixture_id.isin(picks.fixture_id)].iloc[0]
            changed = picks.copy()
            changed.loc[11] = alternative.reindex(changed.columns)
            changed.loc[11, ['decision', 'selection_tier']] = picks.loc[11, ['decision', 'selection_tier']]
            changed.to_csv(source, index=False)
            with self.assertRaisesRegex(ValueError, 'ranking replay'):
                raw_check(root)
            picks.to_csv(source, index=False)
            write_json(raw/'conservative_bet_summary.json', dict(summary, shortfall=5))
            with self.assertRaisesRegex(ValueError, 'shortfall differs'):
                raw_check(root)
            write_json(raw/'conservative_bet_summary.json', summary)
            (raw/'EPL_goal_market_validation.json').unlink()
            with self.assertRaisesRegex(ValueError, 'Missing.*reliability evidence'):
                raw_check(root)

    def test_ev_sensitivity_captures_twelve_and_keeps_archived_ten_cap(self):
        import filter_sensitivity_experiment as ev
        from conservative_bet_filter import TEN_MATCH_BALANCED_SELECTION_POLICY_VERSION
        from performance_tracking import capture, snapshots, write_json
        rows = [dict(only_over_goal(i), kickoff_utc=(NOW+timedelta(hours=24)).isoformat()) for i in range(15)]
        reports = {'Premier League': dict(sample_report(), league='Premier League')}
        frame = pd.DataFrame(rows)
        picks, decisions, summary = select(rows, reports, selection_policy_version=BALANCED_SELECTION_POLICY_VERSION)
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); raw = root/'raw'; raw.mkdir()
            frame.to_csv(raw/'all_leagues_predictions.csv', index=False)
            picks.to_csv(raw/'conservative_bet_shortlist.csv', index=False)
            write_json(raw/'conservative_bet_summary.json', summary)
            write_json(raw/'EPL_goal_market_validation.json', reports['Premier League'])
            data = ev.write_experiment(frame, raw, summary, decisions, reports)
            self.assertEqual(sum(r['ev_floor']==0 and r['decision'] in ev.SELECTED for r in data['rows']), 12)
            self.assertIsNotNone(ev.capture_file(raw, summary['generated_at_utc']))
            self.assertTrue(capture('e'*40, root=root, captured_at=NOW))
            self.assertEqual(len(ev.frozen(root, snapshots(root))[0]), 15*7*4)
            mislabeled = copy.deepcopy(data)
            mislabeled['selection_policy_version'] = TEN_MATCH_BALANCED_SELECTION_POLICY_VERSION
            with self.assertRaisesRegex(ValueError, 'policy cap exceeded'):
                ev.validate(mislabeled, summary['generated_at_utc'], rows)
            overflow = copy.deepcopy(data)
            extra = next(r for r in overflow['rows'] if r['ev_floor']==0 and r['decision']=='NOT_SELECTED'
                         and r['market']=='Over 1.5' and r['fixture_id'] not in set(picks.fixture_id))
            extra.update(decision='SHORTLISTED', selection_tier='STRICT')
            with self.assertRaisesRegex(ValueError, 'policy cap exceeded'):
                ev.validate(overflow, summary['generated_at_utc'], rows)

    def test_under_35_excluded_before_scoring_and_historical_replay_preserved(self):
        from conservative_bet_filter import PREVIOUS_BALANCED_SELECTION_POLICY_VERSION
        row = fixture(); row.update(p_under_3_5=.99, raw_p_under_3_5=.98)
        picks, decisions, summary = self.select([row])
        self.assertNotIn('Under 3.5', summary['eligible_markets'])
        self.assertNotIn('Under 3.5', decisions.market.tolist())
        self.assertNotIn('Under 3.5', picks.market.tolist())
        changed = dict(row, p_under_3_5=.01, raw_p_under_3_5=.01)
        other, _, _ = self.select([changed])
        pd.testing.assert_frame_equal(picks, other)
        # Integrity validation rejects excluded markets even with a forged allow-list.
        from workflow_checks import raw_check
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); raw = root/'raw'; raw.mkdir()
            pd.DataFrame([row]).to_csv(raw/'all_leagues_predictions.csv', index=False)
            forged = picks.copy(); forged['market'] = 'Under 3.5'
            forged.to_csv(raw/'conservative_bet_shortlist.csv', index=False)
            forged_summary = dict(summary, eligible_markets=[*summary['eligible_markets'], 'Under 3.5'])
            (raw/'conservative_bet_summary.json').write_text(json.dumps(forged_summary))
            with self.assertRaisesRegex(ValueError, 'Under 3.5 is excluded'):
                raw_check(root)
        old, old_decisions, old_summary = select([row], {'Premier League':sample_report()},
            selection_policy_version=PREVIOUS_BALANCED_SELECTION_POLICY_VERSION)
        self.assertIn('Under 3.5', old_decisions.market.tolist())
        self.assertIn('Under 3.5', old_summary['eligible_markets'])
        self.assertEqual(old.iloc[0].market, 'Under 3.5')

    def test_v13_experiments_and_archive_reports_still_replay(self):
        from conservative_bet_filter import PREVIOUS_BALANCED_SELECTION_POLICY_VERSION
        from unittest.mock import patch
        with patch(__name__+'.PROBABILITY_SELECTION_POLICY_VERSION', PREVIOUS_BALANCED_SELECTION_POLICY_VERSION):
            ProbabilityShortlistTests('test_new_experiments_capture_replay_and_reporting_include_control_without_ev_gate').test_new_experiments_capture_replay_and_reporting_include_control_without_ev_gate()

    def test_both_probability_and_ev_contribute_to_the_score(self):
        rows = [only_over_goal(i) for i in range(4)]
        for row, probability, ev in zip(rows, [.95,.90,.85,.70], [-.03,.30,.15,.05]):
            row.update(p_over_1_5=probability, raw_p_over_1_5=probability-.02,
                       market_over_1_5_odds=(1+ev)/probability)
        picks, _, summary = self.select(rows)
        self.assertEqual(picks.fixture_id.tolist(), ['fixture-1','fixture-0','fixture-2','fixture-3'])
        self.assertAlmostEqual(picks.iloc[0].selection_score, .875)
        self.assertAlmostEqual(picks.iloc[0].probability_percentile, .75)
        self.assertAlmostEqual(picks.iloc[0].ev_percentile, 1.)
        self.assertEqual(summary['shortlist_lookahead_hours'], 48)
        self.assertEqual(summary['selection_objective'], 'BALANCED_PROBABILITY_EV')
        self.assertTrue(summary['selected_matches_within_48_hours'])
        self.assertFalse(summary['ev_required_for_selection'])
        self.assertFalse(summary['ranking_is_empirically_optimized'])
        # Repeating a provider row does not change the ranking population.
        repeated, _, _ = self.select([*rows, dict(rows[0], fixture_id='duplicate')])
        self.assertEqual(repeated.selection_score.tolist(), picks.selection_score.tolist())
        self.assertEqual(repeated.fixture_id.tolist(), picks.fixture_id.tolist())

    def test_48_hour_bounds_are_anchored_to_generation_and_legacy_stays_72(self):
        rows = [only_over_goal(i) for i in range(4)]
        for row, delta in zip(rows, [timedelta(minutes=19),timedelta(minutes=20),
                                    timedelta(hours=48),timedelta(hours=48,seconds=1)]):
            row['kickoff_utc'] = (NOW+delta).isoformat()
        picks, _, summary = self.select(rows)
        self.assertEqual(set(picks.fixture_id), {'fixture-1','fixture-2'})
        self.assertEqual(summary['shortfall'], 10)
        self.assertEqual(pd.Timestamp(summary['shortlist_window_end_utc']), pd.Timestamp(NOW)+pd.Timedelta(hours=48))
        legacy, _, old_summary = select(rows, {'Premier League':sample_report()})
        self.assertIn('fixture-3', legacy.fixture_id.tolist())
        self.assertEqual(old_summary['shortlist_lookahead_hours'], 72)

    def test_twelve_are_selected_without_probability_or_ev_cutoff(self):
        rows = [dict(only_over_goal(i), kickoff_utc=(NOW+timedelta(hours=24)).isoformat()) for i in range(15)]
        for row in rows:
            row.update(p_over_1_5=.60, raw_p_over_1_5=.55, market_over_1_5_odds=1.05)
        picks, decisions, summary = self.select(rows)
        self.assertEqual(len(picks), 12)
        self.assertTrue(picks.conservative_estimated_ev.lt(0).all())
        self.assertTrue(picks.selection_tier.eq('PROVISIONAL').all())
        self.assertTrue(picks.selection_score.is_monotonic_decreasing)
        self.assertEqual(summary['shortfall'], 0)
        filtered, other, _ = self.select(rows, adjusted_ev_floor=.015)
        self.assertTrue(filtered.empty)
        # Experimental EV gates must not change the underlying score population.
        self.assertEqual(decisions.selection_score.tolist(), other.selection_score.tolist())

    def test_balanced_experiments_and_archive_reports_replay(self):
        from unittest.mock import patch
        # Exercise the same capture/grading/report checks under the new policy.
        with patch(__name__+'.PROBABILITY_SELECTION_POLICY_VERSION', BALANCED_SELECTION_POLICY_VERSION):
            ProbabilityShortlistTests('test_new_experiments_capture_replay_and_reporting_include_control_without_ev_gate').test_new_experiments_capture_replay_and_reporting_include_control_without_ev_gate()

