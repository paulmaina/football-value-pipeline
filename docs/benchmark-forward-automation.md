# Benchmark candidate forward automation

The benchmark-to-forward bridge now nominates one frozen candidate from the benchmark's **development** selection: market weight 0.85 for 1X2. It uses the actual production raw model and the same live reference, changing only the weight from the registered production baseline of 0.5. Production forecasts, shortlist filters and stakes are unchanged.

The registry binds the candidate, primary 1X2 log-loss metric, domestic league scope, parameters, source report hash, start date and review gates before its first eligible forecast. UCL is reported unavailable because it was not included in the historical nomination. L2 and totals anchoring remain offline alternatives; they are not automatically combined with this candidate. Later candidate versions must be separately frozen and cannot be pooled with this trial.

## Forecast generation and capture

Every normal current-fixture command automatically writes `raw/benchmark_forward_experiment.json`; no new flag or odds request is needed. A private copy of the production score matrix supplies goal-market secondary checks. The pipeline's public forecast CSVs and selected bets are unchanged. The candidate has the same raw strengths, recency, L2 and market reference as production.

The trial requires known model teams, reliable matching, coherent complete live reference prices/probabilities, a reference timestamp no more than 24 hours old, and generation/capture at least 20 minutes before kickoff within the 72-hour window. A changed production market weight, unavailable quotes or unknown teams are explicit coverage failures. The baseline and candidate probabilities and the baseline matrix are checked against the original forecast. Hash-protected snapshots freeze first observations, including unavailable observations, and do not backfill earlier forecasts.

## Automated generation and publishing

Scheduled forecast collection runs daily at **08:45 EAT**, on manual dispatch, and after changes to its workflow/publisher/registry. It runs the existing six-league command with the three existing experiment flags, formats readable forecasts, commits raw forecasts, immediately captures that exact forecast commit, verifies results, grades all experiments and validates the reports. It explicitly performs capture/review because a push made with GITHUB_TOKEN does not trigger the other workflows.

Publishing uses a fresh main worktree. A concurrent push causes regeneration on the new head, not a force push, rebase or overwrite of another update. Regeneration retries can consume additional Odds API quota. There is no automated bet placement.

**One-time credential setup is required:** GitHub Actions cannot read the `.env` on your computer. Configure repository Actions Secrets with at least one of `THE_ODDS_API_KEY`, `THE_ODDS_API_KEY_FALLBACK_1`, `THE_ODDS_API_KEY_FALLBACK_2`, and with `FOOTBALL_DATA_API_KEY`. Existing configured secrets can be reused. Do not commit `.env` or send keys in an issue. When credentials are absent, the workflow reports SETUP REQUIRED and generates nothing. If keys are exhausted or providers unavailable, collection can fail or record unavailable coverage; no successful-collection guarantee is implied.

The scheduled job explicitly uses `--api-key-source environment`. Your local command still defaults to `.env` and ignores inherited PowerShell API keys. Daily automatic collection uses the same API requests as a normal manual run. Avoid redundant manual runs if managing a small quota; the new weight trial itself adds no API calls or model fitting.

## Readiness and review notifications

The daily forward-review workflow grades paired forecasts using the shared official FINISHED regulation-time results. Reports are in `performance/benchmark_forward_experiment/`; matrices and probability arrays are retained in JSON ledgers. Versions have separate directories and are never pooled for readiness.

The registry requires **300 distinct paired fixtures across six ISO gameweeks**, at least 80% usable coverage among verified in-scope fixtures, and no rejected snapshot evidence before declaring READY FOR REVIEW. Data-quality failures block readiness. Ready can mean a negative or inconclusive result; it does not mean the candidate should be promoted.

Supportive forecasting evidence requires a positive primary gain with a week-block bootstrap 95% interval above zero, no aggregate 1X2 Brier deterioration, and no top-label calibration deterioration. The production goal-market secondary checks (Over 1.5 and BTTS Yes) also need at least 80% coverage and no paired log-loss/Brier deterioration. These checks are conservative review aids, not proof of betting profitability. League results and secondary goal calibration remain available for human assessment.

`performance/experiment_review_queue.json` and `.md` collect readiness for all experiments and appear in the health report/Excel health sheet. The original four sidecars have a separate initial-review cue at 28 collection days and 30 settled observations. These are first-look thresholds only, not the benchmark candidate's production approval gates. Market-led paper probability evidence is distinguished from settled paper bets.

When a gate is reached, GitHub creates one repository issue inviting review. The notification queries the published main report, rejects stale queues, and checks all open/closed issues for a stable marker so an already-reviewed experiment is not repeatedly announced. Verify the current queue when reviewing: official corrections can change readiness. Issues are review requests and never approve production changes.

You then ask for a review of the sidecar results and approve or reject a concrete versioned production proposal. No workflow changes production parameters automatically. Actual accepted prices, closing-line collection and execution records are still required before making a demonstrated betting-edge claim.
