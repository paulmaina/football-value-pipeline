"""Historical Understat match xG for the harness (candidate C3; docs/plan.md, Phase 2d).

Reads the files written by scripts/fetch_understat_history.py
(.football_cache/understat/{slug}_{year}.json, checked against manifest.json),
maps Understat team names to football-data names through the reviewed
`understat_team_aliases.json` (exact names need no entry; never fuzzy matching),
and attaches each match's xG to the football-data row of the same match as
`HxG` / `AxG`, the columns team_research.form_history already reads.

A football-data row gets xG only when exactly one Understat result has the same
two teams, a kickoff date within one day (Understat times are UTC, football-data
dates are local) and the same final score. Anything else is left without xG and
counted, so a wrong identity can never move a forecast.

The Understat files hold no odds. Understat's own 'forecast' field (its xG
win probabilities) is never read.
"""
from __future__ import annotations

from collections import Counter
import hashlib
import json
from pathlib import Path

import pandas as pd

ALIASES = Path(__file__).with_name('understat_team_aliases.json')
LEAGUES = {'EPL': 'EPL', 'LaLiga': 'La_liga', 'Bundesliga': 'Bundesliga', 'SerieA': 'Serie_A', 'Ligue1': 'Ligue_1'}
COLUMNS = ['understat_id', 'season', 'kickoff_utc', 'date', 'home', 'away', 'home_goals', 'away_goals',
           'home_xg', 'away_xg']


def directory(cache) -> Path:
    return Path(cache) / 'understat'


def manifest(cache) -> dict:
    path = directory(cache) / 'manifest.json'
    return json.loads(path.read_text(encoding='utf-8')) if path.exists() else {'files': {}, 'missing': {}}


def files(cache, league) -> list[Path]:
    """The league's season files listed in the manifest, each verified against its sha256."""
    slug = LEAGUES.get(league)
    out = []
    for key, entry in sorted(manifest(cache)['files'].items()):
        if entry.get('understat_league') != slug:
            continue
        path = directory(cache) / entry['file']
        if hashlib.sha256(path.read_bytes()).hexdigest() != entry['file_sha256']:
            raise ValueError(f'Understat file {path.name} does not match its manifest sha256')
        out.append(path)
    return out


def raw_matches(cache, league) -> pd.DataFrame:
    """Completed Understat matches for one league, Understat names."""
    rows = []
    for path in files(cache, league):
        for m in json.loads(path.read_text(encoding='utf-8')):
            if not m.get('isResult'):
                continue
            kick = pd.Timestamp(m['datetime'], tz='UTC')
            rows.append({'understat_id': str(m['id']), 'season': path.stem.rsplit('_', 1)[1],
                         'kickoff_utc': kick, 'date': kick.tz_localize(None).normalize(),
                         'home': m['h']['title'], 'away': m['a']['title'],
                         'home_goals': int(m['goals']['h']), 'away_goals': int(m['goals']['a']),
                         'home_xg': float(m['xG']['h']), 'away_xg': float(m['xG']['a'])})
    frame = pd.DataFrame(rows, columns=COLUMNS)
    if frame.understat_id.duplicated().any():
        raise ValueError(f'Duplicate Understat match id in {league}')
    return frame


def aliases(league, path=ALIASES) -> dict:
    data = json.loads(Path(path).read_text(encoding='utf-8')) if Path(path).exists() else {}
    return dict(data.get('leagues', {}).get(league, {}))


def matches(cache, league, alias_path=ALIASES) -> pd.DataFrame:
    """Completed Understat matches with team names restated in football-data spelling."""
    frame = raw_matches(cache, league)
    table = aliases(league, alias_path)
    for side in ('home', 'away'):
        frame['understat_' + side] = frame[side]
        frame[side] = frame[side].map(lambda t: table.get(t, t))
    return frame


def attach_xg(data, xg) -> tuple[pd.DataFrame, Counter]:
    """`data` (football-data rows) with HxG/AxG from the one Understat result of the same match."""
    out = data.copy()
    out['HxG'], out['AxG'] = float('nan'), float('nan')
    counts = Counter()
    if xg is None or xg.empty:
        counts['no_understat_file'] = len(out)
        return out, counts
    index = {}
    for i, r in enumerate(xg.itertuples(index=False)):
        index.setdefault((r.home, r.away), []).append(i)
    used = Counter()
    picks = {}
    for idx, row in out.iterrows():
        near = [i for i in index.get((row.HomeTeam, row.AwayTeam), [])
                if abs((xg.date.iat[i] - row.Date).days) <= 1]
        if not near:
            counts['no_understat_match'] += 1
            continue
        if len(near) > 1:
            counts['ambiguous'] += 1
            continue
        i = near[0]
        if (xg.home_goals.iat[i], xg.away_goals.iat[i]) != (row.FTHG, row.FTAG):
            counts['score_mismatch'] += 1
            continue
        picks[idx] = i
        used[i] += 1
    for idx, i in picks.items():
        if used[i] > 1:  # one Understat match claimed by two rows: trust neither
            counts['ambiguous'] += 1
            continue
        out.at[idx, 'HxG'], out.at[idx, 'AxG'] = xg.home_xg.iat[i], xg.away_xg.iat[i]
        counts['attached'] += 1
    counts['understat_unused'] = len(xg) - sum(1 for i in used if used[i] == 1)
    return out, counts


def with_xg(data, cache, league, alias_path=ALIASES) -> tuple[pd.DataFrame, Counter]:
    """The league's history with Understat xG where available (none outside the five leagues)."""
    if league not in LEAGUES:
        out = data.copy()
        out['HxG'], out['AxG'] = float('nan'), float('nan')
        return out, Counter({'league_without_understat': len(out)})
    return attach_xg(data, matches(cache, league, alias_path))


def propose_aliases(xg_raw, data) -> dict:
    """Review aid only: for each Understat team, the football-data team it lines up with on the
    same date (within a day) and score, with the share of its matches that agree. Never used to
    attach xG; reviewed entries go into understat_team_aliases.json by hand."""
    tally = {}
    by_day = {}
    for r in data.itertuples(index=False):
        by_day.setdefault((r.Date, r.FTHG, r.FTAG), []).append(r)
    for r in xg_raw.itertuples(index=False):
        hits = [f for d in (-1, 0, 1)
                for f in by_day.get((r.date + pd.Timedelta(days=d), r.home_goals, r.away_goals), [])]
        for side, fd_side in (('home', 'HomeTeam'), ('away', 'AwayTeam')):
            team = getattr(r, side)
            entry = tally.setdefault(team, Counter())
            entry['_matches'] += 1
            for f in hits:
                entry[getattr(f, fd_side)] += 1
    out = {}
    for team, entry in tally.items():
        n = entry.pop('_matches')
        best, hits = entry.most_common(1)[0] if entry else (None, 0)
        out[team] = {'football_data': best, 'agreeing_matches': hits, 'understat_matches': n}
    return out
