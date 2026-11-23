"""Shadow corner list: one corner total per domestic fixture, recorded and graded, never bet.

Each forecast run writes `corners_shadow.csv`: for every domestic fixture with a corner-count forecast and a
fresh, complete Pinnacle corner-totals pair, the one line and side whose model probability gives the best
expected return at Pinnacle's price, among prices in (1.15, 2.20]. Every row is labelled "unvalidated, not bet"
with zero stake. The list is not part of the value shortlist, the cagey tier or either master, and nothing they
read comes from here.

Near kickoff a separate collector (its own request cap and folder, beside closing_odds.py) stores Pinnacle's
corner prices for these picks. The weekly review grades each fixture's latest pre-kickoff pick: win rate,
return per unit had it been staked, and closing-line value against Pinnacle's margin-free close (power method,
as closing_odds.py; clv = entry odds x fair closing probability - 1, clv_report's definition).

Corner probabilities come from count_markets (count-markets-nb2-v1), the existing count model; the offline
candidate K1 did not clearly beat it (evaluation/corners_candidate/).
"""
from __future__ import annotations

import csv
import hashlib
import json
import math
import re
from datetime import timedelta
from pathlib import Path

VERSION = 'corners-shadow-v1'
FILE = 'corners_shadow.csv'
LABEL = 'unvalidated, not bet'
ODDS_ABOVE, ODDS_MAX = 1.15, 2.20   # Pinnacle price must be in (1.15, 2.20]
MARKET_KEY = 'alternate_totals_corners'
BOOKMAKER = 'Pinnacle'
CLOSING_VERSION = 'corners-closing-v1'
CLOSING_DIR = Path('corners_shadow') / 'closing'
CLOSING_BUDGET = Path('corners_shadow') / 'request_budget.json'
CLOSING_DAILY_CAP = 40               # corner closing requests per UTC day (1 credit each)
CLOSING_MAX_REQUESTS_PER_FIXTURE = 2
PRE_KICKOFF_WINDOW_SECONDS = 6 * 60  # as closing_odds.py
MAX_QUOTE_AGE_SECONDS = 120          # as closing_odds.py
GRADES_DIR = Path('performance') / 'corners_shadow'
MIN_LEAD_MINUTES = 20                # as performance_tracking
COLUMNS = ('list_version', 'status', 'stake', 'generated_at_utc', 'league', 'home_team', 'away_team',
           'kickoff_utc', 'odds_event_id', 'model_home_team', 'model_away_team', 'market', 'side', 'line',
           'bookmaker', 'offered_decimal_odds', 'opposite_decimal_odds', 'quote_last_update_utc',
           'pinnacle_margin_free_probability', 'model_probability', 'expected_return', 'model_mean',
           'model_dispersion', 'model_version', 'priced_lines')


def requests_corners(league_key: str) -> bool:
    """Corner totals are requested for domestic leagues only; Pinnacle does not price UCL/UEL corners."""
    import league_registry
    league = league_registry.LEAGUES.get(league_key)
    return bool(league is not None and league.domestic)


def corner_offers(payload, as_of) -> list:
    """Complete same-book Pinnacle corner Over/Under pairs (count_markets.parse_quotes, corners only)."""
    import count_markets
    return [o for o in count_markets.parse_quotes(payload, as_of)
            if o.get('kind') == 'corners' and o.get('market_key') == MARKET_KEY]


# ---------------------------------------------------------------------------
# The per-run list
# ---------------------------------------------------------------------------

def _loads(value, default):
    if value is None or (isinstance(value, float) and math.isnan(value)) or value == '':
        return default
    try:
        return json.loads(value) if isinstance(value, str) else value
    except (TypeError, ValueError):
        return default


