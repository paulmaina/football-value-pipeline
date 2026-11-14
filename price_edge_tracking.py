"""Forward tracking for production policy v27 (AH price edge vs Pinnacle).

1. Grades every frozen v27 pick by closing line value against Pinnacle's
   near-kickoff price on the same AH line (the closing-odds workflow already
   collects it): clv = entry odds x Pinnacle fair close win-share - 1, with
   the two-way margin removed proportionally, as in the selection rule.
   Splits: bookmaker, odds band, reference type, favourite/underdog side and
   each narrow-margin tag (balanced, low_total, high_draw, even_odds, any tag, no tag).
2. Records every TAGGED candidate, picked or rejected, with the offered price
   vs fair at capture and the final result, so the narrow-margin hypothesis
   is measured forward even when no pick is made.

A STOP REVIEW flag is raised when at least 100 graded picks have mean CLV
below zero. v26 and older history is untouched. Evidence only: nothing here
changes forecasts, selection or stakes.

v28 adds the cagey tier (its own frozen list, cagey_tier_shortlist.csv) and
the cagey correction. Both tiers are graded by CLV and realised profit, split
by tier, policy, bookmaker, reference type (a, b, c, c-cagey), corrected
cagey-score quintile, each tag and "qualified only because of correction".
  * CAGEY REVIEW: >= 50 graded correction-only value picks with mean CLV < 0;
  * CAGEY TIER REVIEW: >= 50 graded cagey-tier picks whose realised ROI 95%
    interval is entirely below 0.
Each flag recommends switching its feature off; it never switches anything off.

Correction monitoring (v28) grades, per fixture, the first eligible pre-kickoff
record of the correction this run computed (cagey_correction_monitoring.csv):
2+/3+ margin rates by fixed quintile, corrected vs uncorrected log loss with a
paired gain, and returns at both fair prices (a calibration diagnostic, not
bookmaker ROI). CORRECTION REVIEW: >= 200 graded fixtures whose paired 2+
log-loss gain interval is entirely below 0; it recommends review only.
"""
from __future__ import annotations

import math
from datetime import timedelta
from pathlib import Path
from typing import Dict, List, Optional

import numpy as np
import pandas as pd

from price_edge_shortlist import POLICY, TAGS
from price_edge_cagey_shortlist import (POLICY as CAGEY_POLICY, MONITOR_FILE, MONITOR_LINES, MONITOR_VERSION,
                                        BOOK_COLUMNS, usable_quote)
import narrow_margin as nm
POLICIES = (POLICY, CAGEY_POLICY)  # v27 and v28 value-tier picks are graded together, split by policy.
from price_edge_cagey_shortlist import (TIER_FILE, TIER_RULE_VALUE, TIER_RULE_NARROW, PRICE_VALUE,
                                        PRICE_BELOW_FAIR, OVER_1_5)
CAGEY_REVIEW_MIN_PICKS = 50
CAGEY_TIER_REVIEW_MIN_PICKS = 50

VERSION = 'price-edge-v27-tracking-v1'
FILE = 'price_edge_tagged_candidates.csv'
OUTPUT_DIR = Path('performance') / 'price_edge_v27'
STOP_REVIEW_MIN_PICKS = 100
MIN_LEAD_MINUTES = 20
COLUMNS = ['list_version', 'generated_at_utc', 'league', 'home_team', 'away_team', 'kickoff_utc', 'fixture_id',
           'market', 'market_to_bet', 'handicap_side', 'handicap_line', 'side_role', 'bookmaker',
           'offered_decimal_odds', 'fair_probability', 'fair_odds', 'reference_type', 'edge', 'decision',
           'rejection_reasons', 'tagged_probe', *TAGS, 'pinnacle_draw_probability', 'pinnacle_over_2_5_probability',
           'cagey_score', 'cagey_fit']
EQUIVALENT = {'Home win': ('home', -0.5), 'Away win': ('away', -0.5),
              'Double Chance 1X': ('home', 0.5), 'Double Chance X2': ('away', 0.5)}
SPLITS = ('bookmaker', 'odds_band', 'reference_type', 'side_role', 'balanced', 'low_total', 'high_draw', 'even_odds', 'tagged',
          'cagey_quintile', 'value_market_group')
TIER_SPLITS = ('tier', 'policy', 'bookmaker', 'reference_type', 'corrected_cagey_quintile', 'balanced', 'low_total',
               'high_draw', 'even_odds', 'qualified_only_by_correction', 'cagey_tier_rule', 'price_flag')
QUINTILES = ('Q1 cagiest', 'Q2', 'Q3', 'Q4', 'Q5 most open')


def cagey_quintiles(scores) -> pd.Series:
    """Quintile of the cagey score within the graded set (Q1 = lowest P(2+ margin)); n/a when unavailable."""
    values = pd.to_numeric(pd.Series(scores), errors='coerce')
    out = pd.Series('n/a', index=values.index, dtype=object)
    known = values.dropna()
    if known.nunique() >= len(QUINTILES):
        out[known.index] = pd.qcut(known.rank(method='first'), len(QUINTILES), labels=QUINTILES).astype(str)
    return out


# ---------------------------------------------------------------------------
# Tagged-candidate sidecar
# ---------------------------------------------------------------------------

def write_list(decisions: pd.DataFrame, raw: Path, generated) -> List[dict]:
    """Every tagged candidate of this run (picked, rejected or probe), bound to its generation instant."""
    from performance_tracking import write_csv
    rows = []
    if len(decisions) and 'any_tag' in decisions:
        tagged = decisions.loc[decisions.any_tag.fillna(False).astype(bool)]
        rows = (tagged.reindex(columns=COLUMNS).assign(list_version=VERSION, generated_at_utc=generated)
                .astype(object).where(lambda f: f.notna(), None).to_dict('records'))
    write_csv(Path(raw) / FILE, rows, COLUMNS)
    return rows


def capture_file(raw: Path, generated) -> Optional[Path]:
    """Archive only a list bound to this exact generation instant."""
    from performance_tracking import read_csv, utc
    path = Path(raw) / FILE
    if not path.exists():
        return None
    rows = read_csv(path)
    if any(r.get('list_version') != VERSION or utc(r.get('generated_at_utc')) != utc(generated) for r in rows):
        return None
    return path


def capture_tier_file(raw: Path, generated) -> Optional[Path]:
    """Archive the cagey-tier list only when it belongs to this exact v28 generation."""
    from performance_tracking import read_csv, utc
    path = Path(raw) / TIER_FILE
    if not path.exists():
        return None
    rows = read_csv(path)
    if any(r.get('selection_policy_version') != CAGEY_POLICY or utc(r.get('evaluated_at_utc')) != utc(generated)
           for r in rows):
        return None
    return path


def capture_master_file(raw: Path, generated) -> Optional[Path]:
    """Archive the master shortlist only when it belongs to this exact v28 generation."""
    from performance_tracking import read_csv, utc
    from master_shortlist import FILE as MASTER_FILE
    path = Path(raw) / MASTER_FILE
    if not path.exists():
        return None
    rows = read_csv(path)
    if any(r.get('selection_policy_version') != CAGEY_POLICY or utc(r.get('evaluated_at_utc')) != utc(generated)
           for r in rows):
        return None
    return path


def capture_new_master_file(raw: Path, generated) -> Optional[Path]:
    """Archive the new master (shadow) only when every row belongs to this exact v28 generation and the rule."""
    from performance_tracking import read_csv, utc
    import master_reconciliation as mr
    path = Path(raw) / mr.load_config()['file']
    if not path.exists():
        return None
    rows = read_csv(path)
    if any(r.get('selection_policy_version') != CAGEY_POLICY or utc(r.get('evaluated_at_utc')) != utc(generated)
           or r.get('new_master_version') != mr.VERSION for r in rows):
        return None
    return path


