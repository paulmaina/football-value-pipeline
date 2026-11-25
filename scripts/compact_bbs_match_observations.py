"""Compact BBS match observations: keep the first observation of each state, drop repeats.

One-off clean-up (25 Nov 2026). The collector used to store every listing of every match, three times a
day: 166,412 files for 1,896 matches, almost all differing only in their retrieval time and request
metadata. For each match, in observation order, an observation is kept when its state
(bbs_data.match_state: everything except the volatile fields) differs from the last kept one, or when a
quarantine of that match falls at or after the last kept observation (the next listing is what lifted
the hold). That is the rule the collector now applies before storing a listing
(bbs_data.match_observation_needed), so the latest observation at any cutoff keeps the same state and
the same quarantine outcome as before.

    python scripts/compact_bbs_match_observations.py                # report only
    python scripts/compact_bbs_match_observations.py --apply        # delete the repeats
"""
from __future__ import annotations

import argparse
from collections import defaultdict
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from bbs_data import decode, match_observation_needed, utc  # noqa: E402


def plan(matches, quarantines):
    """The match observations to keep. matches, quarantines: iterables of (key, observation row)."""
    held = defaultdict(list)
    for _, row in quarantines:
        held[(row['league'], row['entity'])].append(utc(row['observed']))
    by_entity = defaultdict(list)
    for key, row in matches:
        by_entity[(row['league'], row['entity'])].append((utc(row['observed']), key, row))
    keep = set()
    for entity, rows in by_entity.items():
        previous = None
        for observed, key, row in sorted(rows, key=lambda x: (x[0], x[1])):
            quarantined = max((q for q in held.get(entity, ()) if q <= observed), default=None)
            if match_observation_needed(previous, row['payload'],
                                        None if quarantined is None else quarantined.isoformat()):
                keep.add(key)
                previous = row
    return keep


def load(folder):
    return [(path, decode(path.read_text(encoding='utf-8'))) for path in sorted(Path(folder).glob('*.json'))]


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('--store', type=Path, default=Path('.football_cache/bbs/state'))
    parser.add_argument('--apply', action='store_true', help='delete the repeated observations')
    args = parser.parse_args(argv)
    matches = load(args.store/'observations/match')
    keep = plan(matches, load(args.store/'observations/quarantine'))
    drop = [path for path, _ in matches if path not in keep]
    print(f'match observations: {len(matches)}; keep {len(keep)}; drop {len(drop)}')
    if args.apply:
        for path in drop:
            path.unlink()
        print(f'deleted {len(drop)} files')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
