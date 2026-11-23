"""Research v6: CE3n live for UCL and UEL (docs/plan.md, Paul's exception of 14 Nov 2026, "European value picks").

CE3n exactly as the harness computes it (european_candidates' blend on CE's goal rates, the factors and domestic
strengths from the fit files, frozen per forecast), CE (v4) kept beside it in shadow, domestic leagues unchanged on
v5, older forecasts replaying under their own version, the fit files (tested, locked; live, holdout periods
included) and the monitoring that goes into the weekly report (rollback trigger, calibration slopes).
"""
from __future__ import annotations

import copy
import hashlib
import json
from collections import Counter
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import numpy as np
import pandas as pd

import european_candidates as ec
import evaluation_harness as eh
import research_backtest as rb
import research_ce3n as ce3n
import research_monitoring as rm
import team_research as tr
from asian_handicap import margins

REPO = Path(__file__).resolve().parents[1]
FIXTURE = json.loads((Path(__file__).with_name('fixtures') / 'frozen_forecast_row.json').read_text(encoding='utf-8'))
CFG = json.loads((REPO / 'evaluation_harness_config.json').read_text(encoding='utf-8'))
CUTOFF = pd.Timestamp('2026-11-04T12:00:00Z')
UCL = 'UEFA Champions League'
# The harness's locked CE3n fits (tested fit, reproduced from the locked European run): never rebuilt by the
# scheduled refresh, and unchanged by the live fit's inclusion of the holdout periods (Paul, 14 Nov 2026).
HARNESS_FITS_SHA256 = '0cec82f38eb95ea9e0b7f07e8069c3d294c64f0f4537c35385786a592e1b36b3'


def canonical(data) -> str:
    return hashlib.sha256(json.dumps({'windows': data['windows'], 'identities': data['identities']},
                                     sort_keys=True).encode()).hexdigest()


def clubs(path=ce3n.FITS, cutoff=CUTOFF, count=2):
    """European names of UCL clubs with a domestic strength in the window for `cutoff`, from different leagues."""
    data = ce3n.load_fits(path)
    day = cutoff.tz_convert(None).normalize()
    window = [w for w in data['windows'] if pd.Timestamp(w['origin']) <= day][-1]
    out, leagues = [], set()
    for name, (league, team) in sorted(data['identities'].items()):
        if league in leagues or team not in window['strengths'].get(league, {}):
            continue
        if name in ('FC Barcelona', 'FC Bayern München', 'Arsenal FC', 'FC Internazionale Milano',
                    'Paris Saint-Germain FC', 'PSV', 'SL Benfica', 'Galatasaray SK'):
            out.append(name)
            leagues.add(league)
        if len(out) == count:
            return out
    raise AssertionError('no clubs with domestic strengths in the fit window')


def european_row(home, away, league=UCL, frozen_names=True):
    """The frozen fixture row recast as a European match (history and evidence kept: only identities change)."""
    row = copy.deepcopy(FIXTURE['row'])
    research = json.loads(row['team_research_json'])
    evidence = research['evidence']
    for key in eh.DERIVED_EVIDENCE:
        evidence.pop(key, None)
    history = json.loads(row['research_history_json'])
    if frozen_names:
        history['teams'] = {'home': home, 'away': away}
    else:
        history.pop('teams', None)
    row.update(league=league, home_team=home, away_team=away, research_history_json=json.dumps(history))
    return row, evidence


def hda(context):
    cols = tr.outcome_columns(context, '')
    return [cols['home'], cols['draw'], cols['away']]


