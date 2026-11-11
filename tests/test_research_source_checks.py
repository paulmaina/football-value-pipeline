"""Research sources: an HTTP 200 placeholder page is not data.

The fixture is the research client's own cached observation of
https://understat.com/league/EPL/2026 from the 5 Nov 2026 forecast run (commit
3b8b70805, a GitHub runner): understat.com's maintenance page, served with HTTP 200
and recorded then as "available".
"""
import codecs
from datetime import datetime, timezone
import json
from pathlib import Path

import pandas as pd

import team_research as tr

FIXTURE = json.loads((Path(__file__).parent / 'fixtures' / 'understat_maintenance_cache_2026-11-05.json')
                     .read_text(encoding='utf-8'))
MAINTENANCE = FIXTURE['data']
URL = FIXTURE['url']
NOW = datetime(2026, 11, 11, 12, tzinfo=timezone.utc)


def dates_page(values):
    encoded = codecs.encode(json.dumps(values), 'unicode_escape').decode('ascii').replace("'", "\\'")
    return f"<html><script>var datesData = JSON.parse('{encoded}');</script></html>"


MATCH = {'id': '1', 'isResult': True, 'h': {'title': 'Arsenal'}, 'a': {'title': 'Chelsea'},
         'goals': {'h': '2', 'a': '1'}, 'xG': {'h': '1.8', 'a': '0.9'}, 'datetime': '2026-11-01 15:00:00'}


class Response:
    def __init__(self, text, status=200):
        self.text, self.status_code, self.content = text, status, text.encode('utf-8')

    def raise_for_status(self):
        if self.status_code >= 400:
            raise tr.requests.HTTPError(f'HTTP {self.status_code}')

    def json(self):
        return json.loads(self.text)


class Session:
    def __init__(self, text):
        self.text, self.calls = text, 0

    def get(self, url, **kwargs):
        self.calls += 1
        return Response(self.text)


def client(tmp_path, text):
    return tr.FreeSources(tmp_path, session=Session(text), clock=lambda: NOW)


def test_fixture_is_the_cached_maintenance_page_recorded_as_available():
    assert FIXTURE['status'] == 'available' and 'We will come back soon' in MAINTENANCE
    assert 'datesData' not in MAINTENANCE and tr.understat_rows(MAINTENANCE, URL, pd.Timestamp(NOW)) == []


def test_maintenance_page_with_http_200_is_unavailable(tmp_path):
    sources = client(tmp_path, MAINTENANCE)
    page = sources.get(URL, xml=True, check=tr.understat_check)
    assert page['status'] == 'unavailable' and page['reason'] == 'no match data (maintenance page)'
    assert 'data' not in page
    saved = json.loads(next((tmp_path / 'match_research').glob('*.json')).read_text(encoding='utf-8'))
    assert saved['status'] == 'unavailable' and 'data' not in saved
    # Failures keep the short retry TTL: ten minutes later the page is requested again.
    later = tr.FreeSources(tmp_path, session=sources.session, clock=lambda: NOW + pd.Timedelta(minutes=11))
    later.get(URL, xml=True, check=tr.understat_check)
    assert sources.session.calls == 2


def test_other_pages_without_match_data_are_unavailable(tmp_path):
    for text in ('<html>nothing here</html>', dates_page([]), "datesData = JSON.parse('not json')"):
        assert tr.understat_check(text) == 'no match data'


def test_page_with_match_data_stays_available_and_parses(tmp_path):
    text = dates_page([MATCH])
    page = client(tmp_path, text).get(URL, xml=True, check=tr.understat_check)
    assert page['status'] == 'available' and page['data'] == text and page.get('reason') is None
    rows = tr.understat_rows(page['data'], URL, pd.Timestamp(NOW))
    assert [(r['home'], r['away'], r['home_xg'], r['away_xg']) for r in rows] == [('Arsenal', 'Chelsea', 1.8, 0.9)]


def test_sources_without_a_check_are_unchanged(tmp_path):
    page = client(tmp_path, MAINTENANCE).get(URL, xml=True)
    assert page['status'] == 'available' and page['data'] == MAINTENANCE


def test_collect_fixture_records_understat_unavailable(tmp_path, monkeypatch):
    calls = []

    class Recorder:
        def clock(self):
            return NOW

        def get(self, url, xml=False, max_age_minutes=None, check=None):
            calls.append((url, check))
            if 'understat.com' in url:
                reason = check(MAINTENANCE) if check else None
                return {'url': url, 'observed_at_utc': NOW.isoformat(),
                        **({'status': 'unavailable', 'reason': reason} if reason else
                           {'status': 'available', 'data': MAINTENANCE})}
            return {'url': url, 'observed_at_utc': NOW.isoformat(), 'status': 'unavailable', 'reason': 'offline'}

    row = {'league': 'Premier League', 'home_team': 'Arsenal', 'away_team': 'Chelsea',
           'kickoff_utc': '2026-11-14T15:00:00+00:00', 'date': '2026-11-14'}
    evidence = tr.collect_fixture(row, Recorder())
    understat = [s for s in evidence['sources'] if 'understat.com' in s['url']]
    assert [s['url'].rsplit('/', 1)[-1] for s in understat] == ['2026', '2025']
    assert all(s['status'] == 'unavailable' and s['reason'] == 'no match data (maintenance page)' for s in understat)
    assert all(c is tr.understat_check for u, c in calls if 'understat.com' in u)
    assert all(c is None for u, c in calls if 'understat.com' not in u)
