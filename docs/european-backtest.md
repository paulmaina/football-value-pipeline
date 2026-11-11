# European backtest: UCL and UEL results as results-only test matches

Phase 2 of `docs/plan.md`, 11 Nov 2026. It adds the cached European club results to `evaluation_harness.py` (`--mode european`) so that a later candidate carrying domestic form into UCL/UEL (Phase 2c) can be backtested. No candidate is built here, and production is unchanged. The European holdout was locked (commit 966fc1b) before any European score was computed, and it has not been scored.

```bash
python evaluation_harness.py --mode european --output /tmp/europe          # locked: never scores the European holdout
python scripts/european_ce_report.py --run /tmp/europe --output evaluation/european_ce
```

## 1. Inventory of cached European results

Each result is loaded with the live pipeline's own loader: `FootballDataOrg.history` (cache-only) for UCL, and `europa_training.frame` on the verified snapshot for UEL. Scores are regulation time: extra time and penalties are removed. The totals equal the live fits of 8 Nov 2026: UCL 575 and UEL 732 training matches.

| Competition | Season | Matches | Dates | Source | Stages | Corrections |
| --- | --- | ---: | --- | --- | --- | --- |
| UCL | 2023/24 | 125 | 19 Sep 2023 – 1 Jun 2024 | football-data.org | group 96, knockout 29 | 3 decided on penalties (regulation score used) |
| UCL | 2024/25 | 189 | 17 Sep 2024 – 31 May 2025 | football-data.org | league phase 144, knockout 45 | 1 after extra time, 2 on penalties |
| UCL | 2025/26 | 189 | 16 Sep 2025 – 30 May 2026 | football-data.org | league phase 144, knockout 45 | 2 after extra time, 1 on penalties |
| UCL | 2026/27 | 72 | 8 Sep – 4 Nov 2026 | football-data.org | league phase 72 | 72 more scheduled, not played |
| UEL | 2022/23 | 141 | 8 Sep 2022 – 31 May 2023 | OpenFootball, reconciled to Fixture Download | group 96, knockout 45 | 3 regulation scores, 1 opponent identity |
| UEL | 2023/24 | 141 | 21 Sep 2023 – 22 May 2024 | OpenFootball, reconciled to Fixture Download | group 96, knockout 45 | 2 regulation scores |
| UEL | 2024/25 | 189 | 25 Sep 2024 – 21 May 2025 | OpenFootball, reconciled to Fixture Download | league phase 144, knockout 45 | 4 regulation scores |
| UEL | 2025/26 | 189 | 24 Sep 2025 – 20 May 2026 | Fixture Download matched to UEFA reviewed facts | league phase 144, knockout 45 | 3 regulation scores (UEFA match reports) |
| UEL | 2026/27 | 72 | 16 Sep – 5 Nov 2026 | Cornerflick + Fixture Download | league phase 72 | none |

Conflicts and top-up:

- **UEL.** The reviewed reconciliation (`scripts/europa_research.reconcile`, `audit_cornerflick`, `docs/audits/europa-team-aliases.json`, `europa-regulation-reviews.json`) was re-run on the cached sources. It stops on any unresolved identity or score conflict, and none remains. OpenFootball and Fixture Download agree on all 471 matches of 2022/23–2024/25. Fixture Download and UEFA's reviewed facts agree on all 189 of 2025/26. Cornerflick and Fixture Download agree on all 72 played league-phase matches of 2026/27, with 0 score conflicts and 0 unverified identities. The rebuild equals the committed snapshot exactly.
- **Corrections carried over from the reviewed files.** 12 concluding scores included extra time; each is replaced by its reviewed regulation score. One Fixture Download opponent is corrected (Leverkusen v Ferencváros, 9 Mar 2023).
- **Top-up: nothing added.** Every result on which two cached sources agree is already in the snapshot. Cornerflick's other 80 rows of 2026/27 are qualifying-round results (9 Jul – 27 Aug 2026, no round label). They have no second cached source, so they stay out.
- **UCL.** football-data.org is the only cached UCL result source: no Cornerflick or Fixture Download UCL file exists, so there is no cross-source check and nothing to top up.
- **No European prices.** There are no historical European prices. The only cached European odds are live Odds API snapshots from Oct–Nov 2026, which are not used.

## 2. European holdout (locked before scoring)

The split, the reasons and the strict alternative are in `docs/plan.md` ("Where the evidence comes from") and in `evaluation_harness_config.json` (`european`).

| Period | UCL | UEL |
| --- | --- | --- |
| Development (before 1 Jul 2024) | 125, all warm-up | 282, scored from 22 Feb 2024 |
| Validation (1 Jul 2024 – 20 Jan 2025) | 108, all warm-up | 108 |
| **Holdout (21 Jan 2025 – 12 Oct 2026)** | **288, 29 weeks (270 after the warm-up); locked** | — |
| Retrospective | 54 (from 13 Oct 2026) | 342 (from 21 Jan 2025) |

This block is below the 300-match release minimum. No untouched block reaches it after the 250-match warm-up, under either way of counting earlier touches. So, as configured, a European holdout run cannot pass the sample minimum.

## 3. CE: the research model as live runs it for UCL and UEL

CE is `team_research.prepare` + `research_grid` on two inputs:

- the fold's Dixon-Coles goal rates, fitted on the competition's own European results before the origin;
- the ten-match form from those same results.

