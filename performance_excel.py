"""Populate the native Excel report template using verified performance rows.

The template supplies styles, native charts and tables. Python's standard
library fills its OOXML cells and formula caches, so Windows and CI do not
need a separate spreadsheet engine. Excel recalculates editable assumptions.
"""
from __future__ import annotations

import argparse
import copy
import csv
from datetime import datetime, timezone
import json
import math
from pathlib import Path
import re
import xml.etree.ElementTree as ET
from zipfile import ZipFile, ZipInfo, ZIP_DEFLATED


TEMPLATE = Path(__file__).parent / 'assets' / 'performance_report_template.xlsx'
REPORT_NAME = 'football_performance_report.xlsx'
NS = 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'
CHART = 'http://schemas.openxmlformats.org/drawingml/2006/chart'
ET.register_namespace('', NS)
ET.register_namespace('c', CHART)


def tag(name):
    return f'{{{NS}}}{name}'


def num(value):
    try:
        x = float(value)
        return x if math.isfinite(x) else None
    except (TypeError, ValueError):
        return None


def col(index):
    result = ''
    while index:
        index, rest = divmod(index-1, 26)
        result = chr(65+rest) + result
    return result


def date_serial(value):
    if not value:
        return None
    try:
        d = datetime.fromisoformat(value.replace('Z', '+00:00'))
        if d.tzinfo is None:
            return None
        return (d.astimezone(timezone.utc) - datetime(1899, 12, 30, tzinfo=timezone.utc)).total_seconds()/86400
    except ValueError:
        return None


class TemplateSheet:
    def __init__(self, xml):
        self.xml = ET.fromstring(xml)
        self.data = self.xml.find(tag('sheetData'))
        self.cache = {}

    def row(self, index, prototype=None):
        existing = self.data.find(f"{tag('row')}[@r='{index}']")
        if existing is not None:
            return existing
        node = copy.deepcopy(prototype) if prototype is not None else ET.Element(tag('row'))
        node.set('r', str(index))
        if prototype is not None:
            for cell in node.findall(tag('c')):
                cell.set('r', re.sub(r'\d+', str(index), cell.get('r')))
                for child in list(cell):
                    cell.remove(child)
                cell.attrib.pop('t', None)
        self.data.append(node)
        return node

    def set(self, address, value=None, formula=None):
        row = self.row(int(re.search(r'\d+', address).group()))
        cell = row.find(f"{tag('c')}[@r='{address}']")
        if cell is None:
            cell = ET.SubElement(row, tag('c'), {'r': address})
        for child in list(cell):
            cell.remove(child)
        cell.attrib.pop('t', None)
        self.cache[address] = value
        if formula:
            ET.SubElement(cell, tag('f')).text = formula.lstrip('=')
            if isinstance(value, str):
                cell.set('t', 'str')
            if value is not None:
                ET.SubElement(cell, tag('v')).text = str(value)
        elif value is None or value == '':
            pass
        elif isinstance(value, (float, int)):
            ET.SubElement(cell, tag('v')).text = str(value)
        else:
            # Literal inline text protects names/source strings beginning with '='.
            cell.set('t', 'inlineStr')
            ET.SubElement(ET.SubElement(cell, tag('is')), tag('t')).text = str(value)

    def fill(self, rows, start=6):
        prototype = copy.deepcopy(self.row(start))
        # Remove all template cells at and below the data row; reserved formatting
        # is represented by column styles and the single cloned data row.
        for r in list(self.data):
            if int(r.get('r')) >= start:
                self.data.remove(r)
        for i, values in enumerate(rows or [[]], start):
            self.row(i, prototype)
            for c, value in enumerate(values, 1):
                if isinstance(value, tuple):
                    self.set(f'{col(c)}{i}', value[1], value[0])
                else:
                    self.set(f'{col(c)}{i}', value)
        self.end = start+max(1, len(rows))-1
        for cf in self.xml.findall(tag('conditionalFormatting')):
            cf.set('sqref', re.sub(r'(\D+)\d+$', lambda m:m[1]+str(self.end), cf.get('sqref')) if ':' in cf.get('sqref') else cf.get('sqref')+':'+re.sub(r'\d+', str(self.end), cf.get('sqref')))

    def bytes(self):
        # Excel requires ascending row and cell order.
        self.data[:] = sorted(self.data, key=lambda r:int(r.get('r')))
        for row in self.data:
            row[:] = sorted(row, key=lambda c:sum((ord(ch)-64)*26**i for i,ch in enumerate(re.match('[A-Z]+',c.get('r')).group()[::-1])))
        dim = self.xml.find(tag('dimension'))
        if dim is not None:
            dim.set('ref', f'A1:{col(max(len(list(r)) for r in self.data))}{max(int(r.get("r")) for r in self.data)}')
        return ET.tostring(self.xml, encoding='utf-8', xml_declaration=True)


