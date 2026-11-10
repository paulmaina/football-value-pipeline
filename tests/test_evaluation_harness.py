"""Evaluation harness: periods, bookmaker inputs, independence, pairing and the holdout lock."""
import json
from pathlib import Path
import tempfile
import unittest

import numpy as np
import pandas as pd

import evaluation_harness as eh

REPO = Path(__file__).resolve().parents[1]
CFG = json.loads((REPO / 'evaluation_harness_config.json').read_text(encoding='utf-8'))


def priced(**extra):
    row = {'PSH': 2.1, 'PSD': 3.4, 'PSA': 3.6, 'P>2.5': 1.95, 'P<2.5': 1.95, 'AHh': -0.25, 'PAHH': 1.95, 'PAHA': 1.97,
           'B365H': 2.05, 'B365D': 3.3, 'B365A': 3.5, 'B365>2.5': 1.9, 'B365<2.5': 1.9, 'B365AHH': 1.9, 'B365AHA': 1.95}
    return {**row, **extra}


class PeriodTest(unittest.TestCase):
    def test_periods_and_their_bookmaker(self):
        cases = [('2024-03-01', 'EPL', 'development', 'pinnacle'), ('2025-09-01', 'Eredivisie', 'validation', 'pinnacle'),
                 ('2026-01-15', 'SuperLig', 'validation', 'pinnacle'), ('2026-01-16', 'Eredivisie', 'holdout', 'bet365'),
                 ('2026-10-10', 'PrimeiraLiga', 'holdout', 'bet365'), ('2026-10-11', 'SuperLig', 'retrospective', 'bet365'),
                 ('2026-03-01', 'EPL', 'retrospective', 'bet365'), ('2026-10-20', 'LaLiga', 'retrospective', 'bet365')]
        for date, league, name, book in cases:
            self.assertEqual((eh.phase(date, league, CFG), eh.period_book(date, CFG)), (name, book), (date, league))

    def test_fold_windows_break_at_every_period_boundary(self):
        bounds = {b for w in eh.fold_windows(CFG, pd.Timestamp(CFG['end_exclusive'])) for b in w}
        self.assertTrue({pd.Timestamp(CFG[k]) for k in ('development_end', 'holdout_start', 'holdout_end_exclusive')} <= bounds)


class PricesTest(unittest.TestCase):
    def test_complete_prices_per_book(self):
        self.assertEqual(eh.book_prices(priced(), 'pinnacle')['hda'], (2.1, 3.4, 3.6))
        self.assertEqual(eh.book_prices(priced(), 'bet365')['ah'], (-0.25, 1.9, 1.95))

    def test_missing_or_invalid_prices_are_rejected(self):
        for bad in ({'PSH': np.nan}, {'PSH': 1.0}, {'AHh': -0.3}, {'PSH': 1.2}):
            self.assertIsNone(eh.book_prices(priced(**bad), 'pinnacle'), bad)

    def test_market_and_cagey_grids_are_normalised(self):
        import narrow_margin as nm
        prices = eh.book_prices(priced(), 'pinnacle')
        market = eh.market_matrix(prices)
        cagey = eh.cagey_matrix(market, prices, nm.production_model())
        self.assertAlmostEqual(float(market.sum()), 1, places=8)
        self.assertAlmostEqual(float(cagey.sum()), 1, places=8)
        goals = np.arange(market.shape[0])
        wide = np.abs(goals[:, None] - goals[None, :]) >= 2
        self.assertLess(cagey[wide].sum(), market[wide].sum())

    def test_synthetic_prices_add_the_margin(self):
        prices = eh.synthetic_prices([.5, .3, .2], .034)
        self.assertAlmostEqual(float((1 / prices).sum()), 1.034, places=9)
        with self.assertRaises(ValueError):
            eh.synthetic_prices([.5, 0., .5], .034)