class FitFileTest(unittest.TestCase):
    def test_fit_files_hold_every_european_window_with_the_harness_settings(self):
        rule = {'test_start': CFG['european']['test_start'], 'step_days': CFG['european']['step_days'],
                'fixed_bounds': sorted({CFG['european'][k] for k in ('development_end', 'holdout_start',
                                                                       'holdout_end_exclusive')})}
        bounds = [o.date().isoformat() for o, _ in eh.fold_windows(CFG['european'], pd.Timestamp('2030-01-01'))]
        for path, version in ((ce3n.FITS, ce3n.FITS_VERSION), (ce3n.HARNESS_FITS, ce3n.HARNESS_FITS_VERSION)):
            data = ce3n.load_fits(path)
            self.assertEqual((data['version'], data['candidate_version']), (version, ce3n.VERSION))
            self.assertEqual((data['kind'], data['weight']), ('goals', ec.DOMESTIC_WEIGHT))
            self.assertEqual(data['fold_rule'], rule)
            origins = [w['origin'] for w in data['windows']]
            self.assertEqual(origins, sorted(origins))
            self.assertTrue(set(origins) <= set(bounds))
            fitted = [w for w in data['windows'] if w['factors']['status'] == 'fitted']
            self.assertTrue(fitted)
            self.assertTrue(all(set(w['factors']['s']) == set(CFG['leagues']) for w in fitted))
            live = [w for w in data['windows'] if w['origin'] >= data['strengths_from']]
            self.assertTrue(live and all(w.get('strengths') for w in live))
            self.assertFalse(any('strengths' in w for w in data['windows'] if w['origin'] < data['strengths_from']))
            # Identities link European training names to the eight leagues' clubs (reviewed aliases included).
            self.assertTrue(set(league for league, _ in data['identities'].values()) <= set(CFG['leagues']))
            self.assertIn('Galatasaray SK', data['identities'])  # a manual reviewed alias (12 Nov 2026 scope)

    def test_tested_fit_is_the_harness_run_exactly(self):
        data = ce3n.load_fits(ce3n.HARNESS_FITS)
        check = data['built_with']['harness_check']
        self.assertEqual((check['factor_max_abs_diff'], check['strength_max_abs_diff']), (0.0, 0.0))
        self.assertGreater(check['harness_windows_compared'], 100)
        self.assertEqual(data['built_with']['european_end_exclusive'], CFG['european']['end_exclusive'])

    def test_harness_fits_stay_locked(self):
        data = ce3n.load_fits(ce3n.HARNESS_FITS)
        self.assertEqual(canonical(data), HARNESS_FITS_SHA256)
        # Its last window is the locked development run's last factors (evaluation/european_candidates/summary.json).
        saved = json.loads((REPO / 'evaluation' / 'european_candidates' / 'summary.json').read_text(encoding='utf-8'))
        self.assertEqual(data['windows'][-1]['factors']['s'], saved['fits']['factors_last']['goals'])

    def test_live_fit_adds_the_holdout_periods_by_design(self):
        live, tested = ce3n.load_fits(), ce3n.load_fits(ce3n.HARNESS_FITS)
        self.assertEqual(live['basis'], 'live')
        self.assertTrue(live['built_with']['include_holdout'])
        self.assertGreater(live['built_with']['holdout_period_european_results'], 0)
        by_origin = {w['origin']: w for w in tested['windows']}
        start = CFG['european']['holdout_start']
        differs = 0
        for w in live['windows']:
            if w['origin'] not in by_origin:
                continue
            same = w['factors'] == by_origin[w['origin']]['factors']
            if w['origin'] <= start:  # no holdout result precedes it: the factors are identical
                self.assertTrue(same, w['origin'])
            differs += not same
        self.assertGreater(differs, 0)  # later windows learn from the holdout periods' results

    def test_fit_for_uses_the_latest_window_and_flags_a_stale_file(self):
        data = ce3n.load_fits()
        last = data['windows'][-1]
        home, away = clubs()
        stamp = pd.Timestamp(last['origin'] + 'T06:00:00Z')
        fit = ce3n.fit_for(stamp, UCL, ('x', home), ('y', away))
        self.assertEqual((fit['origin'], fit['stale'], fit['competition']), (last['origin'], False, 'UCL'))
        league, team = data['identities'][home]
        self.assertEqual(fit['home']['strength'], last['strengths'][league][team]['goals'])
        self.assertEqual(fit['factors'], last['factors'])
        late = ce3n.fit_for(stamp + pd.Timedelta(days=30), UCL, ('x', home), ('y', away))
        self.assertTrue(late['stale'])
        self.assertIsNone(ce3n.fit_for(pd.Timestamp(data['windows'][0]['origin'] + 'T00:00:00Z') - pd.Timedelta(days=1),
                                       UCL, ('x', home), ('y', away)))

    def test_expected_origin_matches_the_european_fold_windows(self):
        rule = ce3n.load_fits()['fold_rule']
        for day in pd.date_range('2016-01-01', '2026-11-14', freq='9D'):
            bounds = {b for w in eh.fold_windows(CFG['european'], day + pd.Timedelta(days=1)) for b in w}
            self.assertEqual(ce3n.expected_origin(day, rule), max(b for b in bounds if b <= day), day)


