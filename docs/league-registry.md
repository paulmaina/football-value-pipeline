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
| `shortlist_validated` | Reviewed validation evidence exists; `False` keeps every market out of the shortlist |
| `bbs_slug`, `bbs_display_names`, `api_football_id` | Optional statistics collectors; blank means not collected |

Everything else derives from it: the pipeline's `LEAGUES`/`LeagueConfig`, the scheduled forecast league list and committed training files, the training refresh jobs, odds-request budgets, shortlist league eligibility, BBS and API-Football collectors, the historical benchmark, pipeline health and `workflow_checks.py smoke`, which fails if a league has no scheduled refresh.

Print it with `py league_registry.py` (or `--json`).

## Adding a league

Add one entry. Use a refresh method that already exists, verify the Odds API sport key against `GET /v4/sports` (free; no quota cost), and set `shortlist_validated=False`. The league is then forecast, refreshed and committed automatically, but its markets are rejected as "competition excluded from shortlist validation". Change the flag only in a reviewed commit after the league's validation evidence has been examined; no check is relaxed automatically.

## Unvalidated leagues

Eredivisie (`N1`, `soccer_netherlands_eredivisie`) and Primeira Liga (`P1`, `soccer_portugal_primeira_liga`) are registered with `shortlist_validated=False`. Both sport keys were checked against `GET /v4/sports` on 2026-10-24. Their six seasons of football-data.co.uk CSVs are refreshed and committed by `Refresh league training data`, and they are forecast by the scheduled run. Until the flag changes:

- every market is rejected by the existing shortlist league check, in every replayable policy version, even if a historical reliability report passes;
- they receive no ranked-mode extra event-odds reservations, so existing leagues keep theirs;
- the market-led paper experiment skips them without requesting event odds.

Their forecasts still use Odds API credits for the normal league odds request and, in `all` coverage mode, per-event additional markets.
