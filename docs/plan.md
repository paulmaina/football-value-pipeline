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
| 16 Jan – 10 Oct 2026, Eredivisie, Primeira Liga, Süper Lig (646 matches, 25 weeks) | Bet365, margin removed | Locked holdout: results no earlier benchmark or live report has scored |
| All other matches from 16 Jan 2026 | Bet365, margin removed | Retrospective: already scored by the earlier benchmark (five big leagues to 13 Oct) or the live reports (all leagues from 11 Oct). Diagnostics only, never release evidence |

- Pinnacle prices in the files stop on 15 Jan 2026; Bet365 continues for every league.
- On matches priced by both, margin-free Bet365 sits about 0.7 points from Pinnacle, with a 1X2 log-loss gap of about 0.0008. The harness measures this gap; on the holdout a candidate must beat the market by more than it.
- Expected return on the holdout uses synthetic Pinnacle-like prices (Bet365 margin-free probabilities plus Pinnacle's average margin) and is indicative only.
- xG changes become testable for the five Understat leagues once historical xG is backfilled (Phase 2). European fixtures become testable against results (no market prices) once the cached European results are added to the harness (Phase 2). Changes that depend on ESPN context or news can't be backtested: the live model keeps them as they are, and any change to them runs in shadow and reaches production only once live evidence is enough.

## Release gate

- Primary metric: log loss on AH settlement across all lines; draw-sensitive subset AH 0 and ±0.5; calibration tolerance (still to be set).
- Uncertainty: whole calendar weeks are resampled; the 95% interval must be clear of zero.
- Parity test (no waiting): the same match fed through the harness and the live pipeline must give identical probabilities.
- Replay over saved live runs (no waiting): the candidate runs over every forecast frozen since 5 Nov 2026 and must compute cleanly. Integration check only, not evidence of improvement.
- Monitoring after release: the weekly performance reports keep grading every pick, with a rollback trigger if the new model falls behind the old one by a set margin over a set number of matches.
- There is no forward waiting for changes the backtest can test.
- The holdout is scored only with a declaration file (`--declaration`). The declaration names a candidate and baseline registered in the harness, the primary metric, the draw-sensitive lines (must match the config) and the calibration tolerance, and the harness applies exactly those. A holdout run scores only the declared candidate, its baseline and the market reference.
- One evaluation per candidate and per frozen setup: the harness fingerprints the scoring code, model files, config and input data, and `evaluation/holdout_ledger.json` refuses a second run of either.

## Phases

1. **Evaluation foundation**
   - [x] Result matching and duplicate grading fixed (PR #136, merged 9 Nov 2026).
   - [ ] Evaluation harness (`evaluation_harness.py`): historical mode and live replay.
   - [x] Count each verified match once toward the sample size, while scoring each of its offers.
   - [x] Evaluation scope fixed to PR #135's markets (native Pinnacle AH, home/away win, DC 1X/X2) and the 24-hour window.
   - [x] Value model input schema plus the odds-perturbation test in the live pipeline, and the release-gate parity test (`team_research.INPUT_SCHEMA`, `tests/test_value_model_independence.py`, `evaluation_harness.py --mode parity`). Given the same inputs the harness and the live pipeline give identical research probabilities. The live inputs differ from the harness's (live forecasts to 8 Nov 2026), so these are reported and not fixed here:
     - ESPN form includes European, cup and other games the football-data files don't have: 388 of the rows used in the last-ten form, in 56 of 79 domestic forecasts. Pre-kickoff research (ESPN, Understat) moves 1X2 by 2.4 points on average (max 12.9) and changed 72 of 108 forecasts.
     - A live bug: one league match is counted twice when ESPN and the training history name a team differently ("Hull City" / "Hull", "Rayo Vallecano" / "Vallecano"): 108 duplicated rows in 46 of 108 forecasts. Fixing it changes live probabilities, so it needs its own PR through the release gate.
     - Goal rates: the harness refits on football-data every 14 days without BBS; live rates differ by 0.11 goals on average (max 1.13, largest in the Süper Lig, Primeira Liga and Eredivisie). The harness history stops at the fold origin (5.3 days earlier on average). The UEFA Europa League has no football-data file (29 forecasts).
2. **Improve the independent research model** (no market data): draw and low-score adjustment fitted on own history; wider xG coverage; domestic form carried into UCL/UEL; Understat historical xG backfilled for the five big leagues (via local Claude Code or a GitHub workflow, since the cloud workspace can't reach Understat) so xG changes can be backtested; European backtest using the European results already cached (about 575 UCL matches from 2023/24 via football-data.org and 732 UEL matches from 2022/23 via OpenFootball, Fixture Download and Cornerflick) as results-only test matches, topping up gaps from Cornerflick and Fixture Download.
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
| Release holdout | The 646 untouched matches (Eredivisie, Primeira Liga, Süper Lig, 16 Jan – 10 Oct 2026) |
| Still open | Calibration tolerance |
