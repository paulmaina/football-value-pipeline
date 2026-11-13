"""CE2, CE3 (and CE3n) and CE4 against CE on European development and validation (Phase 2c).

Reads a locked European harness run (`python evaluation_harness.py --mode european --output DIR`).
Only development and validation rows are read; a European holdout row anywhere aborts the report.
Retrospective rows (already scored elsewhere) are never summarised. Results only: no market reference.

For each candidate: CE minus candidate log loss (positive = candidate better) with a 95% interval from
resampling whole calendar weeks, on 1X2, AH all lines (primary), AH draw-sensitive (0, +/-0.5) and Over 1.5;
overall, by competition, by stage, and on the fixtures where both teams have domestic form (CE3 used its
domestic strength). Logistic calibration slopes and calibration rules v2 and v3 (v3: each slope in
0.90-1.10 or closer to 1 than CE's on the same fixtures; pass or fail) per candidate, competition and stage. The walk-forward fits: CE2's slope and the rule's choice, CE4's slope, the
league-strength factors. Views after a warm-up and the domestic-form subset are labelled context: they
were not declared beforehand.

    python scripts/european_candidates_report.py --run DIR --output evaluation/european_candidates
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

import pandas as pd

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO))
PHASES = ('development', 'validation')
CANDIDATES = ('CE2', 'CE2p', 'CE2c', 'CE3', 'CE3n', 'CE4')
GROUPS = ('AH all', 'AH draw-sensitive', '1X2', 'Over 1.5')


def comparisons(scores, baseline='CE', candidates=CANDIDATES):
    import evaluation_harness as eh
    out = {}
    for cand in candidates:
        out[cand] = {g: eh.paired(scores.loc[scores.group == g], baseline, cand) for g in GROUPS}
    return out


def means(scores, candidates=('CE',) + CANDIDATES):
    import evaluation_harness as eh
    return {c: {g: eh.week_mean(scores.loc[(scores.group == g) & (scores.candidate == c)]) for g in GROUPS}
            for c in candidates}


def calibration(forecasts, cfg, candidates=('CE',) + CANDIDATES, baseline='CE'):
    import evaluation_harness as eh
    rule = cfg['calibration_tolerance']
    further = {n: r for n, r in eh.calibration_rules(cfg).items() if n != rule['name'] and eh.is_1x2_rule(r)}

    def rows_of(cand):
        return [{'probs': [r.p_home, r.p_draw, r.p_away], 'outcome': int(r.outcome), 'fixture_key': r.fixture_key}
                for r in forecasts.loc[forecasts.candidate == cand].itertuples(index=False)]
    base_rows = rows_of(baseline)
    out = {}
    for cand in candidates:
        rows = rows_of(cand)
        check = eh.calibration_check(rows, rule)
        relative = {}
        for name, r in further.items():
            c = eh.calibration_check(rows, r, base_rows)
            relative[name] = {'baseline': baseline, 'passes': c['passes'], 'slopes_pass': c['slopes_pass'],
                              'bands_pass': c['bands_pass'], 'relative_slopes': c.get('relative_slopes')}
        out[cand] = {'forecasts': check['forecasts'], 'slopes': check['slopes'], 'slopes_pass': check['slopes_pass'],
                     'failing_bands': check['failing_bands'], 'passes_v2': check['passes'],
                     'further_rules': relative,
                     'mean_forecast': {o: float(forecasts.loc[forecasts.candidate == cand, 'p_' + o].mean())
                                       for o in ('home', 'draw', 'away')},
                     'observed': {o: float((forecasts.loc[forecasts.candidate == cand].outcome == k).mean())
                                  for k, o in enumerate(('home', 'draw', 'away'))}}
    return out


def view(scores, forecasts, cfg):
    return {'log_loss': means(scores), 'ce_minus_candidate': comparisons(scores), 'calibration': calibration(forecasts, cfg)}


def fits_summary(results):
    fits = next(f['walk_forward_fits'] for f in results['folds'] if f.get('candidate') == 'CE2-CE4')
    rows = []
    for f in fits:
        rows.append({'origin': f['origin'], 'scored': f['scored_matches'], 'rule': f['CE2']['rule'],
                     'ce2_pooled': f['CE2']['pooled']['slope'], 'ce2_pooled_status': f['CE2']['pooled']['status'],
                     'ce2_ucl': f['CE2']['per_competition']['UCL']['slope'], 'ce2_uel': f['CE2']['per_competition']['UEL']['slope'],
                     'decided_ucl': f['CE2']['decided']['UCL'], 'decided_uel': f['CE2']['decided']['UEL'],
                     'ce4_pooled': f['CE4']['pooled']['slope'], 'ce4_status': f['CE4']['pooled']['status'],
                     'factors_status': f['factors']['xg']['status'], 'factors_matches': f['factors']['xg']['matches'],
                     'domestic_used': f['domestic_used'], 'factors_xg': f['factors']['xg'].get('s'),
                     'factors_goals': f['factors']['goals'].get('s')})
    frame = pd.DataFrame(rows)
    fitted = frame.loc[frame.ce2_pooled_status == 'fitted']
    factors = frame.loc[frame.factors_status == 'fitted']
    return frame, {
        'folds': len(frame),
        'rule_choice': frame.rule.value_counts().to_dict(),
        'ce2_first_fitted_fold': fitted.origin.min() if len(fitted) else None,
        'ce2_pooled_slope': {'min': float(fitted.ce2_pooled.min()), 'median': float(fitted.ce2_pooled.median()),
                             'max': float(fitted.ce2_pooled.max()), 'last': float(fitted.ce2_pooled.iloc[-1])} if len(fitted) else None,
        'ce4_slope': {'min': float(fitted.ce4_pooled.min()), 'median': float(fitted.ce4_pooled.median()),
                      'max': float(fitted.ce4_pooled.max()), 'last': float(fitted.ce4_pooled.iloc[-1])} if len(fitted) else None,
        'max_decided_before_origin': {'UCL': int(frame.decided_ucl.max()), 'UEL': int(frame.decided_uel.max())},
        'factors_first_fitted_fold': factors.origin.min() if len(factors) else None,
        'factors_last': {'xg': factors.factors_xg.iloc[-1], 'goals': factors.factors_goals.iloc[-1]} if len(factors) else None,
    }


def main(argv=None):
    import evaluation_harness as eh
    parser = argparse.ArgumentParser()
    parser.add_argument('--run', type=Path, required=True)
    parser.add_argument('--output', type=Path, default=REPO / 'evaluation' / 'european_candidates')
    args = parser.parse_args(argv)
    cfg = json.loads((REPO / 'evaluation_harness_config.json').read_text(encoding='utf-8'))
    results = json.loads((args.run / 'results.json').read_text(encoding='utf-8'))
    if results.get('mode') != 'european':
        raise SystemExit('Not a locked European run')
    scores = pd.read_csv(args.run / 'fixture_scores.csv')
    forecasts = pd.read_csv(args.run / 'forecasts_1x2.csv')
    if (scores.phase == 'holdout').any() or (forecasts.phase == 'holdout').any():
        raise SystemExit('A European holdout row is in the run: refusing to report')
    stage = dict(zip(forecasts.fixture_key, forecasts.stage_group))
    scores['stage_group'] = scores.fixture_key.map(stage)
    domestic = set(forecasts.loc[(forecasts.candidate == 'CE3') & forecasts.domestic_used, 'fixture_key'])
    domestic_goals = set(forecasts.loc[(forecasts.candidate == 'CE3n') & forecasts.domestic_used, 'fixture_key'])
    fit_frame, fit_summary = fits_summary(results)
    post = fit_summary['ce2_first_fitted_fold']
    out = {'run_commit': results.get('source_commit'), 'candidates': {c: results['candidates'][c] for c in ('CE',) + CANDIDATES},
           'fits': fit_summary, 'periods': {}}
    for name in PHASES:
        s = scores.loc[scores.phase == name]
        f = forecasts.loc[forecasts.phase == name]
        p = {'fixtures': int(s.loc[s.candidate == 'CE'].fixture_key.nunique()),
             'domestic_used_fixtures': int(len(domestic & set(f.fixture_key))),
             'domestic_used_fixtures_goals_only': int(len(domestic_goals & set(f.fixture_key))),
             'overall': view(s, f, cfg),
             'by_competition': {c: view(s.loc[s.league == c], f.loc[f.league == c], cfg) for c in sorted(s.league.unique())},
             'by_stage': {f'{c} {g}': view(s.loc[(s.league == c) & (s.stage_group == g)],
                                           f.loc[(f.league == c) & (f.stage_group == g)], cfg)
                          for c, g in sorted(set(zip(s.league, s.stage_group)))},
             'context_domestic_form_subset': view(s.loc[s.fixture_key.isin(domestic)], f.loc[f.fixture_key.isin(domestic)], cfg)}
        if post is not None:
            later = s.loc[s.fixture_key.str.split('|').str[1] >= post]
            p['context_after_ce2_warm_up'] = {'from': post, 'fixtures': int(later.loc[later.candidate == 'CE'].fixture_key.nunique()),
                                              'ce_minus_candidate': comparisons(later)}
        out['periods'][name] = p
    args.output.mkdir(parents=True, exist_ok=True)
    eh.hb.write_json(args.output / 'summary.json', out)
    fit_frame.drop(columns=['factors_xg', 'factors_goals']).to_csv(args.output / 'walk_forward_fits.csv', index=False)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
