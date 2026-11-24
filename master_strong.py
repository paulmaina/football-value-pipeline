"""The strong-team master, in shadow (rule master-strong-team-v1; master_strong_config.json; docs/plan.md Phase 4c).

Decided by Paul on 23 Nov 2026: at most 6 picks per market group (match result, double chance, Asian handicap), 15
matches, one pick per match. "Proven" picks come first: the market view (the cagey tier, or Pinnacle's margin-free
stand-in) rates the bet safe, the backed team is strong by Elo, it has a proven record on the exact bet over its last
ten matches, and (role R1) the research model's own expected margin also favours it after the line. Proven picks are
ranked by league trust (how well calibrated the cagey tier is in the league), then (role R2) whether the research
view confirms the bet, then the market chance of profit. If fewer than 15 matches have a proven pick, the live
master's fill steps (safe, fill, risky fill) complete the list under the same caps, labelled "not proven" (role R4
breaks near-ties in the chance-of-profit steps by the research chance of profit). UCL/UEL proven picks also need the
research view's no-loss >= 0.70 (role R3).

The pool, execution rule, quote timing and probabilities are exactly the live master's (master_reconciliation.offer_row),
so an offer the live master can't take is never taken here. The research view acts only through R1-R4, each kept only
if it passed its pass rule (master_strong_config.json research_roles; `active`).

Shadow only: master_shortlist_strong.csv beside the live files. It never changes master_shortlist.csv, a probability,
a pick or a stake. The same `annotate` and `select` serve the live shadow and the offline check
(master_strong_check.py), so the two can't drift apart.
"""
from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
from typing import Dict, List, Mapping, Optional

import numpy as np
import pandas as pd

import team_track_record as tr

CONFIG = Path(__file__).with_name('master_strong_config.json')
TRUST_FILE = Path(__file__).with_name('master_league_trust.json')
# Each superseded rule's config, frozen byte for byte, so archived runs replay under the rule they used.
RULES_DIR = Path(__file__).with_name('master_strong_rules')
# v2 (Paul, 24 Nov 2026; docs/plan.md Phase 4d, Part 1): the executable pool's odds floor is 1.20 (config 'execution').
# v3 (Part 2): research no-loss >= 0.70 for every pick in every tier (config 'research_gate'; R3 extended).
# v4 (Part 3): proven picks by Elo expected score, then record share, then chance of profit (config 'proven_order').
# v5 (Part 4): weak-link flags on the picks, flag only (config 'weak_links'; weak_links.py).
# v6 (Part 5): weak-link reasons (f) and (g) narrowed (weak_links 'f.tiers', 'g.counted_review_warnings').
VERSIONS = ('master-strong-team-v1', 'master-strong-team-v2', 'master-strong-team-v3', 'master-strong-team-v4',
            'master-strong-team-v5', 'master-strong-team-v6')
WEAK_COLUMNS = ['weak_link', 'weak_link_reasons']  # since v5 (config 'weak_links')
VERSION = VERSIONS[-1]
TRUST_ORDER = ('trusted', 'not trusted', 'unvalidated')
TIERS = ('proven', 'not proven: safe', 'not proven: fill', 'not proven: risky fill')
DECISIONS = ('SHORTLISTED', 'BEYOND_TARGET', 'NOT_SELECTED', 'LEFT_OUT', 'NOT_EXECUTABLE')
TOLERANCE = 1e-9
STRONG_COLUMNS = [
    'strong_market_group', 'strong_backed_side', 'strong_backed_team', 'strong_line', 'strong_bet_kind',
    'strong_safe', 'strong_elo_expectancy', 'strong_team_check', 'strong_record_matches', 'strong_record_won_share',
    'strong_record_not_lost_share', 'strong_record_check', 'strong_record_reason', 'strong_h2h_matches',
    'strong_h2h_won_share', 'strong_h2h_not_lost_share', 'strong_research_margin', 'strong_r1_check',
    'strong_research_confirms', 'strong_r3_check', 'research_profit_probability', 'strong_league_trust',
    'strong_proven', 'strong_failed_checks', 'strong_labels']
