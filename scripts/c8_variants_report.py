"""C8 with a larger Dixon-Coles penalty or a season carry-over: each variant against C8, and the choice rule.

Reads a locked harness run made with the variants
(`python evaluation_harness.py --output DIR --rate-variants C8P1 C8P3 C8S70 C8S50`): development and
validation, with the retrospective period as a diagnostic. A holdout row anywhere aborts the report.

Declared before any variant score was computed (the commit that added the variants; docs/plan.md, Phase 2g,
"Penalty and season carry-over on top of C8"):
  - each variant is C8's procedure (rate calibration with Elo, then C2's (rho, delta), both refitted
    walk-forward) on goal rates from a fold Dixon-Coles fit with one setting changed: the penalty l2 (1 or 3,
    against 0.08) or the season carry-over (0.7 or 0.5, against 1.0);
  - the choice rule: a variant replaces C8 only if C8 minus variant on AH all lines is positive with its 95%
    interval clear of zero on development, the validation point estimate is not negative, and calibration
    rule v2 still passes on development (every forecast of the variant in the period). Otherwise C8 stands;
  - the combination: only if at least one setting of each kind qualifies, the pair of the qualifying
    settings (of each kind, the one with the larger development AH all gain) is run and judged by the same
    rule against C8;
  - the final candidate: the qualifying variant with the largest development AH all gain over C8; C8 when
    none qualifies;
  - reported for every variant: AH all lines, AH draw-sensitive lines (0, +/-0.5), 1X2 and Over 1.5 (C8
    minus variant: positive means the variant is better; whole calendar weeks resampled,
    evaluation_harness.paired), calibration, the standing diagnostics' thin-team (either team under 16
    training matches) and August-September segments, and predicted against actual goals by favourite
    strength (the standing diagnostics' bands of the favourite's market probability);
  - cohort: the standing diagnostics' common cohort that also has C8 and every variant in the run.

    python scripts/c8_variants_report.py --run DIR --output evaluation/c8_variants
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
VERSION = 'c8-variants-report-v1'
BASE = 'C8'
GROUPS = ('AH all', 'AH draw-sensitive', '1X2', 'Over 1.5')
PRIMARY = 'AH all'
PHASES = ('development', 'validation', 'retrospective')
EVIDENCE = ('development', 'validation')  # the retrospective period is a diagnostic only
SEGMENTS = (('training matches', 'either team under 16'), ('month', 'August-September'))
KINDS = {'penalty': 'l2', 'season carry-over': 'season_carry_over'}
FIT_FIELDS = ('a_home', 'a_away', 'b', 'c')


def kind(settings) -> str | None:
    """'penalty' or 'season carry-over' for a variant that changes one setting; None for a combination."""
    return next((k for k, field in KINDS.items() if set(settings) == {field}), None)


def compare(scores, keys, names) -> dict:
    """Mean log loss and C8-minus-variant differences on `keys`, per metric (C6 minus each view for context)."""
    import evaluation_harness as eh
    out = {}
    for group in GROUPS:
        part = scores.loc[(scores.group == group) & scores.fixture_key.isin(keys)]
        means = part.groupby('candidate').log_loss.mean()
        out[group] = {'fixtures': int(part.fixture_key.nunique()),
                      'mean_log_loss': {c: float(means[c]) for c in ('C6', BASE, *names, 'M') if c in means},
                      'c8_minus': {name: eh.paired(part, BASE, name) for name in names},
                      'c6_minus': {name: eh.paired(part, 'C6', name) for name in (BASE, *names)}}
    return out


def rows_of(forecasts, candidate) -> list:
    part = forecasts.loc[forecasts.candidate == candidate]
    return [{'fixture_key': k, 'probs': [h, d, a], 'outcome': int(o)} for k, h, d, a, o in
            part[['fixture_key', 'p_home', 'p_draw', 'p_away', 'outcome']].itertuples(index=False)]


def calibration(forecasts, cfg, views) -> dict:
    """Per view: levels, slopes and rule v2 on every forecast of the view in the period."""
    import evaluation_harness as eh
    out = {}
    for view in views:
        mine = rows_of(forecasts, view)
        if not mine:
            continue
        probs, outcome = np.array([r['probs'] for r in mine]), np.array([r['outcome'] for r in mine])
        out[view] = {'forecasts': len(mine),
                     'levels': {name: {'mean_forecast': float(probs[:, k].mean()),
                                       'observed_rate': float((outcome == k).mean()),
                                       'calibration_slope': eh.calibration_slope(probs[:, k], outcome == k)}
                                for k, name in enumerate(('home', 'draw', 'away'))},
                     'v2': eh.calibration_check(mine, cfg['calibration_tolerance'])}
    return out


def movement(forecasts, candidate) -> dict:
    wide = forecasts.loc[forecasts.candidate.isin([candidate, BASE])].pivot(
        index='fixture_key', columns='candidate', values=['p_home', 'p_draw', 'p_away'])
    moved = (wide.xs(candidate, level=1, axis=1) - wide.xs(BASE, level=1, axis=1)).abs().max(axis=1).dropna()
    return {'fixtures': int(len(moved)), 'mean_max_1x2_move_points': float(100 * moved.mean()),
            'p90_max_1x2_move_points': float(100 * moved.quantile(.9)), 'max_1x2_move_points': float(100 * moved.max())}


def segment_differences(scores, labels, keys, names) -> dict:
    """C8 minus variant inside the thin-team and August-September segments (and outside them)."""
    import evaluation_harness as eh
    out = {}
    for dimension, wanted in SEGMENTS:
        values = labels.loc[keys, dimension]
        for label in sorted(values.unique(), key=lambda v: v != wanted):
            inside = set(keys[(values == label).to_numpy()])
            part = scores.loc[scores.fixture_key.isin(inside)]
            out[label] = {'fixtures': len(inside),
                          'c8_minus': {name: {group: eh.paired(part.loc[part.group == group], BASE, name)
                                              for group in (PRIMARY, '1X2')} for name in names}}
    return out


def goals_by_favourite(goals, labels, forecasts, members, keys, views) -> list:
    """Predicted (the scored grid's expected goals) against actual goals, by the favourite's market probability.
    The favourite is the side M makes more likely to win. `supremacy` is favourite minus underdog goals."""
    import evaluation_diagnostics as ed
    market = ed._probabilities(forecasts, 'M').reindex(keys)
    home_favourite = (market.p_home >= market.p_away).to_numpy()
    bands = labels.loc[keys, 'favourite market probability']
    weeks = members.week.reindex(keys)
    rows = []
    for label in ('all', *ed.SEGMENT_ORDER['favourite market probability']):
        mask = np.ones(len(keys), bool) if label == 'all' else (bands == label).to_numpy()
        inside = keys[mask]
        entry = {'band': label, 'fixtures': int(mask.sum()), 'views': {}}
        for view in views:
            g = goals.loc[goals.candidate == view].set_index('fixture_key').reindex(inside)
            fav = home_favourite[mask]
            pick = lambda home, away: np.where(fav, g[home].to_numpy(), g[away].to_numpy())
            predicted = {'favourite': pick('expected_home_goals', 'expected_away_goals'),
                         'underdog': pick('expected_away_goals', 'expected_home_goals')}
            actual = {'favourite': pick('home_goals', 'away_goals'), 'underdog': pick('away_goals', 'home_goals')}
            if not len(inside) or np.isnan(predicted['favourite']).any():
                entry['views'][view] = None
                continue
            error = {side: predicted[side] - actual[side] for side in predicted}
            entry['views'][view] = {
                'predicted': {side: float(v.mean()) for side, v in predicted.items()},
                'actual': {side: float(v.mean()) for side, v in actual.items()},
                'predicted_minus_actual': {
                    'favourite': ed.week_mean(error['favourite'], weeks.loc[inside]),
                    'underdog': ed.week_mean(error['underdog'], weeks.loc[inside]),
                    'supremacy': ed.week_mean(error['favourite'] - error['underdog'], weeks.loc[inside]),
                    'total': ed.week_mean(error['favourite'] + error['underdog'], weeks.loc[inside])}}
        rows.append(entry)
    return rows


def walk_forward(results, views) -> dict:
    fits = {f['candidate']: f for f in results['folds'] if f.get('candidate')}
    out = {}
    for name in views:
        path = [{'origin': f['origin'], 'status': f['status'], 'matches': f['matches'],
                 **{k: f[k] for k in FIT_FIELDS}, 'rho': f['low_score']['rho'], 'delta': f['low_score']['delta'],
                 'low_score_status': f['low_score']['status']} for f in fits[name]['walk_forward_fits']]
        fitted = [f for f in path if f['status'] == 'fitted']
        low = [f for f in path if f['low_score_status'] == 'fitted']
        span = lambda key, rows: ({'min': float(min(r[key] for r in rows)), 'max': float(max(r[key] for r in rows)),
                                   'median': float(np.median([r[key] for r in rows])), 'last': float(rows[-1][key])}
                                  if rows else None)
        out[name] = {'settings': fits[name].get('settings', {}), 'windows': len(path),
                     'warm_up_windows': sum(f['status'] == 'warm_up' for f in path),
                     'failed_windows': sum(f['status'] == 'optimiser_failed' for f in path),
                     'ranges': {**{k: span(k, fitted) for k in FIT_FIELDS}, **{k: span(k, low) for k in ('rho', 'delta')}}}
    return out


def choose(report, variants) -> dict:
    """The declared choice rule on the report's figures. `variants` maps each variant in the run to its settings."""
    def verdict(name):
        development = report['development']['log_loss'][PRIMARY]['c8_minus'][name]
        validation = report['validation']['log_loss'][PRIMARY]['c8_minus'][name]
        v2 = report['development']['calibration'][name]['v2']
        conditions = {'development_ah_all_positive_and_clear': bool(development and development['clear_of_zero']),
                      'validation_ah_all_not_negative': bool(validation and validation['mean_gain'] >= 0),
                      'development_calibration_v2_passes': bool(v2['passes'])}
        return {'settings': variants[name], 'development_gain': development and development['mean_gain'],
                'development_interval_95': development and development['interval_95'],
                'validation_gain': validation and validation['mean_gain'],
                'development_slopes': v2['slopes'], 'conditions': conditions, 'qualifies': all(conditions.values())}

    def best(names):
        qualifying = [n for n in names if verdicts[n]['qualifies']]
        return max(qualifying, key=lambda n: verdicts[n]['development_gain']) if qualifying else None

    verdicts = {name: verdict(name) for name in variants}
    singles = {k: best([n for n in variants if kind(variants[n]) == k]) for k in KINDS}
    out = {'rule': 'C8 minus variant on AH all lines positive with its 95% interval clear of zero on development; '
                   'validation point estimate not negative; calibration rule v2 passes on development',
           'verdicts': verdicts, 'best_qualifying_setting': singles, 'combination': None,
           'combination_in_run': None}
    eligible = [n for n in variants if kind(variants[n])]
    if all(singles.values()):
        import evaluation_harness as eh
        wanted = {**variants[singles['penalty']], **variants[singles['season carry-over']]}
        out['combination'] = next(n for n, s in eh.RATE_VARIANTS.items() if s == wanted)
        out['combination_in_run'] = out['combination'] in variants
        if not out['combination_in_run']:
            return {**out, 'final_candidate': None,
                    'reading': f"The combination {out['combination']} must be run before a final candidate is named."}
        eligible.append(out['combination'])
    final = best(eligible)
    out['final_candidate'] = final or BASE
    out['reading'] = (f'{final} replaces C8.' if final else 'No variant qualifies: C8 stands unchanged.')
    return out


def build(run, cfg) -> dict:
    import evaluation_diagnostics as ed
    import evaluation_harness as eh
    results = json.loads((run / 'results.json').read_text(encoding='utf-8'))
    if results.get('mode') != 'historical':
        raise ValueError('Expected a locked historical run')
    scores = pd.read_csv(run / 'fixture_scores.csv')
    forecasts = pd.read_csv(run / 'forecasts_1x2.csv')
    fixtures = pd.read_csv(run / 'diagnostic_fixtures.csv')
    goals = pd.read_csv(run / 'rate_goals.csv')
    for frame in (scores, forecasts, fixtures, goals):
        if (frame.phase == 'holdout').any():
            raise ValueError('Holdout rows found; this report reads locked runs only')
    variants = {f['candidate']: f['settings'] for f in results['folds'] if f.get('candidate') in eh.RATE_VARIANTS}
    if not variants:
        raise ValueError('The run has no C8 variant: run evaluation_harness.py with --rate-variants')
    if any(eh.RATE_VARIANTS[name] != settings for name, settings in variants.items()):
        raise ValueError("The run's variant settings differ from evaluation_harness.RATE_VARIANTS")
    names = tuple(variants)
    views = (BASE, *names)
    standing = ed.cohort(scores)
    members = ed.cohort(scores, (*ed.COHORT, *views))
    labels = ed.segment_labels(members, fixtures, forecasts)
    segments = ed.segments(scores, forecasts, fixtures, members, views)
    report = {
        'version': VERSION, 'source_commit': results['source_commit'], 'harness_version': results['version'],
        'config_sha256': results['config_sha256'], 'base': BASE, 'variants': variants,
        'default_settings': {'l2': cfg['baseline_l2'], 'season_carry_over': 1.0},
        'declared': {'primary_metric': PRIMARY,
                     'differences': 'c8_minus is C8 minus the variant log loss: positive means the variant is better',
                     'cohort': 'fixtures where ' + ', '.join((*ed.COHORT, *views)) + ' all have a score',
                     'intervals': 'whole calendar weeks resampled, 95% (evaluation_harness.paired)',
                     'evidence': list(EVIDENCE), 'diagnostic_only': ['retrospective']},
        'cohort': {phase: int((members.phase == phase).sum()) for phase in PHASES},
        'cohort_equals_standing_diagnostics': bool(members.index.equals(standing.index)),
        'unavailable': {name: {k: v for k, v in sorted(results['coverage'].items())
                               if f':{name}:' in k and not k.endswith(':available')} for name in views},
        'walk_forward': walk_forward(results, views),
    }
    for phase in PHASES:
        keys = members.index[members.phase == phase]
        inside = forecasts.loc[forecasts.phase == phase]
        report[phase] = {'log_loss': compare(scores, keys, names),
                         'calibration': calibration(inside, cfg, ('C6', *views, 'M')),
                         'movement': {name: movement(inside, name) for name in names},
                         'segments': segments.get(phase),
                         'segment_differences': segment_differences(scores, labels, keys, names),
                         'goals_by_favourite': goals_by_favourite(goals, labels, forecasts, members, keys, views)}
    report['choice'] = choose(report, variants)
    return report


def _pair(result, spec='+.5f') -> str:
    if not result:
        return 'n/a'
    low, high = result['interval_95'] or (float('nan'), float('nan'))
    return (f"{result['mean_gain']:{spec}} ({low:{spec}} to {high:{spec}})"
            + (' **clear**' if result['clear_of_zero'] else ' *worse, clear*' if high < 0 else ''))


def _settings(settings, default) -> str:
    return ', '.join(f"{'penalty l2' if k == 'l2' else 'season carry-over'} {v:g} (against {default[k]:g})"
                     for k, v in settings.items())


def markdown(report) -> str:
    import evaluation_diagnostics as ed
    table, ci, f = ed._table, ed._ci, ed._f
    names = tuple(report['variants'])
    views = (BASE, *names)
    choice = report['choice']
    lines = ['# C8 with a larger penalty or a season carry-over', '',
             f"Locked run at commit `{report['source_commit']}` ({report['version']}). Offline only: no live "
             'probability changes. No holdout row is read. The retrospective period is a diagnostic, never '
             'release evidence.', '',
             'Each variant is C8 refitted walk-forward on goal rates from a fold Dixon-Coles fit with one setting '
             'changed. Differences are C8 minus variant log loss (positive: the variant is better), 95% intervals, '
             'whole calendar weeks resampled.', '']
    lines += table(['Variant', 'Setting'], [[n, _settings(s, report['default_settings'])]
                                            for n, s in report['variants'].items()])
    lines += ['Cohort (' + report['declared']['cohort'] + '): '
              + ', '.join(f'{phase} {n:,}' for phase, n in report['cohort'].items())
              + ('; the same fixtures as the standing diagnostics.' if report['cohort_equals_standing_diagnostics']
                 else '; NOT the standing diagnostics\' cohort.'), '']
    lines += ['## Choice rule (fixed before any variant score)', '', choice['rule'] + '. Otherwise C8 stands.', '']
    rows = []
    for name, v in choice['verdicts'].items():
        c = v['conditions']
        low, high = v['development_interval_95'] or (float('nan'), float('nan'))
        yes = lambda flag: 'yes' if flag else 'no'
        rows.append([name, f"{v['development_gain']:+.5f} ({low:+.5f} to {high:+.5f})",
                     yes(c['development_ah_all_positive_and_clear']), f"{v['validation_gain']:+.5f}",
                     yes(c['validation_ah_all_not_negative']),
                     f"{v['development_slopes']['home']:.2f} / {v['development_slopes']['away']:.2f}",
                     yes(c['development_calibration_v2_passes']), '**qualifies**' if v['qualifies'] else 'no'])
    lines += table(['Variant', 'Development AH all, C8 minus variant', 'Positive and clear', 'Validation AH all',
                    'Not negative', 'Development slopes home / away', 'Rule v2 passes', 'Qualifies'], rows)
    lines += ['Combination: ' + (f"{choice['combination']}" + ('' if choice['combination_in_run'] else ' (not in this run)')
                                 if choice['combination'] else 'not run (it needs a qualifying setting of each kind).'),
              '', f"**{choice['reading']}**" + (f" Final candidate: **{choice['final_candidate']}**."
                                                if choice['final_candidate'] else ''), '']
    lines += ['## Walk-forward fits', '']
    rows = []
    for name, e in report['walk_forward'].items():
        r = e['ranges']
        rows.append([name, e['windows'], e['warm_up_windows'], e['failed_windows'],
                     *(f"{f(r[k]['min'], '+.2f')} to {f(r[k]['max'], '+.2f')} ({f(r[k]['median'], '+.2f')})"
                       if r[k] else 'n/a' for k in ('b', 'c', 'a_home', 'a_away', 'rho', 'delta'))])
    lines += table(['View', 'Windows', 'Warm-up', 'Failed', 'b: range (median)', 'c', 'a_home', 'a_away', 'rho', 'delta'],
                   rows)
    for phase in PHASES:
        e = report[phase]
        label = phase.capitalize() + (' (diagnostic only)' if phase not in EVIDENCE else '')
        lines += [f"## {label}: {report['cohort'][phase]:,} fixtures", '', '### Mean log loss', '']
        shown = ('C6', *views, 'M')
        lines += table(['Metric', *shown], [[g, *(f(e['log_loss'][g]['mean_log_loss'].get(c), '.5f') for c in shown)]
                                            for g in GROUPS])
        lines += ['### C8 minus variant (positive: the variant is better)', '']
        lines += table(['Metric', *names], [[g, *(_pair(e['log_loss'][g]['c8_minus'][n]) for n in names)] for g in GROUPS])
        lines += ['### C6 minus each view (context)', '']
        lines += table(['Metric', *views], [[g, *(_pair(e['log_loss'][g]['c6_minus'][n]) for n in views)] for g in GROUPS])
        lines += ['### Calibration (every forecast of the view in the period)', '']
        rows = []
        for view, c in e['calibration'].items():
            lev, v2 = c['levels'], c['v2']
            worst = v2['worst_band']
            rows.append([view, f"{c['forecasts']:,}",
                         ' / '.join(f(lev[o]['calibration_slope'], '.3f') for o in ('home', 'draw', 'away')),
                         f"{lev['draw']['mean_forecast']:.1%} / {lev['draw']['observed_rate']:.1%}",
                         ('pass' if v2['passes'] else 'fail') + f" ({len(v2['failing_bands'])} bands fail)",
                         'n/a' if not worst else
                         f"{worst['outcome']} {worst['band_lower']:.1f}: {worst['mean_forecast']:.1%} / "
                         f"{worst['observed_rate']:.1%} (n {worst['n']}, z {worst['z']:.2f}, bar {v2['band_z_threshold']:.2f})"])
        lines += table(['View', 'Forecasts', 'Slopes home / draw / away', 'Draw forecast / observed', 'Rule v2',
                        'Worst band'], rows)
        lines += ['### How far each variant moves 1X2 from C8 (largest move per fixture, points)', '']
        lines += table(['Variant', 'Fixtures', 'Mean', '90th percentile', 'Max'],
                       [[n, f"{m['fixtures']:,}", f"{m['mean_max_1x2_move_points']:.1f}",
                         f"{m['p90_max_1x2_move_points']:.1f}", f"{m['max_1x2_move_points']:.1f}"]
                        for n, m in e['movement'].items()])
        lines += ['### Thin-team and August-September segments: C8 minus variant', '']
        rows = [[label, f"{s['fixtures']:,}", group, *(_pair(s['c8_minus'][n][group]) for n in names)]
                for label, s in e['segment_differences'].items() for group in (PRIMARY, '1X2')]
        lines += table(['Segment', 'Fixtures', 'Metric', *names], rows)
        seg = e['segments']
        if seg:
            lines += ['### Gap to M on AH all lines by segment (view minus M: positive is behind the market)', '']
            rows = [['all', 'all', f"{seg['all']['fixtures']:,}", *(ci(seg['all']['gap_to_M'][c][PRIMARY]) for c in views)]]
            for dimension in ('training matches', 'month', 'favourite market probability', 'league'):
                for r in seg[dimension]:
                    rows.append([dimension, r['segment'], f"{r['fixtures']:,}",
                                 *(ci(r['gap_to_M'][c][PRIMARY]) if r['gap_to_M'] else 'n/a' for c in views)])
            lines += table(['Dimension', 'Segment', 'Fixtures', *views], rows)
        lines += ['### Predicted against actual goals by favourite strength', '',
                  'The favourite is the side M makes more likely to win; bands are its market probability. '
                  'Predicted goals are the scored grid\'s expected goals. Supremacy is favourite minus underdog '
                  'goals; predicted minus actual above zero means the view expects too much.', '']
        rows = []
        for band in e['goals_by_favourite']:
            for view, g in band['views'].items():
                if g is None:
                    continue
                rows.append([band['band'], f"{band['fixtures']:,}", view,
                             f"{g['predicted']['favourite']:.3f} / {g['actual']['favourite']:.3f}",
                             f"{g['predicted']['underdog']:.3f} / {g['actual']['underdog']:.3f}",
                             ci(g['predicted_minus_actual']['supremacy'], '+.3f'),
                             ci(g['predicted_minus_actual']['total'], '+.3f')])
        lines += table(['Favourite market probability', 'Fixtures', 'View', 'Favourite goals: predicted / actual',
                        'Underdog goals: predicted / actual', 'Supremacy: predicted minus actual',
                        'Total goals: predicted minus actual'], rows)
    return '\n'.join(lines)


def main(argv=None) -> int:
    import evaluation_diagnostics as ed
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('--run', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args(argv)
    cfg = json.loads((REPO / 'evaluation_harness_config.json').read_text(encoding='utf-8'))
    report = build(args.run, cfg)
    args.output.mkdir(parents=True, exist_ok=True)
    ed.write_json(args.output / 'summary.json', report)
    (args.output / 'report.md').write_text(markdown(report), encoding='utf-8', newline='\n')
    for name, v in report['choice']['verdicts'].items():
        print(name, v['conditions'], 'qualifies' if v['qualifies'] else 'does not qualify')
    print(report['choice']['reading'], 'Final candidate:', report['choice']['final_candidate'])
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
