"""Readable monitoring views for the generated report (standard library only).

Presentation is applied after the evidence calculations. Existing ledger cells,
formula caches, native tables and editable simulation inputs are preserved.
"""
from __future__ import annotations

import copy
import json
import math
from pathlib import Path
import re
import tempfile
import os
import xml.etree.ElementTree as ET
from zipfile import ZipFile, ZipInfo, ZIP_DEFLATED

NS = 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'
REL = 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'
PKG = 'http://schemas.openxmlformats.org/package/2006/relationships'
CT = 'http://schemas.openxmlformats.org/package/2006/content-types'
C = 'http://schemas.openxmlformats.org/drawingml/2006/chart'
A = 'http://schemas.openxmlformats.org/drawingml/2006/main'
XDR = 'http://schemas.openxmlformats.org/drawingml/2006/spreadsheetDrawing'
NAMES = {
    'goal_blend_experiment': 'Goal-market blend',
    'market_led_experiment': 'Market-led forecasts',
    'recency_experiment': 'Recency comparison',
    'filter_sensitivity_experiment': 'EV filter sensitivity',
    'benchmark_forward_experiment': '85% market weight',
    'totals_anchor_experiment': 'Pinnacle totals anchor',
    'reliability:stronger_l2': 'Stronger regularisation (L2=3)',
    'reliability:fixed_half_life': 'Fixed half-life (480 days)',
    'shortlist_policy_experiment': 'Probability / calibration policy',
    'shortlist_weight_experiment': 'Shortlist probability / EV weights',
}


def q(name):
    return f'{{{NS}}}{name}'


def xml_bytes(root):
    # OPC readers expect the content-types namespace as the default namespace.
    # Keep package XML portable across Excel and strict OpenXML readers.
    namespace = root.tag.split('}')[0][1:]
    ET.register_namespace('', namespace)
    data = ET.tostring(root, encoding='utf-8', xml_declaration=True)
    ET.register_namespace('', NS)
    return data


def text(cell):
    if cell is None:
        return None
    v = cell.find(q('v'))
    if v is not None:
        if cell.get('t') in ('str', 'e'):
            return v.text
        try:
            return float(v.text)
        except (ValueError, TypeError):
            return v.text
    return ''.join(t.text or '' for t in cell.iter(q('t'))) or None


def column(i):
    result = ''
    while i:
        i, rem = divmod(i - 1, 26)
        result = chr(65 + rem) + result
    return result


def label(value):
    return str(value).replace('_', ' ').lower().capitalize() if value else 'Unavailable'


class Sheet:
    def __init__(self, root=None):
        self.root = root if root is not None else ET.Element(q('worksheet'))
        self.data = self.root.find(q('sheetData'))
        if self.data is None:
            self.data = ET.SubElement(self.root, q('sheetData'))

    def cell(self, address):
        nr = re.search(r'\d+', address).group()
        row = self.data.find(f"{q('row')}[@r='{nr}']")
        if row is None:
            row = ET.SubElement(self.data, q('row'), {'r': nr})
        cell = row.find(f"{q('c')}[@r='{address}']")
        return cell if cell is not None else ET.SubElement(row, q('c'), {'r': address})

    def put(self, address, value, style=None, formula=None):
        cell = self.cell(address)
        cell[:] = []
        cell.attrib.pop('t', None)
        if style is not None:
            cell.set('s', str(style))
        if formula:
            ET.SubElement(cell, q('f')).text = formula.lstrip('=')
        if value is None or value == '':
            return
        if isinstance(value, (int, float)) and math.isfinite(value):
            ET.SubElement(cell, q('v')).text = str(value)
        elif formula:
            cell.set('t', 'str')
            ET.SubElement(cell, q('v')).text = str(value)
        else:
            cell.set('t', 'inlineStr')
            ET.SubElement(ET.SubElement(cell, q('is')), q('t')).text = str(value)

    def row(self, nr, values, styles, header=False):
        for i, value in enumerate(values, 1):
            style = styles['header'] if header else styles['number'] if isinstance(value, (int, float)) else styles['body']
            self.put(f'{column(i)}{nr}', value, style)
        r = self.data.find(f"{q('row')}[@r='{nr}']")
        r.set('ht', '34' if header else '30')
        r.set('customHeight', '1')

    def merge(self, ref):
        merges = self.root.find(q('mergeCells'))
        if merges is None:
            merges = ET.SubElement(self.root, q('mergeCells'))
        if not any(x.get('ref') == ref for x in merges):
            ET.SubElement(merges, q('mergeCell'), {'ref': ref})
        merges.set('count', str(len(merges)))

    def setup(self, widths, freeze=None, hidden=()):
        for name in ('sheetViews', 'cols'):
            old = self.root.find(q(name))
            if old is not None:
                self.root.remove(old)
        views = ET.Element(q('sheetViews'))
        view = ET.SubElement(views, q('sheetView'), {'workbookViewId': '0', 'showGridLines': '0', 'zoomScale': '90'})
        if freeze:
            x, y, top = freeze
            ET.SubElement(view, q('pane'), {'xSplit': str(x), 'ySplit': str(y), 'topLeftCell': top,
                'activePane': 'bottomRight' if x and y else 'bottomLeft', 'state': 'frozen'})
        self.root.insert(0, views)
        cols = ET.Element(q('cols'))
        for i, width in enumerate(widths, 1):
            attrs = {'min': str(i), 'max': str(i), 'width': str(width), 'customWidth': '1'}
            if i in hidden:
                attrs.update(hidden='1', outlineLevel='1')
            ET.SubElement(cols, q('col'), attrs)
        self.root.insert(list(self.root).index(self.data), cols)

    def finish(self):
        self.data[:] = sorted(self.data, key=lambda r: int(r.get('r')))
        for row in self.data:
            row[:] = sorted(row, key=lambda c: (len(re.match('[A-Z]+', c.get('r')).group()), c.get('r')))
        # Keep worksheet child order valid, including views, drawing and tables.
        order = ['sheetPr', 'dimension', 'sheetViews', 'sheetFormatPr', 'cols', 'sheetData',
            'sheetCalcPr', 'sheetProtection', 'protectedRanges', 'scenarios', 'autoFilter',
            'sortState', 'dataConsolidate', 'customSheetViews', 'mergeCells', 'phoneticPr',
            'conditionalFormatting', 'dataValidations', 'hyperlinks', 'printOptions',
            'pageMargins', 'pageSetup', 'headerFooter', 'rowBreaks', 'colBreaks',
            'customProperties', 'cellWatches', 'ignoredErrors', 'smartTags', 'drawing',
            'legacyDrawing', 'legacyDrawingHF', 'picture', 'oleObjects', 'controls',
            'webPublishItems', 'tableParts', 'extLst']
        self.root[:] = sorted(self.root, key=lambda x: order.index(x.tag.split('}')[-1]) if x.tag.split('}')[-1] in order else len(order))
        return xml_bytes(self.root)


