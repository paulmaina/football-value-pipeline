"""Monitoring of research v5 (C6, domestic) and v6 (CE3n, UCL/UEL) after their releases without holdout proof
(docs/plan.md, Decisions, 14 Nov 2026).

Four checks, shown at the top of the weekly performance reports (performance_tracking.report):

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
3. Rollback trigger for research v6 (Paul's decision for the European value picks, 14 Nov 2026): after at least
   150 graded European matches across at least 3 calendar weeks, v6 is rolled back if CE3n's research log loss on
   AH all lines is worse than CE's with the week-resampled 95% interval entirely above zero. Each graded v6
   forecast is replayed from its frozen inputs: CE3n on the independent grid of its frozen CE3n goal rates, CE on
   the grid of the CE goal rates frozen beside them (its 'shadow_v4'), on the same in-scope Pinnacle AH offers.
4. Calibration of CE3n and CE on the graded European matches as they accumulate: home and away logistic
   calibration slopes (evaluation_harness.calibration_slope; 1 is calibrated, below 1 too sharp), CE3n against CE
   on the same forecasts. CE was too sharp on European development (0.75 / 0.76); CE3n passed calibration v3 on
   the European holdout (0.91 / 1.00 against CE's 0.79 / 0.93). Reported, never a trigger.

Reads frozen forecasts and verified results only; no odds reach a research probability (the offers only say
which lines are scored).
"""
from __future__ import annotations

from collections import Counter
import json
from pathlib import Path

import numpy as np
import pandas as pd

VERSION = 'research-v5-v6-monitoring-v1'
MIN_MATCHES = 150
MIN_WEEKS = 3
MONITOR_LEAGUES = ('Eredivisie', 'Primeira Liga', 'Super Lig', 'Süper Lig')
TRIGGERED = 'ROLLBACK TRIGGERED'
HOME_MARKETS = ('Home win', 'Double Chance 1X')
TOLERANCE = 1e-12
CE3N_MIN_MATCHES = 150  # graded European matches
CE3N_MIN_WEEKS = 3
CE3N_WARNING = 'CE3n COMPETITION WARNING'


def _week(stamp) -> str:
    iso = pd.Timestamp(stamp).isocalendar()
    return f'{iso.year}-W{iso.week:02d}'


def _frozen(meta, row):
    return {**row, 'snapshot_generated_utc': meta['generated_at_utc'],
            'snapshot_captured_utc': meta['captured_at_utc']}


def latest_v5_forecasts(archived, records, versions=None):
    """The latest v5 forecast (or one of `versions`) made before each verified match's kickoff:
    {identity: (generated, row, research, final)}."""
    import performance_tracking as pt
    from team_research import C6_VERSIONS, decode, utc
    versions = C6_VERSIONS if versions is None else versions
    latest = {}
    for meta, rows, _ in archived:
        generated = utc(meta['generated_at_utc'])
        for row in rows:
            research = decode(row.get('team_research_json'))
            if research.get('version') not in versions:
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


def ce3n_grids(research):
    """(CE3n grid, CE grid) from a v6 forecast's frozen CE3n and CE goal rates. Raises if the rebuilt grids don't
    reproduce the frozen v6 and shadow (CE) margin distributions."""
    from asian_handicap import margins
    from research_ce3n import live_grid
    from team_research import research_grid
    grids = {'CE3n': live_grid([float(v) for v in research['goal_rates']]),
             'CE': research_grid([float(v) for v in research['shadow_v4']['goal_rates']])}
    for name, frozen in (('CE3n', research.get('margin_distribution')),
                         ('CE', (research.get('shadow_v4') or {}).get('margin_distribution'))):
        rebuilt = json.loads(margins(grids[name]))
        if not frozen or set(frozen) != set(rebuilt) or max(abs(frozen[k] - rebuilt[k]) for k in frozen) > TOLERANCE:
            raise ValueError(f'{name} grid does not reproduce the frozen research')
    return grids['CE3n'], grids['CE']


