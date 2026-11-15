"""Build CE3n's fit files for research v6 (UCL/UEL): the live fits and the harness's locked fits.

A fit window holds, for one European 14-day fold origin (evaluation_harness.fold_windows on cfg['european']):
  factors    the league-strength factors (european_candidates.fit_factors, goals: CE3n has no xG) fitted on the
             European results played before the origin in which both teams had a domestic strength at their
             own fold origin;
  strengths  for the live windows (origin on or after STRENGTHS_FROM), every domestic team's research strength at
             the origin (european_candidates.league_strengths: league Dixon-Coles before the origin and the
             last-ten domestic form, the goal rates and form v4 and v5 share, before C6's corrections), so any
             European fixture of a club in the eight leagues can be priced.
The file also holds the identities (European training name -> domestic league and club) from the reviewed
resolver and aliases exactly as the harness links them (european_results.scoped_identities with the manual
reviewed aliases, every fixture).

Two bases:

  live     (default) research_ce3n_live_fits.json, read by live research v6. Every result known before each
           origin: the backfilled and cached UCL/UEL results including the European holdout period (UCL 21 Jan
           2025 - 12 Oct 2026), and the older and cached domestic files including the domestic holdout period
           (Paul, 14 Nov 2026, the decision for C6 applied to CE3n: the holdout locks apply to the evaluation
           harness, not to live forecasts). Nothing is scored. --leave-out-holdout drops both holdouts' results,
           as a locked run does, to show this builder reproduces the tested factors exactly.
  harness  research_ce3n_fits.json, the tested fit: the factors exactly as the harness's locked European run
           fits them (evaluation_harness.european with CE3n, no holdout result read), checked against this
           builder's holdout-free factors and strengths, plus holdout-free strengths for the live windows to the
           harness end. Locked: the harness's parity mode reads it; the scheduled refresh never rebuilds it.

    python scripts/build_research_ce3n_fits.py                           # live fits to the latest fold origin
    python scripts/build_research_ce3n_fits.py --basis harness           # the locked harness fits
    python scripts/build_research_ce3n_fits.py --leave-out-holdout --end 2026-11-09 --output /tmp/check.json
    python scripts/build_research_ce3n_fits.py --scheduled --publish     # the fortnightly GitHub refresh

The scheduled refresh runs in .github/workflows/research-c6-fits.yml after the C6 refresh, every second Monday,
with C6's publish conditions: every domestic league's current-season file and the UCL and UEL training data
checked at least 12 hours after the origin, every earlier window kept and the window opening today present. Any
failure leaves the committed fit in place, and live v6 forecasts warn that their CE3n fit is stale.
"""
from __future__ import annotations

import argparse
from concurrent.futures import ProcessPoolExecutor
from datetime import datetime, timezone
import hashlib
import json
import math
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

import pandas as pd

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO))

from scripts import build_research_c6_fits as c6b  # noqa: E402  (shared refresh helpers)

STRENGTHS_FROM = '2026-10-13'  # first live window: the end of the European holdout (live-graded from here)
UCL_STATUS = Path('docs/ucl_training_refresh_status.json')
STATUSES = {'fitted', 'warm_up'}


def european_fold_rule(cfg):
    return c6b.fold_rule(cfg['european'])


# ---------------------------------------------------------------------------
# European results and domestic strengths
# ---------------------------------------------------------------------------

def european_rows(cache, cfg, end, include_holdout):
    """Every European result in the fold windows, in the harness's order (evaluate_european's factor_rows: UCL then
    UEL, window by window). include_holdout=False leaves the European holdout out, as a locked run does."""
    import evaluation_harness as eh
    import european_results as er
    e = cfg['european']
    rows = []
    for competition in e['competitions']:
        data = er.load_with_backfill(cache, competition, end)
        data = data.loc[data.Date < end].sort_values('Date', kind='stable').reset_index(drop=True)
        for origin, stop in eh.fold_windows(e, end):
            test = data.loc[(data.Date >= origin) & (data.Date < stop)]
            for _, row in test.iterrows():
                if eh.european_phase(row.Date, competition, cfg) == 'holdout' and not include_holdout:
                    continue
                rows.append({'fixture': '|'.join((competition, row.Date.date().isoformat(), row.HomeTeam, row.AwayTeam)),
                             'competition': competition, 'date': row.Date, 'origin': origin,
                             'home': row.HomeTeam, 'away': row.AwayTeam,
                             'home_goals': row.FTHG, 'away_goals': row.FTAG})
    return rows


