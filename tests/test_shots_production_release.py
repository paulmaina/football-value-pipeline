"""Release defaults, genuine same-run legacy trial binding and offline failure isolation."""
from offline_test_case import OfflineQuotePolicyTestCase
import copy
import json
import os
from datetime import datetime, timezone
from pathlib import Path
import tempfile
from unittest.mock import patch
import numpy as np
import pandas as pd

import benchmark_forward_experiment as bf
import totals_anchor_experiment as ta
from forward_trial_basis import legacy_basis, bound_inputs
from football_value_pipeline_v2_standalone import (FootballValuePipelineV2, MODEL_VERSION,
    LEGACY_MODEL_VERSION, NO_SHOTS_MODEL_VERSION, build_parser)
from performance_tracking import fixture_key, read_csv
from test_totals_anchor_experiment import sample, NOW


def companion_row():
    legacy,matrix,inputs=sample()
    row={**legacy, 'model_version':MODEL_VERSION, 'market_weight':.7,
         'totals_anchor_applied':True, 'legacy_model_version':LEGACY_MODEL_VERSION,
         'legacy_status':'AVAILABLE', 'legacy_trial_matrix':json.dumps(matrix.tolist()),
         'legacy_trial_inputs':json.dumps(inputs)}
    row.update({'legacy_'+k:legacy.get(k) for k in FootballValuePipelineV2.LEGACY_COLUMNS})
    # Distinct production predictions ensure the frozen trial cannot borrow them.
    row.update(p_home=.6,p_draw=.25,p_away=.15,p_over_1_5=.8)
    return row,matrix,inputs


