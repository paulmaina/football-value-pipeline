"""Live replay for research v6 (CE3n, UCL/UEL): every saved forecast recomputed before and after, each run's lists rebuilt.

Integration check for the release of CE3n as research v6 (docs/plan.md, Paul's exception of 14 Nov 2026, "European
value picks"), not evidence that it improves anything: no result is read.

For every saved run generated in [--start, --end):

  frozen   each forecast with research is replayed under the version it was frozen with and must reproduce its
           stored numbers (old forecasts replay unchanged under their own version).
  before   the live rule until now (v5 domestic, v4 for UCL/UEL) on the forecast's frozen inputs brought up to the
           current rule as the v5 replay did (scripts/replay_research_c6.py: renamed domestic sides' history
           rebuilt, ESPN rows labelled with their competition).
  after    the live rule after this change on the same inputs: v6 (CE3n, the live fit for the research day,
           research_ce3n_live_fits.json: every result before the window, holdout periods included) for UCL/UEL,
           v5 for domestic leagues. Domestic contexts must be byte-identical to `before`; v6's CE shadow must
           equal `before` (CE is v4).
  tested   v6 on the harness's tested, holdout-free fit for the same window (research_ce3n_fits.json).

Forecasts saved without research (runs before research was collected) have no frozen research inputs; the value
shortlist prices them with the live rule on their frozen goal rates (profit_shortlist.context), so they are rebuilt
the same way here, before and after, and reported apart ("legacy").

Then each run's decision rows are rebuilt from its frozen predictions at the run's own clock with each side's
research (price_edge_cagey_shortlist.build_shortlist, master_shortlist.refresh under the live switch), and the value
shortlist, the live master (master_shortlist.csv) and the old master in shadow (master_shortlist_old.csv) are
compared: picks, labels and flags.

    python scripts/replay_research_ce3n.py --output evaluation/research_ce3n_replay
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
              'shadow_v4', 'form_friendlies_excluded', 'ce3n_fit', 'ce3n')
PICK_KEY = ['league', 'home_team', 'away_team', 'kickoff_utc', 'market']
OFFER = ['league', 'home_team', 'away_team', 'kickoff_utc', 'market', 'bookmaker', 'offered_decimal_odds']
SIDES = ('before', 'after', 'tested')
PAIRS = {'v4_to_v6': ('before', 'after'), 'v4_to_v6_tested_fit': ('before', 'tested'), 'fit_effect': ('tested', 'after')}
NEW_MASTER = {'file': 'master_shortlist.csv', 'decision': 'new_master_decision',
              'flags': ('new_master_labels', 'inspection_flag', 'unvalidated_view', 'new_master_tier')}
OLD_MASTER = {'file': 'master_shortlist_old.csv', 'decision': 'master_decision',
              'flags': ('master_price_flag', 'master_coverage_warning', 'master_validation_status')}
LEGACY_EVIDENCE = {'errors': ['research not collected for this forecast']}  # profit_shortlist.context's fallback


def load_script(name):
    import importlib.util
    spec = importlib.util.spec_from_file_location(name, REPO / 'scripts' / f'{name}.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def hda(context):
    import team_research as tr
    cols = tr.outcome_columns(context, '')
    return [cols[o] for o in OUTCOMES]


def merged(frozen, recomputed) -> dict:
    out = {k: v for k, v in frozen.items() if k not in RECOMPUTED}
    out.update({k: recomputed[k] for k in RECOMPUTED if k in recomputed})
    out['warnings'] = list(dict.fromkeys([*frozen.get('warnings', []), *recomputed.get('warnings', [])]))
    return out


def dumps(context) -> str:
    return json.dumps(context, sort_keys=True, allow_nan=False, default=str)


def recompute(root, start, end, labels, histories):
    """Per forecast: frozen check, before, after and tested. Returns (records, contexts, counts, worst)."""
    import evaluation_harness as eh
    import performance_tracking as pt
    import research_ce3n as ce3n
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
            league = str(row.get('league'))
            european = league in tr.EUROPEAN_COMPETITIONS
            research = tr.decode(row.get('team_research_json'))
            legacy = not research
            current = dict(row)
            if legacy:
                # profit_shortlist.context prices a forecast without research with the live rule at the run's clock.
                counts['legacy_' + ('european' if european else 'domestic')] += 1
                cutoff = tr.utc(generated)
                view = copy.deepcopy(LEGACY_EVIDENCE)
                frozen_version, diff = None, 0.
            elif not research.get('margin_distribution'):
                counts['research_without_probabilities'] += 1
                continue
            else:
                counts['with_research'] += 1
                cutoff = tr.utc(research.get('observed_at_utc'))
                evidence = copy.deepcopy(research.get('evidence', {}))
                for key in eh.DERIVED_EVIDENCE:
                    evidence.pop(key, None)
                frozen_version = research.get('version', tr.LEGACY_VERSION)
                counts['frozen:' + frozen_version] += 1
                again = tr.prepare(row, cutoff, copy.deepcopy(evidence), version=frozen_version,
                                   c6_fit=research.get('c6_fit'), ce3n_fit=research.get('ce3n_fit'))
                diff = max(abs(a - b) for a, b in zip(hda(research), hda(again)))
                worst = max(worst, diff)
                counts['frozen_not_reproduced'] += diff > TOLERANCE
                league_key = keys.get(league)
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
            before = tr.prepare(current, cutoff, copy.deepcopy(view), version=tr.VERSION)  # v5; UCL/UEL v4
            after = tr.prepare(current, cutoff, copy.deepcopy(view))
            tested = after
            record = {'snapshot': meta['git_commit_sha'], 'snapshot_generated_utc': generated, 'league': league,
                      'group': 'european' if european else 'domestic', 'legacy': legacy,
                      'home_team': row.get('home_team'), 'away_team': row.get('away_team'),
                      'kickoff_utc': str(row.get('kickoff_utc')), 'research_observed_utc': cutoff.isoformat(),
                      'frozen_version': frozen_version, 'frozen_reproduced_max_abs_diff': diff,
                      'before_version': before['version'], 'after_version': after['version']}
            if not european:
                same = dumps(before) == dumps(after)
                counts['domestic_identical'] += same
                counts['domestic_changed'] += not same
            else:
                fit = after.get('ce3n_fit')
                if not after.get('margin_distribution') or not fit:
                    counts['european_without_v6'] += 1
                    record['v6_warnings'] = '; '.join(w for w in after.get('warnings', []) if 'CE3n' in w)
                else:
                    ce_gap = max(abs(a - b) for a, b in zip(hda(after['shadow_v4']), hda(before)))
                    counts['ce_shadow_not_v4'] += ce_gap > TOLERANCE
                    counts['ce_rates_not_v4'] += after['ce3n']['ce_goal_rates'] != before['goal_rates']
                    counts['live_fit_origin:' + fit['origin']] += 1
                    counts['live_fit_stale'] += bool(fit['stale'])
                    counts['domestic_used'] += bool(after['ce3n']['domestic_used'])
                    sides = {s: (row.get(s + '_team'), fit[s]['european_name']) for s in ('home', 'away')}
                    fit_t = ce3n.fit_for(cutoff, league, *sides.values(), path=ce3n.HARNESS_FITS)
                    tested = tr.prepare(current, cutoff, copy.deepcopy(view), ce3n_fit=fit_t)
                    counts['tested_fit_origin:' + fit_t['origin']] += 1
                    record.update(
                        live_fit_origin=fit['origin'], tested_fit_origin=fit_t['origin'],
                        domestic_used=after['ce3n']['domestic_used'],
                        domestic_used_tested=tested['ce3n']['domestic_used'],
                        home_league=fit['home']['league'], away_league=fit['away']['league'],
                        home_european_name=fit['home']['european_name'],
                        away_european_name=fit['away']['european_name'],
                        **{f'goal_rate_{s}_{k}': c['goal_rates'][i] for k, c in
                           (('before', before), ('after', after), ('tested', tested)) for i, s in enumerate(('home', 'away'))})
                b, a, t = hda(before), hda(after), (hda(tested) if tested.get('margin_distribution') else hda(after))
                record.update({**{f'p_{o}_before': v for o, v in zip(OUTCOMES, b)},
                               **{f'p_{o}_after': v for o, v in zip(OUTCOMES, a)},
                               **{f'p_{o}_tested': v for o, v in zip(OUTCOMES, t)},
                               'p_over_1_5_before': before.get('p_over_1_5'), 'p_over_1_5_after': after.get('p_over_1_5'),
                               'p_over_1_5_tested': tested.get('p_over_1_5'),
                               'move_1x2': max(abs(x - y) for x, y in zip(b, a)),
                               'move_1x2_tested': max(abs(x - y) for x, y in zip(b, t)),
                               'fit_effect_1x2': max(abs(x - y) for x, y in zip(t, a))})
            if legacy:  # exactly the context profit_shortlist.context would make at the run's clock
                contexts[(meta['git_commit_sha'], index)] = (before, after, tested)
            else:
                contexts[(meta['git_commit_sha'], index)] = (merged(research, before), merged(research, after),
                                                             merged(research, tested))
            records.append(record)
    frame = pd.DataFrame(records)
    if len(frame):
        key = ['league', 'home_team', 'away_team', 'kickoff_utc']
        frame['latest_forecast_of_fixture'] = frame['research_observed_utc'].eq(
            frame.groupby(key)['research_observed_utc'].transform('max'))
        for col, src in (('changed', 'move_1x2'), ('changed_tested', 'move_1x2_tested'),
                         ('changed_fit_effect', 'fit_effect_1x2')):
            frame[col] = frame[src].fillna(0) > TOLERANCE if src in frame else False
    return frame, contexts, counts, worst


def run_lists(directory, generated, predictions):
    """The run's value picks, live master and old master (shadow), rebuilt from these predictions at the run's
    clock under the live master switch."""
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
        masters = {}
        for name, spec in (('live_master', NEW_MASTER), ('old_master', OLD_MASTER)):
            path = Path(tmp) / spec['file']
            masters[name] = pd.read_csv(path, low_memory=False) if path.exists() else pd.DataFrame()
    value = decisions.loc[decisions['decision'].eq('SHORTLISTED')].copy()
    return value, masters


def _keys(frame, columns):
    if frame is None or not len(frame):
        return set()
    return {tuple(str(r[c]) for c in columns) for _, r in frame[columns].iterrows()}


def _european(frame):
    import team_research as tr
    return frame.loc[frame['league'].astype(str).isin(tr.EUROPEAN_COMPETITIONS)] if len(frame) else frame


def master_difference(before, after, spec) -> dict:
    out = {'offers_before': int(len(before)), 'offers_after': int(len(after))}
    offer = [c for c in OFFER if c in before.columns and c in after.columns]
    if not (len(before) and len(after) and offer):
        return out
    picks_b = before.loc[before[spec['decision']].eq('SHORTLISTED')]
    picks_a = after.loc[after[spec['decision']].eq('SHORTLISTED')]
    flags = [c for c in spec['flags'] if c in before.columns and c in after.columns]
    both = before.merge(after, on=offer, suffixes=('_b', '_a'))
    kinds, changed_offers, changed_picks = Counter(), 0, 0
    for _, r in both.iterrows():
        diffs = [f"{c}: {'' if pd.isna(r[c + '_b']) else r[c + '_b']} -> {'' if pd.isna(r[c + '_a']) else r[c + '_a']}"
                 for c in flags if str(r[c + '_b']) != str(r[c + '_a'])]
        if diffs:
            changed_offers += 1
            changed_picks += 'SHORTLISTED' in (r[spec['decision'] + '_b'], r[spec['decision'] + '_a'])
            kinds.update(diffs)
    eu_b, eu_a = _european(picks_b), _european(picks_a)
    out.update(picks_before=int(len(picks_b)), picks_after=int(len(picks_a)),
               picks_changed=len(_keys(picks_b, offer) ^ _keys(picks_a, offer)),
               european_picks_before=int(len(eu_b)), european_picks_after=int(len(eu_a)),
               european_picks_changed=len(_keys(eu_b, offer) ^ _keys(eu_a, offer)),
               offers_matched=int(len(both)), flag_changes=changed_offers, flag_changes_on_picks=changed_picks,
               flag_change_kinds=dict(kinds))
    if 'unvalidated_view' in after.columns:
        european = _european(after)
        out.update(european_offers_after=int(len(european)),
                   european_offers_not_flagged_unvalidated=int((~european['unvalidated_view'].astype(str)
                                                                 .str.lower().eq('true')).sum()))
    return out


def run_difference(name, generated, before, after) -> dict:
    (vb, mb), (va, ma) = before, after
    out = {'snapshot': name, 'generated_at_utc': generated,
           'value_picks_before': len(vb), 'value_picks_after': len(va),
           'value_picks_added': len(_keys(va, PICK_KEY) - _keys(vb, PICK_KEY)),
           'value_picks_removed': len(_keys(vb, PICK_KEY) - _keys(va, PICK_KEY)),
           'european_value_picks_before': len(_european(vb)), 'european_value_picks_after': len(_european(va)),
           'european_value_picks_added': len(_keys(_european(va), PICK_KEY) - _keys(_european(vb), PICK_KEY)),
           'european_value_picks_removed': len(_keys(_european(vb), PICK_KEY) - _keys(_european(va), PICK_KEY)),
           'domestic_value_picks_changed': len(_keys(vb.loc[~vb.index.isin(_european(vb).index)], PICK_KEY)
                                               ^ _keys(va.loc[~va.index.isin(_european(va).index)], PICK_KEY))}
    if len(vb) and len(va):
        both = _european(vb).merge(_european(va), on=PICK_KEY, suffixes=('_b', '_a'))
        moves = (pd.to_numeric(both['research_p_win_a'], errors='coerce')
                 - pd.to_numeric(both['research_p_win_b'], errors='coerce')).abs()
        out.update(european_value_picks_same=int(len(both)),
                   european_same_p_win_move_mean=float(moves.mean()) if len(both) else None,
                   european_same_p_win_move_max=float(moves.max()) if len(both) else None)
    for name_, spec in (('live_master', NEW_MASTER), ('old_master', OLD_MASTER)):
        out[name_] = master_difference(mb[name_], ma[name_], spec)
    return out


def compare_lists(root, start, end, contexts):
    import performance_tracking as pt
    import team_research as tr
    master_replay = load_script('master_reconciliation_replay')
    runs, picks = {name: [] for name in PAIRS}, []
    for generated, directory, _ in master_replay.runs(root, start, end):
        meta, _, _ = pt.load_snapshot(directory)
        predictions = pd.read_csv(directory / 'predictions.csv', low_memory=False)
        lists = {}
        for which, side in enumerate(SIDES):
            frame = predictions.copy()
            for column in ('research_version', *(tr.SHADOW_PREFIX + k for k in (*OUTCOMES, 'over_1_5'))):
                frame[column] = None
            if 'team_research_json' not in frame:
                frame['team_research_json'] = None
            frame = frame.astype({'team_research_json': object})
            for index in range(len(frame)):
                pair = contexts.get((meta['git_commit_sha'], index))
                if pair is None:
                    continue
                context = pair[which]
                frame.at[index, 'team_research_json'] = json.dumps(context, sort_keys=True, allow_nan=False)
                for column, value in tr.outcome_columns(context, 'research_p_').items():
                    frame.at[index, column] = value
                if 'shadow_v4' in context:
                    for column, value in tr.outcome_columns(context['shadow_v4'], tr.SHADOW_PREFIX).items():
                        frame.at[index, column] = value
                frame.at[index, 'research_version'] = context['version']
            lists[side] = run_lists(directory, generated, frame)
        for name, (b, a) in PAIRS.items():
            runs[name].append(run_difference(directory.name, generated, lists[b], lists[a]))
        for side in SIDES:
            for _, r in lists[side][0].iterrows():
                picks.append({'snapshot': directory.name, 'side': side, **{k: r.get(k) for k in PICK_KEY},
                              'research_p_win': r.get('research_p_win'),
                              'profit_expected_return': r.get('profit_expected_return')})
    return runs, pd.DataFrame(picks)


def movement(rows, before='before', after='after', move='move_1x2', flag='changed') -> dict:
    changed = rows.loc[rows[flag]] if len(rows) else rows
    out = {'fixtures': int(len(rows)), 'changed': int(len(changed))}
    if len(changed):
        largest = changed.loc[changed[move].idxmax()]
        points = changed[move] * 100
        out.update({'move_1x2_points': {'mean': float(points.mean()), 'median': float(points.median()),
                                        'p90': float(points.quantile(.9)), 'max': float(points.max()),
                                        'two_points_or_more': int((points >= 2).sum())},
                    'largest': f"{largest['home_team']} v {largest['away_team']} ({largest['league']})",
                    'mean_direction_points': {o: float((changed[f'p_{o}_{after}'] - changed[f'p_{o}_{before}']).mean() * 100)
                                              for o in OUTCOMES}})
    return out


MOVES = {'v4_to_v6': {}, 'v4_to_v6_tested_fit': {'after': 'tested', 'move': 'move_1x2_tested', 'flag': 'changed_tested'},
         'fit_effect': {'before': 'tested', 'move': 'fit_effect_1x2', 'flag': 'changed_fit_effect'}}


def totals(per_run) -> dict:
    out, kinds = Counter(), {'live_master': Counter(), 'old_master': Counter()}
    for r in per_run:
        for k, v in r.items():
            if isinstance(v, int) and not isinstance(v, bool):
                out[k] += v
            elif isinstance(v, dict) and k in kinds:
                for kk, vv in v.items():
                    if isinstance(vv, int) and not isinstance(vv, bool):
                        out[f'{k}.{kk}'] += vv
                kinds[k].update(v.get('flag_change_kinds', {}))
    return {'totals': dict(sorted(out.items())), 'flag_change_kinds': {k: dict(v.most_common()) for k, v in kinds.items()}}


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
    european = frame.loc[frame['group'].eq('european')]
    latest = european.loc[european['latest_forecast_of_fixture']]
    summary = {
        'before_version': f'{tr.VERSION} (domestic), {tr.V4_VERSION} (UCL/UEL)',
        'after_version': f'{tr.VERSION} (domestic), {tr.CE3N_VERSION} (UCL/UEL)',
        'window': [args.start, args.end], 'counts': dict(sorted(counts.items())),
        'frozen_probabilities_max_abs_diff': worst, 'history_errors': histories.errors,
        'european_with_research': {name: {'all': movement(latest.loc[~latest['legacy']], **kw),
                                          **{c: movement(latest.loc[~latest['legacy'] & latest['league'].eq(c)], **kw)
                                             for c in sorted(tr.EUROPEAN_COMPETITIONS)}}
                                   for name, kw in MOVES.items()},
        'european_legacy_without_research': {name: movement(latest.loc[latest['legacy']], **kw)
                                             for name, kw in MOVES.items()},
        'note': ('Probabilities only: no result is read. Moves are the largest of the three 1X2 probabilities, in '
                 'points, latest forecast per fixture. v4_to_v6: CE (v4) to CE3n on the live fit (holdout periods '
                 "included); v4_to_v6_tested_fit: on the harness's tested, holdout-free fit; fit_effect: tested fit to "
                 'live fit. Legacy: forecasts saved without research, priced by the value shortlist with the live '
                 'rule on their frozen goal rates and no form.')}
    args.output.mkdir(parents=True, exist_ok=True)
    frame.to_csv(args.output / 'forecasts.csv', index=False, lineterminator='\n', float_format='%.6f')
    if not args.skip_lists:
        runs, picks = compare_lists(args.root.parent, args.start, args.end, contexts)
        summary['lists'] = {name: {'from_to': PAIRS[name], 'runs': len(per_run), **totals(per_run), 'per_run': per_run}
                            for name, per_run in runs.items()}
        picks.to_csv(args.output / 'value_picks.csv', index=False, lineterminator='\n', float_format='%.6f')
    (args.output / 'summary.json').write_text(json.dumps(summary, indent=2, sort_keys=True, default=str) + '\n',
                                              encoding='utf-8')
    print(json.dumps({k: v for k, v in summary.items() if k != 'lists'}, indent=1, default=str))
    if 'lists' in summary:
        print(json.dumps({name: v['totals'] for name, v in summary['lists'].items()}, indent=1))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
