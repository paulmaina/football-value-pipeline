"""league_predictions.xlsx: the run's lists and league views in one workbook (display only; standard library).

Tabs, in order: Master shortlist, the shadow master with the same columns, Value shortlist, Cagey tier, then one
tab per league with fixtures. Only the columns used to choose or review a bet are shown; every tab's title line
names the CSV that keeps the full columns. Kickoff and quote times are in Nairobi time (EAT, UTC+3). Blank inputs
are shown with a short reason, never as a silent blank.

The shadow tab follows the run: with the strong-team master live (runs since 23 Nov 2026) it is "Previous master
(shadow)", today's master (master-new-fill-rule-v4) from master_shortlist_new.csv, the rollback baseline; earlier
runs keep "Old master (shadow)" from master_shortlist_old.csv (or master_shortlist.csv when the old master was live).
A strong-master run never reads master_shortlist_old.csv, which that release stopped writing.

Sources: the master tabs read the run bundle's raw master files (master_shortlist.csv, and
master_shortlist_old.csv or master_shortlist_new.csv), so both lists, their overlap and the inspection details are
shown as the pipeline wrote them; the value and cagey tabs read their readable CSVs; league tabs read the readable
league CSVs (the research and cagey views, the lists, the master's verdict on the best offer, the cagey tier's safest
AH line, then the benchmark's 1X2; readable_views.py) plus the raw forecasts for kickoff times when a CSV lacks them.
Nothing here selects, ranks or recomputes a pick, and no CSV is written.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List, Mapping, Optional, Sequence, Tuple
import xml.etree.ElementTree as ET
from zipfile import BadZipFile, ZipFile

import pandas as pd

import excel_book as xb

WORKBOOK_NAME = 'league_predictions.xlsx'
MASTER_TAB, OLD_TAB, VALUE_TAB, CAGEY_TAB = 'Master shortlist', 'Old master (shadow)', 'Value shortlist', 'Cagey tier'
# With the strong-team master live (released 23 Nov 2026) the shadow tab shows the previous master, the rollback
# baseline (master_shortlist_new.csv); earlier runs keep OLD_TAB.
PREVIOUS_TAB, PREVIOUS_FILE = 'Previous master (shadow)', 'master_shortlist_new.csv'
LIST_TABS = (MASTER_TAB, OLD_TAB, PREVIOUS_TAB, VALUE_TAB, CAGEY_TAB)
RELEASED = '14 Nov 2026'
MASTER_COLUMNS = ['Rank', 'Kickoff (EAT)', 'League', 'Match', 'Bet', 'Price', 'Tier', 'Cagey no-loss chance',
                  'Chance of profit', 'Research no-loss chance', 'Research gap (points)', 'Labels and flags',
                  'Inspection note']
MASTER_TAIL = ['On value shortlist', 'On cagey tier', None, 'Quote time (EAT)', 'Re-check price before betting']
# Weak-link flags on the live strong master's picks (since 24 Nov 2026, master-strong-team-v5; flag only): weak-link
# rows are red across the whole row.
WEAK_LINK, WEAK_LINK_REASONS = 'Weak link', 'Weak-link reasons'
MASTER_WEAK = [WEAK_LINK, WEAK_LINK_REASONS]
MASTER_KINDS = ['int', 'datetime', 'text', 'text', 'text', 'odds', 'text', 'pct', 'pct', 'pct', 'points', 'wrap', 'wrap',
                'text', 'text', 'text', 'datetime', 'wrap', 'text', 'wrap']
IN_OLD, IN_NEW = 'In old master (shadow)', 'In new master (live)'
IN_PREVIOUS, IN_STRONG = 'In previous master (shadow)', 'In strong master (live)'
LIST_COLUMNS = ['Kickoff (EAT)', 'League', 'Match', 'Bet', 'Price', 'Chance of no loss', 'Chance of profit',
                'Expected return', 'Probability basis', 'Price check status']
LIST_KINDS = ['datetime', 'text', 'text', 'text', 'odds', 'pct', 'pct', 'signed_pct', 'text', 'wrap']
# League tabs: the two shortlist models side by side, the lists and the master's verdict, the benchmark last.
# (column, readable CSV column, kind); kind 'reason' columns are text with the reason when blank.
LEAGUE_FIELDS = [
    ('Kickoff (EAT)', None, 'datetime'), ('Match', None, 'text'),
    ('Research lean', 'Research lean', 'text'), ('Research lean chance', 'Research lean probability', 'pct'),
    ('Cagey lean', 'Cagey lean', 'text'), ('Cagey lean chance', 'Cagey lean probability', 'pct'),
    ('Views agree', 'Views agree on the lean', 'text'),
    ('Research home win', 'Research home win', 'pct'), ('Research draw', 'Research draw', 'pct'),
    ('Research away win', 'Research away win', 'pct'),
    ('Cagey home win', 'Cagey home win', 'pct'), ('Cagey draw', 'Cagey draw', 'pct'),
    ('Cagey away win', 'Cagey away win', 'pct'),
    ('Research expected goals', 'Research expected total goals', 'odds'),
    ('Cagey expected goals', 'Cagey expected total goals', 'odds'),
    ('Research most likely score', 'Research most likely score', 'text'),
    ('Cagey most likely score', 'Cagey most likely score', 'text'),
    ('Research Over 2.5', 'Research Over 2.5', 'pct'), ('Cagey Over 2.5', 'Cagey Over 2.5', 'pct'),
    ('Research BTTS Yes', 'Research BTTS Yes', 'pct'), ('Cagey BTTS Yes', 'Cagey BTTS Yes', 'pct'),
    ('On value shortlist', 'On value shortlist', 'wrap'), ('On cagey tier', 'On cagey tier', 'wrap'),
    ('On master', 'On master', 'wrap'),
    ('Best offer', 'Best offer', 'wrap'), ('Research no-loss', 'Best offer research no-loss', 'pct'),
    ('Cagey no-loss', 'Best offer cagey no-loss', 'pct'), ('Gap (points)', 'Best offer gap (points)', 'points'),
    ('Gap label', 'Best offer gap label', 'wrap'), ('Cagey tier', 'Best offer cagey tier', 'wrap'),
    ('Master check', 'Best offer master check', 'wrap'),
    ('Safest AH line (cagey)', 'Safest AH line', 'wrap'), ('Safest AH odds (Pinnacle)', 'Safest AH Pinnacle odds', 'odds'),
    ('Safest AH cagey no-loss', 'Safest AH cagey no-loss probability', 'pct'),
    ('Safest AH research no-loss', 'Safest AH research no-loss probability', 'pct'),
    ('Benchmark home win', 'Benchmark home win', 'pct'), ('Benchmark draw', 'Benchmark draw', 'pct'),
    ('Benchmark away win', 'Benchmark away win', 'pct'),
]
LEAGUE_COLUMNS = [name for name, _, _ in LEAGUE_FIELDS]
LEAGUE_KINDS = [kind for _, _, kind in LEAGUE_FIELDS]
RECHECK = 'yes: re-check at Pinnacle before betting'


# --- inputs ------------------------------------------------------------------------------------------------------

def _csv(path: Optional[Path]) -> Optional[pd.DataFrame]:
    if path is None or not Path(path).exists():
        return None
    try:
        return pd.read_csv(path, dtype=str, keep_default_na=False, encoding='utf-8-sig')
    except pd.errors.EmptyDataError:
        return pd.DataFrame()


def _json(path: Optional[Path]) -> dict:
    try:
        return json.loads(Path(path).read_text(encoding='utf-8')) if path and Path(path).exists() else {}
    except ValueError:
        return {}


def _yes(value: Any) -> bool:
    return str(value).strip().lower() in ('true', 'yes', '1')


def _offer_key(row: Mapping) -> Tuple[str, ...]:
    kickoff = xb.parse_utc(row.get('kickoff_utc'))
    return (str(row.get('league', '')), str(row.get('home_team', '')), str(row.get('away_team', '')),
            kickoff.isoformat() if kickoff else '', str(row.get('market_to_bet', '')))


def _fixture_key(row: Mapping) -> Tuple[str, ...]:
    return _offer_key(row)[:4]


def _ranked(frame: Optional[pd.DataFrame]) -> Optional[pd.DataFrame]:
    """A new-schema master file's ranked picks (SHORTLISTED), best first; None without such a file."""
    if frame is None or 'new_master_decision' not in frame.columns:
        return None
    ranked = frame.loc[frame.new_master_decision.eq('SHORTLISTED')].copy()
    ranked['_rank'] = pd.to_numeric(ranked.new_master_rank, errors='coerce')
    return ranked.sort_values('_rank', kind='stable')


