"""Measured pre-match context, never hand-written goal/probability adjustments.

Use permitted public APIs for venue/weather fallback. Provider rosters are not
confirmed XIs without an explicit confirmation flag. Restricted sites remain
manual reference links, not silently scraped or counted as evidence coverage.
"""
from urllib.parse import urlencode
import re

import pandas as pd

from team_research import name, number, utc

SPORTSDB = 'https://www.thesportsdb.com/api/v1/json/123/'
WEATHER_FIELDS = ('temperature_2m', 'precipitation', 'rain', 'snowfall',
                  'wind_speed_10m', 'wind_gusts_10m', 'relative_humidity_2m')


def source(evidence, response):
    evidence.setdefault('sources', []).append({k: response.get(k)
        for k in ('url', 'observed_at_utc', 'status', 'reason')})


def coords(venue):
    data = venue.get('coordinates') or {}
    if not isinstance(data, dict):
        return None
    lat, lon = number(data.get('latitude')), number(data.get('longitude'))
    if lat is not None and lon is not None and -90 <= lat <= 90 and -180 <= lon <= 180:
        return lat, lon
    return None


def sportsdb_venue(row, client, evidence):
    """Only a soccer fixture with exact teams and kickoff can supply venue ID."""
    kick = utc(row.get('kickoff_utc'))
    url = SPORTSDB + 'searchevents.php?' + urlencode({
        'e': str(row.get('home_team'))+'_vs_'+str(row.get('away_team')), 'd': kick.date().isoformat()})
    response = client.get(url)
    source(evidence, response)
    matches = []
    for event in (response.get('data') or {}).get('event') or []:
        stamp = utc(event.get('strTimestamp') or
                    (str(event.get('dateEvent'))+'T'+str(event.get('strTime'))+'Z'))
        if (event.get('strSport') == 'Soccer' and pd.notna(stamp)
                and abs((stamp-kick).total_seconds()) <= 300
                and name(event.get('strHomeTeam')) == name(row.get('home_team'))
                and name(event.get('strAwayTeam')) == name(row.get('away_team'))
                and event.get('intHomeScore') in (None, '') and event.get('intAwayScore') in (None, '')
                and str(event.get('strStatus') or '').casefold() not in ('postponed', 'cancelled', 'match finished')):
            matches.append(event)
    if len(matches) != 1 or not str(matches[0].get('idVenue') or '').isdigit():
        evidence.setdefault('errors', []).append('TheSportsDB venue: exact fixture identity/time unavailable')
        return None
    venue_id = str(matches[0]['idVenue'])
    response = client.get(SPORTSDB+'lookupvenue.php?'+urlencode({'id': venue_id}))
    source(evidence, response)
    venues = [v for v in (response.get('data') or {}).get('venues') or []
              if str(v.get('idVenue')) == venue_id and v.get('strSport') == 'Soccer']
    if len(venues) != 1:
        return None
    record = venues[0]
    parts = str(record.get('strMap') or '').split(',')
    if len(parts) != 2:
        return None
    venue = {'id': venue_id, 'fullName': record.get('strVenue'),
             'coordinates': {'latitude': number(parts[0]), 'longitude': number(parts[1])},
             'address': {'country': record.get('strCountry')}, 'source': 'TheSportsDB matched-fixture venue'}
    return venue if coords(venue) else None


