"""European backfill: older UCL and UEL results for the evaluation harness only.

The raw files are in .football_cache/europa/backfill/ (scripts/fetch_european_backfill.py; manifest.json with
source URL, fetch time and sha256). The live pipeline never reads them: the live UCL loader reads only
fdorg_history_UCL_<year>.json and the live UEL loader only europa/training.json.

Seasons (each ends before the cached seasons start, so no backfilled match is on or after 21 Jan 2025):

  UCL 2015/16-2016/17  OpenFootball only (Fixture Download has no file): single-source seasons
  UCL 2017/18-2022/23  OpenFootball reconciled to Fixture Download (2022/23 closes the gap before the
                       cached football-data.org seasons, which start in 2023/24)
  UEL 2020/21-2021/22  OpenFootball reconciled to Fixture Download (OpenFootball has no older UEL file)
  UEL 2019/20          Fixture Download only: not admitted
  UCL/UEL earlier      no source

A result counts when OpenFootball and Fixture Download agree on the fixture (same teams, dates within a day)
and on the concluding score, or, in a single-source season, when OpenFootball reports it. The regulation
score comes from OpenFootball's explicit periods (extra time and penalties removed), the notation the reviewed
UEL reconciliation reads (scripts/europa_research.parse_openfootball). Awarded and cancelled matches are left
out. A conflict is never resolved here: the row is left out and reported.

Team names. UEL names resolve through the reviewed Europa resolver (docs/audits/europa-team-aliases.json) plus
the reviewed backfill aliases (docs/audits/european-backfill-aliases.json), toward the names the UEL snapshot
already uses. UCL names are put in the football-data.org spelling the live UCL loader uses, so a club is one
team across backfilled and cached seasons. Every backfill alias is confirmed by fixture evidence: every fixture
of the club in the two sources compared has the same side, a date within a day and the same score
(`derive_names`). No string comparison of any kind; only rows before 21 Jan 2025 are read for evidence.
"""
from __future__ import annotations

from collections import Counter, defaultdict
from datetime import date, datetime, timedelta
import csv
import json
from pathlib import Path
import re

import pandas as pd

ROOT = Path(__file__).resolve().parent
ALIASES = ROOT / 'docs' / 'audits' / 'european-backfill-aliases.json'
EUROPA_ALIASES = ROOT / 'docs' / 'audits' / 'europa-team-aliases.json'
LOCK_DATE = '2025-01-21'  # European holdout start: no backfilled row, and no evidence row, is on or after it
TITLES = {'UCL': 'UEFA Champions League', 'UEL': 'UEFA Europa League'}
CODES = {'UCL': 'cl', 'UEL': 'el'}
# competition -> season start year -> sources that report it
SEASONS = {
    'UCL': {**{y: ('openfootball',) for y in (2015, 2016)},
            **{y: ('openfootball', 'fixture_download') for y in range(2017, 2023)}},
    'UEL': {y: ('openfootball', 'fixture_download') for y in (2020, 2021)},
}
NOT_ADMITTED = {('UEL', 2019): 'Fixture Download only (OpenFootball has no UEL file before 2020/21): not admitted'}
EVIDENCE_SEASONS = (2023, 2024)  # UCL name evidence only, rows before LOCK_DATE
COLUMNS = ['Date', 'HomeTeam', 'AwayTeam', 'FTHG', 'FTAG', 'Season', 'stage']
WEEKDAYS = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
# football-data.org stage codes, so european_results.stage_group reads backfilled UCL stages as it reads live ones
UCL_STAGES = {'round of 16': 'LAST_16', 'quarterfinals': 'QUARTER_FINALS', 'semifinals': 'SEMI_FINALS',
              'final': 'FINAL'}


def folder(cache) -> Path:
    return Path(cache) / 'europa' / 'backfill'


def key(text):
    from scripts.europa_research import key as europa_key
    return europa_key(text)


# ---------------------------------------------------------------------------
# Parsing
# ---------------------------------------------------------------------------

def pair(text):
    a, b = (int(x) for x in text.split('-'))
    if max(a, b) > 30:
        raise ValueError('Implausible score')
    return a, b


def _season_date(month_name, day, explicit_year, weekday, year):
    """The date in the season starting `year` whose weekday matches the line. OpenFootball omits the year
    on most lines, and 2019/20 finished in August 2020, so the month alone cannot place a date."""
    month = datetime.strptime(month_name, '%b').month
    years = [explicit_year] if explicit_year else [year, year + 1]
    found = [date(y, month, day) for y in years
             if WEEKDAYS[date(y, month, day).weekday()] == weekday
             and date(year, 7, 1) <= date(y, month, day) < date(year + 1, 10, 1)]
    if len(found) != 1:
        raise ValueError(f'Cannot place {weekday} {month_name} {day} in season {year}')
    return found[0]


