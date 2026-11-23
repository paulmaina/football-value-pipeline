"""C6X (C6 plus rolling pre-kickoff xG) against C6, development first, then validation once (docs/plan.md, Phase 2i).

The research rows come from the harness's own folds (evaluation_harness.evaluate_league, keep C, C6 and M), with the
run end set in memory to RUN_END (1 Jul 2025, the end of the seasons the xG cache covers): no match on or after it is
forecast, fitted or read, so neither holdout, the harness validation period nor anything after 10 Oct 2026 is touched.
evaluation_harness.py and its config are not modified, so the setup fingerprint is unchanged. C6 is the harness's own
candidate (low_score_sharpen_candidate) on those rows; C6X is the same procedure on research_xg's adjusted rates.
Scored: the five leagues only; each fixture's period comes from SPLITS (the harness's own phase labels are not used).

    python scripts/extract_api_football_xg.py                 # first: the xG table (offline, no request)
    python scripts/c6_xg_report.py --period development       # writes evaluation/c6_xg/development.json
    python scripts/c6_xg_report.py --period validation        # then, once: validation.json and the choice rule

The harness rows are cached in data/feature_cache/c6_xg/ (git-ignored), keyed by the run config and the sha256 of the
harness and research files they depend on.
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
import historical_benchmark as hb  # noqa: E402
import research_backtest as rb  # noqa: E402
import research_xg as rx  # noqa: E402

OUT = REPO / 'evaluation' / 'c6_xg'
CACHE = REPO / 'data' / 'feature_cache' / 'c6_xg'
KEEP = frozenset({'C', 'C6', 'M'})
V3 = 'slopes-0.90-1.10-or-closer-than-baseline-bands-30-5pp-bonferroni-v3'
RUN_END = pd.Timestamp('2025-07-01')
# Registered in docs/plan.md Phase 2i before any C6X figure was computed.
SPLITS = {'run_in': ('2024-01-28', '2024-07-01'),
          'development': ('2024-07-01', '2025-01-01'),
          'validation': ('2025-01-01', '2025-07-01')}
PLACEBO_SEED = 2611


def phase_of(date):
    d = pd.Timestamp(date)
    for name, (start, stop) in SPLITS.items():
        if pd.Timestamp(start) <= d < pd.Timestamp(stop):
            return name
    return 'outside'


def run_config():
    cfg = json.loads(eh.CONFIG.read_text(encoding='utf-8'))
    if RUN_END > pd.Timestamp(cfg['development_end']):
        raise ValueError('C6X runs end inside the harness development period')
    return {**cfg, 'end_exclusive': RUN_END.date().isoformat()}, RUN_END


def harness_rows(cfg, workers=None):
    """(records, calib, research) for C, C6's inputs and M on every match before the run end."""
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
    if any(pd.Timestamp(r['date']) >= RUN_END for r in research):
        raise ValueError('A row on or after the run end reached the C6X run')
    CACHE.mkdir(parents=True, exist_ok=True)
    path.write_bytes(pickle.dumps((records, calib, research)))
    return records, calib, research


def teams_of(row):
    league, _, home, away = row['fixture_key'].split('|')
    return league, home, away


def league_matches():
    """Every completed league match of the five leagues in the xG seasons, from the files the harness trains on."""
    out = []
    for league in rx.LEAGUES:
        data, _, _ = hb.load_history(REPO / '.football_cache', league,
                                     {'seasons': ['2324', '2425'], 'test_end_exclusive': RUN_END.date().isoformat()})
        out += [(league, r.Date, r.HomeTeam, r.AwayTeam, int(r.FTHG), int(r.FTAG)) for r in data.itertuples(index=False)]
    return out


def placebo_xg(xg):
    """Leakage check, not part of the choice rule: each league-season's xG pairs shuffled across its matches."""
    rng = np.random.default_rng(PLACEBO_SEED)
    keys = sorted(xg)
    out = {}
    groups = {}
    for k in keys:
        season = pd.Timestamp(k[1]).year - (pd.Timestamp(k[1]).month < 7)
        groups.setdefault((k[0], season), []).append(k)
    for members in groups.values():
        values = [xg[k] for k in members]
        for k, j in zip(members, rng.permutation(len(members))):
            out[k] = values[j]
    return out


def row_features(research, index):
    feats, counts, coverage = [], [], Counter()
    for r in research:
        league, home, away = teams_of(r)
        f, k = rx.match_features(index, league, home, away, r['date'])
        feats.append(f); counts.append(k)
        if league in rx.LEAGUES:
            for side in k:
                coverage['side_k_0' if side == 0 else 'side_k_1_to_2' if side < rx.MIN_SIDE_MATCHES
                         else 'side_k_3_plus'] += 1
    return feats, counts, coverage


