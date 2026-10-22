"""Offline Europa data reconciliation and predeclared experimental validation.

No production league registration, quote requests, shortlist entries or model
cache writes. Source files and row-level outputs stay outside the repository.
"""
import argparse
from collections import Counter, defaultdict
from datetime import datetime, timezone
from html.parser import HTMLParser
import hashlib
import json
from pathlib import Path
import re
import sys
import unicodedata

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))


def key(text):
    return ' '.join(''.join(c for c in unicodedata.normalize('NFKD', text.casefold())
                           if not unicodedata.combining(c)).split())


def team_resolver(aliases):
    table = {}
    for source, target in aliases.items():
        if key(source) in table and table[key(source)] != key(target):
            raise ValueError('Conflicting aliases')
        table[key(source)] = key(target)
    if any(v in table and table[v] != v for v in table.values()):
        raise ValueError('Alias chains are not allowed')
    return lambda name: table.get(key(name), key(name))


def pair_score(value):
    if not re.fullmatch(r'\d+\s*-\s*\d+', value):
        raise ValueError('Invalid score')
    result = tuple(int(x.strip()) for x in value.split('-'))
    if max(result) > 30:
        raise ValueError('Implausible score')
    return result


def parse_openfootball(text, year, resolve):
    """Interpret the explicit AET (regulation, half-time) notation only."""
    if not text.startswith(f'= UEFA Europa League {year}/{str(year+1)[-2:]}'):
        raise ValueError('Wrong competition/season header')
    expected = re.search(r'^# Matches\s+(\d+)', text, re.M)
    stage = date = None
    rows = []
    for line_no, line in enumerate(text.splitlines(), 1):
        if line.startswith('▪ '):
            stage = line[2:].strip()
        d = re.fullmatch(r'\s*(?:Mon|Tue|Wed|Thu|Fri|Sat|Sun) ([A-Z][a-z]{2}) (\d{1,2})(?: (\d{4}))?\s*', line)
        if d:
            month = datetime.strptime(d[1], '%b').month
            actual_year = year if month >= 7 else year + 1
            if d[3] and int(d[3]) != actual_year:
                raise ValueError('Date contradicts declared season')
            date = datetime(actual_year, month, int(d[2])).date().isoformat()
        m = re.fullmatch(r'\s*(?:\d{2}:\d{2}\s+)?(.+?)\s+\([A-Z]{3}\)\s+v\s+(.+?)\s+\([A-Z]{3}\)\s+(.+?)\s*', line)
        if not m:
            if ' v ' in line:
                raise ValueError(f'Unparsed match at line {line_no}')
            continue
        if not date or not stage:
            raise ValueError('Match lacks date/stage')
        score_text = m[3]
        if 'a.e.t.' in score_text:
            s = re.fullmatch(r'(?:(\d+-\d+) pen\. )?(\d+-\d+) a\.e\.t\. \((\d+-\d+), (\d+-\d+)\)', score_text)
            if not s:
                raise ValueError('Ambiguous extra-time notation')
            reported, regulation, halftime = (pair_score(s[i]) for i in (2, 3, 4))
            if any(h > r or r > f for h, r, f in zip(halftime, regulation, reported)):
                raise ValueError('Inconsistent period scores')
            duration = 'AET_PEN' if s[1] else 'AET'
        else:
            s = re.fullmatch(r'(\d+-\d+)(?: \((\d+-\d+)\))?', score_text)
            if not s:
                raise ValueError('Ambiguous regular score')
            regulation = reported = pair_score(s[1])
            duration = 'REGULAR'
        rows.append({'date': date, 'home': resolve(m[1]), 'away': resolve(m[2]),
                     'regulation': regulation, 'reported': reported, 'duration': duration,
                     'stage': stage, 'source_line': line_no})
    if not expected or len(rows) != int(expected[1]):
        raise ValueError('Parsed count does not match header')
    require_unique(rows)
    return rows


def identity(row):
    return row['date'], row['home'], row['away']


def require_unique(rows):
    ids = [identity(x) for x in rows]
    if len(ids) != len(set(ids)) or any(x['home'] == x['away'] for x in rows):
        raise ValueError('Duplicate or self fixture')


def fixture_rows(path, year, resolve):
    import csv
    result = []
    for row in csv.DictReader(Path(path).read_text(encoding='utf-8-sig').splitlines()):
        if not row['Result'].strip():
            continue
        date = datetime.strptime(row['Date'], '%d/%m/%Y %H:%M').date()
        if not datetime(year, 7, 1).date() <= date < datetime(year+1, 7, 1).date():
            raise ValueError('Fixture outside season')
        result.append({'date': date.isoformat(), 'home': resolve(row['Home Team']),
                       'away': resolve(row['Away Team']), 'reported': pair_score(row['Result']),
                       'stage': row['Round Number']})
    require_unique(result)
    return result


