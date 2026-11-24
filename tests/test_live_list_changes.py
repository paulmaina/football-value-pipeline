"""Live list changes released immediately (Paul, 24 Nov 2026; docs/plan.md Phase 4d).

Part 1: odds above 1.20 and at most 2.00 for the value shortlist (local-research-profit-120-200-dc12-v3), the cagey
tier (no-loss-market-reference-120-200-v6) and the strong master's executable pool (master-strong-team-v2). The rules
they replace (v2, v5, master-strong-team-v1) stay registered, and runs replay under the rule they recorded.
"""
from __future__ import annotations

import copy
import hashlib
import json
import subprocess
import unittest
from pathlib import Path

from offline_test_case import OfflineQuotePolicyTestCase
from test_price_edge_shortlist import NOW
from test_team_research_profit import researched
import cagey_tier_v3 as tier
import master_shortlist
import master_strong as ms
import price_edge_cagey_shortlist as v28
import profit_shortlist as ps

REPO = Path(__file__).resolve().parents[1]


class ValueFloorTest(OfflineQuotePolicyTestCase):
    def test_v3_needs_odds_above_1_20_and_v2_keeps_1_15(self):
        row = researched()
        for rule, price, eligible in [(ps.RULE_V3, 1.20, False), (ps.RULE_V3, 1.2001, True), (ps.RULE_V3, 2.0, True),
                                      (ps.RULE_V3, 2.0001, False), (ps.RULE_V2, 1.18, True), (ps.RULE_V2, 1.15, False)]:
            item = {'market': 'Home win', 'handicap_side': 'home', 'handicap_line': -.5,
                    'offered_decimal_odds': price, 'offered_last_update_utc': NOW.isoformat()}
            with self.subTest(rule=rule, price=price):
                out = ps.annotate(row, item, NOW, 0, rule=rule)
                self.assertEqual(out['decision'] == 'ELIGIBLE', eligible, out['rejection_reasons'])
        out = ps.annotate(row, {'market': 'Home win', 'handicap_side': 'home', 'handicap_line': -.5,
                                'offered_decimal_odds': 1.18, 'offered_last_update_utc': NOW.isoformat()}, NOW, 0,
                          rule=ps.RULE_V3)
        self.assertEqual(out['rejection_reasons'], 'offered odds must be greater than 1.20')

    def test_v3_is_a_local_research_rule_everywhere(self):
        self.assertIn(v28.VALUE_RULE_LOCAL_RESEARCH_120, v28.PROFIT_RULES)
        self.assertEqual(v28.VALUE_RULE_LOCAL_RESEARCH_120, ps.RULE_V3)
        self.assertEqual(v28.market_group({'market': 'Double Chance 1X', 'handicap_line': .5},
                                          rule=v28.VALUE_RULE_LOCAL_RESEARCH_120), v28.GROUP_DC)


class CageyFloorTest(OfflineQuotePolicyTestCase):
    def test_v6_needs_odds_above_1_20_and_v5_keeps_1_15(self):
        from test_cagey_market_basis_v5 import context, pin
        from test_cagey_no_loss_v4 import sample, POLICY, item, NOW as CAGEY_NOW
        for rule, price, accepted in [(tier.RULE_MARKET_BASIS_120, 1.20, False),
                                      (tier.RULE_MARKET_BASIS_120, 1.200001, True),
                                      (tier.RULE_MARKET_BASIS_120, 2.0, True),
                                      (tier.RULE_MARKET_BASIS, 1.18, True), (tier.RULE_MARKET_BASIS, 1.15, False)]:
            candidate = item(price=price)
            tier.annotate(candidate, context(), sample(), CAGEY_NOW, POLICY, 0., rule=rule, pin=pin())
            with self.subTest(rule=rule, price=price):
                self.assertEqual(candidate['cagey_tier_decision'] == 'ELIGIBLE', accepted, candidate['cagey_tier_reasons'])
                self.assertEqual(candidate['cagey_tier_rule'], rule)
        candidate = item(price=1.18)
        tier.annotate(candidate, context(), sample(), CAGEY_NOW, POLICY, 0., rule=tier.RULE_MARKET_BASIS_120, pin=pin())
        self.assertIn('cagey offered odds outside (1.20, 2.00]', candidate['cagey_tier_reasons'])
        candidate = item(price=1.10)
        tier.annotate(candidate, context(), sample(), CAGEY_NOW, POLICY, 0., rule=tier.RULE_MARKET_BASIS, pin=pin())
        self.assertIn('cagey offered odds outside (1.15, 2.00]', candidate['cagey_tier_reasons'])

    def test_v6_is_a_market_basis_rule_for_settlement_and_staking(self):
        row = {'cagey_tier_rule': tier.RULE_MARKET_BASIS_120, 'market': 'Over 1.5'}
        self.assertEqual(v28.settlement_basis(row, 'cagey'), 'uncorrected_matrix')
        self.assertIn(tier.RULE_MARKET_BASIS_120, tier.EXPANDED_RULES)
        self.assertEqual(tier.columns(tier.RULE_MARKET_BASIS_120), tier.columns(tier.RULE_MARKET_BASIS))


