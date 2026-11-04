"""Versioned shortlist v27: Asian handicap price edge against Pinnacle's fair price.

Candidates are every AH line, main and alternate, both sides, at the allowed
bookmakers, plus markets that settle identically to an AH line:
home -0.5 = 1X2 home, away -0.5 = 1X2 away, home +0.5 = double chance 1X,
away +0.5 = double chance X2, AH 0 = draw no bet. The draw is never a pick.

Fair reference, in order (the first available one is used):
  a) Pinnacle on the same AH line, two-way margin removed (proportional; Shin recorded);
  b) Pinnacle's equivalent market: 1X2 for the +/-0.5 lines, draw no bet for 0;
  c) the market-implied matrix (market_implied fit B), ONLY for plus lines and
     only when the fit is usable ("derived").
Otherwise the candidate is rejected: no Pinnacle reference (fail closed).

Edge = offered odds x fair win-share - 1 (refunds excluded). Qualify at
>= 2% for a/b and >= 3% for c. One row per fixture: the qualifying candidate
with the highest Pinnacle no-loss probability. No model EV, no no-loss floor.
The production model's gap to Pinnacle is recorded for information only.

Narrow-margin tags (balanced, low_total, high_draw, even_odds) and the cagey score
(market-implied P(2+ goal margin), fit B else fit A) are tracking only: they
never change a decision. Tagged fixtures always get their +1 to +2.25 lines
evaluated so rejections are recorded too. v26 and older stay replayable.
"""

from __future__ import annotations

import json
import math
from typing import Dict, List, Mapping, Optional, Tuple

import numpy as np
import pandas as pd

import market_implied as mi
from ah_close_backtest import devig_proportional, devig_shin, settle
from quote_freshness import quote_is_fresh, quote_utc

POLICY = '48h-ah-price-edge-pinnacle-ref-v27'
OBJECTIVE = 'AH_PRICE_EDGE_VS_PINNACLE'
# Selection never reads the model's goal-market walk-forward or count-market validation.
VALIDATION_REQUIRED = False
MIN_EDGE = 0.02
MIN_EDGE_DERIVED = 0.03
EDGE_TOLERANCE = 1e-9
MAX_HOURS = 48.0
MIN_MINUTES = 20.0
MAX_QUOTE_SKEW_MINUTES = 10.0
PINNACLE_OVERROUND = (1.00, 1.10)
MAX_FAIR_RATIO = 1.15
MAX_ODDS = 3.00
BALANCED_ODDS = (2.00, 3.50)
EVEN_ODDS_MIN = 2.50  # even_odds: both raw Pinnacle 1X2 win odds at least this.
LOW_TOTAL = 0.45
HIGH_DRAW = 0.27
TAGS = ('balanced', 'low_total', 'high_draw', 'even_odds')
TAGGED_LINES = (1.0, 1.5, 1.75, 2.0, 2.25)
REFERENCES = {'a': 'Pinnacle same AH line', 'b': 'Pinnacle equivalent market', 'c': 'market-implied (derived)'}
NO_REFERENCE = 'no Pinnacle reference'
NO_OFFER = 'no offered quote at an allowed bookmaker'
# Totals lines kept from the captured responses: 2.5 feeds the fit; 1.5 is priced by v28's per-market rule.
CAPTURED_TOTAL_POINTS = (2.5, 1.5)
OUTPUT_COLUMNS = [
    'kickoff_utc', 'league', 'home_team', 'away_team', 'balanced', 'low_total', 'high_draw', 'even_odds',
    'pinnacle_draw_probability', 'pinnacle_over_2_5_probability', 'handicap_line', 'handicap_side', 'side_role',
    'market_to_bet', 'bookmaker', 'offered_decimal_odds', 'fair_odds', 'reference_type', 'edge',
    'minimum_odds', 'pinnacle_no_loss_probability', 'offered_quote_age_minutes', 'pinnacle_quote_age_minutes',
    'model_vs_pinnacle_gap', 'cagey_score', 'cagey_fit', 'other_value_lines']
