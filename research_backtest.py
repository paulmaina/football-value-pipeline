"""Offline research-model diagnostics. Never select, stake or promote a live pick.

Historical CSV prices are untimestamped proxies, not proof of tradable returns.
Archive replay uses frozen inputs only; missing full grids never fall back to
raw rates or truncated scorelines. All candidate comparisons are paired.
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import hashlib
import json
from pathlib import Path

import numpy as np
import pandas as pd

import historical_benchmark as hb
from score_probability import valid_matrix, score_grid
from team_research import (C6_VERSIONS, V4_VERSION, VERSION as RESEARCH_VERSION, decode, form_history, prepare,
                           utc)
# Frozen research versions the live replay rebuilds: v4 on its independent grid, v5 on C6's grid under the
# fit frozen in the forecast. Older versions stay unavailable (gaps), as before v5.
REPLAYED_VERSIONS = (V4_VERSION, RESEARCH_VERSION)

VERSION = 'research-comparison-v1'
CANDIDATES = {'A': 'published-grid-v1', 'B': 'pinnacle-uncorrected-fit-B-v1',
              'C': 'team_form_poisson_v1'}
AH_LINES = tuple(i / 4 for i in range(-8, 9))
KINDS = ('p_win', 'p_half_win', 'p_push', 'p_half_loss', 'p_loss')


def matrix_value(value):
    matrix = valid_matrix(json.loads(value) if isinstance(value, str) else value)
    if matrix.shape[0] != matrix.shape[1] or abs(float(matrix.sum()) - 1) > 1e-8:
        raise ValueError('Full square normalized score grid required')
    return matrix


def archived_candidates(row, cutoff):
    """No internet and no refitting. Invalid/missing evidence stays unavailable."""
    from price_edge_shortlist import pinnacle_quotes, market_fit
    matrices, gaps = {}, {}
    try:
        matrices['A'] = matrix_value(row.get('score_matrix_json'))
    except (ValueError, TypeError):
        gaps['A'] = 'missing or invalid full published grid; no reconstruction'
    fit, _ = market_fit(pinnacle_quotes(row), utc(cutoff), cutoff=True)
    if fit.usable:
        matrices['B'] = matrix_value(fit.matrix)
    else:
        gaps['B'] = '; '.join(fit.reasons)
    evidence = decode(row.get('team_research_json'))
    stamp = utc(evidence.get('observed_at_utc'))
    try:
        if evidence.get('version') not in REPLAYED_VERSIONS:
            raise ValueError('unsupported frozen research version')
        if pd.isna(stamp) or stamp > utc(cutoff):
            raise ValueError('research not observed by cutoff')
        rates = evidence['goal_rates']
        if evidence['version'] in C6_VERSIONS:
            from research_low_score_sharpen import live_grid
            matrices['C'] = live_grid([float(rates[0]), float(rates[1])], evidence['c6_fit'])
        else:
            matrices['C'], _ = score_grid(float(rates[0]), float(rates[1]), 0.)
    except (ValueError, TypeError, KeyError, IndexError) as exc:
        gaps['C'] = 'frozen research unavailable: ' + str(exc)
    return matrices, gaps


def historical_candidates(row, train, origin, model, cfg):
    """A is a production CSV proxy, not an archived published forecast.

    Only nominal opening prices enter predictions. Closing prices, held-out
    results and same-fold results are never passed to the model/research step.
    BBS and live research cannot be reconstructed from these CSVs.
    """
    from football_value_pipeline_v2_standalone import reweight_matrix_to_1x2
    import market_implied as mi
    if train.Date.max() >= origin:
        raise ValueError('Training reaches prediction origin')
    if row.HomeTeam not in model.teams or row.AwayTeam not in model.teams:
        return {}, {'all': 'unresolved training team'}
    matrix, info = model.score_matrix(row.HomeTeam, row.AwayTeam)
    opening = hb.market_probabilities(row, ('PSH', 'PSD', 'PSA'), cfg['devig_method'])
    ou = hb.market_probabilities(row, ('P>2.5', 'P<2.5'), cfg['devig_method'])
    profile = cfg['model_upgrade_comparison']['production_v2']
    if opening is not None:
        p = model.one_x_two(matrix)
        target = (1-profile['market_weight'])*np.array([p[k] for k in ('home', 'draw', 'away')]) + profile['market_weight']*opening
        matrix = reweight_matrix_to_1x2(matrix, target)
    gaps = {}
    if profile['totals_anchor'] and ou is not None:
        p = model.one_x_two(matrix)
        try:
            matrix, _ = hb.anchor_totals(info['lambda_home'], info['lambda_away'], model.rho,
                [p[k] for k in ('home', 'draw', 'away')], float(ou[0]), cfg['max_goals'],
                tail_bounded=bool(info.get('score_engine_version')))
        except ValueError:
            gaps['A_anchor'] = 'solver failed; unanchored production proxy retained'
    frozen = {'home_team': row.HomeTeam, 'away_team': row.AwayTeam,
              'lambda_home': info['lambda_home'], 'lambda_away': info['lambda_away'],
              'research_history_json': json.dumps(form_history(train, row.HomeTeam, row.AwayTeam, utc(origin)))}
    context = prepare(frozen, utc(origin), version=V4_VERSION)  # C: research v4's independent grid
    research, _ = score_grid(*context['goal_rates'], 0.)
    matrices = {'A': matrix_value(matrix), 'C': research}
    # Proportional de-vig here matches market_implied, independently of A's
    # configured power de-vig. Never use PCAHH/PCAHA/AHCh or closing 1X2/totals.
    try:
        hda = tuple(float(row[k]) for k in ('PSH', 'PSD', 'PSA'))
        totals = tuple(float(row[k]) for k in ('P>2.5', 'P<2.5'))
        ah = tuple(float(row[k]) for k in ('AHh', 'PAHH', 'PAHA'))
        if opening is None or ou is None or not np.isfinite(ah).all() or min(ah[1:]) <= 1:
            raise ValueError('missing nominal opening inputs')
        if abs(ah[0]*4-round(ah[0]*4)) > 1e-8 or not .98 <= sum(1/p for p in ah[1:]) <= 1.2:
            raise ValueError('invalid opening AH pair')
        result = mi.fit(mi.targets_from_prices(hda, totals, ah), include_ah=True)
        if not result.usable:
            raise ValueError('; '.join(result.reasons))
        matrices['B'] = matrix_value(result.matrix)
    except (ValueError, TypeError, KeyError) as exc:
        gaps['B'] = str(exc)
    return matrices, gaps


def score_fixture(identity, matrices, home_goals, away_goals):
    """Five mutually exclusive AH settlements, with quarter-line support."""
    from ah_close_backtest import settle, outcome_probabilities
    if any(not np.isfinite(v) or v < 0 or int(v) != v for v in (home_goals, away_goals)):
        raise ValueError('Invalid regulation score')
    records = []
    for candidate, matrix in matrices.items():
        matrix = matrix_value(matrix)
        h, a = np.indices(matrix.shape)
        hda = [float(matrix[h > a].sum()), float(matrix[h == a].sum()), float(matrix[h < a].sum())]
        outcome = 0 if home_goals > away_goals else 1 if home_goals == away_goals else 2
        targets = [('1X2', hda, outcome)]
        over = float(matrix[h+a >= 2].sum())
        targets.append(('Over 1.5', [1-over, over], int(home_goals+away_goals >= 2)))
        for line in AH_LINES:
            masses = outcome_probabilities((h-a).ravel(), matrix.ravel(), line)
            won, lost = settle(home_goals-away_goals, line)
            index = {(1., 0.): 0, (.5, 0.): 1, (0., 0.): 2, (0., .5): 3, (0., 1.): 4}[(float(won), float(lost))]
            targets.append((f'AH {line:+.2f}', [masses[k] for k in KINDS], index))
        for market, probs, outcome in targets:
            probs = np.array(probs)
            records.append({**identity, 'candidate': candidate, 'market': market,
                'log_loss': float(-np.log(max(probs[outcome], 1e-15))),
                'brier': float(np.sum((probs-np.eye(len(probs))[outcome])**2))})
    return records


def profit_observations(identity, matrices, home_goals, away_goals, offers, cutoff, cost):
    """Reliability only at actual fresh frozen offers; never infer fair-price bets."""
    from ah_close_backtest import outcome_probabilities, settle
    from quote_freshness import quote_is_fresh
    if not np.isfinite(cost) or not 0 <= cost <= 1:
        raise ValueError('Invalid frozen cost')
    output = []
    for offer in offers:
        stamp = utc(offer.get('stamp'))
        price = float(offer['price'])
        if pd.isna(stamp) or stamp > cutoff or not quote_is_fresh(stamp, cutoff) or not np.isfinite(price) or price <= 1:
            continue
        returns = np.array([price-1, (price-1)/2, 0., -.5, -1.]) - cost
        for candidate, matrix in matrices.items():
            h, a = np.indices(matrix.shape)
            if offer['market'] == 'Over 1.5':
                over = float(matrix[h+a >= 2].sum())
                masses = np.array([over, 0, 0, 0, 1-over])
                actual_return = (price-1 if home_goals+away_goals >= 2 else -1) - cost
            else:
                side = 1 if offer['side'] == 'home' else -1
                p = outcome_probabilities((side*(h-a)).ravel(), matrix.ravel(), offer['line'])
                masses = np.array([p[k] for k in KINDS])
                won, lost = settle(side*(home_goals-away_goals), offer['line'])
                actual_return = float(won*(price-1)-lost-cost)
            probability = float(masses[returns > 1e-12].sum())
            actual = int(actual_return > 1e-12)
            output.append({**identity, 'candidate': candidate, 'market': offer['market'],
                'p_profit': probability, 'actual_profit': actual,
                'binary_brier': (probability-actual)**2,
                'binary_log_loss': float(-np.log(max(probability if actual else 1-probability, 1e-15)))})
    return output


def paired_summary(records, samples=1000, seed=126):
    """Pair the same market/fixture; resample whole calendar weeks, not bets."""
    if not records:
        return {}
    frame = pd.DataFrame(records)
    result = {}
    for market, group in frame.groupby('market', sort=True):
        table = group.pivot(index=['fixture_key', 'date'], columns='candidate', values='log_loss')
        output = {}
        for candidate in ('B', 'C'):
            if 'A' not in table or candidate not in table:
                continue
            pairs = table[['A', candidate]].dropna()
            if pairs.empty:
                continue
            gain = pairs['A']-pairs[candidate]
            weeks = pd.to_datetime(pairs.index.get_level_values('date'), utc=True).tz_localize(None).to_period('W').astype(str)
            groups = pd.DataFrame({'gain': gain.to_numpy(), 'week': weeks}).groupby('week').gain.agg(['sum', 'count'])
            interval = None
            if len(groups) >= 2:
                rng = np.random.default_rng(seed)
                draws = rng.integers(0, len(groups), size=(samples, len(groups)))
                gains = groups['sum'].to_numpy()[draws].sum(axis=1)/groups['count'].to_numpy()[draws].sum(axis=1)
                interval = [float(x) for x in np.quantile(gains, [.025, .975])]
            output[candidate] = {'paired_fixtures': len(pairs), 'calendar_weeks': len(groups),
                'baseline_minus_candidate_log_loss': float(gain.mean()), 'descriptive_95_interval': interval}
        result[market] = output
    return result


def summarize(records, observations, coverage, metadata, samples=1000):
    metrics = defaultdict(list)
    for record in records:
        for dimension, label in (('overall', 'all'), ('league', record['league']), ('phase', record['phase'])):
            metrics[(dimension, label, record['candidate'], record['market'])].append(record)
    aggregates = [{'dimension': k[0], 'cohort': k[1], 'candidate': k[2], 'market': k[3], 'n': len(rows),
                   'log_loss': float(np.mean([r['log_loss'] for r in rows])),
                   'brier': float(np.mean([r['brier'] for r in rows]))} for k, rows in sorted(metrics.items())]
    bins = defaultdict(list)
    for row in observations:
        bucket = min(9, int(row['p_profit']*10))
        bins[(row['league'], row['candidate'], row['market'], bucket)].append(row)
    reliability = [{'league': k[0], 'candidate': k[1], 'market': k[2], 'bin_lower': k[3]/10,
                    'n_offers': len(rows), 'distinct_fixtures': len({r['fixture_key'] for r in rows}),
                    'mean_forecast': float(np.mean([r['p_profit'] for r in rows])),
                    'observed_positive_return_rate': float(np.mean([r['actual_profit'] for r in rows])),
                    'binary_brier': float(np.mean([r['binary_brier'] for r in rows])),
                    'binary_log_loss': float(np.mean([r['binary_log_loss'] for r in rows]))}
                   for k, rows in sorted(bins.items())]
    return {'version': VERSION, 'candidates': CANDIDATES, **metadata, 'coverage': dict(coverage),
            'metrics': aggregates, 'profit_reliability': reliability,
            'paired_by_phase': {phase: paired_summary([r for r in records if r['phase'] == phase], samples)
                                for phase in sorted({r['phase'] for r in records})},
            'paired_by_league': {league: paired_summary([r for r in records if r['league'] == league], samples)
                                 for league in sorted({r['league'] for r in records})},
            'promotion_status': 'SHADOW_ONLY_NO_AUTOMATIC_PROMOTION',
            'roi': None, 'roi_reason': 'Probability diagnostics only; existing forward tracking grades the actual shortlist. No historical tradability claim.',
            'reliability_warning': 'Offer-weighted descriptive bins may contain correlated offers and different candidate coverage. They are not paired promotion evidence.',
            'interval_warning': 'Descriptive intervals are not adjusted for repeated candidate/market testing and cannot authorize promotion.'}


def historical(cache, cfg, source_commit, model_class=None):
    from football_value_pipeline_v2_standalone import DixonColesModel
    hb.validate_config(cfg)
    model_class = model_class or DixonColesModel
    records, folds, sources, coverage = [], [], [], Counter()
    profile = cfg['model_upgrade_comparison']['production_v2']
    for league in cfg['leagues']:
        data, inputs, _ = hb.load_history(cache, league, cfg)
        sources.extend(inputs)
        for origin, stop in hb.fold_windows(cfg):
            train = data.loc[data.Date < origin].copy()
            test = data.loc[(data.Date >= origin) & (data.Date < stop)]
            if test.empty:
                continue
            if len(train) < cfg['min_train']:
                coverage[league+':insufficient_training'] += len(test)
                continue
            model = model_class(half_life_days=profile['half_life_days'], l2=cfg['baseline_l2'],
                max_goals=cfg['max_goals'], shot_features=profile['shot_features'], bbs_statistics=False).fit(train, as_of=origin)
            folds.append({'league': league, 'origin': origin.isoformat(), 'end_exclusive': stop.isoformat(),
                'training_end': train.Date.max().isoformat(), 'training_matches': len(train),
                'training_sha256': hashlib.sha256(train.to_csv(index=False).encode()).hexdigest()})
            for _, row in test.iterrows():
                matrices, gaps = historical_candidates(row, train, origin, model, cfg)
                identity = {'league': league, 'date': row.Date.date().isoformat(),
                    'fixture_key': '|'.join((league, row.Date.isoformat(), row.HomeTeam, row.AwayTeam)),
                    'phase': 'development' if row.Date < pd.Timestamp(cfg['audit_start']) else 'audit'}
                records.extend(score_fixture(identity, matrices, row.FTHG, row.FTAG))
                for key, reason in gaps.items():
                    coverage[league+':'+key+':'+reason] += 1
                for key in matrices:
                    coverage[league+':'+key+':available'] += 1
    return records, [], coverage, {'source_commit': source_commit, 'config': cfg,
        'config_sha256': hashlib.sha256(json.dumps(cfg, sort_keys=True).encode()).hexdigest(),
        'inputs': sources, 'folds': folds, 'mode': 'historical_csv_proxy',
        'A_basis': 'production settings reconstructed from CSV; BBS/live research unavailable',
        'timing': 'nominal opening odds lack observation timestamps; retrospective diagnostics only'}


def archives(root, source_commit):
    """Use existing integrity-checked snapshots and verified cached results."""
    import performance_tracking as pt
    from price_edge_shortlist import offered_candidates, _json_list, _price
    records, observations, coverage = [], [], Counter()
    verified = pt.load_json(root/'performance'/'verified_results.json', {})
    results = list(verified.values()) if isinstance(verified, dict) else verified
    results = [r for r in results if isinstance(r, dict) and pt.verified_result_source(r)]
    # Predeclare latest eligible snapshot per fixture, independent of the result.
    latest, sources = {}, []
    for meta, rows, _ in pt.snapshots(root):
        cutoff = utc(meta['generated_at_utc'])
        captured = utc(meta['captured_at_utc'])
        sources.append({'archive': meta['git_commit_sha'], 'sha256': meta['sha256']})
        for row in rows:
            kickoff = utc(row.get('kickoff_utc'))
            if pd.isna(kickoff) or max(cutoff, captured) > kickoff-pd.Timedelta(minutes=20):
                coverage['not_pre_kickoff'] += 1
                continue
            key = pt.fixture_key(row)
            if key not in latest or cutoff > latest[key][0]:
                latest[key] = (cutoff, row, meta)
    for key, (cutoff, row, meta) in sorted(latest.items()):
        final, reason = pt.fixture_match(row, results)
        if final is None:
            coverage['ungraded:'+reason] += 1
            continue
        identity = {'fixture_key': key, 'league': row['league'], 'date': str(row['kickoff_utc'])[:10], 'phase': 'archive_replay'}
        matrices, gaps = archived_candidates(row, cutoff)
        records.extend(score_fixture(identity, matrices, final['home_goals'], final['away_goals']))
        for candidate, reason in gaps.items():
            coverage[candidate+':'+reason] += 1
        for candidate in matrices:
            coverage[candidate+':available'] += 1
        # Read the archived execution policy/cost, never today's account config.
        directory = root/'performance'/'snapshots'/meta['git_commit_sha'][:16]
        summary = pt.load_json(directory/'selection_summary.json', {})
        policy = summary.get('quote_execution_policy')
        if not isinstance(policy, dict):
            coverage['profit_reliability:missing_frozen_execution_policy'] += 1
            continue
        from quote_policy import validate_policy
        policy = validate_policy(policy)
        offers = offered_candidates(row, policy)
        for quote in _json_list(row.get('price_edge_quotes')):
            from quote_policy import usable_bookmaker
            if quote.get('market') == 'totals' and quote.get('point') == 1.5 and usable_bookmaker(quote.get('bookmaker'), policy):
                over = _price((quote.get('prices') or {}).get('over'))
                if over is not None:
                    offers.append({'market': 'Over 1.5', 'price': over, 'stamp': quote.get('last_update_utc')})
        observations.extend(profit_observations(identity, matrices, final['home_goals'], final['away_goals'],
            offers, cutoff, policy['per_stake_cost_bps']/10000))
    return records, observations, coverage, {'source_commit': source_commit, 'mode': 'frozen_archive_replay',
        'inputs': sources, 'config': {'snapshot_choice': 'latest eligible generated_at per fixture', 'minimum_lead_minutes': 20},
        'timing': 'Archive replay is retrospective until a candidate and comparison window are preregistered.'}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--mode', choices=('historical', 'archives'), required=True)
    parser.add_argument('--cache', type=Path, default=Path('.football_cache'))
    parser.add_argument('--root', type=Path, default=Path('football_output_v2'))
    parser.add_argument('--config', type=Path, default=Path('historical_benchmark_config.json'))
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--source-commit', required=True)
    args = parser.parse_args(argv)
    if args.mode == 'historical':
        cfg = json.loads(args.config.read_text(encoding='utf-8'))
        manifest = json.loads(args.config.with_name(cfg['input_manifest']).read_text(encoding='utf-8')) if cfg.get('input_manifest') else None
        if manifest is not None:
            hb.verify_inputs(args.cache, cfg, manifest)
        rows, observations, coverage, metadata = historical(args.cache, cfg, args.source_commit)
    else:
        rows, observations, coverage, metadata = archives(args.root, args.source_commit)
    metadata['config_sha256'] = hashlib.sha256(json.dumps(metadata['config'], sort_keys=True).encode()).hexdigest()
    hb.write_json(args.output/'results.json', summarize(rows, observations, coverage, metadata))
    pd.DataFrame(rows, columns=['fixture_key', 'league', 'date', 'phase', 'candidate', 'market', 'log_loss', 'brier']).to_csv(args.output/'scores.csv', index=False)
    pd.DataFrame(observations, columns=['fixture_key', 'league', 'date', 'phase', 'candidate', 'market', 'p_profit', 'actual_profit', 'binary_brier', 'binary_log_loss']).to_csv(args.output/'profit_observations.csv', index=False)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
