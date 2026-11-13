"""Master shortlist reconciliation, in shadow (Phase 4, rule master-reconciliation-shadow-v1).

Sorts every candidate pick of a run by whether the research view (value shortlist) and the market view
(cagey tier) agree, scoring both on the same Pinnacle offer, and writes master_shortlist_reconciled.csv
beside the live master_shortlist.csv. Shadow only: the live master file, every probability, every pick and
every stake are untouched; this module only reads the run's decision rows and the live master frame.

Definitions and thresholds live in master_reconciliation_config.json (and docs/plan.md, Phase 4). The same
`classify` and `select` serve the live shadow and the offline backtest (evaluation_harness.py --mode master),
so the two can't drift apart.
"""
from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
from typing import Dict, Iterable, List, Mapping, Optional, Sequence

import numpy as np
import pandas as pd

CONFIG = Path(__file__).with_name('master_reconciliation_config.json')
KINDS = ('win', 'half_win', 'push', 'half_loss', 'loss')
GROUPS = ('missing_evidence', 'both_agree', 'research_edge', 'market_safe', 'conflict', 'neither')
EUROPEAN_SECTION = 'european_unvalidated'
NOT_EXECUTABLE = 'not_executable'
SECTIONS = (*GROUPS, EUROPEAN_SECTION, NOT_EXECUTABLE)
# Which groups can supply a match's pick, best first. Missing, Conflict, Neither and the European section never do.
PICK_PRIORITY = {'both_agree': 0, 'market_safe': 1, 'research_edge': 2}
RANKED = ('both_agree', 'market_safe')
TOLERANCE = 1e-9
DECISIONS = ('SHORTLISTED', 'BEYOND_TARGET', 'RESEARCH_EDGE_SECTION', 'NOT_SELECTED', 'LEFT_OUT',
             'MISSING_EVIDENCE', 'EUROPEAN_UNVALIDATED', 'NOT_EXECUTABLE')
IDENTITY_COLUMNS = ['kickoff_utc', 'league', 'home_team', 'away_team', 'fixture_id', 'market', 'market_to_bet',
                    'handicap_side', 'handicap_line', 'bookmaker', 'offered_decimal_odds', 'offered_last_update_utc',
                    'source_market', 'in_value_shortlist', 'in_cagey_tier']
CLASSIFICATION_COLUMNS = [
    'research_expected_return', 'research_profit_probability', 'research_no_loss_probability',
    'research_win_share', 'research_view', 'cagey_no_loss_probability', 'cagey_expected_return',
    'cagey_fair_odds', 'cagey_edge', 'market_safety', 'market_price', 'pinnacle_win_share',
    'disagreement_gap', 'disagreement', 'unvalidated_view', 'missing_evidence_reason', 'reconciled_group']
COLUMNS = ['reconciled_rank', 'reconciled_section', 'reconciled_section_rank', 'reconciled_decision',
           'reconciled_reason', *IDENTITY_COLUMNS, *CLASSIFICATION_COLUMNS,
           'in_live_master', 'live_master_rank', 'live_master_same_offer', 'reconciliation_version']


def load_config(path: Optional[Path] = None) -> Dict[str, object]:
    config = json.loads(Path(path or CONFIG).read_text(encoding='utf-8'))
    if config.get('version') != 'master-reconciliation-shadow-v1':
        raise ValueError('Unknown master reconciliation version')
    return config


def _number(value) -> Optional[float]:
    try:
        n = float(value)
    except (TypeError, ValueError):
        return None
    return n if math.isfinite(n) else None


def settlement_mass(values: Sequence) -> Optional[np.ndarray]:
    """A valid five-way settlement distribution (win, half win, push, half loss, loss), or None."""
    numbers = [_number(v) for v in values]
    if len(numbers) != 5 or any(n is None for n in numbers):
        return None
    mass = np.array(numbers, float)
    if (mass < -1e-12).any() or (mass > 1 + 1e-12).any() or abs(mass.sum() - 1) > 1e-6:
        return None
    win = mass[0] + mass[1] / 2
    return mass if win > 0 else None


def scored(mass: np.ndarray, price: float, cost: float) -> Dict[str, float]:
    """Expected return after cost, profit and no-loss probabilities, win share and fair odds of one view."""
    returns = np.array([price - 1, (price - 1) / 2, 0., -.5, -1.]) - cost
    win, loss = mass[0] + mass[1] / 2, mass[4] + mass[3] / 2
    return {'expected_return': float(mass @ returns), 'profit': float(mass[returns > 1e-12].sum()),
            'no_loss': float(mass[returns >= -1e-12].sum()), 'win_share': float(win / (win + loss)),
            'fair_odds': float(1 + loss / win)}


