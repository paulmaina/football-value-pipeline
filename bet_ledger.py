"""Private user-recorded placed bets; never infer execution from a recommendation."""
import csv
from datetime import datetime, timezone
import json
import math
from pathlib import Path

DIRECTORY = Path('.football_bets')
INPUT = DIRECTORY/'placed_bets.csv'
FIELDS = ['bet_id','placed_at_utc','recorded_at_utc','league','home_team','away_team','kickoff_utc',
          'market','handicap_side','handicap_line','bookmaker','offered_decimal_odds','stake','currency','per_stake_cost','odds_event_id']


def validate(rows):
    from performance_tracking import utc
    from asian_handicap import parse_label
    supported = {'Home win','Away win','Double Chance 1X','Double Chance X2','Double Chance 12','Over 1.5'}
    seen = set(); result=[]
    for row in rows:
        row = dict(row)
        for key in ('bet_id','league','home_team','away_team','bookmaker','market','currency'):
            if not str(row.get(key) or '').strip(): raise ValueError('Missing placed-bet '+key)
            row[key]=str(row[key]).strip()
        if row['bet_id'] in seen: raise ValueError('Duplicate placed bet_id')
        seen.add(row['bet_id'])
        row['currency']=row['currency'].upper()
        if len(row['currency'])!=3 or not row['currency'].isalpha(): raise ValueError('Invalid placed-bet currency')
        for field in ('placed_at_utc','kickoff_utc'):
            if datetime.fromisoformat(str(row.get(field) or '').replace('Z','+00:00')).tzinfo is None:
                raise ValueError('Placed-bet timestamps require a timezone')
        placed,kick = utc(row.get('placed_at_utc')),utc(row.get('kickoff_utc'))
        if placed is None or kick is None or placed >= kick: raise ValueError('Placed bet must predate kickoff')
        if row['market'] not in supported and parse_label(row['market']) is None: raise ValueError('Unsupported placed-bet market')
        for key in ('stake','offered_decimal_odds','per_stake_cost'):
            try: value=float(row.get(key) or 0)
            except (TypeError,ValueError): raise ValueError('Invalid placed-bet '+key)
            if not math.isfinite(value) or (value<=0 if key=='stake' else value<=1 if key=='offered_decimal_odds' else not 0<=value<=1):
                raise ValueError('Invalid placed-bet '+key)
            row[key]=value
        row['placed_at_utc']=placed.isoformat();row['kickoff_utc']=kick.isoformat()
        # The market label is authoritative for AH, avoiding contradictory manual side/line fields.
        ah=parse_label(row['market'])
        if ah: row['handicap_side'],row['handicap_line']=ah
        row.update(evaluation_view='user_recorded_placed_bets')
        result.append(row)
    return result


def read(path):
    from csv_utils import dict_reader
    with Path(path).open(encoding='utf-8-sig',newline='') as stream:
        return validate(list(dict_reader(stream)))


def write(path,rows):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    temporary=path.with_suffix('.tmp')
    try:
        with temporary.open('w',encoding='utf-8',newline='') as stream:
            writer=csv.DictWriter(stream,fieldnames=FIELDS,extrasaction='ignore');writer.writeheader();writer.writerows(rows)
        temporary.replace(path)
    finally: temporary.unlink(missing_ok=True)


def review_private(root,observations,records,clock):
    import pandas as pd
    from price_edge_tracking import grade
    root=Path(root);path=root/INPUT
    if not path.exists(): return {'status':'NOT_RECORDED','note':'Recommendations are not executed bets'}
    try:
        bets=read(path)
        from performance_tracking import utc
        if any(utc(row['placed_at_utc'])>clock for row in bets): raise ValueError('Placed bet after report clock')
    except (ValueError,KeyError,TypeError,OSError,UnicodeError,csv.Error) as exc:
        summary={'status':'INVALID_PRIVATE_LEDGER','reason':str(exc),'roi':None}
        (path.parent/'summary.json').write_text(json.dumps(summary),encoding='utf-8')
        (path.parent/'graded_bets.csv').unlink(missing_ok=True)
        return {'status':'INVALID_PRIVATE_LEDGER','reason':str(exc)}
    frame=grade(bets,observations,records,clock)
    by_currency={}
    if len(frame):
        frame['cash_profit']=pd.to_numeric(frame.stake)*pd.to_numeric(frame.unit_profit,errors='coerce')
        settled=frame.loc[frame.cash_profit.notna()]
        for currency,part in settled.groupby('currency'):
            stake,profit=float(part.stake.sum()),float(part.cash_profit.sum())
            by_currency[currency]=dict(graded=len(part),graded_stake=stake,cash_profit=profit,roi=profit/stake if stake else None)
    else: settled=frame
    summary=dict(status='USER_RECORDED_BETS',bets=len(bets),graded=len(settled),by_currency=by_currency,
                 note='User-reported execution, not broker-verified; pending bets excluded from ROI; currencies never combined')
    dest=root/DIRECTORY;dest.mkdir(parents=True,exist_ok=True)
    frame.to_csv(dest/'graded_bets.csv',index=False)
    (dest/'summary.json').write_text(json.dumps(summary,indent=2),encoding='utf-8')
    # Public pipeline reports disclose status only. Private stakes/ROI stay in the ignored directory.
    return {'status':'AVAILABLE_PRIVATELY','note':'See .football_bets/summary.json; not mixed with model evaluation'}


def main():
    import argparse
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action',choices=('init','add'))
    parser.add_argument('--root',type=Path,default=Path('football_output_v2'))
    parser.add_argument('--file',type=Path,help='One user-recorded placed bet as JSON')
    args=parser.parse_args();path=args.root/INPUT
    if args.action=='init':
        if path.exists(): parser.error('Ledger already exists')
        write(path,[])
    else:
        if args.file is None: parser.error('--file is required for add')
        row=json.loads(args.file.read_text(encoding='utf-8'))
        row['recorded_at_utc']=datetime.now(timezone.utc).isoformat()
        write(path,validate([*(read(path) if path.exists() else []),row]))
    print(path)


if __name__=='__main__': main()
