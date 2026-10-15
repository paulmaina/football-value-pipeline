# Project-wide reliability audit — 15 October 2026

## Scope

Reviewed the current main project after PR #49: repository-wide source/config
scan, Python syntax/CLI checks, all six GitHub workflows, offline regression
and coverage checks, and targeted manual review of training, model fitting,
live odds, shortlist generation, immutable capture, experiment replay,
settlement, reporting and publication. This is not formal verification or a
guarantee that no undiscovered bugs remain. No new experiment, market input,
selection threshold or automatic promotion is introduced.

## Confirmed defects and corrections

| Defect | Reproduction / effect | Correction |
|---|---|---|
| Scheduled generation omitted reliability trial | The publisher's command enabled recency, goal blend and market-led research but omitted `--reliability-experiment`; scheduled runs could leave the old reliability sidecar stale. | Preserve all four existing experiment flags in automatic generation; regression checks the command across retries. Adds the existing trial's fitting time, no extra odds calls. |
| Malformed training scores accepted | Domestic loading converted 1.8 goals into 1; negative/implausible goals could reach fitting. Duplicate source fixture rows could double their weight. | Require finite integer completed goals in 0–30 before conversion and fitting; reject duplicate domestic completed fixtures. Valid integer-valued floats remain accepted. |
| Duplicate quote outcomes accepted | Repeated home/away/draw or totals/BTTS outcomes overwrote earlier prices and could be treated as a complete market. | Reject the affected malformed market; retain independently valid markets and bookmakers. Cover main 1X2/O-U 2.5 and per-event alternate totals/BTTS parsers. Existing DC parser already rejects valid duplicate outcomes. |
| Failed optional capture was easy to miss | A sidecar marked PRESENT_BUT_REJECTED in detailed health could coexist with a top-level VERIFIED report and empty experiment CSVs. Raw checks covered only two sidecars. | Validate every present sidecar in raw checks; surface rejected archived evidence and latest rejected/missing/tampered capture states as top-level warnings. Baseline reporting remains usable. |

These are reproduced defects. There is no demonstrated effect from malformed
training scores or duplicate quotes on the currently published predictions.
All 20 committed domestic CSVs were inspected: 5,553 completed rows pass the
integer/range checks and contain no duplicate date/home/away fixture keys.

## Validation

- All 297 offline regression/integration tests passed, including nine added
  cases covering malformed scores, model input rejection, duplicate source
  fixtures, duplicate quote outcomes and visibility of rejected sidecars.
- All application and critical-module coverage floors passed; overall source
  coverage is about 87.1%. Coverage measures exercised statements, not proof
  that all input combinations are safe.
- Model offline self-test passed. Source compilation and CLI help smoke checks
  cover all project Python modules and the thirteen CLI entry points.
- Tests exercise six-league generation through capture, verified grading and
  workbook/report reconciliation. Publication tests cover concurrent remote
  updates using temporary local Git repositories.

## Limits and next steps

Live provider response completeness and delayed fixtures cannot be proved by
offline checks. Windows Task Scheduler behaviour and opening the workbook in
desktop Excel still depend on the installed user environment. CI must verify
the patch on Windows and Linux before merge. This audit did not spend API
credits, place bets or change production model parameters.

After merge, pull the code, generate fresh forecasts with the existing flags,
and push them before kickoff. Confirm accepted sidecar captures and look at
the top-level report warnings. Continue collecting forward evidence using the
existing fixed experiments; passing software checks does not establish model
profitability or eliminate future software defects.
