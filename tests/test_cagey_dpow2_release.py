"""The D_pow2 release (docs/plan.md, Phase 3b-3): D_pow2 prices domestic fixtures' cagey figures, UCL and UEL keep
D, D stays in shadow, runs record what they used and replay exactly, earlier runs replay as before, the rollback
trigger rebuilds both corrections from frozen quotes, and the activity log records the switch and the release.
"""
from __future__ import annotations

import json
from pathlib import Path
import tempfile
import unittest

import numpy as np
import pandas as pd

import cagey_tier_v3
import market_implied as mi
import model_activity as ma
import narrow_margin as nm
import price_edge_cagey_shortlist as v28
import price_edge_shortlist as v27
import research_monitoring as rm
from tests import test_cagey_market_independence as independence

REPO = Path(__file__).resolve().parents[1]
FROZEN, POLICY = independence.FROZEN, independence.POLICY
RELEASE_KEYS = ('cagey_correction_live', 'cagey_corrections')
DIGEST = '82cf7306eee5bdfda21c4fb37d367e6e8b1bf9171415f5acacc3f4827b7123af'


def before_settings():
    """The live settings before the release: D everywhere."""
    return {k: v for k, v in v28.load_settings().items() if k not in RELEASE_KEYS}


def build(row, settings, league=None):
    row = dict(row) if league is None else {**row, 'league': league}
    return v28.build_shortlist(pd.DataFrame([row]), FROZEN['snapshot_generated_utc'], execution_policy=POLICY,
                               settings=settings, model=nm.production_model())


class ConfigTest(unittest.TestCase):
    def test_the_switch_is_as_released(self):
        settings = v28.load_settings()
        self.assertEqual(settings['cagey_correction_live'], {'domestic': 'D_pow2', 'european': 'D'})
        self.assertEqual(settings['model_version'], nm.PRODUCTION_VERSION)  # D's model, unchanged
        models = v28.correction_models(settings, nm.production_model())
        self.assertEqual({k: (m['version'], method) for k, (m, method) in models.items()},
                         {'D': (nm.PRODUCTION_VERSION, 'proportional'), 'D_pow2': (nm.ONE_X_TWO_VERSION, 'power')})
        # The production index and the harness's D are untouched: the release is the switch, not a refit.
        self.assertEqual(nm.versions()['production']['version'], 'cagey-correction-through-2425-v1')

    def test_the_released_model_is_the_tested_one_with_its_own_quintiles(self):
        released, tested = nm.load(nm.ONE_X_TWO_VERSION), nm.load(nm.ONE_X_TWO_VERSION, nm.CANDIDATE_DIR)
        self.assertEqual(released, tested)
        self.assertEqual(nm.model_digest(released), DIGEST)
        quintiles = nm.load_quintiles(released)
        self.assertEqual(quintiles['model_sha256'], DIGEST)
        self.assertAlmostEqual(quintiles['boundaries'][0], released['training_cagey_p20'], places=12)
        self.assertEqual(quintiles['training_matches'], 10956)

    def test_bad_switches_and_pairings_are_refused(self):
        base = v28.load_settings()
        model = nm.production_model()
        bad = [({'cagey_correction_live': {'domestic': 'D_pow2', 'european': 'D_pow2'}}, 'UCL and UEL keep D'),
               ({'cagey_correction_live': {'domestic': 'D_pow'}}, 'must give each'),
               ({'cagey_correction_live': {'domestic': 'X', 'european': 'D'}}, 'must give each'),
               ({'devig_method': 'power'}, 'cannot be combined'),
               ({'cagey_corrections': {**base['cagey_corrections'],
                                       'D_pow2': {'model_version': nm.ONE_X_TWO_VERSION, 'devig_method': 'proportional'}}},
                'devig_method'),
               ({'cagey_corrections': {**base['cagey_corrections'],
                                       'D_pow2': {'model_version': nm.PRODUCTION_VERSION, 'devig_method': 'power'}}},
                'cannot correct a power grid'),
               ({'cagey_corrections': {**base['cagey_corrections'],
                                       'D': {'model_version': nm.ONE_X_TWO_VERSION, 'devig_method': 'proportional'}}},
                "run's model")]
        for extra, message in bad:
            with self.assertRaisesRegex(ValueError, message, msg=extra):
                v28.correction_models({**base, **extra}, model)
        # Live loads models from narrow_margin_models only: an offline candidate's name can't be put live.
        with self.assertRaises(FileNotFoundError):
            v28.correction_models({**base, 'cagey_corrections': {**base['cagey_corrections'], 'D_pow2': {
                'model_version': nm.CANDIDATE_VERSIONS['power'], 'devig_method': 'power'}}}, model)
        # The power correction without the 1X2 block is not D_pow2.
        from unittest import mock
        with mock.patch.object(nm, 'load', lambda version, directory=nm.MODEL_DIR: nm.json.loads(
                (nm.CANDIDATE_DIR / f"{nm.CANDIDATE_VERSIONS['power']}.json").read_text(encoding='utf-8'))):
            with self.assertRaisesRegex(ValueError, 'carries the 1X2 rule'):
                v28.correction_models(base, model)
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'config.json'
            data = json.loads(v28.CONFIG.read_text(encoding='utf-8-sig'))
            path.write_text(json.dumps({**data, 'cagey_correction_live': {'domestic': 'D_pow2', 'european': 'D_pow2'}}),
                            encoding='utf-8')
            with self.assertRaisesRegex(ValueError, 'UCL and UEL keep D'):
                v28.load_settings(path)

    def test_the_european_leagues_are_the_masters(self):
        import team_research
        config = json.loads((REPO / 'master_reconciliation_config.json').read_text(encoding='utf-8'))
        self.assertEqual(v28.EUROPEAN_LEAGUES, team_research.EUROPEAN_COMPETITIONS)
        self.assertEqual(v28.EUROPEAN_LEAGUES, frozenset(config['european']['leagues']))
        self.assertEqual(v28.correction_scope('UEFA Champions League'), 'european')
        self.assertEqual(v28.correction_scope('English Premier League'), 'domestic')


