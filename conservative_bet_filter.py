"""Experimental ten-match, seven-market shortlist; never guarantee winners.

One market per fixture, up to ten distinct matches across the whole run.
Only select kickoffs within the next 72 hours of the run, including UCL.
Strict selections retain every rule. When fewer than ten qualify, a clearly
marked PROVISIONAL WATCHLIST may include nearest historical-evidence misses,
never malformed odds, stale quotes or unknown teams. It is not a ten-leg
betting recommendation. The strategy is not validated for profitability.
"""

from __future__ import annotations

from datetime import datetime, timezone
import math
from typing import Mapping, Optional, Tuple

import pandas as pd
from quote_policy import load_policy, usable_bookmaker
from quote_freshness import MAX_QUOTE_AGE_HOURS, quote_is_fresh


DOMESTIC_LEAGUES = frozenset({
    "Premier League", "La Liga", "Bundesliga", "Serie A", "Ligue 1"
})
SUPPORTED_LEAGUES = DOMESTIC_LEAGUES | {"UEFA Champions League"}
TARGET_DISTINCT_MATCHES = 10
SHORTLIST_LOOKAHEAD_HOURS = 72.0
MIN_ESTIMATED_EV = 0.015
MIN_BOOKMAKERS = 1
MIN_DOUBLE_CHANCE_ADJUSTED_EV = 0.015
MIN_DOUBLE_CHANCE_ADJUSTED_PROBABILITY = 0.75
MIN_RAW_DC_EV = 0.0
MIN_TEAM_NAME_MATCH_SCORE = 90.0
MAX_ODDS_AGE_HOURS = MAX_QUOTE_AGE_HOURS
MIN_MINUTES_UNTIL_KICKOFF = 20.0
MIN_REFERENCE_OVERROUND = 0.98
MAX_REFERENCE_OVERROUND = 1.20
PROVISIONAL_MIN_EV = 0.015
PROVISIONAL_MAX_PROBABILITY_SHORTFALL = 0.015
PROVISIONAL_MAX_AUDIT_OVERCONFIDENCE = 0.15
PROVISIONAL_MIN_HIGH_AUDIT = 2
PROVISIONAL_MIN_HIGH_DEVELOPMENT = 3

# These deliberately selective heuristic thresholds have not yet
# been optimized or independently backtested for betting profitability.
SELECTION_POLICY_VERSION = "72h-seven-markets-fresh-references-net-ev15-v11"
PROBABILITY_SELECTION_POLICY_VERSION = "72h-top-ten-adjusted-probability-v12"
PREVIOUS_BALANCED_SELECTION_POLICY_VERSION = "48h-top-ten-probability-ev-v13"
BALANCED_SELECTION_POLICY_VERSION = "48h-top-ten-probability-ev-no-under35-v14"
PREVIOUS_SELECTION_POLICY_VERSION = "72h-seven-markets-dc12-btts-probability-odds-net-ev15-v10"
LEGACY_SELECTION_POLICY_VERSION = "72h-six-markets-dc12-probability-odds-net-ev15-v9"
MARKET_SPECS = (
    ("Home win", "home", 0.65, 0.50),
    ("Away win", "away", 0.65, 0.50),
    ("Over 1.5", "over_1_5", 0.78, 0.72),
    ("Both Teams to Score - Yes", "btts_yes", 0.70, 0.63),
    ("Double Chance 1X", "home_draw", 0.80, 0.75),
    ("Double Chance X2", "draw_away", 0.80, 0.75),
    ("Double Chance 12", "home_away", 0.80, 0.75),
)
PROBABILITY_MARKET_SPECS = (*MARKET_SPECS, ("Under 3.5", "under_3_5", 0.80, 0.75))
DECISION_COLUMNS = [
    "evaluated_at_utc", "date", "league", "home_team", "away_team",
    "fixture_id", "kickoff_utc", "market", "decision",
    "rejection_reasons", "predicted_probability", "raw_dc_probability",
    "market_probability", "offered_decimal_odds", "bookmaker",
    "estimated_ev", "gross_estimated_ev", "per_stake_cost", "bookmaker_availability", "raw_dc_ev", "estimated_edge",
    "min_team_name_match_score", "odds_age_hours",
    "validation_status", "development_validation_matches",
    "audit_validation_matches", "audit_brier",
    "calibration_penalty", "rank_probability", "conservative_estimated_ev",
    "high_confidence_tier", "high_confidence_status",
    "high_confidence_audit_matches", "high_confidence_audit_observed_rate",
    "high_confidence_wilson95_lower", "high_confidence_wilson95_upper",
    "high_confidence_penalty",
    "high_confidence_development_matches", "high_confidence_overconfidence",
    "selection_tier", "near_miss_reason", "historical_gap_score",
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
    if key in ("home_draw", "draw_away", "home_away"):
        return {
            "price": row.get(f"market_{key}_odds"),
            "bookmaker": row.get(f"best_{key}_bookmaker"),
            "last_update": row.get(f"market_best_{key}_last_update_utc"),
            "reference": [row.get(f"market_reference_dc_{side}_odds")
                          for side in ("home_draw", "draw_away", "home_away")],
            "book_count": row.get(f"market_{key}_bookmakers"),
            "min_books": MIN_BOOKMAKERS,
        }
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
            "min_books": MIN_BOOKMAKERS,
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
        "min_books": MIN_BOOKMAKERS,
    }


