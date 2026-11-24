"""A small standard-library .xlsx writer shared by the two readable workbooks (display only).

football_performance_report.xlsx and league_predictions.xlsx are views of data the pipeline has already written
(CSV and JSON); this module only lays them out. It never computes a prediction, probability, pick or grade.

One theme for both workbooks: a title line and a subtitle on every sheet, native Excel tables (each with its own
filter), banded rows, frozen header row and lead columns, number formats by column kind, conditional formatting,
and native charts. Kickoff and run times are shown in Nairobi time (EAT, UTC+3). Output is byte-for-byte
deterministic for the same inputs (fixed ZIP timestamps, sorted parts) and published atomically.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
import math
import os
from pathlib import Path
import re
import tempfile
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple
from xml.sax.saxutils import escape
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

EAT = timezone(timedelta(hours=3), 'EAT')
EAT_LABEL = 'EAT (Nairobi, UTC+3)'

MAIN = 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'
REL = 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'
PKG = 'http://schemas.openxmlformats.org/package/2006/relationships'
CHART = 'http://schemas.openxmlformats.org/drawingml/2006/chart'
DRAW = 'http://schemas.openxmlformats.org/drawingml/2006/main'
XDR = 'http://schemas.openxmlformats.org/drawingml/2006/spreadsheetDrawing'
SHEET_TYPE = 'application/vnd.openxmlformats-officedocument.spreadsheetml'

# Theme colours (RGB): one palette for both workbooks.
NAVY, INK, MUTED, BAND, SECTION, RULE = '1F3A5F', '1F2933', '5B6B7B', 'F2F5F9', 'E3EAF2', 'D5DCE4'
GOOD, GOOD_FILL, BAD, BAD_FILL, WARN, WARN_FILL = '1E6B3A', 'E3F2E7', '9B2226', 'FBE4E4', '7A5200', 'FFF3D6'
INFO, INFO_FILL, SERIES = '1F3A5F', 'DCE8F7', ('1F3A5F', 'D97706', '2E7D32', '9B2226')
FONT = 'Calibri'

# Column kinds: number format, horizontal alignment, wrap.
KINDS = {
    'text': (None, 'left', False),
    'wrap': (None, 'left', True),
    'int': ('0', 'right', False),
    'odds': ('0.00', 'right', False),
    'pct': ('0.0%', 'right', False),
    'signed_pct': ('+0.0%;-0.0%;0.0%', 'right', False),
    'units': ('+0.00;-0.00;0.00', 'right', False),
    'points': ('+0.0;-0.0;0.0', 'right', False),
    'decimal': ('0.000', 'right', False),
    'signed_decimal': ('+0.00000;-0.00000;0.00000', 'right', False),
    'datetime': ('ddd dd mmm hh:mm', 'left', False),
    'datetime_year': ('ddd dd mmm yyyy hh:mm', 'left', False),
    'date': ('ddd dd mmm yyyy', 'left', False),
}
# Non-table cell styles: (font id, fill id, wrap, alignment).
SPECIAL = {
    'title': (2, 0, False, 'left'), 'subtitle': (3, 0, True, 'left'), 'section': (4, 4, False, 'left'),
    'header': (1, 2, True, 'center'), 'label': (5, 0, True, 'left'), 'note': (3, 0, True, 'left'),
    'link': (6, 0, False, 'left'), 'good': (7, 5, True, 'left'), 'bad': (8, 6, True, 'left'),
    'warn': (9, 7, True, 'left'), 'info': (10, 8, True, 'left'),
}
# Conditional-formatting looks (font colour, fill colour, bold).
LOOKS = {
    'good': (GOOD, GOOD_FILL, True), 'bad': (BAD, BAD_FILL, True), 'warn': (WARN, WARN_FILL, True),
    'info': (INFO, INFO_FILL, True), 'good_font': (GOOD, None, True), 'bad_font': (BAD, None, True),
    'muted': (MUTED, None, False),
}
MISSING = '—'


@dataclass(frozen=True)
class Typed:
    """A table cell whose number format differs from its column's (summary tables mixing counts and rates)."""
    value: Any
    kind: str


# --- time and value helpers -------------------------------------------------------------------------------------

def parse_utc(value: Any) -> Optional[datetime]:
    """An aware UTC datetime from an ISO string (naive strings are read as UTC); None when missing or invalid."""
    if value is None or (isinstance(value, float) and math.isnan(value)):
        return None
    if isinstance(value, datetime):
        stamp = value
    else:
        text = str(value).strip()
        if not text or text in (MISSING, 'nan', 'NaT', 'None'):
            return None
        try:
            stamp = datetime.fromisoformat(text.replace('Z', '+00:00'))
        except ValueError:
            return None
    return stamp.replace(tzinfo=timezone.utc) if stamp.tzinfo is None else stamp.astimezone(timezone.utc)


def to_eat(value: Any) -> Optional[datetime]:
    stamp = parse_utc(value)
    return stamp.astimezone(EAT) if stamp is not None else None


def eat_text(value: Any, with_label: bool = True) -> str:
    """'Sat 15 Nov 2026 09:54 EAT', or 'not recorded'."""
    stamp = to_eat(value)
    if stamp is None:
        return 'not recorded'
    return stamp.strftime('%a %d %b %Y %H:%M') + (' EAT' if with_label else '')