DECISION_COLUMNS = [
    'evaluated_at_utc', 'date', 'league', 'home_team', 'away_team', 'fixture_id', 'kickoff_utc',
    'market', 'market_to_bet', 'ah_equivalent', 'handicap_side', 'handicap_line', 'side_role', 'source_market',
    'bookmaker', 'offered_decimal_odds', 'offered_last_update_utc', 'offered_quote_age_minutes',
    'reference_type', 'reference_market', 'pinnacle_last_update_utc', 'pinnacle_quote_age_minutes',
    'quote_skew_minutes', 'pinnacle_overround', 'fair_probability', 'fair_probability_shin', 'fair_odds',
    'edge', 'edge_shin', 'min_edge', 'minimum_odds', 'pinnacle_no_loss_probability', 'p_no_loss',
    'predicted_probability', 'rank_probability', 'probability_basis', 'model_win_share', 'model_vs_pinnacle_gap',
    'balanced', 'low_total', 'high_draw', 'even_odds', 'any_tag', 'tagged_probe', 'cagey_score', 'cagey_fit', 'pinnacle_home_odds', 'pinnacle_away_odds',
    'pinnacle_draw_probability', 'pinnacle_over_2_5_probability', 'fit_usable', 'fit_reasons', 'fit_max_residual',
    'per_stake_cost', 'decision', 'rejection_reasons', 'selection_tier', 'other_value_lines', 'selection_policy_version']


# ---------------------------------------------------------------------------
# Quotes
# ---------------------------------------------------------------------------

def _price(value) -> Optional[float]:
    try:
        price = float(value)
    except (TypeError, ValueError):
        return None
    return price if math.isfinite(price) and price > 1 and not isinstance(value, bool) else None


def _json_list(value) -> list:
    try:
        data = json.loads(value) if isinstance(value, str) else value
    except (TypeError, ValueError):
        return []
    return data if isinstance(data, list) else []


def capture_quotes(payload: Mapping, clock, market_keys) -> List[Dict[str, object]]:
    """Per-book quotes v27 needs beyond the AH offers: complete, fresh outcome sets only.

    h2h (home/draw/away), totals and alternate_totals at 2.5 and 1.5 (over/under; one quote per point) and
    double_chance (home_draw/draw_away/home_away), for the bookmakers
    asian_handicap.bookmaker recognises. No price is ever synthesised.
    """
    from asian_handicap import bookmaker
    from double_chance import outcome_labels
    from football_value_pipeline_v2_standalone import canonical_team_key
    home, away = payload.get('home_team'), payload.get('away_team')
    if not isinstance(home, str) or not isinstance(away, str) or home == away:
        return []
    names = {'h2h': {canonical_team_key(home): 'home', canonical_team_key(away): 'away', 'draw': 'draw'},
             'double_chance': outcome_labels(home, away)}
    wanted = {'h2h': {'home', 'draw', 'away'}, 'double_chance': {'home_draw', 'draw_away', 'home_away'},
              'totals': {'over', 'under'}, 'alternate_totals': {'over', 'under'}}
    out = []
    books = payload.get('bookmakers')
    for book in books if isinstance(books, list) else []:
        if not isinstance(book, dict):
            continue
        name = bookmaker(book.get('title') or book.get('key'))
        markets = book.get('markets')
        if name is None or not isinstance(markets, list):
            continue
        for market in markets:
            key = market.get('key') if isinstance(market, dict) else None
            if key not in market_keys or key not in wanted or not isinstance(market.get('outcomes'), list):
                continue
            stamp = market.get('last_update') or book.get('last_update')
            if clock is not None and not quote_is_fresh(stamp, clock):
                continue
            points = CAPTURED_TOTAL_POINTS if 'totals' in key else (None,)
            for point in points:
                quote = _capture_one(market, key, point, names, wanted, name, stamp)
                if quote is not None:
                    out.append(quote)
    return out


def _capture_one(market, key, point, names, wanted, name, stamp) -> Optional[Dict[str, object]]:
    """One complete outcome set of one market (one totals point at a time), or None."""
    from football_value_pipeline_v2_standalone import canonical_team_key
    prices, duplicate = {}, False
    for outcome in market['outcomes']:
        if not isinstance(outcome, dict):
            continue
        label = str(outcome.get('name') or '').strip()
        if key in ('totals', 'alternate_totals'):
            if outcome.get('point') != point:
                continue
            side = label.lower()
        elif key == 'h2h':
            side = names['h2h'].get('draw' if label.lower() == 'draw' else canonical_team_key(label))
        else:
            side = names['double_chance'].get(label.casefold())
        price = _price(outcome.get('price'))
        if side in wanted[key] and price:
            duplicate |= side in prices
            prices[side] = price
    if duplicate or set(prices) != wanted[key]:
        return None
    return {'bookmaker': name, 'market': 'totals' if 'totals' in key else key, 'market_key': key,
            'point': point, 'prices': prices, 'last_update_utc': stamp}


def merge_quotes(existing, added) -> str:
    """Union of captured quote lists; the newest quote wins per book, market and key."""
    merged = {}
    for quote in sorted(_json_list(existing) + _json_list(added), key=lambda q: str(q.get('last_update_utc'))):
        merged[(quote.get('bookmaker'), quote.get('market'), quote.get('market_key'), quote.get('point'))] = quote
    return json.dumps(list(merged.values()), sort_keys=True, allow_nan=False)


