"""The model activity log: one committed, append-only record of every model release, live-fit refit, stale-fit
warning, rollback check, rollback-switch change and master fallback (reporting only).

    football_output_v2/model_activity/activity_log.jsonl

One JSON object per line, written once and never edited or removed: a writer only appends, and an event whose id is
already in the file is not written again (so a retried workflow attempt or a rerun backfill adds nothing). Each line:

    id                 stable identifier (a repeat of the same event has the same id)
    schema             SCHEMA
    recorded_at_utc    when it happened, ISO 8601 UTC ("...Z")
    recorded_at_eat    the same instant in EAT (Nairobi, UTC+3), "YYYY-MM-DD HH:MM EAT"
    event              Release | Refit | Stale-fit warning | Rollback check | Switch change | Master fallback |
                       Comparison baseline missing | UCL live check
    model              the model or list ("C6 live fit", "research v6 (CE3n)", "new master", "UCL", ...)
    outcome            short status; the workbook colours it (ROLLBACK TRIGGERED, ... WARNING, FAILED red; STALE FIT
                       WARNING STARTED amber; RELEASED and PUBLISHED green)
    details            plain English
    key                what the event tracks, for "compared with the last logged state" (refit:C6, stale:CE3n,
                       switches, rollback:v5, ucl_live_check, ...)
    source             refit workflow | forecast run | weekly report | backfill | closing odds
    backfilled         true for events reconstructed from git history after the fact
    data               the figures behind the line (fit windows and parameters, switch states, intervals, ...)

Writers (each wrapped so that it can never break, delay or alter a forecast, a refit or a review):

  refit workflow     scripts/build_research_c6_fits.py and build_research_ce3n_fits.py with --publish, on fit days
                     only: published (in the same commit as the fit), skipped with its reason or failed with its
                     reason (own commit). A Monday that is not a fit day logs and commits nothing.
  forecast run       publish_scheduled_forecasts.py after the pipeline: stale-fit warning started or ended, a change
                     in any switch of master_shortlist_config.json or research_config.json against the last logged
                     state, new master failed (old published), comparison baseline missing, and the UCL live check
                     (every result until one has passed, then only failures). Every change of serving odds
                     provider (odds_provider.py): within a run, and at run start against the provider serving at
                     the end of the same workflow's previous run (The Odds API before any routed run, and for a
                     run with the switch off); this run's from its summary, earlier forecast runs' and the closing
                     collector's from the committed usage log (source "closing odds").
  weekly report      performance_tracking.review: one rollback-check line per release (new master, research v5,
                     research v6) and per competition (UCL, UEL) for each report week (Monday to Sunday, EAT), and a
                     further line within the week whenever a check's status changes.
  backfill           python model_activity.py backfill: the releases, switch changes and live fits already made
                     (from git history; the refit workflow had not run yet), marked backfilled; idempotent.

Nothing here reads odds into a model, changes a prediction, probability, pick, grade or stake, or switches anything.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timedelta, timezone
import hashlib
import json
from pathlib import Path
import subprocess
import tempfile
from typing import Any, Dict, Iterable, List, Mapping, Optional, Sequence

SCHEMA = 'model-activity-v1'
LOG = Path('football_output_v2/model_activity/activity_log.jsonl')
RELATIVE = Path('model_activity/activity_log.jsonl')  # under an output root (football_output_v2)
EAT = timezone(timedelta(hours=3), 'EAT')

RELEASE, REFIT, STALE, ROLLBACK, SWITCH = 'Release', 'Refit', 'Stale-fit warning', 'Rollback check', 'Switch change'
MASTER_FALLBACK, BASELINE_MISSING, UCL_CHECK = 'Master fallback', 'Comparison baseline missing', 'UCL live check'
ODDS_SWITCH = 'Odds provider switch'
EVENTS = (RELEASE, REFIT, STALE, ROLLBACK, SWITCH, MASTER_FALLBACK, BASELINE_MISSING, UCL_CHECK, ODDS_SWITCH)

PUBLISHED, SKIPPED, FAILED = 'PUBLISHED', 'SKIPPED', 'FAILED'
STALE_STARTED, STALE_ENDED = 'STALE FIT WARNING STARTED', 'STALE FIT WARNING ENDED'
TRIGGERED, COMPETITION_WARNING = 'ROLLBACK TRIGGERED', 'CE3n COMPETITION WARNING'
FITS = {'C6': 'C6 live fit (research v5, domestic)', 'CE3n': 'CE3n live fit (research v6, UCL/UEL)'}
SOURCE_CLOSING = 'closing odds'
SOURCE_REFIT, SOURCE_FORECAST, SOURCE_REVIEW, SOURCE_BACKFILL = ('refit workflow', 'forecast run', 'weekly report',
                                                                 'backfill')
SOURCE_RELEASE = 'release PR'  # a release's own lines, written by its PR so the committed log matches the switches
BOT = ('-c', 'user.name=github-actions[bot]', '-c',
       'user.email=41898282+github-actions[bot]@users.noreply.github.com')


# --- the log -----------------------------------------------------------------------------------------------------

def utc_time(value: Any = None) -> datetime:
    if value is None:
        return datetime.now(timezone.utc)
    if isinstance(value, datetime):
        stamp = value
    else:
        stamp = datetime.fromisoformat(str(value).replace('Z', '+00:00'))
    if stamp.tzinfo is None:
        stamp = stamp.replace(tzinfo=timezone.utc)
    return stamp.astimezone(timezone.utc)


def stamps(when: Any = None) -> Dict[str, str]:
    stamp = utc_time(when).replace(microsecond=0)
    return {'recorded_at_utc': stamp.isoformat().replace('+00:00', 'Z'),
            'recorded_at_eat': stamp.astimezone(EAT).strftime('%Y-%m-%d %H:%M EAT')}


def event(kind: str, model: str, outcome: str, details: str, *, key: str, source: str, data: Optional[Mapping] = None,
          when: Any = None, backfilled: bool = False, ident: Optional[str] = None) -> dict:
    """One log line. The id is `ident` or a hash of what the event says and when, so a repeat is recognised."""
    if kind not in EVENTS:
        raise ValueError(f'unknown event {kind!r}')
    record = {'schema': SCHEMA, **stamps(when), 'event': kind, 'model': model, 'outcome': outcome,
              'details': details, 'key': key, 'source': source, 'backfilled': bool(backfilled),
              'data': json.loads(json.dumps(dict(data or {}), default=str, allow_nan=False))}
    if ident is None:
        body = json.dumps({k: record[k] for k in ('recorded_at_utc', 'event', 'model', 'outcome', 'key', 'data')},
                          sort_keys=True)
        ident = hashlib.sha256(body.encode('utf-8')).hexdigest()[:20]
    return {'id': ident, **record}


def read(path: Path | str) -> List[dict]:
    """Every line of the log, oldest first (a torn or foreign line is skipped, never repaired)."""
    path = Path(path)
    if not path.exists():
        return []
    out = []
    for line in path.read_text(encoding='utf-8').splitlines():
        try:
            item = json.loads(line)
        except ValueError:
            continue
        if isinstance(item, dict) and item.get('schema') == SCHEMA:
            out.append(item)
    return out


def append(path: Path | str, events: Iterable[Mapping]) -> List[dict]:
    """Append each event not already in the log (by id); the existing bytes are never touched. Returns what was
    written."""
    path = Path(path)
    seen = {e.get('id') for e in read(path)}
    new = []
    for item in events:
        if item.get('id') in seen:
            continue
        seen.add(item.get('id'))
        new.append(dict(item))
    if not new:
        return []
    path.parent.mkdir(parents=True, exist_ok=True)
    lead = ''
    if path.exists() and path.stat().st_size:
        with path.open('rb') as handle:
            handle.seek(-1, 2)
            lead = '' if handle.read(1) == b'\n' else '\n'  # a torn last line stays as it is, on its own line
    with path.open('a', encoding='utf-8', newline='\n') as handle:
        handle.write(lead + ''.join(json.dumps(e, sort_keys=True, ensure_ascii=False, allow_nan=False) + '\n'
                                    for e in new))
    return new


def last(events: Sequence[Mapping], key: str) -> Optional[Mapping]:
    """The latest event with this key (by time, then order in the file)."""
    found = [(e.get('recorded_at_utc') or '', i, e) for i, e in enumerate(events) if e.get('key') == key]
    return max(found)[2] if found else None


def git(repo: Path, *args: str, check: bool = True) -> subprocess.CompletedProcess:
    return subprocess.run(['git', '-C', str(repo), *args], check=check, text=True, stdin=subprocess.DEVNULL,
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE)


def commit_events(repo: Path | str, events: Sequence[Mapping], message: str, attempts: int = 3) -> bool:
    """Commit just these events on latest main, as the refit and forecast workflows publish (no rebase or force
    push; a race retries on the new head, where an event already there is not written again). Returns whether a
    commit was pushed."""
    repo = Path(repo).resolve()
    with tempfile.TemporaryDirectory(prefix='model-activity-') as temporary:
        for attempt in range(attempts):
            git(repo, 'fetch', 'origin', 'main')
            base = git(repo, 'rev-parse', 'FETCH_HEAD').stdout.strip()
            work = Path(temporary) / f'work-{attempt}'
            git(repo, 'worktree', 'add', '--detach', str(work), base)
            try:
                if not append(work / LOG, events):
                    return False
                git(work, 'add', '--', LOG.as_posix())
                git(work, *BOT, 'commit', '-m', message)
                if git(work, 'push', 'origin', 'HEAD:refs/heads/main', check=False).returncode == 0:
                    return True
                git(repo, 'fetch', 'origin', 'main')
                if git(repo, 'rev-parse', 'FETCH_HEAD').stdout.strip() == base:
                    raise RuntimeError('model activity push failed')
            finally:
                git(repo, 'worktree', 'remove', '--force', str(work), check=False)
    raise RuntimeError('Main kept advancing; model activity not committed')


REQUIRED = ('id', 'schema', 'recorded_at_utc', 'recorded_at_eat', 'event', 'model', 'outcome', 'details', 'key',
            'source', 'backfilled', 'data')


def check(root: Path | str) -> dict:
    """Raises ValueError unless the log under this output root is append-only: every line a complete event with a
    unique id, and (inside a git checkout) the committed file at HEAD a byte-for-byte prefix of the working file, so
    no committed line was edited, reordered or removed. Run by workflow_checks.py reports before anything is
    pushed."""
    path = Path(root) / RELATIVE
    data = path.read_bytes() if path.exists() else b''
    ids = set()
    for number, line in enumerate(data.decode('utf-8').splitlines(), start=1):
        item = json.loads(line)
        missing = [k for k in REQUIRED if k not in item]
        if missing or item['event'] not in EVENTS:
            raise ValueError(f'model activity line {number}: missing {missing} or unknown event {item.get("event")!r}')
        if item['id'] in ids:
            raise ValueError(f'model activity line {number}: repeated id {item["id"]}')
        ids.add(item['id'])
    committed = None
    try:
        top = subprocess.run(['git', '-C', str(path.parent if path.parent.exists() else Path(root)), 'rev-parse',
                              '--show-toplevel'], check=True, capture_output=True, text=True).stdout.strip()
        relative = path.resolve().relative_to(Path(top).resolve()).as_posix()
        shown = subprocess.run(['git', '-C', top, 'show', f'HEAD:{relative}'], capture_output=True)
        committed = shown.stdout if shown.returncode == 0 else None
    except (OSError, ValueError, subprocess.CalledProcessError):
        pass
    if committed is not None and not data.startswith(committed):
        raise ValueError('model activity log changed: a committed line was edited or removed (append only)')
    return {'events': len(ids), 'append_only': 'checked against HEAD' if committed is not None else
            'no committed log to compare with'}


# --- refit workflow ----------------------------------------------------------------------------------------------

def _num(value: Any, digits: int = 4) -> str:
    try:
        return f'{float(value):+.{digits}f}'
    except (TypeError, ValueError):
        return 'none'


def fit_parameters(fit: str, data: Optional[Mapping]) -> Optional[dict]:
    """The latest window of a live fit file: its dates, parameters and the matches they were fitted on."""
    windows = (data or {}).get('windows') or []
    if not windows:
        return None
    w = windows[-1]
    if fit == 'C6':
        return {'origin': w.get('origin'), 'end_exclusive': w.get('end_exclusive'), 'rho': w.get('rho'),
                'delta': w.get('delta'), 'slope': w.get('slope'), 'low_score_matches': w.get('low_score_matches'),
                'slope_matches': w.get('slope_matches'), 'windows': len(windows)}
    f = w.get('factors') or {}
    return {'origin': w.get('origin'), 'end_exclusive': w.get('end_exclusive'), 'factor_status': f.get('status'),
            'factor_matches': f.get('matches'), 'league_strength': f.get('s'), 'competition': f.get('c'),
            'home': f.get('h'), 'domestic_teams': sum(len(t) for t in (w.get('strengths') or {}).values()),
            'windows': len(windows)}


def parameter_text(fit: str, before: Optional[Mapping], after: Optional[Mapping]) -> str:
    """The latest window's parameters, before → after, in words."""
    if not after:
        return ''
    if fit == 'C6':
        pairs = [(name, (before or {}).get(name), after.get(name)) for name in ('rho', 'delta', 'slope')]
        moved = ', '.join(f'{n} {_num(a)} → {_num(b)}' if before else f'{n} {_num(b)}' for n, a, b in pairs)
        return (f'{moved}; fitted on {after.get("low_score_matches")} matches (rho, delta) and '
                f'{after.get("slope_matches")} decided matches (slope)')
    s_before = (before or {}).get('league_strength') or {}
    league = ', '.join(f'{k} {_num(s_before.get(k), 3)} → {_num(v, 3)}' if before else f'{k} {_num(v, 3)}'
                       for k, v in sorted((after.get('league_strength') or {}).items()))
    comp = ', '.join(f'{k} {_num(v, 3)}' for k, v in sorted((after.get('competition') or {}).items()))
    return (f'league factors ({after.get("factor_status")}, {after.get("factor_matches")} European matches): '
            f'{league or "none"}; competition factors {comp or "none"}; domestic strengths for '
            f'{after.get("domestic_teams")} teams')


