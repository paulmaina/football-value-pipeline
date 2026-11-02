> **ARCHIVED 2026-11-02.** No longer generated, captured or reviewed. This is the last report, frozen as committed; the code is kept for replay in `archive/goal_blend_experiment.py`.

# Goal-market shadow comparison

Fixed, uncalibrated variants on identical verified fixtures. No model promotion or bet selections.

Coverage: 126/897 fixture-markets available.

| Market | Variant | N | Brier | Mean probability | Event rate |
|---|---|---:|---:|---:|---:|
| btts_yes | baseline | 34 | 0.2857 | 51.5% | 50.0% |
| btts_yes | book25 | 34 | 0.2749 | 53.3% | 50.0% |
| btts_yes | book50 | 34 | 0.2679 | 55.2% | 50.0% |
| btts_yes | bookmaker | 34 | 0.2655 | 58.9% | 50.0% |
| btts_yes | raw | 34 | 0.2859 | 51.5% | 50.0% |
| over_1_5 | baseline | 39 | 0.1504 | 76.0% | 87.2% |
| over_1_5 | book25 | 39 | 0.1370 | 78.3% | 87.2% |
| over_1_5 | book50 | 39 | 0.1279 | 80.2% | 87.2% |
| over_1_5 | bookmaker | 39 | 0.1179 | 84.1% | 87.2% |
| over_1_5 | raw | 39 | 0.1488 | 76.3% | 87.2% |
| under_3_5 | baseline | 39 | 0.2936 | 63.5% | 51.3% |
| under_3_5 | book25 | 39 | 0.2770 | 61.9% | 51.3% |
| under_3_5 | book50 | 39 | 0.2652 | 60.7% | 51.3% |
| under_3_5 | bookmaker | 39 | 0.2549 | 58.3% | 51.3% |
| under_3_5 | raw | 39 | 0.2932 | 63.1% | 51.3% |
