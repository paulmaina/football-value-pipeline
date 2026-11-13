"""The Odds API credit usage: per-call header capture, per-run records and a budget guard.

Every live Odds API response carries three numeric headers: x-requests-remaining,
x-requests-used and x-requests-last (the cost of that call). The client records
them per key slot after each call. No key value, URL or response text is kept:
a slot is named only by its environment variable.

Each workflow run that calls the API writes one record to the run summary and
appends it to a committed log, so the credits left on each key are always
visible. The budget guard reads the latest known balances: when the credits
left on all keys fall below what one forecast run needs, optional calls (price
checks, per-event extra coverage, closing quotes for fixtures without a pick)
are skipped so the core forecast can still run.
"""
from __future__ import annotations

import json
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Iterable, List, Mapping, Optional

SLOTS = ('THE_ODDS_API_KEY', 'THE_ODDS_API_KEY_FALLBACK_1', 'THE_ODDS_API_KEY_FALLBACK_2')
HEADERS = ('x-requests-remaining', 'x-requests-used', 'x-requests-last')
LOG = Path('football_output_v2/odds_api_usage/usage_log.jsonl')

# Credits one full forecast run needs: 3 per league for the main request
# (h2h, totals, spreads; one bookmaker group) plus 4 per in-window fixture for
# the per-event request (alternate totals and spreads, double chance, draw no
# bet). The largest run measured from 17 Oct to 8 Nov 2026 used 288 credits
# (10 leagues, 66 in-window fixtures); 300 keeps that with a small margin.
FORECAST_RUN_CREDITS = 300
# The core forecast: one main request per league, and nothing optional.
CORE_CREDITS_PER_LEAGUE = 3
EXTRA_EVENT_CREDITS = 4

NO_FIXTURES = 'NO_FIXTURES'
CREDITS_EXHAUSTED = 'CREDITS_EXHAUSTED'
FORECASTS_PRODUCED = 'FORECASTS_PRODUCED'
EXHAUSTED_MESSAGE = 'Odds API credits exhausted on all keys; forecasts not produced'


def no_fixtures_message(days: int) -> str:
    return f'No fixtures in the next {days} days; nothing to forecast'


def endpoint_kind(url: str) -> str:
    """Endpoint family from a request URL; the URL itself is never stored."""
    path = str(url).split('?', 1)[0].rstrip('/')
    if '/events/' in path and path.endswith('/odds'):
        return 'event_odds'
    if path.endswith('/events'):
        return 'events'
    if path.endswith('/odds'):
        return 'odds'
    return 'other'


def _header_number(headers: Mapping, name: str) -> Optional[int]:
    value = str(headers.get(name, '') if headers is not None else '')
    # Same bound as odds_provider_health: ASCII digits only, at most 12 of them.
    return int(value) if value.isascii() and value.isdigit() and len(value) <= 12 else None


class UsageLedger:
    """Usage headers of every live call made by one client in one process."""

    def __init__(self, seed: Optional[Mapping[str, Mapping]] = None):
        self.calls: List[Dict[str, object]] = []
        self.exhausted = False
        # Latest known balance per slot; seeded from the committed log.
        self.known: Dict[str, Dict[str, object]] = {
            slot: dict(values) for slot, values in (seed or {}).items() if slot in SLOTS}

    def record(self, slot: str, url: str, status: int, headers: Mapping) -> Dict[str, object]:
        entry: Dict[str, object] = {'slot': slot, 'endpoint': endpoint_kind(url), 'http_status': int(status)}
        for name in HEADERS:
            value = _header_number(headers, name)
            if value is not None:
                entry[name] = value
        self.calls.append(entry)
        if 'x-requests-remaining' in entry and slot in SLOTS:
            self.known[slot] = {'remaining': entry['x-requests-remaining'],
                                'used': entry.get('x-requests-used'),
                                'observed_at_utc': datetime.now(timezone.utc).isoformat(timespec='seconds')}
        return entry

    def credits_spent(self) -> int:
        return sum(int(c.get('x-requests-last') or 0) for c in self.calls
                   if 200 <= int(c['http_status']) < 300)

    def remaining_total(self) -> Optional[int]:
        """Sum of the latest known balances; None when no slot's balance is known."""
        values = [int(v['remaining']) for v in self.known.values() if v.get('remaining') is not None]
        return sum(values) if values else None

    def allows_optional(self, cost: int = 0) -> bool:
        """Optional calls run unless the known balance is below one forecast run.

        An unknown balance (no call yet, no committed record) never blocks a call.
        """
        total = self.remaining_total()
        return total is None or total - cost >= FORECAST_RUN_CREDITS

    def summary(self) -> Dict[str, object]:
        by_endpoint: Dict[str, Dict[str, int]] = {}
        for call in self.calls:
            item = by_endpoint.setdefault(str(call['endpoint']), {'calls': 0, 'credits': 0})
            item['calls'] += 1
            if 200 <= int(call['http_status']) < 300:
                item['credits'] += int(call.get('x-requests-last') or 0)
        slots = {}
        for slot in SLOTS:
            if slot in self.known:
                slots[slot] = {k: self.known[slot].get(k) for k in ('remaining', 'used', 'observed_at_utc')}
        return {'calls': len(self.calls), 'credits_spent': self.credits_spent(),
                'by_endpoint': dict(sorted(by_endpoint.items())), 'slots': slots,
                'remaining_total': self.remaining_total(), 'all_keys_exhausted': bool(self.exhausted)}


