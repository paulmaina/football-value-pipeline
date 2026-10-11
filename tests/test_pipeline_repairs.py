import json
from datetime import datetime, timezone, timedelta
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from match_scores import regulation_goals
from football_value_pipeline_v2_standalone import FootballDataOrg, LEAGUES
from goal_market_validation import prioritized_additional_events
from performance_excel import write_workbook


class PipelineRepairsTests(unittest.TestCase):
    def test_training_uses_regulation_score_and_rejects_unknown_or_future_results(self):
        now = datetime(2026, 10, 11, tzinfo=timezone.utc)
        base = dict(status='FINISHED', homeTeam={'name':'A'}, awayTeam={'name':'B'})
        matches = [dict(base, utcDate='2025-01-01T20:00:00Z', score={
            'duration':'PENALTY_SHOOTOUT', 'regularTime':{'home':0,'away':1},
            'fullTime':{'home':1,'away':5}})]
        matches += [dict(base, utcDate=f'2025-02-{i:02}T20:00:00Z', score={
            'duration':'REGULAR','fullTime':{'home':1,'away':0}}) for i in range(1,29)]
        matches.append(dict(base,utcDate='2025-03-01T20:00:00Z',score={
            'duration':'EXTRA_TIME','regularTime':{'home':3,'away':3},'fullTime':{'home':4,'away':3}}))
        matches.append(dict(base,utcDate='2027-01-01T20:00:00Z',score={
            'duration':'REGULAR','fullTime':{'home':9,'away':9}}))
        matches.append(dict(base,utcDate='2025-04-01T20:00:00Z',score={
            'duration':'EXTRA_TIME','fullTime':{'home':4,'away':3}}))
        with tempfile.TemporaryDirectory() as tmp:
            provider = FootballDataOrg('offline-test', cache_dir=tmp)
            with patch.object(provider.http,'get_json',return_value={'matches':matches}):
                history = provider.history(LEAGUES['UCL'],1,now)
        self.assertEqual(len(history),30)
        self.assertEqual(history.iloc[0][['FTHG','FTAG']].tolist(),[0,1])
        self.assertEqual(history.iloc[-1][['FTHG','FTAG']].tolist(),[3,3])
        self.assertIsNone(regulation_goals({'duration':'UNKNOWN','fullTime':{'home':1,'away':0}}))

    def test_additional_odds_budget_cannot_be_spent_outside_shortlist_window(self):
        now = datetime(2026,10,11,tzinfo=timezone.utc)
        def candidate(hours,p):
            return ({'odds_source':'The Odds API','odds_event_id':str(hours),
                     'kickoff_utc':(now+timedelta(hours=hours)).isoformat()},
                    {'home_name_match_score':100,'away_name_match_score':100,
                     'p_over_1_5':p,'raw_p_over_1_5':p})
        self.assertEqual(prioritized_additional_events(
            [candidate(73,.99),candidate(72,.85),candidate(-1,.98)],1,as_of=now),[1])

    def test_locked_workbook_preserves_previous_file_and_removes_temporary_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp); dest=root/'readable'/'football_performance_report.xlsx'
            dest.parent.mkdir(); dest.write_bytes(b'previous workbook')
            with patch.object(Path,'replace',side_effect=PermissionError('locked')):
                with self.assertRaisesRegex(PermissionError,'Close the workbook'):
                    write_workbook(root,[],[],{},dest)
            self.assertEqual(dest.read_bytes(),b'previous workbook')
            self.assertEqual(list(dest.parent.glob('*.tmp')),[])
