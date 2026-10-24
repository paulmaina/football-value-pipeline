from offline_test_case import OfflineQuotePolicyTestCase
import json
import subprocess
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path
from unittest.mock import patch

import league_registry
import refresh_training_data as refresh
from publish_performance import git

REPO = Path(__file__).resolve().parents[1]
CLOCK = datetime(2026, 10, 12, tzinfo=timezone.utc)

# The values every module hard-coded before the registry existed.
ORIGINAL = {
    'EPL': ('Premier League', 'England', 'E0', 'soccer_epl', 'PL'),
    'LaLiga': ('La Liga', 'Spain', 'SP1', 'soccer_spain_la_liga', 'PD'),
    'Bundesliga': ('Bundesliga', 'Germany', 'D1', 'soccer_germany_bundesliga', 'BL1'),
    'SerieA': ('Serie A', 'Italy', 'I1', 'soccer_italy_serie_a', 'SA'),
    'Ligue1': ('Ligue 1', 'France', 'F1', 'soccer_france_ligue_one', 'FL1'),
    'UCL': ('UEFA Champions League', 'Europe', '', 'soccer_uefa_champs_league', 'CL'),
    'UEL': ('UEFA Europa League', 'Europe', '', 'soccer_uefa_europa_league', 'EL'),
}


def europa_payload(n=40):
    return {'verified_at_utc': CLOCK.isoformat(), 'official_source_health': {},
            'matches': [{'date': f'2026-09-{i % 28 + 1:02d}', 'home': f'H{i}', 'away': f'A{i}'} for i in range(n)]}


def fake_refresher(cache_dir, now):
    """Stand-in for europa_training.refresh: writes the snapshot and one source."""
    directory = Path(cache_dir)/'europa'
    (directory/'sources').mkdir(parents=True, exist_ok=True)
    (directory/'sources'/'cornerflick.json').write_text('{"matches": []}\n')
    payload = europa_payload()
    (directory/'training.json').write_text(json.dumps(payload))
    return payload


