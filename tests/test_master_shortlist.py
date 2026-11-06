"""Master shortlist: 10 best bets per run, one per match; value safest first, then fill closest to fair."""

from offline_test_case import OfflineQuotePolicyTestCase
import json
import tempfile
import unittest
from pathlib import Path

import pandas as pd

import master_shortlist as ms
import price_edge_cagey_shortlist as v28
from test_price_edge_shortlist import NOW, POLICY
from test_value_per_market import fixture, h2h_1xbet, over_1xbet, price_at

KICK = (NOW + pd.Timedelta(hours=24)).isoformat()


def cand(home, market='Home win', edge=0.02, safe=0.6, odds=1.8, reasons='', decision=None, **kw):
    """One evaluated candidate row as the v28 decisions frame holds it."""
    if decision is None:
        decision = 'REJECTED' if reasons else 'ELIGIBLE'
    return {'league': 'Premier League', 'home_team': home, 'away_team': 'Away FC', 'kickoff_utc': KICK,
            'fixture_id': 'f-' + home, 'market': market, 'market_to_bet': market, 'bookmaker': '1xBet',
            'offered_decimal_odds': odds, 'fair_odds': odds / (1 + edge), 'edge': edge, 'reference_type': 'a',
            'pinnacle_no_loss_probability': safe, 'rejection_reasons': reasons, 'decision': decision,
            'evaluated_at_utc': NOW.isoformat(), 'selection_policy_version': v28.POLICY, **kw}


class PoolTests(OfflineQuotePolicyTestCase):
    def test_only_price_reasons_may_fail(self):
        rows = pd.DataFrame([
            cand('A'),
            cand('B', edge=-0.03, reasons='edge below 1%'),
            cand('C', edge=0.005, reasons='edge below 2%; expected profit after stake cost below 0'),
            cand('D', reasons='offered quote stale'),
            cand('E', reasons='kickoff outside 20-minute to 48-hour window'),
            cand('F', edge=0.03, reasons='other qualifying line chosen for this fixture and market group (safest first)',
                 decision='NOT_SELECTED'),
            {**cand('G'), 'reference_type': None},
            {**cand('H'), 'offered_decimal_odds': None}])
        flags = dict(zip(*ms.pool(rows)[['home_team', 'master_price_flag']].T.values))
        self.assertEqual(flags, {'A': 'value', 'B': 'below value threshold', 'C': 'below value threshold', 'F': 'value'})

    def test_stake_cost_rejection_is_never_value(self):
        rows = pd.DataFrame([cand('A', edge=0.03, reasons='expected profit after stake cost below 0')])
        self.assertEqual(ms.pool(rows).iloc[0].master_price_flag, 'below value threshold')


class SelectionTests(OfflineQuotePolicyTestCase):
    def test_value_safest_first_then_fill_closest_to_fair(self):
        rows = pd.DataFrame([
            cand('V1', edge=0.05, safe=0.55), cand('V2', edge=0.011, safe=0.90),
            cand('F1', edge=-0.002, safe=0.40, reasons='edge below 1%'),
            cand('F2', edge=-0.06, safe=0.99, odds=1.02, reasons='edge below 1%'),
            cand('F3', edge=0.004, safe=0.50, reasons='edge below 1%')])
        frame = ms.build(rows)
        self.assertEqual(list(frame.home_team), ['V2', 'V1', 'F3', 'F1', 'F2'])
        self.assertEqual(list(frame.master_rank), [1, 2, 3, 4, 5])
        self.assertEqual(list(frame.master_price_flag), ['value'] * 2 + ['below value threshold'] * 3)

    def test_one_bet_per_match_value_before_fill_safest_within(self):
        rows = pd.DataFrame([
            cand('A', market='Over 1.5', edge=-0.01, safe=0.95, reasons='edge below 1%'),
            cand('A', market='Home win', edge=0.015, safe=0.50),
            cand('A', market='Asian Handicap Home +0.00', edge=0.012, safe=0.70)])
        frame = ms.build(rows)
        self.assertEqual(len(frame), 1)
        self.assertEqual(frame.iloc[0].market_to_bet, 'Asian Handicap Home +0.00')

    def test_always_ten_when_enough_matches_fewer_only_when_fewer_matches(self):
        many = pd.DataFrame([cand(f'M{i:02d}', edge=-0.01 * i, reasons='edge below 1%') for i in range(1, 15)]
                            + [cand('V', edge=0.02)])
        frame = ms.build(many)
        self.assertEqual(len(frame), ms.SIZE)
        self.assertEqual(frame.iloc[0].home_team, 'V')
        self.assertEqual(list(frame.home_team[1:4]), ['M01', 'M02', 'M03'])
        few = pd.DataFrame([cand(f'M{i}', edge=-0.02, reasons='edge below 1%') for i in range(3)])
        self.assertEqual(len(ms.build(few)), 3)
        self.assertTrue(ms.build(pd.DataFrame()).empty)

    def test_summary_counts(self):
        frame = ms.build(pd.DataFrame([cand('V'), cand('F', edge=-0.01, reasons='edge below 1%')]))
        info = ms.summary(frame)
        self.assertEqual((info['n_bets'], info['value_bets'], info['below_threshold_bets'], info['size']), (2, 1, 1, 10))


