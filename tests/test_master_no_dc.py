"""DC replacements must be executable native AH offers, never renamed DC prices."""
import json
import tempfile
from pathlib import Path
from unittest.mock import patch
import pandas as pd
from offline_test_case import OfflineQuotePolicyTestCase
import master_selection as v5
import master_selection_ah as v6
import master_shortlist as master
from test_master_market_selection import candidate, forecasts, NOW
from test_price_edge_shortlist import offer
from test_value_per_market import fixture


def dc(market='Double Chance 1X',**kw):
    row=candidate(market=market,price=1.9)
    row.update(source_market='double_chance',value_market_group='double_chance',**kw)
    return row


def prediction(*offers):
    return fixture(offers=list(offers))


def native(side='home',price=1.4,**kw):
    o=offer(side,.5,price,book='Pinnacle',**kw)
    o['opposite_price']=3.2 if price >= 1.4 else 3.8
    return o


class NoDoubleChanceMasterTests(OfflineQuotePolicyTestCase):
    def test_1x_and_x2_become_actual_pinnacle_plus_half_quotes(self):
        for market,side in [('Double Chance 1X','home'),('Double Chance X2','away')]:
            r=dc(market);pred=prediction(native(side))
            with self.subTest(market=market):
                audit=v6.evaluate(pd.DataFrame([r]),pd.DataFrame([pred]))
                row=audit.iloc[0]
                self.assertEqual(row.master_decision,'ELIGIBLE')
                self.assertEqual(row.market,f'Asian Handicap {side.title()} +0.50')
                self.assertEqual(row.market_to_bet,row.market)
                self.assertEqual(row.handicap_side,side)
                self.assertEqual(row.handicap_line,.5)
                self.assertEqual(row.bookmaker,'Pinnacle')
                self.assertEqual(row.offered_decimal_odds,1.4)
                self.assertNotEqual(row.offered_decimal_odds,row.master_original_odds)
                self.assertEqual(row.value_market_group,'asian_handicap')
                self.assertEqual(row.master_original_market,market)
                self.assertEqual(row.master_replacement_status,'DC_TO_PINNACLE_AH')
                self.assertEqual(row.master_offer_source_market,'alternate_spreads')
                self.assertEqual(len(v6.select(audit)),1)
                # Equivalent regulation outcomes, priced again at the AH offer.
                self.assertAlmostEqual(row.master_expected_return,row.master_profit_probability*1.4-1)

    def test_no_dc_price_fallback_or_other_book_fallback(self):
        r=dc()
        cases=[[],[dict(native(),bookmaker='1xBet')],[dict(native(),opposite_price=None)],
               [dict(native(),opposite_price=1.1)],[dict(native(),market_key='draw_no_bet')],
               [dict(native(),line=1.)]]
        for offers in cases:
            with self.subTest(offers=offers):
                a=v6.evaluate(pd.DataFrame([r]),pd.DataFrame([prediction(*offers)]))
                self.assertEqual(a.iloc[0].master_decision,'EXCLUDED')
                self.assertIn('quote unavailable',a.iloc[0].master_rejection_reasons)
                self.assertTrue(v6.select(a).empty)

    def test_12_has_no_single_ah_equivalent_even_with_misleading_metadata(self):
        r=dc('Double Chance 12',handicap_side='home',handicap_line=.5)
        a=v6.evaluate(pd.DataFrame([r]),pd.DataFrame([prediction(native())]))
        self.assertEqual(a.iloc[0].master_decision,'EXCLUDED')
        self.assertIn('no equivalent',a.iloc[0].master_rejection_reasons)
        self.assertTrue(v6.select(a).empty)

    def test_replacement_runs_every_execution_guard(self):
        for updates in [dict(price=1.15,opposite_price=6.),dict(price=2.01,opposite_price=1.9),
            dict(last_update_utc=(NOW-pd.Timedelta(minutes=16)).isoformat()),
            dict(last_update_utc=(NOW+pd.Timedelta(seconds=1)).isoformat())]:
            o=native();o.update(updates)
            with self.subTest(updates=updates):
                a=v6.evaluate(pd.DataFrame([dc()]),pd.DataFrame([prediction(o)]))
                self.assertTrue(v6.select(a).empty)
                self.assertTrue(a.master_decision.eq('EXCLUDED').all())

    def test_valid_replacement_competes_against_other_markets_and_duplicates(self):
        r=dc();other=candidate(price=1.4)
        pred=prediction(native('home',1.3))
        # Native 1.3/+0.5 probability is only about 70%; total 1.5 probability is 75%.
        a=v6.evaluate(pd.DataFrame([r,other,dict(r)]),pd.DataFrame([pred]))
        top=v6.select(a)
        self.assertEqual(len(top),1)
        self.assertEqual(top.iloc[0].market,'Over 1.5')
        self.assertFalse(top.market.str.startswith('Double Chance ').any())

    def test_missing_ah_can_use_another_shortlisted_market_same_fixture(self):
        a=v6.evaluate(pd.DataFrame([dc(),candidate()]),pd.DataFrame([prediction()]))
        top=v6.select(a)
        self.assertEqual(len(top),1)
        self.assertEqual(top.iloc[0].market,'Over 1.5')
        self.assertEqual(v6.summary(top)['shortfall'],9)

    def test_choose_best_valid_native_quote_not_suspect_or_stale_highest(self):
        # Same side/line, fresh actual quote wins; invalid high offer is never used.
        bad=native(price=1.8);bad['opposite_price']=2.
        a=v6.evaluate(pd.DataFrame([dc()]),pd.DataFrame([prediction(native(),bad)]))
        top=v6.select(a)
        self.assertEqual(len(top),1)
        self.assertEqual(top.iloc[0].offered_decimal_odds,1.4)
        self.assertEqual(len(a),2)
        self.assertIn('suspected price error',a.iloc[1].master_rejection_reasons)

    def test_legacy_ah_label_with_dc_price_cannot_bypass_native_offer_check(self):
        r=dc();r.update(market='Asian Handicap Home +0.50',handicap_side='home',handicap_line=.5)
        a=v6.evaluate(pd.DataFrame([r]),pd.DataFrame([prediction()]))
        self.assertTrue(v6.select(a).empty)
        # Contradictory labels/metadata cannot authorize a different outcome.
        for label,side in [('Over 1.5','home'),('Asian Handicap Away +0.50','home')]:
            r.update(market=label,handicap_side=side)
            a=v6.evaluate(pd.DataFrame([r]),pd.DataFrame([prediction(native())]))
            self.assertTrue(v6.select(a).empty)

    def test_v5_archived_rule_and_schema_replay_unchanged(self):
        r=dc();r['offered_decimal_odds']=1.4
        pred=pd.DataFrame([prediction(native())]);d=pd.DataFrame([r])
        old=master.build(d,pred,master.VERSION_MARKET)
        new=master.build(d,pred,master.VERSION_AH)
        self.assertEqual(old.iloc[0].market,'Double Chance 1X')
        self.assertEqual(new.iloc[0].market,'Asian Handicap Home +0.50')
        self.assertEqual(list(old.columns),master.COLUMNS_V3)
        self.assertEqual(list(new.columns),master.COLUMNS_AH)
        self.assertEqual(old.iloc[0].master_version,v5.VERSION)
        self.assertEqual(new.iloc[0].master_version,v6.VERSION)
        self.assertTrue(master.matches(old,master.build(d,pred,master.VERSION_MARKET),master.VERSION_MARKET))

    def test_ten_distinct_matches_survive_dc_replacement_and_12_refill(self):
        rows=[];pred=[]
        for i in range(12):
            home=f'Team {i:02d}'
            r=dc('Double Chance 12' if i%3 == 0 else 'Double Chance 1X');r.update(home_team=home,fixture_id='f-'+home)
            alt=candidate(home=home,market='Home win',price=1.9)
            rows.extend([r,alt])
            pred.append(dict(prediction(native()),home_team=home,fixture_id='f-'+home))
        a=v6.evaluate(pd.DataFrame(rows),pd.DataFrame(pred))
        top=v6.select(a)
        self.assertEqual(len(top),10)
        self.assertEqual(top.home_team.nunique(),10)
        self.assertFalse(top.market.str.startswith('Double Chance ').any())
        self.assertEqual(v6.summary(top)['shortfall'],0)
        self.assertGreater(v6.summary(top)['converted_bets'],0)
        self.assertTrue(top.master_suggested_stake.eq(0).all())

    def test_converted_plus_half_grades_a_draw_as_a_win_not_a_push(self):
        import price_edge_tracking as tracking
        r=dc();pred=prediction(native())
        top=v6.select(v6.evaluate(pd.DataFrame([r]),pd.DataFrame([pred])))
        record=dict(league_code='PL',kickoff_utc=r['kickoff_utc'],home_team='Home FC',away_team='Away FC',
                    home_goals=0,away_goals=0,source='football-data.org/v4',source_status='FINISHED',
                    source_duration='REGULAR',match_id=1)
        grade=tracking.grade(top.to_dict('records'),[],[record],pd.Timestamp(r['kickoff_utc'])+pd.Timedelta(hours=3))
        self.assertEqual(grade.iloc[0].result_status,'WON')
        self.assertAlmostEqual(grade.iloc[0].unit_profit,.4)

    def test_write_readable_and_all_provenance_fields_are_replayed(self):
        from format_football_output import master_section
        d=pd.DataFrame([dc()]);pred=pd.DataFrame([prediction(native())])
        info={'generated_at_utc':NOW.isoformat()}
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            frame=master.write(d,root,info,pred)
            self.assertEqual(info['master_shortlist']['version'],v6.VERSION)
            self.assertEqual(info['master_shortlist']['converted_bets'],1)
            self.assertTrue(master.matches(frame,master.build(d,pred,master.VERSION_AH),master.VERSION_AH))
            for col in v6.EXTRA_COLUMNS:
                modified=frame.copy();modified[col]='tampered'
                self.assertFalse(master.matches(modified,frame,master.VERSION_AH))
            master_section(info,root,root)
            text=(root/'master_shortlist_readable.csv').read_text(encoding='utf-8-sig')
            self.assertIn('Original nominated market',text)
            self.assertIn('AH replacement status',text)
            self.assertIn('Asian Handicap Home +0.50',text)
            self.assertIn('Actual offered market type',text)
            audit=pd.read_csv(root/v6.AUDIT_FILE)
            self.assertEqual(audit.iloc[0].master_original_market,'Double Chance 1X')