def _scored(archived, records, root, clock, versions, grids, names):
    """Each graded forecast of `versions` replayed under both grids on its in-scope Pinnacle AH offers:
    (AH score rows, {identity: (row, research, final, (grid, grid))}, coverage)."""
    import evaluation_harness as eh
    from team_research import utc
    coverage = Counter()
    usable = eh.usable_results(records, root, coverage, clock)
    out, used = [], {}
    for identity, (generated, row, research, final) in sorted(latest_v5_forecasts(archived, usable, versions).items()):
        try:
            pair = grids(research)
        except (ValueError, TypeError, KeyError) as exc:
            coverage['not_replayed:' + str(exc)[:60]] += 1
            continue
        used[identity] = (row, research, final, pair)
        kickoff = utc(final.get('kickoff_utc')) if 'kickoff_utc' in final else utc(row.get('kickoff_utc'))
        offers = [o for o in eh.scoped_offers(row, kickoff, generated, coverage) if o['group'] == 'Asian handicap']
        if not offers:
            coverage['no_in_scope_ah_offer'] += 1
            continue
        date = pd.Timestamp(str(row['kickoff_utc'])[:10])
        ident = {'league': row.get('league'), 'date': date.date().isoformat(), 'week': _week(date),
                 'fixture_key': ':'.join(identity), 'phase': 'live', 'market_book': 'pinnacle'}
        out.extend(eh.score_offers(ident, dict(zip(names, pair)), offers, final['home_goals'], final['away_goals']))
        coverage['matches_scored'] += 1
    return out, used, coverage


def _trigger(out, names, min_matches, min_weeks):
    """Matches, weeks, eligibility and (first minus second) log loss with its interval; triggered when eligible
    and the interval is entirely above zero (the first, the released version, worse)."""
    import evaluation_harness as eh
    scores = eh.match_scores(out)
    scores = scores.loc[scores['group'].eq('Asian handicap')] if len(scores) else scores
    matches = int(scores['fixture_key'].nunique()) if len(scores) else 0
    weeks = int(scores['week'].nunique()) if len(scores) else 0
    # paired(baseline=first, candidate=second) is first minus second: positive = the released version worse.
    difference = eh.paired(scores, *names) if matches else None
    eligible = matches >= min_matches and weeks >= min_weeks
    interval = (difference or {}).get('interval_95')
    means = scores.groupby('candidate').log_loss.mean().to_dict() if len(scores) else {}
    return {'matches': matches, 'weeks': weeks, 'eligible': eligible,
            'triggered': bool(eligible and interval and interval[0] > 0),
            'difference': None if not difference else difference['mean_gain'], 'interval_95': interval,
            'log_loss': {k: float(v) for k, v in means.items()}}


def _calibration(used) -> dict:
    """CE3n and CE home/away logistic calibration slopes on graded forecasts ({identity: (row, research, final, grids)})."""
    import evaluation_harness as eh
    probs = {'CE3n': [], 'CE': []}
    outcomes, domestic = [], 0
    for row, research, final, pair in used.values():
        for name, grid in zip(('CE3n', 'CE'), pair):
            h, a = np.indices(grid.shape)
            probs[name].append([float(grid[h > a].sum()), float(grid[h == a].sum()), float(grid[h < a].sum())])
        hg, ag = final['home_goals'], final['away_goals']
        outcomes.append(0 if hg > ag else 1 if hg == ag else 2)
        domestic += bool((research.get('ce3n') or {}).get('domestic_used'))
    y = np.array(outcomes)
    slopes = {}
    for name, rows in probs.items():
        p = np.array(rows, dtype=float).reshape(-1, 3)
        raw = ({side: eh.calibration_slope(p[:, k], y == k) for k, side in ((0, 'home'), (2, 'away'))}
               if len(y) >= 2 else {'home': None, 'away': None})
        slopes[name] = {k: (None if v is None or not np.isfinite(v) else float(v)) for k, v in raw.items()}
    return {'graded_matches': int(len(y)), 'domestic_used': int(domestic), 'slopes': slopes,
            'note': 'Logistic calibration slopes (1 = calibrated, below 1 too sharp); reported, not a trigger.'}


CE3N_COMPETITIONS = {'UCL': 'UEFA Champions League', 'UEL': 'UEFA Europa League'}


