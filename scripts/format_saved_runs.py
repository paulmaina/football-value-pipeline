"""Format saved live runs with a chosen code tree, and compare two trees' outputs byte for byte.

Evidence for reporting-only changes (e.g. the Excel redesign): for every archived run in
football_output_v2/performance/snapshots generated in [--start, --end), a raw bundle is rebuilt from the
snapshot (forecasts split per league under production's league keys, the shortlist and its summary, every sidecar
the snapshot holds), then format_football_output.py from --code-root formats it into <output>/runs/<snapshot>/.
Run it once with main's tree and once with the branch, then --compare: every output except the two workbooks
must be byte-identical.

--release also rebuilds each run's master lists with this tree's current production rules (the released new
master live, the old master in shadow, as scripts/master_reconciliation_replay.py does) before formatting, so the
workbook can be seen with both master lists filled. Integration evidence only: no result is read.

    python scripts/format_saved_runs.py --output <dir> --code-root <tree>
    python scripts/format_saved_runs.py --compare <main output> <branch output>
"""
from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import subprocess
import sys
import warnings
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SNAPSHOTS = Path('football_output_v2') / 'performance' / 'snapshots'
WORKBOOKS = ('league_predictions.xlsx', 'football_performance_report.xlsx')
SIDECARS = ('bet365_vs_pinnacle.csv', 'cagey_correction_monitoring.csv', 'cagey_tier_shortlist.csv',
            'master_shortlist.csv', 'master_shortlist_audit.csv', 'master_shortlist_new.csv',
            'master_shortlist_old.csv', 'price_edge_tagged_candidates.csv')


def runs(root: Path, start: str, end: str):
    out = []
    for directory in sorted((root / SNAPSHOTS).iterdir()):
        try:
            summary = json.loads((directory / 'selection_summary.json').read_text(encoding='utf-8'))
        except (OSError, ValueError):
            continue
        generated = str(summary.get('generated_at_utc') or '')
        if start <= generated[:10] < end and (directory / 'predictions.csv').exists():
            out.append((generated, directory))
    return sorted(out)


def bundle(snapshot: Path, target: Path, release: bool = False) -> Path:
    """A raw bundle the formatter reads, from one archived run."""
    import pandas as pd
    from league_registry import REGISTRY
    keys = {league.name: league.key for league in REGISTRY}
    target.mkdir(parents=True, exist_ok=True)
    predictions = pd.read_csv(snapshot / 'predictions.csv', dtype=str, keep_default_na=False)
    for league, group in predictions.groupby('league', sort=True):
        key = keys.get(league, ''.join(ch for ch in league if ch.isalnum()) or 'League')
        group.to_csv(target / f'{key}_predictions.csv', index=False)
    shutil.copyfile(snapshot / 'shortlist.csv', target / 'conservative_bet_shortlist.csv')
    shutil.copyfile(snapshot / 'selection_summary.json', target / 'conservative_bet_summary.json')
    for name in SIDECARS:
        if (snapshot / name).exists():
            shutil.copyfile(snapshot / name, target / name)
    if release:
        rebuild_masters(snapshot, target)
    return target


def rebuild_masters(snapshot: Path, target: Path) -> None:
    """The run's master lists under this tree's production rules (new master live, old in shadow)."""
    import pandas as pd
    import master_shortlist
    import narrow_margin as nm
    import price_edge_cagey_shortlist as v28
    from quote_policy import load_policy
    summary = json.loads((snapshot / 'selection_summary.json').read_text(encoding='utf-8'))
    predictions = pd.read_csv(snapshot / 'predictions.csv', low_memory=False)
    for name in ('master_shortlist.csv', 'master_shortlist_audit.csv', 'master_shortlist_new.csv'):
        (target / name).unlink(missing_ok=True)
    with warnings.catch_warnings():
        warnings.simplefilter('ignore')
        _, decisions, rebuilt = v28.build_shortlist(predictions, pd.Timestamp(summary['generated_at_utc']),
                                                    execution_policy=load_policy(), model=nm.production_model())
        rebuilt.setdefault('quote_execution_policy', load_policy())
        master_shortlist.refresh(decisions, target, rebuilt, predictions)
    for key in ('master_shortlist', 'master_shortlist_old', master_shortlist.RELEASE_STATUS_KEY):
        if key in rebuilt:
            summary[key] = rebuilt[key]
    (target / 'conservative_bet_summary.json').write_text(json.dumps(summary, indent=2, default=str) + '\n',
                                                         encoding='utf-8')


def format_run(code_root: Path, raw: Path, output: Path) -> subprocess.CompletedProcess:
    work = output.parent / (output.name + '.root')
    work.mkdir(parents=True, exist_ok=True)
    return subprocess.run([sys.executable, str(code_root / 'format_football_output.py'), '--root-dir', str(work),
                           '--input-dir', str(raw), '--output-dir', str(output)],
                          cwd=code_root, stdin=subprocess.DEVNULL, capture_output=True, text=True)


