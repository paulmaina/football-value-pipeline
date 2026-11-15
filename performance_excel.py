"""Write football_performance_report.xlsx from the verified performance files (standard library only).

The workbook is a display of what the review has already graded; the sheets are laid out in
performance_report_layout.py with the shared theme in excel_book.py, so Windows and CI need no spreadsheet
engine. Nothing here grades, changes a pick or writes a CSV.

The review writes the workbook twice: once when the grades are ready (write_workbook) and once at the very end,
after the tracking, CLV and health reports exist (add_health_sheet), so the published workbook shows the run's
final figures.
"""
from __future__ import annotations

import argparse
from csv_utils import dict_reader
import json
import math
from pathlib import Path

from performance_report_layout import REPORT_NAME, write as write_layout


def num(value):
    try:
        x = float(value)
        return x if math.isfinite(x) else None
    except (TypeError, ValueError):
        return None


def probability(value):
    p = num(value)
    return p if p is not None and 0 <= p <= 1 else None


def prepared_rows(rows):
    """The shortlist ledger as graded rows, one per pick; a duplicate frozen pick is a hard error."""
    seen = set()
    result = []
    from performance_tracking import pick_key
    for row in sorted(rows, key=lambda r: (r.get('kickoff_utc', ''), r.get('fixture_key', ''), pick_key(r))):
        # One row per pick: per-market runs may hold several market groups for one fixture.
        if pick_key(row) in seen:
            raise ValueError('Duplicate frozen fixture in report: ' + pick_key(row))
        seen.add(pick_key(row))
        r = dict(row)
        r['p'] = probability(r.get('predicted_probability'))
        from asian_handicap import SETTLED, parse_label
        ah = parse_label(r.get('market'))
        from performance_tracking import calibration_outcome
        r['y'] = (calibration_outcome(r) if ah and r['status'] in SETTLED else
                  1 if r['status'] == 'WON' else 0 if r['status'] == 'LOST' else None)
        r['asian'] = ah is not None
        r['price'] = num(r.get('offered_decimal_odds'))
        if r['price'] is not None and r['price'] <= 1:
            r['price'] = None
        from quote_policy import stake_cost
        r['cost'] = stake_cost(r.get('per_stake_cost') or 0)
        r['priced'] = r['y'] is not None and r['price'] is not None
        r['gain'] = (float(r['unit_profit']) if r['asian'] else (r['price'] - 1 if r['y'] else -1) - r['cost']) \
            if r['priced'] else None
        r['scored_p'] = r['p'] if r['y'] is not None else None
        r['brier_value'] = (r['p'] - r['y']) ** 2 if r['scored_p'] is not None else None
        r['policy'] = r.get('selection_policy_version') or 'legacy/unspecified'
        result.append(r)
    return result


def summarize(rows):
    settled = [r for r in rows if r['y'] is not None]
    priced = [r for r in rows if r['priced']]
    prob = [r for r in settled if r['scored_p'] is not None]
    wins = sum(r['status'] in ('WON', 'HALF_WON') for r in settled)
    losses = sum(r['status'] in ('LOST', 'HALF_LOST') for r in settled)
    profit = sum(r['gain'] for r in priced)
    mean = sum(r['p'] for r in prob) / len(prob) if prob else None
    observed = sum(r['y'] for r in prob) / len(prob) if prob else None
    return [len(rows), len(settled), wins, losses, len(rows) - len(settled),
            wins / len(settled) if settled else 'n.a.', len(priced),
            profit, profit / len(priced) if priced else 'n.a.',
            sum(r['brier_value'] for r in prob) / len(prob) if prob else 'n.a.',
            mean if prob else 'n.a.', observed if prob else 'n.a.',
            mean - observed if prob else 'n.a.', len(prob)]


def write_workbook(root, selections, predictions, metrics, destination=None):
    """Write the workbook from the performance files under `root`. `selections` (the shortlist ledger) is checked
    for duplicate frozen picks; `predictions` is accepted for the review's call and not displayed."""
    root = Path(root)
    prepared_rows(selections)
    destination = Path(destination) if destination else root / 'readable' / REPORT_NAME
    return write_layout(root, destination, metrics or {})


def add_health_sheet(root, data, history=None):
    """The review's last step: rewrite the workbook with the final tracking, CLV and health figures."""
    root = Path(root)
    destination = root / 'readable' / REPORT_NAME
    if not destination.exists():
        return None
    metrics = _read_json(root / 'performance' / 'metrics.json')
    return write_layout(root, destination, metrics, data)


def _read_json(path):
    try:
        return json.loads(Path(path).read_text(encoding='utf-8')) if Path(path).exists() else {}
    except ValueError:
        return {}


def export_existing(root=Path('football_output_v2'), destination=None):
    root = Path(root)
    p = root / 'performance'
    required = [p / 'metrics.json', p / 'shortlist_grades.csv', p / 'prediction_grades.csv']
    if not all(x.exists() for x in required):
        return None

    def read(path):
        with path.open(encoding='utf-8-sig', newline='') as f:
            return list(dict_reader(f))
    return write_workbook(root, read(required[1]), read(required[2]), json.loads(required[0].read_text()),
                          destination)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path('football_output_v2'))
    args = parser.parse_args(argv)
    path = export_existing(args.root)
    if path is None:
        parser.error('Run performance_tracking.py review first to generate verified grades.')
    print(path)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