def excel_time(value: Any) -> Optional[float]:
    """Excel serial number of the EAT wall-clock time (what the cell shows), or None."""
    stamp = to_eat(value)
    if stamp is None:
        return None
    local = stamp.replace(tzinfo=None)
    return round((local - datetime(1899, 12, 30)).total_seconds() / 86400, 10)


def number(value: Any) -> Optional[float]:
    """A finite float from a number or numeric text ('83.0%' -> 0.83, '+1.5' -> 1.5); None otherwise."""
    if value is None or isinstance(value, bool):
        return None
    if isinstance(value, (int, float)):
        return float(value) if math.isfinite(value) else None
    text = str(value).strip().replace(',', '')
    if not text or text == MISSING:
        return None
    scale = 1.0
    if text.endswith('%'):
        text, scale = text[:-1], 0.01
    elif text.endswith(' pp'):
        text = text[:-3]
    try:
        x = float(text) * scale
    except ValueError:
        return None
    return round(x, 12) if math.isfinite(x) else None


def present(value: Any) -> bool:
    if value is None:
        return False
    if isinstance(value, float):
        return math.isfinite(value)
    return str(value).strip() not in ('', MISSING, 'nan', 'None', 'NaN', 'NaT')


def _xml(value: Any) -> str:
    text = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f]', '', str(value))
    return escape(text, {'"': '&quot;'})


def column_letter(index: int) -> str:
    letters = ''
    while index:
        index, rest = divmod(index - 1, 26)
        letters = chr(65 + rest) + letters
    return letters


def address(row: int, col: int, absolute: bool = False) -> str:
    if absolute:
        return f'${column_letter(col)}${row}'
    return f'{column_letter(col)}{row}'


def sheet_ref(sheet: str, ref: str) -> str:
    return "'" + sheet.replace("'", "''") + "'!" + ref


# --- styles -----------------------------------------------------------------------------------------------------

class Styles:
    """cellXfs registry: one xf per (kind, band) for table cells and one per special style."""

    def __init__(self):
        self.formats: Dict[str, int] = {}
        self.xfs: List[str] = ['<xf numFmtId="0" fontId="0" fillId="0" borderId="0" xfId="0"/>']
        self.index: Dict[Tuple, int] = {}
        self.dxfs: List[str] = []
        self.dxf_index: Dict[str, int] = {}

    def _fmt(self, code: Optional[str]) -> int:
        if code is None:
            return 0
        builtin = {'0': 1, '0.00': 2}
        if code in builtin:
            return builtin[code]
        if code not in self.formats:
            self.formats[code] = 164 + len(self.formats)
        return self.formats[code]

    def _xf(self, key, fmt, font, fill, border, align, wrap, vertical='center') -> int:
        if key not in self.index:
            self.index[key] = len(self.xfs)
            apply_format = ' applyNumberFormat="1"' if fmt else ''
            wrap_text = ' wrapText="1"' if wrap else ''
            self.xfs.append(
                f'<xf numFmtId="{fmt}" fontId="{font}" fillId="{fill}" borderId="{border}" xfId="0"{apply_format}'
                f' applyFont="1" applyFill="1" applyBorder="1" applyAlignment="1">'
                f'<alignment horizontal="{align}" vertical="{vertical}"{wrap_text}/></xf>')
        return self.index[key]

    def cell(self, kind: str, band: int = 0, bold: bool = False) -> int:
        code, align, wrap = KINDS[kind]
        return self._xf(('cell', kind, band, bold), self._fmt(code), 5 if bold else 0, 3 if band else 0, 1, align,
                        wrap, 'top' if wrap else 'center')

    def special(self, name: str, kind: Optional[str] = None) -> int:
        font, fill, wrap, align = SPECIAL[name]
        code = KINDS[kind][0] if kind else None
        if kind and KINDS[kind][1] == 'right' and name in ('label', 'good', 'bad', 'warn', 'info'):
            align = 'right'
        return self._xf(('special', name, kind), self._fmt(code), font, fill, 0, align, wrap,
                        'top' if wrap and name not in ('header',) else 'center')

    def dxf(self, look: str) -> int:
        if look not in self.dxf_index:
            colour, fill, bold = LOOKS[look]
            font = f'<font>{"<b/>" if bold else ""}<color rgb="FF{colour}"/></font>'
            fills = (f'<fill><patternFill patternType="solid"><fgColor rgb="FF{fill}"/><bgColor rgb="FF{fill}"/>'
                     f'</patternFill></fill>') if fill else ''
            self.dxf_index[look] = len(self.dxfs)
            self.dxfs.append(f'<dxf>{font}{fills}</dxf>')
        return self.dxf_index[look]

    def xml(self) -> str:
        fonts = [
            f'<font><sz val="10"/><color rgb="FF{INK}"/><name val="{FONT}"/><family val="2"/></font>',
            f'<font><b/><sz val="10"/><color rgb="FFFFFFFF"/><name val="{FONT}"/><family val="2"/></font>',
            f'<font><b/><sz val="15"/><color rgb="FF{NAVY}"/><name val="{FONT}"/><family val="2"/></font>',
            f'<font><i/><sz val="10"/><color rgb="FF{MUTED}"/><name val="{FONT}"/><family val="2"/></font>',
            f'<font><b/><sz val="11"/><color rgb="FF{NAVY}"/><name val="{FONT}"/><family val="2"/></font>',
            f'<font><b/><sz val="10"/><color rgb="FF{INK}"/><name val="{FONT}"/><family val="2"/></font>',
            f'<font><u/><sz val="10"/><color rgb="FF245BA0"/><name val="{FONT}"/><family val="2"/></font>',
            f'<font><b/><sz val="10"/><color rgb="FF{GOOD}"/><name val="{FONT}"/><family val="2"/></font>',
            f'<font><b/><sz val="10"/><color rgb="FF{BAD}"/><name val="{FONT}"/><family val="2"/></font>',
            f'<font><b/><sz val="10"/><color rgb="FF{WARN}"/><name val="{FONT}"/><family val="2"/></font>',
            f'<font><b/><sz val="10"/><color rgb="FF{INFO}"/><name val="{FONT}"/><family val="2"/></font>',
        ]
        solid = lambda rgb: (f'<fill><patternFill patternType="solid"><fgColor rgb="FF{rgb}"/>'
                             f'<bgColor indexed="64"/></patternFill></fill>')
        fills = ['<fill><patternFill patternType="none"/></fill>', '<fill><patternFill patternType="gray125"/></fill>',
                 solid(NAVY), solid(BAND), solid(SECTION), solid(GOOD_FILL), solid(BAD_FILL), solid(WARN_FILL),
                 solid(INFO_FILL)]
        borders = ['<border><left/><right/><top/><bottom/><diagonal/></border>',
                   f'<border><left/><right/><top/><bottom style="thin"><color rgb="FF{RULE}"/></bottom><diagonal/>'
                   f'</border>']
        formats = ''.join(f'<numFmt numFmtId="{i}" formatCode="{_xml(code)}"/>' for code, i in self.formats.items())
        return (
            '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
            f'<styleSheet xmlns="{MAIN}">'
            + (f'<numFmts count="{len(self.formats)}">{formats}</numFmts>' if self.formats else '')
            + f'<fonts count="{len(fonts)}">{"".join(fonts)}</fonts>'
            + f'<fills count="{len(fills)}">{"".join(fills)}</fills>'
            + f'<borders count="{len(borders)}">{"".join(borders)}</borders>'
            + '<cellStyleXfs count="1"><xf numFmtId="0" fontId="0" fillId="0" borderId="0"/></cellStyleXfs>'
            + f'<cellXfs count="{len(self.xfs)}">{"".join(self.xfs)}</cellXfs>'
            + '<cellStyles count="1"><cellStyle name="Normal" xfId="0" builtinId="0"/></cellStyles>'
            + f'<dxfs count="{len(self.dxfs)}">{"".join(self.dxfs)}</dxfs>'
            + '<tableStyles count="0" defaultTableStyle="TableStyleLight1" defaultPivotStyle="PivotStyleLight16"/>'
            + '</styleSheet>')


