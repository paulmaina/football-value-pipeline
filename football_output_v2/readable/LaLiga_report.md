# La Liga — football model report

Fixtures in this report: **7**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | La Liga |
| Training matches | 1,994 |
| Training data through | 2026-10-24 |
| Model fit succeeded | Yes |
| Recency half-life (days) | 730 |
| Maximum goals per team in score matrix | 10 |
| Bookmaker margin-removal method | power |
| Market blending weight | 50.0% |

<details>
<summary>Technical model diagnostics</summary>

| Parameter | Value |
| --- | --- |
| Training seasons requested | 6 |
| Training seasons loaded | ['2122', '2223', '2324', '2425', '2526', '2627'] |
| Training sha256 | e14c45ea8051650af8323cc965674746e5b9df7dccd04f05893ab6942a3f97a3 |
| Training as of utc | 2026-10-25T10:18:26.012941+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 94, 'bbs_added_results': 5, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 94, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 574, 'added_results': 0, 'conflicts': 0, 'unmapped': 566, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 54, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_RETROSPECTIVE_EXAMPLES', 'cutoff_utc': '2026-10-25T10:18:26.012941+00:00', 'observations': 307, 'observations_sha256': '2ff2d7b6d9494da499d3d2bb236b8ea72da64e716024b558860d8aaf8e8c88a5', 'eligible_training_matches': 102, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 125, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 15, 'retrospective_eligible_training_matches': 102, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:27.155286+00:00', 'retrospective_inputs_sha256': 'f3a69c098245ee69662f66773339d330c59b9d32a5717e27d444bcfef3daae8a', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'input_providers': ['api-football', 'bigballsdata']} |
| Optimizer objective | 2512.485 |
| Base scoring parameter | 0.092 |
| Home-advantage parameter | 0.281 |
| Dixon-Coles low-score adjustment | -0.023 |
| Xi per day | 0.0009 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 29, 'matches': 1994, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-10-24'} |
| Training data health | {'training_end': '2026-10-24', 'days_since_latest_result': 1, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 7.00 |
| Additional event odds calls used before this league | 5.00 |
| Bbs statistics model artifact | bbs/feature_models/LaLiga/20261025T101826012941Z_3ef75cb45d9cd4bf65d46e73c6ab1c6c139b467e939131a61211ba4a4052f457.json |
| Over 1 5 in window quote fixtures | 2 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 5.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 5.00 |
| Bbs statistics applied fixtures | 0 |
| Decay tuning | {'selected_half_life_days': 730.0, 'selected_xi_per_day': 0.0009495166856985552, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365} |
| Goal market reliability | {'home_draw': 'RELIABLE_FOR_RANKING', 'draw_away': 'RELIABLE_FOR_RANKING', 'home_away': 'RELIABLE_FOR_RANKING', 'home': 'RELIABLE_FOR_RANKING', 'draw': 'RELIABLE_FOR_RANKING', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'RELIABLE_FOR_RANKING', 'under_3_5': 'RELIABLE_FOR_RANKING', 'btts_yes': 'UNRELIABLE_AUDIT'} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-24 — Atlético Madrid vs Deportivo La Coruña

The model's most likely 1X2 outcome is **Atlético Madrid win** at **69.9%**. Expected goals are 2.01 for Atlético Madrid and 0.82 for Deportivo La Coruña (2.82 combined). The most likely exact score is 2-0 at 12.9%. Goal-market probabilities: at least one goal: 94.6%; Over 2.5 goals: 54.9%; Under 3.5 goals: 68.0%; Double Chance 1X: 88.1%; Double Chance X2: 30.1%; Double Chance 12 (either team wins): 81.8%; Under 4.5 goals: 83.8%; BTTS Yes (both teams score): 47.5%; BTTS No (at least one team does not score): 52.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Atlético Madrid win | 69.9% | 1.43 |
| Draw | 18.2% | 5.51 |
| Deportivo La Coruña win | 11.9% | 8.38 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Atlético Madrid expected goals | 2.01 |
| Deportivo La Coruña expected goals | 0.82 |
| Expected total goals | 2.82 |
| Over 0.5 | 94.6% |
| Under 0.5 | 5.4% |
| Over 1.5 | 78.1% |
| Under 1.5 | 21.9% |
| Over 2.5 | 54.9% |
| Under 2.5 | 45.1% |
| Over 3.5 | 32.0% |
| Under 3.5 | 68.0% |
| Over 4.5 | 16.2% |
| Under 4.5 | 83.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 12.89% |
| 2 | 1-0 | 12.60% |
| 3 | 2-1 | 10.50% |
| 4 | 1-1 | 8.64% |
| 5 | 3-0 | 8.62% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Atlético Madrid win | 69.9% | 74.8% | 1.28 | -10.5% |
| Draw | 18.2% | 15.4% | 6.01 | +9.1% |
| Deportivo La Coruña win | 11.9% | 9.8% | 11.15 | +33.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T19:00:00+00:00 |
| Fixture id | 70df1835c3b5ddff1c99e0189532136b |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-24T14:43:14Z |
| Market best draw last update utc | 2026-10-24T14:43:14Z |
| Market best away last update utc | 2026-10-24T14:43:14Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 8.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Ath Madrid |
| Matched away-team name | La Coruna |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| Dc lambda home | 2.0076 |
| Dc lambda away | 0.8152 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-25T10:18:26.012941+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 47.5% |
| P btts no | 52.5% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 18.67 |
| Fair Over 1.5 odds | 1.28 |
| Fair Under 1.5 odds | 4.57 |
| Fair Over 2.5 odds | 1.82 |
| Fair Under 2.5 odds | 2.22 |
| Fair Over 3.5 odds | 3.12 |
| Fair Under 3.5 odds | 1.47 |
| Fair Over 4.5 odds | 6.18 |
| Fair Under 4.5 odds | 1.19 |
| Goal margin distribution | {"-1": 0.08314205076515484, "-10": 2.0809786521809415e-09, "-11": 1.52345040482043e-10, "-12": 1.0242467772114402e-11, "-13": 6.365803011041249e-13, "-14": 3.678110794820228e-14, "-15": 1.9851414884803686e-15, "-16": 1.0014031201569931e-16, "-17": 4.380190694802005e-18, "-2": 0.027895946840883153, "-3": 0.006728559778799911, "-4": 0.0012723226545358248, "-5": 0.00019707428681534433, "-6": 2.5797661931683525e-05, "-7": 2.9207318018765113e-06, "-8": 2.911123543641219e-07, "-9": 2.5903247037874003e-08, "0": 0.18152172696077187, "1": 0.2639169930280068, "10": 2.1729764946976135e-05, "11": 3.917868517396162e-06, "12": 6.48724463710112e-07, "13": 9.929857083083272e-08, "14": 1.4130214117956865e-08, "15": 1.878233293729868e-09, "16": 2.3334641975584477e-10, "17": 2.513734194397825e-11, "2": 0.21520653059275127, "3": 0.12784112612554402, "4": 0.059536029185616866, "5": 0.022711546204159692, "6": 0.007322025190152274, "7": 0.002041628332256042, "8": 0.0005011638929810947, "9": 0.00010982658456431272} |
| Raw goal margin distribution | {"-1": 0.09830616188834267, "-10": 2.4605241557647766e-09, "-11": 1.8013094546845756e-10, "-12": 1.2110570832390455e-11, "-13": 7.526848996308311e-13, "-14": 4.348954011973903e-14, "-15": 2.3472074448710305e-15, "-16": 1.184047017600186e-16, "-17": 5.179084850352093e-18, "-2": 0.03298383238001373, "-3": 0.007955768240050622, "-4": 0.0015043790200015734, "-5": 0.00023301826891932372, "-6": 3.0502845513881552e-05, "-7": 3.4534381904859e-06, "-8": 3.4420775013899374e-07, "-9": 3.062768807485564e-08, "0": 0.20896717004647028, "1": 0.2453473033871497, "10": 2.020081833992192e-05, "11": 3.6422000142542995e-06, "12": 6.030790059648054e-07, "13": 9.231173902075087e-08, "14": 1.3135986017224182e-08, "15": 1.7460773118905809e-09, "16": 2.1692773241042112e-10, "17": 2.3368631892609032e-11, "2": 0.20006419952895005, "3": 0.11884598713031795, "4": 0.05534696363231016, "5": 0.02111351964498897, "6": 0.0068068339030598335, "7": 0.0018979755721325127, "8": 0.0004659010709661626, "9": 0.00010209898216071072} |
| Unadjusted home-win probability | 65.0% |
| Unadjusted draw probability | 20.9% |
| Unadjusted away-win probability | 14.1% |
| Raw p over 1 5 | 77.5% |
| Raw p under 3 5 | 68.7% |
| Raw p btts yes | 48.5% |
| P home draw | 88.1% |
| P draw away | 30.1% |
| P home away | 81.8% |
| Raw p home draw | 85.9% |
| Raw p draw away | 35.0% |
| Raw p home away | 79.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.32 |
| Reference draw odds | 6.00 |
| Reference away odds | 9.30 |
| Market reference 1x2 last update utc | 2026-10-24T14:43:20Z |
| Market reference home last update utc | 2026-10-24T14:43:20Z |
| Market reference draw last update utc | 2026-10-24T14:43:20Z |
| Market reference away last update utc | 2026-10-24T14:43:20Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.65 |
| Reference Under 2.5 odds | 2.44 |
| Market reference over 2 5 last update utc | 2026-10-24T14:43:14Z |
| Market reference under 2 5 last update utc | 2026-10-24T14:43:14Z |
| Home probability edge | -4.9% |
| Draw probability edge | +2.7% |
| Away probability edge | +2.2% |
| Over 2.5 probability edge | -4.9% |
| Under 2.5 probability edge | +4.9% |
| Raw edge prob home | -0.0984 |
| Raw ev home | -0.1680 |
| Raw edge prob draw | 0.0549 |
| Raw ev draw | 0.2559 |
| Raw edge prob away | 0.0435 |
| Raw ev away | 0.5723 |
| Count model | {"corners": {"alpha": 0.01460129601713404, "mu": 10.666991839562744, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,650.0417 |
| Elo away rating | 1,441.7911 |
| Elo rating diff | 268.2506 |
| Elo home expectancy | 0.8241 |

</details>


---

## 2026-10-24 — Valencia vs Villarreal

The model's most likely 1X2 outcome is **Villarreal win** at **45.0%**. Expected goals are 1.26 for Valencia and 1.56 for Villarreal (2.81 combined). The most likely exact score is 1-1 at 12.2%. Goal-market probabilities: at least one goal: 93.6%; Over 2.5 goals: 53.2%; Under 3.5 goals: 68.9%; Double Chance 1X: 55.0%; Double Chance X2: 70.7%; Double Chance 12 (either team wins): 74.3%; Under 4.5 goals: 84.6%; BTTS Yes (both teams score): 56.7%; BTTS No (at least one team does not score): 43.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Valencia win | 29.3% | 3.42 |
| Draw | 25.7% | 3.88 |
| Villarreal win | 45.0% | 2.22 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Valencia expected goals | 1.26 |
| Villarreal expected goals | 1.56 |
| Expected total goals | 2.81 |
| Over 0.5 | 93.6% |
| Under 0.5 | 6.4% |
| Over 1.5 | 77.4% |
| Under 1.5 | 22.6% |
| Over 2.5 | 53.2% |
| Under 2.5 | 46.8% |
| Over 3.5 | 31.1% |
| Under 3.5 | 68.9% |
| Over 4.5 | 15.4% |
| Under 4.5 | 84.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.16% |
| 2 | 1-2 | 9.33% |
| 3 | 0-1 | 9.28% |
| 4 | 0-2 | 7.43% |
| 5 | 2-1 | 7.07% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Valencia win | 29.3% | 28.0% | 3.55 | +3.9% |
| Draw | 25.7% | 26.1% | 3.70 | -4.7% |
| Villarreal win | 45.0% | 46.0% | 2.10 | -5.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T16:30:00+00:00 |
| Fixture id | 0dae715cc56fe201f9e667917c126691 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-24T14:43:14Z |
| Market best draw last update utc | 2026-10-24T14:43:14Z |
| Market best away last update utc | 2026-10-24T14:43:14Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Valencia |
| Matched away-team name | Villarreal |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.2563 |
| Dc lambda away | 1.5550 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-25T10:18:26.012941+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 56.7% |
| P btts no | 43.3% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.73 |
| Fair Over 1.5 odds | 1.29 |
| Fair Under 1.5 odds | 4.42 |
| Fair Over 2.5 odds | 1.88 |
| Fair Under 2.5 odds | 2.14 |
| Fair Over 3.5 odds | 3.22 |
| Fair Under 3.5 odds | 1.45 |
| Fair Over 4.5 odds | 6.50 |
| Fair Under 4.5 odds | 1.18 |
| Goal margin distribution | {"-1": 0.22204078603979452, "-10": 1.6701336971022429e-06, "-11": 2.326988695280172e-07, "-12": 2.9785048462033626e-08, "-13": 3.5241993417601897e-09, "-14": 3.851782409917225e-10, "-15": 3.532953092809557e-11, "-2": 0.1361762731187125, "-3": 0.06142763055515403, "-4": 0.02186952504400315, "-5": 0.0064025629557284205, "-6": 0.001587928458094456, "-7": 0.00034116008505104094, "-8": 6.459811347364408e-05, "-9": 1.0928199692078616e-05, "0": 0.2574840717219766, "1": 0.16763308473843522, "10": 1.854544949399737e-07, "11": 2.0875922968278632e-08, "12": 2.1588129274287785e-09, "13": 2.0636804574207402e-10, "14": 1.822254444272076e-11, "15": 1.3503626919601296e-12, "2": 0.08330388872772482, "3": 0.030359378835968044, "4": 0.008732402713393794, "5": 0.0020654445918958275, "6": 0.00041386234123205246, "7": 7.183704824449137e-05, "8": 1.098943556274628e-05, "9": 1.5019983685079354e-06} |
| Raw goal margin distribution | {"-1": 0.21723015450184255, "-10": 1.6339493636778586e-06, "-11": 2.2765732495162296e-07, "-12": 2.9139739570606783e-08, "-13": 3.4478456915958348e-09, "-14": 3.768331498627642e-10, "-15": 3.4564097879802885e-11, "-2": 0.13322594184908615, "-3": 0.06009676831979281, "-4": 0.02139571017073993, "-5": 0.006263848029394888, "-6": 0.0015535251448259132, "-7": 0.0003337686706451185, "-8": 6.319856104225962e-05, "-9": 1.069143444264229e-05, "0": 0.25439046032486096, "1": 0.174990243049491, "10": 1.9359380753986563e-07, "11": 2.1792135125363746e-08, "12": 2.2535599070946956e-09, "13": 2.154252219268152e-10, "14": 1.902230389655731e-11, "15": 1.4096280339873073e-12, "2": 0.08695996830326182, "3": 0.031691805287882666, "4": 0.009115654440214765, "5": 0.0021560937788925494, "6": 0.0004320261229710774, "7": 7.49898658243763e-05, "8": 1.1471744990568519e-05, "9": 1.5679187672007284e-06} |
| Unadjusted home-win probability | 30.5% |
| Unadjusted draw probability | 25.4% |
| Unadjusted away-win probability | 44.0% |
| Raw p over 1 5 | 77.4% |
| Raw p under 3 5 | 68.9% |
| Raw p btts yes | 56.7% |
| P home draw | 55.0% |
| P draw away | 70.7% |
| P home away | 74.3% |
| Raw p home draw | 56.0% |
| Raw p draw away | 69.5% |
| Raw p home away | 74.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 3.40 |
| Reference draw odds | 3.64 |
| Reference away odds | 2.11 |
| Market reference 1x2 last update utc | 2026-10-24T14:43:20Z |
| Market reference home last update utc | 2026-10-24T14:43:20Z |
| Market reference draw last update utc | 2026-10-24T14:43:20Z |
| Market reference away last update utc | 2026-10-24T14:43:20Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.74 |
| Reference Under 2.5 odds | 2.12 |
| Market reference over 2 5 last update utc | 2026-10-24T14:43:20Z |
| Market reference under 2 5 last update utc | 2026-10-24T14:43:20Z |
| Home probability edge | +1.3% |
| Draw probability edge | -0.3% |
| Away probability edge | -1.0% |
| Over 2.5 probability edge | -2.0% |
| Under 2.5 probability edge | +2.0% |
| Raw edge prob home | 0.0257 |
| Raw ev home | 0.0843 |
| Raw edge prob draw | -0.0062 |
| Raw ev draw | -0.0588 |
| Raw edge prob away | -0.0195 |
| Raw ev away | -0.0756 |
| Count model | {"corners": {"alpha": 0.01460129601713404, "mu": 9.873997057540466, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,456.5878 |
| Elo away rating | 1,556.2139 |
| Elo rating diff | -39.6261 |
| Elo home expectancy | 0.4432 |

</details>


---

## 2026-10-25 — Athletic Bilbao vs Getafe

The model's most likely 1X2 outcome is **Athletic Bilbao win** at **55.7%**. Expected goals are 1.20 for Athletic Bilbao and 0.63 for Getafe (1.82 combined). The most likely exact score is 1-0 at 21.4%. Goal-market probabilities: at least one goal: 85.6%; Over 2.5 goals: 28.9%; Under 3.5 goals: 88.4%; Double Chance 1X: 83.1%; Double Chance X2: 44.3%; Double Chance 12 (either team wins): 72.6%; Under 4.5 goals: 96.0%; BTTS Yes (both teams score): 31.8%; BTTS No (at least one team does not score): 68.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Athletic Bilbao win | 55.7% | 1.79 |
| Draw | 27.4% | 3.66 |
| Getafe win | 16.9% | 5.92 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Athletic Bilbao expected goals | 1.20 |
| Getafe expected goals | 0.63 |
| Expected total goals | 1.82 |
| Over 0.5 | 85.6% |
| Under 0.5 | 14.4% |
| Over 1.5 | 55.5% |
| Under 1.5 | 44.5% |
| Over 2.5 | 28.9% |
| Under 2.5 | 71.1% |
| Over 3.5 | 11.6% |
| Under 3.5 | 88.4% |
| Over 4.5 | 4.0% |
| Under 4.5 | 96.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 21.43% |
| 2 | 0-0 | 14.37% |
| 3 | 2-0 | 12.99% |
| 4 | 1-1 | 10.83% |
| 5 | 0-1 | 8.71% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Athletic Bilbao win | 55.7% | 61.9% | 1.60 | -10.8% |
| Draw | 27.4% | 23.4% | 4.12 | +12.7% |
| Getafe win | 16.9% | 14.7% | 5.90 | -0.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T13:00:00+00:00 |
| Fixture id | 9c4254cba9944a839b421db27260504d |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-24T14:43:14Z |
| Market best draw last update utc | 2026-10-24T14:43:14Z |
| Market best away last update utc | 2026-10-24T14:43:14Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Ath Bilbao |
| Matched away-team name | Getafe |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.1953 |
| Dc lambda away | 0.6268 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-25T10:18:26.012941+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 31.8% |
| P btts no | 68.2% |
| Fair Over 0.5 odds | 1.17 |
| Fair Under 0.5 odds | 6.96 |
| Fair Over 1.5 odds | 1.80 |
| Fair Under 1.5 odds | 2.25 |
| Fair Over 2.5 odds | 3.46 |
| Fair Under 2.5 odds | 1.41 |
| Fair Over 3.5 odds | 8.61 |
| Fair Under 3.5 odds | 1.13 |
| Fair Over 4.5 odds | 24.72 |
| Fair Under 4.5 odds | 1.04 |
| Goal margin distribution | {"-1": 0.12504206817521824, "-10": 3.939751453094805e-10, "-11": 2.2321387012729854e-11, "-12": 1.1586225813668704e-12, "-13": 5.28165995561205e-14, "-2": 0.03573944704943988, "-3": 0.007042582046790245, "-4": 0.0010645881100647724, "-5": 0.00013025280288442396, "-6": 1.3370921637598537e-05, "-7": 1.1815572464851309e-06, "-8": 9.162421345054112e-08, "-9": 6.32843079443803e-09, "0": 0.2735319115923543, "1": 0.30655575930017054, "10": 3.1926511747310675e-07, "11": 3.4495516857597325e-08, "12": 3.4146193769765313e-09, "13": 2.96844893083416e-10, "2": 0.16556167538510846, "3": 0.06221609250954603, "4": 0.0179354080041222, "5": 0.004184808216054958, "6": 0.0008192353021916368, "7": 0.00013805778962197284, "8": 2.0416215446614812e-05, "9": 2.6891798510135397e-06} |
| Raw goal margin distribution | {"-1": 0.14160035078528083, "-10": 4.461460018266133e-10, "-11": 2.527722291499152e-11, "-12": 1.3120493474196334e-12, "-13": 5.981066319178639e-14, "-2": 0.04047212520494465, "-3": 0.00797517269837719, "-4": 0.0012055626720422947, "-5": 0.00014750109981670796, "-6": 1.5141521744133213e-05, "-7": 1.3380210597663766e-06, "-8": 1.0375724709576863e-07, "-9": 7.166452326724997e-09, "0": 0.31300961717490505, "1": 0.27253566440991145, "10": 2.838345986781569e-07, "11": 3.0667369053546784e-08, "12": 3.035681217458501e-09, "13": 2.6390246377319614e-10, "2": 0.14718843092331854, "3": 0.05531164753774766, "4": 0.01594502203457238, "5": 0.003720398175503988, "6": 0.0007283204787949585, "7": 0.0001227367951183921, "8": 1.815052130868895e-05, "9": 2.3907475073599576e-06} |
| Unadjusted home-win probability | 49.6% |
| Unadjusted draw probability | 31.3% |
| Unadjusted away-win probability | 19.1% |
| Raw p over 1 5 | 54.6% |
| Raw p under 3 5 | 88.8% |
| Raw p btts yes | 32.8% |
| P home draw | 83.1% |
| P draw away | 44.3% |
| P home away | 72.6% |
| Raw p home draw | 80.9% |
| Raw p draw away | 50.4% |
| Raw p home away | 68.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:43:14Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.89, "price": 1.49, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:18:32Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.01, "price": 1.91, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:18:32Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.91, "price": 2.01, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:43:14Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.49, "price": 2.89, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:18:32Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 5.16, "price": 1.2, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:18:32Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 4.67, "price": 1.23, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:18:32Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 3.33, "price": 1.37, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:18:32Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 3.28, "price": 1.38, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:18:32Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.71, "price": 1.52, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:18:32Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.58, "price": 1.56, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:18:32Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.36, "price": 1.66, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:18:32Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.24, "price": 1.72, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:18:32Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.72, "price": 2.24, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:18:32Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.66, "price": 2.36, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:18:32Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.56, "price": 2.58, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:18:32Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.52, "price": 2.71, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:18:32Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 3.28, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:18:32Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.37, "price": 3.33, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:18:32Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.23, "price": 4.67, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:18:32Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.2, "price": 5.16, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.58 |
| Reference draw odds | 4.00 |
| Reference away odds | 6.25 |
| Market reference 1x2 last update utc | 2026-10-24T14:43:20Z |
| Market reference home last update utc | 2026-10-24T14:43:20Z |
| Market reference draw last update utc | 2026-10-24T14:43:20Z |
| Market reference away last update utc | 2026-10-24T14:43:20Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 2.31 |
| Reference Under 2.5 odds | 1.63 |
| Market reference over 2 5 last update utc | 2026-10-24T14:43:20Z |
| Market reference under 2 5 last update utc | 2026-10-24T14:43:20Z |
| Home probability edge | -6.2% |
| Draw probability edge | +3.9% |
| Away probability edge | +2.2% |
| Over 2.5 probability edge | -11.9% |
| Under 2.5 probability edge | +11.9% |
| Raw edge prob home | -0.1237 |
| Raw ev home | -0.2071 |
| Raw edge prob draw | 0.0790 |
| Raw ev draw | 0.2896 |
| Raw edge prob away | 0.0448 |
| Raw ev away | 0.1294 |
| Count model | {"corners": {"alpha": 0.01460129601713404, "mu": 9.81489003483115, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,491.3653 |
| Elo away rating | 1,456.5803 |
| Elo rating diff | 94.7851 |
| Elo home expectancy | 0.6331 |
| Market p home draw | 85.1% |
| Market home draw odds | 1.14 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-25T10:18:22Z |
| Market reference home draw last update utc | 2026-10-25T10:18:33Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 38.5% |
| Market draw away odds | 2.55 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-25T10:18:22Z |
| Market reference draw away last update utc | 2026-10-25T10:18:33Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 76.4% |
| Market home away odds | 1.28 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-25T10:18:22Z |
| Market reference home away last update utc | 2026-10-25T10:18:33Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.14 |
| Market reference dc draw away odds | 2.52 |
| Market reference dc home away odds | 1.27 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:18:22Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 2.4, "price": 1.56, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:18:22Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 1.56, "price": 2.4, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:18:22Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.88, "price": 1.96, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:18:22Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.96, "price": 1.88, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:18:22Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 1.53, "price": 2.47, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:18:22Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 2.47, "price": 1.53, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 69.9% |
| Market over 1 5 odds | 1.39 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-25T10:18:32Z |
| Market reference over 1 5 odds | 1.36 |
| Market reference over 1 5 opposite odds | 2.80 |
| Market reference over 1 5 last update utc | 2026-10-25T10:18:33Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 78.9% |
| Market reference under 3 5 odds | 1.22 |
| Market reference under 3 5 opposite odds | 3.70 |
| Market reference under 3 5 last update utc | 2026-10-25T10:18:33Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 42.1% |
| Market btts yes odds | 2.32 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-25T10:18:22Z |
| Market reference btts yes odds | 2.17 |
| Market reference btts yes opposite odds | 1.63 |
| Market reference btts yes last update utc | 2026-10-25T10:18:33Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-25 — Barcelona vs Real Madrid

The model's most likely 1X2 outcome is **Barcelona win** at **56.4%**. Expected goals are 1.97 for Barcelona and 1.35 for Real Madrid (3.32 combined). The most likely exact score is 2-1 at 10.3%. Goal-market probabilities: at least one goal: 96.7%; Over 2.5 goals: 65.5%; Under 3.5 goals: 57.2%; Double Chance 1X: 75.9%; Double Chance X2: 43.6%; Double Chance 12 (either team wins): 80.5%; Under 4.5 goals: 75.2%; BTTS Yes (both teams score): 63.2%; BTTS No (at least one team does not score): 36.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Barcelona win | 56.4% | 1.77 |
| Draw | 19.5% | 5.13 |
| Real Madrid win | 24.1% | 4.14 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Barcelona expected goals | 1.97 |
| Real Madrid expected goals | 1.35 |
| Expected total goals | 3.32 |
| Over 0.5 | 96.7% |
| Under 0.5 | 3.3% |
| Over 1.5 | 84.8% |
| Under 1.5 | 15.2% |
| Over 2.5 | 65.5% |
| Under 2.5 | 34.5% |
| Over 3.5 | 42.8% |
| Under 3.5 | 57.2% |
| Over 4.5 | 24.8% |
| Under 4.5 | 75.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 10.34% |
| 2 | 1-1 | 8.60% |
| 3 | 2-0 | 7.64% |
| 4 | 1-0 | 7.52% |
| 5 | 3-1 | 6.78% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Barcelona win | 56.4% | 61.1% | 1.64 | -7.6% |
| Draw | 19.5% | 16.7% | 6.01 | +17.2% |
| Real Madrid win | 24.1% | 22.2% | 3.83 | -7.6% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T20:00:00+00:00 |
| Fixture id | 72089d103a5fe6a922c35e17efba6ffc |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-24T14:43:14Z |
| Market best draw last update utc | 2026-10-24T14:43:14Z |
| Market best away last update utc | 2026-10-24T14:43:14Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Barcelona |
| Matched away-team name | Real Madrid |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.9692 |
| Dc lambda away | 1.3537 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-25T10:18:26.012941+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 63.2% |
| P btts no | 36.8% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 29.91 |
| Fair Over 1.5 odds | 1.18 |
| Fair Under 1.5 odds | 6.59 |
| Fair Over 2.5 odds | 1.53 |
| Fair Under 2.5 odds | 2.90 |
| Fair Over 3.5 odds | 2.34 |
| Fair Under 3.5 odds | 1.75 |
| Fair Over 4.5 odds | 4.04 |
| Fair Under 4.5 odds | 1.33 |
| Goal margin distribution | {"-1": 0.13673277006915735, "-10": 2.412241635919223e-07, "-11": 2.9107669842096875e-08, "-12": 3.2291722036270983e-09, "-13": 3.3144966270488935e-10, "-14": 3.163091494836958e-11, "-15": 2.792544690491193e-12, "-16": 2.0252416784652148e-13, "-2": 0.06850538423254934, "-3": 0.02580685663416983, "-4": 0.007777192316809572, "-5": 0.0019428301386465907, "-6": 0.0004132559510845645, "-7": 7.640661516630516e-05, "-8": 1.2479828244494206e-05, "-9": 1.824314466651105e-06, "0": 0.1950673609028778, "1": 0.2361327122229246, "10": 1.2094074396181803e-05, "11": 2.1228657013923038e-06, "12": 3.4258594302450345e-07, "13": 5.115159359913789e-08, "14": 7.100952293775427e-09, "15": 9.119441171831366e-10, "16": 9.620733927393764e-11, "2": 0.17130518381839588, "3": 0.09387374875906916, "4": 0.0411523977131228, "5": 0.014954448143512104, "6": 0.004627196352987806, "7": 0.0012444946297469125, "8": 0.00029568815536310666, "9": 6.287648788597134e-05} |
| Raw goal margin distribution | {"-1": 0.14790838239543075, "-10": 2.6094019607388957e-07, "-11": 3.1486734010195746e-08, "-12": 3.493102910686288e-09, "-13": 3.5854011756944315e-10, "-14": 3.4216212114583e-11, "-15": 3.020788416182832e-12, "-16": 2.1907712428417054e-13, "-2": 0.07410455125050817, "-3": 0.027916134643803714, "-4": 0.008412847443781518, "-5": 0.0021016239408516695, "-6": 0.0004470326989593467, "-7": 8.26515753892971e-05, "-8": 1.3499845042869625e-05, "-9": 1.973421598980781e-06, "0": 0.22304547205159098, "1": 0.216150895384809, "10": 1.10706601596024e-05, "11": 1.9432264078026345e-06, "12": 3.1359593354895837e-07, "13": 4.682308796917347e-08, "14": 6.50006168961185e-09, "15": 8.347743758770384e-10, "16": 8.806616555108895e-11, "2": 0.1568091456614827, "3": 0.08593004610155615, "4": 0.037670035333883266, "5": 0.013688985849424476, "6": 0.004235637770828673, "7": 0.001139184088426636, "8": 0.00027066668965407785, "9": 5.75558084572975e-05} |
| Unadjusted home-win probability | 51.6% |
| Unadjusted draw probability | 22.3% |
| Unadjusted away-win probability | 26.1% |
| Raw p over 1 5 | 84.6% |
| Raw p under 3 5 | 57.5% |
| Raw p btts yes | 64.0% |
| P home draw | 75.9% |
| P draw away | 43.6% |
| P home away | 80.5% |
| Raw p home draw | 73.9% |
| Raw p draw away | 48.4% |
| Raw p home away | 77.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:43:14Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.43, "price": 1.66, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:18:32Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.0, "price": 1.93, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:18:32Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.93, "price": 2.0, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:43:14Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.66, "price": 2.43, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:18:32Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 3.56, "price": 1.3, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:18:32Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 3.21, "price": 1.36, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:18:32Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.88, "price": 1.45, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:18:32Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.71, "price": 1.49, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:18:32Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.48, "price": 1.59, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:18:32Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.38, "price": 1.63, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:18:32Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.24, "price": 1.72, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:18:32Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.15, "price": 1.77, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:18:32Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.77, "price": 2.15, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:18:32Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.72, "price": 2.24, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:18:32Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.63, "price": 2.38, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:18:32Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.59, "price": 2.48, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:18:32Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.49, "price": 2.71, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:18:32Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.45, "price": 2.88, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:18:32Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.36, "price": 3.21, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:18:32Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.56, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.61 |
| Reference draw odds | 5.65 |
| Reference away odds | 4.30 |
| Market reference 1x2 last update utc | 2026-10-24T14:43:20Z |
| Market reference home last update utc | 2026-10-24T14:43:20Z |
| Market reference draw last update utc | 2026-10-24T14:43:20Z |
| Market reference away last update utc | 2026-10-24T14:43:20Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.15 |
| Reference Under 2.5 odds | 5.20 |
| Market reference over 2 5 last update utc | 2026-10-24T14:42:50Z |
| Market reference under 2 5 last update utc | 2026-10-24T14:42:50Z |
| Home probability edge | -4.8% |
| Draw probability edge | +2.8% |
| Away probability edge | +2.0% |
| Over 2.5 probability edge | -19.6% |
| Under 2.5 probability edge | +19.6% |
| Raw edge prob home | -0.0954 |
| Raw ev home | -0.1538 |
| Raw edge prob draw | 0.0560 |
| Raw ev draw | 0.3405 |
| Raw edge prob away | 0.0394 |
| Raw ev away | -0.0004 |
| Count model | {"corners": {"alpha": 0.01460129601713404, "mu": 10.654616418300819, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,739.3786 |
| Elo away rating | 1,656.5478 |
| Elo rating diff | 142.8309 |
| Elo home expectancy | 0.6947 |
| Market p home draw | 75.1% |
| Market home draw odds | 1.27 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-25T10:18:23Z |
| Market reference home draw last update utc | 2026-10-25T10:18:33Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 42.1% |
| Market draw away odds | 2.41 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-25T10:18:23Z |
| Market reference draw away last update utc | 2026-10-25T10:18:33Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 82.8% |
| Market home away odds | 1.17 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-25T10:18:23Z |
| Market reference home away last update utc | 2026-10-25T10:18:33Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.29 |
| Market reference dc draw away odds | 2.30 |
| Market reference dc home away odds | 1.17 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:18:23Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 2.44, "price": 1.53, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:18:23Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.53, "price": 2.44, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:18:23Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 1.96, "price": 1.87, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:18:23Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 1.87, "price": 1.96, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:18:23Z", "line": 11.5, "market_key": "alternate_totals_corners", "opposite_price": 1.57, "price": 2.34, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:18:23Z", "line": 11.5, "market_key": "alternate_totals_corners", "opposite_price": 2.34, "price": 1.57, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 93.5% |
| Market reference over 1 5 odds | 1.05 |
| Market reference over 1 5 opposite odds | 7.20 |
| Market reference over 1 5 last update utc | 2026-10-25T10:18:33Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 39.5% |
| Market under 3 5 odds | 2.41 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-25T10:18:32Z |
| Market reference under 3 5 odds | 2.25 |
| Market reference under 3 5 opposite odds | 1.55 |
| Market reference under 3 5 last update utc | 2026-10-25T10:18:33Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 78.0% |
| Market btts yes odds | 1.33 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-25T10:18:23Z |
| Market reference btts yes odds | 1.24 |
| Market reference btts yes opposite odds | 3.72 |
| Market reference btts yes last update utc | 2026-10-25T10:18:33Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-25 — Celta Vigo vs Real Betis

The model's most likely 1X2 outcome is **Real Betis win** at **38.0%**. Expected goals are 1.42 for Celta Vigo and 1.29 for Real Betis (2.70 combined). The most likely exact score is 1-1 at 12.8%. Goal-market probabilities: at least one goal: 92.9%; Over 2.5 goals: 50.4%; Under 3.5 goals: 71.4%; Double Chance 1X: 62.0%; Double Chance X2: 64.9%; Double Chance 12 (either team wins): 73.1%; Under 4.5 goals: 86.4%; BTTS Yes (both teams score): 55.3%; BTTS No (at least one team does not score): 44.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Celta Vigo win | 35.1% | 2.85 |
| Draw | 26.9% | 3.71 |
| Real Betis win | 38.0% | 2.63 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Celta Vigo expected goals | 1.42 |
| Real Betis expected goals | 1.29 |
| Expected total goals | 2.70 |
| Over 0.5 | 92.9% |
| Under 0.5 | 7.1% |
| Over 1.5 | 75.4% |
| Under 1.5 | 24.6% |
| Over 2.5 | 50.4% |
| Under 2.5 | 49.6% |
| Over 3.5 | 28.6% |
| Under 3.5 | 71.4% |
| Over 4.5 | 13.6% |
| Under 4.5 | 86.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.79% |
| 2 | 0-1 | 9.35% |
| 3 | 1-2 | 8.80% |
| 4 | 1-0 | 8.12% |
| 5 | 2-1 | 7.62% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Celta Vigo win | 35.1% | 30.4% | 3.17 | +11.2% |
| Draw | 26.9% | 27.6% | 3.62 | -2.5% |
| Real Betis win | 38.0% | 42.0% | 2.26 | -14.2% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T15:15:00+00:00 |
| Fixture id | 2013e3955186ebe5258e85eb741a7553 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-24T14:43:14Z |
| Market best draw last update utc | 2026-10-24T14:43:14Z |
| Market best away last update utc | 2026-10-24T14:43:14Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Celta |
| Matched away-team name | Betis |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.4151 |
| Dc lambda away | 1.2877 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-25T10:18:26.012941+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 55.3% |
| P btts no | 44.7% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.99 |
| Fair Over 1.5 odds | 1.33 |
| Fair Under 1.5 odds | 4.06 |
| Fair Over 2.5 odds | 1.98 |
| Fair Under 2.5 odds | 2.02 |
| Fair Over 3.5 odds | 3.50 |
| Fair Under 3.5 odds | 1.40 |
| Fair Over 4.5 odds | 7.33 |
| Fair Under 4.5 odds | 1.16 |
| Goal margin distribution | {"-1": 0.21273355176822098, "-10": 3.0559430628040044e-07, "-11": 3.5292363101130396e-08, "-12": 3.742717041632702e-09, "-13": 3.645627565600765e-10, "-14": 2.967050424468811e-11, "-2": 0.10973369161045361, "-3": 0.0413242088661091, "-4": 0.01224891729095086, "-5": 0.002980871340107571, "-6": 0.0006139359138500756, "-7": 0.00010946362271597235, "-8": 1.7193119892118348e-05, "-9": 2.4119346361402026e-06, "0": 0.2693099029244493, "1": 0.18442634858393164, "10": 6.183101806700978e-07, "11": 7.846978207418693e-08, "12": 9.144695967529261e-09, "13": 9.788477448966981e-10, "14": 8.754439405906092e-11, "2": 0.10440386558150254, "3": 0.04320576565624098, "4": 0.014073283249052961, "5": 0.0037635832478305473, "6": 0.0008518083703468704, "7": 0.00016689727654382037, "8": 2.8806778491278808e-05, "9": 4.4408500030214834e-06} |
| Raw goal margin distribution | {"-1": 0.1900090644803097, "-10": 2.7295030691779293e-07, "-11": 3.152238488196453e-08, "-12": 3.342914917671095e-09, "-13": 3.256196671497067e-10, "-14": 2.650106063351321e-11, "-2": 0.0980117894500731, "-3": 0.036909900679857256, "-4": 0.01094047128910833, "-5": 0.002662450609987026, "-6": 0.0005483544446651927, "-7": 9.777056968215645e-05, "-8": 1.5356527444991522e-05, "-9": 2.1542884984122055e-06, "0": 0.26297212044872786, "1": 0.2090768002179948, "10": 7.009536061919162e-07, "11": 8.89580641586469e-08, "12": 1.0366977313912934e-08, "13": 1.1096806718507704e-09, "14": 9.924559005494729e-11, "2": 0.11835850090713132, "3": 0.048980654357337505, "4": 0.015954320263161455, "5": 0.004266624312915648, "6": 0.0009656611966699477, "7": 0.00018920478994897787, "8": 3.2657096547157234e-05, "9": 5.034414637652805e-06} |
| Unadjusted home-win probability | 39.8% |
| Unadjusted draw probability | 26.3% |
| Unadjusted away-win probability | 33.9% |
| Raw p over 1 5 | 75.5% |
| Raw p under 3 5 | 71.3% |
| Raw p btts yes | 55.1% |
| P home draw | 62.0% |
| P draw away | 64.9% |
| P home away | 73.1% |
| Raw p home draw | 66.1% |
| Raw p draw away | 60.2% |
| Raw p home away | 73.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:43:14Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.31, "price": 1.72, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:18:32Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.01, "price": 1.92, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:18:32Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.92, "price": 2.01, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:43:14Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.72, "price": 2.31, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:18:32Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 4.08, "price": 1.27, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:18:32Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 4.04, "price": 1.28, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:18:32Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.59, "price": 1.33, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:18:32Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.21, "price": 1.39, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:18:32Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.79, "price": 1.5, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:18:32Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.75, "price": 1.51, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:18:32Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.34, "price": 1.67, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:18:32Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.32, "price": 1.68, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:18:32Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.68, "price": 2.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:18:32Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.67, "price": 2.34, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:18:32Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.51, "price": 2.75, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:18:32Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.5, "price": 2.79, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:18:32Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.39, "price": 3.21, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:18:32Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.33, "price": 3.59, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:18:32Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 4.04, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:18:32Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 4.08, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 3.14 |
| Reference draw odds | 3.45 |
| Reference away odds | 2.30 |
| Market reference 1x2 last update utc | 2026-10-24T14:43:20Z |
| Market reference home last update utc | 2026-10-24T14:43:20Z |
| Market reference draw last update utc | 2026-10-24T14:43:20Z |
| Market reference away last update utc | 2026-10-24T14:43:20Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.79 |
| Reference Under 2.5 odds | 2.05 |
| Market reference over 2 5 last update utc | 2026-10-24T14:43:20Z |
| Market reference under 2 5 last update utc | 2026-10-24T14:43:20Z |
| Home probability edge | +4.7% |
| Draw probability edge | -0.6% |
| Away probability edge | -4.1% |
| Over 2.5 probability edge | -3.2% |
| Under 2.5 probability edge | +3.2% |
| Raw edge prob home | 0.0938 |
| Raw ev home | 0.2611 |
| Raw edge prob draw | -0.0127 |
| Raw ev draw | -0.0480 |
| Raw edge prob away | -0.0811 |
| Raw ev away | -0.2334 |
| Count model | {"corners": {"alpha": 0.01460129601713404, "mu": 8.736079430814915, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,477.2163 |
| Elo away rating | 1,549.1815 |
| Elo rating diff | -11.9651 |
| Elo home expectancy | 0.4828 |
| Market p home draw | 58.4% |
| Market home draw odds | 1.67 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-25T10:17:57Z |
| Market reference home draw last update utc | 2026-10-25T10:18:33Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 69.2% |
| Market draw away odds | 1.39 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-25T10:17:57Z |
| Market reference draw away last update utc | 2026-10-25T10:18:33Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 72.3% |
| Market home away odds | 1.35 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-25T10:17:57Z |
| Market reference home away last update utc | 2026-10-25T10:18:33Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.66 |
| Market reference dc draw away odds | 1.40 |
| Market reference dc home away odds | 1.34 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:17:57Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 2.27, "price": 1.62, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:17:57Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 1.62, "price": 2.27, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:17:57Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.81, "price": 2.04, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:17:57Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 2.04, "price": 1.81, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:17:57Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 1.49, "price": 2.57, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:17:57Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 2.57, "price": 1.49, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 78.9% |
| Market reference over 1 5 odds | 1.22 |
| Market reference over 1 5 opposite odds | 3.70 |
| Market reference over 1 5 last update utc | 2026-10-25T10:18:33Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 68.3% |
| Market under 3 5 odds | 1.43 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-25T10:18:32Z |
| Market reference under 3 5 odds | 1.39 |
| Market reference under 3 5 opposite odds | 2.70 |
| Market reference under 3 5 last update utc | 2026-10-25T10:18:33Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 59.1% |
| Market btts yes odds | 1.64 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-25T10:17:57Z |
| Market reference btts yes odds | 1.60 |
| Market reference btts yes opposite odds | 2.22 |
| Market reference btts yes last update utc | 2026-10-25T10:18:33Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-25 — Real Sociedad vs Levante

The model's most likely 1X2 outcome is **Real Sociedad win** at **57.7%**. Expected goals are 1.97 for Real Sociedad and 1.19 for Levante (3.16 combined). The most likely exact score is 2-1 at 10.2%. Goal-market probabilities: at least one goal: 95.6%; Over 2.5 goals: 61.4%; Under 3.5 goals: 60.8%; Double Chance 1X: 79.7%; Double Chance X2: 42.3%; Double Chance 12 (either team wins): 78.0%; Under 4.5 goals: 78.6%; BTTS Yes (both teams score): 60.0%; BTTS No (at least one team does not score): 40.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Sociedad win | 57.7% | 1.73 |
| Draw | 22.0% | 4.55 |
| Levante win | 20.3% | 4.92 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Real Sociedad expected goals | 1.97 |
| Levante expected goals | 1.19 |
| Expected total goals | 3.16 |
| Over 0.5 | 95.6% |
| Under 0.5 | 4.4% |
| Over 1.5 | 82.8% |
| Under 1.5 | 17.2% |
| Over 2.5 | 61.4% |
| Under 2.5 | 38.6% |
| Over 3.5 | 39.2% |
| Under 3.5 | 60.8% |
| Over 4.5 | 21.4% |
| Under 4.5 | 78.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 10.21% |
| 2 | 1-1 | 10.06% |
| 3 | 2-0 | 8.58% |
| 4 | 1-0 | 8.46% |
| 5 | 3-1 | 6.72% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Sociedad win | 57.7% | 60.0% | 1.61 | -7.2% |
| Draw | 22.0% | 21.8% | 4.49 | -1.3% |
| Levante win | 20.3% | 18.2% | 5.14 | +4.6% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T17:30:00+00:00 |
| Fixture id | 3cb8660cd2375b60e81144a7572cfb89 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-24T14:43:14Z |
| Market best draw last update utc | 2026-10-24T14:43:14Z |
| Market best away last update utc | 2026-10-24T14:43:14Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Sociedad |
| Matched away-team name | Levante |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.9732 |
| Dc lambda away | 1.1904 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-25T10:18:26.012941+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 60.0% |
| P btts no | 40.0% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 22.68 |
| Fair Over 1.5 odds | 1.21 |
| Fair Under 1.5 odds | 5.81 |
| Fair Over 2.5 odds | 1.63 |
| Fair Under 2.5 odds | 2.59 |
| Fair Over 3.5 odds | 2.55 |
| Fair Under 3.5 odds | 1.64 |
| Fair Over 4.5 odds | 4.66 |
| Fair Under 4.5 odds | 1.27 |
| Goal margin distribution | {"-1": 0.12259231223873586, "-10": 7.447782906719632e-08, "-11": 7.921057571672689e-09, "-12": 7.742660012227909e-10, "-13": 7.000483515855566e-11, "-14": 5.8846180550403646e-12, "-15": 4.585000036591145e-13, "-16": 2.974586316592595e-14, "-2": 0.055662024830430486, "-3": 0.018774176665233438, "-4": 0.0050366378054703355, "-5": 0.0011161981349971334, "-6": 0.00021016170826889738, "-7": 3.434376686587937e-05, "-8": 4.9528564850502825e-06, "-9": 6.38776428231995e-07, "0": 0.21989963401660018, "1": 0.23550415534367464, "10": 1.3426419227814184e-05, "11": 2.3669543166157623e-06, "12": 3.835044494794675e-07, "13": 5.747536878837706e-08, "14": 8.008395645373044e-09, "15": 1.0342846896808223e-09, "16": 1.1122459675546515e-10, "2": 0.176077596918084, "3": 0.09844179261146796, "4": 0.04377567444256548, "5": 0.016080773283026543, "6": 0.005018717358164376, "7": 0.0013594416986449107, "8": 0.0003249689859709935, "9": 6.947180208782216e-05} |
| Raw goal margin distribution | {"-1": 0.135407444389166, "-10": 8.226333538764639e-08, "-11": 8.749081757679328e-09, "-12": 8.552035489699326e-10, "-13": 7.732275907517874e-11, "-14": 6.49976395328635e-12, "-15": 5.064290950561499e-13, "-16": 3.2855333575926956e-14, "-2": 0.06148062952868743, "-3": 0.02073672676798342, "-4": 0.005563140470215413, "-5": 0.0012328794043592439, "-6": 0.00023213086779646415, "-7": 3.793387706848915e-05, "-8": 5.470601107196163e-06, "-9": 7.055506344842708e-07, "0": 0.2220703165019011, "1": 0.22593306866049923, "10": 1.2880758272972297e-05, "11": 2.2707593050823744e-06, "12": 3.6791850653083916e-07, "13": 5.513952152479796e-08, "14": 7.682927719751204e-09, "15": 9.922504911522647e-10, "16": 1.0670433572102912e-10, "2": 0.1689216554842317, "3": 0.09444103547426769, "4": 0.04199659426415914, "5": 0.015427237149875376, "6": 0.004814752469293304, "7": 0.0013041928461587796, "8": 0.0003117619734257878, "9": 6.664840969863642e-05} |
| Unadjusted home-win probability | 55.3% |
| Unadjusted draw probability | 22.2% |
| Unadjusted away-win probability | 22.5% |
| Raw p over 1 5 | 82.6% |
| Raw p under 3 5 | 61.1% |
| Raw p btts yes | 60.1% |
| P home draw | 79.7% |
| P draw away | 42.3% |
| P home away | 78.0% |
| Raw p home draw | 77.5% |
| Raw p draw away | 44.7% |
| Raw p home away | 77.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:43:14Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.71, "price": 1.55, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:18:32Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.95, "price": 1.97, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:18:32Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.97, "price": 1.95, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:43:14Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.55, "price": 2.71, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:18:32Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 4.18, "price": 1.26, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:18:32Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 3.83, "price": 1.3, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:18:32Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 3.05, "price": 1.42, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:18:32Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.96, "price": 1.44, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:18:32Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.5, "price": 1.59, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:18:32Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.52, "price": 1.59, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:18:32Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.24, "price": 1.72, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:18:32Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.22, "price": 1.73, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:18:32Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.73, "price": 2.22, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:18:32Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.72, "price": 2.24, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:18:32Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.59, "price": 2.5, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:18:32Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.59, "price": 2.52, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:18:32Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.44, "price": 2.96, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:18:32Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.42, "price": 3.05, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:18:32Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.83, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:18:32Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.26, "price": 4.18, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.63 |
| Reference draw odds | 4.30 |
| Reference away odds | 5.10 |
| Market reference 1x2 last update utc | 2026-10-24T14:43:20Z |
| Market reference home last update utc | 2026-10-24T14:43:20Z |
| Market reference draw last update utc | 2026-10-24T14:43:20Z |
| Market reference away last update utc | 2026-10-24T14:43:20Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.59 |
| Reference Under 2.5 odds | 2.39 |
| Market reference over 2 5 last update utc | 2026-10-24T14:43:20Z |
| Market reference under 2 5 last update utc | 2026-10-24T14:43:20Z |
| Home probability edge | -2.3% |
| Draw probability edge | +0.2% |
| Away probability edge | +2.1% |
| Over 2.5 probability edge | +0.7% |
| Under 2.5 probability edge | -0.7% |
| Raw edge prob home | -0.0469 |
| Raw ev home | -0.1093 |
| Raw edge prob draw | 0.0043 |
| Raw ev draw | -0.0029 |
| Raw edge prob away | 0.0425 |
| Raw ev away | 0.1549 |
| Count model | {"corners": {"alpha": 0.01460129601713404, "mu": 10.488199856444206, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,485.8012 |
| Elo away rating | 1,453.6938 |
| Elo rating diff | 92.1074 |
| Elo home expectancy | 0.6295 |
| Market p home draw | 81.7% |
| Market home draw odds | 1.19 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-25T10:18:28Z |
| Market reference home draw last update utc | 2026-10-25T10:18:33Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 39.9% |
| Market draw away odds | 2.50 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-25T10:18:28Z |
| Market reference draw away last update utc | 2026-10-25T10:18:33Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 78.4% |
| Market home away odds | 1.22 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-25T10:18:28Z |
| Market reference home away last update utc | 2026-10-25T10:18:33Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.19 |
| Market reference dc draw away odds | 2.44 |
| Market reference dc home away odds | 1.24 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:18:28Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 2.21, "price": 1.67, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:18:28Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.67, "price": 2.21, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:18:28Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 1.76, "price": 2.08, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:18:28Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 2.08, "price": 1.76, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 86.0% |
| Market reference over 1 5 odds | 1.13 |
| Market reference over 1 5 opposite odds | 4.90 |
| Market reference over 1 5 last update utc | 2026-10-25T10:18:33Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 56.9% |
| Market under 3 5 odds | 1.72 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-25T10:18:32Z |
| Market reference under 3 5 odds | 1.64 |
| Market reference under 3 5 opposite odds | 2.09 |
| Market reference under 3 5 last update utc | 2026-10-25T10:18:33Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 61.1% |
| Market btts yes odds | 1.58 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-25T10:18:28Z |
| Market reference btts yes odds | 1.55 |
| Market reference btts yes opposite odds | 2.32 |
| Market reference btts yes last update utc | 2026-10-25T10:18:33Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-26 — Sevilla vs CA Osasuna

The model's most likely 1X2 outcome is **Sevilla win** at **48.3%**. Expected goals are 1.51 for Sevilla and 1.06 for CA Osasuna (2.57 combined). The most likely exact score is 1-1 at 12.7%. Goal-market probabilities: at least one goal: 92.0%; Over 2.5 goals: 47.4%; Under 3.5 goals: 74.2%; Double Chance 1X: 75.0%; Double Chance X2: 51.7%; Double Chance 12 (either team wins): 73.3%; Under 4.5 goals: 88.2%; BTTS Yes (both teams score): 51.3%; BTTS No (at least one team does not score): 48.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Sevilla win | 48.3% | 2.07 |
| Draw | 26.7% | 3.74 |
| CA Osasuna win | 25.0% | 4.00 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Sevilla expected goals | 1.51 |
| CA Osasuna expected goals | 1.06 |
| Expected total goals | 2.57 |
| Over 0.5 | 92.0% |
| Under 0.5 | 8.0% |
| Over 1.5 | 73.0% |
| Under 1.5 | 27.0% |
| Over 2.5 | 47.4% |
| Under 2.5 | 52.6% |
| Over 3.5 | 25.8% |
| Under 3.5 | 74.2% |
| Over 4.5 | 11.8% |
| Under 4.5 | 88.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.71% |
| 2 | 1-0 | 11.50% |
| 3 | 2-1 | 9.45% |
| 4 | 2-0 | 8.90% |
| 5 | 0-0 | 8.03% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Sevilla win | 48.3% | 49.3% | 1.93 | -6.8% |
| Draw | 26.7% | 27.1% | 3.46 | -7.6% |
| CA Osasuna win | 25.0% | 23.6% | 4.38 | +9.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-26T20:00:00+00:00 |
| Fixture id | 85e464708d03287f24590e1478aeca31 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-24T14:43:14Z |
| Market best draw last update utc | 2026-10-24T14:43:14Z |
| Market best away last update utc | 2026-10-24T14:43:14Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Sevilla |
| Matched away-team name | Osasuna |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 95/100 |
| Dc lambda home | 1.5100 |
| Dc lambda away | 1.0618 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-25T10:18:26.012941+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 51.3% |
| P btts no | 48.7% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 12.45 |
| Fair Over 1.5 odds | 1.37 |
| Fair Under 1.5 odds | 3.71 |
| Fair Over 2.5 odds | 2.11 |
| Fair Under 2.5 odds | 1.90 |
| Fair Over 3.5 odds | 3.87 |
| Fair Under 3.5 odds | 1.35 |
| Fair Over 4.5 odds | 8.44 |
| Fair Under 4.5 odds | 1.13 |
| Goal margin distribution | {"-1": 0.15458944469924665, "-10": 4.1975132286559206e-08, "-11": 4.003631903857716e-09, "-12": 3.506821061951292e-10, "-13": 2.8389424813083266e-11, "-14": 2.1267200215165757e-12, "-15": 1.3600667838868302e-13, "-2": 0.0674408569609546, "-3": 0.021233623421496595, "-4": 0.005237223619392324, "-5": 0.0010576805504507352, "-6": 0.0001804736563709132, "-7": 2.6629356893056502e-05, "-8": 3.4587133933869507e-06, "-9": 4.0101149525877395e-07, "0": 0.26710373745676436, "1": 0.23835065225388494, "10": 1.5320406322879718e-06, "11": 2.0781153582365784e-07, "12": 2.5886087651612933e-08, "13": 2.980208884955371e-09, "14": 3.1749561515322233e-10, "15": 2.887519639673488e-11, "2": 0.14713055949117607, "3": 0.06587812313592872, "4": 0.023107636390528218, "5": 0.0066366089132161065, "6": 0.0016104336086066775, "7": 0.0003379301856674934, "8": 6.241919808020817e-05, "9": 1.0291951520012061e-05} |
| Raw goal margin distribution | {"-1": 0.1632579051429626, "-10": 4.432884909143983e-08, "-11": 4.228131867987279e-09, "-12": 3.7034628166186654e-10, "-13": 2.9981335609391716e-11, "-14": 2.2459738840117872e-12, "-15": 1.4363312736123204e-13, "-2": 0.07122254077509658, "-3": 0.02242427925873113, "-4": 0.0055308961005110695, "-5": 0.001116989011203066, "-6": 0.00019059355009604846, "-7": 2.8122573505084215e-05, "-8": 3.652657554937272e-06, "-9": 4.2349784476917486e-07, "0": 0.2632367162098057, "1": 0.23334877307993207, "10": 1.499890176395247e-06, "11": 2.0345053163376242e-07, "12": 2.5342858247810833e-08, "13": 2.9176680669851767e-09, "14": 3.108328488035643e-10, "15": 2.826923940800895e-11, "2": 0.1440429686899265, "3": 0.0644956456431392, "4": 0.02262271384415338, "5": 0.00649733714871795, "6": 0.0015766380462629117, "7": 0.00033083859207646855, "8": 6.110930744647217e-05, "9": 1.0075970999377924e-05} |
| Unadjusted home-win probability | 47.3% |
| Unadjusted draw probability | 26.3% |
| Unadjusted away-win probability | 26.4% |
| Raw p over 1 5 | 73.0% |
| Raw p under 3 5 | 74.2% |
| Raw p btts yes | 51.2% |
| P home draw | 75.0% |
| P draw away | 51.7% |
| P home away | 73.3% |
| Raw p home draw | 73.6% |
| Raw p draw away | 52.7% |
| Raw p home away | 73.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:43:14Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.96, "price": 1.48, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:18:32Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.96, "price": 1.94, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:18:32Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.94, "price": 1.96, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:43:14Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.48, "price": 2.96, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:18:32Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 4.34, "price": 1.24, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:18:32Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.78, "price": 1.3, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:18:32Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.76, "price": 1.3, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:18:32Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.33, "price": 1.36, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:18:32Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 3.19, "price": 1.39, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:18:32Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.88, "price": 1.46, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:18:32Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.34, "price": 1.66, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:18:32Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.25, "price": 1.71, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:18:32Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.71, "price": 2.25, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:18:32Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.66, "price": 2.34, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:18:32Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.46, "price": 2.88, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:18:32Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.39, "price": 3.19, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:18:32Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.36, "price": 3.33, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:18:32Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.76, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:18:32Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.78, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:18:32Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.24, "price": 4.34, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.97 |
| Reference draw odds | 3.50 |
| Reference away odds | 4.00 |
| Market reference 1x2 last update utc | 2026-10-24T14:43:20Z |
| Market reference home last update utc | 2026-10-24T14:43:20Z |
| Market reference draw last update utc | 2026-10-24T14:43:20Z |
| Market reference away last update utc | 2026-10-24T14:43:20Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 2.12 |
| Reference Under 2.5 odds | 1.74 |
| Market reference over 2 5 last update utc | 2026-10-24T14:43:20Z |
| Market reference under 2 5 last update utc | 2026-10-24T14:43:20Z |
| Home probability edge | -1.0% |
| Draw probability edge | -0.4% |
| Away probability edge | +1.4% |
| Over 2.5 probability edge | +2.6% |
| Under 2.5 probability edge | -2.6% |
| Raw edge prob home | -0.0203 |
| Raw ev home | -0.0871 |
| Raw edge prob draw | -0.0077 |
| Raw ev draw | -0.0892 |
| Raw edge prob away | 0.0280 |
| Raw ev away | 0.1553 |
| Count model | {"corners": {"alpha": 0.01460129601713404, "mu": 8.559671036495459, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,440.7731 |
| Elo away rating | 1,423.7802 |
| Elo rating diff | 76.9929 |
| Elo home expectancy | 0.6090 |
| Market p home draw | 75.9% |
| Market home draw odds | 1.24 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-25T10:18:14Z |
| Market reference home draw last update utc | 2026-10-25T10:18:33Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 51.7% |
| Market draw away odds | 1.94 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-25T10:18:14Z |
| Market reference draw away last update utc | 2026-10-25T10:18:33Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 72.5% |
| Market home away odds | 1.34 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-25T10:18:14Z |
| Market reference home away last update utc | 2026-10-25T10:18:33Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.28 |
| Market reference dc draw away odds | 1.88 |
| Market reference dc home away odds | 1.34 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:18:14Z", "line": 7.5, "market_key": "alternate_totals_corners", "opposite_price": 2.68, "price": 1.44, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:18:14Z", "line": 7.5, "market_key": "alternate_totals_corners", "opposite_price": 1.44, "price": 2.68, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:18:14Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 2.03, "price": 1.8, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:18:14Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 1.8, "price": 2.03, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:18:14Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.61, "price": 2.26, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:18:14Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 2.26, "price": 1.61, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 70.5% |
| Market over 1 5 odds | 1.40 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-25T10:18:32Z |
| Market reference over 1 5 odds | 1.35 |
| Market reference over 1 5 opposite odds | 2.85 |
| Market reference over 1 5 last update utc | 2026-10-25T10:18:33Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 78.3% |
| Market reference under 3 5 odds | 1.23 |
| Market reference under 3 5 opposite odds | 3.65 |
| Market reference under 3 5 last update utc | 2026-10-25T10:18:33Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 49.7% |
| Market btts yes odds | 2.01 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-25T10:18:14Z |
| Market reference btts yes odds | 1.87 |
| Market reference btts yes opposite odds | 1.85 |
| Market reference btts yes last update utc | 2026-10-25T10:18:33Z |
| Market btts yes bookmakers | 1 |

</details>


---
