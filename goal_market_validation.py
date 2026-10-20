"""Chronological goal-market validation, honest price coverage and odds budgets.

Forecasts are produced by the pipeline's existing expanding-window
walk-forward backtest. Match outcomes are used only after the forecast
date. The development split estimates a conservative overconfidence
penalty; the later audit is only a diagnostic / predeclared safety gate.

Historical alternate-total and BTTS prices are not currently contained
in the repository's Football-Data.co.uk CSVs. Never infer prices from
the current API, historical 2.5 prices, or winning probabilities.
"""
from __future__ import annotations

from collections.abc import Mapping, Sequence
import math
import hashlib
import json
from pathlib import Path
from typing import Optional

import numpy as np
import pandas as pd

SUPPORTED_COMPETITIONS = ("EPL", "LaLiga", "Bundesliga", "SerieA", "Ligue1", "UCL")
HIGH_PROBABILITY_THRESHOLDS = (0.75, 0.85)
MIN_HIGH_DEV = 30
MIN_HIGH_AUDIT = 12
MAX_HIGH_AUDIT_OVERCONFIDENCE = 0.10
# The old overall gate allowed Brier to be 0.03 worse than a hindsight
# constant-frequency comparator. Reduce that allowance; still diagnostic.
MAX_OVERALL_BRIER_EXCESS = 0.005
MARKETS = {
    "home_draw": ("p_home_draw", "raw_p_home_draw", "actual_home_draw", 0.80, 0.75),
    "draw_away": ("p_draw_away", "raw_p_draw_away", "actual_draw_away", 0.80, 0.75),
    "home_away": ("p_home_away", "raw_p_home_away", "actual_home_away", 0.80, 0.75),
    "home": ("p_home", "raw_p_home", "actual_home", 0.65, 0.50),
    "away": ("p_away", "raw_p_away", "actual_away", 0.65, 0.50),
    "over_1_5": ("p_over_1_5", "raw_p_over_1_5", "actual_over_1_5", 0.78, 0.72),
    "under_3_5": ("p_under_3_5", "raw_p_under_3_5", "actual_under_3_5", 0.76, 0.70),
    "btts_yes": ("p_btts_yes", "raw_p_btts_yes", "actual_btts_yes", 0.70, 0.63),
}
VALIDATOR_VERSION = 6


def training_fingerprint(history):
    """Include outcomes, identities and price columns used by validation."""
    frame = history.copy(deep=True)
    frame['Date'] = pd.to_datetime(frame['Date'], utc=True)
    frame = frame.reindex(sorted(frame.columns), axis=1).sort_values(
        ['Date', 'HomeTeam', 'AwayTeam'], kind='stable').reset_index(drop=True)
    content = frame.to_json(orient='split', index=False, date_format='iso', double_precision=15).encode()
    observations = history.attrs.get('bbs_statistics_observations')
    if observations:
        content += json.dumps(observations, sort_keys=True, allow_nan=False).encode()
        content += json.dumps({'bbs_statistics_enabled': history.attrs.get('bbs_statistics_enabled', True),
            'bbs_statistics_validation': history.attrs.get('bbs_statistics_validation', 'auto')},
            sort_keys=True).encode()
    return hashlib.sha256(content).hexdigest()


def validation_code_fingerprint():
    root = Path(__file__).resolve().parent
    files = ('goal_market_validation.py', 'football_value_pipeline_v2_standalone.py',
             'score_probability.py', 'double_chance.py', 'match_scores.py', 'bbs_team_aliases.json',
             'bbs_statistics_model.py', 'bbs_integration.py',
             'api_football_data.py', 'api_football_integration.py')
    return hashlib.sha256(b''.join((name.encode()+b'\0'+(root/name).read_bytes()) for name in files)).hexdigest()


