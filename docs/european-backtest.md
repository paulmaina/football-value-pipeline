# European backtest: UCL and UEL results as results-only test matches

Phase 2 of `docs/plan.md`. PR #158 (11 Nov 2026) added the cached European club results to `evaluation_harness.py` (`--mode european`), so that a later candidate carrying domestic form into UCL/UEL (Phase 2c) can be backtested. The European backfill (also 11 Nov 2026) adds older UCL and UEL seasons, so development has real data.

Phase 2c (section 6) adds the reviewed manual aliases and three candidates, CE2, CE3 and CE4. Production is unchanged. The European holdout was locked (commit 966fc1b) before any European score was computed, and it has not been scored.

```bash
python evaluation_harness.py --mode european --output /tmp/europe          # locked: never scores the European holdout
python scripts/european_ce_report.py --run /tmp/europe --output evaluation/european_ce
python scripts/fetch_european_backfill.py                                   # raw backfill files (already committed)
python european_backfill.py                                                 # reconciliation report, per competition and season
python scripts/european_candidates_report.py --run /tmp/europe --output evaluation/european_candidates  # CE2-CE4 against CE
```

## 1. Inventory of European results

### Cached seasons (what live trains on)

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

The reviewed UEL reconciliation (`scripts/europa_research.reconcile`, `audit_cornerflick`, `docs/audits/europa-team-aliases.json`, `europa-regulation-reviews.json`) rebuilds the snapshot exactly from the cached sources:

- It finds no unresolved conflicts.
- It applies 12 regulation-score corrections and 1 opponent correction, all from the reviewed files.
- There is nothing to top up. Cornerflick's 80 qualifying-round rows of 2026/27 have no second source, so they stay out.

football-data.org is the only cached source for UCL from 2023/24. No historical European prices are cached; the only European odds are live Odds API snapshots from Oct–Nov 2026, which are not used.

### Backfill (harness only)

The older seasons come from OpenFootball's champions-league repository and Fixture Download. The raw files are in `.football_cache/europa/backfill/`, with `manifest.json` recording the source URL, fetch time, HTTP status and sha256 of each file. They are fetched by `scripts/fetch_european_backfill.py` on 11 Nov 2026, with OpenFootball pinned to commit abfaedd, and marked `-text` so the bytes are never normalised.

They are reconciled by `european_backfill.py`. A result counts when one of these holds:

- OpenFootball and Fixture Download agree on the fixture (same teams, dates within a day) and on the concluding score.
- The season is single-source (labelled as such) and OpenFootball reports the result.

The regulation score comes from OpenFootball's explicit periods ("a.e.t." with the 90-minute score), the notation the reviewed UEL reconciliation already reads. Awarded and cancelled matches are left out.

| Competition | Season | Sources | OpenFootball | Fixture Download | Agree | Conflicts | Admitted | Stages | Extra time removed | Left out |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | --- | ---: | --- |
| UCL | 2015/16 | **OpenFootball only (single source)** | 125 | — | — | — | 125 | group 96, knockout 29 | 3 | |
| UCL | 2016/17 | **OpenFootball only (single source)** | 125 | — | — | — | 125 | group 96, knockout 29 | 1 | |
| UCL | 2017/18 | both | 125 | 125 | 125 | 0 | 125 | group 96, knockout 29 | 0 | |
| UCL | 2018/19 | both | 125 | 125 | 125 | 0 | 125 | group 96, knockout 29 | 1 | |
| UCL | 2019/20 | both | 119 | 119 | 119 | 0 | 119 | group 96, knockout 23 (single-leg finals tournament, Aug 2020) | 1 | |
| UCL | 2020/21 | both | 125 | 125 | 125 | 0 | 125 | group 96, knockout 29 | 1 | |
| UCL | 2021/22 | both | 125 | 125 | 125 | 0 | 125 | group 96, knockout 29 | 2 | |
| UCL | 2022/23 | both | 125 | 125 | 125 | 0 | 125 | group 96, knockout 29 | 0 | |
| UEL | 2019/20 | Fixture Download only | — | 197 | — | — | **0 (not admitted)** | | | |
| UEL | 2020/21 | both | 204 | 205 | 204 | 0 | 204 | group 143, knockout 61 | 2 | Villarreal v Qarabağ, 10 Dec 2020 (awarded 3-0) |
| UEL | 2021/22 | both | 139 | 139 | 139 | 0 | 139 | group 96, knockout 43 | 5 | Leipzig v Spartak Moscow, both legs (cancelled) |