class LiveTest(unittest.TestCase):
    """The frozen forecast (Brighton v Brentford, 8 Nov 2026) built before and after the release."""

    @classmethod
    def setUpClass(cls):
        cls.row = FROZEN['row']
        cls.before = build(cls.row, before_settings())
        cls.release = build(cls.row, v28.load_settings())
        offline = {**before_settings(), 'devig_method': 'power'}
        cls.offline = v28.build_shortlist(pd.DataFrame([cls.row]), FROZEN['snapshot_generated_utc'],
                                          execution_policy=POLICY, settings=offline, model=nm.load(nm.ONE_X_TWO_VERSION))

    def test_a_run_without_the_switch_is_exactly_the_old_rule(self):
        import importlib
        decisions, summary = self.before[1], self.before[2]
        for column in v28.SHADOW_COLUMNS:
            self.assertNotIn(column, decisions)
        for key in RELEASE_KEYS:
            self.assertNotIn(key, summary)
        # The same as the pipeline's call with the switch absent from the config.
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'config.json'
            data = json.loads(v28.CONFIG.read_text(encoding='utf-8-sig'))
            path.write_text(json.dumps({k: v for k, v in data.items() if k not in RELEASE_KEYS}), encoding='utf-8')
            old = build(self.row, v28.load_settings(path))
        self.assertEqual(old[1].to_csv(index=False), decisions.to_csv(index=False))
        importlib.reload(v28)

    def test_domestic_rows_are_priced_by_d_pow2_exactly_as_the_tested_candidate(self):
        decisions = self.release[1]
        self.assertEqual(set(decisions.cagey_correction.dropna()), {'D_pow2'})
        offline = self.offline[1]
        for column in ('corrected_cagey_score', 'corrected_no_loss_probability', 'corrected_fair_odds'):
            np.testing.assert_allclose(pd.to_numeric(decisions[column], errors='coerce'),
                                       pd.to_numeric(offline[column], errors='coerce'), atol=1e-12, equal_nan=True)
        self.assertFalse(np.allclose(pd.to_numeric(decisions.corrected_no_loss_probability, errors='coerce').fillna(0),
                                     pd.to_numeric(self.before[1].corrected_no_loss_probability, errors='coerce').fillna(0)))

    def test_d_is_kept_in_shadow(self):
        decisions, before = self.release[1], self.before[1]
        priced = decisions.cagey_correction.eq('D_pow2')
        self.assertTrue(priced.any())
        self.assertTrue(decisions.loc[priced, 'shadow_cagey_correction'].eq('D').all())
        shadow = pd.to_numeric(decisions.shadow_corrected_no_loss_probability, errors='coerce')
        d = pd.to_numeric(before.corrected_no_loss_probability, errors='coerce')
        both = priced & shadow.notna() & d.notna()
        self.assertTrue(both.any())
        np.testing.assert_allclose(shadow[both], d[both], atol=1e-15)

    def test_the_value_shortlist_is_unchanged(self):
        key = lambda frame: frame[['home_team', 'away_team', 'market', 'bookmaker', 'offered_decimal_odds']].to_csv(index=False)
        self.assertEqual(key(self.before[0]), key(self.release[0]))
        self.assertEqual(self.before[1].decision.tolist(), self.release[1].decision.tolist())

    def test_ucl_and_uel_rows_keep_d(self):
        for league in sorted(v28.EUROPEAN_LEAGUES):
            before, release = build(self.row, before_settings(), league), build(self.row, v28.load_settings(), league)
            a, b = before[1], release[1]
            self.assertEqual(set(b.cagey_correction.dropna()), {'D'})
            self.assertTrue(b.shadow_corrected_no_loss_probability.isna().all())
            for column in a.columns:
                if column.startswith(('corrected_', 'cagey_tier')):
                    self.assertEqual(a[column].astype(object).map(str).tolist(), b[column].astype(object).map(str).tolist(),
                                     (league, column))

    def test_the_run_records_what_it_used_and_replays_from_its_summary(self):
        summary = self.release[2]
        self.assertEqual(summary['cagey_correction_live'], {'domestic': 'D_pow2', 'european': 'D'})
        self.assertEqual(summary['cagey_corrections'],
                         {'D': {'model_version': nm.PRODUCTION_VERSION, 'devig_method': 'proportional'},
                          'D_pow2': {'model_version': nm.ONE_X_TWO_VERSION, 'devig_method': 'power'}})
        self.assertEqual(summary['cagey_model_version'], nm.PRODUCTION_VERSION)
        for key in RELEASE_KEYS:
            self.assertIn(key, v28.REPLAY_SETTINGS)
        replayed = v28.build_shortlist(
            pd.DataFrame([self.row]), FROZEN['snapshot_generated_utc'], execution_policy=POLICY,
            settings={**{k: summary.get(k) for k in v28.REPLAY_SETTINGS},
                      'price_edge_execution_version': summary.get('price_edge_execution_version', 1),
                      'shortlist_lookahead_hours': summary['shortlist_lookahead_hours']},
            model=nm.load(summary['cagey_model_version']))
        self.assertEqual(replayed[1].to_csv(index=False), self.release[1].to_csv(index=False))
        # A summary from before the release (no switch recorded) replays under D.
        old = {k: v for k, v in summary.items() if k not in RELEASE_KEYS}
        replayed = v28.build_shortlist(
            pd.DataFrame([self.row]), FROZEN['snapshot_generated_utc'], execution_policy=POLICY,
            settings={**{k: old.get(k) for k in v28.REPLAY_SETTINGS},
                      'price_edge_execution_version': old.get('price_edge_execution_version', 1),
                      'shortlist_lookahead_hours': old['shortlist_lookahead_hours']},
            model=nm.load(old['cagey_model_version']))
        self.assertEqual(replayed[1].to_csv(index=False), self.before[1].to_csv(index=False))

    def test_monitoring_records_the_model_that_priced_the_fixture(self):
        monitor = []
        v28.build_shortlist(pd.DataFrame([self.row]), FROZEN['snapshot_generated_utc'], execution_policy=POLICY,
                            settings=v28.load_settings(), model=nm.production_model(), monitor=monitor)
        self.assertEqual({r['model_version'] for r in monitor}, {nm.ONE_X_TWO_VERSION})
        self.assertEqual({r['quintile_model_sha256'] for r in monitor}, {DIGEST})

    def test_the_cagey_tier_is_still_a_pure_market_view(self):
        mirrored = build(independence.mirrored_research(self.row), v28.load_settings())
        cagey = [c for c in self.release[1].columns if c.startswith(('corrected_', 'shadow_', 'cagey_'))]
        self.assertEqual(self.release[1][cagey].to_csv(index=False), mirrored[1][cagey].to_csv(index=False))


