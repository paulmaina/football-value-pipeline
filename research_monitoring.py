"""Monitoring of research v5 (C6) after its release without holdout proof (docs/plan.md, Decisions, 14 Nov 2026).

Two checks, shown at the top of the weekly performance reports (performance_tracking.report):

1. Rollback trigger (docs/plan.md, release gate, the rule for correctness fixes): after at least 150 graded
   matches across at least 3 calendar weeks, research v5 is rolled back if its research log loss on AH all lines
   is worse than v4's with the week-resampled 95% interval entirely above zero. Each graded v5 forecast (the
   latest made before the verified kickoff, as the live replay grades) is replayed under both versions from its
   own frozen inputs: v5 on C6's grid with the fit frozen in it, v4 on the independent Poisson grid of the same
   goal rates (its 'shadow_v4'), so both are scored on the same matches and the same in-scope Pinnacle AH offers
   (evaluation_harness.scoped_offers / score_offers). Worse means v5's log loss minus v4's is positive.
2. Home favourites in the holdout leagues (Eredivisie, Primeira Liga, Süper Lig), where C6 was too confident on
   the holdout (home slope 0.79): value-shortlist picks backing the home side in matches the v5 research makes
   the home team favourite, with v5's predicted home-win rate, v4's on the same forecasts and the actual rate.

Reads frozen forecasts and verified results only; no odds reach a research probability (the offers only say
which lines are scored).
"""
from __future__ import annotations

from collections import Counter
import json

import numpy as np
import pandas as pd

VERSION = 'research-v5-monitoring-v1'
MIN_MATCHES = 150
MIN_WEEKS = 3
MONITOR_LEAGUES = ('Eredivisie', 'Primeira Liga', 'Super Lig', 'Süper Lig')
TRIGGERED = 'ROLLBACK TRIGGERED'
HOME_MARKETS = ('Home win', 'Double Chance 1X')
TOLERANCE = 1e-12


def _week(stamp) -> str:
    iso = pd.Timestamp(stamp).isocalendar()
    return f'{iso.year}-W{iso.week:02d}'


def _frozen(meta, row):
    return {**row, 'snapshot_generated_utc': meta['generated_at_utc'],
            'snapshot_captured_utc': meta['captured_at_utc']}


def latest_v5_forecasts(archived, records):
    """The latest v5 forecast made before each verified match's kickoff: {identity: (generated, row, research, final)}."""
    import performance_tracking as pt
    from team_research import C6_VERSIONS, decode, utc
    latest = {}
    for meta, rows, _ in archived:
        generated = utc(meta['generated_at_utc'])
        for row in rows:
            research = decode(row.get('team_research_json'))
            if research.get('version') not in C6_VERSIONS:
                continue
            frozen = _frozen(meta, row)
            final, _ = pt.graded_match(frozen, records)
            if final is None:
                continue
            identity = (final.get('league_code'), str(final.get('match_id')))
            if identity not in latest or generated > latest[identity][0]:
                latest[identity] = (generated, frozen, research, final)
    return latest


def version_grids(research):
    """(v5 grid, v4 grid) from a v5 forecast's frozen goal rates and C6 fit. Raises if the rebuilt grids don't
    reproduce the frozen v5 and shadow-v4 margin distributions."""
    from asian_handicap import margins
    from research_low_score_sharpen import live_grid
    from team_research import research_grid
    rates = [float(v) for v in research['goal_rates']]
    grids = {'v5': live_grid(rates, research['c6_fit']), 'v4': research_grid(rates)}
    for name, frozen in (('v5', research.get('margin_distribution')),
                         ('v4', (research.get('shadow_v4') or {}).get('margin_distribution'))):
        rebuilt = json.loads(margins(grids[name]))
        if not frozen or set(frozen) != set(rebuilt) or max(abs(frozen[k] - rebuilt[k]) for k in frozen) > TOLERANCE:
            raise ValueError(f'{name} grid does not reproduce the frozen research')
    return grids['v5'], grids['v4']


