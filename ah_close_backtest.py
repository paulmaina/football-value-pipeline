"""Read-only backtest: production model vs Pinnacle closing Asian handicap (main line).

Walk-forward over football-data.co.uk CSVs already in the cache. Nothing here
changes the production model, policy, thresholds or workflows; it only reuses
the production prediction path (FootballValuePipelineV2._predict_row) on
historical rows and writes evaluation files under
football_output_v2/performance/ah_close_backtest/.

Model variants (all refit weekly on matches dated strictly before the refit date):
  dc       Dixon-Coles, half-life 480, plus the gated CSV shot features: the
           production configuration with no odds inputs at all.
  blend70  dc reweighted to 0.70 x Pinnacle OPENING 1X2 (power de-vig), as
           production blends its reference 1X2.
  prod     blend70 plus the Pinnacle opening O/U 2.5 totals anchor: the closest
           historical replica of the full production identity.
BBS / API-Football statistics are not rebuildable from CSV and stay disabled.

Pinnacle closing AH prices (AHCh/PCAHH/PCAHA) are evaluation targets only and are
never fed into any prediction. AHh/AHCh are the HOME handicap (negative = home
gives goals); see sign_convention_check.
"""

from __future__ import annotations

import argparse
import json
import math
import warnings
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path
from typing import Callable, Dict, List, Optional, Sequence, Tuple

import numpy as np
import pandas as pd

DIVISIONS = ('E0', 'SP1', 'D1', 'I1', 'F1', 'N1', 'P1', 'T1')
SEASONS = ('2122', '2223', '2324', '2425', '2526')
WARMUP_SEASONS = 1
OPEN_COLUMNS = ('AHh', 'PAHH', 'PAHA')
CLOSE_COLUMNS = ('AHCh', 'PCAHH', 'PCAHA')
OPEN_1X2_COLUMNS = ('PSH', 'PSD', 'PSA')
VARIANTS = {
    'dc': 'Dixon-Coles hl480 + gated CSV shots (no odds inputs)',
    'blend70': 'dc + 0.70 Pinnacle opening 1X2 blend',
    'prod': 'blend70 + Pinnacle opening O/U 2.5 anchor (production replica)',
}
REFIT_WEEKDAY = 1  # Tuesday: a refit sits between weekend and midweek rounds.
CLV_MIN_EV = 0.02
GAP_BUCKETS = ((0.0, 0.02, '<2pp'), (0.02, 0.05, '2-5pp'), (0.05, 0.10, '5-10pp'), (0.10, 1.01, '>=10pp'))
OUTPUT_DIR = Path('football_output_v2') / 'performance' / 'ah_close_backtest'
# Known matches for the sign check: (division, season, home, away, expected sign of AHCh).
SIGN_CHECK_MATCHES = (
    ('E0', '2324', 'Man City', 'Luton', -1),
    ('E0', '2324', 'Sheffield United', 'Man City', 1),
    ('SP1', '2324', 'Almeria', 'Real Madrid', 1),
)


# ---------------------------------------------------------------------------
# Asian handicap settlement
# ---------------------------------------------------------------------------

def split_line(line: float) -> Tuple[float, float]:
    """Quarter lines stake half on each adjacent line; others stake twice on one."""
    value = float(line)
    if not math.isfinite(value) or abs(value * 4 - round(value * 4)) > 1e-9:
        raise ValueError(f'Asian handicap line must be a multiple of 0.25: {line!r}')
    quarters = int(round(value * 4))
    value = quarters / 4
    return (value - 0.25, value + 0.25) if quarters % 2 else (value, value)


def line_type(line: float) -> str:
    quarters = int(round(float(line) * 4))
    return 'quarter' if quarters % 2 else ('half' if quarters % 4 else 'whole')


def settle(margin, line: float) -> Tuple[np.ndarray, np.ndarray]:
    """Fractions of stake won and lost for the side getting `line` at goal `margin`."""
    margin = np.asarray(margin, dtype=float)
    low, high = split_line(line)
    won = ((margin + low > 0).astype(float) + (margin + high > 0).astype(float)) / 2
    lost = ((margin + low < 0).astype(float) + (margin + high < 0).astype(float)) / 2
    return won, lost


def outcome_probabilities(margins: np.ndarray, probs: np.ndarray, line: float) -> Dict[str, float]:
    """Full/half win, push, half/full loss probabilities for the side getting `line`."""
    won, lost = settle(margins, line)
    return {'p_win': float(probs[won == 1].sum()), 'p_half_win': float(probs[won == 0.5].sum()),
            'p_push': float(probs[(won == 0) & (lost == 0)].sum()),
            'p_half_loss': float(probs[lost == 0.5].sum()), 'p_loss': float(probs[lost == 1].sum())}


