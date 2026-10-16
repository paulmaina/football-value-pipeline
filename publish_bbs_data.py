"""Publish only BBS cache files; rebuild combined CSVs on each latest-main retry."""
from __future__ import annotations

import shutil
import tempfile
from pathlib import Path

from bbs_data import Store, decode
from bbs_integration import build_dataset, read_existing, write_dataset
from publish_performance import git, merge_snapshots

CACHE = Path('.football_cache/bbs')
CHECKPOINT = CACHE / 'state/checkpoint.json'


def committed_checkpoint(repo, ref):
    result = git(repo, 'show', f'{ref}:{CHECKPOINT.as_posix()}', check=False)
    return result.stdout if result.returncode == 0 else None


def publish(repo, remote='origin', branch='main', attempts=3):
    repo = Path(repo).resolve()
    source = repo / CACHE
    manifest = decode((source/'combined/latest.json').read_text())
    cutoff = manifest['cutoff_utc']
    expected = committed_checkpoint(repo, 'HEAD')
    with tempfile.TemporaryDirectory(prefix='bbs-publish-') as temp:
        for attempt in range(attempts):
            git(repo, 'fetch', remote, branch)
            base = git(repo, 'rev-parse', 'FETCH_HEAD').stdout.strip()
            # Never overwrite another collector's budget or observation state.
            if committed_checkpoint(repo, base) != expected:
                raise RuntimeError('BBS checkpoint advanced remotely; reconcile before publishing')
            work = Path(temp)/str(attempt)
            git(repo, 'worktree', 'add', '--detach', str(work), base)
            try:
                target = work/CACHE
                merge_snapshots(source/'state/observations', target/'state/observations')
                merge_snapshots(source/'combined/snapshots', target/'combined/snapshots')
                for folder in ('state/responses',):
                    for file in (source/folder).glob('*.json'):
                        if file.is_symlink():
                            raise ValueError('Symlink not allowed in collection state')
                        destination = target/folder/file.name
                        destination.parent.mkdir(parents=True, exist_ok=True)
                        shutil.copyfile(file, destination)
                (target/'state').mkdir(parents=True, exist_ok=True)
                shutil.copyfile(source/'state/checkpoint.json', target/'state/checkpoint.json')
                # Use the latest reviewed mappings and primary cache, not a stale export.
                mapping = target/'team_map.json'
                explicit = decode(mapping.read_text()) if mapping.exists() else {}
                store = Store(target/'state')
                dataset = build_dataset(store, read_existing(work/'.football_cache'), cutoff, explicit)
                dataset['report']['collection'] = decode((source/'combined'/manifest['generation']/'report.json').read_text())['collection']
                write_dataset(dataset, target/'combined')
                git(work, 'add', '--', str(CACHE))
                if git(work, 'diff', '--cached', '--quiet', check=False).returncode == 0:
                    return
                git(work, '-c', 'user.name=github-actions[bot]', '-c',
                    'user.email=41898282+github-actions[bot]@users.noreply.github.com',
                    'commit', '-m', 'Refresh validated BBS training data [skip ci]')
                pushed = git(work, 'push', remote, f'HEAD:refs/heads/{branch}', check=False)
                if pushed.returncode == 0:
                    return
                git(repo, 'fetch', remote, branch)
                if git(repo, 'rev-parse', 'FETCH_HEAD').stdout.strip() == base:
                    raise RuntimeError('BBS publication failed: ' + pushed.stderr)
            finally:
                git(repo, 'worktree', 'remove', '--force', str(work))
    raise RuntimeError('Main kept advancing; BBS publication stopped without force-pushing')


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', type=Path, default=Path(__file__).resolve().parent)
    args = parser.parse_args()
    publish(args.repo)
