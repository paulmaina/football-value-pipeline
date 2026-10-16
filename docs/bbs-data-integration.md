# Big Balls Data collection and integration

The collector joins Big Balls Data observations to the existing football-data.co.uk
and football-data.org training caches. It exports a combined dataset with one row
per resolved match, provider identities, additional statistics, new eligible results,
and conflict reports. Standings, teams, players and upcoming fixtures are included
in the dataset. This is the collection/integration stage: the production fitter does
not yet consume these exports. No qualification thresholds, prediction commands,
existing caches, archived forecasts or model experiments are changed.

## Setup and commands

Install `football_value_requirements.txt`. Set `BBS_API_KEY` in your local `.env`
(see `.env.example`), or use an environment variable with `--api-key-source environment`.
Never commit the key. Existing training caches in `.football_cache` must be present;
refresh them with the project's existing refresh commands when needed.

```sh
python collect_bbs_data.py
python collect_bbs_data.py --leagues EPL --seasons 2026 2025 --max-requests 100
python collect_bbs_data.py --offline
python collect_bbs_data.py --offline --as-of 2026-10-16T00:00:00Z
```

The default season starts in July; `--seasons` accepts explicit start years. Start
with one league to check your account's actual coverage. Defaults are 200 requests
per UTC day, 150 per run, and up to 90 statistics responses per run. Requests are
paced, retried for transient network/server failures, and counted before sending,
including failures. Provider rate-limit/retry headers pause collection across runs.
Other applications using the same key are not included in this local counter.

The daily GitHub workflow is `Collect complementary football data`. Configure the
repository Actions secret `BBS_API_KEY`, merge the workflow, then run it manually
and inspect its reports before relying on scheduled collection. Without the secret,
it reports that setup is pending. It reads existing caches from the checked-out
repository and does not commit source data or forecasts.

## Storage and recovery

`football_data_db/bbs.sqlite3` contains raw response envelopes, timestamped normalized
observations, request counters and retry checkpoints. Headers/credentials are not
stored. Repeated cached imports retain the original observation time. Corrections
create new observations instead of rewriting earlier ones. Concurrent local runs
are blocked by `bbs.lock`; only remove a leftover lock after confirming no collector
is running. Back up the SQLite file while collection is stopped.

The workflow restores the newest main-branch `bbs-data-state` artifact and saves
state even after a partial collection. Restore failures stop collection. State
artifacts request 90-day retention; repository policy may shorten it. Artifacts are
not permanent backups: deleting/expiring all retained artifacts removes the ability
to reconstruct earlier observations. Keep independent backups for long-term replay.
A first run with no retained state starts a new store and logs that fact. Manual
runs on another branch do not replace the main branch's state on subsequent runs.

`football_data_db/enriched/latest.json` points atomically to a complete generation:

- `dataset.json`: combined match rows plus fixtures, standings, teams and players.
- `<league>_enriched_history.csv`: original source columns plus prefixed `bbs_*` data.
- `team_mappings.json`: resolved identities and mapping method.
- `report.json`: matched/added/unmapped/conflicting counts, per-league observation ages,
  record counts and collection errors. Observation age is not provider freshness.

Exit code 0 means collection finished (or an offline rebuild succeeded), 1 means
partial collection, and 2 means setup/integration failed. A partial run still exports
validated records and persists progress; it does not imply complete league coverage.
Statistics rotate across leagues, prioritizing unseen/old observations. Recent games
are rechecked daily and older statistics weekly; matches/standings are cached for a
day and entities for a week. Quota limits can delay backfill and entity collection.

## Joining and validation

Existing canonical aliases are reused. No fuzzy team-name guesses are accepted.
Unresolved identities remain in fixtures and reports. To resolve a reviewed identity,
create `bbs_team_map.json` with actual provider IDs and canonical team names:

```json
{"EPL": {"actual-provider-team-id": "Man United"}}
```

Do not use this example's placeholder ID. Multiple provider IDs mapped to the same
league/team are held as collisions. Fixtures join by league, UTC date and ordered
canonical teams. Duplicate fixtures, rescheduled dates, conflicting scores/statuses
and statistics belonging to different teams are reported. Existing values are never
silently overwritten or averaged. Missing statistics remain null, not zero.

New mapped finished domestic results can enter the combined export. New UCL results
are held because a generic final score does not establish the 90-minute result when
extra time is possible. Existing football-data.org UCL results use the project's
regulation-score helper. Original odds columns remain unchanged; this collector
never fetches or fabricates betting prices.

## Timing and model use

An observation timestamp means when we received a response, not when the provider
last refreshed it. Preserve any provider update timestamp separately; its absence
means source freshness is unknown. A cache hit does not refresh observation time.
`--as-of` restricts BBS observations only: existing caches are current revisions,
so this export is not a complete point-in-time reconstruction of legacy inputs.

Same-match statistics are post-match outcomes. They must not be used to predict
that match. A later feature-building change must use only earlier settled fixtures
and observations available before prediction time. Current standings must not be
backfilled into historical forecasts. Identity records alone are not predictive
features. Adding data does not establish improved calibration or profitability;
future model use needs validation against the existing evaluation process.

## Documented contract and unverified assumptions

References: https://bigballsdata.com/docs and https://bigballsdata.com/openapi.json.
The implementation targets `/v1/matches`, `/v1/standings`,
`/v1/matches/{id}/statistics`, `/v1/teams`, `/v1/players`, and `/v1/coverage`.
It uses Bearer authentication, league filters, season-start years, and limit/offset
pagination. It rejects explicitly ignored query filters and inconsistent scopes.
Free-plan basic statistics exclude xG; no paid endpoints or xG features are requested.
The published Free allowance is 250 requests/day (500 with GitHub linking), with
100/minute throttling. The lower defaults are our operating recommendation.

Documentation contains differing statements about Free historical access. The
collector therefore does not assume previous seasons or every statistic/league is
available. API errors and unavailable data are reported, and partial records remain
usable. Provider plan/coverage/schema changes can require adapter updates.

No authenticated live response was available during implementation. Offline tests
cover the documented contracts, not actual account entitlements. Verify pagination,
league coverage, team/player filters, scores and statistics
against a small authenticated run before treating this as an operational feed.

The documented request codes used here are `epl`, `laliga`, `bundesliga`,
`serie_a`, `ligue1` and `cl`. A coverage-endpoint outage is recorded as a partial
run while other endpoint collection and export continue.
