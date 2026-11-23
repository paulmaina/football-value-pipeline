"""A forecast on a stale research fit is flagged at the top of every output (Paul, 23 Nov 2026).

The 16 Nov 2026 refit was missed and the warning lived only in each pick's coverage text and the activity log for
a week. Now: the run summary JSON (stale_fit_warning), the GitHub run summary (first line, plus a warning
annotation; the repo has no other notification set up), the shortlist report (under its title), the master
section of that report (under its heading) and the workbook's master tab (a red line above the list).
"""
from __future__ import annotations

import io
import json
from contextlib import redirect_stdout
from pathlib import Path
import tempfile
import unittest
from unittest import mock

import model_activity as ma


def row(fit='c6_fit', stale=True, origin='2026-11-02', expected='2026-11-16'):
    return {'team_research_json': json.dumps({fit: {'origin': origin, 'expected_origin': expected, 'stale': stale}})}


class StaleWarningTests(unittest.TestCase):
    def test_warning_names_each_stale_fit_and_none_when_current(self):
        warning = ma.stale_warning([row(), row(), row(stale=False, origin='2026-11-16'),
                                    row('ce3n_fit'), {'team_research_json': None}])
        self.assertTrue(warning['text'].startswith('STALE RESEARCH FIT: 2 of 3 forecasts used a stale C6 fit '
                                                   '(window from 2026-11-02; the window for this day opened 2026-11-16)'))
        self.assertIn('1 of 1 forecasts used a stale CE3n fit', warning['text'])
        self.assertEqual(set(warning['fits']), {'C6', 'CE3n'})
        self.assertIsNone(ma.stale_warning([row(stale=False, origin='2026-11-16')]))
        self.assertIsNone(ma.stale_warning([]))

    def test_run_outcome_carries_it_and_the_run_summary_opens_with_it(self):
        import csv
        from football_value_pipeline_v2_standalone import run_outcome
        import publish_scheduled_forecasts as publisher
        with tempfile.TemporaryDirectory() as tmp:
            with (Path(tmp) / 'all_leagues_predictions.csv').open('w', encoding='utf-8', newline='') as handle:
                writer = csv.DictWriter(handle, ['league', 'odds_source', 'team_research_json'])
                writer.writeheader()
                writer.writerow({'league': 'Premier League', 'odds_source': 'The Odds API', **row()})
            outcome = run_outcome(Path(tmp), 3)
        self.assertTrue(outcome['stale_fit_warning'].startswith('STALE RESEARCH FIT: 1 of 1'))
        written = []
        out = io.StringIO()
        with mock.patch.object(publisher.odds_api_usage, 'write_step_summary', written.append), redirect_stdout(out):
            publisher.report(outcome, publisher.usage_record(outcome, 0))
        self.assertTrue(written[0].startswith('## ⚠️ STALE RESEARCH FIT'))
        self.assertIn('::warning title=Stale research fit::STALE RESEARCH FIT', out.getvalue())
        current = dict(outcome)
        current.pop('stale_fit_warning')
        written.clear()
        with mock.patch.object(publisher.odds_api_usage, 'write_step_summary', written.append), redirect_stdout(out):
            publisher.report(current, publisher.usage_record(current, 0))
        self.assertNotIn('STALE', written[0])

    def test_report_banners(self):
        import format_football_output as ff
        summary = {'stale_fit_warning': ma.stale_warning([row()])}
        self.assertEqual(ff.stale_banner(summary)[1][:20], '> **⚠️ STALE RESEARC')
        self.assertEqual(ff.stale_banner({}), [])
        with mock.patch.object(ff, '_master_section', return_value=['', '## Master shortlist', '', 'table']):
            lines = ff.master_section(summary, None, Path('.'))
        self.assertEqual(lines[1], '## Master shortlist')
        self.assertTrue(lines[3].startswith('> **⚠️ STALE RESEARCH FIT'))
        with mock.patch.object(ff, '_master_section', return_value=['', '## Master shortlist', '', 'table']):
            self.assertEqual(ff.master_section({}, None, Path('.')), ['', '## Master shortlist', '', 'table'])

    def test_workbook_master_tab_puts_it_above_the_list(self):
        import openpyxl
        import predictions_workbook as pw
        with tempfile.TemporaryDirectory() as tmp:
            raw = Path(tmp) / 'raw'
            raw.mkdir()
            for stale, name in ((True, 'stale.xlsx'), (False, 'current.xlsx')):
                summary = {'generated_at_utc': '2026-11-23T06:15:00+00:00',
                           **({'stale_fit_warning': ma.stale_warning([row()])} if stale else {})}
                (raw / 'conservative_bet_summary.json').write_text(json.dumps(summary), encoding='utf-8')
                pw.write([], Path(tmp) / name, input_dir=raw)
            stale_sheet = openpyxl.load_workbook(Path(tmp) / 'stale.xlsx')[pw.MASTER_TAB]
            current_sheet = openpyxl.load_workbook(Path(tmp) / 'current.xlsx')[pw.MASTER_TAB]
        self.assertTrue(str(stale_sheet['A4'].value).startswith('⚠️ STALE RESEARCH FIT'))
        self.assertEqual(stale_sheet['A6'].value, 'Rank')
        self.assertEqual(current_sheet['A4'].value, 'Rank')


