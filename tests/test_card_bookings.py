"""Research booking totals: Pinnacle's rule from card events, collection order and study gates."""
import pandas as pd

import card_bookings as cb
from offline_test_case import OfflineQuotePolicyTestCase

HOME, AWAY = 1, 2


def card(team, player, detail, elapsed=30, extra=None):
    return {'type': 'Card', 'detail': detail, 'team': {'id': team}, 'player': {'id': player},
            'time': {'elapsed': elapsed, 'extra': extra}}


class BookingPointsTests(OfflineQuotePolicyTestCase):
    def points(self, events):
        return cb.booking_points(events, HOME, AWAY)

    def test_yellow_one_red_two_second_yellow_excluded(self):
        # Provider encoding seen live: two yellows plus a red at the second yellow.
        second_yellow = [card(AWAY, 7, 'Yellow Card', 15), card(AWAY, 7, 'Yellow Card', 19),
                         card(AWAY, 7, 'Red Card', 19), card(AWAY, 8, 'Yellow Card', 22)]
        self.assertEqual(self.points(second_yellow), {'home': 0, 'away': 4, 'dismissals': 1, 'flags': []})
        # The alternative encoding settles the same.
        alternative = [card(AWAY, 7, 'Yellow Card', 15), card(AWAY, 7, 'Second Yellow card', 19)]
        self.assertEqual(self.points(alternative)['away'], 3)
        # Yellow then straight red is also 1 + 2; a straight red alone is 2.
        self.assertEqual(self.points([card(HOME, 5, 'Yellow Card'), card(HOME, 5, 'Red Card', 60)])['home'], 3)
        self.assertEqual(self.points([card(HOME, 5, 'Red Card')])['home'], 2)
        # Five yellows plus a straight red settle at 7, where yellows plus reds counted once give 6.
        five = [card(HOME, p, 'Yellow Card') for p in range(5)] + [card(AWAY, 9, 'Red Card')]
        result = self.points(five)
        self.assertEqual(result['home'] + result['away'], 7)

    def test_stoppage_time_counts_and_uncertain_cards_are_flagged(self):
        self.assertEqual(self.points([card(HOME, 1, 'Yellow Card', 90, 5)]),
                         {'home': 1, 'away': 0, 'dismissals': 0, 'flags': []})
        cases = {'card outside regulation time or without a time': [card(HOME, 1, 'Yellow Card', 105)],
                 'card without a player identity (possibly staff)': [{**card(HOME, 1, 'Yellow Card'), 'player': {'id': None}}],
                 'card for an unknown team': [card(99, 1, 'Yellow Card')],
                 'two yellows without a dismissal': [card(HOME, 1, 'Yellow Card'), card(HOME, 1, 'Yellow Card', 80)],
                 "unknown card type 'blue card'": [card(HOME, 1, 'Blue Card')]}
        for flag, events in cases.items():
            with self.subTest(flag=flag):
                self.assertIn(flag, self.points(events)['flags'])
        self.assertEqual(self.points([{'type': 'Goal', 'team': {'id': HOME}}])['home'], 0)


def linked(rows):
    return pd.DataFrame([{'league': 'SerieA', 'date': pd.Timestamp('2023-01-01')+pd.Timedelta(days=i),
                          'Date': (pd.Timestamp('2023-01-01')+pd.Timedelta(days=i)).strftime('%d/%m/%Y'),
                          'HomeTeam': f'H{i}', 'AwayTeam': f'A{i}', 'fixture_id': 100+i, 'home_id': HOME,
                          'away_id': AWAY, **row} for i, row in enumerate(rows)])


class PlanAndTargetTests(OfflineQuotePolicyTestCase):
    def test_red_card_matches_first_then_a_deterministic_red_free_sample(self):
        frame = linked([{'HY': 1, 'AY': 1, 'HR': int(i % 4 == 0), 'AR': 0} for i in range(80)])
        plan = cb.collection_plan(frame)
        reds = list(frame.loc[frame.HR > 0].fixture_id)
        self.assertEqual(plan[:len(reds)], reds)
        self.assertEqual(len(plan), len(reds) + cb.SAMPLE_PER_LEAGUE)
        self.assertEqual(plan, cb.collection_plan(frame.sample(frac=1, random_state=3)))

    def test_targets_need_an_exact_shortcut_and_every_red_match(self):
        rows = [{'HY': 2, 'AY': 1, 'HR': 0, 'AR': 0}, {'HY': 1, 'AY': 2, 'HR': 0, 'AR': 1}]
        events = {100: [card(HOME, 1, 'Yellow Card'), card(HOME, 2, 'Yellow Card'), card(AWAY, 3, 'Yellow Card')],
                  101: [card(HOME, 1, 'Yellow Card'), card(AWAY, 3, 'Yellow Card', 15), card(AWAY, 3, 'Yellow Card', 50),
                        card(AWAY, 3, 'Red Card', 50)]}
        frame, report = cb.booking_targets(linked(rows), events.get)
        self.assertTrue(report['ready'])
        self.assertEqual(list(zip(frame.HBK, frame.ABK)), [(2, 1), (1, 3)])
        # A red-card match without events blocks the study rather than biasing it.
        frame, report = cb.booking_targets(linked(rows), {100: events[100]}.get)
        self.assertIsNone(frame)
        self.assertFalse(report['ready'])
        # One shortcut mismatch refuses football-data.co.uk yellows for red-free matches.
        wrong = {**events, 100: events[100][:2]}
        frame, report = cb.booking_targets(linked(rows), wrong.get)
        self.assertIsNone(frame)
        self.assertFalse(report['shortcut_valid'])
        self.assertEqual(report['shortcut']['mismatches'][0]['events'], [2, 0])
        # Flagged red-card events are excluded and reported, so the study is not ready.
        flagged = {**events, 101: events[101] + [card(AWAY, 4, 'Yellow Card', 110)]}
        frame, report = cb.booking_targets(linked(rows), flagged.get)
        self.assertIsNone(frame)
        self.assertEqual(report['excluded_red_matches'][0]['fixture_id'], 101)

    def test_research_module_never_enters_production(self):
        import count_markets
        self.assertEqual(count_markets.LEAGUES['cards'], ())
        self.assertIn('Research only', cb.__doc__)
