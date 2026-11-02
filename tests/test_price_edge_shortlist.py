"""Production policy v27: AH price edge against Pinnacle's fair price."""

from offline_test_case import OfflineQuotePolicyTestCase
import json
import math
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import pandas as pd

import market_implied as mi
import price_edge_shortlist as v27
from asian_handicap import PRODUCTION_POLICY, POLICIES, profit, label
from conservative_bet_filter import build_conservative_shortlist
from performance_tracking import result_for_market

NOW = pd.Timestamp('2026-11-07T12:00:00Z')
FRESH = (NOW - pd.Timedelta(minutes=1)).isoformat()
POLICY = {'allowed_bookmakers': ['Pinnacle', '1xBet'], 'per_stake_cost_bps': 0}
# Pinnacle market drawn from one known matrix, so fit B is usable (3% margin).
LAMBDAS = (1.5, 1.2, -0.05)
MAIN_LINE = -0.25


def pinnacle_market(margin=1.03):
    matrix = mi.dixon_coles_matrix(*LAMBDAS)
    inputs = mi.model_inputs(matrix, MAIN_LINE)
    h2h = {k: round(1 / (inputs[k] * margin), 4) for k in ('home', 'draw', 'away')}
    ou = {'over': round(1 / (inputs['over_2_5'] * margin), 4), 'under': round(1 / ((1 - inputs['over_2_5']) * margin), 4)}
    ah = (round(1 / (inputs['ah_main'] * margin), 4), round(1 / ((1 - inputs['ah_main']) * margin), 4))
    return h2h, ou, ah


def ah_pair(line, home, away, book='Pinnacle', stamp=FRESH, key='alternate_spreads'):
    """Both sides of one home line, as asian_handicap.parse_quotes stores them."""
    return [{'side': 'home', 'line': line, 'price': home, 'opposite_price': away, 'bookmaker': book,
             'last_update_utc': stamp, 'market_key': key, 'quote_source': 'The Odds API'},
            {'side': 'away', 'line': -line if line else 0.0, 'price': away, 'opposite_price': home, 'bookmaker': book,
             'last_update_utc': stamp, 'market_key': key, 'quote_source': 'The Odds API'}]


def offer(side, line, price, book='1xBet', stamp=FRESH, key='alternate_spreads'):
    return {'side': side, 'line': line, 'price': price, 'opposite_price': 1.5, 'bookmaker': book,
            'last_update_utc': stamp, 'market_key': key, 'quote_source': 'The Odds API'}


def quote(market, prices, book='Pinnacle', stamp=FRESH, key=None, point=None):
    return {'bookmaker': book, 'market': market, 'market_key': key or market, 'point': point,
            'prices': prices, 'last_update_utc': stamp}


def row(offers=(), quotes=None, kickoff=NOW + pd.Timedelta(hours=24), home='Home FC', pin_stamp=FRESH, **extra):
    h2h, ou, ah = pinnacle_market()
    if quotes is None:
        quotes = [quote('h2h', h2h, stamp=pin_stamp), quote('totals', ou, key='totals', point=2.5, stamp=pin_stamp)]
    main = ah_pair(MAIN_LINE, *ah, stamp=pin_stamp, key='spreads')
    data = {'league': 'Premier League', 'home_team': home, 'away_team': 'Away FC', 'fixture_id': 'f-' + home,
            'date': str(kickoff.date()), 'kickoff_utc': kickoff.isoformat(),
            'asian_handicap_offers': json.dumps(main + list(offers)), 'price_edge_quotes': json.dumps(quotes)}
    data.update(extra)
    return data


def evaluate(*rows, policy=POLICY):
    return v27.build_shortlist(pd.DataFrame(list(rows)), NOW, execution_policy=policy)


def decision(decisions, market_to_bet, book='1xBet'):
    part = decisions[(decisions.market_to_bet == market_to_bet) & (decisions.bookmaker == book)]
    assert len(part) == 1, (market_to_bet, len(part))
    return part.iloc[0]


