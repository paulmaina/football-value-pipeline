"""Frozen benchmark-to-forward bridge; one-factor shadow trial, never production."""
from datetime import timedelta
import hashlib
import json
import math
from pathlib import Path
import numpy as np

VERSION='benchmark-forward-shadow-v1'
REGISTRY=Path(__file__).with_name('benchmark_forward_registry.json')
FILE='benchmark_forward_experiment.json'


def load_registry():
    r=json.loads(REGISTRY.read_text(encoding='utf-8-sig'))
    if r.get('version')!='benchmark-forward-registry-v1' or r.get('change')!='market_weight_only' or not 0<r['market_weight']<1 or r.get('approval_required') is not True:
        raise ValueError('Invalid frozen forward registry')
    source=REGISTRY.parent/r['selection']['source']
    if hashlib.sha256(source.read_bytes().replace(b'\r\n',b'\n')).hexdigest()!=r['selection']['source_sha256']:raise ValueError('Benchmark nomination evidence changed')
    data=json.loads(source.read_text(encoding='utf-8'))
    pick=next(c for c in data['development_choices'] if c['league']=='ALL' and c['family']=='market_weight' and c['market']=='1x2')
    if pick['selected_on_development']!=r['selection']['selected_variant'] or pick['selected_on_development']!=f"market_weight_{r['market_weight']:g}":raise ValueError('Candidate not selected by development evidence')
    return r


def registry_hash(r):return hashlib.sha256(json.dumps(r,sort_keys=True,separators=(',',':')).encode()).hexdigest()


def simplex(row,prefix):
    from performance_tracking import number
    p=[number(row.get(prefix+k),min_value=0,max_value=1) for k in ('home','draw','away')]
    return p if all(v is not None for v in p) and abs(sum(p)-1)<1e-6 else None


def decision(row,r,clock):
    from performance_tracking import utc,number
    kick=utc(row.get('kickoff_utc'));reasons=[]
    base=simplex(row,'p_');raw=simplex(row,'raw_p_');market=simplex(row,'market_p_')
    if row.get('league') not in r['leagues']:reasons.append('league_outside_frozen_trial')
    if kick is None or not 1200<=(kick-clock).total_seconds()<=72*3600:reasons.append('outside_capture_window')
    if row.get('odds_source')!='The Odds API' or row.get('market_blend_applied') not in (True,1,'True'):reasons.append('no_live_blended_reference')
    if any(number(row.get(k),min_value=90,max_value=100) is None for k in ('home_name_match_score','away_name_match_score')) or any(row.get(k) in (None,'','__LEAGUE_AVERAGE__') for k in ('model_home_team','model_away_team')):reasons.append('unreliable_team_identity')
    updated=utc(row.get('odds_h2h_last_update_utc'))
    if updated is None or not -300<=(clock-updated).total_seconds()<=24*3600:reasons.append('missing_stale_or_future_reference')
    prices=[number(row.get('market_reference_'+k+'_odds'),min_value=1.000001) for k in ('home','draw','away')]
    if any(p is None for p in prices) or not .98<=sum(1/p for p in prices)<=1.20:reasons.append('incoherent_reference_prices')
    if base is None or raw is None or market is None:reasons.append('invalid_probability_simplex')
    weight=number(row.get('market_weight'),min_value=0,max_value=1)
    if weight is None or abs(weight-r['baseline_market_weight'])>1e-12:reasons.append('production_weight_outside_frozen_trial')
    if base is not None and raw is not None and market is not None and any(abs(p-((1-r['baseline_market_weight'])*a+r['baseline_market_weight']*b))>1e-6 for p,a,b in zip(base,raw,market)):reasons.append('production_basis_mismatch')
    candidate=[(1-r['market_weight'])*p+r['market_weight']*q for p,q in zip(raw,market)] if not reasons else None
    return {'status':'available' if candidate is not None else 'unavailable','reasons':reasons,
        'baseline':base,'candidate':candidate,'raw':raw,'market_reference':market,
        'reference_updated_at_utc':row.get('odds_h2h_last_update_utc') or None,'reference_source':row.get('market_source_1x2') or None,
        'production_market_weight':weight}