def latest_per_fixture(rows: List[dict]) -> List[dict]:
    """The pick of the newest generation per fixture; within one generation the first capture.

    A late upload of an older forecast never replaces a newer one: generation decides which pick
    counts, capture time (already applied in archived_tier_rows) enforces the pre-kickoff cutoff.
    `rows` come oldest capture first, so a re-upload of the same generation never moves the pick.
    """
    from performance_tracking import fixture_key, utc
    frozen = {}
    for row in rows:
        key = fixture_key(row)
        if key not in frozen or utc(row['snapshot_generated_utc']) > utc(frozen[key]['snapshot_generated_utc']):
            frozen[key] = row
    return list(frozen.values())


def frozen_master_picks(root: Path, archive) -> List[dict]:
    """Latest-generation pre-kickoff archived master-shortlist pick per fixture."""
    from master_shortlist import FILE as MASTER_FILE
    return latest_per_fixture(archived_tier_rows(root, archive, MASTER_FILE))


def frozen_new_master_picks(root: Path, archive) -> List[dict]:
    """Latest-generation pre-kickoff archived new-master pick per fixture, exactly as the live master's: the
    archived file lists every nominated offer, so only its ranked picks (SHORTLISTED) are picks. Only picks made
    under the current rule's version count, so a rule change restarts the comparison."""
    import master_reconciliation as mr
    rows = archived_tier_rows(root, archive, mr.load_config()['file'])
    return latest_per_fixture([r for r in rows if r.get('new_master_decision') == 'SHORTLISTED'
                               and r.get('new_master_version') == mr.VERSION])


def new_master_offer_counts(root: Path, archive) -> Dict[str, int]:
    """Context for the comparison: gap checks over every offer of each fixture's newest pre-kickoff generation."""
    from performance_tracking import fixture_key, utc
    import master_reconciliation as mr
    rows = [r for r in archived_tier_rows(root, archive, mr.load_config()['file'])
            if r.get('new_master_version') == mr.VERSION]
    newest = {}
    for row in rows:
        key, stamp = fixture_key(row), utc(row['snapshot_generated_utc'])
        newest[key] = max(newest.get(key, stamp), stamp)
    seen, offers = set(), []
    for row in rows:  # a re-upload of the same generation is counted once
        if utc(row['snapshot_generated_utc']) != newest[fixture_key(row)]:
            continue
        if row.get('new_master_source') not in (None, '', mr.SOURCES[0]):
            continue  # fill-pool candidates are not nominated offers (the picks' tiers count them)
        key = (fixture_key(row), row.get('market'), row.get('handicap_side'), row.get('handicap_line'),
               row.get('offered_decimal_odds'))
        if key not in seen and row.get('new_master_decision') != 'NOT_EXECUTABLE':
            seen.add(key)
            offers.append(row)
    flagged = lambda column: sum(1 for r in offers if _flag(r.get(column)))
    return {'fixtures': len(newest), 'offers': len(offers),
            'included': sum(1 for r in offers if r.get('new_master_group') == 'included'),
            **{column: flagged(column) for column, _ in mr.LABELS},
            'no_view': sum(1 for r in offers if r.get('gap_check') == 'no_view')}


def _list_context(frame: pd.DataFrame) -> dict:
    profit = pd.to_numeric(frame['unit_profit'], errors='coerce') if 'unit_profit' in frame else pd.Series(dtype=float)
    graded = frame.loc[profit.notna()] if len(frame) else frame
    if graded.empty:
        return {'graded_matches': 0, 'weeks': 0}
    profit = profit.loc[graded.index]
    return {'graded_matches': int(len(graded)), 'weeks': int(graded['_week'].nunique()),
            'flat_stake_return_per_bet': float(profit.mean()), 'hit_rate': float((profit > 1e-12).mean()),
            'average_price': float(pd.to_numeric(graded['offered_decimal_odds'], errors='coerce').mean())}


def compare_masters(new: pd.DataFrame, live: pd.DataFrame, rule: dict, counts: Optional[dict] = None) -> dict:
    """The live comparison rule decided on 13 Nov 2026 (master_reconciliation_config.json, live_comparison):
    after at least `min_graded_matches` graded matches over at least `min_weeks` kickoff weeks on each list,
    flat-stake return per bet, new minus live, whole kickoff weeks resampled (the same weeks for both), 95%
    interval; the new master is better only if the interval is entirely above zero. Hit rate, average price
    and the offer counts are context only."""
    from performance_tracking import utc

    def weeks(frame):
        frame = frame.copy() if len(frame) else pd.DataFrame(columns=['kickoff_utc', 'unit_profit',
                                                                      'offered_decimal_odds'])
        stamps = [utc(k) for k in frame['kickoff_utc']]
        frame['_week'] = [f'{s.isocalendar().year}-W{s.isocalendar().week:02d}' if s else None for s in stamps]
        return frame
    new, live = weeks(new), weeks(live)
    out = {'rule': rule['rule'], 'decided': rule['decided'], 'new_master': _list_context(new),
           'live_master': _list_context(live), 'new_master_offers': counts or {}}
    ready = all(x['graded_matches'] >= rule['min_graded_matches'] and x['weeks'] >= rule['min_weeks']
                for x in (out['new_master'], out['live_master']))
    if not ready:
        out.update(status='WAITING', difference=None, interval_95=None, verdict='not yet comparable')
        return out
    graded = {name: f.assign(_p=pd.to_numeric(f['unit_profit'], errors='coerce')).dropna(subset=['_p'])
              for name, f in (('new', new), ('live', live))}
    all_weeks = sorted(set(graded['new']._week) | set(graded['live']._week))
    tables = {k: f.groupby('_week')['_p'].agg(['sum', 'count']).reindex(all_weeks, fill_value=0)
              for k, f in graded.items()}
    draws = np.random.default_rng(rule['seed']).integers(0, len(all_weeks),
                                                         size=(rule['bootstrap_samples'], len(all_weeks)))
    with np.errstate(invalid='ignore', divide='ignore'):
        sample = (tables['new']['sum'].to_numpy()[draws].sum(1) / tables['new']['count'].to_numpy()[draws].sum(1)
                  - tables['live']['sum'].to_numpy()[draws].sum(1) / tables['live']['count'].to_numpy()[draws].sum(1))
    sample = sample[np.isfinite(sample)]
    interval = [float(v) for v in np.quantile(sample, [.025, .975])]
    difference = float(graded['new']._p.mean() - graded['live']._p.mean())
    out.update(status='COMPARED', difference=difference, interval_95=interval, weeks_resampled=len(all_weeks),
               verdict='new master better' if interval[0] > 0 else 'new master not shown better')
    return out


def archived_tier_rows(root: Path, archive, name: str = TIER_FILE) -> List[dict]:
    """Every pre-kickoff archived pick of one archived list (the cagey tier by default), oldest capture first."""
    from performance_tracking import read_csv, utc
    rows = []
    for meta, _, _ in sorted(archive, key=lambda item: item[0]['captured_at_utc']):
        path = Path(root) / 'performance' / 'snapshots' / meta['git_commit_sha'][:16] / name
        if name not in meta.get('sha256', {}) or not path.exists():
            continue
        captured, generated = utc(meta['captured_at_utc']), utc(meta['generated_at_utc'])
        for row in read_csv(path):
            kick = utc(row.get('kickoff_utc'))
            if kick is None or max(captured, generated) > kick - timedelta(minutes=MIN_LEAD_MINUTES):
                continue
            rows.append({**row, 'snapshot_commit': meta['git_commit_sha'],
                         'snapshot_captured_utc': meta['captured_at_utc'],
                         'snapshot_generated_utc': meta['generated_at_utc']})
    return rows


