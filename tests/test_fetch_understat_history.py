"""scripts/fetch_understat_history.py --replace-archive, offline (fake responses, no network)."""
import codecs
import importlib.util
import json
from pathlib import Path

import pytest

SPEC = importlib.util.spec_from_file_location(
    'fetch_understat_history', Path(__file__).resolve().parents[1] / 'scripts' / 'fetch_understat_history.py')
fetch = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(fetch)


def match(i, result=True):
    return {'id': str(i), 'isResult': result, 'h': {'title': 'A'}, 'a': {'title': 'B'},
            'goals': {'h': '1', 'a': '0'}, 'xG': {'h': '1.2', 'a': '0.4'}, 'datetime': f'2024-08-{i + 10:02d} 15:00:00'}


def page(values):
    encoded = codecs.encode(json.dumps(values), 'unicode_escape').decode('ascii').replace("'", "\\'")
    return f"<script>var datesData = JSON.parse('{encoded}');</script>"


class Response:
    def __init__(self, text, status=200):
        self.text, self.status_code, self.content, self.ok = text, status, text.encode(), status < 400


class Client:
    def __init__(self, pages):
        self.pages, self.urls = pages, []

    def get(self, url, **headers):
        self.urls.append(url)
        return Response(*self.pages[url]) if url in self.pages else Response('not found', 404)


def seed(tmp_path, results, matches):
    values = [match(i, i < results) for i in range(matches)]
    body = (json.dumps(values, indent=1) + '\n').encode()
    (tmp_path / 'EPL_2024.json').write_bytes(body)
    manifest = {'files': {'EPL_2024': {'league': 'EPL', 'season': '2024/25', 'source': 'internet_archive',
                                        'source_url': 'https://web.archive.org/x', 'archive_timestamp': '2025',
                                        'results': results, 'matches': matches, 'complete': results == matches,
                                        'file_sha256': 'old', 'fetched_at_utc': 'then'}},
                'missing': {}}
    (tmp_path / 'manifest.json').write_text(json.dumps(manifest))
    return body


def run(tmp_path, monkeypatch, pages):
    client = Client(pages)
    monkeypatch.setattr(fetch, 'Polite', lambda delay: client)
    fetch.main(['--leagues', 'EPL', '--seasons', '2024', '--output', str(tmp_path), '--replace-archive', '--no-archive'])
    return json.loads((tmp_path / 'manifest.json').read_text()), client


URL = 'https://understat.com/league/EPL/2024'


def test_direct_fetch_replaces_archive_copy_and_records_it(tmp_path, monkeypatch):
    seed(tmp_path, 2, 4)
    manifest, _ = run(tmp_path, monkeypatch, {URL: (page([match(i) for i in range(4)]),)})
    entry = manifest['files']['EPL_2024']
    assert entry['source'] == 'understat' and entry['complete'] and entry['results'] == 4
    assert entry['replaced']['source'] == 'internet_archive' and entry['replaced']['results'] == 2
    assert len(json.loads((tmp_path / 'EPL_2024.json').read_text())) == 4


@pytest.mark.parametrize('pages', [
    {URL: ('<html>We will come back soon</html>',)},  # maintenance page, HTTP 200
    {},                                                 # 404 everywhere
    {URL: (page([match(0)]),)},                         # fewer results than the archive copy
])
def test_failed_direct_fetch_keeps_archive_copy(tmp_path, monkeypatch, pages):
    body = seed(tmp_path, 2, 4)
    manifest, client = run(tmp_path, monkeypatch, pages)
    entry = manifest['files']['EPL_2024']
    assert entry['source'] == 'internet_archive' and entry['file_sha256'] == 'old'
    assert entry['direct_attempts']['attempts'] and 'EPL_2024' not in manifest['missing']
    assert (tmp_path / 'EPL_2024.json').read_bytes() == body
    assert not any('web.archive.org' in u for u in client.urls)


def test_coverage_lists_missing_seasons():
    rows = fetch.coverage({'files': {}, 'missing': {'Serie_A_2025': {}}})
    assert rows == [{'key': 'Serie_A_2025', 'league': 'SerieA', 'season': '2025/26', 'source': 'missing',
                     'results': 0, 'matches': 0, 'complete': False}]
