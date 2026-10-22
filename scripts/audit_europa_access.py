"""Bounded read-only provider probe; persist only allowlisted aggregate diagnostics."""
from collections import Counter
from datetime import datetime, timezone
import json
import math
import os
from pathlib import Path
import time

import requests

BASES = {'football_data':'https://api.football-data.org/v4',
         'api_football':'https://v3.football.api-sports.io',
         'bbs':'https://api.bigballsdata.com', 'odds':'https://api.the-odds-api.com/v4'}
SECRET_NAMES = ('FOOTBALL_DATA_API_KEY','API_FOOTBALL_KEY','BBS_API_KEY',
                'THE_ODDS_API_KEY','THE_ODDS_API_KEY_FALLBACK_1','THE_ODDS_API_KEY_FALLBACK_2')
BOOKS = {'pinnacle':'Pinnacle','bet365':'bet365','onexbet':'1xBet'}


def europa(value):
    name = ''.join(c for c in str(value).lower() if c.isalnum())
    return name in ('europaleague','uefaeuropaleague')


def items(payload):
    if isinstance(payload,list): return payload
    if not isinstance(payload,dict): return []
    for key in ('response','matches','competitions','data','leagues','items','results'):
        value=payload.get(key)
        if isinstance(value,list): return value
        if isinstance(value,dict):
            found=items(value)
            if found: return found
    return []


def find_leagues(payload):
    result=[]
    if isinstance(payload,list):
        for value in payload: result.extend(find_leagues(value))
    elif isinstance(payload,dict):
        if any(europa(payload.get(k)) for k in ('name','title','league','display_name','league_name')): result.append(payload)
        for value in payload.values():
            if isinstance(value,(dict,list)): result.extend(find_leagues(value))
    return result


def valid_score(value):
    return isinstance(value,dict) and all(type(value.get(s)) is int and 0 <= value[s] <= 30 for s in ('home','away'))


def utc(value):
    try:
        clock=datetime.fromisoformat(str(value).replace('Z','+00:00'))
        return clock.astimezone(timezone.utc) if clock.tzinfo else None
    except (ValueError,TypeError): return None


def summarize(rows, provider, year):
    seen=set();statuses=Counter();teams=Counter();dates=[];scored=regular=wrong=duplicates=0
    for row in rows:
        if provider=='api_football':
            fixture=row.get('fixture',{}); identity=fixture.get('id'); stamp=fixture.get('date')
            status=fixture.get('status',{}).get('short'); score=row.get('score',{}).get('fulltime')
            participants=row.get('teams',{}); finished=status in ('FT','AET','PEN')
            regulation=status=='FT'; competition=row.get('league',{}).get('id')==3
        elif provider=='football_data':
            identity=row.get('id');stamp=row.get('utcDate');status=row.get('status')
            score=row.get('score',{}).get('fullTime');finished=status=='FINISHED'
            regulation=row.get('score',{}).get('duration')=='REGULAR'
            participants={'home':row.get('homeTeam',{}),'away':row.get('awayTeam',{})}
            competition=row.get('competition',{}).get('code')=='EL'
        else:
            identity=row.get('id');stamp=row.get('kickoff_utc');status=row.get('status')
            score=row.get('score');finished=status=='finished';regulation=False
            participants={s:row.get(s,{}) for s in ('home','away')}
            competition=europa(row.get('league')) and row.get('sport')=='football'
        date=utc(stamp)
        if (not competition or not date or not datetime(year,6,1,tzinfo=timezone.utc)<=date<datetime(year+1,7,1,tzinfo=timezone.utc)
                or identity is None): wrong+=1;continue
        if str(identity) in seen: duplicates+=1;continue
        seen.add(str(identity));statuses[str(status)]+=1;dates.append(date.isoformat())
        if finished and valid_score(score):
            scored+=1;regular+=int(regulation)
            for side in ('home','away'):
                team=participants.get(side) or {}; name=team.get('id') or team.get('name')
                if name is not None: teams[str(name)]+=1
    return {'fixtures':len(seen),'statuses':dict(statuses),'finished_with_scores':scored,
            'regulation_confirmed':regular,'teams_in_scored_matches':len(teams),
            'minimum_scored_matches_per_team':min(teams.values(),default=0),
            'first_kickoff':min(dates,default=None),'last_kickoff':max(dates,default=None),
            'wrong_competition_season_or_identity':wrong,'duplicate_fixture_ids':duplicates}


