"""European research candidates CE2, CE3 and CE4 (Phase 2c; offline only, harness candidates).

CE is the research model as live runs it for UCL and UEL (evaluation_harness.european_matrices). On
European development it is far too sharp (home / away calibration slopes 0.75 / 0.76 on 1,154 fixtures).
None of these candidates reads odds, a market fit or the published grid: they read CE's goal rates,
European final scores, and domestic league results (football-data.co.uk, plus Understat xG for the five
Understat leagues) dated before the fold origin.

CE2, calibration only
    CE's home/away split rescaled by a slope (research_sharpen.sharpen_matrix: the draw is held, the home
    share of a decided match becomes sigmoid(slope * logit share)), the slope fitted by research_sharpen's
    weighted logistic fit on CE's own earlier forecasts of decided European matches played before the
    fold origin. The slope may go below 1 (flattening), so its bounds are SLOPE_BOUNDS, wider than C5's.
    Two versions are computed:
      CE2p  pooled over UCL and UEL;
      CE2c  fitted per competition, on that competition's own earlier forecasts.
    Rule, stated before any CE2 score was computed: CE2 is CE2c for a fold only if each competition has at
    least PER_COMPETITION_MIN (1,000) earlier decided matches; otherwise CE2 is CE2p. Neutral (CE2 = CE)
    until MIN_DECIDED (300) earlier decided matches exist for the fit in question (the domestic 1,000 would
    leave CE2 neutral through all of European development, which holds about 900 decided CE forecasts).

CE3, domestic form and xG
    For each team with domestic form (DOMESTIC_MIN_MATCHES league matches in the DOMESTIC_DAYS before the fold
    origin, in the 8 cached leagues; the inventory's rule, with the fold origin as the cutoff so nothing on
    or after it is read), its domestic research strength:
      * the league's Dixon-Coles fit on its results before the origin (live settings: half-life 480 days,
        L2 0.08, shots on, BBS off), read as the team's expected goals for and against an average current
        opponent of the league, both venues averaged (attack and defence rates, relative to the league mean);
      * shrunk with the team's last-ten domestic form exactly as the research model shrinks (10 : n),
        against an average opponent; for clubs in the five Understat leagues, when at least five of the
        last ten carry Understat xG, xG for and against replace goals, as in C3.
    Domestic strengths sit on each league's own scale. They are put on the European scale by league-strength
    factors s_L, fitted walk-forward on earlier European results only:
        log lambda_home = c_comp + h_comp + att_home + s_L(home) + def_away - s_L(away)
        log lambda_away = c_comp          + att_away + s_L(away) + def_home - s_L(home)
    (weighted Poisson maximum likelihood over the European matches played before the origin in which both
    teams had a domestic strength at their own fold origin, both competitions, 480-day recency half-life;
    a Gaussian prior s_L ~ N(0, FACTOR_PRIOR_SD^2) shrinks every league toward equal strength when data is
    thin; neutral until FACTOR_MIN_MATCHES such matches exist).
    CE3's goal rates are then the geometric blend
        log lambda_CE3 = (1 - DOMESTIC_WEIGHT) log lambda_CE + DOMESTIC_WEIGHT log lambda_domestic
    on fixtures where both teams have a domestic strength and the factors are fitted; on every other fixture
    CE3 is CE exactly. DOMESTIC_WEIGHT is fixed by a rule stated before looking (blend_weight_rule): the
    median share of domestic matches among a team's domestic plus European matches in the 365 days before
    the fixture, over the warm-up fixtures' teams with domestic form (dates and names only; no score read),
    rounded to 0.05. It is not tuned on development.
    CE3 carries domestic xG; CE3n is the same with goals-only domestic form (no xG), so xG's effect shows.

CE4
    CE3 followed by CE2's calibration, the slope refitted on CE3's own earlier forecasts (same rule, minimums
    and bounds as CE2).

Not used by the live pipeline.
"""
from __future__ import annotations

from collections import Counter
import math

import numpy as np
import pandas as pd
from scipy.optimize import minimize

