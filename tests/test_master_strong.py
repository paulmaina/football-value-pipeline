"""The strong-team master in shadow (master_strong.py, rule master-strong-team-v1): caps (6 per market group, 15
matches, one pick per match), the order (proven, league trust, research confirms, chance of profit), the not-proven
fill under the same caps, research roles that failed their pass rule staying labels, R3 on UCL/UEL only, thresholds
refused while unset, and the shadow never touching the live files."""
from __future__ import annotations

import copy
import json
import tempfile
import unittest
from pathlib import Path
from unittest import mock

import master_strong as ms

RUN = {'E': .60, 'G': .50, 'R1': True, 'R2': True, 'R3': True, 'R4': True}


def config():
    cfg = ms.load_config()
    cfg = copy.deepcopy(cfg)
    cfg['checks']['strong_team']['E'] = RUN['E']
    roles = cfg['research_roles']
    roles['R1_research_strength'].update(G=RUN['G'], active=True)
    roles['R2_agreement_boost']['active'] = True
    roles['R4_fill_tie_breaker']['active'] = True
    return cfg


def evidence(team='H', wins=8, elo=.70, margin=1.0, side='home'):
    rows = [{'home': team, 'away': f'X{i}', 'home_goals': 2 if i < wins else 0, 'away_goals': 0 if i < wins else 1}
            for i in range(10)]
    return {'elo_home_expectancy': elo if side == 'home' else 1 - elo, 'history': {side: rows}, 'teams': {side: team},
            'h2h': [], 'research_margin': margin if side == 'home' else -margin}


def offer(match, market='Home win', no_loss=.80, profit=.80, odds=1.30, research=.80, gap=0., league='Premier League',
          trust='trusted', european=False, ev=None, **extra):
    row = {'_match': match, 'market': market, 'handicap_side': None, 'handicap_line': None, 'league': league,
           'home_team': 'H', 'away_team': 'A', 'kickoff_utc': f'2026-11-2{match[-1]}T15:00:00Z',
           'offered_decimal_odds': odds, 'ranking_no_loss_probability': no_loss,
           'ranking_profit_probability': profit, 'research_no_loss_probability': research, 'gap_points': gap,
           'research_profit_probability': extra.pop('research_profit', research), 'new_master_executable': True}
    row.update(extra)
    side = 'away' if market in ('Away win', 'Double Chance X2') or market.startswith('Asian Handicap Away') else 'home'
    return ms.annotate(row, ev or evidence(side=side), config=config(), trust=trust, european=european,
                       E=RUN['E'], G=RUN['G'])


class SettingsTest(unittest.TestCase):
    def test_unset_thresholds_are_refused(self):
        cfg = copy.deepcopy(ms.load_config())
        cfg['checks']['strong_team']['E'] = None
        with self.assertRaisesRegex(ValueError, 'thresholds not set'):
            ms.settings(cfg)
        self.assertEqual(ms.settings(config())['E'], .60)


class ChecksTest(unittest.TestCase):
    def test_proven_needs_every_check(self):
        self.assertTrue(ms.proven(offer('m1'), RUN))
        self.assertIn('safe', ms.failed_checks(offer('m1', no_loss=.70), RUN)[0])
        weak = offer('m1', ev=evidence(elo=.55))
        self.assertIn('strong team', ms.failed_checks(weak, RUN)[0])
        record = offer('m1', ev=evidence(wins=6))
        self.assertIn('record', ms.failed_checks(record, RUN)[0])
        research = offer('m1', ev=evidence(margin=.2))  # -0.5 line: 0.2 - 0.5 < 0.5
        self.assertIn('research strength', ms.failed_checks(research, RUN)[0])
        self.assertEqual(ms.failed_checks(research, {**RUN, 'R1': False}), [])

    def test_away_side_and_handicap_line(self):
        row = offer('m1', market='Asian Handicap Away +0.50', ev=evidence(side='away', wins=8))
        self.assertEqual((row['strong_backed_side'], row['strong_line'], row['strong_market_group']),
                         ('away', .5, 'asian_handicap'))
        self.assertAlmostEqual(row['strong_elo_expectancy'], .70)
        self.assertAlmostEqual(row['strong_research_margin'], 1.5)
        self.assertEqual(row['strong_bet_kind'], 'no loss')

    def test_r3_only_on_european_offers(self):
        domestic = offer('m1', research=.60)
        self.assertIsNone(domestic['strong_r3_check'])
        self.assertTrue(ms.proven(domestic, RUN))
        european = offer('m2', research=.60, european=True, trust='unvalidated')
        self.assertFalse(european['strong_r3_check'])
        self.assertFalse(ms.proven(european, RUN))
        self.assertTrue(ms.proven(european, {**RUN, 'R3': False}))


