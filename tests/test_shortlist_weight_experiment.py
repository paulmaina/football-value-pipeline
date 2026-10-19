"""Frozen weighting trials use real production eligibility and verified forward results."""
from offline_test_case import OfflineQuotePolicyTestCase
import copy
from datetime import timedelta
import hashlib
import json
from pathlib import Path
import tempfile
from unittest.mock import patch
import pandas as pd

import shortlist_weight_experiment as trial
from conservative_bet_filter import build_conservative_shortlist, BALANCED_SELECTION_POLICY_VERSION
from performance_tracking import capture, snapshots, write_json
from test_conservative_bet_filter import fixture, NOW
from test_filter_sensitivity_experiment import record
from test_graded_candidates import only_over_goal, sample_report


def setup(root, rows=None):
    raw = root/'raw'; raw.mkdir(parents=True, exist_ok=True)
    if rows is None:
        row = fixture(); row.update(home_team='Manchester City FC', away_team='Everton FC',
            model_home_team='Manchester City FC', model_away_team='Everton FC')
        rows = [row]
    frame = pd.DataFrame(rows)
    reports = {'Premier League':dict(sample_report(), league='Premier League')}
    picks, decisions, summary = build_conservative_shortlist(frame, as_of=NOW,
        market_reliability=reports, selection_policy_version=BALANCED_SELECTION_POLICY_VERSION)
    frame.to_csv(raw/'all_leagues_predictions.csv', index=False)
    picks.to_csv(raw/'conservative_bet_shortlist.csv', index=False)
    write_json(raw/'conservative_bet_summary.json', summary)
    write_json(raw/'EPL_goal_market_validation.json', reports['Premier League'])
    before = {p.name:p.read_bytes() for p in raw.iterdir()}
    data = trial.write_experiment(frame, raw, summary, decisions, reports)
    assert before == {p.name:p.read_bytes() for p in raw.iterdir() if p.name in before}
    return raw, data, frame, picks, decisions, summary


