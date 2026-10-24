from offline_test_case import OfflineQuotePolicyTestCase
import json
import subprocess
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path
from unittest.mock import MagicMock

import pandas as pd

import league_registry
import refresh_training_data as refresh

REPO = Path(__file__).resolve().parents[1]
NEW = {'Eredivisie': ('Eredivisie', 'N1', 'soccer_netherlands_eredivisie'),
       'PrimeiraLiga': ('Primeira Liga', 'P1', 'soccer_portugal_primeira_liga')}
CLOCK = datetime(2026, 10, 12, tzinfo=timezone.utc)


def season_csv(division, year, teams=('A', 'B', 'C', 'D', 'E', 'F')):
    rows = ['Div,Date,HomeTeam,AwayTeam,FTHG,FTAG,FTR']
    day = datetime(year, 8, 10)
    for i, home in enumerate(teams):
        for j, away in enumerate(teams):
            if home != away:
                hg, ag = (i+j) % 3, (i*j) % 2
                result = 'H' if hg > ag else 'A' if ag > hg else 'D'
                rows.append(f'{division},{day:%d/%m/%Y},{home},{away},{hg},{ag},{result}')
                day += timedelta(days=2)
    return ('\n'.join(rows)+'\n').encode()


def fake_download(url):
    division = url.split('/')[-1][:-4]
    year = 2000+int(url.split('/')[-2][:2])
    return f'Div,Date,HomeTeam,AwayTeam,FTHG,FTAG\n{division},01/09/{year},A,B,1,0\n'.encode()


class NewLeagueRegistryTests(OfflineQuotePolicyTestCase):
    def test_new_leagues_are_unvalidated_domestic_registry_entries(self):
        for key, (name, division, sport) in NEW.items():
            league = league_registry.get(key)
            self.assertEqual((league.name, league.football_data_div, league.odds_api_sport_key),
                             (name, division, sport))
            self.assertEqual(league.refresh_method, league_registry.FOOTBALL_DATA_UK)
            self.assertEqual(league.history_seasons, 6)
            self.assertFalse(league.shortlist_validated)
            # Not collected by the optional statistics providers.
            self.assertIsNone(league.bbs_slug)
            self.assertIsNone(league.api_football_id)
        import bbs_data, bbs_integration, api_football_data, conservative_bet_filter, goal_market_validation
        for key, (name, division, _) in NEW.items():
            self.assertNotIn(key, bbs_data.LEAGUES)
            self.assertNotIn(division, bbs_integration.DIVISIONS)
            self.assertNotIn(key, api_football_data.LEAGUES)
            self.assertNotIn(name, conservative_bet_filter.SUPPORTED_LEAGUES)
            self.assertNotIn(key, goal_market_validation.SUPPORTED_COMPETITIONS)

    def test_existing_leagues_keep_their_odds_request_reservations(self):
        from goal_market_validation import distribute_event_odds_budget
        self.assertEqual(distribute_event_odds_budget(list(league_registry.LEAGUES), 24),
                         {'EPL': 4, 'LaLiga': 4, 'Bundesliga': 4, 'SerieA': 3, 'Ligue1': 3, 'UCL': 3, 'UEL': 3})


class NewLeagueLoadTests(OfflineQuotePolicyTestCase):
    def test_new_leagues_load_and_fit_from_cached_csvs(self):
        import football_value_pipeline_v2_standalone as fv
        now = datetime(2026, 10, 20, tzinfo=timezone.utc)
        with tempfile.TemporaryDirectory() as tmp:
            cache = Path(tmp)
            for division in ('N1', 'P1'):
                for year in range(2021, 2027):
                    (cache/f'{refresh.season_code(year)}_{division}.csv').write_bytes(season_csv(division, year))
            pipe = fv.FootballValuePipelineV2(cache_dir=str(cache), seasons_back=4, domestic_seasons_back=6,
                                              live_odds=False, odds_api_key='')
            pipe.source.allow_training_download = False
            for key in NEW:
                with self.subTest(key=key):
                    history = pipe._history_for_league(fv.LEAGUES[key], now=now)
                    self.assertEqual(len(history), 6*30)
                    self.assertEqual(history.attrs['training_seasons_requested'], 6)
                    model = fv.DixonColesModel(max_goals=8).fit(history, as_of=pd.Timestamp(now))
                    prediction = model.predict('A', 'B')
                    self.assertAlmostEqual(prediction['p_home']+prediction['p_draw']+prediction['p_away'], 1, places=9)


