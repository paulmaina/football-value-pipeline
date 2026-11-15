"""Main's pre-release master outputs (ebba9d8), committed as files, and a platform-independent comparison with them.

Why not byte digests: the outputs hold full-precision floats from scipy fits and matrix products, whose last digits
depend on the BLAS kernels the CPU selects (forcing OPENBLAS_CORETYPE=Nehalem on one machine changes every digest by
at most 1e-9), and pandas writes os.linesep (CRLF on Windows). So the comparison is: same file list, same columns in
the same order, the same rows (old master files in their written order; new master files, whose unranked rows can
tie in theory, keyed by offer identity), text, flags, ranks and decisions identical, and numbers within the replay
checks' tolerance (master_shortlist._same: 1e-7 absolute or 1e-8 relative). Byte-for-byte equality is asserted where
it is platform independent: between two modes' outputs on the same machine (test_master_release).
"""
from __future__ import annotations

import io
import json
import math
from pathlib import Path
from typing import List

import pandas as pd

import master_shortlist as ms

ROOT = Path(__file__).with_name('fixtures') / 'master_release_pre_release'
INDEX = json.loads((Path(__file__).with_name('fixtures') / 'master_release_pre_release.json').read_text(encoding='utf-8'))
CASES = {'frozen_forecast': 'frozen', 'snapshot_a00d5e530cc2e80e': 'snapshot'}
NEW_FILES = ('master_shortlist_new.csv',)
IDENTITY = ['kickoff_utc', 'league', 'home_team', 'away_team', 'market', 'handicap_side', 'handicap_line', 'bookmaker',
            'offered_decimal_odds', 'offered_last_update_utc']


def path(case: str, name: str) -> Path:
    return ROOT / CASES[case] / name


def read_csv(source) -> pd.DataFrame:
    """A CSV as the replay checks read it (master_shortlist._as_csv semantics)."""
    data = source.read_bytes() if isinstance(source, Path) else source
    try:
        return pd.read_csv(io.BytesIO(data), low_memory=False, float_precision='round_trip')
    except pd.errors.EmptyDataError:
        return pd.DataFrame()


def _cells(got: pd.DataFrame, want: pd.DataFrame, label: str) -> List[str]:
    problems = []
    for column in want.columns:
        for i, (g, w) in enumerate(zip(got[column].astype(object), want[column].astype(object))):
            if not ms._same(g, w):
                problems.append(f'{label} row {i} {column}: got {g!r}, want {w!r}')
    return problems


def frame_differences(got: pd.DataFrame, want: pd.DataFrame, keyed: bool = False, label: str = '') -> List[str]:
    """Differences between two master frames (empty when they agree as described in the module docstring)."""
    if list(got.columns) != list(want.columns):
        return [f'{label} columns differ: {list(got.columns)} vs {list(want.columns)}']
    if len(got) != len(want):
        return [f'{label} row count {len(got)} vs {len(want)}']
    if not keyed or got.empty:
        return _cells(got.reset_index(drop=True), want.reset_index(drop=True), label)
    key = lambda f: f[IDENTITY].astype(str).agg('|'.join, axis=1)
    got, want = got.assign(_key=key(got)), want.assign(_key=key(want))
    if got._key.duplicated().any() or want._key.duplicated().any() or set(got._key) != set(want._key):
        return [f'{label} offers differ']
    got = got.set_index('_key').loc[list(want._key)].reset_index(drop=True)
    return _cells(got, want.drop(columns='_key').reset_index(drop=True), label)


def json_differences(got, want, label: str = '') -> List[str]:
    if isinstance(want, dict):
        if not isinstance(got, dict) or set(got) != set(want):
            return [f'{label} keys differ: {sorted(got) if isinstance(got, dict) else got!r} vs {sorted(want)}']
        return [p for k in want for p in json_differences(got[k], want[k], f'{label}.{k}')]
    if isinstance(want, list):
        if not isinstance(got, list) or len(got) != len(want):
            return [f'{label} list differs']
        return [p for i, (g, w) in enumerate(zip(got, want)) for p in json_differences(g, w, f'{label}[{i}]')]
    if isinstance(want, float) and not isinstance(want, bool) and isinstance(got, (int, float)) \
            and not isinstance(got, bool):
        same = (math.isnan(want) and math.isnan(got)) or math.isclose(got, want, abs_tol=1e-7, rel_tol=1e-8)
        return [] if same else [f'{label}: got {got!r}, want {want!r}']
    return [] if got == want and type(got) is type(want) else [f'{label}: got {got!r}, want {want!r}']


def golden_json(case: str, name: str):
    return json.loads(path(case, name).read_text(encoding='utf-8'))
