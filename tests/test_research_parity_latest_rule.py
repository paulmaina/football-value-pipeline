"""scripts/research_parity_latest_rule.py: ESPN competition labels and the gap split (report only)."""
from __future__ import annotations

import importlib.util
from pathlib import Path
import unittest

import pandas as pd

import team_research as tr

REPO = Path(__file__).resolve().parents[1]
SOURCE = 'https://site.api.espn.com/apis/site/v2/sports/soccer/all/teams/359/schedule'


def script():
    spec = importlib.util.spec_from_file_location('research_parity_latest_rule',
                                                  REPO / 'scripts' / 'research_parity_latest_rule.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def event(date, league, hg, ag):
    return {'date': date, 'league': league, 'home': 'Arsenal', 'away': 'Other', 'home_goals': hg, 'away_goals': ag}


LABELS = {'359/2026': [event('2026-10-21T19:00Z', 'uefa.champions', 2, 0), event('2026-10-29T19:45Z', 'eng.league_cup', 3, 1),
                       event('2026-10-11T13:00Z', 'club.friendly', 1, 1), event('2026-10-25T15:00Z', 'eng.1', 1, 0),
                       event('2026-11-01T15:00Z', 'eng.charity', 0, 0), event('2026-08-06T18:00Z', 'esp.joan_gamper', 2, 2)],
          '359/2025': [event('2026-05-24T15:00Z', 'eng.1', 2, 1)]}


def row(date, hg, ag):
    return {'date': date, 'home': 'Arsenal', 'away': 'Other', 'home_goals': float(hg), 'away_goals': float(ag), 'source': SOURCE}


class ClassifyTest(unittest.TestCase):
    def test_espn_league_slug_decides_the_class(self):
        m = script()
        cases = [('2026-10-21T19:00:00+00:00', 2, 0, 'european'), ('2026-10-29T19:45:00+00:00', 3, 1, 'domestic_cup'),
                 ('2026-10-11T13:00:00+00:00', 1, 1, 'friendly'), ('2026-10-25T15:00:00+00:00', 1, 0, 'league'),
                 ('2026-11-01T15:00:00+00:00', 0, 0, 'domestic_other'), ('2026-08-06T18:00:00+00:00', 2, 2, 'friendly'),
                 ('2026-05-24T15:00:00+00:00', 2, 1, 'league')]  # previous season's schedule
        for date, hg, ag, expected in cases:
            with self.subTest(date=date):
                self.assertEqual(m.classify(row(date, hg, ag), LABELS, 'eng.1', tr)[0], expected)

    def test_wrong_score_or_day_is_unknown(self):
        m = script()
        self.assertEqual(m.classify(row('2026-10-21T19:00:00+00:00', 1, 0), LABELS, 'eng.1', tr)[0], 'unknown')
        self.assertEqual(m.classify(row('2026-10-24T19:00:00+00:00', 2, 0), LABELS, 'eng.1', tr)[0], 'unknown')

    def test_for_a_european_fixture_a_domestic_top_flight_is_the_league(self):
        m = script()
        labels = {'359/2026': [event('2026-10-25T15:00Z', 'nor.1', 1, 0)]}
        self.assertEqual(m.classify(row('2026-10-25T15:00:00+00:00', 1, 0), labels, 'uefa.europa', tr)[0], 'league')

    def test_without_evidence_nothing_is_dropped(self):
        m = script()
        evidence = {'recent': {'home': [row('2026-10-21T19:00:00+00:00', 2, 0)]}}
        labelled = {'home': [(evidence['recent']['home'][0], 'european')]}
        self.assertEqual(m.without(evidence, (), labelled), evidence)
        self.assertEqual(m.without(evidence, ('european',), labelled)['recent']['home'], [])


class SplitTest(unittest.TestCase):
    def test_the_split_adds_up_to_the_gap(self):
        m = script()
        gaps = {'live': [.05, .02], 'no_cup': [.04, .02], 'no_european': [.02, .01], 'no_cup_no_european': [.015, .01],
                'league_only': [.01, .005]}
        frame = pd.DataFrame({**{f'gap_{k}': v for k, v in gaps.items()}, 'gap_frozen': [.06, .03],
                              'gap_league_only_harness_rates': [.004, .001], 'lambda_max_abs_diff': [.1, .0],
                              'harness_compared': [True, True], 'evidence_used': [True, True],
                              **{f'espn_rows_used_{c}': [1, 0] for c in m.CLASSES},
                              **{f'{k}_vs_live_1x2': [.01, .0] for k in m.SCENARIOS}})
        split = m.summarize_group(frame)['harness_vs_live']['mean_gap_split']
        parts = [v for k, v in split.items() if k != 'total_current_rule']
        self.assertAlmostEqual(sum(parts), split['total_current_rule'])


if __name__ == '__main__':
    unittest.main()
