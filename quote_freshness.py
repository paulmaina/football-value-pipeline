"""Shared live-quote timing rules; callers supply the evaluation clock."""
import pandas as pd

MAX_QUOTE_AGE_HOURS = 24.0
MAX_FUTURE_SKEW_MINUTES = 5.0


def quote_utc(value):
    if value is None:
        return None
    try:
        stamp = pd.to_datetime(value, utc=True, errors='coerce')
    except (TypeError, ValueError, OverflowError):
        return None
    return stamp if isinstance(stamp, pd.Timestamp) and not pd.isna(stamp) else None


def quote_clock(value):
    clock = quote_utc(value)
    if clock is None:
        raise ValueError('Invalid quote evaluation time')
    return clock


def quote_is_fresh(value, as_of):
    updated, clock = quote_utc(value), quote_utc(as_of)
    if updated is None or clock is None:
        return False
    age_seconds = (clock-updated).total_seconds()
    return -MAX_FUTURE_SKEW_MINUTES*60 <= age_seconds <= MAX_QUOTE_AGE_HOURS*3600
