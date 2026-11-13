"""Generate, capture and review scheduled forecasts on fresh main; safe push retries."""
import argparse
from datetime import datetime,timezone
import json
from pathlib import Path
import subprocess
import sys
import tempfile

import league_registry
import odds_api_usage
from prediction_runs import prune_captured_runs
from publish_performance import git

BOT=('-c','user.name=github-actions[bot]','-c','user.email=41898282+github-actions[bot]@users.noreply.github.com')


class ForecastStopped(RuntimeError):
    """A clear, expected stop (not a code failure): reported as one line, no traceback."""


def training_files(work):
    """Every registry league's refreshed training files, plus shared feature models."""
    cache = work/'.football_cache'
    training = [p for league in league_registry.REGISTRY for pattern in league.cache_globs()
                for p in sorted(cache.glob(pattern)) if p.is_file()]
    training += list((cache/'bbs/feature_models').glob('*/*.json'))
    status = work/'docs/ucl_training_refresh_status.json'
    if status.exists(): training.append(status)
    return training


def read_outcome(path):
    """The pipeline's run outcome, or None when it wrote none (older or mocked runners)."""
    try:
        data=json.loads(Path(path).read_text(encoding='utf-8'))
    except (OSError,ValueError):
        return None
    return data if isinstance(data,dict) else None


def usage_record(outcome,attempt):
    usage=outcome.get('odds_api') or {}
    record={'recorded_at_utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),
            'workflow':'scheduled-forecasts','outcome':outcome.get('status',''),'attempt':attempt,
            'calls':usage.get('calls',0),'credits_spent':usage.get('credits_spent',0),
            'by_endpoint':usage.get('by_endpoint',{}),'slots':usage.get('slots',{}),
            'remaining_total':usage.get('remaining_total'),'all_keys_exhausted':usage.get('all_keys_exhausted',False)}
    if outcome.get('message'):record['message']=outcome['message']
    if outcome.get('forecast_rows') is not None:record['forecast_rows']=outcome['forecast_rows']
    return record


def report(outcome,record):
    """One readable block in the run summary: the outcome line first, then credits."""
    lines=[str(outcome.get('message') or ''),*[str(n) for n in outcome.get('notes') or []]]
    odds_api_usage.write_step_summary('\n\n'.join(line for line in lines if line)+'\n\n'+odds_api_usage.summary_markdown(record))


def append_records(work,records):
    for record in records:odds_api_usage.append_log(record,work)
    return str(odds_api_usage.LOG)


def commit_usage_only(work,records,message):
    """Commit just the usage log on a run that publishes nothing else."""
    git(work,'add','--',append_records(work,records))
    if git(work,'diff','--cached','--quiet',check=False).returncode==0:return True
    git(work,*BOT,'commit','-m',message)
    return git(work,'push','origin','HEAD:main',check=False).returncode==0


def publish(repo,attempts=3,runner=None):
    runner=runner or subprocess.run;repo=repo.resolve()
    # Every attempt spends credits, so every attempt's usage is logged once a push lands.
    records=[]
    with tempfile.TemporaryDirectory(prefix='forecast-publish-') as directory:
        for attempt in range(attempts):
            git(repo,'fetch','origin','main');base=git(repo,'rev-parse','FETCH_HEAD').stdout.strip()
            work=Path(directory)/str(attempt);git(repo,'worktree','add','--detach',str(work),base)
            outcome_path=Path(directory)/f'outcome-{attempt}.json'
            try:
                # No legacy companion: its only readers were the archived forward trials.
                try:
                    runner([sys.executable,'football_value_pipeline_v2_standalone.py','--leagues',*league_registry.keys(),
                        '--additional-odds-coverage','all','--api-key-source','environment',
                        '--no-legacy-comparison','--research-free-sources',
                        '--run-outcome-out',str(outcome_path)],cwd=work,check=True)
                except subprocess.CalledProcessError:
                    outcome=read_outcome(outcome_path)
                    if outcome is not None:
                        records.append(usage_record(outcome,attempt));report(outcome,records[-1])
                    if outcome is not None and outcome.get('status')==odds_api_usage.CREDITS_EXHAUSTED:
                        # Keep the balances visible on main, then stop with one line.
                        commit_usage_only(work,records,'Record Odds API usage (credits exhausted)')
                        raise ForecastStopped(odds_api_usage.EXHAUSTED_MESSAGE) from None
                    raise
                outcome=read_outcome(outcome_path)
                if outcome is not None:
                    records.append(usage_record(outcome,attempt));report(outcome,records[-1])
                    if outcome.get('status')==odds_api_usage.NO_FIXTURES:
                        # Not an error: nothing to forecast, nothing to capture.
                        if commit_usage_only(work,records,'Record Odds API usage (no fixtures)'):return outcome
                        print('Main advanced; record usage on latest main.',flush=True);continue
                runner([sys.executable,'workflow_checks.py','raw'],cwd=work,check=True)
                runner([sys.executable,'format_football_output.py'],cwd=work,check=True)
                # Narrow-margin report: read-only over raw/, written to readable/ (committed with the review).
                runner([sys.executable,'narrow_margin_report.py'],cwd=work,check=True)
                git(work,'add','football_output_v2/raw')
                # Preserve the exact validated source revision used by this
                # forecast, including downloads newer than the refresh job.
                # Odds response caches and collection checkpoints are separate.
                # Europa's reconciled snapshot and sources are committed like the others.
                training = training_files(work)
                if training:
                    git(work,'add','--',*[str(p.relative_to(work)) for p in training])
                if git(work,'diff','--cached','--quiet',check=False).returncode==0:return outcome
                git(work,*BOT,'commit','-m','Generate automated pre-match forecasts')
                # Capture forecast commit before review output is committed. Token pushes do not trigger other workflows.
                sha=git(work,'rev-parse','HEAD').stdout.strip()
                runner([sys.executable,'performance_tracking.py','capture','--commit-sha',sha],cwd=work,check=True)
                # Captured, non-current bundles leave in the commit that adds their snapshots.
                pruned=prune_captured_runs(work/'football_output_v2')
                runner([sys.executable,'performance_tracking.py','review','--api-key-source','environment'],cwd=work,check=True)
                runner([sys.executable,'workflow_checks.py','reports','--output',
                    'football_output_v2/performance/workflow_health.json'],cwd=work,check=True)
                git(work,'add','football_output_v2/performance','football_output_v2/readable')
                if records:git(work,'add','--',append_records(work,records))
                if pruned:
                    git(work,'add','--all','--',*[f'football_output_v2/raw/prediction_runs/{run}' for run in pruned])
                if git(work,'diff','--cached','--quiet',check=False).returncode:
                    git(work,*BOT,'commit','-m','Capture and grade automated forecasts')
                pushed=git(work,'push','origin','HEAD:main',check=False)
                if pushed.returncode==0:return outcome
                print('Main advanced; regenerate forecasts on latest main. No rebase or force push.',flush=True)
            finally:git(repo,'worktree','remove','--force',str(work),check=False)
    raise RuntimeError('Scheduled forecast push did not succeed after retries')


def main(argv=None):
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--repo',type=Path,default=Path('.'));args=parser.parse_args(argv)
    try:
        publish(args.repo)
    except ForecastStopped as stop:
        print(f'::error::{stop}',flush=True)
        return 1
    return 0


if __name__=='__main__':raise SystemExit(main())
