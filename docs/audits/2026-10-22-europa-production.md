# Europa production integration — 22 October 2026

> Update, 25 October 2026: current-season league-phase training and settlement
> now require Cornerflick and Fixture Download to agree on the exact fixture
> identities, scores and completed-match coverage. UEFA's current-season article
> and pinned facts are no longer fetched or checked. Archived historical period
> evidence remains in use for 2025/26 to preserve reviewed regulation-time scores.
> Freshness, stage, duplicate and future-date checks still apply. This supersedes
> the three-source requirement described below.

This extends the earlier research audit. Europa (`UEL`) is registered in the
production pipeline and scheduled seven-league generation. A shortlist place
still depends on exactly the existing market, quote, EV, identity, reliability
and no-loss rules. Neither safety nor profitability is guaranteed.

## Gaps found, before changes

| Area | Verified gap / evidence | Likely cause | Impact / severity |
|---|---|---|---|
| Training | `LEAGUES` and `_history_for_league` had no Europa branch; reconciled records existed only in research outputs | Research intentionally isolated | No production Europa predictions; high |
| Identity | Generic `resolve_team` permits fuzzy name matching | Domestic-oriented fallback | Wrong club or league-average estimates in a sparse cross-country pool; high |
| Shortlist | `SUPPORTED_LEAGUES` excluded Europa; no Europa prior-appearance guard | Six-league scope | No eligible Europa candidates, or unsafe inclusion after a simple registration change; high |
| Validation | Default last-third start dropped useful Europa observations, despite a smaller declared warm-up | Shared domestic backtest default | Insufficient calibration samples; medium |
| Settlement | Result collection assumed football-data.org entitlement; Europa access was denied in the earlier source audit | Existing provider route | Europa bets could remain ungraded; high |
| Operations | Publisher selected six leagues; health warning labels assumed UCL | Existing fixed competition scope | Manual-only integration and misleading health labels; medium |

## Targeted changes and expected outcomes

- `europa_training.py` downloads source inputs to `.football_cache/europa/sources`
  and atomically writes `.football_cache/europa/training.json`. The production
  loader uses that snapshot. It bootstraps automatically and refreshes after
  24 hours; `--force-refresh` refreshes once per pipeline instance. Conflicts
  preserve the last snapshot and fail generation rather than pretend it is
  current. Historical sources are reused locally. Source hashes, provenance,
  attribution and refresh timestamp accompany the snapshot. Implementation:
  moderate; dependencies: public publishers; measure: reconciled identities,
  correct regulation scores, no duplicate/future rows, source health current.
- Europa identities use reviewed exact aliases only. Unknown clubs cannot pass
  via fuzzy matches. Both clubs need six verified prior appearances for a live
  shortlist candidate and historical evaluation. Implementation: small;
  dependency: alias review; measure: rejected unknown/thin fixtures and zero
  fuzzy identity admissions.
- Production validation starts after 250 training matches for Europa and uses
  the same chronological refitting, development-only penalties and untouched
  existing eligibility thresholds. Source identity/review code is included in
  validation fingerprints. Implementation: small; dependency: verified cache;
  measure: sample counts and reliability results, never a forced pass.
- The scheduled publisher includes `UEL`; budget reservations include all seven
  competitions. The existing all-coverage mode is unchanged. The new
  `--max-extra-event-odds-requests` option controls ranked-mode calls only.
  Implementation: small; dependency: existing GitHub secrets; measure: expected
  competitions and reported quote usage.
- Europa results use corroborated current league-phase records, actual UTC
  kickoffs and exact club identities. No football-data.org Europa entitlement
  is needed. Per-selection reports retain actual result-provider attribution.
  Implementation: moderate; dependency: all three current sources agreeing;
  measure: correct verified settlement and unresolved results remaining pending.
- Health checks re-evaluate Europa cache freshness and identify the actual
  competition in source warnings. Implementation: small; measure: stale or
  missing snapshots visibly reported.

## Cache inventory and verified local results

The working cache includes 30 domestic season CSVs (six seasons × five leagues),
four UCL season JSON files, and 11 Europa source downloads plus reviewed UEFA factual attestations. Existing BBS and
API-Football integration caches remain in their existing `.football_cache`
subdirectories. No new API-Football or FootyStats records were inferred or added.

Europa snapshot: **696 matches**, 2022/23–2026/27, latest result 15 October 2026.
This consists of 660 reconciled historical matches plus 36 corroborated current
league-phase matches. The 12 reviewed regulation-score corrections and one
match-specific opponent correction are retained. Eighty unclassified current
source rows remain quarantined. Raw provider extracts and the derived row-level
snapshot are local/ignored; the PR includes reproducible download/reconciliation
code rather than redistributing those extracts. A new checkout downloads them.

