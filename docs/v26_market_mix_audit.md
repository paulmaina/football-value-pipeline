# v26 market-mix audit: why the shortlist is mostly Asian handicap

Policy `48h-zero-tolerance-ev05-no-loss75-corners-v26`. Investigation only: no code, thresholds or production settings were changed. Audit date 2026-10-27, branch `chore/v26-market-mix-audit` from `main` at `5e5e800ab`.

## Summary

- **The Asian handicap (AH) tilt is structural.** The 75% adjusted no-loss floor rejects every 1X2, goal-totals, Corners and minus-handicap candidate. Each fixture also offers up to about 24 AH lines, and only plus lines can reach 75% no-loss at a positive EV. In replays of v26 on 11 frozen runs, 56 of 64 picks (88%) are AH, 37 of them at +1.50 or deeper. v22 gives the same mix (91% AH). The EV floor change from 1.0% to 0.5% and the zero risk tolerance barely matter.
- **v26 picks are the lines where the model disagrees most with Pinnacle.** Across all pre-#107 fixtures, the model's break-even win share sits above Pinnacle's no-vig share, and the gap grows with depth: +2.9 pp at +1.00, +4.1 pp at +1.50, +7.7 pp at +2.00, +9.2 pp at +2.50. Selected picks average +8 to +10 pp.
- **That gap is tied to a missing totals anchor that PR #107 fixed.** Every v26 production pick was made on a fixture with `NOT_ANCHORED_NO_PINNACLE_OU25_QUOTE`. Earlier runs used the legacy profile, which has no anchor at all. After #107, the same Serie A fixtures are anchored with goal-rate scales of ×1.14–1.20, and their deep-plus gap shrinks or disappears (Roma–Cagliari away +2.00: +5.9 pp → +2.6 pp). The one post-#107 run produced no eligible AH candidates.
- **The evidence on whether the model or Pinnacle is right is mixed:**
  - Walk-forward history (legacy profile) shows the un-anchored model's deep-plus no-loss calibrated against outcomes: heavy underdogs at +2.00, 84.7% predicted vs 85.0% observed, n = 709.
  - Forward grades favour the picks: 14 of 15 deep-plus picks avoided a loss, from a single round of fixtures.
  - CLV against Pinnacle's fair close is negative: −1.6% on deep-plus candidates. The close moves toward the model on only about 16% of the gap.
- **Verdict: too early to call it edge.** The tilt mostly reflects the selection rules plus a model-vs-Pinnacle disagreement in deep-margin tails that #107 largely removed. It is not demonstrated overconfidence against outcomes either. Treat v26's AH concentration as unproven until post-#107 picks build a graded and CLV record.

## Data and method

| Source | What it gives |
|---|---|
| 13 git commits with `football_output_v2/raw/` from 21–27 Oct | Frozen predictions, per-league `*_goal_market_validation.json`, execution policy and the production shortlist for each run |
| `performance/snapshots/*` | The two archived v26 snapshots (`61fd07517a6d`, `be93fe1f5e1c`) |
| `performance/clv_report/candidates.csv` | Pinnacle fair-close CLV for 390 AH candidate rows |
| `performance/verified_results.json` | Final scores for grading |
| `.football_cache/*_{E0,SP1,D1,I1,F1,N1,P1,T1}.csv` | Walk-forward history for Q4 |

- **Replays.** v22, v25 and v26 were each rebuilt with the current `asian_handicap.build_shortlist` on 11 frozen runs, using each run's own reliability evidence, execution policy and `generated_at_utc`. On all 8 runs whose production policy was v22, v25 or v26, the replay reproduced the production shortlist exactly. The 21 Oct v20 run was excluded: its frozen execution policy has a non-zero risk tolerance, which v22 and v26 refuse.
- **Snapshots vs runs.** Only two v26 runs were archived as snapshots. The other two v26 runs (25 Oct 16:27 and 27 Oct 09:50) were local runs committed in "Include model training data and outputs" and never archived.
- **Model profile.** Runs before 25 Oct 16:27 have no `model_version` column, so they are the legacy profile (`dc-blend50-tuned-half-life-v1`, no totals anchor). Later runs are `dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2`.
- **"Candidate"** means a row that passed every gate (`NOT_SELECTED` or `SHORTLISTED`). "Evaluated" means every row scored.
- **Scripts** are in the session scratchpad, not the repo: `replay.py`, `counterfactual.py`, `ah_vs_pinnacle.py`, `backtest_ah.py`, `bt_analysis.py`.