SELECTION_COLUMNS = ['strong_rank', 'strong_tier', 'strong_decision', 'strong_reason']
REPORTED_CLASSIFICATION = [
    'research_no_loss_probability', 'cagey_no_loss_probability', 'gap_points', 'pinnacle_no_loss_probability',
    'research_expected_return', 'cagey_expected_return', 'cagey_profit_probability', 'pinnacle_profit_probability',
    'line_type', 'probability_source', 'market_basis', 'market_safety', 'market_price', 'ranking_no_loss_probability',
    'ranking_profit_probability', 'new_master_labels', 'one_view_missing', 'unvalidated_view', 'timing_check']


def load_config(path: Optional[Path] = None, version: Optional[str] = None) -> Dict[str, object]:
    """The current rule's config (master_strong_config.json), or with `version` the config that rule used (an older
    rule's frozen copy in master_strong_rules/), so a run replays under the rule it recorded."""
    if path is None and version is not None and version != VERSION:
        if version not in VERSIONS:
            raise ValueError(f'Unknown strong master rule version {version!r}')
        path = RULES_DIR / f'{version}.json'
    config = json.loads(Path(path or CONFIG).read_text(encoding='utf-8'))
    if config.get('version') not in VERSIONS or (path is None and config['version'] != VERSION)             or (version is not None and config['version'] != version):
        raise ValueError('Unknown strong master rule version')
    return config


def execution_config(master_config: Mapping, config: Mapping) -> Dict[str, object]:
    """The live master rule's config (master_reconciliation) with this rule's own execution window, when it sets one
    (config 'execution', since master-strong-team-v2: odds above 1.20 up to 2.00). Rules without one use the live
    master's window unchanged (1.15 to 2.00)."""
    window = config.get('execution')
    if not window:
        return dict(master_config)
    return {**master_config, 'execution': {**master_config['execution'],
                                           'min_odds_exclusive': float(window['min_odds_exclusive']),
                                           'max_odds_inclusive': float(window['max_odds_inclusive'])}}


def _number(value) -> Optional[float]:
    try:
        n = float(value)
    except (TypeError, ValueError):
        return None
    return n if math.isfinite(n) else None


def settings(config: Mapping, **overrides) -> Dict[str, object]:
    """The thresholds and role switches a run uses: E, G and each role's `active` from the config (filled once by the
    offline check), with `overrides` (the offline check's candidates). Refuses to run while any is unset."""
    roles = config['research_roles']
    out = {'E': config['checks']['strong_team']['E'], 'G': roles['R1_research_strength']['G'],
           'R1': roles['R1_research_strength']['active'], 'R2': roles['R2_agreement_boost']['active'],
           'R3': roles['R3_european_second_opinion']['active'], 'R4': roles['R4_fill_tie_breaker']['active']}
    out.update(overrides)
    missing = [k for k, v in out.items() if v is None]
    if missing:
        raise ValueError(f"strong master thresholds not set ({', '.join(missing)}): run the offline check first "
                         f"(master_strong_check.py) and record its choices in the config")
    return out


def load_trust(path: Optional[Path] = None) -> Dict[str, str]:
    """League -> 'trusted' / 'not trusted', by harness key and display name (master_league_trust.json)."""
    path = Path(path or TRUST_FILE)
    if not path.exists():
        return {}
    data = json.loads(path.read_text(encoding='utf-8'))
    out = {}
    for key, entry in (data.get('leagues') or {}).items():
        out[key] = entry['status']
        if entry.get('name'):
            out[entry['name']] = entry['status']
    return out


def league_trust(league, trust: Mapping[str, str], european: bool) -> str:
    if european:
        return 'unvalidated'
    return trust.get(str(league or ''), 'not trusted')


def evidence_from_forecast(forecast: Optional[Mapping]) -> Dict[str, object]:
    """What a live forecast froze before kickoff: Elo expectancy, each side's last matches, head-to-head, history
    names and the research view's mean margin."""
    out = {'elo_home_expectancy': None, 'history': {}, 'teams': {}, 'h2h': [], 'research_margin': None}
    if forecast is None:
        return out
    out['elo_home_expectancy'] = forecast.get('elo_home_expectancy')
    for side in ('home', 'away'):
        rows, h2h, team = tr.history_from_forecast(forecast, side)
        out['history'][side], out['teams'][side], out['h2h'] = rows, team, h2h
    out['research_margin'] = tr.research_margin_from_forecast(forecast)
    return out


