"""Extract expected goals from the cached API-Football statistics responses (offline; docs/plan.md, Phase 2i).

Makes no API-Football request: it reads only `.football_cache/api_football/state` (the collector's immutable match
observations and its cached `/fixtures/statistics` responses) and the football-data caches the harness trains on.
The collector itself, its schedule and config, and the live pipeline are not touched.

Each fixture is mapped to our match identity with the live integration's own name checks
(`api_football_integration.mappings`: a unique canonical name in our history or the reviewed team map; no close
matching), then to exactly one history row on the same date with the same ordered teams. The API-Football
regulation score must equal that row's score, or the fixture is reported as failing to map.

Kept: regular-season league rounds (domestic) and UCL group stage, league stage and knockout rounds, status FT only.
Left out and counted: play-offs (domestic relegation rounds and deciders, UCL qualifying play-offs and knockout
round play-offs), qualifiers and preliminary rounds, and AET/PEN fixtures (their statistics include extra time).
UCL fixtures on or after 21 Jan 2025 are the locked European holdout: counted, never parsed or mapped.

    python scripts/extract_api_football_xg.py

Writes data/feature_cache/api_football_xg/xg_matches.csv (git-ignored) and the coverage report
evaluation/c6_xg/extraction_summary.json (counts and the unmapped list; no xG values and no results).
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import sys
from urllib.parse import urlencode

import pandas as pd

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO))

CACHE = REPO / '.football_cache'
OUT = REPO / 'data' / 'feature_cache' / 'api_football_xg'
SUMMARY = REPO / 'evaluation' / 'c6_xg' / 'extraction_summary.json'
ALIASES = REPO / 'evaluation' / 'c6_xg' / 'api_football_team_aliases.json'
LEAGUES = ('EPL', 'LaLiga', 'Bundesliga', 'SerieA', 'Ligue1', 'UCL')
DOMESTIC_SEASONS = ('2223', '2324', '2425')
EUROPEAN_HOLDOUT_START = pd.Timestamp('2025-01-21', tz='UTC')
LAST_ALLOWED = pd.Timestamp('2025-07-01', tz='UTC')  # the cached seasons end in June 2025; nothing later is read
UCL_KEPT = re.compile(r'(group [a-h]|league stage|round of 16|quarter-finals|semi-finals|final)( - .+)?')
COLUMNS = ['league', 'season', 'date', 'kickoff_utc', 'home', 'away', 'api_fixture_id',
           'home_xg', 'away_xg', 'response_observed_utc', 'response_sha256']


def season_label(start):
    return f'{start % 100:02d}{(start + 1) % 100:02d}'


def scope(league, round_name):
    """'kept' or the reason a fixture's round is left out."""
    name = str(round_name or '').strip().lower()
    if league != 'UCL':
        if name.startswith('regular season'):
            return 'kept'
        return 'play_off' if 'relegation' in name or 'play' in name else 'other_round'
    if 'qualifying' in name or 'preliminary' in name:
        return 'qualifier'
    if 'play-off' in name or 'playoff' in name:
        return 'play_off'
    return 'kept' if UCL_KEPT.fullmatch(name) else 'other_round'


def statistics_response(state, fixture_id):
    """(payload, observed, sha256) of the cached statistics response, or None."""
    query = '/fixtures/statistics?' + urlencode([('fixture', fixture_id)])
    path = state / 'responses' / (hashlib.sha256(query.encode()).hexdigest() + '.json')
    if not path.exists():
        return None
    row = json.loads(path.read_text(encoding='utf-8'))
    if row.get('query') != query:
        raise ValueError(f'{path.name}: cached response is for another query')
    return json.loads(row['payload']), row['observed'], hashlib.sha256(row['payload'].encode()).hexdigest()


def expected_goals(payload, match):
    """(home xG, away xG), or the reason they are unavailable."""
    if payload.get('unavailable'):
        return 'response_unavailable'
    response = payload.get('response')
    if not isinstance(response, list) or len(response) != 2:
        return 'response_not_two_teams'
    by_team = {r.get('team', {}).get('id'): r for r in response}
    out = []
    for side in ('home', 'away'):
        team = by_team.get(match[side]['id'])
        if team is None:
            return 'response_team_mismatch'
        values = [s.get('value') for s in team.get('statistics', []) if s.get('type') == 'expected_goals']
        if len(values) != 1 or values[0] is None:
            return 'xg_missing'
        try:
            value = float(values[0])
        except (TypeError, ValueError):
            return 'xg_invalid'
        if not 0 <= value <= 15:
            return 'xg_invalid'
        out.append(value)
    return tuple(out)


