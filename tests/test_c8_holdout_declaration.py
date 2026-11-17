"""C8's holdout declaration (docs/plan.md, Phase 2g): the committed file is one the harness accepts, and the
three declared outcomes are read from the harness verdict by a rule fixed before the holdout was scored.

Nothing here scores a holdout match: the declaration is only validated, and the outcome rule is exercised on
made-up verdicts.
"""
import json
from pathlib import Path
import tempfile
import unittest

import evaluation_harness as eh
from scripts import c8_holdout_outcome as outcome

REPO = Path(__file__).resolve().parents[1]
CFG = json.loads((REPO / 'evaluation_harness_config.json').read_text(encoding='utf-8'))
PATH = REPO / 'evaluation' / 'declarations' / 'c8_holdout.json'
V3 = 'slopes-0.90-1.10-or-closer-than-baseline-bands-30-5pp-bonferroni-v3'


def verdict(all_gain=.003, draw_gain=.004, clear=False, calibrated=True, enough=True, **extra):
    paired = lambda gain, is_clear: None if gain is None else {
        'fixtures': 640, 'weeks': 25, 'mean_gain': gain, 'interval_95': [gain - .001, gain + .001] if is_clear
        else [gain - .004, gain + .004], 'clear_of_zero': is_clear}
    return {'candidate': 'C8', 'baseline': 'C6', 'primary_metric': 'AH all', 'primary': paired(all_gain, clear),
            'draw_sensitive': paired(draw_gain, False), 'sample_minimum_met': enough,
            'calibration': {'passes': calibrated}, **extra}


class DeclarationTest(unittest.TestCase):
    def setUp(self):
        self.data = json.loads(PATH.read_text(encoding='utf-8'))

    def test_the_committed_declaration_is_what_was_decided(self):
        self.assertEqual((self.data['candidate'], self.data['baseline'], self.data['market_reference']),
                         ('C8', 'C6', 'M'))
        self.assertEqual(self.data['primary_metric'], 'AH all')
        self.assertEqual(self.data['draw_sensitive_lines'], [-0.5, 0.0, 0.5])
        self.assertEqual(self.data['calibration_tolerance'], V3)
        self.assertEqual({k: self.data['sample_minimum'][k] for k in ('fixtures', 'weeks')}, eh.promotion_minimums())
        # No deciding criterion: the harness's own verdict stays log-loss superiority, which is "proven".
        self.assertNotIn('deciding_criterion', self.data)
        self.assertEqual(tuple(self.data['outcomes']), outcome.OUTCOMES)
        for name, release in outcome.RELEASES.items():
            decision = self.data['outcomes'][name]['decision']
            self.assertEqual(decision.startswith('Release'), release, name)
            self.assertEqual(decision.startswith('No release'), not release, name)

    def test_the_harness_accepts_it_and_the_ledger_does_not_refuse_c6_as_the_baseline(self):
        setup = {'sha256': 'a' * 64}
        with tempfile.TemporaryDirectory() as tmp:
            declared = eh.validate_declaration(PATH, CFG, setup, Path(tmp) / 'ledger.json')
        self.assertEqual((declared['candidate'], declared['baseline']), ('C8', 'C6'))
        self.assertEqual(declared['calibration_rule']['name'], V3)
        self.assertTrue(declared['calibration_rule']['slope_relative_to_baseline'])
        # The real ledger holds C6 and D as scored candidates. A ledger without a C8 entry (the committed one
        # before the run; the same entries here) accepts C8 with C6 as its baseline; once C8 is scored it
        # refuses a second run.
        entries = json.loads(eh.LEDGER.read_text(encoding='utf-8'))
        self.assertTrue({'C6', 'D'} <= {e['candidate'] for e in entries})
        with tempfile.TemporaryDirectory() as tmp:
            before = Path(tmp) / 'ledger.json'
            before.write_text(json.dumps([e for e in entries if e['candidate'] != 'C8']), encoding='utf-8')
            eh.validate_declaration(PATH, CFG, setup, before)
            eh.record_holdout(declared, setup, 'abc', 640, {'passes_holdout_gate': False}, before)
            with self.assertRaisesRegex(ValueError, "already scored for candidate 'C8'"):
                eh.validate_declaration(PATH, CFG, {'sha256': 'b' * 64}, before)

    def test_c8_is_the_registered_candidate_and_unchanged(self):
        self.assertIn('C8', eh.CANDIDATES)
        self.assertEqual(eh.RATE_CALIBRATION_CANDIDATES, {'C7': False, 'C8': True})
        self.assertNotIn('C8', eh.RATE_VARIANTS)


class OutcomeTest(unittest.TestCase):
    def test_proven_needs_the_interval_clear_and_everything_else(self):
        result = outcome.declared_outcome(verdict(clear=True))
        self.assertEqual((result['outcome'], result['release']), ('proven', True))

    def test_not_proven_with_both_point_estimates_positive_releases_with_guardrails(self):
        result = outcome.declared_outcome(verdict(clear=False))
        self.assertEqual((result['outcome'], result['release']), ('release_with_guardrails', True))
        self.assertEqual(result['baseline_minus_candidate'], {'AH all': .003, 'AH draw-sensitive': .004})

    def test_a_negative_zero_or_missing_point_estimate_is_no_release(self):
        for changed in ({'all_gain': -.0001}, {'draw_gain': -.0001}, {'all_gain': 0.}, {'draw_gain': 0.},
                        {'draw_gain': None}, {'all_gain': None}):
            result = outcome.declared_outcome(verdict(**changed))
            self.assertEqual((result['outcome'], result['release']), ('no_release', False), changed)

    def test_a_negative_draw_sensitive_estimate_overrides_a_clear_primary(self):
        result = outcome.declared_outcome(verdict(clear=True, draw_gain=-.0002))
        self.assertEqual(result['outcome'], 'no_release')
        self.assertTrue(result['conditions']['primary_interval_clear_of_zero'])

    def test_failed_calibration_or_a_short_sample_is_no_release(self):
        for changed in ({'calibrated': False}, {'enough': False}):
            for clear in (True, False):
                self.assertEqual(outcome.declared_outcome(verdict(clear=clear, **changed))['outcome'], 'no_release')

    def test_proven_is_the_harness_gate_plus_a_positive_draw_sensitive_estimate(self):
        """Wherever the outcome is proven, the harness's own superiority gate passes too."""
        for clear in (True, False):
            for calibrated in (True, False):
                for enough in (True, False):
                    v = verdict(clear=clear, calibrated=calibrated, enough=enough)
                    gate = enough and clear and calibrated  # holdout_verdict's log-loss-superiority rule
                    self.assertEqual(outcome.declared_outcome(v)['outcome'] == 'proven', gate)

    def test_another_declarations_verdict_is_refused(self):
        with self.assertRaisesRegex(ValueError, 'Not the verdict'):
            outcome.declared_outcome({**verdict(), 'candidate': 'C6', 'baseline': 'C'})


if __name__ == '__main__':
    unittest.main()
