"""Expanded cagey selection, common schemas, replay, staking and multi-pick tracking."""
import json
from pathlib import Path
import tempfile
from unittest.mock import patch

import numpy as np
import pandas as pd

from offline_test_case import OfflineQuotePolicyTestCase
from test_value_per_market import fixture, quote, offer, h2h_1xbet, over_1xbet, NOW, FRESH, POLICY
import cagey_tier_v3 as tier
import price_edge_cagey_shortlist as v28
import team_research as tr

SETTINGS = dict(cagey_correction_enabled=True, cagey_tier_enabled=True,
                cagey_tier_rule=tier.RULE, value_rule=v28.VALUE_RULE_LOCAL_RESEARCH,
                quote_timing_rule=v28.TIMING_RULE_CUTOFF)


def sample():
    data = fixture(h2h_1xbet(home=1.8, away=1.9),
        quote('double_chance', {'home_draw': 1.3, 'draw_away': 1.35, 'home_away': 1.3}, book='1xBet'),
        over_1xbet(1.3), offers=[offer('home', 1., 1.2), offer('away', 1.25, 1.2), offer('home', -.75, 1.9)])
    data.update(lambda_home=1.4, lambda_away=1.2, p_home=.4, p_draw=.3, p_away=.3, p_over_1_5=.7)
    data['team_research_json'] = json.dumps(tr.prepare(data, NOW))
    return data


def run(data=None, settings=SETTINGS):
    return v28.build_shortlist(pd.DataFrame([data or sample()]), NOW, execution_policy=POLICY, settings=settings)


def context():
    matrix = np.array([[.15, .20, .02], [.16, .18, .07], [.02, .06, .14]])
    margins = np.arange(-2, 3)
    delta = np.subtract.outer(np.arange(3), np.arange(3))
    probs = np.array([matrix[delta == m].sum() for m in margins])
    return dict(matrix=matrix, margins=margins, probs=probs, score=.33, fit='B', input_stamps=[FRESH])


def item(market='Home win', side='home', line=-.5, price=1.2):
    return dict(market=market, market_to_bet=market, handicap_side=side, handicap_line=line,
                offered_decimal_odds=price, offered_last_update_utc=FRESH, bookmaker='1xBet')


