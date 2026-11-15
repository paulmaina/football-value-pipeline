"""Post-release live check of research v6 (CE3n) on the first UCL fixtures (PR #178 review, 15 Nov 2026).

The release's parity and replay covered UEL only: no UCL forecast with research existed before the release (the
first UCL matchday after it is 24/25 Nov 2026). This check runs automatically on every forecast run that holds UCL
fixtures (football_value_pipeline_v2_standalone writes it to the run summary as `ce3n_ucl_live_check`) and in the
weekly report (research_monitoring.ucl_live_check, from the published snapshots) until a run has passed it.

For every UCL forecast of the run, from its frozen row and research only (no result, no odds):

  competition    the forecast is research v6 and its frozen CE3n fit names the competition UCL;
  mapping        each side has a European training name; where research_history_json froze one (the reviewed
                 resolver), the fit uses that name; the domestic identity is the fit file's reviewed identity for
                 that name (or none, recorded); a side with an identity has a domestic strength in the window;
  fit window     the frozen window is the harness's fold for the research day (expected origin), not stale;
  CE shadow      v4 recomputed from the frozen inputs gives exactly the shadow probabilities and the CE goal rates;
  frozen replay  v6 recomputed from the frozen inputs and fit reproduces the frozen probabilities, and so does the
                 live replay's candidate C (research_backtest.archived_candidates);
  unvalidated    every UCL offer in the live master carries "unvalidated view" (when the master file is given).

A run passes when it holds at least one UCL v6 forecast and every check passes on every one of them.
"""
from __future__ import annotations

import copy
import json
from pathlib import Path

import pandas as pd

VERSION = 'ce3n-ucl-live-check-v1'
LEAGUE = 'UEFA Champions League'
TOLERANCE = 1e-12
CHECKS = ('competition', 'mapping', 'fit_window', 'ce_shadow', 'frozen_replay', 'unvalidated_view')


def _gap(a, b) -> float:
    if not a or not b or set(a) != set(b):
        return float('inf')
    return max(abs(float(a[k]) - float(b[k])) for k in a)


def check_forecast(row) -> dict:
    """The checks for one UCL forecast row (a dict as saved in predictions.csv)."""
    import research_backtest as rb
    import research_ce3n as ce3n
    import team_research as tr
    from asian_handicap import margins
    research = tr.decode(row.get('team_research_json'))
    out = {'home_team': row.get('home_team'), 'away_team': row.get('away_team'),
           'kickoff_utc': str(row.get('kickoff_utc')), 'version': research.get('version'), 'problems': []}
    problems = out['problems']
    fit = research.get('ce3n_fit') or {}
    ok = {}
    ok['competition'] = research.get('version') in tr.CE3N_VERSIONS and fit.get('competition') == 'UCL'
    if not ok['competition']:
        problems.append(f"competition: version {research.get('version')}, fit competition {fit.get('competition')}")
    frozen_names = (tr.decode(row.get('research_history_json')).get('teams') or {})
    mapping = True
    try:
        identities = ce3n.load_fits()['identities']
    except (OSError, ValueError) as exc:
        identities, mapping = {}, False
        problems.append(f'mapping: fit file unavailable ({type(exc).__name__})')
    sides = {}
    for side in ('home', 'away'):
        entry = fit.get(side) or {}
        name = entry.get('european_name')
        ident = identities.get(name) if name else None
        sides[side] = {'european_name': name, 'league': entry.get('league'), 'domestic_team': entry.get('domestic_team'),
                       'strength': entry.get('strength') is not None}
        if not name:
            mapping = False
            problems.append(f'mapping: {side} side has no European training name')
            continue
        if frozen_names.get(side) and frozen_names[side] != name:
            mapping = False
            problems.append(f"mapping: {side} fit name {name!r} differs from the frozen training name {frozen_names[side]!r}")
        if (list(ident) if ident else [None, None]) != [entry.get('league'), entry.get('domestic_team')]:
            mapping = False
            problems.append(f'mapping: {side} identity {entry.get("league")}/{entry.get("domestic_team")} is not the '
                            f'reviewed identity {ident}')
        if ident and fit.get('strengths_available') and entry.get('strength') is None:
            mapping = False
            problems.append(f'mapping: {side} club {ident[1]} has no domestic strength in the window')
    ok['mapping'] = mapping
    out['sides'] = sides
    out['domestic_used'] = bool((research.get('ce3n') or {}).get('domestic_used'))
    ok['fit_window'] = bool(fit) and fit.get('origin') == fit.get('expected_origin') and not fit.get('stale')
    if not ok['fit_window']:
        problems.append(f"fit window: origin {fit.get('origin')}, expected {fit.get('expected_origin')}, stale {fit.get('stale')}")
    out['fit_origin'] = fit.get('origin')
    cutoff = tr.utc(research.get('observed_at_utc'))
    evidence = copy.deepcopy(research.get('evidence', {}))
    for key in ('quality_review', 'rest_and_travel'):
        evidence.pop(key, None)
    try:
        v4 = tr.prepare(row, cutoff, copy.deepcopy(evidence), version=tr.V4_VERSION)
        shadow = research.get('shadow_v4') or {}
        ok['ce_shadow'] = (_gap(v4.get('margin_distribution'), shadow.get('margin_distribution')) <= TOLERANCE
                           and v4.get('goal_rates') == (research.get('ce3n') or {}).get('ce_goal_rates')
                           and v4.get('goal_rates') == shadow.get('goal_rates'))
        again = tr.prepare(row, cutoff, copy.deepcopy(evidence), version=research.get('version'), ce3n_fit=fit or None)
        replay_gap = _gap(again.get('margin_distribution'), research.get('margin_distribution'))
        matrices, gaps = rb.archived_candidates({**row}, cutoff + pd.Timedelta(seconds=1))
        candidate_gap = (_gap(json.loads(margins(matrices['C'])), research.get('margin_distribution'))
                         if 'C' in matrices else float('inf'))
        ok['frozen_replay'] = replay_gap <= TOLERANCE and candidate_gap <= TOLERANCE
        out.update(replay_max_abs_diff=replay_gap, candidate_max_abs_diff=candidate_gap)
    except (ValueError, TypeError, KeyError) as exc:
        ok.setdefault('ce_shadow', False)
        ok['frozen_replay'] = False
        problems.append(f'replay failed: {type(exc).__name__}: {exc}')
    if not ok['ce_shadow']:
        problems.append('CE shadow: v4 on the frozen inputs differs from the frozen shadow')
    if not ok['frozen_replay']:
        problems.append('frozen replay: v6 does not reproduce the frozen probabilities')
    out['checks'] = ok
    return out


