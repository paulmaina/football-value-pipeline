"""The master release (decided by Paul on 14 Nov 2026, a deliberate exception: released without waiting for the live
comparison verdict; docs/plan.md, Phase 5).

The new master rule (master_reconciliation, master-new-fill-rule-v4) writes the live master_shortlist.csv and the old
master runs in shadow as master_shortlist_old.csv. One config switch (master_shortlist_config.json, live) restores
the pre-release output byte for byte, proven against digests of main's output (tests/fixtures/
master_release_pre_release.json). Both lists are graded in the weekly report with the release's rollback rule, and
every reader of the live master reads the new one.
"""
from __future__ import annotations

import contextlib
import hashlib
import io
import json
import os
from pathlib import Path
import tempfile
import unittest
import warnings
from unittest import mock

import numpy as np
import pandas as pd

import master_reconciliation as mr
import master_shortlist as ms
import price_edge_cagey_shortlist as v28
import quote_policy
import master_golden as mg
from master_switch import switched
from test_master_reconciliation import production_run

REPO = Path(__file__).resolve().parents[1]
GOLDEN = mg.INDEX
SNAPSHOT = REPO / 'football_output_v2' / 'performance' / 'snapshots' / 'a00d5e530cc2e80e'
RELEASE_FILES = ['master_shortlist.csv', 'master_shortlist_old.csv', 'master_shortlist_old_audit.csv',
                 'master_shortlist_summary.json']


# The production quote policy, pinned for every test here: the golden digests and the saved runs' replay
# (scripts/master_reconciliation_replay.py) use it, while run_offline_tests.py patches quote_policy.CONFIG to the
# offline policy (no bookmaker allowlist), which changes the value and cagey nominations of a saved run.
PRODUCTION_POLICY = REPO / 'shortlist_quote_policy.json'
_POLICY_PATCH = mock.patch.object(quote_policy, 'CONFIG', PRODUCTION_POLICY)


def setUpModule():
    _POLICY_PATCH.start()


def tearDownModule():
    _POLICY_PATCH.stop()


def sha(data) -> str:
    """sha256 with CRLF normalised to LF: pandas writes os.linesep, so a CSV's raw bytes differ between Windows and
    Linux while its content is the same (no field holds a line break)."""
    raw = data if isinstance(data, bytes) else Path(data).read_bytes()
    return hashlib.sha256(raw.replace(b'\r\n', b'\n')).hexdigest()


SHADOW_NAMES = {live: shadow for shadow, live in ms.SUMMARY_RENAMES.items()}


def as_shadow(live: pd.DataFrame) -> pd.DataFrame:
    """The live file in the shadow file's terms: the shadow-period overlap names (in_live_master, ...), the rule version
    in place of the live version, and only the rule's columns."""
    out = live.rename(columns=SHADOW_NAMES)
    out['new_master_version'] = out['new_master_version'].replace(ms.VERSION_NEW_LIVE, mr.VERSION)
    return out[list(mr.COLUMNS)]


def shadow_summary(info):
    """The live summary in the shadow summary's terms (the shadow-period key names)."""
    if isinstance(info, dict):
        return {SHADOW_NAMES.get(k, k): shadow_summary(v) for k, v in info.items()}
    if isinstance(info, list):
        return [shadow_summary(v) for v in info]
    return info


def frozen_inputs():
    predictions, decisions, summary = production_run()
    return predictions, decisions, summary


_SNAPSHOT_INPUTS = {}


def snapshot_inputs():
    """A saved live run (5 Nov 2026 13:37 UTC) rebuilt as scripts/master_reconciliation_replay.py does."""
    if 'value' not in _SNAPSHOT_INPUTS:
        import narrow_margin as nm
        generated = json.loads((SNAPSHOT / 'selection_summary.json').read_text(encoding='utf-8'))['generated_at_utc']
        predictions = pd.read_csv(SNAPSHOT / 'predictions.csv', low_memory=False)
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            policy = quote_policy.load_policy(PRODUCTION_POLICY)
            _, decisions, summary = v28.build_shortlist(predictions, pd.Timestamp(generated),
                                                        execution_policy=policy, model=nm.production_model())
        summary.setdefault('quote_execution_policy', policy)
        _SNAPSHOT_INPUTS['value'] = (predictions, decisions, summary)
    predictions, decisions, summary = _SNAPSHOT_INPUTS['value']
    return predictions, decisions.copy(), json.loads(json.dumps(summary, default=str))


def refresh(inputs, live=None, out=None):
    predictions, decisions, summary = inputs
    out = Path(out or tempfile.mkdtemp())
    with (switched(live) if live else contextlib.nullcontext()), warnings.catch_warnings():
        warnings.simplefilter('ignore')
        ms.refresh(decisions, out, summary, predictions)
    return out, summary


class SwitchTest(unittest.TestCase):
    """master_shortlist_config.json live: "new" is committed; "old" restores today's (pre-release) output."""

    def test_the_committed_switch_releases_the_new_master(self):
        self.assertEqual(ms.configured_live(), ms.LIVE_NEW)
        self.assertEqual(ms.configured_version(), ms.VERSION_PINNACLE_MARKETS)  # the old master's selector, unchanged
        config = ms.load_config()
        self.assertEqual(config['release']['rollback']['min_graded_matches'], 150)
        self.assertEqual(config['release']['rollback']['min_weeks'], 3)
        for bad in ('both', None, 'NEW'):
            data = {**config, 'live': bad}
            with tempfile.TemporaryDirectory() as tmp:
                path = Path(tmp) / 'c.json'
                path.write_text(json.dumps(data), encoding='utf-8')
                with mock.patch.object(ms, 'CONFIG', path), self.assertRaises(ValueError):
                    ms.configured_live()

    def assert_pre_release(self, case, out, summary):
        """Main's pre-release output (tests/fixtures/master_release_pre_release), compared as master_golden says."""
        golden = GOLDEN[case]
        self.assertEqual(sorted(p.name for p in out.iterdir()), golden['files'])
        for name in golden['files']:
            if name.endswith('.csv'):
                problems = mg.frame_differences(mg.read_csv(out / name), mg.read_csv(mg.path(case, name)),
                                                keyed=name in mg.NEW_FILES, label=name)
            else:
                problems = mg.json_differences(json.loads((out / name).read_text(encoding='utf-8')),
                                               mg.golden_json(case, name), name)
            self.assertEqual(problems, [], name)
        self.assertEqual(mg.json_differences(json.loads(json.dumps(summary['master_shortlist'], default=str)),
                                             mg.golden_json(case, 'run_summary_master_shortlist.json')), [])
        self.assertNotIn(ms.OLD_SUMMARY_KEY, summary)

    def test_the_golden_files_are_mains_output(self):
        """The committed copies are byte for byte (LF) the digests recorded from main ebba9d8."""
        for case in mg.CASES:
            for name in GOLDEN[case]['files']:
                self.assertEqual(sha(mg.path(case, name)), GOLDEN[case][name], (case, name))

    def test_old_restores_the_pre_release_output_on_the_frozen_forecast(self):
        out, summary = refresh(frozen_inputs(), 'old')
        self.assert_pre_release('frozen_forecast', out, summary)

    def test_old_restores_the_pre_release_output_on_a_saved_run(self):
        out, summary = refresh(snapshot_inputs(), 'old')
        self.assert_pre_release('snapshot_a00d5e530cc2e80e', out, summary)

    def test_switching_back_and_forth_leaves_only_the_chosen_modes_files(self):
        out = Path(tempfile.mkdtemp())
        refresh(frozen_inputs(), 'new', out)
        _, summary = refresh(frozen_inputs(), 'old', out)
        self.assert_pre_release('frozen_forecast', out, summary)
        refresh(frozen_inputs(), 'new', out)
        self.assertEqual(sorted(p.name for p in out.iterdir()), sorted(RELEASE_FILES))


