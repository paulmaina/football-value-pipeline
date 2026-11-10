"""Value model input schema, odds-perturbation and harness/live parity (docs/plan.md, release gate).

The value shortlist's research model (team_form_poisson_v1) may read only
team_research.INPUT_SCHEMA plus pre-kickoff research. These tests change every
odds field of a real frozen forecast, and of the live prediction path, and
require the research probabilities to stay identical. The parity tests feed the
same matches through evaluation_harness.research_matrix and the live pipeline
(_predict_row -> team_research.enrich -> frozen replay) and require identical
probabilities, and pin the known input differences so they stay visible.
"""
from __future__ import annotations

import copy
from datetime import datetime, timedelta, timezone
import json
import math
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import numpy as np
import pandas as pd

import evaluation_harness as eh
import historical_benchmark as hb
import profit_shortlist as ps
import research_backtest as rb
import team_research as tr
from football_value_pipeline_v2_standalone import DixonColesModel, FootballValuePipelineV2

REPO = Path(__file__).resolve().parents[1]
FIXTURE = json.loads((Path(__file__).with_name('fixtures') / 'frozen_forecast_row.json').read_text(encoding='utf-8'))
CFG = json.loads((REPO / 'evaluation_harness_config.json').read_text(encoding='utf-8'))
ODDS_TOKENS = ('odds', 'price', 'quote', 'offer', 'market', 'bookmaker', 'pinnacle', 'bet365', 'live_ref', 'live_best',
               'fair_', 'edge', 'ev_', 'anchor', 'devig', 'overround', 'closing', 'blend', 'score_matrix', 'p_')
LINE_KEYS = ('line', 'point', 'handicap')
RESEARCH_OUTPUTS = ('team_research_json', 'research_p_home', 'research_p_draw', 'research_p_away',
                    'research_p_over_1_5', 'research_probability_basis')
PROBABILITIES = ('research_p_home', 'research_p_draw', 'research_p_away', 'research_p_over_1_5')


def is_odds_field(key: str) -> bool:
    key = key.lower()
    return not key.startswith('research_') and any(token in key for token in ODDS_TOKENS)


def shake(value, depth=0):
    """A different but well-formed value: prices move, JSON keeps its shape."""
    if isinstance(value, bool) or value is None:
        return value
    if isinstance(value, (int, float)):
        return float(value) * 1.37 + 0.11 if math.isfinite(value) else value
    if isinstance(value, dict):
        # Prices move; handicap lines and totals points keep valid values.
        return {k: v if any(t in str(k).lower() for t in LINE_KEYS) else shake(v, depth + 1) for k, v in value.items()}
    if isinstance(value, list):
        return [shake(v, depth + 1) for v in value]
    if isinstance(value, str):
        try:
            return shake(float(value)) if depth == 0 and value.strip() else value
        except ValueError:
            pass
        try:
            decoded = json.loads(value)
        except ValueError:
            return value
        return json.dumps(shake(decoded, depth + 1)) if isinstance(decoded, (dict, list)) else value
    return value


def frozen_row():
    row = copy.deepcopy(FIXTURE['row'])
    research = json.loads(row['team_research_json'])
    evidence = research['evidence']
    for key in eh.DERIVED_EVIDENCE:
        evidence.pop(key, None)
    inputs = {k: v for k, v in row.items() if k not in RESEARCH_OUTPUTS}
    return inputs, evidence, tr.utc(research['observed_at_utc']), research


def replay(row, evidence, cutoff):
    """team_research.enrich on the frozen pre-kickoff evidence, with no network."""
    frame = pd.DataFrame([row])
    with tempfile.TemporaryDirectory() as tmp, \
            patch.object(tr, 'collect_fixture', side_effect=lambda r, c: copy.deepcopy(evidence)):
        out = tr.enrich(frame, tmp, fetch=False, clock=lambda: cutoff.to_pydatetime())
    return out.iloc[0].to_dict()


