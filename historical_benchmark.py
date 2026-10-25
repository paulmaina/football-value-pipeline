"""Reproducible offline diagnostics; no network, API keys, production writes or bets."""
from __future__ import annotations
import argparse
from collections import Counter
from datetime import datetime, timezone
import hashlib
import io
import json
import math
from pathlib import Path
import platform
import re
import subprocess

import numpy as np
import pandas as pd
import league_registry
from scipy.optimize import brentq
from scipy.stats import poisson

VERSION = 'historical-dc-benchmark-v2'
SUPPORTED_VERSIONS = ('historical-dc-benchmark-v1', VERSION)
CODES = league_registry.divisions()
GOALS = ('over_1_5','under_3_5','btts_yes','over_2_5')
BASE = 'blend_50_fixed_baseline'
# v2 model-upgrade comparison: production v1 replay, each change alone, full v2.
UPGRADE_BASE = 'production_v1'
UPGRADE_VARIANTS = (UPGRADE_BASE,'upgrade_market_weight_70','upgrade_half_life_480',
    'upgrade_pinnacle_ou25_anchor','upgrade_gated_shot_features','production_v2')
AH_LINES = (-2.5,-1.5,-1.0,0.0,1.0,1.5,2.5)


def ah_key(point):
    return f'ah_home_{point:+.1f}'


AH = tuple(ah_key(p) for p in AH_LINES)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_json(path, data):
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(data,indent=2,sort_keys=True,allow_nan=False)+'\n',encoding='utf-8')


def validate_config(cfg):
    if cfg.get('version') not in SUPPORTED_VERSIONS or not cfg.get('leagues') or any(l not in CODES for l in cfg['leagues']):
        raise ValueError('Invalid benchmark version/leagues')
    if cfg.get('input_manifest') and (Path(cfg['input_manifest']).name!=cfg['input_manifest'] or not re.fullmatch(r'[a-f0-9]{40}',cfg.get('dataset_source_commit',''))):
        raise ValueError('Invalid pinned dataset configuration')
    if len(set(cfg['leagues']))!=len(cfg['leagues']) or not cfg.get('seasons') or any(not re.fullmatch(r'\d{4}',s) for s in cfg['seasons']):
        raise ValueError('Invalid/duplicate league or season configuration')
    dates=[pd.Timestamp(cfg[k]) for k in ('test_start','audit_start','test_end_exclusive')]
    if not dates[0]<dates[1]<dates[2] or any(d.tzinfo is not None for d in dates):
        raise ValueError('Require increasing naive historical dates')
    if pd.Timestamp(cfg['prospective_validation_start'])<dates[2]:
        raise ValueError('Prospective validation cannot overlap historical evaluation')
    for key in ('step_days','min_train','max_goals','min_development_matches','min_audit_matches','min_pinnacle_comparison_matches'):
        value=cfg[key]
        if not isinstance(value,int) or isinstance(value,bool) or value<1:
            raise ValueError('Invalid positive integer '+key)
    if cfg['min_train']<30 or cfg['max_goals']<4:raise ValueError('Insufficient training/score grid')
    for key in ('baseline_half_life','baseline_l2'):
        if not math.isfinite(cfg[key]) or cfg[key]<=0:raise ValueError('Invalid '+key)
    for key in ('l2_candidates','half_life_candidates','market_weights'):
        if not isinstance(cfg[key],list) or len(set(cfg[key]))!=len(cfg[key]) or any(not math.isfinite(v) or v<=0 for v in cfg[key]):
            raise ValueError('Invalid research grid '+key)
    if any(v>=1 for v in cfg['market_weights']) or cfg['devig_method'] not in ('power','proportional'):
        raise ValueError('Invalid probability weight/de-vig method')
    upgrade=cfg.get('model_upgrade_comparison')
    if upgrade is not None:
        if cfg['version']!=VERSION or not isinstance(upgrade,dict):raise ValueError('Upgrade comparison requires the v2 benchmark')
        for name in ('production_v1','production_v2'):
            weight=upgrade.get(name,{}).get('market_weight')
            if isinstance(weight,bool) or not isinstance(weight,(int,float)) or not 0<weight<1:raise ValueError('Invalid upgrade market weight')
        half=upgrade['production_v2'].get('half_life_days')
        if isinstance(half,bool) or not isinstance(half,(int,float)) or not math.isfinite(half) or half<=0:raise ValueError('Invalid upgrade half-life')
        tuning=upgrade['production_v1'].get('half_life_tuning')
        if not isinstance(tuning,dict) or not tuning.get('candidates') or any(not v>0 for v in tuning['candidates']):
            raise ValueError('Invalid production half-life tuning replay')
    return cfg


