"""The strong-team master in shadow (master_strong.py, rule master-strong-team-v1): caps (6 per market group, 15
matches, one pick per match), the order (proven, league trust, research confirms, chance of profit), the not-proven
fill under the same caps, research roles that failed their pass rule staying labels, R3 on UCL/UEL only, thresholds
refused while unset, and the shadow never touching the live files."""
from __future__ import annotations

import copy
import json
import tempfile
import unittest
from pathlib import Path
from unittest import mock

import master_strong as ms
from master_switch import NewMasterLive, switched

RUN = {'E': .60, 'G': .50, 'R1': True, 'R2': True, 'R3': True, 'R4': True}


def config():
    cfg = ms.load_config()
    cfg = copy.deepcopy(cfg)
    cfg['checks']['strong_team']['E'] = RUN['E']
    roles = cfg['research_roles']
    roles['R1_research_strength'].update(G=RUN['G'], active=True)
    roles['R2_agreement_boost']['active'] = True
    roles['R4_fill_tie_breaker']['active'] = True
    return cfg


def evidence(team='H', wins=8, elo=.70, margin=1.0, side='home'):
    rows = [{'home': team, 'away': f'X{i}', 'home_goals': 2 if i < wins else 0, 'away_goals': 0 if i < wins else 1}
            for i in range(10)]
    return {'elo_home_expectancy': elo if side == 'home' else 1 - elo, 'history': {side: rows}, 'teams': {side: team},
            'h2h': [], 'research_margin': margin if side == 'home' else -margin}


def offer(match, market='Home win', no_loss=.80, profit=.80, odds=1.30, research=.80, gap=0., league='Premier League',
          trust='trusted', european=False, ev=None, **extra):
    row = {'_match': match, 'market': market, 'handicap_side': None, 'handicap_line': None, 'league': league,
           'home_team': 'H', 'away_team': 'A', 'kickoff_utc': f'2026-11-2{match[-1]}T15:00:00Z',
           'offered_decimal_odds': odds, 'ranking_no_loss_probability': no_loss,
           'ranking_profit_probability': profit, 'research_no_loss_probability': research, 'gap_points': gap,
           'research_profit_probability': extra.pop('research_profit', research), 'new_master_executable': True}
    row.update(extra)
    side = 'away' if market in ('Away win', 'Double Chance X2') or market.startswith('Asian Handicap Away') else 'home'
    return ms.annotate(row, ev or evidence(side=side), config=config(), trust=trust, european=european,
                       E=RUN['E'], G=RUN['G'])


class SettingsTest(unittest.TestCase):
    def test_unset_thresholds_are_refused(self):
        cfg = copy.deepcopy(ms.load_config())
        cfg['checks']['strong_team']['E'] = None
        with self.assertRaisesRegex(ValueError, 'thresholds not set'):
            ms.settings(cfg)
        self.assertEqual(ms.settings(config())['E'], .60)


