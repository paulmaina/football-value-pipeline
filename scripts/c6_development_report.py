"""C6 (C2's draw correction, then C5's sharpening) versus C, C2 and C5: development primary, validation secondary.

Reads a locked harness run (`python evaluation_harness.py --output DIR`). Only the
development and validation rows are read; a holdout row anywhere aborts the report.
Validation was already inspected by earlier diagnostics, so it is secondary evidence.

Declared before the run (docs/plan.md, Phase 2f):
  - primary: development, all eight leagues, on the common cohort (C, C2, C3, C5, C6, M, D, A
    all available); primary metric AH all lines, also AH draw-sensitive (0, +/-0.5), 1X2 and
    Over 1.5 log loss; paired C - C6, C2 - C6 and C5 - C6 with whole weeks resampled
    (evaluation_harness.paired, 95% intervals);
  - 1X2 calibration of C, C2, C3, C5 and C6: logistic calibration slopes, draw level (mean
    forecast against observed), favourite deciles and strong favourites (0.6+ and 0.7+);
  - the calibration tolerance decided on 11 Nov 2026 (evaluation_harness_config.json,
    `calibration_tolerance`; evaluation_harness.calibration_check): pass or fail for C, C2, C3,
    C5 and C6 on development and on validation;
  - secondary: validation (same metrics);
  - context only, NOT declared: development after C6's warm-up (fixtures from the first fold
    whose slope is fitted), labelled `undeclared_after_warm_up`;
  - the walk-forward paths (C6's slope and the C2 parameters under it, next to C5's slope) and
    how far C6 moves C2's and C's 1X2.

    python scripts/c6_development_report.py --run DIR --output evaluation/c6_low_score_sharpen
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
GROUPS = ('AH all', 'AH draw-sensitive', '1X2', 'Over 1.5')
COHORT = ('C', 'C2', 'C3', 'C5', 'C6', 'M', 'D', 'A')
RESEARCH = ('C', 'C2', 'C3', 'C5', 'C6')
PAIRS = (('C', 'C6'), ('C2', 'C6'), ('C5', 'C6'), ('C', 'C5'), ('C', 'C2'), ('M', 'C6'))
PHASES = ('development', 'validation')


def calibration(frame):
    """Slopes, draw level, deciles and favourites per research candidate."""
    import evaluation_harness as eh
    out = {}
    for cand in RESEARCH:
        part = frame.loc[frame.candidate == cand]
        if part.empty:
            continue
        entry = {}
        for k, outcome in enumerate(('home', 'draw', 'away')):
            p, y = part['p_' + outcome], (part.outcome == k).astype(int)
            bins = np.minimum(9, (p * 10).astype(int))
            entry[outcome] = {
                'forecasts': len(part), 'mean_forecast': float(p.mean()), 'observed_rate': float(y.mean()),
                'calibration_slope': eh.calibration_slope(p, y),
                'deciles': [{'bin_lower': b / 10, 'n': int((bins == b).sum()), 'mean_forecast': float(p[bins == b].mean()),
                             'observed_rate': float(y[bins == b].mean()),
                             'observed_minus_forecast': float(y[bins == b].mean() - p[bins == b].mean())}
                            for b in sorted(bins.unique())]}
        fav_home = part.p_home >= part.p_away
        fav_p = np.where(fav_home, part.p_home, part.p_away)
        fav_won = np.where(fav_home, part.outcome == 0, part.outcome == 2)
        bins = np.minimum(9, (fav_p * 10).astype(int))
        entry['favourite_deciles'] = [{'bin_lower': b / 10, 'n': int((bins == b).sum()),
                                       'mean_forecast': float(fav_p[bins == b].mean()),
                                       'observed_win_rate': float(fav_won[bins == b].mean())} for b in sorted(set(bins))]
        entry['strong_favourites'] = {}
        for low in (.6, .7):
            m = fav_p >= low
            entry['strong_favourites'][f'{low:.1f}+'] = {
                'n': int(m.sum()), 'mean_forecast': float(fav_p[m].mean()), 'observed_win_rate': float(fav_won[m].mean()),
                'observed_minus_forecast': float(fav_won[m].mean() - fav_p[m].mean())}
        out[cand] = entry
    return out


def tolerance(frame, rule):
    """The configured calibration tolerance for each research candidate (all its forecasts in the period)."""
    import evaluation_harness as eh
    out = {}
    for cand in RESEARCH:
        part = frame.loc[frame.candidate == cand]
        rows = [{'probs': [h, d, a], 'outcome': int(o)}
                for h, d, a, o in part[['p_home', 'p_draw', 'p_away', 'outcome']].itertuples(index=False)]
        out[cand] = eh.calibration_check(rows, rule)
    return out


def compare(scores, keep=None):
    import evaluation_harness as eh
    out = {}
    for group in GROUPS:
        part = scores.loc[scores.group == group]
        table = part.pivot_table(index='fixture_key', columns='candidate', values='log_loss')
        common = table[list(COHORT)].dropna().index
        if keep is not None:
            common = common.intersection(keep)
        part = part.loc[part.fixture_key.isin(common)]
        means = part.groupby('candidate').log_loss.mean()
        out[group] = {'fixtures': int(len(common)), 'mean_log_loss': {c: float(means[c]) for c in COHORT},
                      **{f'{cand}_vs_{base}': eh.paired(part, base, cand) for base, cand in PAIRS}}
    return out


def movement(forecasts, base):
    wide = forecasts.pivot_table(index='fixture_key', columns='candidate', values=['p_home', 'p_draw', 'p_away'])
    moved = (wide.xs('C6', level=1, axis=1) - wide.xs(base, level=1, axis=1)).abs().max(axis=1).dropna()
    return {'versus': base, 'fixtures': int(len(moved)), 'changed': int((moved > 1e-12).sum()),
            'mean_max_1x2_move_points': float(100 * moved.mean()),
            'p90_max_1x2_move_points': float(100 * moved.quantile(.9)), 'max_1x2_move_points': float(100 * moved.max())}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('--run', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args(argv)
    cfg = json.loads((REPO / 'evaluation_harness_config.json').read_text(encoding='utf-8'))
    rule = cfg['calibration_tolerance']
    results = json.loads((args.run / 'results.json').read_text(encoding='utf-8'))
    if results.get('mode') != 'historical':
        raise ValueError('Expected a locked historical run')
    if results['config'].get('calibration_tolerance') != rule:
        raise ValueError('The run used a different calibration tolerance from the config')
    scores = pd.read_csv(args.run / 'fixture_scores.csv')
    forecasts = pd.read_csv(args.run / 'forecasts_1x2.csv')
    if (scores.phase == 'holdout').any() or (forecasts.phase == 'holdout').any():
        raise ValueError('Holdout rows found; this report reads locked runs only')
    fits = {f['candidate']: f['walk_forward_fits'] for f in results['folds'] if f.get('candidate')}
    c5_slope = {f['origin']: f.get('slope') for f in fits['C5']}
    first_fitted = min(f['origin'] for f in fits['C6'] if f['status'] == 'fitted')
    report = {'source_commit': results['source_commit'], 'harness_version': results['version'],
              'calibration_tolerance': rule,
              'first_fitted_c6_fold': first_fitted,
              'walk_forward': [{'origin': f['origin'], 'status': f['status'], 'matches': f['matches'],
                                'slope': f.get('slope'), 'c5_slope': c5_slope.get(f['origin']),
                                'rho': f['low_score'].get('rho'), 'delta': f['low_score'].get('delta'),
                                'low_score_status': f['low_score'].get('status'), 'scored_matches': f['scored_matches']}
                               for f in fits['C6']]}
    for name in PHASES:
        s, f = scores.loc[scores.phase == name], forecasts.loc[forecasts.phase == name]
        common = set.intersection(*(set(f.loc[f.candidate == c, 'fixture_key']) for c in RESEARCH))
        report[name] = {
            'all_eight_leagues': compare(s),
            'c6_movement': [movement(f, 'C2'), movement(f, 'C')],
            'calibration_1x2_all_eight': calibration(f.loc[f.fixture_key.isin(common)]),
            'calibration_tolerance': tolerance(f, rule)}
        harness = results['calibration_tolerance_check'][name]
        for cand, check in report[name]['calibration_tolerance'].items():
            # forecasts_1x2.csv rounds the floats, so slopes agree to about 1e-12, not bit for bit.
            same_bands = [(b['outcome'], b['band_lower'], b['n']) for b in check['failing_bands']] == \
                [(b['outcome'], b['band_lower'], b['n']) for b in harness[cand]['failing_bands']]
            same_slopes = all(abs(check['slopes'][k] - harness[cand]['slopes'][k]) < 1e-9 for k in check['slopes'])
            if check['passes'] != harness[cand]['passes'] or not same_bands or not same_slopes:
                raise ValueError(f'Calibration check for {cand} disagrees with the harness run')
    dev = scores.loc[scores.phase == 'development']
    dates = pd.to_datetime(dev.fixture_key.str.split('|').str[1])
    after = pd.Index(dev.loc[dates >= pd.Timestamp(first_fitted), 'fixture_key'].unique())
    report['undeclared_after_warm_up'] = {
        'label': 'NOT DECLARED: context only, never release evidence',
        'from': first_fitted, 'development': compare(dev, keep=after)}
    report['notes'] = [
        'Development (1 Aug 2022 - 30 Jun 2025) is primary; validation (to 15 Jan 2026) is secondary and was '
        'already inspected by earlier diagnostics. No holdout or retrospective row is read.',
        'mean_gain > 0 means the first-named candidate (C6 in X_vs_Y) has the lower log loss: Y minus X.',
        'Intervals resample whole calendar weeks (2,000 draws, seed 136, evaluation_harness.paired).',
        'Calibration slope > 1 means the forecasts are too flat (outcomes more extreme than forecast).',
        'Calibration tolerance: evaluation_harness.calibration_check with the configured rule, on every forecast '
        'of the candidate in the period; it matches results.json calibration_tolerance_check.',
        'Favourite: the side with the higher of the home and away probabilities.']
    args.output.mkdir(parents=True, exist_ok=True)
    (args.output / 'summary.json').write_text(json.dumps(report, indent=2, sort_keys=True) + '\n', encoding='utf-8',
                                              newline='\n')
    sections = [(name, report[name]['all_eight_leagues']) for name in PHASES]
    sections.append(('after-warm-up (undeclared)', report['undeclared_after_warm_up']['development']))
    for name, comparison in sections:
        for group, e in comparison.items():
            for base, cand in PAIRS:
                r = e[f'{cand}_vs_{base}']
                print(name, group, f'{base}-{cand}', e['fixtures'], f"{r['mean_gain']:+.5f}",
                      [round(v, 5) for v in r['interval_95']], 'clear' if r['clear_of_zero'] else '')
    for name in PHASES:
        for cand, c in report[name]['calibration_1x2_all_eight'].items():
            print(name, cand, *(f"{o}: slope {c[o]['calibration_slope']:.3f} fc {c[o]['mean_forecast']:.4f} "
                                f"obs {c[o]['observed_rate']:.4f}" for o in ('home', 'draw', 'away')),
                  *(f"fav{k}: {v['mean_forecast']:.3f}/{v['observed_win_rate']:.3f} n={v['n']}"
                    for k, v in c['strong_favourites'].items()))
        for cand, t in report[name]['calibration_tolerance'].items():
            w = t['worst_band']
            print(name, 'tolerance', cand, 'PASS' if t['passes'] else 'FAIL',
                  {k: round(v, 3) for k, v in t['slopes'].items()},
                  f"worst {w['outcome']} {w['band_lower']:.1f}+ n={w['n']} {100 * w['observed_minus_forecast']:+.1f} pts",
                  f"failing bands {len(t['failing_bands'])}")
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
