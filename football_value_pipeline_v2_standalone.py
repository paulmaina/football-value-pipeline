#!/usr/bin/env python3
"""
football_value_pipeline.py

Keyless football value/probability pipeline for Europe's major leagues.

Data sources:
  - Historical results/odds: Football-Data.co.uk season CSVs
      https://www.football-data.co.uk/mmz4281/{season}/{division}.csv
  - Preferred current fixtures + live market odds: The Odds API v4
      https://api.the-odds-api.com/v4
  - Optional reliable schedule fallback: football-data.org v4
      https://api.football-data.org/v4
  - Last-resort current fixture/odds snapshot: Football-Data.co.uk fixtures.csv

API keys (local CLI reads project .env exclusively; explicit CI mode uses environment):
  - THE_ODDS_API_KEY             primary current fixtures + bookmaker odds
  - THE_ODDS_API_KEY_FALLBACK_1  optional authorized secondary credential
  - THE_ODDS_API_KEY_FALLBACK_2  optional authorized tertiary credential
  - FOOTBALL_DATA_API_KEY        optional schedule fallback for football-data.org

Outputs per fixture:
  - Expected home/away goals
  - 1X2 probabilities and fair decimal odds
  - Full scoreline probability distribution (0..max_goals each side)
  - Over/Under probabilities for 0.5, 1.5, 2.5, 3.5, 4.5 goals
  - If current market odds are available from The Odds API or Football-Data:
      * same-bookmaker de-vigged 1X2 market probabilities
      * best-price model-vs-market probability edge
      * expected value (EV)
      * O/U 2.5 market EV where available

Model:
  - Recency-weighted Dixon-Coles Poisson
  - L2 regularisation
  - Time decay controlled by half_life_days

Install:
    pip install numpy pandas requests scipy rapidfuzz

Examples:
    python football_value_pipeline.py --leagues EPL
    python football_value_pipeline.py --leagues EPL LaLiga Bundesliga SerieA Ligue1
    python football_value_pipeline.py --leagues EPL --seasons-back 4 --lookahead-days 10
    python football_value_pipeline.py --self-test

Designed as a module too:
    from football_value_pipeline import FootballValuePipeline
    pipeline = FootballValuePipeline()
    frames = pipeline.run(["EPL"])
"""

from __future__ import annotations

import argparse
import io
import json
import math
import os
import re
import sys
import unicodedata
import warnings
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Dict, Iterable, List, Mapping, Optional, Sequence, Tuple

import numpy as np
import pandas as pd
import requests
from rapidfuzz import fuzz, process
from requests.adapters import HTTPAdapter
from scipy.optimize import minimize
from scipy.special import gammaln
from scipy.stats import poisson
from urllib3.util.retry import Retry


# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class LeagueConfig:
    key: str
    name: str
    country: str
    football_data_div: str
    odds_api_sport_key: str
    football_data_org_code: str


LEAGUES: Dict[str, LeagueConfig] = {
    "EPL": LeagueConfig(
        "EPL", "Premier League", "England", "E0", "soccer_epl", "PL"
    ),
    "LaLiga": LeagueConfig(
        "LaLiga", "La Liga", "Spain", "SP1", "soccer_spain_la_liga", "PD"
    ),
    "Bundesliga": LeagueConfig(
        "Bundesliga", "Bundesliga", "Germany", "D1",
        "soccer_germany_bundesliga", "BL1"
    ),
    "SerieA": LeagueConfig(
        "SerieA", "Serie A", "Italy", "I1", "soccer_italy_serie_a", "SA"
    ),
    "Ligue1": LeagueConfig(
        "Ligue1", "Ligue 1", "France", "F1", "soccer_france_ligue_one", "FL1"
    ),
    "UCL": LeagueConfig(
        "UCL", "UEFA Champions League", "Europe", "",
        "soccer_uefa_champs_league", "CL"
    ),
}

HISTORICAL_URL = "https://www.football-data.co.uk/mmz4281/{season}/{division}.csv"
FIXTURES_URL = "https://www.football-data.co.uk/fixtures.csv"
THE_ODDS_API_BASE = "https://api.the-odds-api.com/v4"
FOOTBALL_DATA_ORG_BASE = "https://api.football-data.org/v4"

DEFAULT_TOTAL_LINES = (0.5, 1.5, 2.5, 3.5, 4.5)
PIPELINE_VERSION = "2.9.1"


# ---------------------------------------------------------------------------
# Utilities
# ---------------------------------------------------------------------------

def current_season_start_year(now: Optional[datetime] = None) -> int:
    """European season start year: Jul-Dec => current year, Jan-Jun => prior year."""
    now = now or datetime.now(timezone.utc)
    return now.year if now.month >= 7 else now.year - 1


def football_data_season_code(start_year: int) -> str:
    """2026 -> '2627'."""
    return f"{start_year % 100:02d}{(start_year + 1) % 100:02d}"


def safe_float(value) -> Optional[float]:
    try:
        x = float(value)
        return x if math.isfinite(x) else None
    except (TypeError, ValueError):
        return None


def fair_odds(probability: float) -> float:
    return math.inf if probability <= 0 else 1.0 / probability


def ev_decimal(probability: float, decimal_odds: Optional[float]) -> Optional[float]:
    """Expected return per 1 unit staked. 0.05 == +5% EV."""
    if decimal_odds is None or decimal_odds <= 1.0:
        return None
    return probability * decimal_odds - 1.0


def devig_decimal(odds: Sequence[Optional[float]]) -> List[Optional[float]]:
    """Proportional de-vig. Returns normalized implied probabilities."""
    if not odds or any(o is None or o <= 1.0 for o in odds):
        return [None for _ in odds]
    inv = np.array([1.0 / float(o) for o in odds], dtype=float)
    s = float(inv.sum())
    return [float(x / s) for x in inv]


def normalize_team_name(name: str) -> str:
    s = unicodedata.normalize("NFKD", str(name))
    s = "".join(ch for ch in s if not unicodedata.combining(ch)).lower()
    s = s.replace("&", " and ")
    s = re.sub(r"[^a-z0-9]+", " ", s)
    tokens = [
        t for t in re.split(r"\s+", s.strip())
        if t and t not in {
            "fc", "cf", "afc", "ac", "sc", "sv", "club", "de", "football",
            "calcio", "1904", "1899", "04", "05"
        }
    ]
    return " ".join(tokens)


# A small explicit alias layer handles common cross-provider mismatches before fuzzy matching.
TEAM_ALIASES = {
    "manchester united": "Man United",
    "man utd": "Man United",
    "manchester city": "Man City",
    "tottenham hotspur": "Tottenham",
    "spurs": "Tottenham",
    "west ham united": "West Ham",
    "wolverhampton wanderers": "Wolves",
    "newcastle united": "Newcastle",
    "nottingham forest": "Nott'm Forest",
    "brighton and hove albion": "Brighton",
    "leeds united": "Leeds",
    "paris saint germain": "Paris SG",
    "paris saint-germain": "Paris SG",
    "internazionale": "Inter",
    "inter milan": "Inter",
    "ac milan": "Milan",
    "bayern munich": "Bayern Munich",
    "borussia monchengladbach": "M'gladbach",
    "borussia mönchengladbach": "M'gladbach",
    "athletic club": "Ath Bilbao",
    "athletic bilbao": "Ath Bilbao",
    "atletico madrid": "Ath Madrid",
    "atlético madrid": "Ath Madrid",
    "internazionale milano": "Inter",
    "fc internazionale milano": "Inter",
    "bayern munchen": "Bayern Munich",
    "fc bayern munchen": "Bayern Munich",
    "sporting clube portugal": "Sporting CP",
    "sporting lisbon": "Sporting CP",
    "psv eindhoven": "PSV",
    "feyenoord rotterdam": "Feyenoord",
    "slavia praha": "Slavia Prague",
    "sk slavia praha": "Slavia Prague",
    "shakhtar donetsk": "Shakhtar",
    "fc shakhtar donetsk": "Shakhtar",
    "bodo glimt": "Bodo/Glimt",
    "bodoe glimt": "Bodo/Glimt",
    "red bull salzburg": "Salzburg",
    "fc salzburg": "Salzburg",
}


def canonical_team_key(name: str) -> str:
    """Stable cross-provider key used only for strict fixture/odds matching."""
    normalized = normalize_team_name(name)
    alias = TEAM_ALIASES.get(normalized)
    return normalize_team_name(alias if alias else name)


# ---------------------------------------------------------------------------
# HTTP + cache
# ---------------------------------------------------------------------------

class CachedHttpClient:
    def __init__(self, cache_dir: str | Path = ".football_cache", timeout: int = 20):
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        self.timeout = timeout

        retry = Retry(
            total=4,
            connect=4,
            read=4,
            status=4,
            backoff_factor=0.6,
            status_forcelist=(429, 500, 502, 503, 504),
            allowed_methods=frozenset({"GET"}),
            raise_on_status=False,
        )
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "football-value-pipeline/2.0 (+research; public-data-client)"
        })
        self.session.mount("https://", HTTPAdapter(max_retries=retry))
        self.session.mount("http://", HTTPAdapter(max_retries=retry))

    def get_bytes(
        self,
        url: str,
        cache_name: str,
        ttl: timedelta,
        force_refresh: bool = False,
        params: Optional[Mapping[str, object]] = None,
        headers: Optional[Mapping[str, str]] = None,
        allow_stale: bool = True,
    ) -> bytes:
        """GET bytes with TTL caching. Secrets in params are never written to cache names/logs."""
        path = self.cache_dir / cache_name

        if path.exists() and not force_refresh:
            age = datetime.now(timezone.utc).timestamp() - path.stat().st_mtime
            if age <= ttl.total_seconds():
                return path.read_bytes()

        try:
            r = self.session.get(
                url,
                params=dict(params or {}),
                headers=dict(headers or {}),
                timeout=self.timeout,
            )
            r.raise_for_status()
            content = r.content
            if len(content) < 2:
                raise RuntimeError(f"Suspiciously small response from {url}")
            path.write_bytes(content)
            return content
        except Exception:
            if allow_stale and path.exists():
                warnings.warn(
                    f"Live download failed for {url}; using stale cache {path}",
                    RuntimeWarning,
                )
                return path.read_bytes()
            raise

    def get_json(
        self,
        url: str,
        cache_name: str,
        ttl: timedelta,
        force_refresh: bool = False,
        params: Optional[Mapping[str, object]] = None,
        headers: Optional[Mapping[str, str]] = None,
        allow_stale: bool = True,
    ):
        content = self.get_bytes(
            url=url,
            cache_name=cache_name,
            ttl=ttl,
            force_refresh=force_refresh,
            params=params,
            headers=headers,
            allow_stale=allow_stale,
        )
        try:
            return json.loads(content.decode("utf-8-sig"))
        except (UnicodeDecodeError, json.JSONDecodeError) as exc:
            raise RuntimeError(f"Invalid JSON response from {url}") from exc


def read_csv_bytes(content: bytes) -> pd.DataFrame:
    """Football-Data files occasionally vary in encoding."""
    last_error = None
    for encoding in ("utf-8-sig", "latin-1"):
        try:
            return pd.read_csv(
                io.BytesIO(content),
                encoding=encoding,
                on_bad_lines="skip",
                low_memory=False,
            )
        except Exception as exc:
            last_error = exc
    raise last_error  # type: ignore[misc]


# ---------------------------------------------------------------------------
# Football-Data.co.uk ingestion
# ---------------------------------------------------------------------------

class FootballDataUK:
    def __init__(
        self,
        cache_dir: str | Path = ".football_cache",
        force_refresh: bool = False,
    ):
        self.http = CachedHttpClient(cache_dir=cache_dir)
        self.force_refresh = force_refresh

    def season(
        self,
        league: LeagueConfig,
        start_year: int,
        current_start_year: int,
    ) -> pd.DataFrame:
        season_code = football_data_season_code(start_year)
        url = HISTORICAL_URL.format(
            season=season_code,
            division=league.football_data_div,
        )
        # Current season changes frequently; older seasons effectively do not.
        ttl = timedelta(hours=4) if start_year == current_start_year else timedelta(days=30)
        content = self.http.get_bytes(
            url,
            f"{season_code}_{league.football_data_div}.csv",
            ttl=ttl,
            force_refresh=self.force_refresh,
        )
        df = read_csv_bytes(content).copy()
        df["Season"] = season_code
        return df

    def history(
        self,
        league: LeagueConfig,
        seasons_back: int = 3,
        now: Optional[datetime] = None,
    ) -> pd.DataFrame:
        now = now or datetime.now(timezone.utc)
        current_start = current_season_start_year(now)
        frames = []

        for start_year in range(current_start - seasons_back + 1, current_start + 1):
            try:
                frames.append(self.season(league, start_year, current_start))
            except Exception as exc:
                warnings.warn(
                    f"Skipping {league.name} {start_year}/{start_year + 1}: {exc}",
                    RuntimeWarning,
                )

        if not frames:
            raise RuntimeError(f"No history downloaded for {league.name}")

        df = pd.concat(frames, ignore_index=True, sort=False)

        required = {"Date", "HomeTeam", "AwayTeam", "FTHG", "FTAG"}
        missing = required.difference(df.columns)
        if missing:
            raise ValueError(f"{league.name}: historical data missing columns {sorted(missing)}")

        df["Date"] = pd.to_datetime(df["Date"], dayfirst=True, errors="coerce")
        df["FTHG"] = pd.to_numeric(df["FTHG"], errors="coerce")
        df["FTAG"] = pd.to_numeric(df["FTAG"], errors="coerce")

        df = df.dropna(subset=["Date", "HomeTeam", "AwayTeam", "FTHG", "FTAG"]).copy()
        df = df[df["Date"] < pd.Timestamp(now.date()) + pd.Timedelta(days=1)]
        df["FTHG"] = df["FTHG"].astype(int)
        df["FTAG"] = df["FTAG"].astype(int)
        df = df.sort_values("Date").reset_index(drop=True)
        return df

    def fixtures(
        self,
        league: LeagueConfig,
        lookahead_days: int = 10,
        now: Optional[datetime] = None,
    ) -> pd.DataFrame:
        """
        Read the current Football-Data.co.uk fixture snapshot.

        This is a last-resort current source. Unlike older versions, this method
        deliberately does NOT fall back to FixtureDownload because a stale or
        incorrect schedule is worse than returning no fixtures.
        """
        now = now or datetime.now(timezone.utc)

        try:
            content = self.http.get_bytes(
                FIXTURES_URL,
                "fixtures.csv",
                ttl=timedelta(minutes=30),
                force_refresh=self.force_refresh,
                allow_stale=False,
            )

            head = content[:256].lstrip().lower()
            if head.startswith(b"<html") or head.startswith(b"<!doctype html"):
                raise RuntimeError("Football-Data fixtures endpoint returned HTML, not CSV")

            df = read_csv_bytes(content)
            required = {"Div", "Date", "HomeTeam", "AwayTeam"}
            missing = required.difference(df.columns)
            if missing:
                raise ValueError(
                    f"Football-Data fixtures.csv missing columns {sorted(missing)}"
                )

            df = df[df["Div"].astype(str) == league.football_data_div].copy()
            if df.empty:
                return pd.DataFrame()

            df["Date"] = pd.to_datetime(df["Date"], dayfirst=True, errors="coerce")
            df = df.dropna(subset=["Date", "HomeTeam", "AwayTeam"])

            today = pd.Timestamp(now.date())
            last = today + pd.Timedelta(days=lookahead_days)
            df = df[(df["Date"] >= today) & (df["Date"] <= last)].copy()
            if df.empty:
                return pd.DataFrame()

            df["fixture_source"] = "Football-Data.co.uk"
            df["fixture_id"] = [
                f"fdco:{league.key}:{d.date()}:{canonical_team_key(h)}:{canonical_team_key(a)}"
                for d, h, a in zip(df["Date"], df["HomeTeam"], df["AwayTeam"])
            ]
            df["kickoff_utc"] = None
            return df.sort_values(["Date", "HomeTeam"]).reset_index(drop=True)

        except Exception as exc:
            warnings.warn(
                f"Football-Data.co.uk current fixture lookup failed for "
                f"{league.name}: {exc}",
                RuntimeWarning,
            )
            return pd.DataFrame()


# ---------------------------------------------------------------------------
# Reliable current fixtures + dedicated live odds
# ---------------------------------------------------------------------------

