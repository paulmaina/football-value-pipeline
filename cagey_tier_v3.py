"""Versioned 67% narrow-margin cagey selection across real quoted markets."""
import numpy as np
import pandas as pd

RULE = 'narrow-67-per-market-v3'
RULE_NO_GATE = 'corrected-no-loss-per-market-v4'
EXPANDED_RULES = (RULE, RULE_NO_GATE)
BASIS = 'pinnacle_cagey_corrected_matrix_v1'
MIN_NARROW = .67
COLUMNS = ['cagey_tier_rule', 'cagey_market_group', 'cagey_probability_basis']
KINDS = ('win', 'half_win', 'push', 'half_loss', 'loss')


def corrected_grid(context, matrix):
    """Preserve P(score | margin), replacing only margin mass with the correction.

    A margin-only correction does not identify a unique total-goals model. This
    explicit lift retains the original Pinnacle grid's within-margin structure.
    """
    matrix = np.asarray(matrix, float)
    if matrix.ndim != 2 or not np.isfinite(matrix).all() or (matrix < 0).any() or abs(matrix.sum()-1) > 1e-6:
        raise ValueError('Invalid Pinnacle score grid')
    delta = np.subtract.outer(np.arange(matrix.shape[0]), np.arange(matrix.shape[1]))
    corrected = np.zeros_like(matrix)
    for margin, probability in zip(context['margins'], context['probs']):
        mask = delta == margin
        old = matrix[mask].sum()
        if probability > 0 and old <= 0:
            raise ValueError('Corrected margin outside Pinnacle grid support')
        if old > 0:
            corrected[mask] = matrix[mask] * probability / old
    if not np.isfinite(corrected).all() or (corrected < 0).any() or abs(corrected.sum()-1) > 1e-6:
        raise ValueError('Invalid corrected score grid')
    return corrected


def columns(rule):
    if rule == RULE_NO_GATE:
        from narrow_support import COLUMNS as support_columns
        return [*COLUMNS, *support_columns]
    return list(COLUMNS)


def annotate(item, context, row, now, policy, cost, rule=RULE):
    import price_edge_cagey_shortlist as v28
    from quote_freshness import quote_is_fresh, quote_utc
    from quote_policy import usable_bookmaker
    from team_research import number
    from profit_shortlist import probabilities
    label = str(item.get('market') or '')
    group = v28.market_group(item, rule=v28.VALUE_RULE_LOCAL_RESEARCH)
    item.update(cagey_tier_rule=rule, cagey_market_group=group, cagey_probability_basis=BASIS,
                cagey_tier_decision='REJECTED', cagey_tier_reasons='', price_flag=None)
    reasons = []
    if not (label in ('Home win', 'Away win', 'Double Chance 1X', 'Double Chance X2', 'Double Chance 12', 'Over 1.5')
            or label.startswith('Asian Handicap ')):
        reasons.append('market outside cagey rule')
    kick, offer = quote_utc(row.get('kickoff_utc')), quote_utc(item.get('offered_last_update_utc'))
    if kick is None or not now+pd.Timedelta(minutes=20) <= kick <= now+pd.Timedelta(hours=48):
        reasons.append('kickoff outside 20-minute to 48-hour window')
    price = number(item.get('offered_decimal_odds'))
    if price is None or not 1.15 < price <= 2.0:
        reasons.append('cagey offered odds outside (1.15, 2.00]')
    if not usable_bookmaker(item.get('bookmaker'), policy):
        reasons.append('bookmaker unavailable')
    if offer is None or not quote_is_fresh(offer, now) or offer > now or (kick is not None and offer >= kick):
        reasons.append('offered quote stale or not observed before evaluation and kickoff')
    if context is None or 'matrix' not in context:
        reasons.append('corrected Pinnacle distribution unavailable')
    else:
        stamps = [quote_utc(s) for s in context['input_stamps']]
        synchronized = (bool(stamps) and offer is not None and all(s is not None and s <= now and
                        quote_is_fresh(s, now) for s in stamps))
        if synchronized:
            synchronized = (max([offer, *stamps])-min([offer, *stamps])).total_seconds() <= 600
        item['corrected_input_timing_status'] = 'SYNCHRONIZED' if synchronized else 'UNAVAILABLE_OR_UNSYNCHRONIZED'
        if not synchronized:
            reasons.append('corrected distribution inputs unavailable, stale, future or more than 10 minutes apart')
        item.update(corrected_cagey_score=context['score'], corrected_fit=context['fit'])
        if rule == RULE and 1-context['score'] + 1e-9 < MIN_NARROW:
            reasons.append('P(narrow) below 67%')
        matrix = context['matrix']
        evidence = {'margin_distribution': {str(int(m)): float(p) for m, p in zip(context['margins'], context['probs'])},
                    'p_over_1_5': float(matrix[np.add.outer(np.arange(matrix.shape[0]), np.arange(matrix.shape[1])) >= 2].sum())}
        try:
            probs = probabilities(row, item, evidence)
        except (ValueError, TypeError):
            probs = None
        if probs is None:
            reasons.append('corrected market settlement unavailable')
        else:
            item.update({'corrected_p_'+k: probs['p_'+k] for k in KINDS})
            if price is not None:
                mass = np.array([probs['p_'+k] for k in KINDS])
                returns = np.array([price-1, (price-1)/2, 0, -.5, -1])-cost
                ev = float(mass @ returns)
                win_stake, loss_stake = mass[0]+mass[1]/2, mass[4]+mass[3]/2
                fair = 1+loss_stake/win_stake if win_stake > 0 else np.inf
                item.update(corrected_no_loss_probability=float(mass[returns >= -1e-12].sum()),
                            corrected_p_profit=float(mass[returns > 1e-12].sum()),
                            corrected_expected_profit=ev, corrected_fair_odds=fair,
                            price_flag='value' if ev >= -1e-9 else 'below fair')
                if price > 1.15*fair:
                    reasons.append('offered price above 1.15 x corrected fair odds')
    if rule == RULE_NO_GATE:
        from narrow_support import supplement
        item.update(supplement(item, context, cost))
    item['cagey_tier_reasons'] = '; '.join(reasons)
    item['cagey_tier_decision'] = 'REJECTED' if reasons else 'ELIGIBLE'


