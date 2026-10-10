#!/usr/bin/env python3
"""
format_football_output.py

Human-readable football reporting layer. The forward-performance tracker
writes verified results into football_output_v2/performance/; the formatter
never alters those results, snapshots, selections, or the forecasting model.

DEFAULT: If performance tracking exists, produce only one concise file:
    football_output_v2/readable/performance_report.md
The formatter removes previously generated verbose readable exports, but
does not touch football_output_v2/raw/ or football_output_v2/performance/.

OPTIONAL: Generate detailed prediction and conservative-shortlist reports:
    python format_football_output.py --full-reports
If performance tracking is not yet present, legacy prediction formatting
still runs to preserve compatibility with existing forecasting workflows.

Custom directories:
    python format_football_output.py --root-dir football_output_v2
    python format_football_output.py --root-dir football_output_v2 --full-reports

Dependencies: pip install pandas
"""

from __future__ import annotations

import argparse
import json
import math
import re
import shutil
import sys
from pathlib import Path
from typing import Any, Dict, Iterable, List, Mapping, Optional, Sequence, Tuple

import pandas as pd


# ---------------------------------------------------------------------------
# Friendly labels and explanations
# ---------------------------------------------------------------------------

EXPLICIT_LABELS: Dict[str, str] = {
    "league": "League",
    "date": "Match date",
    "home_team": "Home team",
    "away_team": "Away team",
    "fixture_source": "Fixture source",

    "lambda_home": "Expected home goals",
    "lambda_away": "Expected away goals",
    "raw_p_home": "Unadjusted home-win probability",
    "raw_p_draw": "Unadjusted draw probability",
    "raw_p_away": "Unadjusted away-win probability",
    "p_home": "Home-win probability",
    "p_draw": "Draw probability",
    "p_away": "Away-win probability",
    "fair_home": "Fair home odds",
    "fair_draw": "Fair draw odds",
    "fair_away": "Fair away odds",
    "predicted_1x2": "Most likely 1X2 outcome",

    "market_source_1x2": "1X2 market source",
    "market_source_ou25": "O/U 2.5 market source",
    "market_weight": "Market blending weight",
    "market_blend_applied": "Market blend applied",

    "market_home_odds": "Best available home odds",
    "market_draw_odds": "Best available draw odds",
    "market_away_odds": "Best available away odds",
    "market_reference_home_odds": "Reference home odds",
    "market_reference_draw_odds": "Reference draw odds",
    "market_reference_away_odds": "Reference away odds",

    "market_p_home": "Market fair home probability",
    "market_p_draw": "Market fair draw probability",
    "market_p_away": "Market fair away probability",

    "ev_home": "Home expected value",
    "ev_draw": "Draw expected value",
    "ev_away": "Away expected value",
    "edge_home": "Home probability edge",
    "edge_draw": "Draw probability edge",
    "edge_away": "Away probability edge",
    "edge_prob_home": "Home probability edge",
    "edge_prob_draw": "Draw probability edge",
    "edge_prob_away": "Away probability edge",

    "market_over_2_5_odds": "Best Over 2.5 odds",
    "market_under_2_5_odds": "Best Under 2.5 odds",
    "market_reference_over_2_5_odds": "Reference Over 2.5 odds",
    "market_reference_under_2_5_odds": "Reference Under 2.5 odds",
    "market_p_over_2_5": "Market fair Over 2.5 probability",
    "market_p_under_2_5": "Market fair Under 2.5 probability",
    "ev_over_2_5": "Over 2.5 expected value",
    "ev_under_2_5": "Under 2.5 expected value",
    "edge_over_2_5": "Over 2.5 probability edge",
    "edge_under_2_5": "Under 2.5 probability edge",
    "edge_prob_over_2_5": "Over 2.5 probability edge",
    "edge_prob_under_2_5": "Under 2.5 probability edge",

    "model_home_team": "Matched home-team name",
    "model_away_team": "Matched away-team name",
    "home_name_match_score": "Home-name matching confidence",
    "away_name_match_score": "Away-name matching confidence",
    "top_scorelines": "Most likely scorelines",

    # Backtest fields
    "actual_class": "Actual 1X2 outcome",
    "home_goals": "Home goals",
    "away_goals": "Away goals",
    "actual_over_2_5": "Actual Over 2.5",
    "selection": "Selection",
    "model_prob": "Model probability",
    "odds_taken": "Odds taken",
    "edge_ev": "Expected value at bet time",
    "closing_fair_prob": "Closing fair probability",
    "clv": "Closing-line value",
    "won": "Won",
    "stake": "Stake",
    "pnl": "Profit / loss",
    "bankroll_after": "Bankroll after",
}

DIAGNOSTIC_LABELS: Dict[str, str] = {
    "league": "League",
    "training_matches": "Training matches",
    "training_end": "Training data through",
    "fit_success": "Model fit succeeded",
    "objective": "Optimizer objective",
    "base": "Base scoring parameter",
    "home_adv": "Home-advantage parameter",
    "rho": "Dixon-Coles low-score adjustment",
    "half_life_days": "Recency half-life (days)",
    "max_goals": "Maximum goals per team in score matrix",
    "devig_method": "Bookmaker margin-removal method",
    "market_weight": "Market blending weight",
}

TECH_EXPLANATIONS: Dict[str, str] = {
    "Expected goals": (
        "The model's average goal expectation for each team. It is not a prediction "
        "that the team will score exactly that many goals."
    ),
    "Fair odds": (
        "Decimal odds implied by the model probability, before any bookmaker margin."
    ),
    "Expected value": (
        "Model-estimated return per unit staked at the available decimal price. "
        "+5% EV means +0.05 expected units per 1 unit staked under the model; "
        "it is not a guaranteed return."
    ),
    "Probability edge": (
        "Model probability minus the de-vigged market probability."
    ),
    "Fixture source": (
        "Football-Data may include bookmaker prices. A schedule fallback may supply "
        "fixtures without betting prices, so EV fields can legitimately be blank."
    ),
    "Closing-line value": (
        "How the price taken compares with the market's de-vigged closing probability. "
        "Positive CLV over a large sample is generally more informative than short-run ROI."
    ),
}


# ---------------------------------------------------------------------------
# Generic formatting helpers
# ---------------------------------------------------------------------------

def is_missing(value: Any) -> bool:
    if value is None:
        return True
    try:
        missing = pd.isna(value)
        if isinstance(missing, bool):
            return missing
    except Exception:
        pass
    if isinstance(value, str) and value.strip().lower() in {"", "nan", "none", "null"}:
        return True
    return False


def to_float(value: Any) -> Optional[float]:
    if is_missing(value):
        return None
    try:
        number = float(value)
        return number if math.isfinite(number) else None
    except (TypeError, ValueError):
        return None


def pct(value: Any, digits: int = 1) -> str:
    number = to_float(value)
    return "—" if number is None else f"{100 * number:.{digits}f}%"


def decimal(value: Any, digits: int = 2) -> str:
    number = to_float(value)
    return "—" if number is None else f"{number:.{digits}f}"


def signed_pct(value: Any, digits: int = 1) -> str:
    number = to_float(value)
    return "—" if number is None else f"{100 * number:+.{digits}f}%"


def yes_no(value: Any) -> str:
    if is_missing(value):
        return "—"
    if isinstance(value, str):
        v = value.strip().lower()
        if v in {"true", "1", "yes", "y"}:
            return "Yes"
        if v in {"false", "0", "no", "n"}:
            return "No"
    return "Yes" if bool(value) else "No"


def friendly_label(key: str) -> str:
    if key in EXPLICIT_LABELS:
        return EXPLICIT_LABELS[key]

    m = re.fullmatch(r"p_(over|under|push)_(\d+)_(\d+)", key)
    if m:
        side, whole, frac = m.groups()
        return f"{side.title()} {whole}.{frac} probability"

    m = re.fullmatch(r"fair_(over|under)_(\d+)_(\d+)", key)
    if m:
        side, whole, frac = m.groups()
        return f"Fair {side.title()} {whole}.{frac} odds"

    text = key.replace("_", " ").strip()
    return text[:1].upper() + text[1:]


def looks_like_probability(key: str) -> bool:
    return (
        key.startswith("p_")
        or key.startswith("raw_p_")
        or key.startswith("market_p_")
        or key.startswith("edge_prob_")
        or key.startswith("edge_")
        or key.startswith("ev_")
        or key in {
            "model_prob",
            "closing_fair_prob",
            "clv",
            "market_weight",
            "model_accuracy",
            "hit_rate",
            "avg_model_edge",
            "avg_ev_at_bet",
            "avg_clv",
            "pct_positive_clv",
            "roi_on_stake",
            "flat_unit_roi",
            "max_drawdown",
        }
    )


def looks_like_odds(key: str) -> bool:
    return (
        "odds" in key
        or key.startswith("fair_")
        or key in {"avg_odds", "odds_taken"}
    )