def fit_price(side, line):
    h2h, ou, ah = pinnacle_market()
    targets = mi.targets_from_prices(tuple(h2h[k] for k in ('home', 'draw', 'away')), (ou['over'], ou['under']),
                                     (MAIN_LINE, *ah))
    return mi.price(mi.fit(targets, include_ah=True), side, line)


class EquivalenceTests(OfflineQuotePolicyTestCase):
    def test_equivalent_markets_settle_identically_to_their_ah_line(self):
        pairs = {'Home win': ('home', -0.5), 'Away win': ('away', -0.5),
                 'Double Chance 1X': ('home', 0.5), 'Double Chance X2': ('away', 0.5)}
        for h in range(7):
            for a in range(7):
                for market, (side, line) in pairs.items():
                    status, gain = profit(h, a, side, line, 2.0)
                    self.assertEqual(result_for_market(market, h, a), status == 'WON', (market, h, a))
                    self.assertIn(status, ('WON', 'LOST'))
                # Draw no bet = AH 0: refund on a draw, otherwise a straight win or loss.
                for side, wins in (('home', h > a), ('away', a > h)):
                    status, _ = profit(h, a, side, 0.0, 2.0)
                    self.assertEqual(status, 'REFUNDED' if h == a else 'WON' if wins else 'LOST')

    def test_equivalent_candidates_carry_their_ah_line(self):
        quotes = [quote('h2h', {'home': 2.2, 'draw': 3.4, 'away': 3.3}, book='1xBet'),
                  quote('double_chance', {'home_draw': 1.3, 'draw_away': 1.6, 'home_away': 1.3}, book='1xBet')]
        items = v27.offered_candidates(row(quotes=quotes, offers=[offer('home', 0.0, 1.6, key='draw_no_bet')]), POLICY)
        found = {(c['market_to_bet'], c['side'], c['line']) for c in items}
        self.assertTrue({('Home win', 'home', -0.5), ('Away win', 'away', -0.5), ('Double Chance 1X', 'home', 0.5),
                         ('Double Chance X2', 'away', 0.5), ('Draw No Bet Home', 'home', 0.0)} <= found)
        self.assertFalse(any('Draw' == c['market_to_bet'] or '12' in c['market_to_bet'] for c in items))


class ReferenceTests(OfflineQuotePolicyTestCase):
    def test_same_line_pinnacle_is_reference_a(self):
        _, decisions, _ = evaluate(row(offers=[*ah_pair(1.0, 1.25, 4.10), offer('home', 1.0, 1.30)]))
        item = decision(decisions, label('home', 1.0))
        self.assertEqual(item.reference_type, 'a')
        self.assertAlmostEqual(item.fair_probability, (1 / 1.25) / (1 / 1.25 + 1 / 4.10))
        self.assertIsNotNone(item.fair_probability_shin)

    def test_half_line_without_pinnacle_pair_uses_1x2_reference_b(self):
        quotes = [quote('double_chance', {'home_draw': 1.40, 'draw_away': 1.6, 'home_away': 1.3}, book='1xBet')]
        h2h, ou, _ = pinnacle_market()
        base = [quote('h2h', h2h), quote('totals', ou, key='totals', point=2.5)]
        _, decisions, _ = evaluate(row(quotes=base + quotes))
        item = decision(decisions, 'Double Chance 1X')
        self.assertEqual(item.reference_type, 'b')
        home, draw, away = mi.devig_three_way(h2h['home'], h2h['draw'], h2h['away'])
        self.assertAlmostEqual(item.fair_probability, 1 - away)

    def test_draw_no_bet_uses_pinnacle_draw_no_bet_as_reference_b(self):
        dnb = [dict(o, market_key='draw_no_bet') for o in ah_pair(0.0, 1.70, 2.25)]
        _, decisions, _ = evaluate(row(offers=[*dnb, offer('home', 0.0, 1.80, key='draw_no_bet')]))
        item = decision(decisions, 'Draw No Bet Home')
        self.assertEqual((item.reference_type, item.reference_market), ('b', 'Pinnacle draw no bet'))

    def test_derived_reference_only_when_a_and_b_missing_and_plus_line(self):
        fair = fit_price('away', 1.0)['fair_odds']
        _, decisions, _ = evaluate(row(offers=[offer('away', 1.0, round(fair * 1.04, 4))]))
        item = decision(decisions, label('away', 1.0))
        self.assertEqual(item.reference_type, 'c')
        self.assertAlmostEqual(item.fair_odds, fair, places=6)
        self.assertEqual(item.decision, 'SHORTLISTED')
        # With Pinnacle's same line present, the derived price is never used.
        _, decisions, _ = evaluate(row(offers=[*ah_pair(-1.0, 3.0, 1.40), offer('away', 1.0, round(fair * 1.04, 4))]))
        self.assertEqual(decision(decisions, label('away', 1.0)).reference_type, 'a')

    def test_minus_line_with_only_a_derived_price_rejects(self):
        _, decisions, _ = evaluate(row(offers=[offer('home', -1.0, 2.90)]))
        item = decision(decisions, label('home', -1.0))
        self.assertEqual(item.decision, 'REJECTED')
        self.assertIn(v27.NO_REFERENCE, item.rejection_reasons)
        self.assertTrue(pd.isna(item.reference_type))

    def test_no_reference_at_all_fails_closed(self):
        _, decisions, summary = evaluate(row(quotes=[], offers=[offer('away', 1.0, 1.80)],
                                             asian_handicap_offers=json.dumps([offer('away', 1.0, 1.80)])))
        item = decision(decisions, label('away', 1.0))
        self.assertEqual(item.decision, 'REJECTED')
        self.assertEqual(item.rejection_reasons, v27.NO_REFERENCE)
        self.assertFalse(item.fit_usable)
        self.assertEqual(summary['n_shortlisted'], 0)


