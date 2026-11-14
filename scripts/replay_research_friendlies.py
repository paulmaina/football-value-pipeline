"""Live-replay comparison for research v4: friendlies left out of the last-ten form.

Release evidence for a correctness fix the backtest can't test, because ESPN rows
exist only in live forecasts. Every frozen forecast with research is recomputed from
its own frozen inputs:

  frozen  under the version it was frozen with (must reproduce its stored numbers)
  before  research v3, the live rule before this change. A v1/v2 domestic forecast whose
          side the fixture and training history name differently gets that side's history
          rebuilt as in scripts/replay_research_history_names.py; European fixtures keep
          their frozen history, as in scripts/research_parity_latest_rule.py.
  after   research v4 on the same inputs.

Frozen ESPN rows carry no competition (v4 starts recording it), so each one is
labelled with the competition ESPN files it under, from the team's all-competitions
schedule (scripts/research_parity_latest_rule.py, labels cached in
evaluation/research_parity_latest_rule/espn_competitions.json; --fetch-espn fetches
any team-season missing from it). A row with no single label keeps no competition
and stays in the form, as it would live.

No result and no odds field is read: this shows how far probabilities move, not
whether they improve. Holdout leagues are reported apart.

    python scripts/replay_research_friendlies.py --output evaluation/research_friendlies_replay
"""
from __future__ import annotations

import argparse
from collections import Counter
import copy
import importlib.util
import json
from pathlib import Path
import sys
import warnings

import pandas as pd

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO))
OUTCOMES = ('home', 'draw', 'away')
SIDES = ('home', 'away')
HOLDOUT_LEAGUES = ('Eredivisie', 'Primeira Liga', 'Super Lig', 'Süper Lig')
EUROPEAN_LEAGUES = ('UEFA Champions League', 'UEFA Europa League')
LABELS = REPO / 'evaluation' / 'research_parity_latest_rule' / 'espn_competitions.json'
PARITY_CSV = REPO / 'evaluation' / 'research_parity_latest_rule' / 'forecasts.csv'
TOLERANCE = 1e-12