def c6x_candidate(research, feats, counts, cfg, end, name=rx.CANDIDATE):
    """C6X for every scored row: C6's procedure (eh.c6_walk_forward and the C6 grid) on the adjusted rates."""
    import research_low_score_sharpen as c6
    adjusted, fits = rx.walk_forward(research, feats, counts, eh.fold_windows(cfg, end))
    rows = [{**r, 'goal_rates': [float(v) for v in a]} for r, a in zip(research, adjusted)]
    rows, low, windows = eh.c6_walk_forward(rows, cfg, end)
    records, calib = [], []
    for window in windows:
        for i in window['scored']:
            r = rows[i]
            matrix = rb.matrix_value(c6.grid(r['goal_rates'], low[i], window['slope']))
            hg, ag = r['home_goals'], r['away_goals']
            records.extend(rb.score_fixture(r['identity'], {name: matrix}, hg, ag))
            h, a = np.indices(matrix.shape)
            calib.append({'phase': r['identity']['phase'], 'league': r['identity']['league'],
                          'fixture_key': r['identity']['fixture_key'], 'candidate': name,
                          'probs': [float(matrix[h > a].sum()), float(matrix[h == a].sum()), float(matrix[h < a].sum())],
                          'outcome': 0 if hg > ag else 1 if hg == ag else 2})
    return records, calib, fits


def leakage_checks(research, index, xg):
    """Counts that must all be zero, plus the input bounds."""
    late = sum(1 for k in xg if pd.Timestamp(k[1]) >= RUN_END)
    same_day = 0
    for r in research:
        league, home, away = teams_of(r)
        d = np.datetime64(pd.Timestamp(r['date']).date(), 'D')
        for team in (home, away):
            past = [x for x in index.get((league, team), []) if x[0] < d][-rx.WINDOW:]
            same_day += sum(x[0] >= d for x in past)
    return {'xg_rows_on_or_after_run_end': late, 'feature_matches_on_or_after_match_day': same_day,
            'research_rows_on_or_after_run_end': sum(pd.Timestamp(r['date']) >= RUN_END for r in research),
            'xg_first_date': min(k[1] for k in xg), 'xg_last_date': max(k[1] for k in xg),
            'ucl_rows_read': 0, 'odds_or_market_inputs_read_by_c6x': 0}


def summary(period, scores, calib, feats, counts, research, fits, cfg, placebo):
    s = scores.loc[(scores.phase == period) & scores.league.isin(rx.LEAGUES)]
    out = {'period': period, 'dates': SPLITS[period], 'groups': {}}
    for group in eh.GROUPS:
        g = s.loc[s.group == group]
        out['groups'][group] = {
            'C6_minus_C6X': eh.paired(g, 'C6', 'C6X'),
            'M_minus_C6X': eh.paired(g, 'M', 'C6X'),
            'M_minus_C6': eh.paired(g, 'M', 'C6'),
            'C6_minus_C6Xplacebo': eh.paired(g, 'C6', 'C6Xplacebo') if placebo else None,
            'mean_log_loss': {c: float(g.loc[g.candidate == c, 'log_loss'].mean())
                              for c in ('C', 'C6', 'C6X', 'C6Xplacebo', 'M') if (g.candidate == c).any()}}
    rules = eh.calibration_rules(cfg)
    rows = {c: [r for r in calib if r['phase'] == period and r['league'] in rx.LEAGUES and r['candidate'] == c]
            for c in ('C6', 'C6X')}
    out['calibration'] = {'C6X_v3_against_C6': eh.calibration_check(rows['C6X'], rules[V3], rows['C6']),
                          'C6_v2': eh.calibration_check(rows['C6'], rules[cfg['calibration_tolerance']['name']]),
                          'C6X_v2': eh.calibration_check(rows['C6X'], rules[cfg['calibration_tolerance']['name']])}
    c6 = {r['fixture_key']: r['probs'] for r in rows['C6']}
    moves = [max(abs(a - b) for a, b in zip(r['probs'], c6[r['fixture_key']])) for r in rows['C6X'] if r['fixture_key'] in c6]
    out['largest_1x2_move_from_C6'] = {'mean': float(np.mean(moves)) if moves else None,
                                       'p90': float(np.quantile(moves, .9)) if moves else None,
                                       'max': float(np.max(moves)) if moves else None}
    keep = [i for i, r in enumerate(research) if r['identity']['phase'] == period and teams_of(r)[0] in rx.LEAGUES]
    xs = np.array([[*feats[i][0], *feats[i][1]] for i in keep], float).reshape(-1, 4)
    ks = np.array([counts[i] for i in keep], float).reshape(-1, 2)
    out['features'] = {'fixtures': len(keep),
                       'both_sides_k_3_plus_share': float(np.mean(ks.min(axis=1) >= rx.MIN_SIDE_MATCHES)) if len(ks) else None,
                       'x_for_sd': float(np.std(xs[:, [0, 2]])) if len(xs) else None,
                       'x_against_sd': float(np.std(xs[:, [1, 3]])) if len(xs) else None}
    thin = {research[i]['fixture_key'] for i in keep if min(counts[i]) < rx.MIN_SIDE_MATCHES}
    out['segment_either_side_under_3_xg_matches'] = {
        group: eh.paired(s.loc[(s.group == group) & s.fixture_key.isin(thin)], 'C6', 'C6X') for group in ('AH all', '1X2')}
    period_fits = [x for x in fits if phase_of(x['origin']) == period]
    fitted = [x for x in period_fits if x['status'] == 'fitted']
    out['xg_fits'] = {'windows': len(period_fits), 'fitted': len(fitted),
                      'first': period_fits[0] if period_fits else None,
                      'last': period_fits[-1] if period_fits else None,
                      'median': {p: float(np.median([x[p] for x in fitted])) for p in rx.PARAMETERS} if fitted else None}
    return out


