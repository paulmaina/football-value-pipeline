"""Project-local API credentials. Never silently inherit shell keys in dotenv mode."""
from pathlib import Path
import os

API_KEY_NAMES = (
    'THE_ODDS_API_KEY', 'THE_ODDS_API_KEY_FALLBACK_1',
    'THE_ODDS_API_KEY_FALLBACK_2', 'FOOTBALL_DATA_API_KEY', 'BBS_API_KEY', 'API_FOOTBALL_KEY',
)
ENV_PATH = Path(__file__).resolve().parent / '.env'


def load_api_keys(source='dotenv', path=None):
    """Replace only API-key variables; explicit environment mode supports CI secrets.

    Missing/blank .env entries clear inherited credentials, including fallback
    keys. Disable interpolation so shell variables cannot supply file values.
    """
    if source == 'environment':
        return {name: bool(os.getenv(name, '').strip()) for name in API_KEY_NAMES}
    if source != 'dotenv':
        raise ValueError('API key source must be dotenv or environment')
    from dotenv import dotenv_values
    file = Path(path) if path is not None else ENV_PATH
    values = dotenv_values(file, interpolate=False, encoding='utf-8-sig') if file.is_file() else {}
    for name in API_KEY_NAMES:
        value = values.get(name)
        os.environ[name] = value.strip() if isinstance(value, str) else ''
    return {name: bool(os.environ[name]) for name in API_KEY_NAMES}
