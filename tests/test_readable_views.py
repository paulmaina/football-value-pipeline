"""Readable league outputs: the research and cagey views, and the master's verdict on them (display only).

The agreement tests are the PR's check: for every fixture and every Pinnacle offer, the readable research and cagey
no-loss probabilities, gap, label and cagey tier equal those in the run's shortlist and master files
(scripts/readable_views_check.py). They run on a synthetic run built by the real lists, on the latest committed run
bundle and on one saved live run with every list rebuilt."""
from __future__ import annotations

import contextlib
import importlib.util
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest import mock

import numpy as np
import pandas as pd

from offline_test_case import OfflineQuotePolicyTestCase
import format_football_output as fo
import readable_views as rv
import readable_view_fixtures as fx

REPO = Path(__file__).resolve().parents[1]
# A saved live run whose rebuilt lists put fixtures on the master, the value shortlist and the cagey tier.
SAVED_RUN = 'fd052ff5e9f0163b'


def checker():
    spec = importlib.util.spec_from_file_location('readable_views_check', REPO / 'scripts' / 'readable_views_check.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def synthetic_rows():  # Home_0: research no-loss above the strong master's 0.70 gate (since 24 Nov 2026)
    return [fx.forecast(0, rates=(2.4, 0.6), h2h=(1.40, 4.9, 8.0), ou25=(1.80, 2.05),
                        ah=((-1.0, 1.85, 2.02), (0.5, 1.17, 5.2), (1.0, 1.08, 8.5))),
            fx.forecast(1, rates=(1.2, 1.3), h2h=(2.6, 3.3, 2.8), ou25=(2.10, 1.78), ah=((0.0, 1.95, 1.95),
                                                                                         (0.5, 1.48, 2.7))),
            fx.forecast(2, ou25=None),
            fx.forecast(3, kickoff=fx.LATER_KICKOFF, research=False)]


def format_bundle(raw: Path, out: Path) -> None:
    with contextlib.redirect_stdout(io.StringIO()):
        assert fo.main(['--root-dir', str(raw.parent / 'root'), '--input-dir', str(raw), '--output-dir', str(out)]) == 0


class SyntheticRunCase(OfflineQuotePolicyTestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        root = Path(cls.tmp.name)
        cls.raw, cls.out = root / 'raw', root / 'readable'
        import quote_policy
        with mock.patch.object(quote_policy, 'CONFIG', REPO / 'shortlist_quote_policy.json'):
            fx.bundle(cls.raw, synthetic_rows())
            format_bundle(cls.raw, cls.out)
        cls.csv = pd.read_csv(cls.out / 'EPL_predictions_readable.csv', dtype=str, keep_default_na=False,
                              encoding='utf-8-sig')
        cls.report = (cls.out / 'EPL_report.md').read_text(encoding='utf-8')
        cls.scores = pd.read_csv(cls.out / 'EPL_scorelines_readable.csv', dtype=str, keep_default_na=False,
                                 encoding='utf-8-sig')

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def fixture_row(self, i):
        return self.csv.loc[self.csv['Home team'].eq(f'Home_{i}')].iloc[0]


class AgreementTests(SyntheticRunCase):
    def test_every_offer_agrees_with_the_shortlist_and_master_files(self):
        result = checker().check_bundle(self.raw, self.out)
        self.assertEqual(result['problems'], [])
        counts = result['counts']
        for name in ('offers', 'master_rows', 'value_picks', 'cagey_picks', 'ah_lines_research', 'ah_lines_cagey',
                     'formatted_master_fixtures'):
            self.assertGreater(counts[name], 0, name)
        self.assertEqual(counts['fixtures'], 4)

    def test_the_check_catches_a_changed_master_figure(self):
        tool = checker()
        with tempfile.TemporaryDirectory() as tmp:
            import shutil
            raw = Path(tmp) / 'raw'
            shutil.copytree(self.raw, raw)
            master = pd.read_csv(raw / 'master_shortlist.csv')
            master.loc[0, 'cagey_no_loss_probability'] += 0.01
            master.loc[0, 'gap_check'] = 'agree' if master.loc[0, 'gap_check'] != 'agree' else 'research_too_optimistic'
            master.to_csv(raw / 'master_shortlist.csv', index=False)
            problems = tool.check_bundle(raw)['problems']
        self.assertTrue(any('cagey_no_loss_probability' in p for p in problems), problems)
        self.assertTrue(any('gap_check' in p for p in problems), problems)

    def test_latest_committed_run_bundle_agrees(self):
        raw = REPO / 'football_output_v2' / 'raw'
        if not (raw / 'current_run.json').exists():
            self.skipTest('no committed run bundle')
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / 'readable'
            format_bundle(raw, out)
            result = checker().check_bundle(raw, out)
        self.assertEqual(result['problems'], [])
        self.assertGreater(result['counts']['offers'], 0)


class SavedRunAgreementTests(OfflineQuotePolicyTestCase):
    def test_a_saved_live_run_with_every_list_rebuilt_agrees(self):
        tool = checker()
        with tempfile.TemporaryDirectory() as tmp:
            import quote_policy
            with mock.patch.object(quote_policy, 'CONFIG', REPO / 'shortlist_quote_policy.json'):
                report = tool.check_saved(Path(tmp), '2026-10-27', '2026-11-09', only=[SAVED_RUN])
        self.assertEqual(len(report['runs']), 1)
        self.assertEqual([p for r in report['runs'] for p in r['problems']], [])
        for name in ('master_rows', 'value_picks', 'cagey_picks', 'formatted_master_fixtures'):
            self.assertGreater(report['counts'][name], 0, name)


class ViewTests(SyntheticRunCase):
    def test_research_is_the_forecast_rows_own_and_the_rebuilt_grid_reproduces_it(self):
        row = fx.forecast(0, rates=(2.4, 0.6))
        view = rv.research_view(row)
        self.assertEqual(view['p_1x2'], [row['research_p_home'], row['research_p_draw'], row['research_p_away']])
        markets = rv.grid_markets(view['matrix'], view['p_1x2'])
        self.assertAlmostEqual(markets['over_1_5'], row['research_p_over_1_5'], places=12)
        tampered = json.loads(row['team_research_json'])
        tampered['margin_distribution']['0'] += 0.01
        self.assertEqual(rv.research_view({**row, 'team_research_json': json.dumps(tampered)})['reason'],
                         'rebuilt research grid does not reproduce the frozen forecast; not shown')
        self.assertEqual(rv.research_view(fx.forecast(3, research=False))['reason'], 'no research in this forecast')

    def test_live_versions_rebuild_with_their_own_grid_function(self):
        """v5 rebuilds on C6's grid with the fit frozen in the forecast, v6 on CE3n's; each must reproduce."""
        import research_ce3n as ce3n
        import research_low_score_sharpen as c6
        import team_research as tr
        rates = [1.7, 1.05]
        fit = c6.fit_for(pd.Timestamp(fx.CLOCK))
        self.assertIsNotNone(fit)
        for version, matrix, extra in ((tr.VERSION, c6.live_grid(rates, fit), {'c6_fit': fit}),
                                       (tr.CE3N_VERSION, ce3n.live_grid(rates), {})):
            with self.subTest(version=version):
                context = {'version': version, 'goal_rates': rates, 'warnings': [], **extra, **tr.grid_outputs(matrix)}
                row = {**tr.outcome_columns(context, 'research_p_'), 'research_version': version,
                       'team_research_json': json.dumps(context)}
                view = rv.research_view(row)
                np.testing.assert_array_equal(view['matrix'], matrix)
                self.assertEqual(fo.view_model_text('Research', {'research': view}, row),
                                 'research v5, C6' if version == tr.VERSION else 'research v6, CE3n')
        # v5 without its frozen fit is never rebuilt on another grid.
        context = {'version': tr.VERSION, 'goal_rates': rates, 'warnings': [],
                   **tr.grid_outputs(c6.live_grid(rates, fit))}
        row = {**tr.outcome_columns(context, 'research_p_'), 'team_research_json': json.dumps(context)}
        self.assertEqual(rv.research_view(row)['reason'], 'C6 fit not frozen in this forecast; research grid not rebuilt')

    def test_csv_shows_both_views_their_lean_and_whether_they_agree(self):
        first, second = self.fixture_row(0), self.fixture_row(1)
        self.assertEqual(first['Research model'], 'research team-form-research-v4')
        self.assertEqual(second['Cagey model'], 'cagey D_pow2 (fit B)')
        # Home_0's power fit fails its fit check, so the cagey tier priced it with D, flagged (cagey_basis).
        self.assertTrue(first['Cagey model'].startswith('cagey D (fit B); D_pow2 power grid failed its fit check'),
                        first['Cagey model'])
        self.assertTrue(first['Cagey model'].endswith('priced by D'))
        for view in ('Research', 'Cagey'):
            self.assertEqual(first[f'{view} lean'], 'Home_0 win')
            self.assertNotEqual(first[f'{view} home win'], '—')
        self.assertEqual(first['Views agree on the lean'], 'yes')
        self.assertEqual(second['Views agree on the lean'], 'no')
        no_totals = self.fixture_row(2)
        self.assertEqual(no_totals['Cagey model'],
                         'unavailable: no cagey grid: needs Pinnacle 1X2 and O/U 2.5 (no Pinnacle O/U 2.5 quote)')
        self.assertEqual(no_totals['Cagey home win'], '—')
        self.assertEqual(no_totals['Views agree on the lean'], 'one view missing')
        # A forecast saved without research: the value shortlist computes it at the run clock, and so does the view.
        self.assertTrue(self.fixture_row(3)['Research model'].endswith(
            '(forecast saved without research: computed at the run clock, as the value shortlist does)'))

    def test_cagey_over_1_5_is_the_tiers_own_uncorrected_figure(self):
        decisions = pd.read_csv(self.raw / 'conservative_bet_rejections.csv', low_memory=False)
        wanted = decisions.loc[decisions.home_team.eq('Home_0'), 'uncorrected_over_1_5_probability'].dropna()
        self.assertGreater(len(wanted), 0)
        self.assertEqual(self.fixture_row(0)['Cagey Over 1.5'], fo.pct(wanted.iloc[0]))

    def test_european_fixtures_use_d_and_the_fallback_matches_the_decision_rows(self):
        run = rv.Run(self.raw)
        ucl = {**fx.forecast(1, rates=(1.2, 1.3), h2h=(2.6, 3.3, 2.8), ou25=(2.10, 1.78), ah=((0.0, 1.95, 1.95),)),
               'league': 'UEFA Champions League'}
        view = rv.cagey_view(ucl, run.clock, run.cagey)
        self.assertEqual((view['correction'], view['fallback']), ('D', None))
        decisions = pd.read_csv(self.raw / 'conservative_bet_rejections.csv', low_memory=False)
        home_0 = decisions.loc[decisions.home_team.eq('Home_0') & decisions.cagey_correction.notna()]
        self.assertEqual(set(home_0.cagey_correction), {'D'})
        self.assertEqual(set(home_0.cagey_correction_fallback),
                         {rv.cagey_view(fx.forecast(0, rates=(2.4, 0.6), h2h=(1.40, 4.9, 8.0), ou25=(1.80, 2.05),
                                                    ah=((-1.0, 1.85, 2.02), (0.5, 1.17, 5.2), (1.0, 1.08, 8.5))),
                                        run.clock, run.cagey)['fallback']})

    def test_production_model_is_a_labelled_benchmark_at_the_end(self):
        columns = list(self.csv.columns)
        first_benchmark = min(i for i, c in enumerate(columns) if c.startswith('Benchmark '))
        self.assertTrue(all(c.startswith('Benchmark ') for c in columns[first_benchmark:]))
        self.assertIn('Benchmark best EV (display only)', columns)
        self.assertNotIn('Best model-estimated value', columns)
        self.assertNotIn('Model EV', self.report)
        heading = f'## {rv.BENCHMARK}'
        self.assertEqual(self.report.count(heading), 1)
        self.assertGreater(self.report.index(heading), self.report.rindex("### The master's verdict on every"))
        self.assertIn('Benchmark EV (display only)', self.report)

    def test_report_lists_every_pinnacle_offer_with_the_masters_verdict(self):
        run = rv.Run(self.raw)
        offers = sum(len(v) for v in run.offers().values())
        table = self.report.split("### The master's verdict on every Pinnacle offer")
        self.assertEqual(len(table), 5)  # one per fixture
        rows = [line for part in table[1:] for line in part.split('###')[0].splitlines()
                if line.startswith('| ') and not line.startswith('| Offer') and not line.startswith('| ---')]
        self.assertEqual(len(rows), offers)
        # Before the benchmark section, "blend" appears only to say nothing is blended and to name the benchmark.
        views = self.report.split(f'## {rv.BENCHMARK}')[0]
        for phrase in ('No probability here is blended', 'No probability is blended', '(70% Pinnacle blend)'):
            views = views.replace(phrase, '')
        self.assertNotIn('blend', views.lower())
        self.assertNotIn('Benchmark', views)

    def test_lists_and_master_rank_per_fixture(self):
        master = pd.read_csv(self.raw / 'master_shortlist.csv')
        ranked = master.loc[master.new_master_decision.eq('SHORTLISTED')].sort_values('new_master_rank')
        top = ranked.iloc[0]
        row = self.fixture_row(int(top.home_team.split('_')[1]))
        self.assertTrue(row['On master'].startswith(f"yes: rank 1 ({top.new_master_tier}), {top.market_to_bet}"))
        self.assertTrue(row['Best offer basis'].startswith('master pick (rank 1'))
        value = pd.read_csv(self.raw / 'conservative_bet_shortlist.csv')
        for home in value.home_team:
            self.assertTrue(self.fixture_row(int(home.split('_')[1]))['On value shortlist'].startswith('yes: '))
        later = self.fixture_row(3)
        self.assertEqual(later['On master'], 'no')
        self.assertEqual(later['On value shortlist'], 'no')

    def test_scorelines_rank_each_model_with_research_and_cagey_first(self):
        first = self.scores.loc[self.scores['Home team'].eq('Home_0')]
        self.assertEqual(list(dict.fromkeys(first['Model'])), ['Research', 'Cagey', rv.BENCHMARK])
        research = first.loc[first['Model'].eq('Research')]
        self.assertEqual(research['Rank'].astype(int).tolist(), list(range(1, len(research) + 1)))
        probabilities = research['Probability (decimal)'].astype(float)
        self.assertTrue((np.diff(probabilities.to_numpy()) <= 0).all())
        self.assertGreaterEqual(probabilities.min(), rv.SCORELINE_MIN)
        view = rv.research_view(fx.forecast(0, rates=(2.4, 0.6)))
        i, j = map(int, research.iloc[0]['Score'].split('-'))
        self.assertAlmostEqual(probabilities.iloc[0], view['matrix'][i, j], places=12)
        no_cagey = self.scores.loc[self.scores['Home team'].eq('Home_2'), 'Model']
        self.assertNotIn('Cagey', set(no_cagey))

    def test_without_decision_rows_the_verdict_columns_say_why(self):
        frame = fo.readable_predictions_frame(pd.DataFrame([fx.forecast(0)]), {})
        self.assertEqual(frame.loc[0, 'Best offer note'], rv.MISSING_DECISIONS)
        self.assertEqual(frame.loc[0, 'On master'], 'master list not in this run bundle')
        self.assertEqual(frame.loc[0, 'Cagey model'], 'unavailable: no cagey grid: run clock not recorded in this '
                                                      'bundle')


class WorkbookLeagueTabTests(SyntheticRunCase):
    def test_league_tab_shows_both_views_the_verdict_and_the_benchmark_last(self):
        import excel_book as xb
        import predictions_workbook as pw
        from test_league_predictions_workbook import table
        book = xb.read_workbook(self.out / 'league_predictions.xlsx')
        headers, rows = table(book, 'EPL')
        self.assertEqual(headers, pw.LEAGUE_COLUMNS)
        self.assertEqual(headers[-3:], ['Benchmark home win', 'Benchmark draw', 'Benchmark away win'])
        by_match = {r['Match']: r for r in rows}
        first = by_match['Home_0 v Away_0']
        self.assertAlmostEqual(first['Research home win'], xb.number(self.fixture_row(0)['Research home win']))
        self.assertAlmostEqual(first['Cagey home win'], xb.number(self.fixture_row(0)['Cagey home win']))
        self.assertEqual(by_match['Home_2 v Away_2']['Cagey home win'], 'no cagey view')
        self.assertTrue(by_match['Home_2 v Away_2']['Cagey lean'].startswith('unavailable: no cagey grid'))
        for row in rows:
            for header in headers:
                self.assertNotIn(row[header], (None, ''), header)


if __name__ == '__main__':
    unittest.main()
