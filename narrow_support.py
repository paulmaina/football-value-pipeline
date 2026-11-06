"""Market-specific consequences of the corrected narrow event, never a new weight.

All figures use the SAME corrected grid as settlement. Joint contributions are
parts of the existing probabilities; bounds express event inclusion/exclusion.
They must not be added to predictions or applied to the research model's figures.
"""
import numpy as np

VERSION = 'corrected-narrow-support-v1'
THRESHOLD = .67
COLUMNS = ['narrow_support_version', 'narrow_high_67', 'narrow_support_role', 'narrow_support_note',
           'corrected_p_draw', 'corrected_p_home_by_one', 'corrected_p_away_by_one',
           'corrected_narrow_no_loss_contribution', 'corrected_narrow_profit_contribution',
           'corrected_narrow_no_loss_lower_bound', 'corrected_narrow_no_loss_upper_bound',
           'corrected_narrow_profit_lower_bound', 'corrected_narrow_profit_upper_bound']


def supplement(item, context, cost):
    from asian_handicap import profit
    from team_research import number
    out = dict.fromkeys(COLUMNS)
    out.update(narrow_support_version=VERSION, narrow_support_role='unavailable',
               narrow_support_note='Corrected distribution unavailable; no narrow support inferred')
    if context is None or 'matrix' not in context:
        return out
    grid = np.asarray(context['matrix'], float)
    delta = np.subtract.outer(np.arange(grid.shape[0]), np.arange(grid.shape[1]))
    total = np.add.outer(np.arange(grid.shape[0]), np.arange(grid.shape[1]))
    narrow = abs(delta) <= 1
    p = float(grid[narrow].sum())
    high = p + 1e-9 >= THRESHOLD
    out.update(narrow_high_67=high, corrected_p_draw=float(grid[delta == 0].sum()),
               corrected_p_home_by_one=float(grid[delta == 1].sum()),
               corrected_p_away_by_one=float(grid[delta == -1].sum()),
               narrow_support_role='context_only',
               narrow_support_note=('P(narrow) >=67%; ' if high else 'P(narrow) below 67%; ')
                   + 'context only for this market; no directional or totals boost')
    price = number(item.get('offered_decimal_odds'))
    if price is None or price <= 1:
        return out
    market, side, line = item.get('market'), item.get('handicap_side'), number(item.get('handicap_line'))
    if market == 'Over 1.5':
        returns = np.where(total >= 2, price-1, -1)-cost
    elif market == 'Double Chance 12':
        returns = np.where(delta != 0, price-1, -1)-cost
    elif side in ('home', 'away') and line is not None:
        values = {int(d): profit(max(int(d), 0), max(-int(d), 0), side, line, price, cost)[1]
                  for d in np.unique(delta)}
        returns = np.array([[values[int(d)] for d in row] for row in delta])
    else:
        return out
    for event, mask in [('no_loss', returns >= -1e-12), ('profit', returns > 1e-12)]:
        out['corrected_narrow_'+event+'_contribution'] = float(grid[narrow & mask].sum())
        # All three narrow margins must meet the event, even if one has zero mass.
        if mask[narrow].all():
            out['corrected_narrow_'+event+'_lower_bound'] = p
        elif not mask[narrow].any():
            out['corrected_narrow_'+event+'_upper_bound'] = 1-p
    if str(market).startswith('Asian Handicap '):
        lower = out['corrected_narrow_no_loss_lower_bound']
        profit_lower = out['corrected_narrow_profit_lower_bound']
        upper = out['corrected_narrow_profit_upper_bound']
        if lower is not None:
            out['narrow_support_role'] = 'plus_handicap_protection'
            detail = f'All narrow results avoid net loss; corrected no-loss >= {lower:.1%}'
            if profit_lower is not None:
                detail += f'; corrected profit probability >= {profit_lower:.1%}'
        elif upper is not None and line < 0:
            out['narrow_support_role'] = 'minus_handicap_caution'
            detail = f'No narrow result is profitable; corrected profit probability <= {upper:.1%}'
            no_loss_upper = out['corrected_narrow_no_loss_upper_bound']
            if no_loss_upper is not None:
                detail += f'; corrected no-loss <= {no_loss_upper:.1%}'
        else:
            detail = 'No universal narrow-event protection bound at this line, price and execution cost'
        out['narrow_support_note'] = ('P(narrow) >=67%; ' if high else 'P(narrow) below 67%; ') + detail
    return out