- **Totals.** UCL 994 and UEL 343 admitted. Not one score conflict in any two-source season. The only unmatched row is the awarded match, which Fixture Download lists as a 3-0 result.
- **Gaps.** OpenFootball has no UEL file before 2020/21, so UEL 2015/16–2018/19 has no source and 2019/20 has Fixture Download only. Fixture Download has no UCL file before 2017/18.
- **UCL 2022/23 is included** although it lies outside 2015/16–2021/22: the cached football-data.org UCL seasons start in 2023/24, so without it there would be a one-season hole before the cached data.
- **Nothing on or after 21 Jan 2025 changes.** Every backfilled match is before the first cached match of its competition (UCL: 10 Jun 2023 against 19 Sep 2023; UEL: 18 May 2022 against 8 Sep 2022). The live loaders and every cached row, holdout and retrospective included, are unchanged. `european_results.load_with_backfill` returns exactly `load()` after the backfilled rows.
- **The live pipeline never reads the backfill.** It sits in a subfolder that neither live loader reads.

### Team names

No string comparison of any kind: within a season, two names are the same club only when every fixture of the club in the two sources has the same side, a date within a day and the same score (`european_backfill.derive_names`). Only rows before 21 Jan 2025 are read for this. The reviewed aliases are committed in `docs/audits/european-backfill-aliases.json`, and the tests re-derive them.

- **UEL** names go through the reviewed Europa resolver, plus 24 backfill aliases. Each points the club at the name it already has in the snapshot (e.g. "Celtic FC" → `celtic`, "KRC Genk" → `genk`). If the club has no name there, it keeps OpenFootball's name, and only the Fixture Download spelling is aliased, for matching (e.g. "Leipzig" → `rb leipzig`). No reviewed Europa alias is overridden.
- **UCL** names are put in football-data.org's spelling, which the live UCL loader uses, so a club is one team across backfilled and cached seasons. Within each season, the 32 Fixture Download names map to OpenFootball names by fixture evidence: 149 aliases in total, unresolved none.
- **Across seasons**, no fixture is shared, so continuity rests on a name. No source spells clubs the same way on both sides of 2022/23 → 2023/24:
  - OpenFootball switches to football-data.org's spelling in 2023/24 ("Bayern München" → "FC Bayern München"). Its 2023/24–2024/25 names map to themselves against football-data.org on 466 fixtures.
  - Fixture Download changes spellings from year to year ("Atlético" to 2022/23, "Atlético de Madrid" in 2023/24, "Atleti" in 2024/25).
- An older name is linked to a football-data.org name by either reviewed bridge:
  - (a) the same exact Fixture Download spelling on both sides;
  - (b) both names resolve to the same single domestic club through the reviewed research resolver (`team_research.history_team`).

  The bridges never disagree.

  | Link | Clubs |
  | --- | ---: |
  | Same spelling already | 19 (e.g. Liverpool FC, SSC Napoli) |
  | Linked by both bridges | 12 |
  | Linked by the Fixture Download spelling only | 6 |
  | Linked by the domestic club only | 4 |
  | Not linked | 40 |

  The 22 links are in the alias file (e.g. Atlético Madrid → Club Atlético de Madrid, Inter → FC Internazionale Milano).
- Of the 40 not linked, most never played the UCL again before 2025. Five did, in leagues with no cached file and spelled differently by Fixture Download, so they have no reviewed evidence and stay separate teams to the model:
  - Dinamo Zagreb / GNK Dinamo Zagreb;
  - Olympiakos Piraeus / PAE Olympiakos SFP;
  - Slavia Praha / SK Slavia Praha;
  - Qarabağ FK / Qarabağ Ağdam FK;
  - AEK Athen / PAE AEK.

  They were listed for review. Phase 2c links them by manual reviewed aliases (section 6), which rename only the backfilled rows.

## 2. Periods and the European holdout

The European holdout is unchanged. Its split and the reasons for it are in `docs/plan.md` ("Where the evidence comes from") and `evaluation_harness_config.json` (`european`).

| Period | UCL | UEL |
| --- | --- | --- |
| Warm-up (training only) | 2015/16–2016/17, 250 (exactly the two single-source seasons) | 2020/21 and 2021/22 to 24 Oct 2021, 252 |
| Development (end of warm-up to 30 Jun 2024) | from the 4 Sep 2017 fold: 869 | from the 25 Oct 2021 fold: 373 |
| Validation (1 Jul 2024 – 20 Jan 2025, unchanged) | 108 | 108 |
| **Holdout (21 Jan 2025 – 12 Oct 2026, unchanged)** | **288, 29 weeks; locked** | — |
| Retrospective (unchanged) | 54 (from 13 Oct 2026) | 342 (from 21 Jan 2025) |

