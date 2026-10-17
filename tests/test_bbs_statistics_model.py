"""Point-in-time form, gated learning, probability integration and rollback."""
import copy
from datetime import timedelta
from pathlib import Path
import tempfile
from types import SimpleNamespace
from unittest.mock import patch

import numpy as np
import pandas as pd

from offline_test_case import OfflineQuotePolicyTestCase
from bbs_data import STAT_FIELDS, Store
from bbs_statistics_model import FormIndex, PoissonForm, StatisticsModel, fit_statistics, mix_rates
from bbs_integration import feature_observations
from football_value_pipeline_v2_standalone import DixonColesModel, FootballValuePipelineV2, build_parser
from tests.test_model_correctness import history as plain_history


def values(strong):
    result = {k: (12 if strong else 3) for k in STAT_FIELDS}
    result.update(total_shots=20 if strong else 5, shots_on_target=10 if strong else 1,
        total_passes=400 if strong else 200, accurate_passes=320 if strong else 100,
        ball_possession=70 if strong else 30, pass_percentage=80 if strong else 50)
    return result


def sample(n=190):
    rows, observations = [], []
    for i, day in enumerate(pd.date_range('2025-01-01', periods=n, tz='UTC')):
        home, away = ('A', 'B') if i % 2 == 0 else ('B', 'A')
        rows.append({'Date': day.tz_localize(None), 'HomeTeam': home, 'AwayTeam': away,
                     'FTHG': 4 if home == 'A' else 0, 'FTAG': 4 if away == 'A' else 0})
        observations.append({'match_id': str(i), 'kickoff_utc': (day+pd.Timedelta(hours=12)).isoformat(),
            'observed_at_utc': (day+pd.Timedelta(hours=15)).isoformat(),
            'home_team': home, 'away_team': away, 'home': values(home == 'A'), 'away': values(away == 'A')})
    frame = pd.DataFrame(rows)
    frame.attrs['bbs_statistics_observations'] = observations
    return frame, observations, day+pd.Timedelta(days=1)


def constant_baseline(past, origin):
    assert pd.to_datetime(past.Date, utc=True).max() < origin
    return SimpleNamespace(rho=0., max_goals=10,
        expected_goals=lambda h, a: {'lambda_home': 1., 'lambda_away': 1.})


class FormTests(OfflineQuotePolicyTestCase):
    def test_future_own_match_and_cutoff_equal_statistics_cannot_enter_form(self):
        _, observations, cutoff = sample(8)
        index = FormIndex(observations, cutoff)
        origin = pd.Timestamp('2025-01-05T00:00:00Z')
        before, info = index.pair('A', 'B', origin)
        self.assertEqual(info['home_matches'], 4)
        future = copy.deepcopy(observations[-1]); future['home']['total_shots'] = 999
        future['observed_at_utc'] = cutoff.isoformat()
        other = FormIndex(observations+[future], cutoff)
        after, _ = other.pair('A', 'B', origin)
        np.testing.assert_array_equal(before, after)
        own, _ = index.pair('A', 'B', pd.Timestamp('2025-01-04T13:00:00Z'))
        self.assertAlmostEqual(own[0, STAT_FIELDS.index('total_shots')], 20.)
        self.assertEqual(index.form('A', '2025-01-04T13:00:00Z')[1], 3)

    def test_revisions_are_asof_and_unavailable_tombstones_remove_old_values(self):
        _, observations, cutoff = sample(8)
        revision = copy.deepcopy(observations[0]); revision['observed_at_utc'] = '2025-01-06T18:00:00Z'
        revision['home']['total_shots'] = 40
        tombstone = {**copy.deepcopy(revision), 'observed_at_utc': '2025-01-07T18:00:00Z',
                     'available': False, 'home': None, 'away': None}
        original = FormIndex(observations, cutoff)
        changed = FormIndex(observations+[revision, tombstone], cutoff)
        np.testing.assert_array_equal(original.pair('A','B','2025-01-06T00:00:00Z')[0],
                                      changed.pair('A','B','2025-01-06T00:00:00Z')[0])
        self.assertGreater(changed.form('A','2025-01-07T00:00:00Z')[0][STAT_FIELDS.index('total_shots')], 20)
        self.assertEqual(changed.form('A','2025-01-08T00:00:00Z')[1], 6)

    def test_zero_missing_stale_and_conflicting_observations_are_distinct(self):
        _, observations, cutoff = sample(8)
        for item in observations:
            item['home']['fouls'] = item['away']['fouls'] = 0
            item['home']['ball_possession'] = item['away']['ball_possession'] = None
        index = FormIndex(observations, cutoff)
        x, _ = index.pair('A', 'B', cutoff)
        self.assertEqual(x[0, STAT_FIELDS.index('fouls')], 0)
        self.assertTrue(np.isnan(x[0, STAT_FIELDS.index('ball_possession')]))
        self.assertIsNone(index.pair('A','B',cutoff+pd.Timedelta(days=200))[0])
        bad = copy.deepcopy(observations[0]); bad['home']['total_shots'] = 40
        with self.assertRaisesRegex(ValueError, 'Contradictory'):
            FormIndex(observations+[bad], cutoff)

    def test_team_side_values_and_percentages_must_be_valid(self):
        _, observations, cutoff = sample(4)
        for change in ({'ball_possession':101}, {'total_shots':-1}, {'fouls':True},
                       {'total_shots':float('nan')}, {'accurate_passes':999}):
            bad = copy.deepcopy(observations); bad[0]['home'].update(change)
            with self.subTest(change=change), self.assertRaises(ValueError): FormIndex(bad, cutoff)


