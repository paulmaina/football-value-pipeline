"""Model team resolution is league-scoped and fails closed (audit section 1.2).

"Sporting Lisbon" once resolved to Porto at fuzzy score 72, and unknown
teams were silently priced with league-average ratings.
"""
from offline_test_case import OfflineQuotePolicyTestCase
from datetime import datetime, timedelta, timezone
import json
from pathlib import Path
import unittest
from types import SimpleNamespace
from unittest.mock import Mock, patch

import numpy as np
import pandas as pd

from football_value_pipeline_v2_standalone import LEAGUES, DixonColesModel, FootballValuePipelineV2


def model_with(teams, league_key):
    model = DixonColesModel()
    model.teams = list(teams)
    model.team_to_idx = {team: i for i, team in enumerate(model.teams)}
    model.attack = model.weakness = np.zeros(len(model.teams))
    model.base = model.home_adv = model.rho = 0.
    model.league_key = league_key
    return model


PRIMEIRA = ["Porto", "Sp Lisbon", "Benfica", "Sp Braga", "Guimaraes", "Famalicao"]


class ResolutionTests(OfflineQuotePolicyTestCase):
    def test_sporting_lisbon_resolves_to_sporting_never_porto(self):
        model = model_with(PRIMEIRA, "PrimeiraLiga")
        self.assertEqual(model.resolve_team("Sporting Lisbon"), ("Sp Lisbon", 100.0))
        # Without Sporting in training it fails closed instead of picking Porto.
        model = model_with([t for t in PRIMEIRA if t != "Sp Lisbon"], "PrimeiraLiga")
        team, score = model.resolve_team("Sporting Lisbon")
        self.assertIsNone(team)
        self.assertLess(score, 90)

    def test_aek_athens_resolves_to_pae_aek_in_ucl_only(self):
        model = model_with(["PAE AEK", "Sporting Clube de Portugal"], "UCL")
        self.assertEqual(model.resolve_team("AEK Athens"), ("PAE AEK", 100.0))
        model.league_key = "EPL"
        self.assertIsNone(model.resolve_team("AEK Athens")[0])

    def test_reported_uel_feed_names_resolve_to_training_names(self):
        training = json.loads(Path(".football_cache/europa/training.json").read_text(encoding="utf-8"))
        teams = sorted({m[side] for m in training["matches"] for side in ("home", "away")})
        model = model_with(teams, "UEL")
        expected = {
            "Besiktas JK": "besiktas", "Ferencváros TC": "ferencvaros", "Sparta Prague": "sparta praha",
            "SK Sturm Graz": "sturm graz", "TSG Hoffenheim": "hoffenheim", "NK Celje": "celje",
            "Omonoia FC": "omonia", "PFC Levski Sofia": "levski sofia",
            "Jagiellonia Białystok": "jagiellonia", "Hapoel Be'er Sheva": "h. beer-sheva",
            "FC Ararat-Armenia": "ararat-armenia",
        }
        for feed, name in expected.items():
            with self.subTest(feed):
                self.assertEqual(model.resolve_team(feed), (name, 100.0))

    def test_fortuna_sittard_resolves_in_eredivisie(self):
        # Scored 84.6 against "For Sittard": correct, but below the floor without an alias.
        model = model_with(["For Sittard", "Excelsior", "Sparta Rotterdam"], "Eredivisie")
        self.assertEqual(model.resolve_team("Fortuna Sittard"), ("For Sittard", 100.0))

    def test_football_data_org_names_resolve_to_the_right_team(self):
        # football-data.org spellings that matched the wrong team (Espanyol scored
        # 90 against Barcelona) or fell below the floor with the right one.
        cases = {
            "LaLiga": (["Barcelona", "Espanol", "Villarreal"], {"RCD Espanyol de Barcelona": "Espanol"}),
            "Ligue1": (["Rennes", "Lens", "Lille"], {"Stade Rennais FC 1901": "Rennes"}),
            "Eredivisie": (["Nijmegen", "Almere City", "Ajax"], {"NEC": "Nijmegen"}),
            "PrimeiraLiga": (PRIMEIRA + ["Estoril"], {"Sporting Clube de Portugal": "Sp Lisbon",
                                                     "Sporting Clube de Braga": "Sp Braga",
                                                     "Vitória SC": "Guimaraes"}),
        }
        for league, (teams, expected) in cases.items():
            model = model_with(teams, league)
            for feed, name in expected.items():
                with self.subTest(league=league, feed=feed):
                    self.assertEqual(model.resolve_team(feed), (name, 100.0))

    def test_fuzzy_floor_is_90(self):
        model = model_with(["Porto", "Benfica"], "PrimeiraLiga")
        self.assertEqual(model.resolve_team.__defaults__, (90.0,))
        # Scored 72 against "porto" under the old floor.
        self.assertIsNone(model.resolve_team("Sporting Lisbon")[0])