def expected_return(outcomes: Dict[str, float], odds: float) -> float:
    """Expected profit per unit staked at decimal `odds`."""
    return ((outcomes['p_win'] + outcomes['p_half_win'] / 2) * (odds - 1)
            - outcomes['p_loss'] - outcomes['p_half_loss'] / 2)


def effective_probability(outcomes: Dict[str, float]) -> float:
    """q with zero expected return at odds 1/q; equals p_win on half lines."""
    won = outcomes['p_win'] + outcomes['p_half_win'] / 2
    lost = outcomes['p_loss'] + outcomes['p_half_loss'] / 2
    return won / (won + lost) if won + lost > 0 else 0.5


def realised_return(margin: int, line: float, odds: float) -> float:
    won, lost = settle(margin, line)
    return float(won * (odds - 1) - lost)


# ---------------------------------------------------------------------------
# Margin removal
# ---------------------------------------------------------------------------

def devig_proportional(home_odds: float, away_odds: float) -> Tuple[float, float]:
    q = np.array([1 / home_odds, 1 / away_odds])
    fair = q / q.sum()
    return float(fair[0]), float(fair[1])


def devig_shin(home_odds: float, away_odds: float) -> Tuple[float, float]:
    """Shin (1993) insider-trading margin removal; proportional when there is no margin."""
    q = np.array([1 / home_odds, 1 / away_odds])
    book = q.sum()
    if book <= 1:
        return devig_proportional(home_odds, away_odds)

    def fair(z):
        return (np.sqrt(z * z + 4 * (1 - z) * q * q / book) - z) / (2 * (1 - z))

    low, high = 0.0, 0.5
    for _ in range(100):
        mid = (low + high) / 2
        if fair(mid).sum() > 1:
            low = mid
        else:
            high = mid
    p = fair((low + high) / 2)
    p = p / p.sum()
    return float(p[0]), float(p[1])


# ---------------------------------------------------------------------------
# Data
# ---------------------------------------------------------------------------

def load_division(cache_dir: Path, division: str, seasons: Sequence[str] = SEASONS) -> pd.DataFrame:
    from football_value_pipeline_v2_standalone import read_csv_bytes, validated_match_history
    frames = []
    for season in seasons:
        path = Path(cache_dir) / f'{season}_{division}.csv'
        if not path.exists():
            raise FileNotFoundError(path)
        frame = read_csv_bytes(path.read_bytes()).copy()
        frame['Season'] = season
        frames.append(frame)
    history = pd.concat(frames, ignore_index=True, sort=False)
    history['Date'] = pd.to_datetime(history['Date'], dayfirst=True, errors='coerce')
    history = history.loc[history['Date'].notna() & history['FTHG'].notna() & history['FTAG'].notna()]
    history = validated_match_history(history.copy())
    history['Division'] = division
    return history.sort_values('Date', kind='stable').reset_index(drop=True)


def _price(value) -> Optional[float]:
    try:
        value = float(value)
    except (TypeError, ValueError):
        return None
    return value if math.isfinite(value) and value > 1 else None


def _line(value) -> Optional[float]:
    try:
        split_line(value)
    except (TypeError, ValueError):
        return None
    return float(value)


def eligible(row) -> bool:
    """Opening and closing Pinnacle AH plus Pinnacle opening 1X2 all present."""
    return (_line(row.get('AHh')) is not None and _line(row.get('AHCh')) is not None
            and all(_price(row.get(c)) for c in ('PAHH', 'PAHA', 'PCAHH', 'PCAHA', *OPEN_1X2_COLUMNS)))


def sign_convention_check(histories: Dict[str, pd.DataFrame]) -> List[Dict[str, object]]:
    """AHCh must be negative when the home side is the favourite; prints evidence."""
    checks = []
    for division, season, home, away, expected in SIGN_CHECK_MATCHES:
        frame = histories.get(division)
        if frame is None:
            continue
        rows = frame[(frame['Season'] == season) & (frame['HomeTeam'] == home) & (frame['AwayTeam'] == away)]
        if rows.empty:
            raise ValueError(f'Sign-check match missing: {home} v {away} {season}')
        row = rows.iloc[0]
        line = float(row['AHCh'])
        won, lost = settle(int(row['FTHG']) - int(row['FTAG']), line)
        check = {'division': division, 'date': row['Date'].date().isoformat(), 'home': home, 'away': away,
                 'score': f"{int(row['FTHG'])}-{int(row['FTAG'])}", 'AHh': float(row['AHh']), 'AHCh': line,
                 'PSCH': float(row['PSCH']), 'PSCA': float(row['PSCA']),
                 'home_favourite_1x2': bool(row['PSCH'] < row['PSCA']),
                 'home_ah_result': {(1.0, 0.0): 'WON', (0.5, 0.0): 'HALF_WON', (0.0, 0.0): 'PUSH',
                                    (0.0, 0.5): 'HALF_LOST', (0.0, 1.0): 'LOST'}[(float(won), float(lost))]}
        if np.sign(line) != expected or check['home_favourite_1x2'] != (line < 0):
            raise ValueError(f'AH sign convention violated: {check}')
        checks.append(check)
    return checks


