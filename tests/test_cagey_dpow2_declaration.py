"""D_pow2 as a harness candidate and its holdout declaration (docs/plan.md, Phase 3b-2; Paul, 17 Nov 2026).

  * D_pow2 is registered apart from the standing candidates and computed only when asked or declared: a plain
    run fits and scores exactly what it did before;
  * the harness grid is PR #184's: the power-method market grid, the correction fitted on that grid, the 1X2 set
    from the power quote with a and b as fitted; the model file is pinned;
  * it may be declared against D only, under the cagey events rule, and the new deciding criterion
    (calibration_and_point_estimates) needs the sample minimum, the events rule judged against M on the rule's
    own events, and both point estimates against D not negative;
  * declarations of D against M and every log-loss declaration read as before.

No real holdout result is read: the one harness run over holdout fixtures has every holdout result blanked, and
the verdict tests use made-up scores.
"""
from __future__ import annotations

import json
from pathlib import Path
import tempfile
import unittest
from unittest import mock

import numpy as np
import pandas as pd

import evaluation_harness as eh
import market_implied as mi
import narrow_margin as nm
from tests.test_cagey_events_rule import priced

REPO = Path(__file__).resolve().parents[1]
CFG = json.loads((REPO / 'evaluation_harness_config.json').read_text(encoding='utf-8'))
PATH = REPO / 'evaluation' / 'declarations' / 'cagey_dpow2_holdout.json'
NAME = 'cagey-events-v1'
RULE = CFG['calibration_tolerance_rules']['rules'][NAME]
V2 = CFG['calibration_tolerance']['name']
MODEL_DIGEST = '82cf7306eee5bdfda21c4fb37d367e6e8b1bf9171415f5acacc3f4827b7123af'
# The match results (football-data columns); everything else in a row is identity or a pre-match price.
RESULTS = ('FTHG', 'FTAG', 'FTR', 'HTHG', 'HTAG', 'HTR', 'HS', 'AS', 'HST', 'AST', 'HF', 'AF', 'HC', 'AC',
           'HY', 'AY', 'HR', 'AR')


class RegistrationTest(unittest.TestCase):
    def test_d_pow2_is_registered_apart_from_the_standing_candidates(self):
        self.assertEqual(list(eh.CAGEY_CANDIDATES), ['D_pow2'])
        self.assertNotIn('D_pow2', eh.CANDIDATES)
        self.assertIn('narrow_margin_models/candidates/cagey-correction-through-2425-power-1x2-v1.json', eh.SETUP_FILES)
        self.assertIn('narrow_margin_models/cagey-correction-through-2425-v1.json', eh.SETUP_FILES)
        self.assertEqual(eh.CAGEY_EVENT_CANDIDATES, ('D', 'M'))

    def test_its_model_is_pr_184s_fit_and_only_valid_on_the_power_grid(self):
        models = eh.cagey_candidate_models(['D_pow2'])
        model, method = models['D_pow2']
        self.assertEqual(method, mi.DEVIG_POWER)
        self.assertEqual(model['version'], 'cagey-correction-through-2425-power-1x2-v1')
        self.assertEqual(nm.model_digest(model), MODEL_DIGEST)
        spec = nm.one_x_two(model)
        self.assertEqual((round(spec['a'], 6), round(spec['b'], 6)), (0.029140, -0.060942))
        # Fitted on the correction's own rows, which end before validation starts: nothing later.
        self.assertEqual((spec['training_matches'], model['training_matches']), (10956, 10956))
        self.assertEqual((model['training_last_date'], model['training_until_exclusive']), ('2025-06-01', '2025-07-01'))
        self.assertEqual(model['training_until_exclusive'], CFG['development_end'])
        # D_pow's correction, coefficient for coefficient.
        power = nm.load(nm.CANDIDATE_VERSIONS[mi.DEVIG_POWER], nm.CANDIDATE_DIR)
        self.assertEqual(model['targets'], power['targets'])
        # Never the production coefficients on the power grid, nor this model on the proportional grid.
        prices = eh.book_prices(priced(), 'pinnacle')
        with self.assertRaisesRegex(ValueError, 'cannot correct'):
            eh.cagey_matrix(eh.market_matrix(prices), prices, model)
        with self.assertRaisesRegex(ValueError, 'cannot correct'):
            eh.cagey_matrix(eh.market_matrix(prices, mi.DEVIG_POWER), prices, nm.production_model(), mi.DEVIG_POWER)
        self.assertEqual(eh.cagey_candidate_models(()), {})
        with self.assertRaisesRegex(ValueError, 'not a registered cagey candidate'):
            eh.cagey_candidate_models(['D_pow'])

    def test_only_locked_historical_runs_take_the_flag(self):
        with tempfile.TemporaryDirectory() as tmp:
            for extra in (['--declaration', str(PATH)], ['--mode', 'european'], ['--mode', 'master']):
                with self.assertRaisesRegex(ValueError, 'locked historical runs only'):
                    eh.main(['--output', str(Path(tmp) / 'out'), '--cagey-candidates', 'D_pow2', *extra])
            self.assertFalse((Path(tmp) / 'out').exists())