def classify(research: Optional[np.ndarray], cagey: Optional[np.ndarray], price: float, cost: float,
             pinnacle_win_share: Optional[float], *, european: bool, config: Mapping,
             research_reason: Optional[str] = None, cagey_reason: Optional[str] = None) -> Dict[str, object]:
    """Both views on one offer and its group, exactly as master_reconciliation_config.json defines them.

    `research` / `cagey` are the views' settlement distributions on this exact line, or None when that view
    can't score the offer (`*_reason` says why). A missing view makes the offer missing evidence; it is never
    counted as disagreement.
    """
    view = config['market_view']
    out: Dict[str, object] = dict.fromkeys(CLASSIFICATION_COLUMNS)
    out['unvalidated_view'] = bool(european)
    reasons = []
    if research is None:
        reasons.append('research: ' + (research_reason or 'settlement probabilities unavailable'))
    if cagey is None:
        reasons.append('cagey: ' + (cagey_reason or 'settlement probabilities unavailable'))
    if research is not None:
        r = scored(research, price, cost)
        edge = r['expected_return'] > config['research_edge']['min_expected_return_exclusive']
        loss = r['expected_return'] < config['research_loss']['max_expected_return_exclusive']
        out.update(research_expected_return=r['expected_return'], research_profit_probability=r['profit'],
                   research_no_loss_probability=r['no_loss'], research_win_share=r['win_share'],
                   research_view='edge' if edge else 'expects loss' if loss else 'no edge')
        if pinnacle_win_share is not None:
            gap = r['win_share'] - pinnacle_win_share
            out.update(pinnacle_win_share=pinnacle_win_share, disagreement_gap=gap,
                       disagreement=bool(abs(gap) + TOLERANCE >= config['disagreement']['min_abs_gap']))
    if cagey is not None:
        c = scored(cagey, price, cost)
        safe = c['no_loss'] + TOLERANCE >= view['safe']['min_no_loss']
        risky = c['no_loss'] < view['risky']['max_no_loss_exclusive']
        fair = price * (1 + view['fair']['pinnacle_average_margin']) + TOLERANCE >= c['fair_odds']
        out.update(cagey_no_loss_probability=c['no_loss'], cagey_expected_return=c['expected_return'],
                   cagey_fair_odds=c['fair_odds'], cagey_edge=price / c['fair_odds'] - 1,
                   market_safety='safe' if safe else 'risky' if risky else 'middle',
                   market_price='fairly priced' if fair else 'below fair')
    if reasons:
        # Missing evidence is never disagreement: the flag stays blank whatever the remaining view says.
        out.update(missing_evidence_reason='; '.join(reasons), reconciled_group='missing_evidence',
                   disagreement=None, disagreement_gap=None)
        return out
    edge, loss = out['research_view'] == 'edge', out['research_view'] == 'expects loss'
    safe, risky, fair = out['market_safety'] == 'safe', out['market_safety'] == 'risky', \
        out['market_price'] == 'fairly priced'
    out['reconciled_group'] = ('both_agree' if edge and (safe or fair) else
                               'research_edge' if edge else
                               'market_safe' if safe else
                               'conflict' if loss and risky else 'neither')
    return out


def section(group: str, european: bool, executable: bool, config: Mapping) -> str:
    if not executable:
        return NOT_EXECUTABLE
    if european and group in config['european']['kept_out_of']:
        return config['european']['kept_out_section']
    return group


def _tie_key(row: Mapping) -> tuple:
    def neg(name):
        value = _number(row.get(name))
        return -value if value is not None else math.inf
    return (neg('cagey_no_loss_probability'), neg('cagey_expected_return'), neg('research_expected_return'),
            neg('offered_decimal_odds'), str(row.get('kickoff_utc') or ''), str(row.get('league') or ''),
            str(row.get('home_team') or ''), str(row.get('away_team') or ''), str(row.get('market') or ''),
            str(row.get('handicap_side') or ''), _number(row.get('handicap_line')) or 0.)


