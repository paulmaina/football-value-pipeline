"""Live replay for research v5 (C6): every saved forecast recomputed under v4 and v5, and each run's lists rebuilt.

Integration check for the release of C6 as research v5 (docs/plan.md, Paul's exception of 14 Nov 2026), not
evidence that it improves anything: no result is read.

For every saved run generated in [--start, --end):

  frozen  each forecast with research is replayed under the version it was frozen with and must reproduce its
          stored numbers (old forecasts replay unchanged under their own version).
  before  research v4, the live rule until now, on the forecast's frozen inputs brought up to the current rule as
          the v4 replay did (scripts/replay_research_friendlies.py: renamed domestic sides' history rebuilt, ESPN
          rows labelled with their competition).
  after   the live rule after this change on the same inputs: v5 (C6, fit from research_c6_fits.json for the
          research day) for domestic leagues, v4 for UCL/UEL. v5's shadow must equal `before`.

Then each run's decision rows are rebuilt twice from its frozen predictions at the run's own clock, once with
`before` and once with `after` research, exactly as scripts/master_reconciliation_replay.py does
(price_edge_cagey_shortlist.build_shortlist, master_shortlist.refresh), and the value shortlist and the new
master's picks and labels are compared. Holdout leagues are reported apart.

    python scripts/replay_research_c6.py --output evaluation/research_c6_replay
"""
from __future__ import annotations

import argparse
from collections import Counter
import copy
import json
from pathlib import Path
import sys
import tempfile
import warnings

import pandas as pd

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO))
OUTCOMES = ('home', 'draw', 'away')
TOLERANCE = 1e-12
RECOMPUTED = ('version', 'form', 'goal_rates', 'base_rates', 'margin_distribution', 'p_over_1_5', 'c6_fit',
              'shadow_v4', 'form_friendlies_excluded')
PICK_KEY = ['league', 'home_team', 'away_team', 'kickoff_utc', 'market']