VERSION = 'european-candidates-ce2-ce3-ce4-v1'
SLOPE_BOUNDS = (0.2, 2.5)
MIN_DECIDED = 300
PER_COMPETITION_MIN = 1000
DOMESTIC_MIN_MATCHES = 5
DOMESTIC_DAYS = 365
FORM_PRIOR = 10  # the research model's shrinkage weight on the fitted rate (team_research.prepare)
FACTOR_PRIOR_SD = 0.3
FACTOR_MIN_MATCHES = 100
HALF_LIFE_DAYS = 480.
# Fixed by blend_weight_rule on the warm-up fixtures (dates and names only), before any CE3 score was computed;
# tests/test_european_candidates.py recomputes it from the data.
DOMESTIC_WEIGHT = 0.85  # median share 0.826 over 584 warm-up team-fixtures, rounded to 0.05
COMPETITIONS = ('UCL', 'UEL')


# ---------------------------------------------------------------------------
# CE2 / CE4: calibration slope
# ---------------------------------------------------------------------------

def fit_slope(probs, outcomes, age_days, half_life=HALF_LIFE_DAYS):
    import research_sharpen as rs
    return rs.fit(probs, outcomes, age_days, half_life, min_matches=MIN_DECIDED, bounds=SLOPE_BOUNDS)


def slope_fits(probs, outcomes, competitions, dates, origin, half_life=HALF_LIFE_DAYS):
    """The pooled fit, the per-competition fits and the rule's choice for one fold origin, each on the
    forecasts of decided matches played before the origin. `probs` rows with NaN (no forecast) are skipped."""
    past = np.asarray(dates < origin) & np.isfinite(probs).all(axis=1)
    age = (origin - dates[past]).total_seconds().to_numpy() / 86400
    pooled = fit_slope(probs[past], outcomes[past], age, half_life)
    per = {}
    decided = {}
    for comp in COMPETITIONS:
        mask = past & (competitions == comp)
        decided[comp] = int((outcomes[mask] != 1).sum())
        per[comp] = fit_slope(probs[mask], outcomes[mask], (origin - dates[mask]).total_seconds().to_numpy() / 86400,
                              half_life)
    rule = 'per_competition' if all(decided[c] >= PER_COMPETITION_MIN for c in COMPETITIONS) else 'pooled'
    return {'pooled': pooled, 'per_competition': per, 'decided': decided, 'rule': rule}


def chosen_slope(fits, competition, version):
    if version == 'pooled':
        return fits['pooled']['slope']
    if version == 'per_competition':
        return fits['per_competition'][competition]['slope']
    return chosen_slope(fits, competition, fits['rule'])


# ---------------------------------------------------------------------------
# CE3: domestic strength
# ---------------------------------------------------------------------------

def team_strength(model, frame, team, origin, opponents):
    """`team`'s domestic research strength at `origin` (frame: the league's results before the origin, with
    HxG/AxG where Understat has them). Returns {'goals': (att, def), 'xg': (att, def), ...} in logs relative to
    the league mean rate, or None when the team is not in the fit."""
    from team_research import form_history, utc, weighted_form
    if team not in model.teams:
        return None
    opponents = [o for o in opponents if o != team and o in model.teams]
    if not opponents:
        return None
    goals_for, goals_against, league = [], [], []
    for o in opponents:
        home = model.expected_goals(team, o)
        away = model.expected_goals(o, team)
        goals_for += [float(home['lambda_home']), float(away['lambda_away'])]
        goals_against += [float(home['lambda_away']), float(away['lambda_home'])]
    for a in opponents + [team]:  # league mean rate over the current teams, both venues
        for b in opponents + [team]:
            if a != b:
                e = model.expected_goals(a, b)
                league.append((float(e['lambda_home']) + float(e['lambda_away'])) / 2)
    mean = float(np.mean(league))
    base_for, base_against = float(np.mean(goals_for)), float(np.mean(goals_against))
    rows = form_history(frame, team, team, utc(origin))['home']  # the team's last ten results before the origin
    form = weighted_form(rows, team)
    n = form['matches']
    out = {'matches_in_form': n, 'xg_matches': form.get('xg_matches', 0), 'dc_for': base_for,
           'dc_against': base_against, 'league_mean': mean}
    for label, use_xg in (('goals', False), ('xg', True)):
        if n:
            gf, ga = form['goals_for'], form['goals_against']
            if use_xg and form.get('xg_matches', 0) >= 5:
                gf, ga = form['xg_for'], form['xg_against']
            rate_for = (FORM_PRIOR * base_for + n * (gf + mean) / 2) / (FORM_PRIOR + n)
            rate_against = (FORM_PRIOR * base_against + n * (ga + mean) / 2) / (FORM_PRIOR + n)
        else:
            rate_for, rate_against = base_for, base_against
        out[label] = (math.log(max(rate_for, .05) / mean), math.log(max(rate_against, .05) / mean))
    out['used_xg'] = bool(n and form.get('xg_matches', 0) >= 5)
    return out


