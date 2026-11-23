"""One odds-provider adapter: the same normalised Pinnacle data whatever the source.

Off by default (`odds_provider_config.json` "enabled": false). With the switch off nothing in this module runs
and every output is byte-identical to before. With it on, every Odds API request the pipeline, the closing
collector and the shadow corner list make goes through `OddsProviderRouter.fetch`, which asks the providers
in the configured order:

  1. pinnapi   (PINNAPI_API_KEY)   Pinnacle kit API, /kit/v1
  2. pinnodds  (PINNODDS_API_KEY)  the same kit API on another host
  3. The Odds API (existing keys)  final fallback only: called for a request only when every kit provider
                                   failed for it (error, timeout, 429, daily allowance exhausted)

Whatever answered, the response is normalised (`normalise_kit_event`, `normalise_odds_api_event`: Pinnacle
only; 1X2, Asian handicap lines, goal lines, team totals, corners when offered, kickoff, canonical team names,
fetch time) and handed back in The Odds API v4 event shape (`to_odds_api_event`), so the existing parsers run
unchanged and identical prices give byte-identical lists through any provider. The Odds API parser itself is
untouched: old saved runs, grading and replay read it exactly as before.

Each kit key's daily count and Retry-After are tracked in this process and seeded from the committed usage log
(`odds_api_usage.LOG`, an "odds_provider" block in each record), so a closing session knows what the forecast
run already spent today. A request starts from the first provider every time, so the router moves back to
pinnapi as soon as its allowance resets (UTC midnight) or its Retry-After has passed. Every change of serving
provider is a switch: recorded in the run's summary, the usage log and (via model_activity) the activity log.

No key value, URL with a key, or response text is ever stored.
"""
from __future__ import annotations

import json
import math
import os
import re
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Callable, Dict, Iterable, List, Mapping, Optional, Sequence, Tuple

CONFIG = Path(__file__).with_name('odds_provider_config.json')
ALIASES = Path(__file__).with_name('odds_provider_team_aliases.json')
SCHEMA = 'odds-provider-config-v1'
NORMALISED = 'normalised-pinnacle-odds-v1'
KIT, ODDS_API = 'pinnacle-kit-v1', 'the-odds-api-v4'
THE_ODDS_API = 'the-odds-api'
KIT_FIXTURES_PATH = '/kit/v1/prematch/fixtures'
USER_AGENT = 'football-value-pipeline/2.0 (+research; odds-provider-adapter)'

# Failure reasons that pass a request to the next provider.
NOT_CONFIGURED, ERROR, TIMEOUT, RATE_LIMITED, DAILY_ALLOWANCE, RETRY_AFTER = (
    'not_configured', 'error', 'timeout', 'rate_limited', 'daily_allowance', 'retry_after')
FAILURES = (NOT_CONFIGURED, ERROR, TIMEOUT, RATE_LIMITED, DAILY_ALLOWANCE, RETRY_AFTER)

# Odds API market keys the adapter can emit, by normalised market.
H2H, SPREADS, ALT_SPREADS, TOTALS, ALT_TOTALS = 'h2h', 'spreads', 'alternate_spreads', 'totals', 'alternate_totals'
TEAM_TOTALS, ALT_TEAM_TOTALS, CORNERS, DC, DNB = ('team_totals', 'alternate_team_totals', 'alternate_totals_corners',
                                                 'double_chance', 'draw_no_bet')
ODDS_API_EVENT_ID = re.compile(r'[0-9a-f]{32}')


# --- configuration -----------------------------------------------------------------------------------------------

def load_config(path: Path | str = CONFIG) -> dict:
    """The provider settings; refuses a file that leaves a rule out rather than guessing it."""
    data = json.loads(Path(path).read_text(encoding='utf-8'))
    if data.get('schema') != SCHEMA:
        raise ValueError(f'{path}: schema must be {SCHEMA}')
    for key in ('enabled', 'order', 'providers', 'leagues', 'board_ttl_seconds', 'price_tolerance'):
        if key not in data:
            raise ValueError(f'{path}: missing {key}')
    if not isinstance(data['enabled'], bool):
        raise ValueError(f'{path}: enabled must be true or false')
    order = data['order']
    if not order or order[-1] != THE_ODDS_API or order.count(THE_ODDS_API) != 1:
        raise ValueError(f'{path}: The Odds API must be the last provider, and only once')
    for name in order:
        provider = data['providers'].get(name)
        if not isinstance(provider, dict) or provider.get('api') not in (KIT, ODDS_API):
            raise ValueError(f'{path}: provider {name} needs an api of {KIT} or {ODDS_API}')
        if provider['api'] == KIT:
            for key in ('base_url', 'key_env', 'daily_allowance', 'timeout_seconds'):
                if key not in provider:
                    raise ValueError(f'{path}: provider {name} missing {key}')
            allowance = provider['daily_allowance']
            if allowance is not None and (isinstance(allowance, bool) or not isinstance(allowance, int) or allowance < 1):
                raise ValueError(f'{path}: {name} daily_allowance must be a positive whole number or null (no cap)')
    return data


def enabled(path: Path | str = CONFIG) -> bool:
    """The switch. A missing file is off; a malformed one raises (never silently on or off)."""
    path = Path(path)
    return path.exists() and load_config(path)['enabled']


def load_aliases(path: Path | str = ALIASES) -> Dict[str, Dict[str, str]]:
    """Reviewed provider-name -> canonical-name aliases, per league key."""
    path = Path(path)
    if not path.exists():
        return {}
    data = json.loads(path.read_text(encoding='utf-8'))
    return {k: dict(v) for k, v in (data.get('aliases') or {}).items() if isinstance(v, dict)}


def canonical_name(name: str, league_key: str, aliases: Mapping[str, Mapping[str, str]]) -> Tuple[str, str]:
    """(canonical name, how it was found). A reviewed alias first; otherwise the provider's own spelling, which
    the pipeline's strict cross-provider key (canonical_team_key) then matches. Never fuzzy."""
    name = str(name or '').strip()
    alias = (aliases.get(league_key) or {}).get(name) or (aliases.get('*') or {}).get(name)
    return (alias, 'alias') if alias else (name, 'provider')


def team_key(name: str) -> str:
    from football_value_pipeline_v2_standalone import canonical_team_key
    return canonical_team_key(str(name or ''))


# --- time helpers ------------------------------------------------------------------------------------------------