class ShotsReleaseTests(OfflineQuotePolicyTestCase):
    def test_normal_and_scheduled_forecasts_use_gated_shots_without_opt_in(self):
        self.assertFalse(build_parser().parse_args([]).no_shot_features)
        self.assertTrue(build_parser().parse_args(['--no-shot-features']).no_shot_features)
        self.assertTrue(FootballValuePipelineV2.__init__.__kwdefaults__['shot_features'])
        command=Path('publish_scheduled_forecasts.py').read_text()
        self.assertNotIn('--no-shot-features',command)
        self.assertNotIn('--experimental-shot-features',command)
        cfg=json.loads(Path('historical_benchmark_config.json').read_text())['model_upgrade_comparison']['production_v2']
        self.assertEqual(cfg['model_version'],MODEL_VERSION)
        self.assertTrue(cfg['shot_features'])
        self.assertEqual(cfg['feature_rule'],'bbs_priority_mutually_exclusive_shots')

    def test_optional_history_failure_does_not_abort_offline_ucl_validation(self):
        from football_value_pipeline_v2_standalone import main, LEAGUES
        from test_conservative_bet_filter import fixture
        from test_graded_candidates import sample_report
        production=fixture();production['league']='UEFA Champions League'
        def forecast(pipeline, key):
            legacy,status=pipeline._fit_legacy_model(pd.DataFrame(),datetime.now(timezone.utc),LEAGUES[key])
            row={**production, **pipeline._legacy_columns(legacy,pd.Series(production),status)}
            return pd.DataFrame([row]),{'training_end':'2026-09-20','training_matches':1000},{}
        with tempfile.TemporaryDirectory() as tmp, patch.dict(os.environ,{},clear=True), patch(
                'api_key_config.load_api_keys',return_value={}), patch(
                'football_value_pipeline_v2_standalone.FootballValuePipelineV2.run_league',new=forecast), patch(
                'football_value_pipeline_v2_standalone.FootballValuePipelineV2.backtest_league',
                return_value=(pd.DataFrame(),pd.DataFrame(),{},pd.DataFrame())), patch(
                'goal_market_validation.evaluate_market_history',return_value={**sample_report(),'league':'UEFA Champions League'}):
            raw=Path(tmp)/'raw'
            self.assertNotIn('FOOTBALL_DATA_API_KEY',os.environ)
            self.assertEqual(main(['--leagues','UCL','--out-dir',str(raw)]),0)
            output=read_csv(raw/'UCL_predictions.csv')
            self.assertEqual(len(output),1)
            self.assertEqual(output[0]['legacy_status'],'UNAVAILABLE_HALF_LIFE_TUNING_RuntimeError')
            self.assertEqual(float(output[0]['p_home']),production['p_home'])
            self.assertTrue((raw/'conservative_bet_summary.json').is_file())

    def test_legacy_matrix_capture_handles_missing_optional_quote_without_poisoning_production(self):
        from test_model_upgrades_v2 import pipe, toy_model, live_row
        row=live_row();row['shadow_pinnacle_totals']=float('nan')
        result=pipe()._legacy_columns(toy_model(),row,'AVAILABLE')
        self.assertEqual(result['legacy_status'],'AVAILABLE')
        self.assertIsNone(json.loads(result['legacy_trial_inputs'])['reference'])
        row['shadow_pinnacle_totals']={'over':float('nan')}
        result=pipe()._legacy_columns(toy_model(),row,'AVAILABLE')
        self.assertEqual(result['legacy_status'],'UNAVAILABLE_PREDICTION_ValueError')
        self.assertIsNone(result['legacy_p_home'])

    def test_new_forecasts_continue_frozen_trials_using_legacy_companion(self):
        row,matrix,inputs=companion_row();before=copy.deepcopy(row)
        registry=bf.load_registry()
        result=bf.decision(row,registry,NOW)
        expected=bf.decision(legacy_basis(row),registry,NOW)
        self.assertEqual(result,expected)
        self.assertEqual(result['status'],'available',result['reasons'])
        self.assertEqual(result['comparison_model_version'],LEGACY_MODEL_VERSION)
        self.assertEqual(result['forecast_model_version'],MODEL_VERSION)
        self.assertEqual(result['baseline'],[row['legacy_p_'+k] for k in ('home','draw','away')])
        totals=ta.decision(row,matrix,inputs,NOW,ta.registry()[0])
        self.assertEqual(totals['status'],'available',totals['reasons'])
        self.assertEqual(totals['comparison_basis'],'same_run_legacy_companion')
        self.assertEqual(row,before)

    def test_both_sidecars_roundtrip_and_reject_tampered_legacy_evidence(self):
        row,matrix,inputs=companion_row()
        with tempfile.TemporaryDirectory() as tmp:
            raw=Path(tmp);data=pd.DataFrame([row]);data.to_csv(raw/'all_leagues_predictions.csv',index=False)
            # Wrong production matrix must be ignored in favour of bound companion evidence.
            wrong=np.ones((3,3))/9
            bridge=bf.write_experiment(data,raw,NOW.isoformat(),{fixture_key(row):wrong})
            totals=ta.write_experiment(data,raw,NOW.isoformat(),{fixture_key(row):wrong},{})
            original=read_csv(raw/'all_leagues_predictions.csv')
            bf.validate(bridge,NOW.isoformat(),original)
            ta.validate(totals,NOW.isoformat(),original)
            np.testing.assert_allclose(bridge['rows'][0]['production_matrix'],matrix)
            changed=copy.deepcopy(original);changed[0]['legacy_p_home']=.99
            with self.assertRaises(ValueError):bf.validate(bridge,NOW.isoformat(),changed)
            with self.assertRaises(ValueError):ta.validate(totals,NOW.isoformat(),changed)

    def test_missing_or_stale_companion_never_borrows_production_evidence(self):
        row,_,_=companion_row()
        for version in (MODEL_VERSION,NO_SHOTS_MODEL_VERSION):
            bad={**row,'model_version':version,'legacy_status':'UNAVAILABLE'}
            self.assertIs(legacy_basis(bad),bad)
            self.assertEqual(bf.decision(bad,bf.load_registry(),NOW)['status'],'unavailable')
        missing={**row,'legacy_raw_p_home':None}
        self.assertEqual(bf.decision(missing,bf.load_registry(),NOW)['status'],'unavailable')
        matrix,inputs=bound_inputs({**row,'legacy_trial_matrix':'invalid'})
        self.assertIsNone(matrix);self.assertIsNone(inputs)

    def test_archived_rows_without_new_companion_binding_keep_their_old_basis(self):
        row,_,_=companion_row()
        row.pop('legacy_trial_matrix');row.pop('legacy_trial_inputs')
        self.assertIs(legacy_basis(row),row)
        result=bf.decision(row,bf.load_registry(),NOW)
        self.assertEqual(result['status'],'unavailable')
        self.assertNotIn('comparison_basis',result)