def styles(parts):
    root = ET.fromstring(parts['xl/styles.xml'])
    fonts, fills, xfs = (root.find(q(n)) for n in ('fonts', 'fills', 'cellXfs'))
    formats = root.find(q('numFmts'))
    if formats is None:
        formats = ET.Element(q('numFmts')); root.insert(0, formats)
    def add(parent, node):
        raw = ET.tostring(node)
        for i, old in enumerate(parent):
            if ET.tostring(old) == raw:
                return i
        parent.append(node); parent.set('count', str(len(parent))); return len(parent) - 1
    def fmt(code):
        for old in formats:
            if old.get('formatCode') == code:
                return old.get('numFmtId')
        idx = max([163] + [int(x.get('numFmtId')) for x in formats]) + 1
        ET.SubElement(formats, q('numFmt'), {'numFmtId': str(idx), 'formatCode': code})
        formats.set('count', str(len(formats))); return str(idx)
    out = {}
    for name, size, bold, color, fill, number, align in [
        ('body', 11, False, '243746', 'FFFFFF', None, 'left'),
        ('number', 11, False, '243746', 'FFFFFF', '#,##0', 'right'),
        ('percent', 11, False, '243746', 'FFFFFF', '0.0%', 'right'),
        ('decimal', 11, False, '243746', 'FFFFFF', '0.000', 'right'),
        ('units', 11, False, '243746', 'FFFFFF', '0.00;[Red]-0.00', 'right'),
        ('date', 11, False, '243746', 'FFFFFF', 'dd mmm yy hh:mm', 'left'),
        ('header', 11, True, 'FFFFFF', '243E5B', None, 'center'),
        ('title', 16, True, '243E5B', 'FFFFFF', None, 'left'),
        ('section', 11, True, '243E5B', 'EAF0F5', None, 'left'),
        ('note', 11, False, '526477', 'FFFFFF', None, 'left'),
        ('warning', 11, True, '805B10', 'FFF3CF', None, 'left'),
        ('error', 11, True, '9C3030', 'FCE9E9', None, 'left'),
        ('ready', 11, True, '176547', 'E5F3EA', None, 'left'),
        ('link', 11, True, '245BA0', 'FFFFFF', None, 'left'),
    ]:
        f = ET.Element(q('font')); ET.SubElement(f, q('sz'), {'val': str(size)})
        ET.SubElement(f, q('name'), {'val': 'Arial'}); ET.SubElement(f, q('color'), {'rgb': 'FF' + color})
        if bold: ET.SubElement(f, q('b'))
        fid = add(fonts, f)
        f = ET.Element(q('fill')); pattern = ET.SubElement(f, q('patternFill'), {'patternType': 'solid'})
        ET.SubElement(pattern, q('fgColor'), {'rgb': 'FF' + fill}); ET.SubElement(pattern, q('bgColor'), {'indexed': '64'})
        fillid = add(fills, f)
        xf = ET.Element(q('xf'), {'fontId': str(fid), 'fillId': str(fillid), 'borderId': '0', 'xfId': '0',
            'numFmtId': fmt(number) if number else '0', 'applyFont': '1', 'applyFill': '1', 'applyAlignment': '1', 'applyNumberFormat': '1'})
        ET.SubElement(xf, q('alignment'), {'horizontal': align, 'vertical': 'center', 'wrapText': '1'})
        out[name] = add(xfs, xf)
    dxfs = root.find(q('dxfs'))
    if dxfs is None:dxfs = ET.SubElement(root,q('dxfs'),{'count':'0'})
    for name in ('warning','error','ready'):
        xf=xfs[out[name]];dxf=ET.Element(q('dxf'))
        dxf.append(copy.deepcopy(fonts[int(xf.get('fontId'))]))
        dxf.append(copy.deepcopy(fills[int(xf.get('fillId'))]))
        out['dxf_'+name]=add(dxfs,dxf)
    parts['xl/styles.xml'] = xml_bytes(root)
    return out


def status_rules(sheet, ref, st, groups):
    for old in list(sheet.root.findall(q('conditionalFormatting'))):
        if old.get('sqref') == ref and all(int(r.get('priority','0')) >= 101 for r in old):
            sheet.root.remove(old)
    node=ET.SubElement(sheet.root,q('conditionalFormatting'),{'sqref':ref})
    address=ref.split(':')[0]
    for priority,(style,values) in enumerate(groups,101):
        rule=ET.SubElement(node,q('cfRule'),{'type':'expression','priority':str(priority),'dxfId':str(st['dxf_'+style])})
        expressions=[f'{address}="{value}"' for value in values]
        ET.SubElement(rule,q('formula')).text='OR('+','.join(expressions)+')'


def put_sheet(parts, name, sheet):
    wb = ET.fromstring(parts['xl/workbook.xml']); sheets = wb.find(q('sheets'))
    rels = ET.fromstring(parts['xl/_rels/workbook.xml.rels'])
    old = next((s for s in sheets if s.get('name') == name), None)
    if old is not None:
        rid = old.get(f'{{{REL}}}id')
        target = next(r.get('Target') for r in rels if r.get('Id') == rid)
        path = target.lstrip('/') if target.startswith('/') else 'xl/' + target
    else:
        index = max(int(s.get('sheetId')) for s in sheets) + 1
        path = f'xl/worksheets/sheet{index}.xml'; rid = f'rIdReadable{index}'
        ET.SubElement(sheets, q('sheet'), {'name': name, 'sheetId': str(index), f'{{{REL}}}id': rid})
        ET.SubElement(rels, f'{{{PKG}}}Relationship', {'Id': rid, 'Type': REL + '/worksheet', 'Target': path[3:]})
        types = ET.fromstring(parts['[Content_Types].xml'])
        ET.SubElement(types, f'{{{CT}}}Override', {'PartName': '/' + path, 'ContentType': 'application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml'})
        parts['[Content_Types].xml'] = xml_bytes(types)
    parts['xl/workbook.xml'] = xml_bytes(wb); parts['xl/_rels/workbook.xml.rels'] = xml_bytes(rels)
    parts[path] = sheet.finish()
    return path


def get_sheet(parts, name):
    wb = ET.fromstring(parts['xl/workbook.xml']); rels = ET.fromstring(parts['xl/_rels/workbook.xml.rels'])
    node = next((s for s in wb.find(q('sheets')) if s.get('name') == name), None)
    if node is None: return None
    target = next(r.get('Target') for r in rels if r.get('Id') == node.get(f'{{{REL}}}id'))
    path = target.lstrip('/') if target.startswith('/') else 'xl/' + target
    return Sheet(ET.fromstring(parts[path]))


def title(sheet, name, note, widths, st, freeze=None):
    sheet.setup(widths, freeze)
    sheet.put('A2', name, st['title']); sheet.merge(f'A2:{column(len(widths))}2')
    sheet.put('A4', note, st['note']); sheet.merge(f'A4:{column(len(widths))}4')
    for nr, ht in ((2, 28), (4, 34)):
        r = sheet.data.find(f"{q('row')}[@r='{nr}']"); r.set('ht', str(ht)); r.set('customHeight', '1')