def select(rows: List[Dict[str, object]], target: int, match_key: str = '_match') -> List[Dict[str, object]]:
    """One pick per match from its best group; the ranked list is the first `target` matches in Both agree,
    then Market-safe; the Research-edge section is listed by research expected return. Mutates and returns
    `rows`, adding reconciled_rank, reconciled_section_rank, reconciled_decision and reconciled_reason."""
    best: Dict[object, Dict[str, object]] = {}
    for row in rows:
        priority = PICK_PRIORITY.get(row['reconciled_section'])
        row.update(reconciled_rank=None, reconciled_section_rank=None)
        if priority is None:
            continue
        current = best.get(row[match_key])
        if current is None or (priority, _tie_key(row)) < (PICK_PRIORITY[current['reconciled_section']],
                                                           _tie_key(current)):
            best[row[match_key]] = row
    chosen = {id(r) for r in best.values()}
    ranked = sorted((r for r in best.values() if r['reconciled_section'] in RANKED),
                    key=lambda r: (PICK_PRIORITY[r['reconciled_section']], _tie_key(r)))
    for position, row in enumerate(ranked, 1):
        row['reconciled_section_rank'] = sum(1 for r in ranked[:position]
                                             if r['reconciled_section'] == row['reconciled_section'])
        if position <= target:
            row.update(reconciled_rank=position, reconciled_decision='SHORTLISTED', reconciled_reason='')
        else:
            row.update(reconciled_decision='BEYOND_TARGET', reconciled_reason=f'beyond the {target}-match target')
    edge = sorted((r for r in best.values() if r['reconciled_section'] == 'research_edge'),
                  key=lambda r: (-(_number(r.get('research_expected_return')) or 0.), _tie_key(r)))
    for position, row in enumerate(edge, 1):
        row.update(reconciled_section_rank=position, reconciled_decision='RESEARCH_EDGE_SECTION',
                   reconciled_reason='research edge, market below fair: separate section, not a ranked pick')
    for row in rows:
        if id(row) in chosen:
            continue
        name = row['reconciled_section']
        if name in PICK_PRIORITY:
            row.update(reconciled_decision='NOT_SELECTED', reconciled_reason='another offer chosen for this match')
        elif name == 'missing_evidence':
            row.update(reconciled_decision='MISSING_EVIDENCE', reconciled_reason=row.get('missing_evidence_reason'))
        elif name == EUROPEAN_SECTION:
            row.update(reconciled_decision='EUROPEAN_UNVALIDATED',
                       reconciled_reason='European fixture: unvalidated view, kept out of Both agree ranking')
        elif name == NOT_EXECUTABLE:
            row.update(reconciled_decision='NOT_EXECUTABLE')
        else:
            row.update(reconciled_decision='LEFT_OUT', reconciled_reason=f'{name}: left out by rule')
    return rows


# ---------------------------------------------------------------------------
# Live shadow: a pure function of one run's decision rows (and, for overlap only, its live master list)
# ---------------------------------------------------------------------------

def _flag(value) -> bool:
    return value is True or str(value).strip().lower() in ('true', '1')


def pool(decisions: pd.DataFrame) -> List[Dict[str, object]]:
    """Every offer either list shortlisted (the live master's starting union), in decision order."""
    if decisions is None or decisions.empty:
        return []
    records = decisions.astype(object).where(decisions.notna(), None).to_dict('records')
    return [r for r in records if r.get('decision') == 'SHORTLISTED' or r.get('cagey_tier_decision') == 'SHORTLISTED']


def executable(row: Mapping, config: Mapping) -> Optional[str]:
    """None when the offer meets the live master's execution rule, else the reason."""
    from master_selection_pinnacle_markets import allowed
    rule = config['execution']
    price = _number(row.get('offered_decimal_odds'))
    if row.get('bookmaker') != rule['bookmaker']:
        return 'bookmaker other than Pinnacle'
    if price is None or not rule['min_odds_exclusive'] < price <= rule['max_odds_inclusive']:
        return 'offered odds outside (1.15, 2.00]'
    if not allowed({**row, 'master_offer_source_market': row.get('source_market')}):
        return 'market outside the native Pinnacle master markets'
    return None


def research_view(row: Mapping):
    mass = settlement_mass([row.get('research_p_' + k) for k in KINDS])
    if mass is None:
        return None, 'research settlement probabilities unavailable (team or goal rates unknown to the research model)'
    return mass, None


