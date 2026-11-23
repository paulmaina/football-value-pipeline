"""Offline check of the strong-team master (rule master-strong-team-v1; master_strong_config.json; plan Phase 4c).

Locked: development, validation and retrospective only, built from the master backtest's own inputs
(evaluation_harness.master_league: the holdout is skipped before it is read; Elo and each team's record come from the
league's locked training rows, which never hold a holdout result). It never touches evaluation_harness.py, so the
harness's setup fingerprint is unchanged.

Computed once, in this order, by the config's rules (decided 23 Nov 2026 before any figure):
1. League trust: per league, the cagey tier's no-loss events (cagey-events-v1, D) on development: slope in
   0.90-1.10 and no failing band.
2. E (strong team) and G (R1), each the smallest candidate whose proven offers have mean (observed - market no-loss)
   >= 0 on development.
3. The research roles' pass rules (R1, R2, R4; R3 is live only).
4. The strong master selected week by week with those choices, against the live master's logic (master-new-fill-rule-v4,
   the harness's new_master_* selection): flat-stake return, whole weeks resampled; by tier and market group; the
   track-record test (among safe offers, proven minus not-proven, observed - market no-loss).

    python master_strong_check.py --output DIR [--workers N] [--leagues EPL ...]
"""
from __future__ import annotations

import argparse
import bisect
import json
import math
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path
from typing import Dict, List, Mapping, Optional

import numpy as np
import pandas as pd

import evaluation_harness as eh
import master_strong as ms

PERIODS = eh.MASTER_PERIODS
RESEARCH = 'C6'  # live domestic research v5
FINAL = 'fill_current'  # the live master's variant: the sharpening failed its pass rule and stays off


# ---------------------------------------------------------------------------
# Inputs: the master backtest's fixtures plus each fixture's pre-kickoff evidence
# ---------------------------------------------------------------------------

def team_index(history: pd.DataFrame) -> Dict[str, list]:
    """Per canonical team name, its completed matches as team_research.form_history rows, oldest first, with the
    match day for bisecting."""
    from team_research import name
    out: Dict[str, list] = {}
    for r in history.sort_values('Date', kind='mergesort').itertuples(index=False):
        day = pd.Timestamp(r.Date).tz_localize(None).normalize() if pd.Timestamp(r.Date).tzinfo else \
            pd.Timestamp(r.Date).normalize()
        entry = {'date': day.isoformat(), 'home': r.HomeTeam, 'away': r.AwayTeam,
                 'home_goals': float(r.FTHG), 'away_goals': float(r.FTAG)}
        for team in {name(r.HomeTeam), name(r.AwayTeam)}:
            out.setdefault(team, []).append((day, entry))
    return out


def last_matches(index: Mapping[str, list], team: str, kickoff, n: int = 10) -> list:
    """team_research.form_history's rows for one side: its last `n` completed matches on dates before kickoff day,
    newest first."""
    from team_research import name
    rows = index.get(name(team)) or []
    day = pd.Timestamp(kickoff).tz_localize(None).normalize() if pd.Timestamp(kickoff).tzinfo else \
        pd.Timestamp(kickoff).normalize()
    stop = bisect.bisect_left([d for d, _ in rows], day)
    return [entry for _, entry in reversed(rows[max(0, stop - n):stop])]


def strong_league(league, cache, cfg):
    """One league's master inputs (evaluation_harness.master_league) with each fixture's pre-kickoff Elo expectancy
    (elo_ratings.pre_match_ratings) and both sides' last ten matches, from the league's locked training rows."""
    import historical_benchmark as hb
    from elo_ratings import pre_match_ratings
    rows, research = eh.master_league(league, cache, cfg)
    data, _, _ = hb.load_history(Path(cache), league, {**cfg, 'test_end_exclusive': cfg['end_exclusive']})
    history = eh.training_rows(data, league, cfg, False)
    if any(eh.phase(d, league, cfg) == 'holdout' for d in history.Date):
        raise ValueError('Locked holdout rows reached the strong master check')
    elo = pre_match_ratings(history)
    keys = ['|'.join((league, pd.Timestamp(d).date().isoformat(), h, a))
            for d, h, a in zip(history.Date, history.HomeTeam, history.AwayTeam)]
    expectancy = dict(zip(keys, elo['elo_home_expectancy']))
    index = team_index(history)
    for f in rows:
        f['elo_home_expectancy'] = expectancy.get(f['fixture_key'])
        f['history'] = {'home': last_matches(index, f['home_team'], f['date']),
                        'away': last_matches(index, f['away_team'], f['date'])}
    return rows, research


