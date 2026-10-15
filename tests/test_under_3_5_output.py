"""Regression tests for the Under 3.5 probability in prediction reports."""

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


class UnderThreePointFiveReportingTests(OfflineQuotePolicyTestCase):
    def test_readable_predictions_include_under_three_point_five(self):
        row = fixture()
        row["p_under_3_5"] = 0.79123
        frame = readable_predictions_frame(pd.DataFrame([row]), {})
        self.assertIn("Under 3.5", frame.columns)
        self.assertEqual(frame.iloc[0]["Under 3.5"], "79.1%")
        self.assertEqual(
            list(frame.columns).index("Under 3.5"),
            list(frame.columns).index("Over 3.5") + 1,
        )
        # Formatter must not alter the raw probabilities.
        self.assertEqual(row["p_under_3_5"], 0.79123)

    def test_missing_under_three_point_five_shows_unavailable(self):
        row = fixture()
        row.pop("p_under_3_5")
        frame = readable_predictions_frame(pd.DataFrame([row]), {})
        self.assertEqual(frame.iloc[0]["Under 3.5"], "—")

    def test_match_narrative_includes_correct_market_probability(self):
        row = fixture()
        row["p_under_3_5"] = 0.8325
        summary = build_match_summary(row, [])
        self.assertIn("Under 3.5 goals: 83.2%", summary)

    def test_league_export_writes_csv_and_markdown_without_mutating_raw(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            raw = root / "raw"
            readable = root / "readable"
            raw.mkdir()
            readable.mkdir()

            source = raw / "EPL_predictions.csv"
            row = fixture()
            row["p_under_3_5"] = 0.824
            pd.DataFrame([row]).to_csv(source, index=False)
            original_bytes = source.read_bytes()

            league, count = process_league(
                source, raw, readable, top_scorelines=2,
                include_technical=False,
            )
            self.assertEqual((league, count), ("EPL", 1))
            csv_out = pd.read_csv(readable / "EPL_predictions_readable.csv")
            self.assertEqual(csv_out.iloc[0]["Under 3.5"], "82.4%")
            report = (readable / "EPL_report.md").read_text(encoding="utf-8")
            self.assertIn("Under 3.5 goals: 82.4%", report)
            self.assertEqual(source.read_bytes(), original_bytes)


if __name__ == "__main__":
    unittest.main()
