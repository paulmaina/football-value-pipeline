"""Each match counts once in the last-ten form, however two sources name the teams.

ESPN and the training history name teams differently ("Hull City" / "Hull",
"Rayo Vallecano" / "Vallecano"). Research v1 identified a result by its names, so
those league matches were counted twice. The rows below are real rows from live
forecasts frozen 5-8 Nov 2026.
"""
from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import pandas as pd

import evaluation_harness as eh
import team_research as tr

REPO = Path(__file__).resolve().parents[1]
FIXTURE = json.loads((Path(__file__).with_name('fixtures') / 'frozen_forecast_row.json').read_text(encoding='utf-8'))
CUTOFF = pd.Timestamp('2026-11-08T09:00:00Z')
HISTORY = 'pipeline training history'
ESPN = 'https://site.api.espn.com/apis/site/v2/sports/soccer/all/teams/{}/schedule'


def result(date, home, away, home_goals, away_goals, source=HISTORY, home_xg=None, away_xg=None):
    return {'date': date, 'home': home, 'away': away, 'home_goals': float(home_goals), 'away_goals': float(away_goals),
            'home_xg': home_xg, 'away_xg': away_xg, 'source': source}


# Everton's form: Hull 2-2 Everton, 11 Oct 2026.
HULL = [result('2026-10-11T00:00:00+00:00', 'Hull', 'Everton', 2, 2, home_xg=1.33, away_xg=1.68),
        result('2026-10-11T13:00:00+00:00', 'Hull City', 'Everton', 2, 2, ESPN.format(368))]
# Alaves' form: Rayo Vallecano 1-1 Alaves, 20 Aug 2026.
RAYO = [result('2026-08-20T00:00:00+00:00', 'Vallecano', 'Alaves', 1, 1, home_xg=0.42, away_xg=2.0),
        result('2026-08-20T19:00:00+00:00', 'Rayo Vallecano', 'Alavés', 1, 1, ESPN.format(96))]


class OneMatchOnceTest(unittest.TestCase):
    def test_hull_city_and_hull_are_one_match(self):
        rows = tr.form_rows('Everton', HULL, CUTOFF)
        self.assertEqual([(r['home'], r['source']) for r in rows], [('Hull', HISTORY)])
        self.assertEqual(tr.weighted_form(rows, 'Everton')['matches'], 1)

    def test_rayo_vallecano_and_vallecano_are_one_match(self):
        rows = tr.form_rows('Alaves', RAYO, CUTOFF)
        self.assertEqual([(r['home'], r['source']) for r in rows], [('Vallecano', HISTORY)])
        self.assertEqual((rows[0]['home_xg'], rows[0]['away_xg']), (0.42, 2.0))  # the history's xG is kept

    def test_version_one_counted_them_twice(self):
        for team, rows in (('Everton', HULL), ('Alaves', RAYO)):
            self.assertEqual(len(tr.form_rows(team, rows, CUTOFF, version=tr.LEGACY_VERSION)), 2)

    def test_source_order_does_not_matter(self):
        rows = tr.form_rows('Everton', HULL[::-1], CUTOFF)
        self.assertEqual(len(rows), 1)
        # ESPN came first and had no xG, so it takes the verified xG from the history copy.
        self.assertEqual((rows[0]['home'], rows[0]['home_xg'], rows[0]['away_xg']), ('Hull City', 1.33, 1.68))
        self.assertEqual(rows[0]['xg_source'], HISTORY)

    def test_xg_from_a_differently_named_copy_is_merged(self):
        history = result('2026-08-20T00:00:00+00:00', 'Vallecano', 'Alaves', 1, 1)
        understat = result('2026-08-20T19:00:00+00:00', 'Rayo Vallecano', 'Alaves', 1, 1,
                           'https://understat.com/league/La_liga/2026', home_xg=0.42, away_xg=2.0)
        rows = tr.form_rows('Alaves', [history, understat], CUTOFF)
        self.assertEqual(len(rows), 1)
        self.assertEqual((rows[0]['home'], rows[0]['home_xg'], rows[0]['xg_source']),
                         ('Vallecano', 0.42, 'https://understat.com/league/La_liga/2026'))

    def test_two_real_games_on_one_day_both_count(self):
        # Besiktas played two friendlies on 14 Jul 2026 (ESPN lists both).
        rows = [result('2026-07-14T14:00:00+00:00', 'Dynamo Malzenice', 'Besiktas', 0, 0, ESPN.format(1895)),
                result('2026-07-14T17:00:00+00:00', 'FC Spartak Trnava', 'Besiktas', 3, 2, ESPN.format(1895))]
        self.assertEqual(len(tr.form_rows('Besiktas', rows, CUTOFF)), 2)

    def test_same_opponent_on_consecutive_days_both_count(self):
        # Tottenham v Hoffenheim, 15 and 16 Aug 2026.
        rows = [result('2026-08-15T14:00:00+00:00', 'Tottenham Hotspur', 'TSG Hoffenheim', 3, 0, ESPN.format(367)),
                result('2026-08-16T14:00:00+00:00', 'Tottenham Hotspur', 'TSG Hoffenheim', 2, 2, ESPN.format(367))]
        self.assertEqual(len(tr.form_rows('Tottenham Hotspur', rows, CUTOFF)), 2)

    def test_same_names_with_a_different_score_keep_the_first_row(self):
        # Unchanged from v1: two sources that disagree on a score do not become two matches.
        rows = [HULL[0], {**HULL[1], 'home': 'Hull', 'home_goals': 3.0}]
        for version in (tr.VERSION, tr.LEGACY_VERSION):
            kept = tr.form_rows('Everton', rows, CUTOFF, version=version)
            self.assertEqual([(r['home_goals'], r['source']) for r in kept], [(2.0, HISTORY)])

    def test_results_on_or_after_the_cutoff_day_and_other_teams_are_left_out(self):
        rows = [*HULL, result('2026-11-08T00:00:00+00:00', 'Everton', 'Leeds', 1, 0),
                result('2026-10-18T00:00:00+00:00', 'Fulham', 'Leeds', 1, 0)]
        self.assertEqual(len(tr.form_rows('Everton', rows, CUTOFF)), 1)


