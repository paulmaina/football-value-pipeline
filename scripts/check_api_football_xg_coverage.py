"""Rerun 2026-11-12 after the daily reset.
Check whether API-Football fixture statistics carry expected_goals for the holdout leagues.

Read-only probe for Phase 2b. For each league and season it makes one fixture-list
request and samples three finished fixtures (early, middle, late) for statistics.
At most 1 + 3 x 3 x 4 = 37 requests on the default seasons. Prints a JSON report;
it never writes to .football_cache and never prints the key.
"""
import json
import os
import sys
import time

import requests

BASE = 'https://v3.football.api-sports.io'
LEAGUES = {'Eredivisie': 88, 'PrimeiraLiga': 94, 'SuperLig': 203}
FINISHED = {'FT', 'AET', 'PEN'}


def get(path, params, key):
    response = requests.get(BASE + path, params=params, headers={'x-apisports-key': key}, timeout=(10, 30))
    remaining = response.headers.get('x-ratelimit-requests-remaining')
    data = response.json() if response.content else {}
    errors = data.get('errors')
    if errors:
        # Only error categories, never provider text (it can echo credentials).
        return None, sorted(errors) if isinstance(errors, dict) else ['error'], remaining
    return data, None, remaining


def main(seasons=(2022, 2023, 2024)):
    key = os.environ.get('API_FOOTBALL_KEY', '').strip()
    if not key:
        print(json.dumps({'error': 'API_FOOTBALL_KEY not set'}))
        return 1
    report = {'seasons_checked': list(seasons), 'leagues': {}, 'requests_used': 0}
    status, errors, remaining = get('/status', {}, key)
    if status:
        account = (status.get('response') or {})
        report['plan'] = (account.get('subscription') or {}).get('plan')
        report['daily_limit'] = (account.get('requests') or {}).get('limit_day')
        report['used_today_before'] = (account.get('requests') or {}).get('current')
    for league, league_id in LEAGUES.items():
        report['leagues'][league] = {}
        for season in seasons:
            entry = {}
            data, errors, remaining = get('/fixtures', {'league': league_id, 'season': season}, key)
            report['requests_used'] += 1
            time.sleep(7)
            if errors:
                entry['fixtures_error'] = errors
                report['leagues'][league][season] = entry
                continue
            finished = [f for f in data.get('response') or [] if f['fixture']['status']['short'] in FINISHED]
            finished.sort(key=lambda f: f['fixture']['date'])
            entry['fixtures_finished'] = len(finished)
            samples = [finished[i] for i in sorted({0, len(finished) // 2, len(finished) - 1})] if finished else []
            entry['samples'] = []
            for fixture in samples:
                stats, errors, remaining = get('/fixtures/statistics', {'fixture': fixture['fixture']['id']}, key)
                report['requests_used'] += 1
                time.sleep(7)
                if errors:
                    entry['samples'].append({'date': fixture['fixture']['date'][:10], 'error': errors})
                    continue
                values = {team.get('team', {}).get('name'): next(
                    (s.get('value') for s in team.get('statistics', []) if s.get('type') == 'expected_goals'), None)
                    for team in stats.get('response') or []}
                entry['samples'].append({'date': fixture['fixture']['date'][:10],
                                         'match': f"{fixture['teams']['home']['name']} v {fixture['teams']['away']['name']}",
                                         'has_statistics': bool(stats.get('response')),
                                         'expected_goals': values})
            entry['xg_in_samples'] = sum(1 for s in entry['samples']
                                         if s.get('expected_goals') and all(v not in (None, '') for v in s['expected_goals'].values()))
            report['leagues'][league][season] = entry
    report['requests_remaining_today'] = remaining
    print(json.dumps(report, indent=2))
    return 0


if __name__ == '__main__':
    sys.exit(main())
