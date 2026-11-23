"""The odds-provider adapter (odds_provider.py): off by default, normalised Pinnacle data from any provider,
byte-identical lists through any provider, every failover path, provenance and the reports.

Every response is mocked; no request reaches a provider and no real key is used.
"""
from __future__ import annotations

from offline_test_case import OfflineQuotePolicyTestCase
from datetime import datetime, timedelta, timezone
import io
import json
import os
from pathlib import Path
import tempfile
from unittest.mock import patch

import pandas as pd
import requests

import odds_provider as op
from football_value_pipeline_v2_standalone import LEAGUES, TheOddsAPI

KEYS = {'PINNAPI_API_KEY': 'pinnapi-secret-for-tests', 'PINNODDS_API_KEY': 'pinnodds-secret-for-tests',
        'THE_ODDS_API_KEY': 'oddsapi-secret-for-tests'}
EXHAUSTED = {'error_code': 'OUT_OF_USAGE_CREDITS', 'message': 'Usage quota has been reached.'}
EPL = LEAGUES['EPL']
PROVENANCE = ('odds_provider', 'odds_schedule_provider', 'odds_extra_markets_provider')


def stamp(when):
    return op.iso(when)


def response(status, payload, headers=None, url='https://example.test'):
    r = requests.Response()
    r.status_code = status
    r._content = json.dumps(payload).encode('utf-8')
    r.headers['Content-Type'] = 'application/json'
    for k, v in (headers or {}).items():
        r.headers[k] = str(v)
    r.url = url
    return r


class Clock:
    def __init__(self, when):
        self.when = when

    def __call__(self):
        return self.when

    def advance(self, **delta):
        self.when += timedelta(**delta)


class KitSession:
    """A kit provider: each get() returns the next reply (a Response, an exception, or 'board')."""

    def __init__(self, board, *replies):
        self.board, self.replies, self.calls = board, list(replies), []

    def get(self, url, params=None, headers=None, timeout=None):
        self.calls.append({'url': url, 'params': params, 'headers': headers})
        reply = self.replies.pop(0) if self.replies else 'board'
        if isinstance(reply, Exception):
            raise reply
        if reply == 'board':
            return response(200, self.board() if callable(self.board) else self.board)
        return reply


class OddsApiSession:
    """The Odds API: replies chosen by URL; counts every call."""

    def __init__(self, routes):
        self.routes, self.calls = routes, []

    def __call__(self, url, *, params, headers=None, timeout=None):
        self.calls.append(url)
        for fragment, reply in self.routes:
            if fragment in url:
                return reply(url) if callable(reply) else reply
        raise AssertionError(f'unexpected Odds API call {url}')


# --- one fixture, priced identically by every provider --------------------------------------------------------

SPEC = dict(kit_id='1611867830', odds_id='a' * 32, home='Arsenal', away='Chelsea',
            ml=(2.10, 3.50, 3.60),
            spreads={-0.5: (2.08, 1.84), -0.25: (1.85, 2.07), -0.75: (2.40, 1.62)}, main_spread=-0.25,
            totals={2.5: (1.95, 1.95), 1.5: (1.30, 3.60), 3.5: (3.10, 1.38), 2.75: (2.20, 1.70)}, main_total=2.5,
            corners={10.5: (1.90, 1.90), 9.5: (1.60, 2.30)})


def kit_board(kickoff, spec=SPEC, *, stale=False, last_change=None, league='England - Premier League'):
    period = {'number': 0, 'description': 'Game',
              'money_line': dict(zip(('home', 'draw', 'away'), spec['ml'])),
              'spreads': {f'{k:g}': {'hdp': k, 'home': h, 'away': a, 'max': 1000,
                                     'is_alternate': k != spec['main_spread']} for k, (h, a) in spec['spreads'].items()},
              'totals': {f'{k:g}': {'points': k, 'over': o, 'under': u, 'max': 1000,
                                    'is_alternate': k != spec['main_total']} for k, (o, u) in spec['totals'].items()},
              'team_totals': {'home': {'1.5': {'points': 1.5, 'over': 2.0, 'under': 1.8}},
                              'away': {'0.5': {'points': 0.5, 'over': 1.5, 'under': 2.6}}}}
    corners = {'number': 0, 'totals': {f'{k:g}': {'points': k, 'over': o, 'under': u}
                                       for k, (o, u) in spec['corners'].items()}}
    payload = {'sport_id': 1, 'sport_name': 'Soccer', 'last': 7, 'last_call': 7, 'events': [
        {'event_id': int(spec['kit_id']), 'league_id': 1980, 'league_name': league, 'starts': stamp(kickoff),
         'home': spec['home'], 'away': spec['away'], 'event_type': 'prematch', 'periods': {'num_0': period}},
        {'event_id': int(spec['kit_id']) + 1, 'parent_id': int(spec['kit_id']), 'league_id': 1980,
         'league_name': league + ' Corners', 'starts': stamp(kickoff), 'home': spec['home'] + ' (Corners)',
         'away': spec['away'] + ' (Corners)', 'event_type': 'prematch', 'periods': {'num_0': corners}},
        {'event_id': 99, 'league_id': 5, 'league_name': 'Elsewhere - Other League', 'starts': stamp(kickoff),
         'home': 'X', 'away': 'Y', 'event_type': 'prematch', 'periods': {}}]}
    if stale:
        payload.update(stale=True, last_change=int(last_change.timestamp()))
    return payload


