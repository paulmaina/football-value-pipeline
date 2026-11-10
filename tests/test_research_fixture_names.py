"""Each side's research form uses its own training history, however the fixture names it.

The fixture ("Hull City", "Real Sociedad") and the training history ("Hull",
"Sociedad") often name a team differently. Research v2 looked the history up under
the fixture name, so 46 of the 158 sides in the domestic forecasts of 5-8 Nov 2026
got no training-history form, and 25 of them no form at all. Research v3 resolves
each side to its training name from reviewed aliases only (never fuzzy matching).
The name pairs below are the real ones from those forecasts; the team lists are the
real training teams in the cached football-data.co.uk files.
"""
from __future__ import annotations

import copy
from functools import lru_cache
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import pandas as pd

import evaluation_harness as eh
import team_research as tr
from football_value_pipeline_v2_standalone import LEAGUES

REPO = Path(__file__).resolve().parents[1]
FIXTURE = json.loads((Path(__file__).with_name('fixtures') / 'frozen_forecast_row.json').read_text(encoding='utf-8'))
CUTOFF = pd.Timestamp('2026-11-08T09:00:00Z')
HISTORY = 'pipeline training history'
ESPN = 'https://site.api.espn.com/apis/site/v2/sports/soccer/all/teams/{}/schedule'

# (league key, fixture name, training name), as seen in the live forecasts of 5-8 Nov 2026.
REVIEWED = [  # already covered by bbs_team_aliases.json / TEAM_ALIASES
    ('EPL', 'Hull City', 'Hull'), ('EPL', 'Coventry City', 'Coventry'), ('EPL', 'Ipswich Town', 'Ipswich'),
    ('EPL', 'Brighton and Hove Albion', 'Brighton'),
    ('LaLiga', 'Real Sociedad', 'Sociedad'), ('LaLiga', 'Rayo Vallecano', 'Vallecano'), ('LaLiga', 'Real Betis', 'Betis'),
    ('LaLiga', 'Celta Vigo', 'Celta'), ('LaLiga', 'Espanyol', 'Espanol'),
    ('LaLiga', 'Real Racing Club de Santander', 'Santander'),
    ('Bundesliga', 'Bayer Leverkusen', 'Leverkusen'), ('Bundesliga', 'Borussia Dortmund', 'Dortmund'),
    ('Bundesliga', 'Eintracht Frankfurt', 'Ein Frankfurt'), ('Bundesliga', 'Hamburger SV', 'Hamburg'),
    ('Bundesliga', 'VfB Stuttgart', 'Stuttgart'), ('Bundesliga', 'TSG Hoffenheim', 'Hoffenheim'),
    ('Bundesliga', 'FSV Mainz 05', 'Mainz'), ('Bundesliga', '1. FC Köln', 'FC Koln'),
    ('SerieA', 'AS Roma', 'Roma'), ('Ligue1', 'AS Monaco', 'Monaco'), ('Ligue1', 'RC Lens', 'Lens'),
    ('Eredivisie', 'Fortuna Sittard', 'For Sittard'),
    ('PrimeiraLiga', 'Sporting Lisbon', 'Sp Lisbon'), ('PrimeiraLiga', 'Vitória SC', 'Guimaraes'),
    ('SuperLig', 'Besiktas JK', 'Besiktas'), ('SuperLig', 'Basaksehir', 'Buyuksehyr'),
    ('SuperLig', 'Çaykur Rizespor', 'Rizespor'), ('SuperLig', 'Kasimpasa SK', 'Kasimpasa'),
]
NEW = [  # added in team_research.HISTORY_ALIASES; the model reached them only by fuzzy matching
    ('Eredivisie', 'ADO Den Haag', 'Den Haag'), ('Eredivisie', 'FC Twente Enschede', 'Twente'),
    ('Eredivisie', 'NEC Nijmegen', 'Nijmegen'), ('Eredivisie', 'PEC Zwolle', 'Zwolle'),
    ('Eredivisie', 'Willem II Tilburg', 'Willem II'),
    ('LaLiga', 'CA Osasuna', 'Osasuna'), ('LaLiga', 'Deportivo Alavés', 'Alaves'),
    ('LaLiga', 'Deportivo La Coruña', 'La Coruna'),
    ('Ligue1', 'RC Strasbourg Alsace', 'Strasbourg'),
    ('PrimeiraLiga', 'Braga', 'Sp Braga'), ('PrimeiraLiga', 'CS Maritimo', 'Maritimo'),
    ('SerieA', 'Atalanta BC', 'Atalanta'),
]