def _evaluate_market(
    row: pd.Series,
    spec: tuple,
    now: pd.Timestamp,
    validation: Optional[Mapping] = None,
    quote_policy: Optional[Mapping] = None,
    adjusted_ev_floor: Optional[float] = None,
    research_policy: Optional[Mapping] = None,
    *, require_fresh_references: bool = True, lookahead_hours: float = SHORTLIST_LOOKAHEAD_HOURS,
) -> dict:
    label, key, min_prob, min_raw = spec
    research = research_policy or {}
    base_min_prob = min_prob
    min_prob += research.get('blended_shift', 0.0)
    min_raw += research.get('raw_shift', 0.0)
    policy = quote_policy or load_policy()
    cost = policy["per_stake_cost_bps"] / 10000
    reasons = []
    league = str(row.get("league") or "")
    if league not in SUPPORTED_LEAGUES:
        reasons.append("competition excluded from shortlist validation")

    kickoff = _utc(row.get("kickoff_utc"))
    if kickoff is None:
        reasons.append("missing or invalid UTC kickoff")
    elif (kickoff - now).total_seconds() / 60.0 < MIN_MINUTES_UNTIL_KICKOFF:
        reasons.append("kickoff has passed or is less than 20 minutes away")
    elif kickoff > now + pd.Timedelta(hours=lookahead_hours):
        reasons.append(f"kickoff outside next {lookahead_hours:g} hours")

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
    high_dev_n, high_overconfidence = None, None
    high_audit_rate, high_wilson_lower, high_wilson_upper = None, None, None
    high_penalty = 0.0
    if validation is None and key in ("home_draw", "draw_away", "home_away"):
        reasons.append("double chance historical reliability report required")
    if validation is None and league == "UEFA Champions League":
        reasons.append("UCL historical reliability report required")
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
            high_dev_n = high_group.get("development", {}).get("n")
            high_overconfidence = high_audit.get("overconfidence")
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
    calibration_penalty = min(1.0, calibration_penalty * research.get('penalty_multiplier', 1.0))
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

    if not usable_bookmaker(bookmaker, policy):
        reasons.append("bookmaker excluded by execution policy (exchange or user allowlist)")

    ref = [_number(x) for x in quote["reference"]]
    if any(x is None or x <= 1.0 for x in ref):
        reasons.append("incomplete same-book reference market")
    elif not (MIN_REFERENCE_OVERROUND * (2 if key in ("home_draw", "draw_away", "home_away") else 1)
              <= sum(1.0 / x for x in ref)
              <= MAX_REFERENCE_OVERROUND * (2 if key in ("home_draw", "draw_away", "home_away") else 1)):
        reasons.append("implausible same-book reference market overround")
    n_books = _number(quote["book_count"])
    if n_books is None or n_books < quote["min_books"]:
        reasons.append("insufficient bookmaker coverage for this market")
    if market_p is None:
        reasons.append("missing bookmaker reference probability")

    if key in ("home_draw", "draw_away", "home_away"):
        reference_time = _utc(row.get(f"market_reference_{key}_last_update_utc"))
        if not quote_is_fresh(reference_time, now):
            reasons.append("double chance reference is missing, stale or future-dated")
    elif require_fresh_references and not quote_is_fresh(row.get(f"market_reference_{key}_last_update_utc"), now):
        reasons.append("reference market is missing, stale or future-dated")
    if require_fresh_references and not quote_is_fresh(row.get("market_reference_1x2_last_update_utc"), now):
        reasons.append("blended 1X2 reference is missing, stale or future-dated")
    updated = _utc(quote["last_update"])
    age = (now - updated).total_seconds() / 3600.0 if updated is not None else None
    if not quote_is_fresh(updated, now):
        reasons.append("specific bookmaker quote is missing, stale or future-dated")

    ev = p * price - 1.0 - cost if p is not None and price is not None and price > 1 else None
    conservative_ev = (
        rank_p * price - 1.0 - cost
        if rank_p is not None and price is not None and price > 1 else None
    )
    raw_ev = raw_p * price - 1.0 - cost if raw_p is not None and price is not None and price > 1 else None
    edge = p - market_p if p is not None and market_p is not None else None
    is_double_chance = key in ("home_draw", "draw_away", "home_away")
    min_adjusted_ev = MIN_DOUBLE_CHANCE_ADJUSTED_EV if is_double_chance else MIN_ESTIMATED_EV
    if adjusted_ev_floor is not None:
        min_adjusted_ev = adjusted_ev_floor
    min_adjusted_probability = (MIN_DOUBLE_CHANCE_ADJUSTED_PROBABILITY if is_double_chance else base_min_prob) + research.get('adjusted_shift', 0.0)
    adjusted_tolerance = 1e-12
    if conservative_ev is None or conservative_ev + adjusted_tolerance < min_adjusted_ev:
        reasons.append(f"reliability-adjusted EV below +{min_adjusted_ev:.1%} or missing")
    if rank_p is None or rank_p + adjusted_tolerance < min_adjusted_probability:
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
        "gross_estimated_ev": p * price - 1.0 if p is not None and price is not None and price > 1 else None,
        "per_stake_cost": cost,
        "bookmaker_availability": policy["account_availability"],
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
        "high_confidence_development_matches": high_dev_n,
        "high_confidence_overconfidence": high_overconfidence,
        "high_confidence_audit_observed_rate": high_audit_rate,
        "high_confidence_wilson95_lower": high_wilson_lower,
        "high_confidence_wilson95_upper": high_wilson_upper,
        "high_confidence_penalty": high_penalty,
        "rank_probability": rank_p,
        "conservative_estimated_ev": conservative_ev,
        "selection_tier": None,
        "near_miss_reason": None,
        "historical_gap_score": None,
    }



