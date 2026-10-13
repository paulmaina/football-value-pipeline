"""Refresh current-season UCL results separately from prediction generation."""
import argparse
from datetime import datetime, timezone
import os
from pathlib import Path
import tempfile
from api_key_config import load_api_keys
from refresh_training_data import git
from ucl_training import fetch_payload, apply_payload, STATUS


def publish(repo, payload, year, clock, attempts=3):
    repo = repo.resolve()
    with tempfile.TemporaryDirectory(prefix='ucl-publish-') as temporary:
        for attempt in range(attempts):
            git(repo, 'fetch', 'origin', 'main')
            base = git(repo, 'rev-parse', 'FETCH_HEAD').stdout.strip()
            work = Path(temporary)/str(attempt)
            git(repo, 'worktree', 'add', '--detach', str(work), base)
            try:
                status = apply_payload(work, payload, year, clock)
                git(work, 'add', '--', str(STATUS), f'.football_cache/fdorg_history_UCL_{year}.json',
                    f'.football_cache/fdorg_history_UCL_{year}.meta.json')
                git(work, '-c', 'user.name=github-actions[bot]', '-c',
                    'user.email=41898282+github-actions[bot]@users.noreply.github.com',
                    'commit', '-m', 'Refresh validated UCL training results')
                result = git(work, 'push', 'origin', 'HEAD:refs/heads/main', check=False)
                if result.returncode == 0:
                    return status
                git(repo, 'fetch', 'origin', 'main')
                if git(repo, 'rev-parse', 'FETCH_HEAD').stdout.strip() == base:
                    raise RuntimeError('UCL training publish failed')
            finally:
                git(repo, 'worktree', 'remove', '--force', str(work))
    raise RuntimeError('Main kept advancing; no UCL update published')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', type=Path, default=Path(__file__).resolve().parent)
    parser.add_argument('--api-key-source', choices=('dotenv', 'environment'), default='dotenv')
    parser.add_argument('--publish', action='store_true')
    args = parser.parse_args()
    load_api_keys(args.api_key_source)
    clock = datetime.now(timezone.utc); year = clock.year if clock.month >= 7 else clock.year-1
    payload = fetch_payload(os.getenv('FOOTBALL_DATA_API_KEY', ''), year)
    status = publish(args.repo, payload, year, clock) if args.publish else apply_payload(args.repo, payload, year, clock)
    print(f"UCL: {status['completed_matches']} completed; latest {status['latest_completed_date']}; "
          f"added {status['added_matches']}; {status['coverage_status']}")


if __name__ == '__main__':
    main()
