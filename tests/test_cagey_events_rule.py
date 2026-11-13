"""Calibration rule cagey-events-v1 (decided 12 Nov 2026): the cagey tier's events, D against M."""
import json
from pathlib import Path
import unittest

import numpy as np
import pandas as pd

import evaluation_harness as eh
from ah_close_backtest import effective_probability, expected_return, outcome_probabilities, settle

REPO = Path(__file__).resolve().parents[1]
CFG = json.loads((REPO / 'evaluation_harness_config.json').read_text(encoding='utf-8'))
NAME = 'cagey-events-v1'
RULE = CFG['calibration_tolerance_rules']['rules'][NAME]
V3 = CFG['calibration_tolerance_rules']['rules']['slopes-0.90-1.10-or-closer-than-baseline-bands-30-5pp-bonferroni-v3']


def priced(**extra):
    row = {'PSH': 2.1, 'PSD': 3.4, 'PSA': 3.6, 'P>2.5': 1.95, 'P<2.5': 1.95, 'AHh': -0.25, 'PAHH': 1.95, 'PAHA': 1.97,
           'B365H': 2.05, 'B365D': 3.3, 'B365A': 3.5, 'B365>2.5': 1.9, 'B365<2.5': 1.9, 'B365AHH': 1.9, 'B365AHA': 1.95}
    return {**row, **extra}


def fixture(book='pinnacle', margin=0, row=None):
    """Real D and M cagey inputs for one priced match."""
    import narrow_margin as nm
    prices = eh.book_prices(row or priced(), book)
    m = eh.market_matrix(prices)
    d = eh.cagey_matrix(m, prices, nm.production_model())
    return (eh.cagey_inputs(d, prices, book, '2025-W40', margin), eh.cagey_inputs(m, prices, book, '2025-W40', margin))


class ConfigTest(unittest.TestCase):
    def test_the_rule_is_configured_as_decided(self):
        self.assertEqual(RULE['name'], NAME)
        self.assertEqual(RULE['kind'], 'cagey_events')
        self.assertEqual(RULE['decided'], '2026-11-12')
        self.assertEqual((RULE['event_selector'], RULE['price_basis']), ('D', 'M'))
        self.assertEqual(RULE['families'], ['narrow', 'no_loss'])
        import asian_handicap
        self.assertEqual(tuple(RULE['lines']), asian_handicap.LINES)
        self.assertEqual(len(RULE['lines']), 25)
        self.assertEqual((RULE['odds_window']['min_exclusive'], RULE['odds_window']['max_inclusive']), (1.15, 2.0))
        self.assertEqual(set(RULE['synthetic_ah_margin']) - {'script'}, set(eh.BOOKS))
        # v3's logic: the same slope band, relative slopes and Bonferroni bands.
        for key in ('slope_min', 'slope_max', 'slope_relative_to_baseline', 'band_width', 'band_min_matches',
                    'band_max_deviation', 'band_alpha'):
            self.assertEqual(RULE[key], V3[key], key)

    def test_v2_and_v3_are_unchanged_and_stay_1x2_rules(self):
        rules = eh.calibration_rules(CFG)
        self.assertEqual(set(rules), {CFG['calibration_tolerance']['name'], V3['name'], NAME})
        self.assertTrue(eh.is_1x2_rule(rules[CFG['calibration_tolerance']['name']]) and eh.is_1x2_rule(V3))
        self.assertFalse(eh.is_1x2_rule(RULE))
        with self.assertRaisesRegex(ValueError, 'not a 1X2 rule'):
            eh.calibration_check([{'probs': [.4, .3, .3], 'outcome': 0, 'fixture_key': 'f'}], RULE, [])

    def test_the_v5_odds_window_is_the_one_the_rule_uses(self):
        import inspect
        import cagey_tier_v3
        self.assertIn('1.15 < price <= 2.0', inspect.getsource(cagey_tier_v3.annotate))


