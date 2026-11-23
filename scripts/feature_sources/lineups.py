"""Item 3: lineups and missing players: how far back, how complete, known before kickoff or not.

A  The pipeline's own pre-kickoff ESPN evidence (team_research_json in every committed version of
   football_output_v2/raw/all_leagues_predictions.csv): per fixture, the last observation before kickoff, whether it
   held an injury/suspension list, a roster, and both XIs explicitly confirmed, and how long before kickoff it was taken.
   This is the only source here with a verified pre-kickoff timestamp.
B  ESPN match summaries after the match (soccerdata's ESPN reader reads the same endpoint), a fixed sample per league
   and season from the team schedules cached by rest_days.py, plus 2025/26: starters, bench, formation, injury list.
C  Sofascore through soccerdata (schedule, then the event lineups endpoint, which carries missingPlayers).
D  FotMob: soccerdata 2026.43.0 has no FotMob reader; four direct requests at most (a FotMob xG check runs separately
   from this machine), recorded as made.

Caches: data/feature_cache/lineups/{espn,sofascore,fotmob}.  No result or odds field is used.
"""
from __future__ import annotations

import io
import json
import random
import subprocess
import sys
import time
from collections import Counter
from pathlib import Path

import pandas as pd
import requests

sys.path.insert(0, str(Path(__file__).resolve().parent))
import common as c  # noqa: E402

LINEUPS = c.FEATURE_CACHE / 'lineups'
PRED = 'football_output_v2/raw/all_leagues_predictions.csv'
ESPN = 'https://site.api.espn.com/apis/site/v2/sports/soccer/'
SEED = 20261123
UA = {'User-Agent': 'football-research-check/1.0'}


# ---------------------------------------------------------------------------
# A: pipeline's pre-kickoff evidence
# ---------------------------------------------------------------------------

def git(*args):
    return subprocess.run(['git', '-C', str(c.REPO), *args], capture_output=True, check=True, stdin=subprocess.DEVNULL).stdout


def part_a():
    commits = [line.split(' ', 1) for line in git('log', '--format=%H %cI', '--', PRED).decode().split('\n') if line]
    latest = {}
    for sha, when in commits:
        try:
            frame = pd.read_csv(io.BytesIO(git('show', f'{sha}:{PRED}')), low_memory=False)
        except (subprocess.CalledProcessError, pd.errors.EmptyDataError):
            continue
        if 'team_research_json' not in frame:
            continue
        for r in frame.itertuples(index=False):
            kick = pd.to_datetime(getattr(r, 'kickoff_utc', None), utc=True, errors='coerce')
            raw = getattr(r, 'team_research_json', None)
            if pd.isna(kick) or not isinstance(raw, str):
                continue
            try:
                research = json.loads(raw)
            except ValueError:
                continue
            ev = research.get('evidence') or {}
            summary_obs = [pd.to_datetime(s.get('observed_at_utc'), utc=True, errors='coerce')
                           for s in ev.get('sources', []) if isinstance(s, dict) and '/summary?' in str(s.get('url'))
                           and s.get('status') == 'available']
            summary_obs = [t for t in summary_obs if pd.notna(t) and t < kick]
            observed = max(summary_obs) if summary_obs else pd.to_datetime(research.get('observed_at_utc'), utc=True, errors='coerce')
            if pd.isna(observed) or observed >= kick:
                continue
            squads = ev.get('lineups') or []
            key = (r.league, kick.isoformat(), r.home_team, r.away_team)
            row = {'league': r.league, 'kickoff': kick, 'observed': observed,
                   'minutes_before_kickoff': (kick - observed).total_seconds() / 60,
                   'summary_available': bool(summary_obs), 'identity_verified': bool(ev.get('summary_identity_verified')),
                   'availability_list': bool(ev.get('availability')),
                   'availability_players': sum(len(g.get('players', [])) for g in ev.get('availability') or []),
                   'roster_both': len(squads) == 2,
                   'starters_both_11': len(squads) == 2 and all(sum(p.get('starter') for p in s.get('players', [])) == 11 for s in squads),
                   'xi_confirmed_both': len(squads) == 2 and all(s.get('confirmed') for s in squads)}
            if key not in latest or row['observed'] > latest[key]['observed']:
                latest[key] = row
    df = pd.DataFrame(latest.values())
    if df.empty:
        return {'fixtures': 0}
    df['scope'] = df.league.map(lambda x: 'UCL/UEL' if 'UEFA' in str(x) or x in ('UCL', 'UEL') else 'domestic')
    df.drop(columns=['observed']).to_csv(LINEUPS / 'pipeline_prekickoff_evidence.csv', index=False)

    def stats(p):
        return {'fixtures': int(len(p)), 'first_kickoff': str(p.kickoff.min().date()), 'last_kickoff': str(p.kickoff.max().date()),
                'summary_available_share': round(float(p.summary_available.mean()), 4),
                'availability_list_share': round(float(p.availability_list.mean()), 4),
                'availability_players_mean_when_listed': round(float(p.loc[p.availability_list, 'availability_players'].mean()), 2)
                if p.availability_list.any() else None,
                'roster_both_share': round(float(p.roster_both.mean()), 4),
                'starters_both_11_share': round(float(p.starters_both_11.mean()), 4),
                'xi_confirmed_both_share': round(float(p.xi_confirmed_both.mean()), 4),
                'last_observation_minutes_before_kickoff_median': round(float(p.minutes_before_kickoff.median()), 1),
                'last_observation_within_75_min_share': round(float((p.minutes_before_kickoff <= 75).mean()), 4)}
    return {'committed_versions_read': len(commits), 'all': stats(df),
            'by_scope': {k: stats(p) for k, p in df.groupby('scope')},
            'xi_confirmed_by_minutes_before': {
                b: round(float(p.xi_confirmed_both.mean()), 4) for b, p in
                df.groupby(pd.cut(df.minutes_before_kickoff, [0, 75, 180, 720, 1e9],
                                  labels=['<=75 min', '75 min-3 h', '3-12 h', '>12 h']), observed=True)}}


