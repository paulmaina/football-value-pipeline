# Supplementary API-Football data on the free plan

API-Football is an additional source alongside football-data.co.uk,
football-data.org and BBS. Existing sources remain active. Relevant fixture,
result and match-statistics responses are collected independently of prediction
generation. The model reads committed observations without API calls.

## Setup

Add `API_FOOTBALL_KEY` to the project `.env` for deliberate local collection and
to GitHub repository Secrets for Actions. Use a direct API-Sports key, not a
RapidAPI subscription key. No key belongs in a commit, report, command argument,
or chat. Missing configuration leaves the scheduled collector inactive.

The **Collect supplementary API-Football data** workflow runs at 06:13, 14:13
and 22:13 EAT, and can be started manually on main. Collection has no default
local daily ceiling, per-run ceiling, statistics-candidate cap or reserved calls.
Due queries can use the provider's full remaining free allowance. Requests remain
seven seconds apart; confirmed zero remaining daily calls stops further requests
until the next UTC day. HTTP 429 respects the provider's retry window. Request
counts remain persisted as telemetry, not a local allowance. Old reserve-based
`blocked_day` entries no longer prevent use of the last 20 calls.

Caches, entitlement checks and data validation remain active. Collection ends
when all due work is processed, the provider refuses further calls, or the workflow
reaches its execution timeout. It does not issue duplicate calls just to burn quota.
Optional `--daily-budget`, `--max-requests` and `--stats-limit` arguments remain
available for deliberately restricted local runs; scheduled runs set none of them.

The account's live response confirmed free-plan access to season start years
**2022–2024**, with 2026 rejected. Both the CLI default and scheduled workflow now
collect 2024, 2023 and 2022 for all six competitions, newest first. Current-season
fixtures/results continue through the existing sources. These historical seasons
can fill training gaps only where they overlap the model's requested training window.
Historical statistics backfill continues through all due candidates until the
provider allowance is exhausted. Completed-season fixture responses are cached
for 30 days; valid historical statistics are retained without routine weekly
downloads. Unavailable historical statistics retry after seven days, allowing
other matches to be attempted on intervening passes.

Review `.football_cache/api_football/collection_status.json` and the Actions
summary. Reports give fixture totals, saved statistics, requested seasons and safe
query failure categories such as `PLAN_RESTRICTED`. Arbitrary provider error text
and credentials are never saved. Partial coverage produces an Actions warning;
a green workflow means collection state was safely published, not that every query
returned usable data. Current-season access is `NOT_REQUESTED` by default.

For a deliberate local collection, run:

```powershell
py collect_api_football_data.py
```

Override seasons only when your account permits them, for example
`--leagues UCL --seasons 2024 2023`. The permitted years are an explicit default
based on this account's observed response, not a guarantee for every subscription;
update them when the provider changes access.
Commit/push the `.football_cache/api_football` directory after local collection
so observations and its quota checkpoint reach Actions together. Existing
prediction commands remain the same. A Git pull brings cloud observations into
local fits; the next prediction generation consumes them.

## What becomes eligible for the model

* Completed FT/AET/PEN records need valid regulation-time scores, matching
  competition/season, valid identities and a kickoff before collection time.
  Extra-time and shootout totals are never substituted for 90-minute scores.
* Primary/BBS score history stays authoritative. Matching results are annotated;
  verified missing results can extend history within the requested training
  seasons. Conflicts, duplicate provider identities and possible reschedules are
  held. Bookmaker prices are never invented for added rows.
  UCL qualifiers/preliminary rounds and unknown phases stay collected but outside
  training/fixture eligibility, preserving the existing main-competition scope.
* Teams resolve through unique canonical names already in trusted history or an
  explicit reviewed map. Unknown/ambiguous identities are held, not guessed.
  A reviewed map at `.football_cache/api_football/team_map.json` uses league keys
  and provider team-ID strings, for example `{"EPL":{"42":"Arsenal"}}`.
* Recently observed, mapped NS fixtures can fill schedule gaps. Existing fixture
  pairs win when schedules disagree. API schedules older than 24 hours are not
  used. Odds still come through the existing odds pipeline.
* Match statistics remain observations of completed matches. They can influence
  **later** predictions only through the existing lagged-form validation gates,
  chronological partitions, evidence minimums and bounded goal-rate adjustment.
  Missing data or failed gates retain the ordinary model. The existing
  `--no-bbs-statistics` switch disables the shared supplementary statistics model.
  Statistics from AET/PEN matches are excluded because aggregate statistics can
  include extra time even when the score breakdown supplies a 90-minute result.
* BBS and API-Football observations of the same physical match count once in team
  form. Each provider's revisions/tombstones resolve at the prediction origin;
  available BBS fields retain precedence; consistent API observations can fill
  missing fields without counting another match. Statistics inconsistent with
  primary or BBS recorded fields are ineligible.

The legacy `bbs_statistics_*` model/report fields remain compatible. When
API-Football observations enter that validation path, `input_providers` identifies
them. Diagnostics also include explicit API-Football matched/added/conflicting
result counts, unmapped/ambiguous identities and statistics-observation counts.
The workbook health sheet displays the supplementary result counts. Collected
statistics are not a promise that any prediction adjustment passed validation.

## Integrity, freshness and recovery

Raw successful responses and immutable normalized observations are retained
with actual observation timestamps. Training/feature fingerprints include the
new inputs and adapter code. Newer quarantine records suppress old valid match
records; received invalid/empty statistics revisions suppress older revisions.
Network failures, plan denials and provider quota exhaustion retain existing valid
statistics rather than manufacturing a newer unavailable observation. Optional source
corruption is reported and retains the existing primary/BBS history.
Recent-season valid statistics refresh weekly; unavailable/invalid responses retry
after six hours. Historical statistics use the longer cache periods described above. Cached successful responses can rebuild an interrupted
normalization step without another request.
Unchanged normalized matches reuse their original observations. Compact,
timestamped schedule manifests bind unchanged upcoming fixtures to later
successful downloads without copying every season match on each polling pass.

The publisher merges immutable observations onto current main, preserves other
providers' changes and refuses to overwrite an advanced API-Football quota
checkpoint. It never force-pushes. Interrupted/unpublished collection state is
saved as a recovery artifact. A failed previous run no longer blocks a new run
merely because its request counter was unpublished: the provider controls the
allowance. Recover unpublished observations when needed; concurrent checkpoint
changes still stop publication to protect observation history.

Scope: fixture/results and the match-statistics fields consumed by the existing
model. Standings, injuries, lineups, vendor predictions and bookmaker odds are
not polled just because endpoints exist. Settlement/performance grading keeps
its existing football-data.org verification path. This integration does not
silently replace independent grading or add unvalidated predictor features.

Provider references: https://www.api-football.com/documentation-v3 and
https://www.api-football.com/pricing. Account-level access and live data quality
must be checked with your own subscription; offline tests use provider-shaped
fixtures and never require credentials.
