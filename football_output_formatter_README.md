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

# The two workbooks

Both workbooks share one theme (`excel_book.py`): a title line on every sheet with
the run time in Nairobi time (EAT, UTC+3) and the CSV that keeps the full columns,
native Excel tables with their own filters, banded rows, frozen header rows and
lead columns, number formats (odds 2 dp, probabilities as %, returns with a sign)
and colour cues (tiers safe / fill / risky fill; flags such as "research strongly
disagrees" and "unvalidated view"; wins green, losses red). Blank inputs show a
short reason ("no Pinnacle quote", "not graded yet"), never a silent blank.

`league_predictions.xlsx` (`predictions_workbook.py`): Master shortlist, Old master
(shadow) with the same columns, Value shortlist, Cagey tier, then one tab per
league. The master tabs read the run bundle's raw master files: tier, cagey and
research no-loss chances, the research gap, labels, a short inspection note for
flagged picks, list overlap, quote time and a re-check reminder.

`football_performance_report.xlsx` (`performance_report_layout.py`): Dashboard,
Picks & Results, Weekly Trends, Breakdowns, Calibration, CLV, Model Monitoring and
Guide. Master tracking starts afresh at the first forecast run after the new master
went live (14 Nov 2026); earlier graded data stays in the repository but is not
shown. The Dashboard puts the live and old master side by side, the rollback checks
and data health (last forecast run, Odds API credits, warnings, training freshness).
Model Monitoring shows the new master's rollback rule, research v5 vs v4, CE3n vs
CE ("not released yet" until its release writes figures) and the home-favourite
check.

The layout refreshes with the existing formatter and forward-review workflow.
No new command, API request or dependency is required. Close the workbook in
Excel before regenerating it.