class NewLeagueRefreshTests(OfflineQuotePolicyTestCase):
    def test_scheduled_refresh_downloads_and_commits_new_league_csvs(self):
        batch = refresh.fetch_batch(CLOCK, 1, fake_download)
        self.assertEqual({x['division'] for x in batch} >= {'N1', 'P1'}, True)
        full = refresh.fetch_batch(CLOCK, 1, fake_download, full_history=True)
        for division in ('N1', 'P1'):
            self.assertEqual(sorted(x['year'] for x in full if x['division'] == division), list(range(2021, 2027)))
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); remote = root/'remote.git'; repo = root/'repo'
            subprocess.run(['git', 'init', '--bare', str(remote)], check=True, capture_output=True)
            subprocess.run(['git', 'clone', str(remote), str(repo)], check=True, capture_output=True)
            for k, v in [('user.name', 'Test'), ('user.email', 'test@example.test')]:
                refresh.git(repo, 'config', k, v)
            refresh.git(repo, 'checkout', '-b', 'main')
            (repo/'README.md').write_text('seed')
            refresh.git(repo, 'add', '.'); refresh.git(repo, 'commit', '-m', 'Initial')
            refresh.git(repo, 'push', 'origin', 'main')
            refresh.publish(repo, full, CLOCK)
            refresh.git(repo, 'fetch', 'origin', 'main')
            files = set(refresh.git(repo, 'ls-tree', '-r', '--name-only', 'FETCH_HEAD').stdout.split())
            for division in ('N1', 'P1'):
                self.assertTrue({f'.football_cache/{refresh.season_code(y)}_{division}.csv'
                                 for y in range(2021, 2027)} <= files)
            status = json.loads(refresh.git(repo, 'show', f'FETCH_HEAD:{refresh.STATUS.as_posix()}').stdout)
            self.assertIn('Eredivisie', status['scope'])
            self.assertIn('N1', {x['division'] for x in status['files']})

    def test_workflow_and_forecast_publisher_pick_up_new_leagues(self):
        from workflow_checks import registry_check
        import publish_scheduled_forecasts as scheduled
        methods = registry_check(REPO)['refresh_methods']
        self.assertTrue(set(NEW) <= set(methods[league_registry.FOOTBALL_DATA_UK]))
        self.assertTrue(set(NEW) <= set(league_registry.keys()))
        with tempfile.TemporaryDirectory() as tmp:
            work = Path(tmp); cache = work/'.football_cache'; cache.mkdir()
            for name in ('2627_N1.csv', '2122_P1.csv', '2627_E0.csv'):
                (cache/name).write_text('csv')
            found = {p.name for p in scheduled.training_files(work)}
        self.assertEqual(found, {'2627_N1.csv', '2122_P1.csv', '2627_E0.csv'})


class NewLeagueShortlistTests(OfflineQuotePolicyTestCase):
    def _committed(self):
        raw = REPO/'football_output_v2/raw'
        predictions = pd.read_csv(raw/'all_leagues_predictions.csv', low_memory=False)
        reliability = {}
        for path in sorted(raw.glob('*_goal_market_validation.json')):
            report = json.loads(path.read_text(encoding='utf-8'))
            reliability[report['league']] = report
        as_of = datetime.fromisoformat(json.loads((raw/'conservative_bet_summary.json').read_text())['generated_at_utc'])
        return predictions, reliability, as_of

    def test_unvalidated_leagues_are_excluded_even_with_passing_history_evidence(self):
        from conservative_bet_filter import build_conservative_shortlist
        from asian_handicap import CURRENT_POLICY, POLICIES
        from per_market_shortlist import POLICY as V24
        predictions, reliability, as_of = self._committed()
        picks, _, _ = build_conservative_shortlist(predictions, as_of=as_of, market_reliability=reliability,
                                                   selection_policy_version=V24)
        self.assertGreater(len(picks), 0, 'control: committed forecasts must produce picks')
        for key, (name, _, _) in NEW.items():
            # Worst case: the league's rows carry every existing league's passing reports.
            relabelled = predictions.assign(league=name)
            evidence = {**reliability, name: next(iter(reliability.values()))}
            cases = [(V24, None), (V24, {})] + [(v, evidence) for v in
                                                dict.fromkeys((V24, CURRENT_POLICY, *POLICIES[-3:]))]
            for version, market_reliability in cases:
                with self.subTest(league=key, policy=version, evidence=market_reliability is evidence):
                    picks, decisions, summary = build_conservative_shortlist(
                        relabelled, as_of=as_of, market_reliability=market_reliability,
                        selection_policy_version=version)
                    self.assertEqual(len(picks), 0)
                    self.assertNotIn(name, summary.get('eligible_leagues', []))
                    self.assertTrue(decisions.decision.ne('SHORTLISTED').all())
                    # Same SUPPORTED_LEAGUES gate; Asian handicap words it differently.
                    self.assertTrue(decisions.rejection_reasons.fillna('').str.contains(
                        'competition excluded from shortlist validation|competition unsupported').all())

    def test_market_led_experiment_skips_unvalidated_leagues_without_spending_credits(self):
        from market_led_experiment import write_experiment
        import market_led_experiment
        kickoff = (datetime.now(timezone.utc)+timedelta(hours=10)).isoformat()
        predictions = pd.DataFrame([{'league': 'Eredivisie', 'home_team': 'Ajax', 'away_team': 'PSV',
                                     'kickoff_utc': kickoff, 'fixture_id': 'f1', 'odds_event_id': 'evt1'}])
        api = MagicMock()
        with tempfile.TemporaryDirectory() as tmp:
            raw = Path(tmp)
            predictions.to_csv(raw/'all_leagues_predictions.csv', index=False)
            fetch = MagicMock(side_effect=AssertionError('no credits for unvalidated leagues'))
            original = market_led_experiment.fetch_event
            market_led_experiment.fetch_event = fetch
            try:
                data = write_experiment(predictions, raw, kickoff, api, market_led_experiment.settings())
            finally:
                market_led_experiment.fetch_event = original
        fetch.assert_not_called()
        self.assertTrue(data['rows'])
        for row in data['rows']:
            self.assertFalse(row['selected'])
            self.assertIn('competition_excluded_from_shortlist_validation', row['reasons'])


if __name__ == '__main__':
    unittest.main()
