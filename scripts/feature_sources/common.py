"""Shared loaders for the feature-source investigation (scripts/feature_sources).

Investigation only: nothing here is imported by the pipeline, the harness or the research model.
Every loader returns dates and team names only. No goal, result or odds column is read, so no
holdout score is touched; holdout fixtures are counted by identity only, as the plan's European
holdout counting does.
"""
from __future__ import annotations

import io
import json
from pathlib import Path
import sys

import pandas as pd

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO))
CACHE = REPO / '.football_cache'
FEATURE_CACHE = REPO / 'data' / 'feature_cache'
OUT = REPO / 'evaluation' / 'feature_sources_check'

CODES = {'E0': 'EPL', 'SP1': 'LaLiga', 'D1': 'Bundesliga', 'I1': 'SerieA', 'F1': 'Ligue1',
         'N1': 'Eredivisie', 'P1': 'PrimeiraLiga', 'T1': 'SuperLig'}
COUNTRY = {'EPL': 'ENG', 'LaLiga': 'ESP', 'Bundesliga': 'GER', 'SerieA': 'ITA', 'Ligue1': 'FRA',
           'Eredivisie': 'NED', 'PrimeiraLiga': 'POR', 'SuperLig': 'TUR'}
ESPN_SLUG = {'EPL': 'eng.1', 'LaLiga': 'esp.1', 'Bundesliga': 'ger.1', 'SerieA': 'ita.1', 'Ligue1': 'fra.1',
             'Eredivisie': 'ned.1', 'PrimeiraLiga': 'por.1', 'SuperLig': 'tur.1'}
HOLDOUT_LEAGUES = ('Eredivisie', 'PrimeiraLiga', 'SuperLig')


def config():
    return json.loads((REPO / 'evaluation_harness_config.json').read_text(encoding='utf-8'))


def period(date, league, cfg=None):
    """The plan's period for a domestic match (dates from evaluation_harness_config.json)."""
    cfg = cfg or config()
    d = pd.Timestamp(date)
    if d < pd.Timestamp(cfg['test_start']):
        return 'warm_up'
    if d <= pd.Timestamp(cfg['development_end']):
        return 'development'
    if d < pd.Timestamp(cfg['holdout_start']):
        return 'validation'
    if d < pd.Timestamp(cfg['holdout_end_exclusive']) and league in cfg['holdout_leagues']:
        return 'holdout'
    return 'retrospective'


def _season_files():
    for folder in (CACHE / 'domestic_backfill', CACHE):
        for path in sorted(folder.glob('[0-9][0-9][0-9][0-9]_*.csv')):
            season, code = path.stem.split('_', 1)
            if code in CODES:
                yield season, code, path


def domestic_matches() -> pd.DataFrame:
    """Every domestic league match in the cached football-data.co.uk files (2015/16 on): Date, kickoff time where
    the file has one, league, season, HomeTeam, AwayTeam. Only identity columns are read."""
    frames = []
    seen = set()
    for season, code, path in _season_files():
        if (season, code) in seen:
            continue
        seen.add((season, code))
        raw = path.read_bytes()
        try:
            text = raw.decode('utf-8-sig')
        except UnicodeDecodeError:
            text = raw.decode('latin1')
        head = pd.read_csv(io.StringIO(text), nrows=0).columns
        use = [c for c in ('Date', 'Time', 'HomeTeam', 'AwayTeam') if c in head]
        frame = pd.read_csv(io.StringIO(text), usecols=use, dtype=str).dropna(subset=['Date', 'HomeTeam', 'AwayTeam'])
        frame['Date'] = pd.to_datetime(frame.Date.str.strip(), format='mixed', dayfirst=True)
        frame['league'] = CODES[code]
        frame['season'] = season
        for side in ('HomeTeam', 'AwayTeam'):
            frame[side] = frame[side].str.strip()
        if 'Time' not in frame:
            frame['Time'] = None
        frames.append(frame[['Date', 'Time', 'league', 'season', 'HomeTeam', 'AwayTeam']])
    out = pd.concat(frames, ignore_index=True)
    return out.drop_duplicates(['Date', 'HomeTeam', 'AwayTeam']).sort_values('Date', kind='stable').reset_index(drop=True)


def european_matches(now='2026-11-23') -> pd.DataFrame:
    """UCL (2015/16 on) and UEL (2020/21 on) as the harness loads them (european_results.load_with_backfill), with
    the goal columns dropped straight away."""
    import european_results as er
    frames = []
    for competition in ('UCL', 'UEL'):
        f = er.load_with_backfill(CACHE, competition, now)
        f = f[['Date', 'HomeTeam', 'AwayTeam', 'Season', 'stage_group']].copy()
        f['competition'] = competition
        frames.append(f)
    out = pd.concat(frames, ignore_index=True)
    out['Date'] = pd.to_datetime(out.Date).dt.tz_localize(None) if out.Date.dt.tz is not None else out.Date
    return out.sort_values('Date', kind='stable').reset_index(drop=True)


def european_identities(european: pd.DataFrame, domestic: pd.DataFrame):
    """European name -> (league, domestic name), with the reviewed resolver and aliases exactly as CE3n links them
    (european_results.scoped_identities, fixture-evidence plus manual reviewed aliases). Names only."""
    import european_backfill as eb
    import european_results as er
    histories = {}
    for league, part in domestic.groupby('league'):
        histories[league] = (part[['Date', 'HomeTeam', 'AwayTeam']], set(part.HomeTeam) | set(part.AwayTeam))
    teams = sorted(set(european.HomeTeam) | set(european.AwayTeam))
    reviewed = eb.load_reviewed_aliases()
    (mapped, ambiguous), _ = er.scoped_identities(teams, histories, eb.load_domestic_aliases(), reviewed['domestic'])
    return mapped, sorted(ambiguous)


def write_json(path: Path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=1, sort_keys=False, default=str) + '\n', encoding='utf-8')
