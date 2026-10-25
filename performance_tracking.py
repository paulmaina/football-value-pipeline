"""Forward-only performance evaluation using archived predictions and verified scores.

Usage:
  python performance_tracking.py capture --commit-sha <git-sha>
  python performance_tracking.py review

Only pre-kickoff GitHub snapshots are graded. Reporting never retrains or
changes a model. Official football-data.org finished scores are evidence;
unknown, ambiguous, postponed and extra-time-only scores fail closed.
"""
from __future__ import annotations

import argparse
import csv
from datetime import datetime, timedelta, timezone
from difflib import SequenceMatcher
import hashlib
import json
import math
import os
from pathlib import Path
import shutil
import sys
import tempfile
from typing import Any
import warnings

import requests

from football_value_pipeline_v2_standalone import LEAGUES, canonical_team_key


ROOT = Path("football_output_v2")
RAW = ROOT / "raw"
PERFORMANCE = ROOT / "performance"
SNAPSHOTS = PERFORMANCE / "snapshots"
API_BASE = "https://api.football-data.org/v4"
MIN_LEAD_MINUTES = 20
MATCH_KICKOFF_TOLERANCE_HOURS = 36
MAX_RESULTS_LOOKBACK_DAYS = 60

LEAGUE_CODES = {
    name: cfg.football_data_org_code
    for cfg in LEAGUES.values()
    for name in (cfg.name, cfg.key)
}
SUPPORTED_MARKETS = {
    "Home win", "Draw", "Away win", "Over 1.5", "Under 3.5",
    "Both Teams to Score - Yes", "Double Chance 1X", "Double Chance X2", "Double Chance 12",
}
from asian_handicap import SETTLED, LINES, label as handicap_label, parse_label as parse_handicap
SUPPORTED_MARKETS.update(handicap_label(s,p) for s in ('home','away') for p in LINES)
import count_markets
# Gradeable count markets: production corner totals only.
SUPPORTED_MARKETS.update(count_markets.market_label('corners', side, line)
                         for line in count_markets.LINES['corners'] for side in ('Over', 'Under'))
RESULT_CACHE = PERFORMANCE / "verified_results.json"


def now_utc() -> datetime:
    return datetime.now(timezone.utc)


def utc(value: Any) -> datetime | None:
    if not isinstance(value, str) or not value.strip():
        return None
    try:
        value = value.strip().replace("Z", "+00:00")
        parsed = datetime.fromisoformat(value)
        return parsed.astimezone(timezone.utc) if parsed.tzinfo else None
    except ValueError:
        return None


