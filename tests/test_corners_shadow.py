"""Shadow corner list: request scope, live-output invariance, picks, closing collection and grading."""
import copy
import csv
import json
from datetime import timedelta
from pathlib import Path
from unittest.mock import patch

import pytest

import corners_shadow as cs
from offline_test_case import OfflineQuotePolicyTestCase
from test_conservative_bet_filter import NOW

KICK = NOW + timedelta(days=1)


def _pair(point, over, under, key='Over', other='Under'):
    return [{'name': key, 'price': over, 'point': point}, {'name': other, 'price': under, 'point': point}]


def corner_market(stamp=NOW, pairs=((8.5, 1.55, 2.45), (9.5, 1.90, 1.92), (10.5, 2.35, 1.60), (11.5, 3.10, 1.36))):
    return {'key': cs.MARKET_KEY, 'last_update': stamp.isoformat(),
            'outcomes': [o for p, a, b in pairs for o in _pair(p, a, b)]}


def payload(event_id='event0', corners=True):
    """A Pinnacle and bet365 event with every market the per-event request reads, plus corners if asked."""
    stamp = NOW.isoformat()
    def book(key, title):
        markets = [
            {'key': 'alternate_totals', 'last_update': stamp,
             'outcomes': _pair(1.5, 1.30, 3.60) + _pair(2.5, 1.95, 1.90) + _pair(3.5, 3.20, 1.36)},
            {'key': 'alternate_spreads', 'last_update': stamp,
             'outcomes': [{'name': 'Chelsea', 'price': 1.93, 'point': -0.5}, {'name': 'Fulham', 'price': 1.97, 'point': 0.5},
                          {'name': 'Chelsea', 'price': 2.40, 'point': -1.0}, {'name': 'Fulham', 'price': 1.60, 'point': 1.0}]},
            {'key': 'draw_no_bet', 'last_update': stamp,
             'outcomes': [{'name': 'Chelsea', 'price': 1.40}, {'name': 'Fulham', 'price': 3.00}]},
            {'key': 'double_chance', 'last_update': stamp,
             'outcomes': [{'name': 'Chelsea or Draw', 'price': 1.25}, {'name': 'Fulham or Draw', 'price': 2.10},
                          {'name': 'Chelsea or Fulham', 'price': 1.30}]}]
        if corners and key == 'pinnacle':
            markets.append(corner_market())
        return {'key': key, 'title': title, 'markets': markets}
    return {'id': event_id, 'commence_time': KICK.isoformat().replace('+00:00', 'Z'), 'home_team': 'Chelsea',
            'away_team': 'Fulham', 'bookmakers': [book('pinnacle', 'Pinnacle'), book('bet365', 'Bet365')]}


class RequestTests(OfflineQuotePolicyTestCase):
    def extra(self, league, response):
        from football_value_pipeline_v2_standalone import TheOddsAPI, LEAGUES
        api = TheOddsAPI.__new__(TheOddsAPI)
        api.regions = 'eu'; api.api_key = 'fake'; api.force_refresh = False
        with patch.object(api, '_get_json', return_value=response) as request, patch(
                'football_value_pipeline_v2_standalone.datetime') as clock:
            clock.now.return_value = NOW
            result = api.extra_markets_for_event(LEAGUES[league], 'event0')
        return request, result

    def test_domestic_leagues_request_corners_and_european_competitions_do_not(self):
        import league_registry
        for key, league in league_registry.LEAGUES.items():
            request, _ = self.extra(key, payload(corners=False))
            markets = request.call_args.kwargs['params']['markets'].split(',')
            self.assertEqual(cs.MARKET_KEY in markets, league.domestic, key)
            self.assertEqual('corners_' in request.call_args.args[1], league.domestic, key)
        self.assertFalse(cs.requests_corners('UCL'))
        self.assertFalse(cs.requests_corners('UEL'))

    def test_corner_markets_leave_every_live_field_unchanged(self):
        _, without = self.extra('EPL', payload(corners=False))
        _, with_corners = self.extra('EPL', payload(corners=True))
        offers = json.loads(with_corners.pop('count_market_offers'))
        identity = with_corners.pop('_count_market_identity')
        self.assertEqual(with_corners, without)
        self.assertEqual(identity['home_team'], 'Chelsea')
        self.assertEqual({(o['line'], o['side']) for o in offers},
                         {(l, s) for l in (8.5, 9.5, 10.5, 11.5) for s in ('Over', 'Under')})
        self.assertTrue(all(o['bookmaker'] == 'Pinnacle' for o in offers))

    def test_european_payload_with_corners_is_not_parsed(self):
        _, result = self.extra('UCL', payload(corners=True))
        self.assertNotIn('count_market_offers', result)