def _near_miss_score(row: pd.Series, limits: Mapping[str, tuple], adjusted_ev_floor=None) -> Optional[float]:
    """Small, explicitly quantified deviations for a RESEARCH-ONLY candidate.

    Under no circumstances waive odds authenticity, price freshness,
    training-team coverage, 1X2 agreement or nonnegative raw DC EV.
    A missing audit or a demonstrably very overconfident tier is NOT
    treated as nearly reliable.
    """
    if row.get("market") in ("Double Chance 1X", "Double Chance X2", "Double Chance 12"):
        return None
    if row["decision"] != "REJECTED" or row["validation_status"] != "RELIABLE_FOR_RANKING":
        return None
    problems = str(row["rejection_reasons"] or "").split("; ")
    if not problems or any(not p for p in problems):
        return None
    historical = []
    allowed = {
        "reliability-adjusted EV below +1.5% or missing",
        "reliability-adjusted probability below minimum",
    }
    score = 0.0
    for problem in problems:
        if problem in allowed or problem.startswith("reliability-adjusted EV below +"):
            continue
        if problem.startswith(("75plus market history: ", "85plus market history: ")):
            status = problem.split(": ", 1)[1]
            if status not in (
                "INSUFFICIENT_HIGH_CONFIDENCE_HISTORY",
                "HIGH_CONFIDENCE_OVERESTIMATION",
            ):
                return None
            historical.append(status)
        else:
            return None

    key = str(row["market"])
    min_p, _ = limits[key]
    p = _number(row["rank_probability"])
    ev = _number(row["conservative_estimated_ev"])
    if p is None or p < min_p - PROVISIONAL_MAX_PROBABILITY_SHORTFALL:
        return None
    if ev is None or ev + 1e-12 < (MIN_ESTIMATED_EV if adjusted_ev_floor is None else adjusted_ev_floor):
        return None
    score += max(0.0, min_p-p) / PROVISIONAL_MAX_PROBABILITY_SHORTFALL

    if historical:
        high_n = _number(row["high_confidence_audit_matches"])
        high_status = str(row["high_confidence_status"])
        # The matching audit must contain some real scored fixtures.
        if high_n is None or high_n < PROVISIONAL_MIN_HIGH_AUDIT:
            return None
        if high_status == "HIGH_CONFIDENCE_OVERESTIMATION":
            # The group bias is computed from the reported mean model
            # forecast minus observed rate, never inferred from EV.
            # With only CSV row fields, read the equivalent difference
            # from the historical validation subgroup directly when
            # evaluating near-miss eligibility (passed as a field below).
            overconfidence = _number(row["high_confidence_overconfidence"])
            if overconfidence is None or overconfidence > PROVISIONAL_MAX_AUDIT_OVERCONFIDENCE:
                return None
            score += 2.0 + max(0.0, overconfidence-0.10)/0.05
        elif high_status == "INSUFFICIENT_HIGH_CONFIDENCE_HISTORY":
            high_development = _number(row["high_confidence_development_matches"])
            if high_development is None or high_development < PROVISIONAL_MIN_HIGH_DEVELOPMENT:
                return None
            score += max(0.0, 12.0-high_n)/12.0
            score += max(0.0, 30.0-high_development)/30.0
        else:
            return None
    return round(score, 6)