def frozen_tier_picks(root: Path, archive) -> List[dict]:
    """Latest-generation pre-kickoff archived cagey-tier pick per fixture."""
    from performance_tracking import fixture_key, utc
    rows = archived_tier_rows(root, archive)
    newest = {}
    for row in rows:
        key = fixture_key(row)
        stamp = utc(row['snapshot_generated_utc'])
        newest[key] = max(newest.get(key, stamp), stamp)
    chosen = {}
    from cagey_tier_v3 import EXPANDED_RULES
    for row in rows:
        fixture = fixture_key(row)
        if utc(row['snapshot_generated_utc']) != newest[fixture]:
            continue
        group = row.get('cagey_market_group') or row.get('value_market_group')
        key = (fixture, group if row.get('cagey_tier_rule') in EXPANDED_RULES else None)
        chosen.setdefault(key, row)  # Same generation: preserve first capture.
    return list(chosen.values())


def bind_event_ids(rows: List[dict], archive) -> List[dict]:
    """Attach the odds event id the pick's own snapshot recorded for that fixture and kickoff.

    Picks carry no event id of their own (except master v2); the archived forecast of the same
    snapshot does. A pick whose snapshot has no matching forecast keeps none.
    """
    from performance_tracking import fixture_key, utc
    events = {}
    for meta, predictions, _ in archive:
        for item in predictions:
            event = str(item.get('odds_event_id') or '').strip()
            if event and event.lower() != 'nan':
                events[(meta['git_commit_sha'], fixture_key(item), utc(item.get('kickoff_utc')))] = event
    out = []
    for row in rows:
        own = str(row.get('odds_event_id') or '').strip()
        if own and own.lower() != 'nan':
            out.append(row)
            continue
        event = events.get((row.get('snapshot_commit'), fixture_key(row), utc(row.get('kickoff_utc'))))
        out.append({**row, 'odds_event_id': event} if event else row)
    return out


def _event_id(value) -> Optional[str]:
    text = str(value or '').strip()
    return text if text and text.lower() != 'nan' else None


# ---------------------------------------------------------------------------
# Correction monitoring (v28): forward calibration evidence, never a decision
# ---------------------------------------------------------------------------

CORRECTION_REVIEW_MIN_FIXTURES = 200
BOOTSTRAP_SAMPLES = 2000


def capture_monitoring_file(raw: Path, generated) -> Optional[Path]:
    """Archive the correction-monitoring records only when bound to this exact generation instant."""
    from performance_tracking import read_csv, utc
    path = Path(raw) / MONITOR_FILE
    if not path.exists():
        return None
    rows = read_csv(path)
    if any(r.get('monitoring_version') != MONITOR_VERSION or utc(r.get('generated_at_utc')) != utc(generated)
           for r in rows):
        return None
    return path


def _exclusion(row: dict, meta: dict) -> Optional[str]:
    """Why an archived record cannot count as forward evidence, or None when it can."""
    from performance_tracking import utc
    captured, generated = utc(meta.get('captured_at_utc')), utc(meta.get('generated_at_utc'))
    kick, stamp = utc(row.get('kickoff_utc')), utc(row.get('generated_at_utc'))
    latest_input = utc(row.get('latest_input_quote_utc'))
    if kick is None or captured is None or generated is None or stamp != generated:
        return 'record not bound to its snapshot generation'
    if row.get('status') != 'USABLE':
        return row.get('exclusion_reason') or 'unusable market-implied fit'
    if max(captured, generated) > kick - timedelta(minutes=MIN_LEAD_MINUTES):
        return f'captured less than {MIN_LEAD_MINUTES} minutes before kickoff'
    if latest_input is None or latest_input > generated or latest_input >= kick:
        return 'input quote not observed before generation'
    return None


def _validated_prices(row: dict) -> dict:
    """Blank any recorded bookmaker price whose own quote was not fresh at generation or not before kickoff."""
    out, blanked = dict(row), 0
    for side in ('home', 'away'):
        for line in MONITOR_LINES:
            for column in BOOK_COLUMNS.values():
                key = f"{side}_plus_{line:g}".replace('.', '_') + '_' + column
                if out.get(key) not in (None, '') and not usable_quote(out.get(key + '_utc'), out.get('generated_at_utc'),
                                                                       out.get('kickoff_utc')):
                    out[key], blanked = None, blanked + 1
    out['prices_blanked'] = blanked
    return out


def first_monitoring_records(root: Path, archive) -> List[dict]:
    """One record per fixture: its first eligible pre-kickoff capture, else its first record with the reason."""
    from performance_tracking import fixture_key, read_csv
    first, fallback = {}, {}
    for meta, _, _ in sorted(archive, key=lambda item: item[0]['captured_at_utc']):
        path = Path(root) / 'performance' / 'snapshots' / meta['git_commit_sha'][:16] / MONITOR_FILE
        if MONITOR_FILE not in meta.get('sha256', {}) or not path.exists():
            continue
        for row in read_csv(path):
            key = fixture_key(row)
            reason = _exclusion(row, meta)
            item = {**_validated_prices(row), 'fixture_key': key, 'snapshot_commit': meta['git_commit_sha'],
                    'snapshot_captured_utc': meta['captured_at_utc'], 'exclusion_reason': reason or ''}
            if reason is None:
                first.setdefault(key, item)
            else:
                fallback.setdefault(key, item)
    return [first.get(key) or fallback[key] for key in sorted(set(first) | set(fallback))]


def _number(value) -> Optional[float]:
    value = pd.to_numeric(value, errors='coerce')
    return float(value) if pd.notna(value) else None


def _log_loss(p: float, outcome: bool) -> float:
    p = min(max(p, 1e-12), 1 - 1e-12)
    return -math.log(p if outcome else 1 - p)


def grade_monitoring(rows: List[dict], records: List[dict], clock) -> pd.DataFrame:
    """Per fixture: state (GRADED, PENDING, EXCLUDED), outcomes, log losses and fair-price returns."""
    from asian_handicap import profit
    from performance_tracking import fixture_match, utc
    graded = []
    for row in rows:
        item = {**row, 'state': 'EXCLUDED' if row['exclusion_reason'] else 'PENDING', 'final_score': None}
        kick = utc(row.get('kickoff_utc'))
        if item['state'] == 'PENDING' and kick is not None and kick <= clock - timedelta(hours=2):
            match, state = fixture_match(row, records)
            if state == 'VERIFIED_FINISHED':
                home, away = int(match['home_goals']), int(match['away_goals'])
                margin = abs(home - away)
                item.update(state='GRADED', final_score=f'{home}-{away}', abs_margin=margin,
                            gameweek=f'{kick.isocalendar().year}-W{kick.isocalendar().week:02d}')
                for goals in (2, 3):
                    for basis in ('corrected', 'uncorrected'):
                        item[f'log_loss_{goals}plus_{basis}'] = _log_loss(_number(row[f'{basis}_p{goals}']), margin >= goals)
                    item[f'log_loss_gain_{goals}plus'] = (item[f'log_loss_{goals}plus_uncorrected']
                                                          - item[f'log_loss_{goals}plus_corrected'])
                for side in ('home', 'away'):
                    for line in MONITOR_LINES:
                        key = f'{side}_plus_{line:g}'.replace('.', '_')
                        for basis in ('corrected', 'uncorrected'):
                            odds = _number(row.get(f'{key}_{basis}_fair_odds'))
                            item[f'{key}_return_{basis}'] = (profit(home, away, side, line, odds)[1]
                                                             if odds is not None and odds > 1 else None)
        graded.append(item)
    return pd.DataFrame(graded)


def _interval(values, blocks) -> Dict[str, object]:
    from ah_close_backtest import block_bootstrap
    values = pd.to_numeric(pd.Series(list(values)), errors='coerce')
    blocks = pd.Series(list(blocks))
    keep = values.notna().to_numpy()
    if not keep.any():
        return {'n': 0, 'mean': None, 'low95': None, 'high95': None}
    mean, low, high = block_bootstrap(values[keep].to_numpy(), blocks[keep].to_numpy(), n_boot=BOOTSTRAP_SAMPLES)
    return {'n': int(keep.sum()), 'mean': mean, 'low95': low, 'high95': high}


