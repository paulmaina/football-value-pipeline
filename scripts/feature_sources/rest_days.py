"""Item 2: rest days and fixture congestion from fixture data already held, plus an ESPN audit of what is missing.

Part A (offline). One row per team per match for every domestic league match (football-data.co.uk, 2015/16 on)
and every cached UCL (2015/16 on) and UEL (2020/21 on) match: days since the team's previous held match, held
matches in the previous 14 and 21 days, and whether that previous match was a European away fixture. Only matches
on strictly earlier days count, so every value was known before kickoff (fixture dates only; no result is read).
European clubs are joined to their domestic name through the reviewed identities CE3n uses.

Part B (network, ESPN, cached). For a fixed random sample of team-seasons, ESPN's all-competition team schedule
(cups, super cups, UEFA Conference League, older UEL) is compared with the held fixtures: how many competitive
matches are missing, and how often each feature changes on the team's league matches once they are added.

    python scripts/feature_sources/rest_days.py              # both parts
    python scripts/feature_sources/rest_days.py --offline    # part A only
"""
from __future__ import annotations

import argparse
from collections import Counter
import difflib
import json
import random
import sys
import time
from pathlib import Path

import numpy as np
import pandas as pd
import requests

sys.path.insert(0, str(Path(__file__).resolve().parent))
import common as c  # noqa: E402

REST = c.FEATURE_CACHE / 'rest'
ESPN_CACHE = REST / 'espn'
ESPN = 'https://site.api.espn.com/apis/site/v2/sports/soccer/'
SAMPLE_SEASONS = (2016, 2019, 2022, 2024)  # ESPN season = start year; 2024 = 2024/25 (all inside dev or earlier)
PER_LEAGUE = 4
SEED = 20261123
# usa.1 rows for European clubs are MLS All-Star exhibitions; the others are pre-season invitation tournaments.
NON_COMPETITIVE = ('friendly', 'usa.1', 'champs_cup', 'audi_cup', 'joan_gamper')


# ---------------------------------------------------------------------------
# Part A
# ---------------------------------------------------------------------------

def appearances(domestic, european, identities):
    rows = []
    for r in domestic.itertuples(index=False):
        key = f'{r.league}|{r.Date.date()}|{r.HomeTeam}|{r.AwayTeam}'
        rows.append((key, r.Date.normalize(), r.league, r.league, r.HomeTeam, 'home', r.AwayTeam))
        rows.append((key, r.Date.normalize(), r.league, r.league, r.AwayTeam, 'away', r.HomeTeam))
    for r in european.itertuples(index=False):
        key = f'{r.competition}|{r.Date.date()}|{r.HomeTeam}|{r.AwayTeam}'
        home = identities.get(r.HomeTeam, (None, 'EU:' + r.HomeTeam))[1]
        away = identities.get(r.AwayTeam, (None, 'EU:' + r.AwayTeam))[1]
        hl = identities.get(r.HomeTeam, (None,))[0]
        al = identities.get(r.AwayTeam, (None,))[0]
        rows.append((key, r.Date.normalize(), r.competition, hl, home, 'home', away))
        rows.append((key, r.Date.normalize(), r.competition, al, away, 'away', home))
    return pd.DataFrame(rows, columns=['match', 'date', 'competition', 'league', 'team', 'side', 'opponent'])


def features(app):
    """Per appearance, from the same team's appearances on strictly earlier days only."""
    app = app.sort_values(['team', 'date', 'competition'], kind='stable').reset_index(drop=True)
    out = []
    for team, part in app.groupby('team', sort=False):
        dates = part.date.values.astype('datetime64[D]')
        comp = part.competition.values
        side = part.side.values
        for i in range(len(part)):
            d = dates[i]
            prev = np.nonzero(dates < d)[0]
            if len(prev):
                j = prev[-1]
                days = int((d - dates[j]).astype(int))
                last_comp, last_euro_away = comp[j], bool(comp[j] in ('UCL', 'UEL') and side[j] == 'away')
            else:
                days, last_comp, last_euro_away = None, None, None
            n14 = int(((dates >= d - 14) & (dates < d)).sum())
            n21 = int(((dates >= d - 21) & (dates < d)).sum())
            out.append((days, n14, n21, last_euro_away, last_comp))
    f = pd.DataFrame(out, columns=['days_since_last', 'matches_prev_14d', 'matches_prev_21d',
                                   'last_match_european_away', 'last_competition'])
    return pd.concat([app, f], axis=1)


