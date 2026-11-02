"""Pre-registered holdout gate for the cagey-match correction (offline report).

Uses ONLY the saved pre-2024 gate model (narrow_margin_models/<GATE_VERSION>.json)
on matches from 2024-01-01 onward. Nothing is tuned here: the features, fit
period, test period, gate and cagey-tier rules were fixed before this ran.

  a) log-loss gain vs the uncorrected matrix for 2+ margins (gameweek-block 95%);
  b) return of betting AH +1 .. +2 at the CORRECTED and UNCORRECTED fair price,
     both sides, by corrected_cagey_score quintile and by tag;
  c) the same per test season (2023/24 second half, 2024/25, 2025/26);
  d) cagey-tier simulation at Pinnacle's CLOSING main AH line (limited);
  e) identifier comparison: even_odds vs the cagiest matches by corrected score.

GATE PASSES only if (a) the interval is entirely above 0; AND (b) the pooled
corrected return over +1..+2 has an interval containing 0 while the pooled
uncorrected return is above 0; AND (c) no test season's 2+ log-loss gain has
an interval entirely below 0. (d) and (e) are reported, not gated.
Output: football_output_v2/performance/cagey_correction/ (report.md, summary.json).
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Dict, List, Optional, Sequence

import numpy as np
import pandas as pd

import narrow_margin as nm
from ah_close_backtest import _json_default, _table, block_bootstrap, settle
from price_edge_shortlist import BALANCED_ODDS, EVEN_ODDS_MIN, HIGH_DRAW, LOW_TOTAL

OUTPUT_DIR = Path('football_output_v2') / 'performance' / 'cagey_correction'
PLUS_LINES = (1.0, 1.25, 1.5, 1.75, 2.0)
TIER_LINES = (1.0, 1.25, 1.5, 1.75, 2.0, 2.25)
TIER_MIN_NO_LOSS = 0.85
TIER_MAX_ODDS = 3.00
TOLERANCE = 1e-9
QUINTILES = ('Q1 cagiest', 'Q2', 'Q3', 'Q4', 'Q5 most open')
TAGS = ('balanced', 'low_total', 'high_draw', 'even_odds')
TEST_SEASONS = {'2023/24 second half': '2324', '2024/25': '2425', '2025/26': '2526'}


# ---------------------------------------------------------------------------
# Data
# ---------------------------------------------------------------------------

def add_tags(frame: pd.DataFrame) -> pd.DataFrame:
    """Tags from Pinnacle close: raw odds for balanced/even_odds, margin-free probabilities otherwise."""
    low, high = BALANCED_ODDS
    out = frame.copy()
    out['balanced'] = out.home_odds.between(low, high) & out.away_odds.between(low, high)
    out['low_total'] = out.p_over_2_5 < LOW_TOTAL
    out['high_draw'] = out.p_draw >= HIGH_DRAW
    out['even_odds'] = (out.home_odds >= EVEN_ODDS_MIN) & (out.away_odds >= EVEN_ODDS_MIN)
    return out


def apply_model(frame: pd.DataFrame, model) -> pd.DataFrame:
    out = frame.copy()
    out['corrected_p2'] = nm.corrected_frame_p2(out, model)
    out['corrected_p3'] = nm.corrected_frame_p3(out, model)
    out['corrected_probs'] = [nm.correct_distribution(nm.MARGINS, probs, p2, p3)
                              for probs, p2, p3 in zip(out.probs, out.corrected_p2, out.corrected_p3)]
    return out


def verify_gate_model(frame: pd.DataFrame, model) -> None:
    """The gate model must be trained strictly before 2024 on exactly these training rows."""
    cutoff = pd.Timestamp(model['training_until_exclusive'])
    if cutoff != nm.GATE_CUTOFF or pd.Timestamp(model['training_last_date']) >= nm.GATE_CUTOFF:
        raise AssertionError('Gate model includes data on or after 2024-01-01')
    if nm.fingerprint(frame[frame.date < cutoff]) != model['training_fingerprint']:
        raise AssertionError('Gate model was not trained on this pre-2024 data')


def bet_rows(frame: pd.DataFrame, lines: Sequence[float] = PLUS_LINES) -> pd.DataFrame:
    """Both sides of every listed plus line, settled at the corrected and uncorrected fair price."""
    rows = []
    for record in frame.itertuples():
        for side in ('home', 'away'):
            side_margin = record.margin if side == 'home' else -record.margin
            for line in lines:
                won, lost = settle(side_margin, line)
                entry = {'match': record.match, 'week': record.week, 'season': record.season, 'side': side,
                         'line': line, 'quintile': record.quintile, **{t: getattr(record, t) for t in TAGS}}
                for label, probs in (('corrected', record.corrected_probs), ('uncorrected', record.probs)):
                    q = nm.price_distribution(nm.MARGINS, probs, side, line)['win_share']
                    entry[f'{label}_return'] = float(won * (1 / q - 1) - lost) if 0 < q < 1 else np.nan
                rows.append(entry)
    return pd.DataFrame(rows)


def log_loss(p, y) -> np.ndarray:
    p = np.clip(np.asarray(p, dtype=float), 1e-12, 1 - 1e-12)
    return -(y * np.log(p) + (1 - y) * np.log(1 - p))


def interval(values, blocks, n_boot) -> Dict[str, float]:
    mean, low, high = block_bootstrap(values, blocks, n_boot)
    return {'n': int(len(values)), 'mean': mean, 'low95': low, 'high95': high}


def log_loss_gain(frame: pd.DataFrame, goals: int, n_boot: int) -> Dict[str, float]:
    y = (frame.abs_margin >= goals).astype(float).to_numpy()
    gain = log_loss(frame[f'matrix_p{goals}'], y) - log_loss(frame[f'corrected_p{goals}'], y)
    return interval(gain, frame.week, n_boot)


def returns(bets: pd.DataFrame, n_boot: int) -> Dict[str, Dict[str, float]]:
    return {label: interval(bets[f'{label}_return'].dropna(), bets.loc[bets[f'{label}_return'].notna(), 'week'], n_boot)
            for label in ('corrected', 'uncorrected')}


# ---------------------------------------------------------------------------
# Gate, tier simulation, identifier comparison
# ---------------------------------------------------------------------------

def gate(a: Dict, b: Dict, seasons: Dict[str, Dict]) -> Dict[str, object]:
    checks = {
        'a_log_loss_gain_above_zero': a['low95'] > 0,
        'b_corrected_interval_contains_zero': b['corrected']['low95'] <= 0 <= b['corrected']['high95'],
        'b_uncorrected_above_zero': b['uncorrected']['mean'] > 0,
        'c_no_season_significantly_worse': all(s['high95'] >= 0 for s in seasons.values()),
    }
    return {'pass': all(checks.values()), 'checks': checks}


def tier_simulation(test: pd.DataFrame, model, n_boot: int) -> Dict[str, object]:
    """Change-6 rules on Pinnacle's closing MAIN AH line (the only line in history)."""
    cap = model['training_cagey_p20']
    week_cut = test.groupby('week').corrected_p2.transform(lambda s: s.quantile(0.20))
    eligible = test[test.corrected_p2 <= np.minimum(week_cut, cap)]
    bets = []
    for record in eligible.itertuples():
        for side, line, odds in (('home', record.ah_line, record.ah_home_close),
                                 ('away', -record.ah_line, record.ah_away_close)):
            if line not in TIER_LINES or odds > TIER_MAX_ODDS:
                continue
            priced = nm.price_distribution(nm.MARGINS, record.corrected_probs, side, line)
            expected = (priced['p_win'] + priced['p_half_win'] / 2) * (odds - 1) - priced['p_loss'] - priced['p_half_loss'] / 2
            if expected + TOLERANCE < 0 or priced['p_no_loss'] + TOLERANCE < TIER_MIN_NO_LOSS:
                continue
            won, lost = settle(record.margin if side == 'home' else -record.margin, line)
            bets.append({'week': record.week, 'season': record.season, 'side': side, 'line': line, 'odds': odds,
                         'expected_profit': expected, 'corrected_no_loss': priced['p_no_loss'],
                         'profit': float(won * (odds - 1) - lost), 'won': won > 0, 'no_loss': lost == 0})
    frame = pd.DataFrame(bets)
    out = {'eligible_matches': int(len(eligible)), 'training_p20_cap': cap, 'bets': int(len(frame)),
           'label': 'LIMITED: history holds only Pinnacle\'s closing MAIN AH line, so most tier lines cannot be '
                    'simulated; Pinnacle close prices include its margin.'}
    if len(frame):
        out.update(hit_rate_win=float(frame.won.mean()), hit_rate_no_loss=float(frame.no_loss.mean()),
                   roi=interval(frame.profit, frame.week, n_boot), mean_odds=float(frame.odds.mean()),
                   by_line={f'{k:+g}': int(v) for k, v in frame.line.value_counts().sort_index().items()})
    return out


