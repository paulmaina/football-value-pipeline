"""Evaluation harness: one paired, time-ordered yardstick for every candidate in the plan.

Never selects, stakes or promotes a live pick. Builds on research_backtest.py.

Historical mode replays the football-data.co.uk files for the 8 domestic
leagues. The models are refit every 14 days on earlier matches only, and every
candidate is scored on the same matches:

  C  independent research model (team_form_poisson_v1, value shortlist; uses no odds)
  C2 candidate: C's goal rates with a draw and low-score correction (research_low_score.py;
     uses no odds), fitted walk-forward on C's own forecasts of matches played before the
     fold origin, pooled across leagues (low_score_candidate)
  C3 candidate: C with Understat match xG in the team form (understat_history.py; uses no
     odds). The training history before the fold origin carries each match's Understat xG,
     so the research form uses xG wherever team_research.prepare would live (both sides with
     at least five xG matches in the form). Five big leagues only; elsewhere C3 equals C.
  C5 candidate: C with its home/away split sharpened by a calibration slope (research_sharpen.py;
     uses no odds), fitted walk-forward on C's own forecasts of decided matches played before
     the fold origin, pooled across leagues; the draw is held and C5 equals C until enough
     matches exist (sharpen_candidate)
  C6 candidate: C2's grid with C5's home/away sharpening on top (research_low_score_sharpen.py;
     uses no odds). C2's (rho, delta) are fitted as for C2; the slope is fitted walk-forward
     on C2's own forecasts of decided matches played before the fold origin, pooled across
     leagues; C2's draw is held and C6 equals C2 until enough matches exist
     (low_score_sharpen_candidate)
  M  market reference: margin-free fit to Pinnacle, or to Bet365 on the holdout
  D  cagey tier: M corrected toward narrow margins (production correction)
  A  published-grid production proxy (benchmark only; mixes model and market)

Periods (configured in evaluation_harness_config.json):

  development    Aug 2022 - Jun 2025, Pinnacle. Build and choose candidates here.
  validation     Jul 2025 - 15 Jan 2026, Pinnacle. Already inspected by earlier
                 diagnostics; the cagey correction is out-of-sample from here.
  holdout        16 Jan - 10 Oct 2026, Eredivisie, Primeira Liga and Super Lig only,
                 Bet365. No earlier benchmark or live report scored these results.
                 LOCKED: scored only for one declared candidate, once per candidate
                 and once per frozen setup (code, data and config fingerprint), and
                 recorded in evaluation/holdout_ledger.json.
  retrospective  Every other match from 16 Jan 2026, Bet365. The five big leagues
                 were scored by the earlier benchmark (to 13 Oct 2026) and every
                 league from 11 Oct 2026 by the live performance reports, so these
                 results are diagnostics only, never release evidence.

Pinnacle prices in the files stop on 15 Jan 2026; Bet365 continues for every league.

On matches priced by both bookmakers before the holdout, the harness measures
how far margin-free Bet365 sits from margin-free Pinnacle. On the holdout, a
candidate must beat M by more than that gap before it counts as beating the
market. Pinnacle's average margin is reported so expected-return work can
build synthetic Pinnacle-like prices from Bet365 probabilities.

European mode (--mode european) scores the cached UCL and UEL results, plus the older
backfilled seasons (european_backfill.py; harness only), as results-only test matches
(european_results.py; periods, the European holdout, its own ledger and its 250-fixture
sample minimum in cfg['european'] and benchmark_promotion_rules.json). Each competition's
development starts where its 250-match warm-up ends. Its one candidate so far is CE, the research model as live runs
it for UCL and UEL: walk-forward folds on the competition's own results, no odds and no
domestic results. There are no historical European prices, so there is no market
reference and no market bar. The European holdout (UCL, 21 Jan 2025 - 12 Oct 2026) is
locked like the domestic one: never scored or trained on by a locked run, scored only with
a declaration, once per candidate and per frozen setup (evaluation/european_holdout_ledger.json).

Live-replay mode replays the frozen forecasts with the report's grading: each
forecast must precede the verified kickoff (performance_tracking.graded_match)
and the latest such forecast stands for its verified match. Scoring is limited
to PR #135's markets at Pinnacle (native Asian handicap, home or away win, Double
Chance 1X or X2) and to offers timestamped within 24 hours before kickoff. Each
such offer is scored for C, M, D and A, but each verified match counts once toward
the sample: its offers are averaged before pairing and week resampling.
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from concurrent.futures import ProcessPoolExecutor
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import subprocess

import numpy as np
import pandas as pd

import historical_benchmark as hb
import research_backtest as rb

VERSION = 'evaluation-harness-v2'
CONFIG = Path(__file__).with_name('evaluation_harness_config.json')
LEDGER = Path(__file__).with_name('evaluation') / 'holdout_ledger.json'
CANDIDATES = {
    'C': 'independent research model team_form_poisson_v1 (value shortlist; uses no odds)',
    'C2': "candidate: C with a draw and low-score correction (rho, delta) fitted walk-forward on C's own "
          'earlier forecasts and their scores, pooled across leagues (research_low_score.py; uses no odds)',
    'C3': 'candidate: C with historical Understat match xG in the team form, from matches before the fold '
          'origin only (understat_history.py; five big leagues, C elsewhere; uses no odds)',
    'C5': "candidate: C with its home/away split sharpened by a calibration slope fitted walk-forward on C's "
          'own earlier forecasts of decided matches, draw held, pooled across leagues (research_sharpen.py; '
          'uses no odds)',
    'C6': "candidate: C2's draw and low-score corrected grid with its home/away split sharpened by a slope "
          "fitted walk-forward on C2's own earlier forecasts of decided matches, C2's draw held, pooled across "
          'leagues (research_low_score_sharpen.py; uses no odds)',
    'M':'market reference: margin-free fit to the period bookmaker (Pinnacle, Bet365 on the holdout)',
    'D': 'cagey tier: M corrected toward narrow margins (production correction model)',
    'A': 'published-grid production proxy (benchmark only; mixes model and market)',
}
GAP_CANDIDATES = ('MP', 'MB')  # Pinnacle and Bet365 market fits on the same matches
BOOKS = {
    'pinnacle': {'hda': ('PSH', 'PSD', 'PSA'), 'ou': ('P>2.5', 'P<2.5'), 'ah': ('AHh', 'PAHH', 'PAHA')},
    'bet365': {'hda': ('B365H', 'B365D', 'B365A'), 'ou': ('B365>2.5', 'B365<2.5'), 'ah': ('AHh', 'B365AHH', 'B365AHA')},
}
DECLARATION_FIELDS = ('candidate', 'baseline', 'primary_metric', 'draw_sensitive_lines',
                      'calibration_tolerance', 'declared_by', 'declared_at')
# Everything that can change a score. The setup fingerprint hashes these files,
# the config and every input CSV, so one frozen setup is evaluated once.
SETUP_FILES = ('evaluation_harness.py', 'research_backtest.py', 'historical_benchmark.py', 'team_research.py',
               'score_probability.py', 'football_value_pipeline_v2_standalone.py', 'market_implied.py',
               'narrow_margin.py', 'price_edge_cagey_shortlist.py', 'ah_close_backtest.py',
               'evaluation_harness_config.json', 'narrow_margin_models/cagey-correction-through-2425-v1.json',
               'research_low_score.py', 'understat_history.py', 'understat_team_aliases.json',
               'research_sharpen.py', 'research_low_score_sharpen.py')
CALIBRATION_MIN_BIN = 30  # diagnostics' smallest reported band; the release rule's own minimum is in the config
PROMOTION_RULES = Path(__file__).with_name('benchmark_promotion_rules.json')


def promotion_minimums(scope='domestic') -> dict:
    """The holdout sample minimum: the domestic release gate, or the European holdout's own minimum
    (european_holdout_review_gates, decided 11 Nov 2026 before any European holdout scoring)."""
    rules = json.loads(PROMOTION_RULES.read_text(encoding='utf-8'))
    gates = rules['promotion_review_gates' if scope == 'domestic' else 'european_holdout_review_gates']
    return {'fixtures': int(gates['minimum_distinct_paired_fixtures']), 'weeks': int(gates['minimum_gameweeks'])}
GROUPS = ('1X2', 'Over 1.5', 'AH all', 'AH draw-sensitive')


# ---------------------------------------------------------------------------
# Periods and market inputs
# ---------------------------------------------------------------------------

def phase(date, league, cfg) -> str:
    date = pd.Timestamp(date)
    if date >= pd.Timestamp(cfg['holdout_start']):
        untouched = league in cfg['holdout_leagues'] and date < pd.Timestamp(cfg['holdout_end_exclusive'])
        return 'holdout' if untouched else 'retrospective'
    return 'validation' if date >= pd.Timestamp(cfg['development_end']) else 'development'


def period_book(date, cfg) -> str:
    return 'bet365' if pd.Timestamp(date) >= pd.Timestamp(cfg['holdout_start']) else 'pinnacle'


def book_prices(row, book):
    """Pre-match prices for one bookmaker, or None when any are missing or invalid."""
    cols = BOOKS[book]
    try:
        hda = tuple(float(row[k]) for k in cols['hda'])
        ou = tuple(float(row[k]) for k in cols['ou'])
        ah = tuple(float(row[k]) for k in cols['ah'])
    except (KeyError, TypeError, ValueError):
        return None
    prices = (*hda, *ou, *ah[1:])
    if not np.isfinite([*prices, ah[0]]).all() or min(prices) <= 1:
        return None
    if not .98 <= sum(1 / p for p in hda) <= 1.2 or not .98 <= sum(1 / p for p in ou) <= 1.2:
        return None
    if abs(ah[0] * 4 - round(ah[0] * 4)) > 1e-8 or not .98 <= sum(1 / p for p in ah[1:]) <= 1.2:
        return None
    return {'hda': hda, 'ou': ou, 'ah': ah}


def market_matrix(prices):
    """Margin-free score grid fitted to 1X2, totals and the main AH line (fit B)."""
    import market_implied as mi
    result = mi.fit(mi.targets_from_prices(prices['hda'], prices['ou'], prices['ah']), include_ah=True)
    if not result.usable:
        raise ValueError('; '.join(result.reasons))
    return rb.matrix_value(result.matrix)


def cagey_matrix(matrix, prices, model):
    """The production cagey correction applied to a market grid."""
    import market_implied as mi
    import narrow_margin as nm
    from price_edge_cagey_shortlist import devig_proportional
    margins, probs = mi.margin_distribution(matrix)
    p_home, p_draw, p_away = mi.devig_three_way(*prices['hda'])
    inputs = {'p_over_2_5': devig_proportional(*prices['ou'])[0], 'p_home': p_home, 'p_away': p_away, 'p_draw': p_draw}
    p2, p3 = nm.corrected_tails(model, nm.margin_tail(margins, probs, 2), nm.margin_tail(margins, probs, 3), inputs)
    return rb.matrix_value(nm.correct_matrix(matrix, p2, p3))


def overround(prices) -> float:
    return sum(1 / p for p in prices['hda']) - 1


def synthetic_prices(probabilities, margin):
    """Pinnacle-like decimal prices: margin-free probabilities plus a proportional margin."""
    probabilities = np.asarray(probabilities, dtype=float)
    if margin < 0 or not np.all((probabilities > 0) & (probabilities < 1)):
        raise ValueError('Invalid probabilities or margin')
    return 1 / (probabilities * (1 + margin))


# ---------------------------------------------------------------------------
# Candidates for one match
# ---------------------------------------------------------------------------

def research_inputs(row, train, origin, info):
    """The value model's inputs for one historical match, in team_research.INPUT_SCHEMA.

    The football-data files supply team history only: no ESPN schedules (so no cup
    or European results), no Understat xG and no news, and the history stops at the
    fold origin. The goal rates are the fold's Dixon-Coles fit without BBS statistics.
    """
    from team_research import INPUT_SCHEMA, form_history, utc
    inputs = {'home_team': row.HomeTeam, 'away_team': row.AwayTeam, 'kickoff_utc': None,
              'lambda_home': info['lambda_home'], 'lambda_away': info['lambda_away'],
              'research_history_json': json.dumps(form_history(train, row.HomeTeam, row.AwayTeam, utc(origin)))}
    assert set(inputs) == set(INPUT_SCHEMA)
    return inputs


def research_context(row, train, origin, model):
    """The research model's context for one match (goal rates from team history only, never odds)."""
    from team_research import prepare, utc
    matrix, info = model.score_matrix(row.HomeTeam, row.AwayTeam)
    return prepare(research_inputs(row, train, origin, info), utc(origin)), matrix, info


def research_matrix(row, train, origin, model):
    """C: the independent research model. Reads team history only, never odds."""
    from team_research import research_grid
    context, matrix, info = research_context(row, train, origin, model)
    return rb.matrix_value(research_grid(context['goal_rates'])), matrix, info


def low_score_matrix(goal_rates, params):
    """C2: C's goal rates on the draw and low-score corrected grid (research_low_score)."""
    import research_low_score as rls
    return rb.matrix_value(rls.adjusted_grid(goal_rates, params))