# ---------------------------------------------------------------------------
# Walk-forward
# ---------------------------------------------------------------------------

def refit_dates(first: pd.Timestamp, last: pd.Timestamp) -> List[pd.Timestamp]:
    start = first.normalize() - pd.Timedelta(days=(first.weekday() - REFIT_WEEKDAY) % 7)
    return list(pd.date_range(start, last.normalize() + pd.Timedelta(days=7), freq='7D'))


def walk_forward(history: pd.DataFrame, score_from: pd.Timestamp,
                 fit: Callable[[pd.DataFrame, pd.Timestamp], object],
                 predict: Callable[[object, pd.Series], Optional[Dict[str, object]]],
                 is_eligible: Callable[[pd.Series], bool] = eligible) -> List[Dict[str, object]]:
    """Refit weekly on rows dated strictly before the refit date; predict that week."""
    scored = history[history['Date'] >= score_from]
    if scored.empty:
        return []
    out = []
    dates = refit_dates(scored['Date'].min(), scored['Date'].max())
    for refit, following in zip(dates[:-1], dates[1:]):
        week = scored[(scored['Date'] >= refit) & (scored['Date'] < following)]
        week = week[[bool(is_eligible(row)) for _, row in week.iterrows()]]
        if week.empty:
            continue
        train = history[history['Date'] < refit]
        # No lookahead: every training row predates the refit and so every prediction.
        assert train['Date'].max() < refit <= week['Date'].min()
        model = fit(train, refit)
        for _, row in week.iterrows():
            result = predict(model, row)
            if result is None:
                continue
            result.update(refit_date=refit.date().isoformat(), match_date=row['Date'].date().isoformat(),
                          train_max_date=train['Date'].max().date().isoformat(), n_train=int(len(train)))
            assert result['train_max_date'] < result['match_date']
            out.append(result)
    return out


def _margin_arrays(distribution) -> Tuple[np.ndarray, np.ndarray]:
    from asian_handicap import distribution as parse_distribution
    parsed = parse_distribution(distribution)
    margins = np.array(sorted(parsed), dtype=int)
    return margins, np.array([parsed[m] for m in margins], dtype=float)


def match_record(row: pd.Series, distributions: Dict[str, object]) -> Dict[str, object]:
    """Model and Pinnacle quantities for one match; distributions are home-minus-away margins."""
    open_line, close_line = float(row['AHh']), float(row['AHCh'])
    odds = {c: float(row[c]) for c in ('PAHH', 'PAHA', 'PCAHH', 'PCAHA')}
    margin = int(row['FTHG']) - int(row['FTAG'])
    close_won, close_lost = settle(margin, close_line)
    open_won, open_lost = settle(margin, open_line)
    record = {
        'league': row['Division'], 'season': row['Season'], 'home_team': row['HomeTeam'],
        'away_team': row['AwayTeam'], 'home_goals': int(row['FTHG']), 'away_goals': int(row['FTAG']),
        'open_line': open_line, 'open_home_odds': odds['PAHH'], 'open_away_odds': odds['PAHA'],
        'close_line': close_line, 'close_home_odds': odds['PCAHH'], 'close_away_odds': odds['PCAHA'],
        'close_line_type': line_type(close_line), 'open_line_type': line_type(open_line),
        'home_close_won': float(close_won), 'home_close_lost': float(close_lost),
        'home_open_won': float(open_won), 'home_open_lost': float(open_lost),
    }
    for name, prices, devig in (('close', ('PCAHH', 'PCAHA'), devig_proportional),
                                ('close_shin', ('PCAHH', 'PCAHA'), devig_shin),
                                ('open', ('PAHH', 'PAHA'), devig_proportional),
                                ('open_shin', ('PAHH', 'PAHA'), devig_shin)):
        record[f'pin_{name}_q_home'] = devig(odds[prices[0]], odds[prices[1]])[0]
    fair_home = 1 / record['pin_close_q_home']
    record['home_return_fair_close'] = float(close_won * (fair_home - 1) - close_lost)
    for variant, distribution in distributions.items():
        margins, probs = _margin_arrays(distribution)
        close = outcome_probabilities(margins, probs, close_line)
        record.update({f'{variant}_{k}': v for k, v in close.items()})
        record[f'{variant}_q_home'] = effective_probability(close)
        record[f'{variant}_er_home_fair_close'] = expected_return(close, fair_home)
        home_open = outcome_probabilities(margins, probs, open_line)
        away_open = outcome_probabilities(-margins, probs, -open_line)
        record[f'{variant}_ev_open_home'] = expected_return(home_open, odds['PAHH'])
        record[f'{variant}_ev_open_away'] = expected_return(away_open, odds['PAHA'])
    return record


