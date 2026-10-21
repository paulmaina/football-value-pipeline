# Europa League historical CSV audit

Assessment date: 22 October 2026 (Africa/Nairobi). Downloads: 21 October 2026, approximately 23:22–23:23 UTC.

## Decision

Fixture Download provides substantial historical Europa League results: four completed seasons, 660 rows. The files passed the structural checks below. They are suitable for further data preparation and research, but **are not ready to feed unchanged into a model for regulation-time markets**. Verified examples include extra-time goals in the single Result field, with no corresponding flag or separate 90-minute score. This audit did not train a model or establish predictive accuracy or profitability.

## Scope and assumptions

Downloaded the UTC CSV exports for 2022/23, 2023/24, 2024/25 and 2025/26 via the normal download links on Fixture Download. Parsed every CSV row locally with Python's standard csv and datetime libraries. Checked fields, dates, score syntax, fixture keys, match-number uniqueness/continuity, stages, team participation and chronological order. Compared nine selected results with UEFA sources, including finals and extra-time/penalty examples; this is a targeted sample, not an independent verification of every fixture.

The intended training target is the score after 90 minutes plus stoppage time, excluding extra time and shoot-outs. Qualifying rounds are outside these downloaded files. A structurally complete season does not prove every score, date, team identity or historical timestamp is correct. No production ingestion, repository changes, API-key access or paid odds requests were performed in this task.

## Verified coverage and structural results

| Season | Rows | Group/league phase | Knockout matches | Distinct source team labels | Group/league appearances per team | Missing results | Duplicate fixture keys |
|---|---:|---:|---:|---:|---|---:|---:|
| 2022/23 | 141 | 96 | 45 | 40 | 6: 3 home, 3 away | 0 | 0 |
| 2023/24 | 141 | 96 | 45 | 40 | 6: 3 home, 3 away | 0 | 0 |
| 2024/25 | 189 | 144 | 45 | 36 | 8: 4 home, 4 away | 0 | 0 |
| 2025/26 | 189 | 144 | 45 | 36 | 8: 4 home, 4 away | 0 | 0 |

The older seasons each contain 32 group-stage teams, eight groups of four, and eight additional labels appearing in knockouts. Every directed group-stage home/away pair occurs once. The newer seasons each contain 36 league-phase teams. All seasons have the expected knockout structure: 16 play-off, 16 round-of-16, eight quarter-final, four semi-final matches and one final. No qualifying stage is present.

Across all 660 rows: dates parsed using day/month/year hour:minute; all Result values matched two nonnegative integers separated by a hyphen; no blank dates, teams, venues or results; no self-fixtures; no duplicate Match Numbers within a season; no missing numbers in each season's 1..N range; no duplicate (date/time, home, away) keys or (calendar date, home, away) keys.

The older CSVs include a Group column, blank for their 45 knockout matches each. The newer CSVs omit that column. These blanks reflect stage structure, not evidence of missing results. Play-off stage spelling changes from “Play-offs Game” to “Play-off Game.” Source match numbers reset each season and are not cross-provider identifiers.

Observed result-goal totals are 381, 439, 556 and 512 respectively. UEFA's 2023/24, 2024/25 and 2025/26 overview totals agree with the CSV counts and goal sums [S6–S8]. The 2022/23 UEFA overview returned 237 matches alongside 381 goals; that scope discrepancy is unresolved. UEFA's financial report search extract explicitly gives 141 Europa League matches from the group stage [S9]; its full PDF could not be retrieved by the web reader because of its size. The 141-row structure is internally consistent, but the overview counter should not be used as an unqualified comparator.

## Findings and gaps, before proposed changes

| Priority / area | Evidence and status | Likely cause | Potential impact | Severity |
|---|---|---|---|---|
| 1. Score semantics | Verified: Man Utd–Lyon is 5–4 in CSV but 2–2 at 90 minutes; Lazio–Bodø/Glimt is 3–1 but 2–0 at 90 minutes. Freiburg–Lens and Roma–Bologna provide further examples below. CSV schema has only Result, with no extra-time or shoot-out flag. | Export represents the match's concluding playing score, including extra time where applicable. This inference is supported by examples, not a complete provider specification. | Incorrect regulation-time labels would distort goals, win/draw probabilities, handicap settlement and validation results. | High; blocks unchanged training ingestion |
| 2. Identity joins | Verified: source labels include both Sturm and Sturm Graz, and Betis and Real Betis across seasons; CSV has no stable team IDs. Man Utd, M. Tel-Aviv and Qarabag also differ from common provider labels. The production alias resolver was not tested in this task. | Display names and source naming conventions vary. | A name-only join could split one team's history, miss fixtures or attach odds incorrectly. These are potential effects, not verified production failures. | High integration risk |
| 3. Chronology | Verified: 2022/23 places Arsenal–PSV on 20 Oct before the next round's 6 Oct fixtures; 2023/24 places Villarreal–Maccabi Haifa on 6 Dec before 9 Nov fixtures. Each file has one adjacent chronological inversion; newer files have none. | Export groups fixtures by round rather than globally sorting actual dates. | A consumer assuming row order equals time could leak future results into backtests or miscompute form. No such production leak was demonstrated. | High if row order is used |
| 4. Scope and evidence gaps | Verified: files contain group/league stage onward, no qualifying matches, no historical prices, no pre-match snapshot timestamps and no rich performance statistics. Only nine results were independently sampled. | Fixture/result export has a narrow purpose. | Cannot establish EV, closing-line value, profitability, current-team sufficiency or full label accuracy from these files alone. Older data may add little weight for current teams. | Medium; limits validation |
| 5. Schema/provenance | Verified: optional Group column changes, play-off spelling changes, match numbers restart, date strings contain no offset. Source pages specify UTC by default and download names end in UTC. | Format evolution and presentation-oriented export. | Brittle fixed-schema loaders, cross-season deduplication and timezone assumptions could fail. | Medium |
| 6. Reuse conditions | Verified: terms permit personal noncommercial local extracts but restrict uploading, republication and storage elsewhere without permission [S10]. No permission for repository distribution was established. | Source terms impose reuse restrictions. | Committing source CSVs or distributing a cached dataset may be incompatible with the stated conditions. Production/cloud reuse needs clarification. | Deployment gate; not a finding of an existing violation |

