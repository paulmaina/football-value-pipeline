# Per-market approval for every league (2026-10-24)

**Decision:** every registry league now uses `shortlist_approval=PER_MARKET_APPROVAL`. There is no league-level validation bar. A league/market reaches the shortlist only if that market passed its own reliability audit. Failed markets stay blocked, and the league's other markets stay eligible. No threshold changed.

Evidence is the committed walk-forward reliability reports in `football_output_v2/raw/*_goal_market_validation.json` (validator v9; Asian handicap `asian-handicap-profitable-win-v1`, net-profit basis). No new run, shadow trial or sidecar was produced.

## What changed compared with today

| Area | Before | After |
|---|---|---|
| Registry approval | EPL, LaLiga, Bundesliga, SerieA, Ligue1, UCL, UEL `league`; Eredivisie, PrimeiraLiga `per-market` | All nine `per-market` |
| v24 production shortlist | Every league's ordinary markets and AH lines were already hard-blocked by v23's `profitable-win historical reliability unavailable or failed` / `Asian handicap profitable-win validation unavailable or failed` | Unchanged: v24 is frozen for replay. v25 (Part 4) states the per-market rule explicitly for every league |
| Archived policies (v9–v22) | Original seven could show failed audits as PROVISIONAL warnings | Unchanged (frozen in `ARCHIVED_LEAGUE_APPROVAL`) so captures replay |
| Ranked-mode extra event odds (24 requests) | Original seven only: 4/4/4/3/3/3/3 | All nine: EPL–UCL 3 each, UEL/Eredivisie/PrimeiraLiga 2 each. Total budget unchanged. Not used by the scheduled run (`all` coverage) |
| Market-led paper experiment | Original seven | Unchanged (it does not use the model audit) |

**No league/market changes between eligible and blocked in the production shortlist.** Under v24 the per-market gate already applied to every league. The table below is the complete eligibility map that v25 applies.

## Eligibility by league and market

`OK` = audit `RELIABLE_FOR_RANKING` (eligible). `BLOCK` = failed audit. The suffix shows the high-confidence tiers (75%+ / 85%+): `P` passed, `i` insufficient history, `H` high-confidence overestimation. A forecast at or above 75% needs its tier `P`, otherwise it is blocked even when the market is `OK`.

| market | EPL | LaLiga | Bundesliga | SerieA | Ligue1 | UCL | UEL | Eredivisie | PrimeiraLiga |
|---|---|---|---|---|---|---|---|---|---|
| Home win | OK i/i | OK i/i | OK i/i | OK i/i | OK i/i | OK i/i | OK i/i | OK i/i | OK P/i |
| Away win | OK i/i | OK i/i | OK i/i | OK i/i | OK i/i | OK i/i | OK i/i | OK i/i | OK i/i |
| Draw | OK i/i | OK i/i | OK i/i | OK i/i | OK i/i | **BLOCK** | OK i/i | **BLOCK** | **BLOCK** |
| DC 1X | OK P/P | OK P/P | OK P/P | OK P/P | OK P/P | OK P/P | OK H/i | OK P/P | OK P/P |
| DC X2 | OK P/i | OK P/i | OK P/i | OK P/i | OK P/i | OK H/i | OK i/i | OK P/i | OK P/P |
| DC 12 | OK P/i | OK P/i | OK P/i | OK P/i | OK P/i | **BLOCK** | OK P/i | **BLOCK** | **BLOCK** |
| Over 1.5 | **BLOCK** | OK P/i | **BLOCK** | OK P/i | OK P/i | **BLOCK** | OK P/P | **BLOCK** | OK P/i |
| Under 3.5 | **BLOCK** | OK P/P | **BLOCK** | OK P/i | OK P/i | **BLOCK** | **BLOCK** | **BLOCK** | OK H/i |
| BTTS Yes | **BLOCK** | **BLOCK** | **BLOCK** | OK i/i | **BLOCK** | **BLOCK** | **BLOCK** | **BLOCK** | OK i/i |
| AH lines (of 50) | 50 OK | 50 OK | 50 OK | 50 OK | 50 OK | 34 OK, 16 BLOCK | **0: no profitable-win audit** | 50 OK | 50 OK |

Under 3.5 and BTTS are outside the v24/v25 market groups, so they are not shortlisted even where eligible.

- **UCL failed AH lines:** Away −1.00 to −2.75 and Home +1.25 to +3.00 (16 lines).
- **UEL:** its report has a loss-first AH audit but no `asian_handicap_win` (profitable-win) audit, so every UEL AH line stays blocked.

## Asian handicap: Eredivisie and Primeira Liga

Both pass all 50 lines on the same validator version and net-profit basis as every other league. Limits: at least 80 development and 40 audit matches, audit Brier ≤ reference + 0.01, audit overconfidence ≤ 0.10.

| league | reliable / 50 | dev n | audit n | penalty range | max audit overconfidence |
|---|---:|---:|---:|---|---:|
| Eredivisie | 50 | 344 | 188 | 0.000–0.081 | +0.059 (Home 0 / −0.25 to −0.75) |
| Primeira Liga | 50 | 343 | 187 | 0.018–0.073 | +0.044 (Home −2.00 to −2.75) |

Per-line confidence penalty / audit overconfidence (lines sharing a penalty are grouped):

| line group | Eredivisie Home | Eredivisie Away | Primeira Home | Primeira Away |
|---|---|---|---|---|
| 0, −0.25 … −0.75 | 0.069 / +0.059 | 0.081 / −0.010 | 0.073 / +0.035 | 0.032 / +0.017 |
| −1.00 … −1.75 | 0.071 / −0.001 | 0.056 / −0.020 | 0.047 / +0.037 | 0.051 / +0.040 |
| −2.00 … −2.75 | 0.067 / −0.021 | 0.043 / −0.026 | 0.034 / +0.044 | 0.021 / +0.008 |
| −3.00 | 0.046 / −0.011 | 0.024 / −0.010 | 0.025 / +0.025 | 0.019 / +0.005 |
| +0.25 … +1.00 | 0.009 / +0.010 | 0.029 / −0.059 | 0.055 / −0.017 | 0.018 / −0.035 |
| +1.25 … +2.00 | 0.019 / +0.020 | 0.015 / +0.001 | 0.019 / −0.040 | 0.030 / −0.037 |
| +2.25 … +3.00 | 0.006 / +0.026 | 0.000 / +0.021 | 0.030 / −0.008 | 0.025 / −0.044 |

## Replay

All 27 replayable captures were rebuilt with their recorded policy and evidence on `main` and on this branch: 11 prediction-run bundles plus the current run, and 15 snapshots with saved validation evidence, covering v10, v11, v14, v15, v16, v20, v22, v23 and v24. Picks and full decision tables were identical.
