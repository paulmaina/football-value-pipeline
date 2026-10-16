"""Big Balls Free collection: bounded requests, durable observations and replay cutoffs.

No model fitting or forecast mutation. Raw responses never contain request headers.
"""
from __future__ import annotations

import json
import math
import sqlite3
import time
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path
from urllib.parse import urlencode

BASE_URL = 'https://api.bigballsdata.com'
LEAGUES = {'EPL': 'epl', 'LaLiga': 'laliga', 'Bundesliga': 'bundesliga',
           'SerieA': 'serie_a', 'Ligue1': 'ligue1', 'UCL': 'cl'}
DISPLAY_NAMES = {'EPL': {'epl', 'premier league', 'english premier league'},
 'LaLiga': {'laliga', 'la liga'}, 'Bundesliga': {'bundesliga'},
 'SerieA': {'serie_a', 'serie-a', 'seriea', 'serie a'}, 'Ligue1': {'ligue-1', 'ligue1', 'ligue 1'},
 'UCL': {'cl', 'ucl', 'uefa champions league', 'champions league'}}
STAT_FIELDS = ('shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots',
 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides',
 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes',
 'accurate_passes', 'pass_percentage')


def utc(value):
    result = datetime.fromisoformat(str(value).replace('Z', '+00:00'))
    if result.tzinfo is None:
        raise ValueError('Expected timezone-aware timestamp')
    return result.astimezone(timezone.utc)


def dumps(value):
    return json.dumps(value, sort_keys=True, allow_nan=False, separators=(',', ':'))


def decode(value):
    def invalid(_):
        raise ValueError('Nonfinite JSON value')
    return json.loads(value, parse_constant=invalid)


class FetchError(RuntimeError):
    """Safe message only: never includes request headers, key or server body."""


class Deferred(FetchError):
    pass


class Store:
    def __init__(self, path):
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        self.db = sqlite3.connect(path, timeout=30)
        self.db.row_factory = sqlite3.Row
        self.db.executescript('''
          CREATE TABLE IF NOT EXISTS responses (
            query TEXT, observed TEXT, payload TEXT, PRIMARY KEY(query,observed));
          CREATE TABLE IF NOT EXISTS observations (
            kind TEXT, league TEXT, entity TEXT, observed TEXT, payload TEXT, query TEXT,
            PRIMARY KEY(kind,league,entity,observed));
          CREATE TABLE IF NOT EXISTS quota (day TEXT PRIMARY KEY, used INTEGER NOT NULL);
          CREATE TABLE IF NOT EXISTS settings (name TEXT PRIMARY KEY, value TEXT);
        ''')

    def close(self):
        self.db.close()

    def setting(self, name, default=''):
        row = self.db.execute('SELECT value FROM settings WHERE name=?', (name,)).fetchone()
        return row[0] if row else default

    def set(self, name, value):
        with self.db:
            self.db.execute('INSERT OR REPLACE INTO settings VALUES (?,?)', (name, str(value)))

    def latest_response(self, query):
        row = self.db.execute('SELECT * FROM responses WHERE query=? ORDER BY observed DESC LIMIT 1', (query,)).fetchone()
        return dict(row) if row else None

    def response(self, query, observed, payload):
        with self.db:
            self.db.execute('INSERT OR REPLACE INTO responses VALUES (?,?,?)', (query, observed, dumps(payload)))

    def put(self, kind, league, entity, observed, payload, query=''):
        with self.db:
            self.db.execute('INSERT OR REPLACE INTO observations VALUES (?,?,?,?,?,?)',
                            (kind, league, str(entity), observed, dumps(payload), query))

    def latest(self, kind, cutoff=None):
        cutoff = utc(cutoff or datetime.now(timezone.utc).isoformat())
        # ISO strings with offsets or different fractional precision do not sort
        # chronologically. Parse before cutoff filtering, including older stores.
        rows = sorted(self.db.execute('SELECT * FROM observations WHERE kind=?', (kind,)),
                      key=lambda row: utc(row['observed']))
        result = {}
        for row in rows:
            if utc(row['observed']) > cutoff:
                continue
            result[(row['league'], row['entity'])] = {
                **dict(row), 'payload': decode(row['payload'])}
        return list(result.values())

    def reserve(self, now, limit):
        """Commit before I/O: failures and interrupted requests also consume budget."""
        day = now.date().isoformat()
        self.db.execute('BEGIN IMMEDIATE')
        try:
            row = self.db.execute('SELECT used FROM quota WHERE day=?', (day,)).fetchone()
            used = row[0] if row else 0
            if used >= limit:
                raise Deferred('Local daily request budget exhausted')
            self.db.execute('INSERT OR REPLACE INTO quota VALUES (?,?)', (day, used + 1))
            self.db.commit()
        except Exception:
            self.db.rollback()
            raise


