"""Reconcile optional API-Football observations with primary/BBS training data.

No network access and no fuzzy identity guesses. Preserve authoritative results,
prices, and BBS evidence; hold conflicting/ambiguous provider records separately.
"""
from collections import Counter, defaultdict
import json
from pathlib import Path

import pandas as pd

from api_football_data import FINISHED, observations, payload_digest
from bbs_data import utc
from bbs_integration import CSV_STATS, season_year


def latest(rows):
    result = {}
    for row in sorted(rows, key=lambda r: utc(r['observed'])):
        key = (row['league'], row['entity'])
        if key in result and result[key]['observed'] == row['observed'] and result[key]['payload'] != row['payload']:
            raise ValueError('Conflicting API-Football revisions at same timestamp')
        result[key] = row
    return result


def records(cache, league, cutoff):
    matches = latest(observations(cache, 'match', cutoff))
    held = latest(observations(cache, 'quarantine', cutoff))
    return [r for key, r in matches.items() if r['league'] == league and
            (key not in held or utc(held[key]['observed']) < utc(r['observed']))]


def mappings(history, cache, league, matches):
    from football_value_pipeline_v2_standalone import canonical_team_key
    names = defaultdict(set)
    for col in ('HomeTeam', 'AwayTeam'):
        for name in history.get(col, pd.Series(dtype=object)).dropna():
            names[canonical_team_key(str(name))].add(str(name))
    path = Path(cache)/'api_football/team_map.json'
    explicit = json.loads(path.read_text(encoding='utf-8')) if path.exists() else {}
    if not isinstance(explicit, dict) or not isinstance(explicit.get(league, {}), dict):
        raise ValueError('Invalid API-Football reviewed team map')
    aliases = defaultdict(set)
    for row in matches:
        for side in ('home', 'away'):
            team = row['payload'][side]
            aliases[str(team['id'])].add(team['name'])
    mapped = {}
    for entity, options in aliases.items():
        target = explicit.get(league, {}).get(entity)
        if target is not None:
            if not isinstance(target, str) or not target.strip():
                raise ValueError('Invalid API-Football reviewed team identity')
            mapped[entity] = target
        else:
            candidates = {n for option in options for n in names.get(canonical_team_key(option), set())}
            if len(candidates) == 1:
                mapped[entity] = next(iter(candidates))
    collisions = Counter(canonical_team_key(name) for name in mapped.values())
    return {k: v for k, v in mapped.items() if collisions[canonical_team_key(v)] == 1}


def reconcile(baseline, cache, league, now, seasons_back):
    """Add verified missing scores and bind optional, lagged-only statistics."""
    from football_value_pipeline_v2_standalone import canonical_team_key, current_season_start_year
    cutoff = now.isoformat()
    matches = records(cache, league, cutoff)
    if not matches:
        return baseline
    names = mappings(baseline, cache, league, matches)
    def identity(row):
        return (pd.Timestamp(row['Date']).date().isoformat(),
                canonical_team_key(row['HomeTeam']), canonical_team_key(row['AwayTeam']))
    rows = baseline.to_dict('records'); index = {identity(r): r for r in rows}
    if len(index) != len(rows):
        raise ValueError('Duplicate baseline fixture')
    pairs = {(season_year(r['Season']), *identity(r)[1:]) for r in rows}
    first = current_season_start_year(now)-seasons_back+1
    last = current_season_start_year(now)
    resolved = []
    report = {'status': 'AVAILABLE', 'matched_results': 0, 'added_results': 0,
              'conflicts': 0, 'unmapped': 0, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 0,
              'source': 'api-football', 'usage': 'supplementary_cached_observations'}
    for observation in matches:
        m = observation['payload']
        if not m['training_scope_eligible']:
            report['excluded_phase'] += 1
            continue
        if m['status'] not in FINISHED or not m['regulation_score_verified']:
            continue
        if not first <= m['season'] <= last or utc(m['kickoff_utc']) >= now:
            continue
        mapped = [names.get(str(m[s]['id'])) for s in ('home', 'away')]
        if not all(mapped):
            report['unmapped'] += 1
            continue
        day = utc(m['kickoff_utc']).date().isoformat()
        key = (day, *(canonical_team_key(n) for n in mapped))
        resolved.append((observation, mapped, key))
    signatures = Counter(key for _, _, key in resolved)
    # Two provider IDs for one ordered pair/season can be a duplicate or reschedule.
    # UCL can have legitimate rematches; an exact-date match to primary wins there.
    provider_pairs = Counter((r['payload']['season'], *key[1:]) for r, _, key in resolved)
    bound = {}
    for observation, mapped, key in resolved:
        m = observation['payload']; pair = (m['season'], *key[1:])
        if signatures[key] != 1 or (league != 'UCL' and provider_pairs[pair] != 1):
            report['ambiguous'] += 1
            continue
        existing = index.get(key)
        if existing is not None:
            if (int(existing['FTHG']), int(existing['FTAG'])) != (m['score']['home'], m['score']['away']):
                report['conflicts'] += 1
                continue
            if existing.get('kickoff_utc') and abs((utc(existing['kickoff_utc'])-utc(m['kickoff_utc'])).total_seconds()) > 3600:
                report['conflicts'] += 1
                continue
            report['matched_results'] += 1
        else:
            if pair in pairs or provider_pairs[pair] > 1:
                report['conflicts'] += 1
                continue
            existing = {'Date': pd.Timestamp(m['kickoff_utc']).tz_localize(None) if league == 'UCL' else key[0],
                'HomeTeam': mapped[0], 'AwayTeam': mapped[1],
                'FTHG': m['score']['home'], 'FTAG': m['score']['away'],
                'Season': str(m['season']) if league == 'UCL' else f"{m['season']%100:02d}{(m['season']+1)%100:02d}",
                'competition': league, 'history_source': 'api-football', 'kickoff_utc': m['kickoff_utc']}
            rows.append(existing); index[key] = existing; pairs.add(pair)
            report['added_results'] += 1
        existing.update(api_football_match_id=observation['entity'],
                        api_football_observed_at_utc=observation['observed'])
        bound[observation['entity']] = (existing, m)
    features = []
    for observation in observations(cache, 'statistics', cutoff):
        if observation['league'] != league or observation['entity'] not in bound:
            continue
        row, match = bound[observation['entity']]; values = observation['payload']
        available = (match['status'] == 'FT' and values.get('available') is True and
            values.get('team_ids') == {s: str(match[s]['id']) for s in ('home', 'away')} and
            utc(observation['observed']) > utc(match['kickoff_utc']))
        for side, prefix in [('home', 'H'), ('away', 'A')]:
            for field, suffix in CSV_STATS.items():
                value = (values.get(side) or {}).get(field)
                for column in (prefix+suffix, 'bbs_'+side+'_'+field):
                    primary = row.get(column)
                    if primary is not None and not pd.isna(primary) and primary != '' and value is not None:
                        if float(primary) != float(value):
                            available = False
        features.append({'match_id': league+':api-football:'+observation['entity'],
            'source': 'api-football', 'home_team': row['HomeTeam'], 'away_team': row['AwayTeam'],
            'kickoff_utc': match['kickoff_utc'], 'observed_at_utc': observation['observed'],
            'available': available, 'home': values.get('home') if available else None,
            'away': values.get('away') if available else None})
    result = pd.DataFrame(rows)
    result['Date'] = pd.to_datetime(result['Date'])
    for col in baseline.select_dtypes(include='number').columns:
        result[col] = pd.to_numeric(result[col], errors='coerce')
    result = result.sort_values('Date').reset_index(drop=True)
    result.attrs = dict(baseline.attrs)
    existing_features = list(result.attrs.get('bbs_statistics_observations', []))
    result.attrs['bbs_statistics_observations'] = existing_features+features
    report['statistics_observations'] = len(features)
    result.attrs['api_football'] = report
    return result


