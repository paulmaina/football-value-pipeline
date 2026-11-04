"""Narrow-margin probabilities for the fixtures in the current pipeline run.

Narrow = final goal margin of at most one goal (a draw or a one-goal win).
P(narrow) = 1 - corrected P(|margin| >= 2) from the cagey-correction model
(narrow_margin.py), fitted to Pinnacle 1X2, O/U 2.5 and main AH prices.

The run is resolved ONCE through the current-run pointer
(prediction_runs.resolve_raw) and every input is read from that bundle, so the
report can never mix two runs.

Fixtures are matched on fixture_id, else league + teams + kick-off (FixtureIndex);
ambiguous matches are reported, never guessed.

The forecast roster (all_leagues_predictions.csv) is the base: every forecast
fixture appears, scored or not, with an explicit reason when it is not.

For scored fixtures the report reruns the run's own code path on the same row
(price_edge_shortlist.pinnacle_quotes -> market_fit -> corrected_context, at the
run's evaluation time, with the run's model version), so:
  * P(draw) and P(one-goal win) are read from the corrected scoreline matrix;
  * the Pinnacle quotes shown are exactly the ones that fed the fit;
  * the recomputed corrected P(2+) must equal the monitoring record's value,
    otherwise the fixture is marked MISMATCH and no figures are shown.

Writes football_output_v2/readable/narrow_margin_report.csv and .md (the run
bundle is bound to its manifest, so nothing is added there).

Usage: python narrow_margin_report.py [--raw football_output_v2/raw] [--readable football_output_v2/readable]
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Dict, List, Mapping, Optional, Sequence, Tuple

import pandas as pd

MONITORING = 'cagey_correction_monitoring.csv'
PREDICTIONS = 'all_leagues_predictions.csv'
MANIFEST = 'run_manifest.json'
CSV_NAME = 'narrow_margin_report.csv'
MD_NAME = 'narrow_margin_report.md'
TRAINED_LEAGUES = {'Premier League', 'La Liga', 'Bundesliga', 'Serie A', 'Ligue 1', 'Eredivisie',
                   'Primeira Liga', 'Super Lig', 'Süper Lig'}
KEYS = ['league', 'home_team', 'away_team']
# Recomputed corrected P(2+) must match the monitoring record to this tolerance.
MATCH_TOLERANCE = 1e-9
QUOTES = ['pinnacle_home_odds', 'pinnacle_draw_odds', 'pinnacle_away_odds', 'pinnacle_over_2_5_odds',
          'pinnacle_under_2_5_odds', 'pinnacle_ah_main_line', 'pinnacle_ah_home_odds', 'pinnacle_ah_away_odds']
COLUMNS = ['kickoff_utc', 'fixture_id', 'league', 'home_team', 'away_team', 'status', 'exclusion_reason', 'fit',
           *QUOTES,
           'p_narrow', 'p_draw', 'p_one_goal', 'p_two_plus', 'p_three_plus', 'p_narrow_uncorrected',
           'corrected_cagey_quintile', 'latest_input_quote_utc', 'quote_age_at_run_min',
           'quote_age_at_kickoff_min', 'out_of_domain', 'generated_at_utc', 'model_version', 'run_directory']
NOT_MONITORED = 'NOT_MONITORED'
MISMATCH = 'MISMATCH'
AMBIGUOUS = 'AMBIGUOUS'
NO_MONITORING_FILE = 'no cagey monitoring file in this run (monitoring disabled or not written)'
NO_MONITORING_ROW = 'no cagey monitoring row for this fixture (not evaluated by the cagey correction)'


def _read_csv(path: Path) -> Optional[pd.DataFrame]:
    """None when the file is absent; an empty frame (columns kept if any) when it has no rows."""
    if not path.exists():
        return None
    try:
        return pd.read_csv(path, low_memory=False)
    except pd.errors.EmptyDataError:
        return pd.DataFrame()


def _run_generated_at(run: Path, monitoring: Optional[pd.DataFrame]) -> Optional[str]:
    manifest = run / MANIFEST
    if manifest.exists():
        return json.loads(manifest.read_bytes()).get('generated_at_utc')
    if monitoring is not None and 'generated_at_utc' in monitoring and monitoring['generated_at_utc'].notna().any():
        return str(monitoring['generated_at_utc'].dropna().iloc[0])
    return None


def _timing_rule(run: Path) -> Optional[str]:
    """The run's recorded quote timing rule (None for runs that record none: skew-5min-v1)."""
    import json
    path = run / 'conservative_bet_summary.json'
    try:
        return json.loads(path.read_text(encoding='utf-8')).get('quote_timing_rule') if path.exists() else None
    except (OSError, ValueError):
        return None


