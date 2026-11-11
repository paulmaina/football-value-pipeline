"""Cached European club results (UCL, UEL) as results-only test matches for evaluation_harness.

Loads each competition's results exactly as the live pipeline trains on them:

  UCL  football-data.org season files (.football_cache/fdorg_history_UCL_<year>.json), read by the
       live loader FootballDataOrg.history in cache-only mode: finished matches, regulation-time
       scores (extra time and penalties removed by match_scores.regulation_goals).
  UEL  the verified snapshot .football_cache/europa/training.json, read by the live loader
       europa_training.frame: OpenFootball reconciled to Fixture Download (2022/23-2024/25), Fixture
       Download matched to UEFA's reviewed facts (2025/26), Cornerflick + Fixture Download
       (2026/27 league phase). Regulation-time scores; reviewed corrections only.

No odds are read: there are no historical European prices, so these are results-only test matches.
The inventory reconciles the cached sources with the existing reviewed reconciliation
(scripts/europa_research.reconcile, audit_cornerflick) and the reviewed aliases only; no fuzzy matching.
"""
from __future__ import annotations

from collections import Counter
from datetime import datetime, timezone
import json
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent
COMPETITIONS = {'UCL': 'UEFA Champions League', 'UEL': 'UEFA Europa League'}
COLUMNS = ['Date', 'HomeTeam', 'AwayTeam', 'FTHG', 'FTAG', 'Season', 'stage', 'stage_group']
STAGE_GROUPS = ('group stage', 'league phase', 'knockout')


def utc(value):
    stamp = pd.Timestamp(value)
    return stamp.tz_localize('UTC') if stamp.tzinfo is None else stamp.tz_convert('UTC')


def ucl_files(cache):
    """The cached football-data.org UCL seasons, oldest first."""
    return sorted(p for p in Path(cache).glob('fdorg_history_UCL_*.json') if p.stem.split('_')[-1].isdigit())


def europa_snapshot(cache):
    return Path(cache) / 'europa' / 'training.json'


def stage_group(competition, stage) -> str:
    """'group stage' (to 2023/24), 'league phase' (from 2024/25) or 'knockout'."""
    text = str(stage or '').strip()
    if competition == 'UCL':
        return {'GROUP_STAGE': 'group stage', 'LEAGUE_STAGE': 'league phase'}.get(text, 'knockout')
    lower = text.lower()
    if lower.startswith(('group', 'gruppe')):
        return 'group stage'
    if lower == 'league phase' or text.isdigit():  # 2025/26 Fixture Download labels league rounds 1-8
        return 'league phase'
    return 'knockout'


def _ucl_stages(cache):
    """(kickoff, home, away) -> stage, from the same files the live loader reads."""
    stages = {}
    for path in ucl_files(cache):
        for m in json.loads(path.read_text(encoding='utf-8-sig')).get('matches', []):
            if isinstance(m, dict) and m.get('status') == 'FINISHED':
                kickoff = pd.to_datetime(m.get('utcDate'), utc=True).tz_convert(None)
                stages[(kickoff, m['homeTeam']['name'], m['awayTeam']['name'])] = m.get('stage')
    return stages


def load(cache, competition, now) -> pd.DataFrame:
    """One competition's completed results before `now`, as the live pipeline trains on them.

    The live loaders validate the cached files against the current clock (a finished match dated in the
    future is rejected); the rows are then cut at `now`, so an earlier cutoff reads the same validated rows."""
    clock = datetime.now(timezone.utc)
    now = utc(now)
    if competition == 'UCL':
        from football_value_pipeline_v2_standalone import LEAGUES, FootballDataOrg, current_season_start_year
        seasons = [int(p.stem.split('_')[-1]) for p in ucl_files(cache)]
        if not seasons:
            raise ValueError('No cached UCL history')
        back = current_season_start_year(clock) - min(seasons) + 1
        frame = FootballDataOrg('', cache_dir=cache, cache_only=True).history(
            LEAGUES['UCL'], seasons_back=back, now=clock)
        frame = frame.loc[frame.Date < now.tz_convert(None)]
        stages = _ucl_stages(cache)
        frame['stage'] = [stages.get((d, h, a)) for d, h, a in zip(frame.Date, frame.HomeTeam, frame.AwayTeam)]
        if frame['stage'].isna().any():
            raise ValueError('UCL result without a stage in the cached files')
    elif competition == 'UEL':
        import europa_training
        payload = json.loads(europa_snapshot(cache).read_text(encoding='utf-8'))
        frame = europa_training.frame(payload, clock)
        frame = frame.loc[frame.Date < now.tz_convert(None)]
        stages = {(r['date'], r['home'], r['away']): r.get('stage') for r in payload['matches']}
        frame['stage'] = [stages.get((d.date().isoformat(), h, a)) for d, h, a in
                          zip(frame.Date, frame.HomeTeam, frame.AwayTeam)]
    else:
        raise KeyError(competition)
    frame['stage_group'] = [stage_group(competition, s) for s in frame['stage']]
    frame['Season'] = frame['Season'].astype(str)
    return frame[COLUMNS].sort_values(['Date', 'HomeTeam', 'AwayTeam'], kind='stable').reset_index(drop=True)