def build(cache, cfg, workers=None, leagues=None):
    """Every master fixture with its evidence, the offers of the master backtest (research view C6) and the cagey
    tier's no-loss events (for league trust)."""
    leagues = list(leagues or cfg['leagues'])
    with ProcessPoolExecutor(max_workers=workers) as pool:
        parts = list(pool.map(strong_league, leagues, [str(cache)] * len(leagues), [cfg] * len(leagues)))
    fixtures = [f for rows, _ in parts for f in rows]
    eh.master_attach_c6(fixtures, [r for _, research in parts for r in research], cfg)
    frame, _ = eh.master_frame(fixtures, RESEARCH, FINAL)
    events = eh.master_sharpen_events(fixtures, eh.calibration_rules(cfg)['cagey-events-v1'])
    return fixtures, frame, events, eh.master_evaluated(fixtures)


# ---------------------------------------------------------------------------
# 1. League trust
# ---------------------------------------------------------------------------

def league_trust(events: pd.DataFrame, cfg, config) -> dict:
    """Per league and period: the cagey no-loss events' slope, bands and failing bands; status from development."""
    from football_value_pipeline_v2_standalone import LEAGUES
    rule = eh.calibration_rules(cfg)['cagey-events-v1']
    low, high = config['checks']['league_trust']['slope_range']
    part = events.loc[events.quantity.eq('no_loss')].assign(league=lambda e: e.fixture_key.str.split('|').str[0])
    out = {}
    for league, rows in part.groupby('league'):
        entry = {'name': LEAGUES[league].name if league in LEAGUES else league, 'periods': {}}
        for period in PERIODS:
            sub = rows.loc[rows.phase.eq(period)]
            if sub.empty:
                continue
            bands = eh.binary_bands(sub.p, sub.y, rule)
            bar = eh.band_z_threshold(rule['band_alpha'], len(bands))
            failing = [b for b in bands if abs(b['observed_minus_forecast']) > rule['band_max_deviation']
                       and b['z'] > bar]
            slope = eh.calibration_slope(sub.p, sub.y)
            entry['periods'][period] = {
                'events': int(len(sub)), 'fixtures': int(sub.fixture_key.nunique()),
                'mean_forecast': float(sub.p.mean()), 'observed_rate': float(sub.y.mean()), 'slope': slope,
                'failing_bands': failing, 'band_z_threshold': bar,
                'passes': bool(low <= slope <= high and not failing)}
        dev = entry['periods'].get('development')
        entry['status'] = 'trusted' if dev and dev['passes'] else 'not trusted'
        out[league] = entry
    return out


# ---------------------------------------------------------------------------
# 2-4. Annotation, choices, pass rules and the backtest
# ---------------------------------------------------------------------------

def evidence(fixture) -> dict:
    return {'elo_home_expectancy': fixture.get('elo_home_expectancy'), 'history': fixture.get('history') or {},
            'teams': {'home': fixture['home_team'], 'away': fixture['away_team']}, 'h2h': [],
            'research_margin': ms.tr.research_margin(fixture.get(RESEARCH))}


def annotate(frame: pd.DataFrame, fixtures, trust: Mapping[str, str], config, E, G) -> List[dict]:
    """Every offer row of the master backtest with the strong-team checks (raw values kept for the choices)."""
    by_key = {f['fixture_key']: evidence(f) for f in fixtures}
    rows = []
    for r in frame.to_dict('records'):
        r = {k: (None if isinstance(v, float) and math.isnan(v) else v) for k, v in r.items()}
        r['_match'] = r['fixture_key']
        ms.annotate(r, by_key[r['fixture_key']], config=config, trust=trust.get(r['league'], 'not trusted'),
                    european=False, E=E, G=G)
        rows.append(r)
    return rows


def residual(rows: pd.DataFrame, value='_nl') -> pd.DataFrame:
    return rows.assign(_nl=rows.observed_no_loss - pd.to_numeric(rows.ranking_no_loss_probability),
                       _pr=rows.observed_profit - pd.to_numeric(rows.ranking_profit_probability))


def stat(rows: pd.DataFrame, value='_nl') -> dict:
    if rows.empty:
        return {'offers': 0}
    out = eh._week_ratio(rows, value)
    return {'offers': int(len(rows)), 'fixtures': int(rows.fixture_key.nunique()), **(out or {})}


def difference(a: pd.DataFrame, b: pd.DataFrame, value='_nl') -> Optional[dict]:
    if a.empty or b.empty:
        return None
    return eh._difference(a, b, value)


