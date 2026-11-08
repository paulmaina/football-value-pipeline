"""V8: fifteen distinct executable nominations with visible frozen context review."""
import pandas as pd
import master_selection_no_totals as previous
from master_selection import identity
from master_context_review import COLUMNS as CONTEXT_COLUMNS, review, INFLUENCE

VERSION = 'master-profit-15-context-v8'
SIZE = 15
AUDIT_FILE = previous.AUDIT_FILE


def evaluate(decisions, predictions, now=None):
    from master_shortlist import COLUMNS_CONTEXT
    audit = previous.evaluate(decisions, predictions, now)
    forecasts = {}
    if predictions is not None:
        for row in predictions.astype(object).where(predictions.notna(), None).to_dict('records'):
            key = identity(row)
            forecasts[key] = row if key not in forecasts else None
    context = [review(forecasts.get(identity(row)), now if now is not None else row.get('evaluated_at_utc'))
               for row in audit.to_dict('records')]
    for column in CONTEXT_COLUMNS:
        audit[column] = [r[column] for r in context]
    for index, item in zip(audit.index, context):
        audit.at[index, 'master_coverage_warning'] = '; '.join(filter(None, [
            audit.at[index, 'master_coverage_warning'], 'context review: '+item['master_context_status'],
            'missing context: '+item['master_context_missing'] if item['master_context_missing'] else '']))
    audit['master_version'] = VERSION
    return audit.reindex(columns=COLUMNS_CONTEXT)


def select(audit):
    from master_shortlist import COLUMNS_CONTEXT
    eligible = audit.loc[audit.master_decision.eq('ELIGIBLE') & ~previous.is_over(audit)
        & ~audit.market.fillna('').str.startswith('Double Chance ')
        & ~audit.master_offer_source_market.eq('double_chance')].copy()
    eligible['_fixture'] = [identity(r) for r in eligible.to_dict('records')]
    ordered = eligible.sort_values(['master_profit_probability', 'master_expected_return',
        'master_no_loss_probability', 'offered_decimal_odds', 'kickoff_utc', 'league', 'home_team',
        'away_team', 'market', 'bookmaker', 'offered_last_update_utc'],
        ascending=[False, False, False, False, True, True, True, True, True, True, False], kind='stable')
    top = ordered.drop_duplicates('_fixture').head(SIZE).copy()
    top['master_rank'] = range(1, len(top)+1)
    top['master_decision'] = 'SHORTLISTED'
    top['master_version'] = VERSION
    result = top.reindex(columns=COLUMNS_CONTEXT).reset_index(drop=True)
    result.attrs['master_version'] = VERSION
    return result


def summary(frame):
    result = previous.summary(frame)
    result.update(version=VERSION, size=SIZE, target_size=SIZE, shortfall=max(0, SIZE-len(frame)),
        context_review_version='master-context-review-v1', context_influence=INFLUENCE,
        context_status_counts={str(k): int(v) for k, v in frame.master_context_status.value_counts().items()},
        context_missing_policy='Remain eligible with explicit warnings; no missing-evidence ranking bonus',
        rule=result['rule'].replace('nominate ten when ten executable', 'nominate fifteen when fifteen executable')
            + '; fifteen-match target, one selection per fixture; frozen training/research/weather review accompanies every pick')
    return result
