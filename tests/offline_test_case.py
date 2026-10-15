"""Test-scoped quote policy for every supported unittest/pytest entry point."""
from pathlib import Path
import unittest
from unittest.mock import patch

import quote_policy


class OfflineQuotePolicyTestCase(unittest.TestCase):
    """Keep policy injection inside the test lifecycle, including failures.

    Explicit per-test policy overrides still take precedence. The production
    policy file is never edited and the module setting is restored on exit.
    Overriding run also covers subclasses with their own setUp/tearDown.
    """

    def run(self, result=None):
        policy = Path(__file__).with_name('offline_quote_policy.json')
        with patch.object(quote_policy, 'CONFIG', policy):
            return super().run(result)
