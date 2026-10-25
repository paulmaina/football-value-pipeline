"""Corner and card total models: negative-binomial (NB2) regression on lagged team form.

Inputs are football-data.co.uk match statistics only (HC, AC, HY, AY, HR, AR,
HF, AF, HS, AS, HST, AST). Every feature for a match uses results from earlier
calendar days only. Validation reuses the goal-market reliability rules and
thresholds unchanged.

No historical corner or card prices exist, so validation covers probability
accuracy only; it says nothing about profitability (an "unproven edge").
"""
from __future__ import annotations

import math
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.optimize import minimize
from scipy.special import gammaln
from scipy.stats import nbinom

VERSION = 'count-markets-nb2-v1'
# Production leagues per market. Pinnacle quotes corner totals in these five
# (Odds API check, 2026-10-24). It also quotes card totals in Bundesliga, Serie A
# and Ligue 1, but settles them as bookings (yellow 1, red 2, the second yellow
# of a dismissal excluded). football-data.co.uk cannot reproduce that total: it
# records second-yellow dismissals differently by country and does not separate
# them from straight reds. Cards stay out of production until data supports it.
LEAGUES = {'corners': ('EPL', 'LaLiga', 'Bundesliga', 'SerieA', 'Ligue1'),
           'cards': ()}
CARD_SETTLEMENT_GAP = ('Pinnacle settles card totals as bookings (yellow 1, red 2, second yellow excluded); '
                       'football-data.co.uk yellow/red counts cannot reproduce that total')
ODDS_MARKETS = {'corners': 'alternate_totals_corners', 'cards': 'alternate_totals_cards'}
LINES = {'corners': (7.5, 8.5, 9.5, 10.5, 11.5, 12.5), 'cards': (2.5, 3.5, 4.5, 5.5, 6.5)}
GROUPS = {'corners': 'Corners', 'cards': 'Cards'}
# Each card counts once: yellow cards plus red cards as football-data.co.uk
# reports them. This is not the bookmaker's settlement total (CARD_SETTLEMENT_GAP).
TOTALS = {'corners': (('HC',), ('AC',)), 'cards': (('HY', 'HR'), ('AY', 'AR'))}
# Supporting statistics: shots for corners, fouls for cards.
SUPPORT = {'corners': ('HS', 'AS'), 'cards': ('HF', 'AF')}
HALF_LIFE_MATCHES = 10
PRIOR_MATCHES = 3.0
L2 = 1.0
MIN_TRAIN = 500
STEP_DAYS = 56
UNPROVEN_EDGE = 'UNPROVEN EDGE: probability-only validation; no historical corner/card odds'


def market_label(kind, side, line):
    return f'{GROUPS[kind]} {side} {line:.1f}'


def parse_label(label):
    """'Corners Over 9.5' -> ('corners', 'Over', 9.5); None for other markets."""
    parts = str(label).split(' ')
    kinds = {v: k for k, v in GROUPS.items()}
    if len(parts) != 3 or parts[0] not in kinds or parts[1] not in ('Over', 'Under'):
        return None
    try:
        line = float(parts[2])
    except ValueError:
        return None
    return (kinds[parts[0]], parts[1], line) if line in LINES[kinds[parts[0]]] else None


def outcome(kind, side, line, total):
    return total > line if side == 'Over' else total < line


def _side_total(frame, columns):
    return sum(pd.to_numeric(frame[c], errors='coerce') for c in columns)


def prepare(history, kind):
    """Completed matches with the required statistics, ordered by date."""
    needed = [c for side in TOTALS[kind] for c in side] + list(SUPPORT[kind])
    frame = history.copy()
    if not set(needed) <= set(frame.columns):
        return frame.iloc[0:0].assign(date=pd.Series(dtype='datetime64[ns]'))
    frame['date'] = pd.to_datetime(frame['Date'], dayfirst=True, errors='coerce').dt.normalize()
    frame['home_count'] = _side_total(frame, TOTALS[kind][0])
    frame['away_count'] = _side_total(frame, TOTALS[kind][1])
    frame['home_support'] = pd.to_numeric(frame[SUPPORT[kind][0]], errors='coerce')
    frame['away_support'] = pd.to_numeric(frame[SUPPORT[kind][1]], errors='coerce')
    keep = (frame.date.notna() & frame.HomeTeam.notna() & frame.AwayTeam.notna()
            & frame[['home_count', 'away_count', 'home_support', 'away_support']].notna().all(axis=1))
    frame = frame.loc[keep].sort_values(['date', 'HomeTeam', 'AwayTeam'], kind='stable').reset_index(drop=True)
    frame['total'] = (frame.home_count + frame.away_count).astype(int)
    return frame[['date', 'HomeTeam', 'AwayTeam', 'home_count', 'away_count', 'home_support', 'away_support', 'total']]


