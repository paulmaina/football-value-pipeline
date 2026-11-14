"""What the inspection flag ("research strongly disagrees") is about, for each flagged pick of the live master.

Reporting only: it reads a flagged pick, its run's forecast row and the run clock, and writes text columns on that
row and a structured detail in the summary's "For inspection" section. It never changes a pick, a probability, a
rank, a tier or a decision, and it is never read by any selection step.

For each flagged pick (new_master_decision SHORTLISTED and inspection_flag True):

- a one-sentence plain summary of the research view's take;
- both views' expected goals per team, home/draw/away chances and most likely scorelines. The research view is the
  value shortlist's independent model (team_research: goal rates from ten-match form, an independent Poisson grid).
  The market view is Pinnacle's: expected goals and scorelines from the market-implied fit (fit B on 1X2, O/U 2.5
  and the main AH line, price_edge_shortlist.market_fit at the run clock), home/draw/away from the cagey tier's
  corrected margin distribution (the distribution behind the cagey no-loss chance), else from fit B;
- both no-loss chances and the gap (the row's own research_no_loss_probability, cagey_no_loss_probability,
  gap_points);
- the main driver: the team whose expected goals differ most between the views, with its last-10 form W-D-L and
  goals for/against per match (recency-weighted, as the research model uses them), whether xG was used for its rate,
  and how much history the model has (training matches; form matches);
- warnings: thin history (possibly promoted), European match, form from another competition;
- the historical record of comparable bets (evaluation/master_release/inspection_history.json, offline backtest).
"""
from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Dict, List, Mapping, Optional

import numpy as np
import pandas as pd

HISTORY = Path(__file__).with_name('evaluation') / 'master_release' / 'inspection_history.json'
THIN_TRAINING_MATCHES = 20  # fewer matches in the model's training data than about half a season
FULL_FORM = 10
COLUMNS = ['inspection_summary', 'inspection_expected_goals', 'inspection_home_draw_away',
           'inspection_likely_scores', 'inspection_no_loss', 'inspection_driver', 'inspection_warnings',
           'inspection_history']
SIDES = ('home', 'away')


def _number(value) -> Optional[float]:
    try:
        number = float(value)
    except (TypeError, ValueError):
        return None
    return number if math.isfinite(number) else None


def _pct(p: Optional[float]) -> str:
    return 'n/a' if p is None else f'{100 * p:.0f}%'


def _two(x: Optional[float]) -> str:
    return 'n/a' if x is None else f'{x:.2f}'


def _decode(value) -> dict:
    if isinstance(value, dict):
        return value
    try:
        out = json.loads(value) if isinstance(value, str) and value.strip() else {}
    except ValueError:
        return {}
    return out if isinstance(out, dict) else {}


def hda(matrix: np.ndarray) -> Dict[str, float]:
    goals = np.arange(len(matrix))
    diff = np.subtract.outer(goals, goals)
    total = float(matrix.sum())
    return {'home': float(matrix[diff > 0].sum()) / total, 'draw': float(matrix[diff == 0].sum()) / total,
            'away': float(matrix[diff < 0].sum()) / total}


def margin_hda(margins, probs) -> Dict[str, float]:
    margins, probs = np.asarray(margins, dtype=float), np.asarray(probs, dtype=float)
    total = float(probs.sum())
    return {'home': float(probs[margins > 0].sum()) / total, 'draw': float(probs[margins == 0].sum()) / total,
            'away': float(probs[margins < 0].sum()) / total}


def likely_scores(matrix: np.ndarray, top: int = 3) -> List[Dict[str, object]]:
    total = float(matrix.sum())
    cells = sorted(((float(matrix[h, a]) / total, h, a) for h in range(len(matrix)) for a in range(len(matrix))),
                   key=lambda c: (-round(c[0], 12), c[1], c[2]))
    return [{'score': f'{h}-{a}', 'p': p} for p, h, a in cells[:top]]