class LiveConfigTest(unittest.TestCase):
    def test_the_live_config_uses_v3_and_v6(self):
        settings = v28.load_settings()
        self.assertEqual((settings['value_rule'], settings['cagey_tier_rule']),
                         (ps.RULE_V3, tier.RULE_MARKET_BASIS_120))

    def test_the_strong_master_has_its_own_window_since_v2(self):
        for config in (ms.load_config(), ms.load_config(version='master-strong-team-v2')):
            self.assertEqual((config['execution']['min_odds_exclusive'], config['execution']['max_odds_inclusive']),
                             (1.2, 2.0))
        self.assertNotIn('execution', ms.load_config(version='master-strong-team-v1'))
        self.assertEqual(master_shortlist.STRONG_LIVE_VERSIONS['master-strong-team-v2'], 'master-strong-team-v2-live-v12')
        self.assertEqual(master_shortlist.STRONG_LIVE_VERSIONS[ms.VERSION], master_shortlist.VERSION_STRONG_LIVE)
        self.assertEqual(set(master_shortlist.STRONG_LIVE_VERSIONS), set(ms.VERSIONS))


class StrongVersionTest(unittest.TestCase):
    def test_every_superseded_rule_has_its_config_frozen(self):
        for version in ms.VERSIONS[:-1]:
            with self.subTest(version=version):
                self.assertEqual(ms.load_config(version=version)['version'], version)
                self.assertTrue((ms.RULES_DIR / f'{version}.json').exists())
        with self.assertRaisesRegex(ValueError, 'Unknown strong master rule'):
            ms.load_config(version='master-strong-team-v0')

    def test_v1_is_frozen_exactly_as_released(self):
        """The config v1 runs recorded (summary config_sha256) is the one main had before the change."""
        try:
            released = subprocess.run(['git', 'show', '121d64bfa:master_strong_config.json'], cwd=REPO, check=True,
                                      capture_output=True, stdin=subprocess.DEVNULL).stdout
        except (OSError, subprocess.CalledProcessError):
            self.skipTest('git history unavailable')
        digest = lambda c: hashlib.sha256(json.dumps(c, sort_keys=True).encode()).hexdigest()
        self.assertEqual(digest(ms.load_config(version='master-strong-team-v1')), digest(json.loads(released)))

    def test_live_versions_map_back_to_their_rule(self):
        for rule, live in master_shortlist.STRONG_LIVE_VERSIONS.items():
            self.assertEqual(master_shortlist.strong_rule(live), rule)
        self.assertIsNone(master_shortlist.strong_rule(master_shortlist.VERSION_NEW_LIVE))