def _clean(value):
    """CSV-read cells to the objects the pipeline saw: NaN -> None (pinnacle_quotes treats None as absent)."""
    return None if isinstance(value, float) and math.isnan(value) else value


def _fixture_id(value) -> Optional[str]:
    value = _clean(value)
    return None if value is None or not str(value).strip() else str(value).strip()


def _kickoff(value) -> Optional[str]:
    """Kick-off normalised to a UTC ISO string, so '...Z' and '...+00:00' compare equal."""
    value = _clean(value)
    if value is None or not str(value).strip():
        return None
    try:
        return pd.Timestamp(value).tz_convert('UTC').isoformat() if pd.Timestamp(value).tzinfo else \
            pd.Timestamp(value).tz_localize('UTC').isoformat()
    except (ValueError, TypeError):
        return None


def _fallback_key(row: Mapping) -> Optional[tuple]:
    """League, teams and kick-off; None when any part is missing (then no fallback match is attempted)."""
    parts = [_clean(row.get(k)) for k in KEYS]
    kickoff = _kickoff(row.get('kickoff_utc'))
    return None if kickoff is None or any(p is None for p in parts) else (*parts, kickoff)


class FixtureIndex:
    """Matches fixtures: fixture_id when both sides have one; otherwise league + teams + kick-off.

    The kick-off fallback applies whenever either side lacks a fixture_id (in either direction). Two rows
    that both carry fixture_ids match only on equal ids, so conflicting ids are never joined. A query that
    hits more than one row is ambiguous and matches nothing; the caller reports it rather than guessing.
    """

    def __init__(self, rows: Sequence[Mapping]):
        self.rows = list(rows)
        self.ids = [_fixture_id(row.get('fixture_id')) for row in self.rows]
        self.by_id: Dict[str, List[int]] = {}
        self.by_fallback: Dict[tuple, List[int]] = {}
        for i, row in enumerate(self.rows):
            if self.ids[i] is not None:
                self.by_id.setdefault(self.ids[i], []).append(i)
            key = _fallback_key(row)
            if key is not None:
                self.by_fallback.setdefault(key, []).append(i)

    def candidates(self, row: Mapping) -> List[int]:
        fixture_id = _fixture_id(row.get('fixture_id'))
        if fixture_id is not None and fixture_id in self.by_id:
            return list(self.by_id[fixture_id])
        key = _fallback_key(row)
        hits = self.by_fallback.get(key, []) if key is not None else []
        # A query with an id may fall back only to rows without one; rows with another id conflict.
        return [i for i in hits if fixture_id is None or self.ids[i] is None]

    def match_all(self, queries: Sequence[Mapping]) -> List[Tuple[Optional[int], Optional[str]]]:
        """(row index, None) on a unique match; (None, reason) when ambiguous; (None, None) when no row matches.

        A row claimed by several queries matches none of them.
        """
        found = [self.candidates(q) for q in queries]
        claims: Dict[int, int] = {}
        for hits in found:
            if len(hits) == 1:
                claims[hits[0]] = claims.get(hits[0], 0) + 1
        out: List[Tuple[Optional[int], Optional[str]]] = []
        for hits in found:
            if len(hits) > 1:
                out.append((None, f'{len(hits)} monitoring rows match this fixture; not shown'))
            elif len(hits) == 1 and claims[hits[0]] > 1:
                out.append((None, f'its monitoring row also matches {claims[hits[0]] - 1} other forecast '
                                  'fixture(s); not shown'))
            else:
                out.append((hits[0] if hits else None, None))
        return out