def secondary(row,matrix,candidate):
    from historical_benchmark import goals
    from football_value_pipeline_v2_standalone import reweight_matrix_to_1x2
    from performance_tracking import number
    if matrix is None or candidate is None:return {'production_matrix':None,'baseline_goals':None,'candidate_goals':None,'secondary_status':'unavailable'}
    matrix=np.asarray(matrix,dtype=float)
    if matrix.ndim!=2 or not np.isfinite(matrix).all() or (matrix<0).any() or abs(float(matrix.sum())-1)>1e-8:raise ValueError('Invalid frozen production matrix')
    base=goals(matrix);h,a=np.indices(matrix.shape);hda={'home':float(matrix[h>a].sum()),'draw':float(matrix[h==a].sum()),'away':float(matrix[h<a].sum())};p=simplex(row,'p_')
    if p is None or any(abs(p[i]-hda[k])>1e-8 for i,k in enumerate(('home','draw','away'))):raise ValueError('Production matrix is not bound to forecast HDA')
    for k in ('over_1_5','under_3_5','btts_yes'):
        value=number(row.get('p_'+k),min_value=0,max_value=1)
        if value is None or abs(value-base[k])>1e-8:raise ValueError('Production matrix is not bound to goal forecasts')
    return {'production_matrix':matrix.tolist(),'baseline_goals':base,'candidate_goals':goals(reweight_matrix_to_1x2(matrix,candidate)), 'secondary_status':'available'}


def write_experiment(predictions,raw,generated,matrices=None):
    from performance_tracking import utc,write_json,fixture_key
    r=load_registry();clock=utc(generated)
    if clock is None:raise ValueError('Invalid generation time')
    data={'version':VERSION,'registry':r,'registry_sha256':registry_hash(r),'generated_at_utc':generated,
        'predictions_sha256':hashlib.sha256((raw/'all_leagues_predictions.csv').read_bytes()).hexdigest(),'rows':[]}
    for row in predictions.astype(object).where(predictions.notna(),None).to_dict('records'):
        evaluated=decision(row,r,clock)
        try:
            extra=secondary(row,(matrices or {}).get(fixture_key(row)),evaluated['candidate'])
        except ValueError:
            extra=secondary(row,None,evaluated['candidate']);extra['secondary_error']='MATRIX_VALIDATION_FAILED'
        data['rows'].append({**{k:row.get(k) for k in ('league','home_team','away_team','kickoff_utc','fixture_id')},**evaluated,**extra})
    write_json(raw/FILE,data);return data


def validate(data,generated,predictions,require_active=True):
    from performance_tracking import utc,fixture_key
    if data.get('version')!=VERSION or data.get('registry_sha256')!=registry_hash(data['registry']):raise ValueError('Changed trial registry hash')
    if require_active and data['registry']!=load_registry():raise ValueError('Unapproved active trial registry')
    if utc(data.get('generated_at_utc')) is None or utc(generated) is None or abs((utc(data['generated_at_utc'])-utc(generated)).total_seconds())>=1:raise ValueError('Unbound trial generation time')
    originals={fixture_key(p):p for p in predictions};seen=set()
    for row in data['rows']:
        key=fixture_key(row)
        if key not in originals or key in seen:raise ValueError('Invalid duplicate trial fixture')
        seen.add(key)
        expected=decision(originals[key],data['registry'],utc(data['generated_at_utc']))
        extra=secondary(originals[key],row.get('production_matrix'),expected['candidate'])
        if extra!={k:row.get(k) for k in extra}:raise ValueError('Unbound secondary score probabilities')
        for field,value in expected.items():
            actual=row.get(field)
            # CSV encodes absent text as an empty field; JSON uses null.
            # These are the same missing evidence, not different timestamps.
            if field in ('reference_updated_at_utc','reference_source'):
                actual=actual or None
            if isinstance(value,list) and value and isinstance(value[0],(int,float)):
                if not isinstance(actual,list) or len(actual)!=len(value) or any(not math.isfinite(a) or abs(a-b)>1e-9 for a,b in zip(actual,value)):raise ValueError('Unbound trial probability')
            elif isinstance(value,float):
                if actual is None or abs(actual-value)>1e-9:raise ValueError('Unbound trial number')
            elif actual!=value:raise ValueError('Unbound trial evidence '+field)
    if seen!=set(originals):raise ValueError('Incomplete trial coverage')


def capture_file(raw,generated):
    from performance_tracking import read_csv,load_json
    from forecast_integrity import forecast_digest_variants
    path=raw/FILE
    if not path.exists():return None
    data=load_json(path,{})
    validate(data,generated,read_csv(raw/'all_leagues_predictions.csv'))
    if data['predictions_sha256'] not in forecast_digest_variants(raw/'all_leagues_predictions.csv'):raise ValueError('Trial forecast binding failed')
    return path


