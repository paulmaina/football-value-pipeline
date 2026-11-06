"""V5: market-specific settlement source and independent binary price checks."""
import numpy as np
import pandas as pd

UNCORRECTED = 'pinnacle_uncorrected_matrix_v1'
BINARY = ('Home win','Away win','Double Chance 1X','Double Chance X2','Double Chance 12','Over 1.5')
KINDS = ('win','half_win','push','half_loss','loss')
COLUMNS = [*['cagey_p_'+k for k in KINDS], 'cagey_no_loss_probability','cagey_p_profit',
           'cagey_expected_return','cagey_fair_odds','cagey_input_timing_status','cagey_settlement_fit',
           'price_guard_status','price_guard_basis','price_guard_fair_odds','price_guard_warning',
           'corrected_over_1_5_probability','uncorrected_over_1_5_probability','totals_correction_delta',
           'corrected_draw_delta_vs_pinnacle','correction_validation_note']


def binary_market(item):
    market=item.get('market')
    if market in BINARY: return market
    if str(market).startswith('Asian Handicap '):
        from team_research import number
        side,line=item.get('handicap_side'),number(item.get('handicap_line'))
        if side in ('home','away') and line in (-.5,.5):
            return ('Home win' if side=='home' else 'Away win') if line<0 else ('Double Chance 1X' if side=='home' else 'Double Chance X2')
    return None


def reference(item, pin, now):
    """Only a fresh, synchronized, margin-free Pinnacle price; never a fitted fair."""
    from quote_freshness import quote_utc, quote_is_fresh
    from market_implied import devig_three_way
    market = binary_market(item)
    record = (pin or {}).get('ou15' if market == 'Over 1.5' else 'h2h')
    if record is None:
        return None, 'Pinnacle reference missing'
    prices, stamp = record[:-1], quote_utc(record[-1])
    offer = quote_utc(item.get('offered_last_update_utc'))
    if (stamp is None or offer is None or stamp > now or not quote_is_fresh(stamp, now)
            or abs((stamp-offer).total_seconds()) > 600):
        return None, 'Pinnacle reference stale, future or unsynchronized'
    values = np.array(prices, float)
    if not np.isfinite(values).all() or (values <= 1).any() or not 1 <= (1/values).sum() <= 1.1:
        return None, 'Pinnacle reference overround/price invalid'
    if market == 'Over 1.5':
        q = (1/values[0])/(1/values).sum()
    else:
        h,d,a = devig_three_way(*values)
        q = {'Home win':h,'Away win':a,'Double Chance 1X':h+d,
             'Double Chance X2':d+a,'Double Chance 12':h+a}[market]
    return (1/float(q) if q > 0 else None), None


def over_probability(matrix):
    if matrix is None:
        return None
    grid = np.asarray(matrix,float)
    if grid.ndim != 2 or not np.isfinite(grid).all() or (grid < 0).any() or abs(grid.sum()-1) > 1e-6:
        return None
    return float(grid[np.add.outer(np.arange(grid.shape[0]),np.arange(grid.shape[1])) >= 2].sum())


def annotate(item, context, row, now, policy, cost, pin):
    from cagey_tier_v3 import annotate as previous, RULE_NO_GATE, RULE_MARKET_BASIS, BASIS
    from price_edge_shortlist import pinnacle_quotes
    previous(item,context,row,now,policy,cost,rule=RULE_NO_GATE)
    item['cagey_tier_rule'] = RULE_MARKET_BASIS
    item.update({key:None for key in COLUMNS})
    item['cagey_probability_basis'] = UNCORRECTED if item.get('market') == 'Over 1.5' else BASIS
    reasons = [r for r in item['cagey_tier_reasons'].split('; ') if r]
    corrected_p = over_probability(context.get('matrix')) if context else None
    raw_p = over_probability(context.get('uncorrected_matrix')) if context else None
    item.update(corrected_over_1_5_probability=corrected_p, uncorrected_over_1_5_probability=raw_p,
                totals_correction_delta=corrected_p-raw_p if corrected_p is not None and raw_p is not None else None,
                correction_validation_note='Narrow-margin validation is not separate draw/totals validation')
    probs = {k:item.get('corrected_p_'+k) for k in KINDS}
    if item.get('market') == 'Over 1.5':
        if raw_p is None:
            reasons.append('uncorrected Pinnacle grid unavailable for Over 1.5')
            probs = dict.fromkeys(KINDS)
        else:
            probs = dict(win=raw_p, half_win=0.,push=0.,half_loss=0.,loss=1-raw_p)
    item.update({'cagey_p_'+k:v for k,v in probs.items()})
    item.update(cagey_input_timing_status=item.get('corrected_input_timing_status'),
                cagey_settlement_fit=context.get('fit') if context else None)
    if all(v is not None and np.isfinite(v) and 0 <= v <= 1 for v in probs.values()) and abs(sum(probs.values())-1) <= 1e-6:
        price = item.get('offered_decimal_odds')
        if price is not None:
            mass = np.array([probs[k] for k in KINDS])
            returns = np.array([price-1,(price-1)/2,0,-.5,-1])-cost
            win,loss = mass[0]+mass[1]/2,mass[4]+mass[3]/2
            ev = float(mass@returns)
            item.update(cagey_no_loss_probability=float(mass[returns >= -1e-12].sum()),
                        cagey_p_profit=float(mass[returns > 1e-12].sum()),cagey_expected_return=ev,
                        cagey_fair_odds=1+loss/win if win > 0 else np.inf,
                        price_flag='value' if ev >= -1e-9 else 'below fair')
    pin = pin if pin is not None else pinnacle_quotes(row)
    if binary_market(item) is not None:
        # A model discrepancy is not a verified bookmaker data error.
        reasons = [r for r in reasons if r != 'offered price above 1.15 x corrected fair odds']
        fair,warning = reference(item,pin,now)
        item.update(price_guard_fair_odds=fair,price_guard_warning=warning,
                    price_guard_basis='pinnacle_ou15_proportional' if item['market']=='Over 1.5' else 'pinnacle_1x2_proportional',
                    price_guard_status='UNAVAILABLE' if fair is None else 'PASSED')
        if fair is not None and item.get('offered_decimal_odds') is not None and item['offered_decimal_odds'] > 1.15*fair:
            reasons.append('offered price above 1.15 x independent Pinnacle fair odds')
            item['price_guard_status'] = 'SUSPECTED_PRICE_ERROR'
    else:
        item.update(price_guard_fair_odds=item.get('corrected_fair_odds'),price_guard_basis=BASIS,
                    price_guard_status='UNAVAILABLE' if context is None else
                        'SUSPECTED_PRICE_ERROR' if 'offered price above 1.15 x corrected fair odds' in reasons else 'PASSED')
    if context and 'matrix' in context:
        fair,_ = reference({**item,'market':'Home win'},pin,now)
        h2h = pin.get('h2h')
        if fair is not None and h2h is not None:
            from market_implied import devig_three_way
            grid = context['matrix']
            item['corrected_draw_delta_vs_pinnacle'] = float(np.trace(grid))-devig_three_way(*h2h[:3])[1]
    item['cagey_tier_reasons'] = '; '.join(reasons)
    item['cagey_tier_decision'] = 'REJECTED' if reasons else 'ELIGIBLE'
