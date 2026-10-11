# Football Value Pipeline V2

## Consolidated Excel performance report

The single readable performance report is
`football_output_v2/readable/football_performance_report.xlsx`.
The daily forward-performance workflow rebuilds and commits it after
results verification. `py format_football_output.py` also refreshes it
from the existing graded files. To refresh only this workbook locally:

```powershell
py performance_excel.py
```

The workbook contains a dashboard with native Excel charts, an editable
flat-stake ROI plan and cumulative-profit ledger, breakdowns by tier,
league, market, ISO calendar week and selection policy, calibration bins,
and the complete selection/fixture evidence. The default simulation uses
100 starting bankroll units and one unit per separate selection. These
are editable simulation inputs, not real account balances or a staking
recommendation. The simulation does not stop when the balance is exhausted.
Local assumption edits are replaced by the defaults on the next report
refresh. ROI is net profit divided by stake on settled selections with
valid recorded pre-match decimal odds. Missing prices do not create profit.
Win rate is wins divided by all settled selections, independently of odds
coverage. Pending or unverified results never enter either denominator.
No settled evidence means unavailable win rate, ROI and calibration, not 0%.

Review notes highlight small samples, overconfidence and negative simulated
ROI for investigation on a future holdout. Thirty scored samples is an
exploratory review prompt, not proof of a bookmaker edge. The workbook
does not change model parameters automatically. New snapshots record
`selection_policy_version`; older archives remain `legacy/unspecified`
unless their saved summary identifies a policy. Compare policies separately
when evaluating the 72-hour/UCL shortlist change. Brier scores use the same
reliability-adjusted probability shown in the selection report.

The Python exporter fills a bundled native Excel template using the standard
library. No additional Windows or GitHub Actions dependencies are needed.
The original CSV/JSON records and immutable archives remain the audit inputs.

V2 is a multi-league football probability and value pipeline built around a recency-weighted Dixon-Coles score model.

## Recommended daily-use model (single configuration)

**Use this command for the next several weeks.** It runs one consistent
Dixon-Coles model, with a **fixed 50% Dixon-Coles / 50% de-vigged
bookmaker 1X2 blend**, and tunes each competition's historical recency
half-life. You choose only the competitions and whether to tune decay:

```powershell
python football_value_pipeline_v2_standalone.py --leagues EPL LaLiga Bundesliga SerieA Ligue1 UCL --tune-half-life
```

- The market blend is **0.50 by default**; do not pass `--market-weight`
  or `--auto-market-weight` in normal use. Keeping a single fixed rule
  avoids changing the model definition between prediction runs.
- Dixon-Coles uses historical match results; the market contribution uses
  a coherent de-vigged live 1X2 bookmaker snapshot. Without complete
  bookmaker 1X2 odds, that fixture remains a pure Dixon-Coles prediction.
- Historical audit results indicated that a fixed 0.50 blend improved 1X2
  log loss over pure Dixon-Coles in all five **domestic** league audit
  samples. This was a retrospective comparison, not an untouched final
  test; it does **not** prove better exact-score or betting performance.
  **UCL has no usable historical opening-odds audit yet**, so its 50%
  blend is an unvalidated extrapolation.
- The CSV includes final `p_home/p_draw/p_away` and retained raw
  `raw_p_home/raw_p_draw/raw_p_away`, plus `raw_ev_*`
  and `raw_edge_prob_*` for independent model-signal auditing.
- Send back actual match results alongside saved forecast CSVs after a few
  matchweeks to measure accuracy, calibration, and whether betting edges
  are meaningful. Do not use ROI from only a handful of bets as evidence
  of predictive improvement.

The automatic weight tuner remains in the codebase for future research,
but is **not part of the recommended daily-use model**.

## Reliability validation and balanced live goal-market odds

The normal command remains **unchanged**. The pipeline now uses the
following data-driven quality controls while leaving its 50/50
Dixon-Coles prediction engine unchanged:

