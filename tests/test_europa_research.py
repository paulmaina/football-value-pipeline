"""Regression gates for cup periods, source disagreements and research isolation."""
from datetime import datetime, timezone
import json
from pathlib import Path
import tempfile
import unittest

from scripts import europa_research as r
from scripts.europa_validation import metrics, summarize_market


class EuropaResearchTests(unittest.TestCase):
    def source(self, score, header='2024/25', date='Thu Apr 17 2025'):
        return (f'= UEFA Europa League {header}\n# Matches 1\n'
                f'▪ Quarterfinals\n  {date}\n'
                f'    21:00 Club A (ENG) v Club B (FRA) {score}\n')

    def parse(self, score):
        return r.parse_openfootball(self.source(score), 2024, r.key)[0]

    def test_extra_time_and_shootout_are_separate_from_regulation(self):
        row = self.parse('5-4 a.e.t. (2-2, 2-0)')
        self.assertEqual(row['reported'], (5, 4))
        self.assertEqual(row['regulation'], (2, 2))
        row = self.parse('3-5 pen. 0-2 a.e.t. (0-2, 0-1)')
        self.assertEqual(row['regulation'], (0, 2))
        self.assertEqual(row['duration'], 'AET_PEN')
        self.assertEqual(self.parse('0-0')['regulation'], (0, 0))

    def test_ambiguous_periods_bad_scores_and_missing_dates_fail_closed(self):
        for score in ['5-4 a.e.t.', '3-5 pen. 1-1', '1-1 a.e.t. (2-2, 0-0)',
                      '3-2 a.e.t. (2-2, 3-0)', '31-0', '-1-0']:
            with self.subTest(score=score), self.assertRaises(ValueError):
                self.parse(score)
        with self.assertRaises(ValueError):
            r.parse_openfootball(self.source('1-0').replace('  Thu Apr 17 2025\n', ''), 2024, r.key)

    def test_season_header_date_and_count_cannot_silently_drift(self):
        for text in [self.source('1-0', header='2023/24'),
                     self.source('1-0', date='Thu Apr 17 2024'),
                     self.source('1-0').replace('# Matches 1', '# Matches 2')]:
            with self.assertRaises(ValueError):
                r.parse_openfootball(text, 2024, r.key)

    def test_duplicate_and_self_fixtures_rejected(self):
        row = self.parse('1-0')
        with self.assertRaises(ValueError):
            r.require_unique([row, row])
        with self.assertRaises(ValueError):
            r.require_unique([{**row, 'away': row['home']}])

    def test_aliases_preserve_distinct_clubs_and_do_not_fuzzy_match(self):
        resolve = r.team_resolver({'Man Utd': 'Manchester United'})
        self.assertEqual(resolve('Man Utd'), 'manchester united')
        self.assertNotEqual(resolve('Fenerbahçe'), resolve('Ferencváros'))
        self.assertNotEqual(resolve('Club A'), resolve('Club AA'))
        with self.assertRaises(ValueError):
            r.team_resolver({'A': 'B', 'B': 'C'})

    def test_uefa_links_keep_period_flag_and_ignore_unscored_fixture(self):
        html = ('<a href="/uefaeuropaleague/match/123--a-vs-b/">Club A 3-2 Club B (aet, agg: 4-3)</a>'
                '<a href="/uefaeuropaleague/match/124/">Club A vs Club B</a>'
                '<a href="/uefachampionsleague/match/125/">Club A 1-0 Club B</a>')
        rows = r.uefa_scores(html, r.key)
        self.assertEqual(len(rows), 1)
        self.assertTrue(rows[0]['aet'])
        self.assertEqual(rows[0]['reported'], (3, 2))

    def corner_source(self, root, row):
        payload = {'competition': {'slug': 'europa-league'},
                   'meta': {'match_count': 2, 'source': 'api-football'},
                   'matches': [row, {**row, 'round': None}]}
        (root/'cornerflick.json').write_text(json.dumps(payload))
        (root/'fixture-2026.csv').write_text('Date,Home Team,Away Team,Result,Round Number\n'
                                          '15/10/2026 19:00,Club A,Club B,2 - 1,2\n')

    def test_cornerflick_requires_stage_and_matching_fixture_download_score(self):
        row = {'round': 'League Stage - 2', 'status': 'finished', 'kickoff_at': '2026-10-15T19:00:00Z',
               'home_team': 'Club A', 'away_team': 'Club B', 'home_score': 2, 'away_score': 1}
        now = datetime(2026, 10, 22, tzinfo=timezone.utc)
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp)
            self.corner_source(p, row)
            report, records = r.audit_cornerflick(p, r.key, now)
            self.assertEqual(len(records), 1)
            self.assertEqual(report['unclassified_rows_quarantined'], 1)
            self.assertTrue(report['verified_for_research'])
            self.assertFalse(report['production_eligible'])
            self.corner_source(p, {**row, 'away_score': 0})
            report, _ = r.audit_cornerflick(p, r.key, now)
            self.assertFalse(report['verified_for_research'])
            self.assertEqual(len(report['score_conflicts']), 1)
            self.corner_source(p, {**row, 'kickoff_at': '2026-10-23T19:00:00Z'})
            with self.assertRaises(ValueError):
                r.audit_cornerflick(p, r.key, now)

    def test_two_source_audit_still_rejects_missing_matches_in_either_feed(self):
        row = {'round': 'League Stage - 2', 'status': 'finished', 'kickoff_at': '2026-10-15T19:00:00Z',
               'home_team': 'Club A', 'away_team': 'Club B', 'home_score': 2, 'away_score': 1}
        now = datetime(2026, 10, 22, tzinfo=timezone.utc)
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.corner_source(root, row)
            path = root/'fixture-2026.csv'
            original = path.read_text()
            path.write_text(original.splitlines()[0] + '\n')
            report, _ = r.audit_cornerflick(root, r.key, now)
            self.assertFalse(report['verified_for_research'])
            self.assertEqual(len(report['unverified_identities']), 1)
            path.write_text(original + '16/10/2026 19:00,Club C,Club D,1 - 0,2\n')
            report, _ = r.audit_cornerflick(root, r.key, now)
            self.assertFalse(report['verified_for_research'])
            self.assertEqual(report['missing_against_fixture_download'], 1)

    def test_audit_labels_do_not_change_development_penalty_and_no_enable(self):
        dev = [{'p': .9, 'y': 1, 'baseline': .7}] * 40
        audit = [{'p': .9, 'y': 1, 'baseline': .7}] * 20
        good = summarize_market(dev, audit)
        bad = summarize_market(dev, [{**x, 'y': 0} for x in audit])
        self.assertEqual(good['development_penalty'], bad['development_penalty'])
        self.assertEqual(good['diagnostic_status'], 'PASS_RESEARCH_DIAGNOSTIC')
        self.assertEqual(bad['diagnostic_status'], 'FAIL_AUDIT')
        self.assertFalse(good['production_eligible'])
        self.assertEqual(summarize_market(dev[:2], audit)['diagnostic_status'], 'INSUFFICIENT_HIGH_CONFIDENCE_SAMPLE')

    def test_baseline_is_supplied_by_training_not_audit_prevalence(self):
        result = metrics([{'p': .8, 'y': 1, 'baseline': .2}])
        self.assertAlmostEqual(result['brier'], .04)
        self.assertAlmostEqual(result['baseline_brier'], .64)

    def test_output_cannot_write_into_repository(self):
        from unittest.mock import patch
        import contextlib
        import io
        with patch('sys.argv', ['europa_research', '--source-dir', '/tmp/source', '--output-dir', str(r.ROOT)]), \
                contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit):
            r.main()
