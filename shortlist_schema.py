"""Comparable numeric fields; each list retains its own labelled probability source."""
import numpy as np
import pandas as pd

SCHEMA = 'comparable-shortlist-v1'
SETTLEMENT = ('win', 'half_win', 'push', 'half_loss', 'loss')


def harmonize(frame, tier):
    from performance_tracking import fixture_key
    from cagey_tier_v3 import BASIS, RULE
    out = frame.copy()
    cagey = tier == 'cagey'
    prefix = 'cagey' if cagey and 'cagey_p_win' in out else 'corrected' if cagey else 'research'
    out['shortlist_schema_version'] = SCHEMA
    out['shortlist_source'] = tier
    out['selection_rule'] = out.cagey_tier_rule if cagey else 'local-research-profit-115-200-dc12-v2'
    out['selection_objective'] = 'NO_LOSS_PROBABILITY' if cagey else 'POSITIVE_RETURN_PROBABILITY'
    out['source_probability_basis'] = out.cagey_probability_basis if cagey else 'team_form_poisson_v1'
    out['fixture_key'] = out.apply(fixture_key, axis=1) if len(out) else pd.Series(dtype=str)
    if cagey:
        out['value_market_group'] = out.cagey_market_group
    for kind in SETTLEMENT:
        out['settlement_p_'+kind] = pd.to_numeric(out.get(prefix+'_p_'+kind, pd.Series(index=out.index, dtype=float)), errors='coerce')
    cost = pd.to_numeric(out.get('per_stake_cost', pd.Series(0., index=out.index)), errors='coerce')
    price = pd.to_numeric(out.offered_decimal_odds, errors='coerce')
    masses = out[['settlement_p_'+k for k in SETTLEMENT]].to_numpy(float)
    returns = np.column_stack([price-1, (price-1)/2, price*0, price*0-.5, price*0-1])-cost.to_numpy()[:, None]
    out['chance_of_positive_return'] = (masses*(returns > 1e-12)).sum(axis=1)
    out['chance_of_no_loss'] = (masses*(returns >= -1e-12)).sum(axis=1)
    out['expected_return_after_cost'] = (masses*returns).sum(axis=1)
    win = out.settlement_p_win+out.settlement_p_half_win/2
    loss = out.settlement_p_loss+out.settlement_p_half_loss/2
    out['fair_odds_after_cost'] = (1+(loss+cost)/win).where(win > 0)
    out['model_price_edge'] = price/out.fair_odds_after_cost-1
    out['price_assessment'] = np.where(out.expected_return_after_cost >= -1e-9, 'nonnegative expected value', 'negative expected value')
    out['p_narrow'] = 1-pd.to_numeric(out.get('corrected_cagey_score', pd.Series(index=out.index, dtype=float)), errors='coerce')
    return out


def readable(frame, pct, decimal, signed_pct, group_names):
    """Same ordered headers and units in both CSVs, including empty outputs."""
    identity = {'Kickoff (UTC)': 'kickoff_utc', 'League': 'league', 'Home': 'home_team', 'Away': 'away_team',
                'Fixture key': 'fixture_key', 'Market to bet': 'market_to_bet', 'Bookmaker': 'bookmaker',
                'Probability basis': 'source_probability_basis', 'Selection objective': 'selection_objective',
                'Selection rule': 'selection_rule', 'Shortlist source': 'shortlist_source'}
    out = pd.DataFrame({label: frame[key] for label, key in identity.items()})
    out.insert(6, 'Market group', frame.value_market_group.map(group_names))
    for label, key in [('Price', 'offered_decimal_odds'), ('Model fair odds after cost', 'fair_odds_after_cost')]:
        out[label] = frame[key].map(decimal)
    for label, key in [('Chance of positive return', 'chance_of_positive_return'), ('Chance of no loss', 'chance_of_no_loss'),
                       ('P(narrow)', 'p_narrow'), *[(k.replace('_', ' ').title(), 'settlement_p_'+k) for k in SETTLEMENT]]:
        out[label] = frame[key].map(pct)
    out['Expected return after cost'] = frame.expected_return_after_cost.map(signed_pct)
    out['Model price edge'] = frame.model_price_edge.map(signed_pct)
    out['Price assessment'] = frame.price_assessment
    if 'narrow_support_version' in frame:
        out['Corrected P(narrow) >=67%'] = frame.narrow_high_67.map(
            lambda v: 'unavailable' if pd.isna(v) else 'yes' if str(v).lower() == 'true' else 'no')
        out['Corrected narrow support'] = frame.narrow_support_note
        for label, key in [('Corrected draw probability', 'corrected_p_draw'),
                           ('Corrected home win by one', 'corrected_p_home_by_one'),
                           ('Corrected away win by one', 'corrected_p_away_by_one'),
                           ('Corrected-grid narrow no-loss contribution', 'corrected_narrow_no_loss_contribution'),
                           ('Corrected-grid narrow profit contribution', 'corrected_narrow_profit_contribution'),
                           ('Corrected-grid no-loss lower bound', 'corrected_narrow_no_loss_lower_bound'),
                           ('Corrected-grid no-loss upper bound', 'corrected_narrow_no_loss_upper_bound'),
                           ('Corrected-grid profit lower bound', 'corrected_narrow_profit_lower_bound'),
                           ('Corrected-grid profit upper bound', 'corrected_narrow_profit_upper_bound')]:
            out[label] = frame[key].map(pct)
    if 'price_guard_status' in frame:
        out['Price check status'] = frame.price_guard_status
        out['Price check basis'] = frame.price_guard_basis
        out['Pinnacle fair odds for price check'] = frame.price_guard_fair_odds.map(decimal)
        out['Price check warning'] = frame.price_guard_warning
        out['Corrected Over 1.5 (comparison only)'] = frame.corrected_over_1_5_probability.map(pct)
        out['Uncorrected Over 1.5'] = frame.uncorrected_over_1_5_probability.map(pct)
        out['Totals correction delta'] = frame.totals_correction_delta.map(signed_pct)
        out['Draw correction delta vs Pinnacle'] = frame.corrected_draw_delta_vs_pinnacle.map(signed_pct)
    if 'research_warnings' in frame:
        out['Coverage warnings'] = frame.research_warnings
    if 'research_details' in frame:
        import json
        def quality_text(value):
            try:
                details = json.loads(value) if isinstance(value, str) else {}
                review = details.get('quality_review', {})
                if not review:
                    return ''
                return review['status'] + ': ' + '; '.join(review.get('warnings', []))
            except (ValueError, TypeError, AttributeError, KeyError):
                return ''
        reviews = frame.research_details.map(quality_text)
        if reviews.ne('').any():
            out['Research quality review'] = reviews
    return out
