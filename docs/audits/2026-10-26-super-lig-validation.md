# Süper Lig registration and reliability validation (2026-10-26)

**Registry:** `SuperLig` ("Super Lig"), football-data.co.uk `T1`, The Odds API `soccer_turkey_super_league`, six seasons, `PER_MARKET_APPROVAL`. No threshold or gate was changed.

## Sources

| source | status |
|---|---|
| football-data.co.uk `T1` | 6 seasons, 2021/22 to 2026/27: 380 + 342 + 380 + 342 + 306 + 72 = **1,822 matches** to 2026-10-19, all passed the refresh validator. 2022/23 is short because two clubs withdrew after the February 2023 earthquake. |
| The Odds API | `soccer_turkey_super_league` listed and active in `GET /v4/sports` on 2026-10-26. |
| football-data.org | Not offered on this account's plan (13 competitions, none Turkish). No competition code. |
| BBS | No Turkish league in `openapi.json` known league values. No slug. |
| API-Football | Left off, like Eredivisie and Primeira Liga. The daily allowance was already exhausted on 2026-10-26, so league 203 could not be confirmed, and adding a league would share the allowance with the existing six. |

The initial registration had no forward-results adapter. The follow-up Turkish grading repair uses keyless Football-Data.co.uk T1 season results, retaining the downloaded CSV bytes and their SHA-256 for report verification. Matching requires the exact forecast UTC date, home/away order and reviewed team aliases, with no fuzzy match or fabricated kickoff time. Missing, conflicting or ambiguous results remain ungraded. This source can lag completed matches; review retries on subsequent runs. The fixture lookup still skips football-data.org for leagues without a code instead of requesting `/competitions//matches`.

## Team names (Odds API vs football-data.co.uk)

All 18 teams in the next 7 days of Odds API events, which is every 2026/27 club, were checked with the model's `resolve_team` against the T1 history.

- Three did not resolve: `Amed SK` (Amedspor), `Basaksehir` (Buyuksehyr), `Erzurum BB` (Erzurumspor).
- Four resolved only at the shortlist minimum score of exactly 90: `Gazişehir Gaziantep`, `Torku Konyaspor`, `Çaykur Rizespor` and `Çorum FK`.

Eleven reviewed aliases were added under `SuperLig` in `bbs_team_aliases.json`, the per-league map `resolve_team` already reads. After the change, all 18 names resolve at 100. Global canonical keys are unchanged.

## Pinnacle coverage

Live `/odds` (eu region; h2h, totals, spreads) on 2026-10-26 returned 9 of 9 events in the next 7 days. Pinnacle quoted all three markets on 9 of 9; onexbet 9 of 9; bet365 0 of 9. Pinnacle totals points were 2.25 to 3.25. Per-event additional markets (alternate totals, BTTS, double chance) were not sampled, to save credits.

## Method

The production generation step (`_generate_main`, the code path of the scheduled forecast command) ran with `--leagues SuperLig --no-live-odds --fixture-provider football-data-uk --goal-blend-experiment --recency-experiment --reliability-experiment`. It used the unchanged validator settings: min_train 500, 56-day steps, a 75%/25% development/audit split and power de-vig. Production half-life stays 480 days; the tuned diagnostic was 365. It wrote to a scratch directory and spent no credits.

The publish wrapper's raw check rejects any offline run with football-data.co.uk fixtures, because those carry no kickoff time until a live quote supplies one. That applies to every league and does not affect validation.

## Market status

Limits: audit Brier excess ≤ +0.005, |overconfidence| ≤ 0.12, at least 30 development and 12 audit matches. Development n = 451, audit n = 151.

| market | status | audit Brier | baseline | excess | audit overconf | 75+/85+ |
|---|---|---:|---:|---:|---:|---|
| home_draw (DC 1X) | PASS | 0.1654 | 0.1947 | −0.0293 | −0.045 | PASSED/PASSED |
| draw_away (DC X2) | PASS | 0.2350 | 0.2495 | −0.0144 | +0.083 | PASSED/INSUFF |
| home_away (DC 12) | PASS | 0.1690 | 0.1670 | +0.0020 | −0.037 | PASSED/INSUFF |
| home | PASS | 0.2350 | 0.2495 | −0.0144 | −0.083 | INSUFF/INSUFF |
| draw | PASS | 0.1690 | 0.1670 | +0.0020 | +0.037 | INSUFF/INSUFF |
| away | PASS | 0.1654 | 0.1947 | −0.0293 | +0.045 | INSUFF/INSUFF |
| over_1_5 | PASS | 0.1766 | 0.1745 | +0.0021 | −0.023 | PASSED/PASSED |
| under_3_5 | PASS | 0.1996 | 0.2037 | −0.0041 | −0.004 | PASSED/INSUFF |
| btts_yes | **FAIL-audit** | 0.2589 | 0.2497 | **+0.0092** | +0.029 | INSUFF/INSUFF |

Asian handicap: all 50 lines `RELIABLE_FOR_RANKING` on both profitable-win v1 and loss-first v1.

## Shortlist effect

No Süper Lig reliability report is committed, so every market is blocked until the scheduled forecast run produces one. Under per-market approval, that run's audit then decides each market: on the evidence above, BTTS would stay blocked and the other eight markets plus the AH lines could qualify, subject to every quote, identity, timing and high-confidence check.

## Odds API credits

- Events list: 0 credits.
- League odds request: 3 credits (h2h, totals, spreads × 1 region).
- `all` additional coverage: up to 5 per event in the 3-day window (alternate totals, BTTS, alternate spreads, DNB, double chance; no corner markets for this league).
- Per daily scheduled run: about 3 to 48 credits, depending on how many of a round's 9 fixtures fall in the window; at most about 160 a week.
- Closing odds are collected only for shortlisted picks, so they add nothing while no pick qualifies.
- Ranked mode keeps the unchanged 24-request budget; with ten leagues Ligue1 and UCL reserve 2 instead of 3.