class ChecksTest(unittest.TestCase):
    def test_proven_needs_every_check(self):
        self.assertTrue(ms.proven(offer('m1'), RUN))
        self.assertIn('safe', ms.failed_checks(offer('m1', no_loss=.70), RUN)[0])
        weak = offer('m1', ev=evidence(elo=.55))
        self.assertIn('strong team', ms.failed_checks(weak, RUN)[0])
        record = offer('m1', ev=evidence(wins=6))
        self.assertIn('record', ms.failed_checks(record, RUN)[0])
        research = offer('m1', ev=evidence(margin=.2))  # -0.5 line: 0.2 - 0.5 < 0.5
        self.assertIn('research strength', ms.failed_checks(research, RUN)[0])
        self.assertEqual(ms.failed_checks(research, {**RUN, 'R1': False}), [])

    def test_away_side_and_handicap_line(self):
        row = offer('m1', market='Asian Handicap Away +0.50', ev=evidence(side='away', wins=8))
        self.assertEqual((row['strong_backed_side'], row['strong_line'], row['strong_market_group']),
                         ('away', .5, 'asian_handicap'))
        self.assertAlmostEqual(row['strong_elo_expectancy'], .70)
        self.assertAlmostEqual(row['strong_research_margin'], 1.5)
        self.assertEqual(row['strong_bet_kind'], 'no loss')

    def test_r3_only_on_european_offers(self):
        """Rules before master-strong-team-v3; since v3 the research gate covers every offer
        (test_live_list_changes.ResearchGateTest)."""
        import copy as _copy
        old = _copy.deepcopy(config())
        old.pop('research_gate')
        domestic = ms.annotate({**offer('m1', research=.60)}, evidence(), config=old, trust='trusted', european=False,
                               E=RUN['E'], G=RUN['G'])
        self.assertIsNone(domestic['strong_r3_check'])
        self.assertTrue(ms.proven(domestic, RUN))
        self.assertIs(offer('m1', research=.60)['strong_r3_check'], False)  # v3: every offer
        european = offer('m2', research=.60, european=True, trust='unvalidated')
        self.assertFalse(european['strong_r3_check'])
        self.assertFalse(ms.proven(european, RUN))
        self.assertTrue(ms.proven(european, {**RUN, 'R3': False}))


class SelectTest(unittest.TestCase):
    def test_caps_one_per_match_and_target(self):
        rows = [offer(f'm{i:02d}', market='Home win', profit=.9 - i / 100) for i in range(10)]
        rows += [offer(f'n{i:02d}', market='Asian Handicap Home -0.50', profit=.8 - i / 100) for i in range(12)]
        rows += [offer('m00', market='Asian Handicap Home -0.50', profit=.5)]
        ms.select(rows, config(), RUN)
        picks = [r for r in rows if r['strong_decision'] == 'SHORTLISTED']
        self.assertEqual(len(picks), 12)  # 6 match result + 6 Asian handicap; double chance has no offers
        groups = [r['strong_market_group'] for r in picks]
        self.assertEqual(groups.count('match_result'), 6)
        self.assertEqual(groups.count('asian_handicap'), 6)
        self.assertEqual(len({r['_match'] for r in picks}), len(picks))
        full = [r for r in rows if r['strong_reason'].startswith('market group full')]
        self.assertTrue(full)

    def test_total_never_above_fifteen(self):
        rows = [offer(f'a{i:02d}', market=m, profit=.9 - i / 100)
                for i, m in enumerate(['Home win', 'Double Chance 1X', 'Asian Handicap Home -0.50'] * 7)]
        ms.select(rows, config(), RUN)
        picks = [r for r in rows if r['strong_decision'] == 'SHORTLISTED']
        self.assertEqual(len(picks), 15)
        self.assertEqual(sorted(r['strong_rank'] for r in picks), list(range(1, 16)))

    def test_order_proven_then_trust_then_confirms_then_profit(self):
        """Rules before master-strong-team-v4; since v4 proven picks go by Elo, record share, then chance of profit
        (test_live_list_changes.ProvenOrderTest)."""
        before_v4 = copy.deepcopy(config())
        before_v4.pop('proven_order')
        rows = [offer('m1', profit=.95, trust='not trusted'), offer('m2', profit=.80),
                offer('m3', profit=.90, research=.70), offer('m4', profit=.99, no_loss=.70)]
        ms.select(rows, before_v4, RUN)
        order = sorted((r for r in rows if r['strong_rank']), key=lambda r: r['strong_rank'])
        self.assertEqual([r['_match'] for r in order], ['m2', 'm3', 'm1', 'm4'])
        self.assertEqual([r['strong_tier'] for r in order], ['proven'] * 3 + ['not proven: fill'])
        # R2 failed its pass rule: confirmation is a label only and the order is by chance of profit
        rows = [offer('m2', profit=.80), offer('m3', profit=.90, research=.70)]
        ms.select(rows, before_v4, {**RUN, 'R2': False})
        self.assertEqual(min(rows, key=lambda r: r['strong_rank'])['_match'], 'm3')
        self.assertIn('research confirms (label only)', rows[0]['strong_labels'])

    def test_fill_is_labelled_and_capped(self):
        rows = [offer(f'm{i}', market='Home win', no_loss=.6, profit=.6 - i / 100) for i in range(9)]
        ms.select(rows, config(), RUN)
        picks = [r for r in rows if r['strong_decision'] == 'SHORTLISTED']
        self.assertEqual(len(picks), 6)
        self.assertTrue(all(r['strong_tier'] == 'not proven: fill' for r in picks))
        self.assertTrue(all('not proven' in r['strong_labels'] for r in picks))

    def test_r4_breaks_near_ties_by_research_only_when_active(self):
        rows = [offer('m1', no_loss=.6, profit=.611, research_profit=.50),
                offer('m2', no_loss=.6, profit=.605, research_profit=.70)]
        ms.select(rows, config(), RUN)
        self.assertEqual(min(rows, key=lambda r: r['strong_rank'])['_match'], 'm2')
        rows = [offer('m1', no_loss=.6, profit=.611, research_profit=.50),
                offer('m2', no_loss=.6, profit=.605, research_profit=.70)]
        ms.select(rows, config(), {**RUN, 'R4': False})
        self.assertEqual(min(rows, key=lambda r: r['strong_rank'])['_match'], 'm1')

    def test_not_executable_never_picked(self):
        rows = [offer('m1', new_master_executable=False, new_master_reason='timing: stale')]
        ms.select(rows, config(), RUN)
        self.assertEqual((rows[0]['strong_decision'], rows[0]['strong_reason']), ('NOT_EXECUTABLE', 'timing: stale'))