def odds_api_events(kickoff, spec=SPEC):
    return [{'id': spec['odds_id'], 'sport_key': EPL.odds_api_sport_key, 'commence_time': stamp(kickoff),
             'home_team': spec['home'], 'away_team': spec['away']}]


def _side_outcomes(lines, home, away, kind):
    if kind == 'spreads':
        return ([{'name': home, 'price': h, 'point': k} for k, (h, a) in lines] +
                [{'name': away, 'price': a, 'point': -k + 0.0} for k, (h, a) in lines])
    return ([{'name': 'Over', 'price': o, 'point': k} for k, (o, u) in lines] +
            [{'name': 'Under', 'price': u, 'point': k} for k, (o, u) in lines])


def odds_api_odds(kickoff, quoted, spec=SPEC):
    """The /odds response: Pinnacle h2h and the main spread and total, plus another bookmaker the adapter drops."""
    h, d, a = spec['ml']
    sm, tm = spec['main_spread'], spec['main_total']
    markets = [{'key': 'h2h', 'last_update': stamp(quoted), 'outcomes': [
                   {'name': spec['home'], 'price': h}, {'name': spec['away'], 'price': a}, {'name': 'Draw', 'price': d}]},
               {'key': 'spreads', 'last_update': stamp(quoted),
                'outcomes': _side_outcomes([(sm, spec['spreads'][sm])], spec['home'], spec['away'], 'spreads')},
               {'key': 'totals', 'last_update': stamp(quoted),
                'outcomes': _side_outcomes([(tm, spec['totals'][tm])], spec['home'], spec['away'], 'totals')}]
    return [{'id': spec['odds_id'], 'sport_key': EPL.odds_api_sport_key, 'commence_time': stamp(kickoff),
             'home_team': spec['home'], 'away_team': spec['away'],
             'bookmakers': [{'key': 'pinnacle', 'title': 'Pinnacle', 'markets': markets}]}]


def odds_api_event(kickoff, quoted, spec=SPEC):
    """The per-event response: Pinnacle's alternate lines and corners (no double chance or draw no bet, which the
    kit API does not offer, so the two providers hold identical prices)."""
    alt_s = sorted((k, v) for k, v in spec['spreads'].items() if k != spec['main_spread'])
    alt_t = sorted((k, v) for k, v in spec['totals'].items() if k != spec['main_total'])
    markets = [{'key': 'alternate_spreads', 'last_update': stamp(quoted),
                'outcomes': _side_outcomes(alt_s, spec['home'], spec['away'], 'spreads')},
               {'key': 'alternate_totals', 'last_update': stamp(quoted),
                'outcomes': _side_outcomes(alt_t, spec['home'], spec['away'], 'totals')},
               {'key': 'alternate_totals_corners', 'last_update': stamp(quoted),
                'outcomes': _side_outcomes(sorted(spec['corners'].items()), spec['home'], spec['away'], 'totals')}]
    return {'id': spec['odds_id'], 'sport_key': EPL.odds_api_sport_key, 'commence_time': stamp(kickoff),
            'home_team': spec['home'], 'away_team': spec['away'],
            'bookmakers': [{'key': 'pinnacle', 'title': 'Pinnacle', 'markets': markets},
                           {'key': 'onexbet', 'title': '1xBet', 'markets': markets}]}


def config(**changes):
    data = op.load_config()
    data = json.loads(json.dumps(data))
    data['enabled'] = True
    for name, value in changes.items():
        if name in data['providers']:
            data['providers'][name].update(value)
        else:
            data[name] = value
    return data


class Base(OfflineQuotePolicyTestCase):
    def setUp(self):
        super().setUp()
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        env = patch.dict(os.environ, KEYS, clear=False)
        env.start()
        self.addCleanup(env.stop)
        self.now = datetime.now(timezone.utc).replace(microsecond=0)
        self.kickoff = self.now + timedelta(days=1)
        self.clock = Clock(self.now)

    def client(self, cfg=None, *, pinnapi=(), pinnodds=(), odds_api=None, board=None, seed=()):
        api = TheOddsAPI(KEYS['THE_ODDS_API_KEY'], cache_dir=self.tmp.name)
        self.assertIsNone(api.router)  # the committed config is off
        board = board or (lambda: kit_board(self.kickoff))
        self.pinnapi, self.pinnodds = KitSession(board, *pinnapi), KitSession(board, *pinnodds)
        api.router = op.OddsProviderRouter(cfg or config(), clock=self.clock, aliases={}, seed=seed,
                                           sessions={'pinnapi': self.pinnapi, 'pinnodds': self.pinnodds})
        self.odds_api = OddsApiSession(odds_api or [])
        api.http.session.get = self.odds_api
        return api


