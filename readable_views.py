"""The two shortlist models, and the master's verdict on them, for the readable league outputs (display only).

format_football_output.py (football_output_v2/readable: *_predictions_readable.csv, *_report.md,
*_scorelines_readable.csv) and the league tabs of league_predictions.xlsx show, for every fixture:

- Research, the value shortlist's model: live research v5 (domestic, C6) or v6 (UCL/UEL, CE3n), exactly as the
  forecast row carries it. Home/draw/away are the row's research_p_home/draw/away. The score grid behind the other
  markets is rebuilt from the goal rates and fit frozen in team_research_json by the live grid function of the row's
  research version (research_low_score_sharpen.live_grid, research_ce3n.live_grid, team_research.research_grid),
  and shown only when it reproduces the frozen margin distribution and Over 1.5 (else blank, with the reason).
- Cagey, the market view: the cagey tier's grid as the run built it, from the forecast's Pinnacle quotes at the
  run's clock with the run's settings: price_edge_shortlist.pinnacle_quotes and market_fit, then
  price_edge_cagey_shortlist.cagey_basis (D_pow2 domestic and D for UCL/UEL where the run's switch says so; D where
  D_pow2's power fit fails its fit check, flagged), corrected_context and cagey_tier_v3.corrected_grid, the steps of
  price_edge_cagey_shortlist.make_transform. Over/Under 1.5 come from the uncorrected Pinnacle grid, as the cagey
  tier prices Over 1.5 (cagey_market_basis). Without Pinnacle 1X2 and O/U 2.5 there is no grid (blank, reason).
- Each view's no-loss on the quoted Pinnacle AH lines: the view's margin distribution settled on the line by
  profit_shortlist.probabilities (the function both lists settle offers with), no-loss as master_reconciliation.
- The master's verdict on every Pinnacle offer in the run's decision rows: master_reconciliation.offer_row, the
  function the master builds its own rows with (classify: research and cagey no-loss, gap g, gap check, labels,
  market safety and price; execution and timing checks). The fixture's best offer is its master pick, else the
  offer master_reconciliation.select would choose for it.

No probability is blended, averaged or computed in another way than the live code computes it. Nothing here is read
by a list, a grade, a stake or a decision.
"""
from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any, Dict, List, Mapping, Optional, Sequence, Tuple

import numpy as np
import pandas as pd

RESEARCH, CAGEY = 'Research', 'Cagey'
BENCHMARK = 'Benchmark (70% Pinnacle blend), display only'
KINDS = ('win', 'half_win', 'push', 'half_loss', 'loss')
REPRODUCE_TOLERANCE = 1e-9   # a rebuilt research grid must give the frozen margins and Over 1.5 to this
SCORELINE_MIN = 1e-4         # scorelines CSV: research and cagey cells at or above 0.01%
SAFEST_AH_MIN_ODDS = 1.20
MISSING_DECISIONS = 'decision rows not in this run bundle'
SAFETY_TEXT = {'safe': 'safe', 'risky': 'risky', 'middle': 'in between'}


def number(value: Any) -> Optional[float]:
    try:
        x = float(value)
    except (TypeError, ValueError):
        return None
    return x if math.isfinite(x) else None


def _read_csv(path: Path) -> Optional[pd.DataFrame]:
    if not path.exists():
        return None
    try:
        return pd.read_csv(path, low_memory=False)
    except pd.errors.EmptyDataError:
        return pd.DataFrame()


def _records(frame: Optional[pd.DataFrame]) -> List[dict]:
    if frame is None or frame.empty:
        return []
    return frame.astype(object).where(frame.notna(), None).to_dict('records')


# ---------------------------------------------------------------------------------------------------------------
# The two views' grids
# ---------------------------------------------------------------------------------------------------------------

def _same_margins(a: Mapping, b: Mapping) -> bool:
    a = {int(float(k)): float(v) for k, v in (a or {}).items()}
    b = {int(float(k)): float(v) for k, v in (b or {}).items()}
    return bool(a) and all(abs(a.get(k, 0.) - b.get(k, 0.)) <= REPRODUCE_TOLERANCE for k in set(a) | set(b))