- **Warm-up end.** Each competition's development now starts where its 250-match warm-up ends: the first 14-day fold origin with at least 250 earlier matches of that competition. That is the pipeline's own UCL/UEL walk-forward warm-up. The configured dates (`development_start`) are checked against the data on every run (`check_development_start`).
- **Fold grid.** `test_start` moved to 29 Jun 2015, exactly 185 folds before the old 1 Aug 2022, so every earlier fold boundary is kept.
- **Holdout minimum: 250 fixtures and 6 weeks.** This is `european_holdout_review_gates` in `benchmark_promotion_rules.json`, decided on 11 Nov 2026 before any European holdout scoring; the European ledger has no entry. The domestic minimum stays 300.
- **What a declared run would now score.** The warm-up ends in 2017, so no holdout fixture is in the warm-up (before, 18 were). Counted by identity only (dates and team names, no score read), a declared run would score **277 of the 288** holdout fixtures, in 29 weeks (276 before the Phase 2c alias review; unchanged by the 12 Nov 2026 alias scope change). That clears the 250 minimum.
- **The 11 left out** each have a team with no earlier UCL match, as live excludes them: Athletic Club, Como, Bodø/Glimt, Kairat, Fenerbahçe, LASK, Paphos, Real Betis, Union Saint-Gilloise, Sabah and Viking.
  - The reviewed aliases give AEK, Olympiakos, Qarabağ and Slavia Praha their older UCL matches, but only one more fixture becomes reachable: in the others the opponent is also new (for example Olympiakos v Paphos).
  - A fold whose Dixon-Coles grid is invalid would also give no forecast. That can't be checked without the results.

## 3. CE: the research model as live runs it for UCL and UEL

CE is `team_research.prepare` + `research_grid` on two inputs:

- the fold's Dixon-Coles goal rates, fitted on the competition's own European results before the origin;
- the ten-match form from those same results.

The model settings are the live ones: half-life 480 days, L2 0.08, 10 goals, shots on but no shot data, and BBS off, as BBS isn't applied live for UCL or UEL. The rest of the setup:

- 14-day folds, history to the fold origin, so every forecast uses pre-kickoff data only.
- A fixture with a team that has no earlier match in the competition is left out, as live excludes it.
- Unlike live, there is no ESPN form: the harness has none.
- No odds and no domestic results are read.
- With the backfill, the harness has more European history before a fold than live has today. Live trains on UCL from 2023/24 and UEL from 2022/23. The 480-day half-life keeps older seasons' weight small.

Results only: there is no market reference, no cagey tier, no published-grid proxy and no market bar. Log loss is per fixture: the mean, with a 95% interval from resampling whole calendar weeks. Forecasting 1/3 for each outcome scores ln 3 = 1.099 on 1X2.

### Development (1,154 fixtures, 107 weeks)

| Scope | Fixtures | 1X2 | AH all lines | AH draw-sensitive (0, ±0.5) | Over 1.5 |
| --- | ---: | --- | --- | --- | --- |
| All | 1,154 | 0.967 (0.931 to 1.005) | 0.745 (0.725 to 0.767) | 0.717 (0.691 to 0.747) | 0.529 (0.495 to 0.563) |
| UCL | 822 | 0.946 (0.905 to 0.987) | 0.742 (0.720 to 0.766) | 0.703 (0.675 to 0.734) | 0.492 (0.458 to 0.534) |
| UCL group stage | 626 | 0.928 (0.882 to 0.975) | 0.733 (0.710 to 0.759) | 0.686 (0.655 to 0.719) | 0.469 (0.432 to 0.506) |
| UCL knockout | 196 | 1.002 (0.938 to 1.069) | 0.771 (0.726 to 0.818) | 0.759 (0.711 to 0.809) | 0.568 (0.481 to 0.657) |
| UEL | 332 | 1.019 (0.955 to 1.088) | 0.752 (0.714 to 0.793) | 0.752 (0.703 to 0.805) | 0.620 (0.552 to 0.698) |
| UEL group stage | 221 | 0.997 (0.902 to 1.096) | 0.743 (0.690 to 0.798) | 0.741 (0.668 to 0.816) | 0.614 (0.534 to 0.712) |
| UEL knockout | 111 | 1.062 (0.996 to 1.138) | 0.769 (0.717 to 0.827) | 0.774 (0.726 to 0.831) | 0.631 (0.513 to 0.758) |

The development table is unchanged by the Phase 2c alias review to three decimals (draw-sensitive 0.7174 → 0.7175).

### Validation (194 fixtures, 7 weeks; all league phase)

Already inspected for UEL. After the Phase 2c alias review (193 fixtures before: GNK Dinamo Zagreb now has earlier UCL matches).

| Scope | Fixtures | 1X2 | AH all lines | AH draw-sensitive | Over 1.5 |
| --- | ---: | --- | --- | --- | --- |
| All | 194 | 0.985 (0.898 to 1.047) | 0.777 (0.704 to 0.846) | 0.736 (0.663 to 0.796) | 0.561 (0.443 to 0.717) |
| UCL | 101 | 0.960 (0.866 to 1.050) | 0.799 (0.704 to 0.900) | 0.732 (0.650 to 0.813) | 0.577 (0.489 to 0.666) |
| UEL | 93 | 1.011 (0.921 to 1.085) | 0.753 (0.681 to 0.824) | 0.741 (0.664 to 0.808) | 0.545 (0.379 to 0.775) |