def pick(prediction: dict):
    """The fixture's best-expected-return Pinnacle corner line in (1.15, 2.20], or None."""
    import count_markets
    forecast = (_loads(prediction.get('count_model'), {}) or {}).get('corners')
    offers = [o for o in _loads(prediction.get('count_market_offers'), []) or []
              if o.get('kind') == 'corners' and o.get('bookmaker') == BOOKMAKER]
    if not forecast or not offers:
        return None
    try:
        mu, alpha = float(forecast['mu']), float(forecast['alpha'])
    except (KeyError, TypeError, ValueError):
        return None
    if not (math.isfinite(mu) and mu > 0 and math.isfinite(alpha) and alpha > 0):
        return None
    probabilities = count_markets.probabilities(mu, alpha, 'corners')
    candidates = []
    for offer in offers:
        price, opposite = float(offer['price']), float(offer['opposite_price'])
        if not ODDS_ABOVE < price <= ODDS_MAX:
            continue
        label = count_markets.market_label('corners', offer['side'], float(offer['line']))
        p = probabilities.get(label)
        if p is None:
            continue
        candidates.append((p * price - 1, -float(offer['line']), offer['side'] == 'Over', label, p, offer,
                           (1 / price) / (1 / price + 1 / opposite)))
    if not candidates:
        return None
    ev, _, _, label, p, offer, fair = max(candidates, key=lambda c: c[:3])
    return {'market': label, 'side': offer['side'], 'line': float(offer['line']), 'bookmaker': offer['bookmaker'],
            'offered_decimal_odds': float(offer['price']), 'opposite_decimal_odds': float(offer['opposite_price']),
            'quote_last_update_utc': offer.get('last_update_utc'), 'pinnacle_margin_free_probability': round(fair, 6),
            'model_probability': round(p, 6), 'expected_return': round(ev, 6), 'model_mean': round(mu, 6),
            'model_dispersion': round(alpha, 6), 'model_version': forecast.get('version'),
            'priced_lines': len({float(o['line']) for o in offers})}


def build(predictions, generated_at) -> list:
    """One row per domestic fixture that has a qualifying pick; deterministic order."""
    rows = []
    for prediction in predictions:
        chosen = pick(prediction)
        if chosen is None:
            continue
        rows.append({'list_version': VERSION, 'status': LABEL, 'stake': 0, 'generated_at_utc': generated_at,
                     **{k: prediction.get(k) for k in ('league', 'home_team', 'away_team', 'kickoff_utc',
                                                       'odds_event_id', 'model_home_team', 'model_away_team')},
                     **chosen})
    return sorted(rows, key=lambda r: (str(r['kickoff_utc']), str(r['league']), str(r['home_team'])))


def write_list(predictions, out_dir: Path, generated_at) -> list:
    """Write corners_shadow.csv (header only when there is no pick)."""
    rows = build(predictions, generated_at)
    with (Path(out_dir) / FILE).open('w', encoding='utf-8', newline='') as handle:
        writer = csv.DictWriter(handle, fieldnames=COLUMNS, lineterminator='\n')
        writer.writeheader()
        writer.writerows(rows)
    return rows


def capture_file(raw: Path, generated):
    """Archive the list only when it belongs to this exact generation."""
    from performance_tracking import read_csv, utc
    path = Path(raw) / FILE
    if not path.exists():
        return None
    rows = read_csv(path)
    if any(r.get('list_version') != VERSION or r.get('status') != LABEL or str(r.get('stake')) != '0'
           or utc(r.get('generated_at_utc')) != utc(generated) for r in rows):
        return None
    return path


def latest_picks(root: Path, archive) -> list:
    """Each fixture's pick from its latest pre-kickoff archived generation."""
    from performance_tracking import fixture_key, utc
    from price_edge_tracking import archived_tier_rows
    newest = {}
    for row in archived_tier_rows(root, archive, FILE):
        if row.get('list_version') != VERSION:
            continue
        key = fixture_key(row)
        if key not in newest or utc(row['snapshot_generated_utc']) >= utc(newest[key]['snapshot_generated_utc']):
            newest[key] = row
    return [newest[k] for k in sorted(newest)]