def _ah_market(side: str, line: float) -> str:
    from asian_handicap import label
    return label(side, line)


def pinnacle_quotes(row: Mapping) -> Dict[str, object]:
    """Pinnacle 1X2, O/U 2.5 (and O/U 1.5, used only by v28's per-market rule), AH pairs and draw no bet.

    Prefers the per-book `price_edge_quotes` capture; runs captured before it
    existed fall back to fields that are Pinnacle by construction.
    """
    out: Dict[str, object] = {'h2h': None, 'ou25': None, 'ou15': None, 'ah': {}, 'dnb': None, 'main_line': None}
    for quote in _json_list(row.get('price_edge_quotes')):
        if not isinstance(quote, dict) or quote.get('bookmaker') != 'Pinnacle':
            continue
        prices, stamp = quote.get('prices') or {}, quote.get('last_update_utc')
        if quote.get('market') == 'h2h':
            triple = tuple(_price(prices.get(k)) for k in ('home', 'draw', 'away'))
            if all(triple):
                out['h2h'] = (*triple, stamp)
        elif quote.get('market') == 'totals' and quote.get('point') in (2.5, 1.5):
            key = 'ou25' if quote.get('point') == 2.5 else 'ou15'
            pair = (_price(prices.get('over')), _price(prices.get('under')))
            # Prefer the main line over the alternate one when both exist.
            if all(pair) and (out[key] is None or quote.get('market_key') == 'totals'):
                out[key] = (*pair, stamp)
    if out['h2h'] is None and str(row.get('market_source_1x2') or '').endswith('/ Pinnacle'):
        triple = tuple(_price(row.get(f'market_reference_{k}_odds')) for k in ('home', 'draw', 'away'))
        if all(triple):
            out['h2h'] = (*triple, row.get('market_reference_1x2_last_update_utc'))
    if out['ou25'] is None:
        if 'pinnacle' in str(row.get('totals_anchor_reference_source') or '').lower():
            pair = (_price(row.get('totals_anchor_reference_over_odds')),
                    _price(row.get('totals_anchor_reference_under_odds')))
            if all(pair):
                out['ou25'] = (*pair, row.get('totals_anchor_reference_last_update_utc'))
        elif str(row.get('market_source_ou25') or '').endswith('/ Pinnacle'):
            pair = (_price(row.get('market_reference_over_2_5_odds')), _price(row.get('market_reference_under_2_5_odds')))
            if all(pair):
                out['ou25'] = (*pair, row.get('market_reference_over_2_5_last_update_utc'))
    main = []
    for offer in _json_list(row.get('asian_handicap_offers')):
        if not isinstance(offer, dict) or offer.get('bookmaker') != 'Pinnacle' or offer.get('side') != 'home':
            continue
        price, opposite, line = _price(offer.get('price')), _price(offer.get('opposite_price')), offer.get('line')
        if not (price and opposite) or line is None:
            continue
        pair = (price, opposite, offer.get('last_update_utc'))
        if offer.get('market_key') == 'draw_no_bet':
            out['dnb'] = pair
            continue
        out['ah'][float(line)] = pair
        main.append((offer.get('market_key') != 'spreads', abs(price - opposite), float(line)))
    if main:
        # The quoted main line; when deduplication kept only the alternate
        # copy of it, the most balanced Pinnacle pair (which is the main line).
        out['main_line'] = min(main)[2]
    return out


