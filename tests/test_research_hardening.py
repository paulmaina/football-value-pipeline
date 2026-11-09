"""Fresh, identity-bound research without invented probability effects or replay changes."""
import copy
import json
import tempfile
from unittest.mock import Mock, patch
import pandas as pd
from offline_test_case import OfflineQuotePolicyTestCase
import team_research as tr
import match_context as mc
import research_quality as rq
import profit_shortlist as ps
from test_price_edge_shortlist import NOW
from test_cagey_tier_v3 import sample
from test_match_context import roster


def row():
    return dict(sample(),kickoff_utc=(NOW+pd.Timedelta(minutes=90)).isoformat(),
                training_data_status='VERIFIED',training_cutoff=(NOW-pd.Timedelta(days=1)).isoformat())


def event(r):
    return {'id':'123','date':r['kickoff_utc'],'competitions':[{
        'date':r['kickoff_utc'],'venue':{'fullName':'Verified stadium'},'competitors':[
            {'homeAway':'home','team':{'id':'1','displayName':r['home_team']}},
            {'homeAway':'away','team':{'id':'2','displayName':r['away_team']}}]}]}


def summary(r):
    e=event(r)
    return {'header':{'id':e['id'],'competitions':e['competitions']},
            'rosters':[roster(1,True),roster(2,True)],
            'gameInfo':{'venue':{'fullName':'Summary stadium'}}}


def complete_evidence(r):
    evidence={'summary_identity_verified':True,'sources':[{'url':'https://example.test/summary?event=123',
        'status':'available','observed_at_utc':NOW.isoformat()}],
        'availability':[{'team':r['home_team'],'players':[{'player':'Player A','status':'Doubtful'}]}],
        'weather':{'complete_match_window':True,'observed_at_utc':NOW.isoformat()}}
    mc.compact_squads(summary(r),evidence,{'1':r['home_team'],'2':r['away_team']})
    return evidence


class Client:
    def __init__(self,r,data):self.row,self.data=r,data
    def clock(self):return NOW
    def get(self,url,**kw):
        data={'events':[event(self.row)]} if '/scoreboard?' in url else self.data if '/summary?' in url else {}
        return {'url':url,'status':'available','observed_at_utc':NOW.isoformat(),'data':data}


