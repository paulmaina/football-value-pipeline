"""Consensus master nominates ten executable fixtures, flags negative EV and never invents evidence."""
import json
import tempfile
from pathlib import Path
from unittest.mock import patch
import numpy as np
import pandas as pd
from offline_test_case import OfflineQuotePolicyTestCase
import master_shortlist as ms
from master_switch import switched
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
        research_summary=json.dumps({'home':{'all':{'matches':10}},'away':{'all':{'matches':10}}}),
        corrected_input_timing_status='SYNCHRONIZED',
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

    def test_ten_nominations_even_with_negative_ev_and_explicit_shortfall(self):
        rows=[candidate(str(i),price=1.3) for i in range(15)]
        top=selection.select(evaluate(*rows))
        self.assertEqual(len(top),10)
        watch=evaluate(candidate(price=1.3))
        self.assertEqual(watch.iloc[0].master_decision,'ELIGIBLE')
        self.assertIn('negative',watch.iloc[0].master_price_flag)
        self.assertEqual(len(selection.select(watch)),1)
        self.assertEqual(selection.summary(top)['negative_ev_bets'],10)
        self.assertEqual(selection.summary(top)['shortfall'],0)
        self.assertEqual(selection.summary(selection.select(watch))['shortfall'],9)
        self.assertEqual(len(selection.select(evaluate(candidate()))),1)

    def test_reject_missing_future_stale_and_out_of_window_inputs(self):
        bad=[{'offered_decimal_odds':None},{'offered_decimal_odds':1.15},{'offered_decimal_odds':2.01},
            {'per_stake_cost':None},{'per_stake_cost':-1},{'kickoff_utc':None},
            {'offered_last_update_utc':None},
            {'offered_last_update_utc':(NOW+pd.Timedelta(seconds=1)).isoformat()},
            {'offered_last_update_utc':(NOW-pd.Timedelta(minutes=16)).isoformat()},
            {'kickoff_utc':(NOW+pd.Timedelta(minutes=19)).isoformat()},
            {'kickoff_utc':(NOW+pd.Timedelta(hours=49)).isoformat()},
            {'home_team':''}]
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
        self.assertEqual(list(top.home_team),['B','A'])
        refund_heavy=top.loc[top.home_team.eq('A')].iloc[0]
        self.assertAlmostEqual(refund_heavy.master_profit_probability,.65)
        self.assertAlmostEqual(refund_heavy.master_no_loss_probability,.9)
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

    def test_model_disagreement_is_a_diagnostic_not_a_missing_evidence_ranking_advantage(self):
        a=candidate('Optimistic',price=1.3);b=candidate('Agreement',price=1.3)
        for row,prob in [(a,.65),(b,.79)]:
            row.update({'research_p_'+k:p for k,p in zip(selection.KINDS,[prob,0,0,0,1-prob])})
        first=evaluate(a,mass=(.85,0,0,0,.15))
        second=evaluate(b,mass=(.8,0,0,0,.2))
        top=selection.select(pd.concat([first,second]))
        self.assertEqual(top.home_team.tolist(),['Optimistic','Agreement'])
        self.assertAlmostEqual(first.iloc[0].master_no_loss_probability,.85)
        self.assertAlmostEqual(first.iloc[0].master_consensus_no_loss,.65)
        self.assertEqual(first.iloc[0].master_evidence_count,2)
        self.assertEqual(first.iloc[0].master_consensus_sources,'market + research')
        self.assertIn('not confidence bounds',first.iloc[0].master_coverage_warning)

    def test_unvalidated_totals_correction_and_ambiguous_research_do_not_drive_rank(self):
        r=candidate()
        for prefix,prob in [('research',.73),('corrected',.4)]:
            r.update({prefix+'_p_'+k:p for k,p in zip(selection.KINDS,[prob,0,0,0,1-prob])})
        row=evaluate(r).iloc[0]
        self.assertAlmostEqual(row.master_corrected_profit_probability,.4)
        self.assertAlmostEqual(row.master_consensus_profit,.73)
        self.assertNotIn('corrected',row.master_consensus_sources)
        r['research_warnings']='free-source fixture identity missing or ambiguous'
        row=evaluate(r).iloc[0]
        self.assertEqual(row.master_decision,'ELIGIBLE')
        self.assertAlmostEqual(row.master_consensus_profit,.75)
        self.assertEqual(row.master_evidence_count,1)
        self.assertIn('coverage insufficient',row.master_coverage_warning)
        r['market']=r['market_to_bet']='Home win'
        r['corrected_input_timing_status']='UNAVAILABLE_OR_UNSYNCHRONIZED'
        self.assertEqual(evaluate(r).iloc[0].master_evidence_count,1)

    def test_insufficient_distinct_fixtures_reports_shortfall_without_reusing_match(self):
        top=selection.select(evaluate(*[candidate(price=1.3) for _ in range(20)]))
        self.assertEqual(len(top),1)
        self.assertEqual(selection.summary(top)['shortfall'],9)
        unsafe=evaluate(candidate())
        unsafe['master_decision']='EXCLUDED'
        empty=selection.select(unsafe)
        self.assertEqual(selection.summary(empty)['shortfall'],10)

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
            info['input_stamps']['h2h']=(NOW-pd.Timedelta(minutes=16) if stale else NOW).isoformat()
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

    @switched('old')  # pre-release behaviour: the rollback state (master_shortlist_config.json live "old")
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
            self.assertNotIn('Over 1.5',result.market.tolist())
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

    def test_fifteen_minute_quotes_are_allowed_and_require_price_recheck(self):
        from test_price_edge_shortlist import FRESH
        for age in (6.5,8,15):
            r=candidate()
            stamp=(NOW-pd.Timedelta(minutes=age)).isoformat()
            r['offered_last_update_utc']=stamp
            pred=fixture(over_1xbet(1.4,stamp=stamp))
            quotes=json.loads(pred['price_edge_quotes'])
            for q in quotes:
                q['last_update_utc']=stamp
            pred['price_edge_quotes']=json.dumps(quotes)
            out=selection.evaluate(pd.DataFrame([r]),pd.DataFrame([pred])).iloc[0]
            self.assertEqual(out.master_decision,'ELIGIBLE')
            self.assertAlmostEqual(out.master_offer_age_minutes,age)
            self.assertAlmostEqual(out.master_reference_age_minutes,age)
            self.assertTrue(out.master_price_recheck_required)
            self.assertEqual(out.master_freshness_status,'RECHECK_PRICE')
        r=candidate();r['offered_last_update_utc']=(NOW-pd.Timedelta(minutes=15,seconds=1)).isoformat()
        self.assertEqual(evaluate(r).iloc[0].master_decision,'EXCLUDED')

    def test_missing_models_cannot_improve_rank_and_refunds_are_never_profit(self):
        a,b=candidate('A'),candidate('B')
        for k,p in zip(selection.KINDS,[.5,0,0,0,.5]):
            a['research_p_'+k]=p
        complete=selection.select(evaluate(a,b))
        without=selection.select(evaluate(candidate('A'),b))
        self.assertEqual(complete.home_team.tolist(),without.home_team.tolist())
        self.assertEqual(complete.master_profit_probability.tolist(),without.master_profit_probability.tolist())
        self.assertAlmostEqual(complete.iloc[0].master_model_gap,.25)
        self.assertTrue(without.master_price_recheck_required.all())

    def test_clock_mismatch_fails_loudly_before_any_file_is_written(self):
        r=candidate();d=pd.DataFrame([r]);p=forecasts(r)
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            for stamp in (None,(NOW+pd.Timedelta(seconds=1)).isoformat()):
                with self.subTest(stamp=stamp),self.assertRaisesRegex(ValueError,'clock'):
                    ms.write(d,root,{'generated_at_utc':stamp},p,version=ms.VERSION_MARKET)
                self.assertFalse((root/ms.FILE).exists())
                self.assertFalse((root/selection.AUDIT_FILE).exists())
            clock=selection.require_generation_clock(d,NOW.isoformat())
            self.assertEqual(clock,NOW)
            with patch.object(selection,'_reference',return_value=([.75,0,0,0,.25],'test',NOW.isoformat())):
                live=ms.write(d,root,{'generated_at_utc':NOW.isoformat()},p,version=ms.VERSION_MARKET)
                replay=ms.build(d,p,ms.VERSION_MARKET)
            self.assertTrue(ms.matches(live,replay,ms.VERSION_MARKET))

    def test_live_config_is_explicit_and_replay_ignores_it(self):
        r=candidate();r.update(edge=.05,fair_odds=1.3333333333333333,reference_type='a',pinnacle_no_loss_probability=.75)
        d=pd.DataFrame([r]);p=forecasts(r)
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);config=root/'master.json'
            config.write_text(json.dumps({'version':ms.VERSION}),encoding='utf-8')
            with patch.object(ms,'CONFIG',config):
                self.assertEqual(ms.configured_version(),ms.VERSION)
                # Presence of a research column never chooses the live rule.
                with patch.object(ms,'build',wraps=ms.build) as builder:
                    ms.write(d,root,{'generated_at_utc':NOW.isoformat()},p)
                    self.assertEqual(builder.call_args.args[2],ms.VERSION)
                with patch.object(selection,'_reference',return_value=([.75,0,0,0,.25],'test',NOW.isoformat())):
                    replay=ms.build(d,p,ms.VERSION_MARKET)
                self.assertEqual(replay.master_version.iloc[0],ms.VERSION_MARKET)
                config.write_text(json.dumps({'version':'unknown'}),encoding='utf-8')
                with self.assertRaisesRegex(ValueError,'configured'):
                    ms.write(d,root,{'generated_at_utc':NOW.isoformat()},p)

    def test_versions_replay_and_readable_bind_new_fields(self):
        from format_football_output import master_section
        r=candidate();decisions=pd.DataFrame([r]);pred=forecasts(r)
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);summary={'generated_at_utc':NOW.isoformat()}
            with patch.object(selection,'_reference',return_value=([.75,0,0,0,.25],'test',NOW.isoformat())):
                written=ms.write(decisions,root,summary,pred,version=ms.VERSION_MARKET)
                expected=ms.build(decisions,pred,ms.VERSION_MARKET)
            self.assertTrue(ms.matches(written,expected,ms.VERSION_MARKET))
            bad=written.copy();bad['master_p_push']=.5
            self.assertFalse(ms.matches(bad,expected,ms.VERSION_MARKET))
            self.assertTrue((root/selection.AUDIT_FILE).exists())
            lines=master_section(summary,root,root)
            readable=pd.read_csv(root/'master_shortlist_readable.csv')
            self.assertIn('Chance of positive return',readable)
            self.assertIn('Suggested stake',readable)
            self.assertIn('10 profit-first nominations',' '.join(lines))
            self.assertEqual(summary['master_shortlist']['version'],ms.VERSION_MARKET)
            self.assertTrue(ms.summary(written)['automatic_staking'] is False)
        self.assertIn(ms.VERSION,ms.VERSIONS)
        self.assertIn(ms.VERSION_V1,ms.VERSIONS)
