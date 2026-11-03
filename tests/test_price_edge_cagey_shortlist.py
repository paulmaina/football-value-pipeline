"""Policy v28: v27 price edge with the cagey-match correction (value tier, cagey tier, switches)."""

from offline_test_case import OfflineQuotePolicyTestCase
import json
import unittest

import pandas as pd

import market_implied as mi
import narrow_margin as nm
import price_edge_cagey_shortlist as v28
import price_edge_shortlist as v27
from asian_handicap import label
from test_price_edge_shortlist import (NOW, POLICY, ah_pair, decision, evaluate, fit_price, offer, pinnacle_market,
                                       quote, row)

OFF = {'cagey_correction_enabled': False, 'cagey_tier_enabled': False}
VALUE_ONLY = {'cagey_correction_enabled': True, 'cagey_tier_enabled': False}


def run(*rows, settings=None, monitor=None):
    return v28.build_shortlist(pd.DataFrame(list(rows)), NOW, execution_policy=POLICY, settings=settings,
                               monitor=monitor)


def corrected(side, line):
    """Corrected fair price of the default test fixture under the production model."""
    h2h, ou, ah = pinnacle_market()
    targets = mi.targets_from_prices(tuple(h2h[k] for k in ('home', 'draw', 'away')), (ou['over'], ou['under']),
                                     (-0.25, *ah))
    fit = mi.fit(targets, include_ah=True)
    pin = {'h2h': (*[h2h[k] for k in ('home', 'draw', 'away')], None), 'ou25': (ou['over'], ou['under'], None)}
    context = v28.corrected_context(pin, fit, {'fit_a': fit}, nm.production_model())
    return v28.corrected_price(context, side, line), context


class ValueTierTests(OfflineQuotePolicyTestCase):
    def test_derived_plus_line_uses_the_corrected_price(self):
        priced, _ = corrected('away', 1.0)
        uncorrected = fit_price('away', 1.0)['fair_odds']
        self.assertLess(priced['corrected_fair_odds'], uncorrected)  # the correction lengthens plus-line win-shares
        _, decisions, _ = run(row(offers=[offer('away', 1.0, 1.50)]), settings=VALUE_ONLY)
        item = decision(decisions, label('away', 1.0))
        self.assertEqual(item.reference_type, 'c-cagey')
        self.assertAlmostEqual(item.fair_odds, priced['corrected_fair_odds'], places=9)
        self.assertAlmostEqual(item.fair_odds_uncorrected, uncorrected, places=9)
        self.assertAlmostEqual(item.minimum_odds, priced['corrected_fair_odds'] * 1.03, places=9)

    def test_qualified_only_because_of_correction(self):
        priced, _ = corrected('away', 1.0)
        uncorrected = fit_price('away', 1.0)['fair_odds']
        price = round(priced['corrected_fair_odds'] * 1.035, 4)
        self.assertLess(price, uncorrected * 1.03)  # v27 would reject this price
        _, plain, _ = evaluate(row(offers=[offer('away', 1.0, price)]))
        self.assertEqual(decision(plain, label('away', 1.0)).rejection_reasons, 'edge below 3%')
        selected, decisions, summary = run(row(offers=[offer('away', 1.0, price)]), settings=VALUE_ONLY)
        item = decision(decisions, label('away', 1.0))
        self.assertEqual(item.decision, 'SHORTLISTED')
        self.assertTrue(item.qualified_only_by_correction)
        self.assertEqual(summary['correction_only_value_picks'], 1)
        self.assertEqual(summary['reference_type_counts'], {'c-cagey': 1})

    def test_minus_lines_and_pinnacle_references_are_unaffected(self):
        offers = [*ah_pair(-0.75, 1.95, 1.95), offer('home', -0.75, 2.10), offer('home', -1.0, 2.9),
                  *ah_pair(1.5, 1.20, 4.6), offer('home', 1.5, 1.27)]
        _, old, _ = evaluate(row(offers=offers))
        _, new, _ = run(row(offers=offers), settings=VALUE_ONLY)
        for market in (label('home', -0.75), label('home', -1.0), label('home', 1.5)):
            a, b = decision(old, market), decision(new, market)
            self.assertEqual((a.reference_type, a.decision, a.rejection_reasons), (b.reference_type, b.decision, b.rejection_reasons))
            self.assertEqual(a.fair_odds if pd.notna(a.fair_odds) else None, b.fair_odds if pd.notna(b.fair_odds) else None)
        pinned = decision(new, label('home', 1.5))
        self.assertEqual(pinned.reference_type, 'a')
        self.assertAlmostEqual(pinned.corrected_vs_pinnacle_gap, pinned.corrected_fair_probability - pinned.fair_probability)
        self.assertIn(v27.NO_REFERENCE, decision(new, label('home', -1.0)).rejection_reasons)

    def test_derived_plus_lines_below_one_keep_the_uncorrected_price(self):
        _, decisions, _ = run(row(offers=[offer('away', 0.75, 1.80)]), settings=VALUE_ONLY)
        self.assertEqual(decision(decisions, label('away', 0.75)).reference_type, 'c')

    def test_switches_off_reproduce_v27_exactly(self):
        offers = [*ah_pair(-0.75, 1.95, 1.95), offer('home', -0.75, 2.10), offer('away', 1.0, 1.5),
                  offer('away', 1.5, 1.4), offer('home', -1.0, 2.9)]
        rows = [row(offers=offers), row(home='Second', offers=[offer('away', 1.0, 2.6)])]
        a_sel, a_dec, a_sum = v27.build_shortlist(pd.DataFrame(rows), NOW, execution_policy=POLICY)
        b_sel, b_dec, b_sum = run(*rows, settings=OFF)
        drop = ['selection_policy_version']
        self.assertTrue(a_dec.drop(columns=drop).equals(b_dec.drop(columns=drop)))
        self.assertTrue(a_sel.drop(columns=drop).equals(b_sel.drop(columns=drop)))
        self.assertEqual(set(b_dec.selection_policy_version), {v28.POLICY})
        self.assertFalse(b_sum['cagey_correction_enabled'] or b_sum['cagey_tier_enabled'])
        for key in ('rejection_counts', 'tagged_candidates', 'n_shortlisted'):
            self.assertEqual(a_sum[key], b_sum[key])


