"""Corner-total candidate K1 vs the league average (B0) and count-markets-nb2-v1 (NB2), plus inputs on top of K1.

Offline, accuracy only. Development (1 Aug 2022 - 30 Jun 2025) and validation (1 Jul 2025 - 15 Jan 2026), all
eight domestic leagues, Over/Under 8.5-11.5. Nothing after 15 Jan 2026 is read (research_corners.CUTOFF).

1. K1's half-life and shrinkage are chosen on development only (mean Over log loss); the other settings'
   validation forecasts are discarded unscored.
2. K1, B0 and NB2 are compared on the fixtures all three forecast.
3. Each input group is tested on top of K1 through a pooled walk-forward NB2 second stage (log mu = log mu_K1 +
   b0 + b.x), against the same second stage with an intercept only on the same fixtures. Home advantage is
   tested as K1 with and without its home term. An input is kept if development improves with the 95% interval
   clear of zero and validation does not get worse (mean difference <= 0). Market inputs (Pinnacle 1X2, O/U 2.5)
   are a separate, labelled market-informed variant and never part of the odds-free view.

No historical corner prices exist for these periods, so returns are not tested.

    python scripts/corners_candidate_report.py --output evaluation/corners_candidate --work <scratch dir>
"""
from __future__ import annotations

import argparse
import itertools
import json
import os
import pickle
import sys
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

for _v in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ.setdefault(_v, '1')

import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import research_corners as rc  # noqa: E402

KEY = ['league', 'date', 'home_team', 'away_team']
MAIN = ('B0', 'NB2', 'K1', 'K1r')
LL = [f'll_{l}' for l in rc.MAIN_LINES]


# ---------------------------------------------------------------------------
# Phase A: walk-forward forecasts and inputs (parallel, cached)
# ---------------------------------------------------------------------------

def _keyed(frame, league):
    frame = frame.copy()
    frame['league'] = league
    frame['date'] = pd.to_datetime(frame['date']).dt.normalize()
    return frame


def task(spec):
    kind, league = spec[0], spec[1]
    cache = Path(spec[-1])
    division = rc.DIVISIONS[league]
    if kind == 'k1':
        _, _, half_life, prior, home, _ = spec
        m = rc.matches(rc.load_league(cache, division))
        return _keyed(rc.walk_forward_k1(m, rc.STAGE2_START, rc.CUTOFF, half_life, prior, home), league)
    if kind == 'b0':
        m = rc.matches(rc.load_league(cache, division))
        return _keyed(rc.walk_forward_b0(m, rc.PERIODS['development'][0], rc.CUTOFF), league)
    if kind == 'nb2':
        import count_markets as cm
        raw = cm.walk_forward(rc.load_league(cache, division), 'corners')
        raw = raw.loc[(raw.date >= rc.PERIODS['development'][0]) & (raw.date <= rc.CUTOFF)]
        return _keyed(raw[['date', 'home_team', 'away_team', 'total', 'mu', 'alpha']], league)
    history = rc.load_league(cache, division, columns=rc.INPUT_COLUMNS)
    if kind == 'inputs':
        frame = history.assign(date=pd.to_datetime(history.Date, format='%d/%m/%Y'))
        frame = frame.sort_values('date', kind='stable')
        shots = rc.shot_form(frame)
        elo = rc.elo_differences(history)
        market = rc.market_probabilities(history)
        out = pd.concat([frame[['date', 'HomeTeam', 'AwayTeam']], shots], axis=1)
        out['elo_diff'] = elo.elo_diff.reindex(frame.index)
        out[['p_home', 'p_away', 'p_over25']] = market[['p_home', 'p_away', 'p_over25']].reindex(frame.index)
        out = out.rename(columns={'HomeTeam': 'home_team', 'AwayTeam': 'away_team'})
        return _keyed(out.loc[out.date >= rc.STAGE2_START], league)
    if kind == 'dc':
        _, _, origins, _ = spec
        cfg = json.loads((ROOT / 'evaluation_harness_config.json').read_text(encoding='utf-8'))
        out = rc.dc_expected_goals(history, origins, cfg)
        return _keyed(out.rename(columns={'HomeTeam': 'home_team', 'AwayTeam': 'away_team'}), league)
    raise ValueError(kind)


