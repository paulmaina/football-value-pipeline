"""Backfill ESPN's all-competition team schedules for every club in the eight domestic leagues, 2016/17 on.

For the C6-plus-rest candidate (docs/plan.md, Phase 2h). For each league and season (ESPN season = start year):

  1. The league's clubs that season from ESPN's standings (its team list ignores `season`), mapped to the
     football-data.co.uk names of the clubs that played in it: team_research.history_team (the reviewed resolver),
     then the pipeline's normalised name, then the manual pairs in evaluation/c6_rest/espn_team_aliases.json. No close
     matching. The map is written to evaluation/c6_rest/espn_team_map.csv (committed, reviewable); clubs left
     unmapped are listed with a suggestion for review, never applied.
  2. Each mapped club's ESPN schedule that season (league, cups, super cups, UEFA competitions and qualifiers,
     friendlies), cached COMPACT in data/feature_cache/espn_schedules/<espn id>_<season>.json: event id, kickoff,
     competition slug, completed flag and status name, the club's side and the opponent's id. No score or any other
     result field is stored, so the cache holds fixture dates only and can never leak a result.

The cache is git-ignored (data/feature_cache/). Requests are spaced (default 1 s) and retried on 429/5xx.

    python scripts/backfill_espn_schedules.py                   # every league, 2016/17 to the current season
    python scripts/backfill_espn_schedules.py --leagues EPL --seasons 2016 2017
"""
from __future__ import annotations

import argparse
from collections import Counter
import difflib
from datetime import datetime, timezone
import json
from pathlib import Path
import sys
import time

import pandas as pd
import requests

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO))
sys.path.insert(0, str(REPO / 'scripts' / 'feature_sources'))

import common as fs  # noqa: E402  (scripts/feature_sources/common.py: identity-only loaders)

ESPN = 'https://site.api.espn.com/apis/site/v2/sports/soccer/'
ESPN_V2 = 'https://site.api.espn.com/apis/v2/sports/soccer/'
CACHE = REPO / 'data' / 'feature_cache' / 'espn_schedules'
OUT = REPO / 'evaluation' / 'c6_rest'
TEAM_MAP = OUT / 'espn_team_map.csv'
FIRST_SEASON = 2016
SCHEMA = 'espn-schedule-compact-v1'
UA = {'User-Agent': 'football-research-backfill/1.0'}


class Client:
    def __init__(self, delay=1.0):
        self.session = requests.Session()
        self.delay = delay
        self.log = Counter()
        self.failed = []

    def get_v2(self, path):
        return self.get(path, base=ESPN_V2)

    def get(self, path, base=ESPN):
        for attempt in range(4):
            time.sleep(self.delay * (1 + 3 * attempt))
            try:
                r = self.session.get(base + path, timeout=30, headers=UA)
            except requests.RequestException as exc:
                self.log[type(exc).__name__] += 1
                continue
            self.log[f'http_{r.status_code}'] += 1
            if r.status_code == 200:
                try:
                    return r.json()
                except ValueError:
                    self.log['bad_json'] += 1
                    return None
            if r.status_code not in (429, 500, 502, 503, 504):
                break
        self.failed.append(path)
        return None


def compact(payload, team_id) -> list:
    """The schedule without any result: one dict per event."""
    out = []
    for e in (payload or {}).get('events', []):
        comp = (e.get('competitions') or [{}])[0]
        status = (comp.get('status') or e.get('status') or {}).get('type', {})
        side, opponent = None, None
        for c in comp.get('competitors', []):
            if str((c.get('team') or {}).get('id')) == str(team_id):
                side = c.get('homeAway')
            else:
                opponent = str((c.get('team') or {}).get('id'))
        out.append({'id': str(e.get('id')), 'date': e.get('date'),
                    'slug': (e.get('league') or {}).get('slug') or '',
                    'completed': bool(status.get('completed')), 'status': status.get('name'),
                    'side': side, 'opponent_id': opponent})
    return out


def fold(name) -> str:
    """Accent- and case-free spelling, for the manual aliases only."""
    import unicodedata
    return unicodedata.normalize('NFKD', str(name)).encode('ascii', 'ignore').decode().casefold().strip()


def norm(name):
    from football_value_pipeline_v2_standalone import normalize_team_name
    return normalize_team_name(str(name))


ALIASES = OUT / 'espn_team_aliases.json'


def load_aliases() -> dict:
    """{league: {ESPN display name: football-data name}}: manual pairs, each checked by hand against the season's
    standings (same league, same season, plainly the same club). Never fuzzy."""
    if not ALIASES.exists():
        return {}
    return json.loads(ALIASES.read_text(encoding='utf-8'))['aliases']


def map_teams(espn_teams, names, league, aliases=None):
    """football-data name -> (ESPN id, ESPN name, method) for one league-season: the reviewed resolver
    (team_research.history_team), then the pipeline's normalised name (unique), then the manual aliases. No close
    matching: a club never gets another club's schedule. Never two ESPN clubs to one name or the reverse."""
    from team_research import history_team
    aliases = {fold(k): v for k, v in (aliases or {}).get(league, {}).items()}
    normed = {}
    for n in names:
        normed.setdefault(norm(n), []).append(n)
    found, taken = [], set()
    for method in ('reviewed', 'normalised', 'alias'):
        for t in espn_teams:
            tid = str(t['id'])
            if any(tid == f[1] for f in found):
                continue
            labels = [x for x in (t.get('displayName'), t.get('shortDisplayName'), t.get('name'), t.get('location')) if x]
            hit = None
            for label in labels:
                if method == 'reviewed':
                    hit = history_team(label, names, league)
                elif method == 'normalised':
                    cands = normed.get(norm(label), [])
                    hit = cands[0] if len(cands) == 1 else None
                else:
                    hit = aliases.get(fold(label)) if aliases.get(fold(label)) in names else None
                if hit and hit not in taken:
                    break
                hit = None
            if hit:
                taken.add(hit)
                found.append((hit, tid, t.get('displayName'), method))
    return found


