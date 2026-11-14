"""Candidate C6: C2's draw and low-score correction, then C5's home/away sharpening (offline only).

C2 (research_low_score) fixes the research model's draw level but not the flatness of
its home/away split; C5 (research_sharpen) fixes the flatness but holds C's too-low draw
(docs/plan.md, Phase 2a and 2e). C6 applies both, in that order, to one score grid:

    C2 grid  = research_low_score.adjusted_grid(C's goal rates, (rho, delta))
    C6 grid  = research_sharpen.sharpen_matrix(C2 grid, slope)

so C6 holds C2's draw probability exactly and sharpens how C2 splits the rest between
home and away. Every market, Asian handicaps included, still comes from one grid.

Fits, both walk-forward and pooled across leagues, with the same recency half-life:
  (rho, delta)  research_low_score.fit on C's earlier forecasts, exactly as C2 (so C6's
                pre-sharpening grid is C2's grid for that match);
  slope         research_sharpen.fit on C2's own earlier forecasts (each match as C2
                forecast it, under the (rho, delta) of the window it was played in) and
                the final scores, not on C's.
Until research_sharpen.MIN_MATCHES decided matches exist the slope is neutral (1.0)
and C6 equals C2 exactly. Reads only C's goal rates and final scores: never odds,
market fits or the published grid.

Live since research v5 (team-form-research-v5, domestic leagues only), released by Paul's
decision of 14 Nov 2026 without holdout proof (docs/plan.md, Decisions). Live reads its fits
from FITS, a file written by scripts/build_research_c6_fits.py from the harness's own
walk-forward fit (evaluation_harness.c6_walk_forward), one entry per 14-day fold window. A
forecast uses the window with the latest origin on or before its research observation day,
so every result in that fit was played before the forecast was made, and the chosen fit is
frozen in the forecast (team_research_json['c6_fit']) so it replays exactly.
"""
from __future__ import annotations

from functools import lru_cache
import json
from pathlib import Path

import pandas as pd

import research_low_score as rls
import research_sharpen as rs

VERSION = 'research-low-score-then-sharpen-walk-forward-v1'
FITS = Path(__file__).with_name('research_c6_fits.json')
FITS_VERSION = 'research-c6-fits-v1'
FIT_FIELDS = ('rho', 'delta', 'slope')


def c2_one_x_two(goal_rates, low_score_params):
    """C2's 1X2 for one match: the input to C6's slope fit."""
    return rs.one_x_two(rls.adjusted_grid(goal_rates, low_score_params))


def fit_slope(c2_probs, outcomes, age_days, half_life_days):
    """C6's slope: C5's fit (research_sharpen.fit) on C2's earlier forecasts instead of C's."""
    return rs.fit(c2_probs, outcomes, age_days, half_life_days)


def grid(goal_rates, low_score_params, sharpen_params):
    """C6's score grid: C2's grid moved onto its sharpened 1X2. A neutral slope gives C2's grid exactly."""
    return rs.sharpen_matrix(rls.adjusted_grid(goal_rates, low_score_params), sharpen_params['slope'])


# ---------------------------------------------------------------------------
# Live (research v5): the harness's walk-forward fits, frozen per fold window
# ---------------------------------------------------------------------------

@lru_cache(maxsize=4)
def _load(path: str, mtime: float) -> dict:
    data = json.loads(Path(path).read_text(encoding='utf-8'))
    if data.get('version') != FITS_VERSION or data.get('candidate_version') != VERSION:
        raise ValueError(f'unsupported C6 fit file {path}')
    return data


def load_fits(path=FITS) -> dict:
    path = Path(path)
    return _load(str(path), path.stat().st_mtime)


def expected_origin(day, rule) -> pd.Timestamp:
    """The fold origin the harness gives `day` (evaluation_harness.fold_windows): the latest 14-day step from
    the test start, or fixed period boundary, on or before it."""
    start, step = pd.Timestamp(rule['test_start']), int(rule['step_days'])
    steps = (day - start).days // step
    bounds = [start + pd.Timedelta(days=step * steps), *[pd.Timestamp(b) for b in rule['fixed_bounds']]]
    return max(b for b in bounds if start <= b <= day)


def fit_for(cutoff, path=FITS) -> dict | None:
    """The C6 fit a forecast observed at `cutoff` uses: the fit file's window with the latest origin on or before
    the cutoff's UTC day. None when the file has no such window. `stale` is True when the harness would already
    have a later window for that day (the file was built before it) and the older fit is used instead."""
    data = load_fits(path)
    day = pd.Timestamp(cutoff).tz_convert('UTC').tz_localize(None).normalize()
    windows = [w for w in data['windows'] if pd.Timestamp(w['origin']) <= day]
    if not windows:
        return None
    window = windows[-1]
    expected = expected_origin(day, data['fold_rule'])
    return {'fits_version': data['version'], 'candidate_version': data['candidate_version'],
            'origin': window['origin'], 'end_exclusive': window['end_exclusive'],
            **{k: float(window[k]) for k in FIT_FIELDS},
            'low_score_status': window['low_score_status'], 'slope_status': window['slope_status'],
            'expected_origin': expected.date().isoformat(), 'stale': bool(expected > pd.Timestamp(window['origin']))}


def live_grid(goal_rates, fit):
    """C6's score grid for these goal rates under a frozen fit, validated exactly as the harness scores it
    (research_backtest.matrix_value of grid())."""
    from research_backtest import matrix_value
    return matrix_value(grid(goal_rates, {'rho': float(fit['rho']), 'delta': float(fit['delta'])},
                             {'slope': float(fit['slope'])}))