class ShadowTest(unittest.TestCase):
    def test_shadow_failure_leaves_live_files(self):
        import master_shortlist
        with tempfile.TemporaryDirectory() as tmp:
            live = Path(tmp) / master_shortlist.FILE
            live.write_text('live\n', encoding='utf-8')
            with mock.patch.object(ms, 'reconcile', side_effect=RuntimeError('boom')):
                master_shortlist.strong_shadow(object(), tmp, {}, None, None)
            self.assertEqual(live.read_text(encoding='utf-8'), 'live\n')
            self.assertFalse((Path(tmp) / ms.load_config()['file']).exists())


class EmptyRunTest(unittest.TestCase):
    def test_no_nomination_writes_an_empty_list_and_summary(self):
        import pandas as pd
        cfg = config()
        with mock.patch.object(ms, 'load_config', return_value=cfg):
            frame = ms.reconcile(pd.DataFrame([{'decision': 'REJECTED', 'cagey_tier_decision': 'REJECTED'}]))
            self.assertEqual(list(frame.columns), ms.columns())
            self.assertEqual(len(frame), 0)
            out = ms.summary(frame, cfg)
        self.assertEqual((out['ranked_fixtures'], out['shortfall']), (0, 15))


class RefreshIntegrationTest(NewMasterLive, unittest.TestCase):
    def test_refresh_writes_the_strong_list_without_touching_the_live_master(self):
        import pandas as pd
        import master_shortlist
        from test_master_reconciliation import production_run
        predictions, decisions, summary = production_run()
        with tempfile.TemporaryDirectory() as on, tempfile.TemporaryDirectory() as off:
            master_shortlist.refresh(decisions, on, dict(summary), predictions)
            with mock.patch.object(master_shortlist, 'strong_shadow', lambda *a, **k: None):
                master_shortlist.refresh(decisions, off, dict(summary), predictions)
            self.assertEqual((Path(on) / master_shortlist.FILE).read_bytes(),
                             (Path(off) / master_shortlist.FILE).read_bytes())
            frame = pd.read_csv(Path(on) / ms.load_config()['file'])
            info = json.loads((Path(on) / ms.load_config()['summary_file']).read_text(encoding='utf-8'))
        picks = frame.loc[frame.strong_decision.eq('SHORTLISTED')]
        self.assertEqual(info['ranked_fixtures'], len(picks))
        self.assertTrue(picks.groupby('strong_market_group').size().le(6).all())
        self.assertTrue(frame.strong_master_version.eq(ms.VERSION).all())
        self.assertGreater(len(frame), 0)