def format_value(key: str, value: Any) -> str:
    if is_missing(value):
        return "—"

    if key in {"market_blend_applied", "fit_success", "won", "actual_over_2_5"}:
        return yes_no(value)

    if key == "actual_class":
        mapping = {0: "Home win", 1: "Draw", 2: "Away win", "0": "Home win", "1": "Draw", "2": "Away win"}
        return mapping.get(value, str(value))

    if key == "predicted_1x2":
        mapping = {
            "home": "Home win", "draw": "Draw", "away": "Away win",
            "H": "Home win", "D": "Draw", "A": "Away win",
        }
        return mapping.get(str(value), str(value))

    if key == "selection":
        return {"H": "Home win", "D": "Draw", "A": "Away win"}.get(str(value), str(value))

    if looks_like_probability(key):
        return signed_pct(value) if key.startswith(("ev_", "edge_", "edge_prob_")) or key == "clv" else pct(value)

    if looks_like_odds(key):
        return decimal(value, 2)

    if key in {"lambda_home", "lambda_away", "base", "home_adv", "rho", "objective"}:
        return decimal(value, 3)

    if key.endswith("_name_match_score"):
        number = to_float(value)
        return "—" if number is None else f"{number:.0f}/100"

    number = to_float(value)
    if number is not None:
        if abs(number - round(number)) < 1e-9:
            return f"{int(round(number)):,}"
        return f"{number:,.4f}"

    return str(value)


def md_escape(value: Any) -> str:
    return str(value).replace("|", r"\|").replace("\n", " ").strip()


def markdown_table(headers: Sequence[str], rows: Iterable[Sequence[Any]]) -> str:
    rows = list(rows)
    if not rows:
        return "_No data available._"
    head = "| " + " | ".join(md_escape(x) for x in headers) + " |"
    sep = "| " + " | ".join("---" for _ in headers) + " |"
    body = [
        "| " + " | ".join(md_escape(x) for x in row) + " |"
        for row in rows
    ]
    return "\n".join([head, sep, *body])


# ---------------------------------------------------------------------------
# Scoreline parsing
# ---------------------------------------------------------------------------

def parse_top_scorelines(value: Any) -> List[Tuple[str, float]]:
    """Accept V2's JSON string, a Python-like list already decoded, or malformed blanks."""
    if is_missing(value):
        return []

    data = value
    if isinstance(value, str):
        try:
            data = json.loads(value)
        except json.JSONDecodeError:
            return []

    out: List[Tuple[str, float]] = []
    if isinstance(data, list):
        for item in data:
            if isinstance(item, dict):
                score = item.get("score")
                prob = to_float(item.get("p"))
                if score is not None and prob is not None:
                    out.append((str(score), prob))
            elif isinstance(item, (list, tuple)) and len(item) >= 2:
                prob = to_float(item[1])
                if prob is not None:
                    out.append((str(item[0]), prob))
    return out


def load_scoreline_json(path: Path) -> Dict[str, Dict[str, float]]:
    if not path.exists():
        return {}
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}

    result: Dict[str, Dict[str, float]] = {}
    if isinstance(payload, dict):
        for match_id, scores in payload.items():
            if not isinstance(scores, dict):
                continue
            clean: Dict[str, float] = {}
            for score, p in scores.items():
                prob = to_float(p)
                if prob is not None:
                    clean[str(score)] = prob
            result[str(match_id)] = clean
    return result


def match_id_from_row(row: Mapping[str, Any]) -> str:
    return f"{row.get('date', '')}__{row.get('home_team', '')}__{row.get('away_team', '')}"


def ranked_scorelines(
    row: Mapping[str, Any],
    full_scorelines: Mapping[str, Mapping[str, float]],
    top_n: int,
) -> List[Tuple[str, float]]:
    mid = match_id_from_row(row)
    if mid in full_scorelines:
        return sorted(
            full_scorelines[mid].items(),
            key=lambda x: x[1],
            reverse=True,
        )[:top_n]

    return parse_top_scorelines(row.get("top_scorelines"))[:top_n]


# ---------------------------------------------------------------------------
# Football interpretation helpers
# ---------------------------------------------------------------------------

def outcome_name(code: Any, home: str, away: str) -> str:
    value = str(code).strip().lower()
    if value in {"home", "h", "0"}:
        return f"{home} win"
    if value in {"draw", "d", "1"}:
        return "Draw"
    if value in {"away", "a", "2"}:
        return f"{away} win"
    return str(code)


def model_lean(row: Mapping[str, Any]) -> Tuple[str, Optional[float]]:
    options = [
        (str(row.get("home_team", "Home")) + " win", to_float(row.get("p_home"))),
        ("Draw", to_float(row.get("p_draw"))),
        (str(row.get("away_team", "Away")) + " win", to_float(row.get("p_away"))),
    ]
    valid = [(label, p) for label, p in options if p is not None]
    if not valid:
        return ("Unavailable", None)
    return max(valid, key=lambda x: x[1])


def positive_value_candidates(row: Mapping[str, Any]) -> List[Dict[str, Any]]:
    candidates = [
        ("Home win", "p_home", "market_p_home", "market_home_odds", "ev_home"),
        ("Draw", "p_draw", "market_p_draw", "market_draw_odds", "ev_draw"),
        ("Away win", "p_away", "market_p_away", "market_away_odds", "ev_away"),
        ("Over 2.5", "p_over_2_5", "market_p_over_2_5", "market_over_2_5_odds", "ev_over_2_5"),
        ("Under 2.5", "p_under_2_5", "market_p_under_2_5", "market_under_2_5_odds", "ev_under_2_5"),
    ]

    found: List[Dict[str, Any]] = []
    for label, prob_col, market_prob_col, odds_col, ev_col in candidates:
        ev = to_float(row.get(ev_col))
        odds = to_float(row.get(odds_col))
        if ev is None or odds is None or ev <= 0:
            continue
        found.append({
            "selection": label,
            "model_probability": to_float(row.get(prob_col)),
            "market_probability": to_float(row.get(market_prob_col)),
            "odds": odds,
            "ev": ev,
        })
    return sorted(found, key=lambda x: x["ev"], reverse=True)


def build_match_summary(
    row: Mapping[str, Any],
    scorelines: Sequence[Tuple[str, float]],
) -> str:
    home = str(row.get("home_team", "Home team"))
    away = str(row.get("away_team", "Away team"))

    lean_label, lean_prob = model_lean(row)

    lh = to_float(row.get("lambda_home"))
    la = to_float(row.get("lambda_away"))
    expected_goals = (
        f"Expected goals are {lh:.2f} for {home} and {la:.2f} for {away} "
        f"({lh + la:.2f} combined)."
        if lh is not None and la is not None
        else ""
    )

    top_score = ""
    if scorelines:
        top_score = (
            f"The most likely exact score is {scorelines[0][0]} "
            f"at {100 * scorelines[0][1]:.1f}%."
        )

    totals = []
    for label, col in [
        ("at least one goal", "p_over_0_5"),
        ("Over 2.5 goals", "p_over_2_5"),
        ("Under 3.5 goals", "p_under_3_5"),
        ("Under 4.5 goals", "p_under_4_5"),
        ("BTTS Yes (both teams score)", "p_btts_yes"),
        ("BTTS No (at least one team does not score)", "p_btts_no"),
    ]:
        p = to_float(row.get(col))
        if p is not None:
            totals.append(f"{label}: {100 * p:.1f}%")

    lean = (
        f"The model's most likely 1X2 outcome is **{lean_label}** "
        f"at **{100 * lean_prob:.1f}%**."
        if lean_prob is not None
        else "A 1X2 model probability is not available."
    )

    pieces = [lean]
    if expected_goals:
        pieces.append(expected_goals)
    if top_score:
        pieces.append(top_score)
    if totals:
        pieces.append("Goal-market probabilities: " + "; ".join(totals) + ".")
    return " ".join(pieces)


# ---------------------------------------------------------------------------
# Readable data frames
# ---------------------------------------------------------------------------

def readable_predictions_frame(
    df: pd.DataFrame,
    scorelines: Mapping[str, Mapping[str, float]],
) -> pd.DataFrame:
    rows: List[Dict[str, Any]] = []

    for _, r in df.iterrows():
        row = r.to_dict()
        ranked = ranked_scorelines(row, scorelines, top_n=1)
        top_score = ranked[0][0] if ranked else None
        top_score_p = ranked[0][1] if ranked else None

        lh = to_float(row.get("lambda_home"))
        la = to_float(row.get("lambda_away"))
        lean, lean_p = model_lean(row)
        values = positive_value_candidates(row)
        best_value = values[0] if values else None

        out = {
            "Match date": row.get("date"),
            "League": row.get("league"),
            "Home team": row.get("home_team"),
            "Away team": row.get("away_team"),
            "Fixture source": row.get("fixture_source"),
            "Model lean": lean,
            "Model lean probability": pct(lean_p),
            "Home win": pct(row.get("p_home")),
            "Draw": pct(row.get("p_draw")),
            "Away win": pct(row.get("p_away")),
            "Expected home goals": decimal(lh, 2),
            "Expected away goals": decimal(la, 2),
            "Expected total goals": decimal(
                None if lh is None or la is None else lh + la, 2
            ),
            "Most likely score": top_score or "—",
            "Most likely score probability": pct(top_score_p),
            "Over 0.5": pct(row.get("p_over_0_5")),
            "Over 1.5": pct(row.get("p_over_1_5")),
            "Over 2.5": pct(row.get("p_over_2_5")),
            "Under 2.5": pct(row.get("p_under_2_5")),
            "Over 3.5": pct(row.get("p_over_3_5")),
            "Under 3.5": pct(row.get("p_under_3_5")),
            "Under 4.5": pct(row.get("p_under_4_5")),
            "BTTS Yes": pct(row.get("p_btts_yes")),
            "BTTS No": pct(row.get("p_btts_no")),
            "Home market odds": decimal(row.get("market_home_odds"), 2),
            "Draw market odds": decimal(row.get("market_draw_odds"), 2),
            "Away market odds": decimal(row.get("market_away_odds"), 2),
            "Best model-estimated value": (
                f"{best_value['selection']} ({signed_pct(best_value['ev'])})"
                if best_value else "No positive EV found / no odds available"
            ),
        }
        rows.append(out)

    return pd.DataFrame(rows)


