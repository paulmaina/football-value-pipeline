"""Keyless T1 result provenance and end-to-end forward grading."""
from offline_test_case import OfflineQuotePolicyTestCase
from datetime import datetime, timedelta, timezone
import copy
import hashlib
import json
from pathlib import Path
import tempfile
from unittest.mock import Mock, patch

import pandas as pd
import requests

import turkey_results as tr
import performance_tracking as pt
from test_performance_tracking import fixture, pick, SHA

CLOCK = datetime(2026, 10, 26, 21, tzinfo=timezone.utc)
KICK = datetime(2026, 10, 24, 17, tzinfo=timezone.utc)
CSV = b'Div,Date,Time,HomeTeam,AwayTeam,FTHG,FTAG,FTR\nT1,24/10/2026,18:00,Buyuksehyr,Fenerbahce,2,1,H\n'


def forecast():
    return {**fixture(KICK), 'league': 'Super Lig', 'home_team': 'Basaksehir',
            'away_team': 'Fenerbahce'}


def session(content=CSV):
    response = Mock(content=content)
    response.raise_for_status.return_value = None
    return Mock(get=Mock(return_value=response))


class TurkeyResultsTests(OfflineQuotePolicyTestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)/'football_output_v2'

    def test_parse_exact_alias_match_without_fabricated_kickoff(self):
        records = tr.parse_results(CSV, 2026, CLOCK)
        record, state = pt.fixture_match(forecast(), records)
        self.assertEqual(state, 'VERIFIED_FINISHED')
        self.assertEqual((record['home_goals'], record['away_goals']), (2, 1))
        self.assertNotIn('kickoff_utc', record)
        self.assertTrue(pt.verified_result_source(record))
        self.assertFalse(pt.verified_result_source({**record, 'league_code': 'PL'}))
        self.assertEqual(pt.fixture_match({**forecast(), 'league': 'SuperLig'}, records)[1], state)

    def test_aliases_work_both_ways_and_are_not_fuzzy(self):
        aliases = json.loads(Path('bbs_team_aliases.json').read_text(encoding='utf-8'))['SuperLig']
        for feed, training in aliases.items():
            self.assertEqual(tr.team_key(feed), tr.team_key(training))
        record = tr.parse_results(CSV, 2026, CLOCK)[0]
        for fields in ({'home_team': 'Basaksehi'}, {'away_team': 'Galatasaray'},
                       {'home_team': 'Fenerbahce', 'away_team': 'Basaksehir'},
                       {'kickoff_utc': (KICK+timedelta(days=1)).isoformat()},
                       {'league': 'Primeira Liga'}):
            self.assertEqual(pt.fixture_match({**forecast(), **fields}, [record])[1],
                             'UNVERIFIED_FIXTURE_OR_RESULT')
        self.assertEqual(pt.fixture_match({**forecast(), 'kickoff_utc': 'bad'}, [record])[1], 'INVALID_FIXTURE')
        self.assertEqual(tr.fixture_match({'kickoff_utc': 'bad'}, [record])[1], 'INVALID_FIXTURE')
        self.assertEqual(pt.fixture_match(forecast(), [record, record])[1], 'AMBIGUOUS_FIXTURE')

    def test_bad_csvs_are_rejected(self):
        header, row = CSV.splitlines()
        for content in (b'<html>unavailable</html>', CSV.replace(b'T1,24', b'E0,24'),
                        CSV.replace(b',2,1,H', b',,1,H'), CSV.replace(b',2,1,H', b',-1,1,A'),
                        CSV.replace(b',2,1,H', b',2,1,A'), CSV.replace(b'24/10/2026', b'24/10/2027'),
                        CSV.replace(b'24/10/2026', b'27/10/2026'),
                        header+b'\n'+row+b'\n'+row+b'\n',
                        CSV.replace(b',Buyuksehyr,Fenerbahce', b',Buyuksehyr,Basaksehir'),
                        CSV.replace(b'Time,', b'Time,Extra,')
                        ):
            with self.subTest(content=content), self.assertRaises(ValueError):
                tr.parse_results(content, 2026, CLOCK)
        with self.assertRaises(ValueError):
            tr.parse_results(CSV.replace(b'FTR', b'Res'), 2026, CLOCK)

    def test_unplayed_rows_are_not_results(self):
        scheduled = b'T1,25/10/2026,18:00,Galatasaray,Besiktas,,,\n'
        self.assertEqual(len(tr.parse_results(CSV+scheduled, 2026, CLOCK)), 1)

    def test_finished_source_contract_rejects_mutations(self):
        record = tr.parse_results(CSV, 2026, CLOCK)[0]
        for field, value in [('source', 'football-data.org/v4'), ('source_status', 'SCHEDULED'),
                             ('source_duration', 'EXTRA_TIME'), ('source_sha256', '../x'),
                             ('source_url', 'https://example.test/T1.csv'),
                             ('source_season_start', 2025), ('home_goals', True),
                             ('match_id', 'fake'), ('match_date', None), ('home_team', None)]:
            with self.subTest(field=field):
                self.assertFalse(tr.verified({**record, field: value}))
        self.assertFalse(tr.verified({}))

    def test_fetch_preserves_bytes_and_checks_evidence(self):
        client = session()
        records = tr.fetch_results(self.root, [KICK, KICK], CLOCK, session=client)
        self.assertEqual(client.get.call_count, 1)
        self.assertEqual(client.get.call_args.args[0], tr.source_url(2026))
        self.assertNotIn('X-Auth-Token', client.get.call_args.kwargs['headers'])
        record = records[0]
        tr.validate_evidence(self.root, record, CLOCK)
        tr.fetch_results(self.root, [KICK], CLOCK, session=client)
        path = tr.evidence_path(self.root, 2026, record['source_sha256'])
        self.assertEqual(path.read_bytes(), CSV)
        with self.assertRaisesRegex(ValueError, 'differs from source'):
            tr.validate_evidence(self.root, {**record, 'home_goals': 3}, CLOCK)
        with self.assertRaisesRegex(ValueError, 'not verified'):
            tr.validate_evidence(self.root, {**record, 'source_status': 'SCHEDULED'}, CLOCK)
        path.write_bytes(b'tampered')
        with self.assertRaisesRegex(ValueError, 'checksum'):
            tr.validate_evidence(self.root, record, CLOCK)
        with self.assertRaisesRegex(ValueError, 'conflict'):
            tr.fetch_results(self.root, [KICK], CLOCK, session=client)
        path.unlink()
        with self.assertRaisesRegex(ValueError, 'Missing'):
            tr.validate_evidence(self.root, record, CLOCK)

    def test_collector_keyless_refresh_revisions_and_outage(self):
        client = session()
        records, errors = pt.collect_results([forecast()], root=self.root, token='', clock=CLOCK, session=client)
        self.assertEqual(errors, {})
        self.assertEqual(len(records), 1)
        self.assertIn('/2627/T1.csv', client.get.call_args.args[0])
        # Same identity, corrected score; no duplicate stake/result record.
        revised = session(CSV.replace(b',2,1,H', b',1,1,D'))
        updated, errors = pt.collect_results([forecast()], root=self.root, token='',
            clock=CLOCK+timedelta(hours=1), session=revised)
        self.assertEqual(len(updated), 1)
        self.assertEqual(updated[0]['home_goals'], 1)
        self.assertIn('revised_at_utc', updated[0])
        self.assertEqual(updated[0]['first_verified_at_utc'], records[0]['first_verified_at_utc'])
        client.get.side_effect = requests.ConnectionError('offline')
        cached, errors = pt.collect_results([forecast()], root=self.root, token='', clock=CLOCK, session=client)
        self.assertEqual(len(cached), 1)
        self.assertIn('SuperLig', errors)
        path = tr.evidence_path(self.root, 2026, cached[0]['source_sha256'])
        path.unlink()
        cached, errors = pt.collect_results([forecast()], root=self.root, token='', clock=CLOCK, session=client)
        self.assertEqual(cached, [])
        self.assertIn('evidence', errors['SuperLig'])

    def test_no_request_for_future_or_old_forecasts(self):
        client = session()
        rows = [{**forecast(), 'kickoff_utc': (CLOCK+timedelta(days=1)).isoformat()},
                {**forecast(), 'kickoff_utc': (CLOCK-timedelta(days=70)).isoformat()}]
        records, errors = pt.collect_results(rows, root=self.root, token='', clock=CLOCK, session=client)
        self.assertEqual((records, errors), ([], {}))
        client.get.assert_not_called()

    def test_cross_season_downloads_and_invalid_response(self):
        previous = CSV.replace(b'24/10/2026', b'24/05/2026')
        client = session()
        client.get.side_effect = [session(previous).get.return_value, session().get.return_value]
        dates = [KICK, datetime(2026, 5, 24, tzinfo=timezone.utc)]
        self.assertEqual(len(tr.fetch_results(self.root, dates, CLOCK, session=client)), 2)
        with self.assertRaisesRegex(ValueError, 'size limit'):
            tr.fetch_results(self.root, [KICK], CLOCK, session=session(b'x'*10_000_001))
        with self.assertRaises(ValueError):
            tr.fetch_results(self.root, [KICK], CLOCK, session=session(b'bad csv'))

    def test_archive_to_review_excel_roi_and_report_validation(self):
        from workflow_checks import report_check
        raw = self.root/'raw'
        raw.mkdir(parents=True)
        selected = {**pick(KICK, market='Home win'), **{k: v for k, v in forecast().items()
                    if k in ('league', 'home_team', 'away_team')}}
        pd.DataFrame([forecast()]).to_csv(raw/'all_leagues_predictions.csv', index=False)
        pd.DataFrame([selected]).to_csv(raw/'conservative_bet_shortlist.csv', index=False)
        generated = KICK-timedelta(days=1)
        pt.write_json(raw/'conservative_bet_summary.json', {'generated_at_utc': generated.isoformat(),
            'n_fixtures': 1, 'n_shortlisted': 1, 'n_strict_qualified': 1, 'n_provisional_watchlist': 0})
        self.assertTrue(pt.capture(SHA, root=self.root, captured_at=generated))
        self.assertEqual(len(pt.frozen_rows(pt.snapshots(self.root), 'predictions')), 1)
        summary = pt.review(root=self.root, token='', clock=CLOCK, session=session())
        self.assertEqual(summary['shortlist']['wins'], 1)
        self.assertEqual(summary['shortlist']['flat_stake_roi'], .5)
        self.assertEqual(summary['prediction_fixtures_graded'], 1)
        self.assertEqual(summary['provider_errors'], {})
        self.assertEqual(report_check(self.root)['status'], 'VERIFIED')
        self.assertTrue((self.root/'readable/football_performance_report.xlsx').is_file())
        grades = pt.read_csv(self.root/'performance/shortlist_grades.csv')
        self.assertEqual(grades[0]['match_source'], tr.SOURCE)
        records = list(pt.load_json(self.root/'performance/verified_results.json', {}).values())
        # Normal settlement logic also handles double chance and handicap.
        source = {**selected, 'fixture_key': 't1-test', 'snapshot_commit': SHA,
                  'snapshot_captured_utc': generated.isoformat()}
        for market, grade in [('Double Chance 1X', 'WON'), ('Double Chance X2', 'LOST'),
                              ('Asian Handicap Home -1.00', 'REFUNDED')]:
            scored = pt.score_shortlist({**source, 'market': market}, records[0], 'VERIFIED_FINISHED')
            self.assertEqual(scored['status'], grade)
        evidence = tr.evidence_path(self.root, 2026, records[0]['source_sha256'])
        evidence.write_bytes(b'tampered')
        with self.assertRaisesRegex(ValueError, 'checksum'):
            report_check(self.root)