1. **Fair extra-market API allocation**. The maximum **24**
   per-event `alternate_totals,btts` bookmaker requests are reserved
   across the competitions requested for a run. With all six
   competitions, quotas are **4 each**, including UCL. Within each league, fixtures with the strongest
   qualifying *existing model probabilities* are checked first, rather
   than first-encountered chronological fixture order. UCL shares
   the same global 24-call budget. A league without qualifying events may
   leave its reservation unused; the pipeline never silently exceeds
   the global 24-call budget. These event requests consume API quota.

2. **Historical walk-forward validation** for *Home win, Away win,
   Over 1.5, Under 3.5 and BTTS Yes*. For each requested competition, including UCL,
   the existing match-history walk-forward predictor fits only on
   matches preceding each prediction window. Actual full-time
   results label each requested market (including true BTTS Yes).
   Earlier chronological development matches estimate a
   conservative correction for model overconfidence. Later
   chronological audit matches report sample sizes, probability
   reliability bins, Brier scores, binary log loss and observed rates.
   A predeclared audit quality gate (minimum sample, calibration bias,
   and Brier relative to an audit base rate) must pass before a market
   can be considered in the production shortlist. The audit period
   never fits the overconfidence correction.

   The reliability module now also evaluates **cumulative >=75% and
   >=85% forecast groups separately**. Each group reports development
   and later audit sample counts, observed hit rate, model mean
   probability, Brier, log loss, positive overconfidence and a Wilson
   95% interval for the observed rate. A group requires at least **30
   development and 12 audit predictions** and cannot overstate the
   observed audit success rate by more than **10 percentage points**.
   Markets with too little subgroup history are rejected for that
   probability tier, not silently called reliable. The overall audit
   Brier tolerance versus its hindsight base-rate comparator is
   tightened from +0.03 to **+0.005**; this is only a conservative
   diagnostic, not proof of predictive superiority. Confidence
   penalties come exclusively from development history. All
   old validation reports are automatically regenerated with
   `validator_version=2` on the next run.

3. **Reliability-aware shortlist ranking**. The filter uses the
   development-adjusted conservative probability to calculate
   `conservative_estimated_ev`, enforce the existing minimums
   and rank candidate markets. The raw model probability/EV remain
   available. Only fixtures kicking off between 20 minutes and
   **72 hours after the run time** are eligible. This is a hard cutoff
   for STRICT and PROVISIONAL rows; stronger distant fixtures cannot
   override it. The selection never forces ten matches or combines
   several markets from one game.

   With at least 75% predicted probability, the filter requires a
   passing **>=75% historical forecast group**. At 85% or higher,
   it requires a separate **>=85% group**, even if the broader group
   passed. Missing subgroup samples or excess audit overconfidence
   cause rejection, not automatic relaxation. The output reports
   `high_confidence_tier`, `high_confidence_status`, subgroup
   audit count, observed success rate and Wilson interval. The
   conservative probability also uses the greater of the overall
   and development-only subgroup overconfidence penalties.

The new `<league>_goal_market_validation.json` reports are written
under `football_output_v2/raw/`. Repeated runs reuse an existing
report when its model configuration and training cutoff have not
changed; `--force-refresh` forces recomputation. Recalculation can
add substantial CPU time because each league must run extra
historical model fits. In the final CSV/Markdown shortlist reports,
the **reliability-adjusted chance and conservative estimated EV**
are displayed separately from unadjusted model estimates.

**Price-data limitation:** The currently committed historical
Football-Data.co.uk CSVs contain completed match scores and some
1X2/Over 2.5 prices, but **not the actual opening Over 1.5,
Under 3.5 or BTTS Yes prices**. Thus we can honestly validate these
markets' probability accuracy and calibration, but historical
betting profitability for the three added markets is
`UNAVAILABLE_NO_HISTORICAL_PRICES`, not a simulated positive ROI.
If future historical files contain same-book paired opening odds for
those exact markets, the validator can calculate exploratory
flat-unit settled returns without inventing prices. These
simulations are not a guarantee of future returns.

The development/audit historical periods can overlap the period
previously used to tune the half-life parameter, so the audit is
**not completely untouched**. Conservative safety gates are not
proof that a market has a true bookmaker edge. Always collect
timestamped predictions and final scores for future evaluation.

## Automatic forward-only gameweek performance evaluation