def fallback_row(row=None):
    """The frozen forecast with Pinnacle's home price cut from 1.88 to 1.654: the proportional fit B still passes its
    fit check (residual 0.017), the power fit B fails it (0.031 above 0.03) and the power fit A passes, as for the
    two Süper Lig holdout fixtures D_pow2 could not price (residuals 0.0332 and 0.0353)."""
    row = dict(FROZEN['row'] if row is None else row)
    quotes = json.loads(row['price_edge_quotes'])
    for quote in quotes:
        if quote.get('bookmaker') == 'Pinnacle' and quote.get('market') == 'h2h':
            quote['prices']['home'] = 1.654
    return {**row, 'price_edge_quotes': json.dumps(quotes)}


def no_totals_row():
    """The frozen forecast with no Pinnacle O/U 2.5 quote: neither the power nor the proportional fit B exists, and D
    has no corrected distribution (it needs the O/U 2.5 quote), so the fixture has no cagey figures at all."""
    row = dict(FROZEN['row'])
    quotes = [q for q in json.loads(row['price_edge_quotes'])
              if not (q.get('bookmaker') == 'Pinnacle' and q.get('market') == 'totals')]
    return {**row, 'price_edge_quotes': json.dumps(quotes), 'totals_anchor_reference_source': None,
            'market_source_ou25': None}