def parse_openfootball(text, competition, year):
    """Every match line of one OpenFootball season file: played rows and left-out rows (awarded, cancelled).

    Score notation (each form is explicit; anything else stops the parse):
      'a-b (h)' or 'a-b'                      regulation a-b
      'a-b a.e.t. (r, h)'                     concluding a-b after extra time, regulation r
      'p pen. a-b a.e.t. (r, h)'              the same, decided on penalties
      'p pen. 0-0 a.e.t. (0-0)'               goalless after extra time: regulation 0-0
      'a-b [awarded]', '[cancelled]'          left out (not a played result)"""
    header = f'= {TITLES[competition]} {year}/{str(year + 1)[-2:]}'
    if not text.startswith(header):
        raise ValueError(f'Wrong competition/season header: expected {header!r}')
    declared = re.search(r'^# Matches\s+(\d+)', text, re.M)
    stage = day = None
    rows, left_out = [], []
    for line_no, line in enumerate(text.splitlines(), 1):
        if line.startswith('▪ '):
            stage = line[2:].strip()
            continue
        d = re.fullmatch(r'\s*(Mon|Tue|Wed|Thu|Fri|Sat|Sun) ([A-Z][a-z]{2}) (\d{1,2})(?: (\d{4}))?\s*', line)
        if d:
            day = _season_date(d[2], int(d[3]), int(d[4]) if d[4] else None, d[1], year)
            continue
        m = re.fullmatch(r'\s*(?:\d{2}:\d{2}\s+)?(.+?)\s+\([A-Z]{3}\)\s+v\s+(.+?)\s+\([A-Z]{3}\)\s+(.+?)\s*', line)
        if not m:
            if ' v ' in line:
                raise ValueError(f'Unparsed match line {line_no}')
            continue
        if day is None or stage is None:
            raise ValueError(f'Match without date or stage at line {line_no}')
        base = {'date': day.isoformat(), 'home': m[1].strip(), 'away': m[2].strip(), 'stage': stage,
                'source_line': line_no}
        score = m[3]
        flag = re.fullmatch(r'(?:(\d+-\d+)\s+)?\[(awarded|cancelled)\]', score)
        if flag:
            left_out.append({**base, 'reason': flag[2], 'reported': pair(flag[1]) if flag[1] else None})
            continue
        s = re.fullmatch(r'(?:(\d+-\d+) pen\. )?(\d+-\d+) a\.e\.t\. \((\d+-\d+)(?:, (\d+-\d+))?\)', score)
        if s:
            reported = pair(s[2])
            if s[4] is None:
                if reported != (0, 0) or pair(s[3]) != (0, 0):
                    raise ValueError(f'Ambiguous extra-time notation at line {line_no}')
                regulation = (0, 0)
            else:
                regulation, half = pair(s[3]), pair(s[4])
                if any(h > r or r > f for h, r, f in zip(half, regulation, reported)):
                    raise ValueError(f'Inconsistent period scores at line {line_no}')
            duration = 'AET_PEN' if s[1] else 'AET'
        else:
            s = re.fullmatch(r'(\d+-\d+)(?: \((\d+-\d+)\))?', score)
            if not s:
                raise ValueError(f'Unknown score notation at line {line_no}: {score!r}')
            regulation = reported = pair(s[1])
            duration = 'REGULAR'
        rows.append({**base, 'reported': reported, 'regulation': regulation, 'duration': duration})
    if not declared or len(rows) + len(left_out) != int(declared[1]):
        raise ValueError(f'{competition} {year}: parsed {len(rows)} + {len(left_out)} rows, header declares '
                         f'{declared[1] if declared else None}')
    ids = [(r['date'], r['home'], r['away']) for r in rows]
    if len(ids) != len(set(ids)) or any(r['home'] == r['away'] for r in rows):
        raise ValueError('Duplicate or self fixture')
    return rows, left_out


def parse_fixture_download(text, year):
    """Played rows of one Fixture Download season file (UTC kick-off; the concluding score)."""
    rows = []
    for row in csv.DictReader(text.splitlines()):
        if not row['Result'].strip():
            continue
        kickoff = datetime.strptime(row['Date'], '%d/%m/%Y %H:%M')
        if not datetime(year, 7, 1) <= kickoff < datetime(year + 1, 10, 1):
            raise ValueError('Fixture outside season')
        rows.append({'kickoff_utc': kickoff, 'date': kickoff.date().isoformat(), 'home': row['Home Team'].strip(),
                     'away': row['Away Team'].strip(), 'reported': pair(row['Result'].replace(' ', '')),
                     'round': row['Round Number']})
    return rows