class LiveV6Test(unittest.TestCase):
    def test_ucl_v6_is_the_harness_ce3n_on_v4_goal_rates_with_ce_in_shadow(self):
        home, away = clubs()
        row, evidence = european_row(home, away)
        v6 = tr.prepare(row, CUTOFF, copy.deepcopy(evidence))
        v4 = tr.prepare(row, CUTOFF, copy.deepcopy(evidence), version=tr.V4_VERSION)
        self.assertEqual((v6['version'], v4['version']), (tr.CE3N_VERSION, tr.V4_VERSION))
        self.assertEqual(v6['ce3n']['ce_goal_rates'], v4['goal_rates'])
        self.assertEqual(v6['shadow_v4']['goal_rates'], v4['goal_rates'])
        self.assertEqual(v6['shadow_v4']['margin_distribution'], v4['margin_distribution'])
        self.assertEqual(v6['form'], v4['form'])
        self.assertTrue(v6['ce3n']['domestic_used'])
        fit = v6['ce3n_fit']
        self.assertEqual(fit, ce3n.fit_for(CUTOFF, UCL, (home, home), (away, away)))
        # The harness's own code (european_candidates.build's blend, european_candidate_records' grid).
        pair = {s: ({'goals': tuple(fit[s]['strength'])}, fit[s]['league']) for s in ('home', 'away')}
        rates = ec.blended_rates(v4['goal_rates'], ec.domestic_rates(pair, fit['factors'], 'UCL', 'goals'))
        self.assertEqual(v6['goal_rates'], rates)
        self.assertEqual(v6['margin_distribution'], json.loads(margins(rb.matrix_value(tr.research_grid(rates)))))
        self.assertEqual(v6['margin_distribution'], json.loads(margins(eh.ce3n_harness_matrix(v4['goal_rates'], fit))))
        self.assertNotEqual(v6['margin_distribution'], v4['margin_distribution'])

    def test_a_team_without_domestic_form_leaves_ce_exactly(self):
        home, _ = clubs()
        row, evidence = european_row(home, 'FK Bodø/Glimt')
        v6 = tr.prepare(row, CUTOFF, copy.deepcopy(evidence))
        v4 = tr.prepare(row, CUTOFF, copy.deepcopy(evidence), version=tr.V4_VERSION)
        self.assertFalse(v6['ce3n']['domestic_used'])
        self.assertIsNone(v6['ce3n_fit']['away']['strength'])
        self.assertEqual(v6['goal_rates'], v4['goal_rates'])
        self.assertEqual(v6['margin_distribution'], json.loads(margins(rb.matrix_value(tr.research_grid(v4['goal_rates'])))))
        self.assertTrue(any('CE3n equals CE' in w for w in v6['warnings']))

    def test_forecast_without_frozen_names_resolves_them_with_the_reviewed_resolver(self):
        home, away = clubs()
        row, evidence = european_row(home, away, frozen_names=False)
        v6 = tr.prepare(row, CUTOFF, copy.deepcopy(evidence))
        self.assertEqual((v6['ce3n_fit']['home']['european_name'], v6['ce3n_fit']['away']['european_name']), (home, away))

    def test_v6_replays_from_its_frozen_fit_without_the_fit_file(self):
        home, away = clubs()
        row, evidence = european_row(home, away)
        live = tr.prepare(row, CUTOFF, copy.deepcopy(evidence))
        with patch.object(ce3n, 'fit_for', side_effect=AssertionError('fit file read on replay')):
            again = tr.prepare(row, CUTOFF, copy.deepcopy(evidence), version=live['version'], ce3n_fit=live['ce3n_fit'])
        self.assertEqual(again['margin_distribution'], live['margin_distribution'])
        self.assertEqual(again['goal_rates'], live['goal_rates'])

    def test_no_fit_window_leaves_no_research_probabilities(self):
        home, away = clubs()
        row, evidence = european_row(home, away)
        with patch.object(ce3n, 'fit_for', return_value=None):
            context = tr.prepare(row, CUTOFF, copy.deepcopy(evidence))
        self.assertNotIn('margin_distribution', context)
        self.assertIn('shadow_v4', context)
        self.assertTrue(any('no CE3n fit window' in w for w in context['warnings']))

    def test_stale_fit_is_warned(self):
        home, away = clubs()
        row, evidence = european_row(home, away)
        last = pd.Timestamp(ce3n.load_fits()['windows'][-1]['origin']).tz_localize('UTC')
        context = tr.prepare(row, last + pd.Timedelta(days=30), {})
        self.assertTrue(any('CE3n fit is stale' in w for w in context['warnings']))

    def test_domestic_leagues_stay_v5_and_old_versions_replay_unchanged(self):
        row = copy.deepcopy(FIXTURE['row'])
        research = json.loads(row['team_research_json'])
        evidence = research['evidence']
        for key in eh.DERIVED_EVIDENCE:
            evidence.pop(key, None)
        cutoff = tr.utc(research['observed_at_utc'])
        live = tr.prepare(row, cutoff, copy.deepcopy(evidence))
        self.assertEqual(live['version'], tr.VERSION)
        self.assertNotIn('ce3n_fit', live)
        # A v6 replay of a domestic row is v5.
        self.assertEqual(tr.prepare(row, cutoff, copy.deepcopy(evidence), version=tr.CE3N_VERSION), live)
        # A UCL/UEL forecast frozen under v1-v5 replays under its own version (v5: v4 on UCL/UEL).
        home, away = clubs()
        europe, evidence = european_row(home, away)
        for version in (tr.LEGACY_VERSION, tr.V4_VERSION, tr.VERSION):
            context = tr.prepare(europe, cutoff, copy.deepcopy(evidence), version=version)
            self.assertNotIn('ce3n_fit', context)
            self.assertEqual(context['margin_distribution'], json.loads(margins(tr.research_grid(context['goal_rates']))))

    def test_live_replay_rebuilds_v6(self):
        home, away = clubs()
        row, evidence = european_row(home, away)
        context = tr.prepare(row, CUTOFF, copy.deepcopy(evidence))
        frozen = {**row, 'team_research_json': json.dumps(context)}
        matrices, gaps = rb.archived_candidates(frozen, CUTOFF + pd.Timedelta(minutes=1))
        self.assertNotIn('C', gaps)
        self.assertEqual(json.loads(margins(matrices['C'])), context['margin_distribution'])

    def test_enrich_writes_v6_columns_and_ce_shadow(self):
        home, away = clubs()
        row, evidence = european_row(home, away)
        inputs = {k: v for k, v in row.items() if not k.startswith('research_p') and k != 'team_research_json'}
        with tempfile.TemporaryDirectory() as tmp, \
                patch.object(tr, 'collect_fixture', side_effect=lambda r, c: copy.deepcopy(evidence)):
            out = tr.enrich(pd.DataFrame([inputs]), tmp, fetch=False, clock=lambda: CUTOFF.to_pydatetime()).iloc[0]
        context = json.loads(out['team_research_json'])
        self.assertEqual(out['research_version'], tr.CE3N_VERSION)
        self.assertEqual(out['research_p_home'], hda(context)[0])
        self.assertEqual(out[tr.SHADOW_PREFIX + 'home'], hda(context['shadow_v4'])[0])


