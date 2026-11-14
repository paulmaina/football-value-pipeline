"""Historical record for the "research strongly disagrees" inspection flag (master_inspection.py).

Reads the fill rule's offline backtest picks (evaluation/master_new_fill/backtest_picks.csv: development, validation
and retrospective periods only; no holdout) and writes evaluation/master_release/inspection_history.json:

- the flag itself (research no-loss chance at least 8 points below the cagey tier's, cagey >= 0.85): how many
  backtest offers reached it (none did: the cagey tier never rated a backtest offer that safe);
- the closest comparable bets: safe picks (cagey >= 0.75) on which research was at least 8 points more pessimistic.
  How often they avoided defeat (a win, half win or push), against the average no-loss chance the cagey tier (and the
  research view) gave them.

Descriptive only: it never changes a pick, a probability or a ranking.

    python scripts/inspection_history.py
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import pandas as pd

REPO = Path(__file__).resolve().parents[1]
SOURCE = REPO / 'evaluation' / 'master_new_fill' / 'backtest_picks.csv'
OUTPUT = REPO / 'evaluation' / 'master_release' / 'inspection_history.json'
PHASES = ('development', 'validation', 'retrospective')


def record(frame: pd.DataFrame) -> dict:
    if frame.empty:
        return {'bets': 0}
    return {'bets': int(len(frame)), 'avoided_defeat': float(frame.observed_no_loss.mean()),
            'cagey_predicted': float(frame.cagey_no_loss_probability.mean()),
            'research_predicted': float(frame.research_no_loss_probability.mean()),
            'first_kickoff_utc': str(frame.kickoff_utc.min()), 'last_kickoff_utc': str(frame.kickoff_utc.max())}


def build(source: Path = SOURCE) -> dict:
    import master_reconciliation as mr
    config = mr.load_config()
    flag = config['inspection_flag']
    safe = config['inclusion']['min_cagey_no_loss']
    picks = pd.read_csv(source, low_memory=False)
    picks = picks.loc[picks.phase.isin(PHASES) & picks.gap_points.notna() & picks.observed_no_loss.notna()]
    gap = picks.gap_points <= flag['max_gap_points'] + mr.TOLERANCE
    flagged = picks.loc[gap & (picks.cagey_no_loss_probability + mr.TOLERANCE >= flag['min_cagey_no_loss'])]
    comparable = picks.loc[gap & (picks.cagey_no_loss_probability + mr.TOLERANCE >= safe)]
    return {
        'source': str(source.relative_to(REPO)).replace('\\', '/'), 'phases': list(PHASES),
        'rule': flag['rule'],
        'flag': {**record(flagged), 'max_cagey_no_loss_in_backtest': float(picks.cagey_no_loss_probability.max())},
        'comparable': {
            'definition': f"safe picks (cagey no-loss >= {safe:.2f}) on which the research view's no-loss chance "
                          f"was at least {-flag['max_gap_points']:.0f} points below the cagey tier's",
            **record(comparable),
            'by_phase': {phase: record(comparable.loc[comparable.phase.eq(phase)]) for phase in PHASES}},
        'note': 'Offline backtest offers (Bet365 prices with a synthetic Pinnacle margin where Pinnacle is missing); '
                'descriptive only, never used to change a pick or a ranking.'}


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    parser.add_argument('--output', type=Path, default=OUTPUT)
    args = parser.parse_args(argv)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(build(), indent=2) + '\n', encoding='utf-8')
    print(args.output)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
