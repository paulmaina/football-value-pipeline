"""Raw goal-probability recency research, embedded in the existing goal sidecar."""
from collections import Counter
from datetime import timedelta
import hashlib
import math
import numpy as np
import pandas as pd

VERSION = 'goal-recency-shadow-v1'
MARKETS = {'over_1_5': 'Over 1.5', 'btts_yes': 'Both Teams to Score - Yes'}


def variant_name(half):
    return 'half_life_'+format(float(half), '.15g')


def goal_probabilities(matrix):
    matrix = np.asarray(matrix, dtype=float)
    if (matrix.ndim != 2 or not matrix.size or not np.isfinite(matrix).all()
            or (matrix < 0).any() or abs(float(matrix.sum())-1) > 1e-6):
        raise ValueError('Invalid scoreline probability matrix')
    h,a = np.indices(matrix.shape)
    return {'over_1_5': float(matrix[h+a >= 2].sum()), 'btts_yes': float(matrix[1:,1:].sum())}


def binary_metrics(probabilities, outcomes):
    n = len(probabilities)
    if not n:
        return {'n': 0, 'brier': None, 'log_loss': None, 'mean_probability': None, 'event_rate': None}
    loss = [-math.log(max(min(p,1-1e-12),1e-12) if y else max(min(1-p,1-1e-12),1e-12))
            for p,y in zip(probabilities,outcomes)]
    return {'n': n, 'brier': sum((p-y)**2 for p,y in zip(probabilities,outcomes))/n,
            'log_loss': sum(loss)/n, 'mean_probability': sum(probabilities)/n, 'event_rate': sum(outcomes)/n}


def fold_diagnostic(origin, train, test, rows):
    data = {'origin': origin.isoformat(), 'training_end': pd.to_datetime(train.Date).max().isoformat(),
            'test_start': pd.to_datetime(test.Date).min().isoformat(),
            'test_end': pd.to_datetime(test.Date).max().isoformat(), 'n': len(rows),
            'one_x_two_log_loss': sum(r['one_x_two_log_loss'] for r in rows)/len(rows), 'markets': {}}
    data['one_x_two_brier']=sum(r['one_x_two_brier'] for r in rows)/len(rows)
    for key in MARKETS:
        data['markets'][key] = binary_metrics([r[key] for r in rows], [r['y_'+key] for r in rows])
    return data


def aggregate_folds(folds, market=None):
    n = sum(f['n'] for f in folds)
    if market is None:
        return {'n': n, 'log_loss': sum(f['n']*f['one_x_two_log_loss'] for f in folds)/n if n else None,
                'brier':sum(f['n']*f['one_x_two_brier'] for f in folds)/n if n else None}
    names = ('brier','log_loss','mean_probability','event_rate')
    return {'n': n, **{name:sum(f['n']*f['markets'][market][name] for f in folds)/n if n else None for name in names}}