def probability(value):
    p = num(value)
    return p if p is not None and 0 <= p <= 1 else None


def prepared_rows(rows):
    seen = set()
    result = []
    for row in sorted(rows, key=lambda r:(r.get('kickoff_utc',''), r.get('fixture_key',''))):
        if row['fixture_key'] in seen:
            raise ValueError('Duplicate frozen fixture in report: '+row['fixture_key'])
        seen.add(row['fixture_key'])
        r = dict(row)
        r['p'] = probability(r.get('predicted_probability'))
        r['y'] = 1 if r['status']=='WON' else 0 if r['status']=='LOST' else None
        r['price'] = num(r.get('offered_decimal_odds'))
        if r['price'] is not None and r['price'] <= 1:
            r['price'] = None
        r['priced'] = r['y'] is not None and r['price'] is not None
        r['scored_p'] = r['p'] if r['y'] is not None else None
        r['brier_value'] = (r['p']-r['y'])**2 if r['scored_p'] is not None else None
        r['policy'] = r.get('selection_policy_version') or 'legacy/unspecified'
        result.append(r)
    return result


def summarize(rows):
    settled = [r for r in rows if r['y'] is not None]
    priced = [r for r in rows if r['priced']]
    prob = [r for r in settled if r['scored_p'] is not None]
    wins = sum(r['y'] for r in settled)
    profit = sum(r['price']-1 if r['y'] else -1 for r in priced)
    mean = sum(r['p'] for r in prob)/len(prob) if prob else None
    observed = sum(r['y'] for r in prob)/len(prob) if prob else None
    return [len(rows), len(settled), wins, len(settled)-wins, len(rows)-len(settled),
            wins/len(settled) if settled else 'n.a.', len(priced),
            profit, profit/len(priced) if priced else 'n.a.',
            sum(r['brier_value'] for r in prob)/len(prob) if prob else 'n.a.',
            mean if prob else 'n.a.', observed if prob else 'n.a.',
            mean-observed if prob else 'n.a.', len(prob)]


def formula_group(dimension, label, rows, end, column=None):
    def rng(c): return f"Selections!${c}$6:${c}${end}"
    criteria = [rng(column), '"'+label.replace('"','""')+'"'] if column else []
    def count(c, condition):
        return 'COUNTIFS('+','.join(criteria+[rng(c), condition])+')'
    def summ(c, condition_col=None, condition=None):
        args = criteria + ([rng(condition_col),condition] if condition_col else [])
        return ('SUMIFS('+','.join([rng(c)]+args)+')') if args else f'SUM({rng(c)})'
    total = ('COUNTIFS('+','.join(criteria)+')') if column else f'COUNTA({rng("A")})'
    wins=count('K','"WON"'); losses=count('K','"LOST"'); n=f'({wins}+{losses})'
    # Scored forecast column is blank unless both a valid probability and outcome exist.
    pn=summ('T')
    expected=summ('S')
    actual='('+summ('L','T','1')+')'
    metrics=summarize(rows)
    fs=[total,n,wins,losses,f'{total}-{n}',f'IF({n}=0,"n.a.",{wins}/{n})',summ('M'),summ('N'),
        f'IF({summ("M")}=0,"n.a.",{summ("N")}/{summ("M")})',
        f'IF({pn}=0,"n.a.",{summ("O")}/{pn})',
        f'IF({pn}=0,"n.a.",{expected}/{pn})',f'IF({pn}=0,"n.a.",{actual}/{pn})',
        f'IF({pn}=0,"n.a.",({expected}-{actual})/{pn})',pn]
    return [dimension,label]+list(zip(fs,metrics))


