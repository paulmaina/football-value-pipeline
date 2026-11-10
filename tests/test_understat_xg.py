"""Candidate C3 (understat_history): historical Understat xG in the research form, its
identity rules, its pre-kickoff cut and its independence from odds (docs/plan.md, Phase 2d)."""
import hashlib
import json
from pathlib import Path
import tempfile
import unittest

import numpy as np
import pandas as pd

import evaluation_harness as eh
import understat_history as uh

REPO = Path(__file__).resolve().parents[1]
CFG = json.loads((REPO / 'evaluation_harness_config.json').read_text(encoding='utf-8'))
ODDS_PREFIXES = ('PS', 'P>', 'P<', 'PC', 'PAH', 'B365', 'Max', 'Avg', 'BW', 'IW', 'WH', 'VC', 'AH', '1X', 'BF', 'PSC')


def fd(rows):
    return pd.DataFrame([{'Date': pd.Timestamp(d), 'HomeTeam': h, 'AwayTeam': a, 'FTHG': hg, 'FTAG': ag}
                         for d, h, a, hg, ag in rows])


def us(rows):
    return pd.DataFrame([{'understat_id': str(i), 'season': '2023', 'kickoff_utc': pd.Timestamp(d, tz='UTC'),
                          'date': pd.Timestamp(d).normalize(), 'home': h, 'away': a, 'home_goals': hg,
                          'away_goals': ag, 'home_xg': hx, 'away_xg': ax}
                         for i, (d, h, a, hg, ag, hx, ax) in enumerate(rows)], columns=uh.COLUMNS)


class AttachTest(unittest.TestCase):

    def test_same_teams_day_and_score_attach(self):
        data = fd([('2023-08-12', 'Man City', 'Burnley', 3, 0), ('2023-08-13', 'Wolves', 'Leeds', 1, 1)])
        xg = us([('2023-08-11 23:30', 'Man City', 'Burnley', 3, 0, 2.4, .3),   # UTC date a day earlier
                 ('2023-08-13 14:00', 'Wolves', 'Leeds', 2, 1, 1.1, .9)])       # score disagrees
        out, counts = uh.attach_xg(data, xg)
        self.assertEqual(list(out.HxG.iloc[:1]), [2.4])
        self.assertTrue(np.isnan(out.HxG.iloc[1]))
        self.assertEqual((counts['attached'], counts['score_mismatch']), (1, 1))

    def test_far_dates_and_two_candidates_attach_nothing(self):
        data = fd([('2023-08-12', 'A', 'B', 1, 0), ('2023-09-12', 'C', 'D', 0, 0)])
        xg = us([('2023-08-15 12:00', 'A', 'B', 1, 0, 1., 1.),
                 ('2023-09-11 12:00', 'C', 'D', 0, 0, 1., 1.), ('2023-09-13 12:00', 'C', 'D', 0, 0, 1., 1.)])
        out, counts = uh.attach_xg(data, xg)
        self.assertTrue(out.HxG.isna().all())
        self.assertEqual((counts['no_understat_match'], counts['ambiguous']), (1, 1))

    def test_names_map_through_reviewed_aliases_only(self):
        with tempfile.TemporaryDirectory() as tmp:
            cache = Path(tmp)
            (cache / 'understat').mkdir()
            body = json.dumps([{'id': '1', 'isResult': True, 'datetime': '2023-08-11 19:00:00',
                                'h': {'title': 'Manchester City'}, 'a': {'title': 'Burnley'},
                                'goals': {'h': '3', 'a': '0'}, 'xG': {'h': '2.4', 'a': '0.3'}},
                               {'id': '2', 'isResult': False, 'datetime': '2023-08-19 19:00:00',
                                'h': {'title': 'Burnley'}, 'a': {'title': 'Manchester City'},
                                'goals': {'h': None, 'a': None}, 'xG': {'h': None, 'a': None}}]).encode()
            (cache / 'understat' / 'EPL_2023.json').write_bytes(body)
            (cache / 'understat' / 'manifest.json').write_text(json.dumps({'files': {'EPL_2023': {
                'understat_league': 'EPL', 'file': 'EPL_2023.json',
                'file_sha256': hashlib.sha256(body).hexdigest()}}}))
            alias = cache / 'aliases.json'
            alias.write_text(json.dumps({'leagues': {'EPL': {'Manchester City': 'Man City'}}}))
            frame = uh.matches(cache, 'EPL', alias)
            self.assertEqual((len(frame), frame.home.iat[0], frame.understat_home.iat[0]),
                             (1, 'Man City', 'Manchester City'))  # unplayed match dropped
            self.assertEqual(uh.matches(cache, 'EPL', cache / 'none.json').home.iat[0], 'Manchester City')
            (cache / 'understat' / 'EPL_2023.json').write_bytes(body + b' ')
            with self.assertRaises(ValueError):
                uh.matches(cache, 'EPL', alias)  # file no longer matches its manifest sha256

    def test_league_without_understat_gets_no_xg(self):
        out, counts = uh.with_xg(fd([('2023-08-12', 'Ajax', 'PSV', 1, 0)]), REPO / '.football_cache', 'Eredivisie')
        self.assertTrue(out.HxG.isna().all())
        self.assertEqual(counts['league_without_understat'], 1)


