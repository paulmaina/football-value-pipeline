"""Master shortlist and immutable legacy replay.

Live research runs use master-profit-15-pinnacle-markets-v9. The source
shortlist union supplies native Pinnacle Asian Handicap, win and 1X/X2
offers for fifteen distinct fixtures, ranked by market profit probability.
The master keeps the original offered price and shows frozen context for review.
"""

import io
import json
import math
from pathlib import Path
from typing import Dict, List, Mapping, Optional

import numpy as np
import pandas as pd

import shortlist_window

VERSION_V1 = 'master-10-v1'
VERSION = 'master-10-v2'
VERSION_MARKET = 'master-profit-market-v5'
VERSION_AH = 'master-profit-no-dc-v6'
VERSION_NO_TOTALS = 'master-profit-no-dc-no-over15-v7'
VERSION_CONTEXT = 'master-profit-15-context-v8'
VERSION_PINNACLE_MARKETS = 'master-profit-15-pinnacle-markets-v9'
CONTEXT_VERSIONS = (VERSION_CONTEXT, VERSION_PINNACLE_MARKETS)
MARKET_VERSIONS = (VERSION_MARKET, VERSION_AH, VERSION_NO_TOTALS, *CONTEXT_VERSIONS)
VERSIONS = (VERSION_V1, VERSION, *MARKET_VERSIONS)
BASIS_PINNACLE = 'Pinnacle fair price'
BASIS_FIT = 'market-implied fit B'
BASIS_CORRECTED = 'cagey-corrected fit'
BASIS_UNAVAILABLE = 'unavailable'


def _flag_true(value) -> bool:
    return value is True or str(value).strip().lower() in ('true', '1')


def basis(row: Mapping) -> str:
    """Where a candidate's ranking no-loss probability came from (see the module docstring)."""
    if row.get('reference_type') == 'c-cagey':
        return BASIS_CORRECTED
    if row.get('reference_type') == 'c':
        return BASIS_FIT  # priced from fit B, which exists only when usable
    if row.get('market') != 'Over 1.5' and _flag_true(row.get('fit_usable')):
        return BASIS_FIT
    return BASIS_PINNACLE
FILE = 'master_shortlist.csv'
SIZE = 10
MIN_EDGE = 0.01
TOLERANCE = 1e-9
PRICE_VALUE = 'value'
PRICE_BELOW_THRESHOLD = 'below value threshold'
COST_REASON = 'expected profit after stake cost below 0'
NOT_SELECTED_PREFIX = 'other qualifying line chosen for this fixture'
COLUMNS = ['master_rank', 'kickoff_utc', 'league', 'home_team', 'away_team', 'fixture_id', 'market_to_bet',
           'market', 'value_market_group', 'handicap_side', 'handicap_line', 'bookmaker', 'offered_decimal_odds',
           'fair_odds', 'minimum_odds_master', 'edge', 'reference_type', 'master_no_loss_probability',
           'master_price_flag', 'p_narrow', 'in_value_shortlist', 'in_cagey_tier', 'per_stake_cost',
           'offered_last_update_utc', 'pinnacle_last_update_utc', 'evaluated_at_utc', 'selection_policy_version',
           'master_version']
COLUMNS_V1 = COLUMNS
# v2: the event the price belongs to (closing-price lookups bind to it) and the ranking basis.
COLUMNS_V2 = [*COLUMNS[:COLUMNS.index('fixture_id') + 1], 'odds_event_id',
              *COLUMNS[COLUMNS.index('fixture_id') + 1:COLUMNS.index('master_no_loss_probability') + 1],
              'master_probability_basis', *COLUMNS[COLUMNS.index('master_no_loss_probability') + 1:]]
from master_selection import EXTRA_COLUMNS
COLUMNS_V3 = [*COLUMNS_V2, *EXTRA_COLUMNS]
from master_selection_ah import EXTRA_COLUMNS as AH_COLUMNS
COLUMNS_AH = [*COLUMNS_V3, *AH_COLUMNS]
from master_context_review import COLUMNS as CONTEXT_COLUMNS
COLUMNS_CONTEXT = [*COLUMNS_AH, *CONTEXT_COLUMNS]
COLUMNS = COLUMNS_V2  # legacy schema; columns(version) supplies each recorded version


CONFIG = Path(__file__).with_name('master_shortlist_config.json')


