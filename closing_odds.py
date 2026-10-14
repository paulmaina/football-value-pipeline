"""Local pre-kickoff quote collection and evidence-only CLV reporting."""
import argparse
from datetime import datetime,timedelta,timezone
import hashlib
import json
import os
from pathlib import Path
import re
import time

VERSION='local-closing-quotes-v1'
LABELS={'home':'Home win','away':'Away win','over_1_5':'Over 1.5','under_3_5':'Under 3.5','btts_yes':'Both Teams to Score - Yes','home_draw':'Double Chance 1X','draw_away':'Double Chance X2'}


def digest(data):return hashlib.sha256(json.dumps(data,sort_keys=True,separators=(',',':'),allow_nan=False).encode()).hexdigest()


def normalize(source,payload,observed):
    """Complete same-book markets, timestamped before kickoff; no synthetic prices."""
    from performance_tracking import utc,number
    from football_value_pipeline_v2_standalone import canonical_team_key,devig
    from double_chance import parse_quotes
    if not isinstance(payload,dict) or not isinstance(payload.get('bookmakers',[]),list):raise ValueError('Malformed odds response')
    kick=utc(source.get('kickoff_utc'));pk=utc(payload.get('commence_time'))
    if not kick or not pk or abs((pk-kick).total_seconds())>1 or str(payload.get('id'))!=str(source.get('odds_event_id')) or not 0<(kick-observed).total_seconds()<=90 or any(canonical_team_key(str(payload.get(k,'')))!=canonical_team_key(str(source.get(k,''))) for k in ('home_team','away_team')):raise ValueError('Closing event/timing mismatch')
    quotes=[]
    for book in payload.get('bookmakers',[]):
        if not isinstance(book,dict) or not isinstance(book.get('markets',[]),list):continue
        key=str(book.get('key','')).lower()
        if key not in ('pinnacle','1xbet'):continue
        for market in book.get('markets',[]):
            if not isinstance(market,dict) or not isinstance(market.get('outcomes',[]),list):continue
            updated=utc(market.get('last_update') or book.get('last_update'))
            if not updated or not 0<=(observed-updated).total_seconds()<=120 or updated>=kick:continue
            mk=market.get('key');outcomes=market.get('outcomes',[]);pairs=[]
            if mk=='h2h':
                names={canonical_team_key(source['home_team']):'home',canonical_team_key(source['away_team']):'away','draw':'draw'}
                values={};duplicate=False
                for o in outcomes:
                    if not isinstance(o,dict):continue
                    k=names.get(canonical_team_key(str(o.get('name',''))));v=number(o.get('price'),min_value=1.000001)
                    if k and v:
                        if k in values:duplicate=True
                        values[k]=v
                if not duplicate and set(values)=={'home','draw','away'} and .98<=sum(1/v for v in values.values())<=1.20:
                    probabilities=devig([values[k] for k in ('home','draw','away')],method='power')
                    pairs=[(k,values[k],float(probabilities[i]),'power_complete_1x2') for i,k in enumerate(('home','draw','away'))]
            elif mk in ('totals','alternate_totals','btts'):
                for point in ([None] if mk=='btts' else [1.5,2.5,3.5]):
                    values={};duplicate=False
                    for o in outcomes:
                        if not isinstance(o,dict):continue
                        if o.get('point')!=point:continue
                        k=str(o.get('name','')).lower();v=number(o.get('price'),min_value=1.000001)
                        allowed=('yes','no') if mk=='btts' else ('over','under')
                        if k in allowed and v:
                            if k in values:duplicate=True
                            values[k]=v
                    allowed=('yes','no') if mk=='btts' else ('over','under')
                    if duplicate or set(values)!=set(allowed) or not .98<=sum(1/v for v in values.values())<=1.20:continue
                    probs=devig([values[k] for k in allowed],method='power')
                    pairs.extend((('btts_'+k if mk=='btts' else k+'_'+str(point).replace('.','_')),values[k],float(probs[i]),'power_complete_binary') for i,k in enumerate(allowed))
            elif mk=='double_chance':
                dc=parse_quotes({**payload,'bookmakers':[{**book,'markets':[market]}]})
                pairs=[(k,dc['market_reference_dc_'+k+'_odds'],dc['market_p_'+k],'proportional_overlap_sum_two') for k in ('home_draw','draw_away') if 'market_p_'+k in dc]
            for selection,price,p,method in pairs:
                quotes.append({'bookmaker':key,'selection':selection,'decimal_odds':price,'fair_probability':p,'devig_method':method,'updated_at_utc':updated.isoformat()})
    # At most one quote per bookmaker/selection; newest market wins deterministically.
    unique={}
    for q in sorted(quotes,key=lambda x:x['updated_at_utc']):unique[(q['bookmaker'],q['selection'])]=q
    return {'version':VERSION,'observed_at_utc':observed.isoformat(),'fixture':{k:source.get(k) for k in ('league','home_team','away_team','kickoff_utc','odds_event_id')},'payload':payload,'quotes':list(unique.values()),'provenance':'local_clock_live_feed; content hash is not independent proof of capture time; last observed near kickoff, not guaranteed official closing price'}


