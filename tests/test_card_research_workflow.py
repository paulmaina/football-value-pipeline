"""Offline checks of research priority and handled provider stops."""
import contextlib
import io
import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

import yaml

ROOT = Path(__file__).resolve().parents[1]


class CardResearchWorkflowTests(unittest.TestCase):
    def setUp(self):
        self.research = yaml.load((ROOT / '.github/workflows/card-bookings-research.yml').read_text(), Loader=yaml.BaseLoader)
        self.supplementary = yaml.load((ROOT / '.github/workflows/collect-api-football-data.yml').read_text(), Loader=yaml.BaseLoader)
        step = next(s for s in self.research['jobs']['collect']['steps'] if s.get('name') == 'Collect a batch; run the study once complete')
        self.code = step['run'].split("python - <<'PYTHON'\n", 1)[1].split('\nPYTHON', 1)[0]

    def run_batch(self, batch=None, returncode=0):
        result = subprocess.CompletedProcess([], returncode, '' if batch is None else json.dumps(batch), '')
        with tempfile.TemporaryDirectory() as tmp, patch.dict(os.environ, {'STUDY': tmp, 'GITHUB_STEP_SUMMARY': tmp + '/summary'}), patch('subprocess.run', return_value=result), contextlib.redirect_stdout(io.StringIO()) as output:
            code = 0
            try:
                exec(compile(self.code, '<workflow>', 'exec'), {})
            except SystemExit as exc:
                code = exc.code
            return code, output.getvalue()

    def test_research_runs_before_supplementary_without_concurrency_deadlock(self):
        self.assertIn('workflow_call', self.research['on'])
        self.assertNotIn('schedule', self.research['on'])
        jobs = self.supplementary['jobs']
        self.assertEqual(jobs['collect']['needs'], 'card-research')
        self.assertIn('always()', jobs['collect']['if'])
        self.assertNotEqual(self.supplementary['concurrency']['group'], self.research['concurrency']['group'])
        self.assertEqual(jobs['collect']['concurrency']['group'], self.research['concurrency']['group'])

    def test_zero_progress_provider_stop_fails_visibly(self):
        code, output = self.run_batch({'planned': 658, 'cached': 0, 'fetched': 0, 'stopped': 'provider allowance exhausted'})
        self.assertEqual(code, 1)
        self.assertIn('::error::', output)

    def test_partial_progress_warns_and_preserves_success(self):
        code, output = self.run_batch({'planned': 658, 'cached': 80, 'fetched': 80, 'stopped': 'explicit batch limit'})
        self.assertEqual(code, 0)
        self.assertIn('::warning::', output)

    def test_completed_or_already_completed_study_succeeds(self):
        self.assertEqual(self.run_batch()[0], 0)
        self.assertEqual(self.run_batch({'planned': 658, 'cached': 658, 'fetched': 0, 'stopped': None})[0], 0)

    def test_subprocess_failure_is_not_hidden(self):
        self.assertEqual(self.run_batch(returncode=2)[0], 2)

    def test_failure_checkpoints_and_hidden_artifacts_are_retained(self):
        steps = self.research['jobs']['collect']['steps']
        save = next(s for s in steps if s.get('uses', '').startswith('actions/cache/save'))
        self.assertIn('always()', save['if'])
        upload = next(s for s in steps if s.get('uses', '').startswith('actions/upload-artifact'))
        self.assertEqual(upload['with']['include-hidden-files'], 'true')
        self.assertNotIn('gh workflow disable', str(steps))
