import hashlib
import json
from pathlib import Path
import tempfile
import unittest
from forecast_integrity import forecast_digest_variants
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
