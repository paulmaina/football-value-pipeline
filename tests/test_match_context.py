"""Pre-match source identity, completeness, quotas and advisory-only regressions."""
import tempfile
import unittest
from unittest.mock import Mock

import pandas as pd

import match_context as mc
import team_research as tr

NOW = pd.Timestamp('2026-11-05T12:00Z')
ROW = dict(league='Premier League', home_team='Arsenal', away_team='Chelsea',
           kickoff_utc='2026-11-05T14:30Z', lambda_home=1.5, lambda_away=1.1)


class Client:
    def __init__(self, data):
        self.data, self.calls = data, []
    def clock(self):
        return NOW
    def get(self, url, **kwargs):
        self.calls.append((url, kwargs))
        payload = next((value for key, value in self.data.items() if key in url), {})
        return dict(url=url, observed_at_utc=NOW.isoformat(), status='available', data=payload)


def forecast():
    fields = {key: [1., 2., 3.] for key in mc.WEATHER_FIELDS}
    return dict(hourly=dict(time=['2026-11-05T14:00', '2026-11-05T15:00', '2026-11-05T16:00'], **fields),
                hourly_units=dict(temperature_2m='°C', precipitation='mm', rain='mm', snowfall='cm',
                                  wind_speed_10m='km/h', wind_gusts_10m='km/h', relative_humidity_2m='%'))


def event(**extra):
    return dict(strHomeTeam='Arsenal', strAwayTeam='Chelsea', strSport='Soccer',
                strTimestamp=ROW['kickoff_utc'], idVenue='1234', **extra)


def roster(team, confirmed=False):
    return dict(team=dict(id=str(team)), confirmed=confirmed, roster=[
        dict(athlete=dict(id=f'{team}-{i}', displayName=f'Player {team}-{i}'), starter=True)
        for i in range(11)])