def refit_event(fit: str, outcome: str, *, origin: Optional[str] = None, reason: str = '',
                previous: Optional[Mapping] = None, new: Optional[Mapping] = None, built: Optional[Mapping] = None,
                when: Any = None, source: str = SOURCE_REFIT, backfilled: bool = False,
                ident: Optional[str] = None) -> dict:
    """One refit of the C6 or CE3n live fit on a fit day: PUBLISHED, SKIPPED or FAILED, with the fit window,
    the latest window's parameters before and after, and the matches used."""
    before, after = fit_parameters(fit, previous), fit_parameters(fit, new)
    window = (f'{after["origin"]} to {after["end_exclusive"]}' if after else
              f'the window opening {origin}' if origin else 'no window')
    name = 'C6' if fit == 'C6' else 'CE3n'
    if outcome == PUBLISHED:
        details = f'Published the live {name} fit for {window}: {parameter_text(fit, before, after)}.'
        if built:
            details += (f' Results to {built.get("last_result_date")}; data checked through '
                        f'{built.get("results_known_through_utc")}.')
        shown = PUBLISHED
    elif outcome == SKIPPED:
        details = (f'Skipped the {window} refit: {reason}. The committed fit stays in place.'
                   + (' Live forecasts warn that their fit is stale until a refresh succeeds.'
                      if 'unchanged' not in reason else ''))
        shown = f'SKIPPED: {reason}'
    elif outcome == FAILED:
        details = (f'Refit for {window} failed: {reason}. The committed fit stays in place; live forecasts warn that '
                   'their fit is stale until a refresh succeeds (rerun the workflow once the results are in).')
        shown = f'FAILED: {reason}'
    else:
        raise ValueError(f'unknown refit outcome {outcome!r}')
    return event(REFIT, FITS[fit], shown[:200], details, key=f'refit:{fit}', source=source, when=when,
                 backfilled=backfilled, ident=ident,
                 data={'fit': fit, 'outcome': outcome, 'origin': origin, 'reason': reason or None,
                       'window': None if not after else {'origin': after['origin'],
                                                         'end_exclusive': after['end_exclusive']},
                       'parameters_before': before, 'parameters_after': after,
                       'matches_used': None if not after else (
                           {'rho_delta': after.get('low_score_matches'), 'slope': after.get('slope_matches')}
                           if fit == 'C6' else {'european': after.get('factor_matches'),
                                                'domestic_teams': after.get('domestic_teams')}),
                       'built_with': dict(built) if built else None})


