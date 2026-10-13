"""Validate and atomically refresh UCL history without fitting models or odds calls."""
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import tempfile
from match_scores import regulation_goals

URL = 'https://api.football-data.org/v4/competitions/CL/matches'
STATUS = Path('docs/ucl_training_refresh_status.json')


def utc(value):
    try:
        date = datetime.fromisoformat(str(value).replace('Z', '+00:00'))
        return date.astimezone(timezone.utc) if date.tzinfo else None
    except (ValueError, TypeError):
        return None


def inspect_payload(payload, year, clock):
    if not isinstance(payload, dict) or payload.get('competition', {}).get('code') != 'CL':
        raise ValueError('Expected Champions League competition payload')
    matches = payload.get('matches')
    if not isinstance(matches, list):
        raise ValueError('Missing season matches')
    finished = {}; seen = set(); unresolved = []; upcoming = []
    for match in matches:
        if not isinstance(match, dict) or type(match.get('id')) is not int or match['id'] in seen:
            raise ValueError('Missing or duplicate match ID')
        seen.add(match['id'])
        date = utc(match.get('utcDate'))
        season = match.get('season', {})
        if (date is None or not str(season.get('startDate', '')).startswith(str(year))
                or not datetime(year,7,1,tzinfo=timezone.utc) <= date < datetime(year+1,7,1,tzinfo=timezone.utc)):
            raise ValueError('Invalid match date or wrong season')
        home, away = match.get('homeTeam', {}), match.get('awayTeam', {})
        if not home.get('name') or not away.get('name') or home.get('name') == away.get('name'):
            raise ValueError('Invalid team identities')
        state = match.get('status')
        if state == 'FINISHED':
            goals = regulation_goals(match.get('score', {}))
            if date >= clock or goals is None:
                raise ValueError('Future finished match or unavailable regulation score')
            finished[match['id']] = {'kickoff_utc': date.isoformat(), 'goals': list(goals),
                                     'home': home['name'], 'away': away['name']}
        elif state in ('SCHEDULED', 'TIMED', 'IN_PLAY', 'PAUSED'):
            if (clock-date).total_seconds() > 6*3600:
                unresolved.append(match['id'])
            if date > clock:
                upcoming.append(date.isoformat())
        elif state not in ('POSTPONED', 'CANCELLED', 'SUSPENDED', 'AWARDED'):
            raise ValueError('Unknown match status')
    count = payload.get('resultSet', {}).get('count')
    if count is not None and count != len(matches):
        raise ValueError('Season response count mismatch')
    latest = max((v['kickoff_utc'] for v in finished.values()), default=None)
    return {'completed_matches': len(finished), 'latest_completed_utc': latest,
            'latest_completed_date': latest[:10] if latest else None,
            'next_fixture_utc': min(upcoming, default=None),
            'overdue_unfinished_match_ids': unresolved, 'matches': finished,
            'source_schedule_matches': len(matches)}


def atomic_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(dir=path.parent, delete=False) as handle:
        temporary = Path(handle.name)
        handle.write((json.dumps(data, ensure_ascii=False, indent=2)+'\n').encode())
    try:
        os.replace(temporary, path)
    finally:
        temporary.unlink(missing_ok=True)


def apply_payload(repo, payload, year, clock, cache_dir=None):
    repo = Path(repo)
    path = (Path(cache_dir) if cache_dir is not None else repo/'.football_cache')/f'fdorg_history_UCL_{year}.json'
    checked = inspect_payload(payload, year, clock)
    old = inspect_payload(json.loads(path.read_text()), year, clock) if path.exists() else {'matches': {}}
    if not set(old['matches']).issubset(checked['matches']):
        raise ValueError('Refusing UCL refresh that removes completed matches')
    if any(checked['matches'][k]['home'] != v['home'] or checked['matches'][k]['away'] != v['away']
           or checked['matches'][k]['kickoff_utc'] != v['kickoff_utc'] for k, v in old['matches'].items()):
        raise ValueError('Previously finished UCL fixture identity changed')
    added = len(set(checked['matches'])-set(old['matches']))
    corrected = sum(checked['matches'][k]['goals'] != v['goals'] for k,v in old['matches'].items())
    atomic_json(path, payload)
    metadata = {k:v for k,v in checked.items() if k != 'matches'}
    metadata.update(provider='football-data.org', season_start=year, checked_at_utc=clock.isoformat(),
        download_status='VERIFIED_LIVE', added_matches=added, corrected_scores=corrected,
        sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
        coverage_status='PROVIDER_OVERDUE_RESULTS' if checked['overdue_unfinished_match_ids'] else 'CURRENT_WITHIN_PROVIDER_SCHEDULE',
        note='Provider schedule comparison is not independent proof of complete coverage.')
    atomic_json(path.with_suffix('.meta.json'), metadata)
    atomic_json(repo/STATUS, metadata)
    return metadata


def fetch_payload(token, year, session=None):
    if not token.strip():
        raise ValueError('FOOTBALL_DATA_API_KEY is required for UCL refresh')
    import requests
    session = session or requests.Session()
    response = session.get(URL, params={'season': year}, headers={'X-Auth-Token': token}, timeout=30)
    response.raise_for_status()
    return response.json()


def health(repo, training_end, clock, cache_dir=None):
    repo = Path(repo); year = clock.year if clock.month >= 7 else clock.year-1
    path = (Path(cache_dir) if cache_dir is not None else repo/'.football_cache')/f'fdorg_history_UCL_{year}.json'
    meta_path = path.with_suffix('.meta.json')
    meta = json.loads(meta_path.read_text()) if meta_path.exists() else {}
    checked = utc(meta.get('checked_at_utc'))
    bound = path.exists() and meta.get('sha256') == hashlib.sha256(path.read_bytes()).hexdigest()
    age = (clock-checked).total_seconds()/3600 if checked else None
    status = 'DOWNLOAD_NOT_VERIFIED'
    if bound and age is not None and -5/60 <= age <= 8:
        status = meta.get('coverage_status', 'DOWNLOAD_NOT_VERIFIED')
        if meta.get('latest_completed_date') and (not training_end or str(training_end)[:10] < meta['latest_completed_date']):
            status = 'MODEL_BEHIND_VERIFIED_SOURCE'
    elif bound:
        status = 'REFRESH_OVERDUE'
    return {**meta, 'status': status, 'download_age_hours': age,
            'training_end': training_end, 'cache_hash_verified': bound}