def offered_candidates(row: Mapping, policy: Mapping) -> List[Dict[str, object]]:
    """Every allowed-book quote that settles as an AH line, with its market label."""
    from quote_policy import usable_bookmaker
    from asian_handicap import bookmaker, line as valid_line
    items = []
    for offer in _json_list(row.get('asian_handicap_offers')):
        if not isinstance(offer, dict):
            continue
        name, price = bookmaker(offer.get('bookmaker')), _price(offer.get('price'))
        try:
            side, point = offer['side'], valid_line(offer['line'])
        except (KeyError, TypeError, ValueError):
            continue
        if name is None or price is None or side not in ('home', 'away') or not usable_bookmaker(name, policy):
            continue
        dnb = offer.get('market_key') == 'draw_no_bet'
        items.append({'side': side, 'line': point, 'bookmaker': name, 'price': price,
                      'stamp': offer.get('last_update_utc'), 'source_market': offer.get('market_key'),
                      'market': _ah_market(side, point),
                      'market_to_bet': f'Draw No Bet {side.title()}' if dnb else _ah_market(side, point)})
    equivalents = {('h2h', 'home'): ('home', -0.5, 'Home win'), ('h2h', 'away'): ('away', -0.5, 'Away win'),
                   ('double_chance', 'home_draw'): ('home', 0.5, 'Double Chance 1X'),
                   ('double_chance', 'draw_away'): ('away', 0.5, 'Double Chance X2')}
    for quote in _json_list(row.get('price_edge_quotes')):
        if not isinstance(quote, dict) or not usable_bookmaker(str(quote.get('bookmaker') or ''), policy):
            continue
        for key, price in (quote.get('prices') or {}).items():
            target = equivalents.get((quote.get('market'), key))
            if target and _price(price):
                side, point, market = target
                items.append({'side': side, 'line': point, 'bookmaker': quote['bookmaker'], 'price': _price(price),
                              'stamp': quote.get('last_update_utc'), 'source_market': quote.get('market'),
                              'market': market, 'market_to_bet': market})
    if not _json_list(row.get('price_edge_quotes')):
        # Runs captured before price_edge_quotes: the best allowed-book 1X2/DC price on the row.
        for key, side, point, market in (('home', 'home', -0.5, 'Home win'), ('away', 'away', -0.5, 'Away win'),
                                         ('home_draw', 'home', 0.5, 'Double Chance 1X'),
                                         ('draw_away', 'away', 0.5, 'Double Chance X2')):
            name, price = row.get(f'best_{key}_bookmaker'), _price(row.get(f'market_{key}_odds'))
            if isinstance(name, str) and price and usable_bookmaker(name, policy):
                items.append({'side': side, 'line': point, 'bookmaker': name, 'price': price,
                              'stamp': row.get(f'market_best_{key}_last_update_utc'),
                              'source_market': 'h2h' if '_' not in key else 'double_chance',
                              'market': market, 'market_to_bet': market})
    return items


# ---------------------------------------------------------------------------
# Fixture context: tags, fit, references
# ---------------------------------------------------------------------------

def tag_flags(home_odds=None, away_odds=None, draw_probability=None, over_probability=None) -> Dict[str, bool]:
    """balanced: both 1X2 odds in [2.00, 3.50]; low_total: P(over 2.5) < 0.45; high_draw: draw >= 0.27;
    even_odds: both raw 1X2 win odds >= 2.50."""
    low, high = BALANCED_ODDS
    return {'even_odds': home_odds is not None and away_odds is not None
                         and home_odds >= EVEN_ODDS_MIN and away_odds >= EVEN_ODDS_MIN,
            'balanced': home_odds is not None and away_odds is not None
                        and low <= home_odds <= high and low <= away_odds <= high,
            'low_total': over_probability is not None and over_probability < LOW_TOTAL,
            'high_draw': draw_probability is not None and draw_probability >= HIGH_DRAW}


def tags(h2h, ou25) -> Dict[str, object]:
    """Tracking tags from Pinnacle's current prices; never used in a decision."""
    home = away = draw_p = over = None
    if h2h is not None:
        home, away = h2h[0], h2h[2]
        draw_p = mi.devig_three_way(*h2h[:3])[1]
    if ou25 is not None:
        over = devig_proportional(ou25[0], ou25[1])[0]
    out = {**tag_flags(home, away, draw_p, over), 'pinnacle_home_odds': home, 'pinnacle_away_odds': away,
           'pinnacle_draw_probability': draw_p, 'pinnacle_over_2_5_probability': over}
    out['any_tag'] = any(out[t] for t in TAGS)
    return out


def _overround(*prices) -> float:
    return sum(1 / p for p in prices)


FUTURE_INPUT_REASON = 'input timestamped after evaluation'


