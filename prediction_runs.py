"""Complete immutable prediction generations and an atomic current-run pointer.

Local save times are not independent forward-capture evidence. Cloud capture
still uses its actual receipt time, including for runs uploaded together.
"""
from contextlib import contextmanager
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import tempfile

RUNS = 'prediction_runs'
POINTER = 'current_run.json'
MANIFEST = 'run_manifest.json'


def encoded(value):
    return (json.dumps(value, sort_keys=True, separators=(',', ':'), allow_nan=False)+'\n').encode()


def digest(data):
    return hashlib.sha256(data).hexdigest()


def archive_identity(metadata, directory_name):
    run_id = metadata.get('prediction_run_id', '')
    source = metadata.get('git_commit_sha', '')
    archive_id = metadata.get('archive_id', '')
    if (not re.fullmatch('[0-9a-f]{64}', run_id) or not re.fullmatch('[0-9a-fA-F]{40}', source)
            or archive_id != digest(('prediction-run:'+run_id).encode())[:40]
            or directory_name != archive_id[:16]):
        raise ValueError('Invalid prediction-run archive identity')
    return archive_id


def validate_archive_binding(directory, metadata):
    """Bind renamed snapshot core files to their complete original generation."""
    manifest = json.loads((directory/MANIFEST).read_bytes())
    identity = {k: manifest[k] for k in ('version', 'generated_at_utc', 'sha256')}
    if (digest(encoded(identity)) != metadata['prediction_run_id']
            or manifest['run_id'] != metadata['prediction_run_id']):
        raise ValueError('Archived prediction-run identity mismatch')
    for original, archived in [('all_leagues_predictions.csv','predictions.csv'),
            ('conservative_bet_shortlist.csv','shortlist.csv'),
            ('conservative_bet_summary.json','selection_summary.json')]:
        if digest((directory/archived).read_bytes()) != manifest['sha256'].get(original):
            raise ValueError('Archived prediction-run content mismatch')


