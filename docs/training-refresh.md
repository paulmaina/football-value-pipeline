# Background domestic training refresh

`Refresh domestic training data` is a separate GitHub Actions workflow. It downloads football-data.co.uk data without running forecasts, consuming odds API credits, or using an API key.

- Current season in EPL, La Liga, Bundesliga, Serie A and Ligue 1: every four hours at 03:17, 07:17, 11:17, 15:17, 19:17 and 23:17 EAT (GitHub may delay scheduled jobs).
- Four seasons: automatically when the refresh code/workflow is merged, or manually via Actions → Refresh domestic training data → Run workflow → full_history.
- UCL is excluded because its training provider is football-data.org.

Validated CSVs are published to the existing `.football_cache` paths. A machine-readable audit at `docs/training_refresh_status.json` records each source URL, content hash, match count, newest completed result, download time and additions/corrections. The Actions run summary displays those dates. A successful request or recent check time does NOT mean the source has published recent results.

Downloads run in a small bounded pool. Invalid schemas, bad scores/dates, duplicate matches, wrong divisions, empty results and removals of previously recorded completed fixtures reject the batch before replacing files. Score corrections to existing fixtures are permitted and counted. Failed batches fail the Actions job rather than claiming a refresh. Publishing rechecks against the latest main branch and retries a concurrent push without force-pushing or merging CSV contents. All refreshed files and the status record publish as a single commit. No model settings, forecasts, archives or result reports are edited.

## Local use

The cloud job cannot update a Windows working folder directly. Before your usual prediction run:

```powershell
git pull --rebase origin main
py football_value_pipeline_v2_standalone.py --leagues EPL LaLiga Bundesliga SerieA Ligue1 UCL --tune-half-life --goal-blend-experiment
```

Training is refitted when the prediction command runs; the background job only refreshes inputs. The pipeline's existing four-hour cache TTL and stale-cache fallback are unchanged. Check training diagnostics after refitting to confirm which match dates the models actually used. If you have locally changed tracked cache files, commit your intended local work before pulling and resolve any reported conflicts explicitly.

For a training-only download locally, without odds calls:

```powershell
py refresh_training_data.py --seasons-back 4
```

This validates all downloaded files before writing; publishing all files atomically is a Git workflow property, while local replacement is atomic per file. Upstream removals/date or team-name corrections fail closed and require review. The first version deliberately does not merge a second provider, invent missing results, regenerate predictions, or claim completeness from a latest-date check.

UCL now has a separate four-hour validated current-season refresh. See [daily evidence](daily-evidence.md) for its schedule/finished-match comparison, cache provenance, model/source freshness distinction and report integration. The domestic behavior documented above remains unchanged.
