"""Live CE3n for UCL and UEL (research v6): CE's goal rates blended with each team's domestic strength.

CE3n is the harness candidate declared on the European holdout on 12 Nov 2026 (european_candidates, docs/plan.md
Phase 2c; not proven there). Released for UCL and UEL as research v6 by Paul's decision of 14 Nov 2026, a deliberate
exception to the release gate (docs/plan.md, Decisions, "European value picks"). Domestic leagues stay on v5.

For a European fixture:

    CE        research v4 exactly as live has run it for UCL and UEL (team_research.prepare's goal rates: the
              competition's Dixon-Coles rates shrunk with the ten-match form; no odds);
    domestic  each team's domestic research strength at the fit window's origin (european_candidates.team_strength:
              league Dixon-Coles before the origin shrunk 10 : n with the last-ten domestic form, goals only, no
              xG; the goal rates and form v4 and v5 share, before C6's draw and slope corrections), put on the
              European scale by the league-strength factors (european_candidates.fit_factors, goals);
    CE3n      the geometric blend (european_candidates.blended_rates, domestic weight 0.85) when both teams have
              a domestic strength and the factors are fitted, otherwise CE exactly; independent Poisson grid
              (team_research.research_grid), validated as the harness scores it (research_backtest.matrix_value).

The blend reuses the harness's own functions, so a fixture with the same CE goal rates and the same fit gets the
same probabilities in the harness and live.

Fits, one entry per European 14-day fold window (evaluation_harness.fold_windows on cfg['european']), written by
scripts/build_research_ce3n_fits.py:

    FITS          live (research_ce3n_live_fits.json): the factors and strengths from every result known before
                  each origin, including the European holdout period (UCL from 21 Jan 2025) and the domestic
                  holdout period (Paul, 14 Nov 2026: as for C6, the holdout locks apply to the evaluation harness,
                  not to live forecasts, and CE3n has already been scored on the European holdout). Refreshed every
                  second Monday by .github/workflows/research-c6-fits.yml.
    HARNESS_FITS  tested (research_ce3n_fits.json): the harness's own walk-forward factors from a locked European
                  run (no holdout result read), plus holdout-free strengths for the live windows. Locked.

The two differ by design. A forecast uses the live window with the latest origin on or before its research
observation day, so every result in its fit was played before the forecast was made. The part of the fit the
forecast uses (factors, the two teams' identities and strengths) is frozen in it (team_research_json['ce3n_fit'])
and replays without the file. Reads results only: no odds, market fit or published grid.
"""
from __future__ import annotations

from functools import lru_cache
import json
from pathlib import Path

import pandas as pd

VERSION = 'research-ce3n-domestic-form-v1'
CANDIDATE = 'CE3n'
FITS = Path(__file__).with_name('research_ce3n_live_fits.json')  # live: every known result
FITS_VERSION = 'research-ce3n-live-fits-v1'
HARNESS_FITS = Path(__file__).with_name('research_ce3n_fits.json')  # the harness's locked, holdout-free fits
HARNESS_FITS_VERSION = 'research-ce3n-fits-v1'
KIND = 'goals'  # CE3n: goals-only domestic form (CE3 with xG was not declared)
COMPETITIONS = {'UEFA Champions League': 'UCL', 'UEFA Europa League': 'UEL'}
FACTOR_FIELDS = ('status', 'matches', 's', 'c', 'h')


@lru_cache(maxsize=4)
def _load(path: str, mtime: float) -> dict:
    data = json.loads(Path(path).read_text(encoding='utf-8'))
    if data.get('version') not in (FITS_VERSION, HARNESS_FITS_VERSION) or data.get('candidate_version') != VERSION:
        raise ValueError(f'unsupported CE3n fit file {path}')
    return data


def load_fits(path=FITS) -> dict:
    path = Path(path)
    return _load(str(path), path.stat().st_mtime)


