"""Read-only service layer for an HTTP API (for example FastAPI).

Every function returns JSON-safe Python data (NaN/inf become ``None``) and
reads only the current *validated* prediction-run bundle through
``prediction_runs.resolve_raw``, never a partially written projection. A
web app maps routes onto these functions one-to-one; forecasting itself
stays in the scheduled CLI so request latency never triggers a model fit
or a bookmaker API call.

    GET  /runs/current          -> current_run()
    GET  /predictions?league=   -> predictions(league=...)
    GET  /shortlist?tier=       -> shortlist(tier=...)
    GET  /stakes?bankroll=      -> stake_plan(bankroll=...)
    POST /price                 -> price_fixture(...)
"""
from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Mapping, Optional

import numpy as np
import pandas as pd

DEFAULT_RAW = Path(__file__).resolve().parent / 'football_output_v2' / 'raw'


def _clean(value):
    if isinstance(value, dict):
        return {str(k): _clean(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [_clean(v) for v in value]
    if isinstance(value, np.generic):
        value = value.item()
    if isinstance(value, float) and not math.isfinite(value):
        return None
    if value is pd.NaT:
        return None
    return value


def _records(frame: pd.DataFrame) -> list:
    return _clean(frame.astype(object).where(frame.notna(), None).to_dict('records'))


def _bundle(raw) -> Path:
    from prediction_runs import resolve_raw
    return resolve_raw(Path(raw))


def _read(raw, name: str) -> pd.DataFrame:
    path = _bundle(raw) / name
    if not path.is_file():
        raise FileNotFoundError(f'{name} is not part of the current prediction run')
    return pd.read_csv(path)


def current_run(raw=DEFAULT_RAW) -> dict:
    """Identity and file list of the run readers currently follow."""
    directory = _bundle(raw)
    manifest_path = directory / 'run_manifest.json'
    summary = json.loads((directory / 'conservative_bet_summary.json').read_text(encoding='utf-8'))
    manifest = (json.loads(manifest_path.read_text(encoding='utf-8'))
                if manifest_path.is_file() else {})
    return _clean({'run_id': manifest.get('run_id'),
                   'generated_at_utc': summary.get('generated_at_utc'),
                   'saved_at_utc': manifest.get('saved_at_utc'),
                   'selection_policy_version': summary.get('selection_policy_version'),
                   'status': summary.get('status'),
                   'files': sorted(manifest.get('sha256', {}))})


def predictions(raw=DEFAULT_RAW, league: Optional[str] = None) -> list:
    """Fixture forecasts, optionally for one league (name or key, case-insensitive)."""
    frame = _read(raw, 'all_leagues_predictions.csv')
    if league:
        from football_value_pipeline_v2_standalone import LEAGUES
        names = {league.casefold()}
        if league in LEAGUES:
            names.add(LEAGUES[league].name.casefold())
        frame = frame[frame['league'].astype(str).str.casefold().isin(names)]
    return _records(frame)


def shortlist(raw=DEFAULT_RAW, tier: Optional[str] = None) -> list:
    """Conservative shortlist rows, optionally filtered by ``selection_tier``."""
    frame = _read(raw, 'conservative_bet_shortlist.csv')
    if tier:
        frame = frame[frame['selection_tier'].astype(str).str.upper() == tier.upper()]
    return _records(frame)


def stake_plan(raw=DEFAULT_RAW, bankroll: Optional[float] = None, **settings) -> list:
    """Advisory stakes for the current shortlist.

    Uses the run's saved ``stake_recommendations.csv`` when the request
    matches its settings; otherwise recomputes from the saved shortlist with
    ``staking.stake_recommendations`` (pure arithmetic, no model fit).
    """
    import staking
    if bankroll is None and not settings:
        try:
            return _records(_read(raw, staking.OUTPUT_FILE))
        except FileNotFoundError:
            pass
    frame = _read(raw, 'conservative_bet_shortlist.csv')
    plan = staking.stake_recommendations(
        frame, bankroll=staking.DEFAULT_BANKROLL_UNITS if bankroll is None else float(bankroll), **settings)
    return _records(plan)


def price_fixture(lambda_home: float, lambda_away: float, rho: float,
                  odds: Optional[Mapping[str, float]] = None,
                  n_simulations: int = 0, seed: Optional[int] = None) -> dict:
    """Price one fixture from goal rates; optionally compare offered odds.

    ``odds`` keys use ``market:selection[:line]`` labels from the result,
    e.g. ``{"1x2:home": 2.1, "total:over:2.5": 1.95,
    "asian_handicap:home:-0.5": 2.05}``. Each priced key gains
    ``offered_decimal_odds``, ``expected_value`` and ``full_kelly_fraction``.
    """
    import match_simulation
    import staking
    if n_simulations:
        table = match_simulation.simulate_fixture(lambda_home, lambda_away, rho, n_simulations, seed)
        table = table.rename(columns={'true_decimal_price': 'fair_decimal_odds'})
    else:
        table = match_simulation.exact_prices(lambda_home, lambda_away, rho)
    table['key'] = [f'{m}:{s}' if pd.isna(line) else f'{m}:{s}:{float(line):g}'
                    for m, s, line in zip(table['market'], table['selection'], table['line'])]
    table = table.set_index('key')
    unknown = sorted(set(odds or {}) - set(table.index))
    if unknown:
        raise KeyError(f'Unknown market keys: {unknown}')
    for key, price in (odds or {}).items():
        probs = {'full_win': table.at[key, 'win'], 'half_win': table.at[key, 'half_win'],
                 'refund': table.at[key, 'refund'], 'half_loss': table.at[key, 'half_loss'],
                 'full_loss': table.at[key, 'loss']}
        total = sum(probs.values())
        probs = {k: v / total for k, v in probs.items()}
        table.loc[key, 'offered_decimal_odds'] = float(price)
        table.loc[key, 'expected_value'] = staking.settlement_ev(probs, float(price))
        table.loc[key, 'full_kelly_fraction'] = staking.settlement_kelly(probs, float(price))
    return _clean({'model': {'lambda_home': lambda_home, 'lambda_away': lambda_away, 'rho': rho,
                             'n_simulations': int(n_simulations)},
                   'markets': {key: {k: v for k, v in row.items()}
                               for key, row in table.astype(object).where(table.notna(), None)
                               .to_dict('index').items()}})
