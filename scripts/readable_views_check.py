"""Check the readable league outputs against a run's shortlist and master files (display-only outputs).

For every fixture and every Pinnacle offer of a run bundle:

- the master's verdict the readable files show (readable_views: research and cagey no-loss, gap, gap check and
  label, inspection flag, cagey tier, labels) equals the master file's row for every offer the master scored
  (master_shortlist.csv, or master_shortlist_new.csv where the old master was live);
- the value shortlist's research probabilities and the cagey tier's cagey probabilities (research_p_*, cagey_p_* of
  their own files) give the readable no-loss figures of the same offer;
- each view's no-loss on a quoted Pinnacle AH line (the view columns) equals the run's decision row for that line;
- with --formatted (or the saved-run mode), the formatted *_predictions_readable.csv shows those values: the best
  offer of a fixture on the master is its master pick, with the master file's no-loss, gap, label and tier.

    python scripts/readable_views_check.py --bundle football_output_v2/raw [--formatted football_output_v2/readable]
    python scripts/readable_views_check.py --saved --output <dir>   # the 29 saved runs, every list rebuilt

Display only: nothing here or in what it checks decides, grades or stakes anything.
"""
from __future__ import annotations

import argparse
import contextlib
import importlib.util
import io
import json
import math
import sys
import warnings
from pathlib import Path
from typing import Dict, List, Optional

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
EXACT, GRID = 1e-12, 1e-9   # decision-row figures read back exactly; a rebuilt cagey grid to fit noise
KINDS = ('win', 'half_win', 'push', 'half_loss', 'loss')
COMPARED = ('research_no_loss_probability', 'cagey_no_loss_probability', 'gap_points', 'gap_check',
            'inspection_flag', 'market_safety', 'market_price', 'market_basis')


def _value(v):
    if v is None or (isinstance(v, float) and math.isnan(v)):
        return None
    return v


def _same(a, b, tol=EXACT) -> bool:
    a, b = _value(a), _value(b)
    if a is None or b is None:
        return a is None and b is None
    if isinstance(a, (bool, str)) or isinstance(b, (bool, str)):
        if isinstance(a, str) and a.lower() in ('true', 'false'):
            a = a.lower() == 'true'
        if isinstance(b, str) and b.lower() in ('true', 'false'):
            b = b.lower() == 'true'
        return a == b
    return abs(float(a) - float(b)) <= tol


def _no_loss(record, prefix) -> Optional[float]:
    import master_reconciliation as mr
    mass = mr.settlement_mass([record.get(prefix + k) for k in KINDS])
    return None if mass is None else mr.no_loss(mass)


def _labels(text) -> set:
    return {t.strip() for t in str(_value(text) or '').split(';') if t.strip()} - {'risky fill'}


def _records(frame) -> List[dict]:
    if frame is None or frame.empty:
        return []
    return frame.astype(object).where(frame.notna(), None).to_dict('records')


