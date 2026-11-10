"""Download historical Understat match xG for the five big leagues into .football_cache/understat.

One file per league and season (`{slug}_{year}.json`, Understat's own match list:
id, isResult, h/a teams, goals, xG, datetime) plus `manifest.json` with, for every
file, the source URL actually fetched, the original Understat URL, the fetch time,
the HTTP status and the sha256 of both the raw response and the saved file.

Sources, in order:
  1. understat.com itself: the league page (`datesData` embedded, the pre-2025
     layout the live parser reads) or its data endpoint (`getLeagueData`).
  2. The Internet Archive's capture of that same Understat page (raw `id_` copy),
     used only when understat.com does not serve the data (for example its
     maintenance page, served for every URL since 3 Nov 2026). The newest capture
     whose season is complete is taken; otherwise the capture with most results,
     and the manifest marks the season partial.

Understat publishes no API terms and no robots.txt rules (robots.txt serves the
maintenance page). The script is polite anyway: one request at a time, at least
`--delay` seconds (default 6) between requests to the same host, an honest
User-Agent, a backoff on 429/5xx and connection errors, and seasons already in the
manifest are never fetched again unless `--refresh` is given.

The files carry no odds. Nothing here executes page JavaScript: the data is read
with a regular expression and json.

    python scripts/fetch_understat_history.py                      # all leagues, 2021 to current season
    python scripts/fetch_understat_history.py --leagues EPL --seasons 2023
"""
from __future__ import annotations

import argparse
import codecs
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import time
from urllib.parse import quote

import requests

REPO = Path(__file__).resolve().parents[1]
OUT = REPO / '.football_cache' / 'understat'
LEAGUES = {'EPL': 'EPL', 'LaLiga': 'La_liga', 'Bundesliga': 'Bundesliga', 'SerieA': 'Serie_A', 'Ligue1': 'Ligue_1'}
FIRST_SEASON = 2021
USER_AGENT = 'football-value-pipeline/1.0 (historical research backfill; one request per few seconds)'
MAINTENANCE = 'We will come back soon'
PATTERN = re.compile(r"datesData\s*=\s*JSON\.parse\('([^']*)'\)")


def current_season(now=None) -> int:
    now = now or datetime.now(timezone.utc)
    return now.year if now.month >= 7 else now.year - 1


class Polite:
    """One session; at least `delay` seconds between requests to a host; backoff on failures."""

    def __init__(self, delay=6.0, retries=4):
        self.session = requests.Session()
        self.session.headers['User-Agent'] = USER_AGENT
        self.delay, self.retries, self.last = delay, retries, {}

    def get(self, url, **headers):
        host = url.split('/')[2]
        wait = 0.
        for attempt in range(self.retries + 1):
            gap = time.monotonic() - self.last.get(host, -1e9)
            time.sleep(max(0., self.delay - gap) + wait)
            self.last[host] = time.monotonic()
            try:
                response = self.session.get(url, timeout=(10, 60), headers=headers)
            except requests.RequestException as exc:
                error = type(exc).__name__
            else:
                if response.status_code not in (429, 500, 502, 503, 504):
                    return response
                error = f'HTTP {response.status_code}'
            wait = min(300., 15. * 2 ** attempt)
            print(f'  {error} from {host}; retrying in {wait:.0f}s', flush=True)
        return None


def parse_page(text):
    """Understat's match list from a league page (pre-2025 layout), or None."""
    match = PATTERN.search(text or '')
    if not match:
        return None
    values = json.loads(codecs.decode(match[1], 'unicode_escape'))
    return values if isinstance(values, list) else None


def parse_endpoint(text):
    try:
        data = json.loads(text)
    except ValueError:
        return None
    values = data.get('dates') if isinstance(data, dict) else None
    return values if isinstance(values, list) else None


def results(values) -> int:
    return sum(bool(v.get('isResult')) for v in values)


def try_understat(client, slug, year):
    page = f'https://understat.com/league/{slug}/{year}'
    attempts = []
    for url, parse, headers in ((page, parse_page, {}),
                                (f'https://understat.com/getLeagueData/{slug}/{year}', parse_endpoint,
                                 {'X-Requested-With': 'XMLHttpRequest', 'Referer': page})):
        response = client.get(url, **headers)
        if response is None:
            attempts.append({'url': url, 'outcome': 'no response'})
            continue
        if MAINTENANCE in response.text:
            attempts.append({'url': url, 'status': response.status_code, 'outcome': 'maintenance page'})
            return None, attempts  # the whole site serves it; no point trying the endpoint
        values = parse(response.text) if response.ok else None
        if values:
            return {'source': 'understat', 'url': url, 'original_url': page, 'status': response.status_code,
                    'raw': response.content, 'values': values}, attempts
        attempts.append({'url': url, 'status': response.status_code, 'outcome': 'no match data'})
    return None, attempts