class StrongLiveTest(unittest.TestCase):
    """The strong release (Paul, 23 Nov 2026): live "strong" writes the strong master as master_shortlist.csv and
    today's master (master-new-fill-rule-v4) in shadow as master_shortlist_new.csv; "new" rolls back."""

    def run_refresh(self, out, *failing):
        import contextlib
        import warnings
        import master_shortlist
        from test_master_reconciliation import production_run
        predictions, decisions, summary = production_run()
        run = dict(summary)
        with contextlib.ExitStack() as stack, warnings.catch_warnings():
            warnings.simplefilter('ignore')
            for target, name in failing:
                stack.enter_context(mock.patch.object(target, name, side_effect=RuntimeError('boom')))
            master_shortlist.refresh(decisions, out, run, predictions)
        return run, predictions, decisions

    def test_the_committed_switch_is_strong(self):
        import master_shortlist
        self.assertEqual(master_shortlist.configured_live(), master_shortlist.LIVE_STRONG)

    def test_strong_is_the_live_file_and_todays_master_its_baseline(self):
        import pandas as pd
        import master_reconciliation as mr
        import master_shortlist
        with tempfile.TemporaryDirectory() as out:
            run, predictions, decisions = self.run_refresh(out)
            files = sorted(p.name for p in Path(out).iterdir())
            self.assertEqual(files, sorted([master_shortlist.FILE, master_shortlist.SUMMARY_FILE,
                                            mr.load_config()['file'], mr.load_config()['summary_file']]))
            live = pd.read_csv(Path(out) / master_shortlist.FILE)
            baseline = pd.read_csv(Path(out) / mr.load_config()['file'])
        self.assertEqual(list(live.columns), master_shortlist.strong_live_columns())
        self.assertTrue(live.new_master_version.eq(master_shortlist.VERSION_STRONG_LIVE).all())
        self.assertTrue(live.strong_master_version.eq(ms.VERSION).all())
        self.assertTrue((live.new_master_decision == live.strong_decision).all())
        self.assertTrue(baseline.new_master_version.eq(mr.VERSION).all())
        expected = mr.reconcile(decisions, None, mr.load_config(), predictions, run['generated_at_utc'])
        self.assertEqual(list(baseline.new_master_rank.fillna(0)), list(expected.new_master_rank.fillna(0)))
        info = run['master_shortlist']
        self.assertEqual((info['version'], info['rule']), (master_shortlist.VERSION_STRONG_LIVE, ms.VERSION))
        self.assertIn('strong', info)
        self.assertNotIn(master_shortlist.OLD_SUMMARY_KEY, run)
        self.assertNotIn(master_shortlist.RELEASE_STATUS_KEY, run)
        picks = live.loc[live.new_master_decision.eq('SHORTLISTED')]
        self.assertTrue(picks.groupby('strong_market_group').size().le(6).all())
        base_picks = baseline.loc[baseline.new_master_decision.eq('SHORTLISTED')]
        self.assertEqual(int(picks.in_old_master.sum()),
                         len(set(picks.home_team + picks.kickoff_utc) & set(base_picks.home_team + base_picks.kickoff_utc)))

    def test_new_rolls_back_to_the_files_before_the_release(self):
        import master_shortlist
        with tempfile.TemporaryDirectory() as out, switched('new'):
            run, _, _ = self.run_refresh(out)
            files = sorted(p.name for p in Path(out).iterdir())
        self.assertEqual(run['master_shortlist']['version'], master_shortlist.VERSION_NEW_LIVE)
        self.assertIn(master_shortlist.OLD_FILE, files)
        self.assertIn(ms.load_config()['file'], files)  # the strong master back in shadow

    def test_a_strong_failure_publishes_todays_master(self):
        import pandas as pd
        import master_shortlist
        import master_reconciliation as mr
        with tempfile.TemporaryDirectory() as out:
            run, _, _ = self.run_refresh(out, (ms, 'live_frame'))
            live = pd.read_csv(Path(out) / master_shortlist.FILE)
            files = sorted(p.name for p in Path(out).iterdir())
        self.assertEqual(run[master_shortlist.RELEASE_STATUS_KEY]['status'], master_shortlist.STRONG_FAILED)
        self.assertEqual(run['master_shortlist']['version'], master_shortlist.VERSION_NEW_LIVE)
        self.assertTrue(live.new_master_version.eq(master_shortlist.VERSION_NEW_LIVE).all())
        self.assertNotIn(mr.load_config()['file'], files)

    def test_a_baseline_failure_keeps_the_strong_master_live(self):
        import master_shortlist
        import master_reconciliation as mr
        with tempfile.TemporaryDirectory() as out:
            run, _, _ = self.run_refresh(out, (mr, 'write_shadow'))
            files = sorted(p.name for p in Path(out).iterdir())
        self.assertEqual(run[master_shortlist.RELEASE_STATUS_KEY]['status'], master_shortlist.BASELINE_MISSING)
        self.assertEqual(run['master_shortlist']['version'], master_shortlist.VERSION_STRONG_LIVE)
        self.assertEqual(files, sorted([master_shortlist.FILE, master_shortlist.SUMMARY_FILE]))

    def test_both_failing_fails_the_run(self):
        import master_reconciliation as mr
        with tempfile.TemporaryDirectory() as out:
            with self.assertRaises(RuntimeError):
                self.run_refresh(out, (mr, 'write_shadow'), (ms, 'live_frame'))

    def test_the_readable_report_shows_the_strong_section(self):
        import format_football_output as fo
        with tempfile.TemporaryDirectory() as out:
            run, _, _ = self.run_refresh(out)
            lines = fo.master_section(run, Path(out), Path(out))
            self.assertTrue((Path(out) / fo.MASTER_READABLE).exists())
        self.assertTrue(any('strong-team master, live since 23 Nov 2026' in line for line in lines))


