"""Per-market v24 caps, fixture uniqueness, negative-EV flags and short groups."""
import json
from pathlib import Path
import tempfile

import pandas as pd

import asian_handicap as ah
from conservative_bet_filter import build_conservative_shortlist
from format_football_output import process_conservative_shortlist
from offline_test_case import OfflineQuotePolicyTestCase
from per_market_shortlist import (POLICY, MARKET_GROUPS, MAX_SELECTIONS, PER_GROUP_CAP, PROBABILITY_WEIGHT,
                                  market_group, rank_candidates, select_candidates)
from test_asian_handicap import NOW, POLICY as QUOTES, quote, row
from test_shortlist_market_alternatives import dc_fixture
from test_win_first_shortlist import reports
from win_first_shortlist import POLICY as WIN_POLICY

GROUP_MARKETS = {'Asian handicap': ah.label('home', 0), **{g: g for g in MARKET_GROUPS[1:]}}
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def select(values, evidence=None, policy_version=POLICY):
    return build_conservative_shortlist(pd.DataFrame(values), as_of=NOW,
        market_reliability=reports() if evidence is None else evidence,
        execution_policy=QUOTES, selection_policy_version=policy_version)


def candidate(fixture, market, probability=.6, ev=.02):
    """Synthetic eligible decision row; only ranking fields matter here."""
    return {'league': 'Premier League', 'home_team': f'Home {LETTERS[fixture//26]}{LETTERS[fixture%26]}',
            'away_team': 'Visitors', 'kickoff_utc': (NOW+pd.Timedelta(days=1)).isoformat(),
            'market': market, 'bookmaker': 'Pinnacle', 'rank_probability': probability,
            'conservative_estimated_ev': ev, 'raw_dc_ev': ev, 'offered_decimal_odds': 1.8}


def chosen(pool):
    ranked = rank_candidates(pd.DataFrame(pool))
    return ranked.loc[select_candidates(ranked)]


