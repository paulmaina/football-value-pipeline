# Feature sources check: ClubElo, rest and congestion, lineups (23 Nov 2026)

Investigation only. Nothing live, no harness candidate, no declaration. No holdout score was read: holdout fixtures were counted by identity and date only, as the plan's European holdout counting does. The scripts are in `scripts/feature_sources/` and the figures in `clubelo.json`, `rest_days.json` and `lineups.json` here. Caches are in `data/feature_cache/{clubelo,rest,lineups}` (untracked). This ran in its own worktree, venv and cache folders, separate from the FotMob xG check.

**Decisions (Paul, 23 Nov 2026):** rest and congestion go ahead: ESPN schedule backfill, a C6-plus-rest candidate built on development data, and its declaration queued behind 2g-4. ClubElo and lineups are parked (`docs/plan.md`, open items 10 and 11).

## Summary

| Source | History depth | Coverage | Known before kickoff? | Reliability notes | Ready for a holdout backtest? |
| --- | --- | --- | --- | --- | --- |
| ClubElo API (soccerdata `ClubElo`) | Not measurable | None: no data | Yes by construction (rating on day D reflects matches to D−1) | api.clubelo.com unreachable on 23 Nov 2026: connection timeouts from this machine (3 attempts, 07:20–07:50 UTC) and connection refused from Anthropic's fetcher. clubelo.com itself is up (data dated 22 Nov). Whether the ratings use bookmaker odds anywhere is not confirmed | **No** |
| ClubElo mirror (fallback; github.com/xgabora, commit 25882a5) | Genuine ClubElo, 1st and 15th of each month, 1 Jul 2000 – 1 Jun 2025; after that the maintainer's own provisional ratings | Domestic matches with both clubs rated by genuine ClubElo: development 95.7%, validation 0%, holdout 0%. European matches involving a club from outside the eight leagues: 35% | Yes (latest snapshot before the match day, up to 15 days old) | Only 19 countries. Renames break club histories (M'gladbach and Nott'm Forest start Jan 2025, Gaziantep and Estrela Aug 2025). 3 of 61 automatic European matches were wrong on review | **No** (no genuine ratings in validation or holdout) |
| Rest and congestion from fixtures already held | Domestic 2015/16 on; UCL 2015/16 on; UEL 2020/21 on | 96–97% of domestic team-matches have a rest value (the rest are season openers). But 12.8% of competitive matches are missing (ESPN audit): days since last match is wrong for 14.2% of league team-matches (23.2% for clubs playing in Europe) | Yes (dates only) | No domestic cups, no Conference League, no qualifiers, no UEL before 2020/21, no super cups or play-offs | **Not as is**: backfill from ESPN first |
| Rest and congestion from ESPN team schedules | 2016/17 on (checked 2016/17, 2019/20, 2022/23, 2024/25) | All competitions. 288/288 requests answered, no rate limiting | Yes; the live pipeline already reads these schedules (`rest_and_travel` in research evidence) | ESPN ids must be mapped to our names: 125/128 sample clubs through the reviewed resolver, 3 by close match | **Yes, after the backfill** |
| Lineups, ESPN after the match | 2016/17 on | Both starting XIs in 120/120 sample matches; formations 75–100% | Published about 1 h before kickoff; history has no publication time | Never any injury or suspension list (0/120) | **No** (see the timing problem below) |
| Lineups and availability, pipeline's own pre-kickoff ESPN evidence | Kickoffs from 5 Nov 2026 only (191 fixtures) | Both rosters 14%; 11 starters each 14%; XIs explicitly confirmed 0%; injury lists 0% | Yes, timestamped | Last observation a median 190 min before kickoff; 25% within 75 min | **No** (too short and too sparse) |
| Sofascore (soccerdata `Sofascore`) | — | — | — | api.sofascore.com and sofascore.com time out from this machine; the reader fails at its first request | **No** |
| FotMob | — | — | — | soccerdata 2026.43.0 has no FotMob reader; `/api/leagues` and `/api/matchDetails` return 404 (two requests, deliberately few because of the parallel FotMob run) | **No** |

## Recommendation