def production_predictors(cache_dir: Path):
    """Two pipeline instances sharing one fit: blend-only and full production replica."""
    from football_value_pipeline_v2_standalone import FootballValuePipelineV2
    common = dict(cache_dir=str(cache_dir), market_weight=0.70, shot_features=True,
                  live_odds=False, bbs_statistics=False, devig_method='power')
    return (FootballValuePipelineV2(totals_anchor=False, **common),
            FootballValuePipelineV2(totals_anchor=True, **common))


def run_division(division: str, cache_dir: str) -> Dict[str, object]:
    from football_value_pipeline_v2_standalone import DixonColesModel
    warnings.filterwarnings('ignore')
    history = load_division(Path(cache_dir), division)
    score_from = history.loc[history['Season'] == SEASONS[WARMUP_SEASONS], 'Date'].min()
    blend, production = production_predictors(Path(cache_dir))
    skipped = {'unknown_team': 0}

    def fit(train, as_of):
        model = DixonColesModel(half_life_days=production.half_life_days, l2=production.l2,
                                max_goals=production.max_goals, bbs_statistics=False,
                                shot_features=True).fit(train, as_of=as_of)
        model.league_key = division
        return model

    def predict(model, row):
        # Production drops fixtures whose teams the model cannot resolve.
        if row['HomeTeam'] not in model.team_to_idx or row['AwayTeam'] not in model.team_to_idx:
            skipped['unknown_team'] += 1
            return None
        blended, _ = blend._predict_row(model, row)
        full, _ = production._predict_row(model, row)
        record = match_record(row, {'dc': full['raw_goal_margin_distribution'],
                                    'blend70': blended['goal_margin_distribution'],
                                    'prod': full['goal_margin_distribution']})
        record.update(blend_applied=bool(blended['market_blend_applied']),
                      totals_anchor_status=full['totals_anchor_status'],
                      shot_features_status=full.get('shot_features_status'),
                      production_model_version=full['model_version'])
        return record

    scored = history[history['Date'] >= score_from]
    rows = walk_forward(history, score_from, fit, predict)
    return {'division': division, 'rows': rows, 'scored_completed': int(len(scored)),
            'scored_eligible': int(sum(eligible(r) for _, r in scored.iterrows())),
            'missing_pinnacle_ah': int(sum(not eligible(r) for _, r in scored.iterrows())), **skipped}


# ---------------------------------------------------------------------------
# Metrics
# ---------------------------------------------------------------------------

def log_loss(p, y) -> np.ndarray:
    p = np.clip(np.asarray(p, dtype=float), 1e-12, 1 - 1e-12)
    y = np.asarray(y, dtype=float)
    return -(y * np.log(p) + (1 - y) * np.log(1 - p))


def block_bootstrap(values, blocks, n_boot: int = 2000, seed: int = 0) -> Tuple[float, float, float]:
    """Mean with a 95% interval resampling whole blocks (gameweeks)."""
    values = np.asarray(values, dtype=float)
    if values.size == 0:
        return float('nan'), float('nan'), float('nan')
    codes, block_index = np.unique(np.asarray(blocks), return_inverse=True)
    totals = np.bincount(block_index, weights=values, minlength=len(codes))
    counts = np.bincount(block_index, minlength=len(codes)).astype(float)
    draw = np.random.default_rng(seed).integers(0, len(codes), size=(n_boot, len(codes)))
    means = totals[draw].sum(axis=1) / counts[draw].sum(axis=1)
    return float(values.mean()), float(np.quantile(means, 0.025)), float(np.quantile(means, 0.975))