def published_proxy(matrix, info, prices, model, cfg):
    """A: production blend of the model grid toward the period bookmaker, then totals anchor."""
    from football_value_pipeline_v2_standalone import devig, reweight_matrix_to_1x2
    profile = cfg['production_v2']
    p = model.one_x_two(matrix)
    market = np.array(devig(list(prices['hda']), cfg['devig_method']), dtype=float)
    target = (1 - profile['market_weight']) * np.array([p[k] for k in ('home', 'draw', 'away')]) + profile['market_weight'] * market
    matrix = reweight_matrix_to_1x2(matrix, target)
    if profile['totals_anchor']:
        over = devig(list(prices['ou']), cfg['devig_method'])[0]
        p = model.one_x_two(matrix)
        matrix, _ = hb.anchor_totals(info['lambda_home'], info['lambda_away'], model.rho,
                                     [p[k] for k in ('home', 'draw', 'away')], float(over), cfg['max_goals'],
                                     tail_bounded=bool(info.get('score_engine_version')))
    return rb.matrix_value(matrix)


def candidates(row, train, origin, model, cfg, cagey_model, xg_train=None):
    """C, M, D and A for one match (and C3 when `xg_train` is given: the same training rows with
    Understat xG). C's goal rates go out in extra['research_goal_rates'] for C2."""
    from team_research import research_grid
    if train.Date.max() >= origin:
        raise ValueError('Training reaches prediction origin')
    if row.HomeTeam not in model.teams or row.AwayTeam not in model.teams:
        return {}, {'all': 'unresolved training team'}, {}
    matrices, gaps, extra = {}, {}, {}
    context, model_grid, info = research_context(row, train, origin, model)
    matrices['C'] = rb.matrix_value(research_grid(context['goal_rates']))
    extra['research_goal_rates'] = [float(v) for v in context['goal_rates']]
    if xg_train is not None:
        if xg_train.Date.max() >= origin:
            raise ValueError('xG training reaches prediction origin')
        if xg_train[['HxG', 'AxG']].notna().any(axis=None):
            xg_context, _, _ = research_context(row, xg_train, origin, model)
            matrices['C3'] = rb.matrix_value(research_grid(xg_context['goal_rates']))
            extra['c3_used_xg'] = 'xg' in xg_context['coverage']
        else:
            matrices['C3'], extra['c3_used_xg'] = matrices['C'], False
    book = period_book(row.Date, cfg)
    prices = book_prices(row, book)
    if prices is None:
        gaps['market'] = book + ' prices missing'
    else:
        extra['market_book'] = book
        try:
            matrices['M'] = market_matrix(prices)
            matrices['D'] = cagey_matrix(matrices['M'], prices, cagey_model)
        except (ValueError, TypeError, KeyError) as exc:
            gaps['M'] = str(exc)
        try:
            matrices['A'] = published_proxy(model_grid, info, prices, model, cfg)
        except (ValueError, TypeError, KeyError) as exc:
            gaps['A'] = str(exc)
    # Bet365-vs-Pinnacle gap: both books on the same match, before the holdout only.
    if row.Date < pd.Timestamp(cfg['holdout_start']):
        both = {b: book_prices(row, b) for b in BOOKS}
        if all(both.values()):
            try:
                matrices['MP'], matrices['MB'] = market_matrix(both['pinnacle']), market_matrix(both['bet365'])
                extra['overround'] = {b: overround(p) for b, p in both.items()}
            except (ValueError, TypeError, KeyError) as exc:
                gaps['gap'] = str(exc)
    return matrices, gaps, extra


# ---------------------------------------------------------------------------
# Historical run
# ---------------------------------------------------------------------------

def fold_windows(cfg, end):
    start = pd.Timestamp(cfg['test_start'])
    fixed = [pd.Timestamp(cfg[k]) for k in ('development_end', 'holdout_start', 'holdout_end_exclusive')] + [end]
    bounds = sorted({*pd.date_range(start, end, freq=f"{cfg['step_days']}D"), *[b for b in fixed if start < b <= end]})
    return list(zip(bounds, bounds[1:]))


def training_rows(data, league, cfg, include_holdout):
    """Locked runs never train on holdout results, so no diagnostic can carry holdout information."""
    if include_holdout:
        return data
    locked = data.Date.map(lambda d: phase(d, league, cfg) == 'holdout')
    return data.loc[~locked]


def evaluate_league(league, cache, cfg, include_holdout, keep=None):
    """Locked runs skip every holdout match. A holdout run scores ONLY holdout matches,
    and only the candidates in `keep` (declared candidate, baseline and M)."""
    from football_value_pipeline_v2_standalone import DixonColesModel
    import narrow_margin as nm
    cagey_model = nm.production_model()
    load_cfg = {**cfg, 'test_end_exclusive': cfg['end_exclusive']}
    data, sources, _ = hb.load_history(Path(cache), league, load_cfg)
    end = pd.Timestamp(cfg['end_exclusive'])
    profile = cfg['production_v2']
    records, folds, coverage, overrounds, calib, research = [], [], Counter(), [], [], []
    history = training_rows(data, league, cfg, include_holdout)
    xg_history = None
    if keep is None or 'C3' in keep:
        import understat_history as uh
        xg_data, attached = uh.with_xg(history, cache, league)
        coverage.update({f'{league}:understat_xg:{k}': v for k, v in attached.items()})
        xg_history = xg_data
    for origin, stop in fold_windows(cfg, end):
        train = history.loc[history.Date < origin]
        test = data.loc[(data.Date >= origin) & (data.Date < stop)]
        if test.empty:
            continue
        if len(train) < cfg['min_train']:
            coverage[league + ':insufficient_training'] += len(test)
            continue
        model = DixonColesModel(half_life_days=profile['half_life_days'], l2=cfg['baseline_l2'],
                                max_goals=cfg['max_goals'], shot_features=profile['shot_features'],
                                bbs_statistics=False).fit(train.copy(), as_of=origin)
        folds.append({'league': league, 'origin': origin.date().isoformat(), 'end_exclusive': stop.date().isoformat(),
                      'training_end': train.Date.max().date().isoformat(), 'training_matches': len(train)})
        for _, row in test.iterrows():
            name = phase(row.Date, league, cfg)
            if include_holdout and name != 'holdout' and keep is not None and keep & {'C2', 'C5', 'C6'} \
                    and row.HomeTeam in model.teams and row.AwayTeam in model.teams:
                # Not scored in a holdout run, but C2's, C5's and C6's walk-forward fits learn from C's forecast of it.
                context, _, _ = research_context(row, train, origin, model)
                research.append({'identity': {'league': league, 'phase': name}, 'date': row.Date,
                                 'goal_rates': [float(v) for v in context['goal_rates']],
                                 'home_goals': row.FTHG, 'away_goals': row.FTAG, 'scored': False})
            if include_holdout and name != 'holdout':
                # A holdout run still measures the Bet365-Pinnacle gap on pre-holdout matches.
                both = {b: book_prices(row, b) for b in BOOKS} if row.Date < pd.Timestamp(cfg['holdout_start']) else {}
                if not both or not all(both.values()):
                    coverage[league + ':outside_holdout_run'] += 1
                    continue
                try:
                    matrices = {'MP': market_matrix(both['pinnacle']), 'MB': market_matrix(both['bet365'])}
                except (ValueError, TypeError, KeyError):
                    continue
                identity = {'league': league, 'date': row.Date.date().isoformat(),
                            'week': f'{row.Date.isocalendar().year}-W{row.Date.isocalendar().week:02d}',
                            'fixture_key': '|'.join((league, row.Date.date().isoformat(), row.HomeTeam, row.AwayTeam)),
                            'phase': name, 'market_book': 'both'}
                records.extend(rb.score_fixture(identity, matrices, row.FTHG, row.FTAG))
                overrounds.append({b: overround(p) for b, p in both.items()})
                continue
            if name == 'holdout' and not include_holdout:
                coverage[league + ':locked_holdout'] += 1
                continue
            xg_train = None if xg_history is None else xg_history.loc[xg_history.Date < origin]
            matrices, gaps, extra = candidates(row, train, origin, model, cfg, cagey_model, xg_train)
            if 'c3_used_xg' in extra:
                coverage[f"{league}:C3:{'xg_form' if extra['c3_used_xg'] else 'goals_form'}"] += 1
            if keep is not None:
                matrices = {k: v for k, v in matrices.items() if k in keep}
            date = row.Date
            identity = {'league': league, 'date': date.date().isoformat(),
                        'week': f'{date.isocalendar().year}-W{date.isocalendar().week:02d}',
                        'fixture_key': '|'.join((league, date.date().isoformat(), row.HomeTeam, row.AwayTeam)),
                        'phase': name, 'market_book': extra.get('market_book', '')}
            if 'research_goal_rates' in extra:
                research.append({'identity': identity, 'date': date, 'goal_rates': extra['research_goal_rates'],
                                 'home_goals': row.FTHG, 'away_goals': row.FTAG, 'scored': True})
            records.extend(rb.score_fixture(identity, matrices, row.FTHG, row.FTAG))
            outcome = 0 if row.FTHG > row.FTAG else 1 if row.FTHG == row.FTAG else 2
            for cand, matrix in matrices.items():
                h, a = np.indices(matrix.shape)
                probs = [float(matrix[h > a].sum()), float(matrix[h == a].sum()), float(matrix[h < a].sum())]
                calib.append({'phase': identity['phase'], 'league': league, 'fixture_key': identity['fixture_key'],
                              'candidate': cand, 'probs': probs, 'outcome': outcome})
            if 'overround' in extra:
                overrounds.append(extra['overround'])
            for key, reason in gaps.items():
                coverage[f'{league}:{key}:{reason}'] += 1
            for key in matrices:
                coverage[f'{league}:{key}:available'] += 1
    return records, folds, coverage, overrounds, sources, calib, research


def low_score_candidate(research, cfg, end, keep=None):
    """C2 for every scored match: C's goal rates on the corrected grid, walk-forward.

    For each fold window, (rho, delta) is fitted on C's forecasts of the matches played
    before the window opens, pooled across leagues (research_low_score.fit), and applied
    to the scored matches inside it. A locked run never computes C for a holdout match,
    so no holdout result can reach the fit. Reads C's goal rates and final scores only.
    """
    import research_low_score as rls
    records, calib, coverage, fits = [], [], Counter(), []
    if (keep is not None and 'C2' not in keep) or not research:
        return records, calib, coverage, fits
    research = sorted(research, key=lambda r: r['date'])
    dates = pd.DatetimeIndex([r['date'] for r in research])
    rates = np.array([r['goal_rates'] for r in research], dtype=float)
    goals = np.array([(r['home_goals'], r['away_goals']) for r in research], dtype=float)
    half_life = cfg['production_v2']['half_life_days']
    for origin, stop in fold_windows(cfg, end):
        inside = [i for i in np.flatnonzero((dates >= origin) & (dates < stop)) if research[i]['scored']]
        if not inside:
            continue
        past = np.asarray(dates < origin)
        params = rls.fit(rates[past], goals[past, 0], goals[past, 1],
                         (origin - dates[past]).total_seconds().to_numpy() / 86400, half_life)
        fits.append({'origin': origin.date().isoformat(), 'end_exclusive': stop.date().isoformat(),
                     'scored_matches': len(inside), **params})
        for i in inside:
            r = research[i]
            try:
                matrix = low_score_matrix(r['goal_rates'], params)
            except ValueError as exc:
                coverage[f"{r['identity']['league']}:C2:{exc}"] += 1
                continue
            coverage[f"{r['identity']['league']}:C2:available"] += 1
            hg, ag = r['home_goals'], r['away_goals']
            records.extend(rb.score_fixture(r['identity'], {'C2': matrix}, hg, ag))
            h, a = np.indices(matrix.shape)
            calib.append({'phase': r['identity']['phase'], 'league': r['identity']['league'],
                          'fixture_key': r['identity']['fixture_key'], 'candidate': 'C2',
                          'probs': [float(matrix[h > a].sum()), float(matrix[h == a].sum()), float(matrix[h < a].sum())],
                          'outcome': 0 if hg > ag else 1 if hg == ag else 2})
    return records, calib, coverage, fits


def sharpen_candidate(research, cfg, end, keep=None):
    """C5 for every scored match: C's grid moved onto its sharpened 1X2, walk-forward.

    For each fold window the slope is fitted on C's forecasts of the decided matches
    played before the window opens, pooled across leagues (research_sharpen.fit), and
    applied to the scored matches inside it. C's forecasts are rebuilt from the goal
    rates C used (team_research.research_grid), so the fit reads C's own forecasts and
    the final scores only. A locked run never computes C for a holdout match, so no
    holdout result can reach the fit.
    """
    import research_sharpen as rs
    from team_research import research_grid
    records, calib, coverage, fits = [], [], Counter(), []
    if (keep is not None and 'C5' not in keep) or not research:
        return records, calib, coverage, fits
    research = sorted(research, key=lambda r: r['date'])
    dates = pd.DatetimeIndex([r['date'] for r in research])
    probs = np.array([rs.one_x_two(research_grid(r['goal_rates'])) for r in research], dtype=float)
    outcomes = np.array([0 if r['home_goals'] > r['away_goals'] else 1 if r['home_goals'] == r['away_goals'] else 2
                         for r in research])
    half_life = cfg['production_v2']['half_life_days']
    for origin, stop in fold_windows(cfg, end):
        inside = [i for i in np.flatnonzero((dates >= origin) & (dates < stop)) if research[i]['scored']]
        if not inside:
            continue
        past = np.asarray(dates < origin)
        params = rs.fit(probs[past], outcomes[past], (origin - dates[past]).total_seconds().to_numpy() / 86400,
                        half_life)
        fits.append({'origin': origin.date().isoformat(), 'end_exclusive': stop.date().isoformat(),
                     'scored_matches': len(inside), **params})
        for i in inside:
            r = research[i]
            try:
                matrix = rb.matrix_value(rs.sharpened_grid(r['goal_rates'], params))
            except ValueError as exc:
                coverage[f"{r['identity']['league']}:C5:{exc}"] += 1
                continue
            coverage[f"{r['identity']['league']}:C5:available"] += 1
            hg, ag = r['home_goals'], r['away_goals']
            records.extend(rb.score_fixture(r['identity'], {'C5': matrix}, hg, ag))
            calib.append({'phase': r['identity']['phase'], 'league': r['identity']['league'],
                          'fixture_key': r['identity']['fixture_key'], 'candidate': 'C5',
                          'probs': [float(v) for v in rs.one_x_two(matrix)], 'outcome': int(outcomes[i])})
    return records, calib, coverage, fits