def classify_failure(exc: BaseException) -> tuple:
    """(SKIPPED, reason) when the data simply was not in yet; (FAILED, reason) otherwise."""
    text = f'{exc}'.strip() or type(exc).__name__
    if isinstance(exc, ValueError) and 'checked 12 hours after' in text:
        return SKIPPED, 'results not in yet (' + text[:240] + ')'
    return FAILED, f'{type(exc).__name__}: {text[:240]}'


def committed(path: Path | str) -> Optional[dict]:
    """A fit file as it stands (the fit live forecasts keep using after a failed refit), or None."""
    try:
        data = json.loads(Path(path).read_text(encoding='utf-8'))
    except (OSError, ValueError):
        return None
    return data if isinstance(data, dict) else None


def record_refit(repo: Path | str, item: Mapping, message: str) -> None:
    """Commit a refit line on its own (skipped or failed). Never raises: the workflow's own result
    stands."""
    try:
        commit_events(repo, [item], message)
    except Exception as exc:  # noqa: BLE001  (reporting only)
        print(f'Model activity not recorded ({type(exc).__name__}: {exc})')


# --- forecast runs -----------------------------------------------------------------------------------------------

def switch_state(master_config: Path | str, research_config: Path | str,
                 cagey_config: Optional[Path | str] = None) -> dict:
    """The release switches and their files' versions, as read now (None where unreadable). With `cagey_config`
    (cagey_correction_config.json) also the cagey correction live per scope (since 17 Nov 2026); a repository
    without that file records no cagey switch."""
    def load(path):
        try:
            data = json.loads(Path(path).read_text(encoding='utf-8'))
        except (OSError, ValueError):
            return {}
        return data if isinstance(data, dict) else {}
    master, research = load(master_config), load(research_config)
    live = research.get('live') if isinstance(research.get('live'), dict) else {}
    state = {'master_live': master.get('live'), 'research_domestic': live.get('domestic'),
             'research_european': live.get('european'), 'master_config_version': master.get('version'),
             'research_config_version': research.get('version')}
    if cagey_config is not None and Path(cagey_config).exists():
        cagey = load(cagey_config).get('cagey_correction_live')
        cagey = cagey if isinstance(cagey, dict) else {}
        # A config without the switch (before 17 Nov 2026) used D everywhere.
        state.update(cagey_domestic=cagey.get('domestic', 'D'), cagey_european=cagey.get('european', 'D'))
    return state


SWITCH_NAMES = {
    'master_live': 'master_shortlist_config.json live (which master is live)',
    'research_domestic': 'research_config.json live.domestic (domestic research version)',
    'research_european': 'research_config.json live.european (UCL/UEL research version)',
    'master_config_version': 'master_shortlist_config.json version',
    'research_config_version': 'research_config.json version',
    'cagey_domestic': 'cagey_correction_config.json cagey_correction_live.domestic (domestic cagey correction)',
    'cagey_european': 'cagey_correction_config.json cagey_correction_live.european (UCL/UEL cagey correction)',
}
# The first forecast run that finds a correction live logs its release once (the moment it took effect).
CAGEY_RELEASES = {
    'D_pow2': ("The cagey correction D_pow2 (power-method grid, the correction fitted on it and the 1X2 set from the "
               'power quote; model cagey-correction-through-2425-power-1x2-v1) became the domestic leagues\' cagey '
               'correction, D kept in shadow; UCL and UEL keep D. Released by its declared holdout test against D '
               '(scored once on 17 Nov 2026: cagey-events-v1 passed, both point estimates not negative; a Bet365 '
               'safety check, not a measure of the live effect). Rollback rule: D_pow2 − D log loss on AH lines with '
               'a 95% interval entirely above zero after 150 graded domestic matches over 3 weeks; rolling back is '
               'setting cagey_correction_live.domestic to "D".'),
}


# Releases of a master by its live switch (master_shortlist_config.json live): logged once, by the release PR
# (SOURCE_RELEASE) or, failing that, by the first forecast run that finds it live.
MASTER_RELEASES = {
    'strong': ("The strong-team master (master-strong-team-v1: at most 6 picks per market group, proven picks first by "
               "league trust and cagey chance of profit, today's fill labelled 'not proven') became the live master "
               "shortlist (master_shortlist.csv, version master-strong-team-v1-live-v11); today's master "
               "(master-new-fill-rule-v4) runs in shadow as master_shortlist_new.csv, the rollback baseline; the old "
               "master (v9) is no longer written. Paul's exception of 23 Nov 2026: offline it showed no measurable "
               "difference from today's master. Rollback rule: after 150 graded matches over 3 weeks on each list, "
               "strong − today's master return per bet with a 95% interval entirely below zero; rolling back is "
               'master_shortlist_config.json live "new". Takes effect with the merge of its PR.'),
}


