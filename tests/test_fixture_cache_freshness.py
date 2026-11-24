"""Fixture caches are fresh only by evidence from this process or the fetch time stored in them.

A git checkout sets every committed cache file's mtime to "now", so mtime cannot show when a response was
fetched. On 24 Nov 2026 a committed 22 Nov football-data.org copy listing no UCL matches passed as fresh
and the run had no UCL fixtures.
"""
from offline_test_case import OfflineQuotePolicyTestCase
from datetime import datetime, timedelta, timezone
import json
import os
from pathlib import Path
import tempfile
from unittest.mock import Mock

import requests

from football_value_pipeline_v2_standalone import LEAGUES, FootballDataOrg, FootballDataUK

NOW = datetime(2026, 11, 24, 6, 45, tzinfo=timezone.utc)
UCL = LEAGUES['UCL']


def response(content: bytes):
    result = requests.Response()
    result.status_code = 200
    result._content = content
    return result


def fdorg_payload(*matches):
    return {'resultSet': {'count': len(matches)}, 'matches': [
        {'id': i, 'utcDate': kickoff, 'status': 'TIMED',
         'homeTeam': {'name': home}, 'awayTeam': {'name': away}}
        for i, (kickoff, home, away) in enumerate(matches, start=1)]}


LIVE = fdorg_payload(('2026-11-24T20:00:00Z', 'Arsenal FC', 'Borussia Dortmund'))


class FootballDataOrgFixtureCacheTests(OfflineQuotePolicyTestCase):
    def setUp(self):
        super().setUp()
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.cache = Path(self.tmp.name)
        self.provider = FootballDataOrg('offline-test', cache_dir=self.cache)
        self.get = Mock(return_value=response(json.dumps(LIVE).encode('utf-8')))
        self.provider.http.session.get = self.get
        self.path = self.cache / 'fdorg_fixtures_UCL.json'

    def fixtures(self, now=NOW):
        return self.provider.fixtures(UCL, 3, now)

    def test_checked_out_copy_without_fetch_time_is_refetched(self):
        # The committed format before this fix: a bare payload whose mtime a checkout just reset.
        self.path.write_text(json.dumps(fdorg_payload()), encoding='utf-8')
        os.utime(self.path, None)
        frame = self.fixtures()
        self.assertEqual(self.get.call_count, 1)
        self.assertEqual(frame['HomeTeam'].tolist(), ['Arsenal FC'])

    def test_copy_for_another_window_is_refetched(self):
        self.fixtures(NOW - timedelta(days=2))
        frame = self.fixtures()
        self.assertEqual(self.get.call_count, 2)
        self.assertEqual(len(frame), 1)

    def test_old_fetch_time_is_refetched_despite_new_mtime(self):
        self.fixtures()
        stored = json.loads(self.path.read_text(encoding='utf-8'))
        stored['fetched_at_utc'] = (datetime.now(timezone.utc) - timedelta(hours=1)).isoformat()
        self.path.write_text(json.dumps(stored), encoding='utf-8')
        os.utime(self.path, None)
        self.fixtures()
        self.assertEqual(self.get.call_count, 2)

    def test_fresh_copy_for_the_same_window_makes_no_request(self):
        now = datetime.now(timezone.utc)
        first = self.fixtures(now)
        second = self.fixtures(now)
        self.assertEqual(self.get.call_count, 1)
        self.assertEqual(first.to_dict('records'), second.to_dict('records'))
        stored = json.loads(self.path.read_text(encoding='utf-8'))
        today = now.date()
        self.assertEqual(stored['request'], {'dateFrom': today.isoformat(),
                                             'dateTo': (today + timedelta(days=3)).isoformat()})


class FootballDataUKFixtureSnapshotTests(OfflineQuotePolicyTestCase):
    def setUp(self):
        super().setUp()
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.cache = Path(self.tmp.name)
        self.source = FootballDataUK(cache_dir=self.cache)
        live = 'Div,Date,HomeTeam,AwayTeam\nE0,28/11/2026,Arsenal,Chelsea\nSP1,28/11/2026,Getafe,Celta\n'
        self.get = Mock(return_value=response(live.encode('utf-8')))
        self.source.http.session.get = self.get

    def test_checked_out_snapshot_is_downloaded_once_per_process(self):
        stale = self.cache / 'fixtures.csv'
        stale.write_text('Div,Date,HomeTeam,AwayTeam\nE0,06/11/2026,Everton,Coventry\n', encoding='utf-8')
        os.utime(stale, None)
        epl = self.source.fixtures(LEAGUES['EPL'], 5, NOW)
        laliga = self.source.fixtures(LEAGUES['LaLiga'], 5, NOW)
        self.assertEqual(self.get.call_count, 1)  # one download serves every league in the run
        self.assertEqual(epl['HomeTeam'].tolist(), ['Arsenal'])
        self.assertEqual(laliga['HomeTeam'].tolist(), ['Getafe'])