def monitoring_summary(frame: pd.DataFrame) -> Dict[str, object]:
    states = frame['state'].value_counts().to_dict() if len(frame) else {}
    graded = frame[frame['state'] == 'GRADED'] if len(frame) else frame
    eligible = frame[frame['state'] != 'EXCLUDED'] if len(frame) else frame
    out = {'version': MONITOR_VERSION,
           'monitoring_start_utc': min(eligible['snapshot_captured_utc']) if len(eligible) else None,
           'model_versions': sorted(set(frame['model_version'].dropna())) if len(frame) else [],
           'fixtures': {'eligible': int(len(eligible)), 'pending': int(states.get('PENDING', 0)),
                        'graded': int(states.get('GRADED', 0)), 'excluded': int(states.get('EXCLUDED', 0))},
           'excluded_by_reason': (frame.loc[frame['state'] == 'EXCLUDED', 'exclusion_reason'].value_counts().to_dict()
                                  if len(frame) else {}),
           'by_quintile': {}, 'log_loss': {}, 'fair_price_returns': {}}
    if not len(graded):
        out['correction_review'] = False
        return out
    blocks = graded['gameweek']
    for label in nm.QUINTILE_LABELS:
        part = graded[graded['corrected_cagey_quintile'] == label]
        out['by_quintile'][label] = {
            'n': int(len(part)),
            **{f'{goals}plus_{kind}': (float((part['abs_margin'] >= goals).mean()) if kind == 'actual'
                                       else float(pd.to_numeric(part[f'{kind}_p{goals}']).mean())) if len(part) else None
               for goals in (2, 3) for kind in ('actual', 'corrected', 'uncorrected')},
            # Gameweek-block bootstrap interval for each actual rate.
            **{f'{goals}plus_actual_interval': _interval((part['abs_margin'] >= goals).astype(float), part['gameweek'])
               for goals in (2, 3)}}
    for goals in (2, 3):
        out['log_loss'][f'{goals}plus'] = {
            'corrected': float(graded[f'log_loss_{goals}plus_corrected'].mean()),
            'uncorrected': float(graded[f'log_loss_{goals}plus_uncorrected'].mean()),
            'paired_gain': _interval(graded[f'log_loss_gain_{goals}plus'], blocks)}
    # Every AH line of every fixture, kept in its fixture's gameweek block.
    for basis in ('corrected', 'uncorrected'):
        columns = [c for c in graded.columns if c.endswith(f'_return_{basis}')]
        stacked = graded[[*columns, 'gameweek']].melt(id_vars='gameweek', value_vars=columns)
        out['fair_price_returns'][basis] = _interval(stacked['value'], stacked['gameweek'])
    gain = out['log_loss']['2plus']['paired_gain']
    out['correction_review'] = bool(gain['n'] >= CORRECTION_REVIEW_MIN_FIXTURES and gain['high95'] is not None
                                    and gain['high95'] < 0)
    return out


def _interval_text(m: dict, scale: float = 1.0, unit: str = '') -> str:
    if not m.get('n'):
        return 'n/a (0)'
    return (f"{m['mean'] * scale:+.3f}{unit} [{m['low95'] * scale:+.3f}, {m['high95'] * scale:+.3f}] "
            f"(n={m['n']})")


def monitoring_report(m: dict) -> List[str]:
    f = m['fixtures']
    lines = ['## Correction monitoring', '']
    if m.get('correction_review'):
        gain = m['log_loss']['2plus']['paired_gain']
        lines += [f"> **CORRECTION REVIEW**: {gain['n']} graded forward fixtures with a paired 2+ margin log-loss gain "
                  f"of {_interval_text(gain, 1000)} x 1e-3, interval entirely below 0. Recommendation: review the "
                  'correction (this report does not change selection, the correction or stakes).', '']
    lines += [f"Forward monitoring of {MONITOR_VERSION} started {m['monitoring_start_utc'] or 'not yet'} "
              '(first eligible capture). Earlier forecasts are not backfilled. One record per fixture: its first '
              f'pre-kickoff capture at least {MIN_LEAD_MINUTES} minutes before kickoff. Quintiles use the fixed '
              'training-period boundaries stored with the model.', '',
              f"Fixtures: eligible {f['eligible']}, pending {f['pending']}, graded {f['graded']}, "
              f"excluded {f['excluded']}.", '']
    if m['excluded_by_reason']:
        lines += ['| excluded because | fixtures |', '|---|---:|']
        lines += [f'| {k} | {v} |' for k, v in m['excluded_by_reason'].items()]
        lines.append('')
    if not f['graded']:
        return lines + ['No graded fixtures yet.', '']
    lines += ['| quintile | n | 2+ actual | 2+ corrected | 2+ uncorrected | 3+ actual | 3+ corrected | 3+ uncorrected |',
              '|---|---:|---:|---:|---:|---:|---:|---:|']
    def rate(q, goals, kind):
        value = q.get(f'{goals}plus_{kind}')
        if value is None:
            return 'n/a'
        band = q.get(f'{goals}plus_actual_interval') if kind == 'actual' else None
        return f'{value:.1%} [{band["low95"]:.1%}, {band["high95"]:.1%}]' if band and band.get('n') else f'{value:.1%}'
    for label, q in m['by_quintile'].items():
        cells = [rate(q, g, k) for g in (2, 3) for k in ('actual', 'corrected', 'uncorrected')]
        lines.append(f"| {label} | {q['n']} | " + ' | '.join(cells) + ' |')
    lines += ['', '| log loss | corrected | uncorrected | paired gain x 1e-3 [95%] |', '|---|---:|---:|---|']
    for goals in (2, 3):
        ll = m['log_loss'][f'{goals}plus']
        lines.append(f"| {goals}+ margin | {ll['corrected']:.4f} | {ll['uncorrected']:.4f} | "
                     f"{_interval_text(ll['paired_gain'], 1000)} |")
    r = m['fair_price_returns']
    lines += ['', 'Calibration diagnostic, NOT achievable bookmaker ROI: return per bet when every AH +1 to +2 line '
              'on both sides is settled at its own fair price (no margin). A calibrated price returns about 0.',
              f"- at the corrected fair price: {_interval_text(r['corrected'], 100, '%')}",
              f"- at the uncorrected fair price: {_interval_text(r['uncorrected'], 100, '%')}", '',
              'Actual rates show their 95% interval in brackets. '
              f'Intervals: gameweek-block bootstrap ({BOOTSTRAP_SAMPLES} resamples); every line of a fixture stays in '
              f'its gameweek block. CORRECTION REVIEW: >= {CORRECTION_REVIEW_MIN_FIXTURES} graded fixtures with the '
              '2+ paired log-loss gain interval entirely below 0; it recommends review only.', '']
    return lines


def tier_frame(value: pd.DataFrame, tier: pd.DataFrame) -> pd.DataFrame:
    """Both tiers in one frame with the v28 tracking splits."""
    parts = [f.assign(tier=name) for name, f in (('value', value), ('cagey', tier)) if len(f)]
    if not parts:
        return pd.DataFrame(columns=[*TIER_SPLITS, 'clv', 'unit_profit'])
    frame = pd.concat(parts, ignore_index=True, sort=False)
    versions = frame.get('selection_policy_version', pd.Series(index=frame.index, dtype=object))
    frame['policy'] = versions.map({POLICY: 'v27', CAGEY_POLICY: 'v28'}).fillna('other')
    frame['corrected_cagey_quintile'] = cagey_quintiles(frame.get('corrected_cagey_score',
                                                                  pd.Series(index=frame.index, dtype=float)))
    flag = frame.get('qualified_only_by_correction', pd.Series(index=frame.index, dtype=object))
    frame['qualified_only_by_correction'] = flag.map(lambda v: 'yes' if _flag(v) else 'no')
    # Cagey-tier rule and price: value-v1 picks carry no price_flag and all passed expected profit >= 0.
    price = frame.get('price_flag', pd.Series(index=frame.index, dtype=object))
    cagey = frame.tier == 'cagey'
    flagged = cagey & price.notna() & price.astype(str).str.strip().ne('')
    recorded_rules = frame.get('cagey_tier_rule', pd.Series(index=frame.index, dtype=object)).copy()
    frame['cagey_tier_rule'] = None
    frame.loc[cagey, 'cagey_tier_rule'] = TIER_RULE_VALUE
    frame.loc[flagged, 'cagey_tier_rule'] = TIER_RULE_NARROW
    from cagey_tier_v3 import EXPANDED_RULES
    frame.loc[cagey & recorded_rules.isin(EXPANDED_RULES), 'cagey_tier_rule'] = recorded_rules[cagey & recorded_rules.isin(EXPANDED_RULES)]
    frame['price_flag'] = None
    frame.loc[cagey, 'price_flag'] = PRICE_VALUE
    frame.loc[flagged, 'price_flag'] = price[flagged]
    return frame


