"""Conservative, *experimental* 1X2 candidate filter.

This module does not place bets or promise winners. It only inspects
pre-match model outputs and rejects fixtures that lack conservative
signals or trustworthy, timely market prices. The thresholds are
heuristics, not optimized or validated for betting profitability.

Two market decisions (home or away win) per fixture, at most two
candidates per UTC fixture date, and a valid empty/no-bet outcome.
"""

from __future__ import annotations

from datetime import datetime, timezone
import math
from typing import Optional, Tuple

import pandas as pd


DOMESTIC_LEAGUES = frozenset({
    "Premier League", "La Liga", "Bundesliga", "Serie A", "Ligue 1"
})
MIN_BLEND_PROBABILITY = 0.65
MIN_RAW_PROBABILITY = 0.50
MIN_ESTIMATED_EV = 0.03
MIN_TEAM_NAME_MATCH_SCORE = 90.0
MAX_1X2_ODDS_AGE_HOURS = 24.0
MIN_MINUTES_UNTIL_KICKOFF = 20.0
MAX_MATCHES_PER_DATE = 2
MIN_COMPLETE_BOOKMAKERS = 2

DECISION_COLUMNS = [
    "evaluated_at_utc", "date", "league", "home_team", "away_team",
    "kickoff_utc", "market", "decision", "rejection_reasons",
    "predicted_probability", "raw_dc_probability", "market_probability",
    "offered_decimal_odds", "bookmaker", "estimated_ev", "raw_dc_ev",
    "estimated_edge", "min_team_name_match_score", "odds_age_hours",
]
SHORTLIST_COLUMNS = DECISION_COLUMNS


def _number(value) -> Optional[float]:
    try:
        x = float(value)
    except (ValueError, TypeError):
        return None
    return x if math.isfinite(x) else None


def _utc(value) -> Optional[pd.Timestamp]:
    if value is None or pd.isna(value):
        return None
    try:
        parsed = pd.to_datetime(value, utc=True, errors="coerce")
    except (ValueError, TypeError, OverflowError):
        return None
    if pd.isna(parsed) or not isinstance(parsed, pd.Timestamp):
        return None
    return parsed


def _valid_probability(value) -> Optional[float]:
    p = _number(value)
    if p is None or not (0.0 <= p <= 1.0):
        return None
    return p


def _evaluate_market(
    row: pd.Series,
    side: str,
    now: pd.Timestamp,
) -> dict:
    reasons = []
    league = str(row.get("league") or "")
    if league not in DOMESTIC_LEAGUES:
        reasons.append("competition not in validated domestic leagues")

    kickoff = _utc(row.get("kickoff_utc"))
    if kickoff is None:
        reasons.append("missing or invalid UTC kickoff")
    elif (kickoff - now).total_seconds() / 60 < MIN_MINUTES_UNTIL_KICKOFF:
        reasons.append("kickoff has passed or is less than 20 minutes away")

    fixture_date = str(row.get("date") or "")
    if kickoff is not None:
        fixture_date = kickoff.date().isoformat()

    source = str(row.get("odds_source") or "")
    if source != "The Odds API" or row.get("market_blend_applied") is not True:
        # pandas bools are usually bool, but coerce explicitly to accept numpy.bool_.
        if source != "The Odds API" or row.get("market_blend_applied") not in (True, 1):
            reasons.append("no complete blended live 1X2 market")

    n_books = _number(row.get("odds_bookmakers_1x2"))
    if n_books is None or n_books < MIN_COMPLETE_BOOKMAKERS:
        reasons.append("fewer than two complete 1X2 bookmakers")

    home_score = _number(row.get("home_name_match_score"))
    away_score = _number(row.get("away_name_match_score"))
    match_quality = min(home_score, away_score) if home_score is not None and away_score is not None else None
    if (
        match_quality is None
        or match_quality < MIN_TEAM_NAME_MATCH_SCORE
        or row.get("model_home_team") in ("__LEAGUE_AVERAGE__", None)
        or row.get("model_away_team") in ("__LEAGUE_AVERAGE__", None)
    ):
        reasons.append("team-model name mapping is low-confidence or unmatched")

    p = _valid_probability(row.get(f"p_{side}"))
    raw_p = _valid_probability(row.get(f"raw_p_{side}"))
    market_p = _valid_probability(row.get(f"market_p_{side}"))

    if p is None or p < MIN_BLEND_PROBABILITY:
        reasons.append("blended win probability below 65% or missing")

    raw_h = _valid_probability(row.get("raw_p_home"))
    raw_d = _valid_probability(row.get("raw_p_draw"))
    raw_a = _valid_probability(row.get("raw_p_away"))
    if (
        raw_p is None or raw_p < MIN_RAW_PROBABILITY
        or any(x is None for x in (raw_h, raw_d, raw_a))
        or raw_p <= max(x for x in (raw_h, raw_d, raw_a) if x is not None and x != raw_p)
        if False else False
    ):
        pass
    # Explicit ordering also handles equal probabilities conservatively.
    if (
        raw_p is None
        or raw_p < MIN_RAW_PROBABILITY
        or any(x is None for x in (raw_h, raw_d, raw_a))
        or (side == "home" and (raw_h <= raw_d or raw_h <= raw_a)
            if all(x is not None for x in (raw_h, raw_d, raw_a)) else False)
        or (side == "away" and (raw_a <= raw_d or raw_a <= raw_h)
            if all(x is not None for x in (raw_h, raw_d, raw_a)) else False)
    ):
        reasons.append("raw Dixon-Coles does not strongly favor this team")

    price = _number(row.get(f"market_{side}_odds"))
    bookmaker = row.get(f"best_{side}_bookmaker")
    if price is None or price <= 1.0 or not isinstance(bookmaker, str) or not bookmaker.strip():
        reasons.append("no verifiable bookmaker and valid live price")

    ref_prices = [_number(row.get(f"market_reference_{s}_odds")) for s in ("home", "draw", "away")]
    if any(x is None or x <= 1.0 for x in ref_prices):
        reasons.append("incomplete coherent reference 1X2 market")

    if market_p is None:
        reasons.append("missing bookmaker reference probability")

    updated = _utc(row.get(f"market_best_{side}_last_update_utc"))
    odds_age = None if updated is None else (now - updated).total_seconds() / 3600.0
    if updated is None or odds_age is None or odds_age < -5.0 / 60.0 or odds_age > MAX_1X2_ODDS_AGE_HOURS:
        reasons.append("bookmaker price is missing, future-dated or over 24 hours old")

    # Compute EV directly from the validated final probability and quoted
    # price rather than blindly trust precomputed CSV fields.
    ev = (p * price - 1.0) if p is not None and price is not None and price > 1.0 else None
    raw_ev = (raw_p * price - 1.0) if raw_p is not None and price is not None and price > 1.0 else None
    edge = p - market_p if p is not None and market_p is not None else None
    if ev is None or ev < MIN_ESTIMATED_EV:
        reasons.append("estimated EV below +3% or missing")

    return {
        "evaluated_at_utc": now.isoformat(),
        "date": fixture_date,
        "league": league,
        "home_team": row.get("home_team"),
        "away_team": row.get("away_team"),
        "kickoff_utc": None if kickoff is None else kickoff.isoformat(),
        "market": "Home win" if side == "home" else "Away win",
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
        "min_team_name_match_score": match_quality,
        "odds_age_hours": odds_age,
    }