def load_observations(root,clock=None):
    rows=[];rejected=[]
    for path in sorted((root/'closing_odds/observations').glob('*.json')):
        try:
            d=json.loads(path.read_text(encoding='utf-8-sig'))
            if digest(d)!=path.stem or d.get('version')!=VERSION:raise ValueError('Hash')
            from performance_tracking import utc
            observed=utc(d['observed_at_utc'])
            if not observed or (clock is not None and observed>clock):raise ValueError('Clock')
            expected=normalize(d['fixture'],d['payload'],observed)
            if d!=expected:raise ValueError('Quote calculation')
            rows.append(d)
        except (ValueError,TypeError,KeyError,OSError):rejected.append(path.name)
    return rows,rejected


def fetch(api,source,markets):
    from football_value_pipeline_v2_standalone import THE_ODDS_API_BASE,LEAGUES
    event=str(source.get('odds_event_id',''))
    if not re.fullmatch(r'[A-Za-z0-9_-]+',event):raise ValueError('Invalid odds event')
    league=next(l for l in LEAGUES.values() if l.name==source['league'])
    return api._get_json(f'{THE_ODDS_API_BASE}/sports/{league.odds_api_sport_key}/events/{event}/odds',f'closing_v1_{event}.json',ttl=timedelta(seconds=0),force_refresh=True,allow_stale=False,params={'bookmakers':'pinnacle,1xbet','markets':','.join(sorted(markets)),'oddsFormat':'decimal','dateFormat':'iso'})


def collect_once(root,api,clock=None,limit=100,fetcher=None):
    from performance_tracking import read_csv,utc,fixture_key,now_utc,write_json,load_json
    start=clock or now_utc();budget_path=root/'closing_odds/request_budget.json';budget=load_json(budget_path,{})
    used=budget.get('requests',0) if budget.get('date')==start.date().isoformat() else 0
    cap=min(limit,max(0,100-used))
    observations,_=load_observations(root,start);done={str(x['fixture']['odds_event_id']) for x in observations if x['quotes']};predictions=read_csv(root/'raw/all_leagues_predictions.csv');picks=read_csv(root/'raw/conservative_bet_shortlist.csv');count=0;written=0;errors=[]
    for source in predictions:
        event=str(source.get('odds_event_id',''));kick=utc(source.get('kickoff_utc'))
        if event in done or not event or not kick or not 0<(kick-start).total_seconds()<=90:continue
        if count>=cap:break
        markets={'h2h','totals'}
        selected=[x.get('market') for x in picks if fixture_key(x)==fixture_key(source)]
        if any(m in ('Over 1.5','Under 3.5') for m in selected):markets.add('alternate_totals')
        if 'Both Teams to Score - Yes' in selected:markets.add('btts')
        if any(str(m).startswith('Double Chance') for m in selected):markets.add('double_chance')
        count+=1
        write_json(budget_path,{"date":start.date().isoformat(),"requests":used+count,"daily_request_cap":100})
        try:
            payload=(fetcher or fetch)(api,source,markets)
            observed=clock or now_utc()  # RESPONSE time, never request-start time.
            d=normalize(source,payload,observed);directory=root/'closing_odds/observations';directory.mkdir(parents=True,exist_ok=True);path=directory/(digest(d)+'.json')
            if not path.exists():
                with path.open('x',encoding='utf-8') as f:json.dump(d,f,sort_keys=True,indent=2,allow_nan=False);f.write('\n')
                written+=1
        except Exception as exc:errors.append({'event_id':event,'error':type(exc).__name__})
    status={'checked_at_utc':start.isoformat(),'requests':count,'written':written,'errors':errors,'request_limit':limit,'daily_requests':used+count,'daily_request_cap':100}
    write_json(root/'closing_odds/collector_status.json',status);return status


