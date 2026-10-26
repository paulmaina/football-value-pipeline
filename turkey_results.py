"""Date-precision Süper Lig settlement from keyless Football-Data.co.uk T1 CSVs.

Never invent a UTC kickoff from the CSV's unzoned Time column. Results match
reviewed team aliases and the exact UTC match date of the frozen forecast.
Missing/shifted dates remain unverified. Retain downloaded bytes for replay.
"""
from __future__ import annotations

from datetime import date
from functools import lru_cache
import csv
import hashlib
import io
import json
from pathlib import Path
import re

import requests

from match_scores import valid_goals
from refresh_training_data import inspect_csv, season_code, URL

SOURCE = 'football-data.co.uk/T1'
CODE = 'T1'


@lru_cache(maxsize=1)
def _aliases():
    from football_value_pipeline_v2_standalone import canonical_team_key
    aliases = json.loads(Path(__file__).with_name('bbs_team_aliases.json').read_text(encoding='utf-8'))['SuperLig']
    mapped = {canonical_team_key(k): v for k, v in aliases.items()}
    return mapped


def team_key(name):
    from football_value_pipeline_v2_standalone import canonical_team_key
    key = canonical_team_key(name)
    return canonical_team_key(_aliases().get(key, name))


def match_id(day, home, away):
    identity = '|'.join((CODE, day, team_key(home), team_key(away)))
    return 't1-' + hashlib.sha256(identity.encode()).hexdigest()[:24]


def source_url(year):
    return URL.format(season=season_code(year), division=CODE)


def evidence_path(root, year, digest):
    return Path(root)/'performance'/'result_sources'/'T1'/str(year)/(digest+'.csv')


def parse_results(content, year, clock):
    # Shared training validator rejects partial/invalid scores, wrong divisions,
    # future/wrong-season dates, duplicate fixtures and contradictory FTRs.
    header = next(csv.reader(io.StringIO(content.decode('utf-8-sig', errors='replace'))), [])
    if not {'Div', 'FTR'}.issubset(header):
        raise ValueError('Missing T1 division/result columns')
    matches = inspect_csv(content, CODE, year, clock)
    digest = hashlib.sha256(content).hexdigest()
    records, identities = [], set()
    for (day, home, away), (hg, ag) in matches.items():
        identity = match_id(day, home, away)
        if identity in identities or not team_key(home) or team_key(home) == team_key(away):
            raise ValueError('Ambiguous canonical T1 team identity')
        identities.add(identity)
        records.append({'match_id': identity, 'league_code': CODE,
            'match_date': day, 'date_precision': 'UTC_DATE_ONLY',
            'home_team': home, 'away_team': away,
            'home_goals': hg, 'away_goals': ag,
            'source': SOURCE, 'source_status': 'FINISHED', 'source_duration': 'REGULAR',
            'source_url': source_url(year), 'source_season_start': year,
            'source_sha256': digest})
    return records


def verified(record):
    """Strict, source-scoped cache contract; full evidence replay is below."""
    try:
        year = record['source_season_start']
        day = date.fromisoformat(record['match_date'])
        goals = valid_goals({'home': record['home_goals'], 'away': record['away_goals']})
        return (type(year) is int and 2000 <= year <= 2100
            and date(year, 7, 1) <= day < date(year+1, 7, 1)
            and record.get('league_code') == CODE and record.get('source') == SOURCE
            and record.get('source_status') == 'FINISHED' and record.get('source_duration') == 'REGULAR'
            and record.get('date_precision') == 'UTC_DATE_ONLY' and goals is not None
            and record.get('source_url') == source_url(year)
            and bool(re.fullmatch('[0-9a-f]{64}', record.get('source_sha256', '')))
            and isinstance(record['home_team'], str) and isinstance(record['away_team'], str)
            and bool(team_key(record['home_team']))
            and team_key(record['home_team']) != team_key(record['away_team'])
            and record.get('match_id') == match_id(record['match_date'], record['home_team'], record['away_team']))
    except (KeyError, TypeError, ValueError):
        return False


def validate_evidence(root, record, clock, *, evidence_cache=None):
    if not verified(record):
        raise ValueError('T1 result is not verified finished')
    path = evidence_path(root, record['source_season_start'], record['source_sha256'])
    cache = {} if evidence_cache is None else evidence_cache
    if path not in cache:
        if not path.is_file() or path.is_symlink():
            raise ValueError('Missing T1 result-source evidence')
        content = path.read_bytes()
        if hashlib.sha256(content).hexdigest() != record['source_sha256']:
            raise ValueError('T1 result-source checksum differs')
        cache[path] = {r['match_id']: r for r in parse_results(content, record['source_season_start'], clock)}
    expected = cache[path].get(record['match_id'])
    if expected is None or any(record.get(k) != v for k, v in expected.items()):
        raise ValueError('T1 result differs from source evidence')


def fetch_results(root, dates, clock, *, session=None):
    """One bounded keyless request per needed season; never trust checkout mtime."""
    get = session.get if session is not None else requests.get
    years = sorted({d.year if d.month >= 7 else d.year-1 for d in dates})
    records = []
    for year in years:
        response = get(source_url(year), headers={'Cache-Control': 'no-cache',
            'User-Agent': 'football-value-pipeline/results'}, timeout=30)
        response.raise_for_status()
        content = response.content
        if len(content) > 10_000_000:
            raise ValueError('T1 results exceed size limit')
        parsed = parse_results(content, year, clock)
        digest = hashlib.sha256(content).hexdigest()
        path = evidence_path(root, year, digest)
        path.parent.mkdir(parents=True, exist_ok=True)
        if path.exists() and path.read_bytes() != content:
            raise ValueError('T1 result-source evidence conflict')
        if not path.exists():
            path.write_bytes(content)
        records.extend(parsed)
    return records


def fixture_match(row, records):
    from performance_tracking import utc
    when = utc(row.get('kickoff_utc'))
    if when is None:
        return None, 'INVALID_FIXTURE'
    candidates = [r for r in records if verified(r)
        and r['match_date'] == when.date().isoformat()
        and team_key(row.get('home_team', '')) == team_key(r['home_team'])
        and team_key(row.get('away_team', '')) == team_key(r['away_team'])]
    if len(candidates) > 1:
        return None, 'AMBIGUOUS_FIXTURE'
    return (candidates[0], 'VERIFIED_FINISHED') if candidates else (None, 'UNVERIFIED_FIXTURE_OR_RESULT')