class RoleSwapTest(unittest.TestCase):
    """live "new": master_shortlist.csv is main's master_shortlist_new.csv and master_shortlist_old.csv is main's
    master_shortlist.csv, byte for byte apart from file names and the version field."""

    def assert_swapped(self, case, out, summary):
        self.assertEqual(sorted(p.name for p in out.iterdir()), sorted(RELEASE_FILES))
        old = lambda name: mg.read_csv(mg.path(case, name))
        self.assertEqual(mg.frame_differences(mg.read_csv(out / ms.OLD_FILE), old('master_shortlist.csv')), [])
        self.assertEqual(mg.frame_differences(mg.read_csv(out / ms.OLD_AUDIT_FILE), old('master_shortlist_audit.csv')),
                         [])
        self.assertEqual(mg.json_differences(json.loads(json.dumps(summary[ms.OLD_SUMMARY_KEY], default=str)),
                                             mg.golden_json(case, 'run_summary_master_shortlist.json')), [])
        live = mg.read_csv(out / ms.FILE)
        self.assertEqual(mg.frame_differences(as_shadow(live), old('master_shortlist_new.csv'), keyed=True), [])
        written = json.loads((out / ms.SUMMARY_FILE).read_text(encoding='utf-8'))
        strip = lambda info: {k: v for k, v in info.items() if k not in ('version', 'status', 'note')}
        self.assertEqual(mg.json_differences(strip(shadow_summary(written)),
                                             strip(mg.golden_json(case, 'master_shortlist_new_summary.json'))), [])
        # the live file's own order is the platform-independent one
        pd.testing.assert_frame_equal(live, mg.read_csv(mr.stable_order(live).to_csv(index=False).encode()))
        self.assertEqual(summary['master_shortlist'], written)
        self.assertEqual((written['version'], written['status'], written['note']),
                         (ms.VERSION_NEW_LIVE, ms.LIVE_STATUS, ms.LIVE_NOTE))
        frame = pd.read_csv(out / ms.FILE)
        self.assertEqual(list(frame.columns), ms.live_columns())
        self.assertEqual(set(frame.new_master_version), {ms.VERSION_NEW_LIVE} if len(frame) else set())
        return frame

    def test_frozen_forecast(self):
        out, summary = refresh(frozen_inputs())  # the committed config
        frame = self.assert_swapped('frozen_forecast', out, summary)
        self.assertEqual(int(frame.new_master_decision.eq('SHORTLISTED').sum()), summary['master_shortlist']
                         ['ranked_fixtures'])

    def test_saved_run(self):
        out, summary = refresh(snapshot_inputs())
        frame = self.assert_swapped('snapshot_a00d5e530cc2e80e', out, summary)
        self.assertEqual(int(frame.new_master_decision.eq('SHORTLISTED').sum()), 15)

    def test_same_machine_role_separation_byte_for_byte(self):
        """On one machine: live "new" writes the old master's shadow files byte for byte as live "old" writes the live
        ones, and the live file is exactly the old mode's shadow new master (stable order, live version)."""
        for inputs in (frozen_inputs, snapshot_inputs):
            old_out, old_summary = refresh(inputs(), 'old')
            new_out, new_summary = refresh(inputs())
            self.assertEqual((new_out / ms.OLD_FILE).read_bytes(), (old_out / ms.FILE).read_bytes())
            self.assertEqual((new_out / ms.OLD_AUDIT_FILE).read_bytes(),
                             (old_out / 'master_shortlist_audit.csv').read_bytes())
            self.assertEqual(new_summary[ms.OLD_SUMMARY_KEY], old_summary['master_shortlist'])
            shadow = mg.read_csv(old_out / 'master_shortlist_new.csv')
            live = mg.read_csv(new_out / ms.FILE)
            expected = mg.read_csv(mr.stable_order(shadow).to_csv(index=False).encode())
            pd.testing.assert_frame_equal(as_shadow(live), expected, check_exact=True)
            shadow_info = json.loads((old_out / 'master_shortlist_new_summary.json').read_text(encoding='utf-8'))
            strip = lambda info: {k: v for k, v in info.items() if k not in ('version', 'status', 'note')}
            self.assertEqual(strip(shadow_summary(new_summary['master_shortlist'])), strip(shadow_info))

    def test_the_live_file_names_its_overlap_columns_after_the_old_master(self):
        out, summary = refresh(snapshot_inputs())
        live = pd.read_csv(out / ms.FILE)
        for shadow_name, live_name in (('in_live_master', 'in_old_master'), ('live_master_rank', 'old_master_rank'),
                                       ('live_master_same_offer', 'old_master_same_offer')):
            self.assertIn(live_name, live.columns)
            self.assertNotIn(shadow_name, live.columns)
        info = summary['master_shortlist']
        self.assertIn('overlap_with_old_master', info)
        self.assertNotIn('overlap_with_live_master', info)
        self.assertEqual(set(info['overlap_with_old_master']),
                         {'old_master_fixtures', 'new_master_fixtures', 'same_fixture', 'same_offer', 'old_only',
                          'new_only'})
        self.assertTrue({'in_old_master', 'old_master_same_offer'} <= set(info['top_picks'][0]))
        # the old master's picks are the old shadow file's: the overlap columns point at them
        old = pd.read_csv(out / ms.OLD_FILE)
        picks = live.loc[live.new_master_decision.eq('SHORTLISTED')]
        self.assertEqual(int(picks.in_old_master.sum()), info['overlap_with_old_master']['same_fixture'])
        self.assertTrue(set(picks.loc[picks.in_old_master, 'old_master_rank'].astype(int)) <= set(old.master_rank))
        # live "old" keeps the shadow-period names in master_shortlist_new.csv (pre-release bytes)
        shadow_out, _ = refresh(snapshot_inputs(), 'old')
        self.assertIn('in_live_master', pd.read_csv(shadow_out / 'master_shortlist_new.csv').columns)

    def test_the_version_is_bumped_and_distinct(self):
        self.assertNotIn(ms.VERSION_NEW_LIVE, ms.VERSIONS)
        self.assertNotEqual(ms.VERSION_NEW_LIVE, mr.VERSION)
        self.assertTrue(ms.VERSION_NEW_LIVE.startswith(mr.VERSION))
        self.assertTrue(ms.VERSION_NEW_LIVE.endswith('-v10'))  # after master-profit-15-pinnacle-markets-v9

    def test_other_policies_remove_every_master_file(self):
        out = Path(tempfile.mkdtemp())
        for name in (*RELEASE_FILES, 'master_shortlist_audit.csv', 'master_shortlist_new.csv'):
            (out / name).write_text('stale', encoding='utf-8')
        info = {'selection_policy_version': 'other', 'master_shortlist': {}, ms.OLD_SUMMARY_KEY: {}}
        self.assertIsNone(ms.refresh(pd.DataFrame(), out, info))
        self.assertEqual(list(out.iterdir()), [])
        self.assertEqual(info, {'selection_policy_version': 'other'})

    def test_decision_rows_are_never_touched(self):
        predictions, decisions, summary = frozen_inputs()
        before = decisions.to_csv(index=False)
        refresh((predictions, decisions, summary))
        self.assertEqual(decisions.to_csv(index=False), before)


