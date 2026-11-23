"""Cross-provider price check for the odds-provider adapter (docs/odds-providers.md).

Fetches one board from each configured kit provider (pinnapi, pinnodds) and, with --odds-api, The Odds API's
Pinnacle 1X2, totals and spreads for the same leagues (3 credits per league), normalises all of them and
compares every Pinnacle price each provider quotes for the same fixture. Prices are fetched seconds apart, so a
line that moved in between shows as a difference; the report lists every difference and marks those above the
configured tolerance. It also lists fixtures not matched at every provider: candidates for
odds_provider_team_aliases.json or the league names in odds_provider_config.json.

Reads keys from the environment or .env (PINNAPI_API_KEY, PINNODDS_API_KEY, THE_ODDS_API_KEY...). Writes only
under --output. Never part of a forecast.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import odds_provider as op  # noqa: E402


def kit_events(config, leagues, aliases, errors):
    events = {}
    for name in config['order']:
        spec = config['providers'][name]
        if spec['api'] != op.KIT:
            continue
        try:
            payload = op.KitProvider(name, spec).board(datetime.now(timezone.utc))
        except op.ProviderFailure as failure:
            errors[name] = failure.reason + (f' ({failure.detail})' if failure.detail else '')
            continue
        events[name] = op.normalise_kit_board(payload, provider=name, fetched_at=datetime.now(timezone.utc),
                                              leagues=leagues, aliases=aliases)
    return events


def odds_api_events(leagues, aliases, errors):
    from football_value_pipeline_v2_standalone import LEAGUES, THE_ODDS_API_BASE, TheOddsAPI
    key = next((os.getenv(k, '').strip() for k in TheOddsAPI.KEY_ENV_NAMES if os.getenv(k, '').strip()), '')
    if not key:
        errors[op.THE_ODDS_API] = 'not_configured'
        return None
    client = TheOddsAPI(key, force_refresh=True)
    client.router = None  # the raw Odds API, never routed
    start, end = client._window(datetime.now(timezone.utc), 3)
    items = []
    for league_key in leagues:
        league = LEAGUES[league_key]
        payload = client._get_json(
            f'{THE_ODDS_API_BASE}/sports/{league.odds_api_sport_key}/odds', f'odds_provider_compare_{league_key}.json',
            ttl=timedelta(seconds=0), force_refresh=True, allow_stale=False,
            params={'bookmakers': 'pinnacle', 'markets': 'h2h,totals,spreads', 'oddsFormat': 'decimal',
                    'dateFormat': 'iso', 'commenceTimeFrom': start, 'commenceTimeTo': end})
        fetched = datetime.now(timezone.utc)
        items += [e for e in (op.normalise_odds_api_event(x, league_key=league_key, fetched_at=fetched,
                                                           aliases=aliases) for x in payload or []) if e is not None]
    return items


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--leagues', nargs='*', default=None, help='league keys (default: every configured league)')
    parser.add_argument('--odds-api', action='store_true', help='include The Odds API (spends credits)')
    parser.add_argument('--api-key-source', choices=('dotenv', 'environment'), default='dotenv')
    args = parser.parse_args(argv)
    from api_key_config import load_api_keys
    load_api_keys(args.api_key_source)
    config = op.load_config()
    leagues = {k: v for k, v in config['leagues'].items() if not args.leagues or k in args.leagues}
    aliases = op.load_aliases()
    errors = {}
    events = kit_events(config, leagues, aliases, errors)
    if args.odds_api:
        items = odds_api_events(leagues, aliases, errors)
        if items is not None:
            events[op.THE_ODDS_API] = items
    result = op.compare_providers(events, float(config['price_tolerance']['decimal_odds_relative']))
    result['errors'] = errors
    text = op.comparison_markdown(result) + ''.join(f'\nNot fetched: {k}: {v}.' for k, v in errors.items()) + '\n'
    args.output.mkdir(parents=True, exist_ok=True)
    (args.output / 'odds_provider_compare.json').write_text(json.dumps(result, indent=2, sort_keys=True),
                                                           encoding='utf-8')
    (args.output / 'odds_provider_compare.md').write_text(text, encoding='utf-8')
    print(text)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
