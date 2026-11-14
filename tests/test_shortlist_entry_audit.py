"""Shortlist entry audit: the harness's selection functions select exactly what the live lists select.

On saved live runs (27 Oct - 8 Nov 2026), rebuilt under today's production rules as the master replays do,
shortlist_entry_audit.value_select and cagey_select applied to each run's decision rows must pick exactly the
value shortlist and the cagey tier, for the rules they express (odds window, excluded markets, distribution
available, price guard, one pick per fixture and market group, ranking). The live rejection reasons are used only
for the rules a backtest can't express (kickoff window, quote timing, synchronisation, bookmaker, Europa rule).
The full 29-run check is scripts/shortlist_entry_reproduction.py (evaluation/shortlist_entry_audit/reproduction.json).
"""
from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / 'scripts'))

import shortlist_entry_audit as sea  # noqa: E402
import shortlist_entry_reproduction as reproduction  # noqa: E402

RUNS = reproduction.runs()
# Two full slates: 31 Oct (68 value and 62 cagey picks, the lists differ) and the latest run (8 Nov, 12:20 UTC).
SAMPLE = [run for run in RUNS if run[1].name in ('f82ff3e276c6c573', 'd5829163b3fa9bf3')]


@unittest.skipUnless(SAMPLE, 'no saved live runs in the reproduction window')
class SavedRunReproductionTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.decisions = {directory.name: reproduction.rebuild(directory, generated) for generated, directory in SAMPLE}

    def test_harness_selects_exactly_the_live_lists(self):
        for name, decisions in self.decisions.items():
            result = sea.reproduce(decisions)
            for tier in ('value', 'cagey'):
                with self.subTest(run=name, tier=tier):
                    self.assertGreater(result[tier]['live'], 0)
                    self.assertEqual(result[tier]['only_live'], [])
                    self.assertEqual(result[tier]['only_harness'], [])
                    self.assertTrue(result[tier]['same'])

    def test_selection_decides_between_competing_offers(self):
        """Not trivial: in many fixture groups several unblocked offers compete and the functions choose one."""
        for name, decisions in self.decisions.items():
            fixtures = sea.decision_offers(decisions)
            for tier, eligible in (('value', sea.value_eligible), ('cagey', sea.cagey_eligible)):
                contested = 0
                for offers in fixtures.values():
                    groups = {}
                    for offer in offers:
                        if eligible(offer):
                            groups[sea.market_group(offer)] = groups.get(sea.market_group(offer), 0) + 1
                    contested += sum(n >= 2 for n in groups.values())
                with self.subTest(run=name, tier=tier):
                    self.assertGreater(contested, 10)

    def test_a_changed_rule_changes_the_selection(self):
        """Positive control: the functions really apply the rules (one pick per match instead of one per market
        group drops live picks wherever a match has picks in two groups)."""
        for name, decisions in self.decisions.items():
            tighter = sea.reproduce(decisions, sea.with_rules(one_per_match=True))
            with self.subTest(run=name):
                self.assertFalse(tighter['value']['same'])
                self.assertFalse(tighter['cagey']['same'])
                self.assertLess(tighter['value']['harness'], tighter['value']['live'])

    def test_unexpressed_live_reasons_block_and_expressed_ones_do_not(self):
        for name, decisions in self.decisions.items():
            fixtures = sea.decision_offers(decisions)
            rows = decisions.to_dict('records')
            by_index = dict(zip(decisions.index, rows))
            for offers in fixtures.values():
                for offer in offers:
                    reasons = sea._reasons(by_index[offer['index']].get('rejection_reasons'))
                    if any('kickoff outside' in r for r in reasons):
                        self.assertTrue(offer['blocked_value'])
                    if reasons and all(r in sea.VALUE_EXPRESSED for r in reasons):
                        self.assertFalse(offer['blocked_value'])


if __name__ == '__main__':
    unittest.main()
