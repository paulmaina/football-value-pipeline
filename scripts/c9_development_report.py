"""C9 (C8 plus the development walk-forward slope) on development only (docs/plan.md, Phase 2g-4).

The research rows come from the harness's own folds (evaluation_harness.evaluate_league, keep C6, C8, C9 and M),
with the run end set in memory to the development end (1 Jul 2025): no validation, holdout or later match is
forecast, fitted or read. C6, C8 and C9 are the harness's own candidates on those rows. Information for the
declaration only: C9 is declared against C6 as decided (Paul, 17 Nov 2026), whatever these numbers say.

    python scripts/c9_development_report.py      # writes evaluation/c9_walk_forward_slope/development.json

The harness rows are cached in data/feature_cache/c9_walk_forward_slope/ (git-ignored), keyed by the run config
and the sha256 of the files the rows depend on.
"""
from __future__ import annotations

import argparse
from concurrent.futures import ProcessPoolExecutor
import hashlib
import json
from pathlib import Path
import pickle
import sys

import numpy as np
import pandas as pd

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO))

import evaluation_harness as eh  # noqa: E402

OUT = REPO / 'evaluation' / 'c9_walk_forward_slope'
CACHE = REPO / 'data' / 'feature_cache' / 'c9_walk_forward_slope'
KEEP = frozenset({'C6', 'C8', 'C9', 'M'})
V3 = 'slopes-0.90-1.10-or-closer-than-baseline-bands-30-5pp-bonferroni-v3'
FILES = ('evaluation_harness.py', 'research_backtest.py', 'historical_benchmark.py', 'team_research.py',
         'research_low_score.py', 'research_low_score_sharpen.py', 'research_sharpen.py',
         'research_rate_calibration.py', 'elo_ratings.py', 'football_value_pipeline_v2_standalone.py')


def run_config():
    """The harness config with the run end at the development end: nothing on or after 1 Jul 2025 is read."""
    cfg = json.loads(eh.CONFIG.read_text(encoding='utf-8'))
    return {**cfg, 'end_exclusive': cfg['development_end']}, pd.Timestamp(cfg['development_end'])


def harness_rows(cfg, end, workers=None):
    """(records, calib, research) for C6's and C8's inputs and M on every development match."""
    key = hashlib.sha256(json.dumps(cfg, sort_keys=True).encode()
                         + b''.join(hashlib.sha256((REPO / f).read_bytes()).digest() for f in FILES)).hexdigest()[:16]
    path = CACHE / f'harness_rows_{key}.pkl'
    if path.exists():
        return pickle.loads(path.read_bytes())
    records, calib, research = [], [], []
    with ProcessPoolExecutor(max_workers=workers) as pool:
        futures = [pool.submit(eh.evaluate_league, league, str(REPO / '.football_cache'), cfg, False, set(KEEP))
                   for league in cfg['leagues']]
        for future in futures:
            r, _, _, _, _, k, x = future.result()
            records += r; calib += k; research += x
    if any(r['phase'] != 'development' for r in records) or any(pd.Timestamp(r['date']) >= end for r in research):
        raise ValueError('A row on or after the development end reached the C9 development run')
    CACHE.mkdir(parents=True, exist_ok=True)
    path.write_bytes(pickle.dumps((records, calib, research)))
    return records, calib, research


def development_slope(research, cfg, end):
    """The slope C9 applies from the first fold after development: the fit at the development end on every
    development forecast (the fold [1 Jul 2025, 15 Jul 2025) holds no row here, so it is fitted with every_window)."""
    _, _, windows = eh.rate_calibration_slope_walk_forward(research, cfg, end + pd.Timedelta(days=cfg['step_days']),
                                                           every_window=True)
    window = next(w for w in windows if w['origin'] == end)
    return window['slope']


def summary(scores, calib, fits, cfg):
    out = {'period': 'development', 'groups': {}}
    for group in eh.GROUPS:
        g = scores.loc[scores.group == group]
        out['groups'][group] = {
            'C6_minus_C9': eh.paired(g, 'C6', 'C9'), 'C8_minus_C9': eh.paired(g, 'C8', 'C9'),
            'C6_minus_C8': eh.paired(g, 'C6', 'C8'), 'M_minus_C9': eh.paired(g, 'M', 'C9'),
            'mean_log_loss': {c: float(g.loc[g.candidate == c, 'log_loss'].mean()) for c in ('C6', 'C8', 'C9', 'M')
                              if (g.candidate == c).any()}}
    rules = eh.calibration_rules(cfg)
    rows = {c: [r for r in calib if r['candidate'] == c] for c in ('C6', 'C8', 'C9', 'M')}
    v2 = rules[cfg['calibration_tolerance']['name']]
    out['calibration'] = {'C9_v3_against_C6': eh.calibration_check(rows['C9'], rules[V3], rows['C6']),
                          'C8_v3_against_C6': eh.calibration_check(rows['C8'], rules[V3], rows['C6']),
                          **{f'{c}_v2': eh.calibration_check(rows[c], v2) for c in ('C6', 'C8', 'C9', 'M')}}
    c8 = {r['fixture_key']: r['probs'] for r in rows['C8']}
    moves = [max(abs(a - b) for a, b in zip(r['probs'], c8[r['fixture_key']])) for r in rows['C9']
             if r['fixture_key'] in c8]
    out['largest_1x2_move_from_C8'] = {'mean': float(np.mean(moves)), 'max': float(np.max(moves))} if moves else None
    fitted = [f for f in fits if f['status'] == 'fitted']
    out['slope_fits'] = {'windows': len(fits), 'fitted': len(fitted),
                         'first_fitted_origin': fitted[0]['origin'] if fitted else None,
                         'range': [min(f['slope'] for f in fitted), max(f['slope'] for f in fitted)] if fitted else None,
                         'last': fits[-1] if fits else None}
    return out


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument('--workers', type=int)
    args = p.parse_args(argv)
    cfg, end = run_config()
    records, calib, research = harness_rows(cfg, end, args.workers)
    research = sorted(research, key=lambda r: r['date'])
    r6, k6, _, _ = eh.low_score_sharpen_candidate(research, cfg, end, KEEP)
    r8, k8, _, _ = eh.rate_calibration_candidate(research, cfg, end, 'C8', KEEP)
    r9, k9, _, fits = eh.rate_calibration_slope_candidate(research, cfg, end, KEEP)
    scores = eh.fixture_scores([*records, *r6, *r8, *r9], cfg['draw_sensitive_lines'])
    out = summary(scores, [*calib, *k6, *k8, *k9], fits, cfg)
    out.update(candidate='C9', candidate_definition=eh.CANDIDATES['C9'], run_end_exclusive=cfg['end_exclusive'],
               slope_applied_after_development=development_slope(research, cfg, end),
               research_rows=len(research), last_research_row=max(r['date'] for r in research).date().isoformat())
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / 'development.json').write_text(json.dumps(out, indent=1, default=str) + '\n', encoding='utf-8')
    print(json.dumps({g: {k: v[k] for k in ('C6_minus_C9', 'C8_minus_C9')} for g, v in out['groups'].items()},
                     indent=1, default=str))
    print(json.dumps({k: out['calibration']['C9_v3_against_C6'].get(k) for k in ('slopes', 'passes')}, indent=1,
                     default=str))
    print(json.dumps(out['slope_applied_after_development'], indent=1))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