class IndependenceTest(unittest.TestCase):
    """The research model must give identical probabilities whatever the odds say."""

    def test_research_model_ignores_every_odds_field(self):
        import historical_benchmark as hb
        from football_value_pipeline_v2_standalone import DixonColesModel
        data, _, _ = hb.load_history(REPO / '.football_cache', 'EPL',
                                     {**CFG, 'seasons': ['2223', '2324'], 'test_end_exclusive': '2024-07-01'})
        origin = pd.Timestamp('2024-03-01')
        train, row = data[data.Date < origin], data[data.Date >= origin].iloc[0]
        model = DixonColesModel(half_life_days=480., l2=.08, max_goals=10, shot_features=True,
                                bbs_statistics=False).fit(train.copy(), as_of=origin)
        base, _, _ = eh.research_matrix(row, train, origin, model)
        odds = [c for c in row.index if any(c.startswith(p) for p in ('PS', 'P>', 'P<', 'PC', 'PAH', 'B365', 'Max', 'Avg', 'BW', 'IW', 'WH', 'VC', 'AH', '1X'))]
        self.assertTrue(odds)
        changed = row.copy()
        changed[odds] = 9.99
        again, _, _ = eh.research_matrix(changed, train, origin, model)
        np.testing.assert_array_equal(base, again)


class PairedTest(unittest.TestCase):
    def test_positive_gain_means_the_candidate_is_better(self):
        scores = pd.DataFrame([
            {'fixture_key': f'f{i}', 'week': f'w{i % 4}', 'candidate': c, 'log_loss': v}
            for i in range(40) for c, v in (('C', 1.0), ('M', 0.9 + (i % 3) * .01))])
        result = eh.paired(scores, 'C', 'M')
        self.assertGreater(result['mean_gain'], 0)
        self.assertEqual((result['fixtures'], result['weeks']), (40, 4))
        self.assertTrue(result['clear_of_zero'])

    def test_unpaired_candidates_give_nothing(self):
        scores = pd.DataFrame([{'fixture_key': 'a', 'week': 'w', 'candidate': 'C', 'log_loss': 1.}])
        self.assertIsNone(eh.paired(scores, 'C', 'M'))


class HoldoutLockTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.dir = Path(self.tmp.name)
        self.ledger = self.dir / 'ledger.json'
        self.setup = {'sha256': 'a' * 64}

    def declaration(self, **extra):
        data = {'candidate': 'D', 'baseline': 'M', 'primary_metric': 'AH all',
                'draw_sensitive_lines': [-0.5, 0, 0.5], 'calibration_tolerance': 0.05,
                'declared_by': 'Paul', 'declared_at': '2026-11-10', **extra}
        path = self.dir / 'declaration.json'
        path.write_text(json.dumps(data), encoding='utf-8')
        return path

    def test_a_declaration_is_scored_once_per_candidate_and_per_setup(self):
        declared = eh.validate_declaration(self.declaration(), CFG, self.setup, self.ledger)
        eh.record_holdout(declared, self.setup, 'abc', 646, {'passes_holdout_gate': False}, self.ledger)
        with self.assertRaisesRegex(ValueError, "already scored for candidate 'D'"):
            eh.validate_declaration(self.declaration(), CFG, {'sha256': 'b' * 64}, self.ledger)
        # Same frozen setup under another candidate: refused too.
        with self.assertRaisesRegex(ValueError, 'frozen setup'):
            eh.validate_declaration(self.declaration(candidate='A'), CFG, self.setup, self.ledger)

    def test_the_declaration_must_match_registered_candidates_and_scoring(self):
        bad = [({'calibration_tolerance': None}, 'missing calibration_tolerance'),
               ({'candidate': 'research-v9'}, 'registered'), ({'candidate': 'M'}, 'registered'),
               ({'primary_metric': 'profit'}, 'Primary metric'), ({'draw_sensitive_lines': [0]}, 'Draw-sensitive'),
               ({'calibration_tolerance': 0.5}, 'between 0 and 0.2')]
        for extra, message in bad:
            with self.assertRaisesRegex(ValueError, message):
                eh.validate_declaration(self.declaration(**extra), CFG, self.setup, self.ledger)

    def test_setup_fingerprint_changes_with_code_data_or_config(self):
        cfg = {**CFG, 'leagues': ['EPL'], 'seasons': ['2526']}
        first = eh.setup_fingerprint(cfg, REPO / '.football_cache')
        self.assertEqual(first, eh.setup_fingerprint(cfg, REPO / '.football_cache'))
        self.assertNotEqual(first['sha256'], eh.setup_fingerprint({**cfg, 'step_days': 7}, REPO / '.football_cache')['sha256'])
        self.assertIn('data/2526_E0.csv', first['parts'])
        self.assertIn('evaluation_harness.py', first['parts'])

    def test_locked_runs_skip_the_holdout_and_holdout_runs_score_only_it(self):
        cfg = {**CFG, 'test_start': '2026-01-01', 'end_exclusive': '2026-02-15'}
        cache = str(REPO / '.football_cache')
        locked, _, coverage, _, _, _ = eh.evaluate_league('Eredivisie', cache, cfg, False)
        self.assertTrue(locked)
        self.assertEqual({r['phase'] for r in locked}, {'validation'})
        self.assertGreater(coverage['Eredivisie:locked_holdout'], 0)
        unlocked = eh.evaluate_league('Eredivisie', cache, cfg, True, keep={'D', 'M'})[0]
        holdout = [r for r in unlocked if r['phase'] == 'holdout']
        self.assertEqual({r['candidate'] for r in holdout}, {'D', 'M'})
        self.assertEqual({r['market_book'] for r in holdout}, {'bet365'})
        self.assertTrue({r['candidate'] for r in unlocked if r['phase'] != 'holdout'} <= {'MP', 'MB'})
        # Big-league matches after 16 Jan were already scored elsewhere: retrospective, never holdout.
        retro = eh.evaluate_league('EPL', cache, cfg, False)[0]
        self.assertIn('retrospective', {r['phase'] for r in retro})