def line_bucket(line: float) -> str:
    # The requested buckets leave -1.25/+1.25 uncovered; they join the outer buckets.
    if line <= -1.25:
        return '<= -1.25'
    if line < 0:
        return '-1 to -0.25'
    if line == 0:
        return '0'
    return '+0.25 to +1' if line < 1.25 else '>= +1.25'


def gap_bucket(gap: float) -> str:
    return next(label for low, high, label in GAP_BUCKETS if low <= abs(gap) < high)


def primary_metrics(frame: pd.DataFrame, variant: str, n_boot: int) -> Dict[str, object]:
    """Half closing lines only: home covers or not, model vs Pinnacle fair close."""
    y = frame['home_close_won'].to_numpy()
    p_model, p_pin = frame[f'{variant}_q_home'].to_numpy(), frame['pin_close_q_home'].to_numpy()
    ll_model, ll_pin = log_loss(p_model, y), log_loss(p_pin, y)
    ll_shin = log_loss(frame['pin_close_shin_q_home'].to_numpy(), y)
    gain, low, high = block_bootstrap(ll_pin - ll_model, frame['refit_date'], n_boot)
    return {'n': int(len(frame)), 'weeks': int(frame['refit_date'].nunique()),
            'model_log_loss': float(ll_model.mean()), 'pinnacle_log_loss': float(ll_pin.mean()),
            'pinnacle_shin_log_loss': float(ll_shin.mean()),
            'model_brier': float(np.mean((p_model - y) ** 2)), 'pinnacle_brier': float(np.mean((p_pin - y) ** 2)),
            'log_loss_gain': gain, 'gain_low95': low, 'gain_high95': high}


def secondary_metrics(frame: pd.DataFrame, variant: str, n_boot: int) -> Dict[str, object]:
    """All lines: predicted vs settled home return per unit at Pinnacle fair close odds.

    Pinnacle predicts zero return at its own fair price, so its squared error is
    mean(R^2); positive skill means the model's expected returns explain the
    settled returns better than the close. Also the return from betting the
    side the model prefers at fair close odds.
    """
    realised = frame['home_return_fair_close'].to_numpy()
    predicted = frame[f'{variant}_er_home_fair_close'].to_numpy()
    skill, low, high = block_bootstrap(realised ** 2 - (realised - predicted) ** 2, frame['refit_date'], n_boot)
    q = frame['pin_close_q_home'].to_numpy()
    away_return = (frame['home_close_lost'] * (1 / (1 - q) - 1) - frame['home_close_won']).to_numpy()
    side_return = np.where(predicted > 0, realised, away_return)
    mean_return, r_low, r_high = block_bootstrap(side_return, frame['refit_date'], n_boot)
    return {'n': int(len(frame)), 'return_mse_skill': skill, 'skill_low95': low, 'skill_high95': high,
            'model_side_return_at_fair_close': mean_return, 'return_low95': r_low, 'return_high95': r_high}


def simulated_clv(frame: pd.DataFrame, variant: str, n_boot: int, min_ev: float = CLV_MIN_EV) -> Dict[str, object]:
    """SIMULATED: bet the side with model EV >= min_ev at Pinnacle opening; not achievable execution."""
    ev_home, ev_away = frame[f'{variant}_ev_open_home'], frame[f'{variant}_ev_open_away']
    home_bet = (ev_home >= ev_away) & (ev_home >= min_ev)
    away_bet = (ev_away > ev_home) & (ev_away >= min_ev)
    bets = []
    for side, mask in (('home', home_bet), ('away', away_bet)):
        part = frame[mask]
        sign = 1 if side == 'home' else -1
        odds = part[f'open_{side}_odds']
        won = part['home_open_won'] if side == 'home' else part['home_open_lost']
        lost = part['home_open_lost'] if side == 'home' else part['home_open_won']
        q_close = part['pin_close_q_home'] if side == 'home' else 1 - part['pin_close_q_home']
        q_shin = part['pin_close_shin_q_home'] if side == 'home' else 1 - part['pin_close_shin_q_home']
        same = part['open_line'] == part['close_line']
        # Closing line moved against the side we took means it now needs more: favourable.
        favourable = sign * (part['open_line'] - part['close_line']) > 0
        bets.append(pd.DataFrame({
            'refit_date': part['refit_date'], 'side': side, 'odds': odds,
            'ev': ev_home[mask] if side == 'home' else ev_away[mask],
            'profit': won * (odds - 1) - lost, 'same_line': same,
            'clv': np.where(same, odds * q_close - 1, np.nan),
            'clv_shin': np.where(same, odds * q_shin - 1, np.nan),
            'line_moved_favourable': np.where(same, np.nan, favourable.astype(float)),
            'favourite_side': np.where(sign * part['open_line'] < 0, 'favourite',
                                       np.where(part['open_line'] == 0, 'level', 'underdog'))}))
    bets = pd.concat(bets, ignore_index=True)
    out = {'label': 'SIMULATED - assumes every Pinnacle opening price was available; not achievable execution',
           'min_model_ev': min_ev, 'bets': int(len(bets))}
    if bets.empty:
        return out
    same = bets[bets['same_line']]
    roi, roi_low, roi_high = block_bootstrap(bets['profit'], bets['refit_date'], n_boot)
    clv, clv_low, clv_high = block_bootstrap(same['clv'], same['refit_date'], n_boot)
    moved = bets.loc[~bets['same_line'], 'line_moved_favourable']
    out.update({'mean_model_ev': float(bets['ev'].mean()), 'roi_at_opening': roi,
                'roi_low95': roi_low, 'roi_high95': roi_high,
                'same_line_bets': int(len(same)), 'mean_clv_vs_fair_close': clv,
                'clv_low95': clv_low, 'clv_high95': clv_high,
                'mean_clv_shin': float(same['clv_shin'].mean()) if len(same) else float('nan'),
                'share_clv_positive': float((same['clv'] > 0).mean()) if len(same) else float('nan'),
                'line_moved_bets': int(len(moved)),
                'share_line_moved_favourable': float(moved.mean()) if len(moved) else float('nan'),
                'by_side': {k: {'bets': int(len(g)), 'roi_at_opening': float(g['profit'].mean()),
                                'mean_clv': float(g['clv'].mean()) if g['same_line'].any() else float('nan')}
                            for k, g in bets.groupby('favourite_side')}})
    return out


