"""Narrow-margin probabilities for the fixtures in the latest pipeline run.

Narrow = final goal margin of at most one goal (a draw or a one-goal win).
P(narrow) = 1 - corrected P(|margin| >= 2) from the production cagey-correction
model (narrow_margin.py), which is fitted to Pinnacle 1X2, O/U 2.5 and main AH
prices. Nothing here is refitted; this only reads the run outputs.

Also reports:
  * P(draw) and P(exactly one goal), splitting the narrow class by the
    Pinnacle no-vig draw share (the correction keeps the class's shape);
  * Pinnacle quote age at the run time and at kick-off (deterministic: no wall clock);
  * an out-of-domain flag for competitions the model was never trained on
    (it was trained on eight domestic leagues only).

Writes football_output_v2/readable/narrow_margin_report.csv and .md (raw/ is
bound to the run manifest, so nothing is added there).

Usage: python narrow_margin_report.py [--raw football_output_v2/raw] [--readable football_output_v2/readable]
"""
from __future__ import annotations

import argparse
from pathlib import Path
from typing import Optional, Sequence

import pandas as pd

MONITORING = 'cagey_correction_monitoring.csv'
PREDICTIONS = 'all_leagues_predictions.csv'
CSV_NAME = 'narrow_margin_report.csv'
MD_NAME = 'narrow_margin_report.md'
TRAINED_LEAGUES = {'Premier League', 'La Liga', 'Bundesliga', 'Serie A', 'Ligue 1', 'Eredivisie',
                   'Primeira Liga', 'Super Lig', 'Süper Lig'}
KEYS = ['league', 'home_team', 'away_team']
ODDS = ['market_reference_home_odds', 'market_reference_draw_odds', 'market_reference_away_odds',
        'market_reference_over_2_5_odds', 'market_reference_under_2_5_odds']
COLUMNS = ['kickoff_utc', 'league', 'home_team', 'away_team', 'status', 'exclusion_reason', *ODDS,
           'p_narrow', 'p_draw', 'p_one_goal', 'p_two_plus', 'p_three_plus', 'p_narrow_uncorrected',
           'corrected_cagey_quintile', 'latest_input_quote_utc', 'quote_age_at_run_min',
           'quote_age_at_kickoff_min', 'out_of_domain', 'generated_at_utc', 'model_version']


def build(raw: Path) -> pd.DataFrame:
    mon = pd.read_csv(raw / MONITORING)
    if mon.empty:
        return pd.DataFrame(columns=COLUMNS)
    pred = pd.read_csv(raw / PREDICTIONS, low_memory=False)
    pred = pred.reindex(columns=KEYS + ODDS).drop_duplicates(KEYS)
    frame = mon.merge(pred, on=KEYS, how='left', validate='one_to_one')
    inv = 1 / frame[ODDS[:3]].astype(float)
    novig = inv.div(inv.sum(axis=1), axis=0)
    frame['p_narrow'] = 1 - frame['corrected_p2']
    frame['p_narrow_uncorrected'] = 1 - frame['uncorrected_p2']
    # The correction rescales the {|m| <= 1} class as a whole, so the draw keeps its share of it.
    frame['p_draw'] = novig[ODDS[1]] * frame['p_narrow'] / frame['p_narrow_uncorrected']
    frame['p_one_goal'] = frame['p_narrow'] - frame['p_draw']
    frame['p_two_plus'] = frame['corrected_p2']
    frame['p_three_plus'] = frame['corrected_p3']
    stamp = pd.to_datetime(frame['latest_input_quote_utc'], utc=True)
    run = pd.to_datetime(frame['generated_at_utc'], utc=True)
    kickoff = pd.to_datetime(frame['kickoff_utc'], utc=True)
    frame['quote_age_at_run_min'] = ((run - stamp).dt.total_seconds() / 60).round()
    frame['quote_age_at_kickoff_min'] = ((kickoff - stamp).dt.total_seconds() / 60).round()
    frame['out_of_domain'] = ~frame['league'].isin(TRAINED_LEAGUES)
    usable = frame['status'].eq('USABLE')
    frame = pd.concat([frame[usable].sort_values('p_narrow', ascending=False, kind='stable'),
                       frame[~usable].sort_values('kickoff_utc', kind='stable')])
    return frame.reindex(columns=COLUMNS).reset_index(drop=True)


