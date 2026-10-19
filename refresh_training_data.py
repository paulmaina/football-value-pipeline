"""Refresh football-data.co.uk CSVs independently of prediction generation.

No API keys, odds calls, model fitting, or forecast edits. Validate the complete
batch before replacing any file. Publishing retries from latest main, never
rebases generated data or force-pushes.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import os
import subprocess
import tempfile
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path

DIVISIONS = {'EPL': 'E0', 'LaLiga': 'SP1', 'Bundesliga': 'D1', 'SerieA': 'I1', 'Ligue1': 'F1'}
CACHE = Path('.football_cache')
STATUS = Path('docs/training_refresh_status.json')
URL = 'https://www.football-data.co.uk/mmz4281/{season}/{division}.csv'


def season_start(clock):
    return clock.year if clock.month >= 7 else clock.year - 1


def season_code(year):
    return f'{year % 100:02d}{(year + 1) % 100:02d}'


def inspect_csv(content, division, year, clock):
    """Reject malformed/truncated datasets instead of refreshing a bad cache."""
    try:
        text = content.decode('utf-8-sig')
    except UnicodeDecodeError:
        text = content.decode('latin-1')
    reader = csv.DictReader(io.StringIO(text))
    required = {'Date', 'HomeTeam', 'AwayTeam', 'FTHG', 'FTAG'}
    if not required.issubset(reader.fieldnames or []):
        raise ValueError('Missing required CSV columns')
    matches = {}
    for row in reader:
        if not any(str(v or '').strip() for v in row.values()):
            continue
        if None in row:
            raise ValueError('Malformed CSV row with extra fields')
        if row.get('Div', division) != division:
            raise ValueError('Unexpected division')
        hg, ag = row.get('FTHG'), row.get('FTAG')
        if not hg and not ag:  # Scheduled fixture, not a training result.
            continue
        if not hg or not ag or not hg.isdigit() or not ag.isdigit():
            raise ValueError('Missing, negative or non-integer final score')
        if int(hg) > 30 or int(ag) > 30:
            raise ValueError('Implausible final score')
        date = None
        for fmt in ('%d/%m/%Y', '%d/%m/%y'):
            try:
                date = datetime.strptime(row['Date'], fmt).date()
                break
            except (ValueError, TypeError):
                pass
        if date is None or date > clock.date() or not (datetime(year, 7, 1).date() <= date < datetime(year + 1, 7, 1).date()):
            raise ValueError('Invalid, future or wrong-season match date')
        expected_result = 'H' if int(hg) > int(ag) else 'A' if int(ag) > int(hg) else 'D'
        if row.get('FTR') and row['FTR'] != expected_result:
            raise ValueError('Final result contradicts final score')
        home, away = [(row.get(k) or '').strip() for k in ('HomeTeam', 'AwayTeam')]
        if not home or not away or home == away:
            raise ValueError('Invalid team identities')
        key = (date.isoformat(), home, away)
        if key in matches:
            raise ValueError('Duplicate completed fixture')
        matches[key] = (int(hg), int(ag))
    if not matches:
        raise ValueError('No completed matches in source')
    return matches


def download(url):
    last = None
    for attempt in range(3):
        try:
            request = urllib.request.Request(url, headers={
                'User-Agent': 'football-value-pipeline/training-refresh',
                'Cache-Control': 'no-cache'})
            with urllib.request.urlopen(request, timeout=30) as response:
                data = response.read(10_000_001)
            if len(data) > 10_000_000:
                raise ValueError('Source response exceeds size limit')
            return data
        except Exception as exc:
            last = exc
            if attempt < 2:
                time.sleep(1 + attempt)
    raise RuntimeError(f'Download failed for {url}: {last}')


def fetch_batch(clock, seasons_back=1, downloader=download):
    if not 1 <= seasons_back <= 10:
        raise ValueError('seasons_back must be between 1 and 10')
    tasks = [(league, div, year) for league, div in DIVISIONS.items()
             for year in range(season_start(clock)-seasons_back+1, season_start(clock)+1)]

    def fetch(task):
        league, division, year = task
        season = season_code(year)
        url = URL.format(season=season, division=division)
        data = downloader(url)
        matches = inspect_csv(data, division, year, clock)
        return {'league': league, 'division': division, 'year': year,
                'path': str(CACHE / f'{season}_{division}.csv'), 'source_url': url,
                'content': data, 'matches': matches}

    # Small bounded pool; independent public CSVs only, no paid API requests.
    with ThreadPoolExecutor(max_workers=3) as pool:
        return list(pool.map(fetch, tasks))


def apply_batch(repo, batch, clock):
    """Validate against current files before writing any cache file or status."""
    changes, entries = [], []
    for item in batch:
        path = repo / item['path']
        previous = path.read_bytes() if path.exists() else None
        new_matches = item['matches']
        old_matches = {}
        if previous is not None:
            old_matches = inspect_csv(previous, item['division'], item['year'], clock)
            if not set(old_matches).issubset(new_matches):
                raise ValueError(f"Refusing removed completed fixtures in {item['path']}")
        latest = max(key[0] for key in new_matches)
        try:
            source_text = item['content'].decode('utf-8-sig')
        except UnicodeDecodeError:
            source_text = item['content'].decode('latin-1')
        source_rows = list(csv.DictReader(io.StringIO(source_text)))
        statistic_coverage = {field: sum(bool((row.get(field) or '').strip())
            for row in source_rows if row.get('FTHG') and row.get('FTAG'))
            for field in ('HS','AS','HST','AST','HC','AC','HF','AF','HY','AY','HR','AR')}
        entries.append({k: item[k] for k in ('league','division','year','path','source_url')} | {
            'checked_at_utc': clock.isoformat(),
            'sha256': hashlib.sha256(item['content']).hexdigest(),
            'completed_matches': len(new_matches), 'latest_completed_date': latest,
            'statistic_nonempty_rows': statistic_coverage,
            'added_matches': len(set(new_matches)-set(old_matches)),
            'corrected_scores': sum(new_matches[k] != v for k,v in old_matches.items()),
            'download_status': 'unchanged' if previous == item['content'] else 'updated',
            'days_since_latest_match': (clock.date()-datetime.fromisoformat(latest).date()).days,
            'note': 'A successful download does not establish source completeness.'})
        if previous != item['content']:
            changes.append((path,item['content']))
    status_path = repo / STATUS
    previous_status = json.loads(status_path.read_text()) if status_path.exists() else {}
    indexed = {x['path']:x for x in previous_status.get('files',[])}
    indexed.update({x['path']:x for x in entries})
    status = {'provider':'football-data.co.uk', 'checked_at_utc':clock.isoformat(),
              'scope':'Five domestic leagues only; UCL is not supplied by this provider.',
              'files':sorted(indexed.values(),key=lambda x:x['path'])}
    # Atomic replacement per file. In CI the whole batch is then one Git commit.
    for path, content in changes + [(status_path,(json.dumps(status,indent=2)+'\n').encode())]:
        path.parent.mkdir(parents=True,exist_ok=True)
        with tempfile.NamedTemporaryFile(dir=path.parent,delete=False) as handle:
            temporary = Path(handle.name)
            handle.write(content)
        try:
            os.replace(temporary,path)
        finally:
            temporary.unlink(missing_ok=True)
    for entry in entries:
        print(f"{entry['league']} {entry['year']}: {entry['download_status']}; "
              f"{entry['completed_matches']} matches; latest {entry['latest_completed_date']}; "
              f"added {entry['added_matches']}")
    return entries


def git(repo, *args, check=True):
    return subprocess.run(['git','-C',str(repo),*args],check=check,text=True,
                          stdout=subprocess.PIPE,stderr=subprocess.PIPE)


def publish(repo, batch, clock, attempts=3):
    """Reapply validated downloads on latest main; no force-push or rebase."""
    repo = repo.resolve()
    with tempfile.TemporaryDirectory(prefix='training-publish-') as temporary:
        for attempt in range(attempts):
            git(repo,'fetch','origin','main')
            base = git(repo,'rev-parse','FETCH_HEAD').stdout.strip()
            work = Path(temporary)/f'work-{attempt}'
            git(repo,'worktree','add','--detach',str(work),base)
            try:
                entries = apply_batch(work,batch,clock)
                git(work,'add','--',str(STATUS),*[x['path'] for x in batch])
                if git(work,'diff','--cached','--quiet',check=False).returncode == 0:
                    return entries
                git(work,'-c','user.name=github-actions[bot]','-c',
                    'user.email=41898282+github-actions[bot]@users.noreply.github.com',
                    'commit','-m','Refresh validated domestic training data [skip ci]')
                result = git(work,'push','origin','HEAD:refs/heads/main',check=False)
                if result.returncode == 0:
                    print('Published training refresh to main.')
                    return entries
                git(repo,'fetch','origin','main')
                if git(repo,'rev-parse','FETCH_HEAD').stdout.strip() == base:
                    raise RuntimeError('Training refresh push failed: '+result.stderr)
                print('Main advanced; retrying on latest state.')
            finally:
                git(repo,'worktree','remove','--force',str(work))
    raise RuntimeError('Main kept advancing; no training refresh published')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo',type=Path,default=Path(__file__).resolve().parent)
    parser.add_argument('--seasons-back',type=int,default=1)
    parser.add_argument('--publish',action='store_true',help='Publish validated cache files to origin/main')
    args = parser.parse_args()
    clock = datetime.now(timezone.utc)
    batch = fetch_batch(clock,args.seasons_back)
    entries = publish(args.repo,batch,clock) if args.publish else apply_batch(args.repo,batch,clock)
    summary = os.getenv('GITHUB_STEP_SUMMARY')
    if summary:
        with open(summary,'a',encoding='utf-8') as handle:
            handle.write('## Domestic training refresh\n\nSuccessful download is not proof of current results.\n\n')
            handle.write('| League | Season start | Matches | Latest result | Download |\n|---|---:|---:|---|---|\n')
            for x in entries:
                handle.write(f"| {x['league']} | {x['year']} | {x['completed_matches']} | {x['latest_completed_date']} | {x['download_status']} |\n")


if __name__ == '__main__':
    main()
