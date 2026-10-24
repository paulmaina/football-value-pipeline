"""Single source of truth for every supported league and how its history refreshes.

Every league list in the pipeline, refresh jobs, health reports and checks is
derived from REGISTRY. Adding a league means adding one entry here; a new entry
uses PER_MARKET_APPROVAL, so each of its markets reaches the shortlist only after
passing its own reliability audit, unchanged thresholds included.
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass
import json
from typing import Dict, Optional, Tuple

FOOTBALL_DATA_UK = 'football-data.co.uk'
FOOTBALL_DATA_ORG = 'football-data.org'
EUROPA_RECONCILED = 'europa-reconciled'

# Shortlist approval. Every market in every league still passes the per-market
# reliability, quote and identity checks. LEAGUE_APPROVAL: the league itself was
# reviewed (original seven). PER_MARKET_APPROVAL: no league-level review, so a
# market with no reliability report at all is also blocked.
LEAGUE_APPROVAL = 'league'
PER_MARKET_APPROVAL = 'per-market'

# refresh_method -> script that refreshes it and the workflow that schedules it.
REFRESH_METHODS = {
    FOOTBALL_DATA_UK: {'script': 'refresh_training_data.py', 'workflow': 'refresh-training-data.yml',
                       'needs_secret': None},
    EUROPA_RECONCILED: {'script': 'refresh_training_data.py', 'workflow': 'refresh-training-data.yml',
                        'needs_secret': None},
    FOOTBALL_DATA_ORG: {'script': 'refresh_ucl_training.py', 'workflow': 'refresh-ucl-training.yml',
                        'needs_secret': 'FOOTBALL_DATA_API_KEY'},
}


@dataclass(frozen=True)
class League:
    key: str
    name: str
    country: str
    football_data_div: str          # football-data.co.uk division code; '' when another source supplies history
    odds_api_sport_key: str
    football_data_org_code: str
    history_seasons: int            # seasons of history kept in the repository and used for training
    refresh_method: str             # one of REFRESH_METHODS
    shortlist_approval: str         # LEAGUE_APPROVAL or PER_MARKET_APPROVAL
    bbs_slug: Optional[str] = None
    bbs_display_names: Tuple[str, ...] = ()
    api_football_id: Optional[int] = None

    @property
    def domestic(self) -> bool:
        return self.refresh_method == FOOTBALL_DATA_UK

    def cache_globs(self) -> Tuple[str, ...]:
        """Refreshed training files, relative to .football_cache, committed to the repository."""
        if self.refresh_method == FOOTBALL_DATA_UK:
            return (f'????_{self.football_data_div}.csv',)
        if self.refresh_method == FOOTBALL_DATA_ORG:
            return (f'fdorg_history_{self.key}_????.json', f'fdorg_history_{self.key}_????.meta.json')
        return ('europa/training.json', 'europa/sources/*')


REGISTRY: Tuple[League, ...] = (
    League('EPL', 'Premier League', 'England', 'E0', 'soccer_epl', 'PL', 6, FOOTBALL_DATA_UK, LEAGUE_APPROVAL,
           'epl', ('epl', 'premier league', 'english premier league'), 39),
    League('LaLiga', 'La Liga', 'Spain', 'SP1', 'soccer_spain_la_liga', 'PD', 6, FOOTBALL_DATA_UK, LEAGUE_APPROVAL,
           'laliga', ('laliga', 'la liga'), 140),
    League('Bundesliga', 'Bundesliga', 'Germany', 'D1', 'soccer_germany_bundesliga', 'BL1', 6, FOOTBALL_DATA_UK, LEAGUE_APPROVAL,
           'bundesliga', ('bundesliga',), 78),
    League('SerieA', 'Serie A', 'Italy', 'I1', 'soccer_italy_serie_a', 'SA', 6, FOOTBALL_DATA_UK, LEAGUE_APPROVAL,
           'serie_a', ('serie_a', 'serie-a', 'seriea', 'serie a'), 135),
    League('Ligue1', 'Ligue 1', 'France', 'F1', 'soccer_france_ligue_one', 'FL1', 6, FOOTBALL_DATA_UK, LEAGUE_APPROVAL,
           'ligue1', ('ligue-1', 'ligue1', 'ligue 1'), 61),
    League('UCL', 'UEFA Champions League', 'Europe', '', 'soccer_uefa_champs_league', 'CL', 4, FOOTBALL_DATA_ORG, LEAGUE_APPROVAL,
           'cl', ('cl', 'ucl', 'uefa champions league', 'champions league'), 2),
    League('UEL', 'UEFA Europa League', 'Europe', '', 'soccer_uefa_europa_league', 'EL', 5, EUROPA_RECONCILED, LEAGUE_APPROVAL),
    # Sport keys verified against The Odds API GET /v4/sports on 2026-10-24.
    # Not league-approved: each market needs its own passing reliability audit
    # (docs/audits/2026-10-24-eredivisie-primeira-validation.md).
    League('Eredivisie', 'Eredivisie', 'Netherlands', 'N1', 'soccer_netherlands_eredivisie', 'DED', 6,
           FOOTBALL_DATA_UK, PER_MARKET_APPROVAL),
    League('PrimeiraLiga', 'Primeira Liga', 'Portugal', 'P1', 'soccer_portugal_primeira_liga', 'PPL', 6,
           FOOTBALL_DATA_UK, PER_MARKET_APPROVAL),
)

LEAGUES: Dict[str, League] = {league.key: league for league in REGISTRY}


def get(key: str) -> League:
    try:
        return LEAGUES[key]
    except KeyError:
        raise KeyError(f'Unknown league {key!r}. Choose from {list(LEAGUES)}') from None


def keys(refresh_method: Optional[str] = None, *, shortlist_approval: Optional[str] = None) -> Tuple[str, ...]:
    return tuple(l.key for l in REGISTRY if refresh_method in (None, l.refresh_method)
                 and shortlist_approval in (None, l.shortlist_approval))


def divisions() -> Dict[str, str]:
    """League key -> football-data.co.uk division, in registry order."""
    return {l.key: l.football_data_div for l in REGISTRY if l.domestic}


def shortlist_names(*, domestic_only: bool = False, shortlist_approval: Optional[str] = None) -> frozenset:
    """Display names of leagues whose markets may be evaluated for the shortlist."""
    return frozenset(l.name for l in REGISTRY if (l.domestic or not domestic_only)
                     and shortlist_approval in (None, l.shortlist_approval))


def bbs_slugs() -> Dict[str, str]:
    return {l.key: l.bbs_slug for l in REGISTRY if l.bbs_slug}


def bbs_display_names() -> Dict[str, set]:
    return {l.key: set(l.bbs_display_names) for l in REGISTRY if l.bbs_slug}


def api_football_ids() -> Dict[str, int]:
    return {l.key: l.api_football_id for l in REGISTRY if l.api_football_id is not None}


def history_seasons(refresh_method: str) -> int:
    """Longest configured history for one refresh method."""
    return max(l.history_seasons for l in REGISTRY if l.refresh_method == refresh_method)


def validate() -> None:
    names, sport_keys, divisions_seen = set(), set(), set()
    for l in REGISTRY:
        if l.shortlist_approval not in (LEAGUE_APPROVAL, PER_MARKET_APPROVAL):
            raise ValueError(f'{l.key}: unknown shortlist approval {l.shortlist_approval!r}')
        if l.refresh_method not in REFRESH_METHODS:
            raise ValueError(f'{l.key}: unknown refresh method {l.refresh_method!r}')
        if not 1 <= l.history_seasons <= 10:
            raise ValueError(f'{l.key}: history_seasons must be between 1 and 10')
        if l.domestic != bool(l.football_data_div):
            raise ValueError(f'{l.key}: football-data.co.uk leagues, and only those, need a division code')
        if l.refresh_method == FOOTBALL_DATA_ORG and not l.football_data_org_code:
            raise ValueError(f'{l.key}: football-data.org refresh needs a competition code')
        if not l.odds_api_sport_key.startswith('soccer_'):
            raise ValueError(f'{l.key}: invalid Odds API sport key')
        for value, seen, label in ((l.name, names, 'name'), (l.odds_api_sport_key, sport_keys, 'sport key'),
                                   (l.football_data_div, divisions_seen, 'division')):
            if value and value in seen:
                raise ValueError(f'{l.key}: duplicate {label} {value!r}')
            seen.add(value)
    if len(LEAGUES) != len(REGISTRY):
        raise ValueError('Duplicate league key')


validate()


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--json', action='store_true', help='Print the registry as JSON')
    args = parser.parse_args(argv)
    rows = [{**l.__dict__, 'cache_globs': list(l.cache_globs())} for l in REGISTRY]
    if args.json:
        print(json.dumps(rows, indent=2))
    else:
        for r in rows:
            print(f"{r['key']:<12} {r['name']:<24} {r['football_data_div'] or '-':<4} {r['odds_api_sport_key']:<32} "
                  f"{r['history_seasons']} seasons  {r['refresh_method']:<20} approval={r['shortlist_approval']}")
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