class TheOddsAPI:
    """Current event schedule and market-odds client for The Odds API v4.

    Optional credential redundancy is for provider-authorized usage only.
    It does not imply permission to pool multiple accounts' free quotas.
    """

    KEY_ENV_NAMES = (
        "THE_ODDS_API_KEY",
        "THE_ODDS_API_KEY_FALLBACK_1",
        "THE_ODDS_API_KEY_FALLBACK_2",
    )

    def __init__(
        self,
        api_key: str,
        cache_dir: str | Path = ".football_cache",
        force_refresh: bool = False,
        regions: str = "eu",
    ):
        if not api_key:
            raise ValueError("The Odds API key is required")
        self.api_key = api_key
        self.http = CachedHttpClient(cache_dir=cache_dir)
        self.force_refresh = force_refresh
        self.regions = regions

        # The generic historical-data client retries 429 automatically.
        # Do not do that for this Odds API instance: quota/rate-limit
        # failures must be passed promptly to the credential failover.
        retry = Retry(
            total=4,
            connect=4,
            read=4,
            status=4,
            backoff_factor=0.6,
            status_forcelist=(500, 502, 503, 504),
            allowed_methods=frozenset({"GET"}),
            raise_on_status=False,
        )
        self.http.session.mount(
            THE_ODDS_API_BASE + "/",
            HTTPAdapter(max_retries=retry),
        )

    def _configured_keys(self) -> List[Tuple[str, str]]:
        """Read secrets at REQUEST time; don't freeze fallback env at startup."""
        result: List[Tuple[str, str]] = []
        seen = set()
        explicit_in_fallback = {
            os.getenv(name, "").strip()
            for name in self.KEY_ENV_NAMES[1:]
        }
        for name in self.KEY_ENV_NAMES:
            value = os.getenv(name, "").strip()
            # Preserve an explicitly passed legacy key, but if the
            # constructor got its default from FALLBACK_1/2, keep the
            # *correct* fallback label instead of calling it primary.
            if (
                name == "THE_ODDS_API_KEY" and not value
                and self.api_key not in explicit_in_fallback
            ):
                value = self.api_key
            if value and value not in seen:
                seen.add(value)
                result.append((name, value))
        return result

    @staticmethod
    def _is_quota_http_error(exc: requests.HTTPError) -> bool:
        response = exc.response
        if response is None:
            return False
        if response.status_code == 429:
            return True
        if response.status_code not in (401, 403):
            return False
        # 401/403 often means INVALID_KEY or DEACTIVATED_KEY; do not
        # silently disguise a bad credential as monthly credit depletion.
        try:
            payload = response.json()
            if isinstance(payload, dict):
                code = str(payload.get("error_code") or "").upper()
                if code == "OUT_OF_USAGE_CREDITS":
                    return True
                # Tolerate providers that expose a text error instead of
                # the canonical error_code, but only for this exact token.
                if "OUT_OF_USAGE_CREDITS" in str(payload.get("message") or "").upper():
                    return True
        except ValueError:
            pass
        return "OUT_OF_USAGE_CREDITS" in response.text.upper()

    def _get_json(self, url: str, cache_name: str, **kwargs):
        """One cached request; on confirmed quota/rate limits, try next key.

        Do not log secrets or error URLs (which include apiKey). A cache
        hit makes no live request. Non-quota HTTP or network errors fail
        immediately without consuming other credentials.
        """
        keys = self._configured_keys()
        if not keys:
            raise RuntimeError(
                "The Odds API is not configured: set THE_ODDS_API_KEY "
                "or an authorized fallback key."
            )
        original = dict(kwargs.pop("params", {}) or {})
        original.pop("apiKey", None)
        # Normal pipeline uses allow_stale=False for current odds;
        # never turn a quota error into a fabricated or stale live price.
        for name, key in keys:
            try:
                return self.http.get_json(
                    url,
                    cache_name,
                    params={**original, "apiKey": key},
                    **kwargs,
                )
            except requests.HTTPError as exc:
                if self._is_quota_http_error(exc):
                    code = exc.response.status_code if exc.response is not None else "?"
                    warnings.warn(
                        f"The Odds API {name} returned HTTP {code} "
                        "(quota/rate-limit); trying the next configured key.",
                        RuntimeWarning,
                    )
                    continue
                status = (
                    exc.response.status_code
                    if exc.response is not None else "unknown"
                )
                raise RuntimeError(
                    f"The Odds API returned HTTP {status} using {name}; "
                    "not a confirmed quota/rate-limit error."
                ) from None
            except requests.RequestException:
                raise RuntimeError(
                    f"The Odds API network request failed using {name}; "
                    "other keys were not attempted."
                ) from None
        raise RuntimeError(
            "The Odds API: all configured keys returned quota/rate-limit "
            "errors. No bookmaker odds were retrieved."
        )

    @staticmethod
    def _window(now: datetime, lookahead_days: int) -> Tuple[str, str]:
        start = now.astimezone(timezone.utc)
        end = start + timedelta(days=lookahead_days)
        return (
            start.isoformat(timespec="seconds").replace("+00:00", "Z"),
            end.isoformat(timespec="seconds").replace("+00:00", "Z"),
        )

    def events(
        self,
        league: LeagueConfig,
        lookahead_days: int,
        now: datetime,
    ) -> pd.DataFrame:
        start, end = self._window(now, lookahead_days)
        url = f"{THE_ODDS_API_BASE}/sports/{league.odds_api_sport_key}/events"
        payload = self._get_json(
            url,
            f"oddsapi_events_{league.key}.json",
            ttl=timedelta(minutes=10),
            force_refresh=self.force_refresh,
            params={
                "apiKey": self.api_key,
                "dateFormat": "iso",
                "commenceTimeFrom": start,
                "commenceTimeTo": end,
            },
            allow_stale=False,
        )
        if not isinstance(payload, list):
            raise RuntimeError("The Odds API events response was not a list")

        rows: List[Dict[str, object]] = []
        for event in payload:
            if not isinstance(event, dict):
                continue
            event_id = event.get("id")
            home = event.get("home_team")
            away = event.get("away_team")
            raw_dt = event.get("commence_time")
            if not event_id or not home or not away or not raw_dt:
                continue
            dt = pd.to_datetime(raw_dt, utc=True, errors="coerce")
            if pd.isna(dt):
                continue
            rows.append({
                "Div": league.football_data_div,
                "Date": dt.tz_convert(None),
                "HomeTeam": str(home),
                "AwayTeam": str(away),
                "fixture_source": "The Odds API",
                "fixture_id": str(event_id),
                "kickoff_utc": dt.isoformat(),
            })

        if not rows:
            return pd.DataFrame()
        df = pd.DataFrame(rows)
        return (
            df.drop_duplicates(subset=["fixture_id"])
            .sort_values(["Date", "HomeTeam"])
            .reset_index(drop=True)
        )

    @staticmethod
    def _market(bookmaker: Mapping[str, object], key: str) -> Optional[Mapping[str, object]]:
        markets = bookmaker.get("markets")
        if not isinstance(markets, list):
            return None
        for market in markets:
            if isinstance(market, dict) and market.get("key") == key:
                return market
        return None

    @staticmethod
    def _last_update(bookmaker: Mapping[str, object], market: Mapping[str, object]) -> str:
        value = market.get("last_update") or bookmaker.get("last_update") or ""
        return str(value)

    @staticmethod
    def _coherent_overround(prices: Sequence[float], low: float = 0.98,
                            high: float = 1.20) -> bool:
        """Reject crossed, placeholder, incomplete or pathological bookmaker books.

        Margin bounds are data-quality guardrails, not confidence calibration.
        Do not blend against extreme outlier quotes merely because their
        last_update is the newest.
        """
        if not prices or any(
            not math.isfinite(float(price)) or float(price) <= 1.0
            for price in prices
        ):
            return False
        margin = sum(1.0 / float(price) for price in prices)
        return low <= margin <= high

    @staticmethod
    def flatten_odds_event(event: Mapping[str, object]) -> Dict[str, object]:
        """Flatten one API event into best prices + coherent reference markets."""
        event_id = str(event.get("id") or "")
        home = str(event.get("home_team") or "")
        away = str(event.get("away_team") or "")
        commence = str(event.get("commence_time") or "")

        best_h: Tuple[Optional[float], Optional[str]] = (None, None)
        best_d: Tuple[Optional[float], Optional[str]] = (None, None)
        best_a: Tuple[Optional[float], Optional[str]] = (None, None)
        best_o: Tuple[Optional[float], Optional[str]] = (None, None)
        best_u: Tuple[Optional[float], Optional[str]] = (None, None)
        complete_h2h: List[Tuple[str, str, float, float, float]] = []
        complete_ou: List[Tuple[str, str, float, float]] = []
        all_updates: List[str] = []
        h2h_book_updates: Dict[str, str] = {}
        pinnacle_totals = None

        def update_best(
            current: Tuple[Optional[float], Optional[str]],
            price: Optional[float],
            bookmaker_name: str,
        ) -> Tuple[Optional[float], Optional[str]]:
            from quote_policy import usable_bookmaker
            if price is None or price <= 1.0 or not usable_bookmaker(bookmaker_name):
                return current
            if current[0] is None or price > float(current[0]):
                return (price, bookmaker_name)
            return current

        bookmakers = event.get("bookmakers")
        if not isinstance(bookmakers, list):
            bookmakers = []

        home_key = canonical_team_key(home)
        away_key = canonical_team_key(away)

        for bookmaker in bookmakers:
            if not isinstance(bookmaker, dict):
                continue
            book_name = str(bookmaker.get("title") or bookmaker.get("key") or "unknown")

            h2h = TheOddsAPI._market(bookmaker, "h2h")
            if h2h:
                # Timestamp each bookmaker's selected 1X2 quote, not the
                # unrelated latest totals/other-bookmaker update.
                h2h_book_updates[book_name] = TheOddsAPI._last_update(bookmaker, h2h)
                prices: Dict[str, float] = {}
                outcomes = h2h.get("outcomes")
                if isinstance(outcomes, list):
                    for outcome in outcomes:
                        if not isinstance(outcome, dict):
                            continue
                        name = str(outcome.get("name") or "")
                        price = safe_float(outcome.get("price"))
                        if price is None or price <= 1.0:
                            continue
                        key = canonical_team_key(name)
                        if key == home_key:
                            prices["home"] = price
                        elif key == away_key:
                            prices["away"] = price
                        elif name.strip().lower() == "draw":
                            prices["draw"] = price
                if (
                    all(k in prices for k in ("home", "draw", "away"))
                    and TheOddsAPI._coherent_overround(
                        [prices["home"], prices["draw"], prices["away"]]
                    )
                ):
                    best_h = update_best(best_h, prices["home"], book_name)
                    best_d = update_best(best_d, prices["draw"], book_name)
                    best_a = update_best(best_a, prices["away"], book_name)
                    updated = TheOddsAPI._last_update(bookmaker, h2h)
                    complete_h2h.append((
                        updated, book_name, prices["home"], prices["draw"], prices["away"]
                    ))
                    if updated:
                        all_updates.append(updated)

            totals = TheOddsAPI._market(bookmaker, "totals")
            if totals:
                prices: Dict[str, float] = {}
                outcomes = totals.get("outcomes")
                if isinstance(outcomes, list):
                    for outcome in outcomes:
                        if not isinstance(outcome, dict):
                            continue
                        point = safe_float(outcome.get("point"))
                        if point is None or abs(point - 2.5) > 1e-9:
                            continue
                        name = str(outcome.get("name") or "").strip().lower()
                        price = safe_float(outcome.get("price"))
                        if price is None or price <= 1.0:
                            continue
                        if name == "over":
                            prices["over"] = price
                        elif name == "under":
                            prices["under"] = price
                if (
                    all(k in prices for k in ("over", "under"))
                    and TheOddsAPI._coherent_overround(
                        [prices["over"], prices["under"]]
                    )
                ):
                    best_o = update_best(best_o, prices["over"], book_name)
                    best_u = update_best(best_u, prices["under"], book_name)
                    updated = TheOddsAPI._last_update(bookmaker, totals)
                    complete_ou.append((updated, book_name, prices["over"], prices["under"]))
                    if str(bookmaker.get("key", "")).lower() == "pinnacle":
                        pinnacle_totals = {"updated_at_utc": updated, "over": prices["over"], "under": prices["under"], "bookmaker": "pinnacle", "event_id": event_id, "kickoff_utc": commence, "home_team": home, "away_team": away}
                    if updated:
                        all_updates.append(updated)

        from quote_policy import usable_bookmaker
        ref_h2h = max(complete_h2h, key=lambda x: x[0], default=None)
        ref_ou = max(complete_ou, key=lambda x: x[0], default=None)

        return {
            "fixture_id": event_id,
            "_odds_home_team": home,
            "_odds_away_team": away,
            "_odds_commence_time": commence,
            "odds_source": "The Odds API",
            "odds_last_update_utc": max(all_updates) if all_updates else None,
            "odds_h2h_last_update_utc": None if ref_h2h is None else ref_h2h[0],
            "odds_bookmakers_1x2": sum(1 for x in complete_h2h if usable_bookmaker(x[1])),
            "odds_bookmakers_ou25": len(complete_ou),
            "live_best_home_odds": best_h[0],
            "live_best_home_bookmaker": best_h[1],
            "live_best_home_last_update_utc": h2h_book_updates.get(best_h[1]),
            "live_best_draw_odds": best_d[0],
            "live_best_draw_bookmaker": best_d[1],
            "live_best_draw_last_update_utc": h2h_book_updates.get(best_d[1]),
            "live_best_away_odds": best_a[0],
            "live_best_away_bookmaker": best_a[1],
            "live_best_away_last_update_utc": h2h_book_updates.get(best_a[1]),
            "live_ref_home_odds": None if ref_h2h is None else ref_h2h[2],
            "live_ref_draw_odds": None if ref_h2h is None else ref_h2h[3],
            "live_ref_away_odds": None if ref_h2h is None else ref_h2h[4],
            "live_ref_1x2_bookmaker": None if ref_h2h is None else ref_h2h[1],
            "live_best_over_2_5_odds": best_o[0],
            "live_best_over_2_5_bookmaker": best_o[1],
            "live_best_under_2_5_odds": best_u[0],
            "live_best_under_2_5_bookmaker": best_u[1],
            "live_ref_over_2_5_odds": None if ref_ou is None else ref_ou[2],
            "live_ref_under_2_5_odds": None if ref_ou is None else ref_ou[3],
            "live_ref_ou25_bookmaker": None if ref_ou is None else ref_ou[1],
            "shadow_pinnacle_totals": pinnacle_totals,
        }

    def odds(
        self,
        league: LeagueConfig,
        lookahead_days: int,
        now: datetime,
    ) -> pd.DataFrame:
        start, end = self._window(now, lookahead_days)
        url = f"{THE_ODDS_API_BASE}/sports/{league.odds_api_sport_key}/odds"
        region_tag = re.sub(r"[^a-z0-9]+", "_", self.regions.lower()).strip("_")
        payload = self._get_json(
            url,
            f"oddsapi_odds_{league.key}_{region_tag}.json",
            ttl=timedelta(minutes=5),
            force_refresh=self.force_refresh,
            params={
                "apiKey": self.api_key,
                "regions": self.regions,
                "markets": "h2h,totals",
                "oddsFormat": "decimal",
                "dateFormat": "iso",
                "commenceTimeFrom": start,
                "commenceTimeTo": end,
            },
            allow_stale=False,
        )
        if not isinstance(payload, list):
            raise RuntimeError("The Odds API odds response was not a list")
        rows = [
            self.flatten_odds_event(event)
            for event in payload
            if isinstance(event, dict) and event.get("id")
        ]
        return pd.DataFrame(rows)

    def extra_markets_for_event(
        self, league: LeagueConfig, event_id: str
    ) -> Dict[str, object]:
        """Per-event real-price request for alternate totals and BTTS.

        Additional markets are bookmaker/competition dependent. All
        returned prices must be verified complementary outcome pairs
        from the same bookmaker; never estimate unlisted odds.
        """
        safe_id = str(event_id)
        if not re.fullmatch(r"[A-Za-z0-9_-]+", safe_id):
            raise ValueError("Invalid The Odds API event ID")
        url = (
            f"{THE_ODDS_API_BASE}/sports/{league.odds_api_sport_key}"
            f"/events/{safe_id}/odds"
        )
        region_tag = re.sub(r"[^a-z0-9]+", "_", self.regions.lower()).strip("_")
        payload = self._get_json(
            url,
            f"oddsapi_additional_dc_v1_{league.key}_{region_tag}_{safe_id}.json",
            ttl=timedelta(minutes=5),
            force_refresh=self.force_refresh,
            params={
                "apiKey": self.api_key,
                "regions": self.regions,
                "markets": "alternate_totals,btts,double_chance",
                "oddsFormat": "decimal",
                "dateFormat": "iso",
            },
            allow_stale=False,
        )
        if not isinstance(payload, dict) or str(payload.get("id")) != safe_id:
            raise RuntimeError("Event odds response missing/mismatched ID")

        offers: Dict[str, List[Tuple[str, str, float, float]]] = {
            "over_1_5": [], "under_3_5": [], "btts_yes": [],
        }
        books = payload.get("bookmakers")
        if not isinstance(books, list):
            return {}

        for book in books:
            if not isinstance(book, dict):
                continue
            name = str(book.get("title") or book.get("key") or "").strip()
            if not name:
                continue
            for market_key in ("alternate_totals", "btts"):
                market = self._market(book, market_key)
                if market is None:
                    continue
                outcomes = market.get("outcomes")
                if not isinstance(outcomes, list):
                    continue
                updated = self._last_update(book, market)
                for point in ((1.5, 3.5) if market_key == "alternate_totals" else (None,)):
                    pair: Dict[str, float] = {}
                    for outcome in outcomes:
                        if not isinstance(outcome, dict):
                            continue
                        if point is not None and safe_float(outcome.get("point")) != point:
                            continue
                        side = str(outcome.get("name") or "").lower().strip()
                        price = _valid_price(outcome.get("price"))
                        if price is not None:
                            pair[side] = price
                    left, right = (
                        ("over", "under") if point is not None else ("yes", "no")
                    )
                    if (
                        left not in pair or right not in pair
                        or not self._coherent_overround([pair[left], pair[right]])
                    ):
                        continue
                    if point == 1.5:
                        offers["over_1_5"].append(
                            (updated, name, pair["over"], pair["under"])
                        )
                    elif point == 3.5:
                        offers["under_3_5"].append(
                            (updated, name, pair["under"], pair["over"])
                        )
                    else:
                        offers["btts_yes"].append(
                            (updated, name, pair["yes"], pair["no"])
                        )

        from double_chance import parse_quotes
        result: Dict[str, object] = parse_quotes(payload)
        for market, available in offers.items():
            if not available:
                continue
            ref = max(available, key=lambda x: x[0])
            from quote_policy import usable_bookmaker
            usable = [x for x in available if usable_bookmaker(x[1])]
            best = max(usable, key=lambda x: x[2]) if usable else (None, None, None, None)
            fair = devig([ref[2], ref[3]], method="power")
            result[f"market_p_{market}"] = fair[0]
            result[f"market_{market}_odds"] = best[2]
            result[f"best_{market}_bookmaker"] = best[1]
            result[f"market_best_{market}_last_update_utc"] = best[0] or None
            result[f"market_reference_{market}_odds"] = ref[2]
            result[f"market_reference_{market}_opposite_odds"] = ref[3]
            result[f"market_{market}_bookmakers"] = len({x[1] for x in usable})
        return result


