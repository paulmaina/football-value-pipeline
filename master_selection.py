"""Market-referenced, settlement-aware master selection; no automatic stakes.

Inputs are the union of the two current SHORTLISTED decisions, not every
candidate evaluated by the model. References are reconstructed offline from
this generation's frozen fixture quotes. A 2% net-EV buffer is a provisional
policy, not a confidence bound or a validated profitability claim.
"""
import math
import numpy as np
import pandas as pd

VERSION = 'master-market-value-protection-v3'
MIN_EV = .02
MAX_AGE_MINUTES = 6
SIZE = 10
AUDIT_FILE = 'master_shortlist_audit.csv'
KINDS = ('win', 'half_win', 'push', 'half_loss', 'loss')
EXTRA_COLUMNS = ['master_profit_probability', 'master_expected_return', 'master_push_probability',
    'master_half_loss_probability', 'master_full_loss_probability',
    *['master_p_'+k for k in KINDS], 'master_research_profit_probability',
    'master_corrected_profit_probability', 'master_model_gap', 'master_coverage_warning',
    'master_validation_status', 'master_suggested_stake', 'master_reference_utc',
    'master_decision', 'master_rejection_reasons']


def number(value):
    try:
        n = float(value)
    except (ValueError, TypeError):
        return None
    return n if math.isfinite(n) else None


def settlement(mass, odds, cost):
    """Exact per-unit returns, including the cost on a push and half settlement."""
    p = np.asarray(mass, float)
    if p.shape != (5,) or not np.isfinite(p).all() or (p < 0).any() or (p > 1).any() or abs(p.sum()-1) > 1e-6:
        raise ValueError('invalid settlement distribution')
    returns = np.array([odds-1, (odds-1)/2, 0, -.5, -1])-cost
    w, loss = p[0]+p[1]/2, p[4]+p[3]/2
    if w <= 0:
        raise ValueError('no positive settlement mass')
    return dict(profit=float(p[returns > 1e-12].sum()), no_loss=float(p[returns >= -1e-12].sum()),
                ev=float(p@returns), fair=1+(loss+cost)/w, minimum=1+(loss+cost+MIN_EV)/w)


def identity(row):
    from performance_tracking import fixture_key
    from quote_freshness import quote_utc
    return fixture_key(row), quote_utc(row.get('kickoff_utc'))


def _fresh(stamp, now):
    from quote_freshness import quote_utc
    t = quote_utc(stamp)
    return t is not None and 0 <= (now-t).total_seconds() <= MAX_AGE_MINUTES*60


def _reference(row, forecast, now, fits):
    from cagey_market_basis import binary_market, reference
    from price_edge_shortlist import pinnacle_quotes, market_fit
    from market_implied import margin_distribution
    from narrow_margin import price_distribution
    pin = pinnacle_quotes(forecast)
    binary = binary_market(row)
    if binary is not None:
        record = pin.get('ou15' if binary == 'Over 1.5' else 'h2h')
        if record is None or not _fresh(record[-1], now):
            raise ValueError('fresh independent Pinnacle reference unavailable')
        fair, warning = reference(row, pin, now)
        if fair is None:
            raise ValueError(warning)
        q = 1/fair
        return [q, 0., 0., 0., 1-q], 'Pinnacle margin-free '+binary, record[-1]
    if not str(row.get('market', '')).startswith('Asian Handicap '):
        raise ValueError('market outside master rule')
    side, line = row.get('handicap_side'), number(row.get('handicap_line'))
    if side not in ('home', 'away') or line is None or abs(line*4-round(line*4)) > 1e-9:
        raise ValueError('invalid Asian Handicap side/line')
    key = identity(row)
    if key not in fits:
        fits[key] = market_fit(pin, now, cutoff=True)
    fit, info = fits[key]
    stamps = list(info['input_stamps'].values())
    if not fit.usable or fit.kind != 'B' or not stamps or not all(_fresh(t, now) for t in stamps):
        raise ValueError('fresh uncorrected Pinnacle fit B unavailable')
    from quote_freshness import quote_utc
    clocks = [quote_utc(t) for t in stamps] + [quote_utc(row['offered_last_update_utc'])]
    if (max(clocks)-min(clocks)).total_seconds() > 600:
        raise ValueError('Pinnacle inputs unsynchronized')
    margins, probs = margin_distribution(fit.matrix)
    priced = price_distribution(margins, probs, side, line)
    return [priced['p_'+k] for k in KINDS], 'uncorrected Pinnacle fit B', min(clocks).isoformat()


