"""The cagey tier is a pure market view (docs/plan.md, Phase 3): research-perturbation test.

The mirror of the odds-perturbation test (tests/test_value_model_independence.py). Every research, form,
news and xG input, and every other field that is not a bookmaker price or fixture identity, is changed;
the cagey tier's probabilities (the corrected Pinnacle grid D, and the settlement probabilities of every
cagey candidate) and the cagey shortlist's decisions and ranking must stay byte-identical.

Live: a real frozen forecast (Brighton v Brentford, 8 Nov 2026) through the production v28 shortlist with
the production settings, policy and correction model. Harness: D (and M) in evaluation_harness.candidates
with the training results, shots and xG changed and the research model refitted, and in the live replay.

Some research columns ride along on cagey rows because the value tier annotates the shared decision rows
before the cagey list is cut (RESEARCH_CARRIED). They are labels only: no cagey probability, decision or
rank reads them, and the test pins that they are the only columns that move. Since cagey-own-probabilities-v1
the list's p_no_loss, predicted_probability and rank_probability carry the cagey tier's own figure, so they
must not move either; the research no-loss figure is research_p_no_loss.
"""
from __future__ import annotations

import copy
import json
from pathlib import Path
import unittest

import numpy as np
import pandas as pd

import evaluation_harness as eh
import narrow_margin as nm
import price_edge_cagey_shortlist as v28
import research_backtest as rb
from price_edge_shortlist import pinnacle_quotes
from test_value_model_independence import shake

REPO = Path(__file__).resolve().parents[1]
FROZEN = json.loads((Path(__file__).with_name('fixtures') / 'frozen_forecast_row.json').read_text(encoding='utf-8'))
CFG = json.loads((REPO / 'evaluation_harness_config.json').read_text(encoding='utf-8'))
POLICY = json.loads((REPO / 'shortlist_quote_policy.json').read_text(encoding='utf-8'))

# Fields the cagey tier may read: fixture identity and timing, and bookmaker quotes (or values derived only
# from quotes). Everything else on the row is a non-market input and is perturbed.
IDENTITY = ('date', 'league', 'home_team', 'away_team', 'fixture_id', 'kickoff_utc', 'fixture_source')
MARKET_PREFIXES = ('market_', 'price_edge_quotes', 'asian_handicap_offers', 'bet365_pinnacle_quotes', 'best_',
                   'totals_anchor_reference_', 'odds_')
RESEARCH_FIELDS = ('team_research_json', 'research_history_json', 'research_p_home', 'research_p_draw',
                   'research_p_away', 'research_p_over_1_5', 'research_probability_basis')
# Value-tier (research) or published-model columns carried on cagey rows; never read by the cagey tier.
RESEARCH_CARRIED = {'research_p_no_loss', 'in_value_tier', 'decision',
                    'rejection_reasons', 'selection_tier', 'model_win_share', 'model_vs_pinnacle_gap',
                    'profit_model_fair_odds', 'profit_model_edge', 'profit_probability', 'profit_expected_return',
                    'profit_price_flag', 'research_probability_basis', 'research_coverage', 'research_warnings',
                    'research_summary', 'research_details', 'research_sources', 'research_p_win',
                    'research_p_half_win', 'research_p_push', 'research_p_half_loss', 'research_p_loss'}
# What the cagey tier computes for each candidate (cagey_market_basis, cagey_tier_v3, narrow_support).
CAGEY_PREFIXES = ('cagey_', 'corrected_', 'narrow_', 'price_guard_', 'uncorrected_', 'totals_correction')
OFFER = ('fixture_id', 'market', 'market_to_bet', 'bookmaker', 'offered_decimal_odds', 'offered_last_update_utc',
         'handicap_side', 'handicap_line', 'price_flag', 'correction_validation_note')


def is_market(key):
    return key in IDENTITY or key.startswith(MARKET_PREFIXES)


def mirrored_research(row):
    """A different, valid research view: the margin distribution mirrored (home and away swapped), goal rates
    swapped, Over 1.5 moved, every form, head-to-head, schedule, rest and weather number changed, a team-news
    item added, and the training-history form (goals and xG) changed."""
    row = copy.deepcopy(row)
    research = json.loads(row['team_research_json'])
    research['margin_distribution'] = {str(-int(k)): v for k, v in research['margin_distribution'].items()}
    research['goal_rates'], research['base_rates'] = research['goal_rates'][::-1], research['base_rates'][::-1]
    research['p_over_1_5'] = 0.61
    research['form'], research['h2h'] = shake(research['form']), shake(research['h2h'])
    evidence = research['evidence']
    for key in ('recent', 'schedules', 'rest_and_travel', 'weather'):
        evidence[key] = shake(evidence[key])
    evidence['news'] = [{'title': 'Brighton first-choice striker ruled out', 'source': 'test'}]
    row['team_research_json'] = json.dumps(research)
    row['research_history_json'] = json.dumps(shake(json.loads(row['research_history_json'])))
    row.update(research_p_home=row['research_p_away'], research_p_away=row['research_p_home'],
               research_p_draw=0.31, research_p_over_1_5=0.61)
    return row


