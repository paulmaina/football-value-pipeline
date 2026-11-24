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


# ---------------------------------------------------------------------------
# Part 4: weak-link flags, flag only (master-strong-team-v5)
# ---------------------------------------------------------------------------

def weak_rule(version=None):
    return ms.load_config(version=version)['weak_links']


def pick(**extra):
    row = {'_match': 'EPL|H|A|2026-11-25', 'strong_decision': 'SHORTLISTED', 'strong_tier': 'proven',
           'research_no_loss_probability': .82, 'cagey_no_loss_probability': .84, 'strong_record_matches': 10,
           'strong_elo_expectancy': .70, 'market': 'Home win', 'handicap_side': 'home', 'handicap_line': -.5}
    row.update(extra)
    return row


def forecast(h2h=(1.50, 4.20, 6.50), ah=(), research=None, kickoff='2026-11-25T20:00:00+00:00'):
    import json as _json
    quotes = [{'bookmaker': 'Pinnacle', 'market': 'h2h', 'prices': dict(zip(('home', 'draw', 'away'), h2h))}]
    offers = [{'bookmaker': 'Pinnacle', 'side': s, 'line': l, 'price': p, 'opposite_price': o} for s, l, p, o in ah]
    return {'league': 'EPL', 'home_team': 'H', 'away_team': 'A', 'kickoff_utc': kickoff,
            'price_edge_quotes': _json.dumps(quotes), 'asian_handicap_offers': _json.dumps(offers),
            'team_research_json': _json.dumps(research or {})}


class WeakLinkReasonTest(unittest.TestCase):
    def fire(self, row, forecast_row=None, warnings='', fallback=None, move=None, rule=None):
        import weak_links
        return weak_links.reasons(row, rule or weak_rule(), E=.55, forecast=forecast_row, warnings_text=warnings,
                                  fallback=fallback, move=move)

    def test_a_clean_proven_pick_has_no_reason_and_notes_missing_movement(self):
        fired, notes = self.fire(pick())
        self.assertEqual((fired, notes), ([], ['note: no movement data']))

    def test_each_reason(self):
        import weak_links
        cases = {
            'a': pick(research_no_loss_probability=.76, cagey_no_loss_probability=.84),
            'b': pick(research_no_loss_probability=.74, cagey_no_loss_probability=.76),
            'c': pick(cagey_no_loss_probability=None),
            'd': pick(strong_record_matches=7),
            'f': pick(strong_tier='not proven: fill'),
        }
        for letter, row in cases.items():
            with self.subTest(letter=letter):
                fired, _ = self.fire(row)
                self.assertIn(letter, weak_links.reason_letters('; '.join(fired)), fired)
        self.assertIn('d', weak_links.reason_letters('; '.join(self.fire(pick(strong_elo_expectancy=.58))[0])))
        self.assertNotIn('d', weak_links.reason_letters('; '.join(self.fire(pick(strong_elo_expectancy=.59))[0])))
        self.assertIn('c', weak_links.reason_letters('; '.join(self.fire(pick(), fallback='power fit B failed')[0])))
        self.assertEqual(self.fire(pick(research_no_loss_probability=.77, cagey_no_loss_probability=.84))[0], [])  # 7 points
        moved = {'now': .60, 'earliest': .63, 'earliest_generated_utc': '2026-11-24T06:00:00+00:00', 'drop_points': 3.0}
        fired, notes = self.fire(pick(), move=moved)
        self.assertEqual((weak_links.reason_letters('; '.join(fired)), notes), (['e'], []))
        self.assertEqual(self.fire(pick(), move={**moved, 'drop_points': 2.9})[0], [])

    def test_research_warnings_except_the_standing_note_and_stale_fits(self):  # v5: every warning counted
        import weak_links
        v5 = weak_rule('master-strong-team-v5')
        standing = v5['g']['standing_note']
        self.assertEqual(self.fire(pick(), warnings=standing, rule=v5)[0], [])
        fired, _ = self.fire(pick(), warnings=f'{standing}; Research review: lineup unconfirmed', rule=v5)
        self.assertEqual(fired, ['(g) research warning: Research review: lineup unconfirmed'])
        fired, _ = self.fire(pick(), warnings=f'{standing}; lineups unconfirmed; goals are not verified xG; '
                                              'goals are not verified xG', rule=v5)
        self.assertEqual(fired, ['(g) 2 research warnings: lineups unconfirmed | goals are not verified xG'])
        fired, _ = self.fire(pick(), forecast(research={'c6_fit': {'stale': True}}))
        self.assertEqual(fired, ['(g) stale research fit (C6)'])
        self.assertEqual(weak_links.reason_letters('(a) x; (g) y; (g) z; note: no movement data'), ['a', 'g'])