def iso(value: datetime) -> str:
    return value.astimezone(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, Any]], columns: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def write_json(path: Path, obj: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")


def load_json(path: Path, default: Any) -> Any:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else default


def number(value: Any, *, min_value: float | None = None,
           max_value: float | None = None) -> float | None:
    try:
        x = float(value)
    except (TypeError, ValueError):
        return None
    if not math.isfinite(x) or (min_value is not None and x < min_value) or (
        max_value is not None and x > max_value
    ):
        return None
    return x


def fixture_key(row: dict) -> str:
    return "|".join((
        str(row.get("league", "")).strip(),
        canonical_team_key(str(row.get("home_team", ""))),
        canonical_team_key(str(row.get("away_team", ""))),
        str(row.get("kickoff_utc", ""))[:10],
    ))


def capture(commit_sha: str, *, root: Path = ROOT,
            captured_at: datetime | None = None, raw_dir: Path | None = None,
            prediction_run_id: str | None = None) -> bool:
    """Archive exact committed forecast inputs, never overwrite the snapshot.

    The capture time is the actual CI time, not user-controlled model metadata.
    Both generated_at and captured_at must predate a fixture's kickoff.
    """
    if not (len(commit_sha) >= 12 and all(c in "0123456789abcdef" for c in commit_sha.lower())):
        raise ValueError("Expected a Git commit SHA (hexadecimal, at least 12 characters)")
    from prediction_runs import resolve_raw, validate_bundle
    raw = Path(raw_dir) if raw_dir is not None else resolve_raw(root / 'raw')
    if prediction_run_id is None and (raw/'run_manifest.json').exists():
        prediction_run_id = validate_bundle(raw)['run_id']
    if prediction_run_id is not None:
        manifest = validate_bundle(raw)
        if manifest['run_id'] != prediction_run_id:
            raise ValueError('Capture prediction-run identity mismatch')
    # A run may be uploaded with many siblings under one real source commit.
    # Archive identity is separate from the actual source Git commit.
    archive_id = (hashlib.sha256(('prediction-run:'+prediction_run_id).encode()).hexdigest()[:40]
                  if prediction_run_id is not None else commit_sha)
    directory = root / "performance" / "snapshots" / archive_id[:16]
    if directory.exists():
        print(f"Snapshot already archived: {directory}")
        return False
    files = {
        "predictions.csv": raw / "all_leagues_predictions.csv",
        "shortlist.csv": raw / "conservative_bet_shortlist.csv",
        "selection_summary.json": raw / "conservative_bet_summary.json",
    }
    if prediction_run_id is not None:
        files['run_manifest.json'] = raw/'run_manifest.json'
    missing = [str(p) for p in files.values() if not p.exists()]
    if missing:
        raise FileNotFoundError("Cannot snapshot incomplete forecast files: " + ", ".join(missing))
    created = captured_at or now_utc()
    if created.tzinfo is None:
        raise ValueError("captured_at must have timezone information")
    summary = load_json(files["selection_summary.json"], {})
    generated = utc(summary.get("generated_at_utc"))
    if generated is None or generated > created + timedelta(minutes=5):
        raise ValueError("Missing or impossible forecast generated_at_utc")
    forecast = read_csv(files["predictions.csv"])
    picks = read_csv(files["shortlist.csv"])
    if not forecast:
        raise ValueError("Refusing to archive an empty forecast")
    # Some forecast rows may already be underway. They are archived
    # for audit, but permanently ineligible for forward grading.
    eligible = sum(
        1 for row in forecast
        if (k := utc(row.get("kickoff_utc")))
        and created <= k - timedelta(minutes=MIN_LEAD_MINUTES)
        and generated <= k - timedelta(minutes=MIN_LEAD_MINUTES)
    )
    if not eligible:
        print("No verifiable pre-kickoff fixtures; snapshot skipped.")
        return False
    # Optional sidecar; stale/broken experiments must not block baseline capture.
    try:
        from shortlist_weight_experiment import capture_file as capture_weights
        experiment = capture_weights(raw, summary.get('generated_at_utc'))
        if experiment is not None:
            files['shortlist_weight_experiment.json'] = experiment
    except Exception as exc:
        warnings.warn(f'Shortlist weight capture skipped ({type(exc).__name__})')
    try:
        from shortlist_policy_experiment import capture_file as capture_policy
        experiment = capture_policy(raw, summary.get('generated_at_utc'))
        if experiment is not None:
            files['shortlist_policy_experiment.json'] = experiment
    except Exception as exc:
        warnings.warn(f'Shortlist policy capture skipped ({type(exc).__name__})')
    try:
        from goal_blend_experiment import capture_file
        experiment = capture_file(raw, summary.get("generated_at_utc"))
        if experiment is not None:
            files["goal_blend_experiment.json"] = experiment
    except Exception as exc:
        warnings.warn(f"Shadow capture skipped: {exc}")
    try:
        from market_led_experiment import capture_file as capture_market_led
        experiment = capture_market_led(raw, summary.get("generated_at_utc"))
        if experiment is not None:
            files["market_led_experiment.json"] = experiment
    except Exception as exc:
        warnings.warn(f"Market-led capture skipped ({type(exc).__name__})")
    try:
        from filter_sensitivity_experiment import capture_file as capture_filter
        experiment = capture_filter(raw, summary.get("generated_at_utc"))
        if experiment is not None:
            files["filter_sensitivity_experiment.json"] = experiment
    except Exception as exc:
        warnings.warn(f"Filter sensitivity capture skipped ({type(exc).__name__})")
    try:
        from benchmark_forward_experiment import capture_file as capture_benchmark
        experiment = capture_benchmark(raw, summary.get("generated_at_utc"))
        if experiment is not None:
            files["benchmark_forward_experiment.json"] = experiment
    except Exception as exc:
        warnings.warn(f"Benchmark forward capture skipped ({type(exc).__name__})")
    try:
        from model_reliability_experiment import capture_file as capture_reliability
        experiment = capture_reliability(raw, summary.get("generated_at_utc"))
        if experiment is not None: files["model_reliability_experiment.json"] = experiment
    except Exception as exc:
        warnings.warn(f'Reliability capture skipped ({type(exc).__name__})')
    try:
        from totals_anchor_experiment import capture_file as capture_totals
        experiment = capture_totals(raw, summary.get("generated_at_utc"))
        if experiment is not None: files["totals_anchor_experiment.json"] = experiment
    except Exception as exc:
        warnings.warn(f"Totals anchoring capture skipped ({type(exc).__name__})")
    directory.parent.mkdir(parents=True, exist_ok=True)
    # Publish the directory only after every artifact and metadata file exists.
    # A failed health capture or interrupted copy must leave the commit retryable.
    with tempfile.TemporaryDirectory(prefix='.capture-', dir=directory.parent) as temporary:
        staging = Path(temporary) / 'snapshot'
        staging.mkdir()
        digests = {}
        for output_name, source in files.items():
            dest = staging / output_name
            shutil.copyfile(source, dest)
            digests[output_name] = hashlib.sha256(dest.read_bytes()).hexdigest()
        from pipeline_health import capture_health
        write_json(staging / "pipeline_health.json", capture_health(root, created, files, raw_dir=raw))
        digests["pipeline_health.json"] = hashlib.sha256((staging / "pipeline_health.json").read_bytes()).hexdigest()
        write_json(staging / "metadata.json", {
            "schema_version": 1,
            "git_commit_sha": commit_sha,
            **({'archive_id': archive_id, 'prediction_run_id': prediction_run_id,
                'data_origin': 'immutable prediction generation received at actual capture time'}
               if prediction_run_id is not None else {}),
            "captured_at_utc": iso(created),
            # Sidecars bind to the exact generation instant, including microseconds.
            # Do not truncate here: capture succeeds against the raw summary but
            # later archive validation compares against this stored timestamp.
            "generated_at_utc": generated.astimezone(timezone.utc).isoformat().replace("+00:00", "Z"),
            "selection_policy_version": summary.get("selection_policy_version") or "legacy/unspecified",
            "n_all_forecasts": len(forecast),
            "n_shortlist": len(picks),
            "n_pre_kickoff_forecasts": eligible,
            "sha256": digests,
            **({"data_origin": "git-tracked prediction output at capture time"}
               if prediction_run_id is None else {}),
        })
        staging.rename(directory)
    print(f"Archived immutable prediction snapshot: {directory}; {eligible} pre-kickoff fixtures")
    return True


def snapshots(root: Path = ROOT) -> list[tuple[dict, list[dict], list[dict]]]:
    base = root / "performance" / "snapshots"
    if not base.exists():
        return []
    output = []
    for meta_path in base.glob("*/metadata.json"):
        directory = meta_path.parent
        if directory.name.startswith('.capture-'):
            continue
        meta = load_json(meta_path, {})
        if 'archive_id' in meta:
            from prediction_runs import archive_identity
            try:
                archive_id = archive_identity(meta, directory.name)
            except ValueError:
                warnings.warn(f'Invalid prediction-run archive identity ignored: {directory}')
                continue
            meta = {**meta, 'source_git_commit_sha': meta['git_commit_sha'],
                    'git_commit_sha': archive_id}
        if utc(meta.get("captured_at_utc")) is None or utc(meta.get("generated_at_utc")) is None:
            warnings.warn(f"Invalid snapshot metadata ignored: {directory}")
            continue
        required = {'predictions.csv', 'shortlist.csv', 'selection_summary.json'}
        if 'archive_id' in meta:
            required.add('run_manifest.json')
        optional = {'goal_blend_experiment.json', 'market_led_experiment.json',
            'filter_sensitivity_experiment.json', 'benchmark_forward_experiment.json',
            'totals_anchor_experiment.json', 'model_reliability_experiment.json',
            'shortlist_policy_experiment.json', 'shortlist_weight_experiment.json', 'pipeline_health.json'}
        digests = meta.get('sha256')
        if not isinstance(digests, dict) or not required.issubset(digests) or set(digests)-required-optional:
            warnings.warn(f'Missing required or invalid snapshot manifest ignored: {directory}')
            continue
        if any(not isinstance(digests[name], str) or len(digests[name]) != 64 or
               any(c not in '0123456789abcdef' for c in digests[name].lower()) for name in required):
            warnings.warn(f'Invalid snapshot digest ignored: {directory}')
            continue
        # Fail closed if an archived artifact changes after capture.
        if any(
            not (directory / name).exists() or hashlib.sha256(
                (directory / name).read_bytes()
            ).hexdigest() != digest
            for name, digest in digests.items()
            if name not in {"goal_blend_experiment.json", "market_led_experiment.json", "filter_sensitivity_experiment.json", "benchmark_forward_experiment.json", "totals_anchor_experiment.json", "model_reliability_experiment.json", "shortlist_policy_experiment.json", "shortlist_weight_experiment.json", "pipeline_health.json"}
        ):
            warnings.warn(f"Tampered/incomplete snapshot ignored: {directory}")
            continue
        summary = load_json(directory / "selection_summary.json", {})
        if 'archive_id' in meta:
            from prediction_runs import validate_archive_binding
            try:
                validate_archive_binding(directory, meta)
            except (ValueError, KeyError, OSError):
                warnings.warn(f'Unbound prediction-run archive ignored: {directory}')
                continue
        # The immutable summary restores legacy subsecond generation precision;
        # a different generation instant cannot relabel an archived forecast.
        from forecast_integrity import snapshot_generated_at
        try:
            generated = snapshot_generated_at(directory, meta)
        except (ValueError, TypeError, KeyError, OSError):
            warnings.warn(f'Unbound snapshot generation ignored: {directory}')
            continue
        meta = {**meta, 'generated_at_utc': generated, "selection_policy_version": (
            meta.get("selection_policy_version") or summary.get("selection_policy_version")
            or "legacy/unspecified"
        )}
        output.append((
            meta,
            read_csv(directory / "predictions.csv"),
            read_csv(directory / "shortlist.csv"),
        ))
    return sorted(output, key=lambda item: (
        utc(item[0]["captured_at_utc"]), utc(item[0]["generated_at_utc"]), item[0]["git_commit_sha"]
    ))


def tracking_key(row: dict) -> tuple[str, str]:
    """One fixture per actual forecast generation, not per upload commit."""
    generated = utc(row.get('snapshot_generated_utc'))
    run = generated.isoformat() if generated is not None else str(row.get('snapshot_commit') or '')
    return run, row.get('fixture_key') or fixture_key(row)


def frozen_rows(archive: list[tuple[dict, list[dict], list[dict]]],
                which: str, *, all_runs: bool = False, latest: bool = False) -> list[dict]:
    """Freeze the first/latest eligible record per fixture, or per generation/fixture.

    Re-uploading one generation never adds another stake. Default unique-fixture
    semantics remain for model/experiment comparisons and near-close evaluation.
    """
    if all_runs and latest:
        raise ValueError('Choose either all runs or latest per fixture')
    frozen = {}
    for meta, predictions, picks in archive:
        source = picks if which == "shortlist" else predictions
        captured = utc(meta["captured_at_utc"])
        generated = utc(meta["generated_at_utc"])
        for item in source:
            kickoff = utc(item.get("kickoff_utc"))
            if (
                kickoff is None or captured is None or generated is None
                or max(captured, generated) > kickoff - timedelta(minutes=MIN_LEAD_MINUTES)
            ):
                continue
            if which == "shortlist" and item.get("decision") not in (
                "SHORTLISTED", "SHORTLISTED_PROVISIONAL"
            ):
                continue
            if item.get("league") not in LEAGUE_CODES:
                continue
            key = fixture_key(item)
            row = {**item, "snapshot_commit": meta["git_commit_sha"],
                "snapshot_captured_utc": meta["captured_at_utc"],
                "snapshot_generated_utc": meta["generated_at_utc"], "fixture_key": key,
                "selection_policy_version": meta.get("selection_policy_version", "legacy/unspecified")}
            identity = tracking_key(row) if all_runs else key
            if not key.strip("|"):
                continue
            if identity in frozen and (not latest or generated <= utc(frozen[identity]['snapshot_generated_utc'])):
                continue
            frozen[identity] = row
    return list(frozen.values())


from match_scores import valid_goals, regulation_goals


def verified_result_source(record):
    """Recognize the finished-result contract of each competition's collector."""
    if record.get('source_status') != 'FINISHED':
        return False
    if record.get('league_code') == 'EL':
        # Current Europa league-phase results are corroborated by both feeds.
        # Keep previously verified three-source cache records readable, too.
        return record.get('source_duration') == 'REGULAR' and record.get('source') in (
            'Cornerflick + Fixture Download',
            'Cornerflick + Fixture Download + UEFA',
        )
    return record.get('source') == 'football-data.org/v4'


def verified_record(league_code: str, match: dict) -> dict | None:
    """Only scorelines verified as FINISHED, with regulation-time results.

    Never settle European knockout match markets with extra-time or
    penalty-shootout totals, which are not ordinary 90-minute markets.
    """
    if match.get("status") != "FINISHED" or not isinstance(match.get("score"), dict):
        return None
    score = match["score"]
    duration = score.get("duration")
    goals = regulation_goals(score)
    home, away = match.get("homeTeam"), match.get("awayTeam")
    kickoff = utc(match.get("utcDate"))
    if goals is None or kickoff is None or not isinstance(home, dict) or not isinstance(away, dict):
        return None
    if not (isinstance(match.get("id"), int) and home.get("name") and away.get("name")):
        return None
    return {
        "match_id": match["id"], "league_code": league_code,
        "kickoff_utc": iso(kickoff), "home_team": home["name"],
        "away_team": away["name"],
        "home_short_name": home.get("shortName") or "",
        "away_short_name": away.get("shortName") or "",
        "home_goals": goals[0], "away_goals": goals[1],
        "source": "football-data.org/v4",
        "source_status": "FINISHED", "source_duration": duration or "REGULAR",
    }


def fetch_verified(token: str, league_code: str, from_date: str, to_date: str,
                   *, session: requests.Session | None = None) -> list[dict]:
    """One modest date-scoped official-results request per competition."""
    url = f"{API_BASE}/competitions/{league_code}/matches"
    get = session.get if session else requests.get
    response = get(url, headers={"X-Auth-Token": token},
                   params={"dateFrom": from_date, "dateTo": to_date},
                   timeout=30)
    if response.status_code == 429:
        raise RuntimeError("football-data.org rate limited results requests (HTTP 429)")
    if response.status_code in (401, 403):
        raise RuntimeError(f"football-data.org denied access to {league_code} (HTTP {response.status_code})")
    response.raise_for_status()
    payload = response.json()
    if not isinstance(payload, dict) or not isinstance(payload.get("matches"), list):
        raise RuntimeError(f"football-data.org returned malformed results for {league_code}")
    return [
        record for match in payload["matches"]
        if isinstance(match, dict) and (record := verified_record(league_code, match))
    ]


def _overlap(a: str, b: str) -> float:
    a = canonical_team_key(a)
    b = canonical_team_key(b)
    return 100.0 if a and a == b else 100 * SequenceMatcher(None, a, b).ratio() if a and b else 0.0


def fixture_match(row: dict, verified: list[dict]) -> tuple[dict | None, str]:
    when = utc(row.get("kickoff_utc"))
    code = LEAGUE_CODES.get(row.get("league"))
    if when is None or not code:
        return None, "INVALID_FIXTURE"
    candidates = []
    for match in verified:
        kick = utc(match.get("kickoff_utc"))
        if match.get("league_code") != code or kick is None or abs(
            (kick - when).total_seconds()
        ) > MATCH_KICKOFF_TOLERANCE_HOURS * 3600:
            continue
        home = max(_overlap(row.get("home_team", ""), name) for name in (
            match["home_team"], match.get("home_short_name") or ""
        ))
        away = max(_overlap(row.get("away_team", ""), name) for name in (
            match["away_team"], match.get("away_short_name") or ""
        ))
        if code == "EL":
            from europa_training import resolver
            resolve = resolver()
            home = 100 if resolve(row.get("home_team", "")) == resolve(match["home_team"]) else 0
            away = 100 if resolve(row.get("away_team", "")) == resolve(match["away_team"]) else 0
        if home >= 90 and away >= 90:
            candidates.append((min(home, away), home + away, match))
    if not candidates:
        return None, "UNVERIFIED_FIXTURE_OR_RESULT"
    candidates.sort(key=lambda x: (x[0], x[1]), reverse=True)
    if len(candidates) > 1 and candidates[0][1] - candidates[1][1] < 8:
        return None, "AMBIGUOUS_FIXTURE"
    return candidates[0][2], "VERIFIED_FINISHED"


def result_for_market(market: str, h: int, a: int) -> bool | None:
    return {
        "Home win": h > a,
        "Draw": h == a,
        "Away win": a > h,
        "Over 1.5": h + a >= 2,
        "Under 3.5": h + a <= 3,
        "Double Chance 1X": h >= a,
        "Double Chance X2": a >= h,
        "Double Chance 12": h != a,
        "Both Teams to Score - Yes": h > 0 and a > 0,
    }.get(market)


def score_shortlist(row: dict, final: dict | None, state: str) -> dict:
    out = {
        "fixture_key": row["fixture_key"],
        "league": row["league"], "home_team": row["home_team"],
        "away_team": row["away_team"], "kickoff_utc": row["kickoff_utc"],
        "snapshot_commit": row["snapshot_commit"],
        "selection_policy_version": row.get("selection_policy_version") or "legacy/unspecified",
        "snapshot_captured_utc": row["snapshot_captured_utc"],
        "snapshot_generated_utc": row.get("snapshot_generated_utc") or "",
        "market": row.get("market"), "selection_tier": row.get("selection_tier") or (
            "STRICT" if row.get("decision") == "SHORTLISTED" else "PROVISIONAL"
        ),
        "predicted_probability": (row.get('rank_probability') if row.get('probability_basis') == 'net_profit' else row.get('p_no_loss') if parse_handicap(row.get('market')) else row.get("rank_probability") or row.get("predicted_probability")),
        "probability_basis": row.get('probability_basis') or None,
        "offered_decimal_odds": row.get("offered_decimal_odds"),
        "per_stake_cost": row.get("per_stake_cost") or 0,
        "bookmaker": row.get("bookmaker"),
        "match_source": final.get("source", "football-data.org/v4") if final else "",
        "source_match_id": final["match_id"] if final else "",
        "final_score": f"{final['home_goals']}-{final['away_goals']}" if final else "",
        "status": state,
        "unit_profit": "",
        "brier": "",
        "week": "",
    }
    kickoff = utc(row.get("kickoff_utc"))
    if kickoff:
        year, week, _ = kickoff.isocalendar()
        out["week"] = f"{year}-W{week:02d}"
    if state != "VERIFIED_FINISHED" or not final:
        return out
    market = str(row.get("market"))
    handicap = parse_handicap(market)
    if handicap:
        from asian_handicap import profit
        price = number(row.get('offered_decimal_odds'), min_value=1.000001)
        if price is None:
            out['status'] = 'UNSUPPORTED_MARKET'
            return out
        from quote_policy import stake_cost
        status, gain = profit(final['home_goals'], final['away_goals'], *handicap, price, stake_cost(out['per_stake_cost']))
        out.update(status=status, unit_profit=round(gain,6))
        p = number(out.get('predicted_probability'),min_value=0,max_value=1)
        if p is not None:
            out['brier'] = round((p-int(gain > 1e-12 if out['probability_basis'] == 'net_profit' else gain >= -1e-12))**2,8)
        return out
    counted = count_markets.parse_label(market)
    if counted:
        # Count totals settle from the committed match statistics once present.
        total = count_markets.verified_total(row, final)
        if total is None:
            out["status"] = "AWAITING_COUNT_RESULT"
            return out
        result = count_markets.outcome(*counted, total)
    else:
        result = result_for_market(market, final["home_goals"], final["away_goals"])
    if result is None:
        out["status"] = "UNSUPPORTED_MARKET"
        return out
    out["status"] = "WON" if result else "LOST"
    price = number(row.get("offered_decimal_odds"), min_value=1.000001)
    if price is not None:
        from quote_policy import stake_cost
        cost = stake_cost(out["per_stake_cost"])
        out["unit_profit"] = round((price - 1.0 if result else -1.0) - cost, 6)
    p = number(out.get("predicted_probability"), min_value=0, max_value=1)
    if p is not None:
        out["brier"] = round((p - float(result)) ** 2, 8)
    return out


def score_prediction(row: dict, final: dict | None, state: str) -> dict:
    out = {
        "fixture_key": row["fixture_key"], "league": row["league"],
        "home_team": row["home_team"], "away_team": row["away_team"],
        "kickoff_utc": row["kickoff_utc"],
        "snapshot_commit": row["snapshot_commit"],
        "selection_policy_version": row.get("selection_policy_version") or "legacy/unspecified",
        "match_source": final.get("source", "football-data.org/v4") if final else "",
        "source_match_id": final["match_id"] if final else "",
        "final_score": f"{final['home_goals']}-{final['away_goals']}" if final else "",
        "status": state, "predicted_1x2": row.get("predicted_1x2"),
        "predicted_home": row.get("p_home"),
        "predicted_draw": row.get("p_draw"),
        "predicted_away": row.get("p_away"),
        "one_x_two_brier": "",
        "one_x_two_correct": "",
        "over_1_5_correct": "", "under_3_5_correct": "",
        "btts_yes_correct": "", "btts_no_correct": "",
        "week": "",
    }
    kickoff = utc(row.get("kickoff_utc"))
    if kickoff:
        year, week, _ = kickoff.isocalendar()
        out["week"] = f"{year}-W{week:02d}"
    if state != "VERIFIED_FINISHED" or not final:
        return out
    h, a = final["home_goals"], final["away_goals"]
    outcome = "home" if h > a else "away" if h < a else "draw"
    p = [number(row.get(f"p_{key}"), min_value=0, max_value=1)
         for key in ("home", "draw", "away")]
    if all(x is not None for x in p) and abs(sum(p) - 1) <= 0.03:
        # Multiclass Brier uses three outcomes; not equivalent to the
        # binary Brier scores used for individual shortlist markets.
        out["one_x_two_brier"] = round(sum(
            (prob - int(key == outcome)) ** 2 for key, prob in zip(
                ("home", "draw", "away"), p
            )
        ), 8)
        out["one_x_two_correct"] = int(
            ("home", "draw", "away")[p.index(max(p))] == outcome
        )
    outcomes = {
        "over_1_5": h + a >= 2,
        "under_3_5": h + a <= 3,
        "btts_yes": h > 0 and a > 0,
        "btts_no": h == 0 or a == 0,
    }
    for key, actual in outcomes.items():
        prob = number(row.get(f"p_{key}"), min_value=0, max_value=1)
        if prob is not None:
            # Boolean correctness of predicting event at 50% cutoff,
            # not the betting selection win rate.
            out[f"{key}_correct"] = int((prob >= 0.5) == actual)
    out["status"] = "GRADED"
    return out


def collect_results(eligible: list[dict], *, root: Path, token: str,
                    clock: datetime, session: requests.Session | None = None) -> tuple[list[dict], dict]:
    """Refresh verified results; never replace valid records with guesses."""
    cache = root / "performance" / "verified_results.json"
    old = load_json(cache, {})
    if not isinstance(old, dict):
        raise ValueError("Invalid result cache")
    errors = {}
    if not token:
        errors["configuration"] = "FOOTBALL_DATA_API_KEY is missing"
    # Only fetch when results might exist. Previously verified results
    # remain useful for cumulative reports and for temporary API failures.
    for league, code in sorted(LEAGUE_CODES.items()):
        if league not in LEAGUES:  # Avoid duplicate league name aliases.
            continue
        dates = [
            utc(x.get("kickoff_utc")) for x in eligible
            if LEAGUE_CODES.get(x.get("league")) == code
        ]
        dates = [
            d for d in dates if d is not None
            and d <= clock - timedelta(hours=2)
            and d >= clock - timedelta(days=MAX_RESULTS_LOOKBACK_DAYS)
        ]
        if not dates:
            continue
        start = min(dates).date() - timedelta(days=2)
        end = min(clock.date() + timedelta(days=1),
                  max(dates).date() + timedelta(days=3))
        try:
            if league == "UEL":
                from europa_training import results
                fetched = results(root.parent/".football_cache", clock)
            elif not token:
                continue
            else:
                fetched = fetch_verified(
                    token, code, start.isoformat(), end.isoformat(), session=session
                )
        except (requests.RequestException, RuntimeError, ValueError) as exc:
            errors[league] = str(exc).split("?")[0][:180]
            continue
        for rec in fetched:
            key = f"{code}:{rec['match_id']}"
            if key not in old:
                old[key] = {**rec, "first_verified_at_utc": iso(clock)}
            elif any(old[key].get(k) != v for k, v in rec.items()):
                old[key] = {
                    **rec,
                    "first_verified_at_utc": old[key].get("first_verified_at_utc", iso(clock)),
                    "revised_at_utc": iso(clock),
                }
    write_json(cache, old)
    return list(old.values()), errors


SHORTLIST_COLUMNS = [
    "fixture_key", "league", "home_team", "away_team", "kickoff_utc",
    "snapshot_commit", "selection_policy_version", "snapshot_captured_utc", "snapshot_generated_utc", "market", "selection_tier",
    "predicted_probability", "probability_basis", "offered_decimal_odds", "per_stake_cost", "bookmaker", "match_source",
    "source_match_id", "final_score", "status", "unit_profit", "brier", "week",
]
PREDICTION_COLUMNS = [
    "fixture_key", "league", "home_team", "away_team", "kickoff_utc",
    "snapshot_commit", "selection_policy_version", "match_source", "source_match_id", "final_score",
    "status", "predicted_1x2", "predicted_home", "predicted_draw",
    "predicted_away", "one_x_two_brier", "one_x_two_correct",
    "over_1_5_correct", "under_3_5_correct", "btts_yes_correct",
    "btts_no_correct", "week",
]


def stats(rows: list[dict]) -> dict:
    rated = [r for r in rows if r["status"] in SETTLED]
    wins = sum(r["status"] in ("WON", "HALF_WON") for r in rated)
    priced = [r for r in rated if number(r.get("unit_profit")) is not None]
    profit = sum(float(r["unit_profit"]) for r in priced)
    brier = [float(r["brier"]) for r in rated if number(r.get("brier")) is not None]
    return {
        **({'refunds':sum(r['status']=='REFUNDED' for r in rated),
            'half_wins':sum(r['status']=='HALF_WON' for r in rated),
            'half_losses':sum(r['status']=='HALF_LOST' for r in rated),
            'no_loss_rate':round(sum(float(r['unit_profit']) >= -1e-12 for r in rated if number(r.get('unit_profit')) is not None)/len(priced),6) if priced else None}
           if any(parse_handicap(r.get('market')) for r in rows) else {}),
        "total": len(rows), "graded": len(rated),
        "wins": wins, "losses": sum(r["status"] in ("LOST", "HALF_LOST") for r in rated),
        "pending": len(rows) - len(rated),
        "win_rate": round(wins / len(rated), 6) if rated else None,
        "brier": round(sum(brier) / len(brier), 6) if brier else None,
        "settled_with_odds": len(priced),
        "profit_per_unit_staked": round(profit, 6) if priced else None,
        "flat_stake_roi": round(profit / len(priced), 6) if priced else None,
    }


def calibration_outcome(row):
    """Use each frozen probability's event; old AH forecasts still mean no loss."""
    if parse_handicap(row.get('market')):
        gain = float(row['unit_profit'])
        return int(gain > 1e-12 if row.get('probability_basis') == 'net_profit' else gain >= -1e-12)
    return int(row['status'] == 'WON')


def calibration_buckets(rows: list[dict]) -> list[dict]:
    """Binary reliability buckets for graded *selected* markets only."""
    edges = (0.0, 0.5, 0.6, 0.7, 0.8, 0.9, 1.000001)
    buckets = []
    for low, high in zip(edges, edges[1:]):
        cohort = [
            r for r in rows
            if r["status"] in SETTLED
            and (p := number(r.get("predicted_probability"), min_value=0, max_value=1)) is not None
            and low <= p < high
        ]
        if not cohort:
            continue
        n = len(cohort)
        mean = sum(float(r["predicted_probability"]) for r in cohort) / n
        actual = sum(calibration_outcome(r) for r in cohort) / n
        buckets.append({
            "probability_band": f"{low:.0%}–{min(high, 1.0):.0%}",
            "n": n, "mean_forecast": round(mean, 6),
            "observed_win_rate": round(actual, 6),
            "binary_brier": round(sum(
                (float(r["predicted_probability"]) - calibration_outcome(r))**2
                for r in cohort
            ) / n, 6),
        })
    return buckets


def calibration_table(buckets: list[dict]) -> str:
    lines = [
        "| Forecast bin | Samples | Average forecast | Observed event rate (frozen probability basis) | Binary Brier |",
        "|---|---:|---:|---:|---:|",
    ]
    for x in buckets:
        lines.append(
            f"| {x['probability_band']} | {x['n']} | "
            f"{x['mean_forecast']:.1%} | {x['observed_win_rate']:.1%} "
            f"| {x['binary_brier']:.4f} |"
        )
    return "\n".join(lines)


def report_table(groups: dict[str, dict]) -> str:
    lines = [
        "| Group | Graded | W-L | Win rate | Simulated ROI |",
        "|---|---:|---:|---:|---:|",
    ]
    for key, data in sorted(groups.items()):
        rate = "—" if data["win_rate"] is None else f"{100 * data['win_rate']:.1f}%"
        roi = "—" if data["flat_stake_roi"] is None else f"{100 * data['flat_stake_roi']:+.1f}%"
        lines.append(f"| {key} | {data['graded']} | {data['wins']}-{data['losses']} | {rate} | {roi} |")
    return "\n".join(lines)


def report(root: Path, selections: list[dict], all_predictions: list[dict],
           failures: dict, reviewed_at: str | None = None, *,
           selection_history: list[dict] | None = None) -> dict:
    output = root / "performance"
    output.mkdir(parents=True, exist_ok=True)
    write_csv(output / "shortlist_grades.csv", selections, SHORTLIST_COLUMNS)
    write_csv(output / "prediction_grades.csv", all_predictions, PREDICTION_COLUMNS)
    selection_history = selections if selection_history is None else selection_history
    write_csv(output / "shortlist_run_history.csv", selection_history, SHORTLIST_COLUMNS)

    groupings = {
        "tier": {tier: stats([r for r in selections if r["selection_tier"] == tier])
                 for tier in ("STRICT", "PROVISIONAL")},
        "market": {market: stats([r for r in selections if r["market"] == market])
                   for market in sorted(SUPPORTED_MARKETS)},
        "league": {key: stats([r for r in selections if r["league"] == key])
                   for key in sorted({r["league"] for r in selections})},
    }
    policies = sorted({r.get("selection_policy_version") or "legacy/unspecified" for r in selections})
    groupings["policy"] = {policy: stats([r for r in selections
        if (r.get("selection_policy_version") or "legacy/unspecified") == policy]) for policy in policies}
    weeks = sorted({r["week"] for r in selections if r["week"]})
    groupings["week"] = {week: stats([r for r in selections if r["week"] == week])
                         for week in weeks}
    # First archived selection per unique fixture remains a transparent reference.
    first = {}
    for row in selection_history:
        first.setdefault(row['fixture_key'], row)
    unique_selections = list(first.values())
    run_rows = {}
    for row in selection_history:
        run_rows.setdefault(tracking_key(row)[0], []).append(row)
    latest_run_rows = {}
    for row in selections:
        latest_run_rows.setdefault(tracking_key(row)[0], []).append(row)
    groupings['run'] = {key: stats(rows) for key, rows in latest_run_rows.items()}
    graded_prediction = [r for r in all_predictions if r["status"] == "GRADED"]
    one_x_two = [float(r["one_x_two_brier"]) for r in graded_prediction
                 if number(r.get("one_x_two_brier")) is not None]
    result = {
        "status": (
            "AWAITING_PREMATCH_SNAPSHOTS" if not selections
            else "AWAITING_VERIFIED_RESULTS" if not any(
                r["status"] in SETTLED for r in selections
            )
            else "PARTIALLY_GRADED" if any(
                r["status"] not in SETTLED for r in selections
            )
            else "ALL_GRADED"
        ),
        "source": "football-data.org v4 FINISHED regulation-time scorelines; Europa: corroborated Cornerflick / Fixture Download league-phase scores",
        "reviewed_at_utc": reviewed_at,
        "shortlist": stats(selections),
        "tracking_basis": "LATEST_PREMATCH_PER_FIXTURE",
        "first_prediction_reference": stats(unique_selections),
        "shortlist_run_history": stats(selection_history),
        "run_history_groups": {key:stats(rows) for key, rows in run_rows.items()},
        "unique_shortlisted_fixtures": len(first),
        "tracked_prediction_runs": len(run_rows),
        "run_provenance": {key: {'generated_at_utc': rows[0].get('snapshot_generated_utc'),
            'first_snapshot_commit': rows[0]['snapshot_commit']} for key, rows in run_rows.items()},
        "groups": groupings,
        "calibration": calibration_buckets(selections),
        "prediction_fixtures_graded": len(graded_prediction),
        "prediction_1x2_multiclass_brier": (
            round(sum(one_x_two) / len(one_x_two), 6) if one_x_two else None
        ),
        "provider_errors": failures,
        "pending_reason_counts": {
            reason: sum(r["status"] == reason for r in selections)
            for reason in sorted({r["status"] for r in selections
                                  if r["status"] not in SETTLED})
        },
    }
    write_json(output / "metrics.json", result)

    intro = [
        "# Forward-only football performance dashboard",
        "",
        "Only immutable **Git-archived before-kickoff predictions** are scored.",
        "Asian handicaps settle full/half wins, refunds and full/half losses. ROI includes every settled stake; refunds are not wins. Probability/Brier follows the frozen event: v23-v25 profitable outcome; v22, v26 and older Asian no net loss.",
        "Actual results come from football-data.org v4 FINISHED matches;",
        "normal 90-minute results are used, never extra-time/penalty scorelines.",
        "**PROVISIONAL candidates are not audited betting recommendations.**",
        "",
        "The main totals use the latest eligible pre-kickoff shortlist entry for each match,",
        "with that prediction's original market, probability, odds and costs. Each match counts once.",
        "Later uploads of an older generation never replace a newer prediction.",
        "Earlier predictions remain in shortlist_run_history.csv and the Run Tracking tab;",
        "history rows are correlated records and are excluded from main win-rate/ROI totals.",
        "Whole-fixture model metrics and research experiments retain their unique-fixture cohorts.",
        "",
        "## Cumulative shortlist — latest prediction per match",
        "",
        report_table({"All selections": result["shortlist"]}),
        "",
        f"Unsettled / unverified entries: **{result['shortlist']['pending']}**.",
        f"Whole-fixture 1X2 multiclass Brier (n={len(one_x_two)}): "
        + ("—" if not one_x_two else f"{result['prediction_1x2_multiclass_brier']:.4f}"),
        "",
        "## First-prediction reference — historical comparison", "",
        report_table({"Unique fixtures": result['first_prediction_reference']}),
        "", "## Latest selections by prediction run (generation UTC)", "", report_table(groupings['run']),
        "", "## STRICT versus PROVISIONAL", "", report_table(groupings["tier"]),
        "", "## By policy", "", report_table(groupings["policy"]),
        "", "## By market", "", report_table(groupings["market"]),
        "", "## By league", "", report_table(groupings["league"]),
        "", "## Gameweeks", "", report_table(groupings["week"]),
        "", "## Confidence calibration of shortlisted markets",
        "", calibration_table(result["calibration"]),
        "",
        "Calibration bins report observed outcomes against the originally",
        "recorded reliability-adjusted chance; small buckets are unstable.",
        "",
        "## Result-source problems", "",
    ]
    if failures:
        intro += [f"- {key}: {value}" for key, value in sorted(failures.items())]
    else:
        intro.append("No provider errors detected.")
    intro += [
        "", "Accuracy is not calibration or profit. Simulated ROI assumes",
        "one unit staked separately on each settled selection with recorded",
        "pre-kickoff bookmaker decimal odds. These are **not real stakes**;",
        "it is not the return from a ten-leg accumulator.",
        "New execution-policy simulations deduct frozen per-stake costs. Legacy snapshots retain their original gross assumptions; compare policy cohorts separately.",
        "Small samples and stale/invalid prices can undermine conclusions.",
        "A missing, ambiguous or unverified result is **never called a win**.",
        "",
    ]
    (output / "README.md").write_text("\n".join(intro), encoding="utf-8")
    weeks_dir = output / "weekly"
    weeks_dir.mkdir(parents=True, exist_ok=True)
    for week in weeks:
        subset = [r for r in selections if r["week"] == week]
        lines = [
            f"# {week} forward performance",
            "",
            "Predictions frozen in Git before kickoff; 90-minute final results.",
            "Provisional near-misses are separate from strict candidates.",
            "",
            report_table({"Gameweek": stats(subset)}),
            "",
            report_table({
                tier: stats([r for r in subset if r["selection_tier"] == tier])
                for tier in ("STRICT", "PROVISIONAL")
            }),
            "",
            "| Match | Market | Tier | Generated UTC | Snapshot | Result | Grade |",
            "|---|---|---|---|---|---|---|",
        ]
        for r in subset:
            label = f"{r['home_team']} – {r['away_team']}".replace("|", "/")
            lines.append(
                f"| {label} | {r['market']} | {r['selection_tier']} "
                f"| {r.get('snapshot_generated_utc') or 'legacy'} | {r['snapshot_commit'][:12]} | {r['final_score'] or '—'} | {r['status']} |"
            )
        lines += ["", "Pending/unverified fixtures are excluded from win-rate and ROI denominators.", ""]
        (weeks_dir / f"{week}.md").write_text("\n".join(lines), encoding="utf-8")
    from performance_excel import write_workbook
    write_workbook(root, selections, all_predictions, result)
    return result


def review(*, root: Path = ROOT, token: str = "",
           clock: datetime | None = None,
           session: requests.Session | None = None) -> dict:
    clock = clock or now_utc()
    archived = snapshots(root)
    selections = frozen_rows(archived, "shortlist", latest=True)
    history = frozen_rows(archived, "shortlist", all_runs=True)
    predictions = frozen_rows(archived, "predictions")
    unique = {r["fixture_key"]: r for r in (selections + predictions)}
    records, errors = collect_results(
        list(unique.values()), root=root, token=token,
        clock=clock, session=session
    )
    matches = {}
    def verified_for(row):
        # Keep exact identities and kickoff instants in the cache key so a
        # rescheduled or renamed fixture cannot borrow another match's result.
        key = (row.get('league'), row.get('home_team'), row.get('away_team'), utc(row.get('kickoff_utc')))
        if key not in matches:
            matches[key] = fixture_match(row, records)
        match, state = matches[key]
        if key[-1] is not None and key[-1] > clock-timedelta(hours=2):
            return None, 'PENDING_KICKOFF_OR_FINAL_SCORE'
        return match, state
    selections_graded, predictions_graded, history_graded = [], [], []
    for row in history:
        match, state = verified_for(row)
        history_graded.append(score_shortlist(row, match, state))
    latest_keys = {tracking_key(r) for r in selections}
    selections_graded = [r for r in history_graded if tracking_key(r) in latest_keys]
    for row in predictions:
        match, state = verified_for(row)
        predictions_graded.append(score_prediction(row, match, state))
    result = report(root, selections_graded, predictions_graded, errors, reviewed_at=iso(clock), selection_history=history_graded)
    try:
        from bbs_statistics_model import forward_assessment
        write_json(root/'performance/bbs_statistics_forward.json',
                   forward_assessment(predictions, records, clock))
    except Exception as exc:
        warnings.warn(f'BBS forward comparison failed ({type(exc).__name__}); production report complete')
    try:
        from goal_blend_experiment import review_experiment
        review_experiment(root, archived, records, clock)
    except Exception as exc:
        warnings.warn(f"Shadow report failed; baseline report complete: {exc}")
    try:
        from market_led_experiment import review_experiment as review_market_led
        review_market_led(root, archived, records, clock)
    except Exception as exc:
        warnings.warn(f"Market-led report failed ({type(exc).__name__}); baseline report complete")
    try:
        from recency_experiment import review_experiment as review_recency
        review_recency(root, archived, records, clock)
    except Exception as exc:
        warnings.warn(f'Recency report failed ({type(exc).__name__}); baseline report complete')
    try:
        from shortlist_weight_experiment import review_experiment as review_weights
        review_weights(root, archived, records, clock)
    except Exception as exc:
        warnings.warn(f'Shortlist weight report failed ({type(exc).__name__}); baseline report complete')
    try:
        from shortlist_policy_experiment import review_experiment as review_policy
        review_policy(root, archived, records, clock)
    except Exception as exc:
        warnings.warn(f'Shortlist policy report failed ({type(exc).__name__}); baseline report complete')
    try:
        from filter_sensitivity_experiment import review_experiment as review_filter
        review_filter(root, archived, records, clock)
    except Exception as exc:
        warnings.warn(f'Filter sensitivity report failed ({type(exc).__name__}); baseline report complete')
    try:
        from benchmark_forward_experiment import review_experiment as review_benchmark
        review_benchmark(root, archived, records, clock)
    except Exception as exc:
        warnings.warn(f'Benchmark forward review failed ({type(exc).__name__}); production report complete')
    try:
        from model_reliability_experiment import review_experiment as review_reliability
        review_reliability(root, archived, records, clock)
    except Exception as exc:
        warnings.warn(f'Reliability review failed ({type(exc).__name__}); production report complete')
    try:
        from totals_anchor_experiment import review_experiment as review_totals
        review_totals(root, archived, records, clock)
    except Exception as exc:
        warnings.warn(f'Totals anchoring review failed ({type(exc).__name__}); production report complete')
    try:
        from closing_odds import review as review_closing
        review_closing(root, archived, clock)
    except Exception as exc:
        warnings.warn(f'Closing quote review failed ({type(exc).__name__}); production report complete')
    try:
        from clv_report import build_report as build_clv_report
        build_clv_report(root, clock=clock)
    except Exception as exc:
        warnings.warn(f'Candidate CLV report failed ({type(exc).__name__}); production report complete')
    from experiment_review_queue import write_queue
    write_queue(root, clock)
    from pipeline_health import write_report
    write_report(root, result, clock)
    print(f"Performance: {result['shortlist']['graded']} graded, "
          f"{result['shortlist']['pending']} pending, "
          f"{result['prediction_fixtures_graded']} full fixture forecasts graded")
    if errors:
        print(f"Result provider needs attention: {errors}", file=sys.stderr)
    return result


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=("capture", "review"))
    parser.add_argument("--commit-sha", default=os.getenv("GITHUB_SHA", ""))
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--api-key-source", choices=("dotenv", "environment"), default="dotenv")
    args = parser.parse_args(argv)
    if args.action == "capture":
        from prediction_runs import capture_runs
        if (args.root/'raw/prediction_runs').exists():
            capture_runs(args.root, args.commit_sha)
        else:
            capture(args.commit_sha, root=args.root)
    else:
        from api_key_config import load_api_keys
        load_api_keys(args.api_key_source)
        review(root=args.root, token=os.getenv("FOOTBALL_DATA_API_KEY", "").strip())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

