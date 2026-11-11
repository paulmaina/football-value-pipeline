# Football value pipeline: notes for Claude

Read `docs/plan.md` first. It holds the current plan, the release rules and the decisions already made.

## Working rules

- **No production change without evidence.** Predictions, probabilities and shortlist logic change only after a candidate passes the release gate in `docs/plan.md`, and only through a reviewed PR. Reporting-only fixes may go in separate PRs.
- **The value shortlist's research model must stay independent of bookmaker odds.** Never feed odds, the published grid or market fits into it. Keep the odds-perturbation test passing.
- **The holdout (Eredivisie, Primeira Liga and Süper Lig, 16 Jan – 10 Oct 2026) is locked.** Don't run `evaluation_harness.py --declaration` or look at holdout scores while developing; each candidate and each frozen setup can be scored once. Develop on the development period; validation and retrospective periods have already been inspected.
- **The European holdout (UCL, 21 Jan 2025 – 12 Oct 2026) is locked the same way**, with its own ledger (`evaluation/european_holdout_ledger.json`). Don't run `--mode european --declaration`; develop on European development and validation (UEL only; see `docs/european-backtest.md`).
- **Pre-kickoff data only.** Anything graded or replayed must have been known before the match (see `performance_tracking.lead_checked`).
- **Bets are placed at Pinnacle only** (`shortlist_quote_policy.json`). That is separate from where a model's probabilities come from.
- Work on a branch and open a PR; don't push to `main`.

## Useful commands

```bash
pip install -r football_value_dev_requirements.txt
python -m pytest -q tests                                   # full suite (~5 min)
python evaluation_harness.py --output /tmp/eval             # development + validation, 8 leagues
python evaluation_harness.py --mode live --output /tmp/live # replay frozen forecasts since 5 Nov 2026
python evaluation_harness.py --mode parity --output /tmp/parity # research model: harness vs live inputs and probabilities
python evaluation_harness.py --mode european --output /tmp/europe # UCL/UEL results only, locked; CE baseline
python performance_tracking.py review --api-key-source environment && python workflow_checks.py reports
```

## Map

- `football_value_pipeline_v2_standalone.py`: forecasting pipeline (Dixon-Coles, market blend, published grid).
- `team_research.py`, `profit_shortlist.py`: the independent research model and the value shortlist.
- `price_edge_cagey_shortlist.py`, `narrow_margin.py`, `cagey_market_basis.py`: the cagey tier (market view).
- `master_shortlist.py`, `master_selection*.py`: the master shortlist.
- `performance_tracking.py`, `workflow_checks.py`: grading, reports and their validation.
- `evaluation_harness.py`, `research_backtest.py`, `historical_benchmark.py`: offline evaluation; `european_results.py`: cached UCL/UEL results for the harness.
- `.football_cache/`: historical football-data.co.uk files (Pinnacle prices end 15 Jan 2026; Bet365 continues).
