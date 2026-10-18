"""Safe provider diagnostics, retained independently of idle collector polls."""
import json
from pathlib import Path


class OddsProviderError(RuntimeError):
    def __init__(self, message, category, attempts):
        super().__init__(message)
        self.category = category
        self.attempts = attempts


def http_details(exc, credential):
    response = exc.response
    result = {'credential': credential, 'http_status': response.status_code}
    try:
        payload = response.json()
    except ValueError:
        payload = {}
    code = payload.get('error_code') if isinstance(payload, dict) else None
    # Never persist response text, URLs, headers other than numeric usage, or keys.
    if code in ('OUT_OF_USAGE_CREDITS', 'INVALID_KEY', 'DEACTIVATED_KEY', 'EXCEEDED_FREQ_LIMIT'):
        result['error_code'] = code
    for header in ('x-requests-remaining', 'x-requests-used', 'x-requests-last'):
        value = str(response.headers.get(header, ''))
        if value.isascii() and value.isdigit() and len(value) <= 12:
            result[header] = int(value)
    return result


def checkpoint(root, clock, error=None):
    from performance_tracking import load_json, write_json
    path = Path(root)/'closing_odds/provider_status.json'
    previous = load_json(path, {})
    stamp = clock.isoformat()
    state = {**previous, 'checked_at_utc': stamp, 'state': 'AVAILABLE'}
    if error is not None:
        category = error.category if isinstance(error, OddsProviderError) else 'COLLECTION_ERROR'
        failure = {'at_utc': stamp, 'category': category, 'error': type(error).__name__}
        if isinstance(error, OddsProviderError):
            failure['attempts'] = error.attempts
        state.update(state=category, last_failure=failure,
                     incident_started_at_utc=(previous.get('incident_started_at_utc')
                         if previous.get('state') == category else stamp))
    elif previous.get('state') not in (None, 'AVAILABLE'):
        state['recovered_at_utc'] = stamp
    write_json(path, state)
    return state


def alert_summary(root):
    """Actions annotations are delivery signals; GitHub notification settings apply."""
    return alert_summary_from_path(Path(root)/'closing_odds/provider_status.json')


def alert_summary_from_path(path):
    path = Path(path)
    state = json.loads(path.read_text(encoding='utf-8-sig')) if path.exists() else {}
    if state.get('state') not in ('CREDITS_EXHAUSTED', 'RATE_LIMITED', 'HTTP_ERROR'):
        return ''
    return ('Closing odds provider unavailable: '+state['state']+'. '
            'Closing quotes cannot be collected. See closing_odds/provider_status.json '
            'in the recovery artifact or repository for safe provider evidence. '
            'HTTP 429 alone does not confirm monthly credit depletion.')