class RegistryTests(OfflineQuotePolicyTestCase):
    def test_existing_leagues_keep_their_original_identities_and_order(self):
        self.assertEqual(list(league_registry.LEAGUES)[:7], list(ORIGINAL))
        for key, values in ORIGINAL.items():
            l = league_registry.get(key)
            self.assertEqual((l.name, l.country, l.football_data_div, l.odds_api_sport_key,
                              l.football_data_org_code), values)
            self.assertTrue(l.shortlist_validated)
        from football_value_pipeline_v2_standalone import LEAGUES, history_windows
        self.assertEqual(LEAGUES, league_registry.LEAGUES)
        self.assertEqual(history_windows(type('A', (), {'seasons_back': None, 'domestic_seasons_back': None})),
                         {'seasons_back': 4, 'domestic_seasons_back': 6})

    def test_every_module_derives_its_league_list_from_the_registry(self):
        import api_football_data, bbs_data, bbs_integration, conservative_bet_filter, goal_market_validation, \
            historical_benchmark
        self.assertEqual(goal_market_validation.SUPPORTED_COMPETITIONS, league_registry.keys())
        self.assertEqual(refresh.DIVISIONS, league_registry.divisions())
        self.assertEqual(historical_benchmark.CODES, league_registry.divisions())
        self.assertEqual(conservative_bet_filter.SUPPORTED_LEAGUES, league_registry.shortlist_names())
        self.assertEqual(conservative_bet_filter.DOMESTIC_LEAGUES, league_registry.shortlist_names(domestic_only=True))
        self.assertEqual(bbs_data.LEAGUES, {'EPL': 'epl', 'LaLiga': 'laliga', 'Bundesliga': 'bundesliga',
                                            'SerieA': 'serie_a', 'Ligue1': 'ligue1', 'UCL': 'cl'})
        self.assertEqual(set(bbs_data.DISPLAY_NAMES), set(bbs_data.LEAGUES))
        self.assertEqual(bbs_integration.DIVISIONS, {'E0': 'EPL', 'SP1': 'LaLiga', 'D1': 'Bundesliga',
                                                     'I1': 'SerieA', 'F1': 'Ligue1'})
        self.assertEqual(api_football_data.LEAGUES, {'EPL': 39, 'LaLiga': 140, 'Bundesliga': 78,
                                                     'SerieA': 135, 'Ligue1': 61, 'UCL': 2})

    def test_validation_rejects_inconsistent_entries(self):
        good = league_registry.REGISTRY
        bad = [good[0].__class__(**{**good[0].__dict__, 'refresh_method': 'scraper'}),
               good[0].__class__(**{**good[0].__dict__, 'football_data_div': ''}),
               good[0].__class__(**{**good[0].__dict__, 'history_seasons': 0}),
               good[0].__class__(**{**good[0].__dict__, 'odds_api_sport_key': 'epl'})]
        for entry in bad:
            with self.subTest(entry=entry), patch.object(league_registry, 'REGISTRY', (entry,)), \
                    self.assertRaises(ValueError):
                league_registry.validate()
        with patch.object(league_registry, 'REGISTRY', (good[0], good[0])), self.assertRaises(ValueError):
            league_registry.validate()

    def test_cli_lists_every_league(self):
        out = subprocess.run(['python', str(REPO/'league_registry.py'), '--json'], capture_output=True,
                             text=True, check=True, cwd=REPO).stdout
        self.assertEqual([r['key'] for r in json.loads(out)], list(league_registry.LEAGUES))
        import contextlib, io
        for argv in ([], ['--json']):
            with contextlib.redirect_stdout(io.StringIO()) as buffer:
                self.assertEqual(league_registry.main(argv), 0)
            self.assertIn('UEL', buffer.getvalue())
        with self.assertRaises(KeyError):
            league_registry.get('Unknown')

    def test_every_league_has_a_scheduled_refresh(self):
        from workflow_checks import registry_check
        result = registry_check(REPO)
        self.assertEqual(sorted(k for keys in result['refresh_methods'].values() for k in keys),
                         sorted(league_registry.LEAGUES))
        workflow = (REPO/'.github/workflows/refresh-training-data.yml').read_text(encoding='utf-8')
        # The scheduled job is not restricted to a method, so it covers every keyless league.
        self.assertIn('python refresh_training_data.py $history --publish', workflow)
        self.assertNotIn('--method', workflow)
        with tempfile.TemporaryDirectory() as tmp, self.assertRaises(ValueError):
            registry_check(Path(tmp))