class FootballDataOrg:
    """Optional v4 fixture fallback backed by football-data.org."""

    def __init__(
        self,
        api_key: str,
        cache_dir: str | Path = ".football_cache",
        force_refresh: bool = False,
    ):
        if not api_key:
            raise ValueError("football-data.org API key is required")
        self.api_key = api_key
        self.http = CachedHttpClient(cache_dir=cache_dir)
        self.force_refresh = force_refresh

    def fixtures(
        self,
        league: LeagueConfig,
        lookahead_days: int,
        now: datetime,
    ) -> pd.DataFrame:
        start_date = now.astimezone(timezone.utc).date()
        end_date = start_date + timedelta(days=lookahead_days)
        url = (
            f"{FOOTBALL_DATA_ORG_BASE}/competitions/"
            f"{league.football_data_org_code}/matches"
        )
        payload = self.http.get_json(
            url,
            f"fdorg_fixtures_{league.key}.json",
            ttl=timedelta(minutes=15),
            force_refresh=self.force_refresh,
            params={
                "dateFrom": start_date.isoformat(),
                "dateTo": end_date.isoformat(),
            },
            headers={"X-Auth-Token": self.api_key},
            allow_stale=False,
        )
        matches = payload.get("matches") if isinstance(payload, dict) else None
        if not isinstance(matches, list):
            raise RuntimeError("football-data.org matches response missing 'matches'")

        rows: List[Dict[str, object]] = []
        excluded = {"FINISHED", "CANCELLED", "POSTPONED", "SUSPENDED"}
        for match in matches:
            if not isinstance(match, dict):
                continue
            if str(match.get("status") or "").upper() in excluded:
                continue
            home_obj = match.get("homeTeam")
            away_obj = match.get("awayTeam")
            if not isinstance(home_obj, dict) or not isinstance(away_obj, dict):
                continue
            home = home_obj.get("name")
            away = away_obj.get("name")
            raw_dt = match.get("utcDate")
            match_id = match.get("id")
            if not home or not away or not raw_dt or match_id is None:
                continue
            dt = pd.to_datetime(raw_dt, utc=True, errors="coerce")
            if pd.isna(dt):
                continue
            rows.append({
                "Div": league.football_data_div,
                "Date": dt.tz_convert(None),
                "HomeTeam": str(home),
                "AwayTeam": str(away),
                "fixture_source": "football-data.org",
                "fixture_id": f"fdorg:{match_id}",
                "kickoff_utc": dt.isoformat(),
            })

        if not rows:
            return pd.DataFrame()
        return (
            pd.DataFrame(rows)
            .drop_duplicates(subset=["fixture_id"])
            .sort_values(["Date", "HomeTeam"])
            .reset_index(drop=True)
        )


    def history(
        self,
        league: LeagueConfig,
        seasons_back: int,
        now: datetime,
    ) -> pd.DataFrame:
        """
        Load completed competition matches for model training.

        For UCL this provides genuine cross-league observations, avoiding the
        invalid assumption that domestic-league ratings are directly comparable.
        Older-season availability depends on the football-data.org subscription;
        inaccessible seasons are skipped and the model uses all accessible data.
        """
        current_start = current_season_start_year(now)
        frames: List[pd.DataFrame] = []
        failures: List[str] = []

        # One validated current-season refresh per provider instance. Filesystem
        # mtimes after git pull do not establish a successful provider download.
        if league.key == "UCL" and getattr(self, "_ucl_refresh_year", None) != current_start:
            from ucl_training import fetch_payload, apply_payload
            self._ucl_refresh_year = current_start
            self.ucl_refresh_error = None
            self.ucl_refresh_error_reason = None
            try:
                payload = fetch_payload(self.api_key, current_start, session=self.http.session)
                apply_payload(self.http.cache_dir.resolve().parent, payload, current_start, now,
                              cache_dir=self.http.cache_dir)
            except Exception as exc:
                self.ucl_refresh_error = type(exc).__name__
                # Domain validation/decoding errors contain useful reasons;
                # network exception URLs/headers are not copied into diagnostics.
                self.ucl_refresh_error_reason = str(exc).splitlines()[0][:200] if isinstance(exc, ValueError) and str(exc) else None
                warnings.warn("UCL live training refresh failed validation/download; retained previous cache ("
                              + self.ucl_refresh_error + (": " + self.ucl_refresh_error_reason if self.ucl_refresh_error_reason else "")
                              + ")", RuntimeWarning)

        for start_year in range(
            current_start - int(seasons_back) + 1,
            current_start + 1,
        ):
            url = (
                f"{FOOTBALL_DATA_ORG_BASE}/competitions/"
                f"{league.football_data_org_code}/matches"
            )
            try:
                current_path = self.http.cache_dir / f"fdorg_history_{league.key}_{start_year}.json"
                if league.key == "UCL" and start_year == current_start:
                    if not current_path.exists():
                        raise RuntimeError("No validated current-season UCL cache available")
                    payload = json.loads(current_path.read_text(encoding="utf-8-sig"))
                    from ucl_training import inspect_payload
                    inspect_payload(payload, current_start, now)
                else:
                    payload = self.http.get_json(
                        url,
                        f"fdorg_history_{league.key}_{start_year}.json",
                        ttl=(
                            timedelta(hours=4)
                            if start_year == current_start
                            else timedelta(days=30)
                        ),
                        force_refresh=self.force_refresh if start_year != current_start else False,
                        params={
                            "season": start_year,
                            "status": "FINISHED",
                        },
                        headers={"X-Auth-Token": self.api_key},
                        allow_stale=True,
                    )
            except Exception as exc:
                failures.append(f"{start_year}: {exc}")
                continue

            matches = payload.get("matches") if isinstance(payload, dict) else None
            if not isinstance(matches, list):
                failures.append(f"{start_year}: response missing matches")
                continue

            rows: List[Dict[str, object]] = []
            for match in matches:
                if not isinstance(match, dict):
                    continue
                if str(match.get("status") or "").upper() != "FINISHED":
                    continue

                home_obj = match.get("homeTeam")
                away_obj = match.get("awayTeam")
                score_obj = match.get("score")
                if (
                    not isinstance(home_obj, dict)
                    or not isinstance(away_obj, dict)
                    or not isinstance(score_obj, dict)
                ):
                    continue

                from match_scores import regulation_goals
                goals = regulation_goals(score_obj)
                if goals is None:
                    continue

                home = home_obj.get("name")
                away = away_obj.get("name")
                hg, ag = goals
                raw_dt = match.get("utcDate")
                if (
                    not home
                    or not away
                    or hg is None
                    or ag is None
                    or not raw_dt
                ):
                    continue

                dt = pd.to_datetime(raw_dt, utc=True, errors="coerce")
                if pd.isna(dt) or dt >= pd.Timestamp(now):
                    continue

                rows.append({
                    "Date": dt.tz_convert(None),
                    "HomeTeam": str(home),
                    "AwayTeam": str(away),
                    "FTHG": int(hg),
                    "FTAG": int(ag),
                    "Season": str(start_year),
                    "competition": league.key,
                    "history_source": "football-data.org",
                })

            if rows:
                frames.append(pd.DataFrame(rows))

        if not frames:
            detail = " | ".join(failures[-3:]) if failures else "no matches returned"
            raise RuntimeError(
                f"No completed {league.name} history available from "
                f"football-data.org ({detail})"
            )

        df = pd.concat(frames, ignore_index=True, sort=False)
        df = (
            df.drop_duplicates(
                subset=["Date", "HomeTeam", "AwayTeam", "FTHG", "FTAG"]
            )
            .sort_values("Date")
            .reset_index(drop=True)
        )

        if len(df) < 30:
            raise RuntimeError(
                f"Only {len(df)} completed {league.name} matches are accessible. "
                "At least 30 are required for Dixon-Coles training. Increase "
                "--seasons-back or use a football-data.org plan with more history."
            )
        return df


# ---------------------------------------------------------------------------
# Analytic Dixon-Coles negative log-likelihood gradient
# ---------------------------------------------------------------------------

def dixon_coles_loss_and_gradient(
    params: np.ndarray,
    home_idx: np.ndarray,
    away_idx: np.ndarray,
    home_goals: np.ndarray,
    away_goals: np.ndarray,
    weights: np.ndarray,
    n_teams: int,
    l2: float,
) -> Tuple[float, np.ndarray]:
    """
    Return the weighted Dixon-Coles negative log-likelihood and exact gradient.

    An analytic Jacobian avoids the (2 * number_of_teams) finite-difference
    evaluations per L-BFGS-B step that caused MAXFUN warnings in UCL.
    The final team's attack/defence are minus the other teams' sum, so
    gradients use the chain rule for these identifiability constraints.
    """
    free = n_teams - 1
    attack = np.r_[params[:free], -np.sum(params[:free])]
    weakness = np.r_[params[free:2 * free], -np.sum(params[free:2 * free])]
    base, home_adv, rho = (float(x) for x in params[-3:])

    log_lam = base + home_adv + attack[home_idx] + weakness[away_idx]
    log_mu = base + attack[away_idx] + weakness[home_idx]
    lam = np.exp(log_lam)
    mu = np.exp(log_mu)

    tau = np.ones_like(lam)
    dloglam_tau = np.zeros_like(lam)
    dlogmu_tau = np.zeros_like(lam)
    drho_tau = np.zeros_like(lam)

    m00 = (home_goals == 0) & (away_goals == 0)
    m01 = (home_goals == 0) & (away_goals == 1)
    m10 = (home_goals == 1) & (away_goals == 0)
    m11 = (home_goals == 1) & (away_goals == 1)

    lm = lam[m00] * mu[m00]
    tau[m00] = 1.0 - lm * rho
    dloglam_tau[m00] = -lm * rho
    dlogmu_tau[m00] = -lm * rho
    drho_tau[m00] = -lm

    tau[m01] = 1.0 + lam[m01] * rho
    dloglam_tau[m01] = lam[m01] * rho
    drho_tau[m01] = lam[m01]

    tau[m10] = 1.0 + mu[m10] * rho
    dlogmu_tau[m10] = mu[m10] * rho
    drho_tau[m10] = mu[m10]

    tau[m11] = 1.0 - rho
    drho_tau[m11] = -1.0

    # Invalid Dixon-Coles factors are outside the likelihood domain.
    if (
        np.any(tau <= 0)
        or not np.all(np.isfinite(tau))
        or not np.all(np.isfinite(lam))
        or not np.all(np.isfinite(mu))
    ):
        return 1e12, np.zeros_like(params)

    ll = (
        home_goals * log_lam - lam - gammaln(home_goals + 1.0)
        + away_goals * log_mu - mu - gammaln(away_goals + 1.0)
        + np.log(tau)
    )
    penalty = l2 * (float(attack @ attack) + float(weakness @ weakness))
    loss = -float(weights @ ll) + penalty

    # Per-match derivatives of the weighted log likelihood.
    qlam = weights * (home_goals - lam + dloglam_tau / tau)
    qmu = weights * (away_goals - mu + dlogmu_tau / tau)

    # Attack participates in lambda as home team and mu as away team.
    attack_grad = -(
        np.bincount(home_idx, weights=qlam, minlength=n_teams)
        + np.bincount(away_idx, weights=qmu, minlength=n_teams)
    ) + 2.0 * l2 * attack

    # Defence weakness participates in lambda as away, mu as home.
    weakness_grad = -(
        np.bincount(away_idx, weights=qlam, minlength=n_teams)
        + np.bincount(home_idx, weights=qmu, minlength=n_teams)
    ) + 2.0 * l2 * weakness

    gradient = np.empty_like(params)
    gradient[:free] = attack_grad[:free] - attack_grad[-1]
    gradient[free:2 * free] = weakness_grad[:free] - weakness_grad[-1]
    gradient[-3] = -float(np.sum(qlam + qmu))
    gradient[-2] = -float(np.sum(qlam))
    gradient[-1] = -float(weights @ (drho_tau / tau))
    return loss, gradient


# ---------------------------------------------------------------------------
# Dixon-Coles model
# ---------------------------------------------------------------------------