class MasterFiles:
    """The run's master lists: the live list and its shadow. Strong-master runs (since 23 Nov 2026): the strong
    master live and the previous master (master-new-fill-rule-v4, master_shortlist_new.csv) in shadow. Earlier runs:
    the new rule (released 14 Nov 2026) and the old rule, whichever was live."""

    def __init__(self, input_dir: Optional[Path]):
        import master_shortlist as ms
        self.available = input_dir is not None and Path(input_dir).exists()
        base = Path(input_dir) if self.available else None
        summary = _json(base / 'conservative_bet_summary.json') if base else {}
        live = _csv(base / ms.FILE) if base else None
        new_schema = live is not None and 'new_master_decision' in live.columns
        self.new_is_live = new_schema
        self.generated = summary.get('generated_at_utc')
        self.stale_warning = (summary.get('stale_fit_warning') or {}).get('text')  # shown above the master list
        # A strong-master run: the run recorded a strong live version, or the strong master failed and today's
        # master was published in its place (no shadow that run).
        self.strong_failed = (summary.get(ms.RELEASE_STATUS_KEY) or {}).get('status') == ms.STRONG_FAILED
        self.strong_era = (ms.strong_rule((summary.get('master_shortlist') or {}).get('version')) is not None
                           or self.strong_failed)
        self.new_all = live if new_schema else _csv(base / PREVIOUS_FILE) if base else None
        if self.strong_era:
            # The old master (v9) is no longer written; a leftover master_shortlist_old.csv is never read.
            self.old = None
            self.previous_all = None if self.strong_failed or base is None else _csv(base / PREVIOUS_FILE)
        else:
            self.old = _csv(base / ms.OLD_FILE) if base and new_schema else (live if live is not None
                                                                                 and not new_schema else None)
            self.previous_all = None
        self.new = _ranked(self.new_all)
        self.previous = _ranked(self.previous_all)
        self.previous_picks = {_fixture_key(r): r for r in (self.previous.to_dict('records')
                                                            if self.previous is not None else [])}
        if self.old is not None and 'master_rank' in self.old.columns:
            self.old = self.old.assign(_rank=pd.to_numeric(self.old.master_rank, errors='coerce')).sort_values(
                '_rank', kind='stable')
        # The new rule's view of every nominated offer (cagey and research no-loss, labels): shown for the old
        # master's picks too, so the two tabs carry the same columns.
        self.views = {_offer_key(r): r for r in (self.new_all.to_dict('records') if self.new_all is not None
                                                 and 'new_master_decision' in self.new_all.columns else [])}
        self.new_picks = {_fixture_key(r): r for r in (self.new.to_dict('records') if self.new is not None else [])}
        self.old_picks = {_fixture_key(r): r for r in (self.old.to_dict('records') if self.old is not None else [])}