def outcome_rates(frame: pd.DataFrame) -> Dict[str, object]:
    out = {'matches': int(len(frame)), 'margin_2plus': float((frame.abs_margin >= 2).mean()) if len(frame) else None,
           'margin_3plus': float((frame.abs_margin >= 3).mean()) if len(frame) else None}
    for side in ('home', 'away'):
        margin = frame.margin if side == 'home' else -frame.margin
        for line in (1.5, 2.0):
            won, lost = settle(margin.to_numpy(), line)
            out[f'{side}_{line:+g}'] = ({'win': float(won.mean()), 'push': float(((won == 0) & (lost == 0)).mean()),
                                         'loss': float(lost.mean())} if len(frame) else None)
    return out


def identifier_comparison(frame: pd.DataFrame) -> Dict[str, Dict[str, object]]:
    periods = {'pre-2024 (in-sample for the model)': frame.date < nm.GATE_CUTOFF,
               '2024+ (test)': frame.date >= nm.GATE_CUTOFF,
               **{name: (frame.date >= nm.GATE_CUTOFF) & (frame.season == code) for name, code in TEST_SEASONS.items()}}
    out = {}
    for name, mask in periods.items():
        part = frame[mask]
        even = part[part.even_odds]
        cagiest = part.nsmallest(len(even), 'corrected_p2')
        both = part[part.match.isin(set(even.match) & set(cagiest.match))]
        out[name] = {'even_odds': outcome_rates(even), 'cagiest_same_count': outcome_rates(cagiest),
                     'overlap': outcome_rates(both), 'all': outcome_rates(part),
                     'overlap_share': float(len(both) / len(even)) if len(even) else None}
    return out


