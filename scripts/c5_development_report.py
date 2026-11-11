"""C5 (walk-forward home/away sharpening) versus C, C2 and C3: development primary, validation secondary.

Reads a locked harness run (`python evaluation_harness.py --output DIR`). Only the
development and validation rows are read; a holdout row anywhere aborts the report.
Validation was already inspected by earlier diagnostics, so it is secondary evidence.

Declared before the run (docs/plan.md, Phase 2):
  - primary: development, all eight leagues (C5 applies wherever C does); primary metric
    AH all lines; also AH draw-sensitive (0, +/-0.5), 1X2 and Over 1.5 log loss on the
    common cohort (C, C2, C3, C5, M, D, A all available), paired C - C5, C2 - C5 and C3 - C5
    with whole weeks resampled (evaluation_harness.paired);
  - secondary: validation (same metrics), and the five Understat leagues on development;
  - 1X2 calibration of C, C2, C3 and C5: logistic calibration slope per outcome (slope > 1:
    too flat), deciles, and strong favourites (the likelier of home and away at 0.6 or 0.7+);
  - the walk-forward slope path (one fit per 14-day fold) and how far C5 moves C's 1X2.

    python scripts/c5_development_report.py --run DIR --output evaluation/c5_sharpen
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
COHORT = ('C', 'C2', 'C3', 'C5', 'M', 'D', 'A')
RESEARCH = ('C', 'C2', 'C3', 'C5')
PHASES = ('development', 'validation')


def logistic_slope(p, y):
    """Calibration slope b of logit P(y) = a + b * logit(p), by Newton's method."""
    p = np.clip(np.asarray(p, float), 1e-6, 1 - 1e-6)
    x = np.column_stack([np.ones(len(p)), np.log(p / (1 - p))])
    w = np.zeros(2)
    for _ in range(50):
        q = 1 / (1 + np.exp(-x @ w))
        step = np.linalg.solve((x * (q * (1 - q))[:, None]).T @ x, x.T @ (np.asarray(y, float) - q))
        w += step
        if np.abs(step).max() < 1e-10:
            break
    return float(w[1])


def calibration(frame):
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
                'calibration_slope': logistic_slope(p, y),
                'deciles': [{'bin_lower': b / 10, 'n': int((bins == b).sum()), 'mean_forecast': float(p[bins == b].mean()),
                             'observed_rate': float(y[bins == b].mean()),
                             'observed_minus_forecast': float(y[bins == b].mean() - p[bins == b].mean())}
                            for b in sorted(bins.unique())]}
        fav_home = part.p_home >= part.p_away
        fav_p = np.where(fav_home, part.p_home, part.p_away)
        fav_won = np.where(fav_home, part.outcome == 0, part.outcome == 2)
        entry['favourite_deciles'] = []
        bins = np.minimum(9, (fav_p * 10).astype(int))
        for b in sorted(set(bins)):
            m = bins == b
            entry['favourite_deciles'].append({'bin_lower': b / 10, 'n': int(m.sum()), 'mean_forecast': float(fav_p[m].mean()),
                                               'observed_win_rate': float(fav_won[m].mean())})
        entry['strong_favourites'] = {}
        for low in (.6, .7):
            m = fav_p >= low
            entry['strong_favourites'][f'{low:.1f}+'] = {
                'n': int(m.sum()), 'mean_forecast': float(fav_p[m].mean()), 'observed_win_rate': float(fav_won[m].mean()),
                'observed_minus_forecast': float(fav_won[m].mean() - fav_p[m].mean())}
        out[cand] = entry
    return out


def compare(scores, leagues):
    import evaluation_harness as eh
    out = {}
    for group in GROUPS:
        part = scores.loc[(scores.group == group) & scores.league.isin(leagues)]
        table = part.pivot_table(index='fixture_key', columns='candidate', values='log_loss')
        keep = table[list(COHORT)].dropna().index
        part = part.loc[part.fixture_key.isin(keep)]
        means = part.groupby('candidate').log_loss.mean()
        out[group] = {'fixtures': int(len(keep)), 'mean_log_loss': {c: float(means[c]) for c in COHORT},
                      'C5_vs_C': eh.paired(part, 'C', 'C5'), 'C5_vs_C2': eh.paired(part, 'C2', 'C5'),
                      'C5_vs_C3': eh.paired(part, 'C3', 'C5'), 'C5_vs_M': eh.paired(part, 'M', 'C5')}
    return out


