"""Item 1: ClubElo coverage for the eight domestic leagues and UCL/UEL participants.

Source order:
  api     soccerdata's ClubElo reader (api.clubelo.com), cached under data/feature_cache/clubelo/raw. Tried first and
          recorded; on 23 Nov 2026 the host refused or timed out every connection, from this machine and from
          Anthropic's fetcher alike.
  mirror  data/feature_cache/clubelo/mirror/EloRatings.csv (github.com/xgabora/Club-Football-Match-Data-2000-2025,
          commit pinned in manifest.json): ClubElo snapshots on the 1st and 15th of each month to 1 June 2025;
          later rows are the maintainer's provisional continuation, NOT ClubElo. Its club names are already remapped
          to football-data.co.uk spellings, so its domestic name match overstates what the raw API names would give.

Matching, per club: exact name in the league's country; then the pipeline's normalised name in that country; then
a close normalised match (difflib >= 0.80) in that country, flagged for review. European clubs linked to a domestic
club (reviewed identities, as CE3n) take that club's match; others are matched across all countries (exact, then
normalised, then close >= 0.85, unique), flagged for review. Nothing is accepted silently: every non-exact match is
listed in the output.

Pre-kickoff: a rating is used only from a snapshot dated strictly before the match day (ClubElo's rating on day D
reflects matches up to D-1). No result or odds column is read.
"""
from __future__ import annotations

import difflib
import json
import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
import common as c  # noqa: E402

ELO = c.FEATURE_CACHE / 'clubelo'
MIRROR = ELO / 'mirror' / 'EloRatings.csv'
CLUBELO_END = pd.Timestamp('2025-06-01')  # last genuine ClubElo snapshot in the mirror
MAX_AGE_DAYS = 31


def try_api():
    """Returns (by-date frame or None, record). Uses the venv's soccerdata when importable."""
    record = {'source': 'soccerdata.ClubElo (api.clubelo.com)'}
    try:
        import soccerdata as sd
        record['soccerdata_version'] = sd.__version__
        reader = sd.ClubElo(data_dir=ELO / 'raw')
        frame = reader.read_by_date('2026-11-20')
        record['status'] = 'available'
        return frame, record
    except Exception as exc:  # network failure is the expected case on 23 Nov 2026
        record['status'] = 'unavailable'
        record['error'] = f'{type(exc).__name__}: {exc}'[:300]
        return None, record


def norm(name):
    from football_value_pipeline_v2_standalone import normalize_team_name
    return normalize_team_name(str(name))


def match_in(name, pool, normed, cutoff):
    if name in pool:
        return name, 'exact'
    n = norm(name)
    if n in normed and len(normed[n]) == 1:
        return normed[n][0], 'normalised'
    close = difflib.get_close_matches(n, list(normed), n=2, cutoff=cutoff)
    if close and (len(close) == 1 or difflib.SequenceMatcher(None, n, close[0]).ratio()
                  > difflib.SequenceMatcher(None, n, close[1]).ratio() + 0.05) and len(normed[close[0]]) == 1:
        return normed[close[0]][0], 'close (review)'
    return None, 'unmatched'


def index(names):
    out = {}
    for x in names:
        out.setdefault(norm(x), []).append(x)
    return out


AFFIXES = {'fc', 'fk', 'sk', 'kv', 'kaa', 'krc', 'pae', 'gnk', 'nk', 'pfc', 'bsc', 'ac', 'as', 'sc', 'cf', 'cd', 'sl',
           'sfp', 'tc', 'ff', 'if', 'bk', 'afc', 'ssc', 'aek', 'rsc', 'royale', 'club', 'de', 'cp', 'ud', 'jk', 'hnk',
           'ofk', 'sv', 'vfl', 'vfb', 'tsg', 'olympique', 'sporting', 'kf', 'kvc', 'mfk', 'fcsb', '1893', '1907',
           '1909', '1913', '1923', 'red', 'bull'}


def fold(name):
    import re
    import unicodedata
    text = unicodedata.normalize('NFKD', str(name)).encode('ascii', 'ignore').decode().lower()
    return [t for t in re.split(r'[^a-z0-9]+', text) if t]


def stripped(name):
    tokens = [t for t in fold(name) if t not in AFFIXES]
    return tokens or fold(name)


