"""Phase 3b-2: D_pow2, the cagey grid with its 1X2 set separately. Offline candidate only: the live cagey tier,
its correction model and every pick stay unchanged, and this script changes no production file.

    D        today: proportional margin removal, the production correction
    D_pow    PR #182's candidate: the power method on all three inputs, the correction refitted on that grid
    D_pow2   D_pow's grid and correction for the shape of margins, then the 1X2 set separately:
             logit(draw') = logit(draw_q) + a + b * (f - 0.5), draw_q and f (the favourite's probability) from the
             power quote, home and away sharing the rest in the power quote's ratio, and the corrected grid moved
             onto that 1X2 with reweight_matrix_to_1x2 (narrow_margin.one_x_two_target; a and b fitted on the
             correction's own training rows, model cagey-correction-through-2425-power-1x2-v1)

M and M_pow (the uncorrected grids) and the plain quotes QPROP and QPOW are carried for reference.

historical mode (development and validation only, both priced by Pinnacle; holdout and retrospective matches are
skipped before their prices or results are read):

  * the problem statement's figures, reproduced with D and QPOW;
  * log loss on AH settlement (all lines, draw-sensitive lines), 1X2 and Over 1.5, week-resampled 95% intervals;
  * rule cagey-events-v1 on the rule's own events (side chosen by D, synthetic prices from M), every grid scored
    on those same events, and D_pow and D_pow2 on the events their own tier would create;
  * favourite-win and draw calibration by favourite band (the bands of PR #182: the favourite is the likelier of
    home and away under the power-method quote, grouped by that quote);
  * 1X2 calibration slopes and P(narrow);
  * the choice rule of docs/plan.md (3b-2), applied mechanically.

live mode (integration check, no result read): every saved run in the window is rebuilt from its frozen
predictions under today's rule, D_pow and D_pow2, and the cagey no-loss >= 0.75 set, the cagey tier list and the
master list are compared.

    python scripts/cagey_dpow2_report.py --harness-output <locked evaluation_harness.py run> \
        --output evaluation/cagey_dpow2
    python scripts/cagey_dpow2_report.py --mode live --output evaluation/cagey_dpow2
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
from scripts import cagey_devig_report as base  # noqa: E402

PERIODS = base.PERIODS
GROUPS = base.GROUPS
GRIDS = ('M', 'D', 'M_pow', 'D_pow', 'D_pow2')
CORRECTED = ('D', 'D_pow', 'D_pow2')
QUOTES = ('QPROP', 'QPOW')
# Every grid's own uncorrected grid (the price basis of the events its own tier would create).
OWN_BASIS = {'D_pow': 'M_pow', 'D_pow2': 'M_pow'}
# PR #182's favourite bands, plus the two groups of the problem statement.
BANDS = (*((f'under {high:.0%}' if not low else f'{low:.0%}+' if high == 1.0 else f'{low:.0%}-{high:.0%}', low, high)
           for low, high in zip(base.FAVOURITE_EDGES, base.FAVOURITE_EDGES[1:])),
         ('no side above 50%', 0.0, 0.5), ('favourite above 50%', 0.5, 1.0))
EVENT_RULE = base.EVENT_RULE
V3 = 'slopes-0.90-1.10-or-closer-than-baseline-bands-30-5pp-bonferroni-v3'


def models() -> dict:
    """The correction behind each corrected grid, with the margin-removal method of its grid."""
    out = {'D': (nm.production_model(), mi.DEVIG_PROPORTIONAL),
           'D_pow': (nm.load(nm.CANDIDATE_VERSIONS[mi.DEVIG_POWER], nm.CANDIDATE_DIR), mi.DEVIG_POWER),
           'D_pow2': (nm.load(nm.ONE_X_TWO_VERSION, nm.CANDIDATE_DIR), mi.DEVIG_POWER)}
    for name, (model, method) in out.items():
        nm.require_method(model, method)
        assert (nm.one_x_two(model) is not None) == (name == 'D_pow2'), name
    # D_pow2 is D_pow's correction, coefficient for coefficient, plus the 1X2 rule.
    assert out['D_pow2'][0]['targets'] == out['D_pow'][0]['targets']
    return out


# ---------------------------------------------------------------------------
# Per-match work (no holdout or retrospective row ever reaches it)
# ---------------------------------------------------------------------------

def league_records(league, cache, cfg):
    warnings.filterwarnings('ignore')
    corrections = models()
    rule = eh.calibration_rules(cfg)[EVENT_RULE]
    data, _, _ = hb.load_history(Path(cache), league, {**cfg, 'test_end_exclusive': cfg['end_exclusive']})
    start, end = pd.Timestamp(cfg['test_start']), pd.Timestamp(cfg['holdout_start'])
    fixtures, records = [], []
    counts = {'outside_periods_skipped': 0, 'no_prices': 0, 'fit_failed': 0}
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
        try:
            grids = {'M': eh.market_matrix(prices), 'M_pow': eh.market_matrix(prices, mi.DEVIG_POWER)}
            for cand, (model, method) in corrections.items():
                grids[cand] = eh.cagey_matrix(grids['M' if method == mi.DEVIG_PROPORTIONAL else 'M_pow'], prices,
                                              model, method)
        except (ValueError, TypeError, KeyError):
            counts['fit_failed'] += 1
            continue  # every grid is compared on the same matches
        date = row.Date
        identity = {'league': league, 'date': date.date().isoformat(),
                    'week': f'{date.isocalendar().year}-W{date.isocalendar().week:02d}',
                    'fixture_key': '|'.join((league, date.date().isoformat(), row.HomeTeam, row.AwayTeam)),
                    'phase': name, 'market_book': book}
        hg, ag = int(row.FTHG), int(row.FTAG)
        quotes = {'QPROP': [float(v) for v in mi.devig_three_way(*prices['hda'])],
                  'QPOW': [float(v) for v in mi.devig_three_way(*prices['hda'], method=mi.DEVIG_POWER)]}
        records.extend(rb.score_fixture(identity, grids, hg, ag))
        records.extend(eh.score_1x2(identity, quotes, hg, ag))
        margin = hg - ag
        fixture = {**identity, 'margin': margin, 'outcome': 0 if margin > 0 else 1 if margin == 0 else 2, **quotes}
        inputs = {}
        for cand in GRIDS:
            grid = grids[cand]
            h, a = np.indices(grid.shape)
            fixture[cand] = [float(grid[h > a].sum()), float(grid[h == a].sum()), float(grid[h < a].sum())]
            inputs[cand] = eh.cagey_inputs(grid, prices, book, identity['week'], margin)
        fixture['narrow'] = {c: float(np.asarray(inputs[c]['margin_probs'])[np.abs(inputs[c]['margins']) <= 1].sum())
                             for c in GRIDS}
        # The declared events (side chosen by D, synthetic prices from M), and each candidate tier's own events.
        fixture['events'] = {'declared': base.fixture_events(inputs, 'D', 'M', rule),
                             **{'own_' + c: base.fixture_events(inputs, c, b, rule) for c, b in OWN_BASIS.items()}}
        fixtures.append(fixture)
    return fixtures, records, counts


# ---------------------------------------------------------------------------
# Statistics
# ---------------------------------------------------------------------------

def pair(sub, baseline, candidate):
    """Baseline minus candidate log loss (positive = candidate better), whole weeks resampled, with whether the
    interval is clear of zero on either side."""
    out = eh.paired(sub, baseline, candidate)
    if out is None:
        return None
    interval = out['interval_95']
    out['clearly_better'] = bool(interval and interval[0] > 0)
    out['clearly_worse'] = bool(interval and interval[1] < 0)
    return out


def log_loss_section(scores, keys):
    part = scores.loc[scores.fixture_key.isin(keys)]
    out = {}
    for group in GROUPS:
        sub = part.loc[part.group == group]
        means = sub.groupby('candidate').log_loss.mean()
        entry = {'mean': {c: float(means[c]) for c in (*GRIDS, *QUOTES) if c in means},
                 'D_minus': {c: pair(sub, 'D', c) for c in GRIDS if c != 'D'},
                 'D_pow_minus_D_pow2': pair(sub, 'D_pow', 'D_pow2'),
                 'M_pow_minus': {c: pair(sub, 'M_pow', c) for c in ('D_pow', 'D_pow2')}}
        if group == '1X2':
            entry['QPOW_minus'] = {c: pair(sub, 'QPOW', c) for c in GRIDS}
        out[group] = entry
    return out


def calibration_1x2(fx, rules):
    rows = {c: [{'fixture_key': f['fixture_key'], 'probs': f[c], 'outcome': f['outcome']} for f in fx]
            for c in (*GRIDS, *QUOTES)}
    out = {}
    for cand in rows:
        v2 = eh.calibration_check(rows[cand], rules['v2'])
        entry = {'slopes': eh._slopes(rows[cand], ('home', 'draw', 'away')),
                 'mean_forecast': [float(v) for v in np.mean([r['probs'] for r in rows[cand]], axis=0)],
                 'v2_passes': v2['passes'], 'v2_slopes_pass': v2['slopes_pass'], 'v2_failing_bands': v2['failing_bands']}
        for other in ('D', 'D_pow'):
            if cand != other:
                v3 = eh.calibration_check(rows[cand], rules['v3'], baseline_rows=rows[other])
                entry[f'v3_vs_{other}'] = {'passes': v3['passes'], 'slopes_pass': v3['slopes_pass'],
                                           'closer_to_one': v3['relative_slopes']['closer_to_one_than_baseline'],
                                           'failing_bands': v3['failing_bands']}
        out[cand] = entry
    out['observed'] = [float(np.mean([f['outcome'] == k for f in fx])) for k in range(3)]
    return out


FAMILY_KEYS = ('events', 'fixtures', 'mean_forecast', 'baseline_mean_forecast', 'observed_rate', 'slope',
               'baseline_slope', 'slope_in_band', 'closer_to_one_than_baseline', 'slope_passes', 'bands_checked',
               'band_z_threshold', 'failing_bands', 'passes')


def events_check(events, rule, cand, against):
    check = eh.cagey_events_check(events, rule, cand, against)
    return {'passes': check['passes'],
            'families': {fam: {k: v[k] for k in FAMILY_KEYS if k in v} for fam, v in check['families'].items()}}


def event_log_loss(part, cand, against):
    p, y = part[f'p_{cand}'].clip(1e-15, 1 - 1e-15), part.y
    q = part[f'p_{against}'].clip(1e-15, 1 - 1e-15)
    loss = -(y * np.log(p) + (1 - y) * np.log(1 - p))
    gain = -(y * np.log(q) + (1 - y) * np.log(1 - q)) - loss
    return {'mean': float(loss.mean()), 'gain': base.week_mean(part.assign(gain=gain), 'gain')}


def events_section(fx, rule):
    """Rule cagey-events-v1. `declared_events`: the rule's own events (side by D, prices from M), every grid scored
    on them, judged against M (the rule), D and D_pow. `own_events`: D_pow and D_pow2 on the events their own
    tier would create (side by the candidate, prices from M_pow), against M_pow, D and each other."""
    declared = base.events_frame(fx, 'declared')
    out = {'declared_events': {}, 'own_events': {}}
    for cand in GRIDS:
        entry = {f'against_{b}': events_check(declared, rule, cand, b) for b in ('M', 'D', 'D_pow') if b != cand}
        entry['log_loss'] = {family: {**{f'{b}_minus_candidate': event_log_loss(
            declared.loc[declared.family == family], cand, b)['gain'] for b in ('D', 'D_pow') if b != cand},
            'mean': event_log_loss(declared.loc[declared.family == family], cand, 'D')['mean']}
            for family in rule['families']}
        out['declared_events'][cand] = entry
    for cand, basis in OWN_BASIS.items():
        own = base.events_frame(fx, 'own_' + cand)
        out['own_events'][cand] = {f'against_{b}': events_check(own, rule, cand, b)
                                   for b in (basis, 'D', *(c for c in OWN_BASIS if c != cand))}
        sides = own.loc[own.family == 'no_loss'].drop_duplicates('fixture_key').side.value_counts()
        out['own_events'][cand]['no_loss_sides'] = {k: int(v) for k, v in sides.items()}
    return out


def band_frame(fx):
    rows = []
    for f in fx:
        q = f['QPOW']
        side = 0 if q[0] >= q[2] else 2
        rows.append({'week': f['week'], 'phase': f['phase'], 'f': q[side], 'won': int(f['outcome'] == side),
                     'drawn': int(f['outcome'] == 1),
                     **{f'fav_{c}': f[c][side] for c in (*GRIDS, *QUOTES)},
                     **{f'draw_{c}': f[c][1] for c in (*GRIDS, *QUOTES)}})
    return pd.DataFrame(rows)


def gap(part, observed, forecast):
    """Observed rate minus mean forecast, whole weeks resampled."""
    value = base.week_mean(part.assign(gap=part[observed] - part[forecast]), 'gap')
    return {'forecast': float(part[forecast].mean()), 'observed_minus_forecast': value['mean'],
            'interval_95': value['interval_95'], 'clear_of_zero': value.get('clear_of_zero')}


def favourite_bands(fx):
    """Favourite-win and draw calibration by favourite band: the favourite is the likelier of home and away under
    the power quote, grouped by that quote's probability for it."""
    frame = band_frame(fx)
    out = []
    for label, low, high in BANDS:
        part = frame.loc[(frame.f >= low) & (frame.f < high)]
        if part.empty:
            continue
        n = len(part)
        won, drawn = base.week_mean(part, 'won'), base.week_mean(part, 'drawn')
        out.append({'band': label, 'fixtures': n,
                    'won': won['mean'], 'won_interval_95': won['interval_95'],
                    'won_binomial_95': [float(won['mean'] + s * 1.959964 * math.sqrt(won['mean'] * (1 - won['mean']) / n))
                                        for s in (-1, 1)],
                    'drawn': drawn['mean'], 'drawn_interval_95': drawn['interval_95'],
                    'favourite': {c: gap(part, 'won', f'fav_{c}') for c in (*GRIDS, *QUOTES)},
                    'draw': {c: gap(part, 'drawn', f'draw_{c}') for c in (*GRIDS, *QUOTES)}})
    return out