def v6_snapshot(kickoff, home, away, rates=(1.6, 1.1)):
    cutoff = pd.Timestamp(kickoff) - pd.Timedelta(hours=6)
    row, _ = european_row(home, away)
    row = {**row, 'kickoff_utc': pd.Timestamp(kickoff).isoformat(), 'lambda_home': rates[0], 'lambda_away': rates[1],
           'research_history_json': json.dumps({'home': [], 'away': [], 'h2h': [], 'teams': {'home': home, 'away': away}})}
    context = tr.prepare(row, cutoff, {})
    row['team_research_json'] = json.dumps(context)
    meta = {'generated_at_utc': cutoff.isoformat(), 'captured_at_utc': cutoff.isoformat(), 'git_commit_sha': 'x'}
    return meta, row


class MonitoringTest(unittest.TestCase):
    def test_trigger_needs_150_matches_3_weeks_and_a_clear_interval(self):
        weeks = [f'2026-W{w:02d}' for w in range(47, 51)]

        def scores(n, worse):
            rows = []
            for i in range(n):
                week = weeks[i % len(weeks)]
                base = .6 + .01 * (i % 7)
                rows += [{'fixture_key': str(i), 'league': 'UCL', 'week': week, 'phase': 'live', 'group': 'Asian handicap',
                          'candidate': 'CE', 'log_loss': base, 'offers': 2},
                         {'fixture_key': str(i), 'league': 'UCL', 'week': week, 'phase': 'live', 'group': 'Asian handicap',
                          'candidate': 'CE3n', 'log_loss': base + worse + .001 * ((i * 7) % 5 - 2), 'offers': 2}]
            return pd.DataFrame(rows)

        def check(frame):
            with patch.object(rm, 'latest_v5_forecasts', return_value={}), \
                    patch.object(eh, 'match_scores', return_value=frame):
                return rm.ce3n_rollback_check([], [], REPO)
        fired = check(scores(160, .02))
        self.assertTrue(fired['eligible'] and fired['triggered'])
        self.assertGreater(fired['interval_95'][0], 0)
        self.assertFalse(check(scores(140, .02))['triggered'])  # below 150 matches
        self.assertFalse(check(scores(160, -.02))['triggered'])  # CE3n better
        quiet_v5 = {'rule': 'r', 'matches': 0, 'weeks': 0, 'eligible': False, 'triggered': False,
                    'v5_minus_v4_log_loss': None, 'interval_95': None, 'log_loss': {}, 'coverage': {}}
        favourites = {'all': {'fixtures': 0, 'picks': 0, 'graded': 0, 'v5_predicted_home_win': None,
                              'v4_predicted_home_win': None, 'actual_home_win': None}, 'by_league': {}, 'fixtures': []}
        lines = rm.markdown({'rollback': quiet_v5, 'home_favourites': favourites, 'ce3n': fired})
        self.assertIn(rm.TRIGGERED, lines[0])
        self.assertIn('research v6 (CE3n', lines[0])
        self.assertEqual(rm.banner({'rollback': quiet_v5, 'ce3n': fired}), lines[:2])
        text = '\n'.join(rm.markdown({'rollback': quiet_v5, 'home_favourites': favourites,
                                      'ce3n': check(scores(140, .02))}))
        self.assertIn('## Research v6 (CE3n, UCL/UEL) rollback check', text)
        self.assertIn('not yet eligible', text)
        self.assertIn('unvalidated view', text)

    def test_grids_rebuild_from_the_frozen_inputs_and_slopes_are_reported(self):
        home, away = clubs()
        snapshots, records = [], []
        for i, (hg, ag) in enumerate([(2, 0), (1, 1), (0, 1), (3, 1), (0, 0)]):
            meta, row = v6_snapshot(f'2026-11-{4 + i:02d}T20:00:00Z', home, away, rates=(1.2 + .3 * i, 1.4 - .1 * i))
            snapshots.append((meta, [row], []))
            records.append({'league_code': 'CL', 'match_id': i, 'home_goals': hg, 'away_goals': ag, 'row': row})
        research = json.loads(snapshots[0][1][0]['team_research_json'])
        g6, g4 = rm.ce3n_grids(research)
        self.assertEqual(json.loads(margins(g6)), research['margin_distribution'])
        self.assertEqual(json.loads(margins(g4)), research['shadow_v4']['margin_distribution'])
        with self.assertRaises(ValueError):
            rm.ce3n_grids({**research, 'margin_distribution': research['shadow_v4']['margin_distribution']})
        lookup = {snap[1][0]['kickoff_utc']: rec for snap, rec in zip(snapshots, records)}
        with patch('performance_tracking.graded_match',
                   side_effect=lambda row, recs: (lookup[row['kickoff_utc']], 'MATCHED')), \
                patch.object(eh, 'usable_results', side_effect=lambda recs, *a, **k: list(recs)), \
                patch.object(eh, 'scoped_offers', return_value=[]):
            out = rm.ce3n_rollback_check(snapshots, records, REPO)
        self.assertEqual(out['matches'], 0)  # no in-scope offers: nothing scored, never triggered
        self.assertFalse(out['triggered'])
        self.assertEqual(out['calibration']['graded_matches'], 5)
        self.assertEqual(out['calibration']['domestic_used'], 5)
        self.assertEqual(set(out['calibration']['slopes']), {'CE3n', 'CE'})

    def test_report_puts_the_v6_banner_at_the_top(self):
        import performance_tracking as pt
        quiet_v5 = {'rule': 'r', 'matches': 0, 'weeks': 0, 'eligible': False, 'triggered': False,
                    'v5_minus_v4_log_loss': None, 'interval_95': None, 'log_loss': {}, 'coverage': {}}
        fired = {'rule': 'r', 'matches': 160, 'weeks': 4, 'eligible': True, 'triggered': True,
                 'ce3n_minus_ce_log_loss': .02, 'interval_95': [.01, .03], 'log_loss': {}, 'coverage': {},
                 'calibration': {'graded_matches': 160, 'domestic_used': 100, 'slopes': {
                     'CE3n': {'home': .95, 'away': 1.0}, 'CE': {'home': .8, 'away': .9}}, 'note': ''}}
        check = {'version': rm.VERSION, 'rollback': quiet_v5, 'ce3n': fired,
                 'home_favourites': {'all': {'fixtures': 0, 'picks': 0, 'graded': 0, 'v5_predicted_home_win': None,
                                             'v4_predicted_home_win': None, 'actual_home_win': None},
                                     'by_league': {}, 'fixtures': []}}
        row = {k: '' for k in pt.SHORTLIST_COLUMNS}
        row.update(week='2026-W47', selection_tier='STRICT', market='Home win', league='EPL', fixture_key='k',
                   status='WON', home_team='A', away_team='B', snapshot_commit='c' * 12)
        with tempfile.TemporaryDirectory() as tmp, patch('performance_excel.write_workbook'):
            pt.report(Path(tmp), [row], [], {}, research_check=check)
            readme = (Path(tmp) / 'performance' / 'README.md').read_text(encoding='utf-8')
            weekly = (Path(tmp) / 'performance' / 'weekly' / '2026-W47.md').read_text(encoding='utf-8')
        for text in (readme, weekly):
            self.assertTrue(text.startswith('> **' + rm.TRIGGERED + '**: research v6'))
            self.assertIn('| CE3n | 0.95 | 1.00 |', text)
        self.assertEqual(readme.count(rm.TRIGGERED + '**'), 1)