def choice_rule(dev, val):
    a = dev['groups']['AH all']['C6_minus_C6X']
    b = val['groups']['AH all']['C6_minus_C6X']
    c = dev['calibration']['C6X_v3_against_C6']['passes']
    conditions = {'a_development_ah_all_positive_and_clear': bool(a and a['mean_gain'] > 0 and a['clear_of_zero']),
                  'b_validation_ah_all_not_negative': bool(b and b['mean_gain'] >= 0),
                  'c_development_calibration_v3_against_c6': bool(c)}
    return {**conditions, 'put_forward_for_declaration': all(conditions.values())}


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument('--period', choices=('development', 'validation'), required=True)
    p.add_argument('--workers', type=int)
    args = p.parse_args(argv)
    if SPLITS is None:
        p.error('splits are registered in docs/plan.md Phase 2i first')
    if args.period == 'validation' and not (OUT / 'development.json').exists():
        p.error('development is written first')
    if (OUT / f'{args.period}.json').exists():
        p.error(f'{args.period} is computed once; {args.period}.json already exists')
    cfg, end = run_config()
    records, calib, research = harness_rows(cfg, args.workers)
    research = sorted(research, key=lambda r: r['date'])
    xg = rx.load_xg()
    matches = league_matches()
    index = rx.team_index(matches, xg)
    feats, counts, coverage = row_features(research, index)
    placebo_index = rx.team_index(matches, placebo_xg(xg))
    pfeats, pcounts, _ = row_features(research, placebo_index)
    r6, k6, _, _ = eh.low_score_sharpen_candidate(research, cfg, end, KEEP)
    r6x, k6x, fits = c6x_candidate(research, feats, counts, cfg, end)
    rpl, kpl, placebo_fits = c6x_candidate(research, pfeats, pcounts, cfg, end, name='C6Xplacebo')
    phases = {r['fixture_key']: phase_of(r['date']) for r in research}
    for r in research:
        r['identity'] = {**r['identity'], 'phase': phases[r['fixture_key']]}
    scores = eh.fixture_scores([*records, *r6, *r6x, *rpl])
    scores['phase'] = scores.fixture_key.map(phases)
    calib_all = [{**r, 'phase': phases.get(r['fixture_key'], 'outside')} for r in [*calib, *k6, *k6x, *kpl]]
    out = summary(args.period, scores, calib_all, feats, counts, research, fits, cfg, placebo=True)
    out['placebo_fits_median'] = {p: float(np.median([x[p] for x in placebo_fits if x['status'] == 'fitted']))
                                  for p in rx.PARAMETERS} if any(x['status'] == 'fitted' for x in placebo_fits) else None
    out.update(candidate=rx.CANDIDATE, version=rx.VERSION, run_end_exclusive=cfg['end_exclusive'],
               xg_coverage_of_sides=dict(coverage), window=rx.WINDOW, shrink=rx.SHRINK,
               min_side_matches=rx.MIN_SIDE_MATCHES, min_matches=rx.MIN_MATCHES, prior_sd=rx.PRIOR_SD,
               xg_table_sha256=hashlib.sha256(rx.XG_TABLE.read_bytes()).hexdigest(),
               leakage_checks=leakage_checks(research, index, xg))
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / f'{args.period}.json').write_text(json.dumps(out, indent=1, default=str) + '\n', encoding='utf-8', newline='\n')
    if args.period == 'validation':
        dev = json.loads((OUT / 'development.json').read_text(encoding='utf-8'))
        rule = choice_rule(dev, out)
        (OUT / 'choice_rule.json').write_text(json.dumps(rule, indent=1) + '\n', encoding='utf-8', newline='\n')
        print(json.dumps(rule, indent=1))
    print(json.dumps({g: v['C6_minus_C6X'] for g, v in out['groups'].items()}, indent=1))
    print(json.dumps({k: out['calibration']['C6X_v3_against_C6'][k] for k in ('slopes', 'passes')}, indent=1))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