class EventTest(unittest.TestCase):
    def test_lines_share_the_no_loss_event_of_their_floor(self):
        expected = {-3.0: -3, -2.75: -3, -2.25: -3, -2.0: -2, -1.25: -2, -1.0: -1, -0.25: -1, 0.0: 0, 0.25: 0,
                    0.75: 0, 1.0: 1, 1.75: 1, 2.0: 2, 2.75: 2, 3.0: 3}
        for line, k in expected.items():
            self.assertEqual(eh.no_loss_family(line), k, line)
        # 'No loss' at any line of family k is exactly 'side margin >= -k' (lost == 0).
        margins = np.arange(-8, 9)
        for line in RULE['lines']:
            _, lost = settle(margins, line)
            np.testing.assert_array_equal(lost == 0, margins >= -eh.no_loss_family(line), err_msg=str(line))

    def test_event_probability_is_the_no_loss_probability_of_every_line_in_the_family(self):
        d, m = fixture()
        for inputs in (d, m):
            margins, probs = np.asarray(inputs['margins']), np.asarray(inputs['margin_probs'])
            self.assertAlmostEqual(probs.sum(), 1, places=9)
            for side in ('home', 'away'):
                sm = margins if side == 'home' else -margins
                for line in RULE['lines']:
                    out = outcome_probabilities(sm, probs, line)
                    event = {'family': 'no_loss', 'side': side, 'k': eh.no_loss_family(line)}
                    self.assertAlmostEqual(eh.cagey_event_probability(event, inputs),
                                           out['p_win'] + out['p_half_win'] + out['p_push'], places=12)
            self.assertAlmostEqual(eh.cagey_event_probability({'family': 'narrow'}, inputs),
                                   probs[np.abs(margins) <= 1].sum(), places=12)

    def test_main_line_at_the_real_quote_and_other_lines_at_m_fair_plus_the_books_margin(self):
        for book, (home, away) in (('pinnacle', (1.95, 1.97)), ('bet365', (1.9, 1.95))):
            d, m = fixture(book)
            bettable = eh.cagey_bettable(d, m, RULE)
            margin = RULE['synthetic_ah_margin'][book]['margin']
            sm = {'home': np.asarray(m['margins']), 'away': -np.asarray(m['margins'])}
            seen = set()
            for side, lines in bettable.items():
                for line, price, ev in lines:
                    seen.add((side, line))
                    if (side, line) in (('home', -0.25), ('away', 0.25)):
                        self.assertEqual(price, home if side == 'home' else away)
                    else:
                        q = effective_probability(outcome_probabilities(sm[side], np.asarray(m['margin_probs']), line))
                        self.assertAlmostEqual(price, 1 / (q * (1 + margin)), places=12)
                    self.assertTrue(1.15 < price <= 2.0)
                    self.assertAlmostEqual(ev, expected_return(
                        outcome_probabilities(sm[side], np.asarray(d['margin_probs']), line), price), places=12)
            self.assertIn(('home', -0.25), seen)
            self.assertIn(('away', 0.25), seen)
            # Lines priced outside the window are not bettable: e.g. home +3.00 (near-certain no loss).
            self.assertNotIn(('home', 3.0), seen)

    def test_the_bookmaker_margin_moves_the_synthetic_prices(self):
        d, m = fixture('pinnacle')
        wide = {**RULE, 'synthetic_ah_margin': {**RULE['synthetic_ah_margin'], 'pinnacle': {'margin': .10}}}
        normal = dict((s, l) for s, v in eh.cagey_bettable(d, m, RULE).items() for l, *_ in v)
        priced_wide = {(s, l): p for s, v in eh.cagey_bettable(d, m, wide).items() for l, p, _ in v}
        priced_normal = {(s, l): p for s, v in eh.cagey_bettable(d, m, RULE).items() for l, p, _ in v}
        for key in priced_wide.keys() & priced_normal.keys():
            if key not in (('home', -0.25), ('away', 0.25)):
                self.assertLess(priced_wide[key], priced_normal[key])
        self.assertTrue(normal)

    def test_one_side_only_the_higher_ev_side_and_one_event_per_family(self):
        d, m = fixture(margin=-1)
        bettable = eh.cagey_bettable(d, m, RULE)
        side = max(bettable, key=lambda s: max(ev for *_, ev in bettable[s]))
        events = eh.cagey_fixture_events(d, m, RULE)
        self.assertEqual(events[0], {'family': 'narrow', 'side': None, 'k': None, 'y': 1})
        no_loss = events[1:]
        self.assertTrue(no_loss)
        self.assertEqual({e['side'] for e in no_loss}, {side})
        self.assertEqual([e['k'] for e in no_loss], sorted({eh.no_loss_family(l) for l, *_ in bettable[side]}))
        sign = 1 if side == 'home' else -1
        for e in no_loss:
            self.assertEqual(e['y'], int(sign * -1 >= -e['k']))
            self.assertTrue(all(eh.no_loss_family(l) == e['k'] for l in e['lines']))

    def test_an_exact_ev_tie_bets_home(self):
        flat = {'margins': [-1, 0, 1], 'margin_probs': [.3, .4, .3], 'main_ah': [0.0, 1.5, 1.5], 'book': 'pinnacle',
                'week': 'w', 'margin': 0.}
        events = eh.cagey_fixture_events(flat, flat, RULE)
        self.assertEqual({e['side'] for e in events[1:]}, {'home'})

    def test_both_candidates_are_scored_on_the_selectors_events_and_unfinished_matches_are_skipped(self):
        d, m = fixture(margin=2)
        calib = [{'phase': 'validation', 'fixture_key': 'f1', 'candidate': 'D', 'cagey': d},
                 {'phase': 'validation', 'fixture_key': 'f1', 'candidate': 'M', 'cagey': m},
                 {'phase': 'validation', 'fixture_key': 'f2', 'candidate': 'D', 'cagey': d},  # no M: skipped
                 {'phase': 'validation', 'fixture_key': 'f3', 'candidate': 'D', 'cagey': {**d, 'margin': float('nan')}},
                 {'phase': 'validation', 'fixture_key': 'f3', 'candidate': 'M', 'cagey': {**m, 'margin': float('nan')}},
                 {'phase': 'validation', 'fixture_key': 'f1', 'candidate': 'C', 'probs': [.4, .3, .3], 'outcome': 0}]
        events = eh.cagey_events(calib, RULE)
        self.assertEqual(set(events.fixture_key), {'f1'})
        self.assertEqual(len(events), len(eh.cagey_fixture_events(d, m, RULE)))
        self.assertTrue(events[['p_D', 'p_M']].notna().all(axis=None))
        self.assertTrue((events.p_D != events.p_M).any())