def select(decisions, selected, rule=RULE):
    from performance_tracking import fixture_key
    from price_edge_cagey_shortlist import _tier_rank
    for column in ('cagey_tier_decision', 'cagey_tier_reasons', 'in_value_tier'):
        decisions[column] = decisions[column].astype(object)
    keys = decisions.apply(fixture_key, axis=1) if len(decisions) else pd.Series(dtype=str)
    picked = set(selected.apply(fixture_key, axis=1)) if len(selected) else set()
    decisions['in_value_tier'] = keys.isin(picked)
    eligible = decisions.loc[decisions.cagey_tier_decision.eq('ELIGIBLE')].copy()
    eligible['_group'] = keys.reindex(eligible.index) + '#' + eligible.cagey_market_group
    chosen = _tier_rank(eligible).drop_duplicates('_group').index
    decisions.loc[eligible.index, 'cagey_tier_decision'] = 'NOT_SELECTED'
    decisions.loc[chosen, 'cagey_tier_decision'] = 'SHORTLISTED'
    flags = decisions.loc[chosen, 'price_flag']
    result = dict(enabled=True, rule_version=rule, min_p_narrow=MIN_NARROW if rule == RULE else None, n_shortlisted=len(chosen),
                value_picks=int(flags.eq('value').sum()), below_fair_picks=int(flags.eq('below fair').sum()),
                probability_basis=BASIS, selection_objective='NO_LOSS_PROBABILITY',
                rule='P(narrow) >= 67%; real quoted win/DC/AH/Over 1.5; odds (1.15, 2.00]; one per fixture/market group; no-loss then expected return then odds; no EV or no-loss floor; no cap')

    if rule == RULE_NO_GATE:
        result.update(narrow_general_gate=False, narrow_supplement_threshold=MIN_NARROW,
                      narrow_supplement_version='corrected-narrow-support-v1',
                      rule='No P(narrow) eligibility gate; corrected no-loss then expected return then odds; real quoted win/DC/AH/Over 1.5; odds (1.15, 2.00]; one per fixture/market group; no EV or no-loss floor; no cap; 67% narrow is market-specific supporting information only')
    return result