def load_history(cache, league, cfg):
    sources=[];frames=[];excluded=Counter()
    for season in cfg['seasons']:
        path=cache/f'{season}_{CODES[league]}.csv'
        if not path.exists():raise FileNotFoundError(path)
        raw=path.read_bytes()
        try:content=raw.decode('utf-8-sig')
        except UnicodeDecodeError:content=raw.decode('latin1')
        frame=pd.read_csv(io.StringIO(content),on_bad_lines='error',low_memory=False)
        needed={'Date','HomeTeam','AwayTeam','FTHG','FTAG'}
        if needed-set(frame):raise ValueError('Missing training columns '+path.name)
        sources.append({'path':path.name,'sha256':hashlib.sha256(raw).hexdigest(),'rows':len(frame)})
        text_dates=frame['Date'].astype(str).str.strip()
        iso=text_dates.str.match(r'^\d{4}-\d{2}-\d{2}(?:$|T|\s)')
        dates=pd.Series(pd.NaT,index=frame.index,dtype='datetime64[ns]')
        dates.loc[iso]=pd.to_datetime(text_dates.loc[iso],format='ISO8601',errors='coerce')
        dates.loc[~iso]=pd.to_datetime(text_dates.loc[~iso],format='mixed',dayfirst=True,errors='coerce')
        if dates.isna().any():raise ValueError('Invalid historical date '+path.name)
        frame['Date']=dates.dt.normalize()
        hg=pd.to_numeric(frame.FTHG,errors='coerce');ag=pd.to_numeric(frame.FTAG,errors='coerce')
        missing=hg.isna()&ag.isna();excluded['unfinished_rows']+=int(missing.sum())
        invalid=(hg.isna()!=ag.isna())|((hg<0)|(ag<0)|(hg>20)|(ag>20)|(hg%1!=0)|(ag%1!=0))&~missing
        if invalid.any():raise ValueError('Invalid completed goals '+path.name)
        frame=frame.loc[~missing].copy()
        frame['FTHG']=hg[~missing].astype(int);frame['FTAG']=ag[~missing].astype(int)
        for field in ('HomeTeam','AwayTeam'):
            if frame[field].isna().any() or frame[field].astype(str).str.strip().eq('').any():raise ValueError('Missing team identity')
            frame[field]=frame[field].astype(str).str.strip()
        if (frame.HomeTeam==frame.AwayTeam).any():raise ValueError('Self fixture')
        frames.append(frame)
    data=pd.concat(frames,ignore_index=True,sort=False).sort_values(['Date','HomeTeam','AwayTeam']).reset_index(drop=True)
    if data.duplicated(['Date','HomeTeam','AwayTeam']).any():raise ValueError('Duplicate historical fixture')
    excluded['at_or_after_end']=int((data.Date>=pd.Timestamp(cfg['test_end_exclusive'])).sum())
    data=data.loc[data.Date<pd.Timestamp(cfg['test_end_exclusive'])].copy()
    return data,sources,dict(excluded)


def market_probabilities(row, fields, method):
    from football_value_pipeline_v2_standalone import devig
    try:prices=[float(row.get(k)) for k in fields]
    except (ValueError,TypeError):return None
    if any(not math.isfinite(v) or v<=1 for v in prices):return None
    if not .98<=sum(1/v for v in prices)<=1.20:return None
    p=devig(prices,method)
    if any(v is None or not math.isfinite(v) or not 0<v<1 for v in p):return None
    return np.array(p,dtype=float)


def adjusted_matrix(lam,mu,rho,max_goals):
    if min(lam,mu)<=0 or not all(math.isfinite(v) for v in (lam,mu,rho)):raise ValueError('Invalid goal parameters')
    corrections=((0,0,1-lam*mu*rho),(0,1,1+lam*rho),(1,0,1+mu*rho),(1,1,1-rho))
    if any(tau<=0 for _,_,tau in corrections):raise ValueError('Invalid low-score correction')
    grid=np.arange(max_goals+1)
    matrix=np.outer(poisson.pmf(grid,lam),poisson.pmf(grid,mu))
    for h,a,tau in corrections:matrix[h,a]*=tau
    if not np.isfinite(matrix).all() or matrix.sum()<=0:raise ValueError('Invalid score matrix')
    return matrix/matrix.sum()


def goals(matrix):
    h,a=np.indices(matrix.shape)
    return {'over_1_5':float(matrix[h+a>=2].sum()),'under_3_5':float(matrix[h+a<=3].sum()),
            'btts_yes':float(matrix[1:,1:].sum()),'over_2_5':float(matrix[h+a>=3].sum())}


def handicaps(matrix):
    """Home Asian handicap win probability; integer lines exclude the refund."""
    h,a=np.indices(matrix.shape);margin=h-a;out={}
    for point in AH_LINES:
        win=float(matrix[margin+point>0].sum());loss=float(matrix[margin+point<0].sum())
        out[ah_key(point)]=win/(win+loss) if win+loss>0 else None
    return out


def anchor_totals(lam,mu,rho,target_hda,target_over,max_goals,*,tail_bounded=False):
    """Scale fitted intensities; retain fitted rho and exact HDA target after reweighting.

    This constrained proportional scaling is NOT a joint parameter fit.
    Final matrix, after HDA reweighting, must match the O/U probability.
    """
    from football_value_pipeline_v2_standalone import reweight_matrix_to_1x2
    if not 0<target_over<1:raise ValueError('Invalid totals target')
    def matrix(scale):
        if tail_bounded:
            from score_probability import score_grid
            raw,_=score_grid(lam*scale,mu*scale,rho,max_goals)
        else:
            raw=adjusted_matrix(lam*scale,mu*scale,rho,max_goals)
        return reweight_matrix_to_1x2(raw,target_hda)
    points=[]
    for scale in np.geomspace(.2,4,22):
        try:points.append((float(scale),goals(matrix(scale))['over_2_5']-target_over))
        except ValueError:continue
    for (low,fl),(high,fh) in zip(points,points[1:]):
        if fl*fh<=0:
            scale=brentq(lambda s:goals(matrix(s))['over_2_5']-target_over,low,high,xtol=1e-10)
            result=matrix(scale)
            if abs(goals(result)['over_2_5']-target_over)>1e-7:raise ValueError('Totals solver mismatch')
            return result,float(scale)
    raise ValueError('No valid totals-scaling bracket')


def fitting_grid(cfg):
    baseline=(cfg['baseline_half_life'],cfg['baseline_l2'])
    return {'baseline':baseline,
        **{f'l2_{v:g}':(baseline[0],v) for v in cfg['l2_candidates']},
        **{f'half_life_{v:g}':(v,baseline[1]) for v in cfg['half_life_candidates']}}


