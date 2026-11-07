"""V6 master: replace DC nominations only with actual Pinnacle AH +0.5 quotes.

1X == home +0.5 and X2 == away +0.5 for regulation settlement. DC 12
(no draw) has no equivalent single AH line. Never relabel a DC offered price.
The released v5 selector stays unchanged for immutable archived replay.
"""
import pandas as pd
import master_selection as previous

VERSION = 'master-profit-no-dc-v6'
AUDIT_FILE = previous.AUDIT_FILE
EXTRA_COLUMNS = ['master_original_market', 'master_original_bookmaker', 'master_original_odds',
                 'master_replacement_status', 'master_replacement_reason', 'master_offer_source_market']


def _native_offers(forecast, side):
    from price_edge_shortlist import _json_list
    from asian_handicap import bookmaker
    for offer in _json_list(forecast.get('asian_handicap_offers')):
        if not isinstance(offer, dict):
            continue
        if (bookmaker(offer.get('bookmaker')) != 'Pinnacle' or offer.get('side') != side
                or previous.number(offer.get('line')) != .5
                or offer.get('market_key') not in ('spreads', 'alternate_spreads')):
            continue
        price, opposite = previous.number(offer.get('price')), previous.number(offer.get('opposite_price'))
        if (price is not None and opposite is not None and price > 1 and opposite > 1
                and 1 <= 1/price+1/opposite <= 1.10):
            yield offer, price


def evaluate(decisions, predictions, now=None):
    from master_shortlist import COLUMNS_AH
    if decisions is None or decisions.empty:
        return pd.DataFrame(columns=COLUMNS_AH)
    forecasts = {}
    if predictions is not None:
        for row in predictions.astype(object).where(predictions.notna(), None).to_dict('records'):
            key = previous.identity(row)
            forecasts[key] = row if key not in forecasts else None
    records = decisions.astype(object).where(decisions.notna(), None).to_dict('records')
    members = [r for r in records if r.get('decision') == 'SHORTLISTED' or r.get('cagey_tier_decision') == 'SHORTLISTED']
    expanded, provenance = [], []
    for row in members:
        original = dict(master_original_market=row.get('market'), master_original_bookmaker=row.get('bookmaker'),
                        master_original_odds=row.get('offered_decimal_odds'), master_replacement_status='NOT_REQUIRED',
                        master_replacement_reason='', master_offer_source_market=row.get('source_market'))
        market = str(row.get('market') or '')
        side = {'Double Chance 1X':'home', 'Double Chance X2':'away'}.get(market)
        # Older source rows can label the AH equivalent while retaining a DC offer.
        if (side is None and market in ('Asian Handicap Home +0.50', 'Asian Handicap Away +0.50')
                and row.get('source_market') == 'double_chance' and previous.number(row.get('handicap_line')) == .5):
            side = row.get('handicap_side') if market == f"Asian Handicap {str(row.get('handicap_side')).title()} +0.50" else None
        is_dc = market.startswith('Double Chance ') or row.get('source_market') == 'double_chance'
        if not is_dc:
            native = dict(row)
            if market.startswith('Asian Handicap '):
                native['value_market_group'] = 'asian_handicap'
            expanded.append(native); provenance.append(original)
            continue
        if side is None:
            original.update(master_replacement_status='EXCLUDED_DC',
                            master_replacement_reason='DC 12/unsupported DC has no equivalent single Asian Handicap line')
            expanded.append(row); provenance.append(original)
            continue
        forecast = forecasts.get(previous.identity(row))
        offers = list(_native_offers(forecast, side)) if forecast is not None else []
        if not offers:
            original.update(master_replacement_status='EXCLUDED_DC',
                            master_replacement_reason='Actual Pinnacle AH +0.5 quote unavailable; DC price is never reused')
            expanded.append(row); provenance.append(original)
            continue
        for offer, price in offers:
            label = f'Asian Handicap {side.title()} +0.50'
            converted = dict(row, market=label, market_to_bet=label, handicap_side=side, handicap_line=.5,
                value_market_group='asian_handicap', bookmaker='Pinnacle', offered_decimal_odds=price,
                offered_last_update_utc=offer.get('last_update_utc'), source_market=offer['market_key'],
                reference_type='b', reference_market='Pinnacle equivalent 1X2')
            expanded.append(converted)
            provenance.append(dict(original, master_replacement_status='DC_TO_PINNACLE_AH',
                master_replacement_reason=f'{market} regulation outcome equals {label}; actual Pinnacle AH price used',
                master_offer_source_market=offer['market_key']))
    if not expanded:
        return pd.DataFrame(columns=COLUMNS_AH)
    # Keep every decision's generation clock for validation, including nonmembers.
    from quote_freshness import quote_utc
    clocks = {quote_utc(r.get('evaluated_at_utc')) for r in records}
    if len(clocks) != 1:
        raise ValueError('Master generation clock differs from evaluated decision rows')
    audit = previous.evaluate(pd.DataFrame(expanded), predictions, now)
    for column in EXTRA_COLUMNS:
        audit[column] = [p[column] for p in provenance]
    excluded = audit.master_replacement_status.eq('EXCLUDED_DC')
    audit.loc[excluded, 'master_decision'] = 'EXCLUDED'
    for index in audit.index[excluded]:
        audit.loc[index, 'master_rejection_reasons'] = '; '.join(filter(None, [
            audit.loc[index, 'master_rejection_reasons'], audit.loc[index, 'master_replacement_reason']]))
    half = audit.market.fillna('').str.startswith('Asian Handicap ') & pd.to_numeric(audit.handicap_line,errors='coerce').eq(.5)
    usable_half = half & audit.master_decision.ne('EXCLUDED')
    if usable_half.any():
        audit.loc[usable_half, 'master_probability_basis'] = 'Pinnacle margin-free 1X2 equivalent for AH +0.5'
    audit['master_version'] = VERSION
    return audit.reindex(columns=COLUMNS_AH)