def read_text(path):
    return Path(path).read_bytes().decode('utf-8-sig')


def openfootball(cache, competition, year, evidence=False):
    path = folder(cache) / ('evidence' if evidence else '') / f'openfootball-{CODES[competition]}-{year}.txt'
    return parse_openfootball(read_text(path), competition, year)


def fixture_download(cache, competition, year, evidence=False):
    path = folder(cache) / ('evidence' if evidence else '') / f'fixture-{CODES[competition]}-{year}.csv'
    return parse_fixture_download(read_text(path), year)


# ---------------------------------------------------------------------------
# Names: fixture evidence only
# ---------------------------------------------------------------------------

def _near(a, b, days=1):
    return abs((date.fromisoformat(a) - date.fromisoformat(b)).days) <= days


def derive_names(left, right, score='reported', right_score=None):
    """Each name in `left` -> the one name in `right` that fixture evidence confirms.

    A left name maps to a right name when every fixture of the left name has a fixture in `right` on the
    same side, with a date within a day and the same score, involving that right name, and no other right
    name fits every fixture. The mapping must be one to one. No string comparison of any kind.
    Returns ({left: right}, {left: fixtures checked}, [left names with no unique match])."""
    right_score = right_score or score
    by_date = defaultdict(list)
    for r in right:
        by_date[r['date']].append(r)
    fixtures = defaultdict(list)
    for r in left:
        for side in ('home', 'away'):
            fixtures[r[side]].append((r, side))
    found, checked, unresolved = {}, {}, []
    for name, games in sorted(fixtures.items()):
        candidates = None
        for r, side in games:
            d = date.fromisoformat(r['date'])
            near = [x for k in (-1, 0, 1) for x in by_date.get((d + timedelta(days=k)).isoformat(), [])]
            fit = {x[side] for x in near if tuple(x[right_score]) == tuple(r[score])}
            candidates = fit if candidates is None else candidates & fit
        if candidates and len(candidates) == 1:
            found[name] = candidates.pop()
            checked[name] = len(games)
        else:
            unresolved.append(name)
    clash = sorted(t for t, n in Counter(found.values()).items() if n > 1)
    if clash:
        raise ValueError(f'Fixture evidence maps two names to one team: {clash}')
    return found, checked, unresolved


def before_lock(rows):
    """Name evidence reads only rows before the European holdout start."""
    return [r for r in rows if r['date'] < LOCK_DATE]


def load_aliases():
    return json.loads(ALIASES.read_text(encoding='utf-8'))


def europa_table():
    return json.loads(EUROPA_ALIASES.read_text(encoding='utf-8'))


def europa_resolver(extra=None):
    """The reviewed UEL resolver plus reviewed backfill aliases (same rules: no conflicts, no chains).
    A backfill alias may never override a reviewed Europa alias."""
    from scripts.europa_research import team_resolver
    table = europa_table()
    sources = {key(s) for s in table}
    for source, target in (extra or {}).items():
        if key(source) in sources:
            raise ValueError(f'Backfill alias {source!r} would override a reviewed Europa alias')
        table[source] = target
    return team_resolver(table)


def ucl_live_rows(cache):
    """football-data.org UCL rows before the European holdout start, as the live loader returns them."""
    import european_results as er
    frame = er.load(cache, 'UCL', LOCK_DATE)
    return [{'date': d.date().isoformat(), 'home': h, 'away': a, 'regulation': (int(x), int(y))}
            for d, h, a, x, y in zip(frame.Date, frame.HomeTeam, frame.AwayTeam, frame.FTHG, frame.FTAG)]


def _with_awarded(cache, competition, year):
    """OpenFootball rows for name evidence: played rows plus awarded rows with their awarded score
    (Fixture Download lists an awarded match as a result). Awarded rows are never admitted."""
    rows, left_out = openfootball(cache, competition, year)
    return rows + [r for r in left_out if r.get('reported') is not None]


def domestic_names(cache):
    """league -> (None, team names) over every football-data.co.uk file of the 8 leagues (cached seasons and
    the domestic backfill). Names only: no date or score is read."""
    import historical_benchmark as hb
    cfg = json.loads((ROOT / 'evaluation_harness_config.json').read_text(encoding='utf-8'))
    out = {}
    for league in cfg['leagues']:
        code, names = hb.CODES[league], set()
        paths = [Path(cache) / f'{s}_{code}.csv' for s in cfg['seasons']]
        paths += sorted((Path(cache) / 'domestic_backfill').glob(f'????_{code}.csv'))
        for path in paths:
            raw = path.read_bytes()
            try:
                text = raw.decode('utf-8-sig')
            except UnicodeDecodeError:
                text = raw.decode('latin1')
            for row in csv.DictReader(text.splitlines()):
                names |= {row[k].strip() for k in ('HomeTeam', 'AwayTeam') if (row.get(k) or '').strip()}
        out[league] = (None, names)
    return out