def produce(root: Path, code_root: Path, output: Path, start: str, end: str, release: bool) -> dict:
    sys.path.insert(0, str(root))
    report = {'code_root': str(code_root), 'start': start, 'end_exclusive': end, 'release': release, 'runs': []}
    for generated, snapshot in runs(root, start, end):
        raw = bundle(snapshot, output / 'bundles' / snapshot.name, release)
        out = output / 'runs' / snapshot.name
        if out.exists():
            shutil.rmtree(out)
        result = format_run(code_root, raw, out)
        files = {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(out.iterdir()) if p.is_file()} \
            if out.exists() else {}
        report['runs'].append({'snapshot': snapshot.name, 'generated_at_utc': generated,
                               'status': 'ok' if result.returncode == 0 else 'failed',
                               'error': result.stderr[-2000:] if result.returncode else None, 'files': files})
    output.mkdir(parents=True, exist_ok=True)
    (output / 'formatted.json').write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    return report


def compare(a: Path, b: Path) -> dict:
    """Every formatted file except the workbooks, byte for byte, in every run of both outputs. The verdict
    (byte_identical) is over the CSVs; other files (Markdown reports, README) are listed when they differ."""
    out = {'runs': 0, 'files_compared': 0, 'identical': 0, 'csv_compared': 0, 'csv_identical': 0, 'different': [],
           'missing': [], 'workbooks_skipped': 0}
    for run_a in sorted((a / 'runs').iterdir()):
        if not run_a.is_dir() or run_a.name.endswith('.root'):
            continue
        run_b = b / 'runs' / run_a.name
        out['runs'] += 1
        names = {p.name for p in run_a.iterdir() if p.is_file()} | (
            {p.name for p in run_b.iterdir() if p.is_file()} if run_b.exists() else set())
        for name in sorted(names):
            if name in WORKBOOKS:
                out['workbooks_skipped'] += 1
                continue
            pa, pb = run_a / name, run_b / name
            if not pa.exists() or not pb.exists():
                out['missing'].append(f'{run_a.name}/{name}')
                continue
            out['files_compared'] += 1
            same = pa.read_bytes() == pb.read_bytes()
            out['identical'] += same
            if name.endswith('.csv'):
                out['csv_compared'] += 1
                out['csv_identical'] += same
            if not same:
                out['different'].append(f'{run_a.name}/{name}')
    csv_problems = [p for p in out['different'] + out['missing'] if p.endswith('.csv')]
    out['other_files_different'] = sorted({p.split('/', 1)[1] for p in out['different'] if not p.endswith('.csv')})
    out['byte_identical'] = not csv_problems and out['csv_compared'] > 0
    return out


def normalised_digest(data: bytes) -> str:
    return hashlib.sha256(data.replace(b'\r\n', b'\n')).hexdigest()


def csv_digests(output: Path) -> dict:
    """{snapshot: {csv name: sha256}} of a formatted tree, line endings normalised to LF (pandas writes CRLF on
    Windows), so a digest taken on one platform checks the same CSV text on another."""
    out = {}
    for run in sorted((output / 'runs').iterdir()):
        if run.is_dir() and not run.name.endswith('.root'):
            out[run.name] = {p.name: normalised_digest(p.read_bytes()) for p in sorted(run.glob('*.csv'))}
    return out


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--output', type=Path)
    parser.add_argument('--code-root', type=Path, default=ROOT)
    parser.add_argument('--root', type=Path, default=ROOT, help='repository whose snapshots are formatted')
    parser.add_argument('--start', default='2026-10-27')
    parser.add_argument('--end', default='2026-11-09', help='exclusive')
    parser.add_argument('--release', action='store_true')
    parser.add_argument('--compare', nargs=2, type=Path)
    parser.add_argument('--digests', nargs=2, type=Path, metavar=('OUTPUT', 'JSON'),
                        help="write a formatted tree's CSV digests, line endings normalised")
    args = parser.parse_args(argv)
    if args.digests:
        source, target = args.digests
        target.write_text(json.dumps(csv_digests(source), indent=1, sort_keys=True) + '\n', encoding='utf-8')
        return 0
    if args.compare:
        result = compare(*args.compare)
        print(json.dumps(result, indent=2))
        return 0 if result['byte_identical'] else 1
    if args.output is None:
        parser.error('--output is required')
    report = produce(args.root.resolve(), args.code_root.resolve(), args.output.resolve(), args.start, args.end,
                     args.release)
    failed = [r['snapshot'] for r in report['runs'] if r['status'] != 'ok']
    print(f"{len(report['runs'])} runs formatted, {len(failed)} failed{': ' + ', '.join(failed) if failed else ''}")
    return 1 if failed else 0


if __name__ == '__main__':
    raise SystemExit(main())
