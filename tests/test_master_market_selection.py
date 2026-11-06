"""Market-first master selection never fills ten with unsupported/negative-EV picks."""
import json
import tempfile
from pathlib import Path
from unittest.mock import patch
import numpy as np
import pandas as pd
from offline_test_case import OfflineQuotePolicyTestCase
import master_shortlist as ms
import master_selection as selection
from test_price_edge_shortlist import NOW
from test_value_per_market import fixture, over_1xbet


def candidate(home='Home FC', market='Over 1.5', price=1.4, **kw):
    return dict(league='Premier League', home_team=home, away_team='Away FC',
        kickoff_utc=(NOW+pd.Timedelta(hours=24)).isoformat(), evaluated_at_utc=NOW.isoformat(),
        fixture_id='f-'+home, market=market, market_to_bet=market, bookmaker='1xBet',
        offered_decimal_odds=price, offered_last_update_utc=(NOW-pd.Timedelta(minutes=1)).isoformat(),
        per_stake_cost=0., decision='SHORTLISTED', cagey_tier_decision='SHORTLISTED',
        research_probability_basis='team_form_poisson_v1', value_market_group='over_1_5',
        selection_policy_version='48h-ah-price-edge-cagey-v28', **kw)


def forecasts(*rows):
    return pd.DataFrame([dict(league=r['league'], home_team=r['home_team'], away_team=r['away_team'],
        kickoff_utc=r['kickoff_utc'], odds_event_id='event-'+r['home_team']) for r in rows]).drop_duplicates()


def evaluate(*rows, mass=(.75,0,0,0,.25), now=None):
    with patch.object(selection,'_reference',return_value=(mass,'test uncorrected market',NOW.isoformat())):
        return selection.evaluate(pd.DataFrame(rows),forecasts(*rows),now)