class DixonColesModel:
    """
    Recency-weighted Dixon-Coles model.

    log(lambda_home) = base + home_adv + attack_home + weakness_away
    log(lambda_away) = base            + attack_away + weakness_home

    attack and defensive-weakness parameters each sum to zero for identifiability.
    """

    def __init__(
        self,
        half_life_days: float = 240.0,
        l2: float = 0.08,
        max_goals: int = 10,
    ):
        if half_life_days <= 0:
            raise ValueError("half_life_days must be > 0")
        if max_goals < 5:
            raise ValueError("max_goals should be >= 5")

        self.half_life_days = float(half_life_days)
        self.l2 = float(l2)
        self.max_goals = int(max_goals)

        self.teams: List[str] = []
        self.team_to_idx: Dict[str, int] = {}
        self.attack: Optional[np.ndarray] = None
        self.weakness: Optional[np.ndarray] = None
        self.base: Optional[float] = None
        self.home_adv: Optional[float] = None
        self.rho: Optional[float] = None
        self.fit_result = None
        self.training_matches = 0
        self.training_end: Optional[pd.Timestamp] = None

    def _unpack(self, params: np.ndarray) -> Tuple[np.ndarray, np.ndarray, float, float, float]:
        n = len(self.teams)
        a_free = params[: n - 1]
        d_free = params[n - 1 : 2 * n - 2]
        attack = np.r_[a_free, -a_free.sum()]
        weakness = np.r_[d_free, -d_free.sum()]
        base, home_adv, rho = params[-3:]
        return attack, weakness, float(base), float(home_adv), float(rho)

    @staticmethod
    def _tau_vector(
        hg: np.ndarray,
        ag: np.ndarray,
        lam: np.ndarray,
        mu: np.ndarray,
        rho: float,
    ) -> np.ndarray:
        tau = np.ones_like(lam, dtype=float)
        m00 = (hg == 0) & (ag == 0)
        m01 = (hg == 0) & (ag == 1)
        m10 = (hg == 1) & (ag == 0)
        m11 = (hg == 1) & (ag == 1)

        tau[m00] = 1.0 - lam[m00] * mu[m00] * rho
        tau[m01] = 1.0 + lam[m01] * rho
        tau[m10] = 1.0 + mu[m10] * rho
        tau[m11] = 1.0 - rho
        return tau

    @staticmethod
    def _tau_scalar(hg: int, ag: int, lam: float, mu: float, rho: float) -> float:
        if hg == 0 and ag == 0:
            return 1.0 - lam * mu * rho
        if hg == 0 and ag == 1:
            return 1.0 + lam * rho
        if hg == 1 and ag == 0:
            return 1.0 + mu * rho
        if hg == 1 and ag == 1:
            return 1.0 - rho
        return 1.0

    def fit(
        self,
        matches: pd.DataFrame,
        as_of: Optional[pd.Timestamp] = None,
    ) -> "DixonColesModel":
        required = {"Date", "HomeTeam", "AwayTeam", "FTHG", "FTAG"}
        missing = required.difference(matches.columns)
        if missing:
            raise ValueError(f"Training data missing {sorted(missing)}")

        df = matches.dropna(subset=list(required)).copy()
        if len(df) < 30:
            raise ValueError(f"Need at least 30 completed matches; got {len(df)}")

        self.teams = sorted(set(df["HomeTeam"]) | set(df["AwayTeam"]))
        self.team_to_idx = {team: i for i, team in enumerate(self.teams)}
        n = len(self.teams)
        if n < 2:
            raise ValueError("Need at least two teams")

        hi = df["HomeTeam"].map(self.team_to_idx).to_numpy(dtype=int)
        ai = df["AwayTeam"].map(self.team_to_idx).to_numpy(dtype=int)
        hg = df["FTHG"].to_numpy(dtype=float)
        ag = df["FTAG"].to_numpy(dtype=float)

        dates = pd.to_datetime(df["Date"])
        latest = dates.max()
        # During rolling-origin validation, anchor recency at prediction time.
        # With as_of=None, retain the original training behavior.
        reference = latest if as_of is None else pd.Timestamp(as_of)
        if reference.tzinfo is not None:
            reference = reference.tz_convert("UTC").tz_localize(None)
        if reference < latest:
            raise ValueError("as_of must not precede the last training match")
        age_days = (reference - dates).dt.total_seconds().to_numpy() / 86400.0
        weights = np.exp(-math.log(2.0) * age_days / self.half_life_days)

        home_mean = max(float(hg.mean()), 0.2)
        away_mean = max(float(ag.mean()), 0.2)
        base0 = math.log(away_mean)
        home_adv0 = math.log(home_mean / away_mean)

        # 2*(n-1) team params + base + home_adv + rho
        x0 = np.zeros(2 * (n - 1) + 3, dtype=float)
        x0[-3] = np.clip(base0, -1.0, 1.0)
        x0[-2] = np.clip(home_adv0, -0.5, 0.5)
        x0[-1] = -0.05

        def objective(params: np.ndarray) -> Tuple[float, np.ndarray]:
            return dixon_coles_loss_and_gradient(
                params,
                hi,
                ai,
                hg,
                ag,
                weights,
                n,
                self.l2,
            )

        team_bounds = [(-1.75, 1.75)] * (2 * (n - 1))
        bounds = team_bounds + [
            (-1.5, 1.5),   # base
            (-0.8, 0.8),   # home advantage
            (-0.20, 0.05), # rho; conservative upper bound keeps tau stable
        ]

        result = minimize(
            objective,
            x0,
            method="L-BFGS-B",
            jac=True,
            bounds=bounds,
            options={
                "maxiter": 3000,
                "maxfun": 30000,
                "ftol": 1e-9,
                "gtol": 1e-6,
                "maxls": 50,
            },
        )

        if not result.success:
            # Retry at the best point so an exhausted line search or a rare
            # evaluation limit does not silently feed unconverged models into
            # hyperparameter selection and match predictions.
            retry = minimize(
                objective,
                result.x,
                method="L-BFGS-B",
                jac=True,
                bounds=bounds,
                options={
                    "maxiter": 3000,
                    "maxfun": 30000,
                    "ftol": 1e-8,
                    "gtol": 1e-5,
                    "maxls": 50,
                },
            )
            if retry.success or (
                np.isfinite(retry.fun)
                and np.isfinite(result.fun)
                and retry.fun < result.fun
            ):
                result = retry

        if not result.success or not np.isfinite(result.fun) or result.fun >= 1e11:
            raise RuntimeError(
                "Dixon-Coles optimizer did not converge: "
                f"{result.message} (evaluations={result.nfev}). "
                "No prediction or tuning result will be accepted from this fit."
            )

        attack, weakness, base, home_adv, rho = self._unpack(result.x)
        self.attack = attack
        self.weakness = weakness
        self.base = base
        self.home_adv = home_adv
        self.rho = rho
        self.fit_result = result
        self.training_matches = len(df)
        self.training_end = latest
        return self

    def _check_fitted(self) -> None:
        if (
            self.attack is None
            or self.weakness is None
            or self.base is None
            or self.home_adv is None
            or self.rho is None
        ):
            raise RuntimeError("Model is not fitted")

    def resolve_team(self, raw_name: str, min_score: float = 72.0) -> Tuple[Optional[str], float]:
        """Resolve source name to training name. Returns (team, confidence_score)."""
        self._check_fitted()

        if raw_name in self.team_to_idx:
            return raw_name, 100.0

        normalized_raw = canonical_team_key(raw_name)

        explicit = TEAM_ALIASES.get(normalize_team_name(raw_name))
        if explicit in self.team_to_idx:
            return explicit, 100.0

        # Use the same canonical cross-provider key used by fixture/odds matching.
        # This is especially important for UCL names such as PSG, Inter and Bayern.
        normalized_to_original = {
            canonical_team_key(team): team
            for team in self.teams
        }

        if normalized_raw in normalized_to_original:
            return normalized_to_original[normalized_raw], 100.0

        match = process.extractOne(
            normalized_raw,
            list(normalized_to_original.keys()),
            scorer=fuzz.WRatio,
        )
        if not match:
            return None, 0.0

        candidate_norm, score, _ = match
        if score < min_score:
            return None, float(score)
        return normalized_to_original[candidate_norm], float(score)

    def expected_goals(self, home_raw: str, away_raw: str) -> Dict[str, object]:
        self._check_fitted()
        assert self.attack is not None
        assert self.weakness is not None
        assert self.base is not None
        assert self.home_adv is not None

        home, home_match_score = self.resolve_team(home_raw)
        away, away_match_score = self.resolve_team(away_raw)

        # Unknown teams fall back to league-average strength (0 attack/weakness).
        # This avoids hard failure in early-season/promoted-team edge cases,
        # while explicitly lowering matching confidence in output.
        if home is None:
            h_attack = 0.0
            h_weak = 0.0
            home_model_name = "__LEAGUE_AVERAGE__"
        else:
            idx = self.team_to_idx[home]
            h_attack = float(self.attack[idx])
            h_weak = float(self.weakness[idx])
            home_model_name = home

        if away is None:
            a_attack = 0.0
            a_weak = 0.0
            away_model_name = "__LEAGUE_AVERAGE__"
        else:
            idx = self.team_to_idx[away]
            a_attack = float(self.attack[idx])
            a_weak = float(self.weakness[idx])
            away_model_name = away

        lam = math.exp(self.base + self.home_adv + h_attack + a_weak)
        mu = math.exp(self.base + a_attack + h_weak)

        return {
            "lambda_home": lam,
            "lambda_away": mu,
            "model_home_team": home_model_name,
            "model_away_team": away_model_name,
            "home_name_match_score": home_match_score,
            "away_name_match_score": away_match_score,
        }

    def score_matrix(self, home: str, away: str) -> Tuple[np.ndarray, Dict[str, object]]:
        self._check_fitted()
        assert self.rho is not None

        meta = self.expected_goals(home, away)
        lam = float(meta["lambda_home"])
        mu = float(meta["lambda_away"])

        g = np.arange(self.max_goals + 1)
        matrix = np.outer(poisson.pmf(g, lam), poisson.pmf(g, mu))

        # Dixon-Coles adjustment affects only 0-0, 0-1, 1-0, 1-1.
        for hg, ag in ((0, 0), (0, 1), (1, 0), (1, 1)):
            matrix[hg, ag] *= self._tau_scalar(hg, ag, lam, mu, self.rho)

        total = float(matrix.sum())
        if total <= 0 or not math.isfinite(total):
            raise RuntimeError("Invalid score probability matrix")

        # max_goals truncates tiny tails. Renormalize to exact probability mass 1.
        matrix /= total
        return matrix, meta

    @staticmethod
    def one_x_two(matrix: np.ndarray) -> Dict[str, float]:
        home = float(np.tril(matrix, k=-1).sum())  # row(home goals) > col(away goals)
        draw = float(np.trace(matrix))
        away = float(np.triu(matrix, k=1).sum())
        return {"home": home, "draw": draw, "away": away}

    @staticmethod
    def over_under(matrix: np.ndarray, line: float) -> Dict[str, float]:
        """
        Full-time total goals.
        Half-lines have no push.
        Integer lines return explicit push probability.
        Quarter-lines are intentionally rejected because settlement is split
        across adjacent half/integer lines and should be represented separately.
        """
        q = round(line * 4)
        if not math.isclose(line * 4, q, abs_tol=1e-9):
            raise ValueError("Goal line must be in 0.25 increments")
        if q % 2 == 1:
            raise ValueError(
                "Quarter goal lines should be split into their component lines "
                "(e.g. 2.25 = half 2.0 + half 2.5)."
            )

        totals = np.add.outer(np.arange(matrix.shape[0]), np.arange(matrix.shape[1]))

        if math.isclose(line, round(line)):
            target = int(round(line))
            p_under = float(matrix[totals < target].sum())
            p_push = float(matrix[totals == target].sum())
            p_over = float(matrix[totals > target].sum())
        else:
            cutoff = math.floor(line)
            p_under = float(matrix[totals <= cutoff].sum())
            p_push = 0.0
            p_over = float(matrix[totals > cutoff].sum())

        return {"over": p_over, "push": p_push, "under": p_under}

    @staticmethod
    def scoreline_dict(matrix: np.ndarray) -> Dict[str, float]:
        return {
            f"{h}-{a}": float(matrix[h, a])
            for h in range(matrix.shape[0])
            for a in range(matrix.shape[1])
        }

    @staticmethod
    def top_scorelines(matrix: np.ndarray, n: int = 8) -> List[Tuple[str, float]]:
        flat = np.argsort(matrix.ravel())[::-1][:n]
        out = []
        for idx in flat:
            h, a = np.unravel_index(idx, matrix.shape)
            out.append((f"{h}-{a}", float(matrix[h, a])))
        return out

    def predict(
        self,
        home: str,
        away: str,
        total_lines: Sequence[float] = DEFAULT_TOTAL_LINES,
        top_n_scorelines: int = 8,
    ) -> Dict[str, object]:
        matrix, meta = self.score_matrix(home, away)
        x12 = self.one_x_two(matrix)

        result: Dict[str, object] = dict(meta)
        result.update({
            "p_home": x12["home"],
            "p_draw": x12["draw"],
            "p_away": x12["away"],
            "fair_home": fair_odds(x12["home"]),
            "fair_draw": fair_odds(x12["draw"]),
            "fair_away": fair_odds(x12["away"]),
            "predicted_1x2": max(x12, key=x12.get),
            "top_scorelines": self.top_scorelines(matrix, n=top_n_scorelines),
            "scoreline_distribution": self.scoreline_dict(matrix),
        })

        for line in total_lines:
            ou = self.over_under(matrix, float(line))
            label = str(line).replace(".", "_")
            result[f"p_over_{label}"] = ou["over"]
            result[f"p_under_{label}"] = ou["under"]
            if ou["push"] > 0:
                result[f"p_push_{label}"] = ou["push"]
            result[f"fair_over_{label}"] = fair_odds(ou["over"])
            result[f"fair_under_{label}"] = fair_odds(ou["under"])

        return result


# ---------------------------------------------------------------------------
# Market odds extraction
# ---------------------------------------------------------------------------

def _first_valid_from_row(row: pd.Series, columns: Sequence[str]) -> Optional[float]:
    for col in columns:
        if col in row.index:
            x = safe_float(row[col])
            if x is not None and x > 1.0:
                return x
    return None


def extract_market_odds(row: pd.Series) -> Dict[str, Optional[float]]:
    """
    Prefer market maxima where available, then averages, then major books.
    For value screening this intentionally uses the best readily published price.
    """
    return {
        "market_home_odds": _first_valid_from_row(
            row, ("MaxH", "AvgH", "B365H", "PSH", "WHH", "BWH", "IWH")
        ),
        "market_draw_odds": _first_valid_from_row(
            row, ("MaxD", "AvgD", "B365D", "PSD", "WHD", "BWD", "IWD")
        ),
        "market_away_odds": _first_valid_from_row(
            row, ("MaxA", "AvgA", "B365A", "PSA", "WHA", "BWA", "IWA")
        ),
        "market_over_2_5_odds": _first_valid_from_row(
            row, ("Max>2.5", "Avg>2.5", "B365>2.5", "P>2.5")
        ),
        "market_under_2_5_odds": _first_valid_from_row(
            row, ("Max<2.5", "Avg<2.5", "B365<2.5", "P<2.5")
        ),
    }


def add_market_value_metrics(pred: Dict[str, object], row: pd.Series) -> None:
    odds = extract_market_odds(row)
    pred.update(odds)

    h, d, a = (
        odds["market_home_odds"],
        odds["market_draw_odds"],
        odds["market_away_odds"],
    )
    mh, md, ma = devig_decimal((h, d, a))
    pred["market_p_home"] = mh
    pred["market_p_draw"] = md
    pred["market_p_away"] = ma

    for side, mp in (("home", mh), ("draw", md), ("away", ma)):
        model_p = float(pred[f"p_{side}"])
        pred[f"edge_{side}"] = None if mp is None else model_p - mp
        pred[f"ev_{side}"] = ev_decimal(model_p, odds[f"market_{side}_odds"])

    over_odds = odds["market_over_2_5_odds"]
    under_odds = odds["market_under_2_5_odds"]
    mo, mu = devig_decimal((over_odds, under_odds))
    pred["market_p_over_2_5"] = mo
    pred["market_p_under_2_5"] = mu

    p_over = float(pred["p_over_2_5"])
    p_under = float(pred["p_under_2_5"])
    pred["edge_over_2_5"] = None if mo is None else p_over - mo
    pred["edge_under_2_5"] = None if mu is None else p_under - mu
    pred["ev_over_2_5"] = ev_decimal(p_over, over_odds)
    pred["ev_under_2_5"] = ev_decimal(p_under, under_odds)


# ---------------------------------------------------------------------------
# Pipeline
# ---------------------------------------------------------------------------

class FootballValuePipeline:
    def __init__(
        self,
        cache_dir: str | Path = ".football_cache",
        seasons_back: int = 3,
        half_life_days: float = 240.0,
        l2: float = 0.08,
        max_goals: int = 10,
        lookahead_days: int = 10,
        force_refresh: bool = False,
    ):
        self.source = FootballDataUK(cache_dir=cache_dir, force_refresh=force_refresh)
        self.seasons_back = int(seasons_back)
        self.half_life_days = float(half_life_days)
        self.l2 = float(l2)
        self.max_goals = int(max_goals)
        self.lookahead_days = int(lookahead_days)

    def _training_health(self, league, model, now):
        end = None if model.training_end is None else str(model.training_end.date())
        if league.key == "UCL":
            from ucl_training import health
            data = health(self.source.http.cache_dir.resolve().parent, end, now, cache_dir=self.source.http.cache_dir)
            data["last_refresh_error"] = getattr(self.football_data_org, "ucl_refresh_error", None)
            data["last_refresh_error_reason"] = getattr(self.football_data_org, "ucl_refresh_error_reason", None)
            if data["last_refresh_error"]:
                data["status"] = "LIVE_REFRESH_FAILED_USING_CACHE"
            return data
        return {"training_end": end, "days_since_latest_result":
                (now.date()-model.training_end.date()).days if model.training_end is not None else None,
                "status": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED"}

    def run_league(
        self,
        league_key: str,
        now: Optional[datetime] = None,
    ) -> Tuple[pd.DataFrame, Dict[str, object], Dict[str, Dict[str, float]]]:
        if league_key not in LEAGUES:
            raise KeyError(f"Unknown league {league_key!r}. Choose from {list(LEAGUES)}")

        league = LEAGUES[league_key]
        now = now or datetime.now(timezone.utc)

        history = self.source.history(
            league,
            seasons_back=self.seasons_back,
            now=now,
        )
        fixtures = self.source.fixtures(
            league,
            lookahead_days=self.lookahead_days,
            now=now,
        )

        model = DixonColesModel(
            half_life_days=self.half_life_days,
            l2=self.l2,
            max_goals=self.max_goals,
        ).fit(history)

        diagnostics = {
            "league": league.name,
            "training_matches": model.training_matches,
            "training_end": None if model.training_end is None else str(model.training_end.date()),
            "fit_success": bool(model.fit_result.success) if model.fit_result is not None else False,
            "objective": (
                float(model.fit_result.fun) if model.fit_result is not None else None
            ),
            "base": model.base,
            "home_adv": model.home_adv,
            "rho": model.rho,
            "half_life_days": model.half_life_days,
            "max_goals": model.max_goals,
        }

        if fixtures.empty:
            return pd.DataFrame(), diagnostics, {}

        records = []
        scoreline_payload: Dict[str, Dict[str, float]] = {}

        for _, row in fixtures.iterrows():
            home = str(row["HomeTeam"])
            away = str(row["AwayTeam"])

            pred = model.predict(home, away)
            add_market_value_metrics(pred, row)

            score_dist = pred.pop("scoreline_distribution")
            top_scores = pred["top_scorelines"]

            match_id = f"{row['Date'].date()}__{home}__{away}"
            scoreline_payload[match_id] = score_dist  # type: ignore[assignment]

            record = {
                "league": league.name,
                "date": row["Date"].date().isoformat(),
                "home_team": home,
                "away_team": away,
                "fixture_source": row.get("fixture_source", "unknown"),
                **pred,
            }
            record["top_scorelines"] = json.dumps(
                [{"score": s, "p": round(p, 8)} for s, p in top_scores],
                separators=(",", ":"),
            )
            records.append(record)

        out = pd.DataFrame(records)

        # Stable, integration-friendly column order for the core metrics.
        preferred = [
            "league", "date", "home_team", "away_team",
            "lambda_home", "lambda_away",
            "p_home", "p_draw", "p_away",
            "fair_home", "fair_draw", "fair_away",
            "predicted_1x2",
            "p_over_0_5", "p_under_0_5",
            "p_over_1_5", "p_under_1_5",
            "p_over_2_5", "p_under_2_5",
            "p_over_3_5", "p_under_3_5",
            "p_over_4_5", "p_under_4_5",
            "top_scorelines",
            "market_home_odds", "market_draw_odds", "market_away_odds",
            "market_p_home", "market_p_draw", "market_p_away",
            "edge_home", "edge_draw", "edge_away",
            "ev_home", "ev_draw", "ev_away",
            "market_over_2_5_odds", "market_under_2_5_odds",
            "market_p_over_2_5", "market_p_under_2_5",
            "edge_over_2_5", "edge_under_2_5",
            "ev_over_2_5", "ev_under_2_5",
            "model_home_team", "model_away_team",
            "home_name_match_score", "away_name_match_score",
        ]
        ordered = [c for c in preferred if c in out.columns]
        remaining = [c for c in out.columns if c not in ordered]
        out = out[ordered + remaining]
        return out, diagnostics, scoreline_payload

    def run(
        self,
        league_keys: Sequence[str],
        now: Optional[datetime] = None,
    ) -> Dict[str, Tuple[pd.DataFrame, Dict[str, object], Dict[str, Dict[str, float]]]]:
        return {key: self.run_league(key, now=now) for key in league_keys}


# ---------------------------------------------------------------------------
# Self-test
# ---------------------------------------------------------------------------

def self_test() -> None:
    model = DixonColesModel(max_goals=10)
    model.teams = ["A", "B"]
    model.team_to_idx = {"A": 0, "B": 1}
    model.attack = np.array([0.15, -0.15])
    model.weakness = np.array([-0.05, 0.05])
    model.base = math.log(1.20)
    model.home_adv = math.log(1.18)
    model.rho = -0.08

    matrix, _ = model.score_matrix("A", "B")
    assert abs(float(matrix.sum()) - 1.0) < 1e-12

    x12 = model.one_x_two(matrix)
    assert abs(sum(x12.values()) - 1.0) < 1e-12

    for line in DEFAULT_TOTAL_LINES:
        ou = model.over_under(matrix, line)
        assert abs(ou["over"] + ou["under"] + ou["push"] - 1.0) < 1e-12

    p = model.predict("A", "B")
    assert 0.0 < float(p["p_home"]) < 1.0
    assert 0.0 < float(p["p_over_0_5"]) < 1.0
    assert abs(float(p["p_over_4_5"]) + float(p["p_under_4_5"]) - 1.0) < 1e-12

    market = devig_decimal([2.0, 3.5, 4.0])
    assert all(x is not None for x in market)
    assert abs(sum(x for x in market if x is not None) - 1.0) < 1e-12

    print("Self-test passed.")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="Dixon-Coles football value pipeline for major European leagues."
    )
    p.add_argument(
        "--leagues",
        nargs="+",
        choices=list(LEAGUES),
        default=["EPL"],
        help="Leagues to process.",
    )
    p.add_argument("--seasons-back", type=int, default=3)
    p.add_argument("--half-life-days", type=float, default=240.0)
    p.add_argument("--reliability-experiment", action="store_true",
                   help="Compare stronger L2 and fixed half-life fits prospectively; no production changes or extra odds requests.")
    p.add_argument("--l2", type=float, default=0.08)
    p.add_argument("--max-goals", type=int, default=10)
    p.add_argument("--lookahead-days", type=int, default=10)
    p.add_argument("--cache-dir", default=".football_cache")
    p.add_argument("--out-dir", default="football_output")
    p.add_argument("--force-refresh", action="store_true")
    p.add_argument("--self-test", action="store_true")
    return p