class NarrowedWeakLinkTest(unittest.TestCase):
    """Part 5 (master-strong-team-v6): (f) only the fill tiers; (g) only stale fits and match-specific review lines."""
    # The quality review's warnings as they reach the master (research_quality.assess, joined with '; ').
    ROUTINE = ('xg unavailable or unconfirmed; lineups unavailable or unconfirmed; availability unavailable or unconfirmed; '
               'Research review: starting XIs not freshly confirmed for both teams; check before betting tight AH; '
               'Research review: missing absence reports do not mean both teams have full squads; '
               'Research review: match-window weather missing, incomplete or stale; no numerical weather adjustment; '
               'Research review: home xG sample below five; goals are not verified xG; '
               'Research review: inspect training status RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED; '
               'completeness/freshness not established by this review; research older than 24 hours; refresh team news; '
               'research probability model has not passed a forward calibration gate')

    def fire(self, row, *args, **kw):
        return WeakLinkReasonTest.fire(None, row, *args, **kw)

    def test_v6_and_v5_are_frozen_and_differ_only_in_f_and_g(self):
        v5, v6 = weak_rule('master-strong-team-v5'), weak_rule('master-strong-team-v6')
        self.assertNotIn('tiers', v5['f'])
        self.assertNotIn('counted_review_warnings', v5['g'])
        same = lambda rule: {k: v for k, v in rule.items() if k not in ('f', 'g', 'narrowed')}
        self.assertEqual(same(v5), same(v6))  # a-e, the review and the standing note unchanged
        self.assertEqual(v5['g']['standing_note'], v6['g']['standing_note'])

    def test_f_only_for_the_fill_tiers(self):
        self.assertEqual(self.fire(pick(strong_tier='not proven: safe'))[0], [])
        self.assertEqual(self.fire(pick(strong_tier='proven'))[0], [])
        for tier in ('not proven: fill', 'not proven: risky fill'):
            self.assertEqual(self.fire(pick(strong_tier=tier))[0], [f'(f) {tier} tier'])
        v5 = weak_rule('master-strong-team-v5')
        self.assertEqual(self.fire(pick(strong_tier='not proven: safe'), rule=v5)[0], ['(f) not proven: safe tier'])

    def test_g_ignores_routine_coverage_and_standing_review_lines(self):
        self.assertEqual(self.fire(pick(), warnings=self.ROUTINE)[0], [])
        v5 = weak_rule('master-strong-team-v5')
        self.assertEqual(__import__('weak_links').reason_letters('; '.join(self.fire(pick(), warnings=self.ROUTINE,
                                                                                      rule=v5)[0])), ['g'])

    def test_g_counts_match_specific_review_lines_and_stale_fits(self):
        lines = ['Research review: home form/venue evidence is thin', 'Research review: away form/venue evidence is thin',
                 'Research review: training cutoff missing or not before evaluation',
                 'Research review: training health/status not recorded',
                 'Research review: training refresh warning; using cached evidence, inspect cutoff',
                 'Research review: pre-match deadline unavailable or passed']
        for line in lines:
            fired, _ = self.fire(pick(), warnings=f'{self.ROUTINE}; {line}')
            self.assertEqual(fired, [f"(g) research warning: {line.split('; ')[0]}"], line)
        fired, _ = self.fire(pick(), warnings=f'{self.ROUTINE}; {lines[0]}; {lines[1]}')
        self.assertEqual(fired, [f'(g) 2 research warnings: {lines[0]} | {lines[1]}'])
        fired, _ = self.fire(pick(), forecast(research={'ce3n_fit': {'stale': True}}), warnings=self.ROUTINE)
        self.assertEqual(fired, ['(g) stale research fit (CE3n)'])


