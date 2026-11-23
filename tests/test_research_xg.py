"""C6X's features, fit and extraction rules on synthetic data (docs/plan.md, Phase 2i)."""
import importlib.util
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

import research_xg as rx

ROOT = Path(__file__).resolve().parents[1]


def _extractor():
    spec = importlib.util.spec_from_file_location('extract_api_football_xg', ROOT / 'scripts' / 'extract_api_football_xg.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _index():
    matches = [('EPL', '2024-02-01', 'A', 'B', 0, 0), ('EPL', '2024-02-08', 'B', 'A', 1, 3),
               ('EPL', '2024-02-15', 'A', 'C', 2, 2)]
    xg = {('EPL', '2024-02-01', 'A', 'B'): (2.0, 0.5), ('EPL', '2024-02-08', 'B', 'A'): (1.0, 1.0),
          ('EPL', '2024-02-15', 'A', 'C'): (9.0, 9.0)}
    return rx.team_index(matches, xg)


def test_features_use_strictly_earlier_days_and_shrink_to_goals():
    index = _index()
    (f, k) = rx.side_features(index[('EPL', 'A')], '2024-02-15')
    # A's two earlier matches: xG for 2.0 and 1.0 (mean 1.5), goals for 0 and 3 (1.5); against 0.5/1.0 vs 0/1.
    assert k == 2
    w = 2 / (2 + rx.SHRINK)
    assert f == pytest.approx((w * (1.5 - 1.5), w * (0.75 - 0.5)))
    # The match on the day itself (xG 9.0) is never read.
    (f_after, k_after) = rx.side_features(index[('EPL', 'A')], '2024-02-16')
    assert k_after == 3 and f_after != f


def test_no_history_league_or_club_gives_zero_features():
    index = _index()
    assert rx.side_features(index[('EPL', 'A')], '2024-02-01') == ((0., 0.), 0)
    assert rx.match_features(index, 'Eredivisie', 'A', 'B', '2024-03-01') == (((0., 0.), (0., 0.)), (0, 0))
    assert rx.match_features(index, 'EPL', 'Z', 'A', '2024-03-01')[1][0] == 0


def test_window_keeps_last_matches_only():
    matches = [('EPL', f'2024-01-{d:02d}', 'A', f'T{d}', 1, 1) for d in range(1, 21)]
    xg = {(m[0], m[1], m[2], m[3]): (float(i), 0.) for i, m in enumerate(matches)}
    index = rx.team_index(matches, xg)
    (f, k) = rx.side_features(index[('EPL', 'A')], '2024-02-01')
    assert k == rx.WINDOW
    expected_xg = np.mean(range(20 - rx.WINDOW, 20))
    assert f[0] == pytest.approx(rx.WINDOW / (rx.WINDOW + rx.SHRINK) * (expected_xg - 1))


def test_neutral_parameters_or_zero_features_return_c_rates():
    assert rx.adjusted_rates([1.4, 1.1], rx.NEUTRAL, [0.3, -0.2], [0.1, 0.]) == [1.4, 1.1]
    params = {**rx.NEUTRAL, 'alpha_xg_for': 0.2}
    assert rx.adjusted_rates([1.4, 1.1], params, [0., 0.], [0., 0.]) == [1.4, 1.1]
    home, away = rx.adjusted_rates([1.4, 1.1], params, [0.5, 0.], [0., 0.])
    assert home == pytest.approx(1.4 * np.exp(0.1)) and away == 1.1


def test_fit_is_neutral_in_warm_up_and_recovers_a_planted_effect():
    rng = np.random.default_rng(1)
    n = 4000
    rates = np.column_stack([rng.uniform(1.0, 1.8, n), rng.uniform(0.8, 1.4, n)])
    fh, fa = rng.normal(0, 0.3, (n, 2)), rng.normal(0, 0.3, (n, 2))
    lh = np.log(rates[:, 0]) + 0.3 * fh[:, 0] + 0.2 * fa[:, 1]
    la = np.log(rates[:, 1]) + 0.3 * fa[:, 0] + 0.2 * fh[:, 1]
    hg, ag = rng.poisson(np.exp(lh)), rng.poisson(np.exp(la))
    eligible = np.ones(n, bool)
    warm = rx.fit(rates[:100], hg[:100], ag[:100], fh[:100], fa[:100], eligible[:100])
    assert warm['status'] == 'warm_up' and all(warm[p] == 0 for p in rx.PARAMETERS)
    out = rx.fit(rates, hg, ag, fh, fa, eligible)
    assert out['status'] == 'fitted'
    assert out['alpha_xg_for'] == pytest.approx(0.3, abs=0.08)
    assert out['gamma_xg_against'] == pytest.approx(0.2, abs=0.08)
    assert abs(out['alpha_xg_against']) < 0.08 and abs(out['gamma_xg_for']) < 0.08


def test_walk_forward_fits_only_on_rows_before_each_origin():
    rng = np.random.default_rng(2)
    days = pd.date_range('2024-01-01', periods=1400, freq='6h')
    research = [{'date': d, 'goal_rates': [1.3, 1.1], 'home_goals': int(rng.poisson(1.3)),
                 'away_goals': int(rng.poisson(1.1))} for d in days]
    feats = [((0.1, 0.), (0., 0.)) for _ in research]
    counts = [(5, 5) for _ in research]
    windows = [(days[0], days[700]), (days[700], days[1399])]
    adjusted, fits = rx.walk_forward(research, feats, counts, windows)
    assert fits[0]['status'] == 'warm_up' and fits[0]['matches'] == 0
    assert fits[1]['matches'] == 700 and fits[1]['status'] == 'fitted'
    assert adjusted[0].tolist() == [1.3, 1.1]
    # Changing a result after the second origin moves neither fit.
    research[1000]['home_goals'] += 7
    _, again = rx.walk_forward(research, feats, counts, windows)
    assert again == fits


def test_zero_features_give_c6_exactly():
    import json
    import evaluation_harness as eh
    spec = importlib.util.spec_from_file_location('c6_xg_report', ROOT / 'scripts' / 'c6_xg_report.py')
    report = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(report)
    cfg = json.loads(eh.CONFIG.read_text(encoding='utf-8'))
    end = pd.Timestamp('2023-03-01')
    cfg = {**cfg, 'end_exclusive': end.date().isoformat()}
    rng = np.random.default_rng(7)
    dates = pd.date_range('2022-08-01', end - pd.Timedelta(days=1), periods=2600)
    research = []
    for i, d in enumerate(dates):
        key = f'EPL|{d.date()}|H{i}|A{i}'
        research.append({'identity': {'league': 'EPL', 'date': d.date().isoformat(), 'phase': 'development',
                                      'week': f'{d.isocalendar().year}-W{d.isocalendar().week:02d}',
                                      'fixture_key': key, 'market_book': ''},
                         'date': d, 'fixture_key': key, 'goal_rates': list(rng.uniform(.9, 1.9, 2)),
                         'home_goals': int(rng.poisson(1.5)), 'away_goals': int(rng.poisson(1.1)), 'scored': True})
    feats = [((0., 0.), (0., 0.)) for _ in research]
    counts = [(8, 8) for _ in research]
    c6_records, c6_calib, _, _ = eh.low_score_sharpen_candidate(research, cfg, end, {'C6'})
    r, k, fits = report.c6x_candidate(research, feats, counts, cfg, end)
    assert any(f['status'] == 'fitted' for f in fits)
    strip = lambda rows: [{x: v for x, v in row.items() if x != 'candidate'} for row in rows]
    assert strip(r) == strip(c6_records)
    assert strip(k) == strip(c6_calib)


def test_no_odds_or_market_input():
    text = (ROOT / 'research_xg.py').read_text(encoding='utf-8')
    for token in ('market_implied', 'narrow_margin', 'book_prices', 'market_matrix', 'cagey', 'PSH', 'PSA',
                  'B365', 'AHh', 'P>2.5', 'score_matrix_json', 'published_proxy', 'odds_api', 'pinnacle'):
        assert token not in text, token


def test_extraction_scope_drops_play_offs_qualifiers_and_keeps_main_rounds():
    ex = _extractor()
    assert ex.scope('EPL', 'Regular Season - 12') == 'kept'
    assert ex.scope('Bundesliga', 'Relegation Round') == 'play_off'
    assert ex.scope('SerieA', 'Relegation Decider') == 'play_off'
    assert ex.scope('UCL', 'Group C - 3') == 'kept'
    assert ex.scope('UCL', 'League Stage - 8') == 'kept'
    assert ex.scope('UCL', 'Round of 16') == 'kept'
    assert ex.scope('UCL', 'Knockout Round Play-offs') == 'play_off'
    assert ex.scope('UCL', 'Play-offs') == 'play_off'
    assert ex.scope('UCL', '2nd Qualifying Round') == 'qualifier'
    assert ex.scope('UCL', 'Preliminary Round') == 'qualifier'


def test_expected_goals_parser_matches_teams_by_provider_id():
    ex = _extractor()
    match = {'home': {'id': 1}, 'away': {'id': 2}}
    payload = {'response': [
        {'team': {'id': 2}, 'statistics': [{'type': 'expected_goals', 'value': '0.40'}]},
        {'team': {'id': 1}, 'statistics': [{'type': 'Total Shots', 'value': 9}, {'type': 'expected_goals', 'value': '1.75'}]}]}
    assert ex.expected_goals(payload, match) == (1.75, 0.40)
    payload['response'][0]['statistics'][0]['value'] = None
    assert ex.expected_goals(payload, match) == 'xg_missing'
    assert ex.expected_goals({'unavailable': True}, match) == 'response_unavailable'
    assert ex.expected_goals({'response': payload['response'][:1]}, match) == 'response_not_two_teams'
