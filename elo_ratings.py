"""Venue-aware Elo power ratings from the Dixon-Coles training history.

Each team has an overall rating plus home and away ratings. A fixture uses

    R_eff = (1 - v) * R_overall + v * R_venue          (v = venue_weight)

and the home expected score is

    E_home = 1 / (1 + 10 ** (-(R_eff_home + HFA - R_eff_away) / 400)).

After a result (S = 1 / 0.5 / 0 for a home win / draw / loss) the update is
``delta = K * G * (S - E_home)``, added to the home team's overall and home
ratings and subtracted from the away team's overall and away ratings.
``G`` is the World Football Elo margin multiplier: 1 for a margin of 0-1,
1.5 for 2, ``(11 + N) / 8`` for N >= 3.

Two football-specific adjustments:
  * teams first seen after the league is established (usually promoted)
    enter at the 25th percentile of existing ratings, not the average;
  * after a gap of ``season_gap_days`` every rating regresses towards the
    mean by ``season_regression`` to absorb summer squad turnover.

Ratings are informational fixture features. They do not alter Dixon-Coles
probabilities, market blending or selection.
"""
from __future__ import annotations

import math
from dataclasses import dataclass, field
from typing import Dict, Optional

import numpy as np
import pandas as pd

VERSION = 'venue-elo-v1'
ENTRY_PERCENTILE = 25.0


@dataclass
class EloRatings:
    k_factor: float = 20.0
    home_advantage: float = 60.0
    initial_rating: float = 1500.0
    venue_weight: float = 0.5
    season_regression: float = 0.2
    season_gap_days: float = 45.0
    overall: Dict[str, float] = field(default_factory=dict)
    home: Dict[str, float] = field(default_factory=dict)
    away: Dict[str, float] = field(default_factory=dict)
    matches: int = 0
    last_date: Optional[pd.Timestamp] = None

    def __post_init__(self):
        if not self.k_factor > 0:
            raise ValueError('k_factor must be positive')
        if not 0 <= self.venue_weight <= 1 or not 0 <= self.season_regression <= 1:
            raise ValueError('venue_weight and season_regression must be in [0, 1]')

    @staticmethod
    def expected_score(rating_difference: float) -> float:
        return 1.0 / (1.0 + 10.0 ** (-rating_difference / 400.0))

    @staticmethod
    def margin_multiplier(goal_difference: int) -> float:
        margin = abs(int(goal_difference))
        return 1.0 if margin <= 1 else 1.5 if margin == 2 else (11.0 + margin) / 8.0

    def _entry(self) -> float:
        if not self.overall:
            return self.initial_rating
        return float(np.percentile(list(self.overall.values()), ENTRY_PERCENTILE))

    def _ensure(self, team: str) -> None:
        if team not in self.overall:
            start = self._entry()
            self.overall[team] = self.home[team] = self.away[team] = start

    def knows(self, team) -> bool:
        return team in self.overall

    def rating(self, team: str, venue: str) -> float:
        """Effective venue rating; unseen teams use the entry rating."""
        if team not in self.overall:
            return self._entry()
        specific = (self.home if venue == 'home' else self.away)[team]
        return (1 - self.venue_weight) * self.overall[team] + self.venue_weight * specific

    def home_expectancy(self, home: str, away: str) -> float:
        return self.expected_score(self.rating(home, 'home') + self.home_advantage
                                   - self.rating(away, 'away'))

    def _regress(self) -> None:
        mean = float(np.mean(list(self.overall.values())))
        for table in (self.overall, self.home, self.away):
            for team in table:
                table[team] += self.season_regression * (mean - table[team])

    def update(self, date, home: str, away: str, home_goals: int, away_goals: int) -> float:
        """Apply one completed match in kickoff order; return the rating change."""
        date = pd.Timestamp(date)
        if self.last_date is not None:
            if date < self.last_date:
                raise ValueError('Elo updates must be applied in kickoff order')
            if self.overall and (date - self.last_date).days >= self.season_gap_days:
                self._regress()
        self._ensure(home)
        self._ensure(away)
        expected = self.home_expectancy(home, away)
        score = 1.0 if home_goals > away_goals else 0.5 if home_goals == away_goals else 0.0
        delta = self.k_factor * self.margin_multiplier(home_goals - away_goals) * (score - expected)
        self.overall[home] += delta
        self.home[home] += delta
        self.overall[away] -= delta
        self.away[away] -= delta
        self.matches += 1
        self.last_date = date
        return delta

    def table(self) -> pd.DataFrame:
        teams = sorted(self.overall)
        return pd.DataFrame({'overall': [self.overall[t] for t in teams],
                             'home': [self.rating(t, 'home') for t in teams],
                             'away': [self.rating(t, 'away') for t in teams]},
                            index=pd.Index(teams, name='team')).sort_values('overall', ascending=False)


def _completed(history: pd.DataFrame) -> pd.DataFrame:
    frame = history.dropna(subset=['Date', 'HomeTeam', 'AwayTeam', 'FTHG', 'FTAG']).copy()
    frame['elo_date'] = pd.to_datetime(frame['Date'], utc=True).dt.tz_localize(None)
    return frame.sort_values('elo_date', kind='mergesort')


def fit_history(history: pd.DataFrame, **settings) -> EloRatings:
    """Ratings after every completed match in a training frame."""
    ratings = EloRatings(**settings)
    for row in _completed(history).itertuples(index=False):
        ratings.update(row.elo_date, str(row.HomeTeam), str(row.AwayTeam), int(row.FTHG), int(row.FTAG))
    return ratings


def pre_match_ratings(history: pd.DataFrame, **settings) -> pd.DataFrame:
    """Leakage-free ratings *before* each match, aligned to ``history.index``.

    Suitable as walk-forward features: a match's row never includes its result.
    """
    ratings = EloRatings(**settings)
    rows = {}
    for idx, row in _completed(history).iterrows():
        home, away = str(row['HomeTeam']), str(row['AwayTeam'])
        rows[idx] = fixture_features(ratings, home, away, require_known=False)
        ratings.update(row['elo_date'], home, away, int(row['FTHG']), int(row['FTAG']))
    return pd.DataFrame.from_dict(rows, orient='index').reindex(history.index)


def fixture_features(ratings: EloRatings, home: Optional[str], away: Optional[str],
                     require_known: bool = True) -> dict:
    """Prediction-row columns; ``None`` when a team has no rating history."""
    empty = dict.fromkeys(('elo_home_rating', 'elo_away_rating', 'elo_rating_diff',
                           'elo_home_expectancy'))
    if require_known and not (ratings.knows(home) and ratings.knows(away)):
        return empty
    home_rating, away_rating = ratings.rating(home, 'home'), ratings.rating(away, 'away')
    diff = home_rating + ratings.home_advantage - away_rating
    if not math.isfinite(diff):
        return empty
    return {'elo_home_rating': home_rating, 'elo_away_rating': away_rating,
            'elo_rating_diff': diff, 'elo_home_expectancy': ratings.expected_score(diff)}


def diagnostics(ratings: EloRatings) -> dict:
    return {'version': VERSION, 'teams': len(ratings.overall), 'matches': ratings.matches,
            'k_factor': ratings.k_factor, 'home_advantage': ratings.home_advantage,
            'venue_weight': ratings.venue_weight, 'season_regression': ratings.season_regression,
            'last_match_date': None if ratings.last_date is None else str(ratings.last_date.date())}