def link(sheet, address, target, caption, st):
    sheet.put(address, caption, st['link'])
    links = sheet.root.find(q('hyperlinks'))
    if links is None: links = ET.SubElement(sheet.root, q('hyperlinks'))
    for old in list(links):
        if old.get('ref') == address: links.remove(old)
    ET.SubElement(links, q('hyperlink'), {'ref': address, 'location': "'" + target.replace("'", "''") + "'!A1", 'display': caption})


def load(root, filename):
    path = Path(root) / 'performance' / filename
    return json.loads(path.read_text(encoding='utf-8')) if path.exists() else {}


def experiment_rows(root, health):
    queue = (health or {}).get('review_queue') or load(root, 'experiment_review_queue.json')
    by_name = {i['name']: i for i in queue.get('experiments', [])}
    result = []
    for name, display in NAMES.items():
        item = by_name.get(name, {})
        summary = load(root, name + '/summary.json')
        if name.startswith('reliability:'):
            candidate_id = name.split(':', 1)[1]
            name = 'model_reliability_experiment'
            item = next((i for i in queue.get('experiments', []) if i['name'] == name and i.get('candidate_id') == candidate_id), {})
            parent = load(root, name + '/summary.json')
            summary = {**next((c for c in parent.get('comparisons', []) if c['candidate_id'] == candidate_id), {}),
                       'review_gates': parent.get('registry', {}), 'rejected_snapshot_commits': parent.get('rejected_snapshot_commits', [])}
        state = item.get('status', 'REPORT_UNAVAILABLE_OR_STALE')
        n = item.get('settled_evidence')
        requirements = []
        if name in ('benchmark_forward_experiment', 'totals_anchor_experiment', 'model_reliability_experiment', 'shortlist_policy_experiment', 'shortlist_weight_experiment'):
            gates = summary.get('review_gates', {})
            minimum = gates.get('minimum_paired_fixtures'); weeks = gates.get('minimum_gameweeks')
            coverage_min = gates.get('minimum_verified_coverage'); coverage = summary.get('verified_coverage')
            progress = item.get('gameweeks')
            if minimum is None or weeks is None or coverage_min is None:
                requirements.append('Review thresholds unavailable')
            else:
                if n is None or n < minimum: requirements.append(f'{max(0, minimum-(n or 0))} more paired fixtures')
                if progress is None or progress < weeks: requirements.append(f'{max(0, weeks-(progress or 0))} more ISO weeks')
                if coverage is None: requirements.append('Verified coverage unavailable')
                elif coverage < coverage_min: requirements.append(f'Coverage below {coverage_min:.0%}')
            if name == 'shortlist_weight_experiment':
                needed = gates.get('minimum_settled_per_weighting', 100)
                have = summary.get('minimum_settled_per_weighting', 0)
                if have < needed: requirements.append(f'{needed-have} more settled picks in the least-sampled weighting')
            if summary.get('rejected_snapshot_commits'): requirements.append('Rejected snapshots need review')
            scope = 'Approval review'
            threshold = f'{minimum} paired fixtures' if minimum is not None else 'Unavailable'
            period = f'{progress if progress is not None else "?"} / {weeks if weeks is not None else "?"} ISO weeks'
            coverage_text = coverage
        else:
            threshold = '30 settled observations'; period = f'{item.get("collection_days", "?")} / 28 days'
            coverage_text = None; scope = 'Initial review only'
            if n is None or n < 30: requirements.append(f'{max(0,30-(n or 0))} more observations')
            if item.get('collection_days', 0) < 28: requirements.append(f'{28-item.get("collection_days",0)} more days')
        if state == 'REPORT_UNAVAILABLE_OR_STALE': requirements.insert(0, 'Regenerate the forward review')
        if state == 'DATA_QUALITY_BLOCKED': requirements.insert(0, 'Resolve data-quality blockers')
        if state in ('READY_FOR_REVIEW', 'FIRST_LOOK_READY'):
            next_action = 'Review the paired results; approval is separate'
        else:
            next_action = '; '.join(requirements) or 'Continue collection; see detailed report'
        unit = 'Paired fixtures' if name in ('benchmark_forward_experiment','totals_anchor_experiment','model_reliability_experiment','shortlist_policy_experiment', 'shortlist_weight_experiment') else 'Settled observations'
        result.append([display, label(state), n if n is not None else 'Unavailable', unit, threshold, period,
            coverage_text if coverage_text is not None else 'Unavailable' if scope=='Approval review' else 'Not applicable',
            scope, next_action, label(item.get('evidence')) if 'evidence' in item else 'Initial review only'])
    return result