# --- sheets -----------------------------------------------------------------------------------------------------

@dataclass
class Table:
    name: str
    top: int
    left: int
    headers: List[str]
    rows: int  # data rows (at least one)
    columns: Dict[str, int] = field(default_factory=dict)  # header -> sheet column

    @property
    def bottom(self) -> int:
        return self.top + self.rows

    @property
    def right(self) -> int:
        return self.left + len(self.headers) - 1

    def ref(self) -> str:
        return f'{address(self.top, self.left)}:{address(self.bottom, self.right)}'

    def column_range(self, header: str) -> str:
        c = self.columns[header]
        return f'{address(self.top + 1, c)}:{address(self.bottom, c)}'


@dataclass
class Chart:
    kind: str  # 'line' or 'bar'
    title: str
    categories: Tuple[int, int, int]  # (column, first row, last row) on this sheet
    series: List[Tuple[str, int]]  # (name, column)
    anchor: Tuple[int, int, int, int]  # from col, from row, to col, to row (0-based)
    number_format: str = '0'


class Sheet:
    def __init__(self, book: 'Book', name: str, tab_color: Optional[str] = None):
        self.book, self.name, self.tab_color = book, name, tab_color
        self.cells: Dict[Tuple[int, int], Tuple[Any, int]] = {}
        self.heights: Dict[int, float] = {}
        self.widths: Dict[int, float] = {}
        self.merges: List[str] = []
        self.tables: List[Table] = []
        self.rules: List[Tuple[str, str]] = []  # (sqref, cfRule xml without priority)
        self.links: List[Tuple[str, str, str]] = []  # (cell, target sheet, display)
        self.charts: List[Chart] = []
        self.freeze: Optional[Tuple[int, int]] = None  # (rows above, columns left)
        self.width = 1  # widest used column, for title merges
        self.next_row = 1

    # cells
    def put(self, row: int, col: int, value: Any, style: int) -> None:
        if isinstance(value, float) and not math.isfinite(value):
            value = None
        self.cells[(row, col)] = (value, style)
        self.width = max(self.width, col)
        self.next_row = max(self.next_row, row + 1)

    def get(self, row: int, col: int) -> Any:
        return self.cells.get((row, col), (None, 0))[0]

    def text(self, row: int, col: int, value: Any, style: str = 'label', kind: Optional[str] = None,
             merge_to: Optional[int] = None, height: Optional[float] = None) -> None:
        self.put(row, col, value, self.book.styles.special(style, kind))
        if merge_to and merge_to > col:
            self.merges.append(f'{address(row, col)}:{address(row, merge_to)}')
            for c in range(col + 1, merge_to + 1):
                self.put(row, c, None, self.book.styles.special(style, kind))
        if height:
            self.heights[row] = height

    def title(self, heading: str, subtitle: str, span: int = 10) -> None:
        """Row 1: what the sheet shows; row 2: run time, sources and where the full columns are."""
        self.text(1, 1, heading, 'title', merge_to=span, height=24)
        lines = max(1, math.ceil(len(subtitle) / max(40, span * 11)))
        self.text(2, 1, subtitle, 'subtitle', merge_to=span, height=min(15 * lines + 4, 64))
        self.next_row = 4

    def section(self, row: int, text: str, span: int) -> None:
        self.text(row, 1, text, 'section', merge_to=span, height=20)

    def note(self, row: int, text: str, span: int, style: str = 'note') -> None:
        lines = max(1, math.ceil(len(str(text)) / max(40, span * 11)))
        self.text(row, 1, text, style, merge_to=span, height=min(15 * lines + 3, 80))

    def link(self, row: int, col: int, caption: str, target: str) -> None:
        self.text(row, col, caption, 'link')
        self.links.append((address(row, col), target, caption))

    def set_width(self, col: int, width: float) -> None:
        self.widths[col] = max(self.widths.get(col, 0), width)

    # tables
    def table(self, top: int, headers: Sequence[str], rows: Sequence[Sequence[Any]], kinds: Sequence[str], *,
              left: int = 1, empty: str = 'Nothing to show', max_width: float = 48, min_width: float = 7,
              freeze_columns: Optional[int] = None, bold_first: bool = False,
              widths: Optional[Dict[str, float]] = None) -> Table:
        """A native Excel table with its own filter; banded rows; None cells shown as a dash. An empty table gets
        one row with the reason in its first column, never silent blanks."""
        headers = _unique([str(h) for h in headers])
        kinds = list(kinds)
        assert len(kinds) == len(headers), (len(kinds), len(headers))
        body = [list(r) for r in rows] or [[empty] + [MISSING] * (len(headers) - 1)]
        styles = self.book.styles
        for i, h in enumerate(headers):
            self.put(top, left + i, h, styles.special('header'))
        self.heights[top] = 30 if max(len(h) for h in headers) > 12 else 20
        for r, values in enumerate(body, start=1):
            band = (r + 1) % 2
            tall = 1
            for i, kind in enumerate(kinds):
                value = values[i] if i < len(values) else None
                use = kind
                if isinstance(value, Typed):
                    value, use = value.value, value.kind
                if value is None or (isinstance(value, float) and not math.isfinite(value)):
                    value = MISSING
                if isinstance(value, str) and KINDS[use][1] == 'right':
                    use = 'text'  # a reason or dash in a number column keeps the column's alignment simple
                if isinstance(value, bool):
                    value = 'yes' if value else 'no'
                self.put(top + r, left + i, value, styles.cell(use, band, bold_first and i == 0))
                if KINDS[kind][2] and isinstance(value, str):
                    width = (widths or {}).get(headers[i], max_width)
                    tall = max(tall, min(6, math.ceil(len(value) / max(10, width - 2))))
            if tall > 1:
                self.heights[top + r] = 14 * tall + 2
        for i, (h, kind) in enumerate(zip(headers, kinds)):
            fixed = (widths or {}).get(h)
            if fixed:
                self.set_width(left + i, fixed)
                continue
            longest = max([_shown_length(v[i] if i < len(v) else None, kind) for v in body] or [0])
            header = min(len(h), 26) * (0.6 if len(h) > 12 else 1.0) + 2
            self.set_width(left + i, max(min_width, min(max_width, max(longest + 2, header))))
        table = Table(self.book.table_name(self.name), top, left, headers, len(body),
                      {h: left + i for i, h in enumerate(headers)})
        self.tables.append(table)
        if freeze_columns is not None and self.freeze is None:
            self.freeze = (top, left - 1 + freeze_columns)
        self.next_row = max(self.next_row, table.bottom + 2)
        return table

    # conditional formatting
    def highlight(self, ref: str, look: str, rule: str, value: Any = None) -> None:
        """rule: 'contains' (any case) / 'contains_case' / 'equals' / 'begins' text, 'positive', 'negative', 'below'
        value, 'above' value."""
        top_left = ref.split(':')[0]
        dxf = self.book.styles.dxf(look)
        if rule in ('positive', 'negative', 'below', 'above'):
            operator = {'positive': 'greaterThan', 'negative': 'lessThan', 'below': 'lessThan',
                        'above': 'greaterThan'}[rule]
            threshold = 0 if rule in ('positive', 'negative') else value
            xml = (f'<cfRule type="cellIs" dxfId="{dxf}" priority="{{p}}" operator="{operator}">'
                   f'<formula>{threshold}</formula></cfRule>')
        else:
            literal = '"' + str(value).replace('"', '""') + '"'
            formula = {'contains': f'ISNUMBER(SEARCH({literal},{top_left}))',
                       'contains_case': f'ISNUMBER(FIND({literal},{top_left}))',
                       'equals': f'{top_left}={literal}',
                       'begins': f'LEFT({top_left},{len(str(value))})={literal}'}[rule]
            xml = f'<cfRule type="expression" dxfId="{dxf}" priority="{{p}}"><formula>{_xml(formula)}</formula></cfRule>'
        self.rules.append((ref, xml))

    def highlight_rows(self, table: 'Table', header: str, look: str, value: Any) -> None:
        """Every data row of `table` whose `header` cell equals `value` (text), across the whole row."""
        if table.rows < 1 or header not in table.columns:
            return
        ref = f'{address(table.top + 1, table.left)}:{address(table.bottom, table.right)}'
        key = f'${column_letter(table.columns[header])}{table.top + 1}'
        literal = '"' + str(value).replace('"', '""') + '"'
        dxf = self.book.styles.dxf(look)
        self.rules.append((ref, f'<cfRule type="expression" dxfId="{dxf}" priority="{{p}}">'
                                f'<formula>{_xml(key + "=" + literal)}</formula></cfRule>'))

    def chart(self, chart: Chart) -> None:
        self.charts.append(chart)

    # xml
    def xml(self, index: int, selected: bool) -> str:
        rows: Dict[int, List[Tuple[int, Any, int]]] = {}
        for (r, c), (value, style) in self.cells.items():
            rows.setdefault(r, []).append((c, value, style))
        last_row = max(rows) if rows else 1
        last_col = max([c for (_, c) in self.cells] or [1])
        out = ['<?xml version="1.0" encoding="UTF-8" standalone="yes"?>',
               f'<worksheet xmlns="{MAIN}" xmlns:r="{REL}">',
               '<sheetPr>' + (f'<tabColor rgb="FF{self.tab_color}"/>' if self.tab_color else '')
               + '<pageSetUpPr fitToPage="1"/></sheetPr>',
               f'<dimension ref="A1:{address(last_row, last_col)}"/>']
        selected_attr = ' tabSelected="1"' if selected else ''
        view = f'<sheetView showGridLines="0" zoomScale="100" workbookViewId="0"{selected_attr}>'
        if self.freeze:
            down, across = self.freeze
            top_left = address(down + 1, across + 1)
            pane = ('bottomRight' if down and across else 'bottomLeft' if down else 'topRight')
            split = (f' xSplit="{across}"' if across else '') + (f' ySplit="{down}"' if down else '')
            view += (f'<pane{split} topLeftCell="{top_left}" activePane="{pane}" state="frozen"/>'
                     f'<selection pane="{pane}" activeCell="{top_left}" sqref="{top_left}"/>')
        out.append(f'<sheetViews>{view}</sheetView></sheetViews>')
        out.append('<sheetFormatPr defaultRowHeight="15"/>')
        if self.widths:
            out.append('<cols>' + ''.join(
                f'<col min="{c}" max="{c}" width="{w:.1f}" customWidth="1"/>'
                for c, w in sorted(self.widths.items())) + '</cols>')
        out.append('<sheetData>')
        for r in sorted(rows):
            height = self.heights.get(r)
            out.append(f'<row r="{r}"' + (f' ht="{height:g}" customHeight="1"' if height else '') + '>')
            for c, value, style in sorted(rows[r], key=lambda item: item[0]):
                ref = address(r, c)
                if value is None:
                    out.append(f'<c r="{ref}" s="{style}"/>')
                elif isinstance(value, (int, float)) and not isinstance(value, bool):
                    out.append(f'<c r="{ref}" s="{style}"><v>{_num(value)}</v></c>')
                else:
                    out.append(f'<c r="{ref}" s="{style}" t="inlineStr"><is><t xml:space="preserve">'
                               f'{_xml(value)}</t></is></c>')
            out.append('</row>')
        out.append('</sheetData>')
        if self.merges:
            out.append(f'<mergeCells count="{len(self.merges)}">'
                       + ''.join(f'<mergeCell ref="{m}"/>' for m in self.merges) + '</mergeCells>')
        priority = 1
        for ref, rule in self.rules:
            out.append(f'<conditionalFormatting sqref="{ref}">{rule.replace("{p}", str(priority))}'
                       '</conditionalFormatting>')
            priority += 1
        if self.links:
            out.append('<hyperlinks>' + ''.join(
                f'<hyperlink ref="{cell}" location="{_xml(sheet_ref(target, "A1"))}" display="{_xml(text)}"/>'
                for cell, target, text in self.links) + '</hyperlinks>')
        out.append('<pageMargins left="0.4" right="0.4" top="0.5" bottom="0.5" header="0.3" footer="0.3"/>')
        out.append('<pageSetup orientation="landscape" fitToWidth="1" fitToHeight="0"/>')
        if self.charts:
            out.append('<drawing r:id="rIdDrawing"/>')
        if self.tables:
            out.append(f'<tableParts count="{len(self.tables)}">'
                       + ''.join(f'<tablePart r:id="rIdTable{i}"/>' for i in range(1, len(self.tables) + 1))
                       + '</tableParts>')
        out.append('</worksheet>')
        return ''.join(out)


