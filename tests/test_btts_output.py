"""Regression tests for BTTS Yes/No display in human-readable predictions."""

from offline_test_case import OfflineQuotePolicyTestCase
from pathlib import Path
import tempfile
import unittest

import pandas as pd

from format_football_output import (
    build_match_summary,
    process_league,
    readable_predictions_frame,
)
from test_conservative_bet_filter import fixture


class BttsReportingTests(OfflineQuotePolicyTestCase):
    def test_readable_predictions_show_both_btts_outcomes_as_percentages(self):
        row = fixture()
        row["p_btts_yes"] = 0.61234
        row["p_btts_no"] = 0.38766
        output = readable_predictions_frame(pd.DataFrame([row]), {})
        self.assertEqual(output.iloc[0]["BTTS Yes"], "61.2%")
        self.assertEqual(output.iloc[0]["BTTS No"], "38.8%")
        self.assertEqual(
            list(output.columns).index("BTTS No"),
            list(output.columns).index("BTTS Yes") + 1,
        )
        self.assertEqual(row["p_btts_yes"], 0.61234)
        self.assertEqual(row["p_btts_no"], 0.38766)

    def test_missing_btts_probabilities_are_not_fabricated(self):
        row = fixture()
        row.pop("p_btts_yes")
        row.pop("p_btts_no", None)
        output = readable_predictions_frame(pd.DataFrame([row]), {})
        self.assertEqual(output.iloc[0]["BTTS Yes"], "—")
        self.assertEqual(output.iloc[0]["BTTS No"], "—")

    def test_match_narrative_explains_btts_probabilities(self):
        row = fixture()
        row["p_btts_yes"] = 0.67
        row["p_btts_no"] = 0.33
        summary = build_match_summary(row, [])
        self.assertIn("BTTS Yes (both teams score): 67.0%", summary)
        self.assertIn(
            "BTTS No (at least one team does not score): 33.0%", summary
        )

    def test_end_to_end_league_export_includes_btts_without_mutating_raw(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            raw = root / "raw"
            readable = root / "readable"
            raw.mkdir()
            readable.mkdir()

            source = raw / "EPL_predictions.csv"
            row = fixture()
            row["p_btts_yes"] = 0.584
            row["p_btts_no"] = 0.416
            pd.DataFrame([row]).to_csv(source, index=False)
            before = source.read_bytes()

            league, count = process_league(
                source, raw, readable, top_scorelines=2,
                include_technical=False,
            )
            self.assertEqual((league, count), ("EPL", 1))

            csv_report = pd.read_csv(
                readable / "EPL_predictions_readable.csv"
            )
            self.assertEqual(csv_report.iloc[0]["BTTS Yes"], "58.4%")
            self.assertEqual(csv_report.iloc[0]["BTTS No"], "41.6%")

            report = (readable / "EPL_report.md").read_text(
                encoding="utf-8"
            )
            self.assertIn("BTTS Yes (both teams score): 58.4%", report)
            self.assertIn(
                "BTTS No (at least one team does not score): 41.6%",
                report,
            )
            self.assertEqual(source.read_bytes(), before)


if __name__ == "__main__":
    unittest.main()
