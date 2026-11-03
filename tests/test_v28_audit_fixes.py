"""Regressions for the end-to-end audit: timing, chronology, costs, sizing and replay."""
import json
import tempfile
from pathlib import Path

import pandas as pd

from offline_test_case import OfflineQuotePolicyTestCase
import price_edge_cagey_shortlist as v28
import price_edge_tracking as tracking
from performance_tracking import frozen_rows
from shortlist_replay import monitoring_equivalent
import staking
from test_price_edge_cagey_shortlist import cagey_row, tier_fair
from test_price_edge_shortlist import NOW, FRESH, POLICY, ah_pair, offer, row, fit_price
from workflow_checks import raw_check


def build(data, *, revision=2, cost=0, switches=None, monitor=None):
    return v28.build_shortlist(pd.DataFrame([data]), NOW,
        execution_policy={**POLICY, 'per_stake_cost_bps': cost},
        settings={'price_edge_execution_version': revision, **(switches or {})}, monitor=monitor)


def tier_fixture():
    fair, _ = tier_fair(cagey_row(), 'away', 2.0)
    return cagey_row(offers=ah_pair(-2.0, 4.5, 1.28) +
                     [offer('away', 2.0, fair['corrected_fair_odds'] * 1.005)])


class ExecutionTests(OfflineQuotePolicyTestCase):
    def test_direct_quote_cannot_hide_twelve_hour_old_corrected_inputs(self):
        data = tier_fixture()
        quotes = json.loads(data['price_edge_quotes'])
        quotes[1]['last_update_utc'] = (NOW - pd.Timedelta(hours=12)).isoformat()
        data['price_edge_quotes'] = json.dumps(quotes)
        old, old_decisions, old_summary = build(data, revision=1)
        self.assertEqual(len(v28.cagey_tier_list(old_decisions)), 1)
        self.assertNotIn('price_edge_execution_version', old_summary)
        monitor = []
        current, decisions, summary = build(data, monitor=monitor)
        self.assertEqual(monitor[0]['status'], 'UNUSABLE')
        self.assertIn('more than 10 minutes apart', monitor[0]['exclusion_reason'])
        self.assertEqual(len(v28.cagey_tier_list(decisions)), 0)
        candidate = decisions[(decisions.bookmaker == '1xBet') & (decisions.handicap_line == 2)].iloc[0]
        self.assertEqual(candidate.quote_skew_minutes, 0)  # direct reference alone still looks fresh
        self.assertGreater(candidate.corrected_input_quote_skew_minutes, 700)
        self.assertIn('corrected distribution inputs', candidate.cagey_tier_reasons)
        self.assertEqual(summary['price_edge_execution_version'], 2)

    def test_synchronized_fixture_still_qualifies_and_sizes(self):
        selected, decisions, _ = build(tier_fixture())
        tier = v28.cagey_tier_list(decisions)
        self.assertEqual(len(tier), 1)
        self.assertEqual(tier.iloc[0].corrected_input_timing_status, 'SYNCHRONIZED')
        plan = staking.stake_recommendations(tier.assign(selection_tier='STRICT'))
        self.assertNotEqual(plan.iloc[0].staking_status, 'NO_STAKE_INVALID_INPUT')
        self.assertEqual(plan.iloc[0].probability_basis, 'cagey_corrected_margin_distribution')

    def test_fit_a_timing_ignores_the_unused_bad_main_ah_quote(self):
        data = tier_fixture()
        offers = json.loads(data['asian_handicap_offers'])
        for item in offers:
            if item['market_key'] == 'spreads':
                item['last_update_utc'] = (NOW + pd.Timedelta(days=1)).isoformat()
        data['asian_handicap_offers'] = json.dumps(offers)
        records = []
        _, decisions, _ = build(data, monitor=records)
        [record] = records
        self.assertEqual(record['fit'], 'A')
        self.assertLessEqual(pd.Timestamp(record['latest_input_quote_utc']), NOW)
        self.assertEqual(len(v28.cagey_tier_list(decisions)), 1)

    def test_cost_is_frozen_and_can_reject_a_gross_positive_value_pick(self):
        odds = fit_price('home', 1.5)['fair_odds'] * 1.04
        data = row(offers=[offer('home', 1.5, odds)])
        gross, _, _ = build(data)
        self.assertEqual(len(gross), 1)
        selected, decisions, summary = build(data, cost=600)
        candidate = decisions[(decisions.bookmaker == '1xBet') & (decisions.handicap_line == 1.5)].iloc[0]
        self.assertEqual(len(selected), 0)
        self.assertEqual(candidate.per_stake_cost, 0.06)
        self.assertLess(candidate.corrected_expected_profit, 0)
        self.assertIn('after stake cost', candidate.rejection_reasons)
        # Historical v28 preserves its original zero-cost decisions and columns.
        legacy, _, _ = build(data, revision=1, cost=600)
        self.assertEqual(len(legacy), 1)
        self.assertEqual(legacy.iloc[0].per_stake_cost, 0)

    def test_cagey_cost_is_deducted_with_half_and_refund_settlement(self):
        _, before, _ = build(tier_fixture())
        self.assertEqual(len(v28.cagey_tier_list(before)), 1)
        _, after, _ = build(tier_fixture(), cost=100)
        self.assertEqual(len(v28.cagey_tier_list(after)), 0)
        part = after[(after.bookmaker == '1xBet') & (after.handicap_line == 2)].iloc[0]
        self.assertLess(part.corrected_expected_profit, 0)
        graded = tracking.settle({'per_stake_cost': 0.01}, {'home_goals': 2, 'away_goals': 0}, 'away', 2, 1.2)
        self.assertEqual(graded['result_status'], 'REFUNDED')
        self.assertEqual(graded['unit_profit'], -0.01)

    def test_cost_removes_refunds_and_unprofitable_half_wins_from_safety(self):
        _, context = tier_fair(cagey_row(), 'away', 2.0)
        gross = v28.corrected_price(context, 'away', 2.0, 1.2)
        net = v28.corrected_price(context, 'away', 2.0, 1.2, cost=0.001)
        self.assertAlmostEqual(net['corrected_no_loss_probability'],
                               gross['corrected_no_loss_probability'] - gross['corrected_p_push'])
        quarter = v28.corrected_price(context, 'away', 1.25, 1.2, cost=0.15)
        self.assertAlmostEqual(quarter['corrected_p_profit'], quarter['corrected_p_win'])
        self.assertGreater(quarter['corrected_p_half_win'], 0)

    def test_cost_without_a_distribution_and_disabled_switches_fails_closed(self):
        data = row(offers=[offer('home', 1.5, 1.2)], quotes=[])
        selected, decisions, _ = build(data, cost=100)
        self.assertTrue(selected.empty)
        self.assertTrue(decisions.per_stake_cost.eq(0.01).all())
        selected, decisions, _ = build(tier_fixture(), cost=100,
            switches={'cagey_correction_enabled': False, 'cagey_tier_enabled': False})
        self.assertTrue(selected.empty)
        self.assertTrue(decisions.per_stake_cost.eq(0.01).all())
        for version in (0, 3, True, '2'):
            with self.subTest(version=version), self.assertRaisesRegex(ValueError, 'execution version'):
                build(tier_fixture(), revision=version)