class SwitchOffTests(Base):
    def test_committed_config_is_off_and_valid(self):
        self.assertFalse(op.enabled())
        cfg = op.load_config()
        self.assertEqual(cfg['order'], ['pinnapi', 'pinnodds', 'the-odds-api'])
        self.assertEqual(cfg['providers']['pinnapi']['key_env'], 'PINNAPI_API_KEY')
        self.assertEqual(cfg['providers']['pinnodds']['key_env'], 'PINNODDS_API_KEY')

    def test_the_odds_api_must_be_last(self):
        path = Path(self.tmp.name) / 'bad.json'
        bad = config()
        bad['order'] = ['the-odds-api', 'pinnapi', 'pinnodds']
        path.write_text(json.dumps(bad), encoding='utf-8')
        with self.assertRaisesRegex(ValueError, 'last provider'):
            op.load_config(path)
        self.assertFalse(op.enabled(Path(self.tmp.name) / 'missing.json'))

    def test_switch_off_requests_go_to_the_odds_api_unchanged(self):
        api = TheOddsAPI(KEYS['THE_ODDS_API_KEY'], cache_dir=self.tmp.name)
        self.assertIsNone(api.router)
        self.assertEqual(api._provider_request('odds', EPL), {})
        self.assertEqual(op.event_request(api, EPL, {'odds_event_id': 'x'}, ['h2h']), {})
        session = OddsApiSession([('/events/', response(200, odds_api_event(self.kickoff, self.now))),
                                  ('/events', response(200, odds_api_events(self.kickoff))),
                                  ('/odds', response(200, odds_api_odds(self.kickoff, self.now)))])
        api.http.session.get = session
        fixtures = api.events(EPL, 3, self.now)
        odds = api.odds(EPL, 3, self.now)
        extra = api.extra_markets_for_event(EPL, SPEC['odds_id'])
        self.assertEqual(len(session.calls), 3)
        self.assertTrue(all('api.the-odds-api.com' in url for url in session.calls))
        for frame in (fixtures, odds):
            self.assertFalse(set(PROVENANCE) & set(frame.columns))
        self.assertNotIn('odds_extra_markets_provider', extra)
        self.assertEqual(odds.iloc[0]['odds_source'], 'The Odds API')

    def test_switch_off_adds_nothing_to_reports(self):
        import model_activity as ma
        self.assertEqual(op.weekly_lines([{'recorded_at_utc': stamp(self.now), 'credits_spent': 5}],
                                         op.iso_week(self.now)), [])
        self.assertEqual(ma.odds_switch_events([], source=ma.SOURCE_FORECAST), [])
        from football_value_pipeline_v2_standalone import run_outcome
        outcome = run_outcome(Path(self.tmp.name), 3, TheOddsAPI(KEYS['THE_ODDS_API_KEY'], cache_dir=self.tmp.name))
        self.assertNotIn('odds_provider', outcome)