## 1. Candidates and picks by market type

### All 11 runs: v26 vs v25 vs v22 on the same inputs

| Market group | v22 candidates | v22 picks | v25 candidates | v25 picks | v26 candidates | v26 picks |
|---|---:|---:|---:|---:|---:|---:|
| 1X2 | 0 | 0 | 224 | 28 | 0 | 0 |
| Double chance | 5 | 5 | 599 | 47 | 8 | 8 |
| AH minus | 0 | 0 | 1,369 | 0 | 0 | 0 |
| AH level (0.00) | 1 | 0 | 320 | 0 | 1 | 0 |
| AH +0.25 to +1.25 | 32 | 15 | 1,068 | 7 | 37 | 19 |
| **AH +1.50 and deeper** | 86 | **34** | 301 | 7 | 90 | **37** |
| Goal totals | 0 | 0 | 72 | 19 | 0 | 0 |
| Corners | 0 | 0 | 228 | 7 | 0 | 0 |
| **Total** | 124 | 54 | 4,181 | 115 | 136 | 64 |
| **AH share of picks** | | **91%** | | **12%** | | **88%** |

v26 picks by exact line: +1.00 ×17, +1.25 ×2, +2.00 ×33, +2.25 ×2, +3.00 ×2. v22 is almost identical: +1.00 ×13, +1.25 ×2, +2.00 ×30, +2.25 ×2, +3.00 ×2.

v25's candidate counts aren't comparable to v22/v26. v25 uses v23's win-probability gates with no no-loss floor, so both sides of every handicap qualify. Its per-group cap of 2 then limits AH to at most 2 picks per run. v25 found no AH candidates at all on the three v22-era runs, because those inputs lack the `asian_handicap_win` evidence it needs.

### Per run: v26 picks (production runs in bold)

| Run (UTC) | Production policy | Fixtures | DC | AH +0.25..+1.25 | AH ≥ +1.50 | Total | v22 total | v25 total |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| 10-22 10:58 | v22 | 103 | 1 | 0 | 1 | 2 | 2 | 7 |
| 10-22 15:07 | v22 | 106 | 0 | 2 | 5 | 7 | 6 | 12 |
| 10-23 14:36 | v22 | 94 | 1 | 4 | 7 | 12 | 10 | 12 |
| 10-23 16:24 | v23 | 94 | 2 | 5 | 4 | 11 | 8 | 14 |
| 10-24 14:22 | v24 | 31 | 1 | 3 | 5 | 9 | 9 | 14 |
| 10-24 14:50 | v24 | 45 | 2 | 3 | 6 | 11 | 10 | 14 |
| 10-25 10:24 | v25 | 45 | 1 | 2 | 5 | 8 | 6 | 16 |
| **10-25 16:27** | **v26** | 21 | 0 | 0 | 1 | **1** | 1 | 10 |
| **10-26 11:01** | **v26** | 31 | 0 | 0 | 2 | **2** | 1 | 6 |
| **10-26 11:45** | **v26** | 25 | 0 | 0 | 1 | **1** | 1 | 2 |
| **10-27 09:50** | **v26** | 15 | 0 | 0 | 0 | **0** | 0 | 8 |

The four v26 production picks, all AH +2.00 from Pinnacle:

| Fixture | Line | Odds | Run(s) |
|---|---|---:|---|
| Barcelona – Real Madrid | Away +2.00 | 1.36 | 10-25 16:27 |
| Santa Clara – Benfica | Home +2.00 | 1.36, then 1.46 | 10-26 11:01 and 11:45 |
| AS Roma – Cagliari | Away +2.00 | 1.48 | 10-26 11:01 |

## 2. Which v26 rule causes the mix

### Counterfactuals: v26 with one rule changed, same 11 runs