class CheckTest(unittest.TestCase):
    @staticmethod
    def events(n, flatten_d=1., flatten_m=1., seed=3, shift_d=0.):
        """Binary events in both families with true probability p; D and M show p with the logit scaled."""
        rng = np.random.default_rng(seed)
        rows = []
        for family in ('narrow', 'no_loss'):
            p = rng.uniform(.4, .95, n)
            y = (rng.uniform(size=n) < p).astype(int)
            logit = np.log(p / (1 - p))
            for i in range(n):
                rows.append({'phase': 'validation', 'fixture_key': f'{family}{i}', 'week': f'w{i % 20}',
                             'family': family, 'side': None if family == 'narrow' else 'home',
                             'k': None if family == 'narrow' else 1, 'y': int(y[i]),
                             'p_D': float(1 / (1 + np.exp(-(logit[i] * flatten_d + shift_d)))),
                             'p_M': float(1 / (1 + np.exp(-logit[i] * flatten_m)))})
        return pd.DataFrame(rows)

    def test_calibrated_events_pass_for_both(self):
        events = self.events(20000)
        d = eh.cagey_events_check(events, RULE, 'D', 'M')
        self.assertTrue(d['passes'], d)
        self.assertTrue(eh.cagey_events_check(events, RULE, 'M', 'M')['passes'])

    def test_a_flat_slope_passes_only_when_closer_to_one_than_m(self):
        events = self.events(20000, flatten_d=.85, flatten_m=.75)
        d = eh.cagey_events_check(events, RULE, 'D', 'M')
        for family in RULE['families']:
            f = d['families'][family]
            self.assertGreater(f['slope'], 1.1)
            self.assertFalse(f['slope_in_band'])
            self.assertTrue(f['closer_to_one_than_baseline'])
        self.assertTrue(d['passes'], d)
        # M against itself is never closer than itself: it fails outside the band.
        m = eh.cagey_events_check(events, RULE, 'M', 'M')
        self.assertFalse(m['families']['narrow']['slope_passes'])
        self.assertFalse(m['passes'])
        # Swapped roles: D's flatter forecasts fail against a better M.
        self.assertFalse(eh.cagey_events_check(events, RULE, 'M', 'D')['passes'])

    def test_a_clear_level_bias_fails_a_band_and_failing_one_family_fails_the_rule(self):
        events = self.events(20000)
        biased = events.copy()
        mask = biased.family == 'no_loss'
        biased.loc[mask, 'p_D'] = np.clip(biased.loc[mask, 'p_D'] - .08, .01, .99)
        check = eh.cagey_events_check(biased, RULE, 'D', 'M')
        self.assertTrue(check['families']['narrow']['passes'])
        self.assertFalse(check['families']['no_loss']['bands_pass'])
        self.assertFalse(check['passes'])
        band = check['families']['no_loss']['failing_bands'][0]
        self.assertGreater(abs(band['observed_minus_forecast']), .05)
        self.assertGreater(band['z'], check['families']['no_loss']['band_z_threshold'])

    def test_a_large_gap_on_a_small_band_is_noise(self):
        events = self.events(20000)
        rng = np.random.default_rng(9)
        extra = pd.DataFrame([{'phase': 'validation', 'fixture_key': f'x{i}', 'week': 'w0', 'family': 'narrow',
                               'side': None, 'k': None, 'y': int(rng.uniform() < .25), 'p_D': .17, 'p_M': .17}
                              for i in range(40)])  # 0.1-0.2 band, ~8 points off on 40 events: z below the bar
        check = eh.cagey_events_check(pd.concat([events, extra]), RULE, 'D', 'M')
        band = [b for b in check['families']['narrow']['bands'] if b['band_lower'] == .1]
        self.assertTrue(band)
        self.assertNotIn(.1, [b['band_lower'] for b in check['families']['narrow']['failing_bands']])

    def test_bonferroni_is_over_each_familys_own_bands(self):
        check = eh.cagey_events_check(self.events(20000), RULE, 'D', 'M')
        for family in RULE['families']:
            f = check['families'][family]
            self.assertAlmostEqual(f['band_z_threshold'], eh.band_z_threshold(.05, f['bands_checked']))

    def test_no_events_fail(self):
        empty = eh.cagey_events(pd.DataFrame().to_dict('records'), RULE)
        check = eh.cagey_events_check(empty, RULE, 'D', 'M')
        self.assertFalse(check['passes'])
        self.assertEqual(eh.cagey_events_checks([], RULE), {})