def ce3n_rollback_check(archived, records, root, clock=None) -> dict:
    """Research v6's rollback trigger: CE3n against CE on graded European matches, pooled (module docstring, check
    3), with the calibration slopes of both (check 4); and the same per competition (UCL, UEL), with a warning when
    one competition's interval is entirely above zero (CE3n worse) before the pooled trigger is eligible."""
    from team_research import CE3N_VERSIONS
    out, used, coverage = _scored(archived, records, root, clock, CE3N_VERSIONS, ce3n_grids, ('CE3n', 'CE'))
    result = _trigger(out, ('CE3n', 'CE'), CE3N_MIN_MATCHES, CE3N_MIN_WEEKS)
    by_competition = {}
    for code, league in CE3N_COMPETITIONS.items():
        part = _trigger([r for r in out if r.get('league') == league], ('CE3n', 'CE'), CE3N_MIN_MATCHES, CE3N_MIN_WEEKS)
        interval = part['interval_95']
        by_competition[code] = {
            'matches': part['matches'], 'weeks': part['weeks'], 'ce3n_minus_ce_log_loss': part['difference'],
            'interval_95': interval,
            'warning': bool(interval and interval[0] > 0 and not result['eligible']),
            'calibration': _calibration({k: v for k, v in used.items() if v[0].get('league') == league})}
    return {'rule': (f'After at least {CE3N_MIN_MATCHES} graded European matches across at least {CE3N_MIN_WEEKS} '
                     "weeks, roll back research v6 (CE3n, UCL/UEL) if CE3n's research log loss on AH all lines minus "
                     "CE's, on the same frozen inputs, matches and offers, has a week-resampled 95% interval "
                     'entirely above zero (pooled over UCL and UEL). Rolling back is setting research_config.json '
                     'live.european to "v4". Per competition: reported, and a warning (not a rollback) when one '
                     "competition's interval is entirely above zero before the pooled trigger is eligible."),
            'matches': result['matches'], 'weeks': result['weeks'], 'eligible': result['eligible'],
            'triggered': result['triggered'], 'ce3n_minus_ce_log_loss': result['difference'],
            'interval_95': result['interval_95'], 'log_loss': result['log_loss'],
            'calibration': _calibration(used), 'by_competition': by_competition,
            'coverage': dict(sorted(coverage.items()))}


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


def ucl_live_check(root, archived) -> dict:
    """research_live_check on the published snapshots: every run that holds a UCL forecast made under research v6,
    oldest first, until the first one that passes (runs from before the release are never checked). The live master
    file comes from the run's snapshot when it was archived."""
    import research_live_check as lc
    from team_research import CE3N_VERSIONS, decode
    runs = []
    for meta, rows, _ in archived:
        ucl = [r for r in rows if str(r.get('league')) == lc.LEAGUE]
        if not any(decode(r.get('team_research_json')).get('version') in CE3N_VERSIONS for r in ucl):
            continue
        folder = Path(root) / 'performance' / 'snapshots' / str(meta.get('git_commit_sha'))
        master = None
        if (folder / 'master_shortlist.csv').exists():
            try:
                master = pd.read_csv(folder / 'master_shortlist.csv', low_memory=False)
            except pd.errors.EmptyDataError:
                master = pd.DataFrame()
        result = lc.check_run(rows, master)
        runs.append({'snapshot': meta.get('git_commit_sha'), 'generated_at_utc': str(meta.get('generated_at_utc')),
                     'status': result['status'], 'ucl_fixtures': result['ucl_fixtures'],
                     'domestic_used': result.get('domestic_used'), 'checks': result.get('checks'),
                     'problems': result.get('problems', [])})
        if result['status'] == 'passed':
            break
    passed = next((r for r in runs if r['status'] == 'passed'), None)
    status = 'passed' if passed else ('pending: no UCL forecast under research v6 yet' if not runs else 'failed')
    return {'version': lc.VERSION, 'status': status, 'passed_on': passed, 'runs': runs}


def ucl_check_markdown(check) -> list[str]:
    if not check:
        return []
    if check['status'] == 'passed':
        run = check['passed_on']
        return [f"UCL live check of research v6: passed on the run of {run['generated_at_utc'][:16]} UTC "
                f"({run['ucl_fixtures']} UCL fixtures; snapshot {run['snapshot']}).", '']
    lines = ['### UCL live check of research v6 (until a run passes)', '',
             'Competition, reviewed team mapping, fit window, CE shadow, frozen replay and "unvalidated view" on the '
             'first runs with UCL fixtures (research_live_check). Status: **' + check['status'] + '**.', '']
    for run in check['runs']:
        lines.append(f"- {run['generated_at_utc'][:16]} UTC, {run['ucl_fixtures']} UCL fixtures: {run['status']}"
                     + (f" ({'; '.join(run['problems'][:5])})" if run['problems'] else ''))
    return lines + ([''] if check['runs'] else [])


def review(root, archived, records, clock=None) -> dict:
    return {'version': VERSION, 'rollback': rollback_check(archived, records, root, clock),
            'home_favourites': home_favourites(archived, records, root, clock),
            'ce3n': ce3n_rollback_check(archived, records, root, clock),
            'ucl_live_check': ucl_live_check(root, archived)}


def _pct(value):
    return '—' if value is None else f'{100 * value:.1f}%'


