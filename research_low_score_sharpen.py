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

Not used by the live pipeline. It is a harness candidate until it passes the release
gate in docs/plan.md.
"""
from __future__ import annotations

import research_low_score as rls
import research_sharpen as rs

VERSION = 'research-low-score-then-sharpen-walk-forward-v1'


def c2_one_x_two(goal_rates, low_score_params):
    """C2's 1X2 for one match: the input to C6's slope fit."""
    return rs.one_x_two(rls.adjusted_grid(goal_rates, low_score_params))


def fit_slope(c2_probs, outcomes, age_days, half_life_days):
    """C6's slope: C5's fit (research_sharpen.fit) on C2's earlier forecasts instead of C's."""
    return rs.fit(c2_probs, outcomes, age_days, half_life_days)


def grid(goal_rates, low_score_params, sharpen_params):
    """C6's score grid: C2's grid moved onto its sharpened 1X2. A neutral slope gives C2's grid exactly."""
    return rs.sharpen_matrix(rls.adjusted_grid(goal_rates, low_score_params), sharpen_params['slope'])