def upgrade_spec(cfg):
    """variant -> (fitted model key, 1X2 market weight, Pinnacle O/U 2.5 anchor)."""
    upgrade=cfg.get('model_upgrade_comparison')
    if not upgrade:return {}
    old,new=upgrade['production_v1']['market_weight'],upgrade['production_v2']['market_weight']
    return {UPGRADE_BASE:('tuned',old,False),'upgrade_market_weight_70':('tuned',new,False),
        'upgrade_half_life_480':('fixed',old,False),'upgrade_pinnacle_ou25_anchor':('tuned',old,True),
        'upgrade_gated_shot_features':('tuned_shots',old,False),'production_v2':('fixed_shots',new,True)}


def fit_upgrade_models(train,origin,cfg,model_class,fold,errors):
    """Replay per-fold production tuning (v1) and fixed 480 days (v2), with/without shots."""
    upgrade=cfg.get('model_upgrade_comparison')
    if not upgrade:return {}
    from dc_decay_validation import tune_half_life
    t=upgrade['production_v1']['half_life_tuning']
    try:
        tuned=float(tune_half_life(history=train,model_class=model_class,candidates=t['candidates'],l2=cfg['baseline_l2'],
            max_goals=cfg['max_goals'],validation_days=t['validation_days'],step_days=t['step_days'],min_train=t['min_train'],
            min_validation_matches=t['min_validation_matches'])['selected_half_life_days'])
    except (ValueError,RuntimeError) as exc:
        errors.append({**fold,'setting':'production_v1_half_life_tuning','error':type(exc).__name__});return {}
    fold['production_v1_tuned_half_life_days']=tuned
    fixed=float(upgrade['production_v2']['half_life_days']);models={}
    for key,(half,shots) in {'tuned':(tuned,False),'tuned_shots':(tuned,True),'fixed':(fixed,False),'fixed_shots':(fixed,True)}.items():
        try:
            models[key]=model_class(half_life_days=half,l2=cfg['baseline_l2'],max_goals=cfg['max_goals'],
                **({'shot_features':True} if shots else {})).fit(train,as_of=origin)
        except (ValueError,RuntimeError) as exc:
            errors.append({**fold,'setting':'upgrade_'+key,'error':type(exc).__name__});continue
        if shots:
            report=getattr(models[key],'shot_features_report',{})
            fold['shot_gate_'+key]={k:report.get(k) for k in ('status','failed_gates','selected_weight','selected_component',
                'selected_shrinkage','audit_gain','audit_gain_lower95','audit_matches','tuning_matches')}
    return models


