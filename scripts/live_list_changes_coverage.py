"""Coverage cost of Paul's live list changes of 24 Nov 2026, Parts 1-2 (docs/plan.md Phase 4d). Information only.

Locked backtest, development and validation only (the master backtest's own inputs: evaluation_harness.master_league
skips the holdout before it is read; master_strong_check.strong_league refuses any holdout row). Nothing here is a
release rule and nothing live reads it.

- Part 1 (odds above 1.20, was 1.15): the offline offers (Home win, Away win, the main AH line both sides) are rebuilt
  with the 1.20 floor applied before either list selects, exactly where the 1.15 floor applies today
  (evaluation_harness.master_fixture, master_reconciliation_config.json execution), so each list re-selects within the
  narrower window. Value list: research view C6 (live domestic v5); cagey tier: D (as the master backtest).
- Part 2 (research no-loss >= 0.70 on every strong-master pick): the strong master selected week by week under its
  rules before (master-strong-team-v1) and after Parts 1-2 (master-strong-team-v3), with the thresholds and league trust
  the live master uses (master_strong_config.json, master_league_trust.json).

Reported per period: value and cagey nominations (bets) and matches per week, before and after, and the loss; the
strong master's picks and matches per week before and after, and how often it reaches 15 matches. Offline there is no
double chance, so the 6-per-market caps hold the strong master to 12 a week (it can't reach 15 offline either way).

    python scripts/live_list_changes_coverage.py --output evaluation/live_list_changes [--workers N]
"""
from __future__ import annotations

import argparse
import copy
import json
import sys
from pathlib import Path
from unittest import mock

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import evaluation_harness as eh  # noqa: E402
import master_reconciliation as mr  # noqa: E402
import master_strong as ms  # noqa: E402
import master_strong_check as msc  # noqa: E402

PERIODS = ('development', 'validation')
BEFORE_RULE, AFTER_RULE = 'master-strong-team-v1', 'master-strong-team-v3'
FLOOR_BEFORE, FLOOR_AFTER = 1.15, 1.20


def frame_with_floor(fixtures, floor: float) -> pd.DataFrame:
    rcfg = copy.deepcopy(mr.load_config())
    rcfg['execution']['min_odds_exclusive'] = floor
    with mock.patch.object(mr, 'load_config', return_value=rcfg):
        frame, _ = eh.master_frame(fixtures, msc.RESEARCH, msc.FINAL)
    return frame


def per_week(rows: pd.DataFrame, weeks: pd.Index) -> dict:
    bets = rows.groupby('week').size().reindex(weeks, fill_value=0)
    matches = rows.groupby('week').fixture_key.nunique().reindex(weeks, fill_value=0)
    return {'bets': int(bets.sum()), 'matches': int(matches.sum()), 'bets_per_week': float(bets.mean()),
            'matches_per_week': float(matches.mean())}


def lists(before: pd.DataFrame, after: pd.DataFrame, evaluated: pd.DataFrame) -> dict:
    out = {}
    for period in PERIODS:
        weeks = pd.Index(sorted(evaluated.loc[evaluated.phase.eq(period)].week.unique()))
        b, a = before.loc[before.phase.eq(period)], after.loc[after.phase.eq(period)]
        item = {'weeks': int(len(weeks))}
        for name, column in (('value_shortlist', 'in_value_shortlist'), ('cagey_tier', 'in_cagey_tier')):
            x, y = per_week(b.loc[b[column].eq(True)], weeks), per_week(a.loc[a[column].eq(True)], weeks)
            item[name] = {'before': x, 'after': y,
                          'lost_bets_per_week': x['bets_per_week'] - y['bets_per_week'],
                          'lost_matches_per_week': x['matches_per_week'] - y['matches_per_week'],
                          'bets_at_1_15_to_1_20_before': int(((b[column].eq(True))
                                                              & (b.offered_decimal_odds <= FLOOR_AFTER)).sum())}
        out[period] = item
    return out


def strong(fixtures, frame: pd.DataFrame, rule: str) -> pd.DataFrame:
    config = ms.load_config(version=rule)
    run = ms.settings(config)
    return msc.select_weeks(fixtures, frame, ms.load_trust(), config, run)


def master(before: pd.DataFrame, after: pd.DataFrame, evaluated: pd.DataFrame, target: int) -> dict:
    out = {}
    for period in PERIODS:
        weeks = pd.Index(sorted(evaluated.loc[evaluated.phase.eq(period)].week.unique()))
        item = {'weeks': int(len(weeks))}
        for name, picks in (('before', before), ('after', after)):
            chosen = picks.loc[picks.phase.eq(period) & picks.strong_decision.eq('SHORTLISTED')]
            counts = chosen.groupby('week').fixture_key.nunique().reindex(weeks, fill_value=0)
            gated = picks.loc[picks.phase.eq(period)].strong_reason.astype(str).str.startswith('research gate: ')
            item[name] = {**per_week(chosen, weeks), 'weeks_reaching_target': int((counts >= target).sum()),
                          'weeks_at_offline_maximum_12': int((counts >= 12).sum()),
                          'picks_per_week_distribution': {int(k): int(v) for k, v in
                                                          counts.value_counts().sort_index().items()},
                          'by_tier': {t: int(chosen.strong_tier.eq(t).sum()) for t in ms.TIERS},
                          'offers_left_out_by_research_gate': int(gated.sum())}
        item['lost_picks_per_week'] = item['before']['bets_per_week'] - item['after']['bets_per_week']
        item['lost_matches_per_week'] = item['before']['matches_per_week'] - item['after']['matches_per_week']
        out[period] = item
    return out