def transport(path, params, key):
    import requests
    try:
        response = requests.get(BASE_URL + path, params=params,
            headers={'Authorization': 'Bearer ' + key}, timeout=(10, 30), allow_redirects=False)
        # No redirect may forward credentials to an unexpected host.
        if len(response.content) > 10_000_000:
            raise FetchError('Response exceeds 10 MB')
        return response.status_code, dict(response.headers), response.content
    except requests.RequestException:
        raise FetchError('Big Balls network request failed') from None


class Client:
    def __init__(self, store, key, budget=200, max_requests=150, sender=transport,
                 clock=lambda: datetime.now(timezone.utc), sleeper=time.sleep):
        if not key.strip():
            raise FetchError('BBS_API_KEY is missing; configure .env or CI secret')
        if not 1 <= budget <= 500 or not 1 <= max_requests <= budget:
            raise ValueError('Require 1 <= max_requests <= daily_budget <= 500')
        self.store, self.key = store, key
        self.budget, self.max_requests = budget, max_requests
        self.sender, self.clock, self.sleep = sender, clock, sleeper
        self.requests = 0

    def get(self, path, params=None, ttl=86400):
        params = params or {}
        query = path + '?' + urlencode(sorted(params.items()))
        now = self.clock()
        cached = self.store.latest_response(query)
        if cached and 0 <= (now - utc(cached['observed'])).total_seconds() < ttl:
            return decode(cached['payload']), cached['observed'], query
        for attempt in range(3):
            now = self.clock()
            blocked = float(self.store.setting('blocked_until', '0'))
            if now.timestamp() < blocked:
                raise Deferred('Provider retry window active; retry after ' + datetime.fromtimestamp(blocked, timezone.utc).isoformat())
            if self.requests >= self.max_requests:
                raise Deferred('Per-run request budget exhausted')
            last = float(self.store.setting('last_request', '0'))
            self.sleep(max(0, 0.7 - (now.timestamp() - last)))
            now = self.clock()
            self.store.reserve(now, self.budget)
            self.requests += 1
            self.store.set('last_request', now.timestamp())
            try:
                status, headers, body = self.sender(path, params, self.key)
            except FetchError:
                if attempt == 2:
                    raise
                self.sleep(2 ** attempt)
                continue
            headers = {k.lower(): v for k, v in headers.items()}
            delay = 0
            if headers.get('retry-after'):
                try:
                    delay = max(0, float(headers['retry-after']))
                except ValueError:
                    try:
                        delay = max(0, parsedate_to_datetime(headers['retry-after']).timestamp() - now.timestamp())
                    except (ValueError, TypeError):
                        delay = 60
            if status == 429 or delay:
                # Persist long waits instead of keeping the process asleep.
                self.store.set('blocked_until', now.timestamp() + max(delay, 60))
                raise Deferred('Provider requested a retry delay; collection checkpoint saved')
            if headers.get('x-ratelimit-remaining') == '0':
                try:
                    reset = float(headers['x-ratelimit-reset'])
                except (KeyError, ValueError):
                    reset = now.timestamp() + 60
                self.store.set('blocked_until', max(reset, now.timestamp() + 1))
            if 500 <= status <= 599 and attempt < 2:
                self.sleep(2 ** attempt)
                continue
            if status != 200:
                raise FetchError(f'Big Balls HTTP {status} for {path}')
            try:
                payload = decode(body)
                if not isinstance(payload, dict) or 'data' not in payload or payload.get('error'):
                    raise ValueError('Missing data envelope')
                ignored = payload.get('meta', {}).get('ignored_params', [])
                if set(ignored).intersection(params):
                    raise ValueError('Requested filter was ignored')
            except (ValueError, TypeError, AttributeError):
                raise FetchError('Invalid response envelope or ignored filter for ' + path) from None
            observed = self.clock().isoformat()
            self.store.response(query, observed, payload)
            return payload, observed, query
        raise FetchError('Retry limit reached')

    def pages(self, path, params, ttl=86400):
        offset, seen = 0, set()
        for _ in range(100):
            payload, observed, query = self.get(path, {**params, 'limit': 100, 'offset': offset}, ttl)
            rows = payload['data']
            if not isinstance(rows, list) or any(not isinstance(r, dict) for r in rows):
                raise FetchError('Expected a list of objects for ' + path)
            ids = [str(r['id']) if r.get('id') is not None else '' for r in rows]
            if any(not i for i in ids) or len(set(ids)) != len(ids) or seen.intersection(ids):
                raise FetchError('Missing/repeated identifiers while paginating ' + path)
            seen.update(ids)
            yield rows, observed, query, payload.get('meta', {})
            offset += len(rows)
            pagination = payload.get('pagination') or payload.get('meta', {}).get('pagination') or payload.get('meta', {})
            total = pagination.get('total')
            if total is not None:
                if type(total) is not int or total < offset:
                    raise FetchError('Invalid pagination total for ' + path)
                if offset == total:
                    return
                if not rows:
                    raise FetchError('Truncated paginated response for ' + path)
            elif len(rows) < 100:
                return
        raise FetchError('Pagination safety ceiling reached for ' + path)


