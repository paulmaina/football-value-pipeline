# Background league training refresh

`Refresh league training data` is a separate GitHub Actions workflow. It refreshes every league in [`league_registry.py`](league-registry.md) whose refresh method needs no API key, without running forecasts or consuming odds API credits. Leagues are not listed in the workflow: a new registry entry with an existing refresh method is picked up automatically.

- football-data.co.uk leagues (refresh method `football-data.co.uk`): the current season every four hours at 03:17, 07:17, 11:17, 15:17, 19:17 and 23:17 EAT (GitHub may delay scheduled jobs).
- Each league's registry `history_seasons` window (six for the domestic leagues): automatically when the refresh code, registry or workflow is merged, or manually via Actions → Refresh league training data → Run workflow → full_history.
- UEFA Europa League (refresh method `europa-reconciled`): the reconciled Cornerflick / Fixture Download / UEFA snapshot on the same schedule. Its refreshed `.football_cache/europa/training.json` and `sources/` files are committed to main like the domestic CSVs. A source disagreement keeps the prior snapshot and fails the job; the pipeline still refuses a snapshot older than 24 hours.
- UCL (refresh method `football-data.org`) needs `FOOTBALL_DATA_API_KEY`, so it keeps its own `Refresh UCL training data` workflow.

Each method publishes its own commit, so a failed Europa reconciliation never blocks domestic data; the job fails visibly afterwards.

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
py refresh_training_data.py --full-history
py refresh_training_data.py --method football-data.co.uk --seasons-back 1
```

This validates all downloaded files before writing; publishing all files atomically is a Git workflow property, while local replacement is atomic per file. Upstream removals/date or team-name corrections fail closed and require review. The first version deliberately does not merge a second provider, invent missing results, regenerate predictions, or claim completeness from a latest-date check.

UCL now has a separate four-hour validated current-season refresh. See [daily evidence](daily-evidence.md) for its schedule/finished-match comparison, cache provenance, model/source freshness distinction and report integration. The scheduled forecast job also commits the training files of every registry league that it refreshed while generating forecasts.


## Prediction history window

The normal prediction command now reads six domestic seasons by default, including the current season. `--domestic-seasons-back 6` controls this window; use `--domestic-seasons-back 4` to reproduce the prior domestic window. UCL defaults to four seasons; this change makes no additional UCL provider requests. An explicit `--seasons-back N` still overrides both competitions as before; `--domestic-seasons-back` takes precedence for domestic leagues. Programmatic pipeline callers that omit the domestic override retain their existing shared window.

Original CSV statistics columns are retained, with their provider definitions. Loading more score history does not automatically make those columns BBS predictor features. Additional seasons do not establish improved accuracy; historical evaluations remain retrospective.
