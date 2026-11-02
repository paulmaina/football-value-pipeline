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


if __name__ == '__main__':
    unittest.main()
