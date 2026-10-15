import copy
from datetime import timedelta
import hashlib
import json
from pathlib import Path
import tempfile
import unittest
import pandas as pd
from unittest.mock import patch
from conservative_bet_filter import build_conservative_shortlist
from filter_sensitivity_experiment import (write_experiment,capture_file,validate,
    frozen,review_experiment,validate_report,statistics,FLOORS)
from performance_tracking import capture,snapshots,write_json,verified_record
from test_conservative_bet_filter import fixture,NOW
from test_performance_tracking import final


def setup(root,row=None):
    raw=root/'raw';raw.mkdir(exist_ok=True,parents=True)
    row=row or fixture()
    row.update(home_team='Manchester City FC',away_team='Everton FC',
               model_home_team='Manchester City FC',model_away_team='Everton FC')
    predictions=pd.DataFrame([row])
    picks,decisions,summary=build_conservative_shortlist(predictions,as_of=NOW)
    predictions.to_csv(raw/'all_leagues_predictions.csv',index=False)
    picks.to_csv(raw/'conservative_bet_shortlist.csv',index=False)
    write_json(raw/'conservative_bet_summary.json',summary)
    data=write_experiment(predictions,raw,summary,decisions,None)
    return raw,data,predictions,picks,decisions,summary


def record(row,h=2,a=1):
    match=final(h=h,a=a);match['utcDate']=row['kickoff_utc']
    return verified_record('PL',match)


