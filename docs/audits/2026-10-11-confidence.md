# Confidence audit: 11 October 2026

Audit performed 12 October 2026. Repository baseline inspected: `076c7e77c3c2f36a7fee189945ad10207cc403de`.

## Scope and provenance

All eight archived snapshots passed their recorded content hashes after exact local materialization. The analysis uses the first eligible pre-kickoff shortlist per fixture, following `performance_tracking.frozen_rows`. It does not substitute a later, better-looking selection. Original forecasts, odds, snapshots, model settings and qualification rules are unchanged.

Racing, Lecce and Hull first qualified in snapshot `bdc690a8c70643c9`, captured at 06:38:09 UTC on October 11 (generated 06:32:27). Elche and Crystal Palace first qualified in `a2cdead106b513fd`, captured at 10:46:00 UTC (generated 10:39:00). Both groups satisfy the required lead time. This is an aggregate of original selections from different snapshot commits, not a claim that all five came from the latest configuration.

The scores below were checked against public match reports on October 12. These are a separate audit, not imported into the football-data.org verified-results cache. The configured collector must still fetch and reconcile its own match IDs and update the production workbook after PR #22 is approved and merged.

## All archived fixtures on October 11

| Fixture | Final score | Evidence |
|---|---:|---|
| Crystal Palace–Nottingham Forest | 3–1 | [Sky Sports](https://www.skysports.com/football/crystal-palace-vs-nottingham-forest/report/559498) |
| Hull–Everton | 2–2 | [RTÉ](https://www.rte.ie/sport/results/soccer/premier-league/36781/results/) |
| Liverpool–Manchester City | 0–3 | [Sky Sports daily results](https://www.skysports.com/football-scores-fixtures/2026-10-11) |
| Elche–Celta Vigo | 0–0 | [LaLiga](https://www.laliga.com/en-CA/match/temporada-2026-2027-laliga-ea-sports-elche-cf-rc-celta-8) |
| Real Sociedad–Deportivo La Coruña | 3–2 | [Sky Sports daily results](https://www.skysports.com/football-scores-fixtures/2026-10-11) |
| Real Betis–Osasuna | 5–2 | [Sky Sports daily results](https://www.skysports.com/football-scores-fixtures/2026-10-11) |
| Racing Santander–Valencia | 2–2 | [Valencia CF](https://www.valenciacf.com/match-report-valencia-racing) |
| Köln–Mönchengladbach | 2–1 | [Sportschau](https://www.sportschau.de/live-und-ergebnisse/fussball/deutschland-bundesliga/ma12194167/1-fc-koeln_borussia-moenchengladbach/liveticker) |
| Freiburg–Schalke | 2–1 | [Sky Germany daily results](https://sport.sky.de/fussball/spielplan-ergebnisse/2026-10-11) |
| Como–Roma | 0–0 | [Reuters](https://www.reuters.com/sports/soccer/lazio-keep-pace-top-10-man-roma-earn-draw-como-milan-held-by-sassuolo-2026-10-11/) |
| Lazio–Monza | 3–1 | [Reuters](https://www.reuters.com/sports/soccer/lazio-keep-pace-top-10-man-roma-earn-draw-como-milan-held-by-sassuolo-2026-10-11/) |
| Lecce–Bologna | 1–2 | [Bologna FC](https://www.bolognafc.it/en/lecce-1-2-bologna/) |
| Sassuolo–Milan | 1–1 | [Reuters](https://www.reuters.com/sports/soccer/lazio-keep-pace-top-10-man-roma-earn-draw-como-milan-held-by-sassuolo-2026-10-11/) |
| Cagliari–Juventus | 1–1 | [Reuters](https://www.reuters.com/sports/soccer/lazio-keep-pace-top-10-man-roma-earn-draw-como-milan-held-by-sassuolo-2026-10-11/) |
| Nice–Strasbourg | 2–1 | [AFP/NAMPA](https://www.nampa.org/text/23037212) |
| Rennes–Auxerre | 4–1 | [AFP/NAMPA](https://www.nampa.org/text/23037212) |
| Troyes–Marseille | 0–2 | [AFP/NAMPA](https://www.nampa.org/text/23037212) |

## Original shortlist

Probabilities are percentages. Adjusted confidence is the archived `rank_probability` used for grading, after the calibration deduction.

| Fixture | Market | Tier | Raw DC | After 1X2 reweighting | Adjusted confidence | Bookmaker reference | Odds | Outcome |
|---|---|---|---:|---:|---:|---:|---:|---|
| Racing–Valencia | Over 1.5 | PROVISIONAL | 89.97 | 89.95 | 89.95 | 81.86 | 1.24 | Won |
| Lecce–Bologna | Under 3.5 | PROVISIONAL | 83.63 | 83.65 | 79.64 | 77.10 | 1.28 | Won |
| Hull–Everton | Under 3.5 | PROVISIONAL | 90.00 | 90.29 | 83.35 | 74.42 | 1.32 | Lost |
| Elche–Celta | Over 1.5 | STRICT | 80.22 | 80.14 | 80.14 | 74.56 | 1.35 | Lost |
| Palace–Forest | Under 3.5 | PROVISIONAL | 76.26 | 76.21 | 75.51 | 71.09 | 1.39 | Lost |

At one simulated unit per selection: 2 wins / 5 = **40%**, profit **−2.48 units**, ROI **−49.6%**. STRICT: 0/1 and −1 unit. PROVISIONAL: 2/4 and −1.48 units (−37% ROI). These are simulated returns at archived quotes, not evidence of executed bets.

## Confidence comparison on the same five selections

Brier score is the mean of `(probability - outcome)^2`, where outcome is 1 for a winning selection and 0 otherwise; lower is better.

| Estimate | Mean confidence | Brier |
|---|---:|---:|
| Raw Dixon–Coles | 84.01% | 0.41438 |
| After 1X2 market reweighting | 84.05% | 0.41500 |
| After calibration deduction | 81.72% | 0.39173 |
| Exact-market bookmaker reference | 75.81% | 0.34012 |

The calibration deduction helped this batch; bookmaker references scored better still. This is descriptive evidence from only five selected fixtures, not a statistically reliable model ranking or proof of persistent miscalibration.

## Findings

1. **The blend is not a direct goal-market blend.** `FootballValuePipelineV2._predict_row` blends home/draw/away probabilities and calls `reweight_matrix_to_1x2`. Goal-market probabilities are recomputed from that matrix. Exact Over 1.5, Under 3.5 and BTTS bookmaker probabilities enter value metrics and shortlist checks, but not a direct 50/50 goal-market blend. Earlier descriptions implying otherwise were too broad. Hull is the clearest example: 90.00% raw, 90.29% after reweighting, against 74.42% market reference.

2. **Four picks were already flagged as provisional.** Hull and Racing lacked sufficient high-confidence history. Palace carried a high-confidence overestimation flag plus an adjusted-probability shortfall. Lecce missed the adjusted +3% EV threshold. These are not four failures of the STRICT policy. Elche was the only STRICT selection.

3. **Exact-market references exist for all five.** Archived selected and opposite odds are present for the correct goal lines, with 3–5 bookmakers per market. No missing-market substitution was found for these selections.

4. **Team mapping was plausible.** All five matched expected team identities, with minimum name scores of 90–100. This checks archived identities, not every upstream provider record.

5. **Some quoted prices were older than the snapshot.** Racing/Lecce/Hull quotes were about 0.5–1.6 minutes before generation; Elche/Palace selected quotes were about 109–110 minutes before generation. All predated kickoff. That age deserves monitoring and means quote availability at execution is not established.

6. **Goal estimates explain the high confidence, but do not prove the estimates were sound.** Hull's archived home/away lambdas were 1.086/0.658 (1.745 total); Elche's were 1.587/1.412 (2.998 total). The realised totals were four and zero. A single match cannot identify whether the issue is team-strength estimation, dispersion, changing form or ordinary variance.

7. **Publishing failed independently of prediction fitting.** Run 38146259366 attempt 2 collected 3 shortlist grades and 9 full-fixture grades, then hit conflicts in generated reports. PR #22 replaces rebasing with regeneration from latest main in a separate worktree, preserves snapshot bytes and retries bounded concurrent updates.

## Next steps and limits

- Approve and merge PR #22, then verify its newly triggered reporting run publishes all available provider-verified results and Excel output. Do not rerun the old failed job expecting it to use the repair.
- Keep the baseline, archived forecasts and thresholds unchanged. Use simulated stakes; treat PROVISIONAL as research observations.
- Continue daily forward grading and separate tier, market and league comparisons. Compare original raw, reweighted and calibrated forecasts with matching bookmaker references.
- Test direct goal-market blending or other changes as separately versioned experiments with chronological validation and later forward comparisons. Do not choose a weight to optimise these five results.
- This audit did not refit models or establish that every historical training file was current at every original prediction. It does not establish future profitability.
