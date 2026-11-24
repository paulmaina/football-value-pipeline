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
| 3 | 1-0 (9.18%) | — |
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
| Training as of utc | 2026-11-24T16:35:12.223404+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 0, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 0, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.'} |
| Bbs statistics model | {'status': 'NO_OBSERVATIONS'} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-11-24', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1628, 'tune_start_date': '2025-11-25', 'audit_start_date': '2026-05-26', 'training_shot_matches': 1323, 'tuning_matches': 207, 'audit_matches': 92, 'audit_matchdays': 42, 'selected_shrinkage': 5.0, 'selected_component': 'shots_on_target_and_total_shots', 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.8715376387746687, 'audit_candidate_poisson_score': 0.8661166852387249, 'audit_gain': 0.005420953535943851, 'audit_gain_lower95': -0.003731446012881781, 'audit_baseline_briers': [0.5256825537437794, 0.20162598269824156, 0.221887119731087, 0.2543680014638883], 'audit_candidate_briers': [0.5292164683524547, 0.20093844348497894, 0.21876001119885946, 0.2532888353919278], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum', 'bootstrap_lower95_not_positive', 'market_brier_worse']} |
| Optimizer objective | 1448.753 |
| Base scoring parameter | 0.083 |
| Home-advantage parameter | 0.174 |
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

The model's most likely 1X2 outcome is **CD Nacional win** at **41.0%**. Expected goals are 1.21 for CS Marítimo and 1.36 for CD Nacional (2.57 combined). The most likely exact score is 1-1 at 12.0%. Goal-market probabilities: at least one goal: 93.0%; Over 2.5 goals: 47.4%; Under 3.5 goals: 74.2%; Double Chance 1X: 59.0%; Double Chance X2: 66.2%; Double Chance 12 (either team wins): 74.8%; Under 4.5 goals: 88.2%; BTTS Yes (both teams score): 51.5%; BTTS No (at least one team does not score): 48.5%.

| Outcome | Benchmark probability | Benchmark fair odds |
| --- | --- | --- |
| CS Marítimo win | 33.8% | 2.96 |
| Draw | 25.2% | 3.97 |
| CD Nacional win | 41.0% | 2.44 |

