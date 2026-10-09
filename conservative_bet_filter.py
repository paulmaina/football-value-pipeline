"""Experimental ten-match, five-market shortlist; never guarantee winners.

One market per fixture, up to ten distinct matches across the whole run.
Prefer a cohort with kickoff timestamps no more than 96 hours apart.
No forced selections: all price, EV, model-agreement and freshness
checks must pass. The strategy is not validated for profitability.
"""

from __future__ import annotations

from datetime import datetime, timezone
import math
from typing import Mapping, Optional, Tuple

import pandas as pd


DOMESTIC_LEAGUES = frozenset({
    "Premier League", "La Liga", "Bundesliga", "Serie A", "Ligue 1"
})
TARGET_DISTINCT_MATCHES = 10
MAX_COMPACT_QUALITY_COST = 0.02  # 2 percentage points mean adjusted probability
MIN_ESTIMATED_EV = 0.03
MIN_RAW_DC_EV = 0.0
MIN_TEAM_NAME_MATCH_SCORE = 90.0
MAX_ODDS_AGE_HOURS = 24.0
MIN_MINUTES_UNTIL_KICKOFF = 20.0

# These deliberately selective heuristic thresholds have not yet
# been optimized or independently backtested for betting profitability.
MARKET_SPECS = (
    ("Home win", "home", 0.65, 0.50),
    ("Away win", "away", 0.65, 0.50),
    ("Over 1.5", "over_1_5", 0.78, 0.72),
    ("Under 3.5", "under_3_5", 0.76, 0.70),
    ("Both Teams to Score - Yes", "btts_yes", 0.70, 0.63),
)
DECISION_COLUMNS = [
    "evaluated_at_utc", "date", "league", "home_team", "away_team",
    "fixture_id", "kickoff_utc", "market", "decision",
    "rejection_reasons", "predicted_probability", "raw_dc_probability",
    "market_probability", "offered_decimal_odds", "bookmaker",
    "estimated_ev", "raw_dc_ev", "estimated_edge",
    "min_team_name_match_score", "odds_age_hours",
    "validation_status", "development_validation_matches",
    "audit_validation_matches", "audit_brier",
    "calibration_penalty", "rank_probability", "conservative_estimated_ev",
    "high_confidence_tier", "high_confidence_status",
    "high_confidence_audit_matches", "high_confidence_audit_observed_rate",
    "high_confidence_wilson95_lower", "high_confidence_wilson95_upper",
    "high_confidence_penalty",
]
SHORTLIST_COLUMNS = DECISION_COLUMNS


def _number(value) -> Optional[float]:
    try:
        x = float(value)
    except (ValueError, TypeError):
        return None
    return x if math.isfinite(x) else None


def _valid_probability(value) -> Optional[float]:
    x = _number(value)
    return x if x is not None and 0.0 <= x <= 1.0 else None


def _utc(value) -> Optional[pd.Timestamp]:
    if value is None:
        return None
    try:
        result = pd.to_datetime(value, utc=True, errors="coerce")
    except (TypeError, ValueError, OverflowError):
        return None
    return result if isinstance(result, pd.Timestamp) and not pd.isna(result) else None


def _market_fields(row: pd.Series, key: str) -> dict:
    """Take the real quoted price, book, complementary market, and timestamp."""
    if key in ("home", "away"):
        return {
            "price": row.get(f"market_{key}_odds"),
            "bookmaker": row.get(f"best_{key}_bookmaker"),
            "last_update": row.get(f"market_best_{key}_last_update_utc"),
            "reference": [
                row.get(f"market_reference_{side}_odds")
                for side in ("home", "draw", "away")
            ],
            "book_count": row.get("odds_bookmakers_1x2"),
            "min_books": 2,
        }
    return {
        "price": row.get(f"market_{key}_odds"),
        "bookmaker": row.get(f"best_{key}_bookmaker"),
        "last_update": row.get(f"market_best_{key}_last_update_utc"),
        "reference": [
            row.get(f"market_reference_{key}_odds"),
            row.get(f"market_reference_{key}_opposite_odds"),
        ],
        "book_count": row.get(f"market_{key}_bookmakers"),
        "min_books": 1,
    }


