"""C7 (fitted rate calibration on C0's goal rates) and C8 (C7 plus Elo) beside C, C6 and C0.

Reads a locked harness run (`python evaluation_harness.py --output DIR`): development and validation, with
the retrospective period as a diagnostic. A holdout row anywhere aborts the report.

Declared before the run (the commit that added C7 and C8; docs/plan.md, Phase 2g):
  - the bar: C7 and C8 must beat C6 on AH all lines (primary). Removing the form term (C0) is the starting
    point, not the gain;
  - also AH draw-sensitive lines (0, +/-0.5), 1X2 and Over 1.5; baseline minus candidate log loss (positive:
    the candidate is better), whole calendar weeks resampled (evaluation_harness.paired, 95% intervals);
  - cohort: the standing diagnostics' common cohort (C, C2, C3, C5, C6, M, D, A, C0, DC) that also has C7
    and C8; the research views are also compared on every match both forecast (no price needed);
  - calibration rule v2 (slopes 0.90-1.10 and Bonferroni bands) on every forecast of each view in the
    period, and the relative slope rule (v3) for C7 and C8 against C6 and against C;
  - the standing diagnostics' fixed segments (gap to M) and per-league sharpness for C, C6, C0, C7, C8;
  - the information test p ~ M^a * R^b for the same views: passes only when b on development is positive
    with its interval clear of zero;
  - the walk-forward paths of (a_home, a_away, b, c) and (rho, delta), and how far C7 and C8 move 1X2.

    python scripts/c7_c8_report.py --run DIR --output evaluation/c7_c8_rate_calibration
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

import numpy as np
import pandas as pd

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO))
VERSION = 'c7-c8-report-v1'
NEW = ('C7', 'C8')
VIEWS = ('C', 'C6', 'C0', 'C7', 'C8')
BASELINES = ('C6', 'C', 'C0')
PAIRS = (*((base, cand) for cand in NEW for base in BASELINES), ('C7', 'C8'), ('C', 'C6'), ('C', 'C0'), ('C6', 'C0'),
         *(('M', view) for view in VIEWS))
RESEARCH_PAIRS = tuple(pair for pair in PAIRS if 'M' not in pair)
GROUPS = ('AH all', 'AH draw-sensitive', '1X2', 'Over 1.5')
PHASES = ('development', 'validation', 'retrospective')
EVIDENCE = ('development', 'validation')  # the retrospective period is a diagnostic only
V3 = 'slopes-0.90-1.10-or-closer-than-baseline-bands-30-5pp-bonferroni-v3'
FIT_FIELDS = ('a_home', 'a_away', 'b', 'c')


def compare(scores, keys, pairs=PAIRS) -> dict:
    """Mean log loss and baseline-minus-candidate differences on `keys`, per group."""
    import evaluation_harness as eh
    out = {}
    for group in GROUPS:
        part = scores.loc[(scores.group == group) & scores.fixture_key.isin(keys)]
        means = part.groupby('candidate').log_loss.mean()
        out[group] = {'fixtures': int(part.fixture_key.nunique()),
                      'mean_log_loss': {c: float(means[c]) for c in (*VIEWS, 'M') if c in means},
                      'baseline_minus_candidate': {f'{base}_minus_{cand}': eh.paired(part, base, cand)
                                                   for base, cand in pairs}}
    return out


def every_forecast(scores, phase) -> dict:
    """The research views on every match both forecast in the period (no market price needed)."""
    import evaluation_harness as eh
    out = {}
    for group in GROUPS:
        part = scores.loc[(scores.group == group) & (scores.phase == phase)]
        out[group] = {f'{base}_minus_{cand}': eh.paired(part, base, cand) for base, cand in RESEARCH_PAIRS}
    return out


def rows_of(forecasts, candidate) -> list:
    part = forecasts.loc[forecasts.candidate == candidate]
    return [{'fixture_key': k, 'probs': [h, d, a], 'outcome': int(o)} for k, h, d, a, o in
            part[['fixture_key', 'p_home', 'p_draw', 'p_away', 'outcome']].itertuples(index=False)]


def calibration(forecasts, cfg) -> dict:
    """Per view: levels and slopes, rule v2 on every forecast in the period, and for C7 and C8 the relative
    slope rule (v3) against C6 and against C."""
    import evaluation_harness as eh
    v2, v3 = cfg['calibration_tolerance'], cfg['calibration_tolerance_rules']['rules'][V3]
    rows = {view: rows_of(forecasts, view) for view in (*VIEWS, 'M')}
    out = {}
    for view, mine in rows.items():
        if not mine:
            continue
        probs, outcome = np.array([r['probs'] for r in mine]), np.array([r['outcome'] for r in mine])
        entry = {'forecasts': len(mine),
                 'levels': {name: {'mean_forecast': float(probs[:, k].mean()),
                                   'observed_rate': float((outcome == k).mean()),
                                   'calibration_slope': eh.calibration_slope(probs[:, k], outcome == k)}
                            for k, name in enumerate(('home', 'draw', 'away'))},
                 'v2': eh.calibration_check(mine, v2)}
        if view in NEW:
            entry['v3'] = {'against_' + base: eh.calibration_check(mine, v3, rows[base]) for base in ('C6', 'C')}
        out[view] = entry
    return out


def movement(forecasts, candidate, base) -> dict:
    wide = forecasts.loc[forecasts.candidate.isin([candidate, base])].pivot(
        index='fixture_key', columns='candidate', values=['p_home', 'p_draw', 'p_away'])
    moved = (wide.xs(candidate, level=1, axis=1) - wide.xs(base, level=1, axis=1)).abs().max(axis=1).dropna()
    return {'versus': base, 'fixtures': int(len(moved)), 'changed': int((moved > 1e-12).sum()),
            'mean_max_1x2_move_points': float(100 * moved.mean()),
            'p90_max_1x2_move_points': float(100 * moved.quantile(.9)), 'max_1x2_move_points': float(100 * moved.max())}


def walk_forward(results) -> dict:
    fits = {f['candidate']: f['walk_forward_fits'] for f in results['folds'] if f.get('candidate')}
    out = {}
    for name in NEW:
        path = [{'origin': f['origin'], 'status': f['status'], 'matches': f['matches'],
                 **{k: f[k] for k in FIT_FIELDS}, 'rho': f['low_score']['rho'], 'delta': f['low_score']['delta'],
                 'low_score_status': f['low_score']['status'], 'scored_matches': f['scored_matches']}
                for f in fits[name]]
        fitted = [f for f in path if f['status'] == 'fitted']
        span = lambda key, rows: ({'min': float(min(r[key] for r in rows)), 'max': float(max(r[key] for r in rows)),
                                   'median': float(np.median([r[key] for r in rows])), 'last': float(rows[-1][key])}
                                  if rows else None)
        low = [f for f in path if f['low_score_status'] == 'fitted']
        out[name] = {'windows': len(path), 'warm_up_windows': sum(f['status'] == 'warm_up' for f in path),
                     'failed_windows': sum(f['status'] == 'optimiser_failed' for f in path),
                     'first_fitted_origin': fitted[0]['origin'] if fitted else None,
                     'ranges': {**{k: span(k, fitted) for k in FIT_FIELDS},
                                **{k: span(k, low) for k in ('rho', 'delta')}},
                     'path': path}
    return out


def build(run, cfg) -> dict:
    import evaluation_diagnostics as ed
    results = json.loads((run / 'results.json').read_text(encoding='utf-8'))
    if results.get('mode') != 'historical':
        raise ValueError('Expected a locked historical run')
    scores = pd.read_csv(run / 'fixture_scores.csv')
    forecasts = pd.read_csv(run / 'forecasts_1x2.csv')
    fixtures = pd.read_csv(run / 'diagnostic_fixtures.csv')
    for frame in (scores, forecasts, fixtures):
        if (frame.phase == 'holdout').any():
            raise ValueError('Holdout rows found; this report reads locked runs only')
    standing = ed.cohort(scores)
    members = ed.cohort(scores, (*ed.COHORT, *NEW))
    coverage = results['coverage']
    report = {
        'version': VERSION, 'source_commit': results['source_commit'], 'harness_version': results['version'],
        'config_sha256': results['config_sha256'],
        'declared': {'bar': 'C7 and C8 must beat C6 on AH all lines', 'primary_metric': 'AH all',
                     'differences': 'X_minus_Y is baseline X minus candidate Y log loss: positive means Y is better',
                     'cohort': 'fixtures where ' + ', '.join((*ed.COHORT, *NEW)) + ' all have a score',
                     'intervals': 'whole calendar weeks resampled, 95% (evaluation_harness.paired)',
                     'evidence': list(EVIDENCE), 'diagnostic_only': ['retrospective']},
        'cohort': {phase: int((members.phase == phase).sum()) for phase in PHASES},
        'standing_diagnostics_cohort': {phase: int((standing.phase == phase).sum()) for phase in PHASES},
        'cohort_equals_standing_diagnostics': bool(members.index.equals(standing.index)),
        'unavailable': {name: {k: v for k, v in sorted(coverage.items())
                               if f':{name}:' in k and not k.endswith(':available')} for name in NEW},
        'walk_forward': walk_forward(results),
        'information_test': ed.information_test(forecasts, members, VIEWS),
    }
    segments = ed.segments(scores, forecasts, fixtures, members, VIEWS)
    for phase in PHASES:
        keys = members.index[members.phase == phase]
        inside = forecasts.loc[forecasts.phase == phase]
        report[phase] = {'log_loss': compare(scores, keys),
                         'research_views_every_forecast': every_forecast(scores, phase),
                         'calibration': calibration(inside, cfg),
                         'movement': {name: [movement(inside, name, base) for base in ('C0', 'C6', 'C')]
                                      for name in NEW},
                         'segments': segments.get(phase)}
    return report


def _pair(entry, key, spec='+.5f') -> str:
    result = entry.get(key)
    if not result:
        return 'n/a'
    low, high = result['interval_95'] or (float('nan'), float('nan'))
    return (f"{result['mean_gain']:{spec}} ({low:{spec}} to {high:{spec}})"
            + (' **clear**' if result['clear_of_zero'] else ' *worse, clear*' if high < 0 else ''))


def markdown(report) -> str:
    import evaluation_diagnostics as ed
    table, ci, f = ed._table, ed._ci, ed._f
    lines = ['# C7 and C8: fitted rate calibration on the Dixon-Coles goal rates, and Elo', '',
             f"Locked run at commit `{report['source_commit']}` ({report['version']}). Offline only: no live "
             'probability changes. No holdout row is read. The retrospective period is a diagnostic, never '
             'release evidence.', '',
             'The bar, stated before the run: **C7 and C8 must beat C6 on AH all lines.** Differences are '
             'baseline minus candidate log loss (positive: the candidate is better), 95% intervals, whole '
             'calendar weeks resampled.', '',
             'Cohort (' + report['declared']['cohort'] + '): '
             + ', '.join(f'{phase} {n:,}' for phase, n in report['cohort'].items())
             + ('; the same fixtures as the standing diagnostics.' if report['cohort_equals_standing_diagnostics']
                else '; NOT the standing diagnostics\' cohort.'), '']
    lines += ['## Walk-forward fits', '']
    rows = []
    for name, e in report['walk_forward'].items():
        for key, r in e['ranges'].items():
            if r is not None and not (name == 'C7' and key == 'c'):
                rows.append([name, key, f(r['min'], '+.3f'), f(r['median'], '+.3f'), f(r['max'], '+.3f'),
                             f(r['last'], '+.3f')])
        lines += [f"{name}: {e['windows']} windows with scored matches, {e['warm_up_windows']} neutral (warm-up), "
                  f"{e['failed_windows']} failed; first fitted window {e['first_fitted_origin']}.", '']
    lines += table(['Candidate', 'Parameter', 'Min', 'Median', 'Max', 'Last window'], rows)
    for phase in PHASES:
        e = report[phase]
        label = phase.capitalize() + (' (diagnostic only)' if phase not in EVIDENCE else '')
        lines += [f"## {label}: {report['cohort'][phase]:,} fixtures", '', '### Log loss', '']
        lines += table(['Metric', *VIEWS, 'M'],
                       [[g, *(f(e['log_loss'][g]['mean_log_loss'].get(c), '.5f') for c in (*VIEWS, 'M'))]
                        for g in GROUPS])
        for cand in NEW:
            lines += [f'### {cand} against each baseline', '']
            lines += table(['Metric', *(f'{base} minus {cand}' for base in BASELINES)],
                           [[g, *(_pair(e['log_loss'][g]['baseline_minus_candidate'], f'{base}_minus_{cand}')
                                  for base in BASELINES)] for g in GROUPS])
        lines += ['### C8 against C7, and the earlier views', '']
        lines += table(['Metric', 'C7 minus C8', 'C minus C6', 'C minus C0', 'C6 minus C0'],
                       [[g, *(_pair(e['log_loss'][g]['baseline_minus_candidate'], k)
                              for k in ('C7_minus_C8', 'C_minus_C6', 'C_minus_C0', 'C6_minus_C0'))] for g in GROUPS])
        lines += ['### Every match both views forecast (no price needed)', '']
        lines += table(['Metric', 'Fixtures', 'C6 minus C7', 'C6 minus C8', 'C0 minus C7', 'C7 minus C8'],
                       [[g, f"{(e['research_views_every_forecast'][g]['C6_minus_C7'] or {}).get('fixtures', 0):,}",
                         *(_pair(e['research_views_every_forecast'][g], k)
                           for k in ('C6_minus_C7', 'C6_minus_C8', 'C0_minus_C7', 'C7_minus_C8'))] for g in GROUPS])
        lines += ['### Calibration (every forecast of the view in the period)', '']
        rows = []
        for view, c in e['calibration'].items():
            lev, v2 = c['levels'], c['v2']
            relative = '; '.join(f"vs {k.split('_')[1]} {'pass' if v['passes'] else 'fail'}"
                                 for k, v in c.get('v3', {}).items()) or 'n/a'
            worst = v2['worst_band']
            rows.append([view, f"{c['forecasts']:,}",
                         ' / '.join(f(lev[o]['calibration_slope'], '.3f') for o in ('home', 'draw', 'away')),
                         f"{lev['draw']['mean_forecast']:.1%} / {lev['draw']['observed_rate']:.1%}",
                         ('pass' if v2['passes'] else 'fail') + f" ({len(v2['failing_bands'])} bands fail)",
                         relative,
                         'n/a' if not worst else
                         f"{worst['outcome']} {worst['band_lower']:.1f}: {worst['mean_forecast']:.1%} / "
                         f"{worst['observed_rate']:.1%} (n {worst['n']}, z {worst['z']:.2f}, bar {v2['band_z_threshold']:.2f})"])
        lines += table(['View', 'Forecasts', 'Slopes home / draw / away', 'Draw forecast / observed', 'Rule v2',
                        'Relative slope rule (v3)', 'Worst band'], rows)
        lines += ['### How far the candidates move 1X2', '']
        lines += table(['Candidate', 'Versus', 'Fixtures', 'Changed', 'Mean largest move', '90th percentile', 'Max'],
                       [[name, m['versus'], f"{m['fixtures']:,}", f"{m['changed']:,}",
                         f"{m['mean_max_1x2_move_points']:.1f}", f"{m['p90_max_1x2_move_points']:.1f}",
                         f"{m['max_1x2_move_points']:.1f}"] for name, moves in e['movement'].items() for m in moves])
        seg = e['segments']
        if seg:
            for group in ed.SEGMENT_GROUPS:
                rows = [['all', 'all', f"{seg['all']['fixtures']:,}", *(ci(seg['all']['gap_to_M'][c][group]) for c in VIEWS)]]
                for dimension in ('training matches', 'month', 'favourite market probability', 'league'):
                    for r in seg[dimension]:
                        rows.append([dimension, r['segment'], f"{r['fixtures']:,}",
                                     *(ci(r['gap_to_M'][c][group]) if r['gap_to_M'] else 'n/a' for c in VIEWS)])
                lines += [f'### Segments, gap to M on {group} (view minus M: positive is behind the market)', '']
                lines += table(['Dimension', 'Segment', 'Fixtures', *VIEWS], rows)
            lines += ['### Sharpness by league (t minimising the 1X2 log loss of p^t: above 1 too flat)', '']
            lines += table(['League', 'Fixtures', *VIEWS, 'M'],
                           [[r['segment'], f"{r['fixtures']:,}", *(f(r['sharpness'][c], '.2f') for c in (*VIEWS, 'M'))]
                            for r in seg['league']])
    lines += ['## Information test: p ~ M^a x R^b', '',
              'Research passes only when b on development is positive with its interval clear of zero.', '']
    rows = []
    for name, e in report['information_test'].items():
        for period, r in e['by_period'].items():
            rows.append([name, period, f"{r['fixtures']:,}", ci({'mean': r['a'], 'interval_95': r['a_interval_95']}, '.3f'),
                         ci({'mean': r['b'], 'interval_95': r['b_interval_95']}, '+.3f'),
                         'yes' if r['b_positive_and_clear_of_zero'] else 'no'])
    lines += table(['R', 'Period (fitted on it)', 'Fixtures', 'a', 'b', 'b positive and clear'], rows)
    lines += ['Verdict (development): ' + '; '.join(f"{name} {'passes' if e['passes'] else 'does not pass'}"
                                                    for name, e in report['information_test'].items()) + '.', '']
    return '\n'.join(lines)


def main(argv=None) -> int:
    import evaluation_diagnostics as ed
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('--run', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args(argv)
    cfg = json.loads((REPO / 'evaluation_harness_config.json').read_text(encoding='utf-8'))
    report = build(args.run, cfg)
    args.output.mkdir(parents=True, exist_ok=True)
    ed.write_json(args.output / 'summary.json', report)
    (args.output / 'report.md').write_text(markdown(report), encoding='utf-8', newline='\n')
    for phase in PHASES:
        for group in ('AH all', '1X2'):
            entry = report[phase]['log_loss'][group]
            print(phase, group, entry['fixtures'], {c: round(v, 5) for c, v in entry['mean_log_loss'].items()})
            for key in ('C6_minus_C7', 'C6_minus_C8', 'C7_minus_C8'):
                print('   ', key, _pair(entry['baseline_minus_candidate'], key))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
