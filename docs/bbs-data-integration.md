# Big Balls Data: fresh results in the shared training cache

BBS supplies one thing: completed domestic results that football-data.co.uk has not published
yet (typically a weekend's matches before its Monday or Tuesday update), and confirmation of the
results it has. `bbs_integration.combined_training_history` adds a verified, mapped BBS result
to the training history only when the primary history lacks that match; primary scores and
prices are never replaced. On the 22 and 23 Nov 2026 runs this added 7 and 9 results per league;
once football-data.co.uk catches up, the same matches arrive as ordinary primary rows.

## Retired 25 Nov 2026: the statistics adjustment

The match-statistics adjustment (`bbs_statistics_model.py`, the `bbs_statistics_*` prediction
columns, the `--no-bbs-statistics` and `--bbs-statistics-validation` options and the weekly
`performance/bbs_statistics_forward.json`) was removed, with the statistics, standings, player
and coverage requests and their observation folders. In 779 committed league-runs from 9 Oct to
25 Nov 2026 it applied to no fixture (its gate never passed), so no published probability ever
used it. The shot-feature gate keeps its thresholds, which it used to import from that model
(`shot_features.py`). API-Football's collector still saves statistics (unchanged on purpose);
nothing reads them now. The code, the data and the forward report are in git history before the
removal.

At the same time the match observations were compacted. The collector used to store every
listing of every match three times a day (166,412 files for 1,896 matches). Now a match
observation is stored only when the match's state changes, and the store kept the first
observation of each state (2,848 files; `scripts/compact_bbs_match_observations.py`).

## Layout

All BBS data lives under `.football_cache/bbs`:

- `state/checkpoint.json`: UTC-day request counters, pacing and retry checkpoints.
- `state/responses/*.json`: latest cached response per query (match and team lists), with its
  retrieval time. API keys and request headers are never written.
- `state/observations/match/<UTC timestamp>_<hash>.json`: one immutable observation per change
  of a match's state. The state (`bbs_data.match_state`) is the normalized match without its
  volatile fields: `observed_at_utc`, `source_meta`, `has_odds`, `broadcast` and team logo URLs.
  A listing whose state equals the match's latest stored observation is not stored, unless a
  quarantine of that match is at or after it (the next valid listing is what lifts the hold;
  `bbs_data.match_observation_needed`). The latest observation at any cutoff therefore has the
  same state and quarantine outcome as if every listing had been stored; its `observed` time is
  when that state was first seen.
- `state/observations/quarantine/`: rejected match rows (wrong competition, season or status,
  invalid score), kept so a held match stays held until a newer valid listing.
- `state/observations/team/`: team directory entries, used only for mapping names when a club's
  ID differs between surfaces.
- `combined/generations/<content hash>/`: `<league>_enriched_history.csv` per league,
  `fixtures.json`, `teams.json`, `team_mappings.json`, `report.json` and `manifest.json`.
- `combined/latest.json`: atomic pointer to the one kept generation, with CSV checksums and cutoff.
- `team_map.json`: optional reviewed provider-ID to canonical-team mappings.

A forecast cutoff at or after the kept generation reads it directly; an earlier cutoff is
rebuilt from the observations and the primary caches (`bbs_integration.read_combined`). A
publish stages the new generation, switches `latest.json` atomically and then removes the old
one; a reader that loses a race with that removal re-reads `latest.json` once.

## Loading into training

`combined_training_history` joins the combined CSV onto freshly loaded primary history:

- a BBS row with the same date and canonical teams as a primary row adds only `bbs_*` match
  metadata and an `integration_status` (`matched`, or `conflict` if the scores disagree; the
  primary score is kept);
- a BBS-only, finished, mapped result with a verified regulation score, observed before the
  forecast cutoff and in the training seasons, is added (`integration_status` `added`,
  `history_source` `bigballsdata`), never for UCL and never when the same ordered pair already
  has a result that season (a possible reschedule is not counted twice);
- unmapped teams, duplicate provider fixtures and date disagreements are held and reported.

The run's diagnostics record what was used (`training_data_provenance`: confirmed rows, added
results, conflicts). A corrupt CSV or checksum mismatch fails explicitly.

## Collection

`.github/workflows/collect-bbs-data.yml` runs at 06:43, 14:43 and 22:43 UTC, requires the
`BBS_API_KEY` secret and commits only `.football_cache/bbs` (`publish_bbs_data.py`, which
rebuilds the combined CSVs against the latest primary caches on a fresh checkout and retries
push races without force-pushing). It requests only the free `/v1/matches` lists (finished,
plus scheduled, postponed and cancelled for the current season) and `/v1/teams`. Requests are
paced 0.7 s apart; provider quota headers and retry windows are authoritative; a defer
checkpoints and ends the run. Match lists refresh after six hours (current season), a day
(terminal statuses) or seven days (earlier seasons); team lists after seven days.

```sh
python collect_bbs_data.py                                   # needs BBS_API_KEY in .env
python collect_bbs_data.py --leagues EPL --max-requests 20
python collect_bbs_data.py --offline                         # rebuild from stored observations
python collect_bbs_data.py --offline --as-of 2026-11-20T00:00:00Z
```

The run report counts `match_observations_stored` and `match_listings_unchanged`, and per
league the completed matches, scheduled matches and team records. A run with no completed
results for a league, a quarantined record or a deferred request is `partial`.

A `state.lock` lease prevents overlapping local writes; remove a leftover lease only after
checking no collector is running. GitHub should own routine collection, so that one request
counter is authoritative.

## Identity, conflicts and timing

Existing canonical aliases (`bbs_team_aliases.json`) are reused; no fuzzy team-name guesses are
accepted. Score, status and kickoff-date disagreements are flagged, not averaged or silently
overwritten. New UCL results are held unless regulation scores can be established. A retrieval
timestamp is when the response was received; it does not establish when the provider last
updated it.
