"""Shortlist v25: Corners and Cards groups, per-market approval for every league, unproven-edge flags."""
import json
from pathlib import Path

import pandas as pd

import count_markets as cm
import corners_cards_shortlist as v25
import per_market_shortlist as v24
from conservative_bet_filter import build_conservative_shortlist
from offline_test_case import OfflineQuotePolicyTestCase
from test_asian_handicap import NOW, POLICY as QUOTES, row
from test_win_first_shortlist import reports


def offer(kind='corners', side='Over', line=9.5, price=1.9, opposite=1.95, book='Pinnacle'):
    return {'kind': kind, 'side': side, 'line': line, 'price': price, 'opposite_price': opposite,
            'bookmaker': book, 'last_update_utc': NOW.isoformat(), 'market_key': cm.ODDS_MARKETS[kind]}


def count_row(i, offers, mu=10.0, alpha=.02, kinds=('corners',)):
    value = row(i, offers=[])
    value['count_model'] = json.dumps({k: {'mu': mu if k == 'corners' else 4.0, 'alpha': alpha,
                                           'version': cm.VERSION} for k in kinds})
    value['count_market_offers'] = json.dumps(offers)
    return value


def count_report(kind, failed=(), penalty=0.):
    markets = {}
    for line in cm.LINES[kind]:
        for side in ('Over', 'Under'):
            label = cm.market_label(kind, side, line)
            markets[label] = {'status': 'UNRELIABLE_AUDIT' if label in failed else 'RELIABLE_FOR_RANKING',
                              'confidence_penalty': penalty, 'development': {'n': 900}, 'audit': {'n': 300, 'brier': .2},
                              'high_confidence': {t: {'status': 'PASSED', 'development_only_penalty': 0.}
                                                  for t in ('75plus', '85plus')}}
    return {'version': cm.VERSION, 'kind': kind, 'markets': markets}


def evidence(failed=(), league='Premier League', kinds=('corners',)):
    result = reports()
    result[league] = result.pop('Premier League') if league != 'Premier League' else result[league]
    result[league]['count_markets'] = {k: count_report(k, failed) for k in kinds}
    return result


def select(values, evidence_map, policy=v25.POLICY):
    return build_conservative_shortlist(pd.DataFrame(values), as_of=NOW, market_reliability=evidence_map,
                                        execution_policy=QUOTES, selection_policy_version=policy)


