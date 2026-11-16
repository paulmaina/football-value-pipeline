"""Phase 3b: how the cagey tier's market grid removes the bookmaker margin. Offline candidates only: the live
cagey tier, its correction model and every pick stay unchanged, and this script changes no production file.

Today the grid's targets use proportional margin removal (market_implied.devig_three_way and
targets_from_prices). Six grids are compared on the harness's historical matches:

    M, D            proportional (today): the market fit, and the fit plus the production correction
    M_pow, D_pow    power method on 1X2, O/U 2.5 and the main AH pair; D_pow uses the correction refitted on M_pow
    M_shin, D_shin  Shin's method on the same three markets; D_shin uses the correction refitted on M_shin

The refitted corrections come from narrow_margin.py --method (same seasons, rows and procedure as the production
model; narrow_margin_models/candidates/). No correction is ever applied to a grid it was not fitted on.

historical mode (development and validation only, both priced by Pinnacle; holdout and retrospective matches are
skipped before their prices or results are read):

  * log loss on AH settlement (all lines, draw-sensitive lines), 1X2 and Over 1.5, week-resampled 95% intervals;
  * 1X2 calibration (slopes, rule v2, rule v3 against D);
  * the cagey tier's events, rule cagey-events-v1, on the rule's own events (side chosen by D, synthetic prices
    from M) with every grid scored on those same events, and for D_pow and D_shin on their own events;
  * favourite bands: favourites grouped by the power-method 1X2 quote, each grid's forecast against the win rate;
  * the plain de-vigged quotes by market, 1X2 separately from the two-way markets (O/U 2.5, main AH pair), and
    grids where a method is applied to the 1X2 only or to the two-way markets only (where a change comes from).

live mode (integration check, no result read): every saved run in the window is rebuilt from its frozen
predictions under today's rule and under each candidate, and the cagey no-loss >= 0.75 set, the cagey tier list
and the master list are compared.

    python scripts/cagey_devig_report.py --harness-output <locked evaluation_harness.py run> \
        --output evaluation/cagey_devig_methods
    python scripts/cagey_devig_report.py --mode live --output evaluation/cagey_devig_methods
"""
from __future__ import annotations

import argparse
import json
import math
import sys
import warnings
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import evaluation_harness as eh  # noqa: E402
import historical_benchmark as hb  # noqa: E402
import market_implied as mi  # noqa: E402
import narrow_margin as nm  # noqa: E402
import research_backtest as rb  # noqa: E402

PERIODS = ('development', 'validation')
GROUPS = ('AH all', 'AH draw-sensitive', '1X2', 'Over 1.5')
METHODS = mi.DEVIG_METHODS
SUFFIX = {mi.DEVIG_PROPORTIONAL: '', mi.DEVIG_POWER: '_pow', mi.DEVIG_SHIN: '_shin'}
GRIDS = tuple(kind + SUFFIX[m] for m in METHODS for kind in ('M', 'D'))  # M, D, M_pow, D_pow, M_shin, D_shin
CANDIDATES = GRIDS[2:]
# Context only: one method on the 1X2 alone or on the two-way markets alone, the rest proportional (no correction).
SPLITS = tuple(f'M{SUFFIX[m]}_{part}' for m in METHODS[1:] for part in ('1x2', '2way'))
QUOTES = {m: 'Q' + (SUFFIX[m][1:].upper() or 'PROP') for m in METHODS}  # QPROP, QPOW, QSHIN
FAVOURITE_EDGES = (0.0, 0.4, 0.5, 0.6, 0.7, 0.8, 1.0)
SAFE_NO_LOSS = 0.75  # the master's "safe" threshold (master_reconciliation_config.json, min_cagey_no_loss)
SAMPLES, SEED = 2000, 136
EVENT_RULE = 'cagey-events-v1'


def models() -> dict:
    """The correction of each method's grid: production for proportional, the refitted candidates otherwise."""
    out = {mi.DEVIG_PROPORTIONAL: nm.production_model()}
    for method, version in nm.CANDIDATE_VERSIONS.items():
        out[method] = nm.load(version, nm.CANDIDATE_DIR)
    for method, model in out.items():
        nm.require_method(model, method)
    return out


# ---------------------------------------------------------------------------
# Per-match work (no holdout or retrospective row ever reaches it)
# ---------------------------------------------------------------------------

def split_matrix(prices, method, part):
    """Fit B with `method` on the 1X2 only ('1x2') or on O/U 2.5 and the main AH pair only ('2way')."""
    targets = mi.targets_from_prices(prices['hda'], prices['ou'], prices['ah'])
    other = mi.targets_from_prices(prices['hda'], prices['ou'], prices['ah'], method=method)
    keys = ('home', 'draw', 'away') if part == '1x2' else ('over_2_5', 'ah_main')
    targets.update({k: other[k] for k in keys})
    result = mi.fit(targets, include_ah=True)
    if not result.usable:
        raise ValueError('; '.join(result.reasons))
    return rb.matrix_value(result.matrix)