def standings_teams(client, slug, season) -> list:
    """The league's clubs that season, from ESPN's standings (the team list endpoint ignores `season` and returns
    the current clubs)."""
    data = client.get_v2(f'{slug}/standings?season={season}')
    out = []

    def walk(node):
        for e in ((node.get('standings') or {}).get('entries') or []):
            out.append(e['team'])
        for child in node.get('children') or []:
            walk(child)
    if data:
        walk(data)
    seen, unique = set(), []
    for t in out:
        if str(t['id']) not in seen:
            seen.add(str(t['id']))
            unique.append(t)
    return unique


def season_code(season):
    return f'{str(season)[-2:]}{str(season + 1)[-2:]}'


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument('--leagues', nargs='*', default=list(fs.CODES.values()))
    p.add_argument('--seasons', nargs='*', type=int)
    p.add_argument('--delay', type=float, default=1.0)
    p.add_argument('--map-only', action='store_true', help='map clubs only; fetch no schedule')
    args = p.parse_args(argv)
    domestic = fs.domestic_matches()
    latest = max(int('20' + s[:2]) for s in domestic.season.unique())
    seasons = args.seasons or list(range(FIRST_SEASON, latest + 1))
    CACHE.mkdir(parents=True, exist_ok=True)
    OUT.mkdir(parents=True, exist_ok=True)
    client = Client(args.delay)
    aliases = load_aliases()
    previous = pd.read_csv(TEAM_MAP, dtype=str) if TEAM_MAP.exists() else pd.DataFrame()
    rows, unmapped, fetched, cached = [], [], 0, 0
    for league in args.leagues:
        slug = fs.ESPN_SLUG[league]
        for season in seasons:
            part = domestic.loc[(domestic.league == league) & (domestic.season == season_code(season))]
            names = sorted(set(part.HomeTeam) | set(part.AwayTeam))
            if not names:
                continue
            teams = standings_teams(client, slug, season)
            found = map_teams(teams, names, league, aliases)
            for fd_name, tid, espn_name, method in found:
                rows.append({'league': league, 'season': season, 'fd_team': fd_name, 'espn_id': tid,
                             'espn_name': espn_name, 'method': method})
                file = CACHE / f'{tid}_{season}.json'
                if args.map_only:
                    continue
                if file.exists():
                    cached += 1
                    continue
                payload = client.get(f'all/teams/{tid}/schedule?season={season}')
                if payload is None:
                    continue
                file.write_text(json.dumps({'schema': SCHEMA, 'espn_id': tid, 'season': season,
                                            'fetched_at_utc': datetime.now(timezone.utc).isoformat(),
                                            'events': compact(payload, tid)}), encoding='utf-8')
                fetched += 1
            mapped, mapped_ids = {f[0] for f in found}, {f[1] for f in found}
            spare = [t.get('displayName') for t in teams if str(t['id']) not in mapped_ids]
            for n in names:
                if n not in mapped:
                    # A suggestion for the manual alias review only; never applied.
                    hint = difflib.get_close_matches(norm(n), [norm(s) for s in spare], n=1, cutoff=0.5)
                    unmapped.append({'league': league, 'season': season, 'fd_team': n,
                                     'unmapped_espn_clubs': spare,
                                     'suggestion': next((s for s in spare if hint and norm(s) == hint[0]), None)})
            print(f'{league} {season}: {len(found)}/{len(names)} mapped', flush=True)
    new = pd.DataFrame(rows)
    if not previous.empty and args.seasons:  # a partial run keeps the other league-seasons' rows
        keep = ~previous.set_index(['league', 'season']).index.isin(
            list(new.set_index(['league', 'season']).index.unique()) if len(new) else [])
        new = pd.concat([previous.loc[keep].astype({'season': int}), new], ignore_index=True)
    new = new.sort_values(['league', 'season', 'fd_team']).reset_index(drop=True)
    new.to_csv(TEAM_MAP, index=False)
    files = sorted(CACHE.glob('*_*.json'))
    summary = {'schema': SCHEMA, 'run_at_utc': datetime.now(timezone.utc).isoformat(),
               'leagues': args.leagues, 'seasons': seasons, 'team_seasons_mapped': int(len(new)),
               'mapping_methods': new.method.value_counts().to_dict(), 'unmapped_fd_teams': unmapped,
               'schedules_fetched_this_run': fetched, 'schedules_already_cached': cached,
               'schedule_files_in_cache': len(files), 'requests': dict(client.log), 'failed_requests': client.failed}
    (OUT / 'backfill_summary.json').write_text(json.dumps(summary, indent=1) + '\n', encoding='utf-8')
    print(json.dumps({k: v for k, v in summary.items() if k != 'unmapped_fd_teams'}, indent=1))
    print('unmapped:', unmapped)
    return 1 if client.failed else 0


if __name__ == '__main__':
    raise SystemExit(main())