class StrongExecutionTest(unittest.TestCase):
    def test_v2_overrides_only_the_odds_window(self):
        import master_reconciliation as mr
        base = mr.load_config()
        v2 = ms.execution_config(base, ms.load_config())
        self.assertEqual(v2['execution']['min_odds_exclusive'], 1.2)
        self.assertEqual({k: v for k, v in v2.items() if k != 'execution'}, {k: v for k, v in base.items()
                                                                             if k != 'execution'})
        self.assertEqual(base['execution']['min_odds_exclusive'], 1.15)  # today's master (shadow) as it is
        v1 = ms.execution_config(base, ms.load_config(version='master-strong-team-v1'))
        self.assertEqual(v1, base)
        record = {'bookmaker': 'Pinnacle', 'offered_decimal_odds': 1.18, 'market': 'Home win', 'source_market': 'h2h'}
        self.assertEqual(mr.executable(record, v2), 'offered odds outside (1.20, 2.00]')
        self.assertEqual(mr.executable(record, base), None)
        self.assertEqual(mr.executable({**record, 'offered_decimal_odds': 1.12}, base), 'offered odds outside (1.15, 2.00]')

    def test_the_live_strong_master_leaves_offers_at_1_20_or_below_unpicked(self):
        """On a production-shaped run, an offer priced at 1.20 or below is never picked by v2, while v1 (replay of
        runs before 24 Nov 2026) still applies 1.15."""
        import master_reconciliation as mr
        import pandas as pd
        from test_master_reconciliation import production_run
        predictions, decisions, summary = production_run()
        shortlisted = decisions.decision.eq('SHORTLISTED') | decisions.cagey_tier_decision.eq('SHORTLISTED')
        pinnacle = decisions.bookmaker.eq('Pinnacle')
        index = decisions.index[shortlisted & pinnacle][0]
        decisions = decisions.copy()
        decisions.loc[index, 'offered_decimal_odds'] = 1.19
        v2 = ms.live_frame(decisions, predictions, None, summary['generated_at_utc'])
        v1 = ms.live_frame(decisions, predictions, None, summary['generated_at_utc'],
                           config=ms.load_config(version='master-strong-team-v1'))
        at = lambda frame: frame.loc[pd.to_numeric(frame.offered_decimal_odds).eq(1.19)]
        self.assertTrue(len(at(v2)))
        self.assertTrue(at(v2).new_master_decision.eq('NOT_EXECUTABLE').all())
        self.assertTrue(at(v2).new_master_reason.eq('offered odds outside (1.20, 2.00]').all())
        self.assertFalse(at(v1).new_master_reason.astype(str).str.contains('outside').any())
        self.assertEqual(mr.load_config()['execution']['min_odds_exclusive'], 1.15)


class StrongReplayTest(unittest.TestCase):
    def test_a_v1_run_replays_under_v1_and_a_new_run_is_v2(self):
        import warnings
        from test_master_reconciliation import production_run
        predictions, decisions, summary = production_run()
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            _, old = master_shortlist.strong_live(decisions, None, summary['generated_at_utc'], predictions,
                                                  rule='master-strong-team-v1')
            _, new = master_shortlist.strong_live(decisions, None, summary['generated_at_utc'], predictions)
        self.assertEqual((old['version'], old['rule']), ('master-strong-team-v1-live-v11', 'master-strong-team-v1'))
        self.assertNotIn('execution', old['strong'])
        self.assertEqual((new['version'], new['rule']), (master_shortlist.VERSION_STRONG_LIVE, ms.VERSION))
        self.assertEqual(new['strong']['execution'], {'min_odds_exclusive': 1.2, 'max_odds_inclusive': 2.0})
        self.assertEqual(old['strong']['config_sha256'],
                         hashlib.sha256(json.dumps(ms.load_config(version='master-strong-team-v1'),
                                                   sort_keys=True).encode()).hexdigest())


class ActivityTest(unittest.TestCase):
    def test_the_first_run_under_a_new_rule_logs_its_release_once(self):
        import model_activity as ma
        summary = {'master_shortlist': {'rule': ms.VERSION, 'version': master_shortlist.VERSION_STRONG_LIVE},
                   'value_rule': ps.RULE_V3, 'cagey_tier_rule': tier.RULE_MARKET_BASIS_120}
        line = ma.rule_release_event([], summary, '2026-11-24T12:00:00Z')
        self.assertEqual((line['event'], line['key']), (ma.RELEASE, f'release:rule {ms.VERSION}'))
        self.assertEqual(line['data']['versions']['after'], master_shortlist.VERSION_STRONG_LIVE)
        self.assertIsNone(ma.rule_release_event([line], summary))
        old = {'master_shortlist': {'rule': 'master-strong-team-v1'}}
        self.assertIsNone(ma.rule_release_event([], old))
        self.assertIn(ms.VERSION, ma.RULE_RELEASES)


# ---------------------------------------------------------------------------
# Part 2: research no-loss >= 0.70 for every strong-master pick (master-strong-team-v3)
# ---------------------------------------------------------------------------

