"""One frozen Pinnacle totals anchoring trial; no production writes or extra requests."""
from datetime import timedelta
import hashlib
import json
import math
from pathlib import Path
import numpy as np

FILE='totals_anchor_experiment.json'
VERSION='pinnacle-totals-anchor-v1'
REGISTRY=Path(__file__).with_name('totals_anchor_registry.json')


def registry():
    from benchmark_forward_experiment import registry_hash
    r=json.loads(REGISTRY.read_text(encoding='utf-8-sig'))
    if r['version']!=VERSION or r['approval_required'] is not True or r['primary_market']!='under_3_5':raise ValueError('Invalid totals registry')
    source=REGISTRY.parent/r['source'];data=json.loads(source.read_text(encoding='utf-8'))
    if hashlib.sha256(source.read_bytes().replace(b'\r\n',b'\n')).hexdigest()!=r['source_sha256']:raise ValueError('Changed nomination evidence')
    pick=next(x for x in data['development_choices'] if x['league']=='ALL' and x['family']=='totals' and x['market']=='under_3_5')
    if pick['selected_on_development']!='totals_opening_anchor':raise ValueError('Totals nomination mismatch')
    return r,registry_hash(r)


def decision(row,matrix,inputs,clock,r):
    from forward_trial_basis import legacy_basis, provenance
    row=legacy_basis(row)
    from performance_tracking import utc,number
    from football_value_pipeline_v2_standalone import canonical_team_key,devig,reweight_matrix_to_1x2
    from historical_benchmark import adjusted_matrix,anchor_totals,goals
    from benchmark_forward_experiment import secondary,simplex
    reasons=[];kick=utc(row.get('kickoff_utc'));inputs=inputs if isinstance(inputs,dict) else {};ref=inputs.get('reference');ref=ref if isinstance(ref,dict) else {}
    if row.get('league') not in r['leagues']:reasons.append('outside_registered_leagues')
    if kick is None or not 1200<=(kick-clock).total_seconds()<=72*3600:reasons.append('outside_forecast_window')
    if row.get('odds_source')!='The Odds API':reasons.append('no_live_odds')
    weight=number(row.get('market_weight'),min_value=0,max_value=1)
    if weight is None or abs(weight-r['baseline_market_weight'])>1e-12 or row.get('market_blend_applied') not in (True,1,'True'):reasons.append('production_basis_changed')
    from benchmark_forward_experiment import production_version_reasons
    reasons+=production_version_reasons(row)
    if row.get('totals_anchor_applied') in (True,1,'True'):reasons.append('candidate_adopted_in_production')
    if any(number(row.get(k),min_value=90,max_value=100) is None for k in ('home_name_match_score','away_name_match_score')) or any(row.get(k) in (None,'','__LEAGUE_AVERAGE__') for k in ('model_home_team','model_away_team')):reasons.append('unreliable_model_identity')
    if ref.get('bookmaker')!='pinnacle' or str(ref.get('event_id'))!=str(row.get('odds_event_id')):reasons.append('missing_pinnacle_reference')
    rk=utc(ref.get('kickoff_utc'))
    if not rk or not kick or abs((rk-kick).total_seconds())>60 or any(canonical_team_key(str(ref.get(k,'')))!=canonical_team_key(str(row.get(k,''))) for k in ('home_team','away_team')):reasons.append('reference_fixture_mismatch')
    updated=utc(ref.get('updated_at_utc'))
    if updated is None or not 0<=(clock-updated).total_seconds()<=r['quote_max_age_seconds']:reasons.append('reference_stale_or_future')
    hda_updated=utc(row.get('odds_h2h_last_update_utc'))
    if hda_updated is None or not 0<=(clock-hda_updated).total_seconds()<=r['quote_max_age_seconds'] or (updated is not None and abs((hda_updated-updated).total_seconds())>r['maximum_1x2_totals_skew_seconds']):reasons.append('stale_or_unsynchronized_production_hda')
    prices=[number(ref.get(k),min_value=1.000001) for k in ('over','under')]
    if any(x is None for x in prices) or not .98<=sum(1/x for x in prices)<=1.20:reasons.append('incoherent_totals_prices')
    candidate=baseline=None;scale=target=None
    try:
        p=simplex(row,'p_')
        if p is None:raise ValueError('HDA')
        base=secondary(row,matrix,p);baseline=base['baseline_goals']
        if baseline is None:raise ValueError('matrix')
        lam=float(inputs['lambda_home']);mu=float(inputs['lambda_away']);rho=float(inputs['rho']);n=int(inputs['max_goals'])
        from score_probability import SCORE_ENGINE_VERSION, MAX_SCORE_GRID, score_grid
        engine=inputs.get('score_engine_version')
        if engine not in (None,SCORE_ENGINE_VERSION):raise ValueError('unknown score engine')
        adaptive=engine==SCORE_ENGINE_VERSION
        if not all(math.isfinite(x) for x in (lam,mu,rho)) or min(lam,mu)<=0 or not 3<=n<=(MAX_SCORE_GRID if adaptive else 30):raise ValueError('parameters')
        if any(abs(float(row[k])-inputs[k])>1e-9 for k in ('lambda_home','lambda_away')):raise ValueError('intensity')
        reconstructed=reweight_matrix_to_1x2(adjusted_matrix(lam,mu,rho,n),p)
        if adaptive:
            checked,_=score_grid(lam,mu,rho,n)
            if checked.shape!=np.asarray(matrix).shape:raise ValueError('inadequate score grid')
        if not np.allclose(matrix,reconstructed,rtol=0,atol=1e-8):raise ValueError('model binding')
        if not reasons:
            target=float(devig(prices,method='power')[0]);anchored,scale=anchor_totals(lam,mu,rho,p,target,n,tail_bounded=adaptive);candidate=goals(anchored)
    except (ValueError,KeyError,TypeError,OverflowError):reasons.append('invalid_bound_model_or_solver')
    return {'status':'available' if candidate else 'unavailable','reasons':reasons,'baseline_goals':baseline,'candidate_goals':candidate,'scale':scale,'target_over_2_5':target,**provenance(row)}


