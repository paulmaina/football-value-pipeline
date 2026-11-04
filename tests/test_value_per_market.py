"""per-market-v2 value rule: one pick per fixture and market group, 1% minimum edge in every group."""

from offline_test_case import OfflineQuotePolicyTestCase
import json
import tempfile
import unittest
from pathlib import Path

import pandas as pd

import market_implied as mi
import price_edge_cagey_shortlist as v28
import price_edge_shortlist as v27
from test_price_edge_shortlist import NOW, FRESH, POLICY, ah_pair, offer, pinnacle_market, quote, row

V1 = {'cagey_correction_enabled': True, 'cagey_tier_enabled': False, 'value_rule': v28.VALUE_RULE_ONE}
V2 = {**V1, 'value_rule': v28.VALUE_RULE_PER_MARKET}
# Pinnacle's over/under 1.5 for the shared fixture (3% margin around a 75% over chance).
PIN_15 = {'over': round(1 / (0.75 * 1.03), 4), 'under': round(1 / (0.25 * 1.03), 4)}


def run(*rows, settings=V2, monitor=None):
    return v28.build_shortlist(pd.DataFrame(list(rows)), NOW, execution_policy=POLICY, settings=settings,
                               monitor=monitor)


def fair(market):
    """Pinnacle fair win chance of a 1X2 / double chance / over 1.5 selection for the shared fixture."""
    h2h, _, _ = pinnacle_market()
    home, draw, away = mi.devig_three_way(h2h['home'], h2h['draw'], h2h['away'])
    return {'home': home, 'away': away, 'home_draw': 1 - away, 'draw_away': 1 - home,
            'over_1_5': (1 / PIN_15['over']) / (1 / PIN_15['over'] + 1 / PIN_15['under'])}[market]


def price_at(market, edge):
    return round((1 + edge) / fair(market), 4)


def fixture(*extra_quotes, offers=(), with_pin_15=True, **kw):
    h2h, ou, _ = pinnacle_market()
    quotes = [quote('h2h', h2h), quote('totals', ou, key='totals', point=2.5)]
    if with_pin_15:
        quotes.append(quote('totals', PIN_15, key='alternate_totals', point=1.5))
    return row(offers=offers, quotes=quotes + list(extra_quotes), **kw)


def h2h_1xbet(home=None, away=None):
    h2h, _, _ = pinnacle_market()
    return quote('h2h', {'home': home or h2h['home'] * 0.9, 'draw': h2h['draw'] * 0.9, 'away': away or h2h['away'] * 0.9},
                 book='1xBet')


def over_1xbet(price, stamp=FRESH):
    return quote('totals', {'over': price, 'under': 3.0}, book='1xBet', key='alternate_totals', point=1.5, stamp=stamp)


def decision_row(decisions, label, book='1xBet'):
    return decisions[(decisions.market_to_bet == label) & (decisions.bookmaker == book)].iloc[0]


def picked(selected):
    return sorted(zip(selected.value_market_group, selected.market_to_bet)) if len(selected) else []