class FallbackTest(unittest.TestCase):
    """Paul, 17 Nov 2026: where D_pow2's power grid fails its fit check, the fixture is priced by D (D's grid, D's own
    correction), flagged, and counted; D_pow2's correction is never paired with another grid."""

    @classmethod
    def setUpClass(cls):
        cls.row = fallback_row()
        cls.clock = pd.Timestamp(FROZEN['snapshot_generated_utc'])
        cls.pin = v27.pinnacle_quotes(cls.row)
        cls.before = build(cls.row, before_settings())
        cls.monitor = []
        cls.release = v28.build_shortlist(pd.DataFrame([cls.row]), FROZEN['snapshot_generated_utc'],
                                          execution_policy=POLICY, settings=v28.load_settings(),
                                          model=nm.production_model(), monitor=cls.monitor)

    def test_the_fixture_is_the_case_in_question(self):
        proportional, _ = v27.market_fit(self.pin, self.clock, True)
        power, power_info = v27.market_fit(self.pin, self.clock, True, method='power')
        self.assertTrue(proportional.usable)
        self.assertFalse(power.usable)
        self.assertTrue(any(r.startswith('residual') for r in power.reasons))
        # The untested pairing exists: D_pow2's correction on the power fit A would give a figure.
        self.assertTrue(power_info['fit_a'].usable)
        self.assertIsNotNone(v28.corrected_context(self.pin, power, power_info, nm.load(nm.ONE_X_TWO_VERSION), 'power'))

    def test_cagey_basis_falls_back_to_d_and_never_pairs_d_pow2_with_another_grid(self):
        settings = v28.load_settings()
        corrections = v28.correction_models(settings, nm.production_model())
        fit, info = v27.market_fit(self.pin, self.clock, True)
        name, model, method, grid, grid_info, fallback = v28.cagey_basis('D_pow2', corrections, self.pin, fit, info,
                                                                         self.clock, True)
        self.assertEqual((name, model['version'], method), ('D', nm.PRODUCTION_VERSION, 'proportional'))
        self.assertIs(grid, fit)
        self.assertIs(grid_info, info)
        self.assertIn(v28.FALLBACK_REASON, fallback)
        self.assertIn('residual', fallback)
        # A fixture whose power fit passes is D_pow2's, on that fit.
        pin = v27.pinnacle_quotes(FROZEN['row'])
        fit, info = v27.market_fit(pin, self.clock, True)
        name, model, method, grid, _, fallback = v28.cagey_basis('D_pow2', corrections, pin, fit, info, self.clock, True)
        self.assertEqual((name, model['version'], method, grid.usable, fallback),
                         ('D_pow2', nm.ONE_X_TWO_VERSION, 'power', True, None))

    def test_the_fixture_is_priced_by_d_and_flagged(self):
        decisions, before = self.release[1], self.before[1]
        self.assertTrue(len(decisions))
        self.assertEqual(set(decisions.cagey_correction.dropna()), {'D'})
        flags = decisions[v28.FALLBACK_COLUMN]
        self.assertTrue(flags.notna().all())
        self.assertTrue(flags.str.startswith('D_pow2 power grid failed its fit check (residual').all())
        self.assertTrue(decisions.shadow_cagey_correction.isna().all())
        self.assertTrue(decisions.shadow_corrected_no_loss_probability.isna().all())
        for column in before.columns:
            if column.startswith(('corrected_', 'cagey_tier')):
                self.assertEqual(before[column].astype(object).map(str).tolist(),
                                 decisions[column].astype(object).map(str).tolist(), column)
        # The flag reaches the cagey output.
        self.assertIn(v28.FALLBACK_COLUMN, v28.cagey_tier_list(decisions).columns)
        # A fixture D_pow2 prices carries no flag.
        priced = build(FROZEN['row'], v28.load_settings())[1]
        self.assertTrue(priced[v28.FALLBACK_COLUMN].isna().all())
        # Nor does one that neither correction can price (no Pinnacle O/U 2.5): no cagey figures, as before.
        unpriced = build(no_totals_row(), v28.load_settings())[1]
        self.assertTrue(len(unpriced))
        self.assertTrue(unpriced.cagey_correction.isna().all())
        self.assertTrue(unpriced[v28.FALLBACK_COLUMN].isna().all())
        self.assertTrue(pd.to_numeric(unpriced.corrected_cagey_score, errors='coerce').isna().all())

    def test_monitoring_names_ds_model_and_the_report_counts_the_fallback(self):
        self.assertEqual([(r['model_version'], r['quintile_model_sha256']) for r in self.monitor],
                         [(nm.PRODUCTION_VERSION, nm.load_quintiles(nm.production_model())['model_sha256'])])
        summary = self.release[2]
        with self.assertRaises(rm.CageyFallback):
            rm.cagey_contexts(self.row, summary)
        # The archived monitoring records of a D_pow2 run: one fallback, one D_pow2 fixture, one UEFA fixture (D).
        import performance_tracking as pt
        monitor = list(self.monitor)
        for row in (FROZEN['row'], {**FROZEN['row'], 'league': 'UEFA Champions League'},
                    {**no_totals_row(), 'home_team': 'Unpriced'}):
            v28.build_shortlist(pd.DataFrame([row]), FROZEN['snapshot_generated_utc'], execution_policy=POLICY,
                                settings=v28.load_settings(), model=nm.production_model(), monitor=monitor)
        self.assertEqual([(r['model_version'], r['status']) for r in monitor],
                         [(nm.PRODUCTION_VERSION, 'USABLE'), (nm.ONE_X_TWO_VERSION, 'USABLE'),
                          (nm.PRODUCTION_VERSION, 'USABLE'), (nm.PRODUCTION_VERSION, 'UNUSABLE')])
        monitor[1] = {**monitor[1], 'home_team': 'Other'}
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            sha = 'a' * 40
            directory = root / 'performance' / 'snapshots' / sha[:16]
            directory.mkdir(parents=True)
            pt.write_csv(directory / v28.MONITOR_FILE, monitor, v28.MONITOR_COLUMNS)
            meta = {'generated_at_utc': summary['generated_at_utc'], 'git_commit_sha': sha,
                    'sha256': {v28.MONITOR_FILE: '0' * 64}}
            old = {**meta, 'generated_at_utc': '2026-11-10T06:00:00+00:00'}  # a run before the release: not counted
            counts = rm.cagey_fallbacks(root, [(meta, [], []), (old, [], [])],
                                        {summary['generated_at_utc']: summary, old['generated_at_utc']: {}})
        # The unpriced fixture names D's model but is UNUSABLE: not a fallback.
        self.assertEqual(counts, {'runs': 1, 'domestic_records': 3, 'fallback_records': 1, 'domestic_fixtures': 3,
                                  'fallback_fixtures': 1})
        check = {'matches': 0, 'weeks': 0, 'eligible': False, 'triggered': False, 'd_pow2_minus_d_log_loss': None,
                 'interval_95': None, 'rule': 'the rule', 'log_loss': {}, 'coverage': {'fallback_to_D': 1},
                 'graded_fallbacks': 1, 'fallbacks': counts}
        lines = rm.cagey_markdown(check)
        self.assertTrue(any(line.startswith('Fallbacks to D') for line in lines))
        self.assertIn('| 1 | 3 | 1 | 3 | 1 | 1 |', lines)

    def test_inspection_and_the_correction_report_follow_the_same_rule(self):
        import master_inspection
        import master_shortlist
        import narrow_margin_report
        cagey = master_shortlist.cagey_settings(self.release[2])
        self.assertEqual(master_inspection.market_view(self.row, self.clock, nm.PRODUCTION_VERSION, cagey),
                         master_inspection.market_view(self.row, self.clock, nm.PRODUCTION_VERSION))
        evaluated = self.clock.isoformat()
        self.assertIsNone(narrow_margin_report.recompute(self.row, evaluated, nm.ONE_X_TWO_VERSION, True))
        self.assertIsNotNone(narrow_margin_report.recompute(self.row, evaluated, nm.PRODUCTION_VERSION, True))


