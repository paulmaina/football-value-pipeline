"""Replay saved live forecasts through the live master and the new master (Phase 4, revised master rule, shadow).

For every archived run in football_output_v2/performance/snapshots generated in [--start, --end), rebuild the
run's decision rows from its frozen predictions at the run's own clock with the current production rules
(price_edge_cagey_shortlist.build_shortlist with cagey_correction_config.json, the quote policy and the current
lookahead), then call master_shortlist.refresh, exactly as the pipeline does. Each run's outputs go to
<output>/runs/<snapshot>/: master_shortlist.csv, master_shortlist_audit.csv, master_summary.json, decisions.csv
(the run's decision rows after the refresh: every live probability and both lists' picks, the cagey tier's
included) and, on a branch with the shadow, master_shortlist_new.csv and its summary.

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
# decisions.csv: the run's decision rows after the master refresh, i.e. every live probability and both lists' picks
# (value shortlist and cagey tier), so the comparison also shows the cagey tier untouched.
LIVE_FILES = ('master_shortlist.csv', 'master_shortlist_audit.csv', 'master_summary.json', 'decisions.csv',
              # the shadow new master, and (absent before the release) the release's files: under live "old" the
              # branch must write exactly main's files and nothing else
              'master_shortlist_new.csv', 'master_shortlist_new_summary.json', 'master_shortlist_old.csv',
              'master_shortlist_old_audit.csv', 'master_shortlist_summary.json', 'master_old_summary.json')


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
            decisions.to_csv(target / 'decisions.csv', index=False)
            entry.update(run_fixtures(decisions))
            (target / 'master_summary.json').write_text(
                json.dumps(summary.get('master_shortlist'), indent=2, sort_keys=True, default=str) + '\n',
                encoding='utf-8')
            if summary.get('master_shortlist_old') is not None:  # since the release: the old master, in shadow
                (target / 'master_old_summary.json').write_text(
                    json.dumps(summary['master_shortlist_old'], indent=2, sort_keys=True, default=str) + '\n',
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


def run_fixtures(decisions) -> dict:
    """The run's matches, and those with an executable offer, where the replayed code has the fill rule; {} otherwise
    (e.g. replaying main before it). Under rule v4 the new master draws only on the nominations, whose coverage is in
    the shadow summary (nominated_fixtures, fixtures_with_market_view)."""
    try:
        import master_reconciliation as mr
        from performance_tracking import fixture_key
        config = mr.load_config()
        records = mr._records(decisions)
        return {'fixtures': len({fixture_key(r) for r in records}),
                'fixtures_with_executable_offer': len({fixture_key(r) for r in records
                                                       if mr.executable(r, config) is None})}
    except Exception:  # noqa: BLE001  (older code: no fill rule)
        return {}


def totals(output: Path, report: dict) -> dict:
    """New-master inclusion, labels, flags and overlap summed over the replayed runs (integration check only)."""
    out = {'runs_with_shadow': 0, 'offers': 0, 'not_executable_offers': 0, 'offers_by_group': {}, 'gap_checks': {},
           'left_out_by_reason': {}, 'labels_offers': {}, 'labels_ranked': {}, 'decisions': {},
           'overlap_with_live_master': {}, 'ranked_fixtures': 0, 'shortfall': 0, 'european_offers': 0,
           'european_ranked': 0, 'inspection_flagged_offers': 0, 'for_inspection': [], 'per_run': [],
           'list_size': {}}
    for entry in report['runs']:
        path = output / 'runs' / entry['snapshot'] / 'master_shortlist_new_summary.json'
        if not path.exists():
            continue
        s = json.loads(path.read_text(encoding='utf-8'))
        out['runs_with_shadow'] += 1
        for key in ('offers_by_group', 'gap_checks', 'left_out_by_reason', 'labels_offers', 'labels_ranked',
                    'decisions', 'overlap_with_live_master'):
            for name, value in s[key].items():
                out[key][name] = out[key].get(name, 0) + value
        for key in ('offers', 'not_executable_offers', 'ranked_fixtures', 'shortfall', 'european_offers',
                    'european_ranked'):
            out[key] += s[key]
        out['inspection_flagged_offers'] += s['for_inspection']['flagged_offers']
        out['for_inspection'] += [{'snapshot': entry['snapshot'], **pick} for pick in s['for_inspection']['picks']]
        timed = s.get('timing_check') or {}
        out.setdefault('timing_ineligible_offers', 0)
        out['timing_ineligible_offers'] += timed.get('ineligible_offers', 0)
        for name, value in (timed.get('by_reason') or {}).items():
            out.setdefault('timing_by_reason', {})[name] = out.get('timing_by_reason', {}).get(name, 0) + value
        for name, value in (s.get('picks_by_tier') or {}).items():
            out.setdefault('picks_by_tier', {})[name] = out.get('picks_by_tier', {}).get(name, 0) + value
        out['per_run'].append({'snapshot': entry['snapshot'], 'generated_at_utc': entry['generated_at_utc'],
                               'fixtures': entry.get('fixtures'),
                               'fixtures_with_executable_offer': entry.get('fixtures_with_executable_offer'),
                               'target': s['target_fixtures'], 'nominated_fixtures': s.get('nominated_fixtures'),
                               'fixtures_with_market_view': s.get('fixtures_with_market_view'),
                               'fixtures_without_market_view': s.get('fixtures_without_market_view'),
                               'short_reason': s.get('short_reason'),
                               'timing_ineligible_offers': timed.get('ineligible_offers'),
                               'timing_by_reason': {k: v for k, v in (timed.get('by_reason') or {}).items() if v},
                               'offers': s['offers'], 'ranked': s['ranked_fixtures'],
                               'picks_by_tier': s.get('picks_by_tier'), 'groups': s['offers_by_group'],
                               'labels_ranked': s['labels_ranked'], 'overlap': s['overlap_with_live_master'],
                               'european_offers': s['european_offers']})
    runs_ = out['per_run']
    target = max((r['target'] for r in runs_), default=15)
    nominated = [r['nominated_fixtures'] for r in runs_ if r['nominated_fixtures'] is not None]
    out['list_size'] = {
        'runs': len(runs_), 'target': target,
        'runs_listing_target': sum(r['ranked'] >= target for r in runs_),
        'runs_short': sum(r['ranked'] < target for r in runs_),
        'runs_nominations_cover_fewer_than_target': sum(n < target for n in nominated),
        'runs_with_market_view_fewer_than_target': sum((r['fixtures_with_market_view'] or 0) < target for r in runs_),
        'runs_with_matches_without_market_view': sum(bool(r['fixtures_without_market_view']) for r in runs_),
        'runs_without_nominations': sum(n == 0 for n in nominated),
        'ranked_per_run': [r['ranked'] for r in runs_],
        'every_run_lists_min_target_and_viewed': all(
            r['ranked'] == min(target, r['fixtures_with_market_view'] or 0) for r in runs_)}
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


# The release (14 Nov 2026): branch file under live "new" -> the main (pre-release) file it must equal byte for byte,
# apart from the file name and the version field (new_master_version in the CSV; version, status and note in the new
# master's summary, which said "shadow only" before).
RELEASE_PAIRS = (('master_shortlist.csv', 'master_shortlist_new.csv'),
                 ('master_shortlist_summary.json', 'master_shortlist_new_summary.json'),
                 ('master_shortlist_old.csv', 'master_shortlist.csv'),
                 ('master_shortlist_old_audit.csv', 'master_shortlist_audit.csv'),
                 ('master_old_summary.json', 'master_summary.json'),
                 ('decisions.csv', 'decisions.csv'))


def _normalised(path: Path, live_version: str, rule_version: str) -> bytes:
    data = path.read_bytes()
    if path.name == 'master_shortlist.csv':
        return data.replace(live_version.encode(), rule_version.encode())
    if path.name in ('master_shortlist_summary.json', 'master_shortlist_new_summary.json'):
        info = json.loads(data)
        for key in ('version', 'status', 'note'):
            info.pop(key)
        return json.dumps(info, indent=2, default=str).encode()
    return data


def release_compare(main: Path, branch: Path) -> dict:
    """Main's replay (pre-release) against the branch's under live "new", file by file through RELEASE_PAIRS; also
    checks the run summary's live master is the new master's summary file, and the CSV differs from main's shadow file
    only in new_master_version."""
    sys.path.insert(0, str(ROOT))
    import master_reconciliation as mr
    import master_shortlist
    left = json.loads((main / 'replay.json').read_text(encoding='utf-8'))
    right = json.loads((branch / 'replay.json').read_text(encoding='utf-8'))
    a, b = {r['snapshot']: r for r in left['runs']}, {r['snapshot']: r for r in right['runs']}
    result = {'runs_main': len(a), 'runs_branch': len(b), 'same_runs': sorted(a) == sorted(b), 'pairs': RELEASE_PAIRS,
              'compared_files': 0, 'differences': [], 'runs_ok': 0}
    for name in sorted(set(a) & set(b)):
        if not (a[name].get('status') == b[name].get('status') == 'ok'):
            result['differences'].append({'snapshot': name, 'status': [a[name].get('status'), b[name].get('status')]})
            continue
        result['runs_ok'] += 1
        for mine, theirs in RELEASE_PAIRS:
            ours, base = branch / 'runs' / name / mine, main / 'runs' / name / theirs
            result['compared_files'] += 1
            if not (ours.exists() and base.exists()) or (
                    _normalised(ours, master_shortlist.VERSION_NEW_LIVE, mr.VERSION)
                    != _normalised(base, master_shortlist.VERSION_NEW_LIVE, mr.VERSION)):
                result['differences'].append({'snapshot': name, 'file': [mine, theirs]})
        live = json.loads((branch / 'runs' / name / 'master_summary.json').read_text(encoding='utf-8'))
        written = json.loads((branch / 'runs' / name / 'master_shortlist_summary.json').read_text(encoding='utf-8'))
        if live != written or live.get('version') != master_shortlist.VERSION_NEW_LIVE:
            result['differences'].append({'snapshot': name, 'file': 'run summary master_shortlist'})
        new = pd.read_csv(branch / 'runs' / name / 'master_shortlist.csv', dtype=str, keep_default_na=False)
        shadow = pd.read_csv(main / 'runs' / name / 'master_shortlist_new.csv', dtype=str, keep_default_na=False)
        changed = [c for c in new.columns if list(new.columns) != list(shadow.columns) or not new[c].equals(shadow[c])]
        if changed != (['new_master_version'] if len(new) else []):
            result['differences'].append({'snapshot': name, 'columns_changed': changed})
        if set(new.get('new_master_version', [])) - {master_shortlist.VERSION_NEW_LIVE}:
            result['differences'].append({'snapshot': name, 'file': 'version field'})
    result['byte_identical_apart_from_names_and_version'] = result['same_runs'] and not result['differences']
    return result


def _switched_config(live: str, directory: Path) -> Path:
    """A copy of master_shortlist_config.json with only the `live` switch changed."""
    import master_shortlist
    config = json.loads(master_shortlist.CONFIG.read_text(encoding='utf-8'))
    config['live'] = live
    path = directory / 'master_shortlist_config.json'
    path.write_text(json.dumps(config, indent=2) + '\n', encoding='utf-8')
    return path


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('--root', type=Path, default=ROOT, help='repository whose code and snapshots are replayed')
    parser.add_argument('--output', type=Path)
    parser.add_argument('--start', default='2026-10-27')
    parser.add_argument('--end', default='2026-11-09', help='exclusive')
    parser.add_argument('--compare', nargs=2, type=Path, metavar=('MAIN', 'BRANCH'))
    parser.add_argument('--release-compare', nargs=2, type=Path, metavar=('MAIN', 'BRANCH'),
                        help='main (pre-release) against the branch replayed with live "new"')
    parser.add_argument('--live', choices=('new', 'old'),
                        help='replay with master_shortlist_config.json\'s live switch set to this (a copy of the '
                             'config with only that field changed); default: the config as committed')
    args = parser.parse_args(argv)
    if args.compare:
        result = compare(*args.compare)
        print(json.dumps(result, indent=2))
        return 0 if result['byte_identical'] else 1
    if args.release_compare:
        result = release_compare(*args.release_compare)
        print(json.dumps(result, indent=2))
        return 0 if result['byte_identical_apart_from_names_and_version'] else 1
    args.output.mkdir(parents=True, exist_ok=True)
    if args.live:
        sys.path.insert(0, str(args.root.resolve()))
        import master_shortlist
        master_shortlist.CONFIG = _switched_config(args.live, args.output)
    report = replay(args.root.resolve(), args.output, args.start, args.end)
    print(json.dumps({r['snapshot']: r['status'] for r in report['runs']}, indent=2))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
