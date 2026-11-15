"""The sheets of football_performance_report.xlsx (display only; standard library).

Master tracking starts afresh at the first forecast run after the new master went live (PR #175's release of
14 Nov 2026): the live master and the old master (shadow) are shown only from that run on. Earlier graded data
stays in the repo untouched (grading and the rollback check read it) but is not shown here.

Every figure is read from files the review has already written; nothing is graded, recomputed for a decision or
changed. Sources:

  performance/price_edge_v27/master_shortlist_picks.csv       graded new-master picks (every column)
  performance/price_edge_v27/master_shortlist_old_picks.csv   graded old-master picks (every column)
  performance/price_edge_v27/summary.json                     rollback rule, release incidents, live list
  performance/research_v5_monitoring.json                     research v5 vs v4 rollback, home-favourite check
  performance/clv_report/                                     candidate closing-line value
  performance/pipeline_health.json, workflow_health.json      data health and the last validation's warnings
  odds_api_usage/usage_log.jsonl                              Odds API credits and the last forecast run
  model_activity/activity_log.jsonl                           releases, refits, stale fits, switch changes, rollback
                                                              checks and master fallbacks (model_activity.py)

Release status. Each monitored release's status starts from its live switch, read when the workbook is built, so no
section can show an outdated release status:

  master_shortlist_config.json  live           "new": Live (new master)    "old": Rolled back to the old master
  research_config.json          live.domestic  "v5":  Live (research v5)   "v4":  Rolled back to research v4
  research_config.json          live.european  "v6":  Live (research v6)   "v4":  Rolled back to CE (research v4)

While a release is live its status adds the rollback check's state, or "monitoring data not available yet" with the
reason (the review has not written the figures, or no graded matches yet). After a rollback the date is the first
archived forecast run made without the release, when one exists. CE3n's figures are research_monitoring's "ce3n"
entry of research_v5_monitoring.json (PR #178).
"""
from __future__ import annotations

from csv_utils import dict_reader
from datetime import datetime
import json
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple

import excel_book as xb
from excel_book import Typed

REPORT_NAME = 'football_performance_report.xlsx'
SHEETS = ('Dashboard', 'Picks & Results', 'Weekly Trends', 'Breakdowns', 'Calibration', 'CLV', 'Model Monitoring',
          'Model Activity', 'Guide')
RELEASED = '14 Nov 2026'  # the new master's release (docs/plan.md, Decisions: Master shortlist release)
TRACKING = Path('price_edge_v27')
GRADED = {'new': TRACKING / 'master_shortlist_picks.csv', 'old': TRACKING / 'master_shortlist_old_picks.csv'}
PICKS_CSV = ('performance/price_edge_v27/master_shortlist_picks.csv (new) and master_shortlist_old_picks.csv (old)')
# The release switches; None reads the pipeline's own (master_shortlist.CONFIG, team_research.RESEARCH_CONFIG).
MASTER_CONFIG: Optional[Path] = None
RESEARCH_CONFIG: Optional[Path] = None
MONITORING = 'research_v5_monitoring.json'
NOT_AVAILABLE = 'monitoring data not available yet'
SETTLED = {'WON': 'Won', 'HALF_WON': 'Half won', 'REFUNDED': 'Refund', 'HALF_LOST': 'Half lost', 'LOST': 'Lost'}
BANDS = ((0.0, 0.5), (0.5, 0.6), (0.6, 0.7), (0.7, 0.75), (0.75, 0.8), (0.8, 0.85), (0.85, 0.9), (0.9, 1.000001))
TIERS = ('safe', 'fill', 'risky fill')
NO_GRADED = 'no graded picks yet'
SMALL = 30  # below this many graded picks a rate is a small sample


# --- reading -----------------------------------------------------------------------------------------------------

def load(root: Path, relative: str | Path) -> dict:
    path = Path(root) / 'performance' / relative
    try:
        return json.loads(path.read_text(encoding='utf-8')) if path.exists() else {}
    except ValueError:
        return {}


def read_rows(path: Path) -> List[dict]:
    if not path.exists() or path.stat().st_size == 0:
        return []
    with path.open(encoding='utf-8-sig', newline='') as handle:
        return list(dict_reader(handle))


def tracking_start(root: Path) -> Optional[datetime]:
    """Generation time of the first archived run made by the released new master (its run summary records the
    released version), or None while no such run exists."""
    from master_shortlist import VERSION_NEW_LIVE
    base = Path(root) / 'performance' / 'snapshots'
    stamps = []
    for path in sorted(base.glob('*/selection_summary.json')) if base.exists() else []:
        if path.parent.name.startswith('.capture-'):
            continue
        try:
            summary = json.loads(path.read_text(encoding='utf-8'))
        except (OSError, ValueError):
            continue
        if (summary.get('master_shortlist') or {}).get('version') == VERSION_NEW_LIVE:
            stamp = xb.parse_utc(summary.get('generated_at_utc'))
            if stamp is not None:
                stamps.append(stamp)
    return min(stamps) if stamps else None


def live_list(root: Path) -> str:
    """'new' or 'old': which master is live now, from master_shortlist_config.json's switch (rolling back is setting
    it to "old"); the review's record only when the switch can't be read."""
    value, _ = switch('master')
    if value is not None:
        return value
    recorded = load(root, TRACKING / 'summary.json').get('live_master_list')
    return recorded if recorded in ('new', 'old') else 'new'


def list_names(root: Path) -> Dict[str, str]:
    live = live_list(root)
    return {'new': 'New master (live)' if live == 'new' else 'New master (shadow)',
            'old': 'Old master (live)' if live == 'old' else 'Old master (shadow)'}


def market_family(row: dict) -> str:
    bet = str(row.get('market_to_bet') or row.get('market') or '')
    if bet.startswith('Asian Handicap') or bet.startswith('Draw No Bet'):
        return 'Asian handicap'
    if bet.startswith('Double Chance'):
        return 'Double chance'
    if bet in ('Home win', 'Away win') or bet.endswith(' win'):
        return 'Match winner'
    if bet.startswith('Over') or bet.startswith('Under'):
        return 'Totals'
    return bet or 'not recorded'


def fixture_identity(row: dict) -> Tuple[str, str, str, str]:
    kickoff = xb.parse_utc(row.get('kickoff_utc'))
    return (str(row.get('league') or ''), str(row.get('home_team') or ''), str(row.get('away_team') or ''),
            kickoff.isoformat() if kickoff else '')


def week_of(kickoff: Optional[datetime]) -> str:
    if kickoff is None:
        return 'not recorded'
    iso = kickoff.isocalendar()
    return f'{iso.year}-W{iso.week:02d}'


def picks(root: Path, start: Optional[datetime]) -> List[dict]:
    """Both lists' graded picks from the tracking start on, one display record per pick."""
    if start is None:
        return []
    out = []
    raw = {which: [r for r in read_rows(Path(root) / 'performance' / GRADED[which])
                   if (xb.parse_utc(r.get('snapshot_generated_utc')) or datetime.min.replace(tzinfo=start.tzinfo))
                   >= start] for which in GRADED}
    keys = {which: {fixture_identity(r) for r in rows} for which, rows in raw.items()}
    for which, rows in raw.items():
        other = 'old' if which == 'new' else 'new'
        for r in rows:
            kickoff = xb.parse_utc(r.get('kickoff_utc'))
            status = str(r.get('result_status') or '')
            profit = xb.number(r.get('unit_profit')) if status in SETTLED else None
            if which == 'new':
                tier = r.get('new_master_tier') or 'not recorded'
                no_loss, profit_p = r.get('ranking_no_loss_probability'), r.get('ranking_profit_probability')
                labels = [x.strip() for x in str(r.get('new_master_labels') or '').split(';') if x.strip()]
            else:
                tier = 'old rule (no tiers)'
                no_loss, profit_p = r.get('master_no_loss_probability'), r.get('master_profit_probability')
                labels = [str(r['master_price_flag'])] if xb.present(r.get('master_price_flag')) else []
            flags = [name for name, column in (('on value shortlist', 'in_value_shortlist'),
                                                ('on cagey tier', 'in_cagey_tier')) if str(r.get(column)) == 'True']
            out.append({
                'list': which, 'kickoff': kickoff, 'week': week_of(kickoff), 'league': r.get('league') or 'not recorded',
                'match': f"{r.get('home_team', '')} v {r.get('away_team', '')}", 'bet': r.get('market_to_bet') or r.get('market'),
                'market': market_family(r), 'price': xb.number(r.get('offered_decimal_odds')), 'tier': tier,
                'p_no_loss': xb.number(no_loss), 'p_profit': xb.number(profit_p), 'labels': labels, 'flags': flags,
                'score': r.get('final_score') if xb.present(r.get('final_score')) else None,
                'status': status, 'profit': profit, 'clv': xb.number(r.get('clv')),
                'in_other': fixture_identity(r) in keys[other],
            })
    return sorted(out, key=lambda p: (p['kickoff'] or datetime.max.replace(tzinfo=start.tzinfo), p['list'], p['match']))


