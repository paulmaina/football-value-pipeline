"""V7 excludes Over 1.5, retaining the released v6 DC-to-native-AH rules.

Older master selectors remain immutable for archived replay and grading.
"""
import master_selection_ah as previous

VERSION = 'master-profit-no-dc-no-over15-v7'
AUDIT_FILE = previous.AUDIT_FILE
REASON = 'Over 1.5 excluded by master shortlist rule'


def is_over(frame):
    return frame.market.fillna('').eq('Over 1.5') | frame.value_market_group.fillna('').eq('over_1_5')


def evaluate(decisions, predictions, now=None):
    audit = previous.evaluate(decisions, predictions, now)
    excluded = is_over(audit)
    audit.loc[excluded, 'master_decision'] = 'EXCLUDED'
    for index in audit.index[excluded]:
        audit.loc[index, 'master_rejection_reasons'] = '; '.join(filter(None, [
            audit.loc[index, 'master_rejection_reasons'], REASON]))
    audit['master_version'] = VERSION
    return audit


def select(audit):
    result = previous.select(audit.loc[~is_over(audit)].copy())
    result['master_version'] = VERSION
    result.attrs['master_version'] = VERSION
    return result


def summary(frame):
    result = previous.summary(frame)
    result['version'] = VERSION
    result['excluded_markets'] = [*result['excluded_markets'], 'Over 1.5']
    result['rule'] += '; Over 1.5 excluded before ranking; other eligible matches fill the target when available'
    return result
