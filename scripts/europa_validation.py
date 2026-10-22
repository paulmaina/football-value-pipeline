"""Frozen Europa research protocol; final-season labels never tune settings."""
from collections import Counter
import json
import math
from pathlib import Path

import numpy as np
import pandas as pd


PROTOCOL = {'half_life_days': 240, 'l2': .08, 'refit_days': 28,
            'minimum_team_appearances': 6, 'development_season': 2024,
            'audit_season': 2025, 'minimum_high_development': 30,
            'minimum_high_audit': 12, 'high_probability': .75,
            'maximum_audit_overconfidence': .10, 'maximum_brier_excess': .005,
            'market_blend': 0., 'statistics_features': False}


def team_counts(frame):
    return Counter(list(frame.HomeTeam) + list(frame.AwayTeam))


def metrics(rows):
    if not rows:
        return {'n': 0}
    p, y, baseline = np.asarray([(x['p'], x['y'], x['baseline']) for x in rows]).T
    clipped = np.clip(p, 1e-12, 1-1e-12)
    observed = float(y.mean())
    z, n = 1.96, len(rows)
    denominator = 1 + z*z/n
    center = (observed + z*z/(2*n))/denominator
    half = z*math.sqrt(observed*(1-observed)/n + z*z/(4*n*n))/denominator
    return {'n': len(rows), 'mean_probability': float(p.mean()), 'observed_frequency': float(y.mean()),
            'observed_frequency_wilson_95': [max(0., center-half), min(1., center+half)],
            'overconfidence': float((p-y).mean()), 'brier': float(((p-y)**2).mean()),
            'baseline_brier': float(((baseline-y)**2).mean()),
            'binary_log_loss': float(-(y*np.log(clipped)+(1-y)*np.log(1-clipped)).mean())}


def summarize_market(dev, audit):
    # Correction determined on development predictions only. Audit remains a
    # predeclared diagnostic gate; it cannot select a new penalty or settings.
    residuals = np.asarray([x['p']-x['y'] for x in dev])
    penalty = (max(0., float(residuals.mean()+1.96*residuals.std(ddof=1)/math.sqrt(len(dev))))
               if len(dev) > 1 else 1.)
    penalty = min(1., penalty)
    high_dev = [x for x in dev if max(0., x['p']-penalty) >= .75]
    high_audit = [x for x in audit if max(0., x['p']-penalty) >= .75]
    dm, am, hd, ha = metrics(dev), metrics(audit), metrics(high_dev), metrics(high_audit)
    enough = hd['n'] >= 30 and ha['n'] >= 12
    passed = (enough and am['brier'] <= am['baseline_brier'] + .005 and
              ha['overconfidence'] - penalty <= .10)
    return {'development': dm, 'audit': am, 'development_penalty': penalty,
            'high_adjusted_development': hd, 'high_adjusted_audit': ha,
            'diagnostic_status': ('PASS_RESEARCH_DIAGNOSTIC' if passed else
                                  'INSUFFICIENT_HIGH_CONFIDENCE_SAMPLE' if not enough else 'FAIL_AUDIT'),
            'production_eligible': False,
            'reason': 'Retrospective probabilities only; execution EV, live reliability and forward evidence unverified'}


def observations(matrix, goals, training):
    from asian_handicap import margins, probabilities, settlement
    from football_value_pipeline_v2_standalone import DixonColesModel
    p = DixonColesModel.one_x_two(matrix)
    h, a = goals
    base_h = float((training.FTHG > training.FTAG).mean())
    base_d = float((training.FTHG == training.FTAG).mean())
    base_a = float((training.FTHG < training.FTAG).mean())
    ii, jj = np.indices(matrix.shape)
    result = {
        'Home win': (p['home'], int(h > a), base_h),
        'Away win': (p['away'], int(h < a), base_a),
        'Double Chance 1X': (p['home']+p['draw'], int(h >= a), base_h+base_d),
        'Double Chance X2': (p['away']+p['draw'], int(h <= a), base_a+base_d),
        'Double Chance 12': (p['home']+p['away'], int(h != a), base_h+base_a),
        'Over 1.5': (float(matrix[ii+jj >= 2].sum()), int(h+a >= 2), float((training.FTHG+training.FTAG >= 2).mean()))}
    dist = margins(matrix)
    base_margins = (training.FTHG-training.FTAG).to_numpy()
    for side, sign in [('home', 1), ('away', -1)]:
        for quarter in range(-12, 13):
            point = quarter / 4
            # Price 2 is only required by the existing settlement API; no EV
            # or return is used. Zero-loss events are price-independent here.
            no_loss = probabilities(dist, side, point, 2.)['p_no_loss']
            actual = int(settlement((h-a)*sign, point)[1] == 0)
            baseline = float(np.mean([settlement(int(d)*sign, point)[1] == 0 for d in base_margins]))
            result[f'AH {side} {point:+g}'] = (no_loss, actual, baseline)
    return result