# Rule changes of the live lists made by editing the live rules (Paul, 24 Nov 2026; docs/plan.md Phase 4d), keyed by
# the strong-master rule each one brought in: logged once, by the first forecast run whose summary records that rule.
RULE_RELEASES = {
    'master-strong-team-v2': {
        'model': 'live lists: odds floor 1.20 (Part 1)', 'before': 'master-strong-team-v1-live-v11',
        'after': 'master-strong-team-v2-live-v12',
        'details': ("Odds must be above 1.20 and at most 2.00 (was 1.15 to 2.00) on the value shortlist "
                    "(local-research-profit-120-200-dc12-v3), the cagey tier (no-loss-market-reference-120-200-v6) and "
                    "the strong master's executable pool (master-strong-team-v2, live master-strong-team-v2-live-v12). "
                    "Paul's exception of 24 Nov 2026: the live rules edited directly, no shadow list, no pre-release "
                    "backtest gate. Rolling back is setting cagey_correction_config.json value_rule and cagey_tier_rule "
                    "to v2 and v5 and the strong master to master-strong-team-v1. Takes effect with the merge of its PR.")},
    'master-strong-team-v3': {
        'model': 'strong master: research no-loss >= 0.70 for all picks (Part 2)',
        'before': 'master-strong-team-v2-live-v12', 'after': 'master-strong-team-v3-live-v13',
        'details': ("Every strong-master pick in every tier (proven, safe, fill, risky fill) needs research no-loss >= "
                    "0.70 on the exact bet (live research v5 domestic, v6 UCL/UEL); an offer with no research view is "
                    "not eligible (R3 extended from UCL/UEL proven picks; master-strong-team-v3, live "
                    "master-strong-team-v3-live-v13). Reviewed once 50 picks under the rule are graded. Paul's "
                    "exception of 24 Nov 2026: no shadow list, no pre-release backtest gate. Rolling back is the "
                    "strong master back to master-strong-team-v2. Takes effect with the merge of its PR.")},
    'master-strong-team-v4': {
        'model': 'strong master: proven ranking without league trust (Part 3)',
        'before': 'master-strong-team-v3-live-v13', 'after': 'master-strong-team-v4-live-v14',
        'details': ("Proven strong-master picks are ranked by the backed team's Elo expected score, then the "
                    "proven-record share on the exact bet, then the cagey chance of profit, then the tie order; league "
                    "trust is a label only for proven picks; the fill steps keep their order (master-strong-team-v4, "
                    "live master-strong-team-v4-live-v14). Paul's exception of 24 Nov 2026: no shadow list, no "
                    "pre-release backtest gate. Rolling back is the strong master back to master-strong-team-v3. Takes "
                    "effect with the merge of its PR.")},
    'master-strong-team-v5': {
        'model': 'strong master: weak-link flags (Part 4)',
        'before': 'master-strong-team-v4-live-v14', 'after': 'master-strong-team-v5-live-v15',
        'details': ("Every strong-master pick is flagged as a weak link (weak_link, weak_link_reasons) when any of "
                    "seven reasons holds: research 8+ points below cagey, either no-loss below 0.75, cagey view missing "
                    "or fallen back to D, a thin record or Elo near the line, Pinnacle's fair probability down 3+ "
                    "points since the earliest snapshot, a not-proven tier, a research warning or stale fit. Flag "
                    "only: no pick is removed or reordered (master-strong-team-v5, live "
                    "master-strong-team-v5-live-v15). Paul's exception of 24 Nov 2026. Rolling back is the strong "
                    "master back to master-strong-team-v4. Takes effect with the merge of its PR.")},
    'master-strong-team-v6': {
        'model': 'strong master: weak-link flags narrowed (Part 5)',
        'before': 'master-strong-team-v5-live-v15', 'after': 'master-strong-team-v6-live-v16',
        'details': ("Weak-link reason (f) fires only for 'not proven: fill' and 'not proven: risky fill' picks, and "
                    "reason (g) only for stale research fits and match-specific quality-review warnings (thin form or "
                    "venue evidence, training cutoff, status or refresh problems, pre-match deadline); routine coverage "
                    "notes stay visible in the research warnings but no longer flag. Flag only (master-strong-team-v6, "
                    "live master-strong-team-v6-live-v16). Paul's exception of 24 Nov 2026. Rolling back is the strong "
                    "master back to master-strong-team-v5. Takes effect with the merge of its PR.")},
    'master-strong-team-v7': {
        'model': 'strong master: weak-link reason (d) for proven picks only (Part 6)',
        'before': 'master-strong-team-v6-live-v16', 'after': 'master-strong-team-v7-live-v17',
        'details': ("Weak-link reason (d) (proven record on fewer than 8 of the last 10 matches, or the backed team's "
                    "Elo expected score within 0.03 of the strong-team line) fires only for picks in the 'proven' "
                    "tier; not-proven picks no longer fire it. Every other reason unchanged. Flag only "
                    "(master-strong-team-v7, live master-strong-team-v7-live-v17). Paul's exception of 24 Nov 2026. "
                    "Rolling back is the strong master back to master-strong-team-v6. Takes effect with the merge of "
                    "its PR.")},
}


def rule_release_event(log: Sequence[Mapping], summary: Mapping, when: Any = None) -> Optional[dict]:
    """The release line of a live-list rule change (RULE_RELEASES), the first time a run records its rule."""
    rule = (summary.get('master_shortlist') or {}).get('rule')
    if rule not in RULE_RELEASES or last(log, f'release:rule {rule}') is not None:
        return None
    item = RULE_RELEASES[rule]
    return event(RELEASE, item['model'], f'RELEASED ({EXCEPTION})', item['details'], key=f'release:rule {rule}',
                 source=SOURCE_FORECAST, when=when,
                 data={'decided': '2026-11-24', 'decision': EXCEPTION, 'rule': rule,
                       'versions': {'before': item['before'], 'after': item['after']},
                       'value_rule': summary.get('value_rule'), 'cagey_tier_rule': summary.get('cagey_tier_rule')})


def master_release_event(log: Sequence[Mapping], state: Mapping, when: Any = None,
                         source: str = SOURCE_FORECAST) -> Optional[dict]:
    """The release line of a master released by its live switch, the first time it is found live."""
    name = state.get('master_live')
    if name not in MASTER_RELEASES or last(log, f'release:master {name}') is not None:
        return None
    return event(RELEASE, 'master shortlist (strong-team master)', f'RELEASED ({EXCEPTION})', MASTER_RELEASES[name],
                 key=f'release:master {name}', source=source, when=when,
                 data={'decided': '2026-11-23', 'decision': EXCEPTION,
                       'versions': {'before': 'master-new-fill-rule-v4-live-v10',
                                    'after': 'master-strong-team-v1-live-v11'}})


def switch_settings_text(state: Mapping) -> str:
    text = (f'master live "{state.get("master_live")}", research domestic "{state.get("research_domestic")}", '
            f'research UCL/UEL "{state.get("research_european")}"')
    if 'cagey_domestic' in state:
        text += (f', cagey correction domestic "{state.get("cagey_domestic")}", '
                 f'cagey correction UCL/UEL "{state.get("cagey_european")}"')
    return text


def switch_event(before: Optional[Mapping], after: Mapping, *, when: Any = None, source: str = SOURCE_FORECAST,
                 backfilled: bool = False, ident: Optional[str] = None, note: str = '') -> Optional[dict]:
    """A Switch change line when `after` differs from `before` (None when nothing changed)."""
    before = dict(before or {})
    changed = {k: [before.get(k), after.get(k)] for k in SWITCH_NAMES if before.get(k) != after.get(k)}
    if not changed:
        return None
    shown = lambda v: 'not set' if v is None else str(v)
    words = '; '.join(f'{SWITCH_NAMES[k]}: {shown(a)} → {shown(b)}' for k, (a, b) in changed.items())
    flips = [k for k in changed if not k.endswith('_version')]
    outcome = ('SWITCH CHANGED: ' + ', '.join(f'{k.replace("research_", "").replace("_live", "")} '
                                              f'{shown(changed[k][0])} → {shown(changed[k][1])}' for k in flips)
               if flips else 'CONFIG VERSION CHANGED')
    model = ', '.join(sorted({'master shortlist' if k.startswith('master') else 'cagey correction'
                              if k.startswith('cagey') else 'research' for k in changed}))
    return event(SWITCH, model, outcome, f'{words}. Now: {switch_settings_text(after)}.' + (f' {note}' if note else ''),
                 key='switches', source=source, when=when, backfilled=backfilled, ident=ident,
                 data={'changed': changed, 'state_before': before or None, 'state_after': dict(after)})


def _decode(value: Any) -> dict:
    if isinstance(value, dict):
        return value
    try:
        out = json.loads(value) if value not in (None, '') else {}
    except (TypeError, ValueError):
        return {}
    return out if isinstance(out, dict) else {}


def stale_state(rows: Iterable[Mapping]) -> Dict[str, Optional[dict]]:
    """Per fit (C6, CE3n): None when no forecast of the run used it, else {'stale', 'origin', 'expected_origin',
    'forecasts', 'stale_forecasts'} from the fits frozen in the run's research."""
    out: Dict[str, Optional[dict]] = {'C6': None, 'CE3n': None}
    for row in rows:
        research = _decode(row.get('team_research_json'))
        for fit, field in (('C6', 'c6_fit'), ('CE3n', 'ce3n_fit')):
            frozen = research.get(field)
            if not isinstance(frozen, dict):
                continue
            item = out[fit] or {'stale': False, 'origin': None, 'expected_origin': None, 'forecasts': 0,
                                'stale_forecasts': 0}
            item['forecasts'] += 1
            if frozen.get('stale'):
                item.update(stale=True, origin=frozen.get('origin'), expected_origin=frozen.get('expected_origin'))
                item['stale_forecasts'] += 1
            elif not item['stale']:
                item.update(origin=frozen.get('origin'), expected_origin=frozen.get('expected_origin'))
            out[fit] = item
    return out


