# Football Output Folder Structure

Recommended project layout:

```text
FVP_v2/
├── football_value_pipeline_v2_standalone_v203.py
├── format_football_output_v2.py
├── .football_cache/
└── football_output_v2/
    ├── raw/
    │   ├── EPL_predictions.csv
    │   ├── EPL_scorelines.json
    │   ├── EPL_diagnostics.json
    │   ├── EPL_backtest_predictions.csv     # when backtesting
    │   ├── EPL_backtest_bets.csv            # when backtesting
    │   ├── EPL_backtest_metrics.json        # when backtesting
    │   └── ...
    └── readable/
        ├── EPL_report.md
        ├── EPL_predictions_readable.csv
        ├── EPL_scorelines_readable.csv
        ├── EPL_backtest_bets_readable.csv   # when available
        └── README.md
```

## Recommended workflow

### 1. Run the model directly into raw/

```powershell
python football_value_pipeline_v2_standalone_v203.py `
  --leagues EPL `
  --out-dir football_output_v2\raw
```

Use `--force-refresh` when you specifically want fresh downloads:

```powershell
python football_value_pipeline_v2_standalone_v203.py `
  --leagues EPL `
  --out-dir football_output_v2\raw `
  --force-refresh
```

### 2. Generate reader-friendly reports

```powershell
python format_football_output_v2.py
```

The formatter automatically reads `football_output_v2\raw` and writes to
`football_output_v2\readable`.

## Migrating your existing folder

If your current raw files are directly inside `football_output_v2`, run once:

```powershell
python format_football_output_v2.py --organize-raw
```

This moves recognized model-generated files into `football_output_v2\raw` and
then creates the readable reports.

The move is conservative:
- it only moves known pipeline output patterns;
- it does not overwrite files already present in `raw`;
- it does not move files ending in `_readable`;
- it does not alter model data contents.

After migration, use the recommended workflow above.