class ProvenOnlyWeakLinkDTest(unittest.TestCase):
    """Part 6 (master-strong-team-v7): (d) fires only for picks in the 'proven' tier; every other reason is v6's."""
    THIN = {'strong_record_matches': 7}            # (d): record on fewer than 8 of the last 10
    NEAR_LINE = {'strong_elo_expectancy': .57}     # (d): Elo within 0.03 of E = 0.55

    def fire(self, row, *args, **kw):
        return WeakLinkReasonTest.fire(None, row, *args, **kw)

    def letters(self, row, rule=None):
        return __import__('weak_links').reason_letters('; '.join(self.fire(row, rule=rule)[0]))

    def test_the_live_rule_is_v7_and_v6_is_frozen(self):
        self.assertEqual(ms.VERSION, 'master-strong-team-v7')
        self.assertEqual(master_shortlist.VERSION_STRONG_LIVE, 'master-strong-team-v7-live-v17')
        self.assertEqual(master_shortlist.strong_rule('master-strong-team-v6-live-v16'), 'master-strong-team-v6')
        v6, v7 = weak_rule('master-strong-team-v6'), weak_rule()
        self.assertNotIn('tiers', v6['d'])
        self.assertEqual(v7['d']['tiers'], ['proven'])
        without = lambda rule, *keys: {k: v for k, v in rule.items() if k not in keys}
        self.assertEqual(without(v6, 'd', 'narrowed'), without(v7, 'd', 'narrowed'))  # a-c, e-g and the review
        self.assertEqual(without(v6['d'], 'rule'), without(v7['d'], 'rule', 'tiers'))  # thresholds unchanged

    def test_d_fires_for_proven_picks(self):
        for extra in (self.THIN, self.NEAR_LINE):
            self.assertEqual(self.letters(pick(**extra)), ['d'], extra)

    def test_d_never_fires_for_not_proven_picks(self):
        for tier in ('not proven: safe', 'not proven: fill', 'not proven: risky fill'):
            for extra in (self.THIN, self.NEAR_LINE, {**self.THIN, **self.NEAR_LINE}):
                with self.subTest(tier=tier, extra=extra):
                    expected = [] if tier == 'not proven: safe' else ['f']  # (f) as in v6
                    self.assertEqual(self.letters(pick(strong_tier=tier, **extra)), expected)
                    # v6 replays with v6's flags: (d) on every pick
                    self.assertIn('d', self.letters(pick(strong_tier=tier, **extra), weak_rule('master-strong-team-v6')))

    def test_other_reasons_unchanged_for_not_proven_picks(self):
        row = pick(strong_tier='not proven: safe', research_no_loss_probability=.74, cagey_no_loss_probability=None,
                   **self.THIN)
        self.assertEqual(self.letters(row), ['b', 'c'])
        self.assertEqual(self.letters(row, weak_rule('master-strong-team-v6')), ['b', 'c', 'd'])


class FairProbabilityTest(unittest.TestCase):
    def test_power_devig_of_the_pinnacle_quote_with_its_opposite(self):
        import weak_links
        from football_value_pipeline_v2_standalone import devig
        row = forecast(ah=[('home', -0.75, 1.80, 2.10)])
        h, d, a = devig([1.50, 4.20, 6.50], method='power')
        self.assertAlmostEqual(weak_links.fair_probability(row, 'Home win', 'home', -.5), h)
        self.assertAlmostEqual(weak_links.fair_probability(row, 'Double Chance X2', 'away', .5), d + a)
        pair = devig([1.80, 2.10], method='power')
        self.assertAlmostEqual(weak_links.fair_probability(row, 'Asian Handicap Home -0.75', 'home', -.75), pair[0])
        self.assertAlmostEqual(weak_links.fair_probability(row, 'Asian Handicap Away +0.75', 'away', .75), pair[1])
        self.assertIsNone(weak_links.fair_probability(row, 'Asian Handicap Home -1.00', 'home', -1.))
        self.assertIsNone(weak_links.fair_probability(None, 'Home win', 'home', -.5))