def normal_match(row, league, observed, meta):
    if row.get('sport') != 'football' or str(row.get('league', '')).lower() not in DISPLAY_NAMES[league]:
        raise ValueError('Wrong sport or competition')
    kickoff = utc(row['kickoff_utc'])
    for side in ('home', 'away'):
        if not isinstance(row.get(side), dict) or not row[side].get('id') or not row[side].get('name'):
            raise ValueError('Missing team identity')
    if row['home']['id'] == row['away']['id']:
        raise ValueError('Same team on both sides')
    from match_scores import valid_goals
    score = valid_goals(row.get('score'))
    if row.get('status') == 'finished' and (score is None or kickoff >= utc(observed)):
        raise ValueError('Invalid completed score or future completed fixture')
    return {**row, 'kickoff_utc': kickoff.isoformat(), 'observed_at_utc': observed,
            'source_updated_at': row.get('updated_at'), 'source_meta': meta,
            'regulation_score_verified': league != 'UCL' and row.get('status') == 'finished'}


def normal_stats(payload, match):
    data = payload['data']
    if not isinstance(data, dict):
        raise ValueError('Statistics must be an object')
    available = payload.get('meta', {}).get('available') is not False
    result = {'available': available, 'source_meta': payload.get('meta', {}),
              'team_ids': {side: str(match[side]['id']) for side in ('home', 'away')}}
    for side in ('home', 'away'):
        values = data.get(side)
        if not available or values is None:
            result[side] = None
            continue
        if not isinstance(values, dict) or str(values.get('team_id')) != str(match[side]['id']):
            raise ValueError('Statistics team does not match fixture side')
        cleaned = {}
        for key in STAT_FIELDS:
            value = values.get(key)
            percent = key in ('ball_possession', 'pass_percentage')
            if value is not None and (isinstance(value, bool) or not isinstance(value, (int, float))
                or not math.isfinite(value) or value < 0 or (percent and value > 100)
                or (not percent and int(value) != value)):
                raise ValueError('Invalid statistic: ' + key)
            cleaned[key] = value
        for part, whole in [('shots_on_target', 'total_shots'), ('accurate_passes', 'total_passes')]:
            if cleaned[part] is not None and cleaned[whole] is not None and cleaned[part] > cleaned[whole]:
                raise ValueError('Inconsistent statistics')
        result[side] = cleaned
    result['available'] = available and any(result[s] is not None for s in ('home', 'away'))
    return result