class ResearchGateTest(unittest.TestCase):
    def test_every_tier_needs_research_no_loss_at_least_0_70(self):
        from test_master_strong import offer, config, RUN
        cfg = config()
        self.assertEqual(cfg['research_gate']['min_research_no_loss'], 0.7)
        rows = [offer('m1', research=.69), offer('m2', research=None), offer('m3', research=.70),
                offer('m4', no_loss=.55, profit=.55, research=.60), offer('m5', no_loss=.55, profit=.50, research=.90)]
        ms.select(rows, cfg, RUN)
        by = {r['_match']: r for r in rows}
        self.assertEqual((by['m1']['strong_decision'], by['m1']['strong_reason']),
                         ('LEFT_OUT', 'research gate: research no-loss below 0.70'))
        self.assertEqual((by['m2']['strong_decision'], by['m2']['strong_reason']),
                         ('LEFT_OUT', 'research gate: no research view'))
        self.assertEqual(by['m3']['strong_decision'], 'SHORTLISTED')
        # The fill would take m4 (the list is short), but the gate covers every tier.
        self.assertEqual(by['m4']['strong_reason'], 'research gate: research no-loss below 0.70')
        self.assertEqual((by['m5']['strong_decision'], by['m5']['strong_tier']), ('SHORTLISTED', 'not proven: fill'))
        self.assertIs(by['m1']['strong_r3_check'], False)  # domestic offers carry the check since v3
        self.assertIs(by['m3']['strong_r3_check'], True)

    def test_rules_before_v3_have_no_gate(self):
        from test_master_strong import offer, RUN
        old = copy.deepcopy(ms.load_config(version='master-strong-team-v2'))
        old['checks']['strong_team']['E'] = RUN['E']
        old['research_roles']['R1_research_strength'].update(G=RUN['G'])
        rows = [offer('m1', research=.50), offer('m2', research=None, no_loss=.6, profit=.6)]
        for row in rows:
            ms.annotate(row, {'elo_home_expectancy': .7, 'history': {}, 'teams': {}, 'h2h': [], 'research_margin': 1.},
                        config=old, trust='trusted', european=False, E=RUN['E'], G=RUN['G'])
        ms.select(rows, old, RUN)
        self.assertEqual([r['strong_decision'] for r in rows], ['SHORTLISTED', 'SHORTLISTED'])
        self.assertIsNone(rows[0]['strong_r3_check'])  # v2: R3 on UCL/UEL only

    def test_the_summary_counts_offers_left_out_by_the_gate(self):
        import pandas as pd
        from test_master_strong import offer, config, RUN
        cfg = config()
        rows = [offer('m1', research=.69), offer('m2', research=None), offer('m3', research=.80)]
        ms.select(rows, cfg, RUN)
        frame = pd.DataFrame(rows).assign(strong_master_version=cfg['version'], in_live_master=False,
                                          live_master_same_offer=False, unvalidated_view=False)
        info = ms.summary(frame, cfg)
        self.assertEqual(info['research_gate'], {'min_research_no_loss': 0.7, 'left_out_offers': 2,
                                                 'left_out_no_research_view': 1, 'left_out_matches': 2})
        old = ms.summary(frame, ms.load_config(version='master-strong-team-v2'))
        self.assertNotIn('research_gate', old)

    def test_live_version_v3(self):
        self.assertEqual(master_shortlist.STRONG_LIVE_VERSIONS['master-strong-team-v3'], 'master-strong-team-v3-live-v13')
        self.assertIn('research_gate', ms.load_config())  # every later rule keeps the gate
        self.assertEqual(ms.load_config(version='master-strong-team-v2')['execution']['min_odds_exclusive'], 1.2)
        self.assertNotIn('research_gate', ms.load_config(version='master-strong-team-v2'))