1. **Rest and congestion: the only one worth taking towards a backtest, but backfill from ESPN first.** The held fixtures miss about 1 in 8 competitive matches. That error lands mostly on clubs playing in Europe, and in the holdout leagues the Conference League and domestic cups are exactly what is missing. ESPN's all-competition team schedules go back to 2016/17, answered every request, and are what the live pipeline already reads. Building harness features from them keeps harness and live inputs the same, which the parity test requires; building them from held fixtures alone would not. Steps: backfill ESPN schedules for every club in the eight leagues, 2016/17 to date (about 2,800 requests). Build a C6-plus-rest candidate on development only, check it on validation, then declare it against C6 under the existing gate. Domestic holdout coverage is fine (95.8% of holdout team-matches have a rest value from dates alone). Sequencing: under "one change per list at a time" it queues behind C8 plus the walk-forward slope (Phase 2g-4), which Paul has already named the next research candidate.
2. **ClubElo: not ready.** The API was down from two networks, and the mirror is ClubElo only up to June 2025, so validation and holdout would rest on someone else's provisional ratings. Before using it: (a) confirm from ClubElo's own documentation that no bookmaker odds enter the ratings (the independence rule); (b) rerun `scripts/feature_sources/clubelo.py` when the API is back, which tries the API first; (c) review the name matches. The likely gain is mainly cross-league strength for UCL/UEL (CE3n). On domestic matches C8 already carries an Elo term.
3. **Lineups and missing players: not backtestable.** No source here gives a history of injured or suspended players known before kickoff. Confirmed XIs do exist back to 2016/17 on ESPN, but they appear about an hour before kickoff, while the pipeline's last observation is a median 3 h 10 min before. A lineup feature would therefore need later runs, not just data. Under the plan this is ESPN context, which can't be backtested: if pursued, it runs in shadow on live evidence.

## Detail

### 1. ClubElo

- API attempts are recorded in `clubelo.json` (`api_attempt`). soccerdata reports `ConnectionError: Could not download http://api.clubelo.com/2026-11-19` after 5 retries.
- Mirror: 273,972 rows, 984 clubs, 19 countries (AUT, BEL, DEN, ENG, ESP, FIN, FRA, GER, GRE, ITA, NED, NOR, POL, POR, ROM, RUS, SCO, SWE, TUR).
- Domestic clubs, 2015/16 on (269): 265 exact; close matches for review: Ankaragucu → Ankaraguecue, Yeni Malatyaspor → Malatyaspor; unmatched: Ajaccio GFCO (2015/16), Osmanlispor (2017/18). The mirror already uses football-data spellings, so this overstates what raw API names would give.
- European clubs (240): 120 linked to an eight-league club through the reviewed identities CE3n uses. Of the other 120: 61 matched automatically (all listed for review; wrong on review: Lokomotiv Moskva → "FC Moskva", gnk dinamo → "Dinamo Bucuresti", aris limassol → "Aris"), 59 unmatched. Most of the unmatched are from countries the mirror lacks (CZE, UKR, SUI, CRO, SRB, CYP, ISR, HUN, BUL, KAZ, AZE, BLR, MDA, SVN, SVK, ARM, LVA, IRL). A few are naming misses inside covered countries (AEK Athens, Union Saint-Gilloise, HJK, Torreense). The full list is in `data/feature_cache/clubelo/european_name_match.csv`.
- Earliest date: the mirror from 1 Jul 2000. ClubElo's own depth is not verified while the API is down.

### 2. Rest and congestion

- Features per team per match (`data/feature_cache/rest/rest_features.csv`, 61,852 domestic and 5,288 European team-matches): days since last match, matches in the previous 14 and 21 days, and last match a European away fixture. Only strictly earlier days count.
- ESPN audit (128 team-seasons, 4 per league in each of 2016/17, 2019/20, 2022/23 and 2024/25, fixed seed): 704 of 5,493 competitive matches are missing from the held data. The largest gaps are UEL 169 (all before 2020/21), domestic cups 403, Conference League and its qualifiers 58, UCL/UEL qualifiers 20, and Eredivisie European play-offs 17.
- Effect on league team-matches: days since last match differs 14.2% (mean 5.5 days off when it does), 14-day count 23.0%, 21-day count 29.8%, European-away flag 2.6%. For clubs in Europe that season: 23.2%, 36.2%, 45.8% and 6.4%. Seasons with UEL held (2022/23, 2024/25) are better: 11.7–11.8% against 16.5–17.2%.

### 3. Lineups

- ESPN history sample: 24 matches per season (3 per league), 2016/17 to 2025/26. Starters for both teams in every match, average bench of 8–10, no injury list.
- Pipeline evidence: every committed version of `football_output_v2/raw/all_leagues_predictions.csv` (102), taking each fixture's last observation before kickoff. ESPN never sets an explicit lineup-confirmed flag, so `compact_squads` never marks an XI as confirmed. The 11-starter rosters seen (14%) are ESPN's announced lineups, picked up when a run happened to fall inside the hour before kickoff.