def part_a(cfg):
    domestic = c.domestic_matches()
    european = c.european_matches()
    identities, ambiguous = c.european_identities(european, domestic)
    app = appearances(domestic, european, identities)
    feat = features(app)
    feat['period'] = [c.period(d, l, cfg) if comp not in ('UCL', 'UEL') else None
                      for d, l, comp in zip(feat.date, feat.league, feat.competition)]
    REST.mkdir(parents=True, exist_ok=True)
    feat.to_csv(REST / 'rest_features.csv', index=False)
    dom = feat.loc[~feat.competition.isin(['UCL', 'UEL'])].copy()
    # A previous held match within 60 days: inside a season. Season openers have none (summer break) and get no rest value.
    dom['in_season'] = dom.days_since_last.notna() & (dom.days_since_last <= 60)
    summary = {
        'appearances': int(len(feat)), 'domestic_league_appearances': int(len(dom)),
        'european_appearances': int(feat.competition.isin(['UCL', 'UEL']).sum()),
        'first_date': str(feat.date.min().date()), 'last_date': str(feat.date.max().date()),
        'european_teams': int(len(set(european.HomeTeam) | set(european.AwayTeam))),
        'european_teams_linked_to_domestic': int(len(identities)), 'ambiguous_identities': ambiguous,
        'by_period': {}, 'by_league': {}, 'domestic_teams_with_european_matches_by_season': {},
    }
    for name, part in dom.groupby('period'):
        summary['by_period'][name] = {
            'team_matches': int(len(part)),
            'with_rest_value_share': round(float(part.in_season.mean()), 4),
            'last_match_european_away_share': round(float(part.last_match_european_away.fillna(False).mean()), 4),
            'days_since_last_median': float(part.loc[part.in_season, 'days_since_last'].median()),
            'short_rest_le_3d_share': round(float((part.loc[part.in_season, 'days_since_last'] <= 3).mean()), 4),
            'matches_prev_14d_mean': round(float(part.matches_prev_14d.mean()), 3),
        }
    for name, part in dom.groupby('league'):
        summary['by_league'][name] = {
            'team_matches': int(len(part)),
            'after_european_match_share': round(float(part.last_competition.isin(['UCL', 'UEL']).mean()), 4),
            'last_match_european_away_share': round(float(part.last_match_european_away.fillna(False).mean()), 4),
        }
    euro_dom = feat.loc[feat.competition.isin(['UCL', 'UEL']) & feat.league.notna()]
    seasons = euro_dom.assign(season=euro_dom.date.dt.year.where(euro_dom.date.dt.month >= 7, euro_dom.date.dt.year - 1))
    summary['domestic_teams_with_european_matches_by_season'] = {
        f'{int(s)}/{str(int(s) + 1)[-2:]}': {comp: int(p.loc[p.competition == comp, 'team'].nunique()) for comp in ('UCL', 'UEL')}
        for s, p in seasons.groupby('season')}
    return summary, feat, domestic, identities


# ---------------------------------------------------------------------------
# Part B: ESPN audit
# ---------------------------------------------------------------------------

class Espn:
    def __init__(self, delay=1.0):
        self.session = requests.Session()
        self.delay = delay
        self.log = Counter()
        self.errors = []

    def get(self, path):
        ESPN_CACHE.mkdir(parents=True, exist_ok=True)
        file = ESPN_CACHE / (path.replace('/', '_').replace('?', '_').replace('=', '-').replace('&', '_') + '.json')
        if file.exists():
            self.log['cached'] += 1
            return json.loads(file.read_text(encoding='utf-8'))
        for attempt in range(3):
            time.sleep(self.delay * (1 + 2 * attempt))
            try:
                r = self.session.get(ESPN + path, timeout=30, headers={'User-Agent': 'football-research-check/1.0'})
                self.log[f'http_{r.status_code}'] += 1
                if r.status_code == 200:
                    data = r.json()
                    file.write_text(json.dumps(data), encoding='utf-8')
                    return data
                if r.status_code not in (429, 500, 502, 503, 504):
                    break
            except (requests.RequestException, ValueError) as exc:
                self.log[type(exc).__name__] += 1
        self.errors.append(path)
        return None


