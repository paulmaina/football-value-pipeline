"""BBS match observations: the store-on-change rule and the one-off compaction that applies it."""
import sys
import tempfile
import unittest
from pathlib import Path

from bbs_data import Store, match_observation_needed, match_state

sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'scripts'))
from compact_bbs_match_observations import main, plan  # noqa: E402


def payload(minute, **change):
    row = {'id': 'm1', 'sport': 'football', 'league': 'EPL', 'status': 'scheduled', 'score': None,
           'kickoff_utc': '2026-11-22T15:00:00+00:00', 'round': 'Regular Season - 12', 'requested_season': 2026,
           'regulation_score_verified': False, 'linescore': None, 'source_updated_at': None,
           'home': {'id': 'h', 'name': 'Arsenal', 'logo_url': f'https://x/{minute}'},
           'away': {'id': 'a', 'name': 'Chelsea', 'logo_url': 'https://x/a'},
           'observed_at_utc': f'2026-11-20T10:{minute:02d}:00+00:00', 'has_odds': minute % 2 == 0,
           'broadcast': f'TV{minute}', 'source_meta': {'request_id': str(minute)}}
    row.update(change)
    return row


def obs(minute, kind='match', **change):
    return {'kind': kind, 'league': 'EPL', 'entity': 'm1', 'observed': f'2026-11-20T10:{minute:02d}:00+00:00',
            'payload': payload(minute, **change) if kind == 'match' else {'reason': 'bad row'}, 'query': ''}


FINISHED = dict(status='finished', score={'home': 2, 'away': 1}, regulation_score_verified=True)


class MatchStateTests(unittest.TestCase):
    def test_volatile_fields_do_not_change_the_state(self):
        self.assertEqual(match_state(payload(1)), match_state(payload(2)))
        for change in (FINISHED, {'kickoff_utc': '2026-11-22T17:30:00+00:00'}, {'round': 'Regular Season - 13'},
                       {'linescore': {'home': [1, 1], 'away': [0, 1]}}, {'requested_season': 2025},
                       {'home': {'id': 'h2', 'name': 'Arsenal'}}, {'away': {'id': 'a', 'name': 'Chelsea FC'}}):
            self.assertNotEqual(match_state(payload(1)), match_state(payload(1, **change)), change)

    def test_needed_on_first_sight_on_change_and_after_a_quarantine(self):
        first = obs(1)
        self.assertTrue(match_observation_needed(None, payload(1)))
        self.assertFalse(match_observation_needed(first, payload(2)))
        self.assertTrue(match_observation_needed(first, payload(2, **FINISHED)))
        self.assertTrue(match_observation_needed(first, payload(3), '2026-11-20T10:02:00+00:00'))
        self.assertFalse(match_observation_needed(first, payload(3), '2026-11-20T09:00:00+00:00'))


class CompactionPlanTests(unittest.TestCase):
    def keep(self, matches, quarantines=()):
        return sorted(plan([(o['observed'], o) for o in matches], [(o['observed'], o) for o in quarantines]))

    def test_keeps_the_first_of_each_consecutive_state_including_a_reverted_one(self):
        matches = [obs(1), obs(2), obs(3, **FINISHED), obs(4, **FINISHED), obs(5), obs(6)]
        self.assertEqual(self.keep(matches), [m['observed'] for m in (matches[0], matches[2], matches[4])])

    def test_the_listing_after_a_quarantine_is_kept_so_the_hold_still_lifts(self):
        matches = [obs(1), obs(3), obs(4)]
        self.assertEqual(self.keep(matches, [obs(2, kind='quarantine')]), [matches[0]['observed'], matches[1]['observed']])

    def test_latest_state_and_hold_are_unchanged_at_every_cutoff(self):
        matches = [obs(1), obs(2), obs(4), obs(5, **FINISHED), obs(6, **FINISHED), obs(8, **FINISHED)]
        quarantines = [obs(3, kind='quarantine'), obs(7, kind='quarantine')]
        kept = set(self.keep(matches, quarantines))
        compact = [m for m in matches if m['observed'] in kept]
        for minute in range(1, 10):
            cutoff = f'2026-11-20T10:{minute:02d}:00+00:00'
            full_last = [m for m in matches if m['observed'] <= cutoff][-1]
            compact_last = [m for m in compact if m['observed'] <= cutoff][-1]
            self.assertEqual(match_state(full_last['payload']), match_state(compact_last['payload']), cutoff)
            held = [q['observed'] for q in quarantines if q['observed'] <= cutoff]
            if held:
                self.assertEqual(max(held) >= full_last['observed'], max(held) >= compact_last['observed'], cutoff)

    def test_script_reports_then_deletes_only_repeats(self):
        with tempfile.TemporaryDirectory() as tmp:
            store = Store(Path(tmp))
            for o in (obs(1), obs(2), obs(3, **FINISHED), obs(4, **FINISHED)):
                store.put('match', 'EPL', 'm1', o['observed'], o['payload'])
            folder = Path(tmp)/'observations/match'
            self.assertEqual(main(['--store', tmp]), 0)
            self.assertEqual(len(list(folder.glob('*.json'))), 4)
            self.assertEqual(main(['--store', tmp, '--apply']), 0)
            left = sorted(Store(Path(tmp)).observations, key=lambda r: r['observed'])
            self.assertEqual([r['observed'] for r in left],
                             ['2026-11-20T10:01:00+00:00', '2026-11-20T10:03:00+00:00'])


if __name__ == '__main__':
    unittest.main()