class MarketSelectionTests(OfflineQuotePolicyTestCase):
    def test_exact_settlement_and_minimum_price_for_quarter_line_and_cost(self):
        mass=[.5,.2,.1,.1,.1]
        m=selection.settlement(mass,1.5,.01)
        self.assertAlmostEqual(m['ev'],.14)
        self.assertAlmostEqual(m['profit'],.7)
        self.assertAlmostEqual(m['no_loss'],.7) # cost makes push a net loss
        self.assertAlmostEqual(selection.settlement(mass,m['minimum'],.01)['ev'],.02)
        self.assertAlmostEqual(selection.settlement([.7,0,.2,0,.1],1.3,0)['ev'],.11)

    def test_invalid_distributions_fail_closed(self):
        for mass in ([.5,0,0,0,.4],[-.1,0,0,0,1.1],[np.nan,0,0,0,1],[0,0,1,0,0]):
            with self.subTest(mass=mass),self.assertRaises(ValueError):
                selection.settlement(mass,1.5,0)

    def test_union_only_and_one_per_match_with_no_overlap_bonus(self):
        a=candidate(); b=candidate(market='Double Chance 1X',price=1.5)
        c=candidate('Unselected');c.update(decision='NOT_SELECTED',cagey_tier_decision='NOT_SELECTED')
        frame=evaluate(a,b,c)
        self.assertEqual(len(frame),2)
        top=selection.select(frame)
        self.assertEqual(len(top),1)
        self.assertEqual(top.iloc[0].market,'Double Chance 1X')
        self.assertTrue(top.iloc[0].in_value_shortlist)
        self.assertTrue(top.iloc[0].in_cagey_tier)
        self.assertEqual(top.iloc[0].master_suggested_stake,0)

    def test_watchlist_never_fills_the_master_and_ten_is_maximum(self):
        rows=[candidate(str(i)) for i in range(15)]
        top=selection.select(evaluate(*rows))
        self.assertEqual(len(top),10)
        watch=evaluate(candidate(price=1.3))
        self.assertEqual(watch.iloc[0].master_decision,'WATCHLIST')
        self.assertTrue(selection.select(watch).empty)
        self.assertEqual(len(selection.select(evaluate(candidate()))),1)

    def test_reject_missing_future_stale_and_out_of_window_inputs(self):
        bad=[{'offered_decimal_odds':None},{'offered_decimal_odds':1.15},{'offered_decimal_odds':2.01},
            {'per_stake_cost':None},{'per_stake_cost':-1},{'kickoff_utc':None},
            {'offered_last_update_utc':None},
            {'offered_last_update_utc':(NOW+pd.Timedelta(seconds=1)).isoformat()},
            {'offered_last_update_utc':(NOW-pd.Timedelta(minutes=7)).isoformat()},
            {'kickoff_utc':(NOW+pd.Timedelta(minutes=19)).isoformat()},
            {'kickoff_utc':(NOW+pd.Timedelta(hours=49)).isoformat()},
            {'home_team':''},{'research_warnings':'free-source fixture identity missing or ambiguous'}]
        for changes in bad:
            r=candidate();r.update(changes)
            with self.subTest(changes=changes):
                out=evaluate(r)
                self.assertEqual(out.iloc[0].master_decision,'EXCLUDED')
                self.assertTrue(out.iloc[0].master_rejection_reasons)
        self.assertEqual(evaluate(candidate(),now=NOW+pd.Timedelta(hours=1)).iloc[0].master_decision,'EXCLUDED')
        a,b=candidate(),candidate('Other');b['evaluated_at_utc']=(NOW-pd.Timedelta(minutes=1)).isoformat()
        self.assertTrue(evaluate(a,b).master_decision.eq('EXCLUDED').all())

    def test_no_reference_or_ambiguous_prediction_never_falls_back(self):
        r=candidate()
        with patch.object(selection,'_reference',side_effect=ValueError('unavailable')):
            out=selection.evaluate(pd.DataFrame([r]),forecasts(r))
        self.assertEqual(out.iloc[0].master_decision,'EXCLUDED')
        for pred in (None,pd.concat([forecasts(r),forecasts(r)])):
            out=selection.evaluate(pd.DataFrame([r]),pred)
            self.assertEqual(out.iloc[0].master_decision,'EXCLUDED')

    def test_ranking_distinguishes_profit_from_push_and_best_price(self):
        a=evaluate(candidate('A',price=1.25),mass=(.65,0,.25,0,.1))
        b=evaluate(candidate('B',price=1.25),mass=(.85,0,0,0,.15))
        top=selection.select(pd.concat([a,b]))
        self.assertEqual(list(top.home_team),['A','B'])
        self.assertAlmostEqual(top.iloc[0].master_profit_probability,.65)
        self.assertAlmostEqual(top.iloc[0].master_no_loss_probability,.9)
        low=candidate(price=1.4);high=candidate(price=1.45);high['bookmaker']='Pinnacle'
        self.assertEqual(selection.select(evaluate(low,high)).iloc[0].bookmaker,'Pinnacle')

    def test_corrected_and_research_are_diagnostics_not_fallbacks(self):
        r=candidate()
        r.update({prefix+'_p_'+k:p for prefix in ('research','corrected')
                  for k,p in zip(selection.KINDS,[.99,0,0,0,.01])})
        out=evaluate(r)
        self.assertAlmostEqual(out.iloc[0].master_profit_probability,.75)
        self.assertAlmostEqual(out.iloc[0].master_model_gap,.24)
        self.assertIn('disagreement',out.iloc[0].master_coverage_warning)
        r['corrected_p_loss']=.5
        self.assertIn('invalid',evaluate(r).iloc[0].master_coverage_warning)

    def test_binary_reference_uses_fresh_independent_pair(self):
        r=candidate()
        pred=fixture(over_1xbet(1.4))
        out=selection.evaluate(pd.DataFrame([r]),pd.DataFrame([pred]))
        self.assertEqual(out.iloc[0].master_decision,'ELIGIBLE')
        self.assertAlmostEqual(out.iloc[0].master_profit_probability,.75,places=4)
        self.assertIn('margin-free Over 1.5',out.iloc[0].master_probability_basis)
        quotes=json.loads(pred['price_edge_quotes'])
        pred['price_edge_quotes']=json.dumps([q for q in quotes if q.get('point')!=1.5])
        out=selection.evaluate(pd.DataFrame([r]),pd.DataFrame([pred]))
        self.assertEqual(out.iloc[0].master_decision,'EXCLUDED')

    def test_asian_handicap_uses_only_uncorrected_fit_b(self):
        from types import SimpleNamespace
        r=candidate(market='Asian Handicap Home +1.00',price=1.3)
        r.update(handicap_side='home',handicap_line=1.)
        matrix=np.zeros((3,3));matrix[1,0]=.7;matrix[0,1]=.2;matrix[0,2]=.1
        fit=SimpleNamespace(usable=True,kind='B',matrix=matrix)
        info={'input_stamps':{'h2h':NOW.isoformat(),'ou25':NOW.isoformat(),'ah_main':NOW.isoformat()}}
        with patch('price_edge_shortlist.market_fit',return_value=(fit,info)):
            out=selection.evaluate(pd.DataFrame([r]),forecasts(r))
        self.assertEqual(out.iloc[0].master_decision,'ELIGIBLE')
        self.assertAlmostEqual(out.iloc[0].master_expected_return,.11)
        self.assertAlmostEqual(out.iloc[0].master_profit_probability,.7)
        self.assertAlmostEqual(out.iloc[0].master_no_loss_probability,.9)
        for kind,stale in [('A',False),('B',True)]:
            fit.kind=kind
            info['input_stamps']['h2h']=(NOW-pd.Timedelta(minutes=7) if stale else NOW).isoformat()
            with patch('price_edge_shortlist.market_fit',return_value=(fit,info)):
                bad=selection.evaluate(pd.DataFrame([r]),forecasts(r))
            self.assertEqual(bad.iloc[0].master_decision,'EXCLUDED')

    def test_real_fit_b_and_future_quote_leakage(self):
        from market_implied import dixon_coles_matrix, margin_distribution
        from narrow_margin import price_distribution
        from test_price_edge_shortlist import LAMBDAS
        r=candidate(market='Asian Handicap Home +1.00')
        r.update(handicap_side='home',handicap_line=1.)
        margins,mass=margin_distribution(dixon_coles_matrix(*LAMBDAS))
        fair=price_distribution(margins,mass,'home',1.)['fair_odds']
        r['offered_decimal_odds']=fair*1.05
        pred=fixture()
        result=selection.evaluate(pd.DataFrame([r]),pd.DataFrame([pred]))
        self.assertEqual(result.iloc[0].master_decision,'ELIGIBLE')
        self.assertEqual(result.iloc[0].master_probability_basis,'uncorrected Pinnacle fit B')
        old=result.iloc[0].master_profit_probability
        # Research changes do not move the master probability.
        r.update(research_p_win=.99,research_p_half_win=0,research_p_push=0,research_p_half_loss=0,research_p_loss=.01)
        self.assertAlmostEqual(selection.evaluate(pd.DataFrame([r]),pd.DataFrame([pred])).iloc[0].master_profit_probability,old)
        quotes=json.loads(pred['price_edge_quotes'])
        quotes[0]['last_update_utc']=(NOW+pd.Timedelta(seconds=1)).isoformat()
        pred['price_edge_quotes']=json.dumps(quotes)
        self.assertEqual(selection.evaluate(pd.DataFrame([r]),pd.DataFrame([pred])).iloc[0].master_decision,'EXCLUDED')

    def test_pipeline_replay_checks_the_master_and_audit(self):
        from test_local_research_v2 import row_with_evidence, SETTINGS
        from test_value_per_market import run
        from workflow_checks import raw_check
        from pipeline_health import write_generation_metadata
        import price_edge_cagey_shortlist as v28
        pred=row_with_evidence()
        quotes=json.loads(pred['price_edge_quotes'])
        # A genuine offered total with positive independent market EV.
        quotes.append(json.loads(fixture(over_1xbet(1.4))['price_edge_quotes'])[-1])
        pred['price_edge_quotes']=json.dumps(quotes)
        forecasts_frame=pd.DataFrame([pred])
        selected,decisions,info=run(pred,settings=SETTINGS)
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);raw=root/'raw';raw.mkdir()
            forecasts_frame.to_csv(raw/'all_leagues_predictions.csv',index=False)
            selected.to_csv(raw/'conservative_bet_shortlist.csv',index=False)
            decisions.to_csv(raw/'conservative_bet_rejections.csv',index=False)
            v28.cagey_tier_list(decisions).to_csv(raw/v28.TIER_FILE,index=False)
            result=ms.refresh(decisions,raw,info,forecasts_frame)
            self.assertIn('Over 1.5',result.market.tolist())
            (raw/'conservative_bet_summary.json').write_text(json.dumps(info),encoding='utf-8')
            write_generation_metadata(raw,info)
            self.assertEqual(raw_check(root)['selections'],len(selected))
            audit=pd.read_csv(raw/selection.AUDIT_FILE)
            audit['master_model_gap']=.999
            audit.to_csv(raw/selection.AUDIT_FILE,index=False)
            with self.assertRaisesRegex(ValueError,'master selection audit differs'):
                raw_check(root)

    def test_price_guard_cannot_use_research_fair_odds(self):
        r=candidate(price=1.7)
        r.update(fair_odds=1.1,edge=.5)
        out=evaluate(r)
        self.assertEqual(out.iloc[0].master_decision,'EXCLUDED')
        self.assertIn('independent',out.iloc[0].master_rejection_reasons)

    def test_versions_replay_and_readable_bind_new_fields(self):
        from format_football_output import master_section
        r=candidate();decisions=pd.DataFrame([r]);pred=forecasts(r)
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);summary={'generated_at_utc':NOW.isoformat()}
            with patch.object(selection,'_reference',return_value=([.75,0,0,0,.25],'test',NOW.isoformat())):
                written=ms.write(decisions,root,summary,pred)
                expected=ms.build(decisions,pred,ms.VERSION_MARKET)
            self.assertTrue(ms.matches(written,expected,ms.VERSION_MARKET))
            bad=written.copy();bad['master_p_push']=.5
            self.assertFalse(ms.matches(bad,expected,ms.VERSION_MARKET))
            self.assertTrue((root/selection.AUDIT_FILE).exists())
            lines=master_section(summary,root,root)
            readable=pd.read_csv(root/'master_shortlist_readable.csv')
            self.assertIn('Chance of positive return',readable)
            self.assertIn('Suggested stake',readable)
            self.assertIn('up to 10',' '.join(lines))
            self.assertEqual(summary['master_shortlist']['version'],ms.VERSION_MARKET)
            self.assertTrue(ms.summary(written)['automatic_staking'] is False)
        self.assertIn(ms.VERSION,ms.VERSIONS)
        self.assertIn(ms.VERSION_V1,ms.VERSIONS)
