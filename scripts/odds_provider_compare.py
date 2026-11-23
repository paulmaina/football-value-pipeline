"""Cross-provider check for the odds-provider adapter (docs/odds-providers.md, "Before turning it on").

Fetches one board from each configured kit provider (pinnapi, pinnodds) and reports:

- **Requests:** every HTTP request made to each provider, its status and any rate-limit headers, so each run can
  be counted against the key's daily allowance.
- **League names:** for each of our competitions, how many board events sit under the configured Pinnacle league
  name, and every board league whose name looks like a candidate (all board leagues are listed too).
- **Team names:** every board fixture in our competitions matched to The Odds API's schedule (its free events
  list: league, kickoff within 5 minutes, same canonical teams). Unmatched fixtures are listed with the schedule
  fixture at the same kickoff, which is the alias to add to odds_provider_team_aliases.json.
- **Prices:** pinnapi against pinnodds, and, with --odds-api, the kit board against The Odds API's Pinnacle 1X2,
  totals and spreads over the next 7 days (3 credits per league, only for --odds-api-leagues). Every difference is listed and those
  above the configured tolerance are marked.

Reads keys from the environment or .env (PINNAPI_API_KEY, PINNODDS_API_KEY, THE_ODDS_API_KEY...). Writes only
under --output. Never part of a forecast; commits nothing.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
from collections import Counter
from datetime import datetime, timedelta, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import odds_provider as op  # noqa: E402

MATCH_SECONDS = 300
HEADER_PATTERN = re.compile(r'rate|limit|remaining|quota|retry|usage|reset|plan|x-requests', re.I)
SECRET_PATTERN = re.compile(r'key|token|cookie|auth|session', re.I)
CANDIDATE_TOKENS = ('england', 'spain', 'germany', 'italy', 'france', 'netherlands', 'holland', 'portugal',
                    'turkey', 'türkiye', 'turkiye', 'uefa', 'europe', 'champions', 'europa')


def recording_session():
    """A requests session that keeps each response's status, timing and rate-limit headers (never secrets)."""
    import requests

    class Recording(requests.Session):
        def __init__(self):
            super().__init__()
            self.log = []

        def get(self, *args, **kwargs):
            started = time.monotonic()
            try:
                response = super().get(*args, **kwargs)
            except Exception as exc:
                self.log.append({'error': type(exc).__name__, 'seconds': round(time.monotonic() - started, 2)})
                raise
            self.log.append({'status': response.status_code, 'seconds': round(time.monotonic() - started, 2),
                             'bytes': len(response.content or b''),
                             'headers': {k: v for k, v in response.headers.items()
                                         if HEADER_PATTERN.search(k) and not SECRET_PATTERN.search(k)}})
            return response

    return Recording()


def kit_boards(config, errors):
    """{provider: (payload, fetched_at)} and {provider: request log}."""
    boards, requests_made = {}, {}
    for name in config['order']:
        spec = config['providers'][name]
        if spec['api'] != op.KIT:
            continue
        session = recording_session()
        try:
            payload = op.KitProvider(name, spec, session).board(datetime.now(timezone.utc))
            boards[name] = (payload, datetime.now(timezone.utc))
        except op.ProviderFailure as failure:
            errors[name] = failure.reason + (f' ({failure.detail})' if failure.detail else '')
        requests_made[name] = session.log
    return boards, requests_made


def board_leagues(payload):
    """Counter of (league id, league name) over the board's match events (no corner children)."""
    counts = Counter()
    for event in op.kit_events(payload):
        if event.get('parent_id') or event.get('event_type') not in (None, 'prematch'):
            continue
        counts[(str(event.get('league_id', '')), str(event.get('league_name') or '').strip())] += 1
    return counts