class ThresholdTests(OfflineQuotePolicyTestCase):
    def test_pinnacle_reference_qualifies_at_two_percent_not_below(self):
        pair = ah_pair(-0.75, 1.95, 1.95)
        _, ok, _ = evaluate(row(offers=[*pair, offer('home', -0.75, 2.04)]))
        _, low, _ = evaluate(row(offers=[*pair, offer('home', -0.75, 2.0398)]))
        self.assertEqual(decision(ok, label('home', -0.75)).decision, 'SHORTLISTED')
        rejected = decision(low, label('home', -0.75))
        self.assertEqual(rejected.rejection_reasons, 'edge below 2%')
        self.assertAlmostEqual(rejected.edge, 0.0199, places=10)
        self.assertAlmostEqual(decision(ok, label('home', -0.75)).minimum_odds, 2.0 * 1.02)

    def test_derived_reference_qualifies_at_three_percent_not_below(self):
        fair = fit_price('away', 1.0)['fair_odds']
        q = 1 / fair
        _, ok, _ = evaluate(row(offers=[offer('away', 1.0, 1.03 / q)]))
        _, low, _ = evaluate(row(offers=[offer('away', 1.0, 1.0299 / q)]))
        self.assertEqual(decision(ok, label('away', 1.0)).decision, 'SHORTLISTED')
        self.assertEqual(decision(low, label('away', 1.0)).rejection_reasons, 'edge below 3%')
        self.assertAlmostEqual(decision(ok, label('away', 1.0)).minimum_odds, fair * 1.03)