def research_view(row: Mapping, clock=None) -> Dict[str, Any]:
    """The research grid of one forecast row: {'matrix', 'margin_distribution', 'p_1x2', 'version'} or {'reason'}.

    With the run's `clock`, the research is read exactly as the value shortlist reads it (profit_shortlist.context:
    the frozen team_research_json, or for a forecast saved without it team_research.prepare at the clock); without
    a clock, only the frozen research. Home/draw/away are the forecast row's research_p_* where it carries them."""
    import team_research as tr
    if clock is not None:
        from profit_shortlist import context as research_context
        context, warnings = research_context(dict(row), pd.Timestamp(clock))
        if not context:
            return {'reason': 'no research at the run clock: ' + ('; '.join(warnings) or 'not collected')}
    else:
        context = tr.decode(row.get('team_research_json'))
        if not context:
            return {'reason': 'no research in this forecast'}
    version = context.get('version') or row.get('research_version')
    p_1x2 = [number(row.get('research_p_' + k)) for k in ('home', 'draw', 'away')]
    if None in p_1x2 and context.get('margin_distribution'):
        # A forecast saved without research columns: the outcome split enrich would have written.
        derived = tr.outcome_columns(context, '')
        p_1x2 = [number(derived[k]) for k in ('home', 'draw', 'away')]
    rates = context.get('goal_rates') or []
    if None in p_1x2 or not context.get('margin_distribution') or len(rates) != 2 \
            or any(number(r) is None or number(r) <= 0 for r in rates):
        notes = [w for w in context.get('warnings', []) if 'research probabilities' in w or 'goal-rate' in w]
        return {'reason': 'no research probabilities for this fixture' + (f" ({'; '.join(notes)})" if notes else '')}
    try:
        if version in tr.C6_VERSIONS:
            if not context.get('c6_fit'):
                return {'reason': 'C6 fit not frozen in this forecast; research grid not rebuilt'}
            import research_low_score_sharpen as c6
            matrix = c6.live_grid(rates, context['c6_fit'])
        elif version in tr.CE3N_VERSIONS:
            import research_ce3n as ce3n
            matrix = ce3n.live_grid(rates)
        else:
            matrix = tr.research_grid(rates)
    except (ValueError, TypeError, KeyError) as exc:
        return {'reason': f'research grid unavailable ({type(exc).__name__})'}
    outputs = tr.grid_outputs(matrix)
    over = number(context.get('p_over_1_5'))
    if not _same_margins(outputs['margin_distribution'], context['margin_distribution']) or over is None \
            or abs(outputs['p_over_1_5'] - over) > REPRODUCE_TOLERANCE:
        return {'reason': 'rebuilt research grid does not reproduce the frozen forecast; not shown'}
    frozen = bool(tr.decode(row.get('team_research_json')))
    return {'matrix': np.asarray(matrix, float), 'margin_distribution': context['margin_distribution'],
            'p_1x2': p_1x2, 'version': version, 'frozen': frozen}


class CageySettings:
    """The run's cagey settings, model and corrections (from its summary), loaded once per run."""

    def __init__(self, summary: Mapping):
        import narrow_margin as nm
        import price_edge_cagey_shortlist as pecs
        self.error = None
        try:
            self.settings = {k: summary.get(k) for k in pecs.REPLAY_SETTINGS}
            version = summary.get('cagey_model_version')
            self.model = nm.load(version) if version else nm.production_model()
            self.live = pecs.correction_live(self.settings)
            self.corrections = pecs.correction_models(self.settings, self.model)
            self.strict = pecs.timing_rule(self.settings) == pecs.TIMING_RULE_CUTOFF
            self.method = pecs.devig_method(self.settings)
        except (OSError, ValueError, KeyError, TypeError) as exc:
            self.error = f'cagey settings unavailable ({type(exc).__name__}: {exc})'