UEL validation moved from #158's 80 fixtures and 1.125 to 93 and 1.011. The fold grid is the same; what changed is more UEL training history and fewer teams without an earlier UEL match.

### Calibration: still too sharp

These are logistic calibration slopes (1 = calibrated; below 1 = too sharp).

| Period | Scope | Home | Draw | Away |
| --- | --- | ---: | ---: | ---: |
| Development | All | 0.75 | 0.42 | 0.76 |
| Development | UCL | 0.83 | 0.58 | 0.82 |
| Development | UCL group stage / knockout | 0.82 / 0.84 | 0.65 / 0.07 | 0.82 / 0.87 |
| Development | UEL | 0.57 | 0.09 | 0.61 |
| Development | UEL group stage / knockout | 0.61 / 0.35 | −0.18 / 0.99 | 0.61 / 0.50 |
| Validation | All | 0.62 | 0.02 | 0.79 |
| Validation | UCL / UEL | 0.53 / 0.77 | −0.25 / 0.50 | 0.86 / 0.67 |

- CE is too sharp everywhere, the opposite of the domestic C, which is too flat. UEL is the worst; draw slopes near zero mean CE's draw probabilities barely sort draws from non-draws.
- Calibration rule v2 (reported, not a gate) fails in both periods on the slopes. Two bands also fail on development:
  - all fixtures: home below 0.1, 5.5% forecast against 14.7% observed, 75 forecasts, z 3.47;
  - UEL: home 0.3–0.4, 35.2% forecast against 58.2% observed, 55 forecasts, z 3.57.
- Draws are forecast at their observed level (development 22.0% forecast, 21.0% observed), so the problem is sorting, not the draw level.

### Coverage

- **Development.**
  - UCL: 822 scored, 37 with a team without an earlier UCL match, and 10 with no forecast. Those 10 are folds whose Dixon-Coles grid is invalid (rho at its bound), the same failure as Sporting CP v LASK in #158.
  - UEL: 332 scored, 41 with a new team.
- **Validation.** UCL 101 scored and 7 with a new team; UEL 93 scored and 15 with a new team.
- **Retrospective** (counted, not summarised): UCL 46 scored, 7 with a new team and 1 with no forecast; UEL 317 scored and 25 with a new team.

## 4. How much of Europe Phase 2c can reach

These counts show how many fixtures have domestic form for both teams. Domestic form means at least 5 league matches in the 8 cached football-data leagues in the 365 days before the fixture.

- **Older domestic seasons.** These now include football-data.co.uk 2015/16–2020/21 for the 8 leagues, in `.football_cache/domestic_backfill/` (48 files, manifest with sha256). They are used only here. They sit outside the cache's top level, so neither the domestic harness nor live reads them. They are read by `european_results.load_domestic_backfill`, which drops the empty trailing row some older files have (Serie A, Ligue 1, Primeira Liga 2015/16; Süper Lig).
- **Name resolution.** Teams are resolved by the reviewed research resolver (`team_research.history_team`), then by the reviewed European → domestic aliases below. There is never fuzzy matching.
- **Locks.** Domestic holdout results are left out, as in every locked run. Holdout fixtures are counted by identity only.

| Period | UCL: both teams / fixtures | UEL: both teams / fixtures |
| --- | --- | --- |
| Warm-up | 126 / 250 | 46 / 252 |
| Development | **519 / 869 (60%)** | **125 / 373 (34%)** |
| Validation | 56 / 108 (52%) | 27 / 108 (25%) |
| Holdout | 182 / 288 (63%) | — |
| Retrospective | 31 / 54 | 101 / 342 |

With the Phase 2c reviewed aliases (before them: warm-up 102 / 43, development 491 / 124). Since 12 Nov 2026 the manual aliases also link holdout and later fixtures (holdout 170 → 182, UCL retrospective 26 → 31; identity only). 119 of the 240 European team names resolve to one domestic club (113 of 245 before the five UCL renames), and none is ambiguous. Most of the others play in leagues with no cached file (Belgium, Scotland, Greece, Austria, Czechia, the Nordic leagues and others).

### Alias review (the nine gaps from #158)

`docs/audits/european-domestic-aliases.json` holds the European → domestic aliases. They are used for the European coverage only and are not read by the live pipeline.

Each is confirmed by fixture evidence. A source spells the club as the European files do:

- OpenFootball's football.json uses football-data.org's spelling, the same as the UCL files (pinned to commit e674442);
- Fixture Download's league files are read through the reviewed Europa resolver, for the UEL names.

Every domestic fixture of the club in that source matches football-data.co.uk on side, date within a day and score (2023/24–2024/25, before the domestic holdout). The tests re-derive the file.

