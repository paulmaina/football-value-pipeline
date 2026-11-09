"""Live market scope and replay for native Pinnacle quotes."""
import json
from pathlib import Path
from tempfile import TemporaryDirectory

import pandas as pd

from asian_handicap import parse_quotes, profit
from offline_test_case import OfflineQuotePolicyTestCase
import master_shortlist as master
import price_edge_cagey_shortlist as cagey
from test_price_edge_shortlist import FRESH, NOW, ah_pair, pinnacle_market, quote, row
from test_value_per_market import PIN_15

PINNACLE = {'allowed_bookmakers': ['Pinnacle'], 'per_stake_cost_bps': 0}


def forecast(home, *, extra_ah=(), double_chance=None):
    h2h, ou, _ = pinnacle_market()
    quotes = [quote('h2h', h2h), quote('totals', ou, point=2.5),
              quote('totals', PIN_15, key='alternate_totals', point=1.5)]
    if double_chance:
        quotes.append(quote('double_chance', double_chance))
    return row(offers=extra_ah, quotes=quotes, home=home, lambda_home=1.5, lambda_away=1.2,
               p_home=.45, p_draw=.27, p_away=.28)


class PinnacleMarketScopeTests(OfflineQuotePolicyTestCase):
    def test_live_eligibility_and_offline_replay_for_all_three_lists(self):
        from pipeline_health import write_generation_metadata
        from workflow_checks import raw_check

        dc = forecast('Chance FC', double_chance={'home_draw': 1.25, 'draw_away': 1.35, 'home_away': 1.4})
        away_dc = forecast('Away Chance FC',
                           double_chance={'home_draw': 1.10, 'draw_away': 1.35, 'home_away': 1.4})
        handicap = forecast('Handicap FC', extra_ah=ah_pair(3.25, 1.16, 7.0)
                            + ah_pair(0, 1.22, 5.0, key='draw_no_bet')
                            + ah_pair(3.5, 1.16, 7.0, book='1xBet'))
        forecasts = pd.DataFrame([dc, away_dc, handicap])
        value, decisions, info = cagey.build_shortlist(forecasts, NOW, execution_policy=PINNACLE)
        tier = cagey.cagey_tier_list(decisions)
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            raw = root / 'raw'
            raw.mkdir()
            forecasts.to_csv(raw / 'all_leagues_predictions.csv', index=False)
            value.to_csv(raw / 'conservative_bet_shortlist.csv', index=False)
            decisions.to_csv(raw / 'conservative_bet_rejections.csv', index=False)
            tier.to_csv(raw / cagey.TIER_FILE, index=False)
            top = master.write(decisions, raw, info, forecasts)
            self.assertEqual(info['master_shortlist']['version'], master.VERSION_PINNACLE_MARKETS)
            for frame in (value, tier, top):
                self.assertTrue(frame.bookmaker.eq('Pinnacle').all())
                self.assertIn('Asian Handicap Home +3.25', frame.market.tolist())
                self.assertTrue(frame.market.isin(['Home win', 'Away win', 'Double Chance 1X',
                    'Double Chance X2', 'Asian Handicap Home +3.25', 'Asian Handicap Home -0.25',
                    'Asian Handicap Away +0.25']).all())
                self.assertTrue(frame.market.str.startswith('Double Chance ').any())
            dc_picks = top.loc[top.market.str.startswith('Double Chance ')]
            self.assertTrue(dc_picks.master_offer_source_market.eq('double_chance').all())
            self.assertEqual(set(dc_picks.market), {'Double Chance 1X', 'Double Chance X2'})
            self.assertEqual(dict(zip(dc_picks.market, dc_picks.offered_decimal_odds)),
                             {'Double Chance 1X': 1.25, 'Double Chance X2': 1.35})
            self.assertEqual(top.home_team.nunique(), len(top))
            blocked = decisions.loc[decisions.market.isin(['Over 1.5', 'Double Chance 12']) |
                                    decisions.market_to_bet.str.startswith('Draw No Bet')]
            self.assertEqual(set(blocked.market), {'Over 1.5', 'Double Chance 12',
                                                   'Asian Handicap Home +0.00', 'Asian Handicap Away +0.00'})
            self.assertTrue(blocked.decision.eq('REJECTED').all())
            self.assertTrue(blocked.cagey_tier_decision.eq('REJECTED').all())
            (raw / 'conservative_bet_summary.json').write_text(json.dumps(info), encoding='utf-8')
            write_generation_metadata(raw, info)
            self.assertEqual(raw_check(root)['selections'], len(value))

    def test_native_zero_and_draw_no_bet_keep_separate_quote_identity(self):
        markets = [
            {'key': market, 'last_update': FRESH,
             'outcomes': [{'name': 'Home FC', 'point': p, 'price': price},
                          {'name': 'Away FC', 'point': -p, 'price': opposite}]}
            for market, p, price, opposite in (
                ('spreads', 0, 1.9, 1.9), ('draw_no_bet', 0, 1.9, 1.9),
                ('alternate_spreads', 3.25, 1.16, 7.0))]
        quotes = parse_quotes({'home_team': 'Home FC', 'away_team': 'Away FC',
                               'commence_time': (NOW + pd.Timedelta(hours=2)).isoformat(),
                               'bookmakers': [{'title': 'Pinnacle', 'markets': markets}]}, NOW)
        self.assertEqual(len(quotes), 6)
        self.assertEqual({q['market_key'] for q in quotes if q['line'] == 0}, {'spreads', 'draw_no_bet'})
        status, gain = profit(0, 3, 'home', 3.25, 1.16)
        self.assertEqual(status, 'HALF_WON')
        self.assertAlmostEqual(gain, .08)