def recompute(row: Mapping, evaluated_at: str, model_version: str, cutoff: bool = False) -> Optional[Dict[str, object]]:
    """Rerun the run's own fit and correction on one forecast row; None when no usable fit.

    `cutoff`: the run used observed-by-cutoff-v2, which excludes fits with inputs stamped after it."""
    import narrow_margin as nm
    import price_edge_cagey_shortlist as v28
    import price_edge_shortlist as v27
    row = {k: _clean(v) for k, v in row.items()}
    pin = v27.pinnacle_quotes(row)
    fit, fit_info = v27.market_fit(pin, pd.Timestamp(evaluated_at), cutoff)
    context = v28.corrected_context(pin, fit, fit_info, nm.load(model_version))
    if context is None:
        return None
    margins, corrected, raw = context['margins'], context['probs'], context['uncorrected_probs']
    line = pin['main_line']
    h2h, ou = pin['h2h'], pin['ou25']
    ah = pin['ah'].get(line) if line is not None else None
    return {'p_two_plus': float(context['score']),
            'p_three_plus': nm.margin_tail(margins, corrected, 3),
            'p_draw': float(corrected[margins == 0].sum()),
            'p_narrow_uncorrected': 1 - nm.margin_tail(margins, raw, 2),
            'pinnacle_home_odds': h2h[0], 'pinnacle_draw_odds': h2h[1], 'pinnacle_away_odds': h2h[2],
            'pinnacle_over_2_5_odds': ou[0], 'pinnacle_under_2_5_odds': ou[1],
            # The main AH line feeds fit B only; under fit A it is shown but not used.
            'pinnacle_ah_main_line': line, 'pinnacle_ah_home_odds': ah[0] if ah else None,
            'pinnacle_ah_away_odds': ah[1] if ah else None}


def build(raw: Path) -> pd.DataFrame:
    from prediction_runs import resolve_raw
    run = resolve_raw(Path(raw))  # once; both inputs come from this directory
    roster = _read_csv(run / PREDICTIONS)
    monitoring = _read_csv(run / MONITORING)
    generated = _run_generated_at(run, monitoring)
    cutoff = _timing_rule(run) == 'observed-by-cutoff-v2'
    if roster is None or roster.empty or not set(KEYS) <= set(roster.columns):
        return pd.DataFrame(columns=COLUMNS)
    # Every forecast row is kept (no de-duplication by team pairing: the same pairing can recur on another date).
    rows = [row for _, row in roster.iterrows()]
    records = ([m for _, m in monitoring.iterrows()] if monitoring is not None and not monitoring.empty else [])
    matches = FixtureIndex(records).match_all(rows)
    out = []
    for row, (index, ambiguity) in zip(rows, matches):
        rec = {c: None for c in COLUMNS}
        rec.update({k: _clean(row.get(k)) for k in ('kickoff_utc', 'fixture_id', *KEYS)},
                   generated_at_utc=generated, run_directory=str(run))
        if ambiguity is not None:
            rec.update(status=AMBIGUOUS, exclusion_reason=ambiguity)
            out.append(rec)
            continue
        m = records[index] if index is not None else None
        if m is None:
            rec.update(status=NOT_MONITORED, exclusion_reason=NO_MONITORING_FILE if monitoring is None
                       else NO_MONITORING_ROW)
            out.append(rec)
            continue
        rec.update(status=m['status'], exclusion_reason=_clean(m.get('exclusion_reason')) or None,
                   fit=_clean(m.get('fit')), model_version=m.get('model_version'),
                   corrected_cagey_quintile=_clean(m.get('corrected_cagey_quintile')),
                   latest_input_quote_utc=_clean(m.get('latest_input_quote_utc')),
                   generated_at_utc=m.get('generated_at_utc') or generated)
        if m['status'] == 'USABLE':
            figures = recompute(row.to_dict(), m['generated_at_utc'], m['model_version'], cutoff)
            if figures is None or abs(figures['p_two_plus'] - float(m['corrected_p2'])) > MATCH_TOLERANCE:
                got = 'no usable fit' if figures is None else f"P(2+) {figures['p_two_plus']:.6f}"
                rec.update(status=MISMATCH, exclusion_reason=f"recomputed {got} differs from monitoring "
                                                             f"P(2+) {float(m['corrected_p2']):.6f}; not shown")
            else:
                rec.update(figures)
                rec['p_narrow'] = 1 - figures['p_two_plus']
                rec['p_one_goal'] = rec['p_narrow'] - figures['p_draw']
        out.append(rec)
    frame = pd.DataFrame(out, columns=COLUMNS)
    stamp = pd.to_datetime(frame['latest_input_quote_utc'], utc=True)
    frame['quote_age_at_run_min'] = ((pd.to_datetime(frame['generated_at_utc'], utc=True) - stamp)
                                     .dt.total_seconds() / 60).round()
    frame['quote_age_at_kickoff_min'] = ((pd.to_datetime(frame['kickoff_utc'], utc=True) - stamp)
                                         .dt.total_seconds() / 60).round()
    frame['out_of_domain'] = ~frame['league'].isin(TRAINED_LEAGUES)
    scored = frame['p_narrow'].notna()
    frame = pd.concat([frame[scored].sort_values('p_narrow', ascending=False, kind='stable'),
                       frame[~scored].sort_values('kickoff_utc', kind='stable')])
    return frame.reindex(columns=COLUMNS).reset_index(drop=True)