class StrongRawCheckTest(unittest.TestCase):
    """workflow_checks raw check under live "strong": the live strong master and today's master (shadow) are bound
    to the deterministic replay; a strong failure is accepted only when it replays."""

    def pipeline_run(self, tmp, failing=()):
        import contextlib
        import warnings
        import master_shortlist
        import price_edge_cagey_shortlist as v28
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
            for target, name in failing:
                stack.enter_context(mock.patch.object(target, name, side_effect=RuntimeError('boom')))
            master_shortlist.refresh(decisions, raw, summary, case.predictions)
        (raw / 'conservative_bet_summary.json').write_text(json.dumps(summary, default=str), encoding='utf-8')
        settings = {'cagey_correction_enabled': False, 'cagey_tier_enabled': False, 'model_version': None}

        def check(*during):
            with mock.patch.object(v28, 'load_settings', return_value=settings), contextlib.ExitStack() as stack:
                for target, name in during:
                    stack.enter_context(mock.patch.object(target, name, side_effect=RuntimeError('boom')))
                raw_check(Path(tmp), raw_dir=raw)
        return raw, summary, check

    def test_raw_check_replays_the_strong_master_and_its_baseline(self):
        import pandas as pd
        import master_shortlist
        import master_reconciliation as mr
        with tempfile.TemporaryDirectory() as tmp:
            raw, summary, check = self.pipeline_run(tmp)
            self.assertEqual(summary['master_shortlist']['version'], master_shortlist.VERSION_STRONG_LIVE)
            check()
            live = (raw / master_shortlist.FILE).read_bytes()
            frame = pd.read_csv(raw / master_shortlist.FILE)
            frame.assign(new_master_tier='tampered').to_csv(raw / master_shortlist.FILE, index=False)
            with self.assertRaisesRegex(Exception, r'Current master shortlist \(strong\) differs'):
                check()
            (raw / master_shortlist.FILE).write_bytes(live)
            baseline = raw / mr.load_config()['file']
            stored = baseline.read_bytes()
            baseline.unlink()
            with self.assertRaisesRegex(Exception, "Missing today's master"):
                check()
            baseline.write_bytes(stored)
            check()

    def test_raw_check_accepts_a_strong_failure_only_when_it_replays(self):
        import master_shortlist
        with tempfile.TemporaryDirectory() as tmp:
            raw, summary, check = self.pipeline_run(tmp, [(ms, 'live_frame')])
            self.assertEqual(summary[master_shortlist.RELEASE_STATUS_KEY]['status'], master_shortlist.STRONG_FAILED)
            check((ms, 'live_frame'))
            with self.assertRaisesRegex(Exception, 'says the strong master failed, but it replays without error'):
                check()


