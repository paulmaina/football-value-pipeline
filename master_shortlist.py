"""Master shortlist: the 10 best bets of one v28 run, one per match (value safest first, then fill).

Pool: every candidate the run evaluated (value tier and cagey tier share the same
candidate rows: every AH line, home/away win, double chance and, under the
per-market rule, over 1.5) at the allowed bookmakers (Pinnacle, 1xBet) that
passed the data checks. A candidate may fail only on price:
  * "edge below N%" (v27/v28 thresholds), or
  * "expected profit after stake cost below 0" (execution v2).
Any other reason (kick-off outside the 20-minute to 48-hour window, stale or
unsynchronised quotes, no Pinnacle reference, Pinnacle overround, odds above
3.00, price above 1.15 x fair, unavailable settlement inputs, ...) excludes it.

Value: edge >= 1% against the candidate's fair reference (Pinnacle a/b, the
market-implied fit c, or the cagey-corrected fit c-cagey, all treated alike)
and no stake-cost rejection. Everything else in the pool is "below fair".

Selection (deterministic):
  1. per match, the best candidate: value before below fair; among value bets
     the highest no-loss probability (safest), then the higher edge; among
     below-fair bets the price closest to fair (highest edge), then safest;
     then the higher odds;
  2. matches ordered the same way; the first 10 are the master shortlist.
Value bets always come first; below-fair bets only fill the list up to 10.
Fewer than 10 rows only when fewer than 10 matches have a candidate in the pool.

The list is recomputed by workflow_checks from the replayed decisions and is
information for a manual decision: it changes no other list or stake.
"""
from __future__ import annotations

from typing import Dict, List, Mapping

import numpy as np
import pandas as pd

VERSION = 'master-10-v1'
FILE = 'master_shortlist.csv'
SIZE = 10
MIN_EDGE = 0.01
TOLERANCE = 1e-9
PRICE_VALUE = 'value'
PRICE_BELOW_FAIR = 'below fair'
COST_REASON = 'expected profit after stake cost below 0'
NOT_SELECTED_PREFIX = 'other qualifying line chosen for this fixture'
COLUMNS = ['master_rank', 'kickoff_utc', 'league', 'home_team', 'away_team', 'fixture_id', 'market_to_bet',
           'market', 'value_market_group', 'handicap_side', 'handicap_line', 'bookmaker', 'offered_decimal_odds',
           'fair_odds', 'minimum_odds_master', 'edge', 'reference_type', 'master_no_loss_probability',
           'master_price_flag', 'p_narrow', 'in_value_shortlist', 'in_cagey_tier', 'per_stake_cost',
           'offered_last_update_utc', 'pinnacle_last_update_utc', 'evaluated_at_utc', 'selection_policy_version',
           'master_version']


def _reasons(text) -> List[str]:
    return [r for r in str(text or '').split('; ') if r and r != 'nan']


def price_only(reasons: List[str]) -> bool:
    """True when every rejection reason is about the price, never about the data."""
    return all(r.startswith('edge below ') or r == COST_REASON or r.startswith(NOT_SELECTED_PREFIX) for r in reasons)


def _number(series: pd.Series) -> pd.Series:
    return pd.to_numeric(series, errors='coerce')


def pool(decisions: pd.DataFrame) -> pd.DataFrame:
    """Candidates that passed the data checks, with their value flag and safety."""
    if decisions is None or decisions.empty:
        return pd.DataFrame()
    frame = decisions.copy()
    price, edge = _number(frame.get('offered_decimal_odds')), _number(frame.get('edge'))
    reasons = frame.get('rejection_reasons', pd.Series('', index=frame.index)).map(_reasons)
    usable = price.notna() & edge.notna() & frame.get('reference_type').notna() & reasons.map(price_only)
    frame = frame.loc[usable].copy()
    if frame.empty:
        return frame
    reasons = reasons.loc[frame.index]
    value = (_number(frame.edge) + TOLERANCE >= MIN_EDGE) & ~reasons.map(lambda r: COST_REASON in r)
    frame['master_price_flag'] = np.where(value, PRICE_VALUE, PRICE_BELOW_FAIR)
    safety = _number(frame.get('pinnacle_no_loss_probability'))
    if 'corrected_no_loss_probability' in frame:
        safety = safety.fillna(_number(frame['corrected_no_loss_probability']))
    frame['master_no_loss_probability'] = safety
    return frame