def _evaluate_market(
    row: pd.Series,
    spec: tuple,
    now: pd.Timestamp,
    validation: Optional[Mapping] = None,
) -> dict:
    label, key, min_prob, min_raw = spec
    reasons = []
    league = str(row.get("league") or "")
    if league not in DOMESTIC_LEAGUES:
        reasons.append("competition excluded from domestic validation")

    kickoff = _utc(row.get("kickoff_utc"))
    if kickoff is None:
        reasons.append("missing or invalid UTC kickoff")
    elif (kickoff - now).total_seconds() / 60.0 < MIN_MINUTES_UNTIL_KICKOFF:
        reasons.append("kickoff has passed or is less than 20 minutes away")

    date = kickoff.date().isoformat() if kickoff is not None else str(row.get("date") or "")
    if row.get("odds_source") != "The Odds API" or row.get("market_blend_applied") not in (True, 1):
        reasons.append("no valid live 50/50 blended market")

    first = _number(row.get("home_name_match_score"))
    second = _number(row.get("away_name_match_score"))
    confidence = min(first, second) if first is not None and second is not None else None
    if (
        confidence is None or confidence < MIN_TEAM_NAME_MATCH_SCORE
        or row.get("model_home_team") in (None, "__LEAGUE_AVERAGE__")
        or row.get("model_away_team") in (None, "__LEAGUE_AVERAGE__")
    ):
        reasons.append("team-model matching unreliable or unknown")

    p = _valid_probability(row.get(f"p_{key}"))
    raw_p = _valid_probability(row.get(f"raw_p_{key}"))
    market_p = _valid_probability(row.get(f"market_p_{key}"))

    # Audit controls market eligibility; earlier development data alone
    # supplies the overconfidence adjustment.
    validation_status = "NOT_ASSESSED"
    calibration_penalty = 0.0
    dev_n, audit_n, audit_brier = None, None, None
    high_tier, high_status, high_audit_n = None, "NOT_REQUIRED", None
    high_audit_rate, high_wilson_lower, high_wilson_upper = None, None, None
    high_penalty = 0.0
    if validation is not None:
        market_validation = validation.get("markets", {}).get(key, {})
        validation_status = market_validation.get(
            "status", "INSUFFICIENT_HISTORY"
        )
        if validation_status != "RELIABLE_FOR_RANKING":
            reasons.append(f"market historical reliability: {validation_status}")
        raw_penalty = _number(market_validation.get("confidence_penalty"))
        if raw_penalty is None or raw_penalty < 0 or raw_penalty > 1:
            reasons.append("invalid or missing market calibration penalty")
        else:
            calibration_penalty = raw_penalty
        dev_n = market_validation.get("development", {}).get("n")
        audit_n = market_validation.get("audit", {}).get("n")
        audit_brier = market_validation.get("audit", {}).get("brier")
        if p is not None and p >= 0.75:
            high_tier = "85plus" if p >= 0.85 else "75plus"
            high_group = market_validation.get("high_confidence", {}).get(
                high_tier, {}
            )
            high_status = high_group.get(
                "status", "INSUFFICIENT_HIGH_CONFIDENCE_HISTORY"
            )
            if high_status != "PASSED":
                reasons.append(f"{high_tier} market history: {high_status}")
            high_audit = high_group.get("audit", {})
            high_audit_n = high_audit.get("n")
            high_audit_rate = high_audit.get("observed_rate")
            interval = high_audit.get("observed_wilson95")
            if isinstance(interval, (list, tuple)) and len(interval) == 2:
                high_wilson_lower, high_wilson_upper = interval
            extra_penalty = _number(
                high_group.get("development_only_penalty")
            )
            if extra_penalty is None or not 0 <= extra_penalty <= 1:
                reasons.append("missing high-confidence development calibration")
            else:
                high_penalty = extra_penalty
                calibration_penalty = max(calibration_penalty, high_penalty)
    rank_p = (
        max(0.0, p - calibration_penalty) if p is not None else None
    )
    if p is None or p < min_prob:
        reasons.append(f"blended probability below {min_prob:.0%} or missing")
    if raw_p is None or raw_p < min_raw:
        reasons.append(f"raw Dixon-Coles probability below {min_raw:.0%} or missing")

    # For winner markets, the unblended 1X2 model must independently
    # favor that same winning side over draw and the opposite team.
    if key in ("home", "away"):
        h = _valid_probability(row.get("raw_p_home"))
        d = _valid_probability(row.get("raw_p_draw"))
        a = _valid_probability(row.get("raw_p_away"))
        if h is None or d is None or a is None or not (
            (key == "home" and h > d and h > a)
            or (key == "away" and a > d and a > h)
        ):
            reasons.append("raw Dixon-Coles does not favor chosen winner")

    quote = _market_fields(row, key)
    price = _number(quote["price"])
    bookmaker = quote["bookmaker"]
    if price is None or price <= 1.0 or not isinstance(bookmaker, str) or not bookmaker.strip():
        reasons.append("no validated bookmaker quote for this exact market")

    ref = [_number(x) for x in quote["reference"]]
    if any(x is None or x <= 1.0 for x in ref):
        reasons.append("incomplete same-book reference market")
    n_books = _number(quote["book_count"])
    if n_books is None or n_books < quote["min_books"]:
        reasons.append("insufficient bookmaker coverage for this market")
    if market_p is None:
        reasons.append("missing bookmaker reference probability")

    updated = _utc(quote["last_update"])
    age = (now - updated).total_seconds() / 3600.0 if updated is not None else None
    if age is None or age > MAX_ODDS_AGE_HOURS or age < -5.0 / 60.0:
        reasons.append("specific bookmaker quote is missing, stale or future-dated")

    ev = p * price - 1.0 if p is not None and price is not None and price > 1 else None
    conservative_ev = (
        rank_p * price - 1.0
        if rank_p is not None and price is not None and price > 1 else None
    )
    raw_ev = raw_p * price - 1.0 if raw_p is not None and price is not None and price > 1 else None
    edge = p - market_p if p is not None and market_p is not None else None
    if conservative_ev is None or conservative_ev < MIN_ESTIMATED_EV:
        reasons.append("reliability-adjusted EV below +3% or missing")
    if rank_p is None or rank_p < min_prob:
        reasons.append("reliability-adjusted probability below minimum")
    if raw_ev is None or raw_ev < MIN_RAW_DC_EV:
        reasons.append("independent Dixon-Coles EV is negative or missing")

    return {
        "evaluated_at_utc": now.isoformat(),
        "date": date,
        "league": league,
        "home_team": row.get("home_team"),
        "away_team": row.get("away_team"),
        "fixture_id": row.get("fixture_id"),
        "kickoff_utc": None if kickoff is None else kickoff.isoformat(),
        "market": label,
        "decision": "ELIGIBLE" if not reasons else "REJECTED",
        "rejection_reasons": "; ".join(reasons),
        "predicted_probability": p,
        "raw_dc_probability": raw_p,
        "market_probability": market_p,
        "offered_decimal_odds": price,
        "bookmaker": bookmaker,
        "estimated_ev": ev,
        "raw_dc_ev": raw_ev,
        "estimated_edge": edge,
        "min_team_name_match_score": confidence,
        "odds_age_hours": age,
        "validation_status": validation_status,
        "development_validation_matches": dev_n,
        "audit_validation_matches": audit_n,
        "audit_brier": audit_brier,
        "calibration_penalty": calibration_penalty,
        "high_confidence_tier": high_tier,
        "high_confidence_status": high_status,
        "high_confidence_audit_matches": high_audit_n,
        "high_confidence_audit_observed_rate": high_audit_rate,
        "high_confidence_wilson95_lower": high_wilson_lower,
        "high_confidence_wilson95_upper": high_wilson_upper,
        "high_confidence_penalty": high_penalty,
        "rank_probability": rank_p,
        "conservative_estimated_ev": conservative_ev,
    }