def raw_forecasts(input_dir: Optional[Path]) -> Dict[Tuple[str, str, str], dict]:
    """(home, away, date) -> kickoff from the raw forecast files (display only), for CSVs without a kickoff."""
    out: Dict[Tuple[str, str, str], dict] = {}
    if input_dir is None or not Path(input_dir).exists():
        return out
    wanted = {'home_team', 'away_team', 'date', 'kickoff_utc'}
    for path in sorted(Path(input_dir).glob('*_predictions.csv')):
        try:
            frame = pd.read_csv(path, dtype=str, keep_default_na=False, usecols=lambda c: c in wanted)
        except (pd.errors.EmptyDataError, ValueError):
            continue
        for row in frame.to_dict('records'):
            out.setdefault((row.get('home_team', ''), row.get('away_team', ''), row.get('date', '')), row)
    return out


# --- master tabs -------------------------------------------------------------------------------------------------

def _number_or(value: Any, reason: str) -> Any:
    x = xb.number(value)
    return x if x is not None else reason


def _quote_age(row: Mapping, age_column: Optional[str] = None) -> Optional[float]:
    if age_column and xb.number(row.get(age_column)) is not None:
        return xb.number(row.get(age_column))
    quote, run = xb.parse_utc(row.get('offered_last_update_utc')), xb.parse_utc(row.get('evaluated_at_utc'))
    if quote is None or run is None:
        return None
    return max(0.0, (run - quote).total_seconds() / 60)


