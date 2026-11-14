"""Shortlist entry audit (offline only): the two lists that feed the master, as selection functions.

One `value_select` and one `cagey_select`, shared by the historical backtest (`evaluation_harness.py --mode lists`)
and the reproduction check on saved live runs (`decision_offers` + `tests/test_shortlist_entry_audit.py`). They
express the entry rules a backtest can test; `Rules` holds today's values (`TODAY`) and the steps the audit tries.

Today's rules, as live (`cagey_correction_config.json`, `shortlist_quote_policy.json`):

* Value shortlist, `local-research-profit-115-200-dc12-v2` (`profit_shortlist.annotate` / `select`): offered odds
  in (1.15, 2.00]; markets not in `excluded_markets`; a research settlement distribution; one pick per fixture
  and market group (Asian handicap, match winner, double chance), the highest research probability of a positive
  return, then research expected return, then odds. No edge, probability or expected-return floor.
* Cagey tier, `no-loss-market-reference-v5` (`cagey_tier_v3.annotate` -> `cagey_market_basis.annotate`,
  `cagey_tier_v3.select`): offered odds in (1.15, 2.00]; markets not excluded; a cagey settlement distribution;
  the price guard (win, double chance, AH +/-0.5 and Over 1.5 against the independent margin-free Pinnacle fair
  price, other AH lines against the cagey fair odds; offered > 1.15 x fair is rejected; no reference, no guard);
  one pick per fixture and market group, the highest cagey no-loss probability, then cagey expected return, then
  odds. No narrow, expected-return or no-loss floor.

Rules a backtest can't express (kickoff window, quote freshness and timing, input synchronisation, bookmaker,
data availability, the Europa appearance rule) are carried by each offer as `blocked_value` / `blocked_cagey`.
Nothing here reads a result: offers carry their settlement only for the audit's scoring, after selection.
"""
from __future__ import annotations

from dataclasses import dataclass, replace
import math

import numpy as np

KINDS = ('win', 'half_win', 'push', 'half_loss', 'loss')
TOLERANCE = 1e-9
EXCLUDED_TODAY = frozenset({'Over 1.5', 'Double Chance 12', 'Draw No Bet Home', 'Draw No Bet Away'})
BINARY = ('Home win', 'Away win', 'Double Chance 1X', 'Double Chance X2', 'Double Chance 12', 'Over 1.5')


@dataclass(frozen=True)
class Rules:
    """Entry rules of one list. `excluded` is matched against the offer's market and market_to_bet, as live."""
    min_odds: float = 1.15            # exclusive
    max_odds: float = 2.0             # inclusive
    excluded: frozenset = EXCLUDED_TODAY
    main_line_only: bool = False      # alternate AH lines excluded
    picks_per_group: int = 1
    one_per_match: bool = False
    value_ev_floor: float | None = None
    cagey_no_loss_floor: float | None = None
    cagey_ev_floor: float | None = None
    narrow_floor: float | None = None
    guard_ratio: float | None = 1.15  # cagey price guard; None = no guard
    ev_first: bool = False            # context only: order a group by expected return first


TODAY = Rules()


def scored(mass, price, cost=0.0) -> dict:
    """Probability of a positive return, of no loss, expected return and fair odds of one settlement
    distribution at one price (as profit_shortlist.annotate and cagey_market_basis.annotate compute them)."""
    mass = np.asarray(mass, float)
    returns = np.array([price - 1, (price - 1) / 2, 0, -.5, -1]) - cost
    win, loss = mass[0] + mass[1] / 2, mass[4] + mass[3] / 2
    return {'profit': float(mass[returns > 1e-12].sum()), 'no_loss': float(mass[returns >= -1e-12].sum()),
            'ev': float(mass @ returns), 'fair_odds': 1 + loss / win if win > 0 else math.inf}


def market_group(offer) -> str:
    import price_edge_cagey_shortlist as v28
    return v28.market_group(offer, rule=v28.VALUE_RULE_LOCAL_RESEARCH)


