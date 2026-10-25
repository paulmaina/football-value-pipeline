"""Shortlist v26: v22 common no-loss rules plus Corners totals under the same floors."""
import json
from pathlib import Path
import tempfile

import pandas as pd

import asian_handicap as ah
import corners_cards_shortlist as v25
import count_markets as cm
import no_loss_corners_shortlist as v26
from conservative_bet_filter import build_conservative_shortlist
from offline_test_case import OfflineQuotePolicyTestCase
from test_asian_handicap import NOW, POLICY as QUOTES, quote, row
from test_corners_cards_shortlist import count_row, evidence, offer
from test_win_first_shortlist import reports


def select(values, evidence_map, policy=v26.POLICY):
    return build_conservative_shortlist(pd.DataFrame(values), as_of=NOW, market_reliability=evidence_map,
                                        execution_policy=QUOTES, selection_policy_version=policy)


def corner(i, mu=12., price=1.5, opposite=2.6, line=8.5, side='Over'):
    return count_row(i, [offer(side=side, line=line, price=price, opposite=opposite)], mu=mu)


class NoLossCornersShortlistTests(OfflineQuotePolicyTestCase):
    def test_production_routing_keeps_archived_policies_replayable(self):
        self.assertEqual(ah.PRODUCTION_POLICY, v26.POLICY)
        self.assertEqual(ah.CORNERS_CARDS_POLICY, v25.POLICY)
        self.assertIn(v25.POLICY, ah.WIN_FIRST_POLICIES)
        self.assertNotIn(v26.POLICY, ah.WIN_FIRST_POLICIES)
        self.assertIn(v26.POLICY, ah.POLICIES)
        self.assertEqual(ah.ordinary_markets(v26.POLICY), ah.ordinary_markets(ah.POLICY))
        with self.assertRaises(ValueError):
            ah.build_shortlist(pd.DataFrame([row(0)]), NOW, reports(), QUOTES,
                               adjusted_ev_floor=.02, policy_version=v26.POLICY)

    def test_matches_v22_without_corner_quotes(self):
        values = [row(i, offers=[quote(price=1.7 + i/20)]) for i in range(4)]
        old, _, old_summary = select(values, reports(), ah.POLICY)
        new, _, summary = select(values, reports())
        self.assertEqual(len(new), 4)
        self.assertEqual(list(new.market), list(old.market))
        self.assertEqual(list(new.home_team), list(old.home_team))
        self.assertEqual(summary['selection_policy_version'], v26.POLICY)
        for key in ('min_adjusted_no_loss_probability', 'loss_risk_tolerance', 'min_raw_dc_ev'):
            self.assertEqual(summary[key], old_summary[key])
        self.assertEqual(summary['unproven_edge_selections'], 0)
        self.assertEqual(summary['min_estimated_ev'], .005)
        self.assertEqual(old_summary['min_estimated_ev'], .01)

    def test_qualifying_corner_is_selected_and_flagged_unproven(self):
        picks, decisions, summary = select([corner(0)], evidence())
        p = cm.probabilities(12., .02, 'corners')['Corners Over 8.5']
        self.assertEqual(list(picks.market), ['Corners Over 8.5'])
        pick = picks.iloc[0]
        self.assertTrue(pick.unproven_edge)
        self.assertIn('UNPROVEN EDGE', pick.selection_warnings)
        self.assertAlmostEqual(pick.loss_probability_upper, 1-p)
        self.assertAlmostEqual(pick.conservative_estimated_ev, p*1.5-1)
        self.assertEqual((pick.probability_basis, pick.p_refund), ('win', 0.))
        self.assertEqual(summary['unproven_edge_market_groups'], ['Corners'])
        self.assertEqual(summary['unproven_edge_selections'], 1)
        self.assertEqual(summary['negative_adjusted_ev_selections'], 0)
        self.assertIn('Corners Over 8.5', summary['eligible_markets'])
        self.assertFalse(any(m.startswith('Cards') for m in summary['eligible_markets']))
        self.assertEqual(summary['target_distinct_matches'], 12)

    def test_corners_face_the_common_probability_and_ev_floors(self):
        _, decisions, _ = select([corner(0, mu=11.)], evidence())
        unsafe = decisions.loc[decisions.market == 'Corners Over 8.5'].iloc[0]
        self.assertEqual(unsafe.decision, 'REJECTED')
        self.assertIn('adjusted probability of avoiding loss below 75%', unsafe.rejection_reasons)
        _, decisions, _ = select([corner(0, price=1.22, opposite=4.5)], evidence())
        thin = decisions.loc[decisions.market == 'Corners Over 8.5'].iloc[0]
        self.assertEqual(thin.decision, 'REJECTED')
        self.assertIn('adjusted EV below +0.5% or negative unblended EV', thin.rejection_reasons)
        penalised = evidence()
        penalised['Premier League']['count_markets']['corners']['markets']['Corners Over 8.5']['confidence_penalty'] = .07
        picks, _, _ = select([corner(0)], penalised)
        self.assertTrue(picks.empty)

    def test_half_percent_boundary_for_handicaps_and_corners_preserves_v22(self):
        from test_shortlist_market_alternatives import dc_fixture
        p = cm.probabilities(12., .02, 'corners')['Corners Over 8.5']
        for ev in (.00499, .005, .0075, .01):
            with self.subTest(ev=ev):
                ordinary, report = dc_fixture(ev=ev)
                picks, _, _ = select([ordinary], report)
                self.assertEqual(len(picks), int(ev >= .005))
                old, _, _ = select([ordinary], report, ah.POLICY)
                self.assertEqual(len(old), int(ev >= .01))
                price = (1+ev)/.85
                value = row(0, offers=[{**quote(point=.5, price=price),
                                       'opposite_price': 1/(1.04-1/price)}])
                picks, decisions, summary = select([value], reports())
                self.assertEqual(len(picks), int(ev >= .005))
                old, _, frozen = select([value], reports(), ah.POLICY)
                self.assertEqual(len(old), int(ev >= .01))
                self.assertEqual(frozen['min_estimated_ev'], .01)
                price = (1+ev)/p
                value = corner(0, price=price, opposite=1/(1.04-1/price))
                picks, _, summary = select([value], evidence())
                self.assertEqual(len(picks), int(ev >= .005))
                self.assertEqual(summary['min_estimated_ev'], .005)
                self.assertIn('+0.5%', summary['warning'])

    def test_per_market_approval_blocks_only_the_failed_line(self):
        values = [count_row(0, [offer(line=8.5, price=1.5, opposite=2.6),
                                offer(side='Under', line=12.5, price=1.4, opposite=2.9)], mu=10.)]
        picks, decisions, _ = select(values, evidence(failed=('Corners Over 8.5',)))
        blocked = decisions.loc[decisions.market == 'Corners Over 8.5'].iloc[0]
        self.assertIn('per-market approval: market audit UNRELIABLE_AUDIT', blocked.rejection_reasons)
        self.assertEqual(list(picks.market), ['Corners Under 12.5'])
        _, decisions, _ = select([corner(0)], reports())
        self.assertIn('per-market approval: market audit NOT_ASSESSED',
                      decisions.loc[decisions.market == 'Corners Over 8.5'].iloc[0].rejection_reasons)

    def test_failed_ordinary_market_is_labelled_per_market(self):
        evidence_map = reports()
        evidence_map['Premier League']['asian_handicap']['markets'][ah.label('home', 0)]['status'] = 'UNRELIABLE_AUDIT'
        picks, decisions, _ = select([row(0)], evidence_map)
        rejected = decisions.loc[decisions.market == ah.label('home', 0)].iloc[0]
        self.assertEqual(rejected.decision, 'REJECTED')
        self.assertIn('per-market approval: market audit UNRELIABLE_AUDIT', rejected.rejection_reasons)
        self.assertNotIn(ah.label('home', 0), list(picks.market))

    def test_cards_are_excluded_even_with_passing_evidence(self):
        value = count_row(0, [offer('cards', line=4.5, price=1.5, opposite=2.6)], kinds=('corners', 'cards'))
        value['league'] = 'Bundesliga'
        picks, decisions, _ = select([value], evidence(league='Bundesliga', kinds=('corners', 'cards')))
        self.assertFalse(decisions.market.astype(str).str.startswith('Cards').any())
        self.assertTrue(picks.empty or not picks.market.str.startswith('Cards').any())

    def test_lowest_loss_risk_wins_each_fixture(self):
        # The corner (18% loss) beats the handicap (15% no-loss risk + 30% refund) only when it is safer.
        safer = corner(0, mu=13., line=7.5, price=1.2, opposite=5.0)
        safer['asian_handicap_offers'] = json.dumps([quote()])
        picks, decisions, _ = select([safer], evidence())
        self.assertEqual(list(picks.market), ['Corners Over 7.5'])
        riskier = corner(0, mu=12.)
        riskier['asian_handicap_offers'] = json.dumps([quote()])
        picks, decisions, _ = select([riskier], evidence())
        self.assertEqual(list(picks.market), [ah.label('home', 0)])
        self.assertEqual(decisions.loc[decisions.market == 'Corners Over 8.5'].iloc[0].decision, 'NOT_SELECTED')

    def test_twelve_fixture_cap_without_market_quotas(self):
        values = [corner(i, mu=12. + i/10) for i in range(14)]
        for value in values:  # Keep every fixture inside the 48-hour window.
            value.update(kickoff_utc=values[0]['kickoff_utc'], date=values[0]['date'])
        picks, decisions, summary = select(values, evidence())
        self.assertEqual(len(picks), 12)
        self.assertEqual(set(picks.market), {'Corners Over 8.5'})
        self.assertEqual((summary['status'], summary['shortfall']), ('TARGET_MET', 0))
        self.assertEqual((decisions.decision == 'NOT_SELECTED').sum(), 2)
        # The safest fixtures (highest corner means) fill the cap.
        self.assertEqual(sorted(picks.home_team), sorted(pd.DataFrame(values).home_team.iloc[2:]))

    def test_readable_report_states_floors_and_unproven_edge(self):
        from format_football_output import process_conservative_shortlist
        picks, decisions, summary = select([corner(0), row(1)], evidence())
        self.assertEqual(len(picks), 2)
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory); raw = root/'raw'; out = root/'readable'; raw.mkdir(); out.mkdir()
            picks.to_csv(raw/'conservative_bet_shortlist.csv', index=False)
            decisions.to_csv(raw/'conservative_bet_rejections.csv', index=False)
            (raw/'conservative_bet_summary.json').write_text(json.dumps(summary, default=str))
            process_conservative_shortlist(raw, out)
            text = (out/'conservative_bet_shortlist_report.md').read_text()
        self.assertIn('**Common safety cutoff:** adjusted probability of avoiding any loss >= 75.0%', text)
        self.assertIn('**UNPROVEN EDGE (Corners):** validated on probability accuracy only', text)
        self.assertIn('1 of 2 selections', text)