def selection_module(version):
    if version == VERSION_PINNACLE_MARKETS:
        import master_selection_pinnacle_markets
        return master_selection_pinnacle_markets
    if version == VERSION_CONTEXT:
        import master_selection_fifteen
        return master_selection_fifteen
    if version == VERSION_NO_TOTALS:
        import master_selection_no_totals
        return master_selection_no_totals
    if version == VERSION_AH:
        import master_selection_ah
        return master_selection_ah
    if version == VERSION_MARKET:
        import master_selection
        return master_selection
    raise ValueError(f'No market selector for {version!r}')


def configured_version():
    """Live generation is explicit; archived replay never reads this config."""
    config = json.loads(CONFIG.read_text(encoding='utf-8'))
    if not isinstance(config, dict) or config.get('version') not in VERSIONS:
        raise ValueError('Unknown configured master shortlist version')
    return config['version']


def columns(version: str = VERSION) -> List[str]:
    if version not in VERSIONS:
        raise ValueError(f'Unknown master shortlist version {version!r}')
    if version in CONTEXT_VERSIONS:
        return COLUMNS_CONTEXT
    if version in (VERSION_AH, VERSION_NO_TOTALS):
        return COLUMNS_AH
    if version == VERSION_MARKET:
        return COLUMNS_V3
    return COLUMNS_V2 if version == VERSION else COLUMNS_V1


def _reasons(text) -> List[str]:
    return [r for r in str(text or '').split('; ') if r and r != 'nan']


def price_only(reasons: List[str]) -> bool:
    """True when every rejection reason is about the price, never about the data."""
    return all(r.startswith('edge below ') or r == COST_REASON or r.startswith(NOT_SELECTED_PREFIX) for r in reasons)


def _number(series: pd.Series) -> pd.Series:
    return pd.to_numeric(series, errors='coerce')


def pool(decisions: pd.DataFrame, version: str = VERSION) -> pd.DataFrame:
    """Candidates that passed the data checks, with their value flag and safety."""
    if decisions is None or decisions.empty:
        return pd.DataFrame()
    frame = decisions.copy()
    # Master keeps its existing price-edge pool while the main shortlist can
    # independently qualify by team-research profit probability.
    if 'price_edge_rejection_reasons' in frame:
        frame['rejection_reasons'] = frame['price_edge_rejection_reasons']
    price, edge = _number(frame.get('offered_decimal_odds')), _number(frame.get('edge'))
    reasons = frame.get('rejection_reasons', pd.Series('', index=frame.index)).map(_reasons)
    usable = price.notna() & edge.notna() & frame.get('reference_type').notna() & reasons.map(price_only)
    frame = frame.loc[usable].copy()
    if frame.empty:
        return frame
    reasons = reasons.loc[frame.index]
    value = (_number(frame.edge) + TOLERANCE >= MIN_EDGE) & ~reasons.map(lambda r: COST_REASON in r)
    frame['master_price_flag'] = np.where(value, PRICE_VALUE, PRICE_BELOW_THRESHOLD)
    pinnacle = _number(frame.get('pinnacle_no_loss_probability'))
    corrected = _number(frame['corrected_no_loss_probability']) if 'corrected_no_loss_probability' in frame \
        else pd.Series(np.nan, index=frame.index)
    if version == VERSION_V1:
        frame['master_no_loss_probability'] = pinnacle.fillna(corrected)
        return frame
    cagey = frame.reference_type.eq('c-cagey')
    safety = corrected.where(cagey, pinnacle)
    frame['master_no_loss_probability'] = safety
    labels = pd.Series([basis(r) for r in frame.to_dict('records')], index=frame.index, dtype=object)
    frame['master_probability_basis'] = labels.where(safety.notna(), BASIS_UNAVAILABLE)
    return frame


def _order(frame: pd.DataFrame) -> pd.DataFrame:
    """Value bets first, safest first (then edge); below-threshold fill next, closest to fair first (then safest).

    Odds descending and stable keys break any remaining ties deterministically.
    """
    value = frame.master_price_flag == PRICE_VALUE
    safe = frame.master_no_loss_probability.astype(float).fillna(-1.0)
    edge = _number(frame.edge)
    return frame.assign(
        _value=value.astype(int), _first=np.where(value, safe, edge), _second=np.where(value, edge, safe),
        _odds=_number(frame.offered_decimal_odds),
    ).sort_values(['_value', '_first', '_second', '_odds', 'kickoff_utc', 'market', 'bookmaker'],
                  ascending=[False, False, False, False, True, True, True], kind='stable')