class ResearchGateReviewTest(unittest.TestCase):
    def frame(self, n, won, no_loss):
        import pandas as pd
        return pd.DataFrame({'result_status': ['WON'] * won + ['LOST'] * (n - won),
                             'ranking_no_loss_probability': [no_loss] * n})

    def test_waits_for_50_graded_picks_then_compares_with_the_left_out_offers(self):
        import price_edge_tracking as pet
        cfg = ms.load_config()
        waiting = pet.research_gate_review(self.frame(49, 40, .8), self.frame(10, 5, .8), cfg)
        self.assertEqual((waiting['status'], waiting['graded_picks']), ('WAITING', 49))
        self.assertIsNone(waiting['picks_minus_left_out_points'])
        ready = pet.research_gate_review(self.frame(50, 45, .8), self.frame(10, 7, .8), cfg)
        self.assertEqual(ready['status'], 'READY FOR REVIEW')
        self.assertAlmostEqual(ready['picks']['difference_points'], 10.0)
        self.assertAlmostEqual(ready['left_out_by_gate']['difference_points'], -10.0)
        self.assertAlmostEqual(ready['picks_minus_left_out_points'], 20.0)
        self.assertTrue(any('Research gate review: ready' in line for line in pet.research_gate_lines(ready)))
        self.assertIsNone(pet.research_gate_review(self.frame(50, 45, .8), None,
                                                   ms.load_config(version='master-strong-team-v2')))

    def test_half_wins_and_refunds_are_not_losses(self):
        import pandas as pd
        import price_edge_tracking as pet
        frame = pd.DataFrame({'result_status': ['HALF_WON', 'REFUNDED', 'HALF_LOST', None],
                              'ranking_no_loss_probability': [.75, .75, .75, .75]})
        gap = pet.no_loss_gap(frame)
        self.assertEqual(gap['n'], 3)
        self.assertAlmostEqual(gap['observed_no_loss'], 2 / 3)


# ---------------------------------------------------------------------------
# Part 3: proven ranking without league trust (master-strong-team-v4)
# ---------------------------------------------------------------------------

class ProvenOrderTest(unittest.TestCase):
    def proven(self, match, elo, wins, profit, trust='trusted', market='Home win', **extra):
        from test_master_strong import offer, evidence
        side = 'away' if market in ('Away win', 'Double Chance X2') else 'home'
        return offer(match, market=market, profit=profit, trust=trust,
                     ev=evidence(elo=elo, wins=wins, side=side), **extra)

    def test_elo_then_record_share_then_chance_of_profit(self):
        from test_master_strong import config, RUN
        rows = [self.proven('m1', .70, 8, .95), self.proven('m2', .80, 7, .60, trust='not trusted'),
                self.proven('m3', .70, 10, .70), self.proven('m4', .70, 8, .99)]
        self.assertTrue(all(ms.proven(r, RUN) for r in rows))
        ms.select(rows, config(), RUN)
        order = [r['_match'] for r in sorted(rows, key=lambda r: r['strong_rank'])]
        # m2: highest Elo (league not trusted no longer matters); m3: best record at Elo .70; m4 over m1 on profit.
        self.assertEqual(order, ['m2', 'm3', 'm4', 'm1'])
        self.assertIn('league not trusted', next(r for r in rows if r['_match'] == 'm2')['strong_labels'])

    def test_record_share_is_won_share_for_win_bets_and_not_lost_share_for_no_loss_bets(self):
        self.assertEqual(ms.record_share({'strong_bet_kind': 'win', 'strong_record_won_share': .7,
                                          'strong_record_not_lost_share': .9}), .7)
        self.assertEqual(ms.record_share({'strong_bet_kind': 'no loss', 'strong_record_won_share': .7,
                                          'strong_record_not_lost_share': .9}), .9)

    def test_rules_before_v4_rank_proven_picks_by_league_trust_first(self):
        from test_master_strong import config, RUN
        old = copy.deepcopy(config())
        old.pop('proven_order')
        rows = [self.proven('m1', .70, 8, .95), self.proven('m2', .80, 7, .60, trust='not trusted')]
        ms.select(rows, old, RUN)
        self.assertEqual([r['_match'] for r in sorted(rows, key=lambda r: r['strong_rank'])], ['m1', 'm2'])

    def test_the_fill_keeps_league_trust_first(self):
        from test_master_strong import offer, config, RUN
        rows = [offer('m1', no_loss=.6, profit=.70, trust='not trusted'), offer('m2', no_loss=.6, profit=.60)]
        ms.select(rows, config(), RUN)
        self.assertEqual([r['_match'] for r in sorted(rows, key=lambda r: r['strong_rank'])], ['m2', 'm1'])
        self.assertTrue(all(r['strong_tier'] == 'not proven: fill' for r in rows))

    def test_live_version_v4(self):
        self.assertEqual(master_shortlist.STRONG_LIVE_VERSIONS['master-strong-team-v4'], 'master-strong-team-v4-live-v14')
        self.assertIn('proven_order', ms.load_config())
        self.assertNotIn('proven_order', ms.load_config(version='master-strong-team-v3'))
        self.assertIn('research_gate', ms.load_config(version='master-strong-team-v3'))


if __name__ == '__main__':
    unittest.main()
