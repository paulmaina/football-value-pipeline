"""Timestamped free-source match research, frozen in each prediction for offline replay.

Numeric form is ten matches, newest weighted most, with venue splits and xG
only when actually supplied by a source. News/context remain evidence, not
unvalidated numerical modifiers. Missing evidence never means 'no absences'.
"""
from __future__ import annotations

from datetime import datetime, timezone
from functools import lru_cache
import hashlib
import json
import math
from pathlib import Path
from urllib.parse import urlencode, urlparse
import xml.etree.ElementTree as ET

import numpy as np
import pandas as pd
import requests

VERSION = 'team-form-research-v4'
# v3 kept every completed ESPN game in the last-ten form, club friendlies
# included (most of them international-break friendlies, which aren't
# competitive evidence). v4 records the ESPN competition of each result and
# leaves friendlies out of the form (is_friendly); league, cup and European
# games are unchanged. Kept only so forecasts frozen under v3 replay exactly.
V3_VERSION = 'team-form-research-v3'
PREVIOUS_VERSION = V3_VERSION
# v2 looked a side's training history up by its fixture name, so a side the
# fixture and the history name differently ("Hull City" / "Hull") got no
# training-history form at all. v3 resolves each side to its training name
# (history_team) and freezes that name in research_history_json['teams'].
# Kept only so forecasts frozen under v2 replay exactly.
V2_VERSION = 'team-form-research-v2'
# v1 identified a result by its team names, so a match that two sources name
# differently (ESPN "Hull City", training history "Hull") was counted twice in
# the last-ten form. Kept only so forecasts frozen under v1 replay exactly.
LEGACY_VERSION = 'team-form-research-v1'
# Versions that read a side's history under its fixture name only.
FIXTURE_NAME_ONLY = (LEGACY_VERSION, V2_VERSION)
# Versions whose last-ten form keeps club friendlies.
FRIENDLIES_KEPT = (LEGACY_VERSION, V2_VERSION, V3_VERSION)
# ESPN competition slugs of friendlies that don't say "friendly" ("club.friendly",
# "friendly.emirates_cup" do). Reviewed against every ESPN competition in the live
# forms of 5-8 Nov 2026 (evaluation/research_parity_latest_rule/espn_competitions.json).
FRIENDLY_COMPETITIONS = frozenset({'esp.joan_gamper'})
# Reviewed fixture -> training names that bbs_team_aliases.json and TEAM_ALIASES
# don't cover; the model reaches these only through its fuzzy fallback, which the
# research never uses. Every pair below was seen in live forecasts and is the
# same club. Kept apart from bbs_team_aliases.json, which also decides the BBS
# statistics identity checks, so adding them leaves the model's goal rates alone.
HISTORY_ALIASES = {
    'Bundesliga': {'1. FSV Mainz 05': 'Mainz', 'SV 07 Elversberg': 'Elversberg'},
    'Eredivisie': {'ADO Den Haag': 'Den Haag', 'AZ': 'AZ Alkmaar', "FC Twente '65": 'Twente',
                   'FC Twente Enschede': 'Twente', 'NEC Nijmegen': 'Nijmegen', 'PEC Zwolle': 'Zwolle',
                   'SBV Excelsior': 'Excelsior', 'SC Cambuur-Leeuwarden': 'Cambuur', 'Telstar 1963': 'Telstar',
                   'Willem II Tilburg': 'Willem II'},
    'LaLiga': {'CA Osasuna': 'Osasuna', 'Deportivo Alavés': 'Alaves', 'Deportivo La Coruña': 'La Coruna'},
    'Ligue1': {'Angers SCO': 'Angers', 'Lille OSC': 'Lille', 'Olympique Lyonnais': 'Lyon',
               'Olympique de Marseille': 'Marseille', 'RC Strasbourg Alsace': 'Strasbourg',
               'Racing Club de Lens': 'Lens'},
    'PrimeiraLiga': {'Braga': 'Sp Braga', 'CD Nacional': 'Nacional', 'CD Santa Clara': 'Santa Clara',
                     'CS Maritimo': 'Maritimo', 'CS Marítimo': 'Maritimo', 'Sport Lisboa e Benfica': 'Benfica'},
    'SerieA': {'Atalanta BC': 'Atalanta'},
}
ESPN = 'https://site.api.espn.com/apis/site/v2/sports/soccer/'
LEAGUES = {'Premier League': 'eng.1', 'La Liga': 'esp.1', 'Bundesliga': 'ger.1',
           'Serie A': 'ita.1', 'Ligue 1': 'fra.1', 'Eredivisie': 'ned.1',
           'Primeira Liga': 'por.1', 'Super Lig': 'tur.1', 'Süper Lig': 'tur.1',
           'UEFA Champions League': 'uefa.champions', 'UEFA Europa League': 'uefa.europa'}