def _num(value: float) -> str:
    if isinstance(value, int):
        return str(value)
    return repr(round(float(value), 12))


def _shown_length(value: Any, kind: str) -> float:
    if isinstance(value, Typed):
        value, kind = value.value, value.kind
    if value is None:
        return 1
    if isinstance(value, str):
        return min(len(value), 60)
    return {'datetime': 16, 'date': 15, 'pct': 7, 'signed_pct': 7, 'odds': 6, 'units': 7, 'points': 6,
            'int': max(3, len(str(int(value))) if isinstance(value, (int, float)) else 3),
            'decimal': 6, 'signed_decimal': 9}.get(kind, len(str(value)))


def _unique(headers: List[str]) -> List[str]:
    seen, out = {}, []
    for h in headers:
        h = h.strip() or 'Column'
        n = seen.get(h.lower(), 0)
        seen[h.lower()] = n + 1
        out.append(h if n == 0 else f'{h} ({n + 1})')
    return out


# --- book -------------------------------------------------------------------------------------------------------

class Book:
    def __init__(self):
        self.styles = Styles()
        self.sheets: List[Sheet] = []
        self.names: List[Tuple[str, str]] = []  # (defined name, reference)
        self._table_names: set = set()

    def sheet(self, name: str, tab_color: Optional[str] = None) -> Sheet:
        name = sheet_name(name, {s.name.lower() for s in self.sheets})
        sheet = Sheet(self, name, tab_color)
        self.sheets.append(sheet)
        return sheet

    def table_name(self, sheet: str) -> str:
        base = 'T_' + (re.sub(r'[^A-Za-z0-9_]', '_', sheet).strip('_') or 'Sheet')
        name, n = base, 1
        while name.lower() in self._table_names:
            n += 1
            name = f'{base}_{n}'
        self._table_names.add(name.lower())
        return name

    def define(self, name: str, sheet: Sheet, row: int, col: int) -> None:
        """A workbook-level name for one cell, so checks can find headline figures without fixed addresses."""
        self.names.append((name, sheet_ref(sheet.name, address(row, col, absolute=True))))

    def parts(self) -> Dict[str, str]:
        parts: Dict[str, str] = {}
        content = [f'<Override PartName="/xl/workbook.xml" ContentType="{SHEET_TYPE}.sheet.main+xml"/>',
                   f'<Override PartName="/xl/styles.xml" ContentType="{SHEET_TYPE}.styles+xml"/>']
        table_id = chart_id = drawing_id = 0
        for i, sheet in enumerate(self.sheets, start=1):
            rels = []
            for t, table in enumerate(sheet.tables, start=1):
                table_id += 1
                parts[f'xl/tables/table{table_id}.xml'] = _table_xml(table, table_id)
                rels.append(f'<Relationship Id="rIdTable{t}" Type="{REL}/table" Target="../tables/table{table_id}.xml"/>')
                content.append(f'<Override PartName="/xl/tables/table{table_id}.xml" '
                               f'ContentType="{SHEET_TYPE}.table+xml"/>')
            if sheet.charts:
                drawing_id += 1
                anchors, drels = [], []
                for k, chart in enumerate(sheet.charts, start=1):
                    chart_id += 1
                    parts[f'xl/charts/chart{chart_id}.xml'] = _chart_xml(sheet, chart)
                    content.append(f'<Override PartName="/xl/charts/chart{chart_id}.xml" '
                                   'ContentType="application/vnd.openxmlformats-officedocument.drawingml.chart+xml"/>')
                    drels.append(f'<Relationship Id="rIdChart{k}" Type="{REL}/chart" Target="../charts/chart{chart_id}.xml"/>')
                    anchors.append(_anchor_xml(chart, k))
                parts[f'xl/drawings/drawing{drawing_id}.xml'] = (
                    '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
                    f'<xdr:wsDr xmlns:xdr="{XDR}" xmlns:a="{DRAW}">{"".join(anchors)}</xdr:wsDr>')
                parts[f'xl/drawings/_rels/drawing{drawing_id}.xml.rels'] = _rels(drels)
                content.append(f'<Override PartName="/xl/drawings/drawing{drawing_id}.xml" '
                               'ContentType="application/vnd.openxmlformats-officedocument.drawing+xml"/>')
                rels.append(f'<Relationship Id="rIdDrawing" Type="{REL}/drawing" Target="../drawings/drawing{drawing_id}.xml"/>')
            parts[f'xl/worksheets/sheet{i}.xml'] = sheet.xml(i, selected=i == 1)
            content.append(f'<Override PartName="/xl/worksheets/sheet{i}.xml" ContentType="{SHEET_TYPE}.worksheet+xml"/>')
            if rels:
                parts[f'xl/worksheets/_rels/sheet{i}.xml.rels'] = _rels(rels)
        names = ''.join(f'<definedName name="{_xml(n)}">{_xml(ref)}</definedName>' for n, ref in self.names)
        parts['xl/workbook.xml'] = (
            '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
            f'<workbook xmlns="{MAIN}" xmlns:r="{REL}"><bookViews><workbookView activeTab="0"/></bookViews><sheets>'
            + ''.join(f'<sheet name="{_xml(s.name)}" sheetId="{i}" r:id="rId{i}"/>'
                      for i, s in enumerate(self.sheets, start=1))
            + '</sheets>' + (f'<definedNames>{names}</definedNames>' if names else '')
            + '<calcPr calcId="191029"/></workbook>')
        parts['xl/_rels/workbook.xml.rels'] = _rels(
            [f'<Relationship Id="rId{i}" Type="{REL}/worksheet" Target="worksheets/sheet{i}.xml"/>'
             for i in range(1, len(self.sheets) + 1)]
            + [f'<Relationship Id="rId{len(self.sheets) + 1}" Type="{REL}/styles" Target="styles.xml"/>'])
        parts['xl/styles.xml'] = self.styles.xml()
        parts['_rels/.rels'] = _rels([f'<Relationship Id="rId1" Type="{REL}/officeDocument" Target="xl/workbook.xml"/>'])
        parts['[Content_Types].xml'] = (
            '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
            '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
            '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
            '<Default Extension="xml" ContentType="application/xml"/>' + ''.join(content) + '</Types>')
        return parts

    def save(self, destination: Path, tool: str = 'the report') -> Path:
        """Write atomically with fixed timestamps; an unchanged workbook is left untouched."""
        destination = Path(destination)
        if not self.sheets:
            self.sheet('Note').text(1, 1, 'Nothing to show.', 'note')
        parts = self.parts()
        destination.parent.mkdir(parents=True, exist_ok=True)
        fd, name = tempfile.mkstemp(prefix=destination.stem + '.', suffix='.tmp', dir=destination.parent)
        os.close(fd)
        temp = Path(name)
        try:
            with ZipFile(temp, 'w', ZIP_DEFLATED) as archive:
                for path in ['[Content_Types].xml'] + sorted(p for p in parts if p != '[Content_Types].xml'):
                    info = ZipInfo(path, date_time=(1980, 1, 1, 0, 0, 0))
                    info.compress_type = ZIP_DEFLATED
                    archive.writestr(info, parts[path].encode('utf-8'))
            if not destination.exists() or destination.read_bytes() != temp.read_bytes():
                temp.replace(destination)
        except PermissionError as exc:
            raise PermissionError(f'Cannot update {destination}. Close the workbook in Excel and rerun {tool}.') from exc
        finally:
            temp.unlink(missing_ok=True)
        return destination


