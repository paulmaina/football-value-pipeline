"""Check that team_research.prepare() output is unchanged against a git ref, on every frozen forecast.

For each row of each snapshot under <root>/performance/snapshots, both versions of
prepare() get the same inputs: the frozen row, the research observation time and the
frozen pre-kickoff evidence (without the keys enrich()/prepare() derive). Rows without
research get the "not collected" fallback at the snapshot's generation time, as
profit_shortlist.context() does. The full research contexts must be byte-identical
as sorted JSON. Exit code 1 if any row differs.

    python scripts/check_research_unchanged.py --base main
"""
from __future__ import annotations

import argparse
import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import warnings

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO))
DERIVED_EVIDENCE = ('quality_review', 'rest_and_travel')


def load_base(ref: str, folder: Path):
    source = subprocess.run(['git', '-C', str(REPO), 'show', f'{ref}:team_research.py'],
                            check=True, capture_output=True, text=True, encoding='utf-8').stdout
    path = folder / 'team_research_base.py'
    path.write_text(source, encoding='utf-8')
    spec = importlib.util.spec_from_file_location('team_research_base', path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def frozen_inputs(meta, row, tr):
    research = tr.decode(row.get('team_research_json'))
    if research:
        evidence = research.get('evidence', {})
        for key in DERIVED_EVIDENCE:
            evidence.pop(key, None)
        return tr.utc(research['observed_at_utc']), evidence
    return tr.utc(meta['generated_at_utc']), {'errors': ['research not collected for this forecast']}


def compare(base, root: Path) -> dict:
    import performance_tracking as pt
    import team_research as current
    counts = {'rows': 0, 'with_research': 0, 'identical': 0, 'different': 0}
    examples = []
    for meta, rows, _ in pt.snapshots(root):
        for row in rows:
            cutoff, evidence = frozen_inputs(meta, row, current)
            outputs = [json.dumps(module.prepare(row, cutoff, copy.deepcopy(evidence)), sort_keys=True, default=str)
                       for module in (base, current)]
            counts['rows'] += 1
            counts['with_research'] += bool(current.decode(row.get('team_research_json')))
            same = outputs[0] == outputs[1]
            counts['identical' if same else 'different'] += 1
            if not same and len(examples) < 5:
                examples.append({'snapshot': meta.get('generated_at_utc'), 'league': row.get('league'),
                                 'home_team': row.get('home_team'), 'away_team': row.get('away_team')})
    return {**counts, 'examples': examples}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('--base', default='main', help='git ref holding the reference team_research.py')
    parser.add_argument('--root', type=Path, default=REPO / 'football_output_v2')
    args = parser.parse_args(argv)
    with tempfile.TemporaryDirectory() as tmp, warnings.catch_warnings():
        warnings.simplefilter('ignore')
        result = compare(load_base(args.base, Path(tmp)), args.root)
    print(json.dumps({'base': args.base, **result}, indent=2))
    return 0 if result['different'] == 0 and result['rows'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