CATEGORIES = ('form', 'venue_splits', 'xg', 'availability', 'lineups', 'rotation',
              'h2h', 'tactics', 'motivation', 'rivalry', 'weather', 'travel')
TTL_HOURS = 3

# ---------------------------------------------------------------------------
# Value model input schema
# ---------------------------------------------------------------------------
# The value shortlist's research model (team_form_poisson_v1) must stay
# independent of bookmaker odds. prepare() sees ONLY these fields: every
# other column of a forecast row (odds, quotes, the published grid, market
# fits, blended probabilities) is dropped before the model runs. Bookmaker
# prices are used later, by the selection layer only, to price a research
# probability against the Pinnacle offer.
SCHEMA_VERSION = 'value-model-inputs-v1'
INPUT_SCHEMA = {
    # Identity and timing.
    'home_team': 'team identity',
    'away_team': 'team identity',
    'kickoff_utc': 'kickoff time, for rest and travel context only',
    # Independent goal rates: the Dixon-Coles fit to past results (plus the
    # BBS match-statistics or shot adjustment when its own gate passes), read
    # before the market blend and the totals anchor touch the score grid.
    'lambda_home': 'independent home goal rate (pre-blend, pre-anchor)',
    'lambda_away': 'independent away goal rate (pre-blend, pre-anchor)',
    # Team history: completed earlier matches from the training files.
    'research_history_json': 'team history from the training files (form_history)',
}
# Pre-kickoff research (collect_fixture). Only `recent` rows feed numbers;
# the other keys are descriptive evidence and coverage.
EVIDENCE_SCHEMA = ('sources', 'coverage', 'news', 'errors', 'recent', 'schedules')
RESULT_FIELDS = ('date', 'home', 'away', 'home_goals', 'away_goals', 'home_xg', 'away_xg', 'source', 'competition')


def research_inputs(row):
    """Project a forecast row onto the value model's input schema."""
    getter = row.get if hasattr(row, 'get') else (lambda key: None)
    return {key: getter(key) for key in INPUT_SCHEMA}


def observed_by(evidence, cutoff):
    """True when every research source was observed at or before the cutoff.

    prepare() drops all pre-kickoff evidence otherwise; evaluation_harness mirrors it.
    """
    return all(pd.notna(utc(s.get('observed_at_utc'))) and utc(s['observed_at_utc']) <= cutoff
               for s in evidence.get('sources', []))


def research_evidence(evidence):
    """Numeric view of pre-kickoff research: schema keys, and result fields only in `recent`."""
    out = {k: evidence[k] for k in EVIDENCE_SCHEMA if k in evidence}
    if isinstance(out.get('recent'), dict):
        out['recent'] = {side: [{k: r.get(k) for k in RESULT_FIELDS if k in r} for r in rows if isinstance(r, dict)]
                         for side, rows in out['recent'].items() if isinstance(rows, list)}
    return out


def utc(value):
    return pd.to_datetime(value, utc=True, errors='coerce')


def number(value):
    try:
        out = float(value)
        return out if math.isfinite(out) else None
    except (ValueError, TypeError):
        return None


def name(value):
    from football_value_pipeline_v2_standalone import canonical_team_key
    return canonical_team_key(str(value or ''))


def decode(value):
    if isinstance(value, dict):
        return value
    try:
        return json.loads(value) if isinstance(value, str) else {}
    except (ValueError, TypeError):
        return {}


@lru_cache(maxsize=None)
def _reviewed_aliases(league_key):
    """League-scoped reviewed aliases keyed by raw and by canonical name; a canonical key two clubs share is dropped."""
    from football_value_pipeline_v2_standalone import canonical_team_key
    path = Path(__file__).with_name('bbs_team_aliases.json')
    reviewed = {**json.loads(path.read_text(encoding='utf-8')).get(league_key, {}),
                **HISTORY_ALIASES.get(league_key, {})}
    keyed, clash = {}, set()
    for raw, target in reviewed.items():
        key = canonical_team_key(raw)
        if keyed.setdefault(key, target) != target and canonical_team_key(keyed[key]) != canonical_team_key(target):
            clash.add(key)
    return reviewed, {k: v for k, v in keyed.items() if k not in clash}


def history_team(team, teams, league_key=None):
    """The training-history name of a fixture team, or None when it can't be told for certain.

    The same reviewed identities the model's resolve_team() applies before its fuzzy
    fallback (an exact name, the league's reviewed alias, the global alias, the
    canonical key), plus HISTORY_ALIASES; never fuzzy matching, so a side is never
    given another club's history. The answer must be exactly one training team.
    """
    from football_value_pipeline_v2_standalone import TEAM_ALIASES, canonical_team_key, normalize_team_name
    teams = {t for t in teams if isinstance(t, str) and t}
    if not isinstance(team, str) or not team:
        return None
    if team in teams:
        return team
    if league_key == 'UEL':
        from europa_training import resolver
        target = resolver()(team)
        return target if target in teams else None
    reviewed, keyed = _reviewed_aliases(league_key)
    target = (reviewed.get(team) or keyed.get(canonical_team_key(team))
              or TEAM_ALIASES.get(normalize_team_name(team)) or team)
    found = {t for t in teams if canonical_team_key(t) == canonical_team_key(target)}
    return found.pop() if len(found) == 1 else None