class FailureTest(unittest.TestCase):
    """A new-master failure publishes the old master for that run (NEW MASTER FAILED - OLD MASTER PUBLISHED); an
    old-master (shadow) failure keeps the new master and records that the run has no comparison baseline."""

    def test_a_new_master_failure_publishes_the_old_master_for_that_run(self):
        for inputs in (frozen_inputs, snapshot_inputs):
            old_out, old_summary = refresh(inputs(), 'old')
            predictions, decisions, summary = inputs()
            out = Path(tempfile.mkdtemp())
            (out / ms.SUMMARY_FILE).write_text('stale', encoding='utf-8')
            with mock.patch.object(mr, 'reconcile', side_effect=RuntimeError('boom')), \
                    self.assertWarnsRegex(UserWarning, 'NEW MASTER FAILED - OLD MASTER PUBLISHED'):
                frame = ms.refresh(decisions, out, summary, predictions)
            # exactly what live "old" publishes, without the shadow new master
            self.assertEqual(sorted(p.name for p in out.iterdir()), [ms.FILE, 'master_shortlist_audit.csv'])
            self.assertEqual((out / ms.FILE).read_bytes(), (old_out / ms.FILE).read_bytes())
            self.assertEqual((out / 'master_shortlist_audit.csv').read_bytes(),
                             (old_out / 'master_shortlist_audit.csv').read_bytes())
            self.assertEqual(summary['master_shortlist'], old_summary['master_shortlist'])
            self.assertNotIn(ms.OLD_SUMMARY_KEY, summary)
            self.assertEqual(summary[ms.RELEASE_STATUS_KEY]['status'], 'NEW MASTER FAILED - OLD MASTER PUBLISHED')
            self.assertEqual(summary[ms.RELEASE_STATUS_KEY]['error'], 'RuntimeError: boom')
            self.assertEqual(len(frame), old_summary['master_shortlist']['n_bets'])
            self.assertEqual(ms.configured_live(), ms.LIVE_NEW)  # the switch is untouched

    def test_the_runs_report_says_so(self):
        from format_football_output import master_section
        predictions, decisions, summary = frozen_inputs()
        out = Path(tempfile.mkdtemp())
        with mock.patch.object(mr, 'reconcile', side_effect=ValueError('bad rows')), warnings.catch_warnings():
            warnings.simplefilter('ignore')
            ms.refresh(decisions, out, summary, predictions)
        text = '\n'.join(master_section(summary, out, Path(tempfile.mkdtemp())))
        self.assertIn('**NEW MASTER FAILED - OLD MASTER PUBLISHED** in this run (ValueError: bad rows)', text)
        self.assertLess(text.index('## '), text.index('NEW MASTER FAILED'))

    def test_both_masters_failing_fails_the_run(self):
        predictions, decisions, summary = frozen_inputs()
        with mock.patch.object(mr, 'reconcile', side_effect=RuntimeError('new')), \
                mock.patch.object(ms, '_old_master', side_effect=RuntimeError('old')), warnings.catch_warnings(), \
                self.assertRaisesRegex(RuntimeError, 'new'):
            warnings.simplefilter('ignore')
            ms.refresh(decisions, Path(tempfile.mkdtemp()), summary, predictions)

    def test_an_old_shadow_failure_keeps_the_new_master_and_records_the_missing_baseline(self):
        from format_football_output import master_section
        predictions, decisions, summary = frozen_inputs()
        normal, normal_summary = refresh(frozen_inputs())
        out = Path(tempfile.mkdtemp())
        with mock.patch.object(ms, '_old_master', side_effect=RuntimeError('boom')), \
                self.assertWarnsRegex(UserWarning, 'COMPARISON BASELINE MISSING'):
            ms.refresh(decisions, out, summary, predictions)
        self.assertEqual(sorted(p.name for p in out.iterdir()), [ms.FILE, ms.SUMMARY_FILE])
        self.assertNotIn(ms.OLD_SUMMARY_KEY, summary)
        self.assertEqual(summary[ms.RELEASE_STATUS_KEY]['status'], 'COMPARISON BASELINE MISSING')
        self.assertEqual(summary[ms.RELEASE_STATUS_KEY]['old_master_version'], ms.VERSION_PINNACLE_MARKETS)
        expected, info = ms.new_live(decisions, None, summary['generated_at_utc'], predictions)
        self.assertTrue(ms.matches_new(pd.read_csv(out / ms.FILE), expected))
        self.assertEqual(summary['master_shortlist'], info)
        # the picks are the normal run's: only the comparison with the old master is missing
        picks = lambda f: f.loc[f.new_master_decision.eq('SHORTLISTED'), ['home_team', 'market', 'new_master_rank']]
        pd.testing.assert_frame_equal(picks(pd.read_csv(out / ms.FILE)), picks(pd.read_csv(normal / ms.FILE)))
        text = '\n'.join(master_section(summary, out, Path(tempfile.mkdtemp())))
        self.assertIn('**COMPARISON BASELINE MISSING** in this run (RuntimeError: boom)', text)