def no_research(row):
    return {**row, **dict.fromkeys(RESEARCH_FIELDS)}


def every_non_market_field(row):
    """Mirrored research, and every other non-market field (published model, Elo, shot and xG features, BBS,
    training status) changed too."""
    row = mirrored_research(row)
    return {k: v if is_market(k) or k in RESEARCH_FIELDS else shake(v) for k, v in row.items()}


def live_run(row, policy=POLICY):
    selected, decisions, summary = v28.build_shortlist(
        pd.DataFrame([row]), FROZEN['snapshot_generated_utc'], execution_policy=policy,
        settings=v28.load_settings(), model=nm.production_model())
    return selected, decisions, v28.cagey_tier_list(decisions), summary


def cagey_view(decisions):
    columns = [c for c in decisions.columns if c.startswith(CAGEY_PREFIXES) or c in OFFER]
    return decisions[columns].to_csv(index=False)


class LiveCageyResearchPerturbationTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.row = FROZEN['row']
        cls.base = live_run(cls.row)

    def test_the_frozen_row_exercises_the_production_cagey_rule(self):
        _, decisions, picks, summary = self.base
        self.assertEqual(summary['cagey_tier']['rule_version'], v28.TIER_RULE_MARKET_BASIS)
        self.assertEqual(v28.load_settings()['cagey_tier_rule'], v28.TIER_RULE_MARKET_BASIS)
        self.assertGreaterEqual(len(picks), 2)
        self.assertGreater(decisions.cagey_tier_decision.eq('NOT_SELECTED').sum(), 0)
        self.assertTrue(decisions.cagey_no_loss_probability.notna().all())

    def test_the_perturbation_covers_every_non_market_field(self):
        changed = every_non_market_field(self.row)
        moved = [k for k in self.row if changed[k] != self.row[k]]
        self.assertTrue(set(RESEARCH_FIELDS) - {'research_probability_basis'} <= set(moved))
        for key in ('lambda_home', 'goal_margin_distribution', 'score_matrix_json', 'p_home', 'elo_rating_diff',
                    'shot_lambda_home', 'dc_lambda_home', 'raw_goal_margin_distribution'):
            self.assertIn(key, moved)
        self.assertGreater(len(moved), 80)
        self.assertFalse([k for k in moved if is_market(k)])
        research = json.loads(changed['team_research_json'])
        self.assertTrue(research['evidence']['news'])
        self.assertNotEqual(research['form'], json.loads(self.row['team_research_json'])['form'])

    def test_research_changes_reach_the_value_tier(self):
        # Otherwise the test below would prove nothing: the value tier does read the research.
        selected, decisions, _, _ = live_run(mirrored_research(self.row))
        self.assertNotEqual(list(selected.market), list(self.base[0].market))
        self.assertFalse(decisions.research_p_win.equals(self.base[1].research_p_win))

    def test_cagey_probabilities_and_ranking_byte_identical_under_research_changes(self):
        _, base_decisions, base_picks, base_summary = self.base
        for name, change in (('mirrored research', mirrored_research), ('no research', no_research),
                             ('every non-market field', every_non_market_field)):
            with self.subTest(name):
                _, decisions, picks, summary = live_run(change(self.row))
                self.assertEqual(cagey_view(decisions), cagey_view(base_decisions))
                self.assertEqual(summary['cagey_tier'], base_summary['cagey_tier'])
                keep = [c for c in base_picks.columns if c not in RESEARCH_CARRIED]
                self.assertEqual(picks[keep].to_csv(index=False), base_picks[keep].to_csv(index=False))
                moved = {c for c in base_picks.columns
                         if picks[c].to_csv(index=False) != base_picks[c].to_csv(index=False)}
                self.assertTrue(moved, 'the perturbation must reach some carried research column')
                self.assertLessEqual(moved, RESEARCH_CARRIED)

    def test_a_pinnacle_price_change_does_move_the_cagey_view(self):
        # Positive control: the comparison above is not vacuous.
        row = copy.deepcopy(self.row)
        quotes = json.loads(row['price_edge_quotes'])
        for quote in quotes:
            if quote['bookmaker'] == 'Pinnacle' and quote['market'] == 'h2h':
                quote['prices']['home'] = round(quote['prices']['home'] * 1.06, 2)
        row['price_edge_quotes'] = json.dumps(quotes)
        _, decisions, _, _ = live_run(row)
        self.assertNotEqual(cagey_view(decisions), cagey_view(self.base[1]))

    def test_cagey_picks_are_quoted_at_pinnacle_only(self):
        self.assertEqual(POLICY['allowed_bookmakers'], ['Pinnacle'])
        self.assertEqual(POLICY['fallback_bookmakers'], [])
        books = {q['bookmaker'] for q in json.loads(self.row['price_edge_quotes'])}
        self.assertIn('1xBet', books)
        _, decisions, picks, _ = self.base
        self.assertEqual(set(picks.bookmaker), {'Pinnacle'})
        self.assertEqual(set(decisions.bookmaker), {'Pinnacle'})
        # The policy is what keeps 1xBet out: with it allowed, 1xBet candidates appear.
        _, wider, _, _ = live_run(self.row, {**POLICY, 'allowed_bookmakers': ['Pinnacle', '1xBet']})
        self.assertIn('1xBet', set(wider.bookmaker))


