"""Cagey score: market-implied P(2+ goal margin); tracking only, never a decision input."""

from offline_test_case import OfflineQuotePolicyTestCase
import json
import unittest
from unittest.mock import patch

import numpy as np
import pandas as pd

import market_implied as mi
import market_implied_calibration as cal
import price_edge_shortlist as v27
import price_edge_tracking as tracking
from test_market_implied import csv_row
from test_price_edge_shortlist import NOW, FRESH, ah_pair, evaluate, offer, quote, row, pinnacle_market


def fits():
    h2h, ou, ah = pinnacle_market()
    targets = mi.targets_from_prices(tuple(h2h[k] for k in ('home', 'draw', 'away')), (ou['over'], ou['under']),
                                     (-0.25, *ah))
    return mi.fit(targets, include_ah=True), mi.fit(targets, include_ah=False)


class ScoreTests(OfflineQuotePolicyTestCase):
    def test_score_is_one_minus_p_margin_within_one_and_in_unit_interval(self):
        fit_b, fit_a = fits()
        for result in (fit_b, fit_a):
            margins, probs = mi.margin_distribution(result.matrix)
            score = mi.margin_at_least(result, 2)
            self.assertAlmostEqual(score, 1 - probs[np.abs(margins) <= 1].sum(), places=12)
            self.assertTrue(0 <= score <= 1)
            self.assertLess(mi.margin_at_least(result, 3), score)

    def test_fit_b_first_then_fit_a_then_none(self):
        fit_b, fit_a = fits()
        self.assertEqual(mi.cagey_score(fit_b, fit_a), (mi.margin_at_least(fit_b, 2), 'B'))
        fit_b.usable = False
        self.assertEqual(mi.cagey_score(fit_b, fit_a), (mi.margin_at_least(fit_a, 2), 'A'))
        fit_a.usable = False
        self.assertEqual(mi.cagey_score(fit_b, fit_a), (None, None))
        with self.assertRaises(ValueError):
            mi.margin_at_least(mi.Fit('B', False, []), 2)


class PolicyTests(OfflineQuotePolicyTestCase):
    def test_recorded_for_tagged_and_untagged_fixtures(self):
        balanced = row(home='Tagged', quotes=[quote('h2h', {'home': 2.6, 'draw': 3.2, 'away': 2.9}),
                                              quote('totals', {'over': 2.10, 'under': 1.80}, key='totals', point=2.5)],
                       offers=[offer('home', -0.25, 2.0)])
        plain = row(home='Plain', quotes=[quote('h2h', {'home': 1.30, 'draw': 5.5, 'away': 9.0}),
                                          quote('totals', {'over': 1.60, 'under': 2.40}, key='totals', point=2.5)],
                    offers=[offer('home', -0.25, 1.5)])
        _, decisions, _ = evaluate(balanced, plain)
        for team, tagged in (('Tagged', True), ('Plain', False)):
            part = decisions[decisions.home_team == team]
            self.assertEqual(bool(part.any_tag.iloc[0]), tagged)
            self.assertTrue(part.cagey_score.between(0, 1).all())
            self.assertEqual(part.cagey_score.nunique(), 1)
        lopsided = decisions[decisions.home_team == 'Plain'].cagey_score.iloc[0]
        self.assertGreater(lopsided, decisions[decisions.home_team == 'Tagged'].cagey_score.iloc[0])

    def test_equals_fit_b_score_and_falls_back_to_fit_a_without_main_line(self):
        fit_b, _ = fits()
        _, decisions, _ = evaluate(row(offers=[offer('home', -0.25, 2.0)]))
        self.assertEqual(decisions.cagey_fit.unique().tolist(), ['B'])
        self.assertAlmostEqual(decisions.cagey_score.iloc[0], mi.margin_at_least(fit_b, 2), places=6)
        no_main = row(offers=[offer('home', -0.25, 2.0)])
        no_main['asian_handicap_offers'] = json.dumps([offer('home', -0.25, 2.0)])
        _, decisions, _ = evaluate(no_main)
        self.assertEqual(decisions.cagey_fit.unique().tolist(), ['A'])
        _, decisions, _ = evaluate(row(quotes=[], offers=[offer('home', -0.25, 2.0)]))
        self.assertTrue(decisions.cagey_score.isna().all() and decisions.cagey_fit.isna().all())

    def test_never_changes_a_decision(self):
        offers = [*ah_pair(-0.75, 1.95, 1.95), offer('home', -0.75, 2.05), offer('away', 1.0, 1.50),
                  offer('away', 1.0, 2.60), offer('home', -1.0, 2.9)]
        columns = ['market_to_bet', 'bookmaker', 'offered_decimal_odds', 'decision', 'rejection_reasons', 'edge']
        _, real, _ = evaluate(row(offers=offers))
        with patch.object(mi, 'cagey_score', return_value=(0.0, 'X')):
            _, forced, _ = evaluate(row(offers=offers))
        self.assertTrue(real[columns].equals(forced[columns]))
        self.assertEqual(set(forced.cagey_fit), {'X'})

    def test_output_and_tracking_columns_include_the_score(self):
        self.assertIn('cagey_score', v27.OUTPUT_COLUMNS)
        self.assertIn('cagey_fit', v27.OUTPUT_COLUMNS)
        self.assertIn('cagey_score', tracking.COLUMNS)
        self.assertIn('cagey_quintile', tracking.SPLITS)