def league_report(payload, leagues):
    counts = board_leagues(payload)
    ours = {}
    for key, spec in leagues.items():
        hits = {(lid, name): n for (lid, name), n in counts.items()
                if op.league_of({'league_id': lid or None, 'league_name': name}, {key: spec})}
        ours[key] = {'configured_names': spec.get('pinnacle_league_names', []),
                     'configured_ids': spec.get('pinnacle_league_ids', []),
                     'events': sum(hits.values()),
                     'found_as': [{'league_id': lid, 'league_name': name, 'events': n}
                                  for (lid, name), n in sorted(hits.items())]}
    candidates = [{'league_id': lid, 'league_name': name, 'events': n} for (lid, name), n in sorted(counts.items())
                  if any(token in name.casefold() for token in CANDIDATE_TOKENS)]
    every = [{'league_id': lid, 'league_name': name, 'events': n} for (lid, name), n in sorted(counts.items())]
    return {'competitions': ours, 'candidates': candidates, 'all_leagues': every,
            'board_events': sum(counts.values())}


def board_shape(payload, leagues):
    """Top-level keys and one raw event (prefer one of ours) so a field-name mismatch is visible."""
    events = op.kit_events(payload)
    sample = next((e for e in events if op.league_of(e, leagues) and not op.is_corner_child(e)),
                  events[0] if events else None)
    corner = next((e for e in events if op.is_corner_child(e)), None)
    return {'top_level_keys': sorted(payload) if isinstance(payload, dict) else [],
            'stale': payload.get('stale') if isinstance(payload, dict) else None,
            'last_change': payload.get('last_change') if isinstance(payload, dict) else None,
            'events': len(events), 'corner_children': sum(1 for e in events if op.is_corner_child(e)),
            'sample_event': sample, 'sample_corner_event': corner}


def duplicate_report(payload, leagues, limit=6):
    """Board events in our competitions that share league, teams and kickoff: what tells them apart."""
    groups = {}
    for event in op.kit_events(payload):
        key = op.league_of(event, leagues)
        if key is None or op.is_corner_child(event):
            continue
        groups.setdefault((key, str(event.get('home')), str(event.get('away')), str(event.get('starts'))),
                          []).append(event)
    repeated = {k: v for k, v in groups.items() if len(v) > 1}

    def describe(event):
        period = op._kit_period(event) or {}
        periods = event.get('periods')
        return {**{k: v for k, v in event.items() if k != 'periods'},
                'period_keys': sorted(periods) if isinstance(periods, dict) else None,
                'game_period': {'status': period.get('status'), 'money_line': period.get('money_line'),
                                'spreads': len(period.get('spreads') or {}), 'totals': len(period.get('totals') or {}),
                                'team_totals': bool(period.get('team_totals')), 'meta': period.get('meta')}}

    return {'fixtures': len(groups), 'repeated_fixtures': len(repeated),
            'parent_id_patterns': sorted({tuple(sorted(str(e.get('parent_id')) == 'None' for e in v))
                                          for v in repeated.values()}),
            'examples': [{'fixture': ' | '.join(k), 'events': [describe(e) for e in v]}
                         for k, v in list(repeated.items())[:limit]]}