def active_tier_rule() -> str:
    """The cagey-tier rule in force today (cagey_correction_config.json)."""
    from price_edge_cagey_shortlist import load_settings, tier_rule
    return tier_rule(load_settings())


def cagey_flags(frame: pd.DataFrame, active_rule: str = TIER_RULE_VALUE) -> Dict[str, object]:
    """Review flags; each recommends switching its feature off and never does so itself.

    The tier review counts only the ACTIVE rule's own value-priced picks: picks made under another rule never
    trigger it (they stay visible in cagey_tier_roi_by_rule), and below-fair picks are listed knowing the
    model expects a small loss on them.
    """
    if frame.empty:
        value_only, tier = pd.Series(dtype=float), pd.Series(dtype=float)
        by_rule = {}
    else:
        value_only = frame.loc[(frame.tier == 'value') & (frame.qualified_only_by_correction == 'yes'), 'clv']
        cagey = frame.loc[frame.tier == 'cagey']
        rules = cagey['cagey_tier_rule'] if 'cagey_tier_rule' in cagey else pd.Series(TIER_RULE_VALUE, index=cagey.index)
        price = cagey['price_flag'] if 'price_flag' in cagey else pd.Series(PRICE_VALUE, index=cagey.index)
        rules, price = rules.fillna(TIER_RULE_VALUE), price.fillna(PRICE_VALUE)
        tier = cagey.loc[(rules == active_rule) & (price == PRICE_VALUE), 'unit_profit']
        by_rule = {rule: {'all': summarize(cagey.loc[rules == rule, 'unit_profit']),
                          PRICE_VALUE: summarize(cagey.loc[(rules == rule) & (price == PRICE_VALUE), 'unit_profit']),
                          PRICE_BELOW_FAIR: summarize(cagey.loc[(rules == rule) & (price == PRICE_BELOW_FAIR),
                                                                'unit_profit'])}
                   for rule in sorted(set(rules))}
    only, roi = summarize(value_only), summarize(tier)
    cagey_review = only['n'] >= CAGEY_REVIEW_MIN_PICKS and only['mean'] < 0
    tier_review = (roi['n'] >= CAGEY_TIER_REVIEW_MIN_PICKS and roi['standard_error'] is not None
                   and roi['mean'] + 1.96 * roi['standard_error'] < 0)
    return {'correction_only_clv': only, 'cagey_tier_roi': roi, 'cagey_tier_active_rule': active_rule,
            'cagey_tier_roi_by_rule': by_rule,
            'cagey_review': bool(cagey_review), 'cagey_tier_review': bool(tier_review),
            'cagey_review_rule': f'>= {CAGEY_REVIEW_MIN_PICKS} graded correction-only value picks with mean CLV < 0; '
                                 'recommends cagey_correction_enabled = false',
            'cagey_tier_review_rule': f'>= {CAGEY_TIER_REVIEW_MIN_PICKS} graded value-priced cagey-tier picks made '
                                      f'under the active rule ({active_rule}) with realised ROI 95% interval entirely '
                                      'below 0; recommends cagey_tier_enabled = false'}


def frozen_candidates(root: Path, archive) -> List[dict]:
    """Latest pre-kickoff archived entry per fixture, side, line and bookmaker."""
    from performance_tracking import fixture_key, read_csv, utc
    frozen = {}
    for meta, _, _ in sorted(archive, key=lambda item: item[0]['captured_at_utc']):
        path = Path(root) / 'performance' / 'snapshots' / meta['git_commit_sha'][:16] / FILE
        if FILE not in meta.get('sha256', {}) or not path.exists():
            continue
        captured, generated = utc(meta['captured_at_utc']), utc(meta['generated_at_utc'])
        for row in read_csv(path):
            kick = utc(row.get('kickoff_utc'))
            if kick is None or max(captured, generated) > kick - timedelta(minutes=MIN_LEAD_MINUTES):
                continue
            key = (fixture_key(row), row.get('handicap_side'), row.get('handicap_line'), row.get('bookmaker') or '',
                   'DC12' if row.get('market') == 'Double Chance 12' else '')
            if key not in frozen or generated > utc(frozen[key]['snapshot_generated_utc']):
                frozen[key] = {**row, 'snapshot_commit': meta['git_commit_sha'],
                               'snapshot_captured_utc': meta['captured_at_utc'],
                               'snapshot_generated_utc': meta['generated_at_utc']}
    return list(frozen.values())


# ---------------------------------------------------------------------------
# Closing line value
# ---------------------------------------------------------------------------

def ah_line(market: str, side=None, line=None):
    """(side, line) a v27 market settles as."""
    from asian_handicap import parse_label
    parsed = parse_label(market)
    if parsed:
        return parsed
    if market in EQUIVALENT:
        return EQUIVALENT[market]
    try:
        return (side, float(line)) if side in ('home', 'away') else None
    except (TypeError, ValueError):
        return None


def close_win_share(quotes: List[dict], side: str, line: float) -> Optional[float]:
    """Pinnacle fair close win-share on (side, line), proportional margin removal."""
    from asian_handicap import label
    from ah_close_backtest import devig_proportional
    pinnacle = {q['selection']: float(q['decimal_odds']) for q in quotes
                if q.get('bookmaker') == 'pinnacle' and q.get('decimal_odds')}
    mine, other = label(side, line), label('away' if side == 'home' else 'home', -line)
    if mine in pinnacle and other in pinnacle:
        return devig_proportional(pinnacle[mine], pinnacle[other])[0]
    if abs(line) == 0.5 and all(k in pinnacle for k in ('home', 'draw', 'away')):
        total = sum(1 / pinnacle[k] for k in ('home', 'draw', 'away'))
        p = {k: (1 / pinnacle[k]) / total for k in ('home', 'draw', 'away')}
        opponent = 'away' if side == 'home' else 'home'
        return p[side] if line < 0 else 1 - p[opponent]
    return None


def close_over_share(quotes: List[dict], point: float = 1.5) -> Optional[float]:
    """Pinnacle fair close probability of over `point` goals, proportional margin removal."""
    from ah_close_backtest import devig_proportional
    pinnacle = {q['selection']: float(q['decimal_odds']) for q in quotes
                if q.get('bookmaker') == 'pinnacle' and q.get('decimal_odds')}
    suffix = str(point).replace('.', '_')
    over, under = pinnacle.get('over_' + suffix), pinnacle.get('under_' + suffix)
    return devig_proportional(over, under)[0] if over and under else None


