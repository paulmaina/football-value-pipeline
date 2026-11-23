"""C6R (C6 plus rest and congestion) against C6, development first, then validation once (docs/plan.md, Phase 2h).

The research rows come from the harness's own folds (evaluation_harness.evaluate_league, keep C, C6 and M), with the
run end set in memory to the validation end (holdout_start, 16 Jan 2026): no holdout match and no match played after
10 Oct 2026 is forecast, fitted or read. evaluation_harness.py and its config are not modified, so the setup
fingerprint is unchanged. C6 is the harness's own candidate (low_score_sharpen_candidate) on those rows; C6R is the
same procedure on research_rest's adjusted rates.

    python scripts/c6_rest_report.py --period development      # writes evaluation/c6_rest/development.json
    python scripts/c6_rest_report.py --period validation       # then, once: validation.json and the choice rule

The harness rows are cached in data/feature_cache/c6_rest/ (git-ignored), keyed by commit-independent inputs: the
harness config, the run end and the sha256 of the harness and research files the rows depend on.
"""
from __future__ import annotations

import argparse
from collections import Counter
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
import research_backtest as rb  # noqa: E402
import research_rest as rr  # noqa: E402

OUT = REPO / 'evaluation' / 'c6_rest'
CACHE = REPO / 'data' / 'feature_cache' / 'c6_rest'
KEEP = frozenset({'C', 'C6', 'M'})
V3 = 'slopes-0.90-1.10-or-closer-than-baseline-bands-30-5pp-bonferroni-v3'
LAST_ALLOWED = pd.Timestamp('2026-01-16')  # the validation end: nothing on or after it is read


def run_config():
    cfg = json.loads(eh.CONFIG.read_text(encoding='utf-8'))
    end = pd.Timestamp(cfg['holdout_start'])
    if end > LAST_ALLOWED:
        raise ValueError('C6R runs end at the validation end')
    return {**cfg, 'end_exclusive': end.date().isoformat()}, end


def harness_rows(cfg, workers=None):
    """(records, calib, research) for C, C6's inputs and M on every non-holdout match before the run end."""
    files = ['evaluation_harness.py', 'research_backtest.py', 'historical_benchmark.py', 'team_research.py',
             'research_low_score.py', 'research_low_score_sharpen.py', 'research_sharpen.py',
             'football_value_pipeline_v2_standalone.py']
    key = hashlib.sha256(json.dumps(cfg, sort_keys=True).encode()
                         + b''.join(hashlib.sha256((REPO / f).read_bytes()).digest() for f in files)).hexdigest()[:16]
    path = CACHE / f'harness_rows_{key}.pkl'
    if path.exists():
        return pickle.loads(path.read_bytes())
    records, calib, research = [], [], []
    with ProcessPoolExecutor(max_workers=workers) as pool:
        futures = [pool.submit(eh.evaluate_league, league, str(REPO / '.football_cache'), cfg, False, KEEP)
                   for league in cfg['leagues']]
        for future in futures:
            r, _, _, _, _, k, x = future.result()
            records += r; calib += k; research += x
    if any(r['phase'] == 'holdout' for r in records) or any(pd.Timestamp(r['date']) >= LAST_ALLOWED for r in research):
        raise ValueError('A row on or after the validation end reached the C6R run')
    CACHE.mkdir(parents=True, exist_ok=True)
    path.write_bytes(pickle.dumps((records, calib, research)))
    return records, calib, research


def teams_of(row):
    league, _, home, away = row['fixture_key'].split('|')
    return league, home, away


def row_features(research, index):
    feats, coverage = [], Counter()
    for r in research:
        league, home, away = teams_of(r)
        sides = [rr.match_features(index, league, t, r['date']) for t in (home, away)]
        for name, f in zip(('home', 'away'), sides):
            coverage['with_schedule' if f is not None else 'without_schedule'] += 1
        feats.append(tuple(np.zeros(3) if f is None else np.array(f) for f in sides))
    return feats, coverage


def c6r_candidate(research, feats, cfg, end):
    """C6R for every scored row: C6's procedure (eh.c6_walk_forward and the C6 grid) on the adjusted rates."""
    import research_low_score_sharpen as c6
    adjusted, rest_fits = rr.walk_forward(research, feats, eh.fold_windows(cfg, end))
    rows = [{**r, 'goal_rates': [float(v) for v in a]} for r, a in zip(research, adjusted)]
    rows, low, windows = eh.c6_walk_forward(rows, cfg, end)
    records, calib = [], []
    for window in windows:
        for i in window['scored']:
            r = rows[i]
            matrix = rb.matrix_value(c6.grid(r['goal_rates'], low[i], window['slope']))
            hg, ag = r['home_goals'], r['away_goals']
            records.extend(rb.score_fixture(r['identity'], {rr.CANDIDATE: matrix}, hg, ag))
            h, a = np.indices(matrix.shape)
            calib.append({'phase': r['identity']['phase'], 'league': r['identity']['league'],
                          'fixture_key': r['identity']['fixture_key'], 'candidate': rr.CANDIDATE,
                          'probs': [float(matrix[h > a].sum()), float(matrix[h == a].sum()), float(matrix[h < a].sum())],
                          'outcome': 0 if hg > ag else 1 if hg == ag else 2})
    return records, calib, rest_fits


