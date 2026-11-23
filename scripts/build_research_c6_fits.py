"""Build C6's walk-forward fit files: the live fits (research v5) and the harness's locked fits.

Two bases, the same fit (evaluation_harness.c6_walk_forward) at the same fold origins:

  live     (default) research_c6_live_fits.json, read by live research v5. Uses every result known before
           each origin in the eight domestic leagues, including the holdout leagues' 16 Jan - 10 Oct 2026
           matches (Paul, 14 Nov 2026: the holdout lock applies to the evaluation harness, not to live
           forecasts, and C6 has already been scored on it). C's goal rates come from the harness's own
           research step (evaluation_harness.research_context) on a Dixon-Coles fit of all earlier results.
           Nothing is scored: no holdout log loss or other score is computed.
  harness  research_c6_fits.json, the C6 candidate's fits exactly as a locked development run makes them
           (evaluation_harness.evaluate_league, holdout-free training rows, no holdout match forecast or
           read). Locked: the harness's parity mode reads it; the scheduled refresh never rebuilds it.

A fit reads only matches played before its origin, so a window's (rho, delta, slope) doesn't change when the
file is rebuilt later with more results (unless a result is corrected). Reads results and C's goal rates
only: no odds, market fits or published grid reach the fits.

    python scripts/build_research_c6_fits.py                          # live fits up to the latest fold origin
    python scripts/build_research_c6_fits.py --basis harness          # the locked harness fits (harness end)
    python scripts/build_research_c6_fits.py --scheduled --publish    # the fortnightly GitHub refresh

The scheduled refresh (.github/workflows/research-c6-fits.yml) runs every day and builds whenever the committed
fit lacks the window holding today (since 23 Nov 2026; before, only on the fold origin's own UTC day, so a run
GitHub started after midnight missed the 16 Nov 2026 window). It publishes only if the training cache was checked at least 12 hours after
the origin (so the weekend's results are in), the new file keeps every earlier window and it holds the
window opening today. Any failure leaves the committed fit in place, and live forecasts warn that their fit
is stale until a refresh succeeds.
"""
from __future__ import annotations

import argparse
from concurrent.futures import ProcessPoolExecutor
from datetime import datetime, timezone
import hashlib
import json
import math
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

import pandas as pd

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO))

STATUS = Path('docs/training_refresh_status.json')
# A window is published only once every league's current-season results file was checked this long after the
# window opens (00:00 UTC on the origin), so late Sunday matches have reached football-data.co.uk.
SETTLE = pd.Timedelta(hours=12)
STATUSES = {'fitted', 'warm_up'}


def fold_rule(cfg):
    return {'test_start': cfg['test_start'], 'step_days': cfg['step_days'],
            'fixed_bounds': sorted({cfg[k] for k in ('development_end', 'holdout_start', 'holdout_end_exclusive')})}


# ---------------------------------------------------------------------------
# Research rows: C's forecast of every match, made at its fold origin
# ---------------------------------------------------------------------------

def harness_rows(cache, cfg, workers=None):
    """The locked run's research rows (evaluate_league), exactly as the C6 candidate is fitted."""
    import evaluation_harness as eh
    rows = []
    with ProcessPoolExecutor(max_workers=workers) as pool:
        futures = [pool.submit(eh.evaluate_league, league, str(cache), cfg, False, {'C6'}) for league in cfg['leagues']]
        for future in futures:
            rows += future.result()[6]
    if any(r['identity']['phase'] == 'holdout' for r in rows):
        raise ValueError('A holdout match reached the harness C6 fits')
    return rows


def league_rows(league, cache, cfg, include_holdout=True):
    """C's goal rates for every match of `league` in the fold windows, each forecast at its window's origin
    from a Dixon-Coles fit of the results before it (evaluate_league's research step; nothing scored).
    include_holdout=False drops the holdout matches from training and forecasting, as a locked run does."""
    import evaluation_harness as eh
    import historical_benchmark as hb
    from football_value_pipeline_v2_standalone import DixonColesModel
    profile = cfg['production_v2']
    data, _, _ = hb.load_history(Path(cache), league, {**cfg, 'test_end_exclusive': cfg['end_exclusive']})
    history = eh.training_rows(data, league, cfg, include_holdout)
    rows = []
    for origin, stop in eh.fold_windows(cfg, pd.Timestamp(cfg['end_exclusive'])):
        test = data.loc[(data.Date >= origin) & (data.Date < stop)]
        if not include_holdout:
            test = test.loc[test.Date.map(lambda d: eh.phase(d, league, cfg) != 'holdout')]
        train = history.loc[history.Date < origin]
        if test.empty or len(train) < cfg['min_train']:
            continue
        model = DixonColesModel(half_life_days=profile['half_life_days'], l2=cfg['baseline_l2'],
                                max_goals=cfg['max_goals'], shot_features=profile['shot_features'],
                                bbs_statistics=False).fit(train.copy(), as_of=origin)
        for _, row in test.iterrows():
            if row.HomeTeam not in model.teams or row.AwayTeam not in model.teams:
                continue
            context, _, _ = eh.research_context(row, train, origin, model)
            rows.append({'identity': {'league': league, 'phase': eh.phase(row.Date, league, cfg)}, 'date': row.Date,
                         'goal_rates': [float(v) for v in context['goal_rates']],
                         'home_goals': row.FTHG, 'away_goals': row.FTAG, 'scored': True})
    return rows


