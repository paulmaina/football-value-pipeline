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
inside the 48-hour shortlist window. It has no ranked 24-attempt cap. Use
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

The current shortlist is capped at twelve distinct matches within 48 hours.
New policy v17 allows Home win, Draw, Away win, Over 1.5 and full-time Asian goal
handicaps from Pinnacle/bet365. It ranks the lowest conservative estimated loss
risk first, then full-refund probability and positive EV. Double chance, BTTS and
Under 3.5 are excluded from new shortlists. Failed gates are never used to fill
twelve matches. Refunds and half settlements are graded explicitly; estimates
are not guarantees. See [Asian handicap rules, coverage and quote input](docs/asian-handicap-shortlist.md).

Closing collection runs in GitHub Actions; the PC can be off. Its primary
closing analysis now uses the latest-selection ROI cohort, with a separate
first-entry reference. Existing experimental first-entry baselines are preserved.
See [run integrity and recovery](docs/prediction-run-integrity.md).

## Output formats

The project writes both machine-readable and narrative outputs.

### Raw outputs

Located under `football_output_v2/raw/`:

- `<league>_predictions.csv`
- `<league>_scorelines.json`
- `<league>_diagnostics.json`
- `conservative_bet_shortlist.csv`
- `conservative_bet_summary.json`
- `shortlist_history/`

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
- `football_output_v2/readable/README.md` — readable output explanation
- `PIPELINE_AUDIT.md` — audit and reliability details
- `DATABASE_DESIGN.md` — proposed storage architecture
- `Commands.txt` — example commands and parameters

## License

No explicit license file is present in the repository metadata, so licensing terms should be confirmed before redistribution or commercial reuse.

## Contact / ownership

This repository is maintained under the GitHub user `paulmaina` and is described as a football prediction model project.

## Workflow verification

Pipeline CI now tests Python 3.12/3.14 on Linux and Windows, enforces application and critical-module coverage floors, and exercises the six-league prediction/experiment/format/capture/review path offline. Forward review validates immutable archives and independently reconciles generated reports before publishing, retains failure diagnostics, and reports provider health, training dates and policy groups. Windows LF/CRLF conversion no longer silently excludes experimental sidecars.

See [Workflow checks and evidence](docs/workflow-assurance.md) for controls, artifacts, local commands and limitations. Rerun with both experiment flags and push before kickoff to capture future experiment evidence; historical snapshots are preserved.
# Daily evidence and execution checks

See [daily data health and forward evidence](docs/daily-evidence.md) for UCL
automatic refresh, production quote eligibility and costs, and the new
performance report health history. Existing forecasting commands remain valid.

The optional [recency-weighting experiment](docs/recency-experiment.md) extends
the existing goal sidecar with Over 1.5/BTTS half-life comparisons. Add
`--recency-experiment` alongside `--tune-half-life`; production selections stay
independent while forward results are captured and reviewed automatically.


Conservative EV sensitivity is recorded automatically on current-fixture runs: [experiment guide](docs/filter-sensitivity-experiment.md). It compares 1.5%, 3%, and 5% floors without changing the live shortlist.

A separate [historical benchmark](docs/historical-benchmark.md) compares regularisation, recency, market weighting and totals anchoring on pinned data. Run `py historical_benchmark.py --materialize-pinned-data`; production commands and settings are unchanged. Future trial gates are recorded in `benchmark_promotion_rules.json`.

The [benchmark forward bridge](docs/benchmark-forward-automation.md) automatically captures a frozen 85% market-weight candidate and reports review readiness. Daily scheduled forecast collection requires Odds API keys in GitHub Secrets; local `.env` files are not available to Actions. GitHub issues request review once evidence gates are reached; production changes require approval.

GitHub Actions closing quote collection and the separate Pinnacle totals trial: [setup, Windows-task migration and evidence limits](docs/closing-odds-and-totals-trial.md). Normal forecasts generate the totals sidecar automatically; closing collection reuses the existing Odds API repository secrets and publishes observations back to the repository.

## Supplementary API-Football collection

API-Football can add cached, validated results, fixtures and lagged statistics
alongside existing providers. Configure the optional `API_FOOTBALL_KEY` repository
secret for the free-plan collector, which defaults to historical seasons 2022–2024.
Current-season data continues through existing providers. See [setup, limits and model eligibility](docs/api-football-integration.md).

The BBS and API-Football collectors use the full provider allowance for due data,
with no default local request budgets or reserved calls. Provider cooldowns and
cache freshness still apply. football-data.org already has no local request budget.