def run(*rows, settings=None, monitor=None):
    settings = settings or {'cagey_correction_enabled': True, 'cagey_tier_enabled': True,
                            'cagey_tier_rule': v28.TIER_RULE_NARROW, 'value_rule': v28.VALUE_RULE_PER_MARKET}
    return v28.build_shortlist(pd.DataFrame(list(rows)), NOW, execution_policy=POLICY, settings=settings,
                               monitor=monitor)


class PipelineTests(OfflineQuotePolicyTestCase):
    def setUp(self):
        super().setUp()
        self.predictions = pd.DataFrame([
            fixture(h2h_1xbet(home=price_at('home', 0.015)), home='Value FC'),
            fixture(over_1xbet(price_at('over_1_5', 0.005)), home='Fill FC'),
            fixture(home='Pinnacle Only FC')])
        self.predictions['p_home'], self.predictions['p_draw'], self.predictions['p_away'] = 0.45, 0.27, 0.28

    def test_raw_check_binds_the_master_shortlist_to_the_replay(self):
        from unittest.mock import patch
        from workflow_checks import raw_check
        monitoring = []
        selected, decisions, summary = run(*self.predictions.to_dict('records'), monitor=monitoring)
        with tempfile.TemporaryDirectory() as tmp:
            raw = Path(tmp) / 'raw'
            raw.mkdir()
            self.predictions.to_csv(raw / 'all_leagues_predictions.csv', index=False)
            selected.to_csv(raw / 'conservative_bet_shortlist.csv', index=False)
            v28.cagey_tier_list(decisions).to_csv(raw / v28.TIER_FILE, index=False)
            v28.record_monitoring(summary, monitoring, raw)
            master = ms.write(decisions, raw, summary)
            self.assertEqual(len(master), 3)  # one per match, three matches
            self.assertEqual(master.iloc[0].home_team, 'Value FC')
            self.assertEqual(master.iloc[0].master_price_flag, 'value')
            path = raw / 'conservative_bet_summary.json'
            path.write_text(json.dumps(summary, default=str), encoding='utf-8')
            with patch.object(v28, 'load_settings', return_value={'cagey_correction_enabled': False,
                                                                  'cagey_tier_enabled': False, 'model_version': None}):
                raw_check(Path(tmp), raw_dir=raw)
            master.iloc[::-1].assign(master_rank=[1, 2, 3]).to_csv(raw / ms.FILE, index=False)
            with self.assertRaisesRegex(Exception, 'master shortlist differs'):
                raw_check(Path(tmp), raw_dir=raw)
            (raw / ms.FILE).unlink()
            with self.assertRaisesRegex(Exception, 'Missing current master shortlist'):
                raw_check(Path(tmp), raw_dir=raw)
            # A master-10-v1 run replays with v1's rule and schema.
            old = ms.build(decisions, version=ms.VERSION_V1)
            old.to_csv(raw / ms.FILE, index=False)
            path.write_text(json.dumps({**summary, 'master_shortlist': ms.summary(old, ms.VERSION_V1)}, default=str),
                            encoding='utf-8')
            with patch.object(v28, 'load_settings', return_value={'cagey_correction_enabled': False,
                                                                  'cagey_tier_enabled': False, 'model_version': None}):
                raw_check(Path(tmp), raw_dir=raw)
            # A run recorded before the master shortlist existed carries no entry and needs no file.
            path.write_text(json.dumps({k: v for k, v in summary.items() if k != 'master_shortlist'}, default=str),
                            encoding='utf-8')
            raw_check(Path(tmp), raw_dir=raw)

    def test_readable_master_shortlist(self):
        from format_football_output import process_conservative_shortlist, MASTER_READABLE
        selected, decisions, summary = run(*self.predictions.to_dict('records'))
        with tempfile.TemporaryDirectory() as tmp:
            raw, out = Path(tmp) / 'raw', Path(tmp) / 'readable'
            raw.mkdir()
            out.mkdir()
            selected.to_csv(raw / 'conservative_bet_shortlist.csv', index=False)
            v28.cagey_tier_list(decisions).to_csv(raw / v28.TIER_FILE, index=False)
            ms.write(decisions, raw, summary)
            (raw / 'conservative_bet_summary.json').write_text(json.dumps(summary, default=str), encoding='utf-8')
            process_conservative_shortlist(raw, out)
            readable = pd.read_csv(out / MASTER_READABLE)
            report = (out / 'conservative_bet_shortlist_report.md').read_text(encoding='utf-8')
            # Without the summary entry the stale readable file is removed.
            (raw / 'conservative_bet_summary.json').write_text(
                json.dumps({k: v for k, v in summary.items() if k != 'master_shortlist'}, default=str), encoding='utf-8')
            process_conservative_shortlist(raw, out)
            self.assertFalse((out / MASTER_READABLE).exists())
        self.assertEqual(list(readable.Rank), [1, 2, 3])
        self.assertEqual(readable.iloc[0]['Price flag (value / below value threshold)'], 'value')
        self.assertIn('## Master shortlist (the 10 best bets this run)', report)
        self.assertIn('3 bets, 1 value, 2 below value threshold', report)