def quotes(prices) -> dict:
    """The plain de-vigged quotes per method: 1X2, P(over 2.5) and the home win share on the main AH line."""
    return {m: {'hda': list(mi.devig_three_way(*prices['hda'], method=m)),
                'over': mi.devig_two_way(*prices['ou'], method=m)[0],
                'ah_home': mi.devig_two_way(*prices['ah'][1:], method=m)[0]} for m in METHODS}


def fixture_events(inputs, selector, basis, rule) -> list:
    """Rule cagey-events-v1's events for one fixture (side by `selector`, synthetic prices from `basis`), with
    every grid's probability of each event."""
    out = []
    for event in eh.cagey_fixture_events(inputs[selector], inputs[basis], rule):
        out.append({'family': event['family'], 'side': event['side'], 'k': event['k'], 'y': event['y'],
                    **{f'p_{c}': eh.cagey_event_probability(event, f) for c, f in inputs.items()}})
    return out


def league_records(league, cache, cfg, splits):
    warnings.filterwarnings('ignore')
    corrections = models()
    rule = eh.calibration_rules(cfg)[EVENT_RULE]
    data, _, _ = hb.load_history(Path(cache), league, {**cfg, 'test_end_exclusive': cfg['end_exclusive']})
    start, end = pd.Timestamp(cfg['test_start']), pd.Timestamp(cfg['holdout_start'])
    fixtures, records = [], []
    counts = {'outside_periods_skipped': 0, 'no_prices': 0, **{f'fit_failed_{m}': 0 for m in METHODS},
              'split_fit_failed': 0}
    for _, row in data.loc[data.Date >= start].iterrows():
        name = eh.phase(row.Date, league, cfg)
        if name not in PERIODS or row.Date >= end:
            # Holdout and retrospective matches: skipped before their prices or result are read.
            counts['outside_periods_skipped'] += 1
            continue
        book = eh.period_book(row.Date, cfg)
        assert book == 'pinnacle'
        prices = eh.book_prices(row, book)
        if prices is None:
            counts['no_prices'] += 1
            continue
        grids, failed = {}, False
        for method in METHODS:
            try:
                grids['M' + SUFFIX[method]] = eh.market_matrix(prices, method)
                grids['D' + SUFFIX[method]] = eh.cagey_matrix(grids['M' + SUFFIX[method]], prices,
                                                              corrections[method], method)
            except (ValueError, TypeError, KeyError):
                counts[f'fit_failed_{method}'] += 1
                failed = True
        if failed:
            continue  # the six grids are compared on the same matches
        if splits:
            try:
                for name_ in SPLITS:
                    _, tag, part = name_.split('_')
                    grids[name_] = split_matrix(prices, mi.DEVIG_POWER if tag == 'pow' else mi.DEVIG_SHIN, part)
            except (ValueError, TypeError, KeyError):
                counts['split_fit_failed'] += 1
                grids = {k: v for k, v in grids.items() if k in GRIDS}
        date = row.Date
        identity = {'league': league, 'date': date.date().isoformat(),
                    'week': f'{date.isocalendar().year}-W{date.isocalendar().week:02d}',
                    'fixture_key': '|'.join((league, date.date().isoformat(), row.HomeTeam, row.AwayTeam)),
                    'phase': name, 'market_book': book}
        hg, ag = int(row.FTHG), int(row.FTAG)
        records.extend(rb.score_fixture(identity, grids, hg, ag))
        margin = hg - ag
        fixture = {**identity, 'margin': margin, 'outcome': 0 if margin > 0 else 1 if margin == 0 else 2,
                   'over_2_5': int(hg + ag > 2), 'ah_line': float(prices['ah'][0]), 'quotes': quotes(prices),
                   'overround': {'hda': sum(1 / p for p in prices['hda']) - 1, 'ou': sum(1 / p for p in prices['ou']) - 1,
                                 'ah': sum(1 / p for p in prices['ah'][1:]) - 1}}
        inputs = {}
        for cand in GRIDS:
            grid = grids[cand]
            h, a = np.indices(grid.shape)
            fixture[cand] = [float(grid[h > a].sum()), float(grid[h == a].sum()), float(grid[h < a].sum())]
            inputs[cand] = eh.cagey_inputs(grid, prices, book, identity['week'], margin)
        fixture['narrow'] = {c: float(np.asarray(inputs[c]['margin_probs'])[np.abs(inputs[c]['margins']) <= 1].sum())
                             for c in GRIDS}
        # The declared events (side chosen by D, synthetic prices from M), and each candidate tier's own events.
        fixture['events'] = {'declared': fixture_events(inputs, 'D', 'M', rule),
                             **{'own' + SUFFIX[m]: fixture_events(inputs, 'D' + SUFFIX[m], 'M' + SUFFIX[m], rule)
                                for m in METHODS[1:]}}
        fixtures.append(fixture)
    return fixtures, records, counts


