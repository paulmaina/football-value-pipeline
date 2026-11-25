"""Monthly repository hygiene report: tracked files and folders that may be retirement leftovers.

Report only: it never deletes, moves or edits anything. It lists

1. large tracked files and folders that have not changed for at least --stale-days (default 30) and
   that no live code, workflow or test refers to;
2. folders whose README.md or report.md says ARCHIVED.

"Refers to" means the file's repository path, its file name, or the path or name of a folder it sits
in appears as a token in a tracked Python file, workflow or test (or the JSON/YAML/TOML configuration
beside them). Data read through a glob pattern can therefore be listed although it is read;
a listed path is a question for review, never a verdict. A retirement removes its outputs and
references in the same PR (CLAUDE.md), so a clean report is the expected state.

    python scripts/repo_hygiene.py                      # markdown report on stdout
    python scripts/repo_hygiene.py --output report.md --json report.json
"""
from __future__ import annotations

import argparse
from collections import defaultdict
import json
from pathlib import Path, PurePosixPath
import re
import subprocess
import sys

REPO = Path(__file__).resolve().parents[1]
CODE_SUFFIXES = ('.py', '.yml', '.yaml', '.toml', '.cfg', '.ini', '.sh', '.ps1')
# Configuration that names data paths; scanned as code. Data folders' own JSON is not.
CONFIG_JSON = re.compile(r'^[^/]+\.json$|^narrow_margin_models/|^\.github/')
NOT_CODE = ('docs/', 'evaluation/', 'football_output_v2/', '.football_cache/', 'data/')
ARCHIVED = re.compile(r'\bARCHIVED\b')
TOKEN = re.compile(r'[A-Za-z0-9_./-]+')
# Names too generic to count as a reference by themselves.
GENERIC = {'README.md', 'report.md', 'summary.json', 'results.json', 'manifest.json', 'metadata.json',
           'raw', 'state', 'data', 'docs', 'tests', 'scripts', 'performance', 'snapshots', 'weekly'}


def git(*args):
    return subprocess.run(['git', '-C', str(REPO), *args], capture_output=True, text=True, check=True,
                          stdin=subprocess.DEVNULL, encoding='utf-8', errors='replace').stdout


def tracked():
    """Tracked paths with their sizes in the index (blob sizes, not the checkout's line endings)."""
    out = {}
    for line in git('ls-files', '-s', '-z').split('\0'):
        if line:
            meta, path = line.split('\t', 1)
            out[path] = meta.split()[1]
    sizes = {}
    shas = list(out.values())
    if shas:
        batch = subprocess.run(['git', '-C', str(REPO), 'cat-file', '--batch-check=%(objectname) %(objectsize)'],
                               input='\n'.join(shas), capture_output=True, text=True, check=True).stdout
        sizes = dict(line.split() for line in batch.splitlines() if line)
    return {path: int(sizes.get(sha, 0)) for path, sha in out.items()}


def changed_since(days):
    return {p for p in git('log', f'--since={days}.days', '--name-only', '--format=', '--no-renames').splitlines() if p}


def is_code(path):
    return (not path.startswith(NOT_CODE) and (path.endswith(CODE_SUFFIXES) or CONFIG_JSON.match(path) is not None))


def corpus(paths):
    """Every name and path-like token in tracked code, workflows and tests."""
    tokens = set()
    for path in paths:
        if is_code(path):
            try:
                text = (REPO/path).read_text(encoding='utf-8', errors='replace')
            except OSError:
                continue
            for token in TOKEN.findall(text):
                tokens.add(token)
                tokens.update(t for t in token.split('/') if t)
    return tokens


def referenced(path, tokens):
    """The file's path, its name, or a folder it sits in (path, name or data-root-relative path) appears."""
    p = PurePosixPath(path)
    parts = p.parts
    # A top-level folder (football_output_v2, .football_cache, docs) names a whole data root, not this file.
    folders = [parent for parent in p.parents if len(parent.parts) > 1]
    needles = ({path, p.name} | {str(f) for f in folders} | {f.name for f in folders}
               | {'/'.join(parts[i:]) for i in range(1, len(parts) - 1)})
    return any(n not in GENERIC and n in tokens for n in needles)


