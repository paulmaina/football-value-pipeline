"""Research parity under the latest research rule, with the gap split by where ESPN form games come from.

The parity report (`evaluation_harness.py --mode parity`) compares each fixture's
frozen live research probabilities with the harness's. Every saved forecast is
research v1, so this script first applies the current rule (team_research.VERSION):
each forecast is recomputed from its own frozen inputs, and a side whose fixture
and training names differ gets its training history rebuilt as in
scripts/replay_research_history_names.py (football-data.co.uk files, cut to dates
before the run day). The v3 probabilities are checked against the committed replay
(evaluation/research_fixture_name_replay/forecasts.csv).

Each ESPN result the live last-ten form uses is labelled with the competition ESPN
files it under (the event's league slug in the team's all-competitions schedule):
league, domestic cup, other domestic (super cups, play-offs), European, friendly or
unknown. "Other domestic" also holds a promoted team's lower-division league games. The live research is then recomputed without the cup rows, without the
European rows, without both and without every non-league row, and each version is
compared with the harness. Cup and European shares of the gap are Shapley values
over those four versions (they add up to the gap the two remove together).

Probabilities only: no result is scored and no odds field is read. The harness side
uses holdout-free history (as in evaluation_harness.research_parity), and the holdout
leagues are reported apart.

    python scripts/research_parity_latest_rule.py --fetch-espn --output evaluation/research_parity_latest_rule
    python scripts/research_parity_latest_rule.py --output evaluation/research_parity_latest_rule
"""
from __future__ import annotations

import argparse
from collections import Counter
import copy
import importlib.util
import json
from pathlib import Path
import sys
import time
import warnings

import pandas as pd

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO))
SIDES = ('home', 'away')
OUTCOMES = ('home', 'draw', 'away')
EUROPEAN_LEAGUES = ('UEFA Champions League', 'UEFA Europa League')
FIVE_LEAGUES = ('Premier League', 'La Liga', 'Bundesliga', 'Serie A', 'Ligue 1')
CLASSES = ('league', 'domestic_cup', 'domestic_other', 'european', 'friendly', 'unknown')
SCENARIOS = {  # name: ESPN row classes removed from the live form
    'live': (), 'no_cup': ('domestic_cup',), 'no_european': ('european',),
    'no_cup_no_european': ('domestic_cup', 'european'),
    'league_only': ('domestic_cup', 'domestic_other', 'european', 'friendly', 'unknown')}
ESPN_SCHEDULE = 'https://site.api.espn.com/apis/site/v2/sports/soccer/all/teams/{}/schedule'
REPLAY_CSV = REPO / 'evaluation' / 'research_fixture_name_replay' / 'forecasts.csv'


def load_script(name):
    spec = importlib.util.spec_from_file_location(name, REPO / 'scripts' / f'{name}.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


# ---------------------------------------------------------------------------
# ESPN competition labels
# ---------------------------------------------------------------------------

def season_of(date) -> int:
    return date.year if date.month >= 7 else date.year - 1


def team_id(source) -> str | None:
    parts = str(source or '').split('/teams/')
    return parts[1].split('/')[0] if len(parts) == 2 and '/schedule' in parts[1] else None


def compact_events(payload) -> list[dict]:
    """The fields needed to label a result: day, ESPN league slug, names and score."""
    out = []
    for e in payload.get('events') or []:
        comp = (e.get('competitions') or [{}])[0]
        sides = {c.get('homeAway'): c for c in comp.get('competitors') or []}
        if set(sides) != {'home', 'away'}:
            continue
        score = lambda c: (c.get('score') or {}).get('value') if isinstance(c.get('score'), dict) else c.get('score')
        out.append({'date': e.get('date'), 'league': (e.get('league') or {}).get('slug'),
                    'league_name': (e.get('league') or {}).get('name'),
                    'home': sides['home'].get('team', {}).get('displayName'),
                    'away': sides['away'].get('team', {}).get('displayName'),
                    'home_goals': score(sides['home']), 'away_goals': score(sides['away'])})
    return out


def fetch_labels(needed, path, session=None):
    """ESPN all-competitions schedules for each (team id, season); one public request each, cached in `path`."""
    import requests
    session = session or requests.Session()
    labels = json.loads(path.read_text(encoding='utf-8')) if path.exists() else {}
    for tid, season in sorted(needed):
        key = f'{tid}/{season}'
        if key in labels:
            continue
        response = session.get(ESPN_SCHEDULE.format(tid), params={'season': season}, timeout=30)
        response.raise_for_status()
        labels[key] = compact_events(response.json())
        time.sleep(.2)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(labels, indent=1, sort_keys=True, ensure_ascii=False) + '\n', encoding='utf-8')
    return labels