def is_binary(offer) -> bool:
    from cagey_market_basis import binary_market
    return binary_market(offer) is not None


def _excluded(offer, rules) -> bool:
    return (offer.get('market') in rules.excluded or offer.get('market_to_bet') in rules.excluded
            or (rules.main_line_only and bool(offer.get('alternate'))))


def _in_odds(price, rules) -> bool:
    return price is not None and rules.min_odds < price <= rules.max_odds


def value_eligible(offer, rules=TODAY) -> bool:
    if offer.get('blocked_value') or _excluded(offer, rules) or not _in_odds(offer.get('price'), rules):
        return False
    r = offer.get('r')
    if r is None:
        return False
    return rules.value_ev_floor is None or r['ev'] + TOLERANCE >= rules.value_ev_floor


def cagey_guard_fair(offer):
    """The price guard's fair odds: the independent Pinnacle reference for binary markets (None when it is
    unavailable, which never rejects), the cagey fair odds for every other AH line."""
    if is_binary(offer):
        return offer.get('binary_fair')
    return offer['c']['fair_odds'] if offer.get('c') is not None else None


def cagey_eligible(offer, rules=TODAY) -> bool:
    if offer.get('blocked_cagey') or _excluded(offer, rules) or not _in_odds(offer.get('price'), rules):
        return False
    c = offer.get('c')
    if c is None:
        return False
    if rules.guard_ratio is not None:
        fair = cagey_guard_fair(offer)
        if fair is not None and math.isfinite(fair) and offer['price'] > rules.guard_ratio * fair:
            return False
    if rules.cagey_no_loss_floor is not None and c['no_loss'] + TOLERANCE < rules.cagey_no_loss_floor:
        return False
    if rules.cagey_ev_floor is not None and c['ev'] + TOLERANCE < rules.cagey_ev_floor:
        return False
    if rules.narrow_floor is not None and (offer.get('p_narrow') is None
                                           or offer['p_narrow'] + TOLERANCE < rules.narrow_floor):
        return False
    return True


def value_key(offer, ev_first=False):
    r = offer['r']
    head = (-r['ev'], -r['profit']) if ev_first else (-r['profit'], -r['ev'])
    return (*head, -offer['price'], str(offer.get('market')), str(offer.get('bookmaker') or ''))


def cagey_key(offer, ev_first=False):
    c = offer['c']
    head = (-c['ev'], -c['no_loss']) if ev_first else (-c['no_loss'], -c['ev'])
    return (*head, -offer['price'], str(offer.get('market')), str(offer.get('bookmaker') or ''))


def _select(offers, eligible, key, rules):
    """One fixture's picks: per market group, the first `picks_per_group` by `key`; with `one_per_match`, the
    single first eligible offer. Returns (offer, rank within its group) pairs."""
    ranked = sorted((o for o in offers if eligible(o, rules)), key=lambda o: key(o, rules.ev_first))
    if rules.one_per_match:
        return [(ranked[0], 1)] if ranked else []
    out, seen = [], {}
    for offer in ranked:
        group = offer.get('group') or market_group(offer)  # live: market_group(item, rule=v2) for both lists
        seen[group] = seen.get(group, 0) + 1
        if seen[group] <= rules.picks_per_group:
            out.append((offer, seen[group]))
    return out


def value_select(offers, rules=TODAY):
    """The value shortlist's picks among one fixture's offers."""
    return _select(offers, value_eligible, value_key, rules)


def cagey_select(offers, rules=TODAY):
    """The cagey tier's picks among one fixture's offers."""
    return _select(offers, cagey_eligible, cagey_key, rules)


# ---------------------------------------------------------------------------
# Saved live runs: decision rows -> offers (the reproduction check)
# ---------------------------------------------------------------------------

