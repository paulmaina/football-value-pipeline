"""Test helper: the master release switch (master_shortlist_config.json, live).

Tests of the pre-release behaviour (the old master writing master_shortlist.csv, the new master in shadow) run under
live "old", which is exactly the rollback state: the committed config with only its `live` field changed.
"""
from __future__ import annotations

import contextlib
import json
import tempfile
from pathlib import Path
from unittest import mock

import master_shortlist as ms


@contextlib.contextmanager
def switched(live: str):
    """The committed master_shortlist_config.json with only its `live` switch set to `live`."""
    config = json.loads(ms.CONFIG.read_text(encoding='utf-8'))
    config['live'] = live
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / 'master_shortlist_config.json'
        path.write_text(json.dumps(config), encoding='utf-8')
        with mock.patch.object(ms, 'CONFIG', path):
            yield


class OldMasterLive:
    """Mixin for TestCase classes about the pre-release behaviour: every test runs under live "old"."""

    def setUp(self):
        super().setUp()
        self._master_switch = switched('old')
        self._master_switch.__enter__()
        self.addCleanup(self._master_switch.__exit__, None, None, None)


class NewMasterLive:
    """Mixin for TestCase classes about the 14 Nov 2026 release (the new master live, the old master in shadow): every
    test runs under live "new", the state before the strong-team release (23 Nov 2026) and its rollback state."""

    def setUp(self):
        super().setUp()
        self._master_switch = switched('new')
        self._master_switch.__enter__()
        self.addCleanup(self._master_switch.__exit__, None, None, None)


_MODULE_SWITCHES = []


def pin_module(live: str) -> None:
    """setUpModule helper: the whole test module runs under live `live` (undo with unpin_module in tearDownModule).
    Classes inside may still switch again (e.g. OldMasterLive)."""
    context = switched(live)
    context.__enter__()
    _MODULE_SWITCHES.append(context)


def unpin_module() -> None:
    if _MODULE_SWITCHES:
        _MODULE_SWITCHES.pop().__exit__(None, None, None)
