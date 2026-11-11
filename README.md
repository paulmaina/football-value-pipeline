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

- 1X2 outcomes (Home/Draw/Away)
- goal markets such as Over/Under 1.5, 2.5, 3.5, and Under 3.5
- BTTS markets
- candidate shortlist selections based on probability, EV, and reliability gates

It is intended as a research and forecasting tool rather than a guaranteed betting system.

## Supported competitions

- EPL
- La Liga
- Bundesliga
- Serie A
- Ligue 1
- UEFA Champions League (UCL)

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
├── DATABASE_DESIGN.md                           # SQLite-first design notes
├── PIPELINE_AUDIT.md                           # Audit and limitations notes
├── Commands.txt                                 # Example commands
├── .env.example                                 # Example environment config
├── football_output_v2/
│   ├── raw/                                    # Raw predictions and shortlist data
│   ├── readable/                               # Human-readable outputs and reports
│   └── performance/                            # Forward-performance snapshots and summaries
├── tests/                                       # Automated tests
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

### Run the default multi-league forecast

```powershell
python football_value_pipeline_v2_standalone.py --leagues EPL LaLiga Bundesliga SerieA Ligue1 UCL --tune-half-life
```

### Run only a specific league

```powershell
python football_value_pipeline_v2_standalone.py --leagues EPL --tune-half-life
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
eligible archived selection per fixture; all eligible runs remain in Run Tracking.

New value, cagey-tier and master shortlists use kickoffs from 20 minutes to
24 hours after the run. Archived generations retain their recorded horizons.
See the [value rule](docs/team_research_profit.md), [cagey-tier rule](docs/cagey-market-basis-v5.md)
and [master rule](docs/master-market-selection.md).

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
     v27 base rules in [docs/price-edge-shortlist-v27.md](docs/price-edge-shortlist-v27.md));
   - `cagey_correction_monitoring.csv`: one correction record per fixture, from
     the correction the shortlist already computed;
   - `price_edge_tagged_candidates.csv` and `bet365_vs_pinnacle.csv`.

   It no longer runs goal-market walk-forward or count-market validation,
   because v28 selection does not read them (`--goal-market-validation` runs
   them on request; a policy that needs them still runs them and fails closed
   without them). It no longer runs the legacy companion or its half-life
   tuning, because their only readers were archived trials. A manual run without
   `--no-legacy-comparison` still produces them for offline replay.
2. **Check and format**: `workflow_checks.py raw` replays the shortlist, the
   cagey tier and the monitoring records deterministically, then
   `format_football_output.py` writes the readable outputs.
3. **Capture**: `performance_tracking.py capture` archives the forecast, the
   shortlist and these sidecars, each only when bound to the same generation:
   `bet365_vs_pinnacle.csv`, `price_edge_tagged_candidates.csv`,
   `cagey_tier_shortlist.csv` and `cagey_correction_monitoring.csv`.
4. **Review**: `performance_tracking.py review` grades results and refreshes:
   - performance tracking and the BBS forward assessment;
   - the closing-odds review and the CLV report;
   - v27/v28 price-edge tracking, including both tiers and the Correction
     monitoring section;
   - the experiment review queue (no live trials) and pipeline health.

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
- `conservative_bet_shortlist_report.md`
- `conservative_bet_shortlist_readable.csv`

## Recommended usage

The project includes a documented daily-use model that keeps a consistent market blend and recency setup across runs. The README in `football_value_V2_README.md` contains extended operational guidance and validation notes.

For daily use, the usual workflow is:

```powershell
python football_value_pipeline_v2_standalone.py --leagues EPL LaLiga Bundesliga SerieA Ligue1 UCL --tune-half-life
python workflow_checks.py raw
python format_football_output.py
```

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

- `football_value_V2_README.md` — authoritative project-level documentation
- `docs/architecture.md` — module layers, run flow, staking/Elo/Monte Carlo, API service layer
- `football_output_v2/readable/README.md` — readable output explanation
- `PIPELINE_AUDIT.md` — audit and reliability details
- `DATABASE_DESIGN.md` — proposed storage architecture
- `Commands.txt` — example commands and parameters

## License

No explicit license file is present in the repository metadata, so licensing terms should be confirmed before redistribution or commercial reuse.

## Contact / ownership

This repository is maintained under the GitHub user `paulmaina` and is described as a football prediction model project.

## Workflow verification

Pipeline CI tests Python 3.12 and 3.14 on Linux and Python 3.14 on Windows, enforces application and critical-module coverage floors, and exercises the six-league prediction/experiment/format/capture/review path offline. Forward review validates immutable archives and independently reconciles generated reports before publishing, retains failure diagnostics, and reports provider health, training dates and policy groups. Windows LF/CRLF conversion no longer silently excludes experimental sidecars.

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
