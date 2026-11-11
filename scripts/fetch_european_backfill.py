"""Fetch the raw files for the European backfill (harness only; never read by the live pipeline).

European results, UCL and UEL, to the start of the cached seasons, into .football_cache/europa/backfill/:

  openfootball-cl-<y>.txt   OpenFootball champions-league repo, <y>-<y+1>/cl.txt, 2015-2022 (results)
  openfootball-el-<y>.txt   the same repo, <y>-<y+1>/el.txt, 2020-2021 (the repo has no older UEL file)
  fixture-cl-<y>.csv        Fixture Download champions-league-<y>-UTC.csv, 2017-2022 (none before 2017)
  fixture-el-<y>.csv        Fixture Download europa-league-<y>-UTC.csv, 2019-2021 (none before 2019)
  evidence/openfootball-cl-<y>.txt, evidence/fixture-cl-<y>.csv   OpenFootball cl.txt and Fixture Download
                            champions-league 2023/24-2024/25, read ONLY as name evidence against the football-data.org
                            files the live UCL loader trains on, and only their rows before 21 Jan 2025 (never as results)
  evidence/domestic/        OpenFootball football.json (it.1, es.1, de.1, nl.1; 2023/24-2024/25) and Fixture
                            Download league files (2024/25): domestic name evidence for the European -> domestic
                            alias review only (before the domestic holdout)

Domestic league files, football-data.co.uk 2015/16-2020/21 for the 8 cached leagues, into
.football_cache/domestic_backfill/<ss>_<div>.csv: used only for European domestic-form coverage. They are
outside .football_cache's top level, so neither the live pipeline nor the domestic harness reads them.

OpenFootball is pinned to one commit, so each file can be fetched again byte for byte. Each folder gets a
manifest.json with the source URL, fetch time, HTTP status and the sha256 of every file (marked -text
in .gitattributes, so the bytes are never normalised). Files already in a manifest with a matching sha256
are kept, unless --refetch.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import time

import requests

ROOT = Path(__file__).resolve().parents[1]
OPENFOOTBALL_COMMIT = 'abfaeddc2ee3d14f99ecc163c9ddb46cb4d67cef'  # champions-league master, 2 Jul 2026
OPENFOOTBALL = f'https://raw.githubusercontent.com/openfootball/champions-league/{OPENFOOTBALL_COMMIT}' + '/{y}-{yy}/{file}'
FOOTBALL_JSON_COMMIT = 'e6744429ee395bc86f247348c6184bb08d4eb361'  # football.json master, 22 Sep 2026
FOOTBALL_JSON = f'https://raw.githubusercontent.com/openfootball/football.json/{FOOTBALL_JSON_COMMIT}' + '/{y}-{yy}/{code}.json'
FOOTBALL_JSON_LEAGUES = ('it.1', 'es.1', 'de.1', 'nl.1')  # tr.1 2023/24 is not valid JSON; 2024/25 spells no "SK"
FIXTURE_DOWNLOAD_LEAGUES = ('serie-a', 'la-liga', 'bundesliga', 'eredivisie', 'super-lig')
FIXTURE_DOWNLOAD = 'https://fixturedownload.com/download/{slug}-{y}-UTC.csv'
FOOTBALL_DATA = 'https://www.football-data.co.uk/mmz4281/{season}/{div}.csv'
DIVISIONS = ('E0', 'SP1', 'D1', 'I1', 'F1', 'N1', 'P1', 'T1')
USER_AGENT = 'fvp-research-backfill/1.0'
PAUSE_SECONDS = 2.0


def european_files():
    """file name -> (url, role)."""
    out = {}
    for y in range(2015, 2023):
        out[f'openfootball-cl-{y}.txt'] = (OPENFOOTBALL.format(y=y, yy=str(y + 1)[-2:], file='cl.txt'), 'results')
    for y in (2020, 2021):
        out[f'openfootball-el-{y}.txt'] = (OPENFOOTBALL.format(y=y, yy=str(y + 1)[-2:], file='el.txt'), 'results')
    for y in range(2017, 2023):
        out[f'fixture-cl-{y}.csv'] = (FIXTURE_DOWNLOAD.format(slug='champions-league', y=y), 'results')
    for y in (2019, 2020, 2021):
        out[f'fixture-el-{y}.csv'] = (FIXTURE_DOWNLOAD.format(slug='europa-league', y=y), 'results')
    for y in (2023, 2024):  # 2025/26 is all after the European holdout start: never fetched
        out[f'evidence/openfootball-cl-{y}.txt'] = (OPENFOOTBALL.format(y=y, yy=str(y + 1)[-2:], file='cl.txt'),
                                                   'name evidence only')
        out[f'evidence/fixture-cl-{y}.csv'] = (FIXTURE_DOWNLOAD.format(slug='champions-league', y=y), 'name evidence only')
    # Domestic name evidence for the European -> domestic alias review (european_backfill.domestic_aliases):
    # sources that spell clubs as the European files do, with domestic league fixtures. 2023/24-2024/25 only,
    # before the domestic holdout (16 Jan 2026).
    for y in (2023, 2024):
        for code in FOOTBALL_JSON_LEAGUES:
            out[f'evidence/domestic/football-json-{y}-{code}.json'] = (
                FOOTBALL_JSON.format(y=y, yy=str(y + 1)[-2:], code=code), 'domestic name evidence only')
    for slug in FIXTURE_DOWNLOAD_LEAGUES:
        out[f'evidence/domestic/fixture-{slug}-2024.csv'] = (FIXTURE_DOWNLOAD.format(slug=slug, y=2024),
                                                            'domestic name evidence only')
    return out


def domestic_files():
    out = {}
    for s in range(2015, 2021):
        season = f'{str(s)[-2:]}{str(s + 1)[-2:]}'
        for div in DIVISIONS:
            out[f'{season}_{div}.csv'] = (FOOTBALL_DATA.format(season=season, div=div), 'domestic form coverage only')
    return out


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def fetch(folder: Path, files: dict, description: str, refetch=False, session=None):
    session = session or requests.Session()
    manifest_path = folder / 'manifest.json'
    manifest = json.loads(manifest_path.read_text(encoding='utf-8')) if manifest_path.exists() else {}
    entries = manifest.get('files', {})
    for name, (url, role) in files.items():
        path = folder / name
        old = entries.get(name)
        if not refetch and old and path.exists() and sha256(path.read_bytes()) == old['sha256']:
            continue
        response = session.get(url, headers={'User-Agent': USER_AGENT}, timeout=60)
        time.sleep(PAUSE_SECONDS)
        if response.status_code != 200 or not response.content:
            raise RuntimeError(f'{url}: HTTP {response.status_code}')
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(response.content)
        entries[name] = {'source_url': url, 'role': role, 'fetched_at_utc': datetime.now(timezone.utc).isoformat(timespec='seconds'),
                         'http_status': response.status_code, 'bytes': len(response.content),
                         'sha256': sha256(response.content)}
        print(f'{name}: {len(response.content)} bytes')
    manifest = {'description': description, 'written_by': 'scripts/fetch_european_backfill.py',
                'files': dict(sorted(entries.items()))}
    if folder.name == 'backfill':
        manifest['openfootball_commit'] = OPENFOOTBALL_COMMIT
        manifest['football_json_commit'] = FOOTBALL_JSON_COMMIT
    manifest_path.write_text(json.dumps(manifest, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    return manifest


def verify(folder: Path) -> list:
    """Files whose bytes no longer match the manifest (empty when intact)."""
    manifest = json.loads((folder / 'manifest.json').read_text(encoding='utf-8'))
    return sorted(name for name, entry in manifest['files'].items()
                  if not (folder / name).exists() or sha256((folder / name).read_bytes()) != entry['sha256'])


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--cache', type=Path, default=ROOT / '.football_cache')
    parser.add_argument('--refetch', action='store_true')
    parser.add_argument('--only', choices=('european', 'domestic'))
    args = parser.parse_args(argv)
    if args.only != 'domestic':
        fetch(args.cache / 'europa' / 'backfill', european_files(),
              'Raw UCL/UEL results for the European backfill (evaluation harness only; the live pipeline never reads '
              'this folder). Reconciled by european_backfill.py.', args.refetch)
    if args.only != 'european':
        fetch(args.cache / 'domestic_backfill', domestic_files(),
              'football-data.co.uk league files 2015/16-2020/21 for the 8 cached leagues, used only for European '
              'domestic-form coverage (evaluation_harness.py --mode european). Not read by the live pipeline or the '
              'domestic harness.', args.refetch)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
