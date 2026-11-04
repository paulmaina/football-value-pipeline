"""v27 forward tracking: CLV vs Pinnacle close, tagged-candidate record and STOP REVIEW."""

from offline_test_case import OfflineQuotePolicyTestCase
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import pandas as pd

import price_edge_tracking as tracking
from price_edge_shortlist import POLICY

KICK = pd.Timestamp('2026-11-07T15:00:00Z')
CAPTURED = (KICK - pd.Timedelta(hours=20)).isoformat()
CLOCK = KICK + pd.Timedelta(hours=5)


def meta(sha='a' * 40, files=()):
    return {'git_commit_sha': sha, 'captured_at_utc': CAPTURED, 'generated_at_utc': CAPTURED,
            'selection_policy_version': POLICY, 'sha256': {name: '0' * 64 for name in files}}


def pick(home='Home FC', market='Asian Handicap Home +1.00', price=1.90, **extra):
    return {'league': 'Premier League', 'home_team': home, 'away_team': 'Away FC', 'kickoff_utc': KICK.isoformat(),
            'market': market, 'decision': 'SHORTLISTED', 'bookmaker': '1xBet', 'offered_decimal_odds': price,
            'fair_odds': 1.85, 'reference_type': 'a', 'side_role': 'underdog', 'balanced': True,
            'low_total': False, 'high_draw': True, **extra}


def observation(home='Home FC', quotes=None):
    quotes = quotes if quotes is not None else [
        {'bookmaker': 'pinnacle', 'selection': 'Asian Handicap Home +1.00', 'decimal_odds': 1.80},
        {'bookmaker': 'pinnacle', 'selection': 'Asian Handicap Away -1.00', 'decimal_odds': 2.10}]
    return {'observed_at_utc': (KICK - pd.Timedelta(minutes=3)).isoformat(),
            'fixture': {'league': 'Premier League', 'home_team': home, 'away_team': 'Away FC',
                        'kickoff_utc': KICK.isoformat()}, 'quotes': quotes}