# ---------------------------------------------------------------------------
# B: ESPN after the match (history depth)
# ---------------------------------------------------------------------------

def espn_get(path, log, delay=1.0):
    folder = LINEUPS / 'espn'
    folder.mkdir(parents=True, exist_ok=True)
    file = folder / (path.replace('/', '_').replace('?', '_').replace('=', '-').replace('&', '_') + '.json')
    if file.exists():
        log['cached'] += 1
        return json.loads(file.read_text(encoding='utf-8'))
    time.sleep(delay)
    try:
        r = requests.get(ESPN + path, timeout=30, headers=UA)
        log[f'http_{r.status_code}'] += 1
        if r.status_code == 200:
            file.write_text(r.text, encoding='utf-8')
            return r.json()
    except (requests.RequestException, ValueError) as exc:
        log[type(exc).__name__] += 1
    return None


def part_b():
    log = Counter()
    rng = random.Random(SEED)
    sched = sorted((c.FEATURE_CACHE / 'rest' / 'espn').glob('all_teams_*_schedule_season-*.json'))
    events = {}
    for f in sched:
        season = int(f.stem.rsplit('-', 1)[1])
        for e in json.loads(f.read_text(encoding='utf-8')).get('events', []):
            slug = (e.get('league') or {}).get('slug')
            if slug in c.ESPN_SLUG.values():
                events.setdefault((slug, season), {})[str(e['id'])] = e.get('date')
    # 2025/26: one ESPN scoreboard week per league (mid-season dates), for the most recent complete season.
    for league, slug in c.ESPN_SLUG.items():
        for day in ('20260221', '20260222'):
            data = espn_get(f'{slug}/scoreboard?dates={day}', log)
            for e in (data or {}).get('events', []):
                events.setdefault((slug, 2025), {})[str(e['id'])] = e.get('date')
    rows = []
    for (slug, season), ids in sorted(events.items()):
        for event_id in rng.sample(sorted(ids), min(3, len(ids))):
            data = espn_get(f'{slug}/summary?event={event_id}', log)
            if not data:
                rows.append({'slug': slug, 'season': season, 'event': event_id, 'summary': False})
                continue
            rosters = data.get('rosters') or []
            starters = [sum(1 for p in (g.get('roster') or []) if p.get('starter')) for g in rosters]
            bench = [sum(1 for p in (g.get('roster') or []) if not p.get('starter')) for g in rosters]
            injuries = data.get('injuries') or []
            rows.append({'slug': slug, 'season': season, 'event': event_id, 'summary': True,
                         'rosters_both': len(rosters) == 2, 'starters_both_11': len(starters) == 2 and starters == [11, 11],
                         'bench_mean': sum(bench) / len(bench) if bench else 0,
                         'formation_both': len(rosters) == 2 and all(g.get('formation') for g in rosters),
                         'injury_list_any': any((g.get('injuries') or []) for g in injuries),
                         'injury_players': sum(len(g.get('injuries') or []) for g in injuries)})
    df = pd.DataFrame(rows)
    df.to_csv(LINEUPS / 'espn_history_sample.csv', index=False)
    by = {}
    for season, p in df.groupby('season'):
        ok = p.loc[p.summary]
        by[f'{season}/{str(season + 1)[-2:]}'] = {
            'matches': int(len(p)), 'summary_share': round(float(p.summary.mean()), 3),
            'starters_both_11_share': round(float(ok.starters_both_11.mean()), 3) if len(ok) else None,
            'formation_both_share': round(float(ok.formation_both.mean()), 3) if len(ok) else None,
            'bench_players_mean': round(float(ok.bench_mean.mean()), 1) if len(ok) else None,
            'injury_list_share': round(float(ok.injury_list_any.mean()), 3) if len(ok) else None}
    return {'by_season': by, 'requests': dict(log)}