def annotate(row: Dict[str, object], evidence: Mapping, *, config: Mapping, trust: str, european: bool,
             E: float, G: float) -> Dict[str, object]:
    """The strong-team checks on one offer (already classified by master_reconciliation.classify), in place.

    Values behind every check are kept beside its pass/fail column. `proven` is computed by `proven()` from the
    checks and the run's role switches."""
    checks, roles = config['checks'], config['research_roles']
    row.update({k: None for k in STRONG_COLUMNS if k != 'research_profit_probability'})
    row['strong_league_trust'] = trust
    chance = _number(row.get('ranking_no_loss_probability'))
    row['strong_safe'] = chance is not None and chance + TOLERANCE >= checks['safe']['min_no_loss']
    backed = tr.backed_side(row.get('market'), row.get('handicap_side'), row.get('handicap_line'))
    if backed is None:
        row['strong_failed_checks'] = 'market outside the native master markets'
        return row
    side, line, group = backed
    row.update(strong_backed_side=side, strong_line=line, strong_market_group=group,
               strong_bet_kind='win' if tr.is_win_bet(line) else 'no loss')
    team = (evidence.get('teams') or {}).get(side) or row.get(f'{side}_team')
    row['strong_backed_team'] = row.get(f'{side}_team')
    elo = tr.elo_expectancy(evidence.get('elo_home_expectancy'), side)
    row['strong_elo_expectancy'] = elo
    row['strong_team_check'] = elo is not None and elo + TOLERANCE >= float(E)
    rule = checks['proven_record']
    record = tr.bet_record((evidence.get('history') or {}).get(side) or [], team, line, int(rule['matches']))
    passed, reason = tr.record_check(record, line, rule)
    row.update(strong_record_matches=record['matches'], strong_record_won_share=record['won_share'],
               strong_record_not_lost_share=record['not_lost_share'], strong_record_check=passed,
               strong_record_reason=reason)
    h2h = tr.bet_record(evidence.get('h2h') or [], team, line, 5)
    row.update(strong_h2h_matches=h2h['matches'], strong_h2h_won_share=h2h['won_share'],
               strong_h2h_not_lost_share=h2h['not_lost_share'])
    margin = tr.backed_margin(_number(evidence.get('research_margin')), side, line)
    row['strong_research_margin'] = margin
    row['strong_r1_check'] = margin is not None and margin + TOLERANCE >= float(G)
    r2 = roles['R2_agreement_boost']
    research = _number(row.get('research_no_loss_probability'))
    gap = _number(row.get('gap_points'))
    row['strong_research_confirms'] = bool(research is not None and gap is not None
                                           and research + TOLERANCE >= r2['min_research_no_loss']
                                           and gap > r2['min_gap_points_exclusive'] + TOLERANCE)
    gate = config.get('research_gate')
    if gate:  # since v3: every offer, domestic and European (R3 extended)
        row['strong_r3_check'] = research is not None and research + TOLERANCE >= gate['min_research_no_loss']
    elif european:
        r3 = roles['R3_european_second_opinion']
        row['strong_r3_check'] = research is not None and research + TOLERANCE >= r3['min_research_no_loss']
    return row


def research_gate_reason(row: Mapping, config: Mapping) -> Optional[str]:
    """Why the research gate (config 'research_gate', since v3) leaves the offer out, or None (eligible, or a rule
    without the gate)."""
    gate = config.get('research_gate')
    if not gate:
        return None
    research = _number(row.get('research_no_loss_probability'))
    if research is None:
        return 'no research view'
    if research + TOLERANCE < gate['min_research_no_loss']:
        return f"research no-loss below {gate['min_research_no_loss']:.2f}"
    return None