def augment_history(baseline, cache, league, now, seasons_back):
    try:
        return reconcile(baseline, cache, league, now, seasons_back)
    except (ValueError, KeyError, TypeError, OSError, AttributeError):
        # Optional source corruption cannot invalidate trusted primary/BBS inputs.
        result = baseline.copy()
        result.attrs = dict(baseline.attrs)
        result.attrs['api_football'] = {'status': 'BASELINE_RETAINED_SOURCE_ERROR', 'source': 'api-football'}
        return result


def supplement_fixtures(primary, history, cache, league, now, lookahead_days):
    """Union recently observed, mapped schedules; primary conflicts always win."""
    from football_value_pipeline_v2_standalone import canonical_team_key
    from datetime import timedelta
    try:
        matches = records(cache, league, now.isoformat())
        schedules = latest(observations(cache, 'schedule', now.isoformat()))
        names = mappings(history, cache, league, matches)
        rows = primary.to_dict('records')
        pairs = {(canonical_team_key(r['HomeTeam']), canonical_team_key(r['AwayTeam'])) for r in rows}
        candidates = []
        for observation in matches:
            m = observation['payload']; kick = utc(m['kickoff_utc'])
            heartbeat = schedules.get((league, str(m['season'])))
            if heartbeat and heartbeat['payload']['match_sha256'].get(observation['entity']) == payload_digest(m):
                observation = {**observation, 'observed': max(observation['observed'], heartbeat['observed'])}
            if (m['status'] != 'NS' or not m['training_scope_eligible'] or not now < kick <= now+timedelta(days=lookahead_days)
                    or not 0 <= (now-utc(observation['observed'])).total_seconds() <= 24*3600):
                continue
            mapped = [names.get(str(m[s]['id'])) for s in ('home', 'away')]
            if all(mapped):
                pair = tuple(canonical_team_key(n) for n in mapped)
                candidates.append((observation, mapped, pair))
        counts = Counter(pair for _, _, pair in candidates)
        for observation, mapped, pair in candidates:
            if pair in pairs or counts[pair] != 1:
                continue
            m = observation['payload']
            rows.append({'Date': pd.Timestamp(m['kickoff_utc']).tz_localize(None),
                'HomeTeam': mapped[0], 'AwayTeam': mapped[1],
                'kickoff_utc': m['kickoff_utc'], 'fixture_id': 'api-football:'+observation['entity'],
                'fixture_source': 'API-Football cached', 'fixture_observed_at_utc': observation['observed']})
            pairs.add(pair)
        return pd.DataFrame(rows) if len(rows) > len(primary) else primary
    except (ValueError, KeyError, TypeError, OSError, AttributeError):
        return primary
