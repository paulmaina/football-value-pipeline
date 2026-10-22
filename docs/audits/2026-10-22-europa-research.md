# Europa League experimental implementation and results

Checked 22 October 2026. **Research implemented; production remains disabled.**
This extends PR #85 without merging it or changing the production league list,
shortlist rules, archived forecasts or production model caches.

## Verified outcome

The offline research pipeline reconciled 660 historical matches and fitted a
Dixon–Coles model on those plus 36 corroborated current league-phase results:
**696 research training rows**, ending 15 October 2026. The optimizer converged.
There are no historical prices in this experiment, so EV, ROI and bookmaker
blend performance remain unassessed. Research calibration passes are not
production approval or a guarantee of avoiding loss.

| Season | Historical rows | Extra-time matches identified | Regulation scores changed |
|---|---:|---:|---:|
| 2022/23 | 141 | 6 | 3 |
| 2023/24 | 141 | 4 | 2 |
| 2024/25 | 189 | 5 | 4 |
| 2025/26 | 189 | 5 | 3 |

For the first three seasons, every match identity/date and concluding score
was reconciled between OpenFootball and Fixture Download after the one reviewed
identity correction below. Regulation scores come from OpenFootball's explicit
period notation. Both sources agreeing is corroboration, not proof they use
independent upstream data. Not every older match was checked against UEFA.

For 2025/26, all 189 concluding scores matched unique UEFA article links by
canonical home/away names and reported score. All five article-marked extra-time
matches have individually reviewed UEFA Full Time Reports; three needed score
changes. The script rejects any change to the article's reviewed extra-time set.
**The article dates were not parsed**: those dates remain from Fixture Download.
An ambiguous pair/score join stops the run rather than guessing.

## Gaps and findings before deployment recommendations

| Risk | Evidence | Cause / impact | Severity |
|---|---|---|---|
| Wrong regulation labels | Twelve source Results include extra-time goals; explicit period scores/reports establish replacements. | Concluding scores were being considered as potential 90-minute labels. Would distort win, total and handicap learning. Corrected in research staging only. | High |
| Wrong opponent | Fixture Download lists Leverkusen–Fenerbahçe on 9 March 2023; OpenFootball lists Ferencváros. UEFA's technical report confirms Leverkusen beat Ferencváros 2–0 home and away in that round. | Source identity error, not an alias. Applied one date/home/opponent/score-scoped correction; the two clubs remain distinct. | High |
| Current-source stage ambiguity | Cornerflick has 116 results: 36 with League Stage round labels and 80 without. One sampled August qualifier's detail JSON says stage `league`. | Broad stage field cannot separate qualifiers safely. All 80 unclassified rows excluded. | High for unchecked ingestion |
| Thin current-team history | Thirteen of the 36 current teams have fewer than six appearances even after the 36 corroborated matches are added. | Europa-only history misses new entrants and much domestic evidence. League-average/fuzzy substitutes are not used to claim validation coverage. | High |
| Uneven market evidence | Over 1.5 failed the audit; Home/Away wins and DC X2 lack enough high-confidence examples. Other diagnostic passes have small samples and correlated outcomes. | Tournament/team turnover and model limitations. Blanket market enablement would overstate reliability. | High |
| No EV or prospective evidence | No historical executable prices, pre-kickoff snapshots, ROI or forward results in this experiment. | Cannot establish adjusted EV ≥1%, raw EV ≥0%, quote freshness or profitability. Existing shortlist criteria cannot be certified. | Deployment blocker |
| Current-source continuity | Cornerflick's last result is 15 Oct; metadata last refreshed 18 Oct. No refresh SLA or automatic grading recovery was tested. API-Football rejected seasons 2025 and 2026 under this plan. | Correct observed rows do not establish reliable ongoing collection. | Deployment blocker |
| Source reuse / reproducibility | Source files were inspected locally; full raw datasets are not committed. Fixture Download reuse restrictions remain unresolved for production/cloud storage. Inputs are fingerprinted in the aggregate JSON. | Production storage authorization and stable source revisions still need attention. | Deployment blocker |

## API-Football retry

