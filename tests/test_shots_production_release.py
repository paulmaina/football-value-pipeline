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

from football_value_pipeline_v2_standalone import (FootballValuePipelineV2, MODEL_VERSION,
    LEGACY_MODEL_VERSION, NO_SHOTS_MODEL_VERSION, build_parser)
from performance_tracking import fixture_key, read_csv


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
        self.assertEqual(cfg['feature_rule'],'shot_features_only')

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
                'football_value_pipeline_v2_standalone.FootballValuePipelineV2._history_for_league',
                side_effect=RuntimeError('optional history unavailable')), patch(
                'football_value_pipeline_v2_standalone.FootballValuePipelineV2.run_league',new=forecast), patch(
                'football_value_pipeline_v2_standalone.FootballValuePipelineV2.backtest_league',
                return_value=(pd.DataFrame(),pd.DataFrame(),{},pd.DataFrame())), patch(
                'goal_market_validation.evaluate_market_history',return_value={**sample_report(),'league':'UEFA Champions League'}):
            raw=Path(tmp)/'raw'
            self.assertNotIn('FOOTBALL_DATA_API_KEY',os.environ)
            self.assertEqual(main(['--leagues','UCL','--out-dir',str(raw),'--legacy-comparison']),0)
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