def market_fit(pin: Mapping, now: pd.Timestamp, cutoff: bool = False) -> Tuple[mi.Fit, Dict[str, object]]:
    """Fit B on Pinnacle's current 1X2, O/U 2.5 and main AH line.

    `cutoff` (v28 observed-by-cutoff-v2): a fit with any input stamped after `now` is unusable, so no
    ranking, settlement, staking, correction or monitoring figure can depend on a future quote.
    """
    h2h, ou, line = pin['h2h'], pin['ou25'], pin['main_line']
    ah = (line, *pin['ah'][line][:2]) if line is not None else None
    targets = mi.targets_from_prices(h2h[:3] if h2h else None, ou[:2] if ou else None, ah)
    stamps = {'h2h': h2h[3] if h2h else None, 'ou25': ou[2] if ou else None,
              'ah_main': pin['ah'][line][2] if line is not None else None}
    groups = {'h2h': h2h[:3] if h2h else None, 'ou25': ou[:2] if ou else None,
              'ah_main': pin['ah'][line][:2] if line is not None else None}
    stale = [k for k, v in stamps.items() if groups[k] is not None and not quote_is_fresh(v, now)]
    low, high = PINNACLE_OVERROUND
    bad = [k for k, g in groups.items() if g is not None and not low <= _overround(*g) <= high]
    result = mi.fit(targets, include_ah=True, stale=stale)
    future = [k for k, v in stamps.items() if cutoff and groups[k] is not None
              and quote_utc(v) is not None and quote_utc(v) > now]
    if future:
        result.usable = False
        result.reasons.append(FUTURE_INPUT_REASON + ': ' + ', '.join(future))
    if bad:
        result.usable = False
        result.reasons.append('Pinnacle overround outside range: ' + ', '.join(bad))
    # Fit A (1X2 + O/U only) is a fallback for the cagey score; it never prices a candidate.
    fit_a = mi.fit(targets, include_ah=False, stale=[k for k in stale if k != 'ah_main'])
    if any(k != 'ah_main' for k in bad):
        fit_a.usable = False
    if any(k != 'ah_main' for k in future):
        fit_a.usable = False
        fit_a.reasons.append(FUTURE_INPUT_REASON + ': ' + ', '.join(k for k in future if k != 'ah_main'))
    return result, {'stamps': [s for s in stamps.values() if s], 'input_stamps': stamps, 'fit_a': fit_a,
                    'overrounds': {k: _overround(*g) for k, g in groups.items() if g}}


def reference(side: str, line: float, pin: Mapping, fit: mi.Fit, fit_info: Mapping) -> Optional[Dict[str, object]]:
    """First available fair reference for `side` getting `line`, or None (fail closed)."""
    home_line = line if side == 'home' else -line
    pair = pin['ah'].get(home_line)
    if pair is not None:
        home, away, stamp = pair
        prices = (home, away) if side == 'home' else (away, home)
        return {'type': 'a', 'market': f'Pinnacle AH {home_line:+.2f}', 'q': devig_proportional(*prices)[0],
                'q_shin': devig_shin(*prices)[0], 'stamps': [stamp], 'overround': _overround(*prices)}
    if abs(line) == 0.5 and pin['h2h'] is not None:
        home, draw, away, stamp = pin['h2h']
        p_home, _, p_away = mi.devig_three_way(home, draw, away)
        mine, theirs = (p_home, p_away) if side == 'home' else (p_away, p_home)
        return {'type': 'b', 'market': 'Pinnacle 1X2', 'q': mine if line < 0 else 1 - theirs, 'q_shin': None,
                'stamps': [stamp], 'overround': _overround(home, draw, away)}
    if line == 0 and pin['dnb'] is not None:
        home, away, stamp = pin['dnb']
        prices = (home, away) if side == 'home' else (away, home)
        return {'type': 'b', 'market': 'Pinnacle draw no bet', 'q': devig_proportional(*prices)[0],
                'q_shin': devig_shin(*prices)[0], 'stamps': [stamp], 'overround': _overround(*prices)}
    if line > 0 and fit.usable:
        priced = mi.price(fit, side, line)
        return {'type': 'c', 'market': 'market-implied fit B', 'q': priced['win_share'], 'q_shin': None,
                'stamps': list(fit_info['stamps']), 'overround': max(fit_info['overrounds'].values())}
    return None


def no_loss(side: str, line: float, fit: mi.Fit, q: Optional[float]) -> Optional[float]:
    """Pinnacle no-loss probability: from fit B when usable; on half lines it is the win-share."""
    if fit.usable:
        return mi.price(fit, side, line)['p_no_loss']
    if q is not None and round(line * 4) % 4 == 2:
        return q
    return None


def model_win_share(row: Mapping, side: str, line: float) -> Optional[float]:
    """Production model win-share on this line (information only)."""
    from asian_handicap import distribution
    try:
        dist = distribution(row.get('goal_margin_distribution'))
    except (TypeError, ValueError):
        return None
    margins = np.array(list(dist), dtype=float)
    probs = np.array(list(dist.values()), dtype=float)
    won, lost = settle(margins if side == 'home' else -margins, line)
    w, lo = float((probs * won).sum()), float((probs * lost).sum())
    return w / (w + lo) if w + lo > 0 else None


def _age_minutes(stamp, now) -> Optional[float]:
    when = quote_utc(stamp)
    return None if when is None else (now - when).total_seconds() / 60


# ---------------------------------------------------------------------------
# Evaluation
# ---------------------------------------------------------------------------

