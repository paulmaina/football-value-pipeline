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

- `performance_report.md` — one concise verified-performance verdict and model-improvement plan.
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
    p.add_argument("--performance-only", action="store_true", help="Create only one consolidated readable performance report.")
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
    """Format immutable forward-tracker outputs; do not modify/settle source files.

    If metrics.json exists it is authoritative for overall and grouped figures.
    Supplemental weekly/accuracy tables come from the frozen grade CSV files.
    """
    metrics_path = performance_dir / "metrics.json"
    shortlisted_path = performance_dir / "shortlist_grades.csv"
    forecast_path = performance_dir / "prediction_grades.csv"
    if not any(path.is_file() for path in (metrics_path, shortlisted_path, forecast_path)):
        return False
    metrics = load_json_file(metrics_path)
    shortlist = perf_read_csv(shortlisted_path)
    forecasts = perf_read_csv(forecast_path)
    readable_dir.mkdir(parents=True, exist_ok=True)

    perf_grade_frame(shortlist, is_shortlist=True).to_csv(
        readable_dir / "shortlist_grades_readable.csv", index=False, encoding="utf-8-sig")
    perf_grade_frame(forecasts, is_shortlist=False).to_csv(
        readable_dir / "prediction_grades_readable.csv", index=False, encoding="utf-8-sig")

    overall = metrics.get("shortlist") if isinstance(metrics.get("shortlist"), dict) else perf_stats_from_grades(shortlist)
    summary = {label: perf_format(overall.get(field), "signed_rate" if field == "flat_stake_roi" else kind)
               for field, label, kind in PERFORMANCE_STATS_COLUMNS}
    summary.update({
        "Tracking state": metrics.get("status", "UNKNOWN"),
        "Full fixture forecasts graded": perf_format(metrics.get("prediction_fixtures_graded"), "count"),
        "Full fixture 1X2 multiclass Brier": perf_format(metrics.get("prediction_1x2_multiclass_brier"), "score"),
    })
    pd.DataFrame([summary]).to_csv(readable_dir / "performance_summary_readable.csv",
                                   index=False, encoding="utf-8-sig")

    frames = perf_group_frames(metrics)
    fields = {"tier": "performance_by_tier_readable.csv", "market": "performance_by_market_readable.csv",
              "league": "performance_by_league_readable.csv", "week": "performance_by_gameweek_readable.csv"}
    for key, name in fields.items():
        if key not in frames:
            src_key = {"tier": "selection_tier", "market": "market", "league": "league", "week": "week"}[key]
            stats = perf_group_stats(shortlist, src_key)
            frames[key] = pd.DataFrame([
                { {"tier": "Qualification tier", "market": "Market", "league": "League", "week": "ISO gameweek"}[key]: label,
                  **{heading: perf_format(s.get(field), "signed_rate" if field == "flat_stake_roi" else kind)
                     for field, heading, kind in PERFORMANCE_STATS_COLUMNS}}
                for label, s in sorted(stats.items())
            ])
        frames[key].to_csv(readable_dir / name, index=False, encoding="utf-8-sig")

    calibration = metrics.get("calibration") or []
    calibration_rows = []
    for bucket in calibration if isinstance(calibration, list) else []:
        if not isinstance(bucket, dict):
            continue
        calibration_rows.append({
            "Forecast probability band": bucket.get("probability_band", "—"),
            "Graded selections": perf_format(bucket.get("n"), "count"),
            "Average forecast": perf_format(bucket.get("mean_forecast"), "rate"),
            "Observed win rate": perf_format(bucket.get("observed_win_rate"), "rate"),
            "Binary Brier": perf_format(bucket.get("binary_brier"), "score"),
        })
    cal_cols = ["Forecast probability band", "Graded selections", "Average forecast", "Observed win rate", "Binary Brier"]
    calibration_frame = pd.DataFrame(calibration_rows, columns=cal_cols)
    calibration_frame.to_csv(readable_dir / "performance_calibration_readable.csv",
                             index=False, encoding="utf-8-sig")

    trend = perf_weekly_trend(shortlist)
    trend.to_csv(readable_dir / "performance_cumulative_trend_readable.csv",
                 index=False, encoding="utf-8-sig")
    accuracy = perf_prediction_accuracy(forecasts)
    accuracy.to_csv(readable_dir / "performance_prediction_accuracy_readable.csv",
                    index=False, encoding="utf-8-sig")

    pending = metrics.get("pending_reason_counts") or {}
    if not pending and not shortlist.empty and "status" in shortlist:
        pending = shortlist.loc[~shortlist["status"].isin(["WON", "LOST"]), "status"].value_counts().to_dict()
    pending_frame = pd.DataFrame([{"Reason": perf_format(k, "status"), "Selections": n}
                                  for k, n in sorted(pending.items())],
                                 columns=["Reason", "Selections"])
    pending_frame.to_csv(readable_dir / "performance_pending_reasons_readable.csv", index=False, encoding="utf-8-sig")
    issues = metrics.get("provider_errors") or {}
    issue_frame = pd.DataFrame([{"Provider/league": k, "Issue": str(v)} for k, v in sorted(issues.items())],
                               columns=["Provider/league", "Issue"])
    issue_frame.to_csv(readable_dir / "performance_provider_issues_readable.csv", index=False, encoding="utf-8-sig")

    lines = [
        "# Forward prediction performance — readable dashboard", "",
        "This dashboard formats the **immutable pre-kickoff** evaluation outputs.",
        "It does not refresh results, settle bets, or change the model.", "",
        f"**Evaluation status:** `{metrics.get('status', 'UNKNOWN')}`", "",
        "## At a glance", "",
        perf_md_table(["Measure", "Result"], ([heading, summary[heading]] for _, heading, _ in PERFORMANCE_STATS_COLUMNS)),
        "", f"**Full-fixture predictions graded:** {summary['Full fixture forecasts graded']}",
        f"**1X2 multiclass Brier (lower is better):** {summary['Full fixture 1X2 multiclass Brier']}",
        "", "_Win rate counts only WON/LOST shortlist selections. Pending or unverifiable scores are not losses. "
        "ROI is a one-unit-per-selection simulation for settled bets with genuine recorded odds, not actual betting returns._", "",
    ]
    for key, title in (("tier", "STRICT versus PROVISIONAL"), ("market", "Performance by market"),
                       ("league", "Performance by league"), ("week", "Performance by ISO gameweek")):
        frame = frames[key]
        cols = list(frame.columns)
        shown = [cols[0]] + [c for c in ("Verified selections graded", "Wins", "Losses", "Pending / unverified",
                                       "Win rate (graded only)", "Simulated flat-stake ROI (priced only)") if c in cols] if cols else []
        lines += [f"## {title}", "", perf_md_table(shown, frame[shown].itertuples(index=False, name=None)) if shown else "_No observations yet._", ""]

    lines += ["## All-fixture direction accuracy", "",
              "This checks whether each predicted event crossed a **50% cutoff**; it is **not** the selected-bet hit rate.", "",
              perf_md_table(accuracy.columns.tolist(), accuracy.itertuples(index=False, name=None)), "",
              "## Confidence calibration (selected bets)", "",
              perf_md_table(calibration_frame.columns.tolist(), calibration_frame.itertuples(index=False, name=None)), "",
              "_Compare mean forecast with observed win rate. Empty bins or small samples do not establish calibration._", "",
              "## Cumulative simulated results by gameweek", "",
              perf_md_table(["Week", "Graded", "Wins", "Losses", "Week profit (units)", "Cumulative ROI"],
                            (tuple(r[c] for c in ("ISO gameweek", "Graded", "Wins", "Losses", "Week profit (units)", "Cumulative ROI"))
                             for _, r in trend.iterrows())), "",
              "## Pending/unverified and data-quality issues", "",
              perf_md_table(pending_frame.columns.tolist(), pending_frame.itertuples(index=False, name=None)), "",
              "### Result-provider errors", "",
              perf_md_table(issue_frame.columns.tolist(), issue_frame.itertuples(index=False, name=None)), "",
              "## Weekly match-by-match grades", ""]

    week_folder = readable_dir / "performance_weekly"
    week_folder.mkdir(exist_ok=True)
    if not shortlist.empty and "week" in shortlist and "status" in shortlist:
        for week, group in sorted(shortlist.groupby("week", dropna=True), key=lambda item: str(item[0])):
            stat = perf_stats_from_grades(group)
            safe_week = re.sub(r"[^0-9A-Za-z-]+", "_", str(week))
            report_path = week_folder / f"{safe_week}_report.md"
            detail = perf_grade_frame(group, is_shortlist=True)
            keep = [c for c in ("Kickoff (UTC)", "Home team", "Away team", "Selected market", "Selection tier",
                                "Forecast probability", "Recorded bookmaker odds", "Verified 90-minute score",
                                "Verification / grade", "Simulated profit (1 unit stake)") if c in detail]
            content = [f"# {week} — verified gameweek performance", "",
                       f"Tracked {stat['total']}; graded {stat['graded']}; wins {stat['wins']}; losses {stat['losses']}; pending {stat['pending']}.",
                       f"Graded hit rate: **{perf_format(stat['win_rate'], 'rate')}**. "
                       f"Priced-bet simulated ROI: **{perf_format(stat['flat_stake_roi'], 'signed_rate')}**.", "",
                       perf_md_table(keep, detail[keep].itertuples(index=False, name=None)), "",
                       "_Results use verified regulation-time scores. Pending games are not graded._", ""]
            report_path.write_text("\n".join(content), encoding="utf-8")
            lines.append(f"- [{week} details](performance_weekly/{safe_week}_report.md)")
    else:
        lines.append("_No tracked gameweeks yet._")
    lines += ["", "## Audit and interpretation", "",
              "- Source of truth: `../performance/metrics.json`, `shortlist_grades.csv` and `prediction_grades.csv`.",
              "- Snapshot commit and source fixture identifiers remain available in the detailed readable CSV files.",
              "- `STRICT` and `PROVISIONAL` are reported separately; provisional selections are not audited recommendations.",
              "- Win rate is not calibration; short-run results and simulated ROI can be noisy.",
              "- The original 90-minute verification rules and eligibility checks remain in `performance_tracking.py`.", ""]
    (readable_dir / "performance_dashboard.md").write_text("\n".join(lines), encoding="utf-8")
    index_file = readable_dir / "README.md"
    if index_file.is_file():
        index = index_file.read_text(encoding="utf-8")
        index += ("\n## Forward performance reports\n\n"
                  "Start with [`performance_dashboard.md`](performance_dashboard.md). "
                  "`shortlist_grades_readable.csv` and `prediction_grades_readable.csv` contain individual graded events; "
                  "`performance_summary_readable.csv`, `performance_by_*_readable.csv`, "
                  "`performance_calibration_readable.csv`, `performance_prediction_accuracy_readable.csv`, "
                  "`performance_cumulative_trend_readable.csv`, `performance_pending_reasons_readable.csv`, "
                  "and `performance_provider_issues_readable.csv` provide cumulative monitoring. "
                  "Open `performance_weekly/` for week-by-week match detail.\n\n"
                  "These reports are presentation-only; `performance/` remains authoritative.\n")
        index_file.write_text(index, encoding="utf-8")
    return True