def norm(name):
    from football_value_pipeline_v2_standalone import normalize_team_name
    return normalize_team_name(name)


def espn_team_ids(espn, league, season, names):
    """football-data name -> (ESPN id, ESPN name, how) for the league's ESPN teams that season. Reviewed resolver
    first (team_research.history_team); otherwise a close normalised-name match (sample selection only)."""
    from team_research import history_team
    data = espn.get(f'{c.ESPN_SLUG[league]}/teams?season={season}')
    if not data:
        return {}
    teams = [t['team'] for s in data.get('sports', []) for lg in s.get('leagues', []) for t in lg.get('teams', [])]
    out = {}
    normed = {norm(n): n for n in names}
    for t in teams:
        for label in (t.get('displayName'), t.get('shortDisplayName'), t.get('name')):
            hit = history_team(label, names, league) if label else None
            how = 'reviewed'
            if hit is None and label:
                close = difflib.get_close_matches(norm(label), list(normed), n=1, cutoff=0.82)
                hit, how = (normed[close[0]], 'close') if close else (None, None)
            if hit and hit not in out:
                out[hit] = (str(t['id']), t.get('displayName'), how)
                break
    return out


def espn_events(data, team_id):
    rows = []
    for e in (data or {}).get('events', []):
        slug = (e.get('league') or {}).get('slug') or ''
        comp = (e.get('competitions') or [{}])[0]
        status = (comp.get('status') or e.get('status') or {}).get('type', {})
        if not status.get('completed'):
            continue
        side = next((x.get('homeAway') for x in comp.get('competitors', []) if str(x.get('team', {}).get('id')) == team_id), None)
        rows.append({'date': pd.Timestamp(e['date']).tz_convert(None).normalize(), 'slug': slug, 'side': side,
                     'competitive': not any(k in slug for k in NON_COMPETITIVE)})
    return pd.DataFrame(rows, columns=['date', 'slug', 'side', 'competitive'])


def feature_at(dates, comps, sides, d):
    prev = dates < d
    if not prev.any():
        return None, int(((dates >= d - pd.Timedelta(days=14)) & prev).sum()), 0, None
    j = np.nonzero(prev.values)[0][-1]
    days = int((d - dates.iloc[j]).days)
    euro_away = bool(str(comps.iloc[j]).startswith(('uefa.', 'UCL', 'UEL')) and sides.iloc[j] == 'away')
    n14 = int(((dates >= d - pd.Timedelta(days=14)) & prev).sum())
    n21 = int(((dates >= d - pd.Timedelta(days=21)) & prev).sum())
    return days, n14, n21, euro_away