def specs(cache):
    cache = str(cache)
    origins = list(pd.date_range(rc.STAGE2_START, rc.CUTOFF + pd.Timedelta(days=rc.DC_STEP_DAYS + 1),
                                 freq=f'{rc.DC_STEP_DAYS}D'))
    chunks = np.array_split(np.arange(len(origins) - 1), 6)
    result = []
    for league in rc.DIVISIONS:
        for c in chunks:
            result.append(('dc', league, tuple(origins[c[0]:c[-1] + 2]), cache))
    for league in rc.DIVISIONS:
        for half_life, prior in itertools.product(rc.GRID_HALF_LIFE_DAYS, rc.GRID_PRIOR_MATCHES):
            for home in (True, False):
                result.append(('k1', league, half_life, prior, home, cache))
        result += [('b0', league, cache), ('nb2', league, cache), ('inputs', league, cache)]
    return result


def phase_a(cache, work, workers):
    path = Path(work) / 'phase_a.pkl'
    if path.exists():
        return pickle.loads(path.read_bytes())
    todo = specs(cache)
    with ProcessPoolExecutor(max_workers=workers) as pool:
        results = list(pool.map(task, todo))
    store = {}
    for spec, frame in zip(todo, results):
        name = spec[0] if spec[0] != 'k1' else ('k1', spec[2], spec[3], spec[4])
        store.setdefault(name, []).append(frame)
    store = {k: pd.concat(v, ignore_index=True) for k, v in store.items()}
    path.write_bytes(pickle.dumps(store))
    return store


# ---------------------------------------------------------------------------
# Phase B: choose K1, second stage, scoring
# ---------------------------------------------------------------------------

def _period(date):
    for name, (start, end) in rc.PERIODS.items():
        if start <= date <= end:
            return name
    return None


def _prepare(frame):
    frame = rc.score(frame.loc[(frame.date >= rc.PERIODS['development'][0]) & (frame.date <= rc.CUTOFF)])
    frame['period'] = frame.date.map(_period)
    frame['week'] = frame.date.map(lambda d: f'{d.isocalendar().year}-W{d.isocalendar().week:02d}')
    frame['avg_ll'] = frame[LL].mean(axis=1)
    return frame


def choose_k1(store):
    grid = []
    dev_start, dev_end = rc.PERIODS['development']
    for half_life, prior in itertools.product(rc.GRID_HALF_LIFE_DAYS, rc.GRID_PRIOR_MATCHES):
        f = store[('k1', half_life, prior, True)]
        dev = rc.score(f.loc[(f.date >= dev_start) & (f.date <= dev_end)])  # development only
        grid.append({'half_life_days': half_life, 'prior_matches': prior, 'fixtures': int(len(dev)),
                     'mean_over_log_loss': float(dev[LL].mean(axis=1).mean()),
                     'count_log_loss': float(dev.count_log_loss.mean())})
    best = min(grid, key=lambda g: g['mean_over_log_loss'])
    return grid, (best['half_life_days'], best['prior_matches'])


def stage_rows(store, chosen):
    k1 = store[('k1', *chosen, True)][KEY + ['total', 'mu']].rename(columns={'mu': 'mu_k1'})
    nh = store[('k1', *chosen, False)][KEY + ['mu']].rename(columns={'mu': 'mu_k1_no_home'})
    rows = k1.merge(nh, on=KEY, how='left')
    rows = rows.merge(store['inputs'], on=KEY, how='left').merge(store['dc'], on=KEY, how='left')
    return rc.input_columns(rows)


def second_stage(rows, columns, base='mu_k1', require=()):
    data = rows.dropna(subset=list(require)) if require else rows
    return rc.walk_forward_stage2(data, columns, rc.PERIODS['development'][0], rc.CUTOFF, base=base)