def render_compact_performance(performance_dir: Path, readable_dir: Path) -> bool:
    """One actionable performance report. Never grade or modify source data."""
    metrics_file = performance_dir / "metrics.json"
    shortlist_file = performance_dir / "shortlist_grades.csv"
    predictions_file = performance_dir / "prediction_grades.csv"
    if not any(p.exists() for p in (metrics_file, shortlist_file, predictions_file)):
        return False

    metrics = load_json_file(metrics_file)
    def read_rows(path: Path) -> pd.DataFrame:
        if not path.exists():
            return pd.DataFrame()
        try:
            return pd.read_csv(path, low_memory=False)
        except pd.errors.EmptyDataError:
            return pd.DataFrame()

    selections = read_rows(shortlist_file)
    predictions = read_rows(predictions_file)
    def num(v: Any) -> Optional[float]:
        try:
            x = float(v)
            return x if math.isfinite(x) else None
        except (TypeError, ValueError):
            return None

    def percent(v: Any, signed: bool = False) -> str:
        x = num(v)
        return ("{:+.1%}" if signed else "{:.1%}").format(x) if x is not None else "—"

    def mdtable(cols: Sequence[str], rows: Sequence[Sequence[Any]]) -> str:
        if not rows:
            return "_Not enough verified results yet._"
        def safe(v: Any) -> str:
            return str(v).replace("|", "/").replace("\n", " ")
        return "\n".join(
            ["| " + " | ".join(map(safe, cols)) + " |",
             "| " + " | ".join("---" for _ in cols) + " |"] +
            ["| " + " | ".join(map(safe, row)) + " |" for row in rows]
        )

    def summary(frame: pd.DataFrame) -> Dict[str, Any]:
        n = len(frame)
        if frame.empty or "status" not in frame:
            return dict(total=n, graded=0, pending=n, wins=0, losses=0,
                        win_rate=None, flat_stake_roi=None, settled_with_odds=0,
                        profit_per_unit_staked=None)
        status = frame["status"].astype(str)
        graded = status.isin(("WON", "LOST"))
        wins = int(status.eq("WON").sum())
        profit = pd.to_numeric(frame["unit_profit"], errors="coerce").loc[graded].dropna() if "unit_profit" in frame else pd.Series(dtype=float)
        return dict(total=n, graded=int(graded.sum()), pending=n-int(graded.sum()),
                    wins=wins, losses=int(graded.sum())-wins,
                    win_rate=wins/int(graded.sum()) if graded.sum() else None,
                    flat_stake_roi=float(profit.mean()) if not profit.empty else None,
                    settled_with_odds=len(profit),
                    profit_per_unit_staked=float(profit.sum()) if not profit.empty else None)

    overall = summary(selections)
    if isinstance(metrics.get("shortlist"), dict):
        overall = {**overall, **metrics["shortlist"]}
    graded = int(overall.get("graded") or 0)
    pending = int(overall.get("pending") or 0)
    priced = int(overall.get("settled_with_odds") or 0)
    wins = int(overall.get("wins") or 0)
    losses = int(overall.get("losses") or 0)
    brier = num(metrics.get("prediction_1x2_multiclass_brier"))
    if graded == 0:
        verdict = "**Not enough evidence yet.** No selected markets have verified settled results."
        evidence = "Do not change the model based on unplayed or unverified matches."
    elif graded < 30:
        verdict = "**Early evidence only.** A few results are verified, but market-level conclusions would be unreliable."
        evidence = "Collect at least 30 results before exploring patterns and ideally 100+ for more stable overall evaluation."
    elif graded < 100:
        verdict = "**Patterns can be investigated, not trusted yet.** Validate any suspected weakness out of sample."
        evidence = "Small subgroups are still noisy. Do not optimize parameters against these exact scored games."
    else:
        verdict = "**Substantial tracked history.** Focus on calibration, market-specific differences and uncertainty."
        evidence = "Compare a candidate model with the original on the same new fixtures before accepting changes."

    market_rows = []
    gaps = []
    if not selections.empty and {"market", "status"}.issubset(selections.columns):
        for market, group in sorted(selections.groupby("market"), key=lambda v: str(v[0])):
            s = summary(group)
            rated = group[group["status"].isin(("WON", "LOST"))]
            valid = rated.copy()
            if "predicted_probability" in valid:
                valid["predicted_probability"] = pd.to_numeric(valid["predicted_probability"], errors="coerce")
                valid = valid[valid["predicted_probability"].between(0, 1)]
            else:
                valid = valid.iloc[:0]
            mean_p = float(valid["predicted_probability"].mean()) if not valid.empty else None
            actual = float(valid["status"].eq("WON").mean()) if not valid.empty else None
            gap = actual-mean_p if mean_p is not None else None
            market_rows.append([
                market, int(s["graded"]), int(s["pending"]),
                percent(s["win_rate"]), percent(mean_p),
                percent(gap, signed=True), percent(s["flat_stake_roi"], signed=True),
            ])
            if len(valid) >= 30 and gap is not None:
                gaps.append((gap, str(market), len(valid)))

    graded_predictions = predictions[predictions["status"].eq("GRADED")] if "status" in predictions else pd.DataFrame()
    accuracy = []
    for name, key in (("1X2", "one_x_two_correct"),
                      ("Over 1.5", "over_1_5_correct"),
                      ("Under 3.5", "under_3_5_correct"),
                      ("BTTS Yes", "btts_yes_correct")):
        if key in graded_predictions:
            vals = pd.to_numeric(graded_predictions[key], errors="coerce").dropna()
            vals = vals[vals.isin((0, 1))]
            if not vals.empty:
                accuracy.append(f"{name}: {percent(float(vals.mean()))} (n={len(vals)})")

    calibration = metrics.get("calibration") or []
    signals = []
    if isinstance(calibration, list):
        for row in calibration:
            if not isinstance(row, dict):
                continue
            n, p, actual = num(row.get("n")), num(row.get("mean_forecast")), num(row.get("observed_win_rate"))
            if n is not None and n >= 20 and p is not None and actual is not None:
                signals.append((abs(actual-p), str(row.get("probability_band", "bin")), int(n), p, actual))
    signals.sort(reverse=True)
    data_issues = metrics.get("provider_errors") or {}
    if not isinstance(data_issues, dict):
        data_issues = {}

    next_actions = []
    if data_issues:
        next_actions.append("**Repair result verification:** official-score provider errors prevent some predictions from being scored.")
    if graded < 30:
        next_actions.append("**Collect outcomes before tuning:** archive forecasts before kickoff and verify final 90-minute scores. Pending fixtures are not losses.")
    if signals and signals[0][0] >= .10:
        _, band, n, p, actual = signals[0]
        next_actions.append(
            f"**Investigate calibration:** {band} probability estimates averaged {percent(p)} but won {percent(actual)} (n={n}). Test calibration on separate historic data."
        )
    if gaps and min(gaps)[0] < -.08:
        gap, market, n = min(gaps)
        next_actions.append(
            f"**Investigate {market}:** its observed success is {abs(gap):.1%} below predicted probability (n={n}); review model inputs and prices before adjusting thresholds."
        )
    if graded >= 30 and not gaps:
        next_actions.append("**Expand market-level samples:** avoid claiming an edge where each market has too few verified selections.")
    if len(next_actions) < 3:
        next_actions.append("**Benchmark the full-fixture model:** compare 1X2 Brier on the same matches with a market-implied or simple baseline; a standalone Brier score is not a verdict.")
    if len(next_actions) < 3:
        next_actions.append("**Validate proposed changes prospectively:** compare model versions on the same new fixtures; keep STRICT and PROVISIONAL selections separate.")
    next_actions = next_actions[:3]

    tier_note = []
    if not selections.empty and "selection_tier" in selections:
        for tier in ("STRICT", "PROVISIONAL"):
            group = selections[selections["selection_tier"].eq(tier)]
            if not group.empty:
                s = summary(group)
                tier_note.append(f"{tier}: {s['graded']} settled, {percent(s['win_rate'])} hit rate, {percent(s['flat_stake_roi'], signed=True)} simulated ROI")
    weeks = []
    if not selections.empty and {"week", "status"}.issubset(selections.columns):
        for wk, group in selections.groupby("week"):
            s = summary(group)
            if s["graded"]:
                weeks.append((str(wk), s))
    weeks = sorted(weeks, key=lambda z:z[0])[-3:]

    roi = percent(overall.get("flat_stake_roi"), signed=True)
    total_profit = num(overall.get("profit_per_unit_staked"))
    unit_text = f"{total_profit:+.2f} units" if total_profit is not None else "—"
    lines = [
        "# Football model — performance review", "",
        "**VERDICT:** " + verdict, "", evidence, "",
        "## Core scorecard", "",
        mdtable(["Tracked", "Settled", "Pending", "Wins–losses", "Hit rate", "Simulated ROI", "Profit"],
                [[int(overall.get("total") or 0), graded, pending, f"{wins}–{losses}",
                  percent(overall.get("win_rate")), roi, unit_text]]), "",
        f"**ROI sample:** {priced} verified, priced 1-unit selections. "
        "This is hypothetical single-bet return, not real P&L or an accumulator outcome.", "",
        "## Where the model performs (and where it doesn't)", "",
        mdtable(["Selected market", "Settled", "Pending", "Win rate", "Avg. predicted", "Actual − predicted", "Simulated ROI"], market_rows), "",
        "Negative **Actual − predicted** suggests overconfidence, but do not interpret small samples as proof.", "",
        "**Selection tiers:** " + ("; ".join(tier_note) if tier_note else "No selection tiers scored yet."), "",
        "## Probability quality", "",
        f"**Whole-fixture 1X2 multiclass Brier:** {brier:.4f}" if brier is not None else
        "**Whole-fixture 1X2 multiclass Brier:** not available yet.",
        "Lower Brier is better; benchmark against the same fixtures before judging model skill.", "",
        "**Event direction at 50% cutoff:** " + ("; ".join(accuracy) if accuracy else "not yet verified") + ".",
        "These are event-classification tests, not betting selection hit rates.", "",
        "**Calibration:** " + (
            f"Largest qualified forecast-vs-outcome gap: {signals[0][1]} (n={signals[0][2]}), "
            f"{percent(signals[0][3])} predicted versus {percent(signals[0][4])} observed."
            if signals else "not enough observations in any probability bin (need 20+ verified picks per bin)."
        ), "",
    ]
    if weeks:
        lines += ["**Recent gameweeks:** " +
                  "; ".join(f"{wk}: {s['graded']} settled, {percent(s['win_rate'])} hit rate"
                            for wk, s in weeks) + ".", ""]
    lines += ["## What to improve next", ""]
    lines += [f"{i}. {action}" for i, action in enumerate(next_actions, 1)]
    lines += ["", "## Data integrity", "",
              f"**Tracker status:** {str(metrics.get('status', 'UNKNOWN')).replace('_', ' ')}. "
              f"**Still pending/unverified:** {pending}. "
              f"**Graded full-fixture forecasts:** {len(graded_predictions)}.", ""]
    if data_issues:
        lines += ["**Official-result errors:** " +
                  "; ".join(f"{k}: {v}" for k, v in sorted(data_issues.items())) + ".", ""]
    lines += [
        "Only archived pre-kickoff predictions with verified regulation-time scores count. "
        "Pending, ambiguous, postponed and inaccessible matches are never treated as wins or losses. "
        "PROVISIONAL is exploratory; no model parameter or grade is changed by this formatter.", "",
        "_Raw audit trail remains in ../performance/metrics.json, shortlist_grades.csv and prediction_grades.csv._", "",
    ]
    readable_dir.mkdir(parents=True, exist_ok=True)
    (readable_dir / "performance_report.md").write_text("\n".join(lines), encoding="utf-8")

    # Remove only the old reports generated by the previous verbose formatter.
    obsolete = (
        "performance_dashboard.md", "performance_summary_readable.csv",
        "performance_by_tier_readable.csv", "performance_by_market_readable.csv",
        "performance_by_league_readable.csv", "performance_by_gameweek_readable.csv",
        "performance_calibration_readable.csv", "performance_cumulative_trend_readable.csv",
        "performance_prediction_accuracy_readable.csv", "performance_pending_reasons_readable.csv",
        "performance_provider_issues_readable.csv", "shortlist_grades_readable.csv",
        "prediction_grades_readable.csv",
    )
    for file in obsolete:
        (readable_dir / file).unlink(missing_ok=True)
    weekly = readable_dir / "performance_weekly"
    if weekly.is_dir():
        for file in weekly.glob("*_report.md"):
            file.unlink()
        if not any(weekly.iterdir()):
            weekly.rmdir()
    return True


def main(argv: Optional[Sequence[str]] = None) -> int:
    args = build_parser().parse_args(argv)
    if args.performance_only:
        root_dir = args.root_dir
        output_dir = args.output_dir or root_dir / "readable"
        if not render_compact_performance(root_dir / "performance", output_dir):
            raise SystemExit("No tracker outputs in " + str(root_dir / "performance"))
        print(f"Consolidated report: {(output_dir / 'performance_report.md').resolve()}")
        return 0


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

    if render_compact_performance(root_dir / "performance", output_dir):
        print("  Forward performance: one report (performance_report.md)")

    print(f"Raw input folder:       {input_dir.resolve()}")
    print(f"Readable output folder: {output_dir.resolve()}")
    if shortlist_count is not None:
        print(
            f"  Conservative shortlist: {shortlist_count} "
            "match(es), with selected markets (readable CSV and Markdown report)"
        )
    if performance_written:
        print('  Forward performance: dashboard, grades, calibration and weekly reports')
    for league, count in processed:
        print(f"  {league}: {count} fixture(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
