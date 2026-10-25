"""bet365 prices against Pinnacle's margin-free probability at one capture time.

A separate, clearly labelled list; never merged into any shortlist. It reads
only odds responses the pipeline already requests, so it adds no API calls.
Both quotes come from the same response (same capture instant) and must each
pass the shared live-quote freshness window. No price is ever synthesised.
"""
from __future__ import annotations

import json
import math
from datetime import timedelta

VERSION = 'bet365-vs-pinnacle-v1'
TITLE = 'bet365 vs Pinnacle'
FILE = 'bet365_vs_pinnacle.csv'
MIN_EDGE = .02
MIN_LEAD_MINUTES = 20
WINDOW_HOURS = 48
COLUMNS = ['list', 'list_version', 'generated_at_utc', 'league', 'home_team', 'away_team',
           'kickoff_utc', 'fixture_id', 'odds_event_id', 'market', 'selection',
           'bet365_decimal_odds', 'pinnacle_decimal_odds', 'pinnacle_fair_probability',
           'ev_vs_pinnacle_fair', 'ev_basis', 'devig_method', 'capture_utc',
           'bet365_last_update_utc', 'pinnacle_last_update_utc', 'bet365_quote_age_seconds',
           'pinnacle_quote_age_seconds', 'quote_skew_seconds', 'min_edge',
           'closing_tracking', 'execution_status']


def is_bet365(book):
    # bet365_au is a different, AFL/NRL-only feed; accept the football book only.
    return str(book.get('key', '')).casefold() == 'bet365' or str(book.get('title', '')).strip().casefold() == 'bet365'


def _price(value):
    try:
        price = float(value)
    except (TypeError, ValueError):
        return None
    return price if math.isfinite(price) and price > 1 else None


def _point(value):
    try:
        point = float(value)
    except (TypeError, ValueError):
        return None
    return point if math.isfinite(point) else None


def book_groups(book, home, away, clock):
    """Complete, coherent, fresh same-book outcome sets: {group: (prices, updated)}."""
    from football_value_pipeline_v2_standalone import canonical_team_key
    from quote_freshness import quote_is_fresh, quote_utc
    from asian_handicap import LINES, label as handicap_label
    groups = {}
    markets = book.get('markets')
    for market in markets if isinstance(markets, list) else []:
        if not isinstance(market, dict) or not isinstance(market.get('outcomes'), list):
            continue
        updated = market.get('last_update') or book.get('last_update')
        if not quote_is_fresh(updated, clock):
            continue
        key, found, duplicate = market.get('key'), {}, set()

        def put(group, selection, price):
            if price is None:
                return
            if selection in found.setdefault(group, {}):
                duplicate.add(group)
            found[group][selection] = price
        for o in market['outcomes']:
            if not isinstance(o, dict):
                continue
            name, price, point = str(o.get('name', '')).strip(), _price(o.get('price')), _point(o.get('point'))
            if key == 'h2h' and point is None:
                side = ('draw' if name.casefold() == 'draw' else
                        'home' if canonical_team_key(name) == canonical_team_key(home) else
                        'away' if canonical_team_key(name) == canonical_team_key(away) else None)
                if side:
                    put('h2h', side, price)
            elif key in ('totals', 'alternate_totals') and point is not None and name.casefold() in ('over', 'under'):
                put(f'totals_{point:g}', f"{name.casefold()}_{f'{point:g}'.replace('.', '_')}", price)
            elif key == 'btts' and name.casefold() in ('yes', 'no'):
                put('btts', 'btts_'+name.casefold(), price)
            elif key in ('spreads', 'alternate_spreads', 'draw_no_bet'):
                point = 0. if key == 'draw_no_bet' else point
                side = ('home' if canonical_team_key(name) == canonical_team_key(home) else
                        'away' if canonical_team_key(name) == canonical_team_key(away) else None)
                if side is None or point is None:
                    continue
                home_line = point if side == 'home' else -point
                if home_line not in LINES:
                    continue
                put(f'ah_{home_line:+.2f}', handicap_label(side, point), price)
            elif key == 'double_chance' and point is None:
                for selection, names in (('home_draw', (f'{home} or Draw', f'Draw or {home}', f'{home}/Draw', f'Draw/{home}', '1X')),
                                         ('draw_away', (f'{away} or Draw', f'Draw or {away}', f'{away}/Draw', f'Draw/{away}', 'X2')),
                                         ('home_away', (f'{home} or {away}', f'{away} or {home}', f'{home}/{away}', f'{away}/{home}', '12'))):
                    if name.casefold() in {n.casefold() for n in names}:
                        put('double_chance', selection, price)
        for group, prices in found.items():
            size = 3 if group in ('h2h', 'double_chance') else 2
            if group in duplicate or len(prices) != size:
                continue
            overround = sum(1/p for p in prices.values())
            low, high = (1.98, 2.40) if group == 'double_chance' else (.98, 1.20)
            if not low <= overround <= high:
                continue
            previous = groups.get(group)
            if previous is None or quote_utc(updated) > quote_utc(previous[1]):
                groups[group] = (prices, updated)
    return groups