def evaluate_candidate(candidate: Mapping, pin: Mapping, fit: mi.Fit, fit_info: Mapping, context: Mapping,
                       now: pd.Timestamp, kickoff: Optional[pd.Timestamp]) -> Dict[str, object]:
    side, line = candidate['side'], float(candidate['line'])
    reasons = []
    if kickoff is None or not now + pd.Timedelta(minutes=MIN_MINUTES) <= kickoff <= now + pd.Timedelta(hours=MAX_HOURS):
        reasons.append('kickoff outside 20-minute to 48-hour window')
    ref = reference(side, line, pin, fit, fit_info)
    price = candidate.get('price')
    item = {'handicap_side': side, 'handicap_line': line, 'market': candidate.get('market') or _ah_market(side, line),
            'market_to_bet': candidate.get('market_to_bet') or _ah_market(side, line),
            'ah_equivalent': _ah_market(side, line), 'source_market': candidate.get('source_market'),
            'bookmaker': candidate.get('bookmaker'), 'offered_decimal_odds': price,
            'offered_last_update_utc': candidate.get('stamp'), 'offered_quote_age_minutes': _age_minutes(candidate.get('stamp'), now),
            'tagged_probe': bool(candidate.get('probe')),
            'side_role': ('favourite' if (context['favourite'] == side) else 'underdog') if context['favourite'] else None}
    if price is None:
        reasons.append(NO_OFFER)
    elif not quote_is_fresh(candidate.get('stamp'), now):
        reasons.append('offered quote stale')
    if ref is None:
        reasons.append(NO_REFERENCE)
        item.update(fair_probability=None, fair_odds=None, edge=None, reference_type=None)
    else:
        q = ref['q']
        threshold = MIN_EDGE_DERIVED if ref['type'] == 'c' else MIN_EDGE
        fair_odds = 1 / q if q > 0 else math.inf
        item.update(reference_type=ref['type'], reference_market=ref['market'], fair_probability=q,
                    fair_probability_shin=ref['q_shin'], fair_odds=fair_odds, min_edge=threshold,
                    minimum_odds=fair_odds * (1 + threshold), pinnacle_overround=ref['overround'],
                    pinnacle_last_update_utc=max(ref['stamps'], key=lambda s: quote_utc(s) or pd.Timestamp.min.tz_localize('UTC'))
                    if ref['stamps'] else None)
        ages = [_age_minutes(s, now) for s in ref['stamps']]
        item['pinnacle_quote_age_minutes'] = max((a for a in ages if a is not None), default=None)
        if not ref['stamps'] or not all(quote_is_fresh(s, now) for s in ref['stamps']):
            reasons.append('Pinnacle quote stale')
        low, high = PINNACLE_OVERROUND
        if not low <= ref['overround'] <= high:
            reasons.append('Pinnacle overround outside [1.00, 1.10]')
        if price is not None:
            edge = price * q - 1
            item['edge'] = edge
            item['edge_shin'] = price * ref['q_shin'] - 1 if ref['q_shin'] is not None else None
            offered = quote_utc(candidate.get('stamp'))
            skews = [abs((offered - quote_utc(s)).total_seconds()) / 60 for s in ref['stamps']
                     if offered is not None and quote_utc(s) is not None]
            item['quote_skew_minutes'] = max(skews, default=None)
            if not skews or max(skews) > MAX_QUOTE_SKEW_MINUTES:
                reasons.append('offered and Pinnacle quotes more than 10 minutes apart')
            if price > MAX_FAIR_RATIO * fair_odds:
                reasons.append('offered price above 1.15 x fair odds')
            if price > MAX_ODDS:
                reasons.append('offered odds above 3.00')
            if edge + EDGE_TOLERANCE < threshold:
                reasons.append(f'edge below {threshold:.0%}')
    q = item.get('fair_probability')
    p_safe = no_loss(side, line, fit, q)
    model_q = model_win_share(context['row'], side, line)
    item.update(pinnacle_no_loss_probability=p_safe, p_no_loss=p_safe, rank_probability=p_safe,
                predicted_probability=q, probability_basis='pinnacle_fair_win_share',
                model_win_share=model_q, model_vs_pinnacle_gap=None if model_q is None or q is None else model_q - q,
                rejection_reasons='; '.join(dict.fromkeys(reasons)), decision='REJECTED' if reasons else 'ELIGIBLE')
    return item


