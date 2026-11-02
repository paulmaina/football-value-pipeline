"""Policy v28: v27 price edge with the cagey-match correction (value tier, cagey tier, switches)."""

from offline_test_case import OfflineQuotePolicyTestCase
import json
import unittest

import pandas as pd

import market_implied as mi
import narrow_margin as nm
import price_edge_cagey_shortlist as v28
import price_edge_shortlist as v27
from asian_handicap import label
from test_price_edge_shortlist import (NOW, POLICY, ah_pair, decision, evaluate, fit_price, offer, pinnacle_market,
                                       quote, row)

OFF = {'cagey_correction_enabled': False, 'cagey_tier_enabled': False}
VALUE_ONLY = {'cagey_correction_enabled': True, 'cagey_tier_enabled': False}


def run(*rows, settings=None):
    return v28.build_shortlist(pd.DataFrame(list(rows)), NOW, execution_policy=POLICY, settings=settings)


def corrected(side, line):
    """Corrected fair price of the default test fixture under the production model."""
    h2h, ou, ah = pinnacle_market()
    targets = mi.targets_from_prices(tuple(h2h[k] for k in ('home', 'draw', 'away')), (ou['over'], ou['under']),
                                     (-0.25, *ah))
    fit = mi.fit(targets, include_ah=True)
    pin = {'h2h': (*[h2h[k] for k in ('home', 'draw', 'away')], None), 'ou25': (ou['over'], ou['under'], None)}
    context = v28.corrected_context(pin, fit, {'fit_a': fit}, nm.production_model())
    return v28.corrected_price(context, side, line), context


class ValueTierTests(OfflineQuotePolicyTestCase):
    def test_derived_plus_line_uses_the_corrected_price(self):
        priced, _ = corrected('away', 1.0)
        uncorrected = fit_price('away', 1.0)['fair_odds']
        self.assertLess(priced['corrected_fair_odds'], uncorrected)  # the correction lengthens plus-line win-shares
        _, decisions, _ = run(row(offers=[offer('away', 1.0, 1.50)]), settings=VALUE_ONLY)
        item = decision(decisions, label('away', 1.0))
        self.assertEqual(item.reference_type, 'c-cagey')
        self.assertAlmostEqual(item.fair_odds, priced['corrected_fair_odds'], places=9)
        self.assertAlmostEqual(item.fair_odds_uncorrected, uncorrected, places=9)
        self.assertAlmostEqual(item.minimum_odds, priced['corrected_fair_odds'] * 1.03, places=9)

    def test_qualified_only_because_of_correction(self):
        priced, _ = corrected('away', 1.0)
        uncorrected = fit_price('away', 1.0)['fair_odds']
        price = round(priced['corrected_fair_odds'] * 1.035, 4)
        self.assertLess(price, uncorrected * 1.03)  # v27 would reject this price
        _, plain, _ = evaluate(row(offers=[offer('away', 1.0, price)]))
        self.assertEqual(decision(plain, label('away', 1.0)).rejection_reasons, 'edge below 3%')
        selected, decisions, summary = run(row(offers=[offer('away', 1.0, price)]), settings=VALUE_ONLY)
        item = decision(decisions, label('away', 1.0))
        self.assertEqual(item.decision, 'SHORTLISTED')
        self.assertTrue(item.qualified_only_by_correction)
        self.assertEqual(summary['correction_only_value_picks'], 1)
        self.assertEqual(summary['reference_type_counts'], {'c-cagey': 1})

    def test_minus_lines_and_pinnacle_references_are_unaffected(self):
        offers = [*ah_pair(-0.75, 1.95, 1.95), offer('home', -0.75, 2.10), offer('home', -1.0, 2.9),
                  *ah_pair(1.5, 1.20, 4.6), offer('home', 1.5, 1.27)]
        _, old, _ = evaluate(row(offers=offers))
        _, new, _ = run(row(offers=offers), settings=VALUE_ONLY)
        for market in (label('home', -0.75), label('home', -1.0), label('home', 1.5)):
            a, b = decision(old, market), decision(new, market)
            self.assertEqual((a.reference_type, a.decision, a.rejection_reasons), (b.reference_type, b.decision, b.rejection_reasons))
            self.assertEqual(a.fair_odds if pd.notna(a.fair_odds) else None, b.fair_odds if pd.notna(b.fair_odds) else None)
        pinned = decision(new, label('home', 1.5))
        self.assertEqual(pinned.reference_type, 'a')
        self.assertAlmostEqual(pinned.corrected_vs_pinnacle_gap, pinned.corrected_fair_probability - pinned.fair_probability)
        self.assertIn(v27.NO_REFERENCE, decision(new, label('home', -1.0)).rejection_reasons)

    def test_derived_plus_lines_below_one_keep_the_uncorrected_price(self):
        _, decisions, _ = run(row(offers=[offer('away', 0.75, 1.80)]), settings=VALUE_ONLY)
        self.assertEqual(decision(decisions, label('away', 0.75)).reference_type, 'c')

    def test_switches_off_reproduce_v27_exactly(self):
        offers = [*ah_pair(-0.75, 1.95, 1.95), offer('home', -0.75, 2.10), offer('away', 1.0, 1.5),
                  offer('away', 1.5, 1.4), offer('home', -1.0, 2.9)]
        rows = [row(offers=offers), row(home='Second', offers=[offer('away', 1.0, 2.6)])]
        a_sel, a_dec, a_sum = v27.build_shortlist(pd.DataFrame(rows), NOW, execution_policy=POLICY)
        b_sel, b_dec, b_sum = run(*rows, settings=OFF)
        drop = ['selection_policy_version']
        self.assertTrue(a_dec.drop(columns=drop).equals(b_dec.drop(columns=drop)))
        self.assertTrue(a_sel.drop(columns=drop).equals(b_sel.drop(columns=drop)))
        self.assertEqual(set(b_dec.selection_policy_version), {v28.POLICY})
        self.assertFalse(b_sum['cagey_correction_enabled'] or b_sum['cagey_tier_enabled'])
        for key in ('rejection_counts', 'tagged_candidates', 'n_shortlisted'):
            self.assertEqual(a_sum[key], b_sum[key])


if __name__ == '__main__':
    unittest.main()
