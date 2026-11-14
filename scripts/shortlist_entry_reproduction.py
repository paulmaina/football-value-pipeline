"""Reproduction check for the shortlist entry audit: the harness's selection functions on saved live runs.

For every archived run generated in [--start, --end) (football_output_v2/performance/snapshots), rebuild the run's
decision rows from its frozen predictions at its own clock under today's production rules
(price_edge_cagey_shortlist.build_shortlist with cagey_correction_config.json and the quote policy, as the master
replays do), then apply shortlist_entry_audit.value_select and cagey_select to those rows. The live rejection
reasons are used only for the rules the selection functions can't express (kickoff window, quote freshness and
timing, synchronisation, bookmaker, Europa eligibility). Writes <output>/reproduction.json. No result is read.

    python scripts/shortlist_entry_reproduction.py --output evaluation/shortlist_entry_audit
"""
from __future__ import annotations

import argparse
import collections
import json
import sys
import warnings
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
SNAPSHOTS = ROOT / 'football_output_v2' / 'performance' / 'snapshots'


def runs(start='2026-10-27', end='2026-11-09'):
    out = []
    for directory in sorted(SNAPSHOTS.iterdir()):
        try:
            summary = json.loads((directory / 'selection_summary.json').read_text(encoding='utf-8'))
        except (OSError, ValueError):
            continue
        generated = str(summary.get('generated_at_utc') or '')
        if start <= generated[:10] < end and (directory / 'predictions.csv').exists():
            out.append((generated, directory))
    return sorted(out)


def rebuild(directory, generated):
    import narrow_margin as nm
    import price_edge_cagey_shortlist as v28
    from quote_policy import load_policy
    predictions = pd.read_csv(directory / 'predictions.csv', low_memory=False)
    with warnings.catch_warnings():
        warnings.simplefilter('ignore')
        _, decisions, _ = v28.build_shortlist(predictions, pd.Timestamp(generated), execution_policy=load_policy(),
                                              model=nm.production_model())
    return decisions


def reasons(decisions):
    """How often each live rejection reason occurs (context: which rules bind live)."""
    count = lambda column: collections.Counter(r for text in decisions[column].dropna()
                                               for r in str(text).split('; ') if r)
    return {'value': count('rejection_reasons'), 'cagey': count('cagey_tier_reasons')}


def coverage(decisions):
    """Context: fixtures in the run's kickoff window with a priced Pinnacle offer, and how many each list covers."""
    from performance_tracking import fixture_key
    keys = decisions.apply(fixture_key, axis=1)
    window = ~decisions.rejection_reasons.fillna('').str.contains('kickoff outside')
    priced = window & decisions.offered_decimal_odds.notna()
    value = set(keys[decisions.decision.eq('SHORTLISTED')])
    cagey = set(keys[decisions.cagey_tier_decision.eq('SHORTLISTED')])
    return {'fixtures_in_window_priced': int(keys[priced].nunique()), 'fixtures_value': len(value),
            'fixtures_cagey': len(cagey), 'fixtures_either': len(value | cagey)}


def main(argv=None):
    import shortlist_entry_audit as sea
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--start', default='2026-10-27')
    parser.add_argument('--end', default='2026-11-09')
    args = parser.parse_args(argv)
    report = {'start': args.start, 'end_exclusive': args.end, 'runs': [],
              'expressed_value_reasons': list(sea.VALUE_EXPRESSED),
              'expressed_cagey_reasons': list(sea.CAGEY_EXPRESSED)}
    totals = {'value': collections.Counter(), 'cagey': collections.Counter()}
    for generated, directory in runs(args.start, args.end):
        decisions = rebuild(directory, generated)
        result = sea.reproduce(decisions)
        for name, counter in reasons(decisions).items():
            totals[name].update(counter)
        report['runs'].append({'snapshot': directory.name, 'generated_at_utc': generated,
                               'decision_rows': int(len(decisions)), 'coverage': coverage(decisions), **result})
        print(directory.name, generated, {k: (v['live'], v['harness'], v['same']) for k, v in result.items()})
    report['all_identical'] = all(r[k]['same'] for r in report['runs'] for k in ('value', 'cagey'))
    report['picks'] = {k: {'live': sum(r[k]['live'] for r in report['runs']),
                           'harness': sum(r[k]['harness'] for r in report['runs'])} for k in ('value', 'cagey')}
    report['live_rejection_reasons'] = {k: dict(v.most_common()) for k, v in totals.items()}
    cov = [r['coverage'] for r in report['runs']]
    report['coverage_totals'] = {k: sum(c[k] for c in cov) for k in cov[0]} if cov else {}
    report['runs_with_15_fixtures_covered'] = sum(c['fixtures_either'] >= 15 for c in cov)
    report['runs_with_15_fixtures_in_window'] = sum(c['fixtures_in_window_priced'] >= 15 for c in cov)
    args.output.mkdir(parents=True, exist_ok=True)
    (args.output / 'reproduction.json').write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    print('all identical:', report['all_identical'], report['picks'])


if __name__ == '__main__':
    main()