def league_frame(cache, league, cfg):
    """One league's results for European domestic form: the older domestic files (2015/16-2020/21) and the
    cached seasons, without the domestic holdout (always: even a European declared run never reads a domestic
    holdout result), with Understat xG for the five Understat leagues. Results, shots and xG only: no price
    column is kept, so no odds can reach a strength."""
    from pathlib import Path
    import european_results as er
    import evaluation_harness as eh
    import historical_benchmark as hb
    import understat_history as uh
    rule = cfg['european']['domestic_form']
    keep = ['Date', 'HomeTeam', 'AwayTeam', 'FTHG', 'FTAG', 'HS', 'AS', 'HST', 'AST']
    data, _, _ = hb.load_history(Path(cache), league, {**cfg, 'test_end_exclusive': cfg['end_exclusive']})
    old, _ = er.load_domestic_backfill(Path(cache) / rule['backfill_folder'], hb.CODES[league], rule['backfill_seasons'],
                                       columns=keep)
    if not old.empty and old.Date.max() >= data.Date.min():
        raise ValueError(f'{league} domestic backfill overlaps the cached seasons')
    data = pd.concat([old.reindex(columns=keep), data.reindex(columns=keep)], ignore_index=True)
    data = eh.training_rows(data, league, cfg, False).reset_index(drop=True)
    data, _ = uh.with_xg(data, cache, league)
    return data.sort_values(['Date', 'HomeTeam', 'AwayTeam'], kind='stable').reset_index(drop=True)


def league_strengths(league, frame, requests, cfg):
    """Strengths for one league: `requests` maps fold origin -> domestic team names. One Dixon-Coles fit per
    origin, on the league's results before it. Returns {(origin, team): strength}."""
    from football_value_pipeline_v2_standalone import DixonColesModel
    profile = cfg['production_v2']
    out = {}
    for origin, teams in sorted(requests.items()):
        origin = pd.Timestamp(origin)
        train = frame.loc[frame.Date < origin]
        if train.empty or train.Date.max() >= origin:
            continue
        recent = train.loc[train.Date >= origin - pd.Timedelta(days=DOMESTIC_DAYS)]
        current = sorted(set(recent.HomeTeam) | set(recent.AwayTeam))
        counts = Counter(list(recent.HomeTeam) + list(recent.AwayTeam))
        teams = [t for t in teams if counts.get(t, 0) >= DOMESTIC_MIN_MATCHES]
        if not teams or len(train) < cfg['min_train']:
            continue
        try:
            model = DixonColesModel(half_life_days=profile['half_life_days'], l2=cfg['baseline_l2'],
                                    max_goals=cfg['max_goals'], shot_features=profile['shot_features'],
                                    bbs_statistics=False).fit(train.copy(), as_of=origin)
        except (RuntimeError, ValueError):
            continue
        for team in teams:
            strength = team_strength(model, train, team, origin, current)
            if strength is not None:
                out[(origin.date().isoformat(), team)] = {**strength, 'league': league,
                                                          'domestic_matches': int(counts[team])}
    return out


def _league_job(args):
    league, cache, cfg, requests = args
    return league_strengths(league, league_frame(cache, league, cfg), requests, cfg)