def identities(cache, cfg, teams, include_holdout):
    """European name -> (league, domestic name), as european_candidates.domestic_strengths links them: the reviewed
    resolver, the fixture-evidence aliases and the manual reviewed aliases (every fixture since 12 Nov 2026)."""
    import european_backfill as eb
    import european_candidates as ec
    import european_results as er
    names, frames = {}, {}
    for league in cfg['leagues']:
        frame = ec.league_frame(cache, league, cfg, include_holdout)
        frames[league] = frame
        names[league] = (frame[['Date', 'HomeTeam', 'AwayTeam']], set(frame.HomeTeam) | set(frame.AwayTeam))
    reviewed = eb.load_reviewed_aliases()
    if reviewed['applies_before'] is not None:
        raise ValueError('reviewed aliases with a date limit: the live fit links every fixture')
    (mapped, ambiguous), _ = er.scoped_identities(sorted(teams), names, eb.load_domestic_aliases(), reviewed['domestic'])
    return mapped, sorted(ambiguous), frames


def strengths(cache, cfg, requests, include_holdout, workers=None):
    """{(origin iso, league, team): strength} for `requests` ({league: {origin iso: [teams]}}), one Dixon-Coles fit
    per league and origin (european_candidates.league_strengths)."""
    import european_candidates as ec
    jobs = [(league, str(cache), cfg, {o: sorted(t) for o, t in req.items()}, include_holdout)
            for league, req in requests.items() if req]
    found = {}
    with ProcessPoolExecutor(max_workers=workers) as pool:
        for (league, *_), part in zip(jobs, pool.map(ec._league_job, jobs)):
            for (origin, team), value in part.items():
                found[(origin, league, team)] = value
    return found


def build_parts(cache, cfg, end, include_holdout, workers=None, strengths_from=STRENGTHS_FROM):
    """Factor rows with their strengths, the factors at every window, the live windows' strengths and the
    identities."""
    import evaluation_harness as eh
    import european_candidates as ec
    e = cfg['european']
    rows = european_rows(cache, cfg, end, include_holdout)
    teams = {r['home'] for r in rows} | {r['away'] for r in rows}
    mapped, ambiguous, frames = identities(cache, cfg, teams, include_holdout)
    windows = eh.fold_windows(e, end)
    live = [o for o, _ in windows if o >= pd.Timestamp(strengths_from)]
    requests = {league: {} for league in cfg['leagues']}
    for r in rows:
        origin = pd.Timestamp(r['origin']).date().isoformat()
        for team in (r['home'], r['away']):
            if team in mapped:
                league, name = mapped[team]
                requests[league].setdefault(origin, set()).add(name)
    for league, frame in frames.items():
        everyone = set(frame.HomeTeam) | set(frame.AwayTeam)  # league_strengths keeps teams with recent form
        for origin in live:
            requests[league].setdefault(origin.date().isoformat(), set()).update(everyone)
    found = strengths(cache, cfg, requests, include_holdout, workers)
    per_fixture = {}
    for r in rows:
        origin = pd.Timestamp(r['origin']).date().isoformat()
        per_fixture[r['fixture']] = {side: (found.get((origin, *mapped[team])) if team in mapped else None)
                                     for side, team in (('home', r['home']), ('away', r['away']))}
    factor_data = []
    for r in rows:
        pair = ec.strength_pair(per_fixture, r['fixture'])
        if pair is not None:
            factor_data.append({**r, **pair})
    factors = {origin: ec.fit_factors(factor_data, origin, cfg['leagues'], 'goals') for origin, _ in windows}
    window_strengths = {}
    for (origin, league, team), value in found.items():
        if pd.Timestamp(origin) in live:
            window_strengths.setdefault(origin, {}).setdefault(league, {})[team] = value
    return {'rows': rows, 'per_fixture': per_fixture, 'factor_data': len(factor_data), 'windows': windows,
            'factors': factors, 'strengths': window_strengths, 'identities': mapped, 'ambiguous': ambiguous,
            'live': live}