def movement(forecasts):
    wide = forecasts.pivot_table(index='fixture_key', columns='candidate', values=['p_home', 'p_draw', 'p_away'])
    moved = (wide.xs('C5', level=1, axis=1) - wide.xs('C', level=1, axis=1)).abs().max(axis=1).dropna()
    return {'fixtures': int(len(moved)), 'changed': int((moved > 1e-12).sum()),
            'mean_max_1x2_move_points': float(100 * moved.mean()),
            'p90_max_1x2_move_points': float(100 * moved.quantile(.9)), 'max_1x2_move_points': float(100 * moved.max())}


def main(argv=None):
    import understat_history as uh
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('--run', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args(argv)
    cfg = json.loads((REPO / 'evaluation_harness_config.json').read_text(encoding='utf-8'))
    results = json.loads((args.run / 'results.json').read_text(encoding='utf-8'))
    if results.get('mode') != 'historical':
        raise ValueError('Expected a locked historical run')
    scores = pd.read_csv(args.run / 'fixture_scores.csv')
    forecasts = pd.read_csv(args.run / 'forecasts_1x2.csv')
    if (scores.phase == 'holdout').any() or (forecasts.phase == 'holdout').any():
        raise ValueError('Holdout rows found; this report reads locked runs only')
    fits = next(f['walk_forward_fits'] for f in results['folds'] if f.get('candidate') == 'C5')
    report = {'source_commit': results['source_commit'], 'harness_version': results['version'],
              'walk_forward_slopes': [{k: f.get(k) for k in ('origin', 'status', 'matches', 'slope', 'scored_matches')}
                                      for f in fits]}
    for name in PHASES:
        s, f = scores.loc[scores.phase == name], forecasts.loc[forecasts.phase == name]
        common = set.intersection(*(set(f.loc[f.candidate == c, 'fixture_key']) for c in RESEARCH))
        five = f.loc[f.league.isin(uh.LEAGUES)]
        common_five = common & set(five.fixture_key)
        report[name] = {
            'all_eight_leagues': compare(s, cfg['leagues']),
            'five_understat_leagues': compare(s, list(uh.LEAGUES)),
            'c5_movement': movement(f),
            'calibration_1x2_all_eight': calibration(f.loc[f.fixture_key.isin(common)]),
            'calibration_1x2_five_leagues': calibration(five.loc[five.fixture_key.isin(common_five)])}
    report['notes'] = [
        'Development (1 Aug 2022 - 30 Jun 2025) is primary; validation (to 15 Jan 2026) is secondary and was '
        'already inspected by earlier diagnostics. No holdout or retrospective row is read.',
        'mean_gain > 0 means C5 has the lower log loss (C5_vs_C: C minus C5; C5_vs_M: M minus C5).',
        'Intervals resample whole calendar weeks (2,000 draws, seed 136, evaluation_harness.paired).',
        'Calibration slope > 1 means the forecasts are too flat (outcomes more extreme than forecast).',
        'Favourite: the side with the higher of the home and away probabilities.']
    args.output.mkdir(parents=True, exist_ok=True)
    (args.output / 'summary.json').write_text(json.dumps(report, indent=2, sort_keys=True) + '\n', encoding='utf-8',
                                              newline='\n')
    for name in PHASES:
        for subset in ('all_eight_leagues', 'five_understat_leagues'):
            for group, e in report[name][subset].items():
                for key in ('C5_vs_C', 'C5_vs_C2', 'C5_vs_C3', 'C5_vs_M'):
                    r = e[key]
                    print(name, subset, group, key, e['fixtures'], f"{r['mean_gain']:+.5f}",
                          [round(v, 5) for v in r['interval_95']], 'clear' if r['clear_of_zero'] else '')
        for cand, c in report[name]['calibration_1x2_all_eight'].items():
            print(name, 'slope', cand, *(f"{o}={c[o]['calibration_slope']:.3f}" for o in ('home', 'draw', 'away')),
                  *(f"fav{k}: {v['mean_forecast']:.3f}/{v['observed_win_rate']:.3f}" for k, v in c['strong_favourites'].items()))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