def collect_weather(row, client, evidence):
    kick = utc(row.get('kickoff_utc'))
    if pd.isna(kick) or utc(client.clock()) >= kick:
        return
    venue = evidence.get('venue') or {}
    location = coords(venue)
    precision = 'stadium coordinates'
    if location is None:
        fallback = sportsdb_venue(row, client, evidence)
        if fallback:
            venue = fallback
            evidence['venue'] = venue
            location = coords(venue)
            precision = 'matched-fixture stadium coordinates; TheSportsDB'
    if location is None:
        address = venue.get('address') or {}
        city, country = address.get('city'), address.get('country')
        country = {'England': 'United Kingdom', 'Scotland': 'United Kingdom'}.get(country, country)
        if city and country:
            response = client.get('https://geocoding-api.open-meteo.com/v1/search?' + urlencode(
                {'name': city, 'count': 10, 'language': 'en', 'format': 'json'}))
            source(evidence, response)
            candidates = [r for r in (response.get('data') or {}).get('results', [])
                          if str(r.get('country', '')).casefold() == str(country).casefold()
                          and str(r.get('name', '')).casefold() == str(city).casefold()]
            if len(candidates) == 1:
                candidate = {'coordinates': {'latitude': candidates[0].get('latitude'),
                                              'longitude': candidates[0].get('longitude')}}
                location = coords(candidate)
                precision = 'venue city centre; stadium coordinates unavailable'
    if location is None:
        evidence.setdefault('errors', []).append('weather unavailable: verified venue coordinates/location missing')
        return
    response = client.get('https://api.open-meteo.com/v1/forecast?' + urlencode({
        'latitude': location[0], 'longitude': location[1], 'hourly': ','.join(WEATHER_FIELDS),
        'timezone': 'UTC', 'forecast_days': 7, 'wind_speed_unit': 'kmh',
        'temperature_unit': 'celsius', 'precipitation_unit': 'mm'}),
        max_age_minutes=15 if kick-utc(client.clock()) <= pd.Timedelta(hours=2) else 180)
    source(evidence, response)
    data = response.get('data') or {}
    hourly, units = data.get('hourly') or {}, data.get('hourly_units') or {}
    hours = []
    for i, value in enumerate(hourly.get('time') or []):
        stamp = utc(value)
        if pd.notna(stamp) and kick.floor('h') <= stamp <= (kick+pd.Timedelta(minutes=105)).floor('h'):
            values = {key: number(hourly[key][i]) for key in WEATHER_FIELDS
                      if isinstance(hourly.get(key), list) and i < len(hourly[key])}
            bounds = {'temperature_2m': (-100, 70), 'precipitation': (0, 1000), 'rain': (0, 1000),
                      'snowfall': (0, 1000), 'wind_speed_10m': (0, 500), 'wind_gusts_10m': (0, 500),
                      'relative_humidity_2m': (0, 100)}
            values = {key: v if v is not None and bounds[key][0] <= v <= bounds[key][1] else None
                      for key, v in values.items()}
            if any(v is not None for v in values.values()):
                hours.append({'time': stamp.isoformat(), **values})
    core = ('temperature_2m', 'precipitation', 'wind_speed_10m')
    required = list(pd.date_range(kick.floor('h'), (kick+pd.Timedelta(minutes=105)).floor('h'), freq='h'))
    complete = (len(hours) == len(required) and {h['time'] for h in hours} == {t.isoformat() for t in required}
                and units.get('temperature_2m') == '°C' and units.get('precipitation') == 'mm'
                and units.get('wind_speed_10m') == 'km/h'
                and all(all(h.get(k) is not None for k in core) for h in hours))
    if not complete:
        evidence.setdefault('errors', []).append('weather forecast incomplete for the match window')
    if not hours:
        return
    evidence['weather'] = {**hours[0], 'hours': hours, 'units': units,
        'observed_at_utc': response.get('observed_at_utc'), 'source': response.get('url'),
        'latitude': location[0], 'longitude': location[1], 'location_precision': precision,
        'complete_match_window': complete, 'roof_status': 'unverified',
        'missing_fields': [key for key in WEATHER_FIELDS if any(h.get(key) is None for h in hours)],
        'effect_on_probabilities': 'context only; no validated coefficient'}
    evidence['weather_location_precision'] = precision
    if complete:
        evidence.setdefault('coverage', {})['weather'] = 'Open-Meteo match-window forecast with units and observation time'