@lru_cache(maxsize=None)
def training_teams(league_key):
    """Real training team names: the 2025/26 and 2026/27 football-data.co.uk files in the cache."""
    teams = set()
    for season in ('2526', '2627'):
        path = REPO / '.football_cache' / f'{season}_{LEAGUES[league_key].football_data_div}.csv'
        frame = pd.read_csv(path, usecols=['HomeTeam', 'AwayTeam'], encoding='latin-1')
        teams |= set(frame['HomeTeam'].dropna()) | set(frame['AwayTeam'].dropna())
    return frozenset(teams)


def result(date, home, away, home_goals, away_goals, source=HISTORY, home_xg=None, away_xg=None):
    return {'date': date, 'home': home, 'away': away, 'home_goals': float(home_goals), 'away_goals': float(away_goals),
            'home_xg': home_xg, 'away_xg': away_xg, 'source': source}


def history_frame(rows):
    return pd.DataFrame([{'Date': pd.Timestamp(d), 'HomeTeam': h, 'AwayTeam': a, 'FTHG': hg, 'FTAG': ag}
                         for d, h, a, hg, ag in rows])


# Hull's and Everton's league results before 8 Nov 2026, as the training history names them.
HULL_EVERTON = history_frame([
    ('2026-11-01', 'Hull', 'Leeds', 1, 0), ('2026-10-25', 'Brentford', 'Hull', 2, 2),
    ('2026-10-18', 'Hull', 'Fulham', 0, 1), ('2026-10-11', 'Hull', 'Everton', 2, 2),
    ('2026-10-04', 'Burnley', 'Hull', 1, 3), ('2026-09-27', 'Hull', 'Wolves', 2, 0),
    ('2026-11-02', 'Everton', 'Chelsea', 1, 1), ('2026-10-26', 'Everton', 'Fulham', 3, 1),
    ('2026-10-19', 'Arsenal', 'Everton', 2, 0), ('2026-10-05', 'Everton', 'Burnley', 1, 0),
    ('2026-09-28', 'Leeds', 'Everton', 0, 0), ('2026-11-09', 'Hull', 'Chelsea', 4, 0)])  # after the cutoff


class HistoryTeamTest(unittest.TestCase):
    def test_real_fixture_names_resolve_to_their_training_name(self):
        for league, fixture, training in REVIEWED + NEW:
            with self.subTest(fixture=fixture):
                self.assertIn(training, training_teams(league))
                self.assertEqual(tr.history_team(fixture, training_teams(league), league), training)

    def test_a_name_both_sources_share_resolves_to_itself(self):
        for league, team in (('EPL', 'Everton'), ('LaLiga', 'Barcelona'), ('SuperLig', 'Galatasaray')):
            self.assertEqual(tr.history_team(team, training_teams(league), league), team)

    def test_never_another_club(self):
        # The model's fuzzy fallback once matched Espanyol to Barcelona and Sporting Lisbon to Porto.
        self.assertIsNone(tr.history_team('Espanyol', {'Barcelona', 'Real Madrid', 'Sevilla'}, 'LaLiga'))
        self.assertIsNone(tr.history_team('Sporting Lisbon', {'Porto', 'Benfica'}, 'PrimeiraLiga'))
        self.assertEqual(tr.history_team('Sporting Lisbon', {'Porto', 'Sp Lisbon'}, 'PrimeiraLiga'), 'Sp Lisbon')
        self.assertIsNone(tr.history_team('Hull City', training_teams('LaLiga'), 'EPL'))
        self.assertIsNone(tr.history_team('Manchester United', {'Man City', 'Liverpool'}, 'EPL'))
        self.assertIsNone(tr.history_team('Real Sociedad', {'Real Madrid', 'Betis'}, 'LaLiga'))

    def test_an_alias_for_another_league_does_not_apply(self):
        self.assertIsNone(tr.history_team('ADO Den Haag', {'Den Haag'}, 'EPL'))

    def test_an_ambiguous_name_is_left_unresolved(self):
        self.assertIsNone(tr.history_team('Hull City', {'Hull', 'Hull '}, 'EPL'))

    def test_the_new_aliases_are_not_in_the_model_and_bbs_alias_file(self):
        # bbs_team_aliases.json also drives the BBS statistics identity checks; leaving it alone
        # keeps the model's goal rates unchanged.
        reviewed = json.loads((REPO / 'bbs_team_aliases.json').read_text(encoding='utf-8'))
        for league, fixture, _ in NEW:
            self.assertNotIn(fixture, reviewed.get(league, {}))
            self.assertEqual(tr.HISTORY_ALIASES[league][fixture], dict((f, t) for _, f, t in NEW)[fixture])


