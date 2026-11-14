"""Sharpened cagey probabilities for the new master (Phase 4, fill rule, method cagey-sharpen-walk-forward-v1).

A walk-forward recalibration of the cagey tier's own probabilities, research_sharpen.py's approach:

    p' = sigmoid(s * logit(p))          one slope s per quantity and line type, no intercept, s > 1 sharpens

Quantities: the no-loss chance (P(win) + P(half win) + P(push)) and the chance of profit (P(win) + P(half win):
the bet returns more than the stake). Line types: half (Home win, Away win, double chance, AH +/-0.5, +/-1.5, ...),
quarter (AH +/-0.25, +/-0.75, ...) and whole (AH 0, +/-1, ...). On half and quarter lines the two quantities are the
same event, so their fits coincide; on whole lines they differ by the push, and the sharpened chance of profit is
capped at the sharpened no-loss chance.

Fit: recency-weighted maximum likelihood (a logistic regression without intercept of the outcome on logit(p)) on
the cagey tier's forecasts of matches played before the fold origin, never the research model, never anything after
kickoff. Neutral (s = 1, sharpened = current) until `min_fixtures` earlier fixtures contributed events, or when the
optimiser fails, so a bad fit never moves a probability.

The cagey tier's own outputs are never changed: these values are new columns used only by the new master, and only
if the pass rule in master_reconciliation_config.json (cagey_sharpening.pass_rule) passed.
"""
from __future__ import annotations

import math
from typing import Dict, Mapping, Optional, Tuple

import numpy as np
import pandas as pd
from scipy.optimize import minimize_scalar

VERSION = 'cagey-sharpen-walk-forward-v1'
QUANTITIES = ('no_loss', 'profit')
LINE_TYPES = ('half', 'quarter', 'whole')
KEYS = tuple(f'{q}:{t}' for q in QUANTITIES for t in LINE_TYPES)
HALF_MARKETS = ('Home win', 'Away win', 'Double Chance 1X', 'Double Chance X2')
EPS = 1e-9


def line_type(line) -> str:
    """'whole', 'half' or 'quarter' for an Asian handicap line (in quarter-goal units)."""
    quarter = int(round(float(line) * 4)) % 4
    return 'whole' if quarter == 0 else 'half' if quarter == 2 else 'quarter'


def offer_line_type(market, line) -> Optional[str]:
    """Line type of an offer: wins and double chance are half lines (Home win = home -0.5, 1X = home +0.5)."""
    market = str(market or '')
    if market in HALF_MARKETS or market.startswith('Double Chance'):
        return 'half'
    try:
        value = float(line)
    except (TypeError, ValueError):
        return None
    return line_type(value) if math.isfinite(value) else None


def no_loss(mass) -> float:
    """P(win) + P(half win) + P(push) of a settlement distribution (win, half win, push, half loss, loss)."""
    return float(mass[0] + mass[1] + mass[2])


def profit(mass) -> float:
    """P(the bet returns more than the stake) = P(win) + P(half win): a push returns the stake, a half win
    returns stake + (odds - 1) / 2, a half loss half the stake."""
    return float(mass[0] + mass[1])


def logit(p) -> np.ndarray:
    p = np.clip(np.asarray(p, dtype=float), EPS, 1 - EPS)
    return np.log(p / (1 - p))


def apply(p, slope: float):
    """sigmoid(slope * logit(p)); exactly p when the slope is neutral."""
    if float(slope) == 1.:
        return p
    out = 1 / (1 + np.exp(-float(slope) * logit(p)))
    return float(out) if np.ndim(out) == 0 else out


def neutral(matches=0, status='warm_up') -> Dict[str, object]:
    return {'slope': 1., 'status': status, 'fixtures': int(matches), 'events': 0}


def fit(p, y, age_days, fixtures, half_life_days: float, min_fixtures: int, bounds=(0.5, 2.5)) -> Dict[str, object]:
    """The slope by recency-weighted maximum likelihood on earlier cagey forecasts `p` and outcomes `y` (0/1).

    `age_days` is how long before the fold origin each event's match was played (must be >= 0: only earlier
    matches), `fixtures` each event's fixture id. Neutral below `min_fixtures` distinct fixtures."""
    p, y, age = (np.asarray(v, dtype=float) for v in (p, y, age_days))
    if len(p) and ((age <= 0).any() or not np.isfinite(p).all()):
        raise ValueError('Fit events must come from matches played before the origin, with finite probabilities')
    count = int(pd.unique(np.asarray(fixtures, dtype=object)).size) if len(p) else 0
    if count < min_fixtures:
        return neutral(count)
    x, w = logit(p), np.exp(-math.log(2) * age / half_life_days)

    def loss(slope):
        z = slope * x
        return float((w * (np.logaddexp(0., z) - y * z)).sum() / w.sum())

    result = minimize_scalar(loss, bounds=tuple(bounds), method='bounded', options={'xatol': 1e-6})
    if not result.success or not np.isfinite(result.fun):
        return neutral(count, 'optimiser_failed')
    return {'slope': float(result.x), 'status': 'fitted', 'fixtures': count, 'events': int(len(p)),
            'neutral_minus_fitted_loss': float(loss(1.) - result.fun)}


