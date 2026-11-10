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
   - [x] Value model input schema plus the odds-perturbation test in the live pipeline (`team_research.INPUT_SCHEMA`, `tests/test_value_model_independence.py`). No change to live probabilities: `scripts/check_research_unchanged.py --base main` finds all 4,379 frozen rows byte-identical.
   - [ ] Release-gate parity: harness and live give the same research probabilities for the same match. The shared research step is identical given the same inputs (max difference 5.6e-17 over 108 live forecasts), but harness and live inputs don't match yet (ESPN form, goal rates); see the measured gap below (`evaluation_harness.py --mode parity`, live forecasts to 8 Nov 2026). This stays open until the inputs match or the gap is accepted.
     - Holdout leagues (Eredivisie, Primeira Liga, Süper Lig; 29 forecasts) are reported separately. Research parity trains the harness with `training_rows(..., include_holdout=False)`, which drops their 16 Jan – 10 Oct 2026 results, so its fits for these leagues have a nine-month hole in recent form. That is why their gap is largest: goal rates differ from live by 0.28 goals on average (max 1.13) and 1X2 by 6.1 points (max 19.3). The other five leagues (50 forecasts): 0.017 goals (max 0.10) and 3.1 points (max 11.0). The same lock means 75 live form rows in the holdout window can't be checked against the files.
     - ESPN form includes European, cup and other games the football-data files don't have: 269 of the rows used in the last-ten form, in 39 of the 50 other-league forecasts (68 rows in 17 of 29 holdout-league forecasts). Pre-kickoff research (ESPN, Understat) moves 1X2 by 2.4 points on average (max 12.9) and changed 72 of 108 forecasts.
     - A live bug in research v1: one match is counted twice when ESPN and the training history name a team differently ("Hull City" / "Hull", "Rayo Vallecano" / "Vallecano"): 108 duplicated rows in 46 of the 79 domestic forecasts. Fixed in research v2 (next item). A related bug, a side with no training-history form when the fixture names it differently, is fixed in research v3; the parity report replays each forecast under the version it was frozen with, so these v1 forecasts still show the duplicates.
     - The harness also refits every 14 days without BBS, and its history stops at the fold origin (5.3 days earlier on average). The UEFA Europa League has no football-data file (29 forecasts).
     - Rerun under research v3 (`scripts/research_parity_latest_rule.py`, report `docs/research-parity-off-league-form.md`, 10 Nov 2026; probabilities only). Five big leagues, 50 fixtures: the mean research 1X2 gap is 2.23 points (max 11.0), down from 3.05 as frozen. Of it, European games in ESPN form account for 0.88, friendlies 0.74 (mostly October international-break friendlies, which the form also keeps), domestic cups 0.15, goal rates 0.33 and remaining history 0.13. With league games only, the gap is 0.46 (40 of 50 fixtures within 1 point). Holdout leagues, reported apart: 6.57, dominated by the lock (4.30 remains with league-only form on harness goal rates).
     - Recommendation: (b) exclude non-league games from live form for domestic fixtures, through its own shadow-first PR and the release gate. It moves live research 1X2 by 2.1 points on average (max 10.9). Adding the cached European results to the harness (a) closes at most 0.88 points and can't cover cups, friendlies or the Conference League. Not decided yet.
   - [x] Correctness fix, research v2 (`team-form-research-v2`): each match counts once in the last-ten form. A result is the same match when the team names agree or when the day, the team's venue and the score agree (`team_research.form_rows`). Changes live research probabilities for new forecasts only; frozen forecasts keep their v1 numbers and replay exactly under v1.
     - Released as a correctness fix, not as a candidate through the holdout: the backtest has no ESPN data, so it can't show this bug or its fix (its history has one row per team per day, so harness research probabilities are the same before and after). Evidence is a live-replay comparison plus monitoring.
     - Live-replay comparison (`scripts/replay_research_versions.py`, output in `evaluation/research_form_identity_replay/`): every frozen forecast recomputed from its own frozen inputs under v1 and v2. No result and no odds are read, so it shows how far probabilities move, not that they improve. All 689 frozen forecasts with research reproduce their frozen probabilities under v1 (max difference 8e-17); 366 change under v2, and none of the 3,690 without research changes.
     - Movement, latest forecast per fixture (108 fixtures, 5–8 Nov 2026): 57 change, with 128 repeated rows removed (46 domestic fixtures, 108 rows; 11 Europa League fixtures, 20 rows). Largest 1X2 move per fixture: mean 1.1 points, median 1.1, 90th percentile 2.3, max 4.9 (SC Cambuur v PSV); 10 of the 57 move 2 points or more. Over 1.5 moves 0.7 points on average (max 3.3), goal rates 0.03 goals (max 0.19). No direction: home −0.1, draw −0.1, away +0.2 points on average. Holdout leagues, reported apart (no result read): 16 fixtures, mean 1.6, max 4.9; the other five leagues and the Europa League: 41 fixtures, mean 1.0, max 3.6.
     - Monitoring: new forecasts are stamped v2; `evaluation_harness.py --mode parity` reports forecasts by research version and must show no double-counted rows on v2 forecasts; the weekly performance reports keep grading every value pick. The rollback margin and match count in the release gate are still to be set.
   - [x] Correctness fix, research v3 (`team-form-research-v3`): each side gets its own training-history form, however the fixture names it. v2 looked the history up under the fixture name, so a side the history names differently ("Hull City" / "Hull", "Real Sociedad" / "Sociedad") got none: 46 of the 158 sides in the domestic forecasts of 5–8 Nov 2026, and 25 of those had no ESPN form either, so the research made no form adjustment for their matches at all. `team_research.history_team` resolves each side to its training name from reviewed identities only (exact name, `bbs_team_aliases.json`, `TEAM_ALIASES`, canonical key, plus 12 reviewed research-only aliases in `team_research.HISTORY_ALIASES` that the model reached only by fuzzy matching); never fuzzy matching, and the answer must be exactly one training team, otherwise the side is left without history and warned. The training name is frozen in `research_history_json['teams']`; v1 and v2 forecasts have none and replay exactly under their own version. The new aliases stay out of `bbs_team_aliases.json`, which also decides the BBS identity checks, so the model's goal rates don't change. The harness and research backtest pass no names, so their research probabilities are unchanged.
     - Released as a correctness fix, like v2: in the backtest the fixture and history name teams the same way, so it can't show this bug. Evidence is a live-replay comparison plus monitoring.
     - Live-replay comparison (`scripts/replay_research_history_names.py`, output in `evaluation/research_fixture_name_replay/`): every frozen forecast with research, before = v2 on its frozen inputs, after = v3. The frozen history of a renamed side is empty, so after rebuilds that side from the pipeline's own training history (`_history_for_league`, local cache, as of 8 Nov 2026 12:20 UTC), cut like live to completed dates before the run day. All other sides keep their frozen rows. Checks: the rebuild reproduces all 895 frozen non-empty sides exactly; all 689 frozen forecasts reproduce under their own version (max difference 8e-17); the training name equals the model's resolved team on all 1,242 rebuilt sides, with none unresolved. No result and no odds field is read.
     - Movement, latest domestic forecast per fixture (79 fixtures, 5–8 Nov 2026): sides without training history 46 → 0, without any form 25 → 0; 20 forecasts change. Largest 1X2 move per changed forecast: mean 4.7 points, median 4.2, 90th percentile 8.8, max 10.2 (Monza v Atalanta BC); 8 move 5 points or more. Over 1.5 moves 1.9 points on average (max 4.1), goal rates 0.11 goals (max 0.33). The 20 changed forecasts hold 26 of the renamed sides, including all 25 without form. The other 20 renamed sides already had ten ESPN matches, and their form comes out the same. Larger than v2 because these sides had no form at all; v1 → v2 moved 1.1 points on average.
     - Holdout leagues, reported apart (no result read): 29 fixtures, 21 renamed sides, 13 with no form before and 0 after; 10 forecasts change, mean 4.7, max 8.7 points (Vitória SC v FC Porto). Other five leagues: 50 fixtures, 25 renamed sides; 10 change, mean 4.7, max 10.2.
     - UEFA Europa League (29 fixtures): not rebuilt, because the local checkout has no Europa training cache. Live resolves Europa sides with the reviewed Europa resolver (`europa_training.resolver`); 16 Europa sides still had no history in the frozen inputs, cause not checked here.
     - Monitoring and rollback: as for v2. New forecasts are stamped v3; parity reports forecasts by research version, and a v3 side without a training name carries a warning in its research. The weekly performance reports keep grading every value pick, under the same rollback trigger as v2 (margin and match count still to be set). The rollback is reverting the PR; frozen v3 forecasts keep their numbers.
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
| Duplicate-match fix (research v2) | Correctness fix: released with a live-replay comparison and monitoring, because the backtest has no ESPN data |
| Fixture-name fix (research v3) | Correctness fix on the same terms and rollback trigger as v2; reviewed aliases only, never fuzzy matching |
| Still open | Calibration tolerance; rollback margin and match count for monitoring |