def _recheck(row: Mapping, age_column: Optional[str] = None) -> str:
    age = _quote_age(row, age_column)
    return RECHECK + (f' (quote {age:.0f} min old at the run)' if age is not None else '')


def _inspection(view: Optional[Mapping]) -> str:
    if view is None:
        return 'no new-master view of this offer'
    if not _yes(view.get('inspection_flag')):
        return 'not flagged'
    parts = [str(view.get(c)).strip() for c in ('inspection_summary', 'inspection_driver')
             if xb.present(view.get(c))]
    return 'research strongly disagrees: ' + ('; '.join(parts) if parts else 'details not recorded')


def _labels(*parts: Any) -> str:
    seen: List[str] = []
    for part in parts:
        for label in str(part or '').split(';'):
            label = label.strip()
            if label and label.lower() != 'nan' and label not in seen:
                seen.append(label)
    return '; '.join(seen) or 'none'


def _cagey(view: Optional[Mapping], missing: str) -> Any:
    if view is None:
        return missing
    x = xb.number(view.get('cagey_no_loss_probability'))
    if x is not None:
        return x
    pinnacle = xb.number(view.get('pinnacle_no_loss_probability'))
    return 'no cagey score' + (f' (Pinnacle no-loss {pinnacle:.1%})' if pinnacle is not None else '')


def _research(view: Optional[Mapping], missing: str) -> Tuple[Any, Any]:
    if view is None:
        return missing, missing
    no_loss, gap = xb.number(view.get('research_no_loss_probability')), xb.number(view.get('gap_points'))
    reason = str(view.get('missing_evidence_reason') or '').strip() or 'no research view'
    return (no_loss if no_loss is not None else reason), (gap if gap is not None else reason)


def _overlap(row: Mapping, picks: Dict, rank_column: str) -> str:
    other = picks.get(_fixture_key(row))
    if other is None:
        return 'no'
    same = str(other.get('market_to_bet')) == str(row.get('market_to_bet'))
    rank = xb.number(other.get(rank_column))
    return f"yes (rank {rank:.0f}, {'same bet' if same else 'other bet: ' + str(other.get('market_to_bet'))})" \
        if rank is not None else 'yes'


def _new_schema_rows(picks: Optional[pd.DataFrame], overlap, weak) -> List[List[Any]]:
    """Rows of a new-schema master file's ranked picks (the live master, or the previous master in shadow)."""
    rows = []
    for r in picks.to_dict('records') if picks is not None else []:
        research, gap = _research(r, 'no research view')
        rows.append([xb.number(r.get('new_master_rank')), xb.excel_time(r.get('kickoff_utc')) or 'not recorded',
                     r.get('league') or 'not recorded', f"{r.get('home_team', '')} v {r.get('away_team', '')}",
                     r.get('market_to_bet') or 'not recorded', _number_or(r.get('offered_decimal_odds'), 'no Pinnacle quote'),
                     r.get('new_master_tier') or 'not recorded', _cagey(r, 'not recorded'),
                     _number_or(r.get('ranking_profit_probability'), 'not recorded'), research, gap,
                     _labels(r.get('new_master_labels')), _inspection(r),
                     'yes' if _yes(r.get('in_value_shortlist')) else 'no',
                     'yes' if _yes(r.get('in_cagey_tier')) else 'no',
                     overlap(r),
                     xb.excel_time(r.get('offered_last_update_utc')) or 'not recorded', _recheck(r),
                     *weak(r)])
    return rows


def new_master_rows(files: MasterFiles) -> List[List[Any]]:
    if getattr(files, 'strong_era', False):  # the shadow is the previous master
        overlap = ((lambda r: _overlap(r, files.previous_picks, 'new_master_rank')) if files.previous is not None
                   else (lambda r: 'no previous master this run'))
    else:
        overlap = ((lambda r: _overlap(r, files.old_picks, 'master_rank')) if files.old is not None
                   else (lambda r: 'no old master this run'))
    return _new_schema_rows(files.new, overlap, _weak)


