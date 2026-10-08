"""Past-only walk-forward tuning for Dixon-Coles exponential time decay.

The objective follows David Sheehan's Dixon-Coles blog: maximize the
probability assigned to genuinely subsequent match results. The code uses
mean 1X2 negative log likelihood (log loss), with Brier as a diagnostic.
This is hyperparameter selection, not a final untouched test evaluation.
"""

from __future__ import annotations

import math
from typing import Dict, List, Optional, Sequence, Tuple, Type

import numpy as np
import pandas as pd


def make_walkforward_folds(
    history: pd.DataFrame,
    validation_days: int = 365,
    step_days: int = 56,
    min_train: int = 250,
) -> List[Tuple[pd.DataFrame, pd.DataFrame, pd.Timestamp]]:
    """Build temporally disjoint training/test blocks; no same-day data leaks."""
    if validation_days <= 0 or step_days <= 0 or min_train < 30:
        raise ValueError(
            "validation_days and step_days must be positive; min_train >= 30"
        )

    required = {"Date", "HomeTeam", "AwayTeam", "FTHG", "FTAG"}
    missing = required.difference(history.columns)
    if missing:
        raise ValueError(f"Missing history columns: {sorted(missing)}")

    hist = history.dropna(subset=list(required)).copy()
    hist["Date"] = pd.to_datetime(hist["Date"], errors="coerce")
    hist = hist.dropna(subset=["Date"]).sort_values("Date").reset_index(drop=True)
    if hist.empty:
        return []

    final_end = hist["Date"].max().normalize() + pd.Timedelta(days=1)
    first_start = max(
        hist["Date"].min().normalize() + pd.Timedelta(days=1),
        final_end - pd.Timedelta(days=validation_days),
    )
    boundaries = list(pd.date_range(first_start, final_end, freq=f"{step_days}D"))
    if not boundaries or boundaries[0] != first_start:
        boundaries.insert(0, first_start)
    if boundaries[-1] < final_end:
        boundaries.append(final_end)

    folds = []
    for start, stop in zip(boundaries[:-1], boundaries[1:]):
        train = hist[hist["Date"] < start]
        test = hist[(hist["Date"] >= start) & (hist["Date"] < stop)]
        if len(train) >= min_train and not test.empty:
            folds.append((train, test, start))
    return folds


def tune_half_life(
    history: pd.DataFrame,
    model_class: Type,
    candidates: Sequence[float] = (120.0, 240.0, 365.0, 730.0, 1e9),
    l2: float = 0.08,
    max_goals: int = 10,
    validation_days: int = 365,
    step_days: int = 56,
    min_train: int = 250,
    min_validation_matches: int = 25,
) -> Dict[str, object]:
    """Select half-life by historical walk-forward 1X2 log loss (lower is better)."""
    options = sorted(set(float(x) for x in candidates))
    if not options or any(not math.isfinite(x) or x <= 0 for x in options):
        raise ValueError("All candidate half-lives must be positive finite numbers")
    if min_validation_matches < 1:
        raise ValueError("min_validation_matches must be >= 1")

    folds = make_walkforward_folds(
        history,
        validation_days=validation_days,
        step_days=step_days,
        min_train=min_train,
    )
    if not folds:
        raise RuntimeError(
            "Insufficient history for decay tuning; increase --seasons-back "
            "or reduce --tune-min-train."
        )

    scores = []
    for half_life in options:
        logloss_total = 0.0
        brier_total = 0.0
        count = 0
        successful_folds = 0
        try:
            for train, test, origin in folds:
                model = model_class(
                    half_life_days=half_life,
                    l2=l2,
                    max_goals=max_goals,
                ).fit(train, as_of=origin)
                successful_folds += 1

                for row in test.itertuples(index=False):
                    matrix, _ = model.score_matrix(
                        str(row.HomeTeam), str(row.AwayTeam)
                    )
                    x12 = model.one_x_two(matrix)
                    probs = np.array(
                        [x12["home"], x12["draw"], x12["away"]],
                        dtype=float,
                    )
                    hg, ag = int(row.FTHG), int(row.FTAG)
                    actual = 0 if hg > ag else (1 if hg == ag else 2)
                    logloss_total -= math.log(
                        max(float(probs[actual]), 1e-12)
                    )
                    one_hot = np.eye(3)[actual]
                    brier_total += float(np.sum((probs - one_hot) ** 2))
                    count += 1
        except (ValueError, RuntimeError, FloatingPointError) as exc:
            scores.append({
                "half_life_days": half_life,
                "xi_per_day": math.log(2.0) / half_life,
                "valid": False,
                "error": str(exc),
                "n_matches": count,
                "n_folds": successful_folds,
            })
            continue

        valid = count >= min_validation_matches and successful_folds == len(folds)
        scores.append({
            "half_life_days": half_life,
            "xi_per_day": math.log(2.0) / half_life,
            "valid": valid,
            "n_matches": count,
            "n_folds": successful_folds,
            "log_loss": logloss_total / count if count else None,
            "brier_score": brier_total / count if count else None,
        })

    eligible = [x for x in scores if x["valid"]]
    if not eligible:
        raise RuntimeError(
            "Too few held-out matches for half-life selection; increase "
            "--tune-validation-days or reduce --tune-min-validation-matches."
        )

    best = min(
        eligible,
        key=lambda item: (
            float(item["log_loss"]),
            float(item["brier_score"]),
            float(item["half_life_days"]),
        ),
    )
    return {
        "selected_half_life_days": float(best["half_life_days"]),
        "selected_xi_per_day": float(best["xi_per_day"]),
        "selection_metric": "walk_forward_1x2_log_loss",
        "validation_days": validation_days,
        "step_days": step_days,
        "n_folds": len(folds),
        "min_train": min_train,
        "min_validation_matches": min_validation_matches,
        "candidates": scores,
        "note": (
            "Validation scores were used for model selection and are not an "
            "independent final test. Evaluate on a later untouched period."
        ),
    }
