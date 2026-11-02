"""Forward grading of the production model against the legacy model it replaced.

Both models' probabilities come from the same forecast row (``legacy_*`` columns
are computed in the same run, for the same fixtures and odds snapshot). Only
the first eligible pre-kickoff forecast per fixture counts; a later forecast
never fills in for an earlier one that lacks the legacy columns. No setting is
ever changed automatically.
"""
from collections import Counter
from datetime import timedelta
import json
import math

VERSION = 'production-vs-legacy-forward-v1'
MIN_PAIRED_MATCHES = 300
MIN_WEEKS = 6
BINARY = ('over_1_5', 'under_3_5', 'btts_yes', 'over_2_5')


def ah_probabilities(margins):
    """Home Asian handicap win probability per benchmark line from a margin distribution."""
    from asian_handicap import distribution
    from historical_benchmark import AH_LINES, ah_key
    dist = distribution(margins)
    out = {}
    for point in AH_LINES:
        win = sum(p for d, p in dist.items() if d+point > 0)
        loss = sum(p for d, p in dist.items() if d+point < 0)
        out[ah_key(point)] = win/(win+loss) if win+loss > 0 else None
    return out


def model_record(row, prefix):
    """Probabilities for one model, or None when the forecast is incomplete."""
    from performance_tracking import number
    record = {k: number(row.get(prefix+'p_'+k), min_value=0, max_value=1) for k in ('home', 'draw', 'away')}
    if any(v is None for v in record.values()) or abs(sum(record.values())-1) > 1e-6:
        return None
    record = {'p_'+k: v for k, v in record.items()}
    for market in BINARY:
        record[market] = number(row.get(prefix+'p_'+market), min_value=0, max_value=1)
    try:
        record.update(ah_probabilities(row.get(prefix+'goal_margin_distribution')))
    except (ValueError, TypeError):
        pass  # AH markets stay missing; other markets still grade.
    return record


def pinnacle_closing(observations, row):
    """Latest near-kickoff Pinnacle fair probabilities for this exact fixture."""
    from performance_tracking import fixture_key, utc
    from football_value_pipeline_v2_standalone import devig
    from asian_handicap import label
    from historical_benchmark import AH_LINES, ah_key
    candidates = [obs for obs in observations if fixture_key(obs['fixture']) == fixture_key(row)
                  and obs['fixture'].get('odds_event_id') == row.get('odds_event_id')
                  and utc(obs['fixture'].get('kickoff_utc')) == utc(row.get('kickoff_utc'))]
    if not candidates:
        return None
    quotes = {}
    for obs in sorted(candidates, key=lambda o: o['observed_at_utc']):
        quotes.update({q['selection']: q for q in obs['quotes'] if q['bookmaker'] == 'pinnacle'})
    close = {}
    if all(k in quotes and quotes[k]['fair_probability'] is not None for k in ('home', 'draw', 'away')):
        close.update({'p_'+k: quotes[k]['fair_probability'] for k in ('home', 'draw', 'away')})
    for market in BINARY:
        if market in quotes and quotes[market]['fair_probability'] is not None:
            close[market] = quotes[market]['fair_probability']
    for point in AH_LINES:
        home, away = quotes.get(label('home', point)), quotes.get(label('away', -point))
        if home and away:
            close[ah_key(point)] = float(devig([home['decimal_odds'], away['decimal_odds']], 'power')[0])
    return close or None


def distance(record, close, market):
    if close is None:
        return None
    if market == '1x2':
        if not all('p_'+k in close for k in ('home', 'draw', 'away')):
            return None
        return .5*sum(abs(record['p_'+k]-close['p_'+k]) for k in ('home', 'draw', 'away'))
    if record.get(market) is None or close.get(market) is None:
        return None
    return abs(record[market]-close[market])