class _Form:
    """Exponentially weighted team form, shrunk toward the league mean."""
    STATS = ('count_for', 'count_against', 'support_for', 'support_against')

    def __init__(self):
        self.decay = 0.5 ** (1 / HALF_LIFE_MATCHES)
        self.teams = {}
        self.league = dict.fromkeys(self.STATS, None)
        self.observed = 0

    def features(self, team):
        sums, weight = self.teams.get(team, (dict.fromkeys(self.STATS, 0.), 0.))
        return {s: (sums[s] + PRIOR_MATCHES*self.league[s]) / (weight + PRIOR_MATCHES) for s in self.STATS}

    def update(self, team, values):
        sums, weight = self.teams.get(team, (dict.fromkeys(self.STATS, 0.), 0.))
        self.teams[team] = ({s: self.decay*sums[s] + values[s] for s in self.STATS}, self.decay*weight + 1)
        # A running mean at first, then slow league drift (a season is ~760 team-matches).
        self.observed += 1
        rate = max(0.005, 1/self.observed)
        for s in self.STATS:
            self.league[s] = values[s] if self.league[s] is None else (1-rate)*self.league[s] + rate*values[s]


def _design(home, away, league):
    def ratio(value, mean):
        return math.log(max(value, 1e-6) / max(mean, 1e-6))
    return [ratio(home['count_for'], league['count_for']), ratio(home['count_against'], league['count_against']),
            ratio(away['count_for'], league['count_for']), ratio(away['count_against'], league['count_against']),
            ratio(home['support_for'], league['support_for']), ratio(home['support_against'], league['support_against']),
            ratio(away['support_for'], league['support_for']), ratio(away['support_against'], league['support_against'])]


def features(matches, fixtures=None):
    """Pre-match design rows for every match (and optional future fixtures).

    Each calendar day's matches see only earlier days' results. Returns the
    match design, its log league-mean offset, and the same for fixtures.
    """
    form = _Form()
    rows, offsets = [], []
    for _, day in matches.groupby('date', sort=True):
        if not form.league['count_for']:
            rows.extend([None]*len(day))
            offsets.extend([None]*len(day))
        else:
            for m in day.itertuples():
                rows.append(_design(form.features(m.HomeTeam), form.features(m.AwayTeam), form.league))
                offsets.append(math.log(2*form.league['count_for']))
        for m in day.itertuples():
            form.update(m.HomeTeam, {'count_for': m.home_count, 'count_against': m.away_count,
                                     'support_for': m.home_support, 'support_against': m.away_support})
            form.update(m.AwayTeam, {'count_for': m.away_count, 'count_against': m.home_count,
                                     'support_for': m.away_support, 'support_against': m.home_support})
    future = []
    for home, away in (fixtures or []):
        future.append((_design(form.features(home), form.features(away), form.league),
                       math.log(2*form.league['count_for'])) if form.league['count_for'] else None)
    return rows, offsets, future


def _negative_log_likelihood(params, x, offset, y):
    beta, log_alpha = params[:-1], params[-1]
    mu = np.exp(np.clip(offset + x @ beta, -10, 10))
    r = 1 / math.exp(log_alpha)
    ll = (gammaln(y + r) - gammaln(r) - gammaln(y + 1) + r*np.log(r/(r+mu)) + y*np.log(mu/(r+mu)))
    return -ll.sum() + L2*float(beta[1:] @ beta[1:])