class PrepareTest(unittest.TestCase):
    """The duplicate must not move the goal rates: ESPN's copy of a history match adds nothing."""

    def row(self):
        home = [result(f'2026-{m:02d}-{d:02d}T00:00:00+00:00', 'Hull', 'Everton', hg, ag)
                for m, d, hg, ag in ((10, 11, 2, 2), (9, 20, 0, 1), (9, 6, 1, 3), (8, 23, 0, 0), (8, 9, 1, 2), (5, 17, 2, 4))]
        away = [result(f'2026-{m:02d}-{d:02d}T00:00:00+00:00', 'Vallecano', 'Alaves', hg, ag)
                for m, d, hg, ag in ((8, 20, 1, 1), (5, 10, 2, 0), (4, 26, 3, 1), (4, 12, 0, 0), (3, 29, 1, 0), (3, 15, 2, 2))]
        return {'home_team': 'Everton', 'away_team': 'Alaves', 'kickoff_utc': '2026-11-08T15:00:00+00:00',
                'lambda_home': 1.4, 'lambda_away': 1.1,
                'research_history_json': json.dumps({'home': home, 'away': away, 'h2h': []})}

    def test_espn_copies_of_history_matches_leave_the_research_unchanged(self):
        row = self.row()
        history = json.loads(row['research_history_json'])
        copies = {'home': [{**r, 'home': 'Hull City', 'date': r['date'].replace('T00:', 'T14:'), 'source': ESPN.format(368)}
                           for r in history['home']],
                  'away': [{**r, 'home': 'Rayo Vallecano', 'away': 'Alavés', 'date': r['date'].replace('T00:', 'T19:'),
                            'source': ESPN.format(96)} for r in history['away']]}
        bare = tr.prepare(row, CUTOFF)
        fixed = tr.prepare(row, CUTOFF, {'recent': copy.deepcopy(copies)})
        self.assertEqual(fixed['form'], bare['form'])
        self.assertEqual(fixed['goal_rates'], bare['goal_rates'])
        self.assertEqual(fixed['margin_distribution'], bare['margin_distribution'])
        self.assertEqual(fixed['version'], tr.VERSION)
        legacy = tr.prepare(row, CUTOFF, {'recent': copy.deepcopy(copies)}, version=tr.LEGACY_VERSION)
        self.assertEqual(legacy['version'], tr.LEGACY_VERSION)
        self.assertEqual(legacy['form']['home']['all']['matches'], 10)  # six matches counted as ten
        self.assertNotEqual(legacy['goal_rates'], bare['goal_rates'])

    def test_new_forecasts_are_stamped_with_the_current_version(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = tr.enrich(pd.DataFrame([self.row()]), tmp, fetch=False, clock=lambda: CUTOFF.to_pydatetime())
        self.assertEqual(json.loads(out.iloc[0]['team_research_json'])['version'], 'team-form-research-v3')


def frozen():
    row = copy.deepcopy(FIXTURE['row'])
    research = json.loads(row['team_research_json'])
    evidence = research['evidence']
    for key in eh.DERIVED_EVIDENCE:
        evidence.pop(key, None)
    return row, evidence, tr.utc(research['observed_at_utc']), research


class FrozenForecastTest(unittest.TestCase):
    """Brighton v Brentford, frozen 8 Nov 2026 under v1: Brentford v Hull (City) was in Brentford's form twice."""

    def test_frozen_forecast_replays_exactly_under_its_own_version(self):
        row, evidence, cutoff, research = frozen()
        self.assertEqual(research['version'], tr.LEGACY_VERSION)
        again = tr.prepare(row, cutoff, copy.deepcopy(evidence), version=research['version'])
        self.assertEqual(again['goal_rates'], research['goal_rates'])
        self.assertEqual(again['version'], research['version'])

    def test_current_version_counts_the_hull_match_once(self):
        row, evidence, cutoff, research = frozen()
        inputs = tr.research_inputs(row)
        team = inputs['away_team']
        before = eh._used_rows(inputs, evidence, cutoff, 'away', tr.LEGACY_VERSION)
        after = eh._used_rows(inputs, evidence, cutoff, 'away')
        hull = lambda rows: [r['home'] for r in rows if 'hull' in tr.name(r['home'])]
        self.assertEqual(hull(before), ['Hull City', 'Hull'])
        self.assertEqual(hull(after), ['Hull'])
        self.assertEqual((eh._double_counted(before, team), eh._double_counted(after, team)), (1, 0))
        self.assertEqual(len(after), 10)
        # Nine of the old ten remain, and the next older match takes the freed place.
        key = lambda r: (r['date'], r['home'], r['away'])
        self.assertEqual(len({key(r) for r in after} & {key(r) for r in before}), 9)
        fixed = tr.prepare(row, cutoff, copy.deepcopy(evidence))
        self.assertNotEqual(fixed['form']['away']['all']['results'], research['form']['away']['all']['results'])
        self.assertNotEqual(fixed['goal_rates'], research['goal_rates'])

    def test_the_history_copy_with_xg_is_the_one_kept(self):
        # Brighton's tenth match, Coventry 0-5 Brighton: v1 kept ESPN's copy (no xG) and the
        # history copy fell off the end of the ten. Same ten matches, one more with xG.
        row, evidence, cutoff, research = frozen()
        inputs = tr.research_inputs(row)
        before = eh._used_rows(inputs, evidence, cutoff, 'home', tr.LEGACY_VERSION)
        after = eh._used_rows(inputs, evidence, cutoff, 'home')
        self.assertEqual((before[-1]['home'], before[-1]['home_xg']), ('Coventry City', None))
        self.assertEqual((after[-1]['home'], after[-1]['source']), ('Coventry', HISTORY))
        self.assertIsNotNone(after[-1]['home_xg'])
        fixed = tr.prepare(row, cutoff, copy.deepcopy(evidence))['form']['home']['all']
        frozen_form = research['form']['home']['all']
        self.assertEqual((fixed['results'], fixed['goals_for']), (frozen_form['results'], frozen_form['goals_for']))
        self.assertEqual((frozen_form['xg_matches'], fixed['xg_matches']), (5, 6))


class ReplayScriptTest(unittest.TestCase):
    """scripts/replay_research_versions.py: the before/after comparison recorded with the fix."""

    def script(self):
        spec = importlib.util.spec_from_file_location('replay_research_versions',
                                                      REPO / 'scripts' / 'replay_research_versions.py')
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module

    def test_replay_reports_the_frozen_forecast_before_and_after(self):
        script = self.script()
        meta = {'generated_at_utc': FIXTURE['snapshot_generated_utc']}
        clean = {**FIXTURE['row'], 'home_team': 'Nobody', 'away_team': 'Noone', 'team_research_json': None,
                 'research_history_json': None}
        with patch('performance_tracking.snapshots', return_value=[(meta, [FIXTURE['row'], clean], [])]):
            counts, frame, fixtures, worst = script.replay(Path('unused'))
        self.assertEqual(dict(counts), {'forecasts': 2, 'with_research': 1, 'frozen_probabilities_checked': 1,
                                        'frozen_probabilities_reproduced': 1, 'changed': 1, 'unchanged': 1})
        self.assertLess(worst, 1e-12)
        self.assertEqual(dict(fixtures), {'Premier League': 1})
        record = frame.iloc[0]
        research = json.loads(FIXTURE['row']['team_research_json'])
        self.assertEqual((record.repeated_rows_home, record.repeated_rows_away), (0, 1))
        self.assertEqual((record.goal_rate_home_before, record.goal_rate_away_before), tuple(research['goal_rates']))
        self.assertAlmostEqual(record.p_home_before, float(FIXTURE['row']['research_p_home']), places=12)
        self.assertAlmostEqual(record.p_home_after + record.p_draw_after + record.p_away_after, 1., places=6)
        self.assertGreater(record.max_1x2_move, 0)
        self.assertTrue(record.latest_forecast_of_fixture)
        summary = script.summarize(counts, frame, fixtures)
        latest = summary['latest_forecast_per_fixture']
        self.assertEqual((latest['all']['forecasts'], latest['other_leagues']['forecasts'],
                          latest['holdout_leagues']['forecasts']), (1, 1, 0))
        self.assertEqual(latest['all']['repeated_rows_removed'], 1)
        self.assertEqual(latest['by_league']['Premier League']['fixtures_with_research'], 1)

    def test_replay_reads_no_odds_field(self):
        script = self.script()
        meta = {'generated_at_utc': FIXTURE['snapshot_generated_utc']}
        keep = {*tr.INPUT_SCHEMA, 'league', 'team_research_json'}
        stripped = {k: (v if k in keep else 'garbage') for k, v in FIXTURE['row'].items()}
        frames = []
        for row in (FIXTURE['row'], stripped):
            with patch('performance_tracking.snapshots', return_value=[(meta, [row], [])]):
                frames.append(script.replay(Path('unused'))[1])
        pd.testing.assert_frame_equal(frames[0], frames[1])


if __name__ == '__main__':
    unittest.main()