class MasterInspectionTest(unittest.TestCase):
    def test_the_market_view_uses_the_runs_correction_for_the_fixtures_scope(self):
        import master_inspection
        import master_shortlist
        row, clock = FROZEN['row'], pd.Timestamp(FROZEN['snapshot_generated_utc'])
        summary = build(row, v28.load_settings())[2]
        cagey = master_shortlist.cagey_settings(summary)
        self.assertIsNone(master_shortlist.cagey_settings({'cagey_model_version': nm.PRODUCTION_VERSION}))
        before = master_inspection.market_view(row, clock, nm.PRODUCTION_VERSION)
        after = master_inspection.market_view(row, clock, nm.PRODUCTION_VERSION, cagey)
        pin = v27.pinnacle_quotes(row)
        fit, info = v27.market_fit(pin, clock, True, method='power')
        context = v28.corrected_context(pin, fit, info, nm.load(nm.ONE_X_TWO_VERSION), 'power')
        expected = master_inspection.margin_hda(context['margins'], context['probs'])
        self.assertEqual(after['home_draw_away'], expected)
        self.assertNotEqual(after['home_draw_away'], before['home_draw_away'])
        european = master_inspection.market_view({**row, 'league': 'UEFA Champions League'}, clock,
                                                 nm.PRODUCTION_VERSION, cagey)
        self.assertEqual(european['home_draw_away'], before['home_draw_away'])