class LearningTests(OfflineQuotePolicyTestCase):
    def test_informative_statistics_activate_and_change_safe_goal_rates(self):
        frame, _, cutoff = sample()
        learned = fit_statistics(frame, cutoff, constant_baseline)
        self.assertEqual(learned.report['status'], 'VALIDATED')
        rates, info = learned.apply('A', 'B', [1., 1.])
        self.assertTrue(info['bbs_statistics_applied'])
        self.assertGreater(rates[0], 1.)
        self.assertLess(rates[1], 1.)
        self.assertLessEqual(rates[0], 1.25)
        self.assertGreaterEqual(rates[1], .8)
        self.assertGreater(learned.report['audit_gain_lower95'], 0)
        with tempfile.TemporaryDirectory() as tmp:
            artifact = learned.save(tmp, 'EPL')
            self.assertTrue(artifact.is_file())
            self.assertEqual(learned.save(tmp, 'EPL'), artifact)
            artifact.write_text('{}')
            with self.assertRaisesRegex(ValueError, 'Immutable'): learned.save(tmp, 'EPL')
        _, missing = learned.apply('Unknown', 'B', [1., 1.])
        self.assertFalse(missing['bbs_statistics_applied'])

    def test_audit_outcomes_never_select_hyperparameters_and_can_reject(self):
        frame, _, cutoff = sample()
        accepted = fit_statistics(frame, cutoff, constant_baseline)
        changed = frame.copy(deep=True)
        changed.loc[changed.index[-40:], ['FTHG', 'FTAG']] = 1
        rejected = fit_statistics(changed, cutoff, constant_baseline)
        self.assertEqual(rejected.report['selected_ridge'], accepted.report['selected_ridge'])
        self.assertEqual(rejected.report['proposed_weight'], accepted.report['proposed_weight'])
        self.assertEqual(rejected.report['status'], 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED')
        np.testing.assert_array_equal(rejected.apply('A','B',[1.,1.])[0], [1.,1.])

    def test_late_backfill_cannot_manufacture_historical_training_examples(self):
        frame, observations, cutoff = sample()
        for row in observations: row['observed_at_utc'] = cutoff.isoformat()
        frame.attrs['bbs_statistics_observations'] = observations
        learned = fit_statistics(frame, cutoff+pd.Timedelta(days=1), constant_baseline,
                                 validation_mode='strict')
        self.assertEqual(learned.report['eligible_training_matches'], 0)
        self.assertIsNone(learned.model)
        self.assertEqual(learned.report['status'], 'INSUFFICIENT_PAST_OBSERVATIONS')

    def test_auto_backfill_is_labelled_and_live_serving_keeps_actual_observation_time(self):
        frame, observations, cutoff = sample()
        fetched = cutoff + pd.Timedelta(days=1)
        for row in observations:
            row['observed_at_utc'] = fetched.isoformat()
        frame.attrs['bbs_statistics_observations'] = observations
        learned = fit_statistics(frame, fetched+pd.Timedelta(days=1), constant_baseline)
        self.assertEqual(learned.report['validation_mode'], 'retrospective_backfill')
        self.assertEqual(learned.report['strict_eligible_training_matches'], 0)
        self.assertGreater(learned.report['eligible_training_matches'], 120)
        self.assertEqual(learned.report['status'], 'VALIDATED')
        self.assertFalse(learned.report['forward_accuracy_improvement_established'])
        self.assertTrue(learned.report['historical_corrections_may_be_present'])
        self.assertEqual(learned.index.availability_field, 'observed_at_utc')
        self.assertTrue(all(r['observed_at_utc'] == fetched.isoformat() for r in learned.index.records))
        self.assertIsNone(learned.index.pair('A','B',cutoff)[0])
        _, info = learned.apply('A','B',[1.,1.])
        self.assertTrue(info['bbs_statistics_applied'])
        self.assertEqual(info['bbs_statistics_validation_mode'], 'retrospective_backfill')
        with tempfile.TemporaryDirectory() as tmp:
            import json
            payload=json.loads(learned.save(tmp,'EPL').read_text())
            self.assertEqual(payload['report']['validation_mode'], 'retrospective_backfill')
        # A historical outer cutoff cannot see backfill fetched in the future,
        # even though auto mode permits retrospective development at today's cutoff.
        replay = fit_statistics(frame, cutoff, constant_baseline)
        self.assertEqual(replay.report['observations'], 0)
        self.assertIsNone(replay.model)

    def test_retrospective_delay_tombstones_and_latest_revision_are_explicit(self):
        frame, observations, cutoff = sample(9)
        for row in observations: row['observed_at_utc'] = cutoff.isoformat()
        revised = copy.deepcopy(observations[0]); revised['home']['total_shots'] = 40
        revised['observed_at_utc'] = (cutoff+pd.Timedelta(hours=1)).isoformat()
        held = {**copy.deepcopy(observations[1]), 'available': False,
                'observed_at_utc': (cutoff+pd.Timedelta(hours=2)).isoformat()}
        future = {**copy.deepcopy(revised), 'observed_at_utc': (cutoff+pd.Timedelta(days=3)).isoformat(),
                  'home': {**revised['home'], 'total_shots': 999}}
        strict = FormIndex(observations+[revised,held,future],cutoff+pd.Timedelta(days=1))
        retro = strict.retrospective()
        self.assertEqual(len(retro.records),9)
        first=next(r for r in retro.records if r['match_id']=='0')
        self.assertEqual(first['home']['total_shots'],40)
        self.assertEqual(first['observed_at_utc'], revised['observed_at_utc'])
        self.assertEqual(retro.form('A','2025-01-02T12:00:00Z')[1],0)  # Delay equality excluded.
        self.assertEqual(retro.form('A','2025-01-02T12:00:01Z')[1],1)
        self.assertEqual(retro.form('A','2025-01-10T00:00:00Z')[1],7)  # Held and last-day not ready.
        frame.attrs['bbs_statistics_observations'] = observations+[revised,held,future]
        result=fit_statistics(frame,cutoff+pd.Timedelta(days=1),constant_baseline)
        self.assertEqual(result.report['status'],'INSUFFICIENT_RETROSPECTIVE_EXAMPLES')
        self.assertIsNone(result.model)
        with self.assertRaisesRegex(ValueError,'validation mode'):
            fit_statistics(frame,cutoff,constant_baseline,validation_mode='invalid')

    def test_validation_policy_is_bound_to_fingerprints_and_cli(self):
        from goal_market_validation import training_fingerprint
        frame, _, _ = sample(9)
        original=training_fingerprint(frame)
        frame.attrs['bbs_statistics_validation']='strict'
        self.assertNotEqual(original,training_fingerprint(frame))
        self.assertEqual(build_parser().parse_args([]).bbs_statistics_validation,'auto')
        self.assertEqual(build_parser().parse_args(['--bbs-statistics-validation','strict']).bbs_statistics_validation,'strict')
        pipe=FootballValuePipelineV2(bbs_statistics_validation='strict')
        self.assertEqual(pipe.bbs_statistics_validation,'strict')
        with self.assertRaisesRegex(ValueError,'validation mode'):
            FootballValuePipelineV2(bbs_statistics_validation='invalid')

    def test_scaling_uses_training_only_and_missing_fields_are_not_zero_statistics(self):
        x = np.array([[1., np.nan], [2., np.nan], [3., np.nan], [4., np.nan]])
        model = PoissonForm.fit(x, np.array([0,1,2,3]), 10.)
        before = model.median.copy()
        self.assertEqual(model.design(x)[0,-1], 1.)
        self.assertEqual(model.design(np.array([[1.,0.]]))[0,-1], 1.)  # Unsupported column stays masked.
        self.assertEqual(model.design(np.array([[np.nan,0.]]))[0,-2], 1.)
        self.assertTrue(np.isfinite(model.predict(np.array([[9999.,0.]]))).all())
        np.testing.assert_array_equal(model.predict(np.array([[2.,0.],[2.,1000.]])),
                                      np.repeat(model.predict(np.array([[2.,np.nan]])),2))
        np.testing.assert_array_equal(model.median, before)


class IntegrationTests(OfflineQuotePolicyTestCase):
    def test_no_stats_or_disabled_mode_preserves_original_probabilities_exactly(self):
        frame = plain_history(); origin = pd.Timestamp('2026-01-01T00:00:00Z')
        normal = DixonColesModel().fit(frame, as_of=origin)
        disabled = DixonColesModel(bbs_statistics=False).fit(frame, as_of=origin)
        np.testing.assert_array_equal(normal.score_matrix('A','B')[0], disabled.score_matrix('A','B')[0])
        self.assertFalse(normal.score_matrix('A','B')[1]['bbs_statistics_applied'])
        self.assertTrue(build_parser().parse_args(['--no-bbs-statistics']).no_bbs_statistics)

    def test_learned_rates_reach_all_probability_markets_before_bookmaker_blending(self):
        frame, _, cutoff = sample()
        learned = fit_statistics(frame, cutoff, constant_baseline)
        model = DixonColesModel(); model.teams=['A','B']; model.team_to_idx={'A':0,'B':1}
        model.attack=model.weakness=np.zeros(2);model.base=model.home_adv=model.rho=0.
        model.statistics_model=learned;model.bbs_statistics_report=learned.report
        pipeline=object.__new__(FootballValuePipelineV2);pipeline.market_weight=0.;pipeline.devig_method='power'
        row=pd.Series({'HomeTeam':'A','AwayTeam':'B'})
        enhanced, _=pipeline._predict_row(model,row)
        model.statistics_model=None; model.bbs_statistics_report={'status':'DISABLED'}
        baseline, _=pipeline._predict_row(model,row)
        self.assertTrue(enhanced['bbs_statistics_applied'])
        for field in ('p_home','p_away','p_over_1_5','p_under_3_5','p_btts_yes'):
            self.assertNotAlmostEqual(enhanced[field], baseline[field], places=6)
            self.assertAlmostEqual(enhanced['bbs_control_'+field], baseline[field])
        self.assertAlmostEqual(sum(enhanced[k] for k in ('p_home','p_draw','p_away')),1.)
        model.statistics_model=learned;model.bbs_statistics_report=learned.report
        pipeline.market_weight=.5
        with patch('football_value_pipeline_v2_standalone.market_snapshot', return_value={
                'market_p_home':.4,'market_p_draw':.3,'market_p_away':.3}), patch(
                'football_value_pipeline_v2_standalone.add_value_metrics'):
            blended, _=pipeline._predict_row(model,row)
        self.assertTrue(blended['market_blend_applied'])
        for side, market in [('home',.4),('draw',.3),('away',.3)]:
            self.assertAlmostEqual(blended['p_'+side],.5*enhanced['p_'+side]+.5*market)
            self.assertAlmostEqual(blended['bbs_control_p_'+side],baseline['p_'+side])

    def test_forward_comparison_uses_only_paired_frozen_forecasts_and_verified_results(self):
        from bbs_statistics_model import forward_assessment
        from tests.test_performance_tracking import fixture, final, KICK, T0
        from performance_tracking import fixture_key, verified_record
        row=fixture()
        row.update(fixture_key=fixture_key(row),snapshot_commit='a'*40,
            snapshot_generated_utc=T0.isoformat(),snapshot_captured_utc=T0.isoformat(),
            bbs_statistics_applied='True',bbs_statistics_validation_mode='retrospective_backfill',
            bbs_statistics_cutoff_utc=T0.isoformat(),
            bbs_statistics_latest_observed_utc=(T0-timedelta(hours=1)).isoformat())
        for key in ('home','draw','away','over_1_5','under_3_5','btts_yes'):
            row['raw_p_'+key]=row['p_'+key]
            row['bbs_control_p_'+key]=row['p_'+key]
        row.update(bbs_control_p_home=.4,bbs_control_p_draw=.3,bbs_control_p_away=.3)
        record=verified_record('PL',final())
        clock=KICK+timedelta(hours=3)
        report=forward_assessment([row],[record],clock)
        self.assertEqual(report['paired_matches'],1)
        self.assertLess(report['candidate_mean_briers'][0],report['control_mean_briers'][0])
        self.assertFalse(report['automatic_promotion'])
        self.assertEqual(report['by_validation_mode']['retrospective_backfill']['paired_matches'],1)
        for records,when in [([],clock),([record],KICK)]:
            waiting=forward_assessment([row],records,when)
            self.assertEqual(waiting['pending_matches'],1)
            self.assertEqual(waiting['paired_matches'],0)
        self.assertEqual(forward_assessment([{}],[],clock)['paired_matches'],0)
        for change in ({'snapshot_captured_utc':(KICK+timedelta(hours=1)).isoformat()},
                       {'bbs_statistics_latest_observed_utc':T0.isoformat()},
                       {'raw_p_home':'nan'}, {'bbs_control_p_draw':.9},
                       {'bbs_statistics_validation_mode':'unknown'},
                       {'bbs_statistics_cutoff_utc':None}):
            with self.subTest(change=change):
                rejected=forward_assessment([{**row,**change}],[record],clock)
                self.assertEqual(rejected['invalid_forecasts'],1)
                self.assertEqual(rejected['paired_matches'],0)

    def test_feature_sources_preserve_revisions_and_hold_disputes_and_wrong_ids(self):
        from tests.test_bbs_data import base, match, NOW
        from bbs_data import normal_match
        from bbs_integration import build_dataset, write_dataset, combined_training_history
        with tempfile.TemporaryDirectory() as tmp:
            cache=Path(tmp);store=Store(cache/'bbs/state')
            m=normal_match(match(),'EPL',NOW.isoformat(),{});m['requested_season']=2026
            store.put('match','EPL','m1',NOW.isoformat(),m)
            stats={'available':True,'team_ids':{'home':'h1','away':'a1'},'home':values(True),'away':values(False)}
            stats['home']['total_shots']=8;stats['home']['shots_on_target']=4
            store.put('statistics','EPL','m1',NOW.isoformat(),stats)
            write_dataset(build_dataset(store,base(),NOW.isoformat()),cache/'bbs/combined')
            result=combined_training_history(pd.DataFrame(base()),cache,'EPL',NOW+timedelta(seconds=1),4)
            records=result.attrs['bbs_statistics_observations']
            self.assertEqual(len(records),1);self.assertTrue(records[0]['available'])
            later=NOW+timedelta(minutes=1)
            unavailable={**stats,'available':False,'home':None,'away':None}
            store.put('statistics','EPL','m1',later.isoformat(),unavailable)
            records=feature_observations(result,cache,'EPL')
            self.assertEqual(len(records),2);self.assertFalse(records[-1]['available'])
            wrong={**stats,'team_ids':{'home':'other','away':'a1'}}
            store.put('statistics','EPL','m1',(later+timedelta(seconds=1)).isoformat(),wrong)
            self.assertFalse(feature_observations(result,cache,'EPL')[-1]['available'])
            store.put('statistics_quarantine','EPL','m1',(later+timedelta(seconds=2)).isoformat(),{'reason':'bad identity'})
            self.assertFalse(feature_observations(result,cache,'EPL')[-1]['available'])
            store.put('statistics_quarantine','EPL','m1',NOW.isoformat(),{'reason':'same-instant revalidation'})
            self.assertFalse(feature_observations(result,cache,'EPL')[0]['available'])
            result.loc[0,'bbs_conflict_flags']='statistic_conflict'
            self.assertFalse(any(r['available'] for r in feature_observations(result,cache,'EPL')))

    def test_optional_source_corruption_does_not_break_verified_score_history(self):
        from tests.test_bbs_data import base, match, NOW
        from bbs_data import normal_match
        from bbs_integration import build_dataset, write_dataset, combined_training_history
        with tempfile.TemporaryDirectory() as tmp:
            cache=Path(tmp);store=Store(cache/'bbs/state')
            m=normal_match(match(),'EPL',NOW.isoformat(),{});m['requested_season']=2026
            store.put('match','EPL','m1',NOW.isoformat(),m)
            write_dataset(build_dataset(store,base(),NOW.isoformat()),cache/'bbs/combined')
            folder=cache/'bbs/state/observations/statistics';folder.mkdir(parents=True)
            (folder/'broken.json').write_text('{bad')
            frame=combined_training_history(pd.DataFrame(base()),cache,'EPL',NOW,4)
            self.assertEqual(len(frame),1)
            self.assertTrue(frame.attrs['bbs_statistics_source_error'])
            self.assertEqual(frame.attrs['bbs_statistics_observations'],[])

    def test_model_fit_invokes_feature_training_and_carries_mode_to_validation(self):
        frame, _, cutoff=sample()
        learned=fit_statistics(frame,cutoff,constant_baseline)
        with patch('bbs_statistics_model.fit_statistics',return_value=learned) as fitter:
            model=DixonColesModel().fit(frame,as_of=cutoff)
        self.assertIs(model.statistics_model,learned)
        self.assertEqual(fitter.call_count,1)
        frame.attrs['bbs_statistics_enabled']=False
        with patch('bbs_statistics_model.fit_statistics') as fitter:
            model=DixonColesModel().fit(frame,as_of=cutoff)
        self.assertFalse(fitter.called)
        self.assertEqual(model.bbs_statistics_report['status'],'DISABLED')

    def test_failed_optional_fit_retains_baseline_and_exposes_reason(self):
        frame=plain_history();frame.attrs['bbs_statistics_observations']=[{'bad':'payload'}]
        with self.assertWarns(UserWarning): model=DixonColesModel().fit(frame,as_of='2026-01-01')
        self.assertEqual(model.bbs_statistics_report['status'],'BASELINE_RETAINED_FEATURE_ERROR')
        self.assertFalse(model.score_matrix('A','B')[1]['bbs_statistics_applied'])

    def test_unsafe_adjustment_falls_back_to_valid_dc_grid(self):
        model=DixonColesModel();model.teams=['A','B'];model.team_to_idx={'A':0,'B':1}
        model.attack=model.weakness=np.zeros(2);model.base=model.home_adv=0.;model.rho=-.2
        base=model.score_matrix('A','B')[0]
        model.statistics_model=SimpleNamespace(apply=lambda *args:(np.array([6.,6.]),{'bbs_statistics_applied':True}))
        matrix, meta=model.score_matrix('A','B')
        np.testing.assert_array_equal(matrix,base)
        self.assertEqual(meta['bbs_statistics_status'],'UNSAFE_ADJUSTMENT_BASELINE_RETAINED')

    def test_rejected_provider_revision_holds_old_statistics_and_requests_recovery(self):
        import json
        from datetime import timedelta
        from tests.test_bbs_data import NOW, match
        from bbs_data import Client, collect, normal_match
        clock=NOW+timedelta(days=8)
        with tempfile.TemporaryDirectory() as tmp:
            store=Store(Path(tmp)/'bbs')
            m=normal_match(match(),'EPL',NOW.isoformat(),{});m['requested_season']=2026
            store.put('match','EPL','m1',NOW.isoformat(),m)
            good={'available':True,'team_ids':{'home':'h1','away':'a1'},'home':values(True),'away':values(False)}
            store.put('statistics','EPL','m1',NOW.isoformat(),good)
            calls=[]; broken=[True]
            def sender(path,params,key):
                calls.append(path)
                if path=='/v1/matches': data=[match()] if params['status']=='finished' else []
                elif path=='/v1/standings': data={'standings':[]}
                elif path.endswith('/statistics'):
                    data={'home':{**values(True),'team_id':'wrong' if broken[0] else 'h1'},
                          'away':{**values(False),'team_id':'a1'}}
                else:data=[]
                return 200,{},json.dumps({'data':data}).encode()
            client=Client(store,'offline',sender=sender,clock=lambda:clock,sleeper=lambda _:None)
            report=collect(client,['EPL'],[2026])
            self.assertEqual(report['coverage']['EPL']['statistics_quarantined'],1)
            self.assertEqual(report['coverage']['EPL']['statistics_available'],0)
            broken[0]=False;clock+=timedelta(minutes=1)
            report=collect(client,['EPL'],[2026])
            self.assertEqual(calls.count('/v1/matches/m1/statistics'),2)
            self.assertEqual(report['coverage']['EPL']['statistics_quarantined'],0)
            self.assertEqual(report['coverage']['EPL']['statistics_available'],1)