class SwitchTests(OfflineQuotePolicyTestCase):
    def test_config_switches_on_after_gate_pass_and_v28_is_production(self):
        from asian_handicap import PRODUCTION_POLICY, POLICIES
        settings = v28.load_settings()
        self.assertEqual(settings, {'cagey_correction_enabled': True, 'cagey_tier_enabled': True,
                                    'model_version': nm.PRODUCTION_VERSION})
        self.assertEqual(PRODUCTION_POLICY, v28.POLICY)
        self.assertIn(v27.POLICY, POLICIES)

    def test_switches_must_be_booleans_and_need_a_passed_gate(self):
        import tempfile
        from pathlib import Path
        from unittest.mock import patch
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'config.json'
            path.write_text(json.dumps({'cagey_correction_enabled': 'yes', 'cagey_tier_enabled': False,
                                        'model_version': 'x'}), encoding='utf-8')
            with self.assertRaises(ValueError):
                v28.load_settings(path)
            path.write_text(json.dumps({'cagey_correction_enabled': False, 'cagey_tier_enabled': True,
                                        'model_version': 'x'}), encoding='utf-8')
            failed = {'gate': {'gate_result': 'FAIL'}, 'production': {'version': 'x'}}
            with patch.object(nm, 'versions', return_value=failed):
                with self.assertRaises(ValueError):
                    v28.load_settings(path)
                path.write_text(json.dumps({'cagey_correction_enabled': False, 'cagey_tier_enabled': False,
                                            'model_version': 'x'}), encoding='utf-8')
                self.assertFalse(v28.load_settings(path)['cagey_tier_enabled'])

    def test_raw_check_replays_with_the_runs_recorded_settings(self):
        import tempfile
        from pathlib import Path
        from unittest.mock import patch
        from workflow_checks import raw_check
        fair, _ = tier_fair(cagey_row(), 'away', 2.0)
        predictions = pd.DataFrame([cagey_row(offers=[offer('away', 2.0, round(fair['corrected_fair_odds'] * 1.005, 4))]),
                                    row(home='Other', offers=[*ah_pair(-0.75, 1.95, 1.95), offer('home', -0.75, 2.10)])])
        predictions['p_home'], predictions['p_draw'], predictions['p_away'] = 0.45, 0.27, 0.28
        monitoring = []
        selected, decisions, summary = run(*predictions.to_dict('records'), monitor=monitoring)
        self.assertEqual(summary['cagey_model_version'], nm.PRODUCTION_VERSION)
        with tempfile.TemporaryDirectory() as tmp:
            raw = Path(tmp) / 'raw'
            raw.mkdir()
            predictions.to_csv(raw / 'all_leagues_predictions.csv', index=False)
            selected.to_csv(raw / 'conservative_bet_shortlist.csv', index=False)
            v28.cagey_tier_list(decisions).to_csv(raw / v28.TIER_FILE, index=False)
            v28.record_monitoring(summary, monitoring, raw)
            (raw / 'conservative_bet_summary.json').write_text(json.dumps(summary, default=str), encoding='utf-8')
            with patch.object(v28, 'load_settings', return_value=OFF):
                self.assertEqual(raw_check(Path(tmp), raw_dir=raw)['selections'], len(selected))

    def test_raw_check_validates_the_cagey_tier(self):
        import tempfile
        from pathlib import Path
        from workflow_checks import raw_check
        fair, _ = tier_fair(cagey_row(), 'away', 2.0)
        predictions = pd.DataFrame([cagey_row(offers=[offer('away', 2.0, round(fair['corrected_fair_odds'] * 1.005, 4))])])
        predictions['p_home'], predictions['p_draw'], predictions['p_away'] = 0.45, 0.27, 0.28
        monitoring = []
        selected, decisions, summary = run(*predictions.to_dict('records'), monitor=monitoring)
        tier = v28.cagey_tier_list(decisions)
        self.assertEqual(len(tier), 1)
        with tempfile.TemporaryDirectory() as tmp:
            raw = Path(tmp) / 'raw'
            raw.mkdir()
            predictions.to_csv(raw / 'all_leagues_predictions.csv', index=False)
            selected.to_csv(raw / 'conservative_bet_shortlist.csv', index=False)
            v28.record_monitoring(summary, monitoring, raw)

            def write(tier_rows, tier_summary):
                (raw / 'conservative_bet_summary.json').write_text(
                    json.dumps({**summary, 'cagey_tier': tier_summary}, default=str), encoding='utf-8')
                if tier_rows is None:
                    (raw / v28.TIER_FILE).unlink(missing_ok=True)
                else:
                    tier_rows.to_csv(raw / v28.TIER_FILE, index=False)

            write(tier, summary['cagey_tier'])
            raw_check(Path(tmp), raw_dir=raw)
            tampered = [(tier.assign(offered_decimal_odds=999.0), summary['cagey_tier'], 'differs from deterministic'),
                        (tier, {**summary['cagey_tier'], 'n_shortlisted': 999}, 'summary cagey_tier differs'),
                        (None, summary['cagey_tier'], 'Missing current cagey-tier shortlist'),
                        (tier.iloc[0:0], summary['cagey_tier'], 'differs from deterministic')]
            for rows, tier_summary, message in tampered:
                with self.subTest(message=message):
                    write(rows, tier_summary)
                    with self.assertRaisesRegex(Exception, message):
                        raw_check(Path(tmp), raw_dir=raw)
            # The correction-monitoring records are bound to the same replay.
            write(tier, summary['cagey_tier'])
            path = raw / v28.MONITOR_FILE
            original = path.read_bytes()
            frame = pd.read_csv(path)
            for column, value, message in (('corrected_p2', 0.01, 'monitoring records differ'),
                                           ('home_plus_1_5_pinnacle_odds', 9.9, 'monitoring records differ'),
                                           ('generated_at_utc', '2020-01-01T00:00:00+00:00', 'monitoring records differ')):
                with self.subTest(column=column):
                    frame.assign(**{column: value}).to_csv(path, index=False)
                    with self.assertRaisesRegex(Exception, message):
                        raw_check(Path(tmp), raw_dir=raw)
            path.unlink()
            with self.assertRaisesRegex(Exception, 'Missing current correction-monitoring records'):
                raw_check(Path(tmp), raw_dir=raw)
            # A v28 run generated before monitoring existed: no version in its summary, no file.
            earlier = {k: v for k, v in summary.items() if k != 'correction_monitoring_version'}
            (raw / 'conservative_bet_summary.json').write_text(json.dumps(earlier, default=str), encoding='utf-8')
            raw_check(Path(tmp), raw_dir=raw)
            (raw / 'conservative_bet_summary.json').write_text(
                json.dumps({**summary, 'correction_monitoring_version': 'cagey-correction-monitoring-v0'}, default=str),
                encoding='utf-8')
            with self.assertRaisesRegex(Exception, 'Unknown correction-monitoring version'):
                raw_check(Path(tmp), raw_dir=raw)
            path.write_bytes(original)
            write(tier, summary['cagey_tier'])
            raw_check(Path(tmp), raw_dir=raw)