def choose(table: pd.DataFrame, column: str, candidates, fallback) -> dict:
    """The smallest candidate whose offers (column >= candidate) have mean (observed - market no-loss) >= 0 on
    development; else `fallback`."""
    dev = table.loc[table.phase.eq('development')]
    tried = []
    for c in candidates:
        part = dev.loc[pd.to_numeric(dev[column]) + 1e-9 >= c]
        mean = float(part._nl.mean()) if len(part) else None
        tried.append({'candidate': c, 'offers': int(len(part)), 'mean_observed_minus_market': mean,
                      'interval': (eh._week_ratio(part, '_nl') or {}).get('interval_95') if len(part) else None})
        if mean is not None and mean >= 0:
            return {'chosen': c, 'met_rule': True, 'tried': tried}
    return {'chosen': fallback, 'met_rule': False, 'tried': tried}


def role_verdict(dev: Optional[dict], val: Optional[dict], need_validation: bool) -> dict:
    """Pass rule for R2 and R4: development point >= 0 and interval not entirely below zero; validation point >= 0."""
    ok_dev = bool(dev and dev['value'] is not None and dev['value'] >= 0 and dev['interval_reading'] != 'below zero')
    ok_val = (not need_validation) or bool(val and val['value'] is not None and val['value'] >= 0)
    return {'development': dev, 'validation': val, 'passes': ok_dev and ok_val}


def run_check(fixtures, frame, events, evaluated, cfg, config=None) -> dict:
    config = config or ms.load_config()
    trust_table = league_trust(events, cfg, config)
    trust = {k: v['status'] for k, v in trust_table.items()}
    strong, roles = config['checks']['strong_team'], config['research_roles']
    rows = annotate(frame, fixtures, trust, config, E=0., G=-math.inf)
    table = residual(pd.DataFrame(rows))
    eligible = table.loc[table.nominated.eq(True) & pd.to_numeric(table.ranking_no_loss_probability).notna()
                         & pd.to_numeric(table.ranking_profit_probability).notna()
                         & table.strong_market_group.notna()]
    base = eligible.loc[eligible.strong_safe.eq(True) & eligible.strong_record_check.eq(True)]
    e_choice = choose(base, 'strong_elo_expectancy', strong['candidates'], max(strong['candidates']))
    E = e_choice['chosen']
    with_e = base.loc[pd.to_numeric(base.strong_elo_expectancy) + 1e-9 >= E]
    g_choice = choose(with_e, 'strong_research_margin', roles['R1_research_strength']['candidates'],
                      max(roles['R1_research_strength']['candidates']))
    G = g_choice['chosen']
    with_r1 = with_e.loc[pd.to_numeric(with_e.strong_research_margin) + 1e-9 >= G]
    dev = lambda f: f.loc[f.phase.eq('development')]
    val = lambda f: f.loc[f.phase.eq('validation')]
    r1_with, r1_without = stat(dev(with_r1)), stat(dev(with_e))
    r1_pass = bool(r1_with.get('value') is not None and r1_without.get('value') is not None
                   and r1_with['value'] >= r1_without['value'] and r1_with.get('interval_reading') != 'below zero')
    proven = with_r1 if r1_pass else with_e
    confirms = proven.strong_research_confirms.eq(True)
    r2 = role_verdict(difference(dev(proven.loc[confirms]), dev(proven.loc[~confirms])),
                      difference(val(proven.loc[confirms]), val(proven.loc[~confirms])), True)
    proven_keys = set(zip(proven.fixture_key, proven.market))
    not_proven = eligible.loc[[(k, m) not in proven_keys for k, m in zip(eligible.fixture_key, eligible.market)]]
    above = pd.to_numeric(not_proven.research_profit_probability) > pd.to_numeric(not_proven.ranking_profit_probability)
    r4 = role_verdict(difference(dev(not_proven.loc[above]), dev(not_proven.loc[~above]), '_pr'),
                      difference(val(not_proven.loc[above]), val(not_proven.loc[~above]), '_pr'), True)
    run = {'E': E, 'G': G, 'R1': r1_pass, 'R2': r2['passes'], 'R3': True, 'R4': r4['passes']}
    picks = select_weeks(fixtures, frame, trust, config, run)
    return {'version': config['version'], 'research_view': RESEARCH, 'cagey_view': 'D',
            'league_trust': trust_table,
            'choices': {'E': e_choice, 'G': g_choice},
            'research_roles': {
                'R1': {'with_R1_development': r1_with, 'without_R1_development': r1_without, 'passes': r1_pass},
                'R2': r2, 'R3': {'passes': None, 'note': 'live only: no historical European prices'}, 'R4': r4},
            'settings': run,
            'track_record_test': track_record_test(picks),
            'backtest': backtest(picks, evaluated, config)}, picks


def select_weeks(fixtures, frame, trust, config, run) -> pd.DataFrame:
    rows = annotate(frame, fixtures, trust, config, run['E'], run['G'])
    weeks: Dict[tuple, list] = {}
    for r in rows:
        weeks.setdefault((r['phase'], r['week']), []).append(r)
    for part in weeks.values():
        ms.select(part, config, run, executable_key='_executable', nominated_key='nominated')
    return residual(pd.DataFrame(rows))