class HarnessCageyResearchPerturbationTest(unittest.TestCase):
    """D in the harness reads the period bookmaker's prices and the fixed correction model only."""

    @classmethod
    def setUpClass(cls):
        import historical_benchmark as hb
        from football_value_pipeline_v2_standalone import DixonColesModel
        data, _, _ = hb.load_history(REPO / '.football_cache', 'EPL',
                                     {**CFG, 'seasons': ['2223', '2324'], 'test_end_exclusive': '2024-07-01'})
        cls.origin = pd.Timestamp('2024-03-01')
        cls.train, cls.row = data[data.Date < cls.origin], data[data.Date >= cls.origin].iloc[0]
        rng = np.random.default_rng(3)
        changed = cls.train.copy()
        # Every result, shot and xG figure of the training history changes; so does the research model's fit.
        for col in ('FTHG', 'FTAG', 'HTHG', 'HTAG', 'HS', 'AS', 'HST', 'AST', 'HC', 'AC', 'HF', 'AF', 'HY', 'AY'):
            if col in changed:
                changed[col] = rng.integers(0, 6 if col.endswith('G') else 15, len(changed))
        cls.changed = changed
        fit = lambda t: DixonColesModel(half_life_days=480., l2=.08, max_goals=10, shot_features=True,
                                        bbs_statistics=False).fit(t.copy(), as_of=cls.origin)
        cls.model, cls.changed_model = fit(cls.train), fit(changed)
        xg = lambda t, seed: t.assign(HxG=np.random.default_rng(seed).uniform(0, 3, len(t)),
                                      AxG=np.random.default_rng(seed + 1).uniform(0, 3, len(t)))
        cls.xg, cls.changed_xg = xg(cls.train, 5), xg(changed, 7)
        cls.cagey = nm.production_model()

    def test_d_and_m_ignore_every_research_input(self):
        base, _, _ = eh.candidates(self.row, self.train, self.origin, self.model, CFG, self.cagey, self.xg)
        row = self.row.copy()
        for col in ('FTHG', 'FTAG', 'HS', 'AS', 'HST', 'AST', 'Referee'):
            if col in row:
                row[col] = 'X' if col == 'Referee' else 4
        moved, _, _ = eh.candidates(row, self.changed, self.origin, self.changed_model, CFG, self.cagey,
                                    self.changed_xg)
        self.assertFalse(np.array_equal(base['C'], moved['C']))
        self.assertFalse(np.array_equal(base['C3'], moved['C3']))
        for name in ('M', 'D'):
            np.testing.assert_array_equal(base[name], moved[name])
        # D is a function of this match's prices alone (no fold, no training rows, no origin).
        prices = eh.book_prices(self.row, 'pinnacle')
        np.testing.assert_array_equal(base['D'], eh.cagey_matrix(eh.market_matrix(prices), prices, self.cagey))
        self.assertFalse(np.array_equal(base['D'], base['M']))

    def test_live_replay_d_ignores_research_and_model_fields(self):
        cutoff = pd.Timestamp(FROZEN['snapshot_generated_utc'])

        def replay_d(row):
            matrices, _ = rb.archived_candidates(row, cutoff)
            pin = pinnacle_quotes(row)
            return eh.cagey_matrix(matrices['B'], {'hda': pin['h2h'][:3], 'ou': pin['ou25'][:2]}, self.cagey)

        base = replay_d(FROZEN['row'])
        for change in (mirrored_research, no_research, every_non_market_field):
            np.testing.assert_array_equal(replay_d(change(FROZEN['row'])), base)


class CorrectionOutOfSampleTest(unittest.TestCase):
    """The correction is fixed: fitted once on matches before validation, never refitted by the harness."""

    def test_the_correction_never_saw_a_validation_retrospective_or_holdout_match(self):
        model = nm.production_model()
        self.assertEqual(model['version'], v28.load_settings()['model_version'])
        self.assertEqual(nm.versions()['production']['version'], model['version'])
        self.assertLessEqual(pd.Timestamp(model['training_until_exclusive']), pd.Timestamp(CFG['development_end']))
        self.assertLess(pd.Timestamp(model['training_last_date']), pd.Timestamp(CFG['development_end']))
        self.assertLess(pd.Timestamp(model['training_last_date']), pd.Timestamp(CFG['holdout_start']))
        # Any change to the model file changes the setup fingerprint, so a holdout run can't reuse a score.
        self.assertIn(f"narrow_margin_models/{model['version']}.json", eh.SETUP_FILES)


if __name__ == '__main__':
    unittest.main()
