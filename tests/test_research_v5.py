"""Research v5: C6 live for domestic leagues (docs/plan.md, Paul's exception of 14 Nov 2026).

C6 exactly as the harness computes it (fits from the harness's own walk-forward function, frozen per forecast),
v4 kept beside it in shadow, UCL/UEL unchanged, older forecasts replaying under their own version, and the
monitoring that goes into the weekly report (rollback trigger, holdout-league home favourites).
"""
from __future__ import annotations

import copy
from datetime import datetime, timezone
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import numpy as np
import pandas as pd

import evaluation_harness as eh
import research_backtest as rb
import research_low_score_sharpen as c6
import research_monitoring as rm
import team_research as tr
from asian_handicap import margins

REPO = Path(__file__).resolve().parents[1]
FIXTURE = json.loads((Path(__file__).with_name('fixtures') / 'frozen_forecast_row.json').read_text(encoding='utf-8'))
CFG = json.loads((REPO / 'evaluation_harness_config.json').read_text(encoding='utf-8'))
CUTOFF = pd.Timestamp('2026-11-08T12:00:00Z')


def frozen():
    row = copy.deepcopy(FIXTURE['row'])
    research = json.loads(row['team_research_json'])
    evidence = research['evidence']
    for key in eh.DERIVED_EVIDENCE:
        evidence.pop(key, None)
    return row, evidence, tr.utc(research['observed_at_utc']), research


def synthetic_research(n=2600, seed=7):
    """Research rows (C's goal rates and scores) over 2021-2026, as evaluate_league returns them."""
    rng = np.random.default_rng(seed)
    dates = pd.Timestamp('2021-08-01') + pd.to_timedelta(np.sort(rng.integers(0, 1900, n)), unit='D')
    lam, mu = rng.uniform(.6, 2.6, n), rng.uniform(.5, 2.0, n)
    hg, ag = rng.poisson(lam * 1.1), rng.poisson(mu * .9)
    phase = lambda d: 'development' if d < pd.Timestamp('2025-07-01') else 'validation'
    return [{'identity': {'league': 'EPL', 'phase': phase(d), 'fixture_key': f'EPL|{i}', 'date': d.date().isoformat(),
                          'week': f'{d.isocalendar().year}-W{d.isocalendar().week:02d}'},
             'date': d, 'goal_rates': [float(lam[i]), float(mu[i])], 'home_goals': int(hg[i]), 'away_goals': int(ag[i]),
             'scored': bool(d >= pd.Timestamp(CFG['test_start']))} for i, d in enumerate(dates)]