def closing_for(row: dict, observations: List[dict], side: Optional[str], line: Optional[float], share=None):
    """Latest near-kickoff observation after capture that prices the pick for Pinnacle.

    `share(quotes)` overrides the AH win-share lookup (used for over 1.5).
    """
    from performance_tracking import fixture_key, utc
    best = None
    event = _event_id(row.get('odds_event_id'))
    for obs in observations:
        if fixture_key(obs['fixture']) != fixture_key(row) or utc(obs['fixture']['kickoff_utc']) != utc(row['kickoff_utc']):
            continue
        # Bound to the archived odds event: a different event with the same teams and kickoff never prices it.
        observed_event = _event_id(obs['fixture'].get('odds_event_id'))
        if event is not None and observed_event is not None and observed_event != event:
            continue
        entered = utc(row.get('placed_at_utc') if row.get('evaluation_view') == 'user_recorded_placed_bets' else row.get('snapshot_captured_utc'))
        if entered is None or utc(obs['observed_at_utc']) < entered:
            continue
        quotes = obs.get('quotes', [])
        q = share(quotes) if share is not None else close_win_share(quotes, side, line)
        if q is not None and (best is None or utc(obs['observed_at_utc']) > best[0]):
            best = (utc(obs['observed_at_utc']), q)
    return best


def odds_band(odds) -> Optional[str]:
    from price_edge_backtest import odds_band as band
    try:
        return band(float(odds))
    except (TypeError, ValueError, StopIteration):
        return None


def _flag(value) -> bool:
    return str(value).strip().lower() in ('true', '1')


def settle(row: dict, final: Optional[dict], side: str, line: float, price) -> Dict[str, object]:
    from asian_handicap import profit
    if not final:
        return {'result_status': None, 'unit_profit': None}
    try:
        from quote_policy import stake_cost
        status, gain = profit(int(final['home_goals']), int(final['away_goals']), side, line, float(price),
                              stake_cost(row.get('per_stake_cost') or 0))
    except (TypeError, ValueError, KeyError):
        return {'result_status': None, 'unit_profit': None}
    return {'result_status': status, 'unit_profit': gain}


def settle_over_1_5(row: dict, final: Optional[dict], price) -> Dict[str, object]:
    """Over 1.5 goals: won on two or more regulation-time goals; no push."""
    if not final or price is None:
        return {'result_status': None, 'unit_profit': None}
    try:
        from quote_policy import stake_cost
        won = int(final['home_goals']) + int(final['away_goals']) >= 2
        cost = stake_cost(row.get('per_stake_cost') or 0)
    except (TypeError, ValueError, KeyError):
        return {'result_status': None, 'unit_profit': None}
    return {'result_status': 'WON' if won else 'LOST', 'unit_profit': (float(price) - 1 if won else -1.0) - float(cost)}


def close_dc12_share(quotes: List[dict]) -> Optional[float]:
    """P(non-draw) from a normalized Pinnacle DC quote or complete 1X2 book."""
    pin = {q.get('selection'): q for q in quotes if q.get('bookmaker') == 'pinnacle'}
    direct = _number(pin.get('home_away', {}).get('fair_probability'))
    if direct is not None and 0 < direct < 1:
        return direct
    if not all(k in pin for k in ('home', 'draw', 'away')):
        return None
    probs = [_number(pin[k].get('fair_probability')) for k in ('home', 'draw', 'away')]
    if all(p is not None and 0 <= p <= 1 for p in probs) and abs(sum(probs)-1) <= 1e-6:
        return probs[0]+probs[2]
    return None


def settle_dc12(row: dict, final: Optional[dict], price) -> Dict[str, object]:
    if not final or price is None:
        return {'result_status': None, 'unit_profit': None}
    try:
        from quote_policy import stake_cost
        won = int(final['home_goals']) != int(final['away_goals'])
        cost = stake_cost(row.get('per_stake_cost') or 0)
        gain = (float(price)-1 if won else -1.)-cost
    except (ValueError, TypeError, KeyError):
        return {'result_status': None, 'unit_profit': None}
    return {'result_status': 'WON' if won else 'LOST', 'unit_profit': gain}


def verified_final(row, records, clock, cache=None):
    from performance_tracking import fixture_match, utc
    kick=utc(row.get('kickoff_utc'))
    if kick is None or kick > clock-timedelta(hours=2):
        return None
    # Raw identity strings are part of the key: caching must not relax alias verification.
    key=(row.get('league'),row.get('home_team'),row.get('away_team'),kick)
    if cache is not None and key in cache:
        return cache[key]
    match,state=fixture_match(row,records)
    result=match if state=='VERIFIED_FINISHED' else None
    if cache is not None: cache[key]=result
    return result


def grade_over_1_5(row: dict, observations: List[dict], records: List[dict], clock, *, share=None, settlement=None, final_cache=None) -> dict:
    """Binary non-AH pick; defaults to Over 1.5 and accepts DC 12 settlement/close adapters."""
    from performance_tracking import fixture_match, utc
    price = pd.to_numeric(row.get('offered_decimal_odds'), errors='coerce')
    fair = pd.to_numeric(row.get('fair_odds'), errors='coerce')
    share = share or close_over_share
    settlement = settlement or settle_over_1_5
    close = closing_for(row, observations, None, None, share=share)
    final = verified_final(row,records,clock,final_cache)
    item = {**row, 'ah_side': None, 'ah_line': None, 'odds_band': odds_band(price),
            'tagged': 'any tag' if any(_flag(row.get(t)) for t in TAGS) else 'no tag',
            **{t: 'yes' if _flag(row.get(t)) else 'no' for t in TAGS},
            'close_observed_at_utc': close[0].isoformat() if close else None,
            'pinnacle_close_win_share': close[1] if close else None,
            'clv': float(price) * close[1] - 1 if close and pd.notna(price) else None,
            'final_score': f"{final['home_goals']}-{final['away_goals']}" if final else None,
            **settlement(row, final, float(price) if pd.notna(price) else None)}
    fair_result = settlement({**row, 'per_stake_cost': 0}, final, float(fair) if pd.notna(fair) and fair > 1 else None)
    item['return_at_capture_fair'] = fair_result['unit_profit']
    return item


def grade(rows: List[dict], observations: List[dict], records: List[dict], clock) -> pd.DataFrame:
    from performance_tracking import fixture_match, utc
    from performance_tracking import fixture_key
    grouped_observations={}
    for obs in observations:
        key=(fixture_key(obs['fixture']),utc(obs['fixture']['kickoff_utc']))
        grouped_observations.setdefault(key,[]).append(obs)
    final_cache={}
    graded = []
    for row in rows:
        own_observations=grouped_observations.get((fixture_key(row),utc(row.get('kickoff_utc'))),[])
        if row.get('market') == 'Double Chance 12':
            graded.append(grade_over_1_5(row, own_observations, records, clock,
                          share=close_dc12_share, settlement=settle_dc12, final_cache=final_cache))
            continue
        if row.get('market') == OVER_1_5:
            graded.append(grade_over_1_5(row, own_observations, records, clock, final_cache=final_cache))
            continue
        target = ah_line(row.get('market'), row.get('handicap_side'), row.get('handicap_line'))
        if target is None:
            continue
        side, line = target
        price = pd.to_numeric(row.get('offered_decimal_odds'), errors='coerce')
        fair = pd.to_numeric(row.get('fair_odds'), errors='coerce')
        close = closing_for(row, own_observations, side, line)
        final = verified_final(row,records,clock,final_cache)
        item = {**row, 'ah_side': side, 'ah_line': line, 'odds_band': odds_band(price),
                'tagged': 'any tag' if any(_flag(row.get(t)) for t in TAGS) else 'no tag',
                **{t: 'yes' if _flag(row.get(t)) else 'no' for t in TAGS},
                'close_observed_at_utc': close[0].isoformat() if close else None,
                'pinnacle_close_win_share': close[1] if close else None,
                'clv': float(price) * close[1] - 1 if close and pd.notna(price) else None,
                'final_score': f"{final['home_goals']}-{final['away_goals']}" if final else None,
                **settle(row, final, side, line, price if pd.notna(price) else None)}
        fair_result = settle({**row, 'per_stake_cost': 0}, final, side, line,
                             fair if pd.notna(fair) and fair > 1 else None)
        item['return_at_capture_fair'] = fair_result['unit_profit']
        graded.append(item)
    frame = pd.DataFrame(graded)
    if len(frame):
        frame['cagey_quintile'] = cagey_quintiles(frame.get('cagey_score', pd.Series(index=frame.index, dtype=float)))
    return frame