class CaptureTests(OfflineQuotePolicyTestCase):
    def test_totals_capture_keeps_1_5_and_2_5_separately(self):
        payload = {'home_team': 'Home FC', 'away_team': 'Away FC', 'bookmakers': [
            {'title': 'Pinnacle', 'markets': [{'key': 'alternate_totals', 'last_update': FRESH, 'outcomes': [
                {'name': 'Over', 'point': 1.5, 'price': 1.30}, {'name': 'Under', 'point': 1.5, 'price': 3.60},
                {'name': 'Over', 'point': 2.5, 'price': 1.95}, {'name': 'Under', 'point': 2.5, 'price': 1.90},
                {'name': 'Over', 'point': 3.5, 'price': 3.40}, {'name': 'Under', 'point': 3.5, 'price': 1.32}]}]}]}
        quotes = v27.capture_quotes(payload, None, ('alternate_totals',))
        self.assertEqual(sorted((q['point'], q['prices']['over']) for q in quotes), [(1.5, 1.30), (2.5, 1.95)])
        pin = v27.pinnacle_quotes({'price_edge_quotes': json.dumps(quotes)})
        self.assertEqual(pin['ou15'][:2], (1.30, 3.60))
        self.assertEqual(pin['ou25'][:2], (1.95, 1.90))

    def test_incomplete_1_5_pair_is_not_captured(self):
        payload = {'home_team': 'Home FC', 'away_team': 'Away FC', 'bookmakers': [
            {'title': 'Pinnacle', 'markets': [{'key': 'alternate_totals', 'last_update': FRESH, 'outcomes': [
                {'name': 'Over', 'point': 1.5, 'price': 1.30}]}]}]}
        self.assertEqual(v27.capture_quotes(payload, None, ('alternate_totals',)), [])


class GroupTests(OfflineQuotePolicyTestCase):
    def test_market_groups(self):
        cases = {('Home win', -0.5): v28.GROUP_WIN, ('Asian Handicap Away -0.50', -0.5): v28.GROUP_WIN,
                 ('Double Chance X2', 0.5): v28.GROUP_DC, ('Draw No Bet Home', 0.0): v28.GROUP_AH,
                 ('Asian Handicap Home +1.50', 1.5): v28.GROUP_AH, ('Over 1.5', None): v28.GROUP_OVER_1_5}
        for (market, line), group in cases.items():
            self.assertEqual(v28.market_group({'market': market, 'handicap_line': line}), group, market)

    def test_value_rule_defaults_to_one_per_fixture_and_rejects_unknown(self):
        self.assertEqual(v28.value_rule({}), v28.VALUE_RULE_ONE)
        with self.assertRaises(ValueError):
            v28.value_rule({'value_rule': 'per-market-v9'})