class CornersCardsShortlistTests(OfflineQuotePolicyTestCase):
    def test_groups_cap_and_maximum(self):
        self.assertEqual(v25.MARKET_GROUPS, (*v24.MARKET_GROUPS, 'Corners', 'Cards'))
        self.assertEqual((v25.PER_GROUP_CAP, v25.MAX_SELECTIONS), (2, 18))
        self.assertEqual(v25.market_group('Corners Over 9.5'), 'Corners')
        self.assertEqual(v25.market_group('Cards Under 3.5'), 'Cards')
        self.assertEqual(v25.market_group('Home win'), 'Home win')
        self.assertIsNone(v25.market_group('Draw'))
        import asian_handicap
        self.assertEqual(asian_handicap.CORNERS_CARDS_POLICY, v25.POLICY)
        self.assertIn(v24.POLICY, asian_handicap.WIN_FIRST_POLICIES)

    def test_corner_picks_capped_at_two_flagged_unproven_and_ranked_by_probability(self):
        values = [count_row(i, [offer(line=8.5, price=1.5, opposite=2.6)], mu=8 + i) for i in range(5)]
        picks, decisions, summary = select(values, evidence())
        self.assertEqual(list(picks.market_group), ['Corners', 'Corners'])
        # Highest model means give the highest Over 8.5 probabilities.
        self.assertEqual(sorted(picks.home_team), sorted(pd.DataFrame(values).home_team.iloc[[3, 4]]))
        self.assertTrue(picks.selection_warnings.str.contains('UNPROVEN EDGE').all())
        self.assertTrue(picks.unproven_edge.all())
        self.assertEqual((decisions.decision == 'NOT_SELECTED').sum(), 3)
        self.assertEqual(summary['unproven_edge_selections'], 2)
        self.assertEqual(summary['unproven_edge_market_groups'], ['Corners', 'Cards'])
        self.assertEqual(summary['target_distinct_matches'], 18)
        self.assertIn('Corners Over 8.5', summary['eligible_markets'])
        self.assertEqual(summary['group_shortfall']['Corners'], {'eligible_fixtures': 5, 'selected': 2, 'shortfall': 0})
        p = cm.probabilities(12., .02, 'corners')['Corners Over 8.5']
        best = picks.loc[picks.home_team == values[4]['home_team']].iloc[0]
        self.assertAlmostEqual(best.predicted_probability, p)
        self.assertAlmostEqual(best.conservative_estimated_ev, p*1.5-1)

    def test_failed_line_blocks_only_that_line(self):
        values = [count_row(0, [offer(line=8.5), offer(side='Under', line=8.5, price=1.95, opposite=1.9),
                                offer(line=9.5, price=2.0, opposite=1.85)])]
        _, decisions, _ = select(values, evidence(failed=('Corners Over 8.5',)))
        blocked = decisions.loc[decisions.market == 'Corners Over 8.5'].iloc[0]
        self.assertEqual(blocked.decision, 'REJECTED')
        self.assertIn('per-market approval: market audit UNRELIABLE_AUDIT', blocked.rejection_reasons)
        others = decisions.loc[decisions.market.isin(['Corners Under 8.5', 'Corners Over 9.5'])]
        self.assertTrue(others.decision.isin(['SHORTLISTED', 'NOT_SELECTED']).all())

    def test_missing_evidence_unquoted_league_and_bookmaker_are_rejected(self):
        values = [count_row(0, [offer()])]
        _, decisions, _ = select(values, reports())
        self.assertIn('per-market approval: market audit NOT_ASSESSED',
                      decisions.loc[decisions.market == 'Corners Over 9.5'].iloc[0].rejection_reasons)
        # EPL has no validated card market, even with a passing card report and model.
        values = [count_row(0, [offer('cards', line=4.5)], kinds=('corners', 'cards'))]
        _, decisions, _ = select(values, evidence(kinds=('corners', 'cards')))
        self.assertIn('competition has no validated count market',
                      decisions.loc[decisions.market == 'Cards Over 4.5'].iloc[0].rejection_reasons)
        # The parser keeps only supported books; an unsupported one never reaches selection.
        values = [count_row(0, [{**offer(), 'bookmaker': 'LeoVegas'}])]
        _, decisions, _ = select(values, evidence())
        self.assertIn('bookmaker excluded by execution policy',
                      decisions.loc[decisions.market == 'Corners Over 9.5'].iloc[0].rejection_reasons)
        _, decisions, _ = select([count_row(0, [offer()])], evidence())
        self.assertEqual(decisions.loc[decisions.market == 'Corners Over 9.5'].iloc[0].decision, 'SHORTLISTED')

    def test_card_totals_are_rejected_in_every_league_with_the_settlement_reason(self):
        # Even with a passing card report and model, the settlement total cannot be reproduced.
        for league in ('Premier League', 'Bundesliga', 'Serie A', 'Ligue 1'):
            with self.subTest(league=league):
                value = count_row(0, [offer('cards', line=4.5)], kinds=('corners', 'cards'))
                value['league'] = league
                _, decisions, _ = select([value], evidence(league=league, kinds=('corners', 'cards')))
                card = decisions.loc[decisions.market == 'Cards Over 4.5'].iloc[0]
                self.assertEqual(card.decision, 'REJECTED')
                self.assertIn('card totals out of production: Pinnacle settles card totals as bookings',
                              card.rejection_reasons)

    def test_high_probability_needs_its_tier_and_stale_quotes_fail(self):
        failing = evidence()
        for market in failing['Premier League']['count_markets']['corners']['markets'].values():
            market['high_confidence']['85plus']['status'] = 'INSUFFICIENT_HIGH_CONFIDENCE_HISTORY'
        values = [count_row(0, [offer(line=7.5, price=1.1, opposite=6.0)], mu=13)]
        _, decisions, _ = select(values, failing)
        self.assertIn('per-market approval: 85plus audit INSUFFICIENT_HIGH_CONFIDENCE_HISTORY',
                      decisions.loc[decisions.market == 'Corners Over 7.5'].iloc[0].rejection_reasons)
        stale = {**offer(), 'last_update_utc': (NOW-pd.Timedelta(hours=25)).isoformat()}
        _, decisions, _ = select([count_row(0, [stale])], evidence())
        self.assertIn('stale', decisions.loc[decisions.market == 'Corners Over 9.5'].iloc[0].rejection_reasons)

    def test_one_market_per_fixture_and_v24_unchanged_without_count_quotes(self):
        values = [count_row(i, [offer(line=8.5, price=1.5, opposite=2.6)], mu=12) for i in range(2)]
        for value in values:
            value['asian_handicap_offers'] = json.dumps([])
        picks, _, _ = select(values, evidence())
        from performance_tracking import fixture_key
        self.assertEqual(len({fixture_key(r) for r in picks.to_dict('records')}), len(picks))
        plain = [row(i) for i in range(3)]
        a, _, sa = select(plain, reports(), v24.POLICY)
        b, _, sb = select(plain, reports())
        self.assertEqual(list(a.market), list(b.market))
        self.assertEqual(sb['unproven_edge_selections'], 0)

    def test_failed_ordinary_market_is_labelled_per_market(self):
        evidence_map = reports()
        evidence_map['Premier League']['asian_handicap_win']['markets'][list(
            evidence_map['Premier League']['asian_handicap_win']['markets'])[0]]['status'] = 'UNRELIABLE_AUDIT'
        _, decisions, _ = select([row(0)], evidence_map)
        rejected = decisions.loc[decisions.validation_status.ne('RELIABLE_FOR_RANKING')]
        self.assertTrue(len(rejected) and rejected.decision.eq('REJECTED').all())
        self.assertTrue(rejected.rejection_reasons.str.contains('per-market approval: market audit').all())

    def test_readable_report_flags_unproven_edge(self):
        import tempfile
        from format_football_output import process_conservative_shortlist
        values = [count_row(i, [offer(line=8.5, price=1.5, opposite=2.6)], mu=12) for i in range(2)]
        picks, _, summary = select(values, evidence())
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory); raw = root/'raw'; out = root/'readable'; raw.mkdir(); out.mkdir()
            picks.to_csv(raw/'conservative_bet_shortlist.csv', index=False)
            (raw/'conservative_bet_summary.json').write_text(json.dumps(summary, default=str))
            process_conservative_shortlist(raw, out)
            text = (out/'conservative_bet_shortlist_report.md').read_text()
        self.assertIn('**UNPROVEN EDGE (Corners, Cards):** validated on probability accuracy only', text)
        self.assertIn('2 of 2 selections', text)
        self.assertIn('Up to 2 matches per market group (maximum 18)', text)
        self.assertIn('| Corners | 2 | 2 | 0 |', text)
        self.assertIn('| Cards | 0 | 0 | 2 |', text)