class NormalisationTests(Base):
    def test_kit_board_normalised(self):
        events = op.normalise_kit_board(kit_board(self.kickoff), provider='pinnapi', fetched_at=self.now,
                                        leagues=config()['leagues'], aliases={'EPL': {'Arsenal': 'Arsenal FC'}})
        self.assertEqual(len(events), 1)  # the corner child is attached, the unmapped league skipped
        e = events[0]
        self.assertEqual((e['provider'], e['provider_event_id'], e['league_key']), ('pinnapi', SPEC['kit_id'], 'EPL'))
        self.assertEqual((e['home_team'], e['away_team'], e['team_names']), ('Arsenal FC', 'Chelsea', 'alias'))
        self.assertEqual((e['kickoff_utc'], e['fetched_at_utc']), (stamp(self.kickoff), stamp(self.now)))
        self.assertEqual(e['one_x_two'], {'home': 2.1, 'draw': 3.5, 'away': 3.6, 'updated_at_utc': stamp(self.now)})
        self.assertEqual([(x['line'], x['home'], x['away'], x['main']) for x in e['asian_handicap']],
                         [(-0.75, 2.4, 1.62, False), (-0.5, 2.08, 1.84, False), (-0.25, 1.85, 2.07, True)])
        self.assertIn((2.5, 1.95, 1.95, True), [(x['line'], x['over'], x['under'], x['main']) for x in e['goal_lines']])
        self.assertEqual([x['line'] for x in e['team_totals']['home']], [1.5])
        self.assertEqual([(x['line'], x['over']) for x in e['corners']], [(9.5, 1.6), (10.5, 1.9)])
        self.assertIsNone(e['double_chance'])

    def test_main_line_without_flag_is_the_most_balanced_pair(self):
        board = kit_board(self.kickoff)
        for item in board['events'][0]['periods']['num_0']['spreads'].values():
            item.pop('is_alternate')
        e = op.normalise_kit_board(board, provider='pinnapi', fetched_at=self.now, leagues=config()['leagues'],
                                   aliases={})[0]
        self.assertEqual([x['line'] for x in e['asian_handicap'] if x['main']], [-0.25])

    def test_stale_board_quotes_date_from_last_change(self):
        changed = self.now - timedelta(hours=3)
        e = op.normalise_kit_board(kit_board(self.kickoff, stale=True, last_change=changed), provider='pinnapi',
                                   fetched_at=self.now, leagues=config()['leagues'], aliases={})[0]
        self.assertTrue(e['stale'])
        self.assertEqual(e['one_x_two']['updated_at_utc'], stamp(changed))
        self.assertEqual(e['fetched_at_utc'], stamp(self.now))

    def test_round_trip_through_the_odds_api_shape(self):
        e = op.normalise_kit_board(kit_board(self.kickoff), provider='pinnapi', fetched_at=self.now,
                                   leagues=config()['leagues'], aliases={})[0]
        markets = ('h2h', 'spreads', 'alternate_spreads', 'totals', 'alternate_totals', 'team_totals',
                   'alternate_team_totals', 'alternate_totals_corners')
        back = op.normalise_odds_api_event(op.to_odds_api_event(e, markets), league_key='EPL', fetched_at=self.now,
                                           aliases={}, provider='pinnapi')
        self.assertEqual({k: v for k, v in back.items() if k != 'stale'}, {k: v for k, v in e.items() if k != 'stale'})

    def test_odds_api_event_keeps_pinnacle_only(self):
        e = op.normalise_odds_api_event(odds_api_event(self.kickoff, self.now), league_key='EPL',
                                        fetched_at=self.now, aliases={})
        self.assertEqual(e['provider'], 'the-odds-api')
        payload = op.to_odds_api_event(e, ['alternate_spreads', 'alternate_totals', 'alternate_totals_corners'])
        self.assertEqual([b['key'] for b in payload['bookmakers']], ['pinnacle'])


class AnyProviderTests(Base):
    """Identical prices give byte-identical forecast quotes and lists, whichever provider answers."""

    def priced_rows(self, serving):
        fail = response(500, {'error': 'internal'})
        replies = {'pinnapi': dict(pinnapi=['board'] + [fail] * 5),
                   'pinnodds': dict(pinnapi=['board'] + [fail] * 5),
                   'the-odds-api': dict(pinnapi=['board'] + [fail] * 5, pinnodds=[fail] * 5)}[serving]
        if serving == 'pinnapi':
            replies = dict(pinnapi=['board'] * 6)
        api = self.client(config(board_ttl_seconds=0), odds_api=[
            ('/events/', response(200, odds_api_event(self.kickoff, self.now))),
            ('/odds', response(200, odds_api_odds(self.kickoff, self.now)))], **replies)
        fixtures = api.events(EPL, 3, self.now)  # the schedule always comes from pinnapi here
        odds = api.odds(EPL, 3, self.now)
        extra = api.extra_markets_for_event(EPL, fixtures.iloc[0]['fixture_id'])
        self.assertEqual(odds.iloc[0].get('odds_provider'), serving)
        self.assertEqual(extra.get('odds_extra_markets_provider'), serving)
        if serving != 'the-odds-api':
            self.assertEqual(self.odds_api.calls, [])  # The Odds API is called only after both kit providers fail
        row = {**odds.drop(columns=[c for c in PROVENANCE if c in odds]).iloc[0].to_dict(),
               **{k: v for k, v in extra.items() if k not in PROVENANCE}}
        return fixtures.drop(columns=[c for c in PROVENANCE if c in fixtures]), row

    def test_quotes_byte_identical_through_every_provider(self):
        results = {name: self.priced_rows(name) for name in ('pinnapi', 'pinnodds', 'the-odds-api')}
        frames = {name: pd.DataFrame([row]).to_csv(index=False) for name, (_, row) in results.items()}
        self.assertEqual(frames['pinnapi'], frames['pinnodds'])
        self.assertEqual(frames['pinnapi'], frames['the-odds-api'])
        row = results['pinnapi'][1]
        self.assertEqual(row['fixture_id'], SPEC['kit_id'])  # the schedule's id, whoever priced it
        self.assertEqual(row['live_ref_home_odds'], 2.10)
        self.assertEqual(row['live_ref_over_2_5_odds'], 1.95)
        self.assertGreater(len(json.loads(row['asian_handicap_offers'])), 2)
        self.assertIn('count_market_offers', row)

    def test_lists_byte_identical_with_provenance_columns(self):
        from test_asian_handicap import choose, quote, row
        base = row(offers=[{**quote(price=2.1), 'opposite_price': 1.8}])
        lists = []
        for provider in (None, 'pinnapi', 'pinnodds', 'the-odds-api'):
            value = dict(base, **({k: provider for k in PROVENANCE} if provider else {}))
            picks, decisions, summary = choose([value])
            lists.append((picks.to_csv(index=False), decisions.to_csv(index=False)))
        self.assertTrue(lists[0][0].count('\n') > 1)  # a real pick, not an empty list
        self.assertEqual(len(set(lists)), 1)