def main(argv: Optional[Sequence[str]] = None) -> int:
    args = build_parser().parse_args(argv)

    if args.self_test:
        import quote_policy
        from unittest.mock import patch
        with patch.object(quote_policy, 'CONFIG', Path(__file__).resolve().parent / 'tests' / 'offline_quote_policy.json'):
            self_test()
        return 0

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    pipeline = FootballValuePipeline(
        cache_dir=args.cache_dir,
        seasons_back=args.seasons_back,
        half_life_days=args.half_life_days,
        l2=args.l2,
        max_goals=args.max_goals,
        lookahead_days=args.lookahead_days,
        force_refresh=args.force_refresh,
    )

    all_frames = []

    for league_key in args.leagues:
        print(f"[{league_key}] fetching data + fitting model...", file=sys.stderr)
        predictions, diagnostics, scorelines = pipeline.run_league(league_key)

        pred_path = out_dir / f"{league_key}_predictions.csv"
        diag_path = out_dir / f"{league_key}_diagnostics.json"
        score_path = out_dir / f"{league_key}_scorelines.json"

        predictions.to_csv(pred_path, index=False)
        diag_path.write_text(json.dumps(diagnostics, indent=2), encoding="utf-8")
        score_path.write_text(json.dumps(scorelines, indent=2), encoding="utf-8")

        print(
            f"[{league_key}] {len(predictions)} fixtures -> {pred_path}",
            file=sys.stderr,
        )
        if not predictions.empty:
            all_frames.append(predictions)

    if all_frames:
        combined = pd.concat(all_frames, ignore_index=True, sort=False)
        combined_path = out_dir / "all_leagues_predictions.csv"
        combined.to_csv(combined_path, index=False)
        print(f"Combined -> {combined_path}", file=sys.stderr)

    return 0



# ---------------------------------------------------------------------------
# Odds selection and margin removal
# ---------------------------------------------------------------------------

# Probability benchmark: all three prices come from one source.
OPEN_1X2_TRIPLES = (
    ("PSH", "PSD", "PSA"),
    ("B365H", "B365D", "B365A"),
    ("AvgH", "AvgD", "AvgA"),
    ("WHH", "WHD", "WHA"),
    ("BWH", "BWD", "BWA"),
    ("IWH", "IWD", "IWA"),
)

CLOSE_1X2_TRIPLES = (
    ("PSCH", "PSCD", "PSCA"),
    ("B365CH", "B365CD", "B365CA"),
    ("AvgCH", "AvgCD", "AvgCA"),
)

OU25_PAIRS = (
    ("P>2.5", "P<2.5"),
    ("B365>2.5", "B365<2.5"),
    ("Avg>2.5", "Avg<2.5"),
)

BEST_1X2_COLUMNS = {
    "home": ("MaxH", "PSH", "B365H", "AvgH", "WHH", "BWH", "IWH"),
    "draw": ("MaxD", "PSD", "B365D", "AvgD", "WHD", "BWD", "IWD"),
    "away": ("MaxA", "PSA", "B365A", "AvgA", "WHA", "BWA", "IWA"),
}

BEST_OU25_COLUMNS = {
    "over": ("Max>2.5", "P>2.5", "B365>2.5", "Avg>2.5"),
    "under": ("Max<2.5", "P<2.5", "B365<2.5", "Avg<2.5"),
}


def _valid_price(x) -> Optional[float]:
    x = safe_float(x)
    return x if x is not None and x > 1.0 else None


def pick_consistent_market(
    row: pd.Series,
    candidates: Sequence[Sequence[str]],
) -> Tuple[List[Optional[float]], Optional[str]]:
    """Return the first complete odds set, never mixing books within a probability market."""
    for cols in candidates:
        if all(c in row.index for c in cols):
            vals = [_valid_price(row[c]) for c in cols]
            if all(v is not None for v in vals):
                source = str(cols[0]).rstrip("HDA")
                return vals, source
    return [None] * len(candidates[0]), None


def pick_best_price(row: pd.Series, columns: Sequence[str]) -> Optional[float]:
    for col in columns:
        if col in row.index:
            x = _valid_price(row[col])
            if x is not None:
                return x
    return None


def devig(odds: Sequence[Optional[float]], method: str = "power") -> List[Optional[float]]:
    """
    Convert decimal odds to fair probabilities.

    power:
      Solve sum(q_i ** k) = 1 where q_i = 1/odds_i.
      This is generally preferable to proportional normalization for 1X2 because
      it can partially accommodate favourite/longshot bias.

    proportional:
      q_i / sum(q)
    """
    if not odds or any(o is None or o <= 1.0 for o in odds):
        return [None for _ in odds]

    q = np.array([1.0 / float(o) for o in odds], dtype=float)

    if method == "proportional":
        return [float(x) for x in q / q.sum()]

    if method != "power":
        raise ValueError("devig method must be 'power' or 'proportional'")

    # sum(q**k) is monotonically decreasing for 0<q<1.
    lo, hi = 0.01, 10.0
    s_lo = float(np.power(q, lo).sum())
    s_hi = float(np.power(q, hi).sum())

    # Defensive fallback for malformed/very unusual markets.
    if not (s_lo >= 1.0 >= s_hi):
        return [float(x) for x in q / q.sum()]

    for _ in range(80):
        k = (lo + hi) / 2.0
        s = float(np.power(q, k).sum())
        if s > 1.0:
            lo = k
        else:
            hi = k

    fair = np.power(q, (lo + hi) / 2.0)
    fair /= fair.sum()
    return [float(x) for x in fair]


# ---------------------------------------------------------------------------
# Score-matrix consistency
# ---------------------------------------------------------------------------

def reweight_matrix_to_1x2(
    matrix: np.ndarray,
    target: Sequence[float],
) -> np.ndarray:
    """
    Reweight H/D/A regions to target probabilities while preserving the relative
    shape of scorelines inside each region.

    This is the key improvement over simply blending 1X2 after score modelling:
    every downstream market (O/U, scorelines, AH added later) remains derived
    from one internally consistent score matrix.
    """
    target_arr = np.asarray(target, dtype=float)
    if target_arr.shape != (3,) or np.any(target_arr < 0):
        raise ValueError("target must be [home, draw, away]")
    if not math.isclose(float(target_arr.sum()), 1.0, rel_tol=0, abs_tol=1e-8):
        target_arr = target_arr / target_arr.sum()

    n_h, n_a = matrix.shape
    h_idx = np.arange(n_h)[:, None]
    a_idx = np.arange(n_a)[None, :]
    masks = (h_idx > a_idx, h_idx == a_idx, h_idx < a_idx)

    out = matrix.copy().astype(float)
    current = np.array([float(matrix[m].sum()) for m in masks])

    if np.any(current <= 0):
        return matrix.copy()

    for mask, cur, tgt in zip(masks, current, target_arr):
        out[mask] *= float(tgt / cur)

    out /= out.sum()
    return out


def prediction_from_matrix(
    model: DixonColesModel,
    matrix: np.ndarray,
    meta: Dict[str, object],
    total_lines: Sequence[float] = DEFAULT_TOTAL_LINES,
    top_n_scorelines: int = 20,
) -> Dict[str, object]:
    x12 = model.one_x_two(matrix)
    result: Dict[str, object] = dict(meta)
    result.update({
        "p_home": x12["home"],
        "p_draw": x12["draw"],
        "p_away": x12["away"],
        "fair_home": fair_odds(x12["home"]),
        "fair_draw": fair_odds(x12["draw"]),
        "fair_away": fair_odds(x12["away"]),
        "predicted_1x2": max(x12, key=x12.get),
        "p_btts_yes": float(matrix[1:, 1:].sum()),
        "p_btts_no": float(1.0 - matrix[1:, 1:].sum()),
        "top_scorelines": model.top_scorelines(matrix, n=top_n_scorelines),
        # Persist only the highest-probability exact scores. The complete matrix
        # is still used above for 1X2 and totals calculations, but the low-
        # probability tail is intentionally discarded from serialized outputs.
        "scoreline_distribution": dict(
            model.top_scorelines(matrix, n=top_n_scorelines)
        ),
    })

    for line in total_lines:
        ou = model.over_under(matrix, float(line))
        label = str(line).replace(".", "_")
        result[f"p_over_{label}"] = ou["over"]
        result[f"p_under_{label}"] = ou["under"]
        if ou["push"] > 0:
            result[f"p_push_{label}"] = ou["push"]
        result[f"fair_over_{label}"] = fair_odds(ou["over"])
        result[f"fair_under_{label}"] = fair_odds(ou["under"])
    return result


def market_snapshot(row: pd.Series, devig_method: str = "power") -> Dict[str, object]:
    """Build a market snapshot, preferring dedicated live odds when present."""
    live_ref = [
        _valid_price(row.get("live_ref_home_odds")),
        _valid_price(row.get("live_ref_draw_odds")),
        _valid_price(row.get("live_ref_away_odds")),
    ]
    if all(v is not None for v in live_ref):
        coherent = live_ref
        bookmaker = row.get("live_ref_1x2_bookmaker")
        source = f"The Odds API / {bookmaker}" if bookmaker else "The Odds API"
        best_h = _valid_price(row.get("live_best_home_odds"))
        best_d = _valid_price(row.get("live_best_draw_odds"))
        best_a = _valid_price(row.get("live_best_away_odds"))
    else:
        coherent, source = pick_consistent_market(row, OPEN_1X2_TRIPLES)
        best_h = pick_best_price(row, BEST_1X2_COLUMNS["home"])
        best_d = pick_best_price(row, BEST_1X2_COLUMNS["draw"])
        best_a = pick_best_price(row, BEST_1X2_COLUMNS["away"])

    fair = devig(coherent, method=devig_method)

    live_ou = [
        _valid_price(row.get("live_ref_over_2_5_odds")),
        _valid_price(row.get("live_ref_under_2_5_odds")),
    ]
    if all(v is not None for v in live_ou):
        ou_odds = live_ou
        bookmaker = row.get("live_ref_ou25_bookmaker")
        ou_source = f"The Odds API / {bookmaker}" if bookmaker else "The Odds API"
        best_over = _valid_price(row.get("live_best_over_2_5_odds"))
        best_under = _valid_price(row.get("live_best_under_2_5_odds"))
    else:
        ou_odds, ou_source = pick_consistent_market(row, OU25_PAIRS)
        best_over = pick_best_price(row, BEST_OU25_COLUMNS["over"])
        best_under = pick_best_price(row, BEST_OU25_COLUMNS["under"])

    ou_fair = devig(ou_odds, method=devig_method)

    return {
        "market_source_1x2": source,
        "market_home_odds": best_h,
        "market_draw_odds": best_d,
        "market_away_odds": best_a,
        "market_reference_home_odds": coherent[0],
        "market_reference_draw_odds": coherent[1],
        "market_reference_away_odds": coherent[2],
        "market_p_home": fair[0],
        "market_p_draw": fair[1],
        "market_p_away": fair[2],
        "market_source_ou25": ou_source,
        "market_over_2_5_odds": best_over,
        "market_under_2_5_odds": best_under,
        "market_reference_over_2_5_odds": ou_odds[0],
        "market_reference_under_2_5_odds": ou_odds[1],
        "market_p_over_2_5": ou_fair[0],
        "market_p_under_2_5": ou_fair[1],
    }


def add_value_metrics(pred: Dict[str, object], snapshot: Dict[str, object]) -> None:
    pred.update(snapshot)

    for side in ("home", "draw", "away"):
        model_p = float(pred[f"p_{side}"])
        market_p = snapshot.get(f"market_p_{side}")
        odds = snapshot.get(f"market_{side}_odds")
        pred[f"edge_prob_{side}"] = (
            None if market_p is None else model_p - float(market_p)
        )
        pred[f"ev_{side}"] = ev_decimal(model_p, odds)  # type: ignore[arg-type]

    for side in ("over_2_5", "under_2_5"):
        model_p = float(pred[f"p_{side}"])
        market_p = snapshot.get(f"market_p_{side}")
        odds = snapshot.get(f"market_{side}_odds")
        pred[f"edge_prob_{side}"] = (
            None if market_p is None else model_p - float(market_p)
        )
        pred[f"ev_{side}"] = ev_decimal(model_p, odds)  # type: ignore[arg-type]


# ---------------------------------------------------------------------------
# Evaluation / staking utilities borrowed from the PL research workflow
# ---------------------------------------------------------------------------

def multiclass_log_loss(P: np.ndarray, y: np.ndarray) -> float:
    return float(-np.mean(np.log(np.clip(P[np.arange(len(y)), y], 1e-12, 1.0))))


def multiclass_brier(P: np.ndarray, y: np.ndarray) -> float:
    return float(np.mean(np.sum((P - np.eye(3)[y]) ** 2, axis=1)))


def accuracy(P: np.ndarray, y: np.ndarray) -> float:
    return float(np.mean(P.argmax(axis=1) == y))


def binary_brier(p: np.ndarray, y: np.ndarray) -> float:
    return float(np.mean((p - y) ** 2))


def reliability_table(P: np.ndarray, y: np.ndarray, bins: int = 10) -> pd.DataFrame:
    p = P.ravel()
    o = np.eye(3)[y].ravel()
    edges = np.linspace(0.0, 1.0, bins + 1)
    idx = np.clip(np.digitize(p, edges) - 1, 0, bins - 1)
    rows = []
    for b in range(bins):
        mask = idx == b
        if mask.any():
            rows.append({
                "bin_lo": edges[b],
                "bin_hi": edges[b + 1],
                "n": int(mask.sum()),
                "mean_pred": float(p[mask].mean()),
                "observed": float(o[mask].mean()),
            })
    return pd.DataFrame(rows)


def bootstrap_roi_ci(bets: pd.DataFrame, n: int = 5000, seed: int = 0) -> Tuple[float, float]:
    if bets.empty:
        return (math.nan, math.nan)
    unit_returns = np.where(bets["won"], bets["odds_taken"] - 1.0, -1.0)
    rng = np.random.default_rng(seed)
    means = rng.choice(unit_returns, size=(n, len(unit_returns)), replace=True).mean(axis=1)
    return float(np.percentile(means, 2.5)), float(np.percentile(means, 97.5))


def simulate_staking(
    bets: pd.DataFrame,
    bankroll0: float,
    mode: str,
    kelly_frac: float,
    max_stake_pct: float,
    flat_pct: float,
) -> pd.DataFrame:
    bets = bets.copy()
    bets["stake"] = 0.0
    bets["pnl"] = 0.0
    bankroll = float(bankroll0)

    if bets.empty:
        return bets

    for _, group in bets.groupby("date", sort=True):
        start = bankroll
        for i in group.index:
            p = float(bets.at[i, "model_prob"])
            o = float(bets.at[i, "odds_taken"])
            if mode == "kelly":
                full_kelly = max(0.0, (p * o - 1.0) / (o - 1.0))
                stake = start * min(kelly_frac * full_kelly, max_stake_pct)
            else:
                stake = bankroll0 * flat_pct
            stake = min(stake, bankroll)
            bets.at[i, "stake"] = stake
            bets.at[i, "pnl"] = stake * (o - 1.0) if bool(bets.at[i, "won"]) else -stake
        bankroll += float(bets.loc[group.index, "pnl"].sum())

    daily = bets.groupby("date")["pnl"].sum().cumsum() + bankroll0
    bets["bankroll_after"] = bets["date"].map(daily)
    return bets


def summarize_bets(bets: pd.DataFrame, bankroll0: float) -> Dict[str, object]:
    if bets.empty:
        return {"n_bets": 0}

    staked = float(bets["stake"].sum())
    equity = pd.concat([
        pd.Series([bankroll0]),
        bets.drop_duplicates("date")["bankroll_after"],
    ]).to_numpy(dtype=float)

    drawdown = float(np.max(1.0 - equity / np.maximum.accumulate(equity)))
    lo, hi = bootstrap_roi_ci(bets)

    return {
        "n_bets": int(len(bets)),
        "hit_rate": float(bets["won"].mean()),
        "avg_odds": float(bets["odds_taken"].mean()),
        "avg_ev_at_bet": float(bets["edge_ev"].mean()),
        "avg_clv": float(bets["clv"].dropna().mean()) if bets["clv"].notna().any() else None,
        "pct_positive_clv": (
            float((bets.loc[bets["clv"].notna(), "clv"] > 0).mean())
            if bets["clv"].notna().any()
            else None
        ),
        "roi_on_stake": float(bets["pnl"].sum() / staked) if staked else None,
        "flat_unit_roi": float(
            np.where(bets["won"], bets["odds_taken"] - 1.0, -1.0).mean()
        ),
        "flat_unit_roi_95ci": [lo, hi],
        "final_bankroll": float(equity[-1]),
        "max_drawdown": drawdown,
    }


def plot_reliability(curves: Dict[str, pd.DataFrame], path: Path) -> None:
    """Optional; pipeline still works without matplotlib."""
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except ImportError:
        return

    fig, ax = plt.subplots(figsize=(5.5, 5.5))
    ax.plot([0, 1], [0, 1], "k--", lw=1, label="perfect")
    for name, table in curves.items():
        if not table.empty:
            ax.plot(table["mean_pred"], table["observed"], marker="o", label=name)
    ax.set_xlabel("Predicted probability")
    ax.set_ylabel("Observed frequency")
    ax.set_title("1X2 reliability")
    ax.legend()
    fig.tight_layout()
    fig.savefig(path, dpi=130)
    plt.close(fig)


# ---------------------------------------------------------------------------
# V2 pipeline
# ---------------------------------------------------------------------------

