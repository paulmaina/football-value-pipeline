"""Exact-comparison helpers for deterministic shortlist replay.

Moved unchanged from the retired filter-sensitivity and shortlist-policy
experiments, which re-export them, because the live raw check still needs them.
"""
import json
import math


def clean(table):
    # pandas serializes missing/nonfinite values as JSON null.
    return json.loads(table.to_json(orient='records', double_precision=15))


def equivalent(actual, expected):
    """Allow only CSV/JSON floating-point roundoff, never semantic changes."""
    if isinstance(expected, dict):
        return isinstance(actual, dict) and actual.keys() == expected.keys() and all(equivalent(actual[k], v) for k, v in expected.items())
    if isinstance(expected, list):
        return isinstance(actual, list) and len(actual) == len(expected) and all(equivalent(a, b) for a, b in zip(actual, expected))
    if isinstance(expected, (int, float)) and not isinstance(expected, bool):
        return isinstance(actual, (int, float)) and not isinstance(actual, bool) and math.isfinite(actual) and abs(actual-expected) <= 1e-9
    return type(actual) is type(expected) and actual == expected
