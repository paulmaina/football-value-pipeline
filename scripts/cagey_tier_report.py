"""Phase 3 check of the cagey tier: D (market grid plus the narrow-margin correction) against M (the plain
market fit), on the harness's historical matches. Offline only; changes no logic and no production file.

D and M are exactly the harness's candidates (evaluation_harness.market_matrix and cagey_matrix on the
period bookmaker's pre-match prices; Pinnacle to 15 Jan 2026, Bet365 after). For every scored match this
script reports, per period:

  * log loss on AH settlement (all lines, draw-sensitive lines), 1X2 and Over 1.5, M minus D (positive = D
    better), whole calendar weeks resampled, 95% intervals (evaluation_harness.paired);
  * calibration of the probabilities the cagey tier uses: P(narrow) = P(|margin| <= 1), P(no loss) for each
    side and AH line, and 1X2 (calibration rule v3 with M as the baseline, plus v2 for reference);
  * the subset the cagey tier's rule (no-loss-market-reference-v5) selects among the prices the files
    carry: predicted against observed no-loss rate and flat-stake return (reported, never decisive).

Periods: development (in-sample for the correction, which was fitted on Pinnacle closing prices from
6 Aug 2021 to 1 Jun 2025; reported for completeness), validation (out-of-sample; the main evidence) and
retrospective (Bet365; already inspected; diagnostic). LOCKED: a holdout match is skipped before its result
or prices are read, and the script never scores the holdout.

Two cohorts: `harness` (the matches where the harness scores D: it also needs both teams in the research
model's fold, so newly promoted teams are left out) and `all_priced` (every match with valid prices).

    python scripts/cagey_tier_report.py --harness-output <dir of a locked evaluation_harness.py run> \
        --output evaluation/cagey_tier_check
"""
from __future__ import annotations

import argparse
import json
import math
import sys
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import evaluation_harness as eh  # noqa: E402
import historical_benchmark as hb  # noqa: E402
import research_backtest as rb  # noqa: E402

PERIODS = ('development', 'validation', 'retrospective')
GROUPS = ('AH all', 'AH draw-sensitive', '1X2', 'Over 1.5')
LINES = tuple(i / 4 for i in range(-8, 10))  # -2.00 .. +2.25: every line in rb.AH_LINES plus the tier's +2.25
SIDES = ('home', 'away')
PLUS_LINES = (1.0, 1.25, 1.5, 1.75, 2.0, 2.25)  # price_edge_cagey_shortlist.TIER_LINES
MIN_ODDS, MAX_ODDS = 1.15, 2.00  # no-loss-market-reference-v5 odds window (cagey_tier_v3.annotate)
GUARD_RATIO = 1.15                # price above 1.15 x corrected fair odds is rejected (AH lines)
SAMPLES, SEED = 2000, 136


# ---------------------------------------------------------------------------
# Per-match work (no holdout row ever reaches it)
# ---------------------------------------------------------------------------

def margin_distribution(matrix):
    import market_implied as mi
    margins, probs = mi.margin_distribution(matrix)
    return np.asarray(margins, int), np.asarray(probs, float)


def no_loss(margins, probs, side, line):
    from ah_close_backtest import outcome_probabilities
    side_margins = margins if side == 'home' else -margins
    out = outcome_probabilities(side_margins, probs, line)
    return float(out['p_win'] + out['p_half_win'] + out['p_push']), out


def settles(margin, side, line):
    from ah_close_backtest import settle
    won, lost = settle(margin if side == 'home' else -margin, line)
    return float(won), float(lost)


def offers(row, book):
    """Real quoted cagey-tier markets in the files: Home win, Away win (1X2) and the main AH line, both
    sides. The files carry no double-chance, Over 1.5 or alternate AH prices."""
    cols = eh.BOOKS[book]
    hda = [float(row[c]) for c in cols['hda']]
    line, home, away = (float(row[c]) for c in cols['ah'])
    return [('match_winner', 'Home win', 'home', -0.5, hda[0]), ('match_winner', 'Away win', 'away', -0.5, hda[2]),
            ('asian_handicap', f'AH home {line:+.2f}', 'home', line, home),
            ('asian_handicap', f'AH away {-line:+.2f}', 'away', -line, away)]


