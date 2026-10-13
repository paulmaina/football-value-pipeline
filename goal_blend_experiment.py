"""Optional, uncalibrated shadow probabilities. Never makes betting selections."""
from __future__ import annotations

import hashlib
import json
from datetime import timedelta
from pathlib import Path

VERSION = 'goal-blend-shadow-v1'
MARKETS = {'over_1_5': 'Over 1.5', 'under_3_5': 'Under 3.5',
           'btts_yes': 'Both Teams to Score - Yes'}
WEIGHTS = {'raw': 0.0, 'book25': .25, 'book50': .5, 'bookmaker': 1.0}


def generate(predictions, generated_at):
    """Read-only transformation; complete exact-market pairs or explicit gaps."""
    from performance_tracking import utc, number
    clock = utc(generated_at)
    if clock is None:
        raise ValueError('Invalid experiment generation time')
    output = []
    for source in predictions.astype(object).where(predictions.notna(), None).to_dict('records'):
        fixture = []
        for key in MARKETS:
            r = {k: source.get(k) for k in ('league', 'home_team', 'away_team', 'kickoff_utc')}
            r.update(version=VERSION, market=key, generated_at_utc=clock.isoformat())
            p = number(source.get('raw_p_' + key), min_value=0, max_value=1)
            base = number(source.get('p_' + key), min_value=0, max_value=1)
            a = number(source.get('market_reference_' + key + '_odds'), min_value=1.000001)
            b = number(source.get('market_reference_' + key + '_opposite_odds'), min_value=1.000001)
            q = number(source.get('market_p_' + key), min_value=0, max_value=1)
            stamp = source.get('market_best_' + key + '_last_update_utc')
            updated = utc(stamp)
            price = number(source.get('market_' + key + '_odds'), min_value=1.000001)
            books = number(source.get('market_' + key + '_bookmakers'), min_value=1)
            kick = utc(source.get('kickoff_utc'))
            reasons = []
            if p is None or base is None: reasons.append('missing_model_probability')
            if a is None or b is None or q is None or not .98 <= 1/a + 1/b <= 1.20:
                reasons.append('invalid_exact_market_reference')
            if price is None or books is None or not source.get('best_' + key + '_bookmaker'):
                reasons.append('missing_quote_or_coverage')
            if updated is None or not -300 <= (clock-updated).total_seconds() <= 86400:
                reasons.append('stale_or_missing_quote')
            if kick is None or clock >= kick-timedelta(minutes=20):
                reasons.append('insufficient_lead_time')
            r.update(status='unavailable' if reasons else 'available', reasons=reasons,
                     raw_probability=p, baseline_probability=base, bookmaker_probability=q,
                     reference_odds=a, reference_opposite_odds=b, decimal_odds=price,
                     bookmaker=source.get('best_' + key + '_bookmaker'),
                     quote_updated_at_utc=str(stamp), bookmaker_count=books,
                     variants={})
            if not reasons:
                r['variants'] = {name: (1-w)*p+w*q for name,w in WEIGHTS.items()}
                r['variants']['baseline'] = base
            fixture.append(r)
        # P(total<=3) + P(total>=2) >= 1. Never silently repair inconsistent markets.
        o,u = fixture[:2]
        if o['variants'] and u['variants'] and any(
            o['variants'][v]+u['variants'][v] < 1-1e-9 for v in o['variants']
        ):
            for r in (o,u):
                r.update(status='unavailable', variants={})
                r['reasons'].append('inconsistent_goal_lines')
        for r in fixture:
            r['opposite_variants'] = {v:1-p for v,p in r['variants'].items()}
        output.extend(fixture)
    return output


def write_experiment(predictions, raw: Path, generated_at):
    path = raw / 'goal_blend_experiment.json'
    payload = {'version': VERSION, 'generated_at_utc': generated_at,
               'predictions_sha256': hashlib.sha256((raw/'all_leagues_predictions.csv').read_bytes()).hexdigest(),
               'calibrated': False, 'selection_policy': 'none; research only',
               'rows': generate(predictions, generated_at)}
    path.write_text(json.dumps(payload, indent=2, allow_nan=False, default=str)+'\n', encoding='utf-8')