def flattened_scorelines_frame(
    predictions: pd.DataFrame,
    full_scorelines: Mapping[str, Mapping[str, float]],
) -> pd.DataFrame:
    rows: List[Dict[str, Any]] = []

    for _, r in predictions.iterrows():
        row = r.to_dict()
        mid = match_id_from_row(row)

        scores = full_scorelines.get(mid)
        if scores:
            ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        else:
            ranked = parse_top_scorelines(row.get("top_scorelines"))

        for rank, (score, probability) in enumerate(ranked, start=1):
            rows.append({
                "Match date": row.get("date"),
                "League": row.get("league"),
                "Home team": row.get("home_team"),
                "Away team": row.get("away_team"),
                "Rank": rank,
                "Score": score,
                "Probability": pct(probability, 2),
                "Probability (decimal)": probability,
            })

    return pd.DataFrame(rows)


def readable_bets_frame(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        return df.copy()

    friendly = pd.DataFrame()
    for col in df.columns:
        label = friendly_label(col)
        friendly[label] = [format_value(col, x) for x in df[col]]
    return friendly


# ---------------------------------------------------------------------------
# Markdown report generation
# ---------------------------------------------------------------------------

MAIN_MATCH_FIELDS = {
    "league", "date", "home_team", "away_team", "fixture_source",
    "lambda_home", "lambda_away",
    "p_home", "p_draw", "p_away",
    "fair_home", "fair_draw", "fair_away",
    "predicted_1x2", "top_scorelines",
    "p_over_0_5", "p_under_0_5",
    "p_over_1_5", "p_under_1_5",
    "p_over_2_5", "p_under_2_5",
    "p_over_3_5", "p_under_3_5",
    "p_over_4_5", "p_under_4_5",
    "market_home_odds", "market_draw_odds", "market_away_odds",
    "market_p_home", "market_p_draw", "market_p_away",
    "ev_home", "ev_draw", "ev_away",
    "market_over_2_5_odds", "market_under_2_5_odds",
    "market_p_over_2_5", "market_p_under_2_5",
    "ev_over_2_5", "ev_under_2_5",
}


def diagnostics_markdown(diag: Mapping[str, Any]) -> str:
    if not diag:
        return "_No diagnostics file was found._"

    key_rows = []
    for key in [
        "league", "training_matches", "training_end", "fit_success",
        "half_life_days", "max_goals", "devig_method", "market_weight",
    ]:
        if key in diag and not is_missing(diag[key]):
            key_rows.append([
                DIAGNOSTIC_LABELS.get(key, friendly_label(key)),
                format_value(key, diag[key]),
            ])

    appendix_rows = []
    for key, value in diag.items():
        if key in {
            "league", "training_matches", "training_end", "fit_success",
            "half_life_days", "max_goals", "devig_method", "market_weight",
        } or is_missing(value):
            continue
        appendix_rows.append([
            DIAGNOSTIC_LABELS.get(key, friendly_label(key)),
            format_value(key, value),
        ])

    out = ["### Model context", "", markdown_table(["Item", "Value"], key_rows)]
    if appendix_rows:
        out.extend([
            "",
            "<details>",
            "<summary>Technical model diagnostics</summary>",
            "",
            markdown_table(["Parameter", "Value"], appendix_rows),
            "",
            "</details>",
        ])
    return "\n".join(out)


def match_markdown(
    row: Mapping[str, Any],
    full_scorelines: Mapping[str, Mapping[str, float]],
    top_n: int,
    include_technical: bool,
) -> str:
    home = str(row.get("home_team", "Home"))
    away = str(row.get("away_team", "Away"))
    date = str(row.get("date", "Date unavailable"))
    scorelines = ranked_scorelines(row, full_scorelines, top_n=top_n)

    lines = [
        f"## {date} — {home} vs {away}",
        "",
        build_match_summary(row, scorelines),
        "",
    ]

    source = row.get("fixture_source")
    if not is_missing(source):
        lines.append(f"**Fixture source:** {source}")
        lines.append("")

    one_x_two_rows = [
        [home + " win", pct(row.get("p_home")), decimal(row.get("fair_home"))],
        ["Draw", pct(row.get("p_draw")), decimal(row.get("fair_draw"))],
        [away + " win", pct(row.get("p_away")), decimal(row.get("fair_away"))],
    ]
    lines.extend([
        "### Match outcome probabilities",
        "",
        markdown_table(["Outcome", "Model probability", "Model fair odds"], one_x_two_rows),
        "",
    ])

    lh, la = to_float(row.get("lambda_home")), to_float(row.get("lambda_away"))
    goals_rows = []
    if lh is not None:
        goals_rows.append([f"{home} expected goals", f"{lh:.2f}"])
    if la is not None:
        goals_rows.append([f"{away} expected goals", f"{la:.2f}"])
    if lh is not None and la is not None:
        goals_rows.append(["Expected total goals", f"{lh + la:.2f}"])

    for line_value in ("0_5", "1_5", "2_5", "3_5", "4_5"):
        over_key = f"p_over_{line_value}"
        under_key = f"p_under_{line_value}"
        label = line_value.replace("_", ".")
        if over_key in row and not is_missing(row.get(over_key)):
            goals_rows.append([f"Over {label}", pct(row.get(over_key))])
        if under_key in row and not is_missing(row.get(under_key)):
            goals_rows.append([f"Under {label}", pct(row.get(under_key))])

    lines.extend([
        "### Goals outlook",
        "",
        markdown_table(["Measure", "Model estimate"], goals_rows),
        "",
    ])

    if scorelines:
        lines.extend([
            f"### {len(scorelines)} most likely scorelines",
            "",
            markdown_table(
                ["Rank", "Score", "Probability"],
                [[i, score, pct(probability, 2)] for i, (score, probability) in enumerate(scorelines, 1)],
            ),
            "",
        ])

    market_present = any(
        to_float(row.get(c)) is not None
        for c in (
            "market_home_odds", "market_draw_odds", "market_away_odds",
            "market_over_2_5_odds", "market_under_2_5_odds",
        )
    )

    if market_present:
        market_rows = []
        specs = [
            (home + " win", "p_home", "market_p_home", "market_home_odds", "ev_home"),
            ("Draw", "p_draw", "market_p_draw", "market_draw_odds", "ev_draw"),
            (away + " win", "p_away", "market_p_away", "market_away_odds", "ev_away"),
            ("Over 2.5", "p_over_2_5", "market_p_over_2_5", "market_over_2_5_odds", "ev_over_2_5"),
            ("Under 2.5", "p_under_2_5", "market_p_under_2_5", "market_under_2_5_odds", "ev_under_2_5"),
        ]
        for label, model_col, market_col, odds_col, ev_col in specs:
            if all(
                not is_missing(row.get(c))
                for c in (model_col, odds_col)
            ):
                market_rows.append([
                    label,
                    pct(row.get(model_col)),
                    pct(row.get(market_col)),
                    decimal(row.get(odds_col)),
                    signed_pct(row.get(ev_col)),
                ])

        lines.extend([
            "### Market comparison",
            "",
            markdown_table(
                ["Selection", "Model", "Market fair", "Available odds", "Model EV"],
                market_rows,
            ),
            "",
            "_EV is a model estimate, not a guarantee or a recommendation to bet._",
            "",
        ])
    else:
        lines.extend([
            "### Market comparison",
            "",
            "_No bookmaker prices were available in this run. This commonly occurs when "
            "the schedule fallback supplies fixtures before Football-Data publishes its "
            "next odds update. Match probabilities and scoreline estimates are still available._",
            "",
        ])

    if include_technical:
        technical_rows = []
        for key, value in row.items():
            if key in MAIN_MATCH_FIELDS or is_missing(value):
                continue
            technical_rows.append([friendly_label(key), format_value(key, value)])

        if technical_rows:
            lines.extend([
                "<details>",
                "<summary>Additional technical details</summary>",
                "",
                markdown_table(["Field", "Value"], technical_rows),
                "",
                "</details>",
                "",
            ])

    return "\n".join(lines)


def backtest_markdown(
    metrics: Mapping[str, Any],
    bets: Optional[pd.DataFrame],
) -> str:
    if not metrics:
        return ""

    rows = []
    order = [
        "n_predictions",
        "model_log_loss",
        "model_brier",
        "model_accuracy",
        "over_2_5_brier",
        "opening_market_n",
        "opening_market_log_loss",
        "opening_market_brier",
        "closing_market_n",
        "closing_market_log_loss",
        "closing_market_brier",
        "model_minus_closing_log_loss",
    ]
    labels = {
        "n_predictions": "Out-of-sample predictions",
        "model_log_loss": "Model 1X2 log loss",
        "model_brier": "Model 1X2 Brier score",
        "model_accuracy": "Model 1X2 accuracy",
        "over_2_5_brier": "Over 2.5 Brier score",
        "opening_market_n": "Matches with opening market",
        "opening_market_log_loss": "Opening-market log loss",
        "opening_market_brier": "Opening-market Brier score",
        "closing_market_n": "Matches with closing market",
        "closing_market_log_loss": "Closing-market log loss",
        "closing_market_brier": "Closing-market Brier score",
        "model_minus_closing_log_loss": "Model minus closing-line log loss",
    }

    for key in order:
        if key not in metrics or is_missing(metrics[key]):
            continue
        value = metrics[key]
        if key == "model_accuracy":
            display = pct(value)
        elif key in {"n_predictions", "opening_market_n", "closing_market_n"}:
            display = format_value(key, value)
        else:
            display = decimal(value, 4)
        rows.append([labels[key], display])

    lines = [
        "# Historical model evaluation",
        "",
        "These results are from walk-forward testing, where each prediction is made "
        "using only information available before that match.",
        "",
        markdown_table(["Metric", "Result"], rows),
        "",
    ]

    bet_summary = metrics.get("bet_summary")
    if isinstance(bet_summary, dict) and bet_summary:
        br = []
        for key, value in bet_summary.items():
            if key == "flat_unit_roi_95ci" and isinstance(value, list) and len(value) == 2:
                display = f"{signed_pct(value[0])} to {signed_pct(value[1])}"
            elif key in {
                "hit_rate", "avg_ev_at_bet", "avg_clv", "pct_positive_clv",
                "roi_on_stake", "flat_unit_roi", "max_drawdown",
            }:
                display = pct(value) if key in {"hit_rate", "pct_positive_clv", "max_drawdown"} else signed_pct(value)
            elif value is None:
                display = "—"
            else:
                display = format_value(key, value)
            br.append([friendly_label(key), display])

        lines.extend([
            "## Value-bet simulation",
            "",
            markdown_table(["Metric", "Result"], br),
            "",
            "_Short-run ROI can be dominated by variance. Closing-line value and "
            "probability calibration should be evaluated over large samples._",
            "",
        ])

    if bets is not None and not bets.empty:
        lines.extend([
            f"Selected historical bets: **{len(bets):,}**.",
            "",
        ])

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Discovery and orchestration
# ---------------------------------------------------------------------------

def load_json_file(path: Path) -> Dict[str, Any]:
    if not path.exists():
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        return data if isinstance(data, dict) else {}
    except (OSError, json.JSONDecodeError):
        return {}


def discover_prediction_files(input_dir: Path) -> List[Path]:
    files = sorted(input_dir.glob("*_predictions.csv"))
    # Prefer per-league prediction files; avoid duplicating all_leagues if both exist.
    league_files = [
        p for p in files
        if p.name != "all_leagues_predictions.csv"
        and "_backtest_" not in p.name
    ]
    if league_files:
        return league_files

    combined = input_dir / "all_leagues_predictions.csv"
    return [combined] if combined.exists() else []


def league_key_from_path(path: Path) -> str:
    return path.name.removesuffix("_predictions.csv")


def write_readme(output_dir: Path) -> None:
    text = """# Human-readable football reports

This folder is generated by `format_football_output.py`.

## Files

- `performance_report.md` — the single, concise forward-performance review.
- `*_report.md` — narrative report intended for reading and sharing.
- `*_predictions_readable.csv` — compact fixture-level summary for Excel or filtering,
  including **Under 3.5**, **BTTS Yes**, and **BTTS No** model probabilities
  (percentages) alongside the other goal markets.
- `*_scorelines_readable.csv` — flattened scoreline probabilities, ranked per match.
- `*_backtest_bets_readable.csv` — historical selected bets, when backtest files exist.
- `conservative_bet_shortlist_readable.csv` — shortlisted matches with
  **the actual selected betting market** beside each fixture, probability,
  odds, bookmaker, and expected value.
- `conservative_bet_shortlist_report.md` — human-readable shortlist
  plus the four-day kickoff-window status and selection caveats.

The original machine-generated files in `football_output_v2/raw` are not changed.

## Terms

**Model probability** — the pipeline's estimated chance of an outcome.

**Fair odds** — 1 / model probability. These do not include a bookmaker margin.

**Market fair probability** — bookmaker implied probability after the configured
margin-removal method.

**Expected value (EV)** — model probability × available decimal odds − 1.
It is a model estimate, not a guaranteed return.

**Expected goals** — the model's average scoring expectation, not an exact-score forecast.

**Scoreline probability** — estimated probability assigned to a particular final score.

**Closing-line value (CLV)** — compares the price taken with the de-vigged closing
market probability. It is mainly useful when evaluated over many bets.
"""
    (output_dir / "README.md").write_text(text, encoding="utf-8")



def readable_shortlist_frame(df: pd.DataFrame) -> pd.DataFrame:
    """Explain *which market* passed for each shortlisted football fixture.

    The selection is produced by the model pipeline. This formatter never
    changes the market, probabilities, prices, or shortlist membership.
    """
    columns = [
        "Match", "Shortlisted market", "Kickoff (UTC)", "League",
        "Model chance", "Reliability-adjusted chance",
        "Unblended Dixon-Coles chance", "Market implied chance",
        "Bookmaker", "Quoted decimal odds", "Estimated EV",
        "Conservative estimated EV", "Unblended estimated EV",
        "Historical reliability", "High-confidence tier",
        "High-confidence audit matches", "High-confidence observed rate",
        "Observed 95% Wilson lower", "Observed 95% Wilson upper",
        "High-confidence evidence status", "Data/selection status",
        "Qualification", "Near-miss reasons", "Historical gap score",
    ]
    rows: List[Dict[str, str]] = []
    for _, item in df.iterrows():
        home = item.get("home_team")
        away = item.get("away_team")
        fixture = (
            f"{home if not is_missing(home) else 'Unknown home'} vs "
            f"{away if not is_missing(away) else 'Unknown away'}"
        )
        rows.append({
            "Match": fixture,
            "Shortlisted market": (
                str(item.get("market"))
                if not is_missing(item.get("market"))
                else "Market not provided"
            ),
            "Kickoff (UTC)": (
                str(item.get("kickoff_utc"))
                if not is_missing(item.get("kickoff_utc"))
                else "—"
            ),
            "League": (
                str(item.get("league")) if not is_missing(item.get("league")) else "—"
            ),
            "Model chance": pct(item.get("predicted_probability")),
            "Reliability-adjusted chance": pct(item.get("rank_probability")),
            "Unblended Dixon-Coles chance": pct(item.get("raw_dc_probability")),
            "Market implied chance": pct(item.get("market_probability")),
            "Bookmaker": (
                str(item.get("bookmaker"))
                if not is_missing(item.get("bookmaker"))
                else "—"
            ),
            "Quoted decimal odds": decimal(item.get("offered_decimal_odds")),
            "Estimated EV": signed_pct(item.get("estimated_ev")),
            "Conservative estimated EV": signed_pct(
                item.get("conservative_estimated_ev")
            ),
            "Unblended estimated EV": signed_pct(item.get("raw_dc_ev")),
            "Historical reliability": (
                str(item.get("validation_status"))
                if not is_missing(item.get("validation_status"))
                else "Not assessed"
            ),
            "High-confidence tier": (
                str(item.get("high_confidence_tier"))
                if not is_missing(item.get("high_confidence_tier"))
                else "Not applicable"
            ),
            "High-confidence audit matches": (
                str(int(float(item.get("high_confidence_audit_matches"))))
                if to_float(item.get("high_confidence_audit_matches")) is not None
                else "—"
            ),
            "High-confidence observed rate": pct(
                item.get("high_confidence_audit_observed_rate")
            ),
            "Observed 95% Wilson lower": pct(
                item.get("high_confidence_wilson95_lower")
            ),
            "Observed 95% Wilson upper": pct(
                item.get("high_confidence_wilson95_upper")
            ),
            "High-confidence evidence status": (
                str(item.get("high_confidence_status"))
                if not is_missing(item.get("high_confidence_status"))
                else "Not assessed"
            ),
            "Data/selection status": (
                str(item.get("decision"))
                if not is_missing(item.get("decision"))
                else "—"
            ),
            "Qualification": (
                str(item.get("selection_tier"))
                if not is_missing(item.get("selection_tier"))
                else "STRICT" if item.get("decision") == "SHORTLISTED"
                else "Not classified"
            ),
            "Near-miss reasons": (
                str(item.get("near_miss_reason"))
                if not is_missing(item.get("near_miss_reason"))
                else "—"
            ),
            "Historical gap score": (
                decimal(item.get("historical_gap_score"))
                if not is_missing(item.get("historical_gap_score")) else "—"
            ),
        })
    return pd.DataFrame(rows, columns=columns)


def process_conservative_shortlist(
    input_dir: Path,
    output_dir: Path,
) -> Optional[int]:
    """Render the raw shortlist as an Excel-friendly CSV plus Markdown report.

    Only the pipeline may select markets. This function reads but never
    mutates the shortlist or its summary file.
    """
    source = input_dir / "conservative_bet_shortlist.csv"
    if not source.exists():
        # Prevent an obsolete report from appearing current when input
        # has no shortlist, e.g. an older pipeline run.
        for filename in (
            "conservative_bet_shortlist_readable.csv",
            "conservative_bet_shortlist_report.md",
        ):
            (output_dir / filename).unlink(missing_ok=True)
        return None

    try:
        raw = pd.read_csv(source, low_memory=False)
    except pd.errors.EmptyDataError:
        raw = pd.DataFrame()

    summary = load_json_file(input_dir / "conservative_bet_summary.json")
    if "decision" in raw.columns:
        # Fail closed if a mistakenly supplied mixed decision file slips in.
        raw = raw.loc[
            raw["decision"].isin(["SHORTLISTED", "SHORTLISTED_PROVISIONAL"])
        ].copy()

    readable = readable_shortlist_frame(raw)
    readable.to_csv(
        output_dir / "conservative_bet_shortlist_readable.csv",
        index=False,
        encoding="utf-8-sig",
    )

    count = len(readable)
    n_strict = int(summary.get("n_strict_qualified", count))
    n_provisional = int(summary.get("n_provisional_watchlist", 0))
    target = summary.get("target_distinct_matches", 10)
    status = summary.get("status") or ("CANDIDATES_FOUND" if count else "NO BET")
    span = to_float(summary.get("selected_kickoff_span_hours"))
    window = summary.get("selected_matches_within_four_days")
    window_text = (
        "Yes" if window is True else
        "No" if window is False else "Not available"
    )
    generated = summary.get("generated_at_utc") or "not recorded"

    lines = [
        "# Conservative shortlisted matches and markets",
        "",
        f"**Candidates:** {count} of target {target} distinct matches.",
        f"**Strictly qualified:** {n_strict}. **Provisional watchlist:** {n_provisional}.",
        f"**Pipeline status:** {status}.",
        f"**Generated (UTC):** {generated}.",
        (
            "**Kickoffs within 4 days (96 hours):** "
            + window_text
            + (f" (span: {span:.1f} hours)." if span is not None else ".")
        ),
        "",
        "> WARNING: PROVISIONAL watchlist entries FAILED one or more strict "
        "historical/EV rules; they are for research only, NOT qualified bets. "
        "Even STRICT candidates are not guaranteed outcomes or proven "
        "profitable selections. Do not treat ten candidates as a ten-leg betslip.",
        "",
        "## Shortlisted market for each match",
        "",
    ]
    if count:
        headers = [
            "Match", "Shortlisted market", "Qualification", "Kickoff (UTC)",
            "Model chance", "Reliability-adjusted chance",
            "Bookmaker", "Quoted decimal odds", "Conservative estimated EV",
            "Near-miss reasons",
        ]
        lines.append(markdown_table(
            headers,
            [[r[c] for c in headers] for _, r in readable.iterrows()],
        ))
    else:
        lines.append("_No qualifying matches were shortlisted. No bet is a valid outcome._")

    lines.extend([
        "",
        "## Interpretation",
        "",
        "**STRICT** means every configured historical, probability, odds "
        "and EV rule passed. **PROVISIONAL** means the specified historical "
        "or small adjusted-EV checks FAILED, although the essential source, "
        "reference-market integrity, team and price rules passed. "
        "Never count provisional candidates as verified reliable bets. "
        "Model chance describes the selected market, not necessarily the "
        "home or away match winner.",
        "",
        "Reliability-adjusted chance discounts historical overconfidence "
        "using an earlier chronological development sample; a later audit "
        "must pass the predefined quality gate. It remains an estimate.",
        "",
        "When forecast probability is 75% or higher, the chosen market "
        "must separately pass the >=75% historical audit; >=85% forecasts "
        "must pass the >=85% audit. The readable CSV includes the group "
        "sample size, observed rate and Wilson 95% uncertainty range.",
        "",
        "Conservative estimated EV uses that adjusted chance and the quoted "
        "price. Neither the original EV nor the adjusted EV is assured; "
        "bookmaker prices may change before kickoff.",
        "",
        (
            "**Four-day selection:** "
            + str(summary.get("selection_method") or
                  "See the raw summary JSON for selection details.")
        ),
        "",
        "The readable CSV includes raw Dixon-Coles probabilities, "
        "bookmaker-implied probabilities, and unblended EV for audit.",
        "",
    ])
    (output_dir / "conservative_bet_shortlist_report.md").write_text(
        "\n".join(lines), encoding="utf-8"
    )
    return count


def process_league(
    predictions_path: Path,
    input_dir: Path,
    output_dir: Path,
    top_scorelines: int,
    include_technical: bool,
) -> Tuple[str, int]:
    key = league_key_from_path(predictions_path)
    df = pd.read_csv(predictions_path, low_memory=False)

    if df.empty:
        report = (
            f"# {key} football model report\n\n"
            "_The prediction file exists but contains no fixtures._\n"
        )
        (output_dir / f"{key}_report.md").write_text(report, encoding="utf-8")
        return key, 0

    score_path = input_dir / f"{key}_scorelines.json"
    diag_path = input_dir / f"{key}_diagnostics.json"
    metrics_path = input_dir / f"{key}_backtest_metrics.json"
    bets_path = input_dir / f"{key}_backtest_bets.csv"

    scorelines = load_scoreline_json(score_path)
    diagnostics = load_json_file(diag_path)
    metrics = load_json_file(metrics_path)

    readable = readable_predictions_frame(df, scorelines)
    readable.to_csv(
        output_dir / f"{key}_predictions_readable.csv",
        index=False,
        encoding="utf-8-sig",
    )

    flat_scores = flattened_scorelines_frame(df, scorelines)
    if not flat_scores.empty:
        flat_scores.to_csv(
            output_dir / f"{key}_scorelines_readable.csv",
            index=False,
            encoding="utf-8-sig",
        )

    bets: Optional[pd.DataFrame] = None
    if bets_path.exists():
        try:
            bets = pd.read_csv(bets_path, low_memory=False)
        except pd.errors.EmptyDataError:
            bets = pd.DataFrame()

        if bets is not None and not bets.empty:
            readable_bets_frame(bets).to_csv(
                output_dir / f"{key}_backtest_bets_readable.csv",
                index=False,
                encoding="utf-8-sig",
            )

    league_name = (
        str(df["league"].dropna().iloc[0])
        if "league" in df.columns and df["league"].notna().any()
        else key
    )

    lines = [
        f"# {league_name} — football model report",
        "",
        f"Fixtures in this report: **{len(df):,}**.",
        "",
        "> Probabilities are model estimates. They describe uncertainty; they are not "
        "guarantees. Market EV figures are only shown when bookmaker prices are available.",
        "",
        diagnostics_markdown(diagnostics),
        "",
        "## Quick reference",
        "",
        f"- **Expected goals:** {TECH_EXPLANATIONS['Expected goals']}",
        f"- **Fair odds:** {TECH_EXPLANATIONS['Fair odds']}",
        f"- **Expected value:** {TECH_EXPLANATIONS['Expected value']}",
        f"- **Probability edge:** {TECH_EXPLANATIONS['Probability edge']}",
        f"- **Fixture source:** {TECH_EXPLANATIONS['Fixture source']}",
        "",
        "---",
        "",
    ]

    sort_cols = [c for c in ("date", "home_team") if c in df.columns]
    if sort_cols:
        df = df.sort_values(sort_cols, kind="stable")

    for _, r in df.iterrows():
        lines.append(
            match_markdown(
                r.to_dict(),
                scorelines,
                top_n=top_scorelines,
                include_technical=include_technical,
            )
        )
        lines.extend(["", "---", ""])

    if metrics:
        lines.extend([
            "",
            backtest_markdown(metrics, bets),
        ])

    (output_dir / f"{key}_report.md").write_text(
        "\n".join(lines).rstrip() + "\n",
        encoding="utf-8",
    )

    return key, len(df)


def process_combined_file(
    path: Path,
    input_dir: Path,
    output_dir: Path,
    top_scorelines: int,
    include_technical: bool,
) -> List[Tuple[str, int]]:
    df = pd.read_csv(path, low_memory=False)
    if df.empty:
        return []

    if "league" not in df.columns:
        temp = output_dir / "__combined_predictions.csv"
        df.to_csv(temp, index=False)
        result = process_league(
            temp, input_dir, output_dir, top_scorelines, include_technical
        )
        temp.unlink(missing_ok=True)
        return [result]

    results = []
    for league, group in df.groupby("league", dropna=False):
        safe = re.sub(r"[^A-Za-z0-9_-]+", "_", str(league)).strip("_") or "League"
        temp = output_dir / f"{safe}_predictions.csv"
        group.to_csv(temp, index=False)
        result = process_league(
            temp, input_dir, output_dir, top_scorelines, include_technical
        )
        temp.unlink(missing_ok=True)
        results.append(result)
    return results


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="Convert Football Value Pipeline V2 output into reader-friendly reports."
    )
    p.add_argument(
        "--root-dir",
        type=Path,
        default=Path("football_output_v2"),
        help="Main output folder containing raw/ and readable/ (default: football_output_v2).",
    )
    p.add_argument(
        "--input-dir",
        type=Path,
        default=None,
        help=(
            "Optional explicit raw-data folder. If omitted, the formatter uses "
            "<root-dir>/raw when it exists, otherwise <root-dir> for backward compatibility."
        ),
    )
    p.add_argument(
        "--output-dir",
        type=Path,
        default=None,
        help="Optional readable-report folder (default: <root-dir>/readable).",
    )
    p.add_argument(
        "--organize-raw",
        action="store_true",
        help=(
            "Move recognized machine-generated pipeline files currently in <root-dir> "
            "into <root-dir>/raw before formatting. Existing raw files are not overwritten."
        ),
    )
    p.add_argument(
        "--top-scorelines",
        type=int,
        default=5,
        help="Number of likely scores to show in the Markdown report (default: 5).",
    )
    p.add_argument(
        "--no-technical",
        action="store_true",
        help="Hide per-match technical appendix from Markdown reports.",
    )
    p.add_argument(
        "--full-reports", action="store_true",
        help="Also generate detailed per-fixture and conservative-shortlist reports.",
    )
    return p


