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

This project reads API credentials from environment variables instead of storing secrets in source files.

PowerShell example:

```powershell
$env:THE_ODDS_API_KEY="your-primary-key"
$env:THE_ODDS_API_KEY_FALLBACK_1="your-secondary-key"
$env:THE_ODDS_API_KEY_FALLBACK_2="your-tertiary-key"
$env:FOOTBALL_DATA_API_KEY="your-football-data-org-key"
```

bash/zsh example:

```bash
export THE_ODDS_API_KEY="your-primary-key"
export THE_ODDS_API_KEY_FALLBACK_1="your-secondary-key"
export THE_ODDS_API_KEY_FALLBACK_2="your-tertiary-key"
export FOOTBALL_DATA_API_KEY="your-football-data-org-key"
```

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
python format_football_output.py
```

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
