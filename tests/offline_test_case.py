"""Test-scoped quote policy for every supported unittest/pytest entry point."""
from pathlib import Path
import unittest
from unittest.mock import patch

import odds_provider
import quote_policy

# No such file: the odds-provider switch reads a missing file as off, so no test client routes to pinnapi or
# pinnodds whatever the committed switch says (tests that exercise routing attach their own router).
NO_ODDS_PROVIDER_CONFIG = Path(__file__).with_name('odds_provider_config.offline-absent.json')


class OfflineQuotePolicyTestCase(unittest.TestCase):
    """Keep policy injection inside the test lifecycle, including failures.

    Explicit per-test policy overrides still take precedence. The production
    policy file is never edited and the module setting is restored on exit.
    Overriding run also covers subclasses with their own setUp/tearDown.
    The odds-provider switch is held off the same way (NO_ODDS_PROVIDER_CONFIG).
    """

    def run(self, result=None):
        policy = Path(__file__).with_name('offline_quote_policy.json')
        with patch.object(quote_policy, 'CONFIG', policy),                 patch.object(odds_provider, 'CONFIG', NO_ODDS_PROVIDER_CONFIG):
            return super().run(result)