def part_b(feat, domestic):
    espn = Espn()
    rng = random.Random(SEED)
    picks = []
    for season in SAMPLE_SEASONS:
        code = f'{str(season)[-2:]}{str(season + 1)[-2:]}'
        for league in c.CODES.values():
            part = domestic.loc[(domestic.league == league) & (domestic.season == code)]
            names = sorted(set(part.HomeTeam) | set(part.AwayTeam))
            ids = espn_team_ids(espn, league, season, names)
            pool = sorted(ids)
            for team in rng.sample(pool, min(PER_LEAGUE, len(pool))):
                picks.append((season, code, league, team, *ids[team]))
    rows, missing_by_slug, matched_teams = [], Counter(), []
    for season, code, league, team, team_id, espn_name, how in picks:
        data = espn.get(f'all/teams/{team_id}/schedule?season={season}')
        ev = espn_events(data, team_id)
        if ev.empty:
            continue
        start, end = pd.Timestamp(f'{season}-07-01'), pd.Timestamp(f'{season + 1}-06-30')
        ev = ev.loc[(ev.date >= start) & (ev.date <= end)]
        held = feat.loc[(feat.team == team) & (feat.date >= start - pd.Timedelta(days=30)) & (feat.date <= end)]
        held_league = held.loc[(held.competition == league) & (held.date >= start)]
        espn_league = ev.loc[ev.slug == c.ESPN_SLUG[league]]
        matched_teams.append({'season': f'{season}/{str(season + 1)[-2:]}', 'league': league, 'team': team,
                              'espn_name': espn_name, 'match': how, 'held_league_matches': int(len(held_league)),
                              'espn_league_matches': int(len(espn_league))})
        held_dates = set(held.date)
        comp_ev = ev.loc[ev.competitive]
        for r in comp_ev.itertuples(index=False):
            if r.date not in held_dates and not any(abs((r.date - h).days) <= 1 for h in held_dates):
                missing_by_slug[r.slug] += 1
        # Complete schedule: held matches plus ESPN competitive matches on days the held data has none (±1 day).
        extra = comp_ev.loc[[not any(abs((d - h).days) <= 1 for h in held_dates) for d in comp_ev.date]]
        full = pd.concat([held[['date', 'competition', 'side']],
                          extra.rename(columns={'slug': 'competition'})[['date', 'competition', 'side']]])
        full = full.sort_values('date', kind='stable').reset_index(drop=True)
        hs = held.sort_values('date', kind='stable').reset_index(drop=True)
        for t in held_league.itertuples(index=False):
            a = feature_at(hs.date, hs.competition, hs.side, t.date)
            b = feature_at(full.date, full.competition, full.side, t.date)
            rows.append({'season': season, 'league': league, 'team': team, 'date': t.date,
                         'days_held': a[0], 'days_full': b[0], 'n14_held': a[1], 'n14_full': b[1],
                         'n21_held': a[2], 'n21_full': b[2], 'euro_away_held': a[3], 'euro_away_full': b[3],
                         'european_club_season': bool(held.competition.isin(['UCL', 'UEL']).any()
                                                      or extra.slug.str.startswith('uefa.').any())})
    audit = pd.DataFrame(rows)
    audit.to_csv(REST / 'espn_audit_rows.csv', index=False)
    competitive_total = int(sum(len(espn_events(espn.get(f'all/teams/{p[4]}/schedule?season={p[0]}'), p[4])
                                     .query('competitive')) for p in picks))

    def rates(a):
        inseason = a.loc[a.days_full.notna() & (a.days_full <= 60)]
        return {
            'league_team_matches': int(len(a)),
            'days_since_last_differs_share': round(float((inseason.days_held != inseason.days_full).mean()), 4),
            'days_since_last_mean_abs_diff_when_differs': round(float(
                (inseason.days_held - inseason.days_full).abs()[inseason.days_held != inseason.days_full].mean()), 2)
            if (inseason.days_held != inseason.days_full).any() else 0.0,
            'matches_prev_14d_differs_share': round(float((a.n14_held != a.n14_full).mean()), 4),
            'matches_prev_21d_differs_share': round(float((a.n21_held != a.n21_full).mean()), 4),
            'last_match_european_away_differs_share': round(float(
                (a.euro_away_held.fillna(False) != a.euro_away_full.fillna(False)).mean()), 4),
        }
    report = {
        'sample': {'seasons': [f'{s}/{str(s + 1)[-2:]}' for s in SAMPLE_SEASONS], 'per_league_season': PER_LEAGUE,
                   'seed': SEED, 'team_seasons': len(matched_teams)},
        'espn_competitive_matches': competitive_total,
        'espn_competitive_missing_from_held': int(sum(missing_by_slug.values())),
        'missing_by_competition': dict(missing_by_slug.most_common()),
        'league_match_count_mismatches': [m for m in matched_teams if m['held_league_matches'] != m['espn_league_matches']],
        'all': rates(audit) if len(audit) else {},
        'by_season': {str(s): rates(p) for s, p in audit.groupby('season')} if len(audit) else {},
        'european_club_seasons': rates(audit.loc[audit.european_club_season]) if len(audit) else {},
        'requests': dict(espn.log), 'failed_requests': espn.errors,
        'team_matching': Counter(m['match'] for m in matched_teams),
    }
    c.write_json(REST / 'espn_sample_teams.json', matched_teams)
    return report


def main(argv=None):
    p = argparse.ArgumentParser()
    p.add_argument('--offline', action='store_true')
    args = p.parse_args(argv)
    cfg = c.config()
    summary, feat, domestic, identities = part_a(cfg)
    result = {'part_a_held_fixtures': summary}
    if not args.offline:
        result['part_b_espn_audit'] = part_b(feat, domestic)
    c.write_json(c.OUT / 'rest_days.json', result)
    print(json.dumps(result, indent=1, default=str)[:6000])


if __name__ == '__main__':
    raise SystemExit(main())