class TrackingTests(OfflineQuotePolicyTestCase):
    def test_quintiles_order_cagiest_first_and_need_five_values(self):
        labels = tracking.cagey_quintiles([0.30, 0.50, 0.40, None, 0.35, 0.45, 0.32, 0.48, 0.38, 0.42, 0.36])
        self.assertEqual(labels.iloc[0], 'Q1 cagiest')
        self.assertEqual(labels.iloc[1], 'Q5 most open')
        self.assertEqual(labels.iloc[3], 'n/a')
        self.assertEqual(set(tracking.cagey_quintiles([0.3, 0.4])), {'n/a'})


class ClosingCoverageTests(OfflineQuotePolicyTestCase):
    def test_pinnacle_close_on_an_alternate_line_is_captured_and_gradeable(self):
        """The collector requests spreads + alternate_spreads + draw_no_bet for an AH pick and normalize keeps every line."""
        from closing_odds import normalize
        kick = pd.Timestamp('2026-11-07T15:00:00Z')
        observed = kick - pd.Timedelta(minutes=3)
        stamp = (observed - pd.Timedelta(seconds=30)).isoformat()
        source = {'league': 'Premier League', 'home_team': 'Home FC', 'away_team': 'Away FC',
                  'kickoff_utc': kick.isoformat(), 'odds_event_id': 'ev1'}
        payload = {'id': 'ev1', 'commence_time': kick.isoformat(), 'home_team': 'Home FC', 'away_team': 'Away FC',
                   'bookmakers': [{'key': 'pinnacle', 'title': 'Pinnacle', 'markets': [
                       {'key': 'spreads', 'last_update': stamp, 'outcomes': [
                           {'name': 'Home FC', 'point': -0.25, 'price': 1.95}, {'name': 'Away FC', 'point': 0.25, 'price': 1.95}]},
                       {'key': 'alternate_spreads', 'last_update': stamp, 'outcomes': [
                           {'name': 'Home FC', 'point': 1.75, 'price': 1.18}, {'name': 'Away FC', 'point': -1.75, 'price': 5.20}]}]}]}
        quotes = normalize(source, payload, observed)['quotes']
        selections = {q['selection'] for q in quotes}
        self.assertIn('Asian Handicap Home +1.75', selections)
        self.assertIn('Asian Handicap Away -1.75', selections)
        share = tracking.close_win_share(quotes, 'home', 1.75)
        self.assertAlmostEqual(share, (1 / 1.18) / (1 / 1.18 + 1 / 5.20))


class CalibrationTests(OfflineQuotePolicyTestCase):
    def test_match_rows_carry_scores_and_quintile_table(self):
        rows = cal.match_rows(csv_row())
        self.assertTrue(all(0 <= rows[0][f'{k}_cagey'] <= 1 for k in ('A', 'B')))
        self.assertLess(rows[0]['A_p3'], rows[0]['A_cagey'])
        self.assertEqual(rows[0]['abs_margin'], 0)
        matches = pd.DataFrame([cal.match_rows(csv_row(Date=pd.Timestamp('2023-08-01') + pd.Timedelta(days=7 * i),
                                                       PSCH=1.5 + 0.1 * i, PSCA=8 - 0.25 * i, FTHG=i % 4))[0]
                                for i in range(20)])
        records = cal.cagey_calibration(matches, 50)
        self.assertEqual({r['fit'] for r in records}, {'A', 'B'})
        self.assertEqual({r['quintile'] for r in records}, set(cal.CAGEY_QUINTILES))
        self.assertTrue({'all', 'to_2023', 'from_2024'} >= {r['period'] for r in records})
        first = records[0]
        self.assertAlmostEqual(first['gap_2plus'], first['actual_2plus'] - first['predicted_2plus'], places=9)
        self.assertIn('Cagey score: actual vs predicted', '\n'.join(cal.cagey_section(records)))


if __name__ == '__main__':
    unittest.main()
