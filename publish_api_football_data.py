"""Publish supplementary observations without overwriting another collector's quota."""
import argparse
from pathlib import Path
import shutil
import tempfile

from bbs_data import decode
from publish_performance import git, merge_snapshots

CACHE = Path('.football_cache/api_football')
CHECKPOINT = CACHE/'state/checkpoint.json'


def checkpoint(repo, ref):
    result = git(repo, 'show', f'{ref}:{CHECKPOINT.as_posix()}', check=False)
    return result.stdout if result.returncode == 0 else None


def publish(repo, remote='origin', branch='main', attempts=3):
    from api_football_data import observations
    repo = Path(repo).resolve(); source = repo/CACHE
    status = decode((source/'collection_status.json').read_text(encoding='utf-8'))
    for kind in ('match', 'statistics', 'quarantine', 'schedule'):
        observations(repo/'.football_cache', kind, status['collected_at_utc'])
    expected = checkpoint(repo, 'HEAD')
    with tempfile.TemporaryDirectory(prefix='api-football-publish-') as temporary:
        for attempt in range(attempts):
            git(repo, 'fetch', remote, branch)
            base = git(repo, 'rev-parse', 'FETCH_HEAD').stdout.strip()
            if checkpoint(repo, base) != expected:
                raise RuntimeError('API-Football quota checkpoint advanced; reconcile before publishing')
            work = Path(temporary)/str(attempt)
            git(repo, 'worktree', 'add', '--detach', str(work), base)
            try:
                target = work/CACHE
                merge_snapshots(source/'state/observations', target/'state/observations')
                for file in (source/'state/responses').glob('*.json'):
                    if file.is_symlink():
                        raise ValueError('Symlink in API-Football response state')
                    dest = target/'state/responses'/file.name
                    dest.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copyfile(file, dest)
                (target/'state').mkdir(parents=True, exist_ok=True)
                shutil.copyfile(source/'state/checkpoint.json', target/'state/checkpoint.json')
                shutil.copyfile(source/'collection_status.json', target/'collection_status.json')
                git(work, 'add', '--', str(CACHE))
                if git(work, 'diff', '--cached', '--quiet', check=False).returncode == 0:
                    return
                git(work, '-c', 'user.name=github-actions[bot]', '-c',
                    'user.email=41898282+github-actions[bot]@users.noreply.github.com',
                    'commit', '-m', 'Collect supplementary API-Football observations [skip ci]')
                pushed = git(work, 'push', remote, f'HEAD:refs/heads/{branch}', check=False)
                if pushed.returncode == 0:
                    return
                git(repo, 'fetch', remote, branch)
                if git(repo, 'rev-parse', 'FETCH_HEAD').stdout.strip() == base:
                    raise RuntimeError('API-Football publication failed')
            finally:
                git(repo, 'worktree', 'remove', '--force', str(work))
    raise RuntimeError('Main kept advancing; API-Football publication stopped')


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', type=Path, default=Path(__file__).resolve().parent)
    args = parser.parse_args(argv)
    publish(args.repo)


if __name__ == '__main__':
    main()