def domestic_strengths(cache, cfg, fixtures, workers=None):
    """Per European fixture (index of `fixtures`: competition, Date, HomeTeam, AwayTeam, origin), each team's
    domestic strength at the fold origin, or None. Identities through the reviewed resolver and the reviewed
    aliases (manual reviewed aliases only for fixtures before the European holdout start)."""
    from concurrent.futures import ProcessPoolExecutor
    import european_backfill as eb
    import european_results as er
    names = {}
    frames = {}
    for league in cfg['leagues']:
        frames[league] = league_frame(cache, league, cfg)[['Date', 'HomeTeam', 'AwayTeam']]
        names[league] = (frames[league], set(frames[league].HomeTeam) | set(frames[league].AwayTeam))
    reviewed = eb.load_reviewed_aliases()
    teams = sorted(set(fixtures.HomeTeam) | set(fixtures.AwayTeam))
    (before, _), (after, _) = er.scoped_identities(teams, names, eb.load_domestic_aliases(), reviewed['domestic'])
    cut = pd.Timestamp(reviewed['applies_before'])
    sides = {}
    requests = {league: {} for league in cfg['leagues']}
    for idx, r in fixtures.iterrows():
        mapped = before if pd.Timestamp(r.Date) < cut else after
        origin = pd.Timestamp(r.origin).date().isoformat()
        for side, team in (('home', r.HomeTeam), ('away', r.AwayTeam)):
            ident = mapped.get(team)
            sides[(idx, side)] = ident
            if ident is not None:
                requests[ident[0]].setdefault(origin, set()).add(ident[1])
    jobs = [(league, str(cache), cfg, {o: sorted(t) for o, t in req.items()}) for league, req in requests.items() if req]
    found = {}
    with ProcessPoolExecutor(max_workers=workers) as pool:
        for part in pool.map(_league_job, jobs):
            found.update(part)
    out = {}
    for idx, r in fixtures.iterrows():
        origin = pd.Timestamp(r.origin).date().isoformat()
        out[idx] = {side: (found.get((origin, sides[(idx, side)][1])) if sides[(idx, side)] else None)
                    for side in ('home', 'away')}
    return out


def blend_weight_rule(fixtures, cache, cfg):
    """DOMESTIC_WEIGHT's rule (stated before looking): over the warm-up fixtures, for each team with domestic
    form, domestic / (domestic + European) matches in the 365 days before the fixture (European: the same
    competition); the median, rounded to 0.05. Reads dates and team names only."""
    import european_backfill as eb
    import european_results as er
    names = {}
    for league in cfg['leagues']:
        f = league_frame(cache, league, cfg)[['Date', 'HomeTeam', 'AwayTeam']]
        names[league] = (f, set(f.HomeTeam) | set(f.AwayTeam))
    reviewed = eb.load_reviewed_aliases()
    warm = fixtures.loc[fixtures.phase == 'warm_up']
    teams = sorted(set(warm.HomeTeam) | set(warm.AwayTeam))
    (mapped, _), _ = er.scoped_identities(teams, names, eb.load_domestic_aliases(), reviewed['domestic'])
    shares = []
    for r in warm.itertuples(index=False):
        day = pd.Timestamp(r.Date).normalize()
        start = day - pd.Timedelta(days=DOMESTIC_DAYS)
        comp = fixtures.loc[(fixtures.competition == r.competition) & (fixtures.Date < day) & (fixtures.Date >= start)]
        for team in (r.HomeTeam, r.AwayTeam):
            if team not in mapped:
                continue
            league, name = mapped[team]
            f = names[league][0]
            dom = int((((f.HomeTeam == name) | (f.AwayTeam == name)) & (f.Date < day) & (f.Date >= start)).sum())
            eur = int(((comp.HomeTeam == team) | (comp.AwayTeam == team)).sum())
            if dom >= DOMESTIC_MIN_MATCHES:
                shares.append(dom / (dom + eur))
    return {'median_share': float(np.median(shares)), 'weight': round(round(float(np.median(shares)) / .05) * .05, 2),
            'team_fixtures': len(shares)}


# ---------------------------------------------------------------------------
# CE3: league-strength factors and the blend
# ---------------------------------------------------------------------------