def failed_checks(row: Mapping, run: Mapping) -> List[str]:
    """The checks an offer fails, in the config's order, for the run's role switches."""
    out = []
    if not row.get('strong_safe'):
        out.append('safe (market no-loss below 0.75)')
    if row.get('strong_backed_side') is None:
        return out + ['market outside the native master markets']
    if not row.get('strong_team_check'):
        elo = row.get('strong_elo_expectancy')
        out.append('strong team (no Elo rating)' if elo is None else f"strong team (Elo {elo:.2f} below {run['E']:.2f})")
    if not row.get('strong_record_check'):
        out.append(f"record ({row.get('strong_record_reason')})")
    if run['R1'] and not row.get('strong_r1_check'):
        margin = row.get('strong_research_margin')
        out.append('research strength (no research view)' if margin is None else
                   f"research strength (margin {margin:+.2f} below {run['G']:+.2f})")
    if run.get('research_gate') and row.get('strong_r3_check') is False:
        out.append('research second opinion (research no-loss below 0.70 or no research view)')
    elif run['R3'] and row.get('strong_r3_check') is False:
        out.append('European second opinion (research no-loss below 0.70)')
    return out


def proven(row: Mapping, run: Mapping) -> bool:
    return not failed_checks(row, run)


def _tie_key(row: Mapping) -> tuple:
    """The live master's tie order after the probability: higher odds, kickoff, league, teams, market, side, line."""
    import master_reconciliation as mr
    return mr._tie_key(row)[1:]


def _trust_index(row: Mapping) -> int:
    return TRUST_ORDER.index(row.get('strong_league_trust') or 'not trusted')


def _profit(row: Mapping) -> float:
    p = _number(row.get('ranking_profit_probability'))
    return -round(p, 9) if p is not None else math.inf


def _no_loss(row: Mapping) -> float:
    p = _number(row.get('ranking_no_loss_probability'))
    return -round(p, 9) if p is not None else math.inf


def record_share(row: Mapping) -> Optional[float]:
    """The proven-record share on the exact bet: the won share for win bets, the not-lost share for no-loss bets."""
    column = 'strong_record_won_share' if row.get('strong_bet_kind') == 'win' else 'strong_record_not_lost_share'
    return _number(row.get(column))


def _higher_first(value: Optional[float]) -> float:
    return -round(value, 9) if value is not None else math.inf


def proven_key(row: Mapping, run: Mapping, config: Optional[Mapping] = None) -> tuple:
    """Step A's order. Since v4 (config 'proven_order'): Elo expected score, record share on the exact bet, market
    chance of profit, tie order. Before: league trust, (R2 active) research confirms, chance of profit, tie order."""
    if config is not None and config.get('proven_order'):
        return (_higher_first(_number(row.get('strong_elo_expectancy'))), _higher_first(record_share(row)),
                _profit(row), *_tie_key(row))
    confirms = 0 if run['R2'] and row.get('strong_research_confirms') else 1
    return (_trust_index(row), confirms, _profit(row), *_tie_key(row))


def fill_key(row: Mapping, run: Mapping, config: Mapping) -> tuple:
    """Fill and risky fill: league trust, then (R4 active) 2-point bands of the market chance of profit with the
    higher research chance of profit first, then the exact chance of profit and the tie order."""
    if run['R4']:
        width = float(config['research_roles']['R4_fill_tie_breaker']['band_width'])
        p = _number(row.get('ranking_profit_probability'))
        research = _number(row.get('research_profit_probability'))
        band = -math.floor(round(p / width, 9)) if p is not None else math.inf
        return (_trust_index(row), band, -research if research is not None else math.inf, _profit(row), *_tie_key(row))
    return (_trust_index(row), _profit(row), *_tie_key(row))


