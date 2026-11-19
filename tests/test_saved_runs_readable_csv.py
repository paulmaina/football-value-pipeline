"""Reporting-only guard for the Excel redesign: every readable CSV the formatter writes for the 29 saved live runs
(27 Oct – 8 Nov 2026) matches main's.

tests/fixtures/saved_runs_readable_csv_main.zip holds main's 556 CSVs (main at 0986895, formatted with
scripts/format_saved_runs.py --code-root <main>), line endings normalised to LF because pandas writes os.linesep.
Each CSV must be byte-identical after that normalisation, or else cell-for-cell identical with numbers equal to
the last bits (relative 1e-12): some older lists carry full-precision floats whose last digit depends on the CPU's
math kernels (the same reason tests/master_golden.py never compares raw digests across machines). On one machine
main and the branch were compared byte for byte (scripts/format_saved_runs.py --compare): 556 of 556 identical.
The workbooks are not compared: they are what changed.

Since the readable league files show the research and cagey views (readable_views.py, 19 Nov 2026), the league
CSVs (*_predictions_readable.csv, *_scorelines_readable.csv: 466 of the 556) are written and named as before but
their contents are what changed, so they are not compared here; tests/test_readable_views.py checks them against
the run's shortlist and master files. The other 90 (value shortlist, cagey tier, master and bet365 lists) must
still match main's."""
from __future__ import annotations

import contextlib
import csv
import importlib.util
import io
import math
from pathlib import Path
import tempfile
import unittest
from unittest import mock
import zipfile

import quote_policy

REPO = Path(__file__).resolve().parents[1]
FIXTURE = Path(__file__).with_name('fixtures') / 'saved_runs_readable_csv_main.zip'
START, END = '2026-10-27', '2026-11-09'
LEAGUE_FILES = ('_predictions_readable.csv', '_scorelines_readable.csv')  # changed by design (see the docstring)


def script():
    spec = importlib.util.spec_from_file_location('format_saved_runs', REPO / 'scripts' / 'format_saved_runs.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def differences(got: bytes, want: bytes, label: str) -> list:
    """[] when the CSVs agree: identical text, or identical cells with numbers equal to the last bits."""
    got = got.replace(b'\r\n', b'\n')
    if got == want:
        return []
    rows = lambda data: list(csv.reader(io.StringIO(data.decode('utf-8-sig'))))
    a, b = rows(got), rows(want)
    if len(a) != len(b):
        return [f'{label}: {len(a)} rows vs {len(b)}']
    out = []
    for r, (ra, rb) in enumerate(zip(a, b)):
        if len(ra) != len(rb):
            out.append(f'{label} row {r}: {len(ra)} cells vs {len(rb)}')
            continue
        for c, (x, y) in enumerate(zip(ra, rb)):
            if x == y:
                continue
            try:
                fx, fy = float(x), float(y)
            except ValueError:
                out.append(f'{label} row {r} col {c}: {x!r} vs {y!r}')
                continue
            if not math.isclose(fx, fy, rel_tol=1e-12, abs_tol=1e-15):
                out.append(f'{label} row {r} col {c}: {x!r} vs {y!r}')
    return out


class SavedRunsReadableCsvTests(unittest.TestCase):
    def test_every_readable_csv_of_the_saved_runs_matches_main(self):
        import format_football_output as formatter
        tool = script()
        with zipfile.ZipFile(FIXTURE) as archive:
            expected = {}
            for name in archive.namelist():
                run, file = name.split('/')
                expected.setdefault(run, {})[file] = archive.read(name)
        runs = tool.runs(REPO, START, END)
        self.assertEqual(len(runs), 29)
        self.assertEqual({d.name for _, d in runs}, set(expected))
        problems, compared = [], 0
        with tempfile.TemporaryDirectory() as tmp, \
                mock.patch.object(quote_policy, 'CONFIG', REPO / 'shortlist_quote_policy.json'):
            tmp = Path(tmp)
            for _, snapshot in runs:
                raw = tool.bundle(snapshot, tmp / 'bundles' / snapshot.name)
                out = tmp / 'runs' / snapshot.name
                with contextlib.redirect_stdout(io.StringIO()):
                    self.assertEqual(formatter.main(['--root-dir', str(tmp / 'root'), '--input-dir', str(raw),
                                                     '--output-dir', str(out)]), 0)
                written = {p.name: p.read_bytes() for p in sorted(out.glob('*.csv'))}
                self.assertEqual(sorted(written), sorted(expected[snapshot.name]), snapshot.name)
                for name, data in written.items():
                    if name.endswith(LEAGUE_FILES):
                        continue
                    problems += differences(data, expected[snapshot.name][name], f'{snapshot.name}/{name}')
                    compared += 1
                self.assertTrue((out / 'league_predictions.xlsx').exists())
        self.assertEqual(problems, [])
        self.assertEqual(compared, 90)

    def test_comparison_allows_only_last_bit_float_noise(self):
        want = b'a,b\nx,0.2493245851022771\n'
        self.assertEqual(differences(b'a,b\r\nx,0.2493245851022771\r\n', want, 'f'), [])
        self.assertEqual(differences(b'a,b\nx,0.24932458510227713\n', want, 'f'), [])
        self.assertTrue(differences(b'a,b\nx,0.2493245851\n', want, 'f'))
        self.assertTrue(differences(b'a,b\ny,0.2493245851022771\n', want, 'f'))
        self.assertTrue(differences(b'a,b\nx,0.2493245851022771\nz,1\n', want, 'f'))


if __name__ == '__main__':
    unittest.main()
