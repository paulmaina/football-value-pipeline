"""Cagey rows show the cagey tier's own probabilities (reporting only; PR #166 finding 1).

A cagey row shares its decision row with the value tier, which writes the research model's figures into
p_no_loss, predicted_probability and rank_probability. On cagey_tier_shortlist.csv those columns must carry
the cagey tier's own no-loss probability (the figure it ranks by), probability_basis must name its source, and
the research figure stays visible as research_p_no_loss. Nothing else on the list may change.
"""
from __future__ import annotations

import io
import json
from pathlib import Path
import unittest

import numpy as np
import pandas as pd

import narrow_margin as nm
import price_edge_cagey_shortlist as v28

FROZEN = json.loads((Path(__file__).with_name('fixtures') / 'frozen_forecast_row.json').read_text(encoding='utf-8'))
POLICY = json.loads((Path(__file__).resolve().parents[1] / 'shortlist_quote_policy.json').read_text(encoding='utf-8'))
OWN = list(v28.TIER_OWN_PROBABILITY_COLUMNS)
RELABELLED = {*OWN, 'probability_basis', 'research_p_no_loss'}


def assert_own_probabilities(test, picks):
    """Every cagey row's shared probability columns equal the cagey tier's own figure, exactly."""
    test.assertGreater(len(picks), 0)
    own = picks[v28.tier_no_loss_column(picks)].astype(float)
    test.assertTrue(own.notna().all())
    for column in OWN:
        np.testing.assert_array_equal(picks[column].astype(float).to_numpy(), own.to_numpy(), err_msg=column)
    if 'cagey_probability_basis' in picks:
        test.assertEqual(list(picks.probability_basis), list(picks.cagey_probability_basis))


class ProductionCageyRowsTest(unittest.TestCase):
    """The production rule on a real frozen forecast (Brighton v Brentford, 8 Nov 2026)."""

    @classmethod
    def setUpClass(cls):
        cls.selected, cls.decisions, cls.summary = v28.build_shortlist(
            pd.DataFrame([FROZEN['row']]), FROZEN['snapshot_generated_utc'], execution_policy=POLICY,
            settings=v28.load_settings(), model=nm.production_model())
        cls.picks = v28.cagey_tier_list(cls.decisions)
        cls.legacy = v28.cagey_tier_list(cls.decisions, None)

    def test_production_rule_and_research_value_rule_are_exercised(self):
        self.assertEqual(self.summary['cagey_tier']['rule_version'], v28.TIER_RULE_MARKET_BASIS)
        self.assertIn(self.summary['value_rule'], v28.PROFIT_RULES)
        self.assertGreaterEqual(len(self.picks), 2)

    def test_cagey_rows_carry_the_cagey_tiers_own_probabilities(self):
        assert_own_probabilities(self, self.picks)
        np.testing.assert_array_equal(self.picks.p_no_loss.astype(float), self.picks.cagey_no_loss_probability.astype(float))

    def test_the_written_csv_carries_them_too(self):
        # What the pipeline and the refresh write, read back as a reader of the file would.
        assert_own_probabilities(self, pd.read_csv(io.StringIO(self.picks.to_csv(index=False))))

    def test_the_old_labels_did_differ(self):
        # Not vacuous: before the fix these columns held the research model's figures.
        own = self.legacy.cagey_no_loss_probability.astype(float)
        for column in OWN:
            self.assertFalse(np.array_equal(self.legacy[column].astype(float), own), column)

    def test_research_figure_stays_visible_under_its_own_name(self):
        np.testing.assert_array_equal(self.picks.research_p_no_loss.astype(float), self.legacy.p_no_loss.astype(float))
        np.testing.assert_array_equal(self.picks.profit_probability.astype(float), self.legacy.rank_probability.astype(float))

    def test_nothing_else_on_the_list_changes(self):
        self.assertEqual(set(self.picks.columns) - set(self.legacy.columns), {'research_p_no_loss'})
        keep = [c for c in self.legacy.columns if c not in RELABELLED]
        self.assertEqual(self.picks[keep].to_csv(index=False), self.legacy[keep].to_csv(index=False))

    def test_decisions_and_value_list_are_untouched(self):
        # Relabelling happens on the cagey list's own copy; the shared decision rows keep the value tier's figures.
        ranked = v28._tier_rank(self.decisions.loc[self.decisions.cagey_tier_decision == 'SHORTLISTED'])
        np.testing.assert_array_equal(ranked.p_no_loss.astype(float), self.legacy.p_no_loss.astype(float))
        self.assertIn('research_p_no_loss', self.picks)
        self.assertNotIn('research_p_no_loss', self.decisions)
        self.assertNotIn('research_p_no_loss', self.selected)

    def test_run_records_the_labels_version(self):
        self.assertEqual(self.summary['cagey_tier_labels_version'], v28.TIER_LABELS_VERSION)
        with self.assertRaises(ValueError):
            v28.cagey_tier_list(self.decisions, 'unknown-labels')


class EarlierTierRulesTest(unittest.TestCase):
    """Rules without cagey_no_loss_probability rank by corrected_no_loss_probability: that is their figure."""

    def frame(self):
        return pd.DataFrame({
            'cagey_tier_decision': ['SHORTLISTED', 'SHORTLISTED', 'NOT_SELECTED'],
            'corrected_no_loss_probability': [0.91, 0.87, 0.95], 'corrected_expected_profit': [0.01, 0.02, 0.0],
            'offered_decimal_odds': [1.3, 1.4, 1.2], 'kickoff_utc': ['2026-11-08T15:00:00Z'] * 3,
            'market': ['AH Home +1.5', 'AH Away +1.0', 'AH Home +2.0'], 'bookmaker': ['Pinnacle'] * 3,
            'p_no_loss': [0.70, 0.60, 0.50], 'predicted_probability': [0.55, 0.45, 0.40],
            'rank_probability': [0.55, 0.45, 0.40], 'probability_basis': ['net_profit'] * 3,
            'profit_probability': [0.55, np.nan, 0.40]})

    def test_value_rule_rows(self):
        picks = v28.cagey_tier_list(self.frame())
        assert_own_probabilities(self, picks)
        self.assertEqual(list(picks.p_no_loss), [0.91, 0.87])
        self.assertEqual(list(picks.probability_basis), ['corrected_matrix'] * 2)
        # Research no-loss only where the research model priced the row.
        self.assertEqual(picks.research_p_no_loss.iloc[0], 0.70)
        self.assertTrue(np.isnan(picks.research_p_no_loss.iloc[1]))

    def test_empty_list(self):
        frame = self.frame().assign(cagey_tier_decision='REJECTED')
        self.assertEqual(len(v28.cagey_tier_list(frame)), 0)


if __name__ == '__main__':
    unittest.main()
