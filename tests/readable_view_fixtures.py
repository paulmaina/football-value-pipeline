"""Synthetic forecast rows and run bundles for the readable research/cagey views (tests only).

A forecast carries research exactly as team_research.enrich writes it (here research v4 on its independent Poisson
grid, so no fit file is needed) and Pinnacle quotes in the capture format price_edge_shortlist reads. `bundle`
runs the real value shortlist, cagey tier and master on those rows at CLOCK and writes the files the pipeline
writes, so the readable outputs can be checked against real list files.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, List, Optional, Sequence

import pandas as pd

CLOCK = '2026-11-18T21:46:12+00:00'
QUOTED = '2026-11-18T21:42:47Z'        # three minutes before the clock: fresh and synchronised
KICKOFF = '2026-11-19T17:30:00+00:00'  # inside the 24-hour shortlist window
LATER_KICKOFF = '2026-11-21T15:00:00+00:00'


def research_fields(rates=(1.6, 1.0)) -> Dict[str, object]:
    """research_* columns and team_research_json for v4 on these goal rates, as enrich writes them."""
    import team_research as tr
    matrix = tr.research_grid(list(rates))
    context = {'version': tr.V4_VERSION, 'goal_rates': list(rates), 'base_rates': list(rates), 'warnings': [],
               'observed_at_utc': '2026-11-18T21:40:00+00:00', 'coverage': {}, 'evidence': {}, 'form': {},
               **tr.grid_outputs(matrix)}
    return {**tr.outcome_columns(context, 'research_p_'), 'research_version': tr.V4_VERSION,
            'research_probability_basis': 'team_form_poisson_v1',
            'team_research_json': json.dumps(context, sort_keys=True)}


def quotes(h2h=(1.95, 3.68, 4.05), ou25=(1.88, 2.01), ah: Sequence = ((-0.5, 1.95, 1.95),), stamp=QUOTED,
           extra_books: Sequence = ()) -> Dict[str, object]:
    """price_edge_quotes and asian_handicap_offers with Pinnacle's 1X2, O/U 2.5 and AH pairs (home line, home
    price, away price); `extra_books` adds the same AH pairs at another bookmaker."""
    edge = []
    if h2h:
        edge.append({'bookmaker': 'Pinnacle', 'last_update_utc': stamp, 'market': 'h2h', 'market_key': 'h2h',
                     'point': None, 'prices': dict(zip(('home', 'draw', 'away'), h2h))})
    if ou25:
        edge.append({'bookmaker': 'Pinnacle', 'last_update_utc': stamp, 'market': 'totals', 'market_key': 'totals',
                     'point': 2.5, 'prices': {'over': ou25[0], 'under': ou25[1]}})
    offers = []
    for book in ('Pinnacle', *extra_books):
        for i, (line, home, away) in enumerate(ah):
            key = 'spreads' if i == 0 else 'alternate_spreads'
            offers.append({'bookmaker': book, 'last_update_utc': stamp, 'line': line, 'market_key': key,
                           'opposite_price': away, 'price': home, 'side': 'home', 'quote_source': 'The Odds API'})
            offers.append({'bookmaker': book, 'last_update_utc': stamp, 'line': -line + 0., 'market_key': key,
                           'opposite_price': home, 'price': away, 'side': 'away', 'quote_source': 'The Odds API'})
    return {'price_edge_quotes': json.dumps(edge), 'asian_handicap_offers': json.dumps(offers)}


def forecast(i=0, kickoff=KICKOFF, rates=(1.6, 1.0), research=True, **quote_args) -> Dict[str, object]:
    """One forecast row: the production fields a readable file shows, research and Pinnacle quotes."""
    from test_conservative_bet_filter import fixture
    row = fixture(i)
    row.update({'league': 'Premier League', 'date': kickoff[:10], 'kickoff_utc': kickoff,
                'home_team': f'Home_{i}', 'away_team': f'Away_{i}', 'fixture_source': 'The Odds API',
                'p_btts_yes': 0.52, 'p_btts_no': 0.48, 'lambda_home': 1.5, 'lambda_away': 1.1,
                'totals_anchor_status': 'ANCHORED_MAIN', 'odds_last_update_utc': QUOTED,
                'top_scorelines': json.dumps([{'score': '1-1', 'p': 0.12}, {'score': '1-0', 'p': 0.11}]),
                **quotes(**quote_args)})
    if research:
        row.update(research_fields(rates))
    return row


def summary() -> Dict[str, object]:
    """The cagey settings a live run records (cagey_correction_config.json), at CLOCK."""
    import price_edge_cagey_shortlist as pecs
    settings = pecs.load_settings()
    table = settings['cagey_corrections']
    return {'generated_at_utc': CLOCK, **{k: settings.get(k) for k in pecs.REPLAY_SETTINGS},
            'cagey_model_version': table['D']['model_version'], 'price_edge_execution_version': 2}


def production_policy() -> Dict[str, object]:
    import quote_policy
    return quote_policy.validate_policy(json.loads(
        (Path(__file__).resolve().parents[1] / 'shortlist_quote_policy.json').read_text(encoding='utf-8')))


def bundle(raw: Path, rows: List[Dict[str, object]], league_key: str = 'EPL') -> Dict[str, object]:
    """Run the real value shortlist, cagey tier and master on `rows` at CLOCK and write a run bundle."""
    import warnings
    import master_shortlist
    import narrow_margin as nm
    import price_edge_cagey_shortlist as pecs
    raw.mkdir(parents=True, exist_ok=True)
    predictions = pd.DataFrame(rows)
    predictions.to_csv(raw / f'{league_key}_predictions.csv', index=False)
    predictions.to_csv(raw / 'all_leagues_predictions.csv', index=False)
    with warnings.catch_warnings():
        warnings.simplefilter('ignore')
        selected, decisions, run_summary = pecs.build_shortlist(
            predictions, pd.Timestamp(CLOCK), execution_policy=production_policy(), model=nm.production_model())
        run_summary['quote_execution_policy'] = production_policy()
        selected.to_csv(raw / 'conservative_bet_shortlist.csv', index=False)
        decisions.to_csv(raw / 'conservative_bet_rejections.csv', index=False)
        pecs.cagey_tier_list(decisions).to_csv(raw / pecs.TIER_FILE, index=False)
        master_shortlist.refresh(decisions, raw, run_summary, predictions)
    (raw / 'conservative_bet_summary.json').write_text(json.dumps(run_summary, indent=2, default=str),
                                                      encoding='utf-8')
    return run_summary