def evaluate(root, archive, records, clock):
    from performance_tracking import frozen_rows, fixture_match, utc, verified_result_source
    from football_value_pipeline_v2_standalone import MODEL_VERSION, LEGACY_MODEL_VERSION
    from historical_benchmark import AH, score
    from closing_odds import load_observations
    observations, _ = load_observations(root, clock)
    records = [r for r in records if verified_result_source(r) and r.get('league_code') != 'EL']
    markets = ('1x2', *BINARY, *AH)
    excluded, paired = Counter(), []
    # frozen_rows keeps the FIRST eligible pre-kickoff forecast per fixture (no backfill).
    for row in frozen_rows(archive, 'predictions'):
        if row.get('legacy_model_version') != LEGACY_MODEL_VERSION:
            excluded['first_forecast_without_legacy_model'] += 1
            continue
        if row.get('model_version') != MODEL_VERSION:
            excluded['first_forecast_not_production_'+str(row.get('model_version') or 'unlabelled')] += 1
            continue
        if row.get('legacy_status') != 'AVAILABLE':
            excluded['legacy_'+str(row.get('legacy_status')).lower()] += 1
            continue
        production, legacy = model_record(row, ''), model_record(row, 'legacy_')
        if production is None or legacy is None:
            excluded['incomplete_probabilities'] += 1
            continue
        match, _ = fixture_match(row, records)
        if match is None or utc(row['kickoff_utc']) > clock-timedelta(hours=2):
            excluded['pending_or_unverified_result'] += 1
            continue
        h, a = match['home_goals'], match['away_goals']
        outcome = {'home_goals': h, 'away_goals': a, 'y': 0 if h > a else 1 if h == a else 2}
        year, week, _ = utc(row['kickoff_utc']).isocalendar()
        paired.append({'league': row['league'], 'fixture_key': row['fixture_key'], 'week': f'{year}-W{week:02d}',
                       'snapshot_commit': row['snapshot_commit'], 'source_match_id': match['match_id'],
                       'production': {**production, **outcome}, 'legacy': {**legacy, **outcome},
                       'pinnacle_close': pinnacle_closing(observations, row)})
    tables = []
    for league in ('ALL', *sorted({p['league'] for p in paired})):
        subset = [p for p in paired if league == 'ALL' or p['league'] == league]
        for market in markets:
            rows = [p for p in subset if score(p['production'], market) is not None and score(p['legacy'], market) is not None]
            entry = {'league': league, 'market': market, 'matches': len(rows)}
            for model in ('production', 'legacy'):
                scored = [score(p[model], market) for p in rows]
                gaps = [d for d in (distance(p[model], p['pinnacle_close'], market) for p in rows) if d is not None]
                entry[model] = {'log_loss': sum(s['log_loss'] for s in scored)/len(scored) if scored else None,
                                'brier': sum(s['brier'] for s in scored)/len(scored) if scored else None,
                                'mean_abs_distance_to_pinnacle_close': sum(gaps)/len(gaps) if gaps else None,
                                'pinnacle_close_matches': len(gaps)}
            tables.append(entry)
    weeks = len({p['week'] for p in paired})
    enough = len(paired) >= MIN_PAIRED_MATCHES and weeks >= MIN_WEEKS
    summary = {'version': VERSION, 'reviewed_at_utc': clock.isoformat(),
        'production_model_version': MODEL_VERSION, 'legacy_model_version': LEGACY_MODEL_VERSION,
        'status': 'READY_FOR_REVIEW' if enough else 'COLLECT_MORE_DATA',
        'paired_matches': len(paired), 'weeks': weeks,
        'gates': {'minimum_paired_matches': MIN_PAIRED_MATCHES, 'minimum_weeks': MIN_WEEKS},
        'excluded_fixtures': dict(sorted(excluded.items())), 'markets': list(markets), 'tables': tables,
        'automatic_production_change': False,
        'note': ('First eligible pre-kickoff forecast per fixture only, with no backfill. Both models come from '
                 'the same run and odds snapshot. 1X2 distance to the Pinnacle close is total variation; binary '
                 'markets use absolute difference. Asian handicap is the home side and integer lines exclude '
                 'refunds. Legacy probabilities are never used for selection or staking.')}
    return summary, paired


def fmt(value):
    return 'n.a.' if value is None or (isinstance(value, float) and math.isnan(value)) else f'{value:.4f}'


def review(root, archive, records, clock):
    from performance_tracking import write_json
    summary, paired = evaluate(root, archive, records, clock)
    dest = root/'performance'/'model_comparison'
    write_json(dest/'summary.json', summary)
    write_json(dest/'paired.json', paired)
    lines = ['# Production vs legacy model', '', summary['note'], '',
             f"Production `{summary['production_model_version']}` vs legacy `{summary['legacy_model_version']}`.",
             f"Status: **{summary['status']}** (paired matches {summary['paired_matches']}/{MIN_PAIRED_MATCHES}, "
             f"weeks {summary['weeks']}/{MIN_WEEKS}). No automatic production change.", '',
             'Excluded fixtures: ' + (', '.join(f'{k}: {v}' for k, v in summary['excluded_fixtures'].items()) or 'none'), '',
             '| League | Market | Matches | Prod log loss | Legacy log loss | Prod Brier | Legacy Brier | Prod dist. to Pinnacle close | Legacy dist. to Pinnacle close | Close N |',
             '|---|---|---:|---:|---:|---:|---:|---:|---:|---:|']
    for t in summary['tables']:
        p, l = t['production'], t['legacy']
        lines.append(f"| {t['league']} | {t['market']} | {t['matches']} | {fmt(p['log_loss'])} | {fmt(l['log_loss'])} | "
                     f"{fmt(p['brier'])} | {fmt(l['brier'])} | {fmt(p['mean_abs_distance_to_pinnacle_close'])} | "
                     f"{fmt(l['mean_abs_distance_to_pinnacle_close'])} | {p['pinnacle_close_matches']} |")
    (dest/'report.md').write_text('\n'.join(lines)+'\n', encoding='utf-8')
    return summary


def validate_report(root):
    from performance_tracking import load_json, snapshots, utc
    dest = root/'performance'/'model_comparison'
    actual = load_json(dest/'summary.json', {})
    expected, paired = evaluate(root, snapshots(root), list(load_json(root/'performance/verified_results.json', {}).values()),
                                utc(actual['reviewed_at_utc']))
    if json.loads(json.dumps(expected)) != actual or load_json(dest/'paired.json', []) != json.loads(json.dumps(paired)):
        raise ValueError('Model comparison report differs from frozen forecasts/results')
    return True