def add_experiments(parts, root, health, st):
    sheet = Sheet(); title(sheet, 'Experiment readiness', 'Readiness invites review, including negative findings. Production changes still require approval.',
        [28, 28, 12, 22, 25, 20, 15, 23, 48, 32], st, (1, 5, 'B6'))
    sheet.row(5, ['Experiment', 'Status', 'Collected', 'Evidence unit', 'Required sample', 'Time collected / required', 'Verified coverage', 'Review scope', 'Remaining requirements / next action', 'Evidence finding'], st, True)
    rows = experiment_rows(root, health)
    end = 5 + len(rows)
    for nr, values in enumerate(rows, 6):
        sheet.row(nr, values, st); sheet.cell(f'G{nr}').set('s', str(st['percent']))
        state = values[1]
        sheet.cell(f'B{nr}').set('s', str(st['ready'] if state in ('Ready for review','First look ready') else st['error'] if state in ('Report unavailable or stale','Data quality blocked') else st['warning']))
        sheet.data.find(f"{q('row')}[@r='{nr}']").set('ht', '66')
    ET.SubElement(sheet.root, q('autoFilter'), {'ref': f'A5:J{end}'})
    status_rules(sheet,f'B6:B{end}',st,[('ready',['Ready for review','First look ready']),
        ('error',['Report unavailable or stale','Data quality blocked']),('warning',['Collect more data'])])
    sheet.put(f'A{end+2}', 'The original four sidecars count observations, not necessarily independent fixtures. Do not add their sample counts together.', st['note']); sheet.merge(f'A{end+2}:J{end+2}')
    sheet.put(f'A{end+3}', 'Coverage and time gates must also pass. Reaching a sample count alone does not make a candidate ready.', st['note']); sheet.merge(f'A{end+3}:J{end+3}')
    link(sheet, f'A{end+5}', 'Dashboard', 'Back to dashboard', st)
    policy = load(root, 'shortlist_policy_experiment/summary.json')
    if policy.get('comparisons'):
        nr = end+8
        sheet.put(f'A{nr}', 'Probability and calibration policies — fixed comparisons', st['section']); sheet.merge(f'A{nr}:J{nr}')
        nr += 1
        sheet.put(f'A{nr}', 'STRICT is primary. ROI is simulated; different selected cohorts are not paired forecast tests. See the detailed report before drawing conclusions.', st['note']); sheet.merge(f'A{nr}:J{nr}')
        sheet.data.find(f"{q('row')}[@r='{nr}']").set('ht', '44')
        nr += 1
        sheet.row(nr, ['Variant', 'Tier', 'Selected', 'Settled', 'Net ROI', 'Brier', 'Log loss', 'Calibration gap', 'Drawdown (units)', 'Strict profit delta / fixture 95% interval'], st, True)
        paired = {r['variant_id']: r for r in policy.get('paired_strict_returns', [])}
        for item in policy['comparisons']:
            nr += 1
            interval = paired.get(item['variant_id'], {}).get('weekly_block_bootstrap95') if item['tier'] == 'STRICT' else None
            interval_text = f'{interval[0]:+.4f} to {interval[1]:+.4f}' if interval else 'Collect more data' if item['tier'] == 'STRICT' else 'Not applicable'
            values = [item['variant_id'], item['tier'], item['selected'], item['graded'], item['flat_stake_roi'], item['brier'], item['log_loss'], item['calibration_gap'], item['max_drawdown_units'], interval_text]
            sheet.row(nr, [v if v is not None else 'Unavailable' for v in values], st)
            for col in ('E', 'H'): sheet.cell(f'{col}{nr}').set('s', str(st['percent']))
    weights = load(root, 'shortlist_weight_experiment/summary.json')
    if weights.get('comparisons'):
        nr = (nr+3) if policy.get('comparisons') else end+8
        sheet.put(f'A{nr}', 'Shortlist probability / EV weights — ALL selections primary', st['section']); sheet.merge(f'A{nr}:J{nr}')
        nr += 1
        sheet.row(nr, ['Probability / EV', 'Tier', 'Selected', 'Settled', 'Win rate', 'Win rate 95% interval', 'Net ROI', 'Profit (units)', 'Drawdown (units)', 'Profit delta / fixture 95% vs 50/50'], st, True)
        from shortlist_weight_experiment import weight_label
        for cohort in [weights, *weights.get('legacy_cohorts', [])]:
            if cohort is not weights:
                nr += 2
                sheet.put(f'A{nr}', 'Legacy v1 fixed weights — separate cohort', st['section']); sheet.merge(f'A{nr}:J{nr}')
                nr += 1
                sheet.row(nr, ['Probability / EV', 'Tier', 'Selected', 'Settled', 'Win rate', 'Win rate 95% interval', 'Net ROI', 'Profit (units)', 'Drawdown (units)', 'Profit delta / fixture 95% vs 50/50'], st, True)
            paired = {r['variant_id']: r for r in cohort.get('paired_all_returns', [])}
            for item in cohort['comparisons']:
                nr += 1
                interval = paired.get(item['variant_id'], {}).get('weekly_block_bootstrap95') if item['tier'] == 'ALL' else None
                win = item.get('win_rate_wilson95')
                row = [weight_label(item), item['tier'], item['selected'], item['graded'], item['observed_rate'],
                    f'{win[0]:.1%} to {win[1]:.1%}' if win else 'Collect more data', item['flat_stake_roi'], item['profit_units'], item['max_drawdown_units'],
                    f'{interval[0]:+.4f} to {interval[1]:+.4f}' if interval else 'Control' if item['variant_id'] == 'control' and item['tier'] == 'ALL' else 'Collect more data' if item['tier'] == 'ALL' else 'Not applicable']
                sheet.row(nr, [v if v is not None else 'Unavailable' for v in row], st)
                for col in ('E', 'G'): sheet.cell(f'{col}{nr}').set('s', str(st['percent']))
            nr += 2
            sheet.row(nr, ['Weighting', 'Tier', 'Mean probability', 'Win rate', 'Calibration gap', 'Brier', 'Log loss', 'Mean probability weight', 'Min probability weight', 'Max probability weight'], st, True)
            for item in cohort['comparisons']:
                if item['tier'] != 'ALL':
                    continue
                nr += 1
                row = [weight_label(item), 'ALL', item.get('mean_probability'), item.get('observed_rate'),
                    item.get('calibration_gap'), item.get('brier'), item.get('log_loss'),
                    item.get('mean_probability_weight', item.get('probability_weight')),
                    item.get('minimum_probability_weight', item.get('probability_weight')),
                    item.get('maximum_probability_weight', item.get('probability_weight'))]
                sheet.row(nr, [v if v is not None else 'Unavailable' for v in row], st)
                for col in ('C', 'D', 'E', 'H', 'I', 'J'): sheet.cell(f'{col}{nr}').set('s', str(st['percent']))
    put_sheet(parts, 'Experiments', sheet)


