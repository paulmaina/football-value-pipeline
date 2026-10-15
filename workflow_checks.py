"""Offline CI and forward-review integrity checks. Never generate probabilities."""
from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
import math
import os
from pathlib import Path
import re
import subprocess
import sys
import xml.etree.ElementTree as ET
from zipfile import ZipFile

FORECAST_PATHS = (
    'football_output_v2/raw/all_leagues_predictions.csv',
    'football_output_v2/raw/conservative_bet_shortlist.csv',
    'football_output_v2/raw/conservative_bet_summary.json',
    'football_output_v2/raw/goal_blend_experiment.json',
    'football_output_v2/raw/market_led_experiment.json',
    'football_output_v2/raw/filter_sensitivity_experiment.json',
    'football_output_v2/raw/shortlist_policy_experiment.json',
    'football_output_v2/raw/benchmark_forward_experiment.json',
    'football_output_v2/raw/totals_anchor_experiment.json',
    'football_output_v2/raw/model_reliability_experiment.json',
)
SIDECARS = ('goal_blend_experiment.json', 'market_led_experiment.json', 'filter_sensitivity_experiment.json', 'benchmark_forward_experiment.json', 'totals_anchor_experiment.json', 'model_reliability_experiment.json', 'shortlist_policy_experiment.json')
CLI_FILES = ('football_value_pipeline_v2_standalone.py', 'format_football_output.py',
             'performance_tracking.py', 'performance_excel.py', 'publish_performance.py',
             'refresh_conservative_shortlist.py', 'refresh_training_data.py', 'refresh_ucl_training.py', 'historical_benchmark.py', 'experiment_review_queue.py', 'publish_scheduled_forecasts.py', 'closing_odds.py', 'workflow_checks.py')
COVERAGE_FLOORS = {'forecast_integrity.py':100, 'api_key_config.py':90, 'conservative_bet_filter.py':90,
    'shortlist_policy_experiment.py':85,
    'double_chance.py':90, 'goal_market_validation.py':85, 'goal_blend_experiment.py':90,
    'market_led_experiment.py':90, 'match_scores.py':90, 'performance_tracking.py':85,
    'performance_excel.py':85, 'publish_performance.py':75, 'workflow_checks.py':80,
    'dc_decay_validation.py':85, 'market_blend_validation.py':90, 'refresh_training_data.py':70, 'format_football_output.py':60, 'ucl_training.py':90, 'quote_policy.py':95, 'pipeline_health.py':90, 'refresh_ucl_training.py':75, 'recency_experiment.py':85, 'filter_sensitivity_experiment.py':85, 'historical_benchmark.py':85, 'benchmark_forward_experiment.py':85, 'experiment_review_queue.py':85, 'publish_scheduled_forecasts.py':80, 'totals_anchor_experiment.py':90, 'closing_odds.py':90, 'model_reliability_experiment.py':90}


def require(condition, message):
    if not condition: raise ValueError(message)


def read_json(path):
    # Reject non-standard NaN/Infinity rather than carrying invalid metrics.
    def invalid(value): raise ValueError(f'Nonfinite JSON number in {path.name}')
    with path.open(encoding='utf-8-sig') as handle:
        return json.load(handle, parse_constant=invalid)


def close(actual, expected, label):
    if expected is None:
        require(actual is None or actual == '', f'{label}: expected unavailable')
    else:
        require(actual is not None and actual != '' and math.isfinite(float(actual))
                and abs(float(actual)-expected) <= 1e-6, f'{label}: inconsistent value')