def evaluate(frame: pd.DataFrame, n_boot: int = 2000) -> Dict[str, object]:
    half = frame[frame['close_line_type'] == 'half'].copy()
    half['line_bucket'] = half['close_line'].map(line_bucket)
    half['home_role'] = np.where(half['close_line'] < 0, 'home favourite', 'away favourite')
    summary = {'n_matches': int(len(frame)), 'n_half_line': int(len(half)), 'variants': VARIANTS,
               'primary': {}, 'secondary': {}, 'simulated_clv': {}, 'breakdowns': {}}
    breakdowns = (('league', 'league'), ('season', 'season'), ('line_bucket', 'line_bucket'),
                  ('home_role', 'home_role'))
    for variant in VARIANTS:
        summary['primary'][variant] = primary_metrics(half, variant, n_boot)
        summary['secondary'][variant] = {'all_lines': secondary_metrics(frame, variant, n_boot), **{
            kind: secondary_metrics(group, variant, n_boot)
            for kind, group in frame.groupby('close_line_type')}}
        summary['simulated_clv'][variant] = simulated_clv(frame, variant, n_boot)
        tables = {}
        for name, column in breakdowns:
            tables[name] = {str(k): primary_metrics(g, variant, n_boot) for k, g in half.groupby(column)}
        gaps = (half[f'{variant}_q_home'] - half['pin_close_q_home']).map(gap_bucket)
        tables['gap_bucket'] = {k: primary_metrics(g, variant, n_boot) for k, g in half.groupby(gaps)}
        summary['breakdowns'][variant] = tables
    # Sanity: the close should beat the open where the half line did not move.
    stable = half[half['open_line'] == half['close_line']]
    if len(stable):
        y = stable['home_close_won']
        summary['open_vs_close_same_half_line'] = {
            'n': int(len(stable)),
            'pinnacle_open_log_loss': float(log_loss(stable['pin_open_q_home'], y).mean()),
            'pinnacle_close_log_loss': float(log_loss(stable['pin_close_q_home'], y).mean()),
            **{f'{v}_log_loss': float(log_loss(stable[f'{v}_q_home'], y).mean()) for v in VARIANTS}}
    return summary


# ---------------------------------------------------------------------------
# Report
# ---------------------------------------------------------------------------

def _table(headers: Sequence[str], rows: Sequence[Sequence[object]]) -> str:
    def cell(value):
        return f'{value:.4f}' if isinstance(value, float) else str(value)
    lines = ['| ' + ' | '.join(headers) + ' |', '|' + '---|' * len(headers)]
    lines += ['| ' + ' | '.join(cell(v) for v in row) + ' |' for row in rows]
    return '\n'.join(lines)


def _interval(m: Dict[str, object], key='log_loss_gain', low='gain_low95', high='gain_high95', scale=1.0) -> str:
    return f"{m[key] * scale:+.4f} [{m[low] * scale:+.4f}, {m[high] * scale:+.4f}]"