# Live rejection reasons the selection functions express themselves; every other reason blocks the offer.
VALUE_EXPRESSED = ('offered odds must be greater than 1.15', 'offered odds above 2.00',
                   'market excluded by shortlist configuration', 'team goal-rate distribution unavailable at evaluation',
                   'higher profit-probability pick chosen in this market group')
CAGEY_EXPRESSED = ('cagey offered odds outside (1.15, 2.00]', 'market excluded by shortlist configuration',
                   'offered price above 1.15 x independent Pinnacle fair odds',
                   'offered price above 1.15 x corrected fair odds', 'corrected market settlement unavailable',
                   'uncorrected Pinnacle grid unavailable for Over 1.5', 'market outside cagey rule')


def _reasons(text):
    return [r for r in str(text or '').split('; ') if r and r != 'nan']


def _mass(row, prefix):
    values = [row.get(prefix + k) for k in KINDS]
    try:
        mass = np.array([float(v) for v in values])
    except (TypeError, ValueError):
        return None
    return mass if np.isfinite(mass).all() else None


def _number(value):
    try:
        out = float(value)
    except (TypeError, ValueError):
        return None
    return out if math.isfinite(out) else None


def decision_offers(decisions):
    """Offers per fixture from a run's decision rows (price_edge_cagey_shortlist.build_shortlist), with the live
    rejection reasons the selection functions can't express as `blocked_value` / `blocked_cagey`."""
    from performance_tracking import fixture_key
    fixtures = {}
    for index, row in zip(decisions.index, decisions.to_dict('records')):
        price = _number(row.get('offered_decimal_odds'))
        research, cagey = _mass(row, 'research_p_'), _mass(row, 'cagey_p_')
        line = _number(row.get('handicap_line'))
        offer = {'index': index, 'market': row.get('market'), 'market_to_bet': row.get('market_to_bet'),
                 'handicap_side': row.get('handicap_side'), 'handicap_line': line,
                 'bookmaker': row.get('bookmaker'), 'price': price,
                 'binary_fair': _number(row.get('price_guard_fair_odds')) if row.get('price_guard_status') != 'UNAVAILABLE' else None,
                 'r': scored(research, price) if research is not None and price else None,
                 'c': scored(cagey, price) if cagey is not None and price else None,
                 'blocked_value': any(r not in VALUE_EXPRESSED for r in _reasons(row.get('rejection_reasons'))),
                 'blocked_cagey': (row.get('cagey_tier_decision') is None
                                   or str(row.get('cagey_tier_decision')) == 'nan'
                                   or any(r not in CAGEY_EXPRESSED for r in _reasons(row.get('cagey_tier_reasons')))),
                 'value_live': row.get('decision') == 'SHORTLISTED',
                 'cagey_live': row.get('cagey_tier_decision') == 'SHORTLISTED'}
        fixtures.setdefault(fixture_key(row), []).append(offer)
    return fixtures


def reproduce(decisions, rules=TODAY) -> dict:
    """The harness's selection on a run's decision rows against the live lists: index sets and any difference."""
    out = {}
    fixtures = decision_offers(decisions)
    for name, select, flag in (('value', value_select, 'value_live'), ('cagey', cagey_select, 'cagey_live')):
        harness = {o['index'] for offers in fixtures.values() for o, _ in select(offers, rules)}
        live = {o['index'] for offers in fixtures.values() for o in offers if o[flag]}
        out[name] = {'live': len(live), 'harness': len(harness), 'same': harness == live,
                     'only_live': sorted(int(i) for i in live - harness),
                     'only_harness': sorted(int(i) for i in harness - live)}
    return out


def with_rules(**changes) -> Rules:
    return replace(TODAY, **changes)


# ---------------------------------------------------------------------------
# The audit's rule tests (docs/plan.md, Phase 4, "Shortlist entry audit", decided 14 Nov 2026)
# ---------------------------------------------------------------------------

