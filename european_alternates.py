"""UCL/UEL alternate lines 48 hours ahead, once a day (plan open item 15; Paul, 23 Nov 2026).

Per-event markets (Pinnacle's alternate goal and handicap lines among them) are fetched only for fixtures inside
the 24-hour shortlist window. UCL and UEL fixtures priced a day or more ahead therefore often had no Pinnacle 2.5
quote and a blank cagey view (all 18 UCL rows of the first live provider run, 23 Nov 2026). On one forecast run a
day, this step extends the per-event window to 48 hours for UCL and UEL, when:

  - the odds-provider switch is on (pinnapi serves the request; with the switch off every request would cost
    Odds API credits);
  - no forecast run of the same UTC day has already run it (the committed usage log: a scheduled-forecasts record
    whose `european_alternates_48h` block says it ran);
  - the daily pinnapi projection stays within 80 of the 100 a day: the busy-day projection from the usage log
    (odds_provider.daily_projection, which counts this step's earlier requests) plus this run's extra requests so
    far plus one request per extra fixture (the upper bound: a per-event request needs at most one board request).

Nothing else changes: the shortlist, cagey tier and master keep their 24-hour kickoff window, so the extra
fixtures reach only the readable views (cagey view, quotes) and the totals anchor, which a per-event 2.5 quote
applies to the forecast exactly as it does inside 24 hours. The run records what the step did in its summary and
usage record (`european_alternates_48h`).
"""
from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, Dict, Iterable, Mapping, Optional

LEAGUES = ('UCL', 'UEL')
HOURS = 48
LIMIT = 80          # of pinnapi's 100 requests a day
KEY = 'european_alternates_48h'
WORKFLOW = 'scheduled-forecasts'


def ran_today(records: Iterable[Mapping], now: datetime) -> bool:
    """True when a forecast run of `now`'s UTC day already ran this step (committed usage log)."""
    day = now.astimezone(timezone.utc).date().isoformat()
    return any(isinstance(r, Mapping) and r.get('workflow') == WORKFLOW
               and str(r.get('recorded_at_utc') or '')[:10] == day
               and isinstance(r.get(KEY), Mapping) and r[KEY].get('ran') for r in records)


class Step:
    """This run's decisions, one per league with extra fixtures; summarised into the run summary."""

    def __init__(self, records: Iterable[Mapping], now: datetime, *, routed: bool, limit: int = LIMIT):
        self.records = [r for r in records if isinstance(r, Mapping)]
        self.now = now
        self.routed = routed
        self.limit = limit
        self.already = ran_today(self.records, now)
        self.projection: Optional[float] = None
        self.requests = 0       # extra per-event requests made by this step this run
        self.leagues: Dict[str, Dict[str, Any]] = {}

    def _busy(self) -> float:
        if self.projection is None:
            import odds_provider
            try:
                self.projection = float(odds_provider.daily_projection(self.records)['busy_day'])
            except Exception:  # noqa: BLE001 -- no projection, no step
                self.projection = float('inf')
        return self.projection

    def allow(self, league_key: str, extra: int) -> bool:
        """Whether `league_key`'s `extra` fixtures kicking off 24-48 hours ahead get per-event requests now."""
        if league_key not in LEAGUES or extra <= 0:
            return False
        if not self.routed:
            reason, ok = 'odds provider switch off', False
        elif self.already:
            reason, ok = 'already ran today', False
        else:
            projected = self._busy() + self.requests + extra
            ok = projected <= self.limit
            reason = (f'projected {projected:g} of {self.limit} a day' if ok else
                      f'skipped: projected {projected:g} would exceed {self.limit} a day')
        self.leagues[league_key] = {'extra_fixtures': extra, 'allowed': ok, 'reason': reason}
        return ok

    def count(self, league_key: str) -> None:
        self.requests += 1
        item = self.leagues.setdefault(league_key, {})
        item['requests'] = item.get('requests', 0) + 1

    def summary(self) -> Optional[dict]:
        """The run's record of the step, or None when no UCL/UEL fixture kicked off 24-48 hours ahead."""
        if not self.leagues:
            return None
        return {'ran': any(v.get('allowed') for v in self.leagues.values()), 'hours': HOURS, 'limit': self.limit,
                'busy_day_projection_before': None if self.projection in (None, float('inf')) else self.projection,
                'requests': self.requests, 'leagues': self.leagues}
