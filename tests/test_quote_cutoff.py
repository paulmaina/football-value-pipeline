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