class MovementTest(unittest.TestCase):
    def archive(self, base, name, generated, captured, rows):
        import json as _json
        import pandas as pd
        folder = Path(base) / name
        folder.mkdir()
        (folder / 'metadata.json').write_text(_json.dumps({'generated_at_utc': generated, 'captured_at_utc': captured}))
        pd.DataFrame(rows).to_csv(folder / 'predictions.csv', index=False)

    def test_only_snapshots_generated_and_captured_before_the_clock_count(self):
        import tempfile
        import weak_links
        from performance_tracking import fixture_key
        with tempfile.TemporaryDirectory() as base:
            self.archive(base, 'a', '2026-11-24T06:00:00Z', '2026-11-24T06:05:00Z', [forecast(h2h=(1.40, 4.6, 8.0))])
            self.archive(base, 'b', '2026-11-24T09:00:00Z', '2026-11-24T13:00:00Z', [forecast(h2h=(1.30, 5.0, 10.))])
            self.archive(base, 'c', '2026-11-24T13:00:00Z', '2026-11-24T13:05:00Z', [forecast()])  # after the clock
            key = fixture_key(forecast())
            earlier = weak_links.earlier_forecasts({key}, '2026-11-24T12:00:00Z', Path(base))
            self.assertEqual(len(earlier[key]), 1)  # b was captured after the clock, c generated after it
            # The master passes its clock as a Timestamp (master_reconciliation.run_clock); a naive clock counts none.
            import pandas as pd
            from datetime import datetime, timezone
            for clock in (pd.Timestamp('2026-11-24T12:00:00Z'), datetime(2026, 11, 24, 12, tzinfo=timezone.utc)):
                self.assertEqual(len(weak_links.earlier_forecasts({key}, clock, Path(base))[key]), 1)
            self.assertEqual(weak_links.earlier_forecasts({key}, pd.Timestamp('2026-11-24T12:00:00'), Path(base)), {})
            self.assertEqual(weak_links.earlier_forecasts({key}, None, Path(base)), {})
            row = pick(_match=key, _forecast=forecast())
            rows = [row, pick(_match=key, strong_decision='NOT_SELECTED')]
            weak_links.annotate(rows, weak_rule(), E=.55, clock=pd.Timestamp('2026-11-24T12:00:00Z'),
                                snapshots=Path(base))
        self.assertEqual(rows[0]['weak_link'], 'yes')  # home fair probability fell from about 0.69 to 0.64
        self.assertTrue(rows[0]['weak_link_reasons'].startswith('(e) Pinnacle fair probability fell'))
        self.assertEqual((rows[1]['weak_link'], rows[1]['weak_link_reasons']), (None, None))