def select(audit):
    from master_shortlist import COLUMNS_AH
    eligible = audit.loc[audit.master_decision.eq('ELIGIBLE') &
                         ~audit.market.fillna('').str.startswith('Double Chance ') &
                         ~audit.master_offer_source_market.eq('double_chance')].copy()
    if eligible.empty:
        result = pd.DataFrame(columns=COLUMNS_AH)
        result.attrs['master_version'] = VERSION
        return result
    eligible['_fixture'] = [previous.identity(r) for r in eligible.to_dict('records')]
    ordered = eligible.sort_values(['master_profit_probability', 'master_expected_return',
        'master_no_loss_probability', 'offered_decimal_odds', 'kickoff_utc', 'league', 'home_team',
        'away_team', 'market', 'bookmaker', 'offered_last_update_utc'],
        ascending=[False, False, False, False, True, True, True, True, True, True, False], kind='stable')
    top = ordered.drop_duplicates('_fixture').head(previous.SIZE).copy()
    top['master_rank'] = range(1, len(top)+1)
    top['master_decision'] = 'SHORTLISTED'
    return top.reindex(columns=COLUMNS_AH).reset_index(drop=True)


def summary(frame):
    result = previous.summary(frame)
    result.update(version=VERSION, excluded_markets=['Double Chance 1X','Double Chance X2','Double Chance 12'],
        dc_replacement='1X -> actual Pinnacle home +0.5; X2 -> actual Pinnacle away +0.5; 12 excluded',
        converted_bets=int(frame.master_replacement_status.eq('DC_TO_PINNACLE_AH').sum()),
        rule=result['rule']+'; no DC offers; equivalent 1X/X2 nominations require an actual Pinnacle AH +0.5 quote; '
             'DC 12 has no single AH equivalent; original market/book/price retained in audit')
    return result