class SelectionTests(OfflineQuotePolicyTestCase):
    def test_home_win_at_1_5_percent_qualifies_only_under_per_market(self):
        data = fixture(h2h_1xbet(home=price_at('home', 0.015)))
        selected, decisions, summary = run(data)
        self.assertEqual(picked(selected), [(v28.GROUP_WIN, 'Home win')])
        self.assertAlmostEqual(selected.iloc[0].min_edge, 0.01)
        self.assertEqual(summary['value_rule'], v28.VALUE_RULE_PER_MARKET)
        self.assertEqual(summary['value_market_group_counts'][v28.GROUP_WIN], 1)
        old, old_decisions, old_summary = run(data, settings=V1)
        self.assertTrue(old.empty)
        self.assertNotIn('value_rule', old_summary)
        self.assertNotIn('value_market_group', old_decisions.columns)
        home = old_decisions[(old_decisions.market_to_bet == 'Home win') & (old_decisions.bookmaker == '1xBet')].iloc[0]
        self.assertIn('edge below 2%', home.rejection_reasons)

    def test_below_1_percent_is_rejected_with_its_own_reason(self):
        _, decisions, _ = run(fixture(h2h_1xbet(home=price_at('home', 0.005))))
        home = decisions[(decisions.market_to_bet == 'Home win') & (decisions.bookmaker == '1xBet')].iloc[0]
        self.assertEqual(home.decision, 'REJECTED')
        self.assertIn('edge below 1%', home.rejection_reasons)
        self.assertNotIn('edge below 2%', home.rejection_reasons)

    def test_asian_handicap_group_qualifies_at_1_percent_against_pinnacle(self):
        target = v27.reference('home', -0.25, v27.pinnacle_quotes(fixture()), *v27.market_fit(
            v27.pinnacle_quotes(fixture()), NOW))
        label = 'Asian Handicap Home -0.25'
        for edge, expected in ((0.015, 'SHORTLISTED'), (0.005, 'REJECTED')):
            with self.subTest(edge=edge):
                data = fixture(offers=[offer('home', -0.25, round((1 + edge) / target['q'], 4))])
                _, decisions, summary = run(data)
                ah = decisions[(decisions.market_to_bet == label) & (decisions.bookmaker == '1xBet')].iloc[0]
                self.assertEqual(ah.decision, expected)
                self.assertAlmostEqual(ah.min_edge, 0.01)
                self.assertNotIn('edge below 2%', str(ah.rejection_reasons))
                self.assertEqual((summary['min_edge'], summary['min_edge_derived']), (0.01, 0.01))
                _, old, _ = run(data, settings=V1)
                self.assertIn('edge below 2%', decision_row(old, label).rejection_reasons)

    def test_derived_plus_line_qualifies_at_1_percent(self):
        probe = fixture(offers=[offer('away', 1.5, 1.20)])
        line = decision_row(run(probe)[1], 'Asian Handicap Away +1.50')
        self.assertIn(line.reference_type, ('c', 'c-cagey'))
        for edge, expected in ((0.015, 'SHORTLISTED'), (0.005, 'REJECTED')):
            with self.subTest(edge=edge):
                data = fixture(offers=[offer('away', 1.5, round(line.fair_odds * (1 + edge), 4))])
                row_ = decision_row(run(data)[1], 'Asian Handicap Away +1.50')
                self.assertEqual(row_.decision, expected)
                self.assertNotIn('edge below 3%', str(row_.rejection_reasons))
                if expected == 'REJECTED':
                    self.assertIn('edge below 1%', row_.rejection_reasons)
                # Under the old rule a 1.5% derived edge never qualified.
                self.assertIn('edge below 3%', decision_row(run(data, settings=V1)[1],
                                                           'Asian Handicap Away +1.50').rejection_reasons)

    def test_one_pick_per_group_so_a_safer_line_no_longer_hides_a_win_pick(self):
        target = v27.reference('home', -0.25, v27.pinnacle_quotes(fixture()), *v27.market_fit(
            v27.pinnacle_quotes(fixture()), NOW))
        # AH -0.5 settles exactly like Home win, so it competes in the match-winner group.
        data = fixture(h2h_1xbet(home=price_at('home', 0.03)),
                       quote('double_chance', {'home_draw': price_at('home_draw', 0.015), 'draw_away': 1.01,
                                               'home_away': 1.01}, book='1xBet'),
                       offers=[offer('home', -0.25, round(1.03 / target['q'], 4)),
                               offer('home', -0.5, price_at('home', 0.015))])
        selected, decisions, summary = run(data)
        self.assertEqual(picked(selected), [(v28.GROUP_AH, 'Asian Handicap Home -0.25'),
                                            (v28.GROUP_DC, 'Double Chance 1X'), (v28.GROUP_WIN, 'Home win')])
        # Same bet, same no-loss chance: the higher edge wins the group; the other is noted, not lost.
        other = decisions[(decisions.market_to_bet == 'Asian Handicap Home -0.50') & (decisions.bookmaker == '1xBet')].iloc[0]
        self.assertEqual(other.decision, 'NOT_SELECTED')
        self.assertIn('market group', other.rejection_reasons)
        self.assertEqual(summary['value_market_group_counts'],
                         {v28.GROUP_AH: 1, v28.GROUP_WIN: 1, v28.GROUP_DC: 1, v28.GROUP_OVER_1_5: 0})
        old, _, _ = run(data, settings=V1)
        self.assertEqual(len(old), 1)  # one per match before