def collect(client, leagues, seasons, stats_limit=90):
    """Checkpoint pages; incomplete pagination never claims full competition coverage."""
    store = client.store
    report = {'errors': [], 'completed_lists': [], 'statistics_fetched': 0}

    def attempt(label, action):
        try:
            action()
        except Deferred:
            raise
        except (FetchError, ValueError, KeyError, TypeError) as exc:
            report['errors'].append({'scope': label, 'error': str(exc)})

    def list_matches(league, season):
        params = {'sport': 'football', 'league': LEAGUES[league], 'season': season}
        for rows, observed, query, meta in client.pages('/v1/matches', params):
            for row in rows:
                parsed = normal_match(row, league, observed, meta)
                # Requested season is context, never inferred solely from kickoff year.
                parsed['requested_season'] = season
                store.put('match', league, row['id'], observed, parsed, query)
        report['completed_lists'].append(f'matches/{league}/{season}')

    def standings(league, season):
        payload, observed, query = client.get('/v1/standings',
            {'sport': 'football', 'league': LEAGUES[league], 'season': season})
        if not isinstance(payload['data'], dict):
            raise ValueError('Expected standings object')
        groups = payload['data'].get('standings')
        if not isinstance(groups, list):
            raise ValueError('Expected standings groups')
        for group in groups:
            if (not isinstance(group, dict) or group.get('sport') != 'football' or str(group.get('league_name', '')).lower() not in DISPLAY_NAMES[league]
                or str(group.get('season', '')).split('-')[0] != str(season) or not isinstance(group.get('rows'), list)):
                raise ValueError('Wrong standings scope')
        store.put('standings', league, season, observed, payload, query)

    def coverage():
        payload, observed, query = client.get('/v1/coverage', {'sport': 'football'})
        store.put('coverage', 'football', 'coverage', observed, payload, query)

    try:
        attempt('coverage', coverage)
        for season in seasons:
            for league in leagues:
                attempt(f'matches/{league}/{season}', lambda l=league, s=season: list_matches(l, s))
                attempt(f'standings/{league}/{season}', lambda l=league, s=season: standings(l, s))
        # Fair across leagues, unseen/oldest observations first. New data progressively
        # backfills; weekly rechecks capture post-match corrections.
        prior = {(x['league'], x['entity']): x for x in store.latest('statistics', client.clock().isoformat())}
        queue = []
        for league in leagues:
            matches = [x for x in store.latest('match', client.clock().isoformat()) if x['league'] == league and x['payload']['status'] == 'finished']
            matches.sort(key=lambda x: (prior.get((league, x['entity']), {}).get('observed', ''),
                                        -utc(x['payload']['kickoff_utc']).timestamp()))
            queue.append(matches)
        fetched = 0
        while any(queue) and fetched < stats_limit:
            for items in queue:
                if not items or fetched >= stats_limit:
                    continue
                item = items.pop(0)
                def statistics():
                    nonlocal fetched
                    path = '/v1/matches/' + item['entity'] + '/statistics'
                    age = (client.clock() - utc(item['payload']['kickoff_utc'])).total_seconds()
                    ttl = 86400 if age < 7 * 86400 else 7 * 86400
                    payload, observed, query = client.get(path, ttl=ttl)
                    store.put('statistics', item['league'], item['entity'], observed,
                              normal_stats(payload, item['payload']), query)
                    fetched += 1
                    report['statistics_fetched'] = fetched
                attempt('statistics/' + item['entity'], statistics)
        report['statistics_fetched'] = fetched
        for league in leagues:
            for kind, path in [('team', '/v1/teams'), ('player', '/v1/players')]:
                def entities():
                    for rows, observed, query, meta in client.pages(path,
                        {'sport': 'football', 'league': LEAGUES[league]}, ttl=7 * 86400):
                        for row in rows:
                            if row.get('sport') not in (None, 'football'):
                                raise ValueError('Wrong entity sport')
                            store.put(kind, league, row['id'], observed, row, query)
                    report['completed_lists'].append(f'{kind}/{league}')
                attempt(f'{kind}/{league}', entities)
    except Deferred as exc:
        report['deferred'] = str(exc)
    report['requests_this_run'] = client.requests
    report['observed_at_utc'] = client.clock().isoformat()
    report['status'] = 'partial' if report['errors'] or report.get('deferred') else 'complete'
    return report
