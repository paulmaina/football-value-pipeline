"""Display-only safest Asian handicap columns in the readable prediction files: the quoted Pinnacle line the cagey
tier rates safest, with research's no-loss on the same line beside it (readable_views.safest_ah)."""
import json
import unittest

import pandas as pd

import readable_views as rv
from format_football_output import SAFEST_AH_COLUMNS, readable_predictions_frame, safest_ah_values
from football_value_pipeline_v2_standalone import devig
from test_conservative_bet_filter import fixture

# Home-minus-away goal margins. No-loss: Home +0.50 80%; Home +1.00/+1.25/+1.50 95%.
MARGINS = json.dumps({'-2': .05, '-1': .15, '0': .25, '1': .30, '2': .15, '3': .10})
CAGEY = {'margin_distribution': json.loads(MARGINS)}
# Research: a flatter view of the same match (Home +0.50 no-loss 70%).
RESEARCH = {'margin_distribution': {'-2': .10, '-1': .20, '0': .25, '1': .25, '2': .12, '3': .08}}


def offer(side, point, price, book='Pinnacle', opposite=None):
    """One AH quote in the asian_handicap_offers capture format (home side carries the pair)."""
    return {'side': side, 'line': point, 'price': price, 'opposite_price': opposite or 2.0,
            'bookmaker': book, 'last_update_utc': '2026-10-28T12:00:00Z', 'market_key': 'alternate_spreads'}


def row(*offers, **extra):
    return {'home_team': 'Cagliari', 'away_team': 'Roma', 'asian_handicap_offers': json.dumps(list(offers)), **extra}


def safest(*offers, cagey=CAGEY, research=RESEARCH):
    value = row(*offers)
    return rv.safest_ah(value, rv.view_ah_no_loss(value, research, cagey), cagey)


class SafestAsianHandicapTests(unittest.TestCase):
    def test_highest_cagey_no_loss_among_lines_with_nonnegative_ev_and_minimum_odds(self):
        result = safest(
            offer('home', 1.5, 1.15, opposite=5.0),   # 95% no-loss, positive EV, odds below 1.20
            offer('home', 1.0, 1.05, opposite=8.0),   # 95% no-loss, negative EV
            offer('home', .5, 1.40, opposite=2.9),    # 80% no-loss, EV +12%
            offer('home', -.5, 2.10, opposite=1.7))   # 55% no-loss, higher EV
        self.assertEqual(result['label'], 'Cagliari +0.50')
        self.assertEqual(result['price'], 1.40)
        self.assertAlmostEqual(result['ev'], .12)
        self.assertAlmostEqual(result['cagey'], .80)
        self.assertAlmostEqual(result['research'], .70)  # research's no-loss on the same line, beside it

    def test_exactly_zero_ev_and_exactly_minimum_odds_qualify(self):
        # Home +1.50 at 1.20: EV = .95*.20 - .05 = +14%; Roma -1.50 at 1.25 loses money.
        self.assertEqual(safest(offer('home', 1.5, 1.20, opposite=1.25))['label'], 'Cagliari +1.50')
        # Away -0.50 wins on margin <= -1 (20%): EV exactly zero at 5.00 (Cagliari +0.50 at 1.10 is below 1.20).
        result = safest(offer('home', .5, 1.10, opposite=5.0))
        self.assertEqual(result['label'], 'Roma -0.50')
        self.assertAlmostEqual(result['ev'], 0.)

    def test_equal_no_loss_prefers_higher_ev_then_higher_odds(self):
        result = safest(offer('home', 1.0, 1.25, opposite=4.0), offer('home', 1.25, 1.25, opposite=4.0),
                        offer('home', 1.5, 1.25, opposite=4.0))
        self.assertEqual(result['label'], 'Cagliari +1.50')
        self.assertAlmostEqual(result['ev'], .1875)
        # +1.00 at 1.38: .80*.38 - .05; +1.50 at 1.32: .95*.32 - .05; both +25.4%.
        for offers in ([offer('home', 1.5, 1.32, opposite=4.0), offer('home', 1.0, 1.38, opposite=3.5)],
                       [offer('home', 1.0, 1.38, opposite=3.5), offer('home', 1.5, 1.32, opposite=4.0)]):
            with self.subTest(order=[o['line'] for o in offers]):
                self.assertEqual(safest(*offers)['label'], 'Cagliari +1.00')

    def test_only_pinnacle_quotes_count(self):
        # Bets are placed at Pinnacle only: a better bet365 price is not a quoted line here.
        result = safest(offer('home', .5, 1.45, book='bet365'), offer('home', .5, 1.35, opposite=3.2))
        self.assertEqual(result['price'], 1.35)
        self.assertEqual(rv.quoted_ah_lines(row(offer('home', .5, 1.45, book='bet365'))), [])

    def test_win_share_compared_with_pinnacle_on_every_quoted_line_type(self):
        # Break-even share excludes refunds: (full win + half win/2) / (that + full loss + half loss/2).
        cases = {.5: .80, 1.0: .80/.85, 1.25: (.80+.15/2)/(.80+.15/2+.05)}
        for point, share in cases.items():
            with self.subTest(point=point):
                result = safest(offer('home', point, 1.40, opposite=2.90))
                fair = devig([1.40, 2.90], 'proportional')[0]
                self.assertAlmostEqual(result['share'], share)
                self.assertAlmostEqual(result['pinnacle_share'], fair)
                values = safest_ah_values({'safest': result})
                self.assertEqual(values['Safest AH cagey minus Pinnacle win share'], f'{100*(share-fair):+.1f} pp')
        self.assertAlmostEqual(result['cagey'], .95)  # the no-loss column still counts refunds

    def test_blank_reasons(self):
        self.assertEqual(safest(offer('home', .5, 1.10, opposite=1.9), offer('home', -.5, 1.50, opposite=1.15))
                         ['reason'], 'No quoted Pinnacle line has cagey EV >= 0 at odds >= 1.20 (4 lines checked)')
        self.assertEqual(safest()['reason'], 'No Pinnacle Asian handicap quotes')
        no_cagey = {'reason': 'no cagey grid: needs Pinnacle 1X2 and O/U 2.5 (no Pinnacle O/U 2.5 quote)'}
        self.assertEqual(safest(offer('home', .5, 1.40), cagey=no_cagey)['reason'], no_cagey['reason'])
        values = safest_ah_values({'safest': {'reason': 'why'}})
        self.assertEqual([values[c] for c in SAFEST_AH_COLUMNS[:-1]], ['—'] * (len(SAFEST_AH_COLUMNS) - 1))
        self.assertEqual(values['Safest AH reason'], 'why')

    def test_readable_frame_keeps_the_columns_together_before_the_benchmark(self):
        frame = readable_predictions_frame(pd.DataFrame([fixture(), {**fixture(1), **row(offer('away', 2.5, 1.40))}]),
                                           {})
        columns = list(frame.columns)
        at = columns.index(SAFEST_AH_COLUMNS[0])
        self.assertEqual(columns[at:at + len(SAFEST_AH_COLUMNS)], SAFEST_AH_COLUMNS)
        self.assertLess(at, min(i for i, c in enumerate(columns) if c.startswith('Benchmark ')))
        # Without a run bundle there is no run clock, so no cagey grid: the reason says so.
        self.assertEqual(frame.loc[0, 'Safest AH reason'], 'no cagey grid: run clock not recorded in this bundle')


if __name__ == '__main__':
    unittest.main()