def select(rows: List[Dict[str, object]], config: Mapping, run: Mapping, match_key: str = '_match',
           executable_key: str = 'new_master_executable', nominated_key: str = 'new_master_nominated') -> List[Dict]:
    """Proven picks, then the not-proven fill, one pick per match, at most max_picks_per_market per market group and
    target_fixtures in all. Mutates and returns `rows` (strong_rank, strong_tier, strong_decision, strong_reason,
    strong_proven, strong_failed_checks, strong_labels)."""
    target, cap = int(config['target_fixtures']), int(config['max_picks_per_market'])
    floor_fill = 0.5
    run = {**run, 'research_gate': bool(config.get('research_gate'))}
    for row in rows:
        failed = failed_checks(row, run)
        row.update(strong_rank=None, strong_tier=None, strong_decision=None, strong_reason=None,
                   strong_proven=not failed, strong_failed_checks='; '.join(failed) or None)

    def eligible(r):
        return (r.get(executable_key, True) is not False and r.get(nominated_key, True) is not False
                and r.get('strong_market_group') is not None
                and _number(r.get('ranking_no_loss_probability')) is not None
                and _number(r.get('ranking_profit_probability')) is not None
                and research_gate_reason(r, config) is None)
    taken_matches, per_group, picks = set(), {}, 0

    def take(candidates, tier):
        nonlocal picks
        for row in candidates:
            if picks >= target:
                return
            if row[match_key] in taken_matches or per_group.get(row['strong_market_group'], 0) >= cap:
                continue
            taken_matches.add(row[match_key])
            per_group[row['strong_market_group']] = per_group.get(row['strong_market_group'], 0) + 1
            picks += 1
            row.update(strong_rank=picks, strong_tier=tier, strong_decision='SHORTLISTED', strong_reason='')

    pool = [r for r in rows if eligible(r)]
    take(sorted((r for r in pool if r['strong_proven']), key=lambda r: proven_key(r, run, config)), 'proven')
    chance = lambda r: _number(r.get('ranking_no_loss_probability'))
    take(sorted((r for r in pool if r['strong_safe']), key=lambda r: (_trust_index(r), _no_loss(r), *_tie_key(r))),
         'not proven: safe')
    take(sorted((r for r in pool if chance(r) + TOLERANCE >= floor_fill), key=lambda r: fill_key(r, run, config)),
         'not proven: fill')
    take(sorted(pool, key=lambda r: fill_key(r, run, config)), 'not proven: risky fill')
    for row in rows:
        labels = []
        if row['strong_decision'] is None:
            if row.get(executable_key, True) is False:
                row.update(strong_decision='NOT_EXECUTABLE',
                           strong_reason=row.get('new_master_reason') or 'not executable')
            elif not eligible(row):
                gate = research_gate_reason(row, config)
                row.update(strong_decision='LEFT_OUT', strong_reason='no market view or not a native master market'
                           if gate is None or not eligible({**row, 'research_no_loss_probability': 1.0})
                           else f'research gate: {gate}')
            elif row[match_key] in taken_matches:
                row.update(strong_decision='NOT_SELECTED', strong_reason='another offer chosen for this match')
            elif per_group.get(row['strong_market_group'], 0) >= cap:
                row.update(strong_decision='NOT_SELECTED',
                           strong_reason=f"market group full ({cap} {row['strong_market_group']} picks)")
            else:
                row.update(strong_decision='BEYOND_TARGET', strong_reason=f'beyond the {target}-match target')
        labels.append('proven' if row['strong_proven'] else 'not proven')
        if row.get('strong_research_confirms'):
            labels.append('research confirms' if run['R2'] else 'research confirms (label only)')
        if row.get('one_view_missing'):
            labels.append('one view missing')
        if row.get('strong_league_trust') != 'trusted':
            labels.append(f"league {row.get('strong_league_trust')}")
        row['strong_labels'] = '; '.join(labels)
    return rows


# ---------------------------------------------------------------------------
# Live shadow
# ---------------------------------------------------------------------------

def columns(config: Optional[Mapping] = None) -> List[str]:
    import master_reconciliation as mr
    config = config or load_config()
    return [*SELECTION_COLUMNS, *mr.IDENTITY_COLUMNS, *REPORTED_CLASSIFICATION, *STRONG_COLUMNS,
            'in_live_master', 'live_master_rank', 'live_master_same_offer', 'strong_master_version',
            *(WEAK_COLUMNS if config.get('weak_links') else [])]