def load_script(name):
    import importlib.util
    spec = importlib.util.spec_from_file_location(name, REPO / 'scripts' / f'{name}.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def research_columns(context) -> dict:
    import team_research as tr
    return tr.outcome_columns(context, 'research_p_')


def merged(frozen, recomputed) -> dict:
    """The frozen research context with its numbers replaced by a recomputation (evidence and reviews kept)."""
    out = {k: v for k, v in frozen.items() if k not in RECOMPUTED}
    out.update({k: recomputed[k] for k in RECOMPUTED if k in recomputed})
    out['warnings'] = list(dict.fromkeys([*frozen.get('warnings', []), *recomputed.get('warnings', [])]))
    return out


def hda(context):
    import team_research as tr
    cols = tr.outcome_columns(context, '')
    return [cols[o] for o in OUTCOMES]


def recompute(root, start, end, labels, histories):
    """Per forecast: frozen check, v4 (before) and live (after). Returns (records, contexts, counts, worst)."""
    import evaluation_harness as eh
    import performance_tracking as pt
    import team_research as tr
    friendlies = load_script('replay_research_friendlies')
    names = load_script('replay_research_history_names')
    parity = load_script('research_parity_latest_rule')
    keys = names.league_keys()
    counts, records, contexts, worst = Counter(), [], {}, 0.
    for meta, rows, _ in pt.snapshots(root):
        generated = str(meta['generated_at_utc'])
        if not start <= generated[:10] < end:
            continue
        counts['runs'] += 1
        for index, row in enumerate(rows):
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
            again = tr.prepare(row, cutoff, copy.deepcopy(evidence), version=frozen_version,
                               c6_fit=research.get('c6_fit'))
            diff = max(abs(a - b) for a, b in zip(hda(research), hda(again)))
            worst = max(worst, diff)
            counts['frozen_not_reproduced'] += diff > TOLERANCE
            league = str(row.get('league'))
            league_key = keys.get(league)
            current = dict(row)
            if frozen_version in tr.FIXTURE_NAME_ONLY and league_key and league_key not in ('UEL', 'UCL'):
                history = histories(league_key)
                if history is not None and history.attrs:
                    history.attrs = {}
                if history is None:
                    counts['history_unavailable:' + league_key] += 1
                else:
                    rebuilt, _ = names.rebuilt_history(row, history, meta['generated_at_utc'], league_key, tr)
                    current['research_history_json'] = json.dumps(rebuilt, sort_keys=True)
            view, _ = friendlies.labelled_evidence(evidence, labels, tr.LEAGUES.get(league, ''), parity, tr)
            before = tr.prepare(current, cutoff, copy.deepcopy(view), version=tr.V4_VERSION)
            after = tr.prepare(current, cutoff, copy.deepcopy(view))
            if after['version'] in tr.C6_VERSIONS:
                shadow_gap = max(abs(a - b) for a, b in zip(hda(after['shadow_v4']), hda(before)))
                counts['shadow_not_v4'] += shadow_gap > TOLERANCE
                counts['c6_fit_origin:' + after['c6_fit']['origin']] += 1
                counts['c6_fit_stale'] += bool(after['c6_fit']['stale'])
            b, a = hda(before), hda(after)
            contexts[(meta['git_commit_sha'], index)] = (merged(research, before), merged(research, after))
            records.append({
                'snapshot': meta['git_commit_sha'], 'snapshot_generated_utc': generated,
                'league': league, 'group': friendlies.group_of(league), 'home_team': row.get('home_team'),
                'away_team': row.get('away_team'), 'kickoff_utc': str(row.get('kickoff_utc')),
                'research_observed_utc': cutoff.isoformat(), 'frozen_version': frozen_version,
                'frozen_reproduced_max_abs_diff': diff, 'after_version': after['version'],
                'c6_fit_origin': (after.get('c6_fit') or {}).get('origin'),
                **{f'p_{o}_before': v for o, v in zip(OUTCOMES, b)},
                **{f'p_{o}_after': v for o, v in zip(OUTCOMES, a)},
                'p_over_1_5_before': before.get('p_over_1_5'), 'p_over_1_5_after': after.get('p_over_1_5'),
                'move_1x2': max(abs(x - y) for x, y in zip(b, a)),
                'move_over_1_5': abs(before['p_over_1_5'] - after['p_over_1_5']),
                'goal_rates_identical': before['goal_rates'] == after['goal_rates']})
    frame = pd.DataFrame(records)
    if len(frame):
        key = ['league', 'home_team', 'away_team', 'kickoff_utc']
        frame['latest_forecast_of_fixture'] = frame['research_observed_utc'].eq(
            frame.groupby(key)['research_observed_utc'].transform('max'))
        frame['changed'] = frame['move_1x2'] > TOLERANCE
    return frame, contexts, counts, worst


def run_lists(directory, generated, predictions):
    """The run's value picks and new-master rows, rebuilt from these predictions at the run's clock."""
    import master_shortlist
    import narrow_margin as nm
    import price_edge_cagey_shortlist as v28
    from quote_policy import load_policy
    with warnings.catch_warnings(), tempfile.TemporaryDirectory() as tmp:
        warnings.simplefilter('ignore')
        _, decisions, summary = v28.build_shortlist(predictions, pd.Timestamp(generated),
                                                    execution_policy=load_policy(), model=nm.production_model())
        summary.setdefault('quote_execution_policy', load_policy())
        master_shortlist.refresh(decisions, Path(tmp), summary, predictions)
        new = Path(tmp) / 'master_shortlist_new.csv'
        new_master = pd.read_csv(new) if new.exists() else pd.DataFrame()
    value = decisions.loc[decisions['decision'].eq('SHORTLISTED')].copy()
    return value, new_master


def compare_lists(root, start, end, contexts):
    import performance_tracking as pt
    import team_research as tr
    master_replay = load_script('master_reconciliation_replay')
    runs, picks = [], []
    for generated, directory, _ in master_replay.runs(root, start, end):
        meta, _, _ = pt.load_snapshot(directory)
        predictions = pd.read_csv(directory / 'predictions.csv', low_memory=False)
        lists = {}
        for side, which in (('before', 0), ('after', 1)):
            frame = predictions.copy()
            for column in ('research_version', *(tr.SHADOW_PREFIX + k for k in (*OUTCOMES, 'over_1_5'))):
                frame[column] = None
            if 'team_research_json' not in frame:
                frame['team_research_json'] = None  # runs saved before research was collected
            frame = frame.astype({'team_research_json': object})
            for index in range(len(frame)):
                pair = contexts.get((meta['git_commit_sha'], index))
                if pair is None:
                    continue
                context = pair[which]
                frame.at[index, 'team_research_json'] = json.dumps(context, sort_keys=True, allow_nan=False)
                for column, value in research_columns(context).items():
                    frame.at[index, column] = value
                if 'shadow_v4' in context:
                    for column, value in tr.outcome_columns(context['shadow_v4'], tr.SHADOW_PREFIX).items():
                        frame.at[index, column] = value
                frame.at[index, 'research_version'] = context['version']
            lists[side] = run_lists(directory, generated, frame)
        runs.append(run_difference(directory.name, generated, lists))
        for side in ('before', 'after'):
            value = lists[side][0]
            for _, r in value.iterrows():
                picks.append({'snapshot': directory.name, 'side': side, **{k: r.get(k) for k in PICK_KEY},
                              'research_p_win': r.get('research_p_win'),
                              'profit_expected_return': r.get('profit_expected_return')})
    return runs, pd.DataFrame(picks)


def _keys(frame, columns=PICK_KEY):
    if frame is None or not len(frame):
        return set()
    return {tuple(str(r[c]) for c in columns) for _, r in frame[columns].iterrows()}


def run_difference(name, generated, lists) -> dict:
    (vb, nb), (va, na) = lists['before'], lists['after']
    out = {'snapshot': name, 'generated_at_utc': generated,
           'value_picks_before': len(vb), 'value_picks_after': len(va),
           'value_picks_added': len(_keys(va) - _keys(vb)), 'value_picks_removed': len(_keys(vb) - _keys(va))}
    if len(vb) and len(va):
        both = vb.merge(va, on=PICK_KEY, suffixes=('_b', '_a'))
        moves = (pd.to_numeric(both['research_p_win_a'], errors='coerce')
                 - pd.to_numeric(both['research_p_win_b'], errors='coerce')).abs()
        out.update(value_picks_same=int(len(both)), value_same_p_win_move_mean=float(moves.mean()) if len(both) else None,
                   value_same_p_win_move_max=float(moves.max()) if len(both) else None)
    offer = [c for c in ('league', 'home_team', 'away_team', 'kickoff_utc', 'market', 'bookmaker',
                         'offered_decimal_odds') if c in nb.columns and c in na.columns]
    if len(nb) and len(na) and offer:
        nb, na = nb.copy(), na.copy()
        for f in (nb, na):
            f['labels'] = f['new_master_labels'].fillna('')
        both = nb.merge(na, on=offer, suffixes=('_b', '_a'))
        ranked_b = nb.loc[nb['new_master_decision'].eq('SHORTLISTED')]
        ranked_a = na.loc[na['new_master_decision'].eq('SHORTLISTED')]
        changed = both.loc[both['labels_b'] != both['labels_a']]
        out.update(new_master_offers_before=int(len(nb)), new_master_offers_after=int(len(na)),
                   new_master_offers_matched=int(len(both)), new_master_label_changes=int(len(changed)),
                   new_master_label_change_kinds=dict(Counter(f"{b or '-'} -> {a or '-'}" for b, a in
                                                               zip(changed['labels_b'], changed['labels_a']))),
                   new_master_picks_before=int(len(ranked_b)), new_master_picks_after=int(len(ranked_a)),
                   new_master_picks_changed=len(_keys(ranked_b, offer) ^ _keys(ranked_a, offer)),
                   new_master_pick_label_changes=int(len(changed.loc[changed['new_master_decision_b'].eq('SHORTLISTED')
                                                                     | changed['new_master_decision_a'].eq('SHORTLISTED')])))
    return out


def movement(rows) -> dict:
    changed = rows.loc[rows['changed']] if len(rows) else rows
    out = {'fixtures': int(len(rows)), 'changed': int(len(changed))}
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
            'mean_direction_points': {o: float((changed[f'p_{o}_after'] - changed[f'p_{o}_before']).mean() * 100)
                                      for o in OUTCOMES},
            'home_favourite_more_likely': int(((changed['p_home_before'] > changed['p_away_before'])
                                               & (changed['p_home_after'] > changed['p_home_before'])).sum())})
    return out


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('--root', type=Path, default=REPO / 'football_output_v2')
    parser.add_argument('--cache', type=Path, default=REPO / '.football_cache')
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--start', default='2026-10-27')
    parser.add_argument('--end', default='2026-11-09', help='exclusive')
    parser.add_argument('--skip-lists', action='store_true')
    args = parser.parse_args(argv)
    import team_research as tr
    names = load_script('replay_research_history_names')
    friendlies = load_script('replay_research_friendlies')
    with warnings.catch_warnings():
        warnings.simplefilter('ignore')
        labels = json.loads(friendlies.LABELS.read_text(encoding='utf-8'))
        histories = names.Histories(pd.Timestamp.now(tz='UTC').to_pydatetime(), str(args.cache))
        frame, contexts, counts, worst = recompute(args.root, args.start, args.end, labels, histories)
    latest = frame.loc[frame['latest_forecast_of_fixture']]
    summary = {
        'before_version': tr.V4_VERSION, 'after_version': f'{tr.VERSION} (domestic), {tr.V4_VERSION} (UCL/UEL)',
        'window': [args.start, args.end], 'counts': dict(sorted(counts.items())),
        'frozen_probabilities_max_abs_diff': worst, 'history_errors': histories.errors,
        'all_forecasts': {'forecasts': int(len(frame)), 'changed': int(frame['changed'].sum()),
                          'european_changed': int(frame.loc[frame['group'].eq('europa'), 'changed'].sum()),
                          'goal_rates_identical': bool(frame['goal_rates_identical'].all())},
        'latest_forecast_per_fixture': {'all': movement(latest),
                                        **{g: movement(latest.loc[latest['group'].eq(g)])
                                           for g in ('five_leagues', 'holdout_leagues', 'europa')}},
        'note': ('Probabilities only: no result is read. Moves are the largest of the three 1X2 probabilities, '
                 'in points. Holdout leagues (Eredivisie, Primeira Liga, Super Lig) reported apart.')}
    args.output.mkdir(parents=True, exist_ok=True)
    frame.to_csv(args.output / 'forecasts.csv', index=False, lineterminator='\n', float_format='%.6f')
    if not args.skip_lists:
        runs, picks = compare_lists(args.root.parent, args.start, args.end, contexts)
        totals = Counter()
        kinds = Counter()
        for r in runs:
            for k, v in r.items():
                if isinstance(v, int) and not isinstance(v, bool):
                    totals[k] += v
            kinds.update(r.get('new_master_label_change_kinds', {}))
        summary['lists'] = {'runs': len(runs), 'totals': dict(sorted(totals.items())),
                            'new_master_label_change_kinds': dict(kinds.most_common()), 'per_run': runs}
        picks.to_csv(args.output / 'value_picks.csv', index=False, lineterminator='\n', float_format='%.6f')
    (args.output / 'summary.json').write_text(json.dumps(summary, indent=2, sort_keys=True, default=str) + '\n',
                                              encoding='utf-8')
    print(json.dumps({k: v for k, v in summary.items() if k != 'lists'}, indent=1, default=str))
    if 'lists' in summary:
        print(json.dumps(summary['lists']['totals'], indent=1))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
