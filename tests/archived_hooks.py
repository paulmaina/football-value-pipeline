"""Test-only replay of the retired experiments' capture and review hooks.

Production capture/review no longer touch archive/. Tests of the archived
experiments still exercise their freeze, grading and tamper rules end to end,
so this re-attaches the removed hooks around performance_tracking.capture and
performance_tracking.review, in their original order, for the enclosing tests only.
"""
from contextlib import contextmanager
import hashlib
import importlib
from pathlib import Path
import shutil
import sys
import warnings

import performance_tracking

# Original order and warning text of performance_tracking before the retirement.
CAPTURED = {
    'shortlist_weight_experiment': lambda e: f'Shortlist weight capture skipped ({type(e).__name__})',
    'shortlist_policy_experiment': lambda e: f'Shortlist policy capture skipped ({type(e).__name__})',
    'goal_blend_experiment': lambda e: f'Shadow capture skipped: {e}',
    'market_led_experiment': lambda e: f'Market-led capture skipped ({type(e).__name__})',
    'filter_sensitivity_experiment': lambda e: f'Filter sensitivity capture skipped ({type(e).__name__})',
    'model_reliability_experiment': lambda e: f'Reliability capture skipped ({type(e).__name__})',
    # Archived 2026-11-03 (PR E).
    'benchmark_forward_experiment': lambda e: f'Benchmark forward capture skipped ({type(e).__name__})',
    'totals_anchor_experiment': lambda e: f'Totals anchoring capture skipped ({type(e).__name__})',
}
REVIEWED = {
    'goal_blend_experiment': lambda e: f'Shadow report failed; baseline report complete: {e}',
    'market_led_experiment': lambda e: f'Market-led report failed ({type(e).__name__}); baseline report complete',
    'recency_experiment': lambda e: f'Recency report failed ({type(e).__name__}); baseline report complete',
    'shortlist_weight_experiment': lambda e: f'Shortlist weight report failed ({type(e).__name__}); baseline report complete',
    'shortlist_policy_experiment': lambda e: f'Shortlist policy report failed ({type(e).__name__}); baseline report complete',
    'filter_sensitivity_experiment': lambda e: f'Filter sensitivity report failed ({type(e).__name__}); baseline report complete',
    'model_reliability_experiment': lambda e: f'Reliability review failed ({type(e).__name__}); production report complete',
    # Archived 2026-11-03 (PR E).
    'benchmark_forward_experiment': lambda e: f'Benchmark forward review failed ({type(e).__name__}); production report complete',
    'totals_anchor_experiment': lambda e: f'Totals anchoring review failed ({type(e).__name__}); production report complete',
}


def _capture_archived(original):
    def capture(commit_sha, *, root=performance_tracking.ROOT, raw_dir=None, **kwargs):
        snapshots = Path(root)/'performance'/'snapshots'
        before = set(snapshots.iterdir()) if snapshots.exists() else set()
        result = original(commit_sha, root=root, raw_dir=raw_dir, **kwargs)
        created = [d for d in snapshots.iterdir() if d not in before] if snapshots.exists() else []
        if not result or len(created) != 1:
            return result
        from prediction_runs import resolve_raw
        raw = Path(raw_dir) if raw_dir is not None else resolve_raw(Path(root)/'raw')
        generated = performance_tracking.load_json(raw/'conservative_bet_summary.json', {}).get('generated_at_utc')
        directory = created[0]
        meta = performance_tracking.load_json(directory/'metadata.json', {})
        for name, message in CAPTURED.items():
            try:
                source = importlib.import_module('archive.'+name).capture_file(raw, generated)
            except Exception as exc:
                warnings.warn(message(exc))
                continue
            if source is None:
                continue
            shutil.copyfile(source, directory/(name+'.json'))
            meta['sha256'][name+'.json'] = hashlib.sha256((directory/(name+'.json')).read_bytes()).hexdigest()
        performance_tracking.write_json(directory/'metadata.json', meta)
        return result
    return capture


def _review_archived(original):
    def review(*, root=performance_tracking.ROOT, token='', clock=None, session=None):
        clock = clock or performance_tracking.now_utc()
        result = original(root=root, token=token, clock=clock, session=session)
        archived = performance_tracking.snapshots(root)
        rows = (performance_tracking.frozen_rows(archived, 'shortlist', latest=True)
                + performance_tracking.frozen_rows(archived, 'predictions'))
        unique = {r['fixture_key']: r for r in rows}
        records, _ = performance_tracking.collect_results(list(unique.values()), root=root, token=token,
                                                          clock=clock, session=session)
        for name, message in REVIEWED.items():
            try:
                importlib.import_module('archive.'+name).review_experiment(root, archived, records, clock)
            except Exception as exc:
                warnings.warn(message(exc))
        try:
            importlib.import_module('archive.model_comparison').review(root, archived, records, clock)
        except Exception as exc:
            warnings.warn(f'Model comparison review failed ({type(exc).__name__}); production report complete')
        return result
    return review


@contextmanager
def archived_hooks():
    """Patch capture/review everywhere they are bound, then restore them exactly."""
    originals = {'capture': performance_tracking.capture, 'review': performance_tracking.review}
    replacements = {'capture': _capture_archived(originals['capture']),
                    'review': _review_archived(originals['review'])}
    patched = []
    for module in list(sys.modules.values()):
        for name, original in originals.items():
            if getattr(module, name, None) is original:
                setattr(module, name, replacements[name])
                patched.append((module, name, original))
    try:
        yield
    finally:
        for module, name, original in patched:
            setattr(module, name, original)


_active = []


def setUpModule():
    """Use as `from archived_hooks import setUpModule, tearDownModule` in archived-experiment tests."""
    hooks = archived_hooks()
    hooks.__enter__()
    _active.append(hooks)


def tearDownModule():
    _active.pop().__exit__(None, None, None)