def prediction(**changes):
    offers = cs.corner_offers(payload(), NOW)
    row = {'league': 'Premier League', 'home_team': 'Chelsea', 'away_team': 'Fulham',
           'kickoff_utc': KICK.isoformat(), 'odds_event_id': 'event0', 'model_home_team': 'Chelsea',
           'model_away_team': 'Fulham', 'count_market_offers': json.dumps(offers),
           'count_model': json.dumps({'corners': {'mu': 10.4, 'alpha': 0.02, 'version': 'count-markets-nb2-v1'}})}
    row.update(changes)
    return row


def test_pick_is_the_best_expected_return_inside_the_odds_window():
    import count_markets
    chosen = cs.pick(prediction())
    p = count_markets.probabilities(10.4, 0.02, 'corners')
    offers = [o for o in cs.corner_offers(payload(), NOW) if cs.ODDS_ABOVE < o['price'] <= cs.ODDS_MAX]
    best = max(offers, key=lambda o: p[count_markets.market_label('corners', o['side'], o['line'])] * o['price'])
    assert chosen['market'] == count_markets.market_label('corners', best['side'], best['line'])
    assert chosen['expected_return'] == pytest.approx(p[chosen['market']] * chosen['offered_decimal_odds'] - 1, abs=1e-6)
    assert cs.ODDS_ABOVE < chosen['offered_decimal_odds'] <= cs.ODDS_MAX


def test_odds_window_excludes_115_and_includes_220():
    def only(price, opposite):
        offer = {'kind': 'corners', 'side': 'Over', 'line': 9.5, 'price': price, 'opposite_price': opposite,
                 'bookmaker': 'Pinnacle', 'last_update_utc': NOW.isoformat(), 'market_key': cs.MARKET_KEY}
        return cs.pick(prediction(count_market_offers=json.dumps([offer])))
    assert only(1.15, 6.0) is None
    assert only(2.21, 1.70) is None
    assert only(2.20, 1.70)['offered_decimal_odds'] == 2.20


def test_no_pick_without_forecast_or_pinnacle_prices():
    assert cs.pick(prediction(count_model=None)) is None
    assert cs.pick(prediction(count_market_offers='[]')) is None
    other = [dict(o, bookmaker='bet365') for o in cs.corner_offers(payload(), NOW)]
    assert cs.pick(prediction(count_market_offers=json.dumps(other))) is None


def test_list_rows_are_labelled_unvalidated_with_zero_stake_and_bind_to_the_generation(tmp_path):
    generated = NOW.isoformat()
    rows = cs.write_list([prediction(), prediction(count_model=None, home_team='Arsenal')], tmp_path, generated)
    assert len(rows) == 1
    written = list(csv.DictReader((tmp_path / cs.FILE).open(encoding='utf-8')))
    assert written[0]['status'] == 'unvalidated, not bet' and written[0]['stake'] == '0'
    assert tuple(written[0]) == cs.COLUMNS
    assert cs.capture_file(tmp_path, generated) == tmp_path / cs.FILE
    assert cs.capture_file(tmp_path, (NOW + timedelta(seconds=1)).isoformat()) is None
    cs.write_list([], tmp_path, generated)
    assert (tmp_path / cs.FILE).read_text(encoding='utf-8').strip() == ','.join(cs.COLUMNS)


def _closing_payload(stamp):
    data = payload(corners=True)
    data['bookmakers'] = [{'key': 'pinnacle', 'title': 'Pinnacle', 'markets': [corner_market(stamp)]}]
    return data


def _current(tmp_path, row):
    raw = tmp_path / 'raw'
    raw.mkdir(parents=True, exist_ok=True)
    with (raw / cs.FILE).open('w', encoding='utf-8', newline='') as handle:
        writer = csv.DictWriter(handle, fieldnames=cs.COLUMNS, lineterminator='\n')
        writer.writeheader()
        writer.writerow(row)


def test_closing_collection_stays_in_its_window_folder_and_caps(tmp_path):
    row = cs.build([prediction()], NOW.isoformat())[0]
    _current(tmp_path, row)
    calls = []

    def fetcher(api, source):
        calls.append(source['odds_event_id'])
        return _closing_payload(clock - timedelta(seconds=30))
    early = KICK - timedelta(minutes=30)
    clock = early
    assert cs.collect_closing(tmp_path, None, clock=early, fetcher=fetcher, low_credits=False)['eligible'] == 0
    clock = KICK - timedelta(minutes=3)
    status = cs.collect_closing(tmp_path, None, clock=clock, fetcher=fetcher, low_credits=False)
    assert status['requests'] == 1 and status['written'] == 1 and calls == ['event0']
    # Already quoted: no second request.
    assert cs.collect_closing(tmp_path, None, clock=clock, fetcher=fetcher, low_credits=False)['requests'] == 0
    observations, rejected = cs.load_observations(tmp_path, clock)
    assert len(observations) == 1 and not rejected
    close = cs.closing_quote(row, observations)
    assert close['line'] == row['line'] and close['side'] == row['side']
    assert not (tmp_path / 'closing_odds').exists()  # the live collector's folder is never touched
    assert cs.collect_closing(tmp_path, None, clock=clock, fetcher=fetcher, low_credits=True)['reason'] == 'LOW_CREDITS_SKIPPED'