class FailoverTests(Base):
    def odds(self, api):
        return api.odds(EPL, 3, self.now)

    def test_error_moves_to_pinnodds_and_never_calls_the_odds_api(self):
        api = self.client(pinnapi=[response(503, {'error': 'prematch_disabled'})])
        self.assertEqual(self.odds(api).iloc[0]['odds_provider'], 'pinnodds')
        self.assertEqual(self.odds_api.calls, [])
        switch = api.router.switches[-1]
        self.assertEqual((switch['from'], switch['to'], switch['reasons']), ('pinnapi', 'pinnodds', {'pinnapi': 'error'}))
        self.assertEqual(self.pinnapi.calls[0]['headers']['x-portal-apikey'], KEYS['PINNAPI_API_KEY'])

    def test_timeout_moves_to_pinnodds(self):
        api = self.client(pinnapi=[requests.Timeout('slow')])
        self.assertEqual(self.odds(api).iloc[0]['odds_provider'], 'pinnodds')
        self.assertEqual(api.router.summary()['providers']['pinnapi']['failures'], {'timeout': 1})

    def test_429_honours_retry_after_then_returns_to_pinnapi(self):
        limited = response(429, {'error': 'rate_limited', 'window': 'minute', 'limit': 20, 'retry_after_ms': 41052},
                           {'Retry-After': 41})
        api = self.client(config(board_ttl_seconds=0), pinnapi=[limited])
        self.assertEqual(self.odds(api).iloc[0]['odds_provider'], 'pinnodds')
        self.assertEqual(api.router.state['pinnapi'].blocked_until, self.now + timedelta(seconds=41))
        self.clock.advance(seconds=30)
        self.assertEqual(self.odds(api).iloc[0]['odds_provider'], 'pinnodds')
        self.assertEqual(len(self.pinnapi.calls), 1)  # no request while Retry-After runs
        self.assertEqual(api.router.summary()['providers']['pinnapi']['failures'],
                         {'rate_limited': 1, 'retry_after': 1})
        self.clock.advance(seconds=12)
        self.assertEqual(self.odds(api).iloc[0]['odds_provider'], 'pinnapi')
        self.assertEqual([(s['from'], s['to']) for s in api.router.switches],
                         [('pinnapi', 'pinnodds'), ('pinnodds', 'pinnapi')])

    def test_daily_cap_counted_locally_and_from_a_429_day_window(self):
        api = self.client(config(board_ttl_seconds=0, pinnapi={'daily_allowance': 2}))
        self.assertEqual([self.odds(api).iloc[0]['odds_provider'] for _ in range(3)], ['pinnapi', 'pinnapi', 'pinnodds'])
        self.assertEqual(len(self.pinnapi.calls), 2)
        self.assertEqual(api.router.switches[-1]['reasons'], {'pinnapi': 'daily_allowance'})
        day = response(429, {'error': 'rate_limited', 'window': 'day', 'limit': 100, 'retry_after_ms': 1000},
                       {'Retry-After': 1})
        api = self.client(config(board_ttl_seconds=0), pinnapi=[day])
        self.assertEqual(self.odds(api).iloc[0]['odds_provider'], 'pinnodds')
        midnight = datetime.combine((self.now + timedelta(days=1)).date(), datetime.min.time(), timezone.utc)
        self.assertEqual(api.router.state['pinnapi'].blocked_until, midnight)
        self.assertEqual(api.router.switches[-1]['reasons'], {'pinnapi': 'daily_allowance'})

    def test_mid_run_switch_keeps_the_schedule_identity(self):
        fail = response(500, {})
        api = self.client(config(board_ttl_seconds=0), pinnapi=['board', fail, fail],
                          pinnodds=[fail, fail], odds_api=[
                              ('/events/', response(200, odds_api_event(self.kickoff, self.now))),
                              ('/odds', response(200, odds_api_odds(self.kickoff, self.now)))])
        fixtures = api.events(EPL, 3, self.now)
        self.assertEqual(fixtures.iloc[0]['odds_schedule_provider'], 'pinnapi')
        odds = self.odds(api)  # pinnapi and pinnodds fail mid-run: The Odds API prices the same fixture
        self.assertEqual(odds.iloc[0]['odds_provider'], 'the-odds-api')
        self.assertEqual(odds.iloc[0]['fixture_id'], fixtures.iloc[0]['fixture_id'])
        extra = api.extra_markets_for_event(EPL, fixtures.iloc[0]['fixture_id'])  # a kit id, priced by The Odds API
        self.assertTrue(json.loads(extra['asian_handicap_offers']))
        self.assertEqual([(s['from'], s['to']) for s in api.router.switches], [('pinnapi', 'the-odds-api')])
        self.assertEqual(api.router.switches[0]['reasons'], {'pinnapi': 'error', 'pinnodds': 'error'})

    def test_reset_at_utc_midnight_returns_to_pinnapi(self):
        self.clock.when = self.now.replace(hour=23, minute=59, second=0)
        self.kickoff = self.clock.when + timedelta(days=1)
        api = self.client(config(board_ttl_seconds=0, pinnapi={'daily_allowance': 1}))
        self.assertEqual(self.odds(api).iloc[0]['odds_provider'], 'pinnapi')
        self.assertEqual(self.odds(api).iloc[0]['odds_provider'], 'pinnodds')
        self.clock.advance(minutes=2)  # the next UTC day
        self.assertEqual(self.odds(api).iloc[0]['odds_provider'], 'pinnapi')
        self.assertEqual([(s['from'], s['to']) for s in api.router.switches],
                         [('pinnapi', 'pinnodds'), ('pinnodds', 'pinnapi')])
        days = api.router.summary()['providers']['pinnapi']['requests_by_utc_day']
        self.assertEqual(sorted(days.values()), [1, 1])

    def test_all_three_exhausted(self):
        from odds_provider_health import OddsProviderError
        day = response(429, {'error': 'rate_limited', 'window': 'day'}, {'Retry-After': 5})
        api = self.client(config(pinnodds={'daily_allowance': 1}), pinnapi=[day],
                          seed=[{'odds_provider': {'providers': {'pinnodds': {
                              'requests_by_utc_day': {self.now.date().isoformat(): 1}}}}}],
                          odds_api=[('/odds', response(401, EXHAUSTED))])
        with patch.dict(os.environ, {'THE_ODDS_API_KEY_FALLBACK_1': '', 'THE_ODDS_API_KEY_FALLBACK_2': ''}), \
                self.assertWarns(RuntimeWarning), self.assertRaises(OddsProviderError) as caught:
            self.odds(api)
        self.assertEqual(caught.exception.category, 'CREDITS_EXHAUSTED')
        self.assertTrue(api.usage.exhausted)
        self.assertEqual(self.pinnodds.calls, [])  # its allowance was spent by an earlier run today
        last = api.router.switches[-1]
        self.assertEqual((last['to'], last['reasons']),
                         (None, {'pinnapi': 'daily_allowance', 'pinnodds': 'daily_allowance', 'the-odds-api': 'error'}))

    def test_not_configured_key_is_skipped_without_a_request(self):
        with patch.dict(os.environ, {'PINNAPI_API_KEY': ''}):
            api = self.client()
            self.assertEqual(self.odds(api).iloc[0]['odds_provider'], 'pinnodds')
        self.assertEqual(self.pinnapi.calls, [])

    def test_seeded_block_from_the_usage_log(self):
        until = self.now + timedelta(minutes=5)
        api = self.client(seed=[{'odds_provider': {'providers': {'pinnapi': {'blocked_until_utc': stamp(until)}}}}])
        self.assertEqual(self.odds(api).iloc[0]['odds_provider'], 'pinnodds')
        self.assertEqual(self.pinnapi.calls, [])