def capture_file(raw: Path, baseline_generated):
    """Reject stale experiments from previous runs; baseline capture stays independent."""
    from performance_tracking import load_json
    path = raw/'goal_blend_experiment.json'
    if not path.exists(): return None
    data = load_json(path,{})
    from forecast_integrity import forecast_digest_variants
    digests = forecast_digest_variants(raw/'all_leagues_predictions.csv')
    if (data.get('version') == VERSION and data.get('generated_at_utc') == baseline_generated
            and data.get('predictions_sha256') in digests):
        return path
    return None


def review_experiment(root, archived, records, clock):
    """Score first eligible experiment per fixture/market, using shared verified results."""
    from performance_tracking import (load_json, utc, fixture_key, fixture_match,
                                      result_for_market, write_json, write_csv)
    frozen = {}
    for meta, _, _ in archived:
        directory = root/'performance'/'snapshots'/meta['git_commit_sha'][:16]
        if 'goal_blend_experiment.json' not in meta.get('sha256',{}): continue
        sidecar = directory/'goal_blend_experiment.json'
        if not sidecar.exists() or hashlib.sha256(sidecar.read_bytes()).hexdigest() != meta['sha256']['goal_blend_experiment.json']:
            continue
        data = load_json(sidecar, {})
        if data.get('version') != VERSION: continue
        generated, captured = utc(data.get('generated_at_utc')), utc(meta['captured_at_utc'])
        for row in data.get('rows',[]):
            kickoff = utc(row.get('kickoff_utc'))
            if not generated or not captured or not kickoff or max(generated,captured) >= kickoff-timedelta(minutes=20):
                continue
            key = (fixture_key(row), row['market'])
            frozen.setdefault(key, {**row, 'snapshot_commit':meta['git_commit_sha']})
    if not frozen: return
    scored, groups = [], {}
    for row in frozen.values():
        match, state = fixture_match(row, records)
        if utc(row['kickoff_utc']) > clock-timedelta(hours=2): match=None
        if row['status'] != 'available' or match is None: continue
        outcome = int(result_for_market(MARKETS[row['market']], match['home_goals'], match['away_goals']))
        for variant, p in row['variants'].items():
            record = {k: row[k] for k in ('league','home_team','away_team','kickoff_utc','market','snapshot_commit')}
            record.update(variant=variant, probability=p, outcome=outcome, brier=(p-outcome)**2)
            scored.append(record)
            groups.setdefault((row['market'],variant),[]).append(record)
    summary=[]
    for (market,variant), rows in sorted(groups.items()):
        n=len(rows)
        summary.append({'market':market,'variant':variant,'n':n,
                        'brier':sum(x['brier'] for x in rows)/n,
                        'mean_probability':sum(x['probability'] for x in rows)/n,
                        'event_rate':sum(x['outcome'] for x in rows)/n})
    dest=root/'performance'/'goal_blend_experiment'
    write_json(dest/'summary.json', {'version':VERSION,'reviewed_at_utc':clock.isoformat(),
        'total_fixture_markets':len(frozen),
        'available_fixture_markets':sum(r['status']=='available' for r in frozen.values()),
        'graded_fixture_markets':len(scored)//5,'comparisons':summary,
        'note':'Uncalibrated fixed variants; paired samples; no betting policy, ROI or promotion.'})
    write_csv(dest/'graded.csv',scored,['league','home_team','away_team','kickoff_utc','market',
              'snapshot_commit','variant','probability','outcome','brier'])
    lines=['# Goal-market shadow comparison','',
           'Fixed, uncalibrated variants on identical verified fixtures. No model promotion or bet selections.',
           '',f'Coverage: {sum(r["status"]=="available" for r in frozen.values())}/{len(frozen)} fixture-markets available.',
           '', '| Market | Variant | N | Brier | Mean probability | Event rate |',
           '|---|---|---:|---:|---:|---:|']
    for r in summary:
        lines.append(f"| {r['market']} | {r['variant']} | {r['n']} | {r['brier']:.4f} | {r['mean_probability']:.1%} | {r['event_rate']:.1%} |")
    (dest/'report.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