# ---------------------------------------------------------------------------
# Statistics
# ---------------------------------------------------------------------------

def week_mean(frame, value, samples=SAMPLES, seed=SEED):
    """Mean of `value` with whole calendar weeks resampled."""
    if frame.empty:
        return None
    weeks = frame.groupby('week')[value].agg(['sum', 'count'])
    mean = float(weeks['sum'].sum() / weeks['count'].sum())
    if len(weeks) < 2:
        return {'mean': mean, 'interval_95': None, 'weeks': len(weeks), 'n': int(len(frame))}
    draws = np.random.default_rng(seed).integers(0, len(weeks), size=(samples, len(weeks)))
    means = weeks['sum'].to_numpy()[draws].sum(1) / weeks['count'].to_numpy()[draws].sum(1)
    interval = [float(v) for v in np.quantile(means, [.025, .975])]
    return {'mean': mean, 'interval_95': interval, 'weeks': len(weeks), 'n': int(len(frame)),
            'clear_of_zero': bool(interval[0] > 0 or interval[1] < 0)}


def log_loss_section(scores, keys):
    """Per group: each grid's mean, and baseline minus candidate (positive = candidate better) against D (the live
    cagey grid), against M, and each method's own M minus its own D (what its correction adds)."""
    part = scores.loc[scores.fixture_key.isin(keys)]
    out = {}
    for group in GROUPS:
        sub = part.loc[part.group == group]
        means = sub.groupby('candidate').log_loss.mean()
        present = [c for c in (*GRIDS, *SPLITS) if c in means]
        out[group] = {'mean': {c: float(means[c]) for c in present},
                      'D_minus': {c: eh.paired(sub, 'D', c) for c in present if c != 'D'},
                      'M_minus': {c: eh.paired(sub, 'M', c) for c in present if c != 'M'},
                      'own_M_minus_own_D': {'D' + SUFFIX[m]: eh.paired(sub, 'M' + SUFFIX[m], 'D' + SUFFIX[m])
                                            for m in METHODS},
                      'D_pow_minus_D_shin': eh.paired(sub, 'D_pow', 'D_shin'),
                      'M_pow_minus_M_shin': eh.paired(sub, 'M_pow', 'M_shin')}
    return out


def calibration_1x2(fx, rules):
    rows = {c: [{'fixture_key': f['fixture_key'], 'probs': f[c], 'outcome': f['outcome']} for f in fx] for c in GRIDS}
    out = {}
    for cand in GRIDS:
        v2 = eh.calibration_check(rows[cand], rules['v2'])
        entry = {'slopes': eh._slopes(rows[cand], ('home', 'draw', 'away')),
                 'mean_forecast': [float(v) for v in np.mean([r['probs'] for r in rows[cand]], axis=0)],
                 'v2_passes': v2['passes'], 'v2_slopes_pass': v2['slopes_pass'], 'v2_failing_bands': v2['failing_bands']}
        for base in ('D', 'M'):
            if cand != base:
                v3 = eh.calibration_check(rows[cand], rules['v3'], baseline_rows=rows[base])
                entry[f'v3_vs_{base}'] = {'passes': v3['passes'], 'slopes_pass': v3['slopes_pass'],
                                          'closer_to_one': v3['relative_slopes']['closer_to_one_than_baseline'],
                                          'failing_bands': v3['failing_bands']}
        out[cand] = entry
    out['observed'] = [float(np.mean([f['outcome'] == k for f in fx])) for k in range(3)]
    return out


def events_frame(fx, key):
    rows = [{'phase': f['phase'], 'fixture_key': f['fixture_key'], 'week': f['week'], **e}
            for f in fx for e in f['events'][key]]
    return pd.DataFrame(rows)