class CountGradingTests(OfflineQuotePolicyTestCase):
    """Corner picks settle from committed match statistics consistent with the verified score."""

    def committed(self):
        frame = cm.load_history(Path(__file__).resolve().parents[1]/'.football_cache', 'I1')
        match = frame.dropna(subset=['HC', 'AC']).iloc[-1]
        kickoff = pd.to_datetime(match.Date, dayfirst=True).tz_localize('UTC') + pd.Timedelta(hours=18)
        return match, kickoff

    def selection(self, match, kickoff, market, **extra):
        return {'fixture_key': 'k', 'league': 'Serie A', 'home_team': match.HomeTeam, 'away_team': match.AwayTeam,
                'model_home_team': match.HomeTeam, 'model_away_team': match.AwayTeam,
                'kickoff_utc': kickoff.isoformat(), 'snapshot_commit': 'abc', 'snapshot_captured_utc': 'x',
                'market': market, 'decision': 'SHORTLISTED', 'selection_tier': 'STRICT', 'rank_probability': .6,
                'predicted_probability': .62, 'probability_basis': 'net_profit', 'offered_decimal_odds': 1.9,
                'per_stake_cost': 0, 'bookmaker': 'Pinnacle', **extra}

    def test_settles_from_committed_statistics_with_profit_and_brier(self):
        from performance_tracking import score_shortlist, SUPPORTED_MARKETS
        match, kickoff = self.committed()
        total = int(match.HC + match.AC)
        final = {'home_goals': int(match.FTHG), 'away_goals': int(match.FTAG), 'match_id': 1}
        for side, line in (('Over', 9.5), ('Under', 9.5), ('Over', 7.5)):
            market = cm.market_label('corners', side, line)
            self.assertIn(market, SUPPORTED_MARKETS)
            graded = score_shortlist(self.selection(match, kickoff, market), final, 'VERIFIED_FINISHED')
            won = cm.outcome('corners', side, line, total)
            self.assertEqual(graded['status'], 'WON' if won else 'LOST')
            self.assertAlmostEqual(graded['unit_profit'], .9 if won else -1.)
            self.assertAlmostEqual(graded['brier'], (.6-int(won))**2)

    def test_stays_pending_until_statistics_agree_with_the_verified_score(self):
        from performance_tracking import score_shortlist
        from asian_handicap import SETTLED
        match, kickoff = self.committed()
        market = 'Corners Over 9.5'
        wrong = {'home_goals': int(match.FTHG)+1, 'away_goals': int(match.FTAG), 'match_id': 1}
        right = {'home_goals': int(match.FTHG), 'away_goals': int(match.FTAG), 'match_id': 1}
        cases = [(self.selection(match, kickoff, market), wrong),
                 (self.selection(match, kickoff + pd.Timedelta(days=5), market), right),
                 (self.selection(match, kickoff, market, model_home_team='Unknown FC'), right)]
        for selection, final in cases:
            graded = score_shortlist(selection, final, 'VERIFIED_FINISHED')
            self.assertEqual(graded['status'], 'AWAITING_COUNT_RESULT')
            self.assertNotIn(graded['status'], SETTLED)
            self.assertEqual((graded['unit_profit'], graded['brier']), ('', ''))
        # Card totals have no production settlement source.
        self.assertIsNone(cm.verified_total(self.selection(match, kickoff, 'Cards Over 4.5'), right))
