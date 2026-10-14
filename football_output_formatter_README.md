# Football Output Formatter

Keep `format_football_output.py` next to your V2 model script.

The formatter reads the existing `football_output_v2` directory and creates a
separate `football_output_v2/readable` directory. It never rewrites the model's
raw CSV/JSON files.

## Run

```powershell
python format_football_output.py
```

Or specify folders:

```powershell
python format_football_output.py `
  --input-dir football_output_v2 `
  --output-dir football_output_v2\readable
```

Show more scorelines in each match report:

```powershell
python format_football_output.py --top-scorelines 8
```

Hide technical appendices:

```powershell
python format_football_output.py --no-technical
```

## Main outputs

- `EPL_report.md` — natural-language match report with tables and explanations.
- `EPL_predictions_readable.csv` — compact human-friendly fixture summary.
- `EPL_scorelines_readable.csv` — complete available scoreline distribution in tabular form.
- `EPL_backtest_bets_readable.csv` — generated when a V2 backtest bet file exists.
- `README.md` — definitions for common model terms.

The raw `football_output_v2` files remain the source of truth.

# Performance workbook navigation

The generated `football_performance_report.xlsx` opens on Dashboard. Use its
links to open experiment readiness, collection health, weekly sample/profit
trends and metric definitions. Experiments shows each existing review gate,
the unit being counted, coverage and remaining requirements; readiness does
not approve a production change.

Pipeline Health separates source freshness, near-close coverage, quote audits
and capture counts. Capture Details retains all six experiment capture states.
Selections and Predictions freeze the kickoff, league and match columns;
technical fields are grouped and collapsed, and can be expanded in Excel.
ROI Plan retains the editable bankroll and flat stake. Weekly Trends updates
from the calculated breakdowns and shows simulated offered-price results.

The layout refreshes with the existing formatter and forward-review workflow.
No new command, API request or dependency is required. Close the workbook in
Excel before regenerating it.