class ClosingTests(Base):
    def source(self):
        return {'league': EPL.name, 'home_team': SPEC['home'], 'away_team': SPEC['away'],
                'kickoff_utc': stamp(self.kickoff), 'odds_event_id': SPEC['odds_id']}

    def test_closing_request_for_an_odds_api_event_is_priced_by_pinnapi(self):
        import closing_odds
        self.kickoff = self.now + timedelta(minutes=4)  # inside the pre-kickoff window
        api = self.client()
        payload = closing_odds.fetch(api, self.source(), {'h2h', 'totals'})
        self.assertEqual((payload['id'], payload['odds_provider']), (SPEC['odds_id'], 'pinnapi'))
        observation = closing_odds.normalize(self.source(), payload, self.now + timedelta(seconds=1))
        self.assertIn(('pinnacle', 'home'), {(q['bookmaker'], q['selection']) for q in observation['quotes']})
        self.assertEqual(observation['payload']['odds_provider'], 'pinnapi')  # provenance kept with the evidence
        self.assertEqual(self.odds_api.calls, [])
        self.assertFalse(closing_odds.low_credits(Path(self.tmp.name), api))

    def test_odds_api_fallback_finds_its_own_id_for_a_kit_event(self):
        import closing_odds
        self.kickoff = self.now + timedelta(minutes=4)
        fail = response(500, {})
        api = self.client(pinnapi=[fail], pinnodds=[fail], odds_api=[
            ('/events/', response(200, odds_api_event(self.kickoff, self.now))),
            ('/events', response(200, odds_api_events(self.kickoff)))])
        source = {**self.source(), 'odds_event_id': SPEC['kit_id']}
        payload = closing_odds.fetch(api, source, {'alternate_spreads'})
        self.assertEqual((payload['id'], payload['odds_provider']), (SPEC['kit_id'], 'the-odds-api'))
        self.assertTrue(any(SPEC['odds_id'] in url for url in self.odds_api.calls))

    def test_closing_usage_record_keeps_kit_counts(self):
        import closing_odds
        import odds_api_usage
        self.kickoff = self.now + timedelta(minutes=4)
        api = self.client()
        closing_odds.fetch(api, self.source(), {'h2h'})
        root = Path(self.tmp.name) / 'football_output_v2'
        record = closing_odds.record_usage(root, api)
        self.assertEqual(record['odds_provider']['providers']['pinnapi']['requests'], 1)
        logged = odds_api_usage.read_log(root.parent)
        router = op.OddsProviderRouter(config(), clock=self.clock, aliases={}, seed=logged)
        self.assertEqual(router.state['pinnapi'].requests_today, 1)  # the next session starts from it
        text = json.dumps(logged)
        for secret in KEYS.values():
            self.assertNotIn(secret, text)


