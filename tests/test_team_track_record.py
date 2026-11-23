"""Pre-kickoff strength evidence for the strong-team master (team_track_record.py): backed side and line per market,
the record on the exact bet (halves and pushes), the research margin and the Elo expectancy, and that nothing on or
after kickoff day enters a record (team_research.form_history's cutoff)."""
from __future__ import annotations

import json
import unittest

import pandas as pd

import team_track_record as tr
from team_research import form_history


def row(date, home, away, hg, ag):
    return {'date': date, 'home': home, 'away': away, 'home_goals': hg, 'away_goals': ag}


class BackedSideTest(unittest.TestCase):
    def test_markets(self):
        self.assertEqual(tr.backed_side('Home win'), ('home', -.5, 'match_result'))
        self.assertEqual(tr.backed_side('Away win'), ('away', -.5, 'match_result'))
        self.assertEqual(tr.backed_side('Double Chance 1X'), ('home', .5, 'double_chance'))
        self.assertEqual(tr.backed_side('Double Chance X2'), ('away', .5, 'double_chance'))
        self.assertEqual(tr.backed_side('Asian Handicap Away +1.25'), ('away', 1.25, 'asian_handicap'))
        self.assertEqual(tr.backed_side('Asian Handicap Home -0.75'), ('home', -.75, 'asian_handicap'))
        self.assertIsNone(tr.backed_side('Over 1.5'))
        self.assertIsNone(tr.backed_side('Double Chance 12'))

    def test_win_or_no_loss_bet(self):
        self.assertTrue(tr.is_win_bet(-.5))
        self.assertTrue(tr.is_win_bet(-.25))
        self.assertFalse(tr.is_win_bet(0.))
        self.assertFalse(tr.is_win_bet(.5))


class RecordTest(unittest.TestCase):
    rule = {'min_matches': 6, 'win_bets_min_won_share': .7, 'no_loss_bets_min_not_lost_share': .8}

    def test_margins_from_the_team_side(self):
        rows = [row('d3', 'A', 'B', 2, 0), row('d2', 'C', 'A', 1, 1), row('d1', 'D', 'A', 3, 1), row('d0', 'X', 'Y', 9, 0)]
        self.assertEqual(tr.team_margins(rows, 'A'), [2., 0., -2.])
        self.assertEqual(tr.team_margins(rows, 'A', limit=2), [2., 0.])

    def test_quarter_and_whole_lines(self):
        # margins +1, 0, -1 on line +0.25: won 1 + 1/2 + 0, lost 0 + 0 + 1
        out = tr.settle_margins([1, 0, -1], .25)
        self.assertEqual((out['won'], out['not_lost']), (1.5, 2.))
        # line 0: a draw is a push (not lost, not won)
        out = tr.settle_margins([1, 0, -1], 0.)
        self.assertEqual((out['won'], out['not_lost']), (1., 2.))
        # line -0.75 on a one-goal win: half won, half pushed
        out = tr.settle_margins([1], -.75)
        self.assertEqual((out['won'], out['not_lost']), (.5, 1.))

    def test_check(self):
        wins = tr.settle_margins([1, 1, 1, 1, 1, 1, 1, 0, 0, -1], -.5)  # 7 of 10 won
        self.assertTrue(tr.record_check(wins, -.5, self.rule)[0])
        six = tr.settle_margins([1, 1, 1, 1, 1, 1, 0, 0, 0, -1], -.5)
        self.assertFalse(tr.record_check(six, -.5, self.rule)[0])
        safe = tr.settle_margins([0] * 8 + [-1, -1], .5)  # 8 of 10 not lost
        self.assertTrue(tr.record_check(safe, .5, self.rule)[0])
        short = tr.settle_margins([1] * 5, -.5)
        passed, reason = tr.record_check(short, -.5, self.rule)
        self.assertFalse(passed)
        self.assertIn('not enough history', reason)

    def test_no_result_on_or_after_kickoff_day_enters_the_record(self):
        history = pd.DataFrame([
            {'Date': pd.Timestamp('2026-11-01', tz='UTC'), 'HomeTeam': 'Ajax', 'AwayTeam': 'PSV', 'FTHG': 2, 'FTAG': 0},
            {'Date': pd.Timestamp('2026-11-08', tz='UTC'), 'HomeTeam': 'Ajax', 'AwayTeam': 'AZ', 'FTHG': 0, 'FTAG': 4},
            {'Date': pd.Timestamp('2026-11-09', tz='UTC'), 'HomeTeam': 'Utrecht', 'AwayTeam': 'Ajax', 'FTHG': 5,
             'FTAG': 0}])
        cutoff = pd.Timestamp('2026-11-08 18:00', tz='UTC')
        before = form_history(history, 'Ajax', 'Utrecht', cutoff)
        changed = history.copy()
        changed.loc[1:, ['FTHG', 'FTAG']] = [[7, 0], [0, 7]]
        after = form_history(changed, 'Ajax', 'Utrecht', cutoff)
        self.assertEqual(before, after)
        self.assertEqual(tr.bet_record(before['home'], 'Ajax', -.5)['matches'], 1)


class ForecastInputsTest(unittest.TestCase):
    def test_history_names_and_research_margin(self):
        forecast = {'home_team': 'Hull City', 'away_team': 'Leeds',
                    'research_history_json': json.dumps({'home': [row('d', 'Hull', 'X', 1, 0)], 'away': [],
                                                         'h2h': [], 'teams': {'home': 'Hull', 'away': None}}),
                    'team_research_json': json.dumps({'margin_distribution': {'-1': .25, '0': .25, '1': .25, '2': .25}})}
        rows, h2h, team = tr.history_from_forecast(forecast, 'home')
        self.assertEqual((len(rows), team), (1, 'Hull'))
        self.assertEqual(tr.history_from_forecast(forecast, 'away')[2], 'Leeds')
        self.assertAlmostEqual(tr.research_margin_from_forecast(forecast), .5)
        self.assertAlmostEqual(tr.research_margin(([-1, 0, 1, 2], [.25] * 4)), .5)
        self.assertAlmostEqual(tr.backed_margin(.5, 'away', 1.), .5)
        self.assertIsNone(tr.research_margin({'0': .3}))

    def test_elo(self):
        self.assertAlmostEqual(tr.elo_expectancy(.62, 'home'), .62)
        self.assertAlmostEqual(tr.elo_expectancy(.62, 'away'), .38)
        self.assertIsNone(tr.elo_expectancy(None, 'home'))


if __name__ == '__main__':
    unittest.main()