def fit(x, offset, y):
    """NB2 regression: log mu = offset + b0 + b.x; variance mu + alpha*mu^2."""
    x = np.column_stack([np.ones(len(x)), np.asarray(x, dtype=float)])
    start = np.zeros(x.shape[1] + 1)
    start[-1] = math.log(0.05)
    result = minimize(_negative_log_likelihood, start, args=(x, np.asarray(offset, float), np.asarray(y, float)),
                      method='L-BFGS-B', bounds=[(None, None)]*x.shape[1] + [(math.log(1e-4), math.log(5.))])
    if not result.success and not np.all(np.isfinite(result.x)):
        raise RuntimeError('Count model did not converge')
    return {'beta': result.x[:-1].tolist(), 'alpha': float(math.exp(result.x[-1]))}


def mean(model, design, offset):
    return float(math.exp(min(10., max(-10., offset + model['beta'][0] + float(np.dot(model['beta'][1:], design))))))


def probabilities(mu, alpha, kind):
    """Over/Under probability for every half line (no pushes on half lines)."""
    r = 1 / alpha
    dist = nbinom(r, r/(r+mu))
    result = {}
    for line in LINES[kind]:
        under = float(dist.cdf(math.floor(line)))
        result[market_label(kind, 'Under', line)] = under
        result[market_label(kind, 'Over', line)] = 1 - under
    return result


def walk_forward(history, kind, min_train=MIN_TRAIN, step_days=STEP_DAYS):
    """Expanding-window forecasts, refit every step; same windows as the goal validation."""
    matches = prepare(history, kind)
    rows, offsets, _ = features(matches)
    usable = np.array([r is not None for r in rows])
    if len(matches) <= min_train:
        return pd.DataFrame()
    start = matches.date.iloc[min_train].normalize()
    end = matches.date.max() + pd.Timedelta(days=1)
    out = []
    for edge in pd.date_range(start, end, freq=f'{int(step_days)}D'):
        train = np.flatnonzero(usable & (matches.date < edge).to_numpy())
        test = np.flatnonzero(usable & (matches.date >= edge).to_numpy()
                              & (matches.date < edge + pd.Timedelta(days=step_days)).to_numpy())
        if not len(test) or len(train) < min_train:
            continue
        model = fit([rows[i] for i in train], [offsets[i] for i in train], matches.total.to_numpy()[train])
        for i in test:
            mu = mean(model, rows[i], offsets[i])
            out.append({'date': matches.date.iloc[i], 'home_team': matches.HomeTeam.iloc[i],
                        'away_team': matches.AwayTeam.iloc[i], 'total': int(matches.total.iloc[i]),
                        'mu': mu, 'alpha': model['alpha'], **probabilities(mu, model['alpha'], kind)})
    return pd.DataFrame(out)


def _count_log_loss(frame, mu, alpha):
    r = 1/np.asarray(alpha, float)
    mu = np.asarray(mu, float)
    return float(-np.mean(nbinom.logpmf(frame.total.to_numpy(), r, r/(r+mu))))


