"""Collect Big Balls Free data and produce integrated, provenance-preserving history."""
from __future__ import annotations

import argparse
import json
import os
from datetime import datetime, timezone
from pathlib import Path

from api_key_config import load_api_keys
from bbs_data import Client, FetchError, LEAGUES, Store, collect
from bbs_integration import build_dataset, read_existing, write_dataset


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--api-key-source', choices=['dotenv', 'environment'], default='dotenv')
    parser.add_argument('--leagues', nargs='+', choices=list(LEAGUES), default=list(LEAGUES))
    parser.add_argument('--seasons', nargs='+', type=int, help='Explicit season start years; default current season')
    parser.add_argument('--daily-budget', type=int, help='Optional local ceiling; default uses provider allowance')
    parser.add_argument('--max-requests', type=int, help='Optional local ceiling; default has no per-run cap')
    parser.add_argument('--stats-limit', type=int, help='Optional statistics cap; default processes all due candidates')
    parser.add_argument('--store', type=Path, default=Path('.football_cache/bbs/state'))
    parser.add_argument('--existing-cache', type=Path, default=Path('.football_cache'))
    parser.add_argument('--output', type=Path, default=Path('.football_cache/bbs/combined'))
    parser.add_argument('--team-map', type=Path, default=Path('.football_cache/bbs/team_map.json'))
    parser.add_argument('--offline', action='store_true', help='Rebuild from stored observations without network')
    parser.add_argument('--as-of', help='BBS observation cutoff; offline only, does not rewind existing source caches')
    args = parser.parse_args(argv)
    if args.as_of and not args.offline:
        parser.error('--as-of requires --offline')
    if args.stats_limit is not None and args.stats_limit < 0:
        parser.error('--stats-limit cannot be negative')
    now = datetime.now(timezone.utc)
    current = now.year if now.month >= 7 else now.year - 1
    seasons = args.seasons or [current]
    if any(s < 2000 or s > now.year for s in seasons):
        parser.error('Season outside supported year range')
    args.store.parent.mkdir(parents=True, exist_ok=True)
    lock = args.store.with_suffix('.lock')
    try:
        handle = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
    except FileExistsError:
        print('Collection lock exists; check for an active collector before removing ' + str(lock))
        return 2
    os.close(handle)
    store = None
    try:
        store = Store(args.store)
        # No misleading successful empty export if existing history is absent.
        baseline = read_existing(args.existing_cache)
        if not baseline:
            raise ValueError('No existing training caches found; refresh training data first')
        explicit = json.loads(args.team_map.read_text(encoding='utf-8')) if args.team_map.exists() else {}
        if not isinstance(explicit, dict):
            raise ValueError('Team map must be an object keyed by league')
        report = {'status': 'offline'}
        if not args.offline:
            load_api_keys(args.api_key_source)
            client = Client(store, os.getenv('BBS_API_KEY', ''), args.daily_budget, args.max_requests)
            report = collect(client, args.leagues, seasons, args.stats_limit)
        cutoff = args.as_of or datetime.now(timezone.utc).isoformat()
        dataset = build_dataset(store, baseline, cutoff, explicit)
        dataset['report']['collection'] = report
        generation = write_dataset(dataset, args.output)
        print(json.dumps({'output': str(generation), 'rows': dataset['report']['rows'],
                          'join_counts': dataset['report']['join_counts'], 'collection': report}, indent=2))
        return 1 if report['status'] == 'partial' or dataset['report']['data_quality_status'] == 'partial' else 0
    except (FetchError, ValueError, KeyError, TypeError, OSError) as exc:
        print(str(exc))
        return 2
    finally:
        if store is not None:
            store.close()
        lock.unlink(missing_ok=True)


if __name__ == '__main__':
    raise SystemExit(main())