def write_experiment(predictions,raw,generated,matrices,inputs):
    from performance_tracking import fixture_key,utc,write_json
    r,sha=registry();rows=[]
    for row in predictions.astype(object).where(predictions.notna(),None).to_dict('records'):
        key=fixture_key(row);m=matrices.get(key);model=inputs.get(key)
        from forward_trial_basis import bound_inputs
        m,model=bound_inputs(row,m,model)
        if isinstance(model,dict):model={**model,'reference':model.get('reference') if isinstance(model.get('reference'),dict) else None}
        rows.append({**{k:row.get(k) for k in ('league','home_team','away_team','kickoff_utc','fixture_id')},
            'production_matrix':None if m is None else m.tolist(),'model_inputs':model,
            **decision(row,m,model,utc(generated),r)})
    data={'version':VERSION,'registry':r,'registry_sha256':sha,'generated_at_utc':generated,
        'predictions_sha256':hashlib.sha256((raw/'all_leagues_predictions.csv').read_bytes()).hexdigest(),'rows':rows}
    write_json(raw/FILE,data);return data


def equivalent(a,b):
    if isinstance(a,bool) or isinstance(b,bool):return type(a)==type(b) and a==b
    if isinstance(a,dict) and isinstance(b,dict):return set(a)==set(b) and all(equivalent(a[k],b[k]) for k in a)
    if isinstance(a,list) and isinstance(b,list):return len(a)==len(b) and all(equivalent(x,y) for x,y in zip(a,b))
    if isinstance(a,(int,float)) and not isinstance(a,bool) and isinstance(b,(int,float)) and not isinstance(b,bool):return math.isfinite(a) and math.isfinite(b) and abs(a-b)<1e-9
    return a==b


def validate(data,generated,predictions,active=True):
    from benchmark_forward_experiment import registry_hash
    from performance_tracking import utc,fixture_key
    r=data['registry']
    if data.get('version')!=VERSION or data['registry_sha256']!=registry_hash(r) or (active and (r,data['registry_sha256'])!=registry()):raise ValueError('Totals registry binding')
    if utc(generated) is None or utc(data['generated_at_utc'])!=utc(generated):raise ValueError('Totals timestamp binding')
    originals={fixture_key(x):x for x in predictions};seen=set()
    for row in data['rows']:
        key=fixture_key(row)
        if key in seen or key not in originals:raise ValueError('Totals fixture binding')
        seen.add(key);expected=decision(originals[key],row.get('production_matrix'),row.get('model_inputs'),utc(generated),r)
        if any(not equivalent(row.get(k),v) for k,v in expected.items()):raise ValueError('Totals calculation binding')
    if seen!=set(originals):raise ValueError('Totals coverage binding')


def capture_file(raw,generated):
    from performance_tracking import load_json,read_csv
    from forecast_integrity import forecast_digest_variants
    path=raw/FILE
    if not path.exists():return None
    d=load_json(path,{});validate(d,generated,read_csv(raw/'all_leagues_predictions.csv'))
    if d['predictions_sha256'] not in forecast_digest_variants(raw/'all_leagues_predictions.csv'):raise ValueError('Totals forecast digest')
    return path