def paired(a, b):
    """a minus b on fixtures both forecast, per period: mean Over log loss and count log loss, week intervals."""
    from evaluation_diagnostics import week_mean
    m = a.merge(b, on=KEY, suffixes=('_a', '_b'))
    out = {}
    for period in rc.PERIODS:
        p = m.loc[m.period_a == period]
        out[period] = {'fixtures': int(len(p)),
                       'mean_over_log_loss': week_mean(p.avg_ll_a - p.avg_ll_b, p.week_a),
                       'count_log_loss': week_mean(p.count_log_loss_a - p.count_log_loss_b, p.week_a),
                       'lines': {str(l): week_mean(p[f'll_{l}_a'] - p[f'll_{l}_b'], p.week_a)['mean']
                                 for l in rc.MAIN_LINES}}
    return out


def keep(diff):
    dev, val = diff['development']['mean_over_log_loss'], diff['validation']['mean_over_log_loss']
    return bool(dev['interval_95'] and dev['interval_95'][1] < 0 and val['mean'] is not None and val['mean'] <= 0)


def summarise(frames, keys):
    """Accuracy and calibration of each model on a common set of fixtures."""
    from evaluation_diagnostics import week_mean
    out = {'fixtures': int(len(keys)), 'models': {}}
    for name, f in frames.items():
        w = keys.merge(f, on=KEY)
        entry = {'mean_over_log_loss': float(w.avg_ll.mean()), 'count_log_loss': float(w.count_log_loss.mean()),
                 'mean_over_log_loss_interval': week_mean(w.avg_ll, w.week)['interval_95'],
                 'mean_mu': float(w.mu.mean()), 'sd_mu': float(w.mu.std()), 'lines': {}}
        for line in rc.MAIN_LINES:
            y = (w.total > line).astype(float)
            p = w[f'p_over_{line}']
            entry['lines'][str(line)] = {'log_loss': float(w[f'll_{line}'].mean()),
                                         'mean_forecast': float(p.mean()), 'observed_rate': float(y.mean()),
                                         **rc.logistic_calibration(p, y), 'bands': rc.band_check(p, y)}
        out['models'][name] = entry
    return out