class ReviewGuardTest(unittest.TestCase):
    def test_holdout_cannot_pass_below_the_sample_minimum(self):
        records, calib = [], []
        for i in range(30):
            for cand, loss in (('D', .6), ('M', .7)):
                records.append({'fixture_key': f'f{i}', 'league': 'Eredivisie', 'week': f'w{i % 2}',
                                'phase': 'holdout', 'candidate': cand, 'market': 'AH +0.00', 'log_loss': loss})
                calib.append({'phase': 'holdout', 'candidate': cand, 'probs': [.45, .25, .30], 'outcome': i % 3 == 0 and 0 or 2})
        declaration = {'candidate': 'D', 'baseline': 'M', 'primary_metric': 'AH all',
                       'draw_sensitive_lines': [-.5, 0, .5], 'calibration_tolerance': .2}
        verdict = eh.holdout_verdict(records, calib, declaration, {})
        self.assertTrue(verdict['primary']['clear_of_zero'])
        self.assertFalse(verdict['sample_minimum_met'])
        self.assertFalse(verdict['passes_holdout_gate'])
        self.assertEqual(verdict['sample_minimum'], {'fixtures': 300, 'weeks': 6})

    def test_locked_runs_never_train_on_holdout_results(self):
        data = pd.DataFrame({'Date': pd.to_datetime(['2025-12-01', '2026-01-16', '2026-06-01', '2026-10-11'])})
        kept = eh.training_rows(data, 'Eredivisie', CFG, False)
        self.assertEqual(list(kept.Date.dt.date.astype(str)), ['2025-12-01', '2026-10-11'])
        self.assertEqual(len(eh.training_rows(data, 'Eredivisie', CFG, True)), 4)
        self.assertEqual(len(eh.training_rows(data, 'EPL', CFG, False)), 4)

    def test_live_replay_rejects_turkish_results_without_source_evidence(self):
        with tempfile.TemporaryDirectory() as tmp:
            t1 = {'league_code': 'T1', 'source_status': 'FINISHED', 'match_id': 'x', 'source': 'football-data.co.uk',
                  'source_season_start': 2026, 'source_sha256': 'f' * 64, 'home_goals': 1, 'away_goals': 0}
            from unittest.mock import patch
            with patch('turkey_results.verified', return_value=True):
                coverage = {}
                from collections import Counter
                coverage = Counter()
                kept = eh.usable_results([t1], Path(tmp), coverage)
            self.assertEqual(kept, [])
            self.assertTrue(any(k.startswith('result_rejected') for k in coverage))