def domestic_history(league):
    import historical_benchmark as hb
    frames = []
    for season in DOMESTIC_SEASONS:
        data, _, _ = hb.load_history(CACHE, league, {'seasons': [season], 'test_end_exclusive': '2025-07-01'})
        frames.append(data.assign(Season=season))
    return pd.concat(frames, ignore_index=True)


def ucl_history():
    """The European harness's UCL results (european_results), cut at the European holdout start on load."""
    import european_results
    frame = european_results.load_with_backfill(str(CACHE), 'UCL', EUROPEAN_HOLDOUT_START)
    frame = frame.loc[frame['Date'] < EUROPEAN_HOLDOUT_START.tz_localize(None)].copy()
    frame['Date'] = pd.to_datetime(frame['Date']).dt.normalize()
    return frame


def team_names(history, league, matches):
    """Provider team ID -> training name, and how each was resolved. In order: the live integration's check
    (api_football_integration.mappings: unique canonical name or the reviewed team map), the research model's
    reviewed resolver (team_research.history_team; every provider spelling of the ID must agree), then the
    reviewed pairs in evaluation/c6_xg/api_football_team_aliases.json. No close matching; a training name
    claimed by two provider IDs is dropped for both."""
    import api_football_integration as afi
    import team_research
    teams = sorted(set(history['HomeTeam']) | set(history['AwayTeam']))
    spellings = defaultdict(set)
    for observation in matches:
        for side in ('home', 'away'):
            spellings[str(observation['payload'][side]['id'])].add(observation['payload'][side]['name'])
    names = {k: (v, 'integration_check') for k, v in afi.mappings(history, str(CACHE), league, matches).items()}
    reviewed = json.loads(ALIASES.read_text(encoding='utf-8')).get(league, {})
    for entity, options in spellings.items():
        if entity in names:
            continue
        found = {team_research.history_team(o, teams, league) for o in options}
        if len(found) == 1 and None not in found:
            names[entity] = (found.pop(), 'history_team')
        elif entity in reviewed:
            if reviewed[entity] not in teams:
                raise ValueError(f'{league} reviewed alias {entity} -> {reviewed[entity]} is not a training name')
            names[entity] = (reviewed[entity], 'reviewed_alias')
    claimed = Counter(v for v, _ in names.values())
    return {k: v for k, v in names.items() if claimed[v[0]] == 1}