def low_score_sharpen_candidate(research, cfg, end, keep=None):
    """C6 for every scored match: C2's grid moved onto its sharpened 1X2, walk-forward.

    First C2 is rebuilt for every match C forecast, scored or not: (rho, delta) for the
    window holding the match, fitted on C's forecasts of matches before that window opens
    (research_low_score.fit, exactly as low_score_candidate), so each match carries the
    forecast C2 made of it. Then, for each window, the slope is fitted on C2's forecasts of
    the decided matches played before the window opens, pooled across leagues
    (research_sharpen.fit), and applied to C2's grid of the scored matches inside it. A
    neutral slope gives C2 exactly. A locked run never computes C for a holdout match, so
    no holdout result can reach either fit. Reads C's goal rates and final scores only.
    """
    import research_low_score as rls
    import research_low_score_sharpen as c6
    records, calib, coverage, fits = [], [], Counter(), []
    if (keep is not None and 'C6' not in keep) or not research:
        return records, calib, coverage, fits
    research = sorted(research, key=lambda r: r['date'])
    dates = pd.DatetimeIndex([r['date'] for r in research])
    rates = np.array([r['goal_rates'] for r in research], dtype=float)
    goals = np.array([(r['home_goals'], r['away_goals']) for r in research], dtype=float)
    outcomes = np.where(goals[:, 0] > goals[:, 1], 0, np.where(goals[:, 0] == goals[:, 1], 1, 2))
    half_life = cfg['production_v2']['half_life_days']
    windows = fold_windows(cfg, end)
    low = [None] * len(research)
    c2_probs = np.full((len(research), 3), np.nan)  # NaN: C2 made no forecast (invalid grid); left out of the fit
    for origin, stop in windows:
        inside = np.flatnonzero((dates >= origin) & (dates < stop))
        if not len(inside):
            continue
        past = np.asarray(dates < origin)
        params = rls.fit(rates[past], goals[past, 0], goals[past, 1],
                         (origin - dates[past]).total_seconds().to_numpy() / 86400, half_life)
        for i in inside:
            low[i] = params
            try:
                c2_probs[i] = c6.c2_one_x_two(rates[i], params)
            except ValueError:
                pass
    for origin, stop in windows:
        inside = [i for i in np.flatnonzero((dates >= origin) & (dates < stop)) if research[i]['scored']]
        if not inside:
            continue
        past = np.asarray(dates < origin) & np.isfinite(c2_probs).all(axis=1)
        params = c6.fit_slope(c2_probs[past], outcomes[past], (origin - dates[past]).total_seconds().to_numpy() / 86400,
                              half_life)
        low_score = low[inside[0]]
        fits.append({'origin': origin.date().isoformat(), 'end_exclusive': stop.date().isoformat(),
                     'scored_matches': len(inside), **params,
                     'low_score': {k: low_score.get(k) for k in ('rho', 'delta', 'status')}})
        for i in inside:
            r = research[i]
            try:
                matrix = rb.matrix_value(c6.grid(r['goal_rates'], low[i], params))
            except ValueError as exc:
                coverage[f"{r['identity']['league']}:C6:{exc}"] += 1
                continue
            coverage[f"{r['identity']['league']}:C6:available"] += 1
            hg, ag = r['home_goals'], r['away_goals']
            records.extend(rb.score_fixture(r['identity'], {'C6': matrix}, hg, ag))
            h, a = np.indices(matrix.shape)
            calib.append({'phase': r['identity']['phase'], 'league': r['identity']['league'],
                          'fixture_key': r['identity']['fixture_key'], 'candidate': 'C6',
                          'probs': [float(matrix[h > a].sum()), float(matrix[h == a].sum()), float(matrix[h < a].sum())],
                          'outcome': int(outcomes[i])})
    return records, calib, coverage, fits


# ---------------------------------------------------------------------------
# Summaries
# ---------------------------------------------------------------------------

def fixture_scores(records, draw_lines=(-.5, 0., .5)) -> pd.DataFrame:
    """One log loss per fixture, candidate and group; AH groups average their lines per fixture."""
    if not records:
        return pd.DataFrame(columns=['fixture_key', 'league', 'week', 'phase', 'candidate', 'group', 'log_loss'])
    frame = pd.DataFrame(records)
    frame['line'] = frame.market.str.extract(r'^AH ([+-]\d\.\d\d)$')[0].astype(float)
    parts = []
    for group, mask in (('1X2', frame.market == '1X2'), ('Over 1.5', frame.market == 'Over 1.5'),
                        ('AH all', frame.line.notna()), ('AH draw-sensitive', frame.line.round(2).isin([round(float(v), 2) for v in draw_lines]))):
        part = frame.loc[mask].groupby(['fixture_key', 'league', 'week', 'phase', 'candidate'], as_index=False).log_loss.mean()
        parts.append(part.assign(group=group))
    return pd.concat(parts, ignore_index=True)


def paired(scores, baseline, candidate, samples=2000, seed=136):
    """Baseline minus candidate log loss (positive = candidate better), resampling whole weeks."""
    table = scores.pivot_table(index=['fixture_key', 'week'], columns='candidate', values='log_loss')
    if baseline not in table or candidate not in table:
        return None
    pairs = table[[baseline, candidate]].dropna()
    if pairs.empty:
        return None
    gain = (pairs[baseline] - pairs[candidate]).rename('gain').reset_index()
    weeks = gain.groupby('week').gain.agg(['sum', 'count'])
    interval = None
    if len(weeks) >= 2:
        draws = np.random.default_rng(seed).integers(0, len(weeks), size=(samples, len(weeks)))
        means = weeks['sum'].to_numpy()[draws].sum(1) / weeks['count'].to_numpy()[draws].sum(1)
        interval = [float(v) for v in np.quantile(means, [.025, .975])]
    return {'fixtures': len(pairs), 'weeks': len(weeks), 'mean_gain': float(gain.gain.mean()),
            'interval_95': interval, 'clear_of_zero': bool(interval and interval[0] > 0)}


def common_cohort(scores, names=('C', 'C2', 'C3', 'C5', 'C6', 'M', 'D', 'A')):
    """Mean log loss on the fixtures where every named candidate is available."""
    output = []
    for (name, group), part in scores.groupby(['phase', 'group']):
        table = part.pivot_table(index='fixture_key', columns='candidate', values='log_loss')
        present = [n for n in names if n in table]
        if len(present) < 2:
            continue
        common = table[present].dropna()
        output.append({'phase': name, 'group': group, 'fixtures': len(common),
                       **{n: float(common[n].mean()) for n in present}})
    return output


def bookmaker_gap(scores):
    gap = {}
    pre = scores.loc[scores.phase.isin(['development', 'validation'])]
    for group in GROUPS:
        result = paired(pre.loc[pre.group == group], 'MB', 'MP')
        if result:
            gap[group] = {**result, 'bet365_minus_pinnacle_log_loss': result['mean_gain']}
    return gap


def summarize(records, overrounds, coverage, cfg, metadata):
    scores = fixture_scores(records, cfg['draw_sensitive_lines'])
    available = (scores.groupby(['phase', 'group', 'candidate']).log_loss.agg(['mean', 'count']).reset_index()
                 .to_dict('records') if not scores.empty else [])
    gap = bookmaker_gap(scores)
    margins = {b: float(np.mean([o[b] for o in overrounds])) for b in BOOKS} if overrounds else {}
    comparisons = {}
    for name in sorted(scores.phase.unique()) if not scores.empty else []:
        part = scores.loc[scores.phase == name]
        comparisons[name] = {}
        for group in GROUPS:
            sub = part.loc[part.group == group]
            entry = {}
            for base, cand in (('C', 'C2'), ('C', 'C3'), ('C2', 'C3'), ('C', 'C5'), ('C2', 'C5'), ('C3', 'C5'),
                               ('C', 'C6'), ('C2', 'C6'), ('C5', 'C6'), ('C', 'M'), ('C', 'D'), ('C', 'A'), ('M', 'D')):
                result = paired(sub, base, cand)
                if result:
                    entry[f'{cand}_vs_{base}'] = result
            versus = paired(sub, 'M', 'C')
            if versus:
                bar = max(0., gap.get(group, {}).get('bet365_minus_pinnacle_log_loss', 0.)) \
                    if name in ('holdout', 'retrospective') else 0.
                entry['C_vs_M'] = {**versus, 'gap_bar': bar, 'gain_after_gap_bar': versus['mean_gain'] - bar}
            comparisons[name][group] = entry
    return {'version': VERSION, 'candidates': CANDIDATES, 'config': cfg, **metadata,
            'coverage': dict(coverage),
            'log_loss_common_cohort': common_cohort(scores) if not scores.empty else [],
            'log_loss_all_available': available, 'paired': comparisons,
            'bet365_gap': gap, 'average_margin': margins,
            'synthetic_price_margin': margins.get('pinnacle'),
            'notes': ['Headline means use the common cohort: fixtures where C, C2, C3, C5, C6, M, D and A are all '
                      'available (C3 and C5 exist wherever C does, C6 wherever C2 does).',
                      'Positive mean_gain means the first-named candidate has the lower log loss than the second.',
                      'Intervals resample whole calendar weeks across all leagues.',
                      'The cagey correction was trained on seasons through 2024/25; D is in-sample in development.',
                      'Retrospective results were already scored elsewhere; they are diagnostics, never release evidence.',
                      'Historical prices are pre-match snapshots without timestamps; returns are not claimed.',
                      'No automatic promotion: every production change goes through a reviewed PR.']}


def calibration(rows) -> list[dict]:
    """1X2 reliability per phase and candidate: deciles of each outcome's forecast probability."""
    bins = defaultdict(list)
    for r in rows:
        for k, outcome in enumerate(('home', 'draw', 'away')):
            p = r['probs'][k]
            bins[(r['phase'], r['candidate'], outcome, min(9, int(p * 10)))].append((p, int(r['outcome'] == k)))
    return [{'phase': k[0], 'candidate': k[1], 'outcome': k[2], 'bin_lower': k[3] / 10, 'n': len(v),
             'mean_forecast': float(np.mean([p for p, _ in v])), 'observed_rate': float(np.mean([y for _, y in v]))}
            for k, v in sorted(bins.items())]


def calibration_slope(p, y) -> float:
    """Logistic calibration slope b of logit P(y) = a + b * logit(p), by Newton's method (b > 1: too flat).
    NaN when it is undefined (constant forecasts, or a single outcome); NaN fails any slope tolerance."""
    p = np.clip(np.asarray(p, float), 1e-6, 1 - 1e-6)
    x = np.column_stack([np.ones(len(p)), np.log(p / (1 - p))])
    w = np.zeros(2)
    for _ in range(50):
        q = 1 / (1 + np.exp(-x @ w))
        try:
            step = np.linalg.solve((x * (q * (1 - q))[:, None]).T @ x, x.T @ (np.asarray(y, float) - q))
        except np.linalg.LinAlgError:
            return float('nan')
        if not np.isfinite(step).all():
            return float('nan')
        w += step
        if np.abs(step).max() < 1e-10:
            break
    return float(w[1])


def band_z_threshold(alpha, bands) -> float:
    """Two-sided normal quantile for alpha / bands (Bonferroni over the bands checked): about 3.02 for
    alpha 0.05 and 20 bands."""
    from statistics import NormalDist
    return float(NormalDist().inv_cdf(1 - alpha / (2 * max(1, bands))))