def compact_squads(data, evidence, teams):
    """Retain factual player fields; a roster or predicted XI is not confirmation."""
    def records(value):
        return value if isinstance(value, list) else []
    def obj(value):
        return value if isinstance(value, dict) else {}
    def team_name(group):
        info = obj(group.get('team'))
        expected = teams.get(str(info.get('id')))
        actual = info.get('displayName') or info.get('name')
        if expected and (not actual or name(actual) == name(expected)):
            return expected
        return actual if actual and name(actual) in {name(v) for v in teams.values()} else None
    injury_groups = []
    for group in records(data.get('injuries')):
        if not isinstance(group, dict):
            continue
        team = team_name(group)
        players = []
        for item in records(group.get('injuries')):
            if not isinstance(item, dict):
                continue
            athlete, details = obj(item.get('athlete')), obj(item.get('details'))
            player = athlete.get('displayName') or item.get('name')
            if player:
                players.append({'player': player, 'id': athlete.get('id'), 'status': item.get('status'),
                    'type': item.get('type'), 'detail': details.get('detail'),
                    'expected_return': details.get('returnDate'), 'confirmation': 'provider report; not independently confirmed'})
        if team and players:
            injury_groups.append({'team': team, 'players': players})
    if injury_groups:
        evidence['availability'] = injury_groups
        evidence.setdefault('coverage', {})['availability'] = 'named provider reports; no player-value coefficient'
    squads = []
    for group in records(data.get('rosters')):
        if not isinstance(group, dict) or not team_name(group):
            continue
        players = []
        for item in records(group.get('roster')):
            if not isinstance(item, dict):
                continue
            athlete = obj(item.get('athlete'))
            if athlete.get('displayName'):
                players.append({'player': athlete['displayName'], 'id': athlete.get('id'),
                    'starter': item.get('starter') is True,
                    'position': obj(item.get('position') or athlete.get('position')).get('abbreviation')})
        ids = [str(p['id']) for p in players if p['starter'] and p['id'] is not None]
        explicit = group.get('confirmed') is True or group.get('lineupConfirmed') is True or data.get('lineupsConfirmed') is True
        confirmed = explicit and len(ids) == 11 and len(set(ids)) == 11
        if players:
            squads.append({'team': team_name(group), 'players': players,
                           'formation': group.get('formation'), 'confirmed': confirmed,
                           'status': 'confirmed XI' if confirmed else 'reported roster/starters; confirmation unavailable'})
    if squads:
        if not (len(squads) == 2 and len({name(s['team']) for s in squads}) == 2 and all(s['confirmed'] for s in squads)):
            evidence.setdefault('errors', []).append('starting XIs not explicitly confirmed for both teams')
        evidence['lineups'] = squads
        evidence.setdefault('coverage', {})['lineups'] = (
            'both XIs explicitly confirmed by provider' if len(squads) == 2 and len({name(s['team']) for s in squads}) == 2 and all(s['confirmed'] for s in squads)
            else 'provider roster available; XI confirmation incomplete')


def add_review_links(row, evidence):
    links = [{'label': 'Sofascore', 'url': 'https://www.sofascore.com/football',
              'status': 'reference only; no authorized public bulk API'},
             {'label': 'Sports Mole previews', 'url': 'https://www.sportsmole.co.uk/football/',
              'status': 'reference only; article reproduction requires permission'}]
    if row.get('league') == 'Premier League':
        links.append({'label': 'Premier Injuries', 'url': 'https://www.premierinjuries.com/injury-table.php',
                      'status': 'reference only; copying/network storage restricted by source terms'})
    evidence['review_links'] = links


def espn_news(row, client, evidence, league):
    """Dated team-relevant metadata from the league JSON news feed, no article bodies."""
    from team_research import ESPN
    response = client.get(ESPN+league+'/news?limit=20')
    source(evidence, response)
    cutoff = utc(client.clock())
    leads = []
    for article in (response.get('data') or {}).get('articles') or []:
        published = utc(article.get('published'))
        headline = str(article.get('headline') or '')
        normalized = name(headline)
        mentioned = any(re.search(r'(?:^|\s)'+re.escape(name(row.get(side+'_team')))+r'(?:$|\s)', normalized)
                        for side in ('home', 'away') if name(row.get(side+'_team')))
        url = ((article.get('links') or {}).get('web') or {}).get('href')
        if (mentioned and pd.notna(published) and cutoff-pd.Timedelta(days=7) <= published <= cutoff
                and isinstance(url, str) and url.startswith('https://')):
            leads.append({'headline': headline, 'url': url, 'published_at_utc': published.isoformat(),
                          'source': 'ESPN league news; unconfirmed context lead'})
    return leads[:8]