[Run 39739089158](https://github.com/paulmaina/football-value-pipeline/actions/runs/39739089158)
used repository secrets inside Actions, six requests and **zero Odds API credits**.
Push-triggered retries now select only API-Football; manual provider selection
is retained. No credentials or raw match responses were extracted from GitHub.

| Season start year | Fixtures returned, including qualifiers | Regular FT | AET / PEN | Access |
|---|---:|---:|---:|---|
| 2022 | 175 | 165 | 10 | Confirmed |
| 2023 | 175 | 171 | 4 | Confirmed |
| 2024 | 269 | 256 | 13 | Confirmed |
| 2025 | — | — | — | Plan restricted |
| 2026 | — | — | — | Plan restricted |

All reported pages were read for the successful seasons. These 619 returned
fixtures are **not 619 additions** to the training set: overlap, qualifying-stage
identities and regulation semantics need reconciliation. This retry retained
aggregate evidence only and added zero API-Football rows to training.

## Cornerflick audit

Downloaded its season JSON and inspected two match-detail JSON samples. All
36 labelled league-phase results agree with Fixture Download on date/home/away
and score, and with UEFA's current-season article on home/away and score.
The corresponding UEFA article contains exactly 36 scored match links. There
were no duplicate accepted identities, missing accepted fixtures or score
disagreements. Reviewed explicit aliases resolve spelling/display differences.

These 36 regulation-time league-phase rows enter only the final research fit,
**after historical validation has completed**. None enters the development or
audit periods. Extra-time-capable/unclassified records remain excluded. The
upstream is API-Football, so comparison with that provider is not independent.

Data by Cornerflick — https://cornerflick.com. Its published compilation is
CC BY 4.0; its data page separately notes upstream terms for redistribution at
scale. No raw export is redistributed here.

## Frozen experimental protocol and measured results

- Initial history: 2022/23–2023/24. Development: 2024/25. Later audit: 2025/26.
- Fixed half-life 240 days, L2 0.08, 28-day refits. No half-life tuning or market
  blending; statistics features disabled. Every refit uses only dates strictly
  before its origin. No same-day result is used for a forecast on that day.
- Each evaluated team must have at least six earlier appearances, with exact
  canonical names present in the fitted model. This research guard is not a
  claim that six matches establish reliable team strength.
- 108 development fixtures and 118 audit fixtures qualified. The history guard
  excluded 81 and 71 respectively. Results apply to that subset, not all games.
- A development-only residual penalty sets the adjusted probability. The
  predeclared high-confidence gate requires adjusted probability ≥75%, at least
  30 development and 12 audit examples, audit Brier no worse than a **training-only**
  frequency baseline by over 0.005, and high-confidence overconfidence ≤0.10.
- Fifty handicap side/line combinations from −3 to +3 in quarter-goal steps
  measure probability of no full/half loss, including refunds. No quoted price,
  simulated profit or handicap value claim is inferred from this exercise.

| Market | High-confidence development / audit fixtures | Research result |
|---|---:|---|
| Home win | 4 / 4 | Insufficient sample |
| Away win | 0 / 1 | Insufficient sample |
| Over 1.5 | 56 / 47 | Failed audit |
| Double Chance 1X | 31 / 21 | Passed diagnostic |
| Double Chance X2 | 4 / 5 | Insufficient sample |
| Double Chance 12 | 34 / 28 | Passed diagnostic |
| Asian handicaps | Varies by side/line | 13 home-side lines passed diagnostic; 37 other combinations failed or lacked samples |

The 13 AH passes are home +0 through +3 at quarter steps; they are strongly
correlated and increasingly generous lines. They are not 13 independent
confirmations and do not establish that the available odds have positive EV.
Overall: 15 diagnostic passes, six failures, 35 insufficient samples across
56 market/line combinations. No market is production eligible.

Over 1.5 audit Brier was 0.2122 versus baseline 0.2065. Its high-confidence
audit group averaged 83.8% predicted probability but observed 72.3% (34/47),
exceeding the overconfidence limit. It must not be enabled from this evidence.
DC 1X's high-confidence audit group was 20/21; DC 12's was 25/28. Those are small,
retrospectively selected high-probability subsets, not expected future win rates.
The JSON includes Wilson intervals to make that uncertainty visible.

After those checks, the final research model fitted all 660 historical plus
36 corroborated current matches. Parameters and retrospective predictions
were written outside the repository for local inspection. No serialized model,
training rows or betting recommendations were added to production.

The audit outcomes were unseen by fitting/tuning at each historical origin,
but data were retrieved after the events and may contain later corrections.
This is a chronological retrospective experiment, **not a prospective test**.
The settings have not been revised to rescue the failed markets.

## Targeted fixes and action order

| Order | Action | Expected benefit | Effort / dependency | Success measure |
|---|---|---|---|---|
| 1 | Retain reviewed score/identity corrections and reject source conflicts. | Protect regulation targets and joins. | Implemented for this research snapshot; future revisions need review. | Counts/hash evidence reconcile; parser/conflict tests pass. |
| 2 | Add a permitted, monitored current-result collector with explicit stages and confirmed regulation scores. | Dependable model refresh and grading. | Medium; source continuity, reuse route and correction handling required. | Completed match coverage reconciles to UEFA; missed/late updates recover; no qualifier leakage. |
| 3 | Assess qualifying and domestic-history augmentation separately. | Address 13 thin-history current teams. | Medium; API-Football qualifiers need actual records and joins; domestic transfer requires a new modeling experiment. | Current-team effective sample sizes improve without worse unseen calibration. |
| 4 | Capture research predictions and real Pinnacle/bet365/1xBet quotes before kickoff. | Establish forward calibration, price quality and EV evidence. | Medium; existing odds access plus a reviewed experimental-only collector. | Immutable pre-off records, verified settlements, sufficient market samples, EV and freshness gates met. |
| 5 | Consider a separate production integration only for markets/teams that pass all gates. | Controlled Europa rollout. | Medium; preceding gates and owner review. | Same probability, loss-risk, EV and reliability rules as existing shortlist; no blanket activation. |

## Run and inspect

`scripts/europa_research.py` is an offline research entry point, not a new
production `--leagues` option. Supply entitled local source files in a separate
directory and keep all row-level outputs outside the repository:

```powershell
py scripts/europa_research.py `
  --source-dir C:/local-data/europa-source-staging `
  --output-dir C:/research/europa-results `
  --train
```

Required files: `openfootball-2022.txt`, `openfootball-2023.txt`,
`openfootball-2024.txt`; UTC `fixture-2022.csv` through `fixture-2026.csv`;
`uefa-2025.html`, `uefa-2026.html`; `cornerflick.json`. Source revisions must be
reviewed against the recorded hashes and counts; this is not an unattended
production downloader. The checked-in alias and official-report review files
contain the only explicit identity/period corrections.

The run writes local `history.json`, `model_parameters.json`,
`retrospective_predictions.json` and aggregate `report.json`. The committed
[aggregate results](europa-research-results.json) contain no full source rows.

Tests:
`py -m unittest tests.test_europa_research tests.test_europa_history_comparison tests.test_europa_access_audit`.

## Source references

- OpenFootball public-domain source files:
  https://github.com/openfootball/champions-league/blob/master/2022-23/el.txt
  https://github.com/openfootball/champions-league/blob/master/2023-24/el.txt
  https://github.com/openfootball/champions-league/blob/master/2024-25/el.txt
- Fixture Download: https://fixturedownload.com/results/europa-league-2025
  and https://fixturedownload.com/results/europa-league-2026 (earlier seasons as
  in the previous audit; UTC export URL pattern recorded there).
- UEFA 2025/26 article:
  https://www.uefa.com/uefaeuropaleague/news/029c-1e9ad67620f2-05c31d01f0f4-1000/
- UEFA current-season article:
  https://www.uefa.com/uefaeuropaleague/news/02a8-2174cafa5bb6-82bbc20c9b92-1000--2026-27-europa-league-all-the-league-phase-fixtures-and-re/
- Five official 2025/26 reports:
  https://www.uefa.com/newsfiles/uefacup/2026/2047786_FR.pdf
  https://www.uefa.com/newsfiles/uefacup/2026/2047787_FR.pdf
  https://www.uefa.com/newsfiles/uefacup/2026/2047789_FR.pdf
  https://www.uefa.com/newsfiles/uefacup/2026/2048132_FR.pdf
  https://www.uefa.com/newsfiles/uefacup/2026/2048133_FR.pdf
- Opponent correction: UEFA technical report, downloaded and text-inspected:
  https://editorial.uefa.com/resources/0282-1858e6a6971a-137653647ecd-1000/uel_technical_report_part_one_2022-23.pdf
- Cornerflick: https://cornerflick.com/football/leagues/europa-league/results/season.json
  and https://cornerflick.com/data
