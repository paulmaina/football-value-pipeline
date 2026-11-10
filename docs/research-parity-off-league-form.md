# Research parity under research v3: where the 1X2 gap comes from

Report only (10 Nov 2026). No live probability changes. No result is scored, no odds field is read and no holdout score is computed. Script: `scripts/research_parity_latest_rule.py`; output in `evaluation/research_parity_latest_rule/` (`summary.json`, `forecasts.csv` with one line per fixture, and `espn_competitions.json` with the ESPN labels used).

## What was run

- **Latest rule:** every saved forecast is research v1. The latest forecast of each fixture (108, 5–8 Nov 2026) is recomputed from its frozen inputs under v3, with renamed sides rebuilt as in PR #144. All 108 reproduce the committed v3 replay (`evaluation/research_fixture_name_replay/forecasts.csv`) within its six-decimal rounding.
- **Harness side:** unchanged from `evaluation_harness.py --mode parity`: a fold refit on holdout-free football-data history, no BBS, history to the fold origin.
- **ESPN labels:** each ESPN result the live last-ten form keeps is labelled with the competition ESPN files it under (its league slug in the team's all-competitions schedule). The classes are league, domestic cup, other domestic, European, friendly and unknown. None came out unknown.
- **Split:** the live research is recomputed without cup rows, without European rows, without both, and with league games only; each version is compared with the harness. Cup and European shares are Shapley values over those four versions.
- **Gap measure:** for each fixture, the largest of the three 1X2 differences; means are over fixtures, in points.

## Five big leagues (50 fixtures)

| Live research | Mean gap | Median | Max | Within 1 point |
|---|---|---|---|---|
| As frozen (v1) | 3.05 | 2.26 | 11.0 | |
| **Latest rule (v3)** | **2.23** | 1.29 | 11.0 (Inter Milan v Como) | 22 of 50 |
| v3 without domestic-cup games | 2.07 | 1.38 | 11.0 | |
| v3 without European games | 1.34 | 0.68 | 8.0 | 30 of 50 |
| v3 without both | 1.20 | 0.71 | 8.0 | |
| v3, league games only | 0.46 | 0.08 | 4.3 | 40 of 50 |
| v3, league games only, harness goal rates | 0.13 | 0.00 | 3.6 | |

Where the 2.23-point mean gap comes from:

| Source | Points | Share |
|---|---|---|
| European games in ESPN form | 0.88 | 39% |
| Friendlies in ESPN form | 0.74 | 33% |
| Domestic-cup games in ESPN form | 0.15 | 7% |
| Goal rates (live fit with BBS vs fold refit) | 0.33 | 15% |
| Remaining history (fold origin, refit cadence) | 0.13 | 6% |

Shares are of the mean gap. Per fixture the largest-difference terms don't add exactly, but over the 50 fixtures they sum to the total.

ESPN rows the live form uses:

| Class | Rows | Fixtures using any | Competitions |
|---|---|---|---|
| European | 104 | 27 | Champions League 58, Europa League 34, Conference League 12 |
| Domestic cup | 50 | 25 | EFL Cup 29, DFB-Pokal 10, Coppa Italia 7, Copa del Rey 4 |
| Friendly | 34 | 24 | club friendlies; 25 of them in October 2026 (international break), 6 in September, 3 in August |
| League | 0 | 0 | ESPN's copies of league games all match a history row and count once |

Removing every non-league game moves live research 1X2 by 2.06 points on average (median 1.34, max 10.9). That is how far live probabilities would move under option (b).

## Holdout leagues, reported apart (29 fixtures)

Mean gap 6.57 points (max 19.3); as frozen it was 6.12. Here the gap is dominated by the lock, not by ESPN. Harness fits leave out these leagues' 16 Jan – 10 Oct 2026 results, so the gap is still 4.30 points with league games only on harness goal rates, and goal rates account for another 3.22. Removing cup and European games widens the gap (−0.62 and −0.50), because the live form then leans further on 2026 league results the harness can't see. ESPN rows used: European 37 (10 fixtures), cup 13 (12), friendly 4 (4). These leagues can't inform the choice below.

## UEFA Europa League (29 fixtures)

There's no football-data file, so there's no harness comparison. Rows in the live form: domestic league 113, European 57, cup 6, friendly 11.

## Recommendation: (b) exclude non-league games from live form (domestic fixtures)

- **It closes most of the gap.** League-only live form takes the five-league mean gap from 2.23 to 0.46 points (40 of 50 fixtures within 1 point). What remains is goal rates and history cadence, already listed under the parity item.
- **(a) closes at most the European share, and less in practice.** That share is 0.88 points (39%). The cache has no Conference League results (12 of the 104 rows), the UCL cache starts in 2023/24 while development starts in August 2022, and European results would need a second cross-source team identity. It can't touch cups or friendlies, which together are another 0.89 points, because there's no historical source for them in the harness. Parity would stay open.
- **(b) makes the value model testable.** With league-only form, live research uses the same kind of history the harness has, so the development backtest and the one locked holdout run measure the model that actually runs. Under (c) they never would.
- **Friendlies are the clearest case.** They are mostly international-break friendlies, which aren't competitive evidence, and they are a third of the gap.
- **(c) leaves a 2.2-point mean gap (max 11.0).** The release-gate parity item would stay open indefinitely.

**Caveats:**
- (b) changes live probabilities (mean 2.1, max 10.9 points in the five leagues). It is a model change, not a correctness fix: it needs its own PR, shadow first, and the release gate. This report makes no claim that it improves forecasts.
- European fixtures need their own rule: for a UEL/UCL fixture, the European games are its own competition. They belong with the Phase 2 work on carrying domestic form into UCL/UEL.