def evaluate_league(data, league, cfg, model_class=None):
    from football_value_pipeline_v2_standalone import DixonColesModel,reweight_matrix_to_1x2
    model_class=model_class or DixonColesModel
    start,audit,end=(pd.Timestamp(cfg[k]) for k in ('test_start','audit_start','test_end_exclusive'))
    boundaries=sorted(set([*pd.date_range(start,end,freq=f"{cfg['step_days']}D"),audit,end]))
    records=[];folds=[];coverage=Counter();errors=[]
    for origin,stop in zip(boundaries,boundaries[1:]):
        train=data.loc[data.Date<origin].copy();test=data.loc[(data.Date>=origin)&(data.Date<stop)]
        if test.empty:continue
        if len(train)<cfg['min_train']:
            coverage['insufficient_training_matches']+=len(test);continue
        if train.Date.max()>=origin or test.Date.min()<origin:raise ValueError('Temporal leakage')
        fold={'league':league,'origin':origin.date().isoformat(),'end_exclusive':stop.date().isoformat(),
            'training_end':train.Date.max().date().isoformat(),'training_matches':len(train),'test_matches':len(test),
            'training_sha256':hashlib.sha256(train[['Date','HomeTeam','AwayTeam','FTHG','FTAG']].to_csv(index=False,lineterminator='\n').encode()).hexdigest()}
        models={}
        for name,(half,l2) in fitting_grid(cfg).items():
            try:
                models[name]=model_class(half_life_days=half,l2=l2,max_goals=cfg['max_goals']).fit(train,as_of=origin)
            except (ValueError,RuntimeError) as exc:
                errors.append({**fold,'setting':name,'error':type(exc).__name__})
        if 'baseline' not in models:
            coverage['baseline_fit_failure_matches']+=len(test);folds.append(fold);continue
        upgrade_models=fit_upgrade_models(train,origin,cfg,model_class,fold,errors)
        folds.append(fold)
        for _,row in test.iterrows():
            coverage['evaluated_fixtures']+=1
            opening=market_probabilities(row,('PSH','PSD','PSA'),cfg['devig_method'])
            closing=market_probabilities(row,('PSCH','PSCD','PSCA'),cfg['devig_method'])
            ou_open=market_probabilities(row,('P>2.5','P<2.5'),cfg['devig_method'])
            ou_close=market_probabilities(row,('PC>2.5','PC<2.5'),cfg['devig_method'])
            for name,p in [('opening_1x2',opening),('closing_1x2',closing),('opening_ou25',ou_open),('closing_ou25',ou_close)]:
                coverage[name+'_available']+=int(p is not None)
            identity={'league':league,'date':row.Date.date().isoformat(),'home_team':row.HomeTeam,'away_team':row.AwayTeam,
                'origin':fold['origin'],'training_end':fold['training_end'],
                'phase':'development' if row.Date<audit else 'audit','home_goals':int(row.FTHG),'away_goals':int(row.FTAG)}
            identity['fixture_key']='|'.join(str(identity[k]) for k in ('league','date','home_team','away_team'))
            identity['y']=0 if row.FTHG>row.FTAG else 1 if row.FTHG==row.FTAG else 2
            matrices={};meta={}
            for name,model in models.items():
                # Avoid partial-name fallback in benchmark: report unknown teams explicitly.
                if row.HomeTeam not in model.teams or row.AwayTeam not in model.teams:
                    coverage[name+'_unknown_team_matches']+=1;continue
                m,info=model.score_matrix(row.HomeTeam,row.AwayTeam);matrices[name]=m;meta[name]=info
            if 'baseline' not in matrices:continue
            def append(name,m=None,p=None,timing='model_only',scale=None):
                if m is not None:
                    probs=DixonColesModel.one_x_two(m);p=np.array([probs[k] for k in ('home','draw','away')])
                record={**identity,'variant':name,'timing':timing,'p_home':float(p[0]),'p_draw':float(p[1]),'p_away':float(p[2]),
                    **{key:None for key in GOALS},'totals_scale':scale,'opening_hda_available':opening is not None,
                    'closing_hda_available':closing is not None,'opening_ou_available':ou_open is not None,'closing_ou_available':ou_close is not None}
                if m is not None:record.update(goals(m))
                records.append(record)
            append('raw_model',matrices['baseline'])
            for name,m in matrices.items():
                if name!='baseline':append(name+'_raw',m)
            if opening is not None:
                append('pinnacle_opening_only',p=opening,timing='nominal_opening_untimestamped')
                raw_hda=DixonColesModel.one_x_two(matrices['baseline'])
                raw_p=np.array([raw_hda[k] for k in ('home','draw','away')]);target=.5*raw_p+.5*opening
                append(BASE,reweight_matrix_to_1x2(matrices['baseline'],target),timing='nominal_opening_untimestamped')
                for weight in cfg['market_weights']:
                    append(f'market_weight_{weight:g}',reweight_matrix_to_1x2(matrices['baseline'],(1-weight)*raw_p+weight*opening),timing='nominal_opening_untimestamped')
                for name,m in matrices.items():
                    if name=='baseline':continue
                    p=DixonColesModel.one_x_two(m);p=np.array([p[k] for k in ('home','draw','away')])
                    append(name,reweight_matrix_to_1x2(m,.5*p+.5*opening),timing='nominal_opening_untimestamped')
                for name,pair in [('totals_opening_anchor',ou_open),('totals_closing_oracle',ou_close)]:
                    if pair is None:continue
                    try:
                        info=meta['baseline'];m,scale=anchor_totals(info['lambda_home'],info['lambda_away'],models['baseline'].rho,target,float(pair[0]),cfg['max_goals'],tail_bounded=bool(info.get('score_engine_version')))
                        append(name,m,timing='closing_oracle_evaluation_only' if 'closing' in name else 'nominal_opening_untimestamped',scale=scale)
                    except ValueError:
                        coverage[name+'_solver_failures']+=1
            if closing is not None:append('pinnacle_closing_only',p=closing,timing='closing_reference_evaluation_only')
            for name,(key,weight,anchor) in upgrade_spec(cfg).items():
                model=upgrade_models.get(key)
                if model is None or row.HomeTeam not in model.teams or row.AwayTeam not in model.teams:
                    coverage[name+'_unfitted_or_unknown_team']+=1;continue
                m,info=model.score_matrix(row.HomeTeam,row.AwayTeam)
                if opening is not None:
                    # Production blend; no Pinnacle 1X2 means no blend, as live.
                    p=DixonColesModel.one_x_two(m);p=np.array([p[k] for k in ('home','draw','away')])
                    m=reweight_matrix_to_1x2(m,(1-weight)*p+weight*opening)
                status,scale='NOT_APPLICABLE',None
                if anchor:
                    status='NOT_ANCHORED_NO_PINNACLE_OU25_QUOTE'
                    if ou_open is not None:
                        hda=DixonColesModel.one_x_two(m)
                        try:
                            m,scale=anchor_totals(info['lambda_home'],info['lambda_away'],model.rho,[hda[k] for k in ('home','draw','away')],
                                float(ou_open[0]),cfg['max_goals'],tail_bounded=bool(info.get('score_engine_version')))
                            status='ANCHORED'
                        except ValueError:status='NOT_ANCHORED_SOLVER_FAILED'
                    coverage[name+'_'+status.lower()]+=1
                append(name,m,timing='nominal_opening_untimestamped' if opening is not None or scale is not None else 'model_only',scale=scale)
                records[-1].update(handicaps(m),anchor_status=status,blend_applied=opening is not None,
                    shot_features_applied=bool(info.get('shot_features_applied')),half_life_days=float(model.half_life_days))
    return records,folds,dict(coverage),errors


def score(row, market):
    if market=='1x2':
        p=np.array([row['p_home'],row['p_draw'],row['p_away']]);y=np.eye(3)[row['y']]
        return {'log_loss':-math.log(max(1e-12,p[row['y']])), 'brier':float(np.sum((p-y)**2)),
                'rps':float(np.sum((np.cumsum(p)[:2]-np.cumsum(y)[:2])**2)/2)}
    p=row.get(market)
    if p is None:return None
    h,a=row['home_goals'],row['away_goals']
    if market in AH:
        margin=h-a+AH_LINES[AH.index(market)]
        if margin==0:return None  # refunded stake: no binary outcome
        y=int(margin>0)
        return {'log_loss':-math.log(max(1e-12,p if y else 1-p)),'brier':(p-y)**2,'probability':p,'outcome':y}
    y=int({'over_1_5':h+a>=2,'under_3_5':h+a<=3,'btts_yes':h>0 and a>0,'over_2_5':h+a>=3}[market])
    return {'log_loss':-math.log(max(1e-12,p if y else 1-p)),'brier':(p-y)**2,'probability':p,'outcome':y}


