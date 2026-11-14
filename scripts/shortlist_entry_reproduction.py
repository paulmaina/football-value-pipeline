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


def predictions_of(directory):
    return pd.read_csv(directory / 'predictions.csv', low_memory=False)


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
    """Nominations only: fixtures in the run's kickoff window with a priced Pinnacle offer, and how many each list
    nominates. Not master coverage: see master_coverage."""
    from performance_tracking import fixture_key
    keys = decisions.apply(fixture_key, axis=1)
    window = ~decisions.rejection_reasons.fillna('').str.contains('kickoff outside')
    priced = window & decisions.offered_decimal_odds.notna()
    value = set(keys[decisions.decision.eq('SHORTLISTED')])
    cagey = set(keys[decisions.cagey_tier_decision.eq('SHORTLISTED')])
    return {'fixtures_in_window_priced': int(keys[priced].nunique()), 'fixtures_value': len(value),
            'fixtures_cagey': len(cagey), 'fixtures_either': len(value | cagey)}


# Proposed list changes (docs/shortlist-entry-audit.md, section 5), each alone and together: (value rules, cagey
# rules). Nominations are recomputed with shortlist_entry_audit's selection functions on the run's decision rows.
def proposals():
    import shortlist_entry_audit as sea
    dc12 = sea.EXCLUDED_TODAY - {'Double Chance 12'}
    return {'today': (sea.TODAY, sea.TODAY),
            'P1_floor_1_10': (sea.with_rules(min_odds=1.10), sea.with_rules(min_odds=1.10)),
            'P2_double_chance_12': (sea.with_rules(excluded=dc12), sea.with_rules(excluded=dc12)),
            'P3_cagey_ceiling_2_20': (sea.TODAY, sea.with_rules(max_odds=2.20)),
            'all_proposed': (sea.with_rules(min_odds=1.10, excluded=dc12),
                             sea.with_rules(min_odds=1.10, max_odds=2.20, excluded=dc12))}


# The master's execution window: today's, and moved to match the proposed list limits (shown, never proposed here).
MASTER_WINDOWS = {'master_today': None, 'master_odds_1_10_to_2_20': (1.10, 2.20)}


def renominate(decisions, value_rules, cagey_rules):
    """The run's decision rows with each list's nominations recomputed under the given rules (today's rules
    reproduce the live lists exactly; checked by `reproduce`)."""
    import shortlist_entry_audit as sea
    fixtures = sea.decision_offers(decisions)
    value = {o['index'] for offers in fixtures.values() for o, _ in sea.value_select(offers, value_rules)}
    cagey = {o['index'] for offers in fixtures.values() for o, _ in sea.cagey_select(offers, cagey_rules)}
    out = decisions.copy()
    out['decision'] = out['decision'].astype(object)
    out['cagey_tier_decision'] = out['cagey_tier_decision'].astype(object)
    was_value, was_cagey = out.decision.eq('SHORTLISTED'), out.cagey_tier_decision.eq('SHORTLISTED')
    out.loc[was_value, 'decision'] = 'NOT_SELECTED'
    out.loc[was_cagey, 'cagey_tier_decision'] = 'NOT_SELECTED'
    out.loc[sorted(value), 'decision'] = 'SHORTLISTED'
    out.loc[sorted(cagey), 'cagey_tier_decision'] = 'SHORTLISTED'
    return out


def master_coverage(decisions, predictions=None, generated_at_utc=None):
    """Nominations run through the new master's eligibility and selection (master_reconciliation.reconcile and
    summary: Pinnacle, native markets, the master's odds window, its market-view and quote-timing checks, the fill
    rule), for today's nominations and each proposed change, under today's master window and a moved one. The
    run's forecasts and generation clock are passed where the master times its references (as the live shadow
    does in master_shortlist.refresh)."""
    import copy
    import inspect
    import master_reconciliation as mr
    base = mr.load_config()
    accepts = inspect.signature(mr.reconcile).parameters
    timing = {k: v for k, v in (('predictions', predictions), ('generated_at_utc', generated_at_utc)) if k in accepts}
    out = {}
    for label, (value_rules, cagey_rules) in proposals().items():
        nominations = renominate(decisions, value_rules, cagey_rules)
        for window, limits in MASTER_WINDOWS.items():
            config = copy.deepcopy(base)
            if limits is not None:
                config['execution']['min_odds_exclusive'], config['execution']['max_odds_inclusive'] = limits
            frame = mr.reconcile(nominations, config=config, **timing)
            summary = mr.summary(frame, config=config)
            out[f'{label}|{window}'] = {
                'nominated_fixtures': summary['nominated_fixtures'],
                'eligible_fixtures': summary['fixtures_with_market_view'],
                'nominated_executable_fixtures': summary['nominated_executable_fixtures'],
                'ranked_fixtures': summary['ranked_fixtures'],
                'picks_by_tier': summary['picks_by_tier'],
                'fixtures_losing_every_offer_to_timing': (summary.get('timing_check') or {}).get(
                    'fixtures_losing_every_eligible_offer'),
                'master_times_quotes': 'predictions' in timing}
    return out


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
                               'decision_rows': int(len(decisions)), 'coverage': coverage(decisions),
                               'master': master_coverage(decisions, predictions_of(directory), generated),
                               **result})
        print(directory.name, generated, {k: (v['live'], v['harness'], v['same']) for k, v in result.items()})
    report['all_identical'] = all(r[k]['same'] for r in report['runs'] for k in ('value', 'cagey'))
    report['picks'] = {k: {'live': sum(r[k]['live'] for r in report['runs']),
                           'harness': sum(r[k]['harness'] for r in report['runs'])} for k in ('value', 'cagey')}
    report['live_rejection_reasons'] = {k: dict(v.most_common()) for k, v in totals.items()}
    cov = [r['coverage'] for r in report['runs']]
    report['coverage_totals'] = {k: sum(c[k] for c in cov) for k in cov[0]} if cov else {}
    report['runs_with_15_fixtures_covered'] = sum(c['fixtures_either'] >= 15 for c in cov)
    report['runs_with_15_fixtures_in_window'] = sum(c['fixtures_in_window_priced'] >= 15 for c in cov)
    # The new master over all runs: fixture-runs nominated, eligible (nominated, executable, with a market view) and
    # ranked, and runs whose master reaches 15, per proposal and master window.
    scenarios = list(report['runs'][0]['master']) if report['runs'] else []
    report['master_totals'] = {
        name: {'nominated_fixture_runs': sum(r['master'][name]['nominated_fixtures'] for r in report['runs']),
               'eligible_fixture_runs': sum(r['master'][name]['eligible_fixtures'] for r in report['runs']),
               'ranked_fixture_runs': sum(r['master'][name]['ranked_fixtures'] for r in report['runs']),
               'runs_reaching_15': sum(r['master'][name]['ranked_fixtures'] >= 15 for r in report['runs']),
               'fixture_runs_losing_every_offer_to_timing': sum(
                   r['master'][name]['fixtures_losing_every_offer_to_timing'] or 0 for r in report['runs'])}
        for name in scenarios}
    args.output.mkdir(parents=True, exist_ok=True)
    (args.output / 'reproduction.json').write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    print('all identical:', report['all_identical'], report['picks'])


if __name__ == '__main__':
    main()