class SummaryTest(unittest.TestCase):
    def test_headline_uses_one_common_cohort(self):
        records = []
        for i in range(6):
            for cand in ('C', 'M', 'D', 'A') if i < 4 else ('C',):
                records.append({'fixture_key': f'f{i}', 'league': 'EPL', 'week': 'w', 'phase': 'validation',
                                'candidate': cand, 'market': '1X2', 'log_loss': 1. if cand == 'C' else .9})
        cohort = eh.common_cohort(eh.fixture_scores(records))
        row = next(r for r in cohort if r['group'] == '1X2')
        self.assertEqual(row['fixtures'], 4)
        self.assertAlmostEqual(row['C'], 1.)


KICKOFF = pd.Timestamp('2026-11-08T14:00:00Z')
FORECAST = pd.Timestamp('2026-11-08T12:20:00Z')
IN_WINDOW = '2026-11-08T12:14:35Z'


def ah(side, line, price, opposite, key='alternate_spreads', book='Pinnacle', stamp=IN_WINDOW):
    return {'bookmaker': book, 'side': side, 'line': line, 'price': price, 'opposite_price': opposite,
            'market_key': key, 'last_update_utc': stamp}


def frozen_row(**extra):
    quotes = [
        {'bookmaker': 'Pinnacle', 'market': 'h2h', 'market_key': 'h2h', 'last_update_utc': IN_WINDOW,
         'prices': {'home': 1.88, 'draw': 4.0, 'away': 4.11}},
        {'bookmaker': 'Pinnacle', 'market': 'double_chance', 'market_key': 'double_chance', 'last_update_utc': IN_WINDOW,
         'prices': {'home_draw': 1.27, 'draw_away': 2.03, 'home_away': 1.28}},
        {'bookmaker': 'Pinnacle', 'market': 'totals', 'market_key': 'totals', 'point': 2.5, 'last_update_utc': IN_WINDOW,
         'prices': {'over': 1.63, 'under': 2.39}},
        {'bookmaker': 'Bet365', 'market': 'double_chance', 'last_update_utc': IN_WINDOW,
         'prices': {'home_draw': 1.25, 'draw_away': 2.0}},
    ]
    offers = [ah('home', -0.5, 1.9, 2.0, 'spreads'), ah('away', 0.5, 2.0, 1.9, 'spreads'),
              ah('home', -0.5, 1.85, 2.05),  # alternate copy of the main line: dropped
              ah('home', 0.25, 1.33, 3.58), ah('home', 0.0, 1.45, 2.9, 'draw_no_bet'),
              ah('home', -1.0, 2.6, 1.5, book='1xBet'),
              ah('home', -1.5, 3.2, 1.35, stamp='2026-11-07T12:00:00Z'),  # older than 24h
              ah('home', -0.75, 2.2, 1.7, stamp='2026-11-08T12:30:00Z'),  # after the forecast
              ah('home', 1.0, 1.1, 7.0, stamp=None)]
    return {'price_edge_quotes': json.dumps(quotes), 'asian_handicap_offers': json.dumps(offers),
            'kickoff_utc': KICKOFF.isoformat(), 'league': 'EPL', **extra}


def grid():
    goals = np.arange(8)
    home, away = np.exp(-1.4) * 1.4 ** goals, np.exp(-1.1) * 1.1 ** goals
    matrix = np.outer(home / np.cumprod(np.r_[1, goals[1:]]), away / np.cumprod(np.r_[1, goals[1:]]))
    return matrix / matrix.sum()


