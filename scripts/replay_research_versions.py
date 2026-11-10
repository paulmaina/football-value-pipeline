"""Replay every frozen forecast under the research version it was frozen with and under the current one.

Release evidence for a correctness fix to team_research.prepare() that the backtest
can't test, because ESPN rows exist only in live forecasts. Each row of each snapshot
under <root>/performance/snapshots is recomputed twice from its own frozen inputs (the
row, the research observation time and the frozen pre-kickoff evidence): once as it
was frozen ("before") and once with the current version ("after"). No result and no
odds field is read, so this shows how far probabilities move, not whether they improve.

Writes summary.json and forecasts.csv (one line per forecast whose research changed).

    python scripts/replay_research_versions.py --output evaluation/research_form_identity_replay
"""
from __future__ import annotations

import argparse
from collections import Counter
import copy
import json
from pathlib import Path
import sys
import warnings

import pandas as pd

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO))
DERIVED_EVIDENCE = ('quality_review', 'rest_and_travel')  # written by enrich()/prepare(), not inputs
HOLDOUT_LEAGUES = ('Eredivisie', 'Primeira Liga', 'Super Lig', 'Süper Lig')
OUTCOMES = ('home', 'draw', 'away')
TOLERANCE = 1e-12


def hda(context) -> list[float] | None:
    margins = context.get('margin_distribution')
    if not margins:
        return None
    m = {int(d): float(p) for d, p in margins.items()}
    return [sum(p for d, p in m.items() if d > 0), m.get(0, 0.), sum(p for d, p in m.items() if d < 0)]


def repeated_rows(rows, team, tr) -> int:
    """Results kept more than once: same day, venue and score for this team."""
    seen = Counter((tr.utc(r['date']).date(), tr.name(r.get('home')) == tr.name(team),
                    r.get('home_goals'), r.get('away_goals')) for r in rows)
    return sum(n - 1 for n in seen.values())


def replay(root: Path):
    import performance_tracking as pt
    import team_research as tr
    counts, records, latest, worst = Counter(), [], {}, 0.  # latest: fixture -> (observed, index into records or None)
    for meta, rows, _ in pt.snapshots(root):
        for row in rows:
            counts['forecasts'] += 1
            research = tr.decode(row.get('team_research_json'))
            if research:
                counts['with_research'] += 1
                cutoff, evidence = tr.utc(research['observed_at_utc']), copy.deepcopy(research.get('evidence', {}))
                for key in DERIVED_EVIDENCE:
                    evidence.pop(key, None)
                frozen_version = research.get('version', tr.LEGACY_VERSION)
            else:  # as profit_shortlist.context() does for a forecast without research
                cutoff, evidence = tr.utc(meta['generated_at_utc']), {'errors': ['research not collected for this forecast']}
                frozen_version = tr.LEGACY_VERSION
            before = tr.prepare(row, cutoff, copy.deepcopy(evidence), version=frozen_version)
            after = tr.prepare(row, cutoff, copy.deepcopy(evidence))
            if research and hda(research):
                # "before" must be the forecast as it was frozen, or the comparison means nothing.
                frozen, again = research['margin_distribution'], before.get('margin_distribution') or {}
                gap = max(abs(float(frozen.get(k, 0.)) - float(again.get(k, 0.))) for k in set(frozen) | set(again))
                worst = max(worst, gap)
                counts['frozen_probabilities_checked'] += 1
                counts['frozen_probabilities_reproduced'] += gap <= TOLERANCE
            key = (str(row.get('league')), tr.name(row.get('home_team')), tr.name(row.get('away_team')),
                   str(row.get('kickoff_utc')))
            newest = bool(research) and (key not in latest or cutoff > latest[key][0])
            compare = lambda c: json.dumps({k: v for k, v in c.items() if k != 'version'}, sort_keys=True, default=str)
            if compare(before) == compare(after):
                counts['unchanged'] += 1
                if newest:
                    latest[key] = (cutoff, None)
                continue
            counts['changed'] += 1
            if newest:
                latest[key] = (cutoff, len(records))
            p0, p1 = hda(before), hda(after)
            view = tr.research_evidence(evidence) if tr.observed_by(evidence, cutoff) else {}
            history = tr.decode(row.get('research_history_json'))
            removed = {}
            for side in ('home', 'away'):
                rows_in = list(history.get(side, [])) + list(view.get('recent', {}).get(side, []))
                kept = tr.form_rows(row.get(side + '_team'), rows_in, cutoff, version=frozen_version)
                removed[side] = repeated_rows(kept, row.get(side + '_team'), tr)
            record = {
                'snapshot_generated_utc': meta.get('generated_at_utc'), 'league': row.get('league'),
                'home_team': row.get('home_team'), 'away_team': row.get('away_team'),
                'kickoff_utc': str(row.get('kickoff_utc')), 'research_observed_utc': cutoff.isoformat(),
                'frozen_version': frozen_version, 'current_version': tr.VERSION,
                'repeated_rows_home': removed['home'], 'repeated_rows_away': removed['away'],
                'goal_rate_home_before': before['goal_rates'][0], 'goal_rate_home_after': after['goal_rates'][0],
                'goal_rate_away_before': before['goal_rates'][1], 'goal_rate_away_after': after['goal_rates'][1]}
            if p0 and p1:
                for i, outcome in enumerate(OUTCOMES):
                    record[f'p_{outcome}_before'], record[f'p_{outcome}_after'] = p0[i], p1[i]
                record.update(p_over_1_5_before=before['p_over_1_5'], p_over_1_5_after=after['p_over_1_5'],
                              max_1x2_move=max(abs(a - b) for a, b in zip(p0, p1)),
                              over_1_5_move=abs(after['p_over_1_5'] - before['p_over_1_5']))
            records.append(record)
    frame = pd.DataFrame(records)
    if len(frame):
        frame['latest_forecast_of_fixture'] = False
        frame.loc[[i for _, i in latest.values() if i is not None], 'latest_forecast_of_fixture'] = True
    # Distinct fixtures that carry research, per league: the denominator for the changed fixtures.
    return counts, frame, Counter(league for league, *_ in latest), worst