def sheet_name(key: str, used: Iterable[str]) -> str:
    used = set(used)
    base = (re.sub(r"[\[\]:*?/\\']", '_', str(key)).strip() or 'Sheet')[:31]
    name, n = base, 2
    while name.lower() in used:
        name = f'{base[:28]}_{n}'
        n += 1
    return name


def _rels(items: List[str]) -> str:
    return ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
            f'<Relationships xmlns="{PKG}">{"".join(items)}</Relationships>')


def _table_xml(table: Table, table_id: int) -> str:
    columns = ''.join(f'<tableColumn id="{i}" name="{_xml(h)}"/>' for i, h in enumerate(table.headers, start=1))
    return ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
            f'<table xmlns="{MAIN}" id="{table_id}" name="{table.name}" displayName="{table.name}" '
            f'ref="{table.ref()}" totalsRowShown="0"><autoFilter ref="{table.ref()}"/>'
            f'<tableColumns count="{len(table.headers)}">{columns}</tableColumns>'
            '<tableStyleInfo name="TableStyleLight1" showFirstColumn="0" showLastColumn="0" showRowStripes="0" '
            'showColumnStripes="0"/></table>')


def _anchor_xml(chart: Chart, k: int) -> str:
    c1, r1, c2, r2 = chart.anchor
    marker = lambda tag, c, r: (f'<xdr:{tag}><xdr:col>{c}</xdr:col><xdr:colOff>0</xdr:colOff><xdr:row>{r}</xdr:row>'
                                f'<xdr:rowOff>0</xdr:rowOff></xdr:{tag}>')
    return (f'<xdr:twoCellAnchor>{marker("from", c1, r1)}{marker("to", c2, r2)}'
            f'<xdr:graphicFrame macro=""><xdr:nvGraphicFramePr><xdr:cNvPr id="{k + 1}" name="{_xml(chart.title)}"/>'
            '<xdr:cNvGraphicFramePr/></xdr:nvGraphicFramePr><xdr:xfrm><a:off x="0" y="0"/><a:ext cx="0" cy="0"/>'
            f'</xdr:xfrm><a:graphic><a:graphicData uri="{CHART}"><c:chart xmlns:c="{CHART}" xmlns:r="{REL}" '
            f'r:id="rIdChart{k}"/></a:graphicData></a:graphic></xdr:graphicFrame><xdr:clientData/></xdr:twoCellAnchor>')


