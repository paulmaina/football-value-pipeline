"""Join collected BBS match results to existing cached history without duplicate games.

Exports enriched rows; never changes legacy caches or invokes the production fitter.
Every BBS field has an observation timestamp. The match-statistics adjustment and its
statistics, standings, player and coverage collections were retired on 25 Nov 2026.
"""
from __future__ import annotations

import csv
import io
import json
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path

from bbs_data import LEAGUES, dumps, utc
from match_scores import regulation_goals

import league_registry

# football-data.co.uk division -> league key, for domestic leagues BBS covers.
DIVISIONS = {div: key for key, div in league_registry.divisions().items() if key in LEAGUES}
# Holds the one committed combined generation; legacy timestamped copies stay readable.
GENERATIONS = 'generations'


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
    reviewed = json.loads(Path(__file__).with_name('bbs_team_aliases.json').read_text(encoding='utf-8'))
    if not isinstance(explicit, dict) or any(not isinstance(v, dict) for v in explicit.values()):
        raise ValueError('Team map must contain league objects keyed by provider team ID')
    matches = [x for x in store.latest('match', cutoff.isoformat()) if x['league'] in LEAGUES]
    active_quarantine = []
    for q in store.latest('quarantine', cutoff.isoformat()):
        valid = next((m for m in matches if m['league']==q['league'] and m['entity']==q['entity']), None)
        if valid is None or utc(q['observed']) >= utc(valid['observed']):
            active_quarantine.append(q)
    held = {(q['league'], q['entity']) for q in active_quarantine}
    matches = [m for m in matches if (m['league'],m['entity']) not in held]
    names = defaultdict(set)
    base_index = defaultdict(list)
    pair_index = defaultdict(list)
    result = []
    for original in baseline:
        if original['Date'] > cutoff.date().isoformat():
            continue
        row = dict(original)
        row['bbs_match_id'] = None
        row['integration_status'] = 'existing_only'
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
    # The team surface can use a different ID for one reviewed club.
    for item in store.latest('team', cutoff.isoformat()):
        if item['league'] in LEAGUES and item['payload'].get('name'):
            provider_names[(item['league'], item['entity'])].add(item['payload']['name'])
    for (league, entity), aliases in provider_names.items():
        configured = explicit.get(league, {}).get(entity)
        candidates = {n for alias in aliases for n in names.get((league, canonical_team_key(
            reviewed.get(league, {}).get(alias, alias))), set())}
        if configured is not None:
            if not isinstance(configured, str) or not configured.strip():
                raise ValueError('Invalid explicit team mapping')
            mappings[(league, entity)] = {'name': configured, 'method': 'explicit'}
        elif len(candidates) == 1:
            mappings[(league, entity)] = {'name': next(iter(candidates)),
                'method': 'reviewed_name_alias' if any(a in reviewed.get(league, {}) for a in aliases) else 'unique_existing_alias'}
    collisions = Counter((league, canonical_team_key(value['name'])) for (league, _), value in mappings.items())
    for key in list(mappings):
        if collisions[(key[0], canonical_team_key(mappings[key]['name']))] > 1:
            # Multiple explicitly reviewed or exact-name identities may refer to
            # one club across surfaces. Duplicate match records are still held.
            aliases = provider_names[key]
            target = canonical_team_key(mappings[key]['name'])
            proven = all(canonical_team_key(reviewed.get(key[0], {}).get(a, a)) == target for a in aliases)
            if not proven:
                issues.append({'type': 'team_mapping_collision', 'league': key[0], 'bbs_team_id': key[1]})
                del mappings[key]
    claimed = set()
    # Multiple provider IDs representing one fixture are also ambiguous.
    signatures = Counter()
    completed_pairs = Counter()
    for item in matches:
        m, league = item['payload'], item['league']
        mapped = [mappings.get((league, str(m[s]['id']))) for s in ('home', 'away')]
        if all(mapped):
            if league != 'UCL' and m['status'] == 'finished':
                completed_pairs[(league, int(m['requested_season']),
                    *(canonical_team_key(x['name']) for x in mapped))] += 1
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
        pair = (league, int(m['requested_season']), key[2], key[3])
        if signatures[key] > 1 or (m['status'] == 'finished' and completed_pairs[pair] > 1):
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
                'bbs_source_updated_at': m.get('source_updated_at'), 'integration_status': 'added'}
            result.append(row)
            fixture['join_status'] = 'added'
        row['bbs_home_team_id'] = str(m['home']['id'])
        row['bbs_away_team_id'] = str(m['away']['id'])
        row['bbs_kickoff_utc'] = m['kickoff_utc']
    for row in result:
        row['bbs_conflict_flags'] = '|'.join(sorted({i['type'] for i in issues
            if row.get('bbs_match_id') and i.get('bbs_match_id') == row['bbs_match_id']}))
    result.sort(key=lambda r: (r['league'], r['Date'], r['HomeTeam'], r['AwayTeam']))
    freshness = {}
    for kind in ('match', 'team'):
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
    training_coverage = []
    for league in LEAGUES:
        seasons = {int(x['payload']['requested_season']) for x in matches if x['league'] == league}
        for year in sorted(seasons):
            rows = [r for r in result if r['league'] == league and season_year(r['Season']) == year]
            baseline_rows = [r for r in rows if r.get('history_source') != 'bigballsdata']
            matched = sum(r['integration_status'] == 'matched' for r in baseline_rows)
            observed = sum(x['league'] == league and int(x['payload']['requested_season']) == year and x['payload']['status'] == 'finished' for x in matches)
            training_coverage.append(dict(league=league, season=year, baseline_matches=len(baseline_rows),
                bbs_finished_matches=observed, matched_results=matched,
                existing_results_without_bbs_confirmation=len(baseline_rows)-matched))
    report = {'quarantined_records': [dict(league=q['league'], bbs_match_id=q['entity'], reason=q['payload']['reason']) for q in active_quarantine],
        'training_coverage': training_coverage,
        'data_quality_status': 'partial' if active_quarantine or issues or any(x['existing_results_without_bbs_confirmation'] for x in training_coverage) else 'verified_joins',
        'observation_freshness': freshness, 'cutoff_utc': cutoff.isoformat(), 'rows': len(result), 'bbs_matches': len(matches),
        'join_counts': dict(Counter(r['join_status'] for r in fixtures)),
        'issues': issues, 'baseline_history_is_current_revision_not_point_in_time': True,
        'note': 'Observation cutoff applies to BBS only.'}
    return {'matches': result, 'fixtures': fixtures, 'team_mappings': [
        {'league': l, 'bbs_team_id': i, **v} for (l, i), v in sorted(mappings.items())],
        'teams': store.latest('team', cutoff.isoformat()), 'report': report}