class TagTests(OfflineQuotePolicyTestCase):
    def test_tag_boundaries(self):
        self.assertTrue(v27.tag_flags(2.00, 3.50)['balanced'])
        self.assertTrue(v27.tag_flags(3.50, 2.00)['balanced'])
        self.assertFalse(v27.tag_flags(1.99, 3.00)['balanced'])
        self.assertFalse(v27.tag_flags(2.50, 3.51)['balanced'])
        self.assertTrue(v27.tag_flags(over_probability=0.4499)['low_total'])
        self.assertFalse(v27.tag_flags(over_probability=0.45)['low_total'])
        self.assertTrue(v27.tag_flags(draw_probability=0.27)['high_draw'])
        self.assertFalse(v27.tag_flags(draw_probability=0.2699)['high_draw'])
        self.assertEqual(v27.tag_flags(), {'balanced': False, 'low_total': False, 'high_draw': False, 'even_odds': False})

    def test_even_odds_boundaries(self):
        self.assertTrue(v27.tag_flags(2.50, 2.50)['even_odds'])
        self.assertTrue(v27.tag_flags(4.00, 2.50)['even_odds'])
        self.assertFalse(v27.tag_flags(2.49, 2.50)['even_odds'])
        self.assertFalse(v27.tag_flags(2.50, 2.49)['even_odds'])
        self.assertFalse(v27.tag_flags(None, 3.00)['even_odds'])
        # Independent of balanced: 3.60 / 2.60 is even_odds but not balanced.
        self.assertEqual((v27.tag_flags(3.60, 2.60)['even_odds'], v27.tag_flags(3.60, 2.60)['balanced']), (True, False))

    def test_even_odds_fixture_gets_plus_line_probes_and_no_decision_change(self):
        even = [quote('h2h', {'home': 3.60, 'draw': 3.40, 'away': 2.60}),
                quote('totals', {'over': 1.80, 'under': 2.10}, key='totals', point=2.5)]
        _, decisions, summary = evaluate(row(quotes=even))
        self.assertTrue(decisions.even_odds.all())
        self.assertFalse(decisions.balanced.any())
        probes = decisions[decisions.tagged_probe.astype(bool)]
        self.assertEqual(len(probes), 2 * len(v27.TAGGED_LINES))
        self.assertEqual(summary['tagged_candidates']['even_odds'], len(decisions))
        self.assertIn('even_odds', v27.OUTPUT_COLUMNS)

    def test_tags_never_change_a_decision(self):
        offers = [*ah_pair(-0.75, 1.95, 1.95), offer('home', -0.75, 2.05), offer('home', -0.75, 1.90),
                  offer('away', 1.0, 1.50), offer('away', 1.0, 2.60), offer('home', -1.0, 2.9)]
        outcomes = []
        for value in (True, False):
            forced = lambda h2h, ou25, value=value: {**{t: value for t in v27.TAGS}, 'any_tag': False,
                                                     'pinnacle_home_odds': None, 'pinnacle_away_odds': None,
                                                     'pinnacle_draw_probability': None,
                                                     'pinnacle_over_2_5_probability': None}
            with patch.object(v27, 'tags', forced):
                _, decisions, _ = evaluate(row(offers=offers))
            outcomes.append(decisions[['market_to_bet', 'bookmaker', 'offered_decimal_odds', 'decision',
                                       'rejection_reasons']].to_dict('records'))
        self.assertEqual(outcomes[0], outcomes[1])

    def test_tagged_fixture_always_records_plus_lines_both_sides(self):
        balanced = [quote('h2h', {'home': 2.6, 'draw': 3.2, 'away': 2.9}),
                    quote('totals', {'over': 2.10, 'under': 1.80}, key='totals', point=2.5)]
        _, decisions, summary = evaluate(row(quotes=balanced))
        probes = decisions[decisions.tagged_probe.astype(bool)]
        self.assertEqual({(r.handicap_side, r.handicap_line) for r in probes.itertuples()},
                         {(s, x) for s in ('home', 'away') for x in v27.TAGGED_LINES})
        self.assertTrue((probes.rejection_reasons.str.contains(v27.NO_OFFER)).all())
        self.assertTrue(probes.balanced.all() and probes.high_draw.all())
        self.assertEqual(summary['tagged_candidates']['balanced'], len(decisions))
        # Untagged fixtures get no probes.
        lopsided = [quote('h2h', {'home': 1.30, 'draw': 5.5, 'away': 9.0}),
                    quote('totals', {'over': 1.60, 'under': 2.40}, key='totals', point=2.5)]
        _, decisions, _ = evaluate(row(quotes=lopsided))
        self.assertFalse(decisions.tagged_probe.astype(bool).any())