def research_view(row):
    context = json.loads(row['team_research_json'])
    return ({k: row[k] for k in PROBABILITIES},
            {k: context[k] for k in ('goal_rates', 'base_rates', 'margin_distribution', 'p_over_1_5', 'form')})


class InputSchemaTest(unittest.TestCase):
    def test_schema_names_no_odds_or_market_field(self):
        for key in (*tr.INPUT_SCHEMA, *tr.EVIDENCE_SCHEMA, *tr.RESULT_FIELDS):
            self.assertFalse(is_odds_field(key), key)
        # An offer contributes what the bet is, never its price.
        self.assertEqual(ps.OFFER_TERMS, ('market', 'handicap_side', 'handicap_line'))
        self.assertEqual(set(tr.INPUT_SCHEMA), {'home_team', 'away_team', 'kickoff_utc', 'lambda_home',
                                                 'lambda_away', 'research_history_json'})

    def test_prepare_reads_only_schema_fields(self):
        row, evidence, cutoff, _ = frozen_row()
        garbage = {k: (v if k in tr.INPUT_SCHEMA else 'garbage') for k, v in row.items()}
        garbage.update(p_home=0.99, market_p_home=0.99, score_matrix_json='[[1]]', goal_margin_distribution='{"0": 1}')
        same = lambda r: json.dumps(tr.prepare(r, cutoff, copy.deepcopy(evidence)), sort_keys=True, default=str)
        self.assertEqual(same(row), same(garbage))
        self.assertEqual(same(row), same(tr.research_inputs(row)))

    def test_only_result_fields_of_research_rows_feed_the_numbers(self):
        row, evidence, cutoff, _ = frozen_row()
        noisy = copy.deepcopy(evidence)
        for rows in noisy['recent'].values():
            for r in rows:
                r.update(odds={'home': 1.5}, market_p_home=0.9)
        noisy['odds'] = {'pinnacle': [2.0, 3.4, 3.9]}
        a, b = tr.prepare(row, cutoff, copy.deepcopy(evidence)), tr.prepare(row, cutoff, noisy)
        self.assertEqual(a['margin_distribution'], b['margin_distribution'])
        self.assertEqual(a['goal_rates'], b['goal_rates'])

    def test_offer_price_never_reaches_research_probabilities(self):
        _, _, cutoff, research = frozen_row()
        item = {'market': 'Asian Handicap Home -0.25', 'handicap_side': 'home', 'handicap_line': -0.25}
        cheap = ps.probabilities({}, {**item, 'offered_decimal_odds': 1.4, 'p_home': .1}, research)
        dear = ps.probabilities({'odds': 9}, {**item, 'offered_decimal_odds': 3.9, 'p_home': .9}, research)
        self.assertEqual(cheap, dear)