| Measure | Benchmark estimate |
| --- | --- |
| CS Marítimo expected goals | 1.21 |
| CD Nacional expected goals | 1.36 |
| Expected total goals | 2.57 |
| Over 0.5 | 93.0% |
| Under 0.5 | 7.0% |
| Over 1.5 | 72.1% |
| Under 1.5 | 27.9% |
| Over 2.5 | 47.4% |
| Under 2.5 | 52.6% |
| Over 3.5 | 25.8% |
| Under 3.5 | 74.2% |
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
| Dc lambda away | 1.3612 |
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
| Fair Under 0.5 odds | 14.24 |
| Fair Over 1.5 odds | 1.39 |
| Fair Under 1.5 odds | 3.58 |
| Fair Over 2.5 odds | 2.11 |
| Fair Under 2.5 odds | 1.90 |
| Fair Over 3.5 odds | 3.88 |
| Fair Under 3.5 odds | 1.35 |
| Fair Over 4.5 odds | 8.45 |
| Fair Under 4.5 odds | 1.13 |
| Score matrix json | [[0.0702274596793746,0.1104584938643009,0.07089099637447663,0.032164857724775356,0.010945445740986154,0.0029797186356361233,0.0006759830646815699,0.00013144666890107287,2.2365128964675294e-05,3.3825225954177496e-06,4.6041823474054475e-07,5.69733346265332e-08,6.462524495664443e-09,6.766602408355894e-10,6.578917378465251e-11],[0.09881268236529561,0.11963357974352085,0.08570601572208447,0.03888676902347402,0.013232858793615843,0.0036024294380656192,0.0008172520931067137,0.0001589167997010559,2.7039062683608097e-05,4.089412613299864e-06,5.566378592982335e-07,6.887979804159276e-08,7.813082822308715e-09,8.180707876246526e-10,7.953799849201236e-11],[0.055925247394967965,0.07612367088959347,0.05180856178231718,0.023506723051976132,0.007999151244981613,0.002177638133519825,0.0004940219796792747,9.606386163437953e-05,1.634488475257273e-05,2.4720153450668464e-06,3.364828790705092e-07,4.163725547531025e-08,4.72294249942176e-09,4.945168735925681e-10,4.808004752288877e-11],[0.022537559434558846,0.030677410238964448,0.020878558339521073,0.009473076876246335,0.003223612858367432,0.0008775758918785013,0.00019908807287639992,3.8713194700911996e-05,6.586896414789361e-06,9.962082486486861e-07,1.356007034212141e-07,1.6779579236177883e-08,1.9033192027738685e-09,1.9928751233360745e-10,1.9375988111605925e-11],[0.0068118820513967384,0.009272117542137361,0.006310455984597036,0.0028631974341398777,0.0009743233571641016,0.0002652436029723402,6.017352829225984e-05,1.1700899420857441e-05,1.990861592294297e-06,3.010997312343281e-07,4.098473929592197e-08,5.07155688089467e-09,5.752701818979295e-10,6.023380802498054e-11,5.856310486003096e-12],[0.0016470900397844892,0.0022419666600413386,0.0015258469128362248,0.0006923114552080833,0.00023558809224909032,6.41350060491305e-05,1.4549755612481451e-05,2.829237903299087e-06,4.81383599204431e-07,7.280489658451429e-08,9.90997133657583e-09,1.2262852999648319e-09,1.3909838421157146e-10,1.456433104796551e-11,1.4160360673601696e-12],[0.000331884000472503,0.0004517499627147599,0.00030745385213243375,0.00013949880685178707,4.7470336551572816e-05,1.2923022945787866e-05,2.931734745478406e-06,5.700834629284726e-07,9.699743839548842e-08,1.4669981451419018e-08,1.996831291737373e-09,2.4709303149341057e-10,2.802793235118944e-11,2.934671654645625e-12,2.853272762855969e-13],[5.732030625914117e-05,7.802258071645437e-05,5.3100929661247476e-05,2.409309975818404e-05,8.19869058311564e-06,2.2319594556889202e-06,5.063453894798718e-07,9.846018079150871e-08,1.675260894549275e-08,2.53367992555859e-09,3.4487646595577837e-10,4.267589946950566e-11,4.840756601383005e-12,5.068526285534055e-13,4.927940737574675e-14],[8.662410109687422e-06,1.1790997572947087e-05,8.024765740989653e-06,3.64101876873203e-06,1.2390097825420115e-06,3.37300154433296e-07,7.652037658337829e-08,1.4879586679703051e-08,2.531702612282077e-09,3.828970226126571e-10,5.211872685715419e-11,6.449305091521485e-12,7.315491081429639e-13,7.659703201607504e-14,7.447246264197988e-15],[1.1636341472919448e-06,1.5839018509610562e-06,1.077978451954298e-06,4.891033461333482e-07,1.6643798591136854e-07,4.5310020261738984e-08,1.0279093465741131e-08,1.998796517233657e-09,3.4008729362109913e-10,5.1435113873242975e-11,7.001184372065572e-12,8.663445318070956e-13,9.827005554772072e-14,1.0289390701490987e-14,1.0003994207826588e-15],[1.406814004922978e-07,1.9149105511737732e-07,1.3032577178521202e-07,5.9131767385514266e-08,2.0122071020019765e-08,5.477904822224665e-09,1.2427250162063887e-09,2.4165111860799437e-10,4.11159786498152e-11,6.218418281217046e-12,8.464313503167265e-13,1.0473958875055948e-13,1.1880683523324576e-14,1.2439699345940628e-15,1.2094659811670024e-16],[1.5461948547170297e-08,2.1046313379787133e-08,1.4323786731306612e-08,6.4990278858371275e-09,2.2115675966069594e-09,6.02063117165023e-10,1.3658486617011296e-10,2.6559283240057885e-11,4.518956622021978e-12,6.834511397562125e-13,9.302919889559696e-14,1.151167195127257e-14,1.3057768596276938e-15,1.3672169210437491e-16,1.329294469980833e-17],[1.5577695253400748e-09,2.1203864120857867e-09,1.4431013264226333e-09,6.547679003074427e-10,2.2281231855828455e-10,6.065701055657471e-11,1.3760732775261578e-11,2.67581035598578e-12,4.5527851102621e-13,6.885673913111114e-14,9.372560681097533e-15,1.15978472549544e-15,1.3155517835393056e-16,1.3774517795307354e-17,1.3392454445324065e-18],[1.4487053934175256e-10,1.9719317789628156e-10,1.342065460152105e-10,6.089256293577709e-11,2.0721255767587495e-11,5.641023072569728e-12,1.2797302466516492e-12,2.4884688212351587e-13,4.2340309249969574e-14,6.403587162908923e-15,8.716359505026791e-16,1.0785847069782089e-16,1.2234460445728477e-17,1.2810122355828632e-18,1.2454808410636948e-19],[1.2510430860140543e-11,1.702880122744065e-11,1.1589531746967609e-11,5.258434199017597e-12,1.7894034135136244e-12,4.871358210613219e-13,1.105123018324533e-13,2.1489405145539837e-14,3.656336988013491e-15,5.529877559817088e-16,7.527093737293692e-17,9.314219070879723e-18,1.0565182694346333e-18,1.1062300918510272e-19,1.075546623941253e-20]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.2231752260813899, "-10": 5.342261191043789e-07, "-11": 6.53003103105461e-08, "-12": 7.3286753308119845e-09, "-13": 7.561982393276018e-10, "-14": 6.578917378465251e-11, "-2": 0.11871759488512172, "-3": 0.04778664002921423, "-4": 0.015082676060169989, "-5": 0.0038999327485059626, "-6": 0.0008522831969506755, "-7": 0.00016109856127238519, "-8": 2.6808394156122066e-05, "-9": 3.982762679238159e-06, "0": 0.25218416922359427, "1": 0.198927141715121, "10": 1.6323349716485688e-07, "11": 1.772179993947031e-08, "12": 1.7665522349833238e-09, "13": 1.618993405691932e-10, "14": 1.2510430860140543e-11, "2": 0.09365520593072679, "3": 0.03348356921245504, "4": 0.009386681252877555, "5": 0.002155754006123532, "6": 0.00041844118842345357, "7": 7.025068757725488e-05, "8": 1.038336532417346e-05, "9": 1.3701249654325247e-06} |
| Raw goal margin distribution | {"-1": 0.2231752260813899, "-10": 5.342261191043789e-07, "-11": 6.53003103105461e-08, "-12": 7.3286753308119845e-09, "-13": 7.561982393276018e-10, "-14": 6.578917378465251e-11, "-2": 0.11871759488512172, "-3": 0.04778664002921423, "-4": 0.015082676060169989, "-5": 0.0038999327485059626, "-6": 0.0008522831969506755, "-7": 0.00016109856127238519, "-8": 2.6808394156122066e-05, "-9": 3.982762679238159e-06, "0": 0.25218416922359427, "1": 0.198927141715121, "10": 1.6323349716485688e-07, "11": 1.772179993947031e-08, "12": 1.7665522349833238e-09, "13": 1.618993405691932e-10, "14": 1.2510430860140543e-11, "2": 0.09365520593072679, "3": 0.03348356921245504, "4": 0.009386681252877555, "5": 0.002155754006123532, "6": 0.00041844118842345357, "7": 7.025068757725488e-05, "8": 1.038336532417346e-05, "9": 1.3701249654325247e-06} |
| Research history json | {"away": [{"away": "Academico Viseu", "away_goals": 0.0, "away_xg": 0.63, "date": "2026-11-08T00:00:00+00:00", "home": "Nacional", "home_goals": 1.0, "home_xg": 1.13, "source": "pipeline training history"}, {"away": "Nacional", "away_goals": 0.0, "away_xg": 0.32, "date": "2026-11-01T00:00:00+00:00", "home": "Arouca", "home_goals": 1.0, "home_xg": 0.7, "source": "pipeline training history"}, {"away": "Sp Braga", "away_goals": 0.0, "away_xg": 1.67, "date": "2026-10-25T00:00:00+00:00", "home": "Nacional", "home_goals": 1.0, "home_xg": 0.48, "source": "pipeline training history"}, {"away": "Nacional", "away_goals": 2.0, "away_xg": 1.21, "date": "2026-10-11T00:00:00+00:00", "home": "Rio Ave", "home_goals": 3.0, "home_xg": 1.66, "source": "pipeline training history"}, {"away": "Famalicao", "away_goals": 4.0, "away_xg": 1.45, "date": "2026-09-19T00:00:00+00:00", "home": "Nacional", "home_goals": 0.0, "home_xg": 1.23, "source": "pipeline training history"}, {"away": "Alverca", "away_goals": 3.0, "away_xg": 1.16, "date": "2026-09-12T00:00:00+00:00", "home": "Nacional", "home_goals": 1.0, "home_xg": 2.2, "source": "pipeline training history"}, {"away": "Nacional", "away_goals": 0.0, "away_xg": 0.08, "date": "2026-09-05T00:00:00+00:00", "home": "Sp Lisbon", "home_goals": 2.0, "home_xg": 3.0, "source": "pipeline training history"}, {"away": "Estrela", "away_goals": 3.0, "away_xg": 2.1, "date": "2026-08-30T00:00:00+00:00", "home": "Nacional", "home_goals": 2.0, "home_xg": 0.84, "source": "pipeline training history"}, {"away": "Nacional", "away_goals": 0.0, "away_xg": 0.42, "date": "2026-08-23T00:00:00+00:00", "home": "Guimaraes", "home_goals": 1.0, "home_xg": 3.14, "source": "pipeline training history"}, {"away": "Estoril", "away_goals": 0.0, "away_xg": 0.82, "date": "2026-08-16T00:00:00+00:00", "home": "Nacional", "home_goals": 2.0, "home_xg": 2.08, "source": "pipeline training history"}], "h2h": [], "home": [{"away": "Santa Clara", "away_goals": 2.0, "away_xg": 0.82, "date": "2026-11-01T00:00:00+00:00", "home": "Maritimo", "home_goals": 0.0, "home_xg": 2.06, "source": "pipeline training history"}, {"away": "Maritimo", "away_goals": 0.0, "away_xg": 0.52, "date": "2026-10-23T00:00:00+00:00", "home": "Guimaraes", "home_goals": 5.0, "home_xg": 1.78, "source": "pipeline training history"}, {"away": "Porto", "away_goals": 2.0, "away_xg": 2.13, "date": "2026-10-10T00:00:00+00:00", "home": "Maritimo", "home_goals": 1.0, "home_xg": 0.19, "source": "pipeline training history"}, {"away": "Maritimo", "away_goals": 1.0, "away_xg": 0.86, "date": "2026-09-19T00:00:00+00:00", "home": "Gil Vicente", "home_goals": 1.0, "home_xg": 1.2, "source": "pipeline training history"}, {"away": "Maritimo", "away_goals": 1.0, "away_xg": 0.76, "date": "2026-09-14T00:00:00+00:00", "home": "Moreirense", "home_goals": 3.0, "home_xg": 1.99, "source": "pipeline training history"}, {"away": "Benfica", "away_goals": 3.0, "away_xg": 1.31, "date": "2026-09-05T00:00:00+00:00", "home": "Maritimo", "home_goals": 0.0, "home_xg": 0.13, "source": "pipeline training history"}, {"away": "Maritimo", "away_goals": 1.0, "away_xg": 0.67, "date": "2026-08-29T00:00:00+00:00", "home": "Arouca", "home_goals": 2.0, "home_xg": 1.66, "source": "pipeline training history"}, {"away": "Academico Viseu", "away_goals": 2.0, "away_xg": 1.84, "date": "2026-08-22T00:00:00+00:00", "home": "Maritimo", "home_goals": 2.0, "home_xg": 1.28, "source": "pipeline training history"}, {"away": "Maritimo", "away_goals": 2.0, "away_xg": 1.61, "date": "2026-08-16T00:00:00+00:00", "home": "Famalicao", "home_goals": 1.0, "home_xg": 0.59, "source": "pipeline training history"}, {"away": "Casa Pia", "away_goals": 0.0, "away_xg": 0.65, "date": "2026-08-08T00:00:00+00:00", "home": "Maritimo", "home_goals": 1.0, "home_xg": 1.28, "source": "pipeline training history"}], "teams": {"away": "Nacional", "home": "Maritimo"}} |
| Unadjusted home-win probability | 33.8% |
| Unadjusted draw probability | 25.2% |
| Unadjusted away-win probability | 41.0% |
| Raw p over 1 5 | 72.1% |
| Raw p under 3 5 | 74.2% |
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
| Unanchored p over 2 5 | 0.4741 |
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
| Research p home | 0.3313 |
| Research p draw | 0.2826 |
| Research p away | 0.3860 |
| Research p over 1 5 | 0.7219 |
| Research v4 p home | 0.3422 |
| Research v4 p draw | 0.2673 |
| Research v4 p away | 0.3905 |
| Research v4 p over 1 5 | 0.7201 |
| Research version | team-form-research-v5 |
| Research probability basis | team_form_poisson_v1 |
| Team research json | {"base_rates": [1.2089830881956938, 1.361168245747321], "c6_fit": {"candidate_version": "research-low-score-then-sharpen-walk-forward-v1", "delta": 0.055466179703356835, "end_exclusive": "2026-11-30", "expected_origin": "2026-11-16", "fits_version": "research-c6-live-fits-v1", "low_score_status": "fitted", "origin": "2026-11-16", "rho": -0.016463701485858812, "slope": 1.1507759984871408, "slope_status": "fitted", "stale": false}, "coverage": {"form": "last ten, exponential rank half-life five matches", "training_cache": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED", "venue_splits": "home team home matches / away team away matches", "xg": "verified supplied xG; no goals-to-xG substitution"}, "evidence": {"coverage": {}, "errors": ["free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"], "news": [], "quality_review": {"absence_note": "Reported absences only; not proof of complete coverage or a fitted player-value effect", "assessed_at_utc": "2026-11-24T16:35:48.323044+00:00", "availability": "UNAVAILABLE_OR_STALE", "form": {"away": {"matches": 10.0, "venue_matches": 4.0, "xg_matches": 10.0}, "home": {"matches": 10.0, "venue_matches": 5.0, "xg_matches": 10.0}}, "lineups": "UNCONFIRMED_OR_STALE", "probability_effect": "NONE; factual coverage/freshness review, not a calibrated confidence score", "status": "REVIEW_REQUIRED", "summary_max_age_minutes": 180, "training": {"cutoff": "2026-11-08", "status": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED"}, "version": "pre-match-research-quality-v1", "warnings": ["Research review: starting XIs not freshly confirmed for both teams; check before betting tight AH", "Research review: missing absence reports do not mean both teams have full squads", "Research review: match-window weather missing, incomplete or stale; no numerical weather adjustment", "Research review: inspect training status RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED; completeness/freshness not established by this review"], "weather": "UNAVAILABLE_INCOMPLETE_OR_STALE", "weather_max_age_minutes": 180}, "review_links": [{"label": "Sofascore", "status": "reference only; no authorized public bulk API", "url": "https://www.sofascore.com/football"}, {"label": "Sports Mole previews", "status": "reference only; article reproduction requires permission", "url": "https://www.sportsmole.co.uk/football/"}], "sources": [{"observed_at_utc": "2026-11-24T16:35:47.884284+00:00", "reason": null, "status": "available", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/por.1/scoreboard?dates=20261127"}, {"observed_at_utc": "2026-11-24T16:35:47.948908+00:00", "reason": null, "status": "available", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/por.1/news?limit=20"}, {"observed_at_utc": "2026-11-24T16:35:48.238809+00:00", "reason": null, "status": "available", "url": "https://www.bing.com/news/search?q=%22CS+Mar%C3%ADtimo%22+%22CD+Nacional%22+injury+suspension+lineup+preview&format=rss"}, {"observed_at_utc": "2026-11-24T16:35:21.826042+00:00", "reason": null, "status": "available", "url": "https://feeds.bbci.co.uk/sport/football/rss.xml"}, {"observed_at_utc": "2026-11-24T16:35:22.061091+00:00", "reason": null, "status": "available", "url": "https://www.theguardian.com/football/rss"}, {"observed_at_utc": "2026-11-24T16:35:48.322649+00:00", "reason": "TheSportsDB free source limit: 30 requests per minute", "status": "unavailable", "url": "https://www.thesportsdb.com/api/v1/json/123/searchevents.php?e=CS+Mar%C3%ADtimo_vs_CD+Nacional&d=2026-11-27"}]}, "evidence_quality_version": "pre-match-research-quality-v1", "form": {"away": {"all": {"goals_against": 1.5507048527234875, "goals_for": 0.8473887254235924, "last_match": "2026-11-08T00:00:00+00:00", "matches": 10, "points_per_game": 1.0589134132875462, "results": "WLWLLLLLLW", "xg_against": 1.4473966787066475, "xg_for": 0.943443703024997, "xg_matches": 10}, "venue": {"goals_against": 1.7599865214626136, "goals_for": 0.5295057548750894, "last_match": "2026-11-01T00:00:00+00:00", "matches": 4, "points_per_game": 0.0, "results": "LLLL", "xg_against": 1.9738427187746768, "xg_for": 0.5203791930565782, "xg_matches": 4}}, "home": {"all": {"goals_against": 2.3662591888570916, "goals_for": 0.7131841570421359, "last_match": "2026-11-01T00:00:00+00:00", "matches": 10, "points_per_game": 0.49878383320263503, "results": "LLLDLLLDWW", "xg_against": 1.4454419451949967, "xg_for": 0.932195130990825, "xg_matches": 10}, "venue": {"goals_against": 1.8988119457434338, "goals_for": 0.7157020266306037, "last_match": "2026-11-01T00:00:00+00:00", "matches": 5, "points_per_game": 0.6169046207669643, "results": "LLLDW", "xg_against": 1.3603430415604811, "xg_for": 1.0106319966707003, "xg_matches": 5}}}, "goal_rates": [1.2172291412959553, 1.319165561336447], "h2h": [], "margin_distribution": {"-1": 0.2105586893064564, "-10": 4.0000456159279295e-07, "-11": 4.739908517110232e-08, "-12": 5.156829232425683e-09, "-13": 5.159235588670191e-10, "-14": 4.3611464012902315e-11, "-2": 0.11328702270111128, "-3": 0.0443066153519603, "-4": 0.0135754988745768, "-5": 0.003405904009959573, "-6": 0.0007219762604186403, "-7": 0.00013234460725454586, "-8": 2.1355032652579813e-05, "-9": 3.0759917963977135e-06, "0": 0.28263833001981103, "1": 0.19028210412979374, "10": 1.7543103927976703e-07, "11": 1.918158488510438e-08, "12": 1.925618788140871e-09, "13": 1.777648785807682e-10, "14": 1.386546065987722e-11, "2": 0.09454473869843266, "3": 0.03411919796662987, "4": 0.009646262435142943, "5": 0.0022331027949754616, "6": 0.00043678957566429735, "7": 7.388029707847523e-05, "8": 1.1000075339300248e-05, "9": 1.4620210611678474e-06}, "model_note": "Poisson team rates with ten-match shrinkage; qualitative context has no fitted coefficient", "observed_at_utc": "2026-11-24T16:35:48.323044+00:00", "p_over_1_5": 0.7219049646983193, "shadow_v4": {"grid": "independent Poisson (C)", "margin_distribution": {"-1": 0.2139345212659302, "-10": 4.024426235822459e-07, "-11": 4.7687986646201375e-08, "-12": 5.188260547327725e-09, "-13": 5.190681570519205e-10, "-14": 4.3877279613331626e-11, "-2": 0.11397751678659383, "-3": 0.044576667959212564, "-4": 0.013658242700452619, "-5": 0.003426663285987183, "-6": 0.0007263767674298726, "-7": 0.00013315125894664546, "-8": 2.148519340171343e-05, "-9": 3.0947402292875884e-06, "0": 0.26734421098275934, "1": 0.19740307149185338, "10": 1.8006708477341245e-07, "11": 1.968848891151074e-08, "12": 1.9765063411183284e-09, "13": 1.8246259950664455e-10, "14": 1.4231877610226757e-11, "2": 0.09704323446970696, "3": 0.03502085228407217, "4": 0.009901180331523003, "5": 0.002292116104091091, "6": 0.0004483324380462527, "7": 7.583270196501091e-05, "8": 1.1290769904617143e-05, "9": 1.5006573035344722e-06}, "p_over_1_5": 0.7200899395300444, "version": "team-form-research-v4"}, "version": "team-form-research-v5", "warnings": ["availability unavailable or unconfirmed", "lineups unavailable or unconfirmed", "rotation unavailable or unconfirmed", "h2h unavailable or unconfirmed", "tactics unavailable or unconfirmed", "motivation unavailable or unconfirmed", "rivalry unavailable or unconfirmed", "weather unavailable or unconfirmed", "travel unavailable or unconfirmed", "free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing", "Research review: starting XIs not freshly confirmed for both teams; check before betting tight AH", "Research review: missing absence reports do not mean both teams have full squads", "Research review: match-window weather missing, incomplete or stale; no numerical weather adjustment", "Research review: inspect training status RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED; completeness/freshness not established by this review"]} |

</details>