def _dataset_files(dataset):
    files = {}
    for key in ('fixtures', 'teams', 'team_mappings', 'report'):
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
    return files


def write_dataset(dataset, output):
    """Stage a complete generation, switch the manifest atomically, then prune.

    The view is rebuilt from immutable observations, so only the generation the
    manifest points to is kept; earlier cutoffs are rebuilt by read_combined.
    Until the switch, readers keep the previous complete generation; an
    interrupted publish leaves an unused staged copy that the next one prunes.
    """
    import hashlib
    import os
    import shutil
    import tempfile
    from bbs_data import atomic_json
    output = Path(output)
    files = _dataset_files(dataset)
    sha256 = {name: hashlib.sha256(data).hexdigest() for name, data in files.items()}
    digest = hashlib.sha256(dumps(sha256).encode()).hexdigest()
    generations = output / GENERATIONS
    generation = generations / digest[:16]
    manifest = {'version': 2, 'cutoff_utc': dataset['report']['cutoff_utc'],
                'generation': generation.relative_to(output).as_posix(), 'sha256': sha256}
    if not generation.exists():
        generations.mkdir(parents=True, exist_ok=True)
        staging = Path(tempfile.mkdtemp(prefix='.staging-', dir=generations))
        try:
            for name, content in files.items():
                (staging / name).write_bytes(content)
            atomic_json(staging / 'manifest.json', manifest)
            os.replace(staging, generation)
        finally:
            shutil.rmtree(staging, ignore_errors=True)
    atomic_json(output / 'latest.json', manifest)
    for old in generations.iterdir():
        if old != generation:
            shutil.rmtree(old, ignore_errors=True)
    return generation


_REBUILT = {}


