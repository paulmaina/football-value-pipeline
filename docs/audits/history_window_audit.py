"""Offline paired four/six-season diagnostic; never changes production settings."""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

import numpy as np
import pandas as pd
from football_value_pipeline_v2_standalone import DixonColesModel, LEAGUES, read_csv_bytes, validated_match_history
from refresh_training_data import DIVISIONS, inspect_csv


def run():
    clock = datetime.now(timezone.utc)
    status = json.loads((ROOT/'docs/training_refresh_status.json').read_text())
    by_path = {item['path']: item for item in status['files']}
    audit = {'checked_at_utc': clock.isoformat(), 'seasons': list(range(2021, 2027)),
        'source': 'Football-Data.co.uk', 'leagues': {}, 'extra_completed_matches': 0,
        'evaluation': 'Retrospective current-revision score history; monthly pre-match fits on identical Aug-Oct 2026 fixtures. No odds or BBS features. Not forward evidence or a parameter-selection experiment.',
        'automatic_promotion': False}
    for key, division in DIVISIONS.items():
        frames = []; files = []
        for year in range(2021, 2027):
            code = f'{year%100:02d}{(year+1)%100:02d}'
            path = ROOT/'.football_cache'/f'{code}_{division}.csv'
            data = path.read_bytes()
            matches = inspect_csv(data, division, year, clock)
            frame = read_csv_bytes(data)
            completed = frame.loc[~(frame.FTHG.isna() & frame.FTAG.isna())].copy()
            coverage = {field: int(completed[field].notna().sum()) if field in completed else 0
                        for field in ('HS','AS','HST','AST','HC','AC','HF','AF','HY','AY','HR','AR')}
            frame['Season'] = code
            frame['Date'] = pd.to_datetime(frame.Date, dayfirst=True, errors='raise')
            frames.append(validated_match_history(frame))
            rel = path.relative_to(ROOT).as_posix()
            by_path[rel]['statistic_nonempty_rows'] = coverage
            files.append({'path': rel, 'sha256': hashlib.sha256(data).hexdigest(),
                          'completed_matches': len(matches), 'statistic_nonempty_rows': coverage})
        full = pd.concat(frames, ignore_index=True, sort=False).sort_values('Date')
        if full.duplicated(['Date', 'HomeTeam', 'AwayTeam']).any():
            raise ValueError('Duplicate historical fixture across seasons')
        old = full[full.Season.astype(int) >= 2324]
        expected = len(full)-len(old)
        results = {4: [], 6: []}; targets = []
        for start, end in [('2026-08-01','2026-09-01'), ('2026-09-01','2026-10-01'),
                           ('2026-10-01','2026-10-19')]:
            test = full[(full.Date >= start) & (full.Date < end)]
            if test.empty: continue
            models = {}
            for window, history in [(4, old), (6, full)]:
                training = history[history.Date < start]
                model = DixonColesModel(half_life_days=240, l2=.08, bbs_statistics=False).fit(
                    training, as_of=pd.Timestamp(start))
                if not model.fit_result.success:
                    raise ValueError('Diagnostic fit failed')
                models[window] = model
            for row in test.itertuples():
                target = 0 if row.FTHG > row.FTAG else 2 if row.FTHG < row.FTAG else 1
                targets.append(target)
                for window, model in models.items():
                    matrix, _ = model.score_matrix(row.HomeTeam, row.AwayTeam)
                    pred = model.one_x_two(matrix)
                    p = np.array([pred['home'], pred['draw'], pred['away']])
                    if not np.isfinite(p).all() or abs(p.sum()-1)>1e-8:
                        raise ValueError('Invalid probability vector')
                    results[window].append(p)
        outcomes = np.eye(3)[targets]
        metrics = {}
        for window, probabilities in results.items():
            p = np.array(probabilities)
            metrics[str(window)] = {'matches': len(p),
                'log_loss': float(-np.log(np.clip(p[np.arange(len(p)), targets],1e-15,1)).mean()),
                'multiclass_brier_sum': float(((p-outcomes)**2).sum(axis=1).mean())}
        audit['leagues'][key] = {'four_season_matches': len(old), 'six_season_matches': len(full),
            'extra_matches': expected, 'files': files, 'paired_score_only_metrics': metrics}
        audit['extra_completed_matches'] += expected
        print(key, len(old), '->', len(full), metrics, flush=True)
    audit['paired_matches'] = sum(item['paired_score_only_metrics']['4']['matches'] for item in audit['leagues'].values())
    audit['pooled_score_only_metrics'] = {str(window): {metric: sum(
        item['paired_score_only_metrics'][str(window)][metric] * item['paired_score_only_metrics'][str(window)]['matches']
        for item in audit['leagues'].values()) / audit['paired_matches']
        for metric in ('log_loss','multiclass_brier_sum')} for window in (4,6)}
    (ROOT/'docs/six_season_history_audit.json').write_text(json.dumps(audit,indent=2)+'\n')
    (ROOT/'docs/training_refresh_status.json').write_text(json.dumps(status,indent=2)+'\n')


if __name__ == '__main__':
    run()