def offer_rows(decisions: pd.DataFrame, predictions: Optional[pd.DataFrame], generated_at_utc,
               config: Mapping, trust: Optional[Mapping] = None) -> List[Dict[str, object]]:
    """Every nominated offer of one run as the live master's rule sees it (master_reconciliation.offer_row: identity,
    both views, timing, execution), with the strong-team checks and the selection."""
    import master_reconciliation as mr
    from master_selection import identity
    run = settings(config)
    trust = load_trust() if trust is None else trust
    mcfg = execution_config(mr.load_config(), config)
    european_leagues = set(mcfg['european']['leagues'])
    records = mr.pool(decisions)
    clock = mr.run_clock(mr._records(decisions), generated_at_utc)
    by_fixture, fits = mr.forecasts(predictions), {}
    weak = config.get('weak_links')
    rows = []
    for record in records:
        row = mr.offer_row(record, mcfg, clock, by_fixture, fits)
        mass, _ = mr.research_view(record)
        row['research_profit_probability'] = mr.profit_chance(mass) if mass is not None else None
        european = record.get('league') in european_leagues
        annotate(row, evidence_from_forecast(by_fixture.get(identity(record))), config=config,
                 trust=league_trust(record.get('league'), trust, european), european=european,
                 E=run['E'], G=run['G'])
        if weak:  # the weak-link flags' private inputs, dropped once the flags are set
            row.update(_forecast=by_fixture.get(identity(record)), _research_warnings=record.get('research_warnings'),
                       _cagey_fallback=record.get('cagey_correction_fallback'))
        rows.append(row)
    select(rows, config, run)
    if weak:
        import weak_links
        weak_links.annotate(rows, weak, E=run['E'], clock=clock)
        for row in rows:
            for key in ('_forecast', '_research_warnings', '_cagey_fallback'):
                row.pop(key, None)
    return rows


def reconcile(decisions: pd.DataFrame, predictions: Optional[pd.DataFrame] = None,
              live_master: Optional[pd.DataFrame] = None, generated_at_utc=None,
              config: Optional[Mapping] = None, trust: Optional[Mapping] = None) -> pd.DataFrame:
    """The strong master of one run in its shadow schema (columns()): every nominated offer with the strong-team checks
    and the selection. `live_master` (the run's master_shortlist.csv) is read for the overlap columns only."""
    config = config or load_config()
    rows = offer_rows(decisions, predictions, generated_at_utc, config, trust)
    if not rows:  # nothing nominated in this run: an empty list with the full schema
        return pd.DataFrame(columns=columns(config))
    frame = pd.DataFrame(rows)
    frame = overlap(frame, live_master)
    frame['strong_master_version'] = config['version']
    order = frame.assign(_rank=pd.to_numeric(frame.strong_rank, errors='coerce'),
                         _dec=frame.strong_decision.map({d: i for i, d in enumerate(DECISIONS)}),
                         _p=-pd.to_numeric(frame.ranking_profit_probability, errors='coerce').round(9),
                         _line=pd.to_numeric(frame.handicap_line, errors='coerce'))
    order = order.sort_values(['_rank', '_dec', '_p', 'kickoff_utc', 'league', 'home_team', 'away_team', 'market',
                               'handicap_side', '_line'], na_position='last', kind='stable')
    return order.reindex(columns=columns(config)).reset_index(drop=True)


STEP_OF_TIER = {tier: number for number, tier in enumerate(TIERS, start=1)}


def live_columns(config: Optional[Mapping] = None) -> List[str]:
    """The strong master's file when it is the live master_shortlist.csv (master_shortlist_config.json live "strong"):
    the live master file's columns (master_reconciliation.COLUMNS: new_master_rank, tier, step, decision and reason
    carry the strong selection; the classification columns are the live master rule's own, from offer_row), then the
    strong-team columns, then (since v5) weak_link and weak_link_reasons. The overlap columns (in_live_master, ...)
    compare with the baseline, today's master. `config`: the rule's (the current one when omitted)."""
    import master_reconciliation as mr
    config = config or load_config()
    extra = [c for c in (*STRONG_COLUMNS, *SELECTION_COLUMNS, 'strong_master_version') if c not in mr.COLUMNS]
    return [*mr.COLUMNS, *extra, *(WEAK_COLUMNS if config.get('weak_links') else [])]