A separate, **non-model-changing** GitHub Actions workflow is in
`.github/workflows/forward-performance.yml`. Once merged, it:

1. **Captures immutable forecasts on each commit to `main` that changes
   the tracked raw model CSV, shortlist CSV or shortlist summary JSON.**
   Archives are written under
   `football_output_v2/performance/snapshots/<commit-prefix>/`.
   It snapshots the combined model predictions, the shortlisted
   STRICT/PROVISIONAL selections, and the original summary, with a
   capture UTC timestamp and SHA-256 integrity checks. It never
   overwrites earlier snapshots. A capture must occur at least **20
   minutes before kickoff** for each fixture to be eligible.
2. Runs **daily at approximately 07:30 UTC / 10:30 EAT**, including
   midweek European fixtures, plus optional manual runs from
   GitHub Actions → **Forward performance review → Run workflow**.
   The schedule is best effort, subject to GitHub Actions scheduling
   delays. It checks recent completed fixtures for both the full
   prediction set and the separately shortlisted selection markets.
3. Uses the official **football-data.org v4** final score endpoint
   with `FOOTBALL_DATA_API_KEY`, scoped by actual competition code
   (PL, PD, BL1, SA, FL1, CL). Scores are considered verified only
   for `FINISHED` fixtures whose **home/away names, competition
   and kickoff** match unambiguously. Regulation-time scores are
   used for extra-time/penalty cup ties; a missing 90-minute score,
   postponed game, missing subscription permission, ambiguous name,
   or missing fixture is **not** graded as a win/loss.
4. Produces `performance/shortlist_grades.csv` and
   `performance/prediction_grades.csv` with original snapshot IDs,
   source match IDs, verified final scores and results. It writes
   `performance/metrics.json`, a cumulative
   `performance/README.md` (overall, by STRICT/PROVISIONAL,
   league, market, and gameweek), and
   `performance/weekly/YYYY-Www.md` gameweek breakdowns.
   A `verified_results.json` cache records authenticated final scores
   and any subsequent revisions.

**One-time GitHub setup required:** Set the Actions repository secret
`FOOTBALL_DATA_API_KEY` through
GitHub → Settings → Secrets and variables → Actions → New repository
secret. **Don't put your API key in a committed file.** The token
must permit `/v4/competitions/{code}/matches` for the desired
competitions. Provider-free-tier restrictions can prevent scores for
some leagues. If the token is unavailable or permission is denied,
the action flags this in `performance/README.md` and leaves the
affected fixtures **ungraded**; it does not invent scorelines.
Football-data.org free registered access is subject to an API
request-rate limit; the workflow currently makes one modest request
per relevant league each daily run.

**How to activate tracking:** After this feature is merged,
run your usual forecasting command **before kickoff** and commit the
updated three raw inputs to `main`. Merely installing the evaluator
does **not** retroactively establish proof that previous forecast
files existed before a fixture started. The first new data commit
will trigger snapshot capture and an initial review. You can also
run a manual action with `capture_current_snapshot=true`, but it
records the *actual current capture time* and excludes any fixtures
already underway.

All selections are **deduplicated by competition, teams and match date
across snapshots**. The **first eligible** committed forecast for
each fixture is scored, never an arbitrarily chosen post-match or
more favorable later prediction. Grading is by the specific selected
market, using equal one-unit **simulated** stakes where genuine
pre-match bookmaker odds are present. Unsettled games are excluded
from graded accuracy/ROI denominators. Full-fixture 1X2 Brier scores
are reported separately. No training weights, betting thresholds,
or selection tiers are changed by the evaluation.

## Under 3.5 in predictions output

The model already computes `p_under_3_5` as the probability of **at
most three total goals (0, 1, 2 or 3)**. The raw
`football_output_v2/raw/*_predictions.csv` files already include it.
After running `python format_football_output.py`, each
`football_output_v2/readable/<league>_predictions_readable.csv`
includes a dedicated **Under 3.5** percentage column, immediately
after **Over 3.5**, followed by **BTTS Yes** and **BTTS No** model
probabilities after the Under 4.5 column. Each per-fixture readable
Markdown report also summarizes Under 3.5, BTTS Yes and BTTS No
alongside the existing goals metrics. BTTS Yes means **both teams
score at least once**; BTTS No means **at least one team scores zero**.
These are presentation changes only: **no re-fitting, new
bookmaker requests, or changed thresholds**.