def evaluate(root,archive,records,clock):
    from performance_tracking import load_json,utc,fixture_key,fixture_match
    from forecast_integrity import forecast_digest_variants, snapshot_generated_at
    from historical_benchmark import metrics,score
    from benchmark_forward_experiment import block_interval,excluded_reasons
    r,sha=registry();observations={};rejected=[]
    for meta,predictions,_ in archive:
        directory=root/'performance/snapshots'/meta['git_commit_sha'][:16];path=directory/FILE;digest=meta.get('sha256',{}).get(FILE)
        if not digest:continue
        try:
            if hashlib.sha256(path.read_bytes()).hexdigest()!=digest:raise ValueError('Digest')
            d=load_json(path,{});validate(d,snapshot_generated_at(directory,meta),predictions,False)
            if d['predictions_sha256'] not in forecast_digest_variants(directory/'predictions.csv'):raise ValueError('Forecast digest')
        except (ValueError,KeyError,TypeError,OSError):rejected.append(meta['git_commit_sha']);continue
        if d['registry_sha256']!=sha:continue
        generated=utc(d['generated_at_utc']);captured=utc(meta['captured_at_utc'])
        if generated.date().isoformat()<r['registered_on']:continue
        for row in d['rows']:
            kick=utc(row['kickoff_utc'])
            if kick and max(generated,captured)<=kick-timedelta(minutes=20) and kick<=generated+timedelta(hours=72):observations.setdefault(fixture_key(row),{**row,'snapshot_commit':meta['git_commit_sha']})
    records=[x for x in records if x.get('source_status')=='FINISHED' and x.get('source')=='football-data.org/v4'];graded=[];coverage=[];verified=0
    for row in observations.values():
        match,state=fixture_match(row,records)
        if utc(row['kickoff_utc'])>clock-timedelta(hours=2):match=None;state='PENDING_KICKOFF_OR_FINAL_SCORE'
        coverage.append({**row,'result_status':state})
        if not match or row['league'] not in r['leagues']:continue
        verified+=1
        if row['status']!='available':continue
        year,week,_=utc(row['kickoff_utc']).isocalendar();item={**row,'home_goals':match['home_goals'],'away_goals':match['away_goals'],'source_match_id':match['match_id'],'week':f'{year}-W{week:02d}'}
        losses={v:score({**row[v+'_goals'],'home_goals':item['home_goals'],'away_goals':item['away_goals']},r['primary_market']) for v in ('baseline','candidate')}
        item['log_loss_gain']=losses['baseline']['log_loss']-losses['candidate']['log_loss'];graded.append(item)
    def comparison(items):
        return {m:{v:metrics([{**x[v+'_goals'],'home_goals':x['home_goals'],'away_goals':x['away_goals']} for x in items],m) for v in ('baseline','candidate')} for m in r['markets']}
    c=comparison(graded);interval=block_interval(graded,r);weeks=len({x['week'] for x in graded});fraction=len(graded)/verified if verified else None;g=r['review_gates'];enough=len(graded)>=g['minimum_paired_fixtures'] and weeks>=g['minimum_gameweeks'];quality=fraction is not None and fraction>=g['minimum_verified_coverage'] and not rejected
    supports=enough and quality and interval is not None and interval[0]>0 and all(c[m]['candidate']['brier']<=c[m]['baseline']['brier'] and c[m]['candidate']['log_loss']<=c[m]['baseline']['log_loss'] for m in r['markets'])
    summary={'version':VERSION,'registry_sha256':sha,'candidate_id':r['candidate_id'],'reviewed_at_utc':clock.isoformat(),'paired_fixtures':len(graded),'gameweeks':weeks,'verified_coverage':fraction,'observed_fixtures':len(observations),'comparison':c,'by_league':{l:comparison([x for x in graded if x['league']==l]) for l in r['leagues']},'primary_log_loss_gain_week_block95':interval,'excluded_forecast_reasons':excluded_reasons(observations.values()),'rejected_snapshot_commits':rejected,'review_gates':g,'status':'READY_FOR_REVIEW' if enough and quality else 'DATA_QUALITY_BLOCKED' if enough else 'COLLECT_MORE_DATA','evidence':'SUPPORTS_FORECASTING_REVIEW' if supports else 'NO_CLEAR_PROMOTION_EVIDENCE','automatic_production_change':False,'note':'Separate proportional intensity scaling to fresh Pinnacle O/U 2.5, fitted rho and production HDA preserved. Primary Under 3.5 log loss; other markets are guardrails. No bets, automatic promotion or backfill.'}
    return summary,graded,coverage


def review_experiment(root,archive,records,clock):
    from performance_tracking import write_json
    s,g,c=evaluate(root,archive,records,clock);dest=root/'performance/totals_anchor_experiment'
    for directory in (dest,dest/'versions'/s['registry_sha256']):
        write_json(directory/'summary.json',s);write_json(directory/'graded.json',g);write_json(directory/'coverage.json',c)
    (dest/'report.md').write_text('# Pinnacle totals anchoring trial\n\n'+s['note']+'\n\nStatus: '+s['status']+'; paired fixtures: '+str(len(g))+'; gameweeks: '+str(s['gameweeks'])+'\n\nExcluded forecasts by reason: '+(', '.join(f'{k}: {v}' for k,v in s['excluded_forecast_reasons'].items()) or 'none')+'\n\n'+json.dumps(s['comparison'],indent=2)+'\n',encoding='utf-8');return s


def validate_report(root):
    from performance_tracking import load_json,snapshots,utc
    dest=root/'performance/totals_anchor_experiment';actual=load_json(dest/'summary.json',{});expected,g,c=evaluate(root,snapshots(root),list(load_json(root/'performance/verified_results.json',{}).values()),utc(actual['reviewed_at_utc']))
    if actual!=expected or load_json(dest/'graded.json',[])!=g or load_json(dest/'coverage.json',[])!=c:raise ValueError('Totals report evidence mismatch')
    return True
