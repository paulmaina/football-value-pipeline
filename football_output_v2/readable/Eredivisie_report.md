# Eredivisie — football model report

Fixtures in this report: **1**.

> Each match shows the two models the shortlists use, side by side, and the master's verdict on them: **Research** (the value shortlist's model, independent of bookmaker odds) and **Cagey** (the cagey tier's market view, built from Pinnacle's prices). Probabilities are model estimates, not guarantees. No probability here is blended or averaged. The production model (70% Pinnacle blend) is kept only as a benchmark at the end of this report.

## Quick reference

- **Research:** The value shortlist's model: team form, goal rates and xG, never bookmaker odds. Live research v5 (C6 grid) for domestic leagues and v6 (CE3n) for UCL/UEL, exactly as the forecast carries it.
- **Cagey:** The cagey tier's market view: Pinnacle's 1X2, O/U 2.5 and main AH line with the margin removed, plus the narrow-margin correction (D_pow2 for domestic leagues, D for UCL/UEL, D where D_pow2's power fit fails). Blank without Pinnacle 1X2 and O/U 2.5.
- **No-loss:** The chance a bet does not lose: a win, a half win or a refund (push) on that exact line.
- **Gap:** Research minus cagey no-loss on the same Pinnacle offer, in percentage points (the master's g). +4 or more: research too optimistic; -4 or less: research too pessimistic; -8 or less with cagey no-loss of 85% or more: flagged for inspection.
- **Cagey tier:** The master's market classes from the cagey no-loss: safe (75% or more), risky (below 50%), in between otherwise; fair price when the Pinnacle price is within its 2.70% margin of the cagey fair odds.
- **Best offer:** The fixture's master pick, or else the Pinnacle offer the master's own rule would choose for it (safe first, then chance of profit), shown with both views and the master's labels.
- **Expected goals:** A view's average goal expectation for each team, from its score grid. It is not a prediction that the team will score exactly that many goals.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-11-27 — FC Groningen vs Willem II Tilburg

Research leans **FC Groningen win** at **66.0%**. Cagey: no cagey grid: needs Pinnacle 1X2 and O/U 2.5 (no Pinnacle 1X2 or O/U 2.5 quote). Only one view is available.

**Fixture source:** football-data.org

### The two views

- **Research:** research v5, C6
- **Cagey:** unavailable: no cagey grid: needs Pinnacle 1X2 and O/U 2.5 (no Pinnacle 1X2 or O/U 2.5 quote)

| Measure | Research | Cagey |
| --- | --- | --- |
| FC Groningen win | 66.0% | — |
| Draw | 20.1% | — |
| Willem II Tilburg win | 13.9% | — |
| FC Groningen expected goals | 2.33 | — |
| Willem II Tilburg expected goals | 1.05 | — |
| Expected total goals | 3.38 | — |
| Most likely score | 2-1 | — |
| Most likely score probability | 10.0% | — |
| Over 1.5 | 85.4% | — |
| Under 1.5 | 14.6% | — |
| Over 2.5 | 65.5% | — |
| Under 2.5 | 34.5% | — |
| Over 3.5 | 44.0% | — |
| Under 3.5 | 56.0% | — |
| BTTS Yes | 59.8% | — |
| BTTS No | 40.2% | — |
| Double Chance 1X | 86.1% | — |
| Double Chance X2 | 34.0% | — |

### 5 most likely scorelines

| Rank | Research | Cagey |
| --- | --- | --- |
| 1 | 2-1 (10.00%) | — |
| 2 | 2-0 (9.19%) | — |
| 3 | 1-1 (9.02%) | — |
| 4 | 1-0 (7.87%) | — |
| 5 | 3-1 (7.64%) | — |

### No-loss on the quoted Pinnacle Asian handicap lines

_No Pinnacle Asian handicap quotes in this forecast._

### On the lists

- **Value shortlist:** no
- **Cagey tier:** no
- **Master shortlist:** no

### The master's verdict on every Pinnacle offer

_No Pinnacle offer of this match in the run's decision rows._

### Safest Asian handicap (cagey tier)

_no cagey grid: needs Pinnacle 1X2 and O/U 2.5 (no Pinnacle 1X2 or O/U 2.5 quote)._


---

## Benchmark (70% Pinnacle blend), display only

The production forecasting model blends 70% of Pinnacle's prices into its score grid, so it is neither independent research nor the cagey tier's market view. It is shown for comparison only: no list, probability or stake reads it, and its EV is not a recommendation.

- **Benchmark EV:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Probability edge:** Model probability minus the de-vigged market probability.

### Model context

| Item | Value |
| --- | --- |
| League | Eredivisie |
| Training matches | 1,647 |
| Training data through | 2026-11-22 |
| Model fit succeeded | Yes |
| Recency half-life (days) | 480 |
| Maximum goals per team in score matrix | 10 |
| Bookmaker margin-removal method | power |
| Market blending weight | 70.0% |

<details>
<summary>Technical model diagnostics</summary>

| Parameter | Value |
| --- | --- |
| Training seasons requested | 6 |
| Training seasons loaded | ['2122', '2223', '2324', '2425', '2526', '2627'] |
| Training sha256 | 6a6942c4484010b7ee31ba0d63440397e3d2574de9f7102f07acd6e30191f1e0 |
| Training as of utc | 2026-11-24T15:19:46.947987+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 0, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 0, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.'} |
| Bbs statistics model | {'status': 'NO_OBSERVATIONS'} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-11-24', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1647, 'tune_start_date': '2025-11-25', 'audit_start_date': '2026-05-26', 'training_shot_matches': 1341, 'tuning_matches': 189, 'audit_matches': 111, 'audit_matchdays': 39, 'selected_shrinkage': 40.0, 'selected_component': 'shots_on_target_and_total_shots', 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.6308826464450854, 'audit_candidate_poisson_score': 0.6224704282339654, 'audit_gain': 0.008412218211120037, 'audit_gain_lower95': -0.004701228080257648, 'audit_baseline_briers': [0.628450015796775, 0.10533193375569261, 0.29201483407538037, 0.2253102053487333], 'audit_candidate_briers': [0.6243811817352334, 0.10483815203633236, 0.28942699667427135, 0.2190901069387336], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum', 'bootstrap_lower95_not_positive']} |
| Optimizer objective | 1653.845 |
| Base scoring parameter | 0.310 |
| Home-advantage parameter | 0.165 |
| Dixon-Coles low-score adjustment | -0.068 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 25, 'matches': 1647, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-11-22'} |
| Training data health | {'training_end': '2026-11-22', 'days_since_latest_result': 2, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['football-data.org'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 0.00 |
| Excluded started fixtures | [] |
| Excluded unresolved team fixtures | [] |
| Additional event odds calls used before this league | 9.00 |
| Over 1 5 in window quote fixtures | 0 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 0.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 0.00 |
| Totals anchor fixtures | {'NOT_ANCHORED_NO_PINNACLE': 1} |
| Shot features applied fixtures | 0 |
| Goal rate features used | {'none': 1} |
| Legacy comparison status | {'None': 1} |
| Bbs statistics applied fixtures | 0 |
| Goal market validation | SKIPPED: not required by 48h-ah-price-edge-cagey-v28 |

</details>

### 2026-11-27 — FC Groningen vs Willem II Tilburg

The model's most likely 1X2 outcome is **FC Groningen win** at **68.2%**. Expected goals are 2.33 for FC Groningen and 0.93 for Willem II Tilburg (3.26 combined). The most likely exact score is 2-0 at 10.4%. Goal-market probabilities: at least one goal: 95.6%; Over 2.5 goals: 63.3%; Under 3.5 goals: 58.9%; Double Chance 1X: 87.2%; Double Chance X2: 31.8%; Double Chance 12 (either team wins): 81.0%; Under 4.5 goals: 76.9%; BTTS Yes (both teams score): 55.2%; BTTS No (at least one team does not score): 44.8%.

| Outcome | Benchmark probability | Benchmark fair odds |
| --- | --- | --- |
| FC Groningen win | 68.2% | 1.47 |
| Draw | 19.0% | 5.26 |
| Willem II Tilburg win | 12.8% | 7.79 |

| Measure | Benchmark estimate |
| --- | --- |
| FC Groningen expected goals | 2.33 |
| Willem II Tilburg expected goals | 0.93 |
| Expected total goals | 3.26 |
| Over 0.5 | 95.6% |
| Under 0.5 | 4.4% |
| Over 1.5 | 84.2% |
| Under 1.5 | 15.8% |
| Over 2.5 | 63.3% |
| Under 2.5 | 36.7% |
| Over 3.5 | 41.1% |
| Under 3.5 | 58.9% |
| Over 4.5 | 23.1% |
| Under 4.5 | 76.9% |

| Rank | Score | Benchmark probability |
| --- | --- | --- |
| 1 | 2-0 | 10.42% |
| 2 | 2-1 | 9.69% |
| 3 | 1-1 | 8.87% |
| 4 | 1-0 | 8.37% |
| 5 | 3-0 | 8.11% |

<details>
<summary>Additional technical details (forecast row)</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-27T19:00:00+00:00 |
| Fixture id | fdorg:558820 |
| Matched home-team name | Groningen |
| Matched away-team name | Willem II |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| Dc lambda home | 2.3333 |
| Dc lambda away | 0.9294 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 55.2% |
| P btts no | 44.8% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 22.77 |
| Fair Over 1.5 odds | 1.19 |
| Fair Under 1.5 odds | 6.35 |
| Fair Over 2.5 odds | 1.58 |
| Fair Under 2.5 odds | 2.73 |
| Fair Over 3.5 odds | 2.43 |
| Fair Under 3.5 odds | 1.70 |
| Fair Over 4.5 odds | 4.34 |
| Fair Under 4.5 odds | 1.30 |
| Score matrix json | [[0.04391242715806283,0.02995113485309907,0.016534501848588283,0.005122449276505406,0.001190215170858522,0.00022123981345239748,3.42704525582724e-05,4.550190777360758e-06,5.28624667730234e-07,5.458995320924139e-08,5.073650277737587e-09,4.2868239612647563e-10,3.320184439176433e-11,2.3737045585602273e-12,1.5758193697872147e-13,9.763892332031647e-15,5.67166806000145e-16,3.1007709764473426e-17,1.601050356235143e-18],[0.08369766916978826,0.08865109185962099,0.03858060497288277,0.011952412829864456,0.002777175977850545,0.0005162275782629635,7.996459793589213e-05,1.0617139514705017e-05,1.2334607762230745e-06,1.2737688982348846e-07,1.1838548202325399e-08,1.0002615340477579e-09,7.74711723751841e-11,5.5386584207229815e-12,3.676921456183355e-13,2.2782474882485468e-14,1.323392666824824e-15,7.235151155395037e-17,3.735793911497562e-18],[0.10421526547730402,0.09685881367341227,0.045010823238098095,0.013944518017069498,0.00324004709433624,0.0006022670793305992,9.32922743313085e-05,1.238669508491396e-05,1.4390413268202221e-06,1.4860675918621644e-07,1.3811675605012073e-08,1.1669748344417512e-09,9.038327025401969e-11,6.461785016761437e-12,4.2897528911473896e-13,2.657962337767199e-14,1.5439621396013712e-15,8.441031704539227e-17,4.358437601550535e-18],[0.08105652907564029,0.07533482941096344,0.035008509413738,0.010845764532860484,0.0025200432038980326,0.00046843117276032054,7.25608471295902e-05,9.634121313254963e-06,1.1192572855255447e-06,1.1558333648766172e-07,1.074244238724108e-08,9.076494615759367e-10,7.029828249961986e-11,5.025845903599667e-12,3.336483176011533e-13,2.0673094342412185e-14,1.2008625750470412e-15,6.565264010543546e-17,3.3899047568168602e-18],[0.047283098659051295,0.04394543181311574,0.02042168377295552,0.006326712484339508,0.0014700290376829358,0.0002732522303777955,4.232727126042007e-05,5.619918762161788e-06,6.529017866898866e-07,6.742378886454019e-08,6.2664410754758465e-09,5.294635673269581e-10,4.1007438449400807e-11,2.9317510929111382e-12,1.9462869306727954e-13,1.2059336496730313e-14,7.0050499644421305e-16,3.829747331563705e-17,1.9774496007814997e-18],[0.022065503611340454,0.020507921686063142,0.009530143958861348,0.002952473529236063,0.0006860153407809458,0.00012751804021316775,1.9752778124582532e-05,2.6226355983161155e-06,3.0468829540845884e-07,3.146451689658822e-08,2.924346798381737e-09,2.470836427445046e-10,1.9136854539118946e-11,1.3681540796353555e-12,9.08269604053208e-14,5.62770504821884e-15,3.2690318458735186e-16,1.787220084379215e-17,9.228122213799808e-19],[0.008581051570754639,0.007975323686093503,0.0037061767647884217,0.0011481871459594357,0.0002667844396963891,4.959047835683106e-05,7.681655979318023e-06,1.0199165048234485e-06,1.1849020180810996e-07,1.2236232940531659e-08,1.1372489443108828e-09,9.608833399074671e-11,7.44212951558525e-12,5.320613080435437e-13,3.532168786994663e-14,2.1885576732970124e-15,1.271293479178189e-16,6.950318462010778e-18,3.5887235574874837e-19],[0.0028603579864599125,0.0026584481647759506,0.0012353954781631087,0.00038273004722273935,8.892837858585327e-05,1.6530202580737412e-05,2.5605586737835614e-06,3.399730552880798e-07,3.949683698606046e-08,4.078754955268914e-09,3.790839704936846e-10,3.202952823087265e-11,2.4807163108916336e-12,1.7735423207750506e-13,1.1773926675651126e-14,7.295211278042358e-16,4.237655986936285e-17,2.3167788653091577e-18,1.1962443069146383e-19],[0.0008342732560617057,0.0007753827377543818,0.00036032462124317005,0.00011162988835685727,2.593751142699762e-05,4.8213216652155166e-06,7.4683156172291e-07,9.91590665053308e-08,1.1519940843936343e-08,1.1896399658077214e-09,1.1056644653628853e-10,9.341970107861164e-12,7.235441451209243e-13,5.172845265244117e-14,3.4340709067972816e-15,2.127775507611544e-16,1.2359862209646753e-17,6.757289320727838e-19,3.489054998357425e-20],[0.00021629363071165347,0.00020102567872274296,9.341773812982232e-05,2.8941157676107213e-05,6.724557544435262e-06,1.2499755448484478e-06,1.936235026610452e-07,2.5707973204920738e-08,2.9866591223129983e-09,3.0842598102558347e-10,2.8665449818100062e-11,2.421998569350732e-12,1.8758600853050605e-13,1.3411115307842039e-14,8.903170024396738e-16,5.516469412590071e-17,3.204417081568926e-18,1.751894394708015e-19,9.045721744813456e-21],[5.046864550896249e-05,4.6906114083321824e-05,2.1797529101577355e-05,6.752954410024375e-06,1.5690675208423394e-06,2.916617214305687e-07,4.517893516259448e-08,5.998542731767771e-09,6.96888946771943e-10,7.196625000430728e-11,6.68862240864266e-12,5.651344739907342e-13,4.377018285660157e-14,3.1292684029776813e-15,2.0774117591391972e-16,1.2871795546129447e-17,7.476992698326968e-19,4.087764252916282e-20,2.1106739140197315e-21],[1.0705498190874144e-05,9.94980773499782e-06,4.623730357911482e-06,1.432448612212769e-06,3.3283337280676627e-07,6.186779929664848e-08,9.583435492891998e-09,1.2724214750605313e-09,1.478253137897735e-10,1.5265608011776138e-11,1.4188023944975547e-12,1.198773224027583e-13,9.284608466505513e-15,6.637859385564055e-16,4.406642501474683e-17,2.730387997195597e-18,1.5860328922618646e-19,8.671037705290473e-21,4.4771987716711745e-22],[2.08163007934472e-06,1.9346898851025845e-06,8.990610264184222e-07,2.7853240130753995e-07,6.47177691211909e-08,1.2029881250042952e-08,1.8634506521582863e-09,2.4741593234288354e-10,2.874388600949715e-11,2.9683204135130703e-12,2.758789631621306e-13,2.33095401723206e-14,1.8053452454264907e-15,1.290698248048795e-16,8.568493886448035e-18,5.30910162414408e-19,3.0839608923354725e-20,1.6860395083576238e-21,8.705686991998781e-23],[3.7362688649606614e-07,3.47252936666758e-07,1.6137034884527386e-07,4.999312554206003e-08,1.161604014933026e-08,2.1592150886798497e-09,3.3446637431571584e-10,4.4408103720279004e-11,5.159172487989296e-12,5.327768488879262e-13,4.951686617080264e-14,4.1837745364347665e-15,3.2403717153794735e-16,2.3166439254000572e-17,1.5379388127221608e-18,9.529181623588897e-20,5.53532886420267e-21,3.026232654244312e-22,1.5625632805295185e-23],[6.227131021956932e-08,5.787564044607325e-08,2.6895128312159006e-08,8.33220932966309e-09,1.9360117427457484e-09,3.598701203730783e-10,5.574454116071174e-11,7.401369930740839e-12,8.598643247780063e-13,8.879637315729947e-14,8.25283256068729e-15,6.972975753708433e-16,5.4006336162651326e-17,3.8610832828377476e-18,2.563238042205138e-19,1.5882010809930597e-20,9.225572177170659e-22,5.043734249864332e-23,2.604278928962626e-24],[9.686673529589547e-09,9.00290089192373e-09,4.183697541896796e-09,1.2961248329617167e-09,3.0115816794772224e-10,5.5979942558083704e-11,8.67139569372491e-12,1.1513272153422042e-12,1.3375702172471665e-13,1.3812805196381774e-14,1.2837773033499081e-15,1.084687947270629e-16,8.40100754412049e-18,6.006145221535984e-19,3.98726957983014e-20,2.4705414606944133e-21,1.4350927495955118e-22,7.845829303442415e-24,4.0511111257977565e-25],[1.4126435754181866e-09,1.312926472256324e-09,6.101241500500736e-10,1.890186979699854e-10,4.391901408017079e-11,8.16376292288514e-12,1.2645818380511142e-12,1.679023236397017e-13,1.9506283228118474e-14,2.014372680112247e-15,1.8721801187014676e-16,1.5818407169032795e-17,1.225150130020372e-18,8.75898463421319e-20,5.8147833084306386e-21,3.602882363686006e-22,2.0928490535504006e-23,1.1441864253481566e-24,5.907885805877706e-26],[1.9389276132939756e-10,1.802060644015484e-10,8.374274888974762e-11,2.5943810547850695e-11,6.0281156995657095e-12,1.1205194031255672e-12,1.7357050906075207e-13,2.3045477097424695e-14,2.6773399774628772e-15,2.7648324608551113e-16,2.5696656908913976e-17,2.171159589869339e-18,1.681582997200117e-19,1.2022167139128551e-20,7.981095952458834e-22,4.9451455582719595e-23,2.872545411310687e-24,1.5704560537904425e-25,8.108884027460917e-27],[2.513431241618384e-11,2.3360106333545383e-11,1.0855569845689861e-11,3.363095327051275e-12,7.814244442905626e-13,1.4525289419499216e-13,2.2499939508095332e-14,2.987384455073311e-15,3.470634951841688e-16,3.5840514299283707e-17,3.3310568087835468e-18,2.8144734781749524e-19,2.1798354985293798e-20,1.5584331396523465e-21,1.0345892116717525e-22,6.4103905969936956e-24,3.723679692967032e-25,2.0357816775221458e-26,1.0511543757250333e-27]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.08529036668767354, "-10": 6.169521313822097e-09, "-11": 5.129613951456465e-10, "-12": 3.919086993201411e-11, "-13": 2.769216410416819e-12, "-14": 1.8197600409051452e-13, "-15": 1.117508522065868e-14, "-16": 6.438767551556459e-16, "-17": 3.474350367597099e-17, "-18": 1.601050356235143e-18, "-2": 0.03224046553439768, "-3": 0.008580390412723352, "-4": 0.0018100546810852739, "-5": 0.0003147808105160741, "-6": 4.6448737883977254e-05, "-7": 5.943549899630414e-06, "-8": 6.707632942765857e-07, "-9": 6.766879933818047e-08, "0": 0.19002568733075026, "1": 0.22262997333822393, "10": 6.136950067558048e-05, "11": 1.281020013264043e-05, "12": 2.4571193311900213e-06, "13": 4.3588141655059986e-07, "14": 7.191106049653527e-08, "15": 1.108670584606267e-08, "16": 1.6037052096654249e-09, "17": 2.1725286766294295e-10, "18": 2.513431241618384e-11, "2": 0.20320834008470576, "3": 0.13577424146671713, "4": 0.07190716112473912, "5": 0.031394878719320486, "6": 0.011630398358502629, "7": 0.0037362566220117397, "8": 0.0010585958463981031, "9": 0.0002681139923064752} |
| Raw goal margin distribution | {"-1": 0.08529036668767354, "-10": 6.169521313822097e-09, "-11": 5.129613951456465e-10, "-12": 3.919086993201411e-11, "-13": 2.769216410416819e-12, "-14": 1.8197600409051452e-13, "-15": 1.117508522065868e-14, "-16": 6.438767551556459e-16, "-17": 3.474350367597099e-17, "-18": 1.601050356235143e-18, "-2": 0.03224046553439768, "-3": 0.008580390412723352, "-4": 0.0018100546810852739, "-5": 0.0003147808105160741, "-6": 4.6448737883977254e-05, "-7": 5.943549899630414e-06, "-8": 6.707632942765857e-07, "-9": 6.766879933818047e-08, "0": 0.19002568733075026, "1": 0.22262997333822393, "10": 6.136950067558048e-05, "11": 1.281020013264043e-05, "12": 2.4571193311900213e-06, "13": 4.3588141655059986e-07, "14": 7.191106049653527e-08, "15": 1.108670584606267e-08, "16": 1.6037052096654249e-09, "17": 2.1725286766294295e-10, "18": 2.513431241618384e-11, "2": 0.20320834008470576, "3": 0.13577424146671713, "4": 0.07190716112473912, "5": 0.031394878719320486, "6": 0.011630398358502629, "7": 0.0037362566220117397, "8": 0.0010585958463981031, "9": 0.0002681139923064752} |
| Research history json | {"away": [{"away": "Willem II", "away_goals": 1.0, "away_xg": 0.11, "date": "2026-11-22T00:00:00+00:00", "home": "Twente", "home_goals": 2.0, "home_xg": 2.76, "source": "pipeline training history"}, {"away": "Zwolle", "away_goals": 1.0, "away_xg": 0.76, "date": "2026-11-06T00:00:00+00:00", "home": "Willem II", "home_goals": 1.0, "home_xg": 0.7, "source": "pipeline training history"}, {"away": "Willem II", "away_goals": 0.0, "away_xg": 1.22, "date": "2026-10-31T00:00:00+00:00", "home": "PSV Eindhoven", "home_goals": 7.0, "home_xg": 2.57, "source": "pipeline training history"}, {"away": "Cambuur", "away_goals": 6.0, "away_xg": 1.91, "date": "2026-10-24T00:00:00+00:00", "home": "Willem II", "home_goals": 1.0, "home_xg": 1.04, "source": "pipeline training history"}, {"away": "Willem II", "away_goals": 2.0, "away_xg": 1.17, "date": "2026-10-17T00:00:00+00:00", "home": "Sparta Rotterdam", "home_goals": 3.0, "home_xg": 3.38, "source": "pipeline training history"}, {"away": "Willem II", "away_goals": 1.0, "away_xg": 0.61, "date": "2026-10-11T00:00:00+00:00", "home": "Utrecht", "home_goals": 3.0, "home_xg": 1.23, "source": "pipeline training history"}, {"away": "For Sittard", "away_goals": 1.0, "away_xg": 1.31, "date": "2026-09-19T00:00:00+00:00", "home": "Willem II", "home_goals": 0.0, "home_xg": 1.01, "source": "pipeline training history"}, {"away": "Willem II", "away_goals": 1.0, "away_xg": 1.58, "date": "2026-09-15T00:00:00+00:00", "home": "Ajax", "home_goals": 5.0, "home_xg": 3.78, "source": "pipeline training history"}, {"away": "Willem II", "away_goals": 1.0, "away_xg": 0.92, "date": "2026-09-11T00:00:00+00:00", "home": "AZ Alkmaar", "home_goals": 1.0, "home_xg": 2.49, "source": "pipeline training history"}, {"away": "Excelsior", "away_goals": 3.0, "away_xg": 1.59, "date": "2026-09-05T00:00:00+00:00", "home": "Willem II", "home_goals": 0.0, "home_xg": 0.85, "source": "pipeline training history"}], "h2h": [{"away": "Groningen", "away_goals": 3.0, "away_xg": null, "date": "2025-02-15T00:00:00+00:00", "home": "Willem II", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Willem II", "away_goals": 0.0, "away_xg": null, "date": "2024-11-30T00:00:00+00:00", "home": "Groningen", "home_goals": 2.0, "home_xg": null, "source": "pipeline training history"}], "home": [{"away": "Heerenveen", "away_goals": 3.0, "away_xg": 1.51, "date": "2026-11-21T00:00:00+00:00", "home": "Groningen", "home_goals": 1.0, "home_xg": 1.32, "source": "pipeline training history"}, {"away": "Groningen", "away_goals": 3.0, "away_xg": 2.16, "date": "2026-11-08T00:00:00+00:00", "home": "AZ Alkmaar", "home_goals": 4.0, "home_xg": 3.92, "source": "pipeline training history"}, {"away": "Sparta Rotterdam", "away_goals": 3.0, "away_xg": 2.42, "date": "2026-11-01T00:00:00+00:00", "home": "Groningen", "home_goals": 2.0, "home_xg": 2.09, "source": "pipeline training history"}, {"away": "Groningen", "away_goals": 2.0, "away_xg": 1.33, "date": "2026-10-25T00:00:00+00:00", "home": "Nijmegen", "home_goals": 2.0, "home_xg": 1.49, "source": "pipeline training history"}, {"away": "Ajax", "away_goals": 5.0, "away_xg": 3.08, "date": "2026-10-18T00:00:00+00:00", "home": "Groningen", "home_goals": 2.0, "home_xg": 2.36, "source": "pipeline training history"}, {"away": "Groningen", "away_goals": 5.0, "away_xg": 2.75, "date": "2026-10-11T00:00:00+00:00", "home": "Excelsior", "home_goals": 1.0, "home_xg": 1.77, "source": "pipeline training history"}, {"away": "Zwolle", "away_goals": 0.0, "away_xg": 0.43, "date": "2026-09-18T00:00:00+00:00", "home": "Groningen", "home_goals": 3.0, "home_xg": 1.39, "source": "pipeline training history"}, {"away": "Groningen", "away_goals": 1.0, "away_xg": 0.16, "date": "2026-09-12T00:00:00+00:00", "home": "Go Ahead Eagles", "home_goals": 1.0, "home_xg": 2.23, "source": "pipeline training history"}, {"away": "Twente", "away_goals": 2.0, "away_xg": 2.28, "date": "2026-09-06T00:00:00+00:00", "home": "Groningen", "home_goals": 2.0, "home_xg": 1.69, "source": "pipeline training history"}, {"away": "For Sittard", "away_goals": 3.0, "away_xg": 0.88, "date": "2026-08-28T00:00:00+00:00", "home": "Groningen", "home_goals": 2.0, "home_xg": 1.6, "source": "pipeline training history"}], "teams": {"away": "Willem II", "home": "Groningen"}} |
| Unadjusted home-win probability | 68.2% |
| Unadjusted draw probability | 19.0% |
| Unadjusted away-win probability | 12.8% |
| Raw p over 1 5 | 84.2% |
| Raw p under 3 5 | 58.9% |
| Raw p btts yes | 55.2% |
| P home draw | 87.2% |
| P draw away | 31.8% |
| P home away | 81.0% |
| Raw p home draw | 87.2% |
| Raw p draw away | 31.8% |
| Raw p home away | 81.0% |
| Market blending weight | 0.0% |
| Market blend applied | No |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE |
| Unanchored p over 2 5 | 0.6330 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [] |
| Price edge quotes | [] |
| Training data status | RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED |
| Training cutoff | 2026-11-22 |
| Elo home rating | 1,455.5779 |
| Elo away rating | 1,337.5850 |
| Elo rating diff | 177.9929 |
| Elo home expectancy | 0.7359 |
| Research p home | 0.6603 |
| Research p draw | 0.2006 |
| Research p away | 0.1391 |
| Research p over 1 5 | 0.8544 |
| Research v4 p home | 0.6436 |
| Research v4 p draw | 0.1891 |
| Research v4 p away | 0.1673 |
| Research v4 p over 1 5 | 0.8510 |
| Research version | team-form-research-v5 |
| Research probability basis | team_form_poisson_v1 |
| Team research json | {"base_rates": [2.3333394211798875, 0.9294109958824235], "c6_fit": {"candidate_version": "research-low-score-then-sharpen-walk-forward-v1", "delta": 0.055466179703356835, "end_exclusive": "2026-11-30", "expected_origin": "2026-11-16", "fits_version": "research-c6-live-fits-v1", "low_score_status": "fitted", "origin": "2026-11-16", "rho": -0.016463701485858812, "slope": 1.1507759984871408, "slope_status": "fitted", "stale": false}, "coverage": {"form": "last ten, exponential rank half-life five matches", "h2h": "last four years; descriptive only", "training_cache": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED", "venue_splits": "home team home matches / away team away matches", "xg": "verified supplied xG; no goals-to-xG substitution"}, "evidence": {"coverage": {}, "errors": ["free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"], "news": [], "quality_review": {"absence_note": "Reported absences only; not proof of complete coverage or a fitted player-value effect", "assessed_at_utc": "2026-11-24T15:20:25.492976+00:00", "availability": "UNAVAILABLE_OR_STALE", "form": {"away": {"matches": 10.0, "venue_matches": 6.0, "xg_matches": 10.0}, "home": {"matches": 10.0, "venue_matches": 6.0, "xg_matches": 10.0}}, "lineups": "UNCONFIRMED_OR_STALE", "probability_effect": "NONE; factual coverage/freshness review, not a calibrated confidence score", "status": "REVIEW_REQUIRED", "summary_max_age_minutes": 180, "training": {"cutoff": "2026-11-22", "status": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED"}, "version": "pre-match-research-quality-v1", "warnings": ["Research review: starting XIs not freshly confirmed for both teams; check before betting tight AH", "Research review: missing absence reports do not mean both teams have full squads", "Research review: match-window weather missing, incomplete or stale; no numerical weather adjustment", "Research review: inspect training status RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED; completeness/freshness not established by this review"], "weather": "UNAVAILABLE_INCOMPLETE_OR_STALE", "weather_max_age_minutes": 180}, "review_links": [{"label": "Sofascore", "status": "reference only; no authorized public bulk API", "url": "https://www.sofascore.com/football"}, {"label": "Sports Mole previews", "status": "reference only; article reproduction requires permission", "url": "https://www.sportsmole.co.uk/football/"}], "sources": [{"observed_at_utc": "2026-11-24T15:20:25.172109+00:00", "reason": null, "status": "available", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/ned.1/scoreboard?dates=20261127"}, {"observed_at_utc": "2026-11-24T15:20:25.259008+00:00", "reason": null, "status": "available", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/ned.1/news?limit=20"}, {"observed_at_utc": "2026-11-24T15:20:25.454525+00:00", "reason": null, "status": "available", "url": "https://www.bing.com/news/search?q=%22FC+Groningen%22+%22Willem+II+Tilburg%22+injury+suspension+lineup+preview&format=rss"}, {"observed_at_utc": "2026-11-24T15:19:56.781766+00:00", "reason": null, "status": "available", "url": "https://feeds.bbci.co.uk/sport/football/rss.xml"}, {"observed_at_utc": "2026-11-24T15:19:56.994775+00:00", "reason": null, "status": "available", "url": "https://www.theguardian.com/football/rss"}, {"observed_at_utc": "2026-11-24T15:20:25.492700+00:00", "reason": "TheSportsDB free source limit: 30 requests per minute", "status": "unavailable", "url": "https://www.thesportsdb.com/api/v1/json/123/searchevents.php?e=FC+Groningen_vs_Willem+II+Tilburg&d=2026-11-27"}]}, "evidence_quality_version": "pre-match-research-quality-v1", "form": {"away": {"all": {"goals_against": 3.2584065577239567, "goals_for": 0.8436321611467258, "last_match": "2026-11-22T00:00:00+00:00", "matches": 10, "points_per_game": 0.20719289197985322, "results": "LDLLLLLLDL", "xg_against": 2.1516754902944695, "xg_for": 0.8445326901861926, "xg_matches": 10}, "venue": {"goals_against": 3.6030701166169603, "goals_for": 0.9741680296645312, "last_match": "2026-11-22T00:00:00+00:00", "matches": 6, "points_per_game": 0.11461286578853329, "results": "LLLLLD", "xg_against": 2.7017491887016765, "xg_for": 0.8776336913023165, "xg_matches": 6}}, "home": {"all": {"goals_against": 2.6489217114294004, "goals_for": 2.2462812993052665, "last_match": "2026-11-21T00:00:00+00:00", "matches": 10, "points_per_game": 0.7204958745112958, "results": "LLLDLWWDDL", "xg_against": 2.1455152647081097, "xg_for": 1.7389171676140538, "xg_matches": 10}, "venue": {"goals_against": 2.762087879176076, "goals_for": 1.9220068515072548, "last_match": "2026-11-21T00:00:00+00:00", "matches": 6, "points_per_game": 0.5853533596457492, "results": "LLLWDL", "xg_against": 1.8301717539689404, "xg_for": 1.7457153973740847, "xg_matches": 6}}}, "goal_rates": [2.2922367481266352, 1.0885953934148753], "h2h": [{"away": "Groningen", "away_goals": 3.0, "away_xg": null, "date": "2025-02-15T00:00:00+00:00", "home": "Willem II", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Willem II", "away_goals": 0.0, "away_xg": null, "date": "2024-11-30T00:00:00+00:00", "home": "Groningen", "home_goals": 2.0, "home_xg": null, "source": "pipeline training history"}], "margin_distribution": {"-1": 0.08852394159222832, "-10": 2.299604514381131e-08, "-11": 2.234183953626282e-09, "-12": 1.9952795904513087e-10, "-13": 1.6484706465768155e-11, "-14": 1.2668972864676835e-12, "-15": 9.100356830409671e-14, "-16": 6.133448487697362e-15, "-17": 3.8653337510902854e-16, "-18": 2.053046671726838e-17, "-2": 0.03614907273415585, "-3": 0.011056474885652133, "-4": 0.0026970553555244617, "-5": 0.0005443618364682948, "-6": 9.344272734586656e-05, "-7": 1.3931119235892956e-05, "-8": 1.8337930796272231e-06, "-9": 2.1594959102422517e-07, "0": 0.20062423326631973, "1": 0.23019386974589265, "10": 4.83298161154758e-05, "11": 9.887213152972862e-06, "12": 1.859309581658219e-06, "13": 3.2346116316168276e-07, "14": 5.234501276495528e-08, "15": 7.917449540063315e-09, "16": 1.1236332527849029e-09, "17": 1.4910762007489972e-10, "18": 1.6676489727102263e-11, "2": 0.1965691338438941, "3": 0.12659828564599637, "4": 0.06502703909516724, "5": 0.02763660990015874, "6": 0.009989312099607352, "7": 0.0031359495270609373, "8": 0.0008692132995632007, "9": 0.00021553678355902843}, "model_note": "Poisson team rates with ten-match shrinkage; qualitative context has no fitted coefficient", "observed_at_utc": "2026-11-24T15:20:25.492976+00:00", "p_over_1_5": 0.8543566771380896, "shadow_v4": {"grid": "independent Poisson (C)", "margin_distribution": {"-1": 0.1069920116270122, "-10": 2.7430481190375498e-08, "-11": 2.6650122024254862e-09, "-12": 2.3800387820226586e-10, "-13": 1.9663530307506217e-11, "-14": 1.5111990765917374e-12, "-15": 1.0855221639249448e-13, "-16": 7.316190341503012e-15, "-17": 4.610704322883967e-16, "-18": 2.4489453625429943e-17, "-2": 0.04311986924197848, "-3": 0.013188547182181883, "-4": 0.003217141283923125, "-5": 0.0006493337016265317, "-6": 0.00011146172999786361, "-7": 1.6617522785820446e-05, "-8": 2.187412064256298e-06, "-9": 2.575921710717918e-07, "0": 0.1890812341509197, "1": 0.22529125356491544, "10": 4.700707312836398e-05, "11": 9.616609146764221e-06, "12": 1.808421974220774e-06, "13": 3.1460832614378755e-07, "14": 5.091237750767043e-08, "15": 7.700756167386132e-09, "16": 1.0928804354835568e-09, "17": 1.450266805093992e-10, "18": 1.6220069413326156e-11, "2": 0.19118921593455615, "3": 0.12313340603382257, "4": 0.06324730834406601, "5": 0.02688022109359602, "6": 0.009715913738350273, "7": 0.0030501214486973564, "8": 0.0008454237243338135, "9": 0.00020963773837673046}, "p_over_1_5": 0.850967883388932, "version": "team-form-research-v4"}, "version": "team-form-research-v5", "warnings": ["availability unavailable or unconfirmed", "lineups unavailable or unconfirmed", "rotation unavailable or unconfirmed", "tactics unavailable or unconfirmed", "motivation unavailable or unconfirmed", "rivalry unavailable or unconfirmed", "weather unavailable or unconfirmed", "travel unavailable or unconfirmed", "free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing", "Research review: starting XIs not freshly confirmed for both teams; check before betting tight AH", "Research review: missing absence reports do not mean both teams have full squads", "Research review: match-window weather missing, incomplete or stale; no numerical weather adjustment", "Research review: inspect training status RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED; completeness/freshness not established by this review"]} |

</details>