def events_section(fx, rule):
    """Rule cagey-events-v1. `declared`: the rule's own events (side by D, prices from M), every grid scored on
    them, judged against M (the rule) and against D (today's tier). `own`: D_pow and D_shin on the events their
    own tier would have (side by D_x, prices from M_x), each against its own M_x and against D on those events."""
    declared = events_frame(fx, 'declared')
    out = {'declared_events': {}, 'own_events': {}}
    for cand in GRIDS:
        entry = {}
        for base in ('M', 'D'):
            check = eh.cagey_events_check(declared, rule, cand, base)
            entry[f'against_{base}'] = {'passes': check['passes'], 'families': {
                fam: {k: v[k] for k in ('events', 'fixtures', 'mean_forecast', 'observed_rate', 'slope',
                                         'baseline_slope', 'slope_in_band', 'closer_to_one_than_baseline',
                                         'slope_passes', 'bands_checked', 'band_z_threshold', 'failing_bands',
                                         'passes') if k in v}
                for fam, v in check['families'].items()}}
        entry['log_loss'] = {}
        for family in rule['families']:
            part = declared.loc[declared.family == family]
            p, y = part[f'p_{cand}'].clip(1e-15, 1 - 1e-15), part.y
            loss = -(y * np.log(p) + (1 - y) * np.log(1 - p))
            base = part['p_D'].clip(1e-15, 1 - 1e-15)
            gain = -(y * np.log(base) + (1 - y) * np.log(1 - base)) - loss
            entry['log_loss'][family] = {'mean': float(loss.mean()),
                                         'D_minus_candidate': week_mean(part.assign(gain=gain), 'gain')}
        out['declared_events'][cand] = entry
    for method in METHODS[1:]:
        own = events_frame(fx, 'own' + SUFFIX[method])
        cand, base = 'D' + SUFFIX[method], 'M' + SUFFIX[method]
        out['own_events'][cand] = {
            f'against_{b}': (lambda c: {'passes': c['passes'], 'families': {
                fam: {k: v[k] for k in ('events', 'fixtures', 'mean_forecast', 'baseline_mean_forecast',
                                         'observed_rate', 'slope', 'baseline_slope', 'slope_passes',
                                         'failing_bands', 'passes') if k in v}
                for fam, v in c['families'].items()}})(eh.cagey_events_check(own, rule, cand, b))
            for b in (base, 'D')}
    return out


def favourite_bands(fx):
    """Favourites (the likelier of home and away under the power-method 1X2 quote) grouped by that quote's
    probability: each grid's and each plain quote's mean probability for the favourite against its win rate."""
    rows = []
    for f in fx:
        q = f['quotes'][mi.DEVIG_POWER]['hda']
        side = 0 if q[0] >= q[2] else 2
        rows.append({'week': f['week'], 'p_band': q[side], 'won': int(f['outcome'] == side),
                     **{c: f[c][side] for c in GRIDS},
                     **{QUOTES[m]: f['quotes'][m]['hda'][side] for m in METHODS}})
    frame = pd.DataFrame(rows)
    out = []
    for low, high in zip(FAVOURITE_EDGES, FAVOURITE_EDGES[1:]):
        part = frame.loc[(frame.p_band >= low) & (frame.p_band < high)]
        if part.empty:
            continue
        n, won = len(part), float(part.won.mean())
        entry = {'band': f'{low:.0%}-{high:.0%}' if low else f'under {high:.0%}', 'fixtures': n, 'won': won,
                 'forecast': {}}
        if high == 1.0:
            entry['band'] = f'{low:.0%}+'
        for name in (*GRIDS, *QUOTES.values()):
            mean = float(part[name].mean())
            se = math.sqrt(mean * (1 - mean) / n)
            gap = week_mean(part.assign(gap=part.won - part[name]), 'gap')
            entry['forecast'][name] = {'mean': mean, 'won_minus_forecast': won - mean,
                                       'interval_95': gap['interval_95'], 'z': abs(won - mean) / se if se else None}
        out.append(entry)
    return out


def quote_section(fx):
    """The plain de-vigged quotes, by market: 1X2 separately from the two-way markets. Log loss of each method's
    quote, proportional minus method (positive = the method is better), and how far the method moves the quote."""
    from ah_close_backtest import settle
    rows = {'1X2': [], 'O/U 2.5': [], 'AH main': []}
    moves = {m: {k: [] for k in ('1X2 favourite', '1X2 draw', 'O/U 2.5', 'AH main')} for m in METHODS[1:]}
    slopes = {m: {} for m in METHODS}
    for f in fx:
        won, lost = (float(v) for v in settle(f['margin'], f['ah_line']))
        base = f['quotes'][mi.DEVIG_PROPORTIONAL]
        for m in METHODS:
            q = f['quotes'][m]
            common = {'fixture_key': f['fixture_key'], 'week': f['week'], 'candidate': m}
            rows['1X2'].append({**common, 'log_loss': -math.log(max(q['hda'][f['outcome']], 1e-15))})
            rows['O/U 2.5'].append({**common, 'log_loss': -math.log(q['over'] if f['over_2_5'] else 1 - q['over'])})
            if won + lost > 0:  # a push on a whole line carries no information
                rows['AH main'].append({**common, 'log_loss': -(won * math.log(q['ah_home'])
                                                                + lost * math.log(1 - q['ah_home']))})
            if m != mi.DEVIG_PROPORTIONAL:
                fav = 0 if base['hda'][0] >= base['hda'][2] else 2
                moves[m]['1X2 favourite'].append(q['hda'][fav] - base['hda'][fav])
                moves[m]['1X2 draw'].append(q['hda'][1] - base['hda'][1])
                moves[m]['O/U 2.5'].append(abs(q['over'] - base['over']))
                moves[m]['AH main'].append(abs(q['ah_home'] - base['ah_home']))
    for m in METHODS:
        hda = np.array([f['quotes'][m]['hda'] for f in fx])
        outcome = np.array([f['outcome'] for f in fx])
        slopes[m] = {'home': eh.calibration_slope(hda[:, 0], outcome == 0),
                     'away': eh.calibration_slope(hda[:, 2], outcome == 2),
                     'over_2_5': eh.calibration_slope([f['quotes'][m]['over'] for f in fx], [f['over_2_5'] for f in fx])}
    out = {'margin': {k: float(np.mean([f['overround'][k] for f in fx])) for k in ('hda', 'ou', 'ah')},
           'slopes': slopes, 'markets': {}, 'moved_from_proportional': {
               m: {k: {'mean': float(np.mean(v)), 'mean_abs': float(np.mean(np.abs(v))), 'max_abs': float(np.max(np.abs(v)))}
                   for k, v in parts.items()} for m, parts in moves.items()}}
    for market, records in rows.items():
        frame = pd.DataFrame(records)
        means = frame.groupby('candidate').log_loss.mean()
        out['markets'][market] = {'fixtures': int(frame.fixture_key.nunique()),
                                  'mean': {m: float(means[m]) for m in METHODS},
                                  'proportional_minus': {m: eh.paired(frame, mi.DEVIG_PROPORTIONAL, m)
                                                         for m in METHODS[1:]},
                                  'power_minus_shin': eh.paired(frame, mi.DEVIG_POWER, mi.DEVIG_SHIN)}
    return out


