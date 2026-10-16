# Big Balls Data in the shared training cache

All BBS data now lives under `.football_cache/bbs`, alongside the existing domestic
CSV and UCL JSON caches. There is no SQLite dependency or routine artifact download.
After GitHub publishes a successful or partial collection, `git pull` brings the
new data and collection checkpoints to local machines.

## Layout and future database migration

- `state/checkpoint.json`: UTC-day request counters, pacing and retry checkpoints.
- `state/responses/*.json`: latest cached response per query, with original retrieval
  time. API keys and request headers are never written.
- `state/observations/<kind>/<UTC timestamp>_<hash>.json`: immutable normalized
  observations for matches, statistics, standings, teams, players and coverage.
- `combined/snapshots/<UTC timestamp>_<hash>/<league>_enriched_history.csv`:
  normalized combined results/statistics, provider match/team IDs, observation times,
  source update times where supplied, integration status and conflict flags.
- The same generation includes `fixtures.json`, `standings.json`, `teams.json`,
  `players.json`, `team_mappings.json`, `report.json` and `manifest.json`.
- `combined/latest.json`: atomic pointer to a complete generation, including CSV
  checksums and cutoff. Incomplete generations are never selected.
- `team_map.json`: optional reviewed provider-ID to canonical-team mappings.

Immutable timestamped observations preserve corrections rather than rewriting
what was previously received. Combined snapshots retain each published view.
The CSV/JSON boundary can later be imported into a dedicated database. This does
increase Git history size; the first implementation intentionally retains history
rather than automatically pruning records needed for replay.

## Local usage

Pull data published by GitHub, then run the existing prediction command normally.
The pipeline's history loader reads the combined CSV in this cache automatically.
It joins additional fields onto freshly loaded primary history, preserves original
scores and bookmaker prices, and adds only eligible, mapped domestic results that
are absent from primary history. It does not double-count matches or restore stale
primary scores from an older combined snapshot. Different dates for the same ordered
team pair/season are held rather than assumed to be separate fixtures.

The fitter still uses its existing goal-history model. Additional basic statistics
are present as columns, but no shot/possession weights or other new features are
fitted in this PR. Adding verified results may change fitted predictions; thresholds,
commands and existing experiment definitions are unchanged.

If no BBS snapshot exists yet, the primary history works as before. A corrupt CSV
or checksum mismatch fails explicitly instead of silently entering model training.
A forecast cutoff before the first collected snapshot does not use BBS data.
For an older cutoff, the loader selects a complete snapshot no later than that cutoff.
The existing primary caches remain current revisions: this does not retroactively
make the legacy primary feed fully point-in-time. Archived forecasts are not rewritten.

Manual collection is possible, but GitHub should own routine collection to avoid
independent quota counters on multiple machines:

```sh
python collect_bbs_data.py
python collect_bbs_data.py --leagues EPL --max-requests 20
python collect_bbs_data.py --offline
python collect_bbs_data.py --offline --as-of 2026-10-16T00:00:00Z
```

For local collection put `BBS_API_KEY` in the project `.env`. For Actions use the
repository secret of the same name. Existing source caches must be populated.
`--store` now takes a directory, default `.football_cache/bbs/state`; old SQLite
files are not accepted. The earlier draft was not deployed by this change; if an
old SQLite collector was manually used, preserve its file for a separate migration
before starting a new observation history.

## 500-request plan and schedule

The user's GitHub-linked account has a 500-request/day allowance. The collector's
local defaults are 500/day, 500/run, and up to 500 statistics responses. The Actions
workflow runs at **06:43, 14:43 and 22:43 UTC** (**09:43, 17:43 and 01:43 EAT**) with
**500/day and 200/run**. A busy day can use 200 + 200 + 100 requests, preserving some
capacity for later freshness checks. It does not issue unnecessary calls just to
spend quota. Provider headers remain authoritative if another application consumes
part of the same account's allowance.

