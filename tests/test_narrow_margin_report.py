"""Narrow-margin report: one resolved run, the forecast roster as base, figures from the corrected matrix."""

from offline_test_case import OfflineQuotePolicyTestCase
import json
import shutil
import tempfile
import unittest
from pathlib import Path

import pandas as pd

import narrow_margin as nm
import narrow_margin_report as report
import price_edge_cagey_shortlist as v28
import price_edge_shortlist as v27
from prediction_runs import publish_run

RUN = '2026-11-03T13:58:00+00:00'
QUOTED = '2026-11-03T13:57:00Z'
MODEL = nm.versions()['production']['version']


def forecast(home, away, league, h2h, ou, ah_line, ah_prices, kickoff='2026-11-04T20:00:00+00:00'):
    """A forecast row whose Pinnacle quotes reach the fit the way the pipeline reads them."""
    return {'league': league, 'home_team': home, 'away_team': away, 'kickoff_utc': kickoff,
            'market_source_1x2': 'The Odds API / Pinnacle', 'market_reference_home_odds': h2h[0],
            'market_reference_draw_odds': h2h[1], 'market_reference_away_odds': h2h[2],
            'market_reference_1x2_last_update_utc': QUOTED,
            'market_source_ou25': 'The Odds API / Pinnacle', 'market_reference_over_2_5_odds': ou[0],
            'market_reference_under_2_5_odds': ou[1], 'market_reference_over_2_5_last_update_utc': QUOTED,
            'asian_handicap_offers': json.dumps([{'bookmaker': 'Pinnacle', 'side': 'home', 'line': ah_line,
                                                  'price': ah_prices[0], 'opposite_price': ah_prices[1],
                                                  'market_key': 'spreads', 'last_update_utc': QUOTED}])}


ROSTER = [forecast('A', 'B', 'UEFA Champions League', (1.93, 3.89, 3.88), (1.75, 2.14), -0.5, (2.04, 1.86)),
          forecast('C', 'D', 'Serie A', (2.60, 3.10, 2.90), (2.10, 1.76), 0.0, (1.94, 1.96)),
          forecast('E', 'F', 'Premier League', (1.50, 4.50, 6.50), (1.60, 2.40), -1.0, (1.95, 1.95),
                   kickoff='2026-11-06T20:00:00+00:00')]


def expected(row):
    """What the run itself computes for this row."""
    pin = v27.pinnacle_quotes(row)
    fit, info = v27.market_fit(pin, pd.Timestamp(RUN))
    return v28.corrected_context(pin, fit, info, nm.load(MODEL))


def monitoring(rows=ROSTER[:2], unusable=ROSTER[2:]):
    out = []
    for row in rows:
        context = expected(row)
        out.append({'league': row['league'], 'home_team': row['home_team'], 'away_team': row['away_team'],
                    'kickoff_utc': row['kickoff_utc'], 'generated_at_utc': RUN, 'model_version': MODEL,
                    'status': 'USABLE', 'exclusion_reason': '', 'fit': context['fit'], 'latest_input_quote_utc': QUOTED,
                    'corrected_p2': context['score'],
                    'corrected_p3': nm.margin_tail(context['margins'], context['probs'], 3),
                    'uncorrected_p2': nm.margin_tail(context['margins'], context['uncorrected_probs'], 2),
                    'corrected_cagey_quintile': 'Q3'})
    for row in unusable:
        out.append({'league': row['league'], 'home_team': row['home_team'], 'away_team': row['away_team'],
                    'kickoff_utc': row['kickoff_utc'], 'generated_at_utc': RUN, 'model_version': MODEL,
                    'status': 'UNUSABLE', 'exclusion_reason': 'no usable market-implied fit (missing input: over_2_5)'})
    return pd.DataFrame(out, columns=['league', 'home_team', 'away_team', 'kickoff_utc', 'generated_at_utc',
                                      'model_version', 'status', 'exclusion_reason', 'fit', 'latest_input_quote_utc',
                                      'corrected_p2', 'corrected_p3', 'uncorrected_p2', 'corrected_cagey_quintile'])


