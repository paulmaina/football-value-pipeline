"""Advisory fractional-Kelly stake sizing for shortlisted selections.

Expected value per unit stake on a binary selection is ``EV = p*o - 1``.
The Kelly fraction maximises expected log bankroll; for a binary bet
with ``b = o - 1`` it is ``f* = (p*b - (1 - p)) / b``. Asian handicaps can
refund or settle by halves, so the general form maximises

    G(f) = sum_k p_k * log(1 + f * r_k)

over the settlement outcomes, with per-unit returns ``r = w*(o-1) - l - cost``
(``w``/``l`` = fraction of stake won/lost, exactly as
``asian_handicap.profit`` settles them).

Probabilities are deliberately conservative: binary markets use the
shortlist ``rank_probability`` (calibration-penalised), and for Asian
handicaps the same penalty moves probability from winning outcomes to a
full loss. These are the inputs behind ``conservative_estimated_ev``.

Full Kelly overbets whenever probabilities are estimated with error, so
the recommendation is ``multiplier * f*`` (quarter-Kelly by default),
capped per bet and scaled down when the slate's combined exposure would
exceed ``max_total_exposure``. Only STRICT selections receive a stake.
These figures are advisory research outputs; they never change
probabilities, filters or the shortlist itself.
"""
from __future__ import annotations

import math
from pathlib import Path
from typing import Mapping, Optional

import numpy as np
import pandas as pd
from scipy.optimize import minimize_scalar

from asian_handicap import OUTCOMES

VERSION = 'fractional-kelly-conservative-v1'
OUTPUT_FILE = 'stake_recommendations.csv'
KELLY_MULTIPLIER = 0.25
MAX_STAKE_FRACTION = 0.025
MAX_TOTAL_EXPOSURE = 0.10
DEFAULT_BANKROLL_UNITS = 100.0
STAKED_TIERS = ('STRICT',)
# (stake fraction won, stake fraction lost) for each settlement outcome.
SETTLEMENT = {'full_win': (1., 0.), 'half_win': (.5, 0.), 'refund': (0., 0.),
              'half_loss': (0., .5), 'full_loss': (0., 1.)}
IDENTITY_COLUMNS = ['league', 'home_team', 'away_team', 'kickoff_utc', 'fixture_id',
                    'market', 'selection_tier', 'bookmaker', 'offered_decimal_odds']


def _number(value) -> Optional[float]:
    try:
        number = float(value)
    except (TypeError, ValueError):
        return None
    return number if math.isfinite(number) else None


def _check(odds: float, cost: float = 0.0) -> None:
    if not math.isfinite(odds) or odds <= 1:
        raise ValueError('Decimal odds must be finite and above 1')
    if not math.isfinite(cost) or not 0 <= cost < 1:
        raise ValueError('Per-stake cost must be in [0, 1)')


def expected_value(probability: float, odds: float) -> float:
    """``EV = p * odds - 1`` per unit staked."""
    _check(odds)
    if not 0 <= probability <= 1:
        raise ValueError('Probability must be in [0, 1]')
    return probability * odds - 1.0


def kelly_fraction(probability: float, odds: float) -> float:
    """Full binary Kelly ``(p*b - (1 - p)) / b``; negative means no bet."""
    expected_value(probability, odds)
    b = odds - 1.0
    return (probability * b - (1.0 - probability)) / b


def settlement_returns(odds: float, cost: float = 0.0) -> dict:
    """Profit per unit stake for each settlement outcome."""
    _check(odds, cost)
    return {k: w * (odds - 1.0) - lost - cost for k, (w, lost) in SETTLEMENT.items()}


def settlement_ev(probabilities: Mapping[str, float], odds: float, cost: float = 0.0) -> float:
    """Expected profit per unit stake for a settlement distribution."""
    returns = settlement_returns(odds, cost)
    return float(sum(float(probabilities.get(k, 0.0)) * returns[k] for k in OUTCOMES))


def settlement_kelly(probabilities: Mapping[str, float], odds: float, cost: float = 0.0) -> float:
    """Full Kelly fraction for any settlement distribution.

    Equals :func:`kelly_fraction` for win/lose bets and
    ``(p_w*b - p_l) / (b*(p_w + p_l))`` for lines that can refund.
    """
    probs = np.array([float(probabilities.get(k, 0.0)) for k in OUTCOMES])
    if (probs < -1e-12).any() or abs(probs.sum() - 1.0) > 1e-6:
        raise ValueError('Settlement probabilities must form a distribution')
    by_outcome = settlement_returns(odds, cost)
    returns = np.array([by_outcome[k] for k in OUTCOMES])
    if float(probs @ returns) <= 0:
        return 0.0
    losing = (probs > 0) & (returns < 0)
    if not losing.any():
        return 1.0
    upper = min(1.0, 1.0 / float(-returns[losing].min())) - 1e-9
    result = minimize_scalar(lambda f: -float(probs @ np.log1p(f * returns)),
                             bounds=(0.0, upper), method='bounded', options={'xatol': 1e-12})
    return float(result.x)


