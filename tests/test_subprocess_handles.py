"""Subprocess calls must not depend on inheriting this process's stdin/stderr.

On Windows, a test runner can leave the standard handles invalid; any
subprocess.run that inherits them then fails with WinError 6 before the child
starts. On Windows the child here points its standard input and error handles
at an invalid handle (as the runner does); elsewhere it closes fd 0. It then
drives every subprocess call in workflow_checks and refresh_training_data.
"""
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import textwrap
import unittest

REPO = Path(__file__).resolve().parents[1]

CHILD = textwrap.dedent(r'''
    import os, subprocess, sys
    from pathlib import Path
    if sys.platform == 'win32':
        import ctypes
        # A stale, non-zero standard handle: what subprocess would inherit.
        bogus = ctypes.c_void_p(0x7FF0)
        for std in (-10, -12):  # STD_INPUT_HANDLE, STD_ERROR_HANDLE
            assert ctypes.windll.kernel32.SetStdHandle(std, bogus)
    else:
        os.close(0)
    import refresh_training_data, workflow_checks
    repo = Path(sys.argv[1]); cli = sys.argv[2]
    sha = refresh_training_data.git(repo, 'rev-parse', 'HEAD').stdout.strip()
    assert len(sha) == 40, sha
    assert refresh_training_data.git(repo, 'rev-parse', 'no-such-ref', check=False).returncode != 0
    assert workflow_checks.changed_forecasts(repo, '0' * 40, sha) is False
    try:
        workflow_checks.capture_event(repo, repo, 'workflow_dispatch', 'f' * 40)
    except ValueError as error:
        assert 'differs from event SHA' in str(error), error
    else:
        raise AssertionError('capture_event accepted a mismatched SHA')
    workflow_checks.run_help(Path(cli).parent, Path(cli).name)
    try:
        workflow_checks.run_help(Path(cli).parent, 'missing_cli.py')
    except subprocess.CalledProcessError as error:
        assert error.returncode != 0
    else:
        raise AssertionError('run_help accepted a failing CLI')
    print('ok')
''')


class SubprocessHandleTests(unittest.TestCase):
    def test_calls_work_with_invalid_stdin_and_stderr(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            repo = root / 'repo'
            repo.mkdir()
            def git(*args):
                subprocess.run(['git', '-C', str(repo), *args], check=True, capture_output=True,
                               stdin=subprocess.DEVNULL)
            git('init'); git('config', 'user.name', 'Test'); git('config', 'user.email', 'test@example.test')
            (repo / 'code.py').write_text('pass\n'); git('add', '.'); git('commit', '-m', 'initial')
            cli = root / 'cli.py'
            cli.write_text("import sys\nsys.stderr.write('help warning\\n')\nprint('usage')\n")
            env = {**os.environ, 'PYTHONPATH': os.pathsep.join([str(REPO), os.environ.get('PYTHONPATH', '')])}
            result = subprocess.run([sys.executable, '-c', CHILD, str(repo), str(cli)], cwd=REPO, env=env,
                                    stdin=subprocess.DEVNULL, capture_output=True, text=True, timeout=120)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertEqual(result.stdout.strip(), 'ok')
            # run_help echoes the CLI's stderr, as the inherited handle used to.
            self.assertIn('help warning', result.stderr)


if __name__ == '__main__':
    unittest.main()
