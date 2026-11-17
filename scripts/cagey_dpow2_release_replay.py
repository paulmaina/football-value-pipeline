"""The D_pow2 release over the saved live runs (docs/plan.md, Phase 3b-3). Integration check: no result is read.

Every saved run in the window is rebuilt from its frozen predictions twice:

    before   today's live rule until this release: D everywhere (no cagey_correction_live)
    release  cagey_correction_config.json as released: D_pow2 for domestic leagues, D for UCL and UEL

and compared (scripts/cagey_devig_report.compare_run): the cagey no-loss probabilities, the master's 0.75 safe set,
the cagey tier list, the master list and the value shortlist. It also checks, run by run:

  * the release build is the pipeline's own default call (build_shortlist with the config as committed);
  * UCL and UEL rows are untouched (every cagey figure identical to the before build);
  * the shadow column is D exactly: on every row D_pow2 prices, shadow_corrected_no_loss_probability equals the
    before build's corrected_no_loss_probability;

and measures the harness-live parity gap: for each domestic fixture whose live fit B is usable, the live D_pow2
margin distribution (price_edge_cagey_shortlist.corrected_context on the frozen Pinnacle quotes at the run clock)
against the harness's grid on the same three quotes (evaluation_harness.market_matrix and cagey_matrix with the
power method and the same model), and the same for D.

    python scripts/cagey_dpow2_release_replay.py --output evaluation/cagey_dpow2_release
"""
from __future__ import annotations

import argparse
import json
import sys
import warnings
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import evaluation_harness as eh  # noqa: E402
import market_implied as mi  # noqa: E402
import narrow_margin as nm  # noqa: E402
import price_edge_cagey_shortlist as v28  # noqa: E402
import price_edge_shortlist as v27  # noqa: E402
from scripts import cagey_devig_report as base  # noqa: E402

CAGEY_PREFIXES = ('cagey_', 'corrected_', 'shadow_', 'price_flag', 'in_value_tier')


def default_call(predictions, generated):
    """The pipeline's own call: build_shortlist with the committed config (the release)."""
    from quote_policy import load_policy
    with warnings.catch_warnings():
        warnings.simplefilter('ignore')
        return v28.build_shortlist(predictions, pd.Timestamp(generated), execution_policy=load_policy())[1]


def european_untouched(before, release) -> dict:
    a, b = before[0], release[0]
    mask = base._column(a, 'league').isin(v28.EUROPEAN_LEAGUES)
    columns = [c for c in a.columns if c.startswith(CAGEY_PREFIXES)]
    changed = sorted(c for c in columns if c in b and a.loc[mask, c].astype(object).map(str).tolist()
                     != b.loc[mask, c].astype(object).map(str).tolist())
    labels = sorted(set(base._column(b, 'cagey_correction')[mask].dropna().map(str)))
    return {'rows': int(mask.sum()), 'cagey_columns_changed': changed, 'corrections': labels,
            'untouched': not changed and set(labels) <= {v28.CORRECTION_D}}


def shadow_is_d(before, release) -> dict:
    a, b = before[0], release[0]
    priced = base._column(b, 'cagey_correction').eq(v28.CORRECTION_D_POW2)
    shadow = pd.to_numeric(base._column(b, 'shadow_corrected_no_loss_probability'), errors='coerce')
    d = pd.to_numeric(base._column(a, 'corrected_no_loss_probability'), errors='coerce')
    both = priced & shadow.notna() & d.notna()
    gap = float((shadow - d)[both].abs().max()) if both.any() else 0.0
    return {'rows_priced_by_d_pow2': int(priced.sum()), 'rows_with_shadow': int(both.sum()),
            'rows_without_shadow': int((priced & shadow.isna()).sum()), 'max_abs_gap': gap,
            'shadow_is_d': bool(gap <= 1e-12)}


