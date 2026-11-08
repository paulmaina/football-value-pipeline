"""Review frozen pre-kickoff evidence without inventing fitted outcome effects.

Forecast collection owns network access. Selection and replay read only the same
fixture's saved evidence, so later news/weather cannot enter an archived pick.
"""
import json
import pandas as pd
from quote_freshness import quote_utc

VERSION = 'master-context-review-v1'
CATEGORIES = ('form', 'venue_splits', 'xg', 'availability', 'lineups', 'rotation',
              'h2h', 'tactics', 'motivation', 'rivalry', 'weather', 'travel')
COLUMNS = ['master_context_status', 'master_context_observed_utc', 'master_context_coverage',
           'master_context_missing', 'master_training_summary', 'master_form_summary',
           'master_weather_summary', 'master_team_news_summary', 'master_schedule_summary',
           'master_research_sources', 'master_other_context', 'master_context_json']
INFLUENCE = ('Local training and researched form/xG inform source forecasts/nominations; '
             'master probabilities/ranking remain Pinnacle-referenced. Weather, team news, '
             'rest/travel, H2H, tactics and motivation are review context, with no unvalidated numerical adjustment.')


def obj(value):
    if isinstance(value, dict):
        return value
    try:
        parsed = json.loads(value)
    except (TypeError, ValueError):
        return {}
    return parsed if isinstance(parsed, dict) else {}


def clean(value):
    """Only finite JSON primitives; never emit NaN strings or raw response objects."""
    if isinstance(value, dict):
        return {str(k): clean(v) for k, v in value.items()}
    if isinstance(value, list):
        return [clean(v) for v in value]
    if value is None or isinstance(value, (str, bool, int)):
        return value
    if isinstance(value, float) and pd.notna(value) and abs(value) != float('inf'):
        return value
    return None


def dump(value):
    return json.dumps(clean(value), sort_keys=True, allow_nan=False)


def review(forecast, clock):
    forecast = forecast or {}
    clock = quote_utc(clock)
    kick = quote_utc(forecast.get('kickoff_utc'))
    context = obj(forecast.get('team_research_json'))
    stamp = quote_utc(context.get('observed_at_utc'))
    valid = clock is not None and kick is not None and stamp is not None and stamp <= clock < kick
    evidence = obj(context.get('evidence'))
    sources = evidence.get('sources') or []
    valid = valid and isinstance(sources, list) and all(
        isinstance(s, dict) and quote_utc(s.get('observed_at_utc')) is not None
        and quote_utc(s['observed_at_utc']) <= clock for s in sources)
    status = 'UNAVAILABLE' if not context else 'INVALID_TIMING' if not valid else 'PARTIAL'
    if not valid:
        context, evidence, sources = {}, {}, []
    elif clock-stamp > pd.Timedelta(hours=24):
        status = 'STALE_RECHECK'
    coverage = dict(obj(context.get('coverage')))
    # An advertised weather category is insufficient without a complete, dated forecast.
    weather = dict(obj(evidence.get('weather')))
    when = quote_utc(weather.get('observed_at_utc'))
    weather_valid = bool(weather) and when is not None and clock is not None and when <= clock
    hours = weather.get('hours') or []
    expected = set(pd.date_range(kick.floor('h'), (kick+pd.Timedelta(minutes=105)).floor('h'), freq='h')) if kick is not None else set()
    complete_weather = (weather_valid and weather.get('complete_match_window') is True
        and isinstance(hours, list) and len(hours) == len(expected)
        and all(isinstance(h, dict) for h in hours)
        and {quote_utc(h.get('time')) for h in hours} == expected
        and all(all(isinstance(h.get(k), (int, float)) and pd.notna(h[k])
            for k in ('temperature_2m', 'precipitation', 'wind_speed_10m')) for h in hours)
        and all(obj(weather.get('units')).get(k) == v for k, v in
            [('temperature_2m', '°C'), ('precipitation', 'mm'), ('wind_speed_10m', 'km/h')]))
    if weather_valid:
        weather['complete_match_window'] = bool(complete_weather)
    else:
        weather = {}
    if not complete_weather:
        coverage.pop('weather', None)
    missing = [c for c in CATEGORIES if not coverage.get(c)]
    if valid and not missing and status != 'STALE_RECHECK':
        status = 'RECORDED_CATEGORIES_COVERED'
    training = {k: forecast.get(k) for k in ('model_version', 'training_data_status', 'training_cutoff',
                                           'training_refresh_warning')}
    end = quote_utc(training['training_cutoff'])
    if end is not None and (clock is None or end >= clock):
        training = {'warning': 'training cutoff not before evaluation; training evidence unavailable'}
    elif not training.get('training_data_status'):
        training['warning'] = 'training health/status not recorded in forecast row'
    news = [n for n in evidence.get('news', []) if isinstance(n, dict)
            and quote_utc(n.get('published_at_utc')) is not None and clock is not None
            and quote_utc(n['published_at_utc']) <= clock][:5] if isinstance(evidence.get('news', []), list) else []
    availability = evidence.get('availability') if isinstance(evidence.get('availability'), list) else []
    lineups = evidence.get('lineups') if isinstance(evidence.get('lineups'), list) else []
    team_news = {'availability': availability, 'lineups': lineups, 'news_leads': news,
                 'note': 'Provider reports/news leads; confirmation and player-value effects are not inferred'}
    form = obj(context.get('form'))
    schedule = obj(evidence.get('rest_and_travel'))
    source_records = [{k: s.get(k) for k in ('url', 'observed_at_utc', 'status', 'reason')} for s in sources]
    h2h = [r for r in context.get('h2h', []) if isinstance(r, dict)
        and quote_utc(r.get('date')) is not None and quote_utc(r['date']) < clock] if valid and isinstance(context.get('h2h', []), list) else []
    other = {'h2h': h2h, 'motivation': coverage.get('motivation'),
             'tactics': coverage.get('tactics'), 'rivalry': coverage.get('rivalry'),
             'note': 'Descriptive evidence; no fitted outcome coefficients'}
    snapshot = dict(version=VERSION, status=status, observed_at_utc=stamp.isoformat() if valid else None,
        coverage=coverage, missing=missing, training=training, form=form, weather=weather,
        team_news=team_news, rest_and_travel=schedule, sources=source_records,
        other_context=other, warnings=context.get('warnings', []), influence=INFLUENCE)
    return dict(master_context_status=status, master_context_observed_utc=snapshot['observed_at_utc'],
        master_context_coverage=dump(coverage), master_context_missing='; '.join(missing),
        master_training_summary=dump(training), master_form_summary=dump(form),
        master_weather_summary=dump(weather) if weather else 'Unavailable: match-window weather not verified',
        master_team_news_summary=dump(team_news), master_schedule_summary=dump(schedule),
        master_research_sources=dump(source_records), master_other_context=dump(other), master_context_json=dump(snapshot))