class NarrowMarginReportTests(OfflineQuotePolicyTestCase):
    def setUp(self):
        super().setUp()
        self.directory = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.directory, ignore_errors=True)

    def plain(self, roster=ROSTER, monitor=None, write_monitoring=True):
        """A raw directory with no current-run pointer (historical layout)."""
        raw = Path(tempfile.mkdtemp(dir=self.directory))
        pd.DataFrame(roster).to_csv(raw / report.PREDICTIONS, index=False)
        if write_monitoring:
            (monitoring() if monitor is None else monitor).to_csv(raw / report.MONITORING, index=False)
        return raw

    def published(self):
        """A genuine published bundle behind the current-run pointer."""
        raw, staging = self.directory / 'raw', self.directory / 'staging'
        raw.mkdir()
        staging.mkdir()
        pd.DataFrame(ROSTER).to_csv(staging / report.PREDICTIONS, index=False)
        monitoring().to_csv(staging / report.MONITORING, index=False)
        (staging / 'conservative_bet_summary.json').write_text(json.dumps({'generated_at_utc': RUN}),
                                                                encoding='utf-8')
        (staging / 'conservative_bet_shortlist.csv').write_text('fixture_id\n', encoding='utf-8')
        (staging / 'pipeline_run_metadata.json').write_text(json.dumps({'generated_at_utc': RUN}), encoding='utf-8')
        bundle = publish_run(staging, raw)
        return raw, bundle

    def test_draw_and_one_goal_come_from_the_corrected_matrix(self):
        frame = report.build(self.plain())
        a = frame[frame.home_team == 'A'].iloc[0]
        context = expected(ROSTER[0])
        draw = float(context['probs'][context['margins'] == 0].sum())
        self.assertAlmostEqual(a.p_draw, draw, places=12)
        self.assertAlmostEqual(a.p_narrow, 1 - context['score'], places=12)
        self.assertAlmostEqual(a.p_draw + a.p_one_goal + a.p_two_plus, 1.0, places=12)
        # Not the rescaled market draw, which the correction does not preserve.
        novig = (1 / 3.89) / (1 / 1.93 + 1 / 3.89 + 1 / 3.88)
        rescaled = novig * (1 - context['score']) / (1 - nm.margin_tail(context['margins'],
                                                                        context['uncorrected_probs'], 2))
        self.assertNotAlmostEqual(a.p_draw, rescaled, places=6)

    def test_shows_the_quotes_that_fed_the_fit(self):
        a = report.build(self.plain()).set_index('home_team').loc['A']
        self.assertEqual((a.pinnacle_home_odds, a.pinnacle_draw_odds, a.pinnacle_away_odds), (1.93, 3.89, 3.88))
        self.assertEqual((a.pinnacle_over_2_5_odds, a.pinnacle_under_2_5_odds), (1.75, 2.14))
        self.assertEqual((a.pinnacle_ah_main_line, a.pinnacle_ah_home_odds, a.pinnacle_ah_away_odds),
                         (-0.5, 2.04, 1.86))

    def test_reads_the_current_bundle_not_out_of_sync_compatibility_copies(self):
        raw, bundle = self.published()
        # An interrupted publish leaves a compatibility copy that disagrees with the active bundle.
        stale = monitoring()
        stale['corrected_p2'] = 0.90
        stale.to_csv(raw / report.MONITORING, index=False)
        pd.DataFrame(ROSTER[:1]).to_csv(raw / report.PREDICTIONS, index=False)
        frame = report.build(raw)
        self.assertEqual(Path(frame.run_directory.iloc[0]), bundle)
        self.assertEqual(len(frame), 3)
        a = frame.set_index('home_team').loc['A']
        self.assertAlmostEqual(a.p_narrow, 1 - expected(ROSTER[0])['score'], places=12)

    def test_mismatch_with_monitoring_is_flagged_not_shown(self):
        monitor = monitoring()
        monitor.loc[monitor.home_team == 'A', 'corrected_p2'] = 0.10
        a = report.build(self.plain(monitor=monitor)).set_index('home_team').loc['A']
        self.assertEqual(a.status, report.MISMATCH)
        self.assertTrue(pd.isna(a.p_narrow))
        self.assertIn('differs from monitoring', a.exclusion_reason)

    def test_roster_is_the_base_when_monitoring_is_empty_or_missing(self):
        header_only = monitoring().iloc[0:0]
        frame = report.build(self.plain(monitor=header_only))
        self.assertEqual(len(frame), 3)
        self.assertEqual(set(frame.status), {report.NOT_MONITORED})
        self.assertEqual(set(frame.exclusion_reason), {report.NO_MONITORING_ROW})
        missing = self.directory / 'missing'
        shutil.copytree(self.plain(write_monitoring=False), missing)
        frame = report.build(missing)
        self.assertEqual(set(frame.exclusion_reason), {report.NO_MONITORING_FILE})

    def test_fixture_without_a_monitoring_row_is_kept_with_a_reason(self):
        frame = report.build(self.plain(monitor=monitoring(rows=ROSTER[:1], unusable=[])))
        reasons = dict(zip(frame.home_team, frame.status))
        self.assertEqual(reasons, {'A': 'USABLE', 'C': report.NOT_MONITORED, 'E': report.NOT_MONITORED})

    def test_sorted_by_narrow_then_unscored_by_kickoff(self):
        frame = report.build(self.plain())
        scored = frame[frame.p_narrow.notna()]
        self.assertEqual(list(scored.p_narrow), sorted(scored.p_narrow, reverse=True))
        self.assertEqual(frame.iloc[-1].home_team, 'E')

    def test_quote_ages_use_run_and_kickoff_not_wall_clock(self):
        a = report.build(self.plain()).set_index('home_team').loc['A']
        self.assertEqual(a.quote_age_at_run_min, 1)
        self.assertEqual(a.quote_age_at_kickoff_min, 30 * 60 + 3)

    def test_out_of_domain_flags_competitions_outside_training(self):
        flags = dict(zip(*report.build(self.plain())[['home_team', 'out_of_domain']].T.values))
        self.assertEqual(flags, {'A': True, 'C': False, 'E': False})

    def test_writes_csv_and_markdown(self):
        readable = self.directory / 'readable'
        report.write(self.plain(), readable)
        self.assertEqual(len(pd.read_csv(readable / report.CSV_NAME)), 3)
        text = (readable / report.MD_NAME).read_text(encoding='utf-8')
        self.assertIn('| Serie A | C v D |', text)
        self.assertIn('## Not scored (1)', text)
        self.assertIn('[UNUSABLE]: no usable market-implied fit', text)

    def test_for_fixtures_aligns_rows_and_tolerates_missing_data(self):
        raw = self.plain()
        fixtures = pd.DataFrame([{'league': 'Serie A', 'home_team': 'C', 'away_team': 'D'},
                                 {'league': 'Serie A', 'home_team': 'X', 'away_team': 'Y'},
                                 {'league': 'Premier League', 'home_team': 'E', 'away_team': 'F'}], index=[7, 8, 9])
        got = report.for_fixtures(fixtures, raw)
        self.assertEqual(list(got.index), [7, 8, 9])
        self.assertEqual(list(got.columns), list(report.SHORTLIST_COLUMNS))
        self.assertAlmostEqual(got.loc[7, 'p_narrow'], 1 - expected(ROSTER[1])['score'], places=12)
        self.assertTrue(got.loc[[8, 9], 'p_narrow'].isna().all())  # unknown, and unscored
        nowhere = self.directory / 'nowhere'
        nowhere.mkdir()
        self.assertTrue(report.for_fixtures(fixtures, nowhere).isna().all().all())
        self.assertTrue(report.for_fixtures(fixtures.iloc[0:0], raw).empty)


if __name__ == '__main__':
    unittest.main()