def research_view(forecast: Mapping) -> Optional[dict]:
    """The research model's view of the fixture, from its frozen context (team_research_json)."""
    from team_research import research_grid
    context = _decode(forecast.get('team_research_json'))
    rates = context.get('goal_rates') or []
    if len(rates) != 2 or any(_number(r) is None or _number(r) <= 0 for r in rates):
        return None
    matrix = research_grid([float(r) for r in rates])
    return {'expected_goals': {'home': float(rates[0]), 'away': float(rates[1])}, 'home_draw_away': hda(matrix),
            'likely_scores': likely_scores(matrix), 'context': context}


def market_view(forecast: Mapping, clock) -> Optional[dict]:
    """Pinnacle's view at the run clock: fit B's expected goals and scorelines; home/draw/away from the cagey tier's
    corrected margins (fit B's where the correction is unavailable)."""
    import narrow_margin as nm
    import price_edge_cagey_shortlist as v28
    import price_edge_shortlist as v27
    pin = v27.pinnacle_quotes(forecast)
    fit, info = v27.market_fit(pin, pd.Timestamp(clock), cutoff=True)
    if not fit.usable or fit.matrix is None:
        return None
    context = v28.corrected_context(pin, fit, info, nm.production_model())
    split, basis = ((margin_hda(context['margins'], context['probs']), 'cagey-corrected margins')
                    if context is not None else (hda(fit.matrix), 'market fit B'))
    return {'expected_goals': {'home': float(fit.lam_home), 'away': float(fit.lam_away)}, 'home_draw_away': split,
            'home_draw_away_basis': basis, 'likely_scores': likely_scores(fit.matrix)}


def _form(context: Mapping, side: str) -> dict:
    stats = (context.get('form') or {}).get(side) or {}
    return {'all': stats.get('all') or {'matches': 0}, 'venue': stats.get('venue') or {'matches': 0}}


def xg_used(context: Mapping, side: str) -> bool:
    """team_research.prepare's rule for one side's goal rate: verified xG for at least 5 of the matches the side's own
    form uses (venue split when it has at least 3 matches) and of the opponent's."""
    other = 'away' if side == 'home' else 'home'
    pick = lambda s: _form(context, s)['venue'] if _form(context, s)['venue'].get('matches', 0) >= 3 \
        else _form(context, s)['all']
    return pick(side).get('xg_matches', 0) >= 5 and pick(other).get('xg_matches', 0) >= 5


def form_competitions(forecast: Mapping, context: Mapping, side: str) -> List[Optional[str]]:
    """The ESPN competition of each of the side's last-10 form matches (None for the training history and rows
    without one), rebuilt exactly as team_research.prepare chose them."""
    import team_research as tr
    cached = _decode(forecast.get('research_history_json'))
    evidence = context.get('evidence') or {}
    cutoff = pd.Timestamp(context.get('observed_at_utc'))
    version = context.get('version') or tr.VERSION
    rows = list(cached.get(side, [])) + list(((evidence.get('recent') or {}).get(side)) or [])
    own = tr.history_name(forecast.get('research_history_json'), side, version)
    chosen = tr.form_rows(forecast.get(side + '_team'), rows, cutoff, version, own)
    return [r.get('competition') for r in chosen]


def warnings_for(forecast: Mapping, context: Mapping, league: str, european: bool) -> List[str]:
    import team_research as tr
    out = []
    for side in SIDES:
        team = forecast.get(side + '_team')
        trained = _number(forecast.get(side + '_training_matches'))
        if trained is not None and trained < THIN_TRAINING_MATCHES:
            why = 'few matches in this competition' if european else 'possibly promoted or new to the league'
            out.append(f"thin history: {team} has {trained:.0f} matches in the model's training data ({why})")
        played = _form(context, side)['all'].get('matches', 0)
        if played < FULL_FORM:
            out.append(f'thin form: {team} has {played} recent matches (of {FULL_FORM})')
    if european:
        out.append('European match: both views are unvalidated for European fixtures')
    slug = tr.LEAGUES.get(league)
    for side in SIDES:
        try:
            comps = form_competitions(forecast, context, side)
        except (ValueError, TypeError, KeyError):
            continue
        other = [c for c in comps if c and slug and c != slug]
        unknown = sum(1 for c in comps if not c)
        if other:
            out.append(f"form from another competition: {len(other)} of {forecast.get(side + '_team')}'s last "
                       f"{len(comps)} matches ({', '.join(sorted(set(other)))})")
        if european and unknown:
            out.append(f"{unknown} of {forecast.get(side + '_team')}'s last {len(comps)} form matches have no "
                       f"recorded competition (training history)")
    excluded = context.get('form_friendlies_excluded') or {}
    for side in SIDES:
        if excluded.get(side):
            out.append(f"{excluded[side]} friendlies left out of {forecast.get(side + '_team')}'s form")
    return out


