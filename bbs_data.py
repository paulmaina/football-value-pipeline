"""Big Balls Free collection: match results and teams, durable observations and replay cutoffs.

No model fitting or forecast mutation. Raw responses never contain request headers. A match
observation is stored only when the match's state changes. The statistics, standings, player and
coverage requests were retired with the statistics adjustment on 25 Nov 2026.
"""
from __future__ import annotations

import json
import hashlib
import os
import tempfile
import time
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path
from urllib.parse import urlencode

import league_registry

BASE_URL = 'https://api.bigballsdata.com'
# Only registry leagues with a BBS slug are collected.
LEAGUES = league_registry.bbs_slugs()
DISPLAY_NAMES = league_registry.bbs_display_names()


# Match fields that change between listings without the match changing: the retrieval time, the provider's
# per-request metadata, broadcaster and odds flags, and team logo URLs. Nothing downstream reads them.
VOLATILE_MATCH_FIELDS = ('observed_at_utc', 'source_meta', 'has_odds', 'broadcast')
VOLATILE_TEAM_FIELDS = ('logo_url',)


def match_state(payload):
    """A normalized match's state: everything except the volatile fields, as canonical JSON.

    A new match observation is stored only when this changes (and once after a quarantine), so the latest
    observation at any cutoff carries the same state as it would if every listing had been stored.
    """
    state = {k: v for k, v in payload.items() if k not in VOLATILE_MATCH_FIELDS}
    for side in ('home', 'away'):
        if isinstance(state.get(side), dict):
            state[side] = {k: v for k, v in state[side].items() if k not in VOLATILE_TEAM_FIELDS}
    return dumps(state)


def match_observation_needed(previous, payload, quarantined_at=None):
    """Store a listing only if its state differs from the entity's latest stored observation, or if a
    quarantine at or after that observation would otherwise keep holding the match."""
    if previous is None:
        return True
    if quarantined_at is not None and utc(quarantined_at) >= utc(previous['observed']):
        return True
    return match_state(previous['payload']) != match_state(payload)


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