def add_health(parts, data, history, st):
    sheet = Sheet(); title(sheet, 'Pipeline health', 'Health describes collection and evidence coverage. Recent result dates alone do not verify source completeness.',
        [28, 23, 18, 22, 36, 44], st, (1, 6, 'B7'))
    sheet.put('A5', 'Review UTC: ' + str(data.get('reviewed_at_utc', 'Unavailable')), st['note']); sheet.merge('A5:F5')
    nr = 7
    def section(name, headers, records, formats=None):
        nonlocal nr
        sheet.put(f'A{nr}', name, st['section']); sheet.merge(f'A{nr}:F{nr}'); nr += 1
        sheet.row(nr, headers, st, True); nr += 1
        for values in records or [['No observations available']]:
            sheet.row(nr, values, st)
            for i, style in (formats or {}).items(): sheet.cell(f'{column(i)}{nr}').set('s', str(st[style]))
            if name=='Training data freshness':
                status_rules(sheet,f'E{nr}',st,[('error',['Stale','Source unavailable','Refresh failed']),
                    ('warning',['Result date only not completeness verified'])])
            if name=='Forecast capture coverage':
                status_rules(sheet,f'B{nr}',st,[('error',['Capture failed','Invalid','Hash mismatch']),
                    ('warning',['Legacy not recorded','Missing','Not captured'])])
            sheet.data.find(f"{q('row')}[@r='{nr}']").set('ht', '44')
            nr += 1
        nr += 2
    training=[]
    for league, info in data.get('training', {}).items():
        state=info.get('current_source_health', info.get('forecast_training_health',{})).get('status')
        training.append([league,info.get('training_end'),info.get('training_matches'),info.get('days_since_latest_result'),label(state), 'Source completeness unverified' if state=='RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED' else 'See source health report'])
    section('Training data freshness', ['League','Latest result','Training matches','Days since result','Source status','Next check'],training)
    closing=[]
    for book, info in data.get('closing_odds',{}).get('by_bookmaker',{}).items():
        closing.append([book,info.get('covered_selections'),info.get('missing_selections'),info.get('pending_selections'),
            info.get('mean_fair_close_ev') if info.get('mean_fair_close_ev') is not None else 'Unavailable',
            info.get('mean_same_book_offered_price_clv') if info.get('mean_same_book_offered_price_clv') is not None else 'Unavailable'])
    section('Near-close quote coverage', ['Bookmaker','Covered selections','Missing selections','Pending selections','Mean fair-close EV','Same-book offer CLV'],closing,{5:'percent',6:'percent'})
    sheet.put(f'A{nr}', 'Observed near-close quotes are not guaranteed official closes. Accepted bet prices and execution remain unverified.',st['note']);sheet.merge(f'A{nr}:F{nr}');nr+=2
    audit=[]
    for key,value in data.get('quote_audit',{}).items():
        if isinstance(value,dict): audit.extend([[label(key)+': '+str(k),v] for k,v in value.items()])
        else: audit.append([label(key),label(value) if isinstance(value,str) else value])
    section('Latest shortlist quote audit',['Check','Recorded value'],audit)
    counts=[]
    capture=data.get('snapshot_capture_history',[])
    for name,display in NAMES.items():
        states={}
        for snap in capture:
            state=snap.get('experiments',{}).get(name,'LEGACY_NOT_RECORDED');states[state]=states.get(state,0)+1
        counts.extend([[display,label(state),count] for state,count in sorted(states.items())])
    section('Forecast capture coverage',['Experiment','Capture state','Snapshot count'],counts)
    comparisons=data.get('experimental_reports',{}).get('filter_sensitivity_experiment',{}).get('comparisons',[])
    section('EV sensitivity results',['EV floor','Tier','Selected','Settled','Simulated ROI','Drawdown (units)'],
        [[r.get(k) for k in ('ev_floor','tier','selected','graded','flat_stake_roi','max_drawdown_units')] for r in comparisons],{1:'percent',5:'percent',6:'units'})
    section('Daily review observations',['Review date','Graded','Win rate','Simulated ROI','Brier'],
        [[day]+[v['shortlist_performance'].get(k) for k in ('graded','win_rate','flat_stake_roi','brier')] for day,v in sorted((history or {}).get('days',{}).items())],{3:'percent',4:'percent',5:'decimal'})
    section('Dependency versions',['Dependency','Version'],[[k,v] for k,v in data.get('dependencies',{}).items()])
    link(sheet,f'A{nr}','Dashboard','Back to dashboard',st)
    put_sheet(parts,'Pipeline Health',sheet)
    details=Sheet();title(details,'Forecast capture history','Raw capture states are retained for diagnosing missing or failed experiment capture.',[24,26,32,32,32,32,32,32],st,(1,5,'B6'))
    details.row(5,['Snapshot','Captured UTC']+list(NAMES.values()),st,True)
    for nr,snap in enumerate(capture,6):
        details.row(nr,[snap.get('commit'),snap.get('captured_at_utc')]+[snap.get('experiments',{}).get(n,'LEGACY_NOT_RECORDED') for n in NAMES],st)
        details.data.find(f"{q('row')}[@r='{nr}']").set('ht','56')
    ET.SubElement(details.root,q('autoFilter'),{'ref':f'A5:H{max(6,5+len(capture))}'})
    put_sheet(parts,'Capture Details',details)


def add_guide(parts, st):
    sheet=Sheet();title(sheet,'Metric guide','Definitions apply to the archived forecasts and simulated selections in this workbook.',[28,68,64],st)
    sheet.row(5,['Metric','Meaning','How to read it'],st,True)
    definitions=[
        ['Win rate','Wins divided by settled selections. Pending and unverified results are excluded.','Read with the settled sample size and 95% interval.'],
        ['Simulated ROI','Simulated net profit divided by staked units. Includes recorded per-stake costs.','Offered prices and simulated stakes are not proof of actual returns. Missing prices are excluded.'],
        ['Binary Brier','Mean squared error between a forecast probability and a binary outcome.','Lower is better. Read the number of valid probability samples.'],
        ['1X2 Brier','Multiclass probability error across home win, draw and away win.','Lower is better. Its scale differs from binary Brier; do not compare the two directly.'],
        ['Log loss','Penalty assigned to the probability of the observed outcome.','Lower is better. Compare candidates on the same fixtures.'],
        ['Calibration gap','Mean forecast probability minus observed win rate on the same scored selections.','Closer to zero is better. Positive indicates overconfidence; negative indicates underconfidence.'],
        ['Same-book offer CLV','Frozen offered odds divided by observed near-close odds at the same bookmaker, minus one.','Positive means a better earlier offered price. Quotes are not accepted prices or guaranteed official closing odds.'],
        ['Fair-close EV','Frozen offered odds multiplied by the de-vigged near-close probability, minus one and recorded costs.','Positive indicates value relative to that observed reference. Coverage must be shown.'],
        ['Verified coverage','Share of verified in-scope fixtures with a usable paired candidate forecast.','Use each versioned trial\'s registered minimum. Missing coverage remains unavailable.'],
        ['Initial review','Original sidecars: at least 28 collection days and 30 settled observations.','An initial look permits review, not promotion or a profitability claim.'],
        ['Approval review','Versioned trials: registered fixture, ISO-week and coverage gates must pass.','Readiness can include negative findings. Production changes require approval.'],
        ['ISO week','Calendar year and week, assigned by the existing grading system.','This is not a competition gameweek.'],
        ['Unavailable / n.a.','The required input or settled sample is missing.','This is not a zero result and must not be interpreted as healthy evidence.'],
    ]
    for nr,row in enumerate(definitions,6):
        sheet.row(nr,row,st);sheet.data.find(f"{q('row')}[@r='{nr}']").set('ht','54')
    link(sheet,'A21','Dashboard','Back to dashboard',st);put_sheet(parts,'Metric Guide',sheet)