def summarize(values) -> Dict[str, object]:
    values = pd.to_numeric(pd.Series(values), errors='coerce').dropna()
    if values.empty:
        return {'n': 0, 'mean': None, 'positive_share': None, 'standard_error': None}
    se = float(values.std(ddof=1) / math.sqrt(len(values))) if len(values) > 1 else None
    return {'n': int(len(values)), 'mean': float(values.mean()), 'positive_share': float((values > 0).mean()),
            'standard_error': se}


def split_table(frame: pd.DataFrame, value: str, columns=SPLITS) -> Dict[str, Dict[str, dict]]:
    out = {}
    for column in columns:
        if frame.empty or column not in frame:
            out[column] = {}
            continue
        out[column] = {str(k): summarize(g[value]) for k, g in frame.groupby(frame[column].fillna('n/a'), sort=True)}
    return out


def review(root: Path, archive, records: List[dict], clock, active_rule: Optional[str] = None) -> dict:
    """Write performance/price_edge_v27/{summary.json, picks.csv, tagged_candidates.csv, report.md}."""
    from performance_tracking import frozen_rows, write_json
    from closing_odds import load_observations
    root = Path(root)
    observations, rejected = load_observations(root, clock)
    picks = [r for r in frozen_rows(archive, 'shortlist', latest=True) if r.get('selection_policy_version') in POLICIES]
    graded = grade(bind_event_ids(picks, archive), observations, records, clock)
    tagged = grade(bind_event_ids(frozen_candidates(root, archive), archive), observations, records, clock)
    tier = grade(bind_event_ids(frozen_tier_picks(root, archive), archive), observations, records, clock)
    master = grade(bind_event_ids(frozen_master_picks(root, archive), archive), observations, records, clock)
    new_master = grade(bind_event_ids(frozen_new_master_picks(root, archive), archive), observations, records, clock)
    from recommendation_history import rows as history_rows, summarize as history_summary
    history = grade(bind_event_ids(history_rows(root,archive),archive),observations,records,clock)
    from bet_ledger import review_private
    actual_bets = review_private(root,observations,records,clock)
    monitoring = grade_monitoring(first_monitoring_records(root, archive), records, clock)
    both = tier_frame(graded, tier)
    flags = cagey_flags(both, active_rule if active_rule is not None else active_tier_rule())
    clv = graded['clv'] if len(graded) else pd.Series(dtype=float)
    overall = summarize(clv)
    stop = overall['n'] >= STOP_REVIEW_MIN_PICKS and overall['mean'] is not None and overall['mean'] < 0
    summary = {
        'version': VERSION, 'policy': POLICY, 'reviewed_at_utc': clock.isoformat(),
        'recommendation_history': history_summary(history), 'actual_bets': actual_bets,
        'frozen_picks': int(len(graded)), 'clv': overall,
        'profit': summarize(graded['unit_profit'] if len(graded) else []),
        'stop_review': bool(stop),
        'stop_review_rule': f'>= {STOP_REVIEW_MIN_PICKS} graded picks with mean CLV < 0',
        'clv_by': split_table(graded, 'clv'),
        'master_picks': int(len(master)),
        'master': {'clv': summarize(master['clv'] if len(master) else []),
                   'profit': summarize(master['unit_profit'] if len(master) else []),
                   'by_price_flag': {flag: {'clv': summarize(g['clv']), 'profit': summarize(g['unit_profit'])}
                                     for flag, g in (master.groupby(master['master_price_flag'].fillna('n/a'))
                                                     if len(master) and 'master_price_flag' in master else [])}},
        'new_master_picks': int(len(new_master)),
        'new_master': {'clv': summarize(new_master['clv'] if len(new_master) else []),
                       'profit': summarize(new_master['unit_profit'] if len(new_master) else []),
                       'by_labels': {labels: {'clv': summarize(g['clv']), 'profit': summarize(g['unit_profit'])}
                                     for labels, g in (new_master.groupby(new_master['new_master_labels']
                                                                          .fillna('no label'))
                                                       if len(new_master) and 'new_master_labels' in new_master
                                                       else [])},
                       # Context only (the comparison rule never reads it): results by fill-rule tier.
                       'by_tier': {tier: {'clv': summarize(g['clv']), 'profit': summarize(g['unit_profit'])}
                                   for tier, g in (new_master.groupby(new_master['new_master_tier'].fillna('n/a'))
                                                   if len(new_master) and 'new_master_tier' in new_master else [])}},
        'master_comparison': _master_comparison(root, archive, new_master, master),
        'cagey_tier_picks': int(len(tier)),
        'cagey_tier': {'clv': summarize(tier['clv'] if len(tier) else []),
                       'profit': summarize(tier['unit_profit'] if len(tier) else [])},
        'both_tiers_clv_by': split_table(both, 'clv', TIER_SPLITS),
        'both_tiers_profit_by': split_table(both, 'unit_profit', TIER_SPLITS),
        **flags,
        'tagged_candidates': {
            'frozen': int(len(tagged)),
            'with_offered_price': int(tagged['offered_decimal_odds'].notna().sum()) if len(tagged) else 0,
            'edge_at_capture_1xbet': summarize(tagged.loc[tagged.bookmaker.eq('1xBet'), 'edge'] if len(tagged) else []),
            'return_at_capture_fair': summarize(tagged['return_at_capture_fair'] if len(tagged) else []),
            'return_at_capture_fair_plus_lines': summarize(
                tagged.loc[tagged.ah_line.astype(float) > 0, 'return_at_capture_fair'] if len(tagged) else []),
            'by_tag': {t: summarize(tagged.loc[tagged[t].eq('yes'), 'return_at_capture_fair'] if len(tagged) else [])
                       for t in TAGS}},
        'correction_monitoring': monitoring_summary(monitoring),
        'rejected_observation_files': rejected,
        'note': 'CLV = entry odds x Pinnacle near-kickoff fair win-share on the same AH line - 1 (proportional). '
                'Near-kickoff feed quotes, not verified official closes or executed bets. Tagged candidates are '
                'tracked for the narrow-margin hypothesis only; they never change a decision.',
    }
    dest = root / OUTPUT_DIR
    dest.mkdir(parents=True, exist_ok=True)
    write_json(dest / 'summary.json', summary)
    graded.to_csv(dest / 'picks.csv', index=False)
    tagged.to_csv(dest / 'tagged_candidates.csv', index=False)
    tier.to_csv(dest / 'cagey_tier_picks.csv', index=False)
    history.to_csv(dest / 'all_recommendation_generations.csv', index=False)
    master.to_csv(dest / 'master_shortlist_picks.csv', index=False)
    new_master.to_csv(dest / 'master_shortlist_new_picks.csv', index=False)
    monitoring.to_csv(dest / 'correction_monitoring.csv', index=False)
    (dest / 'report.md').write_text(report(summary), encoding='utf-8')
    return summary


def _master_comparison(root: Path, archive, new_master: pd.DataFrame, master: pd.DataFrame) -> dict:
    import master_reconciliation as mr
    return compare_masters(new_master, master, mr.load_config()['live_comparison'],
                           new_master_offer_counts(root, archive))