def _call(low: float, high: float) -> str:
    return 'model better' if low > 0 else 'close better' if high < 0 else 'no detectable difference'


def verdict(summary: Dict[str, object]) -> List[str]:
    lines = []
    for variant in VARIANTS:
        p = summary['primary'][variant]
        s = summary['secondary'][variant]['all_lines']
        c = summary['simulated_clv'][variant]
        lines.append(f"- **{variant}**: half-line log-loss gain vs close {_interval(p)} -> {_call(p['gain_low95'], p['gain_high95'])}; "
                     f"all-line return skill {_interval(s, 'return_mse_skill', 'skill_low95', 'skill_high95')} -> "
                     f"{_call(s['skill_low95'], s['skill_high95'])}; simulated CLV (same line) "
                     + (_interval(c, 'mean_clv_vs_fair_close', 'clv_low95', 'clv_high95') if c.get('same_line_bets') else 'n/a') + '.')
        wins = [f"{name}={key} ({_interval(m)})" for name, table in summary['breakdowns'][variant].items()
                for key, m in table.items() if m['n'] >= 30 and m['gain_low95'] > 0]
        cells = sum(len(t) for t in summary['breakdowns'][variant].values())
        lines.append(f"  - Breakdown cells where the model's 95% interval excludes zero in its favour: "
                     f"{', '.join(wins) if wins else 'none'} (out of {cells} cells; ~{cells * 0.025:.1f} expected by chance alone).")
    return lines


def write_report(summary: Dict[str, object], sign_checks: List[Dict[str, object]], path: Path) -> None:
    parts = ['# Asian handicap backtest: production model vs Pinnacle close', '',
             'Read-only walk-forward backtest. No production model, policy, threshold or workflow was changed, '
             'and nothing here is a recommendation to change production.', '',
             f"Matches scored: {summary['n_matches']} (half closing lines: {summary['n_half_line']}). "
             f"Leagues: {', '.join(DIVISIONS)}; seasons {SEASONS[WARMUP_SEASONS]}-{SEASONS[-1]} scored, "
             f"{SEASONS[0]} warm-up only. Weekly refits on matches dated strictly before the refit date.", '',
             '## Variants', '']
    parts += [f'- `{k}`: {v}' for k, v in VARIANTS.items()]
    parts += ['', '## Sign convention check (AHh/AHCh = home handicap)', '',
              _table(['date', 'match', 'score', 'AHh', 'AHCh', 'PSCH', 'PSCA', 'home AH result'],
                     [[c['date'], f"{c['home']} v {c['away']}", c['score'], c['AHh'], c['AHCh'], c['PSCH'],
                       c['PSCA'], c['home_ah_result']] for c in sign_checks]),
              '', '## Verdict', '']
    parts += verdict(summary)
    parts += ['', '## Primary: half closing lines (no push), home covers', '',
              'Gain = Pinnacle log loss minus model log loss (positive = model better). '
              '95% interval from a paired bootstrap over gameweek blocks.', '',
              _table(['variant', 'n', 'model LL', 'Pinnacle LL (prop)', 'Pinnacle LL (Shin)', 'model Brier',
                      'Pinnacle Brier', 'LL gain [95%]'],
                     [[v, p['n'], p['model_log_loss'], p['pinnacle_log_loss'], p['pinnacle_shin_log_loss'],
                       p['model_brier'], p['pinnacle_brier'], _interval(p)]
                      for v, p in summary['primary'].items()])]
    sanity = summary.get('open_vs_close_same_half_line')
    if sanity:
        parts += ['', f"Sanity check, half lines unchanged open-to-close (n={sanity['n']}): Pinnacle open LL "
                      f"{sanity['pinnacle_open_log_loss']:.4f}, close LL {sanity['pinnacle_close_log_loss']:.4f}; "
                  + ', '.join(f"{v} LL {sanity[v + '_log_loss']:.4f}" for v in VARIANTS) + '.']
    parts += ['', '## Secondary: all lines, expected vs settled home return per unit at Pinnacle fair close', '',
              'Skill = mean(R^2) - mean((R - model expected return)^2); Pinnacle predicts zero at its own fair price. '
              'Model-side return = 1 unit on the side the model prefers at Pinnacle fair close odds.', '']
    rows = []
    for v, groups in summary['secondary'].items():
        for kind, s in groups.items():
            rows.append([v, kind, s['n'], _interval(s, 'return_mse_skill', 'skill_low95', 'skill_high95'),
                         _interval(s, 'model_side_return_at_fair_close', 'return_low95', 'return_high95')])
    parts.append(_table(['variant', 'lines', 'n', 'return skill [95%]', 'model-side return [95%]'], rows))
    for v, tables in summary['breakdowns'].items():
        parts += ['', f'## Breakdowns ({v}, half lines, LL gain [95%])', '']
        for name, table in tables.items():
            parts += [f'**{name}**', '',
                      _table([name, 'n', 'model LL', 'Pinnacle LL', 'LL gain [95%]'],
                             [[k, m['n'], m['model_log_loss'], m['pinnacle_log_loss'], _interval(m)]
                              for k, m in table.items()]), '']
    parts += ['## Simulated CLV (SIMULATED, not achievable execution)', '',
              f'Bet the side where model EV at the Pinnacle OPENING price and line is >= {CLV_MIN_EV:.0%}. '
              'CLV = opening odds x Pinnacle fair closing probability - 1, only where the opening and closing '
              'lines match; moved lines report whether the move favoured the bet. ROI settles at opening odds '
              'on the opening line. Assumes every opening price was available to bet at Pinnacle limits.', '',
              _table(['variant', 'bets', 'mean model EV', 'ROI at open [95%]', 'same-line bets',
                      'mean CLV [95%]', 'CLV (Shin)', 'CLV > 0', 'moved bets', 'moved favourably'],
                     [[v, c['bets'], c.get('mean_model_ev', float('nan')),
                       _interval(c, 'roi_at_opening', 'roi_low95', 'roi_high95') if c['bets'] else 'n/a',
                       c.get('same_line_bets', 0),
                       _interval(c, 'mean_clv_vs_fair_close', 'clv_low95', 'clv_high95') if c.get('same_line_bets') else 'n/a',
                       c.get('mean_clv_shin', float('nan')), c.get('share_clv_positive', float('nan')),
                       c.get('line_moved_bets', 0), c.get('share_line_moved_favourable', float('nan'))]
                      for v, c in summary['simulated_clv'].items()])]
    rows = [[v, k, b['bets'], b['roi_at_opening'], b['mean_clv']]
            for v, c in summary['simulated_clv'].items() for k, b in c.get('by_side', {}).items()]
    parts += ['', _table(['variant', 'bet side', 'bets', 'ROI at open', 'mean CLV'], rows), '']
    path.write_text('\n'.join(parts) + '\n', encoding='utf-8')