def live_frame(decisions: pd.DataFrame, predictions: Optional[pd.DataFrame] = None,
               baseline: Optional[pd.DataFrame] = None, generated_at_utc=None, version: str = VERSION,
               config: Optional[Mapping] = None, trust: Optional[Mapping] = None) -> pd.DataFrame:
    """The strong master as the live list: every nominated offer in live_columns(), with the strong selection written
    into the new_master_* selection columns (rank, tier, step, decision, reason) and `version` in new_master_version.
    `baseline` (today's master, master_reconciliation.reconcile's frame) is read for the overlap columns only."""
    config = config or load_config()
    rows = offer_rows(decisions, predictions, generated_at_utc, config, trust)
    if not rows:
        return pd.DataFrame(columns=live_columns(config))
    for row in rows:
        row.update(new_master_rank=row['strong_rank'], new_master_tier=row['strong_tier'],
                   new_master_step=STEP_OF_TIER.get(row['strong_tier']), new_master_decision=row['strong_decision'],
                   new_master_reason=row['strong_reason'], risky_fill=row['strong_tier'] == TIERS[-1],
                   strong_master_version=config['version'])
    frame = overlap(pd.DataFrame(rows), baseline)
    frame['new_master_version'] = version
    return frame.reindex(columns=live_columns(config))


def _offer_key(row: Mapping) -> tuple:
    line = _number(row.get('handicap_line'))
    return (str(row.get('market') or ''), str(row.get('handicap_side') or ''),
            None if line is None else round(line, 4), round(_number(row.get('offered_decimal_odds')) or 0., 6))


def overlap(frame: pd.DataFrame, live_master: Optional[pd.DataFrame]) -> pd.DataFrame:
    from performance_tracking import fixture_key
    frame = frame.copy()
    frame['in_live_master'], frame['live_master_rank'], frame['live_master_same_offer'] = False, None, False
    if live_master is None or live_master.empty or frame.empty:
        return frame
    live = {}
    rank_column = 'new_master_rank' if 'new_master_rank' in live_master else 'master_rank'
    for r in live_master.astype(object).where(live_master.notna(), None).to_dict('records'):
        if r.get(rank_column) is None or (r.get('new_master_decision') not in (None, 'SHORTLISTED')):
            continue
        live[fixture_key(r)] = (r.get(rank_column), _offer_key(r))
    hits = [live.get(m) for m in frame['_match']]
    frame['in_live_master'] = [h is not None for h in hits]
    frame['live_master_rank'] = [h[0] if h else None for h in hits]
    frame['live_master_same_offer'] = [bool(h) and h[1] == _offer_key(r) for h, r in zip(hits, frame.to_dict('records'))]
    return frame


