"""C3 (Understat xG in team form) versus C and C2 on the development period only.

Reads a locked harness run (`python evaluation_harness.py --output DIR`) and the
Understat cache. Only development rows are read: validation, retrospective and
holdout rows are never loaded into the report (a holdout row anywhere aborts it).

Declared before the run (docs/plan.md, Phase 2d):
  - primary subset: the five Understat leagues (C3 equals C elsewhere by construction);
    all eight leagues are shown as well;
  - metrics: AH all lines, AH draw-sensitive (0, +/-0.5), 1X2 and Over 1.5 log loss on the
    common cohort (C, C2, C3, M, D, A all available), paired C - C3 and C2 - C3 with whole
    weeks resampled (evaluation_harness.paired);
  - 1X2 calibration of home and away probabilities by decile (C, C2, C3, five leagues), a
    logistic calibration slope per outcome (slope > 1: forecasts too flat), and strong
    favourites (the side with the higher home/away probability at 0.6 or more).

It also writes the team-name mapping report: every Understat team, its football-data
name, how many of its matches line up on the same date and score, and anything unmatched.

    python scripts/c3_development_report.py --run DIR --output evaluation/c3_understat_xg
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

import numpy as np
import pandas as pd

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO))
GROUPS = ('AH all', 'AH draw-sensitive', '1X2', 'Over 1.5')
COHORT = ('C', 'C2', 'C3', 'M', 'D', 'A')
RESEARCH = ('C', 'C2', 'C3')
PHASE = 'development'


def mapping_report(cache, cfg):
    import historical_benchmark as hb
    import understat_history as uh
    out = {}
    for league in uh.LEAGUES:
        data, _, _ = hb.load_history(Path(cache), league, {**cfg, 'test_end_exclusive': cfg['end_exclusive']})
        raw = uh.raw_matches(cache, league)
        table = uh.aliases(league)
        proposed = uh.propose_aliases(raw, data)
        fd_teams = set(data.HomeTeam) | set(data.AwayTeam)
        teams = {}
        for team, p in sorted(proposed.items()):
            mapped = table.get(team, team)
            teams[team] = {'football_data': mapped if mapped in fd_teams else None, 'reviewed_alias': team in table,
                           'agrees_with_fixture_evidence': p['football_data'] == mapped,
                           'agreeing_matches': p['agreeing_matches'], 'understat_matches': p['understat_matches']}
        covered = data.loc[data.Date.dt.normalize() <= raw.date.max()] if not raw.empty else data.iloc[:0]
        covered = covered.loc[covered.Date >= raw.date.min()] if not raw.empty else covered
        mapped_names = {table.get(t, t) for t in proposed}
        attached, counts = uh.with_xg(data, cache, league)
        seasons = {}
        for season in cfg['seasons']:
            start = pd.Timestamp(f'20{season[:2]}-07-01')
            part = attached.loc[(attached.Date >= start) & (attached.Date < start + pd.DateOffset(years=1))]
            seasons[season] = {'football_data_matches': len(part), 'with_xg': int(part.HxG.notna().sum())}
        out[league] = {'teams': teams,
                       'understat_teams_unmatched': sorted(t for t, v in teams.items() if v['football_data'] is None
                                                           or not v['agrees_with_fixture_evidence']),
                       'football_data_teams_without_understat': sorted(
                           (set(covered.HomeTeam) | set(covered.AwayTeam)) - mapped_names),
                       'attach_counts': dict(counts), 'by_season': seasons}
    return out


def logistic_slope(p, y):
    """Calibration slope b of logit P(y) = a + b * logit(p), by Newton's method."""
    p = np.clip(np.asarray(p, float), 1e-6, 1 - 1e-6)
    x = np.column_stack([np.ones(len(p)), np.log(p / (1 - p))])
    w = np.zeros(2)
    for _ in range(50):
        q = 1 / (1 + np.exp(-x @ w))
        step = np.linalg.solve((x * (q * (1 - q))[:, None]).T @ x, x.T @ (np.asarray(y, float) - q))
        w += step
        if np.abs(step).max() < 1e-10:
            break
    return float(w[1])


def calibration(frame):
    out = {}
    for cand in RESEARCH:
        part = frame.loc[frame.candidate == cand]
        entry = {}
        for k, outcome in enumerate(('home', 'draw', 'away')):
            p, y = part['p_' + outcome], (part.outcome == k).astype(int)
            bins = np.minimum(9, (p * 10).astype(int))
            entry[outcome] = {
                'forecasts': len(part), 'mean_forecast': float(p.mean()), 'observed_rate': float(y.mean()),
                'calibration_slope': logistic_slope(p, y),
                'deciles': [{'bin_lower': b / 10, 'n': int((bins == b).sum()), 'mean_forecast': float(p[bins == b].mean()),
                             'observed_rate': float(y[bins == b].mean()),
                             'observed_minus_forecast': float(y[bins == b].mean() - p[bins == b].mean())}
                            for b in sorted(bins.unique())]}
        fav_home = part.p_home >= part.p_away
        fav_p = np.where(fav_home, part.p_home, part.p_away)
        fav_won = np.where(fav_home, part.outcome == 0, part.outcome == 2)
        entry['strong_favourites'] = {}
        for low in (.6, .7):
            m = fav_p >= low
            entry['strong_favourites'][f'{low:.1f}+'] = {
                'n': int(m.sum()), 'mean_forecast': float(fav_p[m].mean()), 'observed_win_rate': float(fav_won[m].mean()),
                'observed_minus_forecast': float(fav_won[m].mean() - fav_p[m].mean())}
        out[cand] = entry
    return out