class OfferScopeTest(unittest.TestCase):
    def test_only_pr135_pinnacle_markets_inside_24_hours(self):
        from collections import Counter
        coverage = Counter()
        offers = eh.scoped_offers(frozen_row(), KICKOFF, FORECAST, coverage)
        self.assertEqual(sorted(o['market'] for o in offers), [
            'Asian Handicap Away +0.50', 'Asian Handicap Home +0.25', 'Asian Handicap Home -0.50',
            'Away win', 'Double Chance 1X', 'Double Chance X2', 'Home win'])
        main = next(o for o in offers if o['market'] == 'Asian Handicap Home -0.50')
        self.assertEqual((main['source_market'], main['price']), ('spreads', 1.9))
        self.assertEqual(coverage['offer_out_of_scope:pinnacle draw_no_bet'], 1)
        self.assertEqual(coverage['offer_excluded:older than 24h before kickoff'], 1)
        self.assertEqual(coverage['offer_excluded:after forecast'], 1)
        self.assertEqual(coverage['offer_excluded:no timestamp'], 1)

    def test_window_is_measured_from_the_kickoff(self):
        early = frozen_row()
        self.assertEqual(eh.scoped_offers(early, KICKOFF + pd.Timedelta(hours=24), FORECAST), [])
        edge = eh.scoped_offers(early, pd.Timestamp(IN_WINDOW) + pd.Timedelta(hours=24), FORECAST)
        self.assertEqual(len(edge), 7)


class OfferScoreTest(unittest.TestCase):
    def setUp(self):
        self.matrix = grid()
        self.offers = eh.scoped_offers(frozen_row(), KICKOFF, FORECAST)
        self.ident = {'fixture_key': 'PL:1', 'league': 'EPL', 'week': '2026-W45', 'phase': 'live_replay'}

    def test_each_offer_is_scored_for_each_candidate(self):
        records = eh.score_offers(self.ident, {'M': self.matrix, 'C': self.matrix}, self.offers, 2, 1)
        self.assertEqual(len(records), 2 * len(self.offers))
        by = {r['market']: r for r in records if r['candidate'] == 'M'}
        h, a = np.indices(self.matrix.shape)
        p_home = self.matrix[h > a].sum()
        self.assertAlmostEqual(by['Home win']['log_loss'], -np.log(p_home))
        self.assertAlmostEqual(by['Away win']['log_loss'], -np.log(1 - self.matrix[h < a].sum()))
        self.assertAlmostEqual(by['Double Chance 1X']['log_loss'], -np.log(self.matrix[h >= a].sum()))
        self.assertAlmostEqual(by['Double Chance X2']['log_loss'], -np.log(1 - self.matrix[h <= a].sum()))
        # Home -0.50 wins outright at 2-1; the away side of the same pair loses outright.
        self.assertAlmostEqual(by['Asian Handicap Home -0.50']['log_loss'], -np.log(p_home))
        self.assertAlmostEqual(by['Asian Handicap Away +0.50']['log_loss'], -np.log(p_home))
        self.assertTrue(by['Asian Handicap Home -0.50']['draw_sensitive'])
        self.assertFalse(by['Asian Handicap Home +0.25']['draw_sensitive'])

    def test_quarter_line_settles_half(self):
        offer = [o for o in self.offers if o['market'] == 'Asian Handicap Home +0.25']
        record = eh.score_offers(self.ident, {'M': self.matrix}, offer, 1, 1)[0]
        h, a = np.indices(self.matrix.shape)
        self.assertAlmostEqual(record['log_loss'], -np.log(self.matrix[h == a].sum()))  # half win on a draw

    def test_each_match_counts_once_however_many_offers(self):
        records = []
        for i in range(10):
            ident = {**self.ident, 'fixture_key': f'PL:{i}', 'week': f'2026-W{40 + i % 3}'}
            offers = self.offers if i < 5 else self.offers[:2]
            records += eh.score_offers(ident, {'M': self.matrix, 'C': grid() ** 1.01 / (grid() ** 1.01).sum()},
                                       offers, i % 3, 1)
        scores = eh.match_scores(records)
        everything = scores.loc[scores.group == 'All offers']
        self.assertEqual(len(everything), 20)
        self.assertEqual(sorted(everything.offers.unique()), [2, 7])
        result = eh.paired(everything, 'C', 'M')
        self.assertEqual((result['fixtures'], result['weeks']), (10, 3))
        first = everything.query("fixture_key == 'PL:0' and candidate == 'M'").log_loss.item()
        self.assertAlmostEqual(first, np.mean([r['log_loss'] for r in records
                                               if r['fixture_key'] == 'PL:0' and r['candidate'] == 'M']))
        counts = eh.offer_counts(records)
        self.assertEqual((counts['matches'], counts['offers']), (10, 5 * 7 + 5 * 2))
        self.assertEqual(counts['per_market']['Home win'], {'matches': 10, 'offers': 10})
        self.assertEqual(counts['per_group']['Double chance'], {'matches': 5, 'offers': 10})
        calib = eh.offer_calibration(records)
        self.assertEqual(sum(b['n'] for b in calib if b['candidate'] == 'M'),
                         sum(1 for r in records if r['candidate'] == 'M' and 'won' in r))


