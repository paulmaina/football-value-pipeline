"""Automatic review queue and idempotent repository issue notifications."""
import argparse
import base64
from datetime import datetime,timezone
import hashlib
import json
from pathlib import Path
import re
import subprocess
import tempfile


def build_queue(root,clock):
    # Retired experiments (archive/) left the queue; their committed reports are frozen.
    items=[]
    # The benchmark-forward and totals-anchor trials are archived too, so nothing is queued.
    return {'version':'experiment-review-queue-v1','reviewed_at_utc':clock.isoformat(),'experiments':items,'automatic_promotion':False,
        'note':'Only live forward trials are queued, and none is live. Notifications invite review, including negative findings; they never approve changes.'}


def write_queue(root,clock):
    from performance_tracking import write_json
    data=build_queue(root,clock);dest=root/'performance';write_json(dest/'experiment_review_queue.json',data)
    lines=['# Experiment review queue','',data['note'],'', '| Experiment | Status | Settled evidence | Scope |','|---|---|---:|---|']
    for item in data['experiments']:lines.append(f"| [{item['name']}]({item['report']}) | {item['status']} | {item['settled_evidence']} | {item['scope']} |")
    if not data['experiments']:lines.append('| None live | | | |')
    lines+=['','The benchmark-forward and totals-anchor trials are archived; their frozen reports stay readable.','']
    (dest/'experiment_review_queue.md').write_text('\n'.join(lines),encoding='utf-8');return data


def notify(repository,clock=None,runner=None):
    from performance_tracking import utc
    if not re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+',repository):raise ValueError('Invalid notification repository')
    runner=runner or subprocess.run;clock=clock or datetime.now(timezone.utc)
    def gh(*args):return runner(['gh',*args],check=True,text=True,capture_output=True).stdout
    payload=json.loads(gh('api',f'repos/{repository}/contents/football_output_v2/performance/experiment_review_queue.json'))
    queue=json.loads(base64.b64decode(payload['content']).decode('utf-8'))
    reviewed=utc(queue.get('reviewed_at_utc'))
    if queue.get('version')!='experiment-review-queue-v1' or reviewed is None or not 0<=(clock-reviewed).total_seconds()<48*3600 or queue.get('automatic_promotion') is not False:
        raise ValueError('Review queue is invalid or stale')
    emitted=[]
    for item in queue['experiments']:
        if item['status'] not in ('READY_FOR_REVIEW','FIRST_LOOK_READY'):continue
        keyhash=hashlib.sha256(item['key'].encode()).hexdigest()[:20];marker='experiment-review-'+keyhash
        existing=json.loads(gh('issue','list','--repo',repository,'--state','all','--search',marker+' in:body','--json','number','--limit','100'))
        if existing:continue
        body=f"An automated evidence gate has been reached.\n\nExperiment: {item['name']}\nStatus: {item['status']}\nSettled evidence: {item['settled_evidence']}\nScope: {item['scope']}\n\nRead the [current review queue](https://github.com/{repository}/blob/main/football_output_v2/performance/experiment_review_queue.md) before reviewing results. Verified corrections can change readiness. This issue requests review; it does not approve a production change or establish profitability.\n\n<!-- {marker} -->\n"
        with tempfile.TemporaryDirectory() as directory:
            path=Path(directory)/'body.md';path.write_text(body,encoding='utf-8')
            url=gh('issue','create','--repo',repository,'--title','Experiment review ready: '+item['name'],'--body-file',str(path)).strip();emitted.append(url)
    return emitted


def main(argv=None):
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--notify-repository',required=True);args=parser.parse_args(argv)
    for url in notify(args.notify_repository):print(url)
    return 0


if __name__=='__main__':raise SystemExit(main())