def ledger_layout(parts, st):
    settings={
        'Selections':([12,23,22,44,20,18,32,18,14,12,36,12,14,14,14,16,24,26,18,16,18,28,28],(0,5,'A6'),(1,7,12,17,18,19,20,21),{'B':'date','H':'percent','I':'units','M':'units','N':'units','O':'decimal','S':'percent','U':'units'}),
        'Predictions':([12,23,22,44,32,34,12,16,16,16,16,16,16,16,24,26],(0,5,'A6'),(1,5,15,16),{'B':'date','I':'decimal'}),
        'Breakdowns':([18,38,13,13,13,13,13,15,16,16,15,15,18,18,18,18,48],(2,5,'C6'),(),{'H':'percent','I':'units','J':'units','K':'percent','L':'decimal','M':'percent','N':'percent','O':'percent'}),
        'Calibration':([18,16,16,14,20,20,20,16,48],(1,5,'B6'),(),{'B':'percent','C':'percent','E':'percent','F':'percent','G':'percent','H':'decimal'}),
        'ROI Plan':([24,44,36,16,18,18,18,18,18,16],(2,9,'C10'),(),{'D':'units','E':'units','F':'units','G':'units','H':'units','I':'units'}),
    }
    for name,(widths,freeze,hidden,formats) in settings.items():
        sheet=get_sheet(parts,name)
        if sheet is None:continue
        # Hide only technical fields; freeze visible kickoff/league/match identity.
        if name in ('Selections','Predictions'): freeze=(4,5,'E6')
        sheet.setup(widths,freeze,hidden)
        header=9 if name=='ROI Plan' else 5
        for row in sheet.data:
            nr=int(row.get('r'));row.set('customHeight','1')
            row.set('ht','44' if nr==header else '36' if nr>header else row.get('ht','24'))
            for cell in row:
                address=cell.get('r');c=re.match('[A-Z]+',address).group()
                if nr==2:cell.set('s',str(st['title']))
                elif nr==header:cell.set('s',str(st['header']))
                elif nr>header:
                    kind=formats.get(c,'number' if isinstance(text(cell),(int,float)) else 'body')
                    cell.set('s',str(st[kind]))
        for nr in ((2,) if name=='ROI Plan' else (2,4)):
            sheet.merge(f'A{nr}:{column(len(widths))}{nr}')
        if name!='ROI Plan':sheet.put('A4', text(sheet.cell('A4')) or '',st['note'])
        if name=='Breakdowns':
            sheet.put('O5','Calibration gap',st['header'])
            # Excel requires table column names to match their header cells.
            for path in list(parts):
                if not (path.startswith('xl/tables/') and path.endswith('.xml')):
                    continue
                table = ET.fromstring(parts[path])
                if table.get('name') == 'BreakdownsTable':
                    table.find(q('tableColumns'))[14].set('name', 'Calibration gap')
                    parts[path] = xml_bytes(table)
        if name=='Selections':sheet.put('A4','Latest eligible pre-match selection per fixture. Generated/captured times and source commits show which prediction is graded. Times are UTC.',st['note'])
        if name in ('Selections','Predictions'):
            for nr in (2,4):
                merges=sheet.root.find(q('mergeCells'))
                for node in list(merges):
                    if node.get('ref')==f'A{nr}:{column(len(widths))}{nr}':merges.remove(node)
                sheet.put(f'B{nr}',text(sheet.cell(f'A{nr}')),st['title'] if nr==2 else st['note'])
                sheet.merge(f'B{nr}:{column(len(widths))}{nr}')
        if name=='Selections':
            last=max(int(r.get('r')) for r in sheet.data)
            status_rules(sheet,f'K6:K{max(6,last)}',st,[('ready',['WON']),('error',['LOST']),
                ('warning',['PENDING_KICKOFF_OR_FINAL_SCORE','UNVERIFIED_FIXTURE_OR_RESULT'])])
        put_sheet(parts,name,sheet)


def dashboard(parts, st, health, rows):
    sheet=get_sheet(parts,'Dashboard');sheet.setup([34,17,3,31,13,17])
    for row in sheet.data:
        nr=int(row.get('r'));row.set('ht','26');row.set('customHeight','1')
        for cell in row:
            if nr<=29:cell.set('s',str(st['body']))
    sheet.cell('A2').set('s',str(st['title']));sheet.merge('A2:F2')
    for nr in (4,21,23,24,25,26,27,28,29):
        sheet.merge(f'A{nr}:F{nr}');sheet.cell(f'A{nr}').set('s',str(st['note']))
        sheet.data.find(f"{q('row')}[@r='{nr}']").set('ht','34' if nr in (21,26,28,29) else '26')
    for address in ('A6','B6','D6','E6','F6','D16','E16','F16'):sheet.cell(address).set('s',str(st['header']))
    for nr in range(7,20):sheet.cell(f'B{nr}').set('s',str(st['percent'] if nr in (12,13,16,18,19) else st['decimal'] if nr in (15,17) else st['units'] if nr==14 else st['number']))
    for nr in (7,8,17,18,19,20):sheet.cell(f'F{nr}').set('s',str(st['percent']))
    for ref in ('D11:F12','D14:F15'):sheet.merge(ref)
    sheet.cell('D11').set('s',str(st['warning']))
    sheet.put('A14','Simulated net profit (units)',st['body'])
    sheet.put('A15','Selection Brier (lower is better)',st['body'])
    if health:sheet.put('A27','Review UTC: '+str(health.get('reviewed_at_utc') or 'Unavailable'),st['note'])
    link(sheet,'D43','Run Tracking','Results by prediction run',st)
    link(sheet,'A31','Experiments','Experiment readiness',st);link(sheet,'D31','Pipeline Health','Collection health',st)
    sheet.put('A33','Monitoring and next actions',st['section']);sheet.merge('A33:F33')
    sheet.row(34,['Check','Status',None,'Next action'],st,True);sheet.merge('D34:F34')
    ready=sum(r[1] in ('Ready for review','First look ready') for r in rows)
    stale=sum(r[1]=='Report unavailable or stale' for r in rows)
    rejected=len((health or {}).get('closing_odds',{}).get('rejected_files',[]))
    coverage=(health or {}).get('closing_odds',{}).get('by_bookmaker',{})
    missing=sum(x.get('missing_selections',0) for x in coverage.values())
    capture=(health or {}).get('snapshot_capture_history',[])
    messages=[
        ['Experiments ready',ready,None,'Open Experiments and review results' if ready else 'Continue generating and pushing forecasts'],
        ['Unavailable / stale reports',stale,None,'Run or check the forward review' if stale else 'No stale experiment reports recorded'],
        ['Missing near-close quotes',missing if coverage else 'Unavailable',None,'Check local collection and push quotes; counts overlap across bookmakers' if missing else 'See coverage by bookmaker'],
        ['Rejected quote files',rejected if health else 'Unavailable',None,'Review the closing report' if rejected else 'No rejected quote files recorded' if health else 'Run the forward review'],
        ['Latest frozen capture',str(capture[-1].get('captured_at_utc', 'Unavailable')).replace('T',' ').replace('Z',' UTC') if capture else 'Unavailable',None,'See Capture Details for all six experiment states'],
    ]
    for nr,row in enumerate(messages,35):
        sheet.row(nr,row,st);sheet.merge(f'D{nr}:F{nr}');sheet.data.find(f"{q('row')}[@r='{nr}']").set('ht','44')
    link(sheet,'A41','Weekly Trends','Weekly samples and profit',st);link(sheet,'D41','Metric Guide','Metric definitions',st)
    # Existing charts remain, below the new operational section.
    for path in list(parts):
        if path.startswith('xl/drawings/drawing') and path.endswith('.xml') and 'Monitoring' not in path:
            drawing=ET.fromstring(parts[path])
            for anchor in drawing:
                start=anchor.find(f'{{{XDR}}}from/{{{XDR}}}row')
                if start is not None and int(start.text)==30:
                    for marker in anchor.findall(f'.//{{{XDR}}}row'):marker.text=str(int(marker.text)+20)
            parts[path]=xml_bytes(drawing)
    put_sheet(parts,'Dashboard',sheet)