def compare(scores, leagues):
    import evaluation_harness as eh
    out = {}
    for group in GROUPS:
        part = scores.loc[(scores.group == group) & scores.league.isin(leagues)]
        table = part.pivot_table(index='fixture_key', columns='candidate', values='log_loss')
        keep = table[list(COHORT)].dropna().index
        part = part.loc[part.fixture_key.isin(keep)]
        means = part.groupby('candidate').log_loss.mean()
        out[group] = {'fixtures': int(len(keep)), 'mean_log_loss': {c: float(means[c]) for c in COHORT},
                      'C3_vs_C': eh.paired(part, 'C', 'C3'), 'C3_vs_C2': eh.paired(part, 'C2', 'C3'),
                      'C3_vs_M': eh.paired(part, 'M', 'C3')}
    return out


def main(argv=None):
    import understat_history as uh
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('--run', type=Path, required=True)
    parser.add_argument('--cache', type=Path, default=REPO / '.football_cache')
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args(argv)
    cfg = json.loads((REPO / 'evaluation_harness_config.json').read_text(encoding='utf-8'))
    results = json.loads((args.run / 'results.json').read_text(encoding='utf-8'))
    if results.get('mode') != 'historical':
        raise ValueError('Expected a locked historical run')
    scores = pd.read_csv(args.run / 'fixture_scores.csv')
    forecasts = pd.read_csv(args.run / 'forecasts_1x2.csv')
    if (scores.phase == 'holdout').any() or (forecasts.phase == 'holdout').any():
        raise ValueError('Holdout rows found; this report reads locked runs only')
    scores, forecasts = scores.loc[scores.phase == PHASE], forecasts.loc[forecasts.phase == PHASE]
    five = list(uh.LEAGUES)
    wide = forecasts.pivot_table(index='fixture_key', columns='candidate', values=['p_home', 'p_draw', 'p_away'])
    moved = (wide.xs('C3', level=1, axis=1) - wide.xs('C', level=1, axis=1)).abs().max(axis=1)
    in_five = moved.index.str.split('|').str[0].isin(five)
    cal_frame = forecasts.loc[forecasts.league.isin(five)]
    common = set.intersection(*(set(cal_frame.loc[cal_frame.candidate == c, 'fixture_key']) for c in RESEARCH))
    report = {
        'source_commit': results['source_commit'], 'harness_version': results['version'], 'phase': PHASE,
        'understat_manifest': {k: {f: v[f] for f in ('source', 'source_url', 'fetched_at_utc', 'raw_sha256',
                                                     'file_sha256', 'matches', 'results', 'complete')}
                               for k, v in uh.manifest(args.cache)['files'].items()},
        'understat_missing': sorted(uh.manifest(args.cache).get('missing', {})),
        'team_mapping': mapping_report(args.cache, cfg),
        'c3_movement_five_leagues': {
            'fixtures': int(in_five.sum()), 'changed': int((moved[in_five] > 1e-12).sum()),
            'mean_max_1x2_move_points': float(100 * moved[in_five].mean()),
            'p90_max_1x2_move_points': float(100 * moved[in_five].quantile(.9)),
            'max_1x2_move_points': float(100 * moved[in_five].max())},
        'five_understat_leagues (primary)': compare(scores, five),
        'all_eight_leagues': compare(scores, cfg['leagues']),
        'calibration_1x2_five_leagues': calibration(cal_frame.loc[cal_frame.fixture_key.isin(common)]),
        'notes': ['Development period only (1 Aug 2022 - 30 Jun 2025); no other period is read.',
                  'mean_gain > 0 means C3 has the lower log loss (C3_vs_C: C minus C3; C3_vs_C2: C2 minus C3).',
                  'Intervals resample whole calendar weeks (2,000 draws, seed 136, evaluation_harness.paired).',
                  'Calibration slope > 1 means the forecasts are too flat (outcomes more extreme than forecast).',
                  'Strong favourite: the side with the higher of the home and away probabilities.']}
    args.output.mkdir(parents=True, exist_ok=True)
    (args.output / 'summary.json').write_text(json.dumps(report, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    for subset in ('five_understat_leagues (primary)', 'all_eight_leagues'):
        for group, e in report[subset].items():
            for name in ('C3_vs_C', 'C3_vs_C2'):
                r = e[name]
                print(subset, group, name, e['fixtures'], f"{r['mean_gain']:+.5f}",
                      [round(v, 5) for v in r['interval_95']])
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
