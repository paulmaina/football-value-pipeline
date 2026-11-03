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


def monitoring_equivalent(actual, expected):
    """Solver diagnostics allow max(1e-7 absolute, 1e-8 relative) drift.

    Identity, timestamps, versions, labels and quoted bookmaker prices still
    use the strict comparator. Only recomputed probabilities/fair prices drift.
    """
    if not isinstance(actual, list) or len(actual) != len(expected):
        return False
    for row, replay in zip(actual, expected):
        if not isinstance(row, dict) or row.keys() != replay.keys():
            return False
        for key, value in replay.items():
            fitted = key in ('corrected_p2', 'corrected_p3', 'uncorrected_p2', 'uncorrected_p3') or key.endswith(
                ('_corrected_fair_odds', '_uncorrected_fair_odds'))
            if fitted and value is not None:
                got = row[key]
                if (isinstance(got, bool) or not isinstance(got, (int, float)) or not math.isfinite(got)
                        or not math.isclose(got, value, abs_tol=1e-7, rel_tol=1e-8)):
                    return False
            elif not equivalent(row[key], value):
                return False
    return True

