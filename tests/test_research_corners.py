import numpy as np
import pandas as pd
import pytest

import count_markets as cm
import research_corners as rc


def _season(rng, start, teams, rounds=2):
    rows, day = [], pd.Timestamp(start)
    for _ in range(rounds):
        for i, home in enumerate(teams):
            for away in teams[i + 1:] + teams[:i]:
                rows.append({'Date': day.strftime('%d/%m/%y'), 'HomeTeam': home, 'AwayTeam': away,
                             'FTHG': 1, 'FTAG': 0, 'HC': int(rng.poisson(5.5)), 'AC': int(rng.poisson(4.5)),
                             'HS': 12, 'AS': 10})
                day += pd.Timedelta(days=1)
    return pd.DataFrame(rows)


@pytest.fixture
def cache(tmp_path):
    rng = np.random.default_rng(1)
    teams = list('ABCDEF')
    (tmp_path / 'domestic_backfill').mkdir()
    _season(rng, '2025-08-01', teams).to_csv(tmp_path / 'domestic_backfill' / '2526_X1.csv', index=False)
    later = _season(rng, '2026-01-10', teams)
    later.to_csv(tmp_path / '2627_X1.csv', index=False)
    return tmp_path


def test_load_league_drops_rows_after_cutoff_and_never_loads_goals(cache):
    history = rc.load_league(cache, 'X1')
    dates = pd.to_datetime(history.Date, format='%d/%m/%Y')
    assert dates.max() <= rc.CUTOFF
    assert dates.min() == pd.Timestamp('2025-08-01')
    assert not {'FTHG', 'FTAG'} & set(history.columns)
    assert set(history.columns) <= set(rc.COLUMNS)


def test_forecasts_use_earlier_days_only(cache):
    frame = rc.matches(rc.load_league(cache, 'X1'))
    day = frame.date.iloc[40]
    changed = frame.copy()
    later = changed.date >= day
    changed.loc[later, 'home_count'] = 30
    changed.loc[later, 'total'] = changed.loc[later, 'home_count'] + changed.loc[later, 'away_count']
    for run in (lambda f: rc.walk_forward_k1(f, day, day, 120.0, 5.0), lambda f: rc.walk_forward_b0(f, day, day)):
        a, b = run(frame), run(changed)
        assert len(a) == 1
        assert a.mu.iloc[0] == pytest.approx(b.mu.iloc[0], rel=1e-9)
        assert a.alpha.iloc[0] == pytest.approx(b.alpha.iloc[0], rel=1e-9)


def test_nb_over_matches_count_markets():
    mu, alpha = 10.2, 0.02
    ours = rc.nb_over(mu, alpha)
    theirs = cm.probabilities(mu, alpha, 'corners')
    for line in rc.MAIN_LINES:
        assert ours[line] == pytest.approx(theirs[f'Corners Over {line:.1f}'], abs=1e-12)


def test_score_log_loss_is_for_the_observed_side():
    frame = pd.DataFrame([{'date': pd.Timestamp('2025-01-01'), 'home_team': 'A', 'away_team': 'B',
                           'total': 12, 'mu': 10.0, 'alpha': 0.01}])
    row = rc.score(frame).iloc[0]
    for line in rc.MAIN_LINES:
        assert row[f'll_{line}'] == pytest.approx(-np.log(row[f'p_over_{line}']))


def test_calibration_of_a_calibrated_forecast():
    rng = np.random.default_rng(3)
    p = rng.uniform(0.2, 0.8, 20000)
    y = rng.uniform(size=p.size) < p
    fit = rc.logistic_calibration(p, y)
    assert fit['slope'] == pytest.approx(1.0, abs=0.08)
    assert rc.band_check(p, y)['failing'] == 0


def test_shot_form_uses_earlier_days_only():
    rng = np.random.default_rng(5)
    frame = _season(rng, '2024-08-01', list('ABCD')).assign(HST=4, AST=3)
    frame['date'] = pd.to_datetime(frame.Date, format='%d/%m/%y')
    day = frame.date.iloc[10]
    changed = frame.copy()
    changed.loc[changed.date >= day, ['HS', 'HST']] = 40
    a, b = rc.shot_form(frame), rc.shot_form(changed)
    mask = frame.date <= day
    pd.testing.assert_frame_equal(a.loc[mask], b.loc[mask])


def test_second_stage_trains_on_earlier_rows_only():
    rng = np.random.default_rng(7)
    dates = pd.date_range('2021-01-01', periods=400, freq='D')
    rows = pd.DataFrame({'league': 'EPL', 'date': dates, 'home_team': 'A', 'away_team': 'B',
                         'total': rng.poisson(10, 400), 'mu_k1': 10.0, 'x': rng.normal(size=400)})
    start, end = dates[300], dates[-1]
    a = rc.walk_forward_stage2(rows, ['x'], start, end, step_days=28)
    later = rows.copy()
    later.loc[later.date >= start, 'total'] = 30
    b = rc.walk_forward_stage2(later, ['x'], start, end, step_days=28)
    first = a.date < start + pd.Timedelta(days=28)
    assert np.allclose(a.loc[first, 'mu'], b.loc[first, 'mu'])
    assert np.allclose(a.loc[first, 'alpha'], b.loc[first, 'alpha'])