class ProbabilityBasisTests(OfflineQuotePolicyTestCase):
    def test_cagey_priced_bets_rank_on_the_corrected_no_loss_and_say_so(self):
        # Slavia-style: fair price from the corrected fit, uncorrected fit no-loss 84.71%, corrected 87.15%.
        rows = pd.DataFrame([
            cand('Slavia', market='Asian Handicap Home +1.00', reference_type='c-cagey', safe=0.8471,
                 corrected_no_loss_probability=0.8715),
            cand('Pinnacle FC', safe=0.86, corrected_no_loss_probability=0.99)])
        frame = ms.build(rows)
        self.assertEqual(list(frame.home_team), ['Slavia', 'Pinnacle FC'])
        self.assertEqual(list(frame.master_no_loss_probability), [0.8715, 0.86])
        self.assertEqual(list(frame.master_probability_basis), ['cagey-corrected fit', 'Pinnacle fair price'])
        # master-10-v1 (recorded runs) keeps its rule: the uncorrected figure for every reference.
        old = ms.build(rows, version=ms.VERSION_V1)
        self.assertEqual(list(old.home_team), ['Pinnacle FC', 'Slavia'])
        self.assertEqual(list(old.columns), ms.COLUMNS_V1)

    def test_direct_references_are_labelled_by_the_distribution_actually_used(self):
        rows = pd.DataFrame([
            cand('Fitted', market='Home win', reference_type='b', fit_usable=True, safe=0.62),
            cand('Direct', market='Home win', reference_type='b', fit_usable=False, safe=0.55),
            cand('Over', market='Over 1.5', reference_type='a', fit_usable=True, safe=0.75)])
        labels = dict(zip(*ms.build(rows)[['home_team', 'master_probability_basis']].T.values))
        self.assertEqual(labels, {'Fitted': 'market-implied fit B', 'Direct': 'Pinnacle fair price',
                                  'Over': 'Pinnacle fair price'})

    def test_no_stand_in_distribution_and_missing_safety_ranks_last(self):
        rows = pd.DataFrame([cand('Missing', safe=None, corrected_no_loss_probability=0.95, edge=0.05),
                             cand('Known', safe=0.40, edge=0.011),
                             cand('Fit', reference_type='c', safe=0.70, edge=0.03)])
        frame = ms.build(rows)
        self.assertEqual(list(frame.home_team), ['Fit', 'Known', 'Missing'])
        self.assertEqual(list(frame.master_probability_basis), ['market-implied fit B', 'Pinnacle fair price', 'unavailable'])
        self.assertTrue(pd.isna(frame.master_no_loss_probability.iloc[2]))

    def test_event_id_comes_from_the_runs_forecast(self):
        rows = pd.DataFrame([cand('A'), cand('B')])
        forecasts = pd.DataFrame([{'league': 'Premier League', 'home_team': 'A', 'away_team': 'Away FC',
                                   'kickoff_utc': KICK, 'odds_event_id': 'evt-a'}])
        frame = ms.build(rows, forecasts)
        self.assertEqual(frame.odds_event_id.iloc[0], 'evt-a')
        self.assertTrue(pd.isna(frame.odds_event_id.iloc[1]))
        self.assertEqual(ms.summary(frame)['version'], ms.VERSION)
        self.assertIn('probability_basis', ms.summary(frame))
        self.assertNotIn('probability_basis', ms.summary(frame, ms.VERSION_V1))