def cagey_row(home='Cagey FC', offers=(), lambdas=(0.95, 0.75, -0.08), main_line=-0.25):
    """A low-scoring, cagey fixture: Pinnacle prices drawn from a known matrix (3% margin)."""
    matrix = mi.dixon_coles_matrix(*lambdas)
    inputs = mi.model_inputs(matrix, main_line)
    h2h = {k: round(1 / (inputs[k] * 1.03), 4) for k in ('home', 'draw', 'away')}
    ou = {'over': round(1 / (inputs['over_2_5'] * 1.03), 4), 'under': round(1 / ((1 - inputs['over_2_5']) * 1.03), 4)}
    pair = ah_pair(main_line, round(1 / (inputs['ah_main'] * 1.03), 4), round(1 / ((1 - inputs['ah_main']) * 1.03), 4),
                   key='spreads')
    data = row(home=home, quotes=[quote('h2h', h2h), quote('totals', ou, key='totals', point=2.5)], offers=offers)
    data['asian_handicap_offers'] = json.dumps(pair + list(offers))
    return data


def tier_fair(data, side, line):
    pin = v27.pinnacle_quotes(data)
    fit, info = v27.market_fit(pin, NOW)
    context = v28.corrected_context(pin, fit, info, nm.production_model())
    return v28.corrected_price(context, side, line), context