def form_history(history, home, away, cutoff, names=None):
    """Use completed earlier dates only. Same-day results have no reliable availability time.

    `names` maps 'home'/'away' to each side's training-history name (history_team);
    it is frozen as 'teams' so prepare() knows which rows are the side's own. Without
    it a side is looked up under its fixture name, as research v1/v2 did.
    """
    required = {'Date', 'HomeTeam', 'AwayTeam', 'FTHG', 'FTAG'}
    empty = {'home': [], 'away': [], 'h2h': []}
    if names is not None:
        empty['teams'] = {side: names.get(side) for side in ('home', 'away')}
        home, away = names.get('home') or home, names.get('away') or away
    if history is None or not required <= set(history):
        return empty
    frame = history.copy()
    frame = frame.loc[pd.to_datetime(frame.Date, utc=True, errors='coerce') < utc(cutoff).normalize()]
    rows = []
    for r in frame.to_dict('records'):
        h, a = number(r['FTHG']), number(r['FTAG'])
        if h is None or a is None or h < 0 or a < 0 or h % 1 or a % 1:
            continue
        rows.append({'date': utc(r['Date']).isoformat(), 'home': r['HomeTeam'], 'away': r['AwayTeam'],
                     'home_goals': h, 'away_goals': a, 'home_xg': number(r.get('HxG')),
                     'away_xg': number(r.get('AxG')), 'source': 'pipeline training history'})
    rows.sort(key=lambda r: r['date'], reverse=True)
    return {**empty,
            'home': [r for r in rows if name(home) in (name(r['home']), name(r['away']))][:10],
            'away': [r for r in rows if name(away) in (name(r['home']), name(r['away']))][:10],
            'h2h': [r for r in rows if {name(home), name(away)} == {name(r['home']), name(r['away'])}
                    and utc(r['date']) >= utc(cutoff) - pd.DateOffset(years=4)][:10]}


def history_name(history, side, version=VERSION):
    """The side's frozen training-history name, read from research v3 on (None before, or if unresolved)."""
    if version in FIXTURE_NAME_ONLY:
        return None
    teams = decode(history).get('teams')
    return teams.get(side) if isinstance(teams, dict) else None


def is_friendly(competition) -> bool:
    """True for an ESPN friendly competition slug. A row without a competition (training
    history, Understat, ESPN rows frozen before v4) is never treated as a friendly."""
    slug = str(competition or '').strip().lower()
    return bool(slug) and ('friendly' in slug or slug in FRIENDLY_COMPETITIONS)


def form_rows(team, rows, cutoff, version=VERSION, history_team_name=None):
    """A team's last ten results before the cutoff day, newest first, each match once.

    Sources spell teams differently, so a match is the same match when the names
    agree or when the day, the team's venue and the score agree. The first row
    seen is kept (the training history comes first) and takes verified xG from
    a later copy. `version=LEGACY_VERSION` replays the v1 rule (names only).

    `history_team_name` (v3 on) is the team's training-history name ("Hull" for the
    fixture's "Hull City"); rows naming it are restated with the fixture name, so
    they count as the team's own and the venue is read correctly.

    From v4 on, friendlies (is_friendly on the row's ESPN competition) are left out
    before the last ten are chosen, so the form reaches back to the team's tenth
    competitive game.
    """
    if version not in FRIENDLIES_KEPT:
        rows = [r for r in rows if not is_friendly(r.get('competition'))]
    if history_team_name and version not in FIXTURE_NAME_ONLY and name(history_team_name) != name(team):
        key = name(history_team_name)
        rows = [{**r, **{f: team for f in ('home', 'away') if name(r.get(f)) == key}} for r in rows]
    unique, same_result = {}, {}
    for r in rows:
        date = utc(r.get('date'))
        if pd.isna(date) or date >= cutoff.normalize() or name(team) not in (name(r.get('home')), name(r.get('away'))):
            continue
        day = date.date().isoformat()
        key = (day, name(r.get('home')), name(r.get('away')))
        if version != LEGACY_VERSION:
            result = (day, name(r.get('home')) == name(team), r.get('home_goals'), r.get('away_goals'))
            key = same_result.setdefault(result, key)
        if key not in unique:
            unique[key] = r
        elif (unique[key]['home_goals'], unique[key]['away_goals']) == (r['home_goals'], r['away_goals']):
            if number(r.get('home_xg')) is not None and number(r.get('away_xg')) is not None:
                unique[key] = {**unique[key], 'home_xg': r['home_xg'], 'away_xg': r['away_xg'],
                               'xg_source': r.get('source')}
    return sorted(unique.values(), key=lambda r: r['date'], reverse=True)[:10]