class MatchContextTests(unittest.TestCase):
    def test_weather_uses_matched_event_venue_without_espn(self):
        client = Client({'searchevents': {'event': [event()]},
                         'lookupvenue': {'venues': [dict(idVenue='1234', strSport='Soccer',
                            strVenue='Neutral ground', strCountry='England', strMap='51.5, -0.1')]},
                         '/forecast?': forecast()})
        evidence = {}
        mc.collect_weather(ROW, client, evidence)
        self.assertEqual(evidence['venue']['fullName'], 'Neutral ground')
        self.assertTrue(evidence['weather']['complete_match_window'])
        self.assertEqual(len(evidence['weather']['hours']), 3)
        self.assertEqual(evidence['weather']['units']['snowfall'], 'cm')
        self.assertIn('weather', evidence['coverage'])
        self.assertIn('context only', evidence['weather']['effect_on_probabilities'])

    def test_venue_rejects_wrong_ambiguous_finished_and_mistimed_events(self):
        wrong = event(); wrong['strHomeTeam'] = 'Manchester City'
        late = event(); late['strTimestamp'] = '2026-11-05T15:30Z'
        for values in ([wrong], [event(), event()], [event(intHomeScore='1')], [late]):
            with self.subTest(values=values):
                client = Client({'searchevents': {'event': values}})
                self.assertIsNone(mc.sportsdb_venue(ROW, client, {}))
                self.assertEqual(len(client.calls), 1)
        self.assertIsNone(mc.coords({'coordinates': {'latitude': float('nan'), 'longitude': 20}}))
        self.assertIsNone(mc.coords({'coordinates': {'latitude': 91, 'longitude': 20}}))

    def test_weather_missing_invalid_units_or_hours_stays_partial(self):
        for mode in ('null', 'negative', 'units', 'missing_hour'):
            data = forecast()
            if mode == 'null': data['hourly']['temperature_2m'][1] = None
            if mode == 'negative': data['hourly']['precipitation'][1] = -1
            if mode == 'units': data['hourly_units']['wind_speed_10m'] = 'm/s'
            if mode == 'missing_hour': data['hourly']['time'].pop()
            evidence = {'venue': {'coordinates': {'latitude': 51, 'longitude': 0}}}
            mc.collect_weather(ROW, Client({'/forecast?': data}), evidence)
            self.assertFalse(evidence['weather']['complete_match_window'])
            self.assertNotIn('weather', evidence.get('coverage', {}))
            self.assertTrue(evidence['errors'])

    def test_near_kickoff_weather_requests_short_ttl(self):
        row = dict(ROW, kickoff_utc='2026-11-05T13:00Z')
        client = Client({'/forecast?': forecast()})
        mc.collect_weather(row, client, {'venue': {'coordinates': {'latitude': 51, 'longitude': 0}}})
        self.assertEqual(client.calls[0][1]['max_age_minutes'], 15)

    def test_roster_is_not_confirmed_without_explicit_flag_and_full_xis(self):
        teams = {'1': 'Arsenal', '2': 'Chelsea'}
        evidence = {}
        mc.compact_squads({'rosters': [roster(1), roster(2)]}, evidence, teams)
        self.assertTrue(all(not s['confirmed'] for s in evidence['lineups']))
        self.assertTrue(evidence['errors'])
        evidence = {}
        mc.compact_squads({'rosters': [roster(1, True), roster(2, True)]}, evidence, teams)
        self.assertEqual(evidence['coverage']['lineups'], 'both XIs explicitly confirmed by provider')
        duplicate = roster(1, True); duplicate['roster'][-1] = duplicate['roster'][0]
        evidence = {}
        mc.compact_squads({'rosters': [duplicate, roster(2, True), roster(3, True)]}, evidence, teams)
        self.assertFalse(evidence['lineups'][0]['confirmed'])
        self.assertEqual(len(evidence['lineups']), 2)

    def test_injury_records_are_named_team_bound_and_compact(self):
        evidence = {}
        mc.compact_squads({'injuries': [dict(team=dict(id='1'), injuries=[
            dict(athlete=dict(id='9', displayName='Player'), status='Doubtful',
                 details={'detail': 'Ankle'}, article='do not store article')]),
            dict(team=dict(id='2'), injuries=[])]}, evidence, {'1': 'Arsenal', '2': 'Chelsea'})
        self.assertEqual(len(evidence['availability']), 1)
        self.assertNotIn('article', str(evidence))
        self.assertEqual(evidence['availability'][0]['players'][0]['status'], 'Doubtful')
        mc.compact_squads({'injuries': [None, {'team': 'malformed'}],
                          'rosters': [{'team': {'id': '1'}, 'roster': [{'athlete': 'bad'}]}]}, {}, {'1': 'Arsenal'})

    def test_news_rejects_future_and_substring_team_matches(self):
        articles = [dict(headline=title, published=date, links={'web': {'href': 'https://www.espn.com/story/1'}})
                    for title, date in [('Inter team news', NOW.isoformat()),
                                        ('International football', NOW.isoformat()),
                                        ('Inter win tomorrow', (NOW+pd.Timedelta(hours=1)).isoformat())]]
        news = mc.espn_news(dict(ROW, home_team='Inter'), Client({'/news?': {'articles': articles}}), {}, 'ita.1')
        self.assertEqual([n['headline'] for n in news], ['Inter team news'])

    def test_short_ttl_refetches_and_sportsdb_quota_is_bounded(self):
        with tempfile.TemporaryDirectory() as tmp:
            session = Mock(); session.get.return_value = Mock(content=b'{}', json=lambda: {})
            first = tr.FreeSources(tmp, session=session, clock=lambda: NOW)
            url = 'https://example.test/summary'
            first.get(url)
            later = tr.FreeSources(tmp, session=session, clock=lambda: NOW+pd.Timedelta(minutes=6))
            later.get(url, max_age_minutes=5)
            self.assertEqual(session.get.call_count, 2)
            for i in range(31):
                value = later.get(mc.SPORTSDB+'lookupvenue.php?id='+str(i))
            self.assertEqual(session.get.call_count, 32)
            self.assertIn('30 requests', value['reason'])
            later.get(mc.SPORTSDB+'lookupvenue.php?id=0')
            self.assertEqual(session.get.call_count, 32)

    def test_post_kickoff_collection_never_requests_new_context(self):
        client = Client({})
        result = tr.collect_fixture(dict(ROW, kickoff_utc=NOW.isoformat()), client)
        self.assertEqual(client.calls, [])
        self.assertIn('deadline', result['errors'][0])

    def test_context_changes_do_not_apply_unvalidated_probability_effects(self):
        plain = tr.prepare(ROW, NOW)
        evidence = {'weather': forecast(), 'lineups': [roster(1, True)],
                    'availability': [{'players': ['Missing striker']}], 'coverage': {'weather': 'forecast'}}
        context = tr.prepare(ROW, NOW, evidence)
        self.assertEqual(plain['goal_rates'], context['goal_rates'])
        self.assertEqual(plain['margin_distribution'], context['margin_distribution'])
        self.assertEqual(plain['p_over_1_5'], context['p_over_1_5'])
        mc.add_review_links(ROW, evidence)
        self.assertEqual(len(evidence['review_links']), 3)
        self.assertNotIn('availability', evidence['coverage'])
