# Closing quotes in GitHub Actions and separate Pinnacle totals trial

Production probabilities, shortlist filters and bets remain unchanged. These additions collect evidence; neither promotes a candidate nor places bets. The closing collector uses the same Odds API repository secrets as scheduled forecasts.

## Daily forecast workflow

Continue your existing six-league command with the goal, market-led and recency flags. Every normal run also writes `raw/totals_anchor_experiment.json` automatically, using the Pinnacle O/U 2.5 pair already present in the normal odds response. This adds no odds request and no model fit. Push forecasts promptly before kickoff so the existing Actions workflow captures them with the usual 20-minute minimum lead.

The trial separately scales the fitted home/away goal intensities, retaining fitted Dixon-Coles rho and production 1X2 probabilities, to match the power-devigged Pinnacle Over 2.5 probability. It is the historical benchmark's proportional anchoring method, not a joint fit or an xG feature. Only complete, coherent Pinnacle quotes with market timestamps no more than ten minutes old qualify. Production must retain its registered 0.5 market weight, and its 1X2 reference must also be no more than ten minutes old, within five minutes of the totals quote. Missing quotes, unknown teams, matrix/parameter inconsistencies and solver failures remain explicit unavailable coverage. Domestic leagues only; UCL was absent from the historical nomination. First archived observations, including unavailable observations, are frozen; earlier forecasts are never backfilled.

Primary metric is Under 3.5 paired log loss, selected before forward collection. Under 3.5 remains excluded from the shortlist. Over 1.5, BTTS Yes and Over 2.5 are guardrails. Review requires 300 paired fixtures, six ISO gameweeks, >=80% verified in-scope coverage and no rejected snapshot evidence. Supportive forecasting evidence additionally requires a positive week-block bootstrap interval and no log-loss/Brier deterioration in any registered market. Readiness is not approval or proof of profitable betting. Versions cannot be pooled. The review queue, performance health and Excel health sheet show this trial alongside the others.

## Closing quotes run in GitHub Actions

After this change is merged, **Closing odds collection** runs automatically on
`main`. Your PC can be switched off. The prediction command does not change, and
you do not need to push after each kickoff: the workflow commits collected
evidence and updates closing reports itself. Forecasts still need to be pushed
early enough for their ordinary immutable pre-kickoff capture.

### One-time migration

1. Ensure at least one existing repository Actions secret is configured:
   `THE_ODDS_API_KEY`, `THE_ODDS_API_KEY_FALLBACK_1` or
   `THE_ODDS_API_KEY_FALLBACK_2`. These are the same names as scheduled forecasts;
   no new BBS or football-data.org key is needed for closing collection.
2. Existing unpushed closing observations must be committed and pushed using your normal workflow if you
   want them included in the shared record. Never commit `.env`.
3. Disable the old Windows task and close any manually started watcher:

   ```powershell
   Disable-ScheduledTask -TaskName FootballClosingOddsCollector
   Stop-ScheduledTask -TaskName FootballClosingOddsCollector -ErrorAction SilentlyContinue
   ```

   This computer cannot be controlled by a GitHub workflow. Do not run two
   collectors on separate copies: a local copy cannot see reservations until
   it pulls them and would spend from a stale allowance.
4. Merge the implementation, then `git pull` locally and check the
   **Closing odds collection** workflow in Actions. Its summary says
   whether secrets are missing, there are no approaching fixtures, or the daily
   allowance is exhausted. A manual **Run workflow** supports unusual kickoff
   times outside the automatic schedule.

If the repository applies a rule blocking automated direct pushes to `main`,
that rule must allow this publisher, as it does for existing forecast/data
publishers. A failed quota-reservation push causes zero provider requests.

### Schedule and timing

Lightweight checks run at UTC 08:52, then 09:07/22/37/52 through 21:52
(**11:52 EAT through 00:52 EAT the following day**). This covers kickoff slots
from 09:00 through 22:00 UTC, including every slot in the currently saved
six-league forecasts. Matches outside these times need a manual workflow run
within 18 minutes before kickoff. GitHub cron runs are best effort and can be
queued or dropped; no GitHub-only schedule guarantees an exact closing window.

