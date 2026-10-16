"""Join collected BBS observations to existing cached history without duplicate games.

Exports enriched rows for future feature construction; never changes legacy caches
or invokes the production fitter. Every BBS field has an observation timestamp.
"""
from __future__ import annotations

import csv
import io
import json
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path

from bbs_data import LEAGUES, STAT_FIELDS, dumps, utc
from match_scores import regulation_goals

DIVISIONS = {'E0': 'EPL', 'SP1': 'LaLiga', 'D1': 'Bundesliga', 'I1': 'SerieA', 'F1': 'Ligue1'}
CSV_STATS = {'total_shots': 'S', 'shots_on_target': 'ST', 'corner_kicks': 'C',
             'fouls': 'F', 'yellow_cards': 'Y', 'red_cards': 'R'}


def read_existing(cache_dir):
    """Read source caches, not prediction files; preserve source columns and prices."""
    rows = []
    for path in sorted(Path(cache_dir).glob('????_*.csv')):
        division = path.stem.split('_')[-1]
        if division not in DIVISIONS:
            continue
        raw = path.read_bytes()
        try:
            text = raw.decode('utf-8-sig')
        except UnicodeDecodeError:
            text = raw.decode('latin-1')
        for row in csv.DictReader(io.StringIO(text)):
            if not row.get('FTHG') and not row.get('FTAG'):
                continue
            date = None
            for fmt in ('%d/%m/%Y', '%d/%m/%y'):
                try:
                    date = datetime.strptime(row['Date'], fmt).date().isoformat()
                    break
                except (ValueError, KeyError):
                    pass
            if not date:
                raise ValueError('Invalid source match date in ' + path.name)
            for field in ('FTHG', 'FTAG'):
                value = row.get(field, '')
                if not value.isdigit() or not 0 <= int(value) <= 30:
                    raise ValueError('Invalid source score in ' + path.name)
                row[field] = int(value)
            if not row.get('HomeTeam') or not row.get('AwayTeam'):
                raise ValueError('Missing source team identity')
            rows.append({**row, 'Date': date, 'league': DIVISIONS[division],
                'Season': str(2000 + int(path.stem[:2])), 'history_source': 'football-data.co.uk',
                'source_file': path.name})
    for path in sorted(Path(cache_dir).glob('fdorg_history_UCL_????.json')):
        payload = json.loads(path.read_text(encoding='utf-8-sig'))
        if not isinstance(payload.get('matches'), list):
            raise ValueError('Invalid UCL source cache')
        for match in payload['matches']:
            goals = regulation_goals(match.get('score'))
            if match.get('status') != 'FINISHED' or goals is None:
                continue
            rows.append({'league': 'UCL', 'Date': utc(match['utcDate']).date().isoformat(),
                'HomeTeam': match['homeTeam']['name'], 'AwayTeam': match['awayTeam']['name'],
                'FTHG': goals[0], 'FTAG': goals[1], 'Season': path.stem[-4:],
                'history_source': 'football-data.org', 'source_file': path.name,
                'kickoff_utc': utc(match['utcDate']).isoformat()})
    return rows


def season_year(value):
    value = str(value)
    if len(value) == 4 and value.isdigit() and int(value) >= 2100:
        return 2000 + int(value[:2])  # football-data.co.uk's 2627 format
    return int(value.split('-')[0])