class FootballValuePipelineV2(FootballValuePipeline):
    def __init__(
        self,
        *args,
        devig_method: str = "power",
        market_weight: float = 0.50,
        odds_api_key: Optional[str] = None,
        football_data_api_key: Optional[str] = None,
        odds_regions: str = "eu",
        fixture_provider: str = "auto",
        live_odds: bool = True,
        additional_odds_coverage: str = "all",
        **kwargs,
    ):
        cache_dir = kwargs.get("cache_dir", ".football_cache")
        force_refresh = bool(kwargs.get("force_refresh", False))
        super().__init__(*args, **kwargs)
        if devig_method not in {"power", "proportional"}:
            raise ValueError("devig_method must be power or proportional")
        if not 0.0 <= market_weight <= 1.0:
            raise ValueError("market_weight must be between 0 and 1")
        if fixture_provider not in {
            "auto", "the-odds-api", "football-data-org", "football-data-uk"
        }:
            raise ValueError("Unsupported fixture_provider")

        self.devig_method = devig_method
        self.market_weight = float(market_weight)
        self.odds_regions = str(odds_regions)
        self.fixture_provider = fixture_provider
        self.live_odds = bool(live_odds)
        if additional_odds_coverage not in {"all", "ranked"}:
            raise ValueError("additional_odds_coverage must be all or ranked")
        self.additional_odds_coverage = additional_odds_coverage
        # Per-event BTTS and alternate totals requests consume additional API credits.
        self.extra_event_odds_requests = 0
        self.max_extra_event_odds_requests = 24
        from goal_market_validation import distribute_event_odds_budget
        self.extra_event_odds_quota = distribute_event_odds_budget(
            ["EPL", "LaLiga", "Bundesliga", "SerieA", "Ligue1", "UCL"], 24
        )
        self.extra_event_odds_by_league = {
            key: 0 for key in self.extra_event_odds_quota
        }

        odds_api_key = odds_api_key or next(
            (value for name in TheOddsAPI.KEY_ENV_NAMES
             if (value := os.getenv(name, "").strip())),
            None,
        )
        football_data_api_key = (
            football_data_api_key or os.getenv("FOOTBALL_DATA_API_KEY")
        )
        self.odds_api = (
            TheOddsAPI(
                odds_api_key,
                cache_dir=cache_dir,
                force_refresh=force_refresh,
                regions=self.odds_regions,
            )
            if odds_api_key
            else None
        )
        self.football_data_org = (
            FootballDataOrg(
                football_data_api_key,
                cache_dir=cache_dir,
                force_refresh=force_refresh,
            )
            if football_data_api_key
            else None
        )

    def _history_for_league(
        self,
        league: LeagueConfig,
        now: datetime,
    ) -> pd.DataFrame:
        """
        Select a competition-appropriate training source.

        Domestic leagues use Football-Data.co.uk's long historical CSVs.
        UCL uses football-data.org Champions League results because a domestic
        league model cannot validly estimate cross-country matchups on its own.
        """
        if league.key == "UCL":
            if self.football_data_org is None:
                raise RuntimeError(
                    "UCL predictions require FOOTBALL_DATA_API_KEY for "
                    "Champions League training results. Create a football-data.org "
                    "API token and put FOOTBALL_DATA_API_KEY in the project .env before running UCL."
                )
            return self.football_data_org.history(
                league,
                seasons_back=self.seasons_back,
                now=now,
            )

        return self.source.history(
            league,
            seasons_back=self.seasons_back,
            now=now,
        )

    def _current_fixtures(
        self,
        league: LeagueConfig,
        now: datetime,
    ) -> pd.DataFrame:
        """Use trusted league-specific endpoints; never silently invent a fallback schedule."""
        providers: List[str]
        if self.fixture_provider == "auto":
            providers = ["the-odds-api", "football-data-org", "football-data-uk"]
        else:
            providers = [self.fixture_provider]

        failures: List[str] = []
        for provider in providers:
            try:
                if provider == "the-odds-api":
                    if self.odds_api is None:
                        failures.append("The Odds API: THE_ODDS_API_KEY not set")
                        continue
                    df = self.odds_api.events(league, self.lookahead_days, now)
                elif provider == "football-data-org":
                    if self.football_data_org is None:
                        failures.append(
                            "football-data.org: FOOTBALL_DATA_API_KEY not set"
                        )
                        continue
                    df = self.football_data_org.fixtures(
                        league, self.lookahead_days, now
                    )
                else:
                    df = self.source.fixtures(league, self.lookahead_days, now)

                if not df.empty:
                    print(
                        f"[{league.key}] fixtures: {df.iloc[0]['fixture_source']} "
                        f"({len(df)} matches)",
                        file=sys.stderr,
                    )
                    return df
                failures.append(f"{provider}: no upcoming fixtures in window")
            except Exception as exc:
                failures.append(f"{provider}: {exc}")

        raise RuntimeError(
            f"No reliable upcoming {league.name} fixtures found. "
            + " | ".join(failures)
        )

    def _attach_live_odds(
        self,
        fixtures: pd.DataFrame,
        league: LeagueConfig,
        now: datetime,
    ) -> pd.DataFrame:
        if fixtures.empty or not self.live_odds or self.odds_api is None:
            return fixtures

        try:
            odds_df = self.odds_api.odds(league, self.lookahead_days, now)
        except Exception as exc:
            warnings.warn(
                f"Live odds lookup failed for {league.name}: {exc}",
                RuntimeWarning,
            )
            return fixtures

        if odds_df.empty:
            return fixtures

        result = fixtures.copy()
        odds_rows = odds_df.to_dict("records")
        by_id = {str(r.get("fixture_id")): r for r in odds_rows if r.get("fixture_id")}

        by_match: Dict[Tuple[str, str, str], Dict[str, object]] = {}
        for r in odds_rows:
            dt = pd.to_datetime(r.get("_odds_commence_time"), utc=True, errors="coerce")
            if pd.isna(dt):
                continue
            key = (
                dt.date().isoformat(),
                canonical_team_key(str(r.get("_odds_home_team") or "")),
                canonical_team_key(str(r.get("_odds_away_team") or "")),
            )
            if key not in by_match:
                by_match[key] = r

        copied_fields = [
            c for c in odds_df.columns
            if not c.startswith("_odds_") and c != "fixture_id"
        ]
        for field in [*copied_fields, "odds_match_method", "odds_event_id"]:
            if field not in result.columns:
                result[field] = None

        for idx, row in result.iterrows():
            match = None
            method = None
            fixture_id = str(row.get("fixture_id") or "")
            if fixture_id in by_id:
                match = by_id[fixture_id]
                method = "event_id"
            else:
                date = pd.Timestamp(row["Date"]).date().isoformat()
                key = (
                    date,
                    canonical_team_key(str(row["HomeTeam"])),
                    canonical_team_key(str(row["AwayTeam"])),
                )
                match = by_match.get(key)
                if match is not None:
                    method = "date+teams"

            if match is None:
                continue
            for field in copied_fields:
                result.at[idx, field] = match.get(field)
            result.at[idx, "odds_match_method"] = method
            result.at[idx, "odds_event_id"] = match.get("fixture_id")

        matched = int(result.get("odds_source", pd.Series(dtype=object)).notna().sum())
        print(
            f"[{league.key}] live odds matched: {matched}/{len(result)} fixtures "
            f"(regions={self.odds_regions})",
            file=sys.stderr,
        )
        return result

    def _predict_row(
        self,
        model: DixonColesModel,
        row: pd.Series,
    ) -> Tuple[Dict[str, object], Dict[str, float]]:
        home, away = str(row["HomeTeam"]), str(row["AwayTeam"])
        matrix, meta = model.score_matrix(home, away)

        raw_x12 = model.one_x_two(matrix)
        raw_over_1_5 = model.over_under(matrix, 1.5)["over"]
        raw_under_3_5 = model.over_under(matrix, 3.5)["under"]
        raw_btts_yes = float(matrix[1:, 1:].sum())
        snapshot = market_snapshot(row, devig_method=self.devig_method)
        market_probs = [
            snapshot["market_p_home"],
            snapshot["market_p_draw"],
            snapshot["market_p_away"],
        ]

        blend_applied = False
        if self.market_weight > 0 and all(p is not None for p in market_probs):
            target = (
                (1.0 - self.market_weight)
                * np.array([raw_x12["home"], raw_x12["draw"], raw_x12["away"]])
                + self.market_weight * np.array(market_probs, dtype=float)
            )
            matrix = reweight_matrix_to_1x2(matrix, target)
            blend_applied = True

        if getattr(self, '_benchmark_trial_enabled', False):
            self._benchmark_score_matrices[(home, away, str(row.get('kickoff_utc')))] = matrix.copy()
            if hasattr(self, '_totals_shadow_inputs'):
                self._totals_shadow_inputs[(home, away, str(row.get('kickoff_utc')))] = {'lambda_home': meta['lambda_home'], 'lambda_away': meta['lambda_away'], 'rho': float(model.rho), 'max_goals': model.max_goals, 'reference': row.get('shadow_pinnacle_totals')}
        pred = prediction_from_matrix(model, matrix, meta)
        pred["raw_p_home"] = raw_x12["home"]
        pred["raw_p_draw"] = raw_x12["draw"]
        pred["raw_p_away"] = raw_x12["away"]
        pred["raw_p_over_1_5"] = raw_over_1_5
        pred["raw_p_under_3_5"] = raw_under_3_5
        pred["raw_p_btts_yes"] = raw_btts_yes
        from double_chance import probabilities as double_chance_probabilities
        pred.update(double_chance_probabilities(pred))
        pred["market_weight"] = self.market_weight if blend_applied else 0.0
        pred["market_blend_applied"] = blend_applied
        add_value_metrics(pred, snapshot)

        # Preserve the independent Dixon-Coles signal for bet-value auditing.
        # Blended EV uses market-informed probabilities and can look less
        # advantageous mechanically even when forecast calibration improves.
        for side in ("home", "draw", "away"):
            raw_p = float(raw_x12[side])
            market_p = snapshot.get(f"market_p_{side}")
            price = snapshot.get(f"market_{side}_odds")
            pred[f"raw_edge_prob_{side}"] = (
                None if market_p is None else raw_p - float(market_p)
            )
            pred[f"raw_ev_{side}"] = ev_decimal(raw_p, price)

        score_dist = pred.pop("scoreline_distribution")
        return pred, score_dist  # type: ignore[return-value]

    def run_league(
        self,
        league_key: str,
        now: Optional[datetime] = None,
    ):
        if league_key not in LEAGUES:
            raise KeyError(f"Unknown league {league_key!r}. Choose from {list(LEAGUES)}")

        league = LEAGUES[league_key]
        now = now or datetime.now(timezone.utc)

        history = self._history_for_league(
            league,
            now=now,
        )

        if getattr(self, 'recency_experiment_enabled', False):
            self._recency_history = history.copy(deep=True)
        model = DixonColesModel(
            half_life_days=self.half_life_days,
            l2=self.l2,
            max_goals=self.max_goals,
        ).fit(history)

        if getattr(self, '_benchmark_trial_enabled', False):
            self._benchmark_score_matrices = {}
        fixtures = self._current_fixtures(league, now)
        fixtures = self._attach_live_odds(fixtures, league, now)

        diagnostics = {
            "league": league.name,
            "training_matches": model.training_matches,
            "training_end": None if model.training_end is None else str(model.training_end.date()),
            "fit_success": bool(model.fit_result.success) if model.fit_result is not None else False,
            "objective": float(model.fit_result.fun) if model.fit_result is not None else None,
            "base": model.base,
            "home_adv": model.home_adv,
            "rho": model.rho,
            "half_life_days": model.half_life_days,
            "xi_per_day": math.log(2.0) / model.half_life_days,
            "max_goals": model.max_goals,
            "devig_method": self.devig_method,
            "market_weight": self.market_weight,
            "training_data_health": self._training_health(league, model, now),
            "training_source": (
                "football-data.org"
                if league.key == "UCL"
                else "Football-Data.co.uk"
            ),
            "fixture_provider_mode": self.fixture_provider,
            "fixture_sources": sorted(
                str(x) for x in fixtures.get("fixture_source", pd.Series(dtype=object)).dropna().unique()
            ),
            "the_odds_api_enabled": self.odds_api is not None,
            "odds_regions": self.odds_regions if self.odds_api is not None else None,
            "live_odds_matched": int(
                fixtures.get("odds_source", pd.Series(dtype=object)).notna().sum()
            ),
            "additional_event_odds_calls_used_before_this_league": self.extra_event_odds_requests,
            "additional_event_odds_calls_budget": (self.max_extra_event_odds_requests
                if self.additional_odds_coverage == "ranked" else None),
            "additional_event_odds_league_quota": (self.extra_event_odds_quota.get(league.key, 0)
                if self.additional_odds_coverage == "ranked" else None),
        }

        if fixtures.empty:
            return pd.DataFrame(), diagnostics, {}

        records: List[Dict[str, object]] = []
        scorelines: Dict[str, Dict[str, float]] = {}

        # Predict all fixtures first. Ranked mode prioritizes limited requests;
        # full coverage requests every linked fixture within the shortlist window.
        prepared = [
            (row.to_dict(), *self._predict_row(model, row))
            for _, row in fixtures.iterrows()
        ]
        from goal_market_validation import prioritized_additional_events

        quota = max(
            0, self.extra_event_odds_quota.get(league.key, 0)
            - self.extra_event_odds_by_league.get(league.key, 0)
        )
        full_coverage = self.additional_odds_coverage == "all"
        eligible = prioritized_additional_events(
            [(row, pred) for row, pred, _ in prepared], len(prepared),
            as_of=now, coverage="all"
        )
        positions = prioritized_additional_events(
            [(row, pred) for row, pred, _ in prepared], quota,
            as_of=now, coverage=self.additional_odds_coverage
        )
        coverage_rows = []
        selected = set(positions)
        for idx, (row, pred, _) in enumerate(prepared):
            coverage_row = {
                "fixture_id": row.get("fixture_id"), "event_id": row.get("odds_event_id"),
                "home_team": row.get("HomeTeam"), "away_team": row.get("AwayTeam"),
                "kickoff_utc": str(row.get("kickoff_utc")),
                "status": "NOT_REQUESTED_OUTSIDE_WINDOW_OR_UNLINKED",
                "home_draw_quote": False, "draw_away_quote": False,
            }
            coverage_rows.append(coverage_row)
            if idx not in eligible:
                continue
            if self.odds_api is None:
                coverage_row["status"] = "NOT_REQUESTED_API_UNAVAILABLE"
                continue
            if idx not in selected or (not full_coverage and
                    self.extra_event_odds_requests >= self.max_extra_event_odds_requests):
                coverage_row["status"] = "NOT_REQUESTED_RANKING_OR_BUDGET"
                continue
            event_id = row["odds_event_id"]
            self.extra_event_odds_requests += 1
            self.extra_event_odds_by_league[league.key] = (
                self.extra_event_odds_by_league.get(league.key, 0) + 1
            )
            try:
                extra = self.odds_api.extra_markets_for_event(league, event_id)
                pred.update(extra)
                coverage_row["home_draw_quote"] = bool(extra.get("market_home_draw_odds"))
                coverage_row["draw_away_quote"] = bool(extra.get("market_draw_away_odds"))
                coverage_row["status"] = (
                    "RECEIVED_VALID_DC_QUOTES" if coverage_row["home_draw_quote"] and
                    coverage_row["draw_away_quote"] else "RESPONSE_WITHOUT_VALID_DC_QUOTES"
                )
                coverage_row["dc_bookmakers"] = extra.get("market_home_draw_bookmakers", 0)
            except Exception as exc:
                coverage_row["status"] = "REQUEST_FAILED"
                # Do not persist exception URLs, which may contain credentials.
                coverage_row["error_type"] = type(exc).__name__
                warnings.warn(f"Additional odds missing for {event_id}: {exc}", RuntimeWarning)
        diagnostics["additional_odds_coverage_mode"] = self.additional_odds_coverage
        diagnostics["additional_odds_coverage"] = coverage_rows
        diagnostics["additional_odds_in_window_linked_fixtures"] = len(eligible)
        diagnostics["additional_odds_unrequested_linked_fixtures"] = sum(
            coverage_rows[i]["status"].startswith("NOT_REQUESTED") for i in eligible
        )
        diagnostics["additional_event_odds_hard_cap_applies"] = not full_coverage
        diagnostics["additional_event_odds_calls_this_league"] = (
            self.extra_event_odds_by_league.get(league.key, 0)
        )

        for row, pred, score_dist in prepared:
            home, away = str(row["HomeTeam"]), str(row["AwayTeam"])
            match_id = f"{row['Date'].date()}__{home}__{away}"
            scorelines[match_id] = score_dist

            top_scores = pred.get("top_scorelines", [])
            pred["top_scorelines"] = json.dumps(
                [{"score": s, "p": round(float(p), 8)} for s, p in top_scores],
                separators=(",", ":"),
            )

            records.append({
                "league": league.name,
                "date": row["Date"].date().isoformat(),
                "kickoff_utc": row.get("kickoff_utc"),
                "home_team": home,
                "away_team": away,
                "fixture_source": row.get("fixture_source", "unknown"),
                "fixture_id": row.get("fixture_id"),
                "odds_source": row.get("odds_source"),
                "odds_match_method": row.get("odds_match_method"),
                "odds_event_id": row.get("odds_event_id"),
                "odds_last_update_utc": row.get("odds_last_update_utc"),
                "odds_h2h_last_update_utc": row.get("odds_h2h_last_update_utc"),
                "market_best_home_last_update_utc": row.get("live_best_home_last_update_utc"),
                "market_best_draw_last_update_utc": row.get("live_best_draw_last_update_utc"),
                "market_best_away_last_update_utc": row.get("live_best_away_last_update_utc"),
                "odds_bookmakers_1x2": row.get("odds_bookmakers_1x2"),
                "odds_bookmakers_ou25": row.get("odds_bookmakers_ou25"),
                "best_home_bookmaker": row.get("live_best_home_bookmaker"),
                "best_draw_bookmaker": row.get("live_best_draw_bookmaker"),
                "best_away_bookmaker": row.get("live_best_away_bookmaker"),
                "best_over_2_5_bookmaker": row.get("live_best_over_2_5_bookmaker"),
                "best_under_2_5_bookmaker": row.get("live_best_under_2_5_bookmaker"),
                **pred,
            })

        return pd.DataFrame(records), diagnostics, scorelines

    def backtest_league(
        self,
        league_key: str,
        test_start: Optional[str] = None,
        step_days: int = 28,
        min_train: int = 500,
        min_edge: float = 0.05,
        max_edge: float = 0.25,
        min_prob: float = 0.10,
        max_odds: float = 8.0,
        bankroll: float = 1000.0,
        staking: str = "kelly",
        kelly_frac: float = 0.25,
        max_stake_pct: float = 0.02,
        flat_pct: float = 0.01,
        now: Optional[datetime] = None,
    ) -> Tuple[pd.DataFrame, pd.DataFrame, Dict[str, object], pd.DataFrame]:
        """
        Walk-forward historical evaluation.

        Opening prices are allowed as bet-time information.
        Closing prices are NEVER fed into predictions; they are evaluation-only.
        """
        if league_key not in LEAGUES:
            raise KeyError(league_key)
        league = LEAGUES[league_key]
        now = now or datetime.now(timezone.utc)

        hist = self._history_for_league(
            league,
            now=now,
        ).sort_values("Date").reset_index(drop=True)

        if test_start:
            start = pd.Timestamp(test_start)
        else:
            # Default: evaluate roughly the last third while retaining substantial training history.
            start = pd.Timestamp(hist["Date"].quantile(0.67)).normalize()

        if start <= hist["Date"].min():
            raise ValueError("test_start must leave historical matches for training")

        end = hist["Date"].max() + pd.Timedelta(days=1)
        edges = list(pd.date_range(start, end, freq=f"{int(step_days)}D"))
        if not edges or edges[0] != start:
            edges = [start] + edges
        if edges[-1] < end:
            edges.append(end)

        rows: List[Dict[str, object]] = []
        from goal_market_validation import enrich_historical_goal_markets

        for s, e in zip(edges[:-1], edges[1:]):
            train = hist[hist["Date"] < s]
            test = hist[(hist["Date"] >= s) & (hist["Date"] < e)]

            if test.empty or len(train) < min_train:
                continue

            model = DixonColesModel(
                half_life_days=self.half_life_days,
                l2=self.l2,
                max_goals=self.max_goals,
            ).fit(train)

            for _, row in test.iterrows():
                pred, _ = self._predict_row(model, row)

                if row["FTHG"] > row["FTAG"]:
                    y = 0
                elif row["FTHG"] == row["FTAG"]:
                    y = 1
                else:
                    y = 2

                open_ref, open_src = pick_consistent_market(row, OPEN_1X2_TRIPLES)
                close_ref, close_src = pick_consistent_market(row, CLOSE_1X2_TRIPLES)
                p_open = devig(open_ref, self.devig_method)
                p_close = devig(close_ref, self.devig_method)

                best = [
                    pick_best_price(row, BEST_1X2_COLUMNS["home"]),
                    pick_best_price(row, BEST_1X2_COLUMNS["draw"]),
                    pick_best_price(row, BEST_1X2_COLUMNS["away"]),
                ]

                rows.append({
                    "date": pd.Timestamp(row["Date"]).date().isoformat(),
                    "home_team": row["HomeTeam"],
                    "away_team": row["AwayTeam"],
                    "actual_class": y,
                    "home_goals": int(row["FTHG"]),
                    "away_goals": int(row["FTAG"]),
                    "p_home": pred["p_home"],
                    "p_draw": pred["p_draw"],
                    "p_away": pred["p_away"],
                    "raw_p_home": pred["raw_p_home"],
                    "raw_p_draw": pred["raw_p_draw"],
                    "raw_p_away": pred["raw_p_away"],
                    "p_over_0_5": pred["p_over_0_5"],
                    "p_under_0_5": pred["p_under_0_5"],
                    "p_over_2_5": pred["p_over_2_5"],
                    "p_under_2_5": pred["p_under_2_5"],
                    "p_over_4_5": pred["p_over_4_5"],
                    "p_under_4_5": pred["p_under_4_5"],
                    "actual_over_2_5": int(int(row["FTHG"]) + int(row["FTAG"]) >= 3),
                    **enrich_historical_goal_markets(row, pred),
                    "open_source": open_src,
                    "close_source": close_src,
                    "open_home": open_ref[0],
                    "open_draw": open_ref[1],
                    "open_away": open_ref[2],
                    "close_home": close_ref[0],
                    "close_draw": close_ref[1],
                    "close_away": close_ref[2],
                    "open_p_home": p_open[0],
                    "open_p_draw": p_open[1],
                    "open_p_away": p_open[2],
                    "close_p_home": p_close[0],
                    "close_p_draw": p_close[1],
                    "close_p_away": p_close[2],
                    "best_home": best[0],
                    "best_draw": best[1],
                    "best_away": best[2],
                })

        bt = pd.DataFrame(rows)
        if bt.empty:
            return bt, pd.DataFrame(), {"n_predictions": 0}, pd.DataFrame()

        y = bt["actual_class"].to_numpy(dtype=int)
        P = bt[["p_home", "p_draw", "p_away"]].to_numpy(dtype=float)

        metrics: Dict[str, object] = {
            "league": league.name,
            "test_start": str(start.date()),
            "n_predictions": int(len(bt)),
            "model_log_loss": multiclass_log_loss(P, y),
            "model_brier": multiclass_brier(P, y),
            "model_accuracy": accuracy(P, y),
            "over_2_5_brier": binary_brier(
                bt["p_over_2_5"].to_numpy(dtype=float),
                bt["actual_over_2_5"].to_numpy(dtype=int),
            ),
            "devig_method": self.devig_method,
            "market_weight": self.market_weight,
        }

        close_cols = ["close_p_home", "close_p_draw", "close_p_away"]
        close_mask = bt[close_cols].notna().all(axis=1).to_numpy()
        open_cols = ["open_p_home", "open_p_draw", "open_p_away"]
        open_mask = bt[open_cols].notna().all(axis=1).to_numpy()

        if open_mask.any():
            P_open = bt.loc[open_mask, open_cols].to_numpy(dtype=float)
            y_open = y[open_mask]
            metrics.update({
                "opening_market_n": int(open_mask.sum()),
                "opening_market_log_loss": multiclass_log_loss(P_open, y_open),
                "opening_market_brier": multiclass_brier(P_open, y_open),
            })

        if close_mask.any():
            P_close = bt.loc[close_mask, close_cols].to_numpy(dtype=float)
            y_close = y[close_mask]
            metrics.update({
                "closing_market_n": int(close_mask.sum()),
                "closing_market_log_loss": multiclass_log_loss(P_close, y_close),
                "closing_market_brier": multiclass_brier(P_close, y_close),
                "model_minus_closing_log_loss": (
                    multiclass_log_loss(P[close_mask], y_close)
                    - multiclass_log_loss(P_close, y_close)
                ),
            })

        # Reliability table for model probabilities.
        rel = reliability_table(P, y)

        # At most one 1X2 bet per match: highest positive EV after filters.
        bets: List[Dict[str, object]] = []
        labels = ("H", "D", "A")
        prob_cols = ("p_home", "p_draw", "p_away")
        price_cols = ("best_home", "best_draw", "best_away")
        close_prob_cols = ("close_p_home", "close_p_draw", "close_p_away")

        for _, r in bt.iterrows():
            candidates = []
            for j, (label, pc, oc, cc) in enumerate(
                zip(labels, prob_cols, price_cols, close_prob_cols)
            ):
                p = _valid_price(r[oc])
                if p is None:
                    continue
                model_prob = float(r[pc])
                edge_ev = model_prob * p - 1.0
                if (
                    model_prob >= min_prob
                    and p <= max_odds
                    and min_edge <= edge_ev <= max_edge
                ):
                    candidates.append((edge_ev, j, label, model_prob, p, cc))

            if not candidates:
                continue

            edge_ev, j, label, model_prob, odds_taken, close_prob_col = max(candidates)
            cp = r[close_prob_col]
            close_prob = None if pd.isna(cp) else float(cp)
            clv = None if close_prob is None else odds_taken * close_prob - 1.0

            bets.append({
                "date": r["date"],
                "home_team": r["home_team"],
                "away_team": r["away_team"],
                "selection": label,
                "model_prob": model_prob,
                "odds_taken": odds_taken,
                "edge_ev": edge_ev,
                "closing_fair_prob": close_prob,
                "clv": clv,
                "won": int(r["actual_class"]) == j,
            })

        bets_df = pd.DataFrame(bets)
        if not bets_df.empty:
            bets_df = simulate_staking(
                bets_df,
                bankroll0=bankroll,
                mode=staking,
                kelly_frac=kelly_frac,
                max_stake_pct=max_stake_pct,
                flat_pct=flat_pct,
            )
        metrics["bet_summary"] = summarize_bets(bets_df, bankroll)

        return bt, bets_df, metrics, rel