def factor_out(f):
    """The harness's own record of a window's factors (european_candidates.build's fits): unfitted windows carry
    s, c and h as None."""
    return {k: f.get(k) for k in ('status', 'matches', 's', 'c', 'h')}


def strength_out(value):
    return {'goals': [float(v) for v in value['goals']], 'domestic_matches': int(value['domestic_matches']),
            'matches_in_form': int(value['matches_in_form'])}


def windows_out(parts, publishable, factors=None):
    out = []
    for origin, stop in parts['windows']:
        if not publishable(origin):
            break
        f = (factors or parts['factors']).get(origin)
        if f is None:
            continue
        w = {'origin': origin.date().isoformat(), 'end_exclusive': stop.date().isoformat(), 'factors': factor_out(f)}
        day = origin.date().isoformat()
        if origin in parts['live']:
            w['strengths'] = {league: {team: strength_out(v) for team, v in sorted(teams.items())}
                              for league, teams in sorted(parts['strengths'].get(day, {}).items())}
        out.append(w)
    return out


# ---------------------------------------------------------------------------
# The harness's own factors (tested fit)
# ---------------------------------------------------------------------------

def harness_check(cache, cfg, parts, workers=None):
    """Runs the harness's locked European run with CE3n (evaluation_harness.european; no holdout result is read;
    nothing here reads its scores) and compares its walk-forward factors and domestic strengths with this
    builder's holdout-free ones. Returns ({origin: harness factors}, report); raises if any differs."""
    import evaluation_harness as eh
    extras = {}
    eh.european(cache, cfg, keep={'CE3n'}, extras=extras)
    harness = {pd.Timestamp(f['origin']): f['factors']['goals'] for f in extras['fits']}
    worst, compared = 0.0, 0
    for origin, f in harness.items():
        mine = parts['factors'][origin]
        if (f['status'], f['matches']) != (mine['status'], mine['matches']):
            raise AssertionError(f'factors at {origin.date()}: harness {f["status"]}/{f["matches"]}, '
                                 f'builder {mine["status"]}/{mine["matches"]}')
        if f['status'] == 'fitted':
            for key in ('s', 'c', 'h'):
                for k, v in f[key].items():
                    worst = max(worst, abs(v - mine[key][k]))
        compared += 1
    if worst != 0.0:
        raise AssertionError(f'builder factors differ from the harness run by {worst}')
    keys_h = {r['fixture'] for r in extras['factor_rows']}
    keys_b = {r['fixture'] for r in parts['rows']}
    if keys_h != keys_b:
        raise AssertionError(f'factor rows differ: {len(keys_h - keys_b)} harness only, {len(keys_b - keys_h)} builder only')
    strength_gap, fixtures = 0.0, 0
    for fixture in keys_h:
        for side in ('home', 'away'):
            a, b = extras['strengths'][fixture][side], parts['per_fixture'][fixture][side]
            if (a is None) != (b is None):
                raise AssertionError(f'{fixture} {side}: strength present in one run only')
            if a is not None:
                strength_gap = max(strength_gap, *(abs(x - y) for x, y in zip(a['goals'], b['goals'])))
        fixtures += 1
    if strength_gap != 0.0:
        raise AssertionError(f'builder strengths differ from the harness run by {strength_gap}')
    return harness, {'harness_windows_compared': compared, 'factor_max_abs_diff': worst,
                     'factor_rows_compared': fixtures, 'strength_max_abs_diff': strength_gap}


# ---------------------------------------------------------------------------
# Fit file
# ---------------------------------------------------------------------------