def evaluate(frame: pd.DataFrame, model, n_boot: int) -> Dict[str, object]:
    verify_gate_model(frame, model)
    data = apply_model(add_tags(frame), model)
    test = data[data.date >= nm.GATE_CUTOFF].copy()
    test['quintile'] = pd.qcut(test.corrected_p2.rank(method='first'), len(QUINTILES), labels=QUINTILES).astype(str)
    bets = bet_rows(test)
    seasons = {name: test[test.season == code] for name, code in TEST_SEASONS.items()}
    a = log_loss_gain(test, 2, n_boot)
    b = returns(bets, n_boot)
    c = {name: log_loss_gain(part, 2, n_boot) for name, part in seasons.items() if len(part)}
    return {
        'model_version': model['version'], 'training_matches': model['training_matches'],
        'training_dates': [model['training_first_date'], model['training_last_date']],
        'test_matches': int(len(test)), 'test_dates': [str(test.date.min().date()), str(test.date.max().date())],
        'gate': gate(a, b, c),
        'a_log_loss_gain_2plus': a, 'log_loss_gain_3plus': log_loss_gain(test, 3, n_boot),
        'b_returns_pooled': b,
        'b_returns_by_line': {f'{k:+g}': returns(g, n_boot) for k, g in bets.groupby('line')},
        'b_returns_by_quintile': {k: returns(g, n_boot) for k, g in bets.groupby('quintile')},
        'b_returns_by_tag': {t: returns(bets[bets[t]], n_boot) for t in TAGS},
        'c_by_season': {name: {'log_loss_gain_2plus': c[name], 'returns': returns(bets[bets.season == TEST_SEASONS[name]], n_boot),
                               'matches': int(len(seasons[name]))} for name in c},
        'predicted_vs_actual_2plus': {'uncorrected': float(test.matrix_p2.mean()), 'corrected': float(test.corrected_p2.mean()),
                                      'actual': float((test.abs_margin >= 2).mean())},
        'd_cagey_tier_simulation': tier_simulation(test, model, n_boot),
        'e_identifier_comparison': identifier_comparison(data),
    }