def _event_ids(predictions: Optional[pd.DataFrame]) -> Dict[tuple, str]:
    from performance_tracking import fixture_key, utc
    if predictions is None or not len(predictions) or 'odds_event_id' not in predictions:
        return {}
    events = {}
    for row in predictions.astype(object).where(predictions.notna(), None).to_dict('records'):
        event = str(row.get('odds_event_id') or '').strip()
        if event:
            events[(fixture_key(row), utc(row.get('kickoff_utc')))] = event
    return events


def build(decisions: pd.DataFrame, predictions: Optional[pd.DataFrame] = None, version: str = None, *,
          execution_policy: Optional[Mapping] = None) -> pd.DataFrame:
    """The master shortlist of one run (empty frame with the version's columns when nothing qualifies).

    `predictions` (the run's forecasts) supplies each pick's odds event id under v2.
    """
    if execution_policy is not None:
        from quote_policy import policy_scope
        with policy_scope(execution_policy):
            return build(decisions, predictions, version)
    from performance_tracking import fixture_key, utc
    if version is None:
        version = VERSION  # historical API default; live writes use the explicit config
    if version in MARKET_VERSIONS:
        module = selection_module(version)
        return module.select(module.evaluate(decisions, predictions))
    wanted = columns(version)
    candidates = pool(decisions, version)
    if candidates.empty:
        return pd.DataFrame(columns=wanted)
    candidates['_fixture'] = candidates.apply(fixture_key, axis=1)
    best = _order(candidates).drop_duplicates('_fixture')
    top = _order(best).head(SIZE).copy()
    fair = _number(top.fair_odds)
    score = _number(top.get('corrected_cagey_score', pd.Series(np.nan, index=top.index)))
    top['master_rank'] = range(1, len(top) + 1)
    top['minimum_odds_master'] = fair * (1 + MIN_EDGE)
    top['p_narrow'] = 1 - score
    top['in_value_shortlist'] = top.get('decision', pd.Series(index=top.index, dtype=object)).eq('SHORTLISTED')
    top['in_cagey_tier'] = top.get('cagey_tier_decision', pd.Series(index=top.index, dtype=object)).eq('SHORTLISTED')
    top['master_version'] = version
    if version == VERSION:
        events = _event_ids(predictions)
        top['odds_event_id'] = [events.get((fixture_key(r), utc(r.get('kickoff_utc'))))
                                for r in top.to_dict('records')]
    return top.reindex(columns=wanted).reset_index(drop=True)


def summary(frame: pd.DataFrame, version: str = None) -> Dict[str, object]:
    if version is None:
        version = str(frame.master_version.iloc[0]) if len(frame) else frame.attrs.get('master_version', VERSION)
    if version in MARKET_VERSIONS:
        return selection_module(version).summary(frame)
    flags = frame['master_price_flag'] if len(frame) else pd.Series(dtype=object)
    extra = {} if version == VERSION_V1 else {
        'probability_basis': 'no-loss probability labelled by its source: cagey-corrected fit (c-cagey), '
                             'market-implied fit B (whenever usable), else the Pinnacle fair win share (half '
                             'lines and over 1.5 only); none -> ranked last'}
    return {'version': version, 'size': SIZE, 'n_bets': int(len(frame)),
            'value_bets': int((flags == PRICE_VALUE).sum()),
            'below_threshold_bets': int((flags == PRICE_BELOW_THRESHOLD).sum()),
            'min_edge_for_value': MIN_EDGE,
            'rule': 'the run\'s evaluated candidates that passed the data checks (a candidate may fail only on price); '
                    'one per match: value bets (edge >= 1% vs their fair reference) first, safest first; then '
                    'below-value-threshold bets (edge under 1%, possibly still positive) closest to fair price '
                    'first; first 10 matches; fewer only when fewer matches qualify', **extra}


def _as_csv(frame: pd.DataFrame) -> pd.DataFrame:
    """The frame as the CSV file holds it, so written and replayed lists compare like for like."""
    buffer = io.StringIO()
    frame.to_csv(buffer, index=False)
    buffer.seek(0)
    try:
        return pd.read_csv(buffer, low_memory=False)
    except pd.errors.EmptyDataError:
        return pd.DataFrame(columns=list(frame.columns))


def _same(got, want) -> bool:
    numeric = (int, float, np.integer, np.floating)
    if isinstance(want, numeric) and not isinstance(want, (bool, np.bool_)):
        if not isinstance(got, numeric) or isinstance(got, (bool, np.bool_)):
            return False
        if math.isnan(want) or math.isnan(got):
            return math.isnan(want) and math.isnan(got)
        return math.isclose(float(got), float(want), abs_tol=1e-7, rel_tol=1e-8)
    if isinstance(want, float) and math.isnan(want):
        return isinstance(got, float) and math.isnan(got)
    return type(got) is type(want) and got == want