def league_records(league, cache, cfg):
    import narrow_margin as nm
    model = nm.production_model()
    data, _, _ = hb.load_history(Path(cache), league, {**cfg, 'test_end_exclusive': cfg['end_exclusive']})
    start, end = pd.Timestamp(cfg['test_start']), pd.Timestamp(cfg['end_exclusive'])
    fixtures, records, counts = [], [], {'holdout_skipped': 0, 'no_prices': 0, 'fit_failed': 0}
    for _, row in data.loc[(data.Date >= start) & (data.Date < end)].iterrows():
        name = eh.phase(row.Date, league, cfg)
        if name == 'holdout':
            # Skipped before its prices or result are read.
            counts['holdout_skipped'] += 1
            continue
        book = eh.period_book(row.Date, cfg)
        prices = eh.book_prices(row, book)
        if prices is None:
            counts['no_prices'] += 1
            continue
        try:
            grids = {'M': eh.market_matrix(prices)}
            grids['D'] = eh.cagey_matrix(grids['M'], prices, model)
        except (ValueError, TypeError, KeyError):
            counts['fit_failed'] += 1
            continue
        date = row.Date
        identity = {'league': league, 'date': date.date().isoformat(),
                    'week': f'{date.isocalendar().year}-W{date.isocalendar().week:02d}',
                    'fixture_key': '|'.join((league, date.date().isoformat(), row.HomeTeam, row.AwayTeam)),
                    'phase': name, 'market_book': book}
        hg, ag = int(row.FTHG), int(row.FTAG)
        records.extend(rb.score_fixture(identity, grids, hg, ag))
        margin = hg - ag
        fixture = {**identity, 'margin': margin, 'outcome': 0 if margin > 0 else 1 if margin == 0 else 2,
                   'overround_hda': sum(1 / p for p in prices['hda']) - 1,
                   'overround_ah': sum(1 / p for p in prices['ah'][1:]) - 1,
                   'offers': offers(row, book), 'hda_prices': list(prices['hda']),
                   'ah_prices': list(prices['ah'])}
        for cand, grid in grids.items():
            margins, probs = margin_distribution(grid)
            h, a = np.indices(grid.shape)
            fixture[cand] = {'hda': [float(grid[h > a].sum()), float(grid[h == a].sum()), float(grid[h < a].sum())],
                             'narrow': float(probs[np.abs(margins) <= 1].sum()),
                             'margins': margins.tolist(), 'probs': probs.tolist()}
        fixtures.append(fixture)
    return fixtures, records, counts


# ---------------------------------------------------------------------------
# Statistics
# ---------------------------------------------------------------------------

def week_interval(frame, value, weight=None, samples=SAMPLES, seed=SEED):
    """Mean of `value` (weighted by `weight` if given) with whole weeks resampled."""
    if frame.empty:
        return None
    w = frame[weight] if weight else pd.Series(1.0, index=frame.index)
    weeks = pd.DataFrame({'s': frame[value] * w, 'n': w, 'week': frame.week}).groupby('week')[['s', 'n']].sum()
    mean = float(weeks.s.sum() / weeks.n.sum())
    if len(weeks) < 2:
        return {'mean': mean, 'interval_95': None, 'weeks': len(weeks)}
    draws = np.random.default_rng(seed).integers(0, len(weeks), size=(samples, len(weeks)))
    means = weeks.s.to_numpy()[draws].sum(1) / weeks.n.to_numpy()[draws].sum(1)
    return {'mean': mean, 'interval_95': [float(v) for v in np.quantile(means, [.025, .975])], 'weeks': len(weeks)}


def bands(p, y, width=0.1, minimum=30):
    p, y = np.asarray(p, float), np.asarray(y, float)
    nbins = int(round(1 / width))
    index = np.minimum(nbins - 1, (p * nbins).astype(int))
    out = []
    for b in np.unique(index):
        m = index == b
        if m.sum() >= minimum:
            n, mean, obs = int(m.sum()), float(p[m].mean()), float(y[m].mean())
            se = math.sqrt(mean * (1 - mean) / n)
            out.append({'band_lower': b / nbins, 'n': n, 'mean_forecast': mean, 'observed_rate': obs,
                        'observed_minus_forecast': obs - mean, 'z': abs(obs - mean) / se if se > 0 else float('inf')})
    return out


def binary_check(p, y, base_p, rule):
    """Calibration rule v3 applied to one binary event (the slope of the event itself; bands as v2), with the
    baseline's slope on the same forecasts. Not a configured rule: reported, never a gate."""
    slope = eh.calibration_slope(p, y)
    base = eh.calibration_slope(base_p, y)
    found = bands(p, y, rule['band_width'], rule['band_min_matches'])
    return {'slope': slope, 'baseline_slope': base, 'in_band': bool(rule['slope_min'] <= slope <= rule['slope_max']),
            'closer_to_one_than_baseline': bool(abs(slope - 1) < abs(base - 1)), 'bands': found,
            'forecasts': len(p), 'mean_forecast': float(np.mean(p)), 'observed_rate': float(np.mean(y)),
            'baseline_mean_forecast': float(np.mean(base_p))}


