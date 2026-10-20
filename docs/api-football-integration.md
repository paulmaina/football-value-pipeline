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
and 22:13 EAT, and can be started manually on main. Each pass allows at most
20 requests, including at most 10 statistics queries; there is also a persisted
80-request UTC-day ceiling. The client spaces requests seven seconds apart and
stops when the provider reports 20 or fewer daily calls remaining. The account's
allowance is shared by all uses of the key; avoid running a second independent
collector with the same key at the same time. Default scheduled volume is at
most 60/day, leaving room under the provider's advertised 100/day free quota.

The free plan restricts season access. The collector requests the current season
for all six competitions, records rejected/empty queries as partial coverage and
leaves existing sources intact. It does not assume that advertised competition
coverage means your subscription permits current-season downloads. Review
`.football_cache/api_football/collection_status.json` and the Actions summary
after the first run. A denied season provides no supplementary coverage.

For a deliberate local collection, run:

```powershell
py collect_api_football_data.py
```

Historical backfill is optional, explicitly budgeted and subject to account
access, for example `--leagues UCL --seasons 2023 2024 2025 2026`.
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
Network failures, plan denials and exhausted budgets retain existing valid
statistics rather than manufacturing a newer unavailable observation. Optional source
corruption is reported and retains the existing primary/BBS history.
Valid statistics refresh weekly; unavailable/invalid responses can be retried
after six hours. Cached successful responses can rebuild an interrupted
normalization step without another request.
Unchanged normalized matches reuse their original observations. Compact,
timestamped schedule manifests bind unchanged upcoming fixtures to later
successful downloads without copying every season match on each polling pass.

The publisher merges immutable observations onto current main, preserves other
providers' changes and refuses to overwrite an advanced API-Football quota
checkpoint. It never force-pushes. Interrupted/unpublished collection state is
saved as a recovery artifact. After a failed Actions run with unpublished quota,
restore and commit the recovery state or wait for the next UTC day before
collecting. The guard fails closed rather than granting a fresh daily allowance.

Scope: fixture/results and the match-statistics fields consumed by the existing
model. Standings, injuries, lineups, vendor predictions and bookmaker odds are
not polled just because endpoints exist. Settlement/performance grading keeps
its existing football-data.org verification path. This integration does not
silently replace independent grading or add unvalidated predictor features.

Provider references: https://www.api-football.com/documentation-v3 and
https://www.api-football.com/pricing. Account-level access and live data quality
must be checked with your own subscription; offline tests use provider-shaped
fixtures and never require credentials.
