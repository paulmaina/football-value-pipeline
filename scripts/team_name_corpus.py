"""Collect every team name the repo knows (tests/team_name_corpus.json, 23 Nov 2026) and list the characters
normalize_team_name's NFKD step cannot decompose.

Sources: the reviewed alias files, TEAM_ALIASES and HISTORY_ALIASES, the CE3n fit files' European names and
identities, and the team columns of every CSV under .football_cache (feature models excluded) and
football_output_v2. Usage: python scripts/team_name_corpus.py tests/team_name_corpus.json
"""
import csv
import glob
import json
import sys
import unicodedata
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
csv.field_size_limit(10**9)

names = set()


def add(x):
    if isinstance(x, str) and x.strip():
        names.add(x.strip())


def walk(obj):
    if isinstance(obj, dict):
        for k, v in obj.items():
            add(k)
            walk(v)
    elif isinstance(obj, (list, tuple)):
        for v in obj:
            walk(v)
    else:
        add(obj)


for f in ['bbs_team_aliases.json', 'odds_provider_team_aliases.json', 'docs/audits/europa-team-aliases.json']:
    walk(json.loads(Path(f).read_text(encoding='utf-8')))
for f in ['research_ce3n_live_fits.json', 'research_ce3n_fits.json']:
    d = json.loads(Path(f).read_text(encoding='utf-8'))
    walk(d.get('european_names'))
    walk(d.get('identities'))
import football_value_pipeline_v2_standalone as p
import team_research as tr
walk(p.TEAM_ALIASES)
walk(tr.HISTORY_ALIASES)
cols = ('HomeTeam', 'AwayTeam', 'home_team', 'away_team', 'Home', 'Away', 'home', 'away', 'Home team', 'Away team')
files = [f for f in glob.glob('.football_cache/**/*.csv', recursive=True) if 'feature_models' not in f]
files += glob.glob('football_output_v2/**/*.csv', recursive=True)
for f in files:
    try:
        with open(f, encoding='utf-8', errors='replace', newline='') as h:
            r = csv.DictReader(h)
            use = [c for c in (r.fieldnames or []) if c in cols]
            if not use:
                continue
            for row in r:
                for c in use:
                    add(row.get(c))
    except Exception as e:  # noqa
        print('skip', f, e, file=sys.stderr)
names = {n for n in names if len(n) < 60 and not n.replace('.', '').isdigit()}
dropped = Counter()
for n in names:
    s = unicodedata.normalize('NFKD', n)
    for ch in s:
        if not unicodedata.combining(ch) and ord(ch) > 127:
            dropped[ch] += 1
print(len(names), 'names from', len(files), 'csv files', file=sys.stderr)
print({f'{c} U+{ord(c):04X} {unicodedata.name(c, "?")}': k for c, k in dropped.most_common()}, file=sys.stderr)
out = Path(sys.argv[1])
out.write_text(json.dumps(sorted(names), ensure_ascii=False, indent=0), encoding='utf-8')