def metrics(rows,market):
    scored=[score(r,market) for r in rows];scored=[s for s in scored if s is not None]
    if not scored:return {'n':0,'log_loss':None,'brier':None,'rps':None,'calibration':[]}
    output={'n':len(scored),'log_loss':sum(s['log_loss'] for s in scored)/len(scored),
        'brier':sum(s['brier'] for s in scored)/len(scored),
        'rps':sum(s['rps'] for s in scored)/len(scored) if market=='1x2' else None,'calibration':[]}
    if market!='1x2':
        for lo in np.arange(0,1,.1):
            selected=[s for s in scored if min(9,int(s['probability']*10))==int(round(lo*10))]
            if not selected:continue
            n=len(selected);p=sum(s['probability'] for s in selected)/n;q=sum(s['outcome'] for s in selected)/n;z=1.96
            centre=(q+z*z/(2*n))/(1+z*z/n);radius=z*math.sqrt(q*(1-q)/n+z*z/(4*n*n))/(1+z*z/n)
            output['calibration'].append({'low':float(lo),'high':float(min(1,lo+.1)),'n':n,'mean_probability':p,'observed_rate':q,
                'overconfidence':p-q,'observed_wilson95':[max(0,centre-radius),min(1,centre+radius)]})
    if market!='1x2':
        threshold={'over_1_5':.78,'under_3_5':.80,'btts_yes':.70,'over_2_5':.70}[market]
        selected=[s for s in scored if s['probability']>=threshold]
        output['high_confidence']={'threshold':threshold,'n':len(selected),
            'mean_probability':sum(s['probability'] for s in selected)/len(selected) if selected else None,
            'observed_rate':sum(s['outcome'] for s in selected)/len(selected) if selected else None}
    return output


def paired(candidate,baseline,market):
    left={r['fixture_key']:r for r in candidate if score(r,market) is not None}
    right={r['fixture_key']:r for r in baseline if score(r,market) is not None}
    keys=sorted(left.keys()&right.keys());a=[left[k] for k in keys];b=[right[k] for k in keys]
    output={'candidate':metrics(a,market),'baseline':metrics(b,market),'n':len(keys)}
    for name in ('log_loss','brier',*(['rps'] if market=='1x2' else [])):
        gains=[score(right[k],market)[name]-score(left[k],market)[name] for k in keys]
        mean=float(np.mean(gains)) if gains else None
        se=float(np.std(gains,ddof=1)/math.sqrt(len(gains))) if len(gains)>1 else None
        output[name+'_gain']=mean;output[name+'_gain_approx95']=[mean-1.96*se,mean+1.96*se] if se is not None else None
    return output


def aggregate(records,cfg):
    comparisons=[];choices=[];markets=('1x2',*GOALS)
    for league in ('ALL',*cfg['leagues']):
        subset=[r for r in records if league=='ALL' or r['league']==league]
        for phase in ('development','audit','ALL'):
            cohort=[r for r in subset if phase=='ALL' or r['phase']==phase]
            base=[r for r in cohort if r['variant']==BASE]
            closing=[r for r in cohort if r['variant']=='pinnacle_closing_only']
            for market in markets:
                for variant in sorted({r['variant'] for r in cohort}):
                    selected=[r for r in cohort if r['variant']==variant and score(r,market) is not None]
                    if not selected:continue
                    c={'league':league,'phase':phase,'market':market,'variant':variant,'metrics':metrics(selected,market),
                        'paired_vs_baseline':paired(selected,base,market)}
                    c['paired_vs_raw_model']=paired(selected,[r for r in cohort if r['variant']=='raw_model'],market)
                    if market=='1x2':c['paired_vs_pinnacle_closing']=paired(selected,closing,market)
                    comparisons.append(c)
        families={'l2':(BASE,[f'l2_{v:g}' for v in cfg['l2_candidates']]),
            'half_life':(BASE,[f'half_life_{v:g}' for v in cfg['half_life_candidates']]),
            'raw_l2':('raw_model',[f'l2_{v:g}_raw' for v in cfg['l2_candidates']]),
            'raw_half_life':('raw_model',[f'half_life_{v:g}_raw' for v in cfg['half_life_candidates']]),
            'market_weight':(BASE,[f'market_weight_{v:g}' for v in cfg['market_weights']]),
            'totals':(BASE,['totals_opening_anchor'])}
        for family,(control,names) in families.items():
            # Baseline remains an option. Compare every option on one common cohort.
            candidates=[control,*names]
            for market in markets:
                by_phase={}
                for phase in ('development','audit'):
                    groups={name:{r['fixture_key']:r for r in subset if r['phase']==phase and r['variant']==name and score(r,market) is not None} for name in candidates}
                    common=set.intersection(*(set(g) for g in groups.values()))
                    by_phase[phase]={name:metrics([groups[name][k] for k in sorted(common)],market) for name in candidates}
                dev=by_phase['development'];audit=by_phase['audit'];n=dev[control]['n']
                chosen=min(candidates,key=lambda name:(dev[name]['log_loss'],dev[name]['brier'],candidates.index(name))) if n>=cfg['min_development_matches'] else None
                choices.append({'league':league,'family':family,'market':market,'common_development_n':n,
                    'common_audit_n':audit[control]['n'],'selected_on_development':chosen,
                    'development_metrics':dev,'audit_metrics':audit,
                    'assessment':'INSUFFICIENT_COVERAGE' if chosen is None or audit[control]['n']<cfg['min_audit_matches'] else 'RETROSPECTIVE_DIAGNOSTIC_ONLY'})
    output={'comparisons':comparisons,'development_choices':choices}
    if cfg.get('model_upgrade_comparison'):output['model_upgrade_comparison']=aggregate_upgrades(records,cfg)
    return output