| European name | Domestic | Evidence |
| --- | --- | --- |
| SSC Napoli | Napoli | football.json Serie A 2023/24 (38 of 38 fixtures) and 2024/25 (37) |
| SS Lazio | Lazio | football.json Serie A 2023/24 (38) and 2024/25 (37) |
| Bologna FC 1909 | Bologna | football.json Serie A 2023/24 (38) and 2024/25 (37) |
| Real Sociedad de Fútbol | Sociedad | football.json La Liga 2023/24 (38) and 2024/25 (37) |
| Real Betis Balompié | Betis | football.json La Liga 2023/24 (38) and 2024/25 (37) |
| frankfurt (UEL) | Ein Frankfurt | "Eintracht Frankfurt" (reviewed Europa alias → `frankfurt`), football.json Bundesliga 2023/24 and 2024/25 and Fixture Download 2024/25 (34 each) |
| n.e.c. (UEL) | Nijmegen | "N.E.C. Nijmegen" (reviewed Europa alias → `n.e.c.`), Fixture Download Eredivisie 2024/25 (34) |
| Galatasaray SK | — | **not added**: no source spells the club "Galatasaray SK" in domestic fixtures |
| Fenerbahçe SK | — | **not added**: no source spells the club "Fenerbahçe SK" in domestic fixtures |

An alias is looked up by its exact name or by the reviewed Europa key, so the UEL form `ssc napoli` finds "SSC Napoli". The UEL spellings `galatasaray` and `fenerbahce` already resolve. Galatasaray SK, Fenerbahçe SK and four older names in covered leagues (Bor. Mönchengladbach, VfL Wolfsburg, Leicester City in UCL and UEL, İstanbul Başakşehir) have no fixture evidence; Phase 2c adds them as manual reviewed aliases (section 6).

## 5. Tests

`tests/test_european_backtest.py` covers:

- **Inventory.** The loaders equal what live trains on.
- **Periods.** Including the warm-up.
- **The lock.** A locked run never scores or trains on the European holdout, and a holdout run on synthetic results scores only it.
- **The separate ledger.**
- **The setup fingerprint.** It covers every backfill file, the alias files and the domestic backfill.
- **The 250 and 300 minimums.**
- **CE independence:**
  - odds are ignored;
  - a later result never changes an earlier forecast;
  - CE is identical with no domestic file in the cache.

`tests/test_european_backfill.py` covers:

- **Raw files.** Every raw file matches its manifest; OpenFootball is pinned; no evidence file is from 2025/26.
- **Live loaders.** They are unchanged (575 and 732).
- **The parser.** Its notations, a season ending in August, and unknown notation stopping the parse.
- **Names.**
  - Fixture evidence only: a near-identical name with one different score is not mapped.
  - The committed alias files are what the evidence derives.
  - The five unlinked clubs stay apart.
  - The nine gaps.
- **Reconciliation.** Per season: admitted counts, 0 conflicts, single-source labels; UEL 2019/20 not admitted; awarded and cancelled left out.
- **No change from 21 Jan 2025.** No backfilled row reaches the cached seasons, and every cached row, in particular every row on or after 21 Jan 2025, is unchanged.
- **Harness behaviour with the backfill:**
  - development starts where the warm-up ends;
  - the fold grid is kept;
  - walk-forward holds and odds are ignored;
  - the lock holds;
  - the holdout reach reads no score.
- **The domestic backfill** loads and never enters the domestic harness or its fingerprint.

Domestic outputs are byte-identical between main and this branch (see the PR).

## 6. Phase 2c: reviewed aliases and candidates CE2, CE3, CE4

Offline only; production unchanged; the European holdout not scored (never `--declaration`); no odds, market fits or published grid anywhere.

```bash
python evaluation_harness.py --mode european --output /tmp/europe   # CE, CE2 (CE2p, CE2c), CE3 (CE3n), CE4; about 20 minutes
python scripts/european_candidates_report.py --run /tmp/europe --output evaluation/european_candidates
```

### Reviewed manual aliases

`docs/audits/european-reviewed-aliases.json`, marked "manual, approved by Paul in PR review". These are clubs that are plainly the same team but couldn't be linked by fixture evidence. Every holdout result row is byte-identical (tested against `reviewed=False` and against the live loader): the UCL renames touch only backfilled rows.

**Scope (12 Nov 2026).** Until then they applied only to European matches before 21 Jan 2025. Paul approved removing that limit on 12 Nov 2026, before any European holdout scoring, so they now link names in every European fixture, holdout fixtures included (`applies_to`, `scope_history` in the file). An alias is an identity mapping; no holdout result trains, fits or chooses anything. Effect (identity only): holdout reach stays 277 of 288; holdout fixtures with domestic form for both teams 170 → 182 (league phase 108 / 198, knockouts 74 / 90). European development and validation are unchanged for CE and all candidates (identical to 1e-12).

