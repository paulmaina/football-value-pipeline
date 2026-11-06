"""Every captured generation is graded; placed bets are private and never inferred."""
import copy
import json
from pathlib import Path
import tempfile
from unittest.mock import patch
import pandas as pd
from offline_test_case import OfflineQuotePolicyTestCase
from test_price_edge_tracking import pick,meta,KICK,CLOCK,CAPTURED
import price_edge_tracking as tracking
import recommendation_history as history
import bet_ledger as ledger


def final(home='Home FC',away='Away FC'):
    return dict(league_code='PL',kickoff_utc=KICK.isoformat(),home_team=home,away_team=away,
                home_goals=2,away_goals=0,source='football-data.org/v4',source_status='FINISHED',
                source_duration='REGULAR',match_id=1)


def placed(**extra):
    return dict(bet_id='ticket-1',placed_at_utc=CAPTURED,recorded_at_utc=CAPTURED,
        league='Premier League',home_team='Home FC',away_team='Away FC',kickoff_utc=KICK.isoformat(),
        market='Over 1.5',bookmaker='1xBet',offered_decimal_odds=1.5,stake=100,currency='KES',per_stake_cost=0,**extra)


class HistoryTests(OfflineQuotePolicyTestCase):
    def test_dropped_and_replaced_picks_all_grade_once_per_generation(self):
        from cagey_tier_v3 import RULE_MARKET_BASIS
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);archive=[]
            early=(KICK-pd.Timedelta(hours=5)).isoformat();late=(KICK-pd.Timedelta(hours=2)).isoformat()
            for i,(generation,rows) in enumerate([(early,[pick(market='Over 1.5',price=1.2,value_market_group='over_1_5'),
                    pick(market='Double Chance 12',price=1.6,value_market_group='double_chance')]),
                    (late,[pick(market='Over 1.5',price=1.4,value_market_group='over_1_5')]),
                    (early,[pick(market='Over 1.5',price=1.2,value_market_group='over_1_5'),
                    pick(market='Double Chance 12',price=1.6,value_market_group='double_chance')])]):
                sha=str(i+1)*40;folder=root/'performance/snapshots'/sha[:16];folder.mkdir(parents=True)
                records=[dict(r,selection_policy_version=tracking.CAGEY_POLICY,cagey_market_group=r['value_market_group'],
                              cagey_tier_rule=RULE_MARKET_BASIS) for r in rows]
                pd.DataFrame(records).to_csv(folder/tracking.TIER_FILE,index=False)
                m={**meta(sha,[tracking.TIER_FILE]),'selection_policy_version':tracking.CAGEY_POLICY,
                   'captured_at_utc':generation,'generated_at_utc':generation}
                archive.append((m,[],records))
            latest=tracking.frozen_tier_picks(root,archive)
            self.assertEqual(len(latest),1)
            every=history.rows(root,archive)
            self.assertEqual(len(every),6)  # 3 distinct recommendations in EACH list, no re-upload duplicates.
            self.assertEqual(len({r['recommendation_id'] for r in every}),6)
            graded=tracking.grade(every,[],[final()],CLOCK)
            self.assertEqual(len(graded),6)
            self.assertTrue(graded.unit_profit.notna().all())
            summary=history.summarize(graded)
            self.assertEqual(summary['cagey']['recommendations'],3)
            self.assertEqual(summary['cagey']['distinct_fixtures'],1)
            self.assertIn('not actual',summary['note'])
            # Actual placed bets are not guessed from these records.
            self.assertEqual(ledger.review_private(root,[],[final()],CLOCK)['status'],'NOT_RECORDED')

    def test_late_capture_is_excluded_from_all_generation_history(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);sha='b'*40;folder=root/'performance/snapshots'/sha[:16];folder.mkdir(parents=True)
            row=pick(market='Over 1.5',price=1.4,value_market_group='over_1_5')
            pd.DataFrame([row]).to_csv(folder/tracking.TIER_FILE,index=False)
            stamp=(KICK-pd.Timedelta(minutes=5)).isoformat()
            m={**meta(sha,[tracking.TIER_FILE]),'captured_at_utc':stamp,'generated_at_utc':CAPTURED}
            self.assertEqual(history.rows(root,[(m,[],[row])]),[])

    def test_repeated_generations_reuse_verification_without_relaxing_identity(self):
        import performance_tracking as performance
        rows=[dict(pick(market='Over 1.5',price=1.4),snapshot_captured_utc=CAPTURED) for _ in range(5)]
        with patch.object(performance,'fixture_match',wraps=performance.fixture_match) as verify:
            result=tracking.grade(rows,[],[final()],CLOCK)
        self.assertEqual(len(result),5)
        self.assertEqual(verify.call_count,1)
        mixed=[rows[0],dict(rows[0],home_team='Different identity')]
        with patch.object(performance,'fixture_match',side_effect=[(final(),'VERIFIED_FINISHED'),(None,'UNVERIFIED')]) as verify:
            result=tracking.grade(mixed,[],[final()],CLOCK)
        self.assertEqual(verify.call_count,2)
        self.assertTrue(pd.isna(result.iloc[1].final_score))
        self.assertTrue(pd.isna(result.iloc[1].result_status))

    def test_review_exports_all_history_separately_from_latest(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);stamp=CAPTURED
            row={**pick(market='Over 1.5',price=1.4), 'snapshot_commit':'a'*40,
                 'snapshot_generated_utc':stamp,'snapshot_captured_utc':stamp,
                 'recommendation_tier':'cagey','recommendation_id':'id1'}
            with patch.object(history,'rows',return_value=[row]):
                summary=tracking.review(root,[],[final()],CLOCK)
            self.assertEqual(summary['frozen_picks'],0)
            self.assertEqual(summary['recommendation_history']['cagey']['graded'],1)
            out=pd.read_csv(root/tracking.OUTPUT_DIR/'all_recommendation_generations.csv')
            self.assertEqual(out.recommendation_id.tolist(),['id1'])
            self.assertEqual(summary['actual_bets']['status'],'NOT_RECORDED')
            self.assertIn('not executed-bet ROI',tracking.report(summary))


