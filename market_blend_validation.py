"""Select the 1X2 bookmaker blend using historical pre-match predictions.

Use only opening market prices and Dixon-Coles walk-forward predictions.
The chosen weight is selected on the earlier chronological development
sample. A later chronological audit sample is reported separately and is
NEVER used to choose or change the weight.
"""

from __future__ import annotations

from typing import Dict, Optional, Sequence

import numpy as np
import pandas as pd


def _log_loss(probabilities: np.ndarray, outcomes: np.ndarray) -> float:
    return float(-np.mean(np.log(np.clip(
        probabilities[np.arange(len(outcomes)), outcomes], 1e-12, 1.0
    ))))


def _brier(probabilities: np.ndarray, outcomes: np.ndarray) -> float:
    return float(np.mean(np.sum(
        (probabilities - np.eye(3)[outcomes]) ** 2, axis=1
    )))


def select_market_weight(
    predictions: pd.DataFrame,
    candidates: Sequence[float] = (0.0, 0.15, 0.30, 0.50, 0.70, 1.0),
    min_matches: int = 80,
    audit_fraction: float = 0.25,
    minimum_development_gain: float = 0.002,
) -> Dict[str, object]:
    """
    Tune 1X2 probability blend from strictly past-only match predictions.

    Input frame must contain 1X2 raw Dixon-Coles probabilities, 1X2
    de-vigged *opening* bookmaker probabilities, actual outcomes and date.
    The historical model predictions themselves must have been produced
    with rolling-origin fitting; this helper does not train the DC model.

    Evaluation on later audit rows is diagnostic, not a tuning signal.
    """
    weights = sorted(set(float(w) for w in candidates))
    if not weights or any(not np.isfinite(w) or w < 0 or w > 1 for w in weights):
        raise ValueError("Candidate weights must be in the interval [0, 1]")
    if 0.0 not in weights:
        raise ValueError("Include weight 0 as an unblended model baseline")
    if min_matches < 20:
        raise ValueError("min_matches must be at least 20")
    if not (0.1 <= audit_fraction <= 0.5):
        raise ValueError("audit_fraction must be in [0.1, 0.5]")
    if minimum_development_gain < 0:
        raise ValueError("minimum_development_gain must be non-negative")

    required = [
        "date", "actual_class",
        "raw_p_home", "raw_p_draw", "raw_p_away",
        "open_p_home", "open_p_draw", "open_p_away",
    ]
    missing = set(required).difference(predictions.columns)
    if missing:
        return {
            "selected_market_weight": None,
            "status": "insufficient_history",
            "reason": f"Missing historical columns: {sorted(missing)}",
            "n_usable_matches": 0,
        }

    rows = predictions[required].copy()
    rows["date"] = pd.to_datetime(rows["date"], errors="coerce")
    for col in required[1:]:
        rows[col] = pd.to_numeric(rows[col], errors="coerce")
    rows = rows.dropna().sort_values("date").reset_index(drop=True)

    if not rows.empty:
        raw = rows[["raw_p_home", "raw_p_draw", "raw_p_away"]].to_numpy(float)
        opening = rows[["open_p_home", "open_p_draw", "open_p_away"]].to_numpy(float)
        y = rows["actual_class"].to_numpy(float)
        good = (
            np.all(np.isfinite(raw) & (raw > 0) & (raw < 1), axis=1)
            & np.all(np.isfinite(opening) & (opening > 0) & (opening < 1), axis=1)
            & np.isclose(raw.sum(axis=1), 1, atol=1e-5)
            & np.isclose(opening.sum(axis=1), 1, atol=1e-5)
            & np.isin(y, [0, 1, 2])
        )
        rows = rows.loc[good].reset_index(drop=True)

    if len(rows) < min_matches:
        return {
            "selected_market_weight": None,
            "status": "insufficient_history",
            "reason": "Too few matches with complete historical opening 1X2 odds",
            "n_usable_matches": len(rows),
            "minimum_required": min_matches,
        }

    # Don't split a matchday between development and audit.
    approx = int(len(rows) * (1 - audit_fraction))
    cutoff = rows.loc[approx, "date"]
    development = rows[rows["date"] < cutoff]
    audit = rows[rows["date"] >= cutoff]
    if len(development) < min_matches // 2 or len(audit) < max(10, min_matches // 10):
        return {
            "selected_market_weight": None,
            "status": "insufficient_history",
            "reason": "Not enough chronologically separated development/audit matches",
            "n_usable_matches": len(rows),
        }

    def parts(frame: pd.DataFrame):
        raw = frame[["raw_p_home", "raw_p_draw", "raw_p_away"]].to_numpy(float)
        market = frame[["open_p_home", "open_p_draw", "open_p_away"]].to_numpy(float)
        outcome = frame["actual_class"].to_numpy(int)
        return raw, market, outcome

    dr, dm, dy = parts(development)
    ar, am, ay = parts(audit)

    comparisons = []
    for w in weights:
        dp = (1 - w) * dr + w * dm
        ap = (1 - w) * ar + w * am
        comparisons.append({
            "market_weight": w,
            "development_log_loss": _log_loss(dp, dy),
            "development_brier": _brier(dp, dy),
            "audit_log_loss": _log_loss(ap, ay),
            "audit_brier": _brier(ap, ay),
        })

    best = min(comparisons, key=lambda c: (c["development_log_loss"], c["market_weight"]))
    raw = next(c for c in comparisons if c["market_weight"] == 0)
    gain = float(raw["development_log_loss"] - best["development_log_loss"])

    if gain < minimum_development_gain:
        chosen = raw
        reason = "Insufficient development-set improvement over pure Dixon-Coles"
    else:
        chosen = best
        reason = "Lowest development-set log loss with minimum gain threshold"

    return {
        "status": "selected",
        "selected_market_weight": chosen["market_weight"],
        "selection_reason": reason,
        "development_log_loss_gain": float(raw["development_log_loss"] - chosen["development_log_loss"]),
        "audit_log_loss_gain": float(raw["audit_log_loss"] - chosen["audit_log_loss"]),
        "audit_improved": bool(chosen["audit_log_loss"] < raw["audit_log_loss"]),
        "n_usable_matches": len(rows),
        "n_development_matches": len(development),
        "n_audit_matches": len(audit),
        "audit_start": str(audit["date"].min().date()),
        "candidates": comparisons,
        "caveat": (
            "The audit sample did not select the market weight. It is not an "
            "independent final test if other parameters were tuned using these games. "
            "Opening-price availability may differ from live market quotes; "
            "better probability log loss does not establish profitable betting."
        ),
    }
