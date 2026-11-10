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

  development  Aug 2022 - Jun 2025, Pinnacle. Build and choose candidates here.
  validation   Jul 2025 - 15 Jan 2026, Pinnacle. Already inspected by earlier
               diagnostics; the cagey correction is out-of-sample from here.
  holdout      16 Jan 2026 - end, Bet365. Pinnacle prices in the files stop on
               15 Jan 2026. LOCKED: scored only with a declaration file, and every
               holdout run is appended to evaluation/holdout_ledger.json.

On matches priced by both bookmakers before the holdout, the harness measures
how far margin-free Bet365 sits from margin-free Pinnacle. On the holdout, a
candidate must beat M by more than that gap before it counts as beating the
market. Pinnacle's average margin is reported so expected-return work can
build synthetic Pinnacle-like prices from Bet365 probabilities.

Live-replay mode delegates to research_backtest.archives (frozen forecasts).
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

VERSION = 'evaluation-harness-v1'
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
GROUPS = ('1X2', 'Over 1.5', 'AH all', 'AH draw-sensitive')


# ---------------------------------------------------------------------------
# Periods and market inputs
# ---------------------------------------------------------------------------

def phase(date, cfg) -> str:
    date = pd.Timestamp(date)
    if date >= pd.Timestamp(cfg['holdout_start']):
        return 'holdout'
    return 'validation' if date >= pd.Timestamp(cfg['development_end']) else 'development'


def period_book(date, cfg) -> str:
    return 'bet365' if phase(date, cfg) == 'holdout' else 'pinnacle'


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
    if phase(row.Date, cfg) != 'holdout':
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
    fixed = [pd.Timestamp(cfg['development_end']), pd.Timestamp(cfg['holdout_start']), end]
    bounds = sorted({*pd.date_range(start, end, freq=f"{cfg['step_days']}D"), *[b for b in fixed if start < b <= end]})
    return list(zip(bounds, bounds[1:]))


def evaluate_league(league, cache, cfg, include_holdout):
    from football_value_pipeline_v2_standalone import DixonColesModel
    import narrow_margin as nm
    cagey_model = nm.production_model()
    load_cfg = {**cfg, 'test_end_exclusive': cfg['end_exclusive']}
    data, sources, _ = hb.load_history(Path(cache), league, load_cfg)
    end = pd.Timestamp(cfg['end_exclusive'] if include_holdout else cfg['holdout_start'])
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
            matrices, gaps, extra = candidates(row, train, origin, model, cfg, cagey_model)
            date = row.Date
            identity = {'league': league, 'date': date.date().isoformat(),
                        'week': f'{date.isocalendar().year}-W{date.isocalendar().week:02d}',
                        'fixture_key': '|'.join((league, date.date().isoformat(), row.HomeTeam, row.AwayTeam)),
                        'phase': phase(date, cfg), 'market_book': extra.get('market_book', '')}
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

def fixture_scores(records) -> pd.DataFrame:
    """One log loss per fixture, candidate and group; AH groups average their lines per fixture."""
    if not records:
        return pd.DataFrame(columns=['fixture_key', 'league', 'week', 'phase', 'candidate', 'group', 'log_loss'])
    frame = pd.DataFrame(records)
    frame['line'] = frame.market.str.extract(r'^AH ([+-]\d\.\d\d)$')[0].astype(float)
    parts = []
    for group, mask in (('1X2', frame.market == '1X2'), ('Over 1.5', frame.market == 'Over 1.5'),
                        ('AH all', frame.line.notna()), ('AH draw-sensitive', frame.line.abs() <= .5)):
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


def summarize(records, overrounds, coverage, cfg, metadata, declaration=None):
    scores = fixture_scores(records)
    means = (scores.groupby(['phase', 'group', 'candidate']).log_loss.agg(['mean', 'count']).reset_index()
             .to_dict('records') if not scores.empty else [])
    gap = {}
    pre = scores.loc[scores.phase != 'holdout']
    for group in GROUPS:
        result = paired(pre.loc[pre.group == group], 'MB', 'MP')
        if result:
            gap[group] = {**result, 'bet365_minus_pinnacle_log_loss': result['mean_gain']}
    margins = {b: float(np.mean([o[b] for o in overrounds])) for b in BOOKS} if overrounds else {}
    comparisons = {}
    for name in sorted(scores.phase.unique()) if not scores.empty else []:
        part = scores.loc[scores.phase == name]
        comparisons[name] = {}
        for group in GROUPS:
            sub = part.loc[part.group == group]
            entry = {}
            for cand in ('M', 'D', 'A'):
                result = paired(sub, 'C', cand)
                if result:
                    entry[f'{cand}_vs_C'] = result
            versus = paired(sub, 'M', 'C')
            if versus:
                bar = max(0., gap.get(group, {}).get('bet365_minus_pinnacle_log_loss', 0.)) if name == 'holdout' else 0.
                entry['C_vs_M'] = {**versus, 'gap_bar': bar, 'gain_after_gap_bar': versus['mean_gain'] - bar}
            comparisons[name][group] = entry
    return {'version': VERSION, 'candidates': CANDIDATES, 'config': cfg, **metadata,
            'coverage': dict(coverage), 'log_loss': means, 'paired': comparisons,
            'bet365_gap': gap, 'average_margin': margins,
            'synthetic_price_margin': margins.get('pinnacle'),
            'holdout_scored': declaration is not None, 'declaration': declaration,
            'notes': ['Positive mean_gain means the second-named candidate has the lower log loss.',
                      'Intervals resample whole calendar weeks across all leagues.',
                      'The cagey correction was trained on seasons through 2024/25; D is in-sample in development.',
                      'Historical prices are pre-match snapshots without timestamps; returns are not claimed.',
                      'No automatic promotion: every production change goes through a reviewed PR.']}


