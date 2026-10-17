"""Fixture-aware Actions collection with committed quota reservations.

The plan command uses only the standard library. Collection never replays API
calls when publication races with another main-branch update.
"""
import argparse
import csv
from datetime import datetime, timedelta, timezone
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile

from publish_performance import git, merge_snapshots

ROOT = Path('football_output_v2')
DATA = ROOT/'closing_odds'
BUDGET = DATA/'request_budget.json'
DAILY_CAP = 100


def read(path):
    return json.loads(path.read_text(encoding='utf-8-sig')) if path.exists() else {}


def write(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, sort_keys=True, indent=2, allow_nan=False)+'\n', encoding='utf-8')


def utc(value):
    value = datetime.fromisoformat(str(value).replace('Z','+00:00'))
    if value.tzinfo is None:
        raise ValueError('Expected timezone-aware kickoff')
    return value.astimezone(timezone.utc)


def plan(repo, clock=None, minutes=18):
    """Cheap scheduling gate; the collector revalidates archived identities."""
    clock = clock or datetime.now(timezone.utc)
    if not 1 <= minutes <= 20:
        raise ValueError('Collection horizon must be 1..20 minutes')
    root = Path(repo)/ROOT
    files = [root/'raw/all_leagues_predictions.csv']
    # Include archived fixtures so a newer forecast cannot hide a frozen pick.
    files += sorted((root/'performance/snapshots').glob('*/predictions.csv'))
    upcoming = set()
    for file in files:
        if not file.exists():
            continue
        with file.open(encoding='utf-8-sig',newline='') as handle:
            for row in csv.DictReader(handle):
                try:
                    kick = utc(row.get('kickoff_utc'))
                    event = str(row.get('odds_event_id',''))
                    if re.fullmatch(r'[A-Za-z0-9_-]+',event) and 0 < (kick-clock).total_seconds() <= minutes*60:
                        upcoming.add((kick,event))
                except (ValueError, TypeError):
                    continue
    state = read(Path(repo)/BUDGET)
    used = state.get('requests',0) if state.get('date')==clock.date().isoformat() else 0
    if isinstance(used,bool) or not isinstance(used,int) or not 0 <= used <= DAILY_CAP:
        raise ValueError('Invalid persisted closing request budget')
    ready = bool(upcoming) and used < DAILY_CAP
    return {'checked_at_utc':clock.isoformat(), 'ready':ready,
        'reason':'UPCOMING_FIXTURES' if ready else 'DAILY_REQUEST_CAP_REACHED' if used>=DAILY_CAP else 'NO_UPCOMING_FIXTURES',
        'upcoming_fixtures':len(upcoming), 'daily_allowance_remaining':DAILY_CAP-used,
        'watch_until_utc':max(k for k,_ in upcoming).isoformat() if upcoming else None}


def reserve(state, reservation_id, clock, allowance):
    """Reserve before any provider call. Unknown/interrupted usage stays charged."""
    if not re.fullmatch(r'[A-Za-z0-9_-]{1,100}',reservation_id):
        raise ValueError('Invalid reservation ID')
    if not 1 <= allowance <= DAILY_CAP:
        raise ValueError('Allowance must be 1..100')
    day = clock.date().isoformat()
    state = json.loads(json.dumps(state)) if state.get('date')==day else {'date':day,'requests':0}
    used = state.get('requests',0)
    if isinstance(used,bool) or not isinstance(used,int) or not 0 <= used <= DAILY_CAP:
        raise ValueError('Invalid persisted closing request budget')
    reservations = state.setdefault('reservations',{})
    if reservation_id in reservations:
        raise ValueError('Reservation already exists; no collection replay allowed')
    amount = min(allowance, DAILY_CAP-used)
    if not amount:
        return state,0
    state.update(requests=used+amount,daily_request_cap=DAILY_CAP)
    reservations[reservation_id] = {'allowance':amount,'used':0,'status':'reserved',
                                   'reserved_at_utc':clock.isoformat()}
    return state,amount


def settle(remote, local, reservation_id):
    """Release unused allocation only with a known final checkpoint."""
    if not remote.get('date') or not local.get('date') or not local.get('reservations',{}).get(reservation_id):
        raise ValueError('Missing quota checkpoint; keep committed reservation charged')
    if remote.get('date') != local.get('date'):
        return remote  # Never subtract yesterday's reservation from today's cap.
    remote = json.loads(json.dumps(remote))
    held = remote.get('reservations',{}).get(reservation_id)
    done = local.get('reservations',{}).get(reservation_id)
    if not held or not done or held['allowance']!=done['allowance']:
        raise ValueError('Committed quota reservation changed')
    if held['status']=='complete':
        if held['used']!=done['used']:
            raise ValueError('Completed reservation usage changed')
        return remote
    used = done['used']
    if isinstance(used,bool) or not isinstance(used,int) or not 0<=used<=held['allowance']:
        raise ValueError('Invalid final request count')
    remote['requests'] -= held['allowance']-used
    if not 0 <= remote['requests'] <= DAILY_CAP:
        raise ValueError('Invalid remaining request allowance')
    held.update(status='complete',used=used)
    return remote


def commit_push(work, paths, message, remote, branch):
    git(work,'add','--',*[str(p) for p in paths])
    if git(work,'diff','--cached','--quiet',check=False).returncode==0:
        return True
    git(work,'-c','user.name=github-actions[bot]','-c',
        'user.email=41898282+github-actions[bot]@users.noreply.github.com',
        'commit','-m',message+' [skip ci]')
    return git(work,'push',remote,f'HEAD:refs/heads/{branch}',check=False).returncode==0


