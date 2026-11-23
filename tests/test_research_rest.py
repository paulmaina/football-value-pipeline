"""C6R, C6 plus rest and congestion (docs/plan.md, Phase 2h): offline candidate, not registered in the harness."""
from __future__ import annotations

import json
from pathlib import Path
import tempfile
import unittest

import numpy as np
import pandas as pd

import research_rest as rr

ROOT = Path(__file__).resolve().parents[1]


def days(*values):
    return np.array([np.datetime64(v, 'D') for v in values], dtype='datetime64[D]')


class FeatureTest(unittest.TestCase):
    def test_only_strictly_earlier_days_count(self):
        d = days('2024-01-01', '2024-01-04', '2024-01-07')
        away = np.array([False, True, False])
        # The match day itself (07 Jan) is not an earlier match; the last earlier one is 04 Jan, 3 days before.
        self.assertEqual(rr.features_at(d, away, '2024-01-07'), (1., (2 - 3) / 3, 1.))

    def test_short_rest_boundary_and_congestion_cap(self):
        d = days(*pd.date_range('2023-12-01', periods=10, freq='3D').strftime('%Y-%m-%d'))
        away = np.zeros(10, bool)
        last = pd.Timestamp('2023-12-28')
        self.assertEqual(rr.features_at(d, away, last + pd.Timedelta(days=3))[0], 1.)
        self.assertEqual(rr.features_at(d, away, last + pd.Timedelta(days=4))[0], 0.)
        self.assertEqual(rr.features_at(d, away, last + pd.Timedelta(days=1))[1], 1.)  # 7 in 21 days, capped at 6

    def test_no_earlier_match(self):
        self.assertEqual(rr.features_at(days('2024-05-01'), np.array([True]), '2024-05-01'), (0., -1., 0.))

    def test_competitive_slugs(self):
        for slug in ('eng.1', 'eng.fa', 'eng.league_cup', 'eng.charity', 'uefa.champions', 'uefa.europa.conf_qual',
                     'fifa.cwc', 'fifa.intercontinental_cup', 'uefa.super_cup'):
            self.assertTrue(rr.competitive(slug, 'EPL'), slug)
        for slug in ('club.friendly', 'friendly.emirates_cup', 'usa.1', 'ger.audi_cup', 'esp.joan_gamper',
                     'global.champs_cup', 'eng.asia_trophy', 'jpn.world_challenge', 'global.club_challenge',
                     'euroamericana.supercopa', 'esp.1', ''):
            self.assertFalse(rr.competitive(slug, 'EPL'), slug)
        self.assertTrue(rr.competitive('esp.copa_del_rey', 'LaLiga'))
        self.assertFalse(rr.competitive('esp.joan_gamper', 'LaLiga'))

    def test_index_reads_compact_cache_and_pools_seasons(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp = Path(tmp)
            pd.DataFrame([{'league': 'EPL', 'season': 2023, 'fd_team': 'Arsenal', 'espn_id': '359',
                           'espn_name': 'Arsenal', 'method': 'reviewed'},
                          {'league': 'EPL', 'season': 2024, 'fd_team': 'Arsenal', 'espn_id': '359',
                           'espn_name': 'Arsenal', 'method': 'reviewed'}]).to_csv(tmp / 'map.csv', index=False)
            for season, events in ((2023, [('1', '2024-05-19T15:00Z', 'eng.1', True, 'home'),
                                           ('2', '2024-05-01T19:00Z', 'club.friendly', True, 'away')]),
                                   (2024, [('3', '2024-08-17T14:00Z', 'eng.1', True, 'home'),
                                           ('4', '2024-08-14T19:00Z', 'uefa.champions_qual', True, 'away'),
                                           ('5', '2024-08-10T19:00Z', 'eng.charity', False, 'home')])):
                (tmp / f'359_{season}.json').write_text(json.dumps({'schema': 'espn-schedule-compact-v1', 'events': [
                    {'id': i, 'date': d, 'slug': s, 'completed': c, 'status': None, 'side': side, 'opponent_id': '1'}
                    for i, d, s, c, side in events]}), encoding='utf-8')
            index = rr.load_index(tmp / 'map.csv', tmp)
            # 17 Aug 2024 (season 2024): last competitive match 14 Aug, a UEFA away qualifier; the friendly and the
            # uncompleted Community Shield do not count, so one match in the 21 days before.
            self.assertEqual(rr.match_features(index, 'EPL', 'Arsenal', '2024-08-17'), (1., (1 - 3) / 3, 1.))
            # 1 Jun 2024 (season 2023): the 2023/24 file alone; last match 19 May.
            self.assertEqual(rr.match_features(index, 'EPL', 'Arsenal', '2024-06-01'), (0., (1 - 3) / 3, 0.))
            self.assertIsNone(rr.match_features(index, 'EPL', 'Chelsea', '2024-08-17'))


class FitTest(unittest.TestCase):
    def synthetic(self, n, alpha, gamma, seed=0):
        rng = np.random.default_rng(seed)
        rates = rng.uniform(.8, 2.0, size=(n, 2))
        fh = np.column_stack([rng.random(n) < .1, rng.uniform(-1, 1, n), rng.random(n) < .05]).astype(float)
        fa = np.column_stack([rng.random(n) < .1, rng.uniform(-1, 1, n), rng.random(n) < .05]).astype(float)
        lh = rates[:, 0] * np.exp(fh @ alpha + fa @ gamma)
        la = rates[:, 1] * np.exp(fa @ alpha + fh @ gamma)
        return rates, rng.poisson(lh), rng.poisson(la), fh, fa

    def test_neutral_below_minimum(self):
        rates, hg, ag, fh, fa = self.synthetic(rr.MIN_MATCHES - 1, np.zeros(3), np.zeros(3))
        out = rr.fit(rates, hg, ag, fh, fa)
        self.assertEqual(out['status'], 'warm_up')
        self.assertEqual(rr.adjusted_rates([1.3, 1.1], out, [1, 1, 1], [0, 1, 0]), [1.3, 1.1])

    def test_recovers_known_effects(self):
        alpha, gamma = np.array([-.08, -.05, -.06]), np.array([.06, .04, .05])
        out = rr.fit(*self.synthetic(200_000, alpha, gamma))
        self.assertEqual(out['status'], 'fitted')
        got = np.array([out[p] for p in rr.PARAMETERS])
        np.testing.assert_allclose(got, np.concatenate([alpha, gamma]), atol=.02)

    def test_prior_shrinks_towards_zero(self):
        alpha, gamma = np.array([-.3, 0., 0.]), np.zeros(3)
        small = rr.fit(*self.synthetic(rr.MIN_MATCHES, alpha, gamma, seed=3))
        self.assertLess(abs(small['alpha_short_rest']), .3)

    def test_walk_forward_never_reads_a_later_result(self):
        rng = np.random.default_rng(1)
        n = 3000
        dates = pd.date_range('2022-08-01', periods=n, freq='4h')
        research = [{'date': d, 'goal_rates': [1.4, 1.1], 'home_goals': int(rng.poisson(1.4)),
                     'away_goals': int(rng.poisson(1.1))} for d in dates]
        feats = [(np.array([float(rng.random() < .2), rng.uniform(-1, 1), 0.]),
                  np.array([0., rng.uniform(-1, 1), float(rng.random() < .1)])) for _ in range(n)]
        cut = dates[2600]
        windows = [(dates[0], dates[2100]), (dates[2100], cut), (cut, dates[-1] + pd.Timedelta(days=1))]
        before, _ = rr.walk_forward(research, feats, windows)
        changed = [{**r, 'home_goals': 9} if r['date'] >= cut else r for r in research]
        after, _ = rr.walk_forward(changed, feats, windows)
        inside = np.asarray(pd.DatetimeIndex(dates) < cut)
        np.testing.assert_array_equal(before[inside], after[inside])
        np.testing.assert_array_equal(before[:2100], np.array([[1.4, 1.1]] * 2100))  # warm-up: C's rates


class C6REqualsC6WithoutFeatures(unittest.TestCase):
    def test_zero_features_give_c6_exactly(self):
        import evaluation_harness as eh
        from scripts import c6_rest_report as report
        cfg = json.loads(eh.CONFIG.read_text(encoding='utf-8'))
        end = pd.Timestamp('2023-03-01')
        cfg = {**cfg, 'end_exclusive': end.date().isoformat()}
        rng = np.random.default_rng(7)
        dates = pd.date_range('2022-08-01', end - pd.Timedelta(days=1), periods=2600)
        research = []
        for i, d in enumerate(dates):
            key = f'EPL|{d.date()}|H{i}|A{i}'
            research.append({'identity': {'league': 'EPL', 'date': d.date().isoformat(), 'phase': 'development',
                                          'week': f'{d.isocalendar().year}-W{d.isocalendar().week:02d}',
                                          'fixture_key': key, 'market_book': ''},
                             'date': d, 'fixture_key': key, 'goal_rates': list(rng.uniform(.9, 1.9, 2)),
                             'home_goals': int(rng.poisson(1.5)), 'away_goals': int(rng.poisson(1.1)), 'scored': True})
        feats = [(np.zeros(3), np.zeros(3)) for _ in research]
        c6_records, c6_calib, _, _ = eh.low_score_sharpen_candidate(research, cfg, end, {'C6'})
        r, k, fits = report.c6r_candidate(research, feats, cfg, end)
        self.assertTrue(any(f['status'] == 'fitted' for f in fits))
        strip = lambda rows: [{x: v for x, v in row.items() if x != 'candidate'} for row in rows]
        self.assertEqual(strip(r), strip(c6_records))
        self.assertEqual(strip(k), strip(c6_calib))


class IndependenceTest(unittest.TestCase):
    def test_no_odds_or_market_input(self):
        text = (ROOT / 'research_rest.py').read_text(encoding='utf-8')
        for token in ('market_implied', 'narrow_margin', 'book_prices', 'market_matrix', 'cagey', 'PSH', 'PSA',
                      'B365', 'AHh', 'P>2.5', 'score_matrix_json', 'published_proxy', 'odds_api', 'pinnacle'):
            self.assertNotIn(token, text, token)

    def test_backfill_cache_stores_no_result(self):
        from scripts import backfill_espn_schedules as bf
        raw = {'events': [{'id': '1', 'date': '2024-08-17T14:00Z', 'league': {'slug': 'eng.1'},
                           'competitions': [{'status': {'type': {'completed': True, 'name': 'STATUS_FULL_TIME'}},
                                             'competitors': [{'homeAway': 'home', 'team': {'id': '359'},
                                                              'score': {'value': 2}, 'winner': True},
                                                             {'homeAway': 'away', 'team': {'id': '1'},
                                                              'score': {'value': 0}, 'winner': False}]}]}]}
        out = bf.compact(raw, '359')
        self.assertEqual(set(out[0]), {'id', 'date', 'slug', 'completed', 'status', 'side', 'opponent_id'})
        text = json.dumps(out)
        self.assertNotIn('score', text)
        self.assertNotIn('winner', text)
        self.assertEqual((out[0]['side'], out[0]['opponent_id'], out[0]['completed']), ('home', '1', True))


if __name__ == '__main__':
    unittest.main()