class OverOnePointFiveTests(OfflineQuotePolicyTestCase):
    def test_over_1_5_priced_against_pinnacle_o_u_1_5(self):
        selected, decisions, summary = run(fixture(over_1xbet(price_at('over_1_5', 0.02))))
        self.assertEqual(picked(selected), [(v28.GROUP_OVER_1_5, 'Over 1.5')])
        pick = selected.iloc[0]
        self.assertEqual((pick.reference_type, pick.reference_market), ('a', 'Pinnacle O/U 1.5'))
        self.assertAlmostEqual(pick.fair_probability, fair('over_1_5'))
        self.assertAlmostEqual(pick.edge, pick.offered_decimal_odds * fair('over_1_5') - 1)
        self.assertTrue(pd.isna(pick.handicap_line))
        self.assertIn(v28.OVER_1_5, summary['eligible_markets'])
        # Execution v2 settlement fields (fit B) are present for staking; the price edge is still vs Pinnacle.
        self.assertEqual(pick.value_probability_basis, 'uncorrected_matrix')
        self.assertAlmostEqual(pick.uncorrected_p_win + pick.uncorrected_p_loss, 1.0)
        self.assertEqual(pick.uncorrected_p_push, 0.0)

    def test_over_1_5_needs_pinnacle_and_passes_the_guards(self):
        cases = [(fixture(over_1xbet(price_at('over_1_5', 0.02)), with_pin_15=False), v27.NO_REFERENCE),
                 (fixture(over_1xbet(price_at('over_1_5', 0.005))), 'edge below 1%'),
                 (fixture(over_1xbet(price_at('over_1_5', 0.02), stamp=(NOW - pd.Timedelta(hours=3)).isoformat())),
                  'offered and Pinnacle quotes more than 10 minutes apart'),
                 (fixture(over_1xbet(price_at('over_1_5', 0.02)), kickoff=NOW + pd.Timedelta(hours=60)),
                  'kickoff outside 20-minute to 48-hour window')]
        for data, reason in cases:
            with self.subTest(reason=reason):
                selected, decisions, _ = run(data)
                self.assertTrue(selected.empty)
                over = decisions[(decisions.market == v28.OVER_1_5) & (decisions.bookmaker == '1xBet')].iloc[0]
                self.assertEqual(over.decision, 'REJECTED')
                self.assertIn(reason, over.rejection_reasons)

    def test_no_over_1_5_candidates_under_one_per_fixture(self):
        _, decisions, _ = run(fixture(over_1xbet(price_at('over_1_5', 0.05))), settings=V1)
        self.assertFalse((decisions.market == v28.OVER_1_5).any())

    def test_disallowed_bookmaker_is_ignored(self):
        data = fixture(quote('totals', {'over': price_at('over_1_5', 0.05), 'under': 3.0}, book='Bet365',
                             key='alternate_totals', point=1.5))
        _, decisions, _ = run(data)
        over = decisions[decisions.market == v28.OVER_1_5]
        self.assertNotIn('Bet365', set(over.bookmaker))
        # Pinnacle's own quote is a candidate too, as for AH lines, but never beats its own fair price.
        self.assertEqual(set(over.bookmaker), {'Pinnacle'})
        self.assertIn('edge below 1%', over.iloc[0].rejection_reasons)