def evaluate(root,archive,clock):
    from performance_tracking import frozen_rows,fixture_key,utc,number
    observations,rejected=load_observations(root,clock);picks=frozen_rows(archive,'shortlist');rows=[]
    for pick in picks:
        key=fixture_key(pick);selection=next((k for k,v in LABELS.items() if v==pick.get('market')),None);entry=number(pick.get('offered_decimal_odds'),min_value=1.000001)
        item={**pick,'entry_price_basis':'frozen offered quote; accepted execution unverified','closing':{}}
        if utc(pick['kickoff_utc'])>clock:
            item['closing']={book:{'status':'PENDING_KICKOFF'} for book in ('1xbet','pinnacle')}
            rows.append(item);continue
        for book in ('1xbet','pinnacle'):
            candidates=[]
            for obs in observations:
                if fixture_key(obs['fixture'])!=key or utc(obs['fixture']['kickoff_utc'])!=utc(pick['kickoff_utc']) or utc(obs['observed_at_utc'])<utc(pick['snapshot_captured_utc']):continue
                q=next((x for x in obs['quotes'] if x['bookmaker']==book and x['selection']==selection),None)
                # For Pinnacle double chance, coherent 1X2 sums provide FAIR probabilities only, never prices.
                if q is None and book=='pinnacle' and selection in ('home_draw','draw_away'):
                    hda={x['selection']:x for x in obs['quotes'] if x['bookmaker']==book and x['selection'] in ('home','draw','away')}
                    if set(hda)=={'home','draw','away'} and len({x['updated_at_utc'] for x in hda.values()})==1:
                        sides=('home','draw') if selection=='home_draw' else ('draw','away');q={'decimal_odds':None,'fair_probability':sum(hda[s]['fair_probability'] for s in sides),'updated_at_utc':hda['draw']['updated_at_utc'],'devig_method':'power_1x2_sum_no_synthetic_price'}
                if q:candidates.append((utc(obs['observed_at_utc']),q,obs))
            if not candidates:
                item['closing'][book]={'status':'MISSING_VALID_PRE_KICKOFF_QUOTE'};continue
            observed,q,obs=max(candidates,key=lambda x:x[0]);price=q['decimal_odds'];cost=number(pick.get('per_stake_cost'),min_value=0) or 0
            item['closing'][book]={'status':'OBSERVED_NEAR_CLOSE','observed_at_utc':observed.isoformat(),'seconds_before_kickoff':(utc(pick['kickoff_utc'])-observed).total_seconds(),**q,'offered_price_clv':entry/price-1 if book=='1xbet' and entry and price and str(pick.get('bookmaker','')).lower() in ('1xbet','1xbet.com') else None,'fair_close_ev':entry*q['fair_probability']-1-cost if entry else None,'observation_sha256':digest(obs),'official_close_verified':False}
        rows.append(item)
    groups={}
    for book in ('1xbet','pinnacle'):
        valid=[x['closing'][book] for x in rows if x['closing'][book]['status']=='OBSERVED_NEAR_CLOSE'];values=[x['fair_close_ev'] for x in valid if x['fair_close_ev'] is not None];prices=[x['offered_price_clv'] for x in valid if x['offered_price_clv'] is not None]
        groups[book]={'covered_selections':len(valid),'missing_selections':sum(x['closing'][book]['status']=='MISSING_VALID_PRE_KICKOFF_QUOTE' for x in rows),'pending_selections':sum(x['closing'][book]['status']=='PENDING_KICKOFF' for x in rows),'mean_fair_close_ev':sum(values)/len(values) if values else None,'mean_same_book_offered_price_clv':sum(prices)/len(prices) if prices else None,'positive_fair_close_ev':sum(v>0 for v in values)}
    summary={'version':VERSION,'reviewed_at_utc':clock.isoformat(),'frozen_selections':len(rows),'observations':len(observations),'rejected_files':rejected,'by_bookmaker':groups,'automatic_production_change':False,'note':'Last observed live quote within 90 seconds of scheduled kickoff, market age <=120 seconds. Local timestamps are not independently attested and actual kickoff delays are unknown. Offered quote CLV is not realized execution CLV or guaranteed official closing odds. Missing quotes stay missing.'}
    return summary,rows