def evaluate(forecasts, kind, min_dev=80, min_audit=25, audit_fraction=0.25):
    """Per-market reliability with the goal-market rules and thresholds unchanged."""
    from goal_market_validation import (HIGH_PROBABILITY_THRESHOLDS, MAX_OVERALL_BRIER_EXCESS, _binary_stats,
                                        _high_confidence_group, _reliability_bins)
    report = {'version': VERSION, 'kind': kind, 'source': 'chronological_expanding_window',
              'development_fraction': 1 - audit_fraction, 'probability_only': True,
              'historical_prices_available': False, 'warning': UNPROVEN_EDGE, 'markets': {}}
    labels = [market_label(kind, side, line) for line in LINES[kind] for side in ('Over', 'Under')]
    if forecasts.empty:
        for label in labels:
            report['markets'][label] = {'status': 'INSUFFICIENT_HISTORY', 'development': {'n': 0},
                                        'audit': {'n': 0}, 'confidence_penalty': None, 'high_confidence': {}}
        return report
    ordered = forecasts.sort_values('date', kind='stable')
    split = min(max(int(len(ordered)*(1-audit_fraction)), 1), len(ordered)-1)
    split_date = ordered.iloc[split]['date']
    dev, audit = ordered.loc[ordered.date < split_date], ordered.loc[ordered.date >= split_date]
    # Count-distribution accuracy against a constant league-rate NB (development mean).
    base_mu = float(dev.total.mean()) if len(dev) else float('nan')
    base_var = float(dev.total.var()) if len(dev) > 1 else float('nan')
    base_alpha = max(1e-4, (base_var - base_mu)/base_mu**2) if base_mu == base_mu else 1e-4
    report['count_accuracy'] = {
        part: {'n': len(frame), 'mean_total': float(frame.total.mean()) if len(frame) else None,
               'model_log_loss': _count_log_loss(frame, frame.mu, frame.alpha) if len(frame) else None,
               'constant_rate_log_loss': (_count_log_loss(frame, np.full(len(frame), base_mu),
                                                          np.full(len(frame), base_alpha)) if len(frame) else None)}
        for part, frame in (('development', dev), ('audit', audit))}
    report['split_date'] = pd.Timestamp(split_date).date().isoformat()
    report['first_forecast_date'] = pd.Timestamp(ordered.date.iloc[0]).date().isoformat()
    report['last_forecast_date'] = pd.Timestamp(ordered.date.iloc[-1]).date().isoformat()
    for label in labels:
        _, side, line = parse_label(label)
        def pack(frame):
            return (frame[label].to_numpy(float),
                    np.array([outcome(kind, side, line, t) for t in frame.total], dtype=float))
        dev_p, dev_y = pack(dev)
        audit_p, audit_y = pack(audit)
        dev_stats, audit_stats = _binary_stats(dev_p, dev_y), _binary_stats(audit_p, audit_y)
        bias = max(0.0, float(dev_stats.get('overconfidence', 0)))
        penalty = bias*len(dev_p)/(len(dev_p)+100.0) if len(dev_p) else None
        enough = len(dev_p) >= min_dev and len(audit_p) >= min_audit
        audit_is_ok = (enough and abs(audit_stats['overconfidence']) <= 0.12
                       and audit_stats['brier'] <= audit_stats['baseline_brier'] + MAX_OVERALL_BRIER_EXCESS)
        report['markets'][label] = {
            'status': 'RELIABLE_FOR_RANKING' if audit_is_ok else 'INSUFFICIENT_HISTORY' if not enough
                      else 'UNRELIABLE_AUDIT',
            'development': dev_stats, 'audit': audit_stats,
            'high_confidence': {f'{int(t*100)}plus': _high_confidence_group(dev_p, dev_y, audit_p, audit_y, t)
                                for t in HIGH_PROBABILITY_THRESHOLDS},
            'development_bins': _reliability_bins(dev_p, dev_y), 'audit_bins': _reliability_bins(audit_p, audit_y),
            'confidence_penalty': float(penalty) if penalty is not None else None}
    return report


def validate_league(history, league_key):
    """Reports for every count market this league quotes; {} when none."""
    return {kind: evaluate(walk_forward(history, kind), kind) for kind in LEAGUES if league_key in LEAGUES[kind]}


def forecast_fixtures(history, league_key, fixtures):
    """{kind: {'mu', 'alpha'}} per (home, away) training-name pair; {} when unavailable."""
    result = [dict() for _ in fixtures]
    for kind in LEAGUES:
        if league_key not in LEAGUES[kind]:
            continue
        matches = prepare(history, kind)
        rows, offsets, future = features(matches, fixtures)
        usable = [i for i, r in enumerate(rows) if r is not None]
        if len(usable) < MIN_TRAIN:
            continue
        model = fit([rows[i] for i in usable], [offsets[i] for i in usable], matches.total.to_numpy()[usable])
        for out, item in zip(result, future):
            if item is None:
                continue
            out[kind] = {'mu': mean(model, *item), 'alpha': model['alpha'], 'version': VERSION}
    return result


def load_history(cache_dir, division, seasons=6):
    """The committed football-data.co.uk seasons for one division, oldest first."""
    files = sorted(Path(cache_dir).glob(f'????_{division}.csv'))[-seasons:]
    frames = []
    for path in files:
        try:
            frames.append(pd.read_csv(path, encoding='utf-8-sig'))
        except UnicodeDecodeError:
            frames.append(pd.read_csv(path, encoding='latin-1'))
    return pd.concat(frames, ignore_index=True) if frames else pd.DataFrame()