# ---------------------------------------------------------------------------
# Pre-kickoff corner prices (separate from closing_odds.py and its budget)
# ---------------------------------------------------------------------------

def _digest(data) -> str:
    return hashlib.sha256(json.dumps(data, sort_keys=True, separators=(',', ':'), allow_nan=False).encode()).hexdigest()


def normalize(source: dict, payload, observed, version: str = CLOSING_VERSION) -> dict:
    """Pinnacle corner pairs quoted within 120 s of an observation 0-6 minutes before kickoff."""
    from football_value_pipeline_v2_standalone import canonical_team_key, devig
    from performance_tracking import utc, number
    if not isinstance(payload, dict) or not isinstance(payload.get('bookmakers', []), list):
        raise ValueError('Malformed odds response')
    kick, pk = utc(source.get('kickoff_utc')), utc(payload.get('commence_time'))
    if (not kick or not pk or abs((pk - kick).total_seconds()) > 1
            or str(payload.get('id')) != str(source.get('odds_event_id'))
            or not 0 < (kick - observed).total_seconds() <= PRE_KICKOFF_WINDOW_SECONDS
            or any(canonical_team_key(str(payload.get(k, ''))) != canonical_team_key(str(source.get(k, '')))
                   for k in ('home_team', 'away_team'))):
        raise ValueError('Corner closing event/timing mismatch')
    quotes = []
    for book in payload.get('bookmakers', []):
        if not isinstance(book, dict) or str(book.get('key', '')).lower() != 'pinnacle':
            continue
        for market in book.get('markets', []) if isinstance(book.get('markets'), list) else []:
            if not isinstance(market, dict) or market.get('key') != MARKET_KEY:
                continue
            updated = utc(market.get('last_update') or book.get('last_update'))
            if not updated or not 0 <= (observed - updated).total_seconds() <= MAX_QUOTE_AGE_SECONDS or updated >= kick:
                continue
            pairs, duplicate = {}, set()
            for o in market.get('outcomes', []) if isinstance(market.get('outcomes'), list) else []:
                if not isinstance(o, dict):
                    continue
                side, price = str(o.get('name', '')).lower(), number(o.get('price'), min_value=1.000001)
                point = number(o.get('point'))
                if side not in ('over', 'under') or price is None or point is None or point % 1 != 0.5:
                    continue
                if side in pairs.setdefault(point, {}):
                    duplicate.add(point)
                pairs[point][side] = price
            for point in sorted(pairs):
                prices = pairs[point]
                if point in duplicate or set(prices) != {'over', 'under'} or not .98 <= sum(1 / v for v in prices.values()) <= 1.20:
                    continue
                fair = devig([prices['over'], prices['under']], method='power')
                for i, side in enumerate(('over', 'under')):
                    quotes.append({'line': point, 'side': side.capitalize(), 'decimal_odds': prices[side],
                                   'fair_probability': float(fair[i]), 'quote_last_update_utc': updated.isoformat()})
    fixture = {k: source.get(k) for k in ('league', 'home_team', 'away_team', 'kickoff_utc', 'odds_event_id')}
    return {'version': version, 'observed_at_utc': observed.isoformat(), 'fixture': fixture,
            'payload': payload, 'quotes': quotes}


def load_observations(root: Path, clock=None):
    """Stored observations whose hash and recomputed quotes still match; rejected file names separately."""
    from performance_tracking import utc
    rows, rejected = [], []
    for path in sorted((Path(root) / CLOSING_DIR).glob('*.json')):
        try:
            d = json.loads(path.read_text(encoding='utf-8'))
            if _digest(d) != path.stem or d.get('version') != CLOSING_VERSION:
                raise ValueError('Hash')
            observed = utc(d['observed_at_utc'])
            if not observed or (clock is not None and observed > clock):
                raise ValueError('Clock')
            if normalize(d['fixture'], d['payload'], observed)['quotes'] != d['quotes']:
                raise ValueError('Quote calculation')
            rows.append(d)
        except (ValueError, TypeError, KeyError, OSError):
            rejected.append(path.name)
    return rows, rejected