class FormHistoryTest(unittest.TestCase):
    def test_hull_city_gets_hulls_history(self):
        names = {'home': 'Hull', 'away': 'Everton'}
        data = tr.form_history(HULL_EVERTON, 'Hull City', 'Everton', CUTOFF, names=names)
        self.assertEqual(data['teams'], names)
        self.assertEqual(len(data['home']), 6)
        self.assertTrue(all('Hull' in (r['home'], r['away']) for r in data['home']))
        self.assertEqual(len(data['away']), 6)
        self.assertEqual([(r['home'], r['away']) for r in data['h2h']], [('Hull', 'Everton')])

    def test_v2_lookup_under_the_fixture_name_found_nothing(self):
        data = tr.form_history(HULL_EVERTON, 'Hull City', 'Everton', CUTOFF)
        self.assertEqual((len(data['home']), len(data['away']), data['h2h']), (0, 6, []))
        self.assertNotIn('teams', data)

    def test_without_names_the_output_is_unchanged(self):
        # The harness and research backtest name teams as the history does and pass no names.
        data = tr.form_history(HULL_EVERTON, 'Hull', 'Everton', CUTOFF)
        self.assertEqual(set(data), {'home', 'away', 'h2h'})
        named = tr.form_history(HULL_EVERTON, 'Hull', 'Everton', CUTOFF, names={'home': 'Hull', 'away': 'Everton'})
        self.assertEqual({k: v for k, v in named.items() if k != 'teams'}, data)

    def test_an_unresolved_side_is_recorded_and_gets_no_history(self):
        data = tr.form_history(HULL_EVERTON, 'Hull City', 'Everton', CUTOFF, names={'home': None, 'away': 'Everton'})
        self.assertEqual(data['teams'], {'home': None, 'away': 'Everton'})
        self.assertEqual((len(data['home']), len(data['away'])), (0, 6))


def forecast_row(names=True):
    history = tr.form_history(HULL_EVERTON, 'Hull City', 'Everton', CUTOFF,
                              names={'home': 'Hull', 'away': 'Everton'} if names else None)
    return {'home_team': 'Hull City', 'away_team': 'Everton', 'kickoff_utc': '2026-11-08T15:00:00+00:00',
            'lambda_home': 1.3, 'lambda_away': 1.2, 'research_history_json': json.dumps(history, sort_keys=True)}


