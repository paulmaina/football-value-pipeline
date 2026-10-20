"""Supplementary API-Football observations, independent of production predictions.

The account's 100/day free allowance is not a reason to spend it all. Persist
reservations before requests, leave 20 calls in reserve, and never call from fits.
"""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import time
from urllib.parse import urlencode

from bbs_data import Store, Deferred, FetchError, atomic_json, decode, dumps, utc
from match_scores import valid_goals

BASE = 'https://v3.football.api-sports.io'
LEAGUES = {'EPL': 39, 'LaLiga': 140, 'Bundesliga': 78, 'SerieA': 135, 'Ligue1': 61, 'UCL': 2}
STAT_NAMES = dict(zip(('Shots on Goal', 'Shots off Goal', 'Total Shots', 'Blocked Shots',
    'Shots insidebox', 'Shots outsidebox', 'Fouls', 'Corner Kicks', 'Offsides',
    'Ball Possession', 'Yellow Cards', 'Red Cards', 'Goalkeeper Saves', 'Total passes',
    'Passes accurate', 'Passes %'),
    ('shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots',
    'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides',
    'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes',
    'accurate_passes', 'pass_percentage')))
STATUSES = set('TBD NS 1H HT 2H ET BT P SUSP INT FT AET PEN PST CANC ABD AWD WO LIVE'.split())
FINISHED = {'FT', 'AET', 'PEN'}
FREE_SEASONS = (2022, 2023, 2024)


class QueryRejected(FetchError):
    def __init__(self, reason):
        self.reason = reason
        super().__init__('API-Football query unavailable: '+reason)


def rejection_reason(errors):
    # Only fixed categories survive; arbitrary provider text may echo credentials.
    if isinstance(errors, dict):
        for key, reason in (('plan', 'PLAN_RESTRICTED'), ('token', 'CREDENTIALS_REJECTED'),
                            ('requests', 'REQUEST_LIMIT'), ('rateLimit', 'REQUEST_LIMIT')):
            if key in errors:
                return reason
    return 'QUERY_REJECTED'


def payload_digest(value):
    return hashlib.sha256(dumps(value).encode()).hexdigest()


def main_ucl_stage(round_name):
    return isinstance(round_name, str) and bool(re.fullmatch(
        r'(league stage|league phase|group stage|knockout round play-offs|round of 16|8th finals|quarter-finals|semi-finals|final)( - .+)?',
        round_name.strip().lower()))


def transport(path, params, token):
    import requests
    try:
        response = requests.get(BASE+path, params=params, headers={'x-apisports-key': token},
                                timeout=(10, 30), allow_redirects=False)
        if len(response.content) > 10_000_000:
            raise FetchError('API-Football response exceeds size limit')
        return response.status_code, dict(response.headers), response.content
    except requests.RequestException:
        raise FetchError('API-Football network request failed') from None