def weighted_form(rows, team, venue=None):
    chosen = [r for r in rows if venue is None or name(r[venue]) == name(team)][:10]
    goals_for, goals_against, points, weights, xfor, xagainst = [], [], [], [], [], []
    for i, r in enumerate(chosen):
        home = name(r['home']) == name(team)
        gf, ga = r['home_goals' if home else 'away_goals'], r['away_goals' if home else 'home_goals']
        goals_for.append(gf); goals_against.append(ga)
        points.append(3 if gf > ga else 1 if gf == ga else 0)
        weights.append(2 ** (-i / 5))
        xf, xa = r.get('home_xg' if home else 'away_xg'), r.get('away_xg' if home else 'home_xg')
        if number(xf) is not None and number(xa) is not None:
            xfor.append((float(xf), weights[-1])); xagainst.append((float(xa), weights[-1]))
    if not chosen:
        return {'matches': 0}
    mean = lambda xs: float(np.average(xs, weights=weights))
    result = {'matches': len(chosen), 'goals_for': mean(goals_for), 'goals_against': mean(goals_against),
              'points_per_game': mean(points), 'last_match': chosen[0]['date'],
              'results': ''.join('W' if f > a else 'D' if f == a else 'L' for f, a in zip(goals_for, goals_against))}
    if xfor:
        result.update(xg_matches=len(xfor), xg_for=float(np.average([x for x, _ in xfor], weights=[w for _, w in xfor])),
                      xg_against=float(np.average([x for x, _ in xagainst], weights=[w for _, w in xagainst])))
    return result


class FreeSources:
    """Bounded, cached, public requests. Failed sources stay explicit and cost no API credits.

    A cached observation is immutable and usable only at/after its actual fetch.
    Source failures are cached too, preventing repeated failed requests per fixture.
    """
    def __init__(self, cache, session=None, clock=None, limit=320, online=True):
        self.cache = Path(cache) / 'match_research'
        self.cache.mkdir(parents=True, exist_ok=True)
        self.session = session or requests.Session()
        self.clock = clock or (lambda: datetime.now(timezone.utc))
        self.remaining = limit
        self.online = online
        self.memo = {}
        self.source_requests = {}

    def get(self, url, xml=False, max_age_minutes=None, check=None):
        """`check(data)` returns a reason when an HTTP 2xx response is not the source's data
        (a placeholder such as a maintenance page); the observation is then unavailable."""
        now = utc(self.clock())
        def fresh(value):
            if not isinstance(value, dict):
                return False
            stamp = utc(value.get('observed_at_utc'))
            ttl = pd.Timedelta(hours=TTL_HOURS) if value.get('status') == 'available' else pd.Timedelta(minutes=10)
            if max_age_minutes is not None:
                ttl = min(ttl, pd.Timedelta(minutes=max_age_minutes))
            return value.get('url') == url and pd.notna(stamp) and pd.Timedelta(0) <= now-stamp < ttl
        # A shared URL may be requested later with a stricter lineup/weather TTL.
        if url in self.memo and fresh(self.memo[url]):
            return self.memo[url]
        key = hashlib.sha256(url.encode()).hexdigest()
        path = self.cache / (key + '.json')
        saved = decode(path.read_text(encoding='utf-8')) if path.exists() else {}
        host = (urlparse(url).hostname or '').removeprefix('www.')
        recent = [t for t in self.source_requests.get(host, []) if now-t < pd.Timedelta(minutes=1)]
        self.source_requests[host] = recent
        if fresh(saved):
            self.memo[url] = saved
            return saved
        result = {'url': url, 'observed_at_utc': now.isoformat(), 'status': 'unavailable'}
        if not self.online:
            result['reason'] = 'no cached observation; online research disabled'
        elif host == 'thesportsdb.com' and len(recent) >= 30:
            result['reason'] = 'TheSportsDB free source limit: 30 requests per minute'
        elif self.remaining <= 0:
            result['reason'] = 'free research request budget reached'
        else:
            self.remaining -= 1
            recent.append(now)
            try:
                response = self.session.get(url, timeout=(5, 15), headers={'User-Agent': 'football-value-pipeline/1.0'})
                response.raise_for_status()
                if len(response.content) > 4_000_000:
                    raise ValueError('research response exceeds size limit')
                data = response.text if xml else response.json()
                if not xml and not isinstance(data, dict):
                    raise ValueError('research response is not an object')
                reason = check(data) if check else None
                if reason:
                    result['reason'] = reason
                else:
                    result.update(status='available', data=data)
            except (requests.RequestException, ValueError, OSError) as exc:
                # Do not store URLs from exceptions or headers which may contain credentials.
                result['reason'] = type(exc).__name__
            result['observed_at_utc'] = utc(self.clock()).isoformat()
            temporary = path.with_suffix('.tmp')
            temporary.write_text(json.dumps(result, sort_keys=True), encoding='utf-8')
            temporary.replace(path)
        self.memo[url] = result
        return result