def _chart_xml(sheet: Sheet, chart: Chart) -> str:
    col, first, last = chart.categories
    count = max(0, last - first + 1)
    cat_ref = sheet_ref(sheet.name, f'${column_letter(col)}${first}:${column_letter(col)}${last}')
    cat_points = ''.join(f'<c:pt idx="{i}"><c:v>{_xml(sheet.get(first + i, col))}</c:v></c:pt>'
                         for i in range(count) if sheet.get(first + i, col) is not None)
    series = []
    for idx, (name, vcol) in enumerate(chart.series):
        colour = SERIES[idx % len(SERIES)]
        val_ref = sheet_ref(sheet.name, f'${column_letter(vcol)}${first}:${column_letter(vcol)}${last}')
        points = ''.join(f'<c:pt idx="{i}"><c:v>{_num(v)}</c:v></c:pt>' for i in range(count)
                         if isinstance(v := sheet.get(first + i, vcol), (int, float)) and not isinstance(v, bool))
        look = (f'<c:spPr><a:ln w="28575"><a:solidFill><a:srgbClr val="{colour}"/></a:solidFill></a:ln></c:spPr>'
                '<c:marker><c:symbol val="circle"/><c:size val="5"/></c:marker>' if chart.kind == 'line' else
                f'<c:spPr><a:solidFill><a:srgbClr val="{colour}"/></a:solidFill></c:spPr><c:invertIfNegative val="0"/>')
        series.append(
            f'<c:ser><c:idx val="{idx}"/><c:order val="{idx}"/><c:tx><c:v>{_xml(name)}</c:v></c:tx>{look}'
            f'<c:cat><c:strRef><c:f>{_xml(cat_ref)}</c:f><c:strCache><c:ptCount val="{count}"/>{cat_points}'
            f'</c:strCache></c:strRef></c:cat><c:val><c:numRef><c:f>{_xml(val_ref)}</c:f><c:numCache>'
            f'<c:formatCode>{_xml(chart.number_format)}</c:formatCode><c:ptCount val="{count}"/>{points}'
            '</c:numCache></c:numRef></c:val>' + ('<c:smooth val="0"/>' if chart.kind == 'line' else '') + '</c:ser>')
    body = ('<c:lineChart><c:grouping val="standard"/><c:varyColors val="0"/>' if chart.kind == 'line' else
            '<c:barChart><c:barDir val="col"/><c:grouping val="clustered"/><c:varyColors val="0"/>')
    body += ''.join(series)
    body += ('<c:marker val="1"/>' if chart.kind == 'line' else '<c:gapWidth val="80"/>')
    body += '<c:axId val="1"/><c:axId val="2"/>' + ('</c:lineChart>' if chart.kind == 'line' else '</c:barChart>')
    grid = f'<c:majorGridlines><c:spPr><a:ln w="6350"><a:solidFill><a:srgbClr val="{RULE}"/></a:solidFill></a:ln></c:spPr></c:majorGridlines>'
    text = (f'<c:txPr><a:bodyPr/><a:lstStyle/><a:p><a:pPr><a:defRPr sz="900"><a:solidFill><a:srgbClr val="{MUTED}"/>'
            '</a:solidFill></a:defRPr></a:pPr><a:endParaRPr lang="en-GB"/></a:p></c:txPr>')
    axes = (f'<c:catAx><c:axId val="1"/><c:scaling><c:orientation val="minMax"/></c:scaling><c:delete val="0"/>'
            f'<c:axPos val="b"/><c:numFmt formatCode="General" sourceLinked="0"/><c:tickLblPos val="low"/>{text}'
            '<c:crossAx val="2"/><c:crosses val="autoZero"/><c:auto val="1"/><c:lblAlgn val="ctr"/>'
            '<c:lblOffset val="100"/></c:catAx>'
            f'<c:valAx><c:axId val="2"/><c:scaling><c:orientation val="minMax"/></c:scaling><c:delete val="0"/>'
            f'<c:axPos val="l"/>{grid}<c:numFmt formatCode="{_xml(chart.number_format)}" sourceLinked="0"/>'
            f'<c:tickLblPos val="nextTo"/>{text}<c:crossAx val="1"/><c:crosses val="autoZero"/>'
            '<c:crossBetween val="between"/></c:valAx>')
    title = (f'<c:title><c:tx><c:rich><a:bodyPr/><a:lstStyle/><a:p><a:pPr><a:defRPr sz="1100" b="1"/></a:pPr>'
             f'<a:r><a:rPr lang="en-GB" sz="1100" b="1"><a:solidFill><a:srgbClr val="{NAVY}"/></a:solidFill>'
             f'</a:rPr><a:t>{_xml(chart.title)}</a:t></a:r></a:p></c:rich></c:tx><c:overlay val="0"/></c:title>')
    return ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
            f'<c:chartSpace xmlns:c="{CHART}" xmlns:a="{DRAW}" xmlns:r="{REL}"><c:roundedCorners val="0"/>'
            f'<c:chart>{title}<c:autoTitleDeleted val="0"/><c:plotArea><c:layout/>{body}{axes}</c:plotArea>'
            f'<c:legend><c:legendPos val="b"/><c:overlay val="0"/>{text}</c:legend><c:plotVisOnly val="1"/>'
            '<c:dispBlanksAs val="gap"/></c:chart></c:chartSpace>')


