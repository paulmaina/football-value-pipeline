"""Re-rank stored forecasts with the current shortlist policy and UTC clock.

This does not fetch new odds or refit predictions. Run the full pipeline with
all six leagues for fresh forecasts and UCL historical validation.
"""
import argparse
from datetime import datetime, timezone
import json
from pathlib import Path

import pandas as pd

from conservative_bet_filter import build_conservative_shortlist, BALANCED_SELECTION_POLICY_VERSION
from format_football_output import process_conservative_shortlist


def refresh(root, as_of=None):
    root = Path(root)
    raw = root / 'raw'
    predictions = pd.read_csv(raw / 'all_leagues_predictions.csv')
    reliability = {}
    for path in sorted(raw.glob('*_goal_market_validation.json')):
        report = json.loads(path.read_text(encoding='utf-8'))
        reliability[report['league']] = report
    clock = as_of if as_of is not None else datetime.now(timezone.utc)
    picks, decisions, summary = build_conservative_shortlist(
        predictions, market_reliability=reliability, as_of=clock,
        selection_policy_version=BALANCED_SELECTION_POLICY_VERSION)
    summary['refresh_source'] = 'Stored forecasts re-ranked; no new odds or model fitting'
    summary['ucl_forecasts_available'] = bool(
        predictions.get('league', pd.Series(dtype=str)).eq('UEFA Champions League').any())
    summary['ucl_validation_available'] = 'UEFA Champions League' in reliability
    picks.to_csv(raw / 'conservative_bet_shortlist.csv', index=False)
    picks.loc[picks.selection_tier.eq('STRICT')].to_csv(
        raw / 'conservative_strict_qualifiers.csv', index=False)
    decisions.to_csv(raw / 'conservative_bet_rejections.csv', index=False)
    (raw / 'conservative_bet_summary.json').write_text(
        json.dumps(summary, indent=2), encoding='utf-8')
    (root / 'readable').mkdir(parents=True, exist_ok=True)
    process_conservative_shortlist(raw, root / 'readable')
    return summary


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path('football_output_v2'))
    args = parser.parse_args()
    summary = refresh(args.root)
    print(f"Selected {summary['n_shortlisted']} matches; cutoff {summary['shortlist_window_end_utc']}")
    if not summary['ucl_forecasts_available']:
        print('No UCL forecasts in stored inputs. Run the full pipeline with --leagues EPL LaLiga Bundesliga SerieA Ligue1 UCL.')
    elif not summary['ucl_validation_available']:
        print('UCL forecasts lack historical validation. Run the full six-league pipeline to reassess them.')


if __name__ == '__main__':
    main()
