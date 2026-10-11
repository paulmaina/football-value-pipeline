"""Strict regulation-time scores shared by training and forward settlement."""


def valid_goals(score):
    if not isinstance(score, dict):
        return None
    h, a = score.get('home'), score.get('away')
    if all(type(x) is int and 0 <= x <= 30 for x in (h, a)):
        return h, a
    return None


def regulation_goals(score):
    if not isinstance(score, dict):
        return None
    duration = score.get('duration')
    if duration in ('EXTRA_TIME', 'PENALTY_SHOOTOUT'):
        return valid_goals(score.get('regularTime'))
    if duration in (None, 'REGULAR'):
        return valid_goals(score.get('fullTime'))
    return None