class CageyTierTests(OfflineQuotePolicyTestCase):
    def test_qualify_rule_boundaries(self):
        item = {'handicap_line': 1.5, 'offered_decimal_odds': 1.4, 'rejection_reasons': 'edge below 3%'}
        context = {'score': 0.25}
        cases = [((0.0, 0.85), 'ELIGIBLE', ''),
                 ((-0.0001, 0.85), 'REJECTED', 'expected profit below 0 under the corrected matrix'),
                 ((0.01, 0.8499), 'REJECTED', 'corrected no-loss probability below 85%')]
        for (profit, no_loss), expected, reasons in cases:
            out = {'corrected_expected_profit': profit, 'corrected_no_loss_probability': no_loss,
                   'corrected_fair_odds': 1.3}
            self.assertEqual(v28.tier_candidate(item, out, context),
                             {'cagey_tier_decision': expected, 'cagey_tier_reasons': reasons})
        guarded = {**item, 'rejection_reasons': 'offered odds above 3.00; edge below 3%'}
        good = {'corrected_expected_profit': 0.1, 'corrected_no_loss_probability': 0.9, 'corrected_fair_odds': 1.3}
        self.assertEqual(v28.tier_candidate(guarded, good, context)['cagey_tier_reasons'], 'offered odds above 3.00')
        self.assertIsNone(v28.tier_candidate({**item, 'handicap_line': 0.75}, {}, context)['cagey_tier_decision'])
        self.assertIsNone(v28.tier_candidate({**item, 'handicap_line': -1.5}, {}, context)['cagey_tier_decision'])
        self.assertEqual(v28.tier_candidate(item, {}, None)['cagey_tier_reasons'], 'no corrected price')

    def test_suspicious_price_guard_applies_to_the_tier(self):
        item = {'handicap_line': 1.25, 'offered_decimal_odds': 2.50, 'rejection_reasons': ''}
        good = {'corrected_expected_profit': 0.5, 'corrected_no_loss_probability': 0.95, 'corrected_fair_odds': 1.034}
        self.assertEqual(v28.tier_candidate(item, good, {'score': 0.2}),
                         {'cagey_tier_decision': 'REJECTED', 'cagey_tier_reasons': 'offered price above 1.15 x fair odds'})
        boundary = {**item, 'offered_decimal_odds': round(1.15 * 1.034, 6)}
        self.assertEqual(v28.tier_candidate(boundary, good, {'score': 0.2})['cagey_tier_decision'], 'ELIGIBLE')
        # v27's own guard (against its fair reference) is kept too, once.
        flagged = {**item, 'offered_decimal_odds': 1.10, 'rejection_reasons': 'offered price above 1.15 x fair odds'}
        self.assertEqual(v28.tier_candidate(flagged, good, {'score': 0.2})['cagey_tier_reasons'],
                         'offered price above 1.15 x fair odds')

    def test_suspicious_price_rejected_end_to_end(self):
        fair, _ = tier_fair(cagey_row(), 'away', 1.25)
        price = round(fair['corrected_fair_odds'] * 2.4, 2)
        selected, decisions, _ = run(cagey_row(offers=[offer('away', 1.25, min(price, 2.95))]))
        self.assertEqual(len(v28.cagey_tier_list(decisions)), 0)
        rows = decisions[decisions.cagey_tier_decision.notna() & (decisions.bookmaker == '1xBet')]
        self.assertEqual(rows.cagey_tier_reasons.tolist(), ['offered price above 1.15 x fair odds'])
        self.assertEqual(len(selected), 0)

    def decisions(self, scores):
        kick = (NOW + pd.Timedelta(hours=10)).isoformat()
        return pd.DataFrame([{'league': 'Premier League', 'home_team': f'T{i}', 'away_team': 'A', 'fixture_id': f'f{i}',
                              'kickoff_utc': kick, 'corrected_cagey_score': s, 'cagey_tier_decision': 'ELIGIBLE',
                              'cagey_tier_reasons': '', 'pinnacle_fair_odds': None, 'in_value_tier': None,
                              'corrected_no_loss_probability': 0.9, 'corrected_expected_profit': 0.01,
                              'offered_decimal_odds': 1.3, 'market': 'm', 'bookmaker': '1xBet', 'even_odds': False}
                             for i, s in enumerate(scores)])

    def test_cutoff_never_above_the_training_20th_percentile(self):
        scores = [0.25, 0.30, 0.35, 0.40, 0.45, 0.50, 0.55, 0.60, 0.65, 0.70]
        frame = self.decisions(scores)
        tier = v28.apply_cagey_tier(frame, pd.DataFrame(), NOW, {'training_cagey_p20': 0.20})
        self.assertAlmostEqual(tier['cutoff_run_p20'], float(pd.Series(scores).quantile(0.2)))
        self.assertEqual((tier['cutoff_used'], tier['cutoff_training_p20']), (0.20, 0.20))
        self.assertEqual(tier['n_shortlisted'], 0)
        self.assertTrue(frame.cagey_tier_reasons.str.contains('not among the cagiest 20%').all())
        frame = self.decisions(scores)
        tier = v28.apply_cagey_tier(frame, pd.DataFrame(), NOW, {'training_cagey_p20': 0.90})
        self.assertAlmostEqual(tier['cutoff_used'], tier['cutoff_run_p20'])
        self.assertEqual(frame.loc[frame.cagey_tier_decision == 'SHORTLISTED', 'home_team'].tolist(), ['T0', 'T1'])

    def test_one_safest_pick_per_fixture_separate_from_the_value_tier(self):
        data = cagey_row()
        plus2, context = tier_fair(data, 'away', 2.0)
        plus15, _ = tier_fair(data, 'away', 1.5)
        self.assertLess(context['score'], nm.production_model()['training_cagey_p20'])
        offers = [offer('away', 1.5, round(plus15['corrected_fair_odds'] * 1.01, 4)),
                  offer('away', 2.0, round(plus2['corrected_fair_odds'] * 1.005, 4))]
        data = cagey_row(offers=offers)
        selected, decisions, summary = run(data)
        tier = v28.cagey_tier_list(decisions)
        self.assertEqual(len(tier), 1)
        self.assertEqual(tier.iloc[0].market_to_bet, label('away', 2.0))  # higher corrected no-loss
        self.assertGreaterEqual(tier.iloc[0].corrected_no_loss_probability, 0.85)
        self.assertGreaterEqual(tier.iloc[0].corrected_expected_profit, 0)
        self.assertEqual(summary['cagey_tier']['n_shortlisted'], 1)
        self.assertEqual(set(v28.TIER_OUTPUT_COLUMNS) - set(tier.columns), set())
        # Display-only settlement split: the five outcomes sum to 1 and match the no-loss and profit figures.
        pick = tier.iloc[0]
        outcomes = [pick[c] for c in v28.SETTLEMENT_COLUMNS[:5]]
        self.assertAlmostEqual(sum(outcomes), 1.0, places=9)
        self.assertAlmostEqual(pick.corrected_p_win + pick.corrected_p_half_win + pick.corrected_p_push,
                               pick.corrected_no_loss_probability, places=9)
        self.assertAlmostEqual(pick.corrected_p_profit, pick.corrected_p_win + pick.corrected_p_half_win, places=9)
        self.assertGreater(pick.corrected_p_push, 0)  # +2: losing by exactly two is a refund
        # The correction lowers the plus-line fair price in a cagey match.
        self.assertGreater(pick.uncorrected_matrix_fair_odds, pick.corrected_fair_odds)
        # The tier never changes the value tier.
        value_only, _, _ = run(data, settings=VALUE_ONLY)
        self.assertTrue(selected.drop(columns=v28.TIER_COLUMNS).equals(value_only.drop(columns=v28.TIER_COLUMNS)))
        self.assertEqual(bool(tier.iloc[0].in_value_tier), len(selected) > 0)

    def test_formatter_renders_the_tier_separately(self):
        import tempfile
        from pathlib import Path
        from format_football_output import process_conservative_shortlist
        fair, _ = tier_fair(cagey_row(), 'away', 2.0)
        data = cagey_row(offers=[offer('away', 2.0, round(fair['corrected_fair_odds'] * 1.005, 4))])
        selected, decisions, summary = run(data)
        with tempfile.TemporaryDirectory() as tmp:
            raw, out = Path(tmp) / 'raw', Path(tmp) / 'readable'
            raw.mkdir()
            out.mkdir()
            selected.to_csv(raw / 'conservative_bet_shortlist.csv', index=False)
            v28.cagey_tier_list(decisions).to_csv(raw / v28.TIER_FILE, index=False)
            (raw / 'conservative_bet_summary.json').write_text(json.dumps(summary, default=str), encoding='utf-8')
            process_conservative_shortlist(raw, out)
            report = (out / 'conservative_bet_shortlist_report.md').read_text(encoding='utf-8')
            tier = pd.read_csv(out / 'cagey_tier_shortlist_readable.csv')
        self.assertIn('price edge vs Pinnacle (v28)', report)
        self.assertIn('## Cagey tier (separate list', report)
        self.assertEqual(len(tier), 1)
        for column in ('Full win', 'Half win', 'Push', 'Half loss', 'Full loss', 'Profit probability',
                       'Uncorrected fair odds', 'Corrected fair odds'):
            self.assertIn(column, tier.columns)
            self.assertIn(column, report)
        # Narrow-margin columns follow the corrected cagey score; no monitoring file -> shown as missing.
        import narrow_margin_report as nmr
        names = list(nmr.SHORTLIST_COLUMNS.values())
        start = list(tier.columns).index('Corrected cagey score') + 1
        self.assertEqual(list(tier.columns[start:start + len(names)]), names)
        self.assertEqual(set(tier.iloc[0][names]), {'—'})

    def test_formatter_adds_narrow_margin_columns_from_the_same_run(self):
        import tempfile
        from pathlib import Path
        from format_football_output import process_conservative_shortlist
        import narrow_margin_report as nmr
        fair, _ = tier_fair(cagey_row(), 'away', 2.0)
        data = cagey_row(offers=[offer('away', 2.0, round(fair['corrected_fair_odds'] * 1.005, 4))])
        monitor = []
        selected, decisions, summary = run(data, monitor=monitor)
        tier_raw = v28.cagey_tier_list(decisions)
        pick = tier_raw.iloc[0]
        p2 = float(pick.corrected_cagey_score)
        record = next(r for r in monitor if r['home_team'] == pick.home_team)
        with tempfile.TemporaryDirectory() as tmp:
            raw, out = Path(tmp) / 'raw', Path(tmp) / 'readable'
            raw.mkdir()
            out.mkdir()
            selected.to_csv(raw / 'conservative_bet_shortlist.csv', index=False)
            tier_raw.to_csv(raw / v28.TIER_FILE, index=False)
            (raw / 'conservative_bet_summary.json').write_text(json.dumps(summary, default=str), encoding='utf-8')
            # The run's own monitoring records and forecast row, as the pipeline writes them.
            v28.write_monitoring(monitor, raw)
            pd.DataFrame([data]).to_csv(raw / nmr.PREDICTIONS, index=False)
            process_conservative_shortlist(raw, out)
            tier = pd.read_csv(out / 'cagey_tier_shortlist_readable.csv')
        row = tier.iloc[0]
        self.assertEqual(row['P(narrow: draw or 1-goal win)'], f'{100 * (1 - p2):.1f}%')
        self.assertEqual(row['P(margin 3+)'], f"{100 * record['corrected_p3']:.1f}%")
        self.assertEqual(row['Out of training domain'], 'no' if pick.league in nmr.TRAINED_LEAGUES else 'yes')
        for column in ('P(draw)', 'P(1-goal win)'):
            self.assertRegex(row[column], r'^\d+\.\d%$')
        # Information only: the tier's own decision columns are unchanged.
        self.assertEqual(row['Corrected cagey score'], f'{100 * p2:.1f}%')

    def test_switching_the_tier_off_clears_the_readable_list(self):
        import tempfile
        from pathlib import Path
        from format_football_output import process_conservative_shortlist
        fair, _ = tier_fair(cagey_row(), 'away', 2.0)
        data = cagey_row(offers=[offer('away', 2.0, round(fair['corrected_fair_odds'] * 1.005, 4))])
        readable_tier = 'cagey_tier_shortlist_readable.csv'
        with tempfile.TemporaryDirectory() as tmp:
            raw, out = Path(tmp) / 'raw', Path(tmp) / 'readable'
            raw.mkdir()
            out.mkdir()
            for settings, expected in ((None, True), (VALUE_ONLY, False), (None, True), (OFF, False)):
                selected, decisions, summary = run(data, settings=settings)
                selected.to_csv(raw / 'conservative_bet_shortlist.csv', index=False)
                v28.cagey_tier_list(decisions).to_csv(raw / v28.TIER_FILE, index=False)
                (raw / 'conservative_bet_summary.json').write_text(json.dumps(summary, default=str), encoding='utf-8')
                process_conservative_shortlist(raw, out)
                with self.subTest(settings=settings):
                    self.assertEqual((out / readable_tier).exists(), expected)
                    if expected:
                        self.assertEqual(len(pd.read_csv(out / readable_tier)), 1)
            (raw / 'conservative_bet_shortlist.csv').unlink()
            process_conservative_shortlist(raw, out)
            self.assertFalse((out / readable_tier).exists())


if __name__ == '__main__':
    unittest.main()