def aggregate_upgrades(records,cfg):
    """Each change alone and full v2 against the production v1 replay, on one cohort."""
    markets=('1x2',*GOALS,*AH);scored={}
    for r in records:
        if r['variant'] in UPGRADE_VARIANTS:
            for market in markets:
                value=score(r,market)
                if value is not None:scored.setdefault((r['league'],r['phase'],r['variant'],market),{})[r['fixture_key']]=value
    rows=[]
    for league in ('ALL',*cfg['leagues']):
        for phase in ('development','audit'):
            for market in markets:
                groups={v:{} for v in UPGRADE_VARIANTS}
                for (l,ph,v,mk),values in scored.items():
                    if ph==phase and mk==market and (league=='ALL' or l==league):groups[v].update(values)
                common=sorted(set.intersection(*(set(g) for g in groups.values())))
                for variant in UPGRADE_VARIANTS:
                    row={'league':league,'phase':phase,'market':market,'variant':variant,'n':len(common)}
                    for metric in ('log_loss','brier'):
                        values=[groups[variant][k][metric] for k in common]
                        gains=[groups[UPGRADE_BASE][k][metric]-groups[variant][k][metric] for k in common]
                        mean=float(np.mean(gains)) if gains else None
                        se=float(np.std(gains,ddof=1)/math.sqrt(len(gains))) if len(gains)>1 else None
                        row[metric]=float(np.mean(values)) if values else None
                        row[metric+'_gain_vs_production_v1']=mean
                        row[metric+'_gain_approx95']=[mean-1.96*se,mean+1.96*se] if se is not None else None
                    rows.append(row)
    anchors={};shifts={}
    by_key={(r['fixture_key'],r['variant']):r for r in records if r['variant'] in (UPGRADE_BASE,'upgrade_pinnacle_ou25_anchor')}
    for league in ('ALL',*cfg['leagues']):
        subset=[r for r in records if r['variant']=='upgrade_pinnacle_ou25_anchor' and (league=='ALL' or r['league']==league)]
        anchors[league]=dict(sorted(Counter(r['anchor_status'] for r in subset).items()))
        pairs=[(r,by_key.get((r['fixture_key'],UPGRADE_BASE))) for r in subset if r['anchor_status']=='ANCHORED']
        pairs=[(a,b) for a,b in pairs if b is not None]
        shifts[league]={'anchored_fixtures':len(pairs),**{key:{
            'mean_abs_change':float(np.mean([abs(a[key]-b[key]) for a,b in pairs if a.get(key) is not None and b.get(key) is not None])) if pairs else None,
            'mean_change':float(np.mean([a[key]-b[key] for a,b in pairs if a.get(key) is not None and b.get(key) is not None])) if pairs else None}
            for key in (*AH,'over_2_5')}}
    return {'baseline':UPGRADE_BASE,'variants':list(UPGRADE_VARIANTS),'markets':list(markets),'paired':rows,
        'anchor_status_counts':anchors,'anchor_probability_shift_vs_production_v1':shifts,
        'note':'Positive gain = lower error than the production v1 replay on identical fixtures. Asian handicap = home side; integer lines exclude refunded outcomes.'}


def validate_records(records,folds,cfg):
    foldmap={(f['league'],f['origin']):f for f in folds};seen=set()
    for row in records:
        key=(row['fixture_key'],row['variant'])
        if key in seen:raise ValueError('Duplicate benchmark prediction')
        seen.add(key)
        date,origin,end=(pd.Timestamp(row[k]) for k in ('date','origin','training_end'))
        fold=foldmap[(row['league'],row['origin'])]
        if row['training_end']!=fold['training_end'] or not pd.Timestamp(cfg['test_start'])<=origin< pd.Timestamp(cfg['test_end_exclusive']):raise ValueError('Unbound prediction fold')
        if not end<origin<=date<pd.Timestamp(fold['end_exclusive']):raise ValueError('Temporal prediction violation')
        if row['phase']!=('development' if date<pd.Timestamp(cfg['audit_start']) else 'audit'):raise ValueError('Phase contamination')
        p=[row[k] for k in ('p_home','p_draw','p_away')]
        if any(not math.isfinite(v) or not 0<=v<=1 for v in p) or abs(sum(p)-1)>1e-8:raise ValueError('Invalid 1X2 probabilities')
        if any(row.get(k) is not None and (not math.isfinite(row[k]) or not 0<=row[k]<=1) for k in (*GOALS,*AH)):raise ValueError('Invalid goal probabilities')
        if 'closing' in row['variant'] and not row['timing'].startswith('closing_'):raise ValueError('Unlabelled closing input')
        if row['y']!=(0 if row['home_goals']>row['away_goals'] else 1 if row['home_goals']==row['away_goals'] else 2):raise ValueError('Invalid outcome')
    return True


def write_report(output,summary,records,folds):
    output.mkdir(parents=True,exist_ok=True)
    pd.DataFrame(records).to_csv(output/'predictions.csv',index=False,lineterminator='\n')
    write_json(output/'folds.json',folds)
    write_json(output/'summary.json',summary)
    lines=['# Historical football benchmark','',summary['limitations'],'',
        f"Unique evaluated fixtures: {summary['evaluated_fixtures']}. Baseline: fixed half-life {summary['config']['baseline_half_life']:g} days, L2 {summary['config']['baseline_l2']:g}. This is a named configuration reference, not a replay of per-run production tuning.",'',
        '| League | Evaluated | Opening HDA | Closing HDA | Opening O/U | Closing O/U |',
        '|---|---:|---:|---:|---:|---:|']
    for league,c in summary['coverage'].items():
        lines.append(f"| {league} | {c.get('evaluated_fixtures',0)} | {c.get('opening_1x2_available',0)} | {c.get('closing_1x2_available',0)} | {c.get('opening_ou25_available',0)} | {c.get('closing_ou25_available',0)} |")
    lines+=['','Paired comparisons below use the exact same fixtures as their baseline. Positive gain means lower candidate error. Approximate intervals assume independent fixtures and do not account for multiple comparisons.','',
        '| Phase | Market | Variant | Paired N | Baseline loss | Candidate loss | Loss gain | Brier gain |',
        '|---|---|---|---:|---:|---:|---:|---:|']
    def fmt(v):return f'{v:.5f}' if v is not None else 'n.a.'
    for c in summary['comparisons']:
        if c['league']!='ALL' or c['phase']=='ALL':continue
        p=c['paired_vs_baseline']
        lines.append(f"| {c['phase']} | {c['market']} | {c['variant']} | {p['n']} | {fmt(p['baseline']['log_loss'])} | {fmt(p['candidate']['log_loss'])} | {fmt(p['log_loss_gain'])} | {fmt(p['brier_gain'])} |")
    lines+=['','Development-selected candidates','', '| Family | Market | Selected | Development N | Audit N | Status |','|---|---|---|---:|---:|---|']
    for c in summary['development_choices']:
        if c['league']=='ALL':lines.append(f"| {c['family']} | {c['market']} | {c['selected_on_development'] or 'none'} | {c['common_development_n']} | {c['common_audit_n']} | {c['assessment']} |")
    upgrade=summary.get('model_upgrade_comparison')
    if upgrade:
        lines+=['','Model upgrades versus the production v1 replay (all leagues; per-league rows are in summary.json)','',
            '| Phase | Market | Variant | Paired N | Log loss | Brier | Log-loss gain | Brier gain |','|---|---|---|---:|---:|---:|---:|---:|']
        for r in upgrade['paired']:
            if r['league']=='ALL':lines.append(f"| {r['phase']} | {r['market']} | {r['variant']} | {r['n']} | {fmt(r['log_loss'])} | {fmt(r['brier'])} | {fmt(r['log_loss_gain_vs_production_v1'])} | {fmt(r['brier_gain_vs_production_v1'])} |")
    lines+=['','Closing-reference comparisons, RPS, calibration buckets, per-league results and development/audit metrics are in summary.json. Predictions and fold training hashes are retained in the workflow artifact. No setting is promoted automatically.','']
    (output/'report.md').write_text('\n'.join(lines),encoding='utf-8')
    manifest={'version':VERSION,'sha256':{name:digest(output/name) for name in ('summary.json','predictions.csv','folds.json','report.md')}}
    write_json(output/'manifest.json',manifest)


