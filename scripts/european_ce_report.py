"""CE (the research model as live runs it for UCL and UEL) on the European development and validation periods.

Reads a locked European harness run (`python evaluation_harness.py --mode european --output DIR`).
Only development and validation scores are read; a European holdout row anywhere aborts the report.
Retrospective rows (already scored elsewhere) are counted, never summarised. Results only: there
are no historical European prices, so there is no market reference and no market bar.

Reported: 1X2 log loss, AH all lines and draw-sensitive lines (0, +/-0.5) settled on the result,
Over 1.5; overall, by competition and by stage (group stage or league phase, knockouts); logistic
calibration slopes and calibration rule v2 (reported, not a gate); the cached inventory and the backfill;
how many European fixtures have domestic form for both teams in the 8 cached leagues (Phase 2c reach); and
how many European holdout fixtures a declared run would score, counted by identity only (no score read).

    python scripts/european_ce_report.py --run DIR --output evaluation/european_ce
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

import pandas as pd

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO))
PHASES = ('development', 'validation')


def calibration(frame):
    """Per outcome: forecasts, mean forecast, observed rate and logistic calibration slope."""
    import evaluation_harness as eh
    out = {}
    for k, outcome in enumerate(('home', 'draw', 'away')):
        p, y = frame['p_' + outcome], (frame.outcome == k).astype(int)
        out[outcome] = {'forecasts': int(len(frame)), 'mean_forecast': float(p.mean()), 'observed_rate': float(y.mean()),
                        'calibration_slope': eh.calibration_slope(p, y)}
    return out


def report(run: Path) -> dict:
    results = json.loads((run / 'results.json').read_text(encoding='utf-8'))
    if results.get('mode') != 'european':
        raise ValueError('Not a locked European run')
    scores = pd.read_csv(run / 'fixture_scores.csv')
    forecasts = pd.read_csv(run / 'forecasts_1x2.csv')
    if 'holdout' in set(scores.phase) | set(forecasts.phase) or 'holdout' in results['periods']:
        raise ValueError('A European holdout row is present: this report reads locked runs only')
    periods = {}
    for name in PHASES:
        period = results['periods'].get(name)
        if period is None:
            continue
        part = forecasts.loc[forecasts.phase == name]
        periods[name] = {
            'log_loss': {k: period[k] for k in ('overall', 'by_competition', 'by_stage', 'by_competition_and_stage')},
            'calibration': {'overall': calibration(part),
                            **{c: calibration(p) for c, p in part.groupby('league')},
                            'by_competition_and_stage': {f'{c} {g}': calibration(p)
                                                         for (c, g), p in part.groupby(['league', 'stage_group'])}},
            'calibration_rule_v2_reported_not_a_gate': period['calibration_tolerance_check'],
        }
    counts = scores.loc[scores.group == '1X2'].groupby(['phase', 'league']).fixture_key.nunique()
    return {
        'source': {'run_commit': results['source_commit'], 'config_sha256': results['config_sha256'],
                   'european_version': results['european_version']},
        'candidate': results['candidates'],
        'periods_config': results['config'],
        'coverage': results['coverage'],
        'scored_fixtures': {f'{p} {c}': int(n) for (p, c), n in counts.items()},
        'periods': periods,
        'reference_1x2_uniform_log_loss': 1.0986122886681098,  # ln 3: forecasting 1/3 each, needs no data
        'inventory': results['inventory'],
        'domestic_form': results['domestic_form'],
        'holdout_reach_identity_only': results.get('holdout_reach'),
        'european_holdout_sample_minimum': results.get('sample_minimum'),
        'notes': results['notes'] + ['Retrospective periods are counted in scored_fixtures and coverage but not summarised.'],
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('--run', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args(argv)
    summary = report(args.run)
    args.output.mkdir(parents=True, exist_ok=True)
    (args.output / 'summary.json').write_text(json.dumps(summary, indent=2, ensure_ascii=False, allow_nan=False) + '\n',
                                              encoding='utf-8')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