def classify(row, labels, league_slug, tr) -> tuple[str, str | None]:
    """(class, ESPN slug) of one ESPN result, found by team id, day (+/- 1) and score."""
    tid, date = team_id(row.get('source')), tr.utc(row.get('date'))
    events = labels.get(f'{tid}/{season_of(date)}', []) + labels.get(f'{tid}/{season_of(date) - 1}', [])
    goals = (float(row['home_goals']), float(row['away_goals']))
    found = [e for e in events if e.get('home_goals') is not None and e.get('away_goals') is not None
             and (float(e['home_goals']), float(e['away_goals'])) == goals
             and abs((tr.utc(e['date']) - date).total_seconds()) <= 36 * 3600]
    exact = [e for e in found if tr.utc(e['date']) == date]
    found = exact or found
    slugs = {e['league'] for e in found}
    if len(slugs) != 1:
        return 'unknown', None
    slug = slugs.pop() or ''
    if slug.startswith('uefa.'):
        return 'european', slug
    if any(k in slug for k in ('friendly', 'gamper', 'trophy')):  # e.g. club.friendly, esp.joan_gamper
        return 'friendly', slug
    if slug == league_slug or (league_slug.startswith('uefa.') and slug.endswith('.1')):
        return 'league', slug  # for a European fixture, any domestic top flight is the team's league
    country = slug.split('.')[0] if league_slug.startswith('uefa.') else league_slug.split('.')[0]
    if slug.split('.')[0] == country:
        cup = any(k in slug for k in ('cup', 'copa', 'pokal', 'coppa', 'coupe', 'taca', 'fa', 'beker', 'kupa', 'cis'))
        other = any(k in slug for k in ('super', 'charity', 'playoff', 'promotion', 'relegation'))
        return ('domestic_cup' if cup and not other else 'domestic_other'), slug
    return 'unknown', slug


# ---------------------------------------------------------------------------
# Live research under the current rule
# ---------------------------------------------------------------------------

def latest_forecasts(root, tr):
    import performance_tracking as pt
    latest = {}
    for meta, rows, _ in pt.snapshots(root):
        for row in rows:
            research = tr.decode(row.get('team_research_json'))
            stamp = tr.utc(research.get('observed_at_utc'))
            if not research.get('margin_distribution') or pd.isna(stamp):
                continue
            key = (str(row.get('league')), tr.name(row.get('home_team')), tr.name(row.get('away_team')),
                   str(row.get('kickoff_utc')))
            if key not in latest or stamp > latest[key][0]:
                latest[key] = (stamp, row, research, meta)
    return latest


def current_rule_row(row, meta, history, league_key, tr, replay):
    """The forecast row under the current rule: renamed sides rebuilt, everything else frozen."""
    research = tr.decode(row.get('team_research_json'))
    if research.get('version', tr.LEGACY_VERSION) not in tr.FIXTURE_NAME_ONLY or history is None:
        return dict(row), {}
    rebuilt, checks = replay.rebuilt_history(row, history, meta['generated_at_utc'], league_key, tr)
    return {**row, 'research_history_json': json.dumps(rebuilt, sort_keys=True)}, checks


def without(evidence, drop, labelled):
    """Evidence with the ESPN rows of the dropped classes removed (labelled: side -> [(row, class)])."""
    out = copy.deepcopy(evidence)
    if drop and isinstance(out.get('recent'), dict):
        for side in SIDES:
            if side in out['recent']:
                out['recent'][side] = [r for r, c in labelled.get(side, []) if c not in drop]
    return out