class PerMarketShortlistTests(OfflineQuotePolicyTestCase):
    def test_groups_merge_asian_lines_and_exclude_draw(self):
        for side in ('home', 'away'):
            for point in (-1.5, 0, .25):
                self.assertEqual(market_group(ah.label(side, point)), 'Asian handicap')
        for market in MARKET_GROUPS[1:]:
            self.assertEqual(market_group(market), market)
        self.assertIsNone(market_group('Draw'))
        self.assertNotIn('Draw', ah.ordinary_markets(POLICY))
        picks = chosen([candidate(0, 'Draw', .99, .5)])
        self.assertTrue(picks.empty)

    def test_cap_of_two_per_group(self):
        pool = [candidate(i, GROUP_MARKETS['Asian handicap'], .5+i/100) for i in range(6)]
        # Different Asian lines on the same fixtures still share one group cap.
        pool += [candidate(i, ah.label('away', .5), .9) for i in range(6, 9)]
        picks = chosen(pool)
        self.assertEqual(len(picks), PER_GROUP_CAP)
        self.assertEqual(set(picks.market_group), {'Asian handicap'})
        # Integrated: five qualifying handicap fixtures still yield only two picks.
        values = [row(i, offers=[{**quote(price=2.2), 'opposite_price': 1.7}]) for i in range(5)]
        picks, decisions, summary = select(values)
        self.assertEqual(len(picks), 2)
        self.assertEqual((decisions.decision == 'NOT_SELECTED').sum(), 3)
        self.assertEqual(summary['group_shortfall']['Asian handicap'],
                         {'eligible_fixtures': 5, 'selected': 2, 'shortfall': 0})

    def test_probability_weighted_eighty_twenty(self):
        self.assertEqual(PROBABILITY_WEIGHT, .8)
        # At 50/50, B and C tied and the most likely winner A was dropped.
        # At 80/20, A (70%, negative EV) and B (60%) are chosen over C (50%, best EV).
        pool = [candidate(0, 'Home win', .7, -.05), candidate(1, 'Home win', .6, .02),
                candidate(2, 'Home win', .5, .08), candidate(3, 'Home win', .4, .01)]
        ranked = rank_candidates(pd.DataFrame(pool))
        self.assertEqual(list(ranked.selection_score), [.85, .75, .6, .3])
        self.assertEqual(list(chosen(pool).home_team), ['Home AA', 'Home AB'])
        # EV overtakes when its rank gain exceeds four times the probability
        # rank loss: one probability place lower but five EV places higher.
        ranked = rank_candidates(pd.DataFrame([candidate(i, 'Away win', p, ev) for i, (p, ev) in enumerate(
            [(.61, -.2), (.60, .1), (.5, 0), (.45, .01), (.4, .02), (.3, .03)])]))
        self.assertEqual(list(ranked.home_team[:2]), ['Home AB', 'Home AA'])

    def test_equal_scores_are_broken_by_probability(self):
        # Five candidates: X (probability rank .6, EV rank .2) and Y (.4, 1.0)
        # both score exactly .52; X has the higher probability and ranks first.
        pool = [candidate(0, 'Over 1.5', .9, .03), candidate(1, 'Over 1.5', .8, .02),
                candidate(2, 'Over 1.5', .7, -.1), candidate(3, 'Over 1.5', .6, .2),
                candidate(4, 'Over 1.5', .5, .01)]
        ranked = rank_candidates(pd.DataFrame(pool)).set_index('home_team')
        self.assertEqual(ranked.selection_score['Home AC'], ranked.selection_score['Home AD'])
        self.assertLess(list(ranked.index).index('Home AC'), list(ranked.index).index('Home AD'))

    def test_maximum_fourteen_two_from_every_group(self):
        pool = [candidate(4*g+i, GROUP_MARKETS[group], .5+i/10, .01*i)
                for g, group in enumerate(MARKET_GROUPS) for i in range(4)]
        picks = chosen(pool)
        self.assertEqual(MAX_SELECTIONS, 14)
        self.assertEqual(len(picks), MAX_SELECTIONS)
        self.assertEqual(picks.market_group.value_counts().to_dict(), dict.fromkeys(MARKET_GROUPS, 2))
        # The two best by combined within-group score win each group.
        self.assertEqual(sorted(picks.selection_score), [.75]*7 + [1.]*7)

    def test_one_pick_per_fixture_higher_score_claims_it(self):
        # Fixture 0 tops both Home win and Double Chance 1X. Home win scores
        # higher (EV percentile), so 1X falls through to its next fixture.
        pool = [candidate(0, 'Home win', .6, .10), candidate(1, 'Home win', .5, .01),
                candidate(0, 'Double Chance 1X', .8, .01), candidate(2, 'Double Chance 1X', .7, .05),
                candidate(3, 'Double Chance 1X', .6, .00)]
        picks = chosen(pool)
        self.assertEqual(picks._fixture.nunique(), len(picks))
        self.assertEqual([(r.market, r.home_team) for r in picks.itertuples()],
                         [('Home win', 'Home AA'), ('Double Chance 1X', 'Home AC'),
                          ('Home win', 'Home AB'), ('Double Chance 1X', 'Home AD')])
        # Integrated: a fixture with both Double Chance and handicap quotes
        # contributes exactly one market.
        value, evidence = dc_fixture(offers=[quote()])
        evidence['Premier League']['asian_handicap_win'] = reports()['Premier League']['asian_handicap_win']
        picks, decisions, _ = select([value], evidence)
        self.assertEqual(len(picks), 1)
        self.assertGreater((decisions.decision == 'NOT_SELECTED').sum(), 0)

    def test_shared_fixtures_never_leave_a_fillable_slot_empty(self):
        # Greedy by score took A and B for Home win and left 1X empty (two
        # picks). Rearranging fills three: Home win A and C, 1X B.
        pool = [candidate(0, 'Home win', .9, .1), candidate(1, 'Home win', .8, .09),
                candidate(2, 'Home win', .5, .0), candidate(0, 'Double Chance 1X', .7, .05),
                candidate(1, 'Double Chance 1X', .6, .04)]
        picks = chosen(pool)
        self.assertEqual([(r.market, r.home_team) for r in picks.itertuples()],
                         [('Home win', 'Home AA'), ('Double Chance 1X', 'Home AB'), ('Home win', 'Home AC')])
        # Randomized pools: the selection always fills as many slots as an
        # exhaustive search over valid allocations.
        import itertools, random
        rng = random.Random(24)
        for _ in range(40):
            pool = [candidate(f, GROUP_MARKETS[g], rng.random(), rng.uniform(-.1, .1))
                    for f in range(6) for g in rng.sample(MARKET_GROUPS[:3], rng.randint(0, 3))]
            ranked = rank_candidates(pd.DataFrame(pool))
            rows = list(zip(ranked._fixture, ranked.market_group))
            best = max((n for n in range(len(rows), 0, -1) for combo in itertools.combinations(rows, n)
                        if len({f for f, _ in combo}) == n and
                        max(pd.Series([g for _, g in combo]).value_counts()) <= PER_GROUP_CAP), default=0)
            picks = ranked.loc[select_candidates(ranked)]
            self.assertEqual(len(picks), best)
            self.assertEqual(picks._fixture.nunique(), len(picks))
            self.assertLessEqual(picks.market_group.value_counts().max() if len(picks) else 0, PER_GROUP_CAP)

    def test_short_group_is_not_filled_from_another_group(self):
        value, evidence = dc_fixture(offers=[])
        evidence['Premier League']['asian_handicap_win'] = reports()['Premier League']['asian_handicap_win']
        handicaps = [row(i, offers=[{**quote(price=2.2), 'opposite_price': 1.7}]) for i in range(1, 6)]
        picks, _, summary = select([value, *handicaps], evidence)
        self.assertEqual(picks.market_group.value_counts().to_dict(), {'Asian handicap': 2, 'Double Chance 1X': 1})
        self.assertEqual(summary['group_shortfall']['Double Chance 1X'],
                         {'eligible_fixtures': 1, 'selected': 1, 'shortfall': 1})
        self.assertEqual(summary['group_shortfall']['Home win']['shortfall'], 2)
        self.assertEqual(summary['shortfall'], MAX_SELECTIONS-3)
        self.assertEqual(summary['status'], 'BELOW_TARGET')
        self.assertIn('Double Chance 1X 1/2', summary['shortfall_reason'])
        self.assertIn('not filled from other groups', summary['shortfall_reason'])
        # Picks are presented grouped in policy order.
        self.assertEqual(list(picks.market_group), ['Asian handicap', 'Asian handicap', 'Double Chance 1X'])

    def test_negative_adjusted_ev_is_flagged_not_filtered(self):
        cheap = row(0, offers=[{**quote(price=1.2), 'opposite_price': 5.0}])
        fair = row(1, offers=[{**quote(price=2.2), 'opposite_price': 1.7}])
        picks, _, summary = select([cheap, fair])
        self.assertEqual(len(picks), 2)
        flagged = picks.set_index('home_team').selection_warnings.str.contains('NEGATIVE ADJUSTED EV')
        self.assertTrue(flagged['Home_0'])
        self.assertFalse(flagged['Home_1'])
        self.assertLess(picks.set_index('home_team').conservative_estimated_ev['Home_0'], 0)
        self.assertEqual(summary['negative_adjusted_ev_selections'], 1)
        self.assertEqual(summary['negative_adjusted_ev_markets'], [f"Home_0 vs Away_0: {ah.label('home', 0)}"])
        self.assertFalse(summary['ev_required_for_selection'])
        self.assertEqual(summary['ranking_weights'], {'adjusted_probability_percentile': .8, 'adjusted_ev_percentile': .2})
        self.assertIn('0.8 * probability_percentile + 0.2 * ev_percentile', summary['score_formula'])
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory); raw = root/'raw'; out = root/'readable'; raw.mkdir(); out.mkdir()
            picks.to_csv(raw/'conservative_bet_shortlist.csv', index=False)
            (raw/'conservative_bet_summary.json').write_text(json.dumps(summary))
            process_conservative_shortlist(raw, out)
            text = (out/'conservative_bet_shortlist_report.md').read_text()
            self.assertIn('**Negative adjusted EV:** 1 of 2 selections: Home_0 vs Away_0', text)
            self.assertIn('## Shortfall by market group', text)
            self.assertIn('| Double Chance 12 | 0 | 0 | 2 |', text)
            self.assertIn('Up to 2 matches per market group (maximum 14)', text)
            self.assertIn('80.0% adjusted-probability percentile + 20.0% adjusted-EV percentile; higher probability breaks ties', text)
            readable = pd.read_csv(out/'conservative_bet_shortlist_readable.csv')
            self.assertEqual(set(readable['Market group']), {'Asian handicap'})

    def test_current_dispatch_and_v23_replays_unchanged(self):
        # v24 is archived behind v25 and still dispatches to its own builder.
        self.assertEqual(ah.PER_MARKET_POLICY, POLICY)
        self.assertIn(POLICY, ah.POLICIES)
        self.assertIn(WIN_POLICY, ah.POLICIES)
        self.assertEqual(select([row(0)], policy_version=POLICY)[2]['selection_policy_version'], POLICY)
        values = [row(i) for i in range(13)]
        old, _, summary = select(values, policy_version=WIN_POLICY)
        self.assertEqual(len(old), 12)
        self.assertEqual(summary['selection_policy_version'], WIN_POLICY)
        self.assertNotIn('market_group', old.columns)
        picks, _, summary = select([])
        self.assertTrue(picks.empty)
        self.assertEqual(summary['status'], 'NO BET')
        self.assertEqual(summary['group_shortfall']['Asian handicap']['shortfall'], 2)
        with self.assertRaises(ValueError):
            ah.build_shortlist(pd.DataFrame([row()]), NOW, reports(), adjusted_ev_floor=.01, policy_version=POLICY)

    def test_frozen_replay_checks_group_cap_and_ranking(self):
        from workflow_checks import raw_check
        values = [row(i) for i in range(4)]
        picks, _, summary = select(values)
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory); raw = root/'raw'; raw.mkdir()
            pd.DataFrame(values).to_csv(raw/'all_leagues_predictions.csv', index=False)
            (raw/'conservative_bet_summary.json').write_text(json.dumps(summary))
            evidence = reports()['Premier League']; evidence['league'] = 'Premier League'
            (raw/'EPL_goal_market_validation.json').write_text(json.dumps(evidence))
            picks.to_csv(raw/'conservative_bet_shortlist.csv', index=False)
            self.assertEqual(raw_check(root)['selections'], 2)
            tampered = picks.copy(); tampered.loc[0, 'selection_score'] = .01
            tampered.to_csv(raw/'conservative_bet_shortlist.csv', index=False)
            with self.assertRaisesRegex(ValueError, 'deterministic ranking replay'):
                raw_check(root)
            extra = pd.concat([picks, picks.iloc[[0]].assign(home_team='Home_3', away_team='Away_3')])
            extra.to_csv(raw/'conservative_bet_shortlist.csv', index=False)
            with self.assertRaisesRegex(ValueError, 'group cap'):
                raw_check(root)