def _same_fixture(source, observations):
    from performance_tracking import utc
    return [o for o in observations if str(o['fixture'].get('odds_event_id')) == str(source.get('odds_event_id'))
            and utc(o['fixture'].get('kickoff_utc')) == utc(source.get('kickoff_utc'))]


def _quoted(source, observations) -> bool:
    line, side = float(source['line']), str(source['side'])
    return any(q['line'] == line and q['side'] == side for o in _same_fixture(source, observations) for q in o['quotes'])


_ARCHIVED_PICKS = {}  # per process: the archive cannot change during a collection session (~9 s to load)


def closing_targets(root: Path, clock) -> list:
    """Current and archived shadow picks (latest per fixture) kicking off within the pre-kickoff window."""
    from performance_tracking import fixture_key, read_csv, snapshots, utc
    from prediction_runs import resolve_raw
    key = str(Path(root).resolve())
    if key not in _ARCHIVED_PICKS:
        _ARCHIVED_PICKS[key] = latest_picks(root, snapshots(root))
    picks = {fixture_key(r): r for r in _ARCHIVED_PICKS[key]}
    current = Path(resolve_raw(Path(root) / 'raw')) / FILE
    for row in read_csv(current) if current.exists() else []:
        if row.get('list_version') == VERSION:
            picks[fixture_key(row)] = row
    out = []
    for row in picks.values():
        kick = utc(row.get('kickoff_utc'))
        if kick and row.get('odds_event_id') and 0 < (kick - clock).total_seconds() <= PRE_KICKOFF_WINDOW_SECONDS:
            out.append(row)
    return sorted(out, key=lambda r: (str(r['kickoff_utc']), str(r['odds_event_id'])))


def fetch(api, source):
    from football_value_pipeline_v2_standalone import THE_ODDS_API_BASE, LEAGUES
    event = str(source.get('odds_event_id', ''))
    if not re.fullmatch(r'[A-Za-z0-9_-]+', event):
        raise ValueError('Invalid odds event')
    league = next(l for l in LEAGUES.values() if l.name == source['league'])
    from odds_provider import event_request  # provider switch on: Pinnacle via the providers in order
    return api._get_json(f'{THE_ODDS_API_BASE}/sports/{league.odds_api_sport_key}/events/{event}/odds',
                         f'corners_closing_v1_{event}.json', ttl=timedelta(seconds=0), force_refresh=True,
                         allow_stale=False, params={'bookmakers': 'pinnacle', 'markets': MARKET_KEY,
                                                    'oddsFormat': 'decimal', 'dateFormat': 'iso'},
                         **event_request(api, league, source, (MARKET_KEY,), max_age_seconds=30))