def raw_check(root):
    from performance_tracking import read_csv, utc, fixture_key, SUPPORTED_MARKETS, number
    raw=root/'raw'
    summary=read_json(raw/'conservative_bet_summary.json')
    require(utc(summary.get('generated_at_utc')) is not None, 'Invalid forecast generation timestamp')
    predictions=read_csv(raw/'all_leagues_predictions.csv')
    picks=read_csv(raw/'conservative_bet_shortlist.csv')
    require(bool(predictions), 'No forecast rows to capture')
    keys=set()
    for row in predictions:
        require(all(row.get(k) for k in ('league','home_team','away_team','kickoff_utc')), 'Incomplete forecast identity')
        require(utc(row['kickoff_utc']) is not None, 'Invalid forecast kickoff')
        key=fixture_key(row);require(key not in keys, 'Duplicate forecast fixture');keys.add(key)
        p=[number(row.get('p_'+side),min_value=0,max_value=1) for side in ('home','draw','away')]
        require(all(x is not None for x in p) and abs(sum(p)-1)<=1e-6, 'Invalid 1X2 probability simplex')
        for field,value in row.items():
            if (field.startswith('p_') or field.startswith('raw_p_')) and value not in ('',None):
                require(number(value,min_value=0,max_value=1) is not None, f'Invalid probability column {field}')
    selected=set()
    for row in picks:
        key=fixture_key(row);require(key in keys, 'Selection without matching forecast')
        require(key not in selected, 'Multiple selected markets for one fixture');selected.add(key)
        require(row.get('market') in summary.get('eligible_markets',SUPPORTED_MARKETS), 'Unsupported selected market')
        require(row.get('selection_tier') in ('STRICT','PROVISIONAL'), 'Invalid selection tier')
        require(number(row.get('offered_decimal_odds'),min_value=1.000001) is not None, 'Missing real selection price')
        require(number(row.get('rank_probability') or row.get('predicted_probability'),min_value=0,max_value=1) is not None,
                'Missing selection probability')
    for field,count in [('n_fixtures',len(predictions)),('n_shortlisted',len(picks)),
        ('n_strict_qualified',sum(r.get('selection_tier')=='STRICT' for r in picks)),
        ('n_provisional_watchlist',sum(r.get('selection_tier')=='PROVISIONAL' for r in picks))]:
        if field in summary: require(summary[field]==count, f'Forecast summary {field} does not match CSV')
    warnings=[]
    for name in SIDECARS:
        module = name.removesuffix('.json')
        if (raw/name).exists():
            try:
                import importlib
                valid=importlib.import_module(module).capture_file(raw,summary['generated_at_utc'])
                if valid is None: warnings.append(f'{name}: stale/unbound sidecar excluded from capture')
            except Exception:
                warnings.append(f'{name}: invalid optional sidecar excluded from capture')
    return {'forecasts':len(predictions),'selections':len(picks),'warnings':warnings}


def changed_forecasts(repo, before, sha):
    require(re.fullmatch(r'[0-9a-fA-F]{40}',sha or '') is not None, 'Capture requires a full source SHA')
    def git(*args):
        return subprocess.run(['git','-C',str(repo),*args],check=True,text=True,capture_output=True).stdout
    require(git('rev-parse','HEAD').strip()==sha, 'Capture checkout differs from event SHA')
    if before == '0'*40:
        names=git('ls-tree','-r','--name-only',sha,'--',*FORECAST_PATHS)
    else:
        require(re.fullmatch(r'[0-9a-fA-F]{40}',before or '') is not None, 'Missing previous push SHA')
        names=git('diff','--name-only',before,sha,'--',*FORECAST_PATHS)
    return bool(names.strip())


def capture_event(repo,root,event,sha,before=''):
    from performance_tracking import capture
    if event=='push' and not changed_forecasts(repo,before,sha):
        print('No forecast inputs changed; capture skipped.')
        return False
    require(event in ('push','workflow_dispatch'), 'Capture is only permitted for data pushes or explicit manual requests')
    if event=='workflow_dispatch':
        require(re.fullmatch(r'[0-9a-fA-F]{40}',sha or '') is not None,'Capture requires a full source SHA')
        current=subprocess.run(['git','-C',str(repo),'rev-parse','HEAD'],check=True,text=True,capture_output=True).stdout.strip()
        require(current==sha,'Capture checkout differs from event SHA')
    raw_check(root)
    return capture(sha,root=root)