## Ten candidates: strict qualifiers and transparent near-misses

The run now produces **up to 10 distinct match/market candidates**,
without changing the single 50/50 forecasting model or its CLI. The
top candidates are separated into two **qualification tiers**:

- **STRICT**: passed every existing market-specific, price, team, EV and
  historical audit rule. These remain estimates, not guaranteed wins.
- **PROVISIONAL**: *failed at least one strict requirement*. These are
  **research-only WATCHLIST entries, not verified bets**. They may be
  included only when fewer than ten STRICT fixtures exist, and only
  if all non-negotiable market-data rules still pass.

The provisional fallback is restricted to **near historical misses**:
an underpopulated >=75% or >=85% historical tier with at least **3
development and 2 audit outcomes**, modest tier overconfidence (at
most 15 percentage points, explicitly marked), or an
**adjusted EV of at least +1.5%** and/or adjusted win probability
at most **1.5 percentage points below** its strict minimum. These
are *watchlist-only tolerances*, not claims that the failing markets
have predictive or betting value. Markets that fail the overall
audit, whose raw independent Dixon–Coles EV is negative, have
insufficiently matched teams, stale quotes, unknown odds,
or a malformed reference market are **never backfilled**.
Watchlist ranking emphasizes closeness to the historic gate before
model probability; one market per fixture is enforced globally.

A separate `football_output_v2/raw/conservative_strict_qualifiers.csv`
contains **only** rows that passed all strict requirements. It is never
filled with watchlist candidates.

The files `conservative_bet_shortlist.csv` and
`conservative_bet_shortlist_readable.csv` now carry
`selection_tier` / `Qualification`, `near_miss_reason`, and
`historical_gap_score`. `conservative_bet_summary.json` reports
`n_strict_qualified` versus `n_provisional_watchlist` and, when
ten is reached with watchlist entries, `TARGET_WITH_PROVISIONAL`
rather than falsely claiming ten fully qualified picks. The readable
Markdown report displays the strict/watchlist breakdown.
Earlier releases used four-day preference fields. New runs use a hard
72-hour horizon and emit `selected_matches_within_72_hours` instead.

**Live bookmaker quality repair (v2.7):** Complete 1X2 and goal-market
reference odds must imply a sane total inverse-odds sum
(overround) between **0.98 and 1.20**. Corrupt most-recent
bookmakers are ignored when choosing the reference and **cannot
contribute best odds**. The pipeline uses the newest remaining valid
book or rejects the market if no valid reference exists. This
specifically prevents the previously observed 1.10/1.10/1.10
Ligue 1 Betfair quotes from contaminating the bookmaker blend.
The margin range is a heuristic integrity guard, not proof the
resulting model is calibrated.

**Do not place a ten-leg accumulator based on these lists.**
Even ten truly strict single-match predictions would have a lower
combined all-correct probability than any individual pick.
Provisional rows, by definition, failed validation. Fewer than ten
rows remains possible if honest, valid candidates are unavailable.

## Ten-match, five-market shortlist (experimental; graded qualification)

Running the existing command (no extra flags) now also produces a
**target of ten distinct match candidates per run**, with at most one
market selected from each football match:

```powershell
python football_value_pipeline_v2_standalone.py --leagues EPL LaLiga Bundesliga SerieA Ligue1 UCL --tune-half-life
```

Markets evaluated: **Home win, Away win, Over 1.5, Under 3.5,
Both Teams to Score — Yes**. UCL is eligible using its own Champions
League walk-forward reliability report and the same qualification gates.
Missing/insufficient/unreliable UCL evidence does not become STRICT.
Historical UCL opening bookmaker prices are still unavailable; its blend
and simulated profitability require forward evidence, not claims of
historically validated betting returns.

Outputs remain in `football_output_v2/raw/`:

- `conservative_bet_shortlist.csv`: up to ten distinct fixtures,
  **the selected market and STRICT/PROVISIONAL qualification tier**
  beside each match. STRICT selections rank by calibrated forecast
  probability; provisional gaps rank by distance from strict gates.
  All shortlisted kickoffs must be within the **next 72 hours of the run**,
  with the existing minimum 20-minute lead. The 72-hour endpoint is
  inclusive. If fewer than ten qualify, the shortlist stays below target.
- `conservative_bet_rejections.csv`: five decisions per fixture,
  including rejected/alternate markets and the reasons.
- `conservative_bet_summary.json`: `TARGET_MET`, `BELOW_TARGET`
  or `NO BET`, with the shortfall to ten, actual selected
  kickoff span, `shortlist_lookahead_hours`, UTC window boundaries, and
  `selected_matches_within_72_hours`. The old four-day preference fields
  are no longer emitted for new runs.
- `shortlist_history/conservative_decisions_<timestamp>.csv`:
  immutable dated audit snapshots for later feedback.

### Readable shortlist

After the normal pipeline run, format all raw predictions **and** the
shortlist using the same formatter command:

```powershell
python format_football_output.py
```

The new files are:

- `football_output_v2/readable/conservative_bet_shortlist_readable.csv`
  — each match with its explicit **Shortlisted market**, kickoff UTC,
  model chance, **reliability-adjusted chance**, unblended DC chance,
  bookmaker odds, headline estimated EV and **conservative estimated EV**.
- `football_output_v2/readable/conservative_bet_shortlist_report.md`
  — a readable market-by-match table, 72-hour eligibility window, and
  selection risk notes. If there are no qualifying candidates, the
  report clearly says so.

The formatter does **not** choose or revise candidate markets and
never changes the raw shortlist.

**Ten is a visible candidate target: STRICT rules are never relaxed,
and PROVISIONAL rows are prominently marked watchlist-only.** No
market gets picked without a verified bookmaker price. If fewer than
ten qualifying matches are available, the result is short with
`BELOW_TARGET` or `NO BET`. Multiple markets on the same football
fixture are not counted as different picks. A selection report is not
an automatically placed multi-leg betslip.

The default model remains fixed 50/50 Dixon-Coles / de-vigged
bookmaker 1X2. Specific threshold gates:

| Market | Blended probability at least | Raw DC probability at least |
| --- | ---: | ---: |
| Home win | 65% | 50%, with DC also favoring home over draw and away |
| Away win | 65% | 50%, with DC also favoring away over draw and home |
| Over 1.5 | 78% | 72% |
| Under 3.5 | 76% | 70% |
| BTTS Yes | 70% | 63% |

**STRICT** candidates must have estimated positive EV **at least +3%**
at an actual bookmaker quote and **non-negative unblended DC EV**,
team-name matching confidence **at least 90** for both teams,
a valid 50/50 blended market and current future UTC kickoff at least
20 minutes away. Quote timestamp must be no more than 24 hours old.

For 1X2, at least two complete reference bookmakers are required.
For alternate totals and BTTS Yes, one verified bookmaker with both
complementary outcomes is sufficient. The market's own coherent
quote pair (not unrelated line or h2h quotes) must be available.

**Additional The Odds API quota cost:** The 24 extra event calls
are reserved fairly across the requested competitions, including UCL
and prioritized within leagues. Extra-market coverage may still be
missing at specific bookmakers and prices are never fabricated.

**Risk and interpretation:** These thresholds are provisional
heuristics, not backtested thresholds with proven bookmaker edge.
A claimed +3% estimated EV can disappear with probability error,
odds movement or bookmaker limits. An ten-leg accumulator is
particularly fragile: all eight selections must win to pay out.
Track real-world outcomes for several weeks before considering
stakes or a higher selection target. No guaranteed or perfect
betslip exists.

## Current data architecture

The pipeline separates historical modelling data, current fixtures, and live market odds.

- **Historical results and historical bookmaker columns:** Football-Data.co.uk season CSVs.
- **Preferred current fixtures:** The Odds API v4 `/events` endpoint when `THE_ODDS_API_KEY` is configured.
- **Preferred current odds:** The Odds API v4 `/odds` endpoint using `h2h` (1X2) and `totals` (O/U).
- **Optional fixture fallback:** football-data.org v4 when `FOOTBALL_DATA_API_KEY` is configured.
- **Last-resort fixture snapshot:** Football-Data.co.uk `fixtures.csv`.