def previous_master_rows(files: MasterFiles) -> List[List[Any]]:
    """The previous master (today's master, master-new-fill-rule-v4) in shadow beside the strong master: its own
    ranked picks with its own cagey and research views; weak links are flagged on the live strong master only."""
    overlap = ((lambda r: _overlap(r, files.new_picks, 'new_master_rank')) if files.new is not None
               else (lambda r: 'no strong master this run'))
    return _new_schema_rows(files.previous, overlap, lambda r: ['previous master: not flagged'] * 2)


def _weak(row: Mapping) -> List[str]:
    """The pick's weak-link flag and reasons; rules before master-strong-team-v5 recorded none."""
    if 'weak_link' not in row:
        return ['not flagged (before 24 Nov 2026)', 'not flagged (before 24 Nov 2026)']
    flag = str(row.get('weak_link') or '').strip()
    reasons = row.get('weak_link_reasons')
    reasons = '' if reasons is None or (isinstance(reasons, float) and pd.isna(reasons)) else str(reasons).strip()
    return [flag if flag in ('yes', 'no') else 'not recorded', reasons or 'none']


def old_master_rows(files: MasterFiles) -> List[List[Any]]:
    rows = []
    missing = 'not nominated to the new master' if files.new_all is not None else 'no new-master view in this run'
    for r in files.old.to_dict('records') if files.old is not None else []:
        view = files.views.get(_offer_key(r))
        research, gap = _research(view, missing)
        rows.append([xb.number(r.get('master_rank')), xb.excel_time(r.get('kickoff_utc')) or 'not recorded',
                     r.get('league') or 'not recorded', f"{r.get('home_team', '')} v {r.get('away_team', '')}",
                     r.get('market_to_bet') or 'not recorded', _number_or(r.get('offered_decimal_odds'), 'no Pinnacle quote'),
                     'old rule: no tiers', _cagey(view, missing),
                     _number_or(r.get('master_profit_probability'), 'not recorded'), research, gap,
                     _labels(r.get('master_price_flag'), (view or {}).get('new_master_labels')),
                     _inspection(view) if files.new_all is not None else 'no new-master view in this run',
                     'yes' if _yes(r.get('in_value_shortlist')) else 'no',
                     'yes' if _yes(r.get('in_cagey_tier')) else 'no',
                     _overlap(r, files.new_picks, 'new_master_rank') if files.new is not None
                     else 'no new master this run',
                     xb.excel_time(r.get('offered_last_update_utc')) or 'not recorded',
                     _recheck(r, 'master_offer_age_minutes'), 'old master: not flagged', 'old master: not flagged'])
    return rows


def master_rules(sheet: xb.Sheet, table: xb.Table, overlap: str) -> None:
    sheet.highlight_rows(table, WEAK_LINK, 'bad', 'yes')  # first, so the red row wins over the column colours
    tier = table.column_range('Tier')
    sheet.highlight(tier, 'good', 'equals', 'safe')
    sheet.highlight(tier, 'info', 'equals', 'fill')
    sheet.highlight(tier, 'warn', 'equals', 'risky fill')
    labels = table.column_range('Labels and flags')
    sheet.highlight(labels, 'bad', 'contains', 'research strongly disagrees')
    sheet.highlight(labels, 'warn', 'contains', 'unvalidated view')
    sheet.highlight(labels, 'warn', 'contains', 'risky fill')
    sheet.highlight(labels, 'warn', 'contains', 'negative market EV')
    sheet.highlight(table.column_range('Inspection note'), 'bad', 'begins', 'research strongly disagrees')
    sheet.highlight(table.column_range(overlap), 'info', 'begins', 'yes')
    sheet.highlight(table.column_range('Research gap (points)'), 'bad', 'below', -4)
    sheet.highlight(table.column_range('Research gap (points)'), 'good', 'above', 4)