class PlacedBetTests(OfflineQuotePolicyTestCase):
    def test_actual_stake_and_entry_odds_grade_privately_with_verified_results(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);path=root/ledger.INPUT;ledger.write(path,ledger.validate([placed()]))
            public=ledger.review_private(root,[],[final()],CLOCK)
            self.assertEqual(public['status'],'AVAILABLE_PRIVATELY')
            self.assertNotIn('cash_profit',public)
            summary=json.loads((root/ledger.DIRECTORY/'summary.json').read_text())
            self.assertEqual(summary['by_currency']['KES']['graded_stake'],100)
            self.assertAlmostEqual(summary['by_currency']['KES']['cash_profit'],50)
            self.assertAlmostEqual(summary['by_currency']['KES']['roi'],.5)
            frame=pd.read_csv(root/ledger.DIRECTORY/'graded_bets.csv')
            self.assertEqual(frame.bet_id.tolist(),['ticket-1'])
            self.assertEqual(frame.cash_profit.tolist(),[50])
            # Unverified/missing results remain pending, not a zero-profit bet in ROI.
            ledger.review_private(root,[],[],CLOCK)
            pending=json.loads((root/ledger.DIRECTORY/'summary.json').read_text())
            self.assertEqual(pending['graded'],0)
            self.assertEqual(pending['by_currency'],{})

    def test_bad_and_duplicate_records_are_rejected_and_old_roi_is_not_reused(self):
        cases=[dict(stake=0),dict(stake=float('nan')),dict(offered_decimal_odds=1),dict(per_stake_cost=-.1),
               dict(placed_at_utc=KICK.isoformat()),dict(placed_at_utc='2026-11-06T19:00'),dict(market='Draw'),
               dict(currency=''),dict(bet_id=''),dict(kickoff_utc='invalid')]
        for mutation in cases:
            with self.subTest(mutation=mutation),self.assertRaises(ValueError):
                ledger.validate([{**placed(),**mutation}])
        with self.assertRaisesRegex(ValueError,'Duplicate'):
            ledger.validate([placed(),placed()])
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);path=root/ledger.INPUT;ledger.write(path,ledger.validate([placed()]))
            ledger.review_private(root,[],[final()],CLOCK)
            ledger.write(path,[{**placed(),'stake':-1}])
            self.assertEqual(ledger.review_private(root,[],[final()],CLOCK)['status'],'INVALID_PRIVATE_LEDGER')
            self.assertFalse((root/ledger.DIRECTORY/'graded_bets.csv').exists())
            self.assertIsNone(json.loads((root/ledger.DIRECTORY/'summary.json').read_text())['roi'])

    def test_future_placed_time_is_not_graded_and_currencies_are_not_combined(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);path=root/ledger.INPUT
            ledger.write(path,ledger.validate([placed()]))
            clock=pd.Timestamp(CAPTURED)-pd.Timedelta(minutes=1)
            self.assertEqual(ledger.review_private(root,[],[final()],clock)['status'],'INVALID_PRIVATE_LEDGER')
            ledger.write(path,ledger.validate([placed(),{**placed(),'bet_id':'ticket-2','currency':'USD','stake':5}]))
            ledger.review_private(root,[],[final()],CLOCK)
            summary=json.loads((root/ledger.DIRECTORY/'summary.json').read_text())
            self.assertEqual(set(summary['by_currency']),{'KES','USD'})
            self.assertNotIn('roi',summary)

    def test_ah_ledger_uses_label_and_closing_reference_must_follow_placement(self):
        row={**placed(),'market':'Asian Handicap Home +1.25','handicap_side':'away','handicap_line':-2}
        checked=ledger.validate([row])[0]
        self.assertEqual((checked['handicap_side'],checked['handicap_line']),('home',1.25))
        obs={'observed_at_utc':(pd.Timestamp(CAPTURED)-pd.Timedelta(seconds=1)).isoformat(),
             'fixture':{k:checked[k] for k in ('league','home_team','away_team','kickoff_utc')},'quotes':[]}
        with patch.object(tracking,'close_win_share',return_value=.8):
            self.assertIsNone(tracking.closing_for(checked,[obs],'home',1.25))