## UEFA sample cross-checks

Nine selected CSV results were compared with UEFA. All nine agree with UEFA's concluding match score; that agreement does not mean all are valid 90-minute labels.

| Match / date | CSV Result | What UEFA establishes | Assessment |
|---|---|---|---|
| Sevilla–Roma, 31 May 2023 | 1–1 | 1–1 after extra time; Sevilla won shoot-out 4–1 [S1] | Shoot-out goals excluded in this example; do not infer shoot-out winner from Result |
| Atalanta–Leverkusen, 22 May 2024 | 3–0 | Final result 3–0 [S2] | Sample agrees |
| Tottenham–Man Utd, 21 May 2025 | 1–0 | Final result 1–0 [S3] | Sample agrees |
| Freiburg–Aston Villa, 20 May 2026 | 0–3 | Final result 0–3 [S4] | Sample agrees |
| Freiburg–Lens, 22 Feb 2024 | 3–2 | UEFA report identifies extra time; club report lists equaliser at 90+2 and winner at 99, establishing 2–2 in regulation [S11–S12] | Requires 90-minute replacement |
| Marseille–Benfica, 18 Apr 2024 | 1–0 | UEFA lists 1–0 after extra time and a separate shoot-out [S2] | Result excludes shoot-out; 90-minute score not separately established in this audit |
| Man Utd–Lyon, 17 Apr 2025 | 5–4 | UEFA goal sequence establishes 2–2 before extra time [S5] | Requires 2–2 regulation score |
| Lazio–Bodø/Glimt, 17 Apr 2025 | 3–1 | UEFA records equalising aggregate goal at 90+3, then goals at 100 and 109: regulation score 2–0 [S13] | Requires 2–0 regulation score |
| Roma–Bologna, 19 Mar 2026 | 3–4 | UEFA report lists three goals each in regulation and Cambiaghi's winner at 111 [S14] | Requires 3–3 regulation score |

The four demonstrated regulation-score discrepancies are a lower bound, not the total number of affected rows. Neither a low score nor a draw is sufficient to identify extra time. Stoppage-time goals such as 90+3 remain part of regulation time.

## Targeted recommendations

| Order | Proposed fix | Expected benefit | Effort | Dependencies | Success measure |
|---|---|---|---|---|---|
| 1 | Keep imported source results quarantined; attach a verified regulation-time score and source reference to every potentially extra-time knockout fixture. Reject unresolved scores rather than guessing. Preserve source Result separately. | Correct training/settlement labels. | Medium: adapter plus historical verification. | Authoritative 90-minute records and confirmed reuse route. | Zero unresolved regulation labels in training; regression examples above pass; extra-time and shoot-out values never enter regulation targets. |
| 2 | Map source team labels to stable canonical IDs with an explicit alias table; reject ambiguous joins. | Connect history and live odds consistently. | Small–medium. | Canonical team registry and current Europa participant list. | Every admitted row maps both teams unambiguously; zero duplicate identities or unmatched live candidates. |
| 3 | Parse UTC explicitly, normalize stages, scope IDs by source/competition/season, deduplicate, and sort by actual kickoff before fitting or splitting. | Robust ingestion and chronological evaluation. | Small. | Adapter and existing history schema. | Counts reconcile by stage; postponed-match examples sort correctly; each backtest training result predates prediction time. |
| 4 | Evaluate Europa League separately with chronological walk-forward tests and a final untouched holdout; add historical odds only through an entitled source. Check current-team history after time weighting. | Determines whether added history improves calibration and supports market selection. | Medium–large. | Corrected scores, mapped identities, historical quote coverage and live access. | Predeclared calibration/Brier/log-loss targets versus a baseline, adequate samples per market/team, and independently measured EV/settlement performance. No performance guarantee follows from dataset size. |
| 5 | Clarify source permission for automated/cloud storage and any redistribution before production deployment; keep raw exports out of the repository meanwhile. | Establishes a usable ingestion/distribution route. | Small technical effort; external response time unknown. | Provider terms clarification or a suitable licensed alternative. | Documented authorization covering the intended workflow. |