def review_note(data):
    n=data[-1]
    if n < 30:
        return f'Collect more scored forecasts (n={n}).'
    if isinstance(data[-2], (int,float)) and data[-2] > 0.10:
        return 'Review overconfidence on a future holdout.'
    if isinstance(data[8], (int,float)) and data[8] < 0:
        return 'Review prices and EV on a future holdout.'
    return 'Continue forward testing. No automatic model change.'


def write_workbook(root, selections, predictions, metrics, destination=None):
    root = Path(root)
    destination = Path(destination) if destination else root/'readable'/REPORT_NAME
    rows = prepared_rows(selections)
    end=max(6,5+len(rows))
    with ZipFile(TEMPLATE) as z:
        parts={n:z.read(n) for n in z.namelist()}
    names=['Dashboard','ROI Plan','Breakdowns','Calibration','Selections','Predictions']
    sheets={n:TemplateSheet(parts[f'xl/worksheets/sheet{i}.xml']) for i,n in enumerate(names,1)}
    selection_data=[]
    for i,r in enumerate(rows,6):
        selection_data.append([
            r['fixture_key'],date_serial(r.get('kickoff_utc')),r.get('league'),
            f"{r.get('home_team','')} vs {r.get('away_team','')}",r.get('market'),r.get('selection_tier'),r['policy'],
            r['p'],r['price'],r.get('final_score'),r['status'],r['y'],
            (f'IF(AND(ISNUMBER(L{i}),ISNUMBER(I{i}),I{i}>1),\'ROI Plan\'!$B$5,"")',1 if r['priced'] else ''),
            (f'IF(ISNUMBER(M{i}),M{i}*(I{i}*L{i}-1),"")',(r['price']-1 if r['y'] else -1) if r['priced'] else ''),
            (f'IF(AND(ISNUMBER(L{i}),ISNUMBER(H{i})),(H{i}-L{i})^2,"")',r['brier_value']),
            r.get('week'),r.get('snapshot_commit'),r.get('match_source'),
            (f'IF(AND(ISNUMBER(L{i}),ISNUMBER(H{i})),H{i},"")',r['scored_p']),
            (f'IF(AND(ISNUMBER(L{i}),ISNUMBER(H{i})),1,0)',1 if r['scored_p'] is not None else 0)])
    sheets['Selections'].fill(selection_data)
    ps=[]
    for p in sorted(predictions,key=lambda r:(r.get('kickoff_utc',''),r.get('fixture_key',''))):
        graded=p.get('status')=='GRADED'
        ps.append([p['fixture_key'],date_serial(p.get('kickoff_utc')),p.get('league'),
                   f"{p.get('home_team','')} vs {p.get('away_team','')}",p.get('selection_policy_version') or 'legacy/unspecified',
                   p.get('status'),p.get('final_score')]+[num(p.get(k)) if graded else None for k in
                   ('one_x_two_correct','one_x_two_brier','over_1_5_correct','under_3_5_correct','btts_yes_correct','btts_no_correct')]+
                   [p.get('week'),p.get('snapshot_commit'),p.get('match_source')])
    sheets['Predictions'].fill(ps)
    groups=[('All','All selections',None),('Tier','STRICT','F'),('Tier','PROVISIONAL','F')]
    for dimension,key,column in [('League','league','C'),('Market','market','E'),('Policy','policy','G'),('Week','week','P')]:
        groups += [(dimension,x,column) for x in sorted({r.get(key) for r in rows if r.get(key)})]
    breakdown=[]
    for dim,label,c in groups:
        subset=rows if c is None else [r for r in rows if r.get({'C':'league','E':'market','F':'selection_tier','G':'policy','P':'week'}[c])==label]
        data=formula_group(dim,label,subset,end,c)
        rr=6+len(breakdown)
        note_formula=(f'IF(P{rr}<30,"Collect more scored forecasts (n="&P{rr}&").",'
                      f'IF(O{rr}>0.1,"Review overconfidence on a future holdout.",'
                      f'IF(K{rr}<0,"Review prices and EV on a future holdout.",'
                      '"Continue forward testing. No automatic model change.")))')
        data.append((note_formula,review_note(summarize(subset))))
        breakdown.append(data)
    sheets['Breakdowns'].fill(breakdown)
    cal_rows=[]
    for i,(lo,hi) in enumerate(zip([0,.5,.6,.7,.8,.9],[.5,.6,.7,.8,.9,1.000001]),6):
        subset=[r for r in rows if r['scored_p'] is not None and lo <= r['p'] < hi]
        n=len(subset); d=summarize(subset)
        args=f'Selections!$S$6:$S${end},">="&B{i},Selections!$S$6:$S${end},"<"&C{i},Selections!$T$6:$T${end},1'
        def sums(c):return f'SUMIFS(Selections!${c}$6:${c}${end},{args})'
        cal_rows.append([f'{lo:.0%}–{min(hi,1):.0%}',lo,hi,(f'COUNTIFS({args})',n),
                        (f'IF(D{i}=0,"n.a.",{sums("S")}/D{i})',d[10]),
                        (f'IF(D{i}=0,"n.a.",{sums("L")}/D{i})',d[11]),
                        (f'IF(D{i}=0,"n.a.",E{i}-F{i})',d[12]),
                        (f'IF(D{i}=0,"n.a.",{sums("O")}/D{i})',d[9]),review_note(d)])
    sheets['Calibration'].fill(cal_rows)
    roi=[]; running=0; peak=100
    for i,r in enumerate(rows,10):
        sr=i-4; gain=(r['price']-1 if r['y'] else -1) if r['priced'] else 0
        running+=gain; bank=100+running;peak=max(peak,bank)
        roi.append([r.get('kickoff_utc',''),f"{r.get('home_team','')} vs {r.get('away_team','')}",r['status'],
                    (f'IF(ISNUMBER(Selections!M{sr}),Selections!M{sr},"")',1 if r['priced'] else ''),
                    (f'IF(ISNUMBER(Selections!N{sr}),Selections!N{sr},"")',gain if r['priced'] else ''),
                    (f'SUM($E$10:E{i})',running),(f'$B$4+F{i}',bank),
                    (f'MAX($B$4,$G$10:G{i})',peak),(f'H{i}-G{i}',peak-bank),r.get('week')])
    sheets['ROI Plan'].fill(roi,start=10)
    dash=sheets['Dashboard'];stats=summarize(rows)
    for address,c,index in [('B7','C',0),('B8','D',1),('B9','E',2),('B10','F',3),('B11','G',4),('B12','H',5),('B13','K',8),('B14','J',7),('B15','L',9)]:
        dash.set(address,stats[index],f'Breakdowns!{c}6')
    p_end=max(6,5+len(ps));p_n=sum(num(p.get('one_x_two_correct')) is not None and p.get('status')=='GRADED' for p in predictions)
    p_win=sum(float(p['one_x_two_correct']) for p in predictions if p.get('status')=='GRADED' and num(p.get('one_x_two_correct')) is not None)
    b=[num(p.get('one_x_two_brier')) for p in predictions if p.get('status')=='GRADED' and num(p.get('one_x_two_brier')) is not None]
    dash.set('B16',p_win/p_n if p_n else 'n.a.',f'IF(COUNT(Predictions!H6:H{p_end})=0,"n.a.",AVERAGE(Predictions!H6:H{p_end}))')
    dash.set('B17',sum(b)/len(b) if b else 'n.a.',f'IF(COUNT(Predictions!I6:I{p_end})=0,"n.a.",AVERAGE(Predictions!I6:I{p_end}))')
    n=stats[1];p=stats[5] if n else 0; z=1.96
    centre=(p+z*z/(2*n))/(1+z*z/n) if n else 0
    radius=z*math.sqrt(p*(1-p)/n+z*z/(4*n*n))/(1+z*z/n) if n else 0
    for address,sign,value in [('B18','-',centre-radius),('B19','+',centre+radius)]:
        f=f'IF(B8=0,"n.a.",(B12+1.96^2/(2*B8){sign}1.96*SQRT(B12*(1-B12)/B8+1.96^2/(4*B8^2)))/(1+1.96^2/B8))'
        dash.set(address,value if n else 'n.a.',f)
    for i,br in [(7,7),(8,8)]:
        dash.set(f'E{i}',breakdown[br-6][3][1],f'Breakdowns!D{br}')
        dash.set(f'F{i}',breakdown[br-6][7][1],f'Breakdowns!H{br}')
    status='Awaiting verified results' if not n else 'Early sample: continue forward testing' if n < 30 else 'Review calibration and ROI by segment'
    dash.set('D11',status,'IF(B8=0,"Awaiting verified results",IF(B8<30,"Early sample: continue forward testing","Review calibration and ROI by segment"))')
    dash.set('D14',f'{n} settled; {stats[4]} pending / unverified')
    dash.set('A21','Conclusion: '+('No settled selections yet. Win rate and ROI are unavailable.' if not n else f'{stats[2]} wins from {n} settled selections. '+('Early evidence; do not retune from this sample.' if n < 30 else 'Compare calibration and simulated ROI across policies before any manual change.')))
    errors=metrics.get('provider_errors') or {}
    dash.set('A26','Result-source issues: '+('; '.join(f'{k}: {v}' for k,v in sorted(errors.items())) if errors else 'none recorded'))
    dash.set('A29','Review notes use 30 scored samples as a prompt, not statistical proof. Reassess on a future holdout.')
    dash.set('A27','Review as of UTC: '+str(metrics.get('reviewed_at_utc') or 'not recorded in source'))
    dash.set('A28','PROVISIONAL is a research watchlist. Positive simulated ROI does not establish profitability.')
    dash.set('D16','Forecast metric');dash.set('E16','Samples');dash.set('F16','Accuracy')
    for rr,label,c,key in [(17,'Over 1.5','J','over_1_5_correct'),(18,'Under 3.5','K','under_3_5_correct'),(19,'BTTS Yes','L','btts_yes_correct'),(20,'BTTS No','M','btts_no_correct')]:
        vals=[num(p.get(key)) for p in predictions if p.get('status')=='GRADED' and num(p.get(key)) is not None]
        dash.set(f'D{rr}',label)
        dash.set(f'E{rr}',len(vals),f'COUNT(Predictions!{c}6:{c}{p_end})')
        dash.set(f'F{rr}',sum(vals)/len(vals) if vals else 'n.a.',f'IF(E{rr}=0,"n.a.",AVERAGE(Predictions!{c}6:{c}{p_end}))')
    # Extend table bounds and their filters to the actual populated records.
    table_sheets={'BreakdownsTable':'Breakdowns','CalibrationTable':'Calibration','SelectionsTable':'Selections','PredictionsTable':'Predictions','ROILedger':'ROI Plan'}
    for path in list(parts):
        if path.startswith('xl/tables/') and path.endswith('.xml'):
            xml=ET.fromstring(parts[path]);sheet=sheets[table_sheets[xml.get('name')]]
            ref=xml.get('ref');last=re.sub(r'\d+$',str(sheet.end),ref.split(':')[-1]);xml.set('ref',ref.split(':')[0]+':'+last)
            af=xml.find(tag('autoFilter'))
            if af is not None:af.set('ref',xml.get('ref'))
            parts[path]=ET.tostring(xml,encoding='utf-8',xml_declaration=True)
        elif re.search(r'/charts/chart[^/]*\.xml$',path) and path.endswith('.xml'):
            xml=ET.fromstring(parts[path])
            for ref in xml.iter():
                if ref.tag not in (f'{{{CHART}}}numRef',f'{{{CHART}}}strRef'):
                    continue
                f=ref.find(f'{{{CHART}}}f')
                if f is None or not f.text:continue
                text=f.text
                if 'ROI Plan' in text:text=re.sub(r'\$11$',f'${sheets["ROI Plan"].end}',text)
                f.text=text
                match=re.search(r"'?([^'!]+)'?!\$(\w+)\$(\d+):\$\w+\$(\d+)",text)
                if not match:continue
                sn,c,a,brow=match.groups();sn=sn.strip("'")
                values=[sheets[sn].cache.get(f'{c}{i}') for i in range(int(a),int(brow)+1)]
                numeric=ref.tag.endswith('numRef')
                for child in list(ref):
                    if child is not f:ref.remove(child)
                cache=ET.SubElement(ref,f'{{{CHART}}}'+('numCache' if numeric else 'strCache'))
                if numeric:ET.SubElement(cache,f'{{{CHART}}}formatCode').text='General'
                ET.SubElement(cache,f'{{{CHART}}}ptCount',{'val':str(len(values))})
                for i,v in enumerate(values):
                    if v is None or (numeric and not isinstance(v,(int,float))):continue
                    ET.SubElement(ET.SubElement(cache,f'{{{CHART}}}pt',{'idx':str(i)}),f'{{{CHART}}}v').text=str(v)
            parts[path]=ET.tostring(xml,encoding='utf-8',xml_declaration=True)
    for i,name in enumerate(names,1):parts[f'xl/worksheets/sheet{i}.xml']=sheets[name].bytes()
    wb=ET.fromstring(parts['xl/workbook.xml']);calc=wb.find(tag('calcPr'))
    if calc is None:calc=ET.SubElement(wb,tag('calcPr'))
    calc.set('fullCalcOnLoad','1');calc.set('calcMode','auto')
    parts['xl/workbook.xml']=ET.tostring(wb,encoding='utf-8',xml_declaration=True)
    # Remove an exported template calculation chain after replacing formulas.
    parts.pop('xl/calcChain.xml',None)
    for path in ['[Content_Types].xml','xl/_rels/workbook.xml.rels']:
        xml=ET.fromstring(parts[path])
        for child in list(xml):
            if 'calcChain' in json.dumps(child.attrib):xml.remove(child)
        ET.register_namespace('',xml.tag.split('}')[0][1:])
        parts[path]=ET.tostring(xml,encoding='utf-8',xml_declaration=True)
    ET.register_namespace('',NS)
    destination.parent.mkdir(parents=True,exist_ok=True)
    temp=destination.with_suffix('.tmp')
    with ZipFile(temp,'w',ZIP_DEFLATED) as z:
        for path,data in sorted(parts.items()):
            info=ZipInfo(path,date_time=(1980,1,1,0,0,0));info.compress_type=ZIP_DEFLATED
            z.writestr(info,data)
    if destination.exists() and destination.read_bytes()==temp.read_bytes():temp.unlink()
    else:temp.replace(destination)
    return destination


def export_existing(root=Path('football_output_v2'), destination=None):
    root=Path(root);p=root/'performance'
    required=[p/'metrics.json',p/'shortlist_grades.csv',p/'prediction_grades.csv']
    if not all(x.exists() for x in required):return None
    def read(path):
        with path.open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
    return write_workbook(root,read(required[1]),read(required[2]),json.loads(required[0].read_text()),destination)


def main(argv=None):
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root',type=Path,default=Path('football_output_v2'))
    args=parser.parse_args(argv)
    path=export_existing(args.root)
    if path is None:parser.error('Run performance_tracking.py review first to generate verified grades.')
    print(path)
    return 0


if __name__=='__main__':raise SystemExit(main())