def history_record(path: Path = HISTORY) -> Optional[dict]:
    try:
        return json.loads(Path(path).read_text(encoding='utf-8'))
    except (OSError, ValueError):
        return None


def history_text(history: Optional[dict]) -> str:
    if not history or not history.get('comparable', {}).get('bets'):
        return 'no historical record available'
    c, flag = history['comparable'], history.get('flag', {})
    reached = (f"no backtest bet reached the flag itself (cagey no-loss never exceeded "
               f"{_pct(flag.get('max_cagey_no_loss_in_backtest'))})" if not flag.get('bets') else
               f"{flag['bets']} backtest bets reached the flag itself: they avoided defeat "
               f"{_pct(flag.get('avoided_defeat'))} of the time; cagey predicted {_pct(flag.get('cagey_predicted'))}")
    return (f"When research disagreed this strongly ({c['definition']}), these bets avoided defeat "
            f"{_pct(c['avoided_defeat'])} of the time; cagey predicted {_pct(c['cagey_predicted'])} and research "
            f"{_pct(c['research_predicted'])} ({c['bets']} offline backtest bets, {c['first_kickoff_utc']} to "
            f"{c['last_kickoff_utc']}); {reached}.")


def detail(row: Mapping, forecast: Optional[Mapping], clock, european: bool,
           history: Optional[dict]) -> Dict[str, object]:
    """The structured inspection detail of one flagged pick (see the module docstring)."""
    research_no_loss = _number(row.get('research_no_loss_probability'))
    cagey_no_loss = _number(row.get('cagey_no_loss_probability'))
    gap = _number(row.get('gap_points'))
    out: Dict[str, object] = {
        'no_loss': {'research': research_no_loss, 'cagey': cagey_no_loss, 'gap_points': gap},
        'history': history_text(history)}
    if forecast is None:
        out['unavailable'] = 'no unique forecast row for this fixture'
        return out
    research = research_view(forecast)
    market = market_view(forecast, clock)
    if research is None or market is None:
        out['unavailable'] = ('research goal rates unavailable' if research is None
                              else 'market fit unavailable at the run clock')
        return out
    context = research.pop('context')
    out['research'], out['market'] = research, market
    diffs = {side: research['expected_goals'][side] - market['expected_goals'][side] for side in SIDES}
    side = max(SIDES, key=lambda s: (abs(diffs[s]), s == 'home'))
    team = row.get(side + '_team')
    form = _form(context, side)['all']
    results = str(form.get('results') or '')
    out['driver'] = {
        'side': side, 'team': team, 'research_expected_goals': research['expected_goals'][side],
        'market_expected_goals': market['expected_goals'][side], 'difference': diffs[side],
        'form_matches': int(form.get('matches') or 0), 'results': results,
        'wins': results.count('W'), 'draws': results.count('D'), 'losses': results.count('L'),
        'goals_for_per_match': _number(form.get('goals_for')), 'goals_against_per_match': _number(form.get('goals_against')),
        'xg_used': xg_used(context, side), 'training_matches': _number(forecast.get(side + '_training_matches'))}
    out['warnings'] = warnings_for(forecast, context, str(row.get('league') or ''), european)
    more = 'more' if diffs[side] > 0 else 'fewer'
    out['summary'] = (f"The research view expects {more} goals from {team} than the market "
                      f"({research['expected_goals'][side]:.2f} against {market['expected_goals'][side]:.2f}), so it "
                      f"gives {row.get('market_to_bet')} a {_pct(research_no_loss)} chance of not losing against "
                      f"the cagey tier's {_pct(cagey_no_loss)} ({gap:+.1f} points).")
    return out