class StrongRollbackTest(unittest.TestCase):
    def test_rollback_triggers_only_when_live_and_entirely_below_zero(self):
        import price_edge_tracking as tracking
        compared = {'status': 'COMPARED', 'difference': -.05, 'interval_95': [-.09, -.01]}
        out = tracking.strong_rollback(compared)
        self.assertTrue(out['triggered'])
        self.assertEqual(out['status'], tracking.ROLLBACK_TRIGGERED)
        self.assertFalse(tracking.strong_rollback({**compared, 'interval_95': [-.09, .01]})['triggered'])
        with switched('new'):
            self.assertFalse(tracking.strong_rollback(compared)['triggered'])
        self.assertEqual(tracking.strong_rollback({'status': 'WAITING'})['status'], 'WAITING')

    def test_workbook_names_the_strong_master_live(self):
        import performance_report_layout as layout
        with tempfile.TemporaryDirectory() as tmp:
            self.assertEqual(layout.list_names(Path(tmp))['strong'], 'Strong master (live)')
            self.assertIn('strong-team master', layout.release_status(Path(tmp), 'master'))


class GradingTest(unittest.TestCase):
    def test_capture_only_this_generation_and_rule(self):
        import pandas as pd
        import price_edge_tracking as tracking
        generated = '2026-11-23T10:00:00+00:00'
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / ms.load_config()['file']
            row = {'selection_policy_version': tracking.CAGEY_POLICY, 'evaluated_at_utc': generated,
                   'strong_master_version': ms.VERSION, 'strong_decision': 'SHORTLISTED'}
            pd.DataFrame([row]).to_csv(path, index=False)
            self.assertEqual(tracking.capture_strong_master_file(Path(tmp), generated), path)
            self.assertIsNone(tracking.capture_strong_master_file(Path(tmp), '2026-11-23T11:00:00+00:00'))
            pd.DataFrame([{**row, 'strong_master_version': 'other'}]).to_csv(path, index=False)
            self.assertIsNone(tracking.capture_strong_master_file(Path(tmp), generated))

    def test_comparison_waits_for_enough_graded_matches(self):
        import pandas as pd
        import price_edge_tracking as tracking
        empty = pd.DataFrame(columns=['kickoff_utc', 'unit_profit', 'offered_decimal_odds', 'clv'])
        out = tracking.strong_master_summary(empty, empty)
        self.assertEqual(out['comparison']['status'], 'WAITING')
        self.assertIn('strong_master', out['comparison'])
        text = '\n'.join(tracking.strong_master_report({'strong_master': out}))
        self.assertIn('Strong-team master', text)


if __name__ == '__main__':
    unittest.main()