RAW_FILE_PATTERNS = (
    "*_predictions.csv",
    "*_scorelines.json",
    "*_diagnostics.json",
    "*_backtest_predictions.csv",
    "*_backtest_bets.csv",
    "*_backtest_metrics.json",
    "*_reliability.csv",
    "*_reliability.png",
    "all_leagues_predictions.csv",
    "conservative_bet_shortlist.csv",
    "conservative_bet_rejections.csv",
    "conservative_bet_summary.json",
)


def organize_existing_raw_files(root_dir: Path, raw_dir: Path) -> List[Tuple[Path, Path]]:
    """
    Move known model-generated files from the output root into raw/.

    This is intentionally opt-in via --organize-raw because moving files should
    never be a surprise. Files already in raw/ are left alone, and existing
    destinations are never overwritten.
    """
    raw_dir.mkdir(parents=True, exist_ok=True)
    moved: List[Tuple[Path, Path]] = []
    seen: set[Path] = set()

    for pattern in RAW_FILE_PATTERNS:
        for src in root_dir.glob(pattern):
            if src in seen or not src.is_file():
                continue
            seen.add(src)

            # Do not move formatter outputs or files already under raw/readable.
            if src.parent != root_dir:
                continue
            if "_readable" in src.stem:
                continue

            dst = raw_dir / src.name
            if dst.exists():
                print(
                    f"  ! keeping existing raw file; not moving {src.name}",
                    file=sys.stderr,
                )
                continue

            shutil.move(str(src), str(dst))
            moved.append((src, dst))

    return moved


