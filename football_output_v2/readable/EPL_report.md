# Premier League — football model report

Fixtures in this report: **16**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Premier League |
| Training matches | 1,970 |
| Training data through | 2026-10-19 |
| Model fit succeeded | Yes |
| Recency half-life (days) | 240 |
| Maximum goals per team in score matrix | 10 |
| Bookmaker margin-removal method | power |
| Market blending weight | 50.0% |

<details>
<summary>Technical model diagnostics</summary>

| Parameter | Value |
| --- | --- |
| Training seasons requested | 6 |
| Training seasons loaded | ['2122', '2223', '2324', '2425', '2526', '2627'] |
| Training sha256 | baf564c54ff02f6db9017cd767264f656bed0d3750728784333f48bd3cb27d17 |
| Training as of utc | 2026-10-21T17:09:55.842067+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 70, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 70, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 1102, 'added_results': 0, 'conflicts': 0, 'unmapped': 38, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 40, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_RETROSPECTIVE_EXAMPLES', 'cutoff_utc': '2026-10-21T17:09:55.842067+00:00', 'observations': 158, 'observations_sha256': '2f5490c16b119286f9c8a3a3318ff707460e54443dfed36cc866c433933b6f04', 'eligible_training_matches': 75, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 85, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 8, 'retrospective_eligible_training_matches': 75, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:26.478110+00:00', 'retrospective_inputs_sha256': '8c59b1a7f56d6ab8d819b1bf12c93b811f64fedad70b01bae483397a5df39f4a', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'input_providers': ['api-football', 'bigballsdata']} |
| Optimizer objective | 930.062 |
| Base scoring parameter | 0.212 |
| Home-advantage parameter | 0.185 |
| Dixon-Coles low-score adjustment | -0.089 |
| Xi per day | 0.0029 |
| Training data health | {'training_end': '2026-10-19', 'days_since_latest_result': 2, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 16.00 |
| Additional event odds calls used before this league | 0.00 |
| Bbs statistics model artifact | bbs/feature_models/EPL/20261021T170955842067Z_400f9ab3fa70a2f868878457e58eab11fd503e6448029ce2160a227d64644447.json |
| Over 1 5 in window quote fixtures | 0 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 0.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 0.00 |
| Bbs statistics applied fixtures | 0 |
| Decay tuning | {'selected_half_life_days': 240.0, 'selected_xi_per_day': 0.0028881132523331052, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365} |
| Goal market reliability | {'home_draw': 'RELIABLE_FOR_RANKING', 'draw_away': 'RELIABLE_FOR_RANKING', 'home_away': 'RELIABLE_FOR_RANKING', 'home': 'RELIABLE_FOR_RANKING', 'draw': 'RELIABLE_FOR_RANKING', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'UNRELIABLE_AUDIT', 'under_3_5': 'UNRELIABLE_AUDIT', 'btts_yes': 'UNRELIABLE_AUDIT'} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-23 — Ipswich Town vs Nottingham Forest

The model's most likely 1X2 outcome is **Nottingham Forest win** at **44.0%**. Expected goals are 1.32 for Ipswich Town and 1.69 for Nottingham Forest (3.01 combined). The most likely exact score is 1-1 at 12.2%. Goal-market probabilities: at least one goal: 94.0%; Over 2.5 goals: 57.8%; Under 3.5 goals: 64.5%; Double Chance 1X: 56.0%; Double Chance X2: 70.2%; Double Chance 12 (either team wins): 73.8%; Under 4.5 goals: 81.4%; BTTS Yes (both teams score): 60.9%; BTTS No (at least one team does not score): 39.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Ipswich Town win | 29.8% | 3.36 |
| Draw | 26.2% | 3.81 |
| Nottingham Forest win | 44.0% | 2.27 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Ipswich Town expected goals | 1.32 |
| Nottingham Forest expected goals | 1.69 |
| Expected total goals | 3.01 |
| Over 0.5 | 94.0% |
| Under 0.5 | 6.0% |
| Over 1.5 | 81.2% |
| Under 1.5 | 18.8% |
| Over 2.5 | 57.8% |
| Under 2.5 | 42.2% |
| Over 3.5 | 35.5% |
| Under 3.5 | 64.5% |
| Over 4.5 | 18.6% |
| Under 4.5 | 81.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.19% |
| 2 | 1-2 | 9.04% |
| 3 | 2-1 | 7.45% |
| 4 | 0-1 | 7.14% |
| 5 | 0-2 | 6.84% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Ipswich Town win | 29.8% | 30.5% | 3.32 | -1.1% |
| Draw | 26.2% | 26.7% | 3.49 | -8.4% |
| Nottingham Forest win | 44.0% | 42.8% | 2.24 | -1.5% |
| Over 2.5 | 57.8% | 55.7% | 1.83 | +5.7% |
| Under 2.5 | 42.2% | 44.3% | 2.14 | -9.6% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-23T19:00:00+00:00 |
| Fixture id | d0202960708a442401d7fc7bd74a0183 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T17:11:34Z |
| Market best draw last update utc | 2026-10-21T17:11:34Z |
| Market best away last update utc | 2026-10-21T17:11:34Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 17.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Ipswich |
| Matched away-team name | Nott'm Forest |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.3211 |
| Dc lambda away | 1.6907 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T17:09:55.842067+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 60.9% |
| P btts no | 39.1% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 16.64 |
| Fair Over 1.5 odds | 1.23 |
| Fair Under 1.5 odds | 5.32 |
| Fair Over 2.5 odds | 1.73 |
| Fair Under 2.5 odds | 2.37 |
| Fair Over 3.5 odds | 2.82 |
| Fair Under 3.5 odds | 1.55 |
| Fair Over 4.5 odds | 5.38 |
| Fair Under 4.5 odds | 1.23 |
| Goal margin distribution | {"-1": 0.20250042073093308, "-10": 3.07920651027254e-06, "-11": 4.6549498207009943e-07, "-12": 6.466663851827797e-08, "-13": 8.305145030445114e-09, "-14": 9.836633963234948e-10, "-15": 9.649982379358343e-11, "-2": 0.1359393584091633, "-3": 0.06555881564911355, "-4": 0.025092422945425748, "-5": 0.007923354278306382, "-6": 0.002123873808722082, "-7": 0.0004938450783942026, "-8": 0.00010129755138914595, "-9": 1.8576824464358973e-05, "0": 0.26232323879204833, "1": 0.16456256642609074, "10": 2.7550295232429754e-07, "11": 3.254569958053851e-08, "12": 3.5330522512053815e-09, "13": 3.545750409244035e-10, "14": 3.281698045883313e-11, "15": 2.5157633996980384e-12, "2": 0.0874789020099698, "3": 0.03296707175736691, "4": 0.009860139061666346, "5": 0.0024329920091972638, "6": 0.0005096258906797563, "7": 9.259865335161058e-05, "8": 1.4842397384746189e-05, "9": 2.1270012816239867e-06} |
| Raw goal margin distribution | {"-1": 0.20807982073114498, "-10": 3.1640464564911945e-06, "-11": 4.783205490179899e-07, "-12": 6.644836836190131e-08, "-13": 8.53397283246828e-09, "-14": 1.0107658168214164e-09, "-15": 9.915863859975003e-11, "-2": 0.1396848323869418, "-3": 0.06736512723467107, "-4": 0.02578378281560127, "-5": 0.008141662777135633, "-6": 0.002182391916911988, "-7": 0.0005074517623731875, "-8": 0.00010408855575448027, "-9": 1.9088663077070303e-05, "0": 0.25763907162141003, "1": 0.16045723816919047, "10": 2.686300037576843e-07, "11": 3.173378479924722e-08, "12": 3.4449134991490745e-09, "13": 3.4572948773261906e-10, "14": 3.19982980566946e-11, "15": 2.4530028655330918e-12, "2": 0.08529657333034607, "3": 0.03214464504045275, "4": 0.0096141590165933, "5": 0.002372296365825317, "6": 0.0004969122972125855, "7": 9.028860267355422e-05, "8": 1.447212536780418e-05, "9": 2.0739391627378188e-06} |
| Unadjusted home-win probability | 29.0% |
| Unadjusted draw probability | 25.8% |
| Unadjusted away-win probability | 45.2% |
| Raw p over 1 5 | 81.2% |
| Raw p under 3 5 | 64.5% |
| Raw p btts yes | 60.8% |
| P home draw | 56.0% |
| P draw away | 70.2% |
| P home away | 73.8% |
| Raw p home draw | 54.8% |
| Raw p draw away | 71.0% |
| Raw p home away | 74.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:11:34Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.96, "price": 1.94, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:10:44Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.38, "price": 1.68, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:10:44Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.68, "price": 2.38, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:11:34Z", "line": 0.25, "market_key": "spreads", "opposite_price": 1.94, "price": 1.96, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 3.20 |
| Reference draw odds | 3.65 |
| Reference away odds | 2.30 |
| Market reference 1x2 last update utc | 2026-10-21T17:11:38Z |
| Market reference home last update utc | 2026-10-21T17:11:38Z |
| Market reference draw last update utc | 2026-10-21T17:11:38Z |
| Market reference away last update utc | 2026-10-21T17:11:38Z |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 1.73 |
| Reference Under 2.5 odds | 2.14 |
| Market reference over 2 5 last update utc | 2026-10-21T17:11:38Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:11:38Z |
| Market best over 2 5 last update utc | 2026-10-21T17:10:44Z |
| Market best under 2 5 last update utc | 2026-10-21T17:10:44Z |
| Home probability edge | -0.7% |
| Draw probability edge | -0.5% |
| Away probability edge | +1.2% |
| Over 2.5 probability edge | +2.1% |
| Under 2.5 probability edge | -2.1% |
| Raw edge prob home | -0.0149 |
| Raw ev home | -0.0356 |
| Raw edge prob draw | -0.0094 |
| Raw ev draw | -0.1008 |
| Raw edge prob away | 0.0242 |
| Raw ev away | 0.0122 |

</details>


---

## 2026-10-24 — Arsenal vs Everton

The model's most likely 1X2 outcome is **Arsenal win** at **67.5%**. Expected goals are 1.72 for Arsenal and 0.58 for Everton (2.29 combined). The most likely exact score is 1-0 at 17.3%. Goal-market probabilities: at least one goal: 90.2%; Over 2.5 goals: 41.3%; Under 3.5 goals: 79.7%; Double Chance 1X: 89.5%; Double Chance X2: 32.5%; Double Chance 12 (either team wins): 78.1%; Under 4.5 goals: 91.4%; BTTS Yes (both teams score): 36.1%; BTTS No (at least one team does not score): 63.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Arsenal win | 67.5% | 1.48 |
| Draw | 21.9% | 4.56 |
| Everton win | 10.5% | 9.50 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Arsenal expected goals | 1.72 |
| Everton expected goals | 0.58 |
| Expected total goals | 2.29 |
| Over 0.5 | 90.2% |
| Under 0.5 | 9.8% |
| Over 1.5 | 68.2% |
| Under 1.5 | 31.8% |
| Over 2.5 | 41.3% |
| Under 2.5 | 58.7% |
| Over 3.5 | 20.3% |
| Under 3.5 | 79.7% |
| Over 4.5 | 8.6% |
| Under 4.5 | 91.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 17.29% |
| 2 | 2-0 | 15.64% |
| 3 | 0-0 | 9.79% |
| 4 | 1-1 | 9.69% |
| 5 | 2-1 | 9.01% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Arsenal win | 67.5% | 70.8% | 1.43 | -3.4% |
| Draw | 21.9% | 19.2% | 4.43 | -2.9% |
| Everton win | 10.5% | 10.0% | 8.63 | -9.1% |
| Over 2.5 | 41.3% | 54.0% | 1.89 | -21.9% |
| Under 2.5 | 58.7% | 46.0% | 2.06 | +20.9% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T14:00:00+00:00 |
| Fixture id | f66e4f29c1b7bcfc5ab58c0b88c8850b |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T17:11:33Z |
| Market best draw last update utc | 2026-10-21T17:11:33Z |
| Market best away last update utc | 2026-10-21T17:11:33Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 17.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Arsenal |
| Matched away-team name | Everton |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.7157 |
| Dc lambda away | 0.5763 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T17:09:55.842067+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 36.1% |
| P btts no | 63.9% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 10.22 |
| Fair Over 1.5 odds | 1.47 |
| Fair Under 1.5 odds | 3.15 |
| Fair Over 2.5 odds | 2.42 |
| Fair Under 2.5 odds | 1.70 |
| Fair Over 3.5 odds | 4.92 |
| Fair Under 3.5 odds | 1.26 |
| Fair Over 4.5 odds | 11.64 |
| Fair Under 4.5 odds | 1.09 |
| Goal margin distribution | {"-1": 0.07895377177115039, "-10": 1.1672076642592934e-10, "-11": 6.0700808346373565e-12, "-12": 2.8969686789317693e-13, "-13": 1.277373588381773e-14, "-14": 5.233618310669965e-16, "-15": 1.999215939857061e-17, "-16": 6.781987367219044e-19, "-2": 0.021848492405812894, "-3": 0.0038912239495704354, "-4": 0.000535017014827165, "-5": 5.974307338776715e-05, "-6": 5.6086882117550205e-06, "-7": 4.538608536404123e-07, "-8": 3.225762093446997e-08, "-9": 2.0433655884492412e-09, "0": 0.21927718115575023, "1": 0.27914886494547086, "10": 7.077418839710675e-06, "11": 1.095743914792369e-06, "12": 1.5568480191068618e-07, "13": 2.0436577972921992e-08, "14": 2.492757986364462e-09, "15": 2.8348207409579525e-10, "16": 2.862929792997497e-11, "2": 0.2147067195019471, "3": 0.11384087190005246, "4": 0.04659801390708621, "5": 0.01549084822871646, "6": 0.004329490214781503, "7": 0.0010430041000220652, "8": 0.00022069040407825567, "9": 4.161836519678016e-05} |
| Raw goal margin distribution | {"-1": 0.08327885083699901, "-10": 1.2311471736828384e-10, "-11": 6.402599205285888e-12, "-12": 3.0556643093822605e-13, "-13": 1.3473479751962694e-14, "-14": 5.520315354855911e-16, "-15": 2.108732772499959e-17, "-16": 7.153503900613171e-19, "-2": 0.023045350453312314, "-3": 0.004104384776055048, "-4": 0.0005643251889497256, "-5": 6.301579247695584e-05, "-6": 5.9159315444971995e-06, "-7": 4.787233020434865e-07, "-8": 3.4024689915318016e-08, "-9": 2.1553009340600076e-09, "0": 0.24640869678805394, "1": 0.2655517686071087, "10": 6.732683976435183e-06, "11": 1.0423711899041045e-06, "12": 1.4810153177841484e-07, "13": 1.9441130187101508e-08, "14": 2.3713379315294184e-09, "15": 2.6967391094087003e-10, "16": 2.7234789941810363e-11, "2": 0.20424854353862398, "3": 0.10829578289254196, "4": 0.04432826552607539, "5": 0.0147363026002757, "6": 0.004118604544306435, "7": 0.0009922002852471884, "8": 0.00020994076808818893, "9": 3.959117113623366e-05} |
| Unadjusted home-win probability | 64.3% |
| Unadjusted draw probability | 24.6% |
| Unadjusted away-win probability | 11.1% |
| Raw p over 1 5 | 67.6% |
| Raw p under 3 5 | 80.1% |
| Raw p btts yes | 36.8% |
| P home draw | 89.5% |
| P draw away | 32.5% |
| P home away | 78.1% |
| Raw p home draw | 88.9% |
| Raw p draw away | 35.7% |
| Raw p home away | 75.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:11:33Z", "line": 1.25, "market_key": "spreads", "opposite_price": 1.99, "price": 1.91, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:10:44Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.27, "price": 1.74, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:10:44Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.74, "price": 2.27, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:11:33Z", "line": -1.25, "market_key": "spreads", "opposite_price": 1.91, "price": 1.99, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 1.40 |
| Reference draw odds | 5.00 |
| Reference away odds | 9.50 |
| Market reference 1x2 last update utc | 2026-10-21T17:11:38Z |
| Market reference home last update utc | 2026-10-21T17:11:38Z |
| Market reference draw last update utc | 2026-10-21T17:11:38Z |
| Market reference away last update utc | 2026-10-21T17:11:38Z |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 1.78 |
| Reference Under 2.5 odds | 2.07 |
| Market reference over 2 5 last update utc | 2026-10-21T17:11:38Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:11:38Z |
| Market best over 2 5 last update utc | 2026-10-21T17:10:44Z |
| Market best under 2 5 last update utc | 2026-10-21T17:10:44Z |
| Home probability edge | -3.3% |
| Draw probability edge | +2.7% |
| Away probability edge | +0.6% |
| Over 2.5 probability edge | -12.7% |
| Under 2.5 probability edge | +12.7% |
| Raw edge prob home | -0.0658 |
| Raw ev home | -0.0812 |
| Raw edge prob draw | 0.0543 |
| Raw ev draw | 0.0916 |
| Raw edge prob away | 0.0115 |
| Raw ev away | -0.0415 |

</details>


---

## 2026-10-24 — Aston Villa vs Manchester City

The model's most likely 1X2 outcome is **Manchester City win** at **55.0%**. Expected goals are 1.12 for Aston Villa and 1.82 for Manchester City (2.95 combined). The most likely exact score is 1-1 at 11.0%. Goal-market probabilities: at least one goal: 94.1%; Over 2.5 goals: 57.1%; Under 3.5 goals: 65.7%; Double Chance 1X: 45.0%; Double Chance X2: 78.4%; Double Chance 12 (either team wins): 76.6%; Under 4.5 goals: 82.2%; BTTS Yes (both teams score): 57.1%; BTTS No (at least one team does not score): 42.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Aston Villa win | 21.6% | 4.62 |
| Draw | 23.4% | 4.27 |
| Manchester City win | 55.0% | 1.82 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Aston Villa expected goals | 1.12 |
| Manchester City expected goals | 1.82 |
| Expected total goals | 2.95 |
| Over 0.5 | 94.1% |
| Under 0.5 | 5.9% |
| Over 1.5 | 80.4% |
| Under 1.5 | 19.6% |
| Over 2.5 | 57.1% |
| Under 2.5 | 42.9% |
| Over 3.5 | 34.3% |
| Under 3.5 | 65.7% |
| Over 4.5 | 17.8% |
| Under 4.5 | 82.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.03% |
| 2 | 1-2 | 10.20% |
| 3 | 0-2 | 9.09% |
| 4 | 0-1 | 8.97% |
| 5 | 1-3 | 6.20% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Aston Villa win | 21.6% | 21.0% | 4.54 | -1.7% |
| Draw | 23.4% | 22.0% | 4.29 | +0.4% |
| Manchester City win | 55.0% | 57.1% | 1.71 | -6.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T11:30:00+00:00 |
| Fixture id | aca5dd297dbee71f576f7641569fe578 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T17:11:34Z |
| Market best draw last update utc | 2026-10-21T17:11:34Z |
| Market best away last update utc | 2026-10-21T17:11:34Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Aston Villa |
| Matched away-team name | Man City |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.1221 |
| Dc lambda away | 1.8242 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T17:09:55.842067+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 57.1% |
| P btts no | 42.9% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.09 |
| Fair Over 1.5 odds | 1.24 |
| Fair Under 1.5 odds | 5.10 |
| Fair Over 2.5 odds | 1.75 |
| Fair Under 2.5 odds | 2.33 |
| Fair Over 3.5 odds | 2.92 |
| Fair Under 3.5 odds | 1.52 |
| Fair Over 4.5 odds | 5.60 |
| Fair Under 4.5 odds | 1.22 |
| Goal margin distribution | {"-1": 0.23308273736283372, "-10": 7.389606111670777e-06, "-11": 1.206979219346991e-06, "-12": 1.8112901612143746e-07, "-13": 2.513610917421167e-08, "-14": 3.2428720911246906e-09, "-15": 3.8843044811673056e-10, "-16": 3.9262771752939685e-11, "-2": 0.17116511316700161, "-3": 0.09006344227865848, "-4": 0.037472673934399306, "-5": 0.012835066102043364, "-6": 0.0037268667719799462, "-7": 0.0009378614179395118, "-8": 0.00020806827405309928, "-9": 4.125149611285106e-05, "0": 0.2340401097805866, "1": 0.1301682896819252, "10": 5.344726515063783e-08, "11": 5.369704393195898e-09, "12": 4.956612874708021e-10, "13": 4.230984300877261e-11, "14": 3.357527406302889e-12, "15": 2.473713507255903e-13, "16": 1.5380252920947392e-14, "2": 0.06041549673496998, "3": 0.019553658601715155, "4": 0.005004267975515702, "5": 0.0010543149645316453, "6": 0.00018830528810496149, "7": 2.9147660732605236e-05, "8": 3.9775650214731694e-06, "9": 4.85062292161393e-07} |
| Raw goal margin distribution | {"-1": 0.22411695312053828, "-10": 7.1053567726489315e-06, "-11": 1.1605514341406002e-06, "-12": 1.7416168899572214e-07, "-13": 2.4169221046430916e-08, "-14": 3.118131443990771e-09, "-15": 3.734890430587855e-10, "-16": 3.775248598800393e-11, "-2": 0.16458105854405242, "-3": 0.08659905276305105, "-4": 0.036031246253915565, "-5": 0.012341351146107423, "-6": 0.003583508736308102, "-7": 0.000901785545407908, "-8": 0.00020006469869640985, "-9": 3.966471187475465e-05, "0": 0.24853892038955874, "1": 0.13416198459070564, "10": 5.508708135504462e-08, "11": 5.534452360225076e-09, "12": 5.10868677573943e-10, "13": 4.360795182642959e-11, "14": 3.4605397462622462e-12, "15": 2.5496095420263514e-13, "16": 1.5852134651407526e-14, "2": 0.06226910533896619, "3": 0.020153584643583886, "4": 0.005157803983285535, "5": 0.0010866624150235428, "6": 0.00019408268498279443, "7": 3.004194047274096e-05, "8": 4.0996007431870905e-06, "9": 4.99944494358103e-07} |
| Unadjusted home-win probability | 22.3% |
| Unadjusted draw probability | 24.9% |
| Unadjusted away-win probability | 52.8% |
| Raw p over 1 5 | 80.2% |
| Raw p under 3 5 | 65.9% |
| Raw p btts yes | 57.5% |
| P home draw | 45.0% |
| P draw away | 78.4% |
| P home away | 76.6% |
| Raw p home draw | 47.2% |
| Raw p draw away | 77.7% |
| Raw p home away | 75.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:10:44Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.51, "price": 2.82, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:11:34Z", "line": -0.75, "market_key": "spreads", "opposite_price": 2.0, "price": 1.9, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:11:34Z", "line": 0.75, "market_key": "spreads", "opposite_price": 1.9, "price": 2.0, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:10:44Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.82, "price": 1.51, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 4.60 |
| Reference draw odds | 4.40 |
| Reference away odds | 1.73 |
| Market reference 1x2 last update utc | 2026-10-21T17:11:38Z |
| Market reference home last update utc | 2026-10-21T17:11:38Z |
| Market reference draw last update utc | 2026-10-21T17:11:38Z |
| Market reference away last update utc | 2026-10-21T17:11:38Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.50 |
| Reference Under 2.5 odds | 2.45 |
| Market reference over 2 5 last update utc | 2026-10-21T17:11:33Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:11:33Z |
| Home probability edge | +0.7% |
| Draw probability edge | +1.4% |
| Away probability edge | -2.1% |
| Over 2.5 probability edge | -6.4% |
| Under 2.5 probability edge | +6.4% |
| Raw edge prob home | 0.0133 |
| Raw ev home | 0.0127 |
| Raw edge prob draw | 0.0290 |
| Raw ev draw | 0.0662 |
| Raw edge prob away | -0.0423 |
| Raw ev away | -0.0964 |

</details>


---

## 2026-10-24 — Chelsea vs Tottenham Hotspur

The model's most likely 1X2 outcome is **Chelsea win** at **57.4%**. Expected goals are 2.13 for Chelsea and 1.19 for Tottenham Hotspur (3.33 combined). The most likely exact score is 1-1 at 10.0%. Goal-market probabilities: at least one goal: 95.6%; Over 2.5 goals: 64.5%; Under 3.5 goals: 57.5%; Double Chance 1X: 79.6%; Double Chance X2: 42.6%; Double Chance 12 (either team wins): 77.8%; Under 4.5 goals: 75.8%; BTTS Yes (both teams score): 62.3%; BTTS No (at least one team does not score): 37.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Chelsea win | 57.4% | 1.74 |
| Draw | 22.2% | 4.51 |
| Tottenham Hotspur win | 20.4% | 4.90 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Chelsea expected goals | 2.13 |
| Tottenham Hotspur expected goals | 1.19 |
| Expected total goals | 3.33 |
| Over 0.5 | 95.6% |
| Under 0.5 | 4.4% |
| Over 1.5 | 85.2% |
| Under 1.5 | 14.8% |
| Over 2.5 | 64.5% |
| Under 2.5 | 35.5% |
| Over 3.5 | 42.5% |
| Under 3.5 | 57.5% |
| Over 4.5 | 24.2% |
| Under 4.5 | 75.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.99% |
| 2 | 2-1 | 9.64% |
| 3 | 2-0 | 8.08% |
| 4 | 3-1 | 6.86% |
| 5 | 1-0 | 6.77% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Chelsea win | 57.4% | 56.8% | 1.69 | -3.0% |
| Draw | 22.2% | 22.2% | 4.40 | -2.4% |
| Tottenham Hotspur win | 20.4% | 21.0% | 4.57 | -6.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T16:30:00+00:00 |
| Fixture id | 0382a9faef0bb8df1bcc436536cffb05 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T17:11:33Z |
| Market best draw last update utc | 2026-10-21T17:11:33Z |
| Market best away last update utc | 2026-10-21T17:11:33Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Chelsea |
| Matched away-team name | Tottenham |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.1329 |
| Dc lambda away | 1.1933 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T17:09:55.842067+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 62.3% |
| P btts no | 37.7% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 22.62 |
| Fair Over 1.5 odds | 1.17 |
| Fair Under 1.5 odds | 6.77 |
| Fair Over 2.5 odds | 1.55 |
| Fair Under 2.5 odds | 2.82 |
| Fair Over 3.5 odds | 2.35 |
| Fair Under 3.5 odds | 1.74 |
| Fair Over 4.5 odds | 4.14 |
| Fair Under 4.5 odds | 1.32 |
| Goal margin distribution | {"-1": 0.1214885302014992, "-10": 7.506080165813277e-08, "-11": 7.991287119096804e-09, "-12": 7.821002588205936e-10, "-13": 7.081395383522484e-11, "-14": 5.964371791265633e-12, "-15": 4.693405798248143e-13, "-16": 3.436915783703922e-14, "-17": 2.098394360376801e-15, "-2": 0.05712909797442705, "-3": 0.019100297718358212, "-4": 0.005097648235944069, "-5": 0.0011263179888251194, "-6": 0.00021172082049941918, "-7": 3.4574072805556713e-05, "-8": 4.985774743951554e-06, "-9": 6.432862186914184e-07, "0": 0.22181189130131193, "1": 0.214955119917945, "10": 2.3997437551466756e-05, "11": 4.566537275834518e-06, "12": 7.988243644252586e-07, "13": 1.292785037568378e-07, "14": 1.946214848341119e-08, "15": 2.737365442074572e-09, "16": 3.582879200155104e-10, "17": 3.909930035771809e-11, "2": 0.17533161536018577, "3": 0.1047759493102866, "4": 0.049981574374366754, "5": 0.019738751943399063, "6": 0.006631943808217256, "7": 0.001935737271449828, "8": 0.0004989386227521982, "9": 0.00011506343069451534} |
| Raw goal margin distribution | {"-1": 0.1180128102135027, "-10": 7.291335343231669e-08, "-11": 7.762660792614825e-09, "-12": 7.597248008436855e-10, "-13": 6.878800558837448e-11, "-14": 5.79373439680246e-12, "-15": 4.559130041370573e-13, "-16": 3.338587514634675e-14, "-17": 2.038360452575266e-15, "-2": 0.05549466592230994, "-3": 0.018553848712462163, "-4": 0.004951807325398365, "-5": 0.0010940946510326008, "-6": 0.000205663604345233, "-7": 3.358492761038966e-05, "-8": 4.843134472442311e-06, "-9": 6.248821540064638e-07, "0": 0.22123686233211964, "1": 0.21735818664388815, "10": 2.4265714221079654e-05, "11": 4.617588368660435e-06, "12": 8.077547320794731e-07, "13": 1.30723758333125e-07, "14": 1.9679723396042738e-08, "15": 2.767967512930605e-09, "16": 3.622933597520718e-10, "17": 3.953640661382009e-11, "2": 0.17729171554779125, "3": 0.10594728031911659, "4": 0.05054033779593654, "5": 0.019959419113480585, "6": 0.006706084882409558, "7": 0.001957377629813773, "8": 0.0005045164512918554, "9": 0.00011634976945109116} |
| Unadjusted home-win probability | 58.0% |
| Unadjusted draw probability | 22.1% |
| Unadjusted away-win probability | 19.8% |
| Raw p over 1 5 | 85.3% |
| Raw p under 3 5 | 57.5% |
| Raw p btts yes | 62.2% |
| P home draw | 79.6% |
| P draw away | 42.6% |
| P home away | 77.8% |
| Raw p home draw | 80.2% |
| Raw p draw away | 42.0% |
| Raw p home away | 77.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:11:33Z", "line": 0.75, "market_key": "spreads", "opposite_price": 1.88, "price": 2.03, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:10:44Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.89, "price": 1.49, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:10:44Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.49, "price": 2.89, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:11:33Z", "line": -0.75, "market_key": "spreads", "opposite_price": 2.03, "price": 1.88, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 1.74 |
| Reference draw odds | 4.35 |
| Reference away odds | 4.60 |
| Market reference 1x2 last update utc | 2026-10-21T17:11:38Z |
| Market reference home last update utc | 2026-10-21T17:11:38Z |
| Market reference draw last update utc | 2026-10-21T17:11:38Z |
| Market reference away last update utc | 2026-10-21T17:11:38Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.50 |
| Reference Under 2.5 odds | 2.50 |
| Market reference over 2 5 last update utc | 2026-10-21T17:11:33Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:11:33Z |
| Home probability edge | +0.6% |
| Draw probability edge | -0.1% |
| Away probability edge | -0.6% |
| Over 2.5 probability edge | +0.7% |
| Under 2.5 probability edge | -0.7% |
| Raw edge prob home | 0.0128 |
| Raw ev home | -0.0191 |
| Raw edge prob draw | -0.0012 |
| Raw ev draw | -0.0266 |
| Raw edge prob away | -0.0117 |
| Raw ev away | -0.0935 |

</details>


---

## 2026-10-24 — Coventry City vs Fulham

The model's most likely 1X2 outcome is **Fulham win** at **41.1%**. Expected goals are 1.10 for Coventry City and 1.37 for Fulham (2.47 combined). The most likely exact score is 1-1 at 13.2%. Goal-market probabilities: at least one goal: 90.8%; Over 2.5 goals: 45.3%; Under 3.5 goals: 76.4%; Double Chance 1X: 58.9%; Double Chance X2: 68.9%; Double Chance 12 (either team wins): 72.2%; Under 4.5 goals: 89.4%; BTTS Yes (both teams score): 50.6%; BTTS No (at least one team does not score): 49.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Coventry City win | 31.1% | 3.21 |
| Draw | 27.8% | 3.60 |
| Fulham win | 41.1% | 2.43 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Coventry City expected goals | 1.10 |
| Fulham expected goals | 1.37 |
| Expected total goals | 2.47 |
| Over 0.5 | 90.8% |
| Under 0.5 | 9.2% |
| Over 1.5 | 71.8% |
| Under 1.5 | 28.2% |
| Over 2.5 | 45.3% |
| Under 2.5 | 54.7% |
| Over 3.5 | 23.6% |
| Under 3.5 | 76.4% |
| Over 4.5 | 10.6% |
| Under 4.5 | 89.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.22% |
| 2 | 0-1 | 10.29% |
| 3 | 0-0 | 9.15% |
| 4 | 1-0 | 8.78% |
| 5 | 1-2 | 8.58% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Coventry City win | 31.1% | 33.2% | 3.09 | -3.8% |
| Draw | 27.8% | 26.4% | 3.55 | -1.4% |
| Fulham win | 41.1% | 40.5% | 2.33 | -4.2% |
| Over 2.5 | 45.3% | 55.3% | 1.81 | -18.1% |
| Under 2.5 | 54.7% | 44.7% | 2.15 | +17.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T14:00:00+00:00 |
| Fixture id | 0fbb2626ed9534b9dcf21d16925f9bd7 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T17:11:33Z |
| Market best draw last update utc | 2026-10-21T17:11:33Z |
| Market best away last update utc | 2026-10-21T17:11:33Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 16.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Coventry |
| Matched away-team name | Fulham |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.1009 |
| Dc lambda away | 1.3664 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T17:09:55.842067+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 50.6% |
| P btts no | 49.4% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 10.93 |
| Fair Over 1.5 odds | 1.39 |
| Fair Under 1.5 odds | 3.54 |
| Fair Over 2.5 odds | 2.21 |
| Fair Under 2.5 odds | 1.83 |
| Fair Over 3.5 odds | 4.24 |
| Fair Under 3.5 odds | 1.31 |
| Fair Over 4.5 odds | 9.45 |
| Fair Under 4.5 odds | 1.12 |
| Goal margin distribution | {"-1": 0.21312293208314798, "-10": 5.9814939262686e-07, "-11": 7.347258954428293e-08, "-12": 8.28544905747915e-09, "-13": 8.596386165682818e-10, "-14": 7.576142462464596e-11, "-2": 0.12516779182329282, "-3": 0.05104054144256466, "-4": 0.016268636139846873, "-5": 0.004240505724926811, "-6": 0.0009331560066686248, "-7": 0.00017748365502767558, "-8": 2.9704209991133818e-05, "-9": 4.4366737282918314e-06, "0": 0.27773714599369503, "1": 0.18446680873067658, "10": 7.503269693917556e-08, "11": 7.425834598963152e-09, "12": 6.747066805469832e-10, "13": 5.6401922766648e-11, "14": 4.0050243383329344e-12, "2": 0.0884099629769129, "3": 0.029047109704422227, "4": 0.007459639367068, "5": 0.0015666189452899493, "6": 0.00027776595241183524, "7": 4.256593253062853e-05, "8": 5.739853778756346e-06, "9": 6.907475427568818e-07} |
| Raw goal margin distribution | {"-1": 0.21647747857415992, "-10": 6.075642403230927e-07, "-11": 7.462904518719413e-08, "-12": 8.415861696750561e-09, "-13": 8.731692942694617e-10, "-14": 7.69539064408661e-11, "-2": 0.12713792789801956, "-3": 0.05184391753880149, "-4": 0.016524703826899818, "-5": 0.004307251116709051, "-6": 0.0009478438451716898, "-7": 0.0001802772407125459, "-8": 3.0171753077277007e-05, "-9": 4.5065067966600916e-06, "0": 0.29195634397893033, "1": 0.17220677080634547, "10": 7.004587184923644e-08, "11": 6.932298583299654e-09, "12": 6.298643072863133e-10, "13": 5.2653336682883285e-11, "14": 3.738842304753549e-12, "2": 0.08253405767750381, "3": 0.027116579930427164, "4": 0.006963856618011972, "5": 0.0014624982754827722, "6": 0.00025930506433072254, "7": 3.973691439614154e-05, "8": 5.358371464990023e-06, "9": 6.448390612874477e-07} |
| Unadjusted home-win probability | 29.1% |
| Unadjusted draw probability | 29.2% |
| Unadjusted away-win probability | 41.7% |
| Raw p over 1 5 | 71.7% |
| Raw p under 3 5 | 76.5% |
| Raw p btts yes | 50.9% |
| P home draw | 58.9% |
| P draw away | 68.9% |
| P home away | 72.2% |
| Raw p home draw | 58.3% |
| Raw p draw away | 70.9% |
| Raw p home away | 70.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:11:33Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.88, "price": 2.03, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:10:44Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.25, "price": 1.75, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:10:44Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.75, "price": 2.25, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:11:33Z", "line": 0.25, "market_key": "spreads", "opposite_price": 2.03, "price": 1.88, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 2.95 |
| Reference draw odds | 3.70 |
| Reference away odds | 2.43 |
| Market reference 1x2 last update utc | 2026-10-21T17:11:38Z |
| Market reference home last update utc | 2026-10-21T17:11:38Z |
| Market reference draw last update utc | 2026-10-21T17:11:38Z |
| Market reference away last update utc | 2026-10-21T17:11:38Z |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 1.74 |
| Reference Under 2.5 odds | 2.12 |
| Market reference over 2 5 last update utc | 2026-10-21T17:11:38Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:11:38Z |
| Market best over 2 5 last update utc | 2026-10-21T17:10:44Z |
| Market best under 2 5 last update utc | 2026-10-21T17:10:44Z |
| Home probability edge | -2.1% |
| Draw probability edge | +1.4% |
| Away probability edge | +0.6% |
| Over 2.5 probability edge | -10.0% |
| Under 2.5 probability edge | +10.0% |
| Raw edge prob home | -0.0414 |
| Raw ev home | -0.1021 |
| Raw edge prob draw | 0.0284 |
| Raw ev draw | 0.0364 |
| Raw edge prob away | 0.0129 |
| Raw ev away | -0.0273 |

</details>


---

## 2026-10-25 — Crystal Palace vs Newcastle United

The model's most likely 1X2 outcome is **Newcastle United win** at **40.0%**. Expected goals are 1.50 for Crystal Palace and 1.58 for Newcastle United (3.08 combined). The most likely exact score is 1-1 at 11.9%. Goal-market probabilities: at least one goal: 94.4%; Over 2.5 goals: 59.4%; Under 3.5 goals: 63.0%; Double Chance 1X: 60.0%; Double Chance X2: 65.9%; Double Chance 12 (either team wins): 74.1%; Under 4.5 goals: 80.2%; BTTS Yes (both teams score): 62.6%; BTTS No (at least one team does not score): 37.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Crystal Palace win | 34.1% | 2.93 |
| Draw | 25.9% | 3.87 |
| Newcastle United win | 40.0% | 2.50 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Crystal Palace expected goals | 1.50 |
| Newcastle United expected goals | 1.58 |
| Expected total goals | 3.08 |
| Over 0.5 | 94.4% |
| Under 0.5 | 5.6% |
| Over 1.5 | 82.2% |
| Under 1.5 | 17.8% |
| Over 2.5 | 59.4% |
| Under 2.5 | 40.6% |
| Over 3.5 | 37.0% |
| Under 3.5 | 63.0% |
| Over 4.5 | 19.8% |
| Under 4.5 | 80.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.87% |
| 2 | 1-2 | 8.87% |
| 3 | 2-1 | 7.90% |
| 4 | 0-1 | 6.50% |
| 5 | 2-2 | 6.44% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Crystal Palace win | 34.1% | 33.0% | 2.97 | +1.3% |
| Draw | 25.9% | 25.8% | 3.65 | -5.6% |
| Newcastle United win | 40.0% | 41.1% | 2.36 | -5.5% |
| Over 2.5 | 59.4% | 59.1% | 1.69 | +0.3% |
| Under 2.5 | 40.6% | 40.9% | 2.36 | -4.1% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T14:00:00+00:00 |
| Fixture id | fe235b26408c477368c40672a4488694 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T17:11:34Z |
| Market best draw last update utc | 2026-10-21T17:11:34Z |
| Market best away last update utc | 2026-10-21T17:11:34Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Crystal Palace |
| Matched away-team name | Newcastle |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.4954 |
| Dc lambda away | 1.5800 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T17:09:55.842067+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 62.6% |
| P btts no | 37.4% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.91 |
| Fair Over 1.5 odds | 1.22 |
| Fair Under 1.5 odds | 5.61 |
| Fair Over 2.5 odds | 1.68 |
| Fair Under 2.5 odds | 2.46 |
| Fair Over 3.5 odds | 2.70 |
| Fair Under 3.5 odds | 1.59 |
| Fair Over 4.5 odds | 5.06 |
| Fair Under 4.5 odds | 1.25 |
| Goal margin distribution | {"-1": 0.19639107113419657, "-10": 1.5703064613052197e-06, "-11": 2.2164172026870925e-07, "-12": 2.8751857287633446e-08, "-13": 3.4482351378392867e-09, "-14": 3.810740775168927e-10, "-15": 3.46772597528837e-11, "-2": 0.1221909824712651, "-3": 0.054657442894708586, "-4": 0.019451338717904287, "-5": 0.0057192265037121345, "-6": 0.0014288258593769415, "-7": 0.0003098359344043296, "-8": 5.929493834530856e-05, "-9": 1.0148530645830113e-05, "0": 0.2585618453852348, "1": 0.17452051581303105, "10": 8.528725659752776e-07, "11": 1.139340450913735e-07, "12": 1.3988469037624259e-08, "13": 1.587827912459138e-09, "14": 1.6608034693873901e-10, "15": 1.4303946770501875e-11, "2": 0.10306724452269307, "3": 0.04363481064988811, "4": 0.014697232344425638, "5": 0.0040900219360994975, "6": 0.0009670967405361528, "7": 0.00019848362385286897, "8": 3.5951150603516415e-05, "9": 5.8237217582245105e-06} |
| Raw goal margin distribution | {"-1": 0.19087361433381958, "-10": 1.5261899033906076e-06, "-11": 2.1541486581101228e-07, "-12": 2.7944095867529354e-08, "-13": 3.351359611367057e-09, "-14": 3.7036809303246435e-10, "-15": 3.3703028686588175e-11, "-2": 0.11875812035952402, "-3": 0.05312188387846104, "-4": 0.018904868247196362, "-5": 0.005558549213326359, "-6": 0.0013886840906659446, "-7": 0.0003011313310157559, "-8": 5.76290924445155e-05, "-9": 9.863415446334061e-06, "0": 0.25883199771844334, "1": 0.18013317018567745, "10": 8.803013121856065e-07, "11": 1.1759821267302609e-07, "12": 1.4438344180067474e-08, "13": 1.638893136707165e-09, "14": 1.714215618733487e-10, "15": 1.476396781165883e-11, "2": 0.10638193115395798, "3": 0.04503812480841413, "4": 0.015169901617716778, "5": 0.004221558789499941, "6": 0.000998198985015865, "7": 0.00020486694202108933, "8": 3.710735497121764e-05, "9": 6.011015138828499e-06} |
| Unadjusted home-win probability | 35.2% |
| Unadjusted draw probability | 25.9% |
| Unadjusted away-win probability | 38.9% |
| Raw p over 1 5 | 82.2% |
| Raw p under 3 5 | 63.0% |
| Raw p btts yes | 62.6% |
| P home draw | 60.0% |
| P draw away | 65.9% |
| P home away | 74.1% |
| Raw p home draw | 61.1% |
| Raw p draw away | 64.8% |
| Raw p home away | 74.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:11:34Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.85, "price": 2.06, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:10:44Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.21, "price": 1.78, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:10:44Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.78, "price": 2.21, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:11:34Z", "line": 0.25, "market_key": "spreads", "opposite_price": 2.06, "price": 1.85, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 2.95 |
| Reference draw odds | 3.75 |
| Reference away odds | 2.38 |
| Market reference 1x2 last update utc | 2026-10-21T17:11:38Z |
| Market reference home last update utc | 2026-10-21T17:11:38Z |
| Market reference draw last update utc | 2026-10-21T17:11:38Z |
| Market reference away last update utc | 2026-10-21T17:11:38Z |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 1.63 |
| Reference Under 2.5 odds | 2.30 |
| Market reference over 2 5 last update utc | 2026-10-21T17:11:38Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:11:38Z |
| Market best over 2 5 last update utc | 2026-10-21T17:10:44Z |
| Market best under 2 5 last update utc | 2026-10-21T17:10:44Z |
| Home probability edge | +1.1% |
| Draw probability edge | +0.0% |
| Away probability edge | -1.1% |
| Over 2.5 probability edge | +0.2% |
| Under 2.5 probability edge | -0.2% |
| Raw edge prob home | 0.0219 |
| Raw ev home | 0.0460 |
| Raw edge prob draw | 0.0005 |
| Raw ev draw | -0.0553 |
| Raw edge prob away | -0.0225 |
| Raw ev away | -0.0820 |

</details>


---

## 2026-10-25 — Hull City vs Brentford

The model's most likely 1X2 outcome is **Brentford win** at **44.3%**. Expected goals are 1.19 for Hull City and 1.05 for Brentford (2.24 combined). The most likely exact score is 0-1 at 14.3%. Goal-market probabilities: at least one goal: 89.8%; Over 2.5 goals: 40.2%; Under 3.5 goals: 81.0%; Double Chance 1X: 55.7%; Double Chance X2: 71.2%; Double Chance 12 (either team wins): 73.1%; Under 4.5 goals: 92.0%; BTTS Yes (both teams score): 45.7%; BTTS No (at least one team does not score): 54.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Hull City win | 28.8% | 3.48 |
| Draw | 26.9% | 3.72 |
| Brentford win | 44.3% | 2.25 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Hull City expected goals | 1.19 |
| Brentford expected goals | 1.05 |
| Expected total goals | 2.24 |
| Over 0.5 | 89.8% |
| Under 0.5 | 10.2% |
| Over 1.5 | 66.9% |
| Under 1.5 | 33.1% |
| Over 2.5 | 40.2% |
| Under 2.5 | 59.8% |
| Over 3.5 | 19.0% |
| Under 3.5 | 81.0% |
| Over 4.5 | 8.0% |
| Under 4.5 | 92.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 14.26% |
| 2 | 1-1 | 12.54% |
| 3 | 0-0 | 10.20% |
| 4 | 1-2 | 10.01% |
| 5 | 1-0 | 8.68% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Hull City win | 28.8% | 19.6% | 4.75 | +36.6% |
| Draw | 26.9% | 22.7% | 4.11 | +10.5% |
| Brentford win | 44.3% | 57.7% | 1.72 | -23.7% |
| Over 2.5 | 40.2% | 56.3% | 1.73 | -30.4% |
| Under 2.5 | 59.8% | 43.7% | 2.28 | +36.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T14:00:00+00:00 |
| Fixture id | 69493b5ebb84f24ab1d6023a30ee89f0 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T17:11:34Z |
| Market best draw last update utc | 2026-10-21T17:11:34Z |
| Market best away last update utc | 2026-10-21T17:11:34Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Hull |
| Matched away-team name | Brentford |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.1914 |
| Dc lambda away | 1.0535 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T17:09:55.842067+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 45.7% |
| P btts no | 54.3% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 9.81 |
| Fair Over 1.5 odds | 1.50 |
| Fair Under 1.5 odds | 3.02 |
| Fair Over 2.5 odds | 2.49 |
| Fair Under 2.5 odds | 1.67 |
| Fair Over 3.5 odds | 5.27 |
| Fair Under 3.5 odds | 1.23 |
| Fair Over 4.5 odds | 12.46 |
| Fair Under 4.5 odds | 1.09 |
| Goal margin distribution | {"-1": 0.2659331158582745, "-10": 7.870453132211581e-08, "-11": 7.466181556438206e-09, "-12": 6.477232466268893e-10, "-13": 4.7868223266953246e-11, "-2": 0.12517522337199907, "-3": 0.040010000166023484, "-4": 0.009938163410620359, "-5": 0.002012148258418242, "-6": 0.0003432575934855973, "-7": 5.054574246398405e-05, "-8": 6.543620027467988e-06, "-9": 7.555361680786369e-07, "0": 0.2689207923742017, "1": 0.16083927688798266, "10": 1.4294786565978954e-07, "11": 1.533533435333471e-08, "12": 1.5045303441947733e-09, "13": 1.25740603276065e-10, "2": 0.08498889790159025, "3": 0.030720560850132275, "4": 0.008629457315042768, "5": 0.00197585055365126, "6": 0.0003811808145508531, "7": 6.347639077575531e-05, "8": 9.293140052679515e-06, "9": 1.2134347638796898e-06} |
| Raw goal margin distribution | {"-1": 0.18607074624322606, "-10": 5.5068774825449326e-08, "-11": 5.224012696990487e-09, "-12": 4.5320548916961975e-10, "-13": 3.3492917931161865e-11, "-2": 0.08758385411617274, "-3": 0.027994597679407242, "-4": 0.006953633721521024, "-5": 0.0014078800482878653, "-6": 0.00024017391127608865, "-7": 3.536635138251735e-05, "-8": 4.5785056054920925e-06, "-9": 5.286411139673984e-07, "0": 0.3106569135392382, "1": 0.21197639190352632, "10": 1.883965992583756e-07, "11": 2.0211038670100937e-08, "12": 1.982879555557164e-09, "13": 1.6571847321097026e-10, "2": 0.11201020221934575, "3": 0.04048783215308227, "4": 0.011373100284467471, "5": 0.0026040509470536717, "6": 0.0005023731472481784, "7": 8.365802525383177e-05, "8": 1.2247793797239684e-05, "9": 1.5992332720860584e-06} |
| Unadjusted home-win probability | 37.9% |
| Unadjusted draw probability | 31.1% |
| Unadjusted away-win probability | 31.0% |
| Raw p over 1 5 | 66.8% |
| Raw p under 3 5 | 81.0% |
| Raw p btts yes | 46.5% |
| P home draw | 55.7% |
| P draw away | 71.2% |
| P home away | 73.1% |
| Raw p home draw | 69.0% |
| Raw p draw away | 62.1% |
| Raw p home away | 68.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:10:44Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.46, "price": 3.04, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:11:34Z", "line": -0.75, "market_key": "spreads", "opposite_price": 1.98, "price": 1.93, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:11:34Z", "line": 0.75, "market_key": "spreads", "opposite_price": 1.93, "price": 1.98, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:10:44Z", "line": 1.5, "market_key": "spreads", "opposite_price": 3.04, "price": 1.46, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Everygame |
| Reference home odds | 4.40 |
| Reference draw odds | 3.85 |
| Reference away odds | 1.65 |
| Market reference 1x2 last update utc | 2026-10-21T17:11:39Z |
| Market reference home last update utc | 2026-10-21T17:11:39Z |
| Market reference draw last update utc | 2026-10-21T17:11:39Z |
| Market reference away last update utc | 2026-10-21T17:11:39Z |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 1.71 |
| Reference Under 2.5 odds | 2.17 |
| Market reference over 2 5 last update utc | 2026-10-21T17:11:38Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:11:38Z |
| Market best over 2 5 last update utc | 2026-10-21T17:10:44Z |
| Market best under 2 5 last update utc | 2026-10-21T17:10:44Z |
| Home probability edge | +9.1% |
| Draw probability edge | +4.2% |
| Away probability edge | -13.3% |
| Over 2.5 probability edge | -16.1% |
| Under 2.5 probability edge | +16.1% |
| Raw edge prob home | 0.1829 |
| Raw ev home | 0.8005 |
| Raw edge prob draw | 0.0835 |
| Raw ev draw | 0.2768 |
| Raw edge prob away | -0.2664 |
| Raw ev away | -0.4663 |

</details>


---

## 2026-10-25 — Liverpool vs Brighton and Hove Albion

The model's most likely 1X2 outcome is **Liverpool win** at **43.2%**. Expected goals are 1.64 for Liverpool and 1.47 for Brighton and Hove Albion (3.11 combined). The most likely exact score is 1-1 at 11.2%. Goal-market probabilities: at least one goal: 94.8%; Over 2.5 goals: 60.5%; Under 3.5 goals: 62.1%; Double Chance 1X: 67.8%; Double Chance X2: 56.8%; Double Chance 12 (either team wins): 75.4%; Under 4.5 goals: 79.4%; BTTS Yes (both teams score): 62.8%; BTTS No (at least one team does not score): 37.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Liverpool win | 43.2% | 2.31 |
| Draw | 24.6% | 4.06 |
| Brighton and Hove Albion win | 32.2% | 3.11 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Liverpool expected goals | 1.64 |
| Brighton and Hove Albion expected goals | 1.47 |
| Expected total goals | 3.11 |
| Over 0.5 | 94.8% |
| Under 0.5 | 5.2% |
| Over 1.5 | 82.7% |
| Under 1.5 | 17.3% |
| Over 2.5 | 60.5% |
| Under 2.5 | 39.5% |
| Over 3.5 | 37.9% |
| Under 3.5 | 62.1% |
| Over 4.5 | 20.6% |
| Under 4.5 | 79.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.25% |
| 2 | 2-1 | 9.34% |
| 3 | 1-2 | 7.57% |
| 4 | 1-0 | 6.72% |
| 5 | 2-0 | 6.34% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Liverpool win | 43.2% | 45.7% | 2.16 | -6.7% |
| Draw | 24.6% | 23.6% | 4.00 | -1.5% |
| Brighton and Hove Albion win | 32.2% | 30.7% | 3.12 | +0.4% |
| Over 2.5 | 60.5% | 61.3% | 1.64 | -0.8% |
| Under 2.5 | 39.5% | 38.7% | 2.47 | -2.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T14:00:00+00:00 |
| Fixture id | 290ba8cd3f3a2e9252effca673bf5549 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T17:11:33Z |
| Market best draw last update utc | 2026-10-21T17:11:33Z |
| Market best away last update utc | 2026-10-21T17:11:33Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 8.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Liverpool |
| Matched away-team name | Brighton |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.6381 |
| Dc lambda away | 1.4736 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T17:09:55.842067+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 62.8% |
| P btts no | 37.2% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 19.23 |
| Fair Over 1.5 odds | 1.21 |
| Fair Under 1.5 odds | 5.79 |
| Fair Over 2.5 odds | 1.65 |
| Fair Under 2.5 odds | 2.53 |
| Fair Over 3.5 odds | 2.64 |
| Fair Under 3.5 odds | 1.61 |
| Fair Over 4.5 odds | 4.86 |
| Fair Under 4.5 odds | 1.26 |
| Goal margin distribution | {"-1": 0.16673326575733458, "-10": 7.043053540176079e-07, "-11": 9.268174508700324e-08, "-12": 1.1209793508564533e-08, "-13": 1.253494930886464e-09, "-14": 1.2911776609503217e-10, "-15": 1.092623111121403e-11, "-2": 0.09667151025197392, "-3": 0.040211839906862196, "-4": 0.013320274423720102, "-5": 0.003647600245868292, "-6": 0.0008490099165222419, "-7": 0.00017156714910575576, "-8": 3.0602896667464165e-05, "-9": 4.882519765754008e-06, "0": 0.24629473679739056, "1": 0.20666142232407758, "10": 2.2499328534513257e-06, "11": 3.2911997680489135e-07, "12": 4.424957744568111e-08, "13": 5.50028978387893e-09, "14": 6.297968242730554e-10, "15": 5.924290130609945e-11, "2": 0.13246321153565546, "3": 0.06124945031516013, "4": 0.02255344539849912, "5": 0.006865282845235792, "6": 0.0017762963974426735, "7": 0.0003990141349504115, "8": 7.911669842361752e-05, "9": 1.4031403175344117e-05} |
| Raw goal margin distribution | {"-1": 0.17432569163861636, "-10": 7.363768556095655e-07, "-11": 9.690213432321643e-08, "-12": 1.1720246692406799e-08, "-13": 1.310574526323461e-09, "-14": 1.3499731907194068e-10, "-15": 1.1423771895872948e-11, "-2": 0.1010735788678908, "-3": 0.042042940693235366, "-4": 0.013926831224614408, "-5": 0.003813698680907684, "-6": 0.0008876707370513018, "-7": 0.00017937969243555596, "-8": 3.199644116288846e-05, "-9": 5.1048519396426476e-06, "0": 0.2563382740386321, "1": 0.1948519360180005, "10": 2.1213624075324956e-06, "11": 3.103127034617381e-07, "12": 4.172097402750176e-08, "13": 5.185980532777807e-09, "14": 5.938076353464439e-10, "15": 5.5857517503748905e-11, "2": 0.12489371711769774, "3": 0.05774940402390145, "4": 0.021264648478429737, "5": 0.006472972258981241, "6": 0.0016747914927283437, "7": 0.00037621282104462276, "8": 7.459564385954622e-05, "9": 1.3229590907767522e-05} |
| Unadjusted home-win probability | 40.7% |
| Unadjusted draw probability | 25.6% |
| Unadjusted away-win probability | 33.6% |
| Raw p over 1 5 | 82.7% |
| Raw p under 3 5 | 62.2% |
| Raw p btts yes | 63.1% |
| P home draw | 67.8% |
| P draw away | 56.8% |
| P home away | 75.4% |
| Raw p home draw | 66.4% |
| Raw p draw away | 59.3% |
| Raw p home away | 74.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:10:44Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.66, "price": 2.42, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:11:33Z", "line": 0.25, "market_key": "spreads", "opposite_price": 1.91, "price": 2.0, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:11:33Z", "line": -0.25, "market_key": "spreads", "opposite_price": 2.0, "price": 1.91, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:10:44Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.42, "price": 1.66, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Everygame |
| Reference home odds | 2.05 |
| Reference draw odds | 3.75 |
| Reference away odds | 2.95 |
| Market reference 1x2 last update utc | 2026-10-21T17:11:39Z |
| Market reference home last update utc | 2026-10-21T17:11:39Z |
| Market reference draw last update utc | 2026-10-21T17:11:39Z |
| Market reference away last update utc | 2026-10-21T17:11:39Z |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 1.57 |
| Reference Under 2.5 odds | 2.40 |
| Market reference over 2 5 last update utc | 2026-10-21T17:11:38Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:11:38Z |
| Market best over 2 5 last update utc | 2026-10-21T17:10:44Z |
| Market best under 2 5 last update utc | 2026-10-21T17:10:44Z |
| Home probability edge | -2.5% |
| Draw probability edge | +1.0% |
| Away probability edge | +1.5% |
| Over 2.5 probability edge | -0.8% |
| Under 2.5 probability edge | +0.8% |
| Raw edge prob home | -0.0494 |
| Raw ev home | -0.1201 |
| Raw edge prob draw | 0.0201 |
| Raw ev draw | 0.0254 |
| Raw edge prob away | 0.0293 |
| Raw ev away | 0.0492 |

</details>


---

## 2026-10-25 — Manchester United vs Bournemouth

The model's most likely 1X2 outcome is **Manchester United win** at **50.2%**. Expected goals are 1.76 for Manchester United and 1.27 for Bournemouth (3.04 combined). The most likely exact score is 1-1 at 11.3%. Goal-market probabilities: at least one goal: 94.4%; Over 2.5 goals: 58.8%; Under 3.5 goals: 63.8%; Double Chance 1X: 74.6%; Double Chance X2: 49.8%; Double Chance 12 (either team wins): 75.6%; Under 4.5 goals: 80.7%; BTTS Yes (both teams score): 60.3%; BTTS No (at least one team does not score): 39.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Manchester United win | 50.2% | 1.99 |
| Draw | 24.4% | 4.10 |
| Bournemouth win | 25.4% | 3.94 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Manchester United expected goals | 1.76 |
| Bournemouth expected goals | 1.27 |
| Expected total goals | 3.04 |
| Over 0.5 | 94.4% |
| Under 0.5 | 5.6% |
| Over 1.5 | 81.7% |
| Under 1.5 | 18.3% |
| Over 2.5 | 58.8% |
| Under 2.5 | 41.2% |
| Over 3.5 | 36.2% |
| Under 3.5 | 63.8% |
| Over 4.5 | 19.3% |
| Under 4.5 | 80.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.33% |
| 2 | 2-1 | 9.93% |
| 3 | 1-0 | 7.85% |
| 4 | 2-0 | 7.81% |
| 5 | 1-2 | 6.52% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Manchester United win | 50.2% | 52.3% | 1.91 | -4.1% |
| Draw | 24.4% | 23.5% | 3.87 | -5.5% |
| Bournemouth win | 25.4% | 24.1% | 3.97 | +0.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T14:00:00+00:00 |
| Fixture id | 33fb7467b23c91d57dc976d9ab05ea97 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T17:11:34Z |
| Market best draw last update utc | 2026-10-21T17:11:34Z |
| Market best away last update utc | 2026-10-21T17:11:34Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Man United |
| Matched away-team name | Bournemouth |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.7643 |
| Dc lambda away | 1.2710 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T17:09:55.842067+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 60.3% |
| P btts no | 39.7% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.96 |
| Fair Over 1.5 odds | 1.22 |
| Fair Under 1.5 odds | 5.46 |
| Fair Over 2.5 odds | 1.70 |
| Fair Under 2.5 odds | 2.43 |
| Fair Over 3.5 odds | 2.76 |
| Fair Under 3.5 odds | 1.57 |
| Fair Over 4.5 odds | 5.19 |
| Fair Under 4.5 odds | 1.24 |
| Goal margin distribution | {"-1": 0.14373920133800208, "-10": 1.698214193689672e-07, "-11": 1.9298227148451376e-08, "-12": 2.01531822559234e-09, "-13": 1.9465361960050425e-10, "-14": 1.7479324362001796e-11, "-15": 1.4557298566701803e-12, "-16": 1.0142165293164626e-13, "-2": 0.07362726486263294, "-3": 0.026679369818509283, "-4": 0.007673821231419548, "-5": 0.0018211526482905442, "-6": 0.0003669118575244716, "-7": 6.412655812532974e-05, "-8": 9.887195960131453e-06, "-9": 1.3629563291121565e-06, "0": 0.24405862584271998, "1": 0.2227476503030397, "10": 4.949968115621567e-06, "11": 7.808657586418692e-07, "12": 1.1320135568091269e-07, "13": 1.5178173381594792e-08, "14": 1.8920416717577967e-09, "15": 2.1874386193912936e-10, "16": 2.1156060504151056e-11, "2": 0.15561675722187543, "3": 0.07827846323517793, "4": 0.03125557060028003, "5": 0.010297009986902682, "6": 0.0028798877568719065, "7": 0.0006987161397107885, "8": 0.00014954951762481206, "9": 2.8618235003304962e-05} |
| Raw goal margin distribution | {"-1": 0.150911591568755, "-10": 1.7829527672949605e-07, "-11": 2.0261182379745047e-08, "-12": 2.1158798581779194e-09, "-13": 2.0436656990638739e-10, "-14": 1.835151882340958e-11, "-15": 1.528368792363474e-12, "-16": 1.0648245517558799e-13, "-2": 0.07730116502558164, "-3": 0.028010634008567976, "-4": 0.008056734451476703, "-5": 0.0019120256832157463, "-6": 0.00038522025911540337, "-7": 6.732638597151611e-05, "-8": 1.0380553562329553e-05, "-9": 1.4309659922302886e-06, "0": 0.2528412989892235, "1": 0.21322634866755746, "10": 4.738382765784053e-06, "11": 7.474878154189707e-07, "12": 1.0836258745365129e-07, "13": 1.4529385540981419e-08, "14": 1.8111667469754264e-09, "15": 2.093937013982695e-10, "16": 2.025174913114895e-11, "2": 0.14896495154388364, "3": 0.074932466727425, "4": 0.02991955778456902, "5": 0.009856866452748709, "6": 0.0027567875581842637, "7": 0.0006688496647346643, "8": 0.00014315705483200803, "9": 2.739495454503355e-05} |
| Unadjusted home-win probability | 48.1% |
| Unadjusted draw probability | 25.3% |
| Unadjusted away-win probability | 26.7% |
| Raw p over 1 5 | 81.6% |
| Raw p under 3 5 | 63.9% |
| Raw p btts yes | 60.6% |
| P home draw | 74.6% |
| P draw away | 49.8% |
| P home away | 75.6% |
| Raw p home draw | 73.3% |
| Raw p draw away | 51.9% |
| Raw p home away | 74.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:10:44Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.44, "price": 3.1, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:11:34Z", "line": 0.5, "market_key": "spreads", "opposite_price": 1.92, "price": 1.99, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:11:34Z", "line": -0.5, "market_key": "spreads", "opposite_price": 1.99, "price": 1.92, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:10:44Z", "line": -0.0, "market_key": "spreads", "opposite_price": 3.1, "price": 1.44, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 1.88 |
| Reference draw odds | 4.10 |
| Reference away odds | 4.00 |
| Market reference 1x2 last update utc | 2026-10-21T17:11:38Z |
| Market reference home last update utc | 2026-10-21T17:11:38Z |
| Market reference draw last update utc | 2026-10-21T17:11:38Z |
| Market reference away last update utc | 2026-10-21T17:11:38Z |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 1.57 |
| Reference Under 2.5 odds | 2.40 |
| Market reference over 2 5 last update utc | 2026-10-21T17:11:38Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:11:38Z |
| Home probability edge | -2.1% |
| Draw probability edge | +0.9% |
| Away probability edge | +1.3% |
| Over 2.5 probability edge | -2.5% |
| Under 2.5 probability edge | +2.5% |
| Raw edge prob home | -0.0429 |
| Raw ev home | -0.0822 |
| Raw edge prob draw | 0.0176 |
| Raw ev draw | -0.0215 |
| Raw edge prob away | 0.0253 |
| Raw ev away | 0.0586 |

</details>


---

## 2026-10-25 — Sunderland vs Leeds United

The model's most likely 1X2 outcome is **Leeds United win** at **38.9%**. Expected goals are 1.07 for Sunderland and 1.21 for Leeds United (2.28 combined). The most likely exact score is 1-1 at 14.2%. Goal-market probabilities: at least one goal: 88.7%; Over 2.5 goals: 40.0%; Under 3.5 goals: 80.3%; Double Chance 1X: 61.1%; Double Chance X2: 69.2%; Double Chance 12 (either team wins): 69.7%; Under 4.5 goals: 91.8%; BTTS Yes (both teams score): 47.2%; BTTS No (at least one team does not score): 52.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Sunderland win | 30.8% | 3.25 |
| Draw | 30.3% | 3.30 |
| Leeds United win | 38.9% | 2.57 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Sunderland expected goals | 1.07 |
| Leeds United expected goals | 1.21 |
| Expected total goals | 2.28 |
| Over 0.5 | 88.7% |
| Under 0.5 | 11.3% |
| Over 1.5 | 67.7% |
| Under 1.5 | 32.3% |
| Over 2.5 | 40.0% |
| Under 2.5 | 60.0% |
| Over 3.5 | 19.7% |
| Under 3.5 | 80.3% |
| Over 4.5 | 8.2% |
| Under 4.5 | 91.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 14.22% |
| 2 | 0-1 | 11.44% |
| 3 | 0-0 | 11.25% |
| 4 | 1-0 | 9.65% |
| 5 | 1-2 | 8.18% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Sunderland win | 30.8% | 30.4% | 3.18 | -2.2% |
| Draw | 30.3% | 29.9% | 3.18 | -3.5% |
| Leeds United win | 38.9% | 39.7% | 2.47 | -3.9% |
| Over 2.5 | 40.0% | 44.3% | 2.19 | -12.4% |
| Under 2.5 | 60.0% | 55.7% | 1.79 | +7.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T16:30:00+00:00 |
| Fixture id | e82f6b60fa41b82c8510f5b67ce61849 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T17:11:33Z |
| Market best draw last update utc | 2026-10-21T17:11:33Z |
| Market best away last update utc | 2026-10-21T17:11:33Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 16.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Sunderland |
| Matched away-team name | Leeds |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.0683 |
| Dc lambda away | 1.2110 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T17:09:55.842067+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 47.2% |
| P btts no | 52.8% |
| Fair Over 0.5 odds | 1.13 |
| Fair Under 0.5 odds | 8.89 |
| Fair Over 1.5 odds | 1.48 |
| Fair Under 1.5 odds | 3.09 |
| Fair Over 2.5 odds | 2.50 |
| Fair Under 2.5 odds | 1.67 |
| Fair Over 3.5 odds | 5.08 |
| Fair Under 3.5 odds | 1.24 |
| Fair Over 4.5 odds | 12.23 |
| Fair Under 4.5 odds | 1.09 |
| Goal margin distribution | {"-1": 0.21580018817951516, "-10": 2.194148869486225e-07, "-11": 2.3923589621897427e-08, "-12": 2.3943485319444956e-09, "-13": 2.2068379815528534e-10, "-14": 1.7474837421661123e-11, "-2": 0.11538017784228785, "-3": 0.04228421224287042, "-4": 0.012053522431890952, "-5": 0.002802134839807365, "-6": 0.0005490425591547237, "-7": 9.287854440531152e-05, "-8": 1.381510602062697e-05, "-9": 1.832904511757469e-06, "0": 0.303468652023387, "1": 0.183400734566953, "10": 6.075852367871555e-08, "11": 5.8437830288728604e-09, "12": 5.159192395040487e-10, "13": 4.1946083944965776e-11, "14": 2.929953528484321e-12, "2": 0.08714839529530365, "3": 0.02817299713876811, "4": 0.007084274878557326, "5": 0.0014527706920574519, "6": 0.0002510965043255581, "7": 3.746939436519109e-05, "8": 4.9163422837562285e-06, "9": 5.753794491501682e-07} |
| Raw goal margin distribution | {"-1": 0.21160185641409807, "-10": 2.1514623223866687e-07, "-11": 2.3458162936685908e-08, "-12": 2.347767156905192e-09, "-13": 2.16390457135872e-10, "-14": 1.7134869390762887e-11, "-2": 0.11313548904094264, "-3": 0.041461584825663506, "-4": 0.011819024554303939, "-5": 0.0027476200972198434, "-6": 0.0005383610910980431, "-7": 9.107161853285517e-05, "-8": 1.3546337031413878e-05, "-9": 1.7972458716997208e-06, "0": 0.30790955936270403, "1": 0.18526516499725046, "10": 6.13761877285026e-08, "11": 5.903190244077383e-09, "12": 5.211640141881769e-10, "13": 4.237250293136441e-11, "14": 2.959739093579041e-12, "2": 0.08803433569529065, "3": 0.028459400534600898, "4": 0.007156292788907363, "5": 0.0014675393891017234, "6": 0.0002536491220384112, "7": 3.785030384859217e-05, "8": 4.966321244752412e-06, "9": 5.81228689375385e-07} |
| Unadjusted home-win probability | 31.1% |
| Unadjusted draw probability | 30.8% |
| Unadjusted away-win probability | 38.1% |
| Raw p over 1 5 | 67.6% |
| Raw p under 3 5 | 80.4% |
| Raw p btts yes | 47.3% |
| P home draw | 61.1% |
| P draw away | 69.2% |
| P home away | 69.7% |
| Raw p home draw | 61.9% |
| Raw p draw away | 68.9% |
| Raw p home away | 69.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:11:33Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.81, "price": 2.11, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:10:44Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.15, "price": 1.81, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:10:44Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.81, "price": 2.15, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:11:33Z", "line": 0.25, "market_key": "spreads", "opposite_price": 2.11, "price": 1.81, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Everygame |
| Reference home odds | 3.00 |
| Reference draw odds | 3.05 |
| Reference away odds | 2.35 |
| Market reference 1x2 last update utc | 2026-10-21T17:11:39Z |
| Market reference home last update utc | 2026-10-21T17:11:39Z |
| Market reference draw last update utc | 2026-10-21T17:11:39Z |
| Market reference away last update utc | 2026-10-21T17:11:39Z |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 2.14 |
| Reference Under 2.5 odds | 1.73 |
| Market reference over 2 5 last update utc | 2026-10-21T17:11:38Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:11:38Z |
| Market best over 2 5 last update utc | 2026-10-21T17:10:44Z |
| Market best under 2 5 last update utc | 2026-10-21T17:10:44Z |
| Home probability edge | +0.3% |
| Draw probability edge | +0.4% |
| Away probability edge | -0.8% |
| Over 2.5 probability edge | -4.3% |
| Under 2.5 probability edge | +4.3% |
| Raw edge prob home | 0.0063 |
| Raw ev home | -0.0120 |
| Raw edge prob draw | 0.0089 |
| Raw ev draw | -0.0208 |
| Raw edge prob away | -0.0151 |
| Raw ev away | -0.0579 |

</details>


---

## 2026-10-31 — Bournemouth vs Leeds United

The model's most likely 1X2 outcome is **Bournemouth win** at **43.3%**. Expected goals are 1.44 for Bournemouth and 1.22 for Leeds United (2.65 combined). The most likely exact score is 1-1 at 13.1%. Goal-market probabilities: at least one goal: 92.1%; Over 2.5 goals: 49.7%; Under 3.5 goals: 72.4%; Double Chance 1X: 70.7%; Double Chance X2: 56.7%; Double Chance 12 (either team wins): 72.6%; Under 4.5 goals: 86.9%; BTTS Yes (both teams score): 54.5%; BTTS No (at least one team does not score): 45.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bournemouth win | 43.3% | 2.31 |
| Draw | 27.4% | 3.65 |
| Leeds United win | 29.3% | 3.41 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Bournemouth expected goals | 1.44 |
| Leeds United expected goals | 1.22 |
| Expected total goals | 2.65 |
| Over 0.5 | 92.1% |
| Under 0.5 | 7.9% |
| Over 1.5 | 75.4% |
| Under 1.5 | 24.6% |
| Over 2.5 | 49.7% |
| Under 2.5 | 50.3% |
| Over 3.5 | 27.6% |
| Under 3.5 | 72.4% |
| Over 4.5 | 13.1% |
| Under 4.5 | 86.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.06% |
| 2 | 1-0 | 9.53% |
| 3 | 2-1 | 9.33% |
| 4 | 0-0 | 7.94% |
| 5 | 2-0 | 7.67% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bournemouth win | 43.3% | 45.6% | 2.15 | -6.9% |
| Draw | 27.4% | 26.6% | 3.37 | -7.8% |
| Leeds United win | 29.3% | 27.8% | 3.48 | +2.1% |
| Over 2.5 | 49.7% | 52.6% | 1.88 | -6.5% |
| Under 2.5 | 50.3% | 47.4% | 1.95 | -2.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-31T15:00:00+00:00 |
| Fixture id | a6c06eabdf4e6710354b6098d39449e7 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T17:11:33Z |
| Market best draw last update utc | 2026-10-21T17:11:33Z |
| Market best away last update utc | 2026-10-21T17:11:33Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Bournemouth |
| Matched away-team name | Leeds |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.4355 |
| Dc lambda away | 1.2156 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T17:09:55.842067+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 54.5% |
| P btts no | 45.5% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 12.59 |
| Fair Over 1.5 odds | 1.33 |
| Fair Under 1.5 odds | 4.07 |
| Fair Over 2.5 odds | 2.01 |
| Fair Under 2.5 odds | 1.99 |
| Fair Over 3.5 odds | 3.62 |
| Fair Under 3.5 odds | 1.38 |
| Fair Over 4.5 odds | 7.63 |
| Fair Under 4.5 odds | 1.15 |
| Goal margin distribution | {"-1": 0.16628385804531343, "-10": 1.5247555748609561e-07, "-11": 1.6631700649678853e-08, "-12": 1.6657986539919275e-09, "-13": 1.5331196287023993e-10, "-14": 1.1836099835404382e-11, "-2": 0.0854932403229295, "-3": 0.030538728218064096, "-4": 0.008572077052097766, "-5": 0.0019736190919734035, "-6": 0.0003843439555836201, "-7": 6.47702674058646e-05, "-8": 9.612873194963385e-06, "-9": 1.27401110786904e-06, "0": 0.2736295144905074, "1": 0.21997854330328684, "10": 8.928083534684502e-07, "11": 1.1501061240602829e-07, "12": 1.3604011939183661e-08, "13": 1.4786445360755296e-09, "14": 1.3481542952761984e-10, "2": 0.1322951317506241, "3": 0.05580926121514553, "4": 0.018500549755229027, "5": 0.005030430424583732, "6": 0.0011569247332711198, "7": 0.00023025230234981407, "8": 4.035754560271482e-05, "9": 6.316667086565364e-06} |
| Raw goal margin distribution | {"-1": 0.17487288188354858, "-10": 1.6035134418837053e-07, "-11": 1.7490774254475503e-08, "-12": 1.7518417884069212e-09, "-13": 1.612309522373273e-10, "-14": 1.2447467317690701e-11, "-2": 0.08990920401160878, "-3": 0.0321161384834842, "-4": 0.009014848677733202, "-5": 0.0020755620083082894, "-6": 0.000404196390061594, "-7": 6.811583189599227e-05, "-8": 1.0109404836675546e-05, "-9": 1.3398173256480477e-06, "0": 0.2810553624448693, "1": 0.20851009872078596, "10": 8.462623450678491e-07, "11": 1.0901460563658844e-07, "12": 1.2894775235087907e-08, "13": 1.4015563225409026e-09, "14": 1.27786910931277e-10, "2": 0.12539800731187883, "3": 0.05289968008134478, "4": 0.01753603509653743, "5": 0.004768172062090052, "6": 0.001096609181625014, "7": 0.00021824824172717684, "8": 3.825353005519678e-05, "9": 5.987351575422512e-06} |
| Unadjusted home-win probability | 41.0% |
| Unadjusted draw probability | 28.1% |
| Unadjusted away-win probability | 30.8% |
| Raw p over 1 5 | 75.3% |
| Raw p under 3 5 | 72.5% |
| Raw p btts yes | 54.7% |
| P home draw | 70.7% |
| P draw away | 56.7% |
| P home away | 72.6% |
| Raw p home draw | 69.2% |
| Raw p draw away | 59.0% |
| Raw p home away | 71.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:10:44Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.62, "price": 2.52, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:11:33Z", "line": 0.25, "market_key": "spreads", "opposite_price": 1.85, "price": 2.0, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:11:33Z", "line": -0.25, "market_key": "spreads", "opposite_price": 2.0, "price": 1.85, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:10:44Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.52, "price": 1.62, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 2.14 |
| Reference draw odds | 3.60 |
| Reference away odds | 3.45 |
| Market reference 1x2 last update utc | 2026-10-21T17:11:38Z |
| Market reference home last update utc | 2026-10-21T17:11:38Z |
| Market reference draw last update utc | 2026-10-21T17:11:38Z |
| Market reference away last update utc | 2026-10-21T17:11:38Z |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 1.79 |
| Reference Under 2.5 odds | 1.97 |
| Market reference over 2 5 last update utc | 2026-10-21T17:11:38Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:11:38Z |
| Market best over 2 5 last update utc | 2026-10-21T17:11:33Z |
| Market best under 2 5 last update utc | 2026-10-21T17:11:33Z |
| Home probability edge | -2.3% |
| Draw probability edge | +0.7% |
| Away probability edge | +1.5% |
| Over 2.5 probability edge | -2.9% |
| Under 2.5 probability edge | +2.9% |
| Raw edge prob home | -0.0452 |
| Raw ev home | -0.1175 |
| Raw edge prob draw | 0.0149 |
| Raw ev draw | -0.0528 |
| Raw edge prob away | 0.0303 |
| Raw ev away | 0.0735 |

</details>


---

## 2026-10-31 — Brentford vs Nottingham Forest

The model's most likely 1X2 outcome is **Brentford win** at **48.4%**. Expected goals are 1.60 for Brentford and 1.08 for Nottingham Forest (2.68 combined). The most likely exact score is 1-1 at 12.4%. Goal-market probabilities: at least one goal: 92.4%; Over 2.5 goals: 50.5%; Under 3.5 goals: 71.8%; Double Chance 1X: 74.3%; Double Chance X2: 51.6%; Double Chance 12 (either team wins): 74.0%; Under 4.5 goals: 86.5%; BTTS Yes (both teams score): 53.6%; BTTS No (at least one team does not score): 46.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Brentford win | 48.4% | 2.07 |
| Draw | 26.0% | 3.85 |
| Nottingham Forest win | 25.7% | 3.89 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Brentford expected goals | 1.60 |
| Nottingham Forest expected goals | 1.08 |
| Expected total goals | 2.68 |
| Over 0.5 | 92.4% |
| Under 0.5 | 7.6% |
| Over 1.5 | 75.9% |
| Under 1.5 | 24.1% |
| Over 2.5 | 50.5% |
| Under 2.5 | 49.5% |
| Over 3.5 | 28.2% |
| Under 3.5 | 71.8% |
| Over 4.5 | 13.5% |
| Under 4.5 | 86.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.40% |
| 2 | 1-0 | 9.92% |
| 3 | 2-1 | 9.49% |
| 4 | 2-0 | 8.77% |
| 5 | 0-0 | 7.60% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Brentford win | 48.4% | 48.4% | 2.01 | -2.8% |
| Draw | 26.0% | 24.9% | 3.81 | -1.0% |
| Nottingham Forest win | 25.7% | 26.7% | 3.42 | -12.2% |
| Over 2.5 | 50.5% | 56.4% | 1.78 | -10.1% |
| Under 2.5 | 49.5% | 43.6% | 2.21 | +9.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-31T15:00:00+00:00 |
| Fixture id | b9254b648ca25ce7831988b53ed17c3c |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T17:11:33Z |
| Market best draw last update utc | 2026-10-21T17:11:33Z |
| Market best away last update utc | 2026-10-21T17:11:33Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Brentford |
| Matched away-team name | Nott'm Forest |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.5978 |
| Dc lambda away | 1.0815 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T17:09:55.842067+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 53.6% |
| P btts no | 46.4% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.15 |
| Fair Over 1.5 odds | 1.32 |
| Fair Under 1.5 odds | 4.14 |
| Fair Over 2.5 odds | 1.98 |
| Fair Under 2.5 odds | 2.02 |
| Fair Over 3.5 odds | 3.55 |
| Fair Under 3.5 odds | 1.39 |
| Fair Over 4.5 odds | 7.39 |
| Fair Under 4.5 odds | 1.16 |
| Goal margin distribution | {"-1": 0.15518922902686463, "-10": 5.037034187659905e-08, "-11": 4.889173398995562e-09, "-12": 4.3586503714989047e-10, "-13": 3.5915436032621935e-11, "-14": 2.7369155025088693e-12, "-15": 1.7695239963317205e-13, "-2": 0.07166005669231403, "-3": 0.022799500129050604, "-4": 0.005698121366148297, "-5": 0.0011678570477391475, "-6": 0.0002024281903695179, "-7": 3.036087246894753e-05, "-8": 4.010087513666712e-06, "-9": 4.72952577197648e-07, "0": 0.2597404476914682, "1": 0.22566796070743816, "10": 2.400312886223368e-06, "11": 3.441986161063861e-07, "12": 4.533216227715707e-08, "13": 5.518439251993476e-09, "14": 6.212654952771661e-10, "15": 5.934074880524509e-11, "2": 0.15049578382542594, "3": 0.07073807427718212, "4": 0.026118024449121032, "5": 0.007908225351227302, "6": 0.0020250747782636445, "7": 0.00044870926922632596, "8": 8.755588971588365e-05, "9": 1.5255618965630087e-05} |
| Raw goal margin distribution | {"-1": 0.14910819004690593, "-10": 4.8396596570264545e-08, "-11": 4.6975927448129036e-09, "-12": 4.187858087940953e-10, "-13": 3.450810146522887e-11, "-14": 2.6296703672635072e-12, "-15": 1.700185779593736e-13, "-2": 0.06885208090182553, "-3": 0.021906109203161477, "-4": 0.005474842351506855, "-5": 0.001122094952812496, "-6": 0.0001944961082011965, "-7": 2.9171191650846013e-05, "-8": 3.852953551235392e-06, "-9": 4.5442008576351016e-07, "0": 0.27051966196368116, "1": 0.22533262942808835, "10": 2.3967461415758162e-06, "11": 3.436871542137561e-07, "12": 4.526480095601765e-08, "13": 5.510239127843888e-09, "14": 6.203423258884141e-10, "15": 5.925257142662183e-11, "2": 0.15027215463336552, "3": 0.07063296104413058, "4": 0.026079214373799932, "5": 0.007896474124708038, "6": 0.0020220656186379473, "7": 0.0004480425097411332, "8": 8.742578605198291e-05, "9": 1.523294988044413e-05} |
| Unadjusted home-win probability | 48.3% |
| Unadjusted draw probability | 27.1% |
| Unadjusted away-win probability | 24.7% |
| Raw p over 1 5 | 75.8% |
| Raw p under 3 5 | 71.9% |
| Raw p btts yes | 53.8% |
| P home draw | 74.3% |
| P draw away | 51.6% |
| P home away | 74.0% |
| Raw p home draw | 75.3% |
| Raw p draw away | 51.7% |
| Raw p home away | 72.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:10:44Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.55, "price": 2.71, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:11:33Z", "line": 0.5, "market_key": "spreads", "opposite_price": 2.02, "price": 1.84, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:11:33Z", "line": -0.5, "market_key": "spreads", "opposite_price": 1.84, "price": 2.02, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:10:44Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.71, "price": 1.55, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 2.02 |
| Reference draw odds | 3.85 |
| Reference away odds | 3.60 |
| Market reference 1x2 last update utc | 2026-10-21T17:11:38Z |
| Market reference home last update utc | 2026-10-21T17:11:38Z |
| Market reference draw last update utc | 2026-10-21T17:11:38Z |
| Market reference away last update utc | 2026-10-21T17:11:38Z |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 1.68 |
| Reference Under 2.5 odds | 2.12 |
| Market reference over 2 5 last update utc | 2026-10-21T17:11:38Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:11:38Z |
| Market best over 2 5 last update utc | 2026-10-21T17:10:44Z |
| Market best under 2 5 last update utc | 2026-10-21T17:10:44Z |
| Home probability edge | -0.1% |
| Draw probability edge | +1.1% |
| Away probability edge | -1.0% |
| Over 2.5 probability edge | -5.9% |
| Under 2.5 probability edge | +5.9% |
| Raw edge prob home | -0.0014 |
| Raw ev home | -0.0296 |
| Raw edge prob draw | 0.0216 |
| Raw ev draw | 0.0307 |
| Raw edge prob away | -0.0201 |
| Raw ev away | -0.1563 |

</details>


---

## 2026-10-31 — Chelsea vs Manchester United

The model's most likely 1X2 outcome is **Chelsea win** at **48.0%**. Expected goals are 1.83 for Chelsea and 1.49 for Manchester United (3.33 combined). The most likely exact score is 1-1 at 10.5%. Goal-market probabilities: at least one goal: 95.6%; Over 2.5 goals: 64.8%; Under 3.5 goals: 57.3%; Double Chance 1X: 71.9%; Double Chance X2: 52.0%; Double Chance 12 (either team wins): 76.2%; Under 4.5 goals: 75.6%; BTTS Yes (both teams score): 65.8%; BTTS No (at least one team does not score): 34.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Chelsea win | 48.0% | 2.08 |
| Draw | 23.8% | 4.20 |
| Manchester United win | 28.1% | 3.55 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Chelsea expected goals | 1.83 |
| Manchester United expected goals | 1.49 |
| Expected total goals | 3.33 |
| Over 0.5 | 95.6% |
| Under 0.5 | 4.4% |
| Over 1.5 | 85.4% |
| Under 1.5 | 14.6% |
| Over 2.5 | 64.8% |
| Under 2.5 | 35.2% |
| Over 3.5 | 42.7% |
| Under 3.5 | 57.3% |
| Over 4.5 | 24.4% |
| Under 4.5 | 75.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.47% |
| 2 | 2-1 | 9.65% |
| 3 | 1-2 | 6.72% |
| 4 | 2-2 | 6.58% |
| 5 | 2-0 | 6.45% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Chelsea win | 48.0% | 51.2% | 1.88 | -9.7% |
| Draw | 23.8% | 23.3% | 3.92 | -6.7% |
| Manchester United win | 28.1% | 25.5% | 3.78 | +6.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-31T12:30:00+00:00 |
| Fixture id | 6601f69175a02f03fb7065aacb538e01 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T17:11:33Z |
| Market best draw last update utc | 2026-10-21T17:11:33Z |
| Market best away last update utc | 2026-10-21T17:11:33Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Chelsea |
| Matched away-team name | Man United |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.8317 |
| Dc lambda away | 1.4947 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T17:09:55.842067+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 65.8% |
| P btts no | 34.2% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 22.89 |
| Fair Over 1.5 odds | 1.17 |
| Fair Under 1.5 odds | 6.86 |
| Fair Over 2.5 odds | 1.54 |
| Fair Under 2.5 odds | 2.84 |
| Fair Over 3.5 odds | 2.34 |
| Fair Under 3.5 odds | 1.74 |
| Fair Over 4.5 odds | 4.10 |
| Fair Under 4.5 odds | 1.32 |
| Goal margin distribution | {"-1": 0.14699907986760016, "-10": 6.446785751467214e-07, "-11": 8.585125230143313e-08, "-12": 1.0511876852753257e-08, "-13": 1.1909172577362406e-09, "-14": 1.2544452329194263e-10, "-15": 1.2218405977575894e-11, "-16": 9.746680473341865e-13, "-2": 0.0839895733916946, "-3": 0.03479688578499518, "-4": 0.011547286049248142, "-5": 0.003178897710661855, "-6": 0.0007455205666027297, "-7": 0.00015202495439984023, "-8": 2.739287545093789e-05, "-9": 4.418224303537358e-06, "0": 0.23807300049136712, "1": 0.21309322591890914, "10": 5.7653031845444815e-06, "11": 9.408280422444122e-07, "12": 1.411655059005389e-07, "13": 1.9598129299704244e-08, "14": 2.529702446966715e-09, "15": 3.0193745637857903e-10, "16": 2.9515073911863504e-11, "2": 0.14771569593657188, "3": 0.07499397138002836, "4": 0.030496542511909426, "5": 0.010288023310419182, "6": 0.0029566486608792303, "7": 0.000738821761493015, "8": 0.00016313499175822063, "9": 3.22434844313205e-05} |
| Raw goal margin distribution | {"-1": 0.16076503177789342, "-10": 7.050504786379498e-07, "-11": 9.38909231053894e-08, "-12": 1.1496277512759158e-08, "-13": 1.302442511594301e-09, "-14": 1.3719196604193741e-10, "-15": 1.3362617147191667e-11, "-16": 1.0659423157186318e-12, "-2": 0.09185490444898751, "-3": 0.038055492959786004, "-4": 0.012628649174728395, "-5": 0.0034765904108619303, "-6": 0.0008153359714150001, "-7": 0.00016626156195764027, "-8": 2.9958122842158985e-05, "-9": 4.831975623247418e-06, "0": 0.24353411637025957, "1": 0.19898244355699973, "10": 5.3835316001277695e-06, "11": 8.785275177352746e-07, "12": 1.318176924157059e-07, "13": 1.8300364267258193e-08, "14": 2.3621885313290554e-09, "15": 2.81943513748568e-10, "16": 2.7560620490972195e-11, "2": 0.13793413658474082, "3": 0.07002795895032525, "4": 0.028477097396652547, "5": 0.009606762527766148, "6": 0.002760862869968288, "7": 0.0006898978548990169, "8": 0.0001523323848035156, "9": 3.010835888034162e-05} |
| Unadjusted home-win probability | 44.9% |
| Unadjusted draw probability | 24.4% |
| Unadjusted away-win probability | 30.8% |
| Raw p over 1 5 | 85.3% |
| Raw p under 3 5 | 57.5% |
| Raw p btts yes | 66.0% |
| P home draw | 71.9% |
| P draw away | 52.0% |
| P home away | 76.2% |
| Raw p home draw | 69.2% |
| Raw p draw away | 55.1% |
| Raw p home away | 75.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:10:44Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.5, "price": 2.89, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:11:33Z", "line": 0.5, "market_key": "spreads", "opposite_price": 1.88, "price": 1.97, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:11:33Z", "line": -0.5, "market_key": "spreads", "opposite_price": 1.97, "price": 1.88, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:10:44Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.89, "price": 1.5, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 1.91 |
| Reference draw odds | 4.10 |
| Reference away odds | 3.75 |
| Market reference 1x2 last update utc | 2026-10-21T17:11:38Z |
| Market reference home last update utc | 2026-10-21T17:11:38Z |
| Market reference draw last update utc | 2026-10-21T17:11:38Z |
| Market reference away last update utc | 2026-10-21T17:11:38Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.55 |
| Reference Under 2.5 odds | 2.40 |
| Market reference over 2 5 last update utc | 2026-10-21T17:11:33Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:11:33Z |
| Home probability edge | -3.2% |
| Draw probability edge | +0.5% |
| Away probability edge | +2.6% |
| Over 2.5 probability edge | +3.0% |
| Under 2.5 probability edge | -3.0% |
| Raw edge prob home | -0.0636 |
| Raw ev home | -0.1565 |
| Raw edge prob draw | 0.0109 |
| Raw ev draw | -0.0453 |
| Raw edge prob away | 0.0527 |
| Raw ev away | 0.1635 |

</details>


---

## 2026-10-31 — Coventry City vs Sunderland

The model's most likely 1X2 outcome is **Sunderland win** at **38.2%**. Expected goals are 1.15 for Coventry City and 1.24 for Sunderland (2.39 combined). The most likely exact score is 1-1 at 13.5%. Goal-market probabilities: at least one goal: 90.2%; Over 2.5 goals: 43.4%; Under 3.5 goals: 77.9%; Double Chance 1X: 61.8%; Double Chance X2: 66.8%; Double Chance 12 (either team wins): 71.4%; Under 4.5 goals: 90.3%; BTTS Yes (both teams score): 49.5%; BTTS No (at least one team does not score): 50.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Coventry City win | 33.2% | 3.01 |
| Draw | 28.6% | 3.50 |
| Sunderland win | 38.2% | 2.62 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Coventry City expected goals | 1.15 |
| Sunderland expected goals | 1.24 |
| Expected total goals | 2.39 |
| Over 0.5 | 90.2% |
| Under 0.5 | 9.8% |
| Over 1.5 | 70.3% |
| Under 1.5 | 29.7% |
| Over 2.5 | 43.4% |
| Under 2.5 | 56.6% |
| Over 3.5 | 22.1% |
| Under 3.5 | 77.9% |
| Over 4.5 | 9.7% |
| Under 4.5 | 90.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.54% |
| 2 | 0-1 | 10.45% |
| 3 | 0-0 | 9.80% |
| 4 | 1-0 | 9.47% |
| 5 | 1-2 | 8.33% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Coventry City win | 33.2% | 33.6% | 2.74 | -9.0% |
| Draw | 28.6% | 27.1% | 3.43 | -2.0% |
| Sunderland win | 38.2% | 39.2% | 2.54 | -2.9% |
| Over 2.5 | 43.4% | 51.0% | 1.92 | -16.7% |
| Under 2.5 | 56.6% | 49.0% | 1.92 | +8.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-31T15:00:00+00:00 |
| Fixture id | d20fbb0cd5ad9369b8ed6f2c4a198619 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T17:11:33Z |
| Market best draw last update utc | 2026-10-21T17:11:33Z |
| Market best away last update utc | 2026-10-21T17:11:33Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Coventry |
| Matched away-team name | Sunderland |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.1510 |
| Dc lambda away | 1.2428 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T17:09:55.842067+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 49.5% |
| P btts no | 50.5% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 10.20 |
| Fair Over 1.5 odds | 1.42 |
| Fair Under 1.5 odds | 3.36 |
| Fair Over 2.5 odds | 2.31 |
| Fair Under 2.5 odds | 1.77 |
| Fair Over 3.5 odds | 4.53 |
| Fair Under 3.5 odds | 1.28 |
| Fair Over 4.5 odds | 10.36 |
| Fair Under 4.5 odds | 1.11 |
| Goal margin distribution | {"-1": 0.21028945647378244, "-10": 2.584487665591585e-07, "-11": 2.888957173010166e-08, "-12": 2.96454231093412e-09, "-13": 2.7998509090216095e-10, "-14": 2.255049487110117e-11, "-2": 0.11371767388813683, "-3": 0.0423806196639164, "-4": 0.01232499261917184, "-5": 0.0029283537647140662, "-6": 0.0005870529090760366, "-7": 0.00010167937955439799, "-8": 1.549281264325346e-05, "-9": 2.1063284395901935e-06, "0": 0.28558893483349584, "1": 0.19127015711289924, "10": 1.183843487669699e-07, "11": 1.2255764569873796e-08, "12": 1.1647599776036149e-09, "13": 1.0188099378344478e-10, "14": 7.59965406816671e-12, "2": 0.09623032451519514, "3": 0.03321473299205519, "4": 0.00894601478049613, "5": 0.0019685478015877655, "6": 0.00036549307154728046, "7": 5.8629241012453136e-05, "8": 8.273535483050334e-06, "9": 1.0417570228386821e-06} |
| Raw goal margin distribution | {"-1": 0.204758197653868, "-10": 2.516507699144499e-07, "-11": 2.812968723034977e-08, "-12": 2.8865657395960872e-09, "-13": 2.726206227568442e-10, "-14": 2.1957347569563655e-11, "-2": 0.11072654966716418, "-3": 0.041265879152241225, "-4": 0.012000807444730276, "-5": 0.0028513290633309808, "-6": 0.0005716116138464391, "-7": 9.900489946207908e-05, "-8": 1.5085304069047023e-05, "-9": 2.0509255299318454e-06, "0": 0.29997654490451237, "1": 0.18877565772125304, "10": 1.1684040855989758e-07, "11": 1.2095927835669285e-08, "12": 1.1495694580818942e-09, "13": 1.0055228636327412e-10, "14": 7.500541207405196e-12, "2": 0.09497531176472522, "3": 0.03278155443198601, "4": 0.008829343007102676, "5": 0.001942874474563787, "6": 0.0003607263988034114, "7": 5.786461255056549e-05, "8": 8.165634022933634e-06, "9": 1.0281706782727576e-06} |
| Unadjusted home-win probability | 32.8% |
| Unadjusted draw probability | 30.0% |
| Unadjusted away-win probability | 37.2% |
| Raw p over 1 5 | 70.2% |
| Raw p under 3 5 | 78.0% |
| Raw p btts yes | 49.8% |
| P home draw | 61.8% |
| P draw away | 66.8% |
| P home away | 71.4% |
| Raw p home draw | 62.8% |
| Raw p draw away | 67.2% |
| Raw p home away | 70.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:10:44Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.12, "price": 1.84, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:11:33Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.0, "price": 1.85, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:10:44Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.84, "price": 2.12, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:11:33Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.85, "price": 2.0, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 2.88 |
| Reference draw odds | 3.55 |
| Reference away odds | 2.48 |
| Market reference 1x2 last update utc | 2026-10-21T17:11:38Z |
| Market reference home last update utc | 2026-10-21T17:11:38Z |
| Market reference draw last update utc | 2026-10-21T17:11:38Z |
| Market reference away last update utc | 2026-10-21T17:11:38Z |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 1.85 |
| Reference Under 2.5 odds | 1.92 |
| Market reference over 2 5 last update utc | 2026-10-21T17:11:38Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:11:38Z |
| Market best over 2 5 last update utc | 2026-10-21T17:11:33Z |
| Market best under 2 5 last update utc | 2026-10-21T17:11:33Z |
| Home probability edge | -0.4% |
| Draw probability edge | +1.4% |
| Away probability edge | -1.0% |
| Over 2.5 probability edge | -7.6% |
| Under 2.5 probability edge | +7.6% |
| Raw edge prob home | -0.0087 |
| Raw ev home | -0.1020 |
| Raw edge prob draw | 0.0288 |
| Raw ev draw | 0.0289 |
| Raw edge prob away | -0.0201 |
| Raw ev away | -0.0544 |

</details>


---

## 2026-10-31 — Hull City vs Ipswich Town

The model's most likely 1X2 outcome is **Hull City win** at **48.6%**. Expected goals are 1.86 for Hull City and 0.87 for Ipswich Town (2.73 combined). The most likely exact score is 1-1 at 12.2%. Goal-market probabilities: at least one goal: 92.1%; Over 2.5 goals: 50.1%; Under 3.5 goals: 72.0%; Double Chance 1X: 74.2%; Double Chance X2: 51.4%; Double Chance 12 (either team wins): 74.4%; Under 4.5 goals: 86.5%; BTTS Yes (both teams score): 51.2%; BTTS No (at least one team does not score): 48.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Hull City win | 48.6% | 2.06 |
| Draw | 25.6% | 3.90 |
| Ipswich Town win | 25.8% | 3.88 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Hull City expected goals | 1.86 |
| Ipswich Town expected goals | 0.87 |
| Expected total goals | 2.73 |
| Over 0.5 | 92.1% |
| Under 0.5 | 7.9% |
| Over 1.5 | 75.5% |
| Under 1.5 | 24.5% |
| Over 2.5 | 50.1% |
| Under 2.5 | 49.9% |
| Over 3.5 | 28.0% |
| Under 3.5 | 72.0% |
| Over 4.5 | 13.5% |
| Under 4.5 | 86.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.23% |
| 2 | 2-0 | 9.17% |
| 3 | 1-0 | 9.08% |
| 4 | 2-1 | 7.98% |
| 5 | 0-0 | 7.93% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Hull City win | 48.6% | 37.5% | 2.63 | +27.9% |
| Draw | 25.6% | 27.2% | 3.41 | -12.6% |
| Ipswich Town win | 25.8% | 35.4% | 2.66 | -31.5% |
| Over 2.5 | 50.1% | 54.2% | 1.81 | -9.3% |
| Under 2.5 | 49.9% | 45.8% | 2.17 | +8.2% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-31T15:00:00+00:00 |
| Fixture id | 1ec76c009147b63859f68c6b5a1dd77b |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T17:11:33Z |
| Market best draw last update utc | 2026-10-21T17:11:33Z |
| Market best away last update utc | 2026-10-21T17:11:33Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Hull |
| Matched away-team name | Ipswich |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.8623 |
| Dc lambda away | 0.8711 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T17:09:55.842067+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 51.2% |
| P btts no | 48.8% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 12.62 |
| Fair Over 1.5 odds | 1.33 |
| Fair Under 1.5 odds | 4.08 |
| Fair Over 2.5 odds | 1.99 |
| Fair Under 2.5 odds | 2.01 |
| Fair Over 3.5 odds | 3.57 |
| Fair Under 3.5 odds | 1.39 |
| Fair Over 4.5 odds | 7.43 |
| Fair Under 4.5 odds | 1.16 |
| Goal margin distribution | {"-1": 0.17120330681014562, "-10": 8.316481025860852e-09, "-11": 6.506515595129813e-10, "-12": 4.6748324468724617e-11, "-13": 3.1049073767557717e-12, "-14": 1.916839784946285e-13, "-15": 1.1008967457714133e-14, "-16": 5.441747091707198e-16, "-2": 0.06538958047297687, "-3": 0.016869050909472983, "-4": 0.00341059230886383, "-5": 0.00056473983684979, "-6": 7.90199063229868e-05, "-7": 9.56211333944003e-06, "-8": 1.0186079490750363e-06, "-9": 9.686551669455974e-08, "0": 0.25624415060785716, "1": 0.1953793431552301, "10": 8.46386969803145e-06, "11": 1.415742149685756e-06, "12": 2.1747435733684523e-07, "13": 3.088139958629794e-08, "14": 4.076058983110036e-09, "15": 5.005039996629992e-10, "16": 5.289390581958393e-11, "2": 0.1524359367842936, "3": 0.0840767239860864, "4": 0.036343040666358024, "5": 0.012866078447286145, "6": 0.0038489352125656026, "7": 0.00099578205774744, "8": 0.00022678994207101628, "9": 4.610969481658743e-05} |
| Raw goal margin distribution | {"-1": 0.10737188082597597, "-10": 5.215764965278724e-09, "-11": 4.0806268879336396e-10, "-12": 2.931868324971221e-11, "-13": 1.9472739811177417e-12, "-14": 1.2021654066529117e-13, "-15": 6.904384990633139e-15, "-16": 3.412846580491757e-16, "-2": 0.041009734990638445, "-3": 0.010579595439168926, "-4": 0.0021389873697907793, "-5": 0.0003541822853174199, "-6": 4.9558131339135594e-05, "-7": 5.996975835667603e-06, "-8": 6.38830250152594e-07, "-9": 6.07501858956997e-08, "0": 0.24055572740617173, "1": 0.24026520582896002, "10": 1.0408333666529617e-05, "11": 1.7409904931696305e-06, "12": 2.674362621157129e-07, "13": 3.7975999448381905e-08, "14": 5.012480514738072e-09, "15": 6.154882832301568e-10, "16": 6.504559265890727e-11, "2": 0.18745611043491844, "3": 0.10339225768556366, "4": 0.04469238152374774, "5": 0.015821892613758652, "6": 0.004733178012246028, "7": 0.0012245500327810346, "8": 0.0002788919812691674, "9": 5.670279742426982e-05} |
| Unadjusted home-win probability | 59.8% |
| Unadjusted draw probability | 24.1% |
| Unadjusted away-win probability | 16.2% |
| Raw p over 1 5 | 76.7% |
| Raw p under 3 5 | 70.7% |
| Raw p btts yes | 50.1% |
| P home draw | 74.2% |
| P draw away | 51.4% |
| P home away | 74.4% |
| Raw p home draw | 83.8% |
| Raw p draw away | 40.2% |
| Raw p home away | 75.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:10:44Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.96, "price": 1.98, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:11:33Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.92, "price": 1.93, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:10:44Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.98, "price": 1.96, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:11:33Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.93, "price": 1.92, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 2.60 |
| Reference draw odds | 3.55 |
| Reference away odds | 2.75 |
| Market reference 1x2 last update utc | 2026-10-21T17:11:38Z |
| Market reference home last update utc | 2026-10-21T17:11:38Z |
| Market reference draw last update utc | 2026-10-21T17:11:38Z |
| Market reference away last update utc | 2026-10-21T17:11:38Z |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 1.75 |
| Reference Under 2.5 odds | 2.04 |
| Market reference over 2 5 last update utc | 2026-10-21T17:11:38Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:11:38Z |
| Market best over 2 5 last update utc | 2026-10-21T17:10:44Z |
| Market best under 2 5 last update utc | 2026-10-21T17:10:44Z |
| Home probability edge | +11.2% |
| Draw probability edge | -1.6% |
| Away probability edge | -9.6% |
| Over 2.5 probability edge | -4.1% |
| Under 2.5 probability edge | +4.1% |
| Raw edge prob home | 0.2234 |
| Raw ev home | 0.5726 |
| Raw edge prob draw | -0.0314 |
| Raw ev draw | -0.1797 |
| Raw edge prob away | -0.1920 |
| Raw ev away | -0.5704 |

</details>


---

## 2026-10-31 — Manchester City vs Brighton and Hove Albion

The model's most likely 1X2 outcome is **Manchester City win** at **56.5%**. Expected goals are 1.97 for Manchester City and 1.14 for Brighton and Hove Albion (3.11 combined). The most likely exact score is 1-1 at 10.6%. Goal-market probabilities: at least one goal: 94.8%; Over 2.5 goals: 60.3%; Under 3.5 goals: 62.2%; Double Chance 1X: 79.3%; Double Chance X2: 43.5%; Double Chance 12 (either team wins): 77.2%; Under 4.5 goals: 79.5%; BTTS Yes (both teams score): 59.2%; BTTS No (at least one team does not score): 40.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Manchester City win | 56.5% | 1.77 |
| Draw | 22.8% | 4.39 |
| Brighton and Hove Albion win | 20.7% | 4.84 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Manchester City expected goals | 1.97 |
| Brighton and Hove Albion expected goals | 1.14 |
| Expected total goals | 3.11 |
| Over 0.5 | 94.8% |
| Under 0.5 | 5.2% |
| Over 1.5 | 82.6% |
| Under 1.5 | 17.4% |
| Over 2.5 | 60.3% |
| Under 2.5 | 39.7% |
| Over 3.5 | 37.8% |
| Under 3.5 | 62.2% |
| Over 4.5 | 20.5% |
| Under 4.5 | 79.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.58% |
| 2 | 2-1 | 10.01% |
| 3 | 2-0 | 8.78% |
| 4 | 1-0 | 8.02% |
| 5 | 3-1 | 6.57% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Manchester City win | 56.5% | 57.4% | 1.67 | -5.6% |
| Draw | 22.8% | 22.1% | 4.41 | +0.5% |
| Brighton and Hove Albion win | 20.7% | 20.6% | 4.40 | -9.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-31T15:00:00+00:00 |
| Fixture id | 7df53f9af95d5a4e13b504882078dab8 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T17:11:34Z |
| Market best draw last update utc | 2026-10-21T17:11:34Z |
| Market best away last update utc | 2026-10-21T17:11:34Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Man City |
| Matched away-team name | Brighton |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.9682 |
| Dc lambda away | 1.1397 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T17:09:55.842067+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 59.2% |
| P btts no | 40.8% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 19.24 |
| Fair Over 1.5 odds | 1.21 |
| Fair Under 1.5 odds | 5.75 |
| Fair Over 2.5 odds | 1.66 |
| Fair Under 2.5 odds | 2.52 |
| Fair Over 3.5 odds | 2.65 |
| Fair Under 3.5 odds | 1.61 |
| Fair Over 4.5 odds | 4.89 |
| Fair Under 4.5 odds | 1.26 |
| Goal margin distribution | {"-1": 0.1243881761959399, "-10": 5.551036200555866e-08, "-11": 5.656823599419173e-09, "-12": 5.297523419621802e-10, "-13": 4.588450781173978e-11, "-14": 3.694899729260274e-12, "-15": 2.75950469354962e-13, "-16": 1.7239984188303797e-14, "-2": 0.0575549600174748, "-3": 0.018701394866187965, "-4": 0.004823603936352814, "-5": 0.0010265310738055363, "-6": 0.00018546244384967826, "-7": 2.9067149205890462e-05, "-8": 4.018918351386013e-06, "-9": 4.96810104672146e-07, "0": 0.22793831619215385, "1": 0.2255910223405108, "10": 1.3347326341834936e-05, "11": 2.3488539745443887e-06, "12": 3.798563840774525e-07, "13": 5.6816671061697135e-08, "14": 7.900881106889095e-09, "15": 1.018983540362692e-09, "16": 1.0993501941818348e-10, "2": 0.1749837326583853, "3": 0.09818656854989888, "4": 0.04373336408371354, "5": 0.016072243649729635, "6": 0.005014452801955642, "7": 0.001357166628170497, "8": 0.0003240433234625656, "9": 6.917473076481784e-05} |
| Raw goal margin distribution | {"-1": 0.12496406647415334, "-10": 5.576736294243833e-08, "-11": 5.68301346582048e-09, "-12": 5.322049804116441e-10, "-13": 4.6096943131377924e-11, "-14": 3.712006313648992e-12, "-15": 2.7722806017934733e-13, "-16": 1.731980157605099e-14, "-2": 0.05782142699971286, "-3": 0.01878797826841989, "-4": 0.004845936176424589, "-5": 0.0010312836900410011, "-6": 0.00018632109474121073, "-7": 2.9201723802568232e-05, "-8": 4.0375250717213204e-06, "-9": 4.991102277075397e-07, "0": 0.23522907514359268, "1": 0.22229989956761909, "10": 1.3152603656397013e-05, "11": 2.3145868005867658e-06, "12": 3.7431470079992105e-07, "13": 5.5987778856364584e-08, "14": 7.785616015809613e-09, "15": 1.0041177008443644e-09, "16": 1.0833118943332107e-10, "2": 0.17243091410442551, "3": 0.09675413543091195, "4": 0.043095342814171066, "5": 0.015837767443459123, "6": 0.004941297497995022, "7": 0.0013373670725399605, "8": 0.0003193158908272304, "9": 6.816554817693494e-05} |
| Unadjusted home-win probability | 55.7% |
| Unadjusted draw probability | 23.5% |
| Unadjusted away-win probability | 20.8% |
| Raw p over 1 5 | 82.5% |
| Raw p under 3 5 | 62.3% |
| Raw p btts yes | 59.4% |
| P home draw | 79.3% |
| P draw away | 43.5% |
| P home away | 77.2% |
| Raw p home draw | 79.2% |
| Raw p draw away | 44.3% |
| Raw p home away | 76.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:11:34Z", "line": 0.75, "market_key": "spreads", "opposite_price": 1.84, "price": 2.02, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:10:44Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.82, "price": 1.51, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:10:44Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.51, "price": 2.82, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:11:34Z", "line": -0.75, "market_key": "spreads", "opposite_price": 2.02, "price": 1.84, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 1.71 |
| Reference draw odds | 4.30 |
| Reference away odds | 4.60 |
| Market reference 1x2 last update utc | 2026-10-21T17:11:38Z |
| Market reference home last update utc | 2026-10-21T17:11:38Z |
| Market reference draw last update utc | 2026-10-21T17:11:38Z |
| Market reference away last update utc | 2026-10-21T17:11:38Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.44 |
| Reference Under 2.5 odds | 2.62 |
| Market reference over 2 5 last update utc | 2026-10-21T17:11:33Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:11:33Z |
| Home probability edge | -0.8% |
| Draw probability edge | +0.7% |
| Away probability edge | +0.1% |
| Over 2.5 probability edge | -5.9% |
| Under 2.5 probability edge | +5.9% |
| Raw edge prob home | -0.0165 |
| Raw ev home | -0.0696 |
| Raw edge prob draw | 0.0146 |
| Raw ev draw | 0.0374 |
| Raw edge prob away | 0.0019 |
| Raw ev away | -0.0862 |

</details>


---