def markdown(result: dict) -> str:
    lines = ['# Coverage cost of the live list changes (Parts 1-2, 24 Nov 2026)', '',
             'Information only (docs/plan.md Phase 4d, "After the release"). Locked backtest, development and '
             'validation; the holdout is never read. Offline offers are Home win, Away win and the main AH line, so '
             'double chance and alternate lines are exercised only live.', '',
             '## Value shortlist and cagey tier (Part 1: odds above 1.20)', '',
             "Offline, each list nominates its best offer in each market group of each fixture (the master backtest's "
             "rule, evaluation_harness.master_fixture), without the live lists' entry thresholds. So both lists "
             'nominate the same number of bets by construction, and the floor costs a bet only where every offline '
             'offer in a group is at 1.20 or below. Where a group keeps an offer above 1.20, the list nominates that '
             'offer instead.', '',
             '| period | weeks | list | bets/week before | after | lost | matches/week before | after | lost |',
             '|---|---|---|---|---|---|---|---|---|']
    for period, item in result['lists'].items():
        for name in ('value_shortlist', 'cagey_tier'):
            x = item[name]
            lines.append(f"| {period} | {item['weeks']} | {name.replace('_', ' ')} | {x['before']['bets_per_week']:.2f} | "
                         f"{x['after']['bets_per_week']:.2f} | {x['lost_bets_per_week']:.2f} | "
                         f"{x['before']['matches_per_week']:.2f} | {x['after']['matches_per_week']:.2f} | "
                         f"{x['lost_matches_per_week']:.2f} |")
    lines += ['', '## Strong master (Parts 1-2: odds floor and research no-loss >= 0.70)', '',
              '| period | weeks | picks/week before | after | lost | weeks reaching 15 before | after | weeks at the offline maximum (12) before | after | offers left out by the research gate |',
              '|---|---|---|---|---|---|---|---|---|---|']
    for period, item in result['strong_master'].items():
        b, a = item['before'], item['after']
        lines.append(f"| {period} | {item['weeks']} | {b['bets_per_week']:.2f} | {a['bets_per_week']:.2f} | "
                     f"{item['lost_picks_per_week']:.2f} | {b['weeks_reaching_target']} | {a['weeks_reaching_target']} | "
                     f"{b['weeks_at_offline_maximum_12']} | {a['weeks_at_offline_maximum_12']} | "
                     f"{a['offers_left_out_by_research_gate']} |")
    lines += ['', 'Offline the strong master can hold at most 12 picks a week (6 match result, 6 Asian handicap; no '
              'double chance offline), so it reaches 15 in no week either before or after; live runs also offer double '
              'chance and alternate lines.', '']
    return '\n'.join(lines)


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--config', type=Path, default=Path('evaluation_harness_config.json'))
    parser.add_argument('--cache', type=Path, default=Path('.football_cache'))
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--workers', type=int)
    args = parser.parse_args(argv)
    cfg = json.loads(args.config.read_text(encoding='utf-8'))
    fixtures, before, _, evaluated = msc.build(args.cache, cfg, args.workers)
    fixtures = [f for f in fixtures if f['phase'] in PERIODS]
    before = before.loc[before.phase.isin(PERIODS)].reset_index(drop=True)
    evaluated = evaluated.loc[evaluated.phase.isin(PERIODS)]
    if not before.offered_decimal_odds.gt(FLOOR_BEFORE).all():
        raise ValueError('The master backtest used a floor other than 1.15')
    after = frame_with_floor(fixtures, FLOOR_AFTER)
    target = int(ms.load_config()['target_fixtures'])
    result = {'computed_with': {'research_view': msc.RESEARCH, 'cagey_view': 'D', 'floors': [FLOOR_BEFORE, FLOOR_AFTER],
                                'strong_rules': [BEFORE_RULE, AFTER_RULE], 'source_commit': eh.git_commit(),
                                'periods': list(PERIODS)},
              'lists': lists(before, after, evaluated),
              'strong_master': master(strong(fixtures, before, BEFORE_RULE), strong(fixtures, after, AFTER_RULE),
                                      evaluated, target)}
    args.output.mkdir(parents=True, exist_ok=True)
    (args.output / 'summary.json').write_text(json.dumps(result, indent=2, default=str) + '\n', encoding='utf-8')
    (args.output / 'report.md').write_text(markdown(result), encoding='utf-8')
    print(markdown(result))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