def narrow_section(fx):
    y = np.array([abs(f['margin']) <= 1 for f in fx], float)
    return {'observed': float(y.mean()), 'forecast': {c: float(np.mean([f['narrow'][c] for f in fx])) for c in GRIDS},
            'D_pow2_minus_D_pow_mean_abs': float(np.mean([abs(f['narrow']['D_pow2'] - f['narrow']['D_pow'])
                                                          for f in fx]))}


def uplift_section(fx, spec):
    """What the 1X2 rule does to the power quote and to D_pow's 1X2, on the matches scored."""
    q = np.array([f['QPOW'] for f in fx])
    d_pow, d_pow2 = np.array([f['D_pow'] for f in fx]), np.array([f['D_pow2'] for f in fx])
    target = np.array([nm.one_x_two_target(spec, *row) for row in q])
    return {'a': spec['a'], 'b': spec['b'],
            'grid_equals_target_max_abs': float(np.abs(d_pow2 - target).max()),
            'draw_minus_quote_mean': float((d_pow2[:, 1] - q[:, 1]).mean()),
            'draw_minus_quote_range': [float((d_pow2[:, 1] - q[:, 1]).min()), float((d_pow2[:, 1] - q[:, 1]).max())],
            'draw_minus_D_pow_mean': float((d_pow2[:, 1] - d_pow[:, 1]).mean()),
            'draw_minus_D_pow_range': [float((d_pow2[:, 1] - d_pow[:, 1]).min()), float((d_pow2[:, 1] - d_pow[:, 1]).max())],
            'logit_shift_at_f': {f'{f:.2f}': spec['a'] + spec['b'] * (f - 0.5) for f in (0.35, 0.5, 0.65, 0.8, 0.9)}}