def stale_warning(rows: Iterable[Mapping]) -> Optional[dict]:
    """The run's stale-fit warning, or None when no forecast used a stale fit. Shown at the top of the run summary,
    the shortlist report and the master shortlist outputs (23 Nov 2026: a missed refresh went unnoticed for a
    week); {'text', 'fits'}."""
    fits = {fit: state for fit, state in stale_state(rows).items() if state and state['stale']}
    if not fits:
        return None
    parts = [f"{s['stale_forecasts']} of {s['forecasts']} forecasts used a stale {fit} fit (window from {s['origin']}; "
             f"the window for this day opened {s['expected_origin']})" for fit, s in fits.items()]
    return {'text': 'STALE RESEARCH FIT: ' + '; '.join(parts) + '. Research probabilities are not on the current fit '
                    'until the refit workflow (research-c6-fits.yml) publishes it.', 'fits': fits}


def stale_events(log: Sequence[Mapping], rows: Iterable[Mapping], when: Any = None) -> List[dict]:
    out = []
    for fit, state in stale_state(rows).items():
        if state is None:
            continue  # no forecast used this fit: nothing to say about it
        previous = last(log, f'stale:{fit}')
        was = bool(previous and previous.get('outcome') == STALE_STARTED)
        if state['stale'] == was:
            continue
        name = 'C6' if fit == 'C6' else 'CE3n'
        if state['stale']:
            details = (f'{state["stale_forecasts"]} of {state["forecasts"]} forecasts used a stale {name} fit: the '
                       f'window from {state["origin"]}, while the window for this day opened '
                       f'{state["expected_origin"]} (the fortnightly refresh has not published it).')
        else:
            details = (f'The {name} fit is current again: {state["forecasts"]} forecasts used the window from '
                       f'{state["origin"]}.')
        out.append(event(STALE, FITS[fit], STALE_STARTED if state['stale'] else STALE_ENDED, details,
                         key=f'stale:{fit}', source=SOURCE_FORECAST, when=when, data={'fit': fit, **state}))
    return out


def ucl_event(log: Sequence[Mapping], check: Optional[Mapping], when: Any = None) -> Optional[dict]:
    """The run's UCL live check: logged every time until it has passed once, then only failures."""
    if not isinstance(check, Mapping) or not check.get('ucl_fixtures') and check.get('status') != 'error':
        return None
    status = str(check.get('status') or 'not recorded')
    passed_before = any(e.get('key') == 'ucl_live_check' and e.get('data', {}).get('status') == 'passed' for e in log)
    if passed_before and status not in ('failed', 'error'):
        return None
    problems = [str(p) for p in check.get('problems') or []]
    if status == 'passed':
        details = (f'Research v6 passed the UCL live check on {check.get("ucl_fixtures")} UCL fixtures (competition, '
                   'team mapping, fit window, CE shadow, frozen replay and "unvalidated view"). From now on only '
                   'failures are logged.')
    elif status == 'error':
        details = f'The UCL live check could not run: {check.get("error")}.'
    else:
        details = (f'UCL live check {status} on {check.get("ucl_fixtures")} UCL fixtures'
                   + (f': {"; ".join(problems[:5])}' if problems else '') + '.')
    outcome = 'FAILED' if status in ('failed', 'error') else status
    return event(UCL_CHECK, 'research v6 (CE3n) on UCL', outcome[:200], details, key='ucl_live_check',
                 source=SOURCE_FORECAST, when=when,
                 data={'status': status, 'ucl_fixtures': check.get('ucl_fixtures'), 'checks': check.get('checks'),
                       'problems': problems[:20], 'error': check.get('error')})


def master_events(summary: Mapping, when: Any = None) -> List[dict]:
    import master_shortlist as ms
    status = (summary.get(ms.RELEASE_STATUS_KEY) or {})
    if status.get('status') == ms.NEW_MASTER_FAILED:
        return [event(MASTER_FALLBACK, 'new master', ms.NEW_MASTER_FAILED,
                      f'The new master failed in this run ({status.get("error")}), so the old master was published as '
                      'master_shortlist.csv for this run only; the switch is unchanged and the next run tries the new '
                      'master again.', key='master_fallback', source=SOURCE_FORECAST, when=when,
                      data={'error': status.get('error'), 'generated_at_utc': summary.get('generated_at_utc')})]
    if status.get('status') == ms.BASELINE_MISSING:
        return [event(BASELINE_MISSING, 'old master (shadow)', ms.BASELINE_MISSING,
                      f'The old master shadow failed in this run ({status.get("error")}): the new master was published '
                      'as usual, but this run has no old-master picks for the rollback comparison.',
                      key='baseline_missing', source=SOURCE_FORECAST, when=when,
                      data={'error': status.get('error'), 'generated_at_utc': summary.get('generated_at_utc')})]
    return []


def cagey_release_event(log: Sequence[Mapping], state: Mapping, when: Any = None) -> Optional[dict]:
    """The release line of a domestic cagey correction the first time a forecast run finds it live."""
    name = state.get('cagey_domestic')
    if name not in CAGEY_RELEASES or last(log, f'release:cagey correction {name}') is not None:
        return None
    return event(RELEASE, f'cagey correction {name}, domestic', 'RELEASED (holdout test passed)', CAGEY_RELEASES[name],
                 key=f'release:cagey correction {name}', source=SOURCE_FORECAST, when=when,
                 data={'decided': '2026-11-17', 'decision': 'declared holdout test passed (evaluation/holdout_ledger.json)',
                       'versions': {'before': 'D (cagey-correction-through-2425-v1, proportional grid)',
                                    'after': f'{name} (cagey-correction-through-2425-power-1x2-v1, power grid)'}})


def odds_switch_events(switches: Iterable[Mapping], *, source: str) -> List[dict]:
    """One line per change of serving odds provider (odds_provider.py; switch on only). The id is the switch
    itself, so a switch read again from the summary or the usage log is never logged twice."""
    out = []
    for item in switches or []:
        if not isinstance(item, Mapping):
            continue
        before, after = item.get('from'), item.get('to')
        reasons = ', '.join(f'{k}: {v}' for k, v in (item.get('reasons') or {}).items()) or 'provider available again'
        details = (f'Odds requests moved from {before} to {after}' if after else
                   f'Every odds provider failed (last serving: {before})') +             f" at a {item.get('request')} request for {item.get('league')} ({reasons})."
        ident = 'odds-switch-' + hashlib.sha256(json.dumps(dict(item), sort_keys=True, default=str)
                                                .encode('utf-8')).hexdigest()[:16]
        out.append(event(ODDS_SWITCH, 'odds providers', f"{before} -> {after or 'none'}", details,
                         key='odds_provider_switch', source=source, when=item.get('at_utc'), data=item, ident=ident))
    return out


THE_ODDS_API = 'the-odds-api'  # odds_provider.THE_ODDS_API: serves every request while the switch is off
USAGE_WORKFLOWS = {'scheduled-forecasts': SOURCE_FORECAST, 'closing-odds': SOURCE_CLOSING}


def serving_at_start(block: Optional[Mapping]) -> Optional[Mapping]:
    """Who served a run's first odds request: The Odds API with the switch off (no provider block); otherwise the
    router's first_served, or, for a record written before first_served existed, the first provider in order that
    served anything (exact for a run without switches). None when a routed run served nothing."""
    if not isinstance(block, Mapping):
        return {'provider': THE_ODDS_API, 'switch_off': True}
    first = block.get('first_served')
    if isinstance(first, Mapping):
        return first
    providers = block.get('providers') or {}
    for name in block.get('order') or []:
        if isinstance(providers.get(name), Mapping) and providers[name].get('served'):
            return {'provider': name}
    return None


def run_start_event(before: Optional[str], start: Mapping, *, source: str, stamp: Any) -> dict:
    """One line when a run starts on a different provider from the one serving at the end of the previous run."""
    after = start.get('provider')
    reasons = ', '.join(f'{k}: {v}' for k, v in (start.get('reasons') or {}).items())
    if start.get('switch_off'):
        details = f'Odds provider switch off: The Odds API serves this {source} (the previous run ended on {before}).'
    else:
        details = (f'This {source} started on {after or "none (every provider failed)"}; the previous run ended on '
                   f'{before}' + (f' ({reasons}).' if reasons else '.'))
    when = start.get('at_utc') or stamp
    data = {'from': before, 'to': after, 'request': 'run start', 'run_start': True, 'at_utc': when,
            **{k: start[k] for k in ('reasons', 'league', 'switch_off') if start.get(k)},
            **({'first_request': start['request']} if start.get('request') else {})}
    ident = 'odds-start-' + hashlib.sha256(json.dumps({'source': source, 'from': before, 'to': after, 'at': when},
                                                      sort_keys=True, default=str).encode('utf-8')).hexdigest()[:16]
    return event(ODDS_SWITCH, 'odds providers', f"{before} -> {after or 'none'}", details,
                 key='odds_provider_switch', source=source, when=when, data=data, ident=ident)