def parse_quotes(payload, as_of):
    """Complete same-book Over/Under pairs on validated half lines; no synthetic prices."""
    from asian_handicap import bookmaker
    from quote_freshness import quote_is_fresh
    if not isinstance(payload, dict) or not isinstance(payload.get('bookmakers', []), list):
        return []
    if payload.get('commence_time') is not None:
        kick = pd.to_datetime(payload['commence_time'], utc=True, errors='coerce')
        if pd.isna(kick) or as_of is None or kick <= pd.Timestamp(as_of):
            return []
    kinds = {v: k for k, v in ODDS_MARKETS.items()}
    offers = {}
    for book in payload.get('bookmakers', []):
        if not isinstance(book, dict) or not isinstance(book.get('markets', []), list):
            continue
        name = bookmaker(book.get('title') or book.get('key'))
        if name is None:
            continue
        for market in book.get('markets', []):
            if not isinstance(market, dict) or market.get('key') not in kinds:
                continue
            kind = kinds[market['key']]
            stamp = market.get('last_update') or book.get('last_update')
            if not quote_is_fresh(stamp, as_of) or not isinstance(market.get('outcomes', []), list):
                continue
            pairs, invalid = {}, set()
            for outcome in market['outcomes']:
                try:
                    side, line, price = outcome['name'], float(outcome['point']), float(outcome['price'])
                    if (isinstance(outcome['price'], bool) or side not in ('Over', 'Under')
                            or not math.isfinite(price) or price <= 1):
                        raise ValueError('Invalid outcome')
                except (ValueError, TypeError, KeyError):
                    continue
                indexed = pairs.setdefault(line, {})
                if side in indexed:
                    invalid.add(line)
                indexed[side] = price
            for line, prices in pairs.items():
                if line in invalid or line not in LINES[kind] or set(prices) != {'Over', 'Under'}:
                    continue
                if not .98 <= sum(1/p for p in prices.values()) <= 1.20:
                    continue
                for side, other in (('Over', 'Under'), ('Under', 'Over')):
                    item = {'kind': kind, 'side': side, 'line': line, 'price': prices[side],
                            'opposite_price': prices[other], 'bookmaker': name, 'last_update_utc': stamp,
                            'market_key': market['key'], 'quote_source': 'The Odds API'}
                    identity = (kind, side, line, name)
                    previous = offers.get(identity)
                    if previous is None or (str(stamp), item['price']) > (str(previous['last_update_utc']), previous['price']):
                        offers[identity] = item
    return sorted(offers.values(), key=lambda r: (r['kind'], r['line'], r['side'], r['bookmaker']))


_HISTORY = {}


def _committed_history(cache_dir, division):
    key = (str(Path(cache_dir).resolve()), division)
    if key not in _HISTORY:
        frame = load_history(cache_dir, division, seasons=10)
        if len(frame):
            frame = frame.assign(_date=pd.to_datetime(frame['Date'], dayfirst=True, errors='coerce'))
        _HISTORY[key] = frame
    return _HISTORY[key]


def verified_total(row, final, cache_dir=None):
    """Settled total for a shortlisted count market, or None until it can be verified.

    The total comes from the committed football-data.co.uk row for the same
    model teams within a day of kickoff, and only when that row's score equals
    the verified final score.
    """
    import league_registry
    parsed = parse_label(row.get('market'))
    if parsed is None or not final:
        return None
    league = next((l for l in league_registry.REGISTRY if l.name == row.get('league')), None)
    home, away = row.get('model_home_team'), row.get('model_away_team')
    kickoff = pd.to_datetime(row.get('kickoff_utc'), utc=True, errors='coerce')
    if (league is None or league.key not in LEAGUES[parsed[0]] or not league.football_data_div
            or not home or not away or pd.isna(kickoff)):
        return None
    cache = Path(cache_dir) if cache_dir is not None else Path(__file__).resolve().parent/'.football_cache'
    history = _committed_history(cache, league.football_data_div)
    if not len(history):
        return None
    day = kickoff.tz_convert(None).normalize()
    match = history.loc[(history.HomeTeam == home) & (history.AwayTeam == away)
                        & ((history._date - day).abs() <= pd.Timedelta(days=1))]
    if len(match) != 1:
        return None
    match = match.iloc[0]
    try:
        if (int(match.FTHG), int(match.FTAG)) != (int(final['home_goals']), int(final['away_goals'])):
            return None
        counts = [float(match[c]) for side in TOTALS[parsed[0]] for c in side]
    except (KeyError, TypeError, ValueError):
        return None
    if not all(math.isfinite(c) and c >= 0 for c in counts):
        return None
    return int(sum(counts))