def parity(predictions, generated, settings) -> dict:
    """Harness-live parity gap on every domestic fixture with a usable live fit B (module docstring)."""
    strict = v28.timing_rule(settings) == v28.TIMING_RULE_CUTOFF
    corrections = v28.correction_models(settings, nm.load(settings['model_version']))
    clock = pd.Timestamp(generated)
    gaps = {name: [] for name in corrections}
    skipped = {'european': 0, 'no_usable_fit_b': 0, 'no_context': 0}
    seen = set()
    for row in predictions.astype(object).where(predictions.notna(), None).to_dict('records'):
        key = (row.get('league'), row.get('home_team'), row.get('away_team'), row.get('kickoff_utc'))
        if key in seen:
            continue
        seen.add(key)
        if v28.correction_scope(row.get('league')) != 'domestic':
            skipped['european'] += 1
            continue
        pin = v27.pinnacle_quotes(row)
        line = pin['main_line']
        if pin['h2h'] is None or pin['ou25'] is None or line is None:
            skipped['no_usable_fit_b'] += 1
            continue
        prices = {'hda': pin['h2h'][:3], 'ou': pin['ou25'][:2], 'ah': (line, *pin['ah'][line][:2])}
        for name, (model, method) in corrections.items():
            fit, info = v27.market_fit(pin, clock, strict, method=method)
            if not fit.usable:
                skipped['no_usable_fit_b'] += name == v28.CORRECTION_D
                continue
            context = v28.corrected_context(pin, fit, info, model, method)
            if context is None:
                skipped['no_context'] += 1
                continue
            try:
                harness = eh.cagey_matrix(eh.market_matrix(prices, method), prices, model, method)
            except (ValueError, TypeError, KeyError):
                skipped['no_context'] += 1
                continue
            margins, probs = mi.margin_distribution(harness)
            live = dict(zip(np.asarray(context['margins']).tolist(), np.asarray(context['probs']).tolist()))
            gaps[name].append(max(abs(live.get(int(m), 0.0) - float(p)) for m, p in zip(margins, probs)))
    return {'max_abs_margin_probability_gap': {n: (max(g) if g else None) for n, g in gaps.items()},
            'fixtures_compared': {n: len(g) for n, g in gaps.items()}, 'skipped': skipped}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--start', default='2026-10-27', help='first run day')
    parser.add_argument('--end', default='2026-11-18', help='last run day, exclusive')
    args = parser.parse_args(argv)
    import shortlist_window
    from scripts.master_reconciliation_replay import runs
    release_settings = {**v28.load_settings(), 'shortlist_lookahead_hours': shortlist_window.DEFAULT_HOURS}
    if (release_settings.get('cagey_correction_live') or {}).get('domestic') != v28.CORRECTION_D_POW2:
        raise SystemExit('cagey_correction_config.json does not put D_pow2 live for domestic leagues')
    before_settings = {k: v for k, v in release_settings.items() if k not in ('cagey_correction_live', 'cagey_corrections')}
    model = nm.load(release_settings['model_version'])
    report = {'script': 'scripts/cagey_dpow2_release_replay.py', 'start': args.start, 'end_exclusive': args.end,
              'safe_no_loss': base.SAFE_NO_LOSS, 'note': 'Integration check: no result is read.',
              'release': {k: release_settings[k] for k in ('cagey_correction_live', 'cagey_corrections')}, 'runs': []}
    out_root = args.output / 'live_runs'
    for generated, directory, _ in runs(ROOT, args.start, args.end):
        predictions = pd.read_csv(directory / 'predictions.csv', low_memory=False)
        before = base.build_variant(predictions, generated, before_settings, model, out_root / 'before' / directory.name)
        release = base.build_variant(predictions, generated, release_settings, model, out_root / 'release' / directory.name)
        entry = {'snapshot': directory.name, 'generated_at_utc': generated, 'offers': int(len(release[0])),
                 'release_is_the_default_call': bool(default_call(predictions, generated).to_csv(index=False)
                                                     == release[0].to_csv(index=False)),
                 'european': european_untouched(before, release), 'shadow': shadow_is_d(before, release),
                 'compare': base.compare_run(before, release, directory.name),
                 'parity': parity(predictions, generated, release_settings)}
        report['runs'].append(entry)
        print(directory.name, entry['offers'], entry['release_is_the_default_call'], entry['european']['untouched'],
              entry['shadow']['shadow_is_d'], flush=True)
    rows = report['runs']
    gap = lambda name: max((r['parity']['max_abs_margin_probability_gap'][name] or 0.0) for r in rows)  # noqa: E731
    report['totals'] = {
        **base.run_totals([r['compare'] for r in rows]),
        'runs_with_offers': sum(r['offers'] > 0 for r in rows),
        'release_is_the_default_call_in_every_run': all(r['release_is_the_default_call'] for r in rows),
        'european_rows': sum(r['european']['rows'] for r in rows),
        'european_untouched_in_every_run': all(r['european']['untouched'] for r in rows),
        'rows_priced_by_d_pow2': sum(r['shadow']['rows_priced_by_d_pow2'] for r in rows),
        'shadow_is_d_in_every_run': all(r['shadow']['shadow_is_d'] for r in rows),
        'parity': {'max_abs_margin_probability_gap': {n: gap(n) for n in (v28.CORRECTION_D, v28.CORRECTION_D_POW2)},
                   'fixtures_compared': {n: sum(r['parity']['fixtures_compared'][n] for r in rows)
                                         for n in (v28.CORRECTION_D, v28.CORRECTION_D_POW2)}}}
    args.output.mkdir(parents=True, exist_ok=True)
    (args.output / 'live_replay.json').write_text(json.dumps(report, indent=2, sort_keys=True, default=float) + '\n',
                                                  encoding='utf-8')
    print(json.dumps(report['totals'], indent=2, default=float))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