class HistoricalForwardingTest(unittest.TestCase):
    """historical() asks evaluate_league for D_pow2 only when asked for or declared, and otherwise calls it
    exactly as before (same arguments)."""

    def calls(self, **kwargs):
        from tests.test_research_c8_variants import InlinePool
        seen = []

        def league(*args):
            seen.append(args)
            return [], [], {}, [], [], [], []

        with mock.patch.object(eh, 'ProcessPoolExecutor', InlinePool), mock.patch.object(eh, 'evaluate_league', league):
            eh.historical('cache', CFG, leagues=['EPL'], **kwargs)
        return seen

    def test_default_asked_and_declared_calls(self):
        self.assertEqual(self.calls(), [('EPL', 'cache', CFG, False, None)])
        self.assertEqual(self.calls(cagey=['D_pow2']), [('EPL', 'cache', CFG, False, None, None, ('D_pow2',))])
        keep = {'D_pow2', 'D', 'M'}
        self.assertEqual(self.calls(include_holdout=True, keep=keep),
                         [('EPL', 'cache', CFG, True, keep, None, ('D_pow2',))])
        # A declaration of anything else never computes it.
        self.assertEqual(self.calls(include_holdout=True, keep={'C8', 'C6', 'M'}),
                         [('EPL', 'cache', CFG, True, {'C8', 'C6', 'M'})])