# ---------------------------------------------------------------------------
# Forward-only live performance: presentation, never re-grading
# ---------------------------------------------------------------------------

PERFORMANCE_STATS_COLUMNS = (
    ("total", "Selections tracked", "count"),
    ("graded", "Verified selections graded", "count"),
    ("wins", "Wins", "count"),
    ("losses", "Losses", "count"),
    ("pending", "Pending / unverified", "count"),
    ("win_rate", "Win rate (graded only)", "rate"),
    ("brier", "Binary Brier (lower is better)", "score"),
    ("settled_with_odds", "Settled selections with recorded odds", "count"),
    ("profit_per_unit_staked", "Total simulated profit (units)", "units"),
    ("flat_stake_roi", "Simulated flat-stake ROI (priced only)", "rate"),
)
PERFORMANCE_STATUS = {
    "WON": "Won", "LOST": "Lost", "GRADED": "Graded",
    "PENDING_KICKOFF_OR_FINAL_SCORE": "Awaiting kickoff or verified 90-minute result",
    "VERIFIED_FINISHED": "Verified finished", "UNMATCHED": "Result not matched",
    "AMBIGUOUS_MATCH": "Ambiguous fixture match",
}


def perf_number(value: Any) -> Optional[float]:
    try:
        result = float(value)
    except (TypeError, ValueError):
        return None
    return result if math.isfinite(result) else None