def evaluate_fixture(row: Mapping, policy: Mapping, now: pd.Timestamp, transform=None,
                     cutoff: bool = False) -> List[Dict[str, object]]:
    """Every candidate of one fixture. `transform(row, items, pin, fit, fit_info, now)` lets a later
    policy (v28) post-process the rows with the same Pinnacle quotes and fits; v27 passes none."""
    pin = pinnacle_quotes(row)
    fit, fit_info = market_fit(pin, now, cutoff)
    tag = tags(pin['h2h'], pin['ou25'])
    favourite = None
    if pin['h2h'] is not None:
        favourite = 'home' if pin['h2h'][0] < pin['h2h'][2] else 'away' if pin['h2h'][2] < pin['h2h'][0] else None
    kickoff = quote_utc(row.get('kickoff_utc'))
    context = {'row': row, 'favourite': favourite}
    candidates = offered_candidates(row, policy)
    if tag['any_tag']:
        offered = {(c['side'], float(c['line'])) for c in candidates}
        candidates += [{'side': side, 'line': line, 'probe': True} for side in ('home', 'away')
                       for line in TAGGED_LINES if (side, line) not in offered]
    base = fixture_base(row, pin, fit, fit_info, now)
    items = [{**base, **evaluate_candidate(c, pin, fit, fit_info, context, now, kickoff)} for c in candidates]
    return transform(row, items, pin, fit, fit_info, now) if transform is not None else items


def fixture_base(row: Mapping, pin: Mapping, fit: mi.Fit, fit_info: Mapping, now: pd.Timestamp) -> Dict[str, object]:
    """Fields every candidate row of one fixture shares (identity, fit diagnostics, tracking tags)."""
    base = {k: row.get(k) for k in ('date', 'league', 'home_team', 'away_team', 'fixture_id', 'kickoff_utc')}
    base.update(evaluated_at_utc=now.isoformat(), selection_policy_version=POLICY, per_stake_cost=0.0,
                fit_usable=fit.usable, fit_reasons='; '.join(fit.reasons), fit_max_residual=fit.max_residual,
                **tags(pin['h2h'], pin['ou25']))
    # Tracking only: never read by any decision.
    base['cagey_score'], base['cagey_fit'] = mi.cagey_score(fit, fit_info['fit_a'])
    return base


def _rank(frame: pd.DataFrame) -> pd.DataFrame:
    """Safest first: Pinnacle no-loss probability, then edge, then odds."""
    return frame.assign(_safe=frame.pinnacle_no_loss_probability.astype(float).fillna(-1.0)).sort_values(
        ['_safe', 'edge', 'offered_decimal_odds', 'kickoff_utc', 'market', 'bookmaker'],
        ascending=[False, False, False, True, True, True], kind='stable').drop(columns='_safe')


