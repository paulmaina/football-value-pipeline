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


def forecast(home, away, league, h2h, ou, ah_line, ah_prices, kickoff='2026-11-04T20:00:00+00:00', fixture_id=None):
    """A forecast row whose Pinnacle quotes reach the fit the way the pipeline reads them."""
    return {'league': league, 'home_team': home, 'away_team': away, 'kickoff_utc': kickoff, 'fixture_id': fixture_id,
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
                    'fixture_id': row.get('fixture_id'),
                    'kickoff_utc': row['kickoff_utc'], 'generated_at_utc': RUN, 'model_version': MODEL,
                    'status': 'USABLE', 'exclusion_reason': '', 'fit': context['fit'], 'latest_input_quote_utc': QUOTED,
                    'corrected_p2': context['score'],
                    'corrected_p3': nm.margin_tail(context['margins'], context['probs'], 3),
                    'uncorrected_p2': nm.margin_tail(context['margins'], context['uncorrected_probs'], 2),
                    'corrected_cagey_quintile': 'Q3'})
    for row in unusable:
        out.append({'league': row['league'], 'home_team': row['home_team'], 'away_team': row['away_team'],
                    'fixture_id': row.get('fixture_id'),
                    'kickoff_utc': row['kickoff_utc'], 'generated_at_utc': RUN, 'model_version': MODEL,
                    'status': 'UNUSABLE', 'exclusion_reason': 'no usable market-implied fit (missing input: over_2_5)'})
    return pd.DataFrame(out, columns=['league', 'home_team', 'away_team', 'fixture_id', 'kickoff_utc', 'generated_at_utc',
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
        kick = {'kickoff_utc': ROSTER[1]['kickoff_utc']}
        fixtures = pd.DataFrame([{'league': 'Serie A', 'home_team': 'C', 'away_team': 'D', **kick},
                                 {'league': 'Serie A', 'home_team': 'X', 'away_team': 'Y', **kick},
                                 {'league': 'Premier League', 'home_team': 'E', 'away_team': 'F',
                                  'kickoff_utc': ROSTER[2]['kickoff_utc']}], index=[7, 8, 9])
        got = report.for_fixtures(fixtures, raw)
        self.assertEqual(list(got.index), [7, 8, 9])
        self.assertEqual(list(got.columns), list(report.SHORTLIST_COLUMNS))
        self.assertAlmostEqual(got.loc[7, 'p_narrow'], 1 - expected(ROSTER[1])['score'], places=12)
        self.assertTrue(got.loc[[8, 9], 'p_narrow'].isna().all())  # unknown, and unscored
        nowhere = self.directory / 'nowhere'
        nowhere.mkdir()
        self.assertTrue(report.for_fixtures(fixtures, nowhere).isna().all().all())
        self.assertTrue(report.for_fixtures(fixtures.iloc[0:0], raw).empty)
        # Names alone (no fixture_id, no kick-off) are not an identity.
        names_only = fixtures.drop(columns='kickoff_utc')
        self.assertTrue(report.for_fixtures(names_only, raw).isna().all().all())

    # --- Fixture identity: the same pairing on two dates -------------------------------------------------

    def repeat_pairing(self, with_ids=True):
        first = forecast('A', 'B', 'UEFA Champions League', (1.93, 3.89, 3.88), (1.75, 2.14), -0.5, (2.04, 1.86),
                         kickoff='2026-11-04T20:00:00+00:00', fixture_id='fx:1' if with_ids else None)
        later = forecast('A', 'B', 'UEFA Champions League', (2.40, 3.40, 2.90), (1.95, 1.90), -0.25, (1.98, 1.92),
                         kickoff='2026-11-25T20:00:00+00:00', fixture_id='fx:2' if with_ids else None)
        return first, later

    def test_same_teams_on_two_dates_keeps_both_and_scores_only_the_monitored_one(self):
        for with_ids in (True, False):
            with self.subTest(fixture_ids=with_ids):
                first, later = self.repeat_pairing(with_ids)
                frame = report.build(self.plain(roster=[first, later], monitor=monitoring(rows=[first], unusable=[])))
                self.assertEqual(len(frame), 2)
                by_kickoff = frame.set_index('kickoff_utc')
                scored = by_kickoff.loc[first['kickoff_utc']]
                self.assertAlmostEqual(scored.p_narrow, 1 - expected(first)['score'], places=12)
                self.assertEqual(scored.status, 'USABLE')
                unscored = by_kickoff.loc[later['kickoff_utc']]
                self.assertEqual(unscored.status, report.NOT_MONITORED)
                self.assertTrue(pd.isna(unscored.p_narrow))

    def test_fixture_id_wins_over_names_and_different_ids_never_fall_back(self):
        first, later = self.repeat_pairing()
        monitor = monitoring(rows=[first], unusable=[])
        # Same league, teams and kick-off as the forecast, but another fixture's id: must not match.
        monitor['fixture_id'] = 'fx:other'
        frame = report.build(self.plain(roster=[first], monitor=monitor))
        self.assertEqual(frame.iloc[0].status, report.NOT_MONITORED)
        # Same id with a differently formatted kick-off still matches.
        monitor['fixture_id'], monitor['kickoff_utc'] = 'fx:1', '2026-11-04T20:00:00Z'
        frame = report.build(self.plain(roster=[first], monitor=monitor))
        self.assertEqual(frame.iloc[0].status, 'USABLE')

    def test_kickoff_fallback_works_when_either_side_lacks_an_id(self):
        first, later = self.repeat_pairing()
        bare_first = {**first, 'fixture_id': None}
        cases = {'forecast has id, monitoring has none': ([first, later], monitoring(rows=[bare_first], unusable=[])),
                 'monitoring has id, forecast has none': ([bare_first, {**later, 'fixture_id': None}],
                                                          monitoring(rows=[first], unusable=[]))}
        for name, (roster, monitor) in cases.items():
            with self.subTest(name):
                frame = report.build(self.plain(roster=roster, monitor=monitor)).set_index('kickoff_utc')
                self.assertEqual(frame.loc[first['kickoff_utc']].status, 'USABLE')
                self.assertAlmostEqual(frame.loc[first['kickoff_utc']].p_narrow, 1 - expected(first)['score'],
                                       places=12)
                self.assertEqual(frame.loc[later['kickoff_utc']].status, report.NOT_MONITORED)
                # The tier lookup takes the same path in both directions.
                keys = ('league', 'home_team', 'away_team', 'kickoff_utc', 'fixture_id')
                tier = pd.DataFrame([{k: roster[0][k] for k in keys}])
                got = report.for_fixtures(tier, self.plain(roster=roster, monitor=monitor))
                self.assertAlmostEqual(got.iloc[0].p_narrow, 1 - expected(first)['score'], places=12)

    def test_conflicting_ids_never_fall_back_in_either_direction(self):
        first, _ = self.repeat_pairing()
        for forecast_id, monitor_id in (('fx:1', 'fx:other'), ('fx:other', 'fx:1')):
            with self.subTest(forecast=forecast_id, monitoring=monitor_id):
                monitor = monitoring(rows=[first], unusable=[])
                monitor['fixture_id'] = monitor_id
                frame = report.build(self.plain(roster=[{**first, 'fixture_id': forecast_id}], monitor=monitor))
                self.assertEqual(frame.iloc[0].status, report.NOT_MONITORED)

    def test_id_match_and_bare_twin_on_the_same_kickoff_is_ambiguous_for_the_bare_query(self):
        first, _ = self.repeat_pairing()
        # Monitoring holds the same fixture twice: once with its id, once without.
        monitor = monitoring(rows=[first, {**first, 'fixture_id': None}], unusable=[])
        # A forecast with the id matches its id row only.
        frame = report.build(self.plain(roster=[first], monitor=monitor))
        self.assertEqual(frame.iloc[0].status, 'USABLE')
        # A forecast without an id sees both rows: reported, not guessed.
        frame = report.build(self.plain(roster=[{**first, 'fixture_id': None}], monitor=monitor))
        self.assertEqual(frame.iloc[0].status, report.AMBIGUOUS)

    def test_fallback_kickoff_formats_compare_equal(self):
        first, _ = self.repeat_pairing(with_ids=False)
        monitor = monitoring(rows=[first], unusable=[])
        monitor['kickoff_utc'] = '2026-11-04T20:00:00Z'
        self.assertEqual(report.build(self.plain(roster=[first], monitor=monitor)).iloc[0].status, 'USABLE')

    def test_duplicate_monitoring_rows_are_ambiguous_not_guessed(self):
        first, _ = self.repeat_pairing()
        monitor = monitoring(rows=[first, first], unusable=[])
        row = report.build(self.plain(roster=[first], monitor=monitor)).iloc[0]
        self.assertEqual(row.status, report.AMBIGUOUS)
        self.assertTrue(pd.isna(row.p_narrow))
        self.assertIn('2 monitoring rows match', row.exclusion_reason)

    def test_one_monitoring_row_claimed_by_two_forecasts_is_ambiguous(self):
        first, _ = self.repeat_pairing(with_ids=False)
        frame = report.build(self.plain(roster=[first, dict(first)], monitor=monitoring(rows=[first], unusable=[])))
        self.assertEqual(list(frame.status), [report.AMBIGUOUS, report.AMBIGUOUS])
        self.assertIn('also matches 1 other', frame.iloc[0].exclusion_reason)

    def test_tier_lookup_uses_the_same_identity(self):
        for with_ids in (True, False):
            with self.subTest(fixture_ids=with_ids):
                first, later = self.repeat_pairing(with_ids)
                raw = self.plain(roster=[first, later], monitor=monitoring(rows=[first], unusable=[]))
                keys = ('league', 'home_team', 'away_team', 'kickoff_utc', 'fixture_id')
                tier = pd.DataFrame([{k: later[k] for k in keys}, {k: first[k] for k in keys}], index=[3, 4])
                got = report.for_fixtures(tier, raw)
                self.assertTrue(pd.isna(got.loc[3, 'p_narrow']))  # the later match has no score
                self.assertAlmostEqual(got.loc[4, 'p_narrow'], 1 - expected(first)['score'], places=12)


if __name__ == '__main__':
    unittest.main()