def track_record_test(picks: pd.DataFrame) -> dict:
    """Among safe nominated offers: proven minus not-proven mean (observed - market no-loss), whole weeks resampled."""
    safe = picks.loc[picks.nominated.eq(True) & picks.strong_safe.eq(True) & picks.strong_market_group.notna()]
    out = {}
    for period in PERIODS:
        part = safe.loc[safe.phase.eq(period)]
        yes, no = part.loc[part.strong_proven.eq(True)], part.loc[~part.strong_proven.eq(True)]
        out[period] = {'proven': stat(yes), 'not_proven': stat(no), 'proven_minus_not_proven': difference(yes, no)}
    return out


def list_stats(rows: pd.DataFrame, weeks: int) -> dict:
    stats = eh.master_list_stats(rows)
    if rows.empty:
        return {**stats, 'picks_per_week': 0.}
    return {**stats, 'picks_per_week': float(len(rows) / weeks) if weeks else None,
            'observed_minus_market_no_loss': eh._week_ratio(rows, '_nl'),
            'by_market_group': {g: int(rows.strong_market_group.eq(g).sum()) for g in ms.tr.GROUPS}}


def backtest(picks: pd.DataFrame, evaluated: pd.DataFrame, config) -> dict:
    out = {}
    for period in PERIODS:
        part = picks.loc[picks.phase.eq(period)]
        weeks = int(evaluated.loc[evaluated.phase.eq(period)].week.nunique())
        strong = part.loc[part.strong_decision.eq('SHORTLISTED')]
        live = part.loc[part.new_master_decision.eq('SHORTLISTED')]
        strong_weeks = strong.groupby('week').size().reindex(sorted(evaluated.loc[evaluated.phase.eq(period)]
                                                                     .week.unique()), fill_value=0)
        out[period] = {
            'weeks': weeks, 'strong_master': list_stats(strong, weeks), 'live_master_logic': list_stats(live, weeks),
            'strong_minus_live_return': difference(strong, live, 'return'),
            'reading': eh._reading(difference(strong, live, 'return'), 'strong better', 'strong worse'),
            'weeks_short_of_target': int((strong_weeks < int(config['target_fixtures'])).sum()),
            'by_tier': {t: list_stats(strong.loc[strong.strong_tier.eq(t)], weeks) for t in ms.TIERS},
            'same_fixture_as_live': int(strong.fixture_key.isin(set(live.fixture_key)).sum())}
    return out


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--config', type=Path, default=Path('evaluation_harness_config.json'))
    parser.add_argument('--cache', type=Path, default=Path('.football_cache'))
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--workers', type=int)
    parser.add_argument('--leagues', nargs='*')
    args = parser.parse_args(argv)
    cfg = json.loads(args.config.read_text(encoding='utf-8'))
    args.output.mkdir(parents=True, exist_ok=True)
    fixtures, frame, events, evaluated = build(args.cache, cfg, args.workers, args.leagues)
    result, picks = run_check(fixtures, frame, events, evaluated, cfg)
    result['source_commit'] = eh.git_commit()
    (args.output / 'results.json').write_text(json.dumps(result, indent=2, default=str) + '\n', encoding='utf-8')
    trust = {'version': ms.VERSION, 'rule': ms.load_config()['checks']['league_trust']['rule'],
             'source_commit': result['source_commit'],
             'leagues': {k: {'name': v['name'], 'status': v['status'],
                             'development': v['periods'].get('development'),
                             'validation': v['periods'].get('validation')}
                         for k, v in result['league_trust'].items()}}
    (args.output / 'master_league_trust.json').write_text(json.dumps(trust, indent=2, default=str) + '\n',
                                                          encoding='utf-8')
    keep = ['phase', 'week', 'league', 'fixture_key', 'home_team', 'away_team', 'kickoff_utc', 'market',
            'offered_decimal_odds', 'return', 'observed_no_loss', 'observed_profit', 'nominated',
            'ranking_no_loss_probability', 'ranking_profit_probability', 'research_no_loss_probability',
            'research_profit_probability', 'gap_points', 'new_master_decision', 'new_master_tier', 'live_master_rank',
            *[c for c in ms.STRONG_COLUMNS if c != 'research_profit_probability'], *ms.SELECTION_COLUMNS]
    picks.reindex(columns=keep).to_csv(args.output / 'strong_offers.csv', index=False)
    print(json.dumps({'settings': result['settings'],
                      'backtest': {p: {'strong': v['strong_master'].get('flat_stake_return'),
                                       'difference': v['strong_minus_live_return'], 'reading': v['reading']}
                                   for p, v in result['backtest'].items()}}, indent=2, default=str))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
