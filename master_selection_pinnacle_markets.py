"""V9 master nominations use native Pinnacle Asian handicap, win and 1X/X2 offers."""
from asian_handicap import parse_label
import master_selection as market
from master_selection_fifteen import context_summary, rank_eligible, with_context

VERSION = 'master-profit-15-pinnacle-markets-v9'
AUDIT_FILE = market.AUDIT_FILE
BINARY_MARKETS = ('Home win', 'Away win', 'Double Chance 1X', 'Double Chance X2')
EXCLUSION = 'market or bookmaker outside the native Pinnacle shortlist rule'


def allowed(row):
    if row.get('bookmaker') != 'Pinnacle':
        return False
    label = row.get('market')
    if label in BINARY_MARKETS:
        return True
    handicap = parse_label(label)
    return (handicap is not None
            and handicap == (row.get('handicap_side'), market.number(row.get('handicap_line')))
            and row.get('master_offer_source_market') in ('spreads', 'alternate_spreads'))


def evaluate(decisions, predictions, now=None):
    audit = market.evaluate(decisions, predictions, now)
    records = decisions.to_dict('records') if decisions is not None else []
    audit['master_offer_source_market'] = [
        row.get('source_market') for row in records
        if row.get('decision') == 'SHORTLISTED' or row.get('cagey_tier_decision') == 'SHORTLISTED'
    ]
    audit['master_original_market'] = audit.market
    audit['master_original_bookmaker'] = audit.bookmaker
    audit['master_original_odds'] = audit.offered_decimal_odds
    audit['master_replacement_status'] = 'NOT_REQUIRED'
    audit['master_replacement_reason'] = ''
    excluded = [index for index, row in zip(audit.index, audit.to_dict('records')) if not allowed(row)]
    audit.loc[excluded, 'master_decision'] = 'EXCLUDED'
    for index in excluded:
        audit.at[index, 'master_rejection_reasons'] = '; '.join(filter(None, [
            audit.at[index, 'master_rejection_reasons'], EXCLUSION]))
    return with_context(audit, predictions, now, VERSION)


def select(audit):
    return rank_eligible(audit.loc[audit.master_decision.eq('ELIGIBLE')], VERSION)


def summary(frame):
    result = context_summary(frame, market.summary(frame), VERSION)
    result['eligible_markets'] = ['Asian Handicap', *BINARY_MARKETS]
    result['rule'] += '; native Pinnacle Asian Handicap, home or away win, and Double Chance 1X or X2'
    return result