def stats(rows: Sequence[dict]) -> dict:
    graded = [r for r in rows if r['profit'] is not None]
    gains = [r['profit'] for r in graded]
    prices = [r['price'] for r in graded if r['price'] is not None]
    clv = [r['clv'] for r in rows if r['clv'] is not None]
    n = len(graded)
    return {'picks': len(rows), 'graded': n, 'pending': len(rows) - n,
            'wins': sum(g > 1e-12 for g in gains), 'no_loss': sum(g >= -1e-12 for g in gains),
            'win_rate': sum(g > 1e-12 for g in gains) / n if n else None,
            'no_loss_rate': sum(g >= -1e-12 for g in gains) / n if n else None,
            'return': sum(gains) if n else None, 'per_bet': sum(gains) / n if n else None,
            'odds': sum(prices) / len(prices) if prices else None,
            'clv_n': len(clv), 'clv': sum(clv) / len(clv) if clv else None,
            'clv_positive': sum(c > 0 for c in clv) / len(clv) if clv else None}


def outcome(record: dict) -> str:
    if record['status'] in SETTLED:
        return SETTLED[record['status']]
    if record['status'] == 'UNVERIFIED_FIXTURE_OR_RESULT':
        return 'Not graded yet (result not verified)'
    return 'Not graded yet'


# --- release status ----------------------------------------------------------------------------------------------

# Each monitored release: its switch (config attribute, key path), the released and rolled-back values and texts;
# for research, the scope (European or domestic), its entry in research_v5_monitoring.json and its minimum sample.
RELEASES = {
    'master': {'config': 'MASTER_CONFIG', 'path': ('live',), 'released': 'new', 'rolled': 'old',
               'live': 'Live (new master)', 'back': 'Rolled back to the old master'},
    'v5': {'config': 'RESEARCH_CONFIG', 'path': ('live', 'domestic'), 'released': 'v5', 'rolled': 'v4',
           'live': 'Live (research v5)', 'back': 'Rolled back to research v4', 'european': False,
           'figures': 'rollback', 'matches': 'domestic', 'minimum': ('MIN_MATCHES', 'MIN_WEEKS')},
    'v6': {'config': 'RESEARCH_CONFIG', 'path': ('live', 'european'), 'released': 'v6', 'rolled': 'v4',
           'live': 'Live (research v6)', 'back': 'Rolled back to CE (research v4)', 'european': True,
           'figures': 'ce3n', 'matches': 'European (UCL/UEL)', 'minimum': ('CE3N_MIN_MATCHES', 'CE3N_MIN_WEEKS')},
}


def config_path(key: str) -> Path:
    """The release's switch file: the same one the pipeline reads, unless overridden here."""
    name = RELEASES[key]['config']
    if globals()[name] is not None:
        return Path(globals()[name])
    if name == 'MASTER_CONFIG':
        import master_shortlist
        return Path(master_shortlist.CONFIG)
    import team_research
    return Path(team_research.RESEARCH_CONFIG)


def switch(key: str) -> Tuple[Optional[str], str]:
    """(the switch's value, '') or (None, why it can't be read)."""
    spec = RELEASES[key]
    path = config_path(key)
    where = f"{path.name} {'.'.join(spec['path'])}"
    try:
        value: Any = json.loads(path.read_text(encoding='utf-8'))
        for part in spec['path']:
            value = value[part]
    except (OSError, ValueError, KeyError, TypeError) as exc:
        return None, f'{where} could not be read ({type(exc).__name__})'
    if value not in (spec['released'], spec['rolled']):
        return None, f'{where} is {value!r}, expected "{spec["released"]}" or "{spec["rolled"]}"'
    return value, ''


def load_json(path: Path) -> dict:
    try:
        data = json.loads(Path(path).read_text(encoding='utf-8'))
    except (OSError, ValueError):
        return {}
    return data if isinstance(data, dict) else {}


def archived_runs(root: Path, name: str) -> List[Tuple[datetime, Path]]:
    """(generation time, folder) of every archived run holding `name`, oldest first."""
    base = Path(root) / 'performance' / 'snapshots'
    out = []
    for path in sorted(base.glob(f'*/{name}')) if base.exists() else []:
        if path.parent.name.startswith('.capture-'):
            continue
        meta = 'selection_summary.json' if name == 'selection_summary.json' else 'metadata.json'
        stamp = xb.parse_utc(load_json(path.parent / meta).get('generated_at_utc'))
        if stamp is not None:
            out.append((stamp, path.parent))
    return sorted(out)


def research_versions(folder: Path, european: bool) -> set:
    """The research versions of a run's forecasts in one scope (UCL/UEL or domestic)."""
    from team_research import EUROPEAN_COMPETITIONS, decode
    versions = set()
    for row in read_rows(folder / 'predictions.csv'):
        if (str(row.get('league')) in EUROPEAN_COMPETITIONS) == european:
            version = decode(row.get('team_research_json')).get('version')
            if version:
                versions.add(version)
    return versions


def rollback_date(root: Path, key: str) -> Optional[datetime]:
    """When a release was rolled back: the first archived run after the release's last run that was made without it,
    or None when no run has been made since (or the release never ran)."""
    after = None
    if key == 'master':
        from master_shortlist import VERSION_NEW_LIVE
        for stamp, folder in reversed(archived_runs(root, 'selection_summary.json')):
            version = (load_json(folder / 'selection_summary.json').get('master_shortlist') or {}).get('version')
            if version == VERSION_NEW_LIVE:
                return after
            after = stamp if version else after
        return None
    from team_research import CE3N_VERSIONS, C6_VERSIONS
    released = set(CE3N_VERSIONS if RELEASES[key]['european'] else C6_VERSIONS)
    for stamp, folder in reversed(archived_runs(root, 'predictions.csv')):
        versions = research_versions(folder, RELEASES[key]['european'])
        if versions & released:
            return after
        after = stamp if versions else after
    return None


def research_minimum(key: str) -> Tuple[int, int]:
    import research_monitoring as rm
    matches, weeks = RELEASES[key]['minimum']
    return int(getattr(rm, matches)), int(getattr(rm, weeks))


def research_figures(root: Path, key: str) -> Tuple[Optional[dict], str]:
    """(the release's monitoring figures, '') or (None, why there are none)."""
    if not (Path(root) / 'performance' / MONITORING).exists():
        return None, f'the review has not written performance/{MONITORING} yet'
    figures = load(root, MONITORING).get(RELEASES[key]['figures'])
    if not isinstance(figures, dict) or not figures:
        return None, f'performance/{MONITORING} has no "{RELEASES[key]["figures"]}" entry yet'
    return figures, ''


def release_status(root: Path, key: str, state: Optional[str] = None, missing: str = '') -> str:
    """The release's status from its live switch: rolled back (with the date when known), or live with the rollback
    check's state (`state` for the master), or live with why monitoring data is not available yet."""
    spec = RELEASES[key]
    value, problem = switch(key)
    if value is None:
        return f'Release status unknown: {problem}'
    if value == spec['rolled']:
        date = rollback_date(root, key)
        return spec['back'] + (f' on {xb.eat_text(date)} (first forecast run after the switch)' if date else
                               ' (date not known: no archived forecast run since the switch)')
    if key == 'master':
        return f"{spec['live']} - {state}" if state else f"{spec['live']} - {NOT_AVAILABLE} ({missing})"
    figures, why = research_figures(root, key)
    if figures is None:
        return f"{spec['live']} - {NOT_AVAILABLE} ({why})"
    matches, weeks = int(figures.get('matches') or 0), int(figures.get('weeks') or 0)
    if not matches:
        return f"{spec['live']} - {NOT_AVAILABLE} (no graded {spec['matches']} matches under research {key} yet)"
    if figures.get('triggered'):
        return f"{spec['live']} - ROLLBACK TRIGGERED"
    if figures.get('eligible'):
        return f"{spec['live']} - not triggered"
    need_matches, need_weeks = research_minimum(key)
    return (f"{spec['live']} - not yet eligible ({matches} of {need_matches} graded matches, "
            f"{weeks} of {need_weeks} weeks)")


def master_status(root: Path, rollback: dict) -> str:
    return release_status(root, 'master', master_rollback_status(rollback) if rollback else None,
                          'the review has not recorded the rollback check yet')


def health_data(root: Path, health: Optional[dict]) -> dict:
    return health if health is not None else load(root, 'pipeline_health.json')


def usage(root: Path) -> Tuple[List[dict], dict]:
    """The Odds API usage log under this output root (odds_api_usage/usage_log.jsonl) and the latest key balances."""
    from odds_api_usage import LOG, latest_balances, read_log
    records = read_log(root, LOG.relative_to(LOG.parts[0]))
    return records, latest_balances(records)


def activity_log(root: Path) -> List[dict]:
    """The model activity log under this output root (model_activity/activity_log.jsonl), oldest first."""
    from model_activity import RELATIVE, read
    try:
        return read(Path(root) / RELATIVE)
    except Exception:  # noqa: BLE001  (display only)
        return []