class ChronologyTests(OfflineQuotePolicyTestCase):
    def test_late_older_upload_cannot_replace_newer_tier_or_tagged_pick(self):
        kick = NOW + pd.Timedelta(hours=24)
        item = {**row(kickoff=kick), 'market': 'Asian Handicap Away +2.00', 'handicap_side': 'away',
                'handicap_line': 2.0, 'bookmaker': '1xBet', 'decision': 'SHORTLISTED',
                'selection_policy_version': v28.POLICY, 'any_tag': True}
        with tempfile.TemporaryDirectory() as tmp:
            root, archive = Path(tmp), []
            for sha, generated, captured, odds in (
                    ('a' * 40, NOW, NOW + pd.Timedelta(hours=1), 1.31),
                    ('b' * 40, NOW - pd.Timedelta(hours=2), NOW + pd.Timedelta(hours=2), 1.20),
                    ('c' * 40, NOW, NOW + pd.Timedelta(hours=3), 1.40),  # same generation: first capture wins
                    ('d' * 40, kick - pd.Timedelta(minutes=5), kick - pd.Timedelta(minutes=4), 2.0)):
                directory = root / 'performance' / 'snapshots' / sha[:16]
                directory.mkdir(parents=True)
                data = {**item, 'offered_decimal_odds': odds}
                pd.DataFrame([data]).to_csv(directory / tracking.TIER_FILE, index=False)
                tracking.write_list(pd.DataFrame([data]), directory, generated.isoformat())
                meta = {'git_commit_sha': sha, 'generated_at_utc': generated.isoformat(),
                        'captured_at_utc': captured.isoformat(), 'selection_policy_version': v28.POLICY,
                        'sha256': {tracking.TIER_FILE: 'x', tracking.FILE: 'x'}}
                archive.append((meta, [], [data]))
            self.assertEqual(frozen_rows(archive, 'shortlist', latest=True)[0]['offered_decimal_odds'], 1.31)
            for rows in (tracking.frozen_tier_picks(root, archive), tracking.frozen_candidates(root, archive)):
                self.assertEqual(float(rows[0]['offered_decimal_odds']), 1.31)
                self.assertEqual(pd.Timestamp(rows[0]['snapshot_generated_utc']), NOW)


