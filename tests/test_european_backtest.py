"""European results in the harness: inventory, periods, the European holdout lock, and CE's independence.

Real cached results are used only for locked runs (never a European holdout score); every run that
includes the holdout uses synthetic results.
"""
import json
from pathlib import Path
import shutil
import tempfile
import unittest

import numpy as np
import pandas as pd

import european_results as er
import evaluation_harness as eh

REPO = Path(__file__).resolve().parents[1]
CACHE = REPO / '.football_cache'
CFG = json.loads((REPO / 'evaluation_harness_config.json').read_text(encoding='utf-8'))
END = CFG['european']['end_exclusive']


def window(**european):
    return {**CFG, 'european': {**CFG['european'], **european}}


def synthetic(start, matches, teams=8, seed=7):
    """A round of results every 3 days; scores drawn at random (no odds)."""
    rng = np.random.default_rng(seed)
    names = [f'Club {i}' for i in range(teams)]
    rows = []
    for k in range(0, matches, teams // 2):
        order = rng.permutation(teams)  # each round pairs every club once
        for home, away in zip(order[0::2], order[1::2]):
            rows.append({'Date': pd.Timestamp(start) + pd.Timedelta(days=3 * (k // (teams // 2))),
                         'HomeTeam': names[home], 'AwayTeam': names[away], 'FTHG': int(rng.poisson(1.5)),
                         'FTAG': int(rng.poisson(1.1)), 'Season': '2024', 'stage': 'LEAGUE_STAGE',
                         'stage_group': 'league phase'})
    return pd.DataFrame(rows[:matches])


class InventoryTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ucl = er.load(CACHE, 'UCL', END)
        cls.uel = er.load(CACHE, 'UEL', END)

    def test_each_competition_loads_what_live_trains_on(self):
        import europa_training
        live = europa_training.frame(json.loads(er.europa_snapshot(CACHE).read_text(encoding='utf-8')),
                                     pd.Timestamp(END, tz='UTC').to_pydatetime())
        cols = ['Date', 'HomeTeam', 'AwayTeam', 'FTHG', 'FTAG']
        pd.testing.assert_frame_equal(self.uel[cols].reset_index(drop=True),
                                      live[cols].sort_values(['Date', 'HomeTeam', 'AwayTeam'], kind='stable').reset_index(drop=True))
        self.assertEqual(len(self.ucl), 575)  # the live UCL fit of 8 Nov 2026 trained on 575 matches
        self.assertEqual(len(self.uel), 732)  # and the live UEL fit on 732
        self.assertFalse(self.ucl.stage.isna().any() or self.uel.stage.isna().any())

    def test_stage_groups(self):
        cases = [('UCL', 'GROUP_STAGE', 'group stage'), ('UCL', 'LEAGUE_STAGE', 'league phase'),
                 ('UCL', 'LAST_16', 'knockout'), ('UEL', 'Gruppe H', 'group stage'), ('UEL', 'Group A', 'group stage'),
                 ('UEL', 'League phase', 'league phase'), ('UEL', '7', 'league phase'),
                 ('UEL', 'Play-off Game 1', 'knockout'), ('UEL', 'Final', 'knockout')]
        for competition, stage, group in cases:
            self.assertEqual(er.stage_group(competition, stage), group, (competition, stage))
        self.assertEqual(self.uel.groupby('Season').stage_group.apply(lambda s: (s == 'knockout').sum()).loc['2024'], 45)

    def test_snapshot_rebuilds_from_the_cached_sources_and_nothing_is_topped_up(self):
        inventory = er.uel_inventory(CACHE, END)
        self.assertEqual(inventory['snapshot_vs_rebuilt_from_sources']['differences'], [])
        self.assertEqual(inventory['top_up']['added'], 0)
        self.assertEqual(inventory['regulation_corrections'], 12)
        self.assertEqual(sum(r['matches'] for r in inventory['seasons']), 732)


class EuropeanPeriodTest(unittest.TestCase):
    def test_periods(self):
        cases = [('2024-03-01', 'UEL', 'development'), ('2024-03-01', 'UCL', 'development'),
                 ('2024-10-01', 'UCL', 'validation'), ('2025-01-20 20:00', 'UCL', 'validation'),
                 ('2025-01-21 17:45', 'UCL', 'holdout'), ('2026-10-12 21:00', 'UCL', 'holdout'),
                 ('2026-10-13', 'UCL', 'retrospective'), ('2025-01-21', 'UEL', 'retrospective'),
                 ('2026-04-01', 'UEL', 'retrospective')]
        for date, competition, name in cases:
            self.assertEqual(eh.european_phase(date, competition, CFG), name, (date, competition))

    def test_folds_break_at_every_european_boundary(self):
        e = CFG['european']
        bounds = {b for w in eh.fold_windows(e, pd.Timestamp(e['end_exclusive'])) for b in w}
        self.assertTrue({pd.Timestamp(e[k]) for k in ('development_end', 'holdout_start', 'holdout_end_exclusive')} <= bounds)

    def test_the_locked_block(self):
        ucl = er.load(CACHE, 'UCL', END)[['Date']]  # identities only
        locked = ucl.Date.map(lambda d: eh.european_phase(d, 'UCL', CFG) == 'holdout')
        weeks = ucl.Date[locked].dt.strftime('%G-%V').nunique()
        self.assertEqual((int(locked.sum()), weeks), (288, 29))


class EuropeanLockTest(unittest.TestCase):
    def test_locked_runs_skip_the_european_holdout_on_the_cached_results(self):
        cfg = window(test_start='2024-11-01', end_exclusive='2025-03-01')
        records, _, coverage, calib = eh.european(CACHE, cfg)
        self.assertTrue(records)
        self.assertNotIn('holdout', {r['phase'] for r in records} | {r['phase'] for r in calib})
        self.assertEqual({r['league'] for r in records}, {'UEL'})
        self.assertGreater(coverage['UCL:locked_holdout'], 0)
        self.assertIn('retrospective', {r['phase'] for r in records})

    def test_locked_runs_never_train_on_european_holdout_results(self):
        data = pd.DataFrame({'Date': pd.to_datetime(['2025-01-20', '2025-01-21', '2026-10-12', '2026-10-13'])})
        self.assertEqual(list(eh.european_training_rows(data, 'UCL', CFG, False).Date.dt.date.astype(str)),
                         ['2025-01-20', '2026-10-13'])
        self.assertEqual(len(eh.european_training_rows(data, 'UEL', CFG, False)), 4)
        self.assertEqual(len(eh.european_training_rows(data, 'UCL', CFG, True)), 4)

    def test_holdout_runs_score_only_the_holdout_and_locked_runs_none_of_it(self):
        cfg = window(min_train=40, test_start='2024-09-01', end_exclusive='2026-11-01', step_days=28)
        data = {'UCL': synthetic('2024-09-01', 420), 'UEL': synthetic('2024-09-01', 420, seed=8)}
        locked, _, coverage, _ = eh.european(None, cfg, data=data)
        self.assertTrue(locked)
        self.assertNotIn('holdout', {r['phase'] for r in locked})
        self.assertGreater(coverage['UCL:locked_holdout'], 0)
        unlocked, _, _, _ = eh.european(None, cfg, include_holdout=True, keep={'CE'}, data=data)
        self.assertTrue(unlocked)
        self.assertEqual({(r['league'], r['phase']) for r in unlocked}, {('UCL', 'holdout')})
        # A holdout run forecasts each holdout match from earlier results only, holdout ones included.
        self.assertEqual(len({r['fixture_key'] for r in unlocked}), coverage['UCL:locked_holdout'])

    def test_the_european_ledger_is_its_own_and_once_per_candidate_and_setup(self):
        self.assertNotEqual(eh.european_ledger(CFG).resolve(), eh.LEDGER.resolve())
        with tempfile.TemporaryDirectory() as tmp:
            path, ledger = Path(tmp) / 'declaration.json', Path(tmp) / 'ledger.json'
            declare = {'candidate': 'CE2', 'baseline': 'CE', 'primary_metric': 'AH all',
                       'draw_sensitive_lines': [-0.5, 0, 0.5], 'calibration_tolerance': CFG['calibration_tolerance']['name'],
                       'declared_by': 'Paul', 'declared_at': '2026-11-11'}
            path.write_text(json.dumps(declare), encoding='utf-8')
            registry = {**eh.EUROPEAN_CANDIDATES, 'CE2': 'test'}
            setup = {'sha256': 'b' * 64}
            declared = eh.validate_declaration(path, CFG, setup, ledger, registry)
            with self.assertRaises(ValueError):  # a domestic candidate is not a European one
                path.write_text(json.dumps({**declare, 'candidate': 'C6'}), encoding='utf-8')
                eh.validate_declaration(path, CFG, setup, ledger, registry)
            path.write_text(json.dumps(declare), encoding='utf-8')
            verdict = {'passes_holdout_gate': False}
            eh.record_holdout(declared, setup, 'abc', 270, verdict, ledger)
            with self.assertRaises(ValueError):
                eh.validate_declaration(path, CFG, setup, ledger, registry)
            with self.assertRaises(ValueError):
                eh.validate_declaration(path, CFG, {'sha256': 'c' * 64}, ledger, registry)

    def test_the_european_setup_fingerprint_covers_code_data_and_config(self):
        first = eh.european_setup_fingerprint(CFG, CACHE)
        self.assertIn('data/europa/training.json', first['parts'])
        self.assertIn('data/fdorg_history_UCL_2024.json', first['parts'])
        self.assertIn('european_results.py', first['parts'])
        self.assertNotEqual(first['sha256'], eh.european_setup_fingerprint(window(min_train=200), CACHE)['sha256'])

    def test_a_european_verdict_has_no_market_reference(self):
        records, calib = [], []
        for i in range(40):
            for cand, loss in (('CE2', .6), ('CE', .7)):
                records.append({'fixture_key': f'f{i}', 'league': 'UCL', 'week': f'w{i % 8}', 'phase': 'holdout',
                                'candidate': cand, 'market': 'AH +0.00', 'log_loss': loss})
                calib.append({'phase': 'holdout', 'candidate': cand, 'probs': [.45, .25, .30], 'outcome': 0})
        declaration = {'candidate': 'CE2', 'baseline': 'CE', 'primary_metric': 'AH all',
                       'draw_sensitive_lines': [-.5, 0, .5], 'calibration_rule': CFG['calibration_tolerance']}
        verdict = eh.holdout_verdict(records, calib, declaration, {})
        self.assertIsNone(verdict['versus_market'])
        self.assertFalse(verdict['passes_holdout_gate'])  # 40 fixtures: below the sample minimum


class CEIndependenceTest(unittest.TestCase):
    """CE reads European results only: never odds, never a later result, never a domestic result."""

    @classmethod
    def setUpClass(cls):
        cls.uel = er.load(CACHE, 'UEL', END)

    def fold(self, data, origin):
        from football_value_pipeline_v2_standalone import DixonColesModel
        profile = CFG['production_v2']
        train = data[data.Date < origin]
        model = DixonColesModel(half_life_days=profile['half_life_days'], l2=CFG['baseline_l2'], max_goals=CFG['max_goals'],
                                shot_features=profile['shot_features'], bbs_statistics=False).fit(train.copy(), as_of=origin)
        return train, model

    def test_ce_ignores_every_odds_field(self):
        origin = pd.Timestamp('2024-10-01')
        odds = ['PSH', 'PSD', 'PSA', 'P>2.5', 'P<2.5', 'AHh', 'PAHH', 'PAHA', 'B365H', 'B365D', 'B365A',
                'B365>2.5', 'B365<2.5', 'AvgH', 'AvgD', 'AvgA', 'MaxH', 'PSCH', '1XBH']
        rng = np.random.default_rng(3)
        priced = self.uel.copy()
        for c in odds:
            priced[c] = rng.uniform(1.2, 9., len(priced))
        train, model = self.fold(priced, origin)
        row = priced[priced.Date >= origin].iloc[0]
        base, _ = eh.european_matrices(row, train, origin, model)
        changed_rows = priced.copy()
        changed_rows[odds] = 9.99
        train2, model2 = self.fold(changed_rows, origin)
        again, _ = eh.european_matrices(changed_rows[changed_rows.Date >= origin].iloc[0], train2, origin, model2)
        np.testing.assert_array_equal(base['CE'], again['CE'])
        # And CE on the same rows without any odds column at all.
        bare_train, bare_model = self.fold(self.uel, origin)
        bare, _ = eh.european_matrices(self.uel[self.uel.Date >= origin].iloc[0], bare_train, origin, bare_model)
        np.testing.assert_array_equal(base['CE'], bare['CE'])

    def test_a_later_result_never_changes_an_earlier_forecast(self):
        cfg = window(test_start='2024-02-01', end_exclusive='2024-12-20')
        data = self.uel.loc[self.uel.Date < '2024-12-20'].copy()
        before = eh.evaluate_european('UEL', None, cfg, data=data)[3]
        changed = data.copy()
        target = changed.index[changed.Date == pd.Timestamp('2024-10-03')][0]
        changed.loc[target, ['FTHG', 'FTAG']] = [7, 0]
        after = eh.evaluate_european('UEL', None, cfg, data=changed)[3]
        self.assertEqual([r['fixture_key'] for r in before], [r['fixture_key'] for r in after])
        earlier = [(a['probs'], b['probs']) for a, b in zip(before, after) if a['fixture_key'].split('|')[1] <= '2024-10-03']
        later = [(a['probs'], b['probs']) for a, b in zip(before, after) if a['fixture_key'].split('|')[1] > '2024-10-17']
        self.assertTrue(earlier and later)
        self.assertTrue(all(a == b for a, b in earlier))
        self.assertTrue(any(a != b for a, b in later))

    def test_domestic_results_never_reach_ce(self):
        cfg = window(test_start='2024-02-01', end_exclusive='2024-12-20')
        full = eh.european(CACHE, cfg)
        with tempfile.TemporaryDirectory() as tmp:
            only = Path(tmp)
            for path in er.ucl_files(CACHE):
                shutil.copy(path, only / path.name)
            (only / 'europa').mkdir()
            shutil.copy(er.europa_snapshot(CACHE), only / 'europa' / 'training.json')
            alone = eh.european(only, cfg)
        self.assertTrue(full[0])
        self.assertEqual(full[0], alone[0])
        self.assertEqual(full[3], alone[3])
        # Every team CE was fitted on is a team of that competition.
        teams = set(self.uel.HomeTeam) | set(self.uel.AwayTeam)
        _, model = self.fold(self.uel, pd.Timestamp('2024-10-01'))
        self.assertTrue(set(model.teams) <= teams)


class ReportTest(unittest.TestCase):
    def test_the_report_refuses_any_european_holdout_row(self):
        import sys
        sys.path.insert(0, str(REPO / 'scripts'))
        import european_ce_report as report
        with tempfile.TemporaryDirectory() as tmp:
            run = Path(tmp)
            (run / 'results.json').write_text(json.dumps({'mode': 'european', 'periods': {}}), encoding='utf-8')
            pd.DataFrame([{'phase': 'holdout', 'league': 'UCL', 'fixture_key': 'k', 'group': '1X2', 'log_loss': 1.}]
                         ).to_csv(run / 'fixture_scores.csv', index=False)
            pd.DataFrame([{'phase': 'validation', 'league': 'UEL', 'outcome': 0, 'p_home': .5, 'p_draw': .3,
                           'p_away': .2}]).to_csv(run / 'forecasts_1x2.csv', index=False)
            with self.assertRaises(ValueError):
                report.report(run)
            (run / 'results.json').write_text(json.dumps({'mode': 'european_holdout', 'periods': {}}), encoding='utf-8')
            with self.assertRaises(ValueError):
                report.report(run)


class DomesticFormTest(unittest.TestCase):
    def test_reviewed_identities_only_and_dates_before_the_fixture(self):
        domestic = pd.DataFrame({'Date': pd.to_datetime(['2024-08-01', '2024-08-08', '2024-09-01', '2024-09-20']),
                                 'HomeTeam': ['Aston Villa', 'Brentford', 'Aston Villa', 'Aston Villa'],
                                 'AwayTeam': ['Brentford', 'Aston Villa', 'Brentford', 'Brentford']})
        histories = {'EPL': (domestic, {'Aston Villa', 'Brentford'})}
        fixtures = pd.DataFrame({'Date': pd.to_datetime(['2024-09-20']), 'HomeTeam': ['Aston Villa FC'],
                                 'AwayTeam': ['Aston Villans']})
        flags, teams = er.domestic_form_coverage(fixtures, histories, min_matches=3, days=365)
        self.assertEqual(int(flags.home_domestic_matches.iloc[0]), 3)  # the 20 Sep match itself is not earlier
        self.assertEqual(int(flags.away_domestic_matches.iloc[0]), 0)  # no fuzzy match for a near-miss name
        self.assertFalse(bool(flags.both.iloc[0]))
        self.assertEqual(teams['mapped_teams'], 1)


if __name__ == '__main__':
    unittest.main()