class FrozenRowOddsPerturbationTest(unittest.TestCase):
    """A real frozen forecast (Brighton v Brentford, 8 Nov 2026) with every odds field changed."""

    def test_replay_reproduces_the_frozen_research(self):
        row, evidence, cutoff, research = frozen_row()
        out = replay(row, evidence, cutoff)
        context = json.loads(out['team_research_json'])
        self.assertEqual(context['goal_rates'], research['goal_rates'])
        for key, value in research['margin_distribution'].items():
            self.assertAlmostEqual(context['margin_distribution'][key], value, places=15)
        for key in PROBABILITIES:
            self.assertAlmostEqual(out[key], float(FIXTURE['row'][key]), places=12)

    def test_every_odds_field_changed_research_probabilities_identical(self):
        row, evidence, cutoff, _ = frozen_row()
        odds_fields = [k for k in row if is_odds_field(k)]
        perturbed = {k: (shake(v) if k in odds_fields else v) for k, v in row.items()}
        changed = [k for k in odds_fields if perturbed[k] != row[k]]
        self.assertGreater(len(changed), 100)
        for key in ('market_p_home', 'market_home_odds', 'p_home', 'score_matrix_json', 'price_edge_quotes',
                    'asian_handicap_offers', 'totals_anchor_reference_over_odds'):
            self.assertIn(key, changed)
        self.assertFalse(set(changed) & set(tr.INPUT_SCHEMA))
        base, moved = replay(row, evidence, cutoff), replay(perturbed, evidence, cutoff)
        self.assertEqual(research_view(base), research_view(moved))

        # The selection layer still prices the identical research against the (changed) offer.
        now = cutoff + pd.Timedelta(minutes=1)
        item = {'market': 'Asian Handicap Home -0.25', 'handicap_side': 'home', 'handicap_line': -0.25,
                'offered_last_update_utc': now.isoformat(), 'decision': 'REJECTED', 'rejection_reasons': ''}
        a = ps.annotate(base, {**item, 'offered_decimal_odds': 1.9}, now, 0.)
        b = ps.annotate(moved, {**item, 'offered_decimal_odds': shake(1.9)}, now, 0.)
        for kind in ('win', 'half_win', 'push', 'half_loss', 'loss'):
            self.assertEqual(a['research_p_' + kind], b['research_p_' + kind])
        self.assertNotEqual(a['profit_expected_return'], b['profit_expected_return'])

    def test_frozen_live_replay_candidate_ignores_odds(self):
        row, evidence, cutoff, _ = frozen_row()
        base = replay(row, evidence, cutoff)
        moved = {k: (shake(v) if is_odds_field(k) else v) for k, v in base.items()}
        a, _ = rb.archived_candidates(base, cutoff)
        b, _ = rb.archived_candidates(moved, cutoff)
        np.testing.assert_array_equal(a['C'], b['C'])


def toy_model():
    model = DixonColesModel(max_goals=10)
    model.teams = ['Arsenal', 'Chelsea']
    model.team_to_idx = {t: i for i, t in enumerate(model.teams)}
    model.attack, model.weakness = np.array([.18, .02]), np.array([-.1, .06])
    model.base, model.home_adv, model.rho = math.log(1.25), math.log(1.15), -.07
    model.training_as_of = pd.Timestamp('2026-11-01')
    return model


def live_pipeline(history):
    pipe = object.__new__(FootballValuePipelineV2)
    pipe.market_weight, pipe.devig_method, pipe.totals_anchor = .7, 'power', True
    pipe.model_version = 'test-production'
    pipe._validation_history = history
    return pipe


def epl_history():
    data, _, _ = hb.load_history(REPO / '.football_cache', 'EPL', {**CFG, 'test_end_exclusive': CFG['end_exclusive']})
    return data