def previous_tab(book: xb.Book, files: MasterFiles, run: str) -> None:
    """Strong-master runs: the previous master (today's master, master_shortlist_new.csv), the rollback baseline."""
    s = book.sheet(PREVIOUS_TAB, xb.MUTED)
    columns = MASTER_COLUMNS + [c if c else IN_STRONG for c in MASTER_TAIL] + MASTER_WEAK
    s.title('Previous master (shadow): the rule live before the strong-team master, the rollback baseline',
            f'Run {run}. Today\'s master rule (master-new-fill-rule-v4): safe (market no-loss ≥75%), fill, then risky '
            'fill; it runs in shadow beside the strong-team master as its comparison and rollback baseline, with its '
            f'own cagey and research views. Not bet. Full columns: raw/{PREVIOUS_FILE}.', span=12)
    empty = ('Run bundle not available to the workbook.' if not files.available else
             'No previous-master list in this run: the strong master failed, so the master shortlist tab is '
             'today\'s master.' if files.strong_failed else
             f'No previous-master file in this run ({PREVIOUS_FILE} missing: comparison baseline missing).'
             if files.previous_all is None else
             'No nominated offer passed the previous master\'s execution and timing checks.')
    start = 4
    if getattr(files, 'stale_warning', None):
        s.note(4, f'⚠️ {files.stale_warning}', 12, style='bad')
        start = 6
    table = s.table(start, columns, previous_master_rows(files), MASTER_KINDS, freeze_columns=4, empty=empty,
                    widths={'Labels and flags': 30, 'Inspection note': 40, 'Match': 30,
                            'Re-check price before betting': 30, IN_STRONG: 22, WEAK_LINK_REASONS: 50})
    master_rules(s, table, IN_STRONG)


def master_tab(book: xb.Book, files: MasterFiles, run: str, which: str) -> None:
    if which == 'old' and getattr(files, 'strong_era', False):
        return previous_tab(book, files, run)
    new = which == 'new'
    s = book.sheet(MASTER_TAB if new else OLD_TAB, xb.NAVY if new else xb.MUTED)
    in_shadow = IN_PREVIOUS if getattr(files, 'strong_era', False) else IN_OLD
    columns = MASTER_COLUMNS + [c if c else (in_shadow if new else IN_NEW) for c in MASTER_TAIL] + MASTER_WEAK
    era = ('' if files.new_is_live or not files.available else
           f' In this run (before the {RELEASED} release, or with live set to "old") the old master was the live list.')
    if new:
        s.title('Master shortlist: the live list, best first',
                f'Run {run}. New master rule: safe (market no-loss ≥75%), fill, then risky fill; Pinnacle prices '
                f'only; the research view only labels and flags. Re-check every price at Pinnacle before betting.{era} '
                'Full columns: readable/master_shortlist_readable.csv and raw/master_shortlist.csv.', span=12)
        rows, empty = new_master_rows(files), ('Run bundle not available to the workbook.' if not files.available
                                               else 'No new-master file in this run (made before the release).'
                                               if files.new_all is None else
                                               'No nominated offer passed the master\'s execution and timing checks.')
    else:
        s.title('Old master (shadow): the old rule\'s picks, for comparison',
                f'Run {run}. Same columns as the master shortlist: cagey and research no-loss, gap, labels and '
                f'inspection come from the new rule\'s view of the same offer.{era} Full columns: '
                f'raw/{"master_shortlist_old.csv" if files.new_is_live else "master_shortlist.csv"}.', span=12)
        rows, empty = old_master_rows(files), ('Run bundle not available to the workbook.' if not files.available
                                               else 'No old-master list in this run.')
    start = 4
    if getattr(files, 'stale_warning', None):  # a stale research fit: one red line above the list
        s.note(4, f'⚠️ {files.stale_warning}', 12, style='bad')
        start = 6
    table = s.table(start, columns, rows, MASTER_KINDS, freeze_columns=4, empty=empty,
                    widths={'Labels and flags': 30, 'Inspection note': 40, 'Match': 30,
                            'Re-check price before betting': 30, in_shadow: 22, IN_NEW: 22, WEAK_LINK_REASONS: 50})
    master_rules(s, table, in_shadow if new else IN_NEW)


# --- value and cagey tabs ----------------------------------------------------------------------------------------

def _col(row: Mapping, *names: str) -> Any:
    for name in names:
        if name in row and xb.present(row[name]):
            return row[name]
    return None


def list_rows(frame: pd.DataFrame) -> List[List[Any]]:
    rows = []
    for r in frame.to_dict('records'):
        status, warning = _col(r, 'Price check status'), _col(r, 'Price check warning')
        if status is None:
            check = 'not checked in this run' if 'Price check status' in frame.columns else 'not recorded in this run'
        else:
            check = str(status) + (f': {warning}' if warning else '')
        kickoff = _col(r, 'Kickoff (UTC)')
        number = lambda *names: _number_or(_col(r, *names), 'not recorded in this run')
        rows.append([xb.excel_time(kickoff) or 'not recorded', _col(r, 'League') or 'not recorded',
                     f"{_col(r, 'Home') or ''} v {_col(r, 'Away') or ''}", _col(r, 'Market to bet') or 'not recorded',
                     number('Price'), number('Chance of no loss', 'No-loss probability'),
                     number('Chance of positive return'), number('Expected return after cost'),
                     _col(r, 'Probability basis') or 'not recorded in this run', check])
    return rows


