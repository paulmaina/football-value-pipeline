"""Lightweight price check: refresh odds and re-run v27 selection, no model refit.

Re-requests only the main odds market set (h2h, spreads, totals) for leagues
that have a stored fixture inside the 48-hour window, merges the fresh quotes
into the current forecast rows, and re-ranks with the production policy. The
forecast probabilities, model fits and per-event extra markets are untouched.

OFF BY DEFAULT. The Price checks workflow runs it only when the repository
variable PRICE_CHECKS_ENABLED is 'true', every PRICE_CHECK_INTERVAL_HOURS
(3, 4 or 6). `--estimate` prints the expected monthly Odds API credits for
each interval without any request.
"""
from __future__ import annotations

import argparse
import json
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Dict, Iterable, Optional

import numpy as np
import pandas as pd

MAIN_MARKETS = ('h2h', 'totals', 'spreads')
INTERVALS = (3, 4, 6)
WINDOW_HOURS = 48
LOOKAHEAD_DAYS = 3


def due(clock: datetime, interval: int) -> bool:
    """Run on UTC hours divisible by the interval (the workflow fires hourly)."""
    if interval not in INTERVALS:
        raise ValueError(f'Interval must be one of {INTERVALS} hours')
    return clock.hour % interval == 0


def leagues_in_window(predictions: pd.DataFrame, clock: datetime) -> list:
    """Registry keys with a stored fixture kicking off within the next 48 hours."""
    from football_value_pipeline_v2_standalone import LEAGUES
    if predictions.empty:
        return []
    kick = pd.to_datetime(predictions['kickoff_utc'], utc=True, errors='coerce')
    now = pd.Timestamp(clock)
    upcoming = predictions.loc[(kick > now) & (kick <= now + pd.Timedelta(hours=WINDOW_HOURS)), 'league']
    names = set(upcoming.dropna())
    return sorted(key for key, league in LEAGUES.items() if league.name in names or key in names)


MAX_KICKOFF_SKEW_SECONDS = 300  # Same tolerance as the full pipeline's odds join.


def same_fixture(row, event) -> bool:
    """An event ID alone is not a safe join: teams and kickoff must still match the forecast."""
    from football_value_pipeline_v2_standalone import canonical_team_key
    if any(canonical_team_key(str(row.get(side) or '')) != canonical_team_key(str(event.get(provider) or ''))
           for side, provider in (('home_team', '_odds_home_team'), ('away_team', '_odds_away_team'))):
        return False
    kick = pd.to_datetime(row.get('kickoff_utc'), utc=True, errors='coerce')
    quoted = pd.to_datetime(event.get('_odds_commence_time'), utc=True, errors='coerce')
    return not (pd.isna(kick) or pd.isna(quoted)) and abs((quoted - kick).total_seconds()) <= MAX_KICKOFF_SKEW_SECONDS


def merge_odds(predictions: pd.DataFrame, odds: pd.DataFrame) -> pd.DataFrame:
    """Merge fresh main-market quotes into rows by provider event id; newest quote wins.

    A refreshed event whose teams or kickoff no longer match the stored forecast
    (renamed, rescheduled or reused ID) is skipped, keeping the stored quotes.
    """
    from price_edge_shortlist import merge_quotes
    result = predictions.copy()
    if odds.empty:
        return result
    for column in ('asian_handicap_offers', 'price_edge_quotes'):
        if column not in result:
            result[column] = '[]'
        result[column] = result[column].astype(object)
    fresh = {str(r['fixture_id']): r for r in odds.to_dict('records')}
    for idx, row in result.iterrows():
        event = fresh.get(str(row.get('odds_event_id') or ''))
        if event is None or not same_fixture(row, event):
            continue
        old = json.loads(row.get('asian_handicap_offers') or '[]') if isinstance(row.get('asian_handicap_offers'), str) else []
        new = json.loads(event.get('asian_handicap_offers') or '[]')
        unique = {(x['side'], x['line'], x['bookmaker']): x
                  for x in sorted(old + new, key=lambda x: (str(x['last_update_utc']), x['price']))}
        result.at[idx, 'asian_handicap_offers'] = json.dumps(list(unique.values()), sort_keys=True)
        result.at[idx, 'price_edge_quotes'] = merge_quotes(row.get('price_edge_quotes'), event.get('price_edge_quotes'))
    return result


