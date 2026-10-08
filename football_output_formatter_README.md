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