class Probe:
    def __init__(self, session=None, sleeper=time.sleep):
        self.session=session or requests.Session();self.sleep=sleeper;self.calls=[];self.stopped=set();self.last={}

    def get(self, provider, path, label, params=None, key=None):
        if provider in self.stopped: return None, {'status':'STOPPED_AFTER_ACCESS_OR_QUOTA_ERROR'}
        if len(self.calls)>=40: return None, {'status':'GLOBAL_REQUEST_CAP'}
        names={'football_data':'FOOTBALL_DATA_API_KEY','api_football':'API_FOOTBALL_KEY','bbs':'BBS_API_KEY','odds':'THE_ODDS_API_KEY'}
        key=key or os.getenv(names[provider],'').strip()
        record={'provider':provider,'query':label}
        if not key: return None, {**record,'status':'KEY_NOT_CONFIGURED'}
        elapsed=time.monotonic()-self.last.get(provider,0)
        self.sleep(max(0, (6.2 if provider=='football_data' else .35)-elapsed))
        headers={};query=dict(params or {})
        if provider=='football_data':headers['X-Auth-Token']=key
        elif provider=='api_football':headers['x-apisports-key']=key
        elif provider=='bbs':headers['Authorization']='Bearer '+key
        else:query['apiKey']=key
        self.last[provider]=time.monotonic()
        try:
            response=self.session.get(BASES[provider]+path,params=query,headers=headers,timeout=(10,30),allow_redirects=False)
            record['http']=response.status_code
            for header in ('x-requests-remaining','x-requests-used','x-requests-last','x-ratelimit-remaining','x-ratelimit-requests-remaining'):
                value=response.headers.get(header)
                if value is not None and str(value).replace('.','',1).isdigit():record[header]=str(value)
            try: payload=response.json()
            except (ValueError,TypeError):payload=None
            errors=payload.get('errors') if isinstance(payload,dict) else None
            error_text=json.dumps(errors or payload or {}).lower() if response.status_code>=400 or errors else ''
            if errors:
                record['error_categories']=[name for name in ('plan','requests','rateLimit','token') if isinstance(errors,dict) and name in errors]
                record['limit_scope']=('minute' if 'minute' in error_text else 'daily' if 'day' in error_text else 'unspecified')
            if response.status_code==401:state='AUTHENTICATION_FAILED'
            elif response.status_code==403:state='ACCESS_DENIED'
            elif response.status_code==429:state='QUOTA_OR_RATE_LIMIT'
            elif response.status_code>=400:state=('UNKNOWN_COMPETITION' if any(t in error_text for t in ('unknown league','unrecognised league','unrecognized league','unsupported league')) else 'HTTP_ERROR')
            elif not 200<=response.status_code<300:state='REDIRECT_NOT_FOLLOWED'
            elif errors:
                error_keys=set(errors) if isinstance(errors,dict) else set()
                state=('PLAN_RESTRICTED' if 'plan' in error_keys else
                       'QUOTA_OR_RATE_LIMIT' if error_keys.intersection(('requests','rateLimit')) else
                       'AUTHENTICATION_FAILED' if 'token' in error_keys else 'PROVIDER_ERROR')
            elif payload is None:state='NON_JSON_RESPONSE'
            else:state='OK'
            record['status']=state
            if state in ('AUTHENTICATION_FAILED','QUOTA_OR_RATE_LIMIT'):self.stopped.add(provider)
            if any(record.get(h)=='0' for h in ('x-ratelimit-remaining','x-ratelimit-requests-remaining')):self.stopped.add(provider)
            self.calls.append(record)
            return (payload if state=='OK' else None),record
        except requests.RequestException:
            record['status']='NETWORK_ERROR';self.calls.append(record)
            return None,record  # Never log exception URLs, bodies, headers or credentials.