class GuardTests(OfflineQuotePolicyTestCase):
    def reasons(self, offers, **kwargs):
        _, decisions, _ = evaluate(row(offers=[*ah_pair(-0.75, 1.95, 1.95), *offers], **kwargs))
        return decision(decisions, label('home', -0.75)).rejection_reasons

    def test_each_guard_rejects_with_its_reason(self):
        good = offer('home', -0.75, 2.10)
        self.assertEqual(self.reasons([good]), '')
        self.assertIn('kickoff outside 20-minute to 48-hour window',
                      self.reasons([good], kickoff=NOW + pd.Timedelta(hours=49)))
        self.assertIn('kickoff outside 20-minute to 48-hour window',
                      self.reasons([good], kickoff=NOW + pd.Timedelta(minutes=19)))
        stale = (NOW - pd.Timedelta(hours=25)).isoformat()
        self.assertIn('offered quote stale', self.reasons([offer('home', -0.75, 2.10, stamp=stale)]))
        self.assertIn('offered and Pinnacle quotes more than 10 minutes apart',
                      self.reasons([offer('home', -0.75, 2.10, stamp=(NOW - pd.Timedelta(minutes=12)).isoformat())]))
        self.assertIn('offered price above 1.15 x fair odds', self.reasons([offer('home', -0.75, 2.31)]))

    def test_stale_pinnacle_and_overround_and_long_odds(self):
        stale = (NOW - pd.Timedelta(hours=25)).isoformat()
        _, decisions, _ = evaluate(row(offers=[*ah_pair(-0.75, 1.95, 1.95, stamp=stale), offer('home', -0.75, 2.10)]))
        self.assertIn('Pinnacle quote stale', decision(decisions, label('home', -0.75)).rejection_reasons)
        _, decisions, _ = evaluate(row(offers=[*ah_pair(-0.75, 1.80, 1.80), offer('home', -0.75, 2.00)]))
        self.assertIn('Pinnacle overround outside [1.00, 1.10]', decision(decisions, label('home', -0.75)).rejection_reasons)
        _, decisions, _ = evaluate(row(offers=[*ah_pair(-1.75, 3.30, 1.36), offer('home', -1.75, 3.50)]))
        item = decision(decisions, label('home', -1.75))
        self.assertEqual(item.rejection_reasons, 'offered odds above 3.00')
        self.assertGreater(item.edge, 0.02)

    def test_bet365_and_unknown_books_are_not_candidates(self):
        _, decisions, _ = evaluate(row(offers=[*ah_pair(-0.75, 1.95, 1.95), offer('home', -0.75, 2.10, book='bet365')]))
        self.assertFalse((decisions.bookmaker == 'bet365').any())


class SelectionTests(OfflineQuotePolicyTestCase):
    def test_one_row_per_fixture_safest_first_with_other_value_lines(self):
        fair_plus = fit_price('away', 1.0)['fair_odds']
        first = row(home='Alpha', offers=[*ah_pair(-0.75, 1.95, 1.95), offer('home', -0.75, 2.10),
                                          offer('away', 1.0, round(fair_plus * 1.05, 4))])
        second = row(home='Beta', offers=[*ah_pair(-2.0, 4.0, 1.28), offer('away', 2.0, 1.36)])
        selected, decisions, summary = evaluate(first, second)
        self.assertEqual(len(selected), 2)
        self.assertEqual(selected.home_team.tolist(), ['Beta', 'Alpha'])
        self.assertTrue(selected.pinnacle_no_loss_probability.is_monotonic_decreasing)
        alpha = selected.iloc[1]
        self.assertEqual(alpha.market_to_bet, label('away', 1.0))  # safer than home -0.75
        self.assertIn(label('home', -0.75), alpha.other_value_lines)
        self.assertEqual((decisions.decision == 'NOT_SELECTED').sum(), 1)
        self.assertEqual(set(v27.OUTPUT_COLUMNS) - set(selected.columns), set())
        self.assertEqual(summary['n_shortlisted'], 2)
        self.assertIsNone(summary['target_distinct_matches'])

    def test_ties_break_on_edge_then_odds(self):
        frame = pd.DataFrame({'pinnacle_no_loss_probability': [0.6, 0.6, 0.6, None], 'edge': [0.03, 0.05, 0.05, 0.9],
                              'offered_decimal_odds': [2.0, 1.9, 2.0, 2.5], 'kickoff_utc': ['k'] * 4,
                              'market': ['m'] * 4, 'bookmaker': ['b'] * 4})
        self.assertEqual(v27._rank(frame).index.tolist(), [2, 1, 0, 3])

    def test_production_constant_dispatch_and_v26_still_replayable(self):
        self.assertEqual(PRODUCTION_POLICY, v27.POLICY)
        self.assertIn('48h-zero-tolerance-ev05-no-loss75-corners-v26', POLICIES)
        frame = pd.DataFrame([row(offers=[*ah_pair(-0.75, 1.95, 1.95), offer('home', -0.75, 2.10)])])
        selected, _, summary = build_conservative_shortlist(frame, as_of=NOW, execution_policy=POLICY,
                                                            selection_policy_version=PRODUCTION_POLICY)
        self.assertEqual(summary['selection_policy_version'], v27.POLICY)
        self.assertEqual(len(selected), 1)
        with self.assertRaises(ValueError):
            build_conservative_shortlist(frame, as_of=NOW, execution_policy=POLICY, adjusted_ev_floor=0.02,
                                         selection_policy_version=PRODUCTION_POLICY)

    def test_naive_clock_rejected(self):
        with self.assertRaises(ValueError):
            v27.build_shortlist(pd.DataFrame([row()]), pd.Timestamp('2026-11-07T12:00'))