def validate(history, current, output_dir):
    from football_value_pipeline_v2_standalone import DixonColesModel
    frame = pd.DataFrame([{'Date': pd.Timestamp(x['date']), 'HomeTeam': x['home'],
                           'AwayTeam': x['away'], 'FTHG': x['regulation'][0],
                           'FTAG': x['regulation'][1], 'season': x['season']} for x in history])
    frame = frame.sort_values(['Date', 'HomeTeam', 'AwayTeam']).reset_index(drop=True)
    start, end = pd.Timestamp('2024-07-01'), pd.Timestamp('2026-07-01')
    records, windows, excluded = [], [], Counter()
    for origin in pd.date_range(start, end, freq='28D', inclusive='left'):
        train = frame[frame.Date < origin]
        test = frame[(frame.Date >= origin) & (frame.Date < min(end, origin+pd.Timedelta(days=28)))]
        if test.empty:
            continue
        if len(train) < 30:
            raise ValueError('Not enough training history at origin')
        counts = team_counts(train)
        eligible = test.apply(lambda x: min(counts[x.HomeTeam], counts[x.AwayTeam]) >= 6, axis=1)
        excluded[str(int(test.iloc[0].season))] += int((~eligible).sum())
        if not eligible.any():
            continue
        model = DixonColesModel(half_life_days=240, l2=.08, bbs_statistics=False).fit(train, as_of=origin)
        windows.append({'origin': origin.date().isoformat(), 'training_rows': len(train),
                        'latest_training_date': train.Date.max().date().isoformat(),
                        'test_rows': int(eligible.sum()), 'optimizer_success': bool(model.fit_result.success)})
        for row in test[eligible].itertuples():
            if row.HomeTeam not in model.team_to_idx or row.AwayTeam not in model.team_to_idx:
                raise ValueError('Identity guard failed; fuzzy matching is forbidden')
            matrix, _ = model.score_matrix(row.HomeTeam, row.AwayTeam)
            for market, (p, y, baseline) in observations(matrix, (row.FTHG, row.FTAG), train).items():
                records.append({'date': row.Date.date().isoformat(), 'season': int(row.season),
                                'home': row.HomeTeam, 'away': row.AwayTeam,
                                'market': market, 'p': p, 'y': y, 'baseline': baseline})
    by_market = {}
    for market in sorted({x['market'] for x in records}):
        dev = [x for x in records if x['market'] == market and x['season'] == 2024]
        audit = [x for x in records if x['market'] == market and x['season'] == 2025]
        by_market[market] = summarize_market(dev, audit)
    # Final research fit is performed only after the validation protocol. Newly
    # corroborated league-phase results cannot change historical audit metrics.
    latest = pd.DataFrame([{'Date': pd.Timestamp(x['date']), 'HomeTeam': x['home'],
                            'AwayTeam': x['away'], 'FTHG': x['reported'][0],
                            'FTAG': x['reported'][1], 'season': 2026} for x in current])
    final_frame = pd.concat([frame, latest], ignore_index=True).sort_values('Date') if current else frame
    if final_frame.duplicated(['Date', 'HomeTeam', 'AwayTeam']).any():
        raise ValueError('Final research fit contains duplicate fixtures')
    as_of = pd.Timestamp('2026-10-22')
    final_model = DixonColesModel(half_life_days=240, l2=.08, bbs_statistics=False).fit(final_frame, as_of=as_of)
    counts = team_counts(final_frame)
    participants = sorted({x[k] for x in current for k in ('home', 'away')})
    coverage = {t: counts[t] for t in participants}
    params = {'teams': final_model.teams, 'attack': final_model.attack.tolist(),
              'weakness': final_model.weakness.tolist(), 'base': final_model.base,
              'home_adv': final_model.home_adv, 'rho': final_model.rho,
              'as_of': as_of.date().isoformat(), 'protocol': PROTOCOL}
    Path(output_dir, 'model_parameters.json').write_text(json.dumps(params, indent=2)+'\n')
    Path(output_dir, 'retrospective_predictions.json').write_text(json.dumps(records, indent=2)+'\n')
    return {'protocol': PROTOCOL, 'historical_rows': len(frame), 'training_rows': len(final_frame),
            'corroborated_current_rows': len(current),
            'training_start': frame.Date.min().date().isoformat(),
            'training_end': final_frame.Date.max().date().isoformat(),
            'final_optimizer_success': bool(final_model.fit_result.success),
            'development_predictions': sum(x['season'] == 2024 and x['market'] == 'Home win' for x in records),
            'audit_predictions': sum(x['season'] == 2025 and x['market'] == 'Home win' for x in records),
            'cold_team_excluded_fixtures': dict(excluded), 'windows': windows,
            'current_team_history': coverage, 'current_teams_under_six_matches': sum(n < 6 for n in coverage.values()),
            'markets': by_market, 'roi': None, 'ev': None, 'production_enabled': False,
            'limitations': ['Historical datasets retrieved after results; no point-in-time revision archive.',
                            'Chronological outcome-unseen holdout, not a prospective forward test.',
                            'Historical market prices unavailable; no market blend, EV or ROI claim.',
                            'Six-appearance filter reduces evaluation coverage and cannot certify current teams.',
                            'Many AH lines are correlated; diagnostic passes are not independent confirmations.',
                            'Current-season league-phase results enter final research fit only after corroboration.']}
