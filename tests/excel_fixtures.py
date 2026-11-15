"""A synthetic post-release output root for the performance workbook: two archived runs (one before the new
master's release, one after), both lists' graded picks across the start, and the monitoring and health files.

Used by tests/test_performance_report_layout.py and to generate the evidence workbook for the PR."""
from __future__ import annotations

import csv
import json
from pathlib import Path

PRE_RELEASE = '2026-11-08T12:20:11+00:00'
START = '2026-11-16T09:00:00+00:00'  # the first archived run of the released new master
LATER = '2026-11-21T09:00:00+00:00'

NEW_COLUMNS = ['new_master_rank', 'new_master_tier', 'new_master_labels', 'kickoff_utc', 'league', 'home_team',
               'away_team', 'market_to_bet', 'bookmaker', 'offered_decimal_odds', 'ranking_no_loss_probability',
               'ranking_profit_probability', 'in_value_shortlist', 'in_cagey_tier', 'in_old_master',
               'snapshot_generated_utc', 'final_score', 'result_status', 'unit_profit', 'clv', 'new_master_version']
OLD_COLUMNS = ['master_rank', 'kickoff_utc', 'league', 'home_team', 'away_team', 'market_to_bet', 'bookmaker',
               'offered_decimal_odds', 'master_no_loss_probability', 'master_profit_probability', 'master_price_flag',
               'in_value_shortlist', 'in_cagey_tier', 'snapshot_generated_utc', 'final_score', 'result_status',
               'unit_profit', 'clv']

# (generated, kickoff, league, home, away, bet, odds, tier, labels, no-loss, profit p, score, status, profit, clv)
NEW_PICKS = [
    (PRE_RELEASE, '2026-11-08T17:00:00+00:00', 'Premier League', 'Old FC', 'Before United', 'Asian Handicap Home +0.50',
     1.25, 'safe', 'both agree', 0.80, 0.80, '1-0', 'WON', 0.25, 0.01),  # before the start: never shown
    (START, '2026-11-17T19:00:00+00:00', 'Premier League', 'Arsenal', 'Chelsea', 'Asian Handicap Home +0.00', 1.20,
     'safe', 'both agree', 0.84, 0.62, '2-1', 'WON', 0.20, 0.02),
    (START, '2026-11-17T19:30:00+00:00', 'La Liga', 'Villarreal', 'Getafe', 'Asian Handicap Home +0.25', 1.24, 'safe',
     'research strongly disagrees', 0.81, 0.63, '0-0', 'HALF_LOST', -0.5, -0.03),
    (START, '2026-11-18T18:00:00+00:00', 'Serie A', 'Genoa', 'AC Milan', 'Double Chance X2', 1.30, 'fill',
     'unvalidated view', 0.66, 0.66, '2-0', 'LOST', -1.0, None),
    (START, '2026-11-18T20:45:00+00:00', 'Bundesliga', 'Freiburg', 'Union Berlin', 'Asian Handicap Away +1.00', 1.45,
     'risky fill', 'one view missing; risky fill', 0.58, 0.41, '1-0', 'REFUNDED', 0.0, 0.00),
    (LATER, '2026-11-24T19:00:00+00:00', 'Ligue 1', 'Rennes', 'Lille', 'Asian Handicap Away +1.25', 1.26, 'safe', '',
     0.79, 0.79, '1-1', 'HALF_WON', 0.13, 0.04),
    (LATER, '2026-11-25T19:00:00+00:00', 'Eredivisie', 'Utrecht', 'NEC', 'Asian Handicap Home +1.00', 1.26, 'safe',
     'both agree', 0.81, 0.63, '', 'PENDING_KICKOFF_OR_FINAL_SCORE', '', ''),
]
OLD_PICKS = [
    (PRE_RELEASE, '2026-11-08T17:00:00+00:00', 'Premier League', 'Old FC', 'Before United', 'Home win', 1.6, '', '',
     0.62, 0.62, '1-0', 'WON', 0.6, None),  # before the start: never shown
    (START, '2026-11-17T19:00:00+00:00', 'Premier League', 'Arsenal', 'Chelsea', 'Double Chance 1X', 1.15, '', '',
     0.87, 0.87, '2-1', 'WON', 0.15, 0.01),
    (START, '2026-11-18T20:00:00+00:00', 'Serie A', 'Lazio', 'Roma', 'Away win', 1.95, '', '', 0.51, 0.51, '2-0',
     'LOST', -1.0, -0.02),
    (LATER, '2026-11-24T20:00:00+00:00', 'La Liga', 'Sevilla', 'Betis', 'Asian Handicap Home +0.50', 1.40, '', '',
     0.71, 0.71, '3-1', 'WON', 0.40, 0.03),
]


def _write_csv(path: Path, columns, rows) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('w', encoding='utf-8', newline='') as handle:
        writer = csv.writer(handle)
        writer.writerow(columns)
        writer.writerows(rows)


def _json(path: Path, data) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2), encoding='utf-8')


def snapshot(root: Path, name: str, generated: str, version: str) -> None:
    _json(root / 'performance' / 'snapshots' / name / 'selection_summary.json',
          {'generated_at_utc': generated, 'master_shortlist': {'version': version}})


def archive_research_run(root: Path, name: str, generated: str, european: str | None, domestic: str | None) -> None:
    """An archived run whose forecasts carry these research versions (None: no forecast in that scope)."""
    folder = Path(root) / 'performance' / 'snapshots' / name
    _json(folder / 'metadata.json', {'generated_at_utc': generated, 'git_commit_sha': name})
    rows = [[league, json.dumps({'version': version})] for league, version in
            (('UEFA Champions League', european), ('Premier League', domestic)) if version]
    _write_csv(folder / 'predictions.csv', ['league', 'team_research_json'], rows)


