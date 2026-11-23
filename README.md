# Football Value Pipeline

A Python-based football prediction and value-betting pipeline for forecasting match outcomes, goal markets, and shortlist-quality opportunities across major European competitions.

This project combines:

- Dixon–Coles-style recency-weighted match modelling
- live fixture and odds ingestion
- de-vigging and market blending
- historical validation and reliability checks
- readable output reports and shortlist generation
- performance tracking and audit snapshots

## Overview

The pipeline is designed to estimate probabilities for:

- 1X2 outcomes (Home/Draw/Away), double chance and draw no bet
- goal totals (Over/Under 1.5, 2.5 and 3.5)
- full-time Asian handicap lines, main and alternate
- three shortlists built from those: the value shortlist, the cagey tier and the master shortlist

Bets are placed at Pinnacle only (`shortlist_quote_policy.json`). The value
shortlist takes Pinnacle home and away wins, double chance 1X and X2 and Asian
handicap lines; draw no bet, double chance 12 and totals are excluded
([value rule](docs/team_research_profit.md)). The cagey tier excludes Over 1.5,
double chance 12 and both draw no bet markets (`cagey_correction_config.json`).

It is intended as a research and forecasting tool rather than a guaranteed betting system.

## Supported competitions

The ten leagues in `league_registry.py` (`python league_registry.py` lists them):

- EPL, La Liga, Bundesliga, Serie A, Ligue 1
- Eredivisie, Primeira Liga, Süper Lig
- UEFA Champions League (UCL) and UEFA Europa League (UEL)

## Key features

- Recency-weighted Dixon–Coles model
- Optional decay tuning for historical match weighting
- Live odds support via The Odds API and football-data.org fallbacks
- Historical validation for calibration and reliability
- Conservative shortlist filtering with strict/provisional tiers
- Export to raw machine-readable CSV/JSON files and human-readable reports
- Performance snapshots and weekly forward-evaluation summaries

## Repository structure

```text
.
├── football_value_pipeline_v2_standalone.py     # Main forecasting pipeline
├── format_football_output.py                    # Formats raw outputs into readable reports
├── football_value_requirements.txt              # Python dependencies
├── .env.example                                 # Example environment config
├── football_output_v2/
│   ├── raw/                                    # Raw predictions and shortlist data
│   ├── readable/                               # Human-readable outputs and reports
│   └── performance/                            # Forward-performance snapshots and summaries
├── tests/                                       # Automated tests
├── docs/                                        # Plan, rules and audits (docs/archive/: superseded docs)
├── assets/                                      # Supporting files
├── conservative_bet_filter.py                   # Conservative shortlist logic
├── goal_market_validation.py                    # Market validation checks
├── performance_tracking.py                      # Performance tracking utilities
├── publish_performance.py                       # Performance publication helper
└── README.md                                    # Project documentation
```

## Requirements

Python 3.10+ is recommended.

Install dependencies:

```bash
pip install -r football_value_requirements.txt
```

## Configuration

Local commands read credentials exclusively from the project `.env` beside the
pipeline script. Copy `.env.example`, then fill in your own keys:

```dotenv
THE_ODDS_API_KEY=your-primary-key
THE_ODDS_API_KEY_FALLBACK_1=
THE_ODDS_API_KEY_FALLBACK_2=
FOOTBALL_DATA_API_KEY=your-football-data-org-key
BBS_API_KEY=
API_FOOTBALL_KEY=
```

Never commit `.env`. Missing or blank file entries clear inherited shell API keys.
If deliberately using PowerShell or shell variables, add
`--api-key-source environment` to the prediction/collection/review command.
GitHub Actions explicitly uses environment mode and repository Secrets.

The default training window is **six domestic seasons and four UCL seasons**.
An explicit `--seasons-back N` overrides both; `--domestic-seasons-back N`
overrides domestic history separately.

Additional event-market coverage defaults to **all** eligible linked fixtures
inside the 24-hour shortlist window. It has no ranked 24-attempt cap. Use
`--additional-odds-coverage ranked` for that capped alternative, with reduced
market coverage. A logical attempt is not a provider-credit limit: markets,
regions, retries, failover and optional market-led research can add usage.

## Quick start

### Run the production forecast