class WeakLinkLiveTest(unittest.TestCase):
    def test_flags_never_remove_or_reorder_a_pick(self):
        import warnings
        import pandas as pd
        from test_master_reconciliation import production_run
        predictions, decisions, summary = production_run()
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            v5, info = master_shortlist.strong_live(decisions, None, summary['generated_at_utc'], predictions)
            v4, old = master_shortlist.strong_live(decisions, None, summary['generated_at_utc'], predictions,
                                                   rule='master-strong-team-v4')
        self.assertEqual(info['version'], 'master-strong-team-v7-live-v17')
        self.assertEqual(list(v5.columns[-2 - len(__import__('master_inspection').COLUMNS):][:2]),
                         ['weak_link', 'weak_link_reasons'])
        self.assertNotIn('weak_link', v4.columns)
        key = ['new_master_rank', 'new_master_decision', 'market', 'home_team', 'offered_decimal_odds']
        pd.testing.assert_frame_equal(v5[key].reset_index(drop=True), v4[key].reset_index(drop=True))
        picks = v5.loc[v5.new_master_decision.eq('SHORTLISTED')]
        self.assertTrue(len(picks))
        self.assertTrue(picks.weak_link.isin(['yes', 'no']).all())
        self.assertTrue(v5.loc[~v5.new_master_decision.eq('SHORTLISTED'), 'weak_link'].isna().all())
        self.assertEqual(info['strong']['weak_links']['flagged_picks'], int(picks.weak_link.eq('yes').sum()))
        self.assertNotIn('weak_links', old['strong'])
        self.assertTrue(master_shortlist.matches_strong(v5, v5))
        self.assertTrue(master_shortlist.matches_strong(v4, v4, 'master-strong-team-v4'))

    def test_readable_lists_weak_links_first_and_the_workbook_paints_them_red(self):
        import pandas as pd
        import format_football_output as fo
        import excel_book as xb
        import predictions_workbook as pw
        picks = pd.DataFrame([{'new_master_rank': 1, 'home_team': 'H', 'away_team': 'A', 'market_to_bet': 'Home win',
                               'offered_decimal_odds': 1.5, 'weak_link': 'no', 'weak_link_reasons': ''},
                              {'new_master_rank': 7, 'home_team': 'C', 'away_team': 'D', 'market_to_bet': 'Away win',
                               'offered_decimal_odds': 1.8, 'weak_link': 'yes',
                               'weak_link_reasons': '(f) not proven: fill tier; note: no movement data'}])
        lines = fo.weak_link_lines(picks)
        self.assertTrue(lines[0].startswith('**Weak links: 1 of 2 picks**'))
        self.assertEqual(lines[2], '- Rank 7: C v D, Away win at 1.80: (f) not proven: fill tier')
        book = xb.Book()
        sheet = book.sheet('t')
        table = sheet.table(1, ['Rank', pw.WEAK_LINK], [[1, 'no'], [7, 'yes']], ['int', 'text'])
        sheet.highlight_rows(table, pw.WEAK_LINK, 'bad', 'yes')
        ref, rule = sheet.rules[-1]
        self.assertEqual(ref, 'A2:B3')
        self.assertIn('$B2=&quot;yes&quot;', rule)


class WeakLinkReviewTest(unittest.TestCase):
    def test_flagged_against_unflagged_and_per_reason(self):
        import pandas as pd
        import price_edge_tracking as pet
        rows = ([{'result_status': 'LOST', 'unit_profit': -1., 'clv': -.02, 'ranking_no_loss_probability': .8,
                  'weak_link': 'yes', 'weak_link_reasons': '(f) not proven: fill tier'}] * 50
                + [{'result_status': 'WON', 'unit_profit': .5, 'clv': .01, 'ranking_no_loss_probability': .8,
                    'weak_link': 'no', 'weak_link_reasons': 'note: no movement data'}] * 10)
        review = pet.weak_link_review(pd.DataFrame(rows), ms.load_config())
        self.assertEqual((review['status'], review['flagged_graded']), ('READY FOR REVIEW', 50))
        self.assertEqual((review['flagged']['n'], review['unflagged']['n'], review['by_reason']['f']['n'],
                          review['by_reason']['a']['n']), (50, 10, 50, 0))
        self.assertAlmostEqual(review['flagged']['no_loss']['difference_points'], -80.0)
        self.assertTrue(any('ready for review' in line for line in pet.weak_link_lines(review)))
        self.assertEqual(pet.weak_link_review(pd.DataFrame(rows[:10]), ms.load_config())['status'], 'WAITING')
        self.assertIsNone(pet.weak_link_review(pd.DataFrame(rows), ms.load_config(version='master-strong-team-v4')))


if __name__ == '__main__':
    unittest.main()