def perf_format(value: Any, kind: str = "text") -> str:
    number = perf_number(value)
    if value is None or (isinstance(value, str) and not value.strip()):
        return "—"
    if kind in {"rate", "probability"}:
        return f"{number * 100:.1f}%" if number is not None else "—"
    if kind == "signed_rate":
        return f"{number * 100:+.1f}%" if number is not None else "—"
    if kind == "score":
        return f"{number:.4f}" if number is not None else "—"
    if kind == "units":
        return f"{number:+.2f}" if number is not None else "—"
    if kind == "odds":
        return f"{number:.2f}" if number is not None else "—"
    if kind == "count":
        return str(int(number)) if number is not None else "—"
    if kind == "flag":
        return "Correct" if str(value).strip().lower() in {"1", "true"} else (
            "Incorrect" if str(value).strip().lower() in {"0", "false"} else "—"
        )
    if kind == "outcome":
        return {"home": "Home win", "away": "Away win", "draw": "Draw"}.get(str(value).lower(), str(value))
    if kind == "status":
        return PERFORMANCE_STATUS.get(str(value), str(value).replace("_", " ").title())
    if kind == "datetime":
        timestamp = pd.to_datetime(value, errors="coerce", utc=True)
        return timestamp.strftime("%Y-%m-%d %H:%M UTC") if pd.notna(timestamp) else str(value)
    return str(value)


def perf_md_table(headers: Sequence[str], rows: Iterable[Sequence[Any]]) -> str:
    contents = list(rows)
    if not contents:
        return "_No observations yet._"
    def clean(item: Any) -> str:
        return str(item).replace("|", "\\|").replace("\n", " ")
    lines = ["| " + " | ".join(clean(x) for x in headers) + " |",
             "|" + "|".join("---" for _ in headers) + "|"]
    lines += ["| " + " | ".join(clean(x) for x in row) + " |" for row in contents]
    return "\n".join(lines)


def perf_read_csv(path: Path) -> pd.DataFrame:
    if not path.is_file():
        return pd.DataFrame()
    try:
        return pd.read_csv(path, dtype={"source_match_id": "string"}, low_memory=False)
    except pd.errors.EmptyDataError:
        return pd.DataFrame()


def perf_grade_frame(data: pd.DataFrame, *, is_shortlist: bool) -> pd.DataFrame:
    common = [
        ("league", "League", "text"),
        ("home_team", "Home team", "text"),
        ("away_team", "Away team", "text"),
        ("kickoff_utc", "Kickoff (UTC)", "datetime"),
        ("week", "ISO gameweek", "text"),
    ]
    fields = ([
        ("market", "Selected market", "text"),
        ("selection_tier", "Selection tier", "text"),
        ("predicted_probability", "Forecast probability", "probability"),
        ("offered_decimal_odds", "Recorded bookmaker odds", "odds"),
    ] if is_shortlist else [
        ("predicted_1x2", "Most likely 1X2", "outcome"),
        ("predicted_home", "Home-win probability", "probability"),
        ("predicted_draw", "Draw probability", "probability"),
        ("predicted_away", "Away-win probability", "probability"),
    ])
    common += fields + [
        ("final_score", "Verified 90-minute score", "text"),
        ("status", "Verification / grade", "status"),
    ]
    common += ([
        ("unit_profit", "Simulated profit (1 unit stake)", "units"),
        ("brier", "Binary Brier", "score"),
    ] if is_shortlist else [
        ("one_x_two_correct", "Top 1X2 pick", "flag"),
        ("one_x_two_brier", "Multiclass 1X2 Brier", "score"),
        ("over_1_5_correct", "Over 1.5 at 50% threshold", "flag"),
        ("under_3_5_correct", "Under 3.5 at 50% threshold", "flag"),
        ("btts_yes_correct", "BTTS Yes at 50% threshold", "flag"),
        ("btts_no_correct", "BTTS No at 50% threshold", "flag"),
    ])
    common += [
        ("snapshot_commit", "Source snapshot commit", "text"),
        ("snapshot_captured_utc", "Snapshot captured (UTC)", "datetime"),
        ("source_match_id", "Verified source match ID", "text"),
        ("match_source", "Result provider", "text"),
        ("fixture_key", "Source fixture identifier", "text"),
    ]
    output = pd.DataFrame(index=data.index)
    for source, label, kind in common:
        if source in data.columns:
            output[label] = data[source].map(lambda x: perf_format(x, kind) if pd.notna(x) else "—")
    return output.reset_index(drop=True)


