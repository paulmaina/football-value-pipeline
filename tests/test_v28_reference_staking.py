"""v28 must size and charge costs against the matrix belonging to the pick's reference/list."""
import json
import tempfile
from pathlib import Path
from unittest.mock import patch

import pandas as pd

from offline_test_case import OfflineQuotePolicyTestCase
import market_implied as mi
import price_edge_cagey_shortlist as v28
import price_edge_shortlist as v27
import staking
from test_price_edge_shortlist import row, ah_pair, offer, NOW, POLICY, fit_price
from test_v28_audit_fixes import tier_fixture


def cases():
    return {
        'minus': row(offers=ah_pair(-0.75, 1.95, 1.95) + [offer('home', -0.75, 2.10)]),
        'pinnacle_plus': row(offers=ah_pair(1.5, 1.15, 6.5) + [offer('home', 1.5, 1.22)]),
        'c_cagey': row(offers=[offer('home', 1.5, fit_price('home', 1.5)['fair_odds'] * 1.04)]),
        'tier': tier_fixture(),
    }


def run(data, cost=0, settings=None):
    return v28.build_shortlist(pd.DataFrame([data]), NOW,
        execution_policy={**POLICY, 'per_stake_cost_bps': cost}, settings=settings)


class ReferenceSizingTests(OfflineQuotePolicyTestCase):
    def test_four_pick_types_use_their_own_distribution(self):
        for name, data in cases().items():
            with self.subTest(case=name):
                selected, decisions, _ = run(data)
                tier = 'cagey' if name == 'tier' else 'value'
                picks = v28.cagey_tier_list(decisions) if tier == 'cagey' else selected
                self.assertEqual(len(picks), 1)
                item = picks.iloc[0].to_dict()
                prefix = 'corrected' if name in ('c_cagey', 'tier') else 'uncorrected'
                self.assertEqual(v28.settlement_basis(item, tier), prefix + '_matrix')
                if name == 'c_cagey':
                    self.assertEqual(item['reference_type'], 'c-cagey')
                elif name == 'pinnacle_plus':
                    self.assertEqual(item['reference_type'], 'a')
                probs = staking.conservative_settlement(item, tier=tier)
                mapping = {'full_win': 'win', 'half_win': 'half_win', 'refund': 'push',
                           'half_loss': 'half_loss', 'full_loss': 'loss'}
                for key, suffix in mapping.items():
                    self.assertAlmostEqual(probs[key], item[prefix + '_p_' + suffix])
                if prefix == 'uncorrected':
                    pin = v27.pinnacle_quotes(data)
                    fit, _ = v27.market_fit(pin, NOW)
                    self.assertTrue(fit.usable)
                    expected = mi.price(fit, item['handicap_side'], item['handicap_line'])
                    self.assertAlmostEqual(probs['full_win'], expected['p_win'])
                    self.assertNotAlmostEqual(probs['full_win'], item['corrected_p_win'], places=5)
                plan = staking.stake_recommendations(picks, tier=tier)
                self.assertEqual(plan.iloc[0].probability_basis, prefix + '_matrix')
                self.assertNotIn(plan.iloc[0].staking_status,
                                 ('NO_STAKE_INVALID_INPUT', 'NO_STAKE_UNAVAILABLE_DISTRIBUTION', 'NO_STAKE_NOT_STRICT'))
                self.assertAlmostEqual(plan.iloc[0].conservative_ev,
                                       staking.settlement_ev(probs, item['offered_decimal_odds']))

    def test_missing_required_distribution_never_falls_back(self):
        for name, data in cases().items():
            selected, decisions, _ = run(data)
            tier = 'cagey' if name == 'tier' else 'value'
            picks = v28.cagey_tier_list(decisions) if tier == 'cagey' else selected
            prefix = 'corrected' if name in ('c_cagey', 'tier') else 'uncorrected'
            damaged = picks.copy()
            damaged[prefix + '_p_win'] = None
            plan = staking.stake_recommendations(damaged, tier=tier)
            self.assertEqual(plan.iloc[0].staking_status, 'NO_STAKE_UNAVAILABLE_DISTRIBUTION')
            self.assertEqual(plan.iloc[0].stake_fraction, 0)
            self.assertEqual(plan.iloc[0].probability_basis, prefix + '_matrix')

    def test_fit_a_cannot_substitute_for_uncorrected_fit_b(self):
        data = cases()['pinnacle_plus']
        offers = json.loads(data['asian_handicap_offers'])
        for item in offers:
            if item['market_key'] == 'spreads':
                item['last_update_utc'] = (NOW - pd.Timedelta(days=2)).isoformat()
        data['asian_handicap_offers'] = json.dumps(offers)
        selected, decisions, _ = run(data)
        pick = selected.iloc[0]
        self.assertEqual(pick.corrected_fit, 'A')
        self.assertTrue(pd.isna(pick.uncorrected_fit))
        self.assertEqual(staking.stake_recommendations(selected).iloc[0].staking_status,
                         'NO_STAKE_UNAVAILABLE_DISTRIBUTION')
        selected, decisions, _ = run(data, cost=1)
        self.assertTrue(selected.empty)
        candidate = decisions[decisions.bookmaker.eq('1xBet')].iloc[0]
        self.assertIn('net profit unavailable', candidate.rejection_reasons)

    def test_cost_rule_uses_uncorrected_value_and_corrected_c_cagey(self):
        data = cases()
        for name, cost, expected_pick in (('minus', 1, False), ('pinnacle_plus', 720, False),
                                           ('c_cagey', 450, True), ('tier', 20, True)):
            with self.subTest(case=name):
                selected, decisions, _ = run(data[name], cost=cost)
                candidates = decisions[decisions.bookmaker.eq('1xBet')]
                item = candidates.iloc[0]
                if name == 'tier':
                    picks = v28.cagey_tier_list(decisions)
                    self.assertEqual(bool(len(picks)), expected_pick)
                    plan = staking.stake_recommendations(picks, tier='cagey')
                    self.assertAlmostEqual(plan.iloc[0].conservative_ev, picks.iloc[0].corrected_expected_profit)
                else:
                    prefix = 'corrected' if name == 'c_cagey' else 'uncorrected'
                    self.assertEqual(item.value_probability_basis, prefix + '_matrix')
                    self.assertAlmostEqual(item.value_expected_profit, item[prefix + '_expected_profit'])
                    self.assertEqual(bool(len(selected)), expected_pick)
                    if name == 'pinnacle_plus':
                        self.assertLess(item.value_expected_profit, 0)
                        self.assertGreater(item.corrected_expected_profit, 0)
                    if name == 'c_cagey':
                        self.assertGreater(item.value_expected_profit, 0)
                        self.assertLess(item.uncorrected_expected_profit, 0)

    def test_overlap_is_sized_separately_and_files_clear_when_empty(self):
        selected, decisions, _ = run(cases()['tier'])
        cagey = v28.cagey_tier_list(decisions)
        # The very same row uses raw fit B in the value list and corrected in the cagey list.
        value = cagey.copy().assign(selection_tier='STRICT')
        self.assertEqual(value.iloc[0].reference_type, 'a')
        rejected = cagey.copy().assign(cagey_tier_decision='NOT_SELECTED', selection_tier='STRICT')
        self.assertEqual(staking.stake_recommendations(rejected, tier='cagey').iloc[0].staking_status,
                         'NO_STAKE_NOT_STRICT')
        with tempfile.TemporaryDirectory() as tmp:
            raw = Path(tmp)
            value_path, tier_path = staking.write_shortlist_stakes(value, cagey, raw, bankroll=250)
            self.assertEqual(value_path.name, staking.OUTPUT_FILE)
            self.assertEqual(tier_path.name, staking.CAGEY_OUTPUT_FILE)
            self.assertEqual(pd.read_csv(value_path).iloc[0].probability_basis, 'uncorrected_matrix')
            plan = pd.read_csv(tier_path)
            self.assertEqual(plan.iloc[0].probability_basis, 'corrected_matrix')
            self.assertEqual(plan.iloc[0].bankroll_units, 250)
            self.assertEqual(plan.iloc[0].selection_tier, 'STRICT')
            staking.write_shortlist_stakes(value, cagey.iloc[0:0], raw)
            self.assertTrue(pd.read_csv(tier_path).empty)
        with self.assertRaisesRegex(ValueError, 'Unknown shortlist tier'):
            staking.stake_recommendations(cagey, tier='unknown')
        with self.assertRaisesRegex(ValueError, 'Unknown shortlist tier'):
            v28.settlement_basis({}, 'unknown')

    def test_switches_off_can_size_from_fit_b_without_a_correction(self):
        selected, _, _ = run(cases()['pinnacle_plus'], cost=10,
                             settings={'cagey_correction_enabled': False, 'cagey_tier_enabled': False})
        self.assertEqual(len(selected), 1)
        self.assertTrue(pd.isna(selected.iloc[0].corrected_fit))
        plan = staking.stake_recommendations(selected)
        self.assertEqual(plan.iloc[0].probability_basis, 'uncorrected_matrix')
        self.assertGreater(plan.iloc[0].stake_fraction, 0)

    def test_refresh_writes_cagey_only_stakes_preserves_settings_and_clears_disabled_list(self):
        from refresh_conservative_shortlist import _refresh
        from workflow_checks import raw_check
        settings = {'bankroll': 250, 'multiplier': 0.2, 'max_fraction': 0.01, 'max_total_exposure': 0.04}
        with tempfile.TemporaryDirectory() as tmp:
            root, raw = Path(tmp), Path(tmp) / 'raw'
            raw.mkdir()
            predictions = pd.DataFrame([{**tier_fixture(), 'p_home': 0.45, 'p_draw': 0.27, 'p_away': 0.28}])
            predictions.to_csv(raw / 'all_leagues_predictions.csv', index=False)
            (raw / 'conservative_bet_summary.json').write_text(json.dumps({'staking_settings': settings}))
            summary = _refresh(root, NOW)
            self.assertEqual(summary['staking_settings'], settings)
            self.assertEqual(summary['n_shortlisted'], 0)
            self.assertEqual(summary['cagey_tier']['n_shortlisted'], 1)
            tier_path = raw / staking.CAGEY_OUTPUT_FILE
            plan = pd.read_csv(tier_path)
            self.assertEqual(len(plan), 1)
            self.assertEqual(plan.iloc[0].probability_basis, 'corrected_matrix')
            self.assertEqual(plan.iloc[0].bankroll_units, 250)
            self.assertEqual(plan.iloc[0].kelly_multiplier, 0.2)
            raw_check(root)
            switches = {**v28.load_settings(), 'cagey_tier_enabled': False}
            with patch.object(v28, 'load_settings', return_value=switches):
                _refresh(root, NOW)
            self.assertTrue(pd.read_csv(tier_path).empty)