# ---------------------------------------------------------------------------
# Holdout lock
# ---------------------------------------------------------------------------

def validate_declaration(path, ledger=LEDGER):
    data = json.loads(Path(path).read_text(encoding='utf-8'))
    missing = [k for k in DECLARATION_FIELDS if data.get(k) in (None, '', [])]
    if missing:
        raise ValueError('Declaration missing ' + ', '.join(missing))
    if data['candidate'] in CANDIDATES or data['baseline'] not in (*CANDIDATES, 'current-production'):
        raise ValueError('Declare a new named candidate against an existing baseline')
    entries = json.loads(ledger.read_text(encoding='utf-8')) if ledger.exists() else []
    if any(e['candidate'] == data['candidate'] for e in entries):
        raise ValueError(f"Holdout already scored for {data['candidate']!r}; declare a new candidate name")
    digest = hashlib.sha256(json.dumps(data, sort_keys=True).encode()).hexdigest()
    return {**data, 'sha256': digest}


def record_holdout(declaration, commit, fixtures, ledger=LEDGER):
    entries = json.loads(ledger.read_text(encoding='utf-8')) if ledger.exists() else []
    entries.append({'candidate': declaration['candidate'], 'declaration_sha256': declaration['sha256'],
                    'source_commit': commit, 'holdout_fixtures': fixtures,
                    'scored_at_utc': datetime.now(timezone.utc).isoformat()})
    ledger.parent.mkdir(parents=True, exist_ok=True)
    ledger.write_text(json.dumps(entries, indent=2) + '\n', encoding='utf-8')


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def historical(cache, cfg, *, include_holdout=False, leagues=None, workers=None):
    leagues = list(leagues or cfg['leagues'])
    records, folds, coverage, overrounds, sources, calib = [], [], Counter(), [], [], []
    with ProcessPoolExecutor(max_workers=workers) as pool:
        futures = [pool.submit(evaluate_league, league, str(cache), cfg, include_holdout) for league in leagues]
        for future in futures:
            r, f, c, o, s, k = future.result()
            records += r; folds += f; coverage.update(c); overrounds += o; sources += s; calib += k
    if not include_holdout and any(r['phase'] == 'holdout' for r in records):
        raise ValueError('Locked holdout rows leaked into an unlocked run')
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
    parser.add_argument('--declaration', type=Path, help='Unlocks the holdout for one declared candidate')
    parser.add_argument('--workers', type=int)
    args = parser.parse_args(argv)
    args.output.mkdir(parents=True, exist_ok=True)
    commit = git_commit()
    if args.mode == 'live':
        rows, observations, coverage, metadata = rb.archives(args.root, commit)
        metadata['config_sha256'] = hashlib.sha256(json.dumps(metadata['config'], sort_keys=True).encode()).hexdigest()
        hb.write_json(args.output / 'results.json', rb.summarize(rows, observations, coverage, metadata))
        return 0
    cfg = json.loads(args.config.read_text(encoding='utf-8'))
    declaration = validate_declaration(args.declaration) if args.declaration else None
    records, folds, coverage, overrounds, sources, calib = historical(
        args.cache, cfg, include_holdout=declaration is not None, leagues=args.leagues, workers=args.workers)
    metadata = {'mode': 'historical', 'source_commit': commit, 'folds': folds, 'inputs': sources,
                'config_sha256': hashlib.sha256(json.dumps(cfg, sort_keys=True).encode()).hexdigest()}
    summary = summarize(records, overrounds, coverage, cfg, metadata, declaration)
    summary['calibration_1x2'] = calibration(calib)
    hb.write_json(args.output / 'results.json', summary)
    fixture_scores(records).to_csv(args.output / 'fixture_scores.csv', index=False)
    if declaration is not None:
        record_holdout(declaration, commit, int(sum(r['phase'] == 'holdout' for r in records if r['market'] == '1X2')))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