class ReportTests(Base):
    def switched_router(self):
        api = self.client(pinnapi=[response(500, {})])
        api.odds(EPL, 3, self.now)
        return api.router

    def test_summary_markdown_and_activity_log(self):
        import model_activity as ma
        router = self.switched_router()
        summary = router.summary()
        text = op.summary_markdown(summary)
        self.assertIn('pinnapi → pinnodds', text)
        self.assertIn('Switches this run: 1.', text)
        events = ma.odds_switch_events(summary['switches'], source=ma.SOURCE_FORECAST)
        self.assertEqual([(e['event'], e['outcome']) for e in events], [(ma.ODDS_SWITCH, 'pinnapi -> pinnodds')])
        log = Path(self.tmp.name) / 'activity.jsonl'
        self.assertEqual(len(ma.append(log, events)), 1)
        self.assertEqual(ma.append(log, ma.odds_switch_events(summary['switches'], source=ma.SOURCE_FORECAST)), [])
        out = Path(self.tmp.name) / 'run'
        out.mkdir()
        (out / 'conservative_bet_summary.json').write_text(json.dumps({'odds_provider': summary}), encoding='utf-8')
        found = ma.forecast_events([], out, Path('master_shortlist_config.json'), Path('research_config.json'),
                                   self.now, Path('cagey_correction_config.json'))
        self.assertIn(events[0]['id'], [e['id'] for e in found])

    def test_closing_switches_reach_the_activity_log_from_the_usage_log(self):
        import model_activity as ma
        import odds_api_usage
        summary = self.switched_router().summary()
        repo = Path(self.tmp.name)
        odds_api_usage.append_log({'workflow': 'closing-odds', 'odds_provider': summary}, repo)
        odds_api_usage.append_log({'workflow': 'closing-odds'}, repo)
        events = ma.closing_switch_events(repo)
        self.assertEqual([(e['source'], e['outcome']) for e in events], [(ma.SOURCE_CLOSING, 'pinnapi -> pinnodds')])

    def test_weekly_lines_count_requests_switches_and_credits(self):
        summary = self.switched_router().summary()
        week = op.iso_week(self.now)
        records = [{'recorded_at_utc': stamp(self.now), 'workflow': 'scheduled-forecasts', 'credits_spent': 0,
                    'odds_provider': summary},
                   {'recorded_at_utc': stamp(self.now), 'workflow': 'closing-odds', 'credits_spent': 7},
                   {'recorded_at_utc': stamp(self.now - timedelta(days=14)), 'credits_spent': 100,
                    'odds_provider': summary}]
        text = '\n'.join(op.weekly_lines(records, week))
        self.assertIn('| pinnapi | 1 | 0 | 1 | 0 |', text)
        self.assertIn('| pinnodds | 1 | 1 | 0 | 1 |', text)
        self.assertIn('Switches this week: 1. Odds API credits spent this week (every workflow): 7.', text)

    def test_run_outcome_records_the_provider_summary(self):
        from football_value_pipeline_v2_standalone import run_outcome
        api = self.client(pinnapi=[response(500, {})])
        api.odds(EPL, 3, self.now)
        outcome = run_outcome(Path(self.tmp.name), 3, api)
        self.assertEqual(outcome['odds_provider']['switches'][0]['to'], 'pinnodds')
        import publish_scheduled_forecasts as publisher
        record = publisher.usage_record(outcome, 0)
        self.assertEqual(record['odds_provider'], outcome['odds_provider'])