def check_run(predictions, master=None) -> dict:
    """The check for one run: `predictions` (records or a DataFrame, as saved), `master` (the live master file's
    rows, or None when it isn't available)."""
    import team_research as tr
    if isinstance(predictions, pd.DataFrame):
        predictions = predictions.astype(object).where(predictions.notna(), None).to_dict('records')
    ucl = [r for r in predictions if str(r.get('league')) == LEAGUE]
    live = tr.configured_live()['european']
    result = {'version': VERSION, 'ucl_fixtures': len(ucl)}
    if not ucl:
        return {**result, 'status': 'no UCL fixtures'}
    with_research = [r for r in ucl if tr.decode(r.get('team_research_json')).get('margin_distribution')]
    forecasts = [check_forecast(r) for r in with_research]
    unvalidated = None
    if master is not None:
        frame = master if isinstance(master, pd.DataFrame) else pd.DataFrame(master)
        if len(frame) and 'league' in frame:
            rows = frame.loc[frame['league'].astype(str).eq(LEAGUE)]
            if 'unvalidated_view' in rows:
                flags = rows['unvalidated_view'].astype(str).str.lower().eq('true')
                unvalidated = {'offers': int(len(rows)), 'not_flagged': int((~flags).sum())}
    checks = {name: all(f['checks'].get(name) for f in forecasts) for name in CHECKS[:-1]}
    checks['unvalidated_view'] = None if unvalidated is None else unvalidated['not_flagged'] == 0
    passed = bool(forecasts) and len(forecasts) == len(ucl) and all(checks[n] for n in CHECKS[:-1]) \
        and checks['unvalidated_view'] is not False
    status = 'passed' if passed else ('not applicable: UCL live research is v4' if live != tr.CE3N_VERSION
                                      else 'failed')
    return {**result, 'status': status, 'ucl_forecasts_with_research': len(forecasts), 'checks': checks,
            'unvalidated_view': unvalidated, 'domestic_used': sum(f['domestic_used'] for f in forecasts),
            'problems': sorted({p for f in forecasts for p in f['problems']}) +
                        ([] if len(forecasts) == len(ucl) else [f'{len(ucl) - len(forecasts)} UCL forecasts without research']) +
                        ([] if checks['unvalidated_view'] is not False else
                         [f"{unvalidated['not_flagged']} UCL master offers not flagged unvalidated view"]),
            'forecasts': forecasts}


def run_check(predictions, out_dir) -> dict:
    """The run's check, for the run summary: the live master file of this run (master_shortlist.csv) if written."""
    path = Path(out_dir) / 'master_shortlist.csv'
    master = None
    if path.exists():
        try:
            master = pd.read_csv(path, low_memory=False)
        except pd.errors.EmptyDataError:
            master = pd.DataFrame()
    result = check_run(predictions, master)
    result.pop('forecasts', None) if result.get('status') == 'passed' else None
    return result
