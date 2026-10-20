"""Collect supplementary API-Football fixture/results and optional statistics."""
import argparse
from datetime import datetime, timezone
import json
import os
from pathlib import Path

from api_key_config import load_api_keys
from api_football_data import Client, LEAGUES, Store, collect, atomic_json
from bbs_data import FetchError
from prediction_runs import release_lock


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--api-key-source', choices=('dotenv', 'environment'), default='dotenv')
    parser.add_argument('--cache', type=Path, default=Path('.football_cache'))
    parser.add_argument('--leagues', nargs='+', choices=list(LEAGUES), default=list(LEAGUES))
    parser.add_argument('--seasons', nargs='+', type=int)
    parser.add_argument('--daily-budget', type=int, default=80)
    parser.add_argument('--max-requests', type=int, default=20)
    parser.add_argument('--stats-limit', type=int, default=10)
    args = parser.parse_args(argv)
    now = datetime.now(timezone.utc)
    seasons = args.seasons or [now.year if now.month >= 7 else now.year-1]
    if any(not 2000 <= year <= now.year for year in seasons) or args.stats_limit < 0:
        parser.error('Invalid season or statistics limit')
    root = args.cache/'api_football'; root.mkdir(parents=True, exist_ok=True)
    lock = root/'.collect.lock'
    try:
        lock.mkdir()
    except FileExistsError:
        print('API-Football collector already active; verify it stopped before removing '+str(lock))
        return 2
    try:
        load_api_keys(args.api_key_source)
        client = Client(Store(root/'state'), os.getenv('API_FOOTBALL_KEY', ''),
                        args.daily_budget, args.max_requests)
        report = collect(client, args.leagues, seasons, args.stats_limit)
        report.update(collected_at_utc=datetime.now(timezone.utc).isoformat(),
                      daily_budget=args.daily_budget, max_requests=args.max_requests,
                      role='supplementary', current_season_access='CHECK_QUERY_STATUSES')
        atomic_json(root/'collection_status.json', report)
        print(json.dumps(report, indent=2))
        return 1 if report['status'] == 'partial' else 0
    except (FetchError, ValueError, OSError, KeyError, TypeError):
        print('API-Football collection failed; existing sources retained. Check credentials, state and account access.')
        return 2
    finally:
        release_lock(lock)


if __name__ == '__main__':
    raise SystemExit(main())