def list_tab(book: xb.Book, name: str, frame: Optional[pd.DataFrame], message: str, run: str, csv: str,
             heading: str) -> None:
    s = book.sheet(name, '2E7D32' if name == VALUE_TAB else 'D97706')
    s.title(heading, f'Run {run}. Columns needed to judge each bet; re-check prices at Pinnacle before betting. '
                     f'Full columns (corrected-grid and diagnostic fields included): readable/{csv}.', span=10)
    rows = list_rows(frame) if frame is not None and len(frame) else []
    table = s.table(4, LIST_COLUMNS, rows, LIST_KINDS, freeze_columns=3, empty=message,
                    widths={'Price check status': 34, 'Match': 30, 'Probability basis': 26})
    check = table.column_range('Price check status')
    s.highlight(check, 'good', 'begins', 'PASSED')
    s.highlight(check, 'bad', 'begins', 'FAILED')
    s.highlight(check, 'bad', 'begins', 'BLOCKED')
    s.highlight(check, 'warn', 'begins', 'not checked')
    s.highlight(table.column_range('Expected return'), 'good_font', 'positive')
    s.highlight(table.column_range('Expected return'), 'bad_font', 'negative')


# --- league tabs -------------------------------------------------------------------------------------------------

def _view_reason(row: Mapping, view: str) -> str:
    """Why a view's cells are blank: its model column says (readable_views), else 'not in this run'."""
    text = str(row.get(f'{view} model') or '').strip()
    return f'no {view.lower()} view' if text.startswith('unavailable') else 'not in this run'


def league_rows(frame: pd.DataFrame, raw: Dict[Tuple[str, str, str], dict]) -> List[List[Any]]:
    rows = []
    for r in frame.to_dict('records'):
        home, away, day = str(r.get('Home team', '')), str(r.get('Away team', '')), str(r.get('Match date', ''))
        kickoff = xb.excel_time(r.get('Kickoff (UTC)')) or xb.excel_time(raw.get((home, away, day), {}).get('kickoff_utc'))
        if kickoff is None:
            kickoff = f'{day} (time not recorded)' if day else 'not recorded'
        reasons = {'Research': _view_reason(r, 'Research'), 'Cagey': _view_reason(r, 'Cagey')}
        best_note = str(r.get('Best offer note') or '').strip() or 'no best offer'
        safest = str(r.get('Safest AH reason') or '').strip() or 'none quoted'
        out = []
        for name, column, kind in LEAGUE_FIELDS:
            if name == 'Kickoff (EAT)':
                out.append(kickoff)
                continue
            if name == 'Match':
                out.append(f'{home} v {away}')
                continue
            value = r.get(column)
            view = name.split(' ')[0]
            if name in ('Research lean', 'Cagey lean') and not xb.present(value):
                model = str(r.get(f'{view} model') or '').strip()
                out.append(model or 'not in this run')
                continue
            if name.startswith('Safest AH'):
                reason = f'none: {safest}' if name == 'Safest AH line (cagey)' else 'no line'
            elif name in ('Research no-loss', 'Cagey no-loss', 'Gap (points)') and xb.present(r.get('Best offer')):
                reason = f'no {view.lower()} view' if view in reasons else 'one view missing'
            elif column and column.startswith('Best offer'):
                reason = best_note if name == 'Best offer' else 'no best offer'
            elif view in reasons:
                reason = reasons[view]
            else:
                reason = 'not in this run'
            if kind in ('pct', 'odds', 'points'):
                out.append(_number_or(value, reason))
            else:
                out.append(str(value) if xb.present(value) else reason)
        rows.append(out)
    return rows