def fair_probabilities(groups):
    """Pinnacle margin removal: power for exclusive sets, 1X2 sums for double chance."""
    from football_value_pipeline_v2_standalone import devig
    fair = {}
    for group, (prices, updated) in groups.items():
        if group == 'double_chance':
            continue
        names = list(prices)
        values = devig([prices[n] for n in names], method='power')
        if any(v is None or not 0 < v < 1 for v in values):
            continue
        method = 'power_complete_1x2' if group == 'h2h' else 'power_two_way'
        fair.update({n: (float(v), prices[n], updated, method) for n, v in zip(names, values)})
    if 'h2h' in groups:
        hda = {k: fair[k] for k in ('home', 'draw', 'away') if k in fair}
        if len(hda) == 3:
            stamp = groups['h2h'][1]
            for selection, sides in (('home_draw', ('home', 'draw')), ('draw_away', ('draw', 'away')),
                                     ('home_away', ('home', 'away'))):
                # Pinnacle DC price kept for display when quoted; fair comes from 1X2.
                price = groups.get('double_chance', ({}, None))[0].get(selection)
                fair[selection] = (sum(hda[s][0] for s in sides), price, stamp, 'power_1x2_sum')
    return fair


LABELS = {'home': 'Home win', 'draw': 'Draw', 'away': 'Away win', 'btts_yes': 'Both Teams to Score - Yes',
          'btts_no': 'Both Teams to Score - No', 'home_draw': 'Double Chance 1X',
          'draw_away': 'Double Chance X2', 'home_away': 'Double Chance 12'}


def market_label(selection):
    if selection in LABELS:
        return LABELS[selection]
    if selection.startswith(('over_', 'under_')):
        side, line = selection.split('_', 1)
        return f"{side.title()} {line.replace('_', '.')}"
    return selection


def compare_event(payload, clock):
    """Every bet365 selection with a fresh Pinnacle fair probability; no edge filter."""
    from quote_freshness import quote_clock, quote_utc
    if not isinstance(payload, dict) or not isinstance(payload.get('bookmakers'), list):
        return []
    clock = quote_clock(clock)
    home, away = payload.get('home_team'), payload.get('away_team')
    if not isinstance(home, str) or not isinstance(away, str):
        return []
    books = [b for b in payload['bookmakers'] if isinstance(b, dict)]
    pinnacle = [b for b in books if str(b.get('key', '')).casefold() == 'pinnacle']
    bet365 = [b for b in books if is_bet365(b)]
    if len(pinnacle) != 1 or len(bet365) != 1:
        return []
    fair = fair_probabilities(book_groups(pinnacle[0], home, away, clock))
    rows = []
    for group, (prices, updated) in sorted(book_groups(bet365[0], home, away, clock).items()):
        for selection, price in sorted(prices.items()):
            if selection not in fair:
                continue
            p, pin_price, pin_updated, method = fair[selection]
            b_at, p_at = quote_utc(updated), quote_utc(pin_updated)
            # Only half-ball lines (x.5) settle as a plain win or loss.
            split = selection.startswith('Asian Handicap') and round(float(selection.rsplit(' ', 1)[1]) * 4) % 4 != 2
            rows.append({'event_id': str(payload.get('id', '')), 'market': market_label(selection),
                'selection': selection, 'bet365_decimal_odds': price, 'pinnacle_decimal_odds': pin_price,
                'pinnacle_fair_probability': p, 'ev_vs_pinnacle_fair': p * price - 1,
                'ev_basis': ('two_way_fair_excluding_refund_or_split' if split else 'full_win_or_loss'),
                'devig_method': method, 'capture_utc': clock.isoformat(),
                'bet365_last_update_utc': b_at.isoformat(), 'pinnacle_last_update_utc': p_at.isoformat(),
                'bet365_quote_age_seconds': (clock - b_at).total_seconds(),
                'pinnacle_quote_age_seconds': (clock - p_at).total_seconds(),
                'quote_skew_seconds': (b_at - p_at).total_seconds()})
    return rows