def switch_config(directory, domestic='v5', european='v6'):
    path = Path(directory) / 'research_config.json'
    data = json.loads((REPO / 'research_config.json').read_text(encoding='utf-8'))
    data['live'] = {'domestic': domestic, 'european': european}
    path.write_text(json.dumps(data), encoding='utf-8')
    return path


def domestic_frozen():
    row = copy.deepcopy(FIXTURE['row'])
    research = json.loads(row['team_research_json'])
    evidence = research['evidence']
    for key in eh.DERIVED_EVIDENCE:
        evidence.pop(key, None)
    return row, evidence, tr.utc(research['observed_at_utc'])


class LiveSwitchTest(unittest.TestCase):
    """Rolling back is a config switch (research_config.json), never reverting a release: new forecasts use v4,
    archived v5 and v6 forecasts still reproduce exactly."""

    def test_committed_switch_is_v5_domestic_and_v6_european(self):
        self.assertEqual(tr.configured_live(), {'domestic': tr.VERSION, 'european': tr.CE3N_VERSION})
        self.assertIn(tr.VERSION, rb.REPLAYED_VERSIONS)
        self.assertIn(tr.CE3N_VERSION, rb.REPLAYED_VERSIONS)

    def test_v6_rollback_switch_keeps_archived_v6_forecasts_reproducible(self):
        home, away = clubs()
        row, evidence = european_row(home, away)
        frozen = tr.prepare(row, CUTOFF, copy.deepcopy(evidence))  # made under the committed switch: v6
        self.assertEqual(frozen['version'], tr.CE3N_VERSION)
        archived = {**row, 'team_research_json': json.dumps(frozen)}
        with tempfile.TemporaryDirectory() as tmp, patch.object(tr, 'RESEARCH_CONFIG', switch_config(tmp, european='v4')):
            self.assertEqual(tr.configured_live()['european'], tr.V4_VERSION)
            new = tr.prepare(row, CUTOFF, copy.deepcopy(evidence))
            self.assertEqual(new['version'], tr.V4_VERSION)  # new forecasts use v4
            self.assertNotIn('ce3n_fit', new)
            self.assertEqual(new['margin_distribution'], frozen['shadow_v4']['margin_distribution'])  # = CE
            # The archived v6 forecast replays exactly: under its version and frozen fit, in the live replay's
            # candidate C, and in the monitoring's grids.
            again = tr.prepare(row, CUTOFF, copy.deepcopy(evidence), version=frozen['version'], ce3n_fit=frozen['ce3n_fit'])
            self.assertEqual(again['margin_distribution'], frozen['margin_distribution'])
            matrices, gaps = rb.archived_candidates(archived, CUTOFF + pd.Timedelta(minutes=1))
            self.assertNotIn('C', gaps)
            self.assertEqual(json.loads(margins(matrices['C'])), frozen['margin_distribution'])
            g6, _ = rm.ce3n_grids(frozen)
            self.assertEqual(json.loads(margins(g6)), frozen['margin_distribution'])
            # Domestic stays v5 under this switch.
            row_d, evidence_d, cutoff_d = domestic_frozen()
            self.assertEqual(tr.prepare(row_d, cutoff_d, copy.deepcopy(evidence_d))['version'], tr.VERSION)

    def test_v5_rollback_switch_keeps_archived_v5_forecasts_reproducible(self):
        row, evidence, cutoff = domestic_frozen()
        frozen = tr.prepare(row, cutoff, copy.deepcopy(evidence))  # v5 under the committed switch
        self.assertEqual(frozen['version'], tr.VERSION)
        archived = {**row, 'team_research_json': json.dumps(frozen)}
        with tempfile.TemporaryDirectory() as tmp, patch.object(tr, 'RESEARCH_CONFIG', switch_config(tmp, domestic='v4')):
            new = tr.prepare(row, cutoff, copy.deepcopy(evidence))
            self.assertEqual(new['version'], tr.V4_VERSION)
            self.assertNotIn('c6_fit', new)
            self.assertEqual(new['margin_distribution'], frozen['shadow_v4']['margin_distribution'])  # = v4
            again = tr.prepare(row, cutoff, copy.deepcopy(evidence), version=frozen['version'], c6_fit=frozen['c6_fit'])
            self.assertEqual(again['margin_distribution'], frozen['margin_distribution'])
            matrices, gaps = rb.archived_candidates(archived, cutoff + pd.Timedelta(minutes=1))
            self.assertNotIn('C', gaps)
            for k, v in frozen['margin_distribution'].items():
                self.assertAlmostEqual(json.loads(margins(matrices['C']))[k], v, places=15)
            g5, _ = rm.version_grids(frozen)
            self.assertEqual(json.loads(margins(g5)), frozen['margin_distribution'])
            # UCL/UEL stay v6 under this switch.
            home, away = clubs()
            europe, evidence_e = european_row(home, away)
            self.assertEqual(tr.prepare(europe, CUTOFF, copy.deepcopy(evidence_e))['version'], tr.CE3N_VERSION)

    def test_an_invalid_switch_is_refused(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = switch_config(tmp, european='v5')
            with patch.object(tr, 'RESEARCH_CONFIG', path), self.assertRaises(ValueError):
                tr.configured_live()

    def test_banners_name_the_switch(self):
        fired = {'triggered': True, 'matches': 160, 'weeks': 4}
        lines = rm.banner({'rollback': fired, 'ce3n': fired})
        self.assertIn('research_config.json live.domestic to "v4"', lines[0])
        self.assertIn('research_config.json live.european to "v4"', lines[2])
        self.assertNotIn('revert', ' '.join(lines).lower())


class PerCompetitionTest(unittest.TestCase):
    def check(self, results):
        """results: {'pooled'|'UCL'|'UEL': _trigger result}."""
        out = [{'league': rm.CE3N_COMPETITIONS['UCL']}, {'league': rm.CE3N_COMPETITIONS['UEL']}]

        def trigger(rows, *args):
            leagues = {r['league'] for r in rows}
            key = 'pooled' if len(leagues) > 1 else next(c for c, l in rm.CE3N_COMPETITIONS.items() if l in leagues)
            return results[key]
        with patch.object(rm, '_scored', return_value=(out, {}, Counter())), patch.object(rm, '_trigger', side_effect=trigger):
            return rm.ce3n_rollback_check([], [], REPO)

    def result(self, matches, interval, eligible=False, triggered=False):
        return {'matches': matches, 'weeks': 4, 'eligible': eligible, 'triggered': triggered,
                'difference': None if interval is None else sum(interval) / 2, 'interval_95': interval, 'log_loss': {}}

    def test_competition_warning_before_the_pooled_trigger_is_eligible(self):
        out = self.check({'pooled': self.result(90, [-.01, .02]), 'UCL': self.result(50, [.005, .03]),
                          'UEL': self.result(40, [-.02, .01])})
        self.assertTrue(out['by_competition']['UCL']['warning'])
        self.assertFalse(out['by_competition']['UEL']['warning'])
        self.assertFalse(out['triggered'])
        check = {'rollback': {'triggered': False}, 'ce3n': out}
        lines = rm.banner(check)
        self.assertIn(rm.CE3N_WARNING + ' (UCL)', lines[0])
        self.assertNotIn(rm.TRIGGERED, ' '.join(lines))
        favourites = {'all': {'fixtures': 0, 'picks': 0, 'graded': 0, 'v5_predicted_home_win': None,
                              'v4_predicted_home_win': None, 'actual_home_win': None}, 'by_league': {}, 'fixtures': []}
        quiet_v5 = {'rule': 'r', 'matches': 0, 'weeks': 0, 'eligible': False, 'triggered': False,
                    'v5_minus_v4_log_loss': None, 'interval_95': None, 'log_loss': {}, 'coverage': {}}
        text = '\n'.join(rm.markdown({'rollback': quiet_v5, 'home_favourites': favourites, 'ce3n': out}))
        self.assertIn('| UCL | 50 | 4 |', text)
        self.assertIn('| UEL | 40 | 4 |', text)

    def test_no_competition_warning_once_the_pooled_trigger_is_eligible(self):
        out = self.check({'pooled': self.result(160, [-.01, .02], eligible=True), 'UCL': self.result(90, [.005, .03]),
                          'UEL': self.result(70, [-.02, .01])})
        self.assertFalse(out['by_competition']['UCL']['warning'])
        self.assertEqual(rm.banner({'rollback': {'triggered': False}, 'ce3n': out}), [])


class UclLiveCheckTest(unittest.TestCase):
    def ucl_row(self):
        home, away = clubs()
        row, evidence = european_row(home, away)
        context = tr.prepare(row, CUTOFF, copy.deepcopy(evidence))
        return {**row, 'team_research_json': json.dumps(context)}, context

    def master(self, row, flagged=True):
        return pd.DataFrame([{'league': UCL, 'home_team': row['home_team'], 'away_team': row['away_team'],
                              'unvalidated_view': flagged}])

    def test_a_clean_ucl_run_passes(self):
        import research_live_check as lc
        row, context = self.ucl_row()
        domestic = copy.deepcopy(FIXTURE['row'])
        result = lc.check_run([row, domestic], self.master(row))
        self.assertEqual(result['status'], 'passed', result['problems'])
        self.assertEqual(result['ucl_fixtures'], 1)
        self.assertTrue(all(result['checks'].values()))
        self.assertEqual(result['domestic_used'], 1)

    def test_failures_are_reported(self):
        import research_live_check as lc
        row, context = self.ucl_row()
        self.assertEqual(lc.check_run([row], self.master(row, flagged=False))['status'], 'failed')
        bad = copy.deepcopy(context)
        bad['shadow_v4']['margin_distribution'] = bad['margin_distribution']
        result = lc.check_run([{**row, 'team_research_json': json.dumps(bad)}], self.master(row))
        self.assertEqual(result['status'], 'failed')
        self.assertFalse(result['checks']['ce_shadow'])
        stale = copy.deepcopy(context)
        stale['ce3n_fit']['stale'] = True
        self.assertFalse(lc.check_run([{**row, 'team_research_json': json.dumps(stale)}], None)['checks']['fit_window'])
        self.assertEqual(lc.check_run([copy.deepcopy(FIXTURE['row'])])['status'], 'no UCL fixtures')

    def test_weekly_report_shows_the_check_until_a_run_passes(self):
        row, context = self.ucl_row()
        meta = lambda t: {'generated_at_utc': t, 'git_commit_sha': 'none-' + t[:10]}
        old_ucl = {**row, 'team_research_json': json.dumps({**context, 'version': tr.LEGACY_VERSION})}
        pending = rm.ucl_live_check(REPO, [(meta('2026-11-04T10:00:00Z'), [old_ucl], [])])
        self.assertTrue(pending['status'].startswith('pending'))  # a pre-release run is never checked
        self.assertIn('until a run passes', '\n'.join(rm.ucl_check_markdown(pending)))
        done = rm.ucl_live_check(REPO, [(meta('2026-11-04T10:00:00Z'), [old_ucl], []),
                                        (meta('2026-11-24T10:00:00Z'), [row], []),
                                        (meta('2026-11-25T10:00:00Z'), [row], [])])
        self.assertEqual(done['status'], 'passed')
        self.assertEqual(len(done['runs']), 1)  # stops at the first passing run
        self.assertEqual(len(rm.ucl_check_markdown(done)), 2)  # one line once passed


def build_script():
    import importlib.util
    spec = importlib.util.spec_from_file_location('build_research_ce3n_fits', REPO / 'scripts' / 'build_research_ce3n_fits.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def live_file(origins, s=0.1, strengths=True):
    factors = {'status': 'fitted', 'matches': 900, 's': {league: s for league in CFG['leagues']},
               'c': {'UCL': .2, 'UEL': .2}, 'h': {'UCL': .2, 'UEL': .2}}
    return {'version': ce3n.FITS_VERSION, 'candidate_version': ce3n.VERSION, 'basis': 'live',
            'windows': [{'origin': o, 'end_exclusive': o, 'factors': factors,
                         **({'strengths': {'EPL': {'Arsenal': {'goals': [.1, -.1]}}}} if strengths else {})}
                        for o in origins]}


class ScheduledRefreshTest(unittest.TestCase):
    def setUp(self):
        self.b = build_script()

    def test_validate_accepts_a_complete_file_and_refuses_the_rest(self):
        b = self.b
        report = b.validate(live_file(['2026-11-02', '2026-11-16']), live_file(['2026-11-02']), '2026-11-16')
        self.assertEqual((report['new_windows'], report['earlier_windows_changed']), (1, 0))
        with self.assertRaisesRegex(ValueError, 'checked 12 hours'):
            b.validate(live_file(['2026-11-02']), None, '2026-11-16')
        with self.assertRaisesRegex(ValueError, 'drops earlier windows'):
            b.validate(live_file(['2026-11-16']), live_file(['2026-11-02']))
        with self.assertRaisesRegex(ValueError, 'non-finite'):
            b.validate(live_file(['2026-11-02'], s=float('nan')))
        with self.assertRaisesRegex(ValueError, 'no domestic strengths'):
            b.validate(live_file(['2026-11-16'], strengths=False), None, '2026-11-16')
        with self.assertRaisesRegex(ValueError, 'not a live'):
            b.validate({**live_file(['2026-11-02']), 'version': ce3n.HARNESS_FITS_VERSION})
        with self.assertRaisesRegex(ValueError, 'not built on the live basis'):
            b.validate({**live_file(['2026-11-02']), 'basis': 'live builder, holdout results left out (check only)'})

    def test_european_data_must_be_checked_after_the_origin(self):
        with tempfile.TemporaryDirectory() as tmp:
            status, cache = Path(tmp) / 'ucl.json', Path(tmp) / 'cache'
            (cache / 'europa').mkdir(parents=True)
            (cache / 'europa' / 'training.json').write_text(json.dumps({'verified_at_utc': '2026-11-16T12:00:00+00:00'}))
            status.write_text(json.dumps({'checked_at_utc': '2026-11-16T16:30:00+00:00', 'overdue_unfinished_match_ids': []}))
            self.assertEqual(self.b.european_known_through(cache, status), pd.Timestamp('2026-11-16 12:00'))
            status.write_text(json.dumps({'checked_at_utc': '2026-11-16T16:30:00+00:00', 'overdue_unfinished_match_ids': [1]}))
            with self.assertRaisesRegex(ValueError, 'overdue'):
                self.b.european_known_through(cache, status)

    def test_scheduled_run_builds_whenever_the_committed_fit_lacks_todays_window(self):
        import os
        import tempfile
        env = {k: v for k, v in os.environ.items() if k != 'GITHUB_STEP_SUMMARY'}
        self.assertEqual(ce3n.expected_origin(pd.Timestamp('2026-11-16'), self.b.european_fold_rule(CFG)),
                         pd.Timestamp('2026-11-16'))  # the next Monday after 2 Nov is a fold origin
        with tempfile.TemporaryDirectory() as tmp:
            fits = Path(tmp) / 'fits.json'
            fits.write_text(json.dumps({'windows': [{'origin': '2026-11-02'}]}), encoding='utf-8')
            with patch.object(ce3n, 'FITS', fits), patch.dict(os.environ, env, clear=True):
                # The committed file holds today's window: nothing is built.
                with patch.object(self.b, 'build', side_effect=AssertionError('built with a current fit')):
                    self.assertEqual(self.b.main(['--scheduled', '--today', '2026-11-09']), 0)
                # It lacks it: built on the fold origin, and on any later day (a run GitHub started after midnight
                # on 17 Nov 2026 used to stop as "not a fit day").
                for today in ('2026-11-16', '2026-11-17', '2026-11-28'):
                    with patch.object(self.b, '_refresh', return_value=0) as refresh:
                        self.assertEqual(self.b.main(['--scheduled', '--today', today]), 0)
                    self.assertEqual(refresh.call_args.args[-1], pd.Timestamp('2026-11-16'), today)
                fits.write_text(json.dumps({'windows': []}), encoding='utf-8')  # no window at all: built
                with patch.object(self.b, '_refresh', return_value=0) as refresh:
                    self.assertEqual(self.b.main(['--scheduled', '--today', '2026-11-09']), 0)
                refresh.assert_called_once()

    def test_harness_fits_cannot_be_refreshed_by_the_schedule(self):
        for args in (['--basis', 'harness', '--publish'], ['--basis', 'harness', '--leave-out-holdout']):
            with self.assertRaises(SystemExit):
                self.b.main(args)


class WorkflowTest(unittest.TestCase):
    def test_the_c6_refresh_workflow_also_refits_ce3n(self):
        import yaml
        text = (REPO / '.github' / 'workflows' / 'research-c6-fits.yml').read_text(encoding='utf-8')
        flow = yaml.load(text, Loader=yaml.BaseLoader)
        steps = flow['jobs']['refresh']['steps']
        names = [s.get('name') for s in steps]
        c6_step = names.index('Build, validate and publish the live fits')
        ce3n_step = names.index('Build, validate and publish the live CE3n fits')
        self.assertGreater(ce3n_step, c6_step)
        self.assertEqual(steps[ce3n_step]['if'], 'success() || failure()')  # runs even if the C6 refresh failed
        self.assertIn('scripts/build_research_ce3n_fits.py $scheduled --publish', text)
        self.assertNotIn('--basis harness', text)


if __name__ == '__main__':
    unittest.main()