def calibration_check(rows, rule) -> dict:
    """The configured calibration tolerance (cfg['calibration_tolerance']) on one candidate's 1X2 forecasts
    in one period: the logistic calibration slope of each named outcome inside [slope_min, slope_max], and
    no failing outcome band (home, draw and away; width band_width; at least band_min_matches forecasts).

    v1 (no band_alpha in the rule): a band fails when it is more than band_max_deviation from its observed
    rate. v2 (band_alpha set): it fails only when it is more than band_max_deviation away AND the gap is
    statistically clear, |gap| / sqrt(p(1 - p) / n) above band_z_threshold(band_alpha, bands checked), with
    p the band's mean forecast. Fails when there are no forecasts."""
    rows = list(rows)
    out = {'rule': rule['name'], 'forecasts': len(rows)}
    if not rows:
        return {**out, 'slopes': {}, 'slopes_pass': False, 'bands_checked': 0, 'band_z_threshold': None,
                'failing_bands': [], 'worst_band': None, 'bands_pass': False, 'passes': False}
    probs = np.array([r['probs'] for r in rows], dtype=float)
    outcomes = np.array([r['outcome'] for r in rows])
    names = ('home', 'draw', 'away')
    slopes = {o: calibration_slope(probs[:, names.index(o)], outcomes == names.index(o)) for o in rule['slope_outcomes']}
    slopes_pass = all(rule['slope_min'] <= v <= rule['slope_max'] for v in slopes.values())
    nbins = int(round(1 / rule['band_width']))
    bands = []
    for k, outcome in enumerate(names):
        p, y = probs[:, k], (outcomes == k).astype(float)
        index = np.minimum(nbins - 1, (p * nbins).astype(int))
        for b in np.unique(index):
            m = index == b
            if m.sum() >= rule['band_min_matches']:
                n, mean = int(m.sum()), float(p[m].mean())
                deviation = float(y[m].mean() - mean)
                se = float(np.sqrt(mean * (1 - mean) / n))
                bands.append({'outcome': outcome, 'band_lower': b / nbins, 'n': n,
                              'mean_forecast': mean, 'observed_rate': float(y[m].mean()),
                              'observed_minus_forecast': deviation,
                              'z': abs(deviation) / se if se > 0 else float('inf')})
    worst = max(bands, key=lambda b: abs(b['observed_minus_forecast'])) if bands else None
    z_bar = band_z_threshold(rule['band_alpha'], len(bands)) if 'band_alpha' in rule else None
    failing = [b for b in bands if abs(b['observed_minus_forecast']) > rule['band_max_deviation']
               and (z_bar is None or b['z'] > z_bar)]
    return {**out, 'slopes': slopes, 'slopes_pass': bool(slopes_pass), 'bands_checked': len(bands),
            'band_z_threshold': z_bar, 'failing_bands': failing, 'worst_band': worst, 'bands_pass': not failing,
            'passes': bool(slopes_pass and not failing)}


def calibration_checks(calib, rule) -> dict:
    """calibration_check for every period and candidate in `calib` (gap fits excluded)."""
    groups = defaultdict(list)
    for r in calib:
        if r['candidate'] not in GAP_CANDIDATES:
            groups[(r['phase'], r['candidate'])].append(r)
    output = defaultdict(dict)
    for (name, cand), rows in sorted(groups.items()):
        output[name][cand] = calibration_check(rows, rule)
    return dict(output)


# ---------------------------------------------------------------------------
# Holdout lock
# ---------------------------------------------------------------------------

def file_sha256(path) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def setup_fingerprint(cfg, cache, root=Path(__file__).parent) -> dict:
    """Hash of everything that can change a score: scoring code, model files, config and input data."""
    parts = {name: file_sha256(root / name) for name in SETUP_FILES}
    for league in cfg['leagues']:
        for season in cfg['seasons']:
            name = f"{season}_{hb.CODES[league]}.csv"
            parts['data/' + name] = file_sha256(Path(cache) / name)
    import understat_history as uh
    for league in cfg['leagues']:
        for path in uh.files(cache, league) if league in uh.LEAGUES else []:
            parts['data/understat/' + path.name] = file_sha256(path)
    digest = hashlib.sha256(json.dumps({'parts': parts, 'config': cfg}, sort_keys=True).encode()).hexdigest()
    return {'sha256': digest, 'parts': parts}


def validate_declaration(path, cfg, setup, ledger=LEDGER, candidates=None):
    """A declaration names one registered candidate and how it is judged. It must match the
    configured scoring, and neither the candidate nor the frozen setup may have been scored before.
    `candidates` is the registry it must name (CANDIDATES; EUROPEAN_CANDIDATES for the European holdout)."""
    registry = CANDIDATES if candidates is None else candidates
    data = json.loads(Path(path).read_text(encoding='utf-8'))
    missing = [k for k in DECLARATION_FIELDS if data.get(k) in (None, '', [])]
    if missing:
        raise ValueError('Declaration missing ' + ', '.join(missing))
    if data['candidate'] not in registry or data['baseline'] not in registry or data['candidate'] == data['baseline']:
        raise ValueError('Candidate and baseline must be two different candidates registered in the harness')
    if data['primary_metric'] not in GROUPS:
        raise ValueError('Primary metric must be one of ' + ', '.join(GROUPS))
    if sorted(round(float(v), 2) for v in data['draw_sensitive_lines']) != sorted(round(float(v), 2) for v in cfg['draw_sensitive_lines']):
        raise ValueError('Draw-sensitive lines differ from the configured scoring; change the config in a reviewed PR first')
    rule = cfg['calibration_tolerance']
    if data['calibration_tolerance'] != rule['name']:
        raise ValueError(f"Calibration tolerance must name the configured rule {rule['name']!r}; "
                         'change the config in a reviewed PR first')
    entries = json.loads(ledger.read_text(encoding='utf-8')) if ledger.exists() else []
    if any(e['candidate'] == data['candidate'] for e in entries):
        raise ValueError(f"Holdout already scored for candidate {data['candidate']!r}")
    if any(e.get('setup_sha256') == setup['sha256'] for e in entries):
        raise ValueError('Holdout already scored for this frozen setup (same code, data and config)')
    digest = hashlib.sha256(json.dumps(data, sort_keys=True).encode()).hexdigest()
    return {**data, 'calibration_rule': rule, 'sha256': digest}


def holdout_verdict(records, calib, declaration, gap, minimum=None):
    """Apply the declaration: primary metric, draw-sensitive lines, the configured calibration
    tolerance (calibration_check on the candidate's holdout forecasts) and the market bar.
    `minimum` is the sample minimum (promotion_minimums(); the European holdout passes its own)."""
    scores = fixture_scores(records, declaration['draw_sensitive_lines'])
    hold = scores.loc[scores.phase == 'holdout']
    cand, base = declaration['candidate'], declaration['baseline']
    primary = paired(hold.loc[hold.group == declaration['primary_metric']], base, cand)
    draw = paired(hold.loc[hold.group == 'AH draw-sensitive'], base, cand)
    calibrated = calibration_check([r for r in calib if r['phase'] == 'holdout' and r['candidate'] == cand],
                                   declaration['calibration_rule'])
    market = paired(hold.loc[hold.group == declaration['primary_metric']], 'M', cand) if cand != 'M' else None
    bar = max(0., gap.get(declaration['primary_metric'], {}).get('bet365_minus_pinnacle_log_loss', 0.))
    minimum = minimum or promotion_minimums()
    enough = bool(primary and primary['fixtures'] >= minimum['fixtures'] and primary['weeks'] >= minimum['weeks'])
    passed = bool(enough and primary and primary['clear_of_zero'] and calibrated['passes'])
    return {'candidate': cand, 'baseline': base, 'primary_metric': declaration['primary_metric'],
            'primary': primary, 'draw_sensitive': draw,
            'sample_minimum': minimum, 'sample_minimum_met': enough,
            'calibration': calibrated, 'calibration_tolerance': declaration['calibration_rule'],
            'versus_market': {**market, 'gap_bar': bar, 'beats_market_after_gap': market['mean_gain'] - bar > 0
                              and market['interval_95'] is not None and market['interval_95'][0] > bar} if market else None,
            'passes_holdout_gate': passed,
            'next_steps': 'Passing the holdout is necessary, not sufficient: parity test and live replay follow, then a reviewed PR.'}


def record_holdout(declaration, setup, commit, fixtures, verdict, ledger=LEDGER):
    entries = json.loads(ledger.read_text(encoding='utf-8')) if ledger.exists() else []
    entries.append({'candidate': declaration['candidate'], 'baseline': declaration['baseline'],
                    'declaration_sha256': declaration['sha256'], 'setup_sha256': setup['sha256'],
                    'source_commit': commit, 'holdout_fixtures': fixtures,
                    'passes_holdout_gate': verdict['passes_holdout_gate'],
                    'scored_at_utc': datetime.now(timezone.utc).isoformat()})
    ledger.parent.mkdir(parents=True, exist_ok=True)
    ledger.write_text(json.dumps(entries, indent=2) + '\n', encoding='utf-8')


# ---------------------------------------------------------------------------
# Live replay
# ---------------------------------------------------------------------------

def usable_results(records, root, coverage=None, clock=None):
    """The report's result checks: a verified source, and for Turkish T1 results the retained
    source CSV must validate (turkey_results.validate_evidence). Anything else is not scored."""
    import performance_tracking as pt
    from turkey_results import validate_evidence
    clock = clock or pd.Timestamp.now(tz='UTC')
    coverage = coverage if coverage is not None else Counter()
    output, evidence_cache = [], {}
    for record in records:
        if not isinstance(record, dict):
            continue
        try:
            if not pt.verified_result_source(record):
                raise ValueError('unverified result source')
            if record.get('league_code') == 'T1':
                validate_evidence(root, record, clock, evidence_cache=evidence_cache)
        except (OSError, ValueError, KeyError) as exc:
            coverage['result_rejected:' + str(exc)[:60]] += 1
            continue
        output.append(record)
    return output


# PR #135's markets, as events on the score grid. Draw, 12, totals, draw-no-bet
# and every non-Pinnacle offer are out of scope.
BINARY_MARKETS = {'Home win': lambda h, a: h > a, 'Away win': lambda h, a: h < a,
                  'Double Chance 1X': lambda h, a: h >= a, 'Double Chance X2': lambda h, a: h <= a}
DOUBLE_CHANCE_KEYS = {'home_draw': 'Double Chance 1X', 'draw_away': 'Double Chance X2'}
NATIVE_AH_KEYS = ('spreads', 'alternate_spreads')
OFFER_WINDOW = pd.Timedelta(hours=24)
LIVE_GROUPS = ('All offers', 'Asian handicap', 'AH draw-sensitive', 'Win', 'Double chance')
SETTLEMENT_INDEX = {(1., 0.): 0, (.5, 0.): 1, (0., 0.): 2, (0., .5): 3, (0., 1.): 4}


def scoped_offers(row, kickoff, cutoff, coverage=None):
    """The frozen row's offers in PR #135's scope: Pinnacle only; native Asian handicap
    (spreads or alternate spreads, one offer per side and line), home or away win, and
    Double Chance 1X or X2. Each must be timestamped within the 24 hours before kickoff
    and no later than the forecast (cutoff)."""
    import asian_handicap
    from price_edge_shortlist import _json_list, _price, pinnacle_quotes
    from team_research import utc
    coverage = coverage if coverage is not None else Counter()
    found = []
    h2h = pinnacle_quotes(row)['h2h']
    if h2h is not None:
        found += [{'market': 'Home win', 'group': 'Win', 'price': h2h[0], 'stamp': h2h[3]},
                  {'market': 'Away win', 'group': 'Win', 'price': h2h[2], 'stamp': h2h[3]}]
    for quote in _json_list(row.get('price_edge_quotes')):
        if isinstance(quote, dict) and quote.get('bookmaker') == 'Pinnacle' and quote.get('market') == 'double_chance':
            for key, market in DOUBLE_CHANCE_KEYS.items():
                price = _price((quote.get('prices') or {}).get(key))
                if price:
                    found.append({'market': market, 'group': 'Double chance', 'price': price,
                                  'stamp': quote.get('last_update_utc')})
    handicaps = {}
    for offer in _json_list(row.get('asian_handicap_offers')):
        if not isinstance(offer, dict) or offer.get('bookmaker') != 'Pinnacle':
            continue
        if offer.get('market_key') not in NATIVE_AH_KEYS:
            coverage['offer_out_of_scope:pinnacle ' + str(offer.get('market_key'))] += 1
            continue
        price, side = _price(offer.get('price')), offer.get('side')
        try:
            point = asian_handicap.line(offer.get('line'))
        except (ValueError, TypeError):
            point = None
        if not price or side not in ('home', 'away') or point is None:
            coverage['offer_out_of_scope:invalid handicap offer'] += 1
            continue
        item = {'market': asian_handicap.label(side, point), 'group': 'Asian handicap', 'side': side,
                'line': point, 'price': price, 'stamp': offer.get('last_update_utc'),
                'source_market': offer.get('market_key')}
        # One offer per side and line: the main-line copy wins over its alternate duplicate.
        held = handicaps.get((side, point))
        if held is None or (held['source_market'] != 'spreads' and item['source_market'] == 'spreads'):
            handicaps[(side, point)] = item
    found += handicaps.values()
    output = []
    for offer in found:
        stamp = utc(offer['stamp'])
        if pd.isna(stamp):
            reason = 'no timestamp'
        elif stamp > cutoff or stamp >= kickoff:
            reason = 'after forecast'
        elif stamp < kickoff - OFFER_WINDOW:
            reason = 'older than 24h before kickoff'
        else:
            output.append({**offer, 'stamp': stamp})
            continue
        coverage['offer_excluded:' + reason] += 1
    return output