class RollbackTriggerTest(unittest.TestCase):
    def test_both_corrections_are_rebuilt_from_the_frozen_quotes_as_the_run_built_them(self):
        row = FROZEN['row']
        selected, decisions, summary = build(row, v28.load_settings())
        built = rm.cagey_contexts(row, summary)
        self.assertEqual(set(built), {'D_pow2', 'D'})
        scores = pd.to_numeric(decisions.corrected_cagey_score, errors='coerce').dropna().unique()
        self.assertEqual(len(scores), 1)
        self.assertAlmostEqual(built['D_pow2'][0]['score'], float(scores[0]), places=12)
        before = pd.to_numeric(build(row, before_settings())[1].corrected_cagey_score, errors='coerce').dropna().unique()
        self.assertAlmostEqual(built['D'][0]['score'], float(before[0]), places=12)
        for context, grid in built.values():
            np.testing.assert_allclose(mi.margin_distribution(grid)[1], context['probs'], atol=1e-12)
        self.assertIsNone(rm._verified(built['D_pow2'][0], [{'cagey_correction': 'D_pow2',
                                                              'corrected_cagey_score': str(scores[0])}]))
        self.assertEqual(rm._verified(built['D_pow2'][0], []), 'unverified')
        self.assertGreater(rm._verified(built['D_pow2'][0], [{'cagey_correction': 'D_pow2',
                                                              'corrected_cagey_score': '0.1'}]), 0)

    def test_only_runs_that_priced_domestic_fixtures_with_d_pow2_are_graded(self):
        summaries = {'2026-11-18T06:00:00+00:00': {'cagey_correction_live': {'domestic': 'D_pow2', 'european': 'D'}},
                     '2026-11-16T06:00:00+00:00': {}}
        meta = lambda when: {'generated_at_utc': when, 'captured_at_utc': when}  # noqa: E731
        archived = [(meta(w), [{'league': 'English Premier League', 'home_team': 'A', 'away_team': 'B'},
                               {'league': 'UEFA Champions League', 'home_team': 'C', 'away_team': 'D'}], [])
                    for w in summaries]
        import performance_tracking as pt
        from unittest import mock
        seen = []

        def graded(frozen, records):
            seen.append((frozen['snapshot_generated_utc'], frozen['league']))
            return {'league_code': 'PL', 'match_id': frozen['home_team']}, None

        with mock.patch.object(pt, 'graded_match', graded):
            latest = rm.latest_cagey_forecasts(archived, [], summaries)
        self.assertEqual(seen, [('2026-11-18T06:00:00+00:00', 'English Premier League')])
        self.assertEqual(set(latest), {('PL', 'A')})

    def test_the_trigger_banner_report_and_activity_line(self):
        check = {'matches': 160, 'weeks': 4, 'eligible': True, 'triggered': True, 'd_pow2_minus_d_log_loss': .004,
                 'interval_95': [.001, .007], 'rule': 'the rule', 'log_loss': {}, 'coverage': {}}
        empty = {'v5_minus_v4_log_loss': None, 'interval_95': None, 'triggered': False, 'eligible': False,
                 'matches': 0, 'weeks': 0, 'rule': ''}
        banner = rm.banner({'rollback': empty, 'cagey': check})
        self.assertTrue(any('D_pow2' in line and rm.TRIGGERED in line and 'cagey_correction_live.domestic' in line
                            for line in banner))
        self.assertEqual(rm.cagey_markdown(check)[0], '## Cagey correction D_pow2 rollback check')
        self.assertTrue(rm.cagey_markdown(check)[6].endswith(f'| {rm.TRIGGERED} |'))
        lines = ma.rollback_checks({'cagey': check}, None)
        self.assertEqual([(l['key'], l['status']) for l in lines], [('rollback:cagey', ma.TRIGGERED)])
        quiet = ma.rollback_checks({'cagey': {**check, 'triggered': False, 'eligible': False, 'matches': 20}}, None)
        self.assertTrue(quiet[0]['status'].startswith('not yet eligible'))
        self.assertEqual((rm.CAGEY_MIN_MATCHES, rm.CAGEY_MIN_WEEKS), (rm.MIN_MATCHES, rm.MIN_WEEKS))


