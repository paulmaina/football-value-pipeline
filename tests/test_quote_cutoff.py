"""observed-by-cutoff-v2: no decision may use a quote stamped after the evaluation clock."""

from offline_test_case import OfflineQuotePolicyTestCase
import unittest

import pandas as pd

import price_edge_cagey_shortlist as v28
from test_price_edge_shortlist import NOW, POLICY, quote, pinnacle_market
from test_value_per_market import V2, fixture, h2h_1xbet, price_at, run, decision_row

LATER = (NOW + pd.Timedelta(minutes=4)).isoformat()  # inside the 5-minute provider-skew allowance
STRICT = {**V2, 'quote_timing_rule': v28.TIMING_RULE_CUTOFF}


def future_home_win():
    h2h, _, _ = pinnacle_market()
    return quote('h2h', {'home': price_at('home', 0.03), 'draw': h2h['draw'] * 0.9, 'away': h2h['away'] * 0.9},
                 book='1xBet', stamp=LATER)


class CutoffTests(OfflineQuotePolicyTestCase):
    def test_skew_rule_still_accepts_it_so_old_runs_replay_unchanged(self):
        selected, decisions, summary = run(fixture(future_home_win()), settings=V2)
        self.assertEqual(decision_row(decisions, 'Home win').decision, 'SHORTLISTED')
        self.assertNotIn('quote_timing_rule', summary)

    def test_offer_stamped_after_the_clock_is_rejected(self):
        selected, decisions, summary = run(fixture(future_home_win()), settings=STRICT)
        row = decision_row(decisions, 'Home win')
        self.assertEqual(row.decision, 'REJECTED')
        self.assertIn(v28.FUTURE_REASON, row.rejection_reasons)
        self.assertNotIn('Home win', set(selected.get('market_to_bet', [])))
        self.assertEqual(summary['quote_timing_rule'], v28.TIMING_RULE_CUTOFF)

    def test_quote_at_the_clock_is_usable(self):
        h2h, _, _ = pinnacle_market()
        at_clock = quote('h2h', {'home': price_at('home', 0.03), 'draw': h2h['draw'] * 0.9,
                                 'away': h2h['away'] * 0.9}, book='1xBet', stamp=NOW.isoformat())
        _, decisions, _ = run(fixture(at_clock), settings=STRICT)
        self.assertEqual(decision_row(decisions, 'Home win').decision, 'SHORTLISTED')

    def test_pinnacle_reference_stamped_after_the_clock_rejects_every_decision_using_it(self):
        _, decisions, _ = run(fixture(h2h_1xbet(home=price_at('home', 0.03)), pin_stamp=LATER), settings=STRICT)
        uses = decisions.loc[decisions.pinnacle_last_update_utc.eq(LATER)]
        self.assertTrue(len(uses))
        self.assertTrue(uses.decision.eq('REJECTED').all())
        self.assertTrue(uses.rejection_reasons.str.contains(v28.FUTURE_REASON).all())

    def future_fit_input(self, settings):
        """A valid on-time 1X2 reference and offer; only Pinnacle's O/U 2.5 (a fit B input) is late.

        A 1xBet AH 0.00 offer is included: its Pinnacle draw-no-bet reference is direct, but a level
        line needs the push probability, which only a fit supplies."""
        from test_price_edge_shortlist import row, offer
        h2h, ou, _ = pinnacle_market()
        quotes = [quote('h2h', h2h), quote('totals', ou, key='totals', point=2.5, stamp=LATER),
                  h2h_1xbet(home=price_at('home', 0.03))]
        _, decisions, _ = run(row(offers=[offer('home', 0.0, 1.60)], quotes=quotes), settings=settings)
        return decision_row(decisions, 'Home win'), decisions

    def test_future_fit_input_is_kept_out_of_ranking_settlement_and_staking(self):
        item, decisions = self.future_fit_input(STRICT)
        # The direct 1X2 price still qualifies on its own evidence...
        self.assertEqual(item.decision, 'SHORTLISTED')
        self.assertEqual(item.reference_type, 'b')
        # ...but nothing downstream uses the fit that depends on the late quote.
        self.assertFalse(bool(item.fit_usable))
        self.assertIn('input timestamped after evaluation', item.fit_reasons)
        self.assertAlmostEqual(item.pinnacle_no_loss_probability, item.fair_probability)  # half line: win share
        self.assertNotEqual(item.uncorrected_input_timing_status, 'SYNCHRONIZED')
        self.assertTrue(pd.isna(item.uncorrected_p_win))
        self.assertTrue(pd.isna(item.corrected_cagey_score))
        self.assertFalse((decisions.reference_type == 'c').any())
        self.assertFalse((decisions.reference_type == 'c-cagey').any())
        import master_shortlist as ms
        picked = ms.build(decisions)
        row = picked.loc[picked.market_to_bet.eq('Home win')].iloc[0]
        self.assertEqual(row.master_probability_basis, 'Pinnacle fair price')

    def test_push_line_without_the_fit_has_no_no_loss_figure(self):
        _, decisions = self.future_fit_input(STRICT)
        level = decisions.loc[decisions.handicap_line.astype(float).eq(0.0) & decisions.bookmaker.eq('1xBet')]
        self.assertEqual(len(level), 1)
        self.assertTrue(level.pinnacle_no_loss_probability.isna().all())
        import master_shortlist as ms
        pooled = ms.pool(decisions)
        pooled = pooled.loc[pooled.handicap_line.astype(float).eq(0.0) & pooled.bookmaker.eq('1xBet')]
        self.assertTrue((pooled.master_probability_basis == 'unavailable').all())

    def test_skew_rule_still_uses_the_fit(self):
        item, _ = self.future_fit_input(V2)
        self.assertTrue(bool(item.fit_usable))
        self.assertEqual(item.uncorrected_input_timing_status, 'SYNCHRONIZED')

    def test_master_shortlist_excludes_future_quotes(self):
        import master_shortlist as ms
        _, decisions, _ = run(fixture(future_home_win()), settings=STRICT)
        pool = ms.pool(decisions)
        self.assertFalse(((pool.market_to_bet == 'Home win') & (pool.bookmaker == '1xBet')).any())

    def test_unknown_rule_fails_closed(self):
        with self.assertRaisesRegex(ValueError, 'Unknown quote_timing_rule'):
            v28.timing_rule({'quote_timing_rule': 'anything'})


if __name__ == '__main__':
    unittest.main()