def load_script(name):
    spec = importlib.util.spec_from_file_location(name, REPO / 'scripts' / f'{name}.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def group_of(league) -> str:
    return 'europa' if league in EUROPEAN_LEAGUES else 'holdout_leagues' if league in HOLDOUT_LEAGUES else 'five_leagues'


def labelled_evidence(evidence, labels, league_slug, parity, tr):
    """Evidence whose ESPN rows carry their ESPN competition slug; counts of what was labelled."""
    out, counts = copy.deepcopy(evidence), Counter()
    for side in SIDES:
        for r in (out.get('recent') or {}).get(side, []):
            if not parity.team_id(r.get('source')):
                continue  # Understat or another non-ESPN source: no competition
            counts['espn_rows'] += 1
            if r.get('competition'):
                counts['already_labelled'] += 1
                continue
            label, slug = parity.classify(r, labels, league_slug, tr)
            r['competition'] = slug if label != 'unknown' else None
            counts['labelled' if r['competition'] else 'unlabelled'] += 1
    return out, counts


def needed_labels(root, tr, parity):
    import performance_tracking as pt
    needed = set()
    for _, rows, _ in pt.snapshots(root):
        for row in rows:
            research = tr.decode(row.get('team_research_json'))
            for rows_ in ((research.get('evidence') or {}).get('recent') or {}).values():
                for r in rows_:
                    if parity.team_id(r.get('source')) and pd.notna(tr.utc(r.get('date'))):
                        needed.add((parity.team_id(r['source']), parity.season_of(tr.utc(r['date']))))
    return needed


def replay(root, labels, histories):
    import evaluation_harness as eh
    import performance_tracking as pt
    import team_research as tr
    names = load_script('replay_research_history_names')
    parity = load_script('research_parity_latest_rule')
    keys = names.league_keys()
    counts, records, worst = Counter(), [], 0.
    for meta, rows, _ in pt.snapshots(root):
        for row in rows:
            counts['forecasts'] += 1
            research = tr.decode(row.get('team_research_json'))
            if not research.get('margin_distribution'):
                counts['without_research'] += 1
                continue
            counts['with_research'] += 1
            cutoff = tr.utc(research.get('observed_at_utc'))
            evidence = copy.deepcopy(research.get('evidence', {}))
            for key in eh.DERIVED_EVIDENCE:
                evidence.pop(key, None)
            frozen_version = research.get('version', tr.LEGACY_VERSION)
            counts['frozen:' + frozen_version] += 1
            frozen = names.hda(research)
            again = names.hda(tr.prepare(row, cutoff, copy.deepcopy(evidence), version=frozen_version))
            diff = max(abs(a - b) for a, b in zip(frozen, again))
            worst = max(worst, diff)
            if diff > TOLERANCE:
                counts['frozen_not_reproduced'] += 1
            league = str(row.get('league'))
            league_key = keys.get(league)
            current = dict(row)
            # European fixtures keep their frozen history, as in scripts/research_parity_latest_rule.py
            # (the local checkout's Europa training cache is not the one live used).
            if frozen_version in tr.FIXTURE_NAME_ONLY and league_key and league_key not in ('UEL', 'UCL'):
                history = histories(league_key)
                if history is not None and history.attrs:
                    # Frame metadata (BBS observations) only; pandas deep-copies it on every
                    # column access, which made the rebuild ~100x slower. Rows are untouched.
                    history.attrs = {}
                if history is None:
                    counts['history_unavailable:' + league_key] += 1
                else:
                    rebuilt, _ = names.rebuilt_history(row, history, meta['generated_at_utc'], league_key, tr)
                    current['research_history_json'] = json.dumps(rebuilt, sort_keys=True)
            view, labelled = labelled_evidence(evidence, labels, tr.LEAGUES.get(league, ''), parity, tr)
            counts.update({'espn_' + k: v for k, v in labelled.items()})
            before = tr.prepare(current, cutoff, copy.deepcopy(view), version=tr.V3_VERSION)
            after = tr.prepare(current, cutoff, copy.deepcopy(view), version=tr.V4_VERSION)
            inputs = tr.research_inputs(current)
            used = {s: eh._used_rows(inputs, view, cutoff, s, tr.V3_VERSION) for s in SIDES}
            friendly_used = {s: sum(tr.is_friendly(r.get('competition')) for r in used[s]) for s in SIDES}
            b, a = names.hda(before), names.hda(after)
            records.append({
                'league': league, 'group': group_of(league), 'home_team': row.get('home_team'),
                'away_team': row.get('away_team'), 'kickoff_utc': str(row.get('kickoff_utc')),
                'snapshot_generated_utc': meta.get('generated_at_utc'), 'research_observed_utc': cutoff.isoformat(),
                'frozen_version': frozen_version, 'frozen_reproduced_max_abs_diff': diff,
                **{f'p_{o}_before': v for o, v in zip(OUTCOMES, b)},
                **{f'p_{o}_after': v for o, v in zip(OUTCOMES, a)},
                'p_over_1_5_before': before.get('p_over_1_5'), 'p_over_1_5_after': after.get('p_over_1_5'),
                'goal_rate_home_before': before['goal_rates'][0], 'goal_rate_away_before': before['goal_rates'][1],
                'goal_rate_home_after': after['goal_rates'][0], 'goal_rate_away_after': after['goal_rates'][1],
                'friendlies_in_form_before_home': friendly_used['home'],
                'friendlies_in_form_before_away': friendly_used['away'],
                'friendlies_excluded_after': sum((after.get('form_friendlies_excluded') or {}).values()),
                'form_matches_after_home': after['form']['home']['all']['matches'],
                'form_matches_after_away': after['form']['away']['all']['matches'],
                'move_1x2': max(abs(x - y) for x, y in zip(b, a)),
                'move_over_1_5': abs(before['p_over_1_5'] - after['p_over_1_5']),
                'move_goal_rates': max(abs(x - y) for x, y in zip(before['goal_rates'], after['goal_rates']))})
    frame = pd.DataFrame(records)
    if len(frame):
        key = ['league', 'home_team', 'away_team', 'kickoff_utc']
        latest = frame.groupby(key)['research_observed_utc'].transform('max')
        frame['latest_forecast_of_fixture'] = frame['research_observed_utc'].eq(latest)
        frame['changed'] = frame['move_1x2'] > TOLERANCE
    return frame, counts, worst


def movement(rows) -> dict:
    changed = rows.loc[rows['changed']]
    out = {'fixtures': int(len(rows)), 'changed': int(len(changed)),
           'with_friendlies_in_form_before': int(((rows['friendlies_in_form_before_home']
                                                   + rows['friendlies_in_form_before_away']) > 0).sum()),
           'friendly_rows_in_form_before': int((rows['friendlies_in_form_before_home']
                                                + rows['friendlies_in_form_before_away']).sum())}
    if len(changed):
        move = changed['move_1x2'] * 100
        largest = changed.loc[changed['move_1x2'].idxmax()]
        out.update({
            'move_1x2_points': {'mean': float(move.mean()), 'median': float(move.median()),
                                'p90': float(move.quantile(.9)), 'max': float(move.max()),
                                'two_points_or_more': int((move >= 2).sum())},
            'largest': f"{largest['home_team']} v {largest['away_team']} ({largest['league']})",
            'move_over_1_5_points': {'mean': float(changed['move_over_1_5'].mean() * 100),
                                     'max': float(changed['move_over_1_5'].max() * 100)},
            'move_goal_rates': {'mean': float(changed['move_goal_rates'].mean()),
                                'max': float(changed['move_goal_rates'].max())},
            'mean_direction_points': {o: float((changed[f'p_{o}_after'] - changed[f'p_{o}_before']).mean() * 100)
                                      for o in OUTCOMES}})
    return out


def check_before_against_parity(frame) -> dict:
    """'before' on the latest forecast of each fixture must equal PR #145's current-rule ('live') probabilities."""
    if not PARITY_CSV.exists():
        return {'checked': 0}
    parity = pd.read_csv(PARITY_CSV)
    key = ['league', 'home_team', 'away_team', 'kickoff_utc']
    latest = frame.loc[frame['latest_forecast_of_fixture']]
    both = latest.merge(parity[key + [f'p_{o}_live' for o in OUTCOMES]], on=key, how='inner')
    diff = pd.concat([(both[f'p_{o}_before'] - both[f'p_{o}_live']).abs() for o in OUTCOMES], axis=1).max(axis=1)
    return {'checked': int(len(both)), 'max_abs_diff': float(diff.max()) if len(both) else None,
            'within_csv_rounding_1e-6': int((diff <= 1e-6).sum())}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('--root', type=Path, default=REPO / 'football_output_v2')
    parser.add_argument('--cache', type=Path, default=REPO / '.football_cache')
    parser.add_argument('--labels', type=Path, default=LABELS)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--fetch-espn', action='store_true', help='fetch missing ESPN competition labels first')
    args = parser.parse_args(argv)
    import team_research as tr
    names = load_script('replay_research_history_names')
    parity = load_script('research_parity_latest_rule')
    with warnings.catch_warnings():
        warnings.simplefilter('ignore')
        if args.fetch_espn:
            parity.fetch_labels(needed_labels(args.root, tr, parity), args.labels)
        labels = json.loads(args.labels.read_text(encoding='utf-8'))
        histories = names.Histories(pd.Timestamp.now(tz='UTC').to_pydatetime(), str(args.cache))
        frame, counts, worst = replay(args.root, labels, histories)
    latest = frame.loc[frame['latest_forecast_of_fixture']]
    summary = {
        'before_version': tr.V3_VERSION, 'after_version': tr.V4_VERSION, 'counts': dict(sorted(counts.items())),
        'frozen_probabilities_max_abs_diff': worst, 'history_errors': histories.errors,
        'before_matches_parity_report': check_before_against_parity(frame),
        'all_forecasts': {'forecasts': int(len(frame)), 'changed': int(frame['changed'].sum())},
        'latest_forecast_per_fixture': {'all': movement(latest),
                                        **{g: movement(latest.loc[latest['group'].eq(g)])
                                           for g in ('five_leagues', 'holdout_leagues', 'europa')}},
        'note': ('Probabilities only: no result and no odds field is read. Holdout leagues (Eredivisie, Primeira '
                 'Liga, Super Lig) are reported apart. Moves are the largest of the three 1X2 probabilities, in points.')}
    args.output.mkdir(parents=True, exist_ok=True)
    (args.output / 'summary.json').write_text(json.dumps(summary, indent=2, sort_keys=True, default=str) + '\n',
                                              encoding='utf-8')
    frame.to_csv(args.output / 'forecasts.csv', index=False, lineterminator='\n', float_format='%.6f')
    print(json.dumps(summary, indent=1, default=str))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