def test_closing_retries_once_then_stops_and_respects_the_daily_cap(tmp_path):
    row = cs.build([prediction()], NOW.isoformat())[0]
    _current(tmp_path, row)
    clock = KICK - timedelta(minutes=3)
    stale = lambda api, source: _closing_payload(clock - timedelta(minutes=10))  # noqa: E731 too old: no quotes
    for _ in range(4):
        cs.collect_closing(tmp_path, None, clock=clock, fetcher=stale, low_credits=False)
    budget = json.loads((tmp_path / cs.CLOSING_BUDGET).read_text(encoding='utf-8'))
    assert budget['requests'] == cs.CLOSING_MAX_REQUESTS_PER_FIXTURE
    (tmp_path / cs.CLOSING_BUDGET).write_text(json.dumps({'date': clock.date().isoformat(), 'requests': cs.CLOSING_DAILY_CAP}))
    for path in (tmp_path / cs.CLOSING_DIR).glob('*.json'):
        path.unlink()
    status = cs.collect_closing(tmp_path, None, clock=clock, fetcher=stale, low_credits=False)
    assert status['requests'] == 0 and status['reason'] == 'DAILY_REQUEST_CAP_REACHED'


def test_tampered_closing_observation_is_rejected(tmp_path):
    row = cs.build([prediction()], NOW.isoformat())[0]
    _current(tmp_path, row)
    clock = KICK - timedelta(minutes=3)
    cs.collect_closing(tmp_path, None, clock=clock, fetcher=lambda a, s: _closing_payload(clock), low_credits=False)
    path = next((tmp_path / cs.CLOSING_DIR).glob('*.json'))
    data = json.loads(path.read_text(encoding='utf-8'))
    data['quotes'][0]['decimal_odds'] = 9.9
    path.write_text(json.dumps(data), encoding='utf-8')
    assert cs.load_observations(tmp_path, clock) == ([], [path.name])


def test_grade_and_clv(monkeypatch):
    import count_markets
    row = {**cs.build([prediction()], NOW.isoformat())[0], 'snapshot_generated_utc': NOW.isoformat()}
    line = float(row['line'])
    won_total = int(line + 1) if row['side'] == 'Over' else int(line - 0.5)
    monkeypatch.setattr(count_markets, 'verified_total', lambda r, final, cache_dir=None: won_total)
    close = {'decimal_odds': 1.80, 'fair_probability': 0.55}
    graded = cs.grade(row, {'home_goals': 1, 'away_goals': 0}, close)
    assert graded['result_status'] == 'WON'
    assert graded['unit_return'] == pytest.approx(float(row['offered_decimal_odds']) - 1)
    assert graded['clv_vs_pinnacle_fair'] == pytest.approx(float(row['offered_decimal_odds']) * 0.55 - 1, abs=1e-6)
    assert cs.grade(row, None, None)['result_status'] == 'PENDING'
    monkeypatch.setattr(count_markets, 'verified_total', lambda r, final, cache_dir=None: None)
    assert cs.grade(row, {'home_goals': 1, 'away_goals': 0}, None)['result_status'] == 'AWAITING_COUNT_RESULT'
    summary = cs.summary_block([graded, cs.grade(row, None, None)])
    assert summary['graded'] == 1 and summary['pending'] == 1 and summary['win_rate'] == 1.0


def test_review_writes_grades_summary_and_report(tmp_path, monkeypatch):
    import count_markets
    row = {**cs.build([prediction()], NOW.isoformat())[0], 'snapshot_generated_utc': NOW.isoformat(),
           'snapshot_captured_utc': NOW.isoformat()}
    monkeypatch.setattr(cs, 'latest_picks', lambda root, archive: [row, {**row, 'home_team': 'Arsenal'}])
    monkeypatch.setattr(count_markets, 'verified_total', lambda r, final, cache_dir=None: 30 if r['side'] == 'Over' else 0)
    finals = {'Chelsea': ({'home_goals': 2, 'away_goals': 1}, 'VERIFIED'), 'Arsenal': (None, 'PENDING')}
    summary = cs.review(tmp_path, [], lambda r: finals[r['home_team']], KICK + timedelta(days=1))
    assert summary['all']['picks'] == 2 and summary['all']['graded'] == 1 and summary['all']['pending'] == 1
    assert summary['status'] == 'unvalidated, not bet' and summary['stake'] == 0
    out = tmp_path / cs.GRADES_DIR
    grades = list(csv.DictReader((out / 'grades.csv').open(encoding='utf-8')))
    assert [g['result_status'] for g in grades] == ['WON', 'PENDING']
    report = (out / 'report.md').read_text(encoding='utf-8')
    assert 'unvalidated, not bet' in report and summary['weeks']
    assert json.loads((out / 'summary.json').read_text(encoding='utf-8'))['all']['won'] == 1
