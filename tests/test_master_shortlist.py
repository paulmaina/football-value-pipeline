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
        self.assertEqual(flags, {'A': 'value', 'B': 'below fair', 'C': 'below fair', 'F': 'value'})

    def test_stake_cost_rejection_is_never_value(self):
        rows = pd.DataFrame([cand('A', edge=0.03, reasons='expected profit after stake cost below 0')])
        self.assertEqual(ms.pool(rows).iloc[0].master_price_flag, 'below fair')


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
        self.assertEqual(list(frame.master_price_flag), ['value'] * 2 + ['below fair'] * 3)

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
        self.assertEqual((info['n_bets'], info['value_bets'], info['below_fair_bets'], info['size']), (2, 1, 1, 10))


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
        self.assertEqual(readable.iloc[0]['Price vs fair (value / below fair)'], 'value')
        self.assertIn('## Master shortlist (the 10 best bets this run)', report)
        self.assertIn('3 bets, 1 value, 2 below fair', report)


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