def cagey_view(row: Mapping, clock, cagey: Optional[CageySettings]) -> Dict[str, Any]:
    """The cagey grid of one forecast row as the run built it: {'matrix', 'over_matrix', 'margin_distribution',
    'correction', 'fallback', 'fit'} or {'reason'}."""
    if clock is None:
        return {'reason': 'no cagey grid: run clock not recorded in this bundle'}
    if cagey is None or cagey.error:
        return {'reason': 'no cagey grid: ' + (cagey.error if cagey else 'run summary not in this bundle')}
    import price_edge_cagey_shortlist as pecs
    import price_edge_shortlist as v27
    from cagey_market_basis import over_probability
    from cagey_tier_v3 import corrected_grid
    pin = v27.pinnacle_quotes(row)
    missing = [name for name, key in (('1X2', 'h2h'), ('O/U 2.5', 'ou25')) if pin.get(key) is None]
    if missing:
        return {'reason': f"no cagey grid: needs Pinnacle 1X2 and O/U 2.5 (no Pinnacle {' or '.join(missing)} quote)"}
    fit, fit_info = v27.market_fit(pin, clock, cagey.strict)
    name = None if cagey.live is None else cagey.live[pecs.correction_scope(row.get('league'))]
    name, model, method, cagey_fit, cagey_info, fallback = pecs.cagey_basis(
        name, cagey.corrections, pin, fit, fit_info, clock, cagey.strict, cagey.method)
    context = pecs.corrected_context(pin, cagey_fit, cagey_info, model, method) if model is not None else None
    if context is None:
        reasons = '; '.join(dict.fromkeys([*fit.reasons, *fit_info['fit_a'].reasons])) or 'no usable fit'
        return {'reason': f'no cagey grid: no usable Pinnacle fit ({reasons})'}
    source = cagey_fit if cagey_fit.usable else cagey_info['fit_a']
    try:
        matrix = corrected_grid(context, source.matrix)
    except ValueError as exc:
        return {'reason': f'no cagey grid: {exc}'}
    correction = name or pecs.CORRECTION_D
    return {'matrix': matrix,
            'over_matrix': np.asarray(source.matrix, float) if over_probability(source.matrix) is not None else None,
            'margin_distribution': {str(int(m)): float(p) for m, p in zip(context['margins'], context['probs'])},
            'correction': correction, 'fallback': fallback, 'fit': context['fit']}


def grid_markets(matrix, p_1x2: Optional[Sequence[float]] = None, over_matrix=None) -> Dict[str, Any]:
    """The markets of one score grid (rows home goals, columns away goals). `p_1x2` replaces home/draw/away with the
    values the forecast carries (research); `over_matrix` is the grid Over/Under 1.5 are read from (cagey: the
    uncorrected Pinnacle grid)."""
    m = np.asarray(matrix, float)
    home_goals, away_goals = np.arange(m.shape[0])[:, None], np.arange(m.shape[1])[None, :]
    total = home_goals + away_goals
    home, draw, away = (float(m[home_goals > away_goals].sum()), float(m[home_goals == away_goals].sum()),
                        float(m[home_goals < away_goals].sum())) if p_1x2 is None else tuple(map(float, p_1x2))
    o = np.asarray(over_matrix, float) if over_matrix is not None else m
    o_total = np.add.outer(np.arange(o.shape[0]), np.arange(o.shape[1]))
    best = np.unravel_index(int(np.argmax(m)), m.shape)
    return {'home': home, 'draw': draw, 'away': away,
            'xg_home': float((m.sum(axis=1) * np.arange(m.shape[0])).sum()),
            'xg_away': float((m.sum(axis=0) * np.arange(m.shape[1])).sum()),
            'score': f'{best[0]}-{best[1]}', 'score_p': float(m[best]),
            'over_1_5': float(o[o_total >= 2].sum()), 'under_1_5': float(o[o_total <= 1].sum()),
            'over_2_5': float(m[total >= 3].sum()), 'under_2_5': float(m[total <= 2].sum()),
            'over_3_5': float(m[total >= 4].sum()), 'under_3_5': float(m[total <= 3].sum()),
            'btts_yes': float(m[1:, 1:].sum()), 'btts_no': float(m.sum() - m[1:, 1:].sum()),
            'dc_1x': home + draw, 'dc_x2': draw + away}


def ranked_scores(matrix, minimum: float = 0.) -> List[Tuple[str, float]]:
    m = np.asarray(matrix, float)
    cells = [(f'{i}-{j}', float(m[i, j])) for i in range(m.shape[0]) for j in range(m.shape[1])
             if m[i, j] >= minimum]
    return sorted(cells, key=lambda c: (-c[1], c[0]))


def lean(markets: Optional[Mapping], home: str, away: str) -> Tuple[Optional[str], Optional[float]]:
    if not markets:
        return None, None
    options = [(f'{home} win', markets['home']), ('Draw', markets['draw']), (f'{away} win', markets['away'])]
    return max(options, key=lambda o: o[1])


# ---------------------------------------------------------------------------------------------------------------
# No-loss on the quoted Pinnacle AH lines
# ---------------------------------------------------------------------------------------------------------------