def provider_chain_events(runs: Iterable[tuple], *, source: str,
                          before: Optional[str] = THE_ODDS_API) -> tuple:
    """(events, provider serving at the end) over one workflow's runs, oldest first, each (stamp, provider block
    or None). A run-start line wherever a run starts on another provider than the previous run ended on, then the
    run's own switches (the one its first request made is the run-start line instead). Deterministic, so the
    whole usage log can be read again every run: append keeps each line once by id."""
    out: List[dict] = []
    for stamp, block in runs:
        start = serving_at_start(block)
        if start is not None:
            if start.get('provider') != before:
                out.append(run_start_event(before, start, source=source, stamp=stamp))
            before = start.get('provider')
        switches = [s for s in ((block or {}).get('switches') or []) if isinstance(s, Mapping)]
        out += odds_switch_events([s for s in switches if not s.get('run_start')], source=source)
        if switches:
            before = switches[-1].get('to')
    return out, before


def usage_runs(records: Iterable[Mapping], workflow: str) -> List[tuple]:
    """(stamp, provider block or None) for each of a workflow's runs in the committed usage log."""
    return [(r.get('recorded_at_utc'), r.get('odds_provider') if isinstance(r.get('odds_provider'), Mapping) else None)
            for r in records if isinstance(r, Mapping) and r.get('workflow') == workflow]


def usage_log_switch_events(records: Sequence[Mapping]) -> List[dict]:
    """Provider changes of the forecast runs and the closing collector, from the committed usage log
    (odds_api_usage.LOG)."""
    out: List[dict] = []
    for workflow, source in USAGE_WORKFLOWS.items():
        out += provider_chain_events(usage_runs(records, workflow), source=source)[0]
    return out


def closing_switch_events(repo: Path | str) -> List[dict]:
    """The closing collector's provider changes, from the committed usage log."""
    from odds_api_usage import read_log
    return provider_chain_events(usage_runs(read_log(repo), 'closing-odds'), source=SOURCE_CLOSING)[0]


def forecast_events(log: Sequence[Mapping], out_dir: Path | str, master_config: Path | str,
                    research_config: Path | str, when: Any = None,
                    cagey_config: Optional[Path | str] = None, usage_records: Sequence[Mapping] = ()) -> List[dict]:
    """The events of one forecast run, from its run summary and predictions (out_dir) and the switch files. The
    earlier forecast runs in the usage log (usage_records) give the provider this run's start is compared with."""
    from csv_utils import dict_reader
    out_dir = Path(out_dir)
    when = utc_time(when)
    summary = {}
    try:
        summary = json.loads((out_dir / 'conservative_bet_summary.json').read_text(encoding='utf-8'))
    except (OSError, ValueError):
        pass
    summary = summary if isinstance(summary, dict) else {}
    when = utc_time(summary.get('generated_at_utc') or when)
    rows: List[Mapping] = []
    predictions = out_dir / 'all_leagues_predictions.csv'
    if predictions.exists() and predictions.stat().st_size:
        with predictions.open(encoding='utf-8', newline='') as handle:
            rows = list(dict_reader(handle))
    events = []
    previous = last(log, 'switches')
    state = switch_state(master_config, research_config, cagey_config)
    change = switch_event((previous or {}).get('data', {}).get('state_after'), state, when=when)
    if change is not None:
        events.append(change)
    release = cagey_release_event(log, state, when)
    if release is not None:
        events.append(release)
    master_release = master_release_event(log, state, when)
    if master_release is not None:
        events.append(master_release)
    rule_release = rule_release_event(log, summary, when)
    if rule_release is not None:
        events.append(rule_release)
    events += stale_events(log, rows, when)
    events += master_events(summary, when)
    ucl = ucl_event(log, summary.get('ce3n_ucl_live_check'), when)
    if ucl is not None:
        events.append(ucl)
    provider = summary.get('odds_provider')  # odds provider switch on only
    if isinstance(provider, Mapping):
        # A run with the switch off has no stable stamp of its own; the usage log records it from the next run.
        _, before = provider_chain_events(usage_runs(usage_records, 'scheduled-forecasts'), source=SOURCE_FORECAST)
        events += provider_chain_events([(summary.get('generated_at_utc'), provider)], source=SOURCE_FORECAST,
                                        before=before)[0]
    return events


def record_forecast(repo: Path | str, out_dir: Path | str, when: Any = None) -> List[dict]:
    """Append a forecast run's events to the repo's log (never raises: a reporting failure only warns)."""
    import warnings
    repo = Path(repo)
    try:
        from odds_api_usage import read_log
        log = read(repo / LOG)
        usage = read_log(repo)
        return append(repo / LOG, usage_log_switch_events(usage)
                      + forecast_events(log, out_dir, repo / 'master_shortlist_config.json',
                                        repo / 'research_config.json', when, repo / 'cagey_correction_config.json',
                                        usage))
    except Exception as exc:  # noqa: BLE001
        warnings.warn(f'Model activity not recorded for this forecast run ({type(exc).__name__}: {exc})')
        return []


# --- weekly report -----------------------------------------------------------------------------------------------

def report_week(when: Any) -> str:
    iso = utc_time(when).astimezone(EAT).isocalendar()
    return f'{iso[0]}-W{iso[1]:02d}'


def _interval(interval: Any, pct: bool = False) -> str:
    if not interval or len(interval) != 2 or any(v is None for v in interval):
        return 'not computed yet'
    a, b = (float(v) for v in interval)
    return f'{a:+.1%} to {b:+.1%}' if pct else f'{a:+.5f} to {b:+.5f}'


def minimum_progress(matches: Any, need_matches: int, weeks: Any, need_weeks: int) -> str:
    """Progress towards a rollback rule's two minimums, e.g. '40 of 150 graded matches · weeks met (4)'."""
    matches, weeks = int(matches or 0), int(weeks or 0)
    shown = (f'graded matches met ({matches})' if matches >= need_matches else f'{matches} of {need_matches} graded matches')
    return shown + ' · ' + (f'weeks met ({weeks})' if weeks >= need_weeks else f'{weeks} of {need_weeks} weeks')


def master_progress(rollback: Mapping) -> str:
    """Both master lists' progress towards the release rollback rule's minimums."""
    need_m, need_w = int(rollback.get('min_graded_matches', 150)), int(rollback.get('min_weeks', 3))
    return '; '.join(f'{name} {minimum_progress(part.get("graded_matches"), need_m, part.get("weeks"), need_w)}'
                     for name, part in (('new master', rollback.get('new_master') or {}),
                                        ('old master', rollback.get('old_master') or {})))


def _research_state(figures: Mapping, minimum: tuple) -> tuple:
    """(status shown, state compared) of a research rollback check."""
    if figures.get('triggered'):
        return TRIGGERED, TRIGGERED
    if figures.get('eligible'):
        return 'not triggered', 'not triggered'
    if not figures.get('matches'):
        return 'no graded matches yet', 'no graded matches yet'
    return (f'not yet eligible ({minimum_progress(figures.get("matches"), minimum[0], figures.get("weeks"), minimum[1])})',
            'not yet eligible')


