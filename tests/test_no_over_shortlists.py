"""Live Over 1.5 exclusions must not rewrite archived decisions or predictions."""
import json
import tempfile
from pathlib import Path
import pandas as pd
from offline_test_case import OfflineQuotePolicyTestCase
import price_edge_cagey_shortlist as v28
import master_shortlist as master
import master_selection_ah as v6
import master_selection_no_totals as v7
from test_cagey_tier_v3 import sample, run, SETTINGS
from test_master_market_selection import candidate
from test_value_per_market import fixture


class NoOverShortlistTests(OfflineQuotePolicyTestCase):
    def test_exclusion_rejects_value_and_cagey_before_selection_without_changing_probabilities(self):
        settings={**SETTINGS,'cagey_tier_rule':v28.TIER_RULE_MARKET_BASIS}
        row=sample(); original=json.dumps(row,sort_keys=True)
        old,old_decisions,old_summary=run(row,settings=settings)
        new,decisions,summary=run(row,settings={**settings,'excluded_markets':['Over 1.5']})
        self.assertIn('Over 1.5',old.market.tolist())
        self.assertIn('Over 1.5',v28.cagey_tier_list(old_decisions).market.tolist())
        self.assertNotIn('Over 1.5',new.market.tolist())
        self.assertNotIn('Over 1.5',v28.cagey_tier_list(decisions).market.tolist())
        totals=decisions.loc[decisions.market.eq('Over 1.5')]
        self.assertGreater(len(totals),0)
        self.assertTrue(totals.decision.eq('REJECTED').all())
        self.assertTrue(totals.cagey_tier_decision.eq('REJECTED').all())
        self.assertTrue(totals.rejection_reasons.str.contains('market excluded').all())
        self.assertNotIn('Over 1.5',summary['eligible_markets'])
        self.assertNotIn('over_1_5',summary['value_market_groups'])
        self.assertEqual(summary['excluded_markets'],['Over 1.5'])
        self.assertNotIn('excluded_markets',old_summary)
        self.assertEqual(json.dumps(row,sort_keys=True),original)
        # All researched probabilities survive untouched, including those on rejected totals.
        pd.testing.assert_series_equal(old_decisions.research_p_win,decisions.research_p_win)
        pd.testing.assert_series_equal(old_decisions.corrected_p_profit,decisions.corrected_p_profit)
        replay,_,replayed=run(row,settings={**settings,'excluded_markets':None})
        pd.testing.assert_frame_equal(replay,old)
        self.assertEqual(replayed,old_summary)

    def test_live_config_excludes_over_and_master_has_explicit_version(self):
        self.assertEqual(v28.load_settings()['excluded_markets'],
                         ['Double Chance 12', 'Draw No Bet Away', 'Draw No Bet Home', 'Over 1.5'])
        self.assertEqual(master.configured_version(),master.VERSION_PINNACLE_MARKETS)
        for invalid in ['Over 1.5',[None],[''],{}]:
            with self.subTest(invalid=invalid), self.assertRaises(ValueError):
                v28.excluded_markets({'excluded_markets':invalid})

    def test_master_defence_refills_ten_distinct_matches_and_preserves_v6_replay(self):
        rows=[];pred=[]
        for i in range(12):
            home=f'Home {i}'
            alt=candidate(home=home,market='Home win',price=1.9)
            alt['value_market_group']='match_winner'
            rows.extend([candidate(home=home),alt])
            pred.append(dict(fixture(),home_team=home,fixture_id='f-'+home))
        decisions=pd.DataFrame(rows);predictions=pd.DataFrame(pred)
        old=master.build(decisions,predictions,master.VERSION_AH)
        self.assertTrue(old.market.eq('Over 1.5').all())
        audit=v7.evaluate(decisions,predictions)
        self.assertTrue(audit.loc[audit.market.eq('Over 1.5'),'master_decision'].eq('EXCLUDED').all())
        top=master.build(decisions,predictions,master.VERSION_NO_TOTALS)
        self.assertEqual(len(top),10)
        self.assertEqual(top.home_team.nunique(),10)
        self.assertTrue(top.market.eq('Home win').all())
        self.assertEqual(v7.summary(top)['shortfall'],0)
        self.assertTrue(top.master_suggested_stake.eq(0).all())
        self.assertTrue(master.matches(top,top))
        pd.testing.assert_frame_equal(old,master.build(decisions,predictions,master.VERSION_AH))
        # select itself also blocks a pre-existing eligible v6 audit.
        self.assertTrue(v7.select(v6.evaluate(decisions,predictions)).market.eq('Home win').all())

    def test_empty_master_keeps_v7_version_and_readable_exclusion(self):
        from format_football_output import master_section
        from test_master_market_selection import NOW
        d=pd.DataFrame([candidate()]);pred=pd.DataFrame([fixture()])
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);info={'generated_at_utc':NOW.isoformat()}
            top=master.write(d,root,info,pred,version=master.VERSION_NO_TOTALS)
            self.assertTrue(top.empty)
            self.assertEqual(master.summary(top)['version'],v7.VERSION)
            text=' '.join(master_section(info,root,root))
            self.assertIn('Over 1.5 is excluded',text)
            self.assertIn('Over 1.5',info['master_shortlist']['excluded_markets'])
            self.assertTrue(master.matches(top,master.build(d,pred,master.VERSION_NO_TOTALS)))