@unittest.skipUnless((REPO / '.football_cache' / 'understat' / 'EPL_2023.json').exists(), 'Understat cache missing')
class HarnessCandidateTest(unittest.TestCase):
    """C3 on real EPL folds with the cached Understat xG."""

    @classmethod
    def setUpClass(cls):
        import historical_benchmark as hb
        data, _, _ = hb.load_history(REPO / '.football_cache', 'EPL',
                                     {**CFG, 'seasons': ['2122', '2223', '2324'], 'test_end_exclusive': '2024-07-01'})
        cls.origin = pd.Timestamp('2024-03-01')
        cls.data = data

    @staticmethod
    def fit(train, origin):
        from football_value_pipeline_v2_standalone import DixonColesModel
        return DixonColesModel(half_life_days=480., l2=.08, max_goals=10, shot_features=True,
                               bbs_statistics=False).fit(train.copy(), as_of=origin)

    def forecasts(self, data, xg_data, n=6):
        import narrow_margin as nm
        train = data[data.Date < self.origin]
        xg_train = xg_data[xg_data.Date < self.origin]
        model = self.fit(train, self.origin)
        return [eh.candidates(row, train, self.origin, model, CFG, nm.production_model(), xg_train)
                for _, row in data[data.Date >= self.origin].head(n).iterrows()]

    def test_c3_is_registered(self):
        self.assertIn('C3', eh.CANDIDATES)
        self.assertIn('understat_history.py', eh.SETUP_FILES)
        self.assertIn('understat_team_aliases.json', eh.SETUP_FILES)

    def test_every_team_maps_and_almost_every_match_gets_xg(self):
        xg_data, counts = uh.with_xg(self.data, REPO / '.football_cache', 'EPL')
        self.assertEqual(counts['score_mismatch'] + counts['ambiguous'], 0)
        self.assertEqual(counts['attached'], len(self.data))

    def test_c3_uses_xg_and_ignores_every_odds_field(self):
        xg_data, _ = uh.with_xg(self.data, REPO / '.football_cache', 'EPL')
        odds = [c for c in self.data.columns if c.startswith(ODDS_PREFIXES) and c not in ('AHh', 'AHCh')]
        self.assertGreater(len(odds), 20)
        shake = lambda frame: frame.assign(**{c: pd.to_numeric(frame[c], errors='coerce') * 1.02 + .01 for c in odds})
        first, second = self.forecasts(self.data, xg_data), self.forecasts(shake(self.data), shake(xg_data))
        self.assertTrue(any(e['c3_used_xg'] for _, _, e in first))
        self.assertTrue(any(not np.array_equal(m['C3'], m['C']) for m, _, _ in first))
        for (a, _, _), (b, _, _) in zip(first, second):
            np.testing.assert_array_equal(a['C3'], b['C3'])
            np.testing.assert_array_equal(a['C'], b['C'])
            self.assertFalse(np.array_equal(a['M'], b['M']))  # the market reference did move

    def test_only_xg_from_before_the_origin_reaches_c3(self):
        xg_data, _ = uh.with_xg(self.data, REPO / '.football_cache', 'EPL')
        later = xg_data.copy()
        after = later.Date >= self.origin
        later.loc[after, ['HxG', 'AxG']] = 9.
        base, moved = self.forecasts(self.data, xg_data), self.forecasts(self.data, later)
        for (a, _, _), (b, _, _) in zip(base, moved):
            np.testing.assert_array_equal(a['C3'], b['C3'])
        earlier = xg_data.copy()
        earlier.loc[(~after) & (earlier.Date >= self.origin - pd.Timedelta(days=60)), ['HxG', 'AxG']] = 3.
        self.assertTrue(any(not np.array_equal(a['C3'], b['C3'])
                            for (a, _, _), (b, _, _) in zip(base, self.forecasts(self.data, earlier))))

    def test_without_xg_c3_is_c(self):
        plain = self.data.assign(HxG=np.nan, AxG=np.nan)
        for m, _, extra in self.forecasts(self.data, plain, n=3):
            np.testing.assert_array_equal(m['C3'], m['C'])
            self.assertFalse(extra['c3_used_xg'])


if __name__ == '__main__':
    unittest.main()