class DeclarationTest(unittest.TestCase):
    """A declaration may make calibration the deciding criterion; declarations without one read as before."""

    def setUp(self):
        import tempfile
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.dir = Path(self.tmp.name)
        self.ledger = self.dir / 'ledger.json'
        self.setup = {'sha256': 'c' * 64}

    def declaration(self, **extra):
        data = {'candidate': 'D', 'baseline': 'M', 'primary_metric': 'AH all', 'draw_sensitive_lines': [-0.5, 0, 0.5],
                'calibration_tolerance': NAME, 'deciding_criterion': 'calibration',
                'reported_not_deciding': ['AH all', 'AH draw-sensitive'],
                'sample_minimum': {'fixtures': 300, 'weeks': 6}, 'declared_by': 'Paul', 'declared_at': '2026-11-13'}
        data.update(extra)
        data = {k: v for k, v in data.items() if v is not ...}
        path = self.dir / 'declaration.json'
        path.write_text(json.dumps(data), encoding='utf-8')
        return path

    def test_a_calibration_deciding_declaration_validates_and_carries_the_rule(self):
        declared = eh.validate_declaration(self.declaration(), CFG, self.setup, self.ledger)
        self.assertEqual(declared['calibration_rule'], RULE)
        self.assertEqual(declared['deciding_criterion'], 'calibration')

    def test_bad_calibration_declarations_are_refused(self):
        bad = [({'deciding_criterion': 'profit'}, 'Deciding criterion'),
               ({'candidate': 'C6', 'baseline': 'C'}, 'judges D against M only'),
               ({'candidate': 'M', 'baseline': 'D'}, 'judges D against M only'),
               ({'sample_minimum': {'fixtures': 250, 'weeks': 6}}, 'sample minimum'),
               ({'sample_minimum': ...}, 'sample minimum'),
               ({'reported_not_deciding': ['ROI']}, 'reported_not_deciding')]
        for extra, message in bad:
            with self.assertRaisesRegex(ValueError, message):
                eh.validate_declaration(self.declaration(**extra), CFG, self.setup, self.ledger)
        # The event rule can't be named by a log-loss declaration of another candidate either.
        with self.assertRaisesRegex(ValueError, 'judges D against M only'):
            eh.validate_declaration(self.declaration(candidate='C6', baseline='C', deciding_criterion=...),
                                    CFG, self.setup, self.ledger)

    def test_existing_declarations_read_as_before(self):
        c6 = eh.validate_declaration(REPO / 'evaluation/declarations/c6_holdout.json', CFG, self.setup, self.ledger)
        self.assertNotIn('deciding_criterion', c6)
        self.assertEqual(c6['calibration_rule'], CFG['calibration_tolerance'])
        self.assertEqual(c6['sha256'], '675bbf54924920f28ba6d2c35a70fb5e61821ef649319512f92ca3fb24fd1be0')
        ce3n = eh.validate_declaration(REPO / 'evaluation/declarations/ce3n_european_holdout.json', CFG, self.setup,
                                       self.ledger, eh.EUROPEAN_CANDIDATES)
        self.assertNotIn('deciding_criterion', ce3n)
        # The real ledgers still refuse both candidates.
        with self.assertRaisesRegex(ValueError, "already scored for candidate 'C6'"):
            eh.validate_declaration(REPO / 'evaluation/declarations/c6_holdout.json', CFG, self.setup)

    @staticmethod
    def holdout(n_weeks=10, per_week=40, d_loss=.70, m_loss=.70, flatten_d=1., seed=4):
        """Holdout AH records and D/M calib rows with cagey inputs from real priced grids."""
        import narrow_margin as nm
        rng = np.random.default_rng(seed)
        model = nm.production_model()
        records, calib = [], []
        i = 0
        while i < n_weeks * per_week:
            home = float(rng.uniform(.36, .50))
            row = priced(AHh=-0.25, B365H=1 / (home * 1.05), B365D=1 / (.27 * 1.05), B365A=1 / ((.73 - home) * 1.05),
                         B365AHH=1.9, B365AHA=1.95)
            prices = eh.book_prices(row, 'bet365')
            try:
                m = eh.market_matrix(prices)
            except ValueError:
                continue  # the fixed main line doesn't fit these 1X2 prices
            d = eh.cagey_matrix(m, prices, model)
            margins, probs = __import__('market_implied').margin_distribution(d)
            margin = int(rng.choice(margins, p=probs / probs.sum()))
            key, week = f'f{i}', f'2026-W{i // per_week:02d}'
            for cand, grid, loss in (('D', d, d_loss), ('M', m, m_loss)):
                records.append({'fixture_key': key, 'league': 'Eredivisie', 'week': week, 'phase': 'holdout',
                                'candidate': cand, 'market': 'AH +0.00', 'log_loss': loss + rng.normal(0, .01)})
                calib.append({'phase': 'holdout', 'fixture_key': key, 'candidate': cand, 'probs': [.4, .3, .3],
                              'outcome': 0, 'cagey': eh.cagey_inputs(grid, prices, 'bet365', week, margin)})
            i += 1
        return records, calib

    def declared(self, **extra):
        return eh.validate_declaration(self.declaration(**extra), CFG, self.setup, self.ledger)

    def test_calibration_decides_and_log_loss_is_reported_only(self):
        records, calib = self.holdout()  # D's own grid draws the results: D is calibrated; no log-loss gain
        verdict = eh.holdout_verdict(records, calib, self.declared(), {})
        self.assertEqual(verdict['deciding_criterion'], 'calibration')
        self.assertEqual(verdict['primary_metric_role'], 'reported, not deciding')
        self.assertTrue(verdict['sample_minimum_met'])
        self.assertFalse(verdict['primary']['clear_of_zero'])
        self.assertEqual(verdict['calibration']['rule'], NAME)
        self.assertEqual(set(verdict['calibration']['families']), {'narrow', 'no_loss'})
        self.assertEqual(verdict['baseline_calibration']['candidate'], 'M')
        self.assertEqual(verdict['passes_holdout_gate'], verdict['calibration']['passes'])
        self.assertIsNotNone(verdict['draw_sensitive'])
        # Under log-loss superiority the same data could not pass (no gain clear of zero).
        superiority = eh.holdout_verdict(records, calib, {**self.declared(), 'deciding_criterion': 'log_loss_superiority'}, {})
        self.assertFalse(superiority['passes_holdout_gate'])

    def test_calibration_verdict_needs_the_sample_minimum_and_a_pass(self):
        records, calib = self.holdout(n_weeks=5, per_week=40)  # 200 fixtures: below 300
        verdict = eh.holdout_verdict(records, calib, self.declared(), {})
        self.assertFalse(verdict['sample_minimum_met'])
        self.assertFalse(verdict['passes_holdout_gate'])
        records, calib = self.holdout()
        failing = {**self.declared(), 'calibration_rule': {**RULE, 'band_max_deviation': -1., 'slope_min': 5., 'slope_max': 6.}}
        verdict = eh.holdout_verdict(records, calib, failing, {})
        self.assertFalse(verdict['calibration']['passes'])
        self.assertFalse(verdict['passes_holdout_gate'])

    def test_a_superiority_verdict_is_unchanged(self):
        """The C6-style verdict: same keys and the same pass logic as before 13 Nov 2026."""
        records, calib = [], []
        rng = np.random.default_rng(1)
        for i in range(400):
            for cand, loss in (('C6', .6), ('C', .7)):
                records.append({'fixture_key': f'f{i}', 'league': 'Eredivisie', 'week': f'w{i % 10}', 'phase': 'holdout',
                                'candidate': cand, 'market': 'AH +0.00', 'log_loss': loss + rng.normal(0, .01)})
        declaration = {'candidate': 'C6', 'baseline': 'C', 'primary_metric': 'AH all', 'draw_sensitive_lines': [-.5, 0, .5],
                       'calibration_rule': CFG['calibration_tolerance']}
        verdict = eh.holdout_verdict(records, calib, declaration, {})
        self.assertEqual(set(verdict), {'candidate', 'baseline', 'primary_metric', 'primary', 'draw_sensitive',
                                        'sample_minimum', 'sample_minimum_met', 'calibration', 'calibration_tolerance',
                                        'versus_market', 'passes_holdout_gate', 'next_steps'})
        self.assertTrue(verdict['primary']['clear_of_zero'])
        self.assertFalse(verdict['passes_holdout_gate'])  # no calibration forecasts: v2 fails

    def test_the_committed_declaration_is_valid_and_d_is_now_locked(self):
        path = REPO / 'evaluation/declarations/cagey_d_holdout.json'
        declared = eh.validate_declaration(path, CFG, self.setup, self.ledger)
        self.assertEqual((declared['candidate'], declared['baseline'], declared['deciding_criterion']), ('D', 'M', 'calibration'))
        self.assertEqual(declared['calibration_rule'], RULE)
        self.assertEqual(declared['sha256'], 'd464bc071c6aedc558593dbb8f0a30279cfc945fd57a1b51ad2157ed07b5604b')
        with self.assertRaisesRegex(ValueError, "already scored for candidate 'D'"):
            eh.validate_declaration(path, CFG, self.setup)

    def test_the_ledger_records_the_deciding_criterion_only_when_declared(self):
        declared = self.declared()
        eh.record_holdout(declared, self.setup, 'abc', 640, {'passes_holdout_gate': True}, self.ledger)
        entry = json.loads(self.ledger.read_text(encoding='utf-8'))[0]
        self.assertEqual((entry['deciding_criterion'], entry['calibration_tolerance']), ('calibration', NAME))
        with self.assertRaisesRegex(ValueError, "already scored for candidate 'D'"):
            eh.validate_declaration(self.declaration(), CFG, {'sha256': 'd' * 64}, self.ledger)
        other = self.dir / 'other.json'
        c6 = eh.validate_declaration(REPO / 'evaluation/declarations/c6_holdout.json', CFG, {'sha256': 'e' * 64}, other)
        eh.record_holdout(c6, {'sha256': 'e' * 64}, 'abc', 640, {'passes_holdout_gate': False}, other)
        self.assertNotIn('deciding_criterion', json.loads(other.read_text(encoding='utf-8'))[0])


if __name__ == '__main__':
    unittest.main()