# ---------------------------------------------------------------------------
# C: Sofascore via soccerdata
# ---------------------------------------------------------------------------

def part_c():
    out = {}
    try:
        import soccerdata as sd
        out['soccerdata_version'] = sd.__version__
        reader = sd.Sofascore(leagues='ENG-Premier League', seasons='2526', data_dir=LINEUPS / 'sofascore')
        sched = reader.read_schedule()
        out['schedule'] = {'status': 'available', 'rows': int(len(sched))}
        game = sched.dropna(subset=['game_id']).iloc[-1]
        r = requests.get(f"https://api.sofascore.com/api/v1/event/{int(game['game_id'])}/lineups", timeout=30, headers=UA)
        out['lineups_endpoint'] = {'http': r.status_code,
                                   'has_missing_players': 'missingPlayers' in r.text if r.status_code == 200 else None}
    except Exception as exc:
        out.setdefault('schedule', {'status': 'unavailable', 'error': f'{type(exc).__name__}: {exc}'[:300]})
    return out


# ---------------------------------------------------------------------------
# D: FotMob (at most four requests)
# ---------------------------------------------------------------------------

def part_d():
    folder = LINEUPS / 'fotmob'
    folder.mkdir(parents=True, exist_ok=True)
    out = {'soccerdata_reader': 'none in soccerdata 2026.43.0', 'requests': []}
    session = requests.Session()
    headers = {**UA, 'Accept': 'application/json'}

    def get(url, name):
        time.sleep(3)
        try:
            r = session.get(url, timeout=30, headers=headers)
            out['requests'].append({'url': url, 'http': r.status_code, 'bytes': len(r.content),
                                    'json': r.headers.get('content-type', '').startswith('application/json')})
            if r.status_code == 200:
                (folder / name).write_bytes(r.content)
                try:
                    return r.json()
                except ValueError:
                    return None
        except requests.RequestException as exc:
            out['requests'].append({'url': url, 'error': type(exc).__name__})
        return None
    league = get('https://www.fotmob.com/api/leagues?id=47&ccode3=GBR', 'league_47.json')
    ids = []
    if isinstance(league, dict):
        all_matches = (league.get('fixtures') or {}).get('allMatches') or league.get('matches', {}).get('allMatches') or []
        ids = [m['id'] for m in all_matches if (m.get('status') or {}).get('finished')][-2:]
    else:
        ids = ['4813616']  # a 2025/26 Premier League match id, used only if the league call fails
    for match_id in ids[:3]:
        data = get(f'https://www.fotmob.com/api/matchDetails?matchId={match_id}', f'match_{match_id}.json')
        if isinstance(data, dict):
            lineup = (data.get('content') or {}).get('lineup') or {}
            out.setdefault('matches', []).append({
                'match_id': match_id, 'lineup_present': bool(lineup),
                'unavailable_present': any('unavailable' in json.dumps(lineup.get(s, {})) for s in ('homeTeam', 'awayTeam'))})
    return out


def main():
    LINEUPS.mkdir(parents=True, exist_ok=True)
    result = {'A_pipeline_prekickoff_espn': part_a(), 'B_espn_history': part_b(),
              'C_sofascore_soccerdata': part_c(), 'D_fotmob_direct': part_d()}
    c.write_json(c.OUT / 'lineups.json', result)
    print(json.dumps(result, indent=1, default=str))


if __name__ == '__main__':
    raise SystemExit(main())
