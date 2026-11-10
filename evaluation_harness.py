"""Evaluation harness: one paired, time-ordered yardstick for every candidate in the plan.

Never selects, stakes or promotes a live pick. Builds on research_backtest.py.

Historical mode replays the football-data.co.uk files for the 8 domestic
leagues. The models are refit every 14 days on earlier matches only, and every
candidate is scored on the same matches:

  C  independent research model (team_form_poisson_v1, value shortlist; uses no odds)
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

Live-replay mode replays the frozen forecasts with the report's grading: each
forecast must precede the verified kickoff (performance_tracking.graded_match)
and each verified match is scored once. It scores C, M, D and A on the same
matches.
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
    'M': 'market reference: margin-free fit to the period bookmaker (Pinnacle, Bet365 on the holdout)',
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
               'evaluation_harness_config.json', 'narrow_margin_models/cagey-correction-through-2425-v1.json')
CALIBRATION_MIN_BIN = 30
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

def research_matrix(row, train, origin, model):
    """C: the independent research model. Reads team history only, never odds."""
    from score_probability import score_grid
    from team_research import form_history, prepare, utc
    matrix, info = model.score_matrix(row.HomeTeam, row.AwayTeam)
    frozen = {'home_team': row.HomeTeam, 'away_team': row.AwayTeam,
              'lambda_home': info['lambda_home'], 'lambda_away': info['lambda_away'],
              'research_history_json': json.dumps(form_history(train, row.HomeTeam, row.AwayTeam, utc(origin)))}
    context = prepare(frozen, utc(origin))
    research, _ = score_grid(*context['goal_rates'], 0.)
    return rb.matrix_value(research), matrix, info


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


def candidates(row, train, origin, model, cfg, cagey_model):
    if train.Date.max() >= origin:
        raise ValueError('Training reaches prediction origin')
    if row.HomeTeam not in model.teams or row.AwayTeam not in model.teams:
        return {}, {'all': 'unresolved training team'}, {}
    matrices, gaps, extra = {}, {}, {}
    research, model_grid, info = research_matrix(row, train, origin, model)
    matrices['C'] = research
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
    records, folds, coverage, overrounds, calib = [], [], Counter(), [], []
    for origin, stop in fold_windows(cfg, end):
        train = data.loc[data.Date < origin]
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
            matrices, gaps, extra = candidates(row, train, origin, model, cfg, cagey_model)
            if keep is not None:
                matrices = {k: v for k, v in matrices.items() if k in keep}
            date = row.Date
            identity = {'league': league, 'date': date.date().isoformat(),
                        'week': f'{date.isocalendar().year}-W{date.isocalendar().week:02d}',
                        'fixture_key': '|'.join((league, date.date().isoformat(), row.HomeTeam, row.AwayTeam)),
                        'phase': name, 'market_book': extra.get('market_book', '')}
            records.extend(rb.score_fixture(identity, matrices, row.FTHG, row.FTAG))
            outcome = 0 if row.FTHG > row.FTAG else 1 if row.FTHG == row.FTAG else 2
            for cand, matrix in matrices.items():
                h, a = np.indices(matrix.shape)
                probs = [float(matrix[h > a].sum()), float(matrix[h == a].sum()), float(matrix[h < a].sum())]
                calib.append({'phase': identity['phase'], 'candidate': cand, 'probs': probs, 'outcome': outcome})
            if 'overround' in extra:
                overrounds.append(extra['overround'])
            for key, reason in gaps.items():
                coverage[f'{league}:{key}:{reason}'] += 1
            for key in matrices:
                coverage[f'{league}:{key}:available'] += 1
    return records, folds, coverage, overrounds, sources, calib


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


def common_cohort(scores, names=('C', 'M', 'D', 'A')):
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
            for base, cand in (('C', 'M'), ('C', 'D'), ('C', 'A'), ('M', 'D')):
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
            'notes': ['Headline means use the common cohort: fixtures where C, M, D and A are all available.',
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
    digest = hashlib.sha256(json.dumps({'parts': parts, 'config': cfg}, sort_keys=True).encode()).hexdigest()
    return {'sha256': digest, 'parts': parts}


def validate_declaration(path, cfg, setup, ledger=LEDGER):
    """A declaration names one registered candidate and how it is judged. It must match the
    configured scoring, and neither the candidate nor the frozen setup may have been scored before."""
    data = json.loads(Path(path).read_text(encoding='utf-8'))
    missing = [k for k in DECLARATION_FIELDS if data.get(k) in (None, '', [])]
    if missing:
        raise ValueError('Declaration missing ' + ', '.join(missing))
    if data['candidate'] not in CANDIDATES or data['baseline'] not in CANDIDATES or data['candidate'] == data['baseline']:
        raise ValueError('Candidate and baseline must be two different candidates registered in the harness')
    if data['primary_metric'] not in GROUPS:
        raise ValueError('Primary metric must be one of ' + ', '.join(GROUPS))
    if sorted(round(float(v), 2) for v in data['draw_sensitive_lines']) != sorted(round(float(v), 2) for v in cfg['draw_sensitive_lines']):
        raise ValueError('Draw-sensitive lines differ from the configured scoring; change the config in a reviewed PR first')
    tolerance = float(data['calibration_tolerance'])
    if not 0 < tolerance <= .2:
        raise ValueError('Calibration tolerance must be between 0 and 0.2')
    entries = json.loads(ledger.read_text(encoding='utf-8')) if ledger.exists() else []
    if any(e['candidate'] == data['candidate'] for e in entries):
        raise ValueError(f"Holdout already scored for candidate {data['candidate']!r}")
    if any(e.get('setup_sha256') == setup['sha256'] for e in entries):
        raise ValueError('Holdout already scored for this frozen setup (same code, data and config)')
    digest = hashlib.sha256(json.dumps(data, sort_keys=True).encode()).hexdigest()
    return {**data, 'calibration_tolerance': tolerance, 'sha256': digest}


def holdout_verdict(records, calib, declaration, gap):
    """Apply the declaration: primary metric, draw-sensitive lines, calibration tolerance, market bar."""
    scores = fixture_scores(records, declaration['draw_sensitive_lines'])
    hold = scores.loc[scores.phase == 'holdout']
    cand, base = declaration['candidate'], declaration['baseline']
    primary = paired(hold.loc[hold.group == declaration['primary_metric']], base, cand)
    draw = paired(hold.loc[hold.group == 'AH draw-sensitive'], base, cand)
    deviations = [abs(b['observed_rate'] - b['mean_forecast']) for b in calibration(calib)
                  if b['phase'] == 'holdout' and b['candidate'] == cand and b['n'] >= CALIBRATION_MIN_BIN]
    worst = max(deviations) if deviations else None
    market = paired(hold.loc[hold.group == declaration['primary_metric']], 'M', cand) if cand != 'M' else None
    bar = max(0., gap.get(declaration['primary_metric'], {}).get('bet365_minus_pinnacle_log_loss', 0.))
    passed = bool(primary and primary['clear_of_zero'] and worst is not None and worst <= declaration['calibration_tolerance'])
    return {'candidate': cand, 'baseline': base, 'primary_metric': declaration['primary_metric'],
            'primary': primary, 'draw_sensitive': draw,
            'calibration_worst_bin_deviation': worst, 'calibration_tolerance': declaration['calibration_tolerance'],
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

def live_replay(root):
    """Frozen forecasts graded exactly as the performance report grades them, then scored once
    per verified match: C (frozen research), M (fit to frozen Pinnacle quotes), D (cagey), A (published grid)."""
    import narrow_margin as nm
    import performance_tracking as pt
    from price_edge_shortlist import pinnacle_quotes
    from team_research import utc
    cagey_model = nm.production_model()
    verified = pt.load_json(root / 'performance' / 'verified_results.json', {})
    results = [r for r in (verified.values() if isinstance(verified, dict) else verified)
               if isinstance(r, dict) and pt.verified_result_source(r)]
    coverage, latest = Counter(), {}
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
    records, calib = [], []
    for identity, (generated, row, final) in sorted(latest.items()):
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
        records.extend(rb.score_fixture(ident, matrices, final['home_goals'], final['away_goals']))
        outcome = 0 if final['home_goals'] > final['away_goals'] else 1 if final['home_goals'] == final['away_goals'] else 2
        for cand, matrix in matrices.items():
            h, a = np.indices(matrix.shape)
            calib.append({'phase': 'live_replay', 'candidate': cand, 'outcome': outcome,
                          'probs': [float(matrix[h > a].sum()), float(matrix[h == a].sum()), float(matrix[h < a].sum())]})
    coverage['verified_matches_graded'] = len(latest)
    return records, calib, coverage


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def historical(cache, cfg, *, include_holdout=False, keep=None, leagues=None, workers=None):
    leagues = list(leagues or cfg['leagues'])
    records, folds, coverage, overrounds, sources, calib = [], [], Counter(), [], [], []
    with ProcessPoolExecutor(max_workers=workers) as pool:
        futures = [pool.submit(evaluate_league, league, str(cache), cfg, include_holdout, keep) for league in leagues]
        for future in futures:
            r, f, c, o, s, k = future.result()
            records += r; folds += f; coverage.update(c); overrounds += o; sources += s; calib += k
    if not include_holdout and any(r['phase'] == 'holdout' for r in records):
        raise ValueError('Locked holdout rows leaked into an unlocked run')
    if include_holdout and any(r['phase'] != 'holdout' and r['candidate'] not in GAP_CANDIDATES for r in records):
        raise ValueError('A holdout run scored non-holdout candidates')
    return records, folds, coverage, overrounds, sources, calib


def git_commit():
    try:
        return subprocess.run(['git', 'rev-parse', 'HEAD'], capture_output=True, text=True, check=True).stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        return 'unknown'


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('--mode', choices=('historical', 'live'), default='historical')
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
        records, calib, coverage = live_replay(args.root)
        scores = fixture_scores(records)
        summary = {'version': VERSION, 'mode': 'live_replay', 'source_commit': commit, 'candidates': CANDIDATES,
                   'coverage': dict(coverage), 'log_loss_common_cohort': common_cohort(scores) if not scores.empty else [],
                   'paired': {g: {f'{c}_vs_{b}': paired(scores.loc[scores.group == g], b, c)
                                  for b, c in (('C', 'M'), ('C', 'D'), ('C', 'A'), ('M', 'D'))} for g in GROUPS},
                   'calibration_1x2': calibration(calib),
                   'note': 'Integration check on frozen live inputs; too few matches to be release evidence.'}
        hb.write_json(args.output / 'results.json', summary)
        scores.to_csv(args.output / 'fixture_scores.csv', index=False)
        return 0
    cfg = json.loads(args.config.read_text(encoding='utf-8'))
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
    if declaration is not None:
        verdict = holdout_verdict(records, calib, declaration, summary['bet365_gap'])
        summary.update(declaration=declaration, setup=setup, holdout_verdict=verdict)
        fixtures = len({r['fixture_key'] for r in records if r['phase'] == 'holdout'})
        record_holdout(declaration, setup, commit, fixtures, verdict)
    hb.write_json(args.output / 'results.json', summary)
    fixture_scores(records, cfg['draw_sensitive_lines']).to_csv(args.output / 'fixture_scores.csv', index=False)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
