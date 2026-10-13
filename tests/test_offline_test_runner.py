from pathlib import Path
import unittest
from unittest.mock import Mock, patch
import quote_policy
from run_offline_tests import main


class OfflineTestRunnerTests(unittest.TestCase):
    def test_suite_uses_test_policy_without_changing_production_setting(self):
        original = quote_policy.CONFIG
        def discover(path):
            self.assertEqual(quote_policy.load_policy()['allowed_bookmakers'], [])
            self.assertEqual(Path(path), Path(__file__).resolve().parent)
            return unittest.TestSuite()
        for success in (True, False):
            runner = Mock(); runner.run.return_value.wasSuccessful.return_value = success
            with patch('unittest.defaultTestLoader.discover', side_effect=discover), patch('unittest.TextTestRunner', return_value=runner):
                self.assertEqual(main([]), 0 if success else 1)
            self.assertEqual(quote_policy.CONFIG, original)

    def test_model_self_test_is_isolated_from_personal_allowlist(self):
        original = quote_policy.CONFIG
        with patch('football_value_pipeline_v2_standalone.self_test') as model:
            self.assertEqual(main(['--model-self-test']), 0)
            model.assert_called_once()
        self.assertEqual(quote_policy.CONFIG, original)