class SidecarTests(OfflineQuotePolicyTestCase):
    def test_write_list_keeps_tagged_rows_bound_to_generation(self):
        decisions = pd.DataFrame([{**pick(), 'any_tag': True, 'handicap_side': 'home', 'handicap_line': 1.0},
                                  {**pick(home='Plain'), 'any_tag': False}])
        with tempfile.TemporaryDirectory() as tmp:
            rows = tracking.write_list(decisions, Path(tmp), CAPTURED)
            self.assertEqual([r['home_team'] for r in rows], ['Home FC'])
            self.assertEqual(tracking.capture_file(Path(tmp), CAPTURED), Path(tmp) / tracking.FILE)
            self.assertIsNone(tracking.capture_file(Path(tmp), KICK.isoformat()))
            self.assertEqual(tracking.write_list(pd.DataFrame(), Path(tmp), CAPTURED), [])
            self.assertEqual(tracking.capture_file(Path(tmp), CAPTURED), Path(tmp) / tracking.FILE)
        with tempfile.TemporaryDirectory() as tmp:
            self.assertIsNone(tracking.capture_file(Path(tmp), CAPTURED))

    def test_frozen_candidates_keep_latest_pre_kickoff_entry(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            archive = []
            for sha, price, captured in (('a' * 40, 1.80, CAPTURED), ('b' * 40, 1.95, (KICK - pd.Timedelta(hours=2)).isoformat()),
                                         ('c' * 40, 2.50, (KICK - pd.Timedelta(minutes=5)).isoformat())):
                directory = root / 'performance' / 'snapshots' / sha[:16]
                directory.mkdir(parents=True)
                tracking.write_list(pd.DataFrame([{**pick(price=price), 'any_tag': True, 'handicap_side': 'home',
                                                   'handicap_line': 1.0}]), directory, captured)
                archive.append(({**meta(sha, [tracking.FILE]), 'captured_at_utc': captured, 'generated_at_utc': captured}, [], []))
            archive.append((meta('d' * 40), [], []))  # no sidecar captured
            rows = tracking.frozen_candidates(root, archive)
        self.assertEqual([float(r['offered_decimal_odds']) for r in rows], [1.95])


class ClvTests(OfflineQuotePolicyTestCase):
    def test_close_win_share_from_same_line_pair_and_from_1x2(self):
        pair = observation()['quotes']
        self.assertAlmostEqual(tracking.close_win_share(pair, 'home', 1.0), (1 / 1.8) / (1 / 1.8 + 1 / 2.1))
        hda = [{'bookmaker': 'pinnacle', 'selection': k, 'decimal_odds': v}
               for k, v in (('home', 2.0), ('draw', 3.5), ('away', 4.0))]
        total = 1 / 2 + 1 / 3.5 + 1 / 4
        self.assertAlmostEqual(tracking.close_win_share(hda, 'home', -0.5), 0.5 / total)
        self.assertAlmostEqual(tracking.close_win_share(hda, 'away', 0.5), 1 - 0.5 / total)
        self.assertIsNone(tracking.close_win_share(hda, 'home', 1.0))
        self.assertIsNone(tracking.close_win_share([{**pair[0], 'bookmaker': '1xbet'}, pair[1]], 'home', 1.0))

    def test_equivalent_markets_map_to_their_ah_line(self):
        self.assertEqual(tracking.ah_line('Double Chance X2'), ('away', 0.5))
        self.assertEqual(tracking.ah_line('Asian Handicap Away -0.25'), ('away', -0.25))
        self.assertEqual(tracking.ah_line('Probe', 'home', '1.5'), ('home', 1.5))
        self.assertIsNone(tracking.ah_line('Over 1.5'))

    def test_grade_clv_result_and_splits(self):
        rows = [{**pick(), 'snapshot_captured_utc': CAPTURED}]
        final = {'home_goals': 1, 'away_goals': 2}
        with patch('performance_tracking.fixture_match', return_value=(final, 'VERIFIED_FINISHED')):
            graded = tracking.grade(rows, [observation()], [], CLOCK)
        item = graded.iloc[0]
        q = (1 / 1.8) / (1 / 1.8 + 1 / 2.1)
        self.assertAlmostEqual(item.clv, 1.90 * q - 1)
        self.assertEqual(item.result_status, 'REFUNDED')
        self.assertEqual(item.unit_profit, 0.0)
        self.assertEqual((item.odds_band, item.tagged, item.balanced, item.low_total), ('1.90-2.10', 'any tag', 'yes', 'no'))
        before = tracking.grade(rows, [observation()], [], KICK)
        self.assertIsNone(before.iloc[0].result_status)

    def test_observation_before_capture_is_ignored(self):
        early = {**observation(), 'observed_at_utc': (KICK - pd.Timedelta(hours=22)).isoformat()}
        graded = tracking.grade([{**pick(), 'snapshot_captured_utc': CAPTURED}], [early], [], KICK)
        self.assertTrue(pd.isna(graded.iloc[0].clv))


class ReviewTests(OfflineQuotePolicyTestCase):
    def run_review(self, picks, observations):
        archive = [(meta(), [], picks)]
        with tempfile.TemporaryDirectory() as tmp, \
                patch('closing_odds.load_observations', return_value=(observations, [])), \
                patch('performance_tracking.fixture_match', return_value=(None, 'NOT_FINISHED')):
            summary = tracking.review(Path(tmp), archive, [], CLOCK)
            report = (Path(tmp) / tracking.OUTPUT_DIR / 'report.md').read_text(encoding='utf-8')
            graded = pd.read_csv(Path(tmp) / tracking.OUTPUT_DIR / 'picks.csv')
        return summary, report, graded

    def test_stop_review_needs_100_graded_picks_with_negative_mean(self):
        losing = [pick(home=f'T{i}', price=1.70) for i in range(100)]
        closes = [observation(home=f'T{i}') for i in range(100)]
        summary, report, graded = self.run_review(losing, closes)
        self.assertTrue(summary['stop_review'])
        self.assertIn('STOP REVIEW', report)
        self.assertEqual(len(graded), 100)
        summary, report, _ = self.run_review(losing[:99], closes[:99])
        self.assertFalse(summary['stop_review'])
        self.assertNotIn('> **STOP REVIEW**', report)

    def test_only_v27_picks_are_graded_and_splits_are_reported(self):
        archive_pick = pick(home='Winner', price=2.00)
        summary, report, _ = self.run_review([archive_pick], [observation(home='Winner')])
        self.assertEqual(summary['frozen_picks'], 1)
        self.assertGreater(summary['clv']['mean'], 0)
        self.assertEqual(set(summary['clv_by']), set(tracking.SPLITS))
        self.assertEqual(set(summary['clv_by']['reference_type']), {'a'})
        self.assertIn('## CLV by bookmaker', report)
        self.assertIn('Tagged candidates', report)
        other = {**meta('e' * 40), 'selection_policy_version': 'v26'}
        with tempfile.TemporaryDirectory() as tmp, patch('closing_odds.load_observations', return_value=([], [])):
            summary = tracking.review(Path(tmp), [(other, [], [archive_pick])], [], CLOCK)
        self.assertEqual(summary['frozen_picks'], 0)
        self.assertEqual(summary['clv']['n'], 0)


class CageyTrackingTests(OfflineQuotePolicyTestCase):
    def tier_pick(self, home='Cagey FC', **extra):
        return {**pick(home=home, market='Asian Handicap Away +2.00', price=1.30), 'selection_policy_version': tracking.CAGEY_POLICY,
                'evaluated_at_utc': CAPTURED, 'corrected_cagey_score': 0.25, 'cagey_tier_decision': 'SHORTLISTED',
                'reference_type': 'c-cagey', 'even_odds': False, **extra}

    def test_tier_sidecar_binds_to_its_v28_generation(self):
        with tempfile.TemporaryDirectory() as tmp:
            raw = Path(tmp)
            self.assertIsNone(tracking.capture_tier_file(raw, CAPTURED))
            pd.DataFrame([self.tier_pick()]).to_csv(raw / tracking.TIER_FILE, index=False)
            self.assertEqual(tracking.capture_tier_file(raw, CAPTURED), raw / tracking.TIER_FILE)
            self.assertIsNone(tracking.capture_tier_file(raw, KICK.isoformat()))
            pd.DataFrame([self.tier_pick(selection_policy_version=POLICY)]).to_csv(raw / tracking.TIER_FILE, index=False)
            self.assertIsNone(tracking.capture_tier_file(raw, CAPTURED))
            pd.DataFrame(columns=['selection_policy_version', 'evaluated_at_utc']).to_csv(raw / tracking.TIER_FILE, index=False)
            self.assertEqual(tracking.capture_tier_file(raw, CAPTURED), raw / tracking.TIER_FILE)

    def test_frozen_tier_picks_keep_latest_pre_kickoff_entry_per_fixture(self):
        with tempfile.TemporaryDirectory() as tmp:
            root, archive = Path(tmp), []
            for sha, price, captured in (('a' * 40, 1.25, CAPTURED), ('b' * 40, 1.31, (KICK - pd.Timedelta(hours=3)).isoformat()),
                                         ('c' * 40, 1.50, (KICK - pd.Timedelta(minutes=5)).isoformat())):
                directory = root / 'performance' / 'snapshots' / sha[:16]
                directory.mkdir(parents=True)
                pd.DataFrame([self.tier_pick(offered_decimal_odds=price)]).to_csv(directory / tracking.TIER_FILE, index=False)
                archive.append(({**meta(sha, [tracking.TIER_FILE]), 'captured_at_utc': captured, 'generated_at_utc': captured}, [], []))
            rows = tracking.frozen_tier_picks(root, archive)
        self.assertEqual([float(r['offered_decimal_odds']) for r in rows], [1.31])

    def frame(self, value_rows=(), tier_rows=()):
        return tracking.tier_frame(pd.DataFrame(list(value_rows)), pd.DataFrame(list(tier_rows)))

    def test_cagey_review_needs_50_correction_only_picks_with_negative_clv(self):
        only = [{'clv': -0.01, 'unit_profit': 0.0, 'qualified_only_by_correction': True,
                 'selection_policy_version': tracking.CAGEY_POLICY, 'corrected_cagey_score': 0.3 + i / 1000} for i in range(50)]
        flags = tracking.cagey_flags(self.frame(only))
        self.assertTrue(flags['cagey_review'])
        self.assertIn('cagey_correction_enabled = false', flags['cagey_review_rule'])
        self.assertFalse(tracking.cagey_flags(self.frame(only[:49]))['cagey_review'])
        plain = [{**r, 'qualified_only_by_correction': False} for r in only]
        self.assertFalse(tracking.cagey_flags(self.frame(plain))['cagey_review'])

    def test_cagey_tier_review_needs_an_roi_interval_below_zero(self):
        losing = [{'clv': 0.0, 'unit_profit': -1.0 if i % 4 else 0.25, 'corrected_cagey_score': 0.25} for i in range(50)]
        self.assertTrue(tracking.cagey_flags(self.frame(tier_rows=losing))['cagey_tier_review'])
        self.assertFalse(tracking.cagey_flags(self.frame(tier_rows=losing[:49]))['cagey_tier_review'])
        mixed = [{'clv': 0.0, 'unit_profit': 1.0 if i % 2 else -1.0, 'corrected_cagey_score': 0.25} for i in range(60)]
        self.assertFalse(tracking.cagey_flags(self.frame(tier_rows=mixed))['cagey_tier_review'])
        self.assertFalse(tracking.cagey_flags(self.frame())['cagey_tier_review'])

    def test_below_fair_tier_picks_never_trigger_the_tier_review_and_are_split_out(self):
        losing = [{'clv': 0.0, 'unit_profit': -1.0 if i % 4 else 0.25, 'corrected_cagey_score': 0.25} for i in range(50)]
        below = [{**r, 'price_flag': tracking.PRICE_BELOW_FAIR} for r in losing]
        frame = self.frame(tier_rows=below)
        self.assertFalse(tracking.cagey_flags(frame)['cagey_tier_review'])
        self.assertEqual(tracking.cagey_flags(frame)['cagey_tier_roi']['n'], 0)
        # Value-flagged v2 picks count, as do v1 picks (no flag: all passed expected profit >= 0).
        value = [{**r, 'price_flag': tracking.PRICE_VALUE} for r in losing]
        self.assertTrue(tracking.cagey_flags(self.frame(tier_rows=value))['cagey_tier_review'])
        mixed = self.frame(tier_rows=[*losing[:10], *below[:20], *value[:5]])
        self.assertEqual(tracking.cagey_flags(mixed)['cagey_tier_roi']['n'], 15)
        rules = tracking.split_table(mixed, 'unit_profit', ('cagey_tier_rule', 'price_flag'))
        self.assertEqual({k: v['n'] for k, v in rules['cagey_tier_rule'].items()},
                         {tracking.TIER_RULE_VALUE: 10, tracking.TIER_RULE_NARROW: 25})
        self.assertEqual({k: v['n'] for k, v in rules['price_flag'].items()},
                         {tracking.PRICE_VALUE: 15, tracking.PRICE_BELOW_FAIR: 20})

    def test_splits_cover_tier_policy_reference_quintile_tags_and_correction(self):
        value = [{'clv': 0.02, 'unit_profit': 0.9, 'reference_type': 'c-cagey', 'qualified_only_by_correction': 'True',
                  'selection_policy_version': tracking.CAGEY_POLICY, 'bookmaker': '1xBet', 'even_odds': 'yes',
                  'corrected_cagey_score': s} for s in (0.2, 0.3, 0.4, 0.5, 0.6)]
        tier = [{'clv': 0.01, 'unit_profit': 0.2, 'reference_type': 'c-cagey', 'bookmaker': 'Pinnacle',
                 'selection_policy_version': tracking.CAGEY_POLICY, 'corrected_cagey_score': 0.21}]
        frame = self.frame(value, tier)
        table = tracking.split_table(frame, 'clv', tracking.TIER_SPLITS)
        self.assertEqual(set(table), set(tracking.TIER_SPLITS))
        self.assertEqual(set(table['tier']), {'value', 'cagey'})
        self.assertEqual(set(table['policy']), {'v28'})
        self.assertEqual(table['qualified_only_by_correction']['yes']['n'], 5)
        self.assertIn('Q1 cagiest', table['corrected_cagey_quintile'])

    def test_review_grades_both_tiers_and_reports_flags(self):
        value = [pick(home=f'V{i}', price=1.70, selection_policy_version=tracking.CAGEY_POLICY,
                      qualified_only_by_correction=True, corrected_cagey_score=0.3) for i in range(50)]
        archive = [(meta(files=[tracking.TIER_FILE]), [], value)]
        with tempfile.TemporaryDirectory() as tmp:
            directory = Path(tmp) / 'performance' / 'snapshots' / ('a' * 16)
            directory.mkdir(parents=True)
            pd.DataFrame([self.tier_pick()]).to_csv(directory / tracking.TIER_FILE, index=False)
            closes = [observation(home=f'V{i}') for i in range(50)] + [observation(home='Cagey FC', quotes=[
                {'bookmaker': 'pinnacle', 'selection': 'Asian Handicap Away +2.00', 'decimal_odds': 1.22},
                {'bookmaker': 'pinnacle', 'selection': 'Asian Handicap Home -2.00', 'decimal_odds': 4.60}])]
            with patch('closing_odds.load_observations', return_value=(closes, [])), \
                    patch('performance_tracking.fixture_match', return_value=({'home_goals': 1, 'away_goals': 1}, 'VERIFIED_FINISHED')):
                summary = tracking.review(Path(tmp), archive, [], CLOCK)
            report = (Path(tmp) / tracking.OUTPUT_DIR / 'report.md').read_text(encoding='utf-8')
            tier_csv = pd.read_csv(Path(tmp) / tracking.OUTPUT_DIR / 'cagey_tier_picks.csv')
        self.assertEqual(summary['cagey_tier_picks'], 1)
        self.assertEqual(len(tier_csv), 1)
        self.assertGreater(summary['cagey_tier']['clv']['mean'], 0)
        self.assertAlmostEqual(summary['cagey_tier']['profit']['mean'], 0.30)
        self.assertTrue(summary['cagey_review'])  # 50 correction-only picks at 1.70 vs a 1.80 close
        self.assertIn('CAGEY REVIEW', report)
        self.assertIn('### By tier', report)


if __name__ == '__main__':
    unittest.main()
