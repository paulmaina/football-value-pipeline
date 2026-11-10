# Plan: independent research model, market tier and reconciled master shortlist

Agreed with Paul on 9–10 Nov 2026. The working copy is also kept as a claude.ai doc; this file is the repo copy, so any Claude Code session (local or cloud) starts with the same context.

## Goal

The pipeline holds two deliberately different opinions and lets the master shortlist weigh them.

| List | Its job | Probabilities come from | Must never use |
| --- | --- | --- | --- |
| Value shortlist | Find bets where the research disagrees with the market | Match history, ESPN results, Understat xG, domestic stats carried into UCL/UEL | Any bookmaker odds |
| Cagey tier | Safest bets, priced as close to Pinnacle as possible | Pinnacle 1X2, totals and main AH line, plus the narrow-margin correction | Research form or news |
| Master shortlist | Best bets after the two views are compared | Both lists' probabilities | A third model of its own |

Where bets are placed is a separate setting: all lists bet at Pinnacle only (`shortlist_quote_policy.json`). That has no effect on whether a model is independent. The published score grid already includes 70% Pinnacle, so it is a benchmark only and can never power the value model.

## Ground rules

- Nothing reaches production until it beats the current version on matches it has never seen, by more than noise. Mixed or small results: report them and keep the current rule.
- Pre-kickoff data only. Every test uses only what was known before the match.
- Decide the test before the data: candidate, metrics and subsets are declared before the holdout is scored.
- Shadow first. New logic writes beside the live files until it passes.
- One change per list at a time.
- Independence is enforced: the value model has an explicit input schema, and a test changes every odds field and checks its probabilities stay identical. Only the selection layer uses the Pinnacle offer, to calculate expected return and qualify a bet.

## Where the evidence comes from

Historical data in `.football_cache` (football-data.co.uk, 8 domestic leagues, 2021/22 to date). Run it with `evaluation_harness.py`.

| Period | Market reference | Use |
| --- | --- | --- |
| 2021/22 | — | Training history only (warm-up) |
| 1 Aug 2022 – 30 Jun 2025 | Pinnacle pre-match | Development: build and choose candidates |
| 1 Jul 2025 – 15 Jan 2026 | Pinnacle pre-match | Validation: already inspected by earlier diagnostics; cagey correction is out-of-sample |
| 16 Jan – 8 Nov 2026 (~2,100 matches) | Bet365, margin removed | Locked holdout, scored once per declared candidate |

- Pinnacle prices in the files stop on 15 Jan 2026; Bet365 continues for every league.
- On matches priced by both, margin-free Bet365 sits about 0.7 points from Pinnacle, with a 1X2 log-loss gap of about 0.0008. The harness measures this gap; on the holdout a candidate must beat the market by more than it.
- Expected return on the holdout uses synthetic Pinnacle-like prices (Bet365 margin-free probabilities plus Pinnacle's average margin) and is indicative only.
- xG changes become testable for the five Understat leagues once historical xG is backfilled (Phase 2). Changes that depend on ESPN, news or European matches can't be backtested: they go out in shadow straight away and reach production only once live evidence is enough.

## Release gate

- Primary metric: log loss on AH settlement across all lines; draw-sensitive subset AH 0 and ±0.5; calibration tolerance (still to be set).
- Uncertainty: whole calendar weeks are resampled; the 95% interval must be clear of zero.
- Parity test (no waiting): the same match fed through the harness and the live pipeline must give identical probabilities.
- Replay over saved live runs (no waiting): the candidate runs over every forecast frozen since 5 Nov 2026 and must compute cleanly. Integration check only, not evidence of improvement.
- Monitoring after release: the weekly performance reports keep grading every pick, with a rollback trigger if the new model falls behind the old one by a set margin over a set number of matches.
- There is no forward waiting for changes the backtest can test.
- The holdout is scored only with a declaration file (`--declaration`), and every holdout run is appended to `evaluation/holdout_ledger.json`. A candidate name can be scored once.

## Phases

1. **Evaluation foundation**
   - [x] Result matching and duplicate grading fixed (PR #136, merged 9 Nov 2026).
   - [ ] Evaluation harness (`evaluation_harness.py`): historical mode and live replay.
   - [ ] Count each verified match once toward the sample size, while scoring each of its offers.
   - [ ] Evaluation scope fixed to PR #135's markets (native Pinnacle AH, home/away win, DC 1X/X2) and the 24-hour window.
   - [ ] Value model input schema plus the odds-perturbation test in the live pipeline.
2. **Improve the independent research model** (no market data): draw and low-score adjustment fitted on own history; wider xG coverage; domestic form carried into UCL/UEL; Understat historical xG backfilled for the five big leagues (via local Claude Code or a GitHub workflow, since the cloud workspace can't reach Understat) so xG changes can be backtested.
3. **Confirm the cagey tier as the market view**: inputs all market prices; calibration checked out-of-sample.
4. **Master shortlist reconciliation, in shadow**: both views scored on the same Pinnacle offer. Research edge = positive expected return after costs. Disagreement = 5+ percentage points from Pinnacle's fair probability, a separate flag. Groups: both agree, market-safe, research edge (separate section), conflict (left out), missing evidence (recorded separately). Target stays 15 fixtures.
5. **Release**: one PR per change that passes; anything else stays in shadow.

## Decisions

| Decision | Choice |
| --- | --- |
| Grading fix | Separate reporting-only PR (done: #136) |
| Master shortlist size | Keep the 15-fixture target |
| Research-edge picks | Separate section of the proposed master output |
| Disagreement threshold | 5 percentage points, as a flag only |
| Holdout market reference | Bet365 with margin removed, gap-adjusted |
| Still open | Calibration tolerance |
