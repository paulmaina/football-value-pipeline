"""Offline availability audit. Join archived xG only by identity, date and score."""
import math
from collections import Counter, defaultdict
from pathlib import Path
import pandas as pd
import europa_training as el
import performance_tracking as pt
import team_research as tr

ROOT=Path('football_output_v2')
resolve=el.resolver()
def key(row):
    when=tr.utc(row.get('date'))
    home,away=resolve(row.get('home') or ''),resolve(row.get('away') or '')
    if pd.isna(when) or not home or not away or home==away:
        return None
    return when.date(),home,away,row.get('home_goals'),row.get('away_goals')
def xg(row):
    pair=tr.number(row.get('home_xg')),tr.number(row.get('away_xg'))
    return pair if all(x is not None and math.isfinite(x) and x>=0 for x in pair) else None
archive=pt.snapshots(ROOT)
seen={}
europe={}
cols=Counter()
indexed=defaultdict(list)
for m, rows, _ in archive:
    now=tr.utc(m['generated_at_utc'])
    for row in rows:
        kickoff=tr.utc(row.get('kickoff_utc'))
        if row['league'] in ('UEFA Europa League','UEFA Champions League'):
            if (row.get('score_matrix_version')=='published-score-matrix-v1' and
                now+pd.Timedelta(minutes=20)<=kickoff<=now+pd.Timedelta(hours=24) and
                tr.utc(m['captured_at_utc'])<=kickoff-pd.Timedelta(minutes=20)):
                k=(row['league'],kickoff,resolve(row['home_team']),resolve(row['away_team']))
                if k not in europe or now>europe[k][0]:
                    europe[k]=now,row
            continue
        histories=tr.decode(row.get('research_history_json'))
        for side in ('home','away'):
            for item in histories.get(side,[]):
                k,pair=key(item),xg(item)
                if k and pair and k[0]<now.date():
                    indexed[k].append((now,pair))
for (_,kick,*_), (now,row) in europe.items():
    frozen=tr.decode(row.get('team_research_json'))
    cutoff=tr.utc(frozen.get('observed_at_utc'))
    if pd.isna(cutoff) or cutoff>now:
        cols['missing cutoff']+=1
        continue
    cols['european fixtures']+=1
    saved=tr.decode(row.get('research_history_json'))
    recent=frozen.get('evidence',{}).get('recent',{})
    joined={}
    for side in ('home','away'):
        club=resolve(row[side+'_team'])
        records={}
        for item in saved.get(side,[])+recent.get(side,[]):
            k=key(item)
            if k and k[0]<cutoff.date() and club in k[1:3]:
                records.setdefault(k,item)
        evidence_rows=sorted(records,key=lambda k:k[0],reverse=True)[:10]
        values=[]
        for k in evidence_rows:
            own=xg(records[k])
            pool={pair for observed,pair in indexed[k] if observed<=cutoff}
            if own is None and len(pool)==1:
                values.append(next(iter(pool)))
            elif own is not None:
                values.append(own)
        joined[side]=len(values)
        cols['new exact xG rows']+=sum(xg(records[k]) is None and len({pair for observed,pair in indexed[k] if observed<=cutoff})==1 for k in evidence_rows)
        if len(values)>=5:
            cols['teams with five xG matches']+=1
    if all(n>=5 for n in joined.values()):
        cols['fixtures with enough xG on both sides']+=1
print('Domestic xG index matches:',len(indexed))
print('Strict cutoff-safe cross-competition xG joins:',dict(cols))
# The grid and quote have different provenance. Count explicit capture time
# availability only and never use generation time as the grid's build time.
fields=['score_matrix_generated_at_utc','market_reference_1x2_last_update_utc','totals_anchor_reference_last_update_utc']
for meta, rows, _ in archive:
    for row in rows:
        if row.get('score_matrix_version')=='published-score-matrix-v1':
            seen[(meta['git_commit_sha'],pt.fixture_key(row))]=row
print('Archived grid rows',len(seen))
for field in fields:
    print(field,sum(pd.notna(tr.utc(row.get(field))) for row in seen.values()))