class HarnessRunTest(unittest.TestCase):
    """Real Eredivisie folds across the holdout start, with every holdout result blanked."""

    @classmethod
    def setUpClass(cls):
        # Two fold windows across the holdout start (16 Jan 2026): 10-11 Jan is validation, 17-18 Jan holdout.
        cls.cfg = cfg = {**CFG, 'test_start': '2026-01-05', 'end_exclusive': '2026-01-19',
                         'seasons': ['2324', '2425', '2526']}
        cls.cache = str(REPO / '.football_cache')
        load = eh.hb.load_history
        cls.held, cls.rows = set(), {}

        def without_holdout_results(cache_dir, league, load_cfg):
            data, sources, extra = load(cache_dir, league, load_cfg)
            locked = data.Date.map(lambda d: eh.phase(d, league, cfg) == 'holdout')
            data = data.copy()
            data.loc[locked, [c for c in RESULTS if c in data]] = np.nan
            for _, row in data.loc[(data.Date >= cfg['test_start']) & (data.Date < cfg['end_exclusive'])].iterrows():
                cls.rows[eh.fixture_key(league, row)] = row
            cls.held = {eh.fixture_key(league, row) for _, row in data.loc[
                locked & (data.Date >= cfg['test_start']) & (data.Date < cfg['end_exclusive'])].iterrows()}
            return data, sources, extra

        score = eh.rb.score_fixture
        cls.grids, cls.scored = {}, []

        def keeping_grids(identity, matrices, home_goals, away_goals):
            cls.grids.setdefault(identity['fixture_key'], {}).update(matrices)
            if identity['phase'] == 'holdout':  # identities only: a holdout fixture is never scored here
                cls.scored.append((identity['fixture_key'], home_goals, away_goals))
                return [{**identity, 'candidate': c} for c in matrices]
            return score(identity, matrices, home_goals, away_goals)

        with mock.patch.object(eh.hb, 'load_history', without_holdout_results), \
                mock.patch.object(eh.rb, 'score_fixture', keeping_grids):
            cls.plain = eh.evaluate_league('Eredivisie', cls.cache, cfg, False)
            cls.asked = eh.evaluate_league('Eredivisie', cls.cache, cfg, False, cagey=('D_pow2',))
            cls.declared = eh.evaluate_league('Eredivisie', cls.cache, cfg, True, keep={'D_pow2', 'D', 'M'},
                                              cagey=('D_pow2',))

    def test_a_plain_run_is_unchanged_and_never_computes_the_candidate(self):
        records, folds, coverage, overrounds, sources, calib, research = self.plain
        self.assertTrue(records)
        self.assertNotIn('D_pow2', {r['candidate'] for r in records})
        self.assertFalse([k for k in coverage if 'D_pow2' in k])
        asked = self.asked
        # With the candidate asked for, everything else is the same, record for record and in the same order.
        self.assertEqual([r for r in asked[0] if r['candidate'] != 'D_pow2'], records)
        self.assertEqual([r for r in asked[5] if r['candidate'] != 'D_pow2'], calib)
        self.assertEqual({k: v for k, v in asked[2].items() if 'D_pow2' not in k}, dict(coverage))
        self.assertEqual((asked[1], asked[3], asked[4], asked[6]), (folds, overrounds, sources, research))

    def test_the_grid_is_pr_184s_construction_on_the_same_prices(self):
        records, _, coverage, _, _, calib, _ = self.asked
        mine = [r for r in records if r['candidate'] == 'D_pow2']
        self.assertTrue(mine)
        self.assertEqual({r['phase'] for r in mine}, {'validation'})
        self.assertEqual({r['market'] for r in mine}, {r['market'] for r in records if r['candidate'] == 'D'})
        self.assertEqual(coverage['Eredivisie:D_pow2:available'], coverage['Eredivisie:D:available'])
        model = nm.load(nm.ONE_X_TWO_VERSION, nm.CANDIDATE_DIR)
        keys = {r['fixture_key'] for r in mine}
        for key in keys:
            row = self.rows[key]
            prices = eh.book_prices(row, eh.period_book(row.Date, self.cfg))
            m_pow = eh.market_matrix(prices, mi.DEVIG_POWER)
            np.testing.assert_array_equal(self.grids[key]['D_pow2'], eh.cagey_matrix(m_pow, prices, model, mi.DEVIG_POWER))
            # Its 1X2 is the rule's target on the power quote, and it is not today's cagey grid.
            h, a = np.indices(m_pow.shape)
            grid = self.grids[key]['D_pow2']
            target = nm.one_x_two_target(nm.one_x_two(model), *mi.devig_three_way(*prices['hda'], method=mi.DEVIG_POWER))
            np.testing.assert_allclose([grid[h > a].sum(), grid[h == a].sum(), grid[h < a].sum()], target, atol=1e-9)
            self.assertFalse(np.array_equal(grid, self.grids[key]['D']))
        # Its calibration rows carry what the events rule needs, as D's and M's do.
        cagey = [r for r in calib if r['candidate'] == 'D_pow2']
        self.assertEqual(len(cagey), len(keys))
        self.assertTrue(all('cagey' in r for r in cagey))
        events = eh.cagey_events(calib, RULE)
        self.assertTrue(events[['p_D', 'p_M', 'p_D_pow2']].notna().all(axis=None))
        self.assertNotIn('p_D_pow2', eh.cagey_events(self.plain[5], RULE))
        checks = eh.cagey_events_checks(calib, RULE)
        self.assertEqual(set(checks['validation']), {'D', 'M', 'D_pow2'})
        self.assertEqual(checks['validation']['D_pow2']['baseline'], 'M')
        plain = eh.cagey_events_checks(self.plain[5], RULE)
        self.assertEqual({k: checks['validation'][k] for k in ('D', 'M')}, plain['validation'])

    def test_a_declared_run_computes_only_the_holdout_for_the_three_grids_and_reads_no_result(self):
        records = self.declared[0]
        holdout = [r for r in records if r['phase'] == 'holdout']
        self.assertEqual(len(self.held), 9)
        self.assertEqual({r['fixture_key'] for r in holdout}, self.held)
        self.assertEqual({r['candidate'] for r in holdout}, {'D_pow2', 'D', 'M'})
        self.assertEqual({r['market_book'] for r in holdout}, {'bet365'})
        self.assertTrue({r['candidate'] for r in records if r['phase'] != 'holdout'} <= {'MP', 'MB'})
        blank = [(h, a) for key, h, a in self.scored if key in self.held]
        self.assertEqual(len(blank), len(self.held))
        self.assertTrue(all(np.isnan(h) and np.isnan(a) for h, a in blank))
        # On the holdout the grids are built from Bet365's quote.
        model = nm.load(nm.ONE_X_TWO_VERSION, nm.CANDIDATE_DIR)
        for key in self.held:
            prices = eh.book_prices(self.rows[key], 'bet365')
            np.testing.assert_array_equal(self.grids[key]['D_pow2'], eh.cagey_matrix(
                eh.market_matrix(prices, mi.DEVIG_POWER), prices, model, mi.DEVIG_POWER))
        # A locked run with the candidate asked for never reaches a holdout fixture.
        self.assertFalse(self.held & {r['fixture_key'] for r in self.asked[0]})


class DeclarationTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.dir = Path(self.tmp.name)
        self.ledger = self.dir / 'ledger.json'
        self.setup = {'sha256': 'c' * 64}

    def declaration(self, **extra):
        data = {'candidate': 'D_pow2', 'baseline': 'D', 'primary_metric': 'AH all', 'draw_sensitive_lines': [-0.5, 0, 0.5],
                'calibration_tolerance': NAME, 'deciding_criterion': eh.POINT_ESTIMATES,
                'sample_minimum': {'fixtures': 300, 'weeks': 6}, 'declared_by': 'Paul', 'declared_at': '2026-11-17'}
        data.update(extra)
        data = {k: v for k, v in data.items() if v is not ...}
        path = self.dir / 'declaration.json'
        path.write_text(json.dumps(data), encoding='utf-8')
        return path

    def declared(self, **extra):
        return eh.validate_declaration(self.declaration(**extra), CFG, self.setup, self.ledger)

    def test_the_criterion_is_named_and_the_declaration_validates(self):
        self.assertEqual(eh.DECIDING_CRITERIA, ('log_loss_superiority', 'calibration', 'calibration_and_point_estimates'))
        declared = self.declared()
        self.assertEqual((declared['candidate'], declared['baseline']), ('D_pow2', 'D'))
        self.assertEqual(declared['calibration_rule'], RULE)
        self.assertEqual(declared['deciding_criterion'], 'calibration_and_point_estimates')

    def test_bad_declarations_are_refused(self):
        bad = [({'baseline': 'M'}, 'judges D against M only'),
               ({'baseline': 'C'}, 'judges D against M only'),
               ({'candidate': 'D', 'baseline': 'D_pow2'}, 'cannot be the baseline'),
               ({'candidate': 'M', 'baseline': 'D_pow2'}, 'cannot be the baseline'),
               ({'calibration_tolerance': V2}, 'must be declared under a cagey events rule'),
               ({'calibration_tolerance': V2, 'deciding_criterion': ...}, 'must be declared under a cagey events rule'),
               ({'primary_metric': '1X2'}, "primary metric must be 'AH all'"),
               ({'sample_minimum': ...}, 'sample minimum'),
               ({'sample_minimum': {'fixtures': 250, 'weeks': 6}}, 'sample minimum'),
               ({'reported_not_deciding': ['ROI']}, 'reported_not_deciding'),
               ({'candidate': 'D_pow'}, 'registered in the harness'),
               ({'deciding_criterion': 'point_estimates'}, 'Deciding criterion')]
        for extra, message in bad:
            with self.assertRaisesRegex(ValueError, message, msg=extra):
                self.declared(**extra)
        # The European registry does not know it.
        with self.assertRaisesRegex(ValueError, 'registered in the harness'):
            eh.validate_declaration(self.declaration(), CFG, self.setup, self.ledger, eh.EUROPEAN_CANDIDATES)

    def test_the_committed_declaration_is_what_was_decided_and_the_ledger_accepts_d_as_the_baseline(self):
        data = json.loads(PATH.read_text(encoding='utf-8'))
        self.assertEqual((data['candidate'], data['baseline'], data['market_reference']), ('D_pow2', 'D', 'M'))
        self.assertEqual((data['deciding_criterion'], data['calibration_tolerance']), (eh.POINT_ESTIMATES, NAME))
        self.assertEqual((data['primary_metric'], data['draw_sensitive_lines']), ('AH all', [-0.5, 0.0, 0.5]))
        self.assertIn(MODEL_DIGEST, data['candidate_definition'])
        for phrase in ('built from Bet365 quotes', 'safety check', 'not a measure of the live effect'):
            self.assertIn(phrase, data['bet365_note'])
        self.assertEqual(set(data['outcomes']), {'release', 'no_release'})
        declared = eh.validate_declaration(PATH, CFG, self.setup, self.ledger)
        self.assertEqual(declared['calibration_rule'], RULE)
        # The real ledger holds D as a scored candidate; D as the baseline is accepted, and D_pow2 is locked
        # once it has been scored.
        entries = json.loads(eh.LEDGER.read_text(encoding='utf-8'))
        self.assertIn('D', {e['candidate'] for e in entries})
        before = self.dir / 'before.json'
        before.write_text(json.dumps([e for e in entries if e['candidate'] != 'D_pow2']), encoding='utf-8')
        eh.validate_declaration(PATH, CFG, self.setup, before)
        eh.record_holdout(declared, self.setup, 'abc', 638, {'passes_holdout_gate': False}, before)
        entry = json.loads(before.read_text(encoding='utf-8'))[-1]
        self.assertEqual((entry['candidate'], entry['baseline'], entry['deciding_criterion'], entry['calibration_tolerance']),
                         ('D_pow2', 'D', eh.POINT_ESTIMATES, NAME))
        with self.assertRaisesRegex(ValueError, "already scored for candidate 'D_pow2'"):
            eh.validate_declaration(PATH, CFG, {'sha256': 'd' * 64}, before)

    def test_earlier_declarations_read_as_before(self):
        d = eh.validate_declaration(REPO / 'evaluation/declarations/cagey_d_holdout.json', CFG, self.setup, self.ledger)
        self.assertEqual(d['sha256'], 'd464bc071c6aedc558593dbb8f0a30279cfc945fd57a1b51ad2157ed07b5604b')
        c6 = eh.validate_declaration(REPO / 'evaluation/declarations/c6_holdout.json', CFG, self.setup, self.ledger)
        self.assertEqual(c6['sha256'], '675bbf54924920f28ba6d2c35a70fb5e61821ef649319512f92ca3fb24fd1be0')

    # --- the verdict -----------------------------------------------------------------------------------

    @staticmethod
    def holdout(n_weeks=10, per_week=40, losses=None, seed=4, without_candidate=0):
        """Holdout AH records for D, M and D_pow2 (made-up log losses per line) and calibration rows with cagey
        inputs from real grids priced from Bet365-style quotes. `losses`: {candidate: {market: log loss}}.
        The first `without_candidate` fixtures have no D_pow2 forecast."""
        losses = losses or {}
        rng = np.random.default_rng(seed)
        production, candidate = nm.production_model(), nm.load(nm.ONE_X_TWO_VERSION, nm.CANDIDATE_DIR)
        records, calib = [], []
        i = 0
        while i < n_weeks * per_week:
            home = float(rng.uniform(.36, .50))
            row = priced(AHh=-0.25, B365H=1 / (home * 1.05), B365D=1 / (.27 * 1.05), B365A=1 / ((.73 - home) * 1.05),
                         B365AHH=1.9, B365AHA=1.95)
            prices = eh.book_prices(row, 'bet365')
            try:
                m = eh.market_matrix(prices)
                m_pow = eh.market_matrix(prices, mi.DEVIG_POWER)
            except ValueError:
                continue  # the fixed main line doesn't fit these 1X2 prices
            grids = {'D': eh.cagey_matrix(m, prices, production), 'M': m,
                     'D_pow2': eh.cagey_matrix(m_pow, prices, candidate, mi.DEVIG_POWER)}
            margins, probs = mi.margin_distribution(grids['D_pow2'])
            margin = int(rng.choice(margins, p=probs / probs.sum()))
            key, week = f'f{i:04d}', f'2026-W{i // per_week:02d}'
            for cand, grid in grids.items():
                if cand == 'D_pow2' and i < without_candidate:
                    continue
                for market in ('AH +0.00', 'AH +1.50'):
                    loss = losses.get(cand, {}).get(market, .70)
                    records.append({'fixture_key': key, 'league': 'Eredivisie', 'week': week, 'phase': 'holdout',
                                    'candidate': cand, 'market': market, 'log_loss': loss})
                calib.append({'phase': 'holdout', 'fixture_key': key, 'candidate': cand, 'probs': [.4, .3, .3],
                              'outcome': 0, 'cagey': eh.cagey_inputs(grid, prices, 'bet365', week, margin)})
            i += 1
        return records, calib

    def passing(self, **extra):
        """The declaration with the events rule made to pass whatever the slopes and bands are."""
        return {**self.declared(**extra), 'calibration_rule': {**RULE, 'slope_min': -100., 'slope_max': 100.,
                                                               'band_max_deviation': 1.}}

    BETTER = {'D_pow2': {'AH +0.00': .69, 'AH +1.50': .69}}
    # Draw-sensitive worse (-0.01), all lines better (+0.015): the level line is in both groups.
    DRAW_WORSE = {'D_pow2': {'AH +0.00': .71, 'AH +1.50': .66}}

    def test_it_passes_on_the_events_rule_and_both_point_estimates_not_negative(self):
        records, calib = self.holdout(losses=self.BETTER)
        verdict = eh.holdout_verdict(records, calib, self.passing(), {})
        self.assertEqual(verdict['deciding_criterion'], 'calibration_and_point_estimates')
        self.assertTrue(verdict['sample_minimum_met'] and verdict['calibration']['passes'])
        self.assertAlmostEqual(verdict['primary']['mean_gain'], .01)
        self.assertAlmostEqual(verdict['draw_sensitive']['mean_gain'], .01)
        self.assertEqual(verdict['point_estimates']['not_negative'], {'AH all': True, 'AH draw-sensitive': True})
        self.assertTrue(verdict['passes_holdout_gate'])
        self.assertIn('interval reported, not deciding', verdict['primary_metric_role'])
        # The events rule is the rule's own: D chooses the side, M prices, and M is what D_pow2 is judged against.
        self.assertEqual((verdict['calibration']['candidate'], verdict['calibration']['baseline']), ('D_pow2', 'M'))
        self.assertEqual(verdict['calibration_judged_against'], 'M')
        self.assertEqual((verdict['baseline_calibration']['candidate'], verdict['baseline_calibration']['baseline']), ('D', 'M'))
        self.assertEqual((verdict['price_basis_calibration']['candidate'], verdict['price_basis_calibration']['baseline']),
                         ('M', 'M'))
        self.assertEqual(set(verdict['calibration']['families']), {'narrow', 'no_loss'})

    def test_the_intervals_do_not_decide_and_zero_is_not_negative(self):
        records, calib = self.holdout()  # identical scores: both point estimates exactly zero
        verdict = eh.holdout_verdict(records, calib, self.passing(), {})
        self.assertEqual((verdict['primary']['mean_gain'], verdict['draw_sensitive']['mean_gain']), (0., 0.))
        self.assertFalse(verdict['primary']['clear_of_zero'])
        self.assertTrue(verdict['passes_holdout_gate'])
        # The same data under log-loss superiority could not pass.
        superiority = eh.holdout_verdict(records, calib, {**self.passing(), 'deciding_criterion': 'log_loss_superiority'}, {})
        self.assertFalse(superiority['passes_holdout_gate'])

    def test_either_point_estimate_negative_fails(self):
        records, calib = self.holdout(losses=self.DRAW_WORSE)
        verdict = eh.holdout_verdict(records, calib, self.passing(), {})
        self.assertAlmostEqual(verdict['primary']['mean_gain'], .015)
        self.assertAlmostEqual(verdict['draw_sensitive']['mean_gain'], -.01)
        self.assertEqual(verdict['point_estimates']['not_negative'], {'AH all': True, 'AH draw-sensitive': False})
        self.assertFalse(verdict['passes_holdout_gate'])
        records, calib = self.holdout(losses={'D_pow2': {'AH +0.00': .69, 'AH +1.50': .73}})
        verdict = eh.holdout_verdict(records, calib, self.passing(), {})
        self.assertEqual(verdict['point_estimates']['not_negative'], {'AH all': False, 'AH draw-sensitive': True})
        self.assertFalse(verdict['passes_holdout_gate'])

    def test_a_failed_events_rule_or_a_short_sample_fails_whatever_the_log_loss(self):
        records, calib = self.holdout(losses=self.BETTER)
        failing = {**self.declared(), 'calibration_rule': {**RULE, 'families': ['narrow', 'no_loss', 'absent']}}
        verdict = eh.holdout_verdict(records, calib, failing, {})  # a family with no events fails the rule
        self.assertFalse(verdict['calibration']['passes'])
        self.assertTrue(verdict['point_estimates']['all_not_negative'])
        self.assertFalse(verdict['passes_holdout_gate'])
        records, calib = self.holdout(n_weeks=5, losses=self.BETTER)  # 200 fixtures: below 300
        verdict = eh.holdout_verdict(records, calib, self.passing(), {})
        self.assertFalse(verdict['sample_minimum_met'])
        self.assertFalse(verdict['passes_holdout_gate'])

    def test_all_three_are_judged_on_the_events_the_candidate_forecasts(self):
        records, calib = self.holdout(losses=self.BETTER, without_candidate=50)
        verdict = eh.holdout_verdict(records, calib, self.passing(), {})
        self.assertEqual(verdict['primary']['fixtures'], 350)
        narrow = {k: verdict[k]['families']['narrow'] for k in ('calibration', 'baseline_calibration', 'price_basis_calibration')}
        self.assertEqual({v['events'] for v in narrow.values()}, {350})
        self.assertEqual(narrow['calibration']['baseline_slope'], narrow['price_basis_calibration']['slope'])
        # D against M reads as before: every event of the rule, M against itself as the baseline's check.
        d = eh.validate_declaration(REPO / 'evaluation/declarations/cagey_d_holdout.json', CFG, self.setup, self.ledger)
        d_verdict = eh.holdout_verdict(records, calib, d, {})
        self.assertEqual(d_verdict['calibration']['families']['narrow']['events'], 400)
        self.assertEqual((d_verdict['baseline_calibration']['candidate'], d_verdict['baseline_calibration']['baseline']),
                         ('M', 'M'))
        self.assertNotIn('point_estimates', d_verdict)
        self.assertNotIn('calibration_judged_against', d_verdict)
        self.assertEqual(d_verdict['passes_holdout_gate'], d_verdict['calibration']['passes'])


if __name__ == '__main__':
    unittest.main()
