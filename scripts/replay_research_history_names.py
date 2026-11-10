"""Replay every frozen forecast with research under research v2 and v3 (the fixture-name fix).

Release evidence for a correctness fix the backtest can't test: in the harness the
fixture and the training history name a team the same way, so only live forecasts
show it. Research v2 looked each side's training history up under its fixture name,
so a side the history names differently ("Hull City" / "Hull") was frozen with an
empty history. v3 resolves the side to its training name (team_research.history_team).

Because the frozen input itself is empty, "after" has to rebuild those sides: the
pipeline's own training history (_history_for_league, cache only, one load per league
as of --history-as-of) is cut, as the live run did, to completed dates before the
forecast's run day and looked up under the side's training name. Every side whose
training name is its fixture name keeps its frozen rows, so the two versions differ
only where the name fix applies.

    before = v2 (current main) on the frozen inputs
    after  = v3 on the frozen inputs, with the rebuilt sides

Checks: each forecast's frozen probabilities are reproduced under its own version;
the rebuilt history reproduces every frozen non-empty side (looked up under the
fixture name, as live did); each training name equals the model's resolved team.
No result and no odds field is read, so this shows how far probabilities move, not
whether they improve. Writes summary.json and forecasts.csv (one line per forecast).

    python scripts/replay_research_history_names.py --output evaluation/research_fixture_name_replay
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
SIDES = ('home', 'away')
TOLERANCE = 1e-12


def hda(context) -> list[float] | None:
    margins = context.get('margin_distribution')
    if not margins:
        return None
    m = {int(d): float(p) for d, p in margins.items()}
    return [sum(p for d, p in m.items() if d > 0), m.get(0, 0.), sum(p for d, p in m.items() if d < 0)]


def league_keys() -> dict:
    from football_value_pipeline_v2_standalone import LEAGUES
    keys = {league.name: key for key, league in LEAGUES.items()}
    keys['Süper Lig'] = keys.get('Super Lig', 'SuperLig')
    return keys


class Histories:
    """The live training history per league, loaded once from the local cache as of `as_of`."""

    def __init__(self, as_of, cache='.football_cache'):
        import football_value_pipeline_v2_standalone as fv
        self.fv, self.as_of, self.cache = fv, as_of, cache
        self.pipe = fv.FootballValuePipelineV2(cache_dir=cache, odds_api_key='', football_data_api_key='',
                                               live_odds=False, domestic_seasons_back=6)
        self.frames, self.errors = {}, {}

    def __call__(self, league_key):
        if league_key not in self.frames and league_key not in self.errors:
            try:
                if league_key == 'UEL':  # never refresh the Europa cache from here
                    from europa_training import load
                    self.pipe._europa_preflight_history = load(self.cache, self.as_of, refresh_if_stale=False)
                frame = self.pipe._history_for_league(self.fv.LEAGUES[league_key], now=self.as_of)
                frame = frame.assign(Date=pd.to_datetime(frame['Date'], utc=True, errors='coerce'))
                self.frames[league_key] = frame
            except Exception as exc:  # reported, and the forecast keeps its frozen history
                self.errors[league_key] = f'{type(exc).__name__}: {str(exc)[:200]}'
        return self.frames.get(league_key)


def rebuilt_history(row, history, run_time, league_key, tr):
    """The v3 research_history_json for a frozen forecast, plus its checks."""
    frozen = tr.decode(row.get('research_history_json'))
    known = history.loc[history['Date'] < tr.utc(run_time).normalize()]
    teams = set(known['HomeTeam']) | set(known['AwayTeam'])
    names = {s: tr.history_team(row.get(s + '_team'), teams, league_key) for s in SIDES}
    if names['home'] is not None and names['home'] == names['away']:
        names = {s: None for s in SIDES}
    by_fixture = tr.form_history(history, row.get('home_team'), row.get('away_team'), run_time)
    by_training = tr.form_history(history, row.get('home_team'), row.get('away_team'), run_time, names=names)
    out, checks = {'teams': names}, {}
    for s in SIDES:
        renamed = names[s] is not None and tr.name(names[s]) != tr.name(row.get(s + '_team'))
        out[s] = by_training[s] if renamed else list(frozen.get(s, []))
        checks[s] = {'renamed': renamed, 'training_name': names[s],
                     'model_name_agrees': names[s] == row.get(f'model_{s}_team'),
                     'frozen_rows': len(frozen.get(s, [])), 'after_rows': len(out[s]),
                     'frozen_reproduced': (json.dumps(by_fixture[s], sort_keys=True)
                                           == json.dumps(frozen[s], sort_keys=True)) if frozen.get(s) else None}
    out['h2h'] = by_training['h2h'] if any(c['renamed'] for c in checks.values()) else list(frozen.get('h2h', []))
    return out, checks


def replay(root: Path, histories):
    import performance_tracking as pt
    import team_research as tr
    keys = league_keys()
    counts, records, latest, worst = Counter(), [], {}, 0.
    for meta, rows, _ in pt.snapshots(root):
        for row in rows:
            counts['forecasts'] += 1
            research = tr.decode(row.get('team_research_json'))
            if not research:
                continue
            counts['with_research'] += 1
            cutoff, evidence = tr.utc(research['observed_at_utc']), copy.deepcopy(research.get('evidence', {}))
            for key in DERIVED_EVIDENCE:
                evidence.pop(key, None)
            frozen_version = research.get('version', tr.LEGACY_VERSION)
            again = tr.prepare(row, cutoff, copy.deepcopy(evidence), version=frozen_version)
            if hda(research):
                frozen, replayed = research['margin_distribution'], again.get('margin_distribution') or {}
                gap = max(abs(float(frozen.get(k, 0.)) - float(replayed.get(k, 0.))) for k in set(frozen) | set(replayed))
                worst = max(worst, gap)
                counts['frozen_probabilities_checked'] += 1
                counts['frozen_probabilities_reproduced'] += gap <= TOLERANCE
            before = tr.prepare(row, cutoff, copy.deepcopy(evidence), version=tr.PREVIOUS_VERSION)
            league_key = keys.get(str(row.get('league')))
            history = histories(league_key) if league_key else None
            checks = {}
            after_row = dict(row)
            if frozen_version not in tr.FIXTURE_NAME_ONLY:
                counts['already_current_version'] += 1
            elif history is None:
                counts['history_unavailable'] += 1
            else:
                rebuilt, checks = rebuilt_history(row, history, meta['generated_at_utc'], league_key, tr)
                after_row['research_history_json'] = json.dumps(rebuilt, sort_keys=True)
                for c in checks.values():
                    counts['sides_rebuilt'] += 1
                    counts['sides_renamed'] += c['renamed']
                    counts['sides_unresolved'] += c['training_name'] is None
                    counts['training_name_agrees_with_model'] += c['model_name_agrees']
                    if c['frozen_reproduced'] is not None:
                        counts['frozen_history_sides_checked'] += 1
                        counts['frozen_history_sides_reproduced'] += c['frozen_reproduced']
            after = tr.prepare(after_row, cutoff, copy.deepcopy(evidence))
            same = lambda a, b: json.dumps(a, sort_keys=True, default=str) == json.dumps(b, sort_keys=True, default=str)
            changed = not (same(before['goal_rates'], after['goal_rates'])
                           and same(before.get('margin_distribution'), after.get('margin_distribution')))
            counts['changed' if changed else 'unchanged'] += 1
            key = (str(row.get('league')), tr.name(row.get('home_team')), tr.name(row.get('away_team')),
                   str(row.get('kickoff_utc')))
            if key not in latest or cutoff > latest[key][0]:
                latest[key] = (cutoff, len(records))
            record = {
                'snapshot_generated_utc': meta.get('generated_at_utc'), 'league': row.get('league'),
                'holdout_league': row.get('league') in HOLDOUT_LEAGUES,
                'home_team': row.get('home_team'), 'away_team': row.get('away_team'),
                'kickoff_utc': str(row.get('kickoff_utc')), 'research_observed_utc': cutoff.isoformat(),
                'frozen_version': frozen_version, 'before_version': tr.PREVIOUS_VERSION, 'after_version': tr.VERSION,
                'changed': changed}
            for i, s in enumerate(SIDES):
                c = checks.get(s, {})
                record.update({
                    f'{s}_training_name': c.get('training_name'), f'{s}_renamed': c.get('renamed', False),
                    f'{s}_history_rows_before': c.get('frozen_rows', len(tr.decode(row.get('research_history_json')).get(s, []))),
                    f'{s}_history_rows_after': c.get('after_rows'),
                    f'{s}_form_matches_before': before['form'][s]['all']['matches'],
                    f'{s}_form_matches_after': after['form'][s]['all']['matches'],
                    f'goal_rate_{s}_before': before['goal_rates'][i],
                    f'goal_rate_{s}_after': after['goal_rates'][i]})
            p0, p1 = hda(before), hda(after)
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
        frame.loc[[i for _, i in latest.values()], 'latest_forecast_of_fixture'] = True
    return counts, frame, worst


def movement(frame) -> dict:
    """How far the forecasts move, in probability points (0.01 = 1 point); unchanged ones count as 0."""
    out = {'forecasts': int(len(frame))}
    if not len(frame):
        return out
    sides = [(frame[f'{s}_history_rows_before'] == 0, frame[f'{s}_form_matches_before'] == 0,
              frame[f'{s}_history_rows_after'].fillna(frame[f'{s}_history_rows_before']) == 0,
              frame[f'{s}_form_matches_after'] == 0) for s in SIDES]
    out.update({
        'changed': int(frame['changed'].sum()),
        'sides': int(2 * len(frame)),
        'sides_renamed': int(sum(frame[f'{s}_renamed'].sum() for s in SIDES)),
        'sides_without_history_before': int(sum(a.sum() for a, _, _, _ in sides)),
        'sides_without_history_after': int(sum(c.sum() for _, _, c, _ in sides)),
        'sides_without_any_form_before': int(sum(b.sum() for _, b, _, _ in sides)),
        'sides_without_any_form_after': int(sum(d.sum() for _, _, _, d in sides))})
    changed = frame.loc[frame['changed']]
    if 'max_1x2_move' not in frame or not len(changed):
        return out
    move = changed['max_1x2_move'].dropna()
    signed = {o: (changed[f'p_{o}_after'] - changed[f'p_{o}_before']).dropna() for o in OUTCOMES}
    rates = pd.concat([(changed[f'goal_rate_{s}_after'] - changed[f'goal_rate_{s}_before']).abs() for s in SIDES])
    out['changed_forecasts'] = {
        'max_1x2_move': {'mean': float(move.mean()), 'median': float(move.median()),
                         'p90': float(move.quantile(.9)), 'max': float(move.max())},
        'max_1x2_move_buckets': {'under_1_point': int((move < .01).sum()),
                                 '1_to_2_points': int(((move >= .01) & (move < .02)).sum()),
                                 '2_to_5_points': int(((move >= .02) & (move < .05)).sum()),
                                 '5_points_or_more': int((move >= .05).sum())},
        'mean_signed_move': {o: float(v.mean()) for o, v in signed.items()},
        'over_1_5_move': {'mean': float(changed['over_1_5_move'].mean()), 'max': float(changed['over_1_5_move'].max())},
        'goal_rate_move': {'mean': float(rates.mean()), 'max': float(rates.max())},
        'largest': changed.nlargest(5, 'max_1x2_move')[['league', 'home_team', 'away_team', 'max_1x2_move']]
                          .to_dict('records')}
    return out


def summarize(counts, frame, errors) -> dict:
    latest = frame.loc[frame['latest_forecast_of_fixture']] if len(frame) else frame
    domestic = ~latest['league'].isin(('UEFA Champions League', 'UEFA Europa League')) if len(latest) else latest
    holdout = latest['holdout_league'] if len(latest) else latest
    return {
        'forecasts': dict(counts),
        'history_load_errors': errors,
        'all_forecasts': movement(frame),
        'latest_forecast_per_fixture': {
            'all': movement(latest),
            'domestic': movement(latest.loc[domestic]) if len(latest) else {'forecasts': 0},
            # The locked holdout leagues are kept apart. No result is read here.
            'holdout_leagues': movement(latest.loc[holdout]) if len(latest) else {'forecasts': 0},
            'other_leagues': movement(latest.loc[~holdout]) if len(latest) else {'forecasts': 0},
            'by_league': {league: movement(rows) for league, rows in latest.groupby('league')} if len(latest) else {}},
        'note': ('before = research v2 on the frozen inputs; after = v3, with each renamed side rebuilt from the '
                 'training history under its training name. Probabilities only: no result and no odds field is read.'),
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('--root', type=Path, default=REPO / 'football_output_v2')
    parser.add_argument('--cache', default='.football_cache')
    parser.add_argument('--history-as-of', help='training-history load time (default: the latest research observation)')
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args(argv)
    import performance_tracking as pt
    import team_research as tr
    as_of = tr.utc(args.history_as_of) if args.history_as_of else max(
        tr.utc(tr.decode(r.get('team_research_json'))['observed_at_utc'])
        for _, rows, _ in pt.snapshots(args.root) for r in rows if tr.decode(r.get('team_research_json')))
    with warnings.catch_warnings():
        warnings.simplefilter('ignore')
        histories = Histories(as_of.to_pydatetime(), args.cache)
        counts, frame, worst = replay(args.root, histories)
    summary = {'before_version': tr.PREVIOUS_VERSION, 'after_version': tr.VERSION,
               'history_as_of_utc': as_of.isoformat(), 'frozen_probabilities_max_abs_diff': worst,
               **summarize(counts, frame, histories.errors)}
    args.output.mkdir(parents=True, exist_ok=True)
    (args.output / 'summary.json').write_text(json.dumps(summary, indent=2, sort_keys=True, default=str) + '\n',
                                              encoding='utf-8')
    frame.to_csv(args.output / 'forecasts.csv', index=False, lineterminator='\n', float_format='%.6f')
    print(json.dumps(summary, indent=2, sort_keys=True, default=str))
    reproduced = counts['frozen_probabilities_checked'] == counts['frozen_probabilities_reproduced']
    history_ok = counts['frozen_history_sides_checked'] == counts['frozen_history_sides_reproduced']
    return 0 if counts['with_research'] and reproduced and history_ok else 1


if __name__ == '__main__':
    raise SystemExit(main())