# ---------------------------------------------------------------------------
# Report
# ---------------------------------------------------------------------------

def _ci(m: Dict[str, float], scale: float = 1.0, fmt: str = '{:+.4f}') -> str:
    return f"{fmt.format(m['mean'] * scale)} [{fmt.format(m['low95'] * scale)}, {fmt.format(m['high95'] * scale)}] (n={m['n']})"


def gate_lines(summary: Dict[str, object]) -> List[str]:
    g, a, b = summary['gate'], summary['a_log_loss_gain_2plus'], summary['b_returns_pooled']
    lines = [f"**GATE: {'PASS' if g['pass'] else 'FAIL'}**", '',
             f"- (a) 2+ margin log-loss gain x1e-3: {_ci(a, 1000)} -> "
             f"{'PASS' if g['checks']['a_log_loss_gain_above_zero'] else 'FAIL'} (needs interval entirely above 0).",
             f"- (b) pooled +1..+2 return at CORRECTED fair price: {_ci(b['corrected'])} -> "
             f"{'PASS' if g['checks']['b_corrected_interval_contains_zero'] else 'FAIL'} (needs interval containing 0); "
             f"at UNCORRECTED fair price: {_ci(b['uncorrected'])} -> "
             f"{'PASS' if g['checks']['b_uncorrected_above_zero'] else 'FAIL'} (needs mean above 0).",
             '- (c) 2+ margin log-loss gain by test season x1e-3: ' + '; '.join(
                 f"{k} {_ci(v['log_loss_gain_2plus'], 1000)}" for k, v in summary['c_by_season'].items())
             + f" -> {'PASS' if g['checks']['c_no_season_significantly_worse'] else 'FAIL'} (no interval entirely below 0)."]
    if not g['pass']:
        lines += ['', 'Because the gate failed, the correction, the v28 value-tier change and the cagey tier ship '
                      'switched OFF; production stays v27.']
    return lines