def phase_b(store):
    grid, chosen = choose_k1(store)
    rows = stage_rows(store, chosen)
    forecasts = {'B0': _prepare(store['b0']), 'NB2': _prepare(store['nb2']),
                 'K1': _prepare(store[('k1', *chosen, True)]), 'K1r': _prepare(second_stage(rows, []))}
    tests, kept = {}, []
    for group, cols in rc.INPUT_GROUPS.items():
        variant = _prepare(second_stage(rows, cols))
        base = _prepare(second_stage(rows, [], require=cols))
        diff = paired(variant, base)
        tests[group] = {'columns': cols, 'view': 'odds-free', 'difference_vs_K1r': diff, 'kept': keep(diff)}
        if tests[group]['kept']:
            kept.append(group)
    home = paired(forecasts['K1r'], _prepare(second_stage(rows, [], base='mu_k1_no_home')))
    tests['home_advantage'] = {'columns': ['K1 home term'], 'view': 'odds-free',
                               'difference_vs_K1r': home, 'kept': keep(home),
                               'note': 'K1r with its home term minus the same model with one intercept for both sides'}
    market = {}
    for group, cols in rc.MARKET_GROUPS.items():
        variant = _prepare(second_stage(rows, cols))
        base = _prepare(second_stage(rows, [], require=cols))
        diff = paired(variant, base)
        market[group] = {'columns': cols, 'view': 'market-informed', 'difference_vs_K1r': diff, 'kept': keep(diff)}
    combined = {}
    kept_cols = [c for g in kept for c in rc.INPUT_GROUPS[g]]
    if kept_cols:
        forecasts['K2'] = _prepare(second_stage(rows, kept_cols))
        combined['K2'] = {'inputs': kept, 'note': 'kept odds-free inputs together; validation was used by the keep rule'}
    kept_market = [g for g, t in market.items() if t['kept']]
    if kept_market:
        best_market = max(kept_market, key=lambda g: len(rc.MARKET_GROUPS[g]))
        forecasts['K2m'] = _prepare(second_stage(rows, kept_cols + rc.MARKET_GROUPS[best_market]))
        combined['K2m'] = {'inputs': kept + [best_market],
                           'note': 'market-informed: uses Pinnacle prices; never part of the odds-free view'}
    names = [n for n in ('B0', 'NB2', 'K1', 'K1r', 'K2') if n in forecasts]
    common = None
    for n in names:
        k = forecasts[n][KEY + ['period']]
        common = k if common is None else common.merge(k[KEY], on=KEY)
    res = {'version': rc.VERSION, 'cutoff': rc.CUTOFF.date().isoformat(),
           'periods': {k: [v[0].date().isoformat(), v[1].date().isoformat()] for k, v in rc.PERIODS.items()},
           'lines': list(rc.MAIN_LINES), 'interval': 'whole calendar weeks resampled, 2000 draws, seed 136',
           'returns': 'not tested: no historical corner prices in development or validation',
           'keep_rule': 'development difference with 95% interval below zero and validation mean difference <= 0',
           'k1_grid_development': grid, 'k1_chosen': {'half_life_days': chosen[0], 'prior_matches': chosen[1]},
           'coverage': {n: {p: int((f.period == p).sum()) for p in rc.PERIODS} for n, f in forecasts.items()},
           'inputs': tests, 'market_informed': market, 'combined': combined, 'comparison': {}}
    pairs = [('K1', 'B0'), ('K1', 'NB2'), ('NB2', 'B0'), ('K1r', 'K1'), ('K1r', 'NB2')]
    pairs += [('K2', 'K1r'), ('K2', 'NB2')] if 'K2' in forecasts else []
    pairs += [('K2m', 'K2' if 'K2' in forecasts else 'K1r'), ('K2m', 'NB2')] if 'K2m' in forecasts else []
    for period in rc.PERIODS:
        keys = common.loc[common.period == period, KEY]
        entry = {'all': summarise({n: forecasts[n] for n in names}, keys), 'leagues': {}}
        for league in rc.DIVISIONS:
            lk = keys.loc[keys.league == league]
            entry['leagues'][league] = {
                'fixtures': int(len(lk)),
                'mean_over_log_loss': {n: float(lk.merge(forecasts[n], on=KEY).avg_ll.mean()) for n in names},
                'differences': {f'{a}_minus_{b}': paired(lk.merge(forecasts[a], on=KEY),
                                                         lk.merge(forecasts[b], on=KEY))[period]['mean_over_log_loss']
                                for a, b in pairs if a in names and b in names}}
        res['comparison'][period] = entry
    res['differences'] = {f'{a}_minus_{b}': paired(forecasts[a], forecasts[b]) for a, b in pairs}
    out_forecasts = pd.concat([f[KEY + ['period', 'week', 'total', 'mu', 'alpha']].assign(model=n)
                               for n, f in forecasts.items()], ignore_index=True)
    return res, out_forecasts


# ---------------------------------------------------------------------------
# Report
# ---------------------------------------------------------------------------

def _ci(d):
    if not d or d.get('mean') is None:
        return '—'
    if not d.get('interval_95'):
        return f"{d['mean']:+.4f}"
    lo, hi = d['interval_95']
    return f"{d['mean']:+.4f} [{lo:+.4f}, {hi:+.4f}]"