def collect_closing(root: Path, api, clock=None, fetcher=None, low_credits=None) -> dict:
    """One pass: request Pinnacle corner prices for shadow picks in the pre-kickoff window.

    Own daily cap and folder; skipped entirely when credits are low (closing_odds.low_credits). Never touches
    closing_odds.py's observations or request budget."""
    from performance_tracking import load_json, now_utc, write_json
    root = Path(root)
    start = clock or now_utc()
    if low_credits is None:
        from closing_odds import low_credits as closing_low_credits
        low_credits = closing_low_credits(root, api)
    budget_path = root / CLOSING_BUDGET
    budget = load_json(budget_path, {})
    today = budget.get('date') == start.date().isoformat()
    used = budget.get('requests', 0) if today else 0
    # Requests per fixture (event id and kickoff), counted when made, so a failed or empty reply still counts.
    per_fixture = dict(budget.get('fixtures', {})) if today else {}
    status = {'checked_at_utc': start.isoformat(), 'requests': 0, 'written': 0, 'errors': [], 'eligible': 0}
    if low_credits:
        status['reason'] = 'LOW_CREDITS_SKIPPED'
        return status
    observations, _ = load_observations(root, start)
    for source in closing_targets(root, start):
        status['eligible'] += 1
        fixture = f"{source.get('odds_event_id')}|{source.get('kickoff_utc')}"
        if _quoted(source, observations) or per_fixture.get(fixture, 0) >= CLOSING_MAX_REQUESTS_PER_FIXTURE:
            continue
        if used >= CLOSING_DAILY_CAP:
            status['reason'] = 'DAILY_REQUEST_CAP_REACHED'
            break
        used += 1
        per_fixture[fixture] = per_fixture.get(fixture, 0) + 1
        status['requests'] += 1
        write_json(budget_path, {'date': start.date().isoformat(), 'requests': used, 'daily_request_cap': CLOSING_DAILY_CAP,
                                 'fixtures': per_fixture})
        try:
            payload = (fetcher or fetch)(api, source)
            observed = clock or now_utc()
            d = normalize(source, payload, observed)
            directory = root / CLOSING_DIR
            directory.mkdir(parents=True, exist_ok=True)
            path = directory / (_digest(d) + '.json')
            if not path.exists():
                with path.open('x', encoding='utf-8') as f:
                    json.dump(d, f, sort_keys=True, indent=2, allow_nan=False)
                    f.write('\n')
                status['written'] += 1
            observations.append(d)
        except Exception as exc:  # a shadow collector never stops the live one
            status['errors'].append({'event_id': str(source.get('odds_event_id')), 'error': type(exc).__name__})
            from odds_provider_health import OddsProviderError
            if isinstance(exc, OddsProviderError):
                break
    status.setdefault('reason', 'CHECKED_ELIGIBLE_FIXTURES' if status['eligible'] else 'NO_PICKS_IN_PRE_KICKOFF_WINDOW')
    write_json(root / 'corners_shadow' / 'collector_status.json', status)
    return status


def closing_quote(source, observations):
    """Latest pre-kickoff Pinnacle close for the pick's exact line and side, or None."""
    from performance_tracking import utc
    line, side = float(source['line']), str(source['side'])
    best = None
    for o in _same_fixture(source, observations):
        for q in o['quotes']:
            if q['line'] == line and q['side'] == side and (best is None or utc(o['observed_at_utc']) > utc(best[0])):
                best = (o['observed_at_utc'], q)
    return None if best is None else {'observed_at_utc': best[0], **best[1]}


# ---------------------------------------------------------------------------
# Weekly grading
# ---------------------------------------------------------------------------

def grade(row: dict, final, close) -> dict:
    """WON/LOST from the committed corner counts (count_markets.verified_total), return per unit, CLV."""
    import count_markets
    out = {k: row.get(k) for k in COLUMNS}
    out.update({'snapshot_generated_utc': row.get('snapshot_generated_utc'), 'result_status': 'PENDING',
                'total_corners': None, 'unit_return': None, 'closing_decimal_odds': None,
                'closing_fair_probability': None, 'clv_vs_pinnacle_fair': None})
    if close is not None:
        odds = float(row['offered_decimal_odds'])
        out.update(closing_decimal_odds=close['decimal_odds'], closing_fair_probability=round(close['fair_probability'], 6),
                   clv_vs_pinnacle_fair=round(odds * close['fair_probability'] - 1, 6))
    if final is None:
        return out
    total = count_markets.verified_total(row, final)
    if total is None:
        out['result_status'] = 'AWAITING_COUNT_RESULT'
        return out
    parsed = count_markets.parse_label(row.get('market'))
    won = bool(count_markets.outcome(*parsed, total))
    out.update(result_status='WON' if won else 'LOST', total_corners=total,
               unit_return=round(float(row['offered_decimal_odds']) - 1 if won else -1.0, 6))
    return out