def historical(probe, provider, year, params=None):
    rows=[];complete=False;last={}
    path={'football_data':'/competitions/EL/matches','api_football':'/fixtures','bbs':'/v1/matches'}[provider]
    for page in range(1,4):
        query={'season':year,**(params or {})}
        if provider=='api_football' and page>1:query['page']=page
        if provider=='bbs':query.update(limit=200,offset=len(rows))
        payload,last=probe.get(provider,path,f'season_{year}_page_{page}',query)
        if payload is None:break
        batch=items(payload);rows.extend(batch)
        if provider=='football_data':complete=isinstance(payload.get('matches'),list);break
        if provider=='api_football':
            total=payload.get('paging',{}).get('total',1)
            if page>=total:complete=True;break
        else:
            pagination=payload.get('pagination') or payload.get('meta',{}).get('pagination') or payload.get('meta',{})
            total=pagination.get('total')
            if (isinstance(total,int) and len(rows)>=total) or (total is None and len(batch)<200):complete=True;break
        if not batch:break
    return {**summarize(rows,provider,year),'request_status':last.get('status'),
            'all_reported_pages_read':complete,'pagination_cap':3}


def market_coverage(event, now):
    result={name:{'markets':{},'handicap_lines':[],'fresh_markets':0} for name in BOOKS.values()}
    for book in event.get('bookmakers',[]):
        name=BOOKS.get(book.get('key'))
        if name is None:continue
        for market in book.get('markets',[]):
            key=market.get('key');outcomes=market.get('outcomes',[])
            prices=[o.get('price') for o in outcomes]
            valid=bool(prices) and all(type(p) in (int,float) and math.isfinite(p) and p>1 for p in prices)
            if not valid:continue
            # These are offered coverage counts, not execution/calibration approval.
            result[name]['markets'][key]=len(outcomes)
            stamp=utc(market.get('last_update') or book.get('last_update'))
            result[name]['fresh_markets']+=int(stamp is not None and -300<=(now-stamp).total_seconds()<=86400)
            if key in ('spreads','alternate_spreads'):
                lines={float(o['point']) for o in outcomes if type(o.get('point')) in (int,float) and math.isfinite(o['point']) and -3<=o['point']<=3}
                result[name]['handicap_lines']=sorted(set(result[name]['handicap_lines'])|lines)
    return result