def narrow_section(fx):
    y = np.array([abs(f['margin']) <= 1 for f in fx], float)
    return {'observed': float(y.mean()),
            'forecast': {c: float(np.mean([f['narrow'][c] for f in fx])) for c in GRIDS},
            'correction_moves_narrow_by': {'D' + SUFFIX[m]: float(np.mean([abs(f['narrow']['D' + SUFFIX[m]]
                                                                              - f['narrow']['M' + SUFFIX[m]]) for f in fx]))
                                           for m in METHODS}}


def model_record(model):
    return {**{k: model.get(k) for k in ('version', 'devig_method', 'training_first_date', 'training_last_date',
                                         'training_until_exclusive', 'training_matches', 'training_fingerprint',
                                         'training_fit_counts', 'training_cagey_p20')},
            'targets': {g: {k: t[k] for k in ('intercept', 'coefficients', 'training_log_loss')}
                        for g, t in model['targets'].items()}}


def historical(args, cfg):
    rules = {'v2': cfg['calibration_tolerance'],
             'v3': eh.calibration_rules(cfg)['slopes-0.90-1.10-or-closer-than-baseline-bands-30-5pp-bonferroni-v3']}
    event_rule = eh.calibration_rules(cfg)[EVENT_RULE]
    leagues = cfg['leagues']
    with ProcessPoolExecutor(max_workers=args.workers) as pool:
        parts = list(pool.map(league_records, leagues, [args.cache] * len(leagues), [cfg] * len(leagues),
                              [not args.no_splits] * len(leagues)))
    fixtures = [f for p in parts for f in p[0]]
    records = [r for p in parts for r in p[1]]
    counts = {k: sum(p[2][k] for p in parts) for k in parts[0][2]}
    assert all(f['phase'] in PERIODS for f in fixtures)
    scores = eh.fixture_scores(records, cfg['draw_sensitive_lines'])

    harness = pd.read_csv(args.harness_output / 'fixture_scores.csv')
    assert not harness.phase.eq('holdout').any(), 'the harness output must come from a locked run'
    hd = harness.loc[harness.candidate.isin(['M', 'D']) & harness.phase.isin(PERIODS)]
    harness_keys = set(hd.loc[hd.candidate == 'D', 'fixture_key'])
    # The recomputed D and M must equal the harness's own scores on every match the harness scored.
    merged = hd.merge(scores, on=['fixture_key', 'candidate', 'group'], suffixes=('_harness', ''))
    consistency = {'harness_D_fixtures': len(harness_keys), 'matches_compared': int(merged.fixture_key.nunique()),
                   'max_abs_log_loss_difference': float((merged.log_loss - merged.log_loss_harness).abs().max())}
    missing = harness_keys - {f['fixture_key'] for f in fixtures}
    consistency['harness_fixtures_without_all_six_grids'] = len(missing)
    assert consistency['max_abs_log_loss_difference'] < 1e-12, consistency
    results = json.loads((args.harness_output / 'results.json').read_text(encoding='utf-8'))
    corrections = models()
    summary = {'script': 'scripts/cagey_devig_report.py', 'harness_commit': results.get('source_commit'),
               'config_sha256': results.get('config_sha256'), 'counts': counts,
               'consistency_with_harness': consistency, 'grids': list(GRIDS), 'splits': list(SPLITS),
               'correction_models': {m: model_record(corrections[m]) for m in METHODS},
               'same_training_rows': len({corrections[m]['training_fingerprint'] for m in METHODS}) == 1,
               'periods': {}}
    for name in (*PERIODS, 'development+validation'):
        fx_all = [f for f in fixtures if f['phase'] == name or name == 'development+validation']
        cohorts = {'harness': [f for f in fx_all if f['fixture_key'] in harness_keys], 'all_priced': fx_all}
        summary['periods'][name] = {}
        for cohort, fx in cohorts.items():
            keys = {f['fixture_key'] for f in fx}
            entry = {'fixtures': len(fx), 'weeks': len({f['week'] for f in fx}),
                     'favourite_bands': favourite_bands(fx), 'quotes': quote_section(fx)}
            if name in PERIODS:
                entry.update(log_loss=log_loss_section(scores, keys), calibration_1x2=calibration_1x2(fx, rules),
                             narrow=narrow_section(fx), cagey_events=events_section(fx, event_rule))
            summary['periods'][name][cohort] = entry
    args.output.mkdir(parents=True, exist_ok=True)
    (args.output / 'summary.json').write_text(json.dumps(summary, indent=2, sort_keys=True, default=float) + '\n',
                                              encoding='utf-8')
    print(json.dumps({'counts': counts, 'consistency_with_harness': consistency}, indent=2))
    return 0


