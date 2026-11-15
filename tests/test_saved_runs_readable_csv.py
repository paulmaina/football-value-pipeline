"""Reporting-only guard for the Excel redesign: every readable CSV the formatter writes for the 29 saved live runs
(27 Oct – 8 Nov 2026) is byte-identical to main's, line endings aside.

tests/fixtures/saved_runs_readable_csv_digests_main.json holds main's CSV digests (main at 0986895, formatted with
scripts/format_saved_runs.py --code-root <main> and written with --digests), CRLF normalised to LF because pandas
writes os.linesep. The workbooks are not compared: they are what changed. Main and branch were also compared byte
for byte on one machine (scripts/format_saved_runs.py --compare): 556 of 556 CSVs identical."""
from __future__ import annotations

import contextlib
import importlib.util
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest import mock

import quote_policy

REPO = Path(__file__).resolve().parents[1]
FIXTURE = Path(__file__).with_name('fixtures') / 'saved_runs_readable_csv_digests_main.json'
START, END = '2026-10-27', '2026-11-09'


def script():
    spec = importlib.util.spec_from_file_location('format_saved_runs', REPO / 'scripts' / 'format_saved_runs.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class SavedRunsReadableCsvTests(unittest.TestCase):
    def test_every_readable_csv_of_the_saved_runs_matches_main(self):
        import format_football_output as formatter
        tool = script()
        expected = json.loads(FIXTURE.read_text(encoding='utf-8'))
        runs = tool.runs(REPO, START, END)
        self.assertEqual(len(runs), 29)
        self.assertEqual({d.name for _, d in runs}, set(expected))
        compared = 0
        with tempfile.TemporaryDirectory() as tmp, \
                mock.patch.object(quote_policy, 'CONFIG', REPO / 'shortlist_quote_policy.json'):
            tmp = Path(tmp)
            for _, snapshot in runs:
                raw = tool.bundle(snapshot, tmp / 'bundles' / snapshot.name)
                out = tmp / 'runs' / snapshot.name
                with contextlib.redirect_stdout(io.StringIO()):
                    self.assertEqual(formatter.main(['--root-dir', str(tmp / 'root'), '--input-dir', str(raw),
                                                     '--output-dir', str(out)]), 0)
                actual = {p.name: tool.normalised_digest(p.read_bytes()) for p in sorted(out.glob('*.csv'))}
                self.assertEqual(actual, expected[snapshot.name], snapshot.name)
                self.assertTrue((out / 'league_predictions.xlsx').exists())
                compared += len(actual)
        self.assertEqual(compared, 556)


if __name__ == '__main__':
    unittest.main()