def run(probe=None, now=None):
    probe=probe or Probe();now=now or datetime.now(timezone.utc)
    requested=os.getenv('AUDIT_PROVIDERS','all').split(',')
    selected=set(BASES) if requested==['all'] else set(requested) & set(BASES)
    year=now.year if now.month>=7 else now.year-1
    report={'competition':'UEFA Europa League','checked_at_utc':now.isoformat(),'seasons_tested':list(range(year-4,year+1)),
        'limits':{'total_requests':40,'pages_per_season':3,'odds_sample_events':1},'providers':{},'providers_requested':sorted(selected),
        'limitations':['Returned match counts do not prove season completeness or prediction accuracy.',
            'No model fitting, calibration audit or profitability backtest was performed.',
            'Cup scores after extra time/penalties need verified 90-minute semantics; unverified scores are not training-approved.',
            'One odds event is a coverage sample, not a guarantee across fixtures or bookmakers.']}
    for provider in ('football_data','api_football','bbs'):
        names={'football_data':'FOOTBALL_DATA_API_KEY','api_football':'API_FOOTBALL_KEY','bbs':'BBS_API_KEY'}
        section={'configured':bool(os.getenv(names[provider],'').strip()),'tested':provider in selected,'seasons':{}};report['providers'][provider]=section
        if not section['configured'] or provider not in selected:continue
        if provider=='api_football':
            payload,state=probe.get(provider,'/leagues','competition_discovery',{'name':'UEFA Europa League'})
            found=find_leagues(payload);section['discovery_status']=state['status'];section['competition_found']=bool(found)
            # Official competition identity is checked in every returned fixture.
            params={'league':3}
        elif provider=='bbs':
            coverage,state=probe.get(provider,'/v1/coverage','coverage_catalogue',{'sport':'football'})
            payload,state=probe.get(provider,'/v1/leagues','competition_discovery',{'sport':'football'})
            found=find_leagues(payload);section['discovery_status']=state['status'];section['competition_found']=bool(found)
            if not found:
                section['coverage_catalogue_mentions_europa']=bool(find_leagues(coverage))
                found=[{'name':'UEFA Europa League'}]  # Test documented exact-name resolver without guessing a league id.
            league=found[0];params={'sport':'football','league':league.get('code') or league.get('slug') or league.get('name')}
        else:
            payload,state=probe.get(provider,'/competitions/EL','competition_access')
            section['discovery_status']=state['status']
            if payload is None:continue
            section['competition_found']=payload.get('code')=='EL';params={}
        for season in (year,year-1,year-2,year-3,year-4):
            section['seasons'][str(season)]=historical(probe,provider,season,params)
            if provider in probe.stopped or section['seasons'][str(season)]['request_status']=='UNKNOWN_COMPETITION':break
    odds={'configured':any(os.getenv(n,'').strip() for n in SECRET_NAMES[3:]),'tested':'odds' in selected};report['providers']['odds']=odds
    for slot,name in enumerate(SECRET_NAMES[3:] if 'odds' in selected else (),1):
        key=os.getenv(name,'').strip()
        if not key:continue
        odds['configured']=True;probe.stopped.discard('odds')
        payload,state=probe.get('odds','/sports/soccer_uefa_europa_league/odds','upcoming_1x2',
            {'regions':'eu,uk','markets':'h2h','oddsFormat':'decimal'},key)
        odds['request_status']=state['status'];odds['key_slot_used']=slot
        if payload is None:continue
        events=[e for e in items(payload) if e.get('sport_key')=='soccer_uefa_europa_league']
        future=[e for e in events if utc(e.get('commence_time')) and utc(e['commence_time'])>now]
        odds['upcoming_events']=len(future)
        odds['bookmaker_event_counts']={label:sum(any(b.get('key')==book for b in e.get('bookmakers',[])) for e in future) for book,label in BOOKS.items()}
        if future:
            sample=min(future,key=lambda e:e['commence_time']);odds['sample_kickoff']=sample['commence_time']
            details,state=probe.get('odds',f"/sports/soccer_uefa_europa_league/events/{sample['id']}/odds",'one_event_additional_markets',
                {'regions':'eu,uk','markets':'spreads,alternate_spreads,draw_no_bet,double_chance,alternate_totals','oddsFormat':'decimal'},key)
            odds['additional_markets_status']=state['status']
            odds['sample_market_coverage']=market_coverage(details or sample,now)
        payload,state=probe.get('odds','/sports/soccer_uefa_europa_league/scores','recent_result_verification',{'daysFrom':3},key)
        odds['recent_scores_status']=state['status'];odds['completed_results_in_three_day_window']=sum(bool(e.get('completed')) and bool(e.get('scores')) for e in items(payload))
        break
    report['requests']=probe.calls
    report['request_count']=len(probe.calls)
    report['assessment']='ACCESS_AUDIT_ONLY; use evidence below to decide whether to build an experimental model'
    return report


def main():
    report=run();output=Path('workflow_artifacts/europa_access');output.mkdir(parents=True,exist_ok=True)
    text=json.dumps(report,indent=2,allow_nan=False)
    # Defense in depth: never persist an accidentally reflected credential.
    for name in SECRET_NAMES:
        value=os.getenv(name,'').strip()
        if value:text=text.replace(value,'[REDACTED]')
    (output/'report.json').write_text(text+'\n',encoding='utf-8')
    print(text)
    if os.getenv('GITHUB_STEP_SUMMARY'):
        with open(os.environ['GITHUB_STEP_SUMMARY'],'a',encoding='utf-8') as handle:
            handle.write('# Europa League access audit\n\nCoverage test only; no production outputs changed.\n\n```json\n'+text+'\n```\n')


if __name__=='__main__':main()