| Variant | 1X2 | DC | AH ≥ +1.50 | AH +0.25..+1.25 | AH other | Totals | Corners | Picks | AH share |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| v26 as is | 0 | 8 | 37 | 19 | 0 | 0 | 0 | 64 | 88% |
| EV floor +1.0% (v22 + Corners) | 0 | 5 | 34 | 15 | 0 | 0 | 0 | 54 | 91% |
| EV floor 0% | 0 | 11 | 41 | 16 | 0 | 0 | 0 | 68 | 84% |
| EV floor +2.0% | 0 | 4 | 27 | 13 | 0 | 0 | 0 | 44 | 91% |
| No-loss floor 70% | 3 | 9 | 41 | 19 | 2 | 3 | 2 | 79 | 78% |
| No-loss floor 65% | 3 | 9 | 41 | 20 | 4 | 3 | 3 | 83 | 78% |
| No-loss floor 60% | 3 | 9 | 42 | 21 | 5 | 3 | 6 | 89 | 76% |
| Risk tolerance 2 pp | 0 | 8 | 37 | 19 | 0 | 0 | 0 | 64 | 88% |
| Risk tolerance 5 pp | 0 | 8 | 37 | 19 | 0 | 0 | 0 | 64 | 88% |
| Risk tolerance 100 pp (max EV per fixture) | 0 | 8 | 34 | 22 | 0 | 0 | 0 | 64 | 88% |

### In-window v26 rejections by group

| Group | Rows | Fails 75% floor | Fails EV floor | Blocked by the floor alone | Candidates |
|---|---:|---:|---:|---:|---:|
| 1X2 | 530 | 100% | 75% | 108 | 0 |
| Double chance | 795 | 74% | 87% | 68 | 8 |
| Goal totals | 265 | 54% | 97% | 4 | 0 |
| Corners | 234 | 100% | 72% | 65 | 0 |
| AH minus | 2,961 | 100% | 94% | 164 | 0 |
| AH +0.25 to +1.25 | 1,887 | 83% | 83% | 202 | 37 |
| AH +1.50 and deeper | 1,074 | 49% | 63% | 157 | 90 |

Many Double chance, totals and 1X2 rows also fail the reliability and blend gates.

### Answer: the 75% floor, combined with the AH line ladder and no per-market quota

The EV floor and the risk tolerance are not the cause.