def _probability_choices(decisions, adjusted_ev_floor=None, *, balanced=False, probability_weight=.5):
    """Rank usable quotes globally; strict-rule failures remain visible warnings."""
    from performance_tracking import fixture_key, canonical_team_key
    soft_prefixes = (
        'blended probability below ', 'raw Dixon-Coles probability below ',
        'reliability-adjusted EV below ', 'reliability-adjusted probability below minimum',
        'independent Dixon-Coles EV is negative or missing',
        'raw Dixon-Coles does not favor chosen winner',
        'market historical reliability: ', '75plus market history: ', '85plus market history: ',
        'missing high-confidence development calibration',
        'double chance historical reliability report required', 'UCL historical reliability report required',
    )
    candidates = []
    if balanced:
        for field in ('probability_percentile', 'ev_percentile', 'selection_score'):
            decisions[field] = None
    for i, row in decisions.iterrows():
        reasons = [x for x in str(row['rejection_reasons']).split('; ') if x]
        if row.get('validation_status') == 'NOT_ASSESSED':
            reasons.append('market historical reliability: NOT_ASSESSED')
            decisions.loc[i, 'rejection_reasons'] = '; '.join(reasons)
        valid = all(_valid_probability(row.get(k)) is not None
                    for k in ('predicted_probability', 'raw_dc_probability', 'rank_probability'))
        valid = valid and all(isinstance(row.get(k), str) and row[k].strip()
                              for k in ('home_team', 'away_team'))
        if valid:
            home, away = (canonical_team_key(row[k]) for k in ('home_team', 'away_team'))
            valid = bool(home and away and home != away)
        hard = [x for x in reasons if not x.startswith(soft_prefixes)]
        ev = _number(row.get('conservative_estimated_ev'))
        if ev is None:
            hard.append('missing finite adjusted EV')
        decisions.loc[i, 'decision'] = 'REJECTED'
        if not valid:
            hard.append('missing valid probability or fixture identity')
        if hard:
            decisions.loc[i, 'rejection_reasons'] = '; '.join(dict.fromkeys(reasons + hard))
            continue
        candidates.append(i)
    pool = decisions.loc[candidates].sort_values(
        ['rank_probability', 'offered_decimal_odds', 'conservative_estimated_ev',
         'kickoff_utc', 'league', 'home_team', 'away_team'],
        ascending=[False, False, False, True, True, True, True], kind='stable')
    pool = pool.assign(_fixture_key=pool.apply(lambda r: fixture_key(r), axis=1)) if len(pool) else pool.assign(_fixture_key=[])
    # Duplicate provider rows must not influence empirical percentile ranks.
    pool = pool.drop_duplicates(['_fixture_key', 'market'])
    if balanced:
        for field, source in [('probability_percentile', 'rank_probability'),
                              ('ev_percentile', 'conservative_estimated_ev')]:
            pool[field] = pool[source].rank(method='average', pct=True)
        pool['selection_score'] = probability_weight*pool.probability_percentile + (1-probability_weight)*pool.ev_percentile
        fields = ['probability_percentile', 'ev_percentile', 'selection_score']
        decisions.loc[pool.index, fields] = pool[fields]
        pool = pool.sort_values(
            ['selection_score', 'rank_probability', 'conservative_estimated_ev',
             'offered_decimal_odds', 'kickoff_utc', 'league', 'home_team', 'away_team'],
            ascending=[False, False, False, False, True, True, True, True], kind='stable')
    if adjusted_ev_floor is not None:
        rejected = pool.index[pool.conservative_estimated_ev + 1e-12 < adjusted_ev_floor]
        for i in rejected:
            reasons = decisions.loc[i, 'rejection_reasons']
            decisions.loc[i, 'rejection_reasons'] = '; '.join(filter(None, [reasons, 'experimental adjusted EV floor not met']))
        pool = pool.drop(index=rejected)
        candidates = [i for i in candidates if i not in rejected]
    top = pool.drop_duplicates('_fixture_key').head(TARGET_DISTINCT_MATCHES)
    strict, ranked = [], []
    for i in candidates:
        if i not in top.index:
            decisions.loc[i, 'decision'] = 'NOT_SELECTED'
            continue
        warning = decisions.loc[i, 'rejection_reasons']
        tier = 'PROVISIONAL' if warning else 'STRICT'
        decisions.loc[i, 'decision'] = 'SHORTLISTED_PROVISIONAL' if warning else 'SHORTLISTED'
        decisions.loc[i, 'selection_tier'] = tier
        decisions.loc[i, 'near_miss_reason'] = warning or None
        (ranked if warning else strict).append(i)
    return pd.Index(strict, dtype='int64'), pd.Index(ranked, dtype='int64'), len(pool.drop_duplicates('_fixture_key'))


