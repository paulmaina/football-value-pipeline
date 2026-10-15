import copy
from datetime import timedelta
import hashlib
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
from functools import partial

import numpy as np
import pandas as pd

import model_reliability_experiment as m
from football_value_pipeline_v2_standalone import DixonColesModel, build_parser, main
from performance_tracking import capture, snapshots, write_json, verified_record
from test_benchmark_forward_experiment import NOW
from test_performance_tracking import final


class ToyModel:
    fits = []
    def __init__(self, **settings):
        self.settings = settings
    def fit(self, history):
        self.fits.append((self.settings.copy(), history.copy(deep=True)))
        return self
    def score_matrix(self, home, away):
        matrix = np.array([[.1, .1, .03], [.15, .2, .07], [.15, .1, .1]])
        return matrix, {'home_name_match_score': 100, 'away_name_match_score': 100}


def inputs():
    matrix, _ = ToyModel().score_matrix('Home', 'Away')
    probs = m.probabilities(matrix)
    row = {'league': 'Premier League', 'home_team': 'Manchester City FC', 'away_team': 'Everton FC',
           'model_home_team': 'Manchester City FC', 'model_away_team': 'Everton FC',
           'home_name_match_score': 100, 'away_name_match_score': 100,
           'kickoff_utc': (NOW+timedelta(days=1)).isoformat(),
           'market_weight': .5, 'market_blend_applied': False}
    row.update({k: v for k, v in probs.items() if k.startswith('p_')})
    row.update({'p_'+k: v for k, v in probs.items() if not k.startswith('p_')})
    row.update({'raw_'+k: v for k, v in probs.items() if k.startswith('p_')})
    history = pd.DataFrame({'Date': pd.to_datetime(['2026-10-01', '2026-10-02']),
                            'HomeTeam': ['Home', 'Away'], 'AwayTeam': ['Away', 'Home'],
                            'FTHG': [2, 1], 'FTAG': [1, 0]})
    return pd.DataFrame([row]), history


def generate(data=None, history=None, model=ToyModel):
    d, h = inputs()
    return m.generate_league(d if data is None else data, h if history is None else history,
                            model, half_life=240, l2=.08, max_goals=10)


def setup(root, data=None, rows=None):
    data = inputs()[0] if data is None else data
    raw = root/'raw'
    raw.mkdir(parents=True)
    data.to_csv(raw/'all_leagues_predictions.csv', index=False)
    data.iloc[:0].to_csv(raw/'conservative_bet_shortlist.csv', index=False)
    write_json(raw/'conservative_bet_summary.json', {'generated_at_utc': NOW.isoformat()})
    result = m.write_experiment(data, raw, NOW.isoformat(), generate(data) if rows is None else rows)
    return raw, data, result