def finish_binary(checks, rule):
    """Bonferroni over every band checked in the family; a band fails when > 5 points AND clear."""
    total = sum(len(c['bands']) for c in checks.values())
    bar = eh.band_z_threshold(rule['band_alpha'], total) if total else None
    for c in checks.values():
        failing = [b for b in c['bands'] if abs(b['observed_minus_forecast']) > rule['band_max_deviation'] and b['z'] > bar]
        worst = max(c['bands'], key=lambda b: abs(b['observed_minus_forecast'])) if c['bands'] else None
        c.update(band_z_threshold=bar, bands_checked_in_family=total, failing_bands=failing, worst_band=worst,
                 slope_passes=c['in_band'] or c['closer_to_one_than_baseline'],
                 passes=bool((c['in_band'] or c['closer_to_one_than_baseline']) and not failing))
        c['bands_pass'] = not failing
    return checks


def log_loss_section(scores, keys):
    part = scores.loc[scores.fixture_key.isin(keys)]
    out = {}
    for group in GROUPS:
        sub = part.loc[part.group == group]
        means = sub.groupby('candidate').log_loss.mean()
        out[group] = {'M': float(means.get('M', np.nan)), 'D': float(means.get('D', np.nan)),
                      'M_minus_D': eh.paired(sub, 'M', 'D')}
    return out


def calibration_section(fx, rules):
    v2, v3 = rules['v2'], rules['v3']
    rows = {c: [{'fixture_key': f['fixture_key'], 'probs': f[c]['hda'], 'outcome': f['outcome']} for f in fx]
            for c in ('M', 'D')}
    narrow_y = [int(abs(f['margin']) <= 1) for f in fx]
    narrow = finish_binary({'P(narrow)': binary_check([f['D']['narrow'] for f in fx], narrow_y,
                                                      [f['M']['narrow'] for f in fx], v3)}, v3)['P(narrow)']
    narrow['M_bands'] = bands([f['M']['narrow'] for f in fx], narrow_y, v3['band_width'], v3['band_min_matches'])
    bar = eh.band_z_threshold(v3['band_alpha'], len(narrow['M_bands'])) if narrow['M_bands'] else None
    narrow['M_band_z_threshold'] = bar
    narrow['M_failing_bands'] = [b for b in narrow['M_bands']
                                 if abs(b['observed_minus_forecast']) > v3['band_max_deviation'] and b['z'] > bar]
    lines = {}
    for side in SIDES:
        for line in LINES:
            p = {c: [] for c in ('M', 'D')}
            y = []
            for f in fx:
                won, lost = settles(f['margin'], side, line)
                y.append(int(lost == 0))
                for c in p:
                    p[c].append(no_loss(np.array(f[c]['margins']), np.array(f[c]['probs']), side, line)[0])
            lines[f'{side} {line:+.2f}'] = binary_check(p['D'], y, p['M'], v3)
            lines[f'{side} {line:+.2f}']['M_slope_in_band'] = bool(v3['slope_min'] <= lines[f'{side} {line:+.2f}']['baseline_slope'] <= v3['slope_max'])
    finish_binary(lines, v3)
    # Context, not declared beforehand: the no-loss event on the plus lines the cagey tier bets (+1.00 to +2.25,
    # either side), pooled. A fixture contributes up to twelve dependent events, so bands are not tested here;
    # the log loss difference resamples whole weeks.
    pooled = []
    for f in fx:
        for side in SIDES:
            for line in PLUS_LINES:
                won, lost = settles(f['margin'], side, line)
                p = {c: no_loss(np.array(f[c]['margins']), np.array(f[c]['probs']), side, line)[0] for c in ('M', 'D')}
                y = int(lost == 0)
                ll = {c: -math.log(max(p[c] if y else 1 - p[c], 1e-15)) for c in p}
                pooled.append({'week': f['week'], 'y': y, 'pM': p['M'], 'pD': p['D'], 'gain': ll['M'] - ll['D']})
    pooled = pd.DataFrame(pooled)
    plus = {'events': len(pooled), 'observed_rate': float(pooled.y.mean()), 'mean_forecast_D': float(pooled.pD.mean()),
            'mean_forecast_M': float(pooled.pM.mean()), 'slope_D': eh.calibration_slope(pooled.pD, pooled.y),
            'slope_M': eh.calibration_slope(pooled.pM, pooled.y),
            'log_loss_M_minus_D_per_event': week_interval(pooled, 'gain')}
    moved =float(np.mean([abs(f['D']['narrow'] - f['M']['narrow']) for f in fx]))
    return {'1X2': {'D_v3_vs_M': eh.calibration_check(rows['D'], v3, baseline_rows=rows['M']),
                    'D_v2': eh.calibration_check(rows['D'], v2), 'M_v2': eh.calibration_check(rows['M'], v2)},
            'P(narrow)': {**narrow, 'mean_abs_D_minus_M': moved},
            'P(no loss) by side and line': lines, 'P(no loss) plus lines +1.00 to +2.25, pooled (context)': plus}