def ucl_names(cache):
    """Older OpenFootball UCL names -> football-data.org names (the live UCL loader's spelling).

    Within a season, names are tied by fixture evidence (derive_names). Across seasons no fixture is shared,
    so continuity always rests on a name; and no source spells clubs one way on both sides of 2022/23 ->
    2023/24: OpenFootball switches to football-data.org's spelling in 2023/24 ("Bayern München" ->
    "FC Bayern München") and Fixture Download changes spellings from year to year. Steps:
      1. OpenFootball 2023/24-2024/25 names are football-data.org names (fixture evidence maps each to itself);
      2. Fixture Download 2023/24-2024/25 name -> football-data.org name (fixture evidence);
      3. per season 2017/18-2022/23, Fixture Download name -> older OpenFootball name (fixture evidence).
    An older OpenFootball name is then linked to a football-data.org name by either reviewed bridge:
      a. the same exact Fixture Download spelling on both sides (steps 2 and 3); or
      b. both resolve to the same single domestic club through the reviewed research resolver
         (team_research.history_team via european_results.domestic_identities; never fuzzy). This uses names
         only, so it covers every cached football-data.org name; scores are read only before 21 Jan 2025.
    The bridges must agree where both apply, and the result must be one to one. A club with no link keeps
    its OpenFootball name (to the model, a different team from any football-data.org team): listed in the report."""
    import european_results as er
    live = ucl_live_rows(cache)
    of_new = before_lock([r for y in EVIDENCE_SEASONS for r in openfootball(cache, 'UCL', y, evidence=True)[0]])
    fd_new = before_lock([r for y in EVIDENCE_SEASONS for r in fixture_download(cache, 'UCL', y, evidence=True)])
    step1, checked1, unresolved1 = derive_names(of_new, live, score='regulation')
    renamed = {o: n for o, n in step1.items() if o != n}
    if renamed:
        raise ValueError(f'OpenFootball 2023/24-2024/25 names are not football-data.org names: {renamed}')
    report = {'openfootball_2023_2024_equals_football_data_org': {
        'names': len(step1), 'fixtures': sum(checked1.values()), 'unresolved': unresolved1}}
    new_spellings = defaultdict(set)
    for year in EVIDENCE_SEASONS:  # Fixture Download's spelling changes between seasons: one season at a time
        step2, checked2, unresolved2 = derive_names([r for r in fd_new if r['kickoff_utc'].year in (year, year + 1)
                                                     and datetime(year, 7, 1) <= r['kickoff_utc'] < datetime(year + 1, 7, 1)],
                                                    [r for r in of_new if f'{year}-07-01' <= r['date'] < f'{year + 1}-07-01'])
        report[f'fixture_download_{year}_to_football_data_org'] = {
            'names': len(step2), 'fixtures': sum(checked2.values()), 'unresolved': unresolved2}
        for f, n in step2.items():
            new_spellings[f].add(n)
    fd_to_of, old_spellings, old_names = {}, defaultdict(set), set()
    for year, sources in SEASONS['UCL'].items():
        rows = _with_awarded(cache, 'UCL', year)
        old_names |= {r[s] for r in rows for s in ('home', 'away')}
        if len(sources) == 1:
            continue
        found, checked, unresolved = derive_names(fixture_download(cache, 'UCL', year), rows)
        fd_to_of[str(year)] = {f: o for f, o in sorted(found.items()) if f != o}
        report[f'fixture_download_{year}_to_openfootball'] = {'names': len(found), 'fixtures': sum(checked.values()),
                                                               'unresolved': unresolved}
        for f, o in found.items():
            old_spellings[o].add(f)
    # Every football-data.org UCL name, by identity only (no score is read).
    frame = er.load(cache, 'UCL', pd.Timestamp.now(tz='UTC'))
    fdorg_names = set(frame.HomeTeam) | set(frame.AwayTeam)
    histories = domestic_names(cache)
    old_domestic, _ = er.domestic_identities(sorted(old_names), histories)
    new_domestic, _ = er.domestic_identities(sorted(fdorg_names), histories)
    by_domestic = defaultdict(set)
    for n, club in new_domestic.items():
        by_domestic[club].add(n)
    chain, how = {}, {}
    for o in sorted(old_names):
        via_fd = {n for f in old_spellings.get(o, ()) for n in new_spellings.get(f, ())}
        via_domestic = by_domestic.get(old_domestic[o], set()) if o in old_domestic else set()
        if len(via_fd) > 1 or len(via_domestic) > 1 or (via_fd and via_domestic and via_fd != via_domestic):
            raise ValueError(f'Contradictory links for {o!r}: Fixture Download {via_fd}, domestic {via_domestic}')
        target = next(iter(via_fd or via_domestic or {None}))
        if target is None:
            continue
        if o in fdorg_names and o != target:
            raise ValueError(f'{o!r} is a football-data.org name but links to {target!r}')
        how[o] = [b for b, s in (('fixture_download_spelling', via_fd), ('domestic_club', via_domestic)) if s]
        if o != target:
            chain[o] = target
    targets = Counter(chain.values()) + Counter(o for o in old_names if o in fdorg_names and o not in chain)
    clash = sorted(n for n, k in targets.items() if k > 1)
    if clash:
        raise ValueError(f'Two OpenFootball names link to one football-data.org name: {clash}')
    report['links'] = {'older_openfootball_names': len(old_names),
                       'same_spelling_as_football_data_org': sorted(o for o in old_names if o in fdorg_names),
                       'linked': {o: how[o] for o in sorted(chain)},
                       'not_linked': sorted(o for o in old_names if o not in chain and o not in fdorg_names)}
    return {'to_football_data_org': dict(sorted(chain.items())), 'fixture_download_to_openfootball': fd_to_of}, report