def _rebuilt_files(cache_dir, cutoff):
    """Rebuild the combined view at an earlier cutoff from immutable observations."""
    from bbs_data import Store, decode
    key = (str(Path(cache_dir).resolve()), cutoff)
    if key not in _REBUILT:
        state = Path(cache_dir) / 'bbs' / 'state'
        if not state.is_dir():
            return {}
        mapping = Path(cache_dir) / 'bbs' / 'team_map.json'
        explicit = decode(mapping.read_text()) if mapping.exists() else {}
        store = Store(state)
        try:
            # Before the first observation there is no BBS data to use.
            observed = any(utc(row['observed']) <= utc(cutoff) for row in store.observations)
            dataset = build_dataset(store, read_existing(cache_dir), cutoff, explicit) if observed else None
        finally:
            store.close()
        _REBUILT.clear()
        _REBUILT[key] = _dataset_files(dataset) if dataset else {}
    return _REBUILT[key]


def read_combined(cache_dir, league, cutoff, _retried=False):
    """Read the combined CSV as available by the forecast cutoff.

    The current generation serves cutoffs at or after its own. A cutoff before
    the last legacy timestamped snapshot reads legacy snapshots exactly as
    before, so archived replays are unchanged; any other earlier cutoff is
    rebuilt from the immutable observations.
    """
    import hashlib
    from bbs_data import decode
    root = Path(cache_dir) / 'bbs' / 'combined'
    if not (root / 'latest.json').exists():
        return []
    limit = utc(cutoff)
    manifest = decode((root / 'latest.json').read_text())
    name = f'{league}_enriched_history.csv'
    if utc(manifest['cutoff_utc']) > limit:
        legacy = [decode(p.read_text()) for p in (root/'snapshots').glob('*/manifest.json')]
        if legacy and limit < max(utc(m['cutoff_utc']) for m in legacy):
            candidates = [m for m in legacy if utc(m['cutoff_utc']) <= limit]
            if not candidates:
                return []
            manifest = max(candidates, key=lambda m: utc(m['cutoff_utc']))
        else:
            data = _rebuilt_files(cache_dir, limit.isoformat()).get(name)
            return list(csv.DictReader(io.StringIO(data.decode('utf-8')))) if data else []
    generation = (root / manifest['generation']).resolve()
    if not any(generation.is_relative_to((root / part).resolve()) for part in ('snapshots', GENERATIONS)):
        raise ValueError('Combined snapshot escapes cache')
    if name not in manifest['sha256']:
        return []
    try:
        data = (generation / name).read_bytes()
    except FileNotFoundError:
        # A concurrent publish switched the manifest and pruned this generation:
        # choose again from the new manifest, once.
        if _retried or manifest['generation'].startswith('snapshots/'):
            raise
        return read_combined(cache_dir, league, cutoff, _retried=True)
    if hashlib.sha256(data).hexdigest() != manifest['sha256'][name]:
        raise ValueError('Combined training CSV checksum mismatch')
    return list(csv.DictReader(io.StringIO(data.decode('utf-8'))))


def combined_training_history(baseline, cache_dir, league, now, seasons_back):
    """Reconcile the shared CSV against freshly loaded primary history.

    Never substitute an old exported primary score for a newer primary revision.
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
                metadata['integration_status'] = 'conflict'
                flags = set(filter(None, str(metadata.get('bbs_conflict_flags', '')).split('|')))
                flags.add('result_or_status_conflict')
                metadata['bbs_conflict_flags'] = '|'.join(sorted(flags))
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
    result = result.sort_values('Date').reset_index(drop=True)
    return result


def training_provenance(history):
    """Report the BBS contribution actually present in the fitted input frame."""
    import pandas as pd
    ids = history.get('bbs_match_id', pd.Series(dtype=object))
    confirmed = ids.notna() & ids.astype(str).str.strip().ne('')
    statuses = history.get('integration_status', pd.Series(dtype=object))
    result = {'bbs_confirmed_rows': int((confirmed & statuses.isin(['matched', 'added'])).sum()),
            'bbs_added_results': int(statuses.eq('added').sum()),
            'bbs_result_conflicts': int(statuses.eq('conflict').sum()),
            'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history.'}
    if 'api_football' in history.attrs:
        result['api_football'] = history.attrs['api_football']
    return result
