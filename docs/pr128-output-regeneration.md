# PR #128: generated outputs require a pipeline run

No `football_output_v2/` artifacts are fabricated or hand-edited by these fixes.
The PR's current changed-file list contains no generated output changes to revert.
Existing committed outputs must be regenerated with the updated pipeline; they
must not be presented as evidence that the new code has already forecast UEL.

After merge, run **Scheduled forecast collection** on `main` (or let its next
scheduled run execute). It generates, validates, captures and publishes outputs
using current inputs and credentials. UEL can return only when verified training
is available: on failed refresh, its cached verification must be at most ten
days old. Check `league_availability.json` and the new run's training warnings
rather than restoring old UEL CSV/JSON files by hand.

The self-test and offline suites validate code paths, not regeneration of live
forecasts. No pipeline run or fresh generated output is claimed by this fix.