def rollback_check(archived, records, root, clock=None) -> dict:
    """The correctness rollback trigger for v5 against v4 (module docstring)."""
    import evaluation_harness as eh
    from team_research import utc
    coverage = Counter()
    usable = eh.usable_results(records, root, coverage, clock)
    out = []
    for identity, (generated, row, research, final) in sorted(latest_v5_forecasts(archived, usable).items()):
        kickoff = utc(final.get('kickoff_utc')) if 'kickoff_utc' in final else utc(row.get('kickoff_utc'))
        offers = [o for o in eh.scoped_offers(row, kickoff, generated, coverage) if o['group'] == 'Asian handicap']
        if not offers:
            coverage['no_in_scope_ah_offer'] += 1
            continue
        try:
            v5, v4 = version_grids(research)
        except (ValueError, TypeError, KeyError) as exc:
            coverage['not_replayed:' + str(exc)[:60]] += 1
            continue
        date = pd.Timestamp(str(row['kickoff_utc'])[:10])
        ident = {'league': row.get('league'), 'date': date.date().isoformat(), 'week': _week(date),
                 'fixture_key': ':'.join(identity), 'phase': 'live', 'market_book': 'pinnacle'}
        out.extend(eh.score_offers(ident, {'v5': v5, 'v4': v4}, offers, final['home_goals'], final['away_goals']))
        coverage['matches_scored'] += 1
    scores = eh.match_scores(out)
    scores = scores.loc[scores['group'].eq('Asian handicap')] if len(scores) else scores
    matches = int(scores['fixture_key'].nunique()) if len(scores) else 0
    weeks = int(scores['week'].nunique()) if len(scores) else 0
    # paired(baseline=v5, candidate=v4) is v5 minus v4: positive = v5 worse.
    difference = eh.paired(scores, 'v5', 'v4') if matches else None
    eligible = matches >= MIN_MATCHES and weeks >= MIN_WEEKS
    interval = (difference or {}).get('interval_95')
    triggered = bool(eligible and interval and interval[0] > 0)
    means = scores.groupby('candidate').log_loss.mean().to_dict() if len(scores) else {}
    return {'rule': (f'After at least {MIN_MATCHES} graded matches across at least {MIN_WEEKS} weeks, roll back '
                     'research v5 if its research log loss on AH all lines minus v4\'s, on the same frozen inputs, '
                     'matches and offers, has a week-resampled 95% interval entirely above zero.'),
            'matches': matches, 'weeks': weeks, 'eligible': eligible, 'triggered': triggered,
            'v5_minus_v4_log_loss': None if not difference else difference['mean_gain'],
            'interval_95': interval, 'log_loss': {k: float(v) for k, v in means.items()},
            'coverage': dict(sorted(coverage.items()))}


def is_home_pick(row) -> bool:
    return row.get('handicap_side') == 'home' or row.get('market') in HOME_MARKETS