def movement(frame) -> dict:
    """How far the changed forecasts move, in probability points (0.01 = 1 point)."""
    if not len(frame) or 'max_1x2_move' not in frame:
        return {'forecasts': int(len(frame))}
    move = frame['max_1x2_move'].dropna()
    signed = {o: (frame[f'p_{o}_after'] - frame[f'p_{o}_before']).dropna() for o in OUTCOMES}
    rates = pd.concat([(frame[f'goal_rate_{s}_after'] - frame[f'goal_rate_{s}_before']).abs() for s in ('home', 'away')])
    return {
        'forecasts': int(len(frame)),
        'repeated_rows_removed': int(frame['repeated_rows_home'].sum() + frame['repeated_rows_away'].sum()),
        'max_1x2_move': {'mean': float(move.mean()), 'median': float(move.median()),
                         'p90': float(move.quantile(.9)), 'max': float(move.max())},
        'max_1x2_move_buckets': {'under_0.5_points': int((move < .005).sum()),
                                 '0.5_to_1_point': int(((move >= .005) & (move < .01)).sum()),
                                 '1_to_2_points': int(((move >= .01) & (move < .02)).sum()),
                                 '2_points_or_more': int((move >= .02).sum())},
        'mean_signed_move': {o: float(v.mean()) for o, v in signed.items()},
        'over_1_5_move': {'mean': float(frame['over_1_5_move'].mean()), 'max': float(frame['over_1_5_move'].max())},
        'goal_rate_move': {'mean': float(rates.mean()), 'max': float(rates.max())},
    }


def summarize(counts, frame, fixtures) -> dict:
    latest = frame.loc[frame['latest_forecast_of_fixture']] if len(frame) else frame
    holdout = latest['league'].isin(HOLDOUT_LEAGUES) if len(latest) else pd.Series(dtype=bool)
    by_league = {}
    for league, total in sorted(fixtures.items()):
        rows = latest.loc[latest['league'].eq(league)] if len(latest) else latest
        by_league[league] = {'fixtures_with_research': int(total), **movement(rows)}
    return {
        'forecasts': dict(counts),
        'fixtures_with_research': int(sum(fixtures.values())),
        'all_changed_forecasts': movement(frame),
        'latest_forecast_per_fixture': {
            'all': movement(latest),
            # The locked holdout leagues are kept apart, as in the parity report. No result is read here.
            'holdout_leagues': movement(latest.loc[holdout]) if len(latest) else {'forecasts': 0},
            'other_leagues': movement(latest.loc[~holdout]) if len(latest) else {'forecasts': 0},
            'by_league': by_league},
        'note': ('before = the version each forecast was frozen with; after = the current version. Same frozen '
                 'inputs for both. Probabilities only: no result and no odds field is read.'),
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('--root', type=Path, default=REPO / 'football_output_v2')
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args(argv)
    with warnings.catch_warnings():
        warnings.simplefilter('ignore')
        counts, frame, fixtures, worst = replay(args.root)
    import team_research as tr
    summary = {'current_version': tr.VERSION, 'frozen_probabilities_max_abs_diff': worst,
               **summarize(counts, frame, fixtures)}
    args.output.mkdir(parents=True, exist_ok=True)
    (args.output / 'summary.json').write_text(json.dumps(summary, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    frame.to_csv(args.output / 'forecasts.csv', index=False, lineterminator='\n', float_format='%.6f')
    print(json.dumps(summary, indent=2, sort_keys=True))
    return 0 if counts['forecasts'] and counts['frozen_probabilities_checked'] == counts['frozen_probabilities_reproduced'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