def iso(value: Optional[datetime]) -> Optional[str]:
    """Odds API style UTC stamp: 2026-11-22T17:24:09Z."""
    if value is None:
        return None
    return value.astimezone(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00', 'Z')


def parse_time(value: Any) -> Optional[datetime]:
    if value is None or value == '':
        return None
    if isinstance(value, bool):
        return None
    if isinstance(value, (int, float)):
        if not math.isfinite(float(value)):
            return None
        seconds = float(value) / (1000.0 if float(value) > 1e11 else 1.0)  # epoch ms or s
        return datetime.fromtimestamp(seconds, timezone.utc)
    try:
        stamp = datetime.fromisoformat(str(value).replace('Z', '+00:00'))
    except ValueError:
        return None
    return stamp if stamp.tzinfo else stamp.replace(tzinfo=timezone.utc)


def price(value: Any) -> Optional[float]:
    if isinstance(value, bool):
        return None
    try:
        number = float(value)
    except (TypeError, ValueError):
        return None
    return number if math.isfinite(number) and number > 1.0 else None


def point(value: Any) -> Optional[float]:
    if isinstance(value, bool):
        return None
    try:
        number = float(value)
    except (TypeError, ValueError):
        return None
    return number + 0.0 if math.isfinite(number) else None  # + 0.0 turns -0.0 into 0.0


# --- normalised events -------------------------------------------------------------------------------------------
#
# {schema, provider, provider_event_id, league_key, kickoff_utc, home_team, away_team, provider_home_team,
#  provider_away_team, team_names, fetched_at_utc, stale,
#  one_x_two: {home, draw, away, updated_at_utc} | None,
#  asian_handicap: [{line (home handicap), home, away, main, updated_at_utc}],
#  goal_lines: [{line, over, under, main, updated_at_utc}],
#  team_totals: {home: [{line, over, under, main, updated_at_utc}], away: [...]},
#  corners: [{line, over, under, main, updated_at_utc}],
#  double_chance: {home_or_draw, away_or_draw, home_or_away, updated_at_utc} | None   (The Odds API only)
#  draw_no_bet: {home, away, updated_at_utc} | None                                   (The Odds API only)}


def _main_flags(lines: List[dict], first: str, second: str) -> None:
    """Mark the main line: the provider's own flag when it gives one, otherwise the most balanced pair (Pinnacle's
    main line), ties to the higher limit and then the lower line. Exactly one main line per market."""
    if not lines:
        return
    flagged = [x for x in lines if x.get('_alternate') is False]
    if flagged:
        main = min(flagged, key=lambda x: x['line'])
    else:
        main = min(lines, key=lambda x: (round(abs(1 / x[first] - 1 / x[second]), 12), -(x.get('_max') or 0), x['line']))
    for item in lines:
        item['main'] = item is main
        item.pop('_alternate', None)
        item.pop('_max', None)


def _kit_period(event: Mapping) -> Optional[Mapping]:
    periods = event.get('periods')
    items = periods.values() if isinstance(periods, dict) else periods if isinstance(periods, list) else []
    for period in items:
        if isinstance(period, dict) and str(period.get('number', '')) in ('0', '0.0'):
            return period
    if isinstance(periods, dict) and isinstance(periods.get('num_0'), dict):
        return periods['num_0']
    return None


def _alternate_flag(item: Mapping) -> Optional[bool]:
    value = item.get('is_alternate', item.get('isAlternate'))
    return value if isinstance(value, bool) else None


def _kit_pairs(block: Any, line_key: str, first: str, second: str, stamp: Optional[str],
               *, negate: bool = False) -> List[dict]:
    out = []
    values = block.values() if isinstance(block, dict) else block if isinstance(block, list) else []
    seen = set()
    for item in values:
        if not isinstance(item, dict):
            continue
        line, a, b = point(item.get(line_key)), price(item.get(first)), price(item.get(second))
        if line is None or a is None or b is None or line in seen:
            continue
        seen.add(line)
        out.append({'line': line, first: a, second: b, 'updated_at_utc': stamp,
                    '_alternate': _alternate_flag(item), '_max': point(item.get('max'))})
    out.sort(key=lambda x: x['line'])
    _main_flags(out, first, second)
    return out


def _kit_team_totals(period: Mapping, stamp: Optional[str]) -> Dict[str, List[dict]]:
    result = {}
    every, primary = period.get('team_totals'), period.get('team_total')
    for side in ('home', 'away'):
        lines = _kit_pairs((every or {}).get(side) if isinstance(every, dict) else None, 'points', 'over', 'under',
                           stamp)
        if not lines and isinstance(primary, dict) and isinstance(primary.get(side), dict):
            lines = _kit_pairs([primary[side]], 'points', 'over', 'under', stamp)
        result[side] = lines
    return result


def is_corner_child(event: Mapping) -> bool:
    """Pinnacle prices corners as a child event (parent_id set) whose teams read "Arsenal (Corners)"."""
    names = f"{event.get('home', '')} {event.get('away', '')} {event.get('league_name', '')}".casefold()
    return bool(event.get('parent_id')) and 'corner' in names


def normalise_kit_event(event: Mapping, *, provider: str, league_key: str, fetched_at: datetime,
                        quotes_at: Optional[datetime], stale: bool,
                        aliases: Mapping[str, Mapping[str, str]], corners: Optional[Mapping] = None) -> Optional[dict]:
    """One kit event (period 0, full time) in the normalised form; None without an id, teams or kickoff."""
    event_id, home_raw, away_raw = event.get('event_id'), event.get('home'), event.get('away')
    kickoff = parse_time(event.get('starts') if event.get('starts') is not None else event.get('start_ts'))
    if event_id in (None, '') or not home_raw or not away_raw or kickoff is None:
        return None
    home, how_home = canonical_name(home_raw, league_key, aliases)
    away, how_away = canonical_name(away_raw, league_key, aliases)
    stamp = iso(quotes_at)
    period = _kit_period(event) or {}
    money = period.get('money_line') if isinstance(period.get('money_line'), dict) else {}
    one_x_two = None
    if all(price(money.get(k)) is not None for k in ('home', 'draw', 'away')):
        one_x_two = {'home': price(money['home']), 'draw': price(money['draw']), 'away': price(money['away']),
                     'updated_at_utc': stamp}
    corner_lines: List[dict] = []
    if corners is not None:
        corner_period = _kit_period(corners) or {}
        corner_lines = [{**x, 'main': False}  # corners have one market, so no main line
                        for x in _kit_pairs(corner_period.get('totals'), 'points', 'over', 'under', stamp)]
    return {
        'schema': NORMALISED, 'provider': provider, 'provider_event_id': str(event_id), 'league_key': league_key,
        'kickoff_utc': iso(kickoff), 'home_team': home, 'away_team': away,
        'provider_home_team': str(home_raw), 'provider_away_team': str(away_raw),
        'team_names': 'alias' if 'alias' in (how_home, how_away) else 'provider',
        'fetched_at_utc': iso(fetched_at), 'stale': bool(stale),
        'one_x_two': one_x_two,
        'asian_handicap': _kit_pairs(period.get('spreads'), 'hdp', 'home', 'away', stamp),
        'goal_lines': _kit_pairs(period.get('totals'), 'points', 'over', 'under', stamp),
        'team_totals': _kit_team_totals(period, stamp),
        'corners': corner_lines,
        'double_chance': None, 'draw_no_bet': None,
    }


def kit_events(payload: Any) -> List[Mapping]:
    events = payload.get('events') if isinstance(payload, dict) else payload
    return [e for e in (events if isinstance(events, list) else []) if isinstance(e, dict)]


def kit_quotes_time(payload: Any, fetched_at: datetime) -> Tuple[Optional[datetime], bool]:
    """The kit API gives no per-quote Pinnacle timestamp. A board that is not stale is current as of the fetch;
    a stale board's quotes date from its last real price change (or have no time, so freshness rules drop them)."""
    stale = bool(payload.get('stale')) if isinstance(payload, dict) else False
    if not stale:
        return fetched_at, False
    return parse_time(payload.get('last_change')) if isinstance(payload, dict) else None, True


def league_of(event: Mapping, leagues: Mapping[str, Mapping]) -> Optional[str]:
    """Our league key for a kit event, from the configured Pinnacle league ids or names (exact match only)."""
    league_id, name = event.get('league_id'), str(event.get('league_name') or '').strip().casefold()
    for key, spec in leagues.items():
        if league_id is not None and str(league_id) in {str(x) for x in spec.get('pinnacle_league_ids', [])}:
            return key
        if name and name in {str(x).strip().casefold() for x in spec.get('pinnacle_league_names', [])}:
            return key
    return None


def normalise_kit_board(payload: Any, *, provider: str, fetched_at: datetime, leagues: Mapping[str, Mapping],
                        aliases: Mapping[str, Mapping[str, str]]) -> List[dict]:
    """Every configured-league event on one kit board, corners attached from their child events."""
    quotes_at, stale = kit_quotes_time(payload, fetched_at)
    events = kit_events(payload)
    children = {str(e.get('parent_id')): e for e in events if is_corner_child(e)}
    out = []
    for event in events:
        # A child event (parent_id set) is never a match: corner children attach above; the others are Pinnacle
        # specials under the same teams and league (no draw, no lines; seen on the live board, 23 Nov 2026).
        if event.get('parent_id') or event.get('event_type') not in (None, 'prematch'):
            continue
        key = league_of(event, leagues)
        if key is None:
            continue
        item = normalise_kit_event(event, provider=provider, league_key=key, fetched_at=fetched_at,
                                   quotes_at=quotes_at, stale=stale, aliases=aliases,
                                   corners=children.get(str(event.get('event_id'))))
        if item is not None:
            out.append(item)
    return out


def _odds_api_pinnacle(event: Mapping) -> Optional[Mapping]:
    for book in event.get('bookmakers') or []:
        if isinstance(book, dict) and str(book.get('key', '')).lower() == 'pinnacle':
            return book
    return None


def _odds_api_markets(book: Mapping) -> Dict[str, Mapping]:
    return {m.get('key'): m for m in book.get('markets') or [] if isinstance(m, dict)}


def _odds_api_stamp(book: Mapping, market: Mapping) -> Optional[str]:
    return iso(parse_time(market.get('last_update') or book.get('last_update')))


def _odds_api_lines(markets: Mapping[str, Mapping], book: Mapping, main_key: str, alt_key: str,
                    side_of: Callable[[Mapping], Optional[str]], first: str, second: str,
                    flip_second: bool, description: Optional[str] = None) -> List[dict]:
    """Complete same-line pairs from a main and an alternate market; the main market's line is the main line."""
    lines: Dict[float, dict] = {}
    for key in (main_key, alt_key):
        market = markets.get(key)
        if not market:
            continue
        stamp = _odds_api_stamp(book, market)
        pairs: Dict[float, Dict[str, float]] = {}
        for outcome in market.get('outcomes') or []:
            if not isinstance(outcome, dict):
                continue
            if description is not None and team_key(outcome.get('description')) != team_key(description):
                continue
            side, line, value = side_of(outcome), point(outcome.get('point')), price(outcome.get('price'))
            if side is None or line is None or value is None:
                continue
            if side == second and flip_second:
                line = -line + 0.0
            pairs.setdefault(line, {})[side] = value
        for line, pair in pairs.items():
            if set(pair) != {first, second}:
                continue
            if line in lines and key == alt_key:
                continue  # the main market's quote stands
            lines[line] = {'line': line, first: pair[first], second: pair[second], 'main': key == main_key,
                           'updated_at_utc': stamp}
    return [lines[k] for k in sorted(lines)]


def normalise_odds_api_event(event: Mapping, *, league_key: str, fetched_at: datetime,
                             aliases: Mapping[str, Mapping[str, str]], provider: str = THE_ODDS_API) -> Optional[dict]:
    """Pinnacle's quotes in one Odds API v4 event, in the normalised form (other bookmakers are dropped)."""
    event_id, home_raw, away_raw = event.get('id'), event.get('home_team'), event.get('away_team')
    kickoff = parse_time(event.get('commence_time'))
    if not event_id or not home_raw or not away_raw or kickoff is None:
        return None
    home, how_home = canonical_name(home_raw, league_key, aliases)
    away, how_away = canonical_name(away_raw, league_key, aliases)
    book = _odds_api_pinnacle(event) or {}
    markets = _odds_api_markets(book)
    home_key, away_key = team_key(home_raw), team_key(away_raw)

    def team_side(outcome):
        key = team_key(outcome.get('name'))
        return 'home' if key == home_key else 'away' if key == away_key else None

    def over_under(outcome):
        side = str(outcome.get('name') or '').strip().lower()
        return side if side in ('over', 'under') else None

    one_x_two = None
    if markets.get(H2H):
        prices = {}
        for outcome in markets[H2H].get('outcomes') or []:
            if not isinstance(outcome, dict):
                continue
            side = 'draw' if str(outcome.get('name') or '').strip().lower() == 'draw' else team_side(outcome)
            if side and price(outcome.get('price')) is not None:
                prices[side] = price(outcome['price'])
        if set(prices) == {'home', 'draw', 'away'}:
            one_x_two = {**{k: prices[k] for k in ('home', 'draw', 'away')},
                         'updated_at_utc': _odds_api_stamp(book, markets[H2H])}
    double_chance = draw_no_bet = None
    if markets.get(DC):
        named = {}
        for outcome in markets[DC].get('outcomes') or []:
            if not isinstance(outcome, dict) or price(outcome.get('price')) is None:
                continue
            parts = {team_key(p) for p in str(outcome.get('name') or '').split(' or ')}
            label = ('home_or_draw' if parts == {home_key, team_key('Draw')} else
                     'away_or_draw' if parts == {away_key, team_key('Draw')} else
                     'home_or_away' if parts == {home_key, away_key} else None)
            if label:
                named[label] = price(outcome['price'])
        if set(named) == {'home_or_draw', 'away_or_draw', 'home_or_away'}:
            double_chance = {**named, 'updated_at_utc': _odds_api_stamp(book, markets[DC])}
    if markets.get(DNB):
        named = {team_side(o): price(o.get('price')) for o in markets[DNB].get('outcomes') or []
                 if isinstance(o, dict) and team_side(o) and price(o.get('price')) is not None}
        if set(named) == {'home', 'away'}:
            draw_no_bet = {'home': named['home'], 'away': named['away'],
                           'updated_at_utc': _odds_api_stamp(book, markets[DNB])}
    return {
        'schema': NORMALISED, 'provider': provider, 'provider_event_id': str(event_id), 'league_key': league_key,
        'kickoff_utc': iso(kickoff), 'home_team': home, 'away_team': away,
        'provider_home_team': str(home_raw), 'provider_away_team': str(away_raw),
        'team_names': 'alias' if 'alias' in (how_home, how_away) else 'provider',
        'fetched_at_utc': iso(fetched_at), 'stale': False,
        'one_x_two': one_x_two,
        'asian_handicap': _odds_api_lines(markets, book, SPREADS, ALT_SPREADS, team_side, 'home', 'away', True),
        'goal_lines': _odds_api_lines(markets, book, TOTALS, ALT_TOTALS, over_under, 'over', 'under', False),
        'team_totals': {side: _odds_api_lines(markets, book, TEAM_TOTALS, ALT_TEAM_TOTALS, over_under, 'over',
                                              'under', False, description=str(raw))
                        for side, raw in (('home', home_raw), ('away', away_raw))},
        'corners': [{**x, 'main': False} for x in
                    _odds_api_lines(markets, book, '', CORNERS, over_under, 'over', 'under', False)],
        'double_chance': double_chance, 'draw_no_bet': draw_no_bet,
    }


def _market(key: str, outcomes: List[dict], stamps: Iterable[Optional[str]]) -> Optional[dict]:
    known = [s for s in stamps if s]
    if not outcomes:
        return None
    return {'key': key, 'last_update': max(known) if known else None, 'outcomes': outcomes}


def _line_outcomes(lines: Sequence[dict], *, home: str, away: str, kind: str,
                   description: Optional[str] = None) -> List[dict]:
    if kind == 'handicap':
        return ([{'name': home, 'price': x['home'], 'point': x['line']} for x in lines] +
                [{'name': away, 'price': x['away'], 'point': -x['line'] + 0.0} for x in lines])
    extra = {} if description is None else {'description': description}
    return ([{'name': 'Over', **extra, 'price': x['over'], 'point': x['line']} for x in lines] +
            [{'name': 'Under', **extra, 'price': x['under'], 'point': x['line']} for x in lines])


def to_odds_api_event(event: Mapping, markets: Iterable[str], *, event_id: Optional[str] = None,
                      home: Optional[str] = None, away: Optional[str] = None) -> dict:
    """A normalised event as one Odds API v4 event with a single Pinnacle book, holding only the requested markets.

    The main line goes in the main market (spreads, totals, team_totals) and every other line in the alternate
    one. event_id/home/away override the event's own identity (the run's schedule identity)."""
    wanted = set(markets)
    home = home or event['home_team']
    away = away or event['away_team']
    out: List[dict] = []

    def add(market: Optional[dict]):
        if market is not None and market['key'] in wanted:
            out.append(market)

    one = event.get('one_x_two')
    if one:
        add(_market(H2H, [{'name': home, 'price': one['home']}, {'name': away, 'price': one['away']},
                          {'name': 'Draw', 'price': one['draw']}], [one.get('updated_at_utc')]))
    for main_key, alt_key, lines, kind in ((SPREADS, ALT_SPREADS, event.get('asian_handicap') or [], 'handicap'),
                                           (TOTALS, ALT_TOTALS, event.get('goal_lines') or [], 'total')):
        main = [x for x in lines if x.get('main')]
        alternates = [x for x in lines if not x.get('main')]
        add(_market(main_key, _line_outcomes(main, home=home, away=away, kind=kind),
                    [x.get('updated_at_utc') for x in main]))
        add(_market(alt_key, _line_outcomes(alternates, home=home, away=away, kind=kind),
                    [x.get('updated_at_utc') for x in alternates]))
    teams = event.get('team_totals') or {}
    for key, pick_main in ((TEAM_TOTALS, True), (ALT_TEAM_TOTALS, False)):
        outcomes, stamps = [], []
        for side, name in (('home', home), ('away', away)):
            lines = [x for x in teams.get(side) or [] if bool(x.get('main')) == pick_main]
            outcomes += _line_outcomes(lines, home=home, away=away, kind='total', description=name)
            stamps += [x.get('updated_at_utc') for x in lines]
        add(_market(key, outcomes, stamps))
    corners = event.get('corners') or []
    add(_market(CORNERS, _line_outcomes(corners, home=home, away=away, kind='total'),
                [x.get('updated_at_utc') for x in corners]))
    dc = event.get('double_chance')
    if dc:
        add(_market(DC, [{'name': f'{home} or Draw', 'price': dc['home_or_draw']},
                         {'name': f'{away} or Draw', 'price': dc['away_or_draw']},
                         {'name': f'{home} or {away}', 'price': dc['home_or_away']}], [dc.get('updated_at_utc')]))
    dnb = event.get('draw_no_bet')
    if dnb:
        add(_market(DNB, [{'name': home, 'price': dnb['home']}, {'name': away, 'price': dnb['away']}],
                    [dnb.get('updated_at_utc')]))
    books = [{'key': 'pinnacle', 'title': 'Pinnacle', 'markets': out}] if out else []
    return {'id': str(event_id or event['provider_event_id']), 'sport_key': None,
            'commence_time': event['kickoff_utc'], 'home_team': home, 'away_team': away, 'bookmakers': books}


# --- one request through the providers ---------------------------------------------------------------------------

class ProviderFailure(Exception):
    def __init__(self, reason: str, detail: str = '', *, retry_after_seconds: Optional[float] = None,
                 http_status: Optional[int] = None, window: Optional[str] = None):
        super().__init__(detail or reason)
        self.reason, self.detail = reason, detail
        self.retry_after_seconds, self.http_status, self.window = retry_after_seconds, http_status, window


@dataclass
class ProviderRequest:
    """One Odds API request the pipeline would make, described so any provider can answer it.

    kind: 'events' | 'odds' | 'event_odds'. window: (from, to) ISO stamps for events/odds. identity: kickoff_utc,
    home_team, away_team of the requested event when the caller knows it (closing, corners)."""
    kind: str
    league_key: str
    sport_key: str
    markets: Tuple[str, ...] = ()
    window: Optional[Tuple[str, str]] = None
    event_id: Optional[str] = None
    identity: Optional[Mapping[str, Any]] = None
    max_age_seconds: Optional[float] = None


def _next_utc_midnight(now: datetime) -> datetime:
    return datetime.combine((now + timedelta(days=1)).date(), datetime.min.time(), timezone.utc)


def retry_after(response, now: datetime) -> Tuple[Optional[float], Optional[str]]:
    """Seconds to wait and the limit window from a 429: the Retry-After header, else retry_after_ms; a daily
    window waits until UTC midnight."""
    window, seconds = None, None
    try:
        body = response.json()
    except ValueError:
        body = None
    if isinstance(body, dict):
        window = str(body.get('window') or '') or None
        ms = point(body.get('retry_after_ms'))
        if ms is not None and ms >= 0:
            seconds = ms / 1000.0
    header = str(response.headers.get('Retry-After', '') or '').strip()
    if header.isdigit() and len(header) <= 9:
        seconds = float(header)
    if window == 'day':
        seconds = max(seconds or 0.0, (_next_utc_midnight(now) - now).total_seconds())
    return seconds, window


class KitProvider:
    """The Pinnacle kit API (pinnapi, pinnodds): one board request returns every soccer event with all lines."""

    def __init__(self, name: str, spec: Mapping[str, Any], session=None):
        import requests
        self.name, self.spec = name, dict(spec)
        self.session = session or requests.Session()

    def key(self) -> str:
        return os.getenv(str(self.spec['key_env']), '').strip()

    def board(self, now: datetime) -> Any:
        import requests
        key = self.key()
        if not key:
            raise ProviderFailure(NOT_CONFIGURED, f'{self.spec["key_env"]} not set')
        try:
            response = self.session.get(
                str(self.spec['base_url']).rstrip('/') + KIT_FIXTURES_PATH,
                params={'sport_id': 1, 'line_meta': 1},
                headers={'x-portal-apikey': key, 'User-Agent': USER_AGENT, 'Accept': 'application/json'},
                timeout=float(self.spec['timeout_seconds']))
        except requests.Timeout:
            raise ProviderFailure(TIMEOUT, 'request timed out') from None
        except requests.RequestException as exc:
            raise ProviderFailure(ERROR, type(exc).__name__) from None
        if response.status_code == 429:
            seconds, window = retry_after(response, now)
            raise ProviderFailure(DAILY_ALLOWANCE if window == 'day' else RATE_LIMITED, 'HTTP 429',
                                  retry_after_seconds=seconds, http_status=429, window=window)
        if not 200 <= response.status_code < 300:
            code = ''
            try:
                body = response.json()
                code = str(body.get('error') or '')[:40] if isinstance(body, dict) else ''
            except ValueError:
                pass
            raise ProviderFailure(ERROR, f'HTTP {response.status_code}{" " + code if code else ""}',
                                  http_status=response.status_code)
        try:
            payload = response.json()
        except ValueError:
            raise ProviderFailure(ERROR, 'invalid JSON') from None
        if not isinstance(payload, dict) or not isinstance(payload.get('events'), list):
            raise ProviderFailure(ERROR, 'unexpected response shape')
        return payload


@dataclass
class _State:
    day: str = ''
    requests_today: int = 0
    blocked_until: Optional[datetime] = None
    requests_by_day: Dict[str, int] = field(default_factory=dict)  # this process only
    failures: Dict[str, int] = field(default_factory=dict)
    served: Dict[str, int] = field(default_factory=dict)


class OddsProviderRouter:
    """Asks the providers in order for each request; see the module docstring."""

    def __init__(self, config: Mapping[str, Any], *, clock: Callable[[], datetime] = None,
                 aliases: Optional[Mapping[str, Mapping[str, str]]] = None, sessions: Optional[Mapping] = None,
                 seed: Iterable[Mapping] = ()):
        self.config = dict(config)
        self.order: List[str] = list(config['order'])
        self.clock = clock or (lambda: datetime.now(timezone.utc))
        self.aliases = load_aliases() if aliases is None else dict(aliases)
        self.leagues = dict(config['leagues'])
        self.kit = {name: KitProvider(name, config['providers'][name], (sessions or {}).get(name))
                    for name in self.order if config['providers'][name]['api'] == KIT}
        self.state = {name: _State() for name in self.order}
        self.boards: Dict[str, Tuple[datetime, List[dict]]] = {}
        self.identities: Dict[Tuple[str, str], Dict[str, str]] = {}   # (league, provider id) -> schedule identity
        self.schedule: Dict[str, List[Dict[str, str]]] = {}          # league -> identities from the schedule
        self.odds_api_ids: Dict[Tuple[str, str], str] = {}           # (league, schedule id) -> Odds API id
        self.switches: List[dict] = []
        self.current: Optional[str] = self.order[0]  # who serves requests now; a change is a switch
        self.not_found = 0
        self.unmapped: Dict[str, int] = {}
        self._seed(seed)

    # --- daily counts and Retry-After, seeded from the committed usage log ---

    def _seed(self, records: Iterable[Mapping]) -> None:
        today = self.clock().date().isoformat()
        for record in records:
            block = record.get('odds_provider') if isinstance(record, Mapping) else None
            for name, values in ((block or {}).get('providers') or {}).items():
                if name not in self.state or not isinstance(values, Mapping):
                    continue
                state = self._today(name)
                state.requests_today += int((values.get('requests_by_utc_day') or {}).get(today) or 0)
                until = parse_time(values.get('blocked_until_utc'))
                if until is not None and (state.blocked_until is None or until > state.blocked_until):
                    state.blocked_until = until

    def _today(self, name: str) -> _State:
        state, day = self.state[name], self.clock().date().isoformat()
        if state.day != day:
            state.day, state.requests_today = day, 0  # the daily allowance resets at UTC midnight
        return state

    def _available(self, name: str) -> Optional[str]:
        """None when this provider may be asked now, otherwise why not (no request is made)."""
        if name == THE_ODDS_API:
            return None
        state, now = self._today(name), self.clock()
        if not self.kit[name].key():
            return NOT_CONFIGURED
        if state.blocked_until is not None and now < state.blocked_until:
            return RETRY_AFTER
        allowance = self.config['providers'][name]['daily_allowance']
        if allowance is not None and state.requests_today >= allowance:
            return DAILY_ALLOWANCE
        return None

    def _count(self, name: str) -> None:
        state = self._today(name)
        state.requests_today += 1
        state.requests_by_day[state.day] = state.requests_by_day.get(state.day, 0) + 1

    def _fail(self, name: str, reason: str) -> None:
        failures = self.state[name].failures
        failures[reason] = failures.get(reason, 0) + 1

    # --- boards ---

    def _board(self, name: str, max_age: float) -> List[dict]:
        now = self.clock()
        cached = self.boards.get(name)
        if cached is not None and 0 <= (now - cached[0]).total_seconds() < max_age:
            return cached[1]
        self._count(name)
        payload = self.kit[name].board(now)
        fetched = self.clock()
        events = normalise_kit_board(payload, provider=name, fetched_at=fetched, leagues=self.leagues,
                                     aliases=self.aliases)
        self.boards[name] = (fetched, events)
        return events

    def _ask_kit(self, name: str, request: ProviderRequest) -> Any:
        max_age = float(self.config['board_ttl_seconds'] if request.max_age_seconds is None
                        else min(request.max_age_seconds, self.config['board_ttl_seconds']))
        events = self._board(name, max_age)
        league = [e for e in events if e['league_key'] == request.league_key]
        return self._answer(request, league, name)

    # --- identity: one schedule per run, whoever supplied it ---

    def _schedule_identity(self, request: ProviderRequest, event: Mapping) -> Optional[Dict[str, str]]:
        """The schedule's identity for a provider event: same league, kickoff within 5 minutes, same teams."""
        known = self.identities.get((request.league_key, event['provider_event_id']))
        if known is not None:
            return known
        candidates = list(self.schedule.get(request.league_key, []))
        if request.identity and request.event_id:
            candidates.append({'id': str(request.event_id), **{k: str(request.identity.get(k) or '')
                                                              for k in ('kickoff_utc', 'home_team', 'away_team')}})
        kick = parse_time(event['kickoff_utc'])
        for item in candidates:
            other = parse_time(item.get('kickoff_utc'))
            if (other is not None and kick is not None and abs((other - kick).total_seconds()) <= 300
                    and team_key(item.get('home_team')) == team_key(event['home_team'])
                    and team_key(item.get('away_team')) == team_key(event['away_team'])):
                return item
        return None

    def _remember_schedule(self, request: ProviderRequest, events: Sequence[Mapping]) -> None:
        listed = self.schedule.setdefault(request.league_key, [])
        for event in events:
            identity = self._schedule_identity(request, event)
            if identity is None:
                identity = {'id': event['provider_event_id'], 'kickoff_utc': event['kickoff_utc'],
                            'home_team': event['home_team'], 'away_team': event['away_team']}
                listed.append(identity)
            self.identities[(request.league_key, event['provider_event_id'])] = identity

    def _in_window(self, request: ProviderRequest, event: Mapping) -> bool:
        if not request.window:
            return True
        start, end, kick = parse_time(request.window[0]), parse_time(request.window[1]), parse_time(event['kickoff_utc'])
        return kick is not None and (start is None or kick >= start) and (end is None or kick <= end)

    def _answer(self, request: ProviderRequest, events: List[dict], provider: str) -> Any:
        """The Odds API v4 response to this request, built from normalised events of its league. Each event carries
        `odds_provider` (which provider supplied it): the parsers ignore it, a saved payload keeps it."""
        if request.kind == 'events':
            events = [e for e in events if self._in_window(request, e)]
            self._remember_schedule(request, events)
            out = []
            for event in sorted(events, key=lambda e: (e['kickoff_utc'], e['home_team'])):
                identity = self.identities[(request.league_key, event['provider_event_id'])]
                out.append({'id': identity['id'], 'sport_key': request.sport_key,
                            'commence_time': event['kickoff_utc'],
                            'home_team': identity['home_team'], 'away_team': identity['away_team'],
                            'odds_provider': provider})
            return out
        if request.kind == 'odds':
            events = [e for e in events if self._in_window(request, e)]
            out = []
            for event in sorted(events, key=lambda e: (e['kickoff_utc'], e['home_team'])):
                identity = self._schedule_identity(request, event) or {}
                payload = to_odds_api_event(event, request.markets, event_id=identity.get('id'),
                                            home=identity.get('home_team'), away=identity.get('away_team'))
                payload['sport_key'] = request.sport_key
                payload['odds_provider'] = provider
                out.append(payload)
            return out
        # event_odds: the requested event by id, else by the schedule's or the caller's identity.
        target = str(request.event_id)
        match = None
        for event in events:
            identity = self._schedule_identity(request, event)
            if event['provider_event_id'] == target or (identity is not None and identity.get('id') == target):
                match = (event, identity)
                break
        if match is None:
            self.not_found += 1
            identity = dict(request.identity or {})
            return {'id': target, 'sport_key': request.sport_key, 'commence_time': identity.get('kickoff_utc'),
                    'home_team': identity.get('home_team'), 'away_team': identity.get('away_team'), 'bookmakers': [],
                    'odds_provider': provider}
        event, identity = match
        identity = identity or {}
        payload = to_odds_api_event(event, request.markets, event_id=target,
                                    home=identity.get('home_team'), away=identity.get('away_team'))
        payload['sport_key'] = request.sport_key
        payload['odds_provider'] = provider
        return payload

    def _from_odds_api(self, request: ProviderRequest, odds_api: Callable[[Optional[str]], Any],
                       odds_api_events: Optional[Callable[[], Any]] = None) -> Any:
        """The Odds API's answer, normalised to Pinnacle-only and aligned to the schedule like any other."""
        target = request.event_id
        if request.kind == 'event_odds' and target and not ODDS_API_EVENT_ID.fullmatch(str(target)):
            target = self._odds_api_id(request, odds_api_events)
            if target is None:
                self.not_found += 1
                identity = dict(request.identity or {})
                return {'id': str(request.event_id), 'sport_key': request.sport_key,
                        'commence_time': identity.get('kickoff_utc'), 'home_team': identity.get('home_team'),
                        'away_team': identity.get('away_team'), 'bookmakers': [], 'odds_provider': THE_ODDS_API}
        payload = odds_api(target if target != request.event_id else None)
        fetched = self.clock()
        if request.kind == 'events':
            events = []
            for item in payload if isinstance(payload, list) else []:
                normalised = normalise_odds_api_event({**item, 'bookmakers': []}, league_key=request.league_key,
                                                      fetched_at=fetched, aliases=self.aliases)
                if normalised is not None:
                    events.append(normalised)
            self._learn_odds_api_ids(request, events)
            return self._answer(request, events, THE_ODDS_API)
        items = payload if isinstance(payload, list) else [payload] if isinstance(payload, dict) else []
        events = [e for e in (normalise_odds_api_event(item, league_key=request.league_key, fetched_at=fetched,
                                                       aliases=self.aliases) for item in items) if e is not None]
        if request.kind == 'odds':
            self._learn_odds_api_ids(request, events)
        if request.kind == 'event_odds':
            for event in events:
                event['provider_event_id'] = str(request.event_id)
        return self._answer(request, events, THE_ODDS_API)

    def _learn_odds_api_ids(self, request: ProviderRequest, events: Sequence[Mapping]) -> None:
        """Remember The Odds API's id for each schedule event it answered for, for later per-event fallbacks."""
        for event in events:
            identity = self._schedule_identity(request, event)
            if identity is not None:
                self.odds_api_ids[(request.league_key, str(identity['id']))] = event['provider_event_id']

    def _odds_api_id(self, request: ProviderRequest,
                     odds_api_events: Optional[Callable[[], Any]]) -> Optional[str]:
        """The Odds API's own id for an event known by another provider's id: learnt from an earlier Odds API
        answer this run, else found in its events list (which costs no credits)."""
        known = self.odds_api_ids.get((request.league_key, str(request.event_id)))
        if known is not None:
            return known
        identity = request.identity or next(
            (v for (league, pid), v in self.identities.items()
             if league == request.league_key and v.get('id') == str(request.event_id)), None)
        if not identity:
            return None
        listed = odds_api_events() if odds_api_events is not None else []
        kick = parse_time(identity.get('kickoff_utc'))
        for item in listed if isinstance(listed, list) else []:
            other = parse_time(item.get('commence_time'))
            if (other is not None and kick is not None and abs((other - kick).total_seconds()) <= 300
                    and team_key(canonical_name(item.get('home_team'), request.league_key, self.aliases)[0])
                    == team_key(identity.get('home_team'))
                    and team_key(canonical_name(item.get('away_team'), request.league_key, self.aliases)[0])
                    == team_key(identity.get('away_team'))):
                return str(item.get('id'))
        return None

    def fetch(self, request: ProviderRequest, odds_api: Callable[[Optional[str]], Any],
              odds_api_events: Optional[Callable[[], Any]] = None) -> Any:
        """The answer to one request from the first provider that can give it. `odds_api(event_id)` performs the
        original Odds API request (a non-None event_id replaces the request's own); `odds_api_events()` lists the
        league's Odds API events (no credits), used to find an event first scheduled by another provider."""
        reasons: List[Tuple[str, str]] = []
        for name in self.order:
            if name == THE_ODDS_API:
                self._count(name)
                try:
                    result = self._from_odds_api(request, odds_api, odds_api_events)
                except Exception:
                    self._fail(name, ERROR)
                    self._note(None, request, reasons + [(name, ERROR)])
                    raise
                self._served(name, request, reasons)
                return result
            why = self._available(name)
            if why is not None:
                self._fail(name, why)
                reasons.append((name, why))
                continue
            try:
                result = self._ask_kit(name, request)
            except ProviderFailure as failure:
                reason = failure.reason
                if failure.http_status == 429:
                    self._block(name, failure)
                self._fail(name, reason)
                reasons.append((name, reason))
                continue
            self._served(name, request, reasons)
            return result
        raise RuntimeError('unreachable: The Odds API is always the last provider')

    def _block(self, name: str, failure: ProviderFailure) -> None:
        """Honour a 429: no request to this provider until Retry-After has passed (UTC midnight for a daily cap)."""
        seconds = failure.retry_after_seconds if failure.retry_after_seconds is not None else 60.0
        until = self.clock() + timedelta(seconds=seconds)
        state = self.state[name]
        state.blocked_until = until if state.blocked_until is None else max(state.blocked_until, until)

    def _served(self, name: str, request: ProviderRequest, reasons: List[Tuple[str, str]]) -> None:
        served = self.state[name].served
        served[request.kind] = served.get(request.kind, 0) + 1
        self._note(name, request, reasons)

    def _note(self, name: Optional[str], request: ProviderRequest, reasons: List[Tuple[str, str]]) -> None:
        """A switch whenever the serving provider changes (None: every provider failed for a request)."""
        if name == self.current:
            return
        self.switches.append({'at_utc': iso(self.clock()), 'from': self.current, 'to': name,
                              'reasons': {n: r for n, r in reasons}, 'request': request.kind,
                              'league': request.league_key})
        self.current = name

    # --- what the run records ---

    def summary(self) -> dict:
        providers = {}
        for name in self.order:
            state = self.state[name]
            item = {'requests': sum(state.requests_by_day.values()), 'requests_by_utc_day': dict(state.requests_by_day),
                    'served': dict(sorted(state.served.items())), 'failures': dict(sorted(state.failures.items()))}
            if name != THE_ODDS_API:
                item['daily_allowance'] = self.config['providers'][name]['daily_allowance']
                item['requests_today'] = self._today(name).requests_today
                item['blocked_until_utc'] = iso(state.blocked_until)
            providers[name] = item
        return {'enabled': True, 'order': list(self.order), 'providers': providers, 'switches': list(self.switches),
                'events_not_found': self.not_found}


def summary_markdown(summary: Optional[Mapping]) -> str:
    """The run-summary block: requests, failures and every switch per provider."""
    if not summary:
        return ''
    lines = ['### Odds providers', '', f"Order: {' → '.join(summary.get('order') or [])}.", '',
             '| Provider | Requests | Served | Failures | Today / allowance | Blocked until (UTC) |',
             '|---|---:|---|---|---|---|']
    for name, item in (summary.get('providers') or {}).items():
        served = ', '.join(f'{k} {v}' for k, v in (item.get('served') or {}).items()) or '—'
        failures = ', '.join(f'{k} {v}' for k, v in (item.get('failures') or {}).items()) or '—'
        allowance = item.get('daily_allowance', '')
        today = '—' if name == THE_ODDS_API else f"{item.get('requests_today', 0)} / {allowance if allowance else 'no cap'}"
        lines.append(f"| {name} | {item.get('requests', 0)} | {served} | {failures} | {today} | "
                     f"{item.get('blocked_until_utc') or '—'} |")
    switches = summary.get('switches') or []
    lines += ['', f'Switches this run: {len(switches)}.']
    for switch in switches:
        why = ', '.join(f'{k}: {v}' for k, v in (switch.get('reasons') or {}).items()) or 'provider available again'
        lines.append(f"- {switch.get('at_utc')}: {switch.get('from')} → {switch.get('to') or 'none (all failed)'} "
                     f"({switch.get('request')} {switch.get('league')}; {why})")
    if summary.get('events_not_found'):
        lines.append(f"\nRequested events not on the serving provider's board: {summary['events_not_found']}.")
    return '\n'.join(lines) + '\n'


def router_for(odds_api_client, *, config_path: Path | str = CONFIG, repo: Path | str = '.') -> Optional[
        OddsProviderRouter]:
    """A router for this client when the switch is on (seeded from the committed usage log), else None."""
    if not enabled(config_path):
        return None
    from odds_api_usage import read_log
    router = OddsProviderRouter(load_config(config_path), seed=read_log(repo))
    odds_api_client.router = router
    return router


def event_request(api, league, source: Mapping[str, Any], markets: Iterable[str],
                  max_age_seconds: Optional[float] = None) -> Dict[str, Any]:
    """The provider_request argument for a per-event call from a saved forecast row (closing collector, shadow
    corner list): nothing when the client has no router, i.e. the switch is off."""
    if active_router(api) is None:
        return {}
    identity = {k: source.get(k) for k in ('kickoff_utc', 'home_team', 'away_team')}
    return {'provider_request': ProviderRequest('event_odds', league.key, league.odds_api_sport_key,
                                                markets=tuple(sorted(markets)),
                                                event_id=str(source.get('odds_event_id', '')),
                                                identity=identity, max_age_seconds=max_age_seconds)}


def active_router(client) -> Optional[OddsProviderRouter]:
    """The client's router when the switch is on, else None (a test double's auto-attribute is never a router)."""
    router = getattr(client, 'router', None)
    return router if isinstance(router, OddsProviderRouter) else None


def iso_week(stamp: Any) -> Optional[str]:
    when = parse_time(stamp)
    if when is None:
        return None
    year, week, _ = when.isocalendar()
    return f'{year}-W{week:02d}'


def weekly_lines(records: Iterable[Mapping], week: str) -> List[str]:
    """The weekly report's provider section for one ISO week (UTC) of usage-log records: requests, served
    requests and switches per provider, and the Odds API credits spent. Empty when no record that week carries
    provider figures, i.e. the switch was off, so the report is then unchanged."""
    records = [r for r in records if isinstance(r, Mapping) and iso_week(r.get('recorded_at_utc')) == week]
    routed = [r for r in records if isinstance(r.get('odds_provider'), Mapping)]
    if not routed:
        return []
    totals: Dict[str, Dict[str, int]] = {}
    switches: List[Mapping] = []
    for record in routed:
        block = record['odds_provider']
        for name, item in (block.get('providers') or {}).items():
            row = totals.setdefault(name, {'requests': 0, 'served': 0, 'failed': 0, 'switched_to': 0})
            row['requests'] += int(item.get('requests') or 0)
            row['served'] += sum(int(v or 0) for v in (item.get('served') or {}).values())
            row['failed'] += sum(int(v or 0) for v in (item.get('failures') or {}).values())
        switches += [s for s in block.get('switches') or [] if isinstance(s, Mapping)]
    for item in switches:
        if item.get('to') in totals:
            totals[item['to']]['switched_to'] += 1
    credits = sum(int(r.get('credits_spent') or 0) for r in records)
    lines = ['## Odds providers', '',
             f'From the usage log ({len(routed)} runs with the provider switch on this week, UTC).', '',
             '| Provider | Requests | Served | Failed or skipped | Switches to it |', '|---|---:|---:|---:|---:|']
    for name, row in totals.items():
        lines.append(f"| {name} | {row['requests']} | {row['served']} | {row['failed']} | {row['switched_to']} |")
    lines += ['', f'Switches this week: {len(switches)}. Odds API credits spent this week (every workflow): '
                  f'{credits}.', '']
    return lines


# --- the cross-provider check ------------------------------------------------------------------------------------

def _prices(event: Mapping) -> Dict[str, float]:
    """Every Pinnacle price in a normalised event, keyed by market/line/side."""
    out: Dict[str, float] = {}
    one = event.get('one_x_two') or {}
    for side in ('home', 'draw', 'away'):
        if one.get(side) is not None:
            out[f'1X2 {side}'] = one[side]
    for item in event.get('asian_handicap') or []:
        out[f"AH {item['line']:+g} home"] = item['home']
        out[f"AH {item['line']:+g} away"] = item['away']
    for item in event.get('goal_lines') or []:
        out[f"Goals {item['line']:g} over"] = item['over']
        out[f"Goals {item['line']:g} under"] = item['under']
    for side, lines in (event.get('team_totals') or {}).items():
        for item in lines:
            out[f"Team total {side} {item['line']:g} over"] = item['over']
            out[f"Team total {side} {item['line']:g} under"] = item['under']
    for item in event.get('corners') or []:
        out[f"Corners {item['line']:g} over"] = item['over']
        out[f"Corners {item['line']:g} under"] = item['under']
    return out


def compare_providers(events_by_provider: Mapping[str, Sequence[Mapping]], tolerance: float) -> dict:
    """Match fixtures across providers (league, kickoff in the same 5-minute slot, canonical teams) and compare
    every price all of them quote. A difference is |a - b| / min(a, b); above `tolerance` it is outside."""
    names = list(events_by_provider)
    groups: Dict[Tuple[str, str, str], Dict[str, Mapping]] = {}
    for name in names:
        for event in events_by_provider[name]:
            kick = parse_time(event.get('kickoff_utc'))
            if kick is None:
                continue
            slot = kick.replace(minute=(kick.minute // 5) * 5, second=0, microsecond=0)
            key = (event['league_key'], iso(slot), f"{team_key(event['home_team'])} v {team_key(event['away_team'])}")
            groups.setdefault(key, {})[name] = event
    fixtures, differences, outside = [], [], []
    unmatched: Dict[str, List[str]] = {}
    for key, by_provider in sorted(groups.items()):
        if set(by_provider) != set(names):
            for name, event in by_provider.items():
                unmatched.setdefault(name, []).append(
                    f"{event['league_key']} {event['kickoff_utc']} {event['provider_home_team']} v "
                    f"{event['provider_away_team']}")
            continue
        prices = {name: _prices(event) for name, event in by_provider.items()}
        shared = sorted(set.intersection(*(set(p) for p in prices.values())))
        worst = 0.0
        for label in shared:
            values = {name: prices[name][label] for name in names}
            low, high = min(values.values()), max(values.values())
            gap = (high - low) / low
            worst = max(worst, gap)
            if gap > 0:
                row = {'league': key[0], 'kickoff_utc': key[1], 'match': key[2], 'price': label,
                       **{name: values[name] for name in names}, 'relative_difference': round(gap, 6),
                       'within_tolerance': gap <= tolerance}
                differences.append(row)
                if gap > tolerance:
                    outside.append(row)
        only = {name: len(set(prices[name]) - set(shared)) for name in names}
        fixtures.append({'league': key[0], 'kickoff_utc': key[1], 'match': key[2], 'shared_prices': len(shared),
                         'largest_relative_difference': round(worst, 6),
                         'prices_only_at': {k: v for k, v in only.items() if v}})
    return {'providers': names, 'tolerance': tolerance, 'fixtures_quoted_by_all': len(fixtures),
            'prices_compared': sum(f['shared_prices'] for f in fixtures), 'differences': differences,
            'outside_tolerance': outside, 'fixtures': fixtures,
            'not_quoted_by_all': {k: sorted(v) for k, v in unmatched.items()}}


def comparison_markdown(result: Mapping) -> str:
    names = list(result['providers'])
    lines = ['# Odds provider price check', '',
             f"Providers: {', '.join(names)}. Tolerance: {result['tolerance']:.1%} of the lower price.", '',
             f"Fixtures quoted by every provider: {result['fixtures_quoted_by_all']}; prices compared: "
             f"{result['prices_compared']}; differences: {len(result['differences'])}; outside tolerance: "
             f"{len(result['outside_tolerance'])}.", '']
    if result['differences']:
        lines += ['| League | Kickoff | Match | Price | ' + ' | '.join(names) + ' | Difference | Within |',
                  '|---|---|---|---|' + '---:|' * len(names) + '---:|---|']
        for row in result['differences']:
            lines.append(f"| {row['league']} | {row['kickoff_utc']} | {row['match']} | {row['price']} | "
                         + ' | '.join(f"{row[n]:.3f}" for n in names)
                         + f" | {row['relative_difference']:.2%} | {'yes' if row['within_tolerance'] else 'NO'} |")
        lines.append('')
    for name, items in (result.get('not_quoted_by_all') or {}).items():
        lines += [f'Fixtures from {name} not matched at every provider ({len(items)}; a team-name alias or a '
                  'league name may be missing):', *[f'- {x}' for x in items], '']
    return '\n'.join(lines)