def _order(frame: pd.DataFrame) -> pd.DataFrame:
    """Value bets first, safest first (then edge); fill bets next, closest to fair first (then safest).

    Odds descending and stable keys break any remaining ties deterministically.
    """
    value = frame.master_price_flag == PRICE_VALUE
    safe = frame.master_no_loss_probability.astype(float).fillna(-1.0)
    edge = _number(frame.edge)
    return frame.assign(
        _value=value.astype(int), _first=np.where(value, safe, edge), _second=np.where(value, edge, safe),
        _odds=_number(frame.offered_decimal_odds),
    ).sort_values(['_value', '_first', '_second', '_odds', 'kickoff_utc', 'market', 'bookmaker'],
                  ascending=[False, False, False, False, True, True, True], kind='stable')


def build(decisions: pd.DataFrame) -> pd.DataFrame:
    """The master shortlist of one run (empty frame with COLUMNS when nothing qualifies)."""
    from performance_tracking import fixture_key
    candidates = pool(decisions)
    if candidates.empty:
        return pd.DataFrame(columns=COLUMNS)
    candidates['_fixture'] = candidates.apply(fixture_key, axis=1)
    best = _order(candidates).drop_duplicates('_fixture')
    top = _order(best).head(SIZE).copy()
    fair = _number(top.fair_odds)
    score = _number(top.get('corrected_cagey_score', pd.Series(np.nan, index=top.index)))
    top['master_rank'] = range(1, len(top) + 1)
    top['minimum_odds_master'] = fair * (1 + MIN_EDGE)
    top['p_narrow'] = 1 - score
    top['in_value_shortlist'] = top.get('decision', pd.Series(index=top.index, dtype=object)).eq('SHORTLISTED')
    top['in_cagey_tier'] = top.get('cagey_tier_decision', pd.Series(index=top.index, dtype=object)).eq('SHORTLISTED')
    top['master_version'] = VERSION
    return top.reindex(columns=COLUMNS).reset_index(drop=True)


def summary(frame: pd.DataFrame) -> Dict[str, object]:
    flags = frame['master_price_flag'] if len(frame) else pd.Series(dtype=object)
    return {'version': VERSION, 'size': SIZE, 'n_bets': int(len(frame)),
            'value_bets': int((flags == PRICE_VALUE).sum()), 'below_fair_bets': int((flags == PRICE_BELOW_FAIR).sum()),
            'min_edge_for_value': MIN_EDGE,
            'rule': 'the run\'s evaluated candidates that passed the data checks (a candidate may fail only on price); '
                    'one per match: value bets (edge >= 1% vs their fair reference) first, safest first; then '
                    'below-fair bets closest to fair price first; first 10 matches; fewer only when fewer matches '
                    'qualify'}


def matches(frame: pd.DataFrame, expected: pd.DataFrame) -> bool:
    """Same picks in the same order (prices and flags), for the replay check."""
    keys = ['master_rank', 'league', 'home_team', 'away_team', 'market_to_bet', 'bookmaker', 'master_price_flag']
    if len(frame) != len(expected):
        return False
    if not len(frame):
        return True
    left, right = frame.reindex(columns=keys).astype(str), expected.reindex(columns=keys).astype(str)
    if not left.reset_index(drop=True).equals(right.reset_index(drop=True)):
        return False
    return bool(np.allclose(_number(frame.offered_decimal_odds).to_numpy(float),
                            _number(expected.offered_decimal_odds).to_numpy(float), rtol=0, atol=1e-9))


def write(decisions: pd.DataFrame, out_dir, run_summary: Mapping) -> pd.DataFrame:
    """Write FILE and record the master summary in the run summary (mutates `run_summary`)."""
    from pathlib import Path
    frame = build(decisions)
    frame.to_csv(Path(out_dir) / FILE, index=False)
    run_summary['master_shortlist'] = summary(frame)
    return frame
