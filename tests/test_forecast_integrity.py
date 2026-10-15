import hashlib
import json
from pathlib import Path
import tempfile
import unittest
from forecast_integrity import forecast_digest_variants, snapshot_generated_at
from goal_blend_experiment import capture_file as goal_capture, VERSION as GOAL_VERSION
from market_led_experiment import capture_file as market_capture, VERSION as MARKET_VERSION


class ForecastLineEndingTests(unittest.TestCase):
    def test_both_sidecars_survive_git_line_ending_conversion_but_not_changed_data(self):
        with tempfile.TemporaryDirectory() as tmp:
            raw=Path(tmp);csv=raw/'all_leagues_predictions.csv'
            original=b'league,p_home,p_draw,p_away\r\nEPL,0.7,0.2,0.1\r\n'
            stamp='2026-10-13T07:00:00Z';digest=hashlib.sha256(original).hexdigest()
            (raw/'goal_blend_experiment.json').write_text(json.dumps({'version':GOAL_VERSION,
                'generated_at_utc':stamp,'predictions_sha256':digest}))
            (raw/'market_led_experiment.json').write_text(json.dumps({'version':MARKET_VERSION,
                'baseline_generated_at_utc':stamp,'predictions_sha256':digest}))
            csv.write_bytes(original.replace(b'\r\n',b'\n'))
            self.assertTrue(goal_capture(raw,stamp));self.assertTrue(market_capture(raw,stamp))
            self.assertIn(digest,forecast_digest_variants(csv))
            self.assertIsNone(goal_capture(raw,'2026-10-13T08:00:00Z'))
            csv.write_bytes(csv.read_bytes().replace(b'0.7',b'0.8'))
            self.assertIsNone(goal_capture(raw,stamp));self.assertIsNone(market_capture(raw,stamp))

    def test_attributes_preserve_snapshot_bytes(self):
        root=Path(__file__).resolve().parents[1]
        text=(root/'.gitattributes').read_text()
        self.assertIn('football_output_v2/performance/snapshots/** -text',text)
        self.assertIn('football_output_v2/raw/*.csv text eol=lf',text)



class ArchivedTimestampTests(unittest.TestCase):
    def test_recovery_requires_hash_bound_same_second_summary(self):
        with tempfile.TemporaryDirectory() as tmp:
            directory=Path(tmp);path=directory/'selection_summary.json'
            summary={'generated_at_utc':'2026-10-14T19:07:50.904906+00:00'}
            content=json.dumps(summary).encode();path.write_bytes(content)
            meta={'generated_at_utc':'2026-10-14T19:07:50Z',
                  'sha256':{'selection_summary.json':hashlib.sha256(content).hexdigest()}}
            self.assertEqual(snapshot_generated_at(directory,meta),summary['generated_at_utc'])
            exact={**meta,'generated_at_utc':summary['generated_at_utc']}
            self.assertEqual(snapshot_generated_at(directory,exact),summary['generated_at_utc'])
            self.assertEqual(snapshot_generated_at(directory,{'generated_at_utc':meta['generated_at_utc']}),meta['generated_at_utc'])
            for stamp in ('bad','2026-10-14T19:07:49Z','2026-10-14T19:07:51Z','2026-10-14T19:07:50.5Z'):
                with self.assertRaises(ValueError):snapshot_generated_at(directory,{**meta,'generated_at_utc':stamp})
            path.write_bytes(content+b' ')
            with self.assertRaises(ValueError):snapshot_generated_at(directory,meta)
            path.write_text('{}');meta['sha256']['selection_summary.json']=hashlib.sha256(path.read_bytes()).hexdigest()
            with self.assertRaises(ValueError):snapshot_generated_at(directory,meta)