def league_tab(book: xb.Book, key: str, frame: pd.DataFrame, raw: Dict, run: str) -> None:
    s = book.sheet(key, '5B6B7B')
    league = next((str(v) for v in frame.get('League', []) if xb.present(v)), key)
    s.title(f'{league}: research and cagey views of each match, and the master\'s verdict',
            f'Run {run}. Research is the value shortlist\'s model (v5 domestic, v6 UCL/UEL); cagey is the cagey tier\'s '
            f'Pinnacle market view (D_pow2 domestic, D UCL/UEL; blank without Pinnacle 1X2 and O/U 2.5). Best offer: the '
            f'master pick, else the master\'s own rule over every Pinnacle offer; gap = research minus cagey no-loss. '
            f'Safest AH: the quoted Pinnacle line with the highest cagey no-loss. The benchmark (70% Pinnacle blend) is '
            f'display only. Full columns: readable/{key}_predictions_readable.csv.', span=12)
    table = s.table(4, LEAGUE_COLUMNS, league_rows(frame, raw), LEAGUE_KINDS, freeze_columns=2,
                    empty='No fixtures for this league in this run.',
                    widths={'Match': 32, 'Research lean': 24, 'Cagey lean': 24, 'On value shortlist': 24,
                            'On cagey tier': 28, 'On master': 28, 'Best offer': 26, 'Gap label': 26,
                            'Cagey tier': 24, 'Master check': 24, 'Safest AH line (cagey)': 30})
    s.highlight(table.column_range('Safest AH line (cagey)'), 'muted', 'begins', 'none')
    s.highlight(table.column_range('Views agree'), 'warn', 'equals', 'no')
    s.highlight(table.column_range('On master'), 'info', 'begins', 'yes')
    s.highlight(table.column_range('Gap label'), 'bad', 'contains', 'flagged for inspection')
    s.highlight(table.column_range('Gap (points)'), 'bad', 'below', -4)
    s.highlight(table.column_range('Gap (points)'), 'good', 'above', 4)
    s.highlight(table.column_range('Cagey tier'), 'good', 'begins', 'safe')
    s.highlight(table.column_range('Cagey tier'), 'warn', 'begins', 'risky')


# --- workbook ----------------------------------------------------------------------------------------------------

def run_time(input_dir: Optional[Path], files: MasterFiles) -> str:
    stamp = files.generated
    if stamp is None and files.new is not None and len(files.new):
        stamp = files.new.iloc[0].get('evaluated_at_utc')
    return xb.eat_text(stamp) if stamp else 'time not recorded'


def build(frames: Sequence[Tuple[str, pd.DataFrame]], shortlists: Optional[Sequence[Tuple[str, Optional[pd.DataFrame], str]]],
          input_dir: Optional[Path]) -> xb.Book:
    files = MasterFiles(input_dir)
    run = run_time(input_dir, files)
    book = xb.Book()
    master_tab(book, files, run, 'new')
    master_tab(book, files, run, 'old')
    lists = {name: (frame, message) for name, frame, message in (shortlists or ())}
    for name, csv, heading in ((VALUE_TAB, 'conservative_bet_shortlist_readable.csv',
                                'Value shortlist: research-model value bets'),
                               (CAGEY_TAB, 'cagey_tier_shortlist_readable.csv',
                                'Cagey tier: market-view no-loss bets')):
        frame, message = lists.get(name, (None, f'No {name.lower()} in this run.'))
        list_tab(book, name, frame, message, run, csv, heading)
    raw = raw_forecasts(input_dir)
    used = {n.lower() for n in LIST_TABS}
    for key, frame in frames:
        if frame is None or frame.empty:
            continue
        name = xb.sheet_name(key, used)
        used.add(name.lower())
        league_tab(book, name, frame, raw, run)
    return book


def write(frames, destination: Path, shortlists=None, input_dir: Optional[Path] = None) -> Path:
    return build(frames, shortlists, input_dir).save(destination, 'the formatter')


def league_tabs(destination: Path) -> List[str]:
    """League tab names of an existing workbook (the four list tabs excluded)."""
    try:
        with ZipFile(destination) as archive:
            root = ET.fromstring(archive.read('xl/workbook.xml'))
    except (OSError, KeyError, ET.ParseError, BadZipFile):
        return []
    ns = {'m': xb.MAIN}
    return [s.get('name') for s in root.findall('m:sheets/m:sheet', ns)
            if s.get('name') not in set(LIST_TABS) | {'No fixtures', 'Note'}]
