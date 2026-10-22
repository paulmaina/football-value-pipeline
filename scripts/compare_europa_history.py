"""Offline comparison of entitled, single-season Europa League CSV exports.

Reported-score agreement is not regulation-time certification. Never writes
training data, downloads files, guesses aliases, or admits unmatched fixtures.
"""
import argparse
from collections import Counter, defaultdict
import csv
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import unicodedata


def normalize(value):
    return ' '.join(unicodedata.normalize('NFKC', value).casefold().split())


def alias_map(values):
    if not isinstance(values, dict) or not all(
            isinstance(k, str) and isinstance(v, str) for k, v in values.items()):
        raise ValueError('Aliases must be a JSON object mapping names to names')
    result = {}
    for source, target in values.items():
        key, value = normalize(source), normalize(target)
        if not key or not value or (key in result and result[key] != value):
            raise ValueError('Blank or conflicting team alias')
        result[key] = value
    # Require direct canonical mappings, so mapping order cannot affect joins.
    if any(v in result and result[v] != v for v in result.values()):
        raise ValueError('Aliases must point directly to canonical names')
    return result


def field(row, *names):
    for name in names:
        if isinstance(row.get(name), str) and row[name].strip():
            return row[name].strip()
    raise ValueError('Required field missing')


def load_export(path, provider, year, aliases):
    data = Path(path).read_bytes()
    reader = csv.DictReader(data.decode('utf-8-sig').splitlines())
    required = ({'Date', 'Home Team', 'Away Team', 'Result'} if provider == 'fixture_download'
                else {'timestamp', 'status', 'home_team_goal_count', 'away_team_goal_count'})
    headers = set(reader.fieldnames or [])
    if not required <= headers or (provider == 'footystats' and not (
            {'team_a_name', 'team_b_name'} <= headers or
            {'home_team_name', 'away_team_name'} <= headers)):
        raise ValueError(f'Unsupported {provider} CSV schema')
    records, rejected, skipped = defaultdict(list), Counter(), Counter()
    total = 0
    start = datetime(year, 7, 1, tzinfo=timezone.utc)
    end = datetime(year + 1, 7, 1, tzinfo=timezone.utc)
    for line, row in enumerate(reader, 2):
        total += 1
        if provider == 'footystats' and (row['status'] or '').strip().casefold() != 'complete':
            skipped['not_complete'] += 1
            continue
        try:
            if provider == 'fixture_download':
                dt = datetime.strptime(field(row, 'Date'), '%d/%m/%Y %H:%M').replace(tzinfo=timezone.utc)
                home, away = field(row, 'Home Team'), field(row, 'Away Team')
                score = field(row, 'Result')
                if not re.fullmatch(r'\d+\s*-\s*\d+', score):
                    raise ValueError('Invalid score')
                goals = tuple(int(x.strip()) for x in score.split('-'))
            else:
                stamp = field(row, 'timestamp')
                if not re.fullmatch(r'\d+', stamp):
                    raise ValueError('Invalid timestamp')
                dt = datetime.fromtimestamp(int(stamp), tz=timezone.utc)
                home = field(row, 'team_a_name', 'home_team_name')
                away = field(row, 'team_b_name', 'away_team_name')
                scores = [field(row, k) for k in ('home_team_goal_count', 'away_team_goal_count')]
                if not all(re.fullmatch(r'\d+', x) for x in scores):
                    raise ValueError('Invalid score')
                goals = tuple(map(int, scores))
            if not start <= dt < end:
                rejected['outside_season'] += 1
                continue
            home, away = (aliases.get(normalize(x), normalize(x)) for x in (home, away))
            if home == away:
                rejected['self_fixture'] += 1
                continue
            key = (dt.date().isoformat(), home, away)
            records[key].append({'line': line, 'kickoff': dt.isoformat(), 'score': goals})
        except (ValueError, OverflowError, OSError, TypeError):
            rejected['invalid_required_fields'] += 1
    return records, {'rows': total, 'sha256': hashlib.sha256(data).hexdigest(),
                     'rejected': dict(rejected), 'skipped': dict(skipped),
                     'duplicate_identity_groups': sum(len(v) > 1 for v in records.values())}


def compare(fixture_path, footy_path, year, aliases=None):
    aliases = alias_map(aliases or {})
    fd, fd_info = load_export(fixture_path, 'fixture_download', year, aliases)
    fs, fs_info = load_export(footy_path, 'footystats', year, aliases)
    # Any duplicate on either side quarantines that identity on both sides.
    ambiguous = {k for source in (fd, fs) for k, rows in source.items() if len(rows) != 1}
    overlap = (fd.keys() & fs.keys()) - ambiguous
    conflicts, time_differences = [], []
    for key in sorted(overlap):
        left, right = fd[key][0], fs[key][0]
        ref = {'fixture_download_line': left['line'], 'footystats_line': right['line']}
        if left['score'] != right['score']:
            conflicts.append(ref)
        if left['kickoff'] != right['kickoff']:
            time_differences.append(ref)
    return {
        'competition': 'UEFA Europa League', 'season_start_year': year,
        'scope_assumption': 'Inputs must each contain only Europa League for the specified season',
        'status': 'COMPARISON_ONLY_NOT_TRAINING_APPROVAL',
        'fixture_download': fd_info, 'footystats': fs_info,
        'matched_unique_identities': len(overlap),
        'reported_scores_agree': len(overlap) - len(conflicts),
        'score_conflicts': conflicts, 'kickoff_differences': time_differences,
        'ambiguous_identities_quarantined': len(ambiguous),
        'fixture_download_only_candidates': len((fd.keys() - fs.keys()) - ambiguous),
        'footystats_only_candidates': len((fs.keys() - fd.keys()) - ambiguous),
        'unmatched_meaning': 'Potential aliases, dates, scope differences or extra coverage; not verified additions',
        'regulation_time_verified': False,
        'training_rows_written': 0,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--fixture-download', required=True, type=Path)
    parser.add_argument('--footystats', required=True, type=Path)
    parser.add_argument('--season-start-year', required=True, type=int, choices=range(2000, 2100))
    parser.add_argument('--aliases', type=Path, help='JSON object: source display name to canonical name')
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args()
    if args.output.resolve() in {p.resolve() for p in
            (args.fixture_download, args.footystats, args.aliases) if p}:
        parser.error('Output must not overwrite an input')
    aliases = json.loads(args.aliases.read_text()) if args.aliases else {}
    result = compare(args.fixture_download, args.footystats, args.season_start_year, aliases)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')


if __name__ == '__main__':
    main()