class CaptureTests(OfflineQuotePolicyTestCase):
    def payload(self):
        return {'home_team': 'Home FC', 'away_team': 'Away FC', 'bookmakers': [
            {'key': 'pinnacle', 'title': 'Pinnacle', 'markets': [
                {'key': 'h2h', 'last_update': FRESH, 'outcomes': [
                    {'name': 'Home FC', 'price': 2.1}, {'name': 'Draw', 'price': 3.4}, {'name': 'Away FC', 'price': 3.6}]},
                {'key': 'totals', 'last_update': FRESH, 'outcomes': [
                    {'name': 'Over', 'point': 2.5, 'price': 1.9}, {'name': 'Under', 'point': 2.5, 'price': 1.95},
                    {'name': 'Over', 'point': 3.5, 'price': 3.1}]}]},
            {'key': 'onexbet', 'title': '1xBet', 'markets': [
                {'key': 'double_chance', 'last_update': FRESH, 'outcomes': [
                    {'name': 'Home FC or Draw', 'price': 1.3}, {'name': 'Draw or Away FC', 'price': 1.7},
                    {'name': 'Home FC or Away FC', 'price': 1.3}]},
                {'key': 'h2h', 'last_update': FRESH, 'outcomes': [{'name': 'Home FC', 'price': 2.2}]}]},
            {'key': 'williamhill', 'title': 'William Hill', 'markets': [
                {'key': 'h2h', 'last_update': FRESH, 'outcomes': [
                    {'name': 'Home FC', 'price': 2.1}, {'name': 'Draw', 'price': 3.4}, {'name': 'Away FC', 'price': 3.6}]}]}]}

    def test_capture_keeps_complete_sets_from_known_books_only(self):
        found = v27.capture_quotes(self.payload(), NOW, ('h2h', 'totals', 'double_chance'))
        keys = sorted((q['bookmaker'], q['market']) for q in found)
        self.assertEqual(keys, [('1xBet', 'double_chance'), ('Pinnacle', 'h2h'), ('Pinnacle', 'totals')])
        totals = [q for q in found if q['market'] == 'totals'][0]
        self.assertEqual((totals['point'], totals['prices']), (2.5, {'over': 1.9, 'under': 1.95}))
        late = NOW + pd.Timedelta(days=2)
        self.assertEqual(v27.capture_quotes(self.payload(), late, ('h2h',)), [])
        self.assertEqual(v27.capture_quotes({'home_team': 'X', 'away_team': 'X'}, NOW, ('h2h',)), [])

    def test_merge_keeps_newest_per_book_and_market(self):
        old = [quote('h2h', {'home': 2.0, 'draw': 3, 'away': 4}, stamp='2026-11-07T10:00:00+00:00')]
        new = [quote('h2h', {'home': 2.1, 'draw': 3, 'away': 4}, stamp='2026-11-07T11:00:00+00:00'),
               quote('double_chance', {'home_draw': 1.3, 'draw_away': 1.7, 'home_away': 1.3})]
        merged = json.loads(v27.merge_quotes(json.dumps(old), new))
        self.assertEqual(len(merged), 2)
        self.assertEqual([q['prices']['home'] for q in merged if q['market'] == 'h2h'], [2.1])

    def test_legacy_rows_fall_back_to_pinnacle_reference_fields(self):
        h2h, ou, ah = pinnacle_market()
        legacy = row(quotes=[], market_source_1x2='The Odds API / Pinnacle',
                     market_reference_home_odds=h2h['home'], market_reference_draw_odds=h2h['draw'],
                     market_reference_away_odds=h2h['away'], market_reference_1x2_last_update_utc=FRESH,
                     totals_anchor_reference_source='live_pinnacle_main', totals_anchor_reference_over_odds=ou['over'],
                     totals_anchor_reference_under_odds=ou['under'], totals_anchor_reference_last_update_utc=FRESH,
                     best_home_draw_bookmaker='1xBet', market_home_draw_odds=1.40,
                     market_best_home_draw_last_update_utc=FRESH)
        pin = v27.pinnacle_quotes(legacy)
        self.assertEqual(pin['h2h'][:3], (h2h['home'], h2h['draw'], h2h['away']))
        self.assertEqual(pin['main_line'], MAIN_LINE)
        _, decisions, _ = evaluate(legacy)
        self.assertEqual(decision(decisions, 'Double Chance 1X').reference_type, 'b')
        self.assertTrue(decisions.fit_usable.all())


