# C6R: C6 plus rest and congestion (23 Nov 2026)

**Outcome: not put forward for declaration.** The choice rule fixed in `docs/plan.md` Phase 2h before any figure was computed (commit 6b2c053fd) fails on (a) and (b). Offline only: nothing live changed, nothing was declared, and no harness file or config changed. No holdout match and no match played after 10 Oct 2026 was forecast, fitted or read: runs end at 16 Jan 2026.

| Choice rule condition | Result | Met? |
| --- | --- | --- |
| (a) Development: C6 minus C6R on AH all lines positive, 95% interval clear of zero | −0.00002 (−0.00052 to +0.00045), 6,959 fixtures, 106 weeks | no |
| (b) Validation: that point estimate not negative | −0.00082 (−0.00182 to +0.00016), 1,354 fixtures, 22 weeks | no |
| (c) Development: calibration v3 against C6 | slopes 1.001 / 1.036 (C6 1.020 / 1.052), no failing band | yes |

## Figures

C6 minus C6R (positive means C6R is better), week-resampled 95% intervals:

| Group | Development | Validation |
| --- | --- | --- |
| AH all lines | −0.00002 (−0.00052 to +0.00045) | −0.00082 (−0.00182 to +0.00016) |
| AH draw-sensitive | +0.00010 (−0.00046 to +0.00065) | −0.00088 (−0.00217 to +0.00044) |
| 1X2 | +0.00014 (−0.00052 to +0.00080) | −0.00099 (−0.00256 to +0.00062) |
| Over 1.5 | −0.00024 (−0.00055 to +0.00006) | +0.00003 (−0.00064 to +0.00066) |
| AH all, fixtures where a side had short rest or came from a European away match | −0.00014 (−0.00200 to +0.00161), 1,715 fixtures | −0.00232 (−0.00561 to +0.00052), 401 fixtures |

- Mean AH all log loss, development: C 0.71653, C6 0.71577, C6R 0.71579, M 0.69807. Against M, C6R is behind by the same margin as C6 (−0.01863 and −0.01863).
- Calibration slopes (home / away): development C6 1.020 / 1.052, C6R 1.001 / 1.036; validation C6 1.093 / 1.097, C6R 1.085 / 1.099. Both pass v2 and v3 in both periods; no band fails.
- Movement from C6: the largest 1X2 change averages 0.7 points on development (max 8.0) and 0.8 on validation (max 4.6).

## What the fit learned

- Coverage: every side of every development and validation match had an ESPN schedule (16,626 sides). 12.7% of sides on development had short rest; 4.3% came from a UEFA away match.
- Fitted windows: 39 of 59 on development (neutral, i.e. C6 exactly, until 2,000 earlier rows existed).
- Median coefficients on development (log goal rate per unit of feature): own short rest **+0.034**, own congestion **+0.016**, own European away −0.023; opponent's short rest **−0.022**, opponent's congestion **−0.030**, opponent's European away −0.021. Validation medians are similar.
- Reading: short rest and congestion carry the opposite sign to fatigue. A side with a crowded schedule scores slightly more and concedes slightly less than C expects. Those are the clubs in European and cup runs, i.e. stronger clubs, whose strength C's rates under-state (C6's slopes are above 1). So the features mostly soak up leftover team strength, which is why calibration improves a little and log loss does not. Only the European-away term points the fatigue way (−0.02 on own scoring), and it is small.

## Input

- `scripts/backfill_espn_schedules.py`: 1,673 club-seasons (eight leagues, 2016/17 to 2026/27), 1,761 requests, all answered, none failed. ESPN's team list ignores the season, so clubs come from its standings. Mapping: 1,623 by the reviewed resolver, 50 by the manual pairs in `espn_team_aliases.json` (16 clubs, each checked by hand); `espn_team_map.csv` lists every pair. The cache stores no result field.
- Checked against the football-data.co.uk league matches per club-season: equal except for the matchday after the football-data cache (8 Nov 2026), the Eredivisie play-offs, which ESPN files under the league, and 26 club-matches ESPN lacks (about 0.1%).
- Gaps ESPN cannot fill: no Turkish Cup or Super Cup, and no Portuguese League Cup or Super Cup.

## Files

`development.json` and `validation.json` (every figure above), `choice_rule.json`, `backfill_summary.json`, `espn_team_map.csv`, `espn_team_aliases.json`. Rebuild: `python scripts/backfill_espn_schedules.py`, then `python scripts/c6_rest_report.py --period development` and `--period validation` (each refuses to overwrite its own output).