def build_dataset(store, baseline, cutoff, explicit=None):
    from football_value_pipeline_v2_standalone import canonical_team_key
    cutoff = utc(cutoff)
    explicit = explicit or {}
    if not isinstance(explicit, dict) or any(not isinstance(v, dict) for v in explicit.values()):
        raise ValueError('Team map must contain league objects keyed by provider team ID')
    matches = [x for x in store.latest('match', cutoff.isoformat()) if x['league'] in LEAGUES]
    stats = {(x['league'], x['entity']): x for x in store.latest('statistics', cutoff.isoformat())}
    names = defaultdict(set)
    base_index = defaultdict(list)
    pair_index = defaultdict(list)
    result = []
    for original in baseline:
        if original['Date'] > cutoff.date().isoformat():
            continue
        row = dict(original)
        row['bbs_match_id'] = None
        row['bbs_statistics_available'] = False
        row['integration_status'] = 'existing_only'
        row['post_match_statistics_not_predictor_features'] = True
        index = len(result)
        result.append(row)
        league = row['league']
        for side in ('HomeTeam', 'AwayTeam'):
            names[(league, canonical_team_key(row[side]))].add(row[side])
        keys = (canonical_team_key(row['HomeTeam']), canonical_team_key(row['AwayTeam']))
        base_index[(league, row['Date'], *keys)].append(index)
        pair_index[(league, season_year(row['Season']), *keys)].append(index)
    for key, indexes in base_index.items():
        if len(indexes) > 1:
            raise ValueError('Duplicate baseline fixture: ' + str(key))
    # Resolve unique exact/canonical aliases only; no fuzzy name guessing.
    mappings, issues, fixtures = {}, [], []
    provider_names = defaultdict(set)
    for item in matches:
        for side in ('home', 'away'):
            team = item['payload'][side]
            provider_names[(item['league'], str(team['id']))].add(team['name'])
    for (league, entity), aliases in provider_names.items():
        configured = explicit.get(league, {}).get(entity)
        candidates = {n for alias in aliases for n in names.get((league, canonical_team_key(alias)), set())}
        if configured is not None:
            if not isinstance(configured, str) or not configured.strip():
                raise ValueError('Invalid explicit team mapping')
            mappings[(league, entity)] = {'name': configured, 'method': 'explicit'}
        elif len(candidates) == 1:
            mappings[(league, entity)] = {'name': next(iter(candidates)), 'method': 'unique_existing_alias'}
    collisions = Counter((league, canonical_team_key(value['name'])) for (league, _), value in mappings.items())
    for key in list(mappings):
        if collisions[(key[0], canonical_team_key(mappings[key]['name']))] > 1:
            issues.append({'type': 'team_mapping_collision', 'league': key[0], 'bbs_team_id': key[1]})
            del mappings[key]
    claimed = set()
    # Multiple provider IDs representing one fixture are also ambiguous.
    signatures = Counter()
    for item in matches:
        m, league = item['payload'], item['league']
        mapped = [mappings.get((league, str(m[s]['id']))) for s in ('home', 'away')]
        if all(mapped):
            signatures[(league, utc(m['kickoff_utc']).date().isoformat(),
                        *(canonical_team_key(x['name']) for x in mapped))] += 1
    for item in matches:
        m, league = item['payload'], item['league']
        fixture = {**m, 'league_key': league, 'bbs_match_id': item['entity'], 'join_status': 'unmapped'}
        fixtures.append(fixture)
        mapped = [mappings.get((league, str(m[s]['id']))) for s in ('home', 'away')]
        if not all(mapped):
            issues.append({'type': 'unmapped_team', 'league': league, 'bbs_match_id': item['entity']})
            continue
        home, away = [x['name'] for x in mapped]
        day = utc(m['kickoff_utc']).date().isoformat()
        key = (league, day, canonical_team_key(home), canonical_team_key(away))
        if signatures[key] > 1:
            fixture['join_status'] = 'ambiguous'
            issues.append({'type': 'duplicate_provider_fixture', 'bbs_match_id': item['entity']})
            continue
        indexes = base_index.get(key, [])
        if indexes:
            index = indexes[0]
            row = result[index]
            if index in claimed:
                raise ValueError('Multiple matches attempted to enrich the same baseline row')
            claimed.add(index)
            row['bbs_home_team_id'] = str(m['home']['id'])
            row['bbs_away_team_id'] = str(m['away']['id'])
            row['bbs_kickoff_utc'] = m['kickoff_utc']
            row['bbs_match_id'] = item['entity']
            row['bbs_match_observed_at'] = item['observed']
            row['bbs_source_updated_at'] = m.get('source_updated_at')
            score = m.get('score') or {}
            same_score = (score.get('home'), score.get('away')) == (row['FTHG'], row['FTAG'])
            if m['status'] != 'finished' or not same_score:
                row['integration_status'] = fixture['join_status'] = 'conflict'
                issues.append({'type': 'result_or_status_conflict', 'bbs_match_id': item['entity'],
                    'existing': [row['FTHG'], row['FTAG']], 'bbs': score, 'bbs_status': m['status']})
                continue
            row['integration_status'] = fixture['join_status'] = 'matched'
        else:
            pair = (league, int(m['requested_season']), key[2], key[3])
            if pair_index.get(pair):
                fixture['join_status'] = 'date_conflict'
                issues.append({'type': 'kickoff_date_conflict', 'bbs_match_id': item['entity'],
                    'bbs_date': day, 'existing_dates': [result[i]['Date'] for i in pair_index[pair]]})
                continue
            if m['status'] != 'finished':
                fixture['join_status'] = 'mapped_fixture'
                continue
            if not m.get('regulation_score_verified'):
                fixture['join_status'] = 'unverified_regulation_score'
                issues.append({'type': 'regulation_score_unknown', 'bbs_match_id': item['entity']})
                continue
            row = {'league': league, 'Date': day, 'HomeTeam': home, 'AwayTeam': away,
                'FTHG': m['score']['home'], 'FTAG': m['score']['away'],
                'Season': str(m['requested_season']), 'history_source': 'bigballsdata',
                'bbs_match_id': item['entity'], 'bbs_match_observed_at': item['observed'],
                'bbs_source_updated_at': m.get('source_updated_at'), 'integration_status': 'added',
                'bbs_statistics_available': False, 'post_match_statistics_not_predictor_features': True}
            result.append(row)
            fixture['join_status'] = 'added'
        row['bbs_home_team_id'] = str(m['home']['id'])
        row['bbs_away_team_id'] = str(m['away']['id'])
        row['bbs_kickoff_utc'] = m['kickoff_utc']
        observation = stats.get((league, item['entity']))
        if not observation:
            continue
        values = observation['payload']
        if values.get('team_ids') != {s: str(m[s]['id']) for s in ('home', 'away')}:
            issues.append({'type': 'statistics_identity_conflict', 'bbs_match_id': item['entity']})
            continue
        row['bbs_statistics_observed_at'] = observation['observed']
        row['bbs_statistics_available'] = values['available']
        for side, prefix in [('home', 'H'), ('away', 'A')]:
            for field in STAT_FIELDS:
                value = (values.get(side) or {}).get(field)
                row[f'bbs_{side}_{field}'] = value
                # Preserve the original feed's columns. Disagreements are visible,
                # not averaged or silently substituted in legacy model inputs.
                source_col = prefix + CSV_STATS[field] if field in CSV_STATS else None
                if source_col and row.get(source_col) not in (None, '') and value is not None:
                    try:
                        differs = float(row[source_col]) != value
                    except (TypeError, ValueError):
                        differs = True
                    if differs:
                        issues.append({'type': 'statistic_conflict', 'bbs_match_id': item['entity'],
                            'field': source_col, 'existing': row[source_col], 'bbs': value})
    for row in result:
        row['bbs_conflict_flags'] = '|'.join(sorted({i['type'] for i in issues
            if row.get('bbs_match_id') and i.get('bbs_match_id') == row['bbs_match_id']}))
    result.sort(key=lambda r: (r['league'], r['Date'], r['HomeTeam'], r['AwayTeam']))
    freshness = {}
    for kind in ('match', 'statistics', 'standings', 'team', 'player'):
        observations = store.latest(kind, cutoff.isoformat())
        freshness[kind] = {}
        for league in LEAGUES:
            items = [x for x in observations if x['league'] == league]
            ages = [(cutoff - utc(x['observed'])).total_seconds() / 3600 for x in items]
            freshness[kind][league] = {
                'records': len(items),
                'oldest_observation_age_hours': max(ages) if ages else None,
                'newest_observation_age_hours': min(ages) if ages else None,
            }
    report = {'observation_freshness': freshness, 'cutoff_utc': cutoff.isoformat(), 'rows': len(result), 'bbs_matches': len(matches),
        'join_counts': dict(Counter(r['join_status'] for r in fixtures)),
        'rows_with_bbs_statistics': sum(bool(r['bbs_statistics_available']) for r in result),
        'issues': issues, 'baseline_history_is_current_revision_not_point_in_time': True,
        'note': 'Observation cutoff applies to BBS only. Same-match statistics are outcomes, never pre-match features.'}
    return {'matches': result, 'fixtures': fixtures, 'team_mappings': [
        {'league': l, 'bbs_team_id': i, **v} for (l, i), v in sorted(mappings.items())],
        'standings': store.latest('standings', cutoff.isoformat()),
        'teams': store.latest('team', cutoff.isoformat()), 'players': store.latest('player', cutoff.isoformat()),
        'report': report}