def cagey_view(row: Mapping):
    mass = settlement_mass([row.get('cagey_p_' + k) for k in KINDS])
    if mass is None:
        return None, 'cagey settlement probabilities unavailable'
    if row.get('cagey_input_timing_status') != 'SYNCHRONIZED':
        return None, 'cagey Pinnacle inputs unavailable, stale or unsynchronized with the offer'
    return mass, None


def pinnacle_win_share(row: Mapping) -> Optional[float]:
    """Pinnacle's margin-free win share for this offer: 1 / fair odds when the fair reference is Pinnacle's own
    margin-free price (v27 reference types a and b); None otherwise (the flag is then unavailable)."""
    fair = _number(row.get('fair_odds'))
    if row.get('reference_type') not in ('a', 'b') or fair is None or fair <= 1:
        return None
    return 1 / fair


def reconcile(decisions: pd.DataFrame, live_master: Optional[pd.DataFrame] = None,
              config: Optional[Mapping] = None) -> pd.DataFrame:
    """The reconciled shadow list of one run: every pooled offer with both views, its group and decision.

    Reads only the run's decision rows; `live_master` (the run's master_shortlist.csv frame) is used for the
    overlap columns only and never changes a group, a rank or a decision.
    """
    from performance_tracking import fixture_key
    config = config or load_config()
    european = set(config['european']['leagues'])
    rows = []
    for record in pool(decisions):
        price = _number(record.get('offered_decimal_odds'))
        cost = _number(record.get('per_stake_cost')) or 0.
        research, research_reason = research_view(record)
        cagey, cagey_reason = cagey_view(record)
        blocked = executable(record, config)
        is_european = record.get('league') in european
        if price is None or price <= 1:
            research = cagey = None
            research_reason = cagey_reason = 'no valid offered price'
        row = {k: record.get(k) for k in IDENTITY_COLUMNS}
        row.update(in_value_shortlist=record.get('decision') == 'SHORTLISTED',
                   in_cagey_tier=record.get('cagey_tier_decision') == 'SHORTLISTED')
        row.update(classify(research, cagey, price or 0., cost, pinnacle_win_share(record), european=is_european,
                            config=config, research_reason=research_reason, cagey_reason=cagey_reason))
        row['reconciled_section'] = section(row['reconciled_group'], is_european, blocked is None, config)
        row['_match'] = fixture_key(record)
        if blocked is not None:
            row['reconciled_reason'] = blocked
        rows.append(row)
    select(rows, int(config['target_fixtures']))
    for row in rows:
        if row['reconciled_decision'] == 'NOT_EXECUTABLE' and not row.get('reconciled_reason'):
            row['reconciled_reason'] = 'not executable'
    frame = pd.DataFrame(rows, columns=[*COLUMNS, '_match'])
    frame['reconciliation_version'] = config['version']
    frame = overlap(frame, live_master)
    order = frame.assign(_rank=pd.to_numeric(frame.reconciled_rank, errors='coerce'),
                         _sec=frame.reconciled_section.map({s: i for i, s in enumerate(
                             ('both_agree', 'market_safe', 'research_edge', EUROPEAN_SECTION, 'missing_evidence',
                              'conflict', 'neither', NOT_EXECUTABLE))}),
                         _srank=pd.to_numeric(frame.reconciled_section_rank, errors='coerce'))
    order = order.sort_values(['_rank', '_sec', '_srank', 'kickoff_utc', 'league', 'home_team', 'away_team',
                               'market'], na_position='last', kind='stable')
    return order.reindex(columns=COLUMNS).reset_index(drop=True)


def _offer_key(row: Mapping) -> tuple:
    line = _number(row.get('handicap_line'))
    return (str(row.get('market') or ''), str(row.get('handicap_side') or ''),
            None if line is None else round(line, 4), round(_number(row.get('offered_decimal_odds')) or 0., 6))


def overlap(frame: pd.DataFrame, live_master: Optional[pd.DataFrame]) -> pd.DataFrame:
    from performance_tracking import fixture_key
    frame = frame.copy()
    frame['in_live_master'], frame['live_master_rank'], frame['live_master_same_offer'] = False, None, False
    if live_master is None or live_master.empty or frame.empty:
        return frame.drop(columns=['_match'], errors='ignore')
    live = {}
    for r in live_master.astype(object).where(live_master.notna(), None).to_dict('records'):
        live[fixture_key(r)] = (r.get('master_rank'), _offer_key(r))
    hits = [live.get(m) for m in frame['_match']]
    frame['in_live_master'] = [h is not None for h in hits]
    frame['live_master_rank'] = [h[0] if h else None for h in hits]
    frame['live_master_same_offer'] = [bool(h) and h[1] == _offer_key(r)
                                       for h, r in zip(hits, frame.to_dict('records'))]
    return frame.drop(columns=['_match'])


