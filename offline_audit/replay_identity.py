"""One-off offline production release check. No production imports are modified."""
from argparse import ArgumentParser
from collections import Counter
import json
from pathlib import Path

import numpy as np
import pandas as pd

import ah_close_backtest as ah
import europa_training
import performance_tracking as pt
import price_edge_shortlist as pe
import profit_shortlist as pr
from quote_freshness import quote_is_fresh
from research_backtest import KINDS, matrix_value
from team_research import decode, utc

ROOT = Path('football_output_v2')
TEST_START = pd.Timestamp('2026-11-01', tz='UTC')
TEST_END = pd.Timestamp('2026-11-10', tz='UTC')
PIN = {'allowed_bookmakers': ['Pinnacle'], 'per_stake_cost_bps': 0}
coverage = Counter()
roster = {}
result_rows = []
all_snapshots = pt.snapshots(ROOT)
for meta, predictions, _ in all_snapshots:
    generated, captured = (utc(meta[k]) for k in ('generated_at_utc', 'captured_at_utc'))
    summary = pt.load_json(ROOT/'performance'/'snapshots'/meta['git_commit_sha'][:16]/'selection_summary.json', {})
    if summary.get('value_rule') != pr.RULE_V2:
        continue
    for row in predictions:
        kick = utc(row.get('kickoff_utc'))
        if (pd.isna(kick) or not TEST_START <= kick < TEST_END
                or not generated + pd.Timedelta(minutes=20) <= kick <= generated + pd.Timedelta(hours=24)
                or captured > kick - pd.Timedelta(minutes=20) or captured < generated):
            continue
        key = pt.fixture_key(row)
        if key not in roster or generated > roster[key][0]:
            roster[key] = generated, row, summary

verified = pt.load_json(ROOT/'performance'/'verified_results.json', {})
verified = [r for r in verified.values() if isinstance(r, dict) and pt.verified_result_source(r)]
# Reviewed provider-name pairs from the failed bindings. Scope to the competition.
# Only recover a unique result with exact kickoff and both sides in the same order.
PAIRS = {
    'PD': [('Athletic Bilbao', 'Athletic Club'), ('Celta Vigo', 'RC Celta de Vigo'), ('Levante', 'Levante UD')],
    'DED': [('FC Twente Enschede', "FC Twente '65"), ('AZ Alkmaar', 'AZ'), ('NEC Nijmegen', 'NEC')],
    'SA': [('Como', 'Como 1907')],
    'FL1': [('Rennes', 'Stade Rennais FC 1901'), ('Lille', 'Lille OSC'),
            ('Angers', 'Angers SCO'), ('Nice', 'OGC Nice')],
    'PPL': [('Nacional', 'CD Nacional'), ('CF Estrela', 'CF Estrela da Amadora'),
            ('Benfica', 'Sport Lisboa e Benfica')],
}
aliases = {(code, pt.canonical_team_key(provider)): pt.canonical_team_key(result)
           for code, pairs in PAIRS.items() for provider, result in pairs}

def exact_result(row):
    code = pt.LEAGUE_CODES.get(row.get('league'))
    if code not in PAIRS:
        return None
    sides = [pt.canonical_team_key(row[side + '_team']) for side in ('home', 'away')]
    names = [aliases.get((code, side), side) for side in sides]
    if sides == names:
        return None
    found = []
    for result in verified:
        if result['league_code'] != code or utc(result.get('kickoff_utc')) != utc(row.get('kickoff_utc')):
            continue
        if all(n in {pt.canonical_team_key(result.get(side + '_team') or ''),
                     pt.canonical_team_key(result.get(side + '_short_name') or '')}
               for n, side in zip(names, ('home', 'away'))):
            found.append(result)
    return found[0] if len(found) == 1 else None

physical_roster = {}
for key, (now, row, summary) in sorted(roster.items()):
    final, status = pt.fixture_match(row, verified)
    if final is None and status == 'UNVERIFIED_FIXTURE_OR_RESULT':
        final = exact_result(row)
        if final is not None:
            coverage[(row['league'], 'recovered_verified_result')] += 1
    identity = (final['league_code'], final['match_id']) if final else (None, key)
    if identity in physical_roster:
        coverage[(row['league'], 'duplicate_result_identity')] += 1
        if now <= physical_roster[identity][0]:
            continue
    physical_roster[identity] = now, row, summary, final