def write_report(summary: Dict[str, object], path: Path) -> None:
    pv = summary['predicted_vs_actual_2plus']
    parts = ['# Cagey-match correction: pre-registered holdout gate', '',
             f"Model `{summary['model_version']}` trained on {summary['training_matches']} matches "
             f"{summary['training_dates'][0]}..{summary['training_dates'][1]} (Pinnacle close, 8 leagues); tested on "
             f"{summary['test_matches']} matches {summary['test_dates'][0]}..{summary['test_dates'][1]}. Nothing was tuned "
             'after seeing these results. Intervals resample whole gameweeks.', '', '## Gate', '']
    parts += gate_lines(summary)
    parts += ['', f"Test-period 2+ margin rate: uncorrected matrix {pv['uncorrected']:.3f}, corrected {pv['corrected']:.3f}, "
              f"actual {pv['actual']:.3f}. 3+ margin log-loss gain x1e-3 (not gated): "
              f"{_ci(summary['log_loss_gain_3plus'], 1000)}.", '',
              '## (b) Returns at the fair price, AH +1 to +2, both sides', '']
    rows = [['pooled', _ci(summary['b_returns_pooled']['corrected']), _ci(summary['b_returns_pooled']['uncorrected'])]]
    for group in ('b_returns_by_line', 'b_returns_by_quintile', 'b_returns_by_tag'):
        rows += [[k, _ci(v['corrected']), _ci(v['uncorrected'])] for k, v in summary[group].items()]
    parts.append(_table(['slice', 'corrected fair price', 'uncorrected fair price'], rows))
    parts += ['', '## (c) By test season', '',
              _table(['season', 'matches', '2+ log-loss gain x1e-3', 'corrected return', 'uncorrected return'],
                     [[k, v['matches'], _ci(v['log_loss_gain_2plus'], 1000), _ci(v['returns']['corrected']),
                       _ci(v['returns']['uncorrected'])] for k, v in summary['c_by_season'].items()])]
    d = summary['d_cagey_tier_simulation']
    parts += ['', '## (d) Cagey-tier simulation (reported, not gated)', '', d['label'], '',
              f"Eligible test matches (cagiest 20% per gameweek, capped at the training 20th percentile "
              f"{d['training_p20_cap']:.4f}): {d['eligible_matches']}. Qualifying bets at Pinnacle close: {d['bets']}."]
    if d['bets']:
        parts.append(f"Win rate {d['hit_rate_win']:.1%}, no-loss rate {d['hit_rate_no_loss']:.1%}, mean odds "
                     f"{d['mean_odds']:.2f}, ROI at Pinnacle close {_ci(d['roi'])}. Lines: {d['by_line']}.")
    parts += ['', '## (e) Identifier comparison (reported, not gated)', '',
              'even_odds = both Pinnacle closing 1X2 win odds >= 2.50; cagiest = the same number of matches with the '
              'lowest corrected_cagey_score. Pre-2024 is in-sample for the model.', '']
    rows = []
    for period, groups in summary['e_identifier_comparison'].items():
        for group in ('even_odds', 'cagiest_same_count', 'overlap', 'all'):
            r = groups[group]
            if not r['matches']:
                continue
            cells = [period, group, r['matches'], f"{r['margin_2plus']:.3f}", f"{r['margin_3plus']:.3f}"]
            cells += [f"{r[k]['win']:.3f}/{r[k]['push']:.3f}/{r[k]['loss']:.3f}" for k in ('home_+1.5', 'home_+2', 'away_+1.5', 'away_+2')]
            rows.append(cells)
    parts.append(_table(['period', 'group', 'matches', '2+ rate', '3+ rate', 'home +1.5 W/P/L', 'home +2 W/P/L',
                         'away +1.5 W/P/L', 'away +2 W/P/L'], rows))
    parts += ['', 'Overlap share (overlap / even_odds): ' + '; '.join(
        f"{k} {v['overlap_share']:.0%}" for k, v in summary['e_identifier_comparison'].items() if v['overlap_share'] is not None)]
    path.write_text('\n'.join(parts) + '\n', encoding='utf-8')


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('--cache-dir', default='.football_cache')
    parser.add_argument('--output-dir', default=str(OUTPUT_DIR))
    parser.add_argument('--workers', type=int, default=8)
    parser.add_argument('--bootstrap', type=int, default=2000)
    parser.add_argument('--model-dir', default=str(nm.MODEL_DIR))
    args = parser.parse_args(argv)
    frame = nm.build_dataset(Path(args.cache_dir), workers=args.workers)
    summary = evaluate(frame, nm.load(nm.GATE_VERSION, Path(args.model_dir)), args.bootstrap)
    out = Path(args.output_dir)
    out.mkdir(parents=True, exist_ok=True)
    (out / 'summary.json').write_text(json.dumps(summary, indent=2, default=_json_default), encoding='utf-8')
    write_report(summary, out / 'report.md')
    print('\n'.join(gate_lines(summary)))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