def archive_check(root):
    from performance_tracking import utc,read_csv
    from datetime import timedelta
    manifests=[];warnings=[]
    base=root/'performance'/'snapshots'
    for directory in sorted(base.iterdir()) if base.exists() else []:
        if not directory.is_dir(): continue
        meta=read_json(directory/'metadata.json')
        sha=meta.get('git_commit_sha','')
        require(re.fullmatch(r'[0-9a-fA-F]{40}',sha) is not None and directory.name==sha[:16], 'Invalid snapshot SHA/directory')
        created,generated=utc(meta.get('captured_at_utc')),utc(meta.get('generated_at_utc'))
        require(created and generated and generated<=created+timedelta(minutes=5), 'Invalid snapshot timestamps')
        digests=meta.get('sha256',{})
        require(isinstance(digests,dict) and all(k in digests for k in ('predictions.csv','shortlist.csv','selection_summary.json')),
                'Snapshot missing required integrity manifest')
        for name,digest in digests.items():
            require(name in ('predictions.csv','shortlist.csv','selection_summary.json','pipeline_health.json',*SIDECARS), 'Unexpected snapshot path')
            path=directory/name
            valid=path.is_file() and hashlib.sha256(path.read_bytes()).hexdigest()==digest
            if name in (*SIDECARS, 'pipeline_health.json'):
                if not valid: warnings.append(f'{directory.name}/{name}: optional artifact missing/tampered; excluded from grading')
            else: require(valid, f'Snapshot integrity failure: {directory.name}/{name}')
        summary=read_json(directory/'selection_summary.json')
        source_generated=utc(summary.get('generated_at_utc'))
        require(source_generated is not None and abs((source_generated-generated).total_seconds())<1,'Snapshot generation time differs from source summary')
        rows=read_csv(directory/'predictions.csv');picks=read_csv(directory/'shortlist.csv')
        eligible=sum(1 for r in rows if (kick:=utc(r.get('kickoff_utc'))) and
            max(created,generated)<=kick-timedelta(minutes=20))
        for key,count in [('n_all_forecasts',len(rows)),('n_shortlist',len(picks)),('n_pre_kickoff_forecasts',eligible)]:
            require(meta.get(key)==count, f'Snapshot {directory.name}: {key} mismatch')
        manifests.append({'sha':sha,'forecasts':len(rows),'selections':len(picks),'eligible':eligible,
                          'policy':meta.get('selection_policy_version','legacy/unspecified')})
    return {'snapshots':manifests,'warnings':warnings}


def expected_stats(rows):
    rated=[r for r in rows if r['status'] in ('WON','LOST')]
    wins=sum(r['status']=='WON' for r in rated)
    profit=[float(r['unit_profit']) for r in rated if r.get('unit_profit') not in ('',None)]
    brier=[float(r['brier']) for r in rated if r.get('brier') not in ('',None)]
    return dict(total=len(rows),graded=len(rated),wins=wins,losses=len(rated)-wins,pending=len(rows)-len(rated),
        win_rate=wins/len(rated) if rated else None,brier=sum(brier)/len(brier) if brier else None,
        settled_with_odds=len(profit),profit_per_unit_staked=sum(profit) if profit else None,
        flat_stake_roi=sum(profit)/len(profit) if profit else None)


