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
| `shortlist_approval` | `per-market` for every league: each market needs its own passing audit |
| `bbs_slug`, `bbs_display_names`, `api_football_id` | Optional statistics collectors; blank means not collected |

Everything else derives from it: the pipeline's `LEAGUES`/`LeagueConfig`, the scheduled forecast league list and committed training files, the training refresh jobs, odds-request budgets, shortlist league eligibility, BBS and API-Football collectors, the historical benchmark, pipeline health and `workflow_checks.py smoke`, which fails if a league has no scheduled refresh.

Print it with `py league_registry.py` (or `--json`).

## Adding a league

Add one entry. Use a refresh method that already exists, verify the Odds API sport key against `GET /v4/sports` (free; no quota cost), and set `shortlist_approval=PER_MARKET_APPROVAL`. The league is then forecast, refreshed and committed automatically, and each of its markets reaches the shortlist only after passing its own reliability audit.

## Per-market approval

Every league uses `shortlist_approval=PER_MARKET_APPROVAL`; there is no league-level validation bar. See [audits/2026-10-24-per-market-approval.md](audits/2026-10-24-per-market-approval.md) for the per-league, per-market results.

- A market qualifies only if its own walk-forward audit is `RELIABLE_FOR_RANKING`. A forecast of 75% or more also needs its high-confidence tier `PASSED`. An Asian-handicap line needs its own profitable-win audit. Thresholds are the same for every league.
- A failed market stays blocked; the league's other markets stay eligible. With no reliability report at all, every market is blocked.
- Every league shares the unchanged ranked-mode budget of 24 extra event-odds requests.

Eredivisie (`N1`, `soccer_netherlands_eredivisie`) and Primeira Liga (`P1`, `soccer_portugal_primeira_liga`) sport keys were checked against `GET /v4/sports` on 2026-10-24. Their six seasons of football-data.co.uk CSVs are refreshed and committed by `Refresh league training data`, and they are forecast by the scheduled run.

Süper Lig (`T1`, `soccer_turkey_super_league`) was added the same way on 2026-10-26; see [audits/2026-10-26-super-lig-validation.md](audits/2026-10-26-super-lig-validation.md). football-data.org does not offer it, so it has no competition code and its forecasts are not settled by forward performance tracking. Its reviewed Odds API team names are under `SuperLig` in `bbs_team_aliases.json`.

### Archived policies

Archived captures replay unchanged. Policies up to v24 keep their frozen view: the seven leagues in `ARCHIVED_LEAGUE_APPROVAL` (EPL, LaLiga, Bundesliga, SerieA, Ligue1, UCL, UEL) were league-reviewed, so older policies that showed their failed audits as PROVISIONAL warnings still do. Leagues added later are rejected with `per-market approval: …` in every policy. The market-led paper experiment, which does not use the model audit, stays limited to those seven and spends no event-odds credits on the others.

Their forecasts still use Odds API credits for the normal league odds request and, in `all` coverage mode, per-event additional markets.