def quoted_ah_lines(row: Mapping) -> List[Tuple[str, float, float, float]]:
    """(side, line, Pinnacle price, opposite price) for every quoted Pinnacle AH pair (price_edge_shortlist)."""
    import price_edge_shortlist as v27
    out = []
    for point, (home_price, away_price, _) in sorted(v27.pinnacle_quotes(row)['ah'].items()):
        out.append(('home', float(point), float(home_price), float(away_price)))
        out.append(('away', -float(point) + 0., float(away_price), float(home_price)))
    return sorted(out, key=lambda o: (o[0] != 'home', o[1]))


def settle(view: Optional[Mapping], row: Mapping, side: str, line: float) -> Optional[np.ndarray]:
    """A view's settlement (win, half win, push, half loss, loss) on one AH line: profit_shortlist.probabilities on
    the view's margin distribution, exactly as both lists settle an offer."""
    if not view or 'margin_distribution' not in view:
        return None
    import master_reconciliation as mr
    from price_edge_shortlist import _ah_market
    from profit_shortlist import probabilities
    try:
        probs = probabilities(row, {'market': _ah_market(side, line), 'handicap_side': side, 'handicap_line': line},
                              {'margin_distribution': view['margin_distribution']})
    except (ValueError, TypeError):
        return None
    return None if probs is None else mr.settlement_mass([probs['p_' + k] for k in KINDS])


def ah_line_label(row: Mapping, side: str, line: float) -> str:
    team = row.get('home_team' if side == 'home' else 'away_team') or side.title()
    return f'{team} {line:+.2f}'


def view_ah_no_loss(row: Mapping, research: Mapping, cagey: Mapping) -> List[Dict[str, Any]]:
    import master_reconciliation as mr
    out = []
    for side, line, price, opposite in quoted_ah_lines(row):
        r, c = settle(research, row, side, line), settle(cagey, row, side, line)
        out.append({'side': side, 'line': line, 'label': ah_line_label(row, side, line), 'price': price,
                    'opposite': opposite, 'research': None if r is None else mr.no_loss(r),
                    'cagey': None if c is None else mr.no_loss(c), 'cagey_mass': c})
    return out


def safest_ah(row: Mapping, lines: Sequence[Mapping], cagey: Mapping) -> Dict[str, Any]:
    """The quoted Pinnacle AH line with the highest cagey no-loss among lines with cagey expected value >= 0 at odds
    >= 1.20 (ties: higher expected value, then higher odds), with research's no-loss on the same line."""
    import master_reconciliation as mr
    if 'reason' in cagey:
        return {'reason': cagey['reason']}
    if not lines:
        return {'reason': 'No Pinnacle Asian handicap quotes'}
    candidates = []
    for item in lines:
        if item['cagey_mass'] is None:
            continue
        scored = mr.scored(item['cagey_mass'], item['price'], 0.)
        if item['price'] >= SAFEST_AH_MIN_ODDS and scored['expected_return'] + 1e-12 >= 0:
            candidates.append((item, scored))
    if not candidates:
        return {'reason': f'No quoted Pinnacle line has cagey EV >= 0 at odds >= {SAFEST_AH_MIN_ODDS:.2f} '
                          f'({len(lines)} lines checked)'}
    item, scored = min(candidates, key=lambda c: (-round(c[1]['no_loss'], 12), -round(c[1]['expected_return'], 12),
                                                  -c[0]['price'], c[0]['side'], c[0]['line']))
    mass = item['cagey_mass']
    won, lost = mass[0] + mass[1] / 2, mass[4] + mass[3] / 2
    share = float(won / (won + lost)) if won + lost > 0 else None
    from football_value_pipeline_v2_standalone import devig
    fair = number(devig([item['price'], item['opposite']], 'proportional')[0])
    return {'label': item['label'], 'price': item['price'], 'ev': scored['expected_return'], 'cagey': item['cagey'],
            'research': item['research'], 'share': share, 'pinnacle_share': fair}


# ---------------------------------------------------------------------------------------------------------------
# The run: decision rows, the master's verdict on every Pinnacle offer, and the three lists
# ---------------------------------------------------------------------------------------------------------------

def gap_label(row: Mapping, config: Mapping) -> str:
    gap = config['gap']
    text = {'agree': f"both agree (gap within ±{gap['research_too_optimistic_min_points']:.0f} points)",
            'research_too_optimistic': 'research too optimistic',
            'research_more_pessimistic': 'research too pessimistic',
            'no_research_check': 'no research check (no research view)',
            'one_view_missing': 'one view missing (no cagey view)', 'no_view': 'no view'}.get(row.get('gap_check'), '')
    if row.get('inspection_flag') is True:
        text += '; flagged for inspection (research strongly disagrees)'
    return text or 'not classified'