def european_known_through(cache, status_path=None):
    """When the UCL and UEL training data were last checked (naive UTC): the UCL refresh status (no overdue
    unfinished match) and the reconciled Europa snapshot's verification time."""
    import european_results as er
    status = json.loads(Path(status_path or REPO / UCL_STATUS).read_text(encoding='utf-8'))
    if status.get('overdue_unfinished_match_ids'):
        raise ValueError(f"UCL results overdue: {status['overdue_unfinished_match_ids']}")
    ucl = pd.Timestamp(status['checked_at_utc']).tz_convert('UTC').tz_localize(None)
    snapshot = json.loads(er.europa_snapshot(cache).read_text(encoding='utf-8'))
    uel = pd.Timestamp(snapshot['verified_at_utc']).tz_convert('UTC').tz_localize(None)
    return min(ucl, uel)


def build(cache, cfg, basis='live', workers=None, known_through=None, include_holdout=True):
    import european_candidates as ec
    import research_ce3n as ce3n
    e = cfg['european']
    end = pd.Timestamp(e['end_exclusive'])
    harness = basis == 'harness'
    parts = build_parts(cache, cfg, end, include_holdout and not harness, workers)
    last = max(r['date'] for r in parts['rows'])
    check = None
    if harness:
        harness_factors, check = harness_check(cache, cfg, parts, workers)
        # The tested factors are the harness run's; live windows past its last fitted window take the builder's
        # (verified equal to the harness on every window the harness fits).
        factors = {**parts['factors'], **harness_factors}
        out = windows_out(parts, lambda origin: origin <= last + pd.Timedelta(days=1), factors)
    elif known_through is None:  # a check build: every window the results reach, as the harness basis
        out = windows_out(parts, lambda origin: origin <= last + pd.Timedelta(days=1))
    else:
        out = windows_out(parts, lambda origin: origin + c6b.SETTLE <= known_through)
    try:
        commit = subprocess.run(['git', 'rev-parse', 'HEAD'], cwd=REPO, capture_output=True, text=True,
                                stdin=subprocess.DEVNULL, check=True).stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        commit = None
    sha = hashlib.sha256(json.dumps(cfg, sort_keys=True).encode()).hexdigest()
    common = {'candidate_version': ce3n.VERSION, 'candidate': ce3n.CANDIDATE, 'kind': ce3n.KIND,
              'weight': ec.DOMESTIC_WEIGHT, 'factor_prior_sd': ec.FACTOR_PRIOR_SD,
              'factor_min_matches': ec.FACTOR_MIN_MATCHES, 'half_life_days': ec.HALF_LIFE_DAYS,
              'fold_rule': european_fold_rule(cfg), 'strengths_from': STRENGTHS_FROM,
              'identities': {k: list(v) for k, v in sorted(parts['identities'].items())},
              'european_names': {c: sorted({r[s] for r in parts['rows'] if r['competition'] == c for s in ('home', 'away')})
                                 for c in cfg['european']['competitions']}}
    built = {'commit': commit, 'config_sha256': sha, 'european_end_exclusive': e['end_exclusive'],
             'domestic_end_exclusive': cfg['end_exclusive'], 'seasons': list(cfg['seasons']),
             'european_results': len(parts['rows']), 'factor_rows_with_both_strengths': parts['factor_data'],
             'last_result_date': last.date().isoformat(), 'leagues': list(cfg['leagues']),
             'ambiguous_identities': parts['ambiguous']}
    if harness:
        return {'version': ce3n.HARNESS_FITS_VERSION, **common, 'basis': 'harness',
                'description': ("CE3n's tested fit: the league-strength factors exactly as the harness's locked European "
                                'run fits them (evaluation_harness.european, CE3n; no European or domestic holdout '
                                'result is read), and holdout-free domestic strengths for the live windows. Locked.'),
                'built_with': {**built, 'harness_check': check}, 'windows': out}
    return {'version': ce3n.FITS_VERSION, **common,
            'basis': 'live' if include_holdout else 'live builder, holdout results left out (check only)',
            'description': ("Live CE3n fits for research v6 (UCL/UEL): factors and domestic strengths from every result "
                            'known before each origin, including the European holdout period (UCL 21 Jan 2025 - '
                            '12 Oct 2026) and the domestic holdout period (Paul, 14 Nov 2026). Differs from the '
                            'tested fit (research_ce3n_fits.json) by design.'),
            'built_with': {**built, 'include_holdout': bool(include_holdout),
                           'holdout_period_european_results': int(sum(
                               _phase(r, cfg) == 'holdout' for r in parts['rows'])),
                           'results_known_through_utc': None if known_through is None else known_through.isoformat() + 'Z'},
            'windows': out}