def atomic_write(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(dir=path.parent, prefix='.run-write-', delete=False) as file:
        temporary = Path(file.name)
        file.write(data)
        file.flush()
        os.fsync(file.fileno())
    try:
        os.replace(temporary, path)
    finally:
        temporary.unlink(missing_ok=True)


def validate_bundle(directory):
    directory = Path(directory)
    manifest = json.loads((directory/MANIFEST).read_bytes())
    identity = {k: manifest[k] for k in ('version', 'generated_at_utc', 'sha256')}
    if manifest['version'] != 1 or digest(encoded(identity)) != manifest['run_id']:
        raise ValueError('Invalid prediction-run identity')
    required = {'all_leagues_predictions.csv', 'conservative_bet_shortlist.csv',
                'conservative_bet_summary.json', 'pipeline_run_metadata.json'}
    if not required.issubset(manifest['sha256']):
        raise ValueError('Incomplete prediction-run manifest')
    for name, expected in manifest['sha256'].items():
        relative = Path(name)
        if (relative.is_absolute() or '..' in relative.parts or '\\' in name
                or not relative.parts or name == MANIFEST):
            raise ValueError('Unsafe prediction-run path')
        file = directory/relative
        if any(p.is_symlink() for p in (file, *file.parents)) or digest(file.read_bytes()) != expected:
            raise ValueError('Prediction-run checksum mismatch: '+name)
    summary = json.loads((directory/'conservative_bet_summary.json').read_bytes())
    if summary['generated_at_utc'] != manifest['generated_at_utc']:
        raise ValueError('Prediction-run generation mismatch')
    return manifest


def resolve_raw(raw):
    """Resolve once per operation; never fall back from a corrupt pointer."""
    raw = Path(raw)
    pointer = raw/POINTER
    if not pointer.exists():
        return raw  # Existing historical checkouts and explicit bundle paths.
    data = json.loads(pointer.read_bytes())
    run_id = data.get('run_id', '')
    if data.get('version') != 1 or not re.fullmatch('[0-9a-f]{64}', run_id):
        raise ValueError('Invalid current prediction-run pointer')
    directory = raw/RUNS/run_id
    manifest = validate_bundle(directory)
    if manifest['run_id'] != run_id or digest((directory/MANIFEST).read_bytes()) != data.get('manifest_sha256'):
        raise ValueError('Current prediction-run binding mismatch')
    return directory


@contextmanager
def stage_run(raw, *, seed=False):
    """Serialize writers; failed fits never modify the published generation."""
    raw = Path(raw)
    raw.mkdir(parents=True, exist_ok=True)
    lock = raw/'.prediction-run.lock'
    try:
        lock.mkdir()
    except FileExistsError as exc:
        raise RuntimeError('Another prediction writer is active. If interrupted, verify it stopped before removing '+str(lock)) from exc
    try:
        with tempfile.TemporaryDirectory(prefix='.prediction-stage-', dir=raw.parent) as temporary:
            staging = Path(temporary)/'raw'
            staging.mkdir()
            previous = resolve_raw(raw)
            # Mutable validation-cache projections keep their existing invalidation
            # behavior; forecast readers still use the verified immutable bundle.
            sources = previous if seed else raw
            for source in sources.iterdir():
                if source.is_file() and (seed or source.name.endswith('_goal_market_validation.json')):
                    if source.name not in (POINTER, MANIFEST):
                        shutil.copyfile(source, staging/source.name)
            yield staging
    finally:
        lock.rmdir()


def publish_run(staging, raw):
    """Freeze all run files, update compatibility views, then switch one pointer.

    Readers follow the immutable bundle, not the compatibility copies. Exception
    rollback restores those copies too; a killed writer leaves the old pointer.
    """
    staging, raw = Path(staging), Path(raw)
    summary = json.loads((staging/'conservative_bet_summary.json').read_bytes())
    files = {p.relative_to(staging).as_posix(): digest(p.read_bytes())
             for p in sorted(staging.rglob('*')) if p.is_file() and p.name != MANIFEST}
    identity = {'version': 1, 'generated_at_utc': summary['generated_at_utc'], 'sha256': files}
    manifest = {**identity, 'run_id': digest(encoded(identity)),
                'saved_at_utc': datetime.now(timezone.utc).isoformat()}
    atomic_write(staging/MANIFEST, encoded(manifest))
    validate_bundle(staging)
    target = raw/RUNS/manifest['run_id']
    target.parent.mkdir(exist_ok=True)
    if target.exists():
        existing = validate_bundle(target)
        if any(existing[k] != manifest[k] for k in identity):
            raise ValueError('Immutable prediction-run conflict')
    else:
        # Same filesystem: incomplete bundle directories never become visible.
        staging.rename(target)
    with tempfile.TemporaryDirectory(prefix='.prediction-backup-', dir=raw.parent) as temporary:
        backup = Path(temporary)
        old_files = [p for p in raw.iterdir() if p.is_file() and p.name != POINTER]
        overwritten = {raw/name for name in files if (raw/name).is_file()}
        for file in set(old_files) | overwritten:
            saved = backup/file.relative_to(raw)
            saved.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(file, saved)
        written = []
        try:
            for name in files:
                # Timestamped decision history is retained separately too.
                written.append(raw/name)
                atomic_write(raw/name, (target/name).read_bytes())
            for file in old_files:
                managed = (file.name.endswith(('_predictions.csv', '_diagnostics.json',
                           '_scorelines.json', '_goal_market_validation.json', '_decay_tuning.json',
                           '_market_weight_validation.json', '_experiment.json'))
                           and '_backtest_' not in file.name)
                if managed and file.name not in files:
                    file.unlink()
            atomic_write(raw/POINTER, encoded({'version': 1, 'run_id': manifest['run_id'],
                         'manifest_sha256': digest((target/MANIFEST).read_bytes())}))
        except BaseException:
            for file in written:
                if file.is_file():
                    file.unlink()
            for file in backup.rglob('*'):
                if file.is_file():
                    shutil.copyfile(file, raw/file.relative_to(backup))
            raise
    return target


def capture_runs(root, source_commit, *, captured_at=None):
    """Capture every uploaded generation at actual receipt time, never saved time."""
    from performance_tracking import capture, now_utc
    from workflow_checks import raw_check
    root = Path(root)
    clock = captured_at or now_utc()
    count = 0
    for directory in sorted((root/'raw'/RUNS).glob('*')):
        if not directory.is_dir() or not re.fullmatch('[0-9a-f]{64}', directory.name):
            raise ValueError('Invalid prediction-run directory')
        manifest = validate_bundle(directory)
        if manifest['run_id'] != directory.name:
            raise ValueError('Prediction-run directory identity mismatch')
        raw_check(root, raw_dir=directory)
        count += bool(capture(source_commit, root=root, captured_at=clock,
                              raw_dir=directory, prediction_run_id=manifest['run_id']))
    return count