def walk_forward(events: pd.DataFrame, origins, config: Mapping) -> Dict[str, Dict[str, Dict[str, object]]]:
    """Per fold origin (ISO date), the fit of every slope (KEYS) on the events of matches played before it.

    `events` has one row per (offer line, quantity): date (Timestamp of the match), fixture_key, quantity,
    line_type, p (the cagey tier's probability) and y (observed 0/1). An event on or after the origin never
    reaches that origin's fit, so a later result can never change an earlier forecast."""
    bounds, half_life = config['slope_bounds'], float(config['half_life_days'])
    minimum = int(config['min_fixtures'])
    out = {}
    dates = pd.DatetimeIndex(events['date']) if len(events) else pd.DatetimeIndex([])
    for origin in origins:
        origin = pd.Timestamp(origin)
        past = events.loc[np.asarray(dates < origin)] if len(events) else events
        fits = {}
        for key in KEYS:
            quantity, kind = key.split(':')
            part = past.loc[(past.quantity == quantity) & (past.line_type == kind)] if len(past) else past
            if part.empty:
                fits[key] = neutral()
                continue
            age = (origin - pd.DatetimeIndex(part['date'])).total_seconds().to_numpy() / 86400
            fits[key] = fit(part.p, part.y, age, part.fixture_key, half_life, minimum, bounds)
        out[origin.date().isoformat()] = fits
    return out


def slopes(fits: Mapping[str, Mapping]) -> Dict[str, float]:
    return {key: float(fits[key]['slope']) for key in KEYS}


def sharpen(no_loss_p: float, profit_p: float, kind: str, slope_by_key: Mapping[str, float]) -> Tuple[float, float]:
    """Sharpened (no-loss, chance of profit) of one offer of line type `kind`. On whole lines the sharpened chance of
    profit is capped at the sharpened no-loss chance (a profit is a no-loss outcome)."""
    nl = apply(float(no_loss_p), slope_by_key[f'no_loss:{kind}'])
    pr = apply(float(profit_p), slope_by_key[f'profit:{kind}'])
    if kind == 'whole':
        pr = min(pr, nl)
    return float(nl), float(pr)


def fold_for(date, origins) -> Optional[str]:
    """The latest fold origin (ISO date) on or before `date`, or None."""
    date = pd.Timestamp(date)
    eligible = [o for o in origins if pd.Timestamp(o) <= date]
    return max(eligible, key=pd.Timestamp) if eligible else None


def period_holds(entry: Mapping[str, Mapping]) -> Dict[str, object]:
    """One period of the pass rule: for both quantities, the sharpened slope strictly closer to 1.0 than the current
    one, and the 95% interval of (current minus sharpened) log loss not entirely below zero.

    `entry[quantity]` has slope_current, slope_sharpened and log_loss_current_minus_sharpened ({'interval_95'})."""
    out = {}
    for quantity in QUANTITIES:
        e = entry.get(quantity) or {}
        current, sharp = e.get('slope_current'), e.get('slope_sharpened')
        closer = bool(current is not None and sharp is not None and np.isfinite(current) and np.isfinite(sharp)
                      and abs(sharp - 1) < abs(current - 1))
        interval = (e.get('log_loss_current_minus_sharpened') or {}).get('interval_95')
        no_worse = bool(interval is not None and interval[1] >= 0)
        out[quantity] = {'slope_closer_to_one': closer, 'log_loss_not_worse': no_worse, 'holds': closer and no_worse}
    out['holds'] = all(out[q]['holds'] for q in QUANTITIES)
    return out


def verdict(check: Mapping[str, Mapping]) -> Dict[str, object]:
    """The pass rule (cagey_sharpening.pass_rule): development and validation must both hold; the retrospective is
    reported but never decides. Missing development or validation fails."""
    periods = {name: period_holds(check[name]) for name in ('development', 'validation') if name in check}
    passes = all(name in periods and periods[name]['holds'] for name in ('development', 'validation'))
    return {'periods': periods, 'passes': bool(passes),
            'uses': 'sharpened cagey probabilities' if passes else 'current cagey probabilities'}