def live_rows(cache, cfg, workers=None, include_holdout=True):
    rows = []
    with ProcessPoolExecutor(max_workers=workers) as pool:
        futures = [pool.submit(league_rows, league, str(cache), cfg, include_holdout) for league in cfg['leagues']]
        for future in futures:
            rows += future.result()
    return rows


def live_seasons(cache, cfg):
    """The harness seasons plus any later season every league already has a results file for."""
    from historical_benchmark import CODES
    codes = {p.name.split('_')[0] for p in Path(cache).glob('*_*.csv')}
    later = [s for s in sorted(codes) if s.isdigit() and len(s) == 4 and s > max(cfg['seasons'])
             and all((Path(cache) / f'{s}_{CODES[league]}.csv').exists() for league in cfg['leagues'])]
    return list(cfg['seasons']) + later


# ---------------------------------------------------------------------------
# Fit file
# ---------------------------------------------------------------------------

def results_known_through(cfg, status_path=None):
    """The earliest time any league's latest-season results file was last checked by the training refresh
    (naive UTC)."""
    import historical_benchmark as hb
    status = json.loads(Path(status_path or REPO / STATUS).read_text(encoding='utf-8'))
    checked = {}  # latest check per file (the status can hold an old Windows-style entry for the same file)
    for f in status['files']:
        path = f['path'].replace('\\', '/')
        stamp = pd.Timestamp(f['checked_at_utc']).tz_convert('UTC').tz_localize(None)
        checked[path] = max(stamp, checked.get(path, stamp))
    season = max(cfg['seasons'])
    times = []
    for league in cfg['leagues']:
        stamp = checked.get(f'.football_cache/{season}_{hb.CODES[league]}.csv')
        if stamp is None:
            raise ValueError(f'No training refresh status for {league} {season}')
        times.append(stamp)
    return min(times)


def windows_out(windows, publishable):
    out = []
    for w in windows:
        if not publishable(w['origin']):
            break
        out.append({'origin': w['origin'].date().isoformat(), 'end_exclusive': w['stop'].date().isoformat(),
                    'rho': w['low_score']['rho'], 'delta': w['low_score']['delta'],
                    'low_score_status': w['low_score']['status'], 'low_score_matches': w['low_score']['matches'],
                    'slope': w['slope']['slope'], 'slope_status': w['slope']['status'],
                    'slope_matches': w['slope']['matches']})
    return out