class FitFileTest(unittest.TestCase):
    def test_fit_file_is_the_harness_walk_forward_fit(self):
        data = c6.load_fits()
        self.assertEqual((data['version'], data['candidate_version']), (c6.FITS_VERSION, c6.VERSION))
        self.assertEqual(data['fold_rule'], {'test_start': CFG['test_start'], 'step_days': CFG['step_days'],
                                             'fixed_bounds': sorted({CFG['development_end'], CFG['holdout_start'],
                                                                     CFG['holdout_end_exclusive']})})
        origins = [w['origin'] for w in data['windows']]
        bounds = [o.date().isoformat() for o, _ in eh.fold_windows(CFG, pd.Timestamp(CFG['end_exclusive']))]
        self.assertEqual(origins, bounds[:len(origins)])  # every harness window, in order, none skipped
        fitted = [w for w in data['windows'] if w['slope_status'] == 'fitted']
        self.assertTrue(fitted)
        self.assertTrue(all(1.0 < w['slope'] < 1.3 for w in fitted))
        self.assertEqual(data['built_with']['leagues'], CFG['leagues'])

    def test_every_window_fits_equal_the_candidate_fits(self):
        research = synthetic_research()
        end = pd.Timestamp('2026-11-09')
        with patch.object(c6.rs, 'MIN_MATCHES', 300), patch.object(c6.rls, 'MIN_MATCHES', 300):
            _, _, _, fits = eh.low_score_sharpen_candidate(research, CFG, end)
            _, _, windows = eh.c6_walk_forward(research, CFG, end, every_window=True)
        by_origin = {w['origin'].date().isoformat(): w for w in windows}
        self.assertTrue(any(f['status'] == 'fitted' for f in fits))
        for f in fits:
            w = by_origin[f['origin']]
            self.assertEqual(w['slope']['slope'], f['slope'])
            self.assertEqual((w['low_score']['rho'], w['low_score']['delta']),
                             (f['low_score']['rho'], f['low_score']['delta']))
        self.assertTrue(all(w['slope'] is not None and w['low_score'] is not None for w in windows))

    def test_fit_at_an_origin_does_not_depend_on_the_end(self):
        research = synthetic_research()
        with patch.object(c6.rs, 'MIN_MATCHES', 300), patch.object(c6.rls, 'MIN_MATCHES', 300):
            _, _, short = eh.c6_walk_forward(research, CFG, pd.Timestamp('2025-03-01'), every_window=True)
            _, _, long = eh.c6_walk_forward(research, CFG, pd.Timestamp('2026-11-09'), every_window=True)
        later = {w['origin']: w for w in long}
        for w in short:
            self.assertEqual(w['slope'], later[w['origin']]['slope'])
            self.assertEqual(w['low_score'], later[w['origin']]['low_score'])

    def test_fit_for_uses_the_latest_window_on_or_before_the_research_day(self):
        data = c6.load_fits()
        last = data['windows'][-1]
        fit = c6.fit_for(pd.Timestamp(last['origin'] + 'T06:00:00Z'))
        self.assertEqual(fit['origin'], last['origin'])
        self.assertEqual([fit[k] for k in c6.FIT_FIELDS], [float(last[k]) for k in c6.FIT_FIELDS])
        self.assertFalse(fit['stale'])
        before = c6.fit_for(pd.Timestamp(last['origin'] + 'T06:00:00Z') - pd.Timedelta(days=1))
        self.assertEqual(before['origin'], data['windows'][-2]['origin'])
        self.assertIsNone(c6.fit_for(pd.Timestamp(data['windows'][0]['origin'] + 'T00:00:00Z') - pd.Timedelta(days=1)))

    def test_fit_file_behind_the_harness_window_is_flagged_stale(self):
        last = pd.Timestamp(c6.load_fits()['windows'][-1]['origin'])
        late = c6.fit_for((last + pd.Timedelta(days=30)).tz_localize('UTC'))
        self.assertEqual(late['origin'], last.date().isoformat())
        self.assertTrue(late['stale'])
        self.assertGreater(pd.Timestamp(late['expected_origin']), last)
        row, evidence, _, _ = frozen()
        context = tr.prepare(row, (last + pd.Timedelta(days=30)).tz_localize('UTC'), copy.deepcopy(evidence))
        self.assertTrue(any('C6 fit file is behind' in w for w in context['warnings']))

    def test_expected_origin_matches_the_harness_fold_windows(self):
        rule = c6.load_fits()['fold_rule']
        for day in pd.date_range('2022-08-01', '2026-11-08', freq='5D'):
            bounds = {b for w in eh.fold_windows(CFG, day + pd.Timedelta(days=1)) for b in w}
            self.assertEqual(c6.expected_origin(day, rule), max(b for b in bounds if b <= day), day)


