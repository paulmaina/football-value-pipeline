"""Timestamped free-source match research, frozen in each prediction for offline replay.

Numeric form is ten matches, newest weighted most, with venue splits and xG
only when actually supplied by a source. News/context remain evidence, not
unvalidated numerical modifiers. Missing evidence never means 'no absences'.
"""
from __future__ import annotations

from datetime import datetime, timezone
import hashlib
import json
import math
from pathlib import Path
from urllib.parse import urlencode, urlparse
import xml.etree.ElementTree as ET

import numpy as np
import pandas as pd
import requests

VERSION = 'team-form-research-v1'
ESPN = 'https://site.api.espn.com/apis/site/v2/sports/soccer/'
LEAGUES = {'Premier League': 'eng.1', 'La Liga': 'esp.1', 'Bundesliga': 'ger.1',
           'Serie A': 'ita.1', 'Ligue 1': 'fra.1', 'Eredivisie': 'ned.1',
           'Primeira Liga': 'por.1', 'Super Lig': 'tur.1', 'Süper Lig': 'tur.1',
           'UEFA Champions League': 'uefa.champions', 'UEFA Europa League': 'uefa.europa'}
CATEGORIES = ('form', 'venue_splits', 'xg', 'availability', 'lineups', 'rotation',
              'h2h', 'tactics', 'motivation', 'rivalry', 'weather', 'travel')
TTL_HOURS = 3


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


def form_history(history, home, away, cutoff):
    """Use completed earlier dates only. Same-day results have no reliable availability time."""
    required = {'Date', 'HomeTeam', 'AwayTeam', 'FTHG', 'FTAG'}
    if history is None or not required <= set(history):
        return {'home': [], 'away': [], 'h2h': []}
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
    return {'home': [r for r in rows if name(home) in (name(r['home']), name(r['away']))][:10],
            'away': [r for r in rows if name(away) in (name(r['home']), name(r['away']))][:10],
            'h2h': [r for r in rows if {name(home), name(away)} == {name(r['home']), name(r['away'])}
                    and utc(r['date']) >= utc(cutoff) - pd.DateOffset(years=4)][:10]}


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

    def get(self, url, xml=False, max_age_minutes=None):
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
                    'source': source})
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
            page = client.get(url, xml=True)
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


def prepare(row, cutoff, evidence=None):
    """One replayable context and goal model. Prior shrinks ten-game form to the fitted team rates."""
    evidence = evidence or {}
    cached = decode(row.get('research_history_json'))
    sources = evidence.get('sources', [])
    valid_sources = all(pd.notna(utc(s.get('observed_at_utc'))) and utc(s['observed_at_utc']) <= cutoff for s in sources)
    if not valid_sources:
        evidence = {'errors': ['research observation after evaluation cutoff']}
    stats = {}
    for side in ('home', 'away'):
        team = row.get(side + '_team')
        rows = list(cached.get(side, []))
        if valid_sources:
            rows += evidence.get('recent', {}).get(side, [])
        unique = {}
        for r in rows:
            date = utc(r.get('date'))
            if pd.notna(date) and date < cutoff.normalize() and name(team) in (name(r.get('home')), name(r.get('away'))):
                key = (date.date().isoformat(), name(r.get('home')), name(r.get('away')))
                if key not in unique:
                    unique[key] = r
                elif (unique[key]['home_goals'], unique[key]['away_goals']) == (r['home_goals'], r['away_goals']):
                    if number(r.get('home_xg')) is not None and number(r.get('away_xg')) is not None:
                        unique[key] = {**unique[key], 'home_xg': r['home_xg'], 'away_xg': r['away_xg'],
                                       'xg_source': r.get('source')}

        ordered = sorted(unique.values(), key=lambda r: r['date'], reverse=True)[:10]
        stats[side] = {'all': weighted_form(ordered, team), 'venue': weighted_form(ordered, team, side)}
    coverage = dict(evidence.get('coverage', {}))
    if evidence.get('news'):
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
    if evidence.get('schedules'):
        coverage['rotation'] = 'schedule congestion only; rotation unconfirmed'
        evidence['rest_and_travel'] = {}
        for side, fixtures in evidence['schedules'].items():
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
    warnings += evidence.get('errors', [])
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
    context = {'version': VERSION, 'observed_at_utc': cutoff.isoformat(), 'form': stats,
               'h2h': h2h, 'coverage': coverage, 'warnings': warnings,
               'evidence': evidence, 'base_rates': base, 'goal_rates': rates,
               'model_note': 'Poisson team rates with ten-match shrinkage; qualitative context has no fitted coefficient'}
    if all(r is not None and r > 0 for r in rates):
        from score_probability import score_grid
        # Independent Poisson: do not transfer a fitted DC rho after changing rates.
        matrix, _ = score_grid(*rates, 0.)
        from asian_handicap import margins
        context.update(margin_distribution=json.loads(margins(matrix)),
                       p_over_1_5=float(matrix[np.add.outer(np.arange(len(matrix)), np.arange(len(matrix))) > 1.5].sum()))
    else:
        warnings.append('team goal-rate model unavailable')
    return context


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


def understat_rows(html, source, cutoff):
    """Read the public completed-match JSON, without executing page JavaScript."""
    import re
    import codecs
    match = re.search(r"datesData\s*=\s*JSON\.parse\('([^']*)'\)", html or '')
    if not match:
        return []
    try:
        values = json.loads(codecs.decode(match[1], 'unicode_escape'))
    except (ValueError, UnicodeError):
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