def score_offers(identity, matrices, offers, home_goals, away_goals, draw_lines=(-.5, 0., .5)):
    """One record per offer and candidate: binary log loss for win and Double Chance, the
    five-way settlement log loss for Asian handicap (quarter lines included)."""
    from ah_close_backtest import outcome_probabilities, settle
    if any(not np.isfinite(v) or v < 0 or int(v) != v for v in (home_goals, away_goals)):
        raise ValueError('Invalid regulation score')
    draw_lines = {round(float(v), 2) for v in draw_lines}
    records = []
    for candidate, matrix in matrices.items():
        matrix = rb.matrix_value(matrix)
        h, a = np.indices(matrix.shape)
        for offer in offers:
            base = {**identity, 'candidate': candidate, 'market': offer['market'], 'market_group': offer['group'],
                    'offered_decimal_odds': offer['price'], 'offer_utc': offer['stamp'].isoformat()}
            if offer['group'] == 'Asian handicap':
                sign = 1 if offer['side'] == 'home' else -1
                masses = outcome_probabilities((sign * (h - a)).ravel(), matrix.ravel(), offer['line'])
                won, lost = settle(sign * (home_goals - away_goals), offer['line'])
                probs, outcome = np.array([masses[k] for k in rb.KINDS]), SETTLEMENT_INDEX[(float(won), float(lost))]
                base.update(handicap_side=offer['side'], handicap_line=offer['line'],
                            draw_sensitive=round(offer['line'], 2) in draw_lines)
            else:
                event = BINARY_MARKETS[offer['market']]
                p = float(matrix[event(h, a)].sum())
                probs, outcome = np.array([1 - p, p]), int(event(home_goals, away_goals))
                base.update(probability=p, won=outcome)
            records.append({**base, 'log_loss': float(-np.log(max(probs[outcome], 1e-15))),
                            'brier': float(np.sum((probs - np.eye(len(probs))[outcome]) ** 2))})
    return records


def match_scores(records) -> pd.DataFrame:
    """One log loss per verified match, candidate and group: the mean over that match's offers,
    so each match counts once toward the sample however many offers it carried."""
    columns = ['fixture_key', 'league', 'week', 'phase', 'candidate', 'group', 'log_loss', 'offers']
    if not records:
        return pd.DataFrame(columns=columns)
    frame = pd.DataFrame(records)
    sensitive = (frame['draw_sensitive'] if 'draw_sensitive' in frame else pd.Series(False, index=frame.index))
    sensitive = sensitive.fillna(False).astype(bool)
    parts = []
    for group, mask in (('All offers', frame.market_group.notna()),
                        ('Asian handicap', frame.market_group == 'Asian handicap'),
                        ('AH draw-sensitive', sensitive), ('Win', frame.market_group == 'Win'),
                        ('Double chance', frame.market_group == 'Double chance')):
        part = (frame.loc[mask].groupby(['fixture_key', 'league', 'week', 'phase', 'candidate'], as_index=False)
                .log_loss.agg(log_loss='mean', offers='count'))
        parts.append(part.assign(group=group))
    return pd.concat(parts, ignore_index=True)[columns]


def offer_counts(records) -> dict:
    """Matches and distinct offers scored, overall, per market group and per market."""
    if not records:
        return {'matches': 0, 'offers': 0, 'per_group': {}, 'per_market': {}}
    offers = pd.DataFrame(records).drop_duplicates(['fixture_key', 'market'])

    def grouped(key):
        return {name: {'matches': int(part.fixture_key.nunique()), 'offers': len(part)}
                for name, part in offers.groupby(key)}
    return {'matches': int(offers.fixture_key.nunique()), 'offers': len(offers),
            'per_group': grouped('market_group'), 'per_market': grouped('market')}


def offer_calibration(records) -> list[dict]:
    """Reliability of the binary offers (win and Double Chance) per candidate: probability deciles."""
    bins = defaultdict(list)
    for r in records:
        if r.get('market_group') in ('Win', 'Double chance'):
            p = r['probability']
            bins[(r['candidate'], r['market_group'], min(9, int(p * 10)))].append((p, r['won']))
    return [{'candidate': k[0], 'market_group': k[1], 'bin_lower': k[2] / 10, 'n': len(v),
             'mean_forecast': float(np.mean([p for p, _ in v])), 'observed_rate': float(np.mean([y for _, y in v]))}
            for k, v in sorted(bins.items())]


def live_replay(root):
    """Frozen forecasts graded exactly as the performance report grades them; one forecast
    (the latest made before the verified kickoff) stands for each verified match. Every
    in-scope offer on that forecast (scoped_offers) is scored for C (frozen research),
    M (fit to frozen Pinnacle quotes), D (cagey) and A (published grid)."""
    import narrow_margin as nm
    import performance_tracking as pt
    from price_edge_shortlist import pinnacle_quotes
    from team_research import utc
    cagey_model = nm.production_model()
    verified = pt.load_json(root / 'performance' / 'verified_results.json', {})
    coverage, latest = Counter(), {}
    results = usable_results(verified.values() if isinstance(verified, dict) else verified, root, coverage)
    for meta, rows, _ in pt.snapshots(root):
        for row in rows:
            frozen = {**row, 'snapshot_generated_utc': meta['generated_at_utc'],
                      'snapshot_captured_utc': meta['captured_at_utc']}
            final, state = pt.graded_match(frozen, results)
            if final is None:
                coverage['ungraded:' + state] += 1
                continue
            identity = (final.get('league_code'), str(final.get('match_id')))
            generated = utc(meta['generated_at_utc'])
            # The latest forecast made before the verified kickoff stands for the match.
            if identity not in latest or generated > latest[identity][0]:
                latest[identity] = (generated, frozen, final)
    records = []
    for identity, (generated, row, final) in sorted(latest.items()):
        # The kickoff the lead check used: the verified one when the result carries it.
        kickoff = utc(final.get('kickoff_utc')) if 'kickoff_utc' in final else utc(row.get('kickoff_utc'))
        offers = scoped_offers(row, kickoff, generated, coverage)
        if not offers:
            coverage['no_in_scope_offer'] += 1
            continue
        matrices, gaps = rb.archived_candidates(row, generated)
        if 'B' in matrices:
            matrices['M'] = matrices.pop('B')
            pin = pinnacle_quotes(row)
            if pin['h2h'] is not None and pin['ou25'] is not None:
                try:
                    matrices['D'] = cagey_matrix(matrices['M'], {'hda': pin['h2h'][:3], 'ou': pin['ou25'][:2]}, cagey_model)
                except (ValueError, TypeError, KeyError) as exc:
                    gaps['D'] = str(exc)
        for key, reason in gaps.items():
            coverage[key.replace('B', 'M') + ':' + reason] += 1
        date = pd.Timestamp(str(row['kickoff_utc'])[:10])
        ident = {'league': row['league'], 'date': date.date().isoformat(),
                 'week': f'{date.isocalendar().year}-W{date.isocalendar().week:02d}',
                 'fixture_key': ':'.join(identity), 'phase': 'live_replay', 'market_book': 'pinnacle'}
        if not matrices:
            coverage['no_candidate_available'] += 1
            continue
        coverage['matches_scored'] += 1
        records.extend(score_offers(ident, matrices, offers, final['home_goals'], final['away_goals']))
    coverage['verified_matches_graded'] = len(latest)
    return records, coverage


# ---------------------------------------------------------------------------
# Parity of C between the harness and the live pipeline
# ---------------------------------------------------------------------------

LIVE_LEAGUES = {'Premier League': 'EPL', 'La Liga': 'LaLiga', 'Bundesliga': 'Bundesliga', 'Serie A': 'SerieA',
                'Ligue 1': 'Ligue1', 'Eredivisie': 'Eredivisie', 'Primeira Liga': 'PrimeiraLiga',
                'Super Lig': 'SuperLig', 'Süper Lig': 'SuperLig'}
DERIVED_EVIDENCE = ('quality_review', 'rest_and_travel')  # written by enrich()/prepare(), not inputs
TRAINING_HISTORY = 'pipeline training history'
EVIDENCE_CLASSES = ('league', 'off_league_in_season', 'off_league_before_season', 'holdout_period_unchecked',
                    'double_counted')
# Holdout leagues lose their locked-period results (16 Jan - 10 Oct 2026) from every
# harness fit, so their parity is reported apart from the other leagues.
LEAGUE_GROUPS = ('holdout_leagues', 'other_domestic', 'no_football_data')


def _hda(margins) -> list[float]:
    m = {int(d): float(p) for d, p in margins.items()}
    return [sum(p for d, p in m.items() if d > 0), m.get(0, 0.), sum(p for d, p in m.items() if d < 0)]


def _max_gap(a, b) -> float:
    return max(abs(float(a.get(k, 0.)) - float(b.get(k, 0.))) for k in set(a) | set(b))


def _result_key(r):
    from team_research import name, utc
    return utc(r.get('date')).date().isoformat(), name(r.get('home')), name(r.get('away'))


def _used_rows(inputs, evidence, cutoff, side, version=None):
    """The ten results prepare() keeps for one side, under the forecast's research version.

    Like prepare(), all pre-kickoff evidence is dropped when any source was observed after the cutoff.
    """
    from team_research import VERSION, decode, form_rows, history_name, observed_by, research_evidence
    version = version or VERSION
    history = decode(inputs.get('research_history_json'))
    rows = list(history.get(side, []))
    if observed_by(evidence, cutoff):
        rows += research_evidence(evidence).get('recent', {}).get(side, [])
    return form_rows(inputs.get(side + '_team'), rows, cutoff, version, history_name(history, side, version))


def _team_day(r, team):
    """(day, team, venue side, home goals, away goals): identifies a result whatever the opponent is called."""
    from team_research import name, utc
    side = 'home' if name(r.get('home')) == name(team) else 'away'
    return utc(r.get('date')).date().isoformat(), name(team), side, int(r['home_goals']), int(r['away_goals'])


def league_index(history):
    """Lookup for _classify. Build it from the holdout-free history (training_rows), never the full files."""
    results = set()
    for d, h, a, hg, ag in zip(history.Date, history.HomeTeam, history.AwayTeam, history.FTHG, history.FTAG):
        for team in (h, a):
            results.add(_team_day({'date': d, 'home': h, 'away': a, 'home_goals': hg, 'away_goals': ag}, team))
    starts = {}
    if len(history):
        for year in range(history.Date.min().year, history.Date.max().year + 1):
            later = history.Date.loc[history.Date >= pd.Timestamp(f'{year}-07-01')]
            if len(later):
                starts[year] = later.min()
    return results, starts


def _classify(r, team, league_results, season_starts, locked=None):
    """League result in the football-data file (matched on day +/- 1, team, venue and
    score, since ESPN and the files name opponents differently), or a game they don't have.

    `locked(date)` is true inside a holdout league's holdout window. The lookup has no
    results there, so those rows can't be checked and are counted apart.
    """
    from team_research import utc
    day, key, side, hg, ag = _team_day(r, team)
    days = {day, *[(utc(r['date']) + pd.Timedelta(days=k)).date().isoformat() for k in (-1, 1)]}
    if any((d, key, side, hg, ag) in league_results for d in days):
        return 'league'
    date = utc(r['date']).tz_convert(None)
    if locked is not None and locked(date):
        return 'holdout_period_unchecked'
    start = season_starts.get(date.year if date.month >= 7 else date.year - 1)
    return 'off_league_before_season' if start is not None and date < start else 'off_league_in_season'


def _double_counted(rows, team) -> int:
    """Rows kept twice because two sources name the same match differently (research v1 only)."""
    seen = Counter(_team_day(r, team) for r in rows)
    return sum(n - 1 for n in seen.values() if n > 1)


def _parity_summary(frame) -> dict:
    """Summary of a set of parity rows. A missing column reads as a typed all-zero Series."""
    def col(name, dtype=float):
        if name in frame:
            return frame[name]
        return pd.Series(None if dtype is object else 0, index=frame.index, dtype=dtype)

    def stats(name, rows):
        values = rows[name].dropna() if name in rows else pd.Series(dtype=float)
        return {'matches': int(len(values)), 'mean': float(values.mean()) if len(values) else None,
                'max': float(values.max()) if len(values) else None}

    def positive(name, rows=frame):
        values = rows[name] if name in rows else pd.Series(0, index=rows.index, dtype=float)
        return values.fillna(0) > 0

    compared = frame.loc[col('harness_compared', bool).fillna(False).astype(bool)]
    return {
        'forecasts': int(len(frame)),
        'research_versions': {str(k): int(v) for k, v in col('research_version', object).dropna().value_counts().items()},
        'same_inputs': {**stats('same_inputs_max_abs_diff', frame),
                        'identical_within_1e-12': bool((col('same_inputs_max_abs_diff') <= 1e-12).all())},
        'evidence_effect_1x2': {**stats('evidence_effect_1x2_max_abs', frame),
                                'matches_changed': int((col('evidence_effect_1x2_max_abs') > 1e-12).sum())},
        'evidence_rows_used': {k: int(col('evidence_rows_used_' + k).fillna(0).sum()) for k in EVIDENCE_CLASSES},
        'matches_with_double_counted_rows': int(positive('evidence_rows_used_double_counted').sum()),
        'matches_using_off_league_rows': int((positive('evidence_rows_used_off_league_in_season')
                                              | positive('evidence_rows_used_off_league_before_season')).sum()),
        'live_goal_rate_features': {str(k): int(v) for k, v in
                                    col('live_goal_rate_features', object).dropna().value_counts().items()},
        'live_bbs_applied': int(col('live_bbs_applied', bool).fillna(False).astype(bool).sum()),
        'harness_vs_live': {
            '1x2_max_abs': stats('harness_vs_live_1x2_max_abs', compared),
            'lambda_max_abs': stats('lambda_max_abs_diff', compared),
            'history_days_stale': stats('harness_history_days_stale', compared),
            'training_end': sorted(compared['harness_training_end'].dropna().unique().tolist())
            if 'harness_training_end' in compared else [],
            'matches_history_differs': int((positive('history_rows_only_live', compared)
                                            | positive('history_rows_only_harness', compared)).sum())},
    }