# ---------------------------------------------------------------------------
# Live replay (integration check; no result is read)
# ---------------------------------------------------------------------------

ROW_KEY = ['league', 'home_team', 'away_team', 'kickoff_utc', 'market', 'bookmaker', 'offered_decimal_odds']


def _column(frame, name):
    return frame[name] if name in frame else pd.Series(np.nan, index=frame.index, dtype=object)


def _pick_key(frame) -> list:
    if frame.empty:
        return []
    return ['|'.join(map(str, row)) for row in frame[ROW_KEY].itertuples(index=False)]


def master_picks(frame):
    """The master list's picks in rank order (the file also carries the offers it left out)."""
    if 'new_master_decision' not in frame:
        return frame
    picks = frame.loc[frame.new_master_decision.eq('SHORTLISTED')]
    return picks.sort_values('new_master_rank', kind='stable')


def compare_lists(base, cand, probability, tier=None):
    """Two ranked lists of picks: which are shared, and how the shared ones move."""
    a, b = _pick_key(base), _pick_key(cand)
    tiers = {}
    if tier is not None and tier in base and tier in cand:
        ta, tb = dict(zip(a, base[tier].astype(object).map(str))), dict(zip(b, cand[tier].astype(object).map(str)))
        tiers = {'shared_tier_changed': sum(ta[k] != tb[k] for k in ta if k in tb)}
    shared = [k for k in a if k in set(b)]
    ra, rb_ = {k: i for i, k in enumerate(a)}, {k: i for i, k in enumerate(b)}
    moves = [abs(ra[k] - rb_[k]) for k in shared]
    rho = None
    if len(shared) >= 3:
        rho = float(pd.Series([ra[k] for k in shared]).corr(pd.Series([rb_[k] for k in shared]), method='spearman'))
    return {'picks_baseline': len(a), 'picks_candidate': len(b), 'shared': len(shared),
            'only_baseline': len(set(a) - set(b)), 'only_candidate': len(set(b) - set(a)),
            'same_order': a == b, 'shared_moved': int(sum(m > 0 for m in moves)),
            'mean_rank_move': float(np.mean(moves)) if moves else 0.0, 'max_rank_move': int(max(moves, default=0)),
            'spearman': rho, **tiers,
            'top5_shared': len(set(a[:5]) & set(b[:5])), 'top5_size': min(5, len(a)),
            'mean_probability_baseline': float(pd.to_numeric(base[probability], errors='coerce').mean()) if len(base) else None,
            'mean_probability_candidate': float(pd.to_numeric(cand[probability], errors='coerce').mean()) if len(cand) else None}