def evaluate(decisions, predictions, now=None):
    """Return every shortlisted offer, with explicit eligibility and source diagnostics.

    Replay supplies the recorded generation clock; production supplies the new
    run's generation clock. A caller refreshing old files must supply its new
    evaluation clock, not reuse stored quote-age numbers.
    """
    from quote_freshness import quote_utc
    from quote_policy import usable_bookmaker
    from master_shortlist import COLUMNS_V3
    if decisions is None or decisions.empty:
        return pd.DataFrame(columns=COLUMNS_V3)
    records = decisions.astype(object).where(decisions.notna(), None).to_dict('records')
    members = [r for r in records if r.get('decision') == 'SHORTLISTED' or r.get('cagey_tier_decision') == 'SHORTLISTED']
    clocks = {quote_utc(r.get('evaluated_at_utc')) for r in records}
    clock = quote_utc(now) if now is not None else next(iter(clocks)) if len(clocks) == 1 else None
    forecasts = {}
    if predictions is not None:
        for r in predictions.astype(object).where(predictions.notna(), None).to_dict('records'):
            k = identity(r)
            forecasts[k] = r if k not in forecasts else None  # ambiguous fixtures fail closed
    fits, output = {}, []
    for original in members:
        r = dict(original)
        r.update(master_version=VERSION, master_validation_status='UNVALIDATED_SELECTION_RULE',
                 master_suggested_stake=0., master_decision='EXCLUDED', master_rank=None,
                 in_value_shortlist=r.get('decision') == 'SHORTLISTED',
                 in_cagey_tier=r.get('cagey_tier_decision') == 'SHORTLISTED')
        warnings = [str(r.get('research_warnings') or '')]
        try:
            if clock is None or quote_utc(r.get('evaluated_at_utc')) != clock:
                raise ValueError('missing, mixed or outdated evaluation generation')
            if any(not str(r.get(k) or '').strip() for k in ('league', 'home_team', 'away_team')):
                raise ValueError('fixture identity unavailable')
            if 'identity missing or ambiguous' in str(r.get('research_warnings') or ''):
                raise ValueError('research fixture identity ambiguous')
            kick = quote_utc(r.get('kickoff_utc'))
            if kick is None or not clock+pd.Timedelta(minutes=20) <= kick <= clock+pd.Timedelta(hours=48):
                raise ValueError('kickoff outside 20-minute to 48-hour window')
            odds, cost = number(r.get('offered_decimal_odds')), number(r.get('per_stake_cost'))
            if odds is None or not 1.15 < odds <= 2:
                raise ValueError('offered odds outside (1.15, 2.00]')
            if cost is None or not 0 <= cost <= 1:
                raise ValueError('stake cost unavailable or invalid')
            if not usable_bookmaker(r.get('bookmaker')):
                raise ValueError('bookmaker unavailable')
            if not _fresh(r.get('offered_last_update_utc'), clock):
                raise ValueError('offered quote missing, future or older than six minutes')
            forecast = forecasts.get(identity(r))
            if forecast is None:
                raise ValueError('unique same-generation fixture forecast unavailable')
            mass, label, stamp = _reference(r, forecast, clock, fits)
            metrics = settlement(mass, odds, cost)
            r.update(master_probability_basis=label, master_reference_utc=stamp,
                     master_no_loss_probability=metrics['no_loss'], master_profit_probability=metrics['profit'],
                     master_expected_return=metrics['ev'], fair_odds=metrics['fair'],
                     minimum_odds_master=metrics['minimum'], edge=odds/metrics['fair']-1,
                     master_push_probability=mass[2], master_half_loss_probability=mass[3],
                     master_full_loss_probability=mass[4], **{'master_p_'+k:p for k,p in zip(KINDS,mass)})
            for prefix, dest in [('research', 'master_research_profit_probability'), ('corrected', 'master_corrected_profit_probability')]:
                other = [number(r.get(prefix+'_p_'+k)) for k in KINDS]
                if all(p is not None for p in other):
                    try:
                        r[dest] = settlement(other, odds, cost)['profit']
                    except ValueError:
                        warnings.append(prefix+' distribution invalid')
                else:
                    warnings.append(prefix+' distribution unavailable')
            gaps = [abs(r[k]-metrics['profit']) for k in ('master_research_profit_probability','master_corrected_profit_probability') if number(r.get(k)) is not None]
            r['master_model_gap'] = max(gaps) if gaps else None
            if gaps and max(gaps) > .10:
                warnings.append('model disagreement exceeds ten percentage points; review only, no automatic probability adjustment')
            if odds > 1.15*metrics['fair']:
                raise ValueError('suspected price error: above 1.15 x independent market fair')
            r.update(master_price_flag='value' if metrics['ev']+1e-9 >= MIN_EV else 'watchlist: insufficient net EV',
                     master_decision='ELIGIBLE' if metrics['ev']+1e-9 >= MIN_EV else 'WATCHLIST',
                     master_rejection_reasons='' if metrics['ev']+1e-9 >= MIN_EV else 'net expected return below provisional 2% buffer')
            r['odds_event_id'] = forecast.get('odds_event_id')
        except (ValueError, TypeError, KeyError) as exc:
            r['master_rejection_reasons'] = str(exc)
        warnings.append('2% net-EV buffer and model probabilities are not a validated confidence guarantee; confirm lineups and refresh prices before betting')
        r['master_coverage_warning'] = '; '.join(w for w in warnings if w)
        output.append(r)
    return pd.DataFrame(output).reindex(columns=COLUMNS_V3)