def rollback_checks(research: Optional[Mapping], price_edge: Optional[Mapping]) -> List[dict]:
    """Each rollback check's line content: key, model, status, state (compared for changes), details, data."""
    out = []
    rollback = (price_edge or {}).get('master_rollback') or {}
    if rollback:
        status = str(rollback.get('status') or 'not recorded')
        nm, om = rollback.get('new_master') or {}, rollback.get('old_master') or {}
        shown = (TRIGGERED if rollback.get('triggered') else 'not triggered' if status == 'NOT TRIGGERED'
                 else f'not yet eligible ({master_progress(rollback)})' if status == 'WAITING' else status)
        diff = rollback.get('difference')
        out.append({'key': 'rollback:master', 'model': 'new master vs old master', 'status': shown, 'state': status,
                    'details': (f'New master {nm.get("graded_matches", 0)} graded matches over {nm.get("weeks", 0)} '
                                f'weeks, old master {om.get("graded_matches", 0)} over {om.get("weeks", 0)}; new − old '
                                f'return per bet {"not computed yet" if diff is None else f"{float(diff):+.2%}"}, 95% '
                                f'interval {_interval(rollback.get("interval_95"), pct=True)}. '
                                + str(rollback.get('message') or '')).strip(),
                    'data': {'status': status, 'triggered': bool(rollback.get('triggered')),
                             'new_master': nm, 'old_master': om, 'difference': diff,
                             'interval_95': rollback.get('interval_95'),
                             'baseline_missing_runs': rollback.get('baseline_missing_runs')}})
    if not research:
        return out
    import research_monitoring as rm
    v5 = research.get('rollback') or {}
    if v5:
        shown, state = _research_state(v5, (rm.MIN_MATCHES, rm.MIN_WEEKS))
        diff = v5.get('v5_minus_v4_log_loss')
        out.append({'key': 'rollback:v5', 'model': 'research v5 (C6) vs v4, domestic', 'status': shown, 'state': state,
                    'details': (f'{v5.get("matches", 0)} graded matches over {v5.get("weeks", 0)} weeks; v5 − v4 '
                                f'research log loss on AH lines {"not computed yet" if diff is None else f"{diff:+.5f}"}'
                                f', 95% interval {_interval(v5.get("interval_95"))}. Rollback if the interval is '
                                f'entirely above zero after {rm.MIN_MATCHES} matches and {rm.MIN_WEEKS} weeks.'),
                    'data': {k: v5.get(k) for k in ('matches', 'weeks', 'eligible', 'triggered',
                                                     'v5_minus_v4_log_loss', 'interval_95')}})
    ce3n = research.get('ce3n') or {}
    if ce3n:
        shown, state = _research_state(ce3n, (rm.CE3N_MIN_MATCHES, rm.CE3N_MIN_WEEKS))
        diff = ce3n.get('ce3n_minus_ce_log_loss')
        slopes = ((ce3n.get('calibration') or {}).get('slopes') or {})
        out.append({'key': 'rollback:v6', 'model': 'research v6 (CE3n) vs CE, UCL/UEL', 'status': shown,
                    'state': state,
                    'details': (f'{ce3n.get("matches", 0)} graded European matches over {ce3n.get("weeks", 0)} weeks; '
                                f'CE3n − CE research log loss on AH lines '
                                f'{"not computed yet" if diff is None else f"{diff:+.5f}"}, 95% interval '
                                f'{_interval(ce3n.get("interval_95"))}; calibration slopes {_slopes(slopes)}.'),
                    'data': {**{k: ce3n.get(k) for k in ('matches', 'weeks', 'eligible', 'triggered',
                                                          'ce3n_minus_ce_log_loss', 'interval_95')},
                             'slopes': slopes}})
        for code, part in sorted((ce3n.get('by_competition') or {}).items()):
            d = part.get('ce3n_minus_ce_log_loss')
            sl = (part.get('calibration') or {}).get('slopes') or {}
            warn = bool(part.get('warning'))
            out.append({'key': f'rollback:{code}', 'model': f'CE3n vs CE, {code} only',
                        'status': f'{COMPETITION_WARNING} ({code})' if warn else 'no competition warning',
                        'state': COMPETITION_WARNING if warn else 'no warning',
                        'details': (f'{part.get("matches", 0)} graded {code} matches over {part.get("weeks", 0)} weeks; '
                                    f'CE3n − CE {"not computed yet" if d is None else f"{d:+.5f}"}, 95% interval '
                                    f'{_interval(part.get("interval_95"))}; calibration slopes {_slopes(sl)}.'
                                    + (' The interval is entirely above zero before the pooled trigger is eligible: '
                                       'a warning, not a rollback.' if warn else '')),
                        'data': {'matches': part.get('matches'), 'weeks': part.get('weeks'), 'difference': d,
                                 'interval_95': part.get('interval_95'), 'warning': warn, 'slopes': sl}})
    cagey = research.get('cagey') or {}
    if cagey:
        shown, state = _research_state(cagey, (rm.CAGEY_MIN_MATCHES, rm.CAGEY_MIN_WEEKS))
        diff = cagey.get('d_pow2_minus_d_log_loss')
        out.append({'key': 'rollback:cagey', 'model': 'cagey correction D_pow2 vs D, domestic', 'status': shown,
                    'state': state,
                    'details': (f'{cagey.get("matches", 0)} graded domestic matches over {cagey.get("weeks", 0)} weeks; '
                                f'D_pow2 − D log loss on AH lines {"not computed yet" if diff is None else f"{diff:+.5f}"}'
                                f', 95% interval {_interval(cagey.get("interval_95"))}. Rollback if the interval is '
                                f'entirely above zero after {rm.CAGEY_MIN_MATCHES} matches and {rm.CAGEY_MIN_WEEKS} '
                                'weeks.'),
                    'data': {k: cagey.get(k) for k in ('matches', 'weeks', 'eligible', 'triggered',
                                                        'd_pow2_minus_d_log_loss', 'interval_95')}})
    return out


def _slopes(slopes: Mapping) -> str:
    parts = []
    for name in ('CE3n', 'CE'):
        s = slopes.get(name) or {}
        shown = [f'{side} {float(s[side]):.2f}' for side in ('home', 'away') if s.get(side) is not None]
        parts.append(f'{name} {" / ".join(shown) if shown else "not computed yet"}')
    return '; '.join(parts)


def review_events(log: Sequence[Mapping], research: Optional[Mapping], price_edge: Optional[Mapping],
                  when: Any = None) -> List[dict]:
    """One line per check for each report week, and another whenever a check's status changes."""
    when = utc_time(when)
    week = report_week(when)
    out = []
    for check in rollback_checks(research, price_edge):
        previous = last(log, check['key'])
        same_week = previous is not None and report_week(previous['recorded_at_utc']) == week
        if same_week and previous.get('data', {}).get('state') == check['state']:
            continue
        out.append(event(ROLLBACK, check['model'], check['status'][:200], check['details'], key=check['key'],
                         source=SOURCE_REVIEW, when=when,
                         data={**check['data'], 'state': check['state'], 'report_week': week}))
    return out


def record_review(root: Path | str, research: Optional[Mapping], price_edge: Optional[Mapping],
                  when: Any = None) -> List[dict]:
    """Append the review's rollback-check lines to root/model_activity (never raises)."""
    import warnings
    path = Path(root) / RELATIVE
    try:
        return append(path, review_events(read(path), research, price_edge, when))
    except Exception as exc:  # noqa: BLE001
        warnings.warn(f'Model activity not recorded for this review ({type(exc).__name__}: {exc})')
        return []


# --- backfill ----------------------------------------------------------------------------------------------------