class RefreshTests(OfflineQuotePolicyTestCase):
    def test_full_history_uses_each_leagues_registry_window(self):
        def fake(url):
            division = url.split('/')[-1][:-4]
            year = 2000+int(url.split('/')[-2][:2])
            return f'Div,Date,HomeTeam,AwayTeam,FTHG,FTAG\n{division},01/09/{year},A,B,1,0\n'.encode()
        batch = refresh.fetch_batch(CLOCK, 1, fake, full_history=True)
        for key, division in refresh.DIVISIONS.items():
            years = {x['year'] for x in batch if x['division'] == division}
            self.assertEqual(len(years), league_registry.get(key).history_seasons)

    def test_europa_refresh_failure_keeps_snapshot_and_does_not_block_domestic(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            self.assertEqual(refresh.apply_europa(repo, CLOCK, fake_refresher)['completed_matches'], 40)
            before = (repo/'.football_cache/europa/training.json').read_bytes()

            def disagree(cache_dir, now):
                raise ValueError('Current Europa sources disagree or coverage is incomplete; prior snapshot retained')
            with self.assertRaises(ValueError):
                refresh.apply_europa(repo, CLOCK, disagree)
            self.assertEqual((repo/'.football_cache/europa/training.json').read_bytes(), before)
            calls = []
            with patch.object(refresh, 'fetch_batch', side_effect=lambda *a, **k: calls.append('domestic') or []), \
                    patch.object(refresh, 'apply_batch', return_value=[]), \
                    patch.object(refresh, 'apply_europa', side_effect=ValueError('sources disagree')), \
                    self.assertRaises(ValueError):
                refresh.main(['--repo', tmp])
            self.assertEqual(calls, ['domestic'])

    def test_main_runs_only_the_requested_method_with_full_history(self):
        with patch.object(refresh, 'fetch_batch', return_value=[]) as fetch, \
                patch.object(refresh, 'apply_batch', return_value=[]), \
                patch.object(refresh, 'apply_europa') as europa:
            refresh.main(['--method', league_registry.FOOTBALL_DATA_UK, '--full-history'])
        self.assertTrue(fetch.call_args.kwargs['full_history'])
        europa.assert_not_called()

    def test_europa_publish_commits_snapshot_and_sources(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); remote = root/'remote.git'; repo = root/'repo'
            subprocess.run(['git', 'init', '--bare', str(remote)], check=True, capture_output=True)
            subprocess.run(['git', 'clone', str(remote), str(repo)], check=True, capture_output=True)
            for k, v in [('user.name', 'Test'), ('user.email', 'test@example.test')]:
                git(repo, 'config', k, v)
            git(repo, 'checkout', '-b', 'main')
            (repo/'README.md').write_text('preserve me')
            git(repo, 'add', '.'); git(repo, 'commit', '-m', 'Initial'); git(repo, 'push', 'origin', 'main')
            entry = refresh.publish_europa(repo, CLOCK, refresher=fake_refresher)
            self.assertEqual(entry['league'], 'UEL')
            git(repo, 'fetch', 'origin', 'main')
            files = git(repo, 'ls-tree', '-r', '--name-only', 'FETCH_HEAD').stdout.split()
            self.assertIn('.football_cache/europa/training.json', files)
            self.assertIn('.football_cache/europa/sources/cornerflick.json', files)
            self.assertIn('Europa', git(repo, 'log', '-1', '--format=%s', 'FETCH_HEAD').stdout)
            # An unchanged refresh publishes nothing.
            head = git(repo, 'rev-parse', 'FETCH_HEAD').stdout
            refresh.publish_europa(repo, CLOCK, refresher=fake_refresher)
            git(repo, 'fetch', 'origin', 'main')
            self.assertEqual(git(repo, 'rev-parse', 'FETCH_HEAD').stdout, head)

    def test_europa_freshness_stays_fail_closed_at_24_hours(self):
        from europa_training import fresh
        payload = {'verified_at_utc': CLOCK.isoformat()}
        self.assertTrue(fresh(payload, CLOCK.replace(hour=23)))
        self.assertFalse(fresh(payload, CLOCK.replace(day=13, hour=0, minute=1)))


class ScheduledForecastTests(OfflineQuotePolicyTestCase):
    def test_forecasts_request_every_league_and_commit_every_training_file(self):
        import publish_scheduled_forecasts as scheduled
        with tempfile.TemporaryDirectory() as tmp:
            work = Path(tmp); cache = work/'.football_cache'
            expected = set()
            for league in league_registry.REGISTRY:
                for pattern in league.cache_globs():
                    name = pattern.replace('????', '2627').replace('*', 'source.txt')
                    path = cache/name
                    path.parent.mkdir(parents=True, exist_ok=True)
                    path.write_text(league.key)
                    expected.add(path)
            (cache/'oddsapi_events_EPL.json').write_text('temporary odds response')
            found = set(scheduled.training_files(work))
            self.assertEqual(found, expected)
            self.assertIn(cache/'europa/training.json', found)
        calls = []

        def runner(cmd, cwd, check):
            calls.append(cmd)
            raise subprocess.CalledProcessError(1, cmd)
        with tempfile.TemporaryDirectory() as tmp:
            from tests.test_publish_scheduled_forecasts import repo
            source, _ = repo(tmp)
            with self.assertRaises(subprocess.CalledProcessError):
                scheduled.publish(source, runner=runner)
        leagues = calls[0][calls[0].index('--leagues')+1:calls[0].index('--tune-half-life')]
        self.assertEqual(tuple(leagues), league_registry.keys())


if __name__ == '__main__':
    unittest.main()
