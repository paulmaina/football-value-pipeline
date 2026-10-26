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
    def test_new_leagues_are_per_market_domestic_registry_entries(self):
        for key, (name, division, sport) in NEW.items():
            league = league_registry.get(key)
            self.assertEqual((league.name, league.football_data_div, league.odds_api_sport_key),
                             (name, division, sport))
            self.assertEqual(league.refresh_method, league_registry.FOOTBALL_DATA_UK)
            self.assertEqual(league.history_seasons, 6)
            self.assertEqual(league.shortlist_approval, league_registry.PER_MARKET_APPROVAL)
            # Not collected by the optional statistics providers.
            self.assertIsNone(league.bbs_slug)
            self.assertIsNone(league.api_football_id)
        import bbs_data, bbs_integration, api_football_data, conservative_bet_filter, goal_market_validation
        for key, (name, division, _) in NEW.items():
            self.assertNotIn(key, bbs_data.LEAGUES)
            self.assertNotIn(division, bbs_integration.DIVISIONS)
            self.assertNotIn(key, api_football_data.LEAGUES)
            self.assertIn(name, conservative_bet_filter.SUPPORTED_LEAGUES)
            self.assertIn(name, conservative_bet_filter.PER_MARKET_APPROVAL_LEAGUES)
            self.assertNotIn(name, conservative_bet_filter.DOMESTIC_LEAGUES)
            # Every league shares ranked-mode extra odds reservations.
            self.assertIn(key, goal_market_validation.SUPPORTED_COMPETITIONS)

    def test_every_league_shares_the_unchanged_odds_request_budget(self):
        from goal_market_validation import distribute_event_odds_budget
        budget = distribute_event_odds_budget(list(league_registry.LEAGUES), 24)
        self.assertEqual(budget, {'EPL': 3, 'LaLiga': 3, 'Bundesliga': 3, 'SerieA': 3, 'Ligue1': 3, 'UCL': 3,
                                  'UEL': 2, 'Eredivisie': 2, 'PrimeiraLiga': 2})
        self.assertEqual(sum(budget.values()), 24)


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
    def _sample(self):
        """Fixed eligible markets; production forecasts must not define test coverage."""
        import copy
        from test_asian_handicap import NOW, row
        from test_shortlist_market_alternatives import dc_fixture
        from test_win_first_shortlist import reports

        values = []
        for i, key in enumerate(('home_draw', 'draw_away', 'home_away')):
            value, evidence = dc_fixture(key)
            # Keep the quotes made by dc_fixture, but give each market a
            # distinct fixture so one-pick-per-fixture cannot hide a test case.
            identity = row(i)
            for field in ('fixture_id', 'home_team', 'away_team',
                          'model_home_team', 'model_away_team'):
                value[field] = identity[field]
            values.append(value)
        values.append(row(3))
        report = copy.deepcopy(evidence['Premier League'])
        report['asian_handicap_win'] = reports()['Premier League']['asian_handicap_win']
        report['markets']['draw'] = copy.deepcopy(report['markets']['home'])
        report['league'] = 'Serie A'
        return pd.DataFrame(values).assign(league='Serie A'), {'Serie A': report}, NOW

    @staticmethod
    def _evidence(reliability, failed_markets, failed_lines):
        """A fully passing report with chosen markets and Asian handicap lines failed."""
        import copy
        report = copy.deepcopy(reliability['Serie A'])
        assert all(m['status'] == 'RELIABLE_FOR_RANKING' for m in report['markets'].values())
        for key in failed_markets:
            report['markets'][key]['status'] = 'UNRELIABLE_AUDIT'
        for line in failed_lines:
            report['asian_handicap_win']['markets'][line]['status'] = 'UNRELIABLE_AUDIT'
            report['asian_handicap']['markets'].get(line, {})['status'] = 'UNRELIABLE_AUDIT'
        return report

    def test_only_markets_that_passed_their_own_audit_reach_the_shortlist(self):
        from conservative_bet_filter import build_conservative_shortlist
        from per_market_shortlist import POLICY as V24
        predictions, reliability, as_of = self._sample()
        control, _, _ = build_conservative_shortlist(predictions, as_of=as_of, market_reliability=reliability,
                                                     selection_policy_version=V24)
        self.assertIn('Double Chance 12', set(control.market), 'control: DC 12 must be selectable')
        ah_picks = sorted(m for m in control.market if m.startswith('Asian'))
        self.assertTrue(ah_picks, 'control: an Asian handicap line must be selectable')
        failed_lines = ah_picks[:1]
        for key, (name, _, _) in NEW.items():
            with self.subTest(league=key):
                evidence = {name: self._evidence(reliability, ('home_away', 'draw'), failed_lines)}
                picks, decisions, _ = build_conservative_shortlist(
                    predictions.assign(league=name), as_of=as_of, market_reliability=evidence,
                    selection_policy_version=V24)
                self.assertGreater(len(picks), 0, 'passing markets may be shortlisted')
                self.assertTrue(set(picks.market) & {'Home win', 'Away win', 'Double Chance 1X', 'Double Chance X2'})
                self.assertNotIn('Double Chance 12', set(picks.market))
                self.assertFalse(set(failed_lines) & set(picks.market))
                blocked = decisions.loc[decisions.market.eq('Double Chance 12')]
                self.assertTrue(len(blocked) and blocked.decision.eq('REJECTED').all())
                self.assertTrue(blocked.rejection_reasons.str.contains(
                    'market historical reliability: UNRELIABLE_AUDIT').all())
                line = decisions.loc[decisions.market.isin(failed_lines)]
                self.assertTrue(len(line) and line.decision.eq('REJECTED').all())
                self.assertTrue(line.rejection_reasons.str.contains(
                    'Asian handicap profitable-win validation unavailable or failed').all())

    def test_failed_markets_stay_blocked_in_every_replayable_policy(self):
        """Archived policies admit failed audits as PROVISIONAL warnings for the
        original leagues; a per-market league never gets that path."""
        from conservative_bet_filter import (build_conservative_shortlist, LEGACY_SELECTION_POLICY_VERSION,
                                             PREVIOUS_SELECTION_POLICY_VERSION, SELECTION_POLICY_VERSION,
                                             PROBABILITY_SELECTION_POLICY_VERSION, BALANCED_SELECTION_POLICIES)
        from asian_handicap import POLICIES
        predictions, reliability, as_of = self._sample()
        name = NEW['Eredivisie'][0]
        failed = ('home_away', 'draw', 'over_1_5', 'under_3_5', 'btts_yes')
        lines = sorted(reliability['Serie A']['asian_handicap_win']['markets'])
        report = self._evidence(reliability, failed, lines)
        allowed = {'Home win', 'Away win', 'Double Chance 1X', 'Double Chance X2'}
        keys = {'Home win': 'home', 'Away win': 'away', 'Double Chance 1X': 'home_draw', 'Double Chance X2': 'draw_away'}
        for version in (LEGACY_SELECTION_POLICY_VERSION, PREVIOUS_SELECTION_POLICY_VERSION, SELECTION_POLICY_VERSION,
                        PROBABILITY_SELECTION_POLICY_VERSION, *BALANCED_SELECTION_POLICIES, *POLICIES):
            with self.subTest(policy=version):
                picks, decisions, _ = build_conservative_shortlist(
                    predictions.assign(league=name), as_of=as_of, market_reliability={name: report},
                    selection_policy_version=version)
                self.assertTrue(set(picks.market) <= allowed, set(picks.market) - allowed)
                for pick in picks.itertuples():
                    p = float(pick.predicted_probability)
                    if p >= .75:
                        tier = '85plus' if p >= .85 else '75plus'
                        self.assertEqual(report['markets'][keys[pick.market]]['high_confidence'][tier]['status'],
                                         'PASSED', (version, pick.market, p))
                blocked = decisions.loc[decisions.market.isin({'Double Chance 12', 'Over 1.5', 'Under 3.5'})]
                self.assertTrue(blocked.decision.eq('REJECTED').all())
                self.assertTrue(blocked.rejection_reasons.str.contains('per-market approval: market audit').all())

    def test_no_report_or_missing_league_report_blocks_every_market(self):
        from conservative_bet_filter import build_conservative_shortlist, LEGACY_SELECTION_POLICY_VERSION
        from per_market_shortlist import POLICY as V24
        from asian_handicap import POLICY as V22
        predictions, reliability, as_of = self._sample()
        # Both leagues: no report at all, and a report map that lacks the league.
        cases = [(key, V24, evidence) for key in NEW for evidence in (None, {})]
        # One league covers the other policy paths; the code path is per league name.
        # The evidence map intentionally lacks the tested league.
        others = {k: v for k, v in reliability.items() if k != NEW['Eredivisie'][0]}
        cases += [('Eredivisie', V24, others), ('Eredivisie', V22, None),
                  ('Eredivisie', LEGACY_SELECTION_POLICY_VERSION, None)]
        for key, version, market_reliability in cases:
            name = NEW[key][0]
            with self.subTest(league=key, policy=version, evidence=market_reliability):
                picks, decisions, _ = build_conservative_shortlist(
                    predictions.assign(league=name), as_of=as_of, market_reliability=market_reliability,
                    selection_policy_version=version)
                self.assertEqual(len(picks), 0)
                self.assertTrue(decisions.decision.ne('SHORTLISTED').all())
                if version == LEGACY_SELECTION_POLICY_VERSION:
                    # Without any report the per-market rule names the missing evidence.
                    self.assertTrue(decisions.rejection_reasons.str.contains(
                        'per-market approval: market audit NOT_ASSESSED').all())

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
