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