KICK = pd.Timestamp('2026-11-21T15:00:00Z')


def new_row(home, decision='SHORTLISTED', market='Asian Handicap Home +0.50', side='home', line=0.5, price=1.6,
            version=None, generated=None, kick=KICK):
    generated = generated or (kick - pd.Timedelta(hours=20)).isoformat()
    return {'new_master_rank': 1 if decision == 'SHORTLISTED' else None, 'new_master_tier': 'safe',
            'new_master_group': 'included', 'new_master_decision': decision, 'league': 'Premier League',
            'home_team': home, 'away_team': 'Away FC', 'kickoff_utc': kick.isoformat(), 'market': market,
            'market_to_bet': market, 'handicap_side': side, 'handicap_line': line, 'bookmaker': 'Pinnacle',
            'offered_decimal_odds': price, 'per_stake_cost': 0., 'fair_odds': 1.5, 'reference_type': 'c-cagey',
            'evaluated_at_utc': generated, 'selection_policy_version': v28.POLICY,
            'new_master_version': version or ms.VERSION_NEW_LIVE, 'gap_check': 'agree', 'new_master_labels': '',
            'both_agree': False, 'research_too_optimistic': False, 'inspection_flag': False, 'one_view_missing': False,
            'no_research_check': False, 'unvalidated_view': False}


def old_row(home, market='Asian Handicap Away +1.00', side='away', line=1.0, price=1.4, generated=None, kick=KICK):
    generated = generated or (kick - pd.Timedelta(hours=20)).isoformat()
    return {'master_rank': 1, 'league': 'Premier League', 'home_team': home, 'away_team': 'Away FC',
            'kickoff_utc': kick.isoformat(), 'market': market, 'market_to_bet': market, 'handicap_side': side,
            'handicap_line': line, 'bookmaker': 'Pinnacle', 'offered_decimal_odds': price, 'per_stake_cost': 0.,
            'evaluated_at_utc': generated, 'selection_policy_version': v28.POLICY,
            'master_price_flag': 'value', 'master_version': ms.VERSION_PINNACLE_MARKETS}


def archive(root, snapshots):
    """snapshots: (sha, generated, captured, {file name: rows}) each."""
    out = []
    for sha_, generated, captured, files in snapshots:
        directory = root / 'performance' / 'snapshots' / sha_[:16]
        directory.mkdir(parents=True)
        for name, rows in files.items():
            if name.endswith('.json'):  # the archived run summary (selection_summary.json)
                (directory / name).write_text(json.dumps(rows), encoding='utf-8')
            else:
                pd.DataFrame(rows).to_csv(directory / name, index=False)
        out.append(({'git_commit_sha': sha_, 'captured_at_utc': captured.isoformat(),
                     'generated_at_utc': generated.isoformat(), 'selection_policy_version': v28.POLICY,
                     'sha256': {name: '0' * 64 for name in files}}, [], []))
    return out


