# Primeira Liga — football model report

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

## 2026-11-27 — CS Marítimo vs CD Nacional

Research leans **CD Nacional win** at **38.6%**. Cagey: no cagey grid: needs Pinnacle 1X2 and O/U 2.5 (no Pinnacle 1X2 or O/U 2.5 quote). Only one view is available.

**Fixture source:** football-data.org

### The two views

- **Research:** research v5, C6
- **Cagey:** unavailable: no cagey grid: needs Pinnacle 1X2 and O/U 2.5 (no Pinnacle 1X2 or O/U 2.5 quote)

| Measure | Research | Cagey |
| --- | --- | --- |
| CS Marítimo win | 33.1% | — |
| Draw | 28.3% | — |
| CD Nacional win | 38.6% | — |
| CS Marítimo expected goals | 1.21 | — |
| CD Nacional expected goals | 1.32 | — |
| Expected total goals | 2.53 | — |
| Most likely score | 1-1 | — |
| Most likely score probability | 13.4% | — |
| Over 1.5 | 72.2% | — |
| Under 1.5 | 27.8% | — |
| Over 2.5 | 46.2% | — |
| Under 2.5 | 53.8% | — |
| Over 3.5 | 25.0% | — |
| Under 3.5 | 75.0% | — |
| BTTS Yes | 52.1% | — |
| BTTS No | 47.9% | — |
| Double Chance 1X | 61.4% | — |
| Double Chance X2 | 66.9% | — |

### 5 most likely scorelines

