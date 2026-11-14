"""Build research_c6_fits.json: C6's walk-forward fits for every fold window, for live research v5.

Runs the harness's own research model C over the eight domestic leagues exactly as a locked
development run does (evaluation_harness.evaluate_league, holdout-free training rows, no
holdout match forecast or read) and fits C6 at every fold origin with the function the C6
candidate uses (evaluation_harness.c6_walk_forward). A fit reads only matches played before
its origin, so each window's (rho, delta, slope) is the one the harness uses for the matches
inside it, and it doesn't change when the file is rebuilt later with more data.

Reads results and C's goal rates only: no odds, market fits or published grid reach the fits.

    python scripts/build_research_c6_fits.py                    # windows up to the harness end_exclusive
    python scripts/build_research_c6_fits.py --end 2026-11-23   # later windows, once the cache has the results
"""
from __future__ import annotations

import argparse
from concurrent.futures import ProcessPoolExecutor
import hashlib
import json
from pathlib import Path
import subprocess
import sys

import pandas as pd

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO))


def research_rows(cache, cfg, workers=None):
    import evaluation_harness as eh
    rows = []
    with ProcessPoolExecutor(max_workers=workers) as pool:
        futures = [pool.submit(eh.evaluate_league, league, str(cache), cfg, False, {'C6'}) for league in cfg['leagues']]
        for future in futures:
            rows += future.result()[6]
    if any(r['identity']['phase'] == 'holdout' for r in rows):
        raise ValueError('A holdout match reached the C6 fits')
    return rows


def build(cache, cfg, workers=None):
    import evaluation_harness as eh
    import research_low_score_sharpen as c6
    end = pd.Timestamp(cfg['end_exclusive'])
    research = research_rows(cache, cfg, workers)
    research, _, windows = eh.c6_walk_forward(research, cfg, end, every_window=True)
    last = max(r['date'] for r in research)
    out = []
    for w in windows:
        if w['origin'] > last + pd.Timedelta(days=1):
            break  # a fit needs every result before its origin; the cache stops at `last`
        out.append({'origin': w['origin'].date().isoformat(), 'end_exclusive': w['stop'].date().isoformat(),
                    'rho': w['low_score']['rho'], 'delta': w['low_score']['delta'],
                    'low_score_status': w['low_score']['status'], 'low_score_matches': w['low_score']['matches'],
                    'slope': w['slope']['slope'], 'slope_status': w['slope']['status'],
                    'slope_matches': w['slope']['matches']})
    try:
        commit = subprocess.run(['git', 'rev-parse', 'HEAD'], cwd=REPO, capture_output=True, text=True,
                                check=True).stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        commit = None
    fixed = sorted({cfg[k] for k in ('development_end', 'holdout_start', 'holdout_end_exclusive')})
    return {
        'version': c6.FITS_VERSION, 'candidate_version': c6.VERSION,
        'description': ("C6's walk-forward fits per fold window (evaluation_harness.c6_walk_forward): (rho, delta) "
                        "on C's earlier forecasts, slope on C2's earlier forecasts of decided matches, pooled over "
                        "the eight leagues, recency half-life below. Holdout-free like a locked run: the holdout "
                        "leagues' 16 Jan - 10 Oct 2026 results are never forecast or read. Live research v5 uses the "
                        "window with the latest origin on or before the forecast's observation day."),
        'half_life_days': cfg['production_v2']['half_life_days'],
        'fold_rule': {'test_start': cfg['test_start'], 'step_days': cfg['step_days'], 'fixed_bounds': fixed},
        'built_with': {'commit': commit, 'harness_end_exclusive': cfg['end_exclusive'],
                       'harness_config_sha256': hashlib.sha256(json.dumps(cfg, sort_keys=True).encode()).hexdigest(),
                       'research_rows': len(research), 'last_result_date': last.date().isoformat(),
                       'leagues': list(cfg['leagues'])},
        'windows': out}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('--cache', type=Path, default=REPO / '.football_cache')
    parser.add_argument('--end', help='end_exclusive for the fold windows (default: the harness config)')
    parser.add_argument('--output', type=Path, default=REPO / 'research_c6_fits.json')
    parser.add_argument('--workers', type=int)
    args = parser.parse_args(argv)
    import evaluation_harness as eh
    cfg = json.loads(eh.CONFIG.read_text(encoding='utf-8'))
    if args.end:
        cfg['end_exclusive'] = args.end
    data = build(args.cache, cfg, args.workers)
    args.output.write_text(json.dumps(data, indent=1) + '\n', encoding='utf-8')
    last = data['windows'][-1]
    print(f"{len(data['windows'])} windows; last origin {last['origin']}: rho {last['rho']:.4f}, "
          f"delta {last['delta']:.4f}, slope {last['slope']:.4f}; results to {data['built_with']['last_result_date']}")
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