def match_european(name, pool):
    """Exact, then normalised, then accent-folded with club affixes removed, then a unique ClubElo name whose
    tokens are all in ours (or ours in its), then close >= 0.85. Everything after 'exact' is listed for review."""
    if name in pool:
        return name, 'exact'
    normed = index(pool)
    if len(normed.get(norm(name), [])) == 1:
        return normed[norm(name)][0], 'normalised'
    ours = stripped(name)
    key = ' '.join(ours)
    by_key = {}
    for x in pool:
        by_key.setdefault(' '.join(stripped(x)), []).append(x)
    if key in by_key and len(by_key[key]) == 1:
        return by_key[key][0], 'affixes removed (review)'
    subset = [x for k, xs in by_key.items() for x in xs
              if k and len(xs) == 1 and (set(k.split()) <= set(ours) or set(ours) <= set(k.split()))
              and min(len(k), len(key)) >= 4]
    if len(subset) == 1:
        return subset[0], 'token subset (review)'
    close = difflib.get_close_matches(key, list(by_key), n=2, cutoff=0.85)
    if len(close) == 1 and len(by_key[close[0]]) == 1:
        return by_key[close[0]][0], 'close (review)'
    return None, 'unmatched'


def main():
    api_frame, api_record = try_api()
    elo = pd.read_csv(MIRROR, dtype={'club': str, 'country': str})
    elo['date'] = pd.to_datetime(elo.date)
    manifest = json.loads((ELO / 'mirror' / 'manifest.json').read_text(encoding='utf-8'))
    domestic = c.domestic_matches()
    european = c.european_matches()
    identities, _ = c.european_identities(european, domestic)

    clubs = elo.groupby('club').agg(country=('country', 'first'), first=('date', 'min'), last=('date', 'max'))
    by_country = {k: set(v.index) for k, v in clubs.groupby('country')}
    all_names = set(clubs.index)
    all_index = index(all_names)

    # Domestic clubs
    dom_map, dom_rows = {}, []
    for league, part in domestic.groupby('league'):
        country = c.COUNTRY[league]
        pool = by_country.get(country, set())
        normed = index(pool)
        seasons = part.groupby(['HomeTeam'])['season'].agg(lambda s: sorted(set(s)))
        names = sorted(set(part.HomeTeam) | set(part.AwayTeam))
        for team in names:
            hit, how = match_in(team, pool, normed, 0.80)
            dom_map[(league, team)] = hit
            dom_rows.append({'league': league, 'team': team, 'clubelo_name': hit, 'match': how,
                             'seasons': seasons.get(team, []),
                             'first_snapshot': str(clubs.loc[hit, 'first'].date()) if hit else None})
    dom_df = pd.DataFrame(dom_rows)
    first_season = domestic.assign(start=pd.to_datetime('20' + domestic.season.str[:2] + '-07-01'))
    first_season = pd.concat([first_season[['league', 'HomeTeam', 'start']].rename(columns={'HomeTeam': 'team'}),
                              first_season[['league', 'AwayTeam', 'start']].rename(columns={'AwayTeam': 'team'})])
    first_season = first_season.groupby(['league', 'team']).start.min()
    dom_df['first_season_in_our_data'] = [str(first_season[(l, t)].date()) for l, t in zip(dom_df.league, dom_df.team)]
    gap = dom_df.loc[dom_df.first_snapshot.notna() & (dom_df.first_snapshot > dom_df.first_season_in_our_data)]

    # European clubs
    eu_rows = []
    euro_teams = sorted(set(european.HomeTeam) | set(european.AwayTeam))
    comps = {t: sorted(set(european.loc[(european.HomeTeam == t) | (european.AwayTeam == t), 'competition'])) for t in euro_teams}
    for team in euro_teams:
        if team in identities:
            league, dname = identities[team]
            hit, how = dom_map.get((league, dname)), 'via domestic identity'
            linked = league
        else:
            hit, how = match_european(team, all_names)
            linked = None
        eu_rows.append({'team': team, 'competitions': comps[team], 'forecast_league': linked, 'clubelo_name': hit,
                        'country': clubs.loc[hit, 'country'] if hit else None, 'match': how,
                        'first_snapshot': str(clubs.loc[hit, 'first'].date()) if hit else None})
    eu_df = pd.DataFrame(eu_rows)

    # Pre-kickoff rating lookup: latest snapshot strictly before the match day, at most MAX_AGE_DAYS old.
    snaps = {k: v.set_index('date').elo.sort_index() for k, v in elo.groupby('club')}

    def rating(club, day):
        s = snaps.get(club)
        if s is None:
            return None, None
        s = s.loc[s.index < day]
        if s.empty or (day - s.index[-1]).days > MAX_AGE_DAYS:
            return None, None
        return float(s.iloc[-1]), s.index[-1]

    def coverage(frame, name_of, label_of):
        rows = []
        for r in frame.itertuples(index=False):
            day = r.Date.normalize()
            h, hd = rating(name_of(r, 'HomeTeam'), day)
            a, ad = rating(name_of(r, 'AwayTeam'), day)
            rows.append({'label': label_of(r), 'both': h is not None and a is not None,
                         'genuine': h is not None and a is not None and max(hd, ad) <= CLUBELO_END})
        return pd.DataFrame(rows)

    dom = domestic.loc[domestic.Date >= '2016-07-01'].copy()
    cfg = c.config()
    dom_cov = coverage(dom, lambda r, s: dom_map.get((r.league, getattr(r, s))),
                       lambda r: c.period(r.Date, r.league, cfg))
    eu_name = {row['team']: row['clubelo_name'] for row in eu_rows}
    eu_cov = coverage(european, lambda r, s: eu_name.get(getattr(r, s)),
                      lambda r: ('both forecast-league clubs' if r.HomeTeam in identities and r.AwayTeam in identities
                                 else 'involves a non-forecast-league club'))

    def summarise(cov):
        return {k: {'matches': int(len(p)), 'both_rated_share': round(float(p.both.mean()), 4),
                    'both_rated_by_genuine_clubelo_share': round(float(p.genuine.mean()), 4)}
                for k, p in cov.groupby('label')}

    non_forecast = eu_df.loc[eu_df.forecast_league.isna()]
    result = {
        'api_attempt': api_record,
        'mirror': {**manifest, 'rows': int(len(elo)), 'clubs': int(len(clubs)), 'countries': int(elo.country.nunique()),
                   'first_date': str(elo.date.min().date()), 'last_date': str(elo.date.max().date()),
                   'snapshot_dates_per_year': 24, 'genuine_clubelo_until': str(CLUBELO_END.date())},
        'domestic_name_match': {
            'clubs': int(len(dom_df)), 'by_match': dom_df.match.value_counts().to_dict(),
            'by_league': {l: p.match.value_counts().to_dict() for l, p in dom_df.groupby('league')},
            'not_exact': dom_df.loc[dom_df.match != 'exact'].to_dict('records'),
            'history_starts_after_first_season_in_our_data': gap[
                ['league', 'team', 'first_season_in_our_data', 'first_snapshot']].to_dict('records')},
        'european_name_match': {
            'clubs': int(len(eu_df)), 'linked_to_forecast_league': int(eu_df.forecast_league.notna().sum()),
            'by_match': eu_df.match.value_counts().to_dict(),
            'non_forecast_league_clubs': int(len(non_forecast)),
            'non_forecast_matched_share': round(float(non_forecast.clubelo_name.notna().mean()), 4),
            'non_forecast_by_match': non_forecast.match.value_counts().to_dict(),
            'non_forecast_countries': non_forecast.country.value_counts().to_dict(),
            'unmatched': eu_df.loc[eu_df.clubelo_name.isna(), ['team', 'competitions', 'forecast_league']].to_dict('records'),
            'close_for_review': eu_df.loc[eu_df.match == 'close (review)', ['team', 'clubelo_name', 'country']].to_dict('records')},
        'domestic_match_coverage_from_2016_17': summarise(dom_cov),
        'european_match_coverage': summarise(eu_cov),
        'earliest_snapshot_matched_domestic_clubs': {
            'min': dom_df.first_snapshot.dropna().min(), 'max': dom_df.first_snapshot.dropna().max(),
            'clubs_first_seen_after_2016_07_01': dom_df.loc[dom_df.first_snapshot > '2016-07-01', ['league', 'team', 'first_snapshot']].to_dict('records')},
    }
    dom_df.to_csv(ELO / 'domestic_name_match.csv', index=False)
    eu_df.to_csv(ELO / 'european_name_match.csv', index=False)
    c.write_json(c.OUT / 'clubelo.json', result)
    print(json.dumps({k: v for k, v in result.items() if k not in ('domestic_name_match', 'european_name_match')}, indent=1, default=str))
    print(json.dumps({k: v for k, v in result['domestic_name_match'].items() if k != 'not_exact'}, indent=1))
    print(json.dumps({k: v for k, v in result['european_name_match'].items()}, indent=1, default=str)[:5000])


if __name__ == '__main__':
    raise SystemExit(main())