def hda(context):
    from evaluation_harness import _hda
    return _hda(context['margin_distribution'])


def gap(a, b):
    return max(abs(x - y) for x, y in zip(a, b))


def run(root, cache, cfg, labels):
    import evaluation_harness as eh
    import historical_benchmark as hb
    import team_research as tr
    from asian_handicap import margins as margin_json
    from football_value_pipeline_v2_standalone import DixonColesModel, FootballValuePipelineV2, LEAGUES
    replay = load_script('replay_research_history_names')
    keys = replay.league_keys()
    pipe = FootballValuePipelineV2(cache_dir=str(cache), odds_api_key='', football_data_api_key='', live_odds=False)
    now = pd.Timestamp.now(tz='UTC').to_pydatetime()
    live_histories, harness, models, records, coverage = {}, {}, {}, [], Counter()
    profile = cfg['production_v2']
    load_cfg = {**cfg, 'test_end_exclusive': cfg['end_exclusive']}
    for (league, *_), (stamp, row, research, meta) in sorted(latest_forecasts(root, tr).items()):
        league_key = keys.get(league)
        group = ('europa' if league in EUROPEAN_LEAGUES else
                 'holdout_leagues' if league_key in cfg['holdout_leagues'] else 'five_leagues')
        evidence = copy.deepcopy(research.get('evidence', {}))
        for k in eh.DERIVED_EVIDENCE:
            evidence.pop(k, None)
        history = None
        if league_key and league_key not in ('UEL', 'UCL'):
            if league_key not in live_histories:
                frame = pipe.source.history(LEAGUES[league_key], seasons_back=6, now=now)
                live_histories[league_key] = frame.assign(Date=pd.to_datetime(frame['Date'], utc=True))
            history = live_histories[league_key]
        current, checks = current_rule_row(row, meta, history, league_key, tr, replay)
        inputs = tr.research_inputs(current)
        # Label every ESPN row; prepare() drops all evidence when a source was observed after the cutoff.
        view = tr.research_evidence(evidence) if tr.observed_by(evidence, stamp) else {}
        slug = tr.LEAGUES.get(league)
        labelled = {s: [(r, classify(r, labels, slug, tr)[0]) for r in (evidence.get('recent') or {}).get(s, [])]
                    for s in SIDES}
        contexts = {name: tr.prepare(current, stamp, without(evidence, drop, labelled), version=tr.V4_VERSION) for name, drop in SCENARIOS.items()}
        frozen = eh._hda(research['margin_distribution'])
        record = {'league': league, 'group': group, 'home_team': row.get('home_team'), 'away_team': row.get('away_team'),
                  'kickoff_utc': str(row.get('kickoff_utc')), 'snapshot_generated_utc': meta.get('generated_at_utc'),
                  'research_observed_utc': stamp.isoformat(), 'frozen_version': research.get('version'),
                  'current_version': tr.V4_VERSION, 'evidence_used': bool(view),
                  'renamed_sides': sum(c.get('renamed', False) for c in checks.values()),
                  **{f'p_{o}_frozen': p for o, p in zip(OUTCOMES, frozen)},
                  **{f'p_{o}_{name}': p for name, c in contexts.items() for o, p in zip(OUTCOMES, hda(c))},
                  'frozen_to_current_1x2_move': gap(frozen, hda(contexts['live']))}
        # ESPN rows the live last-ten form actually keeps, by class.
        used = Counter(classify(r, labels, slug, tr)[0] for s in SIDES for r in eh._used_rows(inputs, evidence, stamp, s)
                       if r.get('source') != eh.TRAINING_HISTORY)
        record.update({f'espn_rows_used_{c}': used[c] for c in CLASSES})
        for name in SCENARIOS:
            record[f'{name}_vs_live_1x2'] = gap(hda(contexts[name]), hda(contexts['live']))
        if group == 'europa' or league_key is None:
            coverage['no_football_data_file:' + league] += 1
            records.append(record)
            continue
        if league_key not in harness:
            data, _, _ = hb.load_history(Path(cache), league_key, load_cfg)
            harness[league_key] = eh.training_rows(data, league_key, cfg, False)  # holdout-free
        train_all = harness[league_key]
        kickoff = tr.utc(row['kickoff_utc']).tz_convert(None).normalize()
        bounds = {b for w in eh.fold_windows(cfg, kickoff + pd.Timedelta(days=1)) for b in w}
        origin = max(b for b in bounds if b <= kickoff)
        if (league_key, origin) not in models:
            train = train_all.loc[train_all.Date < origin]
            models[(league_key, origin)] = (train, DixonColesModel(
                half_life_days=profile['half_life_days'], l2=cfg['baseline_l2'], max_goals=cfg['max_goals'],
                shot_features=profile['shot_features'], bbs_statistics=False).fit(train.copy(), as_of=origin))
        train, model = models[(league_key, origin)]
        teams = (row.get('model_home_team'), row.get('model_away_team'))
        if not all(t in model.teams for t in teams):
            coverage['harness_team_unresolved'] += 1
            records.append(record)
            continue
        matrix, _, info = eh.research_matrix(pd.Series({'HomeTeam': teams[0], 'AwayTeam': teams[1]}), train, origin, model)
        h = eh._hda(json.loads(margin_json(matrix)))
        # Live form without non-league games, on the harness's goal rates: what history alone leaves.
        on_harness_rates = tr.prepare({**current, 'lambda_home': info['lambda_home'], 'lambda_away': info['lambda_away']},
                                      stamp, without(evidence, SCENARIOS['league_only'], labelled), version=tr.V4_VERSION)
        record.update({'harness_compared': True, 'harness_origin': origin.date().isoformat(),
                       **{f'p_{o}_harness': p for o, p in zip(OUTCOMES, h)},
                       'gap_frozen': gap(h, frozen),
                       **{f'gap_{name}': gap(h, hda(c)) for name, c in contexts.items()},
                       'gap_league_only_harness_rates': gap(h, hda(on_harness_rates)),
                       'lambda_max_abs_diff': max(abs(float(row['lambda_home']) - info['lambda_home']),
                                                  abs(float(row['lambda_away']) - info['lambda_away']))})
        coverage['harness_compared'] += 1
        records.append(record)
    return pd.DataFrame(records), dict(coverage)