def cagey_tier(row: Mapping) -> str:
    safety = row.get('market_safety')
    if safety is None:
        return 'no market view'
    text = f"{SAFETY_TEXT.get(safety, safety)}, {row.get('market_price')} price"
    return text + (' (Pinnacle stand-in: no cagey view)' if row.get('market_basis') == 'pinnacle' else '')


def live_master_config(summary: Mapping) -> Dict:
    """The master rule config the run's live master executed with: the strong master's rule (recorded in the run
    summary) has its own odds window since master-strong-team-v2; otherwise the live master rule's config."""
    import master_reconciliation as mr
    import master_shortlist
    import master_strong
    rule = master_shortlist.strong_rule((summary.get('master_shortlist') or {}).get('version'))
    if rule is None:
        return mr.load_config()
    return master_strong.execution_config(mr.load_config(), master_strong.load_config(version=rule))


def master_check(row: Mapping) -> str:
    return 'eligible' if row.get('new_master_executable') else str(row.get('new_master_reason') or 'not executable')


def offer_key(row: Mapping) -> Tuple:
    from performance_tracking import fixture_key
    price = number(row.get('offered_decimal_odds'))
    return fixture_key(row), str(row.get('market_to_bet') or ''), None if price is None else round(price, 6)


class Run:
    """One run bundle as the readable outputs read it. Every input is optional; what is missing shows its reason."""

    def __init__(self, input_dir: Optional[Path] = None):
        import master_reconciliation as mr
        self.input_dir = Path(input_dir) if input_dir is not None else None
        base = self.input_dir if self.input_dir is not None and self.input_dir.exists() else None
        summary_path = base / 'conservative_bet_summary.json' if base else None
        try:
            self.summary = json.loads(summary_path.read_text(encoding='utf-8')) if summary_path and \
                summary_path.exists() else {}
        except ValueError:
            self.summary = {}
        from quote_freshness import quote_utc
        stamp = self.summary.get('generated_at_utc')
        self.clock = pd.Timestamp(quote_utc(stamp)) if stamp and quote_utc(stamp) is not None else None
        self._cagey = None
        self.config = live_master_config(self.summary)
        self.decisions = _read_csv(base / 'conservative_bet_rejections.csv') if base else None
        self.value = _read_csv(base / 'conservative_bet_shortlist.csv') if base else None
        self.cagey_list = _read_csv(base / 'cagey_tier_shortlist.csv') if base else None
        master = _read_csv(base / 'master_shortlist.csv') if base else None
        self.master_new = master is not None and 'new_master_decision' in master.columns
        self.master = master
        self.predictions = self._predictions(base)
        self._offers: Optional[Dict[str, List[dict]]] = None

    @staticmethod
    def _predictions(base: Optional[Path]) -> Optional[pd.DataFrame]:
        if base is None:
            return None
        combined = base / 'all_leagues_predictions.csv'
        if combined.exists():
            return _read_csv(combined)
        frames = [f for f in (_read_csv(p) for p in sorted(base.glob('*_predictions.csv'))
                              if '_backtest_' not in p.name) if f is not None and len(f)]
        return pd.concat(frames, ignore_index=True, sort=False) if frames else None

    @property
    def cagey(self) -> Optional[CageySettings]:
        if self._cagey is None and self.summary:
            self._cagey = CageySettings(self.summary)
        return self._cagey

    def offers(self) -> Optional[Dict[str, List[dict]]]:
        """fixture key -> every Pinnacle offer of the run as master_reconciliation.offer_row sees it (None: no
        decision rows in the bundle)."""
        if self._offers is not None or self.decisions is None:
            return self._offers
        import master_reconciliation as mr
        records = [r for r in _records(self.decisions) if r.get('bookmaker') == 'Pinnacle'
                   and (number(r.get('offered_decimal_odds')) or 0) > 1]
        clock = mr.run_clock(_records(self.decisions), self.summary.get('generated_at_utc'))
        by_fixture, fits = mr.forecasts(self.predictions), {}
        self._offers = {}
        for record in records:
            row = mr.offer_row(record, self.config, clock, by_fixture, fits)
            self._offers.setdefault(row['_match'], []).append(row)
        return self._offers

    def picks(self, frame: Optional[pd.DataFrame], key: str, ranked: Optional[str] = None) -> List[dict]:
        from performance_tracking import fixture_key
        rows = _records(frame)
        if ranked is not None:
            rows = [r for r in rows if r.get(ranked) == 'SHORTLISTED']
        return [r for r in rows if fixture_key(r) == key]

    def master_picks(self, key: str) -> List[dict]:
        if self.master is None:
            return []
        if self.master_new:
            return sorted(self.picks(self.master, key, 'new_master_decision'),
                          key=lambda r: number(r.get('new_master_rank')) or math.inf)
        return self.picks(self.master, key)