def _json_default(value):
    if isinstance(value, (np.floating, np.integer)):
        return value.item()
    raise TypeError(type(value))


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('--cache-dir', default='.football_cache')
    parser.add_argument('--output-dir', default=str(OUTPUT_DIR))
    parser.add_argument('--divisions', nargs='+', default=list(DIVISIONS))
    parser.add_argument('--workers', type=int, default=len(DIVISIONS))
    parser.add_argument('--bootstrap', type=int, default=2000)
    args = parser.parse_args(argv)
    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    histories = {d: load_division(Path(args.cache_dir), d) for d in args.divisions}
    sign_checks = sign_convention_check(histories)
    for check in sign_checks:
        print('sign check:', json.dumps(check))

    with ProcessPoolExecutor(max_workers=max(1, args.workers)) as pool:
        results = list(pool.map(run_division, args.divisions, [args.cache_dir] * len(args.divisions)))
    frame = pd.DataFrame([row for r in results for row in r['rows']])
    frame = frame.sort_values(['match_date', 'league', 'home_team'], kind='stable').reset_index(drop=True)
    # Belt and braces: the walk-forward asserts this per prediction as well.
    assert (frame['train_max_date'] < frame['match_date']).all()

    summary = evaluate(frame, args.bootstrap)
    summary['coverage'] = {r['division']: {k: r[k] for k in ('scored_completed', 'scored_eligible',
                                                             'missing_pinnacle_ah', 'unknown_team')}
                           for r in results}
    summary['coverage_by_season'] = frame.groupby(['league', 'season']).size().unstack(fill_value=0).to_dict()
    summary['production_model_versions'] = sorted(frame['production_model_version'].unique())
    summary['totals_anchor_status'] = frame['totals_anchor_status'].value_counts().to_dict()
    summary['shot_features_status'] = frame['shot_features_status'].value_counts().to_dict()
    summary['sign_convention_check'] = sign_checks

    frame.to_csv(out_dir / 'per_match.csv', index=False)
    (out_dir / 'summary.json').write_text(json.dumps(summary, indent=2, default=_json_default), encoding='utf-8')
    write_report(summary, sign_checks, out_dir / 'report.md')
    print('\n'.join(verdict(summary)))
    print(f'Wrote {out_dir}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
