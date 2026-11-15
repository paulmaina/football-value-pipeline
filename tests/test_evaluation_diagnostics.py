"""Standing harness diagnostics: baselines, quote references, information test, segments and odds bands."""
import json
from pathlib import Path
import tempfile
import unittest
from unittest import mock

import numpy as np
import pandas as pd

import evaluation_diagnostics as ed
import evaluation_harness as eh

LEAGUES = ('EPL', 'Eredivisie')
OUTCOMES = ('p_home', 'p_draw', 'p_away')


def flatten(probs, t):
    powered = np.asarray(probs, float) ** t
    return powered / powered.sum(axis=-1, keepdims=True)


def synthetic(counts=(('development', 600), ('validation', 240), ('retrospective', 120)), seed=3,
              research_informed=False, missing=()):
    """A locked run's three frames. M is the truth flattened (t = 0.8); the research views are pure noise
    unless `research_informed`, when market and research each see the truth with independent errors."""
    rng = np.random.default_rng(seed)
    scores, forecasts, fixtures = [], [], []
    starts = {'development': '2023-08-05', 'validation': '2025-08-02', 'retrospective': '2026-02-07'}
    for phase, n in counts:
        dates = pd.Timestamp(starts[phase]) + pd.to_timedelta(np.arange(n) // 6 * 7, unit='D')
        for i in range(n):
            share, draw = rng.uniform(.12, .88), rng.uniform(.2, .3)
            truth = np.array([(1 - draw) * share, draw, (1 - draw) * (1 - share)])
            outcome = int(rng.choice(3, p=truth))
            market = flatten(truth, .8)
            noise = flatten(rng.uniform(.8, 1.25, 3), 1.)  # no outcome carries a level: pure noise
            research = noise
            if research_informed:  # both views see the truth through their own independent error
                market = flatten(truth * rng.uniform(.75, 1.33, 3), .8)
                research = flatten(truth * rng.uniform(.8, 1.25, 3), 1.)
            date = dates[i]
            league = LEAGUES[i % 2]
            key = f'{league}|{date.date()}|H{i}|A{i}'
            week = f'{date.isocalendar().year}-W{date.isocalendar().week:02d}'
            views = {c: research for c in ('C', 'C2', 'C3', 'C5', 'C6', 'C0', 'DC')} | {'M': market, 'D': market, 'A': market}
            margin = 1.03
            odds = 1 / (market * margin)
            if phase != 'retrospective':
                views |= {'QPROP': market, 'QPOW': flatten(market, 1.02)}
            for cand, probs in views.items():
                if (cand, i) in missing:
                    continue
                forecasts.append({'phase': phase, 'league': league, 'fixture_key': key, 'candidate': cand,
                                  'outcome': outcome, **dict(zip(OUTCOMES, probs))})
                for group in ed.GROUPS if cand not in ed.QUOTES else ('1X2',):
                    loss = -np.log(probs[outcome]) * (1. if group == '1X2' else .75)
                    scores.append({'fixture_key': key, 'league': league, 'week': week, 'phase': phase,
                                   'candidate': cand, 'group': group, 'log_loss': float(loss)})
            pinnacle = odds if phase != 'retrospective' else (np.nan,) * 3
            fixtures.append({'fixture_key': key, 'phase': phase, 'league': league, 'date': str(date.date()),
                             'week': week, 'home_training_matches': 10 if i % 5 == 0 else 60,
                             'away_training_matches': 80, 'pinnacle_home': pinnacle[0],
                             'pinnacle_draw': pinnacle[1], 'pinnacle_away': pinnacle[2]})
    return pd.DataFrame(scores), pd.DataFrame(forecasts), pd.DataFrame(fixtures, columns=ed.FIXTURE_COLUMNS)


class FitTest(unittest.TestCase):
    def setUp(self):
        rng = np.random.default_rng(11)
        share, draw = rng.uniform(.1, .9, 20000), rng.uniform(.2, .3, 20000)
        self.truth = np.column_stack([(1 - draw) * share, draw, (1 - draw) * (1 - share)])
        self.outcome = np.array([rng.choice(3, p=p) for p in self.truth])
        self.noise = flatten(rng.uniform(.5, 2., (20000, 3)), 1.)

    def frame(self, probs):
        return pd.DataFrame(probs, columns=list(OUTCOMES)).assign(outcome=self.outcome)

    def test_exponents_are_recovered(self):
        # The market is the truth flattened by 0.8, so the truth is M^1.25: a = 1.25 and noise adds nothing.
        market = flatten(self.truth, .8)
        theta = ed.fit_powers(ed._logs(self.frame(market), self.frame(self.noise)), self.outcome)
        self.assertAlmostEqual(theta[0], 1.25, delta=.04)
        self.assertAlmostEqual(theta[1], 0., delta=.03)
        # Truth = M^0.5 * R^0.5 exactly when M and R are the truth's two halves.
        half = flatten(self.truth * self.noise, 1.), flatten(self.truth / self.noise, 1.)
        theta = ed.fit_powers(ed._logs(self.frame(half[0]), self.frame(half[1])), self.outcome)
        np.testing.assert_allclose(theta, [.5, .5], atol=.03)

    def test_fitted_exponents_minimise_the_log_loss(self):
        logs = ed._logs(self.frame(flatten(self.truth, .8)), self.frame(self.noise))
        theta = ed.fit_powers(logs, self.outcome)
        best = ed.power_log_loss(logs, self.outcome, theta).mean()
        for shift in ([.02, 0.], [-.02, 0.], [0., .02], [0., -.02]):
            self.assertGreater(ed.power_log_loss(logs, self.outcome, theta + np.array(shift)).mean(), best)
        self.assertAlmostEqual(ed.power_log_loss(logs, self.outcome, [1., 0.]).mean(),
                               float(-np.log(flatten(self.truth, .8)[np.arange(20000), self.outcome]).mean()))

    def test_weights_count_matches(self):
        logs = ed._logs(self.frame(flatten(self.truth, .8)), self.frame(self.noise))[:400]
        outcome = self.outcome[:400]
        weights = np.r_[np.full(200, 2.), np.ones(200)]
        doubled = ed.fit_powers(np.concatenate([logs[:200], logs]), np.r_[outcome[:200], outcome])
        np.testing.assert_allclose(ed.fit_powers(logs, outcome, weights), doubled, atol=1e-8)

    def test_collinear_forecasts_have_no_fit(self):
        logs = ed._logs(self.frame(self.truth), self.frame(self.truth))
        self.assertIsNone(ed.fit_powers(logs, self.outcome))
        with mock.patch.object(ed, 'SAMPLES', 20):
            self.assertIsNone(ed.week_bootstrap_fits(logs[:60], self.outcome[:60], np.arange(60) // 6, [1., 0.]))
            self.assertIsNone(ed.week_bootstrap_fits(logs[:60], self.outcome[:60], np.zeros(60), [1., 0.]))

    def test_sharpness_is_the_inverse_of_the_flattening(self):
        self.assertAlmostEqual(ed.sharpness(self.frame(flatten(self.truth, .75))), 1 / .75, delta=.04)
        self.assertAlmostEqual(ed.sharpness(self.frame(self.truth)), 1., delta=.03)
        self.assertIsNone(ed.sharpness(self.frame(self.truth).iloc[:1]))


class HelperTest(unittest.TestCase):
    def test_week_mean_matches_the_harness_pairing(self):
        rng = np.random.default_rng(2)
        rows = [{'fixture_key': f'f{i}', 'week': f'w{i % 9}', 'candidate': c, 'log_loss': float(v)}
                for i in range(90) for c, v in (('C', 1 + rng.normal(0, .2)), ('M', .95 + rng.normal(0, .2)))]
        frame = pd.DataFrame(rows)
        table = frame.pivot(index='fixture_key', columns='candidate', values='log_loss')
        weeks = frame.drop_duplicates('fixture_key').set_index('fixture_key').week.reindex(table.index)
        mine, theirs = ed.week_mean(table['C'] - table['M'], weeks), eh.paired(frame, 'C', 'M')
        self.assertAlmostEqual(mine['mean'], theirs['mean_gain'])
        np.testing.assert_allclose(mine['interval_95'], theirs['interval_95'])
        self.assertEqual((mine['n'], mine['weeks']), (90, 9))
        self.assertEqual(ed.week_mean([], []), {'n': 0, 'weeks': 0, 'mean': None, 'interval_95': None})
        self.assertIsNone(ed.week_mean([1., 2.], ['w', 'w'])['interval_95'])

    def test_odds_bands_are_the_declared_ones(self):
        self.assertEqual(ed.ODDS_BANDS, (1.3, 1.6, 2.0, 2.6, 3.5, 5.0))
        cases = [(1.05, 'up to 1.30'), (1.3, 'up to 1.30'), (1.31, '1.30-1.60'), (2.0, '1.60-2.00'),
                 (2.01, '2.00-2.60'), (3.5, '2.60-3.50'), (5.0, '3.50-5.00'), (5.01, 'above 5.00'), (41., 'above 5.00')]
        for odds, band in cases:
            self.assertEqual(ed.odds_band(odds), band, odds)
        self.assertEqual(len(ed.BAND_ORDER), 7)
        self.assertEqual({ed.odds_band(o) for o, _ in cases}, set(ed.BAND_ORDER))

    def test_favourite_bands_and_segment_definitions_are_the_declared_ones(self):
        cases = [(.34, 'under 45%'), (.4499, 'under 45%'), (.45, '45-60%'), (.5999, '45-60%'), (.6, '60-75%'),
                 (.75, '75%+'), (.97, '75%+')]
        for p, band in cases:
            self.assertEqual(ed.favourite_band(p), band, p)
        self.assertEqual((ed.MIN_TRAINING_MATCHES, ed.EARLY_SEASON_MONTHS), (16, (8, 9)))
        self.assertEqual((ed.INFORMATION, ed.SEGMENT_GROUPS), (('C', 'C6', 'C0'), ('1X2', 'AH all')))

    def test_fixture_rows_come_from_the_research_models_calibration_row(self):
        calib = [{'phase': 'development', 'league': 'EPL', 'fixture_key': 'k1', 'candidate': 'C', 'probs': [.5, .3, .2],
                  'outcome': 0, 'fixture': {'date': '2024-08-17', 'week': '2024-W33', 'home_training_matches': 12,
                                            'away_training_matches': 90, 'pinnacle_hda': [2.1, 3.4, 3.6]}},
                 {'phase': 'development', 'league': 'EPL', 'fixture_key': 'k1', 'candidate': 'M', 'probs': [.5, .3, .2],
                  'outcome': 0},
                 {'phase': 'retrospective', 'league': 'EPL', 'fixture_key': 'k2', 'candidate': 'C', 'probs': [.5, .3, .2],
                  'outcome': 2, 'fixture': {'date': '2026-02-01', 'week': '2026-W05', 'home_training_matches': 50,
                                            'away_training_matches': 60}}]
        frame = ed.fixture_frame(calib)
        self.assertEqual(list(frame.columns), ed.FIXTURE_COLUMNS)
        self.assertEqual(list(frame.fixture_key), ['k1', 'k2'])
        self.assertEqual(frame.loc[0, ['pinnacle_home', 'pinnacle_draw', 'pinnacle_away']].tolist(), [2.1, 3.4, 3.6])
        self.assertTrue(frame.loc[1, ['pinnacle_home', 'pinnacle_draw', 'pinnacle_away']].isna().all())
        self.assertEqual(list(ed.fixture_frame([]).columns), ed.FIXTURE_COLUMNS)


class ReportTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.frames = synthetic()
        with mock.patch.object(ed, 'SAMPLES', 200):
            cls.report = ed.report(*cls.frames)

    def test_cohort_needs_every_candidate(self):
        self.assertEqual(self.report['cohort'], {'development': 600, 'validation': 240, 'retrospective': 120})
        scores, forecasts, fixtures = synthetic(counts=(('development', 60),), missing={('C0', 0), ('A', 1)})
        self.assertEqual(len(ed.cohort(scores)), 58)
        with self.assertRaisesRegex(ValueError, 'no scores for DC'):
            ed.cohort(scores.loc[scores.candidate != 'DC'])

    def test_holdout_rows_abort_the_report(self):
        scores, forecasts, fixtures = synthetic(counts=(('development', 30),))
        for index in range(3):
            frames = [scores.copy(), forecasts.copy(), fixtures.copy()]
            frames[index].loc[frames[index].index[0], 'phase'] = 'holdout'
            with self.assertRaisesRegex(ValueError, 'Holdout rows'):
                ed.report(*frames)

    def test_baselines_are_cohort_means_with_paired_differences(self):
        scores, _, _ = self.frames
        dev = scores[(scores.phase == 'development') & (scores.group == '1X2')]
        entry = self.report['baselines']['development']
        self.assertEqual(entry['fixtures'], 600)
        for cand in ed.BASELINE_TABLE:
            self.assertAlmostEqual(entry['1X2']['mean_log_loss'][cand], dev[dev.candidate == cand].log_loss.mean())
        gap = entry['1X2']['differences']['C_minus_M']
        self.assertAlmostEqual(gap['mean'], entry['1X2']['mean_log_loss']['C'] - entry['1X2']['mean_log_loss']['M'])
        self.assertGreater(gap['interval_95'][0], 0)  # noise is clearly behind the market
        self.assertEqual(entry['1X2']['differences']['C_minus_C0']['mean'], 0.)
        self.assertEqual(set(self.report['baselines']), {p for p, _ in ed.PERIODS})
        self.assertEqual(self.report['baselines']['validation+retrospective']['fixtures'], 360)
        self.assertEqual(set(entry) - {'fixtures'}, set(ed.GROUPS))

    def test_quote_references_cover_pinnacle_periods_only(self):
        quotes = self.report['quote_references']
        self.assertEqual(set(quotes), set(ed.PINNACLE_PERIODS))
        self.assertEqual(quotes['development+validation']['fixtures'], 840)
        self.assertEqual(quotes['development']['differences']['QPROP_minus_M']['mean'], 0.)
        self.assertEqual(set(quotes['development']['mean_log_loss']), {'QPROP', 'QPOW', 'M'})
        scores, forecasts, fixtures = self.frames
        self.assertEqual(ed.quote_references(scores[~scores.candidate.isin(ed.QUOTES)], ed.cohort(scores)), {})

    def test_noise_fails_the_information_test_and_informed_research_passes(self):
        info = self.report['information_test']
        self.assertEqual(set(info), set(ed.INFORMATION))
        dev = info['C']['by_period']['development']
        self.assertAlmostEqual(dev['a'], 1.25, delta=.2)  # M is the truth flattened by 0.8
        self.assertLess(dev['b_interval_95'][0], 0)
        self.assertFalse(dev['b_positive_and_clear_of_zero'])
        self.assertFalse(info['C']['passes'])
        self.assertEqual(set(info['C']['by_period']), {p for p, _ in ed.PERIODS})
        later = info['C']['with_development_weights']
        self.assertEqual(set(later), set(ed.INFORMATION_LATER_PERIODS))
        gains = later['validation']
        self.assertAlmostEqual(gains['gain_over_M']['mean'], gains['market_only_gain_over_M']['mean']
                               + gains['research_gain_beyond_market_only']['mean'])
        self.assertGreater(gains['market_only_gain_over_M']['mean'], 0)  # sharpening a flat market helps
        self.assertEqual(info['C']['development_weights']['a'], dev['a'])
        with mock.patch.object(ed, 'SAMPLES', 200):
            frames = synthetic(research_informed=True)
            informed = ed.information_test(frames[1], ed.cohort(frames[0]))
        self.assertTrue(informed['C0']['passes'])
        self.assertGreater(informed['C0']['by_period']['development']['b_interval_95'][0], 0)
        self.assertGreater(informed['C0']['with_development_weights']['validation']
                           ['research_gain_beyond_market_only']['mean'], 0)

    def test_segments_partition_the_cohort(self):
        _, forecasts, fixtures = self.frames
        for phase, n in (('development', 600), ('validation', 240), ('retrospective', 120)):
            entry = self.report['segments'][phase]
            self.assertEqual(entry['all']['fixtures'], n)
            for dimension in ('training matches', 'month', 'favourite market probability', 'league'):
                self.assertEqual(sum(r['fixtures'] for r in entry[dimension]), n, (phase, dimension))
            self.assertEqual([r['segment'] for r in entry['training matches']],
                             ['either team under 16', 'both teams 16 or more'])
            self.assertEqual(entry['training matches'][0]['fixtures'], n // 5)
            self.assertEqual([r['segment'] for r in entry['favourite market probability']],
                             ['under 45%', '45-60%', '60-75%', '75%+'])
            self.assertEqual([r['segment'] for r in entry['league']], sorted(LEAGUES))
            for row in entry['league']:
                self.assertEqual(set(row['sharpness']), {*ed.SEGMENT_CANDIDATES, 'M'})
                self.assertAlmostEqual(row['sharpness']['M'], 1.25, delta=.45)
            self.assertEqual(set(entry['all']['gap_to_M']), set(ed.SEGMENT_CANDIDATES))
            self.assertEqual(set(entry['all']['gap_to_M']['C']), set(ed.SEGMENT_GROUPS))
        dev = self.report['segments']['development']
        months = pd.to_datetime(fixtures[fixtures.phase == 'development'].date).dt.month
        self.assertEqual(dev['month'][0]['fixtures'], int(months.isin([8, 9]).sum()))
        market = forecasts[(forecasts.candidate == 'M') & (forecasts.phase == 'development')]
        self.assertEqual(dev['favourite market probability'][3]['fixtures'],
                         int((market[['p_home', 'p_away']].max(axis=1) >= .75).sum()))
        self.assertGreater(dev['all']['gap_to_M']['C']['1X2']['mean'], 0)
        with self.assertRaisesRegex(ValueError, 'no diagnostic fixture row'):
            ed.segments(self.frames[0], forecasts, fixtures.iloc[1:], ed.cohort(self.frames[0]))

    def test_odds_bands_back_every_pinnacle_quote_once(self):
        bands = self.report['odds_bands']
        self.assertEqual(set(bands), set(ed.PINNACLE_PERIODS))
        dev = bands['development']
        self.assertEqual(dev['fixtures'], 600)
        rows = {r['band']: r for r in dev['every_quote']}
        self.assertEqual(list(rows), [*ed.BAND_ORDER, 'all'])
        self.assertEqual(rows['all']['bets'], 1800)
        self.assertEqual(sum(r['bets'] for band, r in rows.items() if band != 'all'), 1800)
        _, forecasts, fixtures = self.frames
        bets = ed.quote_bets(forecasts, fixtures, ed.cohort(self.frames[0]))
        self.assertEqual(len(bets), 3 * 840)  # no Pinnacle quote in the retrospective period
        first = bets[bets.fixture_key == bets.fixture_key.iloc[0]]
        self.assertEqual(int(first.won.sum()), 1)
        self.assertAlmostEqual(first.loc[first.won, 'return'].item(), first.loc[first.won, 'odds'].item() - 1)
        self.assertEqual(set(first.loc[~first.won, 'return']), {-1.})
        self.assertAlmostEqual(rows['all']['return_per_bet'], bets.loc[bets.phase == 'development', 'return'].mean())
        picks = dev['positive_expected_return_quotes']
        self.assertEqual(set(picks), set(ed.VALUE_PICK_CANDIDATES))
        chosen = bets[(bets.phase == 'development') & (bets.p_C * bets.odds > 1)]
        self.assertEqual(next(r for r in picks['C'] if r['band'] == 'all')['bets'], len(chosen))
        self.assertEqual(ed.odds_bands(forecasts, fixtures.assign(pinnacle_home=np.nan), ed.cohort(self.frames[0])), {})

    def test_a_combined_period_needs_both_its_phases(self):
        scores, forecasts, fixtures = synthetic(counts=(('development', 60), ('validation', 30)))
        with mock.patch.object(ed, 'SAMPLES', 50):
            report = ed.report(scores, forecasts, fixtures)
        self.assertEqual(set(report['baselines']), {'development', 'validation', 'development+validation'})
        self.assertEqual(set(report['segments']), {'development', 'validation'})
        self.assertEqual(set(report['information_test']['C']['with_development_weights']), {'validation'})

    def test_the_readable_copy_has_every_section(self):
        text = ed.markdown({**self.report, 'source_commit': 'abc123'})
        for heading in ('## 1. Research baselines', '## 2. Quote references', '## 3. Information test',
                        '## 4. Segments: gap to M', '## 5. Flat-stake return at Pinnacle 1X2 prices by odds band',
                        'Verdict (development): C does not pass', 'abc123', 'either team under 16',
                        'August-September', '75%+', 'above 5.00'):
            self.assertIn(heading, text)
        self.assertNotIn('nan', text)


class RunFilesTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.run = Path(self.tmp.name) / 'run'
        self.run.mkdir()
        scores, forecasts, fixtures = synthetic(counts=(('development', 90), ('validation', 48)))
        scores.to_csv(self.run / 'fixture_scores.csv', index=False)
        forecasts.to_csv(self.run / 'forecasts_1x2.csv', index=False)
        fixtures.to_csv(self.run / 'diagnostic_fixtures.csv', index=False)

    def results(self, mode):
        (self.run / 'results.json').write_text(json.dumps({'mode': mode, 'source_commit': 'c0ffee',
                                                           'version': 'evaluation-harness-v2',
                                                           'config_sha256': 'f' * 64}), encoding='utf-8')

    def test_the_report_is_rebuilt_from_a_runs_files(self):
        self.results('historical')
        out = Path(self.tmp.name) / 'out'
        with mock.patch.object(ed, 'SAMPLES', 50), mock.patch('builtins.print'):
            self.assertEqual(ed.main(['--run', str(self.run), '--output', str(out)]), 0)
            again = ed.from_run(self.run)
        saved = json.loads((out / 'summary.json').read_text(encoding='utf-8'))
        self.assertEqual((saved['source_commit'], saved['harness_version']), ('c0ffee', 'evaluation-harness-v2'))
        self.assertEqual({k: v for k, v in saved.items() if k in again}, json.loads(json.dumps(again)))
        self.assertIn('# Evaluation harness diagnostics', (out / 'report.md').read_text(encoding='utf-8'))
        self.assertNotIn(b'\r\n', (out / 'summary.json').read_bytes())

    def test_only_locked_historical_runs_are_read(self):
        self.results('holdout')
        with self.assertRaisesRegex(ValueError, 'locked historical run'):
            ed.main(['--run', str(self.run), '--output', str(Path(self.tmp.name) / 'out')])


if __name__ == '__main__':
    unittest.main()
