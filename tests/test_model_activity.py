"""The model activity log (model_activity.py): append-only writes, each writer's lines (refit workflow, forecast
runs, weekly report, backfill), and its display in football_performance_report.xlsx (Model Activity tab, Dashboard
items, Model Monitoring's CE3n-by-competition and UCL live check sections), with every existing sheet unchanged
apart from these additions."""
from __future__ import annotations

import csv
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest import mock
from zipfile import ZipFile

import numpy as np
import pandas as pd

import excel_book as xb
import model_activity as ma
import performance_report_layout as layout
from excel_fixtures import post_release_root
from test_performance_report_layout import CE3N, table

REPO = Path(__file__).resolve().parents[1]
GOLDEN = Path(__file__).with_name('fixtures') / 'performance_workbook_before_activity.json'
NL = '\n'
STATE = {'master_live': 'new', 'research_domestic': 'v5', 'research_european': 'v6',
         'master_config_version': 'master-profit-15-pinnacle-markets-v9',
         'research_config_version': 'research-live-switch-v1'}


def script(name):
    spec = importlib.util.spec_from_file_location(name, REPO / 'scripts' / f'{name}.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def lines(path):
    return Path(path).read_text(encoding='utf-8').splitlines()


def no_summary_env():
    return {k: v for k, v in os.environ.items() if k != 'GITHUB_STEP_SUMMARY'}


class LogTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.log = Path(self.tmp.name) / 'model_activity' / 'activity_log.jsonl'

    def test_append_writes_one_line_per_event_and_never_rewrites_old_lines(self):
        first = ma.event(ma.RELEASE, 'new master', 'RELEASED', 'x', key='release:new master', source='backfill',
                         when='2026-11-15T05:23:20Z')
        self.assertEqual(len(ma.append(self.log, [first])), 1)
        before = self.log.read_bytes()
        second = ma.event(ma.REFIT, ma.FITS['C6'], 'PUBLISHED', 'y', key='refit:C6', source='refit workflow',
                          when='2026-11-16T17:30:00Z')
        ma.append(self.log, [second])
        self.assertTrue(self.log.read_bytes().startswith(before))
        self.assertEqual(len(lines(self.log)), 2)
        self.assertEqual(ma.append(self.log, [first, second]), [])  # a repeat (retry, rerun) adds nothing
        self.assertEqual(len(lines(self.log)), 2)
        item = json.loads(lines(self.log)[1])
        self.assertEqual((item['recorded_at_utc'], item['recorded_at_eat']), ('2026-11-16T17:30:00Z',
                                                                             '2026-11-16 20:30 EAT'))
        self.assertEqual(item['schema'], ma.SCHEMA)
        self.assertNotIn(b'\r\n', self.log.read_bytes())

    def test_a_torn_last_line_is_kept_and_the_new_event_starts_on_its_own_line(self):
        self.log.parent.mkdir(parents=True)
        self.log.write_bytes(b'{"torn":')
        ma.append(self.log, [ma.event(ma.STALE, 'C6', ma.STALE_STARTED, 'z', key='stale:C6', source='forecast run')])
        self.assertEqual(lines(self.log)[0], '{"torn":')
        self.assertEqual(len(ma.read(self.log)), 1)

    def test_unknown_event_kinds_are_refused(self):
        with self.assertRaises(ValueError):
            ma.event('Something', 'm', 'o', 'd', key='k', source='s')


def live_c6(origins, rho=-.02):
    import research_low_score_sharpen as c6
    return {'version': c6.FITS_VERSION, 'candidate_version': c6.VERSION, 'basis': 'live',
            'built_with': {'last_result_date': '2026-11-15', 'results_known_through_utc': '2026-11-16T16:20:00Z'},
            'windows': [{'origin': o, 'end_exclusive': o, 'rho': rho, 'delta': .03, 'slope': 1.15,
                         'low_score_status': 'fitted', 'low_score_matches': 9000, 'slope_status': 'fitted',
                         'slope_matches': 7000} for o in origins]}


class RefitWorkflowTests(unittest.TestCase):
    """Every refit run appends exactly one line: published (in the fit's own commit), not a fit day, skipped or
    failed (in a commit of its own)."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.log = Path(self.tmp.name) / 'log.jsonl'
        patcher = mock.patch.object(ma, 'commit_events',
                                    side_effect=lambda repo, events, message: bool(ma.append(self.log, events)))
        self.commit = patcher.start()
        self.addCleanup(patcher.stop)

    def run_main(self, builder, argv):
        with mock.patch.dict(os.environ, no_summary_env(), clear=True):
            return builder.main(argv)

    def test_not_a_fit_day_is_one_line_for_each_fit(self):
        for name, fit in (('build_research_c6_fits', 'C6'), ('build_research_ce3n_fits', 'CE3n')):
            b = script(name)
            with mock.patch.object(b, 'build', side_effect=AssertionError('built on a non-fit day')):
                self.assertEqual(self.run_main(b, ['--scheduled', '--publish', '--today', '2026-11-09']), 0)
            item = ma.read(self.log)[-1]
            self.assertEqual((item['event'], item['outcome'], item['key']), (ma.REFIT, ma.NOT_FIT_DAY, f'refit:{fit}'))
            self.assertIn('next refresh', item['details'])
        self.assertEqual(len(lines(self.log)), 2)

    def test_without_publish_nothing_is_logged(self):
        b = script('build_research_c6_fits')
        self.assertEqual(self.run_main(b, ['--scheduled', '--today', '2026-11-09']), 0)
        self.assertFalse(self.log.exists())

    def test_results_not_in_yet_is_skipped_and_anything_else_failed_and_the_error_still_stops_the_run(self):
        for name, fit in (('build_research_c6_fits', 'C6'), ('build_research_ce3n_fits', 'CE3n')):
            b = script(name)
            late = ValueError('latest window 2026-11-02, expected 2026-11-16: the training cache was not checked 12 '
                              'hours after 2026-11-16 for every league yet')
            for error, outcome in ((late, ma.SKIPPED), (RuntimeError('push rejected'), ma.FAILED)):
                with mock.patch.object(b, '_refresh', side_effect=error), self.assertRaises(type(error)):
                    self.run_main(b, ['--scheduled', '--publish', '--today', '2026-11-16'])
                item = ma.read(self.log)[-1]
                self.assertEqual((item['key'], item['data']['outcome']), (f'refit:{fit}', outcome))
                self.assertTrue(item['outcome'].startswith(outcome))
                self.assertEqual(item['data']['origin'], '2026-11-16')
                self.assertIn('committed fit stays in place', item['details'])
        self.assertEqual(len(lines(self.log)), 4)

    def test_published_refit_is_committed_with_the_fit_and_old_lines_stay(self):
        b = script('build_research_c6_fits')
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            remote, repo, other = root / 'remote.git', root / 'repo', root / 'other'
            subprocess.run(['git', 'init', '--bare', str(remote)], check=True, capture_output=True)
            subprocess.run(['git', 'clone', str(remote), str(repo)], check=True, capture_output=True)
            for k, v in (('user.name', 'Test'), ('user.email', 'test@example.test')):
                b.git(repo, 'config', k, v)
            b.git(repo, 'checkout', '-b', 'main')
            target = repo / 'research_c6_live_fits.json'
            target.write_text(json.dumps(live_c6(['2026-11-02'])), encoding='utf-8')
            b.git(repo, 'add', '.'), b.git(repo, 'commit', '-m', 'Initial'), b.git(repo, 'push', 'origin', 'main')
            built = root / 'built.json'

            def refit(origins, origin, rho):
                new = live_c6(origins, rho)
                built.write_text(json.dumps(new), encoding='utf-8')
                return b.publish(repo, built, target, origin, activity=lambda before: ma.refit_event(
                    'C6', ma.PUBLISHED, origin=origin, previous=before, new=new, built=new['built_with']))
            self.assertTrue(refit(['2026-11-02', '2026-11-16'], '2026-11-16', -.021))
            subprocess.run(['git', 'clone', '--branch', 'main', str(remote), str(other)], check=True, capture_output=True)
            files = b.git(other, 'show', '--name-only', '--format=', 'HEAD').stdout.split()
            self.assertEqual(sorted(files), [ma.LOG.as_posix(), 'research_c6_live_fits.json'])
            first = (other / ma.LOG).read_bytes()
            item = json.loads(first)
            self.assertEqual((item['outcome'], item['data']['window']), (ma.PUBLISHED, {'origin': '2026-11-16',
                                                                                        'end_exclusive': '2026-11-16'}))
            self.assertEqual(item['data']['parameters_before']['origin'], '2026-11-02')
            self.assertAlmostEqual(item['data']['parameters_after']['rho'], -.021)
            self.assertEqual(item['data']['matches_used'], {'rho_delta': 9000, 'slope': 7000})
            self.assertIn('rho -0.0200 → -0.0210', item['details'])
            self.assertTrue(refit(['2026-11-02', '2026-11-16', '2026-11-30'], '2026-11-30', -.022))
            b.git(other, 'pull', '--ff-only')
            self.assertTrue((other / ma.LOG).read_bytes().startswith(first))
            self.assertEqual(len(lines(other / ma.LOG)), 2)
        self.commit.assert_not_called()


class CommitEventsTests(unittest.TestCase):
    def test_commits_on_latest_main_and_a_repeat_adds_nothing(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            remote, repo, other = root / 'remote.git', root / 'repo', root / 'other'
            subprocess.run(['git', 'init', '--bare', str(remote)], check=True, capture_output=True)
            subprocess.run(['git', 'clone', str(remote), str(repo)], check=True, capture_output=True)
            for k, v in (('user.name', 'Test'), ('user.email', 'test@example.test')):
                ma.git(repo, 'config', k, v)
            ma.git(repo, 'checkout', '-b', 'main')
            (repo / 'keep.txt').write_text('x', encoding='utf-8')
            ma.git(repo, 'add', '.'), ma.git(repo, 'commit', '-m', 'Initial'), ma.git(repo, 'push', 'origin', 'main')
            item = ma.refit_event('CE3n', ma.NOT_FIT_DAY, origin='2026-11-02', reason='Not a CE3n fit day.')
            self.assertTrue(ma.commit_events(repo, [item], 'Log [skip ci]'))
            self.assertFalse(ma.commit_events(repo, [item], 'Log [skip ci]'))
            subprocess.run(['git', 'clone', '--branch', 'main', str(remote), str(other)], check=True, capture_output=True)
            self.assertEqual([e['id'] for e in ma.read(other / ma.LOG)], [item['id']])


def research(fit_field=None, stale=False, origin='2026-11-02', expected='2026-11-02'):
    data = {'version': 'team-form-research-v5'}
    if fit_field:
        data[fit_field] = {'origin': origin, 'expected_origin': expected, 'stale': stale}
    return json.dumps(data)


class ForecastRunTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.repo = Path(self.tmp.name)
        self.out = self.repo / 'football_output_v2' / 'raw'
        self.out.mkdir(parents=True)
        self.configs(STATE)
        ma.append(self.repo / ma.LOG, [ma.switch_event({}, STATE, when='2026-11-15T11:44:02Z', source='backfill')])
        self.summary({})
        self.predictions([])

    def configs(self, state):
        (self.repo / 'master_shortlist_config.json').write_text(json.dumps(
            {'version': state['master_config_version'], 'live': state['master_live']}), encoding='utf-8')
        (self.repo / 'research_config.json').write_text(json.dumps(
            {'version': state['research_config_version'],
             'live': {'domestic': state['research_domestic'], 'european': state['research_european']}}),
            encoding='utf-8')

    def summary(self, extra):
        (self.out / 'conservative_bet_summary.json').write_text(json.dumps(
            {'generated_at_utc': '2026-11-16T06:00:00+00:00', **extra}), encoding='utf-8')

    def predictions(self, rows):
        with (self.out / 'all_leagues_predictions.csv').open('w', encoding='utf-8', newline='') as handle:
            writer = csv.writer(handle)
            writer.writerow(['league', 'team_research_json'])
            writer.writerows(rows)

    def run_once(self, when='2026-11-16T06:00:00Z'):
        return ma.record_forecast(self.repo, self.out, when)

    def logged(self):
        return ma.read(self.repo / ma.LOG)

    def test_no_change_logs_nothing(self):
        self.assertEqual(self.run_once(), [])
        self.assertEqual(len(self.logged()), 1)

    def test_a_switch_change_is_one_line_with_before_and_after(self):
        self.configs({**STATE, 'research_domestic': 'v4'})
        before = (self.repo / ma.LOG).read_bytes()
        written = self.run_once()
        self.assertEqual(len(written), 1)
        item = written[0]
        self.assertEqual((item['event'], item['outcome']), (ma.SWITCH, 'SWITCH CHANGED: domestic v5 → v4'))
        self.assertEqual(item['data']['changed'], {'research_domestic': ['v5', 'v4']})
        self.assertEqual(item['data']['state_after']['research_domestic'], 'v4')
        self.assertIn('research_config.json live.domestic', item['details'])
        self.assertTrue((self.repo / ma.LOG).read_bytes().startswith(before))
        self.assertEqual(self.run_once('2026-11-17T06:00:00Z'), [])  # compared with the last logged state
        self.configs({**STATE, 'master_live': 'old', 'master_config_version': 'master-profit-15-pinnacle-markets-v10'})
        item = self.run_once('2026-11-18T06:00:00Z')[0]
        self.assertEqual(set(item['data']['changed']), {'master_live', 'master_config_version', 'research_domestic'})
        self.assertIn('master new → old', item['outcome'])

    def test_stale_fit_warning_starts_and_ends_once(self):
        self.predictions([['Premier League', research('c6_fit', True, '2026-11-02', '2026-11-16')],
                          ['Premier League', research('c6_fit')]])
        item, = self.run_once()
        self.assertEqual((item['event'], item['outcome'], item['key']), (ma.STALE, ma.STALE_STARTED, 'stale:C6'))
        self.assertIn('1 of 2 forecasts used a stale C6 fit', item['details'])
        self.assertEqual(self.run_once('2026-11-17T06:00:00Z'), [])  # still stale: nothing new
        self.predictions([['UEFA Europa League', research('ce3n_fit')]])  # no C6 forecast: no C6 verdict
        self.assertEqual(self.run_once('2026-11-18T06:00:00Z'), [])
        self.predictions([['Premier League', research('c6_fit', False, '2026-11-16', '2026-11-16')]])
        item, = self.run_once('2026-11-19T06:00:00Z')
        self.assertEqual(item['outcome'], ma.STALE_ENDED)

    def test_master_fallback_and_missing_baseline(self):
        import master_shortlist as ms
        self.summary({ms.RELEASE_STATUS_KEY: {'status': ms.NEW_MASTER_FAILED, 'error': 'KeyError: x'}})
        item, = self.run_once()
        self.assertEqual((item['event'], item['outcome']), (ma.MASTER_FALLBACK, ms.NEW_MASTER_FAILED))
        self.summary({ms.RELEASE_STATUS_KEY: {'status': ms.BASELINE_MISSING, 'error': 'ValueError: y'}})
        (self.out / 'conservative_bet_summary.json').write_text(json.dumps(
            {'generated_at_utc': '2026-11-17T06:00:00+00:00',
             ms.RELEASE_STATUS_KEY: {'status': ms.BASELINE_MISSING, 'error': 'ValueError: y'}}), encoding='utf-8')
        item, = self.run_once()
        self.assertEqual((item['event'], item['outcome']), (ma.BASELINE_MISSING, ms.BASELINE_MISSING))

    def test_ucl_live_check_until_it_passes_then_only_failures(self):
        def run(status, day):
            (self.out / 'conservative_bet_summary.json').write_text(json.dumps(
                {'generated_at_utc': f'2026-11-{day}T06:00:00+00:00',
                 'ce3n_ucl_live_check': {'status': status, 'ucl_fixtures': 8, 'problems': ['mapping: x']}}),
                encoding='utf-8')
            return self.run_once()
        self.assertEqual(run('failed', 24)[0]['outcome'], 'FAILED')
        self.assertEqual(run('passed', 25)[0]['outcome'], 'passed')
        self.assertEqual(run('passed', 26), [])
        self.assertEqual(run('failed', 27)[0]['outcome'], 'FAILED')
        (self.out / 'conservative_bet_summary.json').write_text(json.dumps(
            {'generated_at_utc': '2026-11-28T06:00:00+00:00', 'ce3n_ucl_live_check': {'status': 'no UCL fixtures',
                                                                                       'ucl_fixtures': 0}}),
            encoding='utf-8')
        self.assertEqual(self.run_once(), [])

    def test_a_broken_run_output_only_warns(self):
        (self.out / 'all_leagues_predictions.csv').write_bytes(b'\xff\xfe broken')
        with self.assertWarns(UserWarning):
            self.assertEqual(self.run_once(), [])

    def test_only_the_log_changes(self):
        self.configs({**STATE, 'research_european': 'v4'})
        before = {p: p.read_bytes() for p in self.repo.rglob('*') if p.is_file() and p != self.repo / ma.LOG}
        self.run_once()
        after = {p: p.read_bytes() for p in self.repo.rglob('*') if p.is_file() and p != self.repo / ma.LOG}
        self.assertEqual(before, after)


def figures(matches=20, weeks=2):
    return {'matches': matches, 'weeks': weeks, 'eligible': False, 'triggered': False, 'interval_95': None}


class WeeklyReportTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.research = {'rollback': {**figures(), 'v5_minus_v4_log_loss': -0.001},
                         'ce3n': {**CE3N}}
        self.price_edge = {'master_rollback': {'status': 'WAITING', 'triggered': False, 'min_graded_matches': 150,
                                               'min_weeks': 3, 'new_master': {'graded_matches': 6, 'weeks': 1},
                                               'old_master': {'graded_matches': 60, 'weeks': 2},
                                               'difference': None, 'interval_95': None, 'message': 'Not triggered.'}}

    def review(self, when):
        return ma.record_review(self.root, self.research, self.price_edge, when)

    def test_one_line_per_release_and_competition_each_week_and_on_status_changes(self):
        written = self.review('2026-11-16T07:30:00Z')
        self.assertEqual([e['key'] for e in written], ['rollback:master', 'rollback:v5', 'rollback:v6',
                                                       'rollback:UCL', 'rollback:UEL'])
        by_key = {e['key']: e for e in written}
        self.assertEqual(by_key['rollback:UCL']['outcome'], 'CE3n COMPETITION WARNING (UCL)')
        self.assertEqual(by_key['rollback:UEL']['outcome'], 'no competition warning')
        self.assertIn('24 graded UCL matches over 2 weeks; CE3n − CE +0.00310, 95% interval +0.00040 to +0.00600',
                      by_key['rollback:UCL']['details'])
        self.assertIn('CE3n home 0.88', by_key['rollback:UCL']['details'])
        self.assertEqual(by_key['rollback:v6']['outcome'],
                         'not yet eligible (40 of 150 graded matches, 2 of 3 weeks)')
        self.assertEqual(by_key['rollback:v6']['data']['interval_95'], [-0.001, 0.003])
        self.assertTrue(by_key['rollback:master']['outcome'].startswith('not yet eligible'))
        before = (self.root / ma.RELATIVE).read_bytes()
        self.research['rollback']['matches'] = 30  # more matches, same status, same week: nothing
        self.assertEqual(self.review('2026-11-18T07:30:00Z'), [])
        self.research['ce3n'] = {**CE3N, 'triggered': True, 'eligible': True}
        changed = self.review('2026-11-19T07:30:00Z')
        self.assertEqual([(e['key'], e['outcome']) for e in changed], [('rollback:v6', 'ROLLBACK TRIGGERED')])
        self.assertEqual(len(self.review('2026-11-23T07:30:00Z')), 5)  # the next report week (Monday, EAT)
        self.assertTrue((self.root / ma.RELATIVE).read_bytes().startswith(before))
        self.assertEqual(len(lines(self.root / ma.RELATIVE)), 11)

    def test_week_boundary_is_monday_eat(self):
        self.assertEqual(ma.report_week('2026-11-22T20:59:00Z'), '2026-W47')  # Sunday 23:59 EAT
        self.assertEqual(ma.report_week('2026-11-22T21:00:00Z'), '2026-W48')  # Monday 00:00 EAT

    def test_a_failed_research_review_still_logs_the_master_check(self):
        written = ma.record_review(self.root, None, self.price_edge, '2026-11-16T07:30:00Z')
        self.assertEqual([e['key'] for e in written], ['rollback:master'])

    def test_review_hook_is_wired(self):
        text = (REPO / 'performance_tracking.py').read_text(encoding='utf-8')
        self.assertIn('record_review(root, research_check, price_edge, clock)', text)
        self.assertIn('football_output_v2/model_activity', (REPO / 'publish_performance.py').read_text(encoding='utf-8'))
        text = (REPO / 'publish_scheduled_forecasts.py').read_text(encoding='utf-8')
        self.assertIn("model_activity.record_forecast(work,work/'football_output_v2/raw')", text)


class BackfillTests(unittest.TestCase):
    def test_backfill_is_idempotent_and_covers_the_three_releases(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            for name in ('research_c6_live_fits.json', 'research_ce3n_live_fits.json'):
                (repo / name).write_text((REPO / name).read_text(encoding='utf-8'), encoding='utf-8')
            first = ma.backfill(repo)
            self.assertEqual(ma.backfill(repo), [])
            self.assertEqual(len(lines(repo / ma.LOG)), len(first))
        releases = [e for e in first if e['event'] == ma.RELEASE]
        self.assertEqual([e['model'] for e in releases], ['new master', 'research v5 (C6), domestic',
                                                          'research v6 (CE3n), UCL/UEL'])
        self.assertTrue(all(e['backfilled'] and e['outcome'] == "RELEASED (Paul's exception)" for e in releases))
        self.assertEqual(releases[0]['data']['versions']['after'], 'master-new-fill-rule-v4-live-v10')
        switches = [e for e in first if e['event'] == ma.SWITCH]
        self.assertEqual(switches[-1]['data']['state_after'], STATE)
        refits = {e['data']['fit']: e for e in first if e['event'] == ma.REFIT}
        self.assertEqual(set(refits), {'C6', 'CE3n'})
        self.assertTrue(all(e['outcome'] == ma.PUBLISHED for e in refits.values()))
        self.assertEqual(refits['C6']['data']['window']['origin'], '2026-11-02')

    def test_committed_log_matches_the_backfill_and_the_current_switches(self):
        committed = ma.read(REPO / ma.LOG)
        ids = [e['id'] for e in committed]
        self.assertEqual(len(ids), len(set(ids)))
        expected = {e['id'] for e in ma.backfill_events(REPO)}
        self.assertTrue(expected <= set(ids))
        state = ma.switch_state(REPO / 'master_shortlist_config.json', REPO / 'research_config.json')
        self.assertEqual(ma.last(committed, 'switches')['data']['state_after'], state)

    def test_archived_master_incidents_are_backfilled_once(self):
        import master_shortlist as ms
        with tempfile.TemporaryDirectory() as tmp:
            folder = Path(tmp) / 'football_output_v2' / 'performance' / 'snapshots' / 'abc'
            folder.mkdir(parents=True)
            (folder / 'selection_summary.json').write_text(json.dumps(
                {'generated_at_utc': '2026-11-16T06:00:00+00:00',
                 ms.RELEASE_STATUS_KEY: {'status': ms.BASELINE_MISSING, 'error': 'E'}}), encoding='utf-8')
            items = ma.archived_master_events(Path(tmp) / 'football_output_v2')
            self.assertEqual([(e['id'], e['backfilled']) for e in items], [('backfill:baseline_missing:abc', True)])


def real_shaped_ce3n():
    """research_monitoring.ce3n_rollback_check's own output (PR #178) on synthetic scored matches: the real
    trigger, interval and calibration code, only the archive replay (_scored) replaced."""
    import evaluation_harness as eh
    import research_monitoring as rm
    from team_research import research_grid
    rng = np.random.default_rng(7)
    out, used = [], {}
    for i in range(40):
        league = 'UEFA Champions League' if i % 2 else 'UEFA Europa League'
        date = pd.Timestamp('2026-11-24') + pd.Timedelta(days=7 * (i % 4))
        rates = [float(rng.uniform(.9, 1.9)), float(rng.uniform(.7, 1.5))]
        ce3n, ce = research_grid([rates[0] * 1.05, rates[1] * .95]), research_grid(rates)
        hg, ag = int(rng.poisson(rates[0])), int(rng.poisson(rates[1]))
        stamp = pd.Timestamp('2026-11-24T12:00:00Z').to_pydatetime()
        offers = [{'market': f'AH {side} {line}', 'group': 'Asian handicap', 'price': 1.9, 'stamp': stamp,
                   'side': side, 'line': line} for side in ('home', 'away') for line in (-.5, 0., .25)]
        ident = {'league': league, 'date': date.date().isoformat(), 'week': rm._week(date),
                 'fixture_key': f'EU:{i}', 'phase': 'live', 'market_book': 'pinnacle'}
        out.extend(eh.score_offers(ident, {'CE3n': ce3n, 'CE': ce}, offers, hg, ag))
        used[('EU', str(i))] = ({'league': league}, {'ce3n': {'domestic_used': bool(i % 3)}},
                                {'home_goals': hg, 'away_goals': ag}, (ce3n, ce))
    with mock.patch.object(rm, '_scored', return_value=(out, used, {'matches_scored': 40})):
        return rm.ce3n_rollback_check([], [], Path('.'))


class WorkbookCase(unittest.TestCase):
    ce3n = CE3N
    activity = True
    research_extra: dict = {}

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = post_release_root(Path(self.tmp.name) / 'out', ce3n=self.ce3n)
        if self.research_extra:
            path = self.root / 'performance' / 'research_v5_monitoring.json'
            data = json.loads(path.read_text(encoding='utf-8'))
            path.write_text(json.dumps({**data, **self.research_extra}), encoding='utf-8')
        configs = Path(self.tmp.name)
        master, research_cfg = configs / 'master_shortlist_config.json', configs / 'research_config.json'
        master.write_text(json.dumps({'version': STATE['master_config_version'], 'live': 'new'}), encoding='utf-8')
        research_cfg.write_text(json.dumps({'version': STATE['research_config_version'],
                                            'live': {'domestic': 'v5', 'european': 'v6'}}), encoding='utf-8')
        for name, path in (('MASTER_CONFIG', master), ('RESEARCH_CONFIG', research_cfg)):
            patcher = mock.patch.object(layout, name, path)
            patcher.start()
            self.addCleanup(patcher.stop)
        if self.activity:
            self.write_activity()
        metrics = json.loads((self.root / 'performance' / 'metrics.json').read_text(encoding='utf-8'))
        self.path = layout.write(self.root, self.root / 'readable' / layout.REPORT_NAME, metrics)
        self.book = xb.read_workbook(self.path)

    def write_activity(self):
        log = self.root / ma.RELATIVE
        ma.append(log, [e for e in ma.backfill_events(REPO) if e['event'] != ma.REFIT])
        ma.append(log, [
            ma.refit_event('C6', ma.PUBLISHED, origin='2026-11-16', previous=live_c6(['2026-11-02']),
                           new=live_c6(['2026-11-02', '2026-11-16'], -.021), when='2026-11-16T17:20:00Z'),
            ma.refit_event('CE3n', ma.FAILED, origin='2026-11-16', reason='RuntimeError: push rejected',
                           when='2026-11-16T17:40:00Z'),
            ma.event(ma.STALE, ma.FITS['CE3n'], ma.STALE_STARTED, 'stale', key='stale:CE3n', source='forecast run',
                     when='2026-11-17T06:00:00Z'),
            *ma.review_events([], {'ce3n': CE3N}, None, '2026-11-23T07:30:00Z'),
        ])

    def named(self, name):
        return xb.named_value(self.book, name)


class ActivityTabTests(WorkbookCase):
    def test_newest_first_with_the_five_columns(self):
        headers, rows = table(self.book, 'Model Activity')
        self.assertEqual(headers, ['Date (EAT)', 'Event', 'Model or list', 'Outcome or status', 'Details'])
        self.assertEqual(len(rows), 6 + 2 + 1 + 3)  # backfilled releases/switches, refits, stale, review lines
        times = [r['Date (EAT)'] for r in rows]
        self.assertEqual(times, sorted(times, reverse=True))
        self.assertEqual(rows[0]['Event'], ma.ROLLBACK)
        self.assertEqual(rows[-1]['Outcome or status'], "RELEASED (Paul's exception)")
        self.assertTrue(rows[-1]['Details'].startswith('Backfilled from git history. The new master'))
        self.assertIn('FAILED: RuntimeError: push rejected', [r['Outcome or status'] for r in rows])
        # Excel serial of the EAT wall clock: 16 Nov 2026 20:20 EAT for the C6 refit at 17:20 UTC
        c6 = next(r for r in rows if r['Model or list'] == ma.FITS['C6'])
        self.assertAlmostEqual(c6['Date (EAT)'], xb.excel_time('2026-11-16T17:20:00Z'))

    def test_conditional_formatting_and_filters(self):
        index = self.book['sheets'].index('Model Activity') + 1
        with ZipFile(self.path) as archive:
            xml = archive.read(f'xl/worksheets/sheet{index}.xml').decode('utf-8')
            tables = [archive.read(n).decode('utf-8') for n in archive.namelist() if n.startswith('xl/tables/')]
        for text in ('ROLLBACK TRIGGERED', 'COMPETITION WARNING', 'FAILED', 'STALE FIT WARNING STARTED',
                     'RELEASED', 'PUBLISHED'):
            self.assertIn(f'&quot;{text}&quot;', xml)
        self.assertEqual(xml.count('<conditionalFormatting'), xml.count('</conditionalFormatting>'))
        self.assertTrue(any('Outcome or status' in t and 'autoFilter' in t for t in tables))

    def test_dashboard_items(self):
        self.assertEqual(self.named('last_c6_refit'), ma.PUBLISHED)
        self.assertEqual(self.named('last_ce3n_refit'), 'FAILED: RuntimeError: push rejected')
        self.assertEqual(self.named('stale_fit_warning'), 'ACTIVE: CE3n')
        self.assertEqual(self.named('switch_settings'),
                         'master live "new", research domestic "v5", research UCL/UEL "v6"')
        self.assertEqual(self.named('last_switch_change'), 'Sun 15 Nov 2026 14:44 EAT')
        dash = json.dumps(self.book['cells']['Dashboard'], ensure_ascii=False)
        for text in ('Research v6 (CE3n) rollback status', 'Live (research v6) - not yet eligible',
                     'CE3n COMPETITION WARNING (UCL)', 'Last rollback check logged Mon 23 Nov 2026 10:30 EAT',
                     'Model Activity'):
            self.assertIn(text, dash)


class NoActivityTests(WorkbookCase):
    activity = False

    def test_empty_log_says_so(self):
        _, rows = table(self.book, 'Model Activity')
        self.assertTrue(rows[0]['Date (EAT)'].startswith('No model activity recorded yet'))
        self.assertEqual(self.named('last_c6_refit'), 'none recorded')
        self.assertEqual(self.named('stale_fit_warning'), 'none active')
        self.assertEqual(self.named('last_switch_change'), 'none recorded')


class MonitoringAdditionTests(WorkbookCase):
    research_extra = {'ucl_live_check': {'version': 'ce3n-ucl-live-check-v1', 'status': 'failed', 'passed_on': None,
                                         'runs': [{'generated_at_utc': '2026-11-24T06:00:00+00:00',
                                                   'status': 'failed', 'ucl_fixtures': 8,
                                                   'problems': ['mapping: home side has no European training name']}]}}

    def competition_table(self):
        cells = self.book['cells']['Model Monitoring']
        row = next(int(a[1:]) for a, v in cells.items() if a.startswith('A')
                   and v == 'CE3n vs CE by competition (research v6): UCL and UEL')
        headers, rows = table(self.book, 'Model Monitoring', row + 1)
        return headers, rows[:2]  # the note under the table follows the two competitions

    def test_competition_table_warning_and_ucl_check(self):
        headers, rows = self.competition_table()
        self.assertEqual(headers, ['Competition', 'Graded matches', 'Weeks', 'CE3n − CE log loss (AH all)',
                                   '95% interval', 'CE3n home slope', 'CE3n away slope', 'CE home slope',
                                   'CE away slope', 'Warning'])
        ucl, uel = rows
        self.assertEqual((ucl['Competition'], ucl['Graded matches'], ucl['Weeks']), ('UCL', 24, 2))
        self.assertAlmostEqual(ucl['CE3n − CE log loss (AH all)'], 0.0031)
        self.assertEqual(ucl['95% interval'], '+0.00040 to +0.00600')
        self.assertAlmostEqual(ucl['CE3n home slope'], 0.88)
        self.assertEqual(ucl['CE3n away slope'], 'not computed yet')
        self.assertEqual(ucl['Warning'], 'CE3n COMPETITION WARNING (UCL)')
        self.assertEqual(uel['Warning'], 'no warning')
        self.assertEqual(self.named('ce3n_competition_warning'), 'CE3n COMPETITION WARNING (UCL)')
        self.assertEqual(self.named('ucl_live_check_status'), 'failed')
        self.assertIn('failed: 8 UCL fixtures (mapping: home side has no European training name)',
                      json.dumps(self.book['cells']['Model Monitoring'], ensure_ascii=False))


class RealShapedCE3nTests(MonitoringAdditionTests):
    """The CE3n figures as research_monitoring.ce3n_rollback_check itself writes them (PR #178's output)."""
    ce3n = real_shaped_ce3n()
    research_extra = {'ucl_live_check': {'version': 'ce3n-ucl-live-check-v1', 'status': 'passed',
                                         'passed_on': {'generated_at_utc': '2026-11-24T06:00:00+00:00',
                                                       'ucl_fixtures': 8, 'snapshot': 'abc'},
                                         'runs': [{'generated_at_utc': '2026-11-24T06:00:00+00:00', 'status': 'passed',
                                                   'ucl_fixtures': 8, 'problems': []}]}}

    def test_competition_table_warning_and_ucl_check(self):
        headers, rows = self.competition_table()
        parts = self.ce3n['by_competition']
        self.assertEqual([r['Competition'] for r in rows], ['UCL', 'UEL'])
        for row in rows:
            part = parts[row['Competition']]
            self.assertEqual(row['Graded matches'], part['matches'])
            self.assertEqual(row['Graded matches'], 20)
            self.assertEqual(row['Weeks'], part['weeks'])
            self.assertAlmostEqual(row['CE3n − CE log loss (AH all)'], part['ce3n_minus_ce_log_loss'])
            low, high = part['interval_95']
            self.assertEqual(row['95% interval'], f'{low:+.5f} to {high:+.5f}')
            for name in ('CE3n', 'CE'):
                for side in ('home', 'away'):
                    self.assertAlmostEqual(row[f'{name} {side} slope'], part['calibration']['slopes'][name][side])
            self.assertEqual(row['Warning'], f'CE3n COMPETITION WARNING ({row["Competition"]})' if part['warning']
                             else 'no warning')
        self.assertEqual(self.named('ucl_live_check_status'), 'passed on the run of Tue 24 Nov 2026 09:00 EAT '
                                                              '(8 UCL fixtures)')
        self.assertEqual(self.named('ce3n_status'), 'Live (research v6) - not yet eligible (40 of 150 graded matches, '
                                                    '4 of 3 weeks)')


class ExistingSheetsUnchangedTests(WorkbookCase):
    """Every sheet main's layout wrote (golden copy: tests/fixtures/performance_workbook_before_activity.json, made by
    performance_report_layout.py at 710381de6 on the same synthetic root) is unchanged, cell for cell, apart from
    the additions: the Dashboard's model-activity block (and the Sheets links below it), Model Monitoring's new
    sections (and the link below them) and the Guide's new rows (and the link below them)."""

    def addition_row(self, sheet):
        cells = self.book['cells'][sheet]
        marks = {'Dashboard': 'Model activity: refits, stale fits, rollback checks and switches',
                 'Model Monitoring': 'CE3n vs CE by competition (research v6): UCL and UEL',
                 'Guide': 'Model Activity'}
        if sheet not in marks:
            return None
        return min(int(''.join(ch for ch in a if ch.isdigit())) for a, v in cells.items()
                   if a.startswith('A') and v == marks[sheet])

    def test_old_cells_names_and_sheet_order(self):
        golden = json.loads(GOLDEN.read_text(encoding='utf-8'))
        self.assertEqual([s for s in self.book['sheets'] if s != 'Model Activity'], golden['sheets'])
        self.assertEqual(self.book['sheets'].index('Model Activity'), self.book['sheets'].index('Model Monitoring') + 1)
        for name, ref in golden['names'].items():
            self.assertEqual(self.book['names'][name], ref, name)
        for sheet, cells in golden['cells'].items():
            new = self.book['cells'][sheet]
            start = self.addition_row(sheet)
            moved = []
            for address, value in cells.items():
                row = int(''.join(ch for ch in address if ch.isdigit()))
                if start is not None and row >= start:
                    moved.append(value)
                    continue
                self.assertEqual(new.get(address), value, f'{sheet}!{address}')
            later = [v for a, v in new.items() if int(''.join(ch for ch in a if ch.isdigit())) >= (start or 0)]
            for value in moved:  # what was below the addition point is still there, further down
                self.assertIn(value, later, f'{sheet}: {value!r}')
            if sheet == 'Dashboard':
                self.assertTrue(all(isinstance(v, str) for v in moved))  # only the Sheets links moved
            if sheet in ('Model Monitoring', 'Guide'):
                self.assertEqual(moved, ['← Dashboard'])


class AppendOnlyCheckTests(unittest.TestCase):
    """workflow_checks.py reports refuses a log whose committed lines changed."""

    def test_appending_passes_and_editing_or_removing_a_committed_line_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            ma.git(repo, 'init', '-q')
            for k, v in (('user.name', 'Test'), ('user.email', 'test@example.test')):
                ma.git(repo, 'config', k, v)
            root = repo / 'football_output_v2'
            log = root / ma.RELATIVE
            first = ma.event(ma.RELEASE, 'new master', 'RELEASED', 'a', key='release', source='backfill',
                             when='2026-11-15T05:23:20Z')
            ma.append(log, [first])
            ma.git(repo, 'add', '.'), ma.git(repo, 'commit', '-q', '-m', 'log')
            self.assertEqual(ma.check(root)['append_only'], 'checked against HEAD')
            ma.append(log, [ma.event(ma.REFIT, 'C6', 'PUBLISHED', 'b', key='refit:C6', source='refit workflow')])
            self.assertEqual(ma.check(root)['events'], 2)
            text = log.read_text(encoding='utf-8')
            log.write_text(text.replace('"details": "a"', '"details": "edited"'), encoding='utf-8', newline=NL)
            with self.assertRaisesRegex(ValueError, 'append only'):
                ma.check(root)
            log.write_text(text.splitlines()[1] + NL, encoding='utf-8', newline=NL)
            with self.assertRaisesRegex(ValueError, 'append only'):
                ma.check(root)
            log.write_text(text + text.splitlines()[1] + NL, encoding='utf-8', newline=NL)
            with self.assertRaisesRegex(ValueError, 'repeated id'):
                ma.check(root)

    def test_the_committed_log_passes(self):
        self.assertGreaterEqual(ma.check(REPO / 'football_output_v2')['events'], 8)


class LayoutDocumentedTests(unittest.TestCase):
    def test_reports_check_expects_the_new_sheet(self):
        import workflow_checks
        self.assertEqual(workflow_checks.REPORT_SHEETS, layout.SHEETS)


if __name__ == '__main__':
    unittest.main()