# ---------------------------------------------------------------------------
# Inventory: every cached European result, its source and conflicts
# ---------------------------------------------------------------------------

def _season_rows(frame, competition, source):
    out = []
    for season, part in frame.groupby('Season'):
        out.append({'competition': competition, 'season': f'{season}/{str(int(season) + 1)[-2:]}',
                    'matches': int(len(part)), 'first': part.Date.min().date().isoformat(),
                    'last': part.Date.max().date().isoformat(), 'source': source(season),
                    'stages': {g: int(n) for g, n in Counter(part.stage_group).items()}})
    return out


def ucl_inventory(cache, now):
    """football-data.org only: no second UCL source is cached, so no cross-source check is possible."""
    frame = load(cache, 'UCL', now)
    raw = Counter()
    for path in ucl_files(cache):
        for m in json.loads(path.read_text(encoding='utf-8-sig')).get('matches', []):
            raw[(path.stem.split('_')[-1], m.get('status'), (m.get('score') or {}).get('duration'))] += 1
    rows = _season_rows(frame, 'UCL', lambda s: 'football-data.org (fdorg_history_UCL_%s.json)' % s)
    for row in rows:
        year = row['season'][:4]
        row['finished_after_extra_time'] = sum(n for (y, st, d), n in raw.items()
                                               if y == year and st == 'FINISHED' and d == 'EXTRA_TIME')
        row['finished_after_penalties'] = sum(n for (y, st, d), n in raw.items()
                                              if y == year and st == 'FINISHED' and d == 'PENALTY_SHOOTOUT')
        row['scheduled_not_yet_played'] = sum(n for (y, st, d), n in raw.items() if y == year and st != 'FINISHED')
    return {'seasons': rows, 'total': int(len(frame)),
            'conflicts': 'none checkable: football-data.org is the only cached UCL result source',
            'score_basis': 'regulation time; extra time and penalties removed (match_scores.regulation_goals)',
            'top_up': {'added': 0, 'reason': 'no Cornerflick or Fixture Download UCL file is cached'}}


