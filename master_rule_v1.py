"""PR #171's master rule (master-new-paul-rule-v1), frozen: the offline comparison only.

Superseded on 13 Nov 2026 by the revised rule (master-new-evidence-rule-v2, master_reconciliation.py). This is a
verbatim copy of #171's `classify`, `_tie_key` and `select` (origin/main f9af693), so the backtest
(evaluation_harness.py --mode master) can compare the revised rule with it on the same offers. The live run never
imports this module. Its thresholds are #171's: the market view and research edge are unchanged in
master_reconciliation_config.json, and the 4-point gap is in its `previous_rule` block (`config()` below).
"""
from __future__ import annotations

import math
from typing import Dict, List, Mapping, Optional

import numpy as np

from master_reconciliation import TOLERANCE, _number, load_config, scored

VERSION = 'master-new-paul-rule-v1'
GROUPS = ('both_agree', 'market_safe', 'left_out')
RANKED = ('both_agree', 'market_safe')
PRIORITY = {'both_agree': 0, 'market_safe': 1}
CLASSIFICATION_COLUMNS = [
    'research_no_loss_probability', 'cagey_no_loss_probability', 'gap_points', 'gap_check',
    'pinnacle_no_loss_probability', 'pinnacle_fair_odds', 'pinnacle_gap_points',
    'research_expected_return', 'research_edge', 'cagey_expected_return', 'cagey_fair_odds',
    'market_basis', 'market_safety', 'market_price', 'ranking_no_loss_probability',
    'one_view_missing', 'missing_view', 'missing_evidence_reason', 'unvalidated_view', 'new_master_group',
    'left_out_reason']


def config(current: Optional[Mapping] = None) -> Dict[str, object]:
    """#171's thresholds: the current config's market view and research edge (unchanged) with #171's gap."""
    current = current or load_config()
    previous = current['previous_rule']
    if previous['version'] != VERSION:
        raise ValueError('Unknown previous master rule')
    return {'version': VERSION, 'gap': previous['gap'], 'market_view': current['market_view'],
            'research_edge': current['research_edge']}


def classify(research: Optional[np.ndarray], cagey: Optional[np.ndarray], price: float, cost: float,
             pinnacle_no_loss: Optional[float] = None, pinnacle_fair_odds: Optional[float] = None, *,
             european: bool, config: Mapping, research_reason: Optional[str] = None,
             cagey_reason: Optional[str] = None, veto: bool = True, ignore: bool = True) -> Dict[str, object]:
    """Both views on one offer, its gap check and its group, exactly as master_reconciliation_config.json says.

    `research` / `cagey` are the views' settlement distributions on this exact line, or None when that view
    can't score the offer (`*_reason` says why). `pinnacle_no_loss` / `pinnacle_fair_odds` are Pinnacle's
    margin-free no-loss probability and fair odds for the same bet (the fallback when a view is missing).
    `veto` / `ignore` switch the two halves of the 4-point check off; only the offline backtest does that, to
    measure what the check does (the live shadow always applies both).
    """
    gap, view, edge_rule = config['gap'], config['market_view'], config['research_edge']
    out: Dict[str, object] = dict.fromkeys(CLASSIFICATION_COLUMNS)
    out.update(unvalidated_view=bool(european), one_view_missing=False)
    pin = _number(pinnacle_no_loss)
    pin = pin if pin is not None and 0 <= pin <= 1 else None
    pin_fair = _number(pinnacle_fair_odds)
    pin_fair = pin_fair if pin_fair is not None and pin_fair > 1 else None
    out.update(pinnacle_no_loss_probability=pin, pinnacle_fair_odds=pin_fair)
    r = scored(research, price, cost) if research is not None else None
    c = scored(cagey, price, cost) if cagey is not None else None
    if r is not None:
        out.update(research_no_loss_probability=r['no_loss'], research_expected_return=r['expected_return'],
                   research_edge=bool(r['expected_return'] > edge_rule['min_expected_return_exclusive']))
    if c is not None:
        out.update(cagey_no_loss_probability=c['no_loss'], cagey_expected_return=c['expected_return'],
                   cagey_fair_odds=c['fair_odds'])
    reasons = []
    if r is None:
        reasons.append('research: ' + (research_reason or 'settlement probabilities unavailable'))
    if c is None:
        reasons.append('cagey: ' + (cagey_reason or 'settlement probabilities unavailable'))
    if reasons:
        out['missing_evidence_reason'] = '; '.join(reasons)

    def left(check, reason):
        out.update(gap_check=check, new_master_group='left_out', left_out_reason=reason)
        return out

    if r is None and c is None:
        out['missing_view'] = 'both'
        return left('no_view', 'no view')
    # The market view: the cagey tier's figures, or Pinnacle's margin-free ones when the cagey score is missing.
    basis, chance, fair_odds = ('cagey', c['no_loss'], c['fair_odds']) if c is not None else \
        ('pinnacle', pin, pin_fair)
    if chance is not None:
        safe = chance + TOLERANCE >= view['safe']['min_no_loss']
        risky = chance < view['risky']['max_no_loss_exclusive']
        fair = fair_odds is not None and \
            price * (1 + view['fair']['pinnacle_average_margin']) + TOLERANCE >= fair_odds
        out.update(market_basis=basis, ranking_no_loss_probability=chance,
                   market_safety='safe' if safe else 'risky' if risky else 'middle',
                   market_price='fair' if fair else 'below fair')
    if r is not None and c is not None:
        g = 100 * (r['no_loss'] - c['no_loss'])
        out['gap_points'] = g
        if g + TOLERANCE >= gap['too_optimistic_min_points'] and ignore:
            return left('ignored', 'ignored')
        if g - TOLERANCE <= gap['too_pessimistic_max_points'] and veto:
            return left('vetoed', 'vetoed')
        out['gap_check'] = 'kept'
    else:
        existing = r if r is not None else c
        out.update(one_view_missing=True, missing_view='cagey' if c is None else 'research')
        if pin is None:
            return left('one_view_missing_no_pinnacle', 'one view missing: no Pinnacle reference')
        out['pinnacle_gap_points'] = 100 * (existing['no_loss'] - pin)
        if abs(out['pinnacle_gap_points']) + TOLERANCE >= gap['too_optimistic_min_points']:
            return left('one_view_missing_apart', 'one view missing: 4+ points from Pinnacle')
        out['gap_check'] = 'one_view_missing_kept'
    edge = bool(out['research_edge'])
    # Both agree needs both views on a validated fixture: never with a missing cagey score, never in Europe.
    can_agree = basis == 'cagey' and r is not None and not european
    if risky:
        return left(out['gap_check'], 'risky')
    if edge and (safe or fair) and can_agree:
        out['new_master_group'] = 'both_agree'
    elif safe:
        out['new_master_group'] = 'market_safe'
    else:
        return left(out['gap_check'], 'neither safe nor fair with a research edge')
    return out