The dependency-free gate examines current and archived fixture times. If nothing
is due within 18 minutes or credentials are missing, it skips Python setup and
dependency installation. Otherwise it checks latest `main` again, reserves quota,
then polls every 30 seconds. It accepts responses only within the existing
**six minutes before scheduled kickoff**, with bookmaker timestamps no more than
120 seconds old. It stops early when required quotes are complete, its allocation
is exhausted, or the planned last kickoff is reached. It does not extend the
collection window to rescue delayed runs; missing coverage remains missing.

This uses one Linux/Python 3.12 job, not a matrix or an all-day watcher. These checks
still consume Actions minutes: there are 53 scheduled checks per day, plus the
time spent in active collection windows. Review actual usage in GitHub billing;
this is not a promise to remain within the repository's free allowance. There is
no full test-suite run inside each scheduled collection.

### Requests, interruptions and publication

The UTC-day cap remains **100 logical fetch attempts**. A workflow reserves up to
three attempts per approaching fixture (at least ten slots, bounded by remaining
daily allowance) **in a commit on main before any provider call**. Each attempt is
checkpointed locally before fetching. On successful evidence publication, unused
slots are released. A hard-killed runner or failed publication leaves its whole
unsettled reservation charged, preventing later jobs from resetting unknown usage.
UTC rollover resets the next day's allowance. Do not manually erase an unsettled
reservation to retry it; first recover its checkpoint and observations from the
`closing-odds-recovery-<run>-<attempt>` Actions artifact, or wait for the next UTC day.

Request attempts are not provider credits: market counts, fallback credentials
and transport retries can consume more than one credit per logical fetch. Existing
quota failover remains in effect. The collector requests Pinnacle and 1xBet h2h
and O/U 2.5, adding alternate totals, BTTS and double chance when frozen/current
shortlists require them. A later forecast cannot hide an earlier frozen selection.
No stale response fallback is allowed. Errors record only exception types.

Publishing copies immutable observations into a fresh checkout of latest main,
settles only that run's reservation, preserves concurrent forecasts/training data,
and regenerates closing reports. Push races retry **publication**, never API
collection. Commits use `[skip ci]` to avoid rerunning the test matrix for quote
data. Workflow concurrency serializes closing collectors, while git push checks
protect against the other data workflows. No force pushes are used.

Content-addressed observations remain at
`football_output_v2/closing_odds/observations/`, with full provider payload,
response time, identities and market timestamps. `request_budget.json` records
actual usage plus unsettled reservations; `collector_status.json` records checks
and coverage. Reports remain at `football_output_v2/performance/closing_odds/`.
A later `git pull` brings these files to your machine. Failed runs attempt an
artifact upload of evidence/checkpoints only; caches, `.env` and keys are excluded.
A hard termination can still prevent artifact upload, but the committed allowance
continues to protect the next run.

### Evidence limits

These are **observed near-close quotes**, not guaranteed official final closing
odds. The clock belongs to the collector machine (now a GitHub runner); its
timestamps are not independent proof of the actual whistle time. Quotes arriving
after scheduled kickoff are rejected. Existing v1/v2/v3 observations remain valid.

The report distinguishes same-book offered-price CLV
(`entry / 1xBet closing offer - 1`) from fair-close EV
(`entry * devigged closing probability - 1 - per-stake cost`). Neither establishes
accepted execution or actual profit. Pinnacle double-chance fair probabilities
may use coherent devigged 1X2 sums; direct prices are never fabricated. Collection
does not alter production probabilities, thresholds, experiments or bets.

### Optional local collection

The local script remains available for explicit manual use with local `.env`
credentials, but leave the Windows task disabled after migrating:

```powershell
py closing_odds.py --watch --hours 1
```

Avoid running it while the Actions collector is enabled. The normal automated
path uses `--api-key-source environment`; local `.env` contents are never
uploaded to GitHub.