The old FixtureDownload fallback was removed. If a trustworthy current endpoint cannot provide fixtures, the pipeline fails explicitly rather than silently producing predictions for a questionable schedule.

## Supported competitions

- EPL
- La Liga
- Bundesliga
- Serie A
- Ligue 1
- UEFA Champions League (UCL)

### Champions League modelling

UCL is intentionally handled differently from a domestic league.

Current UCL fixtures and odds use The Odds API sport key
`soccer_uefa_champs_league`. Model training uses completed UEFA Champions
League matches from football-data.org competition code `CL`.

This avoids fitting a Champions League prediction from unrelated domestic-league
ratings. A `FOOTBALL_DATA_API_KEY` is therefore required when `UCL` is
included. The free football-data.org tier includes Champions League fixtures and
results; access to older seasons can depend on the account/plan. The pipeline
uses all accessible requested seasons and requires at least 30 completed UCL
matches before fitting the Dixon-Coles model.

## Install

```bash
pip install -r football_value_requirements.txt
```

Optional reliability plots require matplotlib.

## Configure current fixtures and live odds

Do **not** commit API keys to GitHub. The pipeline reads them from environment variables.

PowerShell (primary credential and optional **provider-authorized** failovers):

```powershell
$env:THE_ODDS_API_KEY="your-primary-key"
$env:THE_ODDS_API_KEY_FALLBACK_1="your-secondary-key"
$env:THE_ODDS_API_KEY_FALLBACK_2="your-tertiary-key"
```

**No new CLI flags or changed model parameters.** Every current The Odds API
endpoint (fixtures `/events`, featured `/odds`, and the per-event
`alternate_totals,btts` endpoint) uses the existing cached HTTP client
with an ordered primary -> secondary -> tertiary retry:

- The environment variables are read **on every live request**, not
  baked into the program at startup. Empty and duplicate keys are skipped.
  A single primary key still works as before.
- A **429** triggers the next key promptly; unlike the generic historic
  HTTP client, The Odds API does not retry HTTP 429 several times
  with the same key before switching. The provider says 429 can be
  temporary, so this does not mark an account permanently exhausted.
- A **401 or 403** triggers the next key **only if the provider explicitly
  identifies `OUT_OF_USAGE_CREDITS`**. Invalid or deactivated keys,
  incorrect markets, networking failures and unrelated HTTP errors
  stop immediately with a concise error rather than consuming backup
  quotas or hiding configuration problems.
- When every configured credential returns quota/rate-limit errors, the
  request raises a clear `all configured keys` error. Warnings identify
  **variable names only**, never secret values or URLs containing
  `apiKey`. Successful results use the **existing TTL cache**;
  no failed quota response is cached.
- The per-run budget of **24 extra event-market requests** is unchanged.
  Fallover does not multiply, increase, or bypass this pipeline budget.

**Usage-policy note:** The provider's terms do not explicitly confirm
that pooling several free-tier accounts is permitted. Check with The
Odds API before relying on multiple account quotas. This credential
redundancy feature is intended only for credentials you are authorized
to use together.

Optional football-data.org fixture fallback:

```powershell
$env:FOOTBALL_DATA_API_KEY="your-key-here"
```

These variables apply to the current PowerShell session. Keep secrets in your local environment or a secret manager rather than in source files.

## Run the five domestic leagues

```powershell
python football_value_pipeline_v2_standalone.py --leagues EPL LaLiga Bundesliga SerieA Ligue1
```

Include Champions League:

```powershell
$env:THE_ODDS_API_KEY="your-odds-api-key"
$env:FOOTBALL_DATA_API_KEY="your-football-data-org-key"

python football_value_pipeline_v2_standalone.py --leagues EPL LaLiga Bundesliga SerieA Ligue1 UCL
```

UCL only:

```powershell
python football_value_pipeline_v2_standalone.py --leagues UCL
```

Raw model outputs are written by default to:

```text
football_output_v2/raw/
```

The run logs which fixture provider was used and how many fixtures received live odds.

## Odds behavior

For 1X2 and O/U 2.5 the pipeline keeps two concepts separate:

1. **Reference market** — one complete bookmaker market is used for de-vigging, so Home/Draw/Away probabilities are never constructed by mixing bookmakers.
2. **Best available price** — the highest returned price for each individual selection is used for EV.

Outputs include audit fields such as fixture source, fixture ID, odds source, odds-match method, latest odds timestamp, bookmaker counts, and the bookmaker offering each selected best price.

If a current fixture is available but no qualifying bookmaker market is returned, model probabilities remain available and the market/EV fields remain blank.

## API-credit usage

The Odds API charges current odds requests according to requested markets and regions. V2 requests two featured markets (`h2h,totals`). The local five-minute odds cache avoids spending more credits on immediate repeat runs.

Default region:

```powershell
python football_value_pipeline_v2_standalone.py --leagues EPL --odds-regions eu
```

Multiple regions can be comma-separated, but they increase API usage:

```powershell
python football_value_pipeline_v2_standalone.py --leagues EPL --odds-regions uk,eu
```

## Fixture-provider controls

Default:

```text
--fixture-provider auto
```

`auto` tries, in order:

1. The Odds API events endpoint (if any authorized `THE_ODDS_API_KEY*` variable is configured)
2. football-data.org (if `FOOTBALL_DATA_API_KEY` exists)
3. Football-Data.co.uk current fixture CSV for domestic leagues

For UCL, the third option is not used because Football-Data.co.uk does not provide
a UCL division CSV compatible with the domestic fixture loader.

You can force a provider for debugging:

```powershell
python football_value_pipeline_v2_standalone.py --leagues EPL --fixture-provider the-odds-api
```

To fetch fixtures without requesting live odds markets:

```powershell
python football_value_pipeline_v2_standalone.py --leagues EPL --no-live-odds
```

## Model

The score matrix remains the single probability engine:

- recency-weighted Dixon-Coles Poisson
- L2 regularisation
- expected home/away goals
- 1X2 probabilities and fair odds
- top 20 exact-score probabilities per fixture (the full score matrix is used internally, but only the 20 highest-probability scores are serialized)
- O/U 0.5, 1.5, 2.5, 3.5 and 4.5 probabilities

If `--market-weight > 0`, the Home/Draw/Away regions of the score matrix are reweighted toward a de-vigged market target. All downstream markets are then recalculated from the same matrix.

The **recommended default is `0.50`**, a single fixed blend chosen for an extended feedback period. Do not tune market weight on the same test set used for final evaluation.

## Dixon-Coles exponential time-decay tuning

The Dixon-Coles model already uses a low-score correction (rho) and a
recency-weighted likelihood. The default remains a **240-day half-life**.
Do **not** assume 240 days is universally optimal.

The blog's exponential decay coefficient (xi, in reciprocal days) is equivalent
to the pipeline's half-life parameter through:

```text
xi = ln(2) / half_life_days
weight(age_days) = exp(-xi * age_days)
```

You can now compare candidate half-lives using past-only, walk-forward match
result predictions (mean 1X2 log loss; lower is better):

```powershell
python football_value_pipeline_v2_standalone.py --leagues EPL --tune-half-life
```

Customize the candidate half-lives and evaluation window:

```powershell
python football_value_pipeline_v2_standalone.py `
  --leagues EPL LaLiga Bundesliga SerieA Ligue1 `
  --tune-half-life `
  --half-life-candidates 120 240 365 730 1000000000 `
  --tune-validation-days 365 `
  --tune-step-days 56 `
  --tune-min-train 250
```

`1000000000` days approximates no time decay (xi approximately zero).
Each candidate is fitted on results strictly **before** a validation block,
then scored on subsequent results. The optimization re-fits multiple models
per competition, so it is significantly slower than a normal run.

Outputs:

```text
football_output_v2/raw/EPL_decay_tuning.json
football_output_v2/raw/EPL_diagnostics.json
football_output_v2/raw/EPL_predictions.csv
```