def merge(*encoded):
    """Union of comparison lists; the newer capture wins per selection."""
    merged = {}
    for value in encoded:
        try:
            rows = json.loads(value) if isinstance(value, str) else (value or [])
        except ValueError:
            rows = []
        for row in rows if isinstance(rows, list) else []:
            key = row.get('selection')
            if key and (key not in merged or row['capture_utc'] >= merged[key]['capture_utc']):
                merged[key] = row
    return json.dumps(sorted(merged.values(), key=lambda r: r['selection']), sort_keys=True, allow_nan=False)


def build_list(predictions, generated):
    """Rows clearing MIN_EDGE for fixtures 20 minutes to 48 hours ahead."""
    from performance_tracking import utc
    from quote_freshness import quote_is_fresh
    clock = utc(generated)
    rows = []
    for source in predictions:
        kick = utc(source.get('kickoff_utc'))
        if clock is None or kick is None or not (timedelta(minutes=MIN_LEAD_MINUTES) <= kick - clock
                                                <= timedelta(hours=WINDOW_HOURS)):
            continue
        try:
            quotes = json.loads(source.get('bet365_pinnacle_quotes') or '[]')
        except (TypeError, ValueError):
            continue
        for q in quotes:
            if (str(q.get('event_id')) != str(source.get('odds_event_id')) or q['ev_vs_pinnacle_fair'] < MIN_EDGE
                    or not quote_is_fresh(q['bet365_last_update_utc'], clock)
                    or not quote_is_fresh(q['pinnacle_last_update_utc'], clock)):
                continue
            rows.append({**{k: source.get(k) for k in ('league', 'home_team', 'away_team', 'kickoff_utc',
                                                       'fixture_id', 'odds_event_id')},
                         **{k: q[k] for k in COLUMNS if k in q}, 'list': TITLE, 'list_version': VERSION,
                         'generated_at_utc': clock.isoformat(), 'min_edge': MIN_EDGE,
                         'closing_tracking': 'Pinnacle fair and bet365 price collected near kickoff',
                         'execution_status': 'unverified_feed_quote; not part of any shortlist'})
    return sorted(rows, key=lambda r: (-r['ev_vs_pinnacle_fair'], str(r['kickoff_utc']), r['selection']))


def write_list(predictions, raw, generated):
    from performance_tracking import write_csv
    rows = build_list(predictions, generated)
    write_csv(raw/FILE, rows, COLUMNS)
    return rows


def capture_file(raw, generated):
    """Archive only a list bound to this exact generation instant."""
    from performance_tracking import read_csv, utc
    path = raw/FILE
    if not path.exists():
        return None
    rows = read_csv(path)
    if any(r.get('list_version') != VERSION or utc(r.get('generated_at_utc')) != utc(generated) for r in rows):
        return None
    return path


def frozen_entries(root, archive):
    """First pre-kickoff archived entry per fixture/selection, with its snapshot."""
    from performance_tracking import fixture_key, read_csv, utc
    frozen = {}
    for meta, _, _ in archive:
        path = root/'performance'/'snapshots'/meta['git_commit_sha'][:16]/FILE
        if FILE not in meta.get('sha256', {}) or not path.exists():
            continue
        captured, generated = utc(meta['captured_at_utc']), utc(meta['generated_at_utc'])
        for row in read_csv(path):
            kick = utc(row.get('kickoff_utc'))
            if kick is None or max(captured, generated) > kick - timedelta(minutes=MIN_LEAD_MINUTES):
                continue
            frozen.setdefault((fixture_key(row), row['selection']),
                {**row, 'snapshot_commit': meta['git_commit_sha'], 'snapshot_captured_utc': meta['captured_at_utc']})
    return list(frozen.values())