def uel_names(cache):
    """Backfill UEL aliases on top of the reviewed Europa resolver, toward the names the snapshot uses.

    Fixture evidence pairs each club's Fixture Download name f with its OpenFootball name o. Where the
    reviewed resolver already gives both the same name, nothing is added. Otherwise the alias gives the
    club the name it already has in the snapshot (europa/training.json); when neither name is in the
    snapshot, the club keeps OpenFootball's name (the admitted rows are OpenFootball's) and only the Fixture
    Download name is aliased, for matching. A reviewed alias is never overridden."""
    import european_results as er
    base = europa_resolver()
    table = {key(s) for s in europa_table()}
    snapshot = {r[s] for r in json.loads(er.europa_snapshot(cache).read_text(encoding='utf-8'))['matches']
                for s in ('home', 'away')}
    aliases, report = {}, {}
    for year in SEASONS['UEL']:
        found, checked, unresolved = derive_names(fixture_download(cache, 'UEL', year), _with_awarded(cache, 'UEL', year))
        report[f'fixture_download_{year}_to_openfootball'] = {'names': len(found), 'fixtures': sum(checked.values()),
                                                               'unresolved': unresolved}
        for f, o in sorted(found.items()):
            rf, ro = base(f), base(o)
            if rf == ro:
                continue
            if rf in snapshot and ro in snapshot:
                raise ValueError(f'The snapshot already holds {f!r} and {o!r} as two teams')
            options = [(f, ro), (o, rf)] if ro in snapshot or rf not in snapshot else [(o, rf), (f, ro)]
            options = [(s, t) for s, t in options if key(s) not in table]
            if not options:
                raise ValueError(f'Both {f!r} and {o!r} are reviewed Europa alias sources')
            source, target = options[0]
            if aliases.get(source, target) != target:
                raise ValueError(f'UEL alias {source!r} differs between seasons')
            aliases[source] = target
    return {'aliases': dict(sorted(aliases.items()))}, report


# ---------------------------------------------------------------------------
# Reconciliation
# ---------------------------------------------------------------------------

def _match_rows(of_rows, fd_rows, resolve_of, resolve_fd):
    """Pair OpenFootball and Fixture Download rows: same resolved teams, dates within a day; unique."""
    index = defaultdict(list)
    for r in fd_rows:
        index[(resolve_fd(r['home']), resolve_fd(r['away']))].append(r)
    pairs, of_only, used = [], [], set()
    for r in of_rows:
        hits = [x for x in index.get((resolve_of(r['home']), resolve_of(r['away'])), []) if _near(x['date'], r['date'])]
        if len(hits) > 1:
            raise ValueError(f"Ambiguous Fixture Download identity for {r['date']} {r['home']} v {r['away']}")
        if hits:
            used.add(id(hits[0]))
            pairs.append((r, hits[0]))
        else:
            of_only.append(r)
    return pairs, of_only, [x for x in fd_rows if id(x) not in used]