class ResearchHardeningTests(OfflineQuotePolicyTestCase):
    def test_memo_honours_stricter_ttl_in_same_client(self):
        clock=[NOW];session=Mock();session.get.return_value=Mock(content=b'{}',json=lambda:{})
        with tempfile.TemporaryDirectory() as tmp:
            client=tr.FreeSources(tmp,session=session,clock=lambda:clock[0])
            url='https://example.test/summary'
            client.get(url,max_age_minutes=180)
            clock[0]+=pd.Timedelta(minutes=6)
            fresh=client.get(url,max_age_minutes=5)
            self.assertEqual(session.get.call_count,2)
            self.assertEqual(fresh['observed_at_utc'],clock[0].isoformat())
            client.get(url,max_age_minutes=5)
            self.assertEqual(session.get.call_count,2)
            clock[0]+=pd.Timedelta(minutes=6);client.online=False
            self.assertEqual(client.get(url,max_age_minutes=5)['status'],'unavailable')
            self.assertEqual(session.get.call_count,2)

    def test_malformed_cached_response_does_not_abort_other_research(self):
        import hashlib
        from pathlib import Path
        session=Mock();session.get.return_value=Mock(content=b'{}',json=lambda:{})
        url='https://example.test/feed'
        with tempfile.TemporaryDirectory() as tmp:
            client=tr.FreeSources(tmp,session=session,clock=lambda:NOW)
            path=Path(tmp)/'match_research'/(hashlib.sha256(url.encode()).hexdigest()+'.json')
            path.write_text('[]',encoding='utf-8')
            self.assertEqual(client.get(url)['status'],'available')
            self.assertEqual(session.get.call_count,1)

    def test_memo_cannot_borrow_a_future_observation(self):
        clock=[NOW];session=Mock();session.get.return_value=Mock(content=b'{}',json=lambda:{})
        with tempfile.TemporaryDirectory() as tmp:
            client=tr.FreeSources(tmp,session=session,clock=lambda:clock[0])
            client.get('https://example.test/feed')
            clock[0]-=pd.Timedelta(minutes=1);client.online=False
            self.assertEqual(client.get('https://example.test/feed')['status'],'unavailable')
            self.assertEqual(session.get.call_count,1)

    def test_summary_requires_id_teams_kickoff_and_unambiguous_competitors(self):
        r=row();good=summary(r)
        self.assertIs(mc.verified_summary(good,r,'123'),good)
        variants=[{}, {'header':None}, {'header':{'id':'123','competitions':[]}}]
        for mode in ('id','teams','date','duplicate','period','completed'):
            wrong=copy.deepcopy(good)
            if mode=='completed':wrong['header']['status']={'type':{'state':'post','completed':True}}
            if mode=='id':wrong['header']['id']='999'
            if mode=='teams':wrong['header']['competitions'][0]['competitors'][0]['team']['displayName']='Wrong Club'
            if mode=='date':wrong['header']['competitions'][0]['date']=(NOW+pd.Timedelta(days=2)).isoformat()
            if mode=='duplicate':wrong['header']['competitions'][0]['competitors'].append(wrong['header']['competitions'][0]['competitors'][0])
            if mode=='period':wrong['header']['competitions'].append(wrong['header']['competitions'][0])
            variants.append(wrong)
        for wrong in variants:
            with self.subTest(wrong=wrong):self.assertIsNone(mc.verified_summary(wrong,r,'123'))

    def test_collector_rejects_foreign_summary_but_keeps_verified_board_venue(self):
        r=row();wrong=summary(r);wrong['header']['id']='999'
        with patch.object(mc,'collect_weather'),patch.object(mc,'add_review_links'):
            rejected=tr.collect_fixture(r,Client(r,wrong))
            accepted=tr.collect_fixture(r,Client(r,summary(r)))
        self.assertNotIn('lineups',rejected)
        self.assertEqual(rejected['venue']['fullName'],'Verified stadium')
        self.assertIn('summary identity unverified','; '.join(rejected['errors']))
        self.assertTrue(accepted['summary_identity_verified'])
        self.assertEqual(len(accepted['lineups']),2)
        self.assertEqual(accepted['venue']['fullName'],'Summary stadium')

    def test_team_id_name_contradiction_cannot_supply_absences_or_lineups(self):
        wrong=roster(1,True);wrong['team']['displayName']='Away FC'
        badinjury={'team':{'id':'999','displayName':'Home FC'},'injuries':[{'name':'Player A'}]}
        evidence={}
        mc.compact_squads({'rosters':[wrong], 'injuries':[badinjury]},evidence,{'1':'Home FC','2':'Away FC'})
        self.assertNotIn('lineups',evidence)
        self.assertNotIn('availability',evidence)

    def test_quality_requires_both_fresh_xis_and_does_not_infer_no_absences(self):
        r=row();ctx=tr.prepare(r,NOW,complete_evidence(r))
        ctx['form']={s:{'all':{'matches':10,'xg_matches':5},'venue':{'matches':4}} for s in ('home','away')}
        result=rq.assess(r,ctx,NOW)
        self.assertEqual(result['status'],'RECORDED_CHECKS_PASSED')
        self.assertEqual(result['lineups'],'CONFIRMED_FRESH')
        ctx['evidence']['availability']=[]
        missing=rq.assess(r,ctx,NOW)
        self.assertEqual(missing['status'],'REVIEW_REQUIRED')
        self.assertIn('do not mean both teams have full squads','; '.join(missing['warnings']))
        self.assertIn('NONE',missing['probability_effect'])
        ctx['evidence']['lineups'].append(ctx['evidence']['lineups'][0])
        self.assertEqual(rq.assess(r,ctx,NOW)['lineups'],'UNCONFIRMED_OR_STALE')

    def test_quality_freshness_is_reassessed_on_price_refresh_without_network_or_probability_changes(self):
        r=row()
        with tempfile.TemporaryDirectory() as tmp,patch.object(tr,'collect_fixture',return_value=complete_evidence(r)):
            out=tr.enrich(pd.DataFrame([r]),tmp,fetch=False,clock=lambda:NOW)
        frozen=out.iloc[0].to_dict();before=frozen['team_research_json']
        q=json.loads(before)
        self.assertEqual(q['evidence']['quality_review']['lineups'],'CONFIRMED_FRESH')
        late=NOW+pd.Timedelta(minutes=16)
        with patch('requests.sessions.Session.request',side_effect=AssertionError('Replay must be offline')):
            refreshed,warnings=ps.context(frozen,late)
        self.assertEqual(refreshed['evidence']['quality_review']['lineups'],'UNCONFIRMED_OR_STALE')
        self.assertEqual(refreshed['evidence']['quality_review']['weather'],'UNAVAILABLE_INCOMPLETE_OR_STALE')
        self.assertEqual(refreshed['margin_distribution'],q['margin_distribution'])
        self.assertEqual(frozen['team_research_json'],before)
        item={'market':'Asian Handicap Home +0.25','handicap_side':'home','handicap_line':.25,
              'offered_decimal_odds':1.5,'offered_last_update_utc':NOW.isoformat()}
        first=ps.annotate(frozen,dict(item),NOW,0.,rule=ps.RULE_V2)
        item['offered_last_update_utc']=late.isoformat()
        later=ps.annotate(frozen,dict(item),late,0.,rule=ps.RULE_V2)
        self.assertEqual(first['profit_probability'],later['profit_probability'])
        self.assertEqual(first['p_no_loss'],later['p_no_loss'])
        self.assertIn('not freshly confirmed','; '.join(warnings))

    def test_enrichment_keeps_goal_model_and_legacy_context_unchanged(self):
        r=row();evidence=complete_evidence(r)
        baseline=tr.prepare(r,NOW,copy.deepcopy(evidence))
        with tempfile.TemporaryDirectory() as tmp,patch.object(tr,'collect_fixture',return_value=evidence):
            out=tr.enrich(pd.DataFrame([r]),tmp,fetch=False,clock=lambda:NOW)
        new=json.loads(out.iloc[0].team_research_json)
        for field in ('goal_rates','margin_distribution','p_over_1_5'):
            self.assertEqual(new[field],baseline[field])
        self.assertEqual(new['evidence_quality_version'],rq.VERSION)
        legacy=dict(r,team_research_json=json.dumps(baseline))
        context,_=ps.context(legacy,NOW)
        self.assertNotIn('quality_review',context['evidence'])

    def test_quality_is_visible_in_value_cagey_and_master_reports(self):
        import price_edge_cagey_shortlist as v28
        import master_shortlist as master
        from shortlist_schema import readable
        from format_football_output import pct,decimal,signed_pct
        GROUP_NAMES={"asian_handicap":"Asian handicap","match_winner":"Match winner","double_chance":"Double chance"}
        r=row()
        with tempfile.TemporaryDirectory() as tmp,patch.object(tr,'collect_fixture',return_value={}):
            forecasts=tr.enrich(pd.DataFrame([r]),tmp,fetch=False,clock=lambda:NOW)
        value,decisions,_=v28.build_shortlist(forecasts,NOW)
        cagey=v28.cagey_tier_list(decisions)
        for frame in (value,cagey):
            self.assertGreater(len(frame),0)
            view=readable(frame,pct,decimal,signed_pct,GROUP_NAMES)
            self.assertIn('Research quality review',view)
            self.assertTrue(view['Coverage warnings'].str.contains('Research review:').all())
        top=master.build(decisions,forecasts,master.VERSION_CONTEXT)
        self.assertGreater(len(top),0)
        self.assertTrue(top.master_coverage_warning.str.contains('Research review:').all())