def try_archive(client, slug, year, min_length=40_000):
    page = f'https://understat.com/league/{slug}/{year}'
    cdx = ('https://web.archive.org/cdx/search/cdx?url=' + quote(page, safe='') +
           '&output=json&filter=statuscode:200&collapse=digest&fl=timestamp,length')
    response = client.get(cdx)
    if response is None or not response.ok or 'Temporarily Offline' in response.text:
        return None, [{'url': cdx, 'outcome': 'archive index unavailable'}]
    rows = response.json()[1:]
    snapshots = sorted((r for r in rows if int(r[1] or 0) >= min_length), key=lambda r: r[0], reverse=True)
    attempts, best = [], None
    for timestamp, _ in snapshots:
        url = f'https://web.archive.org/web/{timestamp}id_/{page}'
        got = client.get(url)
        if got is None or not got.ok:
            attempts.append({'url': url, 'outcome': 'no response' if got is None else f'HTTP {got.status_code}'})
            continue
        values = parse_page(got.text)
        if not values:
            attempts.append({'url': url, 'status': got.status_code, 'outcome': 'no match data'})
            continue
        found = {'source': 'internet_archive', 'url': url, 'original_url': page, 'status': got.status_code,
                 'archive_timestamp': timestamp, 'raw': got.content, 'values': values}
        if best is None or results(values) > results(best['values']):
            best = found
        if results(values) == len(values):
            break  # newest complete capture
        attempts.append({'url': url, 'outcome': f'partial: {results(values)} of {len(values)} results'})
    return best, attempts


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('--leagues', nargs='+', default=list(LEAGUES))
    parser.add_argument('--seasons', nargs='+', type=int)
    parser.add_argument('--output', type=Path, default=OUT)
    parser.add_argument('--delay', type=float, default=6.)
    parser.add_argument('--refresh', action='store_true', help='refetch seasons already in the manifest')
    parser.add_argument('--no-archive', action='store_true')
    args = parser.parse_args(argv)
    seasons = args.seasons or list(range(FIRST_SEASON, current_season() + 1))
    args.output.mkdir(parents=True, exist_ok=True)
    manifest_path = args.output / 'manifest.json'
    manifest = json.loads(manifest_path.read_text(encoding='utf-8')) if manifest_path.exists() else \
        {'description': 'Understat match xG, five big leagues; written by scripts/fetch_understat_history.py',
         'files': {}, 'missing': {}}
    client = Polite(args.delay)
    understat_down = False
    for league in args.leagues:
        slug = LEAGUES[league]
        for year in seasons:
            key = f'{slug}_{year}'
            entry = manifest['files'].get(key)
            if entry and not args.refresh and (entry['complete'] or year < current_season()):
                print(key, 'already in manifest; skipped', flush=True)
                continue
            print(key, flush=True)
            found, attempts = (None, [{'outcome': 'understat.com in maintenance (earlier request)'}]) \
                if understat_down else try_understat(client, slug, year)
            understat_down = understat_down or any(a.get('outcome') == 'maintenance page' for a in attempts)
            if found is None and not args.no_archive:
                found, more = try_archive(client, slug, year)
                attempts += more
            if found is None:
                manifest['missing'][key] = {'checked_at_utc': datetime.now(timezone.utc).isoformat(),
                                            'attempts': attempts}
                print('  missing', flush=True)
            else:
                values = found['values']
                body = (json.dumps(values, ensure_ascii=False, sort_keys=True, indent=1) + '\n').encode('utf-8')
                (args.output / f'{key}.json').write_bytes(body)
                manifest['missing'].pop(key, None)
                manifest['files'][key] = {
                    'league': league, 'understat_league': slug, 'season': f'{year}/{str(year + 1)[2:]}',
                    'file': f'{key}.json', 'file_sha256': hashlib.sha256(body).hexdigest(),
                    'source': found['source'], 'source_url': found['url'], 'original_url': found['original_url'],
                    'archive_timestamp': found.get('archive_timestamp'), 'http_status': found['status'],
                    'fetched_at_utc': datetime.now(timezone.utc).isoformat(timespec='seconds'),
                    'raw_sha256': hashlib.sha256(found['raw']).hexdigest(), 'raw_bytes': len(found['raw']),
                    'matches': len(values), 'results': results(values), 'complete': results(values) == len(values),
                    'earlier_attempts': attempts}
                print(f"  {found['source']} {results(values)}/{len(values)} results", flush=True)
            manifest_path.write_text(json.dumps(manifest, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
