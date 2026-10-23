# Complete prediction generations and latest-selection monitoring

Normal prediction commands and model settings are unchanged. A successful run
now writes a complete, validated generation before publishing it for readers.

## Local generation

The predictor works in a private staging directory. Historical validation cache
files may be reused, but old forecasts and old optional experiment sidecars are
not copied into a new prediction run. After the requested leagues and sidecars
finish, the existing raw-output validator checks the complete generation.

Every successful run is frozen in `raw/prediction_runs/<64-character-run-id>/`.
Its manifest hashes all generated files, including prediction CSVs, shortlist,
summary, diagnostics, model/code metadata, available experiment sidecars and
new decision history. A single atomic `raw/current_run.json` pointer selects it.

Formatter, raw checks, capture, health reporting and closing collection resolve
this pointer once per operation and verify its bundle. They retain legacy raw
support when no pointer exists. Invalid pointers/checksums fail explicitly;
readers never silently switch to another generation. Top-level raw files remain
compatibility copies for older external tools. Standard readers use the bundle,
so a crash while refreshing those copies cannot expose mixed generations.
Do not edit immutable bundles. Backtests remain research outputs and are not
registered as new live prediction generations.

A writer lease rejects overlapping prediction/re-ranking writers in one raw
directory. Ordinary exceptions roll back compatibility copies and retain the
previous pointer. The lock directory records its owner (`owner.json`: PID,
host, process start time). A process killed before cleanup (closed terminal,
sleep/restart, `taskkill /F`) leaves the lock, and the next run reclaims it
automatically. It does that only when the owner process is provably gone on
this host (including a recycled PID), or when the lock has had no owner record
for 2 minutes. A live writer, or an owner on another host, still blocks the
run, and the error names the owning PID, host and start time. Manual removal
is only needed for a lock owned by another machine. If the pointer is
invalid, recover its exact original file/bundle from Git rather than editing
checksums to accept changed data. Distinct run directories can coexist safely
through ordinary Git reconciliation; never merge the contents of two bundles.
Keep one valid pointer and matching compatibility copies, and run
`py workflow_checks.py raw` after resolving a Git conflict.

Windows access/sharing denials during lock removal are retried for up to 3.1
seconds. A persistent cleanup failure logs a warning and leaves an ownerless
lock, which the next run reclaims after the grace period. It does not turn a
successful publication into an error or hide an earlier
generation/publication exception. Use `py workflow_checks.py raw` to validate the
currently published generation before deciding whether another run is needed.

The standalone shortlist refresh also publishes a new complete bundle. It
retains its explicit stored-forecast/no-new-odds provenance; re-ranking does not
make the underlying forecast inputs fresh.

## Upload and forward eligibility

Commit and push the raw directory with all saved generations. Multiple prediction
runs made before a single push are preserved, instead of only the last overwrite.
The forward workflow validates and captures each uploaded generation separately.
Each archive stores a distinct archive ID, the original run ID and the actual
source Git commit. Internal legacy snapshot identifiers continue to identify
archive directories; source Git identity remains separate and explicit.

Generation identity is independent of upload commit: uploading the same bundle
again does not duplicate its stake, replace its bytes or reset capture time.
First-entry comparisons break simultaneous-receipt ties by generation time.
Headline ROI and win rate use the latest eligible archived shortlist per fixture;
Run Tracking retains all eligible generation/fixture entries.

The actual receiving capture clock remains authoritative. A bundle saved before
kickoff but first captured inside the twenty-minute exclusion window is not
eligible for forward grading. Local timestamps are not upgraded to independent
historical evidence. Publish before kickoff with enough time for Actions to run.
Local files are preserved even when late upload prevents forward grading.

## Closing-price cohorts

`performance/closing_odds/summary.json` and `selections.json` now describe the
**latest eligible archived selection per match**, matching headline ROI.
`first_prediction_summary.json` and `first_prediction_selections.json` retain the
first-entry reference, and the Markdown report labels both comparisons.
The workbook's health view labels the active closing cohort too. Legacy closing
reports without the new tracking-basis field remain verifiable as first-entry
reports; the next review regenerates the two-cohort report.

Collection includes the union of first-entry and latest-entry selected markets,
even after the current shortlist changes. It reuses a fetched event payload and
keeps the existing daily request cap and six-minute quote window. A newly
required market may need an additional fetch if the earlier observation omitted
it. No quote is invented, and missing historic coverage remains missing.
Historical experimental first-entry baselines are unchanged.

## Current credentials and request modes

Copy `.env.example` to `.env` beside the script. Default local mode reads only
that file and clears inherited API-key values. To use deliberately exported
PowerShell/shell credentials, append `--api-key-source environment`. Cloud jobs
use repository Secrets in explicit environment mode.

Training defaults: six domestic seasons, four UCL seasons. `--seasons-back N`
overrides both; `--domestic-seasons-back N` controls domestic history separately.
Fixture retrieval: ten days. Shortlist: 48 hours, twenty-minute minimum lead,
twelve-match maximum, Under 3.5 excluded, unchanged 50/50 probability/EV ranking.

`--additional-odds-coverage all` is the default and has no ranked 24-attempt cap.
Use `ranked` for the shared 24-attempt allocation, accepting less market coverage.
These logical attempts do not cap provider credits: markets/regions, retries,
failover and optional market-led research can add usage. Model/statistical fitting
reads committed BBS cache data without extra BBS API requests. GitHub owns routine
BBS and closing collection; do not run the old Windows watcher simultaneously.