def summary(frame: pd.DataFrame, config: Optional[Mapping] = None, generated_at_utc=None) -> Dict[str, object]:
    config = config or load_config()
    run = settings(config)
    picks = frame.loc[frame.strong_decision.eq('SHORTLISTED')] if len(frame) else frame
    eligible = frame.loc[~frame.strong_decision.isin(['NOT_EXECUTABLE', 'LEFT_OUT'])] if len(frame) else frame
    target = int(config['target_fixtures'])
    groups = ('match_result', 'double_chance', 'asian_handicap')
    count = lambda f, column, names: {n: int(f[column].eq(n).sum()) for n in names} if len(f) else dict.fromkeys(names, 0)
    keep = ('strong_rank', 'strong_tier', 'kickoff_utc', 'league', 'home_team', 'away_team', 'market_to_bet',
            'offered_decimal_odds', 'ranking_no_loss_probability', 'ranking_profit_probability',
            'research_no_loss_probability', 'strong_elo_expectancy', 'strong_record_reason', 'strong_research_margin',
            'strong_league_trust', 'strong_labels', 'strong_failed_checks', 'in_live_master', 'live_master_same_offer')
    clean = lambda r: {k: (None if pd.isna(r.get(k)) else r.get(k)) for k in keep}
    failed = {}
    for text in (eligible.strong_failed_checks.dropna() if len(eligible) else []):
        for item in str(text).split('; '):
            name = item.split(' (')[0]
            failed[name] = failed.get(name, 0) + 1
    matches = (eligible[['league', 'home_team', 'away_team', 'kickoff_utc']].drop_duplicates().shape[0]
               if len(eligible) else 0)
    shortfall = max(0, target - len(picks))
    return {
        'version': config['version'], 'status': config['status'], 'generated_at_utc': generated_at_utc,
        'config_sha256': hashlib.sha256(json.dumps(config, sort_keys=True).encode()).hexdigest(),
        'settings': {k: v for k, v in run.items()},
        'target_fixtures': target, 'max_picks_per_market': int(config['max_picks_per_market']),
        'ranked_fixtures': int(len(picks)), 'shortfall': shortfall,
        'short_reason': None if not shortfall else (
            f'the nominations give only {matches} matches with an eligible offer' if matches < target else
            'market group caps leave no eligible offer for the remaining matches'),
        'picks_by_tier': count(picks, 'strong_tier', TIERS),
        'picks_by_market_group': count(picks, 'strong_market_group', groups),
        'picks_by_league_trust': count(picks, 'strong_league_trust', TRUST_ORDER),
        'eligible_offers': int(len(eligible)), 'eligible_matches': int(matches),
        'proven_offers': int(eligible.strong_proven.eq(True).sum()) if len(eligible) else 0,
        'proven_matches': int(eligible.loc[eligible.strong_proven.eq(True), ['league', 'home_team', 'away_team',
                                                                            'kickoff_utc']].drop_duplicates().shape[0])
        if len(eligible) else 0,
        'failed_checks_on_eligible_offers': failed,
        'research_confirms_picks': int(picks.strong_research_confirms.eq(True).sum()) if len(picks) else 0,
        'european_picks': int(picks.unvalidated_view.eq(True).sum()) if len(picks) else 0,
        'overlap_with_live_master': {
            'same_fixture': int(picks.in_live_master.eq(True).sum()) if len(picks) else 0,
            'same_offer': int(picks.live_master_same_offer.eq(True).sum()) if len(picks) else 0},
        'decisions': count(frame, 'strong_decision', DECISIONS),
        'picks': [clean(r) for r in picks.to_dict('records')],
        'note': 'Shadow only: master_shortlist.csv, every probability, pick and stake are unchanged.',
        **({'execution': {k: config['execution'][k] for k in ('min_odds_exclusive', 'max_odds_inclusive')}}
           if config.get('execution') else {}),
        **({'research_gate': research_gate_summary(frame, config)} if config.get('research_gate') else {}),
        **({'proven_order': list(config['proven_order']['keys'])} if config.get('proven_order') else {}),
        **({'weak_links': __import__('weak_links').summary(frame)} if config.get('weak_links') else {})}


def research_gate_summary(frame: pd.DataFrame, config: Mapping) -> Dict[str, object]:
    """Offers the research gate (since v3) left out, by reason: research no-loss below the line, or no research view."""
    reasons = frame.strong_reason.astype(str) if len(frame) else pd.Series(dtype=str)
    gated = reasons.str.startswith('research gate: ')
    return {'min_research_no_loss': config['research_gate']['min_research_no_loss'],
            'left_out_offers': int(gated.sum()),
            'left_out_no_research_view': int(reasons.eq('research gate: no research view').sum()),
            'left_out_matches': int(frame.loc[gated, ['league', 'home_team', 'away_team', 'kickoff_utc']]
                                    .drop_duplicates().shape[0]) if len(frame) else 0}


def write_shadow(decisions: pd.DataFrame, out_dir, predictions: Optional[pd.DataFrame] = None,
                 live_master: Optional[pd.DataFrame] = None, generated_at_utc=None) -> pd.DataFrame:
    """Write master_shortlist_strong.csv and its summary beside the live files. Never touches the live files."""
    config = load_config()
    frame = reconcile(decisions, predictions, live_master, generated_at_utc, config)
    frame.to_csv(Path(out_dir) / config['file'], index=False)
    (Path(out_dir) / config['summary_file']).write_text(
        json.dumps(summary(frame, config, generated_at_utc), indent=2, default=str) + '\n', encoding='utf-8')
    return frame


def remove_shadow(out_dir) -> None:
    config = load_config()
    for name in (config['file'], config['summary_file']):
        (Path(out_dir) / name).unlink(missing_ok=True)