This is the command the scheduled run uses (`publish_scheduled_forecasts.py`),
apart from `--api-key-source environment`, which GitHub Actions adds because it
reads keys from repository secrets rather than `.env`:

```powershell
python football_value_pipeline_v2_standalone.py --leagues EPL LaLiga Bundesliga SerieA Ligue1 UCL UEL Eredivisie PrimeiraLiga SuperLig --additional-odds-coverage all --no-legacy-comparison --research-free-sources
```

Do not add `--tune-half-life`: it replaces production's fixed 480-day half-life
with a tuned one, so the run is no longer the production model. The legacy
companion model, which nothing live reads, is fitted only with
`--legacy-comparison`; `--no-legacy-comparison` is still accepted and has no
effect.

### Run only a specific league

```powershell
python football_value_pipeline_v2_standalone.py --leagues EPL --additional-odds-coverage all --no-legacy-comparison --research-free-sources
```

### Format raw outputs into readable reports

```powershell
python workflow_checks.py raw
python format_football_output.py
```

## Complete prediction runs and tracking

Every successful prediction command saves a complete immutable bundle in
`football_output_v2/raw/prediction_runs/<run-id>/`. An atomic
`raw/current_run.json` pointer selects the current validated generation;
standard readers use that bundle. Top-level raw files remain compatibility
copies. Failed generation leaves the previous completed generation selected.

Push the raw directory, including **all run bundles**, before kickoff. One push
can carry several runs, and capture records each separately. Forward eligibility
still requires actual capture at least twenty minutes before kickoff; local
save times never backdate cloud evidence. Headline performance uses the latest
eligible archived selection per fixture; all eligible runs remain in shortlist_run_history.csv.

New value, cagey-tier and master shortlists use kickoffs from 20 minutes to
24 hours after the run. Archived generations retain their recorded horizons.
See the [value rule](docs/team_research_profit.md), [cagey-tier rule](docs/cagey-market-basis-v5.md)
and [master rule](docs/master-market-selection.md).