class ActivityTest(unittest.TestCase):
    def test_the_switch_state_carries_the_cagey_correction_and_the_release_is_logged_once(self):
        state = ma.switch_state(REPO / 'master_shortlist_config.json', REPO / 'research_config.json', v28.CONFIG)
        self.assertEqual((state['cagey_domestic'], state['cagey_european']), ('D_pow2', 'D'))
        self.assertIn('cagey correction domestic "D_pow2"', ma.switch_settings_text(state))
        old = {k: v for k, v in state.items() if not k.startswith('cagey')}
        self.assertNotIn('cagey', ma.switch_settings_text(old))
        change = ma.switch_event(old, state)
        self.assertEqual(change['model'], 'cagey correction')
        self.assertIn('cagey_domestic not set → D_pow2', change['outcome'])
        release = ma.cagey_release_event([], state)
        self.assertEqual((release['event'], release['key']), (ma.RELEASE, 'release:cagey correction D_pow2'))
        self.assertIsNone(ma.cagey_release_event([release], state))
        self.assertIsNone(ma.cagey_release_event([], {**state, 'cagey_domestic': 'D'}))
        # A config without the switch is D everywhere.
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'cagey.json'
            path.write_text('{}', encoding='utf-8')
            plain = ma.switch_state(REPO / 'master_shortlist_config.json', REPO / 'research_config.json', path)
        self.assertEqual((plain['cagey_domestic'], plain['cagey_european']), ('D', 'D'))

    def test_a_forecast_run_logs_the_switch_and_the_release(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp)
            log = [ma.event(ma.SWITCH, 'research', 'x', 'x', key='switches', source=ma.SOURCE_FORECAST,
                            data={'state_after': ma.switch_state(REPO / 'master_shortlist_config.json',
                                                                 REPO / 'research_config.json')})]
            events = ma.forecast_events(log, out, REPO / 'master_shortlist_config.json', REPO / 'research_config.json',
                                        '2026-11-18T06:00:00Z', v28.CONFIG)
            kinds = [(e['event'], e['key']) for e in events]
            self.assertIn((ma.SWITCH, 'switches'), kinds)
            self.assertIn((ma.RELEASE, 'release:cagey correction D_pow2'), kinds)
            again = ma.forecast_events(log + events, out, REPO / 'master_shortlist_config.json',
                                       REPO / 'research_config.json', '2026-11-18T08:00:00Z', v28.CONFIG)
            self.assertEqual(again, [])


if __name__ == '__main__':
    unittest.main()