class ReliabilityTests(unittest.TestCase):
    def test_legacy_truncated_time_recovers_using_verified_summary(self):
        with tempfile.TemporaryDirectory() as tmp, patch(__name__+'.NOW',NOW.replace(microsecond=904906)):
            root=Path(tmp);setup(root)
            capture('e'*40,root=root,captured_at=NOW+timedelta(minutes=1))
            directory=root/'performance/snapshots'/('e'*16)
            metadata=json.loads((directory/'metadata.json').read_text())
            metadata['generated_at_utc']=NOW.replace(microsecond=0).isoformat()
            write_json(directory/'metadata.json',metadata)
            archive=snapshots(root);before=(directory/m.FILE).read_bytes()
            rows,rejected=m.frozen(root,archive)
            self.assertEqual(rejected,[]);self.assertEqual(len(rows),1)
            self.assertEqual(before,(directory/m.FILE).read_bytes())
            (directory/'selection_summary.json').write_text('{}')
            self.assertEqual(m.frozen(root,archive)[1],['e'*40])

    def test_review_gates_multiple_trials_and_uncertainty(self):
        source = generate()[0]
        rows = []
        for i in range(300):
            row = copy.deepcopy(source)
            row['kickoff_utc'] = (NOW+timedelta(days=i % 42+1)).isoformat()
            row['baseline'] = {'p_home': .4, 'p_draw': .3, 'p_away': .3,
                               **{k: .5 for k in m.MARKETS[1:]}}
            for item in row['candidates'].values():
                item['probabilities'] = {'p_home': .9, 'p_draw': .05, 'p_away': .05,
                                         **{k: .9 for k in m.MARKETS[1:]}}
            row['snapshot_commit'] = 'a'*40
            rows.append(row)
        match = {'source_status': 'FINISHED', 'source': 'football-data.org/v4',
                 'home_goals': 2, 'away_goals': 1, 'match_id': 1}
        with tempfile.TemporaryDirectory() as tmp, patch.object(m, 'frozen', return_value=(rows, [])), patch(
                'performance_tracking.fixture_match', return_value=(match, 'VERIFIED')):
            summary, ledger = m.evaluate(Path(tmp), [], [match], NOW+timedelta(days=60))
            self.assertEqual(len(ledger), 600)
            self.assertTrue(all(c['status'] == 'READY_FOR_REVIEW' for c in summary['comparisons']))
            self.assertTrue(all(c['evidence'] == 'SUPPORTS_FORECASTING_REVIEW' for c in summary['comparisons']))
            self.assertFalse(summary['automatic_production_change'])
        with tempfile.TemporaryDirectory() as tmp, patch.object(m, 'frozen', return_value=(rows, ['bad'])), patch(
                'performance_tracking.fixture_match', return_value=(match, 'VERIFIED')):
            summary, _ = m.evaluate(Path(tmp), [], [match], NOW+timedelta(days=60))
            self.assertTrue(all(c['status'] == 'DATA_QUALITY_BLOCKED' for c in summary['comparisons']))
            self.assertTrue(all(c['evidence'] == 'NO_CLEAR_PROMOTION_EVIDENCE' for c in summary['comparisons']))

    def test_cli_flag_preserves_production_and_freezes_fit_failures(self):
        from conservative_bet_filter import build_conservative_shortlist
        data, history = inputs()
        def run(pipe, key):
            pipe._recency_history = history.copy(deep=True)
            return data.copy(deep=True), {'training_end': '2026-10-02', 'training_matches': 2}, {}
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            with patch('conservative_bet_filter.build_conservative_shortlist', side_effect=partial(build_conservative_shortlist, as_of=NOW)), patch(
                    'football_value_pipeline_v2_standalone.FootballValuePipelineV2.run_league', new=run), patch(
                    'football_value_pipeline_v2_standalone.FootballValuePipelineV2._history_for_league', return_value=history), patch(
                    'goal_market_validation.evaluate_market_history', return_value={'markets': {}}), patch(
                    'football_value_pipeline_v2_standalone.DixonColesModel', ToyModel):
                for enabled in (False, True):
                    args = ['--leagues', 'EPL', '--out-dir', str(root/str(enabled))]
                    if enabled: args.append('--reliability-experiment')
                    self.assertEqual(main(args), 0)
            for name in ('all_leagues_predictions.csv', 'EPL_predictions.csv', 'conservative_bet_shortlist.csv', 'conservative_bet_rejections.csv'):
                self.assertEqual((root/'False'/name).read_bytes(), (root/'True'/name).read_bytes())
            self.assertFalse((root/'False'/m.FILE).exists())
            sidecar = json.loads((root/'True'/m.FILE).read_text())
            self.assertEqual(sidecar['registry_sha256'], m.digest(m.REGISTRY))
            self.assertTrue(all(x['status'] == 'available' for x in sidecar['rows'][0]['candidates'].values()))

    def test_separate_one_factor_fits_and_production_unchanged(self):
        data, history = inputs()
        original = data.copy(deep=True)
        history_original = history.copy(deep=True)
        ToyModel.fits = []
        rows = generate(data, history)
        self.assertEqual([s for s, _ in ToyModel.fits], [
            {'half_life_days': 240, 'l2': 3., 'max_goals': 10},
            {'half_life_days': 480., 'l2': .08, 'max_goals': 10}])
        pd.testing.assert_frame_equal(data, original)
        pd.testing.assert_frame_equal(history, history_original)
        for _, trained in ToyModel.fits:
            pd.testing.assert_frame_equal(trained, history_original)
        self.assertTrue(all(c['status'] == 'available' for c in rows[0]['candidates'].values()))
        self.assertEqual(rows[0]['baseline'], m.baseline(data.iloc[0]))
        self.assertFalse(build_parser().parse_args([]).reliability_experiment)
        with self.assertRaises(SystemExit):
            main(['--reliability-experiment', '--backtest'])

    def test_matrix_and_blend_validation(self):
        data, _ = inputs()
        row = data.iloc[0].to_dict()
        matrix, _ = ToyModel().score_matrix('', '')
        row.update(market_blend_applied=True, market_p_home=.6, market_p_draw=.25, market_p_away=.15)
        for key in ('home', 'draw', 'away'):
            row['p_'+key] = .5*row['raw_p_'+key]+.5*row['market_p_'+key]
        probs = m.candidate_probabilities(row, matrix)
        self.assertAlmostEqual(probs['p_home'], row['p_home'])
        for bad in (np.array([[np.nan]]), np.array([[1., -1.], [0, 1]]), np.ones((2, 3)), np.ones((2, 2))):
            with self.assertRaises(ValueError): m.probabilities(bad)
        for change in ({'market_weight': 2}, {'market_p_home': None}, {'p_home': .9}):
            with self.assertRaises((ValueError, TypeError)): m.candidate_probabilities({**row, **change}, matrix)
        row['market_blend_applied'] = False
        with self.assertRaises(ValueError): m.candidate_probabilities(row, matrix)

    def test_failures_unknown_teams_and_scope_are_explicit(self):
        class Broken(ToyModel):
            def fit(self, history): raise RuntimeError('fit failed')
        rows = generate(model=Broken)
        self.assertTrue(all(c['status'] == 'unavailable' for c in rows[0]['candidates'].values()))
        for change in ({'model_home_team': '__LEAGUE_AVERAGE__'}, {'home_name_match_score': 20},
                       {'league': 'Champions League'}, {'p_home': None}):
            data, _ = inputs()
            for key, value in change.items(): data[key] = value
            self.assertTrue(all(c['probabilities'] is None for c in generate(data)[0]['candidates'].values()))
        class Unknown(ToyModel):
            def score_matrix(self, *a): return np.eye(2)/2, {'home_name_match_score': 0}
        self.assertTrue(all(c['status'] == 'unavailable' for c in generate(model=Unknown)[0]['candidates'].values()))

    def test_capture_binding_tampering_and_no_backfill(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            raw, data, result = setup(root)
            self.assertEqual(m.capture_file(raw, NOW.isoformat()), raw/m.FILE)
            for mutate in (lambda d: d.update(registry_sha256='changed'),
                           lambda d: d['rows'][0]['baseline'].update(p_home=.9),
                           lambda d: d['rows'][0]['candidates']['stronger_l2']['settings'].update(l2=4),
                           lambda d: d['rows'][0]['candidates']['stronger_l2']['probabilities'].update(p_home=.9),
                           lambda d: d['rows'].append(copy.deepcopy(d['rows'][0])),
                           lambda d: d['rows'][0].update(training_end='2027-01-01')):
                bad = copy.deepcopy(result); mutate(bad)
                with self.assertRaises(ValueError): m.validate(bad, NOW.isoformat(), data.to_dict('records'))
            write_json(raw/m.FILE, {**result, 'predictions_sha256': 'changed'})
            with self.assertRaises(ValueError): m.capture_file(raw, NOW.isoformat())
            write_json(raw/m.FILE, result)
            # First snapshot is unavailable; a later successful rerun cannot replace it.
            first = copy.deepcopy(result)
            for item in first['rows'][0]['candidates'].values():
                item.update(status='unavailable', reason='FIT_FAILED', raw_matrix=None, probabilities=None)
            write_json(raw/m.FILE, first)
            capture('a'*40, root=root, captured_at=NOW)
            write_json(raw/m.FILE, result)
            capture('b'*40, root=root, captured_at=NOW+timedelta(minutes=1))
            frozen, rejected = m.frozen(root, snapshots(root))
            self.assertEqual(rejected, [])
            self.assertEqual(frozen[0]['snapshot_commit'], 'a'*40)
            self.assertEqual(frozen[0]['candidates']['stronger_l2']['status'], 'unavailable')
            path = root/'performance/snapshots'/('a'*16)/m.FILE
            path.write_text('{}')
            frozen, rejected = m.frozen(root, snapshots(root))
            self.assertEqual(rejected, ['a'*40])

    def test_lead_time_missing_generation_and_report_reconciliation(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            raw, data, _ = setup(root)
            generated=NOW.replace(microsecond=904906).isoformat()
            write_json(raw/'conservative_bet_summary.json', {'generated_at_utc': generated})
            sidecar=json.loads((raw/m.FILE).read_text())
            sidecar['generated_at_utc']=generated
            write_json(raw/m.FILE,sidecar)
            capture('c'*40, root=root, captured_at=NOW)
            record = verified_record('PL', final())
            record['home_team'] = data.iloc[0]['home_team']
            record['away_team'] = data.iloc[0]['away_team']
            record['kickoff_utc'] = data.iloc[0]['kickoff_utc']
            clock = NOW+timedelta(days=2)
            summary = m.review_experiment(root, snapshots(root), [record], clock)
            self.assertEqual([c['paired_fixtures'] for c in summary['comparisons']], [1, 1])
            self.assertTrue(all(c['status'] == 'COLLECT_MORE_DATA' for c in summary['comparisons']))
            self.assertEqual(summary['registry']['confidence_level'], .975)
            write_json(root/'performance/verified_results.json', {'result': record})
            self.assertTrue(m.validate_report(root))
            summary['observed_fixtures'] = 99
            write_json(root/'performance/model_reliability_experiment/summary.json', summary)
            with self.assertRaises(ValueError): m.validate_report(root)
            from experiment_review_queue import build_queue
            queue = build_queue(root, clock)
            self.assertEqual(len([r for r in queue['experiments'] if r['name'] == 'model_reliability_experiment']), 2)
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            raw, data, result = setup(root, rows=[])
            self.assertEqual(result['rows'][0]['generation_error'], 'LEAGUE_GENERATION_FAILED')
            capture('d'*40, root=root, captured_at=NOW)
            rows, rejected = m.frozen(root, snapshots(root))
            self.assertEqual(len(rows), 1)
            self.assertEqual(rows[0]['candidates'], {})
            empty, _ = m.evaluate(root, [], [], NOW)
            self.assertEqual(empty['observed_fixtures'], 0)


if __name__ == '__main__':
    unittest.main()