def events(payload):
    return payload.get('events', []) if isinstance(payload, dict) else []


def competitors(event):
    competitions = event.get('competitions') or []
    return competitions[0].get('competitors', []) if competitions else []


def same_fixture(event, row):
    players = competitors(event)
    if (not isinstance(players, list) or len(players) != 2
            or any(not isinstance(r, dict) or not isinstance(r.get('team'), dict) for r in players)):
        return False
    sides = {r.get('homeAway'): r['team'] for r in players}
    kick, target = utc(event.get('date')), utc(row.get('kickoff_utc'))
    return (pd.notna(kick) and pd.notna(target) and abs((kick-target).total_seconds()) <= 60
            and all(name(row.get(side + '_team')) in {name(t.get('displayName')), name(t.get('name')),
                                                     name(t.get('shortDisplayName'))}
                    for side, t in sides.items()) and set(sides) == {'home', 'away'})


def schedule_rows(payload, cutoff, source):
    out = []
    for e in events(payload):
        state = e.get('status') or (e.get('competitions') or [{}])[0].get('status', {})
        status = state.get('type', {})
        kick = utc(e.get('date'))
        sides = {c.get('homeAway'): c for c in competitors(e)}
        if (not status.get('completed') or status.get('name') not in ('STATUS_FULL_TIME', 'STATUS_FINAL')
                or (number(state.get('period')) or 0) > 2
                or pd.isna(kick) or kick + pd.Timedelta(hours=2) >= cutoff or set(sides) != {'home', 'away'}):
            continue
        goals = [number(sides[s].get('score', {}).get('value') if isinstance(sides[s].get('score'), dict)
                        else sides[s].get('score')) for s in ('home', 'away')]
        if any(g is None or g < 0 or g % 1 for g in goals):
            continue
        xg = {}
        for side, competitor in sides.items():
            values = {s.get('name', '').lower(): number(s.get('value', s.get('displayValue')))
                      for s in competitor.get('statistics', [])}
            xg[side] = next((values[k] for k in ('expectedgoals', 'expected_goals', 'xg') if values.get(k) is not None), None)
        out.append({'home_xg': xg.get('home'), 'away_xg': xg.get('away'), 'date': kick.isoformat(), 'home': sides['home']['team'].get('displayName'),
                    'away': sides['away']['team'].get('displayName'), 'home_goals': goals[0], 'away_goals': goals[1],
                    'source': source, 'competition': e['league'].get('slug') if isinstance(e.get('league'), dict) else None})
    return out


def news_items(payload, cutoff):
    """Dated headlines with source links; no inferred injuries, tactics or motivation."""
    try:
        root = ET.fromstring(payload)
    except (ValueError, ET.ParseError, TypeError):
        return []
    out = []
    for item in root.findall('.//item'):
        published = utc(item.findtext('pubDate'))
        if pd.isna(published) or published > cutoff or published < cutoff-pd.Timedelta(days=7):
            continue
        title, link = item.findtext('title'), item.findtext('link')
        if title and link and link.startswith('https://'):
            out.append({'headline': title, 'url': link, 'published_at_utc': published.isoformat(),
                        'source': item.findtext('source') or 'news search'})
    return out[:8]