def validation_cache_matches(cached: object, config: Mapping) -> bool:
    """Reuse only reports with the current configuration and every market.

    A version bump invalidates reports generated before DC12 was introduced.
    Checking coverage also prevents an incomplete report with a matching
    configuration from silently disabling a supported market.
    """
    return (
        isinstance(cached, dict)
        and isinstance(config, Mapping) and config.get('validator_version') == VALIDATOR_VERSION
        and all(isinstance(config.get(k), str) and len(config[k]) == 64
                and all(c in '0123456789abcdef' for c in config[k])
                for k in ('training_sha256', 'validation_code_sha256'))
        and cached.get("config") == config
        and isinstance(cached.get("markets"), dict)
        and all(isinstance(cached["markets"].get(key), dict)
                and isinstance(cached["markets"][key].get("status"), str)
                for key in MARKETS)
    )

# The following are only *optional exact paired* historical opening
# quotations from one bookmaker. Current source files do not contain
# these columns, so ROI must report UNAVAILABLE.
OPENING_PRICE_PAIRS = {
    "over_1_5": (("B365>1.5", "B365<1.5"), ("PS>1.5", "PS<1.5")),
    "under_3_5": (("B365<3.5", "B365>3.5"), ("PS<3.5", "PS>3.5")),
    "btts_yes": (("B365BTTSY", "B365BTTSN"), ("PSBTTSY", "PSBTTSN")),
}


def distribute_event_odds_budget(
    league_keys: Sequence[str], total: int = 24
) -> dict[str, int]:
    """Fair, deterministic per-league reservation; sum cannot exceed budget."""
    if total < 0:
        raise ValueError("Budget cannot be negative")
    valid = [key for key in SUPPORTED_COMPETITIONS if key in league_keys]
    if not valid:
        return {}
    base, remainder = divmod(total, len(valid))
    return {key: base + int(i < remainder) for i, key in enumerate(valid)}


def prioritized_additional_events(
    rows: Sequence[tuple[Mapping, Mapping]],
    quota: int,
    as_of=None,
    coverage="ranked",
) -> list[int]:
    """Rank *within one league* before spending any quota.

    Each item contains a fixture row and its existing probability output.
    All mode requests every securely linked fixture in the time window,
    regardless of quota or model probability. Ranked mode also applies
    model eligibility gates and the supplied quota.
    Extra markets fetched in one call can then be independently screened.
    """
    if coverage not in {"all", "ranked"}:
        raise ValueError("Unknown additional odds coverage mode")
    candidates: list[tuple[float, int]] = []
    for i, (fixture, pred) in enumerate(rows):
        if as_of is not None:
            from conservative_bet_filter import BALANCED_SHORTLIST_LOOKAHEAD_HOURS, MIN_MINUTES_UNTIL_KICKOFF
            clock = pd.to_datetime(as_of, utc=True)
            kickoff = pd.to_datetime(fixture.get('kickoff_utc'), utc=True, errors='coerce')
            if pd.isna(kickoff) or not (
                clock + pd.Timedelta(minutes=MIN_MINUTES_UNTIL_KICKOFF)
                <= kickoff <= clock + pd.Timedelta(hours=BALANCED_SHORTLIST_LOOKAHEAD_HOURS)
            ):
                continue
        if fixture.get("odds_source") != "The Odds API":
            continue
        event_id = fixture.get("odds_event_id")
        if not isinstance(event_id, str) or not event_id:
            continue
        if coverage == "all":
            candidates.append((0.0, i))
            continue
        try:
            quality = min(float(pred["home_name_match_score"]),
                          float(pred["away_name_match_score"]))
        except (ValueError, TypeError, KeyError):
            continue
        if not math.isfinite(quality) or quality < 90:
            continue
        checks = []
        for key in ("over_1_5", "home_draw", "draw_away", "home_away", "btts_yes"):
            pcol, rcol, _, min_p, min_raw = MARKETS[key]
            try:
                p, raw = float(pred[pcol]), float(pred[rcol])
            except (ValueError, TypeError, KeyError):
                continue
            if math.isfinite(p) and math.isfinite(raw) and p >= min_p and raw >= min_raw:
                checks.append(p)
        if checks:
            candidates.append((max(checks), i))
    ordered = sorted(candidates, key=lambda x: (-x[0], x[1]))
    return [i for _, i in (ordered if coverage == "all" else ordered[:quota])]


