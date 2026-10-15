from offline_test_case import OfflineQuotePolicyTestCase
import copy
import json
from datetime import timedelta
from unittest.mock import patch
import pandas as pd
import unittest
import tempfile
from pathlib import Path
from goal_blend_experiment import generate, write_experiment, capture_file, review_experiment
from performance_tracking import capture, snapshots, frozen_rows, verified_record
from test_performance_tracking import fixture, pick, final, T0, KICK, SHA


def frame():
    row=fixture()
    for key in ('over_1_5','under_3_5','btts_yes'):
        row.update({f'raw_p_{key}':.9, f'p_{key}':.88,
            f'market_p_{key}':.75,f'market_reference_{key}_odds':1.28,
            f'market_reference_{key}_opposite_odds':3.84,
            f'market_{key}_odds':1.3,f'best_{key}_bookmaker':'test',
            f'market_{key}_bookmakers':3,
            f'market_best_{key}_last_update_utc':T0.isoformat()})
    return pd.DataFrame([row])


def setup(tmp_path):
    raw=tmp_path/'raw';raw.mkdir()
    data=frame(); data.to_csv(raw/'all_leagues_predictions.csv',index=False)
    pd.DataFrame([pick()]).to_csv(raw/'conservative_bet_shortlist.csv',index=False)
    (raw/'conservative_bet_summary.json').write_text(json.dumps({'generated_at_utc':T0.isoformat()}))
    return raw,data


def test_blends_complements_and_no_mutation():
    data=frame();before=data.copy(deep=True)
    rows=generate(data,T0.isoformat())
    pd.testing.assert_frame_equal(data,before)
    for r in rows:
        assert r['variants']['book50']==.825
        assert r['variants']['book25']==.8625
        assert r['variants']['baseline']==.88
        assert all(p+r['opposite_variants'][k]==1 for k,p in r['variants'].items())


def test_missing_stale_and_late_are_unavailable():
    for field,value in [
        ('market_reference_under_3_5_opposite_odds',None),
        ('market_p_under_3_5',float('nan')),
        ('market_best_under_3_5_last_update_utc',(T0-timedelta(days=2)).isoformat()),
        ('market_best_under_3_5_last_update_utc',(T0+timedelta(hours=1)).isoformat()),
        ('kickoff_utc',(T0+timedelta(minutes=10)).isoformat())]:
        data=frame();data[field]=value
        row=generate(data,T0.isoformat())[1]
        assert row['status']=='unavailable' and not row['variants']


def test_inconsistent_lines_fail_closed():
    data=frame();data['market_p_under_3_5']=.1;data['market_p_over_1_5']=.1
    rows=generate(data,T0.isoformat())
    assert all('inconsistent_goal_lines' in r['reasons'] for r in rows[:2])


def test_capture_binding_and_baseline_bytes(tmp_path):
    raw,data=setup(tmp_path)
    before={p.name:p.read_bytes() for p in raw.iterdir()}
    write_experiment(data,raw,T0.isoformat())
    assert all((raw/n).read_bytes()==b for n,b in before.items())
    assert capture_file(raw,T0.isoformat())
    assert capture_file(raw,(T0+timedelta(seconds=1)).isoformat()) is None
    assert capture(SHA,root=tmp_path,captured_at=T0+timedelta(minutes=1))
    archive=snapshots(tmp_path)
    assert len(frozen_rows(archive,'predictions'))==1
    (raw/'all_leagues_predictions.csv').write_text('changed')
    assert capture_file(raw,T0.isoformat()) is None


def test_paired_grading_and_tamper_isolation(tmp_path):
    raw,data=setup(tmp_path);write_experiment(data,raw,T0.isoformat())
    capture(SHA,root=tmp_path,captured_at=T0+timedelta(minutes=1))
    archived=snapshots(tmp_path)
    records=[verified_record('PL',final())]
    review_experiment(tmp_path,archived,records,KICK+timedelta(days=1))
    report=json.loads((tmp_path/'performance/goal_blend_experiment/summary.json').read_text())
    assert report['graded_fixture_markets']==3
    assert len(report['comparisons'])==15
    for r in report['comparisons']:
        assert r['n']==1 and r['event_rate']==1
    sidecar=tmp_path/'performance/snapshots'/SHA[:16]/'goal_blend_experiment.json'
    sidecar.write_text('{}')
    assert len(frozen_rows(snapshots(tmp_path),'predictions'))==1
    dest=tmp_path/'performance/goal_blend_experiment/summary.json';dest.unlink()
    review_experiment(tmp_path,snapshots(tmp_path),records,KICK+timedelta(days=1))
    assert not dest.exists()


def test_no_sidecar_preserves_capture(tmp_path):
    setup(tmp_path)
    capture(SHA,root=tmp_path,captured_at=T0)
    meta=snapshots(tmp_path)[0][0]
    assert 'goal_blend_experiment.json' not in meta['sha256']


def test_cli_flag_preserves_baseline_files(tmp_path):
    from football_value_pipeline_v2_standalone import main
    from conservative_bet_filter import build_conservative_shortlist
    from functools import partial
    data=frame()
    for enabled in (False,True):
        out=tmp_path/str(enabled)
        with patch('conservative_bet_filter.build_conservative_shortlist',
                   side_effect=partial(build_conservative_shortlist, as_of=T0)), patch(
                   'football_value_pipeline_v2_standalone.FootballValuePipelineV2.run_league',
                   return_value=(data, {'training_end':'2026-09-20','training_matches':1000}, {})), patch(
                   'football_value_pipeline_v2_standalone.FootballValuePipelineV2.backtest_league',
                   return_value=(pd.DataFrame(),pd.DataFrame(),{},pd.DataFrame())):
            args=['--leagues','EPL','--out-dir',str(out)]
            if enabled: args.append('--goal-blend-experiment')
            assert main(args)==0
    for name in ('all_leagues_predictions.csv','EPL_predictions.csv','conservative_bet_shortlist.csv',
                 'conservative_strict_qualifiers.csv','conservative_bet_rejections.csv'):
        assert (tmp_path/'False'/name).read_bytes()==(tmp_path/'True'/name).read_bytes()
    assert not (tmp_path/'False'/'goal_blend_experiment.json').exists()
    assert (tmp_path/'True'/'goal_blend_experiment.json').exists()


class ShadowTests(OfflineQuotePolicyTestCase):
    pass


def _wrap(fn):
    def run(self):
        with tempfile.TemporaryDirectory() as directory:
            if fn.__code__.co_argcount:
                fn(Path(directory))
            else:
                fn()
    return run


for name, fn in list(globals().items()):
    if name.startswith('test_') and callable(fn):
        setattr(ShadowTests, name, _wrap(fn))