def collect_fixture(row, client):
    """Research missing fixture context using ESPN, free news search and Open-Meteo.

    Public endpoints can change. Missing/ambiguous matches, unavailable sources
    and unconfirmed team news remain explicit, never synthesized as facts.
    """
    league = LEAGUES.get(row.get('league'))
    evidence = {'sources': [], 'coverage': {}, 'news': [], 'errors': []}
    if not league:
        evidence['errors'].append('competition has no verified free-source adapter')
        return evidence
    kick = utc(row.get('kickoff_utc'))
    if pd.isna(kick):
        return evidence
    if utc(client.clock()) >= kick:
        evidence['errors'].append('pre-match research deadline passed; no post-kickoff context collected')
        return evidence
    url = ESPN + league + '/scoreboard?' + urlencode({'dates': kick.strftime('%Y%m%d')})
    board = client.get(url)
    evidence['sources'].append({k: board.get(k) for k in ('url', 'observed_at_utc', 'status', 'reason')})
    matches = [e for e in events(board.get('data', {})) if same_fixture(e, row)]
    if len(matches) != 1:
        evidence['errors'].append('free-source fixture identity missing or ambiguous')
    else:
        match = matches[0]
        summary = client.get(ESPN + league + '/summary?' + urlencode({'event': match['id']}),
                             max_age_minutes=5 if kick-utc(client.clock()) <= pd.Timedelta(hours=2) else 180)
        evidence['sources'].append({k: summary.get(k) for k in ('url', 'observed_at_utc', 'status', 'reason')})
        from match_context import compact_squads, verified_summary
        data = verified_summary(summary.get('data'), row, match['id'])
        if data is None:
            evidence['errors'].append('ESPN summary identity unverified; no summary injuries, lineups or venue used')
            data = {}
        else:
            evidence['summary_identity_verified'] = True
            compact_squads(data, evidence, {str(c.get('team', {}).get('id')): c.get('team', {}).get('displayName')
                                           for c in competitors(match)})
        venue = data.get('gameInfo', {}).get('venue') or (match.get('competitions') or [{}])[0].get('venue', {})
        evidence['venue'] = venue
        evidence['recent'] = {}
        for side in competitors(match):
            team = side.get('team', {})
            team_id = str(team.get('id', ''))
            if not team_id.isdigit():
                continue
            schedule = client.get(ESPN + 'all/teams/' + team_id + '/schedule')
            evidence['sources'].append({k: schedule.get(k) for k in ('url', 'observed_at_utc', 'status', 'reason')})
            evidence['recent'][side['homeAway']] = schedule_rows(schedule.get('data', {}), utc(client.clock()), schedule['url'])
            # The full schedule is preserved as evidence of congestion, including upcoming cup fixtures.
            evidence.setdefault('schedules', {})[side['homeAway']] = [
                {'date': e.get('date'), 'name': e.get('name'),
                 'venue': (e.get('competitions') or [{}])[0].get('venue'),
                 'completed': bool((e.get('status') or (e.get('competitions') or [{}])[0].get('status', {})).get('type', {}).get('completed')),
                 'home_away': next((c.get('homeAway') for c in competitors(e)
                                    if str(c.get('team', {}).get('id')) == team_id), None)}
                for e in events(schedule.get('data', {}))
                if pd.notna(utc(e.get('date'))) and kick-pd.Timedelta(days=14) <= utc(e['date']) <= kick+pd.Timedelta(days=7)]
        standings = client.get('https://site.api.espn.com/apis/v2/sports/soccer/' + league + '/standings')
        evidence['sources'].append({k: standings.get(k) for k in ('url', 'observed_at_utc', 'status', 'reason')})
        if standings.get('status') == 'available':
            evidence['standings'] = standings.get('data')
            evidence['coverage']['motivation'] = 'standings context; urgency not inferred'
    from match_context import espn_news
    structured_news = espn_news(row, client, evidence, league)
    query = f'"{row.get("home_team")}" "{row.get("away_team")}" injury suspension lineup preview'
    news = None
    if not structured_news:
        news = client.get('https://www.bing.com/news/search?' + urlencode({'q': query, 'format': 'rss'}), xml=True)
        evidence['sources'].append({k: news.get(k) for k in ('url', 'observed_at_utc', 'status', 'reason')})
    # Public xG for supported domestic leagues. Keep unavailable coverage explicit
    # when a site rejects collection or its schema changes.
    slug = UNDERSTAT.get(row.get('league'))
    if slug:
        season = kick.year if kick.month >= 7 else kick.year-1
        for year in (season, season-1):
            url = f'https://understat.com/league/{slug}/{year}'
            page = client.get(url, xml=True, check=understat_check)
            evidence['sources'].append({k: page.get(k) for k in ('url', 'observed_at_utc', 'status', 'reason')})
            for past in understat_rows(page.get('data'), url, utc(client.clock())):
                for side in ('home', 'away'):
                    if name(row.get(side + '_team')) in (name(past['home']), name(past['away'])):
                        evidence.setdefault('recent', {}).setdefault(side, []).append(past)
    evidence['news'] = structured_news or news_items((news or {}).get('data'), utc(client.clock()))
    if not evidence['news']:
        for url in ('https://feeds.bbci.co.uk/sport/football/rss.xml', 'https://www.theguardian.com/football/rss'):
            feed = client.get(url, xml=True)
            evidence['sources'].append({k: feed.get(k) for k in ('url', 'observed_at_utc', 'status', 'reason')})
            evidence['news'] += [n for n in news_items(feed.get('data'), utc(client.clock()))
                                 if any(name(row.get(s + '_team')) in name(n['headline']) for s in ('home', 'away'))]
    from match_context import collect_weather, add_review_links
    collect_weather(row, client, evidence)
    add_review_links(row, evidence)
    return evidence