class ReplayTests(OfflineQuotePolicyTestCase):
    def test_raw_check_replays_a_per_market_run_and_rejects_it_as_one_per_fixture(self):
        from unittest.mock import patch
        from workflow_checks import raw_check
        predictions = pd.DataFrame([fixture(h2h_1xbet(home=price_at('home', 0.015)),
                                            over_1xbet(price_at('over_1_5', 0.02)))])
        predictions['p_home'], predictions['p_draw'], predictions['p_away'] = 0.45, 0.27, 0.28
        monitoring = []
        settings = {'cagey_correction_enabled': True, 'cagey_tier_enabled': True,
                    'cagey_tier_rule': v28.TIER_RULE_NARROW, 'value_rule': v28.VALUE_RULE_PER_MARKET}
        selected, decisions, summary = run(*predictions.to_dict('records'), settings=settings, monitor=monitoring)
        self.assertEqual(picked(selected), [(v28.GROUP_WIN, 'Home win'), (v28.GROUP_OVER_1_5, 'Over 1.5')])
        with tempfile.TemporaryDirectory() as tmp:
            raw = Path(tmp) / 'raw'
            raw.mkdir()
            predictions.to_csv(raw / 'all_leagues_predictions.csv', index=False)
            selected.to_csv(raw / 'conservative_bet_shortlist.csv', index=False)
            v28.cagey_tier_list(decisions).to_csv(raw / v28.TIER_FILE, index=False)
            v28.record_monitoring(summary, monitoring, raw)
            path = raw / 'conservative_bet_summary.json'
            path.write_text(json.dumps(summary, default=str), encoding='utf-8')
            # Today's config is irrelevant: the run's recorded rules are replayed.
            with patch.object(v28, 'load_settings', return_value={**V1, 'model_version': None}):
                raw_check(Path(tmp), raw_dir=raw)
            selected.assign(offered_decimal_odds=9.9).to_csv(raw / 'conservative_bet_shortlist.csv', index=False)
            with self.assertRaisesRegex(Exception, 'differs from deterministic ranking replay'):
                raw_check(Path(tmp), raw_dir=raw)
            selected.to_csv(raw / 'conservative_bet_shortlist.csv', index=False)
            path.write_text(json.dumps({k: v for k, v in summary.items() if k != 'value_rule'}, default=str),
                            encoding='utf-8')
            with self.assertRaises(Exception):
                raw_check(Path(tmp), raw_dir=raw)


