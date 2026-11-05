"""Standard-library CSV reading for forecasts containing full JSON evidence."""
import csv
import sys


def dict_reader(handle, *args, **kwargs):
    """Keep fields intact, using the largest limit this platform supports.

    Python's default 128-Ki-character limit is too small for frozen research.
    The C integer accepted by csv.field_size_limit can be narrower than
    sys.maxsize on Windows. Back off on overflow rather than breaking import
    or relying on another module to configure the process-wide CSV parser.
    Configure at each entry point, including a standalone closing-odds plan.
    """
    limit = sys.maxsize
    while True:
        try:
            csv.field_size_limit(limit)
            break
        except OverflowError:
            limit //= 10
    return csv.DictReader(handle, *args, **kwargs)
