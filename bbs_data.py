"""Big Balls Free collection: bounded requests, durable observations and replay cutoffs.

No model fitting or forecast mutation. Raw responses never contain request headers.
"""
from __future__ import annotations

import json
import math
import hashlib
import os
import tempfile
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

    Each observation is an immutable timestamped JSON snapshot. Request budgets
    are persisted before network I/O. Malformed checkpoints fail closed.
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

    def reserve(self, now, limit):
        day = now.astimezone(timezone.utc).date().isoformat()
        used = self.state['quota'].get(day, 0)
        if type(used) is not int or used < 0:
            raise ValueError('Invalid request checkpoint')
        if used >= limit:
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
    def __init__(self, store, key, budget=500, max_requests=500, sender=transport,
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


def normal_stats(payload, match):
    data = payload['data']
    if not isinstance(data, dict):
        raise ValueError('Statistics must be an object')
    available = payload.get('meta', {}).get('available') is not False
    result = {'available': available, 'source_meta': payload.get('meta', {}),
              'team_ids': {side: str(match[side]['id']) for side in ('home', 'away')},
              'identity_resolution': {}, 'provider_team_ids': {}}
    from football_value_pipeline_v2_standalone import canonical_team_key
    league = match.get('league_key') or next((key for key, names in DISPLAY_NAMES.items()
        if str(match.get('league', '')).lower() in names), None)
    aliases = decode(Path(__file__).with_name('bbs_team_aliases.json').read_text(encoding='utf-8')).get(league, {})
    def identity(name):
        return canonical_team_key(aliases.get(name, name)) if isinstance(name, str) and name.strip() else None
    for side in ('home', 'away'):
        values = data.get(side)
        if not available or values is None:
            result[side] = None
            continue
        if not isinstance(values, dict):
            raise ValueError('Statistics team does not match fixture side')
        provider_id = values.get('team_id')
        result['provider_team_ids'][side] = provider_id
        if provider_id not in (None, ''):
            if str(provider_id) != str(match[side]['id']):
                raise ValueError('Statistics team does not match fixture side')
            if values.get('team_name') not in (None, '') and identity(values['team_name']) != identity(match[side]['name']):
                raise ValueError('Statistics team name contradicts fixture side')
            result['identity_resolution'][side] = 'provider_id'
        else:
            expected = identity(match[side]['name'])
            other = identity(match['away' if side == 'home' else 'home']['name'])
            if not expected or expected == other or identity(values.get('team_name')) != expected:
                raise ValueError('Missing statistics ID has no verified matching team name')
            result['identity_resolution'][side] = 'verified_name'
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
        result[side] = cleaned if any(v is not None for v in cleaned.values()) else None
    result['available'] = available and any(result[s] is not None for s in ('home', 'away'))
    return result


def collect(client, leagues, seasons, stats_limit=500):
    """Checkpoint pages; incomplete pagination never claims full competition coverage."""
    store = client.store
    report = {'errors': [], 'completed_lists': [], 'statistics_fetched': 0}
    rejected_stats = {(q['league'], q['entity']): q
                      for q in store.latest('statistics_quarantine', client.clock().isoformat())}

    def eligible_matches():
        latest = store.latest('match', client.clock().isoformat())
        rejected = {(x['league'], x['entity']): utc(x['observed'])
                    for x in store.latest('quarantine', client.clock().isoformat())}
        return [x for x in latest if x['league'] in leagues
                and x['payload'].get('requested_season') in seasons
                and ((x['league'], x['entity']) not in rejected
                     or rejected[(x['league'], x['entity'])] < utc(x['observed']))]

    def statistics_ttl(item):
        age = (client.clock() - utc(item['payload']['kickoff_utc'])).total_seconds()
        return 6 * 3600 if age < 2 * 86400 else (86400 if age < 7 * 86400 else 7 * 86400)

    def statistics_due(item, previous):
        rejected = rejected_stats.get((item['league'], item['entity']))
        return (previous is None or
            (rejected is not None and utc(rejected['observed']) >= utc(previous['observed'])) or
            (client.clock() - utc(previous['observed'])).total_seconds() >= statistics_ttl(item) or
            previous['payload'].get('team_ids') != {side: str(item['payload'][side]['id']) for side in ('home', 'away')})

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
                try:
                    if row.get('status') != status:
                        raise ValueError('Requested match status was not honored')
                    parsed = normal_match(row, league, observed, meta)
                    if not (datetime(season, 7, 1, tzinfo=timezone.utc) <= utc(parsed['kickoff_utc']) < datetime(season+1, 7, 1, tzinfo=timezone.utc)):
                        raise ValueError('Requested season was not honored')
                    parsed['requested_season'] = season
                    store.put('match', league, row['id'], observed, parsed, query)
                except (ValueError, KeyError, TypeError) as exc:
                    rejection = {'bbs_match_id': row.get('id'), 'league': league, 'season': season,
                                 'reason': str(exc), 'row': row}
                    store.put('quarantine', league, row['id'], observed, rejection, query)
                    report['errors'].append({'scope': f'match/{league}/{row["id"]}', 'error': str(exc)})
        report['completed_lists'].append(f'matches/{league}/{season}/{status}')

    def standings(league, season):
        previous = next((x for x in store.latest('standings', client.clock().isoformat()) if x['league'] == league and x['entity'] == str(season)), None)
        latest_kickoff = max((utc(x['payload']['kickoff_utc']) for x in store.latest('match', client.clock().isoformat()) if x['league'] == league and x['payload']['status'] == 'finished'), default=None)
        ttl = 0 if previous and latest_kickoff and latest_kickoff > utc(previous['observed']) else 6 * 3600
        payload, observed, query = client.get('/v1/standings',
            {'sport': 'football', 'league': LEAGUES[league], 'season': season}, ttl=ttl)
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
                attempt(f'matches/{league}/{season}/finished', lambda l=league, s=season: list_matches(l, s, 'finished'))
                if season == max(seasons):
                    attempt(f'matches/{league}/{season}/scheduled', lambda l=league, s=season: list_matches(l, s, 'scheduled'))
                    for status in ('postponed', 'cancelled'):
                        attempt(f'matches/{league}/{season}/{status}', lambda l=league, s=season, st=status: list_matches(l, s, st))
                    attempt(f'standings/{league}/{season}', lambda l=league, s=season: standings(l, s))
        # Fair across leagues, unseen/oldest observations first. New data progressively
        # backfills; weekly rechecks capture post-match corrections.
        prior = {(x['league'], x['entity']): x for x in store.latest('statistics', client.clock().isoformat())}
        queue = []
        for league in leagues:
            matches = [x for x in eligible_matches() if x['league'] == league and x['payload']['status'] == 'finished']
            matches = [x for x in matches if statistics_due(x, prior.get((league, x['entity'])))]
            matches.sort(key=lambda x: (int(x['payload']['requested_season']) < max(seasons), (client.clock() - utc(x['payload']['kickoff_utc'])).total_seconds() >= 2 * 86400, prior.get((league, x['entity']), {}).get('observed', ''),
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
                    ttl = statistics_ttl(item)
                    previous = prior.get((item['league'], item['entity']))
                    if previous and previous['payload'].get('team_ids') != {side: str(item['payload'][side]['id']) for side in ('home', 'away')}:
                        ttl = 0
                    rejected = rejected_stats.get((item['league'], item['entity']))
                    if previous and rejected and utc(rejected['observed']) >= utc(previous['observed']):
                        ttl = 0
                    payload, observed, query = client.get(path, ttl=ttl)
                    try:
                        normalized = normal_stats(payload, item['payload'])
                    except (ValueError, KeyError, TypeError) as exc:
                        store.put('statistics_quarantine', item['league'], item['entity'], observed,
                                  {'reason': str(exc)}, query)
                        rejected_stats[(item['league'], item['entity'])] = {'observed': observed}
                        raise
                    store.put('statistics', item['league'], item['entity'], observed, normalized, query)
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
    report['coverage'] = {}
    for league in leagues:
        matches = [x for x in eligible_matches() if x['league'] == league]
        finished = [x for x in matches if x['payload']['status'] == 'finished']
        statistics = {x['entity']: x for x in store.latest('statistics', client.clock().isoformat()) if x['league'] == league}
        rejected = {entity for (scope, entity), q in rejected_stats.items()
                    if scope == league and (entity not in statistics
                    or utc(q['observed']) >= utc(statistics[entity]['observed']))}
        held = sum(x['entity'] in rejected and x['entity'] in statistics for x in finished)
        missing = sum(x['entity'] not in statistics for x in finished)
        unavailable = sum(not statistics[x['entity']]['payload']['available'] for x in finished
                          if x['entity'] in statistics and x['entity'] not in rejected)
        stale = sum(statistics_due(x, statistics[x['entity']]) for x in finished if x['entity'] in statistics)
        report['coverage'][league] = dict(completed_matches=len(finished), statistics_stale=stale,
            team_records=sum(x['league'] == league for x in store.latest('team', client.clock().isoformat())),
            player_records=sum(x['league'] == league for x in store.latest('player', client.clock().isoformat())),
            scheduled_matches=sum(x['payload']['status'] == 'scheduled' for x in matches),
            statistics_missing=missing, statistics_unavailable=unavailable, statistics_quarantined=held,
            statistics_available=len(finished)-missing-unavailable-held)
        if not finished:
            report['errors'].append({'scope': league, 'error': 'No completed results collected; training coverage unverified'})
        if missing or unavailable or stale or held:
            report['errors'].append({'scope': league, 'error': f'Statistics incomplete: {missing} unfetched, {unavailable} unavailable, {stale} stale, {held} quarantined'})
    report['quarantined_records'] = [dict(league=x['league'], bbs_match_id=x['entity'], reason=x['payload']['reason'])
        for x in store.latest('quarantine', client.clock().isoformat())
        if x['league'] in leagues and not any(m['league']==x['league'] and m['entity']==x['entity'] and utc(m['observed']) > utc(x['observed']) for m in store.latest('match', client.clock().isoformat()))]
    report['requests_used_today'] = store.state['quota'].get(client.clock().astimezone(timezone.utc).date().isoformat(), 0)
    report['daily_budget'] = client.budget
    report['requests_this_run'] = client.requests
    report['observed_at_utc'] = client.clock().isoformat()
    report['status'] = 'partial' if report['errors'] or report.get('deferred') or report['quarantined_records'] else 'complete'
    return report