def reconcile(cache, aliases=None):
    """Every backfill season: the admitted rows and a per-season report. Raises on anything unparseable
    and on any row on or after the European holdout start."""
    aliases = load_aliases() if aliases is None else aliases
    resolve_uel = europa_resolver(aliases['UEL']['aliases'])
    to_fdorg = aliases['UCL']['to_football_data_org']
    fd_to_of = aliases['UCL']['fixture_download_to_openfootball']
    rows, report = [], []
    for competition, seasons in SEASONS.items():
        for year, sources in seasons.items():
            of_rows, left_out = openfootball(cache, competition, year)
            if competition == 'UEL':
                resolve_of = resolve_fd = name = resolve_uel
            else:
                resolve_of = lambda n: n
                resolve_fd = lambda n, t=fd_to_of.get(str(year), {}): t.get(n, n)
                name = lambda n: to_fdorg.get(n, n)
            entry = {'competition': competition, 'season': f'{year}/{str(year + 1)[-2:]}', 'sources': list(sources),
                     'openfootball_rows': len(of_rows),
                     'left_out_not_played': [{k: r[k] for k in ('date', 'home', 'away', 'reason')} for r in left_out]}
            if len(sources) == 1:
                admitted = [(r, None) for r in of_rows]
                entry.update(label='single source: OpenFootball only (no Fixture Download file exists for this season)',
                             fixture_download_rows=None, agreements=None, score_conflicts=[],
                             openfootball_only=[], fixture_download_only=[])
            else:
                fd_rows = fixture_download(cache, competition, year)
                pairs, of_only, fd_only = _match_rows(of_rows, fd_rows, resolve_of, resolve_fd)
                admitted = [(o, f) for o, f in pairs if tuple(o['reported']) == tuple(f['reported'])]
                conflicts = [(o, f) for o, f in pairs if tuple(o['reported']) != tuple(f['reported'])]
                awarded = {(resolve_of(r['home']), resolve_of(r['away'])) for r in left_out if r['reason'] == 'awarded'}
                entry.update(label='two sources agree: OpenFootball and Fixture Download',
                             fixture_download_rows=len(fd_rows), agreements=len(admitted),
                             score_conflicts=[{'date': o['date'], 'home': o['home'], 'away': o['away'],
                                               'openfootball': list(o['reported']), 'fixture_download': list(f['reported'])}
                                              for o, f in conflicts],
                             openfootball_only=[[r['date'], r['home'], r['away']] for r in of_only],
                             fixture_download_only=[[r['date'], r['home'], r['away'],
                                                     'awarded in OpenFootball (left out)'
                                                     if (resolve_fd(r['home']), resolve_fd(r['away'])) in awarded else
                                                     'no OpenFootball row'] for r in fd_only])
            season_rows = []
            for o, f in admitted:
                stage = o['stage']
                if competition == 'UCL':
                    stage = 'GROUP_STAGE' if stage.lower().startswith(('group', 'gruppe')) else UCL_STAGES[stage.lower()]
                stamp = pd.Timestamp(f['kickoff_utc']) if f is not None else pd.Timestamp(o['date'])
                season_rows.append({'competition': competition, 'Date': stamp, 'HomeTeam': name(o['home']),
                                    'AwayTeam': name(o['away']), 'FTHG': int(o['regulation'][0]),
                                    'FTAG': int(o['regulation'][1]), 'Season': str(year), 'stage': stage,
                                    'duration': o['duration'], 'source': entry['label']})
            entry['admitted'] = len(season_rows)
            entry['regulation_corrections'] = sum(r['duration'] != 'REGULAR' for r in season_rows)
            entry['first'] = min(r['Date'] for r in season_rows).date().isoformat()
            entry['last'] = max(r['Date'] for r in season_rows).date().isoformat()
            entry['stages'] = dict(Counter('group stage' if r['stage'] in ('GROUP_STAGE',) or
                                           r['stage'].lower().startswith(('group', 'gruppe')) else 'knockout'
                                           for r in season_rows))
            rows += season_rows
            report.append(entry)
    for (competition, year), reason in NOT_ADMITTED.items():
        report.append({'competition': competition, 'season': f'{year}/{str(year + 1)[-2:]}',
                       'sources': ['fixture_download'],
                       'fixture_download_rows': len(fixture_download(cache, competition, year)),
                       'admitted': 0, 'label': reason})
    frame = pd.DataFrame(rows)
    if (frame.Date >= pd.Timestamp(LOCK_DATE)).any():
        raise ValueError('A backfilled row is on or after the European holdout start')
    keys = list(zip(frame.competition, frame.Date.dt.date, frame.HomeTeam, frame.AwayTeam))
    if len(keys) != len(set(keys)) or (frame.HomeTeam == frame.AwayTeam).any():
        raise ValueError('Duplicate or self backfilled fixture')
    return frame, report