def build(cache, cfg, basis='live', workers=None, known_through=None):
    import evaluation_harness as eh
    import research_low_score_sharpen as c6
    end = pd.Timestamp(cfg['end_exclusive'])
    research = harness_rows(cache, cfg, workers) if basis == 'harness' else live_rows(cache, cfg, workers)
    research, _, windows = eh.c6_walk_forward(research, cfg, end, every_window=True)
    last = max(r['date'] for r in research)
    if basis == 'harness':
        # A fit needs every result before its origin; the cache stops at `last`.
        out = windows_out(windows, lambda origin: origin <= last + pd.Timedelta(days=1))
    else:
        out = windows_out(windows, lambda origin: origin + SETTLE <= known_through)
    try:
        commit = subprocess.run(['git', 'rev-parse', 'HEAD'], cwd=REPO, capture_output=True, text=True,
                                check=True).stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        commit = None
    sha = hashlib.sha256(json.dumps(cfg, sort_keys=True).encode()).hexdigest()
    if basis == 'harness':
        return {
            'version': c6.HARNESS_FITS_VERSION, 'candidate_version': c6.VERSION,
            'description': ("C6's walk-forward fits per fold window (evaluation_harness.c6_walk_forward): (rho, delta) "
                            "on C's earlier forecasts, slope on C2's earlier forecasts of decided matches, pooled over "
                            "the eight leagues, recency half-life below. Holdout-free like a locked run: the holdout "
                            "leagues' 16 Jan - 10 Oct 2026 results are never forecast or read. Live research v5 uses the "
                            "window with the latest origin on or before the forecast's observation day."),
            'half_life_days': cfg['production_v2']['half_life_days'], 'fold_rule': fold_rule(cfg),
            'built_with': {'commit': commit, 'harness_end_exclusive': cfg['end_exclusive'],
                           'harness_config_sha256': sha, 'research_rows': len(research),
                           'last_result_date': last.date().isoformat(), 'leagues': list(cfg['leagues'])},
            'windows': out}
    return {
        'version': c6.FITS_VERSION, 'candidate_version': c6.VERSION, 'basis': 'live',
        'description': ("Live C6 fits for research v5, per fold window: the harness's walk-forward fit "
                        "(evaluation_harness.c6_walk_forward) on C's forecasts of every result known before the "
                        "origin in the eight domestic leagues, including the holdout leagues' 16 Jan - 10 Oct 2026 "
                        "matches (Paul, 14 Nov 2026: the holdout lock applies to the evaluation harness, not to live "
                        "forecasts). Differs from the tested fit (research_c6_fits.json, holdout-free) by design. "
                        "Live research v5 uses the window with the latest origin on or before the forecast's "
                        "observation day."),
        'half_life_days': cfg['production_v2']['half_life_days'], 'fold_rule': fold_rule(cfg),
        'built_with': {'commit': commit, 'end_exclusive': cfg['end_exclusive'], 'config_sha256': sha,
                       'seasons': list(cfg['seasons']), 'research_rows': len(research),
                       'holdout_period_rows': int(sum(r['identity']['phase'] == 'holdout' for r in research)),
                       'last_result_date': last.date().isoformat(),
                       'results_known_through_utc': known_through.isoformat() + 'Z',
                       'leagues': list(cfg['leagues'])},
        'windows': out}


def keep_published(new, previous):
    """`new` with every window `previous` already holds replaced by the published one, exactly; returns how many.

    A window reads only results played before its origin, so once published it is final. Rebuilt on another
    machine it would differ in the last digits (the first live fits were built on Windows, the refresh runs on
    Linux: the 23 Nov 2026 refresh moved 96 of 115 earlier C6 windows by up to 2e-4 and broke the exact
    harness-live parity of the pre-holdout windows). A corrected result is the one reason to rebuild them:
    --rebuild-windows."""
    if not previous:
        return 0
    before = {w['origin']: w for w in previous.get('windows') or []}
    kept = 0
    for i, window in enumerate(new.get('windows') or []):
        if window['origin'] in before:
            new['windows'][i] = before[window['origin']]
            kept += 1
    return kept


def validate(new, previous=None, required_origin=None):
    """Raises ValueError unless `new` is a complete live fit file that can replace `previous`; returns the
    comparison with `previous`."""
    import research_low_score_sharpen as c6
    if (new.get('version'), new.get('candidate_version')) != (c6.FITS_VERSION, c6.VERSION):
        raise ValueError('not a live C6 fit file')
    windows = new.get('windows') or []
    if not windows:
        raise ValueError('no fit windows')
    origins = [w['origin'] for w in windows]
    if origins != sorted(set(origins)):
        raise ValueError('fit windows out of order or repeated')
    for w in windows:
        if not all(math.isfinite(float(w[k])) for k in c6.FIT_FIELDS):
            raise ValueError(f"non-finite fit at {w['origin']}")
        if w['low_score_status'] not in STATUSES or w['slope_status'] not in STATUSES:
            raise ValueError(f"fit at {w['origin']}: {w['low_score_status']}/{w['slope_status']}")
    if required_origin is not None and origins[-1] != required_origin:
        raise ValueError(f'latest window {origins[-1]}, expected {required_origin}: the training cache was not '
                         f'checked 12 hours after {required_origin} for every league yet (see '
                         f'{STATUS.as_posix()})')
    report = {'windows': len(windows), 'latest': windows[-1]}
    if previous is not None:
        before = {w['origin']: w for w in previous['windows']}
        missing = sorted(set(before) - set(origins))
        if missing:
            raise ValueError(f'the new file drops earlier windows: {missing[:5]}')
        diffs = [max(abs(float(w[k]) - float(before[w['origin']][k])) for k in c6.FIT_FIELDS)
                 for w in windows if w['origin'] in before]
        report.update(previous_latest=previous['windows'][-1]['origin'], new_windows=len(windows) - len(before),
                      earlier_windows_changed=sum(d > 1e-9 for d in diffs), earlier_max_abs_change=max(diffs, default=0.0))
    return report


