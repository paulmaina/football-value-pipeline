# Pipeline audit — 11 October 2026

## Findings and repairs

- UCL access is working: 521 completed matches across four seasons. The old 500-match warm-up left only 19 validation predictions (13 development / 6 audit). An explicit UCL-only 250-match warm-up yields 180 chronological predictions (133 development / 47 audit), without weakening calibration or audit thresholds. All five markets now pass the existing overall reliability gates; candidate-level high-confidence and price gates still apply.
- Nine UCL historical records use extra-time or penalty durations. The loader previously trained on their fullTime totals. Training and settlement now share regulation-time parsing, excluding unknown/missing regulation scores and future records.
- Limited additional odds requests could be spent outside the 72-hour shortlist window. Queue eligibility now uses the same minimum lead and maximum horizon as selection.
- GitHub Actions run 38126851170 archived and graded successfully but could not publish: a tracked football_performance_report.tmp was removed during workbook replacement, leaving an unstaged deletion that blocked rebase. Remove the tracked temporary file, ignore future temporary files, use unique temporary paths and always clean them on failure.

## End-to-end replay

Replayed the normal six-league command with half-life tuning against provider responses from commit 1cd7e6bed154f42a64d727330bff7e94e7913210. Network reads were disabled; no new API prices were fetched and no API credits were consumed. All six model fits succeeded, 87 fixtures were predicted, and 19 additional event-market responses were used within the 24-request ceiling.

The replay selected nine distinct matches inside the next 72 hours: five STRICT and four PROVISIONAL. Two STRICT selections are UCL. The formatter produced all six readable league reports, the shortlist report and the consolidated Excel workbook. Outputs explicitly record replay provenance.

## Cleanup scope

Remove regenerable live odds/fixture caches, isolated single-league diagnostic output directories, the tracked temporary workbook and byte-identical duplicate decision output. Retain historical training data, canonical six-league outputs, older decision history and every immutable forward snapshot. Git history retains removed files.

## Limits

104 offline regression tests pass, covering score semantics, UCL warm-up configuration, hard timing/odds budgeting and locked-workbook recovery. This demonstrates repaired processing, not a proven increase in future win rate or profitability. The existing forward report still has no graded results. UCL retrospective calibration uses model probabilities where historical bookmaker prices are absent, and its period can overlap decay tuning; it is not an untouched forward holdout. Keep collecting pre-kickoff snapshots and verified results before changing model weights or selection thresholds.