def expected_origin(day, rule) -> pd.Timestamp:
    """The European fold origin the harness gives `day` (evaluation_harness.fold_windows on cfg['european'])."""
    from research_low_score_sharpen import expected_origin as origin
    return origin(day, rule)


def european_name(team, frozen_name, identities, competition):
    """The side's European training name: the name frozen in research_history_json['teams'] (research v3 on), or,
    for a forecast frozen without one, the fixture name resolved against the fit's European names by the live
    research resolver (team_research.history_team: reviewed identities only, never fuzzy)."""
    if isinstance(frozen_name, str) and frozen_name:
        return frozen_name
    from team_research import history_team
    return history_team(team, set(identities), competition)


def fit_for(cutoff, league, home, away, path=FITS) -> dict | None:
    """The CE3n fit a forecast observed at `cutoff` uses, for the fixture's two sides (`home`, `away`: (fixture
    name, frozen European training name or None)): the fit file's window with the latest origin on or before the
    cutoff's UTC day, its factors and each side's identity and domestic strength (None when the side has no
    reviewed domestic identity or no strength in that window). None when the file has no window by then. `stale`
    is True when the harness would already have a later window for that day."""
    data = load_fits(path)
    competition = COMPETITIONS[str(league)]
    day = pd.Timestamp(cutoff).tz_convert('UTC').tz_localize(None).normalize()
    windows = [w for w in data['windows'] if pd.Timestamp(w['origin']) <= day]
    if not windows:
        return None
    window = windows[-1]
    expected = expected_origin(day, data['fold_rule'])
    identities = data['identities']
    # Every training name of this competition (with or without a domestic club), as its own loader spells it.
    names = (data.get('european_names') or {}).get(competition) or identities
    sides = {}
    for side, (team, frozen) in (('home', home), ('away', away)):
        name = european_name(team, frozen, names, competition)
        ident = identities.get(name) if name else None
        entry = {'european_name': name, 'league': None, 'domestic_team': None, 'strength': None}
        if ident is not None:
            league_key, domestic = ident
            strength = (window.get('strengths') or {}).get(league_key, {}).get(domestic)
            entry.update(league=league_key, domestic_team=domestic,
                         strength=None if strength is None else [float(v) for v in strength[KIND]])
        sides[side] = entry
    return {'fits_version': data['version'], 'candidate_version': data['candidate_version'],
            'competition': competition, 'weight': float(data['weight']), 'kind': data['kind'],
            'origin': window['origin'], 'end_exclusive': window['end_exclusive'],
            'factors': {k: window['factors'].get(k) for k in FACTOR_FIELDS},
            'strengths_available': 'strengths' in window,
            **sides, 'expected_origin': expected.date().isoformat(),
            'stale': bool(expected > pd.Timestamp(window['origin']))}


def domestic_used(fit) -> bool:
    return bool(fit['factors'].get('status') == 'fitted' and (fit.get('home') or {}).get('strength') is not None
                and (fit.get('away') or {}).get('strength') is not None)


def live_rates(ce_rates, fit):
    """(CE3n goal rates, domestic rates or None): the harness's blend (european_candidates.domestic_rates and
    blended_rates) of CE's goal rates under a frozen fit; CE's rates exactly when a side has no domestic strength
    or the factors are not fitted."""
    import european_candidates as ec
    ce_rates = [float(v) for v in ce_rates]
    if not domestic_used(fit):
        return list(ce_rates), None
    pair = {side: ({fit['kind']: tuple(float(v) for v in fit[side]['strength'])}, fit[side]['league'])
            for side in ('home', 'away')}
    domestic = ec.domestic_rates(pair, fit['factors'], fit['competition'], fit['kind'])
    return ec.blended_rates(ce_rates, domestic, float(fit['weight'])), [float(v) for v in domestic]


def live_grid(rates):
    """CE3n's score grid for its goal rates, validated exactly as the harness scores it
    (research_backtest.matrix_value of team_research.research_grid)."""
    from research_backtest import matrix_value
    from team_research import research_grid
    return matrix_value(research_grid(rates))
