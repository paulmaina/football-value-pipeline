"""Cagey-match correction to the market-implied fair price (pre-registered).

The market-implied matrix (market_implied fit B; fit A only when B is
unusable) overstates big goal margins. Two logistic regressions recalibrate

    P(|margin| >= 2) and P(|margin| >= 3)

each on standardised features [logit(matrix P for that target), P(over 2.5),
|P(home) - P(away)|, draw probability], all margin-free Pinnacle values. The
correction rescales the matrix by margin class {|m| <= 1}, {|m| = 2},
{|m| >= 3} to the corrected totals, keeping each class's internal shape and
its home/away split, so every AH line is priced exactly from the corrected
matrix. corrected_cagey_score = corrected P(|margin| >= 2).

Training data: football-data.co.uk CSVs, Pinnacle CLOSE prices, 8 leagues.
Coefficients are saved with a version id, the training date range and a
fingerprint of the training rows.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import warnings
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path
from typing import Dict, Iterable, List, Mapping, Optional, Sequence, Tuple

import numpy as np
import pandas as pd
from scipy.optimize import minimize

import market_implied as mi
from ah_close_backtest import DIVISIONS, load_division
from market_implied_calibration import COLUMNS_1X2, COLUMNS_OU, drop_reason
from price_edge_backtest import available_seasons, week_block

MODEL_DIR = Path(__file__).with_name('narrow_margin_models')
GATE_CUTOFF = pd.Timestamp('2024-01-01')
GATE_VERSION = 'cagey-correction-pre2024-v1'
# Production fit after the gate passed: same specification, every season through
# the latest completed one (2024/25). Refits only by a future PR.
PRODUCTION_VERSION = 'cagey-correction-through-2425-v1'
PRODUCTION_UNTIL = pd.Timestamp('2025-07-01')
TARGETS = (2, 3)
FEATURES = ('logit_matrix_p', 'p_over_2_5', 'abs_home_minus_away', 'p_draw')
EPS = 1e-6
FINGERPRINT_COLUMNS = ('Division', 'Date', 'HomeTeam', 'AwayTeam', 'FTHG', 'FTAG',
                       *COLUMNS_1X2, *COLUMNS_OU, 'AHCh', 'PCAHH', 'PCAHA')


# ---------------------------------------------------------------------------
# Matrix correction
# ---------------------------------------------------------------------------

def class_masks(abs_margin: np.ndarray) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    return abs_margin <= 1, abs_margin == 2, abs_margin >= 3


def class_targets(p2: float, p3: float) -> Tuple[float, float, float]:
    """Class totals for the corrected P(>= 2) and P(>= 3); P(>= 3) is capped at P(>= 2)."""
    p2 = min(max(float(p2), 0.0), 1.0)
    p3 = min(max(float(p3), 0.0), p2)
    return 1 - p2, p2 - p3, p3


def _rescale(values: np.ndarray, abs_margin: np.ndarray, p2: float, p3: float) -> np.ndarray:
    out = np.asarray(values, dtype=float).copy()
    for mask, target in zip(class_masks(abs_margin), class_targets(p2, p3)):
        total = out[mask].sum()
        if total <= 0:
            if target > 1e-12:
                raise ValueError('Cannot move probability into an empty margin class')
            continue
        out[mask] *= target / total
    return out / out.sum()


def correct_matrix(matrix: np.ndarray, p2: float, p3: float) -> np.ndarray:
    """Score matrix rescaled by margin class; each class keeps its shape and home/away split."""
    size = matrix.shape[0]
    goals = np.arange(size)
    abs_margin = np.abs(goals[:, None] - goals[None, :])
    return _rescale(matrix, abs_margin, p2, p3)


def correct_distribution(margins: np.ndarray, probs: np.ndarray, p2: float, p3: float) -> np.ndarray:
    """The same correction on a home-margin distribution (sufficient for AH pricing)."""
    return _rescale(probs, np.abs(margins), p2, p3)


def margin_tail(margins: np.ndarray, probs: np.ndarray, goals: int) -> float:
    return float(probs[np.abs(margins) >= goals].sum())


def price_distribution(margins: np.ndarray, probs: np.ndarray, side: str, line: float) -> Dict[str, float]:
    """Fair win-share, odds and settlement probabilities from a margin distribution."""
    from ah_close_backtest import effective_probability, outcome_probabilities
    outcomes = outcome_probabilities(mi.side_margins(margins, side), probs, line)
    q = effective_probability(outcomes)
    return {'win_share': q, 'fair_odds': 1 / q if q > 0 else math.inf,
            'p_no_loss': outcomes['p_win'] + outcomes['p_half_win'] + outcomes['p_push'], **outcomes}


# ---------------------------------------------------------------------------
# Logistic recalibration
# ---------------------------------------------------------------------------

def _logit(p) -> np.ndarray:
    p = np.clip(np.asarray(p, dtype=float), EPS, 1 - EPS)
    return np.log(p / (1 - p))


def feature_matrix(frame: pd.DataFrame, goals: int) -> np.ndarray:
    return np.column_stack([_logit(frame[f'matrix_p{goals}']), frame['p_over_2_5'],
                            (frame['p_home'] - frame['p_away']).abs(), frame['p_draw']]).astype(float)


def fit_logistic(x: np.ndarray, y: np.ndarray) -> Dict[str, object]:
    """Unpenalised logistic regression on standardised features (deterministic BFGS)."""
    mean, std = x.mean(axis=0), x.std(axis=0)
    std = np.where(std > 0, std, 1.0)
    z = np.column_stack([np.ones(len(x)), (x - mean) / std])

    def loss(beta):
        eta = z @ beta
        return float(np.mean(np.logaddexp(0, eta) - y * eta))

    def grad(beta):
        p = 1 / (1 + np.exp(-(z @ beta)))
        return z.T @ (p - y) / len(y)

    result = minimize(loss, np.zeros(z.shape[1]), jac=grad, method='BFGS', options={'gtol': 1e-10, 'maxiter': 1000})
    if not result.success and result.fun > loss(np.zeros(z.shape[1])):
        raise ValueError(f'Logistic fit failed: {result.message}')
    return {'intercept': float(result.x[0]), 'coefficients': [float(v) for v in result.x[1:]],
            'feature_mean': [float(v) for v in mean], 'feature_std': [float(v) for v in std],
            'training_log_loss': float(result.fun)}


def predict(params: Mapping, x: np.ndarray) -> np.ndarray:
    z = (np.atleast_2d(x) - np.array(params['feature_mean'])) / np.array(params['feature_std'])
    return 1 / (1 + np.exp(-(params['intercept'] + z @ np.array(params['coefficients']))))


def features_for(p_matrix: float, p_over: float, p_home: float, p_away: float, p_draw: float) -> np.ndarray:
    return np.array([[float(_logit(p_matrix)), p_over, abs(p_home - p_away), p_draw]])


def corrected_tails(model: Mapping, matrix_p2: float, matrix_p3: float, inputs: Mapping) -> Tuple[float, float]:
    """Corrected P(>= 2) and P(>= 3) for one fixture; P(>= 3) never above P(>= 2)."""
    common = (inputs['p_over_2_5'], inputs['p_home'], inputs['p_away'], inputs['p_draw'])
    p2 = float(predict(model['targets']['2'], features_for(matrix_p2, *common))[0])
    p3 = float(predict(model['targets']['3'], features_for(matrix_p3, *common))[0])
    return p2, min(p3, p2)


def fingerprint(rows: pd.DataFrame) -> str:
    keys = rows.reindex(columns=list(FINGERPRINT_COLUMNS)).astype(object).map(str).agg('|'.join, axis=1).sort_values()
    return hashlib.sha256('\n'.join(keys).encode()).hexdigest()


def train(frame: pd.DataFrame, *, version: str, until: pd.Timestamp) -> Dict[str, object]:
    """Fit both targets on matches dated strictly before `until`."""
    data = frame[frame.date < until]
    if data.empty:
        raise ValueError('No training matches before the cutoff')
    if not (data.date < until).all():
        raise AssertionError('Training data crosses the cutoff')
    return {'version': version, 'features': list(FEATURES), 'targets': {
                str(g): fit_logistic(feature_matrix(data, g), (data.abs_margin >= g).astype(float).to_numpy())
                for g in TARGETS},
            'training_until_exclusive': until.date().isoformat(),
            'training_first_date': data.date.min().date().isoformat(),
            'training_last_date': data.date.max().date().isoformat(),
            'training_matches': int(len(data)), 'training_fingerprint': fingerprint(data),
            'training_fit_counts': {k: int(v) for k, v in data.fit.value_counts().items()},
            'matrix_source': 'market_implied fit B (1X2 + O/U 2.5 + main AH), fit A only when B is unusable'}


def corrected_frame_p2(frame: pd.DataFrame, model: Mapping) -> np.ndarray:
    return predict(model['targets']['2'], feature_matrix(frame, 2))


def corrected_frame_p3(frame: pd.DataFrame, model: Mapping) -> np.ndarray:
    return np.minimum(predict(model['targets']['3'], feature_matrix(frame, 3)), corrected_frame_p2(frame, model))


def finalise(model: Dict[str, object], frame: pd.DataFrame, until: pd.Timestamp) -> Dict[str, object]:
    """Record the training-data 20th percentile of corrected_cagey_score (the cagey-tier cap)."""
    data = frame[frame.date < until]
    model['training_cagey_p20'] = float(np.quantile(corrected_frame_p2(data, model), 0.20))
    return model


def save(model: Mapping, directory: Path = MODEL_DIR) -> Path:
    directory.mkdir(parents=True, exist_ok=True)
    path = directory / f"{model['version']}.json"
    path.write_text(json.dumps(model, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    return path


def load(version: str, directory: Path = MODEL_DIR) -> Dict[str, object]:
    return json.loads((Path(directory) / f'{version}.json').read_text(encoding='utf-8'))


def versions(directory: Path = MODEL_DIR) -> Dict[str, object]:
    """The recorded gate and production versions."""
    return json.loads((Path(directory) / 'index.json').read_text(encoding='utf-8'))


def production_model(directory: Path = MODEL_DIR) -> Dict[str, object]:
    return load(versions(directory)['production']['version'], directory)


# ---------------------------------------------------------------------------
# Fixed quintile boundaries for correction monitoring
# ---------------------------------------------------------------------------

QUINTILE_PROBABILITIES = (0.2, 0.4, 0.6, 0.8)
QUINTILE_LABELS = ('Q1 cagiest', 'Q2', 'Q3', 'Q4', 'Q5 most open')


def model_digest(model: Mapping) -> str:
    """Content hash of a model (independent of file line endings)."""
    return hashlib.sha256(json.dumps(model, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def quintile_boundaries(frame: pd.DataFrame, model: Mapping) -> Dict[str, object]:
    """corrected_cagey_score quintile cutoffs on the model's own training rows; never refits."""
    until = pd.Timestamp(model['training_until_exclusive'])
    data = frame[frame.date < until]
    if fingerprint(data) != model['training_fingerprint']:
        raise ValueError("Training rows differ from the model's recorded training data")
    bounds = [float(b) for b in np.quantile(corrected_frame_p2(data, model), QUINTILE_PROBABILITIES)]
    if not math.isclose(bounds[0], model['training_cagey_p20'], rel_tol=0, abs_tol=1e-12):
        raise ValueError('Recomputed 20th percentile differs from the model record')
    return {'model_version': model['version'], 'model_sha256': model_digest(model),
            'training_fingerprint': model['training_fingerprint'],
            'training_until_exclusive': model['training_until_exclusive'],
            'training_first_date': model['training_first_date'], 'training_last_date': model['training_last_date'],
            'training_matches': model['training_matches'],
            'score': 'corrected P(|margin| >= 2) (corrected_cagey_score)',
            'probabilities': list(QUINTILE_PROBABILITIES), 'boundaries': bounds, 'labels': list(QUINTILE_LABELS),
            'rule': 'Q1 when score <= boundaries[0]; Qk when boundaries[k-2] < score <= boundaries[k-1]; '
                    'Q5 when score > boundaries[3]. Fixed once from training data; never recomputed from outcomes.'}