class OutputTests(OfflineQuotePolicyTestCase):
    def test_raw_check_replays_and_readable_report_renders(self):
        from workflow_checks import raw_check
        from format_football_output import process_conservative_shortlist
        predictions = pd.DataFrame([row(offers=[*ah_pair(-0.75, 1.95, 1.95), offer('home', -0.75, 2.10)]),
                                    row(home='Other')])
        predictions['p_home'], predictions['p_draw'], predictions['p_away'] = 0.45, 0.27, 0.28
        selected, decisions, summary = v27.build_shortlist(predictions, NOW, execution_policy=POLICY)
        with tempfile.TemporaryDirectory() as tmp:
            raw = Path(tmp) / 'raw'
            raw.mkdir()
            predictions.to_csv(raw / 'all_leagues_predictions.csv', index=False)
            selected.to_csv(raw / 'conservative_bet_shortlist.csv', index=False)
            decisions.to_csv(raw / 'conservative_bet_rejections.csv', index=False)
            (raw / 'conservative_bet_summary.json').write_text(json.dumps(summary), encoding='utf-8')
            self.assertEqual(raw_check(Path(tmp), raw_dir=raw)['selections'], 1)
            out = Path(tmp) / 'readable'
            out.mkdir()
            self.assertEqual(process_conservative_shortlist(raw, out), 1)
            report = (out / 'conservative_bet_shortlist_report.md').read_text(encoding='utf-8')
            readable = pd.read_csv(out / 'conservative_bet_shortlist_readable.csv')
        self.assertIn('price edge vs Pinnacle (v27)', report)
        self.assertIn('Rejections by reason', report)
        self.assertEqual(readable['Reference'].tolist(), ['a: Pinnacle same AH line'])
        self.assertEqual(readable['Minimum odds still worth taking'].tolist(), [2.04])

    def test_best_per_match_uses_v27_ranking(self):
        from asian_handicap import best_per_match
        _, decisions, _ = evaluate(row(offers=[*ah_pair(-0.75, 1.95, 1.95), offer('home', -0.75, 2.10)]))
        best = best_per_match(decisions)
        self.assertEqual(best.market.tolist(), [label('home', -0.75)])


if __name__ == '__main__':
    unittest.main()