def summary(frame: pd.DataFrame, live_master: Optional[pd.DataFrame] = None, config: Optional[Mapping] = None,
            generated_at_utc: Optional[str] = None, top: int = 15) -> Dict[str, object]:
    from performance_tracking import fixture_key
    config = config or load_config()
    ranked = frame.loc[frame.reconciled_decision.eq('SHORTLISTED')]
    keys = lambda f: {fixture_key(r) for r in f.astype(object).where(f.notna(), None).to_dict('records')}
    live = live_master if live_master is not None else pd.DataFrame()
    live_keys, ranked_keys = (keys(live) if len(live) else set()), keys(ranked) if len(ranked) else set()
    counts = lambda column, names: {n: int(frame[column].eq(n).sum()) for n in names}
    picks = [{k: (None if pd.isna(r[k]) else r[k]) for k in
              ('reconciled_rank', 'reconciled_section', 'kickoff_utc', 'league', 'home_team', 'away_team',
               'market_to_bet', 'offered_decimal_odds', 'research_expected_return', 'cagey_no_loss_probability',
               'market_price', 'disagreement', 'unvalidated_view', 'in_live_master', 'live_master_same_offer')}
             for r in ranked.head(top).to_dict('records')]
    pooled = frame.loc[~frame.reconciled_section.eq(NOT_EXECUTABLE)]
    return {
        'version': config['version'], 'status': config['status'], 'generated_at_utc': generated_at_utc,
        'config_sha256': hashlib.sha256(json.dumps(config, sort_keys=True).encode()).hexdigest(),
        'target_fixtures': int(config['target_fixtures']), 'ranked_fixtures': int(len(ranked)),
        'shortfall': max(0, int(config['target_fixtures']) - int(len(ranked))),
        'pooled_offers': int(len(frame)), 'pooled_matches': int(frame[['league', 'home_team', 'away_team',
                                                                      'kickoff_utc']].drop_duplicates().shape[0])
        if len(frame) else 0,
        'offers_by_group': counts('reconciled_group', GROUPS),
        'offers_by_section': counts('reconciled_section', SECTIONS),
        'decisions': counts('reconciled_decision', DECISIONS),
        'ranked_by_group': {g: int(ranked.reconciled_section.eq(g).sum()) for g in RANKED},
        'research_edge_section_matches': int(frame.reconciled_decision.eq('RESEARCH_EDGE_SECTION').sum()),
        'disagreement_flags': int(pooled.disagreement.eq(True).sum()),
        'disagreement_unavailable': int(pooled.disagreement.isna().sum()),
        'european_rows': int(frame.unvalidated_view.eq(True).sum()),
        'european_kept_out': int(frame.reconciled_section.eq(EUROPEAN_SECTION).sum()),
        'overlap_with_live_master': {
            'live_master_fixtures': len(live_keys), 'reconciled_fixtures': len(ranked_keys),
            'same_fixture': len(live_keys & ranked_keys),
            'same_offer': int(ranked.live_master_same_offer.eq(True).sum()),
            'live_only': len(live_keys - ranked_keys), 'reconciled_only': len(ranked_keys - live_keys)},
        'top_picks': picks,
        'note': 'Shadow only: master_shortlist.csv, every probability, pick and stake are unchanged. '
                'Market-view thresholds and ranking are proposed, for Paul\'s approval.'}


def write_shadow(decisions: pd.DataFrame, out_dir, live_master: Optional[pd.DataFrame] = None,
                 generated_at_utc: Optional[str] = None) -> pd.DataFrame:
    """Write the reconciled CSV and its summary beside master_shortlist.csv. Never touches the live files."""
    config = load_config()
    frame = reconcile(decisions, live_master, config)
    frame.to_csv(Path(out_dir) / config['file'], index=False)
    (Path(out_dir) / config['summary_file']).write_text(
        json.dumps(summary(frame, live_master, config, generated_at_utc), indent=2, default=str) + '\n',
        encoding='utf-8')
    return frame


def remove_shadow(out_dir) -> None:
    config = load_config()
    for name in (config['file'], config['summary_file']):
        (Path(out_dir) / name).unlink(missing_ok=True)