# ---------------------------------------------------------------------------
# Scheduled refresh
# ---------------------------------------------------------------------------

def git(repo, *args, check=True):
    return subprocess.run(['git', '-C', str(repo), *args], check=check, text=True, stdin=subprocess.DEVNULL,
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE)


def publish(repo, built: Path, target: Path, origin: str, attempts=3, activity=None):
    """Commit the validated file on latest main as the training refresh does (no rebase or force-push).
    Returns whether a commit was pushed. `activity(previous file or None)` gives the model activity line committed
    with the fit (model_activity.py)."""
    import model_activity
    import research_low_score_sharpen as c6
    repo = Path(repo).resolve()
    relative = Path(target).resolve().relative_to(repo)
    new = json.loads(Path(built).read_text(encoding='utf-8'))
    with tempfile.TemporaryDirectory(prefix='c6-fits-publish-') as temporary:
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
                c6.load_fits(current)  # loads under the live rule
                git(work, 'add', '--', relative.as_posix())
                if git(work, 'diff', '--cached', '--quiet', check=False).returncode == 0:
                    print('Live C6 fits unchanged on main.')
                    return False
                if activity is not None:
                    model_activity.append(work / model_activity.LOG, [activity(before)])
                    git(work, 'add', '--', model_activity.LOG.as_posix())
                git(work, '-c', 'user.name=github-actions[bot]', '-c',
                    'user.email=41898282+github-actions[bot]@users.noreply.github.com',
                    'commit', '-m', f'Refresh live C6 research fits to the {origin} window [skip ci]')
                result = git(work, 'push', 'origin', 'HEAD:refs/heads/main', check=False)
                if result.returncode == 0:
                    print('Published live C6 fits to main.')
                    return True
                git(repo, 'fetch', 'origin', 'main')
                if git(repo, 'rev-parse', 'FETCH_HEAD').stdout.strip() == base:
                    raise RuntimeError('C6 fit push failed: ' + result.stderr)
                print('Main advanced; retrying on latest state.')
            finally:
                git(repo, 'worktree', 'remove', '--force', str(work))
    raise RuntimeError('Main kept advancing; live C6 fits not published')


def summary_lines(report, data, origin):
    latest, built = report['latest'], data['built_with']
    lines = [f'### Live C6 research fits: {origin} window', '',
             f"- Windows: {report['windows']} (new: {report.get('new_windows', report['windows'])}); latest "
             f"{latest['origin']} to {latest['end_exclusive']}",
             f"- Latest fit: rho {latest['rho']:.4f}, delta {latest['delta']:.4f}, slope {latest['slope']:.4f} "
             f"({latest['low_score_matches']} and {latest['slope_matches']} matches)",
             f"- Results to {built['last_result_date']}; training cache checked through "
             f"{built['results_known_through_utc']}; {built['research_rows']} research rows"]
    if 'earlier_windows_changed' in report:
        lines.append(f"- Earlier windows changed: {report['earlier_windows_changed']} (largest change "
                     f"{report['earlier_max_abs_change']:.2e}; non-zero only after a corrected result)")
    return lines


def write_summary(lines):
    text = '\n'.join(lines) + '\n'
    print(text)
    path = os.environ.get('GITHUB_STEP_SUMMARY')
    if path:
        with open(path, 'a', encoding='utf-8') as handle:
            handle.write(text)


def committed_origin(path) -> pd.Timestamp | None:
    """The latest window origin in a committed fit file, or None (no file, unreadable, no windows)."""
    import model_activity as ma
    windows = (ma.committed(path) or {}).get('windows') or []
    try:
        return pd.Timestamp(windows[-1]['origin'])
    except (KeyError, TypeError, ValueError, IndexError):
        return None


def current(path, origin) -> bool:
    """True when the committed fit already holds the window opening at `origin` (or a later one)."""
    latest = committed_origin(path)
    return latest is not None and latest >= origin