class ComparisonTests(Base):
    def test_differences_and_tolerance(self):
        leagues = config()['leagues']
        kit = op.normalise_kit_board(kit_board(self.kickoff), provider='pinnapi', fetched_at=self.now,
                                     leagues=leagues, aliases={})
        moved = json.loads(json.dumps(SPEC))
        moved['spreads'] = {float(k): v for k, v in SPEC['spreads'].items()}
        moved['totals'] = {float(k): v for k, v in SPEC['totals'].items()}
        moved['corners'] = {float(k): v for k, v in SPEC['corners'].items()}
        moved['ml'] = (2.12, 3.50, 3.78)  # home +0.95%, away +5%
        other = op.normalise_kit_board(kit_board(self.kickoff, moved), provider='pinnodds', fetched_at=self.now,
                                       leagues=leagues, aliases={})
        late = op.normalise_kit_board(kit_board(self.kickoff + timedelta(hours=3)), provider='pinnodds',
                                      fetched_at=self.now, leagues=leagues, aliases={})
        same = op.compare_providers({'pinnapi': kit, 'pinnodds': kit}, 0.02)
        self.assertEqual((same['fixtures_quoted_by_all'], same['differences']), (1, []))
        result = op.compare_providers({'pinnapi': kit, 'pinnodds': other + late}, 0.02)
        self.assertEqual([(r['price'], r['within_tolerance']) for r in result['differences']],
                         [('1X2 away', False), ('1X2 home', True)])
        self.assertEqual(len(result['outside_tolerance']), 1)
        self.assertEqual(len(result['not_quoted_by_all']['pinnodds']), 1)
        self.assertIn('| NO |', op.comparison_markdown(result))

    def test_check_script_reports_leagues_and_team_names(self):
        import importlib.util
        spec = importlib.util.spec_from_file_location('odds_provider_compare',
                                                      Path(__file__).resolve().parents[1] / 'scripts' /
                                                      'odds_provider_compare.py')
        script = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(script)
        leagues = config()['leagues']
        board = kit_board(self.kickoff)
        board['events'].append({**board['events'][0], 'event_id': 99, 'league_name': 'Spain - LaLiga'})
        report = script.league_report(board, leagues)
        self.assertEqual(report['competitions']['EPL']['events'], 1)
        self.assertEqual(report['competitions']['LaLiga']['events'], 0)
        self.assertIn('Spain - LaLiga', [x['league_name'] for x in report['candidates']])
        events = op.normalise_kit_board(board, provider='pinnapi', fetched_at=self.now, leagues=leagues, aliases={})
        kick = stamp(self.kickoff)
        same = {'EPL': [{'home_team': 'Arsenal', 'away_team': 'Chelsea', 'kickoff_utc': kick}]}
        self.assertEqual(script.match_report(events, same, self.now)['matched'], 1)
        other = {'EPL': [{'home_team': 'Arsenal FC', 'away_team': 'Chelsea Blues', 'kickoff_utc': kick},
                         {'home_team': 'Spurs', 'away_team': 'Leeds', 'kickoff_utc': stamp(self.kickoff
                                                                                          - timedelta(hours=1))}]}
        result = script.match_report(events, other, self.now)
        self.assertEqual((result['matched'], len(result['mismatched'])), (0, 1))
        self.assertIn('Chelsea Blues', result['mismatched'][0]['schedule_at_same_kickoff'][0])
        self.assertEqual([x['schedule'] for x in result['schedule_not_on_board']],
                         ['Arsenal FC v Chelsea Blues', 'Spurs v Leeds'])
        text = script.markdown({'run_at_utc': kick, 'tolerance': 0.02, 'requests': {'pinnapi': [
            {'status': 200, 'seconds': 0.1, 'bytes': 10, 'headers': {'x-ratelimit-remaining': '99'}}]},
            'allowances': {'pinnapi': 100}, 'odds_api_usage': None, 'errors': {},
            'leagues': {'pinnapi': report}, 'team_names': {'pinnapi': result}, 'prices': {}, 'board_shape': {}})
        self.assertIn('x-ratelimit-remaining', text)
        self.assertIn('Spain - LaLiga', text)