| Older / European spelling | Linked to | Country | Sources | Reason |
| --- | --- | --- | --- | --- |
| Dinamo Zagreb | GNK Dinamo Zagreb (UCL) | Croatia | OpenFootball UCL 2015/16–2022/23 / football-data.org 2024/25 | GNK is the club's legal prefix; only Zagreb club in the UCL |
| Olympiakos Piraeus | PAE Olympiakos SFP (UCL) | Greece | OpenFootball 2015/16–2020/21 / football-data.org 2025/26 | Legal name of Olympiacos |
| Slavia Praha | SK Slavia Praha (UCL) | Czechia | OpenFootball 2019/20 / football-data.org 2025/26– | SK prefix |
| Qarabağ FK | Qarabağ Ağdam FK (UCL) | Azerbaijan | OpenFootball 2017/18 / football-data.org 2025/26 | Same club, town in the name |
| AEK Athen | PAE AEK (UCL) | Greece | OpenFootball 2018/19 / football-data.org 2026/27 | PAE prefix; the only AEK in the UCL |
| Galatasaray SK | Galatasaray (Süper Lig) | Turkey | football-data.org UCL / football-data.co.uk T1 | SK suffix |
| Fenerbahçe SK | Fenerbahce (Süper Lig) | Turkey | football-data.org UCL 2026/27 / T1 | SK suffix; its UCL rows are all after 21 Jan 2025, so it links nothing yet |
| İstanbul Başakşehir | Buyuksehyr (Süper Lig) | Turkey | OpenFootball UCL 2020/21 / T1 | football-data.co.uk's spelling |
| Bor. Mönchengladbach | M'gladbach (Bundesliga) | Germany | OpenFootball UCL 2015/16–2020/21 / D1 | Abbreviated both ways |
| VfL Wolfsburg | Wolfsburg (Bundesliga) | Germany | OpenFootball UCL 2015/16, 2021/22 / D1 | VfL prefix |
| Leicester City | Leicester (Premier League) | England | OpenFootball UCL 2016/17, UEL `leicester city` / E0 | football-data.co.uk drops "City" |

Effect:

- **CE.** Development unchanged to three decimals. Validation goes from 193 to 194 fixtures, with AH all 0.779 → 0.777 (section 3).
- **Holdout reach.** 276 → 277 of 288, counted by identity only.
- **Both teams with domestic form.** Development UCL 491 → 519, UEL 124 → 125. The holdout stayed at 170 / 288 while the domestic aliases stopped at 21 Jan 2025; with the limit removed (12 Nov 2026) it is 182 / 288, as holdout fixtures of Galatasaray SK and Fenerbahçe SK now link to their domestic form.

### The candidates (`european_candidates.py`)

Every rule below was stated before any CE2-CE4 score was computed.

- **CE2, calibration only.** CE's draw is held, and its home share of a decided match becomes sigmoid(slope × logit). The slope is fitted for each 14-day fold by `research_sharpen.fit` on CE's own forecasts of decided European matches before the origin (480-day half-life). Its bounds are 0.2–2.5, because the slope can go below 1.
  - CE2p is pooled over UCL and UEL; CE2c is fitted per competition.
  - The rule: CE2 is CE2c only if each competition has at least 1,000 earlier decided matches, otherwise CE2p.
  - CE2 stays neutral below 300 decided matches. The domestic 1,000 would leave CE2 neutral through all of development, which has about 900 decided CE forecasts.
  - Result: no competition reaches 1,000 (at most UCL 769 and UEL 570), so **CE2 = CE2p in every fold**. It first moves on 23 Nov 2020. The slope runs 0.65–1.01 (median 0.81; 0.70 at the last fold).
- **CE3, domestic form and xG.** For each team with domestic form (at least 5 league matches in the 365 days before the fold origin, in the 8 cached leagues; nothing on or after the origin), its domestic research strength is computed:
  - Its expected goals for and against an average current opponent, both venues averaged, from the league's Dixon-Coles fit before the origin. These use live settings (shots on, BBS off) and are taken relative to the league mean.
  - That is shrunk with its last-ten domestic form, 10 : n, as the research model does.
  - For the five Understat leagues, Understat xG replaces goals in the form when at least 5 of the ten carry it, as in C3.

  The strengths are put on the European scale by league-strength factors. These are a weighted Poisson fit (480-day half-life) on earlier European results of both competitions in which both teams had a strength, with an N(0, 0.3²) prior pulling every league toward equal strength. They stay neutral below 100 such matches and first fit on 1 Oct 2018. At the last fold the factors (log goals) are EPL +0.30, Bundesliga +0.10, Serie A +0.08, La Liga +0.06, Ligue 1 −0.06, Primeira Liga −0.10, Süper Lig −0.15, Eredivisie −0.22.

  CE3's goal rates are exp(0.15 × log CE + 0.85 × log domestic) where both teams have a strength and the factors are fitted, and CE exactly elsewhere.

  The weight is fixed by a rule: the median share of domestic matches among domestic plus European matches in the 365 days before the fixture, over the warm-up fixtures (dates and names only). That gives 0.826 over 584 team-fixtures, rounded to 0.85. The weight is not tuned, and a test recomputes it.

  CE3n is the same with goals-only form. Domestic frames carry results, shots and xG only (no price column), and never a domestic holdout row, even in a European declared run.