class RedJobTests(unittest.TestCase):
    """After publishing, a stale fit makes the forecast workflow's last step fail (Paul, 23 Nov 2026)."""

    def test_publisher_flags_the_workflow_only_after_publishing(self):
        import publish_scheduled_forecasts as publisher
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / 'out'
            self.assertTrue(publisher.stale_alert({'stale_fit_warning': 'STALE RESEARCH FIT: 1 of 1\nforecasts'}, output))
            self.assertFalse(publisher.stale_alert({'status': 'FORECASTS_PRODUCED'}, output))
            self.assertFalse(publisher.stale_alert(None, output))
            self.assertEqual(output.read_text(encoding='utf-8').splitlines(),
                             ['stale_fit=true', 'stale_fit_warning=STALE RESEARCH FIT: 1 of 1 forecasts',
                              'stale_fit=false', 'stale_fit=false'])
            env = {'GITHUB_OUTPUT': str(output)}
            for outcome, code in (({'stale_fit_warning': 'STALE'}, 0), ({}, 0)):
                with mock.patch.object(publisher, 'publish', return_value=outcome), mock.patch.dict('os.environ', env):
                    self.assertEqual(publisher.main([]), code)  # the publisher itself still succeeds
            stopped = publisher.ForecastStopped('credits exhausted')
            with mock.patch.object(publisher, 'publish', side_effect=stopped), mock.patch.object(publisher, 'stale_alert') as alert,                     redirect_stdout(io.StringIO()):
                self.assertEqual(publisher.main([]), 1)
            alert.assert_not_called()

    def test_workflow_fails_only_in_a_last_step_after_publishing(self):
        import yaml
        root = Path(__file__).resolve().parents[1]
        flow = yaml.load((root / '.github/workflows/scheduled-forecasts.yml').read_text(encoding='utf-8'),
                         Loader=yaml.BaseLoader)
        steps = flow['jobs']['collect']['steps']
        names = [s.get('name') for s in steps]
        publish = names.index('Generate, capture, grade and publish on latest main')
        fail = names.index('Fail the run when a live forecast used a stale research fit')
        self.assertEqual(fail, len(steps) - 1)
        self.assertGreater(fail, publish)
        self.assertEqual(steps[publish]['id'], 'publish')
        self.assertEqual(steps[fail]['if'], "steps.publish.outputs.stale_fit == 'true'")
        self.assertIn('exit 1', steps[fail]['run'])

if __name__ == '__main__':
    unittest.main()