class ExpandedCageyTests(OfflineQuotePolicyTestCase):
    def test_corrected_grid_has_exact_margin_masses_and_preserves_conditionals(self):
        ctx = context(); raw = ctx['matrix']; ctx['probs'] = np.array([.08, .20, .43, .21, .08])
        result = tier.corrected_grid(ctx, raw)
        delta = np.subtract.outer(np.arange(3), np.arange(3))
        for margin, expected in zip(ctx['margins'], ctx['probs']):
            self.assertAlmostEqual(result[delta == margin].sum(), expected)
        self.assertAlmostEqual(result[0, 0]/result[1, 1], raw[0, 0]/raw[1, 1])
        self.assertAlmostEqual(result.sum(), 1)
        self.assertFalse(np.allclose(result, raw))
        with self.assertRaises(ValueError):
            tier.corrected_grid({**ctx, 'margins': [8], 'probs': [1.]}, raw)

    def test_all_market_probabilities_use_same_corrected_distribution(self):
        ctx = context(); row = sample()
        cases = [('Home win','home',-.5,.24), ('Away win','away',-.5,.29),
                 ('Double Chance 1X','home',.5,.71), ('Double Chance X2','away',.5,.76),
                 ('Double Chance 12',None,None,.53), ('Over 1.5',None,None,.49)]
        for market, side, line, expected in cases:
            candidate = item(market, side, line)
            tier.annotate(candidate, ctx, row, NOW, POLICY, 0.)
            self.assertAlmostEqual(candidate['corrected_p_win'], expected)
            self.assertEqual(candidate['cagey_tier_decision'], 'ELIGIBLE')
        candidate = item('Asian Handicap Home -0.75', 'home', -.75)
        tier.annotate(candidate, ctx, row, NOW, POLICY, 0.)
        self.assertAlmostEqual(candidate['corrected_p_half_win'], .22)
        self.assertAlmostEqual(candidate['corrected_p_win'], .02)

    def test_narrow_and_odds_boundaries(self):
        for score, accepted in [(.33, True), (.33001, False), (.32999, True)]:
            candidate = item()
            tier.annotate(candidate, {**context(), 'score': score}, sample(), NOW, POLICY, 0.)
            self.assertEqual(candidate['cagey_tier_decision'] == 'ELIGIBLE', accepted)
        for price, accepted in [(1.15, False), (1.150001, True), (2., True), (2.000001, False)]:
            candidate = item(price=price)
            tier.annotate(candidate, context(), sample(), NOW, POLICY, 0.)
            self.assertEqual(candidate['cagey_tier_decision'] == 'ELIGIBLE', accepted)

    def test_kickoff_boundaries_and_input_guards(self):
        for minutes, accepted in [(19.99,False),(20,True),(48*60,True),(48*60+.01,False)]:
            candidate = item()
            tier.annotate(candidate, context(), dict(sample(), kickoff_utc=(NOW+pd.Timedelta(minutes=minutes)).isoformat()), NOW, POLICY, 0.)
            self.assertEqual(candidate['cagey_tier_decision'] == 'ELIGIBLE', accepted)
        for stamp in ((NOW+pd.Timedelta(seconds=1)).isoformat(), (NOW-pd.Timedelta(hours=30)).isoformat(), None):
            candidate = item()
            tier.annotate(candidate, {**context(), 'input_stamps': [stamp]}, sample(), NOW, POLICY, 0.)
            self.assertEqual(candidate['cagey_tier_decision'], 'REJECTED')
        candidate=item();tier.annotate(candidate,None,sample(),NOW,POLICY,0.)
        self.assertIn('distribution unavailable', candidate['cagey_tier_reasons'])

    def test_no_ev_or_no_loss_floor_and_quarter_line_push_cost(self):
        candidate=item()
        tier.annotate(candidate, context(), sample(), NOW, POLICY, 0.)
        self.assertEqual(candidate['cagey_tier_decision'], 'ELIGIBLE')
        self.assertEqual(candidate['price_flag'], 'below fair')
        self.assertLess(candidate['corrected_no_loss_probability'], .85)
        candidate=item('Asian Handicap Home +1.00', 'home', 1., price=1.16)
        tier.annotate(candidate, context(), sample(), NOW, POLICY, 0.)
        safe=candidate['corrected_no_loss_probability']
        push=candidate['corrected_p_push']
        tier.annotate(candidate, context(), sample(), NOW, POLICY, .01)
        self.assertAlmostEqual(safe-candidate['corrected_no_loss_probability'], push)

    def test_four_groups_and_value_selection_remains_unchanged(self):
        selected, decisions, summary=run()
        picks=v28.cagey_tier_list(decisions)
        self.assertEqual(set(picks.value_market_group), set(v28.MARKET_GROUPS))
        self.assertEqual(len(picks), 4)
        self.assertTrue(picks.corrected_no_loss_probability.is_monotonic_decreasing)
        self.assertEqual(summary['cagey_tier']['rule_version'], tier.RULE)
        self.assertTrue(picks.source_probability_basis.eq(tier.BASIS).all())
        old, _, _=run(settings=dict(SETTINGS, cagey_tier_rule=v28.TIER_RULE_NARROW))
        self.assertEqual(list(zip(selected.market, selected.bookmaker)),list(zip(old.market, old.bookmaker)))
        np.testing.assert_allclose(selected.profit_probability,old.profit_probability)
        self.assertEqual(set(picks.shortlist_schema_version), {'comparable-shortlist-v1'})

    def test_safest_then_ev_then_odds_per_group_and_no_cap(self):
        _, decisions, _=run()
        rows=[]
        base=decisions[decisions.cagey_tier_decision.eq('SHORTLISTED')].iloc[0].to_dict()
        for i in range(15):
            for safe, ev, price in [(.8,.1,1.5),(.9,-.2,1.3),(.9,-.1,1.3),(.9,-.1,1.4)]:
                rows.append(dict(base,home_team=f'Team{i}',cagey_tier_decision='ELIGIBLE',
                    corrected_no_loss_probability=safe,corrected_expected_profit=ev,offered_decimal_odds=price))
        frame=pd.DataFrame(rows);tier.select(frame,pd.DataFrame())
        chosen=frame[frame.cagey_tier_decision.eq('SHORTLISTED')]
        self.assertEqual(len(chosen),15)
        self.assertTrue(chosen.offered_decimal_odds.eq(1.4).all())

    def test_stakes_and_tracking_preserve_all_new_groups_and_rule(self):
        import price_edge_tracking as tracking
        from staking import stake_recommendations
        _, decisions, _=run();picks=v28.cagey_tier_list(decisions)
        sized=stake_recommendations(picks,tier='cagey')
        self.assertTrue(sized.probability_basis.eq('corrected_matrix').all())
        self.assertFalse(sized.staking_status.str.contains('UNAVAILABLE').any())
        rows=picks.assign(snapshot_generated_utc=NOW.isoformat()).to_dict('records')
        old=dict(rows[0], snapshot_generated_utc=(NOW-pd.Timedelta(hours=1)).isoformat(),cagey_market_group='obsolete')
        with patch.object(tracking,'archived_tier_rows',return_value=[old,*rows,*rows]):
            result=tracking.frozen_tier_picks(Path('.'),[])
        self.assertEqual(len(result),4)
        split=tracking.tier_frame(pd.DataFrame(),pd.DataFrame(result))
        self.assertTrue(split.cagey_tier_rule.eq(tier.RULE).all())

    def test_weather_does_not_affect_selection_and_empty_outputs_keep_schema(self):
        plain, decisions, _=run()
        wet=dict(sample(), weather={'wind': 150, 'rain': 99})
        changed, wet_decisions, _=run(wet)
        self.assertEqual(v28.cagey_tier_list(decisions).market.tolist(),
                         v28.cagey_tier_list(wet_decisions).market.tolist())
        np.testing.assert_allclose(plain.chance_of_positive_return,changed.chance_of_positive_return)
        empty, rejected, _=run(dict(sample(),kickoff_utc=(NOW-pd.Timedelta(hours=1)).isoformat()))
        self.assertTrue(empty.empty)
        self.assertTrue(v28.cagey_tier_list(rejected).empty)
        self.assertIn('chance_of_no_loss',empty)
        self.assertIn('chance_of_no_loss',v28.cagey_tier_list(rejected))

    def test_readable_schema_and_offline_raw_replay(self):
        from workflow_checks import raw_check
        from pipeline_health import write_generation_metadata
        from format_football_output import process_conservative_shortlist
        import master_shortlist as master
        data=sample();monitor=[]
        selected, decisions, summary=v28.build_shortlist(pd.DataFrame([data]),NOW,execution_policy=POLICY,settings=SETTINGS,monitor=monitor)
        picks=v28.cagey_tier_list(decisions)
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);raw=root/'raw';raw.mkdir();out=root/'readable';out.mkdir()
            pd.DataFrame([data]).to_csv(raw/'all_leagues_predictions.csv',index=False)
            selected.to_csv(raw/'conservative_bet_shortlist.csv',index=False)
            selected.to_csv(raw/'conservative_strict_qualifiers.csv',index=False)
            decisions.to_csv(raw/'conservative_bet_rejections.csv',index=False)
            picks.to_csv(raw/v28.TIER_FILE,index=False)
            master.refresh(decisions,raw,summary,pd.DataFrame([data]))
            v28.record_monitoring(summary,monitor,raw)
            (raw/'conservative_bet_summary.json').write_text(json.dumps(summary),encoding='utf-8')
            write_generation_metadata(raw,summary)
            with patch('requests.sessions.Session.request',side_effect=AssertionError('replay must be offline')):
                raw_check(root)
            process_conservative_shortlist(raw,out)
            value=pd.read_csv(out/'conservative_bet_shortlist_readable.csv')
            cagey=pd.read_csv(out/'cagey_tier_shortlist_readable.csv')
            common=['Chance of no loss','Chance of positive return','Expected return after cost','Model fair odds after cost',
                    'Model price edge','Price assessment','Probability basis','Selection objective','Market group','Fixture key']
            self.assertTrue(set(common)<=set(value)&set(cagey))
            self.assertFalse(cagey.empty)
            self.assertEqual(list(value.columns[:len(cagey.columns)-1]),list(cagey.columns[:-1]))