def quintile_path(version: str, directory: Path = MODEL_DIR) -> Path:
    return Path(directory) / f'{version}.quintiles.json'


def save_quintiles(data: Mapping, directory: Path = MODEL_DIR) -> Path:
    """Persist once: an existing file may only be rewritten with identical content."""
    path = quintile_path(data['model_version'], directory)
    text = json.dumps(data, indent=2, sort_keys=True) + '\n'
    if path.exists() and json.loads(path.read_text(encoding='utf-8')) != json.loads(text):
        raise ValueError(f'{path.name} already exists with different boundaries')
    path.write_text(text, encoding='utf-8')
    return path


def load_quintiles(model: Mapping, directory: Path = MODEL_DIR) -> Dict[str, object]:
    """Boundaries bound to exactly this model (version and content hash)."""
    data = json.loads(quintile_path(model['version'], directory).read_text(encoding='utf-8'))
    if data.get('model_version') != model['version'] or data.get('model_sha256') != model_digest(model):
        raise ValueError('Quintile boundaries belong to a different model')
    bounds = data.get('boundaries')
    if not isinstance(bounds, list) or len(bounds) != 4 or sorted(bounds) != bounds:
        raise ValueError('Invalid quintile boundaries')
    return data


def quintile_label(score: float, boundaries: Sequence[float]) -> str:
    return QUINTILE_LABELS[int(np.searchsorted(np.asarray(boundaries, dtype=float), float(score), side='left'))]


