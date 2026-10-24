# League registry

[`league_registry.py`](../league_registry.py) is the single list of supported leagues. Each entry records:

| Field | Meaning |
|---|---|
| `key` | Pipeline league key (`--leagues` value, output file prefix) |
| `name`, `country` | Display name used in forecasts and shortlists |
| `football_data_div` | football-data.co.uk division code (blank when another source supplies history) |
| `odds_api_sport_key` | The Odds API sport key |
| `football_data_org_code` | football-data.org competition code |
| `history_seasons` | Seasons of history kept in the repository and used for training |
| `refresh_method` | `football-data.co.uk`, `football-data.org` or `europa-reconciled` |
| `shortlist_approval` | `league` (the league itself was reviewed) or `per-market` (each market needs its own passing audit) |
| `bbs_slug`, `bbs_display_names`, `api_football_id` | Optional statistics collectors; blank means not collected |

Everything else derives from it: the pipeline's `LEAGUES`/`LeagueConfig`, the scheduled forecast league list and committed training files, the training refresh jobs, odds-request budgets, shortlist league eligibility, BBS and API-Football collectors, the historical benchmark, pipeline health and `workflow_checks.py smoke`, which fails if a league has no scheduled refresh.

Print it with `py league_registry.py` (or `--json`).

## Adding a league

Add one entry. Use a refresh method that already exists, verify the Odds API sport key against `GET /v4/sports` (free; no quota cost), and set `shortlist_approval=PER_MARKET_APPROVAL`. The league is then forecast, refreshed and committed automatically, and each of its markets reaches the shortlist only after passing its own reliability audit.

## Per-market leagues

Eredivisie (`N1`, `soccer_netherlands_eredivisie`) and Primeira Liga (`P1`, `soccer_portugal_primeira_liga`) use `shortlist_approval=PER_MARKET_APPROVAL`. Both sport keys were checked against `GET /v4/sports` on 2026-10-24. Their six seasons of football-data.co.uk CSVs are refreshed and committed by `Refresh league training data`, and they are forecast by the scheduled run.

- A market qualifies only if its own walk-forward audit is `RELIABLE_FOR_RANKING`. A forecast of 75% or more also needs its high-confidence tier `PASSED`. An Asian-handicap line needs its own profitable-win audit. Thresholds are the same as for every other league.
- A failed or missing audit is a hard rejection (`per-market approval: …`) in every replayable policy. Archived policies that let the original leagues' failed audits through as PROVISIONAL warnings never do so for these leagues.
- With no reliability report at all, every market is blocked.
- Per-market leagues receive no ranked-mode extra event-odds reservations, so existing leagues keep theirs.
- The market-led paper experiment, which does not use the model audit, skips them without requesting event odds.

Their forecasts still use Odds API credits for the normal league odds request and, in `all` coverage mode, per-event additional markets.
