"""Cached European club results (UCL, UEL) as results-only test matches for evaluation_harness.

Loads each competition's results exactly as the live pipeline trains on them:

  UCL  football-data.org season files (.football_cache/fdorg_history_UCL_<year>.json), read by the
       live loader FootballDataOrg.history in cache-only mode: finished matches, regulation-time
       scores (extra time and penalties removed by match_scores.regulation_goals).
  UEL  the verified snapshot .football_cache/europa/training.json, read by the live loader
       europa_training.frame: OpenFootball reconciled to Fixture Download (2022/23-2024/25), Fixture
       Download matched to UEFA's reviewed facts (2025/26), Cornerflick + Fixture Download
       (2026/27 league phase). Regulation-time scores; reviewed corrections only.

The harness reads `load_with_backfill`: older seasons from european_backfill.py (UCL 2015/16-2022/23, UEL
2020/21-2021/22; harness only) followed by exactly what `load` returns, so no cached row changes.

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


def cached_ucl_names(cache) -> set:
    """Every team name in the cached football-data.org UCL files (names only; no score is read)."""
    names = set()
    for path in ucl_files(cache):
        for m in json.loads(path.read_text(encoding='utf-8-sig')).get('matches', []):
            if isinstance(m, dict):
                names |= {m[s]['name'] for s in ('homeTeam', 'awayTeam') if (m.get(s) or {}).get('name')}
    return names


def rename_reviewed(old, current, names):
    """Backfilled UCL rows with the manual reviewed names (docs/audits/european-reviewed-aliases.json): an
    older spelling becomes the football-data.org name, so the club is one team across 2022/23 -> 2023/24.
    Only backfilled rows (all before the European holdout start) are renamed; the target must be a cached
    football-data.org name (`current`) and the source must not be one."""
    import european_backfill as eb
    for source, target in names.items():
        if source in current or target not in current:
            raise ValueError(f'Reviewed UCL alias {source!r} -> {target!r} does not join an older name to a cached one')
    out = old.copy()
    if (out.Date >= pd.Timestamp(eb.LOCK_DATE)).any():
        raise ValueError('A renamed row is on or after the European holdout start')
    for side in ('HomeTeam', 'AwayTeam'):
        out[side] = out[side].map(lambda t: names.get(t, t))
    if (out.HomeTeam == out.AwayTeam).any() or out.duplicated(['Date', 'HomeTeam', 'AwayTeam']).any():
        raise ValueError('A reviewed UCL alias makes a self or duplicate fixture')
    return out


def load_with_backfill(cache, competition, now, reviewed=True) -> pd.DataFrame:
    """The harness's European results: the reconciled backfill (european_backfill.py; older seasons, harness
    only) followed by exactly what live trains on (`load`). Every backfilled match is before the first cached
    one, so the live rows, and every row on or after the European holdout start, are untouched.

    `reviewed` applies the manual reviewed UCL names to the backfilled rows only (rename_reviewed, Phase 2c
    alias review); `reviewed=False` gives the rows as before that review."""
    import european_backfill as eb
    live = load(cache, competition, now)
    old = eb.results(cache, competition)
    old = old.loc[old.Date < utc(now).tz_convert(None)].copy()
    if not old.empty and not live.empty and old.Date.max() >= live.Date.min():
        raise ValueError(f'{competition} backfill overlaps the cached seasons')
    if (old.Date >= pd.Timestamp(eb.LOCK_DATE)).any():
        raise ValueError('A backfilled row is on or after the European holdout start')
    if reviewed and competition == 'UCL':
        old = rename_reviewed(old, cached_ucl_names(cache), eb.load_reviewed_aliases()['ucl_names'])
    old['stage_group'] = [stage_group(competition, s) for s in old['stage']]
    frame = pd.concat([old[COLUMNS], live], ignore_index=True)
    return frame.sort_values(['Date', 'HomeTeam', 'AwayTeam'], kind='stable').reset_index(drop=True)


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


def backfill_inventory(cache):
    """Per competition and season: matches, sources, agreements and conflicts of the backfill."""
    import european_backfill as eb
    frame, report = eb.reconcile(cache)
    aliases = eb.load_aliases()
    return {'seasons': report,
            'total': {c: int((frame.competition == c).sum()) for c in eb.SEASONS},
            'rule': ('A result counts when OpenFootball and Fixture Download agree on the fixture (same teams, dates '
                     'within a day) and the concluding score, or when OpenFootball is the only source (single-source '
                     'season, labelled). Regulation score from OpenFootball\'s explicit periods. Awarded and cancelled '
                     'matches are left out; a conflict would be left out and reported.'),
            'names': {'UCL': aliases['UCL']['evidence'], 'UEL': aliases['UEL']['evidence']},
            'live_rows_unchanged': 'Backfilled rows all precede the cached seasons; load() is unchanged.'}


def inventory(cache, now):
    return {'UCL': ucl_inventory(cache, now), 'UEL': uel_inventory(cache, now), 'backfill': backfill_inventory(cache)}


# ---------------------------------------------------------------------------
# Domestic form available for both teams (Phase 2c reach)
# ---------------------------------------------------------------------------

def load_domestic_backfill(folder, code, seasons):
    """Older football-data.co.uk league files (European domestic-form coverage only; the domestic harness
    never reads them). The same checks as historical_benchmark.load_history, except that a row with every
    field empty (the older files end with one) is dropped and counted. Returns (Date, HomeTeam, AwayTeam)
    rows of completed matches, and the rows dropped."""
    import io
    frames, dropped = [], Counter()
    for season in seasons:
        path = Path(folder) / f'{season}_{code}.csv'
        raw = path.read_bytes()
        try:
            text = raw.decode('utf-8-sig')
        except UnicodeDecodeError:
            text = raw.decode('latin1')
        frame = pd.read_csv(io.StringIO(text), on_bad_lines='error', low_memory=False)
        empty = frame.isna().all(axis=1)
        dropped['empty_rows'] += int(empty.sum())
        frame = frame.loc[~empty].copy()
        if {'Date', 'HomeTeam', 'AwayTeam', 'FTHG', 'FTAG'} - set(frame):
            raise ValueError('Missing columns ' + path.name)
        dates = pd.to_datetime(frame.Date.astype(str).str.strip(), format='mixed', dayfirst=True, errors='coerce')
        if dates.isna().any():
            raise ValueError('Invalid date ' + path.name)
        hg, ag = pd.to_numeric(frame.FTHG, errors='coerce'), pd.to_numeric(frame.FTAG, errors='coerce')
        unfinished = hg.isna() & ag.isna()
        dropped['unfinished_rows'] += int(unfinished.sum())
        if ((hg.isna() != ag.isna()) | (((hg < 0) | (ag < 0) | (hg > 20) | (ag > 20)) & ~unfinished)).any():
            raise ValueError('Invalid goals ' + path.name)
        out = pd.DataFrame({'Date': dates.dt.normalize(), 'HomeTeam': frame.HomeTeam.astype(str).str.strip(),
                            'AwayTeam': frame.AwayTeam.astype(str).str.strip()}).loc[~unfinished]
        if (out.HomeTeam == out.AwayTeam).any() or out[['HomeTeam', 'AwayTeam']].isin(['', 'nan']).any().any():
            raise ValueError('Invalid team identity ' + path.name)
        frames.append(out)
    data = pd.concat(frames, ignore_index=True).sort_values(['Date', 'HomeTeam', 'AwayTeam']).reset_index(drop=True)
    if data.duplicated(['Date', 'HomeTeam', 'AwayTeam']).any():
        raise ValueError('Duplicate fixture in the domestic backfill')
    return data, dict(dropped)


def domestic_identities(teams, histories, extra=None):
    """European team -> (league, domestic training name), from reviewed identities only.

    Uses team_research.history_team, the live research resolver (exact name, the league's reviewed
    aliases, the global alias table, the canonical key; never fuzzy), then `extra` ({league: {European name:
    domestic name}}, the reviewed docs/audits/european-domestic-aliases.json, each confirmed by fixture
    evidence; harness only; matched by exact name or reviewed Europa key). A team found in more than one
    domestic league is ambiguous and left out."""
    from team_research import history_team
    extra = extra or {}
    out, ambiguous = {}, set()

    from scripts.europa_research import key
    keyed = {league: {key(k): v for k, v in table.items()} for league, table in extra.items()}

    def resolve(team, names, league):
        # The alias is looked up by its exact name or by the reviewed Europa key (case and accents folded),
        # the form UEL names take ("SSC Napoli" -> "ssc napoli"); never fuzzy.
        name = history_team(team, names, league)
        if name is None:
            target = extra.get(league, {}).get(team) or keyed.get(league, {}).get(key(team))
            if target in names:
                name = target
        return name
    for team in teams:
        found = {(league, name) for league, (frame, names) in histories.items()
                 if (name := resolve(team, names, league)) is not None}
        if len(found) == 1:
            out[team] = found.pop()
        elif found:
            ambiguous.add(team)
    return out, ambiguous


def merge_aliases(extra, reviewed):
    """The fixture-evidence aliases plus the manual reviewed ones ({league: {European: domestic}}); a reviewed
    alias may never override a fixture-evidence one."""
    out = {league: dict(table) for league, table in (extra or {}).items()}
    for league, table in (reviewed or {}).items():
        for source, target in table.items():
            if out.setdefault(league, {}).get(source, target) != target:
                raise ValueError(f'Reviewed alias {source!r} would override a fixture-evidence alias')
            out[league][source] = target
    return out


def scoped_identities(teams, histories, extra=None, reviewed=None):
    """(before, after): team identities with the manual reviewed aliases (for European fixtures before the
    European holdout start) and without them (on or after it)."""
    after = domestic_identities(teams, histories, extra)
    before = domestic_identities(teams, histories, merge_aliases(extra, reviewed)) if reviewed else after
    return before, after


def domestic_form_coverage(fixtures, histories, min_matches=5, days=365, extra=None, reviewed=None,
                           reviewed_before=None):
    """Per European fixture: does each team have at least `min_matches` domestic league matches in the
    `days` before the fixture's day (strictly earlier days only)? Reads domestic dates and team names,
    never a score. `histories` maps league -> (frame, team names); pass holdout-free frames. `reviewed`
    (manual reviewed aliases, {league: {European: domestic}}) applies only to fixtures before `reviewed_before`."""
    teams = sorted(set(fixtures.HomeTeam) | set(fixtures.AwayTeam))
    (mapped_before, ambiguous), (mapped_after, _) = scoped_identities(teams, histories, extra, reviewed)
    cut = pd.Timestamp(reviewed_before) if reviewed else None
    dates = {}
    for team, (league, name) in {**mapped_after, **mapped_before}.items():
        frame = histories[league][0]
        dates[(league, name)] = pd.DatetimeIndex(frame.Date.loc[(frame.HomeTeam == name) | (frame.AwayTeam == name)]).sort_values()
    rows, seen = [], set()
    for r in fixtures.itertuples(index=False):
        day = pd.Timestamp(r.Date).normalize()
        mapped = mapped_before if cut is not None and pd.Timestamp(r.Date) < cut else mapped_after
        counts = []
        for team in (r.HomeTeam, r.AwayTeam):
            if team in mapped:
                seen.add(team)
            d = dates.get(mapped.get(team))
            counts.append(0 if d is None else int(((d < day) & (d >= day - pd.Timedelta(days=days))).sum()))
        rows.append({'home_domestic_matches': counts[0], 'away_domestic_matches': counts[1],
                     'home_league': mapped.get(r.HomeTeam, (None,))[0], 'away_league': mapped.get(r.AwayTeam, (None,))[0],
                     'both': min(counts) >= min_matches, 'one': max(counts) >= min_matches})
    unresolved = Counter(t for t in list(fixtures.HomeTeam) + list(fixtures.AwayTeam) if t not in seen)
    return pd.DataFrame(rows, index=fixtures.index), {'teams': len(teams), 'mapped_teams': len(seen),
                                                      'ambiguous_teams': sorted(ambiguous),
                                                      'unmapped_by_appearances': unresolved.most_common()}