def main_line_report(kit, odds_api, raw=None):
    """Kit main lines (provider flag, otherwise the most balanced pair) against The Odds API's main lines."""
    def index(events):
        out = {}
        for event in events:
            kick = op.parse_time(event.get('kickoff_utc'))
            if kick is None:
                continue
            slot = kick.replace(minute=(kick.minute // 5) * 5, second=0, microsecond=0)
            out[(event['league_key'], op.iso(slot), op.team_key(event['home_team']),
                 op.team_key(event['away_team']))] = event
        return out

    def main(event, market):
        return next((x for x in event.get(market) or [] if x.get('main')), None)

    def limit(event, market, line):
        source = (raw or {}).get(str(event.get('provider_event_id')))
        period = op._kit_period(source) if source else None
        block = (period or {}).get('spreads' if market == 'asian_handicap' else 'totals') or {}
        for item in block.values() if isinstance(block, dict) else []:
            if isinstance(item, dict) and op.point(item.get('hdp' if market == 'asian_handicap' else 'points')) is not None:
                value = op.point(item.get('hdp' if market == 'asian_handicap' else 'points'))
                if value == line:
                    return item.get('max')
        return None

    a, b = index(kit), index(odds_api)
    rows, counts = [], {'asian_handicap': [0, 0], 'goal_lines': [0, 0]}
    for key in sorted(set(a) & set(b)):
        for market, first, second in (('asian_handicap', 'home', 'away'), ('goal_lines', 'over', 'under')):
            ours, theirs = main(a[key], market), main(b[key], market)
            if ours is None or theirs is None:
                continue
            same = ours['line'] == theirs['line']
            counts[market][0 if same else 1] += 1
            if not same:
                at_theirs = next((x for x in a[key].get(market) or [] if x['line'] == theirs['line']), None)
                rows.append({'league': key[0], 'kickoff_utc': key[1], 'match': f'{key[2]} v {key[3]}',
                             'market': market, 'kit_main': ours['line'],
                             'kit_prices': f"{ours[first]:.3f}/{ours[second]:.3f}",
                             'odds_api_main': theirs['line'],
                             'odds_api_prices': f"{theirs[first]:.3f}/{theirs[second]:.3f}",
                             'kit_at_odds_api_line': (f"{at_theirs[first]:.3f}/{at_theirs[second]:.3f}"
                                                      if at_theirs else 'absent'),
                             'kit_limits': f"{limit(a[key], market, ours['line'])}/"
                                           f"{limit(a[key], market, theirs['line'])}"})
    return {'agree': {k: v[0] for k, v in counts.items()}, 'disagree': {k: v[1] for k, v in counts.items()},
            'rows': rows}


def odds_api_client():
    from football_value_pipeline_v2_standalone import TheOddsAPI
    key = next((os.getenv(k, '').strip() for k in TheOddsAPI.KEY_ENV_NAMES if os.getenv(k, '').strip()), '')
    if not key:
        return None
    client = TheOddsAPI(key, force_refresh=True)
    client.router = None  # the raw Odds API, never routed
    return client


def odds_api_schedule(client, leagues, errors):
    """The Odds API's free events list (no credits) per league: the schedule the pipeline matches today."""
    from football_value_pipeline_v2_standalone import LEAGUES, THE_ODDS_API_BASE
    out = {}
    for league_key in leagues:
        league = LEAGUES[league_key]
        try:
            payload = client._get_json(
                f'{THE_ODDS_API_BASE}/sports/{league.odds_api_sport_key}/events',
                f'odds_provider_compare_events_{league_key}.json', ttl=timedelta(seconds=0), force_refresh=True,
                allow_stale=False, params={'apiKey': client.api_key, 'dateFormat': 'iso'})
        except Exception as exc:  # report and continue: one league must not hide the others
            errors[f'{op.THE_ODDS_API} events {league_key}'] = type(exc).__name__
            continue
        out[league_key] = [{'id': e.get('id'), 'home_team': e.get('home_team'), 'away_team': e.get('away_team'),
                            'kickoff_utc': e.get('commence_time')}
                           for e in payload or [] if isinstance(e, dict) and e.get('home_team')]
    return out


def odds_api_prices(client, leagues, aliases, errors, days=7):
    from football_value_pipeline_v2_standalone import LEAGUES, THE_ODDS_API_BASE
    start, end = client._window(datetime.now(timezone.utc), days)
    items = []
    for league_key in leagues:
        league = LEAGUES[league_key]
        try:
            payload = client._get_json(
                f'{THE_ODDS_API_BASE}/sports/{league.odds_api_sport_key}/odds',
                f'odds_provider_compare_{league_key}.json', ttl=timedelta(seconds=0), force_refresh=True,
                allow_stale=False,
                params={'apiKey': client.api_key, 'bookmakers': 'pinnacle', 'markets': 'h2h,totals,spreads',
                        'oddsFormat': 'decimal', 'dateFormat': 'iso', 'commenceTimeFrom': start,
                        'commenceTimeTo': end})
        except Exception as exc:
            errors[f'{op.THE_ODDS_API} odds {league_key}'] = type(exc).__name__
            continue
        fetched = datetime.now(timezone.utc)
        items += [e for e in (op.normalise_odds_api_event(x, league_key=league_key, fetched_at=fetched,
                                                           aliases=aliases) for x in payload or []) if e is not None]
    return items


def match_report(events, schedule, now=None):
    """Each board fixture in our competitions against The Odds API's schedule."""
    now = now or datetime.now(timezone.utc)
    matched, mismatched, no_reference = [], [], []
    for event in sorted(events, key=lambda e: (e['league_key'], e['kickoff_utc'], e['home_team'])):
        league = event['league_key']
        if league not in schedule:
            continue
        kick = op.parse_time(event['kickoff_utc'])
        near = [r for r in schedule[league]
                if op.parse_time(r['kickoff_utc']) is not None
                and abs((op.parse_time(r['kickoff_utc']) - kick).total_seconds()) <= MATCH_SECONDS]
        keys = (op.team_key(event['home_team']), op.team_key(event['away_team']))
        same = [r for r in near if (op.team_key(r['home_team']), op.team_key(r['away_team'])) == keys]
        row = {'league': league, 'kickoff_utc': event['kickoff_utc'],
               'board': f"{event['provider_home_team']} v {event['provider_away_team']}",
               'board_keys': f'{keys[0]} v {keys[1]}'}
        if same:
            matched.append(row)
        elif near:
            mismatched.append({**row, 'schedule_at_same_kickoff': [
                f"{r['home_team']} v {r['away_team']} ({op.team_key(r['home_team'])} v "
                f"{op.team_key(r['away_team'])})" for r in near]})
        else:
            horizon = max((op.parse_time(r['kickoff_utc']) for r in schedule[league]
                           if op.parse_time(r['kickoff_utc'])), default=None)
            no_reference.append({**row, 'beyond_schedule_horizon': bool(horizon and kick > horizon)})
    on_board = {(e['league_key'], op.team_key(e['home_team']), op.team_key(e['away_team'])) for e in events}
    board_end = max((op.parse_time(e['kickoff_utc']) for e in events), default=None)
    missing = []
    for league, rows in sorted(schedule.items()):
        for r in rows:
            kick = op.parse_time(r['kickoff_utc'])
            if (board_end and kick and now < kick <= board_end
                    and (league, op.team_key(r['home_team']), op.team_key(r['away_team'])) not in on_board):
                missing.append({'league': league, 'kickoff_utc': r['kickoff_utc'],
                                'schedule': f"{r['home_team']} v {r['away_team']}"})
    return {'matched': len(matched), 'mismatched': mismatched, 'no_schedule_fixture': no_reference,
            'schedule_not_on_board': missing, 'matched_fixtures': matched}


def price_summary(result):
    compared = result['prices_compared']
    outside = len(result['outside_tolerance'])
    return {'providers': result['providers'], 'fixtures': result['fixtures_quoted_by_all'],
            'prices_compared': compared, 'differences': len(result['differences']), 'outside_tolerance': outside,
            'share_outside': round(outside / compared, 4) if compared else None}


def _table(rows, columns):
    if not rows:
        return ['(none)', '']
    out = ['| ' + ' | '.join(columns) + ' |', '|' + '---|' * len(columns)]
    for row in rows:
        out.append('| ' + ' | '.join(str(row.get(c, '')).replace('|', '/') for c in columns) + ' |')
    return out + ['']


def markdown(report):
    lines = ['# Odds provider check', '', f"Run at {report['run_at_utc']}. Tolerance: "
             f"{report['tolerance']:.1%} of the lower price.", '', '## Requests', '']
    for name, log in report['requests'].items():
        lines.append(f'**{name}:** {len(log)} request(s); daily allowance '
                     f"{report['allowances'].get(name)}.")
        lines += _table([{'status': x.get('status', x.get('error')), 'seconds': x.get('seconds'),
                          'bytes': x.get('bytes', ''), 'headers': json.dumps(x.get('headers', {}))} for x in log],
                        ['status', 'seconds', 'bytes', 'headers'])
    usage = report.get('odds_api_usage')
    if usage is not None:
        lines += [f"**{op.THE_ODDS_API}:** {usage['calls']} request(s), {usage['credits_spent']} credit(s) spent; "
                  f"by endpoint {json.dumps(usage['by_endpoint'])}; known credits left {usage['remaining_total']}.",
                  '']
    for name, text in report['errors'].items():
        lines.append(f'- Not fetched: {name}: {text}')
    lines.append('')
    for name, leagues in report['leagues'].items():
        lines += [f'## League names ({name}: {leagues["board_events"]} match events on the board)', '']
        lines += _table([{'competition': k, 'configured': ' / '.join(v['configured_names']),
                          'events': v['events'],
                          'found as': '; '.join(f"{x['league_name']} (id {x['league_id']})" for x in v['found_as'])}
                         for k, v in leagues['competitions'].items()], ['competition', 'configured', 'events',
                                                                         'found as'])
        lines += ['Candidate board leagues:', '']
        lines += _table(leagues['candidates'], ['league_id', 'league_name', 'events'])
        lines += ['<details><summary>Every board league</summary>', '']
        lines += _table(leagues['all_leagues'], ['league_id', 'league_name', 'events'])
        lines += ['</details>', '']
    for name, match in report['team_names'].items():
        lines += [f'## Team names ({name} against The Odds API schedule)', '',
                  f"Matched: {match['matched']}; name mismatches: {len(match['mismatched'])}; no schedule fixture "
                  f"at that kickoff: {len(match['no_schedule_fixture'])}; schedule fixtures (up to the board's last "
                  f"kickoff) not on the board: {len(match['schedule_not_on_board'])}.", '', 'Name mismatches:', '']
        lines += _table([{**x, 'schedule_at_same_kickoff': '; '.join(x['schedule_at_same_kickoff'])}
                         for x in match['mismatched']],
                        ['league', 'kickoff_utc', 'board', 'board_keys', 'schedule_at_same_kickoff'])
        lines += ['No schedule fixture at that kickoff:', '']
        lines += _table(match['no_schedule_fixture'], ['league', 'kickoff_utc', 'board', 'beyond_schedule_horizon'])
        lines += ['Schedule fixtures not on the board:', '']
        lines += _table(match['schedule_not_on_board'], ['league', 'kickoff_utc', 'schedule'])
    for label, result in report['prices'].items():
        summary = price_summary(result)
        lines += [f'## Prices: {label}', '',
                  f"Fixtures quoted by both: {summary['fixtures']}; prices compared: {summary['prices_compared']}; "
                  f"differences: {summary['differences']}; outside tolerance: {summary['outside_tolerance']}"
                  + (f" ({summary['share_outside']:.2%})" if summary['share_outside'] is not None else '') + '.', '']
        names = list(result['providers'])
        rows = [{**{k: row[k] for k in ('league', 'kickoff_utc', 'match', 'price')},
                 **{n: f'{row[n]:.3f}' for n in names}, 'difference': f"{row['relative_difference']:.2%}",
                 'within': 'yes' if row['within_tolerance'] else 'NO'} for row in result['differences']]
        lines += ['<details><summary>Every difference</summary>', '']
        lines += _table(rows, ['league', 'kickoff_utc', 'match', 'price', *names, 'difference', 'within'])
        lines += ['</details>', '']
    main_lines = report.get('main_lines')
    if main_lines:
        lines += ['## Main lines (kit v The Odds API)', '',
                  f"Asian handicap: {main_lines['agree']['asian_handicap']} agree, "
                  f"{main_lines['disagree']['asian_handicap']} differ. Goal lines: "
                  f"{main_lines['agree']['goal_lines']} agree, {main_lines['disagree']['goal_lines']} differ.", '']
        lines += _table(main_lines['rows'], ['league', 'kickoff_utc', 'match', 'market', 'kit_main', 'kit_prices',
                                             'odds_api_main', 'odds_api_prices', 'kit_at_odds_api_line',
                                             'kit_limits'])
    for name, dup in report.get('duplicates', {}).items():
        lines += [f'## Repeated events ({name})', '',
                  f"Fixtures in our competitions: {dup['fixtures']}; listed more than once: "
                  f"{dup['repeated_fixtures']}; parent_id empty per repeat (True = empty): "
                  f"{dup['parent_id_patterns']}.", '', '<details><summary>Examples</summary>', '', '```json',
                  json.dumps(dup['examples'], indent=1, default=str, ensure_ascii=False)[:20000], '```',
                  '</details>', '']
    for name, shape in report['board_shape'].items():
        lines += [f'<details><summary>Board shape ({name})</summary>', '', '```json',
                  json.dumps(shape, indent=1, default=str)[:6000], '```', '</details>', '']
    return '\n'.join(lines) + '\n'


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--leagues', nargs='*', default=None, help='league keys (default: every configured league)')
    parser.add_argument('--odds-api', action='store_true',
                        help="compare against The Odds API's Pinnacle prices (3 credits per league)")
    parser.add_argument('--odds-api-leagues', nargs='*', default=None,
                        help='leagues for the --odds-api price check (default: every league checked)')
    parser.add_argument('--api-key-source', choices=('dotenv', 'environment'), default='dotenv')
    args = parser.parse_args(argv)
    from api_key_config import load_api_keys
    load_api_keys(args.api_key_source)
    config = op.load_config()
    leagues = {k: v for k, v in config['leagues'].items() if not args.leagues or k in args.leagues}
    aliases = op.load_aliases()
    tolerance = float(config['price_tolerance']['decimal_odds_relative'])
    errors = {}
    boards, requests_made = kit_boards(config, errors)
    events = {name: op.normalise_kit_board(payload, provider=name, fetched_at=fetched, leagues=leagues,
                                           aliases=aliases) for name, (payload, fetched) in boards.items()}
    client = odds_api_client()
    schedule = odds_api_schedule(client, leagues, errors) if client else {}
    if client is None:
        errors[op.THE_ODDS_API] = 'not_configured'
    prices = {}
    kit_names = list(events)
    if len(kit_names) >= 2:
        prices[f'{kit_names[0]} v {kit_names[1]}'] = op.compare_providers(
            {n: events[n] for n in kit_names[:2]}, tolerance)
    if args.odds_api and client and kit_names:
        chosen = [k for k in leagues if not args.odds_api_leagues or k in args.odds_api_leagues]
        items = odds_api_prices(client, chosen, aliases, errors)
        board = [e for e in events[kit_names[0]] if e['league_key'] in chosen]
        prices[f'{kit_names[0]} v {op.THE_ODDS_API}'] = op.compare_providers(
            {kit_names[0]: board, op.THE_ODDS_API: items}, tolerance)
        raw = {str(e.get('event_id')): e for e in op.kit_events(boards[kit_names[0]][0])}
        main_lines = main_line_report(board, items, raw)
    else:
        main_lines = None
    report = {
        'run_at_utc': op.iso(datetime.now(timezone.utc)), 'tolerance': tolerance,
        'requests': requests_made,
        'allowances': {n: config['providers'][n].get('daily_allowance') for n in requests_made},
        'odds_api_usage': client.usage.summary() if client else None,
        'errors': errors,
        'leagues': {name: league_report(payload, leagues) for name, (payload, _) in boards.items()},
        'board_shape': {name: board_shape(payload, leagues) for name, (payload, _) in list(boards.items())[:1]},
        'team_names': {name: match_report(events[name], schedule) for name in kit_names},
        'prices': prices,
        'price_summary': {label: price_summary(result) for label, result in prices.items()},
        'main_lines': main_lines,
        'duplicates': {name: duplicate_report(payload, leagues) for name, (payload, _) in boards.items()},
    }
    args.output.mkdir(parents=True, exist_ok=True)
    (args.output / 'odds_provider_compare.json').write_text(json.dumps(report, indent=2, sort_keys=True,
                                                                       default=str), encoding='utf-8')
    text = markdown(report)
    (args.output / 'odds_provider_compare.md').write_text(text, encoding='utf-8')
    print(text[:4000])
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