class Client:
    def __init__(self, store, token, daily_budget=80, max_requests=20, *, sender=transport,
                 clock=lambda: datetime.now(timezone.utc), sleeper=time.sleep):
        if not token.strip():
            raise ValueError('API_FOOTBALL_KEY is required')
        if not 1 <= daily_budget <= 80 or not 1 <= max_requests <= 80:
            raise ValueError('API-Football free-plan budgets must be between 1 and 80')
        self.store, self.token = store, token
        self.daily_budget, self.max_requests = daily_budget, max_requests
        self.sender, self.clock, self.sleeper = sender, clock, sleeper
        self.requests = 0

    def get(self, path, params, ttl=21600):
        query = path+'?'+urlencode(sorted(params.items()))
        now = self.clock(); day = now.date().isoformat()
        cached = self.store.latest_response(query)
        payload = decode(cached['payload']) if cached else {}
        cache_ttl = min(ttl, 21600) if payload.get('unavailable') else ttl
        if cached and 0 <= (now-utc(cached['observed'])).total_seconds() < cache_ttl:
            if payload.get('unavailable'):
                raise QueryRejected(cached_reason if (cached_reason := payload.get('reason')) in
                                    {'PLAN_RESTRICTED', 'CREDENTIALS_REJECTED', 'REQUEST_LIMIT', 'QUERY_REJECTED'}
                                    else 'QUERY_REJECTED')
            return payload, cached['observed']
        if self.requests >= self.max_requests or self.store.setting('blocked_day') == day:
            raise Deferred('API-Football request budget exhausted or provider rate limited')
        last = float(self.store.setting('last_request', '0'))
        self.sleeper(max(0., 7.-(now.timestamp()-last)))
        now = self.clock()
        self.store.reserve(now, self.daily_budget)
        self.store.set('last_request', now.timestamp())
        self.requests += 1
        status, headers, body = self.sender(path, params, self.token)
        observed = self.clock().isoformat()
        headers = {k.lower(): v for k, v in headers.items()}
        remaining = headers.get('x-ratelimit-requests-remaining')
        if remaining is not None:
            try:
                if int(remaining) <= 20:
                    self.store.set('blocked_day', self.clock().date().isoformat())
            except (ValueError, TypeError):
                raise FetchError('Invalid API-Football quota header') from None
        if status == 429:
            self.store.set('blocked_day', self.clock().date().isoformat())
            raise Deferred('API-Football rate limited; stopped until next UTC day')
        if status != 200:
            raise FetchError('API-Football HTTP '+str(status))
        try:
            data = decode(body)
        except (ValueError, TypeError, UnicodeError):
            raise FetchError('Malformed API-Football JSON') from None
        if not isinstance(data, dict):
            raise FetchError('Malformed API-Football response envelope')
        if data.get('errors'):
            # Do not log or persist arbitrary server errors that could echo a key.
            reason = rejection_reason(data['errors'])
            self.store.response(query, observed, {'unavailable': True, 'reason': reason})
            raise QueryRejected(reason)
        if not isinstance(data.get('response'), list):
            raise FetchError('Malformed API-Football response envelope')
        if data.get('paging', {}).get('total') != 1 or data.get('results') != len(data['response']):
            raise FetchError('Incomplete API-Football response; no partial season accepted')
        self.store.response(query, observed, data)
        return data, observed


def normal_match(row, league, year, observed):
    fixture, competition, teams = row['fixture'], row['league'], row['teams']
    kick = utc(fixture['date']); clock = utc(observed)
    if (type(fixture.get('id')) is not int or fixture['id'] <= 0
            or competition.get('id') != LEAGUES[league] or competition.get('season') != year
            or not datetime(year, 6 if league == 'UCL' else 7, 1, tzinfo=timezone.utc) <= kick < datetime(year+1, 7, 1, tzinfo=timezone.utc)):
        raise ValueError('Invalid API-Football fixture identity, competition or season')
    for side in ('home', 'away'):
        team = teams[side]
        if (type(team.get('id')) is not int or team['id'] <= 0
                or not isinstance(team.get('name'), str) or not team['name'].strip()):
            raise ValueError('Invalid API-Football team')
    if teams['home']['id'] == teams['away']['id'] or teams['home']['name'] == teams['away']['name']:
        raise ValueError('Invalid API-Football opponents')
    status = fixture['status']['short']
    if status not in STATUSES:
        raise ValueError('Unknown API-Football fixture status')
    score = valid_goals(row.get('score', {}).get('fulltime')) if status in FINISHED else None
    if status in FINISHED and (score is None or kick >= clock):
        raise ValueError('Unavailable API-Football regulation score or future finished fixture')
    if status == 'FT' and valid_goals(row.get('goals')) != score:
        raise ValueError('API-Football final scores disagree')
    return {'id': fixture['id'], 'league': league, 'season': year, 'kickoff_utc': kick.isoformat(),
        'status': status, 'home': {k: teams['home'][k] for k in ('id', 'name')},
        'away': {k: teams['away'][k] for k in ('id', 'name')},
        'score': None if score is None else {'home': score[0], 'away': score[1]},
        'regulation_score_verified': score is not None, 'source': 'api-football',
        'round': competition.get('round'),
        'training_scope_eligible': league != 'UCL' or main_ucl_stage(competition.get('round'))}