def fit_factors(rows, origin, leagues, kind='xg', half_life=HALF_LIFE_DAYS):
    """League-strength factors from European matches played before `origin` in which both teams had a domestic
    strength. `rows`: dicts with date, competition, home/away strengths, home_goals, away_goals. Returns
    {'status', 'matches', 's': {league: s}, 'c': {comp: c}, 'h': {comp: h}}; neutral below FACTOR_MIN_MATCHES."""
    past = [r for r in rows if r['date'] < origin]
    if len(past) < FACTOR_MIN_MATCHES:
        return {'status': 'warm_up', 'matches': len(past)}
    index = {l: i for i, l in enumerate(leagues)}
    nl = len(leagues)
    comps = {c: i for i, c in enumerate(COMPETITIONS)}
    n = len(past)
    lh = np.array([index[r['home'][1]] for r in past]); la = np.array([index[r['away'][1]] for r in past])
    ci = np.array([comps[r['competition']] for r in past])
    att_h = np.array([r['home'][0][kind][0] for r in past]); def_h = np.array([r['home'][0][kind][1] for r in past])
    att_a = np.array([r['away'][0][kind][0] for r in past]); def_a = np.array([r['away'][0][kind][1] for r in past])
    yh = np.array([r['home_goals'] for r in past], float); ya = np.array([r['away_goals'] for r in past], float)
    age = np.array([(origin - r['date']).total_seconds() / 86400 for r in past])
    w = np.exp(-math.log(2) * age / half_life)
    off_h, off_a = att_h + def_a, att_a + def_h

    def unpack(theta):
        return theta[:nl], theta[nl:nl + 2], theta[nl + 2:nl + 4]

    def objective(theta):
        s, c, h = unpack(theta)
        eta_h = c[ci] + h[ci] + off_h + s[lh] - s[la]
        eta_a = c[ci] + off_a + s[la] - s[lh]
        mh, ma = np.exp(eta_h), np.exp(eta_a)
        loss = float((w * (mh - yh * eta_h + ma - ya * eta_a)).sum()) + float((s ** 2).sum()) / (2 * FACTOR_PRIOR_SD ** 2)
        rh, ra = w * (mh - yh), w * (ma - ya)
        gs = np.zeros(nl)
        np.add.at(gs, lh, rh - ra); np.add.at(gs, la, ra - rh)
        gs += s / FACTOR_PRIOR_SD ** 2
        gc, gh = np.zeros(2), np.zeros(2)
        np.add.at(gc, ci, rh + ra); np.add.at(gh, ci, rh)
        return loss, np.concatenate([gs, gc, gh])

    start = np.zeros(nl + 4)
    start[nl:nl + 2] = math.log(max((yh.sum() + ya.sum()) / (2 * n), .1))
    result = minimize(objective, start, jac=True, method='L-BFGS-B')
    if not result.success or not np.isfinite(result.fun):
        return {'status': 'optimiser_failed', 'matches': n}
    s, c, h = unpack(result.x)
    return {'status': 'fitted', 'matches': n, 's': {l: float(s[i]) for l, i in index.items()},
            'c': {k: float(c[i]) for k, i in comps.items()}, 'h': {k: float(h[i]) for k, i in comps.items()}}


def domestic_rates(strengths, factors, competition, kind='xg'):
    """The domestic goal rates (home, away) of a European fixture on the European scale."""
    (sh, lh), (sa, la) = strengths['home'], strengths['away']
    s, c, h = factors['s'], factors['c'][competition], factors['h'][competition]
    home = math.exp(c + h + sh[kind][0] + s[lh] + sa[kind][1] - s[la])
    away = math.exp(c + sa[kind][0] + s[la] + sh[kind][1] - s[lh])
    return home, away


def blended_rates(ce_rates, dom_rates, weight=DOMESTIC_WEIGHT):
    return [float(math.exp((1 - weight) * math.log(e) + weight * math.log(d))) for e, d in zip(ce_rates, dom_rates)]


# ---------------------------------------------------------------------------
# Walk-forward driver (called by evaluation_harness.european)
# ---------------------------------------------------------------------------

CANDIDATE_NAMES = ('CE2', 'CE2p', 'CE2c', 'CE3', 'CE3n', 'CE4')


def strength_pair(strengths, fixture):
    s = strengths.get(fixture) or {}
    if s.get('home') is None or s.get('away') is None:
        return None
    return {'home': (s['home'], s['home']['league']), 'away': (s['away'], s['away']['league'])}