def perf_group_frames(metrics: Mapping[str, Any]) -> Dict[str, pd.DataFrame]:
    groups = metrics.get("groups") or {}
    frames: Dict[str, pd.DataFrame] = {}
    if not isinstance(groups, dict):
        return frames
    for key, label in (("tier", "Qualification tier"), ("market", "Market"),
                       ("league", "League"), ("week", "ISO gameweek")):
        payload = groups.get(key) or {}
        if not isinstance(payload, dict):
            continue
        rows = []
        for name, stats in sorted(payload.items()):
            if not isinstance(stats, dict):
                continue
            entry = {label: name}
            for field, heading, kind in PERFORMANCE_STATS_COLUMNS:
                entry[heading] = perf_format(stats.get(field), "signed_rate" if field == "flat_stake_roi" else kind)
            rows.append(entry)
        frames[key] = pd.DataFrame(rows, columns=[label] + [h for _, h, _ in PERFORMANCE_STATS_COLUMNS])
    return frames


def perf_stats_from_grades(rows: pd.DataFrame) -> Dict[str, Any]:
    if rows.empty or "status" not in rows:
        return {"total": len(rows), "graded": 0, "wins": 0, "losses": 0,
                "pending": len(rows), "win_rate": None, "brier": None,
                "settled_with_odds": 0, "profit_per_unit_staked": None, "flat_stake_roi": None}
    status = rows["status"].astype(str)
    wins = int((status == "WON").sum())
    graded_mask = status.isin(["WON", "LOST"])
    graded = int(graded_mask.sum())
    priced = pd.to_numeric(rows.get("unit_profit", pd.Series(index=rows.index, dtype=float)), errors="coerce")
    profit = priced.loc[graded_mask].dropna()
    brier = pd.to_numeric(rows.get("brier", pd.Series(index=rows.index, dtype=float)), errors="coerce").loc[graded_mask].dropna()
    return {
        "total": len(rows), "graded": graded, "wins": wins,
        "losses": graded - wins, "pending": len(rows) - graded,
        "win_rate": wins / graded if graded else None,
        "brier": brier.mean() if not brier.empty else None,
        "settled_with_odds": len(profit),
        "profit_per_unit_staked": profit.sum() if not profit.empty else None,
        "flat_stake_roi": profit.mean() if not profit.empty else None,
    }


def perf_group_stats(data: pd.DataFrame, group: str) -> Dict[str, Dict[str, Any]]:
    if data.empty or group not in data.columns:
        return {}
    return {str(name): perf_stats_from_grades(frame) for name, frame in data.groupby(group, dropna=False)}


def perf_weekly_trend(shortlist: pd.DataFrame) -> pd.DataFrame:
    """Cumulative 1-unit ROI: only verified, priced, settled picks count as stakes."""
    cols = ["ISO gameweek", "Tracked", "Graded", "Wins", "Losses", "Pending",
            "Win rate", "Priced settled", "Week profit (units)", "Week ROI",
            "Cumulative stakes (units)", "Cumulative profit (units)", "Cumulative ROI"]
    if shortlist.empty or "week" not in shortlist:
        return pd.DataFrame(columns=cols)
    rows = []
    stake_total = profit_total = 0.0
    for week, data in sorted(shortlist.groupby("week", dropna=True), key=lambda p: str(p[0])):
        stats = perf_stats_from_grades(data)
        stake_total += stats["settled_with_odds"]
        profit_total += stats["profit_per_unit_staked"] or 0.0
        rows.append([str(week), stats["total"], stats["graded"], stats["wins"], stats["losses"],
                     stats["pending"], perf_format(stats["win_rate"], "rate"),
                     stats["settled_with_odds"], perf_format(stats["profit_per_unit_staked"], "units"),
                     perf_format(stats["flat_stake_roi"], "signed_rate"),
                     int(stake_total), perf_format(profit_total, "units") if stake_total else "—",
                     perf_format(profit_total / stake_total if stake_total else None, "signed_rate")])
    return pd.DataFrame(rows, columns=cols)


def perf_prediction_accuracy(predictions: pd.DataFrame) -> pd.DataFrame:
    columns = ["Prediction type", "Verified predictions scored", "Correct", "Hit rate"]
    if predictions.empty or "status" not in predictions:
        return pd.DataFrame(columns=columns)
    graded = predictions.loc[predictions["status"].astype(str).eq("GRADED")]
    fields = (("one_x_two_correct", "Most likely 1X2"),
              ("over_1_5_correct", "Over 1.5 (50% cutoff)"),
              ("under_3_5_correct", "Under 3.5 (50% cutoff)"),
              ("btts_yes_correct", "BTTS Yes (50% cutoff)"),
              ("btts_no_correct", "BTTS No (50% cutoff)"))
    rows = []
    for field, label in fields:
        if field not in graded:
            continue
        valid = pd.to_numeric(graded[field], errors="coerce").dropna()
        correct = int(valid.eq(1).sum())
        n = len(valid)
        rows.append([label, n, correct, perf_format(correct / n if n else None, "rate")])
    return pd.DataFrame(rows, columns=columns)


