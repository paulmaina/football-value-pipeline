"""Generate, capture and review scheduled forecasts on fresh main; safe push retries."""
import argparse
from datetime import datetime,timezone
from pathlib import Path
import subprocess
import sys
import tempfile

from publish_performance import git


def publish(repo,attempts=3,runner=None):
    runner=runner or subprocess.run;repo=repo.resolve()
    with tempfile.TemporaryDirectory(prefix='forecast-publish-') as directory:
        for attempt in range(attempts):
            git(repo,'fetch','origin','main');base=git(repo,'rev-parse','FETCH_HEAD').stdout.strip()
            work=Path(directory)/str(attempt);git(repo,'worktree','add','--detach',str(work),base)
            try:
                runner([sys.executable,'football_value_pipeline_v2_standalone.py','--leagues','EPL','LaLiga','Bundesliga','SerieA','Ligue1','UCL',
                    '--tune-half-life','--goal-blend-experiment','--additional-odds-coverage','all','--market-led-experiment','--recency-experiment','--reliability-experiment','--api-key-source','environment'],cwd=work,check=True)
                runner([sys.executable,'workflow_checks.py','raw'],cwd=work,check=True)
                runner([sys.executable,'format_football_output.py'],cwd=work,check=True)
                git(work,'add','football_output_v2/raw')
                # Preserve the exact validated source revision used by this
                # forecast, including downloads newer than the refresh job.
                # Odds response caches and collection checkpoints are separate.
                cache = work/'.football_cache'
                training = [p for div in ('E0','SP1','D1','I1','F1')
                            for p in cache.glob(f'????_{div}.csv')]
                training += list(cache.glob('fdorg_history_UCL_????.json'))
                training += list(cache.glob('fdorg_history_UCL_????.meta.json'))
                training += list((cache/'bbs/feature_models').glob('*/*.json'))
                status = work/'docs/ucl_training_refresh_status.json'
                if status.exists(): training.append(status)
                if training:
                    git(work,'add','--',*[str(p.relative_to(work)) for p in training])
                if git(work,'diff','--cached','--quiet',check=False).returncode==0:return
                git(work,'-c','user.name=github-actions[bot]','-c','user.email=41898282+github-actions[bot]@users.noreply.github.com','commit','-m','Generate automated pre-match forecasts')
                # Capture forecast commit before review output is committed. Token pushes do not trigger other workflows.
                sha=git(work,'rev-parse','HEAD').stdout.strip()
                runner([sys.executable,'performance_tracking.py','capture','--commit-sha',sha],cwd=work,check=True)
                runner([sys.executable,'performance_tracking.py','review','--api-key-source','environment'],cwd=work,check=True)
                runner([sys.executable,'workflow_checks.py','reports'],cwd=work,check=True)
                git(work,'add','football_output_v2/performance','football_output_v2/readable')
                if git(work,'diff','--cached','--quiet',check=False).returncode:
                    git(work,'-c','user.name=github-actions[bot]','-c','user.email=41898282+github-actions[bot]@users.noreply.github.com','commit','-m','Capture and grade automated forecasts')
                pushed=git(work,'push','origin','HEAD:main',check=False)
                if pushed.returncode==0:return
                print('Main advanced; regenerate forecasts on latest main. No rebase or force push.',flush=True)
            finally:git(repo,'worktree','remove','--force',str(work),check=False)
    raise RuntimeError('Scheduled forecast push did not succeed after retries')


def main(argv=None):
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--repo',type=Path,default=Path('.'));args=parser.parse_args(argv)
    publish(args.repo);return 0


if __name__=='__main__':raise SystemExit(main())