def publish_results(repo, source, reservation_id, temp, remote, branch, attempts):
    from closing_odds import load_observations, review
    from performance_tracking import snapshots
    _, rejected = load_observations(source/ROOT)
    if rejected:
        raise ValueError('Invalid closing observations; recover artifact before publication')
    local = read(source/BUDGET)
    for attempt in range(attempts):
        git(repo,'fetch',remote,branch)
        base = git(repo,'rev-parse','FETCH_HEAD').stdout.strip()
        work = temp/f'publish-{attempt}'
        git(repo,'worktree','add','--detach',str(work),base)
        try:
            merge_snapshots(source/DATA/'observations',work/DATA/'observations')
            write(work/BUDGET,settle(read(work/BUDGET),local,reservation_id))
            status = read(source/DATA/'collector_status.json')
            previous = read(work/DATA/'collector_status.json')
            if status and (not previous or status['checked_at_utc']>=previous['checked_at_utc']):
                write(work/DATA/'collector_status.json',status)
            review(work/ROOT,snapshots(work/ROOT),datetime.now(timezone.utc))
            if commit_push(work,[DATA,ROOT/'performance/closing_odds'],
                           'Publish pre-kickoff closing quote evidence',remote,branch):
                return
        finally:
            git(repo,'worktree','remove','--force',str(work))
    raise RuntimeError('Closing quote publication failed; recover the workflow artifact. Reserved quota remains charged.')


def collect(repo, reservation_id, *, allowance=100, minutes=18, attempts=3,
            remote='origin', branch='main', runner=None, clock=None):
    repo = Path(repo).resolve()
    runner = runner or subprocess.run
    clock = clock or (lambda:datetime.now(timezone.utc))
    recovery = repo/'workflow_artifacts/closing-odds-recovery'
    with tempfile.TemporaryDirectory(prefix='closing-actions-') as directory:
        temp = Path(directory)
        for attempt in range(attempts):
            git(repo,'fetch',remote,branch)
            base = git(repo,'rev-parse','FETCH_HEAD').stdout.strip()
            work = temp/f'collect-{attempt}'
            git(repo,'worktree','add','--detach',str(work),base)
            try:
                now = clock()
                assessment = plan(work,now,minutes)
                if not assessment['ready']:
                    print(json.dumps(assessment));return assessment
                # Size the reservation to this kickoff group, retaining room
                # for retries without tying up the entire day unnecessarily.
                state,amount = reserve(read(work/BUDGET),reservation_id,now,
                    min(allowance,max(10,assessment['upcoming_fixtures']*3)))
                if not amount:
                    return assessment
                write(work/BUDGET,state)
                if not commit_push(work,[BUDGET],'Reserve closing quote request allowance',remote,branch):
                    continue  # No API request happened. Retry reservation on fresh main.
                try:
                    # Setup can finish late; absolute wall-clock bound comes from
                    # the fixture plan, not a fresh full watch interval.
                    seconds = (utc(assessment['watch_until_utc'])-clock()).total_seconds()
                    if seconds>0:
                        runner([sys.executable,'closing_odds.py','--api-key-source','environment',
                            '--watch','--stop-when-idle','--max-requests',str(amount),
                            '--hours',str(min(minutes*60,seconds)/3600),
                            '--budget-reservation',reservation_id],cwd=work,check=True)
                finally:
                    recovery.mkdir(parents=True,exist_ok=True)
                    shutil.copytree(work/DATA,recovery,dirs_exist_ok=True,
                                    ignore=shutil.ignore_patterns('collector.lock'))
                    publish_results(repo,work,reservation_id,temp,remote,branch,attempts)
                return assessment
            finally:
                git(repo,'worktree','remove','--force',str(work))
    raise RuntimeError('Could not reserve closing quota on latest main; no API calls made')


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command',choices=('plan','collect'))
    parser.add_argument('--repo',type=Path,default=Path(__file__).resolve().parent)
    parser.add_argument('--minutes',type=int,default=18)
    parser.add_argument('--allowance',type=int,default=100)
    parser.add_argument('--reservation-id')
    args = parser.parse_args(argv)
    if args.command=='plan':
        result = plan(args.repo,minutes=args.minutes)
        configured = any(os.getenv(name,'').strip() for name in
            ('THE_ODDS_API_KEY','THE_ODDS_API_KEY_FALLBACK_1','THE_ODDS_API_KEY_FALLBACK_2'))
        result['configured'] = configured
        if path := os.getenv('GITHUB_OUTPUT'):
            with open(path,'a') as handle:
                handle.write('ready='+str(result['ready'] and configured).lower()+'\n')
        if path := os.getenv('GITHUB_STEP_SUMMARY'):
            with open(path,'a') as handle:
                handle.write('Closing collection: '+result['reason']+'. '+
                    ('Credentials configured.' if configured else 'SETUP REQUIRED: add an Odds API repository secret.')+'\n')
        print(json.dumps(result))
    else:
        if not args.reservation_id:
            parser.error('--reservation-id is required for collection')
        collect(args.repo,args.reservation_id,allowance=args.allowance,minutes=args.minutes)
    return 0


if __name__=='__main__':
    raise SystemExit(main())