def run_record(workflow: str, ledger: Optional[UsageLedger], *, outcome: str = '',
               message: str = '', clock: Optional[datetime] = None, **extra) -> Dict[str, object]:
    """One small record per run: no key values, only slot names and counts."""
    clock = clock or datetime.now(timezone.utc)
    usage = ledger.summary() if ledger is not None else UsageLedger().summary()
    record = {'recorded_at_utc': clock.isoformat(timespec='seconds'), 'workflow': workflow,
              'outcome': outcome, **({'message': message} if message else {}), **usage}
    record.update(extra)
    return record


def append_log(record: Mapping, repo: Path | str = '.', log: Path = LOG) -> Path:
    path = Path(repo) / log
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('a', encoding='utf-8', newline='\n') as handle:
        handle.write(json.dumps(record, sort_keys=True, allow_nan=False) + '\n')
    return path


def read_log(repo: Path | str = '.', log: Path = LOG) -> List[Dict[str, object]]:
    path = Path(repo) / log
    if not path.exists():
        return []
    records = []
    for line in path.read_text(encoding='utf-8').splitlines():
        try:
            item = json.loads(line)
        except ValueError:
            continue  # A torn line never blocks forecasting.
        if isinstance(item, dict):
            records.append(item)
    return records


def latest_balances(records: Iterable[Mapping]) -> Dict[str, Dict[str, object]]:
    """Latest known balance per slot across all logged runs (by observation time)."""
    latest: Dict[str, Dict[str, object]] = {}
    for record in records:
        for slot, values in (record.get('slots') or {}).items():
            if slot not in SLOTS or not isinstance(values, dict) or values.get('remaining') is None:
                continue
            stamp = str(values.get('observed_at_utc') or record.get('recorded_at_utc') or '')
            if slot not in latest or stamp >= str(latest[slot].get('observed_at_utc') or ''):
                latest[slot] = {'remaining': values['remaining'], 'used': values.get('used'),
                                'observed_at_utc': stamp}
    return latest


def seeded_ledger(repo: Path | str = '.') -> UsageLedger:
    return UsageLedger(latest_balances(read_log(repo)))


def summary_markdown(record: Mapping) -> str:
    lines = ['### Odds API credits', '']
    if record.get('message'):
        lines += [str(record['message']), '']
    lines.append(f"Calls this run: {record.get('calls', 0)}; credits spent: {record.get('credits_spent', 0)}.")
    slots = record.get('slots') or {}
    if slots:
        lines += ['', '| Key slot | Remaining | Used | As of (UTC) |', '|---|---:|---:|---|']
        for slot in SLOTS:
            if slot in slots:
                values = slots[slot]
                lines.append(f"| {slot} | {values.get('remaining')} | {values.get('used')} | {values.get('observed_at_utc')} |")
        lines += ['', f"Known credits left on all keys: {record.get('remaining_total')}."]
    else:
        lines += ['', 'No usage headers received this run.']
    return '\n'.join(lines) + '\n'


def write_step_summary(text: str) -> None:
    """Append to the GitHub Actions run summary when one is available."""
    path = os.getenv('GITHUB_STEP_SUMMARY')
    if path:
        with open(path, 'a', encoding='utf-8') as handle:
            handle.write(text if text.endswith('\n') else text + '\n')


def write_json(path: Path | str, data: Mapping) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True, allow_nan=False), encoding='utf-8')