def build_shortlist(predictions: pd.DataFrame, as_of, market_reliability=None, execution_policy=None, *,
                    transform=None, extra_columns=(), group_column=None, cutoff=False):
    """One pick per fixture; no cap. Returns (shortlist, decisions, summary).

    `transform`, `extra_columns` and `group_column` are for v28, which reuses this selection; v27 uses none.
    With `group_column`, the pick is one per fixture AND value of that column (one per market group).
    """
    from quote_policy import load_policy, validate_policy
    from performance_tracking import fixture_key
    now = pd.Timestamp(as_of)
    if now.tzinfo is None:
        raise ValueError('as_of must be timezone-aware')
    now = now.tz_convert('UTC')
    policy = load_policy() if execution_policy is None else validate_policy(dict(execution_policy))
    rows = predictions.astype(object).where(predictions.notna(), None).to_dict('records') if len(predictions) else []
    evaluated = [item for row in rows for item in evaluate_fixture(row, policy, now, transform, cutoff)]
    decisions = pd.DataFrame(evaluated).reindex(columns=[*DECISION_COLUMNS, *extra_columns])
    for column in ('selection_tier', 'other_value_lines', 'rejection_reasons', 'decision'):
        decisions[column] = decisions[column].astype(object)
    eligible =decisions.loc[decisions.decision == 'ELIGIBLE'].copy()
    eligible['_fixture'] = eligible.apply(fixture_key, axis=1) if len(eligible) else pd.Series(dtype=str)
    if group_column is not None and len(eligible):
        eligible['_fixture'] = eligible['_fixture'] + '#' + eligible[group_column].astype(str)
    ranked = _rank(eligible)
    chosen = ranked.drop_duplicates('_fixture').index
    others = {}
    for idx in chosen:
        group = ranked.loc[(ranked._fixture == ranked.at[idx, '_fixture']) & (ranked.index != idx)]
        others[idx] = '; '.join(f'{r.market_to_bet} @ {r.bookmaker} {r.offered_decimal_odds:.2f} ({r.edge:+.1%})'
                                for r in group.itertuples())
    decisions.loc[eligible.index, 'decision'] = 'NOT_SELECTED'
    decisions.loc[eligible.index, 'rejection_reasons'] = (
        'other qualifying line chosen for this fixture (safest first)' if group_column is None
        else 'other qualifying line chosen for this fixture and market group (safest first)')
    decisions.loc[chosen, ['decision', 'rejection_reasons', 'selection_tier']] = ['SHORTLISTED', '', 'STRICT']
    for idx, text in others.items():
        decisions.at[idx, 'other_value_lines'] = text
    selected = _rank(decisions.loc[chosen]).reset_index(drop=True)
    rejected = decisions.loc[decisions.decision == 'REJECTED', 'rejection_reasons']
    reasons = pd.Series([r for text in rejected for r in str(text).split('; ') if r]).value_counts()
    tagged = decisions.loc[decisions.any_tag.fillna(False).astype(bool)]
    fixtures = int(predictions.apply(fixture_key, axis=1).nunique()) if len(predictions) else 0
    summary = {
        'generated_at_utc': now.isoformat(), 'selection_policy_version': POLICY, 'selection_objective': OBJECTIVE,
        'status': 'BELOW_TARGET' if len(selected) else 'NO BET', 'n_fixtures': len(predictions),
        'n_markets_evaluated': len(decisions), 'n_shortlisted': len(selected), 'n_strict_qualified': len(selected),
        'n_provisional_watchlist': 0, 'n_total_candidates': len(selected), 'target_distinct_matches': None,
        'shortfall': None, 'usable_distinct_fixtures': fixtures,
        'shortlist_lookahead_hours': MAX_HOURS, 'selected_matches_within_48_hours': bool(len(selected)),
        'shortlist_window_start_utc': now.isoformat(),
        'shortlist_window_end_utc': (now + pd.Timedelta(hours=MAX_HOURS)).isoformat(),
        'eligible_markets': ['Home win', 'Away win', 'Double Chance 1X', 'Double Chance X2'] + [
            _ah_market(s, p) for s in ('home', 'away') for p in __import__('asian_handicap').LINES],
        'quote_execution_policy': policy, 'validation_required': VALIDATION_REQUIRED,
        # Information only: v27 does not use the model's market audits to select.
        'validation_market_statuses': {league: {key: state.get('status', 'INSUFFICIENT_HISTORY')
                                                for key, state in report.get('markets', {}).items()}
                                       for league, report in (market_reliability or {}).items()},
        'min_edge': MIN_EDGE, 'min_edge_derived': MIN_EDGE_DERIVED, 'max_offered_odds': MAX_ODDS,
        'max_offered_to_fair_ratio': MAX_FAIR_RATIO, 'max_quote_skew_minutes': MAX_QUOTE_SKEW_MINUTES,
        'pinnacle_overround_range': list(PINNACLE_OVERROUND), 'reference_order': REFERENCES,
        'derived_reference': 'market_implied fit B (1X2 + O/U 2.5 + main AH), plus lines only, residual <= 3pp',
        'tags': {'balanced': f'Pinnacle 1X2 home and away odds both in [{BALANCED_ODDS[0]:.2f}, {BALANCED_ODDS[1]:.2f}]',
                 'low_total': f'Pinnacle margin-free P(over 2.5) < {LOW_TOTAL}',
                 'high_draw': f'Pinnacle margin-free draw probability >= {HIGH_DRAW}',
                 'even_odds': f'Pinnacle 1X2 home and away odds both >= {EVEN_ODDS_MIN:.2f} (raw quoted odds)',
                 'use': 'tracking only; never changes a decision'},
        'tagged_candidates': {t: int(tagged[t].fillna(False).astype(bool).sum()) for t in TAGS},
        'tagged_fixtures': int(tagged.apply(fixture_key, axis=1).nunique()) if len(tagged) else 0,
        'rejection_counts': {k: int(v) for k, v in reasons.items()},
        'reference_type_counts': {k: int(v) for k, v in selected.reference_type.value_counts().items()},
        'selection_method': 'Per fixture: qualifying candidate with the highest Pinnacle no-loss probability, then edge, '
                            'then odds; shortlist sorted safest first; no cap',
        'ranking_metric': 'pinnacle_no_loss_probability descending; edge descending; odds descending',
        'ev_required_for_selection': False, 'model_ev_required': False, 'no_loss_floor': None,
        'model_role': 'information only (model_vs_pinnacle_gap); never selects',
        'shortfall_reason': None if len(selected) else 'No candidate cleared the price-edge rule against a Pinnacle reference',
        'warning': 'A price edge against Pinnacle is not a guaranteed profit. Track CLV against the Pinnacle close; '
                   'the narrow-margin tags are hypotheses, not rules. Flat-stake research.',
    }
    return selected, decisions.reset_index(drop=True), summary
