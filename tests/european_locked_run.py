"""One locked European run on the cached results, shared by the European lock tests.

The run is computed once per test process (test_european_backtest and test_european_candidates both read it).
Its window crosses the European holdout start (21 Jan 2025) with two active fold origins:

- 9 Dec 2024: UCL validation (10-11 Dec) and UEL validation (11-12 Dec) are scored;
- 21 Jan 2025: UCL holdout (21-22 Jan) must be skipped; UEL (23 Jan) is retrospective and scored.

It is a locked run (no declaration), so it never scores a European holdout match. Every candidate is built
(CE and CE2-CE4, with the real domestic strengths), as the --mode european default does.
"""
from functools import lru_cache
import json
from pathlib import Path

import evaluation_harness as eh

REPO = Path(__file__).resolve().parents[1]
CACHE = REPO / '.football_cache'
CFG = json.loads((REPO / 'evaluation_harness_config.json').read_text(encoding='utf-8'))
WINDOW = {'test_start': '2024-12-09', 'end_exclusive': '2025-01-27'}


def config():
    return {**CFG, 'european': {**CFG['european'], **WINDOW}}


@lru_cache(maxsize=None)
def locked_run():
    """(records, folds, coverage, calib) of eh.european on the cached results in WINDOW. Read only."""
    return eh.european(CACHE, config())