**Strong-team master release (23 Nov 2026).** The live `master_shortlist.csv` is
the strong-team master (`master_strong.py`, rule `master-strong-team-v1`; rows
carry `new_master_version` = `master-strong-team-v1-live-v11`): at most 6 picks
each in match result, double chance and Asian handicap, 15 matches, one pick per
match. "Proven" picks come first: the cagey tier rates the bet safe, the backed
team is stronger by Elo, it has a strong record on the exact bet over its last
10 matches, and the research model's expected margin agrees. They are ranked by
league trust, then the cagey chance of winning; today's fill rule completes the
list, labelled "not proven". The selection is in the usual `new_master_*`
columns, with the checks behind it in the `strong_*` columns. Today's master
(rule `master-new-fill-rule-v4`) keeps running in shadow as
`master_shortlist_new.csv`, the comparison and rollback baseline; the old master
(v9) is no longer written. Paul released it on 23 Nov 2026 as a deliberate
exception to the release gate (offline it showed no measurable difference from
today's master). The weekly report grades both and puts **ROLLBACK TRIGGERED**
at the top if strong minus today's master has its 95% interval entirely below
zero after at least 150 graded matches over at least 3 weeks. To roll back, set
`"live": "new"` in `master_shortlist_config.json`: every master file is then
written exactly as before this release. If the strong master fails during a
run, that run publishes today's master as `master_shortlist.csv` and its run
summary says **STRONG MASTER FAILED - TODAY'S MASTER PUBLISHED**.

**Master shortlist release (14 Nov 2026).** Under `"live": "new"`, the live `master_shortlist.csv` is
written by the new master rule (`master_reconciliation.py`, rule
`master-new-fill-rule-v4`: safe picks, then fill to 15 matches, only from the
value and cagey nominations, Pinnacle prices and quote-timing checks). Its rows
carry `new_master_version` = `master-new-fill-rule-v4-live-v10`, and the file
lists every nominated offer; the picks are the rows with `new_master_decision`
= `SHORTLISTED`. Its summary is `master_shortlist_summary.json` (also the
run summary's `master_shortlist`). The old master logic keeps running in
shadow as `master_shortlist_old.csv` (with `master_shortlist_old_audit.csv`
and the run summary's `master_shortlist_old`). Paul released it on 14 Nov 2026 as a
deliberate exception, without waiting for the live comparison verdict. The
weekly report (`performance/price_edge_v27/report.md`) grades both lists. It
puts **ROLLBACK TRIGGERED** at the top, and in the run summary, if new minus
old flat-stake return per bet has its 95% interval entirely below zero after at
least 150 graded matches over at least 3 weeks. Nothing switches
automatically. To roll back, set `"live": "old"` in
`master_shortlist_config.json`: every master file is then written exactly as
before the release (old master in `master_shortlist.csv`, new master in shadow
as `master_shortlist_new.csv`). Staking, the recommendation history and the
performance workbook never read a master list.

In the live file, `in_old_master`, `old_master_rank` and
`old_master_same_offer` (and the summary's `overlap_with_old_master`) compare
each offer with the old master. If the new master fails during a run, that
run publishes the old master as `master_shortlist.csv` (exactly as with
`"live": "old"`) and its run summary says **NEW MASTER FAILED - OLD MASTER
PUBLISHED** with the error. If the old master (shadow) fails, the new master
stays live and the run is recorded as having no comparison baseline. The weekly
report and the reports check count both kinds of run ("comparison baseline
missing" is never shown as an ordinary wait for data). Graded picks:
`performance/price_edge_v27/master_shortlist_picks.csv` is the new master and
`master_shortlist_old_picks.csv` the old master logic, both across the
release. Each pick flagged "research strongly disagrees" shows, in its row
(`inspection_*` columns) and in the "For inspection" section, what the
disagreement is about: both views' expected goals, home/draw/away chances and
likely scores, both no-loss chances, the main driver with its form and
history, warnings and the historical record of comparable bets
(`master_inspection.py`; reporting only, it never changes a pick).

Closing collection runs in GitHub Actions; the PC can be off. Its primary
closing analysis now uses the latest-selection ROI cohort, with a separate
first-entry reference. Existing experimental first-entry baselines are preserved.
See [run integrity and recovery](docs/prediction-run-integrity.md).

## What the scheduled run does

`publish_scheduled_forecasts.py` (the Scheduled forecasts workflow) runs, on
fresh `main`:

1. **Generate**: `football_value_pipeline_v2_standalone.py --leagues <all
   registry leagues> --additional-odds-coverage all --api-key-source environment
   --no-legacy-comparison`. Per league it fits the production model
   (`dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2`) and writes
   its probabilities. Across leagues it writes:
   - the v28 value-tier shortlist (`conservative_bet_shortlist.csv`) and the
     separate cagey tier (`cagey_tier_shortlist.csv`) ([rules](docs/cagey-correction-v28.md);
     v27 base rules in [docs/price-edge-shortlist-v27.md](docs/price-edge-shortlist-v27.md);
     what its probability columns mean: [docs/cagey-market-basis-v5.md](docs/cagey-market-basis-v5.md#probability-columns-on-cagey_tier_shortlistcsv));
   - `cagey_correction_monitoring.csv`: one correction record per fixture, from
     the correction the shortlist already computed;
   - `price_edge_tagged_candidates.csv`.

   It no longer runs goal-market walk-forward or count-market validation,
   because v28 selection does not read them (`--goal-market-validation` runs
   them on request; a policy that needs them still runs them and fails closed
   without them). It no longer runs the legacy companion or its half-life
   tuning, because their only readers were archived trials. A manual run with
   `--legacy-comparison` still produces them for offline replay. It no longer
   writes `bet365_vs_pinnacle.csv`: requests are Pinnacle-only, so the list was
   always empty (archived runs keep theirs).
2. **Check and format**: `workflow_checks.py raw` replays the shortlist, the
   cagey tier and the monitoring records deterministically, then
   `format_football_output.py` writes the readable outputs.
3. **Capture**: `performance_tracking.py capture` archives the forecast, the
   shortlist and these sidecars, each only when bound to the same generation:
   `price_edge_tagged_candidates.csv`,
   `cagey_tier_shortlist.csv` and `cagey_correction_monitoring.csv`.
4. **Review**: `performance_tracking.py review` grades results and refreshes:
   - performance tracking and the BBS forward assessment. The dashboard
     (`performance/README.md`), the weekly files and the price-edge report
     lead with closing-line value (`clv_report.py`) and give returns second,
     per pick and with one row per fixture, a match's picks averaged
     (`performance/fixture_grades.csv`);
   - the closing-odds review and the CLV report;
   - v27/v28 price-edge tracking, including both tiers and the Correction
     monitoring section;
   - pipeline health.

The provider requests are unchanged: the removed steps use only committed
history, and monitoring reuses the run's own quotes.

Separate workflows collect closing odds (value-tier and cagey-tier picks, exact
AH lines) and refresh training data. Offline only,
never scheduled: `ah_close_backtest.py`, `price_edge_backtest.py`,
`market_implied_calibration.py` and `historical_benchmark.py`.

**Retired (2026-11-02).** These experiments are no longer generated, captured or
reviewed: goal blend, market-led, recency, model reliability, shortlist weight,
shortlist policy, filter sensitivity and the legacy model comparison. The
benchmark-forward and totals-anchor trials followed on 2026-11-03. Their code
is in `archive/`, importable for replay; their last reports under
`football_output_v2/performance/` are frozen and marked ARCHIVED. Archived
snapshots still load and verify.

## History

The archived v22 shortlist was capped at twelve distinct matches within 48 hours.
Policy v22 allows Home win, Away win, Over 1.5, Double Chance 1X/X2/12 and
full-time Asian goal handicaps from Pinnacle/bet365, with 1xBet as an exact-market fallback. Every
shortlisted market requires adjusted estimated EV >=1% and unblended EV >=0.
Every market must also have an adjusted no-loss probability of at least 75%
(conservative loss estimate at most 25%). This common cutoff replaces the old
market-specific probability floors. Zero risk tolerance selects the lowest
conservative loss estimate per match; adjusted EV, unblended EV and refund
probability break equal-risk ties. The 75% cutoff is a user-selected policy
setting, not an empirically optimized threshold. Selected fixture representatives
are ordered by loss risk for the twelve-match cap.
Draw, BTTS and Under 3.5 are excluded under v22. The readable CSV and
Markdown report show a qualifying alternative per match, preferring another
market type, with price, loss risk, refund chance and both EV estimates. Alternatives
are informational and never create extra selections. Failed gates are never used to fill
twelve matches. Refunds and half settlements are graded explicitly; estimates
are not guarantees. See [Asian handicap rules, coverage and quote input](docs/asian-handicap-shortlist.md).

Since 8 Nov 2026 the shortlists use Pinnacle only; bet365 and 1xBet are no
longer quote sources.

## Output formats

The project writes both machine-readable and narrative outputs.

### Raw outputs

Located under `football_output_v2/raw/`:

- `<league>_predictions.csv`
- `<league>_scorelines.json`
- `<league>_diagnostics.json`
- `conservative_bet_shortlist.csv`
- `conservative_bet_summary.json`
- `stake_recommendations.csv` — advisory quarter-Kelly stakes for STRICT
  selections (2.5% per-bet cap, 10% slate cap; `--stake-*` flags)
- `cagey_tier_stake_recommendations.csv` — separate cagey-list advisory plan;
  both plans label the required matrix source ([source rules](docs/cagey-correction-v28.md))
- `shortlist_history/`

Prediction rows also carry informational venue-aware Elo columns
(`elo_home_rating`, `elo_away_rating`, `elo_rating_diff`,
`elo_home_expectancy`) that do not change probabilities.

### Readable outputs

Located under `football_output_v2/readable/`:

- `<league>_report.md`
- `<league>_predictions_readable.csv`
- `<league>_scorelines_readable.csv`

The league files show the two models the shortlists use, side by side: research (the value
shortlist's model, v5 domestic, v6 UCL/UEL) and cagey (the cagey tier's Pinnacle market view,
D_pow2 domestic, D UCL/UEL), the lists each fixture is on, and the master's verdict on every
Pinnacle offer (no-loss from both views, gap, label, cagey tier). The production model (70%
Pinnacle blend) appears only as a labelled benchmark at the end. Display only
(`readable_views.py`; terms in `football_output_v2/readable/README.md`).
- `conservative_bet_shortlist_report.md`
- `conservative_bet_shortlist_readable.csv`

## Recommended usage

For a local run that matches production, use the scheduled command and then
check and format its outputs:

```powershell
python football_value_pipeline_v2_standalone.py --leagues EPL LaLiga Bundesliga SerieA Ligue1 UCL UEL Eredivisie PrimeiraLiga SuperLig --additional-odds-coverage all --no-legacy-comparison --research-free-sources
python workflow_checks.py raw
python format_football_output.py
```

`docs/plan.md` holds the current plan, the release rules and the decisions
already made.

## Testing

The repository includes automated tests for validation, shortlist filtering, and output handling.

Example:

```bash
pytest -q
```

## Important notes

- This is a research and modelling project, not a guaranteed profit system.
- bookmaker odds, model probabilities, and EV estimates should be treated as estimates.
- Historical validation can help detect overconfidence and calibration issues, but it is not proof of future edge.
- Always keep API credentials out of committed source files.

## Documentation

Additional reference documents in this repo include:

- `docs/plan.md` — current plan, release rules and decisions
- `docs/architecture.md` — module layers, run flow, staking/Elo/Monte Carlo
- `football_output_v2/readable/README.md` — readable output explanation
- `docs/audit/simplification-2026-11.md` — the November 2026 simplification audit
- `docs/archive/` — superseded docs kept for history (`football_value_V2_README.md`,
  `PIPELINE_AUDIT.md`, `DATABASE_DESIGN.md`)

## License

No explicit license file is present in the repository metadata, so licensing terms should be confirmed before redistribution or commercial reuse.

## Contact / ownership

This repository is maintained under the GitHub user `paulmaina` and is described as a football prediction model project.

## Workflow verification

Every workflow runs Python 3.14. Pipeline CI tests Python 3.14 on Linux and Windows, enforces application and critical-module coverage floors, and exercises the six-league prediction/experiment/format/capture/review path offline. Forward review validates immutable archives and independently reconciles generated reports before publishing, retains failure diagnostics, and reports provider health, training dates and policy groups. Windows LF/CRLF conversion no longer silently excludes experimental sidecars.

See [Workflow checks and evidence](docs/workflow-assurance.md) for controls, artifacts, local commands and limitations. Historical snapshots, including retired experiments' sidecars, are preserved.
# Daily evidence and execution checks

See [daily data health and forward evidence](docs/daily-evidence.md) for UCL
automatic refresh, production quote eligibility and costs, and the new
performance report health history. Forecasting commands must drop the retired experiment flags
(`--goal-blend-experiment`, `--market-led-experiment`, `--recency-experiment`, `--reliability-experiment`),
which are now rejected; see [What the scheduled run does](#what-the-scheduled-run-does).

The [recency-weighting](docs/recency-experiment.md) and [EV sensitivity](docs/filter-sensitivity-experiment.md) experiments are retired; see [What the scheduled run does](#what-the-scheduled-run-does).

A separate [historical benchmark](docs/historical-benchmark.md) compares regularisation, recency, market weighting and totals anchoring on pinned data. Run `py historical_benchmark.py --materialize-pinned-data`; production commands and settings are unchanged. Future trial gates are recorded in `benchmark_promotion_rules.json`.

The [benchmark forward bridge](docs/benchmark-forward-automation.md) (archived 2026-11-03) captured a frozen 85% market-weight candidate and reported review readiness. Daily scheduled forecast collection requires Odds API keys in GitHub Secrets; local `.env` files are not available to Actions. GitHub issues request review once evidence gates are reached; production changes require approval.

GitHub Actions closing quote collection and the separate Pinnacle totals trial: [setup, Windows-task migration and evidence limits](docs/closing-odds-and-totals-trial.md). Normal forecasts generate the totals sidecar automatically; closing collection reuses the existing Odds API repository secrets and publishes observations back to the repository.

## Supplementary API-Football collection

API-Football can add cached, validated results, fixtures and lagged statistics
alongside existing providers. Configure the optional `API_FOOTBALL_KEY` repository
secret for the free-plan collector, which defaults to historical seasons 2022–2024.
Current-season data continues through existing providers. See [setup, limits and model eligibility](docs/api-football-integration.md).

The BBS and API-Football collectors use the full provider allowance for due data,
with no default local request budgets or reserved calls. Provider cooldowns and
cache freshness still apply. football-data.org already has no local request budget.
