"""Replay saved live forecasts through the live master and the new master (Phase 4, Paul's master rule, shadow).

For every archived run in football_output_v2/performance/snapshots generated in [--start, --end), rebuild the
run's decision rows from its frozen predictions at the run's own clock with the current production rules
(price_edge_cagey_shortlist.build_shortlist with cagey_correction_config.json, the quote policy and the current
lookahead), then call master_shortlist.refresh, exactly as the pipeline does. Each run's outputs go to
<output>/runs/<snapshot>/: master_shortlist.csv, master_shortlist_audit.csv, master_summary.json and, on a
branch with the shadow, master_shortlist_new.csv and its summary.

Integration check, not evidence: no result is read. Run it on main and on the branch with the same arguments
and compare the live master files byte for byte (--compare).

    python scripts/master_reconciliation_replay.py --output <dir>
    python scripts/master_reconciliation_replay.py --compare <main output> <branch output>
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
import traceback
import warnings
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
SNAPSHOTS = Path('football_output_v2') / 'performance' / 'snapshots'
LIVE_FILES = ('master_shortlist.csv', 'master_shortlist_audit.csv', 'master_summary.json')


def runs(root: Path, start: str, end: str):
    out = []
    for directory in sorted((root / SNAPSHOTS).iterdir()):
        try:
            summary = json.loads((directory / 'selection_summary.json').read_text(encoding='utf-8'))
        except (OSError, ValueError):
            continue
        generated = str(summary.get('generated_at_utc') or '')
        if start <= generated[:10] < end and (directory / 'predictions.csv').exists():
            out.append((generated, directory, summary))
    return sorted(out, key=lambda item: item[0])


def replay(root: Path, output: Path, start: str, end: str) -> dict:
    sys.path.insert(0, str(root))
    import master_shortlist
    import narrow_margin as nm
    import price_edge_cagey_shortlist as v28
    from quote_policy import load_policy
    report = {'root': str(root), 'start': start, 'end_exclusive': end, 'runs': []}
    for generated, directory, recorded in runs(root, start, end):
        target = output / 'runs' / directory.name
        target.mkdir(parents=True, exist_ok=True)
        entry = {'snapshot': directory.name, 'generated_at_utc': generated,
                 'recorded_policy': recorded.get('selection_policy_version'),
                 'recorded_master_version': (recorded.get('master_shortlist') or {}).get('version')}
        try:
            predictions = pd.read_csv(directory / 'predictions.csv', low_memory=False)
            with warnings.catch_warnings():
                warnings.simplefilter('ignore')
                _, decisions, summary = v28.build_shortlist(predictions, pd.Timestamp(generated),
                                                            execution_policy=load_policy(), model=nm.production_model())
                summary.setdefault('quote_execution_policy', load_policy())
                master_shortlist.refresh(decisions, target, summary, predictions)
            (target / 'master_summary.json').write_text(
                json.dumps(summary.get('master_shortlist'), indent=2, sort_keys=True, default=str) + '\n',
                encoding='utf-8')
            entry.update(status='ok', decisions=int(len(decisions)),
                         value_shortlisted=int(decisions.decision.eq('SHORTLISTED').sum()),
                         cagey_shortlisted=int(decisions.get('cagey_tier_decision', pd.Series(dtype=object))
                                               .eq('SHORTLISTED').sum()))
        except Exception as exc:  # recorded, the replay continues with the next run
            entry.update(status='failed', error=f'{type(exc).__name__}: {exc}',
                         traceback=traceback.format_exc(limit=3))
        entry['files'] = {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(target.iterdir())}
        report['runs'].append(entry)
    report['shadow_totals'] = totals(output, report)
    (output / 'replay.json').write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    return report


def totals(output: Path, report: dict) -> dict:
    """New-master groups, gap checks and overlap summed over the replayed runs (integration check only)."""
    out = {'runs_with_shadow': 0, 'offers': 0, 'not_executable_offers': 0, 'offers_by_group': {}, 'gap_checks': {},
           'left_out_by_reason': {}, 'one_view_missing': {}, 'ranked_by_group': {}, 'decisions': {},
           'overlap_with_live_master': {}, 'ranked_fixtures': 0, 'shortfall': 0, 'vetoed': 0, 'vetoed_cagey_picks': 0,
           'ignored': 0, 'no_view': 0, 'european_offers': 0, 'european_ranked': 0, 'per_run': []}
    for entry in report['runs']:
        path = output / 'runs' / entry['snapshot'] / 'master_shortlist_new_summary.json'
        if not path.exists():
            continue
        s = json.loads(path.read_text(encoding='utf-8'))
        out['runs_with_shadow'] += 1
        for key in ('offers_by_group', 'gap_checks', 'left_out_by_reason', 'one_view_missing', 'ranked_by_group',
                    'decisions', 'overlap_with_live_master'):
            for name, value in s[key].items():
                out[key][name] = out[key].get(name, 0) + value
        for key in ('offers', 'not_executable_offers', 'ranked_fixtures', 'shortfall', 'vetoed', 'vetoed_cagey_picks',
                    'ignored', 'no_view', 'european_offers', 'european_ranked'):
            out[key] += s[key]
        out['per_run'].append({'snapshot': entry['snapshot'], 'generated_at_utc': entry['generated_at_utc'],
                               'offers': s['offers'], 'ranked': s['ranked_fixtures'], 'groups': s['offers_by_group'],
                               'gap_checks': s['gap_checks'], 'overlap': s['overlap_with_live_master'],
                               'european_offers': s['european_offers']})
    return out


def compare(main: Path, branch: Path) -> dict:
    left = json.loads((main / 'replay.json').read_text(encoding='utf-8'))
    right = json.loads((branch / 'replay.json').read_text(encoding='utf-8'))
    a, b = {r['snapshot']: r for r in left['runs']}, {r['snapshot']: r for r in right['runs']}
    result = {'runs_main': len(a), 'runs_branch': len(b), 'same_runs': sorted(a) == sorted(b), 'differences': [],
              'compared_files': 0, 'runs_with_master': 0}
    for name in sorted(set(a) | set(b)):
        if a.get(name, {}).get('status') != b.get(name, {}).get('status'):
            result['differences'].append({'snapshot': name, 'status': [a.get(name, {}).get('status'),
                                                                       b.get(name, {}).get('status')]})
            continue
        result['runs_with_master'] += 'master_shortlist.csv' in a[name]['files']
        for file in LIVE_FILES:
            left_file, right_file = main / 'runs' / name / file, branch / 'runs' / name / file
            if not left_file.exists() and not right_file.exists():
                continue
            result['compared_files'] += 1
            if not (left_file.exists() and right_file.exists()) or left_file.read_bytes() != right_file.read_bytes():
                result['differences'].append({'snapshot': name, 'file': file})
    result['byte_identical'] = result['same_runs'] and not result['differences']
    return result


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('--root', type=Path, default=ROOT, help='repository whose code and snapshots are replayed')
    parser.add_argument('--output', type=Path)
    parser.add_argument('--start', default='2026-10-27')
    parser.add_argument('--end', default='2026-11-09', help='exclusive')
    parser.add_argument('--compare', nargs=2, type=Path, metavar=('MAIN', 'BRANCH'))
    args = parser.parse_args(argv)
    if args.compare:
        result = compare(*args.compare)
        print(json.dumps(result, indent=2))
        return 0 if result['byte_identical'] else 1
    args.output.mkdir(parents=True, exist_ok=True)
    report = replay(args.root.resolve(), args.output, args.start, args.end)
    print(json.dumps({r['snapshot']: r['status'] for r in report['runs']}, indent=2))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