The model settings are the live ones: half-life 480 days, L2 0.08, 10 goals, shots on but no shot data, and BBS off, as BBS isn't applied live for UCL or UEL. The rest of the setup:

- 14-day folds, history to the fold origin, so every forecast uses pre-kickoff data only.
- The 250-match warm-up is the pipeline's own UCL/UEL walk-forward warm-up.
- A fixture with a team that has no earlier match in the competition is left out, as live excludes it.
- Unlike live, there is no ESPN form: the harness has none.
- No odds and no domestic results are read.

Results only: there is no market reference, no cagey tier, no published-grid proxy and no market bar.

Log loss per fixture, mean with a 95% interval from resampling whole weeks. Every scored fixture is UEL: UCL before the holdout is all warm-up.

| Metric | Development (29 fixtures, 7 weeks; all knockout) | Validation (80 fixtures, 6 weeks; all league phase) |
| --- | --- | --- |
| 1X2 | 0.989 (0.913 to 1.134) | 1.125 (1.000 to 1.291) |
| AH all lines | 0.781 (0.695 to 0.891) | 0.836 (0.742 to 0.944) |
| AH draw-sensitive (0, ±0.5) | 0.748 (0.680 to 0.844) | 0.843 (0.723 to 0.975) |
| Over 1.5 | 0.520 (0.381 to 0.787) | 0.633 (0.440 to 0.965) |

- **1X2 reference.** Forecasting 1/3 for each outcome scores ln 3 = 1.099 on 1X2. On validation CE is no better than that: 1.125, and its interval includes 1.099.
- **Calibration: far too sharp.** Logistic slopes are well below 1, the opposite of the domestic C, which is too flat:

  | Period | Home slope | Away slope | Draw slope |
  | --- | --- | --- | --- |
  | Development | 0.71 | 0.21 | 1.73 |
  | Validation | 0.31 | 0.25 | 0.49 |

  Calibration rule v2, reported and not a gate, fails on the slopes in both periods. No band fails: 0 bands were checked on development and 1 on validation (draw 0.2–0.3: 24.3% forecast, 12.8% observed, 39 forecasts, z 1.67).
- **Samples are small.** These are 29 and 80 fixtures, so the intervals are wide. This fits the 26 Oct accuracy audit: rho at its +0.05 bound in UCL and UEL, many thin-history teams, and no cross-league information.
- **Coverage.**
  - UEL validation: 28 of 108 fixtures are left out, each with a team new to the UEL (first appearance).
  - UEL development: 253 of 282 fixtures fall in the warm-up.
  - Retrospective, counted and not summarised: UEL 310 scored; UCL 35 scored. UCL also has 18 in the warm-up, because locked fits have no holdout results, and 1 with no forecast. That one is Sporting CP v LASK, 21 Oct 2026: its fold's Dixon-Coles grid is invalid (rho at its bound, very large home rate). It is the same fixture the accuracy audit flagged for a live home rate of 6.10.

## 4. How much of Europe Phase 2c can reach

These counts show how many fixtures have domestic form for both teams. Domestic form here means at least 5 league matches in the 8 cached football-data leagues in the 365 days before the fixture. Teams are resolved by the reviewed research resolver (`team_research.history_team`), never fuzzy matching. Domestic holdout results are left out, as in every locked run. Holdout fixtures are counted by identity only.

| Period | UCL: both teams / fixtures | UEL: both teams / fixtures |
| --- | --- | --- |
| Development | 61 / 125 (49%) | 90 / 282 (32%) |
| Validation | 51 / 108 (47%) | 25 / 108 (23%) |
| Holdout | 160 / 288 (56%) | — |
| Retrospective | 21 / 54 (39%) | 95 / 342 (28%) |

At least one team has form in most fixtures: UCL 115/125 and 99/108; UEL 240/282 and 77/108. 94 of the 179 European teams resolve to one domestic club, and none is ambiguous. Most of the others play in leagues with no cached file (Belgium, Scotland, Greece, Austria, Czechia, the Nordic leagues and others).

Some are reviewed-alias gaps in covered leagues, which a Phase 2c alias review would add:

- SSC Napoli, SS Lazio, Bologna FC 1909
- Galatasaray SK, Fenerbahçe SK
- Real Sociedad de Fútbol, Real Betis Balompié
- Frankfurt
- n.e.c.

No alias was added here.

## 5. Tests

`tests/test_european_backtest.py` covers:

- **Inventory.** The loaders equal what live trains on, and the UEL snapshot rebuilds from its sources with nothing to top up.
- **Periods and the locked block.** 288 matches, 29 weeks.
- **The lock on the cached results.** A locked run never scores or trains on the European holdout.
- **A holdout run on synthetic results only.** It scores only the holdout.
- **The separate ledger.** It allows once per candidate and per setup, and refuses domestic candidates.
- **The setup fingerprint.**
- **A verdict with no market reference.**
- **CE independence:**
  - every odds field changed gives identical CE;
  - a later result never changes an earlier forecast;
  - a cache with no domestic files gives identical CE.
- **The report refuses holdout rows.**

## Adding a Phase 2c candidate

1. Register it in `EUROPEAN_CANDIDATES` and compute it next to CE in `evaluation_harness.european_matrices`. The candidate may read domestic results only from before the fold origin.
2. Compare it with CE on development and validation.
3. A European holdout run needs a declaration (`--mode european --declaration`), recorded in `evaluation/european_holdout_ledger.json`. As configured it cannot pass the sample minimum: see section 2.