def archived_folders(paths):
    found = []
    for path in paths:
        if PurePosixPath(path).name in ('README.md', 'report.md') and not path.startswith('docs/'):
            try:
                head = (REPO/path).read_text(encoding='utf-8', errors='replace')[:400]
            except OSError:
                continue
            if ARCHIVED.search(head):
                found.append(str(PurePosixPath(path).parent))
    return sorted(set(found))


def report(min_file_mb=1.0, min_folder_mb=5.0, stale_days=30):
    sizes = tracked()
    recent = changed_since(stale_days)
    tokens = corpus(sizes)
    files = []
    folders = defaultdict(lambda: {'bytes': 0, 'files': 0, 'recent': False, 'referenced': False})
    for path, size in sizes.items():
        if is_code(path):
            continue
        stale = path not in recent
        used = referenced(path, tokens)
        if size >= min_file_mb * 1e6 and stale and not used:
            files.append({'path': path, 'mb': round(size / 1e6, 2)})
        for parent in PurePosixPath(path).parents:
            if str(parent) == '.':
                continue
            entry = folders[str(parent)]
            entry['bytes'] += size; entry['files'] += 1
            entry['recent'] |= not stale
            entry['referenced'] |= used
    candidates = [{'path': f, 'mb': round(e['bytes'] / 1e6, 1), 'files': e['files']}
                  for f, e in folders.items()
                  if e['bytes'] >= min_folder_mb * 1e6 and not e['recent'] and not e['referenced']]
    # Report the outermost candidate folder only.
    outer = [c for c in candidates
             if not any(c['path'].startswith(o['path'] + '/') for o in candidates if o is not c)]
    covered = lambda p: any(p.startswith(c['path'] + '/') for c in outer)
    return {'settings': {'min_file_mb': min_file_mb, 'min_folder_mb': min_folder_mb, 'stale_days': stale_days},
            'tracked_files': len(sizes), 'tracked_mb': round(sum(sizes.values()) / 1e6, 1),
            'folders': sorted(outer, key=lambda c: -c['mb']),
            'files': sorted((f for f in files if not covered(f['path'])), key=lambda f: -f['mb']),
            'archived_folders': archived_folders(sizes)}


def markdown(data):
    s = data['settings']
    lines = ['# Repository hygiene report', '',
             f"Report only; nothing was deleted. {data['tracked_files']} tracked files, {data['tracked_mb']} MB. "
             f"Listed: unchanged for {s['stale_days']}+ days, not referred to by any tracked code, workflow or "
             f"test, and at least {s['min_folder_mb']} MB (folders) or {s['min_file_mb']} MB (files); plus folders "
             "marked ARCHIVED. A listing is a question for review: data read through a glob can appear here.", '']
    if not (data['folders'] or data['files'] or data['archived_folders']):
        lines.append('Nothing to review.')
    if data['folders']:
        lines += ['## Folders', '', '| Folder | MB | Files |', '| --- | ---: | ---: |']
        lines += [f"| `{c['path']}` | {c['mb']} | {c['files']} |" for c in data['folders']] + ['']
    if data['files']:
        lines += ['## Files', '', '| File | MB |', '| --- | ---: |']
        lines += [f"| `{f['path']}` | {f['mb']} |" for f in data['files']] + ['']
    if data['archived_folders']:
        lines += ['## Folders marked ARCHIVED', ''] + [f'- `{p}`' for p in data['archived_folders']] + ['']
    return '\n'.join(lines) + '\n'


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('--min-file-mb', type=float, default=1.0)
    parser.add_argument('--min-folder-mb', type=float, default=5.0)
    parser.add_argument('--stale-days', type=int, default=30)
    parser.add_argument('--output', type=Path)
    parser.add_argument('--json', type=Path)
    args = parser.parse_args(argv)
    data = report(args.min_file_mb, args.min_folder_mb, args.stale_days)
    text = markdown(data)
    if args.output:
        args.output.write_text(text, encoding='utf-8')
    else:
        sys.stdout.write(text)
    if args.json:
        args.json.write_text(json.dumps(data, indent=1), encoding='utf-8')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