# ---------------------------------------------------------------------------
# Self test
# ---------------------------------------------------------------------------

def self_test() -> None:
    # Verify time splitting cannot leak validation matches into training.
    from dc_decay_validation import make_walkforward_folds
    sample = pd.DataFrame({
        "Date": pd.date_range("2024-01-01", periods=100, freq="7D"),
        "HomeTeam": ["A"] * 100,
        "AwayTeam": ["B"] * 100,
        "FTHG": [1] * 100,
        "FTAG": [0] * 100,
    })
    folds = make_walkforward_folds(
        sample, validation_days=250, step_days=60, min_train=30
    )
    assert folds
    for train, test, origin in folds:
        assert train["Date"].max() < origin
        assert test["Date"].min() >= origin
        assert train["Date"].max() < test["Date"].min()

    # Margin removal
    p = devig([2.0, 3.5, 4.0], "power")
    assert all(x is not None for x in p)
    assert abs(sum(float(x) for x in p) - 1.0) < 1e-10

    pp = devig([2.0, 3.5, 4.0], "proportional")
    assert abs(sum(float(x) for x in pp) - 1.0) < 1e-10

    # Matrix reweighting preserves a valid distribution and hits target 1X2.
    model = DixonColesModel(max_goals=10)
    model.teams = ["A", "B"]
    model.team_to_idx = {"A": 0, "B": 1}
    model.attack = np.array([0.15, -0.15])
    model.weakness = np.array([-0.05, 0.05])
    model.base = math.log(1.20)
    model.home_adv = math.log(1.18)
    model.rho = -0.08

    m, meta = model.score_matrix("A", "B")
    target = np.array([0.55, 0.25, 0.20])
    m2 = reweight_matrix_to_1x2(m, target)
    assert abs(float(m2.sum()) - 1.0) < 1e-12
    x12 = model.one_x_two(m2)
    got = np.array([x12["home"], x12["draw"], x12["away"]])
    assert np.max(np.abs(got - target)) < 1e-10

    pred = prediction_from_matrix(model, m2, meta)
    assert abs(
        float(pred["p_over_0_5"]) + float(pred["p_under_0_5"]) - 1.0
    ) < 1e-12
    assert abs(
        float(pred["p_over_4_5"]) + float(pred["p_under_4_5"]) - 1.0
    ) < 1e-12
    assert len(pred["top_scorelines"]) == 20
    assert len(pred["scoreline_distribution"]) == 20

    assert "UCL" in LEAGUES
    assert LEAGUES["UCL"].odds_api_sport_key == "soccer_uefa_champs_league"
    assert LEAGUES["UCL"].football_data_org_code == "CL"

    # Dedicated odds parser: best prices may come from different books, while
    # the de-vig reference remains a complete same-bookmaker market.
    sample_event = {
        "id": "evt-1",
        "home_team": "Arsenal",
        "away_team": "Chelsea",
        "commence_time": "2026-10-10T14:00:00Z",
        "bookmakers": [
            {
                "key": "book_a",
                "title": "Book A",
                "last_update": "2026-10-08T10:00:00Z",
                "markets": [
                    {
                        "key": "h2h",
                        "outcomes": [
                            {"name": "Arsenal", "price": 2.20},
                            {"name": "Draw", "price": 3.40},
                            {"name": "Chelsea", "price": 3.50},
                        ],
                    },
                    {
                        "key": "totals",
                        "outcomes": [
                            {"name": "Over", "price": 1.95, "point": 2.5},
                            {"name": "Under", "price": 1.90, "point": 2.5},
                        ],
                    },
                ],
            },
            {
                "key": "book_b",
                "title": "Book B",
                "last_update": "2026-10-08T10:05:00Z",
                "markets": [
                    {
                        "key": "h2h",
                        "outcomes": [
                            {"name": "Arsenal", "price": 2.10},
                            {"name": "Draw", "price": 3.60},
                            {"name": "Chelsea", "price": 3.40},
                        ],
                    },
                    {
                        "key": "totals",
                        "outcomes": [
                            {"name": "Over", "price": 2.00, "point": 2.5},
                            {"name": "Under", "price": 1.85, "point": 2.5},
                        ],
                    },
                ],
            },
        ],
    }
    flat = TheOddsAPI.flatten_odds_event(sample_event)
    assert flat["live_best_home_odds"] == 2.20
    assert flat["live_best_draw_odds"] == 3.60
    assert flat["live_ref_1x2_bookmaker"] == "Book B"
    assert flat["live_ref_home_odds"] == 2.10
    assert flat["live_best_over_2_5_odds"] == 2.00
    assert flat["live_ref_ou25_bookmaker"] == "Book B"

    print("V2 self-test passed.")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="Multi-league scoreline/value pipeline with walk-forward evaluation."
    )
    p.add_argument("--api-key-source", choices=["dotenv", "environment"], default="dotenv",
                   help="Default: project .env only, ignoring inherited API keys; environment is for explicit CI use.")
    p.add_argument("--leagues", nargs="+", choices=list(LEAGUES), default=["EPL"])
    p.add_argument("--additional-odds-coverage", choices=["all", "ranked"], default="all",
                   help="all: request every linked fixture in the 72h window (more API credits); ranked: capped legacy mode")
    p.add_argument("--market-led-experiment", action="store_true",
                   help="Write a separate Pinnacle-reference double-chance paper experiment.")
    p.add_argument("--market-led-max-age-minutes", type=float, default=10.0)
    p.add_argument("--market-led-max-skew-minutes", type=float, default=5.0)
    p.add_argument("--market-led-cost-bps", type=float, default=0.0,
                   help="Experiment cost per unit staked in basis points; 100 bps = 1%%.")
    p.add_argument("--goal-blend-experiment", action="store_true",
                   help="Write separate uncalibrated goal-market shadow variants; no baseline changes.")
    p.add_argument("--seasons-back", type=int, default=4)
    p.add_argument("--half-life-days", type=float, default=240.0)
    p.add_argument(
        "--tune-half-life",
        action="store_true",
        help="Choose a per-competition time-decay half-life using walk-forward log loss.",
    )
    p.add_argument(
        "--half-life-candidates",
        nargs="+",
        type=float,
        default=[120.0, 240.0, 365.0, 730.0, 1e9],
        help="Half-life candidates in days; 1e9 approximates no time decay.",
    )
    p.add_argument("--tune-validation-days", type=int, default=365)
    p.add_argument("--recency-experiment", action="store_true",
                   help="Extend the goal sidecar with raw Over 1.5/BTTS half-life comparisons; requires --tune-half-life.")
    p.add_argument("--tune-step-days", type=int, default=56)
    p.add_argument("--tune-min-train", type=int, default=250)
    p.add_argument("--tune-min-validation-matches", type=int, default=25)
    p.add_argument("--reliability-experiment", action="store_true",
                   help="Compare stronger L2 and fixed half-life fits prospectively; no production changes or extra odds requests.")
    p.add_argument("--l2", type=float, default=0.08)
    p.add_argument("--max-goals", type=int, default=10)
    p.add_argument("--lookahead-days", type=int, default=10)
    p.add_argument("--cache-dir", default=".football_cache")
    p.add_argument(
        "--out-dir",
        default="football_output_v2/raw",
        help=(
            "Directory for machine-readable pipeline outputs "
            "(default: football_output_v2/raw)."
        ),
    )
    p.add_argument("--force-refresh", action="store_true")
    p.add_argument(
        "--fixture-provider",
        choices=["auto", "the-odds-api", "football-data-org", "football-data-uk"],
        default="auto",
        help=(
            "Current fixture source. auto prefers The Odds API, then "
            "football-data.org, then Football-Data.co.uk."
        ),
    )
    p.add_argument(
        "--odds-regions",
        default="eu",
        help=(
            "The Odds API bookmaker region(s), comma-separated (default: eu). "
            "Each extra region increases API-credit usage."
        ),
    )
    p.add_argument(
        "--no-live-odds",
        action="store_true",
        help="Use fixtures without requesting The Odds API h2h/totals markets.",
    )

    p.add_argument("--devig", choices=["power", "proportional"], default="power")
    p.add_argument(
        "--market-weight",
        type=float,
        default=0.50,
        help=(
            "Fixed bookmaker blend (default: 0.50) for the recommended "
            "single-model profile. Normally leave unchanged."
        ),
    )
    p.add_argument(
        "--auto-market-weight",
        action="store_true",
        help=(
            "Select a market blend weight from prior walk-forward predictions "
            "using historical opening odds. Never uses current or closing odds "
            "for selection."
        ),
    )
    p.add_argument(
        "--market-weight-candidates",
        nargs="+",
        type=float,
        default=[0.0, 0.15, 0.30, 0.50, 0.70, 1.0],
        help="Candidate bookmaker probabilities blend weights, including 0.",
    )
    p.add_argument(
        "--auto-market-min-matches",
        type=int,
        default=80,
        help="Minimum valid historical matches with opening odds for selection.",
    )

    p.add_argument("--backtest", action="store_true")
    p.add_argument("--test-start", default=None)
    p.add_argument("--step-days", type=int, default=28)
    p.add_argument("--min-train", type=int, default=500)
    p.add_argument("--ucl-validation-min-train", type=int, default=250,
                   help="UCL walk-forward calibration warm-up; audit gates remain unchanged.")

    p.add_argument("--min-edge", type=float, default=0.05)
    p.add_argument("--max-edge", type=float, default=0.25)
    p.add_argument("--min-prob", type=float, default=0.10)
    p.add_argument("--max-odds", type=float, default=8.0)
    p.add_argument("--staking", choices=["kelly", "flat"], default="kelly")
    p.add_argument("--kelly", type=float, default=0.25)
    p.add_argument("--max-stake-pct", type=float, default=0.02)
    p.add_argument("--flat-pct", type=float, default=0.01)
    p.add_argument("--bankroll", type=float, default=1000.0)

    p.add_argument("--self-test", action="store_true")
    return p