def research_parity(root, cache, cfg):
    """Release-gate parity for C, on every frozen live forecast that carries research.

    Compares probabilities only; no result is scored. Harness fits and the league
    lookup use only holdout-free history (training_rows), as in a locked run. So the
    harness has no results for the holdout leagues from 16 Jan - 10 Oct 2026, and their
    parity is reported separately (summary['by_group']['holdout_leagues']).

      same_inputs      the shared research step (team_research.prepare + research_grid),
                       fed the live row's own frozen inputs under the research version
                       it was frozen with, must reproduce the frozen live probabilities.
                       It does not show the harness inputs match live.
      evidence_effect  live minus live without pre-kickoff evidence: what the ESPN and
                       Understat rows add. The harness never has them.
      harness          C exactly as the historical harness computes it for that match
                       (fold refit on football-data, no BBS, history to the fold origin),
                       with its inputs compared field by field against the live row.
    """
    import copy
    import performance_tracking as pt
    from asian_handicap import margins as margin_json
    from football_value_pipeline_v2_standalone import DixonColesModel
    from team_research import LEGACY_VERSION, decode, form_history, name, prepare, research_inputs, utc
    latest = {}
    for meta, rows, _ in pt.snapshots(root):
        for row in rows:
            research = decode(row.get('team_research_json'))
            stamp = utc(research.get('observed_at_utc'))
            if not research.get('margin_distribution') or pd.isna(stamp):
                continue
            key = (str(row.get('league')), name(row.get('home_team')), name(row.get('away_team')), str(row.get('kickoff_utc')))
            if key not in latest or stamp > latest[key][0]:
                latest[key] = (stamp, row, research)
    profile = cfg['production_v2']
    load_cfg = {**cfg, 'test_end_exclusive': cfg['end_exclusive']}
    histories, models, matches, coverage = {}, {}, [], Counter()
    for key, (stamp, row, research) in sorted(latest.items()):
        inputs = research_inputs(row)
        evidence = copy.deepcopy(research.get('evidence', {}))
        for k in DERIVED_EVIDENCE:
            evidence.pop(k, None)
        live = research['margin_distribution']
        version = research.get('version', LEGACY_VERSION)
        same = prepare(row, stamp, copy.deepcopy(evidence), version=version)
        bare = prepare(row, stamp)
        league = LIVE_LEAGUES.get(key[0])
        group = ('no_football_data' if league is None else
                 'holdout_leagues' if league in cfg['holdout_leagues'] else 'other_domestic')
        record = {'league': key[0], 'league_group': group, 'home_team': row.get('home_team'),
                  'away_team': row.get('away_team'), 'kickoff_utc': key[3], 'research_observed_utc': stamp.isoformat(),
                  'research_version': version,
                  'same_inputs_max_abs_diff': _max_gap(live, same.get('margin_distribution') or {}),
                  'evidence_effect_1x2_max_abs': max(abs(a - b) for a, b in zip(_hda(live), _hda(bare['margin_distribution']))),
                  'live_lambda_home': float(row['lambda_home']), 'live_lambda_away': float(row['lambda_away']),
                  'live_goal_rate_features': row.get('goal_rate_features_used'),
                  'live_bbs_applied': str(row.get('bbs_statistics_applied')).lower() == 'true',
                  'harness_compared': False}
        if league is None:
            coverage['no_football_data_file:' + key[0]] += 1
            matches.append(record)
            continue
        if league not in histories:
            data, _, _ = hb.load_history(Path(cache), league, load_cfg)
            history = training_rows(data, league, cfg, False)
            histories[league] = (history, *league_index(history))
        history, league_results, season_starts = histories[league]

        def locked(date, league=league):
            return phase(date, league, cfg) == 'holdout'
        # Off-league games actually used in the live ten-match form.
        used = Counter()
        for side in ('home', 'away'):
            team = inputs[side + '_team']
            rows = _used_rows(inputs, evidence, stamp, side, version)
            used['double_counted'] += _double_counted(rows, team)
            for r in rows:
                if r.get('source') != TRAINING_HISTORY:
                    used[_classify(r, team, league_results, season_starts, locked)] += 1
        record.update({'evidence_rows_used_' + k: used[k] for k in EVIDENCE_CLASSES})
        kickoff = utc(row['kickoff_utc']).tz_convert(None).normalize()
        bounds = {b for w in fold_windows(cfg, kickoff + pd.Timedelta(days=1)) for b in w}
        origin = max(b for b in bounds if b <= kickoff)
        if (league, origin) not in models:
            train = history.loc[history.Date < origin]
            models[(league, origin)] = (train, DixonColesModel(
                half_life_days=profile['half_life_days'], l2=cfg['baseline_l2'], max_goals=cfg['max_goals'],
                shot_features=profile['shot_features'], bbs_statistics=False).fit(train.copy(), as_of=origin))
        train, model = models[(league, origin)]
        teams = (row.get('model_home_team'), row.get('model_away_team'))
        if not all(t in model.teams for t in teams):
            coverage['harness_team_unresolved'] += 1
            matches.append(record)
            continue
        fd_row = pd.Series({'HomeTeam': teams[0], 'AwayTeam': teams[1]})
        matrix, _, info = research_matrix(fd_row, train, origin, model)
        harness = json.loads(margin_json(matrix))
        live_history = decode(row.get('research_history_json'))
        fd_history = form_history(train, teams[0], teams[1], utc(origin))
        record.update(
            harness_compared=True, harness_origin=origin.date().isoformat(),
            harness_training_end=train.Date.max().date().isoformat(),
            harness_history_days_stale=int((stamp.tz_convert(None).normalize() - origin).days),
            harness_lambda_home=info['lambda_home'], harness_lambda_away=info['lambda_away'],
            lambda_max_abs_diff=max(abs(float(row['lambda_home']) - info['lambda_home']),
                                    abs(float(row['lambda_away']) - info['lambda_away'])),
            history_rows_only_live=sum(len({_result_key(r) for r in live_history.get(s, [])}
                                           - {_result_key(r) for r in fd_history[s]}) for s in ('home', 'away')),
            history_rows_only_harness=sum(len({_result_key(r) for r in fd_history[s]}
                                              - {_result_key(r) for r in live_history.get(s, [])}) for s in ('home', 'away')),
            harness_vs_live_1x2_max_abs=max(abs(a - b) for a, b in zip(_hda(live), _hda(harness))),
            live_p_home=_hda(live)[0], harness_p_home=_hda(harness)[0])
        coverage['harness_compared'] += 1
        matches.append(record)
    frame = pd.DataFrame(matches)
    groups = frame['league_group'] if 'league_group' in frame else pd.Series(index=frame.index, dtype=object)
    summary = {**_parity_summary(frame), 'coverage': dict(coverage),
               'holdout_leagues': list(cfg['holdout_leagues']),
               'by_group': {g: _parity_summary(frame.loc[groups.eq(g)]) for g in LEAGUE_GROUPS},
               'note': ('same_inputs shows the shared research step is identical given the same inputs. Harness '
                        'and live inputs do not match yet (ESPN form, goal rates): see the measured gap. Harness '
                        'fits for the holdout leagues exclude their 16 Jan - 10 Oct 2026 results.')}
    return summary, frame


# ---------------------------------------------------------------------------
# European results (UCL, UEL): results-only test matches
# ---------------------------------------------------------------------------
# No historical European prices are cached, so there is no market reference (M, D, A)
# and no market bar: candidates are scored against the result only. Periods, the
# European holdout and its ledger are in cfg['european'].

EUROPEAN_CANDIDATES = {
    'CE': 'European baseline: the research model team_form_poisson_v1 exactly as live runs it for UCL and UEL '
          "today: Dixon-Coles goal rates and ten-match form from the competition's own European results before "
          'the fold origin (uses no odds and no domestic results)',
    'CE2': "CE's home/away split rescaled by a slope fitted walk-forward on CE's own earlier European forecasts "
           '(european_candidates; per competition only when each competition has 1,000 earlier decided matches, '
           'otherwise pooled; neutral below 300)',
    'CE2p': 'Context: CE2 always pooled over UCL and UEL',
    'CE2c': 'Context: CE2 always fitted per competition',
    'CE3': "CE's goal rates blended (domestic weight 0.85) with domestic research strength (league Dixon-Coles and "
           'last-ten form, Understat xG where it exists) put on the European scale by league-strength factors fitted '
           'walk-forward on earlier European results; CE exactly where a team has no domestic form',
    'CE3n': 'Context: CE3 with goals-only domestic form (no xG)',
    'CE4': "CE3 followed by CE2's calibration, the slope refitted on CE3's own earlier forecasts",
}
# Everything that can change a European score: the European setup fingerprint hashes these files,
# the config and every cached European result file, so one frozen setup is evaluated once.
EUROPEAN_SETUP_FILES = ('evaluation_harness.py', 'european_results.py', 'research_backtest.py', 'team_research.py',
                        'score_probability.py', 'football_value_pipeline_v2_standalone.py', 'europa_training.py',
                        'ucl_training.py', 'match_scores.py', 'scripts/europa_research.py', 'ah_close_backtest.py',
                        'asian_handicap.py', 'evaluation_harness_config.json', 'docs/audits/europa-team-aliases.json',
                        'european_backfill.py', 'docs/audits/european-backfill-aliases.json',
                        'european_candidates.py', 'research_sharpen.py', 'understat_history.py',
                        'understat_team_aliases.json', 'historical_benchmark.py', 'shot_features.py',
                        'docs/audits/european-domestic-aliases.json', 'docs/audits/european-reviewed-aliases.json',
                        'benchmark_promotion_rules.json')


def european_phase(date, competition, cfg) -> str:
    e = cfg['european']
    date = pd.Timestamp(date)
    if date < pd.Timestamp(e.get('development_start', {}).get(competition, e['test_start'])):
        return 'warm_up'
    if date >= pd.Timestamp(e['holdout_start']):
        locked = competition in e['holdout_competitions'] and date < pd.Timestamp(e['holdout_end_exclusive'])
        return 'holdout' if locked else 'retrospective'
    return 'validation' if date >= pd.Timestamp(e['development_end']) else 'development'


def european_training_rows(data, competition, cfg, include_holdout):
    """Locked runs never train on European holdout results, so no diagnostic can carry them."""
    if include_holdout:
        return data
    locked = data.Date.map(lambda d: european_phase(d, competition, cfg) == 'holdout')
    return data.loc[~locked]


def european_ledger(cfg) -> Path:
    return Path(__file__).parent / cfg['european']['holdout_ledger']


def european_matrices(row, train, origin, model):
    """CE for one European match: the shared research step (team_research.prepare + research_grid) on the
    fold's Dixon-Coles goal rates and the competition's own history before the origin. Never odds. CE's goal
    rates go out in info['research_goal_rates'] for CE2-CE4."""
    from team_research import research_grid
    context, _, info = research_context(row, train, origin, model)
    matrix = rb.matrix_value(research_grid(context['goal_rates']))
    return {'CE': matrix}, {**info, 'research_goal_rates': [float(v) for v in context['goal_rates']]}


