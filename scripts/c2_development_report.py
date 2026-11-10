"""C2 versus C on the development period (validation as a secondary check), from a harness run.

Reads the output of `python evaluation_harness.py --output DIR` (a locked run: no
holdout match is scored or used). Reports, per period:

  - mean log loss on the common cohort (fixtures where C, C2, M, D and A are all
    available) and C2 - C paired on that cohort, whole calendar weeks resampled
    (95% interval), for AH all lines, AH draw-sensitive (0, +/-0.5), 1X2 and Over 1.5;
  - the same pairing on folds where C2's walk-forward fit had passed its warm-up
    (descriptive only: before it C2 equals C by construction);
  - 1X2 calibration of C and C2: mean forecast against observed rate per outcome, and
    the worst decile deviation among bins with at least 30 forecasts.

Retrospective rows in the harness output are not reported.

    python scripts/c2_development_report.py --run DIR --output evaluation/c2_draw_low_score/summary.json
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

import pandas as pd

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO))
PERIODS = ('development', 'validation')
GROUPS = ('AH all', 'AH draw-sensitive', '1X2', 'Over 1.5')
COHORT = ('C', 'C2', 'M', 'D', 'A')


def cohort_scores(scores, phase, group):
    part = scores.loc[(scores.phase == phase) & (scores.group == group)]
    table = part.pivot_table(index='fixture_key', columns='candidate', values='log_loss')
    keep = table[list(COHORT)].dropna().index
    return part.loc[part.fixture_key.isin(keep)]


def calibration(results, phase):
    import evaluation_harness as eh
    out = {}
    for cand in ('C', 'C2'):
        rows = [b for b in results['calibration_1x2'] if b['phase'] == phase and b['candidate'] == cand]
        entry = {}
        for outcome in ('home', 'draw', 'away'):
            bins = [b for b in rows if b['outcome'] == outcome]
            n = sum(b['n'] for b in bins)
            entry[outcome] = {'forecasts': n,
                              'mean_forecast': sum(b['n'] * b['mean_forecast'] for b in bins) / n,
                              'observed_rate': sum(b['n'] * b['observed_rate'] for b in bins) / n}
        big = [b for b in rows if b['n'] >= eh.CALIBRATION_MIN_BIN]
        worst = max(big, key=lambda b: abs(b['observed_rate'] - b['mean_forecast']))
        entry['worst_bin'] = {k: worst[k] for k in ('outcome', 'bin_lower', 'n', 'mean_forecast', 'observed_rate')}
        entry['worst_bin']['abs_deviation'] = abs(worst['observed_rate'] - worst['mean_forecast'])
        out[cand] = entry
    return out


def main(argv=None):
    import evaluation_harness as eh
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('--run', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args(argv)
    results = json.loads((args.run / 'results.json').read_text(encoding='utf-8'))
    if results.get('mode') != 'historical' or any(f.get('phase') == 'holdout' for f in results.get('folds', [])):
        raise ValueError('Expected a locked historical run')
    scores = pd.read_csv(args.run / 'fixture_scores.csv')
    if (scores.phase == 'holdout').any():
        raise ValueError('Holdout scores found; this report reads locked runs only')
    fits = next(f['walk_forward_fits'] for f in results['folds'] if f.get('candidate') == 'C2')
    fitted_from = min(pd.Timestamp(f['origin']) for f in fits if f['status'] == 'fitted')
    report = {'source_commit': results['source_commit'], 'harness_version': results['version'],
              'c2_fits': {'windows': len(fits), 'warm_up_windows': sum(f['status'] == 'warm_up' for f in fits),
                          'first_fitted_origin': fitted_from.date().isoformat(),
                          'rho_range': [min(f['rho'] for f in fits if f['status'] == 'fitted'),
                                        max(f['rho'] for f in fits if f['status'] == 'fitted')],
                          'delta_range': [min(f['delta'] for f in fits if f['status'] == 'fitted'),
                                          max(f['delta'] for f in fits if f['status'] == 'fitted')],
                          'by_window': fits},
              'periods': {}}
    for phase in PERIODS:
        entry = {}
        for group in GROUPS:
            part = cohort_scores(scores, phase, group)
            means = part.groupby('candidate').log_loss.mean()
            fitted = part.loc[pd.to_datetime(part.fixture_key.str.split('|').str[1]) >= fitted_from]
            entry[group] = {'fixtures': int(part.fixture_key.nunique()),
                            'mean_log_loss': {c: float(means[c]) for c in COHORT},
                            'C2_vs_C': eh.paired(part, 'C', 'C2'),
                            'C2_vs_C_after_warm_up (descriptive)': eh.paired(fitted, 'C', 'C2'),
                            'C2_vs_M': eh.paired(part, 'M', 'C2')}
        report['periods'][phase] = {'groups': entry, 'calibration_1x2': calibration(results, phase)}
    report['notes'] = ['mean_gain > 0 means C2 has the lower log loss (C2_vs_C: C minus C2).',
                       'Intervals resample whole calendar weeks (2,000 draws, seed 136, evaluation_harness.paired).',
                       'Common cohort: fixtures where C, C2, M, D and A are all available.',
                       'No holdout match is scored or used for fitting in a locked run.']
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    for phase in PERIODS:
        for group, e in report['periods'][phase]['groups'].items():
            r = e['C2_vs_C']
            print(phase, group, e['fixtures'], round(r['mean_gain'], 5), [round(v, 5) for v in r['interval_95']],
                  'after warm-up', round(e['C2_vs_C_after_warm_up (descriptive)']['mean_gain'], 5),
                  [round(v, 5) for v in e['C2_vs_C_after_warm_up (descriptive)']['interval_95']])
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