def normal_statistics(rows, match):
    from bbs_statistics_model import clean
    if match['status'] != 'FT':
        raise ValueError('API-Football extra-time statistics are not regulation-only features')
    if len(rows) != 2:
        raise ValueError('API-Football statistics require two teams')
    output = {'available': True, 'team_ids': {s: str(match[s]['id']) for s in ('home', 'away')}}
    indexed = {r['team']['id']: r for r in rows}
    if len(indexed) != 2 or set(indexed) != {match[s]['id'] for s in ('home', 'away')}:
        raise ValueError('API-Football statistics team mismatch')
    for side in ('home', 'away'):
        values = {}; seen = set()
        for stat in indexed[match[side]['id']]['statistics']:
            name = stat.get('type')
            if name not in STAT_NAMES:
                continue
            if name in seen:
                raise ValueError('Duplicate API-Football statistic')
            seen.add(name)
            value = stat.get('value')
            if isinstance(value, str) and name in ('Ball Possession', 'Passes %'):
                value = float(value.removesuffix('%'))
            values[STAT_NAMES[name]] = value
        output[side] = clean(values)
    output['available'] = all(any(v is not None for v in output[s].values()) for s in ('home', 'away'))
    return output


def observations(cache, kind, cutoff):
    """Verify immutable observation hashes before exposing cached provider data."""
    result = []
    for path in sorted((Path(cache)/'api_football/state/observations'/kind).glob('*.json')):
        row = decode(path.read_text(encoding='utf-8'))
        digest = hashlib.sha256(dumps(row).encode()).hexdigest()
        if path.is_symlink() or not path.stem.endswith('_'+digest) or row.get('kind') != kind:
            raise ValueError('API-Football observation checksum mismatch')
        if utc(row['observed']) <= utc(cutoff):
            result.append(row)
    return result