def atomic_json(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile('w', dir=path.parent, delete=False, encoding='utf-8') as f:
        f.write(dumps(value) + '\n')
        temporary = Path(f.name)
    try:
        os.replace(temporary, path)
    finally:
        temporary.unlink(missing_ok=True)


class Store:
    """File-backed observations; caller holds the collection lock while writing.

    Each observation is an immutable timestamped JSON snapshot. Request counts
    are persisted before network I/O for telemetry; defaults impose no local quota.
    Malformed checkpoints fail closed.
    """
    def __init__(self, path):
        self.path = Path(path)
        if self.path.is_file():
            raise ValueError('Store must be a directory; SQLite stores are not supported')
        self.path.mkdir(parents=True, exist_ok=True)
        checkpoint = self.path / 'checkpoint.json'
        self.state = decode(checkpoint.read_text()) if checkpoint.exists() else {
            'version': 1, 'quota': {}, 'settings': {}}
        if (self.state.get('version') != 1 or not isinstance(self.state.get('quota'), dict)
                or not isinstance(self.state.get('settings'), dict)):
            raise ValueError('Invalid collection checkpoint')
        self.observations = []
        for file in sorted((self.path / 'observations').glob('*/*.json')):
            row = decode(file.read_text())
            utc(row['observed'])
            self.observations.append(row)

    def close(self):
        pass  # Every write is persisted immediately, including interrupted runs.

    def setting(self, name, default=''):
        return self.state['settings'].get(name, default)

    def set(self, name, value):
        self.state['settings'][name] = str(value)
        atomic_json(self.path / 'checkpoint.json', self.state)

    def response_path(self, query):
        return self.path / 'responses' / (hashlib.sha256(query.encode()).hexdigest() + '.json')

    def latest_response(self, query):
        path = self.response_path(query)
        return decode(path.read_text()) if path.exists() else None

    def response(self, query, observed, payload):
        atomic_json(self.response_path(query), {
            'query': query, 'observed': observed, 'payload': dumps(payload)})

    def put(self, kind, league, entity, observed, payload, query=''):
        observed = utc(observed).isoformat()
        row = dict(kind=kind, league=league, entity=str(entity), observed=observed,
                   payload=payload, query=query)
        digest = hashlib.sha256(dumps(row).encode()).hexdigest()
        stamp = utc(observed).strftime('%Y%m%dT%H%M%S%fZ')
        path = self.path / 'observations' / kind / (stamp + '_' + digest + '.json')
        if not path.exists():
            atomic_json(path, row)
            self.observations.append(row)

    def latest(self, kind, cutoff=None):
        cutoff = utc(cutoff or datetime.now(timezone.utc).isoformat())
        result = {}
        for row in sorted(self.observations, key=lambda r: utc(r['observed'])):
            if row['kind'] == kind and utc(row['observed']) <= cutoff:
                key = (row['league'], row['entity'])
                if key in result and result[key]['observed'] == row['observed'] and result[key]['payload'] != row['payload']:
                    raise ValueError('Conflicting observations at identical timestamp')
                result[key] = row
        return list(result.values())

    def reserve(self, now, limit=None):
        day = now.astimezone(timezone.utc).date().isoformat()
        used = self.state['quota'].get(day, 0)
        if type(used) is not int or used < 0:
            raise ValueError('Invalid request checkpoint')
        if limit is not None and used >= limit:
            raise Deferred('Local daily request budget exhausted')
        self.state['quota'][day] = used + 1
        atomic_json(self.path / 'checkpoint.json', self.state)


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
    def __init__(self, store, key, budget=None, max_requests=None, sender=transport,
                 clock=lambda: datetime.now(timezone.utc), sleeper=time.sleep):
        if not key.strip():
            raise FetchError('BBS_API_KEY is missing; configure .env or CI secret')
        if any(value is not None and (type(value) is not int or value < 1)
               for value in (budget, max_requests)):
            raise ValueError('Explicit request limits must be positive integers')
        self.store, self.key = store, key
        self.budget, self.max_requests = budget, max_requests
        self.sender, self.clock, self.sleep = sender, clock, sleeper
        self.requests = 0

    def get(self, path, params=None, ttl=86400):
        params = params or {}
        query = path + '?' + urlencode(sorted(params.items()))
        now = self.clock()
        denied_key = 'denied:' + hashlib.sha256(query.encode()).hexdigest()
        if now.timestamp() < float(self.store.setting(denied_key, '0')):
            raise FetchError('Endpoint access was refused; retry after entitlement-cache expiry')
        cached = self.store.latest_response(query)
        if cached and 0 <= (now - utc(cached['observed'])).total_seconds() < ttl:
            return decode(cached['payload']), cached['observed'], query
        for attempt in range(3):
            now = self.clock()
            blocked = float(self.store.setting('blocked_until', '0'))
            if now.timestamp() < blocked:
                raise Deferred('Provider retry window active; retry after ' + datetime.fromtimestamp(blocked, timezone.utc).isoformat())
            if self.max_requests is not None and self.requests >= self.max_requests:
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
            if status == 403:
                self.store.set(denied_key, now.timestamp() + 86400)
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

    def pages(self, path, params, ttl=86400, page_size=200):
        offset, seen = 0, set()
        for _ in range(100):
            payload, observed, query = self.get(path, {**params, 'limit': page_size, 'offset': offset}, ttl)
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
            elif len(rows) < page_size:
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


def collect(client, leagues, seasons):
    """Checkpoint pages; incomplete pagination never claims full competition coverage."""
    store = client.store
    report = {'errors': [], 'completed_lists': [], 'match_observations_stored': 0, 'match_listings_unchanged': 0}
    clock = client.clock().isoformat()
    latest_match = {(x['league'], x['entity']): x for x in store.latest('match', clock)}
    latest_quarantine = {(x['league'], x['entity']): x['observed'] for x in store.latest('quarantine', clock)}

    def eligible_matches():
        latest = store.latest('match', client.clock().isoformat())
        rejected = {(x['league'], x['entity']): utc(x['observed'])
                    for x in store.latest('quarantine', client.clock().isoformat())}
        return [x for x in latest if x['league'] in leagues
                and x['payload'].get('requested_season') in seasons
                and ((x['league'], x['entity']) not in rejected
                     or rejected[(x['league'], x['entity'])] < utc(x['observed']))]

    def attempt(label, action):
        try:
            action()
        except Deferred:
            raise
        except (FetchError, ValueError, KeyError, TypeError) as exc:
            report['errors'].append({'scope': label, 'error': str(exc)})

    def list_matches(league, season, status):
        params = {'sport': 'football', 'league': LEAGUES[league], 'season': season, 'status': status}
        for rows, observed, query, meta in client.pages('/v1/matches', params, ttl=(7 * 86400 if season < max(seasons) else (86400 if status in ('postponed', 'cancelled') else 6 * 3600))):
            for row in rows:
                key = (league, str(row.get('id')))
                try:
                    if row.get('status') != status:
                        raise ValueError('Requested match status was not honored')
                    parsed = normal_match(row, league, observed, meta)
                    if not (datetime(season, 7, 1, tzinfo=timezone.utc) <= utc(parsed['kickoff_utc']) < datetime(season+1, 7, 1, tzinfo=timezone.utc)):
                        raise ValueError('Requested season was not honored')
                    parsed['requested_season'] = season
                    if not match_observation_needed(latest_match.get(key), parsed, latest_quarantine.get(key)):
                        report['match_listings_unchanged'] += 1
                        continue
                    store.put('match', league, row['id'], observed, parsed, query)
                    latest_match[key] = {'league': league, 'entity': key[1], 'observed': utc(observed).isoformat(),
                                         'payload': parsed}
                    report['match_observations_stored'] += 1
                except (ValueError, KeyError, TypeError) as exc:
                    rejection = {'bbs_match_id': row.get('id'), 'league': league, 'season': season,
                                 'reason': str(exc), 'row': row}
                    store.put('quarantine', league, row['id'], observed, rejection, query)
                    latest_quarantine[key] = utc(observed).isoformat()
                    report['errors'].append({'scope': f'match/{league}/{row["id"]}', 'error': str(exc)})
        report['completed_lists'].append(f'matches/{league}/{season}/{status}')

    try:
        for season in seasons:
            for league in leagues:
                attempt(f'matches/{league}/{season}/finished', lambda l=league, s=season: list_matches(l, s, 'finished'))
                if season == max(seasons):
                    attempt(f'matches/{league}/{season}/scheduled', lambda l=league, s=season: list_matches(l, s, 'scheduled'))
                    for status in ('postponed', 'cancelled'):
                        attempt(f'matches/{league}/{season}/{status}', lambda l=league, s=season, st=status: list_matches(l, s, st))
        # Teams give mapping names when a club's ID differs between surfaces.
        for league in leagues:
            def entities():
                for rows, observed, query, meta in client.pages('/v1/teams',
                    {'sport': 'football', 'league': LEAGUES[league]}, ttl=7 * 86400):
                    for row in rows:
                        if row.get('sport') not in (None, 'football'):
                            raise ValueError('Wrong entity sport')
                        store.put('team', league, row['id'], observed, row, query)
                report['completed_lists'].append(f'team/{league}')
            attempt(f'team/{league}', entities)
    except Deferred as exc:
        report['deferred'] = str(exc)
    report['coverage'] = {}
    for league in leagues:
        matches = [x for x in eligible_matches() if x['league'] == league]
        finished = [x for x in matches if x['payload']['status'] == 'finished']
        report['coverage'][league] = dict(completed_matches=len(finished),
            team_records=sum(x['league'] == league for x in store.latest('team', client.clock().isoformat())),
            scheduled_matches=sum(x['payload']['status'] == 'scheduled' for x in matches))
        if not finished:
            report['errors'].append({'scope': league, 'error': 'No completed results collected; training coverage unverified'})
    report['quarantined_records'] = [dict(league=x['league'], bbs_match_id=x['entity'], reason=x['payload']['reason'])
        for x in store.latest('quarantine', client.clock().isoformat())
        if x['league'] in leagues and not any(m['league']==x['league'] and m['entity']==x['entity'] and utc(m['observed']) > utc(x['observed']) for m in store.latest('match', client.clock().isoformat()))]
    report['requests_used_today'] = store.state['quota'].get(client.clock().astimezone(timezone.utc).date().isoformat(), 0)
    report['daily_budget'] = client.budget
    report['request_limit_policy'] = 'PROVIDER_ALLOWANCE' if client.budget is None and client.max_requests is None else 'EXPLICIT_LOCAL_LIMIT'
    report['requests_this_run'] = client.requests
    report['observed_at_utc'] = client.clock().isoformat()
    report['status'] = 'partial' if report['errors'] or report.get('deferred') or report['quarantined_records'] else 'complete'
    return report