def report_check(root):
    from performance_tracking import read_csv,utc,frozen_rows,snapshots,result_for_market,number,fixture_match
    from performance_excel import REPORT_NAME
    audit=archive_check(root)
    performance=root/'performance'
    metrics=read_json(performance/'metrics.json')
    require(utc(metrics.get('reviewed_at_utc')) is not None, 'Missing report review timestamp')
    selections=read_csv(performance/'shortlist_grades.csv');predictions=read_csv(performance/'prediction_grades.csv')
    frozen={r['fixture_key']:r for r in frozen_rows(snapshots(root),'shortlist')}
    require(len(selections)==len(frozen), 'Report omitted or added frozen selections')
    cache_path=performance/'verified_results.json'
    records=list(read_json(cache_path).values()) if cache_path.exists() else []
    seen=set()
    for row in selections:
        key=row['fixture_key'];require(key not in seen,'Duplicate graded fixture');seen.add(key)
        original=frozen.get(key);require(original is not None,'Graded selection without immutable snapshot')
        require(row['snapshot_commit']==original['snapshot_commit'] and row['market']==original['market'], 'Report selection provenance changed')
        require(row['selection_policy_version']==original['selection_policy_version'], 'Report policy provenance changed')
        close(row.get('offered_decimal_odds'),number(original.get('offered_decimal_odds')),'Frozen selection price')
        close(row.get('predicted_probability'),number(original.get('rank_probability') or original.get('predicted_probability')),'Frozen selection probability')
        from quote_policy import stake_cost
        close(row.get('per_stake_cost') or 0,stake_cost(original.get('per_stake_cost') or 0),'Frozen selection cost')
        require(row['selection_tier']==(original.get('selection_tier') or ('STRICT' if original.get('decision')=='SHORTLISTED' else 'PROVISIONAL')), 'Report selection tier changed')
        if row['status'] in ('WON','LOST'):
            verified,state=fixture_match(original,records)
            require(verified is not None and str(verified['match_id'])==row.get('source_match_id'), 'Selection result absent from verified cache')
            require(verified.get('source_status')=='FINISHED' and verified.get('source')=='football-data.org/v4','Selection cache source is not verified finished')
            require(row.get('final_score')==f"{verified['home_goals']}-{verified['away_goals']}", 'Selection score differs from verified cache')
            require(row.get('match_source')=='football-data.org/v4' and row.get('source_match_id'), 'Graded result lacks verified source')
            match=re.fullmatch(r'(\d+)-(\d+)',row.get('final_score',''));require(match is not None,'Invalid graded score')
            won=result_for_market(row['market'],int(match[1]),int(match[2]))
            require(won is not None and won==(row['status']=='WON'), 'Outcome differs from regulation-time score')
            p=number(row.get('predicted_probability'),min_value=0,max_value=1)
            if p is not None: close(row.get('brier'),(p-int(won))**2,'Selection Brier')
            price=number(row.get('offered_decimal_odds'),min_value=1.000001)
            from quote_policy import stake_cost
            cost=stake_cost(original.get('per_stake_cost') or 0)
            close(row.get('per_stake_cost') or 0,cost,'Frozen selection cost')
            close(row.get('unit_profit'),((price-1 if won else -1)-cost) if price is not None else None,'Selection P&L')
        else:
            require(row.get('unit_profit') in ('',None) and row.get('brier') in ('',None),'Pending result included in scored metrics')
    for field,value in expected_stats(selections).items():close(metrics['shortlist'].get(field),value,'Shortlist '+field)
    for dimension,column in [('tier','selection_tier'),('market','market'),('league','league'),('week','week'),('policy','selection_policy_version')]:
        groups=metrics.get('groups',{}).get(dimension,{})
        require(all(r.get(column) in groups for r in selections),f'Missing {dimension} group')
        for label,values in groups.items():
            for field,value in expected_stats([r for r in selections if r.get(column)==label]).items():
                close(values.get(field),value,f'{dimension} {label}: {field}')
    frozen_predictions={r['fixture_key']:r for r in frozen_rows(snapshots(root),'predictions')}
    require(len(predictions)==len(frozen_predictions) and len({r['fixture_key'] for r in predictions})==len(predictions), 'Prediction report coverage mismatch')
    require(all(r['fixture_key'] in frozen_predictions and r['snapshot_commit']==frozen_predictions[r['fixture_key']]['snapshot_commit'] for r in predictions), 'Prediction provenance changed')
    require(metrics['prediction_fixtures_graded']==sum(r['status']=='GRADED' for r in predictions), 'Prediction graded count mismatch')
    prediction_brier=[]
    for row in predictions:
        if row['status']!='GRADED': continue
        original=frozen_predictions[row['fixture_key']]
        verified,state=fixture_match(original,records)
        require(verified is not None and str(verified['match_id'])==row.get('source_match_id'),'Prediction result absent from verified cache')
        require(verified.get('source_status')=='FINISHED' and verified.get('source')=='football-data.org/v4','Prediction cache source is not verified finished')
        require(row.get('final_score')==f"{verified['home_goals']}-{verified['away_goals']}", 'Prediction score differs from verified cache')
        probs=[number(original.get('p_'+side),min_value=0,max_value=1) for side in ('home','draw','away')]
        if all(p is not None for p in probs):
            h,a=verified['home_goals'],verified['away_goals']
            expected=sum((p-y)**2 for p,y in zip(probs,(h>a,h==a,h<a)))
            close(row.get('one_x_two_brier'),expected,'Prediction Brier')
            prediction_brier.append(expected)
    close(metrics.get('prediction_1x2_multiclass_brier'),sum(prediction_brier)/len(prediction_brier) if prediction_brier else None,'Prediction mean Brier')
    workbook=root/'readable'/REPORT_NAME
    with ZipFile(workbook) as z:
        require(z.testzip() is None,'Corrupt workbook ZIP')
        require('xl/workbook.xml' in z.namelist(),'Missing native workbook')
        for name in z.namelist():
            if name.endswith('.xml'):ET.fromstring(z.read(name))
        require(len([n for n in z.namelist() if '/charts/chart' in n and n.endswith('.xml')])>=3,'Missing native report charts')
        ns='{http://schemas.openxmlformats.org/spreadsheetml/2006/main}'
        sheet=ET.fromstring(z.read('xl/worksheets/sheet1.xml'))
        for address,field in [('B7','total'),('B8','graded'),('B9','wins'),('B11','pending'),
                              ('B12','win_rate'),('B13','flat_stake_roi'),('B14','profit_per_unit_staked'),('B15','brier')]:
            cell=sheet.find(f'.//{ns}c[@r="{address}"]');require(cell is not None,'Missing workbook metric cell')
            value=cell.find(ns+'v')
            if value is None:value=cell.find(ns+'is/'+ns+'t')
            require(value is not None,'Missing workbook metric value')
            expected=metrics['shortlist'][field]
            if expected is None and field=='profit_per_unit_staked':close(value.text,0,'Workbook empty cumulative P&L')
            elif expected is None:require(value.text=='n.a.',f'Workbook {field} must be unavailable')
            else:close(value.text,expected,'Workbook '+field)
    require((performance/'README.md').is_file(),'Missing readable performance report')
    warnings=audit['warnings']
    if metrics.get('provider_errors'):warnings.append('Result provider has errors; cached verified results used where available')
    experiments={}
    for name in ('goal_blend_experiment','market_led_experiment','recency_experiment','filter_sensitivity_experiment','benchmark_forward_experiment', 'totals_anchor_experiment', 'model_reliability_experiment', 'shortlist_policy_experiment'):
        path=performance/name/'summary.json'
        if path.exists():
            data=read_json(path);experiments[name]=data
            experimental_time=utc(data.get('reviewed_at_utc'))
            if experimental_time is None or abs((experimental_time-utc(metrics['reviewed_at_utc'])).total_seconds()) > 1:
                warnings.append(f'{name}: report timestamp differs from current baseline review')
            elif name=='shortlist_policy_experiment':
                from shortlist_policy_experiment import validate_report
                validate_report(root)
            elif name=='model_reliability_experiment':
                from model_reliability_experiment import validate_report
                validate_report(root)
            elif name=='totals_anchor_experiment':
                from totals_anchor_experiment import validate_report
                validate_report(root)
            elif name=='benchmark_forward_experiment':
                from benchmark_forward_experiment import validate_report
                validate_report(root)
            elif name=='filter_sensitivity_experiment':
                from filter_sensitivity_experiment import validate_report
                validate_report(root)
            elif name=='recency_experiment':
                from recency_experiment import validate_report
                validate_report(root)
            if data.get('rejected_snapshot_commits'):
                warnings.append(f'{name}: invalid archived data excluded; see rejected_snapshot_commits')
    closing_path=performance/"closing_odds/summary.json"
    if closing_path.exists():
        from closing_odds import validate_report as validate_closing
        validate_closing(root)
    training={}
    for path in sorted((root/'raw').glob('*_diagnostics.json')):
        data=read_json(path);training[path.stem.replace('_diagnostics','')]=data.get('training_end')
    health_path=performance/'pipeline_health.json'
    health_data=read_json(health_path) if health_path.exists() else {}
    if health_data:
        health_time=utc(health_data.get('reviewed_at_utc'))
        require(health_time and abs((health_time-utc(metrics['reviewed_at_utc'])).total_seconds())<1,'Health report timestamp differs from performance review')
        history=read_json(performance/'health_history.json')
        latest=history.get('days',{}).get(health_time.date().isoformat(),{})
        for field,value in metrics['shortlist'].items():close(latest.get('shortlist_performance',{}).get(field),value,'Daily health performance '+field)
        require(len(health_data.get('snapshot_capture_history',[]))==len(audit['snapshots']),'Health snapshot coverage mismatch')
        with ZipFile(workbook) as z:
            wb=ET.fromstring(z.read('xl/workbook.xml'))
            require(any(s.get('name')=='Pipeline Health' for s in wb.find(ns+'sheets')),'Missing native Pipeline Health worksheet')
    for info in health_data.get('training',{}).values():
        state=info.get('current_source_health',{}).get('status')
        if state and state!='CURRENT_WITHIN_PROVIDER_SCHEDULE': warnings.append('UCL training/source health: '+state)
    if health_data.get('quote_audit',{}).get('exchange_quotes'): warnings.append('Latest stored shortlist includes gross exchange quotes from an older execution policy')
    capture_history = health_data.get('snapshot_capture_history', [])
    if capture_history:
        for name, state in capture_history[-1].get('experiments', {}).items():
            if state in ('PRESENT_BUT_REJECTED', 'MISSING_OR_TAMPERED'):
                warnings.append(f'{name}: latest snapshot {state}; experimental evidence was not accepted')
    return {'status':'VERIFIED_WITH_WARNINGS' if warnings else 'VERIFIED','pipeline_health':health_data,'reviewed_at_utc':metrics['reviewed_at_utc'],
        'snapshots':len(audit['snapshots']),'shortlist':metrics['shortlist'],'policy_groups':metrics['groups']['policy'],
        'provider_errors':metrics.get('provider_errors',{}),'training_end_dates':training,'experiments':experiments,'warnings':warnings}