| Rank | Research | Cagey |
| --- | --- | --- |
| 1 | 1-1 (13.45%) | — |
| 2 | 0-1 (10.17%) | — |
| 3 | 1-0 (9.19%) | — |
| 4 | 0-0 (8.46%) | — |
| 5 | 1-2 (8.33%) | — |

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
| League | Primeira Liga |
| Training matches | 1,628 |
| Training data through | 2026-11-08 |
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
| Training sha256 | 7c73b44b6e1c6ee16fc6ee45d20634ecf277c8dff8e4ce224e38cad97bc36515 |
| Training as of utc | 2026-11-24T15:19:48.987567+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 0, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 0, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.'} |
| Bbs statistics model | {'status': 'NO_OBSERVATIONS'} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-11-24', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1628, 'tune_start_date': '2025-11-25', 'audit_start_date': '2026-05-26', 'training_shot_matches': 1323, 'tuning_matches': 207, 'audit_matches': 92, 'audit_matchdays': 42, 'selected_shrinkage': 5.0, 'selected_component': 'shots_on_target_and_total_shots', 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.8715376387866776, 'audit_candidate_poisson_score': 0.8661166852473193, 'audit_gain': 0.005420953539358231, 'audit_gain_lower95': -0.0037314460101351495, 'audit_baseline_briers': [0.5256825537476439, 0.20162598270462478, 0.2218871197329721, 0.25436800146761224], 'audit_candidate_briers': [0.5292164683546622, 0.20093844348934414, 0.21876001120007932, 0.2532888353944095], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum', 'bootstrap_lower95_not_positive', 'market_brier_worse']} |
| Optimizer objective | 1448.862 |
| Base scoring parameter | 0.083 |
| Home-advantage parameter | 0.175 |
| Dixon-Coles low-score adjustment | 0.050 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 27, 'matches': 1628, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-11-08'} |
| Training data health | {'training_end': '2026-11-08', 'days_since_latest_result': 16, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
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

### 2026-11-27 — CS Marítimo vs CD Nacional

The model's most likely 1X2 outcome is **CD Nacional win** at **41.0%**. Expected goals are 1.21 for CS Marítimo and 1.36 for CD Nacional (2.57 combined). The most likely exact score is 1-1 at 12.0%. Goal-market probabilities: at least one goal: 93.0%; Over 2.5 goals: 47.4%; Under 3.5 goals: 74.3%; Double Chance 1X: 59.0%; Double Chance X2: 66.2%; Double Chance 12 (either team wins): 74.8%; Under 4.5 goals: 88.2%; BTTS Yes (both teams score): 51.5%; BTTS No (at least one team does not score): 48.5%.

| Outcome | Benchmark probability | Benchmark fair odds |
| --- | --- | --- |
| CS Marítimo win | 33.8% | 2.96 |
| Draw | 25.2% | 3.96 |
| CD Nacional win | 41.0% | 2.44 |

| Measure | Benchmark estimate |
| --- | --- |
| CS Marítimo expected goals | 1.21 |
| CD Nacional expected goals | 1.36 |
| Expected total goals | 2.57 |
| Over 0.5 | 93.0% |
| Under 0.5 | 7.0% |
| Over 1.5 | 72.0% |
| Under 1.5 | 28.0% |
| Over 2.5 | 47.4% |
| Under 2.5 | 52.6% |
| Over 3.5 | 25.7% |
| Under 3.5 | 74.3% |
| Over 4.5 | 11.8% |
| Under 4.5 | 88.2% |

| Rank | Score | Benchmark probability |
| --- | --- | --- |
| 1 | 1-1 | 11.96% |
| 2 | 0-1 | 11.05% |
| 3 | 1-0 | 9.88% |
| 4 | 1-2 | 8.57% |
| 5 | 2-1 | 7.61% |

<details>
<summary>Additional technical details (forecast row)</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-27T20:15:00+00:00 |
| Fixture id | fdorg:567361 |
| Matched home-team name | Maritimo |
| Matched away-team name | Nacional |
| Home-name matching confidence | 95/100 |
| Away-name matching confidence | 95/100 |
| Dc lambda home | 1.2090 |
| Dc lambda away | 1.3608 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 51.5% |
| P btts no | 48.5% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 14.23 |
| Fair Over 1.5 odds | 1.39 |
| Fair Under 1.5 odds | 3.58 |
| Fair Over 2.5 odds | 2.11 |
| Fair Under 2.5 odds | 1.90 |
| Fair Over 3.5 odds | 3.88 |
| Fair Under 3.5 odds | 1.35 |
| Fair Over 4.5 odds | 8.45 |
| Fair Under 4.5 odds | 1.13 |
| Score matrix json | [[0.07025305026730096,0.11046961362389111,0.07088114334951365,0.032152658371145296,0.010938664976458859,0.002977157038426133,0.0006752396240404534,0.00013127055029518896,2.2329795477239664e-05,3.376367119893335e-06,4.5946992420619504e-07,5.68423245656778e-08,6.446114426265623e-09,6.747798177719599e-10,6.559058062749689e-11],[0.09884374647730919,0.1196442621036122,0.08569306982824326,0.038871551286582186,0.013224501430984319,0.0035992890905483265,0.0008163434380336125,0.00015870196079328242,2.699601942996337e-05,4.081921505471728e-06,5.554846668433329e-07,6.872058008697059e-08,7.793149313732343e-09,8.157875467371193e-10,7.92969461295474e-11],[0.05594301065983009,0.07612954976457212,0.05180011121137313,0.023497240601128663,0.007994002854757971,0.002175713573407731,0.0004934667524640213,9.593283605117798e-05,1.6318668610417782e-05,2.467457267703603e-06,3.357817332996702e-07,4.154050844659915e-08,4.710836033150515e-09,4.93130724929502e-10,4.793375516206579e-11],[0.02254444596656783,0.030679409293195615,0.02087490098393201,0.009469141271582717,0.0032214992237642906,0.0008767897279014225,0.00019886192047956932,3.8659925757774025e-05,6.576252125058719e-06,9.943593737707488e-07,1.3531651324533658e-07,1.6740388782303574e-08,1.898417463666856e-09,1.9872650491101306e-10,1.9316800087805033e-11],[0.006813881277725641,0.009272609888244363,0.00630927445277314,0.002861973389022672,0.0009736727741975641,0.0002650027913885877,6.01044496199962e-05,1.1684658150828065e-05,1.9876204231850063e-06,3.005372911055393e-07,4.089835064196446e-08,5.059650695108754e-09,5.737817301950891e-10,6.006352133066647e-11,5.838350725453731e-12],[0.0016475535707833906,0.002242058660722311,0.0015255428191417568,0.0006920071372516221,0.00023542794341717887,6.407600564557612e-05,1.4532877306668914e-05,2.825276736580553e-06,4.805940978580558e-07,7.266802383732927e-08,9.88896355731792e-09,1.2233916661996089e-09,1.3873680798100555e-10,1.4522981104125485e-11,1.4116764283303968e-12],[0.00033197339592077663,0.00045176305077574325,0.00030738886994262566,0.00013943580556570505,4.743749475392368e-05,1.2910978779941231e-05,2.9282984890748454e-06,5.692784315429867e-07,9.683718790980465e-08,1.4642225343033652e-08,1.9925742461282583e-09,2.465069987231736e-10,2.7954738529542103e-11,2.926304456211016e-12,2.844453899191411e-13],[5.733505425611376e-05,7.802389994322325e-05,5.3089066028929116e-05,2.4081928177348523e-05,8.192919580035856e-06,2.229852385593334e-06,5.057458061767971e-07,9.831995623872742e-08,1.6724730026689015e-08,2.5288556094821005e-09,3.441370721717783e-10,4.257417106302638e-11,4.828056916612876e-12,5.054014171870738e-13,4.912650249783075e-14],[8.664534345453996e-06,1.1791054697610866e-05,8.02287609114247e-06,3.6392865848756555e-06,1.2381227158809854e-06,3.3697766280923625e-07,7.642884382935613e-08,1.485821629937933e-08,2.527458979760893e-09,3.821633478390789e-10,5.2006360158949355e-11,6.433853986725594e-12,7.296210933878774e-13,7.637679939914902e-14,7.424049278179539e-15],[1.1639054582667805e-06,1.5838904174315869e-06,1.0777116116318535e-06,4.888647619656822e-07,1.6631681860365017e-07,4.526615342732559e-08,1.0266673886367508e-08,1.995901725524283e-09,3.395131445964571e-10,5.133593898589409e-11,6.9860057148192375e-12,8.64258536498309e-13,9.800988018545741e-14,1.0259682766709447e-14,9.972713053931532e-16],[1.407125040533266e-07,1.914873628264936e-07,1.3029193947237678e-07,5.9102209987108155e-08,2.0107179535658048e-08,5.472535378523064e-09,1.2412085368178935e-09,2.4129823229895325e-10,4.104606984688299e-11,6.206353335081804e-12,8.445860877110395e-13,1.0448613498319513e-13,1.1849085821282508e-14,1.2403633324705513e-15,1.2056695980390827e-16],[1.546518050017449e-08,2.104565368612752e-08,1.4319895557359174e-08,6.4957009439861104e-09,2.2099042509436097e-09,6.014657189980487e-10,1.3641654797765212e-10,2.65201784445689e-11,4.511218695704875e-12,6.821168823669363e-13,9.282527080491279e-14,1.1483676935123858e-14,1.3022883234225273e-15,1.363236547562635e-16,1.3251059728267575e-17],[1.5580763442883186e-09,2.1202943708332126e-09,1.4426918923027751e-09,6.544248209894393e-10,2.2264205299760876e-10,6.059609253578717e-11,1.3743609159366365e-11,2.671838371386714e-12,4.5449344310010885e-13,6.872148556194542e-14,9.351902397237451e-15,1.1569503102704804e-15,1.3120213049855068e-16,1.3734250411126164e-17,1.3350094878706625e-18],[1.4489732514446082e-10,1.9718223948321412e-10,1.3416685066081067e-10,6.08599228254282e-11,2.0705171516329182e-11,5.635289794899183e-12,1.2781223540960144e-12,2.4847449526557186e-13,4.226678907122646e-14,6.390931660301846e-15,8.697042653521126e-16,1.0759357582045762e-16,1.220148026262349e-17,1.2772520131838528e-18,1.2415264793927196e-19],[1.2512593028246696e-11,1.7027651218488032e-11,1.1585964050934393e-11,5.255552131730958e-12,1.7879928736129372e-12,4.866348480174193e-13,1.1037211930008782e-13,2.1456988485173325e-14,3.6499440533614266e-15,5.518882205518131e-16,7.510321889263164e-17,9.291231741876335e-18,1.0536575241549843e-18,1.10296961103628e-19,1.0721188645094097e-20]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.2231615453381393, "-10": 5.331059051819526e-07, "-11": 6.514792140442746e-08, "-12": 7.309835728164807e-09, "-13": 7.540767639015074e-10, "-14": 6.559058062749689e-11, "-2": 0.11868651636403792, "-3": 0.04776391554116114, "-4": 0.015072143069564422, "-5": 0.0038963202423030756, "-6": 0.0008512967630277966, "-7": 0.0001608745448690353, "-8": 2.6764827693950057e-05, "-9": 3.975352187844693e-06, "0": 0.25220734283180857, "1": 0.19895903048686903, "10": 1.6326349754745595e-07, "11": 1.772489727380025e-08, "12": 1.7668445478224672e-09, "13": 1.6192497636294886e-10, "14": 1.2512593028246696e-11, "2": 0.0936734473566732, "3": 0.033490574889315436, "4": 0.00938869539362691, "5": 0.002156216902658126, "6": 0.0004185297593580963, "7": 7.026519457526641e-05, "8": 1.0385440791016858e-05, "9": 1.370388333277987e-06} |
| Raw goal margin distribution | {"-1": 0.2231615453381393, "-10": 5.331059051819526e-07, "-11": 6.514792140442746e-08, "-12": 7.309835728164807e-09, "-13": 7.540767639015074e-10, "-14": 6.559058062749689e-11, "-2": 0.11868651636403792, "-3": 0.04776391554116114, "-4": 0.015072143069564422, "-5": 0.0038963202423030756, "-6": 0.0008512967630277966, "-7": 0.0001608745448690353, "-8": 2.6764827693950057e-05, "-9": 3.975352187844693e-06, "0": 0.25220734283180857, "1": 0.19895903048686903, "10": 1.6326349754745595e-07, "11": 1.772489727380025e-08, "12": 1.7668445478224672e-09, "13": 1.6192497636294886e-10, "14": 1.2512593028246696e-11, "2": 0.0936734473566732, "3": 0.033490574889315436, "4": 0.00938869539362691, "5": 0.002156216902658126, "6": 0.0004185297593580963, "7": 7.026519457526641e-05, "8": 1.0385440791016858e-05, "9": 1.370388333277987e-06} |
| Research history json | {"away": [{"away": "Academico Viseu", "away_goals": 0.0, "away_xg": 0.63, "date": "2026-11-08T00:00:00+00:00", "home": "Nacional", "home_goals": 1.0, "home_xg": 1.13, "source": "pipeline training history"}, {"away": "Nacional", "away_goals": 0.0, "away_xg": 0.32, "date": "2026-11-01T00:00:00+00:00", "home": "Arouca", "home_goals": 1.0, "home_xg": 0.7, "source": "pipeline training history"}, {"away": "Sp Braga", "away_goals": 0.0, "away_xg": 1.67, "date": "2026-10-25T00:00:00+00:00", "home": "Nacional", "home_goals": 1.0, "home_xg": 0.48, "source": "pipeline training history"}, {"away": "Nacional", "away_goals": 2.0, "away_xg": 1.21, "date": "2026-10-11T00:00:00+00:00", "home": "Rio Ave", "home_goals": 3.0, "home_xg": 1.66, "source": "pipeline training history"}, {"away": "Famalicao", "away_goals": 4.0, "away_xg": 1.45, "date": "2026-09-19T00:00:00+00:00", "home": "Nacional", "home_goals": 0.0, "home_xg": 1.23, "source": "pipeline training history"}, {"away": "Alverca", "away_goals": 3.0, "away_xg": 1.16, "date": "2026-09-12T00:00:00+00:00", "home": "Nacional", "home_goals": 1.0, "home_xg": 2.2, "source": "pipeline training history"}, {"away": "Nacional", "away_goals": 0.0, "away_xg": 0.08, "date": "2026-09-05T00:00:00+00:00", "home": "Sp Lisbon", "home_goals": 2.0, "home_xg": 3.0, "source": "pipeline training history"}, {"away": "Estrela", "away_goals": 3.0, "away_xg": 2.1, "date": "2026-08-30T00:00:00+00:00", "home": "Nacional", "home_goals": 2.0, "home_xg": 0.84, "source": "pipeline training history"}, {"away": "Nacional", "away_goals": 0.0, "away_xg": 0.42, "date": "2026-08-23T00:00:00+00:00", "home": "Guimaraes", "home_goals": 1.0, "home_xg": 3.14, "source": "pipeline training history"}, {"away": "Estoril", "away_goals": 0.0, "away_xg": 0.82, "date": "2026-08-16T00:00:00+00:00", "home": "Nacional", "home_goals": 2.0, "home_xg": 2.08, "source": "pipeline training history"}], "h2h": [], "home": [{"away": "Santa Clara", "away_goals": 2.0, "away_xg": 0.82, "date": "2026-11-01T00:00:00+00:00", "home": "Maritimo", "home_goals": 0.0, "home_xg": 2.06, "source": "pipeline training history"}, {"away": "Maritimo", "away_goals": 0.0, "away_xg": 0.52, "date": "2026-10-23T00:00:00+00:00", "home": "Guimaraes", "home_goals": 5.0, "home_xg": 1.78, "source": "pipeline training history"}, {"away": "Porto", "away_goals": 2.0, "away_xg": 2.13, "date": "2026-10-10T00:00:00+00:00", "home": "Maritimo", "home_goals": 1.0, "home_xg": 0.19, "source": "pipeline training history"}, {"away": "Maritimo", "away_goals": 1.0, "away_xg": 0.86, "date": "2026-09-19T00:00:00+00:00", "home": "Gil Vicente", "home_goals": 1.0, "home_xg": 1.2, "source": "pipeline training history"}, {"away": "Maritimo", "away_goals": 1.0, "away_xg": 0.76, "date": "2026-09-14T00:00:00+00:00", "home": "Moreirense", "home_goals": 3.0, "home_xg": 1.99, "source": "pipeline training history"}, {"away": "Benfica", "away_goals": 3.0, "away_xg": 1.31, "date": "2026-09-05T00:00:00+00:00", "home": "Maritimo", "home_goals": 0.0, "home_xg": 0.13, "source": "pipeline training history"}, {"away": "Maritimo", "away_goals": 1.0, "away_xg": 0.67, "date": "2026-08-29T00:00:00+00:00", "home": "Arouca", "home_goals": 2.0, "home_xg": 1.66, "source": "pipeline training history"}, {"away": "Academico Viseu", "away_goals": 2.0, "away_xg": 1.84, "date": "2026-08-22T00:00:00+00:00", "home": "Maritimo", "home_goals": 2.0, "home_xg": 1.28, "source": "pipeline training history"}, {"away": "Maritimo", "away_goals": 2.0, "away_xg": 1.61, "date": "2026-08-16T00:00:00+00:00", "home": "Famalicao", "home_goals": 1.0, "home_xg": 0.59, "source": "pipeline training history"}, {"away": "Casa Pia", "away_goals": 0.0, "away_xg": 0.65, "date": "2026-08-08T00:00:00+00:00", "home": "Maritimo", "home_goals": 1.0, "home_xg": 1.28, "source": "pipeline training history"}], "teams": {"away": "Nacional", "home": "Maritimo"}} |
| Unadjusted home-win probability | 33.8% |
| Unadjusted draw probability | 25.2% |
| Unadjusted away-win probability | 41.0% |
| Raw p over 1 5 | 72.0% |
| Raw p under 3 5 | 74.3% |
| Raw p btts yes | 51.5% |
| P home draw | 59.0% |
| P draw away | 66.2% |
| P home away | 74.8% |
| Raw p home draw | 59.0% |
| Raw p draw away | 66.2% |
| Raw p home away | 74.8% |
| Market blending weight | 0.0% |
| Market blend applied | No |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE |
| Unanchored p over 2 5 | 0.4740 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [] |
| Price edge quotes | [] |
| Training data status | RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED |
| Training cutoff | 2026-11-08 |
| Elo home rating | 1,397.7708 |
| Elo away rating | 1,372.3069 |
| Elo rating diff | 85.4639 |
| Elo home expectancy | 0.6206 |
| Research p home | 0.3314 |
| Research p draw | 0.2827 |
| Research p away | 0.3859 |
| Research p over 1 5 | 0.7219 |
| Research v4 p home | 0.3422 |
| Research v4 p draw | 0.2674 |
| Research v4 p away | 0.3904 |
| Research v4 p over 1 5 | 0.7200 |
| Research version | team-form-research-v5 |
| Research probability basis | team_form_poisson_v1 |
| Team research json | {"base_rates": [1.2089685038754563, 1.3608411286172872], "c6_fit": {"candidate_version": "research-low-score-then-sharpen-walk-forward-v1", "delta": 0.055466179703356835, "end_exclusive": "2026-11-30", "expected_origin": "2026-11-16", "fits_version": "research-c6-live-fits-v1", "low_score_status": "fitted", "origin": "2026-11-16", "rho": -0.016463701485858812, "slope": 1.1507759984871408, "slope_status": "fitted", "stale": false}, "coverage": {"form": "last ten, exponential rank half-life five matches", "training_cache": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED", "venue_splits": "home team home matches / away team away matches", "xg": "verified supplied xG; no goals-to-xG substitution"}, "evidence": {"coverage": {}, "errors": ["free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"], "news": [], "quality_review": {"absence_note": "Reported absences only; not proof of complete coverage or a fitted player-value effect", "assessed_at_utc": "2026-11-24T15:20:25.978413+00:00", "availability": "UNAVAILABLE_OR_STALE", "form": {"away": {"matches": 10.0, "venue_matches": 4.0, "xg_matches": 10.0}, "home": {"matches": 10.0, "venue_matches": 5.0, "xg_matches": 10.0}}, "lineups": "UNCONFIRMED_OR_STALE", "probability_effect": "NONE; factual coverage/freshness review, not a calibrated confidence score", "status": "REVIEW_REQUIRED", "summary_max_age_minutes": 180, "training": {"cutoff": "2026-11-08", "status": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED"}, "version": "pre-match-research-quality-v1", "warnings": ["Research review: starting XIs not freshly confirmed for both teams; check before betting tight AH", "Research review: missing absence reports do not mean both teams have full squads", "Research review: match-window weather missing, incomplete or stale; no numerical weather adjustment", "Research review: inspect training status RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED; completeness/freshness not established by this review"], "weather": "UNAVAILABLE_INCOMPLETE_OR_STALE", "weather_max_age_minutes": 180}, "review_links": [{"label": "Sofascore", "status": "reference only; no authorized public bulk API", "url": "https://www.sofascore.com/football"}, {"label": "Sports Mole previews", "status": "reference only; article reproduction requires permission", "url": "https://www.sportsmole.co.uk/football/"}], "sources": [{"observed_at_utc": "2026-11-24T15:20:25.589883+00:00", "reason": null, "status": "available", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/por.1/scoreboard?dates=20261127"}, {"observed_at_utc": "2026-11-24T15:20:25.696036+00:00", "reason": null, "status": "available", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/por.1/news?limit=20"}, {"observed_at_utc": "2026-11-24T15:20:25.937713+00:00", "reason": null, "status": "available", "url": "https://www.bing.com/news/search?q=%22CS+Mar%C3%ADtimo%22+%22CD+Nacional%22+injury+suspension+lineup+preview&format=rss"}, {"observed_at_utc": "2026-11-24T15:19:56.781766+00:00", "reason": null, "status": "available", "url": "https://feeds.bbci.co.uk/sport/football/rss.xml"}, {"observed_at_utc": "2026-11-24T15:19:56.994775+00:00", "reason": null, "status": "available", "url": "https://www.theguardian.com/football/rss"}, {"observed_at_utc": "2026-11-24T15:20:25.978142+00:00", "reason": "TheSportsDB free source limit: 30 requests per minute", "status": "unavailable", "url": "https://www.thesportsdb.com/api/v1/json/123/searchevents.php?e=CS+Mar%C3%ADtimo_vs_CD+Nacional&d=2026-11-27"}]}, "evidence_quality_version": "pre-match-research-quality-v1", "form": {"away": {"all": {"goals_against": 1.5507048527234875, "goals_for": 0.8473887254235924, "last_match": "2026-11-08T00:00:00+00:00", "matches": 10, "points_per_game": 1.0589134132875462, "results": "WLWLLLLLLW", "xg_against": 1.4473966787066475, "xg_for": 0.943443703024997, "xg_matches": 10}, "venue": {"goals_against": 1.7599865214626136, "goals_for": 0.5295057548750894, "last_match": "2026-11-01T00:00:00+00:00", "matches": 4, "points_per_game": 0.0, "results": "LLLL", "xg_against": 1.9738427187746768, "xg_for": 0.5203791930565782, "xg_matches": 4}}, "home": {"all": {"goals_against": 2.3662591888570916, "goals_for": 0.7131841570421359, "last_match": "2026-11-01T00:00:00+00:00", "matches": 10, "points_per_game": 0.49878383320263503, "results": "LLLDLLLDWW", "xg_against": 1.4454419451949967, "xg_for": 0.932195130990825, "xg_matches": 10}, "venue": {"goals_against": 1.8988119457434338, "goals_for": 0.7157020266306037, "last_match": "2026-11-01T00:00:00+00:00", "matches": 5, "points_per_game": 0.6169046207669643, "results": "LLLDW", "xg_against": 1.3603430415604811, "xg_for": 1.0106319966707003, "xg_matches": 5}}}, "goal_rates": [1.217218723924357, 1.3189319062435654], "h2h": [], "margin_distribution": {"-1": 0.2105431460000676, "-10": 3.993757151222461e-07, "-11": 4.731629060177515e-08, "-12": 5.146919895480541e-09, "-13": 5.148427616095318e-10, "-14": 4.351322619035612e-11, "-2": 0.11326234738627876, "-3": 0.04428996668507584, "-4": 0.013568164343817923, "-5": 0.0034034908687428553, "-6": 0.0007213416136687064, "-7": 0.0001322055060585952, "-8": 2.1328892368783546e-05, "-9": 3.07169209027151e-06, "0": 0.28265590149813535, "1": 0.19030856784417163, "10": 1.7545824509468184e-07, "11": 1.9184437436097737e-08, "12": 1.9258924786467964e-09, "13": 1.7778924638678534e-10, "14": 1.3867507583221028e-11, "2": 0.09456004868803905, "3": 0.0341250842635116, "4": 0.00964796510533061, "5": 0.0022334974882140114, "6": 0.00043686586864683354, "7": 7.389293575293518e-05, "8": 1.100190602511987e-05, "9": 1.4622564901719978e-06}, "model_note": "Poisson team rates with ten-match shrinkage; qualitative context has no fitted coefficient", "observed_at_utc": "2026-11-24T15:20:25.978413+00:00", "p_over_1_5": 0.7218558028905647, "shadow_v4": {"grid": "independent Poisson (C)", "margin_distribution": {"-1": 0.21392307985675882, "-10": 4.018176730581754e-07, "-11": 4.760560311367482e-08, "-12": 5.178390416617545e-09, "-13": 5.179907356096116e-10, "-14": 4.3779285101777166e-11, "-2": 0.1139548829550908, "-3": 0.044560774927874386, "-4": 0.013651126039636703, "-5": 0.003424301301681287, "-6": 0.0007257522120384022, "-7": 0.00013301386839127864, "-8": 2.145930655275212e-05, "-9": 3.090473760244292e-06, "0": 0.2673611089420291, "1": 0.1974257935899279, "10": 1.8009080250502195e-07, "11": 1.9690956851927077e-08, "12": 1.97674108635206e-09, "13": 1.8248334833898163e-10, "14": 1.423364611938917e-11, "2": 0.09705668174187762, "3": 0.03502607590342059, "4": 0.00990269666393752, "5": 0.0022924676741657647, "6": 0.00044840027226538364, "7": 7.58439028728293e-05, "8": 1.1292385171637213e-05, "9": 1.5008638929515524e-06}, "p_over_1_5": 0.7200409362100987, "version": "team-form-research-v4"}, "version": "team-form-research-v5", "warnings": ["availability unavailable or unconfirmed", "lineups unavailable or unconfirmed", "rotation unavailable or unconfirmed", "h2h unavailable or unconfirmed", "tactics unavailable or unconfirmed", "motivation unavailable or unconfirmed", "rivalry unavailable or unconfirmed", "weather unavailable or unconfirmed", "travel unavailable or unconfirmed", "free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing", "Research review: starting XIs not freshly confirmed for both teams; check before betting tight AH", "Research review: missing absence reports do not mean both teams have full squads", "Research review: match-window weather missing, incomplete or stale; no numerical weather adjustment", "Research review: inspect training status RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED; completeness/freshness not established by this review"]} |

</details>