class MatchLinks(HTMLParser):
    def __init__(self):
        super().__init__()
        self.current = None
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            self.current = [dict(attrs).get('href', ''), '']

    def handle_data(self, data):
        if self.current is not None:
            self.current[1] += data

    def handle_endtag(self, tag):
        if tag == 'a' and self.current is not None:
            self.links.append(self.current)
            self.current = None


def uefa_scores(html, resolve):
    parser = MatchLinks()
    parser.feed(html)
    rows = []
    seen = set()
    for url, label in parser.links:
        match = re.search(r'/uefaeuropaleague/match/(\d+)', url)
        s = re.fullmatch(r'(.+?) (\d+)-(\d+) (.+?)(?: \((.*)\))?', label.strip().replace('\ufeff', ''))
        if not match or not s or match[1] in seen:
            continue
        seen.add(match[1])
        rows.append({'home': resolve(s[1]), 'away': resolve(s[4]),
                     'reported': (int(s[2]), int(s[3])), 'aet': 'aet' in (s[5] or '').lower(),
                     'match_id': match[1], 'url': url})
    return rows


def reconcile(source_dir, aliases, reviews):
    resolve = team_resolver(aliases)
    source_dir = Path(source_dir)
    history, evidence, corrections, identity_corrections = [], {}, [], []
    for year in (2022, 2023, 2024):
        of = parse_openfootball((source_dir/f'openfootball-{year}.txt').read_text(encoding='utf-8'), year, resolve)
        fd = fixture_rows(source_dir/f'fixture-{year}.csv', year, resolve)
        for row in fd:
            for review in reviews.get('_identity_reviews', []):
                if identity(row) == (review['date'], resolve(review['home']), resolve(review['wrong_away'])):
                    if list(row['reported']) != review['reported']:
                        raise ValueError('Identity correction no longer matches source score')
                    row['away'] = resolve(review['correct_away'])
                    identity_corrections.append(review)
        require_unique(fd)
        lookup = {identity(x): x for x in of}
        if set(lookup) != {identity(x) for x in fd}:
            raise ValueError(f'Unmatched historical identities in {year}')
        for row in fd:
            other = lookup[identity(row)]
            if row['reported'] != other['reported']:
                raise ValueError(f'Unresolved reported-score conflict in {year}')
            if row['reported'] != other['regulation']:
                corrections.append({'season': year, 'date': row['date'], 'home': row['home'],
                                    'away': row['away'], 'reported': row['reported'],
                                    'regulation': other['regulation'], 'evidence': 'OpenFootball explicit periods'})
            history.append({**other, 'season': year, 'source': 'OpenFootball, reconciled to Fixture Download'})
        evidence[str(year)] = {'rows': len(of), 'cross_source_agreements': len(fd),
                               'aet_matches': sum(x['duration'] != 'REGULAR' for x in of)}
    # UEFA article identifies AET matches; all such rows require a separately
    # reviewed official report. Pair matches are admitted only when unique.
    fd = fixture_rows(source_dir/'fixture-2025.csv', 2025, resolve)
    official = uefa_scores((source_dir/'uefa-2025.html').read_text(encoding='utf-8'), resolve)
    if len(fd) != 189 or len(official) != 189:
        raise ValueError('Incomplete 2025/26 season')
    if {x['match_id'] for x in official if x['aet']} != {k for k in reviews if k.isdigit()}:
        raise ValueError('UEFA extra-time flags differ from the reviewed match set')
    by_pair = defaultdict(list)
    for row in official:
        by_pair[(row['home'], row['away'])].append(row)
    for row in fd:
        matches = [x for x in by_pair[(row['home'], row['away'])] if x['reported'] == row['reported']]
        if len(matches) != 1:
            raise ValueError('Ambiguous or conflicting UEFA match identity')
        match = matches[0]
        review = reviews.get(match['match_id'])
        if match['aet']:
            if not review or tuple(review['reported']) != row['reported'] or review['date'] != row['date']:
                raise ValueError('Extra-time match lacks reviewed regulation score')
            regulation = tuple(review['regulation'])
            if any(r > f or r < 0 for r, f in zip(regulation, row['reported'])):
                raise ValueError('Invalid reviewed regulation score')
        else:
            regulation = row['reported']
        if regulation != row['reported']:
            corrections.append({'season': 2025, 'date': row['date'], 'home': row['home'],
                                'away': row['away'], 'reported': row['reported'],
                                'regulation': regulation, 'evidence': review['url']})
        history.append({**row, 'regulation': regulation, 'duration': 'AET_REVIEWED' if match['aet'] else 'REGULAR',
                        'season': 2025, 'source': match['url']})
    evidence['2025'] = {'rows': len(fd), 'uefa_reported_score_agreements': len(fd),
                         'aet_matches': sum(x['aet'] for x in official),
                         'identity_limit': 'UEFA date not parsed; unique home/away/reported-score links use Fixture Download dates'}
    require_unique(history)
    return sorted(history, key=identity), {'seasons': evidence, 'regulation_corrections': corrections,
                                          'identity_corrections': identity_corrections}


