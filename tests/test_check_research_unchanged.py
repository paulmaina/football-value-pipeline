"""scripts/check_research_unchanged.py: the base team_research loads from a ref with the files it reads beside itself."""
import tempfile
import unittest
from pathlib import Path

import team_research
from scripts import check_research_unchanged as check


class LoadBaseTests(unittest.TestCase):
    def test_base_module_reads_the_refs_research_config(self):
        with tempfile.TemporaryDirectory() as tmp:
            base = check.load_base('HEAD', Path(tmp))
            # research_config.json (since PR #178) and bbs_team_aliases.json come from the same ref.
            self.assertTrue((Path(tmp) / 'research_config.json').is_file())
            self.assertTrue((Path(tmp) / 'bbs_team_aliases.json').is_file())
            self.assertEqual(Path(base.RESEARCH_CONFIG).parent, Path(tmp))
            self.assertEqual(base.configured_live(), team_research.configured_live())
            self.assertEqual(base.understat_live(), team_research.understat_live())


if __name__ == '__main__':
    unittest.main()