def check_bundle(raw: Path, formatted: Optional[Path] = None) -> Dict[str, object]:
    """Counts and problems for one run bundle (and, if given, its formatted readable folder)."""
    import master_reconciliation as mr
    import readable_views as rv
    from performance_tracking import fixture_key
    raw = Path(raw)
    from prediction_runs import resolve_raw
    raw = resolve_raw(raw)
    run = rv.Run(raw)
    problems: List[str] = []
    counts = dict.fromkeys(('fixtures', 'offers', 'master_rows', 'value_picks', 'cagey_picks', 'ah_lines_research',
                            'ah_lines_cagey', 'formatted_rows', 'formatted_master_fixtures'), 0)
    if run.decisions is None:
        return {'bundle': str(raw), 'problems': ['no decision rows in the bundle'], 'counts': counts}
    offers = {rv.offer_key(o): o for rows in (run.offers() or {}).values() for o in rows}
    infos = {}
    for row in _records(run.predictions):
        infos[fixture_key(row)] = (row, rv.fixture(row, run))
    counts['fixtures'] = len(infos)

    # 1. Every Pinnacle offer of the decision rows: the readable offer and each view's AH line figure.
    for record in _records(run.decisions):
        if record.get('bookmaker') != 'Pinnacle' or (rv.number(record.get('offered_decimal_odds')) or 0) <= 1:
            continue
        counts['offers'] += 1
        label = f"{fixture_key(record)} {record.get('market_to_bet')} @ {record.get('offered_decimal_odds')}"
        mine = offers.get(rv.offer_key(record))
        if mine is None:
            problems.append(f'{label}: offer missing from the readable view')
            continue
        research = mr.research_view(record)[0]
        cagey = mr.cagey_view(record)[0]
        for name, mass in (('research_no_loss_probability', research), ('cagey_no_loss_probability', cagey)):
            if not _same(mine[name], None if mass is None else mr.no_loss(mass)):
                problems.append(f'{label}: {name} {mine[name]} vs decision row')
        info = infos.get(fixture_key(record), (None, None))[1]
        cagey_view = (info or {}).get('cagey', {})
        if _value(record.get('cagey_correction')) is not None:
            counts['cagey_corrections'] = counts.get('cagey_corrections', 0) + 1
            if cagey_view.get('correction') != record['cagey_correction'] \
                    or _value(cagey_view.get('fallback')) != _value(record.get('cagey_correction_fallback')):
                problems.append(f"{label}: cagey correction {cagey_view.get('correction')!r} / "
                                f"{cagey_view.get('fallback')!r} vs decision row {record['cagey_correction']!r} / "
                                f"{record.get('cagey_correction_fallback')!r}")
        if not str(record.get('market') or '').startswith('Asian Handicap ') \
                or record.get('source_market') == 'draw_no_bet':
            continue
        line = next((l for l in (info or {}).get('lines', []) if l['side'] == record.get('handicap_side')
                     and abs(l['line'] - float(record['handicap_line'])) < 1e-9), None)
        if line is None:
            problems.append(f'{label}: quoted AH line missing from the view columns')
            continue
        for view, prefix, tol, counter in (('research', 'research_p_', EXACT, 'ah_lines_research'),
                                           ('cagey', 'cagey_p_', GRID, 'ah_lines_cagey')):
            expected = _no_loss(record, prefix)
            if expected is None and line[view] is None:
                continue
            counts[counter] += 1
            if not _same(line[view], expected, tol):
                problems.append(f'{label}: {view} view AH no-loss {line[view]} vs decision row {expected}')

    # 2. The master file: every offer the master scored.
    master = run.master if run.master_new else rv._read_csv(raw / 'master_shortlist_new.csv')
    for row in _records(master):
        if row.get('bookmaker') != 'Pinnacle':
            continue
        counts['master_rows'] += 1
        label = f"master {fixture_key(row)} {row.get('market_to_bet')} @ {row.get('offered_decimal_odds')}"
        mine = offers.get(rv.offer_key(row))
        if mine is None:
            problems.append(f'{label}: missing from the readable view')
            continue
        for name in COMPARED:
            if not _same(mine.get(name), row.get(name), GRID if name == 'gap_points' else EXACT):
                problems.append(f'{label}: {name} {mine.get(name)!r} vs master {row.get(name)!r}')
        if _labels(mine.get('new_master_labels')) != _labels(row.get('new_master_labels')):
            problems.append(f"{label}: labels {mine.get('new_master_labels')!r} vs master {row.get('new_master_labels')!r}")
        if rv.gap_label(mine, run.config) != rv.gap_label({**row, 'inspection_flag': _same(row.get('inspection_flag'),
                                                                                             True)}, run.config):
            problems.append(f'{label}: gap label differs')
        if rv.cagey_tier(mine) != rv.cagey_tier(row):
            problems.append(f'{label}: cagey tier differs')

    # 3. The two lists' own probabilities.
    for frame, prefix, name, counter in ((run.value, 'research_p_', 'research_no_loss_probability', 'value_picks'),
                                         (run.cagey_list, 'cagey_p_', 'cagey_no_loss_probability', 'cagey_picks')):
        for pick in _records(frame):
            counts[counter] += 1
            label = f"{counter} {fixture_key(pick)} {pick.get('market_to_bet')} @ {pick.get('offered_decimal_odds')}"
            mine = offers.get(rv.offer_key(pick))
            if mine is None:
                problems.append(f'{label}: missing from the readable view')
            elif not _same(mine[name], _no_loss(pick, prefix)):
                problems.append(f'{label}: {name} {mine[name]} vs list file {_no_loss(pick, prefix)}')

    # 4. The formatted CSVs: what a reader sees.
    if formatted is not None:
        import format_football_output as fo
        for path in sorted(Path(formatted).glob('*_predictions_readable.csv')):
            frame = pd.read_csv(path, dtype=str, keep_default_na=False, encoding='utf-8-sig')
            for row in frame.to_dict('records'):
                key = fixture_key({'league': row['League'], 'home_team': row['Home team'],
                                   'away_team': row['Away team'], 'kickoff_utc': row['Kickoff (UTC)']})
                if key not in infos:
                    continue
                counts['formatted_rows'] += 1
                forecast, info = infos[key]
                picks = run.master_picks(key)
                if picks and run.master_new:
                    counts['formatted_master_fixtures'] += 1
                    pick = picks[0]
                    gap = rv.number(pick.get('gap_points'))
                    want = {'Best offer': rv._offer_text(pick),
                            'Best offer research no-loss': fo.pct(pick.get('research_no_loss_probability')),
                            'Best offer cagey no-loss': fo.pct(pick.get('cagey_no_loss_probability')),
                            'Best offer gap (points)': f'{gap:+.1f}' if gap is not None else '—',
                            'Best offer cagey tier': rv.cagey_tier(pick)}
                    for column, value in want.items():
                        if row[column] != value:
                            problems.append(f'{path.name} {key}: {column} {row[column]!r} vs master {value!r}')
                    if not row['On master'].startswith(f"yes: rank {rv.number(pick['new_master_rank']):.0f}"):
                        problems.append(f"{path.name} {key}: On master {row['On master']!r}")
                elif row['On master'] not in ('no', 'master list not in this run bundle') and not picks:
                    problems.append(f"{path.name} {key}: On master {row['On master']!r} but no master pick")
    return {'bundle': str(raw), 'counts': counts, 'problems': problems}