class LiveV5Test(unittest.TestCase):
    def test_domestic_v5_is_c6_on_v4_goal_rates_with_v4_in_shadow(self):
        row, evidence, cutoff, _ = frozen()
        v5 = tr.prepare(row, cutoff, copy.deepcopy(evidence))
        v4 = tr.prepare(row, cutoff, copy.deepcopy(evidence), version=tr.V4_VERSION)
        self.assertEqual((v5['version'], v4['version']), (tr.VERSION, tr.V4_VERSION))
        self.assertEqual(v5['goal_rates'], v4['goal_rates'])
        self.assertEqual(v5['form'], v4['form'])
        self.assertEqual(v5['shadow_v4']['margin_distribution'], v4['margin_distribution'])
        self.assertEqual(v5['shadow_v4']['p_over_1_5'], v4['p_over_1_5'])
        self.assertEqual(v5['c6_fit'], c6.fit_for(cutoff))
        grid = eh.c6_matrix(v5['goal_rates'], v5['c6_fit'])
        self.assertEqual(v5['margin_distribution'], json.loads(margins(grid)))
        self.assertNotIn('c6_fit', v4)
        self.assertNotIn('shadow_v4', v4)
        # C6 holds C2's draw and sharpens the split: the favourite gets more likely.
        p5, p4 = rm_hda(v5), rm_hda(v4)
        self.assertNotAlmostEqual(p5[1], p4[1], places=6)
        fav = int(np.argmax([p4[0], p4[2]])) * 2
        self.assertGreater(p5[fav], p4[fav] - (p4[1] - p5[1]))

    def test_european_competitions_stay_v4(self):
        row, evidence, cutoff, _ = frozen()
        for league in sorted(tr.EUROPEAN_COMPETITIONS):
            europe = {**row, 'league': league}
            context = tr.prepare(europe, cutoff, copy.deepcopy(evidence))
            same = tr.prepare(europe, cutoff, copy.deepcopy(evidence), version=tr.V4_VERSION)
            self.assertEqual(context['version'], tr.V4_VERSION)
            self.assertEqual(context, same)
            # Even a v5 replay of a UCL/UEL row is v4.
            self.assertEqual(tr.prepare(europe, cutoff, copy.deepcopy(evidence), version=tr.VERSION), same)
            self.assertNotIn('shadow_v4', context)

    def test_v5_replays_from_its_frozen_fit_without_the_fit_file(self):
        row, evidence, cutoff, _ = frozen()
        live = tr.prepare(row, cutoff, copy.deepcopy(evidence))
        with patch.object(c6, 'fit_for', side_effect=AssertionError('fit file read on replay')):
            again = tr.prepare(row, cutoff, copy.deepcopy(evidence), version=live['version'], c6_fit=live['c6_fit'])
        self.assertEqual(again['margin_distribution'], live['margin_distribution'])
        self.assertEqual(again['p_over_1_5'], live['p_over_1_5'])

    def test_older_versions_replay_unchanged_on_independent_poisson(self):
        row, evidence, cutoff, research = frozen()
        self.assertEqual(research['version'], tr.LEGACY_VERSION)
        again = tr.prepare(row, cutoff, copy.deepcopy(evidence), version=research['version'])
        for key, value in research['margin_distribution'].items():
            self.assertAlmostEqual(again['margin_distribution'][key], value, places=15)
        for version in (tr.LEGACY_VERSION, tr.V2_VERSION, tr.V3_VERSION, tr.V4_VERSION):
            context = tr.prepare(row, cutoff, copy.deepcopy(evidence), version=version)
            self.assertEqual(context['margin_distribution'], json.loads(margins(tr.research_grid(context['goal_rates']))))
            self.assertNotIn('c6_fit', context)

    def test_no_fit_window_leaves_no_research_probabilities(self):
        row, evidence, cutoff, _ = frozen()
        with patch.object(c6, 'fit_for', return_value=None):
            context = tr.prepare(row, cutoff, copy.deepcopy(evidence))
        self.assertNotIn('margin_distribution', context)
        self.assertIn('shadow_v4', context)
        self.assertTrue(any('no C6 fit window' in w for w in context['warnings']))

    def test_enrich_writes_v5_columns_and_v4_shadow(self):
        row, evidence, cutoff, _ = frozen()
        inputs = {k: v for k, v in row.items() if not k.startswith('research_') and k != 'team_research_json'}
        with tempfile.TemporaryDirectory() as tmp, \
                patch.object(tr, 'collect_fixture', side_effect=lambda r, c: copy.deepcopy(evidence)):
            out = tr.enrich(pd.DataFrame([inputs, {**inputs, 'league': 'UEFA Europa League'}]), tmp, fetch=False,
                            clock=lambda: cutoff.to_pydatetime()).to_dict('records')
        domestic, europe = out
        context = json.loads(domestic['team_research_json'])
        self.assertEqual(domestic['research_version'], tr.VERSION)
        self.assertEqual(europe['research_version'], tr.V4_VERSION)
        self.assertEqual(domestic['research_p_home'], rm_hda(context)[0])
        self.assertEqual(domestic[tr.SHADOW_PREFIX + 'home'], rm_hda(context['shadow_v4'])[0])
        self.assertEqual(domestic[tr.SHADOW_PREFIX + 'over_1_5'], context['shadow_v4']['p_over_1_5'])
        self.assertNotIn(tr.SHADOW_PREFIX + 'home', {k for k, v in europe.items() if v is not None and v == v})

    def test_live_replay_rebuilds_v5_on_c6_and_v4_on_poisson(self):
        row, evidence, cutoff, _ = frozen()
        for version in (tr.VERSION, tr.V4_VERSION):
            context = tr.prepare(row, cutoff, copy.deepcopy(evidence), version=version)
            frozen_row = {**row, 'team_research_json': json.dumps(context)}
            matrices, gaps = rb.archived_candidates(frozen_row, cutoff + pd.Timedelta(minutes=1))
            self.assertNotIn('C', gaps)
            self.assertEqual(json.loads(margins(matrices['C'])), context['margin_distribution'])
        old = {**row}
        _, gaps = rb.archived_candidates(old, cutoff + pd.Timedelta(minutes=1))
        self.assertIn('unsupported frozen research version', gaps['C'])  # v1, as before v5

    def test_harness_c_stays_v4(self):
        match = pd.Series({'HomeTeam': 'Arsenal', 'AwayTeam': 'Chelsea'})
        inputs = eh.research_inputs(match, pd.DataFrame(columns=['Date', 'HomeTeam', 'AwayTeam', 'FTHG', 'FTAG']),
                                    pd.Timestamp('2024-02-05'), {'lambda_home': 1.5, 'lambda_away': 1.1})
        self.assertIsNone(inputs['league'])
        self.assertEqual(set(inputs), set(tr.INPUT_SCHEMA))


