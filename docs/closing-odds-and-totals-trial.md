# Local closing quotes and separate Pinnacle totals trial

Production probabilities, shortlist filters and bets remain unchanged. These additions collect evidence; neither promotes a candidate nor places bets. No Odds API key is required in GitHub Secrets.

## Daily forecast workflow

Continue your existing six-league command with the goal, market-led and recency flags. Every normal run also writes `raw/totals_anchor_experiment.json` automatically, using the Pinnacle O/U 2.5 pair already present in the normal odds response. This adds no odds request and no model fit. Push forecasts promptly before kickoff so the existing Actions workflow captures them with the usual 20-minute minimum lead.

The trial separately scales the fitted home/away goal intensities, retaining fitted Dixon-Coles rho and production 1X2 probabilities, to match the power-devigged Pinnacle Over 2.5 probability. It is the historical benchmark's proportional anchoring method, not a joint fit or an xG feature. Only complete, coherent Pinnacle quotes with market timestamps no more than ten minutes old qualify. Production must retain its registered 0.5 market weight, and its 1X2 reference must also be no more than ten minutes old, within five minutes of the totals quote. Missing quotes, unknown teams, matrix/parameter inconsistencies and solver failures remain explicit unavailable coverage. Domestic leagues only; UCL was absent from the historical nomination. First archived observations, including unavailable observations, are frozen; earlier forecasts are never backfilled.

Primary metric is Under 3.5 paired log loss, selected before forward collection. Under 3.5 remains excluded from the shortlist. Over 1.5, BTTS Yes and Over 2.5 are guardrails. Review requires 300 paired fixtures, six ISO gameweeks, >=80% verified in-scope coverage and no rejected snapshot evidence. Supportive forecasting evidence additionally requires a positive week-block bootstrap interval and no log-loss/Brier deterioration in any registered market. Readiness is not approval or proof of profitable betting. Versions cannot be pooled. The review queue, performance health and Excel health sheet show this trial alongside the others.

## Closing quotes stay local

Ordinary morning forecasting cannot record a price immediately before an evening kickoff. A collector must run on your computer near kickoff, with internet access and your `.env` keys. You can either leave a second PowerShell terminal open:

```powershell
py closing_odds.py --watch --hours 12
```

or register a local Windows task **once**, from the repository directory:

```powershell
powershell -ExecutionPolicy Bypass -File .\register_closing_odds_task.ps1
```

The task runs every five minutes while you are signed in. Keep your computer awake. It uses your existing `py` launcher and repository working directory; no administrator access, plaintext credentials or GitHub API keys are embedded in the task. The script has been inspected but must be installed on your Windows computer; it cannot be installed remotely from this workspace. Disable/remove it with:

```powershell
Unregister-ScheduledTask -TaskName FootballClosingOddsCollector -Confirm:$false
```

The watcher polls locally every 30 seconds; API calls are only made when an event in your current forecast CSV is within six minutes of its scheduled kickoff. It normally collects once per event and retries empty/error responses while still in that window. It requests Pinnacle and 1xBet h2h and O/U 2.5, adding alternate totals, BTTS or double chance when the frozen/current shortlist needs those markets. A persistent UTC daily budget caps request attempts at 100 across invocations. This is a request cap, not a provider-credit cap: credits depend on returned markets/bookmaker groups. The collector adds genuine API usage; lower `--max-requests` to limit a session further. No stale cache fallback is allowed. Failed fetches record only exception type, never secret-bearing URLs. A failed/slow response received after kickoff is excluded.

Content-addressed append-only observations are written under `football_output_v2/closing_odds/observations/`. Push them after collection using your usual Git workflow. You may push these files after kickoff: original forecast eligibility still depends on its earlier immutable CI snapshot. The closing-quote files retain the full API payload, event identity, response time, bookmaker market timestamps and calculation method. Hash checks detect changed files. Local capture timestamps are **not independently attested** by GitHub, and the actual whistle time can differ from the scheduled kickoff.

Reports under `performance/closing_odds/` compare the frozen shortlist's offered price with each bookmaker's latest valid observed quote. Quote collection requires a response within six minutes before scheduled kickoff, with market timestamps <=120 seconds old. Missing coverage stays missing. These are **observed near-close quotes**, not guaranteed official final closing odds. If that guarantee is required, a provider supplying an authoritative close/actual kickoff and independent timestamp evidence is still needed.

The report distinguishes same-book offered-price CLV (`entry / 1xBet closing offer - 1`) from fair-close EV (`entry * devigged closing probability - 1 - configured per-stake cost`). Neither proves an accepted execution or actual profit. Pinnacle double-chance fair probabilities may be derived by summing coherent devigged 1X2 probabilities; a direct double-chance price is never fabricated. Collection has no production input path; closing prices cannot influence the pre-match experiment.

## Pushing and review

After forecasts or closing quotes change:

```powershell
git add .
git commit -m "Update forecasts and closing quote evidence"
git pull --rebase
git push origin main
```

Keep `.env` ignored. The push-triggered and daily forward review rebuild and reconcile reports from archived forecasts and collected quotes. There is no need to enable the GitHub scheduled forecast collector. Automatic review issues remain evidence-only; you review findings and approve any later production proposal.