DNB = frozenset({'Draw No Bet Home', 'Draw No Bet Away'})
DC_1X_X2 = frozenset({'Double Chance 1X', 'Double Chance X2'})
WINS = frozenset({'Home win', 'Away win'})


def _market_in(offer, markets):
    return offer.get('market') in markets or offer.get('market_to_bet') in markets


def _test(name, lists, today, removed, passes, looser, tighter, changes):
    """`removed`: the rules with this one removed (None: absent today, so pass/fail splits today's list by
    `passes`); `passes(offer, rank)`; `changes`: what the looser/tighter step changes (for the combined effect)."""
    return {'name': name, 'lists': lists, 'today': today, 'removed': removed, 'passes': passes,
            'looser': looser, 'tighter': tighter, 'changes': changes}


BOTH, VALUE, CAGEY = ('value', 'cagey'), ('value',), ('cagey',)
RULE_TESTS = (
    _test('lowest_odds', BOTH, 'offered odds > 1.15', with_rules(min_odds=1.0),
          lambda o, k: o['price'] > 1.15, with_rules(min_odds=1.10), with_rules(min_odds=1.20),
          {'looser': {'min_odds': 1.10}, 'tighter': {'min_odds': 1.20}}),
    _test('highest_odds', BOTH, 'offered odds <= 2.00', with_rules(max_odds=math.inf),
          lambda o, k: o['price'] <= 2.0, with_rules(max_odds=2.20), with_rules(max_odds=1.80),
          {'looser': {'max_odds': 2.20}, 'tighter': {'max_odds': 1.80}}),
    _test('draw_no_bet_excluded', BOTH, 'separate draw no bet quotes excluded', with_rules(excluded=EXCLUDED_TODAY - DNB),
          lambda o, k: not _market_in(o, DNB), with_rules(excluded=EXCLUDED_TODAY - DNB), None,
          {'looser': {'allow': sorted(DNB)}}),
    _test('double_chance_12_excluded', BOTH, 'double chance 12 excluded',
          with_rules(excluded=EXCLUDED_TODAY - {'Double Chance 12'}),
          lambda o, k: not _market_in(o, {'Double Chance 12'}), with_rules(excluded=EXCLUDED_TODAY - {'Double Chance 12'}),
          None, {'looser': {'allow': ['Double Chance 12']}}),
    _test('over_1_5_excluded', BOTH, 'Over 1.5 excluded', with_rules(excluded=EXCLUDED_TODAY - {'Over 1.5'}),
          lambda o, k: not _market_in(o, {'Over 1.5'}), with_rules(excluded=EXCLUDED_TODAY - {'Over 1.5'}), None,
          {'looser': {'allow': ['Over 1.5']}}),
    _test('double_chance_1x_x2_allowed', BOTH, 'double chance 1X and X2 allowed', None,
          lambda o, k: not _market_in(o, DC_1X_X2), None, with_rules(excluded=EXCLUDED_TODAY | DC_1X_X2),
          {'tighter': {'exclude': sorted(DC_1X_X2)}}),
    _test('alternate_ah_lines_allowed', BOTH, 'alternate AH lines allowed', None,
          lambda o, k: not o.get('alternate'), None, with_rules(main_line_only=True),
          {'tighter': {'main_line_only': True}}),
    _test('home_away_win_allowed', BOTH, 'home and away win allowed', None,
          lambda o, k: not _market_in(o, WINS), None, with_rules(excluded=EXCLUDED_TODAY | WINS),
          {'tighter': {'exclude': sorted(WINS)}}),
    _test('picks_per_match', BOTH, 'one pick per match and market group', with_rules(picks_per_group=99),
          lambda o, k: k == 1, with_rules(picks_per_group=2), with_rules(one_per_match=True),
          {'looser': {'picks_per_group': 2}, 'tighter': {'one_per_match': True}}),
    _test('order_within_group', BOTH, 'value: P(positive return), EV, odds; cagey: no-loss, EV, odds',
          with_rules(picks_per_group=2), lambda o, k: k == 1, None, None, {}),
    _test('value_ev_floor', VALUE, 'no research expected-return floor', None,
          lambda o, k: o['r']['ev'] + TOLERANCE >= 0, None, with_rules(value_ev_floor=0.0),
          {'tighter': {'value_ev_floor': 0.0}}),
    _test('cagey_no_loss_floor', CAGEY, 'no cagey no-loss floor', None,
          lambda o, k: o['c']['no_loss'] + TOLERANCE >= .75, None, with_rules(cagey_no_loss_floor=.75),
          {'tighter': {'cagey_no_loss_floor': .75}}),
    _test('cagey_ev_floor', CAGEY, 'no cagey expected-return floor', None,
          lambda o, k: o['c']['ev'] + TOLERANCE >= 0, None, with_rules(cagey_ev_floor=0.0),
          {'tighter': {'cagey_ev_floor': 0.0}}),
    _test('cagey_narrow_gate', CAGEY, 'no P(narrow) gate', None,
          lambda o, k: o.get('p_narrow') is not None and o['p_narrow'] + TOLERANCE >= .67, None,
          with_rules(narrow_floor=.67), {'tighter': {'narrow_floor': .67}}),
    _test('cagey_price_guard', CAGEY, 'offered <= 1.15 x independent fair (binary) or cagey fair (other AH)',
          with_rules(guard_ratio=None),
          lambda o, k: (lambda f: f is None or not math.isfinite(f) or o['price'] <= 1.15 * f)(cagey_guard_fair(o)),
          with_rules(guard_ratio=1.20), with_rules(guard_ratio=1.10),
          {'looser': {'guard_ratio': 1.20}, 'tighter': {'guard_ratio': 1.10}}),
)