def collect(client, leagues, seasons, stats_limit=10):
    report = {'status': 'complete', 'queries': [], 'quarantined_matches': 0,
              'statistics_saved': 0, 'statistics_failures': [], 'requests': 0}
    known = {(r['league'], r['entity']): r for r in client.store.latest('match', client.clock().isoformat())}
    quarantine = {(r['league'], r['entity']): r for r in client.store.latest('quarantine', client.clock().isoformat())}
    for league in leagues:
        for year in seasons:
            try:
                # Closed seasons do not need three downloads every day.
                historical = year < client.clock().year - (client.clock().month < 7) - 1
                data, observed = client.get('/fixtures', {'league': LEAGUES[league], 'season': year},
                                            ttl=30*86400 if historical else 21600)
                if not data['response']:
                    report['status'] = 'partial'
                seen = set(); schedule = {}
                for row in data['response']:
                    entity = str(row.get('fixture', {}).get('id', 'unknown')) if isinstance(row, dict) else 'unknown'
                    try:
                        value = normal_match(row, league, year, observed)
                        if value['id'] in seen:
                            raise ValueError('Duplicate API-Football match ID')
                        seen.add(value['id'])
                        previous = known.get((league, entity)); held = quarantine.get((league, entity))
                        if (previous is None or previous['payload'] != value or
                                (held and utc(held['observed']) >= utc(previous['observed']))):
                            client.store.put('match', league, entity, observed, value)
                        if value['status'] == 'NS':
                            schedule[entity] = payload_digest(value)
                    except (ValueError, KeyError, TypeError, AttributeError):
                        client.store.put('quarantine', league, entity, observed, {'reason': 'invalid_fixture'})
                        report['quarantined_matches'] += 1
                        report['status'] = 'partial'
                client.store.put('schedule', league, str(year), observed, {'match_sha256': schedule})
                report['queries'].append({'league': league, 'season': year, 'status': 'collected',
                                          'fixtures': len(data['response'])})
            except (FetchError, ValueError, OSError) as exc:
                report['status'] = 'partial'
                report['queries'].append({'league': league, 'season': year, 'status': type(exc).__name__,
                                          'reason': exc.reason if isinstance(exc, QueryRejected) else
                                          'REQUEST_BUDGET_OR_RATE_LIMIT' if isinstance(exc, Deferred) else 'FETCH_FAILED'})
    matches = client.store.latest('match', client.clock().isoformat())
    held = {(r['league'], r['entity']): r for r in client.store.latest('quarantine', client.clock().isoformat())}
    matches = [r for r in matches if r['league'] in leagues and r['payload']['season'] in seasons
               and r['payload']['status'] == 'FT'
               and r['payload']['training_scope_eligible']
               and utc(r['payload']['kickoff_utc']) < client.clock()
               and ((r['league'], r['entity']) not in held or
                    utc(held[(r['league'], r['entity'])]['observed']) < utc(r['observed']))]
    # Newest results first; cached historical statistics allow backfill to advance.
    matches.sort(key=lambda r: r['payload']['kickoff_utc'], reverse=True)
    saved_stats = {(r['league'], r['entity']): r for r in client.store.latest('statistics', client.clock().isoformat())}
    count = 0
    for row in matches:
        if count >= stats_limit:
            break
        query = '/fixtures/statistics?'+urlencode([('fixture', row['payload']['id'])])
        old = client.store.latest_response(query)
        saved = saved_stats.get((row['league'], row['entity']))
        historical = row['payload']['season'] < client.clock().year - (client.clock().month < 7) - 1
        if saved and saved['payload'].get('available'):
            ttl = 36500*86400 if historical else 7*86400
        else:
            ttl = 7*86400 if historical else 21600
        if (old and saved and old['observed'] == saved['observed']
                and (client.clock()-utc(old['observed'])).total_seconds() < ttl):
            if not saved['payload'].get('available'):
                report['status'] = 'partial'
            continue
        if old and decode(old['payload']).get('unavailable') and 0 <= (client.clock()-utc(old['observed'])).total_seconds() < 21600:
            report['status'] = 'partial'
            report['statistics_failures'].append({'league': row['league'], 'fixture': row['entity'],
                                                  'reason': 'CACHED_QUERY_REJECTED'})
            continue
        count += 1
        try:
            data, observed = client.get('/fixtures/statistics', {'fixture': row['payload']['id']}, ttl=ttl)
            try:
                value = normal_statistics(data['response'], row['payload'])
            except (ValueError, KeyError, TypeError, AttributeError):
                value = {'available': False}
                report['status'] = 'partial'
            if not value.get('available'):
                report['status'] = 'partial'
            client.store.put('statistics', row['league'], row['entity'], observed, value)
            report['statistics_saved'] += 1
        except (FetchError, ValueError, OSError) as exc:
            report['status'] = 'partial'
            report['statistics_failures'].append({'league': row['league'], 'fixture': row['entity'],
                'reason': exc.reason if isinstance(exc, QueryRejected) else
                          'REQUEST_BUDGET_OR_RATE_LIMIT' if isinstance(exc, Deferred) else 'FETCH_FAILED'})
            # A failed request is not a new observation about the match. Keep
            # valid saved statistics; only a received invalid/empty revision
            # above can supersede them with an unavailable tombstone.
    report['fixtures_collected'] = sum(q.get('fixtures', 0) for q in report['queries'])
    report['plan_restricted_queries'] = sum(q.get('reason') == 'PLAN_RESTRICTED' for q in report['queries'])
    report['requests'] = client.requests
    return report
