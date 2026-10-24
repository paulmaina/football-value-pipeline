"""Versioned per-market shortlist: at most two picks from each market group.

Reuse every v23 eligibility, quote, identity and 48-hour check unchanged; only
the final selection differs. v23 stays importable so archived captures replay.
"""
import pandas as pd

POLICY = '48h-two-per-market-group-probability-ev-v24'
MARKET_GROUPS = ('Asian handicap', 'Home win', 'Away win', 'Over 1.5',
                 'Double Chance 1X', 'Double Chance X2', 'Double Chance 12')
PER_GROUP_CAP = 2
MAX_SELECTIONS = PER_GROUP_CAP*len(MARKET_GROUPS)
PROBABILITY_WEIGHT = .8
EV_WEIGHT = .2
NEGATIVE_EV_WARNING = 'NEGATIVE ADJUSTED EV'


def market_group(market):
    """All Asian lines and sides share one group; Draw and others have none."""
    from asian_handicap import parse_label
    if parse_label(market) is not None:
        return 'Asian handicap'
    return market if market in MARKET_GROUPS else None


def rank_candidates(pool):
    """Score each fixture-market within its group; best quote per pair only."""
    from performance_tracking import fixture_key
    pool = pool.assign(market_group=pool.market.map(market_group) if len(pool) else pd.Series(dtype=object))
    pool = pool.loc[pool.market_group.notna()].copy()
    pool['_fixture'] = pool.apply(fixture_key, axis=1) if len(pool) else pd.Series(dtype=str)
    order = ['rank_probability', 'conservative_estimated_ev', 'raw_dc_ev', 'offered_decimal_odds',
             'kickoff_utc', 'league', 'home_team', 'away_team', 'market', 'bookmaker']
    ascending = [False, False, False, False, True, True, True, True, True, True]
    # Duplicate bookmaker rows must not influence empirical percentile ranks.
    pool = pool.sort_values(order, ascending=ascending, kind='stable').drop_duplicates(['_fixture', 'market'])
    for field, source in [('probability_percentile', 'rank_probability'),
                          ('ev_percentile', 'conservative_estimated_ev')]:
        pool[field] = (pool.groupby('market_group')[source].rank(method='average', pct=True)
                       if len(pool) else pd.Series(dtype=float))
    # Round so equal weighted scores tie exactly and probability breaks them.
    pool['selection_score'] = (PROBABILITY_WEIGHT*pool.probability_percentile
                               + EV_WEIGHT*pool.ev_percentile).round(12)
    return pool.sort_values(['selection_score', *order], ascending=[False, *ascending], kind='stable')


def _max_fill(pairs, open_slots):
    """Most slots fillable from (fixture, group) pairs, one slot per fixture."""
    slots = [g for g in MARKET_GROUPS for _ in range(open_slots[g])]
    options = {}
    for fixture, group in pairs:
        options.setdefault(fixture, []).extend(i for i, g in enumerate(slots) if g == group)
    holder = {}

    def augment(fixture, seen):
        for slot in options[fixture]:
            if slot not in seen:
                seen.add(slot)
                if slot not in holder or augment(holder[slot], seen):
                    holder[slot] = fixture
                    return True
        return False
    return sum(augment(fixture, set()) for fixture in options)


def select_candidates(ranked):
    """Fill the most slots possible, preferring higher scores in rank order.

    One market per fixture, two per group, fourteen total. Walk candidates by
    score and accept one only if the remaining slots can still be filled as
    fully as the best allocation allows. A slot stays empty only when no
    allocation of the eligible candidates can fill it; groups never borrow
    another group's slots.
    """
    pairs = list(zip(ranked._fixture, ranked.market_group))
    open_slots = dict.fromkeys(MARKET_GROUPS, PER_GROUP_CAP)
    target = _max_fill(pairs, open_slots)
    used, chosen = set(), []
    for idx, (fixture, group) in zip(ranked.index, pairs):
        if len(chosen) == target:
            break
        if fixture in used or not open_slots[group]:
            continue
        open_slots[group] -= 1
        rest = [(f, g) for f, g in pairs if f not in used and f != fixture]
        if len(chosen) + 1 + _max_fill(rest, open_slots) == target:
            used.add(fixture)
            chosen.append(idx)
        else:
            open_slots[group] += 1
    return chosen