def results(cache, competition, aliases=None):
    """Admitted backfill rows for one competition, in COLUMNS order."""
    frame, _ = reconcile(cache, aliases)
    return frame.loc[frame.competition == competition, COLUMNS].reset_index(drop=True)


# ---------------------------------------------------------------------------
# The reviewed alias file (derived from fixture evidence, reviewed, committed; re-derived by the tests)
# ---------------------------------------------------------------------------

def build_aliases(cache):
    ucl, ucl_report = ucl_names(cache)
    uel, uel_report = uel_names(cache)
    return {'description': ('Reviewed team aliases for the European backfill (european_backfill.py). Every entry is '
                            'confirmed by fixture evidence: each fixture of the club in the two sources compared has '
                            'the same side, a date within a day and the same score; no string comparison of any kind. '
                            'Only rows before 21 Jan 2025 are read. Harness only: the live pipeline does not read this file.'),
            'UCL': {**ucl, 'evidence': ucl_report}, 'UEL': {**uel, 'evidence': uel_report}}


# ---------------------------------------------------------------------------
# European -> domestic aliases (European domestic-form coverage only)
# ---------------------------------------------------------------------------

DOMESTIC_ALIASES = ROOT / 'docs' / 'audits' / 'european-domestic-aliases.json'
# The nine reviewed-alias gaps PR #158 listed, as the European files spell them, and their league.
DOMESTIC_GAPS = {'SSC Napoli': 'SerieA', 'SS Lazio': 'SerieA', 'Bologna FC 1909': 'SerieA',
                 'Galatasaray SK': 'SuperLig', 'Fenerbahçe SK': 'SuperLig',
                 'Real Sociedad de Fútbol': 'LaLiga', 'Real Betis Balompié': 'LaLiga',
                 'frankfurt': 'Bundesliga', 'n.e.c.': 'Eredivisie'}
FOOTBALL_JSON_CODES = {'SerieA': 'it.1', 'LaLiga': 'es.1', 'Bundesliga': 'de.1', 'Eredivisie': 'nl.1'}
FIXTURE_DOWNLOAD_SLUGS = {'SerieA': 'serie-a', 'LaLiga': 'la-liga', 'Bundesliga': 'bundesliga',
                          'Eredivisie': 'eredivisie', 'SuperLig': 'super-lig'}


def _football_data_rows(cache, league, season):
    import historical_benchmark as hb
    raw =(Path(cache) / f'{season}_{hb.CODES[league]}.csv').read_bytes()
    try:
        text = raw.decode('utf-8-sig')
    except UnicodeDecodeError:
        text = raw.decode('latin1')
    rows = []
    for r in csv.DictReader(text.splitlines()):
        if not (r.get('FTHG') or '').strip():
            continue
        day = pd.to_datetime(r['Date'].strip(), dayfirst=True).date().isoformat()
        rows.append({'date': day, 'home': r['HomeTeam'].strip(), 'away': r['AwayTeam'].strip(),
                     'reported': (int(float(r['FTHG'])), int(float(r['FTAG'])))})
    return rows


def _domestic_sources(cache, league):
    """(source label, season start year, rows) of the domestic name evidence for one league."""
    out = []
    base = folder(cache) / 'evidence' / 'domestic'
    code = FOOTBALL_JSON_CODES.get(league)
    for year in (2023, 2024):
        if code:
            payload = json.loads((base / f'football-json-{year}-{code}.json').read_text(encoding='utf-8'))
            rows = [{'date': m['date'], 'home': m['team1'], 'away': m['team2'], 'reported': tuple(m['score']['ft'])}
                    for m in payload['matches'] if (m.get('score') or {}).get('ft')]
            out.append((f'OpenFootball football.json {year}/{str(year + 1)[-2:]} {code}', year, rows))
    rows = [{**r, 'date': r['date']} for r in parse_fixture_download(
        read_text(base / f'fixture-{FIXTURE_DOWNLOAD_SLUGS[league]}-2024.csv'), 2024)]
    out.append((f'Fixture Download {FIXTURE_DOWNLOAD_SLUGS[league]} 2024/25', 2024, rows))
    return out