def uel_inventory(cache, now):
    """Re-run the reviewed reconciliation on the cached sources and compare it with the snapshot."""
    from scripts.europa_research import audit_cornerflick, identity, reconcile, team_resolver
    sources = Path(cache) / 'europa' / 'sources'
    aliases = json.loads((ROOT / 'docs/audits/europa-team-aliases.json').read_text(encoding='utf-8'))
    reviews = json.loads((ROOT / 'docs/audits/europa-regulation-reviews.json').read_text(encoding='utf-8'))
    facts = json.loads((sources / 'uefa-reviewed-facts.json').read_text(encoding='utf-8'))['seasons']['2025']['matches']
    payload = json.loads(europa_snapshot(cache).read_text(encoding='utf-8'))
    history, evidence = reconcile(sources, aliases, reviews, official_rows=facts)
    audit, current = audit_cornerflick(sources, team_resolver(aliases), utc(now).to_pydatetime())
    snapshot = {identity(r): r for r in payload['matches']}
    rebuilt = {identity(r): r for r in history}
    rebuilt.update({identity(r): {**r, 'regulation': r['reported']} for r in current})
    differs = sorted(k for k in set(snapshot) | set(rebuilt)
                     if k not in snapshot or k not in rebuilt
                     or list(snapshot[k]['regulation']) != list(rebuilt[k]['regulation']))
    frame = load(cache, 'UEL', now)
    def label(source):
        return 'Fixture Download matched to UEFA reviewed facts' if source.startswith('https://www.uefa.com/') else source
    sources_by_season = {str(s): Counter(label(r['source']) for r in payload['matches'] if str(r['season']) == str(s))
                         for s in {r['season'] for r in payload['matches']}}
    rows = _season_rows(frame, 'UEL', lambda s: ', '.join(sorted(sources_by_season[str(s)])))
    for row in rows:
        season = row['season'][:4]
        row['regulation_corrections'] = sum(c['season'] == int(season) for c in evidence['regulation_corrections'])
        row['identity_corrections'] = sum(c['date'] >= f'{season}-07-01' and c['date'] < f'{int(season) + 1}-07-01'
                                          for c in evidence['identity_corrections'])
    return {'seasons': rows, 'total': int(len(frame)),
            'snapshot_verified_at_utc': payload['verified_at_utc'],
            'reconciliation': evidence['seasons'],
            'regulation_corrections': len(evidence['regulation_corrections']),
            'identity_corrections': len(evidence['identity_corrections']),
            'snapshot_vs_rebuilt_from_sources': {'differences': [list(k) for k in differs]},
            'cornerflick_2026': {k: audit[k] for k in ('total_rows', 'league_phase_rows', 'unclassified_rows_quarantined',
                                                       'score_conflicts', 'unverified_identities',
                                                       'fixture_download_completed_rows',
                                                       'missing_against_fixture_download', 'latest_result')},
            'conflicts': {'reported_score': len(audit['score_conflicts']),
                          'note': ('The reconciliation stops on any unresolved identity or score conflict. Concluding scores '
                                   'that include extra time are replaced by the reviewed regulation score; one Fixture '
                                   'Download opponent is corrected by a reviewed identity correction.')},
            'top_up': {'added': len([k for k in rebuilt if k not in snapshot]),
                       'reason': ('Every result on which two cached sources agree is already in the snapshot. Cornerflick\'s '
                                  f"{audit['unclassified_rows_quarantined']} unclassified 2026/27 rows (no round label; "
                                  'qualifying rounds, July-August) have no second cached source, so none is added.')}}


def inventory(cache, now):
    return {'UCL': ucl_inventory(cache, now), 'UEL': uel_inventory(cache, now)}


# ---------------------------------------------------------------------------
# Domestic form available for both teams (Phase 2c reach)
# ---------------------------------------------------------------------------

def domestic_identities(teams, histories):
    """European team -> (league, domestic training name), from reviewed identities only.

    Uses team_research.history_team, the live research resolver (exact name, the league's reviewed
    aliases, the global alias table, the canonical key; never fuzzy). A team found in more than one
    domestic league is ambiguous and left out."""
    from team_research import history_team
    out, ambiguous = {}, set()
    for team in teams:
        found = {(league, name) for league, (frame, names) in histories.items()
                 if (name := history_team(team, names, league)) is not None}
        if len(found) == 1:
            out[team] = found.pop()
        elif found:
            ambiguous.add(team)
    return out, ambiguous


def domestic_form_coverage(fixtures, histories, min_matches=5, days=365):
    """Per European fixture: does each team have at least `min_matches` domestic league matches in the
    `days` before the fixture's day (strictly earlier days only)? Reads domestic dates and team names,
    never a score. `histories` maps league -> (frame, team names); pass holdout-free frames."""
    teams = sorted(set(fixtures.HomeTeam) | set(fixtures.AwayTeam))
    mapped, ambiguous = domestic_identities(teams, histories)
    dates = {}
    for team, (league, name) in mapped.items():
        frame = histories[league][0]
        dates[team] = pd.DatetimeIndex(frame.Date.loc[(frame.HomeTeam == name) | (frame.AwayTeam == name)]).sort_values()
    rows = []
    for r in fixtures.itertuples(index=False):
        day = pd.Timestamp(r.Date).normalize()
        counts = []
        for team in (r.HomeTeam, r.AwayTeam):
            d = dates.get(team)
            counts.append(0 if d is None else int(((d < day) & (d >= day - pd.Timedelta(days=days))).sum()))
        rows.append({'home_domestic_matches': counts[0], 'away_domestic_matches': counts[1],
                     'home_league': mapped.get(r.HomeTeam, (None,))[0], 'away_league': mapped.get(r.AwayTeam, (None,))[0],
                     'both': min(counts) >= min_matches, 'one': max(counts) >= min_matches})
    unresolved = Counter(t for t in list(fixtures.HomeTeam) + list(fixtures.AwayTeam) if t not in mapped)
    return pd.DataFrame(rows, index=fixtures.index), {'teams': len(teams), 'mapped_teams': len(mapped),
                                                      'ambiguous_teams': sorted(ambiguous),
                                                      'unmapped_by_appearances': unresolved.most_common()}