def write_dataset(dataset, output):
    """Publish CSV/JSON as a timestamped generation, then switch the manifest."""
    import hashlib
    from bbs_data import atomic_json
    output = Path(output)
    digest = hashlib.sha256(dumps(dataset).encode()).hexdigest()
    stamp = utc(dataset['report']['cutoff_utc']).strftime('%Y%m%dT%H%M%S%fZ')
    generation = output / 'snapshots' / (stamp + '_' + digest)
    generation.mkdir(parents=True, exist_ok=True)
    files = {}
    for key in ('fixtures', 'standings', 'teams', 'players', 'team_mappings', 'report'):
        files[key + '.json'] = (dumps(dataset[key]) + '\n').encode()
    for league in LEAGUES:
        rows = [r for r in dataset['matches'] if r['league'] == league]
        if not rows:
            continue
        fields = sorted({k for r in rows for k in r})
        out = io.StringIO(newline='')
        writer = csv.DictWriter(out, fields)
        writer.writeheader()
        writer.writerows(rows)
        files[f'{league}_enriched_history.csv'] = out.getvalue().encode()
    for name, content in files.items():
        path = generation / name
        if path.exists() and path.read_bytes() != content:
            raise ValueError('Immutable combined snapshot conflict')
        path.write_bytes(content)
    manifest = {'version': 1, 'cutoff_utc': dataset['report']['cutoff_utc'],
        'generation': generation.relative_to(output).as_posix(),
        'sha256': {name: hashlib.sha256(data).hexdigest() for name, data in files.items()}}
    atomic_json(generation / 'manifest.json', manifest)
    atomic_json(output / 'latest.json', manifest)
    return generation


