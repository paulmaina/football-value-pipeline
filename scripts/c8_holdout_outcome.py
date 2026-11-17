"""The declared outcome of C8's holdout test (evaluation/declarations/c8_holdout.json; docs/plan.md, Phase 2g).

Committed with the declaration, before the holdout was scored, so the reading of the result is fixed in
code beforehand. It reads the harness's own verdict (results.json, `holdout_verdict`) and computes nothing
from the matches:

    no_release               the sample minimum is not met, or the calibration rule fails, or either point
                             estimate (C6 minus C8 log loss on AH all lines, on the draw-sensitive lines)
                             is negative or exactly zero
    proven                   otherwise, and the AH all interval is clear of zero: release
    release_with_guardrails  otherwise: release with guardrails, as C6 was

Read in that order. A point estimate that is missing counts as not positive.

    python scripts/c8_holdout_outcome.py --results <holdout run>/results.json
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

DECLARATION = Path(__file__).resolve().parents[1] / 'evaluation' / 'declarations' / 'c8_holdout.json'
OUTCOMES = ('proven', 'release_with_guardrails', 'no_release')
RELEASES = {'proven': True, 'release_with_guardrails': True, 'no_release': False}


def declared_outcome(verdict) -> dict:
    """The outcome the declaration names for this harness verdict, with each condition it rests on."""
    if (verdict['candidate'], verdict['baseline'], verdict['primary_metric']) != ('C8', 'C6', 'AH all'):
        raise ValueError('Not the verdict of the C8 declaration')
    primary, draw = verdict['primary'], verdict['draw_sensitive']
    gains = {'AH all': primary['mean_gain'] if primary else None,
             'AH draw-sensitive': draw['mean_gain'] if draw else None}
    conditions = {'sample_minimum_met': bool(verdict['sample_minimum_met']),
                  'calibration_passes': bool(verdict['calibration']['passes']),
                  'point_estimates_positive': {k: bool(v is not None and v > 0) for k, v in gains.items()},
                  'primary_interval_clear_of_zero': bool(primary and primary['clear_of_zero'])}
    releasable = (conditions['sample_minimum_met'] and conditions['calibration_passes']
                  and all(conditions['point_estimates_positive'].values()))
    outcome = ('no_release' if not releasable
               else 'proven' if conditions['primary_interval_clear_of_zero'] else 'release_with_guardrails')
    return {'outcome': outcome, 'release': RELEASES[outcome], 'baseline_minus_candidate': gains,
            'conditions': conditions}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('--results', type=Path, required=True, help="The holdout run's results.json")
    args = parser.parse_args(argv)
    results = json.loads(args.results.read_text(encoding='utf-8'))
    declaration = json.loads(DECLARATION.read_text(encoding='utf-8'))
    if {k: results['declaration'].get(k) for k in declaration} != declaration:
        raise ValueError('results.json was not scored against the committed C8 declaration')
    print(json.dumps(declared_outcome(results['holdout_verdict']), indent=2))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