def _offer_text(row: Mapping) -> str:
    price = number(row.get('offered_decimal_odds'))
    return f"{row.get('market_to_bet')} @ {price:.2f}" if price is not None else str(row.get('market_to_bet'))


def fixture(row: Mapping, run: Run) -> Dict[str, Any]:
    """Everything the readable outputs show for one forecast row (values unformatted)."""
    import master_reconciliation as mr
    from performance_tracking import fixture_key
    home, away = str(row.get('home_team', 'Home')), str(row.get('away_team', 'Away'))
    research = research_view(row, run.clock)
    cagey = cagey_view(row, run.clock, run.cagey)
    markets = {RESEARCH: grid_markets(research['matrix'], research['p_1x2']) if 'matrix' in research else None,
               CAGEY: grid_markets(cagey['matrix'], over_matrix=cagey.get('over_matrix')) if 'matrix' in cagey
               else None}
    leans = {name: lean(m, home, away) for name, m in markets.items()}
    if leans[RESEARCH][0] is None or leans[CAGEY][0] is None:
        agree = 'one view missing'
    else:
        agree = 'yes' if leans[RESEARCH][0] == leans[CAGEY][0] else 'no'
    lines = view_ah_no_loss(row, research, cagey)
    key = fixture_key(row)
    offers_by_fixture = run.offers()
    offers = None if offers_by_fixture is None else offers_by_fixture.get(key, [])
    master = run.master_picks(key)
    best, basis = None, None
    if offers is not None:
        if master and run.master_new:
            pick = master[0]
            # The master file's own row when the pick is not among the decision rows read here.
            best = next((o for o in offers if offer_key(o) == offer_key(pick)), {**pick, 'new_master_executable': True})
            basis = f"master pick (rank {number(pick.get('new_master_rank')):.0f}, {pick.get('new_master_tier')})"
        elif offers:
            rows = [dict(o) for o in offers]
            mr.select(rows, 1, fill_min_no_loss=float(run.config['fill']['step_2_min_no_loss']))
            chosen = [r for r in rows if r.get('new_master_rank') == 1]
            if chosen:
                best = next(o for o in offers if offer_key(o) == offer_key(chosen[0]))
                basis = (f"the master's rule over every Pinnacle offer of this match, nominated or not "
                         f"({chosen[0]['new_master_tier']} step)" + ('' if master else '; not on the master'))
    return {'research': research, 'cagey': cagey, 'markets': markets, 'leans': leans, 'agree': agree,
            'lines': lines, 'safest': safest_ah(row, lines, cagey), 'offers': offers, 'best': best,
            'best_basis': basis, 'value': run.picks(run.value, key) if run.value is not None else None,
            'cagey_picks': run.picks(run.cagey_list, key) if run.cagey_list is not None else None,
            'master': master if run.master is not None else None, 'master_new': run.master_new}


def list_text(picks: Optional[List[dict]], offers: Optional[List[dict]], with_tier: bool = False) -> str:
    if picks is None:
        return 'list not in this run bundle'
    if not picks:
        return 'no'
    found = {offer_key(o): o for o in offers or []}
    parts = []
    for pick in picks:
        text = _offer_text(pick)
        if with_tier and offer_key(pick) in found:
            text += f' ({cagey_tier(found[offer_key(pick)])})'
        parts.append(text)
    return 'yes: ' + '; '.join(parts)


def master_text(info: Mapping) -> str:
    picks = info['master']
    if picks is None:
        return 'master list not in this run bundle'
    if not picks:
        return 'no'
    pick = picks[0]
    if info['master_new']:
        return f"yes: rank {number(pick.get('new_master_rank')):.0f} ({pick.get('new_master_tier')}), {_offer_text(pick)}"
    rank = number(pick.get('master_rank'))
    return f"yes: rank {rank:.0f} (old master rule), {_offer_text(pick)}" if rank is not None else 'yes: ' + _offer_text(pick)