def _tie_key(row: Mapping) -> tuple:
    chance = _number(row.get('ranking_no_loss_probability'))
    odds = _number(row.get('offered_decimal_odds'))
    # Rounded so that equal chances computed by different paths (e.g. AH +0.25 and 1X) tie and go to the odds.
    return (PRIORITY.get(row.get('new_master_group'), 9), -round(chance, 9) if chance is not None else math.inf,
            -odds if odds is not None else math.inf, str(row.get('kickoff_utc') or ''), str(row.get('league') or ''),
            str(row.get('home_team') or ''), str(row.get('away_team') or ''), str(row.get('market') or ''),
            str(row.get('handicap_side') or ''), _number(row.get('handicap_line')) or 0.)


def select(rows: List[Dict[str, object]], target: int, match_key: str = '_match', prefix: str = 'new_master'
           ) -> List[Dict[str, object]]:
    """One pick per match from its best group, then by no-loss chance; the list is the first `target` matches,
    Both agree first, then Market-safe. Rows with `<prefix>_executable` False are never picked. Mutates and
    returns `rows`, adding <prefix>_rank, <prefix>_decision and <prefix>_reason (`<prefix>_group` is read)."""
    group, rank, decision, reason = (f'{prefix}_{k}' for k in ('group', 'rank', 'decision', 'reason'))
    best: Dict[object, Dict[str, object]] = {}
    for row in rows:
        row[rank] = None
        if row.get(f'{prefix}_executable', True) is False or row[group] not in PRIORITY:
            continue
        current = best.get(row[match_key])
        if current is None or _tie_key({**row, 'new_master_group': row[group]}) < \
                _tie_key({**current, 'new_master_group': current[group]}):
            best[row[match_key]] = row
    chosen = {id(r) for r in best.values()}
    ranked = sorted(best.values(), key=lambda r: _tie_key({**r, 'new_master_group': r[group]}))
    for position, row in enumerate(ranked, 1):
        if position <= target:
            row.update({rank: position, decision: 'SHORTLISTED', reason: ''})
        else:
            row.update({decision: 'BEYOND_TARGET', reason: f'beyond the {target}-match target'})
    for row in rows:
        if id(row) in chosen:
            continue
        if row.get(f'{prefix}_executable', True) is False:
            row.update({decision: 'NOT_EXECUTABLE', reason: row.get(reason) or 'not executable'})
        elif row[group] in PRIORITY:
            row.update({decision: 'NOT_SELECTED', reason: 'another offer chosen for this match'})
        else:
            row.update({decision: 'LEFT_OUT', reason: row.get('left_out_reason') or 'left out by rule'})
    return rows
