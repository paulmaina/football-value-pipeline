import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from api_key_config import API_KEY_NAMES, load_api_keys


class APIKeyConfigTests(unittest.TestCase):
    def test_file_overrides_all_inherited_keys_without_touching_other_environment(self):
        with tempfile.TemporaryDirectory() as tmp, patch.dict(os.environ,{**{k:'shell-secret' for k in API_KEY_NAMES},'UNRELATED_SETTING':'keep'},clear=True):
            file=Path(tmp)/'.env'
            file.write_text('\n'.join(k+'="file-'+str(i)+'"' for i,k in enumerate(API_KEY_NAMES)))
            report=load_api_keys(path=file)
            for i,key in enumerate(API_KEY_NAMES):self.assertEqual(os.environ[key],'file-'+str(i))
            self.assertEqual(os.environ['UNRELATED_SETTING'],'keep')
            self.assertEqual(report,{k:True for k in API_KEY_NAMES})
            self.assertNotIn('file-',str(report))

    def test_missing_blank_and_deleted_entries_never_fall_back_to_shell(self):
        with tempfile.TemporaryDirectory() as tmp, patch.dict(os.environ,{k:'shell-secret' for k in API_KEY_NAMES},clear=True):
            file=Path(tmp)/'.env'
            file.write_text('THE_ODDS_API_KEY=from-file\nTHE_ODDS_API_KEY_FALLBACK_1=\nFOOTBALL_DATA_API_KEY\n')
            load_api_keys(path=file)
            self.assertEqual(os.environ['THE_ODDS_API_KEY'],'from-file')
            for key in API_KEY_NAMES[1:]:self.assertEqual(os.environ[key],'')
            file.unlink();load_api_keys(path=file)
            for key in API_KEY_NAMES:self.assertEqual(os.environ[key],'')

    def test_no_interpolation_from_powershell(self):
        with tempfile.TemporaryDirectory() as tmp, patch.dict(os.environ,{'OLD_TOKEN':'shell-secret'},clear=True):
            file=Path(tmp)/'.env';file.write_text('THE_ODDS_API_KEY=${OLD_TOKEN}\n')
            load_api_keys(path=file)
            self.assertEqual(os.environ['THE_ODDS_API_KEY'],'${OLD_TOKEN}')

    def test_project_location_is_independent_of_working_directory(self):
        with tempfile.TemporaryDirectory() as tmp, patch.dict(os.environ,clear=True):
            file=Path(tmp)/'.env';file.write_text('FOOTBALL_DATA_API_KEY=project-secret\n')
            with patch('api_key_config.ENV_PATH',file):load_api_keys()
            self.assertEqual(os.environ['FOOTBALL_DATA_API_KEY'],'project-secret')

    def test_explicit_ci_environment_mode_preserves_secrets(self):
        with patch.dict(os.environ,{k:'ci-secret' for k in API_KEY_NAMES},clear=True):
            self.assertTrue(all(load_api_keys('environment').values()))
            for key in API_KEY_NAMES:self.assertEqual(os.environ[key],'ci-secret')
        with self.assertRaises(ValueError):load_api_keys('other')

    def test_pipeline_cli_loads_before_constructing_clients(self):
        from football_value_pipeline_v2_standalone import main
        for mode in ('dotenv','environment'):
            with tempfile.TemporaryDirectory() as tmp, patch.dict(os.environ,{k:'shell-secret' for k in API_KEY_NAMES},clear=True), patch('api_key_config.ENV_PATH',Path(tmp)/'.env'), patch('football_value_pipeline_v2_standalone.FootballValuePipelineV2',side_effect=RuntimeError('stop before requests')):
                file=Path(tmp)/'.env';file.write_text('THE_ODDS_API_KEY=file-secret\n')
                with self.assertRaisesRegex(RuntimeError,'stop before requests'):
                    main(['--api-key-source',mode,'--out-dir',str(Path(tmp)/'output')])
                self.assertEqual(os.environ['THE_ODDS_API_KEY'],'file-secret' if mode=='dotenv' else 'shell-secret')
                self.assertEqual(os.environ['FOOTBALL_DATA_API_KEY'],'' if mode=='dotenv' else 'shell-secret')

    def test_performance_review_cli_uses_file_and_explicit_ci_mode(self):
        from performance_tracking import main
        for mode in ('dotenv','environment'):
            with tempfile.TemporaryDirectory() as tmp, patch.dict(os.environ,{'FOOTBALL_DATA_API_KEY':'shell-secret'},clear=True), patch('api_key_config.ENV_PATH',Path(tmp)/'.env'), patch('performance_tracking.review') as review:
                (Path(tmp)/'.env').write_text('FOOTBALL_DATA_API_KEY=file-secret\n')
                self.assertEqual(main(['review','--api-key-source',mode]),0)
                self.assertEqual(review.call_args.kwargs['token'],'file-secret' if mode=='dotenv' else 'shell-secret')