class PrepareTest(unittest.TestCase):
    def test_v3_gives_hull_city_its_own_form_and_venue_split(self):
        research = tr.prepare(forecast_row(), CUTOFF)
        self.assertEqual(research['version'], tr.VERSION)
        home = research['form']['home']
        self.assertEqual(home['all']['matches'], 6)
        self.assertEqual(home['all']['results'], 'WDLDWW')
        self.assertEqual(home['venue']['matches'], 4)  # Hull's home matches
        self.assertNotEqual(research['goal_rates'], research['base_rates'])
        self.assertFalse(any('training-history name' in w for w in research['warnings']))

    def test_v2_replays_the_old_answer_from_the_same_input(self):
        old = tr.prepare(forecast_row(), CUTOFF, version=tr.V2_VERSION)
        self.assertEqual(old['version'], tr.V2_VERSION)
        self.assertEqual(old['form']['home']['all']['matches'], 0)
        self.assertEqual(old['goal_rates'], old['base_rates'])  # one side without form: no adjustment at all

    def test_v3_without_frozen_names_is_v2(self):
        # Every forecast frozen before v3 has no 'teams': v3 changes nothing for it on its own inputs.
        row = forecast_row(names=False)
        new, old = tr.prepare(row, CUTOFF), tr.prepare(row, CUTOFF, version=tr.V2_VERSION)
        self.assertEqual({k: v for k, v in new.items() if k != 'version'}, {k: v for k, v in old.items() if k != 'version'})

    def test_espn_copies_still_count_once(self):
        # ESPN names Hull "Hull City" too; its copies of the history matches must not add matches.
        history = json.loads(forecast_row()['research_history_json'])
        copies = [{**r, 'home': 'Hull City' if r['home'] == 'Hull' else r['home'],
                   'away': 'Hull City' if r['away'] == 'Hull' else r['away'],
                   'date': r['date'].replace('T00:', 'T15:'), 'source': ESPN.format(306)} for r in history['home']]
        bare = tr.prepare(forecast_row(), CUTOFF)
        both = tr.prepare(forecast_row(), CUTOFF, {'recent': {'home': copies}})
        self.assertEqual(both['form'], bare['form'])
        self.assertEqual(both['goal_rates'], bare['goal_rates'])
        rows = eh._used_rows(tr.research_inputs(forecast_row()), {'recent': {'home': copies}}, CUTOFF, 'home')
        self.assertEqual(len(rows), 6)
        self.assertEqual(eh._double_counted(rows, 'Hull City'), 0)

    def test_an_unresolved_side_is_warned(self):
        history = tr.form_history(HULL_EVERTON, 'Hull City', 'Everton', CUTOFF, names={'home': None, 'away': 'Everton'})
        row = {**forecast_row(), 'research_history_json': json.dumps(history)}
        research = tr.prepare(row, CUTOFF)
        self.assertIn("home team 'Hull City' has no reviewed training-history name; no history form", research['warnings'])

    def test_new_forecasts_are_stamped_v3(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = tr.enrich(pd.DataFrame([forecast_row()]), tmp, fetch=False, clock=lambda: CUTOFF.to_pydatetime())
        research = json.loads(out.iloc[0]['team_research_json'])
        self.assertEqual(research['version'], tr.VERSION)
        self.assertEqual(research['form']['home']['all']['matches'], 6)


class FrozenForecastTest(unittest.TestCase):
    """Brighton v Brentford, frozen 8 Nov 2026 under v1."""

    def test_frozen_v1_forecast_still_replays_exactly(self):
        row = copy.deepcopy(FIXTURE['row'])
        research = json.loads(row['team_research_json'])
        evidence = research['evidence']
        for key in eh.DERIVED_EVIDENCE:
            evidence.pop(key, None)
        again = tr.prepare(row, tr.utc(research['observed_at_utc']), copy.deepcopy(evidence), version=research['version'])
        self.assertEqual(again['version'], tr.LEGACY_VERSION)
        self.assertEqual(again['goal_rates'], research['goal_rates'])
        frozen, replayed = research['margin_distribution'], again['margin_distribution']
        self.assertEqual(set(frozen), set(replayed))
        self.assertLess(max(abs(frozen[k] - replayed[k]) for k in frozen), 1e-12)  # summation order only


class LivePipelineTest(unittest.TestCase):
    """_predict_row freezes each side's training name and its history."""

    def test_hull_city_fixture_gets_hull_history(self):
        from test_value_model_independence import FixedClock, LivePipelineOddsPerturbationTest, live_pipeline, toy_model
        model = toy_model()
        model.teams, model.league_key = ['Everton', 'Hull'], 'EPL'
        model.team_to_idx = {t: i for i, t in enumerate(model.teams)}
        row = LivePipelineOddsPerturbationTest().live_row(1.0)
        row['HomeTeam'], row['AwayTeam'] = 'Hull City', 'Everton'
        pipe = live_pipeline(HULL_EVERTON)
        with patch('football_value_pipeline_v2_standalone.datetime', FixedClock):
            pred, _ = pipe._predict_row(model, row)
        self.assertEqual(pred['model_home_team'], 'Hull')
        history = json.loads(pred['research_history_json'])
        self.assertEqual(history['teams'], {'home': 'Hull', 'away': 'Everton'})
        self.assertEqual(len(history['home']), 5)  # before the model's 1 Nov training cut-off
        self.assertTrue(all('Hull' in (r['home'], r['away']) for r in history['home']))


class ReplayScriptTest(unittest.TestCase):
    """scripts/replay_research_history_names.py rebuilds only the renamed sides."""

    def script(self):
        spec = importlib.util.spec_from_file_location('replay_research_history_names',
                                                      REPO / 'scripts' / 'replay_research_history_names.py')
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module

    def test_rebuilt_history_fills_the_renamed_side_and_keeps_the_other(self):
        script = self.script()
        frozen = tr.form_history(HULL_EVERTON, 'Hull City', 'Everton', CUTOFF)
        frozen['away'][0] = {**frozen['away'][0], 'marker': 'frozen'}  # the unrenamed side is taken as frozen
        row = {'home_team': 'Hull City', 'away_team': 'Everton', 'model_home_team': 'Hull',
               'model_away_team': 'Everton', 'research_history_json': json.dumps(frozen)}
        history = HULL_EVERTON.assign(Date=pd.to_datetime(HULL_EVERTON.Date, utc=True))
        rebuilt, checks = script.rebuilt_history(row, history, CUTOFF.isoformat(), 'EPL', tr)
        self.assertEqual(rebuilt['teams'], {'home': 'Hull', 'away': 'Everton'})
        self.assertEqual(len(rebuilt['home']), 6)
        self.assertEqual(rebuilt['away'][0].get('marker'), 'frozen')
        self.assertEqual(len(rebuilt['h2h']), 1)
        self.assertEqual((checks['home']['renamed'], checks['away']['renamed']), (True, False))
        self.assertTrue(checks['home']['model_name_agrees'] and checks['away']['model_name_agrees'])
        self.assertEqual(checks['home']['frozen_reproduced'], None)  # nothing frozen to compare
        self.assertFalse(checks['away']['frozen_reproduced'])  # the marker differs from a fresh lookup

    def test_replay_reports_before_and_after(self):
        script = self.script()
        meta = {'generated_at_utc': '2026-11-08T08:00:00+00:00'}
        row = {**forecast_row(names=False), 'league': 'Premier League', 'model_home_team': 'Hull',
               'model_away_team': 'Everton'}
        research = tr.prepare(row, CUTOFF, version=tr.LEGACY_VERSION)
        row['team_research_json'] = json.dumps(research, sort_keys=True)
        history = HULL_EVERTON.assign(Date=pd.to_datetime(HULL_EVERTON.Date, utc=True))
        with patch('performance_tracking.snapshots', return_value=[(meta, [row], [])]):
            counts, frame, worst = script.replay(Path('unused'), lambda key: history if key == 'EPL' else None)
        self.assertEqual(counts['frozen_probabilities_reproduced'], 1)
        self.assertEqual((counts['sides_renamed'], counts['frozen_history_sides_reproduced'], counts['changed']), (1, 1, 1))
        record = frame.iloc[0]
        self.assertEqual((record['home_form_matches_before'], record['home_form_matches_after']), (0, 6))
        self.assertGreater(record['max_1x2_move'], 0)
        summary = script.summarize(counts, frame, {})
        latest = summary['latest_forecast_per_fixture']
        self.assertEqual((latest['all']['sides_without_history_before'], latest['all']['sides_without_history_after']), (1, 0))
        self.assertEqual(latest['holdout_leagues']['forecasts'], 0)


if __name__ == '__main__':
    unittest.main()
