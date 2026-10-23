#!/usr/bin/env python3
"""
format_football_output.py

Human-readable reporting layer for the Football Value Pipeline V2.

The model pipeline writes machine-friendly CSV/JSON files into
`football_output_v2/raw`. This script DOES NOT modify those raw files.

Recommended directory structure:

    football_output_v2/
    ├── raw/
    │   ├── EPL_predictions.csv
    │   ├── EPL_scorelines.json
    │   ├── EPL_diagnostics.json
    │   └── ...
    └── readable/
        ├── EPL_report.md
        ├── EPL_predictions_readable.csv
        └── ...

For backward compatibility, if `football_output_v2/raw` does not exist, the
script will also look directly inside `football_output_v2`.

It creates a `readable/` subfolder containing:
  - <LEAGUE>_report.md
  - <LEAGUE>_predictions_readable.csv
  - <LEAGUE>_scorelines_readable.csv
  - <LEAGUE>_backtest_bets_readable.csv   (if backtest data exists)
  - README.md

Design goals
------------
1. Preserve raw model outputs untouched.
2. Translate technical fields into football-friendly labels.
3. Present probabilities as percentages and odds as decimal odds.
4. Parse JSON scoreline structures safely.
5. Work even when some optional market/backtest fields are absent.
6. Keep important technical details available in a compact appendix.

Usage
-----
    python format_football_output.py

    python format_football_output.py \
        --input-dir football_output_v2 \
        --output-dir football_output_v2/readable

    python format_football_output.py --top-scorelines 8

Dependencies
------------
    pip install pandas
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
        ("Double Chance 1X", "p_home_draw"),
        ("Double Chance X2", "p_draw_away"),
        ("Double Chance 12 (either team wins)", "p_home_away"),
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
            "Double Chance 1X": pct(row.get("p_home_draw")),
            "Double Chance X2": pct(row.get("p_draw_away")),
            "Double Chance 12": pct(row.get("p_home_away")),
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
    if 'p_no_loss' in df.columns:
        columns += ['Any loss chance','Conservative loss estimate','Full refund chance','Full win chance',
                    'Half win chance','Half loss chance','Full loss chance','Probability meaning']
    if 'loss_risk_tolerance' in df.columns:
        columns += ['Minimum eligible loss estimate','Allowed risk difference']
    if 'selection_warnings' in df.columns:
        columns += ['Value warning', 'Quote checked (UTC)']
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
            "Value warning": item.get('selection_warnings') or '—',
            "Quote checked (UTC)": item.get('quote_last_update_utc') or '—',
            "Any loss chance": pct(item.get('p_any_loss')),
            "Conservative loss estimate": pct(item.get('loss_probability_upper')),
            "Full refund chance": pct(item.get('p_refund')),
            "Full win chance": pct(item.get('p_full_win')),
            "Half win chance": pct(item.get('p_half_win')),
            "Half loss chance": pct(item.get('p_half_loss')),
            "Full loss chance": pct(item.get('p_full_loss')),
            "Probability meaning": item.get('probability_basis') or 'win',
            "Minimum eligible loss estimate": pct(item.get('fixture_minimum_loss_probability')),
            "Allowed risk difference": pct(item.get('loss_risk_tolerance')),
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
    if 'selection_score' in df.columns:
        for output, source in [('Combined ranking score', 'selection_score'),
                               ('Probability percentile', 'probability_percentile'),
                               ('EV percentile', 'ev_percentile')]:
            columns.append(output)
            for result, (_, original) in zip(rows, df.iterrows()):
                value = to_float(original.get(source))
                result[output] = (decimal(100*value) + ' / 100' if value is not None else '—') if source == 'selection_score' else pct(value)
    return pd.DataFrame(rows, columns=columns)


def add_shortlist_alternatives(readable, raw, input_dir, summary):
    """Explain frozen candidate decisions without changing the selected picks."""
    from asian_handicap import qualifying_alternatives
    path = input_dir / 'conservative_bet_rejections.csv'
    alternatives = {}
    available = set()
    from performance_tracking import fixture_key
    if path.exists():
        try:
            decisions = pd.read_csv(path, low_memory=False)
        except pd.errors.EmptyDataError:
            decisions = pd.DataFrame()
        if not decisions.empty:
            alternatives = qualifying_alternatives(raw, decisions, summary['loss_risk_tolerance'])
            available = {(fixture_key(r), pd.Timestamp(r['evaluated_at_utc'])) for r in decisions.to_dict('records')}
    fields = ['Alternative market', 'Alternative bookmaker', 'Alternative odds',
              'Alternative loss chance', 'Alternative conservative loss estimate',
              'Alternative refund chance', 'Alternative adjusted EV', 'Alternative unblended EV',
              'Alternative risk increase', 'Alternative comparison']
    for field in fields:
        readable[field] = '—'
    for pos, (idx, pick) in enumerate(raw.iterrows()):
        alternative = alternatives.get(idx)
        if alternative is None:
            readable.loc[pos, 'Alternative comparison'] = (
                'No qualifying alternative' if (fixture_key(pick), pd.Timestamp(pick.evaluated_at_utc)) in available else 'Candidate ledger unavailable')
            continue
        values = [alternative['market'], alternative['bookmaker'], decimal(alternative['offered_decimal_odds']),
                  pct(alternative['p_any_loss']), pct(alternative['loss_probability_upper']),
                  pct(alternative['p_refund']), signed_pct(alternative['conservative_estimated_ev']),
                  signed_pct(alternative['raw_dc_ev']),
                  signed_pct(alternative['loss_probability_upper'] - pick['loss_probability_upper']).replace('%', ' pp'),
                  alternative['alternative_scope'] + '; ' +
                  ('within selected risk band' if alternative['within_selected_risk_band'] else
                   'outside selected risk band; higher-risk comparison only')]
        for field, value in zip(fields, values):
            readable.loc[pos, field] = value
    return readable


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
    balanced = summary.get('selection_objective') == 'BALANCED_PROBABILITY_EV'
    win_first = summary.get('selection_objective') == 'MAXIMIZE_PROFITABLE_WIN_PROBABILITY'
    probability_first = balanced or win_first or summary.get('selection_objective') == 'PROBABILITY_FIRST'
    if "decision" in raw.columns:
        # Fail closed if a mistakenly supplied mixed decision file slips in.
        raw = raw.loc[
            raw["decision"].isin(["SHORTLISTED", "SHORTLISTED_PROVISIONAL"])
        ].copy()

    readable = readable_shortlist_frame(raw)
    if summary.get('min_adjusted_no_loss_probability') is not None:
        readable['Minimum adjusted no-loss chance'] = pct(summary['min_adjusted_no_loss_probability'])
    from asian_handicap import ALTERNATIVE_POLICIES
    show_alternatives = summary.get('selection_policy_version') in ALTERNATIVE_POLICIES
    if show_alternatives:
        readable = add_shortlist_alternatives(readable, raw, input_dir, summary)
    if probability_first:
        readable = readable.rename(columns={'Near-miss reasons': 'Selection warnings'})
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
    current_window = "shortlist_lookahead_hours" in summary
    window = summary.get("selected_matches_within_72_hours", summary.get("selected_matches_within_60_hours")) if current_window else summary.get("selected_matches_within_four_days")
    window_label = (f"Kickoffs within next {summary['shortlist_lookahead_hours']:g} hours of run" if current_window
                    else "Kickoffs within 4 days (96 hours)")
    window_text = (
        "Yes" if window is True else
        "No" if window is False else "Not available"
    )
    generated = summary.get("generated_at_utc") or "not recorded"

    refresh_note = summary.get("refresh_source", "")
    if summary.get("ucl_validation_available") is False:
        refresh_note += "; UCL historical validation missing: rerun the full six-league pipeline"

    ranking_notes = []
    if probability_first:
        ranking_notes = [
            "**Ranking:** highest reliability-adjusted probability across all usable markets; strict qualifications do not take priority.",
            "**Selection warnings:** EV and historical qualification failures are disclosed, not used to fill a smaller strict-only list.",
        ]
        if summary.get('shortfall_reason'):
            ranking_notes.append(f"**Shortfall:** {summary['shortfall_reason']}")
    if balanced:
        ranking_notes[0] = "**Ranking:** 50% adjusted-probability percentile + 50% adjusted-EV percentile across usable fixture-market candidates; no probability or EV cutoff."
        ranking_notes.append("Percentiles and the combined score are relative ranks, not win probabilities. The equal weights are a transparent policy choice, not a proven optimum.")
    if win_first:
        ranking_notes = [
            '**Ranking:** highest reliability-adjusted probability of a profitable outcome; one market per match, then the top twelve distinct matches within 48 hours. Adjusted EV breaks probability ties.',
            '**Win definition:** full and half wins count; full refunds and losses do not. Half wins pay less than full wins; EV retains the actual settlement amounts.',
            '**Value:** no fixed probability or EV cutoff. Negative adjusted EV is explicitly flagged; high winning probability does not imply a profitable price.',
            '**Availability:** only quoted Pinnacle and bet365 selections. Fewer than twelve are returned when usable quotes or validated evidence are insufficient.',
        ]

    lines = [
        f"# Top {target} probability-and-EV-ranked matches" if balanced else f"# Top {target} probability-ranked matches" if probability_first else "# Conservative shortlisted matches and markets",
        "",
        refresh_note,
        f"**Candidates:** {count} of target {target} distinct matches.",
        f"**Strictly qualified:** {n_strict}. **Provisional watchlist:** {n_provisional}.",
        f"**Pipeline status:** {status}.",
        f"**Generated (UTC):** {generated}.",
        *ranking_notes,
        (
            f"**{window_label}:** "
            + window_text
            + (f" (span: {span:.1f} hours)." if span is not None else ".")
        ),
        "",
        "> WARNING: PROVISIONAL watchlist entries FAILED one or more strict "
        "historical/EV rules; they are for research only, NOT qualified bets. "
        "Even STRICT candidates are not guaranteed outcomes or proven "
        "profitable selections. The shortlist is not an accumulator recommendation.",
        "",
        "## Shortlisted market for each match",
        "",
    ]
    from asian_handicap import POLICIES as AH_POLICIES
    asian = summary.get('selection_policy_version') in AH_POLICIES
    if asian and not win_first:
        if summary.get('min_adjusted_no_loss_probability') is not None:
            lines += ['**Common safety cutoff:** adjusted probability of avoiding any loss >= '+pct(summary['min_adjusted_no_loss_probability'])+' for every market. Zero risk tolerance: the lowest conservative estimated loss risk wins; EV breaks equal-risk ties. Refunds count as avoiding loss; half-losses do not. This cutoff is a policy setting, not a guarantee.', '']
        if summary.get('loss_risk_tolerance') is not None:
            lines += ['**Shortlist policy:** require adjusted estimated EV >= '+pct(summary.get('min_estimated_ev'))+' and unblended EV >= 0. For each match, admit candidates within '+pct(summary.get('loss_risk_tolerance'))+' of its lowest eligible estimated loss risk; rank highest adjusted EV, unblended EV, then full-refund probability. The risk tolerance is a provisional policy setting, not empirically tuned.',
                      '**Probability meaning:** Asian model chance includes refunds. Half-losses lose money. Estimates do not guarantee outcomes. Pinnacle/bet365 take priority, with 1xBet as an exact-line fallback.', '']
        else:
            lines += ['**Asian handicap policy:** archived loss-first rules rank loss risk, refund probability, then EV. v17 requires positive adjusted EV; v18 permits negative EV.',
                      '**Probability meaning:** Asian model chance includes refunds. Estimates do not guarantee outcomes.', '']
    if count:
        headers = [
            "Match", "Shortlisted market", "Qualification", "Kickoff (UTC)",
            "Model chance", "Reliability-adjusted chance",
            "Bookmaker", "Quoted decimal odds", "Conservative estimated EV",
            "Selection warnings" if probability_first else "Near-miss reasons",
        ]
        if asian:
            headers = [*headers, 'Unblended estimated EV', 'Any loss chance', 'Conservative loss estimate', 'Full refund chance', 'Probability meaning']
        if win_first:
            headers += ['Full win chance', 'Half win chance', 'Value warning', 'Quote checked (UTC)']
        if balanced:
            headers = ['Combined ranking score', *headers]
        lines.append(markdown_table(
            headers,
            [[r[c] for c in headers] for _, r in readable.iterrows()],
        ))
    else:
        lines.append("_No qualifying matches were shortlisted. No bet is a valid outcome._")

    if show_alternatives:
        lines += ['', '## Qualifying alternatives for comparison', '',
                  'Prefer another market type when one qualifies; otherwise show another qualifying line. '
                  'Alternatives meet the eligibility checks, including adjusted EV >= 1% and unblended EV >= 0. '
                  'Their risk band is ranked separately; an alternative outside the selected risk band is explicitly marked. '
                  'Risk increase is measured in percentage points against the selected pick. '
                  'These are comparisons, not additional selections. Double Chance 1X/X2 and Asian +0.5 cover the same outcomes; '
                  'different market names do not guarantee diversification.', '']
        headers = ['Match', 'Shortlisted market', 'Alternative market', 'Alternative bookmaker',
                   'Alternative odds', 'Alternative conservative loss estimate', 'Alternative refund chance',
                   'Alternative adjusted EV', 'Alternative unblended EV', 'Alternative risk increase', 'Alternative comparison']
        lines.append(markdown_table(headers, [[r[c] for c in headers] for _, r in readable.iterrows()]))

    lines.extend([
        "",
        "## Interpretation",
        "",
        "**STRICT** means every configured historical, probability, odds "
        "and EV rule passed. " + ("**PROVISIONAL** means a probability-ranked selection failed at least one legacy strict rule. Negative EV, lower probability and weak historical evidence remain explicit warnings; essential identity, quote and timing checks still apply. " if probability_first else "**PROVISIONAL** means the specified historical "
        "or small adjusted-EV checks FAILED, although the essential source, "
        "reference-market integrity, team and price rules passed. "
        "Never count provisional candidates as verified reliable bets. ") +
        "Model chance describes the selected market, not necessarily the "
        "home or away match winner.",
        "",
        "Reliability-adjusted chance discounts historical overconfidence "
        "using an earlier chronological development sample; " + ("audit failures are shown as selection warnings. It remains an estimate." if probability_first else "a later audit must pass the predefined quality gate. It remains an estimate."),
        "",
        ("Historical >=75% and >=85% audit status, sample sizes and Wilson uncertainty ranges are shown for context; these checks no longer shorten the probability-ranked shortlist." if probability_first else "When forecast probability is 75% or higher, the chosen market "
        "must separately pass the >=75% historical audit; >=85% forecasts "
        "must pass the >=85% audit. The readable CSV includes the group "
        "sample size, observed rate and Wilson 95% uncertainty range."),
        "",
        ("Conservative estimated EV adjusts the blended model's settlement payoff using the market calibration penalty. "
         "The loss-risk comparison separately uses the worse blended/unblended loss estimate plus that penalty. "
         "Neither measure is assured; bookmaker prices may change before kickoff."
         if summary.get('min_adjusted_no_loss_probability') is not None else
         "Conservative estimated EV uses that adjusted chance and the quoted price. Neither the original EV nor the adjusted EV is assured; bookmaker prices may change before kickoff."),
        "",
        (
            "**Selection method:** "
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
    try:
        df = pd.read_csv(predictions_path, low_memory=False)
    except pd.errors.EmptyDataError:
        # No upcoming fixtures can produce a CSV without even a header.
        df = pd.DataFrame()

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
    try:
        df = pd.read_csv(path, low_memory=False)
    except pd.errors.EmptyDataError:
        return []
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

    from prediction_runs import resolve_raw
    input_dir = resolve_raw(input_dir)
    output_dir: Path = args.output_dir or readable_dir

    if not input_dir.exists():
        raise SystemExit(
            f"Input folder not found: {input_dir}\n"
            "Run the football pipeline first, use --organize-raw, or pass --input-dir."
        )

    output_dir.mkdir(parents=True, exist_ok=True)
    write_readme(output_dir)

    prediction_files = discover_prediction_files(input_dir)
    if not prediction_files:
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
    from performance_excel import export_existing, REPORT_NAME
    performance_path = export_existing(root_dir, output_dir / REPORT_NAME)

    print(f"Raw input folder:       {input_dir.resolve()}")
    print(f"Readable output folder: {output_dir.resolve()}")
    if shortlist_count is not None:
        print(
            f"  Conservative shortlist: {shortlist_count} "
            "match(es), with selected markets (readable CSV and Markdown report)"
        )
    if performance_path is not None:
        print(f"  Excel performance report: {performance_path}")
    for league, count in processed:
        print(f"  {league}: {count} fixture(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())