def audit_cornerflick(source_dir, resolve, now):
    source_dir = Path(source_dir)
    payload = json.loads((source_dir/'cornerflick.json').read_text(encoding='utf-8'))
    if payload.get('competition', {}).get('slug') != 'europa-league':
        raise ValueError('Wrong Cornerflick competition')
    if payload.get('meta', {}).get('match_count') != len(payload['matches']):
        raise ValueError('Cornerflick count does not reconcile')
    official = uefa_scores((source_dir/'uefa-2026.html').read_text(encoding='utf-8'), resolve)
    expected = fixture_rows(source_dir/'fixture-2026.csv', 2026, resolve)
    # Only labelled league-phase rows corroborated against both sources can
    # enter the final research fit, never the historical validation periods.
    rows, unknown_stage = [], 0
    for x in payload['matches']:
        if not re.fullmatch(r'League Stage - \d+', x.get('round') or ''):
            unknown_stage += 1
            continue
        stamp = datetime.fromisoformat(x['kickoff_at'])
        if stamp.tzinfo is None or stamp.astimezone(timezone.utc) >= now or x.get('status') != 'finished':
            raise ValueError('Invalid completed Cornerflick timestamp/status')
        score = (x.get('home_score'), x.get('away_score'))
        if any(type(g) is not int or not 0 <= g <= 30 for g in score):
            raise ValueError('Invalid Cornerflick score')
        rows.append({'date': stamp.astimezone(timezone.utc).date().isoformat(),
                     'home': resolve(x['home_team']), 'away': resolve(x['away_team']), 'reported': score})
    require_unique(rows)
    fd = {identity(x): x for x in expected}
    conflicts, unverified = [], []
    for row in rows:
        found = fd.get(identity(row))
        uefa = [x for x in official if x['home'] == row['home'] and x['away'] == row['away']]
        if not found or len(uefa) != 1:
            unverified.append(identity(row))
        elif row['reported'] != found['reported'] or row['reported'] != uefa[0]['reported']:
            conflicts.append(identity(row))
    return {'total_rows': len(payload['matches']), 'declared_rows': payload['meta'].get('match_count'),
            'league_phase_rows': len(rows), 'unclassified_rows_quarantined': unknown_stage,
            'score_conflicts': conflicts, 'unverified_identities': unverified,
            'fixture_download_completed_rows': len(expected), 'uefa_completed_links': len(official),
            'missing_against_fixture_download': len(set(fd) - {identity(x) for x in rows}),
            'latest_result': max((x['date'] for x in rows), default=None),
            'last_updated_at': payload['meta'].get('last_updated_at'),
            'upstream': payload['meta'].get('source'),
            'verified_for_research': bool(rows) and not conflicts and not unverified and
                                     set(fd) == {identity(x) for x in rows},
            'production_eligible': False,
            'eligibility': 'CORROBORATED_LEAGUE_PHASE_ONLY; refresh SLA and knockout semantics unverified'}, rows


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-dir', required=True, type=Path)
    parser.add_argument('--output-dir', required=True, type=Path)
    parser.add_argument('--train', action='store_true')
    args = parser.parse_args()
    if args.output_dir.resolve().is_relative_to(ROOT) or args.source_dir.resolve() == args.output_dir.resolve():
        parser.error('Output must be outside the repository and separate from source inputs')
    aliases = json.loads((ROOT/'docs/audits/europa-team-aliases.json').read_text(encoding='utf-8'))
    reviews = json.loads((ROOT/'docs/audits/europa-regulation-reviews.json').read_text(encoding='utf-8'))
    history, report = reconcile(args.source_dir, aliases, reviews)
    report['cornerflick'], current = audit_cornerflick(args.source_dir, team_resolver(aliases), datetime.now(timezone.utc))
    report['inputs'] = {p.name: hashlib.sha256(p.read_bytes()).hexdigest()
                        for p in sorted(args.source_dir.iterdir()) if p.is_file()}
    report['production_enabled'] = False
    args.output_dir.mkdir(parents=True, exist_ok=True)
    (args.output_dir/'history.json').write_text(json.dumps(history, indent=2)+'\n')
    if args.train:
        from scripts.europa_validation import validate
        verified_current = current if report['cornerflick']['verified_for_research'] else []
        report['experiment'] = validate(history, verified_current, args.output_dir)
    (args.output_dir/'report.json').write_text(json.dumps(report, indent=2, allow_nan=False)+'\n')
    print(json.dumps({k: v for k, v in report.items() if k != 'inputs'}, indent=2))


if __name__ == '__main__':
    main()