Requests are paced at least 0.7 seconds apart. Failed attempts and retries consume
the persisted budget; cache hits do not. A quota/defer response checkpoints progress
and ends the run rather than sleeping through long cooldowns. The daily counter
resets at midnight UTC (03:00 EAT). Fixture/standings pages refresh after six hours;
entities after seven days. Recent completed matches get priority over older backfill,
with statistics refreshed after six hours for the first two days, daily for the first
week, and weekly thereafter. Collection rotates statistics across competitions.

## GitHub publishing and recovery

The workflow runs on `main`, requires `BBS_API_KEY`, and commits only
`.football_cache/bbs`. It restores state from Git, not artifacts. Partial runs publish
validated observations plus explicit errors, coverage and quota counts. Publication
uses a fresh remote checkout, rebuilds combined CSVs against its current primary
caches/mappings, and retries ordinary push races without force-pushing. A concurrent
BBS checkpoint change stops publication rather than overwriting another collector.
Other workflows' results, forecasts and source caches are preserved.

After a failed run, a recovery artifact retains unpublished local BBS files where
possible. The next run checks whether the prior failed run's request budget was
published; an uncertain same-UTC-day allowance stops collection until recovered or
the day resets. Restore the failed run's state and observations carefully before
resuming if its unpublished observations are needed. Recovery artifacts are only
failure backups, not the normal distribution mechanism. Their retention is 30 days.
A force-killed job can still lose its last unpublished observations; Git holds all
successfully published history.

A `state.lock` lease prevents overlapping local collector writes. It is ignored by
Git; only remove a leftover lease after verifying no collector is running. Avoid
collecting locally while pulling or publishing: GitHub and local counters are not a
live distributed lock. Use the GitHub feed as the authoritative collector.

## Identity, conflicts and timing

Existing canonical aliases are reused; no fuzzy team-name guesses are accepted.
Unresolved teams and duplicate fixtures are reported, not silently added. Example
mapping structure (use actual IDs, never this placeholder):

```json
{"EPL": {"actual-provider-team-id": "Man United"}}
```

Each match retains provider IDs and timestamps. Scores, statuses, kickoff-date and
statistic disagreements are flagged, not averaged or silently overwritten. Missing
statistics stay missing, not zero. New UCL results are held unless regulation scores
can be established: a generic final score may include extra time.

A retrieval timestamp means when the response was received; it does not establish
when the provider last refreshed it. Reported observation ages are not claims of
source freshness. Current standings and same-match statistics cannot be used as
pre-match features for that same historical fixture.

## Contract and operational verification

The adapter follows https://bigballsdata.com/openapi.json, requesting Free endpoints
only: matches, standings, basic statistics, teams, players and coverage. No xG or
paid odds feed is requested. Codes: `epl`, `laliga`, `bundesliga`, `serie_a`, `ligue1`,
`cl`. Season filters are start years; pagination uses limit/offset and rejects
repeated IDs, truncated totals and explicitly ignored filters.

No authenticated key is available in this implementation environment. Actual
account coverage, historical access and response compatibility must still be checked
with a small live run. Tests exercise offline contracts, quota restart, corrections,
cutoff selection, CSV integrity, normal pipeline loading and publication push races.


## Live-coverage corrections and request strategy

The first live run returned 1,562 scheduled fixtures and no completed matches.
A bare `/v1/matches` request served upcoming rows, so a successful HTTP response
was insufficient to establish training coverage. Collection now sends explicit
`status=finished` and `status=scheduled` filters and rejects responses that do not
honor the status or requested season. Current-season postponed and cancelled
fixtures are checked too, so previously saved schedules can be corrected.

List requests use the documented maximum `limit=200` with `offset` pagination.
Current-season results are requested by default (explicit `--seasons`
still overrides this). Previous-season result pages are cached for seven days;
current results and scheduled fixtures for six hours; terminal status lists for a
day. The implementation uses the typed `/v1/matches` response contract. It does
not assume that GraphQL aliases or an undocumented batch request reduce quota.
The reviewed API contract exposes basic statistics per match; each uncached
statistics call costs a request.