def post_release_root(root: Path, ce3n: dict | None = None, released: bool = True) -> Path:
    """A synthetic output root after the new master's release (released=False: no post-release run yet)."""
    import master_shortlist as ms
    root = Path(root)
    snapshot(root, 'aaaaaaaaaaaaaaaa', PRE_RELEASE, 'master-profit-15-context-v8')
    if released:
        snapshot(root, 'bbbbbbbbbbbbbbbb', START, ms.VERSION_NEW_LIVE)
        snapshot(root, 'cccccccccccccccc', LATER, ms.VERSION_NEW_LIVE)
    new = [[i, tier, labels, kickoff, league, home, away, bet, 'Pinnacle', odds, nl, pp,
            str(i % 2 == 0), 'True', str(home in ('Arsenal', 'Old FC')), generated, score, status, profit,
            '' if clv is None else clv, ms.VERSION_NEW_LIVE]
           for i, (generated, kickoff, league, home, away, bet, odds, tier, labels, nl, pp, score, status, profit, clv)
           in enumerate(NEW_PICKS, start=1)]
    old = [[i, kickoff, league, home, away, bet, 'Pinnacle', odds, nl, pp, 'negative market EV nomination', 'True',
            str(i % 2 == 1), generated, score, status, profit, '' if clv is None else clv]
           for i, (generated, kickoff, league, home, away, bet, odds, _, _, nl, pp, score, status, profit, clv)
           in enumerate(OLD_PICKS, start=1)]
    tracking = root / 'performance' / 'price_edge_v27'
    _write_csv(tracking / 'master_shortlist_picks.csv', NEW_COLUMNS, new)
    _write_csv(tracking / 'master_shortlist_old_picks.csv', OLD_COLUMNS, old)
    _json(tracking / 'summary.json', {
        'live_master_list': 'new', 'reviewed_at_utc': '2026-11-26T07:30:00+00:00',
        'master_rollback': {'status': 'WAITING', 'triggered': False, 'min_graded_matches': 150, 'min_weeks': 3,
                            'difference': None, 'interval_95': None, 'live_master_list': 'new',
                            'new_master': {'graded_matches': 6, 'weeks': 2},
                            'old_master': {'graded_matches': 64, 'weeks': 3},
                            'message': 'Not triggered: waiting for at least 150 graded matches over at least 3 weeks '
                                       'on each list.', 'rule': 'After at least 150 graded matches ...'},
        'master_release_incidents': {'new_master_failed': {'runs': 0}, 'baseline_missing': {'runs': 0},
                                     'messages': []}})
    _json(root / 'performance' / 'research_v5_monitoring.json', {
        'version': 'research-v5-monitoring-v1',
        'rollback': {'eligible': False, 'triggered': False, 'matches': 12, 'weeks': 2, 'interval_95': None,
                     'v5_minus_v4_log_loss': -0.0021, 'coverage': {'offers': 40}, 'rule': 'After at least 150 ...'},
        'home_favourites': {'all': {'fixtures': 4, 'picks': 3, 'graded': 2, 'v5_predicted_home_win': 0.61,
                                    'v4_predicted_home_win': 0.58, 'actual_home_win': 0.5},
                            'by_league': {'Eredivisie': {'fixtures': 4, 'picks': 3, 'graded': 2,
                                                         'v5_predicted_home_win': 0.61, 'v4_predicted_home_win': 0.58,
                                                         'actual_home_win': 0.5}}},
        **({'ce3n': ce3n} if ce3n is not None else {})})
    _json(root / 'performance' / 'metrics.json', {'reviewed_at_utc': '2026-11-26T07:30:00+00:00',
                                                  'provider_errors': {}})
    _json(root / 'performance' / 'pipeline_health.json', {
        'reviewed_at_utc': '2026-11-26T07:30:00+00:00',
        'forecast_freshness': {'generated_at_utc': LATER, 'age_hours': 118.5, 'status': 'OLDER_THAN_24_HOURS',
                               'upcoming_fixture_count': 3},
        'training': {'EPL': {'training_end': '2026-11-22', 'days_since_latest_result': 4, 'training_matches': 2000,
                             'current_source_health': {'status': 'CURRENT_WITHIN_PROVIDER_SCHEDULE'}}}})
    _json(root / 'performance' / 'workflow_health.json', {'status': 'VERIFIED_WITH_WARNINGS',
                                                          'reviewed_at_utc': '2026-11-26T07:30:00Z',
                                                          'warnings': ['UEL: example warning']})
    log = root / 'odds_api_usage' / 'usage_log.jsonl'
    log.parent.mkdir(parents=True, exist_ok=True)
    log.write_text('\n'.join(json.dumps(r) for r in [
        {'recorded_at_utc': START, 'workflow': 'scheduled-forecasts', 'outcome': 'FORECASTS_WRITTEN',
         'forecast_rows': 36, 'all_keys_exhausted': False,
         'slots': {'THE_ODDS_API_KEY': {'remaining': 18000, 'used': 2000, 'observed_at_utc': START}}},
        {'recorded_at_utc': LATER, 'workflow': 'scheduled-forecasts', 'outcome': 'NO_FIXTURES', 'forecast_rows': 0,
         'message': 'No fixtures in the next 3 days; nothing to forecast', 'all_keys_exhausted': False,
         'slots': {'THE_ODDS_API_KEY': {'remaining': 17712, 'used': 2288, 'observed_at_utc': LATER}}},
    ]) + '\n', encoding='utf-8')
    return root
