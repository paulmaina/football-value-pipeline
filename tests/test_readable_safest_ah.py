"""Display-only safest Asian handicap columns in the readable prediction files."""
import json
import unittest

import pandas as pd

from format_football_output import SAFEST_AH_COLUMNS, readable_predictions_frame, safest_asian_handicap
from football_value_pipeline_v2_standalone import devig
from test_conservative_bet_filter import fixture

# Home-minus-away goal margins. No-loss: Home +0.50 80%; Home +1.00/+1.25/+1.50 95%.
MARGINS = json.dumps({'-2': .05, '-1': .15, '0': .25, '1': .30, '2': .15, '3': .10})


def offer(side, point, price, book='bet365', opposite=None):
    return {'side': side, 'line': point, 'price': price, 'opposite_price': opposite or 2.0,
            'bookmaker': book, 'last_update_utc': '2026-10-28T12:00:00Z', 'market_key': 'alternate_spreads'}


def row(*offers, **extra):
    return {'home_team': 'Cagliari', 'away_team': 'Roma', 'goal_margin_distribution': MARGINS,
            'asian_handicap_offers': json.dumps(list(offers)), 'totals_anchor_status': 'ANCHORED_MAIN', **extra}


class SafestAsianHandicapTests(unittest.TestCase):
    def test_highest_no_loss_among_lines_with_nonnegative_ev_and_minimum_odds(self):
        result = safest_asian_handicap(row(
            offer('home', 1.5, 1.15),   # 95% no-loss, positive EV, odds below 1.20
            offer('home', 1.0, 1.05),   # 95% no-loss, negative EV
            offer('home', .5, 1.40),    # 80% no-loss, EV +12%
            offer('home', -.5, 2.10)))  # 55% no-loss, higher EV
        self.assertEqual(result['Safest AH line'], 'Cagliari +0.50')
        self.assertEqual(result['Safest AH odds and bookmaker'], '1.40 (bet365)')
        self.assertEqual(result['Safest AH expected value'], '+12.0%')
        self.assertEqual(result['Safest AH model no-loss probability'], '80.0%')
        self.assertEqual(result['Totals anchor status'], 'ANCHORED_MAIN')
        self.assertEqual(result['Safest AH reason'], '')

    def test_exactly_zero_ev_and_exactly_minimum_odds_qualify(self):
        # Home +1.50 at 1.20: EV = .95*.20 - .05 = +14%; Away +0.50 at 1.25: no-loss 45%, EV -43.75%.
        result = safest_asian_handicap(row(offer('home', 1.5, 1.20), offer('away', .5, 1.25)))
        self.assertEqual(result['Safest AH line'], 'Cagliari +1.50')
        # Away -0.50 wins on margin <= -1 (20%): EV exactly zero at 5.00.
        result = safest_asian_handicap(row(offer('away', -.5, 5.0)))
        self.assertEqual(result['Safest AH line'], 'Roma -0.50')
        self.assertEqual(result['Safest AH expected value'], '+0.0%')

    def test_equal_no_loss_prefers_higher_ev(self):
        # +1.00, +1.25 and +1.50 all avoid loss 95% of the time.
        result = safest_asian_handicap(row(
            offer('home', 1.0, 1.25), offer('home', 1.25, 1.25), offer('home', 1.5, 1.25)))
        self.assertEqual(result['Safest AH line'], 'Cagliari +1.50')
        self.assertEqual(result['Safest AH expected value'], '+18.8%')

    def test_equal_no_loss_and_ev_prefers_higher_odds(self):
        # +1.00 at 1.38: .80*.38 - .05; +1.50 at 1.32: .95*.32 - .05; both +25.4%.
        for offers in ([offer('home', 1.5, 1.32), offer('home', 1.0, 1.38)],
                       [offer('home', 1.0, 1.38), offer('home', 1.5, 1.32)]):
            with self.subTest(order=[o['line'] for o in offers]):
                result = safest_asian_handicap(row(*offers))
                self.assertEqual(result['Safest AH line'], 'Cagliari +1.00')
                self.assertEqual(result['Safest AH odds and bookmaker'], '1.38 (bet365)')

    def test_best_price_across_bookmakers_is_used(self):
        result = safest_asian_handicap(row(
            offer('home', .5, 1.35, 'Pinnacle'), offer('home', .5, 1.40, 'bet365'), offer('home', .5, 1.40, '1xBet')))
        self.assertEqual(result['Safest AH odds and bookmaker'], '1.40 (1xBet/bet365)')
        self.assertEqual(result['Safest AH expected value'], '+12.0%')

    def test_win_share_compared_with_pinnacle_on_every_quoted_line_type(self):
        # Break-even share excludes refunds: (full win + half win/2) / (that + full loss + half loss/2).
        cases = {.5: .80, 1.0: .80/.85, 1.25: (.80+.15/2)/(.80+.15/2+.05)}
        for point, share in cases.items():
            with self.subTest(point=point):
                result = safest_asian_handicap(row(offer('home', point, 1.40, 'Pinnacle', opposite=2.90)))
                fair = devig([1.40, 2.90], 'proportional')[0]
                self.assertAlmostEqual(fair, (1/1.40)/(1/1.40+1/2.90))
                self.assertEqual(result['Safest AH model break-even win share'], f'{100*share:.1f}%')
                self.assertEqual(result['Safest AH Pinnacle no-vig win share'], f'{100*fair:.1f}%')
                self.assertEqual(result['Safest AH model minus Pinnacle win share'], f'{100*(share-fair):+.1f} pp')
        # The no-loss column still counts refunds.
        self.assertEqual(result['Safest AH model no-loss probability'], '95.0%')

    def test_pinnacle_not_quoting_line_leaves_reference_blank(self):
        result = safest_asian_handicap(row(offer('home', .5, 1.40, 'bet365'), offer('home', -.5, 2.10, 'Pinnacle')))
        self.assertEqual(result['Safest AH line'], 'Cagliari +0.50')
        self.assertEqual(result['Safest AH model break-even win share'], '80.0%')
        self.assertEqual(result['Safest AH Pinnacle no-vig win share'], '—')
        self.assertEqual(result['Safest AH model minus Pinnacle win share'], '—')

    def test_blank_when_no_line_qualifies(self):
        result = safest_asian_handicap(row(offer('home', .5, 1.10), offer('home', -.5, 1.50), offer('away', .5, 1.15)))
        for column in SAFEST_AH_COLUMNS[:7]:
            self.assertEqual(result[column], '—', column)
        self.assertEqual(result['Safest AH reason'], 'No quoted line has EV >= 0 at odds >= 1.20 (3 lines checked)')
        self.assertEqual(result['Totals anchor status'], 'ANCHORED_MAIN')

    def test_blank_reasons_for_missing_inputs(self):
        cases = {
            'No Asian handicap quotes': [row(), row(asian_handicap_offers=None), row(asian_handicap_offers='not json')],
            'Model goal-margin distribution unavailable': [
                row(offer('home', .5, 1.40), goal_margin_distribution=None),
                row(offer('home', .5, 1.40), goal_margin_distribution=json.dumps({'0': .5}))],
        }
        for reason, rows in cases.items():
            for value in rows:
                with self.subTest(reason=reason):
                    result = safest_asian_handicap(value)
                    self.assertEqual(result['Safest AH line'], '—')
                    self.assertEqual(result['Safest AH reason'], reason)

    def test_readable_frame_appends_columns(self):
        frame = readable_predictions_frame(pd.DataFrame([fixture(), {**fixture(1), **row(offer('away', 2.5, 1.40))}]), {})
        self.assertEqual(list(frame.columns[-len(SAFEST_AH_COLUMNS):]), SAFEST_AH_COLUMNS)
        self.assertEqual(frame.loc[0, 'Safest AH reason'], 'No Asian handicap quotes')
        self.assertEqual(frame.loc[1, 'Safest AH line'], 'Roma +2.50')


if __name__ == '__main__':
    unittest.main()