def add_trends(parts, st):
    breakdown=get_sheet(parts,'Breakdowns');sheet=Sheet()
    selections=get_sheet(parts,'Selections')
    ledger_end=max(6,max(int(r.get('r')) for r in selections.data))
    title(sheet,'Weekly performance','ISO calendar weeks. All archived selection policies and tiers; profit uses offered prices and simulated stakes.',[20,18,18,20,22,22,20,20],st,(0,5,'A6'))
    sheet.row(5,['ISO week','Settled selections','Priced selections','Simulated profit (units)','Cumulative profit (units)','Win rate'],st,True)
    source=[]
    for row in breakdown.data:
        cells={re.match('[A-Z]+',c.get('r')).group():c for c in row}
        if text(cells.get('A'))=='Week':source.append((int(row.get('r')),cells))
    running=0
    for nr,(original,cells) in enumerate(source,6):
        for target,origin in [('A','B'),('B','D'),('C','I'),('D','J'),('F','H')]:
            value=text(cells.get(origin));sheet.put(f'{target}{nr}',value,st['percent'] if target=='F' else st['units'] if target=='D' else st['body'] if target=='A' else st['number'],f'Breakdowns!{origin}{original}')
        sheet.data.find(f"{q('row')}[@r='{nr}']").set('ht','26')
        sheet.data.find(f"{q('row')}[@r='{nr}']").set('customHeight','1')
        priced = text(cells.get('I')) or 0
        sheet.put(f'C{nr}',priced,st['number'],f'COUNTIFS(Selections!$P$6:$P${ledger_end},A{nr},Selections!$M$6:$M${ledger_end},">0")')
        running+=text(cells.get('J')) or 0
        sheet.put(f'D{nr}',text(cells.get('J')) if priced else 'n.a.',st['units'],f'IF(C{nr}=0,"n.a.",Breakdowns!J{original})')
        cumulative_priced=sum(text(cs.get('I')) or 0 for _,cs in source[:nr-5])
        sheet.put(f'E{nr}',running if cumulative_priced else 'n.a.',st['units'],f'IF(SUM($C$6:C{nr})=0,"n.a.",SUM($D$6:D{nr}))')
    end=max(6,5+len(source))
    if not source:sheet.put('A6','No archived weeks',st['note'])
    sheet.put(f'A{end+2}','Pending selections are excluded from rates. Weeks with no priced settled selections have no realised evidence of profit.',st['note']);sheet.merge(f'A{end+2}:H{end+2}')
    path=put_sheet(parts,'Weekly Trends',sheet)
    add_trend_charts(parts,path,sheet,end,max(10,end+5))


def add_trend_charts(parts,path,sheet,end,start):
    # Dedicated package names make repeated formatting idempotent.
    drawing_name='drawingMonitoring.xml'; drawing=ET.Element(f'{{{XDR}}}wsDr')
    rels=ET.Element(f'{{{PKG}}}Relationships')
    types=ET.fromstring(parts['[Content_Types].xml'])
    def content_type(p,t):
        if not any(x.get('PartName')=='/'+p for x in types):
            ET.SubElement(types,f'{{{CT}}}Override',{'PartName':'/'+p,'ContentType':t})
    for idx,(kind,col,title_text) in enumerate([('bar','B','Settled selections by ISO week'),('line','E','Cumulative simulated profit (units)')],1):
        name=f'chartMonitoring{idx}.xml';chart=ET.Element(f'{{{C}}}chartSpace')
        ch=ET.SubElement(chart,f'{{{C}}}chart');tit=ET.SubElement(ch,f'{{{C}}}title');tx=ET.SubElement(tit,f'{{{C}}}tx');rich=ET.SubElement(tx,f'{{{C}}}rich');ET.SubElement(rich,f'{{{A}}}bodyPr');ET.SubElement(rich,f'{{{A}}}lstStyle');p=ET.SubElement(rich,f'{{{A}}}p');r=ET.SubElement(p,f'{{{A}}}r');ET.SubElement(r,f'{{{A}}}rPr',{'sz':'1200'});ET.SubElement(r,f'{{{A}}}t').text=title_text
        plot=ET.SubElement(ch,f'{{{C}}}plotArea');ET.SubElement(plot,f'{{{C}}}layout')
        graph=ET.SubElement(plot,f'{{{C}}}{kind}Chart')
        if kind=='bar':ET.SubElement(graph,f'{{{C}}}barDir',{'val':'col'});ET.SubElement(graph,f'{{{C}}}grouping',{'val':'clustered'})
        else:ET.SubElement(graph,f'{{{C}}}grouping',{'val':'standard'})
        ser=ET.SubElement(graph,f'{{{C}}}ser');ET.SubElement(ser,f'{{{C}}}idx',{'val':'0'});ET.SubElement(ser,f'{{{C}}}order',{'val':'0'});t=ET.SubElement(ser,f'{{{C}}}tx');ET.SubElement(t,f'{{{C}}}v').text=title_text
        sp=ET.SubElement(ser,f'{{{C}}}spPr');fill=ET.SubElement(sp,f'{{{A}}}solidFill');ET.SubElement(fill,f'{{{A}}}srgbClr',{'val':'336A9C'})
        line=ET.SubElement(sp,f'{{{A}}}ln',{'w':'25400'});ET.SubElement(ET.SubElement(line,f'{{{A}}}solidFill'),f'{{{A}}}srgbClr',{'val':'336A9C'})
        for which,source,numeric in [('cat','A',False),('val',col,True)]:
            ref=ET.SubElement(ET.SubElement(ser,f'{{{C}}}{which}'),f'{{{C}}}'+('numRef' if numeric else 'strRef'))
            ET.SubElement(ref,f'{{{C}}}f').text=f"'Weekly Trends'!${source}$6:${source}${end}"
            cache=ET.SubElement(ref,f'{{{C}}}'+('numCache' if numeric else 'strCache'))
            if numeric:ET.SubElement(cache,f'{{{C}}}formatCode').text='0.00' if col=='E' else '0'
            ET.SubElement(cache,f'{{{C}}}ptCount',{'val':str(end-5)})
            for nr in range(6,end+1):
                v=text(sheet.cell(f'{source}{nr}'))
                if v is None or numeric and not isinstance(v,(int,float)):continue
                ET.SubElement(ET.SubElement(cache,f'{{{C}}}pt',{'idx':str(nr-6)}),f'{{{C}}}v').text=str(v)
        for aid in (1,2):ET.SubElement(graph,f'{{{C}}}axId',{'val':str(aid)})
        if kind=='line':ET.SubElement(ser,f'{{{C}}}smooth',{'val':'0'})
        for ax,aid,cross,pos in [('catAx',1,2,'b'),('valAx',2,1,'l')]:
            node=ET.SubElement(plot,f'{{{C}}}{ax}');ET.SubElement(node,f'{{{C}}}axId',{'val':str(aid)});scale=ET.SubElement(node,f'{{{C}}}scaling');ET.SubElement(scale,f'{{{C}}}orientation',{'val':'minMax'})
            if ax=='valAx' and kind=='bar':ET.SubElement(scale,f'{{{C}}}min',{'val':'0'})
            ET.SubElement(node,f'{{{C}}}axPos',{'val':pos});ET.SubElement(node,f'{{{C}}}numFmt',{'formatCode':'0.00' if col=='E' and ax=='valAx' else '0','sourceLinked':'0'});ET.SubElement(node,f'{{{C}}}crossAx',{'val':str(cross)});ET.SubElement(node,f'{{{C}}}crosses',{'val':'min' if ax=='catAx' else 'autoZero'})
        ET.SubElement(ch,f'{{{C}}}plotVisOnly',{'val':'1'});ET.SubElement(ch,f'{{{C}}}dispBlanksAs',{'val':'gap'})
        parts['xl/charts/'+name]=xml_bytes(chart);content_type('xl/charts/'+name,'application/vnd.openxmlformats-officedocument.drawingml.chart+xml')
        anchor=ET.SubElement(drawing,f'{{{XDR}}}twoCellAnchor')
        offset=start-1+(idx-1)*18
        for marker,rownum,coln in [('from',offset,0),('to',offset+16,8)]:
            node=ET.SubElement(anchor,f'{{{XDR}}}{marker}')
            for key,value in [('col',coln),('colOff',0),('row',rownum),('rowOff',0)]:ET.SubElement(node,f'{{{XDR}}}{key}').text=str(value)
        frame=ET.SubElement(anchor,f'{{{XDR}}}graphicFrame',{'macro':''});nv=ET.SubElement(frame,f'{{{XDR}}}nvGraphicFramePr');ET.SubElement(nv,f'{{{XDR}}}cNvPr',{'id':str(idx),'name':title_text});ET.SubElement(nv,f'{{{XDR}}}cNvGraphicFramePr');transform=ET.SubElement(frame,f'{{{XDR}}}xfrm');ET.SubElement(transform,f'{{{A}}}off',{'x':'0','y':'0'});ET.SubElement(transform,f'{{{A}}}ext',{'cx':'0','cy':'0'});graphic=ET.SubElement(frame,f'{{{A}}}graphic');gdata=ET.SubElement(graphic,f'{{{A}}}graphicData',{'uri':C});ET.SubElement(gdata,f'{{{C}}}chart',{f'{{{REL}}}id':f'rId{idx}'});ET.SubElement(anchor,f'{{{XDR}}}clientData')
        ET.SubElement(rels,f'{{{PKG}}}Relationship',{'Id':f'rId{idx}','Type':REL+'/chart','Target':'../charts/'+name})
    parts['xl/drawings/'+drawing_name]=xml_bytes(drawing);parts['xl/drawings/_rels/'+drawing_name+'.rels']=xml_bytes(rels);content_type('xl/drawings/'+drawing_name,'application/vnd.openxmlformats-officedocument.drawing+xml')
    ET.SubElement(sheet.root,q('drawing'),{f'{{{REL}}}id':'rIdMonitoring'})
    srels=ET.Element(f'{{{PKG}}}Relationships');ET.SubElement(srels,f'{{{PKG}}}Relationship',{'Id':'rIdMonitoring','Type':REL+'/drawing','Target':'../drawings/'+drawing_name})
    parts[path.rsplit('/',1)[0]+'/_rels/'+path.rsplit('/',1)[1]+'.rels']=xml_bytes(srels)
    parts[path]=sheet.finish();parts['[Content_Types].xml']=xml_bytes(types)