def select(audit):
    from master_shortlist import COLUMNS_V3
    eligible = audit.loc[audit.master_decision.eq('ELIGIBLE')].copy()
    if eligible.empty:
        result = pd.DataFrame(columns=COLUMNS_V3)
        result.attrs['master_version'] = VERSION
        return result
    eligible['_fixture'] = [identity(r) for r in eligible.to_dict('records')]
    # Never reward overlap or combine the unvalidated probability sources.
    ordered = eligible.sort_values(['master_no_loss_probability', 'master_profit_probability',
        'master_expected_return', 'offered_decimal_odds', 'kickoff_utc', 'league', 'home_team',
        'away_team', 'market', 'bookmaker', 'offered_last_update_utc'],
        ascending=[False, False, False, False, True, True, True, True, True, True, False], kind='stable')
    top = ordered.drop_duplicates('_fixture').head(SIZE).copy()
    top['master_rank'] = range(1, len(top)+1)
    top['master_decision'] = 'SHORTLISTED'
    return top.reindex(columns=COLUMNS_V3).reset_index(drop=True)


def summary(frame):
    return dict(version=VERSION, size=SIZE, n_bets=len(frame), value_bets=len(frame), below_threshold_bets=0,
        min_edge_for_value=None, min_net_expected_return=MIN_EV, max_quote_age_minutes=MAX_AGE_MINUTES,
        probability_basis='independent margin-free Pinnacle binary reference or uncorrected fit B settlement distribution; no fallback',
        validation_status='UNVALIDATED_SELECTION_RULE', automatic_staking=False,
        rule='Union of value and cagey SHORTLISTED offers only; odds (1.15,2.00]; kickoff 20 minutes–48 hours; '
             'fresh synchronized market references; provisional net EV >=2%; one market per match; '
             'no-loss then positive-return probability then net EV then odds; at most ten; no below-value filler')