Real public-source refresh succeeded. Production fitting converged on all 696
matches. The local current-fixture path generated **18 forecasts**, of which
**12** have at least one club below six prior appearances. Historical evaluation
produced **246 eligible forecasts** (150 development, 96 audit for handicap
calibration). All 50 handicap line/side calibration reports met the existing
historical ranking checks for this retrospective run. Ordinary high-confidence
and all live shortlist gates remain separate. Over 1.5, Under 3.5 and BTTS fail
the ordinary reliability checks; only existing allowed markets can enter.

These results differ from the earlier research table because production uses
its own declared warm-up/window and validator. The research protocol has not
been relabelled as a production validation run.

## Commands

From the repository root, after checking out this PR or merging it yourself:

```powershell
py refresh_europa_training.py
py football_value_pipeline_v2_standalone.py --leagues EPL LaLiga Bundesliga SerieA Ligue1 UCL UEL --tune-half-life --goal-blend-experiment --additional-odds-coverage all --market-led-experiment --recency-experiment --reliability-experiment
py format_football_output.py
```

The explicit refresh is optional: the prediction command bootstraps/refetches a
missing or expired Europa cache. Default credential mode reads the project
`.env`; GitHub Actions uses `--api-key-source environment`. GitHub secrets are
not downloaded to your computer. Linux/macOS can replace `py` with `python`.
Use `--leagues UEL` to run only Europa. Defaults retain domestic six-season and
UCL four-season settings; Europa uses all verified cached history independently.

The readable shortlist remains at
`football_output_v2/readable/conservative_bet_shortlist_readable.csv`.

## Verification and remaining limits

- Seven-league offline integration covers prediction publication, shortlist,
  formatting, snapshot capture and verified forward grading with controlled
  quotes/results. This does not establish live bookmaker availability.
- Local full regression: 607 pytest cases passed; 600 unittest cases passed before the deployment fallback.
  Additional attestation regressions verify the fallback and rejection of uncovered results.
  Coverage: 88.98%; existing critical-module floors passed. Model self-test passed.
- Dedicated regressions cover invalid scores, future rows, duplicates, stale
  refresh failure, conflict rollback, exact aliases, thin teams, UTC schedules,
  token-independent Europa result collection and current source-health checks.
- Real local Europa generation used public source data and UTC schedule fallback.
  No live bookmaker credentials are present locally: zero shortlist picks in
  that run is expected and is not evidence of missing production routing.
- GitHub `Europa production integration check` uses configured secrets, ranked
  coverage and at most one additional event quote call. It produces derived
  reports and does not push forecasts, merge, or change main. Live access must
  be assessed from that workflow's actual diagnostics.
- The current source adapter explicitly supports the reviewed 2026/27
  league phase. New season/stage formats and knockout regulation semantics need
  review before admission. Unverified knockout results remain pending; they
  are not settled from concluding extra-time/penalty totals.
- No bookmaker-account execution, historical executable handicap prices,
  profitability claim, independent prospective Europa track record, provider
  uptime SLA or guarantee of optimal performance was established.

## Deployment finding: UEFA runner access

The first live GitHub integration check failed on HTTP 403 from UEFA, before
any bookmaker quote request. The same public download had succeeded locally.
This is a verified high-severity deployment dependency, not an inferred model
failure. Original factual attestations (club names, scores, AET flags, report
IDs/links and original source hash) are now provided for the previously reviewed
189 historical / 36 current UEFA matches. They are copied into the local cache.
A denied UEFA download uses those facts explicitly and records
`HTTP_403_USING_REVIEWED_FACTS`; it does not claim a live UEFA refresh.
Cross-source agreement is still required. New current results absent from the
reviewed facts fail closed until official verification becomes available.
This addresses fresh-checkout operation for covered matches, not reliable
future UEFA access. Source health and review warnings expose the limitation.

## Prioritized follow-up

1. Review Windows/Linux CI and the bounded live Europa integration workflow;
   merge PR #85 only after owner review.
2. Confirm fresh live quote coverage for preferred bookmakers and monitor
   rejected/qualified candidates, source freshness and pending settlement.
3. Accumulate prospective Europa calibration and settlement evidence without
   lowering cutoffs to fill the shortlist.
4. Arrange dependable authorized official verification for new results when
   UEFA denies runner access; refresh reviewed facts before admitting them.
5. Review the next knockout/season source format and regulation periods before
   extending the adapter. Add richer statistics only after entitlement,
   identity, coverage and out-of-time feature validation are established.
