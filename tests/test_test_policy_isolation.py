"""Conventional runners must never inherit or overwrite the user's allowlist."""
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from offline_test_case import OfflineQuotePolicyTestCase
import quote_policy


class PolicyIsolationTests(OfflineQuotePolicyTestCase):
    def test_success_and_failure_restore_the_callers_policy(self):
        production = Path(quote_policy.__file__).with_name('shortlist_quote_policy.json')
        before = production.read_bytes() if production.exists() else None
        with tempfile.TemporaryDirectory() as directory:
            personal = Path(directory)/'personal.json'
            personal.write_text('{"allowed_bookmakers":["1xBet"]}', encoding='utf-8')
            for fail in (False, True):
                observed = []
                class Probe(OfflineQuotePolicyTestCase):
                    def test_policy(probe):
                        observed.append(quote_policy.load_policy()['allowed_bookmakers'])
                        if fail:
                            probe.fail('deliberate test failure')
                with patch.object(quote_policy, 'CONFIG', personal):
                    result = unittest.TestResult()
                    Probe('test_policy').run(result)
                    self.assertEqual(observed, [[]])
                    self.assertEqual(quote_policy.CONFIG, personal)
                    self.assertEqual(quote_policy.load_policy()['allowed_bookmakers'], ['1xBet'])
                    self.assertEqual(len(result.failures), int(fail))
        self.assertEqual(production.read_bytes() if production.exists() else None, before)

    def test_subclass_setup_without_super_still_gets_offline_policy(self):
        observed = []
        class Probe(OfflineQuotePolicyTestCase):
            def setUp(probe):
                observed.append(quote_policy.load_policy()['allowed_bookmakers'])
            def test_policy(probe):
                probe.assertEqual(quote_policy.load_policy()['allowed_bookmakers'], [])
        result = unittest.TestResult()
        Probe('test_policy').run(result)
        self.assertTrue(result.wasSuccessful())
        self.assertEqual(observed, [[]])

    def test_explicit_test_policy_overrides_still_work(self):
        original = quote_policy.CONFIG
        with tempfile.TemporaryDirectory() as directory:
            file = Path(directory)/'test-policy.json'
            file.write_text('{"allowed_bookmakers":["Specific test book"],"per_stake_cost_bps":15}', encoding='utf-8')
            with patch.object(quote_policy, 'CONFIG', file):
                self.assertEqual(quote_policy.load_policy()['allowed_bookmakers'], ['Specific test book'])
                self.assertEqual(quote_policy.load_policy()['per_stake_cost_bps'], 15)
        self.assertEqual(quote_policy.CONFIG, original)
