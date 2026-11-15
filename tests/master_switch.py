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