def check(root: Path, api, clock: Optional[datetime] = None) -> Dict[str, object]:
    """Fetch main odds for in-window leagues, merge, re-rank and publish a new run bundle."""
    from football_value_pipeline_v2_standalone import LEAGUES
    from prediction_runs import stage_run, publish_run, resolve_raw
    from pipeline_health import write_generation_metadata
    from workflow_checks import raw_check
    from refresh_conservative_shortlist import _refresh
    from format_football_output import publish_shortlists
    root = Path(root)
    clock = clock or datetime.now(timezone.utc)
    current = pd.read_csv(resolve_raw(root / 'raw') / 'all_leagues_predictions.csv', low_memory=False)
    leagues = leagues_in_window(current, clock)
    if not leagues:
        return {'status': 'NO_FIXTURES_IN_WINDOW', 'requests': 0, 'credits': 0}
    with stage_run(root / 'raw', seed=True) as staging:
        path = staging / 'all_leagues_predictions.csv'
        predictions = pd.read_csv(path, low_memory=False)
        for key in leagues:
            predictions = merge_odds(predictions, api.odds(LEAGUES[key], LOOKAHEAD_DAYS, clock))
        predictions.to_csv(path, index=False)
        summary = _refresh(root, clock, raw_dir=staging)
        summary['refresh_source'] = 'Price check: main odds refreshed (h2h, spreads, totals); no model refit'
        (staging / 'conservative_bet_summary.json').write_text(json.dumps(summary, indent=2), encoding='utf-8')
        write_generation_metadata(staging, summary)
        raw_check(staging.parent)
        bundle = publish_run(staging, root / 'raw')
    (root / 'readable').mkdir(parents=True, exist_ok=True)
    publish_shortlists(bundle, root / 'readable')
    return {'status': 'CHECKED', 'leagues': leagues, 'requests': len(leagues),
            'credits': len(leagues) * len(MAIN_MARKETS), 'picks': summary['n_shortlisted']}


def monthly_credits(match_days: Iterable, interval: int, regions: int = 1) -> float:
    """Expected credits per 30 days for one league: 3 credits per check with a fixture in the next 48 hours."""
    kicks = np.sort(pd.to_datetime(list(match_days), utc=True).as_unit('ns').asi8)
    if not len(kicks):
        return 0.0
    start = pd.Timestamp(kicks[0], tz='UTC').normalize() - pd.Timedelta(hours=WINDOW_HOURS)
    end = pd.Timestamp(kicks[-1], tz='UTC').normalize()
    checks = pd.date_range(start, end, freq=f'{interval}h').as_unit('ns').asi8
    following = np.searchsorted(kicks, checks, side='right')
    window = int(WINDOW_HOURS * 3600 * 1e9)
    active = (following < len(kicks)) & (kicks[np.minimum(following, len(kicks) - 1)] <= checks + window)
    span = max((end - start).days, 1)
    return int(active.sum()) * len(MAIN_MARKETS) * regions * 30 / span


def estimate(cache_dir: Path = Path('.football_cache'), seasons=('2425',)) -> Dict[str, object]:
    """Monthly credits for N = 3, 4, 6 hours from a full season of real kickoff dates.

    Per league, a check costs 3 credits (h2h, spreads, totals; one region)
    when that league has a fixture within 48 hours. The 8 football-data
    leagues use their real dates; UCL and UEL are approximated by the
    Tuesday-Thursday rounds of the same months (no fixture file is cached).
    """
    from ah_close_backtest import DIVISIONS
    per_league = {}
    for division in DIVISIONS:
        dates = []
        for season in seasons:
            path = Path(cache_dir) / f'{season}_{division}.csv'
            if path.exists():
                frame = pd.read_csv(path, encoding='latin1', usecols=['Date'])
                dates += list(pd.to_datetime(frame['Date'], dayfirst=True, errors='coerce').dropna() + pd.Timedelta(hours=15))
        per_league[division] = dates
    domestic = [d for v in per_league.values() for d in v]
    if domestic:
        months = pd.date_range(min(domestic).normalize(), max(domestic).normalize(), freq='D', tz=None)
        europe = [d + pd.Timedelta(hours=20) for d in months if d.weekday() in (1, 2) and d.month in (9, 10, 11, 12, 1, 2, 3, 4, 5)]
        per_league['UCL'] = europe
        per_league['UEL'] = [d + pd.Timedelta(days=1) for d in europe]
    return {f'{n}h': round(sum(monthly_credits(dates, n) for dates in per_league.values() if dates)) for n in INTERVALS}


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('--root', type=Path, default=Path('football_output_v2'))
    parser.add_argument('--interval-hours', type=int, default=None)
    parser.add_argument('--estimate', action='store_true', help='print monthly credit estimates and exit')
    parser.add_argument('--api-key-source', choices=('dotenv', 'environment'), default='dotenv')
    args = parser.parse_args(argv)
    if args.estimate:
        print(json.dumps({'monthly_credits_main_request_only': estimate()}, indent=2))
        return 0
    clock = datetime.now(timezone.utc)
    if args.interval_hours is not None and not due(clock, args.interval_hours):
        print(f'Not due at {clock:%H}:00 UTC for a {args.interval_hours}-hour interval.')
        return 0
    import os
    from football_value_pipeline_v2_standalone import TheOddsAPI
    from api_key_config import load_api_keys
    load_api_keys(args.api_key_source)
    key = next((v for name in TheOddsAPI.KEY_ENV_NAMES if (v := os.getenv(name, '').strip())), None)
    if key is None:
        print('No Odds API key configured; price check skipped.')
        return 0
    # Odds responses go to a throwaway cache: the tracked .football_cache must
    # stay untouched so the workflow can rebase and publish cleanly.
    import tempfile
    with tempfile.TemporaryDirectory(prefix='price-check-cache-') as cache:
        api = TheOddsAPI(key, cache_dir=cache)
        print(json.dumps(check(args.root, api, clock), indent=2))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