def matches(frame: pd.DataFrame, expected: pd.DataFrame, version: str = None) -> bool:
    """The written list carries exactly the replayed one: the full schema, every field.

    Text, flags, identities, timestamps and booleans must be identical; numbers
    (prices, fair odds, edge, probabilities, line, stake cost) agree within
    max(1e-7 absolute, 1e-8 relative), the solver tolerance used elsewhere.
    """
    if version is None:
        recorded = expected.get('master_version', pd.Series(dtype=str)).dropna()
        version = (recorded.iloc[0] if len(recorded) else expected.attrs.get('master_version'))
        version = version or (VERSION_AH if 'master_replacement_status' in expected else VERSION_MARKET if 'master_profit_probability' in expected else VERSION)
    wanted = columns(version)
    if list(frame.columns) != wanted:
        return False
    left, right = _as_csv(frame), _as_csv(expected.reindex(columns=wanted))
    if len(left) != len(right) or list(left.columns) != list(right.columns):
        return False
    for column in wanted:
        for got, want in zip(left[column].astype(object), right[column].astype(object)):
            if not _same(got, want):
                return False
    return True


def write(decisions: pd.DataFrame, out_dir, run_summary: Mapping,
          predictions: Optional[pd.DataFrame] = None, *, version: Optional[str] = None) -> pd.DataFrame:
    """Write FILE and record the master summary in the run summary (mutates `run_summary`)."""
    if version is None:
        version = configured_version()
    columns(version)  # reject unknown versions before writing any output
    if version in MARKET_VERSIONS:
        from master_selection import require_generation_clock
        module = selection_module(version)
        clock = require_generation_clock(decisions, run_summary.get('generated_at_utc'))
        from quote_policy import policy_scope, load_policy
        lookahead = run_summary.get('shortlist_lookahead_hours', shortlist_window.LEGACY_HOURS)
        with shortlist_window.scope(lookahead), policy_scope(run_summary.get('quote_execution_policy') or load_policy()):
            audit = module.evaluate(decisions, predictions, clock)
            frame = module.select(audit)
        audit.to_csv(Path(out_dir)/module.AUDIT_FILE, index=False)
    else:
        from master_selection import AUDIT_FILE
        frame = build(decisions, predictions, version)
        (Path(out_dir)/AUDIT_FILE).unlink(missing_ok=True)
    frame.to_csv(Path(out_dir) / FILE, index=False)
    with shortlist_window.scope(run_summary.get('shortlist_lookahead_hours', shortlist_window.LEGACY_HOURS)):
        run_summary['master_shortlist'] = summary(frame, version)
    return frame


def refresh(decisions: pd.DataFrame, out_dir, run_summary: Mapping, predictions: Optional[pd.DataFrame] = None):
    """Write the master list for a v28 run; otherwise remove any copy seeded from an earlier run.

    Used by both the full forecast and the stored-forecast refresh so neither can
    publish a master list that is missing or belongs to a previous run.
    """
    from price_edge_cagey_shortlist import POLICY
    if run_summary.get('selection_policy_version') == POLICY:
        frame = write(decisions, out_dir, run_summary, predictions)
        shadow(decisions, out_dir, frame, run_summary.get('generated_at_utc'), predictions)
        return frame
    from master_selection import AUDIT_FILE
    (Path(out_dir) / AUDIT_FILE).unlink(missing_ok=True)
    (Path(out_dir) / FILE).unlink(missing_ok=True)
    run_summary.pop('master_shortlist', None)
    shadow(None, out_dir)
    return None


def shadow(decisions, out_dir, live=None, generated_at_utc=None, predictions=None) -> None:
    """The new master (Phase 4, revised master rule), in shadow: master_shortlist_new.csv and its summary beside
    FILE, written after it from the same decision rows.

    It never changes FILE, the run summary or any decision, and a failure here only warns.
    """
    import warnings
    import master_reconciliation
    try:
        if decisions is None:
            master_reconciliation.remove_shadow(out_dir)
        else:
            master_reconciliation.write_shadow(decisions, out_dir, live, generated_at_utc, predictions)
    except Exception as exc:  # shadow output must never break or alter the live run
        warnings.warn(f'New master shadow skipped ({type(exc).__name__}: {exc})')
        try:
            master_reconciliation.remove_shadow(out_dir)
        except Exception:
            pass