def new_master_report(summary: dict) -> List[str]:
    """The new master (shadow) beside the live master, with the comparison rule's status."""
    if 'master_comparison' not in summary:
        return []
    m, c = summary['new_master'], summary['master_comparison']
    lines = ["## New master (shadow, fill rule) beside the live master", '',
             f"Frozen picks: {summary['new_master_picks']}; CLV {_fmt(m['clv'])}; realised profit per bet "
             f"{_fmt(m['profit'])}. Live master: {summary.get('master_picks', 0)} frozen picks, realised profit per "
             f"bet {_fmt(summary['master']['profit'])}.", '',
             f"Comparison rule (decided {c['decided']}): {c['rule']}", '']
    row = lambda name, x: (f"| {name} | {x['graded_matches']} | {x['weeks']} | "
                           + (f"{x['flat_stake_return_per_bet']:+.2%} | {x['hit_rate']:.1%} | {x['average_price']:.2f} |"
                              if x['graded_matches'] else 'n/a | n/a | n/a |'))
    lines += ['| list | graded matches | weeks | flat-stake return per bet | hit rate | average price |',
              '|---|---|---|---|---|---|', row('new master', c['new_master']), row('live master', c['live_master']), '']
    if c['status'] == 'COMPARED':
        lo, hi = c['interval_95']
        lines.append(f"**New minus live:** {c['difference']:+.2%} per bet (95% interval {lo:+.2%} to {hi:+.2%}, "
                     f"{c['weeks_resampled']} weeks resampled): {c['verdict']}.")
    else:
        lines.append(f"**Status:** waiting for at least 150 graded matches over at least 3 weeks on each list "
                     f"({c['verdict']}).")
    o = c.get('new_master_offers') or {}
    if o:
        lines.append(f"Context, new master offers (newest pre-kickoff generation per fixture): {o['offers']} offers "
                     f"on {o['fixtures']} fixtures; included (cagey safe) {o['included']}; labels: both agree "
                     f"{o['both_agree']}, research too optimistic {o['research_too_optimistic']}, research strongly "
                     f"disagrees {o['inspection_flag']}, one view missing {o['one_view_missing']}, no research check "
                     f"{o['no_research_check']}, unvalidated view {o['unvalidated_view']}; no view {o['no_view']}.")
    if m.get('by_tier'):
        lines += ['', 'By tier (context only; the comparison rule never reads it):', '',
                  '| tier | mean CLV (n) | realised profit per bet (n) |', '|---|---|---|']
        lines += [f"| {g} | {_fmt(v['clv'])} | {_fmt(v['profit'])} |" for g, v in m['by_tier'].items()]
    if m.get('by_labels'):
        lines += ['', '| labels | mean CLV (n) | realised profit per bet (n) |', '|---|---|---|']
        lines += [f"| {g} | {_fmt(v['clv'])} | {_fmt(v['profit'])} |" for g, v in m['by_labels'].items()]
    lines.append('')
    return lines


def _fmt(m: dict) -> str:
    if not m.get('n'):
        return 'n/a (0)'
    se = f" ± {1.96 * m['standard_error']:.2%}" if m.get('standard_error') else ''
    return f"{m['mean']:+.2%}{se} (n={m['n']})"


def report(summary: dict) -> str:
    lines = ['# v27/v28 price-edge tracking', '']
    if 'recommendation_history' in summary:
        info=summary['recommendation_history']
        lines += ['## Recommendation history and placed bets', '', info['note'], '',
                  'Latest-view tables below are simulated recommendations, not executed-bet ROI.']
        for source in ('value','cagey'):
            part=info[source]
            lines += [f"{source}: {part['recommendations']} captured recommendations; {part['graded']} graded; "
                      f"{part['distinct_fixtures']} distinct fixtures."]
        lines += ['Actual placed bets: '+summary.get('actual_bets',{}).get('status','NOT_RECORDED'), '']
    if summary.get('cagey_review'):
        lines += [f"> **CAGEY REVIEW**: {summary['correction_only_clv']['n']} graded correction-only value picks with "
                  f"mean CLV {summary['correction_only_clv']['mean']:+.2%}. Recommendation: set "
                  'cagey_correction_enabled to false (this report does not change it).', '']
    if summary.get('cagey_tier_review'):
        roi = summary['cagey_tier_roi']
        lines += [f"> **CAGEY TIER REVIEW**: {roi['n']} graded cagey-tier picks with realised ROI {_fmt(roi)}, interval "
                  'entirely below 0. Recommendation: set cagey_tier_enabled to false (this report does not change it).', '']
    if summary['stop_review']:
        lines += [f"> **STOP REVIEW**: {summary['clv']['n']} graded picks with mean CLV {summary['clv']['mean']:+.2%} "
                  '(below zero). Review the policy before relying on further picks.', '']
    lines += [f"Reviewed {summary['reviewed_at_utc']}. Frozen v27 picks: {summary['frozen_picks']}.", '',
              f"**Mean CLV vs Pinnacle close:** {_fmt(summary['clv'])}. **Flat-stake profit per bet:** {_fmt(summary['profit'])}.",
              f"STOP REVIEW rule: {summary['stop_review_rule']}.", '']
    for column, groups in summary['clv_by'].items():
        lines += [f'## CLV by {column}', '', '| group | mean CLV (n) |', '|---|---|']
        lines += [f'| {k} | {_fmt(v)} |' for k, v in groups.items()] or ['| none | n/a |']
        lines.append('')
    if summary.get('master_picks'):
        m = summary['master']
        lines += ['## Master shortlist (10 best bets per run)', '',
                  f"Frozen picks: {summary['master_picks']}; CLV {_fmt(m['clv'])}; realised profit per bet {_fmt(m['profit'])}.",
                  '', '| price flag | mean CLV (n) | realised profit per bet (n) |', '|---|---|---|']
        lines += [f"| {flag} | {_fmt(v['clv'])} | {_fmt(v['profit'])} |" for flag, v in m['by_price_flag'].items()]
        lines.append('')
    lines += new_master_report(summary)
    if 'both_tiers_clv_by' in summary:
        lines += ['## Both tiers (value and cagey)', '',
                  f"Cagey-tier picks frozen: {summary['cagey_tier_picks']}; CLV {_fmt(summary['cagey_tier']['clv'])}; "
                  f"realised profit per bet {_fmt(summary['cagey_tier']['profit'])}. Correction-only value picks: "
                  f"CLV {_fmt(summary['correction_only_clv'])}.",
                  f"Flags: {summary['cagey_review_rule']}; {summary['cagey_tier_review_rule']}.", '']
        by_rule = summary.get('cagey_tier_roi_by_rule') or {}
        if by_rule:
            active = summary.get('cagey_tier_active_rule')
            lines += ['### Cagey-tier realised profit per bet by rule', '',
                      '| rule | all picks | value-priced | below fair |', '|---|---|---|---|']
            lines += [f"| {rule}{' (active)' if rule == active else ''} | {_fmt(r['all'])} | "
                      f"{_fmt(r[PRICE_VALUE])} | {_fmt(r[PRICE_BELOW_FAIR])} |" for rule, r in by_rule.items()]
            lines += ['', 'Only the active rule\'s value-priced picks count toward CAGEY TIER REVIEW.', '']
        for column, groups in summary['both_tiers_clv_by'].items():
            profit = summary['both_tiers_profit_by'].get(column, {})
            lines += [f'### By {column}', '', '| group | mean CLV (n) | realised profit per bet (n) |', '|---|---|---|']
            lines += [f'| {k} | {_fmt(v)} | {_fmt(profit.get(k, {}))} |' for k, v in groups.items()] or ['| none | n/a | n/a |']
            lines.append('')
    t = summary['tagged_candidates']
    lines += ['## Tagged candidates (narrow-margin hypothesis)', '',
              f"Frozen tagged candidates: {t['frozen']} ({t['with_offered_price']} with an offered price).",
              f"1xBet edge vs fair at capture: {_fmt(t['edge_at_capture_1xbet'])}.",
              f"Return at the capture fair price, all tagged lines: {_fmt(t['return_at_capture_fair'])}; "
              f"plus lines only: {_fmt(t['return_at_capture_fair_plus_lines'])}.", '']
    lines += [f"- {k}: {_fmt(v)}" for k, v in t['by_tag'].items()]
    if 'correction_monitoring' in summary:
        lines += [''] + monitoring_report(summary['correction_monitoring'])
    lines += ['', summary['note']]
    return '\n'.join(lines) + '\n'