def build_conservative_shortlist(
    predictions: pd.DataFrame,
    as_of: Optional[datetime] = None,
    market_reliability: Optional[Mapping[str, Mapping]] = None,
) -> Tuple[pd.DataFrame, pd.DataFrame, dict]:
    """Aim for ten distinct fixtures; never fabricate a minimum ten.

    Returns shortlist (at most 10 rows), all market decisions (5 per
    fixture), and a summary with any shortfall. A shortlisted row is a
    candidate to study, NOT an automatically constructed accumulator.
    """
    now = pd.Timestamp(as_of if as_of is not None else datetime.now(timezone.utc))
    if now.tzinfo is None:
        raise ValueError("as_of must be timezone-aware")
    now = now.tz_convert("UTC")

    evaluated = []
    for _, row in predictions.iterrows():
        for spec in MARKET_SPECS:
            report = (
                market_reliability.get(str(row.get("league") or ""), {})
                if market_reliability is not None else None
            )
            evaluated.append(_evaluate_market(row, spec, now, report))
    decisions = pd.DataFrame(evaluated, columns=DECISION_COLUMNS)

    eligible = decisions[decisions["decision"] == "ELIGIBLE"].copy()
    eligible = eligible.sort_values(
        ["rank_probability", "conservative_estimated_ev", "kickoff_utc", "home_team"],
        ascending=[False, False, True, True], kind="stable",
    )

    # One eligible market per distinct fixture (never stack correlated
    # same-game outcomes), then a GLOBAL cap of ten for the entire run.
    id_series = eligible["fixture_id"].fillna("").astype(str)
    fallback = (
        eligible["league"].fillna("").astype(str) + "|"
        + eligible["kickoff_utc"].fillna("").astype(str) + "|"
        + eligible["home_team"].fillna("").astype(str) + "|"
        + eligible["away_team"].fillna("").astype(str)
    )
    eligible["_fixture_key"] = id_series.where(id_series.str.len() > 0, fallback)
    top_per_match = eligible.drop_duplicates("_fixture_key", keep="first").copy()
    top_per_match["_kickoff"] = pd.to_datetime(
        top_per_match["kickoff_utc"], utc=True, errors="coerce"
    )
    # The four-day preference is applied AFTER every independent odds/EV
    # gate and one-market-per-match deduplication. Never lower thresholds.
    # If ten qualifying fixtures can fit in ANY 96-hour interval, choose
    # the highest-probability such cohort. Otherwise retain the best
    # candidates over the full available horizon and explain the shortfall.
    chosen = top_per_match.head(TARGET_DISTINCT_MATCHES).index
    compact_window_available = False
    compact_selected = False
    compact_skipped_for_quality = False
    best_score = None
    best_compact = None
    for start in top_per_match["_kickoff"].dropna().sort_values().unique():
        frame = top_per_match.loc[
            (top_per_match["_kickoff"] >= start)
            & (top_per_match["_kickoff"] <= start + pd.Timedelta(hours=96))
        ]
        if len(frame) < TARGET_DISTINCT_MATCHES:
            continue
        compact_window_available = True
        cohort = frame.head(TARGET_DISTINCT_MATCHES)
        # This cohort score is a preference metric, not a validated
        # probability that all eight games win together.
        score = (
            sum(math.log(float(p)) for p in cohort["rank_probability"]),
            float(cohort["conservative_estimated_ev"].sum()),
        )
        if best_score is None or score > best_score:
            best_score, best_compact = score, cohort

    if best_compact is not None:
        global_quality = float(
            top_per_match.loc[chosen, "rank_probability"].mean()
        )
        compact_quality = float(best_compact["rank_probability"].mean())
        if compact_quality >= global_quality - MAX_COMPACT_QUALITY_COST:
            chosen = best_compact.index
            compact_selected = True
        else:
            compact_skipped_for_quality = True

    alternate = eligible.index.difference(top_per_match.index)
    overflow = top_per_match.index.difference(chosen)
    if len(alternate):
        decisions.loc[alternate, "decision"] = "NOT_SELECTED"
        decisions.loc[alternate, "rejection_reasons"] = "higher-probability market chosen for same match"
    if len(overflow):
        decisions.loc[overflow, "decision"] = "NOT_SELECTED"
        decisions.loc[overflow, "rejection_reasons"] = (
            "outside 96-hour cohort of similarly strong candidates"
            if compact_selected
            else "below higher-confidence ten-match ranking"
        )
    if len(chosen):
        decisions.loc[chosen, "decision"] = "SHORTLISTED"

    shortlist = (
        decisions.loc[chosen, SHORTLIST_COLUMNS]
        .sort_values(["rank_probability", "conservative_estimated_ev"], ascending=[False, False])
        .reset_index(drop=True)
    )
    decisions = decisions.reset_index(drop=True)
    n = len(shortlist)
    kickoff_times = pd.to_datetime(
        shortlist["kickoff_utc"], utc=True, errors="coerce"
    ).dropna()
    first_kickoff = kickoff_times.min() if len(kickoff_times) else None
    last_kickoff = kickoff_times.max() if len(kickoff_times) else None
    actual_span = (
        (last_kickoff - first_kickoff).total_seconds() / 3600.0
        if first_kickoff is not None and last_kickoff is not None else None
    )
    inside_four_days = (
        actual_span is not None and actual_span <= 96.0
    )
    status = "TARGET_MET" if n == TARGET_DISTINCT_MATCHES else (
        "BELOW_TARGET" if n else "NO BET"
    )
    return shortlist, decisions, {
        "status": status,
        "generated_at_utc": now.isoformat(),
        "n_fixtures": int(len(predictions)),
        "n_markets_evaluated": int(len(decisions)),
        "n_shortlisted": n,
        "target_distinct_matches": TARGET_DISTINCT_MATCHES,
        "shortfall": TARGET_DISTINCT_MATCHES - n,
        "four_day_window_preferred": True,
        "eight_match_four_day_window_available": compact_window_available,
        "four_day_window_skipped_for_quality": compact_skipped_for_quality,
        "max_compact_mean_probability_cost": MAX_COMPACT_QUALITY_COST,
        "selected_matches_within_four_days": inside_four_days,
        "selected_kickoff_span_hours": actual_span,
        "selected_first_kickoff_utc": (
            first_kickoff.isoformat() if first_kickoff is not None else None
        ),
        "selected_last_kickoff_utc": (
            last_kickoff.isoformat() if last_kickoff is not None else None
        ),
        "selection_method": (
            "Highest-quality eligible ten-fixture 96-hour cohort within 2pp of best overall"
            if compact_selected else
            "Stronger independently audited candidates prioritized over 96-hour preference"
            if compact_skipped_for_quality else
            "Highest-quality eligible fixtures across full forecast horizon"
        ),
        "eligible_markets": [x[0] for x in MARKET_SPECS],
        "eligible_leagues": sorted(DOMESTIC_LEAGUES),
        "min_estimated_ev": MIN_ESTIMATED_EV,
        "validation_required": market_reliability is not None,
        "ranking_metric": (
            "development-calibration-adjusted probability, audit-qualified"
            if market_reliability is not None else "uncalibrated model probability"
        ),
        "validation_market_statuses": {
            league: {
                key: state.get("status", "INSUFFICIENT_HISTORY")
                for key, state in report.get("markets", {}).items()
            }
            for league, report in (market_reliability or {}).items()
        },
        "min_raw_dc_ev": MIN_RAW_DC_EV,
        "min_team_name_match_score": MIN_TEAM_NAME_MATCH_SCORE,
        "max_quote_age_hours": MAX_ODDS_AGE_HOURS,
        "rule": "one independently quoted market per distinct fixture; no forced picks",
        "warning": (
            "These heuristic thresholds are not validated for betting profit. "
            "There are no guaranteed matches or perfect betslips; ten-leg "
            "accumulators carry substantial all-or-nothing loss risk."
        ),
    }