def frozen(root,archive):
    from performance_tracking import load_json,utc,fixture_key
    from forecast_integrity import forecast_digest_variants
    result={};rejected=[]
    for meta,predictions,_ in archive:
        directory=root/'performance/snapshots'/meta['git_commit_sha'][:16];path=directory/FILE
        sha=meta.get('sha256',{}).get(FILE)
        if not sha:continue
        try:
            if not path.exists() or hashlib.sha256(path.read_bytes()).hexdigest()!=sha:raise ValueError('Trial snapshot integrity failure')
            data=load_json(path,{})
            validate(data,meta['generated_at_utc'],predictions,require_active=False)
            if data['predictions_sha256'] not in forecast_digest_variants(directory/'predictions.csv'):raise ValueError('Snapshot forecast binding failed')
        except (ValueError,KeyError,TypeError):rejected.append(meta['git_commit_sha']);continue
        generated=utc(data['generated_at_utc']);captured=utc(meta['captured_at_utc'])
        if generated.date().isoformat()<data['registry']['registered_on']:continue
        for row in data['rows']:
            kick=utc(row['kickoff_utc'])
            if kick is None or max(generated,captured)>kick-timedelta(minutes=20) or kick>generated+timedelta(hours=72):continue
            key=fixture_key(row)
            result.setdefault((data['registry_sha256'],key),{**row,'fixture_key':key,'snapshot_commit':meta['git_commit_sha'],'registry_sha256':data['registry_sha256']})
    return list(result.values()),rejected


def block_interval(rows,r):
    if len(rows)<2:return None
    weeks=sorted({row['week'] for row in rows})
    if len(weeks)<2:return None
    sums=np.array([sum(x['log_loss_gain'] for x in rows if x['week']==w) for w in weeks]);counts=np.array([sum(x['week']==w for x in rows) for w in weeks])
    rng=np.random.default_rng(r['review_gates']['bootstrap_seed']);idx=rng.integers(0,len(weeks),size=(r['review_gates']['bootstrap_replicates'],len(weeks)))
    values=sums[idx].sum(axis=1)/counts[idx].sum(axis=1)
    alpha=(1-r['review_gates']['confidence_level'])/2
    return [float(np.quantile(values,alpha)),float(np.quantile(values,1-alpha))]


def metrics(rows):
    from historical_benchmark import metrics as probability_metrics
    result={}
    for variant in ('baseline','candidate'):
        converted=[{'p_home':x[variant][0],'p_draw':x[variant][1],'p_away':x[variant][2],'y':x['y']} for x in rows]
        result[variant]=probability_metrics(converted,'1x2')
        buckets=[]
        for i in range(10):
            cohort=[x for x in rows if min(9,int(max(x[variant])*10))==i]
            if not cohort:continue
            mean=sum(max(x[variant]) for x in cohort)/len(cohort);rate=sum(int(np.argmax(x[variant]))==x['y'] for x in cohort)/len(cohort)
            buckets.append({'band':i,'n':len(cohort),'mean_probability':mean,'observed_rate':rate,'gap':mean-rate})
        result[variant]['top_label_calibration']=buckets
        result[variant]['ece']=sum(b['n']*abs(b['gap']) for b in buckets)/len(rows) if rows else None
    for metric in ('log_loss','brier','rps'):
        result[metric+'_gain']=result['baseline'][metric]-result['candidate'][metric] if rows else None
    return result