def main(argv: Optional[Sequence[str]] = None) -> int:
    args = build_parser().parse_args(argv)

    if args.self_test:
        import quote_policy
        from unittest.mock import patch
        with patch.object(quote_policy, 'CONFIG', Path(__file__).resolve().parent / 'tests' / 'offline_quote_policy.json'):
            self_test()
        return 0

    from api_key_config import load_api_keys
    load_api_keys(args.api_key_source)

    market_led_settings = None
    if args.market_led_experiment:
        if args.backtest:
            raise SystemExit("--market-led-experiment requires live pre-match quotes; cannot use --backtest")
        from market_led_experiment import settings
        try:
            market_led_settings = settings(args.market_led_max_age_minutes,
                args.market_led_max_skew_minutes, args.market_led_cost_bps)
        except ValueError as exc:
            raise SystemExit(str(exc)) from exc

    if args.tune_half_life and args.backtest:
        raise SystemExit(
            "--tune-half-life and --backtest cannot be combined because "
            "tuning on the same historical results would bias the backtest."
        )
    if args.reliability_experiment and args.backtest:
        raise SystemExit("--reliability-experiment requires live forecasts, not --backtest")
    if args.recency_experiment and not args.tune_half_life:
        raise SystemExit('--recency-experiment requires --tune-half-life')
    if args.auto_market_weight and args.backtest:
        raise SystemExit(
            "--auto-market-weight and --backtest cannot be combined: "
            "market weight selection uses historical match outcomes."
        )
    if args.auto_market_weight:
        from market_blend_validation import select_market_weight
    if args.tune_half_life:
        # Lazy import preserves standalone operation without tuning enabled.
        from dc_decay_validation import tune_half_life

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    print(f"Raw outputs will be written to: {out_dir.resolve()}", file=sys.stderr)

    if os.getenv("THE_ODDS_API_KEY"):
        print(
            f"The Odds API enabled for fixtures/markets (regions={args.odds_regions}).",
            file=sys.stderr,
        )
    else:
        print(
            "THE_ODDS_API_KEY is not set; live market odds may be unavailable.",
            file=sys.stderr,
        )

    pipe = FootballValuePipelineV2(
        cache_dir=args.cache_dir,
        seasons_back=args.seasons_back,
        half_life_days=args.half_life_days,
        l2=args.l2,
        max_goals=args.max_goals,
        lookahead_days=args.lookahead_days,
        force_refresh=args.force_refresh,
        devig_method=args.devig,
        market_weight=args.market_weight,
        odds_regions=args.odds_regions,
        fixture_provider=args.fixture_provider,
        live_odds=not args.no_live_odds,
        additional_odds_coverage=args.additional_odds_coverage,
    )

    # Fair reservations across requested competitions; never allow the
    # first processed league to exhaust the 24 event-market API calls.
    from goal_market_validation import (
        distribute_event_odds_budget, evaluate_market_history,
    )
    pipe.extra_event_odds_quota = distribute_event_odds_budget(
        args.leagues, pipe.max_extra_event_odds_requests
    )
    pipe.extra_event_odds_by_league = {
        key: 0 for key in pipe.extra_event_odds_quota
    }
    market_reliability = {}
    combined = []
    recency_parts = []
    reliability_rows = []
    benchmark_matrices = {}
    totals_shadow_inputs = {}
    pipe.recency_experiment_enabled = args.recency_experiment or args.reliability_experiment

    for league_key in args.leagues:
        # Reset both per-competition settings before tuning; never carry a
        # chosen value into a different competition.
        pipe.half_life_days = args.half_life_days
        pipe.market_weight = args.market_weight
        tuning = None
        market_selection = None
        if args.tune_half_life:
            print(f"[{league_key}] tuning Dixon-Coles half-life...", file=sys.stderr)
            training = pipe._history_for_league(
                LEAGUES[league_key],
                now=datetime.now(timezone.utc),
            )
            tuning = tune_half_life(
                history=training,
                model_class=DixonColesModel,
                candidates=args.half_life_candidates,
                l2=args.l2,
                max_goals=args.max_goals,
                validation_days=args.tune_validation_days,
                step_days=args.tune_step_days,
                min_train=args.tune_min_train,
                min_validation_matches=args.tune_min_validation_matches,
                **({'collect_recency_metrics':True} if args.recency_experiment else {}),
            )
            pipe.half_life_days = float(tuning["selected_half_life_days"])
            (out_dir / f"{league_key}_decay_tuning.json").write_text(
                json.dumps(tuning, indent=2),
                encoding="utf-8",
            )
            print(
                f"[{league_key}] selected half-life: "
                f"{pipe.half_life_days:g} days",
                file=sys.stderr,
            )

        if args.auto_market_weight:
            print(
                f"[{league_key}] selecting market blend from historical opening prices...",
                file=sys.stderr,
            )
            # Exactly one pure Dixon-Coles walk-forward backtest provides
            # historical predictions and pre-match bookmaker probabilities.
            # The helper selects a blend on the earlier development matches
            # and reports the later audit period without using it for tuning.
            pipe.market_weight = 0.0
            historical_predictions, _, _, _ = pipe.backtest_league(
                league_key,
                min_train=args.min_train,
                step_days=args.step_days,
            )
            market_selection = select_market_weight(
                historical_predictions,
                candidates=args.market_weight_candidates,
                min_matches=args.auto_market_min_matches,
            )
            selected = market_selection["selected_market_weight"]
            pipe.market_weight = (
                float(selected) if selected is not None else args.market_weight
            )
            (out_dir / f"{league_key}_market_weight_validation.json").write_text(
                json.dumps(market_selection, indent=2),
                encoding="utf-8",
            )
            if selected is None:
                print(
                    f"[{league_key}] insufficient valid historical opening odds; "
                    f"using --market-weight={pipe.market_weight:g}.",
                    file=sys.stderr,
                )
            else:
                print(
                    f"[{league_key}] selected market weight: "
                    f"{pipe.market_weight:g} "
                    f"(audit gain={market_selection['audit_log_loss_gain']:+.4f} "
                    f"log-loss points; NOT used for selection).",
                    file=sys.stderr,
                )

        print(f"[{league_key}] current-fixture model...", file=sys.stderr)
        pipe._benchmark_trial_enabled = not args.backtest
        pipe._benchmark_score_matrices = {}
        pipe._totals_shadow_inputs = {}
        predictions, diagnostics, scorelines = pipe.run_league(league_key)
        from performance_tracking import fixture_key as benchmark_fixture_key
        for source in predictions.to_dict('records'):
            matrix = getattr(pipe, '_benchmark_score_matrices', {}).get((source['home_team'], source['away_team'], str(source.get('kickoff_utc'))))
            if matrix is not None:
                benchmark_matrices[benchmark_fixture_key(source)] = matrix.copy()
                totals_shadow_inputs[benchmark_fixture_key(source)] = pipe._totals_shadow_inputs.get((source["home_team"], source["away_team"], str(source.get("kickoff_utc"))))
        pipe._benchmark_trial_enabled = False
        if args.reliability_experiment and not predictions.empty:
            try:
                from model_reliability_experiment import generate_league as reliability_generate
                reliability_rows.extend(reliability_generate(predictions, pipe._recency_history,
                    DixonColesModel, half_life=pipe.half_life_days, l2=pipe.l2, max_goals=pipe.max_goals))
            except Exception as exc:
                warnings.warn(f'{league_key}: reliability trial unavailable ({type(exc).__name__}); production outputs complete')
        if args.recency_experiment and not predictions.empty:
            try:
                from recency_experiment import generate_league
                recency_parts.append(generate_league(predictions,pipe._recency_history,
                    DixonColesModel,tuning,league=LEAGUES[league_key].name,
                    production_half_life=pipe.half_life_days,l2=pipe.l2,max_goals=pipe.max_goals))
            except Exception as exc:
                # Freeze failure coverage, not a fabricated replacement prediction.
                recency_parts.append({'league':LEAGUES[league_key].name,
                    'training_end':diagnostics['training_end'],'training_matches':diagnostics['training_matches'],
                    'historical_audit':{'status':'GENERATION_FAILED','error':type(exc).__name__},
                    'rows':[{**{k:r.get(k) for k in ('league','home_team','away_team','kickoff_utc')},
                        'market':key,'status':'unavailable','reasons':['recency_generation_failed'],
                        'variants':{},'half_lives':{},'candidate_errors':{}}
                        for r in predictions.to_dict('records') for key in ('over_1_5','btts_yes')]})
                warnings.warn(f'{league_key}: recency experiment unavailable ({type(exc).__name__}); baseline outputs complete')
        if market_selection is not None:
            diagnostics["market_weight_selection"] = {
                "status": market_selection["status"],
                "selected_market_weight": pipe.market_weight,
                "audit_log_loss_gain": market_selection.get("audit_log_loss_gain"),
                "n_usable_matches": market_selection["n_usable_matches"],
            }
        if tuning is not None:
            diagnostics["decay_tuning"] = {
                "selected_half_life_days": tuning["selected_half_life_days"],
                "selected_xi_per_day": tuning["selected_xi_per_day"],
                "selection_metric": tuning["selection_metric"],
                "validation_days": tuning["validation_days"],
            }

        if not args.backtest:
            # Reuse validated snapshots only when the historical model,
            # training cutoff and validation code version match.
            validation_path = out_dir / f"{league_key}_goal_market_validation.json"
            validation_min_train = (args.ucl_validation_min_train
                                    if league_key == "UCL" else args.min_train)
            if validation_min_train < 30:
                raise ValueError("Validation warm-up must contain at least 30 matches")
            config = {
                "validator_version": 4,
                "min_train": validation_min_train,
                "step_days": 56,
                "devig": pipe.devig_method,
                "score_basis": "regulation_time",
                "half_life_days": pipe.half_life_days,
                "market_weight": pipe.market_weight,
                "l2": pipe.l2,
                "max_goals": pipe.max_goals,
                "training_end": diagnostics["training_end"],
                "training_matches": diagnostics["training_matches"],
            }
            cached = None
            if validation_path.exists() and not args.force_refresh:
                try:
                    cached = json.loads(validation_path.read_text(encoding="utf-8"))
                except (ValueError, OSError):
                    cached = None
            if isinstance(cached, dict) and cached.get("config") == config:
                market_validation = cached
            else:
                print(f"[{league_key}] validating goal markets walk-forward...", file=sys.stderr)
                try:
                    historical, _, _, _ = pipe.backtest_league(
                        league_key, min_train=validation_min_train, step_days=56
                    )
                    market_validation = evaluate_market_history(
                        historical, LEAGUES[league_key].name
                    )
                except (ValueError, RuntimeError) as exc:
                    warnings.warn(
                        f"{league_key}: validation unavailable: {exc}",
                        RuntimeWarning,
                    )
                    market_validation = evaluate_market_history(
                        pd.DataFrame(), LEAGUES[league_key].name
                    )
                market_validation["config"] = config
                validation_path.write_text(
                    json.dumps(market_validation, indent=2), encoding="utf-8"
                )
            market_reliability[LEAGUES[league_key].name] = market_validation
            diagnostics["goal_market_reliability"] = {
                key: value["status"]
                for key, value in market_validation["markets"].items()
            }

        predictions.to_csv(out_dir / f"{league_key}_predictions.csv", index=False)
        (out_dir / f"{league_key}_diagnostics.json").write_text(
            json.dumps(diagnostics, indent=2), encoding="utf-8"
        )
        (out_dir / f"{league_key}_scorelines.json").write_text(
            json.dumps(scorelines, indent=2), encoding="utf-8"
        )
        if not predictions.empty:
            combined.append(predictions)

        if args.backtest:
            print(f"[{league_key}] walk-forward backtest...", file=sys.stderr)
            bt, bets, metrics, rel = pipe.backtest_league(
                league_key,
                test_start=args.test_start,
                step_days=args.step_days,
                min_train=args.min_train,
                min_edge=args.min_edge,
                max_edge=args.max_edge,
                min_prob=args.min_prob,
                max_odds=args.max_odds,
                bankroll=args.bankroll,
                staking=args.staking,
                kelly_frac=args.kelly,
                max_stake_pct=args.max_stake_pct,
                flat_pct=args.flat_pct,
            )
            bt.to_csv(out_dir / f"{league_key}_backtest_predictions.csv", index=False)
            bets.to_csv(out_dir / f"{league_key}_backtest_bets.csv", index=False)
            rel.to_csv(out_dir / f"{league_key}_reliability.csv", index=False)
            (out_dir / f"{league_key}_backtest_metrics.json").write_text(
                json.dumps(metrics, indent=2), encoding="utf-8"
            )
            plot_reliability(
                {"model": rel},
                out_dir / f"{league_key}_reliability.png",
            )

    # One conservative shortlist across all requested leagues, not an
    # independent quota of two picks per league. Do not alter predictions.
    from conservative_bet_filter import build_conservative_shortlist

    all_predictions = (
        pd.concat(combined, ignore_index=True, sort=False)
        if combined else pd.DataFrame()
    )
    if combined:
        all_predictions.to_csv(
            out_dir / "all_leagues_predictions.csv", index=False
        )

    shortlist, decisions, selection_summary = build_conservative_shortlist(
        all_predictions, market_reliability=market_reliability
    )
    shortlist.to_csv(out_dir / "conservative_bet_shortlist.csv", index=False)
    strictly_qualified = shortlist.loc[
        shortlist["selection_tier"] == "STRICT"
    ].copy()
    strictly_qualified.to_csv(
        out_dir / "conservative_strict_qualifiers.csv", index=False
    )
    decisions.to_csv(out_dir / "conservative_bet_rejections.csv", index=False)
    (out_dir / "conservative_bet_summary.json").write_text(
        json.dumps(selection_summary, indent=2), encoding="utf-8"
    )
    if combined:
        from pipeline_health import write_generation_metadata
        write_generation_metadata(out_dir, selection_summary)

    # Retain a timestamped historical audit even though the current raw
    # shortlist is overwritten each run. No picks are ever added by force.
    archive = out_dir / "shortlist_history"
    archive.mkdir(parents=True, exist_ok=True)
    snapshot_stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
    decisions.to_csv(
        archive / f"conservative_decisions_{snapshot_stamp}.csv", index=False
    )
    print(
        f"Conservative candidate filter: {selection_summary['status']} "
        f"({selection_summary['n_strict_qualified']} STRICT, "
        f"{selection_summary['n_provisional_watchlist']} PROVISIONAL WATCHLIST; "
        f"see {out_dir / 'conservative_bet_shortlist.csv'})",
        file=sys.stderr,
    )

    if combined and not args.backtest:
        try:
            from filter_sensitivity_experiment import write_experiment as write_filter_sensitivity
            write_filter_sensitivity(all_predictions, out_dir, selection_summary,
                                     decisions, market_reliability)
        except Exception as exc:
            warnings.warn(f"Filter sensitivity experiment failed ({type(exc).__name__}); baseline outputs complete")

    if combined and not args.backtest:
        try:
            from benchmark_forward_experiment import write_experiment as write_benchmark_forward
            write_benchmark_forward(all_predictions, out_dir, selection_summary["generated_at_utc"], benchmark_matrices)
        except Exception as exc:
            warnings.warn(f"Benchmark forward trial unavailable ({type(exc).__name__}); production outputs complete")
        try:
            from totals_anchor_experiment import write_experiment as write_totals_shadow
            write_totals_shadow(all_predictions, out_dir, selection_summary["generated_at_utc"], benchmark_matrices, totals_shadow_inputs)
        except Exception as exc:
            warnings.warn(f"Totals anchoring trial unavailable ({type(exc).__name__}); production outputs complete")

    if args.reliability_experiment and combined and not args.backtest:
        try:
            from model_reliability_experiment import write_experiment as write_reliability
            write_reliability(all_predictions, out_dir, selection_summary["generated_at_utc"], reliability_rows)
        except Exception as exc:
            warnings.warn(f'Reliability trial unavailable ({type(exc).__name__}); production outputs complete')

    if (args.goal_blend_experiment or args.recency_experiment) and combined and not args.backtest:
        try:
            from goal_blend_experiment import write_experiment
            write_experiment(all_predictions, out_dir, selection_summary["generated_at_utc"],
                **({'recency_parts':recency_parts} if args.recency_experiment else {}))
        except Exception as exc:
            warnings.warn(f"Shadow experiment failed; baseline outputs complete: {exc}")

    if args.market_led_experiment and combined:
        try:
            from market_led_experiment import write_experiment as write_market_led
            experiment = write_market_led(all_predictions, out_dir,
                selection_summary["generated_at_utc"], pipe.odds_api, market_led_settings)
            print(f"Market-led paper experiment: {sum(r['selected'] for r in experiment['rows'])} selections; "
                  f"see {out_dir / 'market_led_report.md'}", file=sys.stderr)
        except Exception as exc:
            # Optional research failure must not invalidate completed baseline output.
            warnings.warn(f"Market-led experiment failed ({type(exc).__name__}); baseline outputs complete")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

