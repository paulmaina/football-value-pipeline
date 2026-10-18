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


NAMES=('goal_blend_experiment','market_led_experiment','recency_experiment','filter_sensitivity_experiment')


def build_queue(root,clock):
    from performance_tracking import load_json,snapshots,utc
    items=[];archive=snapshots(root)
    for name in NAMES:
        data=load_json(root/'performance'/name/'summary.json',{})
        counts={'goal_blend_experiment':data.get('graded_fixture_markets',0),
            'market_led_experiment':data.get('paired_graded_fixture_markets',0),
            'recency_experiment':data.get('graded_fixture_markets',0),
            'filter_sensitivity_experiment':max((c.get('graded',0) for c in data.get('comparisons',[]) if c.get('tier')=='ALL'),default=0)}
        dates=[]
        for meta,_,_ in archive:
            filename='goal_blend_experiment.json' if name=='recency_experiment' else name+'.json'
            path=root/'performance/snapshots'/meta['git_commit_sha'][:16]/filename
            sha=meta.get('sha256',{}).get(filename)
            if not sha or not path.exists() or hashlib.sha256(path.read_bytes()).hexdigest()!=sha:continue
            if name=='recency_experiment' and not load_json(path,{}).get('recency_experiment'):continue
            dates.append(utc(meta['captured_at_utc']))
        days=(clock-min(dates)).days if dates else 0
        fresh=utc(data.get('reviewed_at_utc')) is not None and abs((clock-utc(data['reviewed_at_utc'])).total_seconds())<1
        status='FIRST_LOOK_READY' if fresh and days>=28 and counts[name]>=30 else 'COLLECT_MORE_DATA' if fresh else 'REPORT_UNAVAILABLE_OR_STALE'
        items.append({'name':name,'key':name,'status':status,'settled_evidence':counts[name],
            'collection_days':days,'scope':'FIRST_LOOK_ONLY_NO_PROMOTION','report':name+'/report.md',
            'note':'28 days and 30 settled observations permit an initial review, not approval or demonstrated edge.',
            **({'graded_paper_bets':data.get('graded_selections',0)} if name=='market_led_experiment' else {})})
    policy=load_json(root/'performance/shortlist_policy_experiment/summary.json',{})
    fresh=utc(policy.get('reviewed_at_utc')) is not None and abs((clock-utc(policy['reviewed_at_utc'])).total_seconds())<1
    items.append({'name':'shortlist_policy_experiment','key':'shortlist_policy_experiment:'+policy.get('version','not_generated'),
        'status':policy.get('status','COLLECT_MORE_DATA') if fresh else 'REPORT_UNAVAILABLE_OR_STALE',
        'settled_evidence':policy.get('verified_fixtures',0),'gameweeks':policy.get('gameweeks',0),
        'scope':'POLICY_REVIEW_APPROVAL_REQUIRED','report':'shortlist_policy_experiment/report.md',
        'automatic_production_change':False})
    weights=load_json(root/'performance/shortlist_weight_experiment/summary.json',{})
    fresh=utc(weights.get('reviewed_at_utc')) is not None and abs((clock-utc(weights['reviewed_at_utc'])).total_seconds())<1
    items.append({'name':'shortlist_weight_experiment','key':'shortlist_weight_experiment:'+weights.get('version','not_generated'),
        'status':weights.get('status','COLLECT_MORE_DATA') if fresh else 'REPORT_UNAVAILABLE_OR_STALE',
        'settled_evidence':weights.get('verified_fixtures',0),'gameweeks':weights.get('gameweeks',0),
        'scope':'POLICY_REVIEW_APPROVAL_REQUIRED','report':'shortlist_weight_experiment/report.md',
        'automatic_production_change':False})
    trial=load_json(root/'performance/benchmark_forward_experiment/summary.json',{})
    fresh=utc(trial.get('reviewed_at_utc')) is not None and abs((clock-utc(trial['reviewed_at_utc'])).total_seconds())<1
    items.append({'name':'benchmark_forward_experiment','key':'benchmark_forward:'+trial.get('registry_sha256','not_generated'),
        'status':trial.get('status','COLLECT_MORE_DATA') if fresh else 'REPORT_UNAVAILABLE_OR_STALE',
        'settled_evidence':trial.get('paired_fixtures',0),'gameweeks':trial.get('gameweeks',0),
        'scope':'FORECASTING_REVIEW_APPROVAL_REQUIRED','evidence':trial.get('evidence','UNAVAILABLE'),
        'report':'benchmark_forward_experiment/report.md','automatic_production_change':False})
    totals=load_json(root/'performance/totals_anchor_experiment/summary.json',{})
    fresh=utc(totals.get('reviewed_at_utc')) is not None and abs((clock-utc(totals['reviewed_at_utc'])).total_seconds())<1
    items.append({'name':'totals_anchor_experiment','key':'totals_anchor:'+totals.get('registry_sha256','not_generated'),
        'status':totals.get('status','COLLECT_MORE_DATA') if fresh else 'REPORT_UNAVAILABLE_OR_STALE',
        'settled_evidence':totals.get('paired_fixtures',0),'gameweeks':totals.get('gameweeks',0),
        'scope':'FORECASTING_REVIEW_APPROVAL_REQUIRED','evidence':totals.get('evidence','UNAVAILABLE'),
        'report':'totals_anchor_experiment/report.md','automatic_production_change':False})
    reliability=load_json(root/'performance/model_reliability_experiment/summary.json',{})
    fresh=utc(reliability.get('reviewed_at_utc')) is not None and abs((clock-utc(reliability['reviewed_at_utc'])).total_seconds())<1
    for candidate in reliability.get('comparisons',[]):
        items.append({'name':'model_reliability_experiment','key':'model_reliability:'+reliability.get('registry_sha256','')+':'+candidate['candidate_id'],
            'candidate_id':candidate['candidate_id'],
            'status':candidate['status'] if fresh else 'REPORT_UNAVAILABLE_OR_STALE',
            'settled_evidence':candidate['paired_fixtures'],'gameweeks':candidate['gameweeks'],
            'scope':'FORECASTING_REVIEW_APPROVAL_REQUIRED','evidence':candidate['evidence'],
            'report':'model_reliability_experiment/report.md','automatic_production_change':False})
    return {'version':'experiment-review-queue-v1','reviewed_at_utc':clock.isoformat(),'experiments':items,'automatic_promotion':False,
        'note':'Existing sidecar first-look thresholds differ from the new benchmark candidate promotion gates. Notifications invite review, including negative findings; they never approve changes.'}


def write_queue(root,clock):
    from performance_tracking import write_json
    data=build_queue(root,clock);dest=root/'performance';write_json(dest/'experiment_review_queue.json',data)
    lines=['# Experiment review queue','',data['note'],'', '| Experiment | Status | Settled evidence | Scope |','|---|---|---:|---|']
    for item in data['experiments']:lines.append(f"| [{item['name']}]({item['report']}) | {item['status']} | {item['settled_evidence']} | {item['scope']} |")
    lines+=['','Benchmark candidates require at least 300 paired fixtures, six gameweeks and valid coverage. Four weeks remains an initial review point for the original sidecars.','']
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