class SelectTest(unittest.TestCase):
    def test_caps_one_per_match_and_target(self):
        rows = [offer(f'm{i:02d}', market='Home win', profit=.9 - i / 100) for i in range(10)]
        rows += [offer(f'n{i:02d}', market='Asian Handicap Home -0.50', profit=.8 - i / 100) for i in range(12)]
        rows += [offer('m00', market='Asian Handicap Home -0.50', profit=.5)]
        ms.select(rows, config(), RUN)
        picks = [r for r in rows if r['strong_decision'] == 'SHORTLISTED']
        self.assertEqual(len(picks), 12)  # 6 match result + 6 Asian handicap; double chance has no offers
        groups = [r['strong_market_group'] for r in picks]
        self.assertEqual(groups.count('match_result'), 6)
        self.assertEqual(groups.count('asian_handicap'), 6)
        self.assertEqual(len({r['_match'] for r in picks}), len(picks))
        full = [r for r in rows if r['strong_reason'].startswith('market group full')]
        self.assertTrue(full)

    def test_total_never_above_fifteen(self):
        rows = [offer(f'a{i:02d}', market=m, profit=.9 - i / 100)
                for i, m in enumerate(['Home win', 'Double Chance 1X', 'Asian Handicap Home -0.50'] * 7)]
        ms.select(rows, config(), RUN)
        picks = [r for r in rows if r['strong_decision'] == 'SHORTLISTED']
        self.assertEqual(len(picks), 15)
        self.assertEqual(sorted(r['strong_rank'] for r in picks), list(range(1, 16)))

    def test_order_proven_then_trust_then_confirms_then_profit(self):
        rows = [offer('m1', profit=.95, trust='not trusted'), offer('m2', profit=.80),
                offer('m3', profit=.90, research=.70), offer('m4', profit=.99, no_loss=.70)]
        ms.select(rows, config(), RUN)
        order = sorted((r for r in rows if r['strong_rank']), key=lambda r: r['strong_rank'])
        self.assertEqual([r['_match'] for r in order], ['m2', 'm3', 'm1', 'm4'])
        self.assertEqual([r['strong_tier'] for r in order], ['proven'] * 3 + ['not proven: fill'])
        # R2 failed its pass rule: confirmation is a label only and the order is by chance of profit
        rows = [offer('m2', profit=.80), offer('m3', profit=.90, research=.70)]
        ms.select(rows, config(), {**RUN, 'R2': False})
        self.assertEqual(min(rows, key=lambda r: r['strong_rank'])['_match'], 'm3')
        self.assertIn('research confirms (label only)', rows[0]['strong_labels'])

    def test_fill_is_labelled_and_capped(self):
        rows = [offer(f'm{i}', market='Home win', no_loss=.6, profit=.6 - i / 100) for i in range(9)]
        ms.select(rows, config(), RUN)
        picks = [r for r in rows if r['strong_decision'] == 'SHORTLISTED']
        self.assertEqual(len(picks), 6)
        self.assertTrue(all(r['strong_tier'] == 'not proven: fill' for r in picks))
        self.assertTrue(all('not proven' in r['strong_labels'] for r in picks))

    def test_r4_breaks_near_ties_by_research_only_when_active(self):
        rows = [offer('m1', no_loss=.6, profit=.611, research_profit=.50),
                offer('m2', no_loss=.6, profit=.605, research_profit=.70)]
        ms.select(rows, config(), RUN)
        self.assertEqual(min(rows, key=lambda r: r['strong_rank'])['_match'], 'm2')
        rows = [offer('m1', no_loss=.6, profit=.611, research_profit=.50),
                offer('m2', no_loss=.6, profit=.605, research_profit=.70)]
        ms.select(rows, config(), {**RUN, 'R4': False})
        self.assertEqual(min(rows, key=lambda r: r['strong_rank'])['_match'], 'm1')

    def test_not_executable_never_picked(self):
        rows = [offer('m1', new_master_executable=False, new_master_reason='timing: stale')]
        ms.select(rows, config(), RUN)
        self.assertEqual((rows[0]['strong_decision'], rows[0]['strong_reason']), ('NOT_EXECUTABLE', 'timing: stale'))


class ShadowTest(unittest.TestCase):
    def test_shadow_failure_leaves_live_files(self):
        import master_shortlist
        with tempfile.TemporaryDirectory() as tmp:
            live = Path(tmp) / master_shortlist.FILE
            live.write_text('live\n', encoding='utf-8')
            with mock.patch.object(ms, 'reconcile', side_effect=RuntimeError('boom')):
                master_shortlist.strong_shadow(object(), tmp, {}, None, None)
            self.assertEqual(live.read_text(encoding='utf-8'), 'live\n')
            self.assertFalse((Path(tmp) / ms.load_config()['file']).exists())


class GradingTest(unittest.TestCase):
    def test_capture_only_this_generation_and_rule(self):
        import pandas as pd
        import price_edge_tracking as tracking
        generated = '2026-11-23T10:00:00+00:00'
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / ms.load_config()['file']
            row = {'selection_policy_version': tracking.CAGEY_POLICY, 'evaluated_at_utc': generated,
                   'strong_master_version': ms.VERSION, 'strong_decision': 'SHORTLISTED'}
            pd.DataFrame([row]).to_csv(path, index=False)
            self.assertEqual(tracking.capture_strong_master_file(Path(tmp), generated), path)
            self.assertIsNone(tracking.capture_strong_master_file(Path(tmp), '2026-11-23T11:00:00+00:00'))
            pd.DataFrame([{**row, 'strong_master_version': 'other'}]).to_csv(path, index=False)
            self.assertIsNone(tracking.capture_strong_master_file(Path(tmp), generated))

    def test_comparison_waits_for_enough_graded_matches(self):
        import pandas as pd
        import price_edge_tracking as tracking
        empty = pd.DataFrame(columns=['kickoff_utc', 'unit_profit', 'offered_decimal_odds', 'clv'])
        out = tracking.strong_master_summary(empty, empty)
        self.assertEqual(out['comparison']['status'], 'WAITING')
        self.assertIn('strong_master', out['comparison'])
        text = '\n'.join(tracking.strong_master_report({'strong_master': out}))
        self.assertIn('Strong-team master', text)


if __name__ == '__main__':
    unittest.main()