def build_shortlist(predictions, as_of, market_reliability, execution_policy=None):
    from win_first_shortlist import build_shortlist as build_v23
    _, decisions, summary = build_v23(predictions, as_of, market_reliability, execution_policy)
    eligible = decisions.decision.isin(['SHORTLISTED', 'NOT_SELECTED'])
    decisions.loc[eligible, 'decision'] = 'NOT_SELECTED'
    decisions.loc[eligible, 'selection_tier'] = None
    ungrouped = eligible & decisions.market.map(market_group).isna()
    for idx in decisions.index[ungrouped]:
        decisions.at[idx, 'decision'] = 'REJECTED'
        decisions.at[idx, 'rejection_reasons'] = 'market outside v24 market groups'
    ranked = rank_candidates(decisions.loc[eligible & ~ungrouped])
    fields = ['market_group', 'probability_percentile', 'ev_percentile', 'selection_score']
    for field in fields:
        decisions[field] = None if field == 'market_group' else float('nan')
    decisions.loc[ranked.index, fields] = ranked[fields]
    chosen = select_candidates(ranked)
    decisions.loc[chosen, 'decision'] = 'SHORTLISTED'
    decisions.loc[chosen, 'selection_tier'] = 'STRICT'
    # Present picks grouped by market, best combined score first in each group.
    selected = ranked.loc[chosen].assign(_group=lambda f: f.market_group.map(MARKET_GROUPS.index))
    selected = decisions.loc[selected.sort_values('_group', kind='stable').index].reset_index(drop=True)
    group_shortfall = {}
    for group in MARKET_GROUPS:
        n_selected = int((selected.market_group == group).sum())
        group_shortfall[group] = {
            'eligible_fixtures': int(ranked.loc[ranked.market_group == group, '_fixture'].nunique()),
            'selected': n_selected, 'shortfall': PER_GROUP_CAP-n_selected}
    negative = selected.conservative_estimated_ev < 0
    summary.update(selection_policy_version=POLICY, selection_objective='PER_MARKET_PROBABILITY_WEIGHTED',
        selection_method=f'Within each market group, {PROBABILITY_WEIGHT:g} x adjusted-probability percentile + '
                         f'{EV_WEIGHT:g} x adjusted-EV percentile; at most {PER_GROUP_CAP} per group and '
                         f'{MAX_SELECTIONS} in total; one market per fixture; fill the most slots possible, then prefer higher scores in rank order',
        ranking_metric='selection_score descending; ties: adjusted probability descending, adjusted EV descending, unblended EV descending, odds descending',
        ranking_weights={'adjusted_probability_percentile': PROBABILITY_WEIGHT,
                         'adjusted_ev_percentile': EV_WEIGHT},
        score_formula=f'{PROBABILITY_WEIGHT:g} * probability_percentile + {EV_WEIGHT:g} * ev_percentile (within market group)',
        market_groups=list(MARKET_GROUPS), max_per_market_group=PER_GROUP_CAP,
        target_distinct_matches=MAX_SELECTIONS, group_shortfall=group_shortfall,
        min_estimated_ev=None, min_raw_dc_ev=None, ev_required_for_selection=False,
        n_shortlisted=len(selected), n_strict_qualified=len(selected), n_provisional_watchlist=0,
        n_total_candidates=len(selected), usable_distinct_fixtures=int(ranked._fixture.nunique()),
        shortfall=MAX_SELECTIONS-len(selected), selected_matches_within_48_hours=bool(len(selected)),
        status='TARGET_MET' if len(selected) == MAX_SELECTIONS else 'BELOW_TARGET' if len(selected) else 'NO BET',
        shortfall_reason=(None if len(selected) == MAX_SELECTIONS else
            'Short groups: ' + ', '.join(f"{g} {s['selected']}/{PER_GROUP_CAP}"
                                         for g, s in group_shortfall.items() if s['shortfall']) +
            '. No allocation of eligible candidates fills these slots; they are not filled from other groups.'),
        negative_adjusted_ev_selections=int(negative.sum()),
        negative_adjusted_ev_markets=[f'{r.home_team} vs {r.away_team}: {r.market}'
                                      for r in selected.loc[negative].itertuples()],
        warning=f'Full and half wins count as profitable outcomes; refunds do not. No probability or EV floor. '
                f'Negative adjusted EV is explicitly flagged. Percentile scores are relative ranks within a market group, '
                f'not probabilities. Estimates are not guarantees; {MAX_SELECTIONS} individual picks are not an accumulator recommendation.')
    return selected, decisions.reset_index(drop=True), summary