for key, (now, row, summary, final) in sorted(physical_roster.items(), key=lambda i: str(i[0])):
    key = '|'.join(map(str, key))

    league = row['league']
    coverage[(league, 'fixtures')] += 1
    if final is None:
        coverage[(league, 'ungraded')] += 1
        continue
    coverage[(league, 'graded')] += 1
    if europa_training.eligibility(row):
        coverage[(league, 'training_unverified')] += 1
        continue
    try:
        if row.get('score_matrix_version') != 'published-score-matrix-v1':
            raise ValueError('Missing or unknown version')
        proposed = matrix_value(row['score_matrix_json'])
    except (ValueError, TypeError, KeyError):
        coverage[(league, 'grid_unavailable')] += 1
        continue
    frozen = decode(row.get('team_research_json'))
    if not frozen or pd.isna(utc(frozen.get('observed_at_utc'))) or utc(frozen['observed_at_utc']) > now:
        coverage[(league, 'form_unavailable')] += 1
        continue
    policy = summary.get('quote_execution_policy')
    if not isinstance(policy, dict):
        coverage[(league, 'cost_unavailable')] += 1
        continue
    from quote_policy import validate_policy
    cost = validate_policy(policy)['per_stake_cost_bps']/10000
    pin = pe.pinnacle_quotes(row)
    fit, info = pe.market_fit(pin, now, cutoff=True)
    matrices = {'grid': proposed}
    if fit.usable:
        matrices['pinnacle'] = matrix_value(fit.matrix)
    picks = pe.offered_candidates(row, PIN)
    for item in pr.dc12_candidates(row, pin, fit, info, now, PIN):
        picks.append({'side': None, 'line': None, 'market': item['market'],
                      'price': item['offered_decimal_odds'], 'stamp': item['offered_last_update_utc']})
    unique = {}
    for p in picks:
        stamp = utc(p['stamp'])
        if pd.isna(stamp) or stamp > now or not quote_is_fresh(stamp, now) or not 1.15 < p['price'] <= 2:
            continue
        identity = p['market'], p['side'], p['line']
        if identity not in unique or (stamp, p['price']) > unique[identity][0]:
            unique[identity] = (stamp, p['price']), p
    if not unique:
        coverage[(league, 'no_fresh_pinnacle_offer')] += 1
        continue
    scored = False
    for _, p in unique.values():
        side, line = p['side'], p['line']
        m = p['market']
        old = pr.probabilities(row, {'market': m, 'handicap_side': side, 'handicap_line': line}, frozen)
        if old is None:
            coverage[(league, 'missing_form_offer')] += 1
            continue
        scores = {'current': old}
        hg, ag = final['home_goals'], final['away_goals']
        margin = hg - ag
        for candidate, grid in matrices.items():
            h, a = np.indices(grid.shape)
            if m == 'Double Chance 12':
                win = float(grid[h != a].sum())
                scores[candidate] = dict(zip(KINDS, (win, 0, 0, 0, 1-win)))
            else:
                scores[candidate] = ah.outcome_probabilities(((1 if side == 'home' else -1)*(h-a)).ravel(), grid.ravel(), line)
        won, lost = (float(margin != 0), float(margin == 0)) if m == 'Double Chance 12' else ah.settle((1 if side == 'home' else -1)*margin, line)
        outcome = {(1, 0): 0, (.5, 0): 1, (0, 0): 2, (0, .5): 3, (0, 1): 4}[(float(won), float(lost))]
        returns = np.array([p['price']-1, (p['price']-1)/2, 0., -.5, -1.]) - cost
        truth = int(returns[outcome] > 1e-12)
        scores_out = {}
        for name, values in scores.items():
            mass = np.array([values[k] for k in KINDS])
            assert np.isfinite(mass).all() and (mass >= -1e-10).all() and abs(mass.sum()-1) < 1e-6
            positive = float(np.clip(mass[returns > 1e-12].sum(), 0., 1.))
            scores_out.update({f'{name}_loss': -np.log(max(mass[outcome], 1e-15)),
                               f'{name}_brier': ((mass-np.eye(5)[outcome])**2).sum(),
                               f'{name}_positive': positive, f'{name}_positive_brier': (positive-truth)**2,
                               f'{name}_positive_loss': -np.log(max(positive if truth else 1-positive, 1e-15))})
        result_rows.append({'fixture': key, 'league': league, 'date': row['kickoff_utc'][:10], 'market': m,
                            'line': line, 'truth': truth, **scores_out})
        scored = True
    if scored:
        coverage[(league, 'paired_current_grid')] += 1
        if fit.usable:
            coverage[(league, 'paired_all_three')] += 1

df = pd.DataFrame(result_rows)
parser = ArgumentParser(description=__doc__)
parser.add_argument('--output-dir', type=Path, default=Path('workflow_artifacts/shortlist-audit'))
out = parser.parse_args().output_dir
out.mkdir(parents=True, exist_ok=True)
df.to_csv(out/'identity_matched_offers.csv', index=False)
cover = pd.Series(coverage).unstack(fill_value=0)
print('Valid snapshots:', len(all_snapshots))
print(cover.to_string())
print('Total:', cover.sum().to_dict())
def show(label, data):
    if data.empty:
        return
    by = data.groupby(['fixture', 'date']).mean(numeric_only=True)
    weeks = pd.to_datetime(by.index.get_level_values('date')).to_period('W')
    print(label, 'fixtures', len(by), 'weeks', len(weeks.unique()), 'offers', len(data))
    print(by.mean().round(5).to_dict())
    if len(weeks.unique()) >= 2:
        diffs = (by.current_loss-by.grid_loss).groupby(weeks).agg(['sum','count'])
        ix = np.random.default_rng(134).integers(0, len(diffs), (10000, len(diffs)))
        sample = diffs['sum'].to_numpy()[ix].sum(axis=1)/diffs['count'].to_numpy()[ix].sum(axis=1)
        print('Current-minus-grid log loss, descriptive weekly 95% interval:', np.quantile(sample, [.025,.975]))
if not df.empty:
    show('All eligible offers, current and proposed', df.drop(columns=[c for c in df if c.startswith('pinnacle_')]))
    show('All three, same offers', df.dropna(subset=['pinnacle_loss']) if 'pinnacle_loss' in df else df.iloc[0:0])
    native = df[df.market.str.startswith('Asian Handicap')]
    show('Native AH, primary settlement metric', native)
    show('Draw-sensitive native AH -0.5 to +0.5', native[native.line.abs().le(.5)])
    for league, part in df.groupby('league'):
        show(league, part)