class FailClosedTests(OfflineQuotePolicyTestCase):
    NOW = datetime.now(timezone.utc)

    def run_pipeline(self, model):
        pipeline = object.__new__(FootballValuePipelineV2)
        for key, value in dict(half_life_days=480, l2=0.08, max_goals=10, devig_method="power",
                market_weight=0.7, fixture_provider="auto", odds_regions="eu",
                extra_event_odds_requests=0, max_extra_event_odds_requests=24,
                extra_event_odds_quota={"UCL": 4}, extra_event_odds_by_league={},
                additional_odds_coverage="all").items():
            setattr(pipeline, key, value)
        pipeline._training_health = Mock(return_value={"status": "OFFLINE_TEST"})
        pipeline._history_for_league = Mock(return_value=pd.DataFrame(
            columns=["Date", "HomeTeam", "AwayTeam", "FTHG", "FTAG"]))
        kickoff = (self.NOW + timedelta(hours=30)).isoformat()
        pipeline._current_fixtures = Mock(return_value=pd.DataFrame([
            dict(Date=pd.Timestamp(kickoff[:10]), kickoff_utc=kickoff, HomeTeam=h, AwayTeam=a)
            for h, a in (("PAE AEK", "Unknown Club"), ("AEK Athens", "Sporting Lisbon"))]))
        pipeline._attach_live_odds = lambda fixtures, *args: fixtures
        predicted = []
        def predict(_, row):
            predicted.append((row["HomeTeam"], row["AwayTeam"]))
            return dict(home_name_match_score=100, away_name_match_score=100), {}
        pipeline._predict_row = predict
        pipeline.odds_api = None
        model.training_matches, model.training_end, model.fit_result = 100, None, None
        model.half_life_days, model.max_goals = 480, 10
        with patch("football_value_pipeline_v2_standalone.DixonColesModel") as model_class, \
                self.assertWarnsRegex(RuntimeWarning, "Unknown Club"):
            model_class.return_value.fit.return_value = model
            frame, diagnostics, _ = pipeline.run_league("UCL", self.NOW)
        return predicted, frame, diagnostics

    def test_unknown_team_is_excluded_not_averaged(self):
        model = model_with(["PAE AEK", "Sporting Clube de Portugal"], "UCL")
        predicted, frame, diagnostics = self.run_pipeline(model)
        self.assertEqual(predicted, [("AEK Athens", "Sporting Lisbon")])
        self.assertEqual(frame["home_team"].tolist(), ["AEK Athens"])
        excluded = diagnostics["excluded_unresolved_team_fixtures"]
        self.assertEqual([(x["home_team"], x["away_team"], x["unresolved"]) for x in excluded],
                         [("PAE AEK", "Unknown Club", ["away"])])
        self.assertNotIn("__LEAGUE_AVERAGE__", frame.to_string())


if __name__ == "__main__":
    unittest.main()