def _valid_probability(x) -> bool:
    try:
        y = float(x)
        return math.isfinite(y) and 0.0 <= y <= 1.0
    except (ValueError, TypeError):
        return False


def paired_opening_price(row: Mapping, key: str) -> Optional[float]:
    """Only trust the selected outcome in a complete same-book opening pair."""
    for left, right in OPENING_PRICE_PAIRS.get(key, ()):
        try:
            a, b = float(row[left]), float(row[right])
        except (KeyError, ValueError, TypeError):
            continue
        if math.isfinite(a) and math.isfinite(b) and a > 1 and b > 1:
            return a
    return None


def enrich_historical_goal_markets(row: Mapping, pred: Mapping) -> dict:
    """Add exact full-time settlement and optional real historical price fields."""
    total = int(row["FTHG"]) + int(row["FTAG"])
    goals_h, goals_a = int(row["FTHG"]), int(row["FTAG"])
    result = {
        "actual_home_draw": int(goals_h >= goals_a),
        "actual_draw_away": int(goals_a >= goals_h),
        "actual_home_away": int(goals_h != goals_a),
        "actual_home": int(goals_h > goals_a),
        "actual_away": int(goals_a > goals_h),
        "actual_over_1_5": int(total >= 2),
        "actual_under_3_5": int(total <= 3),
        "actual_btts_yes": int(goals_h >= 1 and goals_a >= 1),
    }
    from double_chance import probabilities
    result.update(probabilities(pred))
    for key in ("home_draw", "draw_away", "home_away"):
        result[f"historical_open_{key}_odds"] = None
    for key in ("over_1_5", "under_3_5", "btts_yes"):
        result[f"p_{key}"] = pred[f"p_{key}"]
        result[f"raw_p_{key}"] = pred[f"raw_p_{key}"]
        result[f"historical_open_{key}_odds"] = paired_opening_price(row, key)
    return result


def _binary_stats(p: np.ndarray, y: np.ndarray) -> dict:
    n = int(len(p))
    if not n:
        return {"n": 0}
    base = float(np.mean(y))
    safe = np.clip(p, 1e-9, 1 - 1e-9)
    brier = float(np.mean((p - y) ** 2))
    return {
        "n": n, "observed_rate": base, "mean_forecast": float(np.mean(p)),
        "overconfidence": float(np.mean(p) - base),
        "brier": brier,
        "baseline_brier": float(np.mean((y - base) ** 2)),
        "log_loss": float(np.mean(-(y*np.log(safe)+(1-y)*np.log(1-safe)))),
    }



def _wilson_interval(successes: int, trials: int, z: float = 1.96) -> list[float] | None:
    """Approximate 95% confidence interval for an observed binary frequency.

    Reports uncertainty, not a guaranteed lower bound on the next fixture.
    """
    if trials <= 0:
        return None
    phat = successes / trials
    z2 = z*z
    center = (phat + z2/(2*trials))/(1+z2/trials)
    half = z*math.sqrt(
        phat*(1-phat)/trials + z2/(4*trials*trials)
    )/(1+z2/trials)
    return [float(max(0.0, center-half)), float(min(1.0, center+half))]