# Columns another readable file (the cagey tier shortlist) can carry, keyed by raw name.
SHORTLIST_COLUMNS = {'p_narrow': 'P(narrow: draw or 1-goal win)', 'p_draw': 'P(draw)',
                     'p_one_goal': 'P(1-goal win)', 'p_three_plus': 'P(margin 3+)',
                     'out_of_domain': 'Out of training domain'}


def for_fixtures(fixtures: pd.DataFrame, raw: Path) -> pd.DataFrame:
    """Narrow-margin columns aligned row for row with `fixtures` (matched on league, home, away).

    Rows with no match, or a run whose inputs are missing, get empty values; never raises for missing files.
    """
    empty = pd.DataFrame(index=fixtures.index, columns=list(SHORTLIST_COLUMNS), dtype=object)
    if fixtures.empty or not set(KEYS) <= set(fixtures.columns):
        return empty
    try:
        frame = build(Path(raw))
    except (FileNotFoundError, pd.errors.EmptyDataError):
        return empty
    lookup = frame[frame['status'].eq('USABLE')].drop_duplicates(KEYS).set_index(KEYS)[list(SHORTLIST_COLUMNS)]
    keys = pd.MultiIndex.from_frame(fixtures[KEYS].astype(object))
    return lookup.reindex(keys).set_axis(fixtures.index)


def _pct(value) -> str:
    return '' if pd.isna(value) else f'{value:.0%}'


def _odds(row, columns) -> str:
    values = [row[c] for c in columns]
    return '' if any(pd.isna(v) for v in values) else ' / '.join(f'{float(v):.2f}' for v in values)


def markdown(frame: pd.DataFrame) -> str:
    usable = frame[frame['status'].eq('USABLE')]
    excluded = frame[~frame['status'].eq('USABLE')]
    generated = frame['generated_at_utc'].dropna()
    lines = ['# Narrow-margin report', '',
             f"Run {generated.iloc[0] if len(generated) else 'unknown'}. Narrow = draw or one-goal win. "
             'P(narrow) = 1 - corrected P(margin 2+) from Pinnacle 1X2, O/U 2.5 and main AH prices. '
             'Uncertain probabilities, not predictions or betting advice.', '',
             'Out of domain = competition not in the training data (eight domestic leagues); '
             'treat those figures as less certain.', '',
             '| Kick-off (UTC) | League | Match | Pinnacle 1X2 | O/U 2.5 | P(narrow) | P(draw) | P(margin 3+) '
             '| Quintile | Quote age at kick-off (h) | Out of domain |',
             '| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |']
    for _, r in usable.iterrows():
        age = '' if pd.isna(r['quote_age_at_kickoff_min']) else f"{r['quote_age_at_kickoff_min'] / 60:.1f}"
        lines.append(f"| {r['kickoff_utc']} | {r['league']} | {r['home_team']} v {r['away_team']} "
                     f"| {_odds(r, ODDS[:3])} | {_odds(r, ODDS[3:])} | {_pct(r['p_narrow'])} | {_pct(r['p_draw'])} "
                     f"| {_pct(r['p_three_plus'])} | {r['corrected_cagey_quintile']} | {age} "
                     f"| {'yes' if r['out_of_domain'] else 'no'} |")
    if usable.empty:
        lines.append('| | | No fixture had a usable Pinnacle fit. | | | | | | | | |')
    lines += ['', f'## Not scored ({len(excluded)})', '']
    for _, r in excluded.iterrows():
        lines.append(f"- {r['kickoff_utc']} {r['home_team']} v {r['away_team']}: {r['exclusion_reason']}")
    return '\n'.join(lines) + '\n'


def write(raw: Path, readable: Path) -> pd.DataFrame:
    frame = build(raw)
    readable.mkdir(parents=True, exist_ok=True)
    frame.to_csv(readable / CSV_NAME, index=False)
    (readable / MD_NAME).write_text(markdown(frame), encoding='utf-8')
    return frame


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('--raw', default='football_output_v2/raw')
    parser.add_argument('--readable', default='football_output_v2/readable')
    args = parser.parse_args(argv)
    frame = write(Path(args.raw), Path(args.readable))
    usable = int(frame['status'].eq('USABLE').sum())
    print(f'Narrow-margin report: {usable} scored, {len(frame) - usable} not scored -> {args.readable}/{CSV_NAME}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