def read_combined(cache_dir, league, cutoff):
    """Read only complete published CSV snapshots available by the forecast cutoff."""
    import hashlib
    from bbs_data import decode
    root = Path(cache_dir) / 'bbs' / 'combined'
    if not (root / 'latest.json').exists():
        return []
    limit = utc(cutoff)
    manifest = decode((root / 'latest.json').read_text())
    if utc(manifest['cutoff_utc']) > limit:
        candidates = [decode(p.read_text()) for p in (root/'snapshots').glob('*/manifest.json')]
        candidates = [m for m in candidates if utc(m['cutoff_utc']) <= limit]
        if not candidates:
            return []
        manifest = max(candidates, key=lambda m: utc(m['cutoff_utc']))
    generation = (root / manifest['generation']).resolve()
    if not generation.is_relative_to((root / 'snapshots').resolve()):
        raise ValueError('Combined snapshot escapes cache')
    name = f'{league}_enriched_history.csv'
    if name not in manifest['sha256']:
        return []
    data = (generation / name).read_bytes()
    if hashlib.sha256(data).hexdigest() != manifest['sha256'][name]:
        raise ValueError('Combined training CSV checksum mismatch')
    return list(csv.DictReader(io.StringIO(data.decode('utf-8'))))


def combined_training_history(baseline, cache_dir, league, now, seasons_back):
    """Reconcile the shared CSV against freshly loaded primary history.

    Never substitute an old exported primary score for a newer primary revision.
    BBS statistics remain additional columns, not newly fitted model features.
    """
    import pandas as pd
    from football_value_pipeline_v2_standalone import canonical_team_key, current_season_start_year
    rows = read_combined(cache_dir, league, now.isoformat())
    if not rows:
        return baseline
    records = baseline.to_dict('records')
    def identity(r):
        return (pd.Timestamp(r['Date']).date().isoformat(),
                canonical_team_key(r['HomeTeam']), canonical_team_key(r['AwayTeam']))
    index = {identity(r): r for r in records}
    if len(index) != len(records):
        raise ValueError('Duplicate baseline fixture')
    first = current_season_start_year(now) - seasons_back + 1
    last = current_season_start_year(now)
    pairs = {(season_year(r['Season']), *identity(r)[1:]) for r in records}
    seen = set()
    for row in rows:
        key = identity(row)
        if key in seen:
            raise ValueError('Duplicate combined fixture')
        seen.add(key)
        if not row.get('bbs_match_id'):
            continue
        observed = row.get('bbs_match_observed_at')
        if not observed or utc(observed) > utc(now.isoformat()):
            continue
        year = season_year(row['Season'])
        if not first <= year <= last:
            continue
        if row.get('bbs_kickoff_utc') and utc(row['bbs_kickoff_utc']) >= now:
            continue
        existing = index.get(key)
        if existing is not None:
            metadata = {k: v for k, v in row.items() if k.startswith('bbs_')}
            metadata['integration_status'] = row['integration_status']
            if (int(row['FTHG']), int(row['FTAG'])) != (int(existing['FTHG']), int(existing['FTAG'])):
                metadata = {k: v for k, v in metadata.items() if k not in
                    {f'bbs_{side}_{field}' for side in ('home', 'away') for field in STAT_FIELDS}}
                metadata.update(integration_status='conflict', bbs_statistics_available=False)
            existing.update(metadata)
        elif row['integration_status'] == 'added' and league != 'UCL':
            if (year, *key[1:]) in pairs:
                continue  # Possible reschedule; never count it twice.
            if not row.get('bbs_kickoff_utc') or utc(row['bbs_kickoff_utc']) >= now:
                continue
            for col in ('FTHG', 'FTAG'):
                if not row[col].isdigit() or not 0 <= int(row[col]) <= 30:
                    raise ValueError('Invalid combined score')
                row[col] = int(row[col])
            row['Season'] = f'{year % 100:02d}{(year + 1) % 100:02d}'
            records.append(row)
            pairs.add((year, *key[1:]))
    result = pd.DataFrame(records)
    result['Date'] = pd.to_datetime(result['Date'])
    for col in ('FTHG', 'FTAG'):
        result[col] = pd.to_numeric(result[col], errors='raise')
    # Added rows have no invented bookmaker prices; preserve numeric odds columns.
    for col in baseline.select_dtypes(include='number').columns:
        if col in result:
            result[col] = pd.to_numeric(result[col], errors='coerce')
    for side in ('home', 'away'):
        for field in STAT_FIELDS:
            col = f'bbs_{side}_{field}'
            if col in result:
                result[col] = pd.to_numeric(result[col], errors='coerce')
    if 'bbs_statistics_available' in result:
        result['bbs_statistics_available'] = result['bbs_statistics_available'].map(
            lambda value: value is True or value == 'True')
    return result.sort_values('Date').reset_index(drop=True)
