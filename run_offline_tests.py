"""Run regression checks independently of personal bookmaker configuration."""
import argparse
from pathlib import Path
import unittest
from unittest.mock import patch
import quote_policy


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--model-self-test', action='store_true')
    args = parser.parse_args(argv)
    repo = Path(__file__).resolve().parent
    with patch.object(quote_policy, 'CONFIG', repo/'tests'/'offline_quote_policy.json'):
        if args.model_self_test:
            from football_value_pipeline_v2_standalone import self_test
            self_test()
            return 0
        suite = unittest.defaultTestLoader.discover(str(repo/'tests'))
        result = unittest.TextTestRunner(verbosity=2).run(suite)
        return 0 if result.wasSuccessful() else 1


if __name__ == '__main__':
    raise SystemExit(main())
