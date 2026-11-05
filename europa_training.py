"""Verified regulation-time Europa cache, with reproducible source downloads.

Raw provider extracts stay local. A single atomic snapshot binds records,
provenance and refresh time; failed reconciliation never replaces that snapshot.
"""
from datetime import datetime, timedelta, timezone
import hashlib
import json
from pathlib import Path
import os
import math
import re
import tempfile
import warnings

import pandas as pd
import requests

from scripts.europa_research import (audit_cornerflick, identity, reconcile,
                                    require_unique, team_resolver)

ROOT = Path(__file__).resolve().parent
MAX_FALLBACK_AGE = timedelta(days=10)


def resolver():
    return team_resolver(json.loads((ROOT/'docs/audits/europa-team-aliases.json').read_text(encoding='utf-8')))


def refresh(cache_dir, now=None, *, download=True, session=None):
    now = now or datetime.now(timezone.utc)
    directory = Path(cache_dir)/'europa'
    sources = directory/'sources'
    sources.mkdir(parents=True, exist_ok=True)
    urls = {f'fixture-{y}.csv': f'https://fixturedownload.com/download/europa-league-{y}-UTC.csv'
            for y in range(2022, 2027)}
    urls.update({f'openfootball-{y}.txt': f'https://raw.githubusercontent.com/openfootball/champions-league/master/{y}-{str(y+1)[-2:]}/el.txt'
                 for y in (2022, 2023, 2024)})
    urls['cornerflick.json'] = 'https://cornerflick.com/football/leagues/europa-league/results/season.json'
    attestation_bytes = (ROOT/'docs/audits/europa-uefa-attestations.json').read_bytes()
    (sources/'uefa-reviewed-facts.json').write_bytes(attestation_bytes)
    # Retain immutable historical period evidence; no live UEFA request or
    # current-season UEFA corroboration is required.
    attestation = json.loads(attestation_bytes)['seasons']['2025']
    official_health = {'2025': {'status': 'REVIEWED_HISTORICAL_FACTS',
        'recorded_at_utc': attestation['recorded_at_utc'],
        'original_source_sha256': attestation['source_sha256']}}
    if download:
        client = session or requests.Session()
        # Completed seasons are immutable inputs; refresh the current season only.
        for name, url in urls.items():
            target = sources/name
            if target.exists() and name not in ('fixture-2026.csv', 'cornerflick.json'):
                continue
            response = client.get(url, timeout=40)
            response.raise_for_status()
            target.write_bytes(response.content)
    aliases = json.loads((ROOT/'docs/audits/europa-team-aliases.json').read_text(encoding='utf-8'))
    reviews = json.loads((ROOT/'docs/audits/europa-regulation-reviews.json').read_text(encoding='utf-8'))
    history, evidence = reconcile(sources, aliases, reviews, official_rows=attestation['matches'])
    audit, current = audit_cornerflick(sources, team_resolver(aliases), now)
    if not audit['verified_for_research']:
        raise ValueError('Current Europa sources disagree or coverage is incomplete; prior snapshot retained; '+
                         json.dumps(audit, sort_keys=True))
    history += [{**r, 'regulation': r['reported'], 'season': 2026,
                 'duration': 'REGULAR', 'stage': 'League phase',
                 'source': 'Cornerflick + Fixture Download'} for r in current]
    require_unique(history)
    history.sort(key=identity)
    payload = {'schema_version': 1, 'score_basis': 'REGULATION_90_MINUTES',
               'verified_at_utc': now.isoformat(), 'matches': history,
               'evidence': evidence, 'current_audit': audit,
               'sources': urls, 'official_source_health': official_health,
               'attribution': 'Data by Cornerflick — cornerflick.com; OpenFootball; Fixture Download; UEFA',
               'source_sha256': {name: hashlib.sha256((sources/name).read_bytes()).hexdigest() for name in (*urls, 'uefa-reviewed-facts.json') if (sources/name).exists()}}
    # Validate before publication, including future dates and duplicate identities.
    frame(payload, now)
    fd, temporary = tempfile.mkstemp(prefix='.snapshot-', dir=directory)
    try:
        with os.fdopen(fd, 'w') as stream:
            json.dump(payload, stream, indent=2)
            stream.write('\n')
        os.replace(temporary, directory/'training.json')
    finally:
        if os.path.exists(temporary): os.unlink(temporary)
    return payload