class LiveReplayTest(unittest.TestCase):
    def replay(self, snapshots, result):
        from unittest.mock import patch
        import performance_tracking as pt
        import research_backtest as rb
        with patch.object(pt, 'snapshots', return_value=snapshots), \
                patch.object(pt, 'load_json', return_value=[result]), \
                patch.object(eh, 'usable_results', side_effect=lambda records, *a, **k: list(records)), \
                patch.object(pt, 'fixture_match', side_effect=lambda row, records: (result, 'GRADED')), \
                patch.object(rb, 'archived_candidates', return_value=({'A': grid()}, {})):
            return eh.live_replay(REPO / 'football_output_v2')

    def test_latest_pre_kickoff_forecast_stands_and_late_ones_are_not_graded(self):
        result = {'league_code': 'PL', 'match_id': 1, 'kickoff_utc': KICKOFF.isoformat(), 'home_goals': 2, 'away_goals': 1}
        meta = lambda when: {'generated_at_utc': when, 'captured_at_utc': when}
        older = frozen_row(price_edge_quotes='[]', asian_handicap_offers='[]')
        late = frozen_row()
        snapshots = [(meta('2026-11-08T09:00:00Z'), [older], []), (meta(FORECAST.isoformat()), [frozen_row()], []),
                     (meta('2026-11-08T13:50:00Z'), [late], [])]
        records, coverage = self.replay(snapshots, result)
        self.assertEqual(coverage['ungraded:FORECAST_NOT_BEFORE_VERIFIED_KICKOFF'], 1)
        self.assertEqual((coverage['verified_matches_graded'], coverage['matches_scored']), (1, 1))
        self.assertEqual(len(records), 7)  # the 12:20 forecast's in-scope offers, scored once each

    def test_window_uses_the_verified_kickoff(self):
        moved = (KICKOFF + pd.Timedelta(hours=30)).isoformat()
        result = {'league_code': 'PL', 'match_id': 1, 'kickoff_utc': moved, 'home_goals': 0, 'away_goals': 0}
        meta = {'generated_at_utc': FORECAST.isoformat(), 'captured_at_utc': FORECAST.isoformat()}
        records, coverage = self.replay([(meta, [frozen_row()], [])], result)
        self.assertEqual(records, [])
        self.assertEqual(coverage['no_in_scope_offer'], 1)

    def test_repository_replay_scores_only_scoped_offers_once_per_match(self):
        records, coverage = eh.live_replay(REPO / 'football_output_v2')
        if not records:
            self.skipTest('no graded live forecasts in this checkout')
        frame = pd.DataFrame(records)
        self.assertEqual(frame.fixture_key.nunique(), coverage['matches_scored'])
        self.assertLessEqual(coverage['matches_scored'], coverage['verified_matches_graded'])
        self.assertEqual(int(frame.groupby(['fixture_key', 'candidate', 'market']).size().max()), 1)
        self.assertTrue(set(frame.market_group) <= {'Asian handicap', 'Win', 'Double chance'})
        binary = set(frame.loc[frame.market_group != 'Asian handicap', 'market'])
        self.assertTrue(binary <= set(eh.BINARY_MARKETS))
        self.assertTrue(frame.loc[frame.market_group == 'Asian handicap', 'market'].str.match(
            r'^Asian Handicap (Home|Away) [+-]\d\.\d\d$').all())
        self.assertIn('D', set(frame.candidate))


if __name__ == '__main__':
    unittest.main()
