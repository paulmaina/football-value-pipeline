# Data and model correctness audit — 17 October 2026 (EAT)

Audited repository snapshot: `fb6b5d192ed6ace91e508d9841de75ed911df14e`.
Forecast generation: `2026-10-16T22:16:28.500933+00:00`.
BBS dataset cutoff: `2026-10-16T21:31:13.338100+00:00`.

## Evidence from the pushed run

All six reconstructed input fingerprints match the pushed league diagnostics.
There are 111 forecasts, no duplicate fixtures, valid probability columns and
normalized 1X2 probabilities. The raw-output integrity check accepts the five
selected fixtures. Five selections do not establish profitability or justify
relaxing the existing selection rules.

| League | Primary completed rows | Combined fitted rows | BBS-linked verified results | BBS-only additions | Rows with BBS statistics |
|---|---:|---:|---:|---:|---:|
| EPL | 1,200 | 1,200 | 60 | 0 | 60 |
| LaLiga | 1,218 | 1,218 | 78 | 0 | 78 |
| Bundesliga | 963 | 964 | 46 | 1 | 45 |
| SerieA | 1,200 | 1,200 | 60 | 0 | 60 |
| Ligue1 | 972 | 972 | 54 | 0 | 54 |
| UCL | 539 | 539 | 36 | 0 | 27 |

The new Bundesliga result is present in the fitted history. Existing results
remain authoritative; no score conflicts were found in these fitted inputs.
Shots, possession, passing and the other BBS statistics are stored columns and
remain outside the probability model.

BBS statistics backfill has no unfetched records at this cutoff. Ten responses
are unavailable, and two unscored UCL records remain quarantined. There are 163
field disagreements across 80 matches. Both values remain available for audit;
disputed BBS records remain ineligible for future statistical features. These
provider gaps cannot be filled with invented values. Collection used 473 of the
500 requests for that UTC day; this is a historical count, not a live quota query.

## Confirmed defects repaired

1. **Different recency origins.** Tuning used forecast origins, but production
   and the ordinary backtest anchored decay at the latest result. Production,
   historical folds and newly generated shadow comparisons now use their
   corresponding prediction origin. Existing hyperparameters and selection
   thresholds are unchanged. With L2 regularization, a uniform shift in decay
   weights can affect fitted strengths; new forecasts can therefore change.

2. **Reviewed identities were unused by the model.** The pushed AEK Athens
   forecast used league-average strength despite training history under
   `PAE AEK`. Model resolution now uses the existing competition-specific reviewed
   aliases. The saved football-data.org response also identifies `RC Lens` as
   the short name of team 546, `Racing Club de Lens`, for match 575373 at the same
   kickoff as the odds fixture. This alias is recorded for UCL and Ligue1.
   Global canonical keys and archived fixture identifiers are unchanged.

3. **Silent loss of malformed training rows.** Bad CSV rows were skipped, while
   invalid/missing completed scores could disappear through coercion/dropna.
   Malformed completed rows now fail validation. Blank-score schedules remain
   excluded. Training validates dates, nonblank identities, same-team fixtures,
   canonical duplicates, scores and model parameter domains before optimization.

4. **Git timestamps mistaken for download freshness.** Each provider instance
   now attempts one live current-season domestic refresh per league. Downloaded
   CSVs are validated before atomic replacement, and a revision removing saved
   completed fixtures is rejected. Failed/invalid downloads retain a valid old
   cache with a warning. Pulling a repository no longer suppresses that first
   refresh merely because Git changed the file modification time.

5. **Unsafe odds joins.** Event-ID matches also require matching ordered team
   identities and kickoff agreement within five minutes. Ambiguous duplicate
   IDs or date/team matches are rejected. A unique validated odds event can
   supply the kickoff missing from a date-only fixture source.

6. **Incorrect opening-price fallback.** When the aggregate maximum is missing,
   historical price selection now takes the highest valid available opening
   price instead of the first configured bookmaker. Closing prices remain
   evaluation-only.

7. **Partial archives blocked retries.** Capture writes all files and metadata
   in staging before publishing the immutable directory. A failed capture can
   retry the same commit. Interrupted staging is ignored by archive readers and
   excluded from Git. The exactly-20-minute eligibility boundary now agrees
   between capture and grading.

8. **Scheduled forecasts lost their refreshed training inputs.** The publisher
   now commits validated domestic CSVs, UCL history and refresh metadata with
   forecast outputs before removing its temporary checkout. Odds response
   caches and BBS collection checkpoints remain under their own publication
   workflows. Existing concurrent-push retry behavior is preserved.

9. **Insufficient source visibility and regression enforcement.** New league
   diagnostics record the training origin and actual BBS result/statistics
   contribution, including conflicts and an explicit statement that statistics
   are not predictor features. Validation cache identity includes reviewed
   alias content. Coverage floors now also guard the four BBS modules.

## Verification and limits

- Canonical offline runner: **382 tests passed**.
- Pytest entry point: **389 passed**, including its additional collected cases.
- Application coverage: **88.35%**, with every required module floor passing.
- Model self-test, all CLI smoke checks, raw-output checks and diff checks pass.
- All six leagues refit successfully offline from the saved source revision;
  valid normalized score grids were generated for all 111 current fixtures.
- Targeted regressions cover reviewed identities, shared experiment clocks,
  malformed rows, invalid parameters, duplicate odds, cache rollback, atomic
  capture/retry, exact lead time and publication of training sources.

No BBS or odds API calls were made by this audit. Existing forecasts, archives,
reports, thresholds and experiment registries are not rewritten. New forecasts
and historical validation should be regenerated after merging because the model
clock and identity fixes can change probabilities. Software checks and successful
refits do not establish improved calibration, future win rate or profitability;
those require subsequent, chronologically valid evaluation. GitHub's Windows/
Linux matrix must pass before merge.