def rm_hda(context):
    cols = tr.outcome_columns(context, '')
    return [cols['home'], cols['draw'], cols['away']]


def v5_snapshot(kickoff, league='Eredivisie', home='AZ Alkmaar', away='Groningen', pick_side='home', rates=(1.9, .8)):
    """A frozen snapshot with one v5 forecast and one value pick, and the verified result record."""
    cutoff = pd.Timestamp(kickoff) - pd.Timedelta(hours=6)
    row, evidence, _, _ = frozen()
    row = {**row, 'league': league, 'home_team': home, 'away_team': away, 'kickoff_utc': pd.Timestamp(kickoff).isoformat(),
           'lambda_home': rates[0], 'lambda_away': rates[1], 'research_history_json': '{}'}
    context = tr.prepare(row, cutoff, {})
    row['team_research_json'] = json.dumps(context)
    row.update(tr.outcome_columns(context, 'research_p_'))
    row.update(tr.outcome_columns(context['shadow_v4'], tr.SHADOW_PREFIX))
    row['asian_handicap_offers'] = json.dumps([])
    meta = {'generated_at_utc': cutoff.isoformat(), 'captured_at_utc': cutoff.isoformat(), 'git_commit_sha': 'x'}
    pick = {'league': league, 'home_team': home, 'away_team': away, 'kickoff_utc': row['kickoff_utc'],
            'shortlist_source': 'value', 'market': 'Asian Handicap Home -0.25' if pick_side == 'home' else 'Away win',
            'handicap_side': pick_side}
    return meta, row, pick