def conservative_settlement(row: Mapping) -> dict:
    """Calibration-penalised settlement distribution for one shortlist row."""
    rank = _number(row.get('rank_probability'))
    predicted = _number(row.get('predicted_probability'))
    basis = rank if rank is not None else predicted
    if basis is None or not 0 <= basis <= 1:
        raise ValueError('Missing selection probability')
    if row.get('handicap_side') in ('home', 'away'):
        probs = {k: _number(row.get('p_' + k)) for k in OUTCOMES}
        if any(v is None for v in probs.values()):
            raise ValueError('Incomplete Asian handicap settlement probabilities')
        penalty = max(0.0, (predicted if predicted is not None else basis) - basis)
        for outcome in ('full_win', 'half_win'):
            moved = min(penalty, probs[outcome])
            probs[outcome] -= moved
            probs['full_loss'] += moved
            penalty -= moved
        return probs
    return {**dict.fromkeys(OUTCOMES, 0.0), 'full_win': basis, 'full_loss': 1.0 - basis}


def stake_recommendations(
    shortlist: pd.DataFrame,
    bankroll: float = DEFAULT_BANKROLL_UNITS,
    multiplier: float = KELLY_MULTIPLIER,
    max_fraction: float = MAX_STAKE_FRACTION,
    max_total_exposure: Optional[float] = MAX_TOTAL_EXPOSURE,
) -> pd.DataFrame:
    """One advisory stake row per shortlisted selection.

    ``stake_fraction = min(multiplier * f*, max_fraction)`` from the
    conservative settlement distribution, then all STRICT stakes are scaled
    proportionally if their sum exceeds ``max_total_exposure``.
    """
    if not math.isfinite(bankroll) or bankroll < 0:
        raise ValueError('Bankroll must be finite and non-negative')
    if not 0 < multiplier <= 1 or not 0 < max_fraction <= 1:
        raise ValueError('Kelly multiplier and stake cap must be in (0, 1]')
    if max_total_exposure is not None and not 0 < max_total_exposure <= 1:
        raise ValueError('Total exposure cap must be in (0, 1]')
    rows = []
    for record in shortlist.to_dict('records'):
        out = {k: record.get(k) for k in IDENTITY_COLUMNS}
        out.update(staking_version=VERSION, probability_basis='rank_probability',
                   kelly_multiplier=multiplier, max_stake_fraction=max_fraction,
                   conservative_ev=None, full_kelly_fraction=None, stake_fraction=0.0)
        try:
            odds = _number(record.get('offered_decimal_odds'))
            cost = _number(record.get('per_stake_cost')) or 0.0
            if odds is None:
                raise ValueError('Missing odds')
            probs = conservative_settlement(record)
            full = settlement_kelly(probs, odds, cost)
            out.update(conservative_ev=settlement_ev(probs, odds, cost), full_kelly_fraction=full)
            if record.get('selection_tier') not in STAKED_TIERS:
                out['staking_status'] = 'NO_STAKE_NOT_STRICT'
            elif full <= 0:
                out['staking_status'] = 'NO_STAKE_NON_POSITIVE_CONSERVATIVE_EV'
            else:
                out['stake_fraction'] = min(multiplier * full, max_fraction)
                out['staking_status'] = ('STAKE_CAPPED' if multiplier * full > max_fraction
                                         else 'STAKE')
        except ValueError as exc:
            out['staking_status'] = 'NO_STAKE_INVALID_INPUT'
            out['staking_error'] = str(exc)
        rows.append(out)
    frame = pd.DataFrame(rows)
    if frame.empty:
        return pd.DataFrame(columns=[*IDENTITY_COLUMNS, 'staking_version', 'stake_fraction',
                                     'stake_units', 'staking_status'])
    total = float(frame['stake_fraction'].sum())
    frame['exposure_scale'] = 1.0
    if max_total_exposure is not None and total > max_total_exposure:
        frame['exposure_scale'] = max_total_exposure / total
        frame['stake_fraction'] *= frame['exposure_scale']
    frame['stake_units'] = frame['stake_fraction'] * bankroll
    frame['bankroll_units'] = bankroll
    return frame


def write_stake_recommendations(shortlist: pd.DataFrame, out_dir: Path, **settings) -> Path:
    """Write :func:`stake_recommendations` beside the shortlist."""
    path = Path(out_dir) / OUTPUT_FILE
    stake_recommendations(shortlist, **settings).to_csv(path, index=False)
    return path