- **CE4.** CE3, then CE2's calibration with the slope refitted on CE3's own earlier forecasts (same rule, bounds and minimum; pooled in every fold). The slope runs 0.71–1.05 (median 0.94).
- **In a holdout run.** A run that scores CE2, CE3 or CE4 also forecasts every non-holdout match of both competitions, unscored, so its fits learn from the same earlier matches as in a locked run.

CE3 uses its domestic strength on 546 of 1,154 development fixtures and 75 of 194 validation fixtures. Understat xG changes few of them: development is mostly before 2021/22, when Understat files start.

### Development (1,154 fixtures, 107 weeks): CE minus candidate log loss

Positive means the candidate is better. Whole weeks are resampled; * marks an interval clear of zero.

| Candidate | AH all lines (primary) | AH draw-sensitive | 1X2 | Over 1.5 |
| --- | --- | --- | --- | --- |
| CE2 (= CE2p) | +0.0008 (−0.0020 to +0.0037) | +0.0004 (−0.0032 to +0.0042) | +0.0003 (−0.0041 to +0.0050) | −0.0005 (−0.0011 to +0.0001) |
| CE2c (context) | −0.0003 (−0.0014 to +0.0007) | −0.0006 | −0.0007 | −0.0002 (−0.0005 to −0.0000) |
| **CE3** | **+0.0094 (+0.0001 to +0.0193)*** | +0.0070 (−0.0038 to +0.0180) | +0.0088 (−0.0043 to +0.0221) | +0.0244 (+0.0140 to +0.0352)* |
| CE3n (no xG) | +0.0100 (+0.0004 to +0.0200)* | +0.0076 (−0.0038 to +0.0189) | +0.0092 (−0.0041 to +0.0230) | +0.0233 (+0.0124 to +0.0348)* |
| CE4 | +0.0090 (−0.0005 to +0.0189) | +0.0060 (−0.0050 to +0.0171) | +0.0075 (−0.0058 to +0.0207) | +0.0241 (+0.0136 to +0.0350)* |

Mean AH-all log loss: CE 0.7449, CE2 0.7442, CE3 0.7355, CE3n 0.7349, CE4 0.7360.

By competition and stage (AH all, CE minus candidate; only CE4 on UEL is clear of zero, by a hair):

| Scope | Fixtures | CE2 | CE3 | CE3n | CE4 |
| --- | ---: | --- | --- | --- | --- |
| UCL | 822 | −0.0004 | +0.0083 (−0.0036 to +0.0202) | +0.0089 (−0.0031 to +0.0211) | +0.0068 (−0.0048 to +0.0187) |
| UCL group stage | 626 | +0.0001 | +0.0098 | +0.0100 | +0.0081 |
| UCL knockout | 196 | −0.0021 | +0.0036 | +0.0055 | +0.0027 |
| UEL | 332 | +0.0037 (−0.0030 to +0.0114) | +0.0122 (−0.0011 to +0.0281) | +0.0127 (−0.0014 to +0.0289) | +0.0142 (+0.0000 to +0.0305)* |
| UEL group stage | 221 | +0.0048 | +0.0096 | +0.0093 | +0.0128 |
| UEL knockout | 111 | +0.0017 | +0.0173 | +0.0194 | +0.0169 |

Over 1.5 is clear of zero for CE3, CE3n and CE4 in both competitions.

### Calibration (logistic slopes home / away; rule v2, reported, not a gate in locked runs)

| Scope | CE | CE2 | CE3 | CE4 |
| --- | --- | --- | --- | --- |
| Development, all | 0.75 / 0.76 fail | 0.82 / 0.83 fail | 0.84 / 0.84 fail | 0.88 / 0.87 fail |
| Development, UCL | 0.83 / 0.82 fail | 0.88 / 0.87 fail | **0.93 / 0.90 pass** | **0.96 / 0.93 pass** |
| UCL group stage / knockout | 0.82 / 0.82, 0.84 / 0.87 | 0.88 / 0.88, 0.88 / 0.89 | 0.92 / 0.94 pass, 0.99 / 0.79 fail | 0.95 / 0.97 pass, 1.01 / 0.81 fail |
| Development, UEL | 0.57 / 0.61 fail | 0.67 / 0.68 fail | 0.64 / 0.65 fail | 0.69 / 0.69 fail |
| Validation, all | 0.62 / 0.79 fail | 0.72 / 0.93 fail | **0.94 / 1.06 pass** | **0.93 / 1.04 pass** |
| Validation, UCL / UEL | 0.53 / 0.86, 0.77 / 0.67 | 0.62 / 1.00, 0.88 / 0.81 | 0.84 / 0.97, 1.11 / 1.17 (both fail) | 0.83 / 0.95, 1.10 / 1.16 (both fail) |

