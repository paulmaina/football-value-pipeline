# Serie A — football model report

Fixtures in this report: **20**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Serie A |
| Training matches | 1,970 |
| Training data through | 2026-10-19 |
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
| Training sha256 | 0a097825d3c8eb610030fff3e667acc826dc106a3537e6b709e28146c8d890ff |
| Training as of utc | 2026-10-21T17:22:27.690536+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 70, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 70, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 918, 'added_results': 0, 'conflicts': 0, 'unmapped': 223, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 31, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_RETROSPECTIVE_EXAMPLES', 'cutoff_utc': '2026-10-21T17:22:27.690536+00:00', 'observations': 151, 'observations_sha256': '1bd6eb4913bd5562b3afca50fbaef785c7460861a0f953a7bcb52f2c27e09e19', 'eligible_training_matches': 43, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 71, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 7, 'retrospective_eligible_training_matches': 43, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:28.568690+00:00', 'retrospective_inputs_sha256': '09611ef1eaa884ab1a5a0c18abdc6e1a537307c3ae873552ab8d45a508384b54', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'input_providers': ['api-football', 'bigballsdata']} |
| Optimizer objective | 2441.186 |
| Base scoring parameter | 0.132 |
| Home-advantage parameter | 0.126 |
| Dixon-Coles low-score adjustment | -0.034 |
| Xi per day | 0.0009 |
| Training data health | {'training_end': '2026-10-19', 'days_since_latest_result': 2, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 20.00 |
| Additional event odds calls used before this league | 1.00 |
| Bbs statistics model artifact | bbs/feature_models/SerieA/20261021T172227690536Z_9aaaa6eef4b2e8811704a32c8dbff6601e21a5ce0154a78aa7c2645a646688eb.json |
| Over 1 5 in window quote fixtures | 0 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 0.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 0.00 |
| Bbs statistics applied fixtures | 0 |
| Decay tuning | {'selected_half_life_days': 730.0, 'selected_xi_per_day': 0.0009495166856985552, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365} |
| Goal market reliability | {'home_draw': 'RELIABLE_FOR_RANKING', 'draw_away': 'RELIABLE_FOR_RANKING', 'home_away': 'RELIABLE_FOR_RANKING', 'home': 'RELIABLE_FOR_RANKING', 'draw': 'RELIABLE_FOR_RANKING', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'RELIABLE_FOR_RANKING', 'under_3_5': 'RELIABLE_FOR_RANKING', 'btts_yes': 'RELIABLE_FOR_RANKING'} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-23 — Torino vs Monza

The model's most likely 1X2 outcome is **Torino win** at **47.1%**. Expected goals are 1.51 for Torino and 1.00 for Monza (2.51 combined). The most likely exact score is 1-1 at 12.7%. Goal-market probabilities: at least one goal: 91.5%; Over 2.5 goals: 45.8%; Under 3.5 goals: 75.7%; Double Chance 1X: 73.8%; Double Chance X2: 52.9%; Double Chance 12 (either team wins): 73.3%; Under 4.5 goals: 89.0%; BTTS Yes (both teams score): 49.7%; BTTS No (at least one team does not score): 50.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Torino win | 47.1% | 2.12 |
| Draw | 26.7% | 3.75 |
| Monza win | 26.2% | 3.81 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Torino expected goals | 1.51 |
| Monza expected goals | 1.00 |
| Expected total goals | 2.51 |
| Over 0.5 | 91.5% |
| Under 0.5 | 8.5% |
| Over 1.5 | 71.8% |
| Under 1.5 | 28.2% |
| Over 2.5 | 45.8% |
| Under 2.5 | 54.2% |
| Over 3.5 | 24.3% |
| Under 3.5 | 75.7% |
| Over 4.5 | 11.0% |
| Under 4.5 | 89.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.67% |
| 2 | 1-0 | 11.46% |
| 3 | 2-0 | 8.98% |
| 4 | 2-1 | 8.94% |
| 5 | 0-0 | 8.54% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Torino win | 47.1% | 45.3% | 2.19 | +3.1% |
| Draw | 26.7% | 26.7% | 3.45 | -7.9% |
| Monza win | 26.2% | 28.0% | 3.49 | -8.4% |
| Over 2.5 | 45.8% | 48.5% | 1.98 | -9.3% |
| Under 2.5 | 54.2% | 51.5% | 1.91 | +3.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-23T18:45:00+00:00 |
| Fixture id | 124c70f8f3248a845bdb983a54e74720 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T17:24:01Z |
| Market best draw last update utc | 2026-10-21T17:24:01Z |
| Market best away last update utc | 2026-10-21T17:24:01Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 17.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Torino |
| Matched away-team name | Monza |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.5140 |
| Dc lambda away | 0.9959 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T17:22:27.690536+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 49.7% |
| P btts no | 50.3% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 11.71 |
| Fair Over 1.5 odds | 1.39 |
| Fair Under 1.5 odds | 3.54 |
| Fair Over 2.5 odds | 2.18 |
| Fair Under 2.5 odds | 1.84 |
| Fair Over 3.5 odds | 4.11 |
| Fair Under 3.5 odds | 1.32 |
| Fair Over 4.5 odds | 9.12 |
| Fair Under 4.5 odds | 1.12 |
| Goal margin distribution | {"-1": 0.16638617376868747, "-10": 2.6401499192839124e-08, "-11": 2.3635637514166316e-09, "-12": 1.9429348221105711e-10, "-13": 1.476076031718083e-11, "-14": 1.0381425030995408e-12, "-15": 6.263042380072228e-14, "-2": 0.06943370522697777, "-3": 0.02063132945012628, "-4": 0.004792158143884376, "-5": 0.0009103006166975834, "-6": 0.00014598908121275735, "-7": 2.023629996838432e-05, "-8": 2.468326836440506e-06, "-9": 2.686939274469977e-07, "0": 0.2668402951389944, "1": 0.22958799949074032, "10": 1.5657139510845347e-06, "11": 2.1308846415136545e-07, "12": 2.6629292992141245e-08, "13": 3.075522567734067e-09, "14": 3.2883341876298554e-10, "15": 3.0158734348401063e-11, "2": 0.1443390650694835, "3": 0.06520029285566666, "4": 0.023023018349821157, "5": 0.006648516344809521, "6": 0.0016209479328035713, "7": 0.0003415769716004044, "8": 6.333866801693873e-05, "9": 1.0481728304435313e-05} |
| Raw goal margin distribution | {"-1": 0.15525940301960953, "-10": 2.4635947270483596e-08, "-11": 2.205504752780095e-09, "-12": 1.8130046130291402e-10, "-13": 1.377366149513756e-11, "-14": 9.68718623847884e-13, "-15": 5.84421288735426e-14, "-2": 0.0647904533099424, "-3": 0.019251647065222147, "-4": 0.00447169134154985, "-5": 0.0008494259295446751, "-6": 0.0001362263286851277, "-7": 1.8883034456847208e-05, "-8": 2.303261998294448e-06, "-9": 2.5072551297688405e-07, "0": 0.26677507087611135, "1": 0.23817374527190724, "10": 1.624265887509158e-06, "11": 2.2105718806620887e-07, "12": 2.7625130494405623e-08, "13": 3.19053578693271e-09, "14": 3.4113057777875917e-10, "15": 3.128655996111372e-11, "2": 0.14973681461095234, "3": 0.06763854372486751, "4": 0.023883994459657762, "5": 0.006897146374624167, "6": 0.0016815654167593075, "7": 0.0003543506925673848, "8": 6.570730097213419e-05, "9": 1.0873706346705651e-05} |
| Unadjusted home-win probability | 48.8% |
| Unadjusted draw probability | 26.7% |
| Unadjusted away-win probability | 24.5% |
| Raw p over 1 5 | 71.9% |
| Raw p under 3 5 | 75.5% |
| Raw p btts yes | 49.6% |
| P home draw | 73.8% |
| P draw away | 52.9% |
| P home away | 73.3% |
| Raw p home draw | 75.5% |
| Raw p draw away | 51.2% |
| Raw p home away | 73.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:23:35Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.61, "price": 2.55, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:24:01Z", "line": 0.25, "market_key": "spreads", "opposite_price": 1.89, "price": 2.02, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:24:01Z", "line": -0.25, "market_key": "spreads", "opposite_price": 2.02, "price": 1.89, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:23:35Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.55, "price": 1.61, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 2.10 |
| Reference draw odds | 3.45 |
| Reference away odds | 3.30 |
| Market reference 1x2 last update utc | 2026-10-21T17:24:07Z |
| Market reference home last update utc | 2026-10-21T17:24:07Z |
| Market reference draw last update utc | 2026-10-21T17:24:07Z |
| Market reference away last update utc | 2026-10-21T17:24:07Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.92 |
| Reference Under 2.5 odds | 1.82 |
| Market reference over 2 5 last update utc | 2026-10-21T17:24:04Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:24:04Z |
| Market best over 2 5 last update utc | 2026-10-21T17:24:01Z |
| Market best under 2 5 last update utc | 2026-10-21T17:24:01Z |
| Home probability edge | +1.8% |
| Draw probability edge | -0.0% |
| Away probability edge | -1.8% |
| Over 2.5 probability edge | -2.7% |
| Under 2.5 probability edge | +2.7% |
| Raw edge prob home | 0.0352 |
| Raw ev home | 0.0697 |
| Raw edge prob draw | -0.0001 |
| Raw ev draw | -0.0796 |
| Raw edge prob away | -0.0351 |
| Raw ev away | -0.1457 |

</details>


---

## 2026-10-24 — Cagliari vs Bologna

The model's most likely 1X2 outcome is **Bologna win** at **42.4%**. Expected goals are 1.04 for Cagliari and 1.43 for Bologna (2.47 combined). The most likely exact score is 1-1 at 13.8%. Goal-market probabilities: at least one goal: 90.5%; Over 2.5 goals: 44.1%; Under 3.5 goals: 76.6%; Double Chance 1X: 57.6%; Double Chance X2: 71.5%; Double Chance 12 (either team wins): 70.8%; Under 4.5 goals: 89.8%; BTTS Yes (both teams score): 50.0%; BTTS No (at least one team does not score): 50.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Cagliari win | 28.5% | 3.51 |
| Draw | 29.2% | 3.43 |
| Bologna win | 42.4% | 2.36 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Cagliari expected goals | 1.04 |
| Bologna expected goals | 1.43 |
| Expected total goals | 2.47 |
| Over 0.5 | 90.5% |
| Under 0.5 | 9.5% |
| Over 1.5 | 70.8% |
| Under 1.5 | 29.2% |
| Over 2.5 | 44.1% |
| Under 2.5 | 55.9% |
| Over 3.5 | 23.4% |
| Under 3.5 | 76.6% |
| Over 4.5 | 10.2% |
| Under 4.5 | 89.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.84% |
| 2 | 0-1 | 10.88% |
| 3 | 0-0 | 9.47% |
| 4 | 1-0 | 8.83% |
| 5 | 1-2 | 8.37% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Cagliari win | 28.5% | 29.8% | 3.30 | -6.1% |
| Draw | 29.2% | 30.9% | 2.97 | -13.3% |
| Bologna win | 42.4% | 39.2% | 2.54 | +7.6% |
| Over 2.5 | 44.1% | 43.3% | 2.24 | -1.2% |
| Under 2.5 | 55.9% | 56.7% | 1.76 | -1.6% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T13:00:00+00:00 |
| Fixture id | b7f0880e3da978f9481f7cb5697e2aa5 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T17:24:01Z |
| Market best draw last update utc | 2026-10-21T17:24:01Z |
| Market best away last update utc | 2026-10-21T17:24:01Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 16.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Cagliari |
| Matched away-team name | Bologna |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.0400 |
| Dc lambda away | 1.4266 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T17:22:27.690536+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 50.0% |
| P btts no | 50.0% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 10.55 |
| Fair Over 1.5 odds | 1.41 |
| Fair Under 1.5 odds | 3.43 |
| Fair Over 2.5 odds | 2.27 |
| Fair Under 2.5 odds | 1.79 |
| Fair Over 3.5 odds | 4.28 |
| Fair Under 3.5 odds | 1.30 |
| Fair Over 4.5 odds | 9.78 |
| Fair Under 4.5 odds | 1.11 |
| Goal margin distribution | {"-1": 0.21591600789270501, "-10": 8.698701501215669e-07, "-11": 1.1157329021505032e-07, "-12": 1.3138147704321948e-08, "-13": 1.4235095980565092e-09, "-14": 1.311586751735628e-10, "-2": 0.12837158954584058, "-3": 0.054727104412211715, "-4": 0.01822824947158362, "-5": 0.004963668693139962, "-6": 0.0011409324572258653, "-7": 0.00022664090321353523, "-8": 3.961323830872893e-05, "-9": 6.178733464070028e-06, "0": 0.2917809821159128, "1": 0.17647073434856297, "10": 4.160994251266003e-08, "11": 3.890572630405934e-09, "12": 3.3396274831425487e-10, "13": 2.6377576143660955e-11, "14": 1.771667042274464e-12, "2": 0.07700639839055538, "3": 0.023931557426845503, "4": 0.0058106411494150785, "5": 0.0011534332779573986, "6": 0.0001932681214687079, "7": 2.7986538216622453e-05, "8": 3.565839862090715e-06, "9": 4.054446270164072e-07} |
| Raw goal margin distribution | {"-1": 0.23184044635465215, "-10": 9.340256234034699e-07, "-11": 1.1980214740524744e-07, "-12": 1.4107124607254563e-08, "-13": 1.5284976034178657e-09, "-14": 1.4083201191193845e-10, "-2": 0.13783937054983597, "-3": 0.0587633887753697, "-4": 0.019572636299648262, "-5": 0.005329753808462585, "-6": 0.0012250795701780463, "-7": 0.00024335633414155396, "-8": 4.253483074591067e-05, "-9": 6.634433167772641e-06, "0": 0.2744286786937336, "1": 0.16785734941363373, "10": 3.9578996966335584e-08, "11": 3.7006771227644468e-09, "12": 3.176623134813842e-10, "13": 2.509010931345558e-11, "14": 1.6851934960064687e-12, "2": 0.07324778224245085, "3": 0.02276347866879695, "4": 0.005527028746920084, "5": 0.001097135190591927, "6": 0.00018383487049932864, "7": 2.6620539329919e-05, "8": 3.391794281887957e-06, "9": 3.856552230952262e-07} |
| Unadjusted home-win probability | 27.1% |
| Unadjusted draw probability | 27.4% |
| Unadjusted away-win probability | 45.5% |
| Raw p over 1 5 | 71.0% |
| Raw p under 3 5 | 76.5% |
| Raw p btts yes | 49.6% |
| P home draw | 57.6% |
| P draw away | 71.5% |
| P home away | 70.8% |
| Raw p home draw | 54.5% |
| Raw p draw away | 72.9% |
| Raw p home away | 72.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:24:01Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.79, "price": 2.14, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:23:35Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.3, "price": 1.72, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:23:35Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.72, "price": 2.3, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:24:01Z", "line": 0.25, "market_key": "spreads", "opposite_price": 2.14, "price": 1.79, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 3.10 |
| Reference draw odds | 3.00 |
| Reference away odds | 2.40 |
| Market reference 1x2 last update utc | 2026-10-21T17:24:06Z |
| Market reference home last update utc | 2026-10-21T17:24:06Z |
| Market reference draw last update utc | 2026-10-21T17:24:06Z |
| Market reference away last update utc | 2026-10-21T17:24:06Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 2.15 |
| Reference Under 2.5 odds | 1.68 |
| Market reference over 2 5 last update utc | 2026-10-21T17:24:04Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:24:04Z |
| Market best over 2 5 last update utc | 2026-10-21T17:23:35Z |
| Market best under 2 5 last update utc | 2026-10-21T17:23:35Z |
| Home probability edge | -1.4% |
| Draw probability edge | -1.7% |
| Away probability edge | +3.1% |
| Over 2.5 probability edge | +0.8% |
| Under 2.5 probability edge | -0.8% |
| Raw edge prob home | -0.0278 |
| Raw ev home | -0.1067 |
| Raw edge prob draw | -0.0347 |
| Raw ev draw | -0.1849 |
| Raw edge prob away | 0.0625 |
| Raw ev away | 0.1554 |

</details>


---

## 2026-10-24 — Como vs Sassuolo

The model's most likely 1X2 outcome is **Como win** at **64.0%**. Expected goals are 2.12 for Como and 0.96 for Sassuolo (3.08 combined). The most likely exact score is 2-0 at 10.4%. Goal-market probabilities: at least one goal: 95.3%; Over 2.5 goals: 59.8%; Under 3.5 goals: 62.9%; Double Chance 1X: 83.7%; Double Chance X2: 36.0%; Double Chance 12 (either team wins): 80.3%; Under 4.5 goals: 80.0%; BTTS Yes (both teams score): 54.4%; BTTS No (at least one team does not score): 45.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Como win | 64.0% | 1.56 |
| Draw | 19.7% | 5.08 |
| Sassuolo win | 16.3% | 6.13 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Como expected goals | 2.12 |
| Sassuolo expected goals | 0.96 |
| Expected total goals | 3.08 |
| Over 0.5 | 95.3% |
| Under 0.5 | 4.7% |
| Over 1.5 | 81.6% |
| Under 1.5 | 18.4% |
| Over 2.5 | 59.8% |
| Under 2.5 | 40.2% |
| Over 3.5 | 37.1% |
| Under 3.5 | 62.9% |
| Over 4.5 | 20.0% |
| Under 4.5 | 80.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 10.38% |
| 2 | 2-1 | 9.99% |
| 3 | 1-0 | 9.49% |
| 4 | 1-1 | 9.25% |
| 5 | 3-0 | 7.32% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Como win | 64.0% | 64.5% | 1.56 | -0.1% |
| Draw | 19.7% | 18.7% | 4.58 | -9.9% |
| Sassuolo win | 16.3% | 16.8% | 5.66 | -7.6% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T13:00:00+00:00 |
| Fixture id | 08ffd99b2249c81d8a7410598f32b9b0 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T17:24:01Z |
| Market best draw last update utc | 2026-10-21T17:24:01Z |
| Market best away last update utc | 2026-10-21T17:24:01Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 7.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Como |
| Matched away-team name | Sassuolo |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.1168 |
| Dc lambda away | 0.9623 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T17:22:27.690536+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 54.4% |
| P btts no | 45.6% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 21.31 |
| Fair Over 1.5 odds | 1.23 |
| Fair Under 1.5 odds | 5.43 |
| Fair Over 2.5 odds | 1.67 |
| Fair Under 2.5 odds | 2.49 |
| Fair Over 3.5 odds | 2.70 |
| Fair Under 3.5 odds | 1.59 |
| Fair Over 4.5 odds | 5.01 |
| Fair Under 4.5 odds | 1.25 |
| Goal margin distribution | {"-1": 0.10750552353799796, "-10": 1.0684224255339775e-08, "-11": 9.206608975448963e-10, "-12": 7.288894505391399e-11, "-13": 5.3363742160417214e-12, "-14": 3.6330644633950947e-13, "-15": 2.310707896033278e-14, "-16": 1.3712533871884843e-15, "-17": 6.931615851778777e-17, "-2": 0.041182415858483284, "-3": 0.01143798531932563, "-4": 0.00251150862534796, "-5": 0.0004539281381359764, "-6": 6.954573300896986e-05, "-7": 9.233834369321069e-06, "-8": 1.0808155524707104e-06, "-9": 1.1305175189478027e-07, "0": 0.19666683681465869, "1": 0.2351031915323003, "10": 2.7719009156017765e-05, "11": 5.254131791178542e-06, "12": 9.150176802782765e-07, "13": 1.4736035373703484e-07, "14": 2.2068562204837815e-08, "15": 3.087539631674489e-09, "16": 4.0304335284680036e-10, "17": 4.481620654144626e-11, "2": 0.194901001028987, "3": 0.11907438354937276, "4": 0.05751353187082751, "5": 0.02286593822971532, "6": 0.007706176776749315, "7": 0.002250697433572931, "8": 0.0005794996500360804, "9": 0.0001333353933658212} |
| Raw goal margin distribution | {"-1": 0.10438885071605986, "-10": 1.0374479878825579e-08, "-11": 8.939701871221421e-10, "-12": 7.077583507971828e-11, "-13": 5.1816683745232616e-12, "-14": 3.5277389610323216e-13, "-15": 2.243718589233063e-14, "-16": 1.3314996329329615e-15, "-17": 6.730662653967332e-17, "-2": 0.03998850402936205, "-3": 0.011106388794707347, "-4": 0.0024386979416074314, "-5": 0.00044076839113245327, "-6": 6.75295454790872e-05, "-7": 8.966137978716831e-06, "-8": 1.0494818279600541e-06, "-9": 1.0977428938860108e-07, "0": 0.20601754511831483, "1": 0.23340638200823885, "10": 2.7518952838504885e-05, "11": 5.216211162343859e-06, "12": 9.084137260551901e-07, "13": 1.4629681031994894e-07, "14": 2.1909286840316164e-08, "15": 3.0652559416114276e-09, "16": 4.001344693252164e-10, "17": 4.44927546750713e-11, "2": 0.19349434264787496, "3": 0.11821498837586843, "4": 0.057098439638328294, "5": 0.02270090796571973, "6": 0.0076505590113601415, "7": 0.002234453482071564, "8": 0.0005753172290363365, "9": 0.00013237307225106714} |
| Unadjusted home-win probability | 63.6% |
| Unadjusted draw probability | 20.6% |
| Unadjusted away-win probability | 15.8% |
| Raw p over 1 5 | 81.6% |
| Raw p under 3 5 | 63.0% |
| Raw p btts yes | 54.7% |
| P home draw | 83.7% |
| P draw away | 36.0% |
| P home away | 80.3% |
| Raw p home draw | 84.2% |
| Raw p draw away | 36.4% |
| Raw p home away | 79.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:24:01Z", "line": 1.25, "market_key": "spreads", "opposite_price": 2.12, "price": 1.81, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:23:35Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.34, "price": 1.7, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:23:35Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.7, "price": 2.34, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:24:01Z", "line": -1.25, "market_key": "spreads", "opposite_price": 1.81, "price": 2.12, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 1.50 |
| Reference draw odds | 4.70 |
| Reference away odds | 5.20 |
| Market reference 1x2 last update utc | 2026-10-21T17:24:06Z |
| Market reference home last update utc | 2026-10-21T17:24:06Z |
| Market reference draw last update utc | 2026-10-21T17:24:06Z |
| Market reference away last update utc | 2026-10-21T17:24:06Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.46 |
| Reference Under 2.5 odds | 2.68 |
| Market reference over 2 5 last update utc | 2026-10-21T17:24:04Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:24:04Z |
| Home probability edge | -0.5% |
| Draw probability edge | +0.9% |
| Away probability edge | -0.5% |
| Over 2.5 probability edge | -6.3% |
| Under 2.5 probability edge | +6.3% |
| Raw edge prob home | -0.0092 |
| Raw ev home | -0.0086 |
| Raw edge prob draw | 0.0187 |
| Raw ev draw | -0.0564 |
| Raw edge prob away | -0.0095 |
| Raw ev away | -0.1032 |

</details>


---

## 2026-10-24 — Lazio vs Parma

The model's most likely 1X2 outcome is **Lazio win** at **63.8%**. Expected goals are 1.60 for Lazio and 0.71 for Parma (2.31 combined). The most likely exact score is 1-0 at 16.9%. Goal-market probabilities: at least one goal: 91.0%; Over 2.5 goals: 42.0%; Under 3.5 goals: 79.2%; Double Chance 1X: 86.2%; Double Chance X2: 36.2%; Double Chance 12 (either team wins): 77.6%; Under 4.5 goals: 91.1%; BTTS Yes (both teams score): 39.9%; BTTS No (at least one team does not score): 60.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lazio win | 63.8% | 1.57 |
| Draw | 22.4% | 4.47 |
| Parma win | 13.8% | 7.22 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lazio expected goals | 1.60 |
| Parma expected goals | 0.71 |
| Expected total goals | 2.31 |
| Over 0.5 | 91.0% |
| Under 0.5 | 9.0% |
| Over 1.5 | 68.3% |
| Under 1.5 | 31.7% |
| Over 2.5 | 42.0% |
| Under 2.5 | 58.0% |
| Over 3.5 | 20.8% |
| Under 3.5 | 79.2% |
| Over 4.5 | 8.9% |
| Under 4.5 | 91.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 16.93% |
| 2 | 2-0 | 13.90% |
| 3 | 1-1 | 10.19% |
| 4 | 2-1 | 9.82% |
| 5 | 0-0 | 9.03% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lazio win | 63.8% | 69.0% | 1.43 | -8.8% |
| Draw | 22.4% | 19.2% | 4.67 | +4.6% |
| Parma win | 13.8% | 11.8% | 7.97 | +10.3% |
| Over 2.5 | 42.0% | 50.7% | 1.90 | -20.2% |
| Under 2.5 | 58.0% | 49.3% | 1.98 | +14.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T18:45:00+00:00 |
| Fixture id | b27cb3ea731fa3f18d05e6a627bdf984 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T17:24:01Z |
| Market best draw last update utc | 2026-10-21T17:24:01Z |
| Market best away last update utc | 2026-10-21T17:24:01Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 17.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Lazio |
| Matched away-team name | Parma |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.6029 |
| Dc lambda away | 0.7067 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T17:22:27.690536+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 39.9% |
| P btts no | 60.1% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 11.07 |
| Fair Over 1.5 odds | 1.46 |
| Fair Under 1.5 odds | 3.15 |
| Fair Over 2.5 odds | 2.38 |
| Fair Under 2.5 odds | 1.72 |
| Fair Over 3.5 odds | 4.81 |
| Fair Under 3.5 odds | 1.26 |
| Fair Over 4.5 odds | 11.25 |
| Fair Under 4.5 odds | 1.10 |
| Goal margin distribution | {"-1": 0.09948725536379804, "-10": 8.197610558612236e-10, "-11": 5.2224438456536e-11, "-12": 3.053745231483196e-12, "-13": 1.649849016992594e-13, "-14": 8.263829794928779e-15, "-15": 3.6202127577731334e-16, "-2": 0.030954408610481373, "-3": 0.006693177267131757, "-4": 0.00112133406874732, "-5": 0.00015287577302948663, "-6": 1.7543463801925334e-05, "-7": 1.736661662816231e-06, "-8": 1.5107479648090647e-07, "-9": 1.1717518275418007e-08, "0": 0.22393771136558518, "1": 0.2878766676829923, "10": 3.698249180524573e-06, "11": 5.34355121770688e-07, "12": 7.086573726277882e-08, "13": 8.683504239588589e-09, "14": 9.86460028845027e-10, "15": 9.801206370527351e-11, "2": 0.1994586682756967, "3": 0.09781603208352621, "4": 0.03716721688466242, "5": 0.01149240708501684, "6": 0.002991127947159097, "7": 0.0006715559064638961, "8": 0.00013249707294579234, "9": 2.3307581755526323e-05} |
| Raw goal margin distribution | {"-1": 0.11439825565104154, "-10": 9.426256106699764e-10, "-11": 6.00517587899694e-11, "-12": 3.511435976466636e-12, "-13": 1.8971259076488504e-13, "-14": 9.502400182616378e-15, "-15": 4.162804804097498e-16, "-2": 0.035593808843149714, "-3": 0.007696340614917606, "-4": 0.0012893979334106468, "-5": 0.00017578856409221745, "-6": 2.0172851785674494e-05, "-7": 1.9969499023339985e-06, "-8": 1.7371765988571766e-07, "-9": 1.3473722301065666e-08, "0": 0.25551195949717953, "1": 0.2642546488773598, "10": 3.3947855049394896e-06, "11": 4.90508057550627e-07, "12": 6.505077562740319e-08, "13": 7.970970285040278e-09, "14": 9.055150271540866e-10, "15": 8.996958207361048e-11, "2": 0.18309188019635386, "3": 0.08978963603008208, "4": 0.0341174223206607, "5": 0.01054938569162209, "6": 0.002745687838425965, "7": 0.0006164506894304941, "8": 0.0001216248880827129, "9": 2.1395053939450773e-05} |
| Unadjusted home-win probability | 58.5% |
| Unadjusted draw probability | 25.6% |
| Unadjusted away-win probability | 15.9% |
| Raw p over 1 5 | 67.5% |
| Raw p under 3 5 | 79.7% |
| Raw p btts yes | 40.9% |
| P home draw | 86.2% |
| P draw away | 36.2% |
| P home away | 77.6% |
| Raw p home draw | 84.1% |
| Raw p draw away | 41.5% |
| Raw p home away | 74.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:24:01Z", "line": 1.25, "market_key": "spreads", "opposite_price": 2.01, "price": 1.9, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:23:35Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.34, "price": 1.7, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:23:35Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.7, "price": 2.34, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:24:01Z", "line": -1.25, "market_key": "spreads", "opposite_price": 1.9, "price": 2.01, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 1.41 |
| Reference draw odds | 4.60 |
| Reference away odds | 7.25 |
| Market reference 1x2 last update utc | 2026-10-21T17:24:07Z |
| Market reference home last update utc | 2026-10-21T17:24:07Z |
| Market reference draw last update utc | 2026-10-21T17:24:07Z |
| Market reference away last update utc | 2026-10-21T17:24:07Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.85 |
| Reference Under 2.5 odds | 1.90 |
| Market reference over 2 5 last update utc | 2026-10-21T17:24:04Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:24:04Z |
| Market best over 2 5 last update utc | 2026-10-21T17:24:01Z |
| Market best under 2 5 last update utc | 2026-10-21T17:24:01Z |
| Home probability edge | -5.2% |
| Draw probability edge | +3.2% |
| Away probability edge | +2.1% |
| Over 2.5 probability edge | -8.7% |
| Under 2.5 probability edge | +8.7% |
| Raw edge prob home | -0.1046 |
| Raw ev home | -0.1630 |
| Raw edge prob draw | 0.0631 |
| Raw ev draw | 0.1932 |
| Raw edge prob away | 0.0415 |
| Raw ev away | 0.2686 |

</details>


---

## 2026-10-24 — Napoli vs AS Roma

The model's most likely 1X2 outcome is **Napoli win** at **36.7%**. Expected goals are 1.20 for Napoli and 1.06 for AS Roma (2.26 combined). The most likely exact score is 1-1 at 13.2%. Goal-market probabilities: at least one goal: 89.6%; Over 2.5 goals: 39.8%; Under 3.5 goals: 80.7%; Double Chance 1X: 64.9%; Double Chance X2: 63.3%; Double Chance 12 (either team wins): 71.8%; Under 4.5 goals: 92.0%; BTTS Yes (both teams score): 45.9%; BTTS No (at least one team does not score): 54.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Napoli win | 36.7% | 2.73 |
| Draw | 28.2% | 3.54 |
| AS Roma win | 35.1% | 2.85 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Napoli expected goals | 1.20 |
| AS Roma expected goals | 1.06 |
| Expected total goals | 2.26 |
| Over 0.5 | 89.6% |
| Under 0.5 | 10.4% |
| Over 1.5 | 66.5% |
| Under 1.5 | 33.5% |
| Over 2.5 | 39.8% |
| Under 2.5 | 60.2% |
| Over 3.5 | 19.3% |
| Under 3.5 | 80.7% |
| Over 4.5 | 8.0% |
| Under 4.5 | 92.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.15% |
| 2 | 0-1 | 11.69% |
| 3 | 1-0 | 11.41% |
| 4 | 0-0 | 10.40% |
| 5 | 1-2 | 7.77% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Napoli win | 36.7% | 34.6% | 2.83 | +3.8% |
| Draw | 28.2% | 27.0% | 3.45 | -2.6% |
| AS Roma win | 35.1% | 38.4% | 2.56 | -10.2% |
| Over 2.5 | 39.8% | 50.7% | 1.92 | -23.6% |
| Under 2.5 | 60.2% | 49.3% | 1.97 | +18.6% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T16:00:00+00:00 |
| Fixture id | 0b4894e9fb123ef3045269f97e339eba |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T17:24:01Z |
| Market best draw last update utc | 2026-10-21T17:24:01Z |
| Market best away last update utc | 2026-10-21T17:24:01Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 17.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Napoli |
| Matched away-team name | Roma |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.2023 |
| Dc lambda away | 1.0610 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T17:22:27.690536+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 45.9% |
| P btts no | 54.1% |
| Fair Over 0.5 odds | 1.12 |
| Fair Under 0.5 odds | 9.61 |
| Fair Over 1.5 odds | 1.50 |
| Fair Under 1.5 odds | 2.99 |
| Fair Over 2.5 odds | 2.51 |
| Fair Under 2.5 odds | 1.66 |
| Fair Over 3.5 odds | 5.17 |
| Fair Under 3.5 odds | 1.24 |
| Fair Over 4.5 odds | 12.45 |
| Fair Under 4.5 odds | 1.09 |
| Goal margin distribution | {"-1": 0.21299636074764314, "-10": 6.422118612236176e-08, "-11": 6.134968867608018e-09, "-12": 5.359175085529602e-10, "-13": 3.9832086892613716e-11, "-2": 0.09688804110056755, "-3": 0.031147323172464162, "-4": 0.007785258093558538, "-5": 0.0015865750350633413, "-6": 0.00027247514813387376, "-7": 4.039656642834299e-05, "-8": 5.265786748809876e-06, "-9": 6.122217222068357e-07, "0": 0.2823868445289366, "1": 0.20735112778233072, "10": 1.9200358843545878e-07, "11": 2.0783486192681537e-08, "12": 2.0572117248109565e-09, "13": 1.732563324096041e-10, "2": 0.10658623221230777, "3": 0.03882635981315124, "4": 0.010996487165441887, "5": 0.002539315036428308, "6": 0.000494148949418248, "7": 8.301382843601639e-05, "8": 1.2261518798990782e-05, "9": 1.6153429729606531e-06} |
| Raw goal margin distribution | {"-1": 0.19293954068782362, "-10": 5.8173792779287274e-08, "-11": 5.5572690129330585e-09, "-12": 4.854527916994708e-10, "-13": 3.608129511097015e-11, "-2": 0.08776457063618316, "-3": 0.028214332890271875, "-4": 0.00705215861639536, "-5": 0.0014371750646696249, "-6": 0.0002468175031031746, "-7": 3.659262038417666e-05, "-8": 4.769933500784698e-06, "-9": 5.545718127158297e-07, "0": 0.2944166788411053, "1": 0.2192171594776642, "10": 2.0299133029324418e-07, "11": 2.1972857615636975e-08, "12": 2.174939271276217e-09, "13": 1.8317122968447097e-10, "2": 0.11268581615595101, "3": 0.041048266301361505, "4": 0.011625780416161214, "5": 0.0026846317898453725, "6": 0.0005224274891046491, "7": 8.776444026006592e-05, "8": 1.2963205702061248e-05, "9": 1.7077838056727227e-06} |
| Unadjusted home-win probability | 38.8% |
| Unadjusted draw probability | 29.4% |
| Unadjusted away-win probability | 31.8% |
| Raw p over 1 5 | 66.5% |
| Raw p under 3 5 | 80.7% |
| Raw p btts yes | 46.2% |
| P home draw | 64.9% |
| P draw away | 63.3% |
| P home away | 71.8% |
| Raw p home draw | 68.2% |
| Raw p draw away | 61.2% |
| Raw p home away | 70.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:23:35Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.09, "price": 1.86, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:24:01Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.06, "price": 1.86, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:23:35Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.86, "price": 2.09, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:24:01Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.86, "price": 2.06, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 2.70 |
| Reference draw odds | 3.40 |
| Reference away odds | 2.45 |
| Market reference 1x2 last update utc | 2026-10-21T17:24:07Z |
| Market reference home last update utc | 2026-10-21T17:24:07Z |
| Market reference draw last update utc | 2026-10-21T17:24:07Z |
| Market reference away last update utc | 2026-10-21T17:24:07Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.85 |
| Reference Under 2.5 odds | 1.90 |
| Market reference over 2 5 last update utc | 2026-10-21T17:24:04Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:24:04Z |
| Market best over 2 5 last update utc | 2026-10-21T17:24:01Z |
| Market best under 2 5 last update utc | 2026-10-21T17:24:01Z |
| Home probability edge | +2.1% |
| Draw probability edge | +1.2% |
| Away probability edge | -3.3% |
| Over 2.5 probability edge | -11.0% |
| Under 2.5 probability edge | +11.0% |
| Raw edge prob home | 0.0420 |
| Raw ev home | 0.0977 |
| Raw edge prob draw | 0.0241 |
| Raw ev draw | 0.0157 |
| Raw edge prob away | -0.0661 |
| Raw ev away | -0.1867 |

</details>


---

## 2026-10-25 — Atalanta BC vs Frosinone

The model's most likely 1X2 outcome is **Atalanta BC win** at **58.5%**. Expected goals are 2.25 for Atalanta BC and 1.11 for Frosinone (3.35 combined). The most likely exact score is 1-1 at 9.4%. Goal-market probabilities: at least one goal: 96.0%; Over 2.5 goals: 64.6%; Under 3.5 goals: 57.4%; Double Chance 1X: 79.4%; Double Chance X2: 41.5%; Double Chance 12 (either team wins): 79.2%; Under 4.5 goals: 75.7%; BTTS Yes (both teams score): 60.7%; BTTS No (at least one team does not score): 39.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Atalanta BC win | 58.5% | 1.71 |
| Draw | 20.8% | 4.80 |
| Frosinone win | 20.6% | 4.85 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Atalanta BC expected goals | 2.25 |
| Frosinone expected goals | 1.11 |
| Expected total goals | 3.35 |
| Over 0.5 | 96.0% |
| Under 0.5 | 4.0% |
| Over 1.5 | 84.7% |
| Under 1.5 | 15.3% |
| Over 2.5 | 64.6% |
| Under 2.5 | 35.4% |
| Over 3.5 | 42.6% |
| Under 3.5 | 57.4% |
| Over 4.5 | 24.3% |
| Under 4.5 | 75.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.40% |
| 2 | 2-1 | 9.10% |
| 3 | 2-0 | 8.22% |
| 4 | 1-0 | 7.04% |
| 5 | 3-1 | 6.82% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Atalanta BC win | 58.5% | 54.3% | 1.84 | +7.7% |
| Draw | 20.8% | 21.8% | 4.20 | -12.5% |
| Frosinone win | 20.6% | 24.0% | 3.95 | -18.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T14:00:00+00:00 |
| Fixture id | 63aa6e3f679ee4c68de5b4bd8d3361bb |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T17:24:01Z |
| Market best draw last update utc | 2026-10-21T17:24:01Z |
| Market best away last update utc | 2026-10-21T17:24:01Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Atalanta |
| Matched away-team name | Frosinone |
| Home-name matching confidence | 95/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.2475 |
| Dc lambda away | 1.1073 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T17:22:27.690536+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 60.7% |
| P btts no | 39.3% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 25.26 |
| Fair Over 1.5 odds | 1.18 |
| Fair Under 1.5 odds | 6.55 |
| Fair Over 2.5 odds | 1.55 |
| Fair Under 2.5 odds | 2.82 |
| Fair Over 3.5 odds | 2.35 |
| Fair Under 3.5 odds | 1.74 |
| Fair Over 4.5 odds | 4.11 |
| Fair Under 4.5 odds | 1.32 |
| Goal margin distribution | {"-1": 0.12946738331514115, "-10": 3.9800035990620126e-08, "-11": 3.933291617474849e-09, "-12": 3.573096441838294e-10, "-13": 3.002777801319862e-11, "-14": 2.3473341243770274e-12, "-15": 1.7143615079805718e-13, "-16": 1.1655335551939383e-14, "-17": 6.622129553194149e-16, "-2": 0.054535264173414595, "-3": 0.016972670425904956, "-4": 0.004212335288219342, "-5": 0.0008649441528036384, "-6": 0.0001510402275584699, "-7": 2.2906884594200242e-05, "-8": 3.067280888172895e-06, "-9": 3.674275999151134e-07, "0": 0.2084180789614807, "1": 0.20810736221648002, "10": 3.6904317811212606e-05, "11": 7.402696433239611e-06, "12": 1.3649558658727842e-06, "13": 2.3282903832062212e-07, "14": 3.694272585183514e-08, "15": 5.476416985097628e-09, "16": 7.557165962405862e-10, "17": 8.71509104593702e-11, "2": 0.1755296643491169, "3": 0.11088258863299436, "4": 0.055856817460156076, "5": 0.02327991547459261, "6": 0.00825136959136306, "7": 0.0025400339054039707, "8": 0.0006903464748265439, "9": 0.00016785157310632732} |
| Raw goal margin distribution | {"-1": 0.10850287149403126, "-10": 3.3355259679856665e-08, "-11": 3.296378006502222e-09, "-12": 2.994508841820553e-10, "-13": 2.5165412751771858e-11, "-14": 1.9672328761822502e-12, "-15": 1.436756823469186e-13, "-16": 9.767999809910378e-15, "-17": 5.54981535525497e-16, "-2": 0.04570442847444987, "-3": 0.014224304461687057, "-4": 0.0035302364407482755, "-5": 0.000724884691866568, "-6": 0.00012658244865669806, "-7": 1.919759781815595e-05, "-8": 2.57059944770352e-06, "-9": 3.0793045040470416e-07, "0": 0.19924366984493658, "1": 0.22324171932316317, "10": 3.95881398470348e-05, "11": 7.941048609634388e-06, "12": 1.4642206361767383e-06, "13": 2.497612495274723e-07, "14": 3.9629341066122313e-08, "15": 5.874682810173801e-09, "16": 8.106751749142936e-10, "17": 9.348885538845271e-11, "2": 0.18829484764096197, "3": 0.11894639125589021, "4": 0.05991893719143906, "5": 0.024972919270582206, "6": 0.008851440500363444, "7": 0.0027247548099315023, "8": 0.0007405510902043336, "9": 0.0001800583764661583} |
| Unadjusted home-win probability | 62.8% |
| Unadjusted draw probability | 19.9% |
| Unadjusted away-win probability | 17.3% |
| Raw p over 1 5 | 85.1% |
| Raw p under 3 5 | 56.8% |
| Raw p btts yes | 60.2% |
| P home draw | 79.4% |
| P draw away | 41.5% |
| P home away | 79.2% |
| Raw p home draw | 82.7% |
| Raw p draw away | 37.2% |
| Raw p home away | 80.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:24:01Z", "line": 0.75, "market_key": "spreads", "opposite_price": 2.06, "price": 1.85, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:23:35Z", "line": 1.5, "market_key": "spreads", "opposite_price": 3.06, "price": 1.45, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:23:35Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.45, "price": 3.06, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:24:01Z", "line": -0.75, "market_key": "spreads", "opposite_price": 1.85, "price": 2.06, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 1.76 |
| Reference draw odds | 4.10 |
| Reference away odds | 3.75 |
| Market reference 1x2 last update utc | 2026-10-21T17:24:06Z |
| Market reference home last update utc | 2026-10-21T17:24:06Z |
| Market reference draw last update utc | 2026-10-21T17:24:06Z |
| Market reference away last update utc | 2026-10-21T17:24:06Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.40 |
| Reference Under 2.5 odds | 2.92 |
| Market reference over 2 5 last update utc | 2026-10-21T17:24:04Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:24:04Z |
| Home probability edge | +4.3% |
| Draw probability edge | -0.9% |
| Away probability edge | -3.3% |
| Over 2.5 probability edge | -4.6% |
| Under 2.5 probability edge | +4.6% |
| Raw edge prob home | 0.0851 |
| Raw ev home | 0.1554 |
| Raw edge prob draw | -0.0183 |
| Raw ev draw | -0.1632 |
| Raw edge prob away | -0.0668 |
| Raw ev away | -0.3173 |

</details>


---

## 2026-10-25 — Genoa vs Venezia

The model's most likely 1X2 outcome is **Genoa win** at **47.6%**. Expected goals are 1.40 for Genoa and 0.86 for Venezia (2.26 combined). The most likely exact score is 1-0 at 13.8%. Goal-market probabilities: at least one goal: 89.0%; Over 2.5 goals: 39.1%; Under 3.5 goals: 80.9%; Double Chance 1X: 76.1%; Double Chance X2: 52.4%; Double Chance 12 (either team wins): 71.4%; Under 4.5 goals: 92.2%; BTTS Yes (both teams score): 43.9%; BTTS No (at least one team does not score): 56.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Genoa win | 47.6% | 2.10 |
| Draw | 28.6% | 3.50 |
| Venezia win | 23.9% | 4.19 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Genoa expected goals | 1.40 |
| Venezia expected goals | 0.86 |
| Expected total goals | 2.26 |
| Over 0.5 | 89.0% |
| Under 0.5 | 11.0% |
| Over 1.5 | 66.2% |
| Under 1.5 | 33.8% |
| Over 2.5 | 39.1% |
| Under 2.5 | 60.9% |
| Over 3.5 | 19.1% |
| Under 3.5 | 80.9% |
| Over 4.5 | 7.8% |
| Under 4.5 | 92.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 13.76% |
| 2 | 1-1 | 13.16% |
| 3 | 0-0 | 11.03% |
| 4 | 2-0 | 9.90% |
| 5 | 0-1 | 9.02% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Genoa win | 47.6% | 46.0% | 2.16 | +2.8% |
| Draw | 28.6% | 28.9% | 3.22 | -8.0% |
| Venezia win | 23.9% | 25.0% | 3.83 | -8.6% |
| Over 2.5 | 39.1% | 48.5% | 2.02 | -21.1% |
| Under 2.5 | 60.9% | 51.5% | 1.87 | +14.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T14:00:00+00:00 |
| Fixture id | 95cfaecfe96bb7ced1fb6af974a4110b |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T17:24:01Z |
| Market best draw last update utc | 2026-10-21T17:24:01Z |
| Market best away last update utc | 2026-10-21T17:24:01Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 17.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Genoa |
| Matched away-team name | Venezia |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.3976 |
| Dc lambda away | 0.8591 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T17:22:27.690536+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 43.9% |
| P btts no | 56.1% |
| Fair Over 0.5 odds | 1.12 |
| Fair Under 0.5 odds | 9.06 |
| Fair Over 1.5 odds | 1.51 |
| Fair Under 1.5 odds | 2.96 |
| Fair Over 2.5 odds | 2.56 |
| Fair Under 2.5 odds | 1.64 |
| Fair Over 3.5 odds | 5.24 |
| Fair Under 3.5 odds | 1.24 |
| Fair Over 4.5 odds | 12.80 |
| Fair Under 4.5 odds | 1.08 |
| Goal margin distribution | {"-1": 0.15961017446262338, "-10": 7.409978377550954e-09, "-11": 5.735186709506417e-10, "-12": 4.074212103558387e-11, "-13": 2.6663975972260452e-12, "-14": 1.5069195093581292e-13, "-2": 0.05957730740974338, "-3": 0.01558604861786555, "-4": 0.0031645116259606362, "-5": 0.0005233314467379514, "-6": 7.288885163286464e-05, "-7": 8.760418368497776e-06, "-8": 9.254911867471426e-07, "-9": 8.718918180247477e-08, "0": 0.2856626605753042, "1": 0.24150995204119066, "10": 8.856856898404507e-07, "11": 1.1152414865397744e-07, "12": 1.2889131629230595e-08, "13": 1.372345941136783e-09, "14": 1.261790975659789e-10, "2": 0.14510227100568857, "3": 0.061757262011669936, "4": 0.02039939892539931, "5": 0.005488405313560609, "6": 0.001243624074306781, "7": 0.0002431708586924959, "8": 4.179435596211636e-05, "9": 6.405700373059924e-06} |
| Raw goal margin distribution | {"-1": 0.15166257077527623, "-10": 7.041007090633543e-09, "-11": 5.449609733016291e-10, "-12": 3.871341432899119e-11, "-13": 2.533627418589283e-12, "-14": 1.4318841985489516e-13, "-2": 0.056610724423125765, "-3": 0.014809959387441661, "-4": 0.0030069384364580635, "-5": 0.0004972727637636197, "-6": 6.925943572655278e-05, "-7": 8.32420348706814e-06, "-8": 8.794074255260097e-07, "-9": 8.284769752602972e-08, "0": 0.28201882816535645, "1": 0.24938875757661466, "10": 9.145795108063486e-07, "11": 1.1516241313261284e-07, "12": 1.3309615177709254e-08, "13": 1.417116132618172e-09, "14": 1.3029545204311482e-10, "2": 0.14983595823613124, "3": 0.06377197591342744, "4": 0.021064890743911803, "5": 0.005667454159372796, "6": 0.001284194958271694, "7": 0.00025110384816695645, "8": 4.315781780010985e-05, "9": 6.6146742357557535e-06} |
| Unadjusted home-win probability | 49.1% |
| Unadjusted draw probability | 28.2% |
| Unadjusted away-win probability | 22.7% |
| Raw p over 1 5 | 66.3% |
| Raw p under 3 5 | 80.8% |
| Raw p btts yes | 43.8% |
| P home draw | 76.1% |
| P draw away | 52.4% |
| P home away | 71.4% |
| Raw p home draw | 77.3% |
| Raw p draw away | 50.9% |
| Raw p home away | 71.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:23:35Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.53, "price": 2.75, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:24:01Z", "line": 0.25, "market_key": "spreads", "opposite_price": 1.85, "price": 2.07, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:24:01Z", "line": -0.25, "market_key": "spreads", "opposite_price": 2.07, "price": 1.85, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:23:35Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.75, "price": 1.53, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 2.05 |
| Reference draw odds | 3.15 |
| Reference away odds | 3.60 |
| Market reference 1x2 last update utc | 2026-10-21T17:24:06Z |
| Market reference home last update utc | 2026-10-21T17:24:06Z |
| Market reference draw last update utc | 2026-10-21T17:24:06Z |
| Market reference away last update utc | 2026-10-21T17:24:06Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.92 |
| Reference Under 2.5 odds | 1.82 |
| Market reference over 2 5 last update utc | 2026-10-21T17:24:04Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:24:04Z |
| Market best over 2 5 last update utc | 2026-10-21T17:24:01Z |
| Market best under 2 5 last update utc | 2026-10-21T17:24:01Z |
| Home probability edge | +1.6% |
| Draw probability edge | -0.4% |
| Away probability edge | -1.2% |
| Over 2.5 probability edge | -9.5% |
| Under 2.5 probability edge | +9.5% |
| Raw edge prob home | 0.0310 |
| Raw ev home | 0.0612 |
| Raw edge prob draw | -0.0073 |
| Raw ev draw | -0.0919 |
| Raw edge prob away | -0.0238 |
| Raw ev away | -0.1319 |

</details>


---

## 2026-10-25 — Inter Milan vs Fiorentina

The model's most likely 1X2 outcome is **Inter Milan win** at **71.5%**. Expected goals are 2.41 for Inter Milan and 0.94 for Fiorentina (3.34 combined). The most likely exact score is 2-0 at 10.5%. Goal-market probabilities: at least one goal: 96.5%; Over 2.5 goals: 65.6%; Under 3.5 goals: 56.8%; Double Chance 1X: 87.8%; Double Chance X2: 28.5%; Double Chance 12 (either team wins): 83.6%; Under 4.5 goals: 75.1%; BTTS Yes (both teams score): 55.2%; BTTS No (at least one team does not score): 44.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Inter Milan win | 71.5% | 1.40 |
| Draw | 16.4% | 6.11 |
| Fiorentina win | 12.2% | 8.22 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Inter Milan expected goals | 2.41 |
| Fiorentina expected goals | 0.94 |
| Expected total goals | 3.34 |
| Over 0.5 | 96.5% |
| Under 0.5 | 3.5% |
| Over 1.5 | 85.1% |
| Under 1.5 | 14.9% |
| Over 2.5 | 65.6% |
| Under 2.5 | 34.4% |
| Over 3.5 | 43.2% |
| Under 3.5 | 56.8% |
| Over 4.5 | 24.9% |
| Under 4.5 | 75.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 10.50% |
| 2 | 2-1 | 9.85% |
| 3 | 1-0 | 8.46% |
| 4 | 3-0 | 8.42% |
| 5 | 3-1 | 7.90% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Inter Milan win | 71.5% | 73.4% | 1.35 | -3.5% |
| Draw | 16.4% | 14.9% | 5.75 | -5.9% |
| Fiorentina win | 12.2% | 11.7% | 8.05 | -2.1% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T11:30:00+00:00 |
| Fixture id | c9b6c7048d8dc33dae618f67f462f67a |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T17:24:01Z |
| Market best draw last update utc | 2026-10-21T17:24:01Z |
| Market best away last update utc | 2026-10-21T17:24:01Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Inter |
| Matched away-team name | Fiorentina |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.4051 |
| Dc lambda away | 0.9383 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T17:22:27.690536+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 55.2% |
| P btts no | 44.8% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 28.69 |
| Fair Over 1.5 odds | 1.17 |
| Fair Under 1.5 odds | 6.72 |
| Fair Over 2.5 odds | 1.53 |
| Fair Under 2.5 odds | 2.90 |
| Fair Over 3.5 odds | 2.31 |
| Fair Under 3.5 odds | 1.76 |
| Fair Over 4.5 odds | 4.01 |
| Fair Under 4.5 odds | 1.33 |
| Goal margin distribution | {"-1": 0.08169294939103343, "-10": 6.071127110564876e-09, "-11": 5.092688081558123e-10, "-12": 3.925843429098512e-11, "-13": 2.799131642420234e-12, "-14": 1.8562021151652155e-13, "-15": 1.1503438810438469e-14, "-16": 6.688833566156879e-16, "-17": 3.6409574216354765e-17, "-18": 1.68646542721103e-18, "-2": 0.029918854811847643, "-3": 0.007996794635037227, "-4": 0.0016970898831818527, "-5": 0.00029720948335546323, "-6": 4.419221039645389e-05, "-7": 5.700583283195759e-06, "-8": 6.487429094565292e-07, "-9": 6.601072907238168e-08, "0": 0.16362293348354673, "1": 0.22796653710735001, "10": 7.94177327072406e-05, "11": 1.707656003411718e-05, "12": 3.374360205169748e-06, "13": 6.16718452475087e-07, "14": 1.048320397238974e-07, "15": 1.6653350130648565e-08, "16": 2.4821582683586516e-09, "17": 3.463377519445642e-10, "18": 4.1121299396057906e-11, "2": 0.2099674124780106, "3": 0.1438560153479088, "4": 0.07825679936368245, "5": 0.03513055844149925, "6": 0.013389774678298582, "7": 0.004427432948764034, "8": 0.001291547774983522, "9": 0.0003368662751247712} |
| Raw goal margin distribution | {"-1": 0.08487582713538863, "-10": 6.3076671731702e-09, "-11": 5.291106717126612e-10, "-12": 4.0788000767828754e-11, "-13": 2.908189937837314e-12, "-14": 1.928522486083699e-13, "-15": 1.195162974547301e-14, "-16": 6.9494403829277e-16, "-17": 3.782814490475012e-17, "-18": 1.7521726065319873e-18, "-2": 0.03108453750328046, "-3": 0.008308361543317232, "-4": 0.0017632110069705697, "-5": 0.0003087892029889822, "-6": 4.5914004064001104e-05, "-7": 5.922686412011411e-06, "-8": 6.740188896201746e-07, "-9": 6.858260439356095e-08, "0": 0.17835681850926116, "1": 0.22175525645533212, "10": 7.725388079787321e-05, "11": 1.6611284260361896e-05, "12": 3.28242084195768e-06, "13": 5.99915059134085e-07, "14": 1.0197573796877624e-07, "15": 1.619960532770379e-08, "16": 2.414528247640996e-09, "17": 3.369012749729302e-10, "18": 4.000088964397094e-11, "2": 0.204246544217136, "3": 0.13993644848452264, "4": 0.07612457877576521, "5": 0.03417337516051835, "6": 0.0130249507464641, "7": 0.004306801083395939, "8": 0.0012563576729286126, "9": 0.000327687862347397} |
| Unadjusted home-win probability | 69.5% |
| Unadjusted draw probability | 17.8% |
| Unadjusted away-win probability | 12.6% |
| Raw p over 1 5 | 84.9% |
| Raw p under 3 5 | 57.1% |
| Raw p btts yes | 55.6% |
| P home draw | 87.8% |
| P draw away | 28.5% |
| P home away | 83.6% |
| Raw p home draw | 87.4% |
| Raw p draw away | 30.5% |
| Raw p home away | 82.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:23:35Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.05, "price": 1.9, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:24:01Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.96, "price": 1.94, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:23:35Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.9, "price": 2.05, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:24:01Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.94, "price": 1.96, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 1.33 |
| Reference draw odds | 5.80 |
| Reference away odds | 7.25 |
| Market reference 1x2 last update utc | 2026-10-21T17:24:07Z |
| Market reference home last update utc | 2026-10-21T17:24:07Z |
| Market reference draw last update utc | 2026-10-21T17:24:07Z |
| Market reference away last update utc | 2026-10-21T17:24:07Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.40 |
| Reference Under 2.5 odds | 2.88 |
| Market reference over 2 5 last update utc | 2026-10-21T17:24:04Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:24:04Z |
| Home probability edge | -1.9% |
| Draw probability edge | +1.5% |
| Away probability edge | +0.5% |
| Over 2.5 probability edge | -3.4% |
| Under 2.5 probability edge | +3.4% |
| Raw edge prob home | -0.0389 |
| Raw ev home | -0.0614 |
| Raw edge prob draw | 0.0295 |
| Raw ev draw | 0.0256 |
| Raw edge prob away | 0.0095 |
| Raw ev away | 0.0175 |

</details>


---

## 2026-10-25 — Lecce vs Juventus

The model's most likely 1X2 outcome is **Juventus win** at **63.0%**. Expected goals are 0.62 for Lecce and 1.48 for Juventus (2.11 combined). The most likely exact score is 0-1 at 19.3%. Goal-market probabilities: at least one goal: 89.1%; Over 2.5 goals: 36.6%; Under 3.5 goals: 83.2%; Double Chance 1X: 37.0%; Double Chance X2: 86.6%; Double Chance 12 (either team wins): 76.5%; Under 4.5 goals: 93.4%; BTTS Yes (both teams score): 35.3%; BTTS No (at least one team does not score): 64.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lecce win | 13.4% | 7.45 |
| Draw | 23.5% | 4.25 |
| Juventus win | 63.0% | 1.59 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lecce expected goals | 0.62 |
| Juventus expected goals | 1.48 |
| Expected total goals | 2.11 |
| Over 0.5 | 89.1% |
| Under 0.5 | 10.9% |
| Over 1.5 | 63.5% |
| Under 1.5 | 36.5% |
| Over 2.5 | 36.6% |
| Under 2.5 | 63.4% |
| Over 3.5 | 16.8% |
| Under 3.5 | 83.2% |
| Over 4.5 | 6.6% |
| Under 4.5 | 93.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 19.28% |
| 2 | 0-2 | 14.60% |
| 3 | 0-0 | 10.91% |
| 4 | 1-1 | 10.12% |
| 5 | 1-2 | 9.11% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lecce win | 13.4% | 11.6% | 8.19 | +9.9% |
| Draw | 23.5% | 20.0% | 4.35 | +2.4% |
| Juventus win | 63.0% | 68.3% | 1.46 | -8.0% |
| Over 2.5 | 36.6% | 52.5% | 1.92 | -29.6% |
| Under 2.5 | 63.4% | 47.5% | 2.02 | +28.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T17:00:00+00:00 |
| Fixture id | 63af660d4d0d52f8ac7685172ef939c4 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T17:24:01Z |
| Market best draw last update utc | 2026-10-21T17:24:01Z |
| Market best away last update utc | 2026-10-21T17:24:01Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 16.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Lecce |
| Matched away-team name | Juventus |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.6238 |
| Dc lambda away | 1.4832 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T17:22:27.690536+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 35.3% |
| P btts no | 64.7% |
| Fair Over 0.5 odds | 1.12 |
| Fair Under 0.5 odds | 9.17 |
| Fair Over 1.5 odds | 1.58 |
| Fair Under 1.5 odds | 2.74 |
| Fair Over 2.5 odds | 2.73 |
| Fair Under 2.5 odds | 1.58 |
| Fair Over 3.5 odds | 5.96 |
| Fair Under 3.5 odds | 1.20 |
| Fair Over 4.5 odds | 15.10 |
| Fair Under 4.5 odds | 1.07 |
| Goal margin distribution | {"-1": 0.29906081821267866, "-10": 2.0502226943820057e-06, "-11": 2.7453838021197695e-07, "-12": 3.3734693875554216e-08, "-13": 3.829441436558385e-09, "-14": 4.032643055849214e-10, "-15": 3.755887776588145e-11, "-2": 0.19661500697126083, "-3": 0.09052837554161458, "-4": 0.03212600296540493, "-5": 0.009250823800190525, "-6": 0.0022383400078487188, "-7": 0.000466670189922, "-8": 8.543594730091834e-05, "-9": 1.3938087841208168e-05, "0": 0.23536369697532347, "1": 0.09976000403261222, "10": 2.8716824853673173e-10, "11": 1.617351818670053e-11, "12": 8.35880625614942e-13, "13": 3.990882755155101e-14, "14": 1.7676218891955443e-15, "15": 6.924337807127857e-17, "2": 0.028120538633005152, "3": 0.00544575063515214, "4": 0.0008128225990715216, "5": 9.844315754888077e-05, "6": 1.0018373868636565e-05, "7": 8.785111716863497e-07, "8": 6.764628007241523e-08, "9": 4.64165148590532e-09} |
| Raw goal margin distribution | {"-1": 0.27391379911634745, "-10": 1.8778263585614746e-06, "-11": 2.51453370510182e-07, "-12": 3.089805684577737e-08, "-13": 3.507436576446848e-09, "-14": 3.693551654507531e-10, "-15": 3.440067796538566e-11, "-2": 0.1800823118342622, "-3": 0.08291614869722112, "-4": 0.0294246353476473, "-5": 0.008472953117730378, "-6": 0.0020501255193782673, "-7": 0.0004274294620734211, "-8": 7.825192563225077e-05, "-9": 1.2766080878865336e-05, "0": 0.27053347733477706, "1": 0.11301497231613046, "10": 3.253238807793238e-10, "11": 1.8322470291068313e-11, "12": 9.469428823657681e-13, "13": 4.521145608046803e-14, "14": 2.002483267818586e-15, "15": 7.844364614542999e-17, "2": 0.03185687416456831, "3": 0.006169319691196821, "4": 0.0009208211689923668, "5": 0.00011152315833369661, "6": 1.1349500798400866e-05, "7": 9.952376877920656e-07, "8": 7.663434403204312e-08, "9": 5.258381044263269e-09} |
| Unadjusted home-win probability | 15.2% |
| Unadjusted draw probability | 27.1% |
| Unadjusted away-win probability | 57.7% |
| Raw p over 1 5 | 62.6% |
| Raw p under 3 5 | 83.7% |
| Raw p btts yes | 36.3% |
| P home draw | 37.0% |
| P draw away | 86.6% |
| P home away | 76.5% |
| Raw p home draw | 42.3% |
| Raw p draw away | 84.8% |
| Raw p home away | 72.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:23:35Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.69, "price": 2.36, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:24:01Z", "line": -1.25, "market_key": "spreads", "opposite_price": 1.88, "price": 2.02, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:24:01Z", "line": 1.25, "market_key": "spreads", "opposite_price": 2.02, "price": 1.88, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:23:35Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.36, "price": 1.69, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 7.25 |
| Reference draw odds | 4.40 |
| Reference away odds | 1.42 |
| Market reference 1x2 last update utc | 2026-10-21T17:24:07Z |
| Market reference home last update utc | 2026-10-21T17:24:07Z |
| Market reference draw last update utc | 2026-10-21T17:24:07Z |
| Market reference away last update utc | 2026-10-21T17:24:07Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.82 |
| Reference Under 2.5 odds | 2.00 |
| Market reference over 2 5 last update utc | 2026-10-21T17:24:05Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:24:05Z |
| Market best over 2 5 last update utc | 2026-10-21T17:23:35Z |
| Market best under 2 5 last update utc | 2026-10-21T17:23:35Z |
| Home probability edge | +1.8% |
| Draw probability edge | +3.5% |
| Away probability edge | -5.3% |
| Over 2.5 probability edge | -15.9% |
| Under 2.5 probability edge | +15.9% |
| Raw edge prob home | 0.0357 |
| Raw ev home | 0.2456 |
| Raw edge prob draw | 0.0703 |
| Raw ev draw | 0.1768 |
| Raw edge prob away | -0.1060 |
| Raw ev away | -0.1570 |

</details>


---

## 2026-10-25 — Udinese vs AC Milan

The model's most likely 1X2 outcome is **AC Milan win** at **55.5%**. Expected goals are 1.04 for Udinese and 1.69 for AC Milan (2.74 combined). The most likely exact score is 1-1 at 11.3%. Goal-market probabilities: at least one goal: 93.4%; Over 2.5 goals: 52.1%; Under 3.5 goals: 70.3%; Double Chance 1X: 44.5%; Double Chance X2: 79.4%; Double Chance 12 (either team wins): 76.2%; Under 4.5 goals: 85.5%; BTTS Yes (both teams score): 52.9%; BTTS No (at least one team does not score): 47.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Udinese win | 20.6% | 4.84 |
| Draw | 23.8% | 4.20 |
| AC Milan win | 55.5% | 1.80 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Udinese expected goals | 1.04 |
| AC Milan expected goals | 1.69 |
| Expected total goals | 2.74 |
| Over 0.5 | 93.4% |
| Under 0.5 | 6.6% |
| Over 1.5 | 76.4% |
| Under 1.5 | 23.6% |
| Over 2.5 | 52.1% |
| Under 2.5 | 47.9% |
| Over 3.5 | 29.7% |
| Under 3.5 | 70.3% |
| Over 4.5 | 14.5% |
| Under 4.5 | 85.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.33% |
| 2 | 0-1 | 11.26% |
| 3 | 1-2 | 10.32% |
| 4 | 0-2 | 9.88% |
| 5 | 0-0 | 6.57% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Udinese win | 20.6% | 18.3% | 5.21 | +7.6% |
| Draw | 23.8% | 22.7% | 4.02 | -4.3% |
| AC Milan win | 55.5% | 58.9% | 1.68 | -6.7% |
| Over 2.5 | 52.1% | 51.4% | 1.91 | -0.6% |
| Under 2.5 | 47.9% | 48.6% | 1.98 | -5.1% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T19:45:00+00:00 |
| Fixture id | 3564688383b255192409c9deb8e526ed |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T17:24:01Z |
| Market best draw last update utc | 2026-10-21T17:24:01Z |
| Market best away last update utc | 2026-10-21T17:24:01Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 17.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Udinese |
| Matched away-team name | Milan |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.0448 |
| Dc lambda away | 1.6923 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T17:22:27.690536+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 52.9% |
| P btts no | 47.1% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.23 |
| Fair Over 1.5 odds | 1.31 |
| Fair Under 1.5 odds | 4.24 |
| Fair Over 2.5 odds | 1.92 |
| Fair Under 2.5 odds | 2.09 |
| Fair Over 3.5 odds | 3.37 |
| Fair Under 3.5 odds | 1.42 |
| Fair Over 4.5 odds | 6.90 |
| Fair Under 4.5 odds | 1.17 |
| Goal margin distribution | {"-1": 0.25116206523645246, "-10": 4.297037898407056e-06, "-11": 6.524474860792731e-07, "-12": 9.09906415397601e-08, "-13": 1.1729220654826177e-08, "-14": 1.3979955067294468e-09, "-15": 1.4109309451037963e-10, "-2": 0.17150439246868757, "-3": 0.08516724028765171, "-4": 0.03325067697827583, "-5": 0.010651086144124725, "-6": 0.0028863120401903595, "-7": 0.0006769272777732578, "-8": 0.00013982907817128748, "-9": 2.579410655402476e-05, "0": 0.23805288726117835, "1": 0.12942533444599894, "10": 2.914220547496687e-08, "11": 2.7317431203544214e-09, "12": 2.3519716737874e-10, "13": 1.8717402534135758e-11, "14": 1.3772832423216594e-12, "15": 8.581521807812701e-14, "2": 0.0551188271237799, "3": 0.016898118799051332, "4": 0.004072933694594213, "5": 0.0008054559783047413, "6": 0.00013475108076158366, "7": 1.9510664232694165e-05, "8": 2.48810439612932e-06, "9": 2.833561594382396e-07} |
| Raw goal margin distribution | {"-1": 0.23577601623718422, "-10": 4.0338037368533936e-06, "-11": 6.124789144686902e-07, "-12": 8.541660523818884e-08, "-13": 1.1010695094254412e-08, "-14": 1.3123550763282787e-09, "-15": 1.324498096912675e-10, "-2": 0.16099812838127955, "-3": 0.0799499423212386, "-4": 0.031213758923931287, "-5": 0.009998606506506483, "-6": 0.0027094981633187126, "-7": 0.0006354590876827068, "-8": 0.00013126322629297728, "-9": 2.4213973873721534e-05, "0": 0.24869158706230624, "1": 0.1440861654121967, "10": 3.2443328475958275e-08, "11": 3.041185041459134e-09, "12": 2.6183944672403254e-10, "13": 2.0837641789099716e-11, "14": 1.5332968767054248e-12, "15": 9.553605373952337e-14, "2": 0.06136248730805377, "3": 0.01881227621204984, "4": 0.0045343008039671565, "5": 0.0008966951008396439, "6": 0.00015001519289244557, "7": 2.1720761286552788e-05, "8": 2.7699478090441643e-06, "9": 3.1545371417539433e-07} |
| Unadjusted home-win probability | 23.0% |
| Unadjusted draw probability | 24.9% |
| Unadjusted away-win probability | 52.1% |
| Raw p over 1 5 | 76.2% |
| Raw p under 3 5 | 70.6% |
| Raw p btts yes | 53.3% |
| P home draw | 44.5% |
| P draw away | 79.4% |
| P home away | 76.2% |
| Raw p home draw | 47.9% |
| Raw p draw away | 77.0% |
| Raw p home away | 75.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:23:35Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.5, "price": 2.86, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:24:01Z", "line": -0.75, "market_key": "spreads", "opposite_price": 2.03, "price": 1.88, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:24:01Z", "line": 0.75, "market_key": "spreads", "opposite_price": 1.88, "price": 2.03, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:23:35Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.86, "price": 1.5, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 4.90 |
| Reference draw odds | 4.00 |
| Reference away odds | 1.64 |
| Market reference 1x2 last update utc | 2026-10-21T17:24:07Z |
| Market reference home last update utc | 2026-10-21T17:24:07Z |
| Market reference draw last update utc | 2026-10-21T17:24:07Z |
| Market reference away last update utc | 2026-10-21T17:24:07Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.86 |
| Reference Under 2.5 odds | 1.96 |
| Market reference over 2 5 last update utc | 2026-10-21T17:24:05Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:24:05Z |
| Market best over 2 5 last update utc | 2026-10-21T17:24:01Z |
| Market best under 2 5 last update utc | 2026-10-21T17:24:01Z |
| Home probability edge | +2.3% |
| Draw probability edge | +1.1% |
| Away probability edge | -3.4% |
| Over 2.5 probability edge | +0.7% |
| Under 2.5 probability edge | -0.7% |
| Raw edge prob home | 0.0468 |
| Raw ev home | 0.1976 |
| Raw edge prob draw | 0.0213 |
| Raw ev draw | -0.0003 |
| Raw edge prob away | -0.0681 |
| Raw ev away | -0.1240 |

</details>


---

## 2026-10-27 — AS Roma vs Cagliari

The model's most likely 1X2 outcome is **AS Roma win** at **69.3%**. Expected goals are 1.92 for AS Roma and 0.71 for Cagliari (2.63 combined). The most likely exact score is 1-0 at 14.2%. Goal-market probabilities: at least one goal: 93.4%; Over 2.5 goals: 50.1%; Under 3.5 goals: 72.4%; Double Chance 1X: 88.2%; Double Chance X2: 30.7%; Double Chance 12 (either team wins): 81.1%; Under 4.5 goals: 86.9%; BTTS Yes (both teams score): 42.9%; BTTS No (at least one team does not score): 57.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AS Roma win | 69.3% | 1.44 |
| Draw | 18.9% | 5.29 |
| Cagliari win | 11.8% | 8.46 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| AS Roma expected goals | 1.92 |
| Cagliari expected goals | 0.71 |
| Expected total goals | 2.63 |
| Over 0.5 | 93.4% |
| Under 0.5 | 6.6% |
| Over 1.5 | 74.7% |
| Under 1.5 | 25.3% |
| Over 2.5 | 50.1% |
| Under 2.5 | 49.9% |
| Over 3.5 | 27.6% |
| Under 3.5 | 72.4% |
| Over 4.5 | 13.1% |
| Under 4.5 | 86.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 14.22% |
| 2 | 2-0 | 13.99% |
| 3 | 2-1 | 9.94% |
| 4 | 3-0 | 8.96% |
| 5 | 1-1 | 8.90% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AS Roma win | 69.3% | 72.8% | 1.34 | -7.2% |
| Draw | 18.9% | 16.3% | 4.80 | -9.2% |
| Cagliari win | 11.8% | 11.0% | 9.84 | +16.4% |
| Over 2.5 | 50.1% | 55.6% | 1.78 | -10.8% |
| Under 2.5 | 49.9% | 44.4% | 2.21 | +10.2% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-27T19:45:00+00:00 |
| Fixture id | 7eecf109ae6a5f87441a79b0e4111982 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T17:24:01Z |
| Market best draw last update utc | 2026-10-21T17:24:01Z |
| Market best away last update utc | 2026-10-21T17:24:01Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Roma |
| Matched away-team name | Cagliari |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.9213 |
| Dc lambda away | 0.7103 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T17:22:27.690536+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 42.9% |
| P btts no | 57.1% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.16 |
| Fair Over 1.5 odds | 1.34 |
| Fair Under 1.5 odds | 3.96 |
| Fair Over 2.5 odds | 1.99 |
| Fair Under 2.5 odds | 2.01 |
| Fair Over 3.5 odds | 3.63 |
| Fair Under 3.5 odds | 1.38 |
| Fair Over 4.5 odds | 7.61 |
| Fair Under 4.5 odds | 1.15 |
| Goal margin distribution | {"-1": 0.08549660266721773, "-10": 6.846740465292159e-10, "-11": 4.376295079805933e-11, "-12": 2.56811576305887e-12, "-13": 1.3928065636393208e-13, "-14": 7.020508513228709e-15, "-15": 3.2954150817637195e-16, "-16": 1.3479890539967395e-17, "-2": 0.026096070594024526, "-3": 0.005582751547194432, "-4": 0.0009305468967049828, "-5": 0.00012661169673195278, "-6": 1.452776848269368e-05, "-7": 1.4397186266430009e-06, "-8": 1.2548628992183785e-07, "-9": 9.757546533727351e-09, "0": 0.1891922222134146, "1": 0.26688370594124666, "10": 1.61999473673683e-05, "11": 2.800875357230365e-06, "12": 4.4458952796669246e-07, "13": 6.52218156249836e-08, "14": 8.892586477225285e-09, "15": 1.1290861993967054e-09, "16": 1.2492828758879313e-10, "2": 0.21544939471619706, "3": 0.12467400406912194, "4": 0.056211259887436076, "5": 0.02068789629069938, "6": 0.0064209436571377055, "7": 0.0017212145931482065, "8": 0.00040579914033006905, "9": 8.535184662787566e-05} |
| Raw goal margin distribution | {"-1": 0.09158971630776538, "-10": 7.334689300928845e-10, "-11": 4.688181896520948e-11, "-12": 2.7511384879185484e-12, "-13": 1.4920681530686407e-13, "-14": 7.520841331738896e-15, "-15": 3.530270479049114e-16, "-16": 1.444056619677519e-17, "-2": 0.027955867577070193, "-3": 0.005980619281616607, "-4": 0.000996864479071989, "-5": 0.0001356349728896398, "-6": 1.556312359093309e-05, "-7": 1.542323513023037e-06, "-8": 1.344293613535831e-07, "-9": 1.0452940713474442e-08, "0": 0.2158184929309181, "1": 0.2533755184962318, "10": 1.5379995003225242e-05, "11": 2.659110429311087e-06, "12": 4.220868477873831e-07, "13": 6.19206455222257e-08, "14": 8.442492588646685e-09, "15": 1.071938057027955e-09, "16": 1.1860510378863396e-10, "2": 0.20454452962345107, "3": 0.11836369070418015, "4": 0.053366154629316306, "5": 0.019640788600283406, "6": 0.006095950753623432, "7": 0.0016340961635110693, "8": 0.0003852598165325675, "9": 8.103180491172339e-05} |
| Unadjusted home-win probability | 65.8% |
| Unadjusted draw probability | 21.6% |
| Unadjusted away-win probability | 12.7% |
| Raw p over 1 5 | 74.2% |
| Raw p under 3 5 | 72.9% |
| Raw p btts yes | 43.7% |
| P home draw | 88.2% |
| P draw away | 30.7% |
| P home away | 81.1% |
| Raw p home draw | 87.3% |
| Raw p draw away | 34.2% |
| Raw p home away | 78.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:23:35Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.1, "price": 1.85, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:24:01Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.02, "price": 1.84, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:23:35Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.85, "price": 2.1, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:24:01Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.84, "price": 2.02, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 1.33 |
| Reference draw odds | 5.10 |
| Reference away odds | 7.25 |
| Market reference 1x2 last update utc | 2026-10-21T17:24:08Z |
| Market reference home last update utc | 2026-10-21T17:24:08Z |
| Market reference draw last update utc | 2026-10-21T17:24:08Z |
| Market reference away last update utc | 2026-10-21T17:24:08Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.73 |
| Reference Under 2.5 odds | 2.13 |
| Market reference over 2 5 last update utc | 2026-10-21T17:24:05Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:24:05Z |
| Market best over 2 5 last update utc | 2026-10-21T17:23:35Z |
| Market best under 2 5 last update utc | 2026-10-21T17:23:35Z |
| Home probability edge | -3.5% |
| Draw probability edge | +2.7% |
| Away probability edge | +0.8% |
| Over 2.5 probability edge | -5.4% |
| Under 2.5 probability edge | +5.4% |
| Raw edge prob home | -0.0701 |
| Raw ev home | -0.1189 |
| Raw edge prob draw | 0.0533 |
| Raw ev draw | 0.0359 |
| Raw edge prob away | 0.0169 |
| Raw ev away | 0.2465 |

</details>


---

## 2026-10-27 — Sassuolo vs Lazio

The model's most likely 1X2 outcome is **Lazio win** at **44.1%**. Expected goals are 1.17 for Sassuolo and 1.67 for Lazio (2.84 combined). The most likely exact score is 1-1 at 12.0%. Goal-market probabilities: at least one goal: 93.6%; Over 2.5 goals: 53.6%; Under 3.5 goals: 68.6%; Double Chance 1X: 55.9%; Double Chance X2: 69.6%; Double Chance 12 (either team wins): 74.5%; Under 4.5 goals: 84.3%; BTTS Yes (both teams score): 56.6%; BTTS No (at least one team does not score): 43.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Sassuolo win | 30.4% | 3.28 |
| Draw | 25.5% | 3.93 |
| Lazio win | 44.1% | 2.27 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Sassuolo expected goals | 1.17 |
| Lazio expected goals | 1.67 |
| Expected total goals | 2.84 |
| Over 0.5 | 93.6% |
| Under 0.5 | 6.4% |
| Over 1.5 | 77.7% |
| Under 1.5 | 22.3% |
| Over 2.5 | 53.6% |
| Under 2.5 | 46.4% |
| Over 3.5 | 31.4% |
| Under 3.5 | 68.6% |
| Over 4.5 | 15.7% |
| Under 4.5 | 84.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.03% |
| 2 | 1-2 | 8.63% |
| 3 | 0-1 | 8.49% |
| 4 | 2-1 | 7.72% |
| 5 | 1-0 | 7.47% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Sassuolo win | 30.4% | 34.6% | 2.95 | -10.2% |
| Draw | 25.5% | 26.0% | 3.25 | -17.2% |
| Lazio win | 44.1% | 39.4% | 2.48 | +9.3% |
| Over 2.5 | 53.6% | 54.6% | 1.82 | -2.4% |
| Under 2.5 | 46.4% | 45.4% | 2.15 | -0.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-27T17:30:00+00:00 |
| Fixture id | c7445242bf16a8f37afef7863af45a78 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T17:24:01Z |
| Market best draw last update utc | 2026-10-21T17:24:01Z |
| Market best away last update utc | 2026-10-21T17:24:01Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Sassuolo |
| Matched away-team name | Lazio |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.1681 |
| Dc lambda away | 1.6709 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T17:22:27.690536+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 56.6% |
| P btts no | 43.4% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.73 |
| Fair Over 1.5 odds | 1.29 |
| Fair Under 1.5 odds | 4.48 |
| Fair Over 2.5 odds | 1.86 |
| Fair Under 2.5 odds | 2.16 |
| Fair Over 3.5 odds | 3.19 |
| Fair Under 3.5 odds | 1.46 |
| Fair Over 4.5 odds | 6.39 |
| Fair Under 4.5 odds | 1.19 |
| Goal margin distribution | {"-1": 0.20430107725765723, "-10": 2.9496352791413743e-06, "-11": 4.416024188155948e-07, "-12": 6.073719429346381e-08, "-13": 7.722106608047156e-09, "-14": 9.069019738426339e-10, "-15": 8.939178533937462e-11, "-2": 0.13528352224183857, "-3": 0.06557979751569744, "-4": 0.025089514916363735, "-5": 0.00789303309066064, "-6": 0.0021035470872307204, "-7": 0.0004856314933287461, "-8": 9.880821871540387e-05, "-9": 1.7961578743940826e-05, "0": 0.254645568533363, "1": 0.18146670831939657, "10": 1.0525787654736609e-07, "11": 1.1016605866791824e-08, "12": 1.0592565990320348e-09, "13": 9.414826660903057e-11, "14": 7.729777018871067e-12, "15": 5.326406568250869e-13, "2": 0.0846234097440921, "3": 0.028677796140744748, "4": 0.007670047435402589, "5": 0.0016868629209122958, "6": 0.00031428104599678464, "7": 5.072276016176122e-05, "8": 7.214715144008672e-06, "9": 9.168551074096846e-07} |
| Raw goal margin distribution | {"-1": 0.22584022917253202, "-10": 3.2606108414032186e-06, "-11": 4.881598903302917e-07, "-12": 6.714062433079198e-08, "-13": 8.536236565491384e-09, "-14": 1.0025152699089138e-09, "-15": 9.88162253384765e-11, "-2": 0.14954625827955126, "-3": 0.07249377584707893, "-4": 0.027734664322857237, "-5": 0.008725183567255846, "-6": 0.002325320857981882, "-7": 0.0005368308832187145, "-8": 0.00010922541896670353, "-9": 1.9855240678521877e-05, "0": 0.24968057313031, "1": 0.1567264003828966, "10": 9.090751827701885e-08, "11": 9.51465421911128e-09, "12": 9.148425922617301e-10, "13": 8.13125397191405e-11, "14": 6.675935983793944e-12, "15": 4.600229629715211e-13, "2": 0.07308625653789338, "3": 0.024768001809690805, "4": 0.006624349647655042, "5": 0.0014568840531820253, "6": 0.00027143346294105194, "7": 4.380746028437278e-05, "8": 6.231095195258955e-06, "9": 7.918554427299027e-07} |
| Unadjusted home-win probability | 26.3% |
| Unadjusted draw probability | 25.0% |
| Unadjusted away-win probability | 48.7% |
| Raw p over 1 5 | 77.9% |
| Raw p under 3 5 | 68.3% |
| Raw p btts yes | 56.3% |
| P home draw | 55.9% |
| P draw away | 69.6% |
| P home away | 74.5% |
| Raw p home draw | 51.3% |
| Raw p draw away | 73.7% |
| Raw p home away | 75.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:23:35Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.13, "price": 1.83, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:24:01Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.11, "price": 1.77, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:23:35Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.83, "price": 2.13, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:24:01Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.77, "price": 2.11, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 2.65 |
| Reference draw odds | 3.45 |
| Reference away odds | 2.35 |
| Market reference 1x2 last update utc | 2026-10-21T17:24:08Z |
| Market reference home last update utc | 2026-10-21T17:24:08Z |
| Market reference draw last update utc | 2026-10-21T17:24:08Z |
| Market reference away last update utc | 2026-10-21T17:24:08Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.76 |
| Reference Under 2.5 odds | 2.09 |
| Market reference over 2 5 last update utc | 2026-10-21T17:24:05Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:24:05Z |
| Market best over 2 5 last update utc | 2026-10-21T17:23:35Z |
| Market best under 2 5 last update utc | 2026-10-21T17:23:35Z |
| Home probability edge | -4.2% |
| Draw probability edge | -0.5% |
| Away probability edge | +4.6% |
| Over 2.5 probability edge | -0.9% |
| Under 2.5 probability edge | +0.9% |
| Raw edge prob home | -0.0830 |
| Raw ev home | -0.2242 |
| Raw edge prob draw | -0.0099 |
| Raw ev draw | -0.1885 |
| Raw edge prob away | 0.0930 |
| Raw ev away | 0.2086 |

</details>


---

## 2026-10-27 — Torino vs Como

The model's most likely 1X2 outcome is **Como win** at **52.4%**. Expected goals are 0.94 for Torino and 1.48 for Como (2.41 combined). The most likely exact score is 0-1 at 13.6%. Goal-market probabilities: at least one goal: 91.2%; Over 2.5 goals: 44.1%; Under 3.5 goals: 77.4%; Double Chance 1X: 47.6%; Double Chance X2: 77.8%; Double Chance 12 (either team wins): 74.6%; Under 4.5 goals: 90.0%; BTTS Yes (both teams score): 46.8%; BTTS No (at least one team does not score): 53.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Torino win | 22.2% | 4.50 |
| Draw | 25.4% | 3.93 |
| Como win | 52.4% | 1.91 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Torino expected goals | 0.94 |
| Como expected goals | 1.48 |
| Expected total goals | 2.41 |
| Over 0.5 | 91.2% |
| Under 0.5 | 8.8% |
| Over 1.5 | 70.1% |
| Under 1.5 | 29.9% |
| Over 2.5 | 44.1% |
| Under 2.5 | 55.9% |
| Over 3.5 | 22.6% |
| Under 3.5 | 77.4% |
| Over 4.5 | 10.0% |
| Under 4.5 | 90.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 13.59% |
| 2 | 1-1 | 11.97% |
| 3 | 0-2 | 10.37% |
| 4 | 1-2 | 9.70% |
| 5 | 0-0 | 8.76% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Torino win | 22.2% | 20.9% | 4.89 | +8.6% |
| Draw | 25.4% | 23.7% | 3.55 | -9.8% |
| Como win | 52.4% | 55.4% | 1.76 | -7.8% |
| Over 2.5 | 44.1% | 54.6% | 1.82 | -19.8% |
| Under 2.5 | 55.9% | 45.4% | 2.15 | +20.2% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-27T19:45:00+00:00 |
| Fixture id | 7d989a0a7bae47eb957731e97c5bd9c1 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T17:24:01Z |
| Market best draw last update utc | 2026-10-21T17:24:01Z |
| Market best away last update utc | 2026-10-21T17:24:01Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Torino |
| Matched away-team name | Como |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.9359 |
| Dc lambda away | 1.4781 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T17:22:27.690536+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 46.8% |
| P btts no | 53.2% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 11.41 |
| Fair Over 1.5 odds | 1.43 |
| Fair Under 1.5 odds | 3.35 |
| Fair Over 2.5 odds | 2.27 |
| Fair Under 2.5 odds | 1.79 |
| Fair Over 3.5 odds | 4.42 |
| Fair Under 3.5 odds | 1.29 |
| Fair Over 4.5 odds | 10.02 |
| Fair Under 4.5 odds | 1.11 |
| Goal margin distribution | {"-1": 0.25800895333324214, "-10": 1.4755153811854643e-06, "-11": 1.962343853883315e-07, "-12": 2.396069501509163e-08, "-13": 2.7036469626428127e-09, "-14": 2.8256987449366315e-10, "-15": 2.549385255698824e-11, "-2": 0.1605446801559509, "-3": 0.07138384887337747, "-4": 0.024740573334028494, "-5": 0.007001175237454401, "-6": 0.001671037698676884, "-7": 0.00034450640021587987, "-8": 6.247081590025672e-05, "-9": 1.010656094393857e-05, "0": 0.25418243007428726, "1": 0.1442157949471187, "10": 1.3621706289195832e-08, "11": 1.147022822795256e-09, "12": 8.867588679242777e-11, "13": 6.335272350595633e-12, "14": 4.1922806256280556e-13, "15": 2.3947993754468425e-14, "2": 0.05738656856417074, "3": 0.0161556143373693, "4": 0.0035452139990842396, "5": 0.0006352034132102673, "6": 9.599249986819265e-05, "7": 1.2530186292474003e-05, "8": 1.4386216459163373e-06, "9": 1.473608068566955e-07} |
| Raw goal margin distribution | {"-1": 0.24321744511411839, "-10": 1.3909249140474527e-06, "-11": 1.8498437841435947e-07, "-12": 2.2587041842700025e-08, "-13": 2.548648402504133e-09, "-14": 2.663703024747363e-10, "-15": 2.403230432479658e-11, "-2": 0.15134074391503985, "-3": 0.06729145295578505, "-4": 0.02332221017612886, "-5": 0.00659980179777156, "-6": 0.0015752380470170431, "-7": 0.00032475604200349545, "-8": 5.888939915131724e-05, "-9": 9.527157487825712e-06, "0": 0.27150495818817677, "1": 0.1524673296710308, "10": 1.4401093751473776e-08, "11": 1.2126515471307925e-09, "12": 9.374961785849945e-11, "13": 6.697754974676778e-12, "14": 4.4321485899341737e-13, "15": 2.5318216080708664e-14, "2": 0.06067003181704849, "3": 0.017079983354922588, "4": 0.003748059023291675, "5": 0.0006715475808014381, "6": 0.00010148486251950949, "7": 1.3247120712364343e-05, "8": 1.520934657956406e-06, "9": 1.5579228840951434e-07} |
| Unadjusted home-win probability | 23.5% |
| Unadjusted draw probability | 27.2% |
| Unadjusted away-win probability | 49.4% |
| Raw p over 1 5 | 69.9% |
| Raw p under 3 5 | 77.6% |
| Raw p btts yes | 47.3% |
| P home draw | 47.6% |
| P draw away | 77.8% |
| P home away | 74.6% |
| Raw p home draw | 50.6% |
| Raw p draw away | 76.5% |
| Raw p home away | 72.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:23:35Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.4, "price": 3.35, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:24:01Z", "line": -0.75, "market_key": "spreads", "opposite_price": 1.87, "price": 1.99, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:24:01Z", "line": 0.75, "market_key": "spreads", "opposite_price": 1.99, "price": 1.87, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:23:35Z", "line": 1.5, "market_key": "spreads", "opposite_price": 3.35, "price": 1.4, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 4.20 |
| Reference draw odds | 3.75 |
| Reference away odds | 1.72 |
| Market reference 1x2 last update utc | 2026-10-21T17:24:08Z |
| Market reference home last update utc | 2026-10-21T17:24:08Z |
| Market reference draw last update utc | 2026-10-21T17:24:08Z |
| Market reference away last update utc | 2026-10-21T17:24:08Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.76 |
| Reference Under 2.5 odds | 2.09 |
| Market reference over 2 5 last update utc | 2026-10-21T17:24:05Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:24:05Z |
| Market best over 2 5 last update utc | 2026-10-21T17:23:35Z |
| Market best under 2 5 last update utc | 2026-10-21T17:23:35Z |
| Home probability edge | +1.3% |
| Draw probability edge | +1.7% |
| Away probability edge | -3.0% |
| Over 2.5 probability edge | -10.5% |
| Under 2.5 probability edge | +10.5% |
| Raw edge prob home | 0.0254 |
| Raw ev home | 0.1479 |
| Raw edge prob draw | 0.0346 |
| Raw ev draw | -0.0362 |
| Raw edge prob away | -0.0601 |
| Raw ev away | -0.1310 |

</details>


---

## 2026-10-28 — AC Milan vs Bologna

The model's most likely 1X2 outcome is **AC Milan win** at **55.4%**. Expected goals are 1.62 for AC Milan and 1.04 for Bologna (2.66 combined). The most likely exact score is 1-0 at 12.0%. Goal-market probabilities: at least one goal: 93.1%; Over 2.5 goals: 50.5%; Under 3.5 goals: 71.9%; Double Chance 1X: 79.2%; Double Chance X2: 44.6%; Double Chance 12 (either team wins): 76.3%; Under 4.5 goals: 86.5%; BTTS Yes (both teams score): 51.7%; BTTS No (at least one team does not score): 48.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AC Milan win | 55.4% | 1.80 |
| Draw | 23.7% | 4.21 |
| Bologna win | 20.8% | 4.81 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| AC Milan expected goals | 1.62 |
| Bologna expected goals | 1.04 |
| Expected total goals | 2.66 |
| Over 0.5 | 93.1% |
| Under 0.5 | 6.9% |
| Over 1.5 | 75.2% |
| Under 1.5 | 24.8% |
| Over 2.5 | 50.5% |
| Under 2.5 | 49.5% |
| Over 3.5 | 28.1% |
| Under 3.5 | 71.9% |
| Over 4.5 | 13.5% |
| Under 4.5 | 86.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 12.03% |
| 2 | 1-1 | 11.31% |
| 3 | 2-1 | 10.51% |
| 4 | 2-0 | 10.07% |
| 5 | 0-0 | 6.86% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AC Milan win | 55.4% | 60.6% | 1.60 | -11.3% |
| Draw | 23.7% | 21.9% | 4.07 | -3.3% |
| Bologna win | 20.8% | 17.5% | 5.39 | +12.1% |
| Over 2.5 | 50.5% | 52.5% | 1.83 | -7.6% |
| Under 2.5 | 49.5% | 47.5% | 2.01 | -0.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-28T17:30:00+00:00 |
| Fixture id | 3d0b0fbec194258530882514714c74be |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T17:24:01Z |
| Market best draw last update utc | 2026-10-21T17:24:01Z |
| Market best away last update utc | 2026-10-21T17:24:01Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Milan |
| Matched away-team name | Bologna |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.6165 |
| Dc lambda away | 1.0433 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T17:22:27.690536+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 51.7% |
| P btts no | 48.3% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 14.58 |
| Fair Over 1.5 odds | 1.33 |
| Fair Under 1.5 odds | 4.02 |
| Fair Over 2.5 odds | 1.98 |
| Fair Under 2.5 odds | 2.02 |
| Fair Over 3.5 odds | 3.56 |
| Fair Under 3.5 odds | 1.39 |
| Fair Over 4.5 odds | 7.43 |
| Fair Under 4.5 odds | 1.16 |
| Goal margin distribution | {"-1": 0.13003313095741917, "-10": 2.963373450547543e-08, "-11": 2.7755180083928253e-09, "-12": 2.3874717350727117e-10, "-13": 1.898171981908428e-11, "-14": 1.3959586778778014e-12, "-15": 8.727992276007965e-14, "-2": 0.05575301487254507, "-3": 0.017156362313732382, "-4": 0.004143329489468362, "-5": 0.0008201655681428139, "-6": 0.0001372582026424376, "-7": 1.9872193907434494e-05, "-8": 2.5333003899483986e-06, "-9": 2.8834106806506093e-07, "0": 0.2374710917752688, "1": 0.25941782767541605, "10": 3.014086247612595e-06, "11": 4.373972348693036e-07, "12": 5.8295216065966684e-08, "13": 7.18113233659603e-09, "14": 8.182624618343692e-10, "15": 7.926785613391606e-11, "2": 0.17074032184015434, "3": 0.08140585495760239, "4": 0.030460890642101883, "5": 0.009342376238093095, "6": 0.0024224611557929353, "7": 0.0005434092469848792, "8": 0.00010733233858513884, "9": 1.892836485893339e-05} |
| Raw goal margin distribution | {"-1": 0.1505241556356169, "-10": 3.4303510435562794e-08, "-11": 3.2128927573203376e-09, "-12": 2.763696946921947e-10, "-13": 2.1972918188174216e-11, "-14": 1.6159381823896566e-12, "-15": 1.0103376409282147e-13, "-2": 0.06453874813318115, "-3": 0.01985991517730152, "-4": 0.004796248220206318, "-5": 0.0009494098059249971, "-6": 0.00015888777655889008, "-7": 2.3003715949309444e-05, "-8": 2.9325057341980805e-06, "-9": 3.337787492002927e-07, "0": 0.25601386733578296, "1": 0.23540172849996585, "10": 2.7350514761989863e-06, "11": 3.969043533051567e-07, "12": 5.289842547898257e-08, "13": 6.5163253418990105e-09, "14": 7.425102569413801e-10, "15": 7.192948347311587e-11, "2": 0.15493371155702448, "3": 0.07386955298621181, "4": 0.027640915711355872, "5": 0.00847748797548247, "6": 0.002198197203359445, "7": 0.0004931021016148452, "8": 9.739584304320978e-05, "9": 1.7176035453685157e-05} |
| Unadjusted home-win probability | 50.3% |
| Unadjusted draw probability | 25.6% |
| Unadjusted away-win probability | 24.1% |
| Raw p over 1 5 | 74.8% |
| Raw p under 3 5 | 72.3% |
| Raw p btts yes | 52.3% |
| P home draw | 79.2% |
| P draw away | 44.6% |
| P home away | 76.3% |
| Raw p home draw | 75.9% |
| Raw p draw away | 49.7% |
| Raw p home away | 74.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:24:01Z", "line": 1.0, "market_key": "spreads", "opposite_price": 2.06, "price": 1.81, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:23:35Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.76, "price": 1.53, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:23:35Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.53, "price": 2.76, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:24:01Z", "line": -1.0, "market_key": "spreads", "opposite_price": 1.81, "price": 2.06, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 1.58 |
| Reference draw odds | 4.00 |
| Reference away odds | 4.90 |
| Market reference 1x2 last update utc | 2026-10-21T17:24:07Z |
| Market reference home last update utc | 2026-10-21T17:24:07Z |
| Market reference draw last update utc | 2026-10-21T17:24:07Z |
| Market reference away last update utc | 2026-10-21T17:24:07Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.82 |
| Reference Under 2.5 odds | 2.00 |
| Market reference over 2 5 last update utc | 2026-10-21T17:24:05Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:24:05Z |
| Market best over 2 5 last update utc | 2026-10-21T17:24:01Z |
| Market best under 2 5 last update utc | 2026-10-21T17:24:01Z |
| Home probability edge | -5.1% |
| Draw probability edge | +1.9% |
| Away probability edge | +3.3% |
| Over 2.5 probability edge | -2.1% |
| Under 2.5 probability edge | +2.1% |
| Raw edge prob home | -0.1027 |
| Raw ev home | -0.1950 |
| Raw edge prob draw | 0.0371 |
| Raw ev draw | 0.0420 |
| Raw edge prob away | 0.0656 |
| Raw ev away | 0.2982 |

</details>


---

## 2026-10-28 — Genoa vs Juventus

The model's most likely 1X2 outcome is **Juventus win** at **55.5%**. Expected goals are 0.78 for Genoa and 1.43 for Juventus (2.21 combined). The most likely exact score is 0-1 at 16.2%. Goal-market probabilities: at least one goal: 89.6%; Over 2.5 goals: 39.0%; Under 3.5 goals: 81.4%; Double Chance 1X: 44.5%; Double Chance X2: 81.2%; Double Chance 12 (either team wins): 74.3%; Under 4.5 goals: 92.4%; BTTS Yes (both teams score): 41.1%; BTTS No (at least one team does not score): 58.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Genoa win | 18.8% | 5.32 |
| Draw | 25.7% | 3.89 |
| Juventus win | 55.5% | 1.80 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Genoa expected goals | 0.78 |
| Juventus expected goals | 1.43 |
| Expected total goals | 2.21 |
| Over 0.5 | 89.6% |
| Under 0.5 | 10.4% |
| Over 1.5 | 65.7% |
| Under 1.5 | 34.3% |
| Over 2.5 | 39.0% |
| Under 2.5 | 61.0% |
| Over 3.5 | 18.6% |
| Under 3.5 | 81.4% |
| Over 4.5 | 7.6% |
| Under 4.5 | 92.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 16.23% |
| 2 | 0-2 | 11.94% |
| 3 | 1-1 | 11.66% |
| 4 | 0-0 | 10.44% |
| 5 | 1-2 | 9.34% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Genoa win | 18.8% | 17.5% | 5.59 | +5.1% |
| Draw | 25.7% | 23.5% | 3.88 | -0.3% |
| Juventus win | 55.5% | 59.0% | 1.62 | -10.1% |
| Over 2.5 | 39.0% | 46.1% | 2.05 | -20.1% |
| Under 2.5 | 61.0% | 53.9% | 1.80 | +9.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-28T19:45:00+00:00 |
| Fixture id | 34848497b90b1392f6a767fc183d3ac1 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T17:24:01Z |
| Market best draw last update utc | 2026-10-21T17:24:01Z |
| Market best away last update utc | 2026-10-21T17:24:01Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Genoa |
| Matched away-team name | Juventus |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.7826 |
| Dc lambda away | 1.4324 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T17:22:27.690536+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 41.1% |
| P btts no | 58.9% |
| Fair Over 0.5 odds | 1.12 |
| Fair Under 0.5 odds | 9.58 |
| Fair Over 1.5 odds | 1.52 |
| Fair Under 1.5 odds | 2.92 |
| Fair Over 2.5 odds | 2.57 |
| Fair Under 2.5 odds | 1.64 |
| Fair Over 3.5 odds | 5.37 |
| Fair Under 3.5 odds | 1.23 |
| Fair Over 4.5 odds | 13.09 |
| Fair Under 4.5 odds | 1.08 |
| Goal margin distribution | {"-1": 0.27493157694735054, "-10": 1.2907255227709404e-06, "-11": 1.6667044568909312e-07, "-12": 1.9752286404490653e-08, "-13": 2.1572039306393973e-09, "-14": 2.0435076549059526e-10, "-2": 0.170745220591433, "-3": 0.07488849106771861, "-4": 0.025441723778801547, "-5": 0.007032481469278157, "-6": 0.0016360674439911012, "-7": 0.0003283140714140903, "-8": 5.789431785083553e-05, "-9": 9.101979189128055e-06, "0": 0.2568536344298231, "1": 0.13022796944055226, "10": 2.6871703399449757e-09, "11": 1.8957684068827126e-10, "12": 1.2274659232386636e-11, "13": 7.324005439908228e-13, "14": 3.790522766659562e-14, "2": 0.044780276732939495, "3": 0.010730468462029037, "4": 0.0019916614659544604, "5": 0.0003007758546008179, "6": 3.822970624937718e-05, "7": 4.191356872639629e-06, "8": 4.038001444644786e-07, "9": 3.468420562828454e-08} |
| Raw goal margin distribution | {"-1": 0.257864565221629, "-10": 1.2106007590882358e-06, "-11": 1.5632399337360762e-07, "-12": 1.8526117670370274e-08, "-13": 2.0232905213912274e-09, "-14": 1.9166522041966272e-10, "-2": 0.16014581722605323, "-3": 0.07023961526608923, "-4": 0.02386237009787268, "-5": 0.006595923962753273, "-6": 0.0015345047840714856, "-7": 0.0003079332182259652, "-8": 5.430039454604875e-05, "-9": 8.536952838670425e-06, "0": 0.2786198654243497, "1": 0.1390157049723226, "10": 2.8684996072114318e-09, "11": 2.023694162469155e-10, "12": 1.3102948727647919e-11, "13": 7.818226636135518e-13, "14": 4.046305850306307e-14, "2": 0.0478020333544938, "3": 0.011454556531446097, "4": 0.002126058049935718, "5": 0.00032107209876348794, "6": 4.0809432781396496e-05, "7": 4.4741880944904665e-06, "8": 4.3104842985576957e-07, "9": 3.702468308101823e-08} |
| Unadjusted home-win probability | 20.1% |
| Unadjusted draw probability | 27.9% |
| Unadjusted away-win probability | 52.1% |
| Raw p over 1 5 | 65.3% |
| Raw p under 3 5 | 81.6% |
| Raw p btts yes | 41.7% |
| P home draw | 44.5% |
| P draw away | 81.2% |
| P home away | 74.3% |
| Raw p home draw | 47.9% |
| Raw p draw away | 79.9% |
| Raw p home away | 72.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:23:35Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.45, "price": 3.06, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:24:01Z", "line": -0.75, "market_key": "spreads", "opposite_price": 2.05, "price": 1.81, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:24:01Z", "line": 0.75, "market_key": "spreads", "opposite_price": 1.81, "price": 2.05, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:23:35Z", "line": 1.5, "market_key": "spreads", "opposite_price": 3.06, "price": 1.45, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 4.90 |
| Reference draw odds | 3.75 |
| Reference away odds | 1.62 |
| Market reference 1x2 last update utc | 2026-10-21T17:24:07Z |
| Market reference home last update utc | 2026-10-21T17:24:07Z |
| Market reference draw last update utc | 2026-10-21T17:24:07Z |
| Market reference away last update utc | 2026-10-21T17:24:07Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 2.06 |
| Reference Under 2.5 odds | 1.78 |
| Market reference over 2 5 last update utc | 2026-10-21T17:24:05Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:24:05Z |
| Market best over 2 5 last update utc | 2026-10-21T17:24:01Z |
| Market best under 2 5 last update utc | 2026-10-21T17:24:01Z |
| Home probability edge | +1.3% |
| Draw probability edge | +2.2% |
| Away probability edge | -3.4% |
| Over 2.5 probability edge | -7.1% |
| Under 2.5 probability edge | +7.1% |
| Raw edge prob home | 0.0254 |
| Raw ev home | 0.1223 |
| Raw edge prob draw | 0.0435 |
| Raw ev draw | 0.0810 |
| Raw edge prob away | -0.0689 |
| Raw ev away | -0.1566 |

</details>


---

## 2026-10-28 — Monza vs Napoli

The model's most likely 1X2 outcome is **Napoli win** at **56.5%**. Expected goals are 0.81 for Monza and 1.88 for Napoli (2.69 combined). The most likely exact score is 0-1 at 11.2%. Goal-market probabilities: at least one goal: 92.6%; Over 2.5 goals: 49.7%; Under 3.5 goals: 72.3%; Double Chance 1X: 43.5%; Double Chance X2: 80.0%; Double Chance 12 (either team wins): 76.5%; Under 4.5 goals: 86.8%; BTTS Yes (both teams score): 48.1%; BTTS No (at least one team does not score): 51.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Monza win | 20.0% | 4.99 |
| Draw | 23.5% | 4.26 |
| Napoli win | 56.5% | 1.77 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Monza expected goals | 0.81 |
| Napoli expected goals | 1.88 |
| Expected total goals | 2.69 |
| Over 0.5 | 92.6% |
| Under 0.5 | 7.4% |
| Over 1.5 | 74.6% |
| Under 1.5 | 25.4% |
| Over 2.5 | 49.7% |
| Under 2.5 | 50.3% |
| Over 3.5 | 27.7% |
| Under 3.5 | 72.3% |
| Over 4.5 | 13.2% |
| Under 4.5 | 86.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 11.24% |
| 2 | 1-1 | 11.15% |
| 3 | 0-2 | 10.85% |
| 4 | 1-2 | 8.84% |
| 5 | 0-0 | 7.41% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Monza win | 20.0% | 24.8% | 3.72 | -25.4% |
| Draw | 23.5% | 24.4% | 3.86 | -9.5% |
| Napoli win | 56.5% | 50.8% | 1.91 | +7.9% |
| Over 2.5 | 49.7% | 55.6% | 1.80 | -10.6% |
| Under 2.5 | 50.3% | 44.4% | 2.17 | +9.2% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-28T19:45:00+00:00 |
| Fixture id | abec89862e33762414fcb8b2232aba08 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T17:24:01Z |
| Market best draw last update utc | 2026-10-21T17:24:01Z |
| Market best away last update utc | 2026-10-21T17:24:01Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Monza |
| Matched away-team name | Napoli |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.8150 |
| Dc lambda away | 1.8784 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T17:22:27.690536+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 48.1% |
| P btts no | 51.9% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.50 |
| Fair Over 1.5 odds | 1.34 |
| Fair Under 1.5 odds | 3.94 |
| Fair Over 2.5 odds | 2.01 |
| Fair Under 2.5 odds | 1.99 |
| Fair Over 3.5 odds | 3.61 |
| Fair Under 3.5 odds | 1.38 |
| Fair Over 4.5 odds | 7.58 |
| Fair Under 4.5 odds | 1.15 |
| Goal margin distribution | {"-1": 0.22645725870129935, "-10": 1.064520243267954e-05, "-11": 1.7971965239960662e-06, "-12": 2.786135657147355e-07, "-13": 3.992452573809579e-08, "-14": 5.3175798847606854e-09, "-15": 6.591376015798199e-10, "-16": 7.062632292822406e-11, "-2": 0.1756186058543087, "-3": 0.09827710426700972, "-4": 0.043013763734898854, "-5": 0.015400691990823202, "-6": 0.004656219739143963, "-7": 0.0012168956888255742, "-8": 0.00027987845270107124, "-9": 5.745059744154948e-05, "0": 0.23457454270630643, "1": 0.13875337127632906, "10": 3.6188607237683403e-09, "11": 2.650727377450096e-10, "12": 1.78288487734405e-11, "13": 1.1084404291971941e-12, "14": 6.405280660887449e-14, "15": 3.444702955146959e-15, "16": 1.601377916711926e-16, "2": 0.047552798083942235, "3": 0.011545412443491714, "4": 0.0021923813298557753, "5": 0.00034056532992936446, "6": 4.467301000349712e-05, "7": 5.065433866257517e-06, "8": 5.054571107110316e-07, "9": 4.501538250385569e-08} |
| Raw goal margin distribution | {"-1": 0.2491009522625095, "-10": 1.1709627142070677e-05, "-11": 1.9769000477074275e-06, "-12": 3.064724219078241e-07, "-13": 4.391662001484638e-08, "-14": 5.849290151361581e-09, "-15": 7.250454463998048e-10, "-16": 7.768832139501288e-11, "-2": 0.19317889037518238, "-3": 0.1081039327196165, "-4": 0.04731475408739646, "-5": 0.016940622978554372, "-6": 0.005121799926467093, "-7": 0.0013385743368483762, "-8": 0.00030786378624124243, "-9": 6.319514160337203e-05, "0": 0.22524441632615277, "1": 0.10610362769440945, "10": 2.7673147497652332e-09, "11": 2.0269906827433175e-10, "12": 1.3633582485788426e-11, "13": 8.476158059377858e-13, "14": 4.898068481287737e-14, "15": 2.6341376538005412e-15, "16": 1.2245612824388196e-16, "2": 0.03636325616678393, "3": 0.008828687420091751, "4": 0.0016764970122702574, "5": 0.00026042766845992715, "6": 3.4161104539651004e-05, "7": 3.873498021072804e-06, "8": 3.8651913533379094e-07, "9": 3.4422914137332816e-08} |
| Unadjusted home-win probability | 15.3% |
| Unadjusted draw probability | 22.5% |
| Unadjusted away-win probability | 62.1% |
| Raw p over 1 5 | 75.4% |
| Raw p under 3 5 | 71.6% |
| Raw p btts yes | 47.6% |
| P home draw | 43.5% |
| P draw away | 80.0% |
| P home away | 76.5% |
| Raw p home draw | 37.9% |
| Raw p draw away | 84.7% |
| Raw p home away | 77.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:24:01Z", "line": -0.5, "market_key": "spreads", "opposite_price": 1.93, "price": 1.92, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:23:35Z", "line": -0.0, "market_key": "spreads", "opposite_price": 3.04, "price": 1.46, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:23:35Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.46, "price": 3.04, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:24:01Z", "line": 0.5, "market_key": "spreads", "opposite_price": 1.92, "price": 1.93, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 3.60 |
| Reference draw odds | 3.65 |
| Reference away odds | 1.86 |
| Market reference 1x2 last update utc | 2026-10-21T17:24:07Z |
| Market reference home last update utc | 2026-10-21T17:24:07Z |
| Market reference draw last update utc | 2026-10-21T17:24:07Z |
| Market reference away last update utc | 2026-10-21T17:24:07Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.73 |
| Reference Under 2.5 odds | 2.13 |
| Market reference over 2 5 last update utc | 2026-10-21T17:24:05Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:24:05Z |
| Market best over 2 5 last update utc | 2026-10-21T17:23:35Z |
| Market best under 2 5 last update utc | 2026-10-21T17:23:35Z |
| Home probability edge | -4.7% |
| Draw probability edge | -0.9% |
| Away probability edge | +5.6% |
| Over 2.5 probability edge | -5.9% |
| Under 2.5 probability edge | +5.9% |
| Raw edge prob home | -0.0943 |
| Raw ev home | -0.4298 |
| Raw edge prob draw | -0.0187 |
| Raw ev draw | -0.1306 |
| Raw edge prob away | 0.1130 |
| Raw ev away | 0.1870 |

</details>


---

## 2026-10-28 — Parma vs Udinese

The model's most likely 1X2 outcome is **Udinese win** at **38.8%**. Expected goals are 1.05 for Parma and 1.17 for Udinese (2.22 combined). The most likely exact score is 1-1 at 13.4%. Goal-market probabilities: at least one goal: 88.9%; Over 2.5 goals: 38.4%; Under 3.5 goals: 81.6%; Double Chance 1X: 61.2%; Double Chance X2: 67.9%; Double Chance 12 (either team wins): 70.9%; Under 4.5 goals: 92.5%; BTTS Yes (both teams score): 45.0%; BTTS No (at least one team does not score): 55.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Parma win | 32.1% | 3.12 |
| Draw | 29.1% | 3.44 |
| Udinese win | 38.8% | 2.57 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Parma expected goals | 1.05 |
| Udinese expected goals | 1.17 |
| Expected total goals | 2.22 |
| Over 0.5 | 88.9% |
| Under 0.5 | 11.1% |
| Over 1.5 | 65.4% |
| Under 1.5 | 34.6% |
| Over 2.5 | 38.4% |
| Under 2.5 | 61.6% |
| Over 3.5 | 18.4% |
| Under 3.5 | 81.6% |
| Over 4.5 | 7.5% |
| Under 4.5 | 92.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.45% |
| 2 | 0-1 | 12.53% |
| 3 | 0-0 | 11.06% |
| 4 | 1-0 | 10.98% |
| 5 | 1-2 | 7.95% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Parma win | 32.1% | 32.1% | 3.00 | -3.7% |
| Draw | 29.1% | 28.3% | 3.26 | -5.2% |
| Udinese win | 38.8% | 39.6% | 2.45 | -4.8% |
| Over 2.5 | 38.4% | 43.4% | 2.22 | -14.7% |
| Under 2.5 | 61.6% | 56.6% | 1.77 | +9.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-28T17:30:00+00:00 |
| Fixture id | 482c18a8081afdfa310324fa8f37e95a |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T17:24:01Z |
| Market best draw last update utc | 2026-10-21T17:24:01Z |
| Market best away last update utc | 2026-10-21T17:24:01Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Parma |
| Matched away-team name | Udinese |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.0479 |
| Dc lambda away | 1.1681 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T17:22:27.690536+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 45.0% |
| P btts no | 55.0% |
| Fair Over 0.5 odds | 1.12 |
| Fair Under 0.5 odds | 9.04 |
| Fair Over 1.5 odds | 1.53 |
| Fair Under 1.5 odds | 2.89 |
| Fair Over 2.5 odds | 2.60 |
| Fair Under 2.5 odds | 1.62 |
| Fair Over 3.5 odds | 5.43 |
| Fair Under 3.5 odds | 1.23 |
| Fair Over 4.5 odds | 13.36 |
| Fair Under 4.5 odds | 1.08 |
| Goal margin distribution | {"-1": 0.22272501375664025, "-10": 1.6179639082892557e-07, "-11": 1.7021822080329827e-08, "-12": 1.6379305773098259e-09, "-13": 1.345045798552979e-10, "-2": 0.11192413612169355, "-3": 0.039748857311267614, "-4": 0.010961926661907689, "-5": 0.0024631146531653787, "-6": 0.00046620719205893923, "-7": 7.615638012599431e-05, "-8": 1.0935884582846276e-05, "-9": 1.4004592300126317e-06, "0": 0.2907505598222002, "1": 0.1956454994183435, "10": 5.36126008166652e-08, "11": 5.0599412883407005e-09, "12": 4.3679363985787484e-10, "13": 3.2178016668458215e-11, "2": 0.08840782790711961, "3": 0.02816650764518534, "4": 0.00696845710291326, "5": 0.0014046746705189746, "6": 0.00023851268252209805, "7": 3.4952656217920443e-05, "8": 4.502660424233935e-06, "9": 5.172817206923917e-07} |
| Raw goal margin distribution | {"-1": 0.2184734281876721, "-10": 1.5870786840049723e-07, "-11": 1.6696893452450837e-08, "-12": 1.6066642103759747e-09, "-13": 1.3193702930932398e-10, "-2": 0.10978762242739355, "-3": 0.03899009355466409, "-4": 0.010752675045226784, "-5": 0.0024160963926768897, "-6": 0.0004573077885457232, "-7": 7.470263516368704e-05, "-8": 1.0727130081983914e-05, "-9": 1.3737259405997247e-06, "0": 0.29835231558477393, "1": 0.19553085110907747, "10": 5.358118381981499e-08, "11": 5.056976161540349e-09, "12": 4.365376786808648e-10, "13": 3.215916034302503e-11, "2": 0.08835602089890546, "3": 0.02815000206499542, "4": 0.006964373585390921, "5": 0.0014038515308274283, "6": 0.00023837291403332143, "7": 3.493217395305029e-05, "8": 4.500021864152706e-06, "9": 5.169785934808387e-07} |
| Unadjusted home-win probability | 32.1% |
| Unadjusted draw probability | 29.8% |
| Unadjusted away-win probability | 38.1% |
| Raw p over 1 5 | 65.4% |
| Raw p under 3 5 | 81.6% |
| Raw p btts yes | 45.2% |
| P home draw | 61.2% |
| P draw away | 67.9% |
| P home away | 70.9% |
| Raw p home draw | 61.9% |
| Raw p draw away | 67.9% |
| Raw p home away | 70.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:24:01Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.78, "price": 2.1, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:23:35Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.21, "price": 1.78, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:23:35Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.78, "price": 2.21, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:24:01Z", "line": 0.25, "market_key": "spreads", "opposite_price": 2.1, "price": 1.78, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 2.85 |
| Reference draw odds | 3.20 |
| Reference away odds | 2.35 |
| Market reference 1x2 last update utc | 2026-10-21T17:24:07Z |
| Market reference home last update utc | 2026-10-21T17:24:07Z |
| Market reference draw last update utc | 2026-10-21T17:24:07Z |
| Market reference away last update utc | 2026-10-21T17:24:07Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 2.18 |
| Reference Under 2.5 odds | 1.70 |
| Market reference over 2 5 last update utc | 2026-10-21T17:24:05Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:24:05Z |
| Market best over 2 5 last update utc | 2026-10-21T17:23:35Z |
| Market best under 2 5 last update utc | 2026-10-21T17:23:35Z |
| Home probability edge | -0.0% |
| Draw probability edge | +0.8% |
| Away probability edge | -0.7% |
| Over 2.5 probability edge | -5.0% |
| Under 2.5 probability edge | +5.0% |
| Raw edge prob home | -0.0004 |
| Raw ev home | -0.0379 |
| Raw edge prob draw | 0.0152 |
| Raw ev draw | -0.0274 |
| Raw edge prob away | -0.0148 |
| Raw ev away | -0.0666 |

</details>


---

## 2026-10-28 — Venezia vs Inter Milan

The model's most likely 1X2 outcome is **Inter Milan win** at **76.5%**. Expected goals are 0.69 for Venezia and 2.67 for Inter Milan (3.36 combined). The most likely exact score is 0-2 at 12.0%. Goal-market probabilities: at least one goal: 96.3%; Over 2.5 goals: 64.9%; Under 3.5 goals: 57.3%; Double Chance 1X: 23.5%; Double Chance X2: 90.4%; Double Chance 12 (either team wins): 86.1%; Under 4.5 goals: 75.5%; BTTS Yes (both teams score): 46.9%; BTTS No (at least one team does not score): 53.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Venezia win | 9.6% | 10.42 |
| Draw | 13.9% | 7.20 |
| Inter Milan win | 76.5% | 1.31 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Venezia expected goals | 0.69 |
| Inter Milan expected goals | 2.67 |
| Expected total goals | 3.36 |
| Over 0.5 | 96.3% |
| Under 0.5 | 3.7% |
| Over 1.5 | 84.6% |
| Under 1.5 | 15.4% |
| Over 2.5 | 64.9% |
| Under 2.5 | 35.1% |
| Over 3.5 | 42.7% |
| Under 3.5 | 57.3% |
| Over 4.5 | 24.5% |
| Under 4.5 | 75.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-2 | 11.97% |
| 2 | 0-3 | 10.67% |
| 3 | 0-1 | 8.74% |
| 4 | 1-2 | 8.24% |
| 5 | 1-3 | 7.35% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Venezia win | 9.6% | 12.2% | 7.76 | -25.5% |
| Draw | 13.9% | 13.9% | 5.92 | -17.8% |
| Inter Milan win | 76.5% | 73.9% | 1.32 | +1.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-28T17:30:00+00:00 |
| Fixture id | 33320ad169692216a91dec030e7ef6a6 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T17:24:01Z |
| Market best draw last update utc | 2026-10-21T17:24:01Z |
| Market best away last update utc | 2026-10-21T17:24:01Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Venezia |
| Matched away-team name | Inter |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.6888 |
| Dc lambda away | 2.6747 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T17:22:27.690536+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 19 |
| Score grid omitted mass | 0 |
| P btts yes | 46.9% |
| P btts no | 53.1% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 27.18 |
| Fair Over 1.5 odds | 1.18 |
| Fair Under 1.5 odds | 6.49 |
| Fair Over 2.5 odds | 1.54 |
| Fair Under 2.5 odds | 2.85 |
| Fair Over 3.5 odds | 2.34 |
| Fair Under 3.5 odds | 1.74 |
| Fair Over 4.5 odds | 4.08 |
| Fair Under 4.5 odds | 1.32 |
| Goal margin distribution | {"-1": 0.1994092417231836, "-10": 0.0002040074132851019, "-11": 4.8929902305078614e-05, "-12": 1.0779934743836594e-05, "-13": 2.1958757699011767e-06, "-14": 4.1589759641281514e-07, "-15": 7.359828819524669e-08, "-16": 1.2220905755471844e-08, "-17": 1.9110564711122308e-09, "-18": 2.8131602359989827e-10, "-19": 3.610104082097333e-11, "-2": 0.21232336654580738, "-3": 0.16587112983507296, "-4": 0.10203659976859401, "-5": 0.05154654151053787, "-6": 0.022041611595488016, "-7": 0.008160141659701869, "-8": 0.002661462209562228, "-9": 0.0007753370955895395, "0": 0.1389351190006261, "1": 0.07109785948890646, "10": 3.7358824765639555e-10, "11": 2.307524199198144e-11, "12": 1.3092202273722929e-12, "13": 6.867979660023686e-14, "14": 3.3499035515628482e-15, "15": 1.5266457224282571e-16, "16": 6.528277485599138e-18, "17": 2.6290169767220495e-19, "18": 9.966415733973281e-21, "19": 3.2937369459759576e-22, "2": 0.02009776554248403, "3": 0.004043388260358123, "4": 0.000640553310318599, "5": 8.333424266239719e-05, "6": 9.176814762939869e-06, "7": 8.749253046527832e-07, "8": 7.348830698758928e-08, "9": 5.5133194955081235e-09} |
| Raw goal margin distribution | {"-1": 0.20632327806191975, "-10": 0.00021108088017478003, "-11": 5.062642910426152e-05, "-12": 1.1153703080268841e-05, "-13": 2.272012486220085e-06, "-14": 4.3031784629663435e-07, "-15": 7.61501320047583e-08, "-16": 1.2644636299530065e-08, "-17": 1.977317762577293e-09, "-18": 2.910699808038402e-10, "-19": 3.735275767193504e-11, "-2": 0.21968516913416677, "-3": 0.17162231272567807, "-4": 0.10557447370354674, "-5": 0.05333379398720478, "-6": 0.02280585151846544, "-7": 0.008443074965484828, "-8": 0.0027537420170178463, "-9": 0.000802220046486659, "0": 0.13880570466153716, "1": 0.05154170813327655, "10": 2.7082920021991143e-10, "11": 1.6728174327681537e-11, "12": 9.491065881095005e-13, "13": 4.9788756742733455e-14, "14": 2.4284802998354585e-15, "15": 1.106727105625309e-16, "16": 4.732611856314644e-18, "17": 1.905880523910568e-19, "18": 7.225057049368659e-21, "19": 2.3877628603399968e-22, "2": 0.014569681466758697, "3": 0.002931215357016659, "4": 0.0004643629499056407, "5": 6.041235620438201e-05, "6": 6.652643434059946e-06, "7": 6.34268668775719e-07, "8": 5.3274640012952275e-08, "9": 3.99682784159377e-09} |
| Unadjusted home-win probability | 7.0% |
| Unadjusted draw probability | 13.9% |
| Unadjusted away-win probability | 79.2% |
| Raw p over 1 5 | 85.1% |
| Raw p under 3 5 | 56.6% |
| Raw p btts yes | 46.6% |
| P home draw | 23.5% |
| P draw away | 90.4% |
| P home away | 86.1% |
| Raw p home draw | 20.8% |
| Raw p draw away | 93.0% |
| Raw p home away | 86.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:23:35Z", "line": -1.5, "market_key": "spreads", "opposite_price": 2.06, "price": 1.89, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:24:01Z", "line": -1.5, "market_key": "spreads", "opposite_price": 2.02, "price": 1.84, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:23:35Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.89, "price": 2.06, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:24:01Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.84, "price": 2.02, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 6.50 |
| Reference draw odds | 5.80 |
| Reference away odds | 1.31 |
| Market reference 1x2 last update utc | 2026-10-21T17:24:08Z |
| Market reference home last update utc | 2026-10-21T17:24:08Z |
| Market reference draw last update utc | 2026-10-21T17:24:08Z |
| Market reference away last update utc | 2026-10-21T17:24:08Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.33 |
| Reference Under 2.5 odds | 3.37 |
| Market reference over 2 5 last update utc | 2026-10-21T17:24:05Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:24:05Z |
| Home probability edge | -2.6% |
| Draw probability edge | -0.0% |
| Away probability edge | +2.7% |
| Over 2.5 probability edge | -8.4% |
| Under 2.5 probability edge | +8.4% |
| Raw edge prob home | -0.0528 |
| Raw ev home | -0.4601 |
| Raw edge prob draw | -0.0003 |
| Raw ev draw | -0.1783 |
| Raw edge prob away | 0.0531 |
| Raw ev away | 0.0449 |

</details>


---

## 2026-10-29 — Fiorentina vs Atalanta BC

The model's most likely 1X2 outcome is **Atalanta BC win** at **38.4%**. Expected goals are 1.25 for Fiorentina and 1.59 for Atalanta BC (2.84 combined). The most likely exact score is 1-1 at 12.0%. Goal-market probabilities: at least one goal: 93.8%; Over 2.5 goals: 53.9%; Under 3.5 goals: 68.5%; Double Chance 1X: 61.6%; Double Chance X2: 63.9%; Double Chance 12 (either team wins): 74.5%; Under 4.5 goals: 84.2%; BTTS Yes (both teams score): 57.4%; BTTS No (at least one team does not score): 42.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Fiorentina win | 36.1% | 2.77 |
| Draw | 25.5% | 3.92 |
| Atalanta BC win | 38.4% | 2.60 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Fiorentina expected goals | 1.25 |
| Atalanta BC expected goals | 1.59 |
| Expected total goals | 2.84 |
| Over 0.5 | 93.8% |
| Under 0.5 | 6.2% |
| Over 1.5 | 77.8% |
| Under 1.5 | 22.2% |
| Over 2.5 | 53.9% |
| Under 2.5 | 46.1% |
| Over 3.5 | 31.5% |
| Under 3.5 | 68.5% |
| Over 4.5 | 15.8% |
| Under 4.5 | 84.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.03% |
| 2 | 2-1 | 8.82% |
| 3 | 1-0 | 8.39% |
| 4 | 1-2 | 7.91% |
| 5 | 0-1 | 7.61% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Fiorentina win | 36.1% | 42.4% | 2.30 | -17.1% |
| Draw | 25.5% | 25.6% | 3.54 | -9.7% |
| Atalanta BC win | 38.4% | 32.0% | 3.01 | +15.7% |
| Over 2.5 | 53.9% | 55.6% | 1.78 | -4.1% |
| Under 2.5 | 46.1% | 44.4% | 2.21 | +1.9% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-29T19:45:00+00:00 |
| Fixture id | da159a6b84dbb548b4d7b94c722caac5 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T17:24:01Z |
| Market best draw last update utc | 2026-10-21T17:24:01Z |
| Market best away last update utc | 2026-10-21T17:24:01Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Fiorentina |
| Matched away-team name | Atalanta |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 95/100 |
| Dc lambda home | 1.2523 |
| Dc lambda away | 1.5902 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T17:22:27.690536+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 57.4% |
| P btts no | 42.6% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 16.03 |
| Fair Over 1.5 odds | 1.29 |
| Fair Under 1.5 odds | 4.50 |
| Fair Over 2.5 odds | 1.86 |
| Fair Under 2.5 odds | 2.17 |
| Fair Over 3.5 odds | 3.18 |
| Fair Under 3.5 odds | 1.46 |
| Fair Over 4.5 odds | 6.34 |
| Fair Under 4.5 odds | 1.19 |
| Goal margin distribution | {"-1": 0.1861655484935417, "-10": 1.7025552608032766e-06, "-11": 2.4251135521345057e-07, "-12": 3.1735208360127446e-08, "-13": 3.8389767315610975e-09, "-14": 4.288821127626686e-10, "-15": 4.013799191385399e-11, "-2": 0.11696993554329081, "-3": 0.05383248307779402, "-4": 0.01956868746024032, "-5": 0.005852109220377535, "-6": 0.0014830216123185521, "-7": 0.000325621784554804, "-8": 6.30187478714884e-05, "-9": 1.0897668585351645e-05, "0": 0.25517145535301583, "1": 0.2067309585431726, "10": 2.213382019977141e-07, "11": 2.4828308981657066e-08, "12": 2.558682029905112e-09, "13": 2.4375321180711847e-10, "14": 2.1445328482524797e-11, "15": 1.5805575454230472e-12, "2": 0.10278984106161783, "3": 0.0372546303519997, "4": 0.010664916146757918, "5": 0.0025117017790299502, "6": 0.0005012599800301972, "7": 8.66740133433603e-05, "8": 1.3210070227336198e-05, "9": 1.7989904374953383e-06} |
| Raw goal margin distribution | {"-1": 0.2173030367635748, "-10": 1.987319519772408e-06, "-11": 2.8307307320806987e-07, "-12": 3.704314361483331e-08, "-13": 4.481072403478937e-09, "-14": 5.006156416751778e-10, "-15": 4.6851351407668555e-11, "-2": 0.1365339742464674, "-3": 0.06283634186877605, "-4": 0.02284168711664192, "-5": 0.006830915361895065, "-6": 0.0017310673352326199, "-7": 0.00038008430234656493, "-8": 7.355907361123567e-05, "-9": 1.2720379771674432e-05, "0": 0.2544367225847861, "1": 0.17030047523419767, "10": 1.8233360524868723e-07, "11": 2.04530218823258e-08, "12": 2.1077867037270256e-09, "13": 2.0079860366895807e-10, "14": 1.7666195996303824e-11, "15": 1.302028989839613e-12, "2": 0.08467603935762469, "3": 0.03068955563467271, "4": 0.008785526371689742, "5": 0.002069085393061981, "6": 0.0004129270885047431, "7": 7.140017038012678e-05, "8": 1.0882169044471723e-05, "9": 1.4819692638500138e-06} |
| Unadjusted home-win probability | 29.7% |
| Unadjusted draw probability | 25.4% |
| Unadjusted away-win probability | 44.9% |
| Raw p over 1 5 | 78.0% |
| Raw p under 3 5 | 68.2% |
| Raw p btts yes | 57.2% |
| P home draw | 61.6% |
| P draw away | 63.9% |
| P home away | 74.5% |
| Raw p home draw | 55.1% |
| Raw p draw away | 70.3% |
| Raw p home away | 74.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:23:35Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.76, "price": 2.24, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:24:01Z", "line": 0.25, "market_key": "spreads", "opposite_price": 2.0, "price": 1.85, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:24:01Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.85, "price": 2.0, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:23:35Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.24, "price": 1.76, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 2.20 |
| Reference draw odds | 3.50 |
| Reference away odds | 2.85 |
| Market reference 1x2 last update utc | 2026-10-21T17:24:07Z |
| Market reference home last update utc | 2026-10-21T17:24:07Z |
| Market reference draw last update utc | 2026-10-21T17:24:07Z |
| Market reference away last update utc | 2026-10-21T17:24:07Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.73 |
| Reference Under 2.5 odds | 2.13 |
| Market reference over 2 5 last update utc | 2026-10-21T17:24:05Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:24:05Z |
| Market best over 2 5 last update utc | 2026-10-21T17:23:35Z |
| Market best under 2 5 last update utc | 2026-10-21T17:23:35Z |
| Home probability edge | -6.4% |
| Draw probability edge | -0.1% |
| Away probability edge | +6.4% |
| Over 2.5 probability edge | -1.7% |
| Under 2.5 probability edge | +1.7% |
| Raw edge prob home | -0.1271 |
| Raw ev home | -0.3169 |
| Raw edge prob draw | -0.0015 |
| Raw ev draw | -0.0993 |
| Raw edge prob away | 0.1285 |
| Raw ev away | 0.3501 |

</details>


---

## 2026-10-29 — Frosinone vs Lecce

The model's most likely 1X2 outcome is **Frosinone win** at **50.0%**. Expected goals are 1.56 for Frosinone and 0.97 for Lecce (2.53 combined). The most likely exact score is 1-1 at 12.0%. Goal-market probabilities: at least one goal: 92.0%; Over 2.5 goals: 46.8%; Under 3.5 goals: 75.1%; Double Chance 1X: 75.2%; Double Chance X2: 50.0%; Double Chance 12 (either team wins): 74.8%; Under 4.5 goals: 88.6%; BTTS Yes (both teams score): 49.3%; BTTS No (at least one team does not score): 50.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Frosinone win | 50.0% | 2.00 |
| Draw | 25.2% | 3.97 |
| Lecce win | 24.8% | 4.03 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Frosinone expected goals | 1.56 |
| Lecce expected goals | 0.97 |
| Expected total goals | 2.53 |
| Over 0.5 | 92.0% |
| Under 0.5 | 8.0% |
| Over 1.5 | 72.3% |
| Under 1.5 | 27.7% |
| Over 2.5 | 46.8% |
| Under 2.5 | 53.2% |
| Over 3.5 | 24.9% |
| Under 3.5 | 75.1% |
| Over 4.5 | 11.4% |
| Under 4.5 | 88.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.97% |
| 2 | 1-0 | 11.83% |
| 3 | 2-0 | 9.55% |
| 4 | 2-1 | 9.28% |
| 5 | 0-0 | 8.02% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Frosinone win | 50.0% | 49.3% | 1.96 | -2.0% |
| Draw | 25.2% | 24.2% | 3.58 | -9.8% |
| Lecce win | 24.8% | 26.5% | 3.81 | -5.5% |
| Over 2.5 | 46.8% | 60.9% | 1.69 | -21.0% |
| Under 2.5 | 53.2% | 39.1% | 2.37 | +26.2% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-29T17:30:00+00:00 |
| Fixture id | 667cf69986b200753742c90cb9c5126c |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T17:24:01Z |
| Market best draw last update utc | 2026-10-21T17:24:01Z |
| Market best away last update utc | 2026-10-21T17:24:01Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Frosinone |
| Matched away-team name | Lecce |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.5622 |
| Dc lambda away | 0.9711 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T17:22:27.690536+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 49.3% |
| P btts no | 50.7% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 12.46 |
| Fair Over 1.5 odds | 1.38 |
| Fair Under 1.5 odds | 3.61 |
| Fair Over 2.5 odds | 2.14 |
| Fair Under 2.5 odds | 1.88 |
| Fair Over 3.5 odds | 4.01 |
| Fair Under 3.5 odds | 1.33 |
| Fair Over 4.5 odds | 8.77 |
| Fair Under 4.5 odds | 1.13 |
| Goal margin distribution | {"-1": 0.15932334623169703, "-10": 2.0096596655254075e-08, "-11": 1.7541363006177976e-09, "-12": 1.405920334487197e-10, "-13": 1.0414059367974874e-11, "-14": 7.141008203384042e-13, "-15": 4.198331720329063e-14, "-2": 0.06481074841581817, "-3": 0.018766125663285543, "-4": 0.004248541562525625, "-5": 0.0007866944916223338, "-6": 0.0001229944883759106, "-7": 1.6621146534591345e-05, "-8": 1.976565886429249e-06, "-9": 2.0977579819923509e-07, "0": 0.25202513253702274, "1": 0.2377591387478079, "10": 2.1427682803638402e-06, "11": 3.008926244383593e-07, "12": 3.8797561679637475e-08, "13": 4.623376727706082e-09, "14": 5.100283052949424e-10, "15": 4.8239967983863044e-11, "2": 0.1540052834785177, "3": 0.07173956148009288, "4": 0.02612880106320998, "5": 0.007783612986040258, "6": 0.0019577457442392665, "7": 0.00042562500092095304, "8": 8.142784871136093e-05, "9": 1.3903129286555385e-05} |
| Raw goal margin distribution | {"-1": 0.14833506437100716, "-10": 1.8710565833585364e-08, "-11": 1.6331562650539865e-09, "-12": 1.30895620917593e-10, "-13": 9.695817990575916e-12, "-14": 6.648504042730961e-13, "-15": 3.9087793516475635e-14, "-2": 0.06034085252146755, "-3": 0.017471855343847063, "-4": 0.0039555262996024115, "-5": 0.0007324374036521435, "-6": 0.00011451175098963687, "-7": 1.5474812068929823e-05, "-8": 1.840245230417394e-06, "-9": 1.9530788968059138e-07, "0": 0.26210234334255805, "1": 0.24110380672406426, "10": 2.172911594667618e-06, "11": 3.051254204122637e-07, "12": 3.934334495758061e-08, "13": 4.688415910488997e-09, "14": 5.172031097995706e-10, "15": 4.8918581966656776e-11, "2": 0.15617174716331106, "3": 0.07274875513370739, "4": 0.026496367015182865, "5": 0.007893108676641643, "6": 0.0019852862607926797, "7": 0.00043161246503262444, "8": 8.257333199076167e-05, "9": 1.4098711048583119e-05} |
| Unadjusted home-win probability | 50.7% |
| Unadjusted draw probability | 26.2% |
| Unadjusted away-win probability | 23.1% |
| Raw p over 1 5 | 72.4% |
| Raw p under 3 5 | 75.0% |
| Raw p btts yes | 49.5% |
| P home draw | 75.2% |
| P draw away | 50.0% |
| P home away | 74.8% |
| Raw p home draw | 76.9% |
| Raw p draw away | 49.3% |
| Raw p home away | 73.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:23:35Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.51, "price": 2.84, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:24:01Z", "line": 0.5, "market_key": "spreads", "opposite_price": 1.97, "price": 1.88, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:24:01Z", "line": -0.5, "market_key": "spreads", "opposite_price": 1.88, "price": 1.97, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:23:35Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.84, "price": 1.51, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 1.92 |
| Reference draw odds | 3.70 |
| Reference away odds | 3.40 |
| Market reference 1x2 last update utc | 2026-10-21T17:24:07Z |
| Market reference home last update utc | 2026-10-21T17:24:07Z |
| Market reference draw last update utc | 2026-10-21T17:24:07Z |
| Market reference away last update utc | 2026-10-21T17:24:07Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.59 |
| Reference Under 2.5 odds | 2.40 |
| Market reference over 2 5 last update utc | 2026-10-21T17:24:05Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:24:05Z |
| Market best over 2 5 last update utc | 2026-10-21T17:23:35Z |
| Market best under 2 5 last update utc | 2026-10-21T17:23:35Z |
| Home probability edge | +0.7% |
| Draw probability edge | +1.0% |
| Away probability edge | -1.7% |
| Over 2.5 probability edge | -14.1% |
| Under 2.5 probability edge | +14.1% |
| Raw edge prob home | 0.0141 |
| Raw ev home | -0.0064 |
| Raw edge prob draw | 0.0202 |
| Raw ev draw | -0.0617 |
| Raw edge prob away | -0.0342 |
| Raw ev away | -0.1200 |

</details>


---
