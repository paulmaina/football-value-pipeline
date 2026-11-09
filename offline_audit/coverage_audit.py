from pathlib import Path
from collections import Counter
import json
import pandas as pd
import performance_tracking as pt
import europa_training as el
import team_research as tr
import turkey_results as trk
from quote_freshness import quote_is_fresh
from price_edge_shortlist import offered_candidates
from profit_shortlist import RULE_V2

ROOT=Path('football_output_v2')
clock=pd.Timestamp('2026-11-09T09:00:23Z')
archive=pt.snapshots(ROOT)
fixtures={}
for meta,rows,_ in archive:
    g=pd.Timestamp(meta['generated_at_utc']); cap=pd.Timestamp(meta['captured_at_utc'])
    summary=pt.load_json(ROOT/'performance'/'snapshots'/meta['git_commit_sha'][:16]/'selection_summary.json',{})
    if summary.get('value_rule')!=RULE_V2:
        continue
    for row in rows:
        kick=pd.Timestamp(row['kickoff_utc'])
        if not pd.Timestamp('2026-11-01T00:00:00Z')<=kick<pd.Timestamp('2026-11-10T00:00:00Z') or not g+pd.Timedelta(minutes=20)<=kick<=g+pd.Timedelta(hours=24) or not g<=cap<=kick-pd.Timedelta(minutes=20):
            continue
        k=pt.fixture_key(row)
        if k not in fixtures or g>fixtures[k][0]:
            fixtures[k]=(g,row)
cache=pt.load_json(ROOT/'performance'/'verified_results.json',{})
verified=[r for r in cache.values() if pt.verified_result_source(r)]
print('Fixture and result cache counts',len(fixtures),Counter(r['league_code'] for r in verified))
evidence_files=list((ROOT/'performance/result_sources/T1/2026').glob('*.csv'))
print('T1 immutable evidence files',len(evidence_files))
print('T1 date coverage',min((x['match_date'] for x in verified if x['league_code']=='T1'),default=None),max((x['match_date'] for x in verified if x['league_code']=='T1'),default=None))
# Existing pinned *training* cache can help identify a missing result, but does not publish a grade.
p=Path('.football_cache/2627_T1.csv')
t1=trk.parse_results(p.read_bytes(),2026,clock.to_pydatetime())
print('T1 training-cache max date',max(x['match_date'] for x in t1))
for g,r in fixtures.values():
    final, why=pt.fixture_match(r,verified)
    if final is not None: continue
    t=pd.Timestamp(r['kickoff_utc'])
    code=pt.LEAGUE_CODES.get(r['league'])
    near=[(c['home_team'],c['away_team'],c.get('kickoff_utc'),round(pt._overlap(r['home_team'],c['home_team'])),round(pt._overlap(r['away_team'],c['away_team']))) for c in verified if c['league_code']==code and c.get('kickoff_utc') and abs(pd.Timestamp(c['kickoff_utc'])-t)<=pd.Timedelta(hours=12)]
    near.sort(key=lambda x:x[-1]+x[-2],reverse=True)
    exact_training = trk.fixture_match(r,t1)[0] if code=='T1' else None
    print('UNGRADED',r['league'],r['home_team'],r['away_team'],str(t),why,'training match',bool(exact_training),'near',near[:1])
counts=Counter()
for now,r in fixtures.values():
    raw=tr.decode(r.get('team_research_json'))
    stats=raw.get('form',{})
    counts[r['league'],'fixture']+=1
    for side in ('home','away'):
        d=stats.get(side,{}).get('all',{})
        if d.get('matches',0)<5: counts[r['league'],'form_below_5']+=1
        if d.get('xg_matches',0)>=5: counts[r['league'],'xg_ge_5']+=1
    if el.eligibility(r):
        print('UEL_MIN',r['home_team'],r['away_team'],r.get('home_training_matches'),r.get('away_training_matches'))
print(pd.Series(counts).unstack(fill_value=0).to_string())