def _week(kickoff) -> str:
    from performance_tracking import utc
    k = utc(kickoff)
    return f'{k.isocalendar().year}-W{k.isocalendar().week:02d}' if k else ''


def summary_block(rows: list) -> dict:
    graded = [r for r in rows if r['result_status'] in ('WON', 'LOST')]
    clv = [r['clv_vs_pinnacle_fair'] for r in rows if r['clv_vs_pinnacle_fair'] is not None]
    won = sum(r['result_status'] == 'WON' for r in graded)
    returns = sum(r['unit_return'] for r in graded)
    return {'picks': len(rows), 'graded': len(graded), 'won': won,
            'win_rate': round(won / len(graded), 4) if graded else None,
            'units_returned': round(returns, 4), 'return_per_unit': round(returns / len(graded), 4) if graded else None,
            'mean_odds': round(sum(float(r['offered_decimal_odds']) for r in graded) / len(graded), 4) if graded else None,
            'with_close': len(clv), 'mean_clv_vs_pinnacle_fair': round(sum(clv) / len(clv), 4) if clv else None,
            'positive_clv_share': round(sum(c > 0 for c in clv) / len(clv), 4) if clv else None,
            'pending': sum(r['result_status'] in ('PENDING', 'AWAITING_COUNT_RESULT') for r in rows)}


RULE_MIN_WEEKS = 2  # plan Phase 6: "after two weeks of graded picks"
RULE_MET, RULE_NOT_MET, RULE_TOO_EARLY = 'rule met', 'rule not met', 'not enough weeks yet'


def decision_rule(rows: list) -> dict:
    """The corners decision rule (docs/plan.md, Phase 6, fixed 18 Nov 2026), computed exactly as defined there.

    Over every graded pick (WON or LOST) that has a Pinnacle close: mean clv_vs_pinnacle_fair with a 95% interval
    that resamples whole kickoff ISO weeks (evaluation_diagnostics.week_mean: 2,000 draws, seed 136). Once graded
    picks span at least two kickoff weeks, the rule is met only if the mean is positive and the interval is clear of
    zero (lower bound above zero); with no interval (closes in fewer than two weeks) it is not met. Win rate and
    return are not used."""
    from evaluation_diagnostics import week_mean
    graded = [r for r in rows if r['result_status'] in ('WON', 'LOST')]
    closed = [r for r in graded if r['clv_vs_pinnacle_fair'] is not None]
    weeks = sorted({r['week'] for r in graded})
    stats = week_mean([r['clv_vs_pinnacle_fair'] for r in closed], [r['week'] for r in closed])
    interval = stats['interval_95']
    if len(weeks) < RULE_MIN_WEEKS:
        verdict = RULE_TOO_EARLY
    elif stats['mean'] is not None and stats['mean'] > 0 and interval is not None and interval[0] > 0:
        verdict = RULE_MET
    else:
        verdict = RULE_NOT_MET
    return {'graded_picks': len(graded), 'graded_with_close': len(closed),
            'graded_lacking_close': len(graded) - len(closed), 'graded_weeks': len(weeks),
            'weeks_with_close': stats['weeks'], 'mean_clv_vs_pinnacle_fair': stats['mean'],
            'interval_95': interval, 'verdict': verdict,
            'rule': 'plan Phase 6 (18 Nov 2026): after two weeks of graded picks, small stakes only if mean CLV against '
                    "Pinnacle's margin-free close across all graded corner picks is positive with its 95% interval "
                    '(whole weeks resampled) clear of zero; otherwise no bets, keep tracking, re-check after two more '
                    'weeks. Win rate and return do not decide.'}


