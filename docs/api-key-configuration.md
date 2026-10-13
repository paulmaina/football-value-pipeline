# API credentials from .env

Local prediction and performance-review commands read credentials exclusively
from `.env` beside the Python scripts. This works even when launched from a
different working directory. The file overrides inherited PowerShell API-key
values. Missing or blank entries clear inherited values, including fallback keys;
there is no silent fallback to PowerShell when `.env` is absent or incomplete.

Keep these four settings in `.env`:

```dotenv
THE_ODDS_API_KEY=your_primary_key
THE_ODDS_API_KEY_FALLBACK_1=your_optional_secondary_key
THE_ODDS_API_KEY_FALLBACK_2=your_optional_tertiary_key
FOOTBALL_DATA_API_KEY=your_football_data_org_key
```

Leave unused fallback entries blank. Quotes and dotenv comments are supported.
Interpolation is disabled so `${VARIABLE}` cannot import a shell credential.
Only these API-key variables are replaced; other process settings remain intact.
Restart the command after editing `.env` to load the new credentials.

Update dependencies after pulling:

```powershell
py -m pip install -r football_value_requirements.txt
```

If you have no `.env` yet, copy `.env.example` and fill in your own keys. Preserve
any existing `.env`. The file remains ignored by git and must not be committed.
Keys are not printed by the loader; configuration status only reports presence.

The usual prediction command needs no new flags. Manual
`py performance_tracking.py review` uses the same file. Programmatic client calls
retain their explicit-credential API; callers can invoke `load_api_keys()` first
to apply this configuration policy outside the command-line entry points.

## GitHub Actions

Automated reviews run in a fresh checkout without your private local `.env`.
The workflow explicitly passes `--api-key-source environment` to the publisher,
which forwards it to the review subprocess. GitHub repository secrets therefore
remain usable. This opt-in mode is not selected automatically by a PowerShell
variable, working directory, or presence of `GITHUB_ACTIONS`.

The predictions and review CLIs also accept this explicit mode for CI. Their
default always remains `dotenv`. No actual credentials are added by this change.