# ---------------------------------------------------------------------------
# Historical dataset (shared with the holdout gate report)
# ---------------------------------------------------------------------------

def match_record(row) -> Optional[Dict[str, object]]:
    """One historical match: fit B (else A), matrix tails, margin distribution and outcome."""
    targets = mi.targets_from_prices(tuple(float(row[c]) for c in COLUMNS_1X2),
                                     tuple(float(row[c]) for c in COLUMNS_OU),
                                     (float(row['AHCh']), float(row['PCAHH']), float(row['PCAHA'])))
    fit_b = mi.fit(targets, include_ah=True)
    result = fit_b if fit_b.usable else mi.fit(targets, include_ah=False)
    if not result.usable:
        return None
    margins, probs = mi.margin_distribution(result.matrix)
    return {'match': f"{row['Division']}|{row['Date'].date()}|{row['HomeTeam']}", 'date': row['Date'],
            'week': week_block(row['Date']), 'league': row['Division'], 'season': row['Season'],
            'home_team': row['HomeTeam'], 'away_team': row['AwayTeam'],
            'home_odds': float(row['PSCH']), 'away_odds': float(row['PSCA']), 'fit': result.kind,
            'p_home': targets['home'], 'p_draw': targets['draw'], 'p_away': targets['away'],
            'p_over_2_5': targets['over_2_5'], 'matrix_p2': margin_tail(margins, probs, 2),
            'matrix_p3': margin_tail(margins, probs, 3), 'margin': int(row['FTHG']) - int(row['FTAG']),
            'abs_margin': abs(int(row['FTHG']) - int(row['FTAG'])), 'ah_line': float(row['AHCh']),
            'ah_home_close': float(row['PCAHH']), 'ah_away_close': float(row['PCAHA']),
            'probs': probs, **{c: row[c] for c in FINGERPRINT_COLUMNS if c not in ('Date',)}}