After fixture/result and current standings refreshes, remaining requests go to
due current-season match statistics across the selected leagues, then older backfill.
Fresh cached statistics do not consume backfill slots. Team/player directory
backfill follows statistics. Free-plan historical access remains account-dependent:
a 403 is reported and cached for 24 hours rather than repeatedly spending quota on
the same denied request. Provider request limits and the shared 500/day budget still
apply. Missing/withheld xG is not requested or replaced with fabricated values.

`bbs_team_aliases.json` records reviewed league-specific club-name equivalents from
the first live audit. Fixture, team-directory and standings identities contribute
to mapping; reviewed aliases may bridge different IDs for the same club across
surfaces. Conflicting or duplicate fixtures are still quarantined. The core model's
global team-name rules are unchanged.

Coverage reports now distinguish completed results, scheduled fixtures, statistics
available/unfetched/unavailable, and team/player record counts. A run with no
completed results or incomplete statistics is partial even if every HTTP request
succeeds. Dataset reports additionally show baseline results lacking BBS confirmation,
per-field populated statistics, and standings-versus-history differences. Standings
comparison covers games played, wins, draws, losses, goals for and goals against;
missing identities and differences are explicit. Current standings remain a
cross-check, not historical predictor features.

Saved-response replay on commit `0c14c197d393cac3160d7b8d8d0829e35ad89fa1`
resolved all 1,562 scheduled fixtures (previously 908) and reconciled all 132
current-season standings teams with 333 existing completed fixtures. There were
no differences in the compared totals. This replay verifies mapping/reconciliation;
it does not prove completed-match retrieval or actual statistics coverage. Those
require the next authenticated collection after deployment. Existing observations
and published snapshots are preserved; no historical outputs were rewritten.


## Recovery after the second live run

The live Free key refused previous-season requests and `status=suspended` returned
400. Defaults therefore collect only the current season and omit suspended queries.
Explicit `--seasons` remains available for accounts with verified historical access.
Postponed/cancelled records are still checked.

Statistics with missing IDs can now use exact, reviewed club-name equivalents for
the expected fixture side. Non-empty contradictory IDs, missing names, opposite-side
names and ambiguous clubs are rejected. Normalized records retain original provider
IDs and identify whether each side was resolved by ID or verified name. Replay of
all 69 previously rejected cached responses passed these checks; cached responses
retain their original observation time and cost no new API requests.

Each malformed match is quarantined individually, with ID, reason and raw record.
Valid neighbors and later pages continue. A quarantined newer revision prevents
reusing older BBS data for that fixture until a later valid observation arrives.
Unscored finished UCL records never become zero-goal results.

Statistical disagreements retain both provider values and flag the disputed fields.
The existing primary value stays authoritative for existing inputs. Disputed BBS
statistics are explicitly ineligible for future features pending reconciliation;
this does not assert that either provider's differing value is correct. Identity
resolution and source timestamps remain in the exports. Standings refresh when newer
finished fixtures postdate their cached view; the report identifies possible timing
skew using available source update times without hiding differences.

Manual Actions runs now accept `max_requests` (default 500); scheduled runs remain
200/run. Both share the same persisted 500/UTC-day budget. If 271 requests have
already been used, a manual 500-request run can make at most the remaining 229.
Unavailable provider data may remain partial after all fetchable statistics are
collected. This is reported explicitly rather than fabricated or silently dropped.


## Pre-merge data safeguards

Quarantined revisions are excluded from statistics requests and coverage counts until
a later valid match observation arrives. Backfill and coverage respect the selected
seasons, and persisted unresolved quarantines keep the collection status partial.
Empty statistics objects remain unavailable; a present team name must agree with
the reviewed fixture identity even when its provider ID matches.

Multiple completed provider fixtures for the same ordered clubs in one domestic
league season are held as ambiguous even if their dates differ. The loader rechecks
BBS values against newly loaded primary statistics and disables disputed records
for future feature use while preserving the primary values. These checks do not
activate statistical predictor features. Failed or cancelled collections attempt a
recovery upload including the hidden cache directory; hard termination may still
prevent an upload, so the unpublished-budget guard remains in place.