def frame(payload, now):
    if not isinstance(payload, dict) or payload.get('schema_version') != 1 or payload.get('score_basis') != 'REGULATION_90_MINUTES':
        raise ValueError('Unrecognized Europa score basis/schema')
    rows = payload['matches']
    if not isinstance(rows, list) or any(not isinstance(row, dict) or
            not {'date', 'home', 'away', 'regulation', 'season'} <= row.keys() for row in rows):
        raise ValueError('Invalid Europa training rows')
    require_unique(rows)
    result = []
    for row in rows:
        if (any(not isinstance(row[k], str) or not row[k].strip() for k in ('home', 'away'))
                or row['home'].strip().casefold() == row['away'].strip().casefold()):
            raise ValueError('Invalid Europa team identities')
        stamp = pd.Timestamp(row['date'])
        score = row['regulation']
        if pd.isna(stamp) or stamp.tzinfo is not None or stamp.date() > now.date():
            raise ValueError('Invalid or future Europa training date')
        if len(score) != 2 or any(type(g) is not int or not 0 <= g <= 30 for g in score):
            raise ValueError('Invalid Europa regulation score')
        result.append({'Date': stamp, 'HomeTeam': row['home'], 'AwayTeam': row['away'],
                       'FTHG': score[0], 'FTAG': score[1], 'Season': str(row['season'])})
    if len(result) < 30: raise ValueError('Insufficient verified Europa history')
    return pd.DataFrame(result).sort_values('Date').reset_index(drop=True)


def load(cache_dir, now=None, *, refresh_if_stale=True, force_refresh=False):
    now = now or datetime.now(timezone.utc)
    path = Path(cache_dir)/'europa/training.json'
    payload = None
    cached = None
    if path.exists():
        try:
            payload = json.loads(path.read_text(encoding='utf-8'))
            stamp = datetime.fromisoformat(payload['verified_at_utc'])
            if stamp.tzinfo is None or stamp > now:
                raise ValueError('Europa verification time missing or after evaluation')
            cached = frame(payload, now)
        except (ValueError, KeyError, TypeError):
            # Invalid cache is never a fallback. A successful refresh may repair it.
            payload = None
    refresh_error = None
    if force_refresh or (refresh_if_stale and (payload is None or not fresh(payload, now))):
        try:
            payload = refresh(cache_dir, now)
        except (ValueError, OSError, requests.RequestException) as exc:
            if cached is None or now-stamp > MAX_FALLBACK_AGE:
                raise
            refresh_error = type(exc).__name__ + (': ' + str(exc).splitlines()[0][:200] if isinstance(exc, ValueError) else '')
            warnings.warn('Europa live refresh failed; using last verified local training snapshot: ' + refresh_error,
                          RuntimeWarning)
    if payload is None: raise ValueError('Europa cache missing: run refresh_europa_training.py')
    verified = datetime.fromisoformat(payload['verified_at_utc'])
    if verified.tzinfo is None or verified > now:
        raise ValueError('Europa verification time missing or after evaluation')
    result = frame(payload, now)
    result.attrs['training_seasons_requested'] = len({r['season'] for r in payload['matches']})
    result.attrs['training_cache_status'] = ('LIVE_REFRESH_FAILED_USING_VERIFIED_CACHE' if refresh_error else
        'VERIFIED_WITHIN_24_HOURS' if fresh(payload, now) else 'VERIFIED_CACHED_HISTORY')
    result.attrs['training_verified_at_utc'] = payload['verified_at_utc']
    result.attrs['training_refresh_warning'] = refresh_error
    return result


def fresh(payload, now):
    stamp = datetime.fromisoformat(payload['verified_at_utc'])
    return stamp.tzinfo is not None and 0 <= (now-stamp).total_seconds() <= 86400