def build_conservative_shortlist(
    predictions: pd.DataFrame,
    as_of: Optional[datetime] = None,
    market_reliability: Optional[Mapping[str, Mapping]] = None,
    *, adjusted_ev_floor: Optional[float] = None,
    research_policy: Optional[Mapping] = None,
    execution_policy: Optional[Mapping] = None,
    selection_policy_version: Optional[str] = None,
) -> Tuple[pd.DataFrame, pd.DataFrame, dict]:
    """Aim for ten distinct fixtures; never fabricate a minimum ten.

    Returns shortlist (at most 10 rows), all market decisions, and a
    summary with any shortfall. A shortlisted row is a
    candidate to study, NOT an automatically constructed accumulator.
    """
    now = pd.Timestamp(as_of if as_of is not None else datetime.now(timezone.utc))
    if now.tzinfo is None:
        raise ValueError("as_of must be timezone-aware")
    now = now.tz_convert("UTC")
    policy_version = SELECTION_POLICY_VERSION if selection_policy_version is None else selection_policy_version
    balanced_policy = policy_version in (BALANCED_SELECTION_POLICY_VERSION, PREVIOUS_BALANCED_SELECTION_POLICY_VERSION)
    probability_policy = balanced_policy or policy_version == PROBABILITY_SELECTION_POLICY_VERSION
    lookahead_hours = 48.0 if balanced_policy else SHORTLIST_LOOKAHEAD_HOURS
    if policy_version not in (BALANCED_SELECTION_POLICY_VERSION, PREVIOUS_BALANCED_SELECTION_POLICY_VERSION, PROBABILITY_SELECTION_POLICY_VERSION, SELECTION_POLICY_VERSION, PREVIOUS_SELECTION_POLICY_VERSION, LEGACY_SELECTION_POLICY_VERSION):
        raise ValueError("Unsupported baseline shortlist policy; preserve replay compatibility")
    # Archived v9 comparisons must replay their original six-market ranking.
    specs = tuple(spec for spec in (PROBABILITY_MARKET_SPECS if probability_policy and policy_version != BALANCED_SELECTION_POLICY_VERSION else MARKET_SPECS)
                  if policy_version != LEGACY_SELECTION_POLICY_VERSION or spec[1] != "btts_yes")

    if adjusted_ev_floor is not None and (not math.isfinite(adjusted_ev_floor) or adjusted_ev_floor < MIN_ESTIMATED_EV):
        raise ValueError("Research EV floor must be finite and at least the production floor")
    if research_policy is not None:
        limits = {'blended_shift': (-.03, .03), 'raw_shift': (-.03, .03),
                  'adjusted_shift': (-.03, .03), 'penalty_multiplier': (.5, 1.5),
                  **({'probability_weight': (.25, 1.0)} if policy_version == BALANCED_SELECTION_POLICY_VERSION else {})}
        if not isinstance(research_policy, Mapping) or set(research_policy) - set(limits):
            raise ValueError('Unknown research policy setting')
        for name, value in research_policy.items():
            lo, hi = limits[name]
            if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value) or not lo <= value <= hi:
                raise ValueError('Research policy setting outside fixed bounds')
    probability_weight = (research_policy or {}).get('probability_weight', .5)
    from quote_policy import validate_policy
    policy = load_policy() if execution_policy is None else validate_policy(dict(execution_policy))
    evaluated = []
    for _, row in predictions.iterrows():
        for spec in specs:
            report = (
                market_reliability.get(str(row.get("league") or ""), {})
                if market_reliability is not None else None
            )
            evaluated.append(_evaluate_market(row, spec, now, report, policy, adjusted_ev_floor, research_policy,
                require_fresh_references=policy_version not in (PREVIOUS_SELECTION_POLICY_VERSION, LEGACY_SELECTION_POLICY_VERSION),
                lookahead_hours=lookahead_hours))
    decisions = pd.DataFrame(evaluated, columns=DECISION_COLUMNS)
    original_decisions = decisions.copy() if probability_policy else None

    eligible = decisions[decisions["decision"] == "ELIGIBLE"].copy()
    eligible = eligible.sort_values(
        ["rank_probability", "offered_decimal_odds", "conservative_estimated_ev", "kickoff_utc", "home_team"],
        ascending=[False, False, False, True, True], kind="stable",
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
    # The horizon is a hard eligibility rule above, including provisional picks.
    chosen = top_per_match.head(TARGET_DISTINCT_MATCHES).index

    alternate = eligible.index.difference(top_per_match.index)
    overflow = top_per_match.index.difference(chosen)
    if len(alternate):
        decisions.loc[alternate, "decision"] = "NOT_SELECTED"
        decisions.loc[alternate, "rejection_reasons"] = "higher-ranked market chosen for same match (adjusted probability, then quoted odds)"
    if len(overflow):
        decisions.loc[overflow, "decision"] = "NOT_SELECTED"
        decisions.loc[overflow, "rejection_reasons"] = "below higher-confidence ten-match ranking"
    if len(chosen):
        decisions.loc[chosen, "decision"] = "SHORTLISTED"
        decisions.loc[chosen, "selection_tier"] = "STRICT"

    n_strict = len(chosen)
    provisional_ids = pd.Index([], dtype="int64")
    # A visible research/watchlist supplement: actual strict qualifiers
    # retain their statuses. A near miss is NEVER reclassified as strict.
    if market_reliability is not None and n_strict < TARGET_DISTINCT_MATCHES:
        pool = decisions.loc[decisions["decision"] == "REJECTED"].copy()
        minimums = {
            label: (min_p + (research_policy or {}).get('adjusted_shift', 0.0), min_raw)
            for label, _, min_p, min_raw in specs
        }
        pool["historical_gap_score"] = pool.apply(
            lambda item: _near_miss_score(item, minimums, adjusted_ev_floor), axis=1
        )
        pool = pool.loc[pool["historical_gap_score"].notna()].copy()
        pool = pool.sort_values(
            ["historical_gap_score", "rank_probability", "offered_decimal_odds", "conservative_estimated_ev",
             "kickoff_utc", "home_team"],
            ascending=[True, False, False, False, True, True],
            kind="stable",
        )
        def fixture_keys(table: pd.DataFrame) -> pd.Series:
            ids = table["fixture_id"].fillna("").astype(str)
            names = (
                table["league"].fillna("").astype(str) + "|"
                + table["kickoff_utc"].fillna("").astype(str) + "|"
                + table["home_team"].fillna("").astype(str) + "|"
                + table["away_team"].fillna("").astype(str)
            )
            return ids.where(ids.str.len() > 0, names)

        excluded_keys = set(fixture_keys(decisions.loc[chosen]).tolist())
        pool["_fixture_key"] = fixture_keys(pool)
        pool = pool.loc[~pool["_fixture_key"].isin(excluded_keys)]
        pool = pool.drop_duplicates("_fixture_key", keep="first")
        provisional_ids = pool.head(TARGET_DISTINCT_MATCHES-n_strict).index
        if len(provisional_ids):
            decisions.loc[provisional_ids, "decision"] = "SHORTLISTED_PROVISIONAL"
            decisions.loc[provisional_ids, "selection_tier"] = "PROVISIONAL"
            decisions.loc[provisional_ids, "historical_gap_score"] = (
                pool.loc[provisional_ids, "historical_gap_score"]
            )
            decisions.loc[provisional_ids, "near_miss_reason"] = (
                pool.loc[provisional_ids, "rejection_reasons"]
            )
    if probability_policy:
        decisions = original_decisions
        chosen, provisional_ids, available_fixtures = _probability_choices(decisions, adjusted_ev_floor, balanced=balanced_policy, probability_weight=probability_weight)
        n_strict = len(chosen)
    chosen_all = chosen.append(provisional_ids)
    shortlist = (
        decisions.loc[chosen_all, SHORTLIST_COLUMNS + (['probability_percentile', 'ev_percentile', 'selection_score'] if balanced_policy else [])]
        .sort_values(
            ["selection_tier", "historical_gap_score", "rank_probability",
             "offered_decimal_odds", "conservative_estimated_ev"],
            ascending=[False, True, False, False, False], kind="stable"
        ).reset_index(drop=True)
    )
    decisions = decisions.reset_index(drop=True)
    if probability_policy:
        sort_fields = (['selection_score', 'rank_probability', 'conservative_estimated_ev', 'offered_decimal_odds',
                        'kickoff_utc', 'league', 'home_team', 'away_team'] if balanced_policy else
                       ['rank_probability', 'offered_decimal_odds', 'conservative_estimated_ev',
                        'kickoff_utc', 'league', 'home_team', 'away_team'])
        shortlist = shortlist.sort_values(
            sort_fields, ascending=([False]*4+[True]*4 if balanced_policy else [False]*3+[True]*4),
            kind='stable').reset_index(drop=True)
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
    inside_window = (
        bool(len(kickoff_times))
        and bool((kickoff_times <= now + pd.Timedelta(hours=lookahead_hours)).all())
        and bool((kickoff_times >= now + pd.Timedelta(minutes=MIN_MINUTES_UNTIL_KICKOFF)).all())
    )
    status = (
        "TARGET_MET" if n == TARGET_DISTINCT_MATCHES and not len(provisional_ids)
        else "TARGET_WITH_PROVISIONAL" if n == TARGET_DISTINCT_MATCHES
        else "BELOW_TARGET_WITH_PROVISIONAL" if len(provisional_ids)
        else "BELOW_TARGET" if n
        else "NO BET"
    )
    return shortlist, decisions, {
        "status": status,
        "generated_at_utc": now.isoformat(),
        "selection_policy_version": policy_version,
        "n_fixtures": int(len(predictions)),
        "n_markets_evaluated": int(len(decisions)),
        "n_shortlisted": n,
        "n_strict_qualified": int(n_strict),
        "n_provisional_watchlist": int(len(provisional_ids)),
        "n_total_candidates": n,
        "target_distinct_matches": TARGET_DISTINCT_MATCHES,
        "shortfall": TARGET_DISTINCT_MATCHES - n,
        "shortlist_lookahead_hours": lookahead_hours,
        "shortlist_window_start_utc": now.isoformat(),
        "shortlist_window_end_utc": (
            now + pd.Timedelta(hours=lookahead_hours)
        ).isoformat(),
        "selected_matches_within_72_hours": inside_window,
        **({'selected_matches_within_48_hours': inside_window} if balanced_policy else {}),
        "selected_kickoff_span_hours": actual_span,
        "selected_first_kickoff_utc": (
            first_kickoff.isoformat() if first_kickoff is not None else None
        ),
        "selected_last_kickoff_utc": (
            last_kickoff.isoformat() if last_kickoff is not None else None
        ),
        "selection_method": ("Top ten distinct fixtures within 48 hours; equal-weight adjusted probability and adjusted EV percentile score; strict status does not change ranking" if balanced_policy else
                             "Top ten distinct fixtures within 72 hours; highest adjusted probability, then highest quoted odds; strict status does not change ranking"
                             if probability_policy else "Strict-first ranking within 72 hours; highest adjusted probability, then highest quoted odds"),
        **({'selection_objective': 'BALANCED_PROBABILITY_EV' if balanced_policy else 'PROBABILITY_FIRST', 'usable_distinct_fixtures': available_fixtures,
            'ev_required_for_selection': False, 'probability_thresholds_required_for_selection': False,
            'shortfall_reason': 'Fewer than ten distinct fixtures have usable predictions and fresh allowed-bookmaker quotes inside the window' if n < TARGET_DISTINCT_MATCHES else None}
           if probability_policy else {}),
        **({'ranking_weights': {'adjusted_probability_percentile': probability_weight, 'adjusted_ev_percentile': 1-probability_weight},
            'score_formula': f'{probability_weight:g} * probability_percentile + {1-probability_weight:g} * ev_percentile',
            'score_population': 'usable unique fixture-market candidates within 48 hours before experimental EV filters',
            'ranking_is_empirically_optimized': False} if balanced_policy else {}),
        "eligible_markets": [x[0] for x in specs],
        "eligible_leagues": sorted(SUPPORTED_LEAGUES),
        "quote_execution_policy": policy,
        "min_estimated_ev": MIN_ESTIMATED_EV,
        "min_bookmakers": MIN_BOOKMAKERS,
        "double_chance_min_adjusted_ev": MIN_DOUBLE_CHANCE_ADJUSTED_EV,
        "double_chance_min_adjusted_probability": MIN_DOUBLE_CHANCE_ADJUSTED_PROBABILITY,
        "validation_required": market_reliability is not None,
        "ranking_metric": (
            "equal-weight adjusted probability and adjusted EV percentile score" if balanced_policy else
            "development-calibration-adjusted probability; historical/EV failures are warnings" if probability_policy else
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
        "rule": (
            "Top ten by equal-weight adjusted probability/EV percentile score, one market per fixture, within 48 hours; no probability or EV cutoff" if balanced_policy else
            "Top ten by adjusted probability, one real quoted market per fixture; EV and confidence thresholds annotate qualification rather than limit ranking" if probability_policy else
            "one independently quoted market per distinct fixture; "
            "strict qualifications first, then up to ten clearly labeled "
            "provisional near-miss watchlist candidates"
        ),
        "near_miss_policy": (
            "PROVISIONAL identifies a probability-ranked candidate that fails one or more legacy strict rules, including negative EV or insufficient historical evidence. The warnings are not waived or relabelled as strict qualifications." if probability_policy else
            "PROVISIONAL is not strictly qualified. Only limited "
            "historical sample gaps, modest audit overconfidence, "
            "or small adjusted probability misses are considered; adjusted EV must remain at least +1.5%; "
            "bookmaker sanity, source, timing, team mapping, "
            "raw DC probability and raw EV must remain valid."
        ),
        "warning": (
            "PROVISIONAL picks explicitly FAILED strict historical or EV "
            "requirements and are ONLY an analysis watchlist, not betting "
            "recommendations. No validated guaranteed matches or perfect "
            "betslips exist; ten-leg accumulators have substantial loss risk."
        ),
    }