def validate_report(output):
    manifest=json.loads((output/'manifest.json').read_text(encoding='utf-8'))
    if manifest.get('version') not in SUPPORTED_VERSIONS or set(manifest.get('sha256',{}))!={'summary.json','predictions.csv','folds.json','report.md'}:
        raise ValueError('Incomplete benchmark artifact manifest')
    for name,value in manifest['sha256'].items():
        if name not in ('summary.json','predictions.csv','folds.json','report.md') or digest(output/name)!=value:raise ValueError('Benchmark artifact integrity failure')
    summary=json.loads((output/'summary.json').read_text(encoding='utf-8'))
    records=pd.read_csv(output/'predictions.csv',keep_default_na=False).to_dict('records')
    for row in records:
        for key in (*GOALS,*AH,'totals_scale'):
            if key in row:row[key]=float(row[key]) if row[key]!='' else None
    folds=json.loads((output/'folds.json').read_text(encoding='utf-8'))
    validate_config(summary['config']);validate_records(records,folds,summary['config'])
    expected=aggregate(records,summary['config'])
    # CSV round-trip can change floating arithmetic in the last few bits.
    def equal(a,b):
        if isinstance(b,dict):return set(a)==set(b) and all(equal(a[k],b[k]) for k in b)
        if isinstance(b,list):return len(a)==len(b) and all(equal(x,y) for x,y in zip(a,b))
        if isinstance(b,(float,int)):return a is not None and abs(a-b)<=1e-9
        return a==b
    if any(not equal(summary[k],v) for k,v in expected.items()):raise ValueError('Benchmark metrics do not reconcile')
    if summary['evaluated_fixtures']!=len({r['fixture_key'] for r in records}):raise ValueError('Fixture count mismatch')
    return True


def verify_inputs(cache,cfg,manifest):
    required={f'{season}_{CODES[league]}.csv' for league in cfg['leagues'] for season in cfg['seasons']}
    if manifest.get('dataset_source_commit')!=cfg.get('dataset_source_commit') or required-set(manifest.get('sha256',{})):
        raise ValueError('Input manifest does not match benchmark configuration')
    for name in sorted(required):
        if digest(cache/name)!=manifest['sha256'][name]:
            raise ValueError('Pinned input changed: '+name+'; use --materialize-pinned-data or the benchmark workflow')
    return True


def materialize_inputs(repo,destination,cfg,manifest):
    sha=cfg.get('dataset_source_commit','')
    if not re.fullmatch(r'[a-f0-9]{40}',sha):raise ValueError('Invalid pinned dataset SHA')
    destination.mkdir(parents=True,exist_ok=True)
    for league in cfg['leagues']:
        for season in cfg['seasons']:
            name=f'{season}_{CODES[league]}.csv'
            content=subprocess.run(['git','-C',str(repo),'show',f'{sha}:.football_cache/{name}'],
                check=True,capture_output=True).stdout
            if hashlib.sha256(content).hexdigest()!=manifest.get('sha256',{}).get(name):
                raise ValueError('Git dataset does not match pinned manifest')
            (destination/name).write_bytes(content)
    verify_inputs(destination,cfg,manifest)
    return destination