def prepare(row, cutoff, evidence=None, version=VERSION):
    """One replayable context and goal model. Prior shrinks ten-game form to the fitted team rates.

    `version` is for replaying a frozen forecast under the rules it was made with (see form_rows):
    v3 reads each side's training-history name from research_history_json['teams'].

    Enforces the value model input schema: the row is projected onto
    INPUT_SCHEMA and the numbers read only research_evidence(evidence), so no
    odds field can reach the research probabilities.
    """
    row = research_inputs(row)
    evidence = evidence or {}
    cached = decode(row.get('research_history_json'))
    valid_sources = observed_by(evidence, cutoff)
    if not valid_sources:
        evidence = {'errors': ['research observation after evaluation cutoff']}
    # The stored evidence keeps everything collected; the model reads only the schema view.
    view = research_evidence(evidence)
    stats, unresolved, friendlies = {}, [], {}
    for side in ('home', 'away'):
        team = row.get(side + '_team')
        rows = list(cached.get(side, []))
        if valid_sources:
            rows += view.get('recent', {}).get(side, [])
        own = history_name(cached, side, version)
        ordered = form_rows(team, rows, cutoff, version, own)
        stats[side] = {'all': weighted_form(ordered, team), 'venue': weighted_form(ordered, team, side)}
        if version not in FRIENDLIES_KEPT:
            friendlies[side] = len({r.get('date') for r in rows if is_friendly(r.get('competition'))
                                    and pd.notna(utc(r.get('date'))) and utc(r['date']) < cutoff.normalize()})
        if version not in FIXTURE_NAME_ONLY and 'teams' in cached and not own:
            unresolved.append(f'{side} team {team!r} has no reviewed training-history name; no history form')
    coverage = dict(view.get('coverage', {}))
    if view.get('news'):
        coverage['team_news'] = 'dated news leads; absences and tactics require confirmation'
    if all(stats[s]['all']['matches'] >= 5 for s in stats):
        coverage['form'] = 'last ten, exponential rank half-life five matches'
    if all(stats[s]['venue']['matches'] >= 3 for s in stats):
        coverage['venue_splits'] = 'home team home matches / away team away matches'
    h2h = [r for r in cached.get('h2h', []) if pd.notna(utc(r.get('date')))
           and cutoff-pd.DateOffset(years=4) <= utc(r['date']) < cutoff.normalize()]
    if h2h:
        coverage['h2h'] = 'last four years; descriptive only'
    if all(stats[s]['all'].get('xg_matches', 0) >= 5 for s in stats):
        coverage['xg'] = 'verified supplied xG; no goals-to-xG substitution'
    if view.get('schedules'):
        coverage['rotation'] = 'schedule congestion only; rotation unconfirmed'
        evidence['rest_and_travel'] = {}
        for side, fixtures in view['schedules'].items():
            previous = [e for e in fixtures if e.get('completed') is True
                        and pd.notna(utc(e.get('date'))) and utc(e['date']) < cutoff]
            if previous:
                last = max(previous, key=lambda e: utc(e['date']))
                evidence['rest_and_travel'][side] = {
                    'previous_fixture': last,
                    'days_between_kickoffs': (utc(row.get('kickoff_utc'))-utc(last['date'])).total_seconds()/86400,
                    'completed_matches_last_14_days': sum(utc(row.get('kickoff_utc'))-pd.Timedelta(days=14) <= utc(e['date']) for e in previous),
                    'note': 'schedule-derived travel context; actual itinerary and fatigue unverified'}
        if any(v['previous_fixture'].get('venue') for v in evidence['rest_and_travel'].values()):
            coverage['travel'] = 'previous fixture venue; itinerary and fatigue unverified'
    warnings = [c + ' unavailable or unconfirmed' for c in CATEGORIES if c not in coverage]
    warnings += view.get('errors', []) + unresolved
    base = [number(row.get('lambda_home')), number(row.get('lambda_away'))]
    rates = list(base)
    for i, side in enumerate(('home', 'away')):
        other = 'away' if side == 'home' else 'home'
        own = stats[side]['venue'] if stats[side]['venue']['matches'] >= 3 else stats[side]['all']
        opp = stats[other]['venue'] if stats[other]['venue']['matches'] >= 3 else stats[other]['all']
        if rates[i] is None or rates[i] <= 0:
            continue
        n = min(own['matches'], opp['matches'])
        if n:
            gf, ga = own['goals_for'], opp['goals_against']
            if own.get('xg_matches', 0) >= 5 and opp.get('xg_matches', 0) >= 5:
                gf, ga = own['xg_for'], opp['xg_against']
            rates[i] = max(.05, min(8., (10*base[i] + n*(gf+ga)/2) / (10+n)))
    context = {'version': version, 'observed_at_utc': cutoff.isoformat(), 'form': stats,
               'h2h': h2h, 'coverage': coverage, 'warnings': warnings,
               'evidence': evidence, 'base_rates': base, 'goal_rates': rates,
               'model_note': 'Poisson team rates with ten-match shrinkage; qualitative context has no fitted coefficient'}
    if any(friendlies.values()):
        context['form_friendlies_excluded'] = friendlies
    if all(r is not None and r > 0 for r in rates):
        matrix = research_grid(rates)
        from asian_handicap import margins
        context.update(margin_distribution=json.loads(margins(matrix)),
                       p_over_1_5=float(matrix[np.add.outer(np.arange(len(matrix)), np.arange(len(matrix))) > 1.5].sum()))
    else:
        warnings.append('team goal-rate model unavailable')
    return context


