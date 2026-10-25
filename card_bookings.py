"""Research only: Pinnacle-style booking totals from API-Football card events.

Pinnacle settles card totals as bookings: an eligible yellow counts 1, a red 2,
and the second yellow of a dismissal is excluded, so yellow then second-yellow
red totals 3. football-data.co.uk HY/HR cannot reproduce that, so production
keeps card totals out (count_markets.CARD_SETTLEMENT_GAP). This module rebuilds
the target from events for a free-plan research study. It never enters
production, requests nothing by default and keeps its own cache directory.

Cards after regulation time and cards whose participation cannot be checked
without line-ups are flagged, not guessed. A match with any flag has no total.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path

import pandas as pd

LEAGUES = {'Bundesliga': 'D1', 'SerieA': 'I1', 'Ligue1': 'F1'}
SEASONS = {2022: '2223', 2023: '2324', 2024: '2425'}  # API-Football free-plan start years
SAMPLE_PER_LEAGUE = 50  # red-free matches that test the football-data.co.uk yellow-count shortcut
STORE = Path('.football_cache/api_football/card_events')
DEFAULT_MAX_REQUESTS = 80  # leaves room in the shared 100/day free allowance


def booking_points(events, home_id, away_id):
    """{'home', 'away', 'flags'} booking points per team under Pinnacle's rule.

    Per player: a single yellow is 1; any dismissal is 2 plus 1 if a yellow
    preceded it. That covers both encodings of a second-yellow dismissal
    ('Second Yellow card', or 'Yellow Card' twice plus 'Red Card') and a
    yellow followed by a straight red. Two yellows with no dismissal, unknown
    card types, unknown teams or players, and cards after 90 minutes plus
    stoppage time of the second half are flagged.
    """
    per_player, flags = {}, []
    for event in events or []:
        if not isinstance(event, dict) or event.get('type') != 'Card':
            continue
        detail = str(event.get('detail') or '').strip().lower()
        team = (event.get('team') or {}).get('id')
        player = (event.get('player') or {}).get('id')
        timing = event.get('time') or {}
        elapsed = timing.get('elapsed')
        side = 'home' if team == home_id else 'away' if team == away_id else None
        if side is None:
            flags.append('card for an unknown team')
            continue
        if player is None:
            flags.append('card without a player identity (possibly staff)')
            continue
        if not isinstance(elapsed, int) or elapsed > 90 and timing.get('extra') is None:
            flags.append('card outside regulation time or without a time')
            continue
        record = per_player.setdefault((side, player), {'yellow': 0, 'red': 0})
        if detail == 'yellow card':
            record['yellow'] += 1
        elif detail in ('red card', 'second yellow card'):
            record['red'] += 1
        else:
            flags.append(f'unknown card type {detail!r}')
    points = {'home': 0, 'away': 0}
    for (side, _), record in per_player.items():
        if record['red'] > 1:
            flags.append('player dismissed more than once')
        if record['red']:
            points[side] += 2 + min(record['yellow'], 1)
        elif record['yellow'] > 1:
            flags.append('two yellows without a dismissal')
            points[side] += 1
        else:
            points[side] += record['yellow']
    return {**points, 'dismissals': sum(bool(r['red']) for r in per_player.values()), 'flags': sorted(set(flags))}


def _similar(a, b):
    from rapidfuzz import fuzz
    from football_value_pipeline_v2_standalone import canonical_team_key
    a, b = canonical_team_key(str(a)), canonical_team_key(str(b))
    return max(fuzz.token_set_ratio(a, b), fuzz.partial_ratio(a, b))


def linked_matches(cache='.football_cache', now=None):
    """football-data.co.uk rows for the study, each with a unique API-Football fixture ID.

    A link needs a fixture within a day, the identical full-time score and both
    team names similar (>= 60); anything else is left unlinked.
    """
    from api_football_integration import records
    now = now or datetime.now(timezone.utc)
    frames = []
    for key, division in LEAGUES.items():
        api = pd.DataFrame([{'fixture_id': p['id'], 'api_date': pd.Timestamp(p['kickoff_utc'][:10]),
                             'api_home': p['home']['name'], 'api_away': p['away']['name'],
                             'home_id': p['home']['id'], 'away_id': p['away']['id'],
                             'hg': p['score']['home'], 'ag': p['score']['away']}
                            for p in (r['payload'] for r in records(cache, key, now.isoformat()))
                            if p.get('score') and p.get('season') in SEASONS])
        for start, code in SEASONS.items():
            path = Path(cache)/f'{code}_{division}.csv'
            if not path.exists():
                continue
            fd = pd.read_csv(path, encoding='latin-1')
            fd = fd.assign(date=pd.to_datetime(fd.Date, dayfirst=True))
            for row in fd.to_dict('records'):
                near = api.loc[((api.api_date - row['date']).abs() <= pd.Timedelta(days=1))
                               & (api.hg == row['FTHG']) & (api.ag == row['FTAG'])] if len(api) else api
                near = near.loc[[min(_similar(row['HomeTeam'], h), _similar(row['AwayTeam'], a)) >= 60
                                 for h, a in zip(near.api_home, near.api_away)]] if len(near) else near
                link = near.iloc[0] if len(near) == 1 else None
                frames.append({**row, 'league': key, 'season_start': start,
                               'fixture_id': int(link.fixture_id) if link is not None else None,
                               'home_id': int(link.home_id) if link is not None else None,
                               'away_id': int(link.away_id) if link is not None else None})
    return pd.DataFrame(frames)


def _sample_key(row):
    return hashlib.sha256(f"{row['league']}|{row['fixture_id']}".encode()).hexdigest()


def collection_plan(linked):
    """Fixture IDs in request order: red-card matches, then the red-free sample."""
    usable = linked.loc[linked.fixture_id.notna()].copy()
    usable['red'] = (usable.HR + usable.AR) > 0
    plan = list(usable.loc[usable.red].sort_values(['league', 'date']).fixture_id.astype(int))
    for league, group in usable.loc[~usable.red].groupby('league'):
        chosen = sorted(group.to_dict('records'), key=_sample_key)[:SAMPLE_PER_LEAGUE]
        plan += [int(r['fixture_id']) for r in chosen]
    return plan


def events_store(cache='.football_cache'):
    from bbs_data import Store
    return Store(Path(cache)/'api_football'/'card_events')


def cached_events(store, fixture_id):
    from bbs_data import decode
    cached = store.latest_response('/fixtures/events?'+f'fixture={fixture_id}')
    if not cached:
        return None
    payload = decode(cached['payload'])
    return None if payload.get('unavailable') else payload.get('response')


def collect(client, plan, store):
    """Request events for planned fixtures not yet cached; stop on provider limits."""
    from bbs_data import Deferred, FetchError
    done = fetched = 0
    for fixture_id in plan:
        if cached_events(store, fixture_id) is not None:
            done += 1
            continue
        try:
            client.get('/fixtures/events', {'fixture': fixture_id}, ttl=10**9)
            fetched += 1
            done += 1
        except Deferred as exc:
            return {'planned': len(plan), 'cached': done, 'fetched': fetched, 'stopped': str(exc)}
        except FetchError as exc:
            return {'planned': len(plan), 'cached': done, 'fetched': fetched, 'stopped': type(exc).__name__}
    return {'planned': len(plan), 'cached': done, 'fetched': fetched, 'stopped': None}


def booking_targets(linked, events_for):
    """Rebuild per-team booking points for every linked match, or report why not.

    Red-card matches always come from events. Red-free matches use
    football-data.co.uk yellows only if every sampled red-free match with
    clean events agrees exactly; otherwise the shortcut is refused.
    """
    report = {'shortcut': {'checked': 0, 'agree': 0, 'mismatches': []}, 'red_matches': 0,
              'red_with_clean_events': 0, 'excluded_red_matches': []}
    usable = linked.loc[linked.fixture_id.notna()].copy()
    usable['red'] = (usable.HR + usable.AR) > 0
    points = {}
    for row in usable.to_dict('records'):
        events = events_for(int(row['fixture_id']))
        if events is None:
            continue
        result = booking_points(events, row['home_id'], row['away_id'])
        if result['flags']:
            if row['red']:
                report['excluded_red_matches'].append({'fixture_id': int(row['fixture_id']), 'flags': result['flags']})
            continue
        points[int(row['fixture_id'])] = (result['home'], result['away'])
        if not row['red']:
            report['shortcut']['checked'] += 1
            same = (result['home'], result['away']) == (int(row['HY']), int(row['AY']))
            report['shortcut']['agree'] += same
            if not same:
                report['shortcut']['mismatches'].append({'fixture_id': int(row['fixture_id']),
                    'football_data': [int(row['HY']), int(row['AY'])], 'events': [result['home'], result['away']]})
    report['red_matches'] = int(usable.red.sum())
    report['red_with_clean_events'] = int(sum(int(f) in points for f in usable.loc[usable.red, 'fixture_id']))
    shortcut_ok = report['shortcut']['checked'] > 0 and not report['shortcut']['mismatches']
    complete = report['red_with_clean_events'] + len(report['excluded_red_matches']) == report['red_matches']
    report['shortcut_valid'] = shortcut_ok
    report['ready'] = shortcut_ok and complete and not report['excluded_red_matches']
    if not report['ready']:
        return None, report
    frame = usable.copy()
    frame['HBK'] = [points[int(f)][0] if red else int(y) for f, red, y in zip(frame.fixture_id, frame.red, frame.HY)]
    frame['ABK'] = [points[int(f)][1] if red else int(y) for f, red, y in zip(frame.fixture_id, frame.red, frame.AY)]
    return frame, report


def study(cache='.football_cache', events_for=None):
    """Walk-forward validation of booking totals per league, with unchanged rules.

    The booking total stands in for the count model's card total (HY/AY set to
    booking points, HR/AR to zero); features, fit and thresholds are unchanged.
    """
    import count_markets as cm
    store = events_store(cache) if events_for is None else None
    events_for = events_for or (lambda f: cached_events(store, f))
    frame, report = booking_targets(linked_matches(cache), events_for)
    report['leagues'] = {}
    if frame is None:
        return report
    for league, group in frame.groupby('league'):
        history = group.drop(columns=['date']).assign(HY=group.HBK, AY=group.ABK, HR=0, AR=0)
        report['leagues'][league] = cm.evaluate(cm.walk_forward(history, 'cards'), 'cards')
    return report


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('--cache', default='.football_cache')
    parser.add_argument('--max-requests', type=int, default=DEFAULT_MAX_REQUESTS)
    parser.add_argument('--plan-only', action='store_true', help='Print the plan and progress; no requests')
    parser.add_argument('--study', type=Path, help='Write the validation study to this file (keep it out of git); no requests')
    args = parser.parse_args(argv)
    linked = linked_matches(args.cache)
    plan = collection_plan(linked)
    store = events_store(args.cache)
    progress = {'linked': int(linked.fixture_id.notna().sum()), 'unlinked': int(linked.fixture_id.isna().sum()),
                'planned': len(plan), 'cached': sum(cached_events(store, f) is not None for f in plan)}
    if args.plan_only:
        print(json.dumps(progress, indent=2))
        return 0
    if args.study:
        result = study(args.cache)
        args.study.write_text(json.dumps(result, indent=2, default=str), encoding='utf-8')
        print(json.dumps({k: v for k, v in result.items() if k != 'leagues'} | {'leagues': sorted(result['leagues'])},
                         indent=2, default=str))
        return 0
    from api_football_data import Client
    from api_key_config import load_api_keys
    load_api_keys()
    client = Client(store, os.environ.get('API_FOOTBALL_KEY', ''), max_requests=args.max_requests)
    print(json.dumps({**progress, **collect(client, plan, store)}, indent=2))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