def banner(check) -> list[str]:
    """The trigger banners (each a line and a blank line) that open the report when a rollback fires."""
    if not check:
        return []
    lines = []
    rollback = check['rollback']
    if rollback['triggered']:
        lines += [f'> **{TRIGGERED}**: research v5 (C6) has a worse research log loss than v4 on AH all lines '
                  f'over {rollback["matches"]} graded matches and {rollback["weeks"]} weeks, with the 95% interval '
                  'entirely above zero. Roll back by setting research_config.json live.domestic to "v4" (Paul decides): new '
                  'forecasts then use v4; v5 forecasts keep their numbers and still replay exactly.', '']
    ce3n = check.get('ce3n') or {}
    if ce3n.get('triggered'):
        lines += [f'> **{TRIGGERED}**: research v6 (CE3n, UCL/UEL) has a worse research log loss than CE on AH all '
                  f'lines over {ce3n["matches"]} graded European matches and {ce3n["weeks"]} weeks, with the 95% '
                  'interval entirely above zero. Roll back by setting research_config.json live.european to "v4" (Paul '
                  'decides): new UCL/UEL forecasts then use v4; v6 forecasts keep their numbers and still replay exactly.', '']
    for code, part in sorted((ce3n.get('by_competition') or {}).items()):
        if part.get('warning'):
            low, high = part['interval_95']
            lines += [f'> **{CE3N_WARNING} ({code})**: CE3n has a worse research log loss than CE on AH all lines over '
                      f"{part['matches']} graded {code} matches and {part['weeks']} weeks (CE3n − CE {low:+.5f} to "
                      f'{high:+.5f}, entirely above zero), before the pooled rollback trigger is eligible. A warning, '
                      'not a rollback: review it with the pooled check below.', '']
    return lines


def _slope(value):
    return '—' if value is None else f'{value:.2f}'


def ce3n_markdown(ce3n) -> list[str]:
    if not ce3n:
        return []
    diff, interval = ce3n['ce3n_minus_ce_log_loss'], ce3n['interval_95']
    status = (TRIGGERED if ce3n['triggered'] else 'not triggered' if ce3n['eligible']
              else f'not yet eligible (needs {CE3N_MIN_MATCHES} matches and {CE3N_MIN_WEEKS} weeks)')
    cal = ce3n['calibration']
    lines = ['## Research v6 (CE3n, UCL/UEL) rollback check', '',
             "Released on 14 Nov 2026 without holdout proof (Paul's exception; not proven on the European holdout). "
             'European rows stay flagged "unvalidated view". ' + ce3n['rule'], '',
             '| Graded European matches | Weeks | CE3n − CE log loss (AH all) | 95% interval | Status |',
             '|---|---|---|---|---|',
             f"| {ce3n['matches']} | {ce3n['weeks']} | {'—' if diff is None else f'{diff:+.5f}'} | "
             f"{'—' if not interval else f'{interval[0]:+.5f} to {interval[1]:+.5f}'} | {status} |", '',
             f"Calibration on {cal['graded_matches']} graded European matches ({cal['domestic_used']} with domestic "
             'form for both teams); logistic slopes, 1 = calibrated, below 1 too sharp. Reported, not a trigger.', '',
             '| | Home slope | Away slope |', '|---|---|---|']
    for name in ('CE3n', 'CE'):
        slope = cal['slopes'].get(name) or {}
        lines.append(f"| {name} | {_slope(slope.get('home'))} | {_slope(slope.get('away'))} |")
    lines.append('')
    parts = ce3n.get('by_competition') or {}
    if parts:
        lines += ['By competition (reported; a competition whose interval is entirely above zero before the pooled '
                  'trigger is eligible gets a warning, not a rollback):', '',
                  '| Competition | Graded matches | Weeks | CE3n − CE log loss (AH all) | 95% interval | '
                  'CE3n home / away slope | CE home / away slope | Warning |',
                  '|---|---|---|---|---|---|---|---|']
        for code, part in sorted(parts.items()):
            d, i, sl = part['ce3n_minus_ce_log_loss'], part['interval_95'], part['calibration']['slopes']
            lines.append(f"| {code} | {part['matches']} | {part['weeks']} | {'—' if d is None else f'{d:+.5f}'} | "
                         f"{'—' if not i else f'{i[0]:+.5f} to {i[1]:+.5f}'} | "
                         f"{_slope(sl['CE3n'].get('home'))} / {_slope(sl['CE3n'].get('away'))} | "
                         f"{_slope(sl['CE'].get('home'))} / {_slope(sl['CE'].get('away'))} | "
                         f"{'yes' if part['warning'] else 'no'} |")
        lines.append('')
    return lines


def markdown(check) -> list[str]:
    """The report section; it opens with the trigger banners (banner()) when a rollback fires."""
    if not check:
        return []
    rollback, fav = check['rollback'], check['home_favourites']
    lines = banner(check)
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
    lines += ce3n_markdown(check.get('ce3n'))
    lines += ucl_check_markdown(check.get('ucl_live_check'))
    return lines