class WeightTrialTests(OfflineQuotePolicyTestCase):
    def test_fixed_weights_change_selection_on_identical_pool_without_changing_production(self):
        rows = [dict(only_over_goal(i), kickoff_utc=(NOW+timedelta(hours=24)).isoformat()) for i in range(14)]
        for i, row in enumerate(rows):
            p = .95-.02*i; ev = -.03+.03*i
            row.update(p_over_1_5=p, raw_p_over_1_5=p-.02, market_over_1_5_odds=(1+ev)/p)
        with tempfile.TemporaryDirectory() as tmp:
            raw, data, frame, picks, decisions, summary = setup(Path(tmp), rows)
            self.assertEqual(len(data['rows']), 14*7*4)
            self.assertNotIn('Under 3.5', {r['market'] for r in data['rows']})
            by_variant = {v:[r for r in data['rows'] if r['variant_id']==v] for v in trial.VARIANTS}
            for v, policy in trial.VARIANTS.items():
                w = policy.get('probability_weight', .5)
                chosen = [r for r in by_variant[v] if r['decision'] in trial.SELECTED]
                self.assertEqual(len(chosen), 12)
                self.assertEqual(len({r['fixture_id'] for r in chosen}), 12)
                for r in by_variant[v]:
                    if r['selection_score'] is not None:
                        self.assertAlmostEqual(r['selection_score'], w*r['probability_percentile']+(1-w)*r['ev_percentile'])
            hi = {r['fixture_id'] for r in by_variant['probability_100_ev_0'] if r['decision'] in trial.SELECTED}
            ev = {r['fixture_id'] for r in by_variant['probability_25_ev_75'] if r['decision'] in trial.SELECTED}
            self.assertIn('fixture-0', hi); self.assertNotIn('fixture-0', ev)
            self.assertIn('fixture-13', ev); self.assertNotIn('fixture-13', hi)
            replay = build_conservative_shortlist(frame, as_of=NOW, market_reliability=data['validation_evidence'], selection_policy_version=BALANCED_SELECTION_POLICY_VERSION)
            pd.testing.assert_frame_equal(picks, replay[0]); pd.testing.assert_frame_equal(decisions, replay[1])
            self.assertEqual(summary, replay[2])
            self.assertIsNotNone(trial.capture_file(raw, summary['generated_at_utc']))

    def test_weight_settings_reject_invalid_values_and_legacy_policy(self):
        for value in (True, float('nan'), float('inf'), 0, 1.01, '0.75'):
            with self.assertRaises(ValueError):
                build_conservative_shortlist(pd.DataFrame([fixture()]), as_of=NOW,
                    research_policy={'probability_weight': value}, selection_policy_version=BALANCED_SELECTION_POLICY_VERSION)
        with self.assertRaises(ValueError):
            build_conservative_shortlist(pd.DataFrame([fixture()]), as_of=NOW, research_policy={'probability_weight':.75})

    def test_capture_deduplication_grading_reports_and_pending_results(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); raw, data, frame, *rest = setup(root)
            self.assertTrue(capture('a'*40, root=root, captured_at=NOW))
            self.assertTrue(capture('b'*40, root=root, captured_at=NOW+timedelta(minutes=1)))
            frozen, rejected = trial.frozen(root, snapshots(root))
            self.assertEqual(len(frozen), 28); self.assertEqual(rejected, [])
            rec = record(frame.iloc[0].to_dict())
            write_json(root/'performance/verified_results.json', {'PL:90002':rec})
            summary = trial.review_experiment(root, snapshots(root), [rec], NOW+timedelta(days=3))
            self.assertEqual(summary['verified_fixtures'], 1)
            self.assertEqual(len(summary['comparisons']), 12)
            all_rows = [r for r in summary['comparisons'] if r['tier']=='ALL']
            self.assertTrue(all(r['graded']==1 for r in all_rows))
            self.assertTrue(all(r['win_rate_wilson95'] is not None for r in all_rows))
            self.assertEqual(summary['primary_tier'], 'ALL')
            self.assertFalse(summary['automatic_production_change'])
            self.assertTrue(trial.validate_report(root))
            pending = trial.review_experiment(root, snapshots(root), [rec], NOW)
            self.assertEqual(pending['verified_fixtures'], 0)
            self.assertTrue(all(r['flat_stake_roi'] is None for r in pending['comparisons']))
            self.assertTrue(trial.validate_report(root))
            path = root/'performance'/trial.NAME/'selections.csv'
            path.write_text(path.read_text().replace('PROVISIONAL','ALTERED'))
            with self.assertRaises(ValueError): trial.validate_report(root)
            trial.review_experiment(root, snapshots(root), [rec], NOW)
            path.write_text('fixture_key\n')
            with self.assertRaises(ValueError): trial.validate_report(root)
            trial.review_experiment(root, snapshots(root), [rec], NOW)
            report = root/'performance'/trial.NAME/'summary.json'
            changed = json.loads(report.read_text()); changed['verified_fixtures']=99; write_json(report, changed)
            with self.assertRaises(ValueError): trial.validate_report(root)

    def test_tampering_fails_closed_but_baseline_archives_survive(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); raw, data, frame, picks, decisions, summary = setup(root)
            mutations = [lambda d:d.update(version='bad'), lambda d:d.update(variants={}),
                lambda d:d.update(selection_policy_version='old'), lambda d:d['rows'].pop(),
                lambda d:d['rows'][0].update(selection_score=.001), lambda d:d['rows'][0].update(bookmaker='fake'),
                lambda d:d.update(validation_evidence=[]), lambda d:d.update(execution_policy={})]
            for mutate in mutations:
                bad = copy.deepcopy(data); mutate(bad)
                with self.assertRaises(ValueError): trial.validate(bad, summary['generated_at_utc'], frame.to_dict('records'))
            with self.assertRaises(ValueError): trial.validate(data, summary['generated_at_utc'], frame.to_dict('records')*2)
            with self.assertRaises(ValueError): trial.validate(data, (NOW+timedelta(seconds=1)).isoformat(), frame.to_dict('records'))
            with self.assertRaises(ValueError): trial.validate_control(data, [])
            for field, value in [('bookmaker','fake'), ('offered_decimal_odds',9), ('rank_probability',.01),
                                 ('selection_score',None), ('per_stake_cost','invalid')]:
                changed = picks.to_dict('records'); changed[0][field]=value
                with self.assertRaises(ValueError): trial.validate_control(data,changed)
            wrong = decisions.copy(); wrong.loc[0,'decision']='ALTERED'
            with self.assertRaises(ValueError): trial.write_experiment(frame,raw,summary,wrong,data['validation_evidence'])
            with self.assertRaises(ValueError): trial.write_experiment(frame,raw,dict(summary,selection_policy_version='old'),decisions,None)
            capture('a'*40, root=root, captured_at=NOW)
            archive = root/'performance/snapshots'/('a'*16)/(trial.NAME+'.json')
            archive.write_text('{}')
            self.assertEqual(len(snapshots(root)), 1)
            self.assertEqual(trial.frozen(root,snapshots(root))[1], ['a'*40])
            self.assertEqual(trial.review_experiment(root,snapshots(root),[],NOW)['status'],'DATA_QUALITY_BLOCKED')
            (raw/(trial.NAME+'.json')).write_text('{}')
            with self.assertWarnsRegex(UserWarning,'Shortlist weight capture skipped'):
                self.assertTrue(capture('b'*40,root=root,captured_at=NOW))
            health = json.loads((root/'performance/snapshots'/('b'*16)/'pipeline_health.json').read_text())
            self.assertEqual(health['experiments'][trial.NAME], 'PRESENT_BUT_REJECTED')
            (raw/(trial.NAME+'.json')).unlink(); self.assertIsNone(trial.capture_file(raw,summary['generated_at_utc']))

    def test_late_outside_window_invalid_only_and_absent_sidecars_supply_no_evidence(self):
        for rows in ([fixture(kickoff=NOW+timedelta(hours=49))], [dict(fixture(), home_name_match_score=0)]):
            with tempfile.TemporaryDirectory() as tmp:
                root=Path(tmp); setup(root,rows)
                capture('a'*40,root=root,captured_at=NOW)
                self.assertEqual(trial.frozen(root,snapshots(root))[0],[])
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp); raw, data, *_=setup(root)
            self.assertFalse(capture('a'*40,root=root,captured_at=NOW+timedelta(days=1,minutes=-19)))
            (raw/(trial.NAME+'.json')).unlink(); capture('b'*40,root=root,captured_at=NOW)
            self.assertEqual(trial.frozen(root,snapshots(root))[0],[])

    def test_readiness_counts_unique_usable_fixtures_and_provisional_returns(self):
        rows=[]
        for i in range(300):
            for variant in trial.VARIANTS:
                rows.append({'fixture_key':str(i), 'kickoff_utc':(NOW+timedelta(days=i//5)).isoformat(),
                    'variant_id':variant,'decision':'SHORTLISTED_PROVISIONAL','selection_tier':'PROVISIONAL',
                    'market':'Home win','league':'Premier League','rank_probability':.8,
                    'offered_decimal_odds':1.5,'per_stake_cost':.02})
        match={'home_goals':2,'away_goals':0,'match_id':90002}
        with patch.object(trial,'frozen',return_value=(rows,[])),patch('performance_tracking.fixture_match',return_value=(match,'VERIFIED')):
            summary, selections, coverage=trial.evaluate(Path('.'),[],[],NOW+timedelta(days=90))
        self.assertEqual(summary['status'],'READY_FOR_REVIEW')
        self.assertEqual(summary['verified_fixtures'],300)
        self.assertEqual(summary['minimum_settled_per_weighting'],300)
        self.assertEqual(summary['paired_all_returns'][0]['weekly_block_bootstrap95'],[0,0])
        self.assertAlmostEqual(next(r for r in summary['comparisons'] if r['tier']=='ALL')['flat_stake_roi'],.48)
        coverage[1]['decision']='NOT_SELECTED'
        self.assertLess(trial.paired_returns(coverage,'probability_100_ev_0')['mean_profit_delta_per_fixture'],0)
        self.assertIsNone(trial.paired_returns([],'probability_100_ev_0')['weekly_block_bootstrap95'])
        for row in rows:
            if row['variant_id']=='probability_100_ev_0':row['decision']='NOT_SELECTED'
        with patch.object(trial,'frozen',return_value=(rows,[])),patch('performance_tracking.fixture_match',return_value=(match,'VERIFIED')):
            self.assertEqual(trial.evaluate(Path('.'),[],[],NOW+timedelta(days=90))[0]['status'],'COLLECT_MORE_DATA')

    def test_review_queue_excel_and_frozen_input_binding(self):
        from experiment_review_queue import write_queue
        from performance_report_layout import experiment_rows, get_sheet, text, q
        from performance_excel import write_workbook
        from zipfile import ZipFile
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp); raw, data, frame, picks, decisions, summary=setup(root)
            self.assertIsNotNone(trial.capture_file(raw,summary['generated_at_utc']))
            (raw/'EPL_goal_market_validation.json').write_text('{}')
            with self.assertRaises(ValueError): trial.capture_file(raw,summary['generated_at_utc'])
            write_json(raw/'EPL_goal_market_validation.json',data['validation_evidence']['Premier League'])
            (raw/'all_leagues_predictions.csv').write_text('changed')
            with self.assertRaises(ValueError): trial.capture_file(raw,summary['generated_at_utc'])
            trial.review_experiment(root,[],[],NOW)
            queue=write_queue(root,NOW)
            item=next(r for r in queue['experiments'] if r['name']==trial.NAME)
            self.assertEqual(item['status'],'COLLECT_MORE_DATA')
            self.assertFalse(item['automatic_production_change'])
            ready=next(r for r in experiment_rows(root,{'review_queue':queue}) if r[0]=='Shortlist probability / EV weights')
            self.assertEqual(ready[4],'300 paired fixtures')
            self.assertIn('100 more settled picks',ready[8])
            workbook=write_workbook(root,[],[],{})
            with ZipFile(workbook) as z: parts={n:z.read(n) for n in z.namelist()}
            sheet=get_sheet(parts,'Experiments')
            displayed=' '.join(text(c) or '' for c in sheet.root.iter(q('c')))
            self.assertIn('ALL selections primary',displayed)
            self.assertIn('75% / 25%',displayed)
            self.assertIn('Win rate 95% interval',displayed)
            report=root/'performance'/trial.NAME/'report.md'
            self.assertIn('No automatic production change',report.read_text())