def latest_activity(events: Sequence[dict], key: str) -> Optional[dict]:
    from model_activity import last
    return last(events, key)


# --- formatting helpers ------------------------------------------------------------------------------------------

def value_or(value: Any, reason: str, kind: Optional[str] = None) -> Any:
    if value is None:
        return reason
    return Typed(value, kind) if kind else value


def interval_text(interval: Any, kind: str = 'pct') -> str:
    if not interval or len(interval) != 2 or any(xb.number(v) is None for v in interval):
        return 'not computed yet'
    a, b = (float(v) for v in interval)
    if kind == 'pct':
        return f'{a:+.1%} to {b:+.1%}'
    return f'{a:+.5f} to {b:+.5f}'


def status_rules(sheet: xb.Sheet, ref: str) -> None:
    for text in ('ROLLBACK TRIGGERED', 'FAILED', 'MISSING', 'Release status unknown'):
        sheet.highlight(ref, 'bad', 'contains_case', text)
    sheet.highlight(ref, 'warn', 'begins', 'Rolled back')
    sheet.highlight(ref, 'good', 'contains', 'not triggered')
    for text in ('not yet eligible', 'Waiting', NOT_AVAILABLE):
        sheet.highlight(ref, 'warn', 'contains', text)


def result_rules(sheet: xb.Sheet, table: xb.Table, result: str = 'Result', money: Iterable[str] = ()) -> None:
    ref = table.column_range(result)
    sheet.highlight(ref, 'good', 'begins', 'Won')
    sheet.highlight(ref, 'good', 'equals', 'Half won')
    sheet.highlight(ref, 'bad', 'equals', 'Lost')
    sheet.highlight(ref, 'bad', 'equals', 'Half lost')
    sheet.highlight(ref, 'muted', 'begins', 'Not graded')
    for header in money:
        sheet.highlight(table.column_range(header), 'good_font', 'positive')
        sheet.highlight(table.column_range(header), 'bad_font', 'negative')


def tier_rules(sheet: xb.Sheet, ref: str) -> None:
    sheet.highlight(ref, 'good', 'equals', 'safe')
    sheet.highlight(ref, 'info', 'equals', 'fill')
    sheet.highlight(ref, 'warn', 'equals', 'risky fill')


def label_rules(sheet: xb.Sheet, ref: str) -> None:
    sheet.highlight(ref, 'bad', 'contains', 'research strongly disagrees')
    sheet.highlight(ref, 'warn', 'contains', 'unvalidated view')
    sheet.highlight(ref, 'warn', 'contains', 'risky fill')


def money_rules(sheet: xb.Sheet, table: xb.Table, headers: Iterable[str]) -> None:
    for header in headers:
        sheet.highlight(table.column_range(header), 'good_font', 'positive')
        sheet.highlight(table.column_range(header), 'bad_font', 'negative')


def nav(sheet: xb.Sheet, row: int) -> None:
    sheet.link(row, 1, '← Dashboard', 'Dashboard')


# --- sheets ------------------------------------------------------------------------------------------------------

class Context:
    def __init__(self, root: Path, metrics: dict, health: Optional[dict]):
        self.root = Path(root)
        self.metrics = metrics or {}
        self.health = health_data(self.root, health) or {}
        self.start = tracking_start(self.root)
        self.names = list_names(self.root)
        self.picks = picks(self.root, self.start)
        self.by_list = {w: [p for p in self.picks if p['list'] == w] for w in ('new', 'old')}
        self.tracking = load(self.root, TRACKING / 'summary.json')
        self.research = load(self.root, 'research_v5_monitoring.json')
        self.activity = activity_log(self.root)
        reviewed = self.metrics.get('reviewed_at_utc') or self.health.get('reviewed_at_utc') \
            or self.tracking.get('reviewed_at_utc')
        self.run = xb.eat_text(reviewed)

    @property
    def start_text(self) -> str:
        """The tracking start as a phrase: a date, or why there is none yet."""
        if self.start is None:
            return f'not started yet (the first forecast run after the {RELEASED} release; none archived yet)'
        return xb.eat_text(self.start)

    @property
    def tracking_phrase(self) -> str:
        if self.start is None:
            return (f'Master tracking has not started yet: it begins with the first forecast run after the new master '
                    f'went live on {RELEASED}, and none is archived yet')
        return f'Master tracking from {self.start_text} (the first forecast run after the {RELEASED} release)'

    def empty(self, what: str) -> str:
        if self.start is None:
            return f'No {what} yet: master tracking has not started (first forecast run after the {RELEASED} release).'
        return f'No {what} since the start ({self.start_text}).'

    def subtitle(self, what: str, csv: str = PICKS_CSV) -> str:
        return f'{what} Run {self.run}. {self.tracking_phrase}. Full columns: {csv}.'


