"""Access probes never expose credentials or turn partial coverage into approval."""
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import requests
import yaml
from scripts import audit_europa_access as audit

NOW=datetime(2026,10,22,tzinfo=timezone.utc)


class Response:
    def __init__(self, payload, code=200, headers=None):
        self.payload=payload;self.status_code=code;self.headers=headers or {}
    def json(self):return self.payload


class Session:
    def __init__(self, sender):self.sender=sender;self.calls=[]
    def get(self,url,**kwargs):
        self.calls.append((url,kwargs));return self.sender(url,kwargs)


class EuropaAccessAuditTests(unittest.TestCase):
    def test_plan_error_with_http_200_is_not_access_success(self):
        session=Session(lambda u,k:Response({'errors':{'plan':'not allowed; secret-do-not-print'}}))
        probe=audit.Probe(session,lambda _:None)
        payload,state=probe.get('api_football','/fixtures','season_2026',key='secret-do-not-print')
        self.assertIsNone(payload);self.assertEqual(state['status'],'PLAN_RESTRICTED')
        self.assertNotIn('secret-do-not-print',json.dumps(probe.calls))
        self.assertFalse(session.calls[0][1]['allow_redirects'])

    def test_quota_stops_more_calls_and_network_errors_do_not_echo_urls(self):
        session=Session(lambda u,k:Response({},429))
        probe=audit.Probe(session,lambda _:None)
        probe.get('bbs','/v1/leagues','catalogue',key='secret')
        _,state=probe.get('bbs','/v1/matches','season',key='secret')
        self.assertEqual(state['status'],'STOPPED_AFTER_ACCESS_OR_QUOTA_ERROR')
        self.assertEqual(len(session.calls),1)
        def fail(u,k):raise requests.RequestException('apiKey=secret-do-not-print')
        probe=audit.Probe(Session(fail),lambda _:None)
        _,state=probe.get('odds','/sports','catalogue',key='secret-do-not-print')
        self.assertEqual(state['status'],'NETWORK_ERROR')
        self.assertNotIn('secret-do-not-print',json.dumps(probe.calls))

    def test_discovery_excludes_champions_and_conference_leagues(self):
        data={'data':[{'name':'UEFA Champions League'},{'name':'UEFA Europa League','code':'el'},
                      {'name':'UEFA Europa Conference League'},{'name':'UEFA Europa League Qualification'}]}
        self.assertEqual(audit.find_leagues(data),[{'name':'UEFA Europa League','code':'el'}])

    def test_match_summary_rejects_wrong_season_competition_and_unverified_regulation(self):
        match={'id':1,'utcDate':'2024-10-01T19:00:00Z','status':'FINISHED',
            'competition':{'code':'EL'},'score':{'duration':'REGULAR','fullTime':{'home':2,'away':1}},
            'homeTeam':{'id':1},'awayTeam':{'id':2}}
        result=audit.summarize([match,match,{**match,'id':2,'competition':{'code':'CL'}},
                              {**match,'id':3,'utcDate':'2020-01-01T00:00:00Z'},
                              {**match,'id':4,'score':{'duration':'EXTRA_TIME','fullTime':{'home':2,'away':1}}}],
                              'football_data',2024)
        self.assertEqual(result['fixtures'],2)
        self.assertEqual(result['finished_with_scores'],2)
        self.assertEqual(result['regulation_confirmed'],1)
        self.assertEqual(result['wrong_competition_season_or_identity'],2)
        self.assertEqual(result['duplicate_fixture_ids'],1)
        self.assertFalse(audit.valid_score({'home':True,'away':0}))

    def test_pagination_cap_is_explicit_and_never_claims_complete(self):
        payload={'response':[],'paging':{'total':10}}
        probe=audit.Probe(Session(lambda u,k:Response(payload)),lambda _:None)
        with patch.dict(os.environ,{'API_FOOTBALL_KEY':'test-key'},clear=True):
            result=audit.historical(probe,'api_football',2024,{'league':3})
        self.assertFalse(result['all_reported_pages_read'])
        self.assertEqual(result['fixtures'],0)

    def test_unconfigured_sources_do_not_issue_requests(self):
        session=Session(lambda u,k:self.fail('Unexpected live request'))
        with patch.dict(os.environ,{},clear=True):
            report=audit.run(audit.Probe(session,lambda _:None),NOW)
        self.assertEqual(report['request_count'],0)
        self.assertTrue(all(not p['configured'] for p in report['providers'].values()))

    def test_market_presence_is_not_an_execution_or_model_approval(self):
        event={'bookmakers':[{'key':'pinnacle','markets':[{'key':'alternate_spreads',
            'last_update':NOW.isoformat(),'outcomes':[{'price':1.8,'point':.25},{'price':2.1,'point':-.25}]}]}]}
        result=audit.market_coverage(event,NOW)
        self.assertEqual(result['Pinnacle']['handicap_lines'],[-.25,.25])
        self.assertEqual(result['bet365']['markets'],{})
        self.assertEqual(result['1xBet']['markets'],{})

    def test_output_redacts_reflected_secrets(self):
        with tempfile.TemporaryDirectory() as tmp,patch.dict(os.environ,{'API_FOOTBALL_KEY':'secret-do-not-print'},clear=True),patch.object(audit,'run',return_value={'test':'secret-do-not-print'}),patch('builtins.print'):
            old=Path.cwd()
            try:
                os.chdir(tmp);audit.main()
                text=Path('workflow_artifacts/europa_access/report.json').read_text()
                self.assertNotIn('secret-do-not-print',text);self.assertIn('[REDACTED]',text)
            finally:os.chdir(old)

    def test_workflow_is_read_only_and_targeted_to_the_audit_branch(self):
        path=Path(__file__).resolve().parents[1]/'.github/workflows/audit-europa-access.yml'
        workflow=yaml.safe_load(path.read_text())
        self.assertEqual(workflow['permissions'],{'contents':'read'})
        trigger=workflow.get('on',workflow.get(True))
        self.assertEqual(trigger['push']['branches'],['audit/europa-league-access'])
        steps=workflow['jobs']['audit']['steps']
        self.assertFalse(steps[0]['with']['persist-credentials'])
        self.assertFalse(any('git push' in str(step.get('run','')) for step in steps))