def review(root: Path, archive, verified_for, clock) -> dict:
    """Grade every fixture's latest archived pick; write grades.csv, summary.json and report.md."""
    from performance_tracking import write_json
    root = Path(root)
    observations, rejected = load_observations(root, clock)
    rows = []
    for row in latest_picks(root, archive):
        match, _ = verified_for(row)
        rows.append({**grade(row, match, closing_quote(row, observations)), 'week': _week(row.get('kickoff_utc'))})
    weeks = {}
    for r in rows:
        weeks.setdefault(r['week'], []).append(r)
    summary = {'list_version': VERSION, 'status': LABEL, 'stake': 0, 'reviewed_at_utc': clock.isoformat(),
               'definition': 'latest pre-kickoff pick per fixture; return per unit had it been staked; '
                             'clv_vs_pinnacle_fair = entry odds x Pinnacle power-de-vigged closing probability - 1',
               'rejected_closing_observations': rejected, 'decision_rule': decision_rule(rows),
               'all': summary_block(rows),
               'positive_expected_return_at_entry': summary_block([r for r in rows if float(r['expected_return']) > 0]),
               'weeks': {w: summary_block(v) for w, v in sorted(weeks.items())}}
    out = root / GRADES_DIR
    out.mkdir(parents=True, exist_ok=True)
    columns = list(COLUMNS) + ['snapshot_generated_utc', 'week', 'result_status', 'total_corners', 'unit_return',
                               'closing_decimal_odds', 'closing_fair_probability', 'clv_vs_pinnacle_fair']
    with (out / 'grades.csv').open('w', encoding='utf-8', newline='') as handle:
        writer = csv.DictWriter(handle, fieldnames=columns, lineterminator='\n', extrasaction='ignore')
        writer.writeheader()
        writer.writerows(rows)
    write_json(out / 'summary.json', summary)
    (out / 'report.md').write_text(markdown(summary), encoding='utf-8', newline='\n')
    return summary


def markdown(summary: dict) -> str:
    def line(name, b):
        f = lambda v, fmt: '—' if v is None else fmt.format(v)  # noqa: E731
        return (f"| {name} | {b['picks']} | {b['graded']} | {f(b['win_rate'], '{:.1%}')} | {f(b['mean_odds'], '{:.2f}')} | "
                f"{f(b['return_per_unit'], '{:+.3f}')} | {b['with_close']} | {f(b['mean_clv_vs_pinnacle_fair'], '{:+.3f}')} | "
                f"{f(b['positive_clv_share'], '{:.0%}')} | {b['pending']} |")
    head = ['| | picks | graded | win rate | mean odds | return per unit | with close | mean CLV | CLV > 0 | pending |',
            '|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|']
    rule = summary['decision_rule']
    mean, interval = rule['mean_clv_vs_pinnacle_fair'], rule['interval_95']
    out = ['# Shadow corner list (unvalidated, not bet)', '',
           f"Zero stake: returns are what one unit per pick would have made. {summary['definition']}.", '',
           '## Decision rule (plan Phase 6)', '',
           f"**Verdict: {rule['verdict']}.**", '',
           f"- Graded picks: {rule['graded_picks']} over {rule['graded_weeks']} kickoff week(s); "
           f"{rule['graded_with_close']} with a Pinnacle close, {rule['graded_lacking_close']} lacking one.",
           f"- Mean CLV against Pinnacle's margin-free close: {'—' if mean is None else f'{mean:+.4f}'}; 95% interval, "
           f"whole weeks resampled ({rule['weeks_with_close']} week(s)): "
           f"{'—' if interval is None else f'[{interval[0]:+.4f}, {interval[1]:+.4f}]'}.",
           f"- Rule: {rule['rule']}", '',
           *head, line('All', summary['all']), line('Positive expected return at entry',
                                                   summary['positive_expected_return_at_entry']), '',
           '## By kickoff week', '', *head]
    out += [line(w, b) for w, b in summary['weeks'].items()]
    return '\n'.join(out) + '\n'