# --- reading (checks and tests; standard library) ---------------------------------------------------------------

def read_workbook(path: Path) -> Dict[str, Any]:
    """{'sheets': [names in order], 'cells': {sheet: {address: value}}, 'names': {defined name: reference}};
    numbers come back as floats, text as str (inline or shared strings)."""
    import xml.etree.ElementTree as ET
    m = '{' + MAIN + '}'
    with ZipFile(path) as archive:
        listing = set(archive.namelist())
        shared: List[str] = []
        if 'xl/sharedStrings.xml' in listing:
            for item in ET.fromstring(archive.read('xl/sharedStrings.xml')).iter(m + 'si'):
                shared.append(''.join(t.text or '' for t in item.iter(m + 't')))
        book = ET.fromstring(archive.read('xl/workbook.xml'))
        rels = ET.fromstring(archive.read('xl/_rels/workbook.xml.rels'))
        targets = {r.get('Id'): r.get('Target') for r in rels}
        out: Dict[str, Any] = {'sheets': [], 'cells': {}, 'names': {}}
        for node in book.find(m + 'sheets'):
            name = node.get('name')
            target = targets[node.get('{' + REL + '}id')].lstrip('/')
            target = target if target.startswith('xl/') else 'xl/' + target
            cells: Dict[str, Any] = {}
            for cell in ET.fromstring(archive.read(target)).iter(m + 'c'):
                kind, v = cell.get('t'), cell.find(m + 'v')
                if kind == 'inlineStr':
                    cells[cell.get('r')] = ''.join(t.text or '' for t in cell.iter(m + 't'))
                elif v is not None and kind == 's':
                    cells[cell.get('r')] = shared[int(v.text)]
                elif v is not None and kind in ('str', 'e'):
                    cells[cell.get('r')] = v.text
                elif v is not None:
                    cells[cell.get('r')] = float(v.text)
            out['sheets'].append(name)
            out['cells'][name] = cells
        names = book.find(m + 'definedNames')
        for node in names if names is not None else []:
            out['names'][node.get('name')] = node.text
    return out


def named_value(book: Dict[str, Any], name: str) -> Any:
    """The value of a single-cell defined name from read_workbook's result."""
    reference = book['names'][name]
    sheet, cell = reference.rsplit('!', 1)
    return book['cells'][sheet.strip("'").replace("''", "'")].get(cell.replace('$', ''))