def _phase(row, cfg):
    import evaluation_harness as eh
    return eh.european_phase(row['date'], row['competition'], cfg)


def validate(new, previous=None, required_origin=None):
    """Raises ValueError unless `new` is a complete live CE3n fit file that can replace `previous`."""
    import research_ce3n as ce3n
    if (new.get('version'), new.get('candidate_version')) != (ce3n.FITS_VERSION, ce3n.VERSION):
        raise ValueError('not a live CE3n fit file')
    if new.get('basis') != 'live':
        raise ValueError('not built on the live basis')
    windows = new.get('windows') or []
    if not windows:
        raise ValueError('no fit windows')
    origins = [w['origin'] for w in windows]
    if origins != sorted(set(origins)):
        raise ValueError('fit windows out of order or repeated')
    for w in windows:
        f = w['factors']
        if f['status'] not in STATUSES:
            raise ValueError(f"factors at {w['origin']}: {f['status']}")
        if f['status'] == 'fitted' and not all(math.isfinite(v) for k in ('s', 'c', 'h') for v in f[k].values()):
            raise ValueError(f"non-finite factors at {w['origin']}")
    if required_origin is not None:
        if origins[-1] != required_origin:
            raise ValueError(f'latest window {origins[-1]}, expected {required_origin}: the training data was not '
                             f'checked 12 hours after {required_origin} for every league and competition yet')
        if not windows[-1].get('strengths'):
            raise ValueError(f'the {required_origin} window has no domestic strengths')
    report = {'windows': len(windows), 'latest': windows[-1]}
    if previous is not None:
        before = {w['origin']: w for w in previous['windows']}
        missing = sorted(set(before) - set(origins))
        if missing:
            raise ValueError(f'the new file drops earlier windows: {missing[:5]}')
        diffs = [factor_change(w['factors'], before[w['origin']]['factors']) for w in windows if w['origin'] in before]
        report.update(previous_latest=previous['windows'][-1]['origin'], new_windows=len(windows) - len(before),
                      earlier_windows_changed=sum(d > 1e-9 for d in diffs), earlier_max_abs_change=max(diffs, default=0.0))
    return report


def factor_change(a, b) -> float:
    if a.get('status') != b.get('status') or a.get('matches') != b.get('matches'):
        return math.inf
    if a.get('status') != 'fitted':
        return 0.0
    return max(abs(a[k][x] - b[k][x]) for k in ('s', 'c', 'h') for x in a[k])


def publish(repo, built: Path, target: Path, origin: str, attempts=3, activity=None):
    """Commit the validated file on latest main as the C6 refresh does (no rebase or force-push), with the model
    activity line `activity(previous file or None)` when given (model_activity.py)."""
    import model_activity
    import research_ce3n as ce3n
    repo = Path(repo).resolve()
    relative = Path(target).resolve().relative_to(repo)
    new = json.loads(Path(built).read_text(encoding='utf-8'))
    git = c6b.git
    with tempfile.TemporaryDirectory(prefix='ce3n-fits-publish-') as temporary:
        for attempt in range(attempts):
            git(repo, 'fetch', 'origin', 'main')
            base = git(repo, 'rev-parse', 'FETCH_HEAD').stdout.strip()
            work = Path(temporary) / f'work-{attempt}'
            git(repo, 'worktree', 'add', '--detach', str(work), base)
            try:
                current = work / relative
                before = json.loads(current.read_text(encoding='utf-8')) if current.exists() else None
                validate(new, before, origin)
                shutil.copyfile(built, current)
                ce3n.load_fits(current)
                git(work, 'add', '--', relative.as_posix())
                if git(work, 'diff', '--cached', '--quiet', check=False).returncode == 0:
                    print('Live CE3n fits unchanged on main.')
                    return False
                if activity is not None:
                    model_activity.append(work / model_activity.LOG, [activity(before)])
                    git(work, 'add', '--', model_activity.LOG.as_posix())
                git(work, '-c', 'user.name=github-actions[bot]', '-c',
                    'user.email=41898282+github-actions[bot]@users.noreply.github.com',
                    'commit', '-m', f'Refresh live CE3n research fits to the {origin} window [skip ci]')
                result = git(work, 'push', 'origin', 'HEAD:refs/heads/main', check=False)
                if result.returncode == 0:
                    print('Published live CE3n fits to main.')
                    return True
                git(repo, 'fetch', 'origin', 'main')
                if git(repo, 'rev-parse', 'FETCH_HEAD').stdout.strip() == base:
                    raise RuntimeError('CE3n fit push failed: ' + result.stderr)
                print('Main advanced; retrying on latest state.')
            finally:
                git(repo, 'worktree', 'remove', '--force', str(work))
    raise RuntimeError('Main kept advancing; live CE3n fits not published')