def combined_rules(changes) -> Rules:
    """Today's rules with every adopted step applied together (`changes`: the steps' `changes` dicts)."""
    rules, excluded = TODAY, set(EXCLUDED_TODAY)
    for change in changes:
        for key, value in change.items():
            if key == 'allow':
                excluded -= set(value)
            elif key == 'exclude':
                excluded |= set(value)
            else:
                rules = replace(rules, **{key: value})
    return replace(rules, excluded=frozenset(excluded))


def clearly(difference, side):
    """'above' or 'below': the 95% interval lies entirely on that side of zero."""
    if not difference or not difference.get('interval_95'):
        return False
    low, high = difference['interval_95']
    return low > 0 if side == 'above' else high < 0


def _point(difference):
    return None if not difference else difference.get('value')


def verdict(development, validation) -> dict:
    """The decided verdict for one rule and list: tighten > keep > loosen > no evidence on development; validation
    must point the same way (keep/tighten: point estimate above zero; loosen: not clearly worse and adds
    coverage)."""
    def call(period):
        if period is None:
            return 'no evidence'
        if clearly(period.get('tighter_minus_today'), 'above'):
            return 'tighten'
        if clearly(period.get('pass_minus_fail'), 'above'):
            return 'keep'
        looser = period.get('looser_minus_today')
        if looser and not clearly(looser, 'below') and period.get('looser_adds_coverage'):
            return 'loosen'
        return 'no evidence'
    first = call(development)
    if first == 'no evidence':
        return {'verdict': first, 'development': first}
    if validation is None:
        return {'verdict': 'no evidence (no validation)', 'development': first}
    if first == 'tighten':
        same = (_point(validation.get('tighter_minus_today')) or 0) > 0
    elif first == 'keep':
        same = (_point(validation.get('pass_minus_fail')) or 0) > 0
    else:
        same = (bool(validation.get('looser_minus_today')) and not clearly(validation['looser_minus_today'], 'below')
                and bool(validation.get('looser_adds_coverage')))
    return {'verdict': first if same else 'no evidence (validation disagrees)', 'development': first,
            'validation_same_way': same}