class ReplayComparisonTests(OfflineQuotePolicyTestCase):
    def setUp(self):
        super().setUp()
        rows = pd.DataFrame([
            cand('A', market='Asian Handicap Home +1.00', handicap_side='home', handicap_line=1.0, per_stake_cost=0.0),
            cand('B', edge=-0.004, reasons='edge below 1%', per_stake_cost=0.0)])
        self.expected = ms.build(rows)
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / ms.FILE
            self.expected.to_csv(path, index=False)
            self.written = pd.read_csv(path, low_memory=False)

    def test_written_list_matches_its_replay(self):
        self.assertTrue(ms.matches(self.written, self.expected))
        # CSV/solver round-off on a fitted number is tolerated.
        self.assertTrue(ms.matches(self.written.assign(fair_odds=self.written.fair_odds + 1e-10), self.expected))

    def test_every_grading_and_display_field_is_compared(self):
        changes = {'handicap_line': -1.0, 'fixture_id': 'f-other', 'fair_odds': 1.5, 'per_stake_cost': 0.01,
                   'edge': 0.2, 'minimum_odds_master': 9.0, 'master_no_loss_probability': 0.1, 'kickoff_utc':
                   (NOW + pd.Timedelta(hours=30)).isoformat(), 'handicap_side': 'away', 'in_cagey_tier': True,
                   'reference_type': 'c', 'value_market_group': 'match_winner', 'master_version': 'other',
                   'odds_event_id': 'other-event', 'master_probability_basis': 'cagey-corrected fit'}
        for column, value in changes.items():
            tampered = self.written.copy()
            tampered[column] = tampered[column].astype(object)
            tampered.loc[0, column] = value
            with self.subTest(column=column):
                self.assertFalse(ms.matches(tampered, self.expected))

    def test_full_schema_required(self):
        self.assertFalse(ms.matches(self.written.drop(columns=['per_stake_cost']), self.expected))
        self.assertFalse(ms.matches(self.written.assign(extra=1), self.expected))
        self.assertFalse(ms.matches(self.written[ms.COLUMNS[::-1]], self.expected))
        self.assertTrue(ms.matches(pd.DataFrame(columns=ms.COLUMNS), ms.build(pd.DataFrame())))