class TrackingTests(OfflineQuotePolicyTestCase):
    def test_pick_key_separates_market_groups_and_leaves_old_picks_unchanged(self):
        from performance_tracking import pick_key, tracking_key
        old = {'fixture_key': 'EPL|a|b|2026-11-08', 'snapshot_generated_utc': '2026-11-07T12:00:00+00:00'}
        self.assertEqual(pick_key(old), 'EPL|a|b|2026-11-08')
        self.assertEqual(pick_key({**old, 'value_market_group': ''}), 'EPL|a|b|2026-11-08')
        self.assertEqual(pick_key({**old, 'value_market_group': float('nan')}), 'EPL|a|b|2026-11-08')
        win, over = {**old, 'value_market_group': 'match_winner'}, {**old, 'value_market_group': 'over_1_5'}
        self.assertNotEqual(tracking_key(win), tracking_key(over))
        self.assertEqual(tracking_key(win)[1], 'EPL|a|b|2026-11-08#match_winner')

    def test_frozen_rows_keep_one_pick_per_group_of_the_same_fixture(self):
        from performance_tracking import frozen_rows
        base = {'league': 'Premier League', 'home_team': 'Home FC', 'away_team': 'Away FC',
                'kickoff_utc': (NOW + pd.Timedelta(hours=24)).isoformat(), 'decision': 'SHORTLISTED'}
        meta = {'captured_at_utc': NOW.isoformat(), 'generated_at_utc': NOW.isoformat(), 'git_commit_sha': 'a' * 40,
                'selection_policy_version': v28.POLICY}
        picks = [{**base, 'market': 'Home win', 'value_market_group': 'match_winner'},
                 {**base, 'market': 'Over 1.5', 'value_market_group': 'over_1_5'}]
        rows = frozen_rows([(meta, [], picks)], 'shortlist', latest=True)
        self.assertEqual(sorted(r['market'] for r in rows), ['Home win', 'Over 1.5'])
        legacy = [{k: v for k, v in p.items() if k != 'value_market_group'} for p in picks]
        self.assertEqual(len(frozen_rows([(meta, [], legacy)], 'shortlist', latest=True)), 1)

    def test_score_shortlist_settles_over_1_5_and_keeps_the_group(self):
        from performance_tracking import score_shortlist
        pick = {'fixture_key': 'k', 'league': 'Premier League', 'home_team': 'h', 'away_team': 'a',
                'kickoff_utc': '2026-11-08T12:00:00+00:00', 'snapshot_commit': 'c', 'snapshot_captured_utc': 'x',
                'market': 'Over 1.5', 'decision': 'SHORTLISTED', 'rank_probability': 0.75,
                'offered_decimal_odds': 1.36, 'bookmaker': '1xBet', 'value_market_group': 'over_1_5'}
        for goals, status, profit in (((1, 1), 'WON', 0.36), ((1, 0), 'LOST', -1.0)):
            final = {'home_goals': goals[0], 'away_goals': goals[1], 'match_id': 1, 'source': 's'}
            out = score_shortlist(pick, final, 'VERIFIED_FINISHED')
            self.assertEqual(out['status'], status)
            self.assertAlmostEqual(float(out['unit_profit']), profit)
            self.assertEqual(out['value_market_group'], 'over_1_5')

    def test_price_edge_tracker_grades_over_1_5_with_clv(self):
        import price_edge_tracking as tracking
        from unittest.mock import patch
        kick = NOW + pd.Timedelta(hours=24)
        pick = {'league': 'Premier League', 'home_team': 'Home FC', 'away_team': 'Away FC',
                'kickoff_utc': kick.isoformat(), 'market': 'Over 1.5', 'offered_decimal_odds': 1.40,
                'fair_odds': 1.35, 'snapshot_captured_utc': NOW.isoformat(), 'value_market_group': 'over_1_5'}
        close = {'fixture': {**pick}, 'observed_at_utc': (kick - pd.Timedelta(minutes=5)).isoformat(),
                 'quotes': [{'bookmaker': 'pinnacle', 'selection': 'over_1_5', 'decimal_odds': 1.30},
                            {'bookmaker': 'pinnacle', 'selection': 'under_1_5', 'decimal_odds': 3.80}]}
        final = {'home_goals': 2, 'away_goals': 0}
        with patch('performance_tracking.fixture_match', return_value=(final, 'VERIFIED_FINISHED')):
            graded = tracking.grade([pick], [close], [], kick + pd.Timedelta(hours=5))
        row = graded.iloc[0]
        q = (1 / 1.30) / (1 / 1.30 + 1 / 3.80)
        self.assertAlmostEqual(row.clv, 1.40 * q - 1)
        self.assertEqual(row.result_status, 'WON')
        self.assertAlmostEqual(row.unit_profit, 0.40)
        self.assertAlmostEqual(row.return_at_capture_fair, 0.35)


class ReadableTests(OfflineQuotePolicyTestCase):
    def test_readable_shortlist_shows_market_groups_and_blank_ah_line_for_over_1_5(self):
        from format_football_output import process_conservative_shortlist
        data = fixture(h2h_1xbet(home=price_at('home', 0.015)), over_1xbet(price_at('over_1_5', 0.02)))
        selected, decisions, summary = run(data)
        with tempfile.TemporaryDirectory() as tmp:
            raw, out = Path(tmp) / 'raw', Path(tmp) / 'readable'
            raw.mkdir()
            out.mkdir()
            selected.to_csv(raw / 'conservative_bet_shortlist.csv', index=False)
            (raw / 'conservative_bet_summary.json').write_text(json.dumps(summary, default=str), encoding='utf-8')
            process_conservative_shortlist(raw, out)
            readable = pd.read_csv(out / 'conservative_bet_shortlist_readable.csv', keep_default_na=False)
            report = (out / 'conservative_bet_shortlist_report.md').read_text(encoding='utf-8')
        self.assertEqual(sorted(readable['Market group']), ['Match winner', 'Over 1.5'])
        over = readable[readable['Market to bet'] == 'Over 1.5'].iloc[0]
        self.assertEqual(over['AH line'], '')
        self.assertIn('per market group', report)
        self.assertIn('match winner 1', report.lower())


if __name__ == '__main__':
    unittest.main()