class LivePipelineOddsPerturbationTest(unittest.TestCase):
    """Odds enter the live pipeline at _predict_row; the research inputs and probabilities must not move."""

    def live_row(self, scale):
        now = datetime.now(timezone.utc)
        price = lambda p: round(p * scale + (scale - 1) * .2, 3)
        return pd.Series({
            'HomeTeam': 'Arsenal', 'AwayTeam': 'Chelsea', 'kickoff_utc': (now + timedelta(hours=20)).isoformat(),
            'odds_source': 'The Odds API', 'odds_event_id': 'e1',
            'odds_h2h_last_update_utc': now.isoformat(), 'odds_ou25_last_update_utc': now.isoformat(),
            'live_ref_home_odds': price(1.7), 'live_ref_draw_odds': price(4.0), 'live_ref_away_odds': price(5.2),
            'live_best_home_odds': price(1.74), 'live_best_draw_odds': price(4.1), 'live_best_away_odds': price(5.4),
            'live_ref_1x2_bookmaker': 'pinnacle', 'live_ref_ou25_bookmaker': 'pinnacle',
            'live_ref_over_2_5_odds': price(1.8), 'live_ref_under_2_5_odds': price(2.05),
            'live_best_over_2_5_odds': price(1.83), 'live_best_under_2_5_odds': price(2.1),
            'shadow_pinnacle_totals': {'bookmaker': 'pinnacle', 'event_id': 'e1', 'updated_at_utc': now.isoformat(),
                                       'over': price(1.8), 'under': price(2.05)},
            'bet365_pinnacle_quotes': json.dumps([{'bookmaker': 'pinnacle', 'price': price(1.7)}]),
            'asian_handicap_offers': json.dumps([{'line': -0.5, 'home': price(1.7), 'away': price(2.2)}]),
            'price_edge_quotes': json.dumps([{'market': 'h2h', 'prices': {'home': price(1.7)}}])})

    def test_changing_every_odds_input_leaves_research_identical(self):
        history = epl_history()
        history = history.loc[history.Date < pd.Timestamp('2026-11-01')]
        model, pipe = toy_model(), live_pipeline(history)
        outputs = []
        for scale in (1.0, 1.6):
            pred, _ = pipe._predict_row(model, self.live_row(scale))
            pred.update(league='Premier League', home_team='Arsenal', away_team='Chelsea',
                        kickoff_utc=self.live_row(scale)['kickoff_utc'])
            outputs.append(pred)
        first, second = outputs
        self.assertTrue(first['market_blend_applied'])
        self.assertTrue(first['totals_anchor_applied'])
        self.assertNotAlmostEqual(first['p_home'], second['p_home'], places=4)  # the published grid did move
        for key in tr.INPUT_SCHEMA:
            if key != 'kickoff_utc':
                self.assertEqual(first[key], second[key], key)
        cutoff = tr.utc(first['kickoff_utc']) - pd.Timedelta(hours=3)
        with tempfile.TemporaryDirectory() as tmp:
            enriched = [tr.enrich(pd.DataFrame([o]), tmp, fetch=False, clock=lambda: cutoff.to_pydatetime()).iloc[0]
                        for o in outputs]
        self.assertEqual(research_view(enriched[0]), research_view(enriched[1]))


class HarnessLiveParityTest(unittest.TestCase):
    """The same development-period matches through the harness and the live pipeline."""

    @classmethod
    def setUpClass(cls):
        data = epl_history()
        # One real harness fold in the development period.
        cls.origin, stop = next(w for w in eh.fold_windows(CFG, pd.Timestamp(CFG['end_exclusive']))
                                if w[0] >= pd.Timestamp('2024-02-01'))
        cls.train = data.loc[data.Date < cls.origin]
        cls.test = data.loc[(data.Date >= cls.origin) & (data.Date < stop)].head(12)
        profile = CFG['production_v2']
        cls.model = DixonColesModel(half_life_days=profile['half_life_days'], l2=CFG['baseline_l2'],
                                    max_goals=CFG['max_goals'], shot_features=profile['shot_features'],
                                    bbs_statistics=False).fit(cls.train.copy(), as_of=cls.origin)
        assert eh.phase(cls.test.Date.max(), 'EPL', CFG) == 'development'

    def test_harness_and_live_research_probabilities_are_identical(self):
        self.assertGreaterEqual(len(self.test), 10)
        pipe = live_pipeline(self.train)
        pipe.totals_anchor = True
        for _, match in self.test.iterrows():
            harness, _, info = eh.research_matrix(match, self.train, self.origin, self.model)
            row = match.copy()
            kickoff = (match.Date + pd.Timedelta(hours=15)).tz_localize('UTC')
            row['kickoff_utc'] = kickoff.isoformat()
            pred, _ = pipe._predict_row(self.model, row)  # real Pinnacle columns drive the blend and anchor
            self.assertTrue(pred['market_blend_applied'])
            pred.update(league='Premier League', home_team=match.HomeTeam, away_team=match.AwayTeam,
                        kickoff_utc=row['kickoff_utc'])
            self.assertEqual((pred['lambda_home'], pred['lambda_away']), (info['lambda_home'], info['lambda_away']))
            cutoff = kickoff - pd.Timedelta(hours=3)
            with tempfile.TemporaryDirectory() as tmp:
                live = tr.enrich(pd.DataFrame([pred]), tmp, fetch=False, clock=lambda: cutoff.to_pydatetime()).iloc[0]
            context = json.loads(live['team_research_json'])
            self.assertEqual(context['margin_distribution'], json.loads(__import__('asian_handicap').margins(harness)))
            h, a = np.indices(harness.shape)
            self.assertEqual(live['research_p_home'], sum(context['margin_distribution'][str(d)]
                                                          for d in range(1, harness.shape[0])))
            self.assertAlmostEqual(live['research_p_home'], float(harness[h > a].sum()), places=14)
            self.assertAlmostEqual(live['research_p_draw'], float(harness[h == a].sum()), places=14)
            # The live replay (evaluation_harness --mode live) rebuilds the same grid from the frozen row.
            replayed, gaps = rb.archived_candidates(live.to_dict(), cutoff + pd.Timedelta(minutes=1))
            self.assertNotIn('C', gaps)
            np.testing.assert_array_equal(replayed['C'], harness)

    def test_harness_inputs_follow_the_schema(self):
        match = self.test.iloc[0]
        _, info = self.model.score_matrix(match.HomeTeam, match.AwayTeam)
        self.assertEqual(set(eh.research_inputs(match, self.train, self.origin, info)), set(tr.INPUT_SCHEMA))