def run(cache,output,cfg,source_commit='unrecorded',model_class=None,input_manifest=None):
    validate_config(cfg)
    release=cfg.get('model_upgrade_comparison',{}).get('production_v2',{})
    if 'feature_rule' in release:
        from football_value_pipeline_v2_standalone import MODEL_VERSION, MODEL_PROFILES, SHOTS_WITH_BBS_VALIDATED
        profile=MODEL_PROFILES[MODEL_VERSION]
        if (release['model_version']!=MODEL_VERSION or release['market_weight']!=profile['market_weight']
                or release['half_life_days']!=profile['half_life_days'] or release['shot_features']!=profile['shot_features']
                or release['totals_anchor']!=profile['totals_anchor'] or release['bbs_statistics'] is not True
                or release['feature_rule']!='bbs_priority_mutually_exclusive_shots' or SHOTS_WITH_BBS_VALIDATED):
            raise ValueError('Benchmark release settings differ from production')
    if cfg.get('input_manifest'):
        if input_manifest is None:raise ValueError('Pinned benchmark requires its input manifest')
        verify_inputs(cache,cfg,input_manifest)
    records=[];folds=[];sources=[];coverage={};errors=[];exclusions={}
    for league in cfg['leagues']:
        data,inputs,excluded=load_history(cache,league,cfg);sources.extend(inputs);exclusions[league]=excluded
        print(f'{league}: {len(data)} historical results; running chronological comparisons...',flush=True)
        rows,leaguefolds,counts,failures=evaluate_league(data,league,cfg,model_class)
        records.extend(rows);folds.extend(leaguefolds);coverage[league]=counts;errors.extend(failures)
    if not records:raise ValueError('No benchmark predictions; refusing an empty report')
    validate_records(records,folds,cfg)
    summary={'version':VERSION,'generated_at_utc':datetime.now(timezone.utc).isoformat(),'config':cfg,
        'source_commit':source_commit,'dataset_source_commit':cfg.get('dataset_source_commit','unrecorded'),
        'input_binding':'PINNED_SHA256' if input_manifest is not None else 'UNPINNED_DIAGNOSTIC',
        'source_files':sources,'coverage':coverage,'excluded_rows':exclusions,'fit_errors':errors,
        'evaluated_fixtures':len({r['fixture_key'] for r in records}),
        'code_sha256':{p.name:digest(p) for p in (Path(__file__),*(Path(__file__).with_name(n) for n in ('football_value_pipeline_v2_standalone.py','score_probability.py','shot_features.py','bbs_statistics_model.py','dc_decay_validation.py','historical_benchmark_config.json')))},
        'source_worktree_diff_sha256':hashlib.sha256(subprocess.run(['git','diff','HEAD','--'],cwd=Path(__file__).parent,capture_output=True,check=True).stdout).hexdigest(),
        'release_profile':release,
        'bbs_input_limitation':'Pinned Football-Data CSVs contain shots but no timestamped BBS observations. The production BBS-priority rule runs unchanged; BBS therefore cannot activate on these pinned inputs.',
        'runtime':{'python':platform.python_version(),'numpy':np.__version__,'pandas':pd.__version__},
        'limitations':'Retrospective diagnostics only. Historical periods were already examined by Claude and are not untouched evidence. Nominal opening odds lack exact availability timestamps; no historical betting edge/ROI/CLV claim is made. Closing inputs are explicitly oracle/evaluation-only. Baseline fixes half-life at 240 days rather than replaying production tuning. Fitted rho is retained for totals scaling. No bookmaker fallback, new data download or automatic production change.',
        **aggregate(records,cfg)}
    if cfg.get('model_upgrade_comparison'):
        gates={}
        for f in folds:
            for key in ('shot_gate_tuned_shots','shot_gate_fixed_shots'):
                if key in f:
                    g=gates.setdefault(f['league'],{}).setdefault(key,{'folds':0,'status':Counter(),'failed_gates':Counter()})
                    g['folds']+=1;g['status'][f[key]['status']]+=1;g['failed_gates'].update(f[key].get('failed_gates') or [])
        summary['shot_feature_gate_by_league']={l:{k:{'folds':v['folds'],'status':dict(v['status']),'failed_gates':dict(v['failed_gates'])} for k,v in g.items()} for l,g in gates.items()}
        summary['tuned_half_life_by_fold']={f"{f['league']}|{f['origin']}":f.get('production_v1_tuned_half_life_days') for f in folds}
    summary['pinnacle_comparison_status']='TARGET_COVERAGE_MET' if sum(r['variant']=='pinnacle_closing_only' for r in records)>=cfg['min_pinnacle_comparison_matches'] else 'BELOW_1000_MATCH_TARGET'
    write_report(output,summary,records,folds);validate_report(output)
    return summary


def main(argv=None):
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--cache-dir',type=Path,default=Path('.football_cache'))
    parser.add_argument('--config',type=Path,default=Path(__file__).with_name('historical_benchmark_config.json'))
    parser.add_argument('--out-dir',type=Path,default=Path('workflow_artifacts/historical_benchmark'))
    parser.add_argument('--source-commit',default='unrecorded')
    parser.add_argument('--validate-only',action='store_true')
    parser.add_argument('--materialize-pinned-data',action='store_true',help='Read pinned CSVs from local Git objects into the benchmark output folder; never overwrite production cache')
    args=parser.parse_args(argv)
    if args.validate_only:validate_report(args.out_dir);print('Benchmark evidence reconciled');return 0
    if args.source_commit!='unrecorded' and not re.fullmatch(r'[a-f0-9]{40}',args.source_commit):parser.error('source-commit must be a full Git SHA')
    cfg=json.loads(args.config.read_text(encoding='utf-8-sig'))
    if args.out_dir.resolve()==args.cache_dir.resolve() or args.cache_dir.resolve() in args.out_dir.resolve().parents:
        parser.error('Benchmark output cannot overwrite training inputs')
    if 'raw' in args.out_dir.parts or 'snapshots' in args.out_dir.parts:parser.error('Benchmark cannot write production raw/snapshots')
    manifest=json.loads((args.config.parent/cfg['input_manifest']).read_text(encoding='utf-8-sig')) if cfg.get('input_manifest') else None
    cache=args.cache_dir
    if args.materialize_pinned_data:
        if manifest is None:parser.error('materialize-pinned-data requires an input manifest')
        cache=materialize_inputs(Path(__file__).parent,args.out_dir/'pinned_inputs',cfg,manifest)
    summary=run(cache,args.out_dir,cfg,args.source_commit,input_manifest=manifest)
    print(f"Benchmark: {summary['evaluated_fixtures']} fixtures; {summary['pinnacle_comparison_status']}; see {args.out_dir/'report.md'}")
    return 0


if __name__=='__main__':raise SystemExit(main())
