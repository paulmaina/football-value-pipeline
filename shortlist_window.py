"""Kickoff horizon shared by live shortlist generation and recorded replay."""
from contextlib import contextmanager
from contextvars import ContextVar

DEFAULT_HOURS = 24
LEGACY_HOURS = 48
_HOURS = ContextVar('shortlist_lookahead_hours', default=LEGACY_HOURS)


def hours():
    return _HOURS.get()


def rejection_reason():
    return f'kickoff outside 20-minute to {hours():g}-hour window'


@contextmanager
def scope(lookahead_hours):
    if lookahead_hours not in (DEFAULT_HOURS, LEGACY_HOURS):
        raise ValueError('Unknown shortlist lookahead')
    token = _HOURS.set(lookahead_hours)
    try:
        yield
    finally:
        _HOURS.reset(token)