def add_run_tracking(parts, root, st):
    metrics = load(root, 'metrics.json')
    sheet = Sheet()
    title(sheet, 'Prediction run tracking',
        'Main totals count each match once using its latest eligible pre-kickoff shortlist entry. The history below preserves earlier predictions; it is excluded from main win rate and ROI.',
        [30,24,14,14,14,17,17,20,14], st, (2,11,'C12'))
    unique = metrics.get('shortlist', {})
    sheet.put('A6', 'Main totals — latest eligible prediction per match', st['section']); sheet.merge('A6:I6')
    sheet.row(7, ['Unique matches','Settled','Wins','Losses','Pending','Win rate','Net ROI','Profit (units)','Runs tracked'], st, True)
    sheet.row(8, [metrics.get('unique_shortlisted_fixtures','Unavailable'), unique.get('graded','Unavailable'),
        unique.get('wins','Unavailable'), unique.get('losses','Unavailable'), unique.get('pending','Unavailable'),
        unique.get('win_rate','Unavailable'), unique.get('flat_stake_roi','Unavailable'),
        unique.get('profit_per_unit_staked','Unavailable'), metrics.get('tracked_prediction_runs','Unavailable')], st)
    for c in ('F','G'): sheet.cell(c+'8').set('s',str(st['percent']))
    sheet.put('A10', 'Historical runs — descriptive results, excluded from main totals', st['section']); sheet.merge('A10:I10')
    sheet.row(11, ['Generated UTC','First snapshot','Selected','Settled','Wins','Win rate','Net ROI','Profit (units)','Pending'], st, True)
    nr = 12
    for run, values in sorted(metrics.get('run_history_groups',{}).items()):
        source = metrics.get('run_provenance',{}).get(run,{})
        sheet.row(nr, [run, source.get('first_snapshot_commit','Unavailable'), values['total'],values['graded'],
            values['wins'],values['win_rate'],values['flat_stake_roi'],values['profit_per_unit_staked'],values['pending']], st)
        for c in ('F','G'): sheet.cell(f'{c}{nr}').set('s',str(st['percent']))
        nr += 1
    if nr == 12: sheet.put('A12','No tracked prediction runs yet',st['note'])
    link(sheet,f'A{nr+2}','Dashboard','Back to dashboard',st)
    put_sheet(parts,'Run Tracking',sheet)


def format_report(destination, root, health=None, history=None):
    """Apply presentation atomically without recomputing evidence or changing it."""
    destination=Path(destination)
    with ZipFile(destination) as z:parts={n:z.read(n) for n in z.namelist()}
    if health is None:
        health = load(root, 'pipeline_health.json') or None
        history = load(root, 'health_history.json') if health else None
    st=styles(parts);ledger_layout(parts,st)
    add_experiments(parts,root,health,st);add_trends(parts,st);add_guide(parts,st);add_run_tracking(parts,root,st)
    if health is not None:add_health(parts,health,history,st)
    dashboard(parts,st,health,experiment_rows(root,health))
    # Show monitoring views first; source and simulation tabs remain available.
    wb=ET.fromstring(parts['xl/workbook.xml']);sheets=wb.find(q('sheets'))
    order=['Dashboard','Run Tracking','Experiments','Pipeline Health','Weekly Trends','Breakdowns','Calibration','Selections','Predictions','ROI Plan','Capture Details','Metric Guide']
    sheets[:]=sorted(sheets,key=lambda s:order.index(s.get('name')) if s.get('name') in order else len(order))
    parts['xl/workbook.xml']=xml_bytes(wb)
    fd,name=tempfile.mkstemp(prefix='layout.',suffix='.tmp',dir=destination.parent);os.close(fd)
    temp=Path(name)
    try:
        with ZipFile(temp,'w',ZIP_DEFLATED) as z:
            for path,data in sorted(parts.items()):
                info=ZipInfo(path,date_time=(1980,1,1,0,0,0));info.compress_type=ZIP_DEFLATED;z.writestr(info,data)
        if destination.read_bytes()!=temp.read_bytes():temp.replace(destination)
    finally:temp.unlink(missing_ok=True)
