"""Execution checks for production candidates; never infer exchange liquidity."""
import json
import math
from pathlib import Path

CONFIG = Path(__file__).with_name('shortlist_quote_policy.json')


def is_exchange(name):
    value = str(name or '').casefold().replace(' ', '').replace('_', '').replace('-', '')
    return any(key in value for key in ('matchbook', 'betfairex', 'betfairexchange', 'smarkets', 'betdaq'))


def load_policy(path=None):
    file = Path(path) if path is not None else CONFIG
    data = json.loads(file.read_text(encoding='utf-8-sig')) if file.exists() else {}
    return validate_policy(data)


def validate_policy(data):
    """Validate current or frozen execution settings without changing globals."""
    if not isinstance(data, dict):
        raise ValueError('Execution policy must be an object')
    names = data.get('allowed_bookmakers', [])
    costs = data.get('per_stake_cost_bps', 0)
    if not isinstance(names, list) or any(not isinstance(n, str) or not n.strip() for n in names):
        raise ValueError('allowed_bookmakers must be a list of nonblank names')
    if isinstance(costs, bool) or not isinstance(costs, (float, int)) or not math.isfinite(costs) or not 0 <= costs <= 10000:
        raise ValueError('per_stake_cost_bps must be finite and between 0 and 10000')
    fallback = data.get('fallback_bookmakers', [])
    if not isinstance(fallback, list) or any(not isinstance(n, str) or not n.strip() for n in fallback):
        raise ValueError('fallback_bookmakers must be a list of nonblank names')
    risk_settings = {}
    if 'asian_handicap_risk_tolerance' in data:
        tolerance = data['asian_handicap_risk_tolerance']
        if isinstance(tolerance,bool) or not isinstance(tolerance,(int,float)) or not math.isfinite(tolerance) or not 0 <= tolerance <= 1:
            raise ValueError('asian_handicap_risk_tolerance must be a finite probability from 0 to 1')
        risk_settings['asian_handicap_risk_tolerance'] = tolerance
    return {**risk_settings, **({'fallback_bookmakers': fallback} if fallback else {}), 'allowed_bookmakers': names, 'per_stake_cost_bps': costs,
            'exchange_policy': 'EXCLUDED_UNTIL_COMMISSION_AND_LIQUIDITY_ADAPTER',
            'account_availability': 'USER_ALLOWLIST' if names else 'NOT_VERIFIED'}


def usable_bookmaker(name, policy=None):
    policy = policy or load_policy()
    if not isinstance(name, str) or not name.strip() or is_exchange(name):
        return False
    allowed = policy['allowed_bookmakers']
    return not allowed or name.casefold().strip() in {x.casefold().strip() for x in allowed}


def stake_cost(value):
    try:
        cost = float(value)
    except (ValueError, TypeError):
        raise ValueError('Invalid frozen stake cost') from None
    if not math.isfinite(cost) or not 0 <= cost <= 1:
        raise ValueError('Invalid frozen stake cost')
    return cost


def bookmaker_priority(name, policy=None):
    """Prefer primary quotes over fallback quotes for an exact market."""
    policy = policy or load_policy()
    fallback = {n.casefold().strip() for n in policy.get('fallback_bookmakers', [])}
    return 0 if str(name).casefold().strip() in fallback else 1