def extract(league, cutoff):
    import api_football_integration as afi
    from football_value_pipeline_v2_standalone import canonical_team_key
    state = CACHE / 'api_football' / 'state'
    counts, failures, rows = Counter(), [], []
    matches = [m for m in afi.records(str(CACHE), league, cutoff) if m['league'] == league]
    history = ucl_history() if league == 'UCL' else domestic_history(league)
    eligible = []
    for observation in matches:
        m = observation['payload']
        kick = pd.Timestamp(m['kickoff_utc'])
        counts['fixtures_cached'] += 1
        if league == 'UCL' and kick >= EUROPEAN_HOLDOUT_START:
            counts['european_holdout_not_read'] += 1
            continue
        if kick >= LAST_ALLOWED:
            counts['after_cached_seasons_not_read'] += 1
            continue
        reason = scope(league, m.get('round'))
        if reason != 'kept':
            counts['excluded_' + reason] += 1
            continue
        if m['status'] != 'FT':
            counts['excluded_extra_time_or_penalties' if m['status'] in ('AET', 'PEN') else 'excluded_not_finished'] += 1
            continue
        eligible.append(observation)
    resolved = team_names(history, league, eligible)
    names = {k: v for k, (v, _) in resolved.items()}
    counts.update('teams_by_' + how for _, how in resolved.values())
    index = {}
    for r in history.itertuples(index=False):
        key = (pd.Timestamp(r.Date).date().isoformat(), canonical_team_key(r.HomeTeam), canonical_team_key(r.AwayTeam))
        index.setdefault(key, []).append(r)
    for observation in eligible:
        m = observation['payload']
        kick = pd.Timestamp(m['kickoff_utc'])
        base = {'league': league, 'season': season_label(m['season']), 'api_fixture_id': m['id'],
                'kickoff_utc': m['kickoff_utc'], 'api_home': m['home']['name'], 'api_away': m['away']['name']}
        cached = statistics_response(state, m['id'])
        if cached is None:
            counts['xg_not_cached_yet'] += 1
            continue
        payload, observed, digest = cached
        if pd.Timestamp(observed) > pd.Timestamp(cutoff):
            counts['xg_not_cached_yet'] += 1
            continue
        xg = expected_goals(payload, m)
        if isinstance(xg, str):
            counts['xg_' + xg if not xg.startswith('xg_') else xg] += 1
            continue
        counts['xg_cached'] += 1
        mapped = [names.get(str(m[s]['id'])) for s in ('home', 'away')]
        if not all(mapped):
            failures.append({**base, 'reason': 'team_not_mapped',
                             'unmapped': [m[s]['name'] for s, n in zip(('home', 'away'), mapped) if not n]})
            continue
        day = kick.date().isoformat()
        found = index.get((day, canonical_team_key(mapped[0]), canonical_team_key(mapped[1])), [])
        if len(found) != 1:
            failures.append({**base, 'reason': 'no_history_row_on_date' if not found else 'duplicate_history_row',
                             'home': mapped[0], 'away': mapped[1]})
            continue
        row = found[0]
        if (int(row.FTHG), int(row.FTAG)) != (m['score']['home'], m['score']['away']):
            failures.append({**base, 'reason': 'score_disagrees_with_history', 'home': row.HomeTeam, 'away': row.AwayTeam})
            continue
        counts['mapped'] += 1
        rows.append({'league': league, 'season': base['season'], 'date': day, 'kickoff_utc': m['kickoff_utc'],
                     'home': row.HomeTeam, 'away': row.AwayTeam, 'api_fixture_id': m['id'],
                     'home_xg': xg[0], 'away_xg': xg[1], 'response_observed_utc': observed, 'response_sha256': digest})
    history_rows = Counter(str(s) for s in history['Season']) if 'Season' in history else Counter()
    return rows, counts, failures, history_rows


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument('--cutoff', default='2026-11-23T12:00:00+00:00',
                   help='Use only observations and responses received at or before this time (frozen snapshot)')
    args = p.parse_args(argv)
    all_rows, report = [], {'cutoff_utc': args.cutoff, 'api_football_requests': 0, 'leagues': {}}
    for league in LEAGUES:
        rows, counts, failures, history_rows = extract(league, args.cutoff)
        all_rows += rows
        frame = pd.DataFrame(rows, columns=COLUMNS)
        by_season = {}
        for season in sorted({*frame['season'], *[f.get('season') for f in failures]} - {None}):
            part = frame.loc[frame.season == season]
            by_season[season] = {'mapped_with_xg': int(len(part)),
                                 'first_date': part['date'].min() if len(part) else None,
                                 'last_date': part['date'].max() if len(part) else None,
                                 'failed_to_map': sum(f['season'] == season for f in failures)}
        months = Counter(d[:7] for d in frame['date'])
        report['leagues'][league] = {'counts': dict(sorted(counts.items())), 'by_season': by_season,
                                     'by_month': dict(sorted(months.items())), 'failed_to_map': failures}
        print(league, json.dumps(dict(sorted(counts.items()))), flush=True)
    table = pd.DataFrame(all_rows, columns=COLUMNS).sort_values(['date', 'league', 'home']).reset_index(drop=True)
    if table.duplicated(['league', 'date', 'home', 'away']).any():
        raise ValueError('Duplicate mapped match')
    OUT.mkdir(parents=True, exist_ok=True)
    text = table.to_csv(index=False, lineterminator='\n')
    (OUT / 'xg_matches.csv').write_text(text, encoding='utf-8', newline='')
    report['table'] = {'path': 'data/feature_cache/api_football_xg/xg_matches.csv', 'rows': int(len(table)),
                       'sha256': hashlib.sha256(text.encode('utf-8')).hexdigest(),
                       'first_date': table['date'].min(), 'last_date': table['date'].max()}
    SUMMARY.parent.mkdir(parents=True, exist_ok=True)
    SUMMARY.write_text(json.dumps(report, indent=1, default=str) + '\n', encoding='utf-8', newline='\n')
    print(json.dumps(report['table'], indent=1))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