def review(root,archive,clock):
    from performance_tracking import write_json
    s,rows=evaluate(root,archive,clock);dest=root/'performance/closing_odds';write_json(dest/'summary.json',s);write_json(dest/'selections.json',rows)
    (dest/'report.md').write_text('# Closing quote evidence\n\n'+s['note']+'\n\n'+json.dumps(s['by_bookmaker'],indent=2)+'\n',encoding='utf-8');return s


def validate_report(root):
    from performance_tracking import load_json,snapshots,utc
    dest=root/'performance/closing_odds';actual=load_json(dest/'summary.json',{});s,rows=evaluate(root,snapshots(root),utc(actual['reviewed_at_utc']))
    if s!=actual or rows!=load_json(dest/'selections.json',[]):raise ValueError('Closing evidence reconciliation failed')
    return True


def main(argv=None):
    from api_key_config import load_api_keys
    from football_value_pipeline_v2_standalone import TheOddsAPI
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--root',type=Path,default=Path('football_output_v2'));parser.add_argument('--watch',action='store_true');parser.add_argument('--max-requests',type=int,default=100);parser.add_argument('--hours',type=float,default=12);args=parser.parse_args(argv)
    if not 1<=args.max_requests<=1000 or not 0<args.hours<=24:parser.error('Requests must be 1..1000 and hours >0..24')
    load_api_keys();key=next((os.getenv(k,'').strip() for k in TheOddsAPI.KEY_ENV_NAMES if os.getenv(k,'').strip()),'')
    if not key:parser.error('Configure an Odds API key in local .env')
    api=TheOddsAPI(key,cache_dir=Path('.football_cache'),force_refresh=True,regions='eu');remaining=args.max_requests;deadline=time.monotonic()+args.hours*3600
    lock=args.root/'closing_odds/collector.lock';lock.parent.mkdir(parents=True,exist_ok=True)
    if lock.exists() and time.time()-lock.stat().st_mtime>1200:lock.unlink()
    try:
        with lock.open('x') as file:file.write(str(os.getpid()))
    except FileExistsError:
        print('Another local closing collector is active; skipped.');return 0
    try:
        while True:
            os.utime(lock,None)
            result=collect_once(args.root,api,limit=remaining);remaining-=result['requests']
            if result['requests'] or not args.watch:print(json.dumps(result))
            if not args.watch or remaining<=0 or time.monotonic()>=deadline:break
            time.sleep(30)
    finally:
        lock.unlink(missing_ok=True)
    return 0


if __name__=='__main__':raise SystemExit(main())