- CE's development band failure (home below 0.1: 5.5% forecast, 14.7% observed) does not appear for CE2, CE3 or CE4. No band fails for them in either period.
- Draws are forecast at their level: development 21.8% (CE3) against 21.0% observed.

### Context, not declared beforehand

- **Fixtures where CE3 used both teams' domestic form** (546 on development). AH all: CE3 +0.0199 (−0.0002 to +0.0400), CE3n +0.0211 (+0.0006 to +0.0424), CE4 +0.0189, CE2 +0.0025. Over 1.5: CE3 +0.0515, clear.
  - On this subset CE3 is now slightly too flat (slopes 1.12 / 1.13; CE 0.74 / 0.78). The rest of the fixtures are CE's and stay too sharp, which is why the overall slope is 0.84.
  - CE4's single pooled slope sharpens the subset further the wrong way (1.18 / 1.19).
- **After CE2's warm-up** (from 23 Nov 2020, 772 development fixtures). AH all: CE2 +0.0011 (−0.0033 to +0.0054), CE3 +0.0140 (+0.0018 to +0.0260), CE3n +0.0149, CE4 +0.0133, all three clear.

### Validation (secondary; 194 fixtures, all league phase; UEL already inspected)

| Candidate | AH all | AH draw-sensitive | 1X2 | Over 1.5 |
| --- | --- | --- | --- | --- |
| CE2 | +0.0036 (−0.0063 to +0.0127) | +0.0032 | +0.0038 | +0.0011 |
| CE3 | +0.0435 (+0.0136 to +0.0755)* | +0.0385 (+0.0033 to +0.0775)* | +0.0453 (+0.0054 to +0.0874)* | +0.0223 (−0.0034 to +0.0573) |
| CE3n | +0.0436 (+0.0110 to +0.0789)* | +0.0368 (−0.0010 to +0.0785) | +0.0436 (+0.0008 to +0.0882)* | +0.0208 |
| CE4 | +0.0429 (+0.0130 to +0.0748)* | +0.0377 (+0.0027 to +0.0769)* | +0.0442 (+0.0042 to +0.0864)* | +0.0220 |

On UCL validation (101) CE3's AH all is +0.0462 (+0.0197 to +0.0727), clear of zero.

### Reading

- **Calibration alone (CE2) doesn't help.** Pooled sharpness correction moves log loss by less than 0.001 and isn't clear of zero. The per-competition fit (CE2c) is slightly worse, and on UEL it is neutral for most folds.
- **Domestic form (CE3) is the gain.** It is the best or close to the best on every metric in both periods. Its primary metric is just clear of zero on development (lower bound +0.0001) and clearly so on validation. It also fixes most of CE's sharpness on UCL.
- **xG adds nothing measurable.** Understat covers only 2021/22–2024/25. CE3n is marginally better than CE3 on development.
- **CE4 doesn't improve on CE3.** Its pooled slope trades sharp CE fixtures against flat CE3 fixtures.

### Tests (`tests/test_european_candidates.py`)

- **Odds.** Every price column in the European and domestic rows changes, and CE2–CE4 and the domestic strengths stay identical. Domestic frames carry no price column.
- **Walk-forward.** A later European result never changes an earlier CE2–CE4 forecast. The league factors use only European matches before the origin and shrink to equal strength without data. Warm-up folds equal CE exactly.
- **Pre-kickoff.** No domestic match on or after the fold origin changes a strength.
- **The European lock.** A locked run scores no holdout row for any candidate. A holdout run on synthetic results scores only holdout rows, for CE2, CE3 and CE4, with fits learning from earlier unscored matches.
- **Fixed settings.** The blend weight is what its rule gives. The CE2 rule is pooled unless both competitions have 1,000 matches. C5's fit defaults are unchanged.

`tests/test_european_backfill.py` (ReviewedAliasesTest) checks the manual aliases: only backfilled rows are renamed, holdout rows are byte-identical, and the domestic aliases apply only before 21 Jan 2025.

## Adding a Phase 2c candidate

1. Register it in `EUROPEAN_CANDIDATES` and compute it next to CE in `evaluation_harness.european_matrices`. The candidate may read domestic results only from before the fold origin; the older domestic seasons are in `domestic_backfill`.
2. Compare it with CE on development and validation.
3. A European holdout run needs a declaration (`--mode european --declaration`), recorded in `evaluation/european_holdout_ledger.json`. Its sample minimum is 250 fixtures and 6 weeks; by identity, 276 holdout fixtures would be scored.
