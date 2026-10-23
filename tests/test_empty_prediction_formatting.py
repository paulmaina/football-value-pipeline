"""A league without fixtures must not stop scheduled report publication."""

from pathlib import Path
import tempfile
import unittest

import pandas as pd

from offline_test_case import OfflineQuotePolicyTestCase
from format_football_output import main, process_combined_file, process_league
from test_conservative_bet_filter import fixture


class EmptyPredictionFormattingTests(OfflineQuotePolicyTestCase):
    def test_empty_league_files_produce_no_fixture_report(self):
        for contents in ("", "\n", "  \n\t\n", "date,home_team,away_team\n"):
            with self.subTest(contents=contents), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                source = root / "UCL_predictions.csv"
                source.write_text(contents, encoding="utf-8")
                original = source.read_bytes()
                self.assertEqual(process_league(source, root, root, 2, False), ("UCL", 0))
                self.assertIn("contains no fixtures", (root / "UCL_report.md").read_text())
                self.assertEqual(source.read_bytes(), original)

    def test_empty_combined_file_has_no_groups(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / "all_leagues_predictions.csv"
            source.write_text("\n", encoding="utf-8")
            self.assertEqual(process_combined_file(source, root, root, 2, False), [])

    def test_formatter_continues_past_empty_league_to_populated_league(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            raw = root / "raw"
            raw.mkdir()
            (raw / "UCL_predictions.csv").write_text("\n", encoding="utf-8")
            pd.DataFrame([fixture()]).to_csv(raw / "UEL_predictions.csv", index=False)
            originals = {p: p.read_bytes() for p in raw.iterdir()}
            self.assertEqual(main(["--root-dir", str(root)]), 0)
            readable = root / "readable"
            self.assertIn("contains no fixtures", (readable / "UCL_report.md").read_text())
            self.assertEqual(len(pd.read_csv(readable / "UEL_predictions_readable.csv")), 1)
            for path, contents in originals.items():
                self.assertEqual(path.read_bytes(), contents)

    def test_malformed_csv_still_raises(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / "UCL_predictions.csv"
            source.write_text('date,home_team\n"unterminated', encoding="utf-8")
            with self.assertRaises(pd.errors.ParserError):
                process_league(source, root, root, 2, False)


if __name__ == "__main__":
    unittest.main()
