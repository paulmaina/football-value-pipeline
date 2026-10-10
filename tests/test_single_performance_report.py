"""Regression tests for the single forward-performance report."""
import csv
import json
from pathlib import Path
import tempfile
import unittest

from format_football_output import main


def save_csv(path, rows):
    with path.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


class SinglePerformanceReportTests(unittest.TestCase):
    def prepare(self, base, graded=False):
        root = base / "football_output_v2"
        raw = root / "raw"
        perf = root / "performance"
        readable = root / "readable"
        raw.mkdir(parents=True)
        perf.mkdir()
        readable.mkdir()
        rows = [
            {
                "status": "WON" if graded and i % 3 else
                          ("LOST" if graded else "PENDING_KICKOFF_OR_FINAL_SCORE"),
                "market": "Under 3.5",
                "selection_tier": "STRICT" if i % 2 else "PROVISIONAL",
                "predicted_probability": "0.75",
                "unit_profit": "0.5" if graded and i % 3 else
                               ("-1" if graded else ""),
            }
            for i in range(35 if graded else 10)
        ]
        preds = [{
            "status": "GRADED" if graded else "PENDING_KICKOFF_OR_FINAL_SCORE",
            "one_x_two_brier": "0.4" if graded else "",
            "one_x_two_correct": "1" if graded else "",
            "over_1_5_correct": "1" if graded else "",
            "under_3_5_correct": "1" if graded else "",
            "btts_yes_correct": "0" if graded else "",
        }]
        save_csv(perf / "shortlist_grades.csv", rows)
        save_csv(perf / "prediction_grades.csv", preds)
        (perf / "metrics.json").write_text(json.dumps({
            "status": "ALL_GRADED" if graded else "AWAITING_VERIFIED_RESULTS",
            "calibration": [],
            "provider_errors": {},
        }), encoding="utf-8")
        (readable / "EPL_report.md").write_text("old generated file")
        (readable / "performance_dashboard.md").write_text("old verbose dashboard")
        (readable / "performance_by_market_readable.csv").write_text("old market export")
        (readable / "custom_notes.txt").write_text("user-managed; leave unchanged")
        return root, perf, readable

    def test_default_generates_only_consolidated_report(self):
        with tempfile.TemporaryDirectory() as folder:
            root, perf, readable = self.prepare(Path(folder))
            before = {name: (perf / name).read_bytes()
                      for name in ("shortlist_grades.csv", "prediction_grades.csv", "metrics.json")}
            self.assertEqual(main(["--root-dir", str(root)]), 0)
            self.assertEqual(sorted(p.name for p in readable.iterdir()),
                             ["custom_notes.txt", "performance_report.md"])
            report = (readable / "performance_report.md").read_text()
            self.assertIn("NOT EVALUABLE YET", report)
            self.assertIn("10", report)
            self.assertIn("Under 3.5", report)
            self.assertIn("PROVISIONAL", report)
            self.assertIn("STRICT", report)
            self.assertNotIn("## Weekly match-by-match grades", report)
            self.assertEqual(before, {name: (perf / name).read_bytes() for name in before})
            self.assertEqual(main(["--root-dir", str(root)]), 0)
            self.assertEqual(sorted(p.name for p in readable.iterdir()),
                             ["custom_notes.txt", "performance_report.md"])

    def test_graded_report_uses_settled_denominators_and_brier(self):
        with tempfile.TemporaryDirectory() as folder:
            root, _, readable = self.prepare(Path(folder), graded=True)
            self.assertEqual(main(["--root-dir", str(root)]), 0)
            report = (readable / "performance_report.md").read_text()
            self.assertIn("PRELIMINARY", report)
            self.assertIn("35", report)
            self.assertIn("1X2 multiclass Brier (lower is better):** 0.4000", report)
            self.assertIn("Simulated ROI", report)
            self.assertIn("Top priorities for model improvement", report)


if __name__ == "__main__":
    unittest.main()