def reproduction(fx, scores, harness_scores):
    """The problem statement's figures, with D and QPOW, on development and validation together."""
    bands = {b['band']: b for b in favourite_bands(fx)}
    keys = {f['fixture_key'] for f in fx}
    sub = scores.loc[scores.fixture_key.isin(keys) & scores.group.eq('1X2')]
    own = pair(sub, 'QPOW', 'D')
    hs = harness_scores.loc[harness_scores.fixture_key.isin(keys) & harness_scores.group.eq('1X2')]
    harness = pair(hs, 'QPOW', 'D')
    pick = lambda b, kind, c: bands[b][kind][c]['forecast']  # noqa: E731
    above, level, strong = bands['favourite above 50%'], bands['no side above 50%'], bands['70%-80%']
    return {
        'fixtures': len(fx),
        'favourites_above_50': {'fixtures': above['fixtures'], 'quote': pick('favourite above 50%', 'favourite', 'QPOW'),
                                'D': pick('favourite above 50%', 'favourite', 'D'), 'won': above['won'],
                                'won_interval_95_weeks': above['won_interval_95'],
                                'won_interval_95_binomial': above['won_binomial_95']},
        'D_minus_QPOW_1x2_log_loss': {'mean': -own['mean_gain'], 'interval_95': [-own['interval_95'][1], -own['interval_95'][0]],
                                      'fixtures': own['fixtures'],
                                      'from_harness_scores': {'mean': -harness['mean_gain'],
                                                              'interval_95': [-harness['interval_95'][1], -harness['interval_95'][0]],
                                                              'fixtures': harness['fixtures']}},
        'draws_no_side_above_50': {'fixtures': level['fixtures'], 'observed': level['drawn'],
                                   'D': pick('no side above 50%', 'draw', 'D'),
                                   'quote': pick('no side above 50%', 'draw', 'QPOW')},
        'draws_70_80': {'fixtures': strong['fixtures'], 'observed': strong['drawn'],
                        'quote': pick('70%-80%', 'draw', 'QPOW'), 'D': pick('70%-80%', 'draw', 'D')}}


