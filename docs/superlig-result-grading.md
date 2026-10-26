# Süper Lig forward result grading

`performance_tracking.py review` retrieves Football-Data.co.uk's public T1 season CSV only when an archived Turkish forecast is at least two hours past kickoff and within the existing 60-day result lookback. It makes one keyless request per relevant season, including across July season boundaries. Other leagues keep their existing results providers. No Odds API credits are needed for Turkish results.

The same CSV validation used by training checks division, season, completed integer scores, result consistency and duplicate fixtures. The adapter matches the exact UTC date of the archived kickoff, ordered home/away teams and the reviewed `SuperLig` aliases. It does not use fuzzy matching, a 36-hour date tolerance, or the CSV's unzoned `Time` column. A date change or unresolved identity remains unverified rather than borrowing another result. Only forecasts actually captured before kickoff are eligible, including older Turkish snapshots previously excluded from grading.

Downloaded CSV bytes are retained under `performance/result_sources/T1/<season-start>/<sha256>.csv`. Result records carry the source URL, digest, match date and stable fixture identity. The review and report validator replay each Turkish result against those exact bytes. Git preserves evidence bytes on Windows and Linux. Previously verified evidence-backed results remain usable during provider outages; errors appear in the report. Corrections update the existing result identity and retain first-verification/revision timestamps.

Once a result matches, the existing settlement logic updates selections, run history, fixture accuracy, win rate, simulated ROI and the Excel workbook. Experiment consumers accept the same verified Turkish result contract. Prediction probabilities, shortlist gates and thresholds are unchanged. Corner/card grading is outside this result adapter; final goals alone do not establish count-market outcomes.

Source publication is not immediate. A missing result stays pending until a later download includes it. The existing 60-day lookback applies; no historical predictions are fabricated or backdated. A UTC/source date disagreement requires review rather than an automatic date adjustment.

Offline regression tests exercise archived forecast → keyless result download → alias/date matching → grading → Excel → report validation, plus provider failures, score corrections, ambiguous fixtures and corrupted evidence. A successful synthetic test is not a live post-deployment grading claim.