def evaluate_european(competition, cache, cfg, include_holdout=False, keep=None, data=None, fit_rows=False):
    """Walk-forward CE for one competition: 14-day folds, the live model settings (half-life, L2, max goals,
    shots; BBS off, as it is not applied live for UCL or UEL), refit on the competition's results before
    each origin. Locked runs skip every European holdout match and never train on one; a holdout run
    scores ONLY holdout matches, and only the candidates in `keep`. `data` replaces the cached results
    (tests only).

    Also returns, for CE2-CE4 (european_candidates): `research`, CE's goal rates for every forecast (scored, or,
    in a holdout run with `fit_rows`, unscored so the walk-forward fits can learn from earlier matches), and
    `factor_rows`, every result the league-strength factors may train on (warm-up included; never a locked
    holdout result)."""
    from football_value_pipeline_v2_standalone import DixonColesModel
    import european_results as er
    e = cfg['european']
    end = pd.Timestamp(e['end_exclusive'])
    if data is None:
        data = er.load_with_backfill(cache, competition, end)
    data = data.loc[data.Date < end].sort_values('Date', kind='stable').reset_index(drop=True)
    profile = cfg['production_v2']
    history = european_training_rows(data, competition, cfg, include_holdout)
    records, folds, coverage, calib, research, factor_rows = [], [], Counter(), [], [], []
    for origin, stop in fold_windows(e, end):
        train = history.loc[history.Date < origin]
        test = data.loc[(data.Date >= origin) & (data.Date < stop)]
        if test.empty:
            continue
        model = None
        for _, row in test.iterrows():
            name = european_phase(row.Date, competition, cfg)
            date = row.Date
            key = '|'.join((competition, date.date().isoformat(), row.HomeTeam, row.AwayTeam))
            if not (name == 'holdout' and not include_holdout):
                factor_rows.append({'fixture': key, 'competition': competition, 'date': date, 'origin': origin,
                                    'home': row.HomeTeam, 'away': row.AwayTeam,
                                    'home_goals': row.FTHG, 'away_goals': row.FTAG})
            if name == 'warm_up':
                coverage[competition + ':warm_up'] += 1  # training only, never scored
                continue
            if name == 'holdout' and not include_holdout:
                coverage[competition + ':locked_holdout'] += 1
                continue
            scored = True
            if include_holdout and name != 'holdout':
                coverage[competition + ':outside_holdout_run'] += 1
                if not fit_rows:
                    continue
                scored = False  # not scored in a holdout run; CE2-CE4's walk-forward fits learn from it
            if len(train) < e['min_train']:
                coverage[f'{competition}:{name}:insufficient_training'] += 1
                continue
            if model is None:
                if train.Date.max() >= origin:
                    raise ValueError('Training reaches prediction origin')
                model = DixonColesModel(half_life_days=profile['half_life_days'], l2=cfg['baseline_l2'],
                                        max_goals=cfg['max_goals'], shot_features=profile['shot_features'],
                                        bbs_statistics=False).fit(train.copy(), as_of=origin)
                folds.append({'competition': competition, 'origin': origin.date().isoformat(),
                              'end_exclusive': stop.date().isoformat(), 'training_end': train.Date.max().isoformat(),
                              'training_matches': len(train)})
            if row.HomeTeam not in model.teams or row.AwayTeam not in model.teams:
                # Live excludes a fixture with a team that has no earlier match (no league-average fallback).
                coverage[f'{competition}:{name}:team without earlier {competition} match'] += 1
                continue
            try:
                matrices, info = european_matrices(row, train, origin, model)
            except (RuntimeError, ValueError) as exc:
                # The fold's own Dixon-Coles grid is invalid (rho at its bound with very large goal rates):
                # no forecast can be made, live or here.
                coverage[f'{competition}:{name}:no forecast: {exc}'] += 1
                continue
            identity = {'league': competition, 'date': date.date().isoformat(),
                        'week': f'{date.isocalendar().year}-W{date.isocalendar().week:02d}',
                        'fixture_key': key, 'phase': name, 'stage_group': row.stage_group, 'market_book': ''}
            research.append({'identity': identity, 'competition': competition, 'date': date, 'origin': origin,
                             'fixture': key, 'goal_rates': info['research_goal_rates'],
                             'home_goals': row.FTHG, 'away_goals': row.FTAG, 'scored': scored})
            if not scored:
                continue
            if keep is not None:
                matrices = {k: v for k, v in matrices.items() if k in keep}
            records.extend(rb.score_fixture(identity, matrices, row.FTHG, row.FTAG))
            outcome = 0 if row.FTHG > row.FTAG else 1 if row.FTHG == row.FTAG else 2
            for cand, matrix in matrices.items():
                h, a = np.indices(matrix.shape)
                calib.append({'phase': name, 'league': competition, 'stage_group': row.stage_group,
                              'fixture_key': identity['fixture_key'], 'candidate': cand,
                              'probs': [float(matrix[h > a].sum()), float(matrix[h == a].sum()), float(matrix[h < a].sum())],
                              'outcome': outcome})
            for cand in matrices:
                coverage[f'{competition}:{name}:{cand}:scored'] += 1
    return records, folds, coverage, calib, (research, factor_rows)


def check_development_start(data, competition, cfg):
    """Each competition's development start is where its 250-match warm-up ends: the first fold origin with
    at least min_train earlier matches of that competition that has matches to score. Reads dates only."""
    e = cfg['european']
    dates = pd.Series(sorted(pd.to_datetime(data.Date)))
    for origin, stop in fold_windows(e, pd.Timestamp(e['end_exclusive'])):
        if int((dates < origin).sum()) >= e['min_train'] and bool(((dates >= origin) & (dates < stop)).any()):
            configured = pd.Timestamp(e['development_start'][competition])
            if origin != configured:
                raise ValueError(f'{competition} warm-up ends at {origin.date()}, config says {configured.date()}')
            return origin
    raise ValueError(f"{competition} never reaches {e['min_train']} training matches")


def european_holdout_reach(cache, cfg):
    """How many European holdout fixtures a declared run would score, by identity only (dates and team
    names; no score is read). A declared run trains on every result before the fold origin, holdout ones
    included, so a fixture is scored when its fold has at least min_train earlier matches and both teams have
    an earlier match in the competition before the origin. (A fold whose Dixon-Coles grid is invalid would
    still give no forecast; that needs the results, so it is not checked.)"""
    import european_results as er
    e = cfg['european']
    end = pd.Timestamp(e['end_exclusive'])
    out = {}
    for competition in e['holdout_competitions']:
        data = er.load_with_backfill(cache, competition, end)[['Date', 'HomeTeam', 'AwayTeam']]
        hold = data.loc[data.Date.map(lambda d, c=competition: european_phase(d, c, cfg) == 'holdout')]
        reasons, new_teams = Counter(), Counter()
        for origin, stop in fold_windows(e, end):
            test = hold.loc[(hold.Date >= origin) & (hold.Date < stop)]
            if test.empty:
                continue
            train = data.loc[data.Date < origin]
            teams = set(train.HomeTeam) | set(train.AwayTeam)
            for r in test.itertuples(index=False):
                if len(train) < e['min_train']:
                    reasons['insufficient training'] += 1
                elif r.HomeTeam not in teams or r.AwayTeam not in teams:
                    reasons['team without earlier match'] += 1
                    new_teams.update(t for t in (r.HomeTeam, r.AwayTeam) if t not in teams)
                else:
                    reasons['scored'] += 1
        out[competition] = {'fixtures': int(len(hold)), 'weeks': int(hold.Date.dt.strftime('%G-%V').nunique()),
                            'declared_run_would_score': int(reasons['scored']),
                            'left_out': {k: int(v) for k, v in reasons.items() if k != 'scored'},
                            'teams_without_earlier_match': dict(sorted(new_teams.items())),
                            'note': 'Identity only: dates and team names, no score read.'}
    return out


def european(cache, cfg, *, include_holdout=False, keep=None, competitions=None, data=None, strengths=None,
             extras=None):
    """Every European competition. A holdout run scores only the holdout competitions.

    CE2-CE4 (european_candidates) are built after CE from CE's walk-forward forecasts of both competitions; a
    holdout run that scores one of them still forecasts (unscored) every non-holdout match of every
    competition, so its fits learn from the same earlier matches. `strengths` (fixture key -> domestic
    strengths) replaces european_candidates.domestic_strengths (tests); with neither a cache nor `strengths`,
    no team has domestic form and CE3 = CE. `extras` (a dict) receives the strengths and the fits."""
    import european_candidates as ec
    e = cfg['european']
    needs = keep is None or bool(set(keep) & set(ec.CANDIDATE_NAMES))
    scored = list(competitions or (e['holdout_competitions'] if include_holdout else e['competitions']))
    run = list(e['competitions']) if include_holdout and needs and competitions is None else scored
    records, folds, coverage, calib, research, factor_rows = [], [], Counter(), [], [], []
    for competition in run:
        r, f, c, k, (x, y) = evaluate_european(competition, cache, cfg, include_holdout, keep,
                                               None if data is None else data[competition], fit_rows=needs)
        records += r; folds += f; coverage.update(c); calib += k; research += x; factor_rows += y
    if needs:
        r, k, c, fits, found = european_candidate_records(research, factor_rows, cache, cfg, keep, strengths)
        records += r; calib += k; coverage.update(c)
        folds.append({'candidate': 'CE2-CE4', 'walk_forward_fits': fits})
        if extras is not None:
            extras.update(strengths=found, fits=fits)
    if not include_holdout and any(r['phase'] == 'holdout' for r in records):
        raise ValueError('Locked European holdout rows leaked into an unlocked run')
    if include_holdout and any(r['phase'] != 'holdout' for r in records):
        raise ValueError('A European holdout run scored non-holdout matches')
    return records, folds, coverage, calib


def european_candidate_records(research, factor_rows, cache, cfg, keep, strengths=None):
    """Records and 1X2 rows of CE2-CE4 (european_candidates.build) for every scored CE forecast."""
    import european_candidates as ec
    e = cfg['european']
    if strengths is None:
        if cache is None or not any(r['scored'] for r in research):
            strengths = {}
        else:
            keys = {r['fixture']: r for r in factor_rows}
            keys.update({r['fixture']: r for r in research})
            fixtures = pd.DataFrame([{'competition': r['competition'], 'Date': r['date'], 'HomeTeam': r['fixture'].split('|')[2],
                                      'AwayTeam': r['fixture'].split('|')[3], 'origin': r['origin']} for r in keys.values()],
                                    index=list(keys))
            strengths = ec.domestic_strengths(cache, cfg, fixtures)
    out, fits = ec.build(research, factor_rows, strengths, fold_windows(e, pd.Timestamp(e['end_exclusive'])),
                         cfg['leagues'], keep)
    records, calib, coverage = [], [], Counter()
    for cand, rows in sorted(out.items()):
        for r, grid, extra in rows:
            identity = r['identity']
            try:
                matrix = rb.matrix_value(grid)
            except ValueError as exc:
                coverage[f"{identity['league']}:{cand}:{exc}"] += 1
                continue
            hg, ag = r['home_goals'], r['away_goals']
            records.extend(rb.score_fixture(identity, {cand: matrix}, hg, ag))
            h, a = np.indices(matrix.shape)
            calib.append({'phase': identity['phase'], 'league': identity['league'], 'stage_group': identity['stage_group'],
                          'fixture_key': identity['fixture_key'], 'candidate': cand,
                          'probs': [float(matrix[h > a].sum()), float(matrix[h == a].sum()), float(matrix[h < a].sum())],
                          'outcome': 0 if hg > ag else 1 if hg == ag else 2, 'domestic_used': bool(extra['domestic_used'])})
            coverage[f"{identity['league']}:{identity['phase']}:{cand}:scored"] += 1
            if extra['domestic_used']:
                coverage[f"{identity['league']}:{identity['phase']}:{cand}:domestic_used"] += 1
    return records, calib, coverage, fits, strengths


def week_mean(scores, samples=2000, seed=136):
    """Mean log loss per fixture with a 95% interval from resampling whole calendar weeks."""
    if scores.empty:
        return None
    weeks = scores.groupby('week').log_loss.agg(['sum', 'count'])
    interval = None
    if len(weeks) >= 2:
        draws = np.random.default_rng(seed).integers(0, len(weeks), size=(samples, len(weeks)))
        means = weeks['sum'].to_numpy()[draws].sum(1) / weeks['count'].to_numpy()[draws].sum(1)
        interval = [float(v) for v in np.quantile(means, [.025, .975])]
    return {'fixtures': int(scores.fixture_key.nunique()), 'weeks': int(len(weeks)),
            'mean_log_loss': float(scores.log_loss.mean()), 'interval_95': interval}


def european_setup_fingerprint(cfg, cache, root=Path(__file__).parent) -> dict:
    """Hash of everything that can change a European score: code, config and the cached European results."""
    import european_results as er
    import european_backfill as eb
    parts = {name: file_sha256(root / name) for name in EUROPEAN_SETUP_FILES}
    for path in er.ucl_files(cache):
        parts['data/' + path.name] = file_sha256(path)
    parts['data/europa/training.json'] = file_sha256(er.europa_snapshot(cache))
    for path in sorted(p for p in eb.folder(cache).rglob('*') if p.is_file()):
        parts['data/europa/backfill/' + path.relative_to(eb.folder(cache)).as_posix()] = file_sha256(path)
    for path in sorted((Path(cache) / cfg['european']['domestic_form']['backfill_folder']).glob('*')):
        parts['data/domestic_backfill/' + path.name] = file_sha256(path)
    digest = hashlib.sha256(json.dumps({'parts': parts, 'config': cfg}, sort_keys=True).encode()).hexdigest()
    return {'sha256': digest, 'parts': parts}


def european_domestic_form(cache, cfg, fixtures):
    """How many European fixtures have domestic league form for both teams in the 8 cached leagues
    (Phase 2c reach). Reads European identities and dates and domestic dates and names, never a score;
    the domestic histories are holdout-free (training_rows), as in every locked run."""
    import european_results as er
    load_cfg = {**cfg, 'test_end_exclusive': cfg['end_exclusive']}
    rule = cfg['european']['domestic_form']
    histories = {}
    for league in cfg['leagues']:
        data, _, _ = hb.load_history(Path(cache), league, load_cfg)
        # Older seasons (2015/16-2020/21) for European domestic-form coverage only: a separate folder that the
        # domestic harness never reads. They end before the domestic holdout, so training_rows keeps them all.
        old, _ = er.load_domestic_backfill(Path(cache) / rule['backfill_folder'], hb.CODES[league],
                                           rule['backfill_seasons'])
        if not old.empty and old.Date.max() >= data.Date.min():
            raise ValueError(f'{league} domestic backfill overlaps the cached seasons')
        data = pd.concat([old, data], ignore_index=True, sort=False)
        frame = training_rows(data, league, cfg, False)[['Date', 'HomeTeam', 'AwayTeam']]
        histories[league] = (frame, set(frame.HomeTeam) | set(frame.AwayTeam))
    import european_backfill as eb
    reviewed = eb.load_reviewed_aliases()
    flags, teams = er.domestic_form_coverage(fixtures, histories, rule['min_matches'], rule['days'],
                                             extra=eb.load_domestic_aliases(), reviewed=reviewed['domestic'],
                                             reviewed_before=reviewed['applies_before'])
    table = pd.concat([fixtures[['competition', 'phase', 'stage_group', 'Date', 'HomeTeam', 'AwayTeam']], flags], axis=1)
    summary = {}
    for (competition, name), part in table.groupby(['competition', 'phase']):
        summary.setdefault(name, {})[competition] = {
            'fixtures': int(len(part)), 'both_teams': int(part.both.sum()), 'one_team_or_more': int(part.one.sum()),
            'by_stage': {g: {'fixtures': int(len(p)), 'both_teams': int(p.both.sum())} for g, p in part.groupby('stage_group')}}
    return table, {'rule': rule, 'by_period': summary, 'teams': teams,
                   'note': ('Domestic form = at least min_matches league matches in the 8 football-data files within the '
                            'days before the fixture (earlier days only), team names resolved by the reviewed research '
                            'resolver (team_research.history_team; no fuzzy matching), over the cached seasons and the '
                            'older domestic files (2015/16-2020/21, European coverage only). Domestic holdout results (16 Jan - '
                            '10 Oct 2026, Eredivisie, Primeira Liga, Super Lig) are left out, so fixtures then involving '
                            'those clubs count as without form. European holdout fixtures are counted by identity only.')}