def build_conservative_shortlist(
    predictions: pd.DataFrame,
    as_of: Optional[datetime] = None,
) -> Tuple[pd.DataFrame, pd.DataFrame, dict]:
    """Return (shortlist, all market decisions, summary).

    Each independent home/away selection is evaluated. Never force a
    candidate if none pass. Selection is sorted by higher probability
    first, then by larger estimated EV for matches with the same UTC date.
    """
    now = pd.Timestamp(as_of if as_of is not None else datetime.now(timezone.utc))
    if now.tzinfo is None:
        raise ValueError("as_of must be timezone-aware")
    now = now.tz_convert("UTC")

    if predictions.empty:
        decisions = pd.DataFrame(columns=DECISION_COLUMNS)
    else:
        evaluated = []
        for _, row in predictions.iterrows():
            for side in ("home", "away"):
                evaluated.append(_evaluate_market(row, side, now))
        decisions = pd.DataFrame(evaluated, columns=DECISION_COLUMNS)

    eligible = decisions[decisions["decision"] == "ELIGIBLE"].copy()
    eligible = eligible.sort_values(
        ["date", "predicted_probability", "estimated_ev", "kickoff_utc", "home_team", "away_team"],
        ascending=[True, False, False, True, True, True],
        kind="stable",
    )

    # The gate permits at most one 1X2 win selection per fixture. The home
    # and away thresholds make double-eligibility mathematically impossible,
    # but the explicit key also guards future threshold changes.
    eligible = eligible.drop_duplicates(subset=["date", "league", "home_team", "away_team"], keep="first")
    chosen_ids = eligible.groupby("date", sort=False).head(MAX_MATCHES_PER_DATE).index
    overflow_ids = eligible.index.difference(chosen_ids)
    if len(overflow_ids):
        decisions.loc[overflow_ids, "decision"] = "NOT_SELECTED"
        decisions.loc[overflow_ids, "rejection_reasons"] = "exceeded two candidates per UTC matchday"
    if len(chosen_ids):
        decisions.loc[chosen_ids, "decision"] = "SHORTLISTED"
    shortlist = decisions.loc[chosen_ids, SHORTLIST_COLUMNS].copy()
    shortlist = shortlist.sort_values(
        ["date", "predicted_probability", "estimated_ev"], ascending=[True, False, False],
    ).reset_index(drop=True)
    decisions = decisions.reset_index(drop=True)
    count = len(shortlist)
    summary = {
        "status": "CANDIDATES_FOUND" if count else "NO BET",
        "generated_at_utc": now.isoformat(),
        "n_fixtures": int(len(predictions)),
        "n_markets_evaluated": int(len(decisions)),
        "n_shortlisted": int(count),
        "max_matches_per_utc_date": MAX_MATCHES_PER_DATE,
        "n_utc_matchdates": int(shortlist["date"].nunique()) if count else 0,
        "min_blended_probability": MIN_BLEND_PROBABILITY,
        "min_raw_dc_probability": MIN_RAW_PROBABILITY,
        "min_estimated_ev": MIN_ESTIMATED_EV,
        "min_team_name_match_score": MIN_TEAM_NAME_MATCH_SCORE,
        "max_quote_age_hours": MAX_1X2_ODDS_AGE_HOURS,
        "min_minutes_until_kickoff": MIN_MINUTES_UNTIL_KICKOFF,
        "eligible_leagues": sorted(DOMESTIC_LEAGUES),
        "eligible_markets": ["Home win", "Away win"],
        "note": (
            "Experimental, unvalidated selection thresholds, not guaranteed "
            "outcomes, profitability, or a recommendation to place bets. "
            "A NO BET result is valid; no selections are forced."
        ),
    }
    return shortlist, decisions, summary