def frame(profits, start='2026-11-16', per_week=50):
    kicks = [pd.Timestamp(start, tz='UTC') + pd.Timedelta(days=7 * (i // per_week), minutes=10 * (i % per_week))
             for i in range(len(profits))]
    return pd.DataFrame({'kickoff_utc': [k.isoformat() for k in kicks], 'unit_profit': profits,
                         'offered_decimal_odds': 1.5})


class RollbackTest(unittest.TestCase):
    """After at least 150 graded matches over at least 3 weeks, new minus old flat-stake return per bet with its 95%
    interval entirely below zero: ROLLBACK TRIGGERED, reported only."""

    def test_waits_for_150_matches_over_3_weeks_on_each_list(self):
        import price_edge_tracking as tracking
        worse, old = [-1.] * 149, [0.4] * 200
        self.assertEqual(tracking.master_rollback(frame(worse), frame(old), 'new')['status'], 'WAITING')
        two_weeks = tracking.master_rollback(frame([-1.] * 160, per_week=80), frame([0.4] * 160, per_week=80), 'new')
        self.assertEqual((two_weeks['status'], two_weeks['triggered']), ('WAITING', False))
        self.assertEqual(tracking.master_rollback(frame([-1.] * 150), frame([0.4] * 149), 'new')['status'], 'WAITING')

    def test_triggered_only_when_the_interval_is_entirely_below_zero(self):
        import price_edge_tracking as tracking
        rng = np.random.default_rng(3)
        old = frame(list(rng.choice([0.4, -1.], 200, p=[.75, .25])))
        worse = frame(list(rng.choice([0.4, -1.], 200, p=[.45, .55])))
        out = tracking.master_rollback(worse, old, 'new')
        self.assertEqual((out['status'], out['triggered']), (tracking.ROLLBACK_TRIGGERED, True))
        self.assertLess(out['interval_95'][1], 0)
        self.assertTrue(out['message'].startswith('ROLLBACK TRIGGERED: new master minus old master'))
        self.assertIn('Nothing has been switched', out['message'])
        same = tracking.master_rollback(old, old, 'new')
        self.assertEqual((same['status'], same['triggered']), ('NOT TRIGGERED', False))
        better = tracking.master_rollback(old, worse, 'new')
        self.assertEqual((better['status'], better['triggered']), ('NOT TRIGGERED', False))

    def test_it_uses_the_live_comparisons_interval(self):
        import price_edge_tracking as tracking
        rng = np.random.default_rng(4)
        old, new = frame(list(rng.choice([0.4, -1.], 200))), frame(list(rng.choice([0.4, -1.], 200)))
        comparison = tracking.compare_masters(new, old, mr.load_config()['live_comparison'])
        rollback = tracking.master_rollback(new, old, 'new')
        self.assertEqual((rollback['difference'], rollback['interval_95']),
                         (comparison['difference'], comparison['interval_95']))

    def test_not_applied_while_the_old_master_is_live(self):
        import price_edge_tracking as tracking
        out = tracking.master_rollback(frame([-1.] * 200), frame([0.4] * 200), 'old')
        self.assertEqual((out['status'], out['triggered']), ('OLD MASTER LIVE', False))
        with switched('old'):
            self.assertEqual(tracking.master_rollback(frame([-1.] * 200), frame([0.4] * 200))['status'],
                             'OLD MASTER LIVE')

    def test_the_weekly_report_says_rollback_triggered_at_the_top(self):
        """150 matches over 3 weeks on each list, every new pick losing and every old pick winning: triggered, at the
        top of the report, in its summary, and graded from the live file (new) and the shadow file (old)."""
        import price_edge_tracking as tracking
        final = {'home_goals': 0, 'away_goals': 1}  # home +0.50 loses, away +1.00 wins
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            snaps = []
            for week in range(3):
                kick = KICK + pd.Timedelta(days=7 * week)
                generated = kick - pd.Timedelta(hours=20)
                kicks = [kick + pd.Timedelta(minutes=i) for i in range(50)]
                snaps.append((f'{week}' * 40, generated, generated, {
                    ms.FILE: [new_row(f'Team {week}-{i}', kick=k, generated=generated.isoformat())
                              for i, k in enumerate(kicks)]
                    + [new_row(f'Team {week}-0', decision='LEFT_OUT', market='Home win', kick=kicks[0],
                               generated=generated.isoformat())],
                    ms.OLD_FILE: [old_row(f'Team {week}-{i}', kick=k, generated=generated.isoformat())
                                  for i, k in enumerate(kicks)]}))
            arch = archive(root, snaps)
            with mock.patch('closing_odds.load_observations', return_value=([], [])), \
                    mock.patch('performance_tracking.fixture_match', return_value=(final, 'VERIFIED_FINISHED')):
                summary = tracking.review(root, arch, [], KICK + pd.Timedelta(days=21))
            report = (root / tracking.OUTPUT_DIR / 'report.md').read_text(encoding='utf-8')
        self.assertEqual((summary['new_master_picks'], summary['master_picks']), (150, 150))
        self.assertAlmostEqual(summary['new_master']['profit']['mean'], -1.0)
        self.assertAlmostEqual(summary['master']['profit']['mean'], 0.4)
        self.assertEqual(summary['live_master_list'], 'new')
        rollback = summary['master_rollback']
        self.assertTrue(rollback['triggered'])
        lines = report.splitlines()
        self.assertEqual(lines[0], '# v27/v28 price-edge tracking')
        self.assertTrue(lines[2].startswith('> **ROLLBACK TRIGGERED** (master shortlist): ROLLBACK TRIGGERED'))
        self.assertIn('## Master shortlist: new master (live since 14 Nov 2026) beside the old master (shadow)',
                      report)
        self.assertIn('**Rollback status: ROLLBACK TRIGGERED.**', report)
        self.assertIn('## Old master (shadow since 14 Nov 2026; master_shortlist_old.csv)', report)

    def test_no_banner_while_waiting(self):
        import price_edge_tracking as tracking
        final = {'home_goals': 0, 'away_goals': 1}
        generated = KICK - pd.Timedelta(hours=20)
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            arch = archive(root, [('a' * 40, generated, generated,
                                   {ms.FILE: [new_row('Home FC')], ms.OLD_FILE: [old_row('Home FC')]})])
            with mock.patch('closing_odds.load_observations', return_value=([], [])), \
                    mock.patch('performance_tracking.fixture_match', return_value=(final, 'VERIFIED_FINISHED')):
                summary = tracking.review(root, arch, [], KICK + pd.Timedelta(hours=5))
            report = (root / tracking.OUTPUT_DIR / 'report.md').read_text(encoding='utf-8')
        self.assertEqual(summary['master_rollback']['status'], 'WAITING')
        self.assertNotIn('> **ROLLBACK TRIGGERED**', report)
        self.assertLess(report.index('## Master shortlist: new master'), report.index('## Old master (shadow'))
        self.assertIn('**Rollback status: WAITING.**', report)

    def test_a_missing_baseline_is_never_an_ordinary_wait(self):
        import price_edge_tracking as tracking
        out = tracking.master_rollback(frame([-1.] * 20), frame([0.4] * 20), 'new', baseline_missing_runs=2)
        self.assertEqual((out['status'], out['triggered']), ('COMPARISON BASELINE MISSING', False))
        self.assertTrue(out['message'].startswith('Comparison baseline missing in 2 runs (the old master shadow '
                                                  'failed); not triggered: waiting'))
        rng = np.random.default_rng(3)
        old = frame(list(rng.choice([0.4, -1.], 200, p=[.75, .25])))
        worse = frame(list(rng.choice([0.4, -1.], 200, p=[.45, .55])))
        triggered = tracking.master_rollback(worse, old, 'new', baseline_missing_runs=1)
        self.assertEqual(triggered['status'], tracking.ROLLBACK_TRIGGERED)
        self.assertIn('Comparison baseline missing in 1 run (the old master shadow failed).', triggered['message'])
        self.assertEqual(tracking.master_rollback(frame([-1.] * 20), frame([0.4] * 20), 'new')['status'], 'WAITING')

    def test_the_weekly_report_counts_release_incidents_and_grades_across_them(self):
        """Three runs: a normal one, one whose new master failed (the old master was published live) and one whose
        old master shadow failed. The report and the reports check name both incidents with their counts, the
        rollback status says the baseline is missing, and each list is graded from the right file."""
        import price_edge_tracking as tracking
        import workflow_checks
        final = {'home_goals': 0, 'away_goals': 1}
        run_info = lambda **extra: {'selection_policy_version': v28.POLICY,
                                    'master_shortlist': {'version': ms.VERSION_NEW_LIVE}, **extra}
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            gens = [KICK - pd.Timedelta(hours=h) for h in (22, 21, 20)]
            arch = archive(root, [
                ('a' * 40, gens[0], gens[0], {
                    ms.FILE: [new_row('Normal FC', generated=gens[0].isoformat())],
                    ms.OLD_FILE: [old_row('Normal FC', generated=gens[0].isoformat())],
                    'selection_summary.json': run_info(**{ms.OLD_SUMMARY_KEY: {}})}),
                ('b' * 40, gens[1], gens[1], {
                    ms.FILE: [old_row('Fallback FC', generated=gens[1].isoformat())],
                    'selection_summary.json': {
                        'selection_policy_version': v28.POLICY,
                        'master_shortlist': {'version': ms.VERSION_PINNACLE_MARKETS},
                        ms.RELEASE_STATUS_KEY: {'status': ms.NEW_MASTER_FAILED, 'error': 'RuntimeError: boom'}}}),
                ('c' * 40, gens[2], gens[2], {
                    ms.FILE: [new_row('Baseline FC', generated=gens[2].isoformat())],
                    'selection_summary.json': run_info(**{ms.RELEASE_STATUS_KEY: {
                        'status': ms.BASELINE_MISSING, 'error': 'KeyError: x'}})})])
            with mock.patch('closing_odds.load_observations', return_value=([], [])), \
                    mock.patch('performance_tracking.fixture_match', return_value=(final, 'VERIFIED_FINISHED')):
                summary = tracking.review(root, arch, [], KICK + pd.Timedelta(hours=5))
            report = (root / tracking.OUTPUT_DIR / 'report.md').read_text(encoding='utf-8')
            incidents = summary['master_release_incidents']
            self.assertEqual((incidents['new_master_failed']['runs'], incidents['baseline_missing']['runs']), (1, 1))
            self.assertEqual(incidents['new_master_failed']['details'][0]['error'], 'RuntimeError: boom')
            self.assertEqual(summary['master_rollback']['status'], 'COMPARISON BASELINE MISSING')
            self.assertNotIn('**Rollback status: WAITING.**', report)
            self.assertIn('**Rollback status: COMPARISON BASELINE MISSING.** Comparison baseline missing in 1 run',
                          report)
            top = report.split('## ')[0]
            self.assertIn('> **NEW MASTER FAILED - OLD MASTER PUBLISHED** (master shortlist) in 1 run', top)
            self.assertIn('> **Comparison baseline missing** (master shortlist) in 1 run', top)
            # grading across the incidents: the fallback run's live file is graded as the old master
            self.assertEqual(sorted(r['home_team'] for r in tracking.frozen_new_master_picks(root, arch)),
                             ['Baseline FC', 'Normal FC'])
            self.assertEqual(sorted(r['home_team'] for r in tracking.frozen_old_master_picks(root, arch)),
                             ['Fallback FC', 'Normal FC'])
            # the reports check and its run summary carry both, never as an ordinary wait
            path = root / tracking.OUTPUT_DIR / 'summary.json'
            stored = json.loads(path.read_text(encoding='utf-8'))
            self.assertEqual(stored['master_release_incidents']['messages'], incidents['messages'])
            step = Path(tmp) / 'step.md'
            with mock.patch.dict(os.environ, {'GITHUB_STEP_SUMMARY': str(step)}), \
                    contextlib.redirect_stdout(io.StringIO()):
                workflow_checks.emit({'status': 'VERIFIED_WITH_WARNINGS', 'warnings': incidents['messages'],
                                      'master_release_incidents': incidents}, summary=True)
            text = step.read_text(encoding='utf-8')
        self.assertTrue(text.startswith('> **NEW MASTER FAILED - OLD MASTER PUBLISHED** (master shortlist) in 1 run'))
        self.assertIn('> **Comparison baseline missing** (master shortlist) in 1 run', text)
        source = (REPO / 'workflow_checks.py').read_text(encoding='utf-8')
        self.assertIn("for message in reversed(incidents.get('messages', [])): warnings.insert(0, message)", source)

    def test_an_unrecorded_missing_shadow_still_counts(self):
        import price_edge_tracking as tracking
        generated = KICK - pd.Timedelta(hours=20)
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            arch = archive(root, [('d' * 40, generated, generated, {
                ms.FILE: [new_row('Home FC')], 'selection_summary.json': {
                    'master_shortlist': {'version': ms.VERSION_NEW_LIVE}}})])
            incidents = tracking.master_release_incidents(root, arch)
        self.assertEqual(incidents['baseline_missing']['runs'], 1)
        self.assertEqual(incidents['baseline_missing']['details'][0]['error'], 'not recorded')

    def test_the_run_summary_carries_it_first(self):
        import workflow_checks
        message = 'ROLLBACK TRIGGERED: new master minus old master ...'
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'summary.md'
            with mock.patch.dict(os.environ, {'GITHUB_STEP_SUMMARY': str(path)}), \
                    contextlib.redirect_stdout(io.StringIO()):
                workflow_checks.emit({'status': 'VERIFIED_WITH_WARNINGS', 'warnings': [message],
                                      'master_rollback': {'triggered': True, 'status': 'ROLLBACK TRIGGERED',
                                                          'message': message}}, summary=True)
            text = path.read_text(encoding='utf-8')
        self.assertTrue(text.startswith('> **ROLLBACK TRIGGERED** (master shortlist): ROLLBACK TRIGGERED'))

    def test_report_check_and_the_review_pass_it_on(self):
        source = (REPO / 'workflow_checks.py').read_text(encoding='utf-8')
        self.assertIn("'master_rollback':rollback", source)
        self.assertIn("if rollback.get('triggered'): warnings.insert(0, rollback['message'])", source)
        review = (REPO / 'performance_tracking.py').read_text(encoding='utf-8')
        self.assertIn("rollback = (price_edge or {}).get('master_rollback') or {}", review)
        self.assertIn("print(rollback['message'], file=sys.stderr)", review)


class ReadersTest(unittest.TestCase):
    """Every reader of the live master reads the new one; the old master is read only as the shadow."""

    def test_capture_archives_the_live_new_master_and_the_old_shadow(self):
        import price_edge_tracking as tracking
        out, summary = refresh(frozen_inputs())
        generated = summary['generated_at_utc']
        self.assertEqual(tracking.capture_master_file(out, generated), out / ms.FILE)
        self.assertEqual(tracking.capture_old_master_file(out, generated), out / ms.OLD_FILE)
        self.assertIsNone(tracking.capture_new_master_file(out, generated))  # no shadow new master any more
        later = (pd.Timestamp(generated) + pd.Timedelta(hours=1)).isoformat()
        self.assertIsNone(tracking.capture_master_file(out, later))
        self.assertIsNone(tracking.capture_old_master_file(out, later))

    def test_the_old_file_is_an_allowed_snapshot_sidecar(self):
        import prediction_runs
        import workflow_checks
        self.assertIn(ms.OLD_FILE, prediction_runs.SIDECARS)
        self.assertIn(ms.OLD_FILE, workflow_checks.SIDECARS)
        source = (REPO / 'performance_tracking.py').read_text(encoding='utf-8')
        self.assertIn("'master_shortlist_old.csv'}", source)
        self.assertIn('capture_old_master_file', source)

    def test_grading_reads_each_list_from_both_eras(self):
        """New master: its shadow file before the release, the live file since (ranked picks only). Old master: the
        live file before the release (old rows only), its shadow file since."""
        import price_edge_tracking as tracking
        day = KICK.normalize()
        before, after = day - pd.Timedelta(hours=14), day - pd.Timedelta(hours=10)
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            arch = archive(root, [
                ('a' * 40, before, before, {ms.FILE: [old_row('Old Era FC')],
                                            'master_shortlist_new.csv': [new_row('Old Era FC', version=mr.VERSION)]}),
                ('b' * 40, after, after, {ms.FILE: [new_row('New Era FC'), new_row('Left FC', decision='LEFT_OUT')],
                                          ms.OLD_FILE: [old_row('New Era FC')]})])
            new = tracking.frozen_new_master_picks(root, arch)
            old = tracking.frozen_old_master_picks(root, arch)
            counts = tracking.new_master_offer_counts(root, arch)
        self.assertEqual(sorted((r['home_team'], r['new_master_version']) for r in new),
                         [('New Era FC', ms.VERSION_NEW_LIVE), ('Old Era FC', mr.VERSION)])
        self.assertEqual(sorted(r['home_team'] for r in old), ['New Era FC', 'Old Era FC'])
        self.assertTrue(all('new_master_decision' not in r for r in old))
        self.assertEqual((counts['fixtures'], counts['offers']), (3, 3))
        self.assertIs(tracking.frozen_master_picks, tracking.frozen_old_master_picks)

    def test_closing_odds_collect_the_new_masters_picks_and_the_old_shadow(self):
        import closing_odds
        import price_edge_tracking
        predictions = [{'league': 'Premier League', 'home_team': h, 'away_team': 'Away FC',
                        'kickoff_utc': KICK.isoformat()} for h in ('Pick FC', 'Left FC', 'Old FC')]
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            raw = root / 'raw'
            raw.mkdir()
            pd.DataFrame([new_row('Pick FC'), new_row('Left FC', decision='LEFT_OUT', market='Home win')]) \
                .to_csv(raw / ms.FILE, index=False)
            pd.DataFrame([old_row('Old FC')]).to_csv(raw / ms.OLD_FILE, index=False)
            with mock.patch('performance_tracking.snapshots', return_value=[]), \
                    mock.patch.object(price_edge_tracking, 'archived_tier_rows', return_value=[]):
                targets = closing_odds.collection_targets(root, predictions, [])
        markets = {source['home_team']: selected for source, selected in targets}
        self.assertEqual(markets['Pick FC'], {'Asian Handicap Home +0.50'})
        self.assertEqual(markets['Left FC'], set())  # a nominated offer the master did not pick
        self.assertEqual(markets['Old FC'], {'Asian Handicap Away +1.00'})

    def test_readable_output_and_workbook_show_the_new_masters_picks(self):
        from format_football_output import (MASTER_READABLE, master_section, read_shortlist_tabs,
                                            write_predictions_workbook)
        from zipfile import ZipFile
        out, summary = refresh(snapshot_inputs())
        readable_dir = Path(tempfile.mkdtemp())
        lines = master_section(summary, out, readable_dir)
        readable = pd.read_csv(readable_dir / MASTER_READABLE)
        live = pd.read_csv(out / ms.FILE)
        picks = live.loc[live.new_master_decision.eq('SHORTLISTED')].sort_values('new_master_rank')
        self.assertEqual(list(readable.Rank), list(picks.new_master_rank))
        self.assertEqual(list(readable.Home), list(picks.home_team))
        self.assertEqual(list(readable['Market to bet']), list(picks.market_to_bet))
        self.assertEqual(len(readable), 15)
        self.assertIn('In old master (shadow)', readable.columns)
        text = '\n'.join(lines)
        self.assertIn('Master shortlist (new master rule, live since 14 Nov 2026; target 15 matches)', text)
        self.assertIn('safe 13, fill 2, risky fill 0', text)
        book = write_predictions_workbook([], readable_dir / 'book.xlsx', read_shortlist_tabs(readable_dir))
        with ZipFile(book) as archive_:
            sheet = archive_.read('xl/worksheets/sheet1.xml').decode()
            names = archive_.read('xl/workbook.xml').decode()
        self.assertIn('Master shortlist', names)
        self.assertIn(str(picks.iloc[0].home_team), sheet)

    def test_readable_output_under_the_old_switch_is_the_old_master(self):
        from format_football_output import MASTER_READABLE, master_section
        out, summary = refresh(frozen_inputs(), 'old')
        readable_dir = Path(tempfile.mkdtemp())
        master_section(summary, out, readable_dir)
        readable = pd.read_csv(readable_dir / MASTER_READABLE)
        self.assertEqual(list(readable.Home), list(pd.read_csv(out / ms.FILE).home_team))
        self.assertNotIn('Tier (safe / fill / risky fill)', readable.columns)

    def test_staking_recommendation_history_and_the_performance_workbook_never_read_a_master_file(self):
        """They read the value shortlist and the cagey tier only, before and after the release: nothing to switch."""
        for name in ('staking.py', 'recommendation_history.py', 'performance_excel.py'):
            self.assertNotIn('master', (REPO / name).read_text(encoding='utf-8').lower(), name)

    def test_readme_describes_the_release(self):
        readme = (REPO / 'README.md').read_text(encoding='utf-8')
        self.assertIn('master_shortlist_old.csv', readme)
        self.assertIn('"live": "old"', readme)


class RawCheckTest(unittest.TestCase):
    """workflow_checks raw check: the live new master and the old shadow are both bound to the deterministic replay."""

    def test_matches_new_is_exact_on_a_saved_run(self):
        predictions, decisions, summary = snapshot_inputs()
        out, summary = refresh((predictions, decisions, summary))
        frame = pd.read_csv(out / ms.FILE)
        old = pd.read_csv(out / ms.OLD_FILE)
        expected, info = ms.new_live(decisions, ms._old_master(decisions, summary, predictions,
                                                               ms.configured_version())[0],
                                     summary['generated_at_utc'], predictions)
        self.assertGreater(len(old), 0)
        self.assertTrue(ms.matches_new(frame, expected))
        self.assertEqual(info, summary['master_shortlist'])
        tampered = frame.copy()
        tampered.loc[tampered.new_master_decision.eq('SHORTLISTED').idxmax(), 'offered_decimal_odds'] += 0.01
        self.assertFalse(ms.matches_new(tampered, expected))
        self.assertFalse(ms.matches_new(frame.iloc[::-1], expected))
        self.assertFalse(ms.matches_new(frame.drop(columns=['timing_check']), expected))

    def test_raw_check_replays_both_masters(self):
        from unittest.mock import patch
        from offline_test_case import OfflineQuotePolicyTestCase  # noqa: F401  (policy fixtures below)
        from test_master_shortlist import run as run_v28, PipelineTests
        from workflow_checks import raw_check
        case = PipelineTests('test_raw_check_binds_the_master_shortlist_to_the_replay')
        case.setUp()
        try:
            monitoring = []
            selected, decisions, summary = run_v28(*case.predictions.to_dict('records'), monitor=monitoring)
            with tempfile.TemporaryDirectory() as tmp:
                raw = Path(tmp) / 'raw'
                raw.mkdir()
                case.predictions.to_csv(raw / 'all_leagues_predictions.csv', index=False)
                selected.to_csv(raw / 'conservative_bet_shortlist.csv', index=False)
                v28.cagey_tier_list(decisions).to_csv(raw / v28.TIER_FILE, index=False)
                v28.record_monitoring(summary, monitoring, raw)
                with warnings.catch_warnings():
                    warnings.simplefilter('ignore')
                    ms.refresh(decisions, raw, summary, case.predictions)
                self.assertEqual(summary['master_shortlist']['version'], ms.VERSION_NEW_LIVE)
                self.assertIn(ms.OLD_SUMMARY_KEY, summary)
                path = raw / 'conservative_bet_summary.json'
                path.write_text(json.dumps(summary, default=str), encoding='utf-8')
                settings = {'cagey_correction_enabled': False, 'cagey_tier_enabled': False, 'model_version': None}

                def check():
                    with patch.object(v28, 'load_settings', return_value=settings):
                        raw_check(Path(tmp), raw_dir=raw)
                check()
                live, old = (raw / ms.FILE).read_bytes(), (raw / ms.OLD_FILE).read_bytes()
                frame = pd.read_csv(raw / ms.FILE)
                frame.assign(new_master_version='master-new-fill-rule-v4').to_csv(raw / ms.FILE, index=False)
                with self.assertRaisesRegex(Exception, 'Current master shortlist differs'):
                    check()
                (raw / ms.FILE).write_bytes(live)
                stored = path.read_bytes()
                bad = json.loads(stored)
                bad[ms.OLD_SUMMARY_KEY]['n_bets'] = bad[ms.OLD_SUMMARY_KEY]['n_bets'] + 1
                path.write_text(json.dumps(bad), encoding='utf-8')
                with self.assertRaisesRegex(Exception, r'old master shortlist \(shadow\) summary differs'):
                    check()
                path.write_bytes(stored)
                (raw / ms.OLD_FILE).unlink()
                with self.assertRaisesRegex(Exception, r'Missing current old master shortlist \(shadow\)'):
                    check()
                (raw / ms.OLD_FILE).write_bytes(old)
                (raw / ms.FILE).unlink()
                with self.assertRaisesRegex(Exception, 'Missing current master shortlist'):
                    check()
                (raw / ms.FILE).write_bytes(live)
                check()
        finally:
            case.tearDown()

    def _pipeline_run(self, tmp, patches):
        """The test_master_shortlist pipeline run written to tmp/raw under `patches`; returns (raw, check)."""
        from unittest.mock import patch
        from test_master_shortlist import run as run_v28, PipelineTests
        from workflow_checks import raw_check
        case = PipelineTests('test_raw_check_binds_the_master_shortlist_to_the_replay')
        case.setUp()
        self.addCleanup(case.tearDown)
        monitoring = []
        selected, decisions, summary = run_v28(*case.predictions.to_dict('records'), monitor=monitoring)
        raw = Path(tmp) / 'raw'
        raw.mkdir()
        case.predictions.to_csv(raw / 'all_leagues_predictions.csv', index=False)
        selected.to_csv(raw / 'conservative_bet_shortlist.csv', index=False)
        v28.cagey_tier_list(decisions).to_csv(raw / v28.TIER_FILE, index=False)
        v28.record_monitoring(summary, monitoring, raw)
        with contextlib.ExitStack() as stack, warnings.catch_warnings():
            warnings.simplefilter('ignore')
            for target, name in patches:
                stack.enter_context(patch.object(target, name, side_effect=RuntimeError('boom')))
            ms.refresh(decisions, raw, summary, case.predictions)
        (raw / 'conservative_bet_summary.json').write_text(json.dumps(summary, default=str), encoding='utf-8')
        settings = {'cagey_correction_enabled': False, 'cagey_tier_enabled': False, 'model_version': None}

        def check(*during):
            with patch.object(v28, 'load_settings', return_value=settings), contextlib.ExitStack() as stack:
                for target, name in during:
                    stack.enter_context(patch.object(target, name, side_effect=RuntimeError('boom')))
                raw_check(Path(tmp), raw_dir=raw)
        return raw, summary, check

    def test_raw_check_accepts_a_new_master_failure_only_when_it_replays(self):
        with tempfile.TemporaryDirectory() as tmp:
            raw, summary, check = self._pipeline_run(tmp, [(mr, 'reconcile')])
            self.assertEqual(summary[ms.RELEASE_STATUS_KEY]['status'], ms.NEW_MASTER_FAILED)
            check((mr, 'reconcile'))  # the failure replays: accepted, and the old master is checked as the live list
            with self.assertRaisesRegex(Exception, 'says the new master failed, but it replays without error'):
                check()
            (raw / ms.SUMMARY_FILE).write_text('{}', encoding='utf-8')
            with self.assertRaisesRegex(Exception, 'Unexpected release files'):
                check((mr, 'reconcile'))

    def test_raw_check_accepts_a_missing_baseline_only_when_it_replays(self):
        with tempfile.TemporaryDirectory() as tmp:
            raw, summary, check = self._pipeline_run(tmp, [(ms, '_old_master')])
            self.assertEqual(summary[ms.RELEASE_STATUS_KEY]['status'], ms.BASELINE_MISSING)
            check((ms, '_old_master'))
            with self.assertRaisesRegex(Exception, r'says the old master \(shadow\) failed, but it replays'):
                check()
            path = raw / 'conservative_bet_summary.json'
            info = json.loads(path.read_text(encoding='utf-8'))
            info.pop(ms.RELEASE_STATUS_KEY)
            path.write_text(json.dumps(info), encoding='utf-8')
            with self.assertRaisesRegex(Exception, r'Missing current old master shortlist \(shadow\) summary'):
                check((ms, '_old_master'))


if __name__ == '__main__':
    unittest.main()