def division_records(division: str, cache_dir: str) -> List[Dict[str, object]]:
    warnings.filterwarnings('ignore')
    history = load_division(Path(cache_dir), division, available_seasons(Path(cache_dir), division))
    records = []
    for _, row in history.iterrows():
        if drop_reason(row) is None:
            record = match_record(row)
            if record is not None:
                records.append(record)
    return records


def build_dataset(cache_dir: Path = Path('.football_cache'), divisions: Sequence[str] = DIVISIONS,
                  workers: int = len(DIVISIONS)) -> pd.DataFrame:
    if workers > 1:
        with ProcessPoolExecutor(max_workers=workers) as pool:
            parts = list(pool.map(division_records, divisions, [str(cache_dir)] * len(divisions)))
    else:
        parts = [division_records(d, str(cache_dir)) for d in divisions]
    frame = pd.DataFrame([r for p in parts for r in p])
    frame['Date'] = frame['date']
    return frame.sort_values(['date', 'league', 'home_team'], kind='stable').reset_index(drop=True)


MARGINS = np.arange(-mi.MAX_GOALS, mi.MAX_GOALS + 1)


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('--cache-dir', default='.football_cache')
    parser.add_argument('--until', default=GATE_CUTOFF.date().isoformat(), help='train on matches before this date')
    parser.add_argument('--version', default=GATE_VERSION)
    parser.add_argument('--workers', type=int, default=len(DIVISIONS))
    parser.add_argument('--divisions', nargs='+', default=list(DIVISIONS))
    parser.add_argument('--model-dir', default=str(MODEL_DIR))
    parser.add_argument('--quintiles', action='store_true',
                        help='write the fixed monitoring quintile boundaries of the saved --version model (no refit)')
    args = parser.parse_args(argv)
    frame = build_dataset(Path(args.cache_dir), args.divisions, workers=args.workers)
    if args.quintiles:
        data = quintile_boundaries(frame, load(args.version, Path(args.model_dir)))
        print(f"Saved {save_quintiles(data, Path(args.model_dir))}: boundaries {data['boundaries']}")
        return 0
    until = pd.Timestamp(args.until)
    model = finalise(train(frame, version=args.version, until=until), frame, until)
    print(f"Saved {save(model, Path(args.model_dir))}: {model['training_matches']} matches "
          f"{model['training_first_date']}..{model['training_last_date']}")
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