def historical_audit(tuning):
    """Select on early folds only; later folds never choose a goal half-life."""
    candidates = [c for c in tuning.get('candidates',[]) if c.get('valid') and c.get('recency_folds')]
    result = {'status':'INSUFFICIENT_HISTORY', 'selection_metric':'development_binary_log_loss',
              'markets':{}, 'minimum_matches_per_phase':tuning.get('min_validation_matches',25)}
    if not candidates or len(candidates[0]['recency_folds']) < 3:
        return result
    nfold = len(candidates[0]['recency_folds']); split = max(1,min(nfold-1,2*nfold//3))
    origins = [f['origin'] for f in candidates[0]['recency_folds']]
    # Missing or mismatched diagnostics cannot create unequal candidate samples.
    if any([f['origin'] for f in c['recency_folds']] != origins for c in candidates):
        return result
    result.update(development_folds=split, audit_folds=nfold-split,
        audit_start=origins[split], production_half_life=tuning.get('selected_half_life_days'),
        note='Goal and comparison 1X2 selectors use development folds only. Production tuning uses the whole tuning period and is assessed independently in forward snapshots.')
    for c in candidates:
        for f in c['recency_folds']:
            if not pd.Timestamp(f['training_end']) < pd.Timestamp(f['origin']) <= pd.Timestamp(f['test_start']):
                raise ValueError('Historical recency diagnostic violates chronological boundaries')
    baseline = min(candidates,key=lambda c:(aggregate_folds(c['recency_folds'][:split])['log_loss'],
        aggregate_folds(c['recency_folds'][:split])['brier'],c['half_life_days']))
    result['development_1x2_half_life'] = baseline['half_life_days']
    minimum = result['minimum_matches_per_phase']
    for key in MARKETS:
        ranking = sorted(candidates,key=lambda c:(aggregate_folds(c['recency_folds'][:split],key)['log_loss'],
            aggregate_folds(c['recency_folds'][:split],key)['brier'],c['half_life_days']))
        best = ranking[0]; dev = aggregate_folds(best['recency_folds'][:split],key)
        audit = aggregate_folds(best['recency_folds'][split:],key)
        control = aggregate_folds(baseline['recency_folds'][split:],key)
        winners = Counter()
        for i in range(split):
            winner = min(candidates,key=lambda c:(c['recency_folds'][i]['markets'][key]['log_loss'],c['half_life_days']))
            winners[str(winner['half_life_days'])] += 1
        supported = dev['n'] >= minimum and audit['n'] >= minimum
        result['markets'][key] = {'status':'AUDIT_COMPLETE' if supported else 'INSUFFICIENT_HISTORY',
            'selected_half_life_days': best['half_life_days'] if supported else None,
            'development':dev, 'audit':audit, 'development_1x2_audit':control,
            'audit_brier_gain':control['brier']-audit['brier'],
            'audit_log_loss_gain':control['log_loss']-audit['log_loss'],
            'development_log_loss_margin': aggregate_folds(ranking[1]['recency_folds'][:split],key)['log_loss']-dev['log_loss'] if len(ranking)>1 else None,
            'development_fold_winners':dict(winners),
            'candidate_phase_scores':[{'half_life_days':c['half_life_days'],
                'development':aggregate_folds(c['recency_folds'][:split],key),
                'audit':aggregate_folds(c['recency_folds'][split:],key)} for c in candidates]}
    result['status'] = 'AUDIT_COMPLETE' if all(m['status']=='AUDIT_COMPLETE' for m in result['markets'].values()) else 'INSUFFICIENT_HISTORY'
    return result


def generate_league(predictions, history, model_class, tuning, *, league, production_half_life, l2, max_goals, as_of=None):
    """Fit alternates on the exact production history; no provider/odds requests."""
    options = sorted({float(c['half_life_days']) for c in tuning['candidates']})
    if not options or any(not math.isfinite(h) or h <= 0 for h in options):
        raise ValueError('Invalid recency candidates')
    audit = historical_audit(tuning); fitted = {}; failures = {}
    for half in options:
        if half == production_half_life:
            continue
        try:
            model = model_class(half_life_days=half,l2=l2,max_goals=max_goals).fit(history.copy(deep=True),
                **({'as_of': pd.Timestamp(as_of)} if as_of is not None else {}))
            from football_value_pipeline_v2_standalone import LEAGUES
            model.league_key = next((c.key for c in LEAGUES.values() if c.name == league), None)
            fit = getattr(model,'fit_result',None)
            if fit is not None and not fit.success:
                raise ValueError('Optimizer did not converge')
            fitted[half] = model
        except (ValueError,RuntimeError,FloatingPointError) as exc:
            failures[variant_name(half)] = type(exc).__name__
    rows = []
    for source in predictions.astype(object).where(predictions.notna(),None).to_dict('records'):
        probabilities = {}; errors = dict(failures)
        for half,model in fitted.items():
            try:
                matrix,meta = model.score_matrix(str(source['home_team']),str(source['away_team']))
                if min(float(meta.get('home_name_match_score',0)),float(meta.get('away_name_match_score',0))) < 90:
                    raise ValueError('Unknown or unreliable team mapping')
                probabilities[half] = goal_probabilities(matrix)
            except (ValueError,RuntimeError,FloatingPointError,TypeError) as exc:
                errors[variant_name(half)] = type(exc).__name__
        for key in MARKETS:
            from performance_tracking import number
            baseline = number(source.get('raw_p_'+key),min_value=0,max_value=1)
            reliable = all(source.get(k) not in (None,'__LEAGUE_AVERAGE__') for k in ('model_home_team','model_away_team'))
            reliable = reliable and min(number(source.get(k)) or 0 for k in ('home_name_match_score','away_name_match_score')) >= 90
            variants = {'production_raw':baseline} if baseline is not None and reliable else {}
            halves = {'production_raw':production_half_life}
            for half in options:
                value = baseline if half == production_half_life else probabilities.get(half,{}).get(key)
                if variants and value is not None:
                    variants[variant_name(half)] = value; halves[variant_name(half)] = half
            for name,half in [('goal_selected',audit.get('markets',{}).get(key,{}).get('selected_half_life_days')),
                              ('development_1x2',audit.get('development_1x2_half_life'))]:
                if half is not None and variant_name(half) in variants:
                    variants[name] = variants[variant_name(half)]; halves[name] = half
            rows.append({**{k:source.get(k) for k in ('league','home_team','away_team','kickoff_utc')},
                'market':key, 'status':'available' if len(variants)>1 else 'unavailable',
                'reasons':[] if variants else ['missing_raw_probability_or_unreliable_team'],
                'variants':variants, 'half_lives':halves, 'candidate_errors':errors})
    canonical = history[['Date','HomeTeam','AwayTeam','FTHG','FTAG']].to_csv(index=False,lineterminator='\n').encode('utf-8')
    return {'league':league,'training_end':pd.to_datetime(history.Date).max().isoformat(),
        'training_matches':len(history),'training_sha256':hashlib.sha256(canonical).hexdigest(),
        'production_half_life_days':production_half_life,'l2':l2,'max_goals':max_goals,
        'training_as_of_utc':None if as_of is None else pd.Timestamp(as_of).isoformat(),
        'candidate_fit_errors':failures,
        'historical_diagnostic_errors':{variant_name(c['half_life_days']):c['recency_diagnostics_error'] for c in tuning['candidates'] if c.get('recency_diagnostics_error')},
        'historical_audit':audit,'rows':rows}


def assemble(parts, generated_at):
    from performance_tracking import utc
    clock = utc(generated_at)
    if clock is None:
        raise ValueError('Invalid recency generation time')
    rows=[]; leagues=[]
    for part in parts:
        leagues.append({k:v for k,v in part.items() if k!='rows'})
        for row in part['rows']:
            row = {**row, 'generated_at_utc':generated_at}
            kickoff=utc(row.get('kickoff_utc'))
            trained=utc(part['training_end'])
            if trained is None:
                trained=pd.Timestamp(part['training_end']).tz_localize('UTC').to_pydatetime()
            if trained > clock:
                raise ValueError('Recency history contains future training results')
            if kickoff is None or clock >= kickoff-timedelta(minutes=20):
                row.update(status='unavailable',variants={},reasons=[*row['reasons'],'insufficient_lead_time'])
            rows.append(row)
    return {'version':VERSION,'generated_at_utc':generated_at,'leagues':leagues,'rows':rows,
        'probability_basis':'raw Dixon-Coles; same-history fits; no bookmaker blend or calibration',
        'selection_policy':'none; no paper bets, ROI or automatic promotion',
        'sample_policy':'first eligible recency snapshot per fixture-market; missing variants stay missing'}


def valid_extension(data, generated_at):
    from performance_tracking import utc,number,fixture_key
    if not isinstance(data,dict) or data.get('version') != VERSION or data.get('generated_at_utc') != generated_at:
        return False
    if not isinstance(data.get('rows'),list) or not isinstance(data.get('leagues'),list):
        return False
    seen=set()
    for row in data['rows']:
        if not isinstance(row,dict) or row.get('status') not in ('available','unavailable'):
            return False
        key=(fixture_key(row),row.get('market'))
        if key in seen or row.get('market') not in MARKETS or not utc(row.get('kickoff_utc')):
            return False
        seen.add(key)
        variants=row.get('variants',{})
        if not isinstance(variants,dict) or any(number(p,min_value=0,max_value=1) is None for p in variants.values()):
            return False
        if variants and 'production_raw' not in variants:
            return False
        halves=row.get('half_lives',{})
        if not isinstance(halves,dict) or any(number(halves.get(k),min_value=1e-12) is None for k in variants):
            return False
    return True


def paired_comparison(rows):
    metrics=binary_metrics([r['probability'] for r in rows],[r['outcome'] for r in rows])
    metrics['overconfidence']=metrics['mean_probability']-metrics['event_rate']
    for metric in ('brier','log_loss'):
        gains=[r['baseline_'+metric]-r[metric] for r in rows]
        mean=sum(gains)/len(gains)
        se=math.sqrt(sum((g-mean)**2 for g in gains)/(len(gains)-1)/len(gains)) if len(gains)>1 else None
        metrics['paired_'+metric+'_gain']=mean
        metrics['paired_'+metric+'_gain_approx95']= [mean-1.96*se,mean+1.96*se] if se is not None else None
    metrics['assessment']='COLLECT_MORE_DATA' if len(rows)<30 else 'REVIEW_ON_LATER_HOLDOUT'
    edges=(0,.5,.6,.7,.8,.9,1.0000001)
    metrics['calibration']=[]
    for low,high in zip(edges,edges[1:]):
        group=[r for r in rows if low <= r['probability'] < high]
        if group:
            m=binary_metrics([r['probability'] for r in group],[r['outcome'] for r in group])
            n=m['n'];q=m['event_rate'];z=1.96
            centre=(q+z*z/(2*n))/(1+z*z/n)
            radius=z*math.sqrt(q*(1-q)/n+z*z/(4*n*n))/(1+z*z/n)
            metrics['calibration'].append({'probability_band':f'{low:.0%}-{min(high,1):.0%}',
                **m,'observed_wilson95':[max(0,centre-radius),min(1,centre+radius)]})
    return metrics


def frozen_recency(root, archived):
    from performance_tracking import load_json,utc,fixture_key,fixture_match,result_for_market,write_json,write_csv
    frozen={}; audits=[]; rejected=[]
    for meta,predictions,_ in archived:
        directory=root/'performance/snapshots'/meta['git_commit_sha'][:16]
        path=directory/'goal_blend_experiment.json'; expected=meta.get('sha256',{}).get(path.name)
        if not expected or not path.exists() or hashlib.sha256(path.read_bytes()).hexdigest()!=expected:
            continue
        parent=load_json(path,{});data=parent.get('recency_experiment')
        if data is None: continue
        if not valid_extension(data,parent.get('generated_at_utc')):
            rejected.append(meta['git_commit_sha']);continue
        generated,captured=utc(data['generated_at_utc']),utc(meta['captured_at_utc'])
        parent_generated=utc(meta.get('generated_at_utc'))
        if generated is None or parent_generated is None or abs((generated-parent_generated).total_seconds())>=1:
            rejected.append(meta['git_commit_sha']);continue
        originals={fixture_key(r):r for r in predictions}
        audits.append({'snapshot_commit':meta['git_commit_sha'],'leagues':data['leagues']})
        for row in data['rows']:
            kick=utc(row['kickoff_utc']);key=fixture_key(row)
            if max(generated,captured)>=kick-timedelta(minutes=20):continue
            original=originals.get(key)
            if original is None:continue
            control=row['variants'].get('production_raw')
            if control is not None:
                from performance_tracking import number
                expected_control=number(original.get('raw_p_'+row['market']))
                if expected_control is None or abs(control-expected_control)>1e-9:
                    rejected.append(meta['git_commit_sha']);continue
            frozen.setdefault((key,row['market']),{**row,'snapshot_commit':meta['git_commit_sha']})
    return frozen,audits,rejected


def review_experiment(root, archived, records, clock):
    from performance_tracking import utc,fixture_match,result_for_market,write_json,write_csv
    frozen,audits,rejected=frozen_recency(root,archived)
    if not frozen and not rejected:return
    scored=[];coverage=[]
    for row in frozen.values():
        match,state=fixture_match(row,records)
        if utc(row['kickoff_utc'])>clock-timedelta(hours=2):match=None;state='PENDING_KICKOFF_OR_FINAL_SCORE'
        coverage.append({**{k:row[k] for k in ('league','home_team','away_team','kickoff_utc','market','snapshot_commit')},
            'availability':row['status'],'result_status':state,'available_variants':','.join(row['variants']),
            'reasons':';'.join(row.get('reasons',[])),'candidate_errors':str(row.get('candidate_errors',{}))})
        if not match or not row['variants']:continue
        y=int(result_for_market(MARKETS[row['market']],match['home_goals'],match['away_goals']))
        base=binary_metrics([row['variants']['production_raw']],[y])
        for name,p in row['variants'].items():
            value=binary_metrics([p],[y]);scored.append({**{k:row[k] for k in ('league','home_team','away_team','kickoff_utc','market','snapshot_commit')},
                'variant':name,'half_life_days':row['half_lives'].get(name),'probability':p,'outcome':y,
                'brier':value['brier'],'log_loss':value['log_loss'],
                'baseline_brier':base['brier'],'baseline_log_loss':base['log_loss'],
                'source_match_id':match['match_id'],'match_source':'football-data.org/v4'})
            year,week,_=utc(row['kickoff_utc']).isocalendar()
            scored[-1]['week']=f'{year}-W{week:02d}'
    comparisons=[]
    for league in ['ALL',*sorted({r['league'] for r in scored})]:
        for key in MARKETS:
            cohort=[r for r in scored if r['market']==key and (league=='ALL' or r['league']==league)]
            for name in sorted({r['variant'] for r in cohort}):
                comparisons.append({'league':league,'market':key,'variant':name,
                    **paired_comparison([r for r in cohort if r['variant']==name])})
    dest=root/'performance/recency_experiment'
    weekly=[]
    for week in sorted({r['week'] for r in scored}):
        for key in MARKETS:
            cohort=[r for r in scored if r['week']==week and r['market']==key]
            for name in sorted({r['variant'] for r in cohort}):
                weekly.append({'week':week,'market':key,'variant':name,
                    **paired_comparison([r for r in cohort if r['variant']==name])})
    summary={'version':VERSION,'reviewed_at_utc':clock.isoformat(),'total_fixture_markets':len(frozen),
        'available_fixture_markets':sum(bool(r['variants']) for r in frozen.values()),
        'graded_fixture_markets':len({(r['league'],r['home_team'],r['away_team'],r['kickoff_utc'],r['market']) for r in scored}),
        'comparisons':comparisons,'weekly_comparisons':weekly,'historical_audits':audits,'rejected_snapshot_commits':sorted(set(rejected)),
        'note':'Same-snapshot raw baseline; paired available variants, not identical cohorts across variants. Historical audit periods overlap across runs and must not be added together. Approximate intervals assume independent fixtures, do not adjust for multiple comparisons and do not prove profitability. No automatic promotion.'}
    write_json(dest/'summary.json',summary)
    write_csv(dest/'graded.csv',scored,['league','home_team','away_team','kickoff_utc','market','snapshot_commit','variant','half_life_days','probability','outcome','brier','log_loss','baseline_brier','baseline_log_loss','source_match_id','match_source','week'])
    write_csv(dest/'coverage.csv',coverage,['league','home_team','away_team','kickoff_utc','market','snapshot_commit','availability','result_status','available_variants','reasons','candidate_errors'])
    lines=['# Goal recency experiment','',summary['note'],'',
        f"Coverage: {summary['available_fixture_markets']}/{len(frozen)} fixture-markets; {summary['graded_fixture_markets']} graded.",
        f"Rejected snapshot data: {len(summary['rejected_snapshot_commits'])} commit(s); details in summary.json.",'',
        '| League | Market | Variant | N | Brier | Log loss | Brier gain | Log-loss gain | Overconfidence |',
        '|---|---|---|---:|---:|---:|---:|---:|---:|']
    for r in comparisons:
        lines.append(f"| {r['league']} | {r['market']} | {r['variant']} | {r['n']} | {r['brier']:.4f} | {r['log_loss']:.4f} | {r['paired_brier_gain']:+.4f} | {r['paired_log_loss_gain']:+.4f} | {r['overconfidence']:+.1%} |")
    lines += ['', 'Positive paired gain means lower error than the raw production model on those same matches. A 30-match review prompt is not statistical proof.','',
        'Calibration buckets, approximate paired-gain intervals, gameweek comparisons and historical selection stability for each frozen run are retained in summary.json. Historical audits overlap and are not additional forward samples.','',
        '## Latest historical development/audit diagnostics','',
        '| League | Market | Goal half-life | Development N | Audit N | Audit log-loss gain | Development fold wins |',
        '|---|---|---:|---:|---:|---:|---|']
    if audits:
        for league in audits[-1]['leagues']:
            for key,m in league.get('historical_audit',{}).get('markets',{}).items():
                lines.append(f"| {league['league']} | {key} | {m['selected_half_life_days']} | {m['development']['n']} | {m['audit']['n']} | {m['audit_log_loss_gain']:+.4f} | {m['development_fold_winners']} |")
    (dest/'report.md').write_text('\n'.join(lines),encoding='utf-8')
    return summary


def validate_report(root):
    """Reconcile reported scores and cohorts with frozen variants/verified results."""
    from performance_tracking import load_json,read_csv,snapshots,utc,fixture_key,fixture_match,result_for_market,number
    dest=root/'performance/recency_experiment';summary=load_json(dest/'summary.json',{})
    clock=utc(summary.get('reviewed_at_utc'))
    def require(value,message):
        if not value:raise ValueError('Recency report: '+message)
    def equal(actual,expected):
        if isinstance(expected,dict):
            require(isinstance(actual,dict) and set(actual)==set(expected),'metric fields differ')
            for key,value in expected.items():equal(actual[key],value)
        elif isinstance(expected,list):
            require(isinstance(actual,list) and len(actual)==len(expected),'metric list differs')
            for a,b in zip(actual,expected):equal(a,b)
        elif isinstance(expected,(float,int)):
            value=number(actual)
            require(value is not None and abs(value-expected)<1e-8,'score/calibration aggregate differs')
        else:require(actual==expected,'metric label differs')
    require(clock is not None and summary.get('version')==VERSION,'invalid version/review time')
    frozen,audits,rejected=frozen_recency(root,snapshots(root))
    records=list(load_json(root/'performance/verified_results.json',{}).values())
    expected={}
    for key,row in frozen.items():
        match,_=fixture_match(row,records)
        if not match or utc(row['kickoff_utc'])>clock-timedelta(hours=2):continue
        require(match.get('source_status')=='FINISHED' and match.get('source')=='football-data.org/v4','unverified source cache')
        y=int(result_for_market(MARKETS[row['market']],match['home_goals'],match['away_goals']))
        for variant,p in row['variants'].items():
            expected[(key,variant)]=(row,p,y,match)
    graded=read_csv(dest/'graded.csv');seen=set();numeric=[]
    for r in graded:
        key=((fixture_key(r),r['market']),r['variant'])
        require(key not in seen and key in expected,'unexpected/duplicate variant')
        seen.add(key);original,p,y,match=expected[key]
        require(r['snapshot_commit']==original['snapshot_commit'],'snapshot provenance differs')
        equal(number(r['half_life_days']),original['half_lives'][r['variant']])
        equal(number(r['probability']),p);equal(number(r['outcome']),y)
        require(r['source_match_id']==str(match['match_id']) and r['match_source']=='football-data.org/v4','result provenance differs')
        values=binary_metrics([p],[y]);control=binary_metrics([original['variants']['production_raw']],[y])
        for field in ('brier','log_loss'):
            equal(number(r[field]),values[field]);equal(number(r['baseline_'+field]),control[field])
        year,week,_=utc(r['kickoff_utc']).isocalendar();require(r['week']==f'{year}-W{week:02d}','gameweek differs')
        numeric.append({**r,**{k:float(r[k]) for k in ('probability','outcome','brier','log_loss','baseline_brier','baseline_log_loss')}})
    require(seen==set(expected),'graded cohort omitted or added variants')
    coverage=read_csv(dest/'coverage.csv');keys=[(fixture_key(r),r['market']) for r in coverage]
    require(len(keys)==len(set(keys)) and set(keys)==set(frozen),'coverage differs from first observations')
    for r,key in zip(coverage,keys):
        require(r['availability']==frozen[key]['status'] and r['snapshot_commit']==frozen[key]['snapshot_commit'],'availability provenance differs')
    require(summary['total_fixture_markets']==len(frozen),'total count differs')
    require(summary['available_fixture_markets']==sum(bool(r['variants']) for r in frozen.values()),'available count differs')
    require(summary['graded_fixture_markets']==len({key[0] for key in expected}),'graded count differs')
    require(summary['historical_audits']==audits and summary['rejected_snapshot_commits']==sorted(set(rejected)),'historical audit provenance differs')
    for field,dimension in [('comparisons','league'),('weekly_comparisons','week')]:
        groups={}
        for r in numeric:
            labels=[r[dimension]]+(['ALL'] if dimension=='league' else [])
            for label in labels:groups.setdefault((label,r['market'],r['variant']),[]).append(r)
        actual=summary[field];actual_keys=[(r[dimension],r['market'],r['variant']) for r in actual]
        require(len(actual_keys)==len(set(actual_keys)) and set(actual_keys)==set(groups),'comparison cohorts differ')
        for r,key in zip(actual,actual_keys):
            metrics=paired_comparison(groups[key])
            equal({k:r.get(k) for k in metrics},metrics)
    return {'graded_variants':len(graded),'fixture_markets':len(frozen)}