EXCEPTION = "Paul's exception"
# From git history (merge commits on main) and the release PRs; the refit workflow (research-c6-fits.yml) had no
# run before this log existed. Times are the merge commits' (the moment each release reached main).
BACKFILL_RELEASES = (
    {'id': 'backfill:release:new-master', 'when': '2026-11-15T05:23:20Z', 'model': 'new master',
     'commit': 'f66efc88a84e1eee8610b67af6f72b9ded9effb8', 'pr': 175,
     'versions': {'before': 'master-profit-15-pinnacle-markets-v9 (old master)',
                  'after': 'master-new-fill-rule-v4-live-v10'},
     'details': ('The new master (fill rule master-new-fill-rule-v4, live version master-new-fill-rule-v4-live-v10) '
                 'became the live master shortlist; the old master (master-profit-15-pinnacle-markets-v9) runs in '
                 "shadow. Paul's exception of 14 Nov 2026: released without waiting for the live comparison verdict. "
                 'Rollback rule: after 150 graded matches over 3 weeks on each list, new − old return per bet with a '
                 '95% interval entirely below zero. PR #175.')},
    {'id': 'backfill:release:research-v5', 'when': '2026-11-15T06:04:52Z', 'model': 'research v5 (C6), domestic',
     'commit': '84172898af9814932a8d2bcd9985afaf55408dba', 'pr': 176,
     'versions': {'before': 'team-form-research-v4', 'after': 'team-form-research-v5'},
     'details': ("Research v5 (C6 low-score sharpening) became the domestic leagues' research model, v4 kept in "
                 "shadow. Paul's exception of 14 Nov 2026: not proven on the holdout. Rollback rule: v5 − v4 research "
                 'log loss on AH lines with a 95% interval entirely above zero after 150 graded matches over 3 weeks. '
                 'PR #176.')},
    {'id': 'backfill:release:research-v6', 'when': '2026-11-15T11:44:02Z', 'model': 'research v6 (CE3n), UCL/UEL',
     'commit': '36580e0f096f39e5e5ea94c106a0484e42d30c78', 'pr': 178,
     'versions': {'before': 'team-form-research-v4 (CE)', 'after': 'team-form-research-v6'},
     'details': ("Research v6 (CE3n: v4's goal rates blended with domestic strength) became the UCL/UEL research "
                 "model, CE (v4) kept in shadow. Paul's exception of 14 Nov 2026: not proven on the European "
                 'holdout. Rollback rule: CE3n − CE research log loss on AH lines with a 95% interval entirely above '
                 'zero after 150 graded European matches over 3 weeks; per-competition warnings. PR #178.')},
)
_V9 = 'master-profit-15-pinnacle-markets-v9'
BACKFILL_SWITCHES = (
    {'id': 'backfill:switch:master-live', 'when': '2026-11-15T05:23:20Z',
     'before': {'master_live': None, 'research_domestic': 'v4', 'research_european': 'v4',
                'master_config_version': _V9, 'research_config_version': None},
     'after': {'master_live': 'new', 'research_domestic': 'v4', 'research_european': 'v4',
               'master_config_version': _V9, 'research_config_version': None},
     'note': ('PR #175 added the live switch to master_shortlist_config.json (before it the old master was the only '
              'live list). Research was v4 everywhere, set in code; research_config.json did not exist yet.')},
    {'id': 'backfill:switch:research-domestic', 'when': '2026-11-15T06:04:52Z',
     'before': {'master_live': 'new', 'research_domestic': 'v4', 'research_european': 'v4',
                'master_config_version': _V9, 'research_config_version': None},
     'after': {'master_live': 'new', 'research_domestic': 'v5', 'research_european': 'v4',
               'master_config_version': _V9, 'research_config_version': None},
     'note': 'PR #176 set domestic research to v5 in code (team_research); the switch moved to research_config.json '
             'live.domestic with PR #178.'},
    {'id': 'backfill:switch:research-european', 'when': '2026-11-15T11:44:02Z',
     'before': {'master_live': 'new', 'research_domestic': 'v5', 'research_european': 'v4',
                'master_config_version': _V9, 'research_config_version': None},
     'after': {'master_live': 'new', 'research_domestic': 'v5', 'research_european': 'v6',
               'master_config_version': _V9, 'research_config_version': 'research-live-switch-v1'},
     'note': 'PR #178 created research_config.json (research-live-switch-v1) with live.domestic "v5" and '
             'live.european "v6".'},
)
# The live fits shipped with the releases (built locally, published on main by the merge); later refits come from
# the workflow and are logged by it.
BACKFILL_FITS = (
    {'id': 'backfill:refit:C6', 'fit': 'C6', 'when': '2026-11-15T06:04:52Z', 'file': 'research_c6_live_fits.json',
     'commit': '50bc4cec9', 'merged_in': 'PR #176'},
    {'id': 'backfill:refit:CE3n', 'fit': 'CE3n', 'when': '2026-11-15T11:44:02Z', 'file': 'research_ce3n_live_fits.json',
     'commit': '4c166c064', 'merged_in': 'PR #178'},
)


def _file_at(repo: Path, commit: str, name: str) -> Optional[dict]:
    """A file as committed (git show), or the working copy when git can't show it."""
    try:
        text = git(repo, 'show', f'{commit}:{name}').stdout
    except (OSError, subprocess.CalledProcessError):
        path = repo / name
        if not path.exists():
            return None
        text = path.read_text(encoding='utf-8')
    return json.loads(text)


def backfill_events(repo: Path | str) -> List[dict]:
    """The releases, switch changes and initial live fits already made, oldest first, marked backfilled; plus any
    master fallback or baseline-missing run found in the archived run summaries since the release."""
    repo = Path(repo)
    out = []
    for r in BACKFILL_RELEASES:
        out.append(event(RELEASE, r['model'], f'RELEASED ({EXCEPTION})', r['details'], key=f'release:{r["model"]}',
                         source=SOURCE_BACKFILL, when=r['when'], backfilled=True, ident=r['id'],
                         data={'commit': r['commit'], 'pr': r['pr'], 'decided': '2026-11-14', 'decision': EXCEPTION,
                               'versions': r['versions']}))
    for s in BACKFILL_SWITCHES:
        out.append(switch_event(s['before'], s['after'], when=s['when'], source=SOURCE_BACKFILL, backfilled=True,
                                ident=s['id'], note=s['note']))
    for f in BACKFILL_FITS:
        data = _file_at(repo, f['commit'], f['file'])
        item = refit_event(f['fit'], PUBLISHED, new=data, built=(data or {}).get('built_with'), when=f['when'],
                           source=SOURCE_BACKFILL, backfilled=True, ident=f['id'])
        item['details'] = (f'Initial live fit, built locally (commit {f["commit"]}) and published on main by '
                           f'{f["merged_in"]}. ' + item['details'])
        out.append(item)
    out += archived_master_events(repo / 'football_output_v2')
    out.sort(key=lambda e: e['recorded_at_utc'])
    return out


def archived_master_events(root: Path) -> List[dict]:
    """Master fallback / baseline-missing runs recorded in archived run summaries (performance/snapshots)."""
    import master_shortlist as ms
    out = []
    base = Path(root) / 'performance' / 'snapshots'
    for path in sorted(base.glob('*/selection_summary.json')) if base.exists() else []:
        if path.parent.name.startswith('.capture-'):
            continue
        try:
            summary = json.loads(path.read_text(encoding='utf-8'))
        except (OSError, ValueError):
            continue
        status = (summary.get(ms.RELEASE_STATUS_KEY) or {}).get('status')
        if status not in (ms.NEW_MASTER_FAILED, ms.BASELINE_MISSING) or not summary.get('generated_at_utc'):
            continue
        for item in master_events(summary, summary['generated_at_utc']):
            item.update(source=SOURCE_BACKFILL, backfilled=True, id=f'backfill:{item["key"]}:{path.parent.name}')
            out.append(item)
    return out


def backfill(repo: Path | str) -> List[dict]:
    """Append the backfilled events not yet in the log (idempotent)."""
    repo = Path(repo)
    return append(repo / LOG, backfill_events(repo))


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('action', choices=('backfill', 'show'))
    parser.add_argument('--repo', type=Path, default=Path(__file__).resolve().parent)
    args = parser.parse_args(argv)
    if args.action == 'backfill':
        written = backfill(args.repo)
        print(f'{len(written)} backfilled events appended to {LOG.as_posix()}')
        return 0
    for item in read(args.repo / LOG):
        print(f"{item['recorded_at_eat']}  {item['event']:<28} {item['model']:<40} {item['outcome']}")
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