class SensitivityTests(unittest.TestCase):
    def test_previous_six_market_policy_remains_valid_for_archived_evidence(self):
        import conservative_bet_filter as shortlist
        old_specs = tuple(s for s in shortlist.MARKET_SPECS if s[1] != "home_away") + (("Both Teams to Score - Yes", "btts_yes", .70, .63),)
        with tempfile.TemporaryDirectory() as tmp:
            with patch.object(shortlist, "MARKET_SPECS", old_specs):
                _, data, predictions, _, _, summary = setup(Path(tmp))
            data["selection_policy_version"] = "72h-all-markets-net-ev15-execution-v7"
            self.assertEqual(len(data["rows"]), 18)
            validate(data, summary["generated_at_utc"], predictions.to_dict("records"))
            data["selection_policy_version"] = summary["selection_policy_version"]
            with self.assertRaises(ValueError):
                validate(data, summary["generated_at_utc"], predictions.to_dict("records"))

    def test_previous_five_market_policy_remains_valid(self):
        import conservative_bet_filter as shortlist
        old_specs=tuple(s for s in shortlist.MARKET_SPECS if s[1] != 'home_away')
        with tempfile.TemporaryDirectory() as tmp:
            with patch.object(shortlist, 'MARKET_SPECS', old_specs):
                _, data, predictions, _, _, summary=setup(Path(tmp))
            data['selection_policy_version']='72h-five-markets-probability-odds-net-ev15-v8'
            self.assertEqual(len(data['rows']), 15)
            validate(data, summary['generated_at_utc'], predictions.to_dict('records'))

    def test_production_unchanged_and_all_markets_rejections_retained(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);raw,data,predictions,picks,decisions,summary=setup(root)
            before=(raw/'conservative_bet_shortlist.csv').read_bytes()
            self.assertEqual(len(data['rows']),18)
            control=[r for r in data['rows'] if r['ev_floor']==.015]
            self.assertEqual([r['decision'] for r in control],decisions.decision.tolist())
            self.assertEqual([r['market'] for r in control],decisions.market.tolist())
            self.assertEqual(before,(raw/'conservative_bet_shortlist.csv').read_bytes())
            self.assertTrue(any(r['decision']=='REJECTED' for r in control))
            validate(data,summary['generated_at_utc'],predictions.to_dict('records'))
            self.assertIsNotNone(capture_file(raw,summary['generated_at_utc']))
            for bad in (float('nan'),.01,float('inf')):
                with self.assertRaises(ValueError):build_conservative_shortlist(predictions,as_of=NOW,adjusted_ev_floor=bad)

    def test_reranks_alternative_market_after_raising_floor(self):
        with tempfile.TemporaryDirectory() as tmp:
            row=fixture();row['raw_p_over_1_5']=.86;row['market_over_1_5_odds']=1.195 # ~2.77% adjusted EV
            raw,data,*_=setup(Path(tmp),row)
            chosen={floor:[r['market'] for r in data['rows'] if r['ev_floor']==floor and r['decision']=='SHORTLISTED'] for floor in FLOORS}
            self.assertEqual(chosen[.015],['Over 1.5'])
            self.assertEqual(chosen[.03],['Home win'])
            self.assertEqual(chosen[.05],['Home win'])
            self.assertTrue(any('+3.0%' in r['rejection_reasons'] for r in data['rows'] if r['ev_floor']==.03))

    def test_invalid_or_stale_sidecars_and_line_endings(self):
        with tempfile.TemporaryDirectory() as tmp:
            raw,data,predictions,_,_,summary=setup(Path(tmp))
            original=data
            for mutate in (lambda d:d.update(version='bad'),lambda d:d.update(floors=[.015]),
                lambda d:d['rows'].pop(),lambda d:d['rows'].append(copy.deepcopy(d['rows'][0])),
                lambda d:d['rows'][0].update(decision='bogus')):
                data=copy.deepcopy(original);mutate(data)
                with self.assertRaises(ValueError):validate(data,summary['generated_at_utc'],predictions.to_dict('records'))
            data=copy.deepcopy(original)
            selected=next(r for r in data['rows'] if r['decision']=='SHORTLISTED')
            selected['conservative_estimated_ev']=1
            with self.assertRaises(ValueError):validate(data,summary['generated_at_utc'],predictions.to_dict('records'))
            with self.assertRaises(ValueError):capture_file(raw,(NOW+timedelta(minutes=2)).isoformat())
            path=raw/'all_leagues_predictions.csv';path.write_bytes(path.read_bytes().replace(b'\r\n',b'\n').replace(b'\n',b'\r\n'))
            self.assertIsNotNone(capture_file(raw,summary['generated_at_utc']))
            path.write_bytes(path.read_bytes()+b'\n')
            with self.assertRaises(ValueError):capture_file(raw,summary['generated_at_utc'])
            (raw/'filter_sensitivity_experiment.json').unlink()
            self.assertIsNone(capture_file(raw,summary['generated_at_utc']))

    def test_forward_freeze_verified_grading_pending_and_tamper_reconciliation(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);raw,data,predictions,*_=setup(root)
            sha='a'*40;capture(sha,root=root,captured_at=NOW)
            # Duplicate runs cannot add markets or replace first rejections.
            capture('b'*40,root=root,captured_at=NOW+timedelta(minutes=1))
            rows,rejected=frozen(root,snapshots(root));self.assertEqual(len(rows),18);self.assertFalse(rejected)
            row=predictions.iloc[0].to_dict();rec=record(row);clock=NOW+timedelta(days=3)
            write_json(root/'performance/verified_results.json',{'PL:90002':rec})
            summary=review_experiment(root,snapshots(root),[rec],clock)
            self.assertEqual(summary['total_fixtures'],1)
            self.assertEqual(summary['comparisons'][0]['graded'],1)
            self.assertAlmostEqual(summary['comparisons'][0]['flat_stake_roi'],.27)
            self.assertTrue(validate_report(root))
            pending=review_experiment(root,snapshots(root),[rec],NOW)
            self.assertEqual(pending['comparisons'][0]['pending'],1)
            self.assertIsNone(pending['comparisons'][0]['flat_stake_roi'])
            self.assertTrue(validate_report(root))
            dest=root/'performance/filter_sensitivity_experiment/summary.json'
            pending['comparisons'][0]['selected']=999;write_json(dest,pending)
            with self.assertRaises(ValueError):validate_report(root)
            review_experiment(root,snapshots(root),[rec],clock)
            ledger=root/'performance/filter_sensitivity_experiment/selections.csv'
            ledger.write_text(ledger.read_text().replace('SHORTLISTED','REJECTED'))
            with self.assertRaises(ValueError):validate_report(root)
            archive=root/'performance/snapshots'/sha[:16]/'filter_sensitivity_experiment.json'
            archive.write_text('{}')
            self.assertEqual(len(snapshots(root)),2) # optional failure preserves baseline
            rows,rejected=frozen(root,snapshots(root));self.assertIn(sha,rejected)
            self.assertEqual(len(rows),18)

    def test_only_ev_changes_and_selected_quote_is_bound_to_forecast(self):
        with tempfile.TemporaryDirectory() as tmp:
            raw,data,predictions,_,_,summary=setup(Path(tmp))
            for field,value in [('rank_probability',.5),('predicted_probability',.1),('offered_decimal_odds',9),('bookmaker','Invented')]:
                altered=copy.deepcopy(data)
                # Alter all policy copies to exercise forecast bindings too.
                market=next(r['market'] for r in altered['rows'] if r['decision']=='SHORTLISTED')
                for row in altered['rows']:
                    if row['market']==market:row[field]=value
                with self.assertRaises(ValueError):validate(altered,summary['generated_at_utc'],predictions.to_dict('records'))
            altered=copy.deepcopy(data)
            altered['rows'][6]['audit_brier']=.999
            with self.assertRaises(ValueError):validate(altered,summary['generated_at_utc'],predictions.to_dict('records'))
            altered=copy.deepcopy(data)
            altered['rows'][0]['selection_tier']='PROVISIONAL'
            # Use a selected row for tier validation.
            selected=next(r for r in altered['rows'] if r['decision']=='SHORTLISTED');selected['selection_tier']='PROVISIONAL'
            with self.assertRaises(ValueError):validate(altered,summary['generated_at_utc'],predictions.to_dict('records'))
            altered=copy.deepcopy(data);altered['rows'][0]=None
            with self.assertRaises(ValueError):validate(altered,summary['generated_at_utc'],predictions.to_dict('records'))
            with self.assertRaises(ValueError):validate(None,summary['generated_at_utc'],predictions.to_dict('records'))

    def test_outside_72h_forecasts_do_not_lock_later_eligible_decisions(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);row=fixture(kickoff=NOW+timedelta(days=4))
            setup(root,row);capture('a'*40,root=root,captured_at=NOW)
            self.assertEqual(frozen(root,snapshots(root))[0],[])
            later=NOW+timedelta(days=2)
            for key in row:
                if key.startswith('market_best_') and key.endswith('_last_update_utc'):
                    row[key]=(later-timedelta(hours=1)).isoformat()
            with patch('test_filter_sensitivity_experiment.NOW',later):setup(root,row)
            capture('b'*40,root=root,captured_at=later)
            rows,_=frozen(root,snapshots(root))
            self.assertEqual(len(rows),18)
            self.assertTrue(all(r['snapshot_commit']=='b'*40 for r in rows))

    def test_late_and_legacy_not_backfilled(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);raw,data,predictions,*_=setup(root)
            (raw/'filter_sensitivity_experiment.json').unlink()
            capture('a'*40,root=root,captured_at=NOW)
            self.assertEqual(frozen(root,snapshots(root))[0],[])
            write_json(raw/'filter_sensitivity_experiment.json',data)
            # No baseline eligible forecasts => no capture near kickoff.
            kick=NOW+timedelta(days=1)
            self.assertFalse(capture('b'*40,root=root,captured_at=kick-timedelta(minutes=19)))
            summary=review_experiment(root,snapshots(root),[],NOW)
            self.assertEqual(summary['candidate_decisions'],0)
            write_json(root/'performance/verified_results.json',{})
            self.assertTrue(validate_report(root))

    def test_statistics_costs_drawdown_calibration_and_pending(self):
        rows=[{'kickoff_utc':'2026-10-10','fixture_key':'a','outcome':1,'rank_probability':.8,'brier':.04,'unit_profit':.2},
            {'kickoff_utc':'2026-10-11','fixture_key':'b','outcome':0,'rank_probability':.8,'brier':.64,'unit_profit':-1.01},
            {'kickoff_utc':'2026-10-12','fixture_key':'c','outcome':None}]
        s=statistics(rows);self.assertEqual(s['graded'],2);self.assertEqual(s['pending'],1)
        self.assertAlmostEqual(s['max_drawdown_units'],1.01)
        self.assertAlmostEqual(s['flat_stake_roi'],-.405)
        self.assertEqual(s['calibration'][0]['observed_rate'],.5)
        self.assertEqual(statistics([])['graded'],0)