class KnownParityDifferencesTest(unittest.TestCase):
    """Input differences between live and harness research, reported rather than hidden.

    On the real frozen row the live form includes European and cup games the
    football-data files don't have, and counts one league match twice because ESPN
    ("Hull City") and the training history ("Hull") name the opponent differently.
    evaluation_harness --mode parity reports both across every frozen forecast.
    """

    def test_frozen_row_off_league_and_double_counted_rows_are_detected(self):
        row, evidence, cutoff, _ = frozen_row()
        data = epl_history()
        results = set()
        for d, h, a, hg, ag in zip(data.Date, data.HomeTeam, data.AwayTeam, data.FTHG, data.FTAG):
            for team in (h, a):
                results.add(eh._team_day({'date': d, 'home': h, 'away': a, 'home_goals': hg, 'away_goals': ag}, team))
        starts = {y: data.Date[data.Date >= pd.Timestamp(f'{y}-07-01')].min() for y in range(2021, 2027)}
        inputs = tr.research_inputs(row)
        classes = {}
        for side in ('home', 'away'):
            team = inputs[side + '_team']
            used = eh._used_rows(inputs, evidence, cutoff, side)
            classes[side] = {(r['home'], r['away']): eh._classify(r, team, results, starts)
                             for r in used if r['source'] != eh.TRAINING_HISTORY}
            classes[side + '_double'] = eh._double_counted(used, team)
        self.assertEqual(classes['home'][('Jablonec', 'Brighton & Hove Albion')], 'off_league_in_season')
        self.assertEqual(classes['home'][('Getafe', 'Brighton & Hove Albion')], 'off_league_in_season')
        self.assertEqual(classes['away'][('Hull City', 'Brentford')], 'league')
        self.assertEqual((classes['home_double'], classes['away_double']), (0, 1))

    def test_live_research_with_evidence_differs_from_the_harness_view(self):
        row, evidence, cutoff, research = frozen_row()
        bare = tr.prepare(row, cutoff)  # what the harness can see: team history only
        self.assertNotEqual(bare['goal_rates'], research['goal_rates'])
        self.assertEqual(bare['base_rates'], research['base_rates'])


class ParityModeTest(unittest.TestCase):
    def test_parity_mode_writes_a_report_without_scoring_results(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / 'out'
            self.assertEqual(eh.main(['--mode', 'parity', '--root', tmp, '--output', str(out)]), 0)
            report = json.loads((out / 'results.json').read_text(encoding='utf-8'))
        self.assertEqual((report['mode'], report['forecasts']), ('research_parity', 0))
        self.assertTrue(report['same_inputs']['identical_within_1e-12'])
        self.assertNotIn('log_loss_common_cohort', report)


if __name__ == '__main__':
    unittest.main()