def research_grid(goal_rates):
    """The research score grid from prepare()'s goal rates; shared by the live pipeline and the harness."""
    from score_probability import score_grid
    # Independent Poisson: do not transfer a fitted DC rho after changing rates.
    matrix, _ = score_grid(*goal_rates, 0.)
    return matrix


def enrich(predictions, cache, fetch=False, client=None, clock=None):
    """Called before saving a run. Replay/price refresh use the frozen columns, with no network."""
    out = predictions.copy()
    if out.empty:
        return out
    if client is None:
        client = FreeSources(cache, online=fetch, clock=clock)
    rows = []
    for row in out.astype(object).where(out.notna(), None).to_dict('records'):
        try:
            evidence = collect_fixture(row, client)
        except (ValueError, KeyError, TypeError, IndexError, AttributeError) as exc:
            evidence = {'errors': ['free-source schema unavailable: ' + type(exc).__name__]}
        clock = utc(client.clock()) if client else utc(datetime.now(timezone.utc))
        context = prepare(row, clock, evidence)
        training_status = row.get('training_data_status')
        if training_status:
            context['coverage']['training_cache'] = str(training_status)
        if row.get('training_refresh_warning'):
            context['warnings'].append('training refresh unavailable; using verified local history through '
                + str(row.get('training_cutoff')) + ': ' + str(row['training_refresh_warning']))
        from research_quality import assess
        quality = assess(row, context, clock)
        context['evidence']['quality_review'] = quality
        context['evidence_quality_version'] = quality['version']
        context['warnings'] = list(dict.fromkeys([*context['warnings'], *quality['warnings']]))
        values = context.get('margin_distribution', {})
        for key, predicate in [('home', lambda d: d > 0), ('draw', lambda d: d == 0), ('away', lambda d: d < 0)]:
            row['research_p_' + key] = sum(p for d, p in values.items() if predicate(int(d))) if values else None
        row['research_p_over_1_5'] = context.get('p_over_1_5')
        row['research_probability_basis'] = 'team_form_poisson_v1'
        row['team_research_json'] = json.dumps(context, sort_keys=True, allow_nan=False)
        rows.append(row)
    return pd.DataFrame(rows)


UNDERSTAT = {'Premier League': 'EPL', 'La Liga': 'La_liga', 'Bundesliga': 'Bundesliga',
             'Serie A': 'Serie_A', 'Ligue 1': 'Ligue_1'}


def understat_matches(html):
    """The page's embedded match list (`datesData`), or None when the page carries none.

    understat.com answers HTTP 200 with a maintenance page for every URL, so a 2xx
    response alone does not mean match data."""
    import re
    import codecs
    match = re.search(r"datesData\s*=\s*JSON\.parse\('([^']*)'\)", html or '')
    if not match:
        return None
    try:
        values = json.loads(codecs.decode(match[1], 'unicode_escape'))
    except (ValueError, UnicodeError):
        return None
    return values if isinstance(values, list) else None


def understat_check(html):
    """FreeSources check: a reason when an Understat response has no match data."""
    if understat_matches(html):  # an empty list is no match data either
        return None
    return 'no match data (maintenance page)' if 'We will come back soon' in (html or '') else 'no match data'


def understat_rows(html, source, cutoff):
    """Read the public completed-match JSON, without executing page JavaScript."""
    values = understat_matches(html)
    if values is None:
        return []
    out = []
    for row in values:
        date = utc(row.get('datetime'))
        goals = row.get('goals') or {}
        xg = row.get('xG') or {}
        home, away = number(goals.get('h')), number(goals.get('a'))
        if (not row.get('isResult') or pd.isna(date) or date + pd.Timedelta(hours=2) >= cutoff
                or home is None or away is None or min(home, away) < 0):
            continue
        out.append({'date': date.isoformat(), 'home': row.get('h', {}).get('title'),
                    'away': row.get('a', {}).get('title'), 'home_goals': home, 'away_goals': away,
                    'home_xg': number(xg.get('h')), 'away_xg': number(xg.get('a')), 'source': source})
    return out