def european_summary(records, calib, coverage, cfg, metadata):
    scores = fixture_scores(records, cfg['draw_sensitive_lines'])
    stages = {r['fixture_key']: r['stage_group'] for r in records}
    scores['stage_group'] = scores.fixture_key.map(stages)
    rule = cfg['calibration_tolerance']
    periods = {}

    def table(frame):
        return {group: week_mean(frame.loc[frame.group == group]) for group in GROUPS}

    def block(part, rows):
        return {
            'overall': table(part),
            'by_competition': {c: table(p) for c, p in part.groupby('league')},
            'by_stage': {g: table(p) for g, p in part.groupby('stage_group')},
            'by_competition_and_stage': {f'{c} {g}': table(p) for (c, g), p in part.groupby(['league', 'stage_group'])},
            'calibration_tolerance_check': {
                'overall': calibration_check(rows, rule),
                **{c: calibration_check([r for r in rows if r['league'] == c], rule) for c in sorted({r['league'] for r in rows})}},
        }
    for name in sorted(scores.phase.unique()) if not scores.empty else []:
        part = scores.loc[scores.phase == name]
        rows = [r for r in calib if r['phase'] == name]
        # CE's block keeps its shape; each candidate also gets its own block (never mixed across candidates).
        periods[name] = {**block(part.loc[part.candidate == 'CE'], [r for r in rows if r['candidate'] == 'CE']),
                         'by_candidate': {c: block(part.loc[part.candidate == c], [r for r in rows if r['candidate'] == c])
                                          for c in sorted(part.candidate.unique())}}
    return {'version': VERSION, 'european_version': cfg['european']['version'], 'candidates': EUROPEAN_CANDIDATES,
            'config': cfg['european'], **metadata, 'coverage': dict(coverage), 'periods': periods,
            'calibration_1x2': calibration(calib),
            'notes': ['Results only: no historical European prices are cached, so there is no market reference (M), '
                      'no cagey tier (D), no published-grid proxy (A) and no market bar. Log loss is against the '
                      'result alone.',
                      'Calibration rule v2 is reported for information; it is not a gate for European matches.',
                      'CE is the research model as live runs it for UCL/UEL, without the ESPN form live adds (the '
                      'harness has none) and with history to the fold origin.',
                      'Intervals resample whole calendar weeks.',
                      'Retrospective results were already scored elsewhere: diagnostics only, never release evidence.']}


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def historical(cache, cfg, *, include_holdout=False, keep=None, leagues=None, workers=None):
    leagues = list(leagues or cfg['leagues'])
    records, folds, coverage, overrounds, sources, calib, research = [], [], Counter(), [], [], [], []
    with ProcessPoolExecutor(max_workers=workers) as pool:
        futures = [pool.submit(evaluate_league, league, str(cache), cfg, include_holdout, keep) for league in leagues]
        for future in futures:
            r, f, c, o, s, k, x = future.result()
            records += r; folds += f; coverage.update(c); overrounds += o; sources += s; calib += k; research += x
    r, k, c, fits = low_score_candidate(research, cfg, pd.Timestamp(cfg['end_exclusive']), keep)
    records += r; calib += k; coverage.update(c)
    folds.append({'candidate': 'C2', 'walk_forward_fits': fits})
    r, k, c, fits = sharpen_candidate(research, cfg, pd.Timestamp(cfg['end_exclusive']), keep)
    records += r; calib += k; coverage.update(c)
    folds.append({'candidate': 'C5', 'walk_forward_fits': fits})
    r, k, c, fits = low_score_sharpen_candidate(research, cfg, pd.Timestamp(cfg['end_exclusive']), keep)
    records += r; calib += k; coverage.update(c)
    folds.append({'candidate': 'C6', 'walk_forward_fits': fits})
    if not include_holdout and any(r['phase'] == 'holdout' for r in records):
        raise ValueError('Locked holdout rows leaked into an unlocked run')
    if include_holdout and any(r['phase'] != 'holdout' and r['candidate'] not in GAP_CANDIDATES for r in records):
        raise ValueError('A holdout run scored non-holdout candidates')
    return records, folds, coverage, overrounds, sources, calib


def european_main(args, cfg, commit):
    """--mode european: CE on the cached European results. Locked unless --declaration is given."""
    import european_results as er
    e = cfg['european']
    declaration = setup = keep = None
    ledger = european_ledger(cfg)
    for competition in e['competitions']:  # dates only: the configured development start is where the warm-up ends
        check_development_start(er.load_with_backfill(args.cache, competition, pd.Timestamp(e['end_exclusive']))[['Date']],
                                competition, cfg)
    if args.declaration:
        if args.leagues:
            raise ValueError('A European holdout run always covers every holdout competition')
        setup = european_setup_fingerprint(cfg, args.cache)
        declaration = validate_declaration(args.declaration, cfg, setup, ledger, EUROPEAN_CANDIDATES)
        keep = {declaration['candidate'], declaration['baseline']}
    extras = {}
    records, folds, coverage, calib = european(args.cache, cfg, include_holdout=declaration is not None, keep=keep,
                                               competitions=args.leagues, extras=extras)
    metadata = {'mode': 'european_holdout' if declaration else 'european', 'source_commit': commit, 'folds': folds,
                'config_sha256': hashlib.sha256(json.dumps(cfg, sort_keys=True).encode()).hexdigest()}
    summary = european_summary(records, calib, coverage, cfg, metadata)
    if declaration is not None:
        verdict = holdout_verdict(records, calib, declaration, {}, minimum=promotion_minimums('european'))
        summary.update(declaration=declaration, setup=setup, holdout_verdict=verdict)
        fixtures = len({r['fixture_key'] for r in records if r['phase'] == 'holdout'})
        record_holdout(declaration, setup, commit, fixtures, verdict, ledger)
    else:
        end = pd.Timestamp(e['end_exclusive'])
        summary['inventory'] = er.inventory(args.cache, end)
        summary['holdout_reach'] = european_holdout_reach(args.cache, cfg)
        summary['sample_minimum'] = promotion_minimums('european')
        frames = []
        for competition in args.leagues or e['competitions']:
            data = er.load_with_backfill(args.cache, competition, end)[['Date', 'HomeTeam', 'AwayTeam', 'stage_group']]
            frames.append(data.assign(competition=competition,
                                      phase=data.Date.map(lambda d, c=competition: european_phase(d, c, cfg))))
        fixtures = pd.concat(frames, ignore_index=True)
        form, summary['domestic_form'] = european_domestic_form(args.cache, cfg, fixtures)
        form.to_csv(args.output / 'domestic_form.csv', index=False)
        pd.DataFrame([{k: r[k] for k in ('phase', 'league', 'stage_group', 'fixture_key', 'candidate', 'outcome')}
                      | dict(zip(('p_home', 'p_draw', 'p_away'), r['probs'])) | {'domestic_used': r.get('domestic_used', False)}
                      for r in calib]).to_csv(args.output / 'forecasts_1x2.csv', index=False)
        strength_rows = []
        for key, sides in sorted((extras.get('strengths') or {}).items()):
            row = {'fixture_key': key}
            for side in ('home', 'away'):
                st = sides.get(side) or {}
                row.update({f'{side}_league': st.get('league'), f'{side}_domestic_matches': st.get('domestic_matches'),
                            f'{side}_att_goals': (st.get('goals') or (None, None))[0],
                            f'{side}_def_goals': (st.get('goals') or (None, None))[1],
                            f'{side}_att_xg': (st.get('xg') or (None, None))[0], f'{side}_def_xg': (st.get('xg') or (None, None))[1],
                            f'{side}_used_xg': st.get('used_xg')})
            strength_rows.append(row)
        pd.DataFrame(strength_rows).to_csv(args.output / 'domestic_strengths.csv', index=False)
    hb.write_json(args.output / 'results.json', summary)
    scores = fixture_scores(records, cfg['draw_sensitive_lines'])
    scores.to_csv(args.output / 'fixture_scores.csv', index=False)
    return 0


def git_commit():
    try:
        return subprocess.run(['git', 'rev-parse', 'HEAD'], capture_output=True, text=True, check=True).stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        return 'unknown'


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('--mode', choices=('historical', 'live', 'parity', 'european'), default='historical')
    parser.add_argument('--cache', type=Path, default=Path('.football_cache'))
    parser.add_argument('--root', type=Path, default=Path('football_output_v2'))
    parser.add_argument('--config', type=Path, default=CONFIG)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--leagues', nargs='+')
    parser.add_argument('--declaration', type=Path, help='Scores the locked holdout for one declared candidate, once')
    parser.add_argument('--workers', type=int)
    args = parser.parse_args(argv)
    args.output.mkdir(parents=True, exist_ok=True)
    commit = git_commit()
    if args.mode == 'live':
        records, coverage = live_replay(args.root)
        scores = match_scores(records)
        summary = {'version': VERSION, 'mode': 'live_replay', 'source_commit': commit, 'candidates': CANDIDATES,
                   'scope': {'bookmaker': 'Pinnacle', 'markets': ['native Asian handicap', *BINARY_MARKETS],
                             'offer_window_hours': OFFER_WINDOW.total_seconds() / 3600,
                             'sample_unit': 'verified match (its offers averaged before pairing and resampling)'},
                   'counts': offer_counts(records), 'coverage': dict(coverage),
                   'log_loss_common_cohort': common_cohort(scores) if not scores.empty else [],
                   'paired': {g: {f'{c}_vs_{b}': paired(scores.loc[scores.group == g], b, c)
                                  for b, c in (('C', 'M'), ('C', 'D'), ('C', 'A'), ('M', 'D'))} for g in LIVE_GROUPS},
                   'calibration_binary_offers': offer_calibration(records),
                   'note': 'Integration check on frozen live inputs; too few matches to be release evidence.'}
        hb.write_json(args.output / 'results.json', summary)
        scores.to_csv(args.output / 'match_scores.csv', index=False)
        pd.DataFrame(records).to_csv(args.output / 'offer_scores.csv', index=False)
        return 0
    cfg = json.loads(args.config.read_text(encoding='utf-8'))
    if args.mode == 'parity':
        summary, frame = research_parity(args.root, args.cache, cfg)
        hb.write_json(args.output / 'results.json', {'version': VERSION, 'mode': 'research_parity',
                                                     'source_commit': commit, **summary})
        frame.to_csv(args.output / 'parity_matches.csv', index=False)
        return 0
    if args.mode == 'european':
        return european_main(args, cfg, commit)
    declaration = setup = keep = None
    if args.declaration:
        if args.leagues:
            raise ValueError('A holdout run always covers every configured league')
        setup = setup_fingerprint(cfg, args.cache)
        declaration = validate_declaration(args.declaration, cfg, setup)
        keep = {declaration['candidate'], declaration['baseline'], 'M'}
    records, folds, coverage, overrounds, sources, calib = historical(
        args.cache, cfg, include_holdout=declaration is not None, keep=keep, leagues=args.leagues, workers=args.workers)
    metadata = {'mode': 'holdout' if declaration else 'historical', 'source_commit': commit, 'folds': folds,
                'inputs': sources, 'config_sha256': hashlib.sha256(json.dumps(cfg, sort_keys=True).encode()).hexdigest()}
    summary = summarize(records, overrounds, coverage, cfg, metadata)
    summary['calibration_1x2'] = calibration(calib)
    summary['calibration_tolerance_check'] = calibration_checks(calib, cfg['calibration_tolerance'])
    import understat_history as uh
    summary['calibration_1x2_understat_leagues'] = calibration([r for r in calib if r.get('league') in uh.LEAGUES])
    if declaration is not None:
        verdict = holdout_verdict(records, calib, declaration, summary['bet365_gap'])
        summary.update(declaration=declaration, setup=setup, holdout_verdict=verdict)
        fixtures = len({r['fixture_key'] for r in records if r['phase'] == 'holdout'})
        record_holdout(declaration, setup, commit, fixtures, verdict)
    hb.write_json(args.output / 'results.json', summary)
    fixture_scores(records, cfg['draw_sensitive_lines']).to_csv(args.output / 'fixture_scores.csv', index=False)
    if declaration is None:  # per-forecast 1X2 for calibration work; locked runs only
        pd.DataFrame([{k: r[k] for k in ('phase', 'league', 'fixture_key', 'candidate', 'outcome')}
                      | dict(zip(('p_home', 'p_draw', 'p_away'), r['probs'])) for r in calib
                      if 'fixture_key' in r]).to_csv(args.output / 'forecasts_1x2.csv', index=False)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