def settle_return(won, lost, price):
    return won * (price - 1) - lost  # stake 1: full/half win pays (price-1) x share; loss share loses the stake


def selection_section(fx, cand, synthetic_margins=None):
    """The v5 rule on the files' real quoted markets: odds in (1.15, 2.00]; AH price guard against the
    candidate's own fair odds; one per fixture and market group (highest no-loss, then expected return,
    then odds). In the Bet365 period the offer is a synthetic Pinnacle-like price (Bet365 margin-free plus
    Pinnacle's average margin), indicative only."""
    picks = []
    for f in fx:
        margins, probs = np.array(f[cand]['margins']), np.array(f[cand]['probs'])
        offered = f['offers']
        if synthetic_margins is not None:
            from market_implied import devig_three_way
            h, d, a = devig_three_way(*f['hda_prices'])
            line, ph, pa = f['ah_prices']
            qh = (1 / ph) / (1 / ph + 1 / pa)
            prices = [1 / (h * (1 + synthetic_margins['hda'])), 1 / (a * (1 + synthetic_margins['hda'])),
                      1 / (qh * (1 + synthetic_margins['ah'])), 1 / ((1 - qh) * (1 + synthetic_margins['ah']))]
            offered = [(*o[:4], p) for o, p in zip(offered, prices)]
        best = {}
        for group, market, side, line, price in offered:
            if not MIN_ODDS < price <= MAX_ODDS:
                continue
            p_no_loss, out = no_loss(margins, probs, side, line)
            win, loss = out['p_win'] + out['p_half_win'] / 2, out['p_loss'] + out['p_half_loss'] / 2
            ev = win * (price - 1) - loss
            fair = 1 + loss / win if win > 0 else math.inf
            if group == 'asian_handicap' and price > GUARD_RATIO * fair:
                continue
            key = (-p_no_loss, -ev, -price)
            if group not in best or key < best[group][0]:
                won, lost = settles(f['margin'], side, line)
                best[group] = (key, {'fixture_key': f['fixture_key'], 'week': f['week'], 'group': group,
                                     'market': market, 'price': price, 'predicted_no_loss': p_no_loss,
                                     'expected_return': ev, 'no_loss': float(lost == 0),
                                     'return': settle_return(won, lost, price)})
        picks.extend(v for _, v in best.values())
    frame = pd.DataFrame(picks)
    out = {}
    for group, part in [('all', frame), *((g, frame.loc[frame.group == g]) for g in ('match_winner', 'asian_handicap'))]:
        if part.empty:
            out[group] = {'picks': 0}
            continue
        part = part.assign(gap=part.no_loss - part.predicted_no_loss)
        out[group] = {'picks': int(len(part)), 'fixtures': int(part.fixture_key.nunique()),
                      'mean_odds': float(part.price.mean()),
                      'predicted_no_loss': float(part.predicted_no_loss.mean()),
                      'observed_no_loss': float(part.no_loss.mean()),
                      'observed_minus_predicted': week_interval(part, 'gap'),
                      'mean_expected_return': float(part.expected_return.mean()),
                      'flat_stake_return': week_interval(part, 'return')}
    return out, frame


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('--cache', type=Path, default=ROOT / '.football_cache')
    parser.add_argument('--config', type=Path, default=eh.CONFIG)
    parser.add_argument('--harness-output', type=Path, required=True,
                        help='output of a locked evaluation_harness.py run (fixture_scores.csv, results.json)')
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--workers', type=int, default=8)
    args = parser.parse_args(argv)
    cfg = json.loads(args.config.read_text(encoding='utf-8'))
    rules = {'v2': cfg['calibration_tolerance'],
             'v3': eh.calibration_rules(cfg)['slopes-0.90-1.10-or-closer-than-baseline-bands-30-5pp-bonferroni-v3']}
    with ProcessPoolExecutor(max_workers=args.workers) as pool:
        parts = list(pool.map(league_records, cfg['leagues'], [args.cache] * len(cfg['leagues']),
                              [cfg] * len(cfg['leagues'])))
    fixtures = [f for p in parts for f in p[0]]
    records = [r for p in parts for r in p[1]]
    counts = {k: sum(p[2][k] for p in parts) for k in parts[0][2]}
    assert not any(f['phase'] == 'holdout' for f in fixtures)
    scores = eh.fixture_scores(records, cfg['draw_sensitive_lines'])

    harness = pd.read_csv(args.harness_output / 'fixture_scores.csv')
    assert not harness.phase.eq('holdout').any(), 'the harness output must come from a locked run'
    hd = harness.loc[harness.candidate.isin(['M', 'D'])]
    harness_keys = set(hd.loc[hd.candidate == 'D', 'fixture_key'])
    # The recomputed D and M must equal the harness's own scores on every match the harness scored.
    merged = hd.merge(scores, on=['fixture_key', 'candidate', 'group'], suffixes=('_harness', ''))
    consistency = {'matches_compared': int(merged.fixture_key.nunique()),
                   'harness_D_fixtures': len(harness_keys),
                   'max_abs_log_loss_difference': float((merged.log_loss - merged.log_loss_harness).abs().max())}
    assert consistency['matches_compared'] == len(harness_keys), consistency
    assert consistency['max_abs_log_loss_difference'] < 1e-12, consistency
    results = json.loads((args.harness_output / 'results.json').read_text(encoding='utf-8'))

    pre = [f for f in fixtures if f['phase'] in ('development', 'validation') and f['market_book'] == 'pinnacle']
    synthetic = {'hda': float(np.mean([f['overround_hda'] for f in pre])),
                 'ah': float(np.mean([f['overround_ah'] for f in pre]))}
    summary = {'script': 'scripts/cagey_tier_report.py', 'config_sha256': results.get('config_sha256'),
               'counts': counts, 'consistency_with_harness': consistency,
               'bet365_gap': {g: results['bet365_gap'][g]['bet365_minus_pinnacle_log_loss']
                              for g in results.get('bet365_gap', {})},
               'pinnacle_average_margin_pre_holdout': synthetic,
               'correction_model': {k: __import__('narrow_margin').production_model()[k] for k in
                                    ('version', 'training_first_date', 'training_last_date', 'training_matches')},
               'periods': {}}
    picks_out = []
    for name in PERIODS:
        fx_all = [f for f in fixtures if f['phase'] == name]
        cohorts = {'harness': [f for f in fx_all if f['fixture_key'] in harness_keys], 'all_priced': fx_all}
        summary['periods'][name] = {}
        for cohort, fx in cohorts.items():
            if not fx:
                continue
            keys = {f['fixture_key'] for f in fx}
            entry = {'fixtures': len(fx), 'weeks': len({f['week'] for f in fx}),
                     'market_book': sorted({f['market_book'] for f in fx}),
                     'log_loss': log_loss_section(scores, keys)}
            if cohort == 'harness':
                entry['calibration'] = calibration_section(fx, rules)
                entry['selection'], frames = {}, {}
                for cand in ('D', 'M'):
                    section, frames[cand] = selection_section(fx, cand, synthetic if name == 'retrospective' else None)
                    entry['selection'][cand] = section
                    picks_out.append(frames[cand].assign(phase=name, candidate=cand))
                same = frames['D'].merge(frames['M'], on=['fixture_key', 'group'], suffixes=('_D', '_M'))
                entry['selection']['agreement'] = {
                    'D_picks': int(len(frames['D'])), 'M_picks': int(len(frames['M'])),
                    'same_fixture_and_group': int(len(same)),
                    'same_market': int((same.market_D == same.market_M).sum())}
            summary['periods'][name][cohort] = entry
    args.output.mkdir(parents=True, exist_ok=True)
    (args.output / 'summary.json').write_text(json.dumps(summary, indent=2, sort_keys=True, default=float) + '\n',
                                              encoding='utf-8')
    pd.concat(picks_out).to_csv(args.output / 'selection_picks.csv', index=False)
    print(json.dumps({k: summary[k] for k in ('counts', 'consistency_with_harness')}, indent=2))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