def home_favourites(archived, records, root, clock=None) -> dict:
    """Value picks backing the home favourite in the holdout leagues: v5 predicted vs actual home-win rate."""
    import evaluation_harness as eh
    import performance_tracking as pt
    from team_research import C6_VERSIONS, SHADOW_PREFIX, decode, utc
    usable = eh.usable_results(records, root, Counter(), clock)
    latest = {}
    for meta, predictions, shortlist in archived:
        generated = utc(meta['generated_at_utc'])
        forecasts = {r.get('fixture_key') or pt.fixture_key(r): r for r in predictions}
        for pick in shortlist:
            if pick.get('shortlist_source') != 'value' or pick.get('league') not in MONITOR_LEAGUES:
                continue
            if not is_home_pick(pick):
                continue
            key = pick.get('fixture_key') or pt.fixture_key(pick)
            forecast = forecasts.get(key)
            if forecast is None:
                continue
            research = decode(forecast.get('team_research_json'))
            p = [pt.number(forecast.get('research_p_' + k)) for k in ('home', 'draw', 'away')]
            if research.get('version') not in C6_VERSIONS or None in p or p[0] <= max(p[1:]):
                continue
            kickoff = utc(forecast.get('kickoff_utc'))
            if kickoff is None or generated >= kickoff:
                continue
            if key not in latest or generated > latest[key]['generated']:
                latest[key] = {'generated': generated, 'meta': meta, 'forecast': forecast, 'picks': [], 'p': p}
            if latest[key]['generated'] == generated:
                latest[key]['picks'].append(pick)
    rows = []
    for key, item in sorted(latest.items()):
        forecast = _frozen(item['meta'], item['forecast'])
        final, state = pt.graded_match(forecast, usable)
        rows.append({'league': forecast.get('league'), 'fixture': f"{forecast.get('home_team')} v {forecast.get('away_team')}",
                     'kickoff_utc': forecast.get('kickoff_utc'), 'picks': len(item['picks']),
                     'markets': sorted({p.get('market') for p in item['picks']}),
                     'v5_p_home': item['p'][0], 'v4_p_home': pt.number(forecast.get(SHADOW_PREFIX + 'home')),
                     'graded': final is not None,
                     'home_won': None if final is None else bool(final['home_goals'] > final['away_goals'])})
    frame = pd.DataFrame(rows)

    def summary(part):
        graded = part.loc[part['graded']] if len(part) else part
        return {'fixtures': int(len(part)), 'picks': int(part['picks'].sum()) if len(part) else 0,
                'graded': int(len(graded)),
                'v5_predicted_home_win': float(graded['v5_p_home'].mean()) if len(graded) else None,
                'v4_predicted_home_win': (float(graded['v4_p_home'].dropna().mean())
                                          if len(graded) and graded['v4_p_home'].notna().any() else None),
                'actual_home_win': float(graded['home_won'].astype(float).mean()) if len(graded) else None}
    by_league = {}
    if len(frame):
        for league, part in frame.groupby('league'):
            by_league[str(league)] = summary(part)
    return {'leagues': list(MONITOR_LEAGUES[:3]), 'all': summary(frame), 'by_league': by_league,
            'fixtures': rows}


def review(root, archived, records, clock=None) -> dict:
    return {'version': VERSION, 'rollback': rollback_check(archived, records, root, clock),
            'home_favourites': home_favourites(archived, records, root, clock)}


def _pct(value):
    return '—' if value is None else f'{100 * value:.1f}%'


def markdown(check) -> list[str]:
    """The report section; its first line is the trigger banner when the rollback fires."""
    if not check:
        return []
    rollback, fav = check['rollback'], check['home_favourites']
    lines = []
    if rollback['triggered']:
        lines += [f'> **{TRIGGERED}**: research v5 (C6) has a worse research log loss than v4 on AH all lines '
                  f'over {rollback["matches"]} graded matches and {rollback["weeks"]} weeks, with the 95% interval '
                  'entirely above zero. Roll back by reverting the v5 release PR; v5 forecasts keep their numbers.', '']
    diff, interval = rollback['v5_minus_v4_log_loss'], rollback['interval_95']
    status = (TRIGGERED if rollback['triggered'] else 'not triggered' if rollback['eligible']
              else f'not yet eligible (needs {MIN_MATCHES} matches and {MIN_WEEKS} weeks)')
    lines += ['## Research v5 (C6) rollback check', '',
              'Released on 14 Nov 2026 without holdout proof (Paul\'s exception). ' + rollback['rule'], '',
              '| Graded matches | Weeks | v5 − v4 log loss (AH all) | 95% interval | Status |',
              '|---|---|---|---|---|',
              f"| {rollback['matches']} | {rollback['weeks']} | {'—' if diff is None else f'{diff:+.5f}'} | "
              f"{'—' if not interval else f'{interval[0]:+.5f} to {interval[1]:+.5f}'} | {status} |", '',
              '## Home favourites in Eredivisie, Primeira Liga and Süper Lig (v5 value picks)', '',
              'C6 was too confident on these leagues\' home sides in the holdout (home slope 0.79). Value-shortlist '
              'picks backing the home side when the v5 research makes it favourite; latest pre-kickoff pick per match.', '',
              '| League | Matches | Picks | Graded | v5 predicted home win | v4 on the same forecasts | Actual home win |',
              '|---|---|---|---|---|---|---|']
    for name, part in [*sorted(fav['by_league'].items()), ('All three', fav['all'])]:
        lines.append(f"| {name} | {part['fixtures']} | {part['picks']} | {part['graded']} | "
                     f"{_pct(part['v5_predicted_home_win'])} | {_pct(part['v4_predicted_home_win'])} | "
                     f"{_pct(part['actual_home_win'])} |")
    lines.append('')
    return lines