def _saved_runs_tool():
    spec = importlib.util.spec_from_file_location('format_saved_runs', ROOT / 'scripts' / 'format_saved_runs.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def check_saved(output: Path, start: str, end: str, only: Optional[List[str]] = None) -> Dict[str, object]:
    """Rebuild every list of each saved run (format_saved_runs --lists), format it and check it."""
    import format_football_output as fo
    tool = _saved_runs_tool()
    report = {'runs': [], 'counts': {}, 'problems': 0}
    for _, snapshot in tool.runs(ROOT, start, end):
        if only and snapshot.name not in only:
            continue
        raw = tool.bundle(snapshot, output / 'bundles' / snapshot.name, lists=True)
        out = output / 'runs' / snapshot.name
        with warnings.catch_warnings(), contextlib.redirect_stdout(io.StringIO()):
            warnings.simplefilter('ignore')
            fo.main(['--root-dir', str(output / 'root'), '--input-dir', str(raw), '--output-dir', str(out)])
        result = check_bundle(raw, out)
        result['snapshot'] = snapshot.name
        report['runs'].append(result)
        for k, v in result['counts'].items():
            report['counts'][k] = report['counts'].get(k, 0) + v
        report['problems'] += len(result['problems'])
    return report


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--bundle', type=Path)
    parser.add_argument('--formatted', type=Path)
    parser.add_argument('--saved', action='store_true')
    parser.add_argument('--output', type=Path)
    parser.add_argument('--start', default='2026-10-27')
    parser.add_argument('--end', default='2026-11-09', help='exclusive')
    args = parser.parse_args(argv)
    if args.saved:
        if args.output is None:
            parser.error('--saved needs --output')
        report = check_saved(args.output.resolve(), args.start, args.end)
        print(json.dumps({'runs': len(report['runs']), 'counts': report['counts'], 'problems': report['problems'],
                          'first_problems': [p for r in report['runs'] for p in r['problems']][:20]}, indent=2))
        (args.output / 'readable_views_check.json').write_text(json.dumps(report, indent=1) + '\n', encoding='utf-8')
        return 1 if report['problems'] else 0
    if args.bundle is None:
        parser.error('give --bundle or --saved')
    result = check_bundle(args.bundle, args.formatted)
    print(json.dumps({**result, 'problems': result['problems'][:20], 'n_problems': len(result['problems'])},
                     indent=2))
    return 1 if result['problems'] else 0


if __name__ == '__main__':
    raise SystemExit(main())