The 480 group/league-phase rows offer a straightforward initial research subset because those stages do not use extra time. The remaining 180 rows are knockouts; 92 are second legs or finals where extra-time review is especially necessary. These counts are structural, not certification of all scores. Use neither an arbitrary goal threshold nor “draw means refund” logic to infer 90-minute results.

## Prioritized next steps and remaining information

1. Resolve the permitted production storage/reuse route and preserve this audit's provenance.
2. Build a staging adapter with identity, UTC, schema, chronological and duplicate checks; keep production training unchanged.
3. Reconcile knockout scores against explicit regulation-time records. Independently verify a broader random sample, not just unusual matches.
4. Measure coverage of the current Europa League teams and effective sample sizes under the model's time decay; decide whether domestic history or older seasons add useful information.
5. Run separate Europa validation and shadow predictions before considering shortlist eligibility.

Still needed: a dependable permitted 90-minute history source, current-season fixture/result access, canonical team mapping, historical bookmaker prices if evaluating EV, acceptable calibration/sample-size criteria, and clarification of the inconsistent 2022/23 UEFA overview match counter. This task did not assess end-to-end importer behavior, current-season completeness, API reliability over time, or model performance after adding Europa League.

## Sources

[S1] UEFA 2022/23 season/match: https://www.uefa.com/uefaeuropaleague/history/seasons/2023/ and https://www.uefa.com/uefaeuropaleague/match/2037767--sevilla-vs-roma/
[S2] UEFA 2023/24 results: https://www.uefa.com/uefaeuropaleague/news/0285-18e1b3c016e7-7ad67605b4e1-1000--europa-league-all-the-fixtures-and-results/
[S3] UEFA 2024/25 results: https://www.uefa.com/uefaeuropaleague/news/0290-1bbed698826a-30134da51557-1000--europa-league-all-the-2024-25-results/
[S4] UEFA 2025/26 results: https://www.uefa.com/uefaeuropaleague/news/029c-1e9ad67620f2-05c31d01f0f4-1000/
[S5] UEFA Man Utd–Lyon report: https://www.uefa.com/uefaeuropaleague/news/0298-1d8bb1cd992d-9a76e3419e3f-1000--manchester-united-5-4-lyon-agg-7-6-harry-maguire-scores-winn/
[S6] https://www.uefa.com/uefaeuropaleague/history/seasons/2024/
[S7] https://www.uefa.com/uefaeuropaleague/history/seasons/2025/
[S8] https://www.uefa.com/uefaeuropaleague/history/seasons/2026/
[S9] UEFA financial report 2022/23, search extract only: https://editorial.uefa.com/resources/028a-1a2134203eb5-f59fe74100ae-1000/uefa_financial_report_2022-23_en.pdf
[S10] Fixture Download terms: https://fixturedownload.com/terms
[S11] https://www.uefa.com/newsfiles/uefacup/2024/2039940_FR.pdf
[S12] https://www.scfreiburg.com/en/latest/news/first-team/reports/2023-24/incredible-comeback-to-reach-the-last-16/
[S13] https://www.uefa.com/uefaeuropaleague/news/0298-1d8bb67ee012-448c5d8e41be-1000--lazio-3-1-bodo-glimt-agg-3-3-2-3-pens-norwegian-side-make-h/
[S14] https://www.uefa.com/newsfiles/uefacup/2026/2048133_FR.pdf

## Download provenance

Normal download landing pages are https://fixturedownload.com/download/csv/europa-league-YYYY and season previews https://fixturedownload.com/results/europa-league-YYYY, where YYYY is the start year. The downloaded raw CSVs were used locally for analysis; this report does not redistribute them.

- 2022/23: https://fixturedownload.com/download/europa-league-2022-UTC.csv — 10844 bytes; SHA-256 `a367dd37aaef0559c2efce4b3fe30506bca1410eaeba9ae8f7e184ce1e91c656`.
- 2023/24: https://fixturedownload.com/download/europa-league-2023-UTC.csv — 10766 bytes; SHA-256 `64b104cbd63ff0c5ea3afaa3e722c5587efcfcaa1ac99a7d944317a0a67ec538`.
- 2024/25: https://fixturedownload.com/download/europa-league-2024-UTC.csv — 13163 bytes; SHA-256 `ce2886cc24eef582f2c21e7728254f0bbf5b95d18c17feb99d57f2e1ffec29cb`.
- 2025/26: https://fixturedownload.com/download/europa-league-2025-UTC.csv — 13305 bytes; SHA-256 `850dde058c684632e210b7bbf456de95ef89b288cdde64d11ccc4d192995c8f5`.