def smoke(repo):
    paths=sorted(repo.glob('*.py'))+sorted((repo/'tests').glob('*.py'))
    for path in paths:compile(path.read_text(encoding='utf-8-sig'),str(path),'exec')
    for name in CLI_FILES:
        subprocess.run([sys.executable,str(repo/name),'--help'],check=True,stdout=subprocess.DEVNULL,cwd=repo,timeout=30)
    return {'python_modules_compiled':len(paths),'cli_help_checked':len(CLI_FILES)}


def coverage_check(path):
    data=read_json(path)
    require(data['totals']['percent_covered']>=75,'Overall application coverage below 75%')
    for name,floor in COVERAGE_FLOORS.items():
        found=[entry for file,entry in data['files'].items() if Path(file).name==name]
        require(len(found)==1,f'Missing coverage for {name}')
        require(found[0]['summary']['percent_covered']>=floor,f'{name}: coverage below {floor}%')
    return {'overall_percent':data['totals']['percent_covered'],'critical_module_floors':COVERAGE_FLOORS}


def emit(data,output=None,summary=False):
    content=json.dumps(data,indent=2,allow_nan=False)+'\n'
    if output:
        output.parent.mkdir(parents=True,exist_ok=True);output.write_text(content,encoding='utf-8')
    print(content)
    if summary and (destination:=os.getenv('GITHUB_STEP_SUMMARY')):
        with open(destination,'a',encoding='utf-8') as handle:
            handle.write('## Forward review integrity\n\n')
            handle.write(f'Status: **{data.get("status","VERIFIED")}**; snapshots: {data.get("snapshots",0)}.\n\n')
            if 'shortlist' in data:
                d=data['shortlist'];handle.write(f'Selections: {d["total"]}; graded: {d["graded"]}; pending: {d["pending"]}.\n\n')
            for warning in data.get('warnings',[]):handle.write(f'- {warning}\n')
            handle.write('\nTraining end dates: '+json.dumps(data.get('training_end_dates',{}))+'\n')
            handle.write('\n| Policy | Graded | Wins | Losses | Pending |\n|---|---:|---:|---:|---:|\n')
            for policy,counts in data.get('policy_groups',{}).items():
                handle.write(f"| {policy} | {counts['graded']} | {counts['wins']} | {counts['losses']} | {counts['pending']} |\n")
            for name,experiment in data.get('experiments',{}).items():
                handle.write('\n'+name+': '+json.dumps({k:v for k,v in experiment.items() if k in
                    ('total_fixture_markets','observed_fixture_markets','available_fixture_markets',
                     'graded_fixture_markets','paired_graded_fixture_markets','selected','graded_selections','decision')})+'\n')


def main(argv=None):
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action',choices=('smoke','capture','raw','archives','reports','coverage'))
    parser.add_argument('--repo',type=Path,default=Path('.'))
    parser.add_argument('--root',type=Path,default=Path('football_output_v2'))
    parser.add_argument('--event',default='workflow_dispatch')
    parser.add_argument('--sha',default=os.getenv('GITHUB_SHA',''))
    parser.add_argument('--before',default=os.getenv('BEFORE_SHA',''))
    parser.add_argument('--output',type=Path)
    parser.add_argument('--github-summary',action='store_true')
    parser.add_argument('--coverage-file',type=Path,default=Path('workflow_artifacts/coverage.json'))
    args=parser.parse_args(argv)
    if args.action=='smoke':data=smoke(args.repo)
    elif args.action=='capture':data={'captured':capture_event(args.repo,args.root,args.event,args.sha,args.before)}
    elif args.action=='raw':data=raw_check(args.root)
    elif args.action=='archives':data=archive_check(args.root)
    elif args.action=='reports':data=report_check(args.root)
    else:data=coverage_check(args.coverage_file)
    emit(data,args.output,args.github_summary)
    return 0


if __name__=='__main__':raise SystemExit(main())