def summary_lines(report, data, origin):
    latest, built = report['latest'], data['built_with']
    f = latest['factors']
    s = ', '.join(f'{k} {v:+.3f}' for k, v in sorted((f.get('s') or {}).items()))
    lines = [f'### Live CE3n research fits (UCL/UEL): {origin} window', '',
             f"- Windows: {report['windows']} (new: {report.get('new_windows', report['windows'])}); latest "
             f"{latest['origin']} to {latest['end_exclusive']}",
             f"- Latest factors ({f['status']}, {f['matches']} European matches): {s or '—'}",
             f"- Domestic strengths in the latest window: {sum(len(t) for t in (latest.get('strengths') or {}).values())} teams",
             f"- European results to {built['last_result_date']}; training data checked through "
             f"{built['results_known_through_utc']}"]
    if 'earlier_windows_changed' in report:
        lines.append(f"- Earlier windows changed: {report['earlier_windows_changed']} (largest change "
                     f"{report['earlier_max_abs_change']:.2e}; non-zero only after a corrected result)")
    return lines


def main(argv=None):
    import evaluation_harness as eh
    import model_activity as ma
    import research_ce3n as ce3n
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('--basis', choices=('live', 'harness'), default='live')
    parser.add_argument('--cache', type=Path, default=REPO / '.football_cache')
    parser.add_argument('--end', help='end_exclusive of the fold windows (live default: the end of the window '
                                      'holding --today; harness default: the harness config)')
    parser.add_argument('--today', help='live: the run day, a UTC date (default: today)')
    parser.add_argument('--known-through', help='live: results known through this UTC time (default: the training '
                                                'refresh statuses)')
    parser.add_argument('--leave-out-holdout', action='store_true',
                        help='live builder without the European and domestic holdout results (check only)')
    parser.add_argument('--output', type=Path)
    parser.add_argument('--workers', type=int)
    parser.add_argument('--scheduled', action='store_true', help='live: build only on a fold origin (every second Monday)')
    parser.add_argument('--publish', action='store_true', help='live: validate and commit the file on latest main')
    args = parser.parse_args(argv)
    cfg = json.loads(eh.CONFIG.read_text(encoding='utf-8'))
    if args.basis == 'harness':
        if args.scheduled or args.publish or args.leave_out_holdout:
            parser.error('the harness fits are locked; the scheduled refresh builds the live fits only')
        data = build(args.cache, cfg, 'harness', args.workers)
        (args.output or ce3n.HARNESS_FITS).write_text(json.dumps(data, indent=1) + '\n', encoding='utf-8')
        print(json.dumps({'windows': len(data['windows']), 'last': data['windows'][-1]['origin'],
                          **data['built_with']['harness_check']}))
        return 0
    if args.leave_out_holdout:
        if args.scheduled or args.publish or not args.output:
            parser.error('--leave-out-holdout is a check: give --output and no --scheduled/--publish')
        if args.end:
            cfg['european']['end_exclusive'] = cfg['end_exclusive'] = args.end
        data = build(args.cache, cfg, 'live', args.workers, None, include_holdout=False)
        args.output.write_text(json.dumps(data, indent=1) + '\n', encoding='utf-8')
        print(f"{len(data['windows'])} windows; results to {data['built_with']['last_result_date']}")
        return 0
    today = pd.Timestamp(args.today or datetime.now(timezone.utc).date().isoformat())
    origin = ce3n.expected_origin(today, european_fold_rule(cfg))
    if args.scheduled and origin != today:
        upcoming = origin + pd.Timedelta(days=int(cfg['european']['step_days']))
        text = f'Not a CE3n fit day: the current window opened {origin.date()}; next refresh {upcoming.date()}.'
        c6b.write_summary([text])
        if args.publish:  # the scheduled workflow: every run is logged (model_activity.py)
            ma.record_refit(REPO, ma.refit_event('CE3n', ma.NOT_FIT_DAY, origin=origin.date().isoformat(), reason=text),
                            f'Log the CE3n refit check of {today.date()} (not a fit day) [skip ci]')
        return 0
    try:
        return _refresh(args, cfg, origin)
    except Exception as exc:
        if args.publish:
            outcome, reason = ma.classify_failure(exc)
            ma.record_refit(REPO, ma.refit_event('CE3n', outcome, origin=origin.date().isoformat(), reason=reason,
                                                 previous=ma.committed(ce3n.FITS)),
                            f'Log the CE3n refit of the {origin.date()} window ({outcome.lower()}) [skip ci]')
        raise