def live(args):
    import master_shortlist
    import price_edge_cagey_shortlist as v28
    import shortlist_window
    from quote_policy import load_policy
    from scripts.master_reconciliation_replay import runs
    corrections = models()
    base_settings = {**v28.load_settings(), 'shortlist_lookahead_hours': shortlist_window.DEFAULT_HOURS}
    report = {'script': 'scripts/cagey_devig_report.py --mode live', 'start': args.start, 'end_exclusive': args.end,
              'safe_no_loss': SAFE_NO_LOSS, 'note': 'Integration check: no result is read.', 'runs': []}
    out_root = args.output / 'live_runs'
    for generated, directory, _ in runs(ROOT, args.start, args.end):
        predictions = pd.read_csv(directory / 'predictions.csv', low_memory=False)
        built, entry = {}, {'snapshot': directory.name, 'generated_at_utc': generated}
        for method in METHODS:
            settings = base_settings if method == mi.DEVIG_PROPORTIONAL else {**base_settings, 'devig_method': method}
            target = out_root / method / directory.name
            target.mkdir(parents=True, exist_ok=True)
            with warnings.catch_warnings():
                warnings.simplefilter('ignore')
                _, decisions, summary = v28.build_shortlist(predictions, pd.Timestamp(generated),
                                                            execution_policy=load_policy(), settings=settings,
                                                            model=corrections[method])
                tier = v28.cagey_tier_list(decisions)
                summary.setdefault('quote_execution_policy', load_policy())
                master_shortlist.refresh(decisions.copy(), target, summary, predictions)
            master = master_picks(pd.read_csv(target / master_shortlist.FILE, low_memory=False)
                                  if (target / master_shortlist.FILE).exists() else pd.DataFrame(columns=ROW_KEY))
            built[method] = (decisions, tier, master)
        if args.check_default:
            # Today's rule with the settings spelled out must be the pipeline's own default call.
            with warnings.catch_warnings():
                warnings.simplefilter('ignore')
                _, default, _ = v28.build_shortlist(predictions, pd.Timestamp(generated),
                                                    execution_policy=load_policy(), model=nm.production_model())
            entry['default_identical'] = bool(default.to_csv(index=False) == built[mi.DEVIG_PROPORTIONAL][0].to_csv(index=False))
            assert entry['default_identical'], directory.name
        base_decisions, base_tier, base_master = built[mi.DEVIG_PROPORTIONAL]
        entry['offers'] = int(len(base_decisions))
        column = v28.tier_no_loss_column(base_decisions)
        base_p = pd.to_numeric(_column(base_decisions, column), errors='coerce')
        entry['offers_with_cagey_no_loss'] = int(base_p.notna().sum())
        entry['methods'] = {}
        for method in METHODS[1:]:
            decisions, tier, master = built[method]
            assert _pick_key(decisions) == _pick_key(base_decisions), directory.name
            p = pd.to_numeric(_column(decisions, column), errors='coerce')
            both = base_p.notna() & p.notna()
            safe_a, safe_b = both & (base_p >= SAFE_NO_LOSS), both & (p >= SAFE_NO_LOSS)
            other = [c for c in decisions.columns if not c.startswith(('cagey_', 'corrected_', 'uncorrected_',
                                                                       'price_guard', 'totals_correction', 'narrow_'))
                     and c not in ('price_flag', 'in_value_tier', 'correction_validation_note')]
            value_same = bool(_pick_key(decisions.loc[_column(decisions, 'decision').eq('SHORTLISTED')])
                              == _pick_key(base_decisions.loc[_column(base_decisions, 'decision').eq('SHORTLISTED')]))
            entry['methods'][method] = {
                'offers_scored_by_both': int(both.sum()),
                'scored_only_by_baseline': int((base_p.notna() & p.isna()).sum()),
                'scored_only_by_candidate': int((base_p.isna() & p.notna()).sum()),
                'no_loss_mean_change': float((p - base_p)[both].mean()) if both.any() else None,
                'no_loss_mean_abs_change': float((p - base_p)[both].abs().mean()) if both.any() else None,
                'no_loss_max_abs_change': float((p - base_p)[both].abs().max()) if both.any() else None,
                'safe_baseline': int(safe_a.sum()), 'safe_candidate': int(safe_b.sum()),
                'safe_both': int((safe_a & safe_b).sum()), 'safe_left': int((safe_a & ~safe_b).sum()),
                'safe_entered': int((~safe_a & safe_b).sum()),
                'cagey_decision_changed': int((_column(decisions, 'cagey_tier_decision').astype(object).map(str)
                                               != _column(base_decisions, 'cagey_tier_decision').astype(object).map(str)).sum()),
                'value_shortlist_same': value_same,
                'columns_changed_outside_cagey': sorted(
                    c for c in other if c in base_decisions and decisions[c].astype(object).map(str).tolist()
                    != base_decisions[c].astype(object).map(str).tolist()),
                'cagey_tier': compare_lists(base_tier, tier, v28.tier_no_loss_column(base_tier)),
                # The value tier's older price-edge reference for derived plus lines (reference_type c-cagey) is
                # the cagey-corrected fair price by definition, so those rows' fair odds follow the cagey grid.
                'value_reference_rows_moved': int((pd.to_numeric(_column(decisions, 'fair_odds'), errors='coerce')
                                                   .sub(pd.to_numeric(_column(base_decisions, 'fair_odds'), errors='coerce'))
                                                   .abs() > 1e-12).sum()),
                'value_reference_rows_moved_not_c_cagey': int(((pd.to_numeric(_column(decisions, 'fair_odds'), errors='coerce')
                                                                .sub(pd.to_numeric(_column(base_decisions, 'fair_odds'), errors='coerce'))
                                                                .abs() > 1e-12)
                                                               & ~_column(base_decisions, 'reference_type').eq('c-cagey')).sum()),
                'value_decisions_same': bool(
                    _column(decisions, 'decision').astype(object).map(str).tolist()
                    == _column(base_decisions, 'decision').astype(object).map(str).tolist()
                    and _column(decisions, 'rejection_reasons').astype(object).map(str).tolist()
                    == _column(base_decisions, 'rejection_reasons').astype(object).map(str).tolist()),
                'master': compare_lists(base_master, master, 'ranking_no_loss_probability', tier='new_master_tier')}
        report['runs'].append(entry)
    totals = {}
    for method in METHODS[1:]:
        rows = [r['methods'][method] for r in report['runs']]
        add = lambda key: int(sum(r[key] for r in rows))  # noqa: E731
        weight = sum(r['offers_scored_by_both'] for r in rows)
        totals[method] = {
            'runs': len(rows), 'offers_scored_by_both': weight,
            'scored_only_by_baseline': add('scored_only_by_baseline'),
            'scored_only_by_candidate': add('scored_only_by_candidate'),
            'no_loss_mean_change': sum((r['no_loss_mean_change'] or 0) * r['offers_scored_by_both'] for r in rows) / max(weight, 1),
            'no_loss_mean_abs_change': sum((r['no_loss_mean_abs_change'] or 0) * r['offers_scored_by_both'] for r in rows) / max(weight, 1),
            'no_loss_max_abs_change': max((r['no_loss_max_abs_change'] or 0) for r in rows),
            **{k: add(k) for k in ('safe_baseline', 'safe_candidate', 'safe_both', 'safe_left', 'safe_entered',
                                   'cagey_decision_changed', 'value_reference_rows_moved',
                                   'value_reference_rows_moved_not_c_cagey')},
            'value_decisions_same_in_every_run': all(r['value_decisions_same'] for r in rows),
            'master_shared_tier_changed': int(sum(r['master'].get('shared_tier_changed', 0) for r in rows)),
            'runs_with_safe_set_changed': sum(bool(r['safe_left'] or r['safe_entered']) for r in rows),
            'value_shortlist_same_in_every_run': all(r['value_shortlist_same'] for r in rows),
            'columns_changed_outside_cagey': sorted({c for r in rows for c in r['columns_changed_outside_cagey']}),
            **{name: {'picks_baseline': sum(r[name]['picks_baseline'] for r in rows),
                      'picks_candidate': sum(r[name]['picks_candidate'] for r in rows),
                      'shared': sum(r[name]['shared'] for r in rows),
                      'only_baseline': sum(r[name]['only_baseline'] for r in rows),
                      'only_candidate': sum(r[name]['only_candidate'] for r in rows),
                      'runs_same_picks': sum(r[name]['only_baseline'] == 0 and r[name]['only_candidate'] == 0 for r in rows),
                      'runs_same_order': sum(r[name]['same_order'] for r in rows),
                      'shared_moved': sum(r[name]['shared_moved'] for r in rows),
                      'max_rank_move': max(r[name]['max_rank_move'] for r in rows),
                      'mean_spearman': float(np.mean([r[name]['spearman'] for r in rows if r[name]['spearman'] is not None]))
                      if any(r[name]['spearman'] is not None for r in rows) else None,
                      'top5_shared': sum(r[name]['top5_shared'] for r in rows),
                      'top5_size': sum(r[name]['top5_size'] for r in rows)}
               for name in ('cagey_tier', 'master')}}
    report['totals'] = totals
    report['default_identical_in_every_run'] = (all(r.get('default_identical') for r in report['runs'])
                                                if args.check_default else None)
    args.output.mkdir(parents=True, exist_ok=True)
    (args.output / 'live_replay.json').write_text(json.dumps(report, indent=2, sort_keys=True, default=float) + '\n',
                                                  encoding='utf-8')
    print(json.dumps({'runs': len(report['runs']), 'totals': totals}, indent=2, default=float))
    return 0


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('--mode', choices=('historical', 'live'), default='historical')
    parser.add_argument('--cache', type=Path, default=ROOT / '.football_cache')
    parser.add_argument('--config', type=Path, default=eh.CONFIG)
    parser.add_argument('--harness-output', type=Path,
                        help='output of a locked evaluation_harness.py run (fixture_scores.csv, results.json)')
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--workers', type=int, default=8)
    parser.add_argument('--no-splits', action='store_true', help='skip the 1X2-only and two-way-only grids')
    parser.add_argument('--start', default='2026-10-27', help='live mode: first run day')
    parser.add_argument('--end', default='2026-11-09', help='live mode: last run day, exclusive')
    parser.add_argument('--no-check-default', dest='check_default', action='store_false')
    args = parser.parse_args(argv)
    if args.mode == 'live':
        return live(args)
    if args.harness_output is None:
        parser.error('--harness-output is required in historical mode')
    return historical(args, json.loads(args.config.read_text(encoding='utf-8')))


if __name__ == '__main__':
    raise SystemExit(main())