def choice_rule(periods):
    """docs/plan.md, 3b-2: D_pow2 replaces D_pow only if all four conditions hold (written before any D_pow2
    figure was computed). Applied to the harness cohort."""
    dev, val = periods['development']['harness'], periods['validation']['harness']

    def events_pass(period, cand):
        return bool(period['cagey_events']['declared_events'][cand]['against_M']['passes'])

    def ah(period, key, cand=None):
        entry = period['log_loss']['AH all'][key]
        return entry[cand] if cand else entry

    above = next(b for b in val['favourite_bands'] if b['band'] == 'favourite above 50%')
    gaps = {c: abs(above['favourite'][c]['observed_minus_forecast']) for c in ('D_pow', 'D_pow2')}
    harm = {g: val['log_loss'][g]['D_pow_minus_D_pow2'] for g in ('AH draw-sensitive', '1X2', 'Over 1.5')}
    conditions = {
        '1_events': {'development': events_pass(dev, 'D_pow2'), 'validation': events_pass(val, 'D_pow2')},
        '2_release_metric': {
            'validation_D_pow_minus_D_pow2_AH_all': ah(val, 'D_pow_minus_D_pow2')['mean_gain'],
            'validation_no_worse_than_D_pow': bool(ah(val, 'D_pow_minus_D_pow2')['mean_gain'] >= 0),
            'validation_not_clearly_worse_than_D': not ah(val, 'D_minus', 'D_pow2')['clearly_worse'],
            'development_not_clearly_worse_than_D_pow': not ah(dev, 'D_pow_minus_D_pow2')['clearly_worse']},
        '3_no_clear_harm_validation': {g: not v['clearly_worse'] for g, v in harm.items()},
        '4_purpose_validation_favourites_above_50': {
            'fixtures': above['fixtures'], 'won': above['won'], 'abs_gap': gaps,
            'D_pow2_closer': bool(gaps['D_pow2'] < gaps['D_pow'])}}
    passed = {'1_events': all(conditions['1_events'].values()),
              '2_release_metric': all(v for k, v in conditions['2_release_metric'].items() if isinstance(v, bool)),
              '3_no_clear_harm_validation': all(conditions['3_no_clear_harm_validation'].values()),
              '4_purpose_validation_favourites_above_50': conditions['4_purpose_validation_favourites_above_50']['D_pow2_closer']}
    d_pow_ok = bool(events_pass(val, 'D_pow') and not ah(val, 'D_minus', 'D_pow')['clearly_worse'])
    chosen = 'D_pow2' if all(passed.values()) else 'D_pow' if d_pow_ok else None
    return {'conditions': conditions, 'passed': passed, 'D_pow_meets_3b_validation_check': d_pow_ok, 'chosen': chosen}