def build(research, factor_rows, strengths, windows, leagues, keep=None, weight=DOMESTIC_WEIGHT):
    """CE2, CE2p, CE2c, CE3, CE3n and CE4 for every scored CE forecast in `research`.

    research     CE's forecasts, scored or not (unscored rows only feed the walk-forward fits): dicts with
                 identity, competition, date, goal_rates, home_goals, away_goals, scored, fixture (strengths key).
    factor_rows  every European result that may train the league factors (never a locked holdout result):
                 dicts with date, competition, fixture, home_goals, away_goals.
    strengths    fixture -> {'home': strength or None, 'away': ...} (domestic_strengths).
    windows      the 14-day fold windows.
    Each fit for a window uses only matches played before the window opens. Returns
    ({candidate: [(row, grid, extra)]}, fits)."""
    from team_research import research_grid
    import research_sharpen as rs
    wanted = set(CANDIDATE_NAMES) if keep is None else set(keep) & set(CANDIDATE_NAMES)
    out = {k: [] for k in wanted}
    fits = []
    if not research or not wanted:
        return out, fits
    research = sorted(research, key=lambda r: r['date'])
    dates = pd.DatetimeIndex([r['date'] for r in research])
    comps = np.array([r['competition'] for r in research])
    outcomes = np.array([0 if r['home_goals'] > r['away_goals'] else 1 if r['home_goals'] == r['away_goals'] else 2
                         for r in research])
    ce = np.array([rs.one_x_two(research_grid(r['goal_rates'])) for r in research])
    factor_data = []
    for r in factor_rows:
        p = strength_pair(strengths, r['fixture'])
        if p is not None:
            factor_data.append({**r, **p})
    # Pass 1: CE3 / CE3n goal rates for every research row, with the factors of the window holding it.
    ce3 = {kind: [None] * len(research) for kind in ('xg', 'goals')}
    ce3_probs = np.full((len(research), 3), np.nan)  # NaN: no CE3 forecast; left out of CE4's fit
    window_info = {}
    for origin, stop in windows:
        inside = np.flatnonzero((dates >= origin) & (dates < stop))
        if not len(inside):
            continue
        factors = {kind: fit_factors(factor_data, origin, leagues, kind) for kind in ('xg', 'goals')}
        window_info[origin] = factors
        for i in inside:
            r = research[i]
            p = strength_pair(strengths, r['fixture'])
            for kind in ('xg', 'goals'):
                rates, used = list(r['goal_rates']), False
                if p is not None and factors[kind]['status'] == 'fitted':
                    rates = blended_rates(r['goal_rates'], domestic_rates(p, factors[kind], r['competition'], kind),
                                          weight)
                    used = True
                ce3[kind][i] = (rates, used)
            try:
                ce3_probs[i] = rs.one_x_two(research_grid(ce3['xg'][i][0]))
            except ValueError:
                pass
    # Pass 2: per window, the slopes (CE2 on CE's forecasts, CE4 on CE3's), applied to the scored rows inside.
    for origin, stop in windows:
        inside = [i for i in np.flatnonzero((dates >= origin) & (dates < stop)) if research[i]['scored']]
        if not inside:
            continue
        ce_fit = slope_fits(ce, outcomes, comps, dates, origin)
        ce3_fit = slope_fits(ce3_probs, outcomes, comps, dates, origin)
        factors = window_info[origin]
        fits.append({'origin': origin.date().isoformat(), 'end_exclusive': stop.date().isoformat(),
                     'scored_matches': len(inside), 'CE2': _fit_summary(ce_fit), 'CE4': _fit_summary(ce3_fit),
                     'factors': {k: {f: v.get(f) for f in ('status', 'matches', 's', 'c', 'h')} for k, v in factors.items()},
                     'domestic_used': int(sum(ce3['xg'][i][1] for i in inside))})
        for i in inside:
            r = research[i]
            base = research_grid(r['goal_rates'])
            grids = {}
            for name, version in (('CE2', 'rule'), ('CE2p', 'pooled'), ('CE2c', 'per_competition')):
                if name in wanted:
                    grids[name] = (rs.sharpen_matrix(base, chosen_slope(ce_fit, r['competition'], version)), False)
            if wanted & {'CE3', 'CE4'}:
                g3 = research_grid(ce3['xg'][i][0])
                if 'CE3' in wanted:
                    grids['CE3'] = (g3, ce3['xg'][i][1])
                if 'CE4' in wanted:
                    grids['CE4'] = (rs.sharpen_matrix(g3, chosen_slope(ce3_fit, r['competition'], 'rule')), ce3['xg'][i][1])
            if 'CE3n' in wanted:
                grids['CE3n'] = (research_grid(ce3['goals'][i][0]), ce3['goals'][i][1])
            for name, (grid, used) in grids.items():
                out[name].append((r, grid, {'domestic_used': used}))
    return out, fits


def _fit_summary(fit):
    return {'rule': fit['rule'], 'decided': fit['decided'],
            'pooled': {k: fit['pooled'].get(k) for k in ('slope', 'status', 'matches')},
            'per_competition': {c: {k: v.get(k) for k in ('slope', 'status', 'matches')}
                                for c, v in fit['per_competition'].items()}}