The model automatically uses the selected half-life **for that competition
and current prediction run only**. Without `--tune-half-life`, existing
behavior is unchanged. The scoreline top-20 limit, live odds, fixture
providers and scoring matrix calculations are unaffected.

**Evaluation integrity:** the log-loss values used to choose the half-life are
*validation* scores, **not** independent test performance. To determine
whether tuning improves real accuracy, use a later untouched test period or
implement nested walk-forward evaluation. The CLI prevents combining
`--tune-half-life` and `--backtest` in one command because selecting
hyperparameters on the backtest period would introduce selection leakage.

The implementation follows David Sheehan's discussion of Dixon-Coles
time weighting and predictive profile likelihood:
https://dashee87.github.io/football/python/predicting-football-results-with-statistical-modelling-dixon-coles-and-time-weighting/

### Optimizer reliability

V2.2.2 calculates the exact gradient of the Dixon–Coles weighted
log-likelihood instead of asking SciPy to estimate a numerical gradient for
every attack/defence parameter. This is particularly important for UCL, which
includes more distinct clubs than most domestic competitions.

A failed or incomplete optimization is now **rejected** instead of being used
to select a half-life or to produce probability estimates. It is therefore
possible for a tuning run to fail explicitly if all candidate fits are invalid,
rather than returning misleading results.

For every competition, inspect:

- `*_decay_tuning.json`: candidate half-life, log loss, match counts and validity.
- `*_diagnostics.json`: `fit_success`, selected half-life, and optimizer information.

The large `1000000000`-day candidate approximates **no recency decay**,
not an error. It can be selected if it actually yields the best validation
log loss, but it is not proof of superior betting performance.

The self-test and automated unit tests cover the exact objective gradient,
high-dimensional synthetic fitting, and leak-free temporal validation.
Live provider calls and actual historical score validation remain separate
checks.

## Market-weight research (advanced, not part of daily use)

The optional `--auto-market-weight` research mode evaluates historical
opening-bookmaker probability blends by chronological development/audit
splits. It requires historical opening prices and can fall back to the
standard 0.50 weight when no suitable history is available. Results
are written to `<league>_market_weight_validation.json`.

This research helper remains available for a future dedicated experiment.
For now, **do not run it** in the daily-use model. Its historical audit
may overlap with half-life tuning, so it is not a final independent
assessment of prediction performance.

## Walk-forward backtest

```powershell
python football_value_pipeline_v2_standalone.py `
  --leagues EPL `
  --seasons-back 6 `
  --backtest `
  --test-start 2024-08-01 `
  --min-edge 0.05 `
  --kelly 0.25
```

Historical backtesting continues to use Football-Data.co.uk's historical opening/closing market columns; current live prices are not injected into historical matches.

## Self-test

```powershell
python football_value_pipeline_v2_standalone.py --self-test
```

The self-test checks probability normalization, matrix reweighting, and dedicated live-odds parsing, including the distinction between best prices and same-bookmaker reference markets.

## Database direction

See `DATABASE_DESIGN.md` for a proposed SQLite-first storage layer for HTTP cache, fixtures, odds snapshots, prediction runs and backtests. Database storage is intentionally separated from this live-odds change so source correctness can be validated before persistence is changed.


### Refreshing an older shortlist

Merging selection code does not regenerate committed CSVs. To re-rank existing
forecasts against the current UTC time and hard 72-hour cutoff, run:

```powershell
py refresh_conservative_shortlist.py
```

This refreshes raw and readable shortlist files, including rejection reasons.
It does not fetch fresh odds or add missing league forecasts. For fresh predictions
including UCL, set the required API keys and run:

```powershell
py football_value_pipeline_v2_standalone.py --leagues EPL LaLiga Bundesliga SerieA Ligue1 UCL --tune-half-life
py format_football_output.py
```

The shortlist is anchored to generation time, never the first fixture. Exactly
72 hours is included; later kickoffs are rejected even when they score higher.
STRICT candidates rank first by calibration-adjusted probability and EV;
PROVISIONAL candidates remain an explicitly labelled research watchlist.
UCL requires its own historical validation and qualifying pre-match odds.
Existing immutable performance archives retain their original selection policy.
