"""Pre-kickoff strength evidence for the strong-team master (rule master-strong-team-v1, master_strong_config.json).

Reporting features only: nothing here changes a probability. Each function reads what the forecast froze before
kickoff (research_history_json, team_research_json, elo_home_expectancy) or, offline, the same structures built from
the harness's locked training rows, so the live shadow and the offline check use one definition.

- backed_side: the team a bet is on, its line from that team's side, and its market group.
- bet_record: the backed team's record on the exact bet over its last matches (team_research.form_history rows,
  completed earlier dates only), each past score settled with ah_close_backtest.settle.
- research_margin: the mean goal margin (home minus away) of the research view's margin distribution.
- elo_expectancy: the backed team's pre-match Elo expected score.
"""
from __future__ import annotations

import json
import math
from typing import Dict, Iterable, Mapping, Optional, Sequence, Tuple

import numpy as np

AH_PREFIX = 'Asian Handicap'
GROUPS = ('match_result', 'double_chance', 'asian_handicap')


def _number(value) -> Optional[float]:
    try:
        n = float(value)
    except (TypeError, ValueError):
        return None
    return n if math.isfinite(n) else None


def backed_side(market: Optional[str], handicap_side=None, handicap_line=None) -> Optional[Tuple[str, float, str]]:
    """(side, line from the backed team's side, market group) for a native master market, else None.

    Home win / Away win: line -0.5, group match_result; Double Chance 1X / X2: line +0.5, group double_chance;
    Asian Handicap Home/Away <line>: the handicap line (from the label, or handicap_line), group asian_handicap."""
    text = str(market or '').strip()
    if text == 'Home win':
        return 'home', -.5, 'match_result'
    if text == 'Away win':
        return 'away', -.5, 'match_result'
    if text == 'Double Chance 1X':
        return 'home', .5, 'double_chance'
    if text == 'Double Chance X2':
        return 'away', .5, 'double_chance'
    if text.startswith(AH_PREFIX):
        parts = text[len(AH_PREFIX):].split()
        side = parts[0].lower() if parts else str(handicap_side or '').lower()
        line = _number(parts[1]) if len(parts) > 1 else _number(handicap_line)
        if side in ('home', 'away') and line is not None:
            return side, line, 'asian_handicap'
    return None


def is_win_bet(line: float) -> bool:
    """Win bets need the backed team to win (line below 0); no-loss bets (line 0 or above) need it not to lose."""
    return line < 0


def decode(value) -> Dict:
    if isinstance(value, dict):
        return value
    if value is None or (isinstance(value, float) and not math.isfinite(value)):
        return {}
    try:
        out = json.loads(value)
    except (TypeError, ValueError):
        return {}
    return out if isinstance(out, dict) else {}


def _name(value) -> str:
    from team_research import name
    return name(value)


def team_margins(rows: Iterable[Mapping], team: str, limit: Optional[int] = None) -> list:
    """The team's goal margin (its goals minus its opponent's) in each row it played, newest first as given."""
    key, out = _name(team), []
    for r in rows:
        h, a = _number(r.get('home_goals')), _number(r.get('away_goals'))
        if h is None or a is None:
            continue
        if _name(r.get('home')) == key:
            out.append(h - a)
        elif _name(r.get('away')) == key:
            out.append(a - h)
        else:
            continue
        if limit is not None and len(out) >= limit:
            break
    return out


def settle_margins(margins: Sequence[float], line: float) -> Dict[str, object]:
    """The record of a bet at `line` over past margins: matches, stake shares won and not lost (a half win counts
    1/2 won, a half loss 1/2 lost, a push not lost and not won)."""
    from ah_close_backtest import settle
    if not len(margins):
        return {'matches': 0, 'won': 0., 'not_lost': 0., 'won_share': None, 'not_lost_share': None}
    won, lost = settle(np.asarray(margins, float), float(line))
    n = len(margins)
    return {'matches': n, 'won': float(won.sum()), 'not_lost': float(n - lost.sum()),
            'won_share': float(won.sum() / n), 'not_lost_share': float((n - lost.sum()) / n)}


def bet_record(rows: Iterable[Mapping], team: str, line: float, matches: int = 10) -> Dict[str, object]:
    """The backed team's record on a bet at `line` over its last `matches` games in `rows` (form_history rows,
    newest first)."""
    return settle_margins(team_margins(rows, team, matches), line)


def record_check(record: Mapping, line: float, rule: Mapping) -> Tuple[bool, str]:
    """(passed, reason) for the proven-record check (master_strong_config.json checks.proven_record)."""
    if record.get('matches', 0) < int(rule['min_matches']):
        return False, f"not enough history ({record.get('matches', 0)} of {int(rule['min_matches'])} matches)"
    if is_win_bet(line):
        share, floor, what = record['won_share'], float(rule['win_bets_min_won_share']), 'won'
    else:
        share, floor, what = record['not_lost_share'], float(rule['no_loss_bets_min_not_lost_share']), 'not lost'
    passed = share + 1e-9 >= floor
    return passed, f"{what} {share:.0%} of {record['matches']} (needs {floor:.0%})"


def history_from_forecast(forecast: Optional[Mapping], side: str) -> Tuple[list, list, Optional[str]]:
    """(the side's last matches, head-to-head rows, the side's history name) from a forecast's research_history_json;
    the name is the frozen training name (research v3 on) or the fixture name."""
    if forecast is None:
        return [], [], None
    history = decode(forecast.get('research_history_json'))
    teams = history.get('teams') if isinstance(history.get('teams'), dict) else {}
    team = teams.get(side) or forecast.get(f'{side}_team')
    return list(history.get(side) or []), list(history.get('h2h') or []), team


def research_margin(distribution) -> Optional[float]:
    """Mean home-minus-away goal margin of a margin distribution: a {margin: probability} mapping (as frozen in
    team_research_json) or a (margins, probabilities) pair (as the harness keeps it)."""
    if distribution is None:
        return None
    if isinstance(distribution, Mapping):
        pairs = [(_number(k), _number(v)) for k, v in distribution.items()]
    else:
        try:
            margins, probs = distribution
        except (TypeError, ValueError):
            return None
        pairs = [(_number(m), _number(p)) for m, p in zip(margins, probs)]
    pairs = [(m, p) for m, p in pairs if m is not None and p is not None and p >= 0]
    total = sum(p for _, p in pairs)
    if not pairs or not total > 0 or abs(total - 1) > 1e-3:
        return None
    return float(sum(m * p for m, p in pairs) / total)


def research_margin_from_forecast(forecast: Optional[Mapping]) -> Optional[float]:
    if forecast is None:
        return None
    return research_margin(decode(forecast.get('team_research_json')).get('margin_distribution'))


def backed_margin(margin: Optional[float], side: str, line: float) -> Optional[float]:
    """The research expected margin from the backed team's side, after its line: s * E[margin] + line."""
    if margin is None:
        return None
    return (margin if side == 'home' else -margin) + float(line)


def elo_expectancy(home_expectancy, side: str) -> Optional[float]:
    """The backed team's Elo expected score (draws one half): elo_home_expectancy for home, its complement for away."""
    e = _number(home_expectancy)
    if e is None or not 0 <= e <= 1:
        return None
    return e if side == 'home' else 1 - e