def summary(period, scores, calib, feats, research, rest_fits, cfg):
    s = scores.loc[scores.phase == period]
    out = {'period': period, 'groups': {}}
    for group in eh.GROUPS:
        g = s.loc[s.group == group]
        out['groups'][group] = {
            'C6_minus_C6R': eh.paired(g, 'C6', 'C6R'),
            'M_minus_C6R': eh.paired(g, 'M', 'C6R'),
            'M_minus_C6': eh.paired(g, 'M', 'C6'),
            'mean_log_loss': {c: float(g.loc[g.candidate == c, 'log_loss'].mean()) for c in ('C', 'C6', 'C6R', 'M')
                              if (g.candidate == c).any()}}
    rules = eh.calibration_rules(cfg)
    rows = {c: [r for r in calib if r['phase'] == period and r['candidate'] == c] for c in ('C6', 'C6R', 'M')}
    out['calibration'] = {'C6R_v3_against_C6': eh.calibration_check(rows['C6R'], rules[V3], rows['C6']),
                          'C6_v2': eh.calibration_check(rows['C6'], rules[cfg['calibration_tolerance']['name']]),
                          'C6R_v2': eh.calibration_check(rows['C6R'], rules[cfg['calibration_tolerance']['name']])}
    c6 = {r['fixture_key']: r['probs'] for r in rows['C6']}
    moves = [max(abs(a - b) for a, b in zip(r['probs'], c6[r['fixture_key']])) for r in rows['C6R'] if r['fixture_key'] in c6]
    out['largest_1x2_move_from_C6'] = {'mean': float(np.mean(moves)) if moves else None,
                                       'max': float(np.max(moves)) if moves else None}
    phase = {r['fixture_key']: r['identity']['phase'] for r in research}
    keys = [r['fixture_key'] for r in research]
    f = [(k, fh, fa) for k, (fh, fa) in zip(keys, feats) if phase[k] == period]
    out['features'] = {'fixtures': len(f),
                       'short_rest_share_of_sides': float(np.mean([x[1][0] for x in f] + [x[2][0] for x in f])),
                       'european_away_last_share_of_sides': float(np.mean([x[1][2] for x in f] + [x[2][2] for x in f])),
                       'congestion_mean': float(np.mean([x[1][1] for x in f] + [x[2][1] for x in f]))}
    flagged = {k for k, fh, fa in f if fh[0] or fa[0] or fh[2] or fa[2]}
    seg = s.loc[s.fixture_key.isin(flagged)]
    out['segment_short_rest_or_european_away'] = {
        group: eh.paired(seg.loc[seg.group == group], 'C6', 'C6R') for group in ('AH all', '1X2')}
    period_fits = [x for x in rest_fits if eh.phase(pd.Timestamp(x['origin']), 'EPL', cfg) == period]
    out['rest_fits'] = {'windows': len(period_fits), 'fitted': sum(x['status'] == 'fitted' for x in period_fits),
                        'last': period_fits[-1] if period_fits else None,
                        'median': {p: float(np.median([x[p] for x in period_fits])) for p in rr.PARAMETERS} if period_fits else None}
    return out


def choice_rule(dev, val):
    a = dev['groups']['AH all']['C6_minus_C6R']
    b = val['groups']['AH all']['C6_minus_C6R']
    c = dev['calibration']['C6R_v3_against_C6']['passes']
    conditions = {'a_development_ah_all_positive_and_clear': bool(a and a['mean_gain'] > 0 and a['clear_of_zero']),
                  'b_validation_ah_all_not_negative': bool(b and b['mean_gain'] >= 0),
                  'c_development_calibration_v3_against_c6': bool(c)}
    return {**conditions, 'put_forward_for_declaration': all(conditions.values())}


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument('--period', choices=('development', 'validation'), required=True)
    p.add_argument('--workers', type=int)
    args = p.parse_args(argv)
    if args.period == 'validation' and not (OUT / 'development.json').exists():
        p.error('development is written first')
    if (OUT / f'{args.period}.json').exists():
        p.error(f'{args.period} is computed once; {args.period}.json already exists')
    cfg, end = run_config()
    records, calib, research = harness_rows(cfg, args.workers)
    research = sorted(research, key=lambda r: r['date'])
    index = rr.load_index()
    feats, coverage = row_features(research, index)
    r6, k6, _, _ = eh.low_score_sharpen_candidate(research, cfg, end, KEEP)
    r6r, k6r, rest_fits = c6r_candidate(research, feats, cfg, end)
    scores = eh.fixture_scores([*records, *r6, *r6r])
    out = summary(args.period, scores, [*calib, *k6, *k6r], feats, research, rest_fits, cfg)
    out.update(candidate=rr.CANDIDATE, version=rr.VERSION, run_end_exclusive=cfg['end_exclusive'],
               schedule_coverage_of_sides=dict(coverage), min_matches=rr.MIN_MATCHES, prior_sd=rr.PRIOR_SD)
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / f'{args.period}.json').write_text(json.dumps(out, indent=1, default=str) + '\n', encoding='utf-8')
    if args.period == 'validation':
        dev = json.loads((OUT / 'development.json').read_text(encoding='utf-8'))
        rule = choice_rule(dev, out)
        (OUT / 'choice_rule.json').write_text(json.dumps(rule, indent=1) + '\n', encoding='utf-8')
        print(json.dumps(rule, indent=1))
    print(json.dumps({g: v['C6_minus_C6R'] for g, v in out['groups'].items()}, indent=1))
    print(json.dumps({k: out['calibration']['C6R_v3_against_C6'][k] for k in ('slopes', 'passes')}, indent=1))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