class SizingTests(OfflineQuotePolicyTestCase):
    def test_v28_uses_the_complete_distribution_and_charges_cost_on_refunds(self):
        item = {'selection_policy_version': v28.POLICY, 'selection_tier': 'STRICT',
                'offered_decimal_odds': 1.53, 'handicap_side': 'home', 'handicap_line': 0,
                'predicted_probability': 0.99, 'rank_probability': 0.999, 'per_stake_cost': 0.01,
                'corrected_p_win': 0.495, 'corrected_p_half_win': 0.0, 'corrected_p_push': 0.257,
                'corrected_p_half_loss': 0.0, 'corrected_p_loss': 0.248}
        probabilities = staking.conservative_settlement(item)
        self.assertEqual(probabilities['full_win'], 0.495)
        self.assertEqual(probabilities['refund'], 0.257)
        plan = staking.stake_recommendations(pd.DataFrame([item]))
        self.assertAlmostEqual(plan.iloc[0].conservative_ev, 0.495 * 0.53 - 0.248 - 0.01)
        self.assertGreater(plan.iloc[0].stake_fraction, 0)
        for changes in ({'corrected_p_push': None}, {'corrected_p_win': 1.1},
                        {'corrected_p_push': 0.0}, {'corrected_input_timing_status': 'UNAVAILABLE_OR_UNSYNCHRONIZED'}):
            with self.subTest(changes=changes), self.assertRaises(ValueError):
                staking.conservative_settlement({**item, **changes})


class ReplayTests(OfflineQuotePolicyTestCase):
    def test_only_solver_fields_have_numerical_tolerance(self):
        expected = [{'corrected_p2': 0.2, 'home_plus_1_corrected_fair_odds': 3.13311793766082,
                     'home_plus_1_onexbet_odds': 1.2, 'kickoff_utc': FRESH, 'model_version': 'v1',
                     'monitoring_version': v28.MONITOR_VERSION, 'corrected_cagey_quintile': 'Q1 cagiest'}]
        actual = [{**expected[0], 'home_plus_1_corrected_fair_odds': 3.133117935937099}]
        self.assertTrue(monitoring_equivalent(actual, expected))
        for key, value in (('corrected_p2', 0.2001), ('home_plus_1_corrected_fair_odds', 3.134),
                           ('home_plus_1_corrected_fair_odds', float('nan')), ('corrected_p2', True),
                           ('home_plus_1_onexbet_odds', 1.200000002), ('model_version', 'v2'),
                           ('kickoff_utc', NOW.isoformat()), ('corrected_cagey_quintile', 'Q2')):
            with self.subTest(key=key, value=value):
                self.assertFalse(monitoring_equivalent([{**expected[0], key: value}], expected))
        self.assertFalse(monitoring_equivalent([], expected))
        self.assertFalse(monitoring_equivalent([{}], expected))
        self.assertFalse(monitoring_equivalent([None], expected))

    def test_raw_replays_old_and_new_runs_and_rejects_changed_monitoring(self):
        for revision in (1, 2):
            data = tier_fixture()
            predictions = pd.DataFrame([{**data, 'p_home': 0.45, 'p_draw': 0.27, 'p_away': 0.28}])
            monitor = []
            selected, decisions, summary = build(predictions.iloc[0].to_dict(), revision=revision, monitor=monitor)
            with tempfile.TemporaryDirectory() as tmp:
                root, raw = Path(tmp), Path(tmp) / 'raw'
                raw.mkdir()
                predictions.to_csv(raw / 'all_leagues_predictions.csv', index=False)
                selected.to_csv(raw / 'conservative_bet_shortlist.csv', index=False)
                v28.cagey_tier_list(decisions).to_csv(raw / v28.TIER_FILE, index=False)
                v28.record_monitoring(summary, monitor, raw)
                (raw / 'conservative_bet_summary.json').write_text(json.dumps(summary))
                self.assertEqual(raw_check(root)['selections'], len(selected))
                frame = pd.read_csv(raw / v28.MONITOR_FILE)
                original = frame.home_plus_1_corrected_fair_odds.copy()
                frame.home_plus_1_corrected_fair_odds += 2e-9
                frame.to_csv(raw / v28.MONITOR_FILE, index=False)
                raw_check(root)
                frame.home_plus_1_corrected_fair_odds = original + 0.001
                frame.to_csv(raw / v28.MONITOR_FILE, index=False)
                with self.assertRaisesRegex(ValueError, 'monitoring records differ'):
                    raw_check(root)