def _high_confidence_group(
    dev_p: np.ndarray, dev_y: np.ndarray,
    audit_p: np.ndarray, audit_y: np.ndarray,
    threshold: float,
) -> dict:
    """Out-of-time assessment for a cumulative >=75% / >=85% forecast group.

    Correction comes from development outcomes only. Audit outcomes may
    reject a group but never set its correction or threshold.
    """
    dmask, amask = dev_p >= threshold, audit_p >= threshold
    dp, dy = dev_p[dmask], dev_y[dmask]
    ap, ay = audit_p[amask], audit_y[amask]
    development, audit = _binary_stats(dp, dy), _binary_stats(ap, ay)
    for stat, y in ((development, dy), (audit, ay)):
        stat["n_wins"] = int(np.sum(y))
        stat["observed_wilson95"] = _wilson_interval(int(np.sum(y)), len(y))

    enough = len(dp) >= MIN_HIGH_DEV and len(ap) >= MIN_HIGH_AUDIT
    if not enough:
        status = "INSUFFICIENT_HIGH_CONFIDENCE_HISTORY"
    elif audit["overconfidence"] > MAX_HIGH_AUDIT_OVERCONFIDENCE:
        status = "HIGH_CONFIDENCE_OVERESTIMATION"
    else:
        status = "PASSED"

    # Shrink development-only high-probability overestimation to avoid
    # treating a moderate, noisy subgroup sample as exact calibration.
    raw_bias = max(0.0, float(development.get("overconfidence", 0.0)))
    penalty = raw_bias * len(dp) / (len(dp) + 30.0) if len(dp) else None
    return {
        "threshold": threshold,
        "status": status,
        "development": development,
        "audit": audit,
        "development_only_penalty": float(penalty) if penalty is not None else None,
        "minimum_development_samples": MIN_HIGH_DEV,
        "minimum_audit_samples": MIN_HIGH_AUDIT,
        "maximum_audit_overconfidence": MAX_HIGH_AUDIT_OVERCONFIDENCE,
    }


def _reliability_bins(p: np.ndarray, y: np.ndarray) -> list[dict]:
    bins = []
    for i in range(5):
        lo, hi = i/5.0, (i+1)/5.0
        mask = (p >= lo) & ((p < hi) if i < 4 else (p <= hi))
        if np.any(mask):
            bins.append({
                "range": [lo, hi], "n": int(mask.sum()),
                "mean_probability": float(p[mask].mean()),
                "observed_frequency": float(y[mask].mean()),
            })
    return bins


def _historical_return(bt: pd.DataFrame, key: str) -> dict:
    """Simulated flat-unit returns at *actual historical opening prices* only."""
    odds_col = f"historical_open_{key}_odds"
    if odds_col not in bt.columns:
        return {"status": "UNAVAILABLE_NO_HISTORICAL_PRICES", "n_quotes": 0,
                "n_simulated": 0, "roi_per_unit": None}
    odds = pd.to_numeric(bt[odds_col], errors="coerce")
    quoted = bt.loc[odds.gt(1) & np.isfinite(odds)].copy()
    if quoted.empty:
        return {"status": "UNAVAILABLE_NO_HISTORICAL_PRICES", "n_quotes": 0,
                "n_simulated": 0, "roi_per_unit": None}
    _, raw_col, outcome_col, min_p, min_raw = MARKETS[key]
    filtered = quoted.loc[
        (quoted[f"p_{key}"] >= min_p)
        & (quoted[raw_col] >= min_raw)
        & (quoted[f"p_{key}"] * quoted[odds_col] - 1 >= 0.03)
        & (quoted[raw_col] * quoted[odds_col] - 1 >= 0.0)
    ]
    wins = pd.to_numeric(filtered[outcome_col], errors="coerce")
    prices = pd.to_numeric(filtered[odds_col], errors="coerce")
    ret = np.where(wins == 1, prices - 1.0, -1.0) if len(filtered) else []
    return {
        "status": "SIMULATED_AT_RECORDED_OPENING_PRICES",
        "n_quotes": int(len(quoted)), "n_simulated": int(len(filtered)),
        "roi_per_unit": float(np.mean(ret)) if len(filtered) else None,
        "win_rate": float(np.mean(wins)) if len(filtered) else None,
        "note": "Exploratory, not a certified out-of-sample betting strategy",
    }