def _refresh(args, cfg, origin):
    """Build, validate and write or publish the live CE3n fit for the window opening at `origin`."""
    import model_activity as ma
    import research_ce3n as ce3n
    end = args.end or (origin + pd.Timedelta(days=int(cfg['european']['step_days']))).date().isoformat()
    cfg['european']['end_exclusive'] = cfg['end_exclusive'] = end
    cfg['seasons'] = c6b.live_seasons(args.cache, cfg)
    if args.known_through:
        known = pd.Timestamp(args.known_through).tz_localize(None)
    else:
        known = min(c6b.results_known_through(cfg), european_known_through(args.cache))
    data = build(args.cache, cfg, 'live', args.workers, known)
    previous = json.loads(ce3n.FITS.read_text(encoding='utf-8')) if ce3n.FITS.exists() else None
    try:
        report = validate(data, previous if args.publish else None, origin.date().isoformat() if args.publish else None)
    except ValueError as exc:
        c6b.write_summary([f'### Live CE3n research fits: {origin.date()} window NOT refreshed', '',
                           f'- {exc}', '- The committed fit stays in place; live v6 forecasts warn that it is stale '
                           'until a refresh succeeds (rerun this workflow once the results are in).'])
        raise
    if args.publish:
        with tempfile.TemporaryDirectory(prefix='ce3n-fits-') as temporary:
            built = Path(temporary) / ce3n.FITS.name
            built.write_text(json.dumps(data, indent=1) + '\n', encoding='utf-8')
            changed = publish(REPO, built, ce3n.FITS, origin.date().isoformat(),
                              activity=lambda before: ma.refit_event('CE3n', ma.PUBLISHED,
                                                                     origin=origin.date().isoformat(), previous=before,
                                                                     new=data, built=data['built_with']))
        if not changed:
            ma.record_refit(REPO, ma.refit_event('CE3n', ma.SKIPPED, origin=origin.date().isoformat(),
                                                 reason='unchanged on main (this window is already published)',
                                                 previous=data, new=data),
                            f'Log the CE3n refit of the {origin.date()} window (unchanged) [skip ci]')
        c6b.write_summary(summary_lines(report, data, origin.date()) +
                          [f"- {'Committed to main' if changed else 'Unchanged on main; nothing committed'}"])
    else:
        target = args.output or ce3n.FITS
        target.write_text(json.dumps(data, indent=1) + '\n', encoding='utf-8')
        c6b.write_summary(summary_lines(report, data, origin.date()) + [f'- Written to {target}'])
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