def model_record(model):
    return {**{k: model.get(k) for k in ('version', 'devig_method', 'training_first_date', 'training_last_date',
                                         'training_until_exclusive', 'training_matches', 'training_fingerprint',
                                         'one_x_two')},
            'targets': {g: {k: t[k] for k in ('intercept', 'coefficients', 'training_log_loss')}
                        for g, t in model['targets'].items()}}


def historical(args, cfg):
    rules = {'v2': cfg['calibration_tolerance'], 'v3': eh.calibration_rules(cfg)[V3]}
    event_rule = eh.calibration_rules(cfg)[EVENT_RULE]
    corrections = models()
    leagues = cfg['leagues']
    with ProcessPoolExecutor(max_workers=args.workers) as pool:
        parts = list(pool.map(league_records, leagues, [args.cache] * len(leagues), [cfg] * len(leagues)))
    fixtures = [f for p in parts for f in p[0]]
    records = [r for p in parts for r in p[1]]
    counts = {k: sum(p[2][k] for p in parts) for k in parts[0][2]}
    assert all(f['phase'] in PERIODS for f in fixtures)
    scores = eh.fixture_scores(records, cfg['draw_sensitive_lines'])

    harness = pd.read_csv(args.harness_output / 'fixture_scores.csv')
    assert not harness.phase.eq('holdout').any(), 'the harness output must come from a locked run'
    hd = harness.loc[harness.candidate.isin(['M', 'D', 'QPOW', 'QPROP']) & harness.phase.isin(PERIODS)]
    harness_keys = set(hd.loc[hd.candidate == 'D', 'fixture_key'])
    # The recomputed D, M and quote references must equal the harness's own scores on every match it scored.
    merged = hd.merge(scores, on=['fixture_key', 'candidate', 'group'], suffixes=('_harness', ''))
    consistency = {'harness_D_fixtures': len(harness_keys), 'matches_compared': int(merged.fixture_key.nunique()),
                   'rows_compared': {k: int(v) for k, v in merged.candidate.value_counts().items()},
                   'max_abs_log_loss_difference': float((merged.log_loss - merged.log_loss_harness).abs().max()),
                   'harness_fixtures_without_every_grid': len(harness_keys - {f['fixture_key'] for f in fixtures})}
    assert consistency['max_abs_log_loss_difference'] < 1e-12, consistency
    results = json.loads((args.harness_output / 'results.json').read_text(encoding='utf-8'))
    summary = {'script': 'scripts/cagey_dpow2_report.py', 'harness_commit': results.get('source_commit'),
               'config_sha256': results.get('config_sha256'), 'counts': counts,
               'consistency_with_harness': consistency, 'grids': list(GRIDS),
               'correction_models': {c: model_record(m) for c, (m, _) in corrections.items()}, 'periods': {}}
    spec = corrections['D_pow2'][0]['one_x_two']
    for name in (*PERIODS, 'development+validation'):
        fx_all = [f for f in fixtures if f['phase'] == name or name == 'development+validation']
        cohorts = {'harness': [f for f in fx_all if f['fixture_key'] in harness_keys], 'all_priced': fx_all}
        summary['periods'][name] = {}
        for cohort, fx in cohorts.items():
            keys = {f['fixture_key'] for f in fx}
            entry = {'fixtures': len(fx), 'weeks': len({f['week'] for f in fx}),
                     'favourite_bands': favourite_bands(fx), 'uplift': uplift_section(fx, spec)}
            if name in PERIODS:
                entry.update(log_loss=log_loss_section(scores, keys), calibration_1x2=calibration_1x2(fx, rules),
                             narrow=narrow_section(fx), cagey_events=events_section(fx, event_rule))
            else:
                entry['reproduction'] = reproduction(fx, scores, hd)
            summary['periods'][name][cohort] = entry
    summary['choice_rule'] = choice_rule(summary['periods'])
    args.output.mkdir(parents=True, exist_ok=True)
    (args.output / 'summary.json').write_text(json.dumps(summary, indent=2, sort_keys=True, default=float) + '\n',
                                              encoding='utf-8')
    print(json.dumps({'counts': counts, 'consistency_with_harness': consistency,
                      'choice_rule': summary['choice_rule']}, indent=2, default=float))
    return 0