def columns(info: Mapping) -> Dict[str, Optional[str]]:
    """The row's text columns from a detail."""
    nl = info['no_loss']
    row = dict.fromkeys(COLUMNS)
    row['inspection_no_loss'] = (f"research {_pct(nl['research'])}, cagey {_pct(nl['cagey'])}, gap "
                                 f"{nl['gap_points']:+.1f} points" if nl['gap_points'] is not None else None)
    row['inspection_history'] = info['history']
    if 'unavailable' in info:
        row['inspection_summary'] = f"details unavailable: {info['unavailable']}"
        return row
    r, m, d = info['research'], info['market'], info['driver']
    view = lambda v: f"home {v['home']:.2f}, away {v['away']:.2f}"
    split = lambda v: f"home {_pct(v['home'])}, draw {_pct(v['draw'])}, away {_pct(v['away'])}"
    scores = lambda v: ', '.join(f"{s['score']} ({_pct(s['p'])})" for s in v)
    trained = 'n/a' if d['training_matches'] is None else f"{d['training_matches']:.0f}"
    row.update(
        inspection_summary=info['summary'],
        inspection_expected_goals=f"research {view(r['expected_goals'])}; market {view(m['expected_goals'])}",
        inspection_home_draw_away=(f"research {split(r['home_draw_away'])}; market {split(m['home_draw_away'])} "
                                   f"({m['home_draw_away_basis']})"),
        inspection_likely_scores=f"research {scores(r['likely_scores'])}; market {scores(m['likely_scores'])}",
        inspection_driver=(
            f"{d['team']} ({d['side']}): expected goals {d['research_expected_goals']:.2f} research vs "
            f"{d['market_expected_goals']:.2f} market ({d['difference']:+.2f}); last {d['form_matches']} "
            f"W{d['wins']}-D{d['draws']}-L{d['losses']}, goals for {_two(d['goals_for_per_match'])} / against "
            f"{_two(d['goals_against_per_match'])} per match (recency-weighted); xG used: "
            f"{'yes' if d['xg_used'] else 'no'}; model history: {trained} training matches"),
        inspection_warnings='; '.join(info['warnings']) or 'none')
    return row


def annotate(frame: pd.DataFrame, predictions: Optional[pd.DataFrame], clock, config: Mapping):
    """(frame with COLUMNS added, {row index: detail}) for the flagged picks; every other row gets empty columns.
    A pick whose detail can't be built says so in its row; the list itself is never affected."""
    from master_selection import identity
    import master_reconciliation as mr
    out = frame.copy()
    for column in COLUMNS:
        out[column] = None
    details: Dict[int, dict] = {}
    if out.empty:
        return out, details
    flagged = out.new_master_decision.eq('SHORTLISTED') & out.inspection_flag.astype(object).eq(True)
    if not flagged.any():
        return out, details
    by_fixture = mr.forecasts(predictions)
    history = history_record()
    european = set(config['european']['leagues'])
    for index in out.index[flagged]:
        row = out.loc[index].to_dict()
        try:
            info = detail(row, by_fixture.get(identity(row)), clock, row.get('league') in european, history)
            text = columns(info)
        except Exception as exc:  # reporting only: never affects the list
            info = {'no_loss': {'research': _number(row.get('research_no_loss_probability')),
                                'cagey': _number(row.get('cagey_no_loss_probability')),
                                'gap_points': _number(row.get('gap_points'))},
                    'history': history_text(history), 'unavailable': f'{type(exc).__name__}: {exc}'}
            text = columns(info)
        details[index] = info
        for column, value in text.items():
            out.at[index, column] = value
    return out, details
