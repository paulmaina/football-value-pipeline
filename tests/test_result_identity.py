"""Result matching recovers renamed clubs, and each verified match is graded once."""
import unittest

import performance_tracking as pt
from performance_tracking import (
    DUPLICATE_RESULT, alias_match, fixture_match, mark_duplicate_results, result_identity,
)

KICK = "2026-10-25T13:00:00+00:00"


def result(match_id=1, home="Athletic Club", away="Getafe CF", kick=KICK, code="PD", **extra):
    return {"match_id": match_id, "league_code": code, "kickoff_utc": kick,
            "home_team": home, "away_team": away, "home_short_name": "", "away_short_name": "",
            "home_goals": 4, "away_goals": 0, "source": "football-data.org/v4",
            "source_status": "FINISHED", "source_duration": "REGULAR", **extra}


def row(home="Athletic Bilbao", away="Getafe", kick=KICK, league="La Liga", **extra):
    return {"league": league, "home_team": home, "away_team": away, "kickoff_utc": kick, **extra}


class AliasMatchTest(unittest.TestCase):
    def test_reviewed_alias_recovers_a_renamed_club(self):
        final, state = fixture_match(row(), [result()])
        self.assertEqual((final["match_id"], state), (1, "VERIFIED_FINISHED"))

    def test_both_sides_aliased(self):
        final, _ = fixture_match(
            row("Rennes", "Lille", league="Ligue 1"),
            [result(7, "Stade Rennais FC 1901", "Lille OSC", code="FL1")])
        self.assertEqual(final["match_id"], 7)

    def test_alias_is_scoped_to_its_competition(self):
        # "Athletic Bilbao" has no alias in Serie A, so nothing is recovered.
        self.assertIsNone(alias_match(row(league="Serie A"), [result(code="SA")], "SA"))

    def test_kickoff_must_match_exactly(self):
        moved = result(kick="2026-10-26T13:00:00+00:00")
        self.assertEqual(fixture_match(row(), [moved]), (None, "UNVERIFIED_FIXTURE_OR_RESULT"))

    def test_sides_keep_their_order(self):
        reversed_ = result(home="Getafe CF", away="Athletic Club")
        self.assertEqual(fixture_match(row(), [reversed_])[0], None)

    def test_unaliased_side_still_needs_a_close_name(self):
        other = result(away="Real Sociedad de Fútbol")
        self.assertIsNone(fixture_match(row(), [other])[0])

    def test_two_qualifying_results_fail_closed(self):
        self.assertIsNone(alias_match(row(), [result(1), result(2)], "PD"))

    def test_existing_matches_are_unchanged(self):
        final, _ = fixture_match(row("Valencia", "Getafe"), [result(3, "Valencia CF", "Getafe CF")])
        self.assertEqual(final["match_id"], 3)


class DuplicateResultTest(unittest.TestCase):
    def graded(self, key, kick, match_id=9):
        return {"fixture_key": key, "league": "Ligue 1", "kickoff_utc": kick, "status": "GRADED",
                "source_match_id": match_id, **{f: 0.1 for f in pt.PREDICTION_SCORE_FIELDS}}

    def test_one_forecast_per_verified_match_keeps_its_scores(self):
        records = [result(9, "Toulouse FC", "ES Troyes AC", kick="2026-10-25T16:15:00+00:00", code="FL1")]
        stale = self.graded("Ligue 1|toulouse|troyes|2026-10-24", "2026-10-24T15:15:00+00:00")
        exact = self.graded("Ligue 1|toulouse|troyes|2026-10-25", "2026-10-25T16:15:00+00:00")
        other = self.graded("Ligue 1|lyon|nice|2026-10-18", "2026-10-18T18:45:00+00:00", match_id=10)
        originals = [{"snapshot_generated_utc": "2026-10-24T10:00:00+00:00"}] * 3
        graded = [stale, exact, other]
        mark_duplicate_results(originals, graded, records)
        self.assertEqual([r["status"] for r in graded], [DUPLICATE_RESULT, "GRADED", "GRADED"])
        self.assertTrue(all(stale[f] == "" for f in pt.PREDICTION_SCORE_FIELDS))
        self.assertEqual(exact["one_x_two_brier"], 0.1)

    def test_earliest_generation_breaks_a_kickoff_tie(self):
        first = self.graded("Ligue 1|fenerbahce sk|slavia prague|2026-10-20", KICK)
        later = self.graded("Ligue 1|fenerbahce|slavia prague|2026-10-20", KICK)
        originals = [{"snapshot_generated_utc": "2026-10-19T10:00:00+00:00"},
                     {"snapshot_generated_utc": "2026-10-20T08:00:00+00:00"}]
        graded = [later, first]
        mark_duplicate_results(originals[::-1], graded, [result(9, kick=KICK, code="FL1")])
        self.assertEqual([r["status"] for r in graded], [DUPLICATE_RESULT, "GRADED"])

    def test_ungraded_rows_are_left_alone(self):
        pending = {"fixture_key": "a", "league": "Ligue 1", "status": "UNVERIFIED_FIXTURE_OR_RESULT",
                   "source_match_id": ""}
        mark_duplicate_results([{}], [pending], [])
        self.assertEqual(pending["status"], "UNVERIFIED_FIXTURE_OR_RESULT")
        self.assertIsNone(result_identity(pending))


if __name__ == "__main__":
    unittest.main()