# ---------------------------------------------------------------------------
# Live replay (integration check; no result is read)
# ---------------------------------------------------------------------------

LIVE_PAIRS = (('D', 'D_pow'), ('D', 'D_pow2'), ('D_pow', 'D_pow2'))


def side_split(baseline, candidate):
    """How the cagey no-loss probability moves on Asian handicap offers, by the sign of the offer's line: the side
    receives goals (plus), gives goals (minus) or neither (level)."""
    import price_edge_cagey_shortlist as v28
    a, b = baseline[0], candidate[0]
    column = v28.tier_no_loss_column(a)
    change = pd.to_numeric(base._column(b, column), errors='coerce') - pd.to_numeric(base._column(a, column), errors='coerce')
    line = pd.to_numeric(base._column(a, 'handicap_line'), errors='coerce')
    out = {}
    for name, mask in (('plus', line > 0), ('level', line == 0), ('minus', line < 0)):
        part = change[mask & change.notna()]
        out[name] = {'offers': int(len(part)), 'sum_change': float(part.sum())}
    return out


def live(args):
    import price_edge_cagey_shortlist as v28
    import shortlist_window
    from scripts.master_reconciliation_replay import runs
    corrections = models()
    base_settings = {**v28.load_settings(), 'shortlist_lookahead_hours': shortlist_window.DEFAULT_HOURS}
    report = {'script': 'scripts/cagey_dpow2_report.py --mode live', 'start': args.start, 'end_exclusive': args.end,
              'safe_no_loss': base.SAFE_NO_LOSS, 'note': 'Integration check: no result is read.',
              'pairs': [f'{a}->{b}' for a, b in LIVE_PAIRS], 'runs': []}
    out_root = args.output / 'live_runs'
    for generated, directory, _ in runs(ROOT, args.start, args.end):
        predictions = pd.read_csv(directory / 'predictions.csv', low_memory=False)
        built, entry = {}, {'snapshot': directory.name, 'generated_at_utc': generated}
        for cand, (model, method) in corrections.items():
            settings = base_settings if method == mi.DEVIG_PROPORTIONAL else {**base_settings, 'devig_method': method}
            built[cand] = base.build_variant(predictions, generated, settings, model, out_root / cand / directory.name)
        if args.check_default:
            entry['default_identical'] = base.check_default(predictions, generated, built['D'], directory.name)
        decisions = built['D'][0]
        entry['offers'] = int(len(decisions))
        p = pd.to_numeric(base._column(decisions, v28.tier_no_loss_column(decisions)), errors='coerce')
        entry['offers_with_cagey_no_loss'] = int(p.notna().sum())
        entry['pairs'] = {f'{a}->{b}': base.compare_run(built[a], built[b], directory.name) for a, b in LIVE_PAIRS}
        entry['by_side'] = {f'{a}->{b}': side_split(built[a], built[b]) for a, b in LIVE_PAIRS}
        report['runs'].append(entry)
        print(directory.name, entry['offers'], flush=True)
    report['totals'] = {}
    for a, b in LIVE_PAIRS:
        key = f'{a}->{b}'
        totals = base.run_totals([r['pairs'][key] for r in report['runs']])
        sides = {}
        for name in ('plus', 'level', 'minus'):
            offers = sum(r['by_side'][key][name]['offers'] for r in report['runs'])
            total = sum(r['by_side'][key][name]['sum_change'] for r in report['runs'])
            sides[name] = {'offers': offers, 'mean_change': total / offers if offers else None}
        report['totals'][key] = {**totals, 'no_loss_mean_change_by_line_sign': sides}
    report['runs_with_offers'] = sum(r['offers'] > 0 for r in report['runs'])
    report['default_identical_in_every_run'] = (all(r.get('default_identical') for r in report['runs'])
                                                if args.check_default else None)
    args.output.mkdir(parents=True, exist_ok=True)
    (args.output / 'live_replay.json').write_text(json.dumps(report, indent=2, sort_keys=True, default=float) + '\n',
                                                  encoding='utf-8')
    print(json.dumps({'runs': len(report['runs']), 'totals': report['totals']}, indent=2, default=float))
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