def eligibility(row):
    if row.get('league') != 'UEFA Europa League': return []
    try:
        counts = [float(row.get(s+'_training_matches', 0)) for s in ('home', 'away')]
        if all(math.isfinite(n) and n >= 6 for n in counts):
            return []
    except (TypeError, ValueError): pass
    return ['Europa team has fewer than six verified prior appearances']


def main():
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--cache-dir', type=Path, default=Path('.football_cache'))
    args = parser.parse_args()
    payload = refresh(args.cache_dir)
    print(f"Verified {len(payload['matches'])} Europa matches in {args.cache_dir}/europa/training.json")


if __name__ == '__main__': main()


def fixtures(cache_dir, now, lookahead_days):
    """UTC schedule fallback; quotes still require an independent live event link."""
    import csv
    resolve = resolver()
    rows = []
    path = Path(cache_dir)/'europa/sources/fixture-2026.csv'
    if not path.exists(): return pd.DataFrame()
    for row in csv.DictReader(path.read_text(encoding='utf-8-sig').splitlines()):
        stamp = pd.Timestamp(datetime.strptime(row['Date'], '%d/%m/%Y %H:%M'), tz='UTC')
        if now <= stamp.to_pydatetime() <= now + pd.Timedelta(days=lookahead_days) and not row['Result'].strip():
            rows.append({'Div': '', 'Date': stamp.tz_convert(None), 'kickoff_utc': stamp.isoformat(),
                         'HomeTeam': resolve(row['Home Team']), 'AwayTeam': resolve(row['Away Team']),
                         'fixture_id': 'uel-fd-'+row['Match Number'], 'fixture_source': 'Fixture Download UTC'})
    return pd.DataFrame(rows)


def results(cache_dir, now):
    """Return current league-phase 90-minute results corroborated by both sources."""
    payload = refresh(cache_dir, now)
    resolve = resolver()
    records = {identity(r): r for r in payload['matches'] if r['season'] == 2026}
    source = json.loads((Path(cache_dir)/'europa/sources/cornerflick.json').read_text(encoding='utf-8'))
    out = []
    for match in source['matches']:
        if not re.fullmatch(r'League Stage - \d+', match.get('round') or ''):
            continue
        stamp = datetime.fromisoformat(match['kickoff_at']).astimezone(timezone.utc)
        key = (stamp.date().isoformat(), resolve(match['home_team']), resolve(match['away_team']))
        row = records.get(key)
        if row is None: continue
        out.append({'match_id': hashlib.sha256('|'.join(key).encode()).hexdigest()[:20],
                    'league_code': 'EL', 'kickoff_utc': stamp.isoformat(),
                    'home_team': row['home'], 'away_team': row['away'],
                    'home_goals': row['regulation'][0], 'away_goals': row['regulation'][1],
                    'source': 'Cornerflick + Fixture Download', 'source_status': 'FINISHED',
                    'source_duration': 'REGULAR'})
    return out


def forecast_availability(league_keys, cache_dir, now=None, *, histories=None):
    """Preflight Europa before spending odds credits; other model errors still fail."""
    requested = list(league_keys)
    status = {'requested_leagues': requested, 'excluded_leagues': {}}
    if 'UEL' not in requested:
        return requested, status
    try:
        history = load(cache_dir, now)
        if histories is not None:
            histories['UEL'] = history
        if history.attrs.get('training_refresh_warning'):
            status['training_warnings'] = {'UEL': {
                'status': history.attrs['training_cache_status'],
                'verified_at_utc': history.attrs['training_verified_at_utc'],
                'reason': history.attrs['training_refresh_warning']}}
    except (ValueError, OSError, requests.RequestException) as exc:
        status['excluded_leagues']['UEL'] = {
            'status': 'TRAINING_UNVERIFIED',
            'reason': str(exc) if isinstance(exc, ValueError) else type(exc).__name__,
        }
    available = [key for key in requested if key not in status['excluded_leagues']]
    status['forecast_leagues'] = available
    if not available:
        raise ValueError('No requested leagues have verified training data: ' +
                         json.dumps(status['excluded_leagues'], sort_keys=True))
    return available, status