def dashboard(book: xb.Book, ctx: Context) -> None:
    s = book.sheet('Dashboard', xb.NAVY)
    s.title('Performance dashboard: live master vs old master (shadow)',
            ctx.subtitle('Headline results at Pinnacle prices, rollback checks and data health.'), span=6)
    new, old = (stats(ctx.by_list[w]) for w in ('new', 'old'))
    style = 'info' if ctx.start is not None else 'warn'
    s.note(4, (f'Master tracking started afresh on {ctx.start_text}, the first forecast run after the new master went '
               f'live ({RELEASED}).' if ctx.start is not None else ctx.tracking_phrase + '.')
           + ' Graded picks from before the start stay in the repo (grading and the rollback check use them) and are '
             'not shown in this workbook.', 6, style)
    row = 6
    s.section(row, 'Headline results (1-unit flat stakes at the Pinnacle price)', 6)
    rows = []
    for label, key, kind in (('Picks since the start', 'picks', 'int'), ('Graded', 'graded', 'int'),
                             ('Not graded yet', 'pending', 'int'), ('Wins (full or half)', 'wins', 'int'),
                             ('Win rate', 'win_rate', 'pct'), ('No-loss rate (win, half win or refund)', 'no_loss_rate', 'pct'),
                             ('Return (units)', 'return', 'units'), ('Return per bet', 'per_bet', 'signed_pct'),
                             ('Average odds (graded picks)', 'odds', 'odds'),
                             ('Mean CLV (picks with a near-kickoff quote)', 'clv', 'signed_pct')):
        rows.append([label, value_or(new[key], NO_GRADED if key not in ('picks', 'pending') else 0, kind),
                     value_or(old[key], NO_GRADED if key not in ('picks', 'pending') else 0, kind)])
    table = s.table(row + 1, ['Measure', ctx.names['new'], ctx.names['old']], rows, ['text', 'int', 'int'],
                    widths={'Measure': 40, ctx.names['new']: 22, ctx.names['old']: 22}, bold_first=True)
    # Named cells: workflow_checks.py reads the headline figures by name, not by address.
    for which, col in (('new', table.left + 1), ('old', table.left + 2)):
        for name, offset in (('picks', 1), ('graded', 2), ('return', 7)):
            book.define(f'{which}_master_{name}', s, table.top + offset, col)
    for col in (table.left + 1, table.left + 2):  # return and return per bet: green above zero, red below
        ref = f'{xb.address(table.top + 7, col)}:{xb.address(table.top + 8, col)}'
        s.highlight(ref, 'good_font', 'positive')
        s.highlight(ref, 'bad_font', 'negative')
    book.define('master_tracking_start', s, 4, 1)
    row = table.bottom + 2

    s.section(row, 'Return by tier', 6)
    tier_rows = []
    for which in ('new', 'old'):
        groups = ([(t, [p for p in ctx.by_list[which] if p['tier'] == t]) for t in TIERS] if which == 'new'
                  else [('all picks (old rule has no tiers)', ctx.by_list[which])])
        for tier, part in groups:
            st = stats(part)
            tier_rows.append([ctx.names[which], tier, st['picks'], st['graded'],
                              value_or(st['win_rate'], NO_GRADED), value_or(st['no_loss_rate'], NO_GRADED),
                              value_or(st['return'], NO_GRADED), value_or(st['per_bet'], NO_GRADED)])
    table = s.table(row + 1, ['List', 'Tier', 'Picks', 'Graded', 'Win rate', 'No-loss rate', 'Return (units)',
                              'Return per bet'], tier_rows,
                    ['text', 'text', 'int', 'int', 'pct', 'pct', 'units', 'signed_pct'])
    tier_rules(s, table.column_range('Tier'))
    money_rules(s, table, ['Return (units)', 'Return per bet'])
    row = table.bottom + 2

    s.section(row, 'Rollback status', 6)
    checks = monitoring_checks(ctx)
    table = s.table(row + 1, ['Check', 'Status', 'Detail'], [c[:3] for c in checks], ['text', 'text', 'wrap'],
                    widths={'Check': 40, 'Status': 30, 'Detail': 70}, bold_first=True)
    status_rules(s, table.column_range('Status'))
    book.define('master_rollback_status', s, table.top + 1, table.left + 1)
    row = table.bottom + 2

    s.section(row, 'Data health (folded in from Pipeline Health)', 6)
    health_rows, warnings = data_health(ctx)
    table = s.table(row + 1, ['Item', 'Value', 'Detail'], health_rows, ['text', 'text', 'wrap'],
                    widths={'Item': 40, 'Value': 30, 'Detail': 70}, bold_first=True)
    s.highlight(table.column_range('Value'), 'bad', 'contains', 'exhausted')
    s.highlight(table.column_range('Value'), 'warn', 'contains', 'older than')
    s.highlight(table.column_range('Value'), 'warn', 'contains', 'WARNINGS')
    s.highlight(table.column_range('Value'), 'good', 'begins', 'VERIFIED')
    row = table.bottom + 2
    s.section(row, 'Warnings', 6)
    table = s.table(row + 1, ['Source', 'Warning'], warnings, ['text', 'wrap'], empty='none recorded',
                    widths={'Source': 40, 'Warning': 100})
    row = table.bottom + 2
    training = []
    for league, info in sorted((ctx.health.get('training') or {}).items()):
        state = (info.get('current_source_health') or info.get('forecast_training_health') or {}).get('status')
        training.append([league, value_or(info.get('training_end'), 'not recorded'),
                         value_or(info.get('days_since_latest_result'), 'not recorded', 'int'),
                         int(xb.number(info.get('training_matches')))
                         if xb.number(info.get('training_matches')) is not None else 'not recorded',
                         str(state).replace('_', ' ').lower() if state else 'not recorded'])
    s.section(row, 'Training data freshness', 6)
    table = s.table(row + 1, ['League', 'Latest result', 'Days since result', 'Training matches', 'Source status'],
                    training, ['text', 'text', 'int', 'int', 'text'], empty='no health report yet')
    s.highlight(table.column_range('Source status'), 'warn', 'contains', 'stale')
    s.highlight(table.column_range('Source status'), 'bad', 'contains', 'unavailable')
    row = table.bottom + 2
    s.section(row, 'Model activity: refits, stale fits, rollback checks and switches', 6)
    table = s.table(row + 1, ['Item', 'Status', 'Detail'], activity_summary(ctx), ['text', 'text', 'wrap'],
                    widths={'Item': 40, 'Status': 30, 'Detail': 70}, bold_first=True)
    status_rules(s, table.column_range('Status'))
    activity_rules(s, table.column_range('Status'))
    for name, offset in (('last_c6_refit', 1), ('last_ce3n_refit', 2), ('stale_fit_warning', 3),
                         ('switch_settings', 8), ('last_switch_change', 9)):
        book.define(name, s, table.top + offset, table.left + 1)
    s.note(table.bottom + 1, 'From model_activity/activity_log.jsonl (every event is in the Model Activity sheet); '
                             'release statuses from the live switches, as in Rollback status above.', 6)
    row = table.bottom + 3
    s.section(row, 'Sheets', 6)
    for i, name in enumerate(SHEETS[1:]):
        s.link(row + 1 + i // 3, 1 + i % 3, name, name)
    s.freeze = (2, 0)


def master_rollback_status(rollback: dict) -> str:
    """The release's rollback status as the review recorded it (price_edge_tracking.master_rollback)."""
    if not rollback:
        return 'not recorded (no review yet)'
    status = str(rollback.get('status') or '')
    if rollback.get('triggered'):
        return 'ROLLBACK TRIGGERED'
    if status == 'WAITING':
        return (f"Waiting: {rollback.get('min_graded_matches', 150)} graded matches over "
                f"{rollback.get('min_weeks', 3)} weeks on each list")
    if status == 'NOT TRIGGERED':
        return 'not triggered'
    return status or 'not recorded'


def switch_text(key: str) -> str:
    spec = RELEASES[key]
    value, problem = switch(key)
    return problem if value is None else f"{config_path(key).name} {'.'.join(spec['path'])} = \"{value}\""


def log_figures(figures: Optional[dict], key: str, label: str) -> str:
    """'N graded matches over W weeks; <difference>; 95% interval ...' for a research rollback check."""
    if not figures:
        return 'no figures'
    diff = figures.get(key)
    return (f"{figures.get('matches', 0)} graded matches over {figures.get('weeks', 0)} weeks; "
            f"{label} log loss "
            f"{'not computed yet' if xb.number(diff) is None else f'{float(diff):+.5f}'}; 95% interval "
            f"{interval_text(figures.get('interval_95'), 'log')}.")


def monitoring_checks(ctx: Context) -> List[List[str]]:
    rollback = ctx.tracking.get('master_rollback') or {}
    incidents = ctx.tracking.get('master_release_incidents') or {}
    favourites = (ctx.research.get('home_favourites') or {}).get('all') or {}
    v5, why_v5 = research_figures(ctx.root, 'v5')
    ce3n, why_ce3n = research_figures(ctx.root, 'v6')
    failed = (incidents.get('new_master_failed') or {}).get('runs', 0)
    missing = (incidents.get('baseline_missing') or {}).get('runs', 0)
    return [
        ['New master vs old master (flat return per bet)', master_status(ctx.root, rollback),
         rollback.get('message') or 'The review has not recorded the rollback check yet.'],
        ['Release incidents', 'none' if not (failed or missing) else
         f'NEW MASTER FAILED in {failed} runs; BASELINE MISSING in {missing} runs',
         '; '.join(incidents.get('messages') or []) or 'No run published the old master in place of the new one, '
                                                       'and every run kept its old-master shadow.'],
        ['Research v5 vs v4 (AH log loss, domestic)', release_status(ctx.root, 'v5'),
         log_figures(v5, 'v5_minus_v4_log_loss', 'v5 − v4') if v5 else why_v5],
        ['Home favourites (Eredivisie, Primeira Liga, Süper Lig)',
         f"{favourites.get('graded', 0)} graded of {favourites.get('picks', 0)} picks",
         'Value picks backing a v5 home favourite in the three holdout leagues; see Model Monitoring.'],
        ['CE3n vs CE (research v6, UCL/UEL)', release_status(ctx.root, 'v6'),
         log_figures(ce3n, 'ce3n_minus_ce_log_loss', 'CE3n − CE') if ce3n else why_ce3n],
    ]


def data_health(ctx: Context) -> Tuple[List[List[Any]], List[List[str]]]:
    rows: List[List[Any]] = []
    freshness = ctx.health.get('forecast_freshness') or {}
    age = xb.number(freshness.get('age_hours'))
    rows.append(['Last forecast generated', xb.eat_text(freshness.get('generated_at_utc')),
                 (f'{age:.0f} hours before the review; ' if age is not None else '')
                 + f"{freshness.get('upcoming_fixture_count', 'unknown')} upcoming fixtures; status "
                 + str(freshness.get('status') or 'not recorded').replace('_', ' ').lower()])
    try:
        records, balances = usage(ctx.root)
    except Exception:  # noqa: BLE001  (display only)
        records, balances = [], {}
    forecasts = [r for r in records if (xb.number(r.get('forecast_rows')) or 0) > 0]
    rows.append(['Last run that produced forecasts', xb.eat_text(forecasts[-1].get('recorded_at_utc'))
                 if forecasts else 'none in the usage log',
                 f"{forecasts[-1].get('workflow', 'workflow not recorded')}: {int(forecasts[-1]['forecast_rows'])} "
                 'forecast rows' if forecasts else 'odds_api_usage/usage_log.jsonl'])
    if records:
        last = records[-1]
        rows.append(['Last forecast workflow run', xb.eat_text(last.get('recorded_at_utc')),
                     f"{last.get('outcome') or 'outcome not recorded'}: {last.get('message') or 'no message'}"])
    else:
        rows.append(['Last forecast workflow run', 'none in the usage log', 'odds_api_usage/usage_log.jsonl'])
    if balances:
        total = sum(int(v['remaining']) for v in balances.values())
        detail = '; '.join(f"{slot}: {v['remaining']} left ({xb.eat_text(v.get('observed_at_utc'))})"
                           for slot, v in sorted(balances.items()))
        exhausted = bool(records and records[-1].get('all_keys_exhausted'))
        rows.append(['Odds API credits left', f'{total}' + (' (all keys exhausted)' if exhausted else ''), detail])
    else:
        rows.append(['Odds API credits left', 'not recorded', 'No usage log entry with key balances yet.'])
    workflow = load(ctx.root, 'workflow_health.json')
    rows.append(['Last report validation', str(workflow.get('status') or 'not recorded'),
                 f"workflow_checks.py reports, {xb.eat_text(workflow.get('reviewed_at_utc'))}"])
    errors = ctx.metrics.get('provider_errors') or {}
    rows.append(['Result provider', 'errors recorded' if errors else 'no errors',
                 '; '.join(f'{k}: {v}' for k, v in sorted(errors.items())) or 'football-data.org results verified'])
    warnings = [['Last report validation', str(w)] for w in workflow.get('warnings') or []]
    warnings += [['Master release', str(m)] for m in (ctx.tracking.get('master_release_incidents') or {}).get('messages') or []]
    return rows, warnings


def picks_sheet(book: xb.Book, ctx: Context) -> None:
    s = book.sheet('Picks & Results', xb.NAVY)
    s.title('Every pick on both master lists since the start, with its result',
            ctx.subtitle('Returns are for a 1-unit stake at the Pinnacle price; refunds and half results settle as '
                         'graded.'), span=10)
    rows = []
    for p in ctx.picks:
        rows.append([xb.excel_time(p['kickoff']) if p['kickoff'] else 'not recorded', p['match'], ctx.names[p['list']],
                     p['league'], p['bet'] or 'not recorded', value_or(p['price'], 'no Pinnacle quote'), p['tier'],
                     value_or(p['p_no_loss'], 'not recorded'), value_or(p['p_profit'], 'not recorded'),
                     '; '.join(p['labels'] + p['flags']) or 'none',
                     p['score'] or 'not graded yet', outcome(p), value_or(p['profit'], 'not graded yet'),
                     value_or(p['clv'], 'no near-kickoff quote'), 'yes' if p['in_other'] else 'no'])
    headers = ['Kickoff (EAT)', 'Match', 'List', 'League', 'Bet', 'Price', 'Tier', 'Predicted no-loss',
               'Chance of profit', 'Labels and flags', 'Score', 'Result', 'Return (units)', 'CLV',
               'Also on the other list']
    kinds = ['datetime', 'text', 'text', 'text', 'text', 'odds', 'text', 'pct', 'pct', 'wrap', 'text', 'text', 'units',
             'signed_pct', 'text']
    table = s.table(4, headers, rows, kinds, freeze_columns=2,
                    empty=ctx.empty('picks'),
                    widths={'Labels and flags': 34, 'Match': 32})
    result_rules(s, table, 'Result', ['Return (units)', 'CLV'])
    tier_rules(s, table.column_range('Tier'))
    label_rules(s, table.column_range('Labels and flags'))
    nav(s, table.bottom + 2)


def weekly(book: xb.Book, ctx: Context) -> None:
    s = book.sheet('Weekly Trends', xb.NAVY)
    s.title('Weekly results by kickoff week (ISO week, UTC kickoff as the rollback check counts it)',
            ctx.subtitle('Graded picks and returns per week, and cumulative return since the start.'), span=10)
    weeks = sorted({p['week'] for p in ctx.picks if p['profit'] is not None})
    rows, running = [], {'new': 0.0, 'old': 0.0}
    for week in weeks:
        line = [week]
        for which in ('new', 'old'):
            st = stats([p for p in ctx.by_list[which] if p['week'] == week])
            running[which] += st['return'] or 0.0
            line += [st['graded'], value_or(st['return'], 0.0) if st['graded'] else 0.0, running[which],
                     value_or(st['no_loss_rate'], NO_GRADED)]
        rows.append(line)
    n, o = ctx.names['new'], ctx.names['old']
    headers = ['Week', f'{n}: graded', f'{n}: return (units)', f'{n}: cumulative (units)', f'{n}: no-loss rate',
               f'{o}: graded', f'{o}: return (units)', f'{o}: cumulative (units)', f'{o}: no-loss rate']
    table = s.table(4, headers, rows, ['text', 'int', 'units', 'units', 'pct', 'int', 'units', 'units', 'pct'],
                    freeze_columns=1, empty=ctx.empty('graded weeks'))
    money_rules(s, table, [h for h in headers if 'units' in h])
    first, last = table.top + 1, table.bottom
    anchor_row = table.bottom + 2
    s.chart(xb.Chart('line', 'Cumulative return (units, 1-unit stakes)', (1, first, last),
                     [(n, table.columns[headers[3]]), (o, table.columns[headers[7]])],
                     (0, anchor_row, 6, anchor_row + 18), '0.00'))
    s.chart(xb.Chart('bar', 'Graded picks per week', (1, first, last),
                     [(n, table.columns[headers[1]]), (o, table.columns[headers[5]])],
                     (6, anchor_row, 12, anchor_row + 18), '0'))
    nav(s, anchor_row + 20)


def breakdowns(book: xb.Book, ctx: Context) -> None:
    s = book.sheet('Breakdowns', xb.NAVY)
    s.title('Results by league, market, tier, labels and flags',
            ctx.subtitle('Graded picks only for rates and returns; a pick can carry several labels.'), span=10)
    rows = []
    dims = (('League', lambda p: [p['league']]), ('Market', lambda p: [p['market']]),
            ('Tier', lambda p: [p['tier']]), ('Labels and flags',
                                              lambda p: p['labels'] + p['flags'] + (['also on the other list']
                                                                                     if p['in_other'] else []) or ['none']))
    for dim, groups_of in dims:
        for which in ('new', 'old'):
            groups: Dict[str, List[dict]] = {}
            for p in ctx.by_list[which]:
                for g in groups_of(p):
                    groups.setdefault(g, []).append(p)
            for group in sorted(groups):
                st = stats(groups[group])
                rows.append([dim, group, ctx.names[which], st['picks'], st['graded'],
                             value_or(st['win_rate'], NO_GRADED), value_or(st['no_loss_rate'], NO_GRADED),
                             value_or(st['return'], NO_GRADED), value_or(st['per_bet'], NO_GRADED),
                             value_or(st['odds'], NO_GRADED)])
    table = s.table(4, ['Breakdown', 'Group', 'List', 'Picks', 'Graded', 'Win rate', 'No-loss rate', 'Return (units)',
                        'Return per bet', 'Average odds'], rows,
                    ['text', 'text', 'text', 'int', 'int', 'pct', 'pct', 'units', 'signed_pct', 'odds'],
                    freeze_columns=2, empty=ctx.empty('picks'))
    money_rules(s, table, ['Return (units)', 'Return per bet'])
    label_rules(s, table.column_range('Group'))
    tier_rules(s, table.column_range('Group'))
    nav(s, table.bottom + 2)


def calibration(book: xb.Book, ctx: Context) -> None:
    s = book.sheet('Calibration', xb.NAVY)
    s.title('Predicted vs actual no-loss rate, by predicted band',
            ctx.subtitle('Predicted no-loss: the new master\'s ranking (market) no-loss chance and the old master\'s '
                         'no-loss probability, both frozen before kickoff. Actual: win, half win or refund.'), span=8)
    rows = []
    for which in ('new', 'old'):
        for lo, hi in BANDS:
            part = [p for p in ctx.by_list[which] if p['profit'] is not None and p['p_no_loss'] is not None
                    and lo <= p['p_no_loss'] < hi]
            n = len(part)
            mean = sum(p['p_no_loss'] for p in part) / n if n else None
            actual = sum(p['profit'] >= -1e-12 for p in part) / n if n else None
            gap = (actual - mean) * 100 if n else None
            reading = ('no graded picks' if not n else f'small sample (under {SMALL})' if n < SMALL else
                       'within 5 points' if abs(gap) <= 5 else
                       'actual lower than predicted' if gap < 0 else 'actual higher than predicted')
            rows.append([ctx.names[which], f'{lo:.0%}–{min(hi, 1):.0%}', n, value_or(mean, NO_GRADED),
                         value_or(actual, NO_GRADED), value_or(gap, NO_GRADED), reading])
    table = s.table(4, ['List', 'Predicted no-loss band', 'Graded picks', 'Mean predicted no-loss',
                        'Actual no-loss rate', 'Actual minus predicted (points)', 'Reading'], rows,
                    ['text', 'text', 'int', 'pct', 'pct', 'points', 'text'], freeze_columns=2)
    s.highlight(table.column_range('Reading'), 'bad', 'equals', 'actual lower than predicted')
    s.highlight(table.column_range('Reading'), 'good', 'equals', 'within 5 points')
    s.highlight(table.column_range('Reading'), 'muted', 'begins', 'small sample')
    nav(s, table.bottom + 2)


def clv_reading(n, t):
    """Descriptive reading gated on independent fixture count."""
    if not n or n < 30:
        return 'Small sample'
    if t is not None and t >= 2:
        return 'Positive (t >= 2)'
    if t is not None and t <= -2:
        return 'Negative (t <= -2)'
    return 'Not distinguishable from zero'


def clv_sheet(book: xb.Book, ctx: Context) -> None:
    s = book.sheet('CLV', xb.NAVY)
    s.title('Closing-line value: entry price vs Pinnacle\'s near-kickoff fair price',
            ctx.subtitle('CLV = entry odds × Pinnacle near-kickoff fair probability − 1. Near-kickoff feed quotes are '
                         'not guaranteed official closes; descriptive, not proof of an edge.',
                         PICKS_CSV + '; candidate CLV: performance/clv_report/*.csv'), span=10)
    row = 4
    s.section(row, 'Master picks since the start', 10)
    rows = []
    for which in ('new', 'old'):
        tiers = (('all tiers', ctx.by_list[which]),) + tuple(
            (t, [p for p in ctx.by_list[which] if p['tier'] == t]) for t in (TIERS if which == 'new' else ()))
        for tier, part in tiers:
            st = stats(part)
            rows.append([ctx.names[which], tier, st['picks'], st['clv_n'],
                         value_or(st['clv'], 'no near-kickoff quote yet'),
                         value_or(st['clv_positive'], 'no near-kickoff quote yet'),
                         'Small sample' if st['clv_n'] < SMALL else 'Descriptive only'])
    table = s.table(row + 1, ['List', 'Tier', 'Picks', 'Picks with a near-kickoff quote', 'Mean CLV',
                              'Positive share', 'Reading'], rows,
                    ['text', 'text', 'int', 'int', 'signed_pct', 'pct', 'text'], freeze_columns=1)
    money_rules(s, table, ['Mean CLV'])
    tier_rules(s, table.column_range('Tier'))
    row = table.bottom + 2
    summary = load(ctx.root, 'clv_report/summary.json')
    s.section(row, 'All priced candidates (shortlisted or not), from the candidate CLV report', 10)
    if summary.get('status') != 'OK':
        s.note(row + 1, 'No candidate CLV report yet: it is written by the daily performance review (clv_report.py).',
               10, 'warn')
        row += 3
    else:
        rows = []
        for label, scope, key in (('CLV vs Pinnacle fair close', 'All candidates', 'overall_pinnacle_fair'),
                                  ('CLV vs Pinnacle fair close', 'Shortlisted picks', 'shortlisted_pinnacle_fair'),
                                  ('Same-book price CLV', 'Where the entry book was quoted', 'overall_same_book')):
            st = summary.get(key) or {}
            rows.append([label, scope, value_or(st.get('n'), 0), value_or(st.get('independent_fixtures'), 0),
                         value_or(st.get('mean'), 'no quotes'), value_or(st.get('positive_share'), 'no quotes'),
                         value_or(st.get('t_stat'), 'not computed'),
                         clv_reading(st.get('independent_fixtures'), st.get('t_stat'))])
        table = s.table(row + 1, ['Measure', 'Scope', 'Candidates', 'Fixtures', 'Mean CLV', 'Positive share', 't',
                                  'Reading'], rows,
                        ['text', 'text', 'int', 'int', 'signed_pct', 'pct', 'odds', 'text'])
        reading_rules(s, table)
        row = table.bottom + 2
        folder = ctx.root / 'performance' / 'clv_report'
        for name, filename, keys in (('By market and entry bookmaker', 'by_market_bookmaker.csv',
                                      ['market_family', 'entry_bookmaker']),
                                     ('By league', 'by_league.csv', ['league'])):
            records = read_rows(folder / filename)
            if not records:
                continue
            records.sort(key=lambda r: -(xb.number(r.get('pinnacle_fair_n')) or 0))
            rows = []
            for r in records:
                n = int(xb.number(r.get('pinnacle_fair_n')) or 0)
                fixtures = int(xb.number(r.get('fixtures')) or 0)
                t = xb.number(r.get('pinnacle_fair_t_stat'))
                rows.append([' / '.join(str(r.get(k) or 'not recorded') for k in keys), n, fixtures,
                             value_or(xb.number(r.get('pinnacle_fair_mean')), 'no quotes'),
                             value_or(xb.number(r.get('pinnacle_fair_positive_share')), 'no quotes'),
                             value_or(t, 'not computed'), clv_reading(fixtures, t)])
            s.section(row, name, 10)
            table = s.table(row + 1, ['Group', 'Candidates', 'Fixtures', 'Mean CLV', 'Positive share', 't', 'Reading'],
                            rows, ['text', 'int', 'int', 'signed_pct', 'pct', 'odds', 'text'])
            reading_rules(s, table)
            row = table.bottom + 2
    nav(s, row)


def reading_rules(sheet: xb.Sheet, table: xb.Table) -> None:
    ref = table.column_range('Reading')
    sheet.highlight(ref, 'good', 'begins', 'Positive')
    sheet.highlight(ref, 'bad', 'begins', 'Negative')
    sheet.highlight(ref, 'muted', 'equals', 'Small sample')
    money_rules(sheet, table, ['Mean CLV'])


def coverage_text(figures: dict) -> str:
    return '; '.join(f'{k}: {v}' for k, v in sorted((figures.get('coverage') or {}).items())) or 'no graded matches yet'


def slopes_text(calibration: Optional[dict]) -> str:
    calibration = calibration or {}
    parts = []
    for name, slopes in sorted((calibration.get('slopes') or {}).items()):
        shown = [f"{side} {float(slopes[side]):.2f}" for side in ('home', 'away') if xb.number(slopes.get(side)) is not None]
        parts.append(f"{name}: {', '.join(shown) if shown else 'not computed yet'}")
    graded = calibration.get('graded_matches', 0)
    return (f"{'; '.join(parts) or 'not computed yet'} ({graded} graded matches; reported, not a trigger)")


def competition_text(part: dict) -> str:
    diff = part.get('ce3n_minus_ce_log_loss')
    return (f"{part.get('matches', 0)} graded matches over {part.get('weeks', 0)} weeks; CE3n − CE "
            f"{'not computed yet' if xb.number(diff) is None else f'{float(diff):+.5f}'}; 95% interval "
            f"{interval_text(part.get('interval_95'), 'log')}; calibration {slopes_text(part.get('calibration'))}"
            + ('. WARNING: interval entirely above zero before the pooled trigger is eligible' if part.get('warning')
               else ''))


def ucl_check_text(check: Optional[dict]) -> str:
    if not check:
        return 'not recorded'
    passed = check.get('passed_on') or {}
    if check.get('status') == 'passed' and passed:
        return f"passed on the run of {xb.eat_text(passed.get('generated_at_utc'))} ({passed.get('ucl_fixtures')} UCL fixtures)"
    return str(check.get('status') or 'not recorded')


def monitoring(book: xb.Book, ctx: Context) -> None:
    s = book.sheet('Model Monitoring', xb.NAVY)
    s.title('Model monitoring: the new master\'s rollback rule, research v5 vs v4, CE3n vs CE, home favourites',
            f'Run {ctx.run}. From performance/price_edge_v27/summary.json and performance/research_v5_monitoring.json '
            '(written by price_edge_tracking.py and research_monitoring.py); the weekly report shows the same checks. '
            'Nothing here switches anything automatically: Paul decides.', span=4)
    row = 4
    rollback = ctx.tracking.get('master_rollback') or {}
    checks = monitoring_checks(ctx)
    s.section(row, 'New master vs old master: rollback rule', 4)
    nm, om = rollback.get('new_master') or {}, rollback.get('old_master') or {}
    live, recorded = live_list(ctx.root), rollback.get('live_master_list') or ctx.tracking.get('live_master_list')
    rows = [['Status', checks[0][1]],
            ['Release switch', switch_text('master')],
            ['Live list', ctx.names[live] + ('' if recorded in (None, live) else
                                             f' (the last review ran with the {recorded} master live; the next '
                                             'review re-runs the rollback check)')],
            ['New master graded matches / weeks', f"{nm.get('graded_matches', 0)} / {nm.get('weeks', 0)}"],
            ['Old master graded matches / weeks', f"{om.get('graded_matches', 0)} / {om.get('weeks', 0)}"],
            ['Minimum on each list', f"{rollback.get('min_graded_matches', 150)} matches over "
                                     f"{rollback.get('min_weeks', 3)} weeks"],
            ['New − old return per bet', value_or(xb.number(rollback.get('difference')), 'not computed yet',
                                                  'signed_pct')],
            ['95% interval (weeks resampled)', interval_text(rollback.get('interval_95'))],
            ['Release incidents', checks[1][1]],
            ['Rule', rollback.get('rule') or 'not recorded (no review yet)']]
    table = s.table(row + 1, ['Item', 'Value'], rows, ['text', 'wrap'], widths={'Item': 38, 'Value': 100},
                    bold_first=True)
    status_rules(s, f'{xb.address(table.top + 1, table.left + 1)}:{xb.address(table.top + 1, table.left + 1)}')
    s.note(table.bottom + 1, 'The graded counts here are the rollback rule\'s own (every graded pick under the '
                             'released rule); the other sheets start at the first run after the release.', 4)
    row = table.bottom + 3

    s.section(row, 'Research v5 (C6) vs v4: rollback trigger (domestic leagues)', 4)
    research, why = research_figures(ctx.root, 'v5')
    rows = [['Status', checks[2][1]], ['Release switch', switch_text('v5')]]
    if research is None:
        rows.append(['Why no figures', why])
    else:
        diff = research.get('v5_minus_v4_log_loss')
        rows += [['Graded matches / weeks', f"{research.get('matches', 0)} / {research.get('weeks', 0)}"],
                 ['v5 − v4 research log loss (AH all lines)',
                  value_or(xb.number(diff), 'not computed yet', 'signed_decimal')],
                 ['95% interval (weeks resampled)', interval_text(research.get('interval_95'), 'log')],
                 ['Coverage', coverage_text(research)],
                 ['Rule', research.get('rule') or 'not recorded']]
    table = s.table(row + 1, ['Item', 'Value'], rows, ['text', 'wrap'], widths={'Item': 38, 'Value': 100},
                    bold_first=True)
    status_rules(s, f'{xb.address(table.top + 1, table.left + 1)}:{xb.address(table.top + 1, table.left + 1)}')
    book.define('research_v5_status', s, table.top + 1, table.left + 1)
    row = table.bottom + 2

    s.section(row, 'CE3n vs CE (research v6, UCL/UEL): rollback trigger', 4)
    ce3n, why = research_figures(ctx.root, 'v6')
    rows = [['Status', checks[4][1]], ['Release switch', switch_text('v6')]]
    if ce3n is None:
        rows.append(['Why no figures', why])
    else:
        diff = ce3n.get('ce3n_minus_ce_log_loss')
        means = ce3n.get('log_loss') or {}
        rows += [['Graded matches / weeks (UCL and UEL pooled)', f"{ce3n.get('matches', 0)} / {ce3n.get('weeks', 0)}"],
                 ['CE3n − CE research log loss (AH all lines)',
                  value_or(xb.number(diff), 'not computed yet', 'signed_decimal')],
                 ['95% interval (weeks resampled)', interval_text(ce3n.get('interval_95'), 'log')],
                 ['Mean log loss', ', '.join(f'{k} {float(v):.5f}' for k, v in sorted(means.items())
                                             if xb.number(v) is not None) or 'not computed yet'],
                 ['Calibration slopes (1 = calibrated)', slopes_text(ce3n.get('calibration'))]]
        for code, part in sorted((ce3n.get('by_competition') or {}).items()):
            rows.append([code, competition_text(part)])
        rows += [['UCL live check', ucl_check_text(ctx.research.get('ucl_live_check'))],
                 ['Coverage', coverage_text(ce3n)],
                 ['Rule', ce3n.get('rule') or 'not recorded']]
    table = s.table(row + 1, ['Item', 'Value'], rows, ['text', 'wrap'], widths={'Item': 38, 'Value': 100},
                    bold_first=True)
    status_rules(s, f'{xb.address(table.top + 1, table.left + 1)}:{xb.address(table.top + 1, table.left + 1)}')
    s.highlight(table.column_range('Value'), 'warn', 'contains_case', 'WARNING')
    book.define('ce3n_status', s, table.top + 1, table.left + 1)
    row = table.bottom + 2

    favourites = ctx.research.get('home_favourites') or {}
    s.section(row, 'Home favourites in Eredivisie, Primeira Liga and Süper Lig (v5 value picks)', 4)
    pct = lambda v: value_or(xb.number(v), 'no graded picks')
    rows = [[name, part.get('fixtures', 0), part.get('picks', 0), part.get('graded', 0),
             pct(part.get('v5_predicted_home_win')), pct(part.get('v4_predicted_home_win')),
             pct(part.get('actual_home_win'))]
            for name, part in [*sorted((favourites.get('by_league') or {}).items()), ('All three', favourites.get('all') or {})]]
    table = s.table(row + 1, ['League', 'Matches', 'Picks', 'Graded', 'v5 predicted home win', 'v4 on the same forecasts',
                              'Actual home win'], rows, ['text', 'int', 'int', 'int', 'pct', 'pct', 'pct'],
                    bold_first=False)
    s.note(table.bottom + 1, 'C6 was too confident on these leagues\' home sides in the holdout (home slope 0.79). '
                             'Latest pre-kickoff value-shortlist pick per match.', 7)
    row = ce3n_competitions(book, s, ctx, table.bottom + 3)
    nav(s, row)
    s.set_width(1, 38)


CE3N_WARNING = 'CE3n COMPETITION WARNING'


def competition_rows(ce3n: Optional[dict]) -> List[List[Any]]:
    """One row per competition (UCL, UEL) from research_monitoring's ce3n.by_competition (PR #178)."""
    rows = []
    parts = (ce3n or {}).get('by_competition') or {}
    for code in ('UCL', 'UEL'):
        part = parts.get(code)
        if part is None:
            rows.append([code] + ['not recorded'] * 9)
            continue
        slopes = (part.get('calibration') or {}).get('slopes') or {}

        def slope(name, side):
            return value_or(xb.number((slopes.get(name) or {}).get(side)), 'not computed yet')
        rows.append([code, int(part.get('matches') or 0), int(part.get('weeks') or 0),
                     value_or(xb.number(part.get('ce3n_minus_ce_log_loss')), 'not computed yet'),
                     interval_text(part.get('interval_95'), 'log'),
                     slope('CE3n', 'home'), slope('CE3n', 'away'), slope('CE', 'home'), slope('CE', 'away'),
                     f'{CE3N_WARNING} ({code})' if part.get('warning') else 'no warning'])
    return rows


def ucl_check_rows(check: Optional[dict]) -> List[List[str]]:
    if not check:
        return [['Status', 'not recorded (the review has not run the UCL live check yet)']]
    runs = check.get('runs') or []
    rows = [['Status', ucl_check_text(check)],
            ['Runs checked', f'{len(runs)} (every run with a UCL forecast under research v6, oldest first, until one '
                             'passes)' if runs else 'none yet (no UCL forecast under research v6)'],
            ['Check version', str(check.get('version') or 'not recorded')]]
    for run in runs[-5:]:
        problems = '; '.join(str(p) for p in (run.get('problems') or [])[:5])
        rows.append([f"Run of {xb.eat_text(run.get('generated_at_utc'))}",
                     f"{run.get('status')}: {run.get('ucl_fixtures')} UCL fixtures" + (f' ({problems})' if problems else '')])
    return rows


def ce3n_competitions(book: xb.Book, s: xb.Sheet, ctx: Context, row: int) -> int:
    """CE3n by competition, the competition warning and the UCL live check (PR #178); returns the next free row."""
    ce3n, why = research_figures(ctx.root, 'v6')
    s.section(row, 'CE3n vs CE by competition (research v6): UCL and UEL', 4)
    table = s.table(row + 1, ['Competition', 'Graded matches', 'Weeks', 'CE3n − CE log loss (AH all)', '95% interval',
                              'CE3n home slope', 'CE3n away slope', 'CE home slope', 'CE away slope', 'Warning'],
                    competition_rows(ce3n), ['text', 'int', 'int', 'signed_decimal', 'text', 'decimal', 'decimal',
                                             'decimal', 'decimal', 'text'], bold_first=True,
                    widths={'Competition': 38, 'Warning': 34})
    s.highlight(table.column_range('Warning'), 'bad', 'contains_case', CE3N_WARNING)
    s.highlight(table.column_range('Warning'), 'good', 'equals', 'no warning')
    s.note(table.bottom + 1, ('Log loss difference positive = CE3n worse. A competition whose interval is entirely '
                              'above zero before the pooled trigger is eligible gets the CE3n COMPETITION WARNING: a '
                              'warning, not a rollback. Slopes: 1 is calibrated, below 1 too sharp (reported, not a '
                              'trigger).') if ce3n is not None else f'No CE3n figures: {why}.', 10)
    row = table.bottom + 3
    warned = [c for c, part in sorted(((ce3n or {}).get('by_competition') or {}).items()) if part.get('warning')]
    s.section(row, 'CE3n competition warning and UCL live check', 4)
    rows = [['CE3n competition warning', ', '.join(f'{CE3N_WARNING} ({c})' for c in warned) if warned else
             ('none' if ce3n is not None else f'not recorded ({why})')]]
    rows += [['UCL live check' if k == 'Status' else f'UCL live check: {k}', v]
             for k, v in ucl_check_rows(ctx.research.get('ucl_live_check'))]
    table = s.table(row + 1, ['Item', 'Value'], rows, ['text', 'wrap'], widths={'Item': 38, 'Value': 100},
                    bold_first=True)
    s.highlight(table.column_range('Value'), 'bad', 'contains_case', CE3N_WARNING)
    s.highlight(table.column_range('Value'), 'bad', 'begins', 'failed')
    s.highlight(table.column_range('Value'), 'good', 'begins', 'passed')
    s.highlight(table.column_range('Value'), 'warn', 'begins', 'pending')
    book.define('ce3n_competition_warning', s, table.top + 1, table.left + 1)
    book.define('ucl_live_check_status', s, table.top + 2, table.left + 1)
    return table.bottom + 2


# --- model activity ----------------------------------------------------------------------------------------------

def activity_rules(sheet: xb.Sheet, ref: str) -> None:
    """Red: rollback triggered, competition warnings, failures; amber: stale fits (and skipped refits); green:
    releases and published refits."""
    for text in ('ROLLBACK TRIGGERED', 'COMPETITION WARNING', 'FAILED', 'MISSING'):
        sheet.highlight(ref, 'bad', 'contains_case', text)
    sheet.highlight(ref, 'warn', 'contains_case', 'STALE FIT WARNING STARTED')
    sheet.highlight(ref, 'warn', 'begins', 'ACTIVE')
    sheet.highlight(ref, 'warn', 'begins', 'SKIPPED')
    sheet.highlight(ref, 'good', 'begins', 'RELEASED')
    sheet.highlight(ref, 'good', 'begins', 'PUBLISHED')


def activity_rows(events: Sequence[dict]) -> List[List[Any]]:
    """The log newest first (same instant: later in the file first): Date (EAT), Event, Model or list, Outcome or
    status, Details."""
    ordered = sorted(enumerate(events), key=lambda item: (item[1].get('recorded_at_utc') or '', item[0]), reverse=True)
    rows = []
    for _, e in ordered:
        when = xb.parse_utc(e.get('recorded_at_utc'))
        details = str(e.get('details') or '')
        if e.get('backfilled'):
            details = 'Backfilled from git history. ' + details
        rows.append([xb.excel_time(when) if when else 'not recorded', str(e.get('event') or ''),
                     str(e.get('model') or ''), str(e.get('outcome') or ''), details])
    return rows


def activity_sheet(book: xb.Book, ctx: Context) -> None:
    s = book.sheet('Model Activity', xb.NAVY)
    s.title('Model activity: releases, refits, stale fits, rollback checks, switch changes and master fallbacks',
            f'Run {ctx.run}. Newest first, from model_activity/activity_log.jsonl (append-only; written by the refit '
            'workflow, each forecast run, the weekly report and the backfill of earlier releases). Times are '
            f'{xb.EAT_LABEL}. Use the filters to pick an event, model or outcome.', span=5)
    table = s.table(4, ['Date (EAT)', 'Event', 'Model or list', 'Outcome or status', 'Details'],
                    activity_rows(ctx.activity), ['datetime_year', 'text', 'text', 'text', 'wrap'], freeze_columns=1,
                    empty='No model activity recorded yet (model_activity/activity_log.jsonl is empty or missing).',
                    widths={'Date (EAT)': 22, 'Event': 24, 'Model or list': 34, 'Outcome or status': 36,
                            'Details': 100})
    activity_rules(s, table.column_range('Outcome or status'))
    book.define('latest_activity', s, table.top + 1, table.left + 3)
    nav(s, table.bottom + 2)


def activity_summary(ctx: Context) -> List[List[str]]:
    """The Dashboard's model-activity rows."""
    import model_activity as ma
    events = ctx.activity
    rows = []
    for fit, label in (('C6', 'Last C6 refit (research v5 live fit)'),
                       ('CE3n', 'Last CE3n refit (research v6 live fit)')):
        item = latest_activity(events, f'refit:{fit}')
        rows.append([label, str(item.get('outcome')) if item else 'none recorded',
                     f"{xb.eat_text(item.get('recorded_at_utc'))}: {item.get('details')}" if item else
                     'No refit in the activity log yet.'])
    active = []
    for fit in ('C6', 'CE3n'):
        item = latest_activity(events, f'stale:{fit}')
        if item and item.get('outcome') == ma.STALE_STARTED:
            active.append((fit, item))
    rows.append(['Stale-fit warning', 'ACTIVE: ' + ', '.join(f for f, _ in active) if active else 'none active',
                 ' '.join(f"{fit} since {xb.eat_text(i.get('recorded_at_utc'))}: {i.get('details')}" for fit, i in active)
                 or 'No forecast run is using a stale C6 or CE3n fit.'])
    checks = monitoring_checks(ctx)
    for label, key, status in (('New master rollback status', 'rollback:master', checks[0][1]),
                               ('Research v5 rollback status', 'rollback:v5', checks[2][1]),
                               ('Research v6 (CE3n) rollback status', 'rollback:v6', checks[4][1])):
        item = latest_activity(events, key)
        rows.append([label, status, f"Last rollback check logged {xb.eat_text(item.get('recorded_at_utc'))}: "
                                    f"{item.get('outcome')}." if item else 'No rollback check logged yet.'])
    ce3n, _ = research_figures(ctx.root, 'v6')
    warned = [c for c, part in sorted(((ce3n or {}).get('by_competition') or {}).items()) if part.get('warning')]
    rows.append(['CE3n competition warnings (UCL, UEL)',
                 ', '.join(f'{CE3N_WARNING} ({c})' for c in warned) if warned else 'none',
                 'Per-competition CE3n − CE check; see Model Monitoring.'])
    state = ma.switch_state(config_path('master'), config_path('v6'))
    rows.append(['Switch settings', ma.switch_settings_text(state),
                 'master_shortlist_config.json live; research_config.json live.domestic and live.european (read when '
                 'the workbook is built).'])
    change = latest_activity(events, 'switches')
    rows.append(['Last switch change', xb.eat_text(change.get('recorded_at_utc')) if change else 'none recorded',
                 f"{change.get('outcome')}: {change.get('details')}" if change else 'No switch change in the log.'])
    return rows


def guide(book: xb.Book, ctx: Context) -> None:
    s = book.sheet('Guide', xb.NAVY)
    s.title('Guide: what each measure means', f'Run {ctx.run}. One line per measure; times are {xb.EAT_LABEL}.',
            span=3)
    rows = [
        ['Master tracking start', 'The first forecast run after the new master went live; earlier picks are not shown.'],
        ['New master / old master', 'The live list (new rule since 14 Nov 2026) and the old rule kept in shadow for comparison.'],
        ['Tier', 'New master step: safe (no-loss ≥75%), fill (≥50%, ranked by chance of profit), risky fill (labelled).'],
        ['Graded', 'Picks whose match finished and whose result was verified; the rest are "not graded yet".'],
        ['Win rate', 'Full or half wins divided by graded picks.'],
        ['No-loss rate', 'Wins, half wins and refunds (no money lost) divided by graded picks.'],
        ['Return (units)', 'Profit of a 1-unit stake on every graded pick at the Pinnacle price.'],
        ['Return per bet', 'Return divided by graded picks (flat-stake ROI).'],
        ['Average odds', 'Mean Pinnacle price of the graded picks.'],
        ['Predicted no-loss', 'The list\'s own no-loss chance, frozen before kickoff (new: market ranking chance).'],
        ['Chance of profit', 'The list\'s own chance that the bet ends in profit, frozen before kickoff.'],
        ['Labels and flags', 'Research view labels (e.g. research strongly disagrees, unvalidated view) and list overlap; they never reorder bets.'],
        ['CLV', 'Entry odds × Pinnacle near-kickoff fair probability − 1; positive means the price was better than near-kickoff.'],
        ['Calibration gap', 'Actual no-loss rate minus mean predicted no-loss, in percentage points.'],
        ['Rollback rule', 'After 150 graded matches over 3 weeks on each list, new − old return per bet; triggered if the 95% interval is below zero.'],
        ['Research v5 rollback', 'Triggered if v5 − v4 research log loss on AH lines has a 95% interval above zero after 150 matches and 3 weeks.'],
        ['Release status', 'Read from each release\'s live switch when the workbook is built (master_shortlist_config.json live; research_config.json live.domestic and live.european): Live, or Rolled back with the date of the first run after the switch.'],
        ['CE3n vs CE', 'Research v6 (UCL/UEL) monitoring: CE3n − CE research log loss on AH lines; rollback if its 95% interval is above zero after 150 European matches over 3 weeks.'],
        ['Small sample', f'Fewer than {SMALL} graded picks (or fixtures): read rates with care.'],
        ['not graded yet / not recorded', 'The input is missing or the match is not settled; never a zero.'],
        ['Model Activity', 'Every release, live-fit refit (C6, CE3n), stale-fit warning, rollback check, switch change and master fallback, newest first, from the append-only model_activity/activity_log.jsonl.'],
        ['CE3n competition warning', 'UCL or UEL alone: CE3n − CE log loss interval entirely above zero before the pooled trigger is eligible; a warning, not a rollback.'],
        ['UCL live check', 'Research v6 on the first UCL fixtures (competition, mapping, fit window, CE shadow, frozen replay, unvalidated view), until a run passes.'],
    ]
    table = s.table(4, ['Measure', 'What it means'], rows, ['text', 'wrap'], widths={'Measure': 30, 'What it means': 110},
                    bold_first=True, freeze_columns=1)
    nav(s, table.bottom + 2)


def build(root: Path, metrics: Optional[dict] = None, health: Optional[dict] = None) -> xb.Book:
    ctx = Context(root, metrics or {}, health)
    book = xb.Book()
    dashboard(book, ctx)
    picks_sheet(book, ctx)
    weekly(book, ctx)
    breakdowns(book, ctx)
    calibration(book, ctx)
    clv_sheet(book, ctx)
    monitoring(book, ctx)
    activity_sheet(book, ctx)
    guide(book, ctx)
    return book


def write(root: Path, destination: Path, metrics: Optional[dict] = None, health: Optional[dict] = None) -> Path:
    return build(root, metrics, health).save(destination, 'the performance review')
