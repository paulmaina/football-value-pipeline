"""Factual pre-match research quality, not a probability or staking coefficient.

Only enrichment adds this review. Archived selection reads its original frozen
context, so older research versions and probabilities remain reproducible.
"""
from team_research import name, number, utc
import pandas as pd

VERSION = 'pre-match-research-quality-v1'


def obj(value):
    return value if isinstance(value, dict) else {}


def assess(row, context, cutoff):
    cutoff = utc(cutoff)
    kick = utc(row.get('kickoff_utc'))
    evidence = obj(context.get('evidence'))
    sources = evidence.get('sources') or []
    sources = [s for s in sources if isinstance(s, dict)] if isinstance(sources, list) else []
    near = pd.notna(kick) and kick-cutoff <= pd.Timedelta(hours=2)
    summary_ttl = 5 if near else 180
    weather_ttl = 15 if near else 180
    warnings = []
    def fresh(stamp, minutes):
        stamp = utc(stamp)
        return pd.notna(stamp) and pd.Timedelta(0) <= cutoff-stamp < pd.Timedelta(minutes=minutes)
    summary_fresh = evidence.get('summary_identity_verified') is True and any(s.get('status') == 'available' and '/summary?' in str(s.get('url', ''))
                        and fresh(s.get('observed_at_utc'), summary_ttl) for s in sources)
    squads = evidence.get('lineups') or []
    squads = [s for s in squads if isinstance(s, dict)] if isinstance(squads, list) else []
    expected = {name(row.get('home_team')), name(row.get('away_team'))}
    seen = set()
    player_ids = set()
    for squad in squads:
        players = squad.get('players') or []
        players = players if isinstance(players, list) else []
        starters = [p for p in players if isinstance(p, dict) and p.get('starter') is True]
        ids = [str(p['id']) for p in starters if p.get('id') is not None]
        if squad.get('confirmed') is True and len(ids) == 11 and len(set(ids)) == 11:
            seen.add(name(squad.get('team')))
            player_ids.update(ids)
    lineups = 'CONFIRMED_FRESH' if summary_fresh and len(squads) == 2 and len(expected) == 2 and len(player_ids) == 22 and seen == expected else 'UNCONFIRMED_OR_STALE'
    if lineups != 'CONFIRMED_FRESH':
        warnings.append('Research review: starting XIs not freshly confirmed for both teams; check before betting tight AH')
    availability = 'PROVIDER_REPORTS_FRESH' if summary_fresh and evidence.get('availability') else 'UNAVAILABLE_OR_STALE'
    if availability != 'PROVIDER_REPORTS_FRESH':
        warnings.append('Research review: missing absence reports do not mean both teams have full squads')
    weather = obj(evidence.get('weather'))
    weather_ok = weather.get('complete_match_window') is True and fresh(weather.get('observed_at_utc'), weather_ttl)
    if not weather_ok:
        warnings.append('Research review: match-window weather missing, incomplete or stale; no numerical weather adjustment')
    form = {}
    for side in ('home', 'away'):
        all_games = obj(obj(context.get('form')).get(side))
        overall, venue = obj(all_games.get('all')), obj(all_games.get('venue'))
        form[side] = {'matches': number(overall.get('matches')) or 0,
                      'venue_matches': number(venue.get('matches')) or 0,
                      'xg_matches': number(overall.get('xg_matches')) or 0}
        if form[side]['matches'] < 5 or form[side]['venue_matches'] < 3:
            warnings.append('Research review: '+side+' form/venue evidence is thin')
        if form[side]['xg_matches'] < 5:
            warnings.append('Research review: '+side+' xG sample below five; goals are not verified xG')
    training = {'status': row.get('training_data_status') or 'NOT_RECORDED', 'cutoff': row.get('training_cutoff')}
    end = utc(training['cutoff'])
    if pd.isna(end) or end >= cutoff:
        warnings.append('Research review: training cutoff missing or not before evaluation')
    if training['status'] == 'NOT_RECORDED':
        warnings.append('Research review: training health/status not recorded')
    elif training['status'] not in ('VERIFIED', 'VERIFIED_WITHIN_24_HOURS', 'VERIFIED_CACHED_HISTORY', 'FRESH'):
        warnings.append('Research review: inspect training status '+str(training['status'])+'; completeness/freshness not established by this review')
    if row.get('training_refresh_warning'):
        warnings.append('Research review: training refresh warning; using cached evidence, inspect cutoff')
    if pd.isna(kick) or pd.isna(cutoff) or cutoff >= kick:
        warnings.append('Research review: pre-match deadline unavailable or passed')
    return {'version': VERSION, 'assessed_at_utc': cutoff.isoformat(),
            'status': 'REVIEW_REQUIRED' if warnings else 'RECORDED_CHECKS_PASSED',
            'lineups': lineups, 'availability': availability,
            'absence_note': 'Reported absences only; not proof of complete coverage or a fitted player-value effect',
            'weather': 'FRESH_COMPLETE_WINDOW' if weather_ok else 'UNAVAILABLE_INCOMPLETE_OR_STALE',
            'summary_max_age_minutes': summary_ttl, 'weather_max_age_minutes': weather_ttl,
            'form': form, 'training': training, 'warnings': warnings,
            'probability_effect': 'NONE; factual coverage/freshness review, not a calibrated confidence score'}