def render_performance_reports(performance_dir: Path, readable_dir: Path) -> bool:
    """Write one decision-focused report, using verified tracker files only.

    Presentation only: never score unverified games or modify source data.
    """
    metrics_path = performance_dir / "metrics.json"
    picks_path = performance_dir / "shortlist_grades.csv"
    forecasts_path = performance_dir / "prediction_grades.csv"
    if not any(p.is_file() for p in (metrics_path, picks_path, forecasts_path)):
        return False

    metrics = load_json_file(metrics_path)
    picks = perf_read_csv(picks_path)
    forecasts = perf_read_csv(forecasts_path)
    stats = perf_stats_from_grades(picks)
    graded = stats["graded"]
    priced = stats["settled_with_odds"]
    completed = forecasts.loc[forecasts["status"].eq("GRADED")] if "status" in forecasts else pd.DataFrame()
    brier = (pd.to_numeric(completed["one_x_two_brier"], errors="coerce").dropna()
             if "one_x_two_brier" in completed else pd.Series(dtype=float))

    if graded == 0:
        verdict = "**NOT EVALUABLE YET — no verified shortlisted outcomes.**"
        evidence = "Do not change model parameters or selection thresholds based on pending fixtures."
    elif graded < 30:
        verdict = "**EARLY RESULTS — insufficient evidence for reliable model changes.**"
        evidence = f"Only {graded} selections are graded. Market results are descriptive, not an established edge."
    elif graded < 100:
        verdict = "**PRELIMINARY — useful for investigation, not proof of an edge.**"
        evidence = f"{graded} selections graded. Compare weak markets on new, unseen fixtures before acting."
    else:
        verdict = "**REVIEWABLE TRACK RECORD — confirm by market and out-of-time validation.**"
        evidence = "A larger aggregate sample still cannot establish profitability for each individual market."

    def markdown_stats(group: pd.DataFrame) -> Dict[str, Any]:
        s = perf_stats_from_grades(group)
        return {"graded": s["graded"], "pending": s["pending"],
                "wl": f"{s['wins']}-{s['losses']}" if s["graded"] else "—",
                "hit": perf_format(s["win_rate"], "rate"),
                "roi": perf_format(s["flat_stake_roi"], "signed_rate")}

    market_rows = []
    market_stats = {}
    if "market" in picks:
        for market, group in picks.groupby("market", dropna=False, sort=True):
            s = markdown_stats(group)
            market_stats[str(market)] = (perf_stats_from_grades(group), group)
            market_rows.append([str(market), s["graded"], s["pending"], s["wl"], s["hit"], s["roi"]])

    tier_rows = []
    if "selection_tier" in picks:
        for tier, group in picks.groupby("selection_tier", dropna=False, sort=True):
            s = markdown_stats(group)
            tier_rows.append([str(tier), s["graded"], s["wl"], s["hit"], s["roi"]])

    direction_rows = []
    for col, label in (("one_x_two_correct", "1X2 most likely result"),
                       ("over_1_5_correct", "Over 1.5"),
                       ("under_3_5_correct", "Under 3.5"),
                       ("btts_yes_correct", "BTTS Yes")):
        if col not in completed:
            continue
        values = pd.to_numeric(completed[col], errors="coerce").dropna()
        values = values.loc[values.isin((0, 1))]
        if not values.empty:
            direction_rows.append([label, len(values), perf_format(values.mean(), "rate")])

    calibration = []
    for item in metrics.get("calibration", []):
        if not isinstance(item, dict):
            continue
        n = perf_number(item.get("n"))
        forecast = perf_number(item.get("mean_forecast"))
        observed = perf_number(item.get("observed_win_rate"))
        if n is not None and n >= 20 and forecast is not None and observed is not None:
            calibration.append((abs(observed - forecast), str(item.get("probability_band", "")),
                                int(n), forecast, observed))
    calibration.sort(reverse=True)

    issues = metrics.get("provider_errors") or {}
    if not isinstance(issues, dict):
        issues = {}
    priorities = []
    if issues:
        priorities.append("**Resolve official-result access/matching issues:** " +
                          "; ".join(f"{key}: {str(value)[:130]}" for key, value in sorted(issues.items())) + ".")
    if graded < 30:
        priorities.append("**Collect more forward-verified results.** Archive each forecast before kickoff; grade only matched 90-minute finals. Avoid parameter tuning for now.")
    elif graded < 100:
        priorities.append("**Expand the forward sample.** Monitor market-level outcomes over fresh gameweeks; compare model versions on the same fixtures.")
    if calibration and calibration[0][0] >= 0.10:
        gap, band, n, forecast, observed = calibration[0]
        priorities.append(f"**Audit probability calibration in {band}:** {perf_format(forecast, 'rate')} predicted versus {perf_format(observed, 'rate')} observed (n={n}). Test recalibration only on a separate training window.")
    # A market is worth investigating only after enough actually settled trials.
    suspect = []
    for name, (s, group) in market_stats.items():
        if s["graded"] < 30:
            continue
        actual = group.loc[group["status"].isin(["WON", "LOST"])]
        if "predicted_probability" not in actual:
            continue
        probs = pd.to_numeric(actual["predicted_probability"], errors="coerce").dropna()
        if len(probs) < 30:
            continue
        gap = s["win_rate"] - float(probs.mean())
        if gap < -0.08:
            suspect.append((gap, name, s["graded"]))
    if suspect:
        gap, name, n = min(suspect)
        priorities.append(f"**Audit {name} forecasts:** actual win rate trails the predicted probability by {abs(gap):.1%} across {n} graded selections. Check market-specific calibration and quoted odds before changing filters.")
    if len(priorities) < 3:
        priorities.append("**Benchmark prediction quality:** compare 1X2 Brier and market-specific hit rates against de-vigged bookmaker probabilities on identical verified fixtures; lower Brier alone is not proof of an edge.")
    if len(priorities) < 3:
        priorities.append("**Keep STRICT and PROVISIONAL separate.** Compare their verified ROI and calibration only after each group has sufficient settled observations.")

    lines = [
        "# Football model — performance and improvement review", "",
        "_Forward-only evaluation · all reported results must be verified 90-minute scores_", "",
        "## Verdict", "", verdict, "", evidence, "",
        "## Overall scorecard", "",
        perf_md_table(["Tracked", "Verified", "Pending", "W–L", "Hit rate", "Simulated ROI", "Profit (units)"],
                      [[stats["total"], graded, stats["pending"],
                        f"{stats['wins']}-{stats['losses']}" if graded else "—",
                        perf_format(stats["win_rate"], "rate"),
                        perf_format(stats["flat_stake_roi"], "signed_rate"),
                        perf_format(stats["profit_per_unit_staked"], "units")]]), "",
        f"**ROI sample:** {priced} independently priced, settled selections. Each is simulated at a 1-unit flat stake; no parlays or real-money profit are implied.", "",
        "## What works by market?", "",
        perf_md_table(["Market", "Graded", "Pending", "W–L", "Hit rate", "Sim. ROI"], market_rows), "",
        "_A market needs its own meaningful verified sample. A high hit rate may still lose money at low odds._", "",
        "**STRICT vs PROVISIONAL**", "",
        perf_md_table(["Tier", "Graded", "W–L", "Hit rate", "Sim. ROI"], tier_rows), "",
        "## Forecast quality", "",
        f"**1X2 multiclass Brier (lower is better):** {perf_format(brier.mean() if not brier.empty else None, 'score')} (n={len(brier)})", "",
        perf_md_table(["Prediction", "Verified tests", "Direction correct"], direction_rows), "",
        "_Direction accuracy uses a 50% cutoff for goal/BTTS probabilities; it is not the selected-bet success rate. BTTS No is complementary to BTTS Yes._", "",
    ]
    if calibration:
        _, band, n, forecast, observed = calibration[0]
        lines += [f"**Largest reasonably sampled calibration gap:** {band}, n={n}; average forecast {perf_format(forecast, 'rate')} vs observed {perf_format(observed, 'rate')}. This is exploratory, not a confidence guarantee.", ""]
    else:
        lines += ["**Calibration:** too few verified observations per probability band to draw a meaningful conclusion (minimum shown: 20).", ""]

    lines += ["## Top priorities for model improvement", ""]
    lines.extend(f"{i}. {item}" for i, item in enumerate(priorities[:3], start=1))
    lines += ["", "## Data integrity", "",
              f"Tracker state: **{str(metrics.get('status', 'UNKNOWN')).replace('_', ' ')}**. "
              f"Unverified selections: **{stats['pending']}**; graded full-fixture forecasts: **{len(completed)}**.", "",
              "Only Git-archived pre-kickoff selections and verified regulation-time results count. "
              "Pending/postponed/ambiguous fixtures are **not** losses. "
              "PROVISIONAL selections are exploratory. "
              "The report never updates forecasts, thresholds, source grades or snapshots.", "",
              "_Detailed audit data remains in \`../performance/metrics.json\`, \`shortlist_grades.csv\` and \`prediction_grades.csv\`._", ""]

    readable_dir.mkdir(parents=True, exist_ok=True)
    (readable_dir / "performance_report.md").write_text("\n".join(lines), encoding="utf-8")
    return True


def clear_generated_readable_reports(readable_dir: Path) -> None:
    """Remove only known legacy formatter output, never raw/performance data."""
    generated = ("*_report.md", "*_predictions_readable.csv", "*_scorelines_readable.csv",
                 "*_backtest_bets_readable.csv", "performance_*_readable.csv",
                 "*_grades_readable.csv", "conservative_bet_shortlist_readable.csv",
                 "performance_dashboard.md", "README.md")
    for pattern in generated:
        for candidate in readable_dir.glob(pattern):
            if candidate.is_file() and candidate.name != "performance_report.md":
                candidate.unlink()
    week_dir = readable_dir / "performance_weekly"
    if week_dir.is_dir():
        for candidate in week_dir.glob("*_report.md"):
            if candidate.is_file():
                candidate.unlink()
        if not any(week_dir.iterdir()):
            week_dir.rmdir()


def main(argv: Optional[Sequence[str]] = None) -> int:
    args = build_parser().parse_args(argv)

    root_dir: Path = args.root_dir
    raw_dir = root_dir / "raw"
    readable_dir = root_dir / "readable"

    root_dir.mkdir(parents=True, exist_ok=True)

    if args.organize_raw:
        moved = organize_existing_raw_files(root_dir, raw_dir)
        if moved:
            print(f"Moved {len(moved)} raw pipeline file(s) into: {raw_dir.resolve()}")
            for old, new in moved:
                print(f"  {old.name} -> raw/{new.name}")
        else:
            print("No root-level raw pipeline files needed moving.")

    if args.input_dir is not None:
        input_dir = args.input_dir
    elif raw_dir.exists():
        input_dir = raw_dir
    else:
        # Backward compatibility for existing projects created before raw/ existed.
        input_dir = root_dir

    output_dir: Path = args.output_dir or readable_dir

    if not input_dir.exists():
        raise SystemExit(
            f"Input folder not found: {input_dir}\n"
            "Run the football pipeline first, use --organize-raw, or pass --input-dir."
        )

    output_dir.mkdir(parents=True, exist_ok=True)
    write_readme(output_dir)

    prediction_files = discover_prediction_files(input_dir)
    has_perf = any((root_dir / 'performance' / name).is_file() for name in ('metrics.json', 'shortlist_grades.csv', 'prediction_grades.csv'))
    if has_perf and not args.full_reports:
        if not render_performance_reports(root_dir / "performance", output_dir):
            raise SystemExit("Performance data could not be formatted.")
        clear_generated_readable_reports(output_dir)
        print(f"Single performance report: {(output_dir / 'performance_report.md').resolve()}")
        return 0

    if not prediction_files and not has_perf:
        hint = (
            f"\nRecommended model command:\n"
            f"  python football_value_pipeline_v2_standalone.py "
            f"--leagues EPL --out-dir \"{raw_dir}\""
        )
        raise SystemExit(
            f"No *_predictions.csv files were found in {input_dir}.{hint}"
        )

    processed: List[Tuple[str, int]] = []
    for path in prediction_files:
        if path.name == "all_leagues_predictions.csv":
            processed.extend(
                process_combined_file(
                    path,
                    input_dir,
                    output_dir,
                    top_scorelines=max(1, args.top_scorelines),
                    include_technical=not args.no_technical,
                )
            )
        else:
            processed.append(
                process_league(
                    path,
                    input_dir,
                    output_dir,
                    top_scorelines=max(1, args.top_scorelines),
                    include_technical=not args.no_technical,
                )
            )

    shortlist_count = process_conservative_shortlist(input_dir, output_dir)

    performance_written = render_performance_reports(root_dir / 'performance', output_dir)
    print(f"Raw input folder:       {input_dir.resolve()}")
    print(f"Readable output folder: {output_dir.resolve()}")
    if shortlist_count is not None:
        print(
            f"  Conservative shortlist: {shortlist_count} "
            "match(es), with selected markets (readable CSV and Markdown report)"
        )
    if performance_written:
        print("  Single performance report: performance_report.md")
    for league, count in processed:
        print(f"  {league}: {count} fixture(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