def evaluate_market_history(
    historical: pd.DataFrame,
    league: str,
    min_dev: int = 80,
    min_audit: int = 25,
    audit_fraction: float = 0.25,
) -> dict:
    """Chronological dev/audit, with development-only confidence correction.

    Audit outcomes do NOT choose or fit the overconfidence correction.
    Predeclared safety gates can mark a market as unreliable; an audit
    cannot turn a rejected market into a newly chosen calibration.
    """
    results = {"league": league, "source": "chronological_expanding_window",
               "development_fraction": 1.0 - audit_fraction,
               "markets": {}, "historical_goal_prices_available": False,
               "high_confidence_thresholds": list(HIGH_PROBABILITY_THRESHOLDS),
               "validation_rules": {
                   "high_dev_min": MIN_HIGH_DEV,
                   "high_audit_min": MIN_HIGH_AUDIT,
                   "high_max_overconfidence": MAX_HIGH_AUDIT_OVERCONFIDENCE,
                   "overall_max_brier_excess": MAX_OVERALL_BRIER_EXCESS,
               },
               "caution": (
                   "Development and audit are chronological but may overlap prior "
                   "half-life/market-hyperparameter tuning periods. This is not "
                   "a wholly untouched final holdout."
               )}
    if historical.empty:
        for key in MARKETS:
            results["markets"][key] = {
                "status": "INSUFFICIENT_HISTORY", "development": {"n": 0},
                "audit": {"n": 0}, "confidence_penalty": None,
                "high_confidence": {
                    f"{int(t*100)}plus": _high_confidence_group(
                        np.array([]), np.array([]), np.array([]),
                        np.array([]), t
                    ) for t in HIGH_PROBABILITY_THRESHOLDS
                },
                "historical_betting": {"status": "UNAVAILABLE_NO_HISTORICAL_PRICES",
                                       "n_quotes": 0, "n_simulated": 0, "roi_per_unit": None},
            }
        return results

    ordered = historical.sort_values("date", kind="stable")
    split = min(max(int(len(ordered)*(1-audit_fraction)), 1), len(ordered)-1)
    # Never split a calendar day between development and audit:
    # same-day match results are not necessarily known before kickoff.
    split_date = ordered.iloc[split]["date"]
    dev_frame = ordered.loc[ordered["date"] < split_date]
    audit_frame = ordered.loc[ordered["date"] >= split_date]
    for key, (pcol, _, target_col, _, _) in MARKETS.items():
        def pack(frame):
            if pcol not in frame or target_col not in frame:
                return np.empty(0), np.empty(0)
            p = pd.to_numeric(frame[pcol], errors="coerce")
            y = pd.to_numeric(frame[target_col], errors="coerce")
            valid = p.between(0, 1) & y.isin([0, 1])
            return p[valid].to_numpy(dtype=float), y[valid].to_numpy(dtype=float)

        dev_p, dev_y = pack(dev_frame)
        audit_p, audit_y = pack(audit_frame)
        dev_stats, audit_stats = _binary_stats(dev_p, dev_y), _binary_stats(audit_p, audit_y)
        bias = max(0.0, float(dev_stats.get("overconfidence", 0)))
        penalty = bias * len(dev_p)/(len(dev_p)+100.0) if len(dev_p) else None
        enough = len(dev_p) >= min_dev and len(audit_p) >= min_audit
        audit_is_ok = (
            enough and abs(audit_stats["overconfidence"]) <= 0.12
            and audit_stats["brier"] <= audit_stats["baseline_brier"] + MAX_OVERALL_BRIER_EXCESS
        )
        prices = _historical_return(ordered, key)
        high_groups = {
            f"{int(t*100)}plus": _high_confidence_group(
                dev_p, dev_y, audit_p, audit_y, t
            ) for t in HIGH_PROBABILITY_THRESHOLDS
        }
        results["markets"][key] = {
            "status": ("RELIABLE_FOR_RANKING" if audit_is_ok
                       else "INSUFFICIENT_HISTORY" if not enough
                       else "UNRELIABLE_AUDIT"),
            "development": dev_stats, "audit": audit_stats,
            "high_confidence": high_groups,
            "development_bins": _reliability_bins(dev_p, dev_y),
            "audit_bins": _reliability_bins(audit_p, audit_y),
            "confidence_penalty": float(penalty) if penalty is not None else None,
            "historical_betting": prices,
        }
        if prices["n_quotes"]:
            results["historical_goal_prices_available"] = True
    return results