1. **The 75% adjusted no-loss floor** is what excludes the other markets.
   - The floor is set at [asian_handicap.py:38](../asian_handicap.py#L38) (`MIN_ADJUSTED_NO_LOSS = .75`) and [shortlist_quote_policy.json:9](../shortlist_quote_policy.json#L9), and applied at [asian_handicap.py:477-482](../asian_handicap.py#L477-L482). Corners get the same floor at [no_loss_corners_shortlist.py:41-42](../no_loss_corners_shortlist.py#L41-L42).
   - For 1X2, goal totals and Corners, the adjusted no-loss probability is the win probability minus a calibration penalty ([asian_handicap.py:386-389](../asian_handicap.py#L386-L389)). Reaching 75% needs short prices, around 1.25 to 1.30, where positive EV is rare.
   - Lowering the floor to 60–70% admits some 1X2, totals and Corners picks, but AH still makes up 76–78% of picks.
2. **The AH ladder gives every fixture many tries.**
   - [asian_handicap.py:40](../asian_handicap.py#L40) allows quarter lines from −3 to +3, and every quoted line is scored ([asian_handicap.py:395-474](../asian_handicap.py#L395-L474)).
   - Moving to deeper plus lines raises no-loss steadily, so on most fixtures some plus line clears 75%. Only one or two Double Chance lines exist per fixture.
   - AH risk is `max(blended, raw) any-loss + penalty` ([asian_handicap.py:452-453](../asian_handicap.py#L452-L453)). The penalties on deep lines are small, 0.00 to 0.03, so they don't hold deep lines back (see section 4).
3. **No per-market quota or cap.** [no_loss_corners_shortlist.py:76-84](../no_loss_corners_shortlist.py#L76-L84) pools all candidates and takes the first 12 after ranking.
4. **Zero risk tolerance is not the driver.**
   - Within a fixture, [asian_handicap.py:250-262](../asian_handicap.py#L250-L262) keeps only the lowest-risk candidate, which is always the deepest plus line that clears EV.
   - Most fixtures have only one or two candidates, so widening the tolerance, even to "max EV per fixture", swaps a few +2.00 picks for +1.00 or +1.25 and leaves the AH share at 88%.
5. **The EV floor, 0.5% vs 1.0%, is not the driver.**
   - Set at [no_loss_corners_shortlist.py:19](../no_loss_corners_shortlist.py#L19) and passed into v22 at [no_loss_corners_shortlist.py:54-55](../no_loss_corners_shortlist.py#L54-L55).
   - It only changes how many picks pass: 54 at 1.0% vs 64 at 0.5%. The AH share stays at 88–91%.

The EV floor still acts as a filter on which AH lines survive. Most deep-plus prices are 1.15–1.60. At those prices the floor is only cleared when the model's no-loss probability is well above the price-implied one, which happens on the lines where the model disagrees most with Pinnacle (section 3).

## 3. Model vs Pinnacle no-vig on the same line

**Method.**
- **Primary metric: break-even win share.** Settlement can be full win, half win, push, half loss or full loss, so I compare `(full win + ½ half win) / (that + full loss + ½ half loss)`. That is 1 / fair price, which is what a two-way no-vig price measures. It works the same way for half, whole and quarter lines.
- **No-vig** is multiplicative normalisation of Pinnacle's pair at the exact line.
- **Win/push/loss split.** Where Pinnacle also quotes the neighbouring half lines, I derived Pinnacle's split from that ladder. For example, +2.00 uses the +1.50 and +2.50 quotes.
- **Model** is the blended goal-margin distribution, before the calibration penalty.

### All pre-#107 evaluated AH rows quoted by Pinnacle

This shows a systematic difference that affects every fixture, not only the selected ones.

| Line | Rows | Model share | Pinnacle share | Mean gap | Model higher in |
|---|---:|---:|---:|---:|---:|
| +0.50 | 421 | 0.544 | 0.539 | +0.5 pp | 56% |
| +1.00 | 300 | 0.617 | 0.588 | +2.9 pp | 69% |
| +1.50 | 190 | 0.643 | 0.602 | +4.1 pp | 75% |
| +1.75 | 142 | 0.697 | 0.645 | +5.2 pp | 77% |
| +2.00 | 99 | 0.756 | 0.679 | +7.7 pp | 85% |
| +2.25 | 65 | 0.771 | 0.693 | +7.9 pp | 85% |
| +2.50 | 38 | 0.771 | 0.679 | +9.2 pp | 95% |
| +2.75 | 9 | 0.838 | 0.701 | +13.7 pp | 100% |
| +3.00 | 4 | 0.932 | 0.737 | +19.5 pp | 100% |

Minus lines mirror these numbers. Average gap by depth: deep plus +6.1 pp (547 rows), +0.25 to +1.25 +1.4 pp, level 0.0 pp. The model's goal-margin distribution has thinner tails than Pinnacle's: it gives fewer multi-goal wins to the favourite.

### v26 picks (replays, 56 picks, 48 with a Pinnacle quote at the exact line)

| Line | Picks | With Pinnacle quote | Model share | Pinnacle share | Mean gap |
|---|---:|---:|---:|---:|---:|
| +1.00 | 17 | 16 | 0.775 | 0.678 | +9.6 pp |
| +1.25 | 2 | 2 | 0.826 | 0.744 | +8.2 pp |
| +2.00 | 33 | 28 | 0.797 | 0.709 | +8.9 pp |
| +2.25 | 2 | 2 | 0.766 | 0.730 | +3.5 pp |
| +3.00 | 2 | 0 | — | — | no Pinnacle quote |

Counting each fixture-line once (25 unique picks): +1.00 averages +8.7 pp (7 with a quote) and +2.00 averages +8.2 pp (10 with a quote).

### Win / push / loss where Pinnacle's ladder allows the split

| Line | Picks | Model win / push / loss | Pinnacle win / push / loss | Model no-loss | Pinnacle no-loss |
|---|---:|---|---|---:|---:|
| +1.00 | 8 | 52.7 / 26.2 / 21.1 | 45.0 / 23.4 / 31.6 | 78.9% | 68.4% |
| +2.00 | 9 | 57.7 / 20.8 / 21.5 | 50.4 / 20.5 / 29.1 | 78.5% | 70.9% |

Push probabilities agree closely. The disagreement is almost entirely win vs loss: Pinnacle gives the favourite a much better chance of winning by more than the line.

The calibration penalty doesn't close the gap. Selected picks carry adjusted no-loss probabilities only 0–3 pp below the unpenalised model, against an 8–10 pp gap to Pinnacle.

Multiplicative de-vig gives the short-priced side slightly less than power or Shin de-vig would. The pair margins here are about 3%, so moving the whole margin to the long side would lower the gap by at most about 2 pp. It would not remove it.

## 4. Predicted vs observed no-loss on deep plus lines (graded history)

### Walk-forward history, legacy-style profile

**Set-up.** `backtest_league` with `min_train=500`, `step_days=56`, run offline from cached football-data.co.uk CSVs.
- Profile: market weight 0.5, no totals anchor, no shots, no BBS. Half-life fixed at 240 days, not tuned per league as in the original legacy profile.
- 8 domestic leagues, 1,676 matches, 2025-12-30 to 2026-10-26.
- No-loss is scored on full-time scores using the pipeline's own settlement function.

**Predicted 70–95% no-loss, lines +1.50 and deeper, by predicted band.** This is the band v26 picks from.

| Predicted band | Rows | Predicted | Observed | Gap (pred − obs) | Observed 95% CI |
|---|---:|---:|---:|---:|---|
| 70–75% | 875 | 72.7% | 73.5% | −0.8 pp | 70.5–76.3% |
| 75–80% | 1,235 | 77.8% | 82.6% | −4.8 pp | 80.4–84.6% |
| 80–85% | 1,946 | 82.6% | 84.1% | −1.5 pp | 82.4–85.6% |
| 85–90% | 3,007 | 87.7% | 88.0% | −0.3 pp | 86.7–89.1% |
| 90–95% | 4,849 | 92.7% | 93.2% | −0.5 pp | 92.5–93.9% |

Rows repeat across lines that share a no-loss event. For example, +1.50 and +1.75 have the same no-loss event, as do +2.00, +2.25 and +2.50.

**Heavy underdogs** (model win probability under 25%) at +2.00, predicted 75–95%: n = 709, 84.7% predicted vs 85.0% observed (95% CI 82.2–87.5%).

By win-probability band at +2.00:

| Underdog's win probability | n | Predicted | Observed |
|---|---:|---:|---:|
| 0–15% | 327 | 71.0% | 71.9% |
| 15–25% | 588 | 85.5% | 86.7% |
| 25–35% | 692 | 92.0% | 91.3% |

**By league (deep plus, predicted 70–95%).** Seven leagues are within 3 pp, mostly under-confident. Two are over-confident:
- Eredivisie: 86.3% predicted vs 82.4% observed (+3.9 pp).
- Süper Lig: +1.1 pp.

**The model's deep-plus no-loss probabilities are not overconfident against outcomes, unconditionally.** But a model and Pinnacle that disagree by 7 pp on the same fixtures cannot both be calibrated. On these heavy-underdog +2.00 rows, a value 7 pp lower (about 78%) would sit outside the observed CI. This history therefore favours the model's tails. Three caveats limit how much that is worth:
1. **It's unconditional.** It cannot show the model is right on the fixtures where it disagrees most with Pinnacle, which are exactly the fixtures v26 picks.
2. **No historical Pinnacle check is possible.** The 2025/26 football-data.co.uk files carry Pinnacle AH prices on only 3% of rows, leaving 4 deep main-line cases.
3. **Inputs differ from live.** The backtest's 1X2 blend reference comes from football-data.co.uk, not from live Odds API quotes, and it uses the legacy profile, not production-v2.

**The pipeline's own AH audit is weak evidence for deep lines.** The `asian_handicap` audit in each `*_goal_market_validation.json` ([asian_handicap.py:209-247](../asian_handicap.py#L209-L247)) scores every match at every line. For Home +2.00, that pool is mostly ordinary fixtures where no-loss is about 90–95%. It passes easily (audit overconfidence −4 pp to +3 pp) and produces the small penalties above, but says little about the underdog cases v26 selects.

### Forward graded picks

- **v22 production AH picks** (shortlist_grades.csv): 6 graded, 6 avoided a loss. Deep plus: Augsburg, Lazio, Aston Villa and Stuttgart all won at +2.00.
- **v26 replay picks, one per fixture-line:** 24 of 25 are graded. Observed no-loss is 91.7% vs 84.6% predicted, +4.4 units flat stake.
  - Deep plus: 15 picks, 14 avoided a loss (93.3% vs 85.4% predicted, +2.55 units).
  - The one loss was Athletic Bilbao 4–0 Getafe, Getafe +2.00 at 1.21.
- **v26 production picks:**
  - Barcelona – Real Madrid away +2.00: won 1–2.
  - Santa Clara – Benfica home +2.00: won 1–2. `verified_results.json` has the result; the closing-odds file still shows it as unverified.
  - Roma – Cagliari: kicks off 27 Oct at 19:45 UTC.

All of these fixtures fall in one round, 23–26 Oct, and outcomes within a round are correlated. 14 of 15 is consistent with both the model (85%) and Pinnacle (about 77%).

## 5. CLV for v26 Asian handicap picks

CLV here is entry odds × Pinnacle fair-close probability − 1, as in [clv_report.py](../clv_report.py). For whole and quarter lines, that probability is the two-way no-vig share. The closing-odds records themselves give no fair probability for split settlement (`split_settlement_fair_probability_unavailable`), so only price CLV is available from them.

### v26 production picks

| Pick | Entry | Pinnacle close | Price CLV |
|---|---:|---:|---|
| Santa Clara +2.00 (11:45 run) | 1.46 | 1.42 | +2.8% |
| Santa Clara +2.00 (11:01 run) | 1.36 | 1.42 | −4.2% |
| Roma – Cagliari away +2.00 | 1.48 | not yet | close not captured yet |
| Barcelona – Real Madrid away +2.00 | 1.36 | none | local run, never archived |

### v26 replay picks with a Pinnacle fair close (one per fixture, 10)

| Pick | CLV |
|---|---:|
| Celta +1.00 | +7.7% |
| Como +2.00 | +1.5% |
| Santa Clara +2.00 | +0.8% |
| Stuttgart–Gladbach away +2.00 | −0.2% |
| Hull +1.00 | −1.1% |
| Rayo–Elche away +1.00 | −1.3% |
| Bilbao–Getafe away +2.00 | −2.8% |
| Paderborn–HSV away +1.00 | −3.9% |
| Lazio–Parma away +2.00 | −5.2% |
| Augsburg–Union away +1.00 | −10.9% |
| **Mean** | **about −1.5%** |

3 of the 10 are positive.

### All AH candidates in the CLV report (21–26 Oct)

| Depth | Entry book | Rows | Fixtures | Mean CLV vs fair close | Positive | Same-book price CLV |
|---|---|---:|---:|---:|---:|---:|
| ≥ +1.50 | Pinnacle | 55 | 15 | −3.2% | 29% | −0.7% |
| ≥ +1.50 | 1xBet | 20 | 13 | −3.3% | 30% | — |
| +0.25 to +1.25 | Pinnacle | 84 | 17 | −4.9% | 18% | −1.2% |
| minus | Pinnacle | 139 | 17 | −3.3% | 27% | +0.8% |

### Does Pinnacle close toward the model?

200 Pinnacle-entry rows could be matched to their entry no-vig share.

| Depth | Rows | Fixtures | Model − Pinnacle at entry | Pinnacle move to close | Move toward model | Median share of gap closed |
|---|---:|---:|---:|---:|---:|---:|
| ≥ +1.50 | 27 | 9 | +8.5 pp | +1.0 pp | 74% | 16% |
| +0.25 to +1.25 | 63 | 11 | +4.8 pp | −0.3 pp | 40% | — |
| minus | 90 | 11 | −5.9 pp | −0.1 pp | 50% | — |

On deep plus lines Pinnacle drifts the model's way, but only about a sixth of the gap. CLV is negative on average, and there are too few fixtures (9–17) for these numbers to be significant either way.

## 6. Before vs after the PR #107 merge

PR #107 merged at **2026-10-27 09:20:06 UTC** (`d02ecb8c0`).

| | Before | After |
|---|---|---|
| v26 production runs | 3: 10-25 16:27, 10-26 11:01, 10-26 11:45 | 1: 10-27 09:50 |
| v26 production picks | 4 (3 unique fixture-lines) | 0 |
| Archived v26 snapshots | 2 (`61fd07517a6d`, `be93fe1f5e1c`) | 0 (the post-merge run is local and not archived) |
| v26 replay picks | 64 over 10 runs | 0 over 1 run |
| v26 AH candidates | 128 | 0 |
| Totals anchor applied | 0–19% of fixtures per v2 run; never in legacy runs; every v26 production pick unanchored | 53% of fixtures (7 `ANCHORED_ALTERNATE`) |
| Model − Pinnacle gap, deep plus (Pinnacle-quoted rows) | +6.4 pp (529 rows, 61 fixtures) | −2.5 pp (18 rows, 6 fixtures) |
| Model − Pinnacle gap, +0.25 to +1.25 | +1.5 pp | −0.2 pp |

After #107, every in-window v26 row is rejected. The leading reasons are the 75% floor (242 of 272 rows) and the EV floor (195 rows). v25 would still pick 8: 2 DC, 2 AH +0.25..+1.25, 2 Corners, 1 1X2, 1 totals.

### Same fixtures, before (10-26 11:01) and after (10-27 09:50)

| Fixture / line | Before: model / Pinnacle | After: model / Pinnacle | Gap before → after |
|---|---|---|---|
| Roma–Cagliari away +2.00 | 0.714 / 0.655 | 0.664 / 0.638 | +5.9 → +2.6 pp |
| Roma–Cagliari away +2.50 | 0.778 / 0.726 | 0.737 / 0.715 | +5.2 → +2.2 pp |
| Torino–Como home +1.50 | 0.709 / 0.674 | 0.685 / 0.685 | +3.5 → 0.0 pp |
| Torino–Como home +1.75 | 0.775 / 0.735 | 0.747 / 0.746 | +4.0 → +0.1 pp |
| Sassuolo–Lazio home +1.00 | 0.691 / 0.709 | 0.672 / 0.688 | −1.8 → −1.6 pp |

The mechanism is visible in the prediction columns:
- Before #107 these fixtures were `NOT_ANCHORED_NO_PINNACLE_OU25_QUOTE`. The model's own over-2.5 probability was 0.46–0.52, against Pinnacle's no-vig of about 0.57–0.60.
- After #107 they are `ANCHORED_ALTERNATE`, with goal-rate scales of 1.14–1.20.
- Higher scoring rates widen the goal-margin distribution, which lowers deep-plus no-loss.

**Caveat.** The post-merge run also differs in other ways: it was a local run (Python 3.14, pandas 3.0.6), training data was refreshed in `9cac5681a`, and it is about 22 hours closer to kick-off. The same-fixture comparison controls for the fixture but not for these. With one run and 15 fixtures, all Serie A plus 5 others, the post-merge numbers are directional only.

## 7. How often Pinnacle quotes each AH line

These are unique (run, fixture, side, line) combinations offered by any book (Pinnacle or 1xBet) in the v26 replays. Plus and minus sides have the same coverage by construction.

| Line | Combinations offered | Pinnacle exact quote | v26 candidates (with Pinnacle) | v26 picks (with Pinnacle) |
|---|---:|---:|---:|---:|
| 0.00 | 802 | 73% | 1 (1) | 0 |
| ±0.25, ±0.50, ±0.75, ±1.25, ±1.75, ±2.25, ±2.75 | — | 100% (1xBet offers no quarter lines here) | 41 (41) | 4 (4) |
| ±1.00 | 395 | 76% | 22 (21) | 17 (16) |
| ±1.50 | 420 | 45% | 12 (11) | 0 |
| ±2.00 | 203 | 49% | 37 (31) | 33 (28) |
| ±2.50 | 137 | 28% | 13 (9) | 0 |
| ±3.00 | 54 | 7% | 2 (0) | 2 (0) |

- **Deep lines are not mostly selected where Pinnacle has no quote.** 48 of the 56 v26 replay picks, and all four production picks, are priced off Pinnacle's own quote at that line.
- **The other 8 picks are 1xBet fallbacks** at lines Pinnacle doesn't quote: +3.00 ×2, +2.00 ×5, +1.00 ×1. The fallback rule at [asian_handicap.py:486-490](../asian_handicap.py#L486-L490) never hid a cheaper Pinnacle price in this sample.
- **Every +3.00 pick is a 1xBet-only line.** There, the model's gap to Pinnacle's ladder is largest (+19.5 pp on the four Pinnacle-quoted rows), and there is no same-line sharp price to check against.
- **Pinnacle quotes deep whole and half lines (±1.50, ±2.00, ±2.50) less than half the time**, so the win/push/loss split from section 3 is possible for only 17 of 56 picks.

## 8. Conclusion and options

**Verdict: too early to tell, and the evidence leans toward an artefact of model inputs rather than proven edge.**

- **The tilt itself is explained by the rules, not by edge.** The 75% no-loss floor removes 1X2, totals, Corners and minus lines. The AH ladder gives every fixture many plus lines to try, and nothing caps any one market. v22 had the same tilt (91% AH). v26's lower EV floor didn't create it.
- **Within AH, v26 picks the lines where the model and Pinnacle disagree most.** That disagreement was systematic in pre-#107 inputs (+6 pp across all deep plus lines) and lines up with fixtures whose totals were never anchored to Pinnacle. Once #107 anchors the totals, the gap on the same fixtures mostly closes and v26 finds nothing.
- **It is not shown to be model overconfidence against outcomes.** The un-anchored legacy model's deep-plus no-loss is calibrated in walk-forward history (85.0% observed vs 84.7% predicted for heavy-underdog +2.00), and the forward picks have done well (14 of 15).
- **It is not shown to be edge either.** CLV against Pinnacle's fair close is negative (about −1.5% on picks, −3.2% on deep-plus candidates). Pinnacle moves only about 16% of the way toward the model. The forward sample is one round of fixtures.
- **What would settle it:** post-#107 v26 picks, graded and CLV-tracked over several rounds. If the post-#107 model keeps finding few or no deep-plus picks, the tilt was an input artefact. If deep-plus picks return with positive Pinnacle-fair CLV, it is more likely edge.

### Options (not implemented)

1. **Maximum model-vs-Pinnacle gap for AH.** Reject an AH line if the model's break-even share exceeds Pinnacle's no-vig share at that line by more than a set amount. Every selected pick here had a gap of +3.5 to +10 pp, so a 5 pp cap would have removed almost all of them. It is a blunt tool: it assumes Pinnacle is right.
2. **Require the totals anchor for goal-margin markets.** Only allow AH (and other margin-derived markets) when `totals_anchor_applied` is true. This targets the mechanism found here directly. The open follow-up on the O/U 2.5 alternate reference matters for how often that would be available.
3. **Require a Pinnacle quote at the exact line for deep lines.** For example, +1.50 or deeper only with a Pinnacle quote at that line, or with Pinnacle's neighbouring half lines. That removes 1xBet-only +3.00 picks with nothing to check against.
4. **Cap per market group.** For example, at most 4–6 AH picks out of 12, or at most half the shortlist. This limits concentration without judging which side is right. It would leave v26 with very few picks, since only 8 DC candidates exist over 11 runs.
5. **Conditional AH audit.** Calibrate the AH penalty on the probability band v26 actually uses (75–95% no-loss, underdog side) instead of on every match at every line. Today's unconditional pool produces near-zero penalties on deep lines.
6. **Shadow tracking before any change.** Keep v26, but log the counterfactual mixes (floor 70%, gap cap, anchor-required) per run with grades and CLV. Decide after a fixed post-#107 sample, for example 50 graded deep-plus picks across at least 6 rounds of fixtures.
7. **Archive every v26 production run as a snapshot.** Two of the four v26 runs (one before #107, the only one after) exist only as local commits, which limits this audit.