# Columns another readable file (the cagey tier shortlist) can carry, keyed by raw name.
SHORTLIST_COLUMNS = {'p_narrow': 'P(narrow: draw or 1-goal win)', 'p_draw': 'P(draw)',
                     'p_one_goal': 'P(1-goal win)', 'p_three_plus': 'P(margin 3+)',
                     'out_of_domain': 'Out of training domain'}


def for_fixtures(fixtures: pd.DataFrame, raw: Path) -> pd.DataFrame:
    """Narrow-margin columns aligned row for row with `fixtures`, matched as FixtureIndex does
    (fixture_id first, else league + teams + kick-off).

    Rows with no unique scored match, or a run whose inputs are missing, get empty values; never raises for
    missing files.
    """
    empty = pd.DataFrame(index=fixtures.index, columns=list(SHORTLIST_COLUMNS), dtype=object)
    if fixtures.empty:
        return empty
    frame = build(Path(raw))
    scored = [r for _, r in frame[frame['p_narrow'].notna()].iterrows()]
    if not scored:
        return empty
    queries = [r for _, r in fixtures.iterrows()]
    out = empty.copy()
    for label, (index, _) in zip(fixtures.index, FixtureIndex(scored).match_all(queries)):
        if index is not None:
            out.loc[label] = [scored[index][c] for c in SHORTLIST_COLUMNS]
    return out


def _pct(value) -> str:
    return '' if pd.isna(value) else f'{value:.0%}'


def _odds(row, columns) -> str:
    values = [row[c] for c in columns]
    return '' if any(pd.isna(v) for v in values) else ' / '.join(f'{float(v):.2f}' for v in values)


def _ah(row) -> str:
    if pd.isna(row['pinnacle_ah_main_line']):
        return ''
    used = '' if row['fit'] == 'B' else ' (not used: fit A)'
    return f"{float(row['pinnacle_ah_main_line']):+.2f} @ {_odds(row, QUOTES[6:])}{used}"


def markdown(frame: pd.DataFrame) -> str:
    scored = frame[frame['p_narrow'].notna()]
    other = frame[frame['p_narrow'].isna()]
    generated = frame['generated_at_utc'].dropna()
    lines = ['# Narrow-margin report', '',
             f"Run {generated.iloc[0] if len(generated) else 'unknown'}. Narrow = draw or one-goal win. "
             'P(narrow) = 1 - corrected P(margin 2+); draw and one-goal split from the corrected scoreline matrix. '
             'Quotes are the Pinnacle prices that fed the fit. Uncertain probabilities, not predictions or '
             'betting advice.', '',
             'Out of domain = competition not in the training data (eight domestic leagues); '
             'treat those figures as less certain.', '',
             '| Kick-off (UTC) | League | Match | Pinnacle 1X2 | O/U 2.5 | Main AH (home) | P(narrow) | P(draw) '
             '| P(margin 3+) | Quintile | Quote age at kick-off (h) | Out of domain |',
             '| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |']
    for _, r in scored.iterrows():
        age = '' if pd.isna(r['quote_age_at_kickoff_min']) else f"{r['quote_age_at_kickoff_min'] / 60:.1f}"
        lines.append(f"| {r['kickoff_utc']} | {r['league']} | {r['home_team']} v {r['away_team']} "
                     f"| {_odds(r, QUOTES[:3])} | {_odds(r, QUOTES[3:5])} | {_ah(r)} | {_pct(r['p_narrow'])} "
                     f"| {_pct(r['p_draw'])} | {_pct(r['p_three_plus'])} | {r['corrected_cagey_quintile']} | {age} "
                     f"| {'yes' if r['out_of_domain'] else 'no'} |")
    if scored.empty:
        lines.append('| | | No fixture had a usable Pinnacle fit. | | | | | | | | | |')
    lines += ['', f'## Not scored ({len(other)})', '']
    for _, r in other.iterrows():
        lines.append(f"- {r['kickoff_utc']} {r['home_team']} v {r['away_team']} [{r['status']}]: "
                     f"{r['exclusion_reason']}")
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
    scored = int(frame['p_narrow'].notna().sum())
    mismatched = int(frame['status'].eq(MISMATCH).sum())
    print(f'Narrow-margin report: {scored} scored, {len(frame) - scored} not scored '
          f'({mismatched} mismatched) -> {args.readable}/{CSV_NAME}')
    if mismatched:
        # Information-only report: flag loudly, never fail the forecast publish.
        print(f'WARNING: {mismatched} fixture(s) could not be reproduced from the run bundle; see the report.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