class MonitoringTest(unittest.TestCase):
    def test_trigger_needs_150_matches_and_3_weeks_and_a_clear_interval(self):
        weeks = [f'2026-W{w:02d}' for w in range(46, 50)]

        def scores(n, worse):
            rows = []
            for i in range(n):
                week = weeks[i % len(weeks)]
                base = .6 + .01 * (i % 7)
                rows += [{'fixture_key': str(i), 'league': 'L', 'week': week, 'phase': 'live', 'group': 'Asian handicap',
                          'candidate': 'v4', 'log_loss': base, 'offers': 2},
                         {'fixture_key': str(i), 'league': 'L', 'week': week, 'phase': 'live', 'group': 'Asian handicap',
                          'candidate': 'v5', 'log_loss': base + worse + .001 * ((i * 7) % 5 - 2), 'offers': 2}]
            return pd.DataFrame(rows)

        def check(frame):
            with patch.object(rm, 'latest_v5_forecasts', return_value={}), \
                    patch.object(eh, 'match_scores', return_value=frame):
                return rm.rollback_check([], [], REPO)
        fired = check(scores(160, .02))
        self.assertTrue(fired['eligible'])
        self.assertTrue(fired['triggered'])
        self.assertGreater(fired['interval_95'][0], 0)
        self.assertFalse(check(scores(140, .02))['triggered'])  # below 150 matches
        self.assertFalse(check(scores(160, -.02))['triggered'])  # v5 better
        lines = rm.markdown({'rollback': fired, 'home_favourites': {'all': rm.home_favourites([], [], REPO)['all'],
                                                                    'by_league': {}}})
        self.assertIn(rm.TRIGGERED, lines[0])
        quiet = rm.markdown({'rollback': check(scores(140, .02)), 'home_favourites': rm.home_favourites([], [], REPO)})
        self.assertNotIn(rm.TRIGGERED, quiet[0])
        self.assertIn('not yet eligible', '\n'.join(quiet))

    def test_v5_and_v4_grids_are_rebuilt_from_the_frozen_inputs(self):
        meta, row, _ = v5_snapshot('2026-11-08T15:00:00Z')
        research = json.loads(row['team_research_json'])
        v5, v4 = rm.version_grids(research)
        self.assertEqual(json.loads(margins(v5)), research['margin_distribution'])
        tampered = {**research, 'margin_distribution': research['shadow_v4']['margin_distribution']}
        with self.assertRaises(ValueError):
            rm.version_grids(tampered)

    def test_home_favourite_picks_in_holdout_leagues(self):
        records = []
        snapshots = []
        for i, (league, side, hg, ag) in enumerate([('Eredivisie', 'home', 2, 0), ('Super Lig', 'home', 0, 1),
                                                    ('Premier League', 'home', 3, 0), ('Eredivisie', 'away', 0, 2)]):
            kickoff = f'2026-11-{10 + i:02d}T15:00:00Z'
            meta, row, pick = v5_snapshot(kickoff, league=league, home=f'H{i}', away=f'A{i}', pick_side=side)
            snapshots.append((meta, [row], [pick]))
            records.append({'league_code': 'X', 'match_id': i, 'home_goals': hg, 'away_goals': ag})
        with patch('performance_tracking.graded_match',
                   side_effect=lambda row, recs: (next(r for r in recs if r['match_id'] == int(row['home_team'][1:])),
                                                  'MATCHED')), \
                patch.object(eh, 'usable_results', side_effect=lambda recs, *a, **k: list(recs)):
            out = rm.home_favourites(snapshots, records, REPO)
        self.assertEqual(out['all']['fixtures'], 2)  # Premier League and the away pick left out
        self.assertEqual(out['all']['graded'], 2)
        self.assertEqual(out['all']['actual_home_win'], .5)
        self.assertGreater(out['all']['v5_predicted_home_win'], .5)
        self.assertEqual(set(out['by_league']), {'Eredivisie', 'Super Lig'})
        self.assertNotEqual(out['all']['v5_predicted_home_win'], out['all']['v4_predicted_home_win'])

    def test_report_puts_the_banner_at_the_top(self):
        import performance_tracking as pt
        check = {'version': rm.VERSION,
                 'rollback': {'rule': 'r', 'matches': 160, 'weeks': 4, 'eligible': True, 'triggered': True,
                              'v5_minus_v4_log_loss': .02, 'interval_95': [.01, .03], 'log_loss': {}, 'coverage': {}},
                 'home_favourites': {'all': {'fixtures': 0, 'picks': 0, 'graded': 0, 'v5_predicted_home_win': None,
                                             'v4_predicted_home_win': None, 'actual_home_win': None},
                                     'by_league': {}, 'fixtures': []}}
        row = {k: '' for k in pt.SHORTLIST_COLUMNS}
        row.update(week='2026-W46', selection_tier='STRICT', market='Home win', league='EPL', fixture_key='k',
                   status='WON', home_team='A', away_team='B', snapshot_commit='c' * 12)
        with tempfile.TemporaryDirectory() as tmp, patch('performance_excel.write_workbook'):
            pt.report(Path(tmp), [row], [], {}, research_check=check)
            readme = (Path(tmp) / 'performance' / 'README.md').read_text(encoding='utf-8')
            weekly = (Path(tmp) / 'performance' / 'weekly' / '2026-W46.md').read_text(encoding='utf-8')
            saved = json.loads((Path(tmp) / 'performance' / 'research_v5_monitoring.json').read_text(encoding='utf-8'))
        self.assertTrue(readme.startswith('> **' + rm.TRIGGERED))
        self.assertTrue(weekly.startswith('> **' + rm.TRIGGERED))
        self.assertIn('## Research v5 (C6) rollback check', readme)
        self.assertIn('## Home favourites in Eredivisie, Primeira Liga and Süper Lig', weekly)
        self.assertEqual(saved['rollback']['triggered'], True)


if __name__ == '__main__':
    unittest.main()