def evaluate(root,archive,records,clock):
    from performance_tracking import utc,fixture_match
    from historical_benchmark import score
    registry=load_registry();all_observations,rejected=frozen(root,archive);active_hash=registry_hash(registry)
    observations=[r for r in all_observations if r['registry_sha256']==active_hash];graded=[];coverage=[]
    records=[x for x in records if x.get('source_status')=='FINISHED' and x.get('source')=='football-data.org/v4']
    verified=available=0
    for row in observations:
        match,state=fixture_match(row,records)
        if utc(row['kickoff_utc'])>clock-timedelta(hours=2):match=None;state='PENDING_KICKOFF_OR_FINAL_SCORE'
        coverage.append({**row,'result_status':state})
        if not match or row['league'] not in registry['leagues']:continue
        verified+=1
        if row['status']!='available':continue
        available+=1;y=0 if match['home_goals']>match['away_goals'] else 1 if match['home_goals']==match['away_goals'] else 2
        year,week,_=utc(row['kickoff_utc']).isocalendar()
        item={**row,'y':y,'home_goals':match['home_goals'],'away_goals':match['away_goals'],'source_match_id':match['match_id'],'week':f'{year}-W{week:02d}'}
        scores={name:score(dict(zip(('p_home','p_draw','p_away'),row[name]),y=y),'1x2') for name in ('baseline','candidate')}
        item.update({m+'_gain':scores['baseline'][m]-scores['candidate'][m] for m in ('log_loss','brier','rps')});graded.append(item)
    comparison=metrics(graded);interval=block_interval(graded,registry);weeks=len({x['week'] for x in graded});gates=registry['review_gates']
    sufficient=len(graded)>=gates['minimum_paired_fixtures'] and weeks>=gates['minimum_gameweeks']
    fraction=available/verified if verified else None
    quality=fraction is not None and fraction>=gates['minimum_verified_coverage'] and not rejected
    from historical_benchmark import metrics as goal_metrics
    second=[x for x in graded if x.get('secondary_status')=='available']
    secondary_comparison={}
    for market in registry['secondary_markets']:
        secondary_comparison[market]={name:goal_metrics([{market:x[name+'_goals'][market],'home_goals':x['home_goals'],'away_goals':x['away_goals']} for x in second],market) for name in ('baseline','candidate')}
    secondary_fraction=len(second)/len(graded) if graded else None
    secondary_pass=secondary_fraction is not None and secondary_fraction>=.8 and all(c['candidate']['brier']<=c['baseline']['brier'] and c['candidate']['log_loss']<=c['baseline']['log_loss'] for c in secondary_comparison.values())
    supports=sufficient and quality and secondary_pass and interval is not None and interval[0]>0 and comparison['brier_gain']>=0 and comparison['candidate']['ece']<=comparison['baseline']['ece']
    summary={'version':VERSION,'candidate_id':registry['candidate_id'],'registry_sha256':registry_hash(registry),'reviewed_at_utc':clock.isoformat(),
        'status':'READY_FOR_REVIEW' if sufficient and quality else 'DATA_QUALITY_BLOCKED' if sufficient else 'COLLECT_MORE_DATA',
        'evidence':'SUPPORTS_FORECASTING_REVIEW' if supports else 'NO_CLEAR_PROMOTION_EVIDENCE',
        'paired_fixtures':len(graded),'gameweeks':weeks,'verified_coverage':fraction,'observed_fixtures':len(observations),'verified_in_scope_fixtures':verified,
        'rejected_snapshot_commits':rejected,'comparison':comparison,'log_loss_gain_week_block95':interval,
        'secondary_comparison':secondary_comparison,'secondary_coverage':secondary_fraction,'secondary_gate_passed':secondary_pass,
        'by_league':{league:metrics([x for x in graded if x['league']==league]) for league in registry['leagues']},'review_gates':gates,
        'other_archived_registry_versions':sorted({r['registry_sha256'] for r in all_observations if r['registry_sha256']!=active_hash}),
        'automatic_production_change':False,'note':'Primary 1X2 log loss; week-block bootstrap, one preregistered candidate. Calibration and subgroup metrics are descriptive. Ready means enough evidence to review, including negative findings; it does not mean approval or profitability. Baseline is the actual production forecast. No closing odds, backfill, bets or automatic promotion.'}
    return summary,graded,coverage


def review_experiment(root,archive,records,clock):
    from performance_tracking import write_json,write_csv
    summary,graded,coverage=evaluate(root,archive,records,clock);dest=root/'performance/benchmark_forward_experiment'
    versioned=dest/'versions'/summary['registry_sha256']
    write_json(versioned/'summary.json',summary);write_json(versioned/'graded.json',graded);write_json(versioned/'coverage.json',coverage)
    write_json(dest/'summary.json',summary)
    # JSON ledgers retain arrays exactly; human CSV records use flattened probabilities.
    write_json(dest/'graded.json',graded);write_json(dest/'coverage.json',coverage)
    lines=['# Benchmark forward trial','',summary['note'],'',f"Candidate: {summary['candidate_id']}; status: **{summary['status']}**; evidence: {summary['evidence']}.",'',
        f"Paired fixtures: {summary['paired_fixtures']}/300; gameweeks: {summary['gameweeks']}/6; verified coverage: {summary['verified_coverage']}.",'',
        f"Comparison: {json.dumps(summary['comparison'])}",'',f"Week-block 95% log-loss gain interval: {summary['log_loss_gain_week_block95']}.",'','Production changes require your review and approval.','']
    (dest/'report.md').write_text('\n'.join(lines),encoding='utf-8')
    return summary


def validate_report(root):
    from performance_tracking import load_json,snapshots,utc
    from historical_benchmark import write_json
    dest=root/'performance/benchmark_forward_experiment';actual=load_json(dest/'summary.json',{})
    expected,graded,coverage=evaluate(root,snapshots(root),list(load_json(root/'performance/verified_results.json',{}).values()),utc(actual['reviewed_at_utc']))
    if actual!=expected or load_json(dest/'graded.json',[])!=graded or load_json(dest/'coverage.json',[])!=coverage:raise ValueError('Forward trial report differs from immutable evidence')
    return True