def report(res) -> str:
    out = ['# Corner-total candidate K1 and its inputs (offline, accuracy only)', '',
           f"Generated by `scripts/corners_candidate_report.py` ({res['version']}). Data read up to {res['cutoff']} only; "
           f"no match after it is read. Returns: {res['returns']}. Log loss is the mean over Over/Under "
           f"{', '.join(str(l) for l in res['lines'])} (binary, per line); differences are first minus second "
           f"(negative favours the first) with 95% intervals from {res['interval']}.", '',
           '## K1 development grid', '', '| half-life (days) | prior matches | fixtures | mean Over log loss | count log loss |',
           '|---:|---:|---:|---:|---:|']
    for g in res['k1_grid_development']:
        out.append(f"| {g['half_life_days']:.0f} | {g['prior_matches']:.0f} | {g['fixtures']} | "
                   f"{g['mean_over_log_loss']:.5f} | {g['count_log_loss']:.5f} |")
    c = res['k1_chosen']
    out += ['', f"Chosen on development: half-life {c['half_life_days']:.0f} days, prior {c['prior_matches']:.0f} matches. "
            'Validation was scored only for this setting.', '']
    for period, entry in res['comparison'].items():
        a = entry['all']
        out += [f'## {period.capitalize()}: models on {a["fixtures"]} common fixtures', '',
                '| model | mean Over log loss | count log loss | 8.5 | 9.5 | 10.5 | 11.5 | slopes 8.5/9.5/10.5/11.5 | failing bands |',
                '|---|---:|---:|---:|---:|---:|---:|---|---:|']
        for n, e in a['models'].items():
            ls = [e['lines'][str(l)] for l in res['lines']]
            out.append(f"| {n} | {e['mean_over_log_loss']:.5f} | {e['count_log_loss']:.5f} | "
                       + ' | '.join(f"{x['log_loss']:.5f}" for x in ls) + ' | '
                       + ' / '.join(f"{x['slope']:.2f}" for x in ls) + ' | '
                       + f"{sum(x['bands']['failing'] for x in ls)}/{sum(x['bands']['bands_checked'] for x in ls)} |")
        out += ['', '| pair | mean Over log loss | count log loss |', '|---|---|---|']
        for pair, d in res['differences'].items():
            out.append(f"| {pair.replace('_minus_', ' − ')} | {_ci(d[period]['mean_over_log_loss'])} | "
                       f"{_ci(d[period]['count_log_loss'])} |")
        pairs = list(next(iter(entry['leagues'].values()))['differences'])
        out += ['', 'Per league (mean Over log loss, then differences):', '',
                '| league | n | ' + ' | '.join(a['models']) + ' | ' + ' | '.join(p.replace('_minus_', ' − ') for p in pairs) + ' |',
                '|---|---:|' + '---:|' * len(a['models']) + '---|' * len(pairs)]
        for league, e in entry['leagues'].items():
            out.append(f"| {league} | {e['fixtures']} | " + ' | '.join(f"{v:.5f}" for v in e['mean_over_log_loss'].values())
                       + ' | ' + ' | '.join(_ci(e['differences'][p]) for p in pairs) + ' |')
        out.append('')
    for title, block in (('Inputs on top of K1 (odds-free: the corner research view)', res['inputs']),
                         ('Market-informed variant (Pinnacle pre-match 1X2 and O/U 2.5; labelled, never odds-free)',
                          res['market_informed'])):
        out += [f'## {title}', '', f"Keep rule: {res['keep_rule']}.", '',
                '| input | development n | development | validation n | validation | kept |', '|---|---:|---|---:|---|---|']
        for g, t in block.items():
            d = t['difference_vs_K1r']
            out.append(f"| {g} | {d['development']['fixtures']} | {_ci(d['development']['mean_over_log_loss'])} | "
                       f"{d['validation']['fixtures']} | {_ci(d['validation']['mean_over_log_loss'])} | "
                       f"{'yes' if t['kept'] else 'no'} |")
        out.append('')
    if res['combined']:
        out += ['## Combined', ''] + [f"- {k}: {', '.join(v['inputs'])} ({v['note']})" for k, v in res['combined'].items()] + ['']
    return '\n'.join(out)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('--cache', default=str(ROOT / '.football_cache'))
    parser.add_argument('--output', required=True)
    parser.add_argument('--work', required=True, help='folder for the cached phase-A forecasts')
    parser.add_argument('--workers', type=int, default=max(1, (os.cpu_count() or 2) - 1))
    args = parser.parse_args(argv)
    out, work = Path(args.output), Path(args.work)
    out.mkdir(parents=True, exist_ok=True)
    work.mkdir(parents=True, exist_ok=True)
    store = phase_a(Path(args.cache), work, args.workers)
    print('phase A done', flush=True)
    res, forecasts = phase_b(store)
    (out / 'results.json').write_text(json.dumps(res, indent=1), encoding='utf-8')
    forecasts.assign(date=forecasts.date.dt.date).sort_values(KEY + ['model']).to_csv(
        out / 'forecasts.csv', index=False, float_format='%.5f', lineterminator='\n')
    (out / 'report.md').write_text(report(res), encoding='utf-8', newline='\n')
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