def main(argv=None):
    import evaluation_harness as eh
    import model_activity as ma
    import research_low_score_sharpen as c6
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('--basis', choices=('live', 'harness'), default='live')
    parser.add_argument('--cache', type=Path, default=REPO / '.football_cache')
    parser.add_argument('--end', help='end_exclusive for the fold windows (live default: the end of the window '
                                      'holding --today; harness default: the harness config)')
    parser.add_argument('--today', help='live: the run day, a UTC date (default: today)')
    parser.add_argument('--known-through', help='live: results known through this UTC time (default: the training '
                                                'refresh status)')
    parser.add_argument('--output', type=Path)
    parser.add_argument('--workers', type=int)
    parser.add_argument('--scheduled', action='store_true',
                        help='live: build only when the committed fit lacks the window holding today')
    parser.add_argument('--publish', action='store_true', help='live: validate and commit the file on latest main')
    parser.add_argument('--rebuild-windows', action='store_true',
                        help='live: rebuild the windows already published too (only after a corrected result)')
    args = parser.parse_args(argv)
    cfg = json.loads(eh.CONFIG.read_text(encoding='utf-8'))
    if args.basis == 'harness':
        if args.scheduled or args.publish:
            parser.error('the harness fits are locked; the scheduled refresh builds the live fits only')
        if args.end:
            cfg['end_exclusive'] = args.end
        data = build(args.cache, cfg, 'harness', args.workers)
        (args.output or c6.HARNESS_FITS).write_text(json.dumps(data, indent=1) + '\n', encoding='utf-8')
        last = data['windows'][-1]
        print(f"{len(data['windows'])} windows; last origin {last['origin']}: rho {last['rho']:.4f}, "
              f"delta {last['delta']:.4f}, slope {last['slope']:.4f}; results to {data['built_with']['last_result_date']}")
        return 0
    today = pd.Timestamp(args.today or datetime.now(timezone.utc).date().isoformat())
    origin = c6.expected_origin(today, fold_rule(cfg))
    if args.scheduled and current(c6.FITS, origin):
        upcoming = origin + pd.Timedelta(days=int(cfg['step_days']))
        write_summary([f'C6 fit current: the committed file holds the window from {origin.date()}; '
                       f'next window {upcoming.date()}.'])
        # Nothing to do: nothing is built, logged or committed. A missing window is built whatever the day, and
        # its outcome (published, skipped or failed) is logged (model_activity).
        return 0
    try:
        return _refresh(args, cfg, origin)
    except Exception as exc:
        if args.publish:
            outcome, reason = ma.classify_failure(exc)
            ma.record_refit(REPO, ma.refit_event('C6', outcome, origin=origin.date().isoformat(), reason=reason,
                                                 previous=ma.committed(c6.FITS)),
                            f'Log the C6 refit of the {origin.date()} window ({outcome.lower()}) [skip ci]')
        raise


def _refresh(args, cfg, origin):
    """Build, validate and write or publish the live fit for the window opening at `origin`."""
    import model_activity as ma
    import research_low_score_sharpen as c6
    cfg['end_exclusive'] = args.end or (origin + pd.Timedelta(days=int(cfg['step_days']))).date().isoformat()
    cfg['seasons'] = live_seasons(args.cache, cfg)
    known = (pd.Timestamp(args.known_through).tz_localize(None) if args.known_through
             else results_known_through(cfg))
    data = build(args.cache, cfg, 'live', args.workers, known)
    previous = json.loads(c6.FITS.read_text(encoding='utf-8')) if c6.FITS.exists() else None
    if not getattr(args, 'rebuild_windows', False):
        keep_published(data, previous)  # published windows are final; only new windows are added
    try:
        report = validate(data, previous if args.publish else None, origin.date().isoformat() if args.publish else None)
    except ValueError as exc:
        write_summary([f'### Live C6 research fits: {origin.date()} window NOT refreshed', '',
                       f'- {exc}', '- The committed fit stays in place; live forecasts warn that it is stale until '
                       'a refresh succeeds (rerun this workflow once the results are in).'])
        raise
    if args.publish:
        with tempfile.TemporaryDirectory(prefix='c6-fits-') as temporary:
            built = Path(temporary) / c6.FITS.name
            built.write_text(json.dumps(data, indent=1) + '\n', encoding='utf-8')
            changed = publish(REPO, built, c6.FITS, origin.date().isoformat(),
                              activity=lambda before: ma.refit_event('C6', ma.PUBLISHED, origin=origin.date().isoformat(),
                                                                     previous=before, new=data,
                                                                     built=data['built_with']))
        if not changed:
            ma.record_refit(REPO, ma.refit_event('C6', ma.SKIPPED, origin=origin.date().isoformat(),
                                                 reason='unchanged on main (this window is already published)',
                                                 previous=data, new=data),
                            f'Log the C6 refit of the {origin.date()} window (unchanged) [skip ci]')
        write_summary(summary_lines(report, data, origin.date()) +
                      [f"- {'Committed to main' if changed else 'Unchanged on main; nothing committed'}"])
    else:
        target = args.output or c6.FITS
        target.write_text(json.dumps(data, indent=1) + '\n', encoding='utf-8')
        write_summary(summary_lines(report, data, origin.date()) + [f'- Written to {target}'])
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