def check_against_replay(frame):
    """The current-rule live probabilities must equal the committed v3 replay ('after')."""
    replay = pd.read_csv(REPLAY_CSV)
    replay = replay.loc[replay['latest_forecast_of_fixture']]
    key = ['league', 'home_team', 'away_team', 'kickoff_utc']
    both = frame.merge(replay[key + [f'p_{o}_after' for o in OUTCOMES]], on=key, how='left')
    diff = pd.concat([(both[f'p_{o}_live'] - both[f'p_{o}_after']).abs() for o in OUTCOMES], axis=1).max(axis=1)
    return {'forecasts': int(len(both)), 'matched': int(diff.notna().sum()), 'max_abs_diff': float(diff.max()),
            # forecasts.csv stores probabilities to six decimals
            'reproduced_within_csv_rounding_1e-6': int((diff <= 1e-6).sum())}


def stats(values):
    values = values.dropna()
    return {'matches': int(len(values)), 'mean': float(values.mean()) if len(values) else None,
            'median': float(values.median()) if len(values) else None,
            'max': float(values.max()) if len(values) else None}


def summarize_group(rows) -> dict:
    out = {'forecasts': int(len(rows)), 'with_evidence': int(rows['evidence_used'].sum()) if len(rows) else 0,
           'espn_rows_used': {c: int(rows[f'espn_rows_used_{c}'].sum()) for c in CLASSES} if len(rows) else {},
           'forecasts_using': {c: int((rows[f'espn_rows_used_{c}'] > 0).sum()) for c in CLASSES} if len(rows) else {},
           'live_move_when_removed': {name: stats(rows[f'{name}_vs_live_1x2'])
                                      for name in SCENARIOS if name != 'live'} if len(rows) else {}}
    compared = rows.loc[rows.get('harness_compared', pd.Series(False, index=rows.index)).fillna(False).astype(bool)] \
        if len(rows) else rows
    if not len(compared):
        return out
    mean = {name: float(compared[f'gap_{name}'].mean()) for name in SCENARIOS}
    # Two-factor Shapley split of the mean gap the cup and European rows remove together.
    cup = ((mean['live'] - mean['no_cup']) + (mean['no_european'] - mean['no_cup_no_european'])) / 2
    european = ((mean['live'] - mean['no_european']) + (mean['no_cup'] - mean['no_cup_no_european'])) / 2
    out['harness_vs_live'] = {
        'compared': int(len(compared)),
        'gap_frozen_v1': stats(compared['gap_frozen']),
        **{f'gap_{name}': stats(compared[f'gap_{name}']) for name in SCENARIOS},
        'gap_league_only_on_harness_goal_rates': stats(compared['gap_league_only_harness_rates']),
        'lambda_max_abs_diff': stats(compared['lambda_max_abs_diff']),
        'mean_gap_split': {
            'total_current_rule': mean['live'],
            'domestic_cup': cup, 'european': european,
            'other_non_league (super cups, play-offs, friendlies, unknown)': mean['no_cup_no_european'] - mean['league_only'],
            'goal_rates': mean['league_only'] - float(compared['gap_league_only_harness_rates'].mean()),
            'remaining_history (window, staleness, ESPN league copies)': float(compared['gap_league_only_harness_rates'].mean())},
        'note': ('Mean of the per-forecast largest 1X2 gap, in probability (0.01 = 1 point). The split is sequential '
                 'except cup/European (Shapley); max-gap terms are not strictly additive per forecast.')}
    return out


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('--root', type=Path, default=REPO / 'football_output_v2')
    parser.add_argument('--cache', type=Path, default=REPO / '.football_cache')
    parser.add_argument('--config', type=Path, default=REPO / 'evaluation_harness_config.json')
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--fetch-espn', action='store_true', help='fetch missing ESPN competition labels first')
    args = parser.parse_args(argv)
    import team_research as tr
    cfg = json.loads(args.config.read_text(encoding='utf-8'))
    labels_path = args.output / 'espn_competitions.json'
    with warnings.catch_warnings():
        warnings.simplefilter('ignore')
        if args.fetch_espn:
            needed = set()
            for stamp, row, research, _ in latest_forecasts(args.root, tr).values():
                for rows in (research.get('evidence', {}).get('recent') or {}).values():
                    for r in rows:
                        if team_id(r.get('source')):
                            needed.add((team_id(r['source']), season_of(tr.utc(r['date']))))
            fetch_labels(needed, labels_path)
        labels = json.loads(labels_path.read_text(encoding='utf-8')) if labels_path.exists() else {}
        frame, coverage = run(args.root, args.cache, cfg, labels)
    summary = {'current_research_version': tr.V4_VERSION, 'coverage': coverage,
               'current_rule_check': check_against_replay(frame),
               'groups': {g: summarize_group(frame.loc[frame['group'].eq(g)])
                          for g in ('five_leagues', 'holdout_leagues', 'europa')},
               'by_league': {league: summarize_group(rows) for league, rows in frame.groupby('league')},
               'note': ('Probabilities only; no result is scored and no odds field is read. Harness fits use '
                        'holdout-free history, so the holdout leagues lack their 16 Jan - 10 Oct 2026 results '
                        'and are reported apart.')}
    args.output.mkdir(parents=True, exist_ok=True)
    (args.output / 'summary.json').write_text(json.dumps(summary, indent=2, sort_keys=True, default=str) + '\n',
                                              encoding='utf-8')
    frame.to_csv(args.output / 'forecasts.csv', index=False, lineterminator='\n', float_format='%.6f')
    print(json.dumps(summary['current_rule_check'], indent=1))
    print(json.dumps(summary['groups'], indent=1, default=str))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