def domestic_aliases(cache):
    """European name -> football-data.co.uk name for the nine gaps, confirmed by fixture evidence.

    A source that spells the club as the European files do (OpenFootball football.json: the football-data.org
    spelling of the UCL files; Fixture Download, read through the reviewed Europa resolver for UEL names) is
    compared with football-data.co.uk's league file of the same season: every fixture of the club must have a
    football-data.co.uk fixture on the same side, with a date within a day and the same score, and no other
    team may fit (derive_names). 2023/24-2024/25 only, before the domestic holdout. Every source that confirms
    the club must give the same domestic name. Never fuzzy."""
    resolve = europa_resolver()
    aliases, evidence = defaultdict(dict), {}
    for name, league in DOMESTIC_GAPS.items():
        found, notes = set(), []
        for label, year, rows in _domestic_sources(cache, league):
            target_rows = _football_data_rows(cache, league, f'{str(year)[-2:]}{str(year + 1)[-2:]}')
            names, checked, unresolved = derive_names(rows, target_rows)
            spellings = [s for s in names if s == name or resolve(s) == name]
            for s in spellings:
                found.add(names[s])
                notes.append({'source': label, 'spelled': s, 'domestic': names[s], 'fixtures_agreeing': checked[s]})
            if not spellings:
                notes.append({'source': label, 'spelled': None,
                              'note': 'no team in this source is spelled as the European files spell the club'})
        if len(found) > 1:
            raise ValueError(f'{name!r}: sources disagree on the domestic club {sorted(found)}')
        evidence[name] = {'league': league, 'sources': notes,
                          'alias': next(iter(found)) if found else None,
                          'result': 'confirmed by fixture evidence' if found else
                                    'not added: no source spells the club this way in domestic fixtures'}
        if found:
            aliases[league][name] = next(iter(found))
    return {'description': ('Reviewed European -> domestic aliases for the European domestic-form coverage only '
                            '(european_results.domestic_identities, after the research resolver). Each is confirmed by '
                            'fixture evidence: every domestic fixture of the club, in a source that spells it as the '
                            'European files do, matches football-data.co.uk on side, date within a day and score. '
                            'Never fuzzy. Not read by the live pipeline.'),
            'aliases': {k: dict(sorted(v.items())) for k, v in sorted(aliases.items())}, 'evidence': evidence}


def load_domestic_aliases():
    return json.loads(DOMESTIC_ALIASES.read_text(encoding='utf-8'))['aliases']


# ---------------------------------------------------------------------------
# Manual reviewed aliases (Phase 2c alias review; approved in PR review, not fixture evidence)
# ---------------------------------------------------------------------------

REVIEWED_ALIASES = ROOT / 'docs' / 'audits' / 'european-reviewed-aliases.json'
REVIEWED_STATUS = 'manual, approved by Paul in PR review'


def load_reviewed_aliases(path=REVIEWED_ALIASES):
    """{'ucl_names': {old: new}, 'domestic': {league: {European name: domestic name}}, 'applies_before': date}.

    Manual aliases for clubs that are plainly the same team but have no fixture evidence. They apply only to
    European matches before the European holdout start (LOCK_DATE), so no holdout row is renamed or relinked."""
    data = json.loads(Path(path).read_text(encoding='utf-8'))
    if data.get('status') != REVIEWED_STATUS or data.get('applies_before') != LOCK_DATE:
        raise ValueError('Reviewed aliases must be marked manual and apply only before the European holdout start')
    return {'ucl_names': {k: v['to'] for k, v in data['ucl_names']['aliases'].items()},
            'domestic': {league: {k: v['to'] for k, v in table.items()}
                         for league, table in data['domestic']['aliases'].items()},
            'applies_before': data['applies_before']}


def verify_aliases(cache, aliases=None):
    """Sections of the committed file that differ from what fixture evidence derives today (empty when sound)."""
    aliases = load_aliases() if aliases is None else aliases
    fresh = build_aliases(cache)
    return [f'{s}.{f}' for s, f in (('UCL', 'to_football_data_org'), ('UCL', 'fixture_download_to_openfootball'),
                                    ('UEL', 'aliases')) if aliases[s][f] != fresh[s][f]]


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Derive the backfill aliases, or print the reconciliation report')
    parser.add_argument('--cache', type=Path, default=ROOT / '.football_cache')
    parser.add_argument('--derive-aliases', type=Path, help='write freshly derived aliases here (for review)')
    parser.add_argument('--derive-domestic-aliases', type=Path, help='write freshly derived European -> domestic aliases here')
    args = parser.parse_args()
    if args.derive_domestic_aliases:
        args.derive_domestic_aliases.write_text(json.dumps(domestic_aliases(args.cache), indent=1, ensure_ascii=False)
                                                + '\n', encoding='utf-8')
    elif args.derive_aliases:
        args.derive_aliases.write_text(json.dumps(build_aliases(args.cache), indent=1, ensure_ascii=False) + '\n',
                                       encoding='utf-8')
    else:
        print(json.dumps(reconcile(args.cache)[1], indent=1, ensure_ascii=False, default=str))
