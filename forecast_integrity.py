"""Semantic CSV binding across Git's LF/CRLF conversion; archive hashes stay exact."""
import hashlib
import json


def forecast_digest_variants(path):
    data=path.read_bytes()
    lf=data.replace(b'\r\n',b'\n')
    return {hashlib.sha256(value).hexdigest() for value in (data,lf,lf.replace(b'\n',b'\r\n'))}


def snapshot_generated_at(directory, metadata):
    """Recover legacy subsecond precision only from the hash-bound summary.

    Older capture metadata truncated microseconds. The original selection
    summary retained them; verify its exact bytes before using that timestamp.
    No sidecar, prediction, selection, or archived metadata is rewritten.
    """
    from performance_tracking import utc
    stamp = metadata.get('generated_at_utc')
    recorded = utc(stamp)
    if recorded is None:
        raise ValueError('Invalid snapshot generation time')
    expected = metadata.get('sha256', {}).get('selection_summary.json')
    if not expected:
        return stamp
    content = (directory/'selection_summary.json').read_bytes()
    if hashlib.sha256(content).hexdigest() != expected:
        raise ValueError('Snapshot selection summary integrity failure')
    precise = json.loads(content).get('generated_at_utc')
    generated = utc(precise)
    if generated is None or (generated != recorded and (
            recorded.microsecond != 0 or generated.replace(microsecond=0) != recorded)):
        raise ValueError('Snapshot generation time differs from bound summary')
    return precise