class RefreshTests(OfflineQuotePolicyTestCase):
    def test_refresh_rebuilds_the_master_list_and_replaces_a_seeded_copy(self):
        from refresh_conservative_shortlist import _refresh
        from format_football_output import publish_shortlists, MASTER_READABLE
        import narrow_margin_report as narrow
        predictions = pd.DataFrame([
            fixture(h2h_1xbet(home=price_at('home', 0.015)), home='Value FC'),
            fixture(over_1xbet(price_at('over_1_5', 0.03)), home='Fill FC')])
        predictions['p_home'], predictions['p_draw'], predictions['p_away'] = 0.45, 0.27, 0.28
        with tempfile.TemporaryDirectory() as tmp:
            raw, out = Path(tmp) / 'raw', Path(tmp) / 'readable'
            raw.mkdir()
            out.mkdir()
            predictions.to_csv(raw / 'all_leagues_predictions.csv', index=False)
            # A master list seeded from the previous run (different match, older evaluation).
            stale = ms.build(pd.DataFrame([cand('Old FC')]))
            stale.assign(evaluated_at_utc=(NOW - pd.Timedelta(hours=6)).isoformat()).to_csv(raw / ms.FILE, index=False)
            summary = _refresh(Path(tmp), as_of=NOW.to_pydatetime(), raw_dir=raw)
            written = pd.read_csv(raw / ms.FILE)
            decisions = pd.read_csv(raw / 'conservative_bet_rejections.csv', low_memory=False)
            stored = json.loads((raw / 'conservative_bet_summary.json').read_text(encoding='utf-8'))
            # A narrow report left over from the previous run.
            pd.DataFrame([{'home_team': 'Old FC'}]).to_csv(out / narrow.CSV_NAME, index=False)
            (out / narrow.MD_NAME).write_text('previous run', encoding='utf-8')
            publish_shortlists(raw, out)
            readable = pd.read_csv(out / MASTER_READABLE)
            report = pd.read_csv(out / narrow.CSV_NAME)
            expected_report = narrow.build(raw)
            report_md = (out / narrow.MD_NAME).read_text(encoding='utf-8')
        self.assertEqual(sorted(report.home_team), ['Fill FC', 'Value FC'])
        self.assertEqual(list(report.home_team), list(expected_report.home_team))
        self.assertNotEqual(report_md, 'previous run')
        self.assertNotIn('Old FC', set(written.home_team))
        self.assertEqual(set(written.evaluated_at_utc), {summary['generated_at_utc']})
        self.assertEqual(stored['master_shortlist'], ms.summary(written))
        self.assertTrue(ms.matches(written, ms.build(decisions, predictions)))
        self.assertEqual(list(readable.Home), list(written.home_team))

    def test_other_policies_remove_a_seeded_copy(self):
        with tempfile.TemporaryDirectory() as tmp:
            ms.build(pd.DataFrame([cand('Old FC')])).to_csv(Path(tmp) / ms.FILE, index=False)
            info = {'selection_policy_version': 'some-earlier-policy', 'master_shortlist': {'n_bets': 1}}
            self.assertIsNone(ms.refresh(pd.DataFrame(), tmp, info))
            self.assertFalse((Path(tmp) / ms.FILE).exists())
            self.assertNotIn('master_shortlist', info)


class TrackingTests(OfflineQuotePolicyTestCase):
    def test_capture_only_this_generation(self):
        import price_edge_tracking as tracking
        with tempfile.TemporaryDirectory() as tmp:
            raw = Path(tmp)
            pd.DataFrame([{**cand('A'), 'master_rank': 1}]).reindex(columns=ms.COLUMNS).assign(
                evaluated_at_utc=NOW.isoformat(), selection_policy_version=v28.POLICY).to_csv(raw / ms.FILE, index=False)
            self.assertEqual(tracking.capture_master_file(raw, NOW.isoformat()), raw / ms.FILE)
            self.assertIsNone(tracking.capture_master_file(raw, (NOW + pd.Timedelta(hours=1)).isoformat()))


if __name__ == '__main__':
    unittest.main()
